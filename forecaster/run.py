#!/usr/bin/env python3
"""Hourly crypto forecaster (FORECASTING ONLY - no trading, no API keys, public market data only).

Durable store: append-only JSONL files under data/ (committed to git each run, so history is
immutable and versioned). Every record is keyed by asset. Uniqueness (asset + forecast_hour) is
enforced on load + insert; existing lines are never rewritten (append-only guard verifies this).
"""
import json, math, os, sys, time, uuid, argparse, statistics, traceback, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
MODEL_VERSION = "heuristic-v1"
ASSETS = {  # asset -> Kraken public pair (verified via /0/public/AssetPairs)
    "BTC": "XBTUSD",
    "ETH": "ETHUSD",
    "SOL": "SOLUSD",
    "HYPE": "HYPEUSD",
}
KRAKEN = "https://api.kraken.com/0/public"
SOURCE = "Kraken public REST (Ticker + OHLC interval=60)"
STALE_SECONDS = 180  # spot ticker older than this (vs. last trade) is treated as stale

def now_utc():
    return datetime.now(timezone.utc)

def et_str(dt):
    return dt.astimezone(ET).isoformat(timespec="seconds")

def hour_floor(dt):
    e = dt.astimezone(ET)
    return e.replace(minute=0, second=0, microsecond=0)

# ---------------- storage (append-only JSONL) ----------------
def path(table, asset=None):
    if asset:
        return os.path.join(DATA, table, f"{asset}.jsonl")
    return os.path.join(DATA, f"{table}.jsonl")

def load(table, asset=None):
    p = path(table, asset)
    if not os.path.exists(p):
        return []
    with open(p) as f:
        return [json.loads(l) for l in f if l.strip()]

def append(table, rec, asset=None):
    p = path(table, asset)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "a") as f:
        f.write(json.dumps(rec, sort_keys=True) + "\n")
        f.flush(); os.fsync(f.fileno())

# ---------------- HTTP with retry/backoff ----------------
def get_json(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "samuel-forecaster/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                j = json.loads(r.read().decode())
            if j.get("error"):
                raise RuntimeError(f"Kraken error: {j['error']}")
            return j
        except Exception as e:
            last = e
            time.sleep(min(2 ** i, 10))
    raise RuntimeError(f"GET {url} failed after {tries} tries: {last}")

def kraken_result(j):
    res = j["result"]
    keys = [k for k in res if k != "last"]
    return res[keys[0]], res.get("last")

def fetch_spot(pair):
    j = get_json(f"{KRAKEN}/Ticker?pair={pair}")
    t, _ = kraken_result(j)
    return {"last": float(t["c"][0]), "bid": float(t["b"][0]), "ask": float(t["a"][0]),
            "vol24h": float(t["v"][1]), "fetched_at_utc": now_utc().isoformat(timespec="seconds")}

def fetch_ohlc(pair):
    j = get_json(f"{KRAKEN}/OHLC?pair={pair}&interval=60")
    rows, last = kraken_result(j)
    candles = [{"t": int(r[0]), "o": float(r[1]), "h": float(r[2]), "l": float(r[3]), "c": float(r[4]),
                "vwap": float(r[5]), "v": float(r[6]), "n": int(r[7])} for r in rows]
    return candles, last

def fetch_last_trade_time(pair):
    j = get_json(f"{KRAKEN}/Trades?pair={pair}&count=1")
    trades, _ = kraken_result(j)
    return float(trades[-1][2]) if trades else None

# ---------------- indicators + model ----------------
def ema(vals, n):
    k = 2 / (n + 1); e = vals[0]
    for v in vals[1:]:
        e = v * k + e * (1 - k)
    return e

def rsi(closes, n=14):
    gains, losses = [], []
    for a, b in zip(closes[-n-1:-1], closes[-n:]):
        d = b - a; gains.append(max(d, 0)); losses.append(max(-d, 0))
    ag, al = sum(gains) / n, sum(losses) / n
    if al == 0:
        return 100.0
    return 100 - 100 / (1 + ag / al)

def atr(c, n=14):
    trs = []
    for i in range(len(c) - n, len(c)):
        prev = c[i - 1]["c"]
        trs.append(max(c[i]["h"] - c[i]["l"], abs(c[i]["h"] - prev), abs(c[i]["l"] - prev)))
    return sum(trs) / n

def build_forecast(completed, start_price):
    closes = [x["c"] for x in completed]
    rets = [math.log(b / a) for a, b in zip(closes[:-1], closes[1:])]
    vol_h = statistics.pstdev(rets[-24:]) or 1e-4             # realized hourly vol (24h)
    atr14 = atr(completed, 14); atr_pct = atr14 / closes[-1]
    e9, e21 = ema(closes[-60:], 9), ema(closes[-60:], 21)
    trend = (e9 - e21) / e21
    r1 = rets[-1]; r3 = math.log(closes[-1] / closes[-4]); r24 = math.log(closes[-1] / closes[-25])
    rs = rsi(closes, 14)
    vols = [x["v"] for x in completed]
    vol_ratio = vols[-1] / (statistics.mean(vols[-25:-1]) or 1e-9)
    last = completed[-1]
    mom_w = 1.3 if vol_ratio > 1.5 else 1.0
    exp_ret = mom_w * (0.10 * r1 + 0.04 * r3) + 0.15 * trend
    factors = []
    if rs > 70:
        exp_ret -= 0.25 * vol_h; factors.append(f"RSI {rs:.0f} overbought -> mean-reversion drag")
    elif rs < 30:
        exp_ret += 0.25 * vol_h; factors.append(f"RSI {rs:.0f} oversold -> mean-reversion lift")
    else:
        factors.append(f"RSI {rs:.0f} neutral")
    # spot drift since the last completed candle close
    drift = math.log(start_price / last["c"])
    exp_ret = max(-0.5 * vol_h, min(0.5 * vol_h, exp_ret))
    factors.append(f"EMA9 {'above' if trend > 0 else 'below'} EMA21 ({trend*100:+.3f}%)")
    factors.append(f"last hour {r1*100:+.2f}%, 3h {r3*100:+.2f}%, 24h {r24*100:+.2f}%")
    factors.append(f"last-hour volume {vol_ratio:.2f}x 24h avg" + (" (confirms move)" if vol_ratio > 1.5 else ""))
    factors.append(f"realized hourly vol {vol_h*100:.2f}%, ATR14 {atr_pct*100:.2f}%")
    band = 0.25 * vol_h
    direction = "UP" if exp_ret > band else "DOWN" if exp_ret < -band else "SIDEWAYS"
    conf = 0.5
    if (trend > 0) == (r3 > 0):
        conf += 0.1
    if vol_ratio > 1.5:
        conf += 0.05
    if (rs > 70 and direction == "UP") or (rs < 30 and direction == "DOWN"):
        conf -= 0.1
    if direction == "SIDEWAYS":
        conf = 0.5 + (0.1 if abs(trend) < vol_h * 0.2 else 0)
    conf = round(max(0.3, min(0.75, conf)), 2)
    pred = start_price * math.exp(exp_ret)
    half = max(vol_h, atr_pct * 0.8) * start_price
    return {
        "predicted_price": round(pred, 6), "predicted_low": round(pred - half, 6),
        "predicted_high": round(pred + half, 6), "direction": direction, "confidence": conf,
        "sideways_band_pct": round(band * 100, 5), "expected_return_pct": round(exp_ret * 100, 5),
        "main_factors": factors,
        "indicators": {"ema9": e9, "ema21": e21, "rsi14": rs, "atr14": atr14, "atr_pct": atr_pct * 100,
                       "realized_vol_1h_pct": vol_h * 100, "ret_1h_pct": r1 * 100, "ret_3h_pct": r3 * 100,
                       "ret_24h_pct": r24 * 100, "volume_last_hour": last["v"], "volume_ratio": vol_ratio,
                       "spot_drift_since_close_pct": drift * 100},
    }

# ---------------- run ----------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trigger", default="manual")
    ap.add_argument("--gh-run", default="")
    a = ap.parse_args()
    started = now_utc()
    H = hour_floor(started)                 # forecast hour (ET) = the hour in progress
    Hkey = H.isoformat(timespec="minutes")
    run_id = f"{started.strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:6]}"
    run = {"run_id": run_id, "trigger": a.trigger, "github_run_id": a.gh_run,
           "started_at_et": et_str(started), "started_at_utc": started.isoformat(timespec="seconds"),
           "forecast_hour_et": Hkey, "minutes_after_hour": round((started - H).total_seconds() / 60, 2),
           "forecasts_created": [], "duplicates_skipped": [], "scores_created": 0, "gaps": [], "errors": []}
    gaps_existing = {(g["asset"], g["hour_et"], g["kind"]) for g in load("gaps")}

    def gap(asset, hour, kind, detail):
        run["gaps"].append(f"{asset}:{kind}")
        if (asset, hour, kind) in gaps_existing:
            return
        gaps_existing.add((asset, hour, kind))
        append("gaps", {"asset": asset, "hour_et": hour, "kind": kind, "detail": detail,
                        "logged_at_et": et_str(now_utc()), "run_id": run_id})

    for asset, pair in ASSETS.items():
        try:
            forecasts = load("forecasts", asset)
            have = {f["forecast_hour_et"]: f for f in forecasts}
            scored = {s["forecast_hour_et"] for s in load("scores", asset)}
            have_actual = {x["hour_et"] for x in load("actuals", asset)}
            candles, _ = fetch_ohlc(pair)
            by_t = {c["t"]: c for c in candles}
            # ---- 1. score any forecast whose hour has ended (catch-up included) ----
            for fh, f in sorted(have.items()):
                if fh in scored:
                    continue
                hstart = datetime.fromisoformat(fh)
                if now_utc() < hstart + timedelta(hours=1, seconds=30):
                    continue
                c = by_t.get(int(hstart.timestamp()))
                if not c:
                    gap(asset, fh, "actual_unavailable", "completed candle not returned by Kraken OHLC")
                    continue
                if fh not in have_actual:
                    append("actuals", {"asset": asset, "pair": pair, "hour_et": fh, "open": c["o"], "high": c["h"],
                                       "low": c["l"], "close": c["c"], "volume": c["v"], "vwap": c["vwap"],
                                       "trades": c["n"], "data_source": SOURCE + f" pair={pair}",
                                       "fetched_at_et": et_str(now_utc())}, asset)
                    have_actual.add(fh)
                actual = c["c"]; start = f["start_price"]
                err = f["predicted_price"] - actual
                move_pct = (actual - start) / start * 100
                band = f["sideways_band_pct"]
                act_dir = "UP" if move_pct > band else "DOWN" if move_pct < -band else "SIDEWAYS"
                append("scores", {"asset": asset, "forecast_hour_et": fh, "forecast_id": f["forecast_id"],
                                  "start_price": start, "predicted_price": f["predicted_price"],
                                  "actual_close": actual, "actual_high": c["h"], "actual_low": c["l"],
                                  "dollar_error": round(err, 6), "abs_dollar_error": round(abs(err), 6),
                                  "pct_error": round(err / actual * 100, 6), "abs_pct_error": round(abs(err) / actual * 100, 6),
                                  "predicted_direction": f["direction"], "actual_direction": act_dir,
                                  "actual_move_pct": round(move_pct, 5), "direction_correct": act_dir == f["direction"],
                                  "close_in_predicted_range": f["predicted_low"] <= actual <= f["predicted_high"],
                                  "data_source": SOURCE + f" pair={pair}", "scored_at_et": et_str(now_utc()),
                                  "run_id": run_id}, asset)
                scored.add(fh); run["scores_created"] += 1
            # ---- 2. log missed hours (last 48h, after first forecast) ----
            if forecasts:
                first = datetime.fromisoformat(min(have))
                h = max(first, H - timedelta(hours=48))
                while h < H:
                    k = h.astimezone(ET).isoformat(timespec="minutes")
                    if k not in have:
                        gap(asset, k, "missed_run", "no forecast recorded for this hour (scheduler did not run in time)")
                    h += timedelta(hours=1)
            # ---- 3. forecast the current hour (idempotent: one per asset+hour) ----
            if Hkey in have:
                run["duplicates_skipped"].append(asset); continue
            spot = fetch_spot(pair)
            ltt = fetch_last_trade_time(pair)
            completed = [c for c in candles if c["t"] + 3600 <= started.timestamp()]
            if not completed or completed[-1]["t"] != int((H - timedelta(hours=1)).timestamp()):
                gap(asset, Hkey, "stale_candle", f"latest completed candle is {et_str(datetime.fromtimestamp(completed[-1]['t'], timezone.utc)) if completed else None}, expected {et_str(H - timedelta(hours=1))}")
                continue
            if ltt is None or started.timestamp() - ltt > STALE_SECONDS * 20:
                gap(asset, Hkey, "stale_spot", f"last trade at {ltt}")
                continue
            if len(completed) < 60:
                gap(asset, Hkey, "insufficient_history", f"{len(completed)} candles"); continue
            fc = build_forecast(completed, spot["last"])
            lc = completed[-1]
            rec = {"forecast_id": f"{asset}-{Hkey}", "asset": asset, "pair": pair, "forecast_hour_et": Hkey,
                   "target_time_et": (H + timedelta(hours=1)).isoformat(timespec="minutes"),
                   "created_at_et": et_str(now_utc()), "run_id": run_id, "model_version": MODEL_VERSION,
                   "start_price": spot["last"], "spot": spot,
                   "spot_last_trade_et": et_str(datetime.fromtimestamp(ltt, timezone.utc)),
                   "last_completed_candle": {"hour_et": et_str(datetime.fromtimestamp(lc["t"], timezone.utc)),
                                             "open": lc["o"], "high": lc["h"], "low": lc["l"], "close": lc["c"],
                                             "volume": lc["v"], "vwap": lc["vwap"], "trades": lc["n"]},
                   "data_source": SOURCE + f" pair={pair}", **fc}
            append("forecasts", rec, asset)
            run["forecasts_created"].append(asset)
        except Exception as e:
            run["errors"].append(f"{asset}: {e}")
            gap(asset, Hkey, "feed_unavailable", str(e)[:300])
    ended = now_utc()
    run["ended_at_et"] = et_str(ended)
    run["duration_s"] = round((ended - started).total_seconds(), 2)
    run["status"] = ("ok" if not run["errors"] and not [g for g in run["gaps"] if not g.endswith("missed_run")]
                     else "partial" if len(run["errors"]) < len(ASSETS) else "failed")
    append("scheduler_runs", run)
    export_dashboard()
    print(json.dumps(run, indent=1))
    return 0 if run["status"] != "failed" else 1

# ---------------- dashboard export ----------------
def metrics(scores):
    if not scores:
        return {"n": 0}
    return {"n": len(scores),
            "mae_usd": statistics.mean(s["abs_dollar_error"] for s in scores),
            "mae_pct": statistics.mean(s["abs_pct_error"] for s in scores),
            "directional_accuracy": sum(s["direction_correct"] for s in scores) / len(scores),
            "range_hit_rate": sum(s["close_in_predicted_range"] for s in scores) / len(scores)}

def export_dashboard():
    now = now_utc()
    out = {"generated_at_et": et_str(now), "model_version": MODEL_VERSION, "assets": {},
           "scheduler": {"platform": "GitHub Actions scheduled workflow `hourly-forecast` in repo samuelkreitl-wq/crypto-hourly-forecaster",
                         "cron_utc": ["0 * * * *", "10 * * * *", "25 * * * *", "45 * * * *"],
                         "note": "Primary trigger at minute 00 every hour (00 UTC == 00 ET, whole-hour offset). Backup triggers at :10/:25/:45 recover late/dropped runs; duplicates are skipped by the asset+hour key.",
                         "timezone_of_records": "America/New_York"}}
    windows = {"24h": 24, "7d": 168, "30d": 720}
    combined = {w: [] for w in windows}
    for asset in ASSETS:
        fs = load("forecasts", asset)
        sc = {s["forecast_hour_et"]: s for s in load("scores", asset)}
        rows = []
        for f in fs[-720:]:
            s = sc.get(f["forecast_hour_et"])
            rows.append({k: f[k] for k in ("forecast_hour_et", "target_time_et", "created_at_et", "start_price",
                                           "predicted_price", "predicted_low", "predicted_high", "direction",
                                           "confidence", "data_source")} |
                        ({"actual_close": s["actual_close"], "dollar_error": s["dollar_error"], "pct_error": s["pct_error"],
                          "actual_direction": s["actual_direction"], "direction_correct": s["direction_correct"],
                          "in_range": s["close_in_predicted_range"]} if s else {}))
        m = {}
        for w, hrs in windows.items():
            sel = [s for s in sc.values() if datetime.fromisoformat(s["forecast_hour_et"]) >= now - timedelta(hours=hrs)]
            m[w] = metrics(sel); combined[w] += sel
        latest = fs[-1] if fs else None
        out["assets"][asset] = {"pair": ASSETS[asset], "latest_forecast": latest, "metrics": m, "history": rows}
    out["combined_metrics"] = {w: metrics(v) | ({"mae_usd_note": "mixes assets with very different prices; prefer MAE %"} if v else {}) for w, v in combined.items()}
    out["scheduler_runs"] = load("scheduler_runs")[-200:]
    out["gaps"] = load("gaps")[-200:]
    with open(os.path.join(DATA, "dashboard.json"), "w") as f:
        json.dump(out, f)
    write_readme(out)

def _p(v, a):
    if v is None:
        return "—"
    return f"${v:,.4f}" if a == "HYPE" or v < 10 else f"${v:,.2f}"

def write_readme(out):
    """Auto-generated dashboard rendered by GitHub on the repo home page (regenerated every run)."""
    L = ["# Hourly crypto forecaster: BTC · ETH · SOL · HYPE", "",
         "> This is for forecasting and measurement only. It uses Kraken's public market data and places no trades. "
         "It holds no API keys and spends nothing. All times are Eastern (America/New_York). "
         "This page is regenerated automatically on every scheduler run.", "",
         f"**Last updated:** {out['generated_at_et']} · **Interactive dashboard:** "
         "[open it here](https://htmlpreview.github.io/?https://github.com/samuelkreitl-wq/crypto-hourly-forecaster/blob/main/docs/index.html)", "",
         "## Latest forecasts", "",
         "| Asset | Kraken spot at run | Spot time (ET) | Forecast close at | Predicted | Range (low–high) | Direction | Confidence | Main factors |",
         "|---|---|---|---|---|---|---|---|---|"]
    for a, x in out["assets"].items():
        f = x["latest_forecast"]
        if not f:
            L.append(f"| {a} | — | — | — | — | — | — | — | no forecast yet |"); continue
        L.append(f"| **{a}** | {_p(f['start_price'], a)} | {f['spot_last_trade_et'].replace('T', ' ')} | {f['target_time_et'].replace('T', ' ')} | "
                 f"**{_p(f['predicted_price'], a)}** | {_p(f['predicted_low'], a)} – {_p(f['predicted_high'], a)} | {f['direction']} | "
                 f"{f['confidence']*100:.0f}% | {'; '.join(f['main_factors'][:3])} |")
    L += ["", "## Accuracy (scored forecasts only)", "",
          "| Asset | Window | Scored | MAE $ | MAE % | Direction hit rate | Close inside range |", "|---|---|---|---|---|---|---|"]
    for a in list(out["assets"]) + ["Combined"]:
        m = out["combined_metrics"] if a == "Combined" else out["assets"][a]["metrics"]
        for w in ("24h", "7d", "30d"):
            z = m[w]
            if not z.get("n"):
                L.append(f"| {a} | {w} | 0 | — | — | — | — |"); continue
            mae = "(mixed assets)" if a == "Combined" else _p(z["mae_usd"], a)
            L.append(f"| {a} | {w} | {z['n']} | {mae} | {z['mae_pct']:.3f}% | {z['directional_accuracy']*100:.1f}% | {z['range_hit_rate']*100:.1f}% |")
    L += ["", "## Predicted vs actual (last 48 scored hours)", ""]
    for a, x in out["assets"].items():
        rows = [r for r in x["history"] if "actual_close" in r][-48:]
        if len(rows) < 2:
            L.append(f"**{a}:** the chart appears once at least 2 forecasts are scored ({len(rows)} so far)."); L.append(""); continue
        lab = ", ".join('"' + r["forecast_hour_et"][11:16] + '"' for r in rows)
        vals = [r["predicted_price"] for r in rows] + [r["actual_close"] for r in rows]
        L += ["```mermaid", "xychart-beta", f'    title "{a}: predicted (line 1) vs actual (line 2) close"', f"    x-axis [{lab}]",
              f"    y-axis \"USD\" {min(vals)*0.999:.4f} --> {max(vals)*1.001:.4f}",
              "    line [" + ", ".join(f"{r['predicted_price']:.4f}" for r in rows) + "]",
              "    line [" + ", ".join(f"{r['actual_close']:.4f}" for r in rows) + "]", "```", ""]
    L += ["## Recent forecasts with scores", "",
          "| Asset | Hour (ET) | Start | Predicted | Range | Dir | Actual close | $ error | % error | Dir correct |", "|---|---|---|---|---|---|---|---|---|---|"]
    allrows = sorted(((a, r) for a, x in out["assets"].items() for r in x["history"]), key=lambda t: t[1]["forecast_hour_et"], reverse=True)[:40]
    for a, r in allrows:
        sc = "actual_close" in r
        L.append(f"| {a} | {r['forecast_hour_et'].replace('T', ' ')} | {_p(r['start_price'], a)} | {_p(r['predicted_price'], a)} | "
                 f"{_p(r['predicted_low'], a)}–{_p(r['predicted_high'], a)} | {r['direction']} | {_p(r.get('actual_close'), a) if sc else 'pending'} | " +
                 (("%+.4f" % r["dollar_error"]) if sc else "—") + " | " + (("%+.3f%%" % r["pct_error"]) if sc else "—") + " | " + 
                 f"{('yes' if r['direction_correct'] else 'no') if sc else 'pending'} |")
    s = out["scheduler"]
    L += ["", "## Scheduler", "", f"- Platform: {s['platform']}", f"- Cron (UTC): `{' | '.join(s['cron_utc'])}`", f"- {s['note']}",
          "- Config: [.github/workflows/hourly.yml](.github/workflows/hourly.yml) · Raw run log: [data/scheduler_runs.jsonl](data/scheduler_runs.jsonl)", "",
          "| Started (ET) | Trigger | Min after :00 | Status | New forecasts | Duplicates skipped | Scored | Gaps/errors |", "|---|---|---|---|---|---|---|---|"]
    for r in out["scheduler_runs"][::-1][:25]:
        L.append(f"| {r['started_at_et'].replace('T', ' ')} | {r['trigger']} | {r['minutes_after_hour']} | {r['status']} | {','.join(r['forecasts_created']) or '—'} | "
                 f"{','.join(r['duplicates_skipped']) or '—'} | {r['scores_created']} | {len(r['gaps'])}{' / ' + '; '.join(r['errors']) if r['errors'] else ''} |")
    L += ["", "## Data gaps, missed runs and errors", ""]
    if out["gaps"]:
        L += ["| Asset | Hour (ET) | Kind | Detail | Logged (ET) |", "|---|---|---|---|---|"]
        for g in out["gaps"][::-1][:30]:
            L.append(f"| {g['asset']} | {g['hour_et']} | {g['kind']} | {g['detail']} | {g['logged_at_et']} |")
    else:
        L.append("No gaps logged.")
    L += ["", "## How it works", "",
          "Every run checks each asset (Kraken pairs XBTUSD, ETHUSD, SOLUSD and HYPEUSD) in four steps:",
          "1. It scores any earlier forecast whose hour has ended, using that hour's completed Kraken candle close. Missed scoring is caught up on the next run.",
          "2. It logs any hour from the past 48 that has no forecast as `missed_run`.",
          "3. If no forecast exists yet for the current ET hour, it fetches Kraken spot, the latest trade time and hourly OHLC. It computes EMA9/21, RSI14, ATR14, realized volatility, momentum and a volume ratio, then saves the forecast for the close at the next :00.",
          "4. If an asset's feed is unavailable or stale, it logs a gap for that asset only and still forecasts the others.",
          "",
          "Records are append-only JSONL in `data/`, keyed by asset. Every run is a git commit, and the workflow fails if any existing line changes. The model is a transparent heuristic (`heuristic-v1`), not financial advice."]
    with open(os.path.join(ROOT, "README.md"), "w") as f:
        f.write("\n".join(L) + "\n")

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc(); sys.exit(1)

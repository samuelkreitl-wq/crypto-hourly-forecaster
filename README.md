# Hourly crypto forecaster: BTC · ETH · SOL · HYPE

> This is for forecasting and measurement only. It uses Kraken's public market data and places no trades. It holds no API keys and spends nothing. All times are Eastern (America/New_York). This page is regenerated automatically on every scheduler run.

**Last updated:** 2026-11-18T20:14:18-05:00 · **Interactive dashboard:** [open it here](https://htmlpreview.github.io/?https://github.com/samuelkreitl-wq/crypto-hourly-forecaster/blob/main/docs/index.html)

## Latest forecasts

| Asset | Kraken spot at run | Spot time (ET) | Forecast close at | Predicted | Range (low–high) | Direction | Confidence | Main factors |
|---|---|---|---|---|---|---|---|---|
| **BTC** | $63,077.50 | 2026-11-18 20:11:24-05:00 | 2026-11-18 21:00-05:00 | **$63,060.37** | $62,571.93 – $63,548.82 | SIDEWAYS | 50% | RSI 35 neutral; EMA9 below EMA21 (-0.694%); last hour +0.22%, 3h +1.38%, 24h -2.50% |
| **ETH** | $1,783.35 | 2026-11-18 20:11:23-05:00 | 2026-11-18 21:00-05:00 | **$1,783.65** | $1,766.83 – $1,800.47 | SIDEWAYS | 50% | RSI 42 neutral; EMA9 below EMA21 (-0.501%); last hour +0.46%, 3h +1.16%, 24h -1.98% |
| **SOL** | $73.53 | 2026-11-18 20:11:24-05:00 | 2026-11-18 21:00-05:00 | **$73.53** | $72.83 – $74.24 | SIDEWAYS | 50% | RSI 41 neutral; EMA9 below EMA21 (-0.303%); last hour +0.10%, 3h +1.04%, 24h -1.74% |
| **HYPE** | $67.0600 | 2026-11-18 20:11:25-05:00 | 2026-11-18 21:00-05:00 | **$67.0484** | $66.1854 – $67.9115 | SIDEWAYS | 50% | RSI 40 neutral; EMA9 below EMA21 (-0.767%); last hour +0.33%, 3h +1.62%, 24h -3.37% |

## Accuracy (scored forecasts only)

| Asset | Window | Scored | MAE $ | MAE % | Direction hit rate | Close inside range |
|---|---|---|---|---|---|---|
| BTC | 24h | 0 | — | — | — | — |
| BTC | 7d | 0 | — | — | — | — |
| BTC | 30d | 0 | — | — | — | — |
| ETH | 24h | 0 | — | — | — | — |
| ETH | 7d | 0 | — | — | — | — |
| ETH | 30d | 0 | — | — | — | — |
| SOL | 24h | 0 | — | — | — | — |
| SOL | 7d | 0 | — | — | — | — |
| SOL | 30d | 0 | — | — | — | — |
| HYPE | 24h | 0 | — | — | — | — |
| HYPE | 7d | 0 | — | — | — | — |
| HYPE | 30d | 0 | — | — | — | — |
| Combined | 24h | 0 | — | — | — | — |
| Combined | 7d | 0 | — | — | — | — |
| Combined | 30d | 0 | — | — | — | — |

## Predicted vs actual (last 48 scored hours)

**BTC:** the chart appears once at least 2 forecasts are scored (0 so far).

**ETH:** the chart appears once at least 2 forecasts are scored (0 so far).

**SOL:** the chart appears once at least 2 forecasts are scored (0 so far).

**HYPE:** the chart appears once at least 2 forecasts are scored (0 so far).

## Recent forecasts with scores

| Asset | Hour (ET) | Start | Predicted | Range | Dir | Actual close | $ error | % error | Dir correct |
|---|---|---|---|---|---|---|---|---|---|
| BTC | 2026-11-18 20:00-05:00 | $63,077.50 | $63,060.37 | $62,571.93–$63,548.82 | SIDEWAYS | pending | — | — | pending |
| ETH | 2026-11-18 20:00-05:00 | $1,783.35 | $1,783.65 | $1,766.83–$1,800.47 | SIDEWAYS | pending | — | — | pending |
| SOL | 2026-11-18 20:00-05:00 | $73.53 | $73.53 | $72.83–$74.24 | SIDEWAYS | pending | — | — | pending |
| HYPE | 2026-11-18 20:00-05:00 | $67.0600 | $67.0484 | $66.1854–$67.9115 | SIDEWAYS | pending | — | — | pending |

## Scheduler

- Platform: GitHub Actions scheduled workflow `hourly-forecast` in repo samuelkreitl-wq/crypto-hourly-forecaster
- Cron (UTC): `0 * * * * | 10 * * * * | 25 * * * * | 45 * * * *`
- Primary trigger at minute 00 every hour (00 UTC == 00 ET, whole-hour offset). Backup triggers at :10/:25/:45 recover late/dropped runs; duplicates are skipped by the asset+hour key.
- Config: [.github/workflows/hourly.yml](.github/workflows/hourly.yml) · Raw run log: [data/scheduler_runs.jsonl](data/scheduler_runs.jsonl)

| Started (ET) | Trigger | Min after :00 | Status | New forecasts | Duplicates skipped | Scored | Gaps/errors |
|---|---|---|---|---|---|---|---|
| 2026-11-18 20:14:17-05:00 | workflow_dispatch:verify-duplicate-prevention | 14.3 | ok | — | BTC,ETH,SOL,HYPE | 0 | 0 |
| 2026-11-18 20:11:27-05:00 | workflow_dispatch:initial-verification | 11.46 | ok | BTC,ETH,SOL,HYPE | — | 0 | 0 |

## Data gaps, missed runs and errors

No gaps logged.

## How it works

Every run checks each asset (Kraken pairs XBTUSD, ETHUSD, SOLUSD and HYPEUSD) in four steps:
1. It scores any earlier forecast whose hour has ended, using that hour's completed Kraken candle close. Missed scoring is caught up on the next run.
2. It logs any hour from the past 48 that has no forecast as `missed_run`.
3. If no forecast exists yet for the current ET hour, it fetches Kraken spot, the latest trade time and hourly OHLC. It computes EMA9/21, RSI14, ATR14, realized volatility, momentum and a volume ratio, then saves the forecast for the close at the next :00.
4. If an asset's feed is unavailable or stale, it logs a gap for that asset only and still forecasts the others.

Records are append-only JSONL in `data/`, keyed by asset. Every run is a git commit, and the workflow fails if any existing line changes. The model is a transparent heuristic (`heuristic-v1`), not financial advice.

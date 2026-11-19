# Crypto hourly forecaster (BTC, ETH, SOL, HYPE)

**Forecasting and measurement only.** Uses only Kraken's public market-data endpoints. No API keys, no trading, no spending.

- **Scheduler:** GitHub Actions `.github/workflows/hourly.yml`, cron `0 * * * *` with backup ticks at :10/:25/:45. A `concurrency` run lock, plus a unique `asset + forecast_hour` key, prevents duplicate forecasts.
- **Every run:** for each asset it pulls Kraken Ticker (spot), Trades (freshness) and OHLC interval=60. It scores any forecast whose hour has ended (with catch-up), logs missed hours, then forecasts the current hour: start price, predicted close at the next :00, ~1-sigma range, UP/DOWN/SIDEWAYS, confidence and factors.
- **Database:** append-only JSONL under `data/`, keyed by asset (`forecasts/`, `actuals/`, `scores/`), plus `scheduler_runs.jsonl` and `gaps.jsonl`. Every run is a git commit, so history is versioned. `append_only_guard.sh` fails the run if any existing line changes.
- **Dashboard:** a Vercel project that reads `data/dashboard.json` plus live Kraken prices through a proxy.
- All timestamps are America/New_York.

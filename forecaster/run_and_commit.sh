#!/usr/bin/env bash
# One forecaster execution + durable commit. Safe to run concurrently with other triggers:
# on a push race it resets to the latest origin/main and re-runs; run.py skips any asset+hour
# that already has a forecast, so a forecast hour can never be recorded twice.
# FORECASTING ONLY: public Kraken market data, no keys, no trading.
set -uo pipefail
TRIGGER="${1:-manual}"; GHRUN="${2:-}"
git config user.name "forecaster-bot"
git config user.email "forecaster-bot@users.noreply.github.com"
for attempt in 1 2 3 4 5; do
  git fetch -q origin main && git reset -q --hard origin/main
  ok=0
  for t in 1 2 3; do
    python3 forecaster/run.py --trigger "$TRIGGER" --gh-run "$GHRUN" && { ok=1; break; }
    echo "forecaster attempt $t failed; backing off"; sleep $((t*20))
  done
  bash forecaster/append_only_guard.sh || { echo "append-only guard failed"; exit 1; }
  git add data README.md
  git commit -q -m "forecast run $(TZ=America/New_York date '+%Y-%m-%d %H:%M:%S %Z') [$TRIGGER]" || { echo "nothing to commit"; exit 0; }
  if git push -q origin HEAD:main; then echo "pushed (ok=$ok)"; exit 0; fi
  echo "push race on attempt $attempt; resetting to origin/main and re-running"; sleep $((attempt*3))
done
exit 1

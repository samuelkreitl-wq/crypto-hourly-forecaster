# Hourly crypto forecaster: BTC · ETH · SOL · HYPE

> This is for forecasting and measurement only. It uses Kraken's public market data and places no trades. It holds no API keys and spends nothing. All times are Eastern (America/New_York). This page is regenerated automatically on every scheduler run.

**Last updated:** 2026-11-20T14:00:41-05:00 · **Interactive dashboard:** [open it here](https://samuelkreitl-wq.github.io/crypto-hourly-forecaster/)

## Latest forecasts

| Asset | Kraken spot at run | Spot time (ET) | Forecast close at | Predicted | Range (low–high) | Direction | Confidence | Main factors |
|---|---|---|---|---|---|---|---|---|
| **BTC** | $58,322.60 | 2026-11-20 14:00:39-05:00 | 2026-11-20 15:00-05:00 | **$58,172.50** | $57,547.78 – $58,797.21 | DOWN | 55% | RSI 23 oversold -> mean-reversion lift; EMA9 below EMA21 (-1.567%); last hour -1.29%, 3h -1.81%, 24h -7.40% |
| **ETH** | $1,615.47 | 2026-11-20 14:00:39-05:00 | 2026-11-20 15:00-05:00 | **$1,612.21** | $1,589.70 – $1,634.71 | SIDEWAYS | 50% | RSI 24 oversold -> mean-reversion lift; EMA9 below EMA21 (-2.118%); last hour -0.90%, 3h -2.38%, 24h -9.51% |
| **SOL** | $68.79 | 2026-11-20 14:00:39-05:00 | 2026-11-20 15:00-05:00 | **$68.58** | $67.72 – $69.44 | DOWN | 55% | RSI 30 neutral; EMA9 below EMA21 (-1.674%); last hour -0.65%, 3h +0.69%, 24h -7.33% |
| **HYPE** | $61.2300 | 2026-11-20 14:00:36-05:00 | 2026-11-20 15:00-05:00 | **$61.1765** | $60.2477 – $62.1053 | SIDEWAYS | 50% | RSI 24 oversold -> mean-reversion lift; EMA9 below EMA21 (-2.418%); last hour +0.11%, 3h -0.57%, 24h -11.59% |

## Accuracy (scored forecasts only)

| Asset | Window | Scored | MAE $ | MAE % | Direction hit rate | Close inside range |
|---|---|---|---|---|---|---|
| BTC | 24h | 23 | $431.43 | 0.709% | 8.7% | 78.3% |
| BTC | 7d | 35 | $366.59 | 0.598% | 11.4% | 77.1% |
| BTC | 30d | 35 | $366.59 | 0.598% | 11.4% | 77.1% |
| ETH | 24h | 23 | $13.48 | 0.787% | 21.7% | 78.3% |
| ETH | 7d | 35 | $11.39 | 0.659% | 20.0% | 80.0% |
| ETH | 30d | 35 | $11.39 | 0.659% | 20.0% | 80.0% |
| SOL | 24h | 23 | $0.5969 | 0.840% | 30.4% | 73.9% |
| SOL | 7d | 35 | $0.5177 | 0.722% | 34.3% | 77.1% |
| SOL | 30d | 35 | $0.5177 | 0.722% | 34.3% | 77.1% |
| HYPE | 24h | 23 | $0.6561 | 1.017% | 21.7% | 82.6% |
| HYPE | 7d | 35 | $0.5841 | 0.893% | 25.7% | 80.0% |
| HYPE | 30d | 35 | $0.5841 | 0.893% | 25.7% | 80.0% |
| Combined | 24h | 92 | (mixed assets) | 0.838% | 20.7% | 78.3% |
| Combined | 7d | 140 | (mixed assets) | 0.718% | 22.9% | 78.6% |
| Combined | 30d | 140 | (mixed assets) | 0.718% | 22.9% | 78.6% |

## Predicted vs actual (last 48 scored hours)

```mermaid
xychart-beta
    title "BTC: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00"]
    y-axis "USD" 58277.5641 --> 64047.4023
    line [63060.3716, 62587.6439, 63617.4254, 63635.2318, 63784.5035, 63653.0941, 63983.4189, 63531.0235, 63000.0108, 62611.7840, 62594.5179, 62738.9417, 62107.3691, 62034.4887, 61364.4996, 62144.4125, 61917.8839, 62115.3426, 61461.4709, 62265.8151, 61917.1456, 61375.4786, 61782.2757, 61907.4304, 61710.4094, 61713.2007, 61496.0052, 62043.6711, 61706.2766, 61402.0444, 61826.2549, 61809.0941, 58985.3443, 59327.2301, 58898.1341]
    line [62782.7000, 62534.9000, 63664.0000, 63786.4000, 63720.2000, 63968.3000, 63491.0000, 63028.9000, 62729.5000, 62683.5000, 62817.6000, 62298.8000, 62055.0000, 61484.9000, 62108.5000, 61913.5000, 62062.2000, 61516.7000, 62199.9000, 62089.6000, 61454.1000, 61863.2000, 61999.7000, 61795.2000, 61766.6000, 61587.1000, 61983.7000, 61744.7000, 61499.4000, 61808.9000, 61696.8000, 59399.9000, 59473.4000, 59090.8000, 58335.9000]
```

```mermaid
xychart-beta
    title "ETH: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00"]
    y-axis "USD" 1613.0653 --> 1813.4016
    line [1783.6536, 1770.0216, 1800.2369, 1798.6210, 1803.2721, 1802.7104, 1809.5477, 1799.5438, 1777.2612, 1763.9669, 1767.2241, 1774.7205, 1764.5976, 1758.7069, 1734.9427, 1759.2032, 1753.8095, 1754.2157, 1733.1769, 1750.0062, 1739.9959, 1724.6459, 1737.5651, 1746.5479, 1749.7396, 1747.9575, 1742.1400, 1756.6841, 1745.7351, 1734.5177, 1753.7047, 1742.1809, 1639.3421, 1635.8606, 1618.4518]
    line [1777.1700, 1768.4400, 1801.3700, 1804.6700, 1801.2200, 1811.5900, 1796.4400, 1780.4900, 1766.9800, 1769.3000, 1775.7500, 1768.7100, 1759.2000, 1739.3100, 1758.4600, 1755.2900, 1755.1800, 1733.4500, 1747.5700, 1744.0700, 1725.2600, 1741.4100, 1748.2700, 1751.1500, 1749.2500, 1744.5900, 1755.3500, 1746.6900, 1737.7000, 1752.6300, 1741.7300, 1653.5300, 1643.7000, 1629.2900, 1614.6800]
```

```mermaid
xychart-beta
    title "SOL: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00"]
    y-axis "USD" 67.8299 --> 75.2954
    line [73.5341, 73.2381, 74.4685, 74.2437, 74.4589, 74.6981, 75.2202, 75.0883, 73.3377, 73.0445, 73.7306, 73.9697, 73.3643, 72.9832, 72.1030, 73.1512, 72.9967, 72.9224, 71.8644, 72.9845, 72.6319, 72.0148, 72.5046, 72.7890, 72.5212, 72.3440, 71.8221, 72.3817, 71.5518, 70.7955, 71.2176, 70.9479, 67.8978, 69.4654, 69.0075]
    line [73.4800, 73.1400, 74.4800, 74.4700, 74.3800, 75.0800, 74.8700, 73.5200, 73.1800, 73.7400, 74.0000, 73.4700, 73.0200, 72.1700, 73.2000, 73.0700, 72.9300, 72.0200, 72.8800, 72.8400, 72.0600, 72.6500, 72.8300, 72.5900, 72.4600, 71.9500, 72.3600, 71.7300, 71.0500, 71.2800, 70.9900, 68.3000, 69.4400, 69.2200, 68.7700]
```

```mermaid
xychart-beta
    title "HYPE: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00"]
    y-axis "USD" 60.6694 --> 69.2223
    line [67.0484, 66.8208, 68.3664, 68.4064, 68.4537, 68.7347, 68.5994, 69.1532, 67.7420, 67.4244, 69.0731, 68.5737, 67.4783, 67.6486, 65.6478, 67.2095, 66.6644, 66.2963, 65.2308, 66.0059, 65.6164, 64.6495, 65.6119, 65.5884, 65.9825, 64.8338, 64.7556, 64.8722, 63.6870, 63.2640, 63.1148, 63.6180, 61.1716, 61.6585, 60.7301]
    line [66.9400, 66.5900, 68.4900, 68.4900, 68.3600, 68.7200, 69.0400, 67.8700, 67.5900, 68.8500, 68.6500, 67.6000, 67.7200, 65.9400, 67.0700, 66.7400, 66.2100, 65.3600, 66.0400, 65.9200, 64.8700, 65.6900, 65.7600, 65.9800, 65.0600, 64.9100, 64.9300, 63.8800, 63.3600, 63.1700, 63.4300, 61.4900, 61.7800, 61.0700, 61.1400]
```

## Recent forecasts with scores

| Asset | Hour (ET) | Start | Predicted | Range | Dir | Actual close | $ error | % error | Dir correct |
|---|---|---|---|---|---|---|---|---|---|
| BTC | 2026-11-20 14:00-05:00 | $58,322.60 | $58,172.50 | $57,547.78–$58,797.21 | DOWN | pending | — | — | pending |
| ETH | 2026-11-20 14:00-05:00 | $1,615.47 | $1,612.21 | $1,589.70–$1,634.71 | SIDEWAYS | pending | — | — | pending |
| SOL | 2026-11-20 14:00-05:00 | $68.79 | $68.58 | $67.72–$69.44 | DOWN | pending | — | — | pending |
| HYPE | 2026-11-20 14:00-05:00 | $61.2300 | $61.1765 | $60.2477–$62.1053 | SIDEWAYS | pending | — | — | pending |
| BTC | 2026-11-20 13:00-05:00 | $59,013.00 | $58,898.13 | $58,300.44–$59,495.83 | SIDEWAYS | $58,335.90 | +562.2341 | +0.964% | no |
| ETH | 2026-11-20 13:00-05:00 | $1,625.32 | $1,618.45 | $1,596.37–$1,640.53 | DOWN | $1,614.68 | +3.7718 | +0.234% | yes |
| SOL | 2026-11-20 13:00-05:00 | $69.10 | $69.01 | $68.16–$69.85 | SIDEWAYS | $68.77 | +0.2375 | +0.345% | no |
| HYPE | 2026-11-20 13:00-05:00 | $60.9800 | $60.7301 | $59.8041–$61.6562 | DOWN | $61.1400 | -0.4099 | -0.670% | no |
| BTC | 2026-11-20 12:00-05:00 | $59,391.00 | $59,327.23 | $58,735.97–$59,918.49 | SIDEWAYS | $59,090.80 | +236.4301 | +0.400% | no |
| ETH | 2026-11-20 12:00-05:00 | $1,641.00 | $1,635.86 | $1,614.15–$1,657.57 | DOWN | $1,629.29 | +6.5706 | +0.403% | yes |
| SOL | 2026-11-20 12:00-05:00 | $69.37 | $69.47 | $68.61–$70.32 | SIDEWAYS | $69.22 | +0.2454 | +0.355% | yes |
| HYPE | 2026-11-20 12:00-05:00 | $61.7000 | $61.6585 | $60.7534–$62.5637 | SIDEWAYS | $61.0700 | +0.5885 | +0.964% | no |
| BTC | 2026-11-20 11:00-05:00 | $59,260.90 | $58,985.34 | $58,398.57–$59,572.12 | DOWN | $59,473.40 | -488.0557 | -0.821% | no |
| ETH | 2026-11-20 11:00-05:00 | $1,649.27 | $1,639.34 | $1,618.44–$1,660.24 | DOWN | $1,643.70 | -4.3579 | -0.265% | yes |
| SOL | 2026-11-20 11:00-05:00 | $68.25 | $67.90 | $67.07–$68.73 | DOWN | $69.44 | -1.5422 | -2.221% | no |
| HYPE | 2026-11-20 11:00-05:00 | $61.5100 | $61.1716 | $60.2730–$62.0701 | DOWN | $61.7800 | -0.6084 | -0.985% | no |
| BTC | 2026-11-20 10:00-05:00 | $61,860.10 | $61,809.09 | $61,292.19–$62,326.00 | SIDEWAYS | $59,399.90 | +2409.1941 | +4.056% | no |
| ETH | 2026-11-20 10:00-05:00 | $1,744.40 | $1,742.18 | $1,724.34–$1,760.03 | SIDEWAYS | $1,653.53 | +88.6509 | +5.361% | no |
| SOL | 2026-11-20 10:00-05:00 | $71.10 | $70.95 | $70.20–$71.69 | DOWN | $68.30 | +2.6479 | +3.877% | yes |
| HYPE | 2026-11-20 10:00-05:00 | $63.5900 | $63.6180 | $62.7873–$64.4486 | SIDEWAYS | $61.4900 | +2.1280 | +3.461% | no |
| BTC | 2026-11-20 09:00-05:00 | $61,835.00 | $61,826.25 | $61,340.87–$62,311.64 | SIDEWAYS | $61,696.80 | +129.4549 | +0.210% | no |
| ETH | 2026-11-20 09:00-05:00 | $1,753.24 | $1,753.70 | $1,737.17–$1,770.23 | SIDEWAYS | $1,741.73 | +11.9747 | +0.688% | no |
| SOL | 2026-11-20 09:00-05:00 | $71.33 | $71.22 | $70.51–$71.93 | SIDEWAYS | $70.99 | +0.2276 | +0.321% | no |
| HYPE | 2026-11-20 09:00-05:00 | $63.1800 | $63.1148 | $62.2673–$63.9624 | SIDEWAYS | $63.4300 | -0.3152 | -0.497% | no |
| BTC | 2026-11-20 08:00-05:00 | $61,474.30 | $61,402.04 | $60,931.20–$61,872.89 | SIDEWAYS | $61,808.90 | -406.8556 | -0.658% | no |
| ETH | 2026-11-20 08:00-05:00 | $1,736.81 | $1,734.52 | $1,718.93–$1,750.11 | SIDEWAYS | $1,752.63 | -18.1123 | -1.033% | no |
| SOL | 2026-11-20 08:00-05:00 | $71.01 | $70.80 | $70.11–$71.48 | DOWN | $71.28 | -0.4845 | -0.680% | no |
| HYPE | 2026-11-20 08:00-05:00 | $63.3400 | $63.2640 | $62.4072–$64.1209 | SIDEWAYS | $63.1700 | +0.0940 | +0.149% | yes |
| BTC | 2026-11-20 07:00-05:00 | $61,774.00 | $61,706.28 | $61,224.34–$62,188.21 | SIDEWAYS | $61,499.40 | +206.8766 | +0.336% | no |
| ETH | 2026-11-20 07:00-05:00 | $1,747.76 | $1,745.74 | $1,729.87–$1,761.60 | SIDEWAYS | $1,737.70 | +8.0351 | +0.462% | no |
| SOL | 2026-11-20 07:00-05:00 | $71.71 | $71.55 | $70.86–$72.25 | DOWN | $71.05 | +0.5018 | +0.706% | yes |
| HYPE | 2026-11-20 07:00-05:00 | $63.9600 | $63.6870 | $62.8030–$64.5709 | DOWN | $63.3600 | +0.3270 | +0.516% | yes |
| BTC | 2026-11-20 06:00-05:00 | $62,027.40 | $62,043.67 | $61,540.44–$62,546.91 | SIDEWAYS | $61,744.70 | +298.9711 | +0.484% | no |
| ETH | 2026-11-20 06:00-05:00 | $1,756.57 | $1,756.68 | $1,740.00–$1,773.37 | SIDEWAYS | $1,746.69 | +9.9941 | +0.572% | no |
| SOL | 2026-11-20 06:00-05:00 | $72.41 | $72.38 | $71.68–$73.09 | SIDEWAYS | $71.73 | +0.6517 | +0.909% | no |
| HYPE | 2026-11-20 06:00-05:00 | $65.0200 | $64.8722 | $63.9526–$65.7917 | SIDEWAYS | $63.8800 | +0.9922 | +1.553% | no |
| BTC | 2026-11-20 05:00-05:00 | $61,582.20 | $61,496.01 | $60,993.23–$61,998.78 | SIDEWAYS | $61,983.70 | -487.6948 | -0.787% | no |
| ETH | 2026-11-20 05:00-05:00 | $1,744.13 | $1,742.14 | $1,725.38–$1,758.90 | SIDEWAYS | $1,755.35 | -13.2100 | -0.753% | no |
| SOL | 2026-11-20 05:00-05:00 | $71.97 | $71.82 | $71.11–$72.53 | DOWN | $72.36 | -0.5379 | -0.743% | no |
| HYPE | 2026-11-20 05:00-05:00 | $64.9100 | $64.7556 | $63.7876–$65.7236 | SIDEWAYS | $64.9300 | -0.1744 | -0.269% | yes |

## Scheduler

- Platform: Primary: GitHub Actions workflow `hourly-keeper` (always-on job that fires at HH:00:40 ET and hands off to a successor every ~5h40m). Backup: scheduled workflow `hourly-forecast` (best-effort cron), which also restarts the keeper if it is not running. Repo samuelkreitl-wq/crypto-hourly-forecaster
- Cron (UTC): `keeper: every hour at :00:40 | backup cron: 0 * * * * | 10 * * * * | 25 * * * * | 45 * * * *`
- One forecast per asset per ET hour (asset+forecast_hour key); late or concurrent triggers are skipped as duplicates. Push races reset to the latest database and re-run.
- Config: [.github/workflows/hourly.yml](.github/workflows/hourly.yml) · Raw run log: [data/scheduler_runs.jsonl](data/scheduler_runs.jsonl)

| Started (ET) | Trigger | Min after :00 | Status | New forecasts | Duplicates skipped | Scored | Gaps/errors |
|---|---|---|---|---|---|---|---|
| 2026-11-20 14:00:40-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 13:35:55-05:00 | schedule:10 * * * * | 35.92 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 13:00:41-05:00 | keeper:44749387900 | 0.69 | ok | — | BTC,ETH,SOL,HYPE | 4 | 28 |
| 2026-11-20 13:00:26-05:00 | schedule:45 * * * * | 0.44 | ok | BTC,ETH,SOL,HYPE | — | 0 | 28 |
| 2026-11-20 12:54:54-05:00 | schedule:25 * * * * | 54.9 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 12:25:55-05:00 | schedule:0 * * * * | 25.92 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 12:00:40-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 11:00:41-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 10:00:41-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 09:00:58-05:00 | keeper-start:44749387900 | 0.97 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 09:00:40-05:00 | keeper:44707089952 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 08:00:40-05:00 | keeper:44707089952 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 07:00:40-05:00 | keeper:44707089952 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 06:00:40-05:00 | keeper:44707089952 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 05:00:40-05:00 | keeper:44707089952 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 04:58:28-05:00 | schedule:10 * * * * | 58.47 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 04:11:11-05:00 | schedule:45 * * * * | 11.19 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 04:00:51-05:00 | keeper-start:44707089952 | 0.86 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 04:00:40-05:00 | keeper:44671511289 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 03:41:30-05:00 | schedule:25 * * * * | 41.5 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 03:07:46-05:00 | schedule:0 * * * * | 7.78 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 03:00:41-05:00 | keeper:44671511289 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 02:00:40-05:00 | keeper:44671511289 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 01:00:40-05:00 | keeper:44671511289 | 0.67 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 00:00:40-05:00 | keeper:44671511289 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |

## Data gaps, missed runs and errors

| Asset | Hour (ET) | Kind | Detail | Logged (ET) |
|---|---|---|---|---|
| HYPE | 2026-11-19T07:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:49-05:00 |
| HYPE | 2026-11-19T06:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:49-05:00 |
| SOL | 2026-11-19T07:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:48-05:00 |
| SOL | 2026-11-19T06:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:48-05:00 |
| ETH | 2026-11-19T07:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:48-05:00 |
| ETH | 2026-11-19T06:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:48-05:00 |
| BTC | 2026-11-19T07:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:48-05:00 |
| BTC | 2026-11-19T06:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T08:18:48-05:00 |
| HYPE | 2026-11-19T02:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| HYPE | 2026-11-19T01:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| HYPE | 2026-11-19T00:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| HYPE | 2026-11-18T23:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| HYPE | 2026-11-18T22:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| SOL | 2026-11-19T02:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| SOL | 2026-11-19T01:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| SOL | 2026-11-19T00:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| SOL | 2026-11-18T23:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| SOL | 2026-11-18T22:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:56-05:00 |
| ETH | 2026-11-19T02:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| ETH | 2026-11-19T01:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| ETH | 2026-11-19T00:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| ETH | 2026-11-18T23:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| ETH | 2026-11-18T22:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| BTC | 2026-11-19T02:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| BTC | 2026-11-19T01:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| BTC | 2026-11-19T00:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| BTC | 2026-11-18T23:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |
| BTC | 2026-11-18T22:00-05:00 | missed_run | no forecast recorded for this hour (scheduler did not run in time) | 2026-11-19T03:54:55-05:00 |

## How it works

Every run checks each asset (Kraken pairs XBTUSD, ETHUSD, SOLUSD and HYPEUSD) in four steps:
1. It scores any earlier forecast whose hour has ended, using that hour's completed Kraken candle close. Missed scoring is caught up on the next run.
2. It logs any hour from the past 48 that has no forecast as `missed_run`.
3. If no forecast exists yet for the current ET hour, it fetches Kraken spot, the latest trade time and hourly OHLC. It computes EMA9/21, RSI14, ATR14, realized volatility, momentum and a volume ratio, then saves the forecast for the close at the next :00.
4. If an asset's feed is unavailable or stale, it logs a gap for that asset only and still forecasts the others.

Records are append-only JSONL in `data/`, keyed by asset. Every run is a git commit, and the workflow fails if any existing line changes. The model is a transparent heuristic (`heuristic-v1`), not financial advice.

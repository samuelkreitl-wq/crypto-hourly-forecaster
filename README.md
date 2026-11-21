# Hourly crypto forecaster: BTC · ETH · SOL · HYPE

> This is for forecasting and measurement only. It uses Kraken's public market data and places no trades. It holds no API keys and spends nothing. All times are Eastern (America/New_York). This page is regenerated automatically on every scheduler run.

**Last updated:** 2026-11-20T23:52:36-05:00 · **Interactive dashboard:** [open it here](https://samuelkreitl-wq.github.io/crypto-hourly-forecaster/)

## Latest forecasts

| Asset | Kraken spot at run | Spot time (ET) | Forecast close at | Predicted | Range (low–high) | Direction | Confidence | Main factors |
|---|---|---|---|---|---|---|---|---|
| **BTC** | $56,732.10 | 2026-11-20 23:00:39-05:00 | 2026-11-21 00:00-05:00 | **$56,426.19** | $55,648.95 – $57,203.42 | DOWN | 55% | RSI 14 oversold -> mean-reversion lift; EMA9 below EMA21 (-1.721%); last hour -3.22%, 3h -3.91%, 24h -9.18% |
| **ETH** | $1,571.14 | 2026-11-20 23:00:39-05:00 | 2026-11-21 00:00-05:00 | **$1,561.96** | $1,535.53 – $1,588.38 | DOWN | 55% | RSI 10 oversold -> mean-reversion lift; EMA9 below EMA21 (-2.280%); last hour -3.07%, 3h -3.21%, 24h -10.60% |
| **SOL** | $66.35 | 2026-11-20 23:00:39-05:00 | 2026-11-21 00:00-05:00 | **$65.97** | $64.89 – $67.05 | DOWN | 55% | RSI 27 oversold -> mean-reversion lift; EMA9 below EMA21 (-1.691%); last hour -3.36%, 3h -3.92%, 24h -9.56% |
| **HYPE** | $57.1800 | 2026-11-20 23:00:40-05:00 | 2026-11-21 00:00-05:00 | **$56.8203** | $55.7111 – $57.9296 | DOWN | 55% | RSI 19 oversold -> mean-reversion lift; EMA9 below EMA21 (-2.775%); last hour -4.08%, 3h -6.32%, 24h -14.75% |

## Accuracy (scored forecasts only)

| Asset | Window | Scored | MAE $ | MAE % | Direction hit rate | Close inside range |
|---|---|---|---|---|---|---|
| BTC | 24h | 23 | $431.39 | 0.728% | 17.4% | 87.0% |
| BTC | 7d | 44 | $375.62 | 0.621% | 15.9% | 77.3% |
| BTC | 30d | 44 | $375.62 | 0.621% | 15.9% | 77.3% |
| ETH | 24h | 23 | $12.77 | 0.769% | 30.4% | 87.0% |
| ETH | 7d | 44 | $11.17 | 0.657% | 22.7% | 81.8% |
| ETH | 30d | 44 | $11.17 | 0.657% | 22.7% | 81.8% |
| SOL | 24h | 23 | $0.6335 | 0.916% | 26.1% | 82.6% |
| SOL | 7d | 44 | $0.5454 | 0.771% | 31.8% | 77.3% |
| SOL | 30d | 44 | $0.5454 | 0.771% | 31.8% | 77.3% |
| HYPE | 24h | 23 | $0.6382 | 1.040% | 21.7% | 78.3% |
| HYPE | 7d | 44 | $0.6115 | 0.958% | 22.7% | 77.3% |
| HYPE | 30d | 44 | $0.6115 | 0.958% | 22.7% | 77.3% |
| Combined | 24h | 92 | (mixed assets) | 0.863% | 23.9% | 83.7% |
| Combined | 7d | 176 | (mixed assets) | 0.752% | 23.3% | 78.4% |
| Combined | 30d | 176 | (mixed assets) | 0.752% | 23.3% | 78.4% |

## Predicted vs actual (last 48 scored hours)

```mermaid
xychart-beta
    title "BTC: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]
    y-axis "USD" 56585.4579 --> 64047.4023
    line [63060.3716, 62587.6439, 63617.4254, 63635.2318, 63784.5035, 63653.0941, 63983.4189, 63531.0235, 63000.0108, 62611.7840, 62594.5179, 62738.9417, 62107.3691, 62034.4887, 61364.4996, 62144.4125, 61917.8839, 62115.3426, 61461.4709, 62265.8151, 61917.1456, 61375.4786, 61782.2757, 61907.4304, 61710.4094, 61713.2007, 61496.0052, 62043.6711, 61706.2766, 61402.0444, 61826.2549, 61809.0941, 58985.3443, 59327.2301, 58898.1341, 58172.4965, 58458.9385, 58305.6354, 59078.4154, 58997.5993, 58827.3552, 58968.6345, 58942.6948, 58414.1547]
    line [62782.7000, 62534.9000, 63664.0000, 63786.4000, 63720.2000, 63968.3000, 63491.0000, 63028.9000, 62729.5000, 62683.5000, 62817.6000, 62298.8000, 62055.0000, 61484.9000, 62108.5000, 61913.5000, 62062.2000, 61516.7000, 62199.9000, 62089.6000, 61454.1000, 61863.2000, 61999.7000, 61795.2000, 61766.6000, 61587.1000, 61983.7000, 61744.7000, 61499.4000, 61808.9000, 61696.8000, 59399.9000, 59473.4000, 59090.8000, 58335.9000, 58480.8000, 58351.6000, 58999.0000, 59035.8000, 58806.3000, 58900.3000, 58909.9000, 58492.8000, 56642.1000]
```

```mermaid
xychart-beta
    title "ETH: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]
    y-axis "USD" 1567.0614 --> 1813.4016
    line [1783.6536, 1770.0216, 1800.2369, 1798.6210, 1803.2721, 1802.7104, 1809.5477, 1799.5438, 1777.2612, 1763.9669, 1767.2241, 1774.7205, 1764.5976, 1758.7069, 1734.9427, 1759.2032, 1753.8095, 1754.2157, 1733.1769, 1750.0062, 1739.9959, 1724.6459, 1737.5651, 1746.5479, 1749.7396, 1747.9575, 1742.1400, 1756.6841, 1745.7351, 1734.5177, 1753.7047, 1742.1809, 1639.3421, 1635.8606, 1618.4518, 1612.2067, 1600.2784, 1595.2670, 1612.6241, 1617.4705, 1620.4496, 1620.2096, 1624.2236, 1615.3975]
    line [1777.1700, 1768.4400, 1801.3700, 1804.6700, 1801.2200, 1811.5900, 1796.4400, 1780.4900, 1766.9800, 1769.3000, 1775.7500, 1768.7100, 1759.2000, 1739.3100, 1758.4600, 1755.2900, 1755.1800, 1733.4500, 1747.5700, 1744.0700, 1725.2600, 1741.4100, 1748.2700, 1751.1500, 1749.2500, 1744.5900, 1755.3500, 1746.6900, 1737.7000, 1752.6300, 1741.7300, 1653.5300, 1643.7000, 1629.2900, 1614.6800, 1605.8200, 1599.3600, 1616.2500, 1619.0800, 1619.3200, 1619.8200, 1622.5900, 1617.4900, 1568.6300]
```

```mermaid
xychart-beta
    title "SOL: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]
    y-axis "USD" 66.1338 --> 75.2954
    line [73.5341, 73.2381, 74.4685, 74.2437, 74.4589, 74.6981, 75.2202, 75.0883, 73.3377, 73.0445, 73.7306, 73.9697, 73.3643, 72.9832, 72.1030, 73.1512, 72.9967, 72.9224, 71.8644, 72.9845, 72.6319, 72.0148, 72.5046, 72.7890, 72.5212, 72.3440, 71.8221, 72.3817, 71.5518, 70.7955, 71.2176, 70.9479, 67.8978, 69.4654, 69.0075, 68.5838, 67.9712, 67.2747, 68.7969, 69.0329, 68.5864, 68.7318, 68.5812, 68.1957]
    line [73.4800, 73.1400, 74.4800, 74.4700, 74.3800, 75.0800, 74.8700, 73.5200, 73.1800, 73.7400, 74.0000, 73.4700, 73.0200, 72.1700, 73.2000, 73.0700, 72.9300, 72.0200, 72.8800, 72.8400, 72.0600, 72.6500, 72.8300, 72.5900, 72.4600, 71.9500, 72.3600, 71.7300, 71.0500, 71.2800, 70.9900, 68.3000, 69.4400, 69.2200, 68.7700, 68.1200, 67.3900, 68.9400, 69.2100, 68.7200, 68.8500, 68.6700, 68.4600, 66.2000]
```

```mermaid
xychart-beta
    title "HYPE: predicted (line 1) vs actual (line 2) close"
    x-axis ["20:00", "21:00", "03:00", "04:00", "05:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]
    y-axis "USD" 56.8231 --> 69.2223
    line [67.0484, 66.8208, 68.3664, 68.4064, 68.4537, 68.7347, 68.5994, 69.1532, 67.7420, 67.4244, 69.0731, 68.5737, 67.4783, 67.6486, 65.6478, 67.2095, 66.6644, 66.2963, 65.2308, 66.0059, 65.6164, 64.6495, 65.6119, 65.5884, 65.9825, 64.8338, 64.7556, 64.8722, 63.6870, 63.2640, 63.1148, 63.6180, 61.1716, 61.6585, 60.7301, 61.1765, 60.5161, 60.1090, 61.0236, 61.4086, 60.8346, 60.5340, 60.4181, 58.9773]
    line [66.9400, 66.5900, 68.4900, 68.4900, 68.3600, 68.7200, 69.0400, 67.8700, 67.5900, 68.8500, 68.6500, 67.6000, 67.7200, 65.9400, 67.0700, 66.7400, 66.2100, 65.3600, 66.0400, 65.9200, 64.8700, 65.6900, 65.7600, 65.9800, 65.0600, 64.9100, 64.9300, 63.8800, 63.3600, 63.1700, 63.4300, 61.4900, 61.7800, 61.0700, 61.1400, 60.6400, 60.1200, 61.1600, 61.4000, 60.9000, 60.5900, 60.4500, 59.2500, 56.8800]
```

## Recent forecasts with scores

| Asset | Hour (ET) | Start | Predicted | Range | Dir | Actual close | $ error | % error | Dir correct |
|---|---|---|---|---|---|---|---|---|---|
| BTC | 2026-11-20 23:00-05:00 | $56,732.10 | $56,426.19 | $55,648.95–$57,203.42 | DOWN | pending | — | — | pending |
| ETH | 2026-11-20 23:00-05:00 | $1,571.14 | $1,561.96 | $1,535.53–$1,588.38 | DOWN | pending | — | — | pending |
| SOL | 2026-11-20 23:00-05:00 | $66.35 | $65.97 | $64.89–$67.05 | DOWN | pending | — | — | pending |
| HYPE | 2026-11-20 23:00-05:00 | $57.1800 | $56.8203 | $55.7111–$57.9296 | DOWN | pending | — | — | pending |
| BTC | 2026-11-20 22:00-05:00 | $58,459.90 | $58,414.15 | $57,723.16–$59,105.15 | SIDEWAYS | $56,642.10 | +1772.0547 | +3.129% | no |
| ETH | 2026-11-20 22:00-05:00 | $1,616.30 | $1,615.40 | $1,591.01–$1,639.79 | SIDEWAYS | $1,568.63 | +46.7675 | +2.981% | no |
| SOL | 2026-11-20 22:00-05:00 | $68.37 | $68.20 | $67.22–$69.17 | SIDEWAYS | $66.20 | +1.9957 | +3.015% | no |
| HYPE | 2026-11-20 22:00-05:00 | $59.2100 | $58.9773 | $57.9620–$59.9926 | DOWN | $56.8800 | +2.0973 | +3.687% | yes |
| BTC | 2026-11-20 21:00-05:00 | $58,935.00 | $58,942.69 | $58,244.52–$59,640.87 | SIDEWAYS | $58,492.80 | +449.8948 | +0.769% | no |
| ETH | 2026-11-20 21:00-05:00 | $1,624.31 | $1,624.22 | $1,599.18–$1,649.27 | SIDEWAYS | $1,617.49 | +6.7336 | +0.416% | no |
| SOL | 2026-11-20 21:00-05:00 | $68.77 | $68.58 | $67.58–$69.58 | SIDEWAYS | $68.46 | +0.1212 | +0.177% | no |
| HYPE | 2026-11-20 21:00-05:00 | $60.5100 | $60.4181 | $59.4291–$61.4071 | SIDEWAYS | $59.2500 | +1.1681 | +1.972% | no |
| BTC | 2026-11-20 20:00-05:00 | $58,958.20 | $58,968.63 | $58,266.22–$59,671.05 | SIDEWAYS | $58,909.90 | +58.7345 | +0.100% | yes |
| ETH | 2026-11-20 20:00-05:00 | $1,620.83 | $1,620.21 | $1,595.16–$1,645.26 | SIDEWAYS | $1,622.59 | -2.3804 | -0.147% | yes |
| SOL | 2026-11-20 20:00-05:00 | $68.88 | $68.73 | $67.72–$69.74 | SIDEWAYS | $68.67 | +0.0618 | +0.090% | no |
| HYPE | 2026-11-20 20:00-05:00 | $60.6300 | $60.5340 | $59.5173–$61.5507 | SIDEWAYS | $60.4500 | +0.0840 | +0.139% | no |
| BTC | 2026-11-20 19:00-05:00 | $58,834.40 | $58,827.36 | $58,101.81–$59,552.90 | SIDEWAYS | $58,900.30 | -72.9448 | -0.124% | yes |
| ETH | 2026-11-20 19:00-05:00 | $1,620.72 | $1,620.45 | $1,594.82–$1,646.08 | SIDEWAYS | $1,619.82 | +0.6296 | +0.039% | yes |
| SOL | 2026-11-20 19:00-05:00 | $68.75 | $68.59 | $67.55–$69.63 | SIDEWAYS | $68.85 | -0.2636 | -0.383% | yes |
| HYPE | 2026-11-20 19:00-05:00 | $60.9000 | $60.8346 | $59.8186–$61.8506 | SIDEWAYS | $60.5900 | +0.2446 | +0.404% | no |
| BTC | 2026-11-20 18:00-05:00 | $58,978.90 | $58,997.60 | $58,280.38–$59,714.82 | SIDEWAYS | $58,806.30 | +191.2993 | +0.325% | no |
| ETH | 2026-11-20 18:00-05:00 | $1,617.99 | $1,617.47 | $1,591.85–$1,643.09 | SIDEWAYS | $1,619.32 | -1.8495 | -0.114% | yes |
| SOL | 2026-11-20 18:00-05:00 | $69.14 | $69.03 | $68.01–$70.06 | SIDEWAYS | $68.72 | +0.3129 | +0.455% | no |
| HYPE | 2026-11-20 18:00-05:00 | $61.4100 | $61.4086 | $60.3930–$62.4242 | SIDEWAYS | $60.9000 | +0.5086 | +0.835% | no |
| BTC | 2026-11-20 17:00-05:00 | $58,970.00 | $59,078.42 | $58,365.55–$59,791.28 | SIDEWAYS | $59,035.80 | +42.6154 | +0.072% | yes |
| ETH | 2026-11-20 17:00-05:00 | $1,611.71 | $1,612.62 | $1,587.03–$1,638.22 | SIDEWAYS | $1,619.08 | -6.4559 | -0.399% | no |
| SOL | 2026-11-20 17:00-05:00 | $68.78 | $68.80 | $67.79–$69.81 | SIDEWAYS | $69.21 | -0.4131 | -0.597% | no |
| HYPE | 2026-11-20 17:00-05:00 | $60.9800 | $61.0236 | $59.9917–$62.0554 | SIDEWAYS | $61.4000 | -0.3764 | -0.613% | no |
| BTC | 2026-11-20 16:00-05:00 | $58,369.00 | $58,305.64 | $57,632.52–$58,978.75 | SIDEWAYS | $58,999.00 | -693.3646 | -1.175% | no |
| ETH | 2026-11-20 16:00-05:00 | $1,599.10 | $1,595.27 | $1,570.85–$1,619.68 | SIDEWAYS | $1,616.25 | -20.9830 | -1.298% | no |
| SOL | 2026-11-20 16:00-05:00 | $67.44 | $67.27 | $66.34–$68.21 | SIDEWAYS | $68.94 | -1.6653 | -2.416% | no |
| HYPE | 2026-11-20 16:00-05:00 | $60.2700 | $60.1090 | $59.1214–$61.0966 | SIDEWAYS | $61.1600 | -1.0510 | -1.718% | no |
| BTC | 2026-11-20 15:00-05:00 | $58,502.90 | $58,458.94 | $57,800.12–$59,117.76 | SIDEWAYS | $58,351.60 | +107.3385 | +0.184% | no |
| ETH | 2026-11-20 15:00-05:00 | $1,604.32 | $1,600.28 | $1,576.89–$1,623.67 | SIDEWAYS | $1,599.36 | +0.9184 | +0.057% | no |
| SOL | 2026-11-20 15:00-05:00 | $68.09 | $67.97 | $67.09–$68.86 | SIDEWAYS | $67.39 | +0.5812 | +0.863% | no |
| HYPE | 2026-11-20 15:00-05:00 | $60.6700 | $60.5161 | $59.5888–$61.4434 | SIDEWAYS | $60.1200 | +0.3961 | +0.659% | no |
| BTC | 2026-11-20 14:00-05:00 | $58,322.60 | $58,172.50 | $57,547.78–$58,797.21 | DOWN | $58,480.80 | -308.3035 | -0.527% | no |
| ETH | 2026-11-20 14:00-05:00 | $1,615.47 | $1,612.21 | $1,589.70–$1,634.71 | SIDEWAYS | $1,605.82 | +6.3867 | +0.398% | no |
| SOL | 2026-11-20 14:00-05:00 | $68.79 | $68.58 | $67.72–$69.44 | DOWN | $68.12 | +0.4638 | +0.681% | yes |
| HYPE | 2026-11-20 14:00-05:00 | $61.2300 | $61.1765 | $60.2477–$62.1053 | SIDEWAYS | $60.6400 | +0.5365 | +0.885% | no |

## Scheduler

- Platform: Primary: GitHub Actions workflow `hourly-keeper` (always-on job that fires at HH:00:40 ET and hands off to a successor every ~5h40m). Backup: scheduled workflow `hourly-forecast` (best-effort cron), which also restarts the keeper if it is not running. Repo samuelkreitl-wq/crypto-hourly-forecaster
- Cron (UTC): `keeper: every hour at :00:40 | backup cron: 0 * * * * | 10 * * * * | 25 * * * * | 45 * * * *`
- One forecast per asset per ET hour (asset+forecast_hour key); late or concurrent triggers are skipped as duplicates. Push races reset to the latest database and re-run.
- Config: [.github/workflows/hourly.yml](.github/workflows/hourly.yml) · Raw run log: [data/scheduler_runs.jsonl](data/scheduler_runs.jsonl)

| Started (ET) | Trigger | Min after :00 | Status | New forecasts | Duplicates skipped | Scored | Gaps/errors |
|---|---|---|---|---|---|---|---|
| 2026-11-20 23:52:35-05:00 | schedule:0 * * * * | 52.6 | ok | — | BTC,ETH,SOL,HYPE | 0 | 24 |
| 2026-11-20 23:00:41-05:00 | keeper:44840883315 | 0.69 | ok | BTC,ETH,SOL,HYPE | — | 4 | 24 |
| 2026-11-20 22:00:41-05:00 | keeper:44840883315 | 0.69 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 21:00:40-05:00 | keeper:44840883315 | 0.67 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 20:00:40-05:00 | keeper:44840883315 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 19:47:34-05:00 | schedule:10 * * * * | 47.58 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 19:13:51-05:00 | schedule:45 * * * * | 13.86 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 19:04:03-05:00 | schedule:25 * * * * | 4.06 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 19:00:54-05:00 | keeper-start:44840883315 | 0.91 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 19:00:41-05:00 | keeper:44798125011 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 18:30:13-05:00 | schedule:0 * * * * | 30.22 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 18:00:40-05:00 | keeper:44798125011 | 0.67 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 17:00:40-05:00 | keeper:44798125011 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 16:00:40-05:00 | keeper:44798125011 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 15:00:40-05:00 | keeper:44798125011 | 0.67 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 14:00:50-05:00 | keeper-start:44798125011 | 0.85 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 14:00:40-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 13:35:55-05:00 | schedule:10 * * * * | 35.92 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 13:00:41-05:00 | keeper:44749387900 | 0.69 | ok | — | BTC,ETH,SOL,HYPE | 4 | 28 |
| 2026-11-20 13:00:26-05:00 | schedule:45 * * * * | 0.44 | ok | BTC,ETH,SOL,HYPE | — | 0 | 28 |
| 2026-11-20 12:54:54-05:00 | schedule:25 * * * * | 54.9 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 12:25:55-05:00 | schedule:0 * * * * | 25.92 | ok | — | BTC,ETH,SOL,HYPE | 0 | 28 |
| 2026-11-20 12:00:40-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 11:00:41-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |
| 2026-11-20 10:00:41-05:00 | keeper:44749387900 | 0.68 | ok | BTC,ETH,SOL,HYPE | — | 4 | 28 |

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

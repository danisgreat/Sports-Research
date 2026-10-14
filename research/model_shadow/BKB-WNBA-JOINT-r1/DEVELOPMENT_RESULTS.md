# Development results: `BKB-WNBA-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 241 | 0.2192 | 0.2499 | -0.0340 | -0.0537 | -0.0143 | 17 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 241 | 0.2188 | 0.2501 | -0.0296 | -0.0482 | -0.0111 | 16 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 287 | 0.2192 | 0.2469 | -0.0283 | -0.0443 | -0.0124 | 18 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 769 | 0.2191 | 0.2488 | -0.0306 | -0.0403 | -0.0209 | 51 | BELOW_ZERO |
| Home-win log loss | 2023 | 241 | 0.6280 | 0.6929 | -0.0720 | -0.1163 | -0.0277 | 17 | BELOW_ZERO |
| Home-win log loss | 2024 | 241 | 0.6278 | 0.6933 | -0.0613 | -0.1024 | -0.0203 | 16 | BELOW_ZERO |
| Home-win log loss | 2025 | 287 | 0.6288 | 0.6869 | -0.0598 | -0.0939 | -0.0256 | 18 | BELOW_ZERO |
| Home-win log loss | ALL | 769 | 0.6283 | 0.6908 | -0.0643 | -0.0857 | -0.0429 | 51 | BELOW_ZERO |
| Margin CRPS | 2023 | 241 | 7.2463 | 7.9792 | -0.8131 | -1.3188 | -0.3074 | 17 | BELOW_ZERO |
| Margin CRPS | 2024 | 241 | 6.5613 | 7.3379 | -0.7167 | -1.0934 | -0.3400 | 16 | BELOW_ZERO |
| Margin CRPS | 2025 | 287 | 7.8589 | 8.4795 | -0.6272 | -0.9751 | -0.2794 | 18 | BELOW_ZERO |
| Margin CRPS | ALL | 769 | 7.2602 | 7.9649 | -0.7173 | -0.9409 | -0.4937 | 51 | BELOW_ZERO |
| Total CRPS | 2023 | 241 | 9.8694 | 10.0444 | -0.1831 | -0.5442 | 0.1780 | 17 | SPANS_ZERO |
| Total CRPS | 2024 | 241 | 8.8191 | 9.6024 | -0.8211 | -1.2219 | -0.4203 | 16 | BELOW_ZERO |
| Total CRPS | 2025 | 287 | 9.2894 | 9.6936 | -0.4280 | -0.8851 | 0.0290 | 18 | SPANS_ZERO |
| Total CRPS | ALL | 769 | 9.3238 | 9.7750 | -0.4697 | -0.7021 | -0.2373 | 51 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 241 | 0.2429 | 0.2493 | -0.0072 | -0.0193 | 0.0050 | 17 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 241 | 0.2229 | 0.2499 | -0.0280 | -0.0412 | -0.0147 | 16 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 287 | 0.2367 | 0.2503 | -0.0156 | -0.0315 | 0.0003 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 769 | 0.2343 | 0.2498 | -0.0167 | -0.0245 | -0.0088 | 51 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 241 | 0.2192 | 0.2196 | -0.0017 | -0.0156 | 0.0121 | 17 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 241 | 0.2188 | 0.2176 | 0.0017 | -0.0120 | 0.0153 | 16 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 287 | 0.2192 | 0.2229 | -0.0029 | -0.0147 | 0.0088 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 769 | 0.2191 | 0.2202 | -0.0011 | -0.0081 | 0.0059 | 51 | SPANS_ZERO |
| Home-win log loss | 2023 | 241 | 0.6280 | 0.6292 | -0.0042 | -0.0341 | 0.0258 | 17 | SPANS_ZERO |
| Home-win log loss | 2024 | 241 | 0.6278 | 0.6254 | 0.0040 | -0.0269 | 0.0348 | 16 | SPANS_ZERO |
| Home-win log loss | 2025 | 287 | 0.6288 | 0.6358 | -0.0057 | -0.0312 | 0.0198 | 18 | SPANS_ZERO |
| Home-win log loss | ALL | 769 | 0.6283 | 0.6305 | -0.0022 | -0.0176 | 0.0132 | 51 | SPANS_ZERO |
| Margin CRPS | 2023 | 241 | 7.2463 | 7.2107 | 0.0082 | -0.2451 | 0.2615 | 17 | SPANS_ZERO |
| Margin CRPS | 2024 | 241 | 6.5613 | 6.5867 | -0.0112 | -0.2784 | 0.2560 | 16 | SPANS_ZERO |
| Margin CRPS | 2025 | 287 | 7.8589 | 7.8064 | 0.0659 | -0.1721 | 0.3039 | 18 | SPANS_ZERO |
| Margin CRPS | ALL | 769 | 7.2602 | 7.2375 | 0.0225 | -0.1130 | 0.1580 | 51 | SPANS_ZERO |
| Total CRPS | 2023 | 241 | 9.8694 | 10.1320 | -0.3140 | -0.7262 | 0.0983 | 17 | SPANS_ZERO |
| Total CRPS | 2024 | 241 | 8.8191 | 9.2214 | -0.4225 | -0.6040 | -0.2410 | 16 | BELOW_ZERO |
| Total CRPS | 2025 | 287 | 9.2894 | 9.5896 | -0.2868 | -0.5751 | 0.0014 | 18 | SPANS_ZERO |
| Total CRPS | ALL | 769 | 9.3238 | 9.6442 | -0.3384 | -0.5068 | -0.1701 | 51 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 241 | 0.2429 | 0.2520 | -0.0112 | -0.0259 | 0.0036 | 17 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 241 | 0.2229 | 0.2346 | -0.0121 | -0.0181 | -0.0061 | 16 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 287 | 0.2367 | 0.2465 | -0.0098 | -0.0214 | 0.0017 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 769 | 0.2343 | 0.2445 | -0.0110 | -0.0172 | -0.0048 | 51 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0144; ECE 0.0349; logistic slope 1.134 (SE 0.124), intercept -0.089 (SE 0.080). Brier decomposition: reliability 0.0019, resolution 0.0299, uncertainty 0.2488.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 3 | 0.1809 | 0.0000 | 0.0000 | 0.5615 |
| [0.2, 0.3) | 43 | 0.2602 | 0.3256 | 0.2049 | 0.4748 |
| [0.3, 0.4) | 107 | 0.3551 | 0.2710 | 0.1958 | 0.3621 |
| [0.4, 0.5) | 139 | 0.4502 | 0.4460 | 0.3660 | 0.5290 |
| [0.5, 0.6) | 172 | 0.5513 | 0.5233 | 0.4489 | 0.5966 |
| [0.6, 0.7) | 162 | 0.6482 | 0.6235 | 0.5468 | 0.6944 |
| [0.7, 0.8) | 111 | 0.7496 | 0.7928 | 0.7082 | 0.8578 |
| [0.8, 0.9) | 32 | 0.8354 | 0.8438 | 0.6825 | 0.9314 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.0225 | 1.2365 | 241 | 0.2192 | 0.2201 | 0.0004 | -0.0039 | 0.0047 | SPANS_ZERO |
| 2024 | -0.1488 | 1.1316 | 241 | 0.2188 | 0.2177 | -0.0012 | -0.0058 | 0.0034 | SPANS_ZERO |
| 2025 | -0.1226 | 1.0803 | 287 | 0.2192 | 0.2196 | 0.0005 | -0.0028 | 0.0037 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 8.0000 | 1.0000 | 16.0284 | 410.0000 |
| 180.0000 | 8.0000 | 0.9000 | 16.0332 | 410.0000 |
| 180.0000 | 2.0000 | 1.0000 | 16.0333 | 410.0000 |
| 180.0000 | 2.0000 | 0.9000 | 16.0413 | 410.0000 |
| 180.0000 | 8.0000 | 1.1000 | 16.0423 | 410.0000 |
| 180.0000 | 2.0000 | 1.1000 | 16.0442 | 410.0000 |
| 180.0000 | 2.0000 | 1.2000 | 16.0704 | 410.0000 |
| 180.0000 | 8.0000 | 1.2000 | 16.0714 | 410.0000 |
| 365.0000 | 8.0000 | 0.9000 | 16.0987 | 410.0000 |
| 365.0000 | 8.0000 | 1.0000 | 16.1014 | 410.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:03:14Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-WNBA-JOINT-r1
- `archive_snapshot_sha256`: e651045662e22d9aca0a4696605a09448f52392fdc8fb86b95b5b0f442701e58
- `seconds`: 72

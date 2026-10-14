# Development results: `BKB-NBA-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `PASS_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `BELOW_ZERO_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 1231 | 0.2170 | 0.2482 | -0.0310 | -0.0389 | -0.0232 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 1231 | 0.2127 | 0.2484 | -0.0362 | -0.0435 | -0.0289 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 1230 | 0.2080 | 0.2471 | -0.0379 | -0.0489 | -0.0269 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 3692 | 0.2125 | 0.2479 | -0.0350 | -0.0399 | -0.0301 | 75 | BELOW_ZERO |
| Home-win log loss | 2023 | 1231 | 0.6223 | 0.6896 | -0.0669 | -0.0838 | -0.0500 | 25 | BELOW_ZERO |
| Home-win log loss | 2024 | 1231 | 0.6137 | 0.6898 | -0.0774 | -0.0931 | -0.0618 | 25 | BELOW_ZERO |
| Home-win log loss | 2025 | 1230 | 0.6045 | 0.6874 | -0.0800 | -0.1037 | -0.0562 | 25 | BELOW_ZERO |
| Home-win log loss | ALL | 3692 | 0.6135 | 0.6890 | -0.0748 | -0.0853 | -0.0642 | 75 | BELOW_ZERO |
| Margin CRPS | 2023 | 1231 | 7.9888 | 8.7543 | -0.7550 | -0.9596 | -0.5504 | 25 | BELOW_ZERO |
| Margin CRPS | 2024 | 1231 | 7.9564 | 8.9082 | -0.9465 | -1.1286 | -0.7644 | 25 | BELOW_ZERO |
| Margin CRPS | 2025 | 1230 | 8.1984 | 9.2406 | -1.0062 | -1.3199 | -0.6925 | 25 | BELOW_ZERO |
| Margin CRPS | ALL | 3692 | 8.0478 | 8.9676 | -0.9026 | -1.0371 | -0.7681 | 75 | BELOW_ZERO |
| Total CRPS | 2023 | 1231 | 10.5050 | 11.4845 | -0.9618 | -1.2473 | -0.6762 | 25 | BELOW_ZERO |
| Total CRPS | 2024 | 1231 | 10.3943 | 11.2095 | -0.8256 | -1.0905 | -0.5606 | 25 | BELOW_ZERO |
| Total CRPS | 2025 | 1230 | 10.7419 | 11.2737 | -0.5473 | -0.8182 | -0.2763 | 25 | BELOW_ZERO |
| Total CRPS | ALL | 3692 | 10.5470 | 11.3226 | -0.7782 | -0.9340 | -0.6224 | 75 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 1231 | 0.2261 | 0.2499 | -0.0234 | -0.0316 | -0.0153 | 25 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 1231 | 0.2282 | 0.2495 | -0.0212 | -0.0295 | -0.0129 | 25 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 1230 | 0.2349 | 0.2496 | -0.0148 | -0.0220 | -0.0077 | 25 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 3692 | 0.2297 | 0.2497 | -0.0198 | -0.0242 | -0.0154 | 75 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 1231 | 0.2170 | 0.2240 | -0.0069 | -0.0100 | -0.0039 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 1231 | 0.2127 | 0.2199 | -0.0074 | -0.0107 | -0.0040 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 1230 | 0.2080 | 0.2165 | -0.0080 | -0.0123 | -0.0038 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 3692 | 0.2125 | 0.2202 | -0.0074 | -0.0094 | -0.0055 | 75 | BELOW_ZERO |
| Home-win log loss | 2023 | 1231 | 0.6223 | 0.6395 | -0.0169 | -0.0237 | -0.0102 | 25 | BELOW_ZERO |
| Home-win log loss | 2024 | 1231 | 0.6137 | 0.6307 | -0.0174 | -0.0251 | -0.0097 | 25 | BELOW_ZERO |
| Home-win log loss | 2025 | 1230 | 0.6045 | 0.6240 | -0.0183 | -0.0281 | -0.0086 | 25 | BELOW_ZERO |
| Home-win log loss | ALL | 3692 | 0.6135 | 0.6314 | -0.0175 | -0.0220 | -0.0131 | 75 | BELOW_ZERO |
| Margin CRPS | 2023 | 1231 | 7.9888 | 8.1560 | -0.1617 | -0.2439 | -0.0795 | 25 | BELOW_ZERO |
| Margin CRPS | 2024 | 1231 | 7.9564 | 8.1442 | -0.1866 | -0.2821 | -0.0912 | 25 | BELOW_ZERO |
| Margin CRPS | 2025 | 1230 | 8.1984 | 8.4405 | -0.2267 | -0.3575 | -0.0958 | 25 | BELOW_ZERO |
| Margin CRPS | ALL | 3692 | 8.0478 | 8.2468 | -0.1917 | -0.2497 | -0.1337 | 75 | BELOW_ZERO |
| Total CRPS | 2023 | 1231 | 10.5050 | 10.7749 | -0.2649 | -0.3673 | -0.1625 | 25 | BELOW_ZERO |
| Total CRPS | 2024 | 1231 | 10.3943 | 10.5871 | -0.1986 | -0.3132 | -0.0840 | 25 | BELOW_ZERO |
| Total CRPS | 2025 | 1230 | 10.7419 | 10.9487 | -0.2068 | -0.3028 | -0.1107 | 25 | BELOW_ZERO |
| Total CRPS | ALL | 3692 | 10.5470 | 10.7702 | -0.2234 | -0.2814 | -0.1655 | 75 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 1231 | 0.2261 | 0.2334 | -0.0073 | -0.0103 | -0.0043 | 25 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 1231 | 0.2282 | 0.2333 | -0.0053 | -0.0088 | -0.0017 | 25 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 1230 | 0.2349 | 0.2399 | -0.0051 | -0.0078 | -0.0023 | 25 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 3692 | 0.2297 | 0.2356 | -0.0059 | -0.0076 | -0.0042 | 75 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0051; ECE 0.0352; logistic slope 1.368 (SE 0.063), intercept -0.093 (SE 0.038). Brier decomposition: reliability 0.0020, resolution 0.0364, uncertainty 0.2478.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 29 | 0.1716 | 0.0690 | 0.0191 | 0.2196 |
| [0.2, 0.3) | 178 | 0.2632 | 0.1742 | 0.1255 | 0.2366 |
| [0.3, 0.4) | 424 | 0.3557 | 0.2736 | 0.2333 | 0.3179 |
| [0.4, 0.5) | 656 | 0.4540 | 0.4223 | 0.3850 | 0.4604 |
| [0.5, 0.6) | 1002 | 0.5503 | 0.5539 | 0.5230 | 0.5844 |
| [0.6, 0.7) | 751 | 0.6467 | 0.6711 | 0.6367 | 0.7038 |
| [0.7, 0.8) | 476 | 0.7438 | 0.8025 | 0.7644 | 0.8358 |
| [0.8, 0.9) | 171 | 0.8348 | 0.8655 | 0.8063 | 0.9087 |
| [0.9, 1.0] | 5 | 0.9142 | 1.0000 | 0.5655 | 1.0000 |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.0110 | 1.0061 | 1231 | 0.2170 | 0.2168 | -0.0001 | -0.0003 | -0.0000 | BELOW_ZERO |
| 2024 | -0.1518 | 1.3023 | 1231 | 0.2127 | 0.2115 | -0.0014 | -0.0038 | 0.0011 | SPANS_ZERO |
| 2025 | -0.0762 | 1.3394 | 1230 | 0.2080 | 0.2049 | -0.0028 | -0.0057 | 0.0001 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 45.0000 | 8.0000 | 1.1000 | 18.1836 | 2460.0000 |
| 22.5000 | 8.0000 | 1.1000 | 18.1861 | 2460.0000 |
| 45.0000 | 8.0000 | 1.0000 | 18.1884 | 2460.0000 |
| 22.5000 | 8.0000 | 1.2000 | 18.1921 | 2460.0000 |
| 45.0000 | 8.0000 | 1.2000 | 18.1971 | 2460.0000 |
| 22.5000 | 8.0000 | 1.0000 | 18.1985 | 2460.0000 |
| 22.5000 | 8.0000 | 1.3000 | 18.2133 | 2460.0000 |
| 45.0000 | 8.0000 | 1.3000 | 18.2256 | 2460.0000 |
| 45.0000 | 2.0000 | 1.1000 | 18.2588 | 2460.0000 |
| 45.0000 | 2.0000 | 1.2000 | 18.2660 | 2460.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:07:28Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBA-JOINT-r1
- `archive_snapshot_sha256`: 20aa58d79a1236a3129e418a188f86aa9bec0e22da15a341aee9eb71da187434
- `seconds`: 361

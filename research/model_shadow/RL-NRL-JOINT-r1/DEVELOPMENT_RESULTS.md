# Development results: `RL-NRL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 204 | 0.2233 | 0.2478 | -0.0238 | -0.0455 | -0.0021 | 27 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 204 | 0.2260 | 0.2459 | -0.0142 | -0.0388 | 0.0104 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 204 | 0.2298 | 0.2461 | -0.0151 | -0.0335 | 0.0034 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 612 | 0.2264 | 0.2466 | -0.0176 | -0.0297 | -0.0056 | 83 | BELOW_ZERO |
| Home-win log loss | 2023 | 204 | 0.6409 | 0.6888 | -0.0465 | -0.0947 | 0.0018 | 27 | SPANS_ZERO |
| Home-win log loss | 2024 | 204 | 0.6446 | 0.6848 | -0.0280 | -0.0837 | 0.0278 | 28 | SPANS_ZERO |
| Home-win log loss | 2025 | 204 | 0.6512 | 0.6852 | -0.0313 | -0.0704 | 0.0078 | 28 | SPANS_ZERO |
| Home-win log loss | ALL | 612 | 0.6456 | 0.6863 | -0.0351 | -0.0618 | -0.0084 | 83 | BELOW_ZERO |
| Margin CRPS | 2023 | 204 | 9.9571 | 10.7261 | -0.7520 | -1.3422 | -0.1619 | 27 | BELOW_ZERO |
| Margin CRPS | 2024 | 204 | 9.9550 | 10.5564 | -0.4730 | -1.0695 | 0.1235 | 28 | SPANS_ZERO |
| Margin CRPS | 2025 | 204 | 10.1800 | 10.6239 | -0.3565 | -0.8819 | 0.1688 | 28 | SPANS_ZERO |
| Margin CRPS | ALL | 612 | 10.0307 | 10.6355 | -0.5245 | -0.8422 | -0.2068 | 83 | BELOW_ZERO |
| Total CRPS | 2023 | 204 | 7.4567 | 7.3417 | 0.1180 | -0.0514 | 0.2874 | 27 | SPANS_ZERO |
| Total CRPS | 2024 | 204 | 7.8815 | 7.9177 | -0.0708 | -0.3684 | 0.2267 | 28 | SPANS_ZERO |
| Total CRPS | 2025 | 204 | 7.7514 | 7.9131 | -0.1455 | -0.5020 | 0.2109 | 28 | SPANS_ZERO |
| Total CRPS | ALL | 612 | 7.6965 | 7.7242 | -0.0346 | -0.1955 | 0.1262 | 83 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 204 | 0.2595 | 0.2507 | 0.0095 | 0.0001 | 0.0190 | 27 | ABOVE_ZERO |
| Over the league-median line, Brier | 2024 | 204 | 0.2453 | 0.2489 | -0.0044 | -0.0170 | 0.0082 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 204 | 0.2578 | 0.2526 | 0.0060 | -0.0126 | 0.0246 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 612 | 0.2542 | 0.2507 | 0.0037 | -0.0043 | 0.0116 | 83 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 204 | 0.2233 | 0.2329 | -0.0090 | -0.0239 | 0.0059 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 204 | 0.2260 | 0.2331 | -0.0043 | -0.0210 | 0.0124 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 204 | 0.2298 | 0.2336 | -0.0029 | -0.0147 | 0.0089 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 612 | 0.2264 | 0.2332 | -0.0054 | -0.0134 | 0.0027 | 83 | SPANS_ZERO |
| Home-win log loss | 2023 | 204 | 0.6409 | 0.6586 | -0.0166 | -0.0500 | 0.0167 | 27 | SPANS_ZERO |
| Home-win log loss | 2024 | 204 | 0.6446 | 0.6586 | -0.0076 | -0.0462 | 0.0309 | 28 | SPANS_ZERO |
| Home-win log loss | 2025 | 204 | 0.6512 | 0.6597 | -0.0063 | -0.0324 | 0.0197 | 28 | SPANS_ZERO |
| Home-win log loss | ALL | 612 | 0.6456 | 0.6590 | -0.0101 | -0.0284 | 0.0081 | 83 | SPANS_ZERO |
| Margin CRPS | 2023 | 204 | 9.9571 | 10.1987 | -0.2266 | -0.5949 | 0.1417 | 27 | SPANS_ZERO |
| Margin CRPS | 2024 | 204 | 9.9550 | 10.1476 | -0.1312 | -0.5166 | 0.2542 | 28 | SPANS_ZERO |
| Margin CRPS | 2025 | 204 | 10.1800 | 10.3857 | -0.1423 | -0.4816 | 0.1969 | 28 | SPANS_ZERO |
| Margin CRPS | ALL | 612 | 10.0307 | 10.2440 | -0.1660 | -0.3678 | 0.0358 | 83 | SPANS_ZERO |
| Total CRPS | 2023 | 204 | 7.4567 | 7.4938 | -0.0477 | -0.4091 | 0.3138 | 27 | SPANS_ZERO |
| Total CRPS | 2024 | 204 | 7.8815 | 7.9224 | -0.0711 | -0.3020 | 0.1598 | 28 | SPANS_ZERO |
| Total CRPS | 2025 | 204 | 7.7514 | 7.8485 | -0.0856 | -0.3575 | 0.1864 | 28 | SPANS_ZERO |
| Total CRPS | ALL | 612 | 7.6965 | 7.7549 | -0.0683 | -0.2293 | 0.0927 | 83 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 204 | 0.2595 | 0.2539 | 0.0056 | -0.0085 | 0.0197 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 204 | 0.2453 | 0.2376 | 0.0055 | -0.0073 | 0.0184 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 204 | 0.2578 | 0.2537 | 0.0055 | -0.0086 | 0.0195 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 612 | 0.2542 | 0.2484 | 0.0055 | -0.0020 | 0.0131 | 83 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0094; ECE 0.0269; logistic slope 0.896 (SE 0.134), intercept 0.061 (SE 0.088). Brier decomposition: reliability 0.0026, resolution 0.0217, uncertainty 0.2461.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 1 | 0.1688 | 0.0000 | 0.0000 | 0.7935 |
| [0.2, 0.3) | 31 | 0.2639 | 0.2258 | 0.1139 | 0.3981 |
| [0.3, 0.4) | 83 | 0.3565 | 0.3855 | 0.2881 | 0.4931 |
| [0.4, 0.5) | 121 | 0.4511 | 0.4628 | 0.3765 | 0.5514 |
| [0.5, 0.6) | 128 | 0.5532 | 0.6016 | 0.5150 | 0.6822 |
| [0.6, 0.7) | 120 | 0.6471 | 0.6417 | 0.5527 | 0.7218 |
| [0.7, 0.8) | 105 | 0.7419 | 0.7524 | 0.6619 | 0.8251 |
| [0.8, 0.9) | 22 | 0.8375 | 0.7273 | 0.5185 | 0.8685 |
| [0.9, 1.0] | 1 | 0.9149 | 0.0000 | 0.0000 | 0.7935 |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2024 | 0.0440 | 0.8889 | 204 | 0.2260 | 0.2257 | -0.0010 | -0.0037 | 0.0018 | SPANS_ZERO |
| 2025 | 0.0906 | 0.8713 | 204 | 0.2298 | 0.2298 | -0.0003 | -0.0031 | 0.0025 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 2.0000 | 1.1000 | 17.7572 | 384.0000 |
| 180.0000 | 2.0000 | 1.2000 | 17.7574 | 384.0000 |
| 180.0000 | 2.0000 | 1.3000 | 17.7721 | 384.0000 |
| 180.0000 | 2.0000 | 1.0000 | 17.7748 | 384.0000 |
| 180.0000 | 1.0000 | 1.2000 | 17.7760 | 384.0000 |
| 180.0000 | 1.0000 | 1.1000 | 17.7767 | 384.0000 |
| 180.0000 | 1.0000 | 1.3000 | 17.7899 | 384.0000 |
| 180.0000 | 1.0000 | 1.0000 | 17.7951 | 384.0000 |
| 90.0000 | 2.0000 | 1.3000 | 17.8194 | 384.0000 |
| 90.0000 | 2.0000 | 1.2000 | 17.8203 | 384.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:04:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: RL-NRL-JOINT-r1
- `archive_snapshot_sha256`: e6ae0e16ed76975379c4e355e58b8f06a0155738636c942807d2b97c3ce8751c
- `seconds`: 103

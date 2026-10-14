# Development results: `BKB-NBA-G-LEAGUE-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 527 | 0.2368 | 0.2487 | -0.0108 | -0.0190 | -0.0026 | 14 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 527 | 0.2425 | 0.2490 | -0.0056 | -0.0118 | 0.0006 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 558 | 0.2369 | 0.2479 | -0.0102 | -0.0197 | -0.0008 | 15 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 1612 | 0.2387 | 0.2485 | -0.0089 | -0.0133 | -0.0045 | 43 | BELOW_ZERO |
| Home-win log loss | 2023 | 527 | 0.6654 | 0.6905 | -0.0229 | -0.0399 | -0.0060 | 14 | BELOW_ZERO |
| Home-win log loss | 2024 | 527 | 0.6779 | 0.6912 | -0.0115 | -0.0245 | 0.0015 | 14 | SPANS_ZERO |
| Home-win log loss | 2025 | 558 | 0.6667 | 0.6890 | -0.0207 | -0.0404 | -0.0011 | 15 | BELOW_ZERO |
| Home-win log loss | ALL | 1612 | 0.6699 | 0.6902 | -0.0184 | -0.0275 | -0.0094 | 43 | BELOW_ZERO |
| Margin CRPS | 2023 | 527 | 7.8726 | 8.2154 | -0.3210 | -0.5241 | -0.1179 | 14 | BELOW_ZERO |
| Margin CRPS | 2024 | 527 | 8.0592 | 8.2831 | -0.1947 | -0.3942 | 0.0048 | 14 | SPANS_ZERO |
| Margin CRPS | 2025 | 558 | 7.8114 | 8.1240 | -0.3010 | -0.4582 | -0.1437 | 15 | BELOW_ZERO |
| Margin CRPS | ALL | 1612 | 7.9124 | 8.2059 | -0.2729 | -0.3727 | -0.1730 | 43 | BELOW_ZERO |
| Total CRPS | 2023 | 527 | 10.8764 | 11.4416 | -0.5454 | -0.9804 | -0.1105 | 14 | BELOW_ZERO |
| Total CRPS | 2024 | 527 | 10.9849 | 11.6018 | -0.6519 | -1.0614 | -0.2424 | 14 | BELOW_ZERO |
| Total CRPS | 2025 | 558 | 10.6869 | 11.4290 | -0.7097 | -1.1107 | -0.3087 | 15 | BELOW_ZERO |
| Total CRPS | ALL | 1612 | 10.8463 | 11.4896 | -0.6374 | -0.8574 | -0.4174 | 43 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 527 | 0.2364 | 0.2487 | -0.0123 | -0.0255 | 0.0009 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 527 | 0.2348 | 0.2492 | -0.0154 | -0.0305 | -0.0002 | 14 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 558 | 0.2279 | 0.2498 | -0.0209 | -0.0338 | -0.0080 | 15 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 1612 | 0.2329 | 0.2492 | -0.0163 | -0.0236 | -0.0090 | 43 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 527 | 0.2368 | 0.2389 | -0.0014 | -0.0058 | 0.0029 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 527 | 0.2425 | 0.2438 | -0.0007 | -0.0046 | 0.0033 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 558 | 0.2369 | 0.2387 | -0.0019 | -0.0062 | 0.0025 | 15 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 1612 | 0.2387 | 0.2405 | -0.0014 | -0.0036 | 0.0009 | 43 | SPANS_ZERO |
| Home-win log loss | 2023 | 527 | 0.6654 | 0.6704 | -0.0037 | -0.0127 | 0.0053 | 14 | SPANS_ZERO |
| Home-win log loss | 2024 | 527 | 0.6779 | 0.6806 | -0.0015 | -0.0097 | 0.0067 | 14 | SPANS_ZERO |
| Home-win log loss | 2025 | 558 | 0.6667 | 0.6703 | -0.0038 | -0.0130 | 0.0054 | 15 | SPANS_ZERO |
| Home-win log loss | ALL | 1612 | 0.6699 | 0.6737 | -0.0030 | -0.0077 | 0.0017 | 43 | SPANS_ZERO |
| Margin CRPS | 2023 | 527 | 7.8726 | 7.9399 | -0.0573 | -0.1757 | 0.0611 | 14 | SPANS_ZERO |
| Margin CRPS | 2024 | 527 | 8.0592 | 8.1294 | -0.0522 | -0.1665 | 0.0621 | 14 | SPANS_ZERO |
| Margin CRPS | 2025 | 558 | 7.8114 | 7.8462 | -0.0349 | -0.1228 | 0.0531 | 15 | SPANS_ZERO |
| Margin CRPS | ALL | 1612 | 7.9124 | 7.9694 | -0.0478 | -0.1043 | 0.0086 | 43 | SPANS_ZERO |
| Total CRPS | 2023 | 527 | 10.8764 | 10.9736 | -0.0698 | -0.2264 | 0.0867 | 14 | SPANS_ZERO |
| Total CRPS | 2024 | 527 | 10.9849 | 11.0618 | -0.1017 | -0.2562 | 0.0529 | 14 | SPANS_ZERO |
| Total CRPS | 2025 | 558 | 10.6869 | 10.8251 | -0.1302 | -0.2669 | 0.0064 | 15 | SPANS_ZERO |
| Total CRPS | ALL | 1612 | 10.8463 | 10.9510 | -0.1013 | -0.1802 | -0.0223 | 43 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 527 | 0.2364 | 0.2374 | -0.0005 | -0.0048 | 0.0038 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 527 | 0.2348 | 0.2371 | -0.0031 | -0.0086 | 0.0025 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 558 | 0.2279 | 0.2322 | -0.0040 | -0.0079 | -0.0000 | 15 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 1612 | 0.2329 | 0.2355 | -0.0026 | -0.0050 | -0.0001 | 43 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0158; ECE 0.0180; logistic slope 0.901 (SE 0.114), intercept 0.076 (SE 0.052). Brier decomposition: reliability 0.0009, resolution 0.0100, uncertainty 0.2483.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 1 | 0.1918 | 0.0000 | 0.0000 | 0.7935 |
| [0.2, 0.3) | 53 | 0.2662 | 0.2830 | 0.1797 | 0.4157 |
| [0.3, 0.4) | 155 | 0.3591 | 0.3613 | 0.2899 | 0.4394 |
| [0.4, 0.5) | 433 | 0.4584 | 0.5127 | 0.4657 | 0.5595 |
| [0.5, 0.6) | 576 | 0.5495 | 0.5521 | 0.5113 | 0.5922 |
| [0.6, 0.7) | 310 | 0.6431 | 0.6419 | 0.5871 | 0.6933 |
| [0.7, 0.8) | 78 | 0.7333 | 0.7179 | 0.6097 | 0.8057 |
| [0.8, 0.9) | 6 | 0.8281 | 1.0000 | 0.6097 | 1.0000 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.0968 | 1.0071 | 527 | 0.2368 | 0.2380 | 0.0012 | -0.0005 | 0.0030 | SPANS_ZERO |
| 2024 | 0.0636 | 1.0060 | 527 | 0.2425 | 0.2427 | 0.0000 | -0.0016 | 0.0016 | SPANS_ZERO |
| 2025 | 0.0330 | 0.7931 | 558 | 0.2369 | 0.2368 | -0.0002 | -0.0021 | 0.0016 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 8.0000 | 1.1000 | 18.3203 | 938.0000 |
| 90.0000 | 8.0000 | 1.2000 | 18.3278 | 938.0000 |
| 90.0000 | 8.0000 | 1.0000 | 18.3313 | 938.0000 |
| 45.0000 | 8.0000 | 1.2000 | 18.3471 | 938.0000 |
| 45.0000 | 8.0000 | 1.1000 | 18.3484 | 938.0000 |
| 90.0000 | 8.0000 | 1.3000 | 18.3504 | 938.0000 |
| 45.0000 | 8.0000 | 1.3000 | 18.3611 | 938.0000 |
| 45.0000 | 8.0000 | 1.0000 | 18.3684 | 938.0000 |
| 180.0000 | 8.0000 | 1.0000 | 18.3703 | 938.0000 |
| 180.0000 | 8.0000 | 1.1000 | 18.3750 | 938.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:03:08Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBA-G-LEAGUE-JOINT-r1
- `archive_snapshot_sha256`: b6b7e881eb74f963f6205432acbafb818949b56e753a63e0621b23d1069bce85
- `seconds`: 98

# Development results: `BSB-KBO-NB-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 747 | 0.2494 | 0.2511 | -0.0021 | -0.0057 | 0.0015 | 31 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 720 | 0.2501 | 0.2507 | -0.0013 | -0.0050 | 0.0025 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 720 | 0.2465 | 0.2503 | -0.0041 | -0.0083 | 0.0001 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 2187 | 0.2487 | 0.2507 | -0.0025 | -0.0046 | -0.0003 | 89 | BELOW_ZERO |
| Home-win log loss | 2023 | 747 | 0.6921 | 0.6954 | -0.0042 | -0.0115 | 0.0030 | 31 | SPANS_ZERO |
| Home-win log loss | 2024 | 720 | 0.6934 | 0.6945 | -0.0025 | -0.0100 | 0.0050 | 29 | SPANS_ZERO |
| Home-win log loss | 2025 | 720 | 0.6862 | 0.6938 | -0.0082 | -0.0168 | 0.0004 | 29 | SPANS_ZERO |
| Home-win log loss | ALL | 2187 | 0.6906 | 0.6946 | -0.0050 | -0.0093 | -0.0006 | 89 | BELOW_ZERO |
| Margin CRPS | 2023 | 747 | 2.5344 | 2.5445 | -0.0132 | -0.0369 | 0.0106 | 31 | SPANS_ZERO |
| Margin CRPS | 2024 | 720 | 2.8247 | 2.8185 | -0.0007 | -0.0308 | 0.0293 | 29 | SPANS_ZERO |
| Margin CRPS | 2025 | 720 | 2.6095 | 2.6441 | -0.0350 | -0.0660 | -0.0040 | 29 | BELOW_ZERO |
| Margin CRPS | ALL | 2187 | 2.6547 | 2.6675 | -0.0162 | -0.0322 | -0.0003 | 89 | BELOW_ZERO |
| Total CRPS | 2023 | 747 | 2.5985 | 2.5935 | -0.0017 | -0.0280 | 0.0245 | 31 | SPANS_ZERO |
| Total CRPS | 2024 | 720 | 2.9499 | 2.9884 | -0.0386 | -0.0688 | -0.0084 | 29 | BELOW_ZERO |
| Total CRPS | 2025 | 720 | 2.6565 | 2.6544 | 0.0025 | -0.0260 | 0.0309 | 29 | SPANS_ZERO |
| Total CRPS | ALL | 2187 | 2.7333 | 2.7436 | -0.0124 | -0.0285 | 0.0038 | 89 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 747 | 0.2462 | 0.2452 | -0.0003 | -0.0043 | 0.0037 | 31 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 720 | 0.2543 | 0.2602 | -0.0055 | -0.0099 | -0.0012 | 29 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 720 | 0.2465 | 0.2466 | 0.0002 | -0.0041 | 0.0045 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 2187 | 0.2490 | 0.2506 | -0.0019 | -0.0043 | 0.0006 | 89 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 747 | 0.2494 | 0.2508 | -0.0018 | -0.0041 | 0.0005 | 31 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 720 | 0.2501 | 0.2508 | -0.0004 | -0.0033 | 0.0024 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 720 | 0.2465 | 0.2467 | -0.0001 | -0.0022 | 0.0020 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 2187 | 0.2487 | 0.2495 | -0.0008 | -0.0022 | 0.0006 | 89 | SPANS_ZERO |
| Home-win log loss | 2023 | 747 | 0.6921 | 0.6948 | -0.0036 | -0.0083 | 0.0012 | 31 | SPANS_ZERO |
| Home-win log loss | 2024 | 720 | 0.6934 | 0.6948 | -0.0008 | -0.0065 | 0.0049 | 29 | SPANS_ZERO |
| Home-win log loss | 2025 | 720 | 0.6862 | 0.6865 | -0.0002 | -0.0045 | 0.0041 | 29 | SPANS_ZERO |
| Home-win log loss | ALL | 2187 | 0.6906 | 0.6921 | -0.0016 | -0.0043 | 0.0012 | 89 | SPANS_ZERO |
| Margin CRPS | 2023 | 747 | 2.5344 | 2.5610 | -0.0280 | -0.0478 | -0.0081 | 31 | BELOW_ZERO |
| Margin CRPS | 2024 | 720 | 2.8247 | 2.8315 | -0.0060 | -0.0218 | 0.0099 | 29 | SPANS_ZERO |
| Margin CRPS | 2025 | 720 | 2.6095 | 2.6262 | -0.0171 | -0.0355 | 0.0014 | 29 | SPANS_ZERO |
| Margin CRPS | ALL | 2187 | 2.6547 | 2.6715 | -0.0172 | -0.0275 | -0.0070 | 89 | BELOW_ZERO |
| Total CRPS | 2023 | 747 | 2.5985 | 2.6093 | -0.0161 | -0.0326 | 0.0004 | 31 | SPANS_ZERO |
| Total CRPS | 2024 | 720 | 2.9499 | 2.9320 | 0.0108 | -0.0297 | 0.0513 | 29 | SPANS_ZERO |
| Total CRPS | 2025 | 720 | 2.6565 | 2.6829 | -0.0212 | -0.0482 | 0.0059 | 29 | SPANS_ZERO |
| Total CRPS | ALL | 2187 | 2.7333 | 2.7398 | -0.0090 | -0.0254 | 0.0075 | 89 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 747 | 0.2462 | 0.2468 | -0.0024 | -0.0068 | 0.0019 | 31 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 720 | 0.2543 | 0.2502 | 0.0020 | -0.0061 | 0.0102 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 720 | 0.2465 | 0.2489 | -0.0015 | -0.0056 | 0.0026 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 2187 | 0.2490 | 0.2486 | -0.0007 | -0.0039 | 0.0026 | 89 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0222; ECE 0.0230; logistic slope 0.818 (SE 0.205), intercept 0.077 (SE 0.045). Brier decomposition: reliability 0.0009, resolution 0.0017, uncertainty 0.2500.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 1 | 0.2982 | 1.0000 | 0.2065 | 1.0000 |
| [0.3, 0.4) | 108 | 0.3751 | 0.3704 | 0.2852 | 0.4644 |
| [0.4, 0.5) | 1257 | 0.4579 | 0.4909 | 0.4633 | 0.5185 |
| [0.5, 0.6) | 783 | 0.5308 | 0.5402 | 0.5052 | 0.5749 |
| [0.6, 0.7) | 38 | 0.6166 | 0.6053 | 0.4472 | 0.7440 |
| [0.7, 0.8) | 0 | — | — | — | — |
| [0.8, 0.9) | 0 | — | — | — | — |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.0681 | 1.2778 | 747 | 0.2494 | 0.2490 | -0.0003 | -0.0016 | 0.0010 | SPANS_ZERO |
| 2024 | 0.1628 | 0.9377 | 720 | 0.2501 | 0.2505 | -0.0001 | -0.0036 | 0.0035 | SPANS_ZERO |
| 2025 | 0.0376 | 0.5096 | 720 | 0.2465 | 0.2473 | 0.0005 | -0.0022 | 0.0033 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 180.0000 | 128.0000 | 5.2730 | 1490.0000 |
| 90.0000 | 128.0000 | 5.2746 | 1490.0000 |
| 180.0000 | 64.0000 | 5.2757 | 1490.0000 |
| 365.0000 | 128.0000 | 5.2778 | 1490.0000 |
| 180.0000 | 32.0000 | 5.2778 | 1490.0000 |
| 180.0000 | 16.0000 | 5.2793 | 1490.0000 |
| 365.0000 | 64.0000 | 5.2793 | 1490.0000 |
| 365.0000 | 32.0000 | 5.2804 | 1490.0000 |
| 180.0000 | 4.0000 | 5.2805 | 1490.0000 |
| 180.0000 | 1.0000 | 5.2809 | 1490.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:01:27Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-KBO-NB-r1
- `archive_snapshot_sha256`: fa56bb7595bb5f65f52984e32765222d2035a1c6b67d78f3ba901b81d50d6a25
- `seconds`: 138

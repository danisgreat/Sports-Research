# Development results: `IH-NHL-REG-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 1312 | 0.2345 | 0.2483 | -0.0117 | -0.0172 | -0.0062 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 1312 | 0.2370 | 0.2467 | -0.0088 | -0.0138 | -0.0038 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 1312 | 0.2487 | 0.2498 | -0.0019 | -0.0066 | 0.0027 | 26 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 3936 | 0.2401 | 0.2483 | -0.0076 | -0.0106 | -0.0047 | 82 | BELOW_ZERO |
| Home-win log loss | 2023 | 1312 | 0.6610 | 0.6898 | -0.0244 | -0.0359 | -0.0130 | 28 | BELOW_ZERO |
| Home-win log loss | 2024 | 1312 | 0.6666 | 0.6865 | -0.0182 | -0.0287 | -0.0078 | 28 | BELOW_ZERO |
| Home-win log loss | 2025 | 1312 | 0.6906 | 0.6928 | -0.0039 | -0.0136 | 0.0059 | 26 | SPANS_ZERO |
| Home-win log loss | ALL | 3936 | 0.6727 | 0.6897 | -0.0158 | -0.0220 | -0.0096 | 82 | BELOW_ZERO |
| Margin CRPS | 2023 | 1312 | 1.4530 | 1.5166 | -0.0543 | -0.0788 | -0.0297 | 28 | BELOW_ZERO |
| Margin CRPS | 2024 | 1312 | 1.4463 | 1.4811 | -0.0314 | -0.0551 | -0.0077 | 28 | BELOW_ZERO |
| Margin CRPS | 2025 | 1312 | 1.4407 | 1.4549 | -0.0164 | -0.0354 | 0.0026 | 26 | SPANS_ZERO |
| Margin CRPS | ALL | 3936 | 1.4467 | 1.4842 | -0.0345 | -0.0475 | -0.0215 | 82 | BELOW_ZERO |
| Total CRPS | 2023 | 1312 | 1.2912 | 1.2895 | 0.0041 | -0.0087 | 0.0168 | 28 | SPANS_ZERO |
| Total CRPS | 2024 | 1312 | 1.3014 | 1.2978 | 0.0099 | -0.0066 | 0.0264 | 28 | SPANS_ZERO |
| Total CRPS | 2025 | 1312 | 1.2835 | 1.2806 | 0.0029 | -0.0071 | 0.0129 | 26 | SPANS_ZERO |
| Total CRPS | ALL | 3936 | 1.2920 | 1.2893 | 0.0057 | -0.0018 | 0.0132 | 82 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 1312 | 0.2487 | 0.2484 | 0.0006 | -0.0023 | 0.0035 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 1312 | 0.2451 | 0.2449 | 0.0020 | -0.0023 | 0.0062 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 1312 | 0.2506 | 0.2497 | 0.0008 | -0.0018 | 0.0034 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 3936 | 0.2481 | 0.2477 | 0.0011 | -0.0007 | 0.0030 | 82 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 1312 | 0.2345 | 0.2416 | -0.0061 | -0.0097 | -0.0025 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 1312 | 0.2370 | 0.2431 | -0.0051 | -0.0092 | -0.0010 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 1312 | 0.2487 | 0.2473 | 0.0008 | -0.0027 | 0.0043 | 26 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 3936 | 0.2401 | 0.2440 | -0.0036 | -0.0057 | -0.0014 | 82 | BELOW_ZERO |
| Home-win log loss | 2023 | 1312 | 0.6610 | 0.6762 | -0.0130 | -0.0206 | -0.0053 | 28 | BELOW_ZERO |
| Home-win log loss | 2024 | 1312 | 0.6666 | 0.6792 | -0.0106 | -0.0193 | -0.0020 | 28 | BELOW_ZERO |
| Home-win log loss | 2025 | 1312 | 0.6906 | 0.6877 | 0.0017 | -0.0056 | 0.0091 | 26 | SPANS_ZERO |
| Home-win log loss | ALL | 3936 | 0.6727 | 0.6810 | -0.0075 | -0.0121 | -0.0029 | 82 | BELOW_ZERO |
| Margin CRPS | 2023 | 1312 | 1.4530 | 1.5003 | -0.0435 | -0.0574 | -0.0297 | 28 | BELOW_ZERO |
| Margin CRPS | 2024 | 1312 | 1.4463 | 1.4803 | -0.0292 | -0.0477 | -0.0107 | 28 | BELOW_ZERO |
| Margin CRPS | 2025 | 1312 | 1.4407 | 1.4586 | -0.0198 | -0.0346 | -0.0049 | 26 | BELOW_ZERO |
| Margin CRPS | ALL | 3936 | 1.4467 | 1.4797 | -0.0311 | -0.0402 | -0.0220 | 82 | BELOW_ZERO |
| Total CRPS | 2023 | 1312 | 1.2912 | 1.2999 | -0.0081 | -0.0175 | 0.0013 | 28 | SPANS_ZERO |
| Total CRPS | 2024 | 1312 | 1.3014 | 1.3233 | -0.0204 | -0.0462 | 0.0054 | 28 | SPANS_ZERO |
| Total CRPS | 2025 | 1312 | 1.2835 | 1.2924 | -0.0081 | -0.0179 | 0.0016 | 26 | SPANS_ZERO |
| Total CRPS | ALL | 3936 | 1.2920 | 1.3052 | -0.0123 | -0.0218 | -0.0028 | 82 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 1312 | 0.2487 | 0.2471 | 0.0019 | -0.0001 | 0.0039 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 1312 | 0.2451 | 0.2464 | -0.0003 | -0.0060 | 0.0055 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 1312 | 0.2506 | 0.2485 | 0.0022 | 0.0003 | 0.0041 | 26 | ABOVE_ZERO |
| Over the league-median line, Brier | ALL | 3936 | 0.2481 | 0.2473 | 0.0012 | -0.0009 | 0.0033 | 82 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0063; ECE 0.0085; logistic slope 0.944 (SE 0.084), intercept 0.034 (SE 0.034). Brier decomposition: reliability 0.0002, resolution 0.0083, uncertainty 0.2482.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 27 | 0.2872 | 0.3333 | 0.1864 | 0.5218 |
| [0.3, 0.4) | 290 | 0.3585 | 0.3552 | 0.3023 | 0.4118 |
| [0.4, 0.5) | 1041 | 0.4562 | 0.4726 | 0.4425 | 0.5030 |
| [0.5, 0.6) | 1569 | 0.5478 | 0.5513 | 0.5266 | 0.5758 |
| [0.6, 0.7) | 838 | 0.6400 | 0.6360 | 0.6029 | 0.6679 |
| [0.7, 0.8) | 168 | 0.7348 | 0.7619 | 0.6921 | 0.8200 |
| [0.8, 0.9) | 3 | 0.8050 | 1.0000 | 0.4385 | 1.0000 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.0402 | 1.1329 | 1312 | 0.2345 | 0.2346 | 0.0004 | -0.0003 | 0.0011 | SPANS_ZERO |
| 2024 | 0.0315 | 1.0953 | 1312 | 0.2370 | 0.2366 | -0.0003 | -0.0009 | 0.0004 | SPANS_ZERO |
| 2025 | 0.1063 | 1.0187 | 1312 | 0.2487 | 0.2503 | 0.0015 | 0.0002 | 0.0029 | ABOVE_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 180.0000 | 32.0000 | 2.7131 | 2624.0000 |
| 180.0000 | 16.0000 | 2.7135 | 2624.0000 |
| 90.0000 | 32.0000 | 2.7137 | 2624.0000 |
| 180.0000 | 64.0000 | 2.7151 | 2624.0000 |
| 180.0000 | 4.0000 | 2.7153 | 2624.0000 |
| 90.0000 | 16.0000 | 2.7158 | 2624.0000 |
| 180.0000 | 1.0000 | 2.7161 | 2624.0000 |
| 90.0000 | 64.0000 | 2.7167 | 2624.0000 |
| 365.0000 | 32.0000 | 2.7209 | 2624.0000 |
| 365.0000 | 16.0000 | 2.7211 | 2624.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:06:07Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: IH-NHL-REG-r1
- `archive_snapshot_sha256`: 6621881af29ea6ad02308dd6bff3bcd337b47daaca7d44980656ed5771d0ecce
- `seconds`: 179

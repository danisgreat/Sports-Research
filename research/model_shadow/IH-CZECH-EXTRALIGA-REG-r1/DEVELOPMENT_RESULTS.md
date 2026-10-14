# Development results: `IH-CZECH-EXTRALIGA-REG-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 364 | 0.2283 | 0.2481 | -0.0235 | -0.0342 | -0.0129 | 23 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 364 | 0.2425 | 0.2428 | -0.0023 | -0.0097 | 0.0052 | 23 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 364 | 0.2342 | 0.2408 | -0.0114 | -0.0239 | 0.0011 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 1092 | 0.2350 | 0.2439 | -0.0124 | -0.0185 | -0.0063 | 70 | BELOW_ZERO |
| Home-win log loss | 2023 | 364 | 0.6485 | 0.6894 | -0.0484 | -0.0700 | -0.0268 | 23 | BELOW_ZERO |
| Home-win log loss | 2024 | 364 | 0.6774 | 0.6787 | -0.0052 | -0.0209 | 0.0106 | 23 | SPANS_ZERO |
| Home-win log loss | 2025 | 364 | 0.6609 | 0.6747 | -0.0235 | -0.0488 | 0.0019 | 24 | SPANS_ZERO |
| Home-win log loss | ALL | 1092 | 0.6623 | 0.6809 | -0.0256 | -0.0381 | -0.0132 | 70 | BELOW_ZERO |
| Margin CRPS | 2023 | 364 | 1.3741 | 1.4525 | -0.0839 | -0.1142 | -0.0537 | 23 | BELOW_ZERO |
| Margin CRPS | 2024 | 364 | 1.3351 | 1.3435 | -0.0113 | -0.0402 | 0.0175 | 23 | SPANS_ZERO |
| Margin CRPS | 2025 | 364 | 1.3171 | 1.3496 | -0.0389 | -0.0744 | -0.0034 | 24 | BELOW_ZERO |
| Margin CRPS | ALL | 1092 | 1.3421 | 1.3819 | -0.0446 | -0.0634 | -0.0258 | 70 | BELOW_ZERO |
| Total CRPS | 2023 | 364 | 1.1929 | 1.2085 | -0.0142 | -0.0326 | 0.0042 | 23 | SPANS_ZERO |
| Total CRPS | 2024 | 364 | 1.2071 | 1.2042 | -0.0055 | -0.0278 | 0.0169 | 23 | SPANS_ZERO |
| Total CRPS | 2025 | 364 | 1.2261 | 1.2276 | -0.0057 | -0.0237 | 0.0123 | 24 | SPANS_ZERO |
| Total CRPS | ALL | 1092 | 1.2087 | 1.2134 | -0.0084 | -0.0192 | 0.0024 | 70 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 364 | 0.2457 | 0.2500 | -0.0039 | -0.0088 | 0.0009 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 364 | 0.2394 | 0.2406 | -0.0028 | -0.0078 | 0.0022 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 364 | 0.2410 | 0.2406 | -0.0027 | -0.0087 | 0.0033 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 1092 | 0.2420 | 0.2437 | -0.0031 | -0.0061 | -0.0002 | 70 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 364 | 0.2283 | 0.2363 | -0.0103 | -0.0167 | -0.0039 | 23 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 364 | 0.2425 | 0.2430 | -0.0034 | -0.0117 | 0.0049 | 23 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 364 | 0.2342 | 0.2361 | -0.0028 | -0.0102 | 0.0045 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 1092 | 0.2350 | 0.2384 | -0.0055 | -0.0096 | -0.0013 | 70 | BELOW_ZERO |
| Home-win log loss | 2023 | 364 | 0.6485 | 0.6649 | -0.0211 | -0.0340 | -0.0082 | 23 | BELOW_ZERO |
| Home-win log loss | 2024 | 364 | 0.6774 | 0.6790 | -0.0074 | -0.0248 | 0.0099 | 23 | SPANS_ZERO |
| Home-win log loss | 2025 | 364 | 0.6609 | 0.6647 | -0.0058 | -0.0207 | 0.0091 | 24 | SPANS_ZERO |
| Home-win log loss | ALL | 1092 | 0.6623 | 0.6695 | -0.0114 | -0.0198 | -0.0029 | 70 | BELOW_ZERO |
| Margin CRPS | 2023 | 364 | 1.3741 | 1.4268 | -0.0581 | -0.0789 | -0.0373 | 23 | BELOW_ZERO |
| Margin CRPS | 2024 | 364 | 1.3351 | 1.3641 | -0.0350 | -0.0621 | -0.0080 | 23 | BELOW_ZERO |
| Margin CRPS | 2025 | 364 | 1.3171 | 1.3499 | -0.0312 | -0.0594 | -0.0030 | 24 | BELOW_ZERO |
| Margin CRPS | ALL | 1092 | 1.3421 | 1.3803 | -0.0413 | -0.0556 | -0.0270 | 70 | BELOW_ZERO |
| Total CRPS | 2023 | 364 | 1.1929 | 1.2073 | -0.0175 | -0.0317 | -0.0033 | 23 | BELOW_ZERO |
| Total CRPS | 2024 | 364 | 1.2071 | 1.2262 | -0.0254 | -0.0463 | -0.0045 | 23 | BELOW_ZERO |
| Total CRPS | 2025 | 364 | 1.2261 | 1.2486 | -0.0300 | -0.0480 | -0.0121 | 24 | BELOW_ZERO |
| Total CRPS | ALL | 1092 | 1.2087 | 1.2273 | -0.0244 | -0.0343 | -0.0145 | 70 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 364 | 0.2457 | 0.2477 | -0.0058 | -0.0154 | 0.0037 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 364 | 0.2394 | 0.2432 | -0.0059 | -0.0136 | 0.0018 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 364 | 0.2410 | 0.2439 | -0.0074 | -0.0162 | 0.0013 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 1092 | 0.2420 | 0.2449 | -0.0064 | -0.0112 | -0.0016 | 70 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0073; ECE 0.0177; logistic slope 1.244 (SE 0.196), intercept -0.036 (SE 0.082). Brier decomposition: reliability 0.0010, resolution 0.0087, uncertainty 0.2439.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 0 | — | — | — | — |
| [0.3, 0.4) | 15 | 0.3830 | 0.5333 | 0.3012 | 0.7519 |
| [0.4, 0.5) | 200 | 0.4632 | 0.4350 | 0.3682 | 0.5043 |
| [0.5, 0.6) | 470 | 0.5519 | 0.5574 | 0.5123 | 0.6017 |
| [0.6, 0.7) | 354 | 0.6403 | 0.6497 | 0.5987 | 0.6976 |
| [0.7, 0.8) | 53 | 0.7269 | 0.8302 | 0.7077 | 0.9080 |
| [0.8, 0.9) | 0 | — | — | — | — |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.1216 | 1.1860 | 364 | 0.2283 | 0.2259 | -0.0037 | -0.0073 | -0.0001 | BELOW_ZERO |
| 2024 | -0.3366 | 1.9697 | 364 | 0.2425 | 0.2528 | 0.0083 | 0.0010 | 0.0156 | ABOVE_ZERO |
| 2025 | 0.1721 | 0.5038 | 364 | 0.2342 | 0.2358 | 0.0037 | -0.0028 | 0.0102 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 180.0000 | 64.0000 | 2.4827 | 784.0000 |
| 180.0000 | 32.0000 | 2.4837 | 784.0000 |
| 365.0000 | 64.0000 | 2.4848 | 784.0000 |
| 365.0000 | 128.0000 | 2.4851 | 784.0000 |
| 180.0000 | 16.0000 | 2.4877 | 784.0000 |
| 365.0000 | 32.0000 | 2.4879 | 784.0000 |
| 180.0000 | 128.0000 | 2.4880 | 784.0000 |
| 730.0000 | 128.0000 | 2.4884 | 784.0000 |
| 90.0000 | 32.0000 | 2.4887 | 784.0000 |
| 90.0000 | 64.0000 | 2.4906 | 784.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:03:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: IH-CZECH-EXTRALIGA-REG-r1
- `archive_snapshot_sha256`: d55afa9fd1088e934e4d4fa18cb976587e44e9bdbb05afed6b9644c806ec2ed3
- `seconds`: 80

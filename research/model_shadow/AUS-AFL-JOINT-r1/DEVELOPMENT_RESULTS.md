# Development results: `AUS-AFL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 207 | 0.2126 | 0.2457 | -0.0344 | -0.0626 | -0.0062 | 24 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 207 | 0.2104 | 0.2450 | -0.0324 | -0.0635 | -0.0013 | 25 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 207 | 0.1774 | 0.2462 | -0.0718 | -0.0982 | -0.0454 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 621 | 0.2001 | 0.2456 | -0.0467 | -0.0630 | -0.0304 | 75 | BELOW_ZERO |
| Home-win log loss | 2023 | 207 | 0.6159 | 0.6845 | -0.0722 | -0.1421 | -0.0022 | 24 | BELOW_ZERO |
| Home-win log loss | 2024 | 207 | 0.6041 | 0.6831 | -0.0737 | -0.1446 | -0.0029 | 25 | BELOW_ZERO |
| Home-win log loss | 2025 | 207 | 0.5282 | 0.6855 | -0.1653 | -0.2283 | -0.1022 | 26 | BELOW_ZERO |
| Home-win log loss | ALL | 621 | 0.5827 | 0.6844 | -0.1050 | -0.1436 | -0.0663 | 75 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 207 | 0.2162 | 0.2498 | -0.0349 | -0.0627 | -0.0070 | 24 | BELOW_ZERO |
| Three-way half-sum Brier | 2024 | 207 | 0.2173 | 0.2510 | -0.0316 | -0.0624 | -0.0008 | 25 | BELOW_ZERO |
| Three-way half-sum Brier | 2025 | 207 | 0.1811 | 0.2482 | -0.0703 | -0.0967 | -0.0438 | 26 | BELOW_ZERO |
| Three-way half-sum Brier | ALL | 621 | 0.2049 | 0.2497 | -0.0460 | -0.0622 | -0.0299 | 75 | BELOW_ZERO |
| Margin CRPS | 2023 | 207 | 19.4185 | 22.4495 | -3.1102 | -4.7855 | -1.4349 | 24 | BELOW_ZERO |
| Margin CRPS | 2024 | 207 | 19.0890 | 22.4703 | -3.1675 | -4.9683 | -1.3666 | 25 | BELOW_ZERO |
| Margin CRPS | 2025 | 207 | 19.1146 | 23.9502 | -5.4970 | -8.0462 | -2.9477 | 26 | BELOW_ZERO |
| Margin CRPS | ALL | 621 | 19.2074 | 22.9567 | -3.9567 | -5.1254 | -2.7881 | 75 | BELOW_ZERO |
| Total CRPS | 2023 | 207 | 17.2427 | 18.5214 | -1.2930 | -2.6390 | 0.0529 | 24 | SPANS_ZERO |
| Total CRPS | 2024 | 207 | 16.2239 | 15.9682 | 0.2431 | -0.5569 | 1.0430 | 25 | SPANS_ZERO |
| Total CRPS | 2025 | 207 | 17.0035 | 16.8298 | 0.5426 | -0.5917 | 1.6768 | 26 | SPANS_ZERO |
| Total CRPS | ALL | 621 | 16.8234 | 17.1065 | -0.1447 | -0.7824 | 0.4931 | 75 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 207 | 0.2290 | 0.2539 | -0.0247 | -0.0538 | 0.0045 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 207 | 0.2576 | 0.2522 | 0.0057 | -0.0107 | 0.0220 | 25 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 207 | 0.2493 | 0.2498 | 0.0053 | -0.0161 | 0.0268 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 621 | 0.2453 | 0.2519 | -0.0042 | -0.0170 | 0.0087 | 75 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 207 | 0.2126 | 0.2197 | -0.0078 | -0.0246 | 0.0090 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 207 | 0.2104 | 0.2177 | -0.0064 | -0.0233 | 0.0104 | 25 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 207 | 0.1774 | 0.2012 | -0.0255 | -0.0364 | -0.0146 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 621 | 0.2001 | 0.2128 | -0.0135 | -0.0220 | -0.0050 | 75 | BELOW_ZERO |
| Home-win log loss | 2023 | 207 | 0.6159 | 0.6295 | -0.0160 | -0.0603 | 0.0284 | 24 | SPANS_ZERO |
| Home-win log loss | 2024 | 207 | 0.6041 | 0.6251 | -0.0186 | -0.0595 | 0.0222 | 25 | SPANS_ZERO |
| Home-win log loss | 2025 | 207 | 0.5282 | 0.5906 | -0.0670 | -0.0953 | -0.0386 | 26 | BELOW_ZERO |
| Home-win log loss | ALL | 621 | 0.5827 | 0.6151 | -0.0345 | -0.0562 | -0.0129 | 75 | BELOW_ZERO |
| Margin CRPS | 2023 | 207 | 19.4185 | 20.4416 | -1.0678 | -2.0243 | -0.1113 | 24 | BELOW_ZERO |
| Margin CRPS | 2024 | 207 | 19.0890 | 20.2391 | -1.0710 | -2.0686 | -0.0734 | 25 | BELOW_ZERO |
| Margin CRPS | 2025 | 207 | 19.1146 | 20.8156 | -2.0198 | -3.1220 | -0.9175 | 26 | BELOW_ZERO |
| Margin CRPS | ALL | 621 | 19.2074 | 20.4988 | -1.3989 | -1.9723 | -0.8254 | 75 | BELOW_ZERO |
| Total CRPS | 2023 | 207 | 17.2427 | 16.8943 | 0.3248 | -0.1276 | 0.7773 | 24 | SPANS_ZERO |
| Total CRPS | 2024 | 207 | 16.2239 | 15.9620 | 0.2659 | -0.2161 | 0.7479 | 25 | SPANS_ZERO |
| Total CRPS | 2025 | 207 | 17.0035 | 17.0541 | 0.1971 | -0.4316 | 0.8258 | 26 | SPANS_ZERO |
| Total CRPS | ALL | 621 | 16.8234 | 16.6368 | 0.2609 | -0.0320 | 0.5538 | 75 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 207 | 0.2290 | 0.2255 | 0.0027 | -0.0059 | 0.0113 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 207 | 0.2576 | 0.2534 | 0.0046 | -0.0049 | 0.0141 | 25 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 207 | 0.2493 | 0.2514 | 0.0019 | -0.0100 | 0.0139 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 621 | 0.2453 | 0.2434 | 0.0031 | -0.0026 | 0.0087 | 75 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0053; ECE 0.0314; logistic slope 0.993 (SE 0.105), intercept 0.028 (SE 0.092). Brier decomposition: reliability 0.0015, resolution 0.0458, uncertainty 0.2451.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 8 | 0.0734 | 0.0000 | 0.0000 | 0.3244 |
| [0.1, 0.2) | 27 | 0.1478 | 0.1111 | 0.0385 | 0.2806 |
| [0.2, 0.3) | 43 | 0.2534 | 0.2326 | 0.1315 | 0.3774 |
| [0.3, 0.4) | 64 | 0.3519 | 0.4219 | 0.3087 | 0.5439 |
| [0.4, 0.5) | 89 | 0.4532 | 0.4607 | 0.3609 | 0.5637 |
| [0.5, 0.6) | 110 | 0.5512 | 0.5455 | 0.4524 | 0.6354 |
| [0.6, 0.7) | 102 | 0.6477 | 0.6961 | 0.6010 | 0.7769 |
| [0.7, 0.8) | 84 | 0.7485 | 0.7024 | 0.5975 | 0.7896 |
| [0.8, 0.9) | 59 | 0.8495 | 0.8305 | 0.7154 | 0.9052 |
| [0.9, 1.0] | 35 | 0.9343 | 0.9714 | 0.8547 | 0.9949 |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2024 | 0.0378 | 0.7966 | 207 | 0.2104 | 0.2097 | -0.0009 | -0.0060 | 0.0042 | SPANS_ZERO |
| 2025 | 0.0567 | 0.8769 | 207 | 0.1774 | 0.1794 | 0.0022 | 0.0001 | 0.0043 | ABOVE_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 2.0000 | 1.2000 | 35.2135 | 396.0000 |
| 90.0000 | 2.0000 | 1.3000 | 35.2277 | 396.0000 |
| 90.0000 | 2.0000 | 1.1000 | 35.2294 | 396.0000 |
| 45.0000 | 2.0000 | 1.3000 | 35.2773 | 396.0000 |
| 90.0000 | 2.0000 | 1.0000 | 35.2821 | 396.0000 |
| 45.0000 | 2.0000 | 1.2000 | 35.3135 | 396.0000 |
| 90.0000 | 1.0000 | 1.2000 | 35.3351 | 396.0000 |
| 90.0000 | 1.0000 | 1.3000 | 35.3428 | 396.0000 |
| 90.0000 | 1.0000 | 1.1000 | 35.3579 | 396.0000 |
| 45.0000 | 2.0000 | 1.1000 | 35.3801 | 396.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:01:08Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUS-AFL-JOINT-r1
- `archive_snapshot_sha256`: ae44699d2ca08b3f169f285693e78b71fa9eb323ac967be745ff4c824c299e19
- `seconds`: 119

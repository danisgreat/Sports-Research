# Development results: `BKB-AUSTRIA-BASKETBALL-BUNDESLIGA-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 132 | 0.1080 | 0.1840 | -0.0760 | -0.1048 | -0.0471 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 132 | 0.1285 | 0.1646 | -0.0361 | -0.0657 | -0.0065 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 132 | 0.1320 | 0.2067 | -0.0747 | -0.1048 | -0.0446 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 396 | 0.1228 | 0.1851 | -0.0622 | -0.0790 | -0.0455 | 66 | BELOW_ZERO |
| Home-win log loss | 2023 | 132 | 0.3398 | 0.5547 | -0.2149 | -0.2782 | -0.1515 | 22 | BELOW_ZERO |
| Home-win log loss | 2024 | 132 | 0.3812 | 0.5118 | -0.1307 | -0.1948 | -0.0665 | 22 | BELOW_ZERO |
| Home-win log loss | 2025 | 132 | 0.3949 | 0.6046 | -0.2098 | -0.2787 | -0.1408 | 22 | BELOW_ZERO |
| Home-win log loss | ALL | 396 | 0.3720 | 0.5571 | -0.1851 | -0.2221 | -0.1481 | 66 | BELOW_ZERO |
| Margin CRPS | 2023 | 132 | 4.8230 | 7.5215 | -2.6984 | -3.3792 | -2.0177 | 22 | BELOW_ZERO |
| Margin CRPS | 2024 | 132 | 4.5547 | 6.8440 | -2.2893 | -3.0090 | -1.5696 | 22 | BELOW_ZERO |
| Margin CRPS | 2025 | 132 | 5.2208 | 7.9584 | -2.7376 | -3.4462 | -2.0289 | 22 | BELOW_ZERO |
| Margin CRPS | ALL | 396 | 4.8662 | 7.4413 | -2.5751 | -2.9622 | -2.1880 | 66 | BELOW_ZERO |
| Total CRPS | 2023 | 132 | 5.4354 | 5.3185 | 0.1169 | -0.1498 | 0.3836 | 22 | SPANS_ZERO |
| Total CRPS | 2024 | 132 | 5.2447 | 5.1264 | 0.1183 | -0.0458 | 0.2825 | 22 | SPANS_ZERO |
| Total CRPS | 2025 | 132 | 4.8586 | 4.9100 | -0.0514 | -0.2620 | 0.1591 | 22 | SPANS_ZERO |
| Total CRPS | ALL | 396 | 5.1796 | 5.1183 | 0.0613 | -0.0593 | 0.1818 | 66 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 132 | 0.2628 | 0.2518 | 0.0110 | -0.0078 | 0.0298 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 132 | 0.2589 | 0.2542 | 0.0047 | -0.0094 | 0.0188 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 132 | 0.2611 | 0.2582 | 0.0029 | -0.0164 | 0.0222 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 396 | 0.2609 | 0.2547 | 0.0062 | -0.0034 | 0.0158 | 66 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 132 | 0.1080 | 0.1458 | -0.0378 | -0.0647 | -0.0108 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 132 | 0.1285 | 0.1416 | -0.0131 | -0.0457 | 0.0194 | 22 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 132 | 0.1320 | 0.1922 | -0.0602 | -0.0935 | -0.0269 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 396 | 0.1228 | 0.1599 | -0.0370 | -0.0546 | -0.0194 | 66 | BELOW_ZERO |
| Home-win log loss | 2023 | 132 | 0.3398 | 0.4423 | -0.1024 | -0.1629 | -0.0420 | 22 | BELOW_ZERO |
| Home-win log loss | 2024 | 132 | 0.3812 | 0.4376 | -0.0564 | -0.1323 | 0.0194 | 22 | SPANS_ZERO |
| Home-win log loss | 2025 | 132 | 0.3949 | 0.5572 | -0.1623 | -0.2456 | -0.0790 | 22 | BELOW_ZERO |
| Home-win log loss | ALL | 396 | 0.3720 | 0.4790 | -0.1071 | -0.1488 | -0.0654 | 66 | BELOW_ZERO |
| Margin CRPS | 2023 | 132 | 4.8230 | 6.1395 | -1.3165 | -1.9446 | -0.6884 | 22 | BELOW_ZERO |
| Margin CRPS | 2024 | 132 | 4.5547 | 5.6823 | -1.1276 | -1.8401 | -0.4151 | 22 | BELOW_ZERO |
| Margin CRPS | 2025 | 132 | 5.2208 | 6.9874 | -1.7666 | -2.2831 | -1.2501 | 22 | BELOW_ZERO |
| Margin CRPS | ALL | 396 | 4.8662 | 6.2698 | -1.4036 | -1.7507 | -1.0564 | 66 | BELOW_ZERO |
| Total CRPS | 2023 | 132 | 5.4354 | 5.2826 | 0.1528 | -0.1715 | 0.4771 | 22 | SPANS_ZERO |
| Total CRPS | 2024 | 132 | 5.2447 | 4.8462 | 0.3985 | 0.0724 | 0.7246 | 22 | ABOVE_ZERO |
| Total CRPS | 2025 | 132 | 4.8586 | 4.5949 | 0.2636 | 0.0114 | 0.5159 | 22 | ABOVE_ZERO |
| Total CRPS | ALL | 396 | 5.1796 | 4.9079 | 0.2716 | 0.1045 | 0.4388 | 66 | ABOVE_ZERO |
| Over the league-median line, Brier | 2023 | 132 | 0.2628 | 0.2587 | 0.0041 | -0.0223 | 0.0306 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 132 | 0.2589 | 0.2351 | 0.0238 | -0.0031 | 0.0507 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 132 | 0.2611 | 0.2388 | 0.0223 | 0.0050 | 0.0397 | 22 | ABOVE_ZERO |
| Over the league-median line, Brier | ALL | 396 | 0.2609 | 0.2442 | 0.0168 | 0.0035 | 0.0300 | 66 | ABOVE_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0113; ECE 0.0682; logistic slope 1.284 (SE 0.149), intercept -0.079 (SE 0.166). Brier decomposition: reliability 0.0078, resolution 0.0694, uncertainty 0.1849.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 6 | 0.1445 | 0.0000 | 0.0000 | 0.3903 |
| [0.2, 0.3) | 19 | 0.2497 | 0.1053 | 0.0294 | 0.3139 |
| [0.3, 0.4) | 15 | 0.3621 | 0.6667 | 0.4171 | 0.8482 |
| [0.4, 0.5) | 31 | 0.4485 | 0.5161 | 0.3484 | 0.6803 |
| [0.5, 0.6) | 43 | 0.5511 | 0.4884 | 0.3462 | 0.6325 |
| [0.6, 0.7) | 23 | 0.6553 | 0.5652 | 0.3681 | 0.7437 |
| [0.7, 0.8) | 61 | 0.7521 | 0.7049 | 0.5811 | 0.8045 |
| [0.8, 0.9) | 51 | 0.8545 | 0.9412 | 0.8408 | 0.9798 |
| [0.9, 1.0] | 147 | 0.9615 | 0.9932 | 0.9625 | 0.9988 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 1460.0000 | 8.0000 | 1.0000 | 9.7872 | 264.0000 |
| 2920.0000 | 8.0000 | 1.0000 | 9.7877 | 264.0000 |
| 730.0000 | 2.0000 | 1.0000 | 9.7887 | 264.0000 |
| 1460.0000 | 2.0000 | 1.0000 | 9.7905 | 264.0000 |
| 1460.0000 | 8.0000 | 0.9000 | 9.7908 | 264.0000 |
| 2920.0000 | 8.0000 | 0.9000 | 9.7918 | 264.0000 |
| 730.0000 | 2.0000 | 0.9000 | 9.7927 | 264.0000 |
| 730.0000 | 1.0000 | 1.0000 | 9.7936 | 264.0000 |
| 2920.0000 | 2.0000 | 1.0000 | 9.7946 | 264.0000 |
| 1460.0000 | 2.0000 | 0.9000 | 9.7950 | 264.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:01:30Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-AUSTRIA-BASKETBALL-BUNDESLIGA-JOINT-r1
- `archive_snapshot_sha256`: d3f929d227064f3bba145eb30be882958de56ac76945c19d90ebb6ba44040268
- `seconds`: 140

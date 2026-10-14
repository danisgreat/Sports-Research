# Development results: `AUSST-WAFL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2019, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 90 | 0.1852 | 0.2564 | -0.0751 | -0.0975 | -0.0527 | 20 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 90 | 0.1900 | 0.2305 | -0.0411 | -0.0896 | 0.0073 | 21 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 96 | 0.1916 | 0.2532 | -0.0576 | -0.0907 | -0.0245 | 24 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 276 | 0.1890 | 0.2468 | -0.0576 | -0.0778 | -0.0375 | 65 | BELOW_ZERO |
| Home-win log loss | 2023 | 90 | 0.5380 | 0.7062 | -0.1782 | -0.2359 | -0.1206 | 20 | BELOW_ZERO |
| Home-win log loss | 2024 | 90 | 0.5715 | 0.6538 | -0.0858 | -0.2075 | 0.0359 | 21 | SPANS_ZERO |
| Home-win log loss | 2025 | 96 | 0.5671 | 0.6996 | -0.1249 | -0.1985 | -0.0514 | 24 | BELOW_ZERO |
| Home-win log loss | ALL | 276 | 0.5591 | 0.6868 | -0.1287 | -0.1777 | -0.0797 | 65 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 90 | 0.1866 | 0.2617 | -0.0785 | -0.0993 | -0.0576 | 20 | BELOW_ZERO |
| Three-way half-sum Brier | 2024 | 90 | 0.1936 | 0.2342 | -0.0414 | -0.0898 | 0.0070 | 21 | SPANS_ZERO |
| Three-way half-sum Brier | 2025 | 96 | 0.1958 | 0.2579 | -0.0579 | -0.0910 | -0.0249 | 24 | BELOW_ZERO |
| Three-way half-sum Brier | ALL | 276 | 0.1921 | 0.2514 | -0.0589 | -0.0789 | -0.0389 | 65 | BELOW_ZERO |
| Margin CRPS | 2023 | 90 | 20.5791 | 29.0639 | -9.0517 | -12.8033 | -5.3002 | 20 | BELOW_ZERO |
| Margin CRPS | 2024 | 90 | 17.2022 | 21.1967 | -4.0789 | -7.0336 | -1.1243 | 21 | BELOW_ZERO |
| Margin CRPS | 2025 | 96 | 19.0747 | 23.3016 | -3.8508 | -5.7289 | -1.9728 | 24 | BELOW_ZERO |
| Margin CRPS | ALL | 276 | 18.9547 | 24.4943 | -5.5248 | -7.1865 | -3.8631 | 65 | BELOW_ZERO |
| Total CRPS | 2023 | 90 | 18.0724 | 20.9523 | -3.1269 | -5.4209 | -0.8329 | 20 | BELOW_ZERO |
| Total CRPS | 2024 | 90 | 17.6056 | 18.4225 | -0.9043 | -3.1594 | 1.3507 | 21 | SPANS_ZERO |
| Total CRPS | 2025 | 96 | 16.4608 | 16.9713 | -0.9798 | -2.7132 | 0.7536 | 24 | SPANS_ZERO |
| Total CRPS | ALL | 276 | 17.3596 | 18.7427 | -1.6161 | -2.7754 | -0.4568 | 65 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 90 | 0.2012 | 0.2365 | -0.0426 | -0.0701 | -0.0151 | 20 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 90 | 0.2462 | 0.2492 | -0.0013 | -0.0464 | 0.0439 | 21 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 96 | 0.2473 | 0.2489 | -0.0062 | -0.0383 | 0.0258 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 276 | 0.2319 | 0.2449 | -0.0158 | -0.0358 | 0.0042 | 65 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 90 | 0.1852 | 0.2046 | -0.0229 | -0.0431 | -0.0027 | 20 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 90 | 0.1900 | 0.2063 | -0.0177 | -0.0453 | 0.0099 | 21 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 96 | 0.1916 | 0.2209 | -0.0212 | -0.0444 | 0.0020 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 276 | 0.1890 | 0.2108 | -0.0206 | -0.0337 | -0.0075 | 65 | BELOW_ZERO |
| Home-win log loss | 2023 | 90 | 0.5380 | 0.5892 | -0.0587 | -0.1016 | -0.0158 | 20 | BELOW_ZERO |
| Home-win log loss | 2024 | 90 | 0.5715 | 0.6022 | -0.0358 | -0.1149 | 0.0433 | 21 | SPANS_ZERO |
| Home-win log loss | 2025 | 96 | 0.5671 | 0.6315 | -0.0471 | -0.0971 | 0.0029 | 24 | SPANS_ZERO |
| Home-win log loss | ALL | 276 | 0.5591 | 0.6082 | -0.0470 | -0.0794 | -0.0147 | 65 | BELOW_ZERO |
| Margin CRPS | 2023 | 90 | 20.5791 | 23.2957 | -2.9330 | -4.7149 | -1.1510 | 20 | BELOW_ZERO |
| Margin CRPS | 2024 | 90 | 17.2022 | 19.1331 | -2.0249 | -4.0341 | -0.0158 | 21 | BELOW_ZERO |
| Margin CRPS | 2025 | 96 | 19.0747 | 20.9223 | -1.5604 | -2.5828 | -0.5380 | 24 | BELOW_ZERO |
| Margin CRPS | ALL | 276 | 18.9547 | 21.1128 | -2.1328 | -3.0202 | -1.2454 | 65 | BELOW_ZERO |
| Total CRPS | 2023 | 90 | 18.0724 | 17.9577 | 0.0035 | -0.9944 | 1.0014 | 20 | SPANS_ZERO |
| Total CRPS | 2024 | 90 | 17.6056 | 18.3935 | -0.8382 | -2.1941 | 0.5177 | 21 | SPANS_ZERO |
| Total CRPS | 2025 | 96 | 16.4608 | 16.9945 | -0.6240 | -1.7778 | 0.5298 | 24 | SPANS_ZERO |
| Total CRPS | ALL | 276 | 17.3596 | 17.7648 | -0.5001 | -1.1523 | 0.1521 | 65 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 90 | 0.2012 | 0.1910 | 0.0068 | -0.0110 | 0.0245 | 20 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 90 | 0.2462 | 0.2529 | -0.0044 | -0.0345 | 0.0256 | 21 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 96 | 0.2473 | 0.2526 | -0.0048 | -0.0267 | 0.0171 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 276 | 0.2319 | 0.2326 | -0.0011 | -0.0142 | 0.0120 | 65 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0113; ECE 0.0489; logistic slope 1.133 (SE 0.172), intercept -0.090 (SE 0.144). Brier decomposition: reliability 0.0037, resolution 0.0595, uncertainty 0.2462.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 6 | 0.0484 | 0.1667 | 0.0301 | 0.5635 |
| [0.1, 0.2) | 8 | 0.1387 | 0.1250 | 0.0224 | 0.4709 |
| [0.2, 0.3) | 18 | 0.2576 | 0.1667 | 0.0584 | 0.3922 |
| [0.3, 0.4) | 29 | 0.3565 | 0.2414 | 0.1222 | 0.4211 |
| [0.4, 0.5) | 41 | 0.4560 | 0.4390 | 0.2989 | 0.5896 |
| [0.5, 0.6) | 43 | 0.5497 | 0.5814 | 0.4333 | 0.7162 |
| [0.6, 0.7) | 47 | 0.6438 | 0.5957 | 0.4534 | 0.7236 |
| [0.7, 0.8) | 40 | 0.7492 | 0.8250 | 0.6805 | 0.9125 |
| [0.8, 0.9) | 27 | 0.8489 | 0.8519 | 0.6752 | 0.9408 |
| [0.9, 1.0] | 17 | 0.9569 | 0.9412 | 0.7302 | 0.9895 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 2.0000 | 1.4000 | 35.9994 | 180.0000 |
| 90.0000 | 2.0000 | 1.3000 | 36.0086 | 180.0000 |
| 90.0000 | 2.0000 | 1.5000 | 36.0110 | 180.0000 |
| 180.0000 | 2.0000 | 1.2000 | 36.0251 | 180.0000 |
| 180.0000 | 2.0000 | 1.1000 | 36.0393 | 180.0000 |
| 180.0000 | 2.0000 | 1.3000 | 36.0403 | 180.0000 |
| 90.0000 | 2.0000 | 1.2000 | 36.0423 | 180.0000 |
| 180.0000 | 2.0000 | 1.4000 | 36.0797 | 180.0000 |
| 180.0000 | 2.0000 | 1.0000 | 36.0889 | 180.0000 |
| 90.0000 | 2.0000 | 1.1000 | 36.1052 | 180.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:05:35Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-WAFL-JOINT-r1
- `archive_snapshot_sha256`: 768780bcda5aba1a81538e455a4fe41cb9611a13de7fe0a3ddf3b0ee2d3987bf
- `seconds`: 81

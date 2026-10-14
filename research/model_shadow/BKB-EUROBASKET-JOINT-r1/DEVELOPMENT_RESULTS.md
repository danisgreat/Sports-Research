# Development results: `BKB-EUROBASKET-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2017, 2022, 2025]; hyperparameters chosen on [2013, 2015] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2017 | 76 | 0.2141 | 0.2513 | -0.0332 | -0.0652 | -0.0012 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win Brier (primary) | 2022 | 76 | 0.2709 | 0.2741 | 0.0067 | -0.0579 | 0.0712 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win Brier (primary) | ALL | 152 | 0.2425 | 0.2627 | -0.0132 | -0.0432 | 0.0167 | 6 | INSUFFICIENT_EVIDENCE |
| Home-win log loss | 2017 | 76 | 0.6193 | 0.6957 | -0.0684 | -0.1336 | -0.0032 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win log loss | 2022 | 76 | 0.7436 | 0.7477 | 0.0232 | -0.1523 | 0.1987 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win log loss | ALL | 152 | 0.6814 | 0.7217 | -0.0226 | -0.0953 | 0.0500 | 6 | INSUFFICIENT_EVIDENCE |
| Margin CRPS | 2017 | 76 | 9.0384 | 9.9955 | -0.7805 | -1.8546 | 0.2937 | 3 | INSUFFICIENT_EVIDENCE |
| Margin CRPS | 2022 | 76 | 81.2334 | 80.0651 | 2.5561 | -6.9690 | 12.0811 | 3 | INSUFFICIENT_EVIDENCE |
| Margin CRPS | ALL | 152 | 45.1359 | 45.0303 | 0.8878 | -2.3118 | 4.0874 | 6 | INSUFFICIENT_EVIDENCE |
| Total CRPS | 2017 | 76 | 11.0195 | 10.9654 | 0.0612 | -0.0513 | 0.1736 | 3 | INSUFFICIENT_EVIDENCE |
| Total CRPS | 2022 | 76 | 83.4853 | 81.5473 | 1.5424 | -2.9913 | 6.0760 | 3 | INSUFFICIENT_EVIDENCE |
| Total CRPS | ALL | 152 | 47.2524 | 46.2563 | 0.8018 | -0.6791 | 2.2827 | 6 | INSUFFICIENT_EVIDENCE |
| Over the league-median line, Brier | 2017 | 76 | 0.2393 | 0.2402 | -0.0011 | -0.0115 | 0.0092 | 3 | INSUFFICIENT_EVIDENCE |
| Over the league-median line, Brier | 2022 | 76 | 0.2231 | 0.2198 | 0.0006 | -0.0160 | 0.0172 | 3 | INSUFFICIENT_EVIDENCE |
| Over the league-median line, Brier | ALL | 152 | 0.2312 | 0.2300 | -0.0003 | -0.0056 | 0.0050 | 6 | INSUFFICIENT_EVIDENCE |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2017 | 76 | 0.2141 | 0.2207 | -0.0003 | -0.0680 | 0.0673 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win Brier (primary) | 2022 | 76 | 0.2709 | 0.2908 | -0.0779 | -0.4344 | 0.2785 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win Brier (primary) | ALL | 152 | 0.2425 | 0.2558 | -0.0391 | -0.1458 | 0.0676 | 6 | INSUFFICIENT_EVIDENCE |
| Home-win log loss | 2017 | 76 | 0.6193 | 0.6325 | -0.0001 | -0.1396 | 0.1394 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win log loss | 2022 | 76 | 0.7436 | 1.6148 | -1.4979 | -5.9266 | 2.9308 | 3 | INSUFFICIENT_EVIDENCE |
| Home-win log loss | ALL | 152 | 0.6814 | 1.1236 | -0.7490 | -2.2128 | 0.7148 | 6 | INSUFFICIENT_EVIDENCE |
| Margin CRPS | 2017 | 76 | 9.0384 | 9.3845 | -0.1673 | -2.4461 | 2.1116 | 3 | INSUFFICIENT_EVIDENCE |
| Margin CRPS | 2022 | 76 | 81.2334 | 76.3868 | 2.9534 | -12.8241 | 18.7309 | 3 | INSUFFICIENT_EVIDENCE |
| Margin CRPS | ALL | 152 | 45.1359 | 42.8856 | 1.3931 | -3.2285 | 6.0146 | 6 | INSUFFICIENT_EVIDENCE |
| Total CRPS | 2017 | 76 | 11.0195 | 10.3149 | 1.1130 | -1.5650 | 3.7911 | 3 | INSUFFICIENT_EVIDENCE |
| Total CRPS | 2022 | 76 | 83.4853 | 98.0670 | -12.8112 | -45.9959 | 20.3734 | 3 | INSUFFICIENT_EVIDENCE |
| Total CRPS | ALL | 152 | 47.2524 | 54.1909 | -5.8491 | -17.8150 | 6.1168 | 6 | INSUFFICIENT_EVIDENCE |
| Over the league-median line, Brier | 2017 | 76 | 0.2393 | 0.2174 | 0.0240 | 0.0063 | 0.0416 | 3 | INSUFFICIENT_EVIDENCE |
| Over the league-median line, Brier | 2022 | 76 | 0.2231 | 0.2673 | -0.0455 | -0.1535 | 0.0625 | 3 | INSUFFICIENT_EVIDENCE |
| Over the league-median line, Brier | ALL | 152 | 0.2312 | 0.2424 | -0.0108 | -0.0603 | 0.0387 | 6 | INSUFFICIENT_EVIDENCE |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0289; ECE 0.1217; logistic slope 0.622 (SE 0.305), intercept 0.013 (SE 0.190). Brier decomposition: reliability 0.0230, resolution 0.0285, uncertainty 0.2479.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 2 | 0.1828 | 1.0000 | 0.3424 | 1.0000 |
| [0.2, 0.3) | 37 | 0.2518 | 0.3784 | 0.2406 | 0.5390 |
| [0.3, 0.4) | 21 | 0.3619 | 0.3333 | 0.1719 | 0.5463 |
| [0.4, 0.5) | 46 | 0.4664 | 0.3261 | 0.2087 | 0.4703 |
| [0.5, 0.6) | 37 | 0.5398 | 0.6486 | 0.4876 | 0.7817 |
| [0.6, 0.7) | 7 | 0.6385 | 0.7143 | 0.3589 | 0.9178 |
| [0.7, 0.8) | 2 | 0.7140 | 1.0000 | 0.3424 | 1.0000 |
| [0.8, 0.9) | 0 | — | — | — | — |
| [0.9, 1.0] | 0 | — | — | — | — |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 5840.0000 | 32.0000 | 1.1000 | 17.1941 | 169.0000 |
| 2920.0000 | 32.0000 | 1.1000 | 17.1971 | 169.0000 |
| 5840.0000 | 32.0000 | 1.0000 | 17.2008 | 169.0000 |
| 2920.0000 | 32.0000 | 1.0000 | 17.2017 | 169.0000 |
| 5840.0000 | 32.0000 | 1.2000 | 17.2038 | 169.0000 |
| 2920.0000 | 32.0000 | 1.2000 | 17.2088 | 169.0000 |
| 1460.0000 | 32.0000 | 1.1000 | 17.2096 | 169.0000 |
| 1460.0000 | 32.0000 | 1.0000 | 17.2107 | 169.0000 |
| 1460.0000 | 32.0000 | 1.2000 | 17.2246 | 169.0000 |
| 2920.0000 | 32.0000 | 0.9000 | 17.2263 | 169.0000 |


## Receipt

- `run_utc`: 2026-10-14T08:59:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-EUROBASKET-JOINT-r1
- `archive_snapshot_sha256`: 0b2f088de6f8ae1884ccfbf3e5c7ad89715e4063e9d114c7cd473c79b9fd38f9
- `seconds`: 31

# Development results: `BKB-GREEK-BASKET-LEAGUE-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `PASS_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `BELOW_ZERO_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 132 | 0.1441 | 0.2353 | -0.0912 | -0.1215 | -0.0609 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 132 | 0.1612 | 0.2389 | -0.0776 | -0.1046 | -0.0506 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 156 | 0.1757 | 0.2430 | -0.0673 | -0.0965 | -0.0381 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 420 | 0.1612 | 0.2393 | -0.0781 | -0.0941 | -0.0620 | 70 | BELOW_ZERO |
| Home-win log loss | 2023 | 132 | 0.4392 | 0.6635 | -0.2244 | -0.2957 | -0.1531 | 22 | BELOW_ZERO |
| Home-win log loss | 2024 | 132 | 0.4861 | 0.6707 | -0.1846 | -0.2544 | -0.1148 | 22 | BELOW_ZERO |
| Home-win log loss | 2025 | 156 | 0.5271 | 0.6792 | -0.1521 | -0.2263 | -0.0778 | 26 | BELOW_ZERO |
| Home-win log loss | ALL | 420 | 0.4866 | 0.6716 | -0.1850 | -0.2253 | -0.1447 | 70 | BELOW_ZERO |
| Margin CRPS | 2023 | 132 | 7.0616 | 9.7500 | -2.6884 | -3.6009 | -1.7759 | 22 | BELOW_ZERO |
| Margin CRPS | 2024 | 132 | 6.2929 | 8.4299 | -2.1371 | -3.1418 | -1.1323 | 22 | BELOW_ZERO |
| Margin CRPS | 2025 | 156 | 7.0326 | 8.7657 | -1.7331 | -2.5278 | -0.9385 | 26 | BELOW_ZERO |
| Margin CRPS | ALL | 420 | 6.8092 | 8.9695 | -2.1603 | -2.6612 | -1.6594 | 70 | BELOW_ZERO |
| Total CRPS | 2023 | 132 | 10.3133 | 10.9421 | -0.6288 | -1.2911 | 0.0335 | 22 | SPANS_ZERO |
| Total CRPS | 2024 | 132 | 9.0821 | 9.2790 | -0.1969 | -0.8107 | 0.4169 | 22 | SPANS_ZERO |
| Total CRPS | 2025 | 156 | 10.2881 | 10.9761 | -0.6880 | -1.6425 | 0.2664 | 26 | SPANS_ZERO |
| Total CRPS | ALL | 420 | 9.9170 | 10.4321 | -0.5151 | -0.9504 | -0.0798 | 70 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 132 | 0.2342 | 0.2497 | -0.0156 | -0.0417 | 0.0106 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 132 | 0.2276 | 0.2509 | -0.0233 | -0.0444 | -0.0022 | 22 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 156 | 0.2412 | 0.2500 | -0.0088 | -0.0389 | 0.0213 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 420 | 0.2347 | 0.2502 | -0.0155 | -0.0302 | -0.0008 | 70 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 132 | 0.1441 | 0.1949 | -0.0509 | -0.0766 | -0.0252 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 132 | 0.1612 | 0.2036 | -0.0424 | -0.0664 | -0.0183 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 156 | 0.1757 | 0.2085 | -0.0328 | -0.0548 | -0.0109 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 420 | 0.1612 | 0.2027 | -0.0415 | -0.0547 | -0.0284 | 70 | BELOW_ZERO |
| Home-win log loss | 2023 | 132 | 0.4392 | 0.5730 | -0.1338 | -0.1890 | -0.0786 | 22 | BELOW_ZERO |
| Home-win log loss | 2024 | 132 | 0.4861 | 0.5948 | -0.1086 | -0.1683 | -0.0490 | 22 | BELOW_ZERO |
| Home-win log loss | 2025 | 156 | 0.5271 | 0.6038 | -0.0767 | -0.1298 | -0.0237 | 26 | BELOW_ZERO |
| Home-win log loss | ALL | 420 | 0.4866 | 0.5913 | -0.1047 | -0.1358 | -0.0736 | 70 | BELOW_ZERO |
| Margin CRPS | 2023 | 132 | 7.0616 | 8.5025 | -1.4409 | -2.4063 | -0.4755 | 22 | BELOW_ZERO |
| Margin CRPS | 2024 | 132 | 6.2929 | 7.4454 | -1.1526 | -1.8557 | -0.4494 | 22 | BELOW_ZERO |
| Margin CRPS | 2025 | 156 | 7.0326 | 7.8989 | -0.8663 | -1.4964 | -0.2361 | 26 | BELOW_ZERO |
| Margin CRPS | ALL | 420 | 6.8092 | 7.9461 | -1.1369 | -1.5599 | -0.7138 | 70 | BELOW_ZERO |
| Total CRPS | 2023 | 132 | 10.3133 | 11.0927 | -0.7794 | -1.9080 | 0.3492 | 22 | SPANS_ZERO |
| Total CRPS | 2024 | 132 | 9.0821 | 9.3965 | -0.3144 | -0.9621 | 0.3333 | 22 | SPANS_ZERO |
| Total CRPS | 2025 | 156 | 10.2881 | 10.2344 | 0.0537 | -0.4163 | 0.5236 | 26 | SPANS_ZERO |
| Total CRPS | ALL | 420 | 9.9170 | 10.2408 | -0.3238 | -0.7525 | 0.1048 | 70 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 132 | 0.2342 | 0.2542 | -0.0200 | -0.0733 | 0.0333 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 132 | 0.2276 | 0.2382 | -0.0105 | -0.0312 | 0.0101 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 156 | 0.2412 | 0.2364 | 0.0048 | -0.0094 | 0.0189 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 420 | 0.2347 | 0.2425 | -0.0078 | -0.0257 | 0.0100 | 70 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0012; ECE 0.0623; logistic slope 1.302 (SE 0.145), intercept -0.110 (SE 0.131). Brier decomposition: reliability 0.0063, resolution 0.0824, uncertainty 0.2385.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 11 | 0.0711 | 0.0000 | 0.0000 | 0.2588 |
| [0.1, 0.2) | 26 | 0.1393 | 0.0385 | 0.0068 | 0.1889 |
| [0.2, 0.3) | 21 | 0.2379 | 0.0476 | 0.0085 | 0.2267 |
| [0.3, 0.4) | 25 | 0.3656 | 0.2400 | 0.1150 | 0.4343 |
| [0.4, 0.5) | 39 | 0.4529 | 0.4872 | 0.3386 | 0.6380 |
| [0.5, 0.6) | 60 | 0.5510 | 0.6667 | 0.5406 | 0.7727 |
| [0.6, 0.7) | 72 | 0.6459 | 0.6528 | 0.5376 | 0.7525 |
| [0.7, 0.8) | 69 | 0.7468 | 0.7826 | 0.6718 | 0.8636 |
| [0.8, 0.9) | 40 | 0.8445 | 0.7750 | 0.6250 | 0.8768 |
| [0.9, 1.0] | 57 | 0.9546 | 0.9825 | 0.9071 | 0.9969 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 2.0000 | 1.1000 | 15.7199 | 286.0000 |
| 180.0000 | 1.0000 | 1.1000 | 15.7202 | 286.0000 |
| 180.0000 | 1.0000 | 1.2000 | 15.7264 | 286.0000 |
| 180.0000 | 2.0000 | 1.2000 | 15.7275 | 286.0000 |
| 180.0000 | 2.0000 | 1.0000 | 15.7288 | 286.0000 |
| 180.0000 | 1.0000 | 1.0000 | 15.7308 | 286.0000 |
| 180.0000 | 1.0000 | 1.3000 | 15.7463 | 286.0000 |
| 180.0000 | 2.0000 | 1.3000 | 15.7488 | 286.0000 |
| 90.0000 | 2.0000 | 1.2000 | 15.7797 | 286.0000 |
| 90.0000 | 2.0000 | 1.1000 | 15.7836 | 286.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:02:03Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-GREEK-BASKET-LEAGUE-JOINT-r1
- `archive_snapshot_sha256`: 3b339b1e6cfddb4dcd387071bcb2c5b5b786c9d8221dd03b6191f926a00174f8
- `seconds`: 90

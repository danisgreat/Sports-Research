# Development results: `AUSST-VFLW-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 84 | 0.2338 | 0.2512 | -0.0174 | -0.0488 | 0.0141 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 84 | 0.2419 | 0.2514 | -0.0095 | -0.0520 | 0.0329 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 84 | 0.2128 | 0.2499 | -0.0371 | -0.0749 | 0.0007 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 252 | 0.2295 | 0.2508 | -0.0213 | -0.0414 | -0.0013 | 42 | BELOW_ZERO |
| Home-win log loss | 2023 | 84 | 0.6540 | 0.6955 | -0.0416 | -0.1137 | 0.0306 | 14 | SPANS_ZERO |
| Home-win log loss | 2024 | 84 | 0.6929 | 0.6960 | -0.0031 | -0.1182 | 0.1120 | 14 | SPANS_ZERO |
| Home-win log loss | 2025 | 84 | 0.6160 | 0.6929 | -0.0769 | -0.1709 | 0.0171 | 14 | SPANS_ZERO |
| Home-win log loss | ALL | 252 | 0.6543 | 0.6948 | -0.0405 | -0.0916 | 0.0106 | 42 | SPANS_ZERO |
| Three-way half-sum Brier | 2023 | 84 | 0.2450 | 0.2631 | -0.0181 | -0.0500 | 0.0137 | 14 | SPANS_ZERO |
| Three-way half-sum Brier | 2024 | 84 | 0.2675 | 0.2689 | -0.0014 | -0.0457 | 0.0430 | 14 | SPANS_ZERO |
| Three-way half-sum Brier | 2025 | 84 | 0.2200 | 0.2553 | -0.0353 | -0.0726 | 0.0021 | 14 | SPANS_ZERO |
| Three-way half-sum Brier | ALL | 252 | 0.2442 | 0.2624 | -0.0183 | -0.0388 | 0.0023 | 42 | SPANS_ZERO |
| Margin CRPS | 2023 | 84 | 13.8805 | 15.6496 | -1.7691 | -3.3647 | -0.1734 | 14 | BELOW_ZERO |
| Margin CRPS | 2024 | 84 | 19.2702 | 20.6736 | -1.4034 | -4.3480 | 1.5412 | 14 | SPANS_ZERO |
| Margin CRPS | 2025 | 84 | 16.6458 | 19.5830 | -2.9372 | -5.6181 | -0.2563 | 14 | BELOW_ZERO |
| Margin CRPS | ALL | 252 | 16.5988 | 18.6354 | -2.0366 | -3.3565 | -0.7166 | 42 | BELOW_ZERO |
| Total CRPS | 2023 | 84 | 10.5278 | 11.3828 | -0.8550 | -1.7488 | 0.0388 | 14 | SPANS_ZERO |
| Total CRPS | 2024 | 84 | 12.8161 | 13.8962 | -1.0800 | -2.4590 | 0.2990 | 14 | SPANS_ZERO |
| Total CRPS | 2025 | 84 | 10.8663 | 11.4800 | -0.6137 | -1.8681 | 0.6407 | 14 | SPANS_ZERO |
| Total CRPS | ALL | 252 | 11.4034 | 12.2530 | -0.8496 | -1.4807 | -0.2184 | 42 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 84 | 0.2416 | 0.2664 | -0.0248 | -0.0630 | 0.0134 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 84 | 0.2235 | 0.2479 | -0.0244 | -0.0614 | 0.0127 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 84 | 0.2370 | 0.2478 | -0.0108 | -0.0581 | 0.0365 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 252 | 0.2341 | 0.2540 | -0.0200 | -0.0417 | 0.0018 | 42 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 84 | 0.2338 | 0.2371 | -0.0033 | -0.0263 | 0.0197 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 84 | 0.2419 | 0.2438 | -0.0019 | -0.0440 | 0.0402 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 84 | 0.2128 | 0.2254 | -0.0127 | -0.0415 | 0.0162 | 14 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 252 | 0.2295 | 0.2355 | -0.0060 | -0.0230 | 0.0111 | 42 | SPANS_ZERO |
| Home-win log loss | 2023 | 84 | 0.6540 | 0.6653 | -0.0114 | -0.0650 | 0.0423 | 14 | SPANS_ZERO |
| Home-win log loss | 2024 | 84 | 0.6929 | 0.6853 | 0.0076 | -0.0943 | 0.1094 | 14 | SPANS_ZERO |
| Home-win log loss | 2025 | 84 | 0.6160 | 0.6419 | -0.0259 | -0.1009 | 0.0490 | 14 | SPANS_ZERO |
| Home-win log loss | ALL | 252 | 0.6543 | 0.6642 | -0.0099 | -0.0519 | 0.0321 | 42 | SPANS_ZERO |
| Margin CRPS | 2023 | 84 | 13.8805 | 14.4136 | -0.5331 | -1.6890 | 0.6228 | 14 | SPANS_ZERO |
| Margin CRPS | 2024 | 84 | 19.2702 | 19.6074 | -0.3372 | -2.4167 | 1.7423 | 14 | SPANS_ZERO |
| Margin CRPS | 2025 | 84 | 16.6458 | 17.8247 | -1.1789 | -2.9228 | 0.5650 | 14 | SPANS_ZERO |
| Margin CRPS | ALL | 252 | 16.5988 | 17.2819 | -0.6831 | -1.5867 | 0.2206 | 42 | SPANS_ZERO |
| Total CRPS | 2023 | 84 | 10.5278 | 10.1933 | 0.3345 | -0.3314 | 1.0004 | 14 | SPANS_ZERO |
| Total CRPS | 2024 | 84 | 12.8161 | 13.1394 | -0.3232 | -0.8118 | 0.1654 | 14 | SPANS_ZERO |
| Total CRPS | 2025 | 84 | 10.8663 | 11.2587 | -0.3924 | -1.1131 | 0.3283 | 14 | SPANS_ZERO |
| Total CRPS | ALL | 252 | 11.4034 | 11.5304 | -0.1270 | -0.4758 | 0.2218 | 42 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 84 | 0.2416 | 0.2288 | 0.0128 | -0.0046 | 0.0302 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 84 | 0.2235 | 0.2396 | -0.0161 | -0.0304 | -0.0017 | 14 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 84 | 0.2370 | 0.2358 | 0.0012 | -0.0288 | 0.0313 | 14 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 252 | 0.2341 | 0.2347 | -0.0007 | -0.0127 | 0.0114 | 42 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0154; ECE 0.0513; logistic slope 0.694 (SE 0.157), intercept -0.062 (SE 0.132). Brier decomposition: reliability 0.0051, resolution 0.0240, uncertainty 0.2499.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 1 | 0.0964 | 0.0000 | 0.0000 | 0.7935 |
| [0.1, 0.2) | 16 | 0.1433 | 0.1875 | 0.0659 | 0.4301 |
| [0.2, 0.3) | 23 | 0.2512 | 0.3913 | 0.2216 | 0.5921 |
| [0.3, 0.4) | 30 | 0.3547 | 0.3667 | 0.2187 | 0.5449 |
| [0.4, 0.5) | 50 | 0.4587 | 0.3800 | 0.2586 | 0.5185 |
| [0.5, 0.6) | 57 | 0.5472 | 0.5439 | 0.4159 | 0.6663 |
| [0.6, 0.7) | 37 | 0.6421 | 0.6486 | 0.4876 | 0.7817 |
| [0.7, 0.8) | 15 | 0.7506 | 0.6667 | 0.4171 | 0.8482 |
| [0.8, 0.9) | 17 | 0.8382 | 0.7059 | 0.4687 | 0.8672 |
| [0.9, 1.0] | 6 | 0.9455 | 0.8333 | 0.4365 | 0.9699 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 2.0000 | 1.4000 | 28.0245 | 138.0000 |
| 90.0000 | 2.0000 | 1.5000 | 28.0304 | 138.0000 |
| 90.0000 | 2.0000 | 1.3000 | 28.0359 | 138.0000 |
| 90.0000 | 2.0000 | 1.2000 | 28.0676 | 138.0000 |
| 90.0000 | 1.0000 | 1.5000 | 28.1046 | 138.0000 |
| 90.0000 | 1.0000 | 1.4000 | 28.1137 | 138.0000 |
| 90.0000 | 2.0000 | 1.1000 | 28.1237 | 138.0000 |
| 90.0000 | 1.0000 | 1.3000 | 28.1407 | 138.0000 |
| 45.0000 | 2.0000 | 1.5000 | 28.1539 | 138.0000 |
| 45.0000 | 2.0000 | 1.4000 | 28.1688 | 138.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:04:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-VFLW-JOINT-r1
- `archive_snapshot_sha256`: c116f28e7e887b77556d2bc0e82fdab6f9edb7fff8fb5de323743773e614b514
- `seconds`: 44

# Development results: `AUSST-SANFL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 90 | 0.2228 | 0.2513 | -0.0303 | -0.0590 | -0.0017 | 19 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 90 | 0.2092 | 0.2463 | -0.0353 | -0.0580 | -0.0127 | 19 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 90 | 0.1804 | 0.2513 | -0.0735 | -0.1037 | -0.0433 | 20 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 270 | 0.2041 | 0.2496 | -0.0469 | -0.0626 | -0.0311 | 58 | BELOW_ZERO |
| Home-win log loss | 2023 | 90 | 0.6366 | 0.6958 | -0.0631 | -0.1234 | -0.0029 | 19 | BELOW_ZERO |
| Home-win log loss | 2024 | 90 | 0.6069 | 0.6857 | -0.0753 | -0.1231 | -0.0275 | 19 | BELOW_ZERO |
| Home-win log loss | 2025 | 90 | 0.5426 | 0.6958 | -0.1589 | -0.2248 | -0.0930 | 20 | BELOW_ZERO |
| Home-win log loss | ALL | 270 | 0.5954 | 0.6924 | -0.1001 | -0.1339 | -0.0663 | 58 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 90 | 0.2334 | 0.2618 | -0.0303 | -0.0593 | -0.0012 | 19 | BELOW_ZERO |
| Three-way half-sum Brier | 2024 | 90 | 0.2089 | 0.2452 | -0.0345 | -0.0571 | -0.0120 | 19 | BELOW_ZERO |
| Three-way half-sum Brier | 2025 | 90 | 0.1803 | 0.2516 | -0.0738 | -0.1040 | -0.0436 | 20 | BELOW_ZERO |
| Three-way half-sum Brier | ALL | 270 | 0.2076 | 0.2529 | -0.0467 | -0.0625 | -0.0309 | 58 | BELOW_ZERO |
| Margin CRPS | 2023 | 90 | 16.6145 | 18.2828 | -1.8833 | -3.2078 | -0.5588 | 19 | BELOW_ZERO |
| Margin CRPS | 2024 | 90 | 22.0579 | 24.1814 | -2.1285 | -3.8131 | -0.4438 | 19 | BELOW_ZERO |
| Margin CRPS | 2025 | 90 | 22.0938 | 27.3736 | -4.8864 | -6.9489 | -2.8238 | 20 | BELOW_ZERO |
| Margin CRPS | ALL | 270 | 20.2554 | 23.2793 | -2.9991 | -4.0050 | -1.9933 | 58 | BELOW_ZERO |
| Total CRPS | 2023 | 90 | 17.6109 | 17.6849 | 0.0969 | -0.8243 | 1.0180 | 19 | SPANS_ZERO |
| Total CRPS | 2024 | 90 | 15.7535 | 15.7450 | 0.2153 | -0.6358 | 1.0664 | 19 | SPANS_ZERO |
| Total CRPS | 2025 | 90 | 17.6908 | 19.4462 | -1.9184 | -3.4232 | -0.4136 | 20 | BELOW_ZERO |
| Total CRPS | ALL | 270 | 17.0184 | 17.6254 | -0.5592 | -1.2335 | 0.1150 | 58 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 90 | 0.2553 | 0.2623 | -0.0031 | -0.0234 | 0.0171 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 90 | 0.2320 | 0.2441 | -0.0073 | -0.0284 | 0.0138 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 90 | 0.2237 | 0.2418 | -0.0240 | -0.0542 | 0.0062 | 20 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 270 | 0.2370 | 0.2494 | -0.0117 | -0.0252 | 0.0018 | 58 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 90 | 0.2228 | 0.2186 | 0.0048 | -0.0052 | 0.0149 | 19 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 90 | 0.2092 | 0.2190 | -0.0088 | -0.0282 | 0.0107 | 19 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 90 | 0.1804 | 0.1831 | -0.0028 | -0.0237 | 0.0181 | 20 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 270 | 0.2041 | 0.2069 | -0.0023 | -0.0119 | 0.0074 | 58 | SPANS_ZERO |
| Home-win log loss | 2023 | 90 | 0.6366 | 0.6276 | 0.0105 | -0.0104 | 0.0314 | 19 | SPANS_ZERO |
| Home-win log loss | 2024 | 90 | 0.6069 | 0.6284 | -0.0194 | -0.0605 | 0.0217 | 19 | SPANS_ZERO |
| Home-win log loss | 2025 | 90 | 0.5426 | 0.5504 | -0.0078 | -0.0525 | 0.0370 | 20 | SPANS_ZERO |
| Home-win log loss | ALL | 270 | 0.5954 | 0.6021 | -0.0056 | -0.0261 | 0.0149 | 58 | SPANS_ZERO |
| Margin CRPS | 2023 | 90 | 16.6145 | 16.5387 | 0.1226 | -0.3834 | 0.6287 | 19 | SPANS_ZERO |
| Margin CRPS | 2024 | 90 | 22.0579 | 22.9423 | -0.7967 | -2.0025 | 0.4092 | 19 | SPANS_ZERO |
| Margin CRPS | 2025 | 90 | 22.0938 | 22.8398 | -0.6883 | -2.2404 | 0.8639 | 20 | SPANS_ZERO |
| Margin CRPS | ALL | 270 | 20.2554 | 20.7736 | -0.4582 | -1.1108 | 0.1945 | 58 | SPANS_ZERO |
| Total CRPS | 2023 | 90 | 17.6109 | 17.5873 | 0.0391 | -0.2583 | 0.3365 | 19 | SPANS_ZERO |
| Total CRPS | 2024 | 90 | 15.7535 | 17.0285 | -1.2202 | -2.4322 | -0.0083 | 19 | BELOW_ZERO |
| Total CRPS | 2025 | 90 | 17.6908 | 17.8675 | -0.1991 | -0.7710 | 0.3727 | 20 | SPANS_ZERO |
| Total CRPS | ALL | 270 | 17.0184 | 17.4944 | -0.4556 | -0.9044 | -0.0068 | 58 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 90 | 0.2553 | 0.2576 | -0.0016 | -0.0106 | 0.0073 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 90 | 0.2320 | 0.2385 | -0.0064 | -0.0154 | 0.0027 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 90 | 0.2237 | 0.2268 | -0.0035 | -0.0149 | 0.0078 | 20 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 270 | 0.2370 | 0.2410 | -0.0038 | -0.0092 | 0.0015 | 58 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0397; ECE 0.0881; logistic slope 1.810 (SE 0.271), intercept 0.163 (SE 0.138). Brier decomposition: reliability 0.0101, resolution 0.0524, uncertainty 0.2473.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 5 | 0.1639 | 0.0000 | -0.0000 | 0.4345 |
| [0.2, 0.3) | 17 | 0.2605 | 0.1176 | 0.0329 | 0.3434 |
| [0.3, 0.4) | 38 | 0.3566 | 0.3684 | 0.2338 | 0.5272 |
| [0.4, 0.5) | 67 | 0.4520 | 0.4030 | 0.2939 | 0.5226 |
| [0.5, 0.6) | 63 | 0.5459 | 0.6508 | 0.5275 | 0.7567 |
| [0.6, 0.7) | 52 | 0.6467 | 0.7500 | 0.6179 | 0.8477 |
| [0.7, 0.8) | 23 | 0.7431 | 0.9130 | 0.7320 | 0.9758 |
| [0.8, 0.9) | 5 | 0.8195 | 1.0000 | 0.5655 | 1.0000 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 8.0000 | 1.2000 | 35.1805 | 60.0000 |
| 45.0000 | 8.0000 | 1.1000 | 35.1861 | 60.0000 |
| 90.0000 | 8.0000 | 1.1000 | 35.1913 | 60.0000 |
| 45.0000 | 8.0000 | 1.2000 | 35.1966 | 60.0000 |
| 90.0000 | 8.0000 | 1.3000 | 35.2000 | 60.0000 |
| 45.0000 | 8.0000 | 1.0000 | 35.2114 | 60.0000 |
| 45.0000 | 8.0000 | 1.3000 | 35.2365 | 60.0000 |
| 90.0000 | 8.0000 | 1.0000 | 35.2391 | 60.0000 |
| 180.0000 | 8.0000 | 1.2000 | 35.2555 | 60.0000 |
| 180.0000 | 8.0000 | 1.3000 | 35.2608 | 60.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:04:14Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-SANFL-JOINT-r1
- `archive_snapshot_sha256`: 24bd39fff403156337cb2e0a80e6e1949cab78d4bdb4b495220b745e0dd66d40
- `seconds`: 19

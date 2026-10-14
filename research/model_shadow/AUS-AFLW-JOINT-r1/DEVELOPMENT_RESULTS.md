# Development results: `AUS-AFLW-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 79 | 0.2108 | 0.2508 | -0.0403 | -0.0989 | 0.0183 | 10 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 87 | 0.1864 | 0.2507 | -0.0600 | -0.1126 | -0.0074 | 10 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 95 | 0.1873 | 0.2504 | -0.0634 | -0.1006 | -0.0262 | 12 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 261 | 0.1941 | 0.2506 | -0.0551 | -0.0802 | -0.0300 | 32 | BELOW_ZERO |
| Home-win log loss | 2023 | 79 | 0.6121 | 0.6947 | -0.0829 | -0.2347 | 0.0689 | 10 | SPANS_ZERO |
| Home-win log loss | 2024 | 87 | 0.5499 | 0.6945 | -0.1346 | -0.2532 | -0.0160 | 10 | BELOW_ZERO |
| Home-win log loss | 2025 | 95 | 0.5487 | 0.6939 | -0.1459 | -0.2329 | -0.0589 | 12 | BELOW_ZERO |
| Home-win log loss | ALL | 261 | 0.5683 | 0.6943 | -0.1227 | -0.1835 | -0.0618 | 32 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 79 | 0.2215 | 0.2571 | -0.0359 | -0.0982 | 0.0263 | 10 | SPANS_ZERO |
| Three-way half-sum Brier | 2024 | 87 | 0.1979 | 0.2624 | -0.0603 | -0.1116 | -0.0091 | 10 | BELOW_ZERO |
| Three-way half-sum Brier | 2025 | 95 | 0.1869 | 0.2499 | -0.0634 | -0.1001 | -0.0266 | 12 | BELOW_ZERO |
| Three-way half-sum Brier | ALL | 261 | 0.2010 | 0.2563 | -0.0538 | -0.0794 | -0.0283 | 32 | BELOW_ZERO |
| Margin CRPS | 2023 | 79 | 13.2765 | 17.4469 | -4.1601 | -8.1947 | -0.1256 | 10 | BELOW_ZERO |
| Margin CRPS | 2024 | 87 | 14.5099 | 18.9057 | -4.2278 | -6.9101 | -1.5454 | 10 | BELOW_ZERO |
| Margin CRPS | 2025 | 95 | 16.2109 | 20.6306 | -4.4313 | -6.2100 | -2.6527 | 12 | BELOW_ZERO |
| Margin CRPS | ALL | 261 | 14.7557 | 19.0920 | -4.2830 | -5.7301 | -2.8358 | 32 | BELOW_ZERO |
| Total CRPS | 2023 | 79 | 12.3696 | 12.6791 | -0.2796 | -1.9077 | 1.3485 | 10 | SPANS_ZERO |
| Total CRPS | 2024 | 87 | 12.8467 | 12.1625 | 0.6016 | -0.8812 | 2.0845 | 10 | SPANS_ZERO |
| Total CRPS | 2025 | 95 | 11.7612 | 12.8922 | -1.1106 | -2.2392 | 0.0180 | 12 | SPANS_ZERO |
| Total CRPS | ALL | 261 | 12.3072 | 12.5845 | -0.3158 | -1.0710 | 0.4393 | 32 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 79 | 0.2157 | 0.2235 | -0.0070 | -0.0462 | 0.0322 | 10 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 87 | 0.2545 | 0.2415 | 0.0108 | -0.0319 | 0.0535 | 10 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 95 | 0.2137 | 0.2352 | -0.0211 | -0.0428 | 0.0006 | 12 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 261 | 0.2279 | 0.2337 | -0.0067 | -0.0248 | 0.0113 | 32 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 79 | 0.2108 | 0.2182 | -0.0081 | -0.0529 | 0.0367 | 10 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 87 | 0.1864 | 0.2035 | -0.0162 | -0.0514 | 0.0189 | 10 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 95 | 0.1873 | 0.2093 | -0.0225 | -0.0605 | 0.0156 | 12 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 261 | 0.1941 | 0.2101 | -0.0160 | -0.0362 | 0.0042 | 32 | SPANS_ZERO |
| Home-win log loss | 2023 | 79 | 0.6121 | 0.6257 | -0.0147 | -0.1326 | 0.1031 | 10 | SPANS_ZERO |
| Home-win log loss | 2024 | 87 | 0.5499 | 0.5962 | -0.0435 | -0.1222 | 0.0353 | 10 | SPANS_ZERO |
| Home-win log loss | 2025 | 95 | 0.5487 | 0.6060 | -0.0581 | -0.1458 | 0.0295 | 12 | SPANS_ZERO |
| Home-win log loss | ALL | 261 | 0.5683 | 0.6087 | -0.0400 | -0.0890 | 0.0090 | 32 | SPANS_ZERO |
| Margin CRPS | 2023 | 79 | 13.2765 | 15.4198 | -2.1607 | -5.1592 | 0.8378 | 10 | SPANS_ZERO |
| Margin CRPS | 2024 | 87 | 14.5099 | 16.3324 | -1.7755 | -3.5346 | -0.0164 | 10 | BELOW_ZERO |
| Margin CRPS | 2025 | 95 | 16.2109 | 17.9701 | -1.7724 | -3.0797 | -0.4651 | 12 | BELOW_ZERO |
| Margin CRPS | ALL | 261 | 14.7557 | 16.6523 | -1.8947 | -2.9391 | -0.8503 | 32 | BELOW_ZERO |
| Total CRPS | 2023 | 79 | 12.3696 | 11.9006 | 0.4797 | -0.6274 | 1.5869 | 10 | SPANS_ZERO |
| Total CRPS | 2024 | 87 | 12.8467 | 12.8646 | -0.0254 | -1.2166 | 1.1658 | 10 | SPANS_ZERO |
| Total CRPS | 2025 | 95 | 11.7612 | 12.0259 | -0.2647 | -0.9124 | 0.3829 | 12 | SPANS_ZERO |
| Total CRPS | ALL | 261 | 12.3072 | 12.2675 | 0.0427 | -0.4632 | 0.5486 | 32 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 79 | 0.2157 | 0.2030 | 0.0127 | -0.0191 | 0.0446 | 10 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 87 | 0.2545 | 0.2577 | -0.0026 | -0.0238 | 0.0185 | 10 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 95 | 0.2137 | 0.2172 | -0.0037 | -0.0190 | 0.0115 | 12 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 261 | 0.2279 | 0.2264 | 0.0018 | -0.0102 | 0.0137 | 32 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0006; ECE 0.0320; logistic slope 0.947 (SE 0.144), intercept 0.003 (SE 0.141). Brier decomposition: reliability 0.0015, resolution 0.0549, uncertainty 0.2500.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 16 | 0.0580 | 0.0625 | 0.0111 | 0.2833 |
| [0.1, 0.2) | 17 | 0.1553 | 0.1765 | 0.0619 | 0.4103 |
| [0.2, 0.3) | 30 | 0.2488 | 0.3333 | 0.1923 | 0.5122 |
| [0.3, 0.4) | 29 | 0.3522 | 0.3103 | 0.1728 | 0.4923 |
| [0.4, 0.5) | 41 | 0.4528 | 0.4390 | 0.2989 | 0.5896 |
| [0.5, 0.6) | 39 | 0.5474 | 0.5128 | 0.3620 | 0.6614 |
| [0.6, 0.7) | 30 | 0.6557 | 0.6667 | 0.4878 | 0.8077 |
| [0.7, 0.8) | 24 | 0.7521 | 0.7917 | 0.5953 | 0.9076 |
| [0.8, 0.9) | 21 | 0.8499 | 0.8095 | 0.6000 | 0.9233 |
| [0.9, 1.0] | 14 | 0.9369 | 0.9286 | 0.6853 | 0.9873 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 1.0000 | 1.4000 | 25.0175 | 193.0000 |
| 180.0000 | 1.0000 | 1.3000 | 25.0249 | 193.0000 |
| 180.0000 | 1.0000 | 1.5000 | 25.0258 | 193.0000 |
| 180.0000 | 1.0000 | 1.2000 | 25.0508 | 193.0000 |
| 180.0000 | 2.0000 | 1.3000 | 25.0520 | 193.0000 |
| 180.0000 | 2.0000 | 1.4000 | 25.0538 | 193.0000 |
| 180.0000 | 2.0000 | 1.2000 | 25.0687 | 193.0000 |
| 180.0000 | 2.0000 | 1.5000 | 25.0710 | 193.0000 |
| 180.0000 | 1.0000 | 1.1000 | 25.0987 | 193.0000 |
| 180.0000 | 2.0000 | 1.1000 | 25.1073 | 193.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:00:23Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUS-AFLW-JOINT-r1
- `archive_snapshot_sha256`: a43882ba9d94778710fa0eeb9e28a1ed1f6e1b5fb95d431c301ecd27d24039be
- `seconds`: 74

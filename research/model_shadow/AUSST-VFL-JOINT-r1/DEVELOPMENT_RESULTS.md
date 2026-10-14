# Development results: `AUSST-VFL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 173 | 0.1879 | 0.2490 | -0.0645 | -0.0845 | -0.0445 | 23 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 173 | 0.2079 | 0.2503 | -0.0341 | -0.0596 | -0.0086 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 172 | 0.2158 | 0.2527 | -0.0409 | -0.0608 | -0.0210 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 518 | 0.2038 | 0.2507 | -0.0468 | -0.0592 | -0.0344 | 67 | BELOW_ZERO |
| Home-win log loss | 2023 | 173 | 0.5576 | 0.6911 | -0.1413 | -0.1858 | -0.0969 | 23 | BELOW_ZERO |
| Home-win log loss | 2024 | 173 | 0.6039 | 0.6937 | -0.0708 | -0.1286 | -0.0130 | 22 | BELOW_ZERO |
| Home-win log loss | 2025 | 172 | 0.6221 | 0.6986 | -0.0845 | -0.1305 | -0.0385 | 22 | BELOW_ZERO |
| Home-win log loss | ALL | 518 | 0.5945 | 0.6945 | -0.0995 | -0.1277 | -0.0714 | 67 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 173 | 0.1941 | 0.2542 | -0.0631 | -0.0817 | -0.0445 | 23 | BELOW_ZERO |
| Three-way half-sum Brier | 2024 | 173 | 0.2184 | 0.2582 | -0.0316 | -0.0573 | -0.0060 | 22 | BELOW_ZERO |
| Three-way half-sum Brier | 2025 | 172 | 0.2270 | 0.2636 | -0.0408 | -0.0603 | -0.0213 | 22 | BELOW_ZERO |
| Three-way half-sum Brier | ALL | 518 | 0.2131 | 0.2587 | -0.0454 | -0.0576 | -0.0333 | 67 | BELOW_ZERO |
| Margin CRPS | 2023 | 173 | 22.1551 | 27.9940 | -6.0498 | -7.3723 | -4.7272 | 23 | BELOW_ZERO |
| Margin CRPS | 2024 | 173 | 17.7360 | 20.5064 | -2.3756 | -3.6866 | -1.0647 | 22 | BELOW_ZERO |
| Margin CRPS | 2025 | 172 | 19.5338 | 22.9238 | -3.4639 | -4.7587 | -2.1691 | 22 | BELOW_ZERO |
| Margin CRPS | ALL | 518 | 19.8088 | 23.8098 | -3.9942 | -4.8052 | -3.1833 | 67 | BELOW_ZERO |
| Total CRPS | 2023 | 173 | 15.3535 | 15.5567 | -0.1942 | -0.7732 | 0.3847 | 23 | SPANS_ZERO |
| Total CRPS | 2024 | 173 | 16.4668 | 16.7904 | -0.2646 | -0.8287 | 0.2995 | 22 | SPANS_ZERO |
| Total CRPS | 2025 | 172 | 16.6872 | 16.9636 | -0.1238 | -0.7090 | 0.4613 | 22 | SPANS_ZERO |
| Total CRPS | ALL | 518 | 16.1682 | 16.4359 | -0.1942 | -0.5094 | 0.1210 | 67 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 173 | 0.2456 | 0.2513 | -0.0049 | -0.0192 | 0.0095 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 173 | 0.2443 | 0.2505 | -0.0040 | -0.0204 | 0.0124 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 172 | 0.2469 | 0.2501 | 0.0027 | -0.0151 | 0.0205 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 518 | 0.2456 | 0.2507 | -0.0021 | -0.0110 | 0.0068 | 67 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 173 | 0.1879 | 0.1964 | -0.0105 | -0.0225 | 0.0016 | 23 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 173 | 0.2079 | 0.2288 | -0.0159 | -0.0337 | 0.0018 | 22 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 172 | 0.2158 | 0.2236 | -0.0111 | -0.0235 | 0.0013 | 22 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 518 | 0.2038 | 0.2163 | -0.0125 | -0.0203 | -0.0047 | 67 | BELOW_ZERO |
| Home-win log loss | 2023 | 173 | 0.5576 | 0.5802 | -0.0271 | -0.0532 | -0.0010 | 23 | BELOW_ZERO |
| Home-win log loss | 2024 | 173 | 0.6039 | 0.6490 | -0.0331 | -0.0738 | 0.0075 | 22 | SPANS_ZERO |
| Home-win log loss | 2025 | 172 | 0.6221 | 0.6383 | -0.0228 | -0.0502 | 0.0047 | 22 | SPANS_ZERO |
| Home-win log loss | ALL | 518 | 0.5945 | 0.6225 | -0.0277 | -0.0451 | -0.0102 | 67 | BELOW_ZERO |
| Margin CRPS | 2023 | 173 | 22.1551 | 23.4675 | -1.5152 | -2.4714 | -0.5590 | 23 | BELOW_ZERO |
| Margin CRPS | 2024 | 173 | 17.7360 | 19.1507 | -1.1460 | -2.1651 | -0.1269 | 22 | BELOW_ZERO |
| Margin CRPS | 2025 | 172 | 19.5338 | 20.1235 | -0.6122 | -1.3602 | 0.1358 | 22 | SPANS_ZERO |
| Margin CRPS | ALL | 518 | 19.8088 | 20.9154 | -1.0975 | -1.6066 | -0.5884 | 67 | BELOW_ZERO |
| Total CRPS | 2023 | 173 | 15.3535 | 15.8388 | -0.4681 | -0.8691 | -0.0671 | 23 | BELOW_ZERO |
| Total CRPS | 2024 | 173 | 16.4668 | 16.8569 | -0.3436 | -1.2723 | 0.5851 | 22 | SPANS_ZERO |
| Total CRPS | 2025 | 172 | 16.6872 | 16.9003 | -0.2782 | -0.7726 | 0.2161 | 22 | SPANS_ZERO |
| Total CRPS | ALL | 518 | 16.1682 | 16.5313 | -0.3649 | -0.7171 | -0.0127 | 67 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 173 | 0.2456 | 0.2533 | -0.0069 | -0.0142 | 0.0004 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 173 | 0.2443 | 0.2552 | -0.0091 | -0.0285 | 0.0104 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 172 | 0.2469 | 0.2536 | -0.0088 | -0.0188 | 0.0012 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 518 | 0.2456 | 0.2540 | -0.0082 | -0.0154 | -0.0010 | 67 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0267; ECE 0.0766; logistic slope 1.462 (SE 0.163), intercept -0.192 (SE 0.101). Brier decomposition: reliability 0.0089, resolution 0.0531, uncertainty 0.2499.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 2 | 0.0734 | 0.5000 | 0.0945 | 0.9055 |
| [0.1, 0.2) | 14 | 0.1569 | 0.0714 | 0.0127 | 0.3147 |
| [0.2, 0.3) | 29 | 0.2669 | 0.2414 | 0.1222 | 0.4211 |
| [0.3, 0.4) | 68 | 0.3588 | 0.1912 | 0.1153 | 0.3001 |
| [0.4, 0.5) | 101 | 0.4540 | 0.3465 | 0.2609 | 0.4434 |
| [0.5, 0.6) | 119 | 0.5471 | 0.5630 | 0.4733 | 0.6488 |
| [0.6, 0.7) | 85 | 0.6505 | 0.7294 | 0.6266 | 0.8124 |
| [0.7, 0.8) | 71 | 0.7402 | 0.7042 | 0.5898 | 0.7977 |
| [0.8, 0.9) | 26 | 0.8367 | 0.9615 | 0.8111 | 0.9932 |
| [0.9, 1.0] | 3 | 0.9291 | 1.0000 | 0.4385 | 1.0000 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 8.0000 | 1.1000 | 40.8453 | 232.0000 |
| 180.0000 | 8.0000 | 1.2000 | 40.8476 | 232.0000 |
| 365.0000 | 8.0000 | 1.1000 | 40.8624 | 232.0000 |
| 365.0000 | 8.0000 | 1.2000 | 40.8692 | 232.0000 |
| 180.0000 | 8.0000 | 1.3000 | 40.8840 | 232.0000 |
| 180.0000 | 8.0000 | 1.0000 | 40.8844 | 232.0000 |
| 365.0000 | 8.0000 | 1.0000 | 40.8969 | 232.0000 |
| 365.0000 | 8.0000 | 1.3000 | 40.9099 | 232.0000 |
| 730.0000 | 8.0000 | 1.1000 | 40.9714 | 232.0000 |
| 730.0000 | 8.0000 | 1.2000 | 40.9756 | 232.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:04:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-VFL-JOINT-r1
- `archive_snapshot_sha256`: 230f8737cee8decd6fe2e2949cd832561402b8ba555cb8322726ea9038eceb82
- `seconds`: 42

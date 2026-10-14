# Development results: `BKB-EUROCUP-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 180 | 0.2203 | 0.2535 | -0.0386 | -0.0588 | -0.0184 | 19 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 179 | 0.2071 | 0.2408 | -0.0273 | -0.0496 | -0.0050 | 19 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 180 | 0.2083 | 0.2425 | -0.0258 | -0.0513 | -0.0003 | 19 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 539 | 0.2119 | 0.2456 | -0.0306 | -0.0430 | -0.0182 | 57 | BELOW_ZERO |
| Home-win log loss | 2023 | 180 | 0.6309 | 0.7004 | -0.0834 | -0.1304 | -0.0364 | 19 | BELOW_ZERO |
| Home-win log loss | 2024 | 179 | 0.6008 | 0.6746 | -0.0607 | -0.1074 | -0.0141 | 19 | BELOW_ZERO |
| Home-win log loss | 2025 | 180 | 0.6046 | 0.6780 | -0.0563 | -0.1091 | -0.0035 | 19 | BELOW_ZERO |
| Home-win log loss | ALL | 539 | 0.6121 | 0.6843 | -0.0668 | -0.0934 | -0.0402 | 57 | BELOW_ZERO |
| Margin CRPS | 2023 | 180 | 7.4550 | 8.2415 | -0.7916 | -1.1606 | -0.4226 | 19 | BELOW_ZERO |
| Margin CRPS | 2024 | 179 | 7.6078 | 8.3706 | -0.5794 | -1.1040 | -0.0547 | 19 | BELOW_ZERO |
| Margin CRPS | 2025 | 180 | 8.2613 | 9.3410 | -1.0175 | -1.4405 | -0.5944 | 19 | BELOW_ZERO |
| Margin CRPS | ALL | 539 | 7.7750 | 8.6515 | -0.7961 | -1.0407 | -0.5516 | 57 | BELOW_ZERO |
| Total CRPS | 2023 | 180 | 10.3499 | 11.6475 | -1.1773 | -1.6939 | -0.6606 | 19 | BELOW_ZERO |
| Total CRPS | 2024 | 179 | 9.9185 | 10.0441 | -0.4687 | -1.4424 | 0.5050 | 19 | SPANS_ZERO |
| Total CRPS | 2025 | 180 | 10.3568 | 11.3877 | -1.1385 | -1.7144 | -0.5625 | 19 | BELOW_ZERO |
| Total CRPS | ALL | 539 | 10.2089 | 11.0283 | -0.9282 | -1.3260 | -0.5303 | 57 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 180 | 0.2028 | 0.2494 | -0.0538 | -0.0786 | -0.0290 | 19 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 179 | 0.2542 | 0.2499 | -0.0034 | -0.0311 | 0.0242 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 180 | 0.2229 | 0.2466 | -0.0267 | -0.0431 | -0.0103 | 19 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 539 | 0.2266 | 0.2486 | -0.0280 | -0.0418 | -0.0142 | 57 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 180 | 0.2203 | 0.2223 | -0.0033 | -0.0152 | 0.0086 | 19 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 179 | 0.2071 | 0.2214 | -0.0133 | -0.0248 | -0.0017 | 19 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 180 | 0.2083 | 0.2166 | -0.0047 | -0.0161 | 0.0068 | 19 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 539 | 0.2119 | 0.2201 | -0.0071 | -0.0135 | -0.0007 | 57 | BELOW_ZERO |
| Home-win log loss | 2023 | 180 | 0.6309 | 0.6351 | -0.0084 | -0.0346 | 0.0179 | 19 | SPANS_ZERO |
| Home-win log loss | 2024 | 179 | 0.6008 | 0.6342 | -0.0312 | -0.0563 | -0.0062 | 19 | BELOW_ZERO |
| Home-win log loss | 2025 | 180 | 0.6046 | 0.6233 | -0.0112 | -0.0351 | 0.0128 | 19 | SPANS_ZERO |
| Home-win log loss | ALL | 539 | 0.6121 | 0.6308 | -0.0169 | -0.0308 | -0.0031 | 57 | BELOW_ZERO |
| Margin CRPS | 2023 | 180 | 7.4550 | 7.4596 | 0.0053 | -0.2216 | 0.2322 | 19 | SPANS_ZERO |
| Margin CRPS | 2024 | 179 | 7.6078 | 7.9219 | -0.2841 | -0.5334 | -0.0347 | 19 | BELOW_ZERO |
| Margin CRPS | 2025 | 180 | 8.2613 | 8.5513 | -0.2612 | -0.4526 | -0.0697 | 19 | BELOW_ZERO |
| Margin CRPS | ALL | 539 | 7.7750 | 7.9777 | -0.1800 | -0.3060 | -0.0540 | 57 | BELOW_ZERO |
| Total CRPS | 2023 | 180 | 10.3499 | 10.7335 | -0.3125 | -0.7690 | 0.1441 | 19 | SPANS_ZERO |
| Total CRPS | 2024 | 179 | 9.9185 | 9.9026 | -0.0849 | -0.5421 | 0.3723 | 19 | SPANS_ZERO |
| Total CRPS | 2025 | 180 | 10.3568 | 10.3906 | -0.1116 | -0.4829 | 0.2598 | 19 | SPANS_ZERO |
| Total CRPS | ALL | 539 | 10.2089 | 10.3430 | -0.1696 | -0.4038 | 0.0645 | 57 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 180 | 0.2028 | 0.2087 | -0.0064 | -0.0189 | 0.0061 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 179 | 0.2542 | 0.2456 | 0.0061 | -0.0105 | 0.0228 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 180 | 0.2229 | 0.2219 | -0.0008 | -0.0105 | 0.0089 | 19 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 539 | 0.2266 | 0.2254 | -0.0003 | -0.0076 | 0.0069 | 57 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0131; ECE 0.0347; logistic slope 1.265 (SE 0.158), intercept -0.142 (SE 0.105). Brier decomposition: reliability 0.0026, resolution 0.0335, uncertainty 0.2449.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 1 | 0.1447 | 0.0000 | 0.0000 | 0.7935 |
| [0.2, 0.3) | 19 | 0.2637 | 0.3158 | 0.1536 | 0.5399 |
| [0.3, 0.4) | 49 | 0.3556 | 0.2449 | 0.1460 | 0.3809 |
| [0.4, 0.5) | 91 | 0.4562 | 0.3956 | 0.3013 | 0.4983 |
| [0.5, 0.6) | 132 | 0.5559 | 0.5530 | 0.4679 | 0.6352 |
| [0.6, 0.7) | 113 | 0.6519 | 0.6460 | 0.5544 | 0.7281 |
| [0.7, 0.8) | 94 | 0.7462 | 0.7766 | 0.6825 | 0.8490 |
| [0.8, 0.9) | 37 | 0.8388 | 0.8919 | 0.7529 | 0.9571 |
| [0.9, 1.0] | 3 | 0.9141 | 0.6667 | 0.2077 | 0.9385 |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 365.0000 | 8.0000 | 1.1000 | 16.6015 | 354.0000 |
| 365.0000 | 8.0000 | 1.0000 | 16.6072 | 354.0000 |
| 365.0000 | 8.0000 | 1.2000 | 16.6130 | 354.0000 |
| 180.0000 | 8.0000 | 1.1000 | 16.6255 | 354.0000 |
| 730.0000 | 8.0000 | 1.1000 | 16.6324 | 354.0000 |
| 180.0000 | 8.0000 | 1.0000 | 16.6332 | 354.0000 |
| 180.0000 | 8.0000 | 1.2000 | 16.6352 | 354.0000 |
| 365.0000 | 8.0000 | 1.3000 | 16.6386 | 354.0000 |
| 730.0000 | 8.0000 | 1.0000 | 16.6408 | 354.0000 |
| 730.0000 | 8.0000 | 1.2000 | 16.6412 | 354.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:00:51Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-EUROCUP-JOINT-r1
- `archive_snapshot_sha256`: 2ce7859cf98d73c270504b37e4548e5a304d6445e27d3c71604f7ad587e20834
- `seconds`: 70

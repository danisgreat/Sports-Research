# Development results: `AMF-NFL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 272 | 0.2300 | 0.2472 | -0.0167 | -0.0242 | -0.0091 | 18 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 272 | 0.2199 | 0.2499 | -0.0310 | -0.0470 | -0.0150 | 18 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 272 | 0.2274 | 0.2499 | -0.0232 | -0.0358 | -0.0106 | 18 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 816 | 0.2258 | 0.2490 | -0.0236 | -0.0305 | -0.0167 | 54 | BELOW_ZERO |
| Home-win log loss | 2023 | 272 | 0.6517 | 0.6875 | -0.0347 | -0.0509 | -0.0186 | 18 | BELOW_ZERO |
| Home-win log loss | 2024 | 272 | 0.6302 | 0.6930 | -0.0647 | -0.0987 | -0.0307 | 18 | BELOW_ZERO |
| Home-win log loss | 2025 | 272 | 0.6455 | 0.6930 | -0.0489 | -0.0764 | -0.0213 | 18 | BELOW_ZERO |
| Home-win log loss | ALL | 816 | 0.6425 | 0.6912 | -0.0494 | -0.0643 | -0.0346 | 54 | BELOW_ZERO |
| Margin CRPS | 2023 | 272 | 7.5456 | 8.0608 | -0.5094 | -0.7016 | -0.3171 | 18 | BELOW_ZERO |
| Margin CRPS | 2024 | 272 | 7.4206 | 8.0820 | -0.6706 | -0.9877 | -0.3536 | 18 | BELOW_ZERO |
| Margin CRPS | 2025 | 272 | 7.3954 | 8.0029 | -0.6130 | -0.9328 | -0.2933 | 18 | BELOW_ZERO |
| Margin CRPS | ALL | 816 | 7.4539 | 8.0486 | -0.5977 | -0.7510 | -0.4444 | 54 | BELOW_ZERO |
| Total CRPS | 2023 | 272 | 7.5480 | 7.8727 | -0.3198 | -0.6308 | -0.0089 | 18 | BELOW_ZERO |
| Total CRPS | 2024 | 272 | 7.1728 | 7.2740 | -0.0956 | -0.2582 | 0.0671 | 18 | SPANS_ZERO |
| Total CRPS | 2025 | 272 | 7.5617 | 7.8073 | -0.2467 | -0.4941 | 0.0007 | 18 | SPANS_ZERO |
| Total CRPS | ALL | 816 | 7.4275 | 7.6514 | -0.2207 | -0.3566 | -0.0848 | 54 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 272 | 0.2442 | 0.2588 | -0.0150 | -0.0303 | 0.0003 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 272 | 0.2452 | 0.2488 | -0.0036 | -0.0136 | 0.0064 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 272 | 0.2344 | 0.2488 | -0.0144 | -0.0260 | -0.0027 | 18 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 816 | 0.2413 | 0.2521 | -0.0110 | -0.0179 | -0.0041 | 54 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 272 | 0.2300 | 0.2356 | -0.0055 | -0.0122 | 0.0011 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 272 | 0.2199 | 0.2264 | -0.0072 | -0.0161 | 0.0018 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 272 | 0.2274 | 0.2292 | -0.0016 | -0.0132 | 0.0099 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 816 | 0.2258 | 0.2304 | -0.0048 | -0.0098 | 0.0002 | 54 | SPANS_ZERO |
| Home-win log loss | 2023 | 272 | 0.6517 | 0.6631 | -0.0114 | -0.0252 | 0.0024 | 18 | SPANS_ZERO |
| Home-win log loss | 2024 | 272 | 0.6302 | 0.6442 | -0.0153 | -0.0342 | 0.0037 | 18 | SPANS_ZERO |
| Home-win log loss | 2025 | 272 | 0.6455 | 0.6493 | -0.0035 | -0.0286 | 0.0216 | 18 | SPANS_ZERO |
| Home-win log loss | ALL | 816 | 0.6425 | 0.6522 | -0.0100 | -0.0208 | 0.0007 | 54 | SPANS_ZERO |
| Margin CRPS | 2023 | 272 | 7.5456 | 7.6672 | -0.1266 | -0.2683 | 0.0151 | 18 | SPANS_ZERO |
| Margin CRPS | 2024 | 272 | 7.4206 | 7.5072 | -0.0908 | -0.2783 | 0.0967 | 18 | SPANS_ZERO |
| Margin CRPS | 2025 | 272 | 7.3954 | 7.4879 | -0.0921 | -0.3345 | 0.1504 | 18 | SPANS_ZERO |
| Margin CRPS | ALL | 816 | 7.4539 | 7.5541 | -0.1031 | -0.2082 | 0.0019 | 54 | SPANS_ZERO |
| Total CRPS | 2023 | 272 | 7.5480 | 7.6206 | -0.0783 | -0.2678 | 0.1111 | 18 | SPANS_ZERO |
| Total CRPS | 2024 | 272 | 7.1728 | 7.2528 | -0.0795 | -0.2281 | 0.0692 | 18 | SPANS_ZERO |
| Total CRPS | 2025 | 272 | 7.5617 | 7.8225 | -0.2610 | -0.5206 | -0.0014 | 18 | BELOW_ZERO |
| Total CRPS | ALL | 816 | 7.4275 | 7.5653 | -0.1396 | -0.2522 | -0.0270 | 54 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 272 | 0.2442 | 0.2451 | -0.0014 | -0.0114 | 0.0085 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 272 | 0.2452 | 0.2465 | -0.0012 | -0.0096 | 0.0072 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 272 | 0.2344 | 0.2457 | -0.0113 | -0.0254 | 0.0028 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 816 | 0.2413 | 0.2457 | -0.0046 | -0.0108 | 0.0015 | 54 | SPANS_ZERO |


## Variant: KEYNUM_vs_MODEL (NFL key-number reweighting minus the plain model)

| metric | season | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 0.0001 | -0.0002 | 0.0004 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 0.0007 | -0.0000 | 0.0014 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 0.0001 | -0.0006 | 0.0009 | 18 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 0.0003 | -0.0000 | 0.0006 | 54 | SPANS_ZERO |
| Home-win log loss | 2023 | 0.0002 | -0.0005 | 0.0010 | 18 | SPANS_ZERO |
| Home-win log loss | 2024 | 0.0015 | -0.0001 | 0.0032 | 18 | SPANS_ZERO |
| Home-win log loss | 2025 | 0.0004 | -0.0014 | 0.0022 | 18 | SPANS_ZERO |
| Home-win log loss | ALL | 0.0007 | -0.0001 | 0.0015 | 54 | SPANS_ZERO |
| Margin CRPS | 2023 | -0.0028 | -0.0246 | 0.0189 | 18 | SPANS_ZERO |
| Margin CRPS | 2024 | -0.0010 | -0.0387 | 0.0368 | 18 | SPANS_ZERO |
| Margin CRPS | 2025 | -0.0031 | -0.0459 | 0.0397 | 18 | SPANS_ZERO |
| Margin CRPS | ALL | -0.0023 | -0.0213 | 0.0167 | 54 | SPANS_ZERO |
| Total CRPS | 2023 | -0.0033 | -0.0071 | 0.0005 | 18 | SPANS_ZERO |
| Total CRPS | 2024 | 0.0018 | -0.0020 | 0.0056 | 18 | SPANS_ZERO |
| Total CRPS | 2025 | -0.0009 | -0.0058 | 0.0039 | 18 | SPANS_ZERO |
| Total CRPS | ALL | -0.0008 | -0.0031 | 0.0015 | 54 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | -0.0002 | -0.0004 | -0.0000 | 18 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 0.0000 | -0.0001 | 0.0002 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | -0.0000 | -0.0003 | 0.0002 | 18 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | -0.0001 | -0.0002 | 0.0001 | 54 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0228; ECE 0.0530; logistic slope 1.326 (SE 0.157), intercept -0.180 (SE 0.084). Brier decomposition: reliability 0.0036, resolution 0.0251, uncertainty 0.2483.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 14 | 0.2639 | 0.2857 | 0.1172 | 0.5465 |
| [0.3, 0.4) | 61 | 0.3631 | 0.3443 | 0.2375 | 0.4695 |
| [0.4, 0.5) | 171 | 0.4574 | 0.3684 | 0.2998 | 0.4429 |
| [0.5, 0.6) | 258 | 0.5511 | 0.4961 | 0.4356 | 0.5567 |
| [0.6, 0.7) | 205 | 0.6507 | 0.6976 | 0.6315 | 0.7563 |
| [0.7, 0.8) | 88 | 0.7429 | 0.7386 | 0.6382 | 0.8191 |
| [0.8, 0.9) | 19 | 0.8204 | 0.9474 | 0.7536 | 0.9906 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.0113 | 1.2631 | 272 | 0.2300 | 0.2302 | 0.0002 | -0.0018 | 0.0022 | SPANS_ZERO |
| 2024 | -0.0518 | 1.1176 | 272 | 0.2199 | 0.2180 | -0.0020 | -0.0040 | -0.0001 | BELOW_ZERO |
| 2025 | -0.2662 | 1.6634 | 272 | 0.2274 | 0.2266 | -0.0013 | -0.0089 | 0.0064 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 8.0000 | 1.1000 | 15.0513 | 543.0000 |
| 180.0000 | 8.0000 | 1.0000 | 15.0544 | 543.0000 |
| 180.0000 | 8.0000 | 1.2000 | 15.0633 | 543.0000 |
| 180.0000 | 8.0000 | 1.3000 | 15.0876 | 543.0000 |
| 90.0000 | 8.0000 | 1.1000 | 15.1091 | 543.0000 |
| 90.0000 | 8.0000 | 1.2000 | 15.1101 | 543.0000 |
| 365.0000 | 8.0000 | 1.0000 | 15.1193 | 543.0000 |
| 365.0000 | 8.0000 | 1.1000 | 15.1206 | 543.0000 |
| 90.0000 | 8.0000 | 1.0000 | 15.1234 | 543.0000 |
| 90.0000 | 8.0000 | 1.3000 | 15.1237 | 543.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:00:32Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AMF-NFL-JOINT-r1
- `archive_snapshot_sha256`: 6a3e2ed90a8ac962a6ec085295498c8acc8bd15774c2d5de3b86ac0d19a1eadf
- `seconds`: 83

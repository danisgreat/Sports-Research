# Development results: `BKB-B-LEAGUE-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `PASS_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `BELOW_ZERO_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 720 | 0.2000 | 0.2496 | -0.0516 | -0.0647 | -0.0385 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 719 | 0.1986 | 0.2494 | -0.0541 | -0.0689 | -0.0393 | 27 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 780 | 0.2068 | 0.2497 | -0.0413 | -0.0567 | -0.0260 | 24 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 2219 | 0.2019 | 0.2496 | -0.0493 | -0.0573 | -0.0413 | 77 | BELOW_ZERO |
| Home-win log loss | 2023 | 720 | 0.5846 | 0.6924 | -0.1114 | -0.1402 | -0.0825 | 26 | BELOW_ZERO |
| Home-win log loss | 2024 | 719 | 0.5812 | 0.6920 | -0.1181 | -0.1517 | -0.0844 | 27 | BELOW_ZERO |
| Home-win log loss | 2025 | 780 | 0.6002 | 0.6926 | -0.0885 | -0.1232 | -0.0539 | 24 | BELOW_ZERO |
| Home-win log loss | ALL | 2219 | 0.5890 | 0.6923 | -0.1066 | -0.1247 | -0.0885 | 77 | BELOW_ZERO |
| Margin CRPS | 2023 | 720 | 7.4676 | 8.7245 | -1.2523 | -1.5332 | -0.9714 | 26 | BELOW_ZERO |
| Margin CRPS | 2024 | 719 | 7.3407 | 8.4787 | -1.2147 | -1.5589 | -0.8706 | 27 | BELOW_ZERO |
| Margin CRPS | 2025 | 780 | 7.4535 | 8.5704 | -1.0584 | -1.4407 | -0.6762 | 24 | BELOW_ZERO |
| Margin CRPS | ALL | 2219 | 7.4215 | 8.5907 | -1.1787 | -1.3649 | -0.9925 | 77 | BELOW_ZERO |
| Total CRPS | 2023 | 720 | 9.2009 | 9.9699 | -0.8493 | -1.2153 | -0.4833 | 26 | BELOW_ZERO |
| Total CRPS | 2024 | 719 | 9.0577 | 10.1113 | -1.0835 | -1.4320 | -0.7351 | 27 | BELOW_ZERO |
| Total CRPS | 2025 | 780 | 9.5024 | 9.9661 | -0.4561 | -0.8638 | -0.0484 | 24 | BELOW_ZERO |
| Total CRPS | ALL | 2219 | 9.2605 | 10.0144 | -0.8089 | -1.0223 | -0.5954 | 77 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 720 | 0.2264 | 0.2488 | -0.0236 | -0.0355 | -0.0117 | 26 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 719 | 0.2162 | 0.2501 | -0.0348 | -0.0473 | -0.0223 | 27 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 780 | 0.2364 | 0.2488 | -0.0119 | -0.0238 | -0.0000 | 24 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 2219 | 0.2266 | 0.2492 | -0.0239 | -0.0309 | -0.0169 | 77 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 720 | 0.2000 | 0.2112 | -0.0131 | -0.0203 | -0.0060 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 719 | 0.1986 | 0.2150 | -0.0179 | -0.0253 | -0.0105 | 27 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 780 | 0.2068 | 0.2185 | -0.0118 | -0.0192 | -0.0043 | 24 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 2219 | 0.2019 | 0.2150 | -0.0144 | -0.0184 | -0.0103 | 77 | BELOW_ZERO |
| Home-win log loss | 2023 | 720 | 0.5846 | 0.6120 | -0.0309 | -0.0472 | -0.0147 | 26 | BELOW_ZERO |
| Home-win log loss | 2024 | 719 | 0.5812 | 0.6209 | -0.0431 | -0.0612 | -0.0251 | 27 | BELOW_ZERO |
| Home-win log loss | 2025 | 780 | 0.6002 | 0.6277 | -0.0271 | -0.0450 | -0.0093 | 24 | BELOW_ZERO |
| Home-win log loss | ALL | 2219 | 0.5890 | 0.6204 | -0.0340 | -0.0437 | -0.0243 | 77 | BELOW_ZERO |
| Margin CRPS | 2023 | 720 | 7.4676 | 7.7922 | -0.3373 | -0.4825 | -0.1922 | 26 | BELOW_ZERO |
| Margin CRPS | 2024 | 719 | 7.3407 | 7.6614 | -0.3726 | -0.5754 | -0.1698 | 27 | BELOW_ZERO |
| Margin CRPS | 2025 | 780 | 7.4535 | 7.7697 | -0.3112 | -0.5139 | -0.1086 | 24 | BELOW_ZERO |
| Margin CRPS | ALL | 2219 | 7.4215 | 7.7419 | -0.3416 | -0.4438 | -0.2394 | 77 | BELOW_ZERO |
| Total CRPS | 2023 | 720 | 9.2009 | 9.4564 | -0.3341 | -0.6955 | 0.0274 | 26 | SPANS_ZERO |
| Total CRPS | 2024 | 719 | 9.0577 | 9.4559 | -0.4175 | -0.6501 | -0.1849 | 27 | BELOW_ZERO |
| Total CRPS | 2025 | 780 | 9.5024 | 9.5209 | -0.0179 | -0.2918 | 0.2561 | 24 | SPANS_ZERO |
| Total CRPS | ALL | 2219 | 9.2605 | 9.4789 | -0.2648 | -0.4313 | -0.0983 | 77 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 720 | 0.2264 | 0.2328 | -0.0077 | -0.0202 | 0.0048 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 719 | 0.2162 | 0.2283 | -0.0126 | -0.0216 | -0.0036 | 27 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 780 | 0.2364 | 0.2351 | 0.0013 | -0.0075 | 0.0101 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 2219 | 0.2266 | 0.2321 | -0.0066 | -0.0124 | -0.0008 | 77 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0033; ECE 0.0228; logistic slope 1.075 (SE 0.057), intercept 0.012 (SE 0.047). Brier decomposition: reliability 0.0009, resolution 0.0484, uncertainty 0.2495.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 18 | 0.0800 | 0.0556 | 0.0099 | 0.2576 |
| [0.1, 0.2) | 129 | 0.1603 | 0.1550 | 0.1027 | 0.2274 |
| [0.2, 0.3) | 249 | 0.2531 | 0.2691 | 0.2178 | 0.3274 |
| [0.3, 0.4) | 315 | 0.3521 | 0.3302 | 0.2805 | 0.3839 |
| [0.4, 0.5) | 317 | 0.4498 | 0.4353 | 0.3818 | 0.4904 |
| [0.5, 0.6) | 338 | 0.5450 | 0.5414 | 0.4881 | 0.5938 |
| [0.6, 0.7) | 346 | 0.6473 | 0.6272 | 0.5751 | 0.6765 |
| [0.7, 0.8) | 281 | 0.7489 | 0.8221 | 0.7731 | 0.8623 |
| [0.8, 0.9) | 200 | 0.8427 | 0.8650 | 0.8107 | 0.9055 |
| [0.9, 1.0] | 26 | 0.9183 | 0.8846 | 0.7102 | 0.9600 |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.0194 | 0.9871 | 720 | 0.2000 | 0.2001 | 0.0001 | -0.0004 | 0.0005 | SPANS_ZERO |
| 2024 | 0.0389 | 1.0966 | 719 | 0.1986 | 0.1985 | -0.0002 | -0.0014 | 0.0010 | SPANS_ZERO |
| 2025 | -0.0249 | 1.1300 | 780 | 0.2068 | 0.2072 | 0.0004 | -0.0011 | 0.0019 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 2.0000 | 1.1000 | 16.1684 | 1322.0000 |
| 90.0000 | 2.0000 | 1.0000 | 16.1689 | 1322.0000 |
| 90.0000 | 2.0000 | 1.2000 | 16.1843 | 1322.0000 |
| 90.0000 | 1.0000 | 1.1000 | 16.1953 | 1322.0000 |
| 90.0000 | 1.0000 | 1.0000 | 16.1969 | 1322.0000 |
| 90.0000 | 1.0000 | 1.2000 | 16.2101 | 1322.0000 |
| 90.0000 | 2.0000 | 1.3000 | 16.2136 | 1322.0000 |
| 90.0000 | 1.0000 | 1.3000 | 16.2383 | 1322.0000 |
| 90.0000 | 8.0000 | 1.0000 | 16.2522 | 1322.0000 |
| 90.0000 | 8.0000 | 1.1000 | 16.2558 | 1322.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:02:45Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-B-LEAGUE-JOINT-r1
- `archive_snapshot_sha256`: be13f37084c10310045ff6214298db22ed83fce1d5cacae2dbeb99be62df519d
- `seconds`: 216

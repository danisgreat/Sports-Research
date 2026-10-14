# Development results: `BKB-EUROLEAGUE-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 306 | 0.1981 | 0.2277 | -0.0278 | -0.0403 | -0.0153 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 306 | 0.2154 | 0.2381 | -0.0225 | -0.0368 | -0.0082 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 380 | 0.2214 | 0.2316 | -0.0124 | -0.0219 | -0.0029 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 992 | 0.2124 | 0.2324 | -0.0207 | -0.0275 | -0.0138 | 80 | BELOW_ZERO |
| Home-win log loss | 2023 | 306 | 0.5814 | 0.6479 | -0.0617 | -0.0894 | -0.0339 | 26 | BELOW_ZERO |
| Home-win log loss | 2024 | 306 | 0.6174 | 0.6691 | -0.0515 | -0.0830 | -0.0200 | 26 | BELOW_ZERO |
| Home-win log loss | 2025 | 380 | 0.6324 | 0.6559 | -0.0278 | -0.0481 | -0.0075 | 28 | BELOW_ZERO |
| Home-win log loss | ALL | 992 | 0.6120 | 0.6575 | -0.0465 | -0.0615 | -0.0315 | 80 | BELOW_ZERO |
| Margin CRPS | 2023 | 306 | 6.4533 | 6.9789 | -0.5296 | -0.8087 | -0.2505 | 26 | BELOW_ZERO |
| Margin CRPS | 2024 | 306 | 6.6284 | 7.1348 | -0.4916 | -0.7792 | -0.2041 | 26 | BELOW_ZERO |
| Margin CRPS | 2025 | 380 | 6.5406 | 6.8073 | -0.3058 | -0.5154 | -0.0962 | 28 | BELOW_ZERO |
| Margin CRPS | ALL | 992 | 6.5408 | 6.9613 | -0.4389 | -0.5834 | -0.2945 | 80 | BELOW_ZERO |
| Total CRPS | 2023 | 306 | 8.9700 | 9.6418 | -0.6958 | -1.0525 | -0.3391 | 26 | BELOW_ZERO |
| Total CRPS | 2024 | 306 | 9.2913 | 10.0831 | -0.8424 | -1.3292 | -0.3556 | 26 | BELOW_ZERO |
| Total CRPS | 2025 | 380 | 9.8368 | 10.8669 | -1.0662 | -1.4992 | -0.6333 | 28 | BELOW_ZERO |
| Total CRPS | ALL | 992 | 9.4012 | 10.2472 | -0.8731 | -1.1124 | -0.6338 | 80 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 306 | 0.2266 | 0.2492 | -0.0209 | -0.0357 | -0.0061 | 26 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 306 | 0.2263 | 0.2512 | -0.0275 | -0.0406 | -0.0145 | 26 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 380 | 0.2206 | 0.2458 | -0.0281 | -0.0404 | -0.0159 | 28 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 992 | 0.2242 | 0.2485 | -0.0256 | -0.0330 | -0.0182 | 80 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 306 | 0.1981 | 0.2088 | -0.0107 | -0.0180 | -0.0034 | 26 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 306 | 0.2154 | 0.2235 | -0.0087 | -0.0180 | 0.0007 | 26 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 380 | 0.2214 | 0.2248 | -0.0035 | -0.0092 | 0.0022 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 992 | 0.2124 | 0.2195 | -0.0075 | -0.0117 | -0.0033 | 80 | BELOW_ZERO |
| Home-win log loss | 2023 | 306 | 0.5814 | 0.6060 | -0.0238 | -0.0399 | -0.0078 | 26 | BELOW_ZERO |
| Home-win log loss | 2024 | 306 | 0.6174 | 0.6373 | -0.0214 | -0.0423 | -0.0006 | 26 | BELOW_ZERO |
| Home-win log loss | 2025 | 380 | 0.6324 | 0.6411 | -0.0088 | -0.0209 | 0.0033 | 28 | SPANS_ZERO |
| Home-win log loss | ALL | 992 | 0.6120 | 0.6291 | -0.0178 | -0.0270 | -0.0085 | 80 | BELOW_ZERO |
| Margin CRPS | 2023 | 306 | 6.4533 | 6.6497 | -0.2142 | -0.3574 | -0.0709 | 26 | BELOW_ZERO |
| Margin CRPS | 2024 | 306 | 6.6284 | 6.8367 | -0.2103 | -0.3989 | -0.0218 | 26 | BELOW_ZERO |
| Margin CRPS | 2025 | 380 | 6.5406 | 6.5902 | -0.0485 | -0.1425 | 0.0456 | 28 | SPANS_ZERO |
| Margin CRPS | ALL | 992 | 6.5408 | 6.6846 | -0.1549 | -0.2367 | -0.0731 | 80 | BELOW_ZERO |
| Total CRPS | 2023 | 306 | 8.9700 | 9.0601 | -0.0960 | -0.2379 | 0.0459 | 26 | SPANS_ZERO |
| Total CRPS | 2024 | 306 | 9.2913 | 9.1363 | 0.1510 | -0.0661 | 0.3682 | 26 | SPANS_ZERO |
| Total CRPS | 2025 | 380 | 9.8368 | 9.9955 | -0.1694 | -0.3461 | 0.0073 | 28 | SPANS_ZERO |
| Total CRPS | ALL | 992 | 9.4012 | 9.4419 | -0.0414 | -0.1459 | 0.0631 | 80 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 306 | 0.2266 | 0.2283 | -0.0007 | -0.0072 | 0.0058 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 306 | 0.2263 | 0.2228 | 0.0038 | -0.0045 | 0.0122 | 26 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 380 | 0.2206 | 0.2230 | -0.0044 | -0.0110 | 0.0022 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 992 | 0.2242 | 0.2246 | -0.0005 | -0.0045 | 0.0035 | 80 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0145; ECE 0.0403; logistic slope 1.235 (SE 0.138), intercept -0.037 (SE 0.092). Brier decomposition: reliability 0.0031, resolution 0.0206, uncertainty 0.2320.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 1 | 0.1775 | 0.0000 | 0.0000 | 0.7935 |
| [0.2, 0.3) | 6 | 0.2645 | 0.0000 | 0.0000 | 0.3903 |
| [0.3, 0.4) | 39 | 0.3652 | 0.3077 | 0.1857 | 0.4642 |
| [0.4, 0.5) | 118 | 0.4570 | 0.5593 | 0.4693 | 0.6456 |
| [0.5, 0.6) | 254 | 0.5543 | 0.5197 | 0.4584 | 0.5804 |
| [0.6, 0.7) | 312 | 0.6515 | 0.6731 | 0.6192 | 0.7227 |
| [0.7, 0.8) | 199 | 0.7418 | 0.7487 | 0.6842 | 0.8039 |
| [0.8, 0.9) | 59 | 0.8362 | 0.9492 | 0.8608 | 0.9826 |
| [0.9, 1.0] | 4 | 0.9093 | 1.0000 | 0.5101 | 1.0000 |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.0491 | 1.0321 | 306 | 0.1981 | 0.1974 | -0.0002 | -0.0016 | 0.0013 | SPANS_ZERO |
| 2024 | -0.1158 | 1.5106 | 306 | 0.2154 | 0.2179 | 0.0028 | -0.0040 | 0.0095 | SPANS_ZERO |
| 2025 | -0.1564 | 1.2195 | 380 | 0.2214 | 0.2233 | 0.0013 | -0.0013 | 0.0038 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 8.0000 | 1.1000 | 16.0242 | 584.0000 |
| 180.0000 | 8.0000 | 1.0000 | 16.0256 | 584.0000 |
| 180.0000 | 8.0000 | 1.2000 | 16.0391 | 584.0000 |
| 90.0000 | 8.0000 | 1.1000 | 16.0501 | 584.0000 |
| 90.0000 | 8.0000 | 1.0000 | 16.0576 | 584.0000 |
| 90.0000 | 8.0000 | 1.2000 | 16.0588 | 584.0000 |
| 365.0000 | 8.0000 | 1.0000 | 16.0594 | 584.0000 |
| 365.0000 | 8.0000 | 1.1000 | 16.0606 | 584.0000 |
| 180.0000 | 8.0000 | 1.3000 | 16.0671 | 584.0000 |
| 365.0000 | 8.0000 | 1.2000 | 16.0781 | 584.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:02:09Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-EUROLEAGUE-JOINT-r1
- `archive_snapshot_sha256`: be335921205567a11b625046f80d2b2011c835a56a25427eaad2df6992cfaa9d
- `seconds`: 106

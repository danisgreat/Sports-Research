# Development results: `BKB-KBL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 270 | 0.2205 | 0.2463 | -0.0247 | -0.0431 | -0.0063 | 23 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 270 | 0.2349 | 0.2494 | -0.0154 | -0.0296 | -0.0011 | 24 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 270 | 0.2353 | 0.2480 | -0.0110 | -0.0240 | 0.0019 | 26 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 810 | 0.2302 | 0.2479 | -0.0168 | -0.0252 | -0.0083 | 73 | BELOW_ZERO |
| Home-win log loss | 2023 | 270 | 0.6316 | 0.6857 | -0.0522 | -0.0916 | -0.0127 | 23 | BELOW_ZERO |
| Home-win log loss | 2024 | 270 | 0.6628 | 0.6919 | -0.0310 | -0.0607 | -0.0013 | 24 | BELOW_ZERO |
| Home-win log loss | 2025 | 270 | 0.6637 | 0.6891 | -0.0219 | -0.0489 | 0.0050 | 26 | SPANS_ZERO |
| Home-win log loss | ALL | 810 | 0.6527 | 0.6889 | -0.0344 | -0.0523 | -0.0166 | 73 | BELOW_ZERO |
| Margin CRPS | 2023 | 270 | 7.4987 | 8.1820 | -0.6442 | -1.0169 | -0.2716 | 23 | BELOW_ZERO |
| Margin CRPS | 2024 | 270 | 7.3986 | 7.5553 | -0.1691 | -0.4535 | 0.1153 | 24 | SPANS_ZERO |
| Margin CRPS | 2025 | 270 | 6.8573 | 7.0330 | -0.1396 | -0.4094 | 0.1302 | 26 | SPANS_ZERO |
| Margin CRPS | ALL | 810 | 7.2515 | 7.5901 | -0.3083 | -0.4859 | -0.1307 | 73 | BELOW_ZERO |
| Total CRPS | 2023 | 270 | 9.3832 | 10.1998 | -0.8317 | -1.4480 | -0.2154 | 23 | BELOW_ZERO |
| Total CRPS | 2024 | 270 | 9.1573 | 9.8927 | -0.7056 | -1.0986 | -0.3127 | 24 | BELOW_ZERO |
| Total CRPS | 2025 | 270 | 9.3929 | 10.4784 | -1.0660 | -1.6233 | -0.5086 | 26 | BELOW_ZERO |
| Total CRPS | ALL | 810 | 9.3111 | 10.1903 | -0.8737 | -1.1671 | -0.5802 | 73 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 270 | 0.2229 | 0.2466 | -0.0240 | -0.0408 | -0.0071 | 23 | BELOW_ZERO |
| Over the league-median line, Brier | 2024 | 270 | 0.2296 | 0.2534 | -0.0236 | -0.0359 | -0.0113 | 24 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 270 | 0.2125 | 0.2498 | -0.0349 | -0.0573 | -0.0124 | 26 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 810 | 0.2217 | 0.2499 | -0.0277 | -0.0377 | -0.0177 | 73 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 270 | 0.2205 | 0.2207 | -0.0004 | -0.0058 | 0.0051 | 23 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 270 | 0.2349 | 0.2379 | -0.0044 | -0.0129 | 0.0041 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 270 | 0.2353 | 0.2389 | -0.0033 | -0.0106 | 0.0039 | 26 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 810 | 0.2302 | 0.2325 | -0.0028 | -0.0067 | 0.0012 | 73 | SPANS_ZERO |
| Home-win log loss | 2023 | 270 | 0.6316 | 0.6323 | -0.0012 | -0.0135 | 0.0111 | 23 | SPANS_ZERO |
| Home-win log loss | 2024 | 270 | 0.6628 | 0.6689 | -0.0092 | -0.0269 | 0.0085 | 24 | SPANS_ZERO |
| Home-win log loss | 2025 | 270 | 0.6637 | 0.6708 | -0.0066 | -0.0219 | 0.0088 | 26 | SPANS_ZERO |
| Home-win log loss | ALL | 810 | 0.6527 | 0.6573 | -0.0057 | -0.0142 | 0.0027 | 73 | SPANS_ZERO |
| Margin CRPS | 2023 | 270 | 7.4987 | 7.5991 | -0.0965 | -0.2427 | 0.0496 | 23 | SPANS_ZERO |
| Margin CRPS | 2024 | 270 | 7.3986 | 7.4077 | -0.0338 | -0.1995 | 0.1319 | 24 | SPANS_ZERO |
| Margin CRPS | 2025 | 270 | 6.8573 | 6.8953 | -0.0319 | -0.1762 | 0.1124 | 26 | SPANS_ZERO |
| Margin CRPS | ALL | 810 | 7.2515 | 7.3007 | -0.0529 | -0.1368 | 0.0310 | 73 | SPANS_ZERO |
| Total CRPS | 2023 | 270 | 9.3832 | 9.5979 | -0.2241 | -0.4692 | 0.0210 | 23 | SPANS_ZERO |
| Total CRPS | 2024 | 270 | 9.1573 | 8.8686 | 0.3211 | -0.0801 | 0.7223 | 24 | SPANS_ZERO |
| Total CRPS | 2025 | 270 | 9.3929 | 9.7239 | -0.3597 | -0.6655 | -0.0540 | 26 | BELOW_ZERO |
| Total CRPS | ALL | 810 | 9.3111 | 9.3968 | -0.0932 | -0.2847 | 0.0983 | 73 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 270 | 0.2229 | 0.2295 | -0.0073 | -0.0151 | 0.0006 | 23 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 270 | 0.2296 | 0.2221 | 0.0073 | -0.0073 | 0.0220 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 270 | 0.2125 | 0.2231 | -0.0105 | -0.0203 | -0.0008 | 26 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 810 | 0.2217 | 0.2249 | -0.0036 | -0.0100 | 0.0028 | 73 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0157; ECE 0.0331; logistic slope 1.070 (SE 0.147), intercept 0.060 (SE 0.075). Brier decomposition: reliability 0.0017, resolution 0.0200, uncertainty 0.2477.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 4 | 0.1906 | 0.2500 | 0.0456 | 0.6994 |
| [0.2, 0.3) | 21 | 0.2611 | 0.1905 | 0.0767 | 0.4000 |
| [0.3, 0.4) | 104 | 0.3640 | 0.4038 | 0.3146 | 0.4999 |
| [0.4, 0.5) | 181 | 0.4499 | 0.4199 | 0.3504 | 0.4927 |
| [0.5, 0.6) | 260 | 0.5501 | 0.5615 | 0.5008 | 0.6205 |
| [0.6, 0.7) | 169 | 0.6447 | 0.7160 | 0.6438 | 0.7786 |
| [0.7, 0.8) | 60 | 0.7432 | 0.7500 | 0.6277 | 0.8422 |
| [0.8, 0.9) | 11 | 0.8308 | 0.8182 | 0.5230 | 0.9486 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.0251 | 1.3710 | 270 | 0.2205 | 0.2217 | 0.0008 | -0.0039 | 0.0056 | SPANS_ZERO |
| 2024 | 0.1192 | 1.0206 | 270 | 0.2349 | 0.2354 | 0.0007 | -0.0030 | 0.0044 | SPANS_ZERO |
| 2025 | 0.0063 | 1.0944 | 270 | 0.2353 | 0.2349 | -0.0002 | -0.0014 | 0.0009 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 8.0000 | 1.1000 | 16.3707 | 540.0000 |
| 90.0000 | 8.0000 | 1.0000 | 16.3721 | 540.0000 |
| 180.0000 | 8.0000 | 1.0000 | 16.3728 | 540.0000 |
| 180.0000 | 8.0000 | 1.1000 | 16.3779 | 540.0000 |
| 180.0000 | 32.0000 | 1.0000 | 16.3839 | 540.0000 |
| 90.0000 | 8.0000 | 1.2000 | 16.3860 | 540.0000 |
| 180.0000 | 32.0000 | 1.1000 | 16.3927 | 540.0000 |
| 365.0000 | 32.0000 | 1.0000 | 16.3948 | 540.0000 |
| 180.0000 | 8.0000 | 1.2000 | 16.3996 | 540.0000 |
| 365.0000 | 8.0000 | 1.0000 | 16.4057 | 540.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:02:26Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-KBL-JOINT-r1
- `archive_snapshot_sha256`: 4ae0e14227af8cd619d34c35bb01b2192e6aa7f48dbdb8ea4f030cb77fc75af6
- `seconds`: 95

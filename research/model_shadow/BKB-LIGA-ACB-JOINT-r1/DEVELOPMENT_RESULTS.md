# Development results: `BKB-LIGA-ACB-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `PASS_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `BELOW_ZERO_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 306 | 0.1928 | 0.2346 | -0.0436 | -0.0582 | -0.0289 | 32 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 306 | 0.2001 | 0.2391 | -0.0390 | -0.0503 | -0.0276 | 33 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 306 | 0.2042 | 0.2428 | -0.0406 | -0.0600 | -0.0212 | 33 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 918 | 0.1990 | 0.2388 | -0.0410 | -0.0497 | -0.0324 | 98 | BELOW_ZERO |
| Home-win log loss | 2023 | 306 | 0.5687 | 0.6622 | -0.0973 | -0.1301 | -0.0644 | 32 | BELOW_ZERO |
| Home-win log loss | 2024 | 306 | 0.5841 | 0.6712 | -0.0872 | -0.1117 | -0.0628 | 33 | BELOW_ZERO |
| Home-win log loss | 2025 | 306 | 0.5929 | 0.6786 | -0.0891 | -0.1326 | -0.0457 | 33 | BELOW_ZERO |
| Home-win log loss | ALL | 918 | 0.5819 | 0.6707 | -0.0912 | -0.1104 | -0.0719 | 98 | BELOW_ZERO |
| Margin CRPS | 2023 | 306 | 6.3509 | 7.1927 | -0.8871 | -1.1889 | -0.5853 | 32 | BELOW_ZERO |
| Margin CRPS | 2024 | 306 | 6.6116 | 7.5498 | -0.9378 | -1.1845 | -0.6911 | 33 | BELOW_ZERO |
| Margin CRPS | 2025 | 306 | 7.0418 | 7.9411 | -0.9264 | -1.3394 | -0.5135 | 33 | BELOW_ZERO |
| Margin CRPS | ALL | 918 | 6.6681 | 7.5612 | -0.9174 | -1.1002 | -0.7346 | 98 | BELOW_ZERO |
| Total CRPS | 2023 | 306 | 9.6331 | 9.8526 | -0.2071 | -0.4879 | 0.0736 | 32 | SPANS_ZERO |
| Total CRPS | 2024 | 306 | 9.5094 | 10.6955 | -1.1655 | -1.5548 | -0.7763 | 33 | BELOW_ZERO |
| Total CRPS | 2025 | 306 | 9.6062 | 10.4974 | -0.6812 | -1.2554 | -0.1071 | 33 | BELOW_ZERO |
| Total CRPS | ALL | 918 | 9.5829 | 10.3485 | -0.6895 | -0.9439 | -0.4351 | 98 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 306 | 0.2456 | 0.2492 | -0.0032 | -0.0123 | 0.0059 | 32 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 306 | 0.2150 | 0.2439 | -0.0286 | -0.0419 | -0.0153 | 33 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 306 | 0.2150 | 0.2388 | -0.0186 | -0.0357 | -0.0014 | 33 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 918 | 0.2252 | 0.2440 | -0.0169 | -0.0248 | -0.0090 | 98 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 306 | 0.1928 | 0.2113 | -0.0193 | -0.0278 | -0.0108 | 32 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 306 | 0.2001 | 0.2144 | -0.0145 | -0.0224 | -0.0067 | 33 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 306 | 0.2042 | 0.2160 | -0.0126 | -0.0224 | -0.0028 | 33 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 918 | 0.1990 | 0.2139 | -0.0154 | -0.0203 | -0.0105 | 98 | BELOW_ZERO |
| Home-win log loss | 2023 | 306 | 0.5687 | 0.6122 | -0.0452 | -0.0648 | -0.0257 | 32 | BELOW_ZERO |
| Home-win log loss | 2024 | 306 | 0.5841 | 0.6172 | -0.0338 | -0.0501 | -0.0175 | 33 | BELOW_ZERO |
| Home-win log loss | 2025 | 306 | 0.5929 | 0.6215 | -0.0296 | -0.0526 | -0.0067 | 33 | BELOW_ZERO |
| Home-win log loss | ALL | 918 | 0.5819 | 0.6169 | -0.0361 | -0.0472 | -0.0250 | 98 | BELOW_ZERO |
| Margin CRPS | 2023 | 306 | 6.3509 | 6.6723 | -0.3442 | -0.5315 | -0.1569 | 32 | BELOW_ZERO |
| Margin CRPS | 2024 | 306 | 6.6116 | 6.9625 | -0.3585 | -0.5209 | -0.1961 | 33 | BELOW_ZERO |
| Margin CRPS | 2025 | 306 | 7.0418 | 7.3449 | -0.3143 | -0.5303 | -0.0983 | 33 | BELOW_ZERO |
| Margin CRPS | ALL | 918 | 6.6681 | 6.9932 | -0.3390 | -0.4447 | -0.2332 | 98 | BELOW_ZERO |
| Total CRPS | 2023 | 306 | 9.6331 | 9.8344 | -0.1716 | -0.3486 | 0.0054 | 32 | SPANS_ZERO |
| Total CRPS | 2024 | 306 | 9.5094 | 9.6887 | -0.1846 | -0.3705 | 0.0014 | 33 | SPANS_ZERO |
| Total CRPS | 2025 | 306 | 9.6062 | 9.5231 | 0.1826 | -0.0620 | 0.4271 | 33 | SPANS_ZERO |
| Total CRPS | ALL | 918 | 9.5829 | 9.6821 | -0.0567 | -0.1760 | 0.0626 | 98 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 306 | 0.2456 | 0.2522 | -0.0054 | -0.0116 | 0.0008 | 32 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 306 | 0.2150 | 0.2193 | -0.0045 | -0.0122 | 0.0032 | 33 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 306 | 0.2150 | 0.2113 | 0.0059 | -0.0024 | 0.0142 | 33 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 918 | 0.2252 | 0.2276 | -0.0013 | -0.0056 | 0.0030 | 98 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0045; ECE 0.0443; logistic slope 1.332 (SE 0.116), intercept -0.153 (SE 0.087). Brier decomposition: reliability 0.0043, resolution 0.0432, uncertainty 0.2384.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 1 | 0.1811 | 0.0000 | 0.0000 | 0.7935 |
| [0.2, 0.3) | 32 | 0.2678 | 0.0938 | 0.0324 | 0.2422 |
| [0.3, 0.4) | 86 | 0.3555 | 0.3837 | 0.2880 | 0.4894 |
| [0.4, 0.5) | 104 | 0.4576 | 0.3173 | 0.2357 | 0.4119 |
| [0.5, 0.6) | 177 | 0.5481 | 0.5367 | 0.4633 | 0.6086 |
| [0.6, 0.7) | 216 | 0.6474 | 0.6806 | 0.6157 | 0.7391 |
| [0.7, 0.8) | 182 | 0.7463 | 0.7473 | 0.6795 | 0.8048 |
| [0.8, 0.9) | 110 | 0.8480 | 0.9182 | 0.8518 | 0.9564 |
| [0.9, 1.0] | 10 | 0.9212 | 1.0000 | 0.7225 | 1.0000 |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | -0.0889 | 1.6878 | 306 | 0.1928 | 0.1921 | -0.0013 | -0.0078 | 0.0053 | SPANS_ZERO |
| 2024 | -0.0762 | 1.3288 | 306 | 0.2001 | 0.1978 | -0.0023 | -0.0056 | 0.0011 | SPANS_ZERO |
| 2025 | -0.2297 | 1.4795 | 306 | 0.2042 | 0.2042 | -0.0017 | -0.0095 | 0.0061 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 180.0000 | 8.0000 | 1.1000 | 16.1765 | 612.0000 |
| 180.0000 | 8.0000 | 1.0000 | 16.1779 | 612.0000 |
| 90.0000 | 2.0000 | 1.1000 | 16.1879 | 612.0000 |
| 90.0000 | 2.0000 | 1.2000 | 16.1897 | 612.0000 |
| 180.0000 | 8.0000 | 1.2000 | 16.1914 | 612.0000 |
| 180.0000 | 2.0000 | 1.1000 | 16.1957 | 612.0000 |
| 90.0000 | 2.0000 | 1.0000 | 16.2027 | 612.0000 |
| 180.0000 | 2.0000 | 1.0000 | 16.2031 | 612.0000 |
| 180.0000 | 2.0000 | 1.2000 | 16.2048 | 612.0000 |
| 90.0000 | 2.0000 | 1.3000 | 16.2050 | 612.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:03:33Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-LIGA-ACB-JOINT-r1
- `archive_snapshot_sha256`: 406fb0bbfbf3bcb84b9d7e3a969ea0840ec523864a79b5f28ac5f2be3486594f
- `seconds`: 144

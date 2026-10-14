# Development results: `BSB-NPB-NB-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 853 | 0.2501 | 0.2516 | -0.0014 | -0.0045 | 0.0017 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 854 | 0.2485 | 0.2512 | -0.0019 | -0.0065 | 0.0027 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 858 | 0.2472 | 0.2513 | -0.0043 | -0.0083 | -0.0003 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 2565 | 0.2486 | 0.2514 | -0.0025 | -0.0047 | -0.0003 | 86 | BELOW_ZERO |
| Home-win log loss | 2023 | 853 | 0.6934 | 0.6964 | -0.0028 | -0.0091 | 0.0034 | 29 | SPANS_ZERO |
| Home-win log loss | 2024 | 854 | 0.6902 | 0.6956 | -0.0038 | -0.0131 | 0.0056 | 29 | SPANS_ZERO |
| Home-win log loss | 2025 | 858 | 0.6876 | 0.6957 | -0.0086 | -0.0168 | -0.0005 | 28 | BELOW_ZERO |
| Home-win log loss | ALL | 2565 | 0.6904 | 0.6959 | -0.0050 | -0.0095 | -0.0006 | 86 | BELOW_ZERO |
| Margin CRPS | 2023 | 853 | 2.0561 | 2.0560 | 0.0003 | -0.0151 | 0.0158 | 29 | SPANS_ZERO |
| Margin CRPS | 2024 | 854 | 2.1038 | 2.1203 | -0.0141 | -0.0351 | 0.0069 | 29 | SPANS_ZERO |
| Margin CRPS | 2025 | 858 | 2.0138 | 2.0465 | -0.0355 | -0.0548 | -0.0163 | 28 | BELOW_ZERO |
| Margin CRPS | ALL | 2565 | 2.0579 | 2.0742 | -0.0162 | -0.0270 | -0.0054 | 86 | BELOW_ZERO |
| Total CRPS | 2023 | 853 | 2.1003 | 2.1293 | -0.0285 | -0.0507 | -0.0063 | 29 | BELOW_ZERO |
| Total CRPS | 2024 | 854 | 2.0748 | 2.1334 | -0.0539 | -0.0903 | -0.0176 | 29 | BELOW_ZERO |
| Total CRPS | 2025 | 858 | 2.0601 | 2.0744 | -0.0155 | -0.0408 | 0.0098 | 28 | SPANS_ZERO |
| Total CRPS | ALL | 2565 | 2.0784 | 2.1123 | -0.0329 | -0.0491 | -0.0166 | 86 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 853 | 0.2396 | 0.2424 | -0.0025 | -0.0065 | 0.0015 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 854 | 0.2213 | 0.2290 | -0.0075 | -0.0133 | -0.0018 | 29 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 858 | 0.2488 | 0.2500 | -0.0018 | -0.0064 | 0.0029 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 2565 | 0.2366 | 0.2405 | -0.0040 | -0.0067 | -0.0012 | 86 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 853 | 0.2501 | 0.2493 | 0.0013 | -0.0004 | 0.0030 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 854 | 0.2485 | 0.2472 | 0.0014 | -0.0006 | 0.0033 | 29 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 858 | 0.2472 | 0.2459 | 0.0009 | -0.0025 | 0.0043 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 2565 | 0.2486 | 0.2475 | 0.0012 | -0.0001 | 0.0026 | 86 | SPANS_ZERO |
| Home-win log loss | 2023 | 853 | 0.6934 | 0.6918 | 0.0027 | -0.0008 | 0.0061 | 29 | SPANS_ZERO |
| Home-win log loss | 2024 | 854 | 0.6902 | 0.6876 | 0.0028 | -0.0011 | 0.0067 | 29 | SPANS_ZERO |
| Home-win log loss | 2025 | 858 | 0.6876 | 0.6848 | 0.0019 | -0.0050 | 0.0088 | 28 | SPANS_ZERO |
| Home-win log loss | ALL | 2565 | 0.6904 | 0.6881 | 0.0025 | -0.0003 | 0.0052 | 86 | SPANS_ZERO |
| Margin CRPS | 2023 | 853 | 2.0561 | 2.0756 | -0.0162 | -0.0310 | -0.0013 | 29 | BELOW_ZERO |
| Margin CRPS | 2024 | 854 | 2.1038 | 2.1131 | -0.0080 | -0.0167 | 0.0006 | 29 | SPANS_ZERO |
| Margin CRPS | 2025 | 858 | 2.0138 | 2.0345 | -0.0239 | -0.0361 | -0.0117 | 28 | BELOW_ZERO |
| Margin CRPS | ALL | 2565 | 2.0579 | 2.0743 | -0.0159 | -0.0228 | -0.0091 | 86 | BELOW_ZERO |
| Total CRPS | 2023 | 853 | 2.1003 | 2.1299 | -0.0326 | -0.0507 | -0.0145 | 29 | BELOW_ZERO |
| Total CRPS | 2024 | 854 | 2.0748 | 2.1074 | -0.0336 | -0.0501 | -0.0172 | 29 | BELOW_ZERO |
| Total CRPS | 2025 | 858 | 2.0601 | 2.0808 | -0.0211 | -0.0332 | -0.0090 | 28 | BELOW_ZERO |
| Total CRPS | ALL | 2565 | 2.0784 | 2.1060 | -0.0292 | -0.0380 | -0.0203 | 86 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 853 | 0.2396 | 0.2417 | -0.0029 | -0.0061 | 0.0002 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 854 | 0.2213 | 0.2237 | -0.0040 | -0.0080 | 0.0000 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 858 | 0.2488 | 0.2490 | -0.0006 | -0.0034 | 0.0023 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 2565 | 0.2366 | 0.2382 | -0.0025 | -0.0044 | -0.0006 | 86 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0414; ECE 0.0436; logistic slope 0.960 (SE 0.200), intercept 0.165 (SE 0.041). Brier decomposition: reliability 0.0022, resolution 0.0011, uncertainty 0.2492.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 0 | — | — | — | — |
| [0.3, 0.4) | 101 | 0.3832 | 0.5050 | 0.4091 | 0.6005 |
| [0.4, 0.5) | 1437 | 0.4605 | 0.5017 | 0.4759 | 0.5276 |
| [0.5, 0.6) | 992 | 0.5317 | 0.5696 | 0.5385 | 0.6000 |
| [0.6, 0.7) | 35 | 0.6221 | 0.5429 | 0.3819 | 0.6953 |
| [0.7, 0.8) | 0 | — | — | — | — |
| [0.8, 0.9) | 0 | — | — | — | — |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.0775 | 0.1797 | 853 | 0.2501 | 0.2487 | -0.0019 | -0.0047 | 0.0010 | SPANS_ZERO |
| 2024 | 0.1859 | 0.8309 | 854 | 0.2485 | 0.2477 | -0.0010 | -0.0045 | 0.0025 | SPANS_ZERO |
| 2025 | 0.1300 | 0.9008 | 858 | 0.2472 | 0.2456 | -0.0016 | -0.0047 | 0.0016 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 90.0000 | 128.0000 | 4.4449 | 1645.0000 |
| 180.0000 | 128.0000 | 4.4473 | 1645.0000 |
| 90.0000 | 64.0000 | 4.4490 | 1645.0000 |
| 180.0000 | 64.0000 | 4.4493 | 1645.0000 |
| 180.0000 | 32.0000 | 4.4514 | 1645.0000 |
| 45.0000 | 128.0000 | 4.4529 | 1645.0000 |
| 180.0000 | 16.0000 | 4.4530 | 1645.0000 |
| 90.0000 | 32.0000 | 4.4542 | 1645.0000 |
| 180.0000 | 4.0000 | 4.4548 | 1645.0000 |
| 180.0000 | 1.0000 | 4.4555 | 1645.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:01:37Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-NPB-NB-r1
- `archive_snapshot_sha256`: aa092627e3ea25c966cb025017aee11e6bcd7a15fcc243399fc83e5be38faa18
- `seconds`: 148

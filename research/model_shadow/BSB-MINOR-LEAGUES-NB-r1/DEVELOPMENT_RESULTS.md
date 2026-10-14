# Development results: `BSB-MINOR-LEAGUES-NB-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 2157 | 0.2475 | 0.2501 | -0.0009 | -0.0047 | 0.0029 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 2160 | 0.2502 | 0.2501 | 0.0006 | -0.0021 | 0.0034 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 2151 | 0.2486 | 0.2500 | -0.0013 | -0.0034 | 0.0008 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 6468 | 0.2488 | 0.2501 | -0.0005 | -0.0022 | 0.0011 | 81 | SPANS_ZERO |
| Home-win log loss | 2023 | 2157 | 0.6882 | 0.6934 | -0.0018 | -0.0094 | 0.0057 | 27 | SPANS_ZERO |
| Home-win log loss | 2024 | 2160 | 0.6937 | 0.6933 | 0.0013 | -0.0042 | 0.0068 | 27 | SPANS_ZERO |
| Home-win log loss | 2025 | 2151 | 0.6903 | 0.6931 | -0.0026 | -0.0068 | 0.0016 | 27 | SPANS_ZERO |
| Home-win log loss | ALL | 6468 | 0.6907 | 0.6933 | -0.0010 | -0.0043 | 0.0022 | 81 | SPANS_ZERO |
| Margin CRPS | 2023 | 2157 | 2.7233 | 2.7405 | -0.0132 | -0.0312 | 0.0048 | 27 | SPANS_ZERO |
| Margin CRPS | 2024 | 2160 | 2.6790 | 2.6775 | 0.0098 | -0.0165 | 0.0361 | 27 | SPANS_ZERO |
| Margin CRPS | 2025 | 2151 | 2.6962 | 2.7048 | -0.0099 | -0.0222 | 0.0025 | 27 | SPANS_ZERO |
| Margin CRPS | ALL | 6468 | 2.6995 | 2.7076 | -0.0044 | -0.0156 | 0.0067 | 81 | SPANS_ZERO |
| Total CRPS | 2023 | 2157 | 3.0316 | 3.0656 | -0.0319 | -0.0689 | 0.0051 | 27 | SPANS_ZERO |
| Total CRPS | 2024 | 2160 | 2.8720 | 2.8906 | 0.0062 | -0.0519 | 0.0643 | 27 | SPANS_ZERO |
| Total CRPS | 2025 | 2151 | 2.7889 | 2.8709 | -0.0692 | -0.1016 | -0.0367 | 27 | BELOW_ZERO |
| Total CRPS | ALL | 6468 | 2.8976 | 2.9424 | -0.0316 | -0.0568 | -0.0064 | 81 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 2157 | 0.2490 | 0.2518 | -0.0024 | -0.0071 | 0.0023 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 2160 | 0.2475 | 0.2495 | -0.0000 | -0.0054 | 0.0053 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 2151 | 0.2405 | 0.2494 | -0.0076 | -0.0112 | -0.0040 | 27 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 6468 | 0.2457 | 0.2502 | -0.0033 | -0.0060 | -0.0007 | 81 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 2157 | 0.2475 | 0.2490 | 0.0008 | -0.0036 | 0.0051 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 2160 | 0.2502 | 0.2490 | 0.0020 | -0.0003 | 0.0043 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 2151 | 0.2486 | 0.2488 | -0.0008 | -0.0027 | 0.0010 | 27 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 6468 | 0.2488 | 0.2490 | 0.0006 | -0.0011 | 0.0023 | 81 | SPANS_ZERO |
| Home-win log loss | 2023 | 2157 | 0.6882 | 0.6912 | 0.0015 | -0.0072 | 0.0102 | 27 | SPANS_ZERO |
| Home-win log loss | 2024 | 2160 | 0.6937 | 0.6912 | 0.0040 | -0.0006 | 0.0087 | 27 | SPANS_ZERO |
| Home-win log loss | 2025 | 2151 | 0.6903 | 0.6907 | -0.0017 | -0.0054 | 0.0020 | 27 | SPANS_ZERO |
| Home-win log loss | ALL | 6468 | 0.6907 | 0.6910 | 0.0013 | -0.0021 | 0.0047 | 81 | SPANS_ZERO |
| Margin CRPS | 2023 | 2157 | 2.7233 | 2.7364 | -0.0087 | -0.0216 | 0.0043 | 27 | SPANS_ZERO |
| Margin CRPS | 2024 | 2160 | 2.6790 | 2.6869 | 0.0063 | -0.0276 | 0.0401 | 27 | SPANS_ZERO |
| Margin CRPS | 2025 | 2151 | 2.6962 | 2.7057 | -0.0138 | -0.0256 | -0.0020 | 27 | BELOW_ZERO |
| Margin CRPS | ALL | 6468 | 2.6995 | 2.7096 | -0.0054 | -0.0177 | 0.0069 | 81 | SPANS_ZERO |
| Total CRPS | 2023 | 2157 | 3.0316 | 3.0626 | -0.0242 | -0.0709 | 0.0225 | 27 | SPANS_ZERO |
| Total CRPS | 2024 | 2160 | 2.8720 | 2.9118 | -0.0206 | -0.0709 | 0.0297 | 27 | SPANS_ZERO |
| Total CRPS | 2025 | 2151 | 2.7889 | 2.8251 | -0.0262 | -0.0515 | -0.0008 | 27 | BELOW_ZERO |
| Total CRPS | ALL | 6468 | 2.8976 | 2.9333 | -0.0237 | -0.0470 | -0.0003 | 81 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 2157 | 0.2490 | 0.2532 | -0.0022 | -0.0098 | 0.0054 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 2160 | 0.2475 | 0.2514 | -0.0023 | -0.0078 | 0.0031 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 2151 | 0.2405 | 0.2435 | -0.0018 | -0.0049 | 0.0012 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 6468 | 0.2457 | 0.2494 | -0.0021 | -0.0052 | 0.0010 | 81 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0266; ECE 0.0329; logistic slope 0.765 (SE 0.131), intercept 0.107 (SE 0.025). Brier decomposition: reliability 0.0013, resolution 0.0013, uncertainty 0.2493.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 0 | — | — | — | — |
| [0.3, 0.4) | 112 | 0.3832 | 0.3482 | 0.2663 | 0.4401 |
| [0.4, 0.5) | 3018 | 0.4642 | 0.5023 | 0.4845 | 0.5201 |
| [0.5, 0.6) | 3193 | 0.5335 | 0.5578 | 0.5405 | 0.5749 |
| [0.6, 0.7) | 145 | 0.6174 | 0.5034 | 0.4230 | 0.5837 |
| [0.7, 0.8) | 0 | — | — | — | — |
| [0.8, 0.9) | 0 | — | — | — | — |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.1111 | 0.8314 | 2157 | 0.2475 | 0.2465 | 0.0000 | -0.0022 | 0.0022 | SPANS_ZERO |
| 2024 | 0.1324 | 0.9604 | 2160 | 0.2502 | 0.2496 | -0.0018 | -0.0047 | 0.0011 | SPANS_ZERO |
| 2025 | 0.1023 | 0.4168 | 2151 | 0.2486 | 0.2485 | -0.0011 | -0.0040 | 0.0018 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 365.0000 | 128.0000 | 5.4366 | 4025.0000 |
| 180.0000 | 128.0000 | 5.4395 | 4025.0000 |
| 730.0000 | 128.0000 | 5.4397 | 4025.0000 |
| 365.0000 | 64.0000 | 5.4405 | 4025.0000 |
| 730.0000 | 64.0000 | 5.4430 | 4025.0000 |
| 365.0000 | 32.0000 | 5.4444 | 4025.0000 |
| 180.0000 | 64.0000 | 5.4459 | 4025.0000 |
| 730.0000 | 32.0000 | 5.4461 | 4025.0000 |
| 90.0000 | 128.0000 | 5.4467 | 4025.0000 |
| 365.0000 | 16.0000 | 5.4477 | 4025.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:04:14Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-MINOR-LEAGUES-NB-r1
- `archive_snapshot_sha256`: f0df08d6dce87a1350a9c713e15fb9e612766fa2745888de63757074b460eafd
- `seconds`: 304

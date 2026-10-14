# Development results: `BSB-MLB-NB-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2024, 2025, 2026]; hyperparameters chosen on [2022, 2023] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2024 | 2429 | 0.2440 | 0.2499 | -0.0055 | -0.0077 | -0.0033 | 29 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 2430 | 0.2442 | 0.2500 | -0.0068 | -0.0108 | -0.0028 | 28 | BELOW_ZERO |
| Home-win Brier (primary) | 2026 | 2429 | 0.2456 | 0.2500 | -0.0047 | -0.0073 | -0.0020 | 27 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 7288 | 0.2446 | 0.2499 | -0.0057 | -0.0074 | -0.0040 | 84 | BELOW_ZERO |
| Home-win log loss | 2024 | 2429 | 0.6811 | 0.6929 | -0.0111 | -0.0155 | -0.0067 | 29 | BELOW_ZERO |
| Home-win log loss | 2025 | 2430 | 0.6814 | 0.6931 | -0.0138 | -0.0219 | -0.0057 | 28 | BELOW_ZERO |
| Home-win log loss | 2026 | 2429 | 0.6843 | 0.6931 | -0.0094 | -0.0148 | -0.0041 | 27 | BELOW_ZERO |
| Home-win log loss | ALL | 7288 | 0.6823 | 0.6930 | -0.0115 | -0.0149 | -0.0080 | 84 | BELOW_ZERO |
| Margin CRPS | 2024 | 2429 | 2.4209 | 2.4605 | -0.0383 | -0.0527 | -0.0239 | 29 | BELOW_ZERO |
| Margin CRPS | 2025 | 2430 | 2.4864 | 2.5273 | -0.0455 | -0.0695 | -0.0216 | 28 | BELOW_ZERO |
| Margin CRPS | 2026 | 2429 | 2.4835 | 2.5079 | -0.0263 | -0.0429 | -0.0096 | 27 | BELOW_ZERO |
| Margin CRPS | ALL | 7288 | 2.4636 | 2.4986 | -0.0369 | -0.0474 | -0.0263 | 84 | BELOW_ZERO |
| Total CRPS | 2024 | 2429 | 2.3906 | 2.3943 | -0.0011 | -0.0140 | 0.0117 | 29 | SPANS_ZERO |
| Total CRPS | 2025 | 2430 | 2.5227 | 2.5341 | -0.0046 | -0.0250 | 0.0158 | 28 | SPANS_ZERO |
| Total CRPS | 2026 | 2429 | 2.4922 | 2.5019 | -0.0093 | -0.0193 | 0.0007 | 27 | SPANS_ZERO |
| Total CRPS | ALL | 7288 | 2.4685 | 2.4768 | -0.0049 | -0.0133 | 0.0035 | 84 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 2429 | 0.2499 | 0.2501 | -0.0003 | -0.0023 | 0.0018 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 2430 | 0.2498 | 0.2499 | 0.0001 | -0.0021 | 0.0023 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2026 | 2429 | 0.2495 | 0.2502 | -0.0006 | -0.0021 | 0.0009 | 27 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 7288 | 0.2498 | 0.2501 | -0.0003 | -0.0014 | 0.0008 | 84 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2024 | 2429 | 0.2440 | 0.2456 | -0.0018 | -0.0035 | -0.0001 | 29 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 2430 | 0.2442 | 0.2463 | -0.0036 | -0.0075 | 0.0003 | 28 | SPANS_ZERO |
| Home-win Brier (primary) | 2026 | 2429 | 0.2456 | 0.2474 | -0.0020 | -0.0036 | -0.0005 | 27 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 7288 | 0.2446 | 0.2464 | -0.0025 | -0.0039 | -0.0010 | 84 | BELOW_ZERO |
| Home-win log loss | 2024 | 2429 | 0.6811 | 0.6844 | -0.0036 | -0.0070 | -0.0002 | 29 | BELOW_ZERO |
| Home-win log loss | 2025 | 2430 | 0.6814 | 0.6857 | -0.0073 | -0.0152 | 0.0005 | 28 | SPANS_ZERO |
| Home-win log loss | 2026 | 2429 | 0.6843 | 0.6879 | -0.0042 | -0.0074 | -0.0010 | 27 | BELOW_ZERO |
| Home-win log loss | ALL | 7288 | 0.6823 | 0.6860 | -0.0050 | -0.0080 | -0.0021 | 84 | BELOW_ZERO |
| Margin CRPS | 2024 | 2429 | 2.4209 | 2.4435 | -0.0251 | -0.0376 | -0.0126 | 29 | BELOW_ZERO |
| Margin CRPS | 2025 | 2430 | 2.4864 | 2.5137 | -0.0353 | -0.0578 | -0.0128 | 28 | BELOW_ZERO |
| Margin CRPS | 2026 | 2429 | 2.4835 | 2.5056 | -0.0235 | -0.0343 | -0.0127 | 27 | BELOW_ZERO |
| Margin CRPS | ALL | 7288 | 2.4636 | 2.4876 | -0.0280 | -0.0370 | -0.0190 | 84 | BELOW_ZERO |
| Total CRPS | 2024 | 2429 | 2.3906 | 2.4772 | -0.1141 | -0.3011 | 0.0728 | 29 | SPANS_ZERO |
| Total CRPS | 2025 | 2430 | 2.5227 | 2.5468 | -0.0211 | -0.0338 | -0.0085 | 28 | BELOW_ZERO |
| Total CRPS | 2026 | 2429 | 2.4922 | 2.5143 | -0.0218 | -0.0305 | -0.0131 | 27 | BELOW_ZERO |
| Total CRPS | ALL | 7288 | 2.4685 | 2.5128 | -0.0534 | -0.1163 | 0.0094 | 84 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 2429 | 0.2499 | 0.2541 | -0.0054 | -0.0122 | 0.0014 | 29 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 2430 | 0.2498 | 0.2510 | -0.0009 | -0.0028 | 0.0009 | 28 | SPANS_ZERO |
| Over the league-median line, Brier | 2026 | 2429 | 0.2495 | 0.2517 | -0.0023 | -0.0042 | -0.0005 | 27 | BELOW_ZERO |
| Over the league-median line, Brier | ALL | 7288 | 0.2498 | 0.2523 | -0.0029 | -0.0053 | -0.0005 | 84 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0297; ECE 0.0297; logistic slope 1.143 (SE 0.092), intercept 0.121 (SE 0.024). Brier decomposition: reliability 0.0010, resolution 0.0048, uncertainty 0.2490.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 0 | — | — | — | — |
| [0.3, 0.4) | 473 | 0.3726 | 0.3805 | 0.3379 | 0.4251 |
| [0.4, 0.5) | 3089 | 0.4605 | 0.4862 | 0.4686 | 0.5039 |
| [0.5, 0.6) | 3229 | 0.5399 | 0.5714 | 0.5542 | 0.5884 |
| [0.6, 0.7) | 497 | 0.6265 | 0.6901 | 0.6482 | 0.7292 |
| [0.7, 0.8) | 0 | — | — | — | — |
| [0.8, 0.9) | 0 | — | — | — | — |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2024 | 0.0786 | 1.0341 | 2429 | 0.2440 | 0.2434 | 0.0002 | -0.0014 | 0.0018 | SPANS_ZERO |
| 2025 | 0.1030 | 1.1579 | 2430 | 0.2442 | 0.2428 | -0.0008 | -0.0027 | 0.0010 | SPANS_ZERO |
| 2026 | 0.1622 | 1.1279 | 2429 | 0.2456 | 0.2452 | -0.0005 | -0.0021 | 0.0010 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 180.0000 | 128.0000 | 4.8970 | 4860.0000 |
| 90.0000 | 128.0000 | 4.8971 | 4860.0000 |
| 180.0000 | 64.0000 | 4.8983 | 4860.0000 |
| 90.0000 | 64.0000 | 4.8996 | 4860.0000 |
| 180.0000 | 32.0000 | 4.9000 | 4860.0000 |
| 180.0000 | 16.0000 | 4.9011 | 4860.0000 |
| 180.0000 | 4.0000 | 4.9022 | 4860.0000 |
| 180.0000 | 1.0000 | 4.9025 | 4860.0000 |
| 90.0000 | 32.0000 | 4.9038 | 4860.0000 |
| 365.0000 | 128.0000 | 4.9044 | 4860.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:05:02Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-MLB-NB-r1
- `archive_snapshot_sha256`: f63cc6ebac4b4dc987a6598e915bc30f08644bbef87b142aa39bce2b0f38f667
- `seconds`: 353

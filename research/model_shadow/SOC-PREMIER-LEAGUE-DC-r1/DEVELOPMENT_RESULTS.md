# Development results: `SOC-PREMIER-LEAGUE-DC-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `BELOW_ZERO_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 380 | 0.2100 | 0.2497 | -0.0393 | -0.0575 | -0.0211 | 37 | BELOW_ZERO |
| Home-win Brier (primary) | 2024 | 380 | 0.2098 | 0.2429 | -0.0359 | -0.0494 | -0.0224 | 36 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 380 | 0.2232 | 0.2449 | -0.0212 | -0.0327 | -0.0098 | 36 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 1140 | 0.2143 | 0.2458 | -0.0322 | -0.0406 | -0.0238 | 109 | BELOW_ZERO |
| Home-win log loss | 2023 | 380 | 0.6064 | 0.6926 | -0.0851 | -0.1237 | -0.0465 | 37 | BELOW_ZERO |
| Home-win log loss | 2024 | 380 | 0.6059 | 0.6788 | -0.0780 | -0.1068 | -0.0492 | 36 | BELOW_ZERO |
| Home-win log loss | 2025 | 380 | 0.6360 | 0.6829 | -0.0460 | -0.0707 | -0.0213 | 36 | BELOW_ZERO |
| Home-win log loss | ALL | 1140 | 0.6161 | 0.6848 | -0.0698 | -0.0877 | -0.0520 | 109 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 380 | 0.2798 | 0.3196 | -0.0389 | -0.0536 | -0.0242 | 37 | BELOW_ZERO |
| Three-way half-sum Brier | 2024 | 380 | 0.2954 | 0.3276 | -0.0351 | -0.0468 | -0.0233 | 36 | BELOW_ZERO |
| Three-way half-sum Brier | 2025 | 380 | 0.3093 | 0.3275 | -0.0180 | -0.0297 | -0.0064 | 36 | BELOW_ZERO |
| Three-way half-sum Brier | ALL | 1140 | 0.2948 | 0.3249 | -0.0307 | -0.0381 | -0.0234 | 109 | BELOW_ZERO |
| Margin CRPS | 2023 | 380 | 1.0074 | 1.1442 | -0.1412 | -0.1909 | -0.0915 | 37 | BELOW_ZERO |
| Margin CRPS | 2024 | 380 | 0.9285 | 1.0327 | -0.1054 | -0.1421 | -0.0687 | 36 | BELOW_ZERO |
| Margin CRPS | 2025 | 380 | 0.8441 | 0.8991 | -0.0563 | -0.0880 | -0.0246 | 36 | BELOW_ZERO |
| Margin CRPS | ALL | 1140 | 0.9267 | 1.0253 | -0.1013 | -0.1248 | -0.0778 | 109 | BELOW_ZERO |
| Total CRPS | 2023 | 380 | 0.9473 | 0.9621 | -0.0150 | -0.0353 | 0.0053 | 37 | SPANS_ZERO |
| Total CRPS | 2024 | 380 | 0.8920 | 0.8912 | 0.0036 | -0.0146 | 0.0219 | 36 | SPANS_ZERO |
| Total CRPS | 2025 | 380 | 0.8788 | 0.8722 | 0.0055 | -0.0100 | 0.0210 | 36 | SPANS_ZERO |
| Total CRPS | ALL | 1140 | 0.9061 | 0.9085 | -0.0021 | -0.0124 | 0.0082 | 109 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 380 | 0.2546 | 0.2600 | -0.0053 | -0.0118 | 0.0012 | 37 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 380 | 0.2266 | 0.2252 | 0.0028 | -0.0044 | 0.0100 | 36 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 380 | 0.2102 | 0.2078 | 0.0026 | -0.0031 | 0.0083 | 36 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 1140 | 0.2305 | 0.2310 | 0.0000 | -0.0037 | 0.0037 | 109 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 380 | 0.2100 | 0.2199 | -0.0096 | -0.0199 | 0.0007 | 37 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 380 | 0.2098 | 0.2212 | -0.0102 | -0.0189 | -0.0016 | 36 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 380 | 0.2232 | 0.2297 | -0.0065 | -0.0138 | 0.0007 | 36 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 1140 | 0.2143 | 0.2236 | -0.0088 | -0.0137 | -0.0038 | 109 | BELOW_ZERO |
| Home-win log loss | 2023 | 380 | 0.6064 | 0.6305 | -0.0233 | -0.0453 | -0.0014 | 37 | BELOW_ZERO |
| Home-win log loss | 2024 | 380 | 0.6059 | 0.6326 | -0.0237 | -0.0428 | -0.0045 | 36 | BELOW_ZERO |
| Home-win log loss | 2025 | 380 | 0.6360 | 0.6509 | -0.0151 | -0.0308 | 0.0007 | 36 | SPANS_ZERO |
| Home-win log loss | ALL | 1140 | 0.6161 | 0.6380 | -0.0207 | -0.0314 | -0.0100 | 109 | BELOW_ZERO |
| Three-way half-sum Brier | 2023 | 380 | 0.2798 | 0.2904 | -0.0109 | -0.0190 | -0.0028 | 37 | BELOW_ZERO |
| Three-way half-sum Brier | 2024 | 380 | 0.2954 | 0.3056 | -0.0088 | -0.0173 | -0.0003 | 36 | BELOW_ZERO |
| Three-way half-sum Brier | 2025 | 380 | 0.3093 | 0.3137 | -0.0048 | -0.0114 | 0.0019 | 36 | SPANS_ZERO |
| Three-way half-sum Brier | ALL | 1140 | 0.2948 | 0.3032 | -0.0082 | -0.0126 | -0.0038 | 109 | BELOW_ZERO |
| Margin CRPS | 2023 | 380 | 1.0074 | 1.0400 | -0.0369 | -0.0640 | -0.0098 | 37 | BELOW_ZERO |
| Margin CRPS | 2024 | 380 | 0.9285 | 0.9634 | -0.0274 | -0.0560 | 0.0012 | 36 | SPANS_ZERO |
| Margin CRPS | 2025 | 380 | 0.8441 | 0.8588 | -0.0167 | -0.0385 | 0.0052 | 36 | SPANS_ZERO |
| Margin CRPS | ALL | 1140 | 0.9267 | 0.9541 | -0.0271 | -0.0417 | -0.0124 | 109 | BELOW_ZERO |
| Total CRPS | 2023 | 380 | 0.9473 | 0.9359 | -0.0031 | -0.0360 | 0.0298 | 37 | SPANS_ZERO |
| Total CRPS | 2024 | 380 | 0.8920 | 0.9064 | -0.0121 | -0.0321 | 0.0078 | 36 | SPANS_ZERO |
| Total CRPS | 2025 | 380 | 0.8788 | 0.8835 | -0.0044 | -0.0242 | 0.0154 | 36 | SPANS_ZERO |
| Total CRPS | ALL | 1140 | 0.9061 | 0.9086 | -0.0065 | -0.0206 | 0.0076 | 109 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 380 | 0.2546 | 0.2489 | 0.0029 | -0.0065 | 0.0123 | 37 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 380 | 0.2266 | 0.2313 | -0.0049 | -0.0127 | 0.0029 | 36 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 380 | 0.2102 | 0.2078 | 0.0028 | -0.0038 | 0.0095 | 36 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 1140 | 0.2305 | 0.2293 | 0.0003 | -0.0042 | 0.0048 | 109 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0003; ECE 0.0398; logistic slope 1.243 (SE 0.109), intercept 0.059 (SE 0.070). Brier decomposition: reliability 0.0024, resolution 0.0323, uncertainty 0.2453.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 3 | 0.0901 | 0.0000 | 0.0000 | 0.5615 |
| [0.1, 0.2) | 60 | 0.1662 | 0.1167 | 0.0577 | 0.2218 |
| [0.2, 0.3) | 165 | 0.2534 | 0.1939 | 0.1409 | 0.2609 |
| [0.3, 0.4) | 272 | 0.3518 | 0.3640 | 0.3091 | 0.4227 |
| [0.4, 0.5) | 286 | 0.4483 | 0.4336 | 0.3774 | 0.4915 |
| [0.5, 0.6) | 178 | 0.5479 | 0.6292 | 0.5562 | 0.6967 |
| [0.6, 0.7) | 116 | 0.6345 | 0.5862 | 0.4952 | 0.6717 |
| [0.7, 0.8) | 50 | 0.7375 | 0.8000 | 0.6696 | 0.8876 |
| [0.8, 0.9) | 10 | 0.8421 | 1.0000 | 0.7225 | 1.0000 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only

Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.

| season | intercept | slope | n | uncalibrated | calibrated | mean | lo | hi | status |
|---|---|---|---|---|---|---|---|---|---|
| 2023 | 0.2275 | 0.9843 | 380 | 0.2100 | 0.2098 | 0.0017 | -0.0045 | 0.0079 | SPANS_ZERO |
| 2024 | 0.2120 | 1.3818 | 380 | 0.2098 | 0.2124 | 0.0010 | -0.0051 | 0.0072 | SPANS_ZERO |
| 2025 | -0.0899 | 1.2034 | 380 | 0.2232 | 0.2245 | 0.0017 | -0.0018 | 0.0052 | SPANS_ZERO |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 365.0000 | 16.0000 | 1.8875 | 760.0000 |
| 365.0000 | 4.0000 | 1.8884 | 760.0000 |
| 180.0000 | 4.0000 | 1.8898 | 760.0000 |
| 730.0000 | 16.0000 | 1.8899 | 760.0000 |
| 180.0000 | 16.0000 | 1.8908 | 760.0000 |
| 730.0000 | 4.0000 | 1.8921 | 760.0000 |
| 365.0000 | 1.0000 | 1.8931 | 760.0000 |
| 730.0000 | 32.0000 | 1.8933 | 760.0000 |
| 365.0000 | 32.0000 | 1.8950 | 760.0000 |
| 730.0000 | 1.0000 | 1.8962 | 760.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:05:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: SOC-PREMIER-LEAGUE-DC-r1
- `archive_snapshot_sha256`: 042634114d6d7a64619ab41fd5c28d9b544503d9e2319d41783a91e477e956d2
- `seconds`: 128

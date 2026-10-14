# Development results: `IH-DANISH-METAL-LIGAEN-REG-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 192 | 0.1942 | 0.1935 | 0.0007 | -0.0116 | 0.0130 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 192 | 0.1893 | 0.1939 | -0.0046 | -0.0134 | 0.0043 | 25 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 192 | 0.1871 | 0.1873 | -0.0034 | -0.0172 | 0.0104 | 25 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 576 | 0.1902 | 0.1916 | -0.0024 | -0.0090 | 0.0041 | 74 | SPANS_ZERO |
| Home-win log loss | 2023 | 192 | 0.5755 | 0.5762 | -0.0007 | -0.0291 | 0.0277 | 24 | SPANS_ZERO |
| Home-win log loss | 2024 | 192 | 0.5645 | 0.5773 | -0.0120 | -0.0318 | 0.0077 | 25 | SPANS_ZERO |
| Home-win log loss | 2025 | 192 | 0.5604 | 0.5636 | -0.0098 | -0.0406 | 0.0209 | 25 | SPANS_ZERO |
| Home-win log loss | ALL | 576 | 0.5668 | 0.5723 | -0.0076 | -0.0223 | 0.0071 | 74 | SPANS_ZERO |
| Margin CRPS | 2023 | 192 | 0.9679 | 0.9980 | -0.0301 | -0.0794 | 0.0192 | 24 | SPANS_ZERO |
| Margin CRPS | 2024 | 192 | 0.9654 | 1.0145 | -0.0467 | -0.0800 | -0.0134 | 25 | BELOW_ZERO |
| Margin CRPS | 2025 | 192 | 0.9499 | 0.9778 | -0.0389 | -0.0933 | 0.0155 | 25 | SPANS_ZERO |
| Margin CRPS | ALL | 576 | 0.9610 | 0.9968 | -0.0387 | -0.0643 | -0.0131 | 74 | BELOW_ZERO |
| Total CRPS | 2023 | 192 | 1.1174 | 1.1095 | 0.0079 | -0.0069 | 0.0226 | 24 | SPANS_ZERO |
| Total CRPS | 2024 | 192 | 1.1562 | 1.1417 | 0.0124 | -0.0028 | 0.0276 | 25 | SPANS_ZERO |
| Total CRPS | 2025 | 192 | 1.2003 | 1.1917 | 0.0089 | -0.0037 | 0.0214 | 25 | SPANS_ZERO |
| Total CRPS | ALL | 576 | 1.1580 | 1.1476 | 0.0097 | 0.0019 | 0.0175 | 74 | ABOVE_ZERO |
| Over the league-median line, Brier | 2023 | 192 | 0.2177 | 0.2153 | 0.0024 | -0.0021 | 0.0070 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 192 | 0.2142 | 0.2113 | 0.0023 | -0.0025 | 0.0070 | 25 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 192 | 0.2166 | 0.2149 | 0.0017 | -0.0012 | 0.0046 | 25 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 576 | 0.2162 | 0.2139 | 0.0021 | -0.0002 | 0.0044 | 74 | SPANS_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 192 | 0.1942 | 0.1923 | 0.0018 | -0.0162 | 0.0199 | 24 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 192 | 0.1893 | 0.1872 | 0.0023 | -0.0150 | 0.0196 | 25 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 192 | 0.1871 | 0.1759 | 0.0070 | -0.0120 | 0.0261 | 25 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 576 | 0.1902 | 0.1851 | 0.0038 | -0.0062 | 0.0138 | 74 | SPANS_ZERO |
| Home-win log loss | 2023 | 192 | 0.5755 | 0.5743 | 0.0011 | -0.0421 | 0.0443 | 24 | SPANS_ZERO |
| Home-win log loss | 2024 | 192 | 0.5645 | 0.5595 | 0.0060 | -0.0339 | 0.0459 | 25 | SPANS_ZERO |
| Home-win log loss | 2025 | 192 | 0.5604 | 0.5349 | 0.0163 | -0.0274 | 0.0599 | 25 | SPANS_ZERO |
| Home-win log loss | ALL | 576 | 0.5668 | 0.5563 | 0.0079 | -0.0154 | 0.0312 | 74 | SPANS_ZERO |
| Margin CRPS | 2023 | 192 | 0.9679 | 0.9749 | -0.0070 | -0.0576 | 0.0436 | 24 | SPANS_ZERO |
| Margin CRPS | 2024 | 192 | 0.9654 | 0.9823 | -0.0132 | -0.0516 | 0.0252 | 25 | SPANS_ZERO |
| Margin CRPS | 2025 | 192 | 0.9499 | 0.9436 | -0.0060 | -0.0696 | 0.0577 | 25 | SPANS_ZERO |
| Margin CRPS | ALL | 576 | 0.9610 | 0.9669 | -0.0088 | -0.0373 | 0.0198 | 74 | SPANS_ZERO |
| Total CRPS | 2023 | 192 | 1.1174 | 1.1186 | -0.0012 | -0.0634 | 0.0610 | 24 | SPANS_ZERO |
| Total CRPS | 2024 | 192 | 1.1562 | 1.1541 | 0.0067 | -0.0473 | 0.0608 | 25 | SPANS_ZERO |
| Total CRPS | 2025 | 192 | 1.2003 | 1.2197 | -0.0195 | -0.0801 | 0.0412 | 25 | SPANS_ZERO |
| Total CRPS | ALL | 576 | 1.1580 | 1.1641 | -0.0047 | -0.0372 | 0.0278 | 74 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 192 | 0.2177 | 0.2341 | -0.0163 | -0.0361 | 0.0034 | 24 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 192 | 0.2142 | 0.2245 | -0.0084 | -0.0230 | 0.0063 | 25 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 192 | 0.2166 | 0.2305 | -0.0146 | -0.0327 | 0.0034 | 25 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 576 | 0.2162 | 0.2297 | -0.0131 | -0.0227 | -0.0034 | 74 | BELOW_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large -0.0760; ECE 0.0760; logistic slope 0.745 (SE 0.235), intercept 0.563 (SE 0.191). Brier decomposition: reliability 0.0078, resolution 0.0038, uncertainty 0.1866.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 0 | — | — | — | — |
| [0.3, 0.4) | 0 | — | — | — | — |
| [0.4, 0.5) | 10 | 0.4887 | 0.5000 | 0.2366 | 0.7634 |
| [0.5, 0.6) | 124 | 0.5559 | 0.7097 | 0.6244 | 0.7823 |
| [0.6, 0.7) | 181 | 0.6497 | 0.7072 | 0.6371 | 0.7686 |
| [0.7, 0.8) | 212 | 0.7445 | 0.8113 | 0.7533 | 0.8583 |
| [0.8, 0.9) | 49 | 0.8160 | 0.8163 | 0.6864 | 0.9002 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | objective | n |
|---|---|---|---|
| 730.0000 | 0.1250 | 2.0418 | 384.0000 |
| 730.0000 | 0.2500 | 2.0418 | 384.0000 |
| 730.0000 | 0.5000 | 2.0418 | 384.0000 |
| 730.0000 | 1.0000 | 2.0419 | 384.0000 |
| 730.0000 | 4.0000 | 2.0419 | 384.0000 |
| 730.0000 | 16.0000 | 2.0422 | 384.0000 |
| 1460.0000 | 0.1250 | 2.0423 | 384.0000 |
| 1460.0000 | 0.2500 | 2.0423 | 384.0000 |
| 1460.0000 | 0.5000 | 2.0423 | 384.0000 |
| 1460.0000 | 1.0000 | 2.0423 | 384.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:03:55Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: IH-DANISH-METAL-LIGAEN-REG-r1
- `archive_snapshot_sha256`: e89e937ee34807d28071cb84dbe658154778eb8f758183d0482583fd50d5310a
- `seconds`: 70

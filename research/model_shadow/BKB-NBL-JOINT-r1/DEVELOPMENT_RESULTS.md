# Development results: `BKB-NBL-JOINT-r1`

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).

**Verdict:** `FAIL_DEVELOPMENT`. Against BASELINE_LEAGUE_V1: `NOT_EVERY_SEASON`. Against TB-1: `NOT_EVERY_SEASON`. Rule: the primary metric (home-win Brier) must have a 95% week-block interval below 0 against both comparators in every test season (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).

Test seasons [2023, 2024, 2025]; hyperparameters chosen on [2021, 2022] only; differences are candidate − comparator (negative favours the model); each interval is a t-interval over ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).

## Against BASELINE_LEAGUE_V1

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 140 | 0.2416 | 0.2444 | -0.0056 | -0.0244 | 0.0131 | 20 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 145 | 0.2312 | 0.2476 | -0.0203 | -0.0402 | -0.0004 | 20 | BELOW_ZERO |
| Home-win Brier (primary) | 2025 | 165 | 0.2131 | 0.2528 | -0.0391 | -0.0571 | -0.0210 | 22 | BELOW_ZERO |
| Home-win Brier (primary) | ALL | 450 | 0.2278 | 0.2485 | -0.0222 | -0.0331 | -0.0114 | 62 | BELOW_ZERO |
| Home-win log loss | 2023 | 140 | 0.6761 | 0.6819 | -0.0116 | -0.0508 | 0.0277 | 20 | SPANS_ZERO |
| Home-win log loss | 2024 | 145 | 0.6571 | 0.6883 | -0.0398 | -0.0836 | 0.0041 | 20 | SPANS_ZERO |
| Home-win log loss | 2025 | 165 | 0.6143 | 0.6989 | -0.0832 | -0.1221 | -0.0444 | 22 | BELOW_ZERO |
| Home-win log loss | ALL | 450 | 0.6473 | 0.6902 | -0.0461 | -0.0695 | -0.0227 | 62 | BELOW_ZERO |
| Margin CRPS | 2023 | 140 | 7.8490 | 8.1404 | -0.3394 | -0.7213 | 0.0425 | 20 | SPANS_ZERO |
| Margin CRPS | 2024 | 145 | 8.6116 | 8.9293 | -0.3750 | -0.7799 | 0.0299 | 20 | SPANS_ZERO |
| Margin CRPS | 2025 | 165 | 8.9141 | 10.2486 | -1.3403 | -1.9019 | -0.7787 | 22 | BELOW_ZERO |
| Margin CRPS | ALL | 450 | 8.4853 | 9.1676 | -0.7060 | -0.9863 | -0.4258 | 62 | BELOW_ZERO |
| Total CRPS | 2023 | 140 | 10.0738 | 10.9576 | -0.8946 | -1.5689 | -0.2202 | 20 | BELOW_ZERO |
| Total CRPS | 2024 | 145 | 10.6906 | 12.6465 | -1.9123 | -2.8668 | -0.9578 | 20 | BELOW_ZERO |
| Total CRPS | 2025 | 165 | 10.4295 | 10.6714 | -0.2062 | -0.8104 | 0.3980 | 22 | SPANS_ZERO |
| Total CRPS | ALL | 450 | 10.4030 | 11.3968 | -0.9786 | -1.4246 | -0.5325 | 62 | BELOW_ZERO |
| Over the league-median line, Brier | 2023 | 140 | 0.2217 | 0.2425 | -0.0188 | -0.0442 | 0.0067 | 20 | SPANS_ZERO |
| Over the league-median line, Brier | 2024 | 145 | 0.2008 | 0.2437 | -0.0406 | -0.0647 | -0.0164 | 20 | BELOW_ZERO |
| Over the league-median line, Brier | 2025 | 165 | 0.2468 | 0.2486 | -0.0018 | -0.0202 | 0.0167 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 450 | 0.2242 | 0.2451 | -0.0198 | -0.0327 | -0.0068 | 62 | BELOW_ZERO |


## Against TEAM_BASELINE_P (TB-1)

| metric | season | n_games | candidate | comparator_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|
| Home-win Brier (primary) | 2023 | 140 | 0.2416 | 0.2428 | -0.0023 | -0.0155 | 0.0109 | 20 | SPANS_ZERO |
| Home-win Brier (primary) | 2024 | 145 | 0.2312 | 0.2340 | -0.0050 | -0.0164 | 0.0063 | 20 | SPANS_ZERO |
| Home-win Brier (primary) | 2025 | 165 | 0.2131 | 0.2181 | -0.0046 | -0.0121 | 0.0030 | 22 | SPANS_ZERO |
| Home-win Brier (primary) | ALL | 450 | 0.2278 | 0.2309 | -0.0040 | -0.0098 | 0.0019 | 62 | SPANS_ZERO |
| Home-win log loss | 2023 | 140 | 0.6761 | 0.6785 | -0.0047 | -0.0327 | 0.0232 | 20 | SPANS_ZERO |
| Home-win log loss | 2024 | 145 | 0.6571 | 0.6611 | -0.0091 | -0.0346 | 0.0165 | 20 | SPANS_ZERO |
| Home-win log loss | 2025 | 165 | 0.6143 | 0.6266 | -0.0115 | -0.0281 | 0.0050 | 22 | SPANS_ZERO |
| Home-win log loss | ALL | 450 | 0.6473 | 0.6539 | -0.0085 | -0.0213 | 0.0042 | 62 | SPANS_ZERO |
| Margin CRPS | 2023 | 140 | 7.8490 | 7.9845 | -0.1475 | -0.4043 | 0.1093 | 20 | SPANS_ZERO |
| Margin CRPS | 2024 | 145 | 8.6116 | 8.5803 | -0.0030 | -0.2526 | 0.2466 | 20 | SPANS_ZERO |
| Margin CRPS | 2025 | 165 | 8.9141 | 9.1821 | -0.2844 | -0.5522 | -0.0166 | 22 | BELOW_ZERO |
| Margin CRPS | ALL | 450 | 8.4853 | 8.6156 | -0.1495 | -0.2935 | -0.0055 | 62 | BELOW_ZERO |
| Total CRPS | 2023 | 140 | 10.0738 | 10.0449 | 0.0373 | -0.1848 | 0.2593 | 20 | SPANS_ZERO |
| Total CRPS | 2024 | 145 | 10.6906 | 11.1570 | -0.4791 | -0.7723 | -0.1859 | 20 | BELOW_ZERO |
| Total CRPS | 2025 | 165 | 10.4295 | 10.5526 | -0.0624 | -0.4839 | 0.3591 | 22 | SPANS_ZERO |
| Total CRPS | ALL | 450 | 10.4030 | 10.5894 | -0.1647 | -0.3535 | 0.0242 | 62 | SPANS_ZERO |
| Over the league-median line, Brier | 2023 | 140 | 0.2217 | 0.2145 | 0.0079 | 0.0002 | 0.0156 | 20 | ABOVE_ZERO |
| Over the league-median line, Brier | 2024 | 145 | 0.2008 | 0.2062 | -0.0054 | -0.0122 | 0.0014 | 20 | SPANS_ZERO |
| Over the league-median line, Brier | 2025 | 165 | 0.2468 | 0.2489 | 0.0003 | -0.0137 | 0.0143 | 22 | SPANS_ZERO |
| Over the league-median line, Brier | ALL | 450 | 0.2242 | 0.2244 | 0.0009 | -0.0049 | 0.0067 | 62 | SPANS_ZERO |


## Calibration of P(home win) on the test seasons

Calibration-in-the-large 0.0102; ECE 0.0333; logistic slope 1.205 (SE 0.208), intercept -0.089 (SE 0.109). Brier decomposition: reliability 0.0018, resolution 0.0232, uncertainty 0.2478.

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 2 | 0.1406 | 0.0000 | 0.0000 | 0.6576 |
| [0.2, 0.3) | 9 | 0.2758 | 0.2222 | 0.0632 | 0.5474 |
| [0.3, 0.4) | 39 | 0.3628 | 0.2821 | 0.1654 | 0.4378 |
| [0.4, 0.5) | 85 | 0.4548 | 0.3882 | 0.2916 | 0.4945 |
| [0.5, 0.6) | 135 | 0.5481 | 0.5630 | 0.4787 | 0.6437 |
| [0.6, 0.7) | 128 | 0.6413 | 0.6641 | 0.5785 | 0.7400 |
| [0.7, 0.8) | 45 | 0.7379 | 0.7333 | 0.5896 | 0.8404 |
| [0.8, 0.9) | 7 | 0.8178 | 0.8571 | 0.4869 | 0.9743 |
| [0.9, 1.0] | 0 | — | — | — | — |


## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)

| half_life_days | ridge | cov_inflation | objective | n |
|---|---|---|---|---|
| 90.0000 | 8.0000 | 1.2000 | 17.4690 | 280.0000 |
| 90.0000 | 8.0000 | 1.1000 | 17.4731 | 280.0000 |
| 90.0000 | 8.0000 | 1.3000 | 17.4798 | 280.0000 |
| 90.0000 | 8.0000 | 1.0000 | 17.4953 | 280.0000 |
| 90.0000 | 2.0000 | 1.2000 | 17.5111 | 280.0000 |
| 90.0000 | 2.0000 | 1.3000 | 17.5155 | 280.0000 |
| 90.0000 | 2.0000 | 1.1000 | 17.5216 | 280.0000 |
| 90.0000 | 2.0000 | 1.0000 | 17.5504 | 280.0000 |
| 45.0000 | 8.0000 | 1.2000 | 17.5588 | 280.0000 |
| 45.0000 | 8.0000 | 1.3000 | 17.5617 | 280.0000 |


## Receipt

- `run_utc`: 2026-10-14T09:02:39Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBL-JOINT-r1
- `archive_snapshot_sha256`: e021011368510ac7f3e1ec167b426403426f1afc8c9b7d8412d25ddffc57cddb
- `seconds`: 61

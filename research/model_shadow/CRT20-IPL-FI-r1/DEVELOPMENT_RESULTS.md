# Development results: `CRT20-IPL-FI-r1` (first-innings runs, `Cricket T20/IPL`)

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Refitted before every match date from earlier IPL first innings (four seasons plus season to date). Hyperparameters chosen on [2021, 2022] only; test seasons [2023, 2024, 2025].

**Verdict for C2 (team model):** `FAIL_DEVELOPMENT` (CRPS interval below 0 against both C1 and C0 in every test season required).

Central 80% interval coverage on the test seasons (target 0.80): C0 0.815, C1 0.801, C2 0.796, C2PRE 0.796.

PIT histogram, 5 equal bins (a flat histogram is calibrated; U-shaped means too narrow): C0 [36, 40, 38, 47, 50]; C2 [36, 37, 40, 47, 51].

| candidate | comparator | metric | season | n | cand_value | comp_value | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | C0 | crps | 2023 | 71 | 17.7127 | 17.8118 | -0.1193 | -0.3257 | 0.0870 | 9 | SPANS_ZERO |
| C1 | C0 | crps | 2024 | 70 | 21.5857 | 21.7090 | -0.2110 | -0.7077 | 0.2857 | 10 | SPANS_ZERO |
| C1 | C0 | crps | 2025 | 70 | 19.9237 | 20.0487 | -0.0278 | -0.3019 | 0.2463 | 12 | SPANS_ZERO |
| C1 | C0 | crps | ALL | 211 | 19.7311 | 19.8468 | -0.1135 | -0.2925 | 0.0656 | 31 | SPANS_ZERO |
| C1 | C0 | brier_over | 2023 | 71 | 0.2281 | 0.2312 | -0.0031 | -0.0071 | 0.0010 | 9 | SPANS_ZERO |
| C1 | C0 | brier_over | 2024 | 70 | 0.2412 | 0.2425 | -0.0036 | -0.0135 | 0.0063 | 10 | SPANS_ZERO |
| C1 | C0 | brier_over | 2025 | 70 | 0.2511 | 0.2532 | 0.0053 | -0.0091 | 0.0197 | 12 | SPANS_ZERO |
| C1 | C0 | brier_over | ALL | 211 | 0.2401 | 0.2423 | -0.0000 | -0.0060 | 0.0060 | 31 | SPANS_ZERO |
| C2 | C1 | crps | 2023 | 71 | 17.7122 | 17.7127 | -0.0097 | -0.0523 | 0.0328 | 9 | SPANS_ZERO |
| C2 | C1 | crps | 2024 | 70 | 21.5976 | 21.5857 | 0.0165 | -0.0157 | 0.0488 | 10 | SPANS_ZERO |
| C2 | C1 | crps | 2025 | 70 | 19.9232 | 19.9237 | -0.0151 | -0.0639 | 0.0337 | 12 | SPANS_ZERO |
| C2 | C1 | crps | ALL | 211 | 19.7347 | 19.7311 | -0.0033 | -0.0259 | 0.0192 | 31 | SPANS_ZERO |
| C2 | C1 | brier_over | 2023 | 71 | 0.2280 | 0.2281 | -0.0002 | -0.0007 | 0.0004 | 9 | SPANS_ZERO |
| C2 | C1 | brier_over | 2024 | 70 | 0.2417 | 0.2412 | 0.0005 | -0.0001 | 0.0012 | 10 | SPANS_ZERO |
| C2 | C1 | brier_over | 2025 | 70 | 0.2511 | 0.2511 | -0.0002 | -0.0010 | 0.0007 | 12 | SPANS_ZERO |
| C2 | C1 | brier_over | ALL | 211 | 0.2402 | 0.2401 | 0.0001 | -0.0003 | 0.0005 | 31 | SPANS_ZERO |
| C2 | C0 | crps | 2023 | 71 | 17.7122 | 17.8118 | -0.1291 | -0.3528 | 0.0947 | 9 | SPANS_ZERO |
| C2 | C0 | crps | 2024 | 70 | 21.5976 | 21.7090 | -0.1945 | -0.6891 | 0.3001 | 10 | SPANS_ZERO |
| C2 | C0 | crps | 2025 | 70 | 19.9232 | 20.0487 | -0.0429 | -0.3299 | 0.2442 | 12 | SPANS_ZERO |
| C2 | C0 | crps | ALL | 211 | 19.7347 | 19.8468 | -0.1168 | -0.2984 | 0.0648 | 31 | SPANS_ZERO |
| C2 | C0 | brier_over | 2023 | 71 | 0.2280 | 0.2312 | -0.0032 | -0.0073 | 0.0008 | 9 | SPANS_ZERO |
| C2 | C0 | brier_over | 2024 | 70 | 0.2417 | 0.2425 | -0.0031 | -0.0128 | 0.0067 | 10 | SPANS_ZERO |
| C2 | C0 | brier_over | 2025 | 70 | 0.2511 | 0.2532 | 0.0051 | -0.0094 | 0.0197 | 12 | SPANS_ZERO |
| C2 | C0 | brier_over | ALL | 211 | 0.2402 | 0.2423 | 0.0001 | -0.0060 | 0.0061 | 31 | SPANS_ZERO |
| C2PRE | C0 | crps | 2023 | 71 | 17.7245 | 17.8118 | -0.1103 | -0.3184 | 0.0977 | 9 | SPANS_ZERO |
| C2PRE | C0 | crps | 2024 | 70 | 21.5985 | 21.7090 | -0.1950 | -0.6788 | 0.2889 | 10 | SPANS_ZERO |
| C2PRE | C0 | crps | 2025 | 70 | 19.9214 | 20.0487 | -0.0481 | -0.3172 | 0.2209 | 12 | SPANS_ZERO |
| C2PRE | C0 | crps | ALL | 211 | 19.7385 | 19.8468 | -0.1136 | -0.2881 | 0.0610 | 31 | SPANS_ZERO |
| C2PRE | C0 | brier_over | 2023 | 71 | 0.2280 | 0.2312 | -0.0032 | -0.0073 | 0.0010 | 9 | SPANS_ZERO |
| C2PRE | C0 | brier_over | 2024 | 70 | 0.2414 | 0.2425 | -0.0033 | -0.0130 | 0.0064 | 10 | SPANS_ZERO |
| C2PRE | C0 | brier_over | 2025 | 70 | 0.2511 | 0.2532 | 0.0048 | -0.0091 | 0.0186 | 12 | SPANS_ZERO |
| C2PRE | C0 | brier_over | ALL | 211 | 0.2401 | 0.2423 | -0.0001 | -0.0060 | 0.0057 | 31 | SPANS_ZERO |


## Tuning (top 8; objective = C2 mean CRPS on the tune seasons)

| half_life_days | ridge | k_venue | sd_inflation | objective |
|---|---|---|---|---|
| 91.2500 | 320.0000 | 20.0000 | 1.0000 | 17.1438 |
| 91.2500 | 320.0000 | 40.0000 | 1.0000 | 17.1610 |
| 91.2500 | 160.0000 | 20.0000 | 1.0000 | 17.1616 |
| 91.2500 | 320.0000 | 5.0000 | 1.0000 | 17.1682 |
| 91.2500 | 320.0000 | 20.0000 | 1.1000 | 17.1729 |
| 91.2500 | 160.0000 | 40.0000 | 1.0000 | 17.1784 |
| 91.2500 | 320.0000 | 5.0000 | 1.1000 | 17.1790 |
| 91.2500 | 160.0000 | 5.0000 | 1.0000 | 17.1867 |


## Receipt

- `run_utc`: 2026-10-14T09:13:42Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: CRT20-IPL-FI-r1
- `params`: CricketParams(half_life_days=91.25, ridge=320.0, k_venue=20.0, sd_inflation=1.0)
- `dropped_rows`: {'method:Not applicable': 33, 'short_first_innings': 13, 'method:DLS': 22, 'method:Weather Abandonment': 11, 'invalid_identity_or_date': 2}
- `rows_used`: 1132
- `seconds`: 676

# Calibration audit of the issued cards' stated probabilities

**Descriptive only.** Source: `GAME_PREDICTION_RANK_LOG.csv` (rows with a numeric `stated_p` and a PASS or FAIL grade). Rows within a card are dependent, so intervals resample whole cards. The cards span several method and scoring versions, many were ungated, and line choice shapes hit rates (CURRENT_RULES §10). Nothing here recalibrates, regrades or relabels any card. This report applies the October 14 calibration recommendations to the cards' own history (see ML_RL_IMPLEMENTATION_FRAMEWORK §4, report R4).

Inventory: {'rows': 2245, 'with_numeric_p': 807, 'decisive_with_p': 795, 'excluded_statuses': {'UNVERIFIED': 12}}.

Calibration-in-the-large is mean p − hit rate (positive = over-confident). Slope: logistic regression of the outcome on logit(p); 1 is ideal, below 1 means probabilities are too extreme.

| group | rows | cards | mean_p | hit_rate | cal_in_large | cil_card_lo | cil_card_hi | slope | slope_se | ece | brier | reliability | resolution |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL | 795 | 203 | 0.5932 | 0.6000 | -0.0068 | -0.0278 | 0.0141 | 0.8314 | 0.1119 | 0.0308 | 0.2231 | 0.0019 | 0.0175 |
| RANK_1_2 | 383 | 200 | 0.6577 | 0.6371 | 0.0206 | -0.0232 | 0.0685 | 0.8645 | 0.1906 | 0.0280 | 0.2188 | 0.0014 | 0.0135 |
| RANK_3_PLUS | 412 | 196 | 0.5332 | 0.5655 | -0.0323 | -0.0778 | 0.0122 | 0.8985 | 0.1621 | 0.0454 | 0.2270 | 0.0029 | 0.0193 |
| P-300..P-499 | 536 | 134 | 0.5606 | 0.5672 | -0.0066 | -0.0286 | 0.0178 | 0.9178 | 0.1611 | 0.0313 | 0.2302 | 0.0012 | 0.0153 |
| P-500+ | 248 | 62 | 0.6679 | 0.6694 | -0.0015 | -0.0443 | 0.0403 | 0.7319 | 0.1674 | 0.0582 | 0.2063 | 0.0104 | 0.0236 |


## Reliability bins, all rows

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 4 | 0.2525 | 0.5000 | 0.1500 | 0.8500 |
| [0.3, 0.4) | 69 | 0.3614 | 0.4058 | 0.2979 | 0.5236 |
| [0.4, 0.5) | 169 | 0.4451 | 0.5089 | 0.4341 | 0.5832 |
| [0.5, 0.6) | 230 | 0.5555 | 0.5522 | 0.4876 | 0.6151 |
| [0.6, 0.7) | 133 | 0.6482 | 0.5940 | 0.5090 | 0.6737 |
| [0.7, 0.8) | 68 | 0.7484 | 0.7500 | 0.6356 | 0.8377 |
| [0.8, 0.9) | 116 | 0.8633 | 0.8534 | 0.7778 | 0.9064 |
| [0.9, 1.0] | 6 | 0.9067 | 0.8333 | 0.4365 | 0.9699 |


## Reliability bins, Ranks 1–2

| bin | n | mean_p | hit_rate | wilson_lo | wilson_hi |
|---|---|---|---|---|---|
| [0.0, 0.1) | 0 | — | — | — | — |
| [0.1, 0.2) | 0 | — | — | — | — |
| [0.2, 0.3) | 0 | — | — | — | — |
| [0.3, 0.4) | 0 | — | — | — | — |
| [0.4, 0.5) | 10 | 0.4601 | 0.6000 | 0.3127 | 0.8318 |
| [0.5, 0.6) | 159 | 0.5556 | 0.5409 | 0.4634 | 0.6165 |
| [0.6, 0.7) | 100 | 0.6451 | 0.6000 | 0.5020 | 0.6906 |
| [0.7, 0.8) | 39 | 0.7472 | 0.7436 | 0.5892 | 0.8543 |
| [0.8, 0.9) | 70 | 0.8682 | 0.8429 | 0.7401 | 0.9099 |
| [0.9, 1.0] | 5 | 0.9080 | 0.8000 | 0.3755 | 0.9638 |


## Receipt

- `run_utc`: 2026-10-14T11:16:17Z
- `repo_head`: 773f64f39ecc55b64ce76de6b7b49644a1d8e8da
- `code_sha256`: 8b429aa88492aabdf45e13558dff330696678b4faef7b11ae8869b24d1271f5a
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `rank_log_sha256`: 1d92b72a7e06a6cda846ef5275b9707b5efe874d536ee62a37f9501634c56456
- `completed_utc`: 2026-10-14T11:16:17Z

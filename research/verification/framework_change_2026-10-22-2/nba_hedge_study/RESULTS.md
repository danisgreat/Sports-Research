# Hedge schedule study

**Evidence class: `HISTORICAL_DEVELOPMENT_HEDGE_STUDY_NOT_PROSPECTIVE`.** Schedules chosen on the tune window only, evaluated afterwards on identical events; reference = V3 fixed η = 2. CRPS columns are weight-averaged expert CRPS (upper bounds on the mixture). Study only; PRIMARY_HEDGE_MIX_V3 unchanged.

| policy | selected | tune_common_loss | test_events | test_common_loss | test_brier_home | test_brier_over | mean_ess | collapsed_share |
|---|---|---|---|---|---|---|---|---|
| V3_FIXED_ETA_2 | 0 | 0.2235 | 1231 | 0.2278 | 0.2144 | 0.2412 | 1.1926 | 0.6206 |
| ADAHEDGE | 0 | 0.2234 | 1231 | 0.2268 | 0.2136 | 0.2400 | 1.4476 | 0.0000 |
| FIXED_ETA_0.5 | 0 | 0.2229 | 1231 | 0.2265 | 0.2133 | 0.2396 | 1.5847 | 0.0000 |
| FIXED_ETA_1 | 0 | 0.2231 | 1231 | 0.2271 | 0.2140 | 0.2402 | 1.3322 | 0.0000 |
| FIXED_ETA_5 | 0 | 0.2241 | 1231 | 0.2286 | 0.2148 | 0.2424 | 1.1044 | 0.7782 |
| FIXED_ETA_10 | 0 | 0.2244 | 1231 | 0.2288 | 0.2150 | 0.2426 | 1.0665 | 0.8660 |
| FIXED_ETA_20 | 0 | 0.2246 | 1231 | 0.2290 | 0.2152 | 0.2428 | 1.0389 | 0.9033 |
| DISCOUNTED_ETA_2_G0.99 | 0 | 0.2229 | 1231 | 0.2258 | 0.2118 | 0.2399 | 1.8545 | 0.0000 |
| DISCOUNTED_ETA_2_G0.995 | 0 | 0.2230 | 1231 | 0.2264 | 0.2122 | 0.2406 | 1.5659 | 0.0000 |
| DISCOUNTED_ETA_2_G0.999 | 0 | 0.2234 | 1231 | 0.2275 | 0.2140 | 0.2409 | 1.2454 | 0.3274 |
| ESS_FLOOR_1.5_ETA_20 | 0 | 0.2234 | 1231 | 0.2270 | 0.2134 | 0.2407 | 1.5106 | 0.0000 |
| ESS_FLOOR_2_ETA_20 | 1 | 0.2226 | 1231 | 0.2259 | 0.2125 | 0.2393 | 2.0000 | 0.0000 |
| SEASON_RESET_ETA_2 | 0 | 0.2235 | 1231 | 0.2278 | 0.2144 | 0.2412 | 1.1926 | 0.6206 |


| policy | reference | metric | k_weeks | n_events | mean | lo | hi | sd_w | status |
|---|---|---|---|---|---|---|---|---|---|
| ADAHEDGE | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0010 | -0.0017 | -0.0003 | 0.0017 | BELOW_ZERO |
| FIXED_ETA_0.5 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0013 | -0.0023 | -0.0004 | 0.0023 | BELOW_ZERO |
| FIXED_ETA_1 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0007 | -0.0012 | -0.0002 | 0.0013 | BELOW_ZERO |
| FIXED_ETA_5 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | 0.0008 | 0.0001 | 0.0014 | 0.0015 | ABOVE_ZERO |
| FIXED_ETA_10 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | 0.0010 | 0.0002 | 0.0018 | 0.0020 | ABOVE_ZERO |
| FIXED_ETA_20 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | 0.0012 | 0.0001 | 0.0022 | 0.0026 | ABOVE_ZERO |
| DISCOUNTED_ETA_2_G0.99 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0018 | -0.0028 | -0.0007 | 0.0026 | BELOW_ZERO |
| DISCOUNTED_ETA_2_G0.995 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0013 | -0.0020 | -0.0005 | 0.0019 | BELOW_ZERO |
| DISCOUNTED_ETA_2_G0.999 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0003 | -0.0005 | -0.0001 | 0.0005 | BELOW_ZERO |
| ESS_FLOOR_1.5_ETA_20 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0007 | -0.0014 | -0.0001 | 0.0016 | BELOW_ZERO |
| ESS_FLOOR_2_ETA_20 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | -0.0019 | -0.0033 | -0.0005 | 0.0035 | BELOW_ZERO |
| SEASON_RESET_ETA_2 | V3_FIXED_ETA_2 | common_loss | 26 | 1231 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | SPANS_ZERO |


## Regime alerts (tune window, Page–Hinkley)

| worse | than | alarm | event_id | available_at |
|---|---|---|---|---|
| RATINGS_FAST | RATINGS_SLOW | 1 | ESPN:401704685 | 2024-10-31T23:00:00+00:00 |
| RATINGS_FAST | LEAGUE_BASELINE | 1 | ESPN:401584953 | 2023-12-16T03:30:00+00:00 |
| RATINGS_SLOW | RATINGS_FAST | 1 | ESPN:401704696 | 2024-11-02T01:00:00+00:00 |
| RATINGS_SLOW | LEAGUE_BASELINE | 1 | ESPN:401584952 | 2023-12-16T03:00:00+00:00 |
| LEAGUE_BASELINE | RATINGS_FAST | 1 | ESPN:401584900 | 2023-12-02T01:00:00+00:00 |
| LEAGUE_BASELINE | RATINGS_SLOW | 1 | ESPN:401584900 | 2023-12-02T01:00:00+00:00 |


## Receipt

- `ledger`: research\verification\framework_change_2026-10-22-2\nba_hedge_ledger_2023_26.csv
- `ledger_sha256`: c857ce805751eef1a182ef13fa48f65f96a66ac3cc3291cd825a30f5ad0242ac
- `tune_end`: 2025-06-30T00:00:00+00:00
- `code_sha256`: 39cfede450f27ceaa9591ec096a46c34969a68a3524049051421dad43e0ee1a8
- `repository_head`: ba6f0e25c406dc29bea21f85877efc4425450558
- `generated_at`: 2026-10-22T04:50:21.926538+00:00
- `evidence_class`: HISTORICAL_DEVELOPMENT_HEDGE_STUDY_NOT_PROSPECTIVE
- `selected_on_tune_window`: ESS_FLOOR_2_ETA_20
- `summary_csv_sha256`: b9a5c830fc04443bee520eeb749fda6f24a1b7fe0597b1c91742acb02c2d5a77
- `paired_csv_sha256`: 6810119bda1d8ce6cf87f27e7553a5c2b6624d291552c862a991e3eef0c8122b
- `alerts_csv_sha256`: 573b71111ad8da07ca69afd3d05aa1d8ae74abc5d20acb56f05d9792ee727ba6

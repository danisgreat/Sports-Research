# Competition parameter rows and width floors (WIDTH-v1)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-05 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md) and recommendations 1-2 of the [21 October league-neutral review](research/verification/review_2026-10-21_league_neutral_ml_sim/REPORT.md). One method, league-specific numbers. The authoritative table is [COMPETITION_PARAMETERS.csv](research/competition_parameters/COMPETITION_PARAMETERS.csv); this page explains it and shows it. Prompt 1 reads a competition's row instead of re-deriving the league anchors each time; the row also supplies the **width floor** and the league-only baseline.

## 1. What a row holds

| Column | Meaning |
|---|---|
| `mean_total`, `mean_home_margin` | Mean total and mean home margin of the competition's games |
| `raw_margin_sd`, `raw_total_sd` | Spread of margin and total with no team information: the league-only baseline's widths |
| `resid_margin_sd`, `resid_total_sd` | Spread left after a fitted team-strength model: the **width floor** for a card centred on team strength |
| `z_margin_sd`, `z_total_sd` | SD of (actual − model mean) / model SD: how honest the fitted model's own widths were; a row outside 0.80-1.25 is `NOT_USABLE` |
| `store_final_events`, `store_extra_time_rate` | For competitions with at least 300 verified finals in the learning store: the count and the share decided in overtime or extras |
| `usable` | `USABLE_DEVELOPMENT`, `NOT_USABLE` (data-defect flag, implausible z, or fewer than 30 rows) or `STORE_ONLY` |
| `evidence_class` | `HISTORICAL_DEVELOPMENT_UNADMITTED` (stored development predictions, test seasons 2023 onward, source admission unverified) and/or `STORE_VERIFIED_FINALS_CURRENT_CAPTURE` |

Method (script outside the repository, MD-only rule): for each stored `DEVELOPMENT_PREDICTIONS.csv` the FROZEN rows give the mean total, mean home margin, raw SDs and the SD of the residual between the actual margin or total and the fitted model's mean; the learning store's latest FINAL result per event gives the verified counts and extra-time share. Residual SDs come from models that know team strength but not lineups, so they are floors for a card that has no better information, and a card with a documented reason may go below them (`width_floor_exception`).

## 2. The width floor

`python -m ml reference width --competition C` prints the floor for the margin and the total.

1. The competition's own row, if `USABLE_DEVELOPMENT` and it has a residual SD: floor = that SD.
2. Else the competition's **family prior** (the median of the usable members) widened by 10%.
3. Else no floor: the card prints `NOT_COVERED` and uses the widest of the supplied or analogous benchmarks.

A card's printed margin or total SD below its floor fails the linter unless the picks header carries a `width_floor_exception` with its reason. The monthly coverage report (`ledger coverage`) checks the realised z RMS against 0.85-1.15 per family; outside the band, the row is the first suspect. This addresses the finding that card margins ran too narrow (z RMS 1.46 on six margins, 2026-10-21).

## 3. Rows (22 October 2026)

| Competition | Status | Games | Mean total | Home margin | Raw margin SD | Raw total SD | Residual margin SD | Residual total SD | z SD margin / total | Store finals | Extra-time share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| AFL/AFL | USABLE_DEVELOPMENT | 819 | 167.72 | 6.44 | 40.51 | 29.07 | 33.45 | 29.47 | 1.021 / 1.024 | - | - |
| AFL/AFLW | USABLE_DEVELOPMENT | 400 | 74.08 | 0.83 | 32.4 | 22.36 | 25.13 | 21.88 | 1.082 / 1.028 | - | - |
| State Level AFL/SANFL | USABLE_DEVELOPMENT | 330 | 144.1 | 1.05 | 40.46 | 30.92 | 35.56 | 29.9 | 1.055 / 1.017 | - | - |
| State Level AFL/VFL | USABLE_DEVELOPMENT | 689 | 160.28 | 3.07 | 43.26 | 29.71 | 36.58 | 29.25 | 0.988 / 0.995 | - | - |
| State Level AFL/VFLW | USABLE_DEVELOPMENT | 336 | 67.95 | 1.75 | 36.28 | 21.17 | 30.71 | 20.3 | 1.159 / 1.084 | - | - |
| State Level AFL/WAFL | USABLE_DEVELOPMENT | 366 | 146.27 | 8.35 | 43.52 | 32.06 | 33.84 | 30.63 | 1.071 / 1.076 | - | - |
| American Football/NFL | USABLE_DEVELOPMENT | 1087 | 44.79 | 2.15 | 13.86 | 13.63 | 12.95 | 13.36 | 1.024 / 1.039 | - | - |
| Baseball/KBO | USABLE_DEVELOPMENT | 2933 | 9.59 | -0.08 | 4.79 | 4.89 | 4.75 | 4.88 | 1.005 / 1.034 | - | - |
| Baseball/MLB | USABLE_DEVELOPMENT | 9718 | 8.97 | 0.02 | 4.52 | 4.5 | 4.46 | 4.49 | 1.01 / 1.025 | 374 | 0.0802 |
| Baseball/Minor Leagues | USABLE_DEVELOPMENT | 8645 | 10.83 | -0.08 | 4.87 | 5.29 | 4.86 | 5.21 | 0.975 / 1.052 | - | - |
| Baseball/NPB | USABLE_DEVELOPMENT | 3425 | 6.84 | 0.09 | 3.85 | 3.83 | 3.83 | 3.79 | 1.018 / 1.017 | - | - |
| Basketball/Austria Basketball Bundesliga | NOT_USABLE | 528 | 155.66 | 8.95 | 12.86 | 8.18 | 8.51 | 8.49 | 0.97 / 0.868 | - | - |
| Basketball/B League | USABLE_DEVELOPMENT | 2937 | 159.19 | 0.61 | 14.94 | 17.66 | 12.9 | 16.28 | 0.995 / 0.994 | - | - |
| Basketball/EuroBasket | NOT_USABLE | 231 | 177.5 | -20.79 | 124.06 | 127.91 | 123.57 | 126.58 | 5.343 / 4.936 | - | - |
| Basketball/EuroCup | USABLE_DEVELOPMENT | 719 | 168.06 | 2.57 | 14.94 | 18.83 | 13.52 | 17.56 | 1.062 / 0.998 | - | - |
| Basketball/EuroLeague | USABLE_DEVELOPMENT | 1298 | 166.65 | 3.74 | 12.43 | 17.92 | 11.72 | 16.67 | 0.996 / 0.964 | - | - |
| Basketball/Greek Basket League | NOT_USABLE | 552 | 161.49 | 4.05 | 16.17 | 17.87 | 12.0 | 17.1 | 1.008 / 0.992 | - | - |
| Basketball/KBL | USABLE_DEVELOPMENT | 1080 | 159.39 | 1.18 | 13.13 | 17.93 | 12.61 | 16.82 | 0.993 / 0.982 | - | - |
| Basketball/Liga ACB | USABLE_DEVELOPMENT | 1224 | 169.45 | 3.98 | 13.95 | 18.36 | 12.08 | 17.07 | 0.984 / 0.986 | - | - |
| Basketball/NBA | USABLE_DEVELOPMENT | 4922 | 229.15 | 2.0 | 15.43 | 19.9 | 14.05 | 18.7 | 1.024 / 0.985 | 3693 | 0.0468 |
| Basketball/NBA G League | USABLE_DEVELOPMENT | 2092 | 228.61 | 1.12 | 14.59 | 20.32 | 14.0 | 19.06 | 1.008 / 0.979 | - | - |
| Basketball/NBL | USABLE_DEVELOPMENT | 590 | 181.51 | 1.4 | 16.08 | 19.38 | 15.03 | 18.12 | 1.016 / 0.961 | - | - |
| Basketball/WNBA | USABLE_DEVELOPMENT | 986 | 164.12 | 1.49 | 13.97 | 17.29 | 12.76 | 16.63 | 1.04 / 1.008 | - | - |
| Ice Hockey/Czech Extraliga | USABLE_DEVELOPMENT | 1456 | 5.4 | 0.47 | 2.44 | 2.19 | 2.38 | 2.18 | 1.027 / 0.966 | - | - |
| Ice Hockey/Danish Metal Ligaen | NOT_USABLE | 768 | 6.93 | 1.25 | 1.72 | 2.0 | 1.62 | 2.02 | 0.63 / 0.796 | - | - |
| Ice Hockey/NHL | USABLE_DEVELOPMENT | 5248 | 6.23 | 0.21 | 2.62 | 2.3 | 2.55 | 2.3 | 1.026 / 0.944 | 1313 | 0.2064 |
| Rugby League/NRL | USABLE_DEVELOPMENT | 804 | 45.54 | 2.83 | 19.31 | 13.55 | 17.98 | 13.51 | 1.105 / 1.068 | - | - |
| Soccer/Premier League | USABLE_DEVELOPMENT | 1900 | 2.93 | 0.27 | 1.9 | 1.66 | 1.71 | 1.65 | 1.015 / 0.976 | - | - |

Units are points (basketball, football, rugby, AFL), goals (hockey, soccer) or runs (baseball). The learning store's counts are verified two-lineage finals captured on 22 October 2026 (NBA 3,693) or earlier (NHL 1,313, MLB 374); NBA extra time is 4.7% of games and NHL 20.6%.

| Family prior | Mean total | Home margin | Residual margin SD | Residual total SD | Members |
|---|---:|---:|---:|---:|---|
| FAMILY_PRIOR:AFL | 145.19 | 2.41 | 33.65 | 29.36 | AFL/AFL, AFL/AFLW, State Level AFL/SANFL, State Level AFL/VFL, State Level AFL/VFLW, State Level AFL/WAFL |
| FAMILY_PRIOR:AMERICAN_FOOTBALL | 44.79 | 2.15 | 12.95 | 13.36 | American Football/NFL |
| FAMILY_PRIOR:BASEBALL | 9.28 | -0.03 | 4.61 | 4.69 | Baseball/KBO, Baseball/Minor Leagues, Baseball/MLB, Baseball/NPB |
| FAMILY_PRIOR:BASKETBALL_FIBA40 | 166.65 | 1.49 | 12.76 | 16.82 | Basketball/B League, Basketball/EuroCup, Basketball/EuroLeague, Basketball/KBL, Basketball/Liga ACB, Basketball/NBL, Basketball/WNBA |
| FAMILY_PRIOR:BASKETBALL_NBA48 | 228.88 | 1.56 | 14.03 | 18.88 | Basketball/NBA G League, Basketball/NBA |
| FAMILY_PRIOR:ICE_HOCKEY | 5.82 | 0.34 | 2.46 | 2.24 | Ice Hockey/Czech Extraliga, Ice Hockey/NHL |
| FAMILY_PRIOR:RUGBY_LEAGUE | 45.54 | 2.83 | 17.98 | 13.51 | Rugby League/NRL |
| FAMILY_PRIOR:SOCCER | 2.93 | 0.27 | 1.71 | 1.65 | Soccer/Premier League |

## 4. Data defects the table carries

- **Austria Basketball Bundesliga:** overtime field implausible (0 of 909 explicit rows) and total SD 8.5 points: `NOT_USABLE`.
- **EuroBasket:** margin and total SDs above 120 points: a corrupted build, `NOT_USABLE`.
- **Greek Basket League:** overtime field implausible and score dispersion flags for old seasons: `NOT_USABLE` until its history is re-verified.
- **Danish Metal Ligaen:** z SD 0.63 and 0.80, outside the band: `NOT_USABLE`.
- Every other development row carries `FIELD_OWNER_ADMISSION_UNVERIFIED`; the NBA, NHL and MLB rows also rest on the verified store.

## 5. Use and refresh

- **Baseline.** `ml.reference.baseline_grid` builds the league-only distribution (BASELINE_LEAGUE_V1 shape) from the row or the prior; hockey and baseball use `python -m ml baseline` because mean and SD alone do not fix a count distribution. A row older than 400 days prints `STALE_PROFILE`.
- **Refresh.** Prompt 7 rebuilds the table from verified results after each season and appends dated rows; prompt 8 admits them. A new row never overwrites the old one inside a season (STATFREEZE-v1).
- **Tournaments** (World Cup, EuroBasket, Olympics): short national-team histories and a failed development model; keep them qualitative or widely priced until a national-team rating across windows is built.
- **Early season:** widths do not shrink. The reference's rating uncertainty is already in the shrinkage constant k; a card never narrows below the floor because "the teams are known".

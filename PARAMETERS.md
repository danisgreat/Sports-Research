# Parameters: competition parameters, effect tables, base rates and league profiles

**Consolidated 2026-11-07, CR-2026.11.07-R3.** Four documents were joined verbatim on 2026-11-07 (R2) and then rewritten (R3): contradictions are resolved, Parts A and B keep their data tables byte for byte, and Part C (the September–October base-rates register, about 40 KB of historical numbers that no live rule reads) is condensed to its status, its regime table and an index of the archived original. Part and section numbers are unchanged. What changed and why: [consolidation report](research/verification/framework_change_2026-11-07-3/CONTRADICTIONS.md). Verbatim originals: [archive/consolidation_2026-11-07/merged_sources/](archive/consolidation_2026-11-07/merged_sources/).

**Which numbers a card may use.** Competition means, home edges, widths and floors: Part A (`research/competition_parameters/COMPETITION_PARAMETERS.csv`). Adjustment sizes: Part B (`research/effect_tables/EFFECT_TABLES.csv`), entered under [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) section 1. Nothing in Parts C or D is a card input.

---

# Part A: COMPETITION_PARAMETERS

*WIDTH-v1 (REV-05 of the [22 October review](research/verification/review_2026-10-22_framework_revamp/REPORT.md); recommendations 1–2 of the [21 October league-neutral review](research/verification/review_2026-10-21_league_neutral_ml_sim/REPORT.md)). One method, league-specific numbers. The authoritative table is [COMPETITION_PARAMETERS.csv](research/competition_parameters/COMPETITION_PARAMETERS.csv) (rows below checked against it on 2026-11-07); prompt 1 reads the competition's row instead of re-deriving league anchors. The row also supplies the width floor and the league-only baseline.*

## 1. What a row holds

| Column | Meaning |
|---|---|
| `mean_total`, `mean_home_margin` | Mean total and mean home margin of the competition's games |
| `raw_margin_sd`, `raw_total_sd` | Spread of margin and total with no team information: the league-only baseline's widths |
| `resid_margin_sd`, `resid_total_sd` | Spread left after a fitted team-strength model: the **width floor** for a card centred on team strength |
| `z_margin_sd`, `z_total_sd` | SD of (actual − model mean) / model SD: how honest the fitted model's widths were; a row outside 0.80–1.25 is `NOT_USABLE` |
| `store_final_events`, `store_extra_time_rate` | For competitions with at least 300 verified finals in the learning store: the count and the share decided in overtime or extras |
| `usable` | `USABLE_DEVELOPMENT`, `NOT_USABLE` (data-defect flag, implausible z, or fewer than 30 rows) or `STORE_ONLY` |
| `evidence_class` | `HISTORICAL_DEVELOPMENT_UNADMITTED` (stored development predictions, test seasons from 2023, source admission unverified) and/or `STORE_VERIFIED_FINALS_CURRENT_CAPTURE` |

Method (a disclosed helper outside the repository): for each stored `DEVELOPMENT_PREDICTIONS.csv`, the frozen rows give the mean total, mean home margin, raw SDs and the SD of the residual between the actual margin or total and the fitted model's mean; the learning store's latest FINAL result per event gives the verified counts and extra-time share. Residual SDs come from models that know team strength but not lineups, so they are floors for a card with no better information; a card with a documented reason may go below them (`width_floor_exception`).

## 2. The width floor

`python -m ml reference width --competition C` prints the floor for margin and total:

1. the competition's own row, if `USABLE_DEVELOPMENT` with a residual SD;
2. else its **family prior** (the median of usable members) widened by 10%;
3. else no floor: the card prints `NOT_COVERED` and uses the widest supplied or analogous benchmark.

A card SD below its floor fails `ml card lint` unless the picks header carries a `width_floor_exception` with its reason. The monthly `ledger coverage` report checks the realised z RMS against 0.85–1.15 per family; outside the band, the row is the first suspect (card margins ran too narrow, z RMS 1.46 on six margins, 2026-10-21).

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
- **Greek Basket League:** overtime field implausible and score-dispersion flags for old seasons: `NOT_USABLE` until its history is re-verified.
- **Danish Metal Ligaen:** z SD 0.63 and 0.80, outside the band: `NOT_USABLE`.
- Every other development row carries `FIELD_OWNER_ADMISSION_UNVERIFIED`; the NBA, NHL and MLB rows also rest on the verified store.

## 5. Use and refresh

- **Baseline.** `ml.reference.baseline_grid` builds the league-only distribution (BASELINE_LEAGUE_V1 shape) from the row or the prior; hockey and baseball use `python -m ml baseline`, because a mean and SD alone do not fix a count distribution. A row older than 400 days prints `STALE_PROFILE`.
- **Refresh.** Prompt 7 rebuilds the table from verified results after each season and appends dated rows; prompt 8 admits them. A row is never overwritten inside a season (STATFREEZE-v1).
- **Tournaments** (World Cup, EuroBasket, Olympics): short national-team histories and a failed development model; keep them qualitative or widely priced until a national-team rating across windows exists.
- **Early season:** widths do not shrink. The reference's rating uncertainty is already in its shrinkage constant k; a card never narrows below the floor because "the teams are known".
- **Overtime:** basketball lines include overtime (BK-OT-1); the extra-time share above is the overtime mass to price.

---

# Part B: EFFECT_TABLES

*EFFECT-v1 (REV-17). The authoritative table is [EFFECT_TABLES.csv](research/effect_tables/EFFECT_TABLES.csv); this part explains it and records what was measured on 22 October 2026. These are the only sizes an adjustment may use; the rules for using a row are in [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) section 1.*

## 1. Status classes

| Status | Meaning | Entry in the ledger |
|---|---|---|
| `MEASURED_CONFIRMED` | Estimated on this repository's verified finals and shown to help a held-out season (or a structural fact observed directly) | Full size |
| `MEASURED_NOT_CONFIRMED` | Estimated here, significant in sample, not shown to improve a held-out season | Half size until λ exists |
| `MEASURED_NULL` | Estimated here; the interval contains zero | No adjustment |
| `LITERATURE_START` | A published estimate for another period or data set | Half size until λ exists |
| `NOT_ESTIMATED` | No usable number; the row lists the data needed | `SCENARIO` row with declared weights only |

## 2. Measured on 22 October 2026 (NBA 2023-24 to 2025-26, NHL 2024-25)

Method (a disclosed helper outside the repository): for each game after the league had played 300 team-games in the season, the home margin was regressed on the difference in season-to-date net rating (points for minus against per game, shrunk with k = 2, same-season earlier games only) and on rest flags from the teams' previous game dates in the US Eastern calendar (back-to-back = played the previous calendar day; long rest = three or more days). Ordinary least squares with HC1 standard errors, on the learning store's verified finals ([nba_backfill](research/verification/framework_change_2026-10-22-2/nba_backfill/)).

| Competition | Term | Estimate | SE | Share of games | Reading |
|---|---|---:|---:|---:|---|
| NBA | Home edge (given net rating) | +1.66 pts | 0.35 | | Matches the toolkit's 1.71 |
| NBA | Net-rating coefficient | 0.90 | 0.03 | | Close to 1: the additive form is right and the average form (0.5) is not |
| NBA | Home team back-to-back | −2.88 pts | 0.71 | 17.5% | Significant in sample |
| NBA | Away team back-to-back | +2.74 pts to the home margin | 0.69 | 18.6% | Significant in sample |
| NBA | Home or away three or more rest days | +0.65, −0.02 | 0.66, 0.70 | 20.4%, 18.7% | Null |
| NHL | Home edge | +0.31 goals | 0.11 | | |
| NHL | Home or away back-to-back | −0.31, +0.29 goals | 0.28, 0.20 | 9.5%, 21.7% | Null |

**Out of sample, the NBA back-to-back effect did not help.** Fitted on 2023-24 and 2024-25 (−3.2 and +3.7 points) and applied to 2025-26, it left the home-win Brier at 0.2043 against 0.2037 without it (paired difference +0.0008, interval −0.0013 to +0.0029, 23 weeks). A significant in-sample coefficient is therefore `MEASURED_NOT_CONFIRMED` and enters at half size. The literature (Small 2007: 2.26 points, 1999-2000) and this repository agree in sign and size, and the adjustment has still not been shown to add accuracy.

## 3. Structural facts already measured

NFL margins of exactly 3 and 7 occur in 14.2% and 8.3% of games against 5.7% and 5.2% under a discretised normal; hockey and baseball one-goal and one-run margins are 39.9% and 28.1% against 28.7% and 17.4% ([simulation review](research/verification/framework_change_2026-10-22-1/SIMULATION_REVIEW.md)). These are distribution shapes, handled by the margin table and the simulators ([SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md)), not by adjustments.

## 4. What is missing, and what would fill it

Every `NOT_ESTIMATED` row names its data. The largest gap is player availability: the store's `PLAYER_AVAILABILITY.csv` still holds no rows (checked 2026-11-07), so no availability effect can be measured until lineups are captured with publication times at every freeze (REV-07). Prompt 7 should capture them for every game the league-day lane freezes; prompt 8 re-estimates the table between seasons. **Regime effects** were measured on 8 November 2026 (REGIME-v2, owner instruction): each archive multiplier was tested against the reference's own walk-forward forecasts on verified finals, with leave-one-season-out scoring. Four rows move a number (NBA playoffs, MLB postseason and NRL early-season totals at full size; AFL finals at half size), four are `MEASURED_NULL`, NHL and NFL stay `NOT_ESTIMATED`, and NRL six-again is retired (Part C has the table). Cup rotation still needs starting lineups and stays a `SCENARIO` row.

## 5. Use

1. Find the row for the factor and competition. No row, or `NOT_ESTIMATED`: scenario only.
2. Apply the estimate to the reference centre at the entry size its status gives; print the row id, estimate, interval and entry size in the adjustment table.
3. Never count an effect twice: a season-to-date net rating already contains the games a rested or tired team played, a player out for most of the window is already in the rating, and a reference's home edge already includes the home advantage.
4. A new estimate appends a row; an old row is never overwritten.

---

# Part C: BASE_RATES_REGISTER

*Historical register (September–October 2026). Its own status line of 16 October applies: archive-derived populations are retired for new use, and every number here needs independent online re-establishment before any reuse. It is not a card input: current competition numbers are in Part A, adjustment sizes in Part B. The full original (every table, query and maintenance note) is kept verbatim at [archive/consolidation_2026-11-07/merged_sources/BASE_RATES_REGISTER.md](archive/consolidation_2026-11-07/merged_sources/BASE_RATES_REGISTER.md).*

**Regime flags (PRD-07).** The flags (NONE, FINALS_COMPRESSION, EARLY_SEASON, CUP_ROTATION, RULE_CHANGE:<verified name>) still label a card's context ([RULES_REFERENCE](RULES_REFERENCE.md#part-b-selection_rules) Part B §6). The multipliers below were estimated from the retired results archive on 2026-10-09 (season-block bootstrap of the ratio of mean game totals over each league's last 25 seasons) and are kept as historical reference; a regime effect enters a card only as an effect-table row (Part B) or a declared `SCENARIO` row, never as a multiplier from this table.

**Tested 2026-11-08 (REGIME-v2; corrected the same day as REGIME-v3).** The first test (leave one season out) used later seasons to evaluate earlier ones; it is exploratory. Confirmation is the chronological test: each season's multiplier is fitted on earlier seasons only. A raw ratio of early-season (or finals) scoring to the season mean is not what a card needs: the reference already follows the season to date, so the question is whether it is biased in that regime. Each row below was tested on verified finals against a walk-forward replication of the reference (standings from earlier games only, prior-season league mean blended in), with each held-out season's multiplier fitted on the other seasons and the paired CRPS and Brier bootstrapped by season. Study, code and data hashes: [regime_study](research/verification/framework_change_2026-11-08-1/regime_study/REGIME_STUDY.md).

| League | Flag | Archive (2026-10-09) | Bias of the reference in the regime (95% CI) | Held-out result | Effect row and entry |
|---|---|---:|---|---|---|
| NBA | FINALS_COMPRESSION | 0.970 | −4.5% (−6.0 to −3.1), 507 games | Chronological: CRPS and Brier better, 5 of 5 later seasons | `E-NBA-PLAYOFF-TOTAL-R2`, FULL |
| NBA | EARLY_SEASON | 0.988 | −0.3% (−0.7 to +0.3), 1,231 | No gain; 0.988 made every window worse | `E-NBA-EARLY-TOTAL`, none |
| MLB | FINALS_COMPRESSION | 0.924 | −10.9% (−13.9 to −7.7), 248 | Chronological on the proxy: better, 5 of 5; not tested on MLB-CYCLE-4 | `E-MLB-POSTSEASON-TOTAL-R2`, HALF |
| MLB | EARLY_SEASON | 1.000 | −1.4% (−3.4 to +0.4), 1,962 | Slight gain, interval of the size contains zero | `E-MLB-EARLY-TOTAL`, none |
| AFL | FINALS_COMPRESSION | 0.943 | −3.2% (−6.1 to −0.5), 101 | Chronological: not confirmed, 4 of 10 | `E-AFL-FINALS-TOTAL-R2`, HALF |
| AFL | EARLY_SEASON | 1.000 | −0.7% (−1.2 to −0.1), 373 | Smaller than the reference's −1.7% bias elsewhere | `E-AFL-EARLY-TOTAL`, none |
| NRL | EARLY_SEASON | 0.938 | −2.5% (−4.5 to −0.4), 177 | Chronological: Brier −0.0019 (−0.0049 to +0.0019), not confirmed | `E-NRL-EARLY-TOTAL-R2`, HALF |
| NRL | FINALS_COMPRESSION | 0.938 | −7.5% (−16.1 to +1.8), 54 | No gain, 3 of 6 | `E-NRL-FINALS-TOTAL`, none |
| NRL | RULE_CHANGE:six_again | 1.121 | — | Every season since 2020 is under the rule | Retired (`E-NRL-SIX-AGAIN`) |
| NHL | both | 1.024, 0.917 | Not testable: one verified season, no playoffs | — | `E-NEED-REGIME-NHL`, scenario |
| NFL | FINALS_COMPRESSION | 1.057 | Not testable: no verified history, no permitted bulk source | — | `E-NEED-REGIME-NFL`, scenario |
| WNBA | both | 1.000 | — | Recommended 1.000: nothing to apply | — |

*Archive table (historical, 2026-10-09):*

| League | Flag | Estimate | 95% CI | Seasons | Recommended |
|---|---|---:|---|---:|---:|
| AFL | EARLY_SEASON | 1.013 | 0.998–1.028 | 25 | 1.000 |
| AFL | FINALS_COMPRESSION | 0.943 | 0.919–0.967 | 25 | 0.943 |
| MLB | EARLY_SEASON | 0.999 | 0.975–1.024 | 25 | 1.000 |
| MLB | FINALS_COMPRESSION | 0.924 | 0.890–0.960 | 25 | 0.924 |
| NBA | EARLY_SEASON | 0.988 | 0.982–0.993 | 25 | 0.988 |
| NBA | FINALS_COMPRESSION | 0.970 | 0.961–0.980 | 25 | 0.970 |
| NFL | EARLY_SEASON | 1.000 | 0.982–1.018 | 25 | 1.000 |
| NFL | FINALS_COMPRESSION | 1.057 | 1.029–1.087 | 25 | 1.057 |
| NHL | EARLY_SEASON | 1.024 | 1.006–1.040 | 24 | 1.024 |
| NHL | FINALS_COMPRESSION | 0.917 | 0.884–0.955 | 24 | 0.917 |
| NRL | EARLY_SEASON | 0.938 | 0.913–0.963 | 25 | 0.938 |
| NRL | FINALS_COMPRESSION | 0.938 | 0.907–0.973 | 25 | 0.938 |
| NRL | RULE_CHANGE:six_again | 1.121 | 1.087–1.152 | 5+5 | 1.121 |
| WNBA | EARLY_SEASON | 0.998 | 0.988–1.010 | 25 | 1.000 |
| WNBA | FINALS_COMPRESSION | 1.010 | 0.994–1.027 | 25 | 1.000 |

Not estimable from the archive: `CUP_ROTATION` (needs starting lineups) and `RULE_CHANGE:kbl_foreign_player_2026_27` (no games played under it).

**Contents of the archived register** (its original section titles; the "consumed by" rules some of them name, such as RULES_GENERAL §16, G-L24, G-L19 and baseball controls 35 and 37, were archived or rewritten before v24 and no longer read these numbers, checked 2026-11-07):

- What belongs here, and what does not
- Why it exists
- 1. Handicap / margin bands — consumed by `G-L24` (RULES_GENERAL (archived) §16.13(e))
- 2. Endpoint / overtime mixtures — consumed by `RULES_BASEBALL.md` control 37 and `G-L19`
- 3. Total-runs / total-points geometry — consumed by `RULES_BASEBALL.md` control 35 and `CURRENT_RULES.md` §D7
- Venue reference distributions (2026, through 16 Sep)
- 4. Round / competition reference rates — evidence only, not identity inputs
- 5. MLB 2026 doubleheader and one-run rates — derived 2026-09-24(f)
- 6. Cricket and tennis records carried from the 2026-09-22 cohort audit (added 2026-09-25)
- 7. Cross-sport reference rates — derived 2026-09-25
- 7.1 Basketball — regular season
- 7.2 NHL 2025-26 — regular season, `api-web.nhle.com/v1/score/{date}` (n = 1,312)
- 7.3 EPL 2025-26 (n = 380; scoreboard plus match summaries)
- 7.4 Tennis 2026 — ESPN tennis scoreboard, completed singles, 1 Jan – 24 Sep
- 7.5 MLB 2026 — all parks, first five innings, width (statsapi; 9-inning Finals, n = 2,373 through 24 Sep)
- 7.6 Width calibration of issued cards — descriptive, hindsight (2026-09-24 cohort, P-495–P-509)
- 7.7 NFL, AFL and NRL references, TB-1 widths and underdog-cushion cover rates (derived 2026-09-25(e))
- 7.8 Predictability map — how often a STRONG pick exists, by league (derived 2026-09-26(e); EXPLORATORY, descriptive)
- Maintenance

---

# Part D: LEAGUE_PROFILES

*LP-2026.10.16-v4.* Profiles derived from the retired store are `RETIRED_SOURCE / NOT_ADMITTED` for new cards; their rows are preserved in [archive/superseded_2026-10-16-3/LEAGUE_PROFILES.md](archive/superseded_2026-10-16-3/LEAGUE_PROFILES.md) and git for historical interpretation and are never a fallback. Current per-competition means and widths are Part A; a competition's tier and declared reference are in [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md) and `research/competition_parameters/REFERENCE_CHOICE.csv`. A competition without a Part A row is researched online as an exact-competition population under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md): season, stage and endpoint, IDs, expected, collected and eligible fixture counts, true n, dates, known-at and corrections, missingness, source URLs and capture hashes, and derivation. Means, spreads, covariance and extras are computed only where verified fields support them: no borrowed league constants and no periods inferred from totals. Until then the competition's status is `DATA_PENDING` and unsupported values stay `NOT_ESTIMATED`; a game can still use reviewed web HISTORY.csv and COMPETITION_SOURCE.csv rows without a shared profile, with its qualitative research and baseline attempt kept. Such numbers are printed on the card with their provenance and enter Part A only through prompt 7 and prompt 8; a refresh is not predictive qualification.


## v24.15 operational and parameter amendment

The v24.15 owner-authorized statistical release loads 32 measured soccer competition rows and its declared family prior; originals remain archived. The upload builder does not silently modify this table. The explicit --install-soccer release option requires the reviewed prior SHA and an unoccupied archive destination. Existing card probabilities and frozen model bundles are unchanged. See [EXT-v3](EXTERNAL_RESEARCH_PROTOCOL_V3.md).

# Cohort tables — retrospective 2026-10-16 (P-577 to P-600)

Every input row and every computed table of [RETROSPECTIVE_REPORT.md](RETROSPECTIVE_REPORT.md). Inputs are the committed settlement row inventories named in [DATA_INVENTORY.md](DATA_INVENTORY.md); nothing was re-graded. Wilson intervals treat rows as independent and therefore understate uncertainty (rows of one card share an event). Brier = (p − y)²; log loss = −ln p for WIN, −ln(1 − p) for LOSS; PUSH rows are excluded from decisive scores. Arithmetic ran in a helper outside the repository using `ml.core.metrics` (Wilson, week-block interval, logistic calibration fit); the formulas are those of SCORING_AND_VALIDATION §§3–5 and can be redone by hand from the rows below.

## 0. Input rows, counted cohorts C1–C3 (original ranks 1–4)

| Card | Cohort | Sport | Rank | Proposition | p_card | BASELINE_P | Grade | Evidence | Timing | ISO week |
|---|---|---|---:|---|---:|---:|---|---|---|---|
| P-577 | C1_PRE_V10 | Tennis | 1 | Combined total games Under 33.5 — completed best-of-three match (tiebreak set = 13 games) | 0.899 | — | LOSS | B | PRE_SCHEDULED_ESTIMATE | 2026-W41 |
| P-577 | C1_PRE_V10 | Tennis | 2 | Brandon Nakashima +5.5 aggregate games — completed best-of-three match | 0.897 | — | WIN | B | PRE_SCHEDULED_ESTIMATE | 2026-W41 |
| P-577 | C1_PRE_V10 | Tennis | 3 | Combined total games Over 17.5 — completed best-of-three match | 0.888 | — | WIN | B | PRE_SCHEDULED_ESTIMATE | 2026-W41 |
| P-577 | C1_PRE_V10 | Tennis | 4 | Combined total games Under 32.5 — completed best-of-three match | 0.869 | — | LOSS | B | PRE_SCHEDULED_ESTIMATE | 2026-W41 |
| P-578 | C1_PRE_V10 | Basketball | 1 | Total points Under 258.5, NBA preseason full game incl. OT | 0.897 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-578 | C1_PRE_V10 | Basketball | 2 | Total points Over 198.5, NBA preseason full game incl. OT | 0.896 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-578 | C1_PRE_V10 | Basketball | 3 | Houston Rockets +21.5, NBA preseason full game incl. OT | 0.893 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-578 | C1_PRE_V10 | Basketball | 4 | Dallas Mavericks +24.5, NBA preseason full game incl. OT | 0.887 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-579 | C1_PRE_V10 | Basketball | 1 | Combined total points Under 197.5 — full game incl. OT | 0.8966 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-579 | C1_PRE_V10 | Basketball | 2 | Combined total points Over 147.5 — full game incl. OT | 0.8934 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-579 | C1_PRE_V10 | Basketball | 3 | UCAM Murcia +13.5 point handicap — full game incl. OT | 0.8891 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-579 | C1_PRE_V10 | Basketball | 4 | Combined total points Over 148.5 — full game incl. OT | 0.8839 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-580 | C2_V10 | Ice Hockey | 1 | `margin_lib+2.5_full`: Liberec +2.5 goals, full match including OT/SO | 0.891554 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-580 | C2_V10 | Ice Hockey | 2 | `total_under8.5_full`: combined total Under 8.5 goals, full match including OT/SO | 0.872092 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-580 | C2_V10 | Ice Hockey | 3 | `margin_motor+2.5_full`: Motor +2.5 goals, full match including OT/SO | 0.828332 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-580 | C2_V10 | Ice Hockey | 4 | `total_under7.5_full`: combined total Under 7.5 goals, full match including OT/SO | 0.810266 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-581 | C2_V10 | Soccer | 1 | Combined total goals Under 4.5 — regulation | 0.8245 | 0.8303 | LOSS | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-581 | C2_V10 | Soccer | 2 | Combined total goals Over 1.5 — regulation | 0.7924 | 0.7869 | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-581 | C2_V10 | Soccer | 3 | Either team wins in regulation (12; draw loses) | 0.7553 | — | WIN | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-581 | C2_V10 | Soccer | 4 | Combined total goals Under 3.5 — regulation | 0.6597 | 0.6676 | LOSS | A | LATE_START_UNVERIFIED | 2026-W41 |
| P-582 | C2_V10 | Soccer | 1 | `ft:under:5.5` Full time total goals Under 5.5 (regulation) | 0.8893 | 0.9392 | WIN | A | PRE_SCHEDULED_UNVERIFIED | 2026-W41 |
| P-582 | C2_V10 | Soccer | 2 | `firsthalf:under:2.5` First-half combined total goals Under 2.5 (regulation) | 0.8795 | 0.8816 | WIN | A | PRE_SCHEDULED_UNVERIFIED | 2026-W41 |
| P-582 | C2_V10 | Soccer | 3 | `ft:over:1.5` Full time total goals Over 1.5 (regulation) | 0.8347 | 0.7603 | WIN | A | PRE_SCHEDULED_UNVERIFIED | 2026-W41 |
| P-582 | C2_V10 | Soccer | 4 | `mancity:+1.5` Man City +1.5 goals (regulation) | 0.8256 | — | WIN | A | PRE_SCHEDULED_UNVERIFIED | 2026-W41 |
| P-585 | C3_SUPPLIED_FIRST_V1 | Tennis | 1 | Total match games Over 23.5 | 0.525 | — | LOSS | B | PRE_SCHEDULED_ESTIMATE | 2026-W42 |
| P-585 | C3_SUPPLIED_FIRST_V1 | Tennis | 2 | Menšík −2.5 total games | 0.5161 | — | LOSS | B | PRE_SCHEDULED_ESTIMATE | 2026-W42 |
| P-585 | C3_SUPPLIED_FIRST_V1 | Tennis | 3 | Gea +2.5 total games | 0.4839 | — | WIN | B | PRE_SCHEDULED_ESTIMATE | 2026-W42 |
| P-585 | C3_SUPPLIED_FIRST_V1 | Tennis | 4 | Total match games Under 23.5 | 0.475 | — | WIN | B | PRE_SCHEDULED_ESTIMATE | 2026-W42 |
| P-586 | C3_SUPPLIED_FIRST_V1 | Basketball | 1 | Manresa +13.5 points | 0.5837 | — | WIN | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-586 | C3_SUPPLIED_FIRST_V1 | Basketball | 2 | Combined Under 178.5 points | 0.5331 | — | LOSS | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-586 | C3_SUPPLIED_FIRST_V1 | Basketball | 3 | Combined Over 178.5 points | 0.4669 | — | WIN | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-586 | C3_SUPPLIED_FIRST_V1 | Basketball | 4 | Bahçeşehir −13.5 points | 0.4163 | — | LOSS | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-587 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 1 | Flames +1.5 | 0.630112 | 0.6989 | WIN | A | LATE_START_UNVERIFIED | 2026-W42 |
| P-587 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 2 | Ducks ML | 0.62263 | 0.5221 | LOSS | A | LATE_START_UNVERIFIED | 2026-W42 |
| P-587 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 3 | Combined Total Goals: Over 6.0 Goals | 0.514553 | 0.5234 | PUSH | A | LATE_START_UNVERIFIED | 2026-W42 |
| P-587 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 4 | Combined Total Goals: Under 6.0 Goals | 0.485447 | 0.4766 | PUSH | A | LATE_START_UNVERIFIED | 2026-W42 |
| P-588 | C3_SUPPLIED_FIRST_V1 | Basketball | 1 | Combined Total Points: Under 228.5 Points | 0.609554 | — | WIN | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-588 | C3_SUPPLIED_FIRST_V1 | Basketball | 2 | Warriors -2.5 points | 0.546734 | — | WIN | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-588 | C3_SUPPLIED_FIRST_V1 | Basketball | 3 | Lakers +2.5 points | 0.453266 | — | LOSS | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-588 | C3_SUPPLIED_FIRST_V1 | Basketball | 4 | Combined Total Points: Over 228.5 Points | 0.390446 | — | LOSS | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-589 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 1 | Bruins ML | 0.59308 | 0.4779 | WIN | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-589 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 2 | Combined Total Goals: Under 6.5 Goals | 0.562676 | 0.5312 | LOSS | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-589 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 3 | Combined Total Goals: Over 6.5 Goals | 0.437324 | 0.4688 | WIN | B | LATE_START_UNVERIFIED | 2026-W42 |
| P-589 | C3_SUPPLIED_FIRST_V1 | Ice Hockey | 4 | Sharks ML | 0.40692 | 0.5221 | LOSS | B | LATE_START_UNVERIFIED | 2026-W42 |

## 0b. Input rows, legacy retained cohort P-590–P-600 (EFFECTIVE_SETTLEMENT_ROWS.csv)

| Event | Contract | analyst p | Original rank type | Sporting grade | Evidence class |
|---|---|---:|---|---|---|
| P-590 | West Indies powerplay Under 57.5 runs | 0.5830 | ORIGINAL_RANK_1 | LOSS | OWNER_TEAM_AND_REPORT |
| P-590 | West Indies innings Under 200.5 runs | 0.5690 | ORIGINAL_RANK_2_INFORMATIONAL | LOSS | OWNER_TEAM_AND_REPORT |
| P-590 | West Indies innings Over 200.5 runs | 0.4310 | ORIGINAL_RANK_3 | WIN | OWNER_TEAM_AND_REPORT |
| P-590 | West Indies powerplay Over 57.5 runs | 0.4170 | ORIGINAL_RANK_4 | WIN | OWNER_TEAM_AND_REPORT |
| P-591 | Combined Under 172.5 points | 0.6390 | ORIGINAL_RANK_1 | WIN | ABA_COMPETITION_RECAP |
| P-591 | U-BT Cluj-Napoca −4.5 points | 0.5510 | ORIGINAL_RANK_2 | WIN | ABA_COMPETITION_RECAP |
| P-591 | Šiauliai +4.5 points | 0.4490 | ORIGINAL_RANK_3 | LOSS | ABA_COMPETITION_RECAP |
| P-591 | Combined Over 172.5 points | 0.3610 | ORIGINAL_RANK_4 | LOSS | ABA_COMPETITION_RECAP |
| P-592 | Combined Under 137.5 points | 0.5185 | ORIGINAL_RANK_1 | LOSS | BOTH_CLUBS_REPORT |
| P-592 | Zaragoza Women −6.5 points | 0.5146 | ORIGINAL_RANK_2 | LOSS | BOTH_CLUBS_REPORT |
| P-592 | Basket Landes Women +6.5 points | 0.4854 | ORIGINAL_RANK_3 | WIN | BOTH_CLUBS_REPORT |
| P-592 | Combined Over 137.5 points | 0.4815 | ORIGINAL_RANK_4 | WIN | BOTH_CLUBS_REPORT |
| P-593 | First-half combined goals Over 0.5 | 0.7578 | ANALYST_ONLY | LOSS | OFFICIAL_RSL_MATCH_RECAP |
| P-593 | First-half combined goals Under 0.5 | 0.2422 | ANALYST_ONLY | WIN | OFFICIAL_RSL_MATCH_RECAP |
| P-593 | Full-time combined goals Over 2.5 | 0.6099 | ANALYST_ONLY | LOSS | OFFICIAL_RSL_MATCH_RECAP |
| P-593 | Full-time combined goals Under 2.5 | 0.3901 | ANALYST_ONLY | WIN | OFFICIAL_RSL_MATCH_RECAP |
| P-593 | Full-time combined corners Over 10.5 | 0.5401 | ANALYST_ONLY | LOSS | OFFICIAL_RSL_MATCH_RECAP |
| P-593 | Full-time combined corners Under 10.5 | 0.4599 | ANALYST_ONLY | WIN | OFFICIAL_RSL_MATCH_RECAP |
| P-594 | Samsung +1.5 points | 0.5352 | ANALYST_DIAGNOSTIC_2 | WIN | YONHAP_NEWS_WIRE_PLUS_SCORE_OWNER |
| P-594 | LG −1.5 points | 0.4648 | ANALYST_DIAGNOSTIC_3 | LOSS | YONHAP_NEWS_WIRE_PLUS_SCORE_OWNER |
| P-594 | Combined Over 160.5 points | 0.4219 | ANALYST_DIAGNOSTIC_4 | WIN | YONHAP_NEWS_WIRE_PLUS_SCORE_OWNER |
| P-594 | Combined Under 160.5 points | 0.5781 | ANALYST_DIAGNOSTIC_1 | LOSS | YONHAP_NEWS_WIRE_PLUS_SCORE_OWNER |
| P-595 | Zidanšek −3.5 games | 0.4726 | ANALYST_ONLY | WIN | TWO_SPECIALIST_PROVIDERS |
| P-595 | Steur +3.5 games | 0.5274 | ANALYST_ONLY | LOSS | TWO_SPECIALIST_PROVIDERS |
| P-595 | Total games Over 20.5 | 0.4667 | ANALYST_ONLY | LOSS | TWO_SPECIALIST_PROVIDERS |
| P-595 | Total games Under 20.5 | 0.5333 | ANALYST_ONLY | WIN | TWO_SPECIALIST_PROVIDERS |
| P-596 | Arlan Kokshetau +1.5 goals | 0.6370 | ANALYST_ONLY | WIN | OFFICIAL_CLUB_SCHEDULE |
| P-596 | Saryarka ML | 0.6034 | ANALYST_ONLY | UNRESOLVED | OFFICIAL_CLUB_SCHEDULE |
| P-596 | Combined goals Over 5.5 | 0.5893 | ANALYST_ONLY | WIN | OFFICIAL_CLUB_SCHEDULE |
| P-596 | Combined goals Under 5.5 | 0.4107 | ANALYST_ONLY | LOSS | OFFICIAL_CLUB_SCHEDULE |
| P-597 | Alytus ML | — | NO_NUMERIC_RANK | WIN | OFFICIAL_NKL_MATCH_RECAP |
| P-597 | Vytis ML | — | NO_NUMERIC_RANK | LOSS | OFFICIAL_NKL_MATCH_RECAP |
| P-597 | Combined Over 168.5 points | — | NO_NUMERIC_RANK | WIN | OFFICIAL_NKL_MATCH_RECAP |
| P-597 | Combined Under 168.5 points | — | NO_NUMERIC_RANK | LOSS | OFFICIAL_NKL_MATCH_RECAP |
| P-598 | Huima −8.5 ML (ambiguous spread vs ML) | — | NO_NUMERIC_RANK | UNRESOLVED | TWO_SECONDARY_RESULTS |
| P-598 | NMKY +8.5 points | — | NO_NUMERIC_RANK | WIN | TWO_SECONDARY_RESULTS |
| P-598 | Combined Over 162.5 points | — | NO_NUMERIC_RANK | WIN | TWO_SECONDARY_RESULTS |
| P-598 | Combined Under 162.5 points | — | NO_NUMERIC_RANK | LOSS | TWO_SECONDARY_RESULTS |
| P-599 | Seahawks −2.5 points | 0.5068 | ANALYST_DIAGNOSTIC_2 | LOSS | SINGLE_POSTGAME_SECONDARY_REPORT |
| P-599 | Broncos +2.5 points | 0.4932 | ANALYST_DIAGNOSTIC_3 | WIN | SINGLE_POSTGAME_SECONDARY_REPORT |
| P-599 | Combined Over 40.5 points | 0.6436 | ANALYST_DIAGNOSTIC_1 | LOSS | SINGLE_POSTGAME_SECONDARY_REPORT |
| P-599 | Combined Under 40.5 points | 0.3564 | ANALYST_DIAGNOSTIC_4 | WIN | SINGLE_POSTGAME_SECONDARY_REPORT |
| P-600 | Thunder −2.5 points | 0.3658 | ANALYST_DIAGNOSTIC_3 | LOSS | TWO_POSTGAME_SOURCES |
| P-600 | Rockets +2.5 points | 0.6342 | ANALYST_DIAGNOSTIC_2 | WIN | TWO_POSTGAME_SOURCES |
| P-600 | Combined Over 227.5 points | 0.6631 | ANALYST_DIAGNOSTIC_1 | LOSS | TWO_POSTGAME_SOURCES |
| P-600 | Combined Under 227.5 points | 0.3369 | ANALYST_DIAGNOSTIC_4 | WIN | TWO_POSTGAME_SOURCES |

## 1. Primary rows (original Ranks 1–2), counted cohorts C1–C3

| Cohort | Cards | Decisive primary rows | W–L | Rate (Wilson 95%) | Mean stated p | Expected wins | z | Brier | Log loss | In-sample climatology Brier | Skill vs climatology |
|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| C1 PRE_V10 (P-577–P-579) | 3 | 6 | 5–1 | 83.3% (43.6–97.0%) | 89.6% | 5.38 | -0.51 | 0.1437 | 0.4736 | 0.1389 | -0.03 |
| C2 V10 (P-580–P-582) | 3 | 6 | 5–1 | 83.3% (43.6–97.0%) | 85.8% | 5.15 | -0.18 | 0.1296 | 0.4117 | 0.1389 | +0.07 |
| C1+C2 (ceiling ladder) | 6 | 12 | 10–2 | 83.3% (55.2–95.3%) | 87.7% | 10.53 | -0.47 | 0.1367 | 0.4427 | 0.1389 | +0.02 |
| C3 SUPPLIED_FIRST_V1 (P-585–P-589) | 5 | 10 | 5–5 | 50.0% (23.7–76.3%) | 57.2% | 5.72 | -0.46 | 0.2364 | 0.6655 | 0.2500 | +0.05 |
| All counted (C1–C3) | 11 | 22 | 15–7 | 68.2% (47.3–83.6%) | 73.9% | 16.25 | -0.65 | 0.1820 | 0.5440 | 0.2169 | +0.16 |

### By slot

| Cohort | Rank 1 W–L (Wilson) | Rank 2 W–L (Wilson) | Ranks 3–4 W–L (Wilson; PUSH excluded) |
|---|---|---|---|
| C1+C2 | 4–2 (30.0–90.3%) | 6–0 (61.0–100.0%) | 10–2 (55.2–95.3%) |
| C3 | 4–1 (37.6–96.4%) | 1–4 (3.6–62.4%) | 4–4 (21.5–78.5%) |
| All C1–C3 | 8–3 (43.4–90.3%) | 7–4 (35.4–84.8%) | 14–6 (48.1–85.5%) |

## 2. Card classes, Hit@2 and joint failure

| Card | Cohort | Sport / competition | R1 | R2 | Class | Stated P(both lose) | Mechanically protected | Gate label | Timing |
|---|---|---|---|---|---|---:|---|---|---|
| P-577 | C1_PRE_V10 | Tennis / ATP Shanghai | LOSS | WIN | SPLIT | 0.00% | YES | RANK1_UNSTABLE | PRE_SCHEDULED_ESTIMATE |
| P-578 | C1_PRE_V10 | Basketball / NBA preseason | WIN | WIN | ALL_WON | 0.00% | YES | RANK1_UNSTABLE | LATE_START_UNVERIFIED |
| P-579 | C1_PRE_V10 | Basketball / Liga ACB | WIN | WIN | ALL_WON | 0.00% | YES | RANK1_UNSTABLE | LATE_START_UNVERIFIED |
| P-580 | C2_V10 | Ice Hockey / Czech Extraliga | WIN | WIN | ALL_WON | 1.86% | NO | RANK1_UNSTABLE | LATE_START_UNVERIFIED |
| P-581 | C2_V10 | Soccer / Danish Superliga | LOSS | WIN | SPLIT | 0.00% | YES | RANK1_UNSTABLE | LATE_START_UNVERIFIED |
| P-582 | C2_V10 | Soccer / Premier League | WIN | WIN | ALL_WON | 5.18% | NO | RANK1_UNSTABLE | PRE_SCHEDULED_UNVERIFIED |
| P-585 | C3_SUPPLIED_FIRST_V1 | Tennis / ATP Shanghai | LOSS | LOSS | ALL_LOST | 12.82% | NO | RANK1_UNSTABLE | PRE_SCHEDULED_ESTIMATE |
| P-586 | C3_SUPPLIED_FIRST_V1 | Basketball / EuroCup | WIN | LOSS | SPLIT | 19.59% | NO | FAIL_FLOOR | LATE_START_UNVERIFIED |
| P-587 | C3_SUPPLIED_FIRST_V1 | Ice Hockey / NHL | WIN | LOSS | SPLIT | 0.00% | YES | RANK1_UNSTABLE | LATE_START_UNVERIFIED |
| P-588 | C3_SUPPLIED_FIRST_V1 | Basketball / NBA preseason | WIN | WIN | ALL_WON | 18.06% | NO | RANK1_UNSTABLE | LATE_START_UNVERIFIED |
| P-589 | C3_SUPPLIED_FIRST_V1 | Ice Hockey / NHL | WIN | LOSS | SPLIT | 17.83% | NO | RANK1_UNSTABLE | LATE_START_UNVERIFIED |

Hit@2 (≥1 primary win): 10/11 cards. Mechanically protected: 5 (P-577, P-578, P-579, P-581, P-587), Hit@2 5/5 by construction. Not protected: 6, Hit@2 5/6; stated mean P(both lose) 12.56%, expected ALL_LOST 0.75, observed 1.

## 3. Calibration bins, all numeric original rows C1–C3 (ranks 1–4, PUSH excluded)

| Stated p bin | Rows | Mean stated | Realised | Wilson 95% |
|---|---:|---:|---:|---|
| 0–50% | 8 | 44.1% | 50.0% | 21.5–78.5% |
| 50–60% | 7 | 55.1% | 42.9% | 15.8–75.0% |
| 60–70% | 4 | 63.0% | 50.0% | 15.0–85.0% |
| 70–80% | 2 | 77.4% | 100.0% | 34.2–100.0% |
| 80–90% | 21 | 87.4% | 85.7% | 65.4–95.0% |
| 90–100% | 0 | — | — | — |

Logistic recalibration on all 42 decisive rows (descriptive, dependent rows): intercept -0.17 (SE 0.48), slope 1.09 (SE 0.42); calibration-in-the-large +1.9 points; ECE 8.2 points.

## 4. Frozen same-row baseline pairs (BASELINE_P numeric in the original)

| Card | Rank | Proposition | p_card | BASELINE_P | Outcome | Brier card | Brier baseline | Difference | ISO week |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| P-581 | 1 | Combined total goals Under 4.5 — regulation | 0.8245 | 0.8303 | LOSS | 0.6798 | 0.6894 | -0.0096 | 2026-W41 |
| P-581 | 2 | Combined total goals Over 1.5 — regulation | 0.7924 | 0.7869 | WIN | 0.0431 | 0.0454 | -0.0023 | 2026-W41 |
| P-581 | 4 | Combined total goals Under 3.5 — regulation | 0.6597 | 0.6676 | LOSS | 0.4352 | 0.4457 | -0.0105 | 2026-W41 |
| P-582 | 1 | `ft:under:5.5` Full time total goals Under 5.5 (regulation) | 0.8893 | 0.9392 | WIN | 0.0123 | 0.0037 | +0.0086 | 2026-W41 |
| P-582 | 2 | `firsthalf:under:2.5` First-half combined total goals Under  | 0.8795 | 0.8816 | WIN | 0.0145 | 0.0140 | +0.0005 | 2026-W41 |
| P-582 | 3 | `ft:over:1.5` Full time total goals Over 1.5 (regulation) | 0.8347 | 0.7603 | WIN | 0.0273 | 0.0575 | -0.0301 | 2026-W41 |
| P-587 | 1 | Flames +1.5 | 0.6301 | 0.6989 | WIN | 0.1368 | 0.0906 | +0.0462 | 2026-W42 |
| P-587 | 2 | Ducks ML | 0.6226 | 0.5221 | LOSS | 0.3877 | 0.2726 | +0.1151 | 2026-W42 |
| P-589 | 1 | Bruins ML | 0.5931 | 0.4779 | WIN | 0.1656 | 0.2726 | -0.1070 | 2026-W42 |
| P-589 | 2 | Combined Total Goals: Under 6.5 Goals | 0.5627 | 0.5312 | LOSS | 0.3166 | 0.2822 | +0.0344 | 2026-W42 |
| P-589 | 3 | Combined Total Goals: Over 6.5 Goals | 0.4373 | 0.4688 | WIN | 0.3166 | 0.2822 | +0.0344 | 2026-W42 |
| P-589 | 4 | Sharks ML | 0.4069 | 0.5221 | LOSS | 0.1656 | 0.2726 | -0.1070 | 2026-W42 |

Primary rows: 8 rows on 4 events in 2 ISO weeks; mean Brier card 0.2195 vs baseline 0.2088; event-then-week mean difference +0.0107; status INSUFFICIENT_EVIDENCE (k = 2 weeks).
All rows with a baseline: 12 rows on 4 events; mean difference +0.0075; status INSUFFICIENT_EVIDENCE.
Baseline coverage of decisive primary rows: 8/22.

## 5. Timing strata (counted primary rows)

| Timing class | Cards | W–L | Rate (Wilson) | Brier |
|---|---:|---|---|---:|
| LATE_START_UNVERIFIED | 8 | 12–4 | 75.0% (50.5–89.8%) | 0.1635 |
| PRE_SCHEDULED_ESTIMATE | 2 | 1–3 | 25.0% (4.6–69.9%) | 0.3402 |
| PRE_SCHEDULED_UNVERIFIED | 1 | 2–0 | 100.0% (34.2–100.0%) | 0.0134 |

## 6. Evidence grade (counted primary rows)

| Grade | Rows | W–L |
|---|---:|---|
| A | 12 | 10–2 |
| B | 10 | 5–5 |

## 7. Sport (counted primary rows)

| Sport | Cards | Rank 1 W–L | Rank 2 W–L |
|---|---:|---|---|
| Basketball | 4 | 4–0 | 3–1 |
| Ice Hockey | 3 | 3–0 | 1–2 |
| Soccer | 2 | 1–1 | 2–0 |
| Tennis | 2 | 0–2 | 1–1 |

## 8. Legacy retained cohort P-590–P-600 (NOT_PRIMARY analyst diagnostics)

Supplied propositions: 46 on 11 events; grades WIN 23, LOSS 21, UNRESOLVED 2. Numeric analyst rows with a decisive grade: 37 (W 19 / L 18); mean squared error 0.2861; mean log loss 0.7704. Non-numeric: P-597, P-598 (8 rows); P-596 Saryarka ML numeric but UNRESOLVED.

| Event | Highest analyst p row | p | Outcome |
|---|---|---:|---|
| P-590 | West Indies powerplay Under 57.5 runs | 0.5830 | LOSS |
| P-591 | Combined Under 172.5 points | 0.6390 | WIN |
| P-592 | Combined Under 137.5 points | 0.5185 | LOSS |
| P-593 | First-half combined goals Over 0.5 | 0.7578 | LOSS |
| P-594 | Combined Under 160.5 points | 0.5781 | LOSS |
| P-595 | Total games Under 20.5 | 0.5333 | WIN |
| P-596 | Arlan Kokshetau +1.5 goals | 0.6370 | WIN |
| P-599 | Combined Over 40.5 points | 0.6436 | LOSS |
| P-600 | Combined Over 227.5 points | 0.6631 | LOSS |

Highest-p analyst row per event: 3/9 won (12.1–64.6%); mean stated 61.7%. These rows were never primary picks and enter no T2, Brier, calibration or feedback cohort.

| Analyst p bin | Rows | Mean stated | Realised |
|---|---:|---:|---:|
| 0–40% | 6 | 34.2% | 66.7% |
| 40–50% | 12 | 45.4% | 66.7% |
| 50–60% | 12 | 54.6% | 33.3% |
| 60–70% | 6 | 63.8% | 50.0% |
| 70–100% | 1 | 75.8% | 0.0% |

## 9. Expected score against final (cards that printed a centre)

Error = final − expected; z uses the card's own SD (P-587 SDs back-computed from the import's readback of error and z).

| Card | Sport | Total exp (SD) | Total final | Error | z | Margin exp (SD) | Margin final | Error | z |
|---|---|---|---:|---:|---:|---|---:|---:|---:|
| P-577 | Tennis | 24.37 (6.18) | 35 | +10.630 | +1.72 | -0.41 (4.59) | +3 | +3.410 | +0.74 |
| P-578 | Basketball | 228.37 (23.85) | 247 | +18.630 | +0.78 | +1.78 (18.81) | -17 | -18.780 | -1.00 |
| P-579 | Basketball | 172.31 (20.03) | 167 | -5.310 | -0.27 | +4.61 (14.83) | -13 | -17.610 | -1.19 |
| P-580 | Ice Hockey | 5.6667 (2.3346) | 7 | +1.333 | +0.57 | -0.3333 (2.3805) | +1 | +1.333 | +0.56 |
| P-581 | Soccer | 2.944 (1.716) | 7 | +4.056 | +2.36 | +0.167 (1.716) | +3 | +2.833 | +1.65 |
| P-582 | Soccer | 3.246 (1.802) | 3 | -0.246 | -0.14 | -0.116 (1.802) | -3 | -2.884 | -1.60 |
| P-585 | Tennis | 25.467 (6.03) | 23 | -2.467 | -0.41 | -1.628 (3.923) | +3 | +4.628 | +1.18 |
| P-586 | Basketball | 176.861 (not estimated) | 188 | +11.139 | — | +10 (not estimated) | +12 | +2.000 | — |
| P-587 | Ice Hockey | 6.271 (2.533) | 6 | -0.271 | -0.11 | +0.745 (2.5) | -2 | -2.745 | -1.10 |
| P-588 | Basketball | 222.126 (23.624) | 190 | -32.126 | -1.36 | +4.292 (18.063) | +12 | +7.708 | +0.43 |
| P-589 | Ice Hockey | 6.107 (2.507) | 9 | +2.893 | +1.15 | +0.551 (2.366) | +3 | +2.449 | +1.04 |

Totals (10 with SD): mean z +0.43, mean |z| 0.89, |z| > 2 on 1 (P-581), inside the central 80% band 7/10, inside 50% 5/10. Margins (10 with SD): mean z +0.07, mean |z| 1.05, |z| > 2 on 0, inside 80% 8/10, inside 50% 2/10 (P(≤ 2 of 10 inside a correct 50% band) = 56/1024 = 0.055). A correct normal width gives mean |z| ≈ 0.80.

Legacy original-model centres (NOT_PRIMARY): P-591 total 165.48 (SD 20.04) vs 169, z +0.18; margin −6.50 (16.93) vs −19, z −0.74. P-592 total 136.65 (19.91) vs 151 after OT, z +0.72; margin +7.00 (14.94) vs +1, z −0.40. P-590 innings E[T] 193.5 vs 247 (+53.5, no SD printed); powerplay E 54.25 vs 79.

## 10. Extra-time frequency in the legacy cohort

Basketball and NFL legacy events: P-591 no OT, P-592 OT, P-594 no OT, P-597 OT, P-598 OT, P-599 OT, P-600 no OT (4 of 7); ice hockey P-596 regulation 3–3, shootout. Under an illustrative 6% per-game extra-time rate, P(≥ 4 of 7) = 0.00039; at 10% it is 0.0027. Sources: P-599 Seattle official game centre (Final/OT) corroborated by ESPN; P-597 official NKL recap; P-592 both clubs; P-598 two secondary results (owner confirmation open). The rate is improbable enough to require field-owner re-verification of every extra-time result before any training admission; it changes no grade here.

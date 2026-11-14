# READ_ONLY_RESEARCH_DRAFT — Akita Northern Happinets vs Ibaraki Robots (B.PREMIER)

**Status:** `RESEARCH-DRAFT-07 / NOT_ISSUED / NOT_FROZEN / NOT_SETTLED / NOT_GRADED`  
**Research framework:** `MDS-2026.11.11-v24.15 / CR-2026.11.11-R3 / P-2026.11.11-v24.13`, `SCV-2026.10.22-v12`, `SEL-2026.10.22-v4`.  
**GitHub read-only main:** `4d8bd1771d20974bcbfc7c694a009cd44e95a693`. Repo mini path `research/active_minis/20261109R3NEXT.md`; official mini empty and writer lease not transferred.  
**Local record-created clock:** 2026-11-11T20:55:20+11:00 (Australia/Melbourne, UTC+11), from actual container clock. Individual source-open clocks not instrumented at microsecond resolution: `SOURCE_RETRIEVAL_CLOCK_PARTIAL`.  
**Nature:** Chat-local research input only. No issued v24.15 `p_card`, no `SR-KIT` receipt, no official `EV2` manifest, no freeze/commit/ledger or GitHub mutation. Illustrative analytic figures below are not qualified/calibrated forecast probabilities.

## A1. Identity, event timing, venue, contract definitions

- **Official event key:** B.LEAGUE schedule `506570`. 2026–27 B.LEAGUE PREMIER (B.PREMIER) regular season, East division. Home **Akita Northern Happinets**, away **Ibaraki Robots**. Venue CNA Arena Akita, Japan. Official start **2026-11-11 19:05 JST (+09:00)** = **2026-11-11 10:05 UTC** = **2026-11-11 21:05 AEDT (+11:00)**. User's 21:00 AEDT is an estimate, five minutes early. Sources S1 and S2 below, both clubs corroborated. At research first check 20:45 AEDT, pre-scheduled-start page showed `VS`, no score. Actual first possession/puck status is `NOT_VERIFIED`, so no claim of formal issued pre-start freeze.
- User's exact supplied four contracts: Akita `-1.5` points; Ibaraki `+1.5` points; combined total `Over 167.5`; combined total `Under 167.5`. Informational ML for each side is derived only for comparison, **not a supplied contract**. BK-OT-1: full-game points include overtime, barring unknown operator-specific settlement terms. No spread push at ±1.5; no total push at 167.5. `rank_scope: SUPPLIED_ONLY`.
- This is **B.PREMIER** in its new 2026–27 competition regime. The wider repository `Basketball/B League` development constants are **not** independently verified as exact-scope B.PREMIER reference rows. They appear only as a sensitivity proxy in A5, not as a claimed admitted formal reference.

## A2. Recent scoring history with true windows

All results are completed 2026–27 B.PREMIER games **before 11 November 19:05 JST**. Team perspective with HOME/AWAY and season scores. Team results are primary B.LEAGUE club lists (S3, S4) and checked against independent tabulations (S5, S6). No 11-Nov fixture result used.

**Akita last ten (latest first)**

| Date JST | Opponent | Venue | For | Against | Combined | W/L |
|---|---|---|---:|---:|---:|---|
| 2026-11-08 | Shinshu | H | 96 | 101 | 197 | L |
| 2026-11-06 | Hokkaido | A | 118 | 123 | 241 | L |
| 2026-11-01 | Altiri Chiba | H | 83 | 102 | 185 | L |
| 2026-10-30 | Altiri Chiba | H | 85 | 89 | 174 | L |
| 2026-10-26 | Kyoto | A | 71 | 79 | 150 | L |
| 2026-10-24 | Yokohama BC | H | 95 | 86 | 181 | W |
| 2026-10-21 | Hiroshima | A | 84 | 98 | 182 | L |
| 2026-10-19 | Alvark Tokyo | A | 74 | 90 | 164 | L |
| 2026-10-17 | Shinshu | H | 102 | 95 | 197 | W |
| 2026-10-11 | Utsunomiya | A | 82 | 71 | 153 | W |

**Ibaraki last ten (latest first)**

| Date JST | Opponent | Venue | For | Against | Combined | W/L |
|---|---|---|---:|---:|---:|---|
| 2026-11-09 | Ryukyu | H | 80 | 72 | 152 | W |
| 2026-11-07 | Osaka | A | 86 | 68 | 154 | W |
| 2026-11-01 | Hokkaido | H | 88 | 96 | 184 | L |
| 2026-10-31 | Hokkaido | H | 101 | 69 | 170 | W |
| 2026-10-26 | Toyama | A | 83 | 61 | 144 | W |
| 2026-10-24 | Altiri Chiba | H | 102 | 87 | 189 | W |
| 2026-10-22 | Alvark Tokyo | A | 69 | 66 | 135 | W |
| 2026-10-18 | Osaka | H | 98 | 63 | 161 | W |
| 2026-10-16 | Kawasaki | A | 82 | 74 | 156 | W |
| 2026-10-11 | Nagoya D | H | 78 | 90 | 168 | L |

| Window | Akita | Ibaraki |
|---|---|---|
| L5 | n=5; points for=90.6; against=98.8; combined=189.4; over167.5=4/5 | n=5; points for=87.6; against=73.2; combined=160.8; over167.5=2/5 |
| L10 | n=10; points for=89.0; against=93.4; combined=182.4; over167.5=7/10 | n=10; points for=86.7; against=74.6; combined=161.3; over167.5=4/10 |
| L15 | n=15 season, 4–11; PPG 82.7, points allowed 90.1; L15 all game-level rows not fully enumerated in this record | n=15 subset of 16 season games NOT_RECONSTRUCTED; do not infer L15 from L16 |
| L20 | current season n=15; older season not merged into this roster regime | current season n=16; older season not merged into this roster regime |
| Full 2026–27 season | Akita 4–11, 82.7 scored, 90.1 conceded; n15 | Ibaraki 8–8, 83.6 scored, 78.4 conceded; n16 |

**Notable extreme:** Akita's 118–123 loss to Hokkaido on 6 November was **241 regulation points**, per official quarter scores 31–39 / 29–28 / 30–27 / 33–24. It was *not* an overtime game. This drives the L5 total mean and inflates recent volatility. Excluding it only as a labeled sensitivity changes Akita's other-four combined mean to 176.5; it is **not** silently discarded. S7.

**Head-to-head (2025–26 only, no current-season meeting):** Ibaraki won all four, in game totals 173 (Akita 86–87), 124 (53–71), 126 (57–69), 151 (70–81); mean 143.5, under 167.5 in 3 of 4. Historical regime/roster differences block using these four directly as a probability prior. Source S8. Older series has mixed directions; do not double-count H2H as an independent model effect.

## A3. Availability, roles, players, corroboration

- Akita **Reid Travis OUT**, registered B.LEAGUE official injury list 5 Nov, bone bruise of lumbar facet joint; not eligible for removal until at least 5 Dec. Had averaged **7.6 points and 5.2 rebounds across 9 appearances** prior to registration (S9, S10). His injury is already partly represented in last-five and season samples: **no extra numeric adjustment** without player/minute replacement evidence.
- Akita **Angelo Chol REMOVED from injury register 5 Nov**, left patellar tendinitis. This is an *eligibility-list removal*, not verification of starting or minutes; prior status remains logged, and no full-production assumption is made (S9, S10).
- Ibaraki: no current Ibaraki name appears on official 11-Nov register as viewed. This means only *no currently registered injuries identified*, not all players healthy or confirmed. The register also has a historic removal for Kohei Nakamura, July–October 2026; not a current absence. The exact dressed 12, starting fives, and full bench remain `NOT_VERIFIED`.
- Reported season leaders: Akita **Mark Smith** 24.9 points / 7.0 assists per game, **Yanni Wetzell** 16.7 points / 8.7 rebounds. Ibaraki **Vic Law** 20.5 points / 9.1 rebounds / 4.5 assists, **Tim Soares** 14.9 points, **Finn Delany** 11.7 points. These are season-role indicators, not confirmed starts (S3, S4, S5, S6).
- Key high-leverage recheck: B.LEAGUE official game centre selected-players/entry list or club match-day announcement before tip; not obtained at the documented check. `LINEUP_UNCONFIRMED` is not `NO_INJURIES`.

## A4. Tactical, coaching, venue, fatigue, travel and H2H mechanisms

- Season-adjusted pace proxy from rating and points: Akita ≈82.7/1.083=**76.4** possessions, Ibaraki ≈83.6/1.135=**73.7**. The inferred fixture pace ≈75 possessions is illustrative, not independently possession-tracked.
- Akita ORtg **108.3**, DRtg **117.7**, net **−9.4**; Ibaraki ORtg **113.5**, DRtg **106.7**, net **+6.8** (S5/S6; secondary provider formulas). Ibaraki's clear advantage is opponent scoring suppression, particularly against Akita's poor defensive shape.
- Ibaraki has made about **11.2 3PM** per game and has high assist production around 22.5 per game; Akita about **10.4 3PM**, 18.7 assists. These represent volume/creation routes, not certainty of current shooting efficiency. Akita has high recent opponent points; Ibaraki's own L10 defensive profile is markedly lower.
- Last outing Akita home **8 Nov** (3 calendar days of rest before 11-Nov), Ibaraki home **9 Nov** (2 days, then travel north from Ibaraki). Some travel/rest headwind for Ibaraki, but no quantified points value is available.
- Last year's Ibaraki 4–0 H2H is supportive directionally, but the new season roster and league format can invalidate a direct scoring conversion.

## A5. Reference attempt, baseline arithmetic, coherent contract approximation

**Actual formal code execution:** `ml reference tier`: NOT_RUN; `ml pregame reference`: NOT_RUN; `SR-KIT-v24.15` primary: NOT_RUN; `ml external init/merge`: NOT_RUN. Current competition exact-scope parameter/width is `NOT_VERIFIED`; shared v24.15 model-promotions registry has no rows beyond its header. This file is a **diagnostic normal-CDF calculation performed in the chat's container**, not the official `ANALYST_PRIMARY_V1`/`PICKS_V2` primary forecast. No synthetic N=100k Monte Carlo was claimed.

Inputs: Akita 82.7 PF, 90.1 PA (n15); Ibaraki 83.6 PF, 78.4 PA (n16). Last ten Akita 89.0 PF/93.4 PA; Ibaraki 86.7 PF/74.6 PA. Data are current-season only. Cross-match as (own attack + opponent defence)/2; blend **2/3 season, 1/3 L10** as an illustrative sensitivity (L10 overlaps season; this is not two independent samples). Add **+0.305 to home** and **−0.305 to away** (0.61-point home margin, broader v24.15 B.League family proxy, not exact B.PREMIER adjudication).

```
season Akita = (82.7 + 78.4) / 2 = 80.55
season Ibaraki = (83.6 + 90.1) / 2 = 86.85
L10 Akita = (89.0 + 74.6) / 2 = 81.80
L10 Ibaraki = (86.7 + 93.4) / 2 = 90.05
Akita centre = (2*80.55 + 81.80)/3 + 0.305 = 81.2716667
Ibaraki centre = (2*86.85 + 90.05)/3 - 0.305 = 87.6116667
TOTAL centre = 168.8833333
MARGIN (Akita - Ibaraki) centre = -6.34
Proxy SD margin = 14.94; proxy SD total = 17.66 (general B.League development family; B.PREMIER calibration absent)
```

**Arithmetic:** normal CDF directly from SciPy in a coherent bivariate normal score proxy, using independent margin and total coordinates (not a possession-level joint grid), without integer discretisation or an explicit real-overtime branch. Because the two coordinate distributions share the same expected score centre, each side's and each total's complement agree. Continuity and OT approximation are a real limitation. The probability figures are illustrative only, not independently validated.

| Market | Numeric diagnostic | Valid v24.15 `p_card` |
|---|---:|---|
| Akita ML (informational) | 33.6% | NOT_ESTIMATED |
| Ibaraki ML (informational) | 66.4% | NOT_ESTIMATED |
| Akita −1.5 | 30.0% | NOT_ESTIMATED |
| Ibaraki +1.5 | 70.0% | NOT_ESTIMATED |
| Over 167.5 | 53.1% | NOT_ESTIMATED |
| Under 167.5 | 46.9% | NOT_ESTIMATED |

The full-game total/handicap includes OT as a contract definition; arithmetic uses historical final scores, but **does not model OT as a separate period**. Such a proxy is not eligible as a kit-certified v24.15 primary forecast.

**Scenario sensitivity:** Season-only cross-match centre 167.4 / Akita −5.69 margin after same home allowance -> Ibaraki +1.5 ≈68.5%, Over 167.5 ≈49.8%. L10-season blended margin −6.34 ±2 gives Ibaraki +1.5 about **65.2–74.5%**. Total centre 168.88 ±4 gives Over ≈**44.1–62.0%**. These sensitivity widths/weight assumptions are not outcome-derived calibration. Exact probability bands are unavailable.

## A6. Supplied lines, comparison and dependence

- **Single conditional preference:** Ibaraki Robots +1.5. Its loss path is Akita winning by 2 or more points. It wins if Ibaraki wins outright or loses by one. Ibaraki has better recent results, higher estimated net rating, better defensive points conceded, and last-season H2H (directional only). No odds/tip/market anchors used.
- **Akita −1.5:** not supported given negative 2026−27 net differential and Travis absence. Home court and Ibaraki travel can moderate but not erase the gap absent a material confirmed roster report.
- **Total:** no strong pick. Base diagnostic Over 53.1%, Under 46.9%, highly sensitive to Akita 241-point outlier and Ibaraki's more defensive recent games. Akita last five 189.4 combined vs Ibaraki 160.8. 2025–26 H2H 143.5 should not be mechanically imported.
- Paired handicap sides are mutually exclusive and totals form an exact complementary pair. Correlation between Ibaraki +1.5 and Over/Under is not calculated; no multi-leg recommendation.
- Default rank is `SUPPLIED_ONLY`. Informational MLs do not displace owner-supplied handicap or total candidates.

## A7. Decision, freeze, and risk limitations

**Preferred contract:** Ibaraki Robots **+1.5 points**, *conditional, medium-low confidence*, from uncalibrated diagnostics around 68.5–70.0%. **No strong total preference**. Winner direction: Ibaraki ML. A 65% strong numerical threshold on an uncalibrated normal proxy is **not** proof of accuracy. Formal v24.15 output is `RESEARCH_ONLY / NOT_ISSUED / NO_QUALIFIED_PRIMARY_P`, because the pre-game kit/reference/evidence freeze and competition-specific widths were not established.

All listed source windows were prior to scheduled tip; actual first play unverified. No result for this event was consulted. No outcome grading, prediction freezing, settlement or canonical import. No claim that the repository writer has custody of this chat's local file.

## A8. Source ledger and access limitations

| ID | Source and URL | Supported fields | Limitations |
|---|---|---|---|
| S1 | Official B.LEAGUE fixture https://www.bleague.jp/en/game_detail/?ScheduleKey=506570&tab=1 | game key 506570, 19:05 JST, home, venue, season identity | game-centre summary sometimes lags updated 15/16 standings (4–10 and 6–8); prefer latest club pages |
| S2 | Ibaraki club event notice https://www.ibarakirobots.win/news/detail/id%3D25510 | independently names exact 11 Nov 19:05 venue/away assignment | event notice is from Oct 6, no current lineup |
| S3 | B.LEAGUE Akita club https://www.bleague.jp/club_detail/?TeamID=693 | season scoring, record, leader and results | no exact selected 11 Nov lineup |
| S4 | B.LEAGUE Ibaraki club https://www.bleague.jp/en/club_detail/?TeamID=712&tab=2 | season scoring, record, leader and results | no exact selected 11 Nov lineup |
| S5 | B.League stats secondary https://www.bleague-db.com/teams/693 | Akita L10, ORtg/DRtg, season PA | secondary derivation, not independently shot-verified |
| S6 | B.League stats secondary https://www.bleague-db.com/teams/712 | Ibaraki L10, ORtg/DRtg, season PA | same source collector as S5, not independent corroboration |
| S7 | Official 6 Nov game https://www.bleague.jp/game_detail/?ScheduleKey=506545&tab=2 | 118–123 regulation extreme, Q1/Q2/Q3/Q4 | extreme not discarded |
| S8 | Official all-time H2H https://www.bleague.jp/record/?club1=693&club2=712 | four 2025–26 H2H and prior seasons | earlier roster/league regime |
| S9 | Official B.LEAGUE injury register https://www.bleague.jp/news/injury.html | Travis listed 5 Nov; Chol removed 5 Nov | registration only, not full-team clearance or game-selected roster |
| S10 | Official B.LEAGUE news from club https://www.bleague.jp/media_news/detail/id=667179 | confirmation of Travis injury, Chol removal, historical per-game production | team-derived story, not independent team medical source |

Reader-specific `SRC-ALT-v3`: repository current access snapshot was read via GitHub connector with `ChatGPT-User`, current `CURRENT_ACCESS.csv` snapshot. We did **not** run the exact URL repo source audit for each path via `ml source-audit`, nor did we establish original collector lineage/hashes for all web pages. Mark `ACCESS_EVIDENCE_PARTIAL`, not `ALLOWED_BY_AUDIT` per individual URL. No bookmaker or betting predictor projections used to produce outputs. Source lookup begins with league/club official pages.

## A9. Completion matrix and custody

| Requirement | Completed | Gap / final disposition |
|---|---|---|
| Fixture, venue, timezone, native event ID | YES | actual first-play timestamp `NOT_VERIFIED` |
| Both team season/L5/L10 scoring and margins | YES n15/16 season, n5/n10 game rows | independent primary row-by-row verification only partially completed |
| L15/L20 exact completed-game tables | PARTIAL | L15 Ibaraki true n15 subset NOT_RECONSTRUCTED; Akita only n15; L20 capped by games available |
| Availability and injuries | PARTIAL | official list and season leaders; exact final five + bench NOT_VERIFIED |
| H2H, rest/travel, tactical | PARTIAL | H2H old roster; ORtg/DRtg proxy; no verified late lineup |
| Reference tier, calculation kit, model | NOT_RUN | competition exact-scope baseline and `SR-KIT-v24.15` receipt absent; no promoted model |
| Probabilities for all supplied directions | DIAGNOSTIC_ONLY | not frozen/validated primary; margin/total normal approximation only |
| Formal mini card/ledger/learning/freeze | NOT_RUN | writer lease reserved to repository agent; GitHub strictly read-only |
| Settlement | NOT_REQUESTED | no final score, WIN/LOSS/PUSH/VOID grade, or correction entered |
| Reuse/read-back | YES | local file and appendix, footer verification after write |

**Custody:** `READ_ONLY_DRAFT / NOT_ISSUED / NOT_SETTLED / NOT_GRADED / NOT_PERFORMANCE_ELIGIBLE` · `LOCAL_REPORT_RECEIPT=RESEARCH-DRAFT-07` · `EV2_KEY=NOT_ASSIGNED` · `OFFICIAL_LOCAL_KEY=NOT_ALLOCATED` · `P_ID=NOT_ASSIGNED` · `CLEAN_PRE_START_ISSUE=NOT_CERTIFIED` · `MODEL_P=NONE` · `PRIMARY_P_CARD=NOT_ESTIMATED` · `GITHUB_WRITE=NONE`.

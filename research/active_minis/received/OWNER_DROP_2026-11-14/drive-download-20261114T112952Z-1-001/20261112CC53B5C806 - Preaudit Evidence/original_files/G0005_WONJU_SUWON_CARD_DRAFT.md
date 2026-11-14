<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0005 -->
## Card · LOCAL-20261112CC53B5C806-G0005 · Basketball / Korea KBL · Wonju DB Promy vs Suwon KT Sonicboom · 2026-11-13 KST

- **Local event key:** `LOCAL-20261112CC53B5C806-G0005` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED` / `PROMPT_4_IMPORT`.
- **Authority:** `PUBLISHED_MAIN_PINNED` GitHub `main` SHA `008cedc4ff469e7a808292aa3667a7bffe22e273`; MDS v24.16, control CR-2026.11.11-R4, records CR-2026.11.12-R1, scoring SCV-2026.11.11-v13, selection SEL-2026.10.22-v4, prompt P-2026.11.11-v24.14. Owner's chat-local read-only override; no working tree or published freeze.
- **Game identity / aliases:** 2026–27 Korean Basketball League regular season, Wonju DB Promy/Dongbu Promy (home) vs Suwon KT Sonicboom/KT (away), exact matching StatGG game `S49G01N66`; official KBL schedule November 13, 19:00 Korea Standard Time, Wonju DB Promy Arena, Wonju, Republic of Korea. Native KBL game identifier not separately confirmed.
- **User-requested start:** 2026-11-13 21:00 AEDT (UTC+11) = 19:00 KST (UTC+09) = 10:00 UTC. User request arrived about 20:54 AEDT, estimated from supplied conversation context. Scheduled start verified; **actual first possession NOT_VERIFIED**, no GitHub pregame freeze. Do not treat work performed after scheduled tip as an issued pregame forecast.
- **Competition / regulation:** Korean KBL 2026–27, FIBA-derived 4×10-minute regulation, 5-minute overtime as needed; every full-game spread and total **includes overtime** under framework BK-OT-1 (`FROZEN_FRAMEWORK_CONVENTION`). No half or quarter contracts.
- **Issue status:** `UNCALIBRATED_QUALITATIVE / READ_ONLY_DRAFT / NOT_ISSUED_IN_REPOSITORY`. Any numeric figures are `EXPLORATORY_SHADOW_NOT_PRIMARY` and **not official p_card**, not a released predictive model, not independently qualified and not suitable for formal Rank-1 numerical gate. Original source publication times for some mutable pregame pages are unknown (`KNOWN_AT_UNVERIFIED`).
- **Model/source disposition:** GitHub `ml reference`, `ml pregame`, `ml card lint`, `ml learning-log` and freeze NOT_RUN (working repository/runtime unavailable; owner no-Git-change instruction). Separately executed **1,200,000-match** source-disclosed normal/scoreboard+OT shadow in `/mnt/data/kbl_shadow_wonju_suwon_20261113.py`, diagnostic `/mnt/data/KBL_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0005.json`; no fictitious model receipt.
- **Baseline:** `BASELINE_LEAGUE_V1 NOT_FORMALLY_FROZEN`. Main-branch historical KBL competition parameter: `Basketball/KBL`, development 1,080 rows, mean combined 159.39, raw total SD 17.93, raw margin SD 13.97, residual total 16.82, residual margin 12.61; `HISTORICAL_DEVELOPMENT_UNADMITTED` (not current season and not predictive qualification). Current 2026–27 13-game team records and external league scoring reference around 171.4 indicate scoring-regime shift; exact current-league cohort/row dates not audited. Shadow uses historical family widths inflated 10%, not a formal league baseline. Do not promote old KBL 159.39 mean to current expected total.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`: precise dated L5 results and standings retained below; independently audited L10 dated row set, all current-season games, lineups, and feature source-time fields not fully acquired. Future learning PENDING_SETTLEMENT and independently verified known-at gate.
- **Expected result (shadow only):** Wonju ~91.30, Suwon ~85.28, combined ~176.58, signed home margin ~+6.02; total SD ~20.69, margin SD ~15.46. Descriptive means, not exact score picks.
- **Cutoff and outcome exposure:** Calculations use only historical results through 2026-11-09, official 13-Nov pregame news and no 13-Nov live game states; checked source pages showed `upcoming` without target score. Actual first possession not independently timestamped. Research/append timestamps are recorded in local append receipt; no prospective freeze claimed.

### Decision block

**Decision:** Under 179.5 total points is the **least fragile directional lean**, but remains LOW confidence and fails the framework's 0.65 strong-pick convention. Wonju has a plausible home advantage, especially with Henry Ellenson expected back and several Suwon absences, but **Wonju −5.5 sits almost on the estimated margin** and has no robust support. No high-confidence single or multi-leg position is justified.

| Rank | Role | Tag | Contract / exact proposition | Primary p_card | Primary p_base | BASELINE_P | Shadow diagnostic only | Principal failure route |
|---|---|---|---|---|---|---|---|---|
| 1 | PICK (conditional direction) | SUPPLIED | `TOTAL_UNDER_179_5`: combined final including OT ≤179 | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **55.88%**, sensitivity 40.38–68.40% | Ellenson return and Bass/KT perimeter shooting produce 180+; late fouls/OT |
| 2 | PICK (weak directional only) | SUPPLIED | `WONJU_MINUS_5_5`: Wonju final margin ≥6 | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **51.57%**, sensitivity 48.44–58.01% | KT stays within 5, or wins, via rebounding/Paris Bass scoring |
| – | INFORMATIONAL | SUPPLIED | `SUWON_PLUS_5_5`: Suwon loses by ≤5 or wins | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **48.43%**, sensitivity 41.99–51.56% | Wonju transition and paint advantage becomes 6+ |
| – | INFORMATIONAL | SUPPLIED | `TOTAL_OVER_179_5`: combined final including OT ≥180 | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **44.12%**, sensitivity 31.60–59.62% | Short rotation and offensive suppression limit scoring |

**Winner (shadow only):** Wonju 65.15%, Suwon 34.85%. **Strong-pick gate:** `NOT_ASSESSABLE`; no calibrated/formally frozen primary probability and the exploratory leading direction <0.65. **Rank-2 floor:** NOT_ASSESSABLE. **Primary baseline coverage:** 0/0 numeric ranked rows. **Model shadow:** independently executed conditional Monte Carlo, **not an MLSCOPE-v3 GitHub shadow release**. **Adjustment dependence:** scenario-dependent; ranked Under flips in high-scoring scenario. **Joint failure:** for chosen directional Under and Wonju−5.5, both lose when `total≥180 AND Wonju margin≤5`; approximate complement joint must be read from shared simulation array (not reported as exact without calculation). **Exact supplied contracts:** all four mutually complementary propositions accounted for; no push at half-point lines; no void assumed outside applicable abandonment/operator terms.

### Appendix

#### A1. Identity, event state and exact user contracts

Owner request: `Upcoming Basketball Game: Wonju Promy vs Suwon Sonicboom, Korea KBL; Estimated Game Time Start: 13 November 2026, 9:00 PM AEDT; Promy -5.5; Sonicboom +5.5; Combined Total: Over/Under 179.5 Points`. Both clubs' unambiguous official names resolved; 13-Nov KBL game, not the earlier 23-Oct meeting. 19:00 KST venue Wonju DB Promy Arena confirmed by KBL schedule (`https://www.kbl.or.kr/match/schedule`) and independent StatGG game `S49G01N66` (`https://statgg.com/en/kbl/matches/S49G01N66`). Actual start, official active list and contemporaneous live/event state NOT_VERIFIED at append; the existence of a planned 19:00 start does not certify pre-start issuance. MARKET_BLIND: no prices used.

#### A2. Frozen supplied contracts, endpoints and action

| Key | Proposition | W/L/P/V mechanism | Source of status |
|---|---|---|---|
| WONJU_MINUS_5_5 | `DB − KT ≥ 6` | WIN if ≥6, LOSS if ≤5; PUSH impossible on half point | exact owner line; final incl OT |
| SUWON_PLUS_5_5 | `DB − KT ≤ 5` | complement of Wonju −5.5, not a second independent signal | exact owner line; final incl OT |
| TOTAL_OVER_179_5 | `DB + KT ≥ 180` | WIN if ≥180, LOSS if ≤179 | exact owner line; final incl OT |
| TOTAL_UNDER_179_5 | `DB + KT ≤ 179` | complement of Over 179.5 | exact owner line; final incl OT |

Both line pairs use full-match basket scoring and five-minute overtime under BK-OT-1. Exact operator cancellation/abandonment convention is not supplied; no VOID assessment can be made.

#### A3. Sources, actual dated form, personnel and known-at

**Pre-event standings / pace.** StatGG 13-Nov matchup snapshot: DB 7–6, 90.1 PF/89.3 PA, home 3–2; KT 6–7, 85.0 PF/86.5 PA, away 3–4; records through 13 games each. StatGG source reports pace 77.2 DB and 72.7 KT, ORtg 113.8 vs 111.8, DRtg 113.1 vs 116.7; provider's pace/efficiency scale is unverified against raw totals, so used directionally only. `https://statgg.com/en/kbl/matches/S49G01N66`. Separate primary pregame schedules on `https://www.kbl.or.kr/match/schedule` and `https://promy.kbl.or.kr/match/schedule`.

**Last five official-season results before target** (score shown in team's perspective, W/L from that team's side; AiScore dated list corroborated against another pregame results source):

| Wonju date (KST) | Opponent | Wonju–opponent | Result | Combined |
|---|---|---|---|---|
| 2026-11-08 | Seoul SK | 65–81 | L | 146 |
| 2026-11-07 | Seoul Samsung | 84–76 | W | 160 |
| 2026-11-01 | Changwon LG | 104–98 | W | 202 |
| 2026-10-31 | Busan KCC | 74–90 | L | 164 |
| 2026-10-28 | Daegu KOGAS | 90–95 (OT) | L | 185 |

| Suwon date (KST) | Opponent | Suwon–opponent | Result | Combined |
|---|---|---|---|---|
| 2026-11-09 | Seoul Samsung | 78–85 | L | 163 |
| 2026-11-07 | Daegu KOGAS | 92–81 | W | 173 |
| 2026-11-01 | Goyang Sono | 103–96 | W | 199 |
| 2026-10-31 | Anyang Red Boosters | 92–90 | W | 182 |
| 2026-10-25 | Seoul SK | 79–90 | L | 169 |

Rows: `https://www.aiscore.com/en/head-to-head/basketball/busan-ktf-sonicboom-vs-wonju-dongbu-promy`, corroborating `https://abasketballreport.com/predictions/head-to-head/2026-11-13/south-korea/kbl/wonju-db-promy/suwon-kt-sonicboom/NzAyNjMtNzAyNjI%3D` and 2026 season fixture/standings. **Overlapping form windows are not independent features.** Wonju L5 (n=5) PF83.4, PA88.0, total171.4; Suwon L5 (n=5) PF88.8, PA88.4, total177.2. Wonju L10 and Suwon L10 exact per-game dated rows not independently reconciled (n effective 0 verified complete). Current-season 13 games are a usable season summary only, not rebranded as individually verified L15/L20: season n=13, L15 and L20 **insufficient current-season 15/20**; full prior-season extension NOT_RECONSTRUCTED. One available aggregate provider lists last-10 numbers but not a full dated-rows audit, so it is withheld from quantitative fitting. KBL league scoring average around 171.4 on pregame schedule reference, cohort provenance incomplete; treat as context not exact audited league baseline.

**Head-to-head.** On 2026-10-23 Wonju won at Suwon 102–95 (197 combined), confirmed by StatGG and 13-Nov fixture source. Older 2025–26 H2H games had mostly closer margins; roster/season regime differs and they are not independently fitted. One H2H is descriptive, not a numerical adjustment.

**Availability / roles.** News published 2026-11-09 from Sports Chosun quotes DB club plans for Henry Ellenson (F/C) to return 13-Nov after concussion/headache protocol, first appearance since October 19; 13-Nov 10:45 KST Jumpball preview also calls it his return. **RETURN_EXPECTED, not a confirmed dressed/starting role**, with playing minutes restriction unknown; foreign lineup combinations with Ration Hammonds / Alan Williams unknown. DB leading on-ball guard E'Twaun/Lee Sean Alvano (name rendered differently by providers), scoring forward Ration Hammonds, Kang Sang-jae (reported unavailable), Jung Ho-young (reported ACL injury); DB starting five, selected bench and final scratches NOT_CONFIRMED.

KT: Kim Sun-hyung (G, surgical recovery), Ha Yun-gi (C, bone bruise/rehab), Miguel Oczon (G, appendicitis surgery Nov 6) reported **OUT** by 13-Nov Korean injury briefing; Jeong Chang-young (F) questionable after 9-Nov injury. Paris Bass (high-usage primary scorer, 39 points/15 rebounds in prior game) and backup foreign big are expected contributors, but their exact roles/starting status NOT_CONFIRMED. Sources: `https://www.dailyil.com/ko/briefing/2026-11-13_KBL/`, `https://www.dailyil.com/ko/games/kbl-2026-11-13-kt-db/`, `https://www.chosun.com/english/sports-en/2026/11/09/ZPWYKNMKAZH7BPW7KMZPUJGLKI/`, `https://www.jumpball.co.kr/news/newsview.php?ncode=1065577530368244`. This is secondary journalism/injury tracking; no official same-minute lineup or club medical bulletin retrieved. **KT availability is a major scoring and margin regime uncertainty.**

#### A4. Reference, score grid and sensitivity

`ANALYST_PRIMARY_V1` formal reference stage NOT_RUN: KBL not covered by current released NBA/WNBA/NBL TB-2 model; historical KBL competition row has inadmissible stale development evidence. No primary p_card reported. Standalone shadow calculation (script, JSON) uses one coherent synthetic joint scoreboard and the identical event paths for all four propositions. Inputs: DB season PF90.08, PA89.31, Suwon PF85.00, PA86.46; neutral matchup arithmetic centres (90.08+86.46)/2=88.27 DB, (85.00+89.31)/2=87.16 Suwon; modest home/rest and player-availability uncertainty in declared three scenarios. Independent regulation total/margin Gaussian innovations with standard deviations 17.93×1.10=19.723 and 13.97×1.10=15.367 from FIBA historical family-width sensitivity, rho=0.0 before scoreboard transform. Team scores = rounded clipped integers (T±M)/2; tied regulation scores add an approximate five-minute OT basket total (~21.5±7 points). This does **not** reproduce KBL exact possession/shot/foul and OT state rules and its weights are illustrative, not fitted. Explicit 25/50/25 scenario mixture is for sensitivity exploration only; formal primary mixture weights require stronger evidence.

| Predeclared sensitivity scenario | Weight | Regulation expected score DB–KT | Shadow P(Under179.5) | Shadow P(DB−5.5) |
|---|---:|---|---:|---:|
| KT injury-short-rotation / slower | 0.25 | 89.0–80.5 | 68.40% | 58.01% |
| Central, mixed recovery | 0.50 | 90.1–85.3 | 57.36% | 48.44% |
| Both offenses efficient, Bass high | 0.25 | 95.0–89.0 | 40.38% | 51.39% |
| **Mixture, N=1,200,000** | 1.00 | simulated full-game ~91.30–85.28 | **55.88%** | **51.57%** |

Shadow output mean total ~176.58, SD20.69; margin +6.02, SD15.46; ~2.4% regulation ties trigger synthetic OT. **The input scenarios are not confidence bands or an independently calibrated forecast.** Simple 2026 raw-data total midpoint ~175.4; with Ellenson return, PT impact of KT absences and opponent-adjusted pace unknown, the central budget is unstable. League-only baseline attempt: historical KBL table mean159.39 belongs older regime and cannot be used as same-event current exact-line BASELINE_P; fresh league total ~171.4 with unverified cohort has no frozen, independently reproducible same-line comparator. BASELINE_UNAVAILABLE.

**Score budget:** with KT scoring 78/85/92, Under179.5 needs DB ≤101/94/87 respectively; Over needs DB ≥102/95/88. Opposite: if DB scores 84/91/98, Under needs KT ≤95/88/81; Over requires KT ≥96/89/82. A healthy Ellenson/high shooting line or high Bass support can defeat the Under even with a DB win. At −5.5, DB 91 needs KT ≤85 to cover; KT scoring 86+ defeats that line. High late-foul shooting/OT can alter both, without automatic Under or handicap benefit.

#### A5. Full priced universe (exact supplied rows only)

Four full-game owner-supplied contracts retained in the decision table, two complete 0.5-line complement pairs, no unrequested alternate lines ranked. Every half-point contract is decisive in a completed game; no exact push; void/abandonment outside current data. `p_card NOT_ESTIMATED`, shadow rows are CONDITIONAL_DIAGNOSTICS with explicit complement checks (Under+Over=1, DB−5.5+KT+5.5=1). Ranking scope `SUPPLIED_ONLY`; winner directional shadow shown. A rank is only a research ordering, not a numerically gated/published primary pick.

#### A6. Adjustments, availability regimes and dependence

Admitted historical facts: DB home (3–2), KT away (3–4), five days since 8-Nov last DB game, four days since 9-Nov last KT game (local dates; no back-to-back on 13-Nov); KT shot fewer threes at lower accuracy 31.3% vs DB 34.6% from pregame StatGG; DB Ellenson expected, KT three outs + one questionable. No official sourced effect-table magnitudes for KBL 2026 cohort; **no claim of formally measured +X possession/margin shift**. Avoid double-counting injuries already captured in the 13-match season sample. Strongest changes: Ellenson minutes availability (DB offense), KT guard creation (tempo, Bass help) and live three-point conversion (widens both directions). These are evaluated in the named scenario tree rather than asserted as proven shifts. Fast and slow alternatives reverse the total direction, invalidating high confidence. Margin-total outcomes from the *same* synthetic joint scores; no independence assumption for combined legs. Joint formal primary failure NOT_COMPUTED.

#### A7. Family checks / shadow / uncertainty and calibration

Reference `NOT_RUN_UNAVAILABLE_LOCAL_GIT_CODE`; no release, no certified skill, no published primary. Shadow `EXECUTED` n=1,200,000 with deterministic seed 13112026 and actual program/JSON. All four complementary probabilities sum to one within rounding. Widths above historical KBL residual floors, but older season evidence unadmitted for 2026 KBL. OT is explicitly drawn when regulation tied; do not label approx simulation a KBL-realistic possession engine. True KBL late-foul timing, lineups, substitution constraints, score/period correlation and eligibility are not fully modelled. Median of mixture not necessarily a safe pick. No sportsbook, prices, analyst-tip sentiment or externally supplied projected scores enter calculation.

#### A8. Source/failure register and settlement capture

1. KBL official `https://www.kbl.or.kr/match/schedule` + DB club `https://promy.kbl.or.kr/match/schedule`: exact 13-Nov schedule and venue, no reliable confirmed starting five or signed 13-Nov pregame play-by-play retrieved.
2. StatGG `https://statgg.com/en/kbl/matches/S49G01N66`: pregame 13-game team totals, ranks, home/away, 23-Oct H2H, shooting and estimated pace; page mutable and source publication timestamp absent.
3. AiScore `https://www.aiscore.com/en/head-to-head/basketball/busan-ktf-sonicboom-vs-wonju-dongbu-promy`: both team L5 dated game rows and quarter scoreboard; source is a live page, query time in local research receipt.
4. Sports Chosun dated Nov9 `https://www.chosun.com/english/sports-en/2026/11/09/ZPWYKNMKAZH7BPW7KMZPUJGLKI/`: club quote on Ellenson return; corroborated Jumpball 13-Nov 10:45 KST `https://www.jumpball.co.kr/news/newsview.php?ncode=1065577530368244`.
5. Daily IL 13-Nov `https://www.dailyil.com/ko/briefing/2026-11-13_KBL/`: named KT absences and Jeong Chang-young doubtful; status is secondary source and club record unverified.
6. Current source state as seen during web research: preview/schedule; no 13-Nov match outcome used. Several `web.open` routes returned cached fetch errors; equivalent `web.search` indexed full source snippets provided evidence; exact page capture/publish time not always known. Unresolved: actual tipoff; both confirmed starting fives; full selected benches; Ellenson actual minutes/scratch status; official KT active squad; dated pregame L10/L15/L20; KBL 2026–27 exact same-line league baseline; possession/shot-quality features; operator cancellation terms.

For an explicit later settlement request, obtain field-owner official KBL final quarter scoring, OT segments and final score; confirm second scoreboard and native event ID. Grade spread from `DB − KT` and total from sum **including overtime**; source and final time required; no scheduled follow-up or autonomous monitoring created. Suggested review due `2026-11-15T21:00:00+11:00` is a triage target, not an automation or actual action.

#### A9. Integrity, completion matrix, issue and readback

| Required procedure | Actual work and finding | Remaining gap | Status |
|---|---|---|---|
| Authority / identity / duplicate / timing | Pinned repo SHA; official 13-Nov 19 KST fixture; G0001–G0004 unrelated | Actual first play, native KBL event ID | DONE_WITH_GAPS |
| Starters / bench / absences / recheck | Team-level previews, Ellenson return, KT 3 out + 1 questionable, DB named unavailable | Official dressed squad, fives, bench, Ellenson restriction | INFORMATION_INCOMPLETE |
| Online history / independent comparison / known-at | KBL official schedule, StatGG, AiScore, news, dated L5 games | Publication timestamps on mutable statistics, full dates L10+ | INFORMATION_INCOMPLETE |
| L5 / L10 / L15 / L20 / season / league | Recomputed both L5 from 10 dated scores; season n=13 each; KBL league context | Complete L10 dates, current-season n<15 and prior-season changes, exact league sample | INFORMATION_INCOMPLETE |
| KBL mechanisms, rules, venue, fatigue | FIBA40+OT, home court, 4/5-day rest, roster regime and budget, pace/special shooting | Exact shot creation, official minutes / active players | DONE_WITH_GAPS |
| Reference / frozen primary | Historical KBL row inspected; separate source-based approximation | No official `ml reference`/freeze/lint or calibrated baseline | NOT_RUN |
| Scenario arithmetic and dependence | 1.2m executed coherent score-grid paths, OT approximation, exact four row counters | Model release, fit, calibration, detailed overtime quality | SHADOW_ONLY |
| Every supplied contract | Two spread and two total directions computed; complement tests, definitions | Operator-specific void terms | DONE_CONDITIONAL |
| Expected score, W/P/L/V, baseline and sensitivity | Separate numerical shadows, score budget and branch thresholds | No valid primary p_card or same-line league comparator | SHADOW_ONLY |
| Complete A1–A9, append and custody | Draft card/source list/readback planned; preserving originals and updating local footer | No GitHub repository linter, freeze, ledger issue, commit or push by owner instruction | CHAT_LOCAL_DRAFT |

**Overall:** `INFORMATION_INCOMPLETE`; `RESEARCH_ONLY_NOT_CERTIFIED`; `NO_STRONG_PICK`; `EXPLORATORY_SHADOW_EXECUTED / PRIMARY_NOT_RUN`; `CHAT_LOCAL_READ_ONLY_DRAFT_NOT_REPO_ISSUED`; actual pre-start status must be decided from the recorded append time against **verified** first-possession time, not the user-supplied estimate. No canonical allocation or settlement.

**SPORTS_ONLY_MARKET_BLIND:** YES · **OUTCOME_EXPOSURE:** NO_TARGET_RESULT_SEEN_DURING_RESEARCH · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0005 -->

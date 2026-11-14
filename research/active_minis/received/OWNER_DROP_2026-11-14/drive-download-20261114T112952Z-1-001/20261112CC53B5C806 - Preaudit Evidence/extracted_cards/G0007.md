<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0007 -->
## Card · LOCAL-20261112CC53B5C806-G0007 · Ice hockey / Czech U20 Extraliga · Motor České Budějovice U20 vs Bílí Tygři Liberec U20 · 2026-11-13 CET

- **Local event key:** `LOCAL-20261112CC53B5C806-G0007` — `LOCAL_UNIMPORTED_EVENT`; first local record for this event in this chat.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED / PROMPT_4_IMPORT`; no canonical ID reserved.
- **Event / native ID / aliases:** Czech Hockey Federation `match 3156`, game-detail internal URL `178203`, Komerční banka extraliga juniorů 2026/27 round 20; BANES Motor České Budějovice (Motor U20, České Budějovice U20) vs Bílí Tygři Liberec (Liberec U20). No relation to senior teams or U18 fixtures of similar names.
- **Authority:** GitHub `danisgreat/Sports-Research` `main` pinned `008cedc4ff469e7a808292aa3667a7bffe22e273` read-only. MDS v24.16; forecast control CR-2026.11.11-R4; records update CR-2026.11.12-R1; prompt v24.14; scoring SCV-v13; selection SEL-v4; user `CHAT_LOCAL_ONLY / NO_GITHUB_WRITE` override. No local clone, repo reference freeze, issued card or ledger execution.
- **Probability method:** `UNCALIBRATED_QUALITATIVE` as primary; independently **executed** `EXPLORATORY_SHADOW_NOT_PRIMARY` 1,200,000-run joint goal Monte Carlo with 3 source-anchored but *assumed* scoring/goalie/empty-net scenarios. Not an official primary `ANALYST_PRIMARY_V1` run; no released model or independently validated calibration. Source/JSON: `hockey_shadow_motor_liberec_20261113.py`, `HOCKEY_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0007.json`.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`; official Liberec 17 results and Motor L5 retained with dates/score sources; Motor L10/L15/L20 dated rows, complete current goalkeeper and skater availability snapshots, shot/PP covariates and point-in-time league event-level baseline not assembled. No LEARNLOG or frozen repository feature pack executed.
- **Future learning:** `PENDING_SETTLEMENT / NOT_ADMITTED`: requires verified actual start/final/periods, goaltenders, source timestamps and unknown operator terms; this card's timing is not certified pregame.
- **Analysis status:** `UNCALIBRATED_QUALITATIVE` with shadow directional diagnostics; `INFORMATION_INCOMPLETE`; `NO_STRONG_PICK`; not performance-eligible.
- **Timing and exposure:** User estimated `2026-11-13T00:30+11:00`, equal to 12-Nov 13:30 UTC or 14:30 CET. **Official federation and current club match list** publish **13-Nov-2026 12:00 CET** = 13-Nov **22:00 AEDT** (11:00 UTC); a minority of club cached listings show **15:30 CET** (14-Nov **01:30 AEDT**). These conflict and the actual first puck-drop was never independently checked. Initial fixture/standings/goalie-empty match centre observed before 22:00 AEDT; further research and chat-local append are after the 22:00 scheduled clock. `POST_SCHEDULED_START / ACTUAL_START_UNVERIFIED / NOT_CLEAN_PREGAME_ISSUE`. No target-game live/final score consulted, and `0:0` on a pregame match page is not graded as a result.
- **Venue and conditions:** Budvar aréna, České Budějovice, Czechia. Indoor ice; outdoor weather `NOT_APPLICABLE`; ice quality, officials' penalty environment and rink differences not quantified.
- **Exact endpoint / actions:** User supplied full-game Motor `−1.5`, Liberec `+1.5` goals, combined `O/U 5.5`. Model assumes regulation + winner-takes-one-goal OT/SO if tied, one conditional empty-net scoring branch; half-point lines have no pushes when action stands. Under these simplified rules the exact supplied contracts are OT-goal-invariant if a regulation tie can add at most one goal, although named sportsbook/operator action rules, suspension, forfeits and shootout convention are `UNKNOWN_DEFINITION` and not presumed. Win/lose/void need operator confirmation in settlement.
- **Shadow distribution object:** `IND_POISSON_60MIN_PLUS_STYLIZED_OT_EN_SCENARIOS` with 0.25 low, 0.50 base, 0.25 high weights; three independent Monte Carlo batches of 300k / 600k / 300k. Home edge implicit in home team pairing, **not** separately fitted. Correlated scoring/true pulled-goalie likelihood and lineup states are not fit. Empty-net branch may double-count raw season scoring; simulation is sensitivity only.
- **Shadow expected score and uncertainty:** scenario-weighted Motor **3.779**, Liberec **2.652**, combined **6.431**, Motor signed lead **+1.127** goals; within-scenario weighted SD total **2.468** and margin **2.546** (NOT the full-mixture SD). These numbers are uncalibrated diagnostics, **not** certified primary expected scores.
- **Baseline:** Exact-line `BASELINE_LEAGUE_V1` **NOT_COMPUTED**: official league-wide pre-event standings allow empirical mean but no verified past same-line event-level distribution or Czech-junior goaltender/OT calibrated baseline. League prior 910 team goals / 296 team appearances = **3.0743 per team-game**, 6.1486 combined; this descriptive mean does not substitute for `BASELINE_P`.
- **Regime/context:** host 5th / 38 pts from 19 games vs visitor 15th / 12 pts from 17; youth-junior volatile goalie/depth exposure; last match on 19-Sep ended Liberec 3–4 Motor after extra-time process (exact SO/OT subtype needs re-verification). Motor more reliable recent defense; Liberec 3 wins in last 4 including extra-time, so weak season record not equivalent to guaranteed blowout.
- **Settlement capture plan:** after the event on explicit user follow-up, capture official Czech Hockey Federation `match 3156` final (score, period splits, OT/SO, goaltenders, exact start and status) and corroborate hokej.cz and both clubs; determine total and full-game margin; preserve operator rules/void condition separately. No scheduled automation; no settlement performed here. Triage due **2026-11-15T22:00+11:00** is a manual target only, final-time basis `UNKNOWN`.
- **Rules/source reading receipt:** `CORE.md`, `CURRENT_STATE.md`, `RULES_REFERENCE.md` §7–9, `RULES_ICE_HOCKEY.md` §§0–3,6–8, `PROBABILITY_TOOLKIT.md` §2, `CARD_AND_LOG_TEMPLATES.md` §§2–3, `RESEARCH_PROTOCOL.md` Parts A/B/E, `research/prompts/1_GAME_CARD.md` and ice-hockey sport-specific requirements by pinned main; 2026 Czech federation fixture/standings, official Liberec U20 results, Motor regional club match reports. Only read/search/fetch GitHub operations; repository's `ml reference`/`card lint`/pregame freeze were **not executed**.
- **Known-at and lineup state:** Federation fixture/standings and dated pre-event results captured prior to official 22:00 AEDT schedule and other same-game result exposure. Page publication timestamps for mutable roster/standings unknown. Exact-game official `SESTAVY` skater and goaltender tables contained `NO DATA AVAILABLE` in the pre-match inspection; **both starting goaltenders, defense pairs, offensive lines, scratches, call-ups and injuries unconfirmed**. A season roster at Motor lists goaltenders Štěpán Bogač and Vojtěch Jelínek, **not verified starters**. Do not label unreported injuries as none.
- **Pricing basis:** `SHADOW_ONLY` three illustrative cases with unfit 0.25/0.50/0.25 weights, not an independently frozen primary reference/adjustment ledger. Official `p_card` NOT_ESTIMATED. No uncalibrated shadow promoted to a calibrated probability.
- **Form windows:** Motor L5 from dated 17–31 Oct rows: GF16/5 3.20, GA10/5 2.00, total 5.20; L10/L15/L20 dated rows **NOT_COMPLETED**; regular-season full n19 69 GF/45 GA from official table. Liberec complete L5 GF14 GA16 total6.00, L10 GF28 GA40 total6.80, L15 GF38 GA64 total6.80, L20 available n17 GF41 GA71 total6.59 (cannot imply 20 games); season n17 same 41/71. League total 6.1486 goals/game from all 16 standings entries. Full source rows and gaps in A3.

### Decision block

**Assessment:** **Over 5.5 goals** is the strongest *exploratory* direction due to a 6.15-goal league environment and Liberec's season-high conceded rate; however its sensitivity range spans both sides of 50%. Motor is clearly the stronger outright side; its `−1.5` remains vulnerable to close games, and **no high-confidence pick can be issued** without confirmed goalies, exact endpoint custody and pregame timing.

| Rank | Role | Tag | Exact contract / proposition | p_card | p_base | BASELINE_P | Line distance | Basis / failure |
|---|---|---|---|---|---|---|---|---|
| 1 | PICK (directional only) | SUPPLIED | `TOTAL_OVER_5_5`: combined match goals ≥6 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow centre 6.431 − 5.5 = +0.931 goals; no validated z | Qualitative; separate shadow ~0.6044. Goaltending, low-shot and low-conversion 5-goal branch kills |
| 2 | PICK (directional only) | SUPPLIED | `LIBEREC_PLUS_1_5`: Motor winning margin <2 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow margin 1.127 vs +1.5, no validated z | Qualitative; separate shadow ~0.5255. Motor finishing and empty-net 2-goal outcome kills |
| — | INFORMATIONAL | SUPPLIED | `MOTOR_MINUS_1_5`: Motor winning margin ≥2 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow margin 1.127 vs +1.5; no validated z | Shadow ~0.4745; vulnerable to 1-goal/OT finish |
| — | INFORMATIONAL | SUPPLIED | `TOTAL_UNDER_5_5`: combined match goals ≤5 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow total centre 6.431 >5.5; no validated z | Shadow ~0.3956; killed by 6+ goal conversion/goalie weakness |

**Baseline coverage:** 0/0 numeric primary rows. **Rank-1 gate:** `NOT_ASSESSABLE`; no frozen exact-line baseline, certified p_card, goalie confirmation or prospective freeze. **Rank-2 floor:** `NOT_ASSESSABLE`. **Joint failure (shadow only):** P(Over5.5 loses AND Liberec+1.5 loses) = P(total ≤5 AND Motor margin ≥2) ≈ **0.1490**, unconditional across the assumed sample tree; no issued-card joint. **Family check:** `Motor−1.5` + `Liberec+1.5` =1.000 in shadow, `Over+Under5.5` =1.000; pushes excluded for half-lines in assumed action. **Adjustment dependence:** `SCENARIO_SENSITIVE`; Over crosses 50% between cases and handicap direction flips in high case. **Potential winner (shadow only):** Motor 0.6792; Liberec 0.3208 (OT winner branch included). **Abstain:** YES, `NO_STRONG_PICK`; all qualified primary probabilities unavailable. **Model shadow (MLSCOPE-v3):** `NOT_RUN_NO_RELEASE_OR_LOCAL_MODEL`; separate executable *illustrative* Monte Carlo is not the GitHub model shadow.

### Appendix

#### A1. Identity, timing and state

- Official game `3156` / page `https://czehockey.cz/game/detail/178203`; organizer's full pre-match fixture `https://www.czehockey.cz/competition/games/1?gameListWidget-page=13`. Club current schedule `https://www.hcbilitygri.cz/matches/JUN`. All identify same home and away U20 players and 13-Nov match.
- Official and most current published scheduling: **13-Nov 12:00 CET**, i.e. UTC11:00, AEDT22:00; user originally supplied **13-Nov AEDT00:30** (previous Czech local date, unrelated to actual match). Old filtered/cached club lists advertise **15:30 CET**. Retain both, source conflict; a post-scheduled issue is *not* a prestart issue unless first play actually verified later (not done).
- `STATUS_AT_ISSUE`: `TIMING_UNVERIFIED`, `POST_OFFICIAL_SCHEDULE_CLOCK`, no verified live/final target exposure, no access to actual first-play timestamp. Neither the federation pregame placeholder `0:0` nor any unrelated age-group/senior match is target evidence.
- Venue Budvar aréna, České Budějovice; youth regular season, three 20-minute regulation periods. Exact OT/SO & contract settlement only assumed for exploratory scoring, field-owner regulation and operator terms unavailable.

#### A2. Frozen owner-supplied contracts and candidate plan

| Exact row | Scored quantity | Win condition | Push/void | Support | Counterargument / primary status |
|---|---|---|---|---|---|
| Motor −1.5 | Full-game home-away goal margin | Motor wins by at least 2 | None on half-line if valid match, operator void UNKNOWN | Fifth place, 69–45 and Liberec defensive 71 conceded | One-goal H2H, OT games, scoring width; NOT_ESTIMATED primary |
| Liberec +1.5 | Full-game goal margin | Liberec wins or loses by ≤1 | None on half-line if valid, operator void UNKNOWN | 3/last4 wins for Liberec, Motor close losses in last2 | 15th-place defense, Motor attack & EN goals; NOT_ESTIMATED primary |
| Over 5.5 | Total official match goals | At least 6 | None on half-line if valid, operator void UNKNOWN | League 6.1486, Liberec GA 4.176, 19-Sep H2H total7 | Both teams' most recent L5 total means 5.2 / 6.0; goalie uncertainty; NOT_ESTIMATED primary |
| Under 5.5 | Total official match goals | At most 5 | None on half-line if valid, operator void UNKNOWN | Motor last five 5.2 total, 2.0 goals against | Liberec's porous defense + power play, empty-net tail; NOT_ESTIMATED primary |

Rank scope supplied lines only (no derived thresholds). One coherent three-scenario joint goal simulator provided all **shadow**, not primary, row values. No multiple user fixtures combined.

#### A3. Evidence and online historical rows

**Official league snapshot** `https://ceskyhokej.cz/competition/standings/1` (2026/27 before match): 16 teams, 296 team appearances / 148 games, GF sum 910, league average GF/team 3.0743 and full-game 6.1486; Motor 5th 19 GP GF69 GA45 38pts; Liberec 15th 17 GP GF41 GA71 12pts. Site shows season-to-date tabular figures; publication/correction time unknown.

**Motor U20 recent played matches**, official/regional reports and source corroboration; scores are Motor first. OT/SO match-score shorthand is explicitly not a regulation goals record:

| Date | Opponent / site | Final Motor–opponent | Source |
|---|---|---|---|
| 2026-10-17 | Litvínov away | 3–1 | competition result summaries; regional report index; full official original row not independently recovered |
| 2026-10-19 | Slavia Praha home | 3–1 | `https://hcmotor.cz/zapasy.asp?filtrTym=SLA&kde=vsechno&sezona=2027&stats=true` |
| 2026-10-23 | Plzeň home | 5–1 | `https://hcmotor.cz/zapasy.asp?filtrTym=PLZ&kde=doma&sezona=2027&stats=true` |
| 2026-10-30 | Mountfield HK away | 3–4 | `https://www.onlajny.com/match/index/date/2026-10-30/id/540494`; `https://www.jchokej.cz/archiv-kratkych-zprav?page=2` |
| 2026-10-31 | Pardubice away | 2–3 after shootout (reg 2–2) | `https://www.jchokej.cz/archiv-kratkych-zprav?page=2` and Motor club match archive |

Motor **L5** GF16 GA10, average scored 3.20 and conceded 2.00, total 5.20. **L10/L15/L20 dated opponent-specific records** NOT_COMPLETE because no verified intact 19-game source pack was retrieved (several search pages identified as 2025/26, explicitly rejected). Season n19 69/45 independently from organizer. Don't convert 19-game aggregates into 20 specific rows.

**Liberec U20 current-season results**, all from `https://www.hcbilitygri.cz/matches/JUN`, ordered by date; scores are Liberec first. Club match page lists 17 results. Extra-time subtypes for some matches require result-details recheck; final team-scoring totals match federation 41/71 exactly:

| Date | Opponent | Final LIB–opp |
|---|---|---|
| 2026-09-04 | Litvínov | 2–3 |
| 2026-09-05 | Karlovy Vary | 1–4 |
| 2026-09-11 | Vítkovice | 3–4 |
| 2026-09-12 | Třinec | 3–6 |
| 2026-09-18 | Jihlava | 0–2 |
| 2026-09-19 | Motor | 3–4 after extra time |
| 2026-09-25 | Mountfield HK | 1–8 |
| 2026-09-26 | Pardubice | 1–7 |
| 2026-09-28 | Mladá Boleslav | 3–5 |
| 2026-10-10 | Sparta Praha | 3–5 |
| 2026-10-16 | Plzeň | 5–6 after extra time |
| 2026-10-17 | Slavia Praha | 2–1 |
| 2026-10-23 | Karlovy Vary | 1–2 |
| 2026-10-24 | Litvínov | 4–3 OT (`https://www.hcverva.cz/match/6814`) |
| 2026-10-28 | Poruba | 3–2 |
| 2026-10-30 | Třinec | 1–5 |
| 2026-10-31 | Vítkovice | 5–4 after shootout |

Liberec form from dated results: **L5 GF14 GA16** (2.80/3.20, total6.00); **L10 GF28 GA40** (2.80/4.00, total6.80); **L15 GF38 GA64** (2.53/4.27, total6.80); **L20 only n17 GF41 GA71** (2.41/4.18, total6.59); season n17 same. Windows overlap and are ONE evidence stream, not independent signals. League-level benchmark 6.1486 combined, not an identical-line success-rate baseline.

**H2H:** one corroborated 2026/27 U20 match, 19 September at Liberec, final `3:4` after extra-time handling; Motor won by **1**, both teams scored ≥3 (7 total). No use of U18 matchup 11 Oct (4–3) or senior team results; no trusted current-regime older H2H changes to p.

**Both-side availability/roster:** exact-match federation page `SESTAVY` skaters/goalies empty pregame. Motor general season roster `https://hcmotor.cz/soupiska.asp?kategorie=U20&sezona=2027` shows potential goalkeeper names Štěpán Bogač and Vojtěch Jelínek, **not confirmed**. Club pre-match Onlajny top scorers: Motor Matyáš Humeník (30 points), Jakub Lev (29); Liberec Daniel Pekař (15), Vasyl Špilka (12). Liberec's possible goalie, both lines/bench, scratches, suspensions, illnesses, injury and return reports remain **MISSING / not independently confirmed**. No fabricated absence/health assertions.

#### A4. Distribution, official reference gap, arithmetic and sensitivity

- Source anchor: league μ goals/team =910/296=**3.074324**. Season Motor GF69 GA45 n19 and Liberec GF41 GA71 n17. Using an **illustrative** pseudogame shrinkage constant k=10, rating `O=(GF+k×μ)/(n+k)`, `D=(GA+k×μ)/(n+k)`. Base 60-minute goal centres `λMotor=(OM+DL)/2≈3.604`, `λLib=(OL+DM)/2≈2.635`; sum≈6.239. No league-certified reference or calibrated goal process executed.
- Assumed scenario rates, declared before simulation: low (Motor 3.10, Liberec 2.05, conditional empty net p=.15); base (3.604, 2.635, p=.30); high (4.25, 2.90, p=.45). Weighted **.25/.50/.25** for *illustrative sensitivity*, NOT source-fitted likelihoods. Independent Poisson 60-minute goals, one extra potential empty-net goal on an exactly-one-goal late lead, and a one-goal extra result in regulation draws with arbitrary win split `λMotor/(λMotor+λLib)`. This is **not** a fit to Czech U20 events. The explicit empty-net addition is possibly double-counted by full-game season rates and can bias expected totals and handicaps; quantify as shadow only.
- Runtime: Python 3, NumPy random generator deterministic seed `20261113`, `1_200_000` completed simulations (300k low / 600k base / 300k high), standard source script `hockey_shadow_motor_liberec_20261113.py`. NOT executed: repository `python -m ml reference`, reference freeze, pregame run, canonical ledger or model source admission. No training dataset or performance qualification.
- Shadow outcome probabilities (conditional estimates only): Motor −1.5 **0.474520**, Liberec +1.5 **0.525480**, Over5.5 **0.604422**, Under5.5 **0.395578**, outright Motor **0.679200**, Liberec **0.320800**. Complimentary rows sum to 1.00 by construction (no push under half-lines; no void simulated).
- Scenario outcome matrix:

| Scenario / weight | Motor −1.5 | Liberec +1.5 | Over5.5 | Under5.5 |
|---|---:|---:|---:|---:|
| Low conversion .25 | 0.4412 | 0.5589 | 0.4268 | 0.5732 |
| Base .50 | 0.4581 | 0.5419 | 0.6195 | 0.3805 |
| High pace/goalies .25 | 0.5407 | 0.4593 | 0.7519 | 0.2481 |

- **Sensitivity:** Over5.5 range **0.427–0.752** (crosses 50%), Motor−1.5 range **0.441–0.541** (crosses 50%). No family-level robust numeric advantage. `NO_STRONG_PICK`. Possession/game-width/shot-based fitted covariance and competition-specific goalie effects unavailable.
- **Goal-line budget:** At total 5.5, combinations 3–2 and 4–1 are Under; 3–3, 4–2, 5–1, 5–2 are Over. Motor −1.5 fails 3–2 and on any one-goal OT/SO win; succeeds 4–2 or 4–1. Extra-net risk may turn 3–2 into 4–2, hurting Lib+1.5 and helping Over.
- **Formal league baseline:** `BASELINE_LEAGUE_V1=NOT_COMPUTED`; only official league mean 6.1486 exists, not a certified same-threshold distribution/cohort. Official lineup effects not quantified; applying NHL distributions or 73% EN rule to Czech U20 would be invalid.

#### A5. All four contracts, hypothetical W/P/L/V and pair relations

| Supplied proposition | Qualitative preference | Shadow W/P/L/V (only under assumed operator) | Primary disposition |
|---|---|---|---|
| Motor −1.5 goals | lower-ranked side of spread pair | 0.4745 / 0 / 0.5255 / 0 | NOT_ESTIMATED, not qualified |
| Liberec +1.5 goals | secondary directional | 0.5255 / 0 / 0.4745 / 0 | NOT_ESTIMATED, not qualified |
| Total Over 5.5 goals | strongest directional | 0.6044 / 0 / 0.3956 / 0 | NOT_ESTIMATED, not qualified |
| Total Under 5.5 goals | less supported | 0.3956 / 0 / 0.6044 / 0 | NOT_ESTIMATED, not qualified |

All void values assumed zero **only in illustrative completed-game simulation**; real operator postponement, abandonment, shootout or settlement terms unknown. The first two proposed directional legs are **not independent**; the same Motor two-goal lead that defeats Lib+1.5 can coexist with an Over. Joint failure in simulated complete game states =0.1490, not calibrated. No numerical rank gate passed.

#### A6. Mechanisms, adjustments and counterfactuals

| Mechanism | Known evidence | Effect disposition | Unresolved response |
|---|---|---|---|
| Relative team strength | Motor +24 goals /19, Liberec −30/17; fifth vs fifteenth | Source-backed direction Motor outright, but no effect-table adjustment inferred | Elite goalies, lineup timing and variance may compress 2-goal spread |
| Motor recent defense | L5 allowed 10 goals, 2.0/game, stronger than full-season 2.37 | Widen defensive uncertainty; no automatic Under centre shift due overlapping form | If goalie substitution, this history may not transport |
| Liberec form rebound | Won 3/last 4, long-run defensive 4.18 against | Separate close-game and weak-goalie/large-tail scenarios | Small sample and opponent-strength mixture |
| H2H Sep19 | Motor 4–3 after extra time | One-goal caution for −1.5 and 7-goal path for Over, no direct rate bump | Personnel/regime continuity incomplete |
| Fatigue and travel | Both last played 31 October; youth international break; Liberec travels to České Budějovice and has 14-Nov Jihlava fixture | Potential future workload/context; not a quantified center effect | Travel distance, practices, goalie workload missing |
| Goalkeepers / skaters | Match-centre lineup blank before schedule; Motor season roster not game starters | Scenario widening only, no invented starting/backup grade | Exact starting goalies, lines, scratches, PP/PK details |
| Score state / empty net | Full-game −1.5 prone to late net-pull insurance goals | Model includes stylized EN scenarios for transparency | No measured Czech-junior EN frequency or validation; may double-count |
| Penalties / shot quality | Liberec scored 2 PP goals vs Litvínov on 24-Oct; game-specific units and shot-mix unknown | Mechanistic uncertainty, not a numeric adjustment | Current special teams, expected-goals shot data absent |

**Adjustment dependence:** synthetic scenario results vary with manually specified team λ and EN assumption; no official adjustment ledger, release or formal unadjusted ranking comparison. Independent-Poisson limitations dominate.

#### A7. Family consistency and non-primary comparison

- All shadow contract rows derived from the same simulated two-team score and time-state tree; complementary sums exactly 1 per scenario and mixture. One-goal OT branch never creates a two-goal winner; on 5.5 total, tie goals 0–0/1–1/2–2/3–3 plus one retain threshold classification versus 60 min; operator void still unknown.
- All applicable exact-row width/goaltender guards `NOT_ASSESSABLE` for a **primary** card. Model lacks release qualification, event-specific goalie variance, score covariance/overdispersion fit and official known-at baseline. Historical NHL one-goal percentages were NOT ported to Czech juniors.
- External betting-market odds, predictions and bookmaker probabilities were deliberately excluded. Published probability is **NOT_ESTIMATED** on every supplied row; the executed diagnostics are for sensitivity and not learning-eligible forecasts.

#### A8. Sources, failures, capture plan and no-outcome precautions

| Source or route | Pre-target field observed | Actual gap/limitation |
|---|---|---|
| `https://czehockey.cz/game/detail/178203` | Official U20 match 3156, venue, 12:00 CET fixture, empty game-day lineup tables before official start | Actual start/final/goaltenders NOT_VERIFIED; pregame 0:0 placeholder is not an actual score |
| `https://ceskyhokej.cz/competition/standings/1` | Official 2026/27 team table: full 16 teams, n, GF/GA, position, points | Snapshot modification times not exposed, event-level total history not exported |
| `https://www.hcbilitygri.cz/matches/JUN` | Official Liberec all 17 dated pregame fixtures and results, 12:00 CET current schedule | No exact current lineup, injury/return roster release; some older mirrored 15:30 pages conflict |
| `https://www.hcverva.cz/match/6814` | Liberec won Litvínov 4–3 OT, published 24-Oct and shots 34/26 | Not a pregame current-pace or goaltender estimate |
| `https://www.jchokej.cz/archiv-kratkych-zprav?page=2` | Motor lost 30 Oct HK 3–4, 31 Oct Pardubice 2–3 SO | Motor full L10–20 dated row pack incomplete |
| `https://hcmotor.cz/zapasy.asp?filtrTym=SLA&kde=vsechno&sezona=2027&stats=true` | Motor vs Slavia 3–1 on 19-Oct | Single indexed match, not entire seasonal game list |
| `https://hcmotor.cz/zapasy.asp?filtrTym=PLZ&kde=doma&sezona=2027&stats=true` | Motor vs Plzeň 5–1 on 23-Oct | Single indexed match, no full L15 history |
| `https://hcmotor.cz/soupiska.asp?kategorie=U20&sezona=2027` | Motor youth roster and potential named goalkeepers | Game starting status explicitly UNCONFIRMED |
| `https://m.onlajny.com/match/index/date/2026-11-13/id/540507` | Pre-match standings and scoring leaders, official 12:00 local listing | Live mutable feed deliberately NOT checked for outcome after start; independent organizer listing used |
| `https://hcmotor.cz/zapasy.asp?filtrTym=LIB&kde=vsechno&sezona=2027&stats=true` | Match U20 listed but an older mirror showed 15:30 CET | Time conflict retained, not silently treated as actual start |

**Failed/rejected histories:** broad `hcmotor.cz/zapasy.asp?sezona=2026U20` shows **2025/26** and would incorrectly join two seasons; excluded in favor of 2026/27 official federation and 2027 team-filtered match results. Some general club pages mix senior U18/U20 results; those are excluded. Exact injury/goalie evidence was not recovered and must not be assumed absent. No target live/final score searched after pre-event status check, so analysis avoids outcome-conditioned inputs; nevertheless the post-schedule output is NOT a pregame issue.

**Capture after explicit settlement request:** field owner full match report + match 3156 status and period scores/goalies/first puck; independent club Hokej.cz results; original score/goal sum; operator-defined void/OT as a separate term. No background monitoring was scheduled.

#### A9. Integrity receipt, completion matrix and limitations

| Procedure | Actual work performed | Gap / affected contract | Status |
|---|---|---|---|
| Exact event, source controls, duplicate and time | Czech federation match 3156, U20 aliases/venue, distinct from seniors/U18, current mini G0007 free; main SHA pinned | conflicting 12:00 vs archived 15:30 CET; actual first play unknown | DONE_WITH_GAP |
| Both teams' starters, bench, goaltenders, absences | Official blank game-day sheet checked; Motor season roster inspected; searched club/report pages | BOTH goalies, all starter/bench/medical and precise scratches remain unconfirmed | INFORMATION_INCOMPLETE |
| Verified prior games and independent search | Lib 17 dated club records; Motor five dated matches with club/regional corroboration; excluded stale previous-season page | Motor full L10/L15/L20, cross-field independent source per date incomplete | INFORMATION_INCOMPLETE |
| L5/L10/L15/L20, season, league | Exact Lib L5/10/15/17; Motor L5, season n19; league all 16 rows/148 games | Motor complete L10/L15; L20 has only n19 season aggregate not dated list | INFORMATION_INCOMPLETE |
| Sport mechanisms, venue, conditions, rules | Relative strengths, H2H, travel and break, shot/special-teams and empty-net risk, indoor applicability | field-owner youth OT/SO fine terms and goaltender performance | DONE_WITH_GAPS |
| Official reference, lineup mixtures, freeze, formal baseline | Read pinned rules and league mean; disclosed numerical model limitations | No repository model release/ref/freeze, no exact-row baseline cohort | NOT_RUN |
| Analytic distribution, assumptions, simulation | Deterministic 1.2m simulation script, output JSON, three rate/EN scenarios with actual model math | Unfitted youth league parameters, no measured goalie/score-state/shot model; shadow only | SHADOW_EXECUTED |
| Every owner line, complementary W/P/L/V | Four full-game contracts assessed with support, counterarguments and shadow exact masses | p_card formally NOT_ESTIMATED; operator void unresolved | DONE_QUALITATIVE |
| Expected scores, sensitivity, dependence, loss joint | Shadow 3.779–2.652, total6.431, scenario ranges; joint losing states 0.1490 | No fitted primary expected score or calibrated p | SHADOW_ONLY |
| A1–A9, local custody and readback | All appendices recorded and prior cards checked through local writer script | No GitHub commit, freeze, model receipt or C1–C27 repo lint by owner override | CHAT_LOCAL_ONLY |

**Overall research status:** `INFORMATION_INCOMPLETE`; missing fields explicitly held above. **Forecast:** `UNCALIBRATED_QUALITATIVE / EXECUTED_EXPLORATORY_1_200_000_SHADOW / PRIMARY_NOT_RUN`. **Issue:** `POST_OFFICIAL_SCHEDULE_TIME / ACTUAL_START_UNVERIFIED / CHAT_LOCAL_READ_ONLY_DRAFT / NOT_REPOSITORY_ISSUED`. **No strong/high-confidence pick.** **Model values are not published probabilities.** Local writer and footer/index readback receipt is separately saved after the append.

**SPORTS_ONLY_MARKET_BLIND:** YES · **OUTCOME_EXPOSURE:** NO_TARGET_LIVE_OR_FINAL_SCORE_USED · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0007 -->

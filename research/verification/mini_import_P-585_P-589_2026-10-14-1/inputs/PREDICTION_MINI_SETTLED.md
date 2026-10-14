<!-- MINI-LOG-FORMAT: mini-log-7 -->
# Prediction Mini Running Log — P-585 onward

## A. Authority snapshot
| Field | Value |
|---|---|
| Authority mode | `PUBLISHED_MAIN_PINNED 65f780cef9f1a97a411b47fcb08e2355eb1be897` |
| Repository / branch / read HEAD | `https://github.com/danisgreat/Sports-Research` / `main` (read-only); pinned commit `65f780cef9f1a97a411b47fcb08e2355eb1be897`; read `2026-10-13T15:55:33+11:00` (Australia/Melbourne) |
| Relevant working differences | N/A to `PUBLISHED_MAIN_PINNED`: published controls alone govern this mini; any unpublished checkout differences and user-machine writers NOT_VERIFIED, not applied |
| Method / control / scoring / selection | `MDS-2026.10.12-v11.0` / `CR-2026.10.12-R2` / `SCV-2026.10.12-v7` / `SEL-2026.10.12-v3` (`P_ORDER_V2`); suite `P-2026.10.12-v11.0`; `mini-log-7` |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_7.md` (Parts 1–6 historical/immutable) |
| Highest committed / next canonical ID | `P-584` / `P-585`; corroborated by `CURRENT_STATE.md`, `GAME_LOG_STATUS_CURRENT.md` current section, October 13 import report and P-580–P-584 source-to-canonical mapping; direct large Part 7 content fetch EMPTY (tail byte reread NOT_VERIFIED) |
| Reserved canonical IDs | `P-518`–`P-522` (reserved, not allocatable) |
| Outstanding local minis and IDs | **No unimported working ID found among inspected accessible local files**. Previous mini `ORIGINAL_MINI.md` / `CHAT_ACTIVE_MINI_P580_ONWARD_2026-10-12.md`: P-580–P-584, frozen at `2026-10-13T15:08:06+11:00`, all imported by October 13 canonical report; earlier canonical carryovers P-577–P-579 imported. Latest settled copy `PREDICTION_MINI_SETTLED.md` and manifest mapped P-577–P-584. **External user-machine minis, competing writers, unshared subsequent copies: NOT_VERIFIED, not claimed NONE.** |
| First working ID | **`P-585`** = max(canonical next `P-585`, highest verified unimported working ID+1 [none]); availability is conditional on renewed conflict/lease search at first card issue |
| Issuing writer / lease start / lease expiry | `ChatGPT — this conversation, active local mini` / `2026-10-13T15:55:33+11:00` / `2026-10-14T15:55:33+11:00` (24 h; no concurrent writer authorised by this file; lease renewal requires an explicit dated edit) |
| Lease hand-overs | NONE; frozen prior mini's distinct lifecycle is CLOSED_IMPORTED per import report; no active authorisation to append to it |
| Frozen for settlement | NO |
| Reading receipt / opened at | `PUBLISHED_MAIN_PINNED 65f780cef9f1a97a411b47fcb08e2355eb1be897` / `2026-10-13T15:55:33+11:00`; read: `README.md`; `CURRENT_STATE.md`; `METHOD.md`; `CURRENT_RULES.md` §0; `SELECTION_RULES.md`; `CARD_AND_LOG_TEMPLATES.md` §2; `research/prompts/2_START_LOCAL_MINI.md`; `research/prompts/README.md`; `research/prompts/examples/EXAMPLE_ACTIVE_MINI.md`; `GAME_LOG_STATUS_CURRENT.md` (current queue and P-577–P-584 entries); `research/verification/mini_import_P-577_P-584_2026-10-13-1/CANONICAL_IMPORT_REPORT.md`, `CANONICAL_ID_MAPPING.md`, `UNRESOLVED_POST_IMPORT.md`; checked Library's frozen original, settled mini, settlement manifest, report and accessible recent minis. Canonical Combined Log 7 direct body fetch returned EMPTY; relied on state/status/import byte mapping for tail. No sporting source, settlement or card work. |
| Mode | LOCAL_MINI_STAGING |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING

## B. Local ID rules
Creating this mini consumes no ID. One retained event receives one permanent working ID; canonical status requires an explicit authorised import. Addenda and carryovers consume none. No silent skipping, reuse, overwrite, duplicate-event cards or renumbering. Only a complete appended card successfully written and read back advances the mutable footer. The issuing writer above is the only writer during its valid lease. Another writer must await expiry and make a documented hand-over, or receive an explicit dated hand-over. Never append a card after this mini is frozen for settlement; start an authorised subsequent mini instead.

Before issuing the **first** new card, refresh the `main` current-state/status and import receipts, inspect new accessible mini files and their leases, confirm the identity is not already represented, and verify that `P-585` has not been locally assigned by another writer. Inaccessible external user-machine minis and potential parallel writers remain `NOT_VERIFIED`; if a competing lease, unexplained gap or duplicate is discovered, record request as `BLOCKED`, do not issue/advance any P-ID, and reconcile custody first. The `P-585` footer here is a working-ID *snapshot*, not a reservation or canonical consumption. Historical opening headers in Combined Logs do not supersede current-state records.

## C. Carryover and evidence queue
| ID | Event key | Queue | Original card / frozen pick table | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `P-584` (CANONICAL) | `MEX-LIGA-PREMIER-SERIE-A:2026-27:R7:DRAGONES-OAXACA-GUERREROS-PACIFICO:2026-10-12` · Dragones de Oaxaca vs Guerreros del Pacífico, 12 Oct Oaxaca | `PENDING_EVENT` | Part 7 `BEGIN CANONICAL RESEARCH P-584`; frozen original `ORIGINAL_MINI.md` `BEGIN CARD P-584` (around line 812), Decision block. **Diagnostic rows NOT_PRIMARY**; 90 min + stoppage, excludes post-match shootout and extra points, draw allowed; operator abandonment terms UNKNOWN | `revision-1` sporting settlement + phase `2026-10-13-PHASE-01`; terminal result not verified | Official terminal state, full-time regulation goals, first-half goals, match corners and exact field/operator action | Next user-invoked settlement session | Dragones official club fixture/calendar and Liga Premier match sheet: final status, FT score, HT score, corners, actual kickoff; BeSoccer match 2027176995 fallback | `2026-10-14T12:00:00+11:00` PROPOSED_MANUAL | UNKNOWN | `2026-10-13T15:15:00+11:00`, source package reported scheduled/not terminal; no new attempt in this mini | NO / NOT_SCHEDULED |
| `P-583` (CANONICAL) | `KBO:2026:REGULAR:20261012KTSS0` · KT Wiz @ Samsung Lions, 12 Oct 2026 | `UNRESOLVED_EVIDENCE` (terminal) | Part 7 `BEGIN CANONICAL RESEARCH P-583`; original `ORIGINAL_MINI.md` `BEGIN CARD P-583` (around line 591). **NO_FORECAST; no primary pick table**. KBO full-game regulation/extras (tie possible); operator shortening/action unknown | `revision-1`; sporting terminal observation retained, source conflict open | Reported final 4–2 conflicts with detailed cache 4–1; verify official detailed innings/total | Next settlement-correction review | KBO official game `20261012KTSS0` detailed box, runs by inning / R-H-E-B, compare official club result and Yonhap 4–2 | `2026-10-14T12:00:00+11:00` PROPOSED_MANUAL | UNKNOWN; report publication is not game-final time | `2026-10-13T15:15:00+11:00`, unresolved 4–1 vs 4–2 | NO / NOT_SCHEDULED |
| `P-581` (CANONICAL) | `DEN-SUPERLIGA:2026-27:DBU-556151:2026-10-11` · Brøndby IF vs Lyngby BK | `UNRESOLVED_EVIDENCE` (terminal; diagnostic only) | Part 7 `BEGIN CANONICAL RESEARCH P-581`; original `ORIGINAL_MINI.md` `BEGIN CARD P-581` (around line 249), frozen decision block; regulation 90 min + stoppage, draw allowed, corners field/operator UNKNOWN | `revision-1` terminal settlement | Confirm authoritative match-corners field 8 / 4 (secondary total 12), definition / field ownership | Next evidence review | DBU / Opta field-owner match stats: `wonCorners` Brøndby=8, Lyngby=4 | `2026-10-14T12:00:00+11:00` PROPOSED_MANUAL | UNKNOWN; DBU displays finished, no verified full-time wall clock | `2026-10-13T15:15:00+11:00`, 2 secondary sources give 12 | NO / NOT_SCHEDULED |
| `P-582` (CANONICAL) | `EPL:2026-27:ESPN-401879264:2026-10-11` · Liverpool FC vs Manchester City | `UNRESOLVED_EVIDENCE` (terminal; diagnostic only) | Part 7 `BEGIN CANONICAL RESEARCH P-582`; original `ORIGINAL_MINI.md` `BEGIN CARD P-582` (around line 397), frozen decision block; 90 min + stoppage, `wonCorners` convention/operator UNKNOWN | `revision-1` terminal settlement | Confirm EPL corner field definition, counts 5 / 6, operator action and dataset lineage | Next evidence review | Premier League official match stats `wonCorners` Liverpool=5, City=6; TNT Sports secondary 5/6 | `2026-10-14T12:00:00+11:00` PROPOSED_MANUAL | UNKNOWN; club site says FULL TIME, no verified full-time wall clock | `2026-10-13T15:15:00+11:00`, TNT Sports total 11 | NO / NOT_SCHEDULED |

| `P-585` (LOCAL_UNIMPORTED) | `ATP-SHANGHAI:2026:R16:ARTHUR-GEA:JAKUB-MENSIK:2026-10-13` · Arthur Gea vs Jakub Menšík, 13 Oct Shanghai | `PENDING_EVENT` (new local card; not imported) | This file `BEGIN CARD P-585` / Decision block, exact four supplied contracts, completed BO3 7-point tiebreak sets; operator retirement terms UNKNOWN | NONE; settlement NOT_PERFORMED | ATP official final match state, scores, games, any retirement, actual first serve and final | Next user-invoked settlement run | ATP event draw/scores exact-match; Tennis Majors / Sofascore fallback for official finished sets; operator written action rules separately | NOT_VERIFIED; within 72h of verified final, manual | UNKNOWN | Research/issue 2026-10-13T16:08:33+11:00, Tennis.com Upcoming at prewrite source; no terminal report | NO / NOT_SCHEDULED |

| `P-586` (LOCAL_UNIMPORTED) | `EUROCUP:2026-27:RS-R3:U2026-GAME47:BKS-MAN:2026-10-13` · Bahçeşehir Koleji Istanbul vs Kids&Us Manresa | `PENDING_EVENT` (new local card) | This file `BEGIN CARD P-586` Decision block; four supplied half-point full-game OT-inclusive propositions, operator action UNKNOWN | NONE; settlement NOT_PERFORMED | Official terminal 4Q/OT final, team scores, starters/bench, actual start/final, operator rules | Next user-invoked settlement run | EuroLeague EuroCup gamecode47 U2026 official terminal box / play-by-play | UNKNOWN until official final; manual within 72h of final | UNKNOWN | `2026-10-14T03:03:58+11:00` issue; last researched pre 03:00; no post-start evidence used | NO / NOT_SCHEDULED |

| `P-589` (LOCAL_UNIMPORTED) | `NHL:2026-27:REG:2026020105:BOS@SJS:2026-10-13` · Boston Bruins @ San Jose Sharks | `PENDING_EVENT` (new numeric local card; NOT prospective certified) | This file `BEGIN CARD P-589`, ML BOS/SJS + total O/U6.5 ranked supplied-only, timing late, final game state unverified | NONE | Final result and full-game OT/SO credited action, goalie/game sheet; operator terms UNKNOWN | NHL official box/event summary `2026020105`, final scores, players, period endpoint | AFTER VERIFIED FINAL (capture within 36 h subject to verification) | Final timestamp NOT_VERIFIED | NONE | NONE |

**Queue counts:** `PENDING_EVENT = 3` (P-584 canonical carryover; P-585 local new card); `UNRESOLVED_EVIDENCE = 3` terminal field-specific records (P-583, P-581, P-582). Pending-event cap threshold >5: NOT_TRIGGERED. **The four inherited queue records are previously canonical imports; P-585 is the new LOCAL_UNIMPORTED pending card**, not new `LOCAL_UNIMPORTED` IDs, and no forecast or frozen candidate table is reissued here.

**Grouped cross-event evidence dependencies (not additional sporting pending events):** `P-577`–`P-584` (8 imported events) have `OPERATOR_UNKNOWN` for written action/void/abandonment terms, only relevant to operator-grade reconciliation; due `USER_SUPPLIED`, actor user/next review, no automation. `P-577`–`P-583` (7 terminal records) have actual final wall-clock / 72-hour SLA `NOT_VERIFIED`; actor next evidence review, due NEXT_REVIEW / NOT_SCHEDULED. Four separately named source-companion files were not supplied in the preceding import package: retained documentary custody limitation, NOT new forecast records. P-577–P-579 original-core comparison resolved by import; no queue reissue. All terminal scores and Rank-1/Rank-2 original grades remain frozen and referenced, not replicated.

**Previous local inventory / disposition:** `P-577`–`P-579`: canonical before this mini, now source-core comparison RESOLVED_WITH_POINTER (October 13 importer). `P-580`–`P-584`: local in frozen `ORIGINAL_MINI.md` (5 complete cards), imported exactly once into Part 7 under their unchanged IDs (mapping and October 13 report). P-584 terminal sporting evidence outstanding; P-583/P-581/P-582 specific terminal evidence still open; remaining completed records reference their imported parent/settlement revisions. **Verified unimported local working ID range: NONE in accessible files**; user-machine copies and concurrent external writers `NOT_VERIFIED`. The old `mini-log-6` header/footer is a frozen *historical* record; do not append to or correct it here. ID continuity: imported P-577→P-584, then prepared P-585; no verified gap or overlap. P-518–P-522 stay reserved and are not silently allocated.


**Queue update on P-589 issue 2026-10-14T14:17:28+11:00:** PENDING_EVENT=6 (P-584 canonical and P-585..P-589 local), UNRESOLVED_EVIDENCE=3; >5 pending threshold TRIGGERED, explicit manual review warranted. Earlier header count remains a dated snapshot, mutable footer now controls.

## D. Request intake
| Request key | Received (ISO, tz) | Event / alias as requested | Disposition | Card or addendum pointer, or no-card reason |
|---|---|---|---|---|
| REQ-P585-20261013-160833 | `2026-10-13T16:08:33+11:00` | Arthur Gea vs Jakub Mensik, ATP Shanghai Round 4, four specified supplied lines, 16:30 AEDT estimated | CARD | `BEGIN CARD P-585` / `END CARD P-585` in this local file; no canonical import |

| REQ-P586-20261014-030358 | `2026-10-14T03:03:58+11:00` | Bahçeşehir Koleji Istanbul vs Kids&Us Manresa, EuroCup R3, 03:00 AEDT, supplied −13.5/+13.5 and Over/Under178.5; supplied-only | CARD | `BEGIN CARD P-586` / `END CARD P-586`; LATE_START_UNVERIFIED, starting five/bench unconfirmed |

| REQ-P587-20261014-125803 | `2026-10-14T12:58:03+11:00` | CGY Flames @ ANA Ducks, NHL 2026-10-13, 12:52 AEDT estimated (official 12:45); 4 exact supplied sides / SF-2 | CARD: LATE_START_UNVERIFIED | `BEGIN CARD P-587` / `END CARD P-587`, numeric scenario, operator definitions UNKNOWN; pregame certification NOT_CLAIMED |

| REQ-P588-NBA-0012600048 | `RECEIVED_TIME_NOT_VERIFIED` (request was already present by first observed local clock `2026-10-14T13:01:07+11:00`; issue/processing time is recorded in card) | GS Warriors @ LA Lakers, NBA preseason, user 2026-10-14 13:00 AEDT, four distinct ±2.5 & Over/Under 228.5 supplied; SF-2 | CARD: LATE_START_UNVERIFIED / UNCALIBRATED_ANALYST_SCENARIO | `BEGIN CARD P-588` / `END CARD P-588`, local-only, lineup/actual start/operator definitions unverified; no canonical import |

| REQ-P589-NHL-2026020105 | `RECEIVED_TIME_NOT_VERIFIED` (first research clock approx 2026-10-14 14:04 AEDT; exact issue at 2026-10-14T14:17:28+11:00) | BOS Bruins @ SJ Sharks, NHL 2026-10-14 estimated 14:07 AEDT, official 14:00; 4 literal ML and +/-6.5 full-game propositions; SF-2 | CARD: LATE_START_UNVERIFIED / UNCALIBRATED_ANALYST_SCENARIO | `BEGIN CARD P-589` / `END CARD P-589` in this mini; working P-589 unimported; no settlement |

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD P-585 -->
## Card · P-585 · TENNIS / ATP Masters 1000 Shanghai 2026 · Arthur Gea vs Jakub Menšík · 2026-10-13

- **Working ID:** `P-585` — `LOCAL_WORKING_ID` — `PENDING_CANONICAL_IMPORT`, issued to the active chat mini only after local write/readback. This is not an imported canonical card.
- **Event key / native ID / aliases:** `ATP-SHANGHAI:2026:R16:ARTHUR-GEA:JAKUB-MENSIK:2026-10-13`. Native ATP match ID `NOT_VERIFIED`; TennisDB event `4709456` and Sportschau `ma11762227` secondary pointers, not ATP-native IDs. Alias Arthur Géa / Gea; Jakub Menšík / Mensik. H2H 0–0 according to contemporary pre-match source; no event duplicate found in the accessible current mini or current tracked canonical index.
- **Authority:** `PUBLISHED_MAIN_PINNED 65f780cef9f1a97a411b47fcb08e2355eb1be897`; MDS-2026.10.12-v11.0 / CR-2026.10.12-R2 / SCV-2026.10.12-v7 / SEL-2026.10.12-v3; `mini-log-7`. User superseding card policy `SUPPLIED_FIRST_V1`: supplied contracts only for primary ranks; published full-universe selection is reported only as shadow.
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO` / `RESEARCH_ONLY_NOT_CERTIFIED` / `ISSUED_LOCAL_WITH_ACTUAL_START_NOT_VERIFIED`. No fitted/calibrated match model, no operator-specific grade or clean prospective certification.
- **Timing:** input known-at cutoff = research completion / last sporting-source read roughly `2026-10-13T16:08:33+11:00`. Local card file completion/issue = `2026-10-13T16:08:33+11:00` (readback to follow). Last explicit cross-source state check before write: Tennis.com `Upcoming`, Sofascore scheduled with `05:10 UTC`, other providers `05:30 UTC`; **independently verified actual first serve NOT_VERIFIED**. Scheduling lead to earliest dynamic 16:10 estimate at issue `1.45 minutes`; issue band `SCHEDULED_LEAD_LE_5 / ACTUAL_START_NOT_VERIFIED`. The user's original 16:30 AEDT was a stated estimate, not a fixed first-serve receipt. No source match outcome used.
- **Scheduled start:** `2026-10-13T12:00:00+08:00` is first Stadium Court match (De Minaur–Khachanov), NOT this match. This match follows it on Stadium Court, Qizhong Forest Sports City Arena, Shanghai: indicative provider estimate 2026-10-13T13:10:00+08:00 = `2026-10-13T05:10:00Z` = `2026-10-13T16:10:00+11:00` AEDT; another estimate `05:30Z / 16:30 AEDT`. **Official fixed time not established.** Match order and start depend on earlier match length and potential suspension.
- **Endpoint / definition:** ATP men's singles Round 4 / last 16, outdoor hard, **best of 3 standard tiebreak sets**; 6–6 leads to 7-point set tiebreak won by 2 (including any deciding set), no deciding *match* supertiebreak. Match games sum games actually won by both players (a 7–6 set has 13 games; tiebreak points never add games). Games handicap `Gea +2.5` means Gea total games minus Mensik total games >= −2 (integer); `Mensik −2.5` means Mensik minus Gea >= 3. Totals 23.5: Over >=24, Under <=23. All four half-game contracts decisive on normal completed matches (no push). Walkover/retirement/abandonment: framework sporting research treats uncompleted game markets as unresolved/VOID under the framework convention, **subject to original operator written terms, currently UNKNOWN_DEFINITION**. Already irrevocably decided totals on retirement may differ by operator; no assumed settlement. Match winner on retirement is separate from full-games grade.
- **Distribution object:** `P585_ATP_BO3_SERVICE_GAME_TREE_3CASE_v1`: service-game Markov model, case hold rates `(h_G,h_M)` LOW `(0.78,0.87)`, BASE `(0.80,0.86)`, HIGH `(0.82,0.85)`, mixture weights `(0.25,0.50,0.25)`. LOW/HIGH labels refer to Gea's competitive state. Each service game's holder wins with that side's model hold probability. Both possible first-server states are given 0.5 each; set first-server parity is **approximated independently** across sets, not asserted as official service order. At 6–6, tiebreak probability is calculated from serve-point strengths obtained by inversion of the advantage-game formula (A4). All set-score possibilities to 7–6 are enumerated; a new set is needed only at 1–1 sets. Total scenario outcome mass exactly 1. This is an **unfitted, subjective** matchup-level approximation, not ATP-calibrated data; first-server independence is a known model limitation.
- **Expected score:** Gea `11.919` match games (SD `3.992`), Mensik `13.548` (SD `3.152`); total `25.467` (SD `6.030`); signed Gea−Mensik margin `-1.628` (SD `3.923`); expected sets `2.469`, deciding-set probability `46.95%`. Tiebreak set counts 13 games; no exact final set score claimed.
- **Baseline:** `BASELINE_LEAGUE_V1 = BASELINE_UNAVAILABLE`: no independent, pre-cutoff, same-format ATP men's hardcourt population score-grid with exact 23.5 total and ±2.5 games values was verified at issue. Historical men BO3 deciding-set **reference** 0.358 from RULES_TENNIS §0.3 is descriptive, NOT a same-row BASELINE_P. `BASELINE_P` is missing on all four lines (0/4); no fabricated 0.50 comparator or post-issue fill.
- **Regime/context:** `ATP_M1000_OUTDOOR_HARD`; Gea recent upset of Shelton and short Shanghai run; Menšík higher-ranked and stronger established tour profile. Official full injury/withdrawal clearance and actual in-venue match-start verification unavailable; status `PARTICIPATION_LISTED`, `MEDICAL_CLEARANCE_NOT_VERIFIED`. Both had Oct 11 R32 matches; no match-day fitness examination obtained. Recent form source has restricted tour main-draw coverage and differing qualifying/Grand Slam samples; quality adjustment explicitly subjective.
- **Settlement fields/capture:** official ATP result with match ID, final state, winner, exact set games and tiebreaks; completed match total Gea/Mensik games and sum, set count, 6–6 final-set tiebreak, any retirement/walkover/suspension; obtain official start/final wall-clock, written operator specific abandonment/retirement terms. Owner: next user-invoked settlement session. Source order ATP results/draw → Tennis Majors/Sofascore exact-match score fallback (independence NOT_VERIFIED). Suggested manual follow-up after completed match and within 72h of verified final; **AUTOMATION NOT_SCHEDULED**, time DUE_UNKNOWN without verified final wall-clock.
- **Rules read / archive check:** pinned README, CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES §§2–3/7, SCORING_AND_VALIDATION, PROBABILITY_TOOLKIT §6 and game formulas, research/prompts/1_GAME_CARD.md, prompt index, VERIFICATION_PROTOCOL, RULES_TENNIS §0, SOURCES §3.10, ARCHIVE_USE_GUIDE, ACTIVE_FILE_INDEX, LEAGUE_PROFILES, BASE_RATES_REGISTER §7.4 and this user-supplied card specification. Tennis yearly archive is described as header-only by active guide/index; attempted `Previous Sports Results/Tennis/ATP/2026/2026_games.csv` pinned path was NOT_FOUND; **0 admissible ATP archive rows read**. Replaced with dated TennisDB player score logs plus Tennis Abstract sport source (current snapshot/field limitations below). Latest imported canonical ID P-584 from state/status/report; not a duplicate of Gea–Menšík. Full Part 7 body fetch still unavailable from connector; external competing local writers NOT_VERIFIED.
- **Evidence receipt:** primary source URLs and exact evidence in A8; research input freeze `2026-10-13T16:08:33+11:00` Australia/Sydney. All sporting records selected are dated before 13 October. No outcomes of this fixture; no odds, tips, or commercial lines used for estimation.

### Decision block — SUPPLIED_FIRST_V1 (four supplied contracts only)

**Assessment:** In a best-of-three matchup, the service-game model favours Menšík's match victory but expects frequent close sets. Because the line is only 23.5 total games, **Over 23.5** is narrowly ahead of **Menšík −2.5 games**. Both are weak, highly sensitive directional rankings; neither clears the numerical selection gate, and a claimed high-confidence pair would be unjustified.

| Rank | Role | Tag | Contract key / exact supplied proposition | p_card (mixture) | p_base | BASELINE_P | Line distance (model centre; units / z) | Probability basis | Main failure route |
|---|---|---|---|---:|---:|---|---|---|---|
| 1 | PICK | SUPPLIED | `total_games:over:23.5:completed_bo3`: **Total match games Over 23.5** (24+) | `52.50%` | `52.80%` | BASELINE_UNAVAILABLE | 23.5−25.467=-1.967 games / `-0.326` | P585 3-case complete-match tree | Short straight-sets match <=23 games |
| 2 | PICK | SUPPLIED | `aggregate_games_margin:mensik_minus:2.5:completed_bo3`: **Menšík −2.5 total games** (wins margin >=3 games; may win or lose match) | `51.61%` | `51.67%` | BASELINE_UNAVAILABLE | 2.5−1.628=+0.872 games / `+0.222` | Same model | Gea keeps total game margin within 2 or leads |
| 3 | INFORMATIONAL | SUPPLIED | `aggregate_games_margin:gea_plus:2.5:completed_bo3`: **Gea +2.5 total games** | `48.39%` | `48.33%` | BASELINE_UNAVAILABLE | −2.5−-1.628=-0.872 games / `-0.222` | Same model | Menšík accumulates >=3 more total games |
| 4 | INFORMATIONAL | SUPPLIED | `total_games:under:23.5:completed_bo3`: **Total match games Under 23.5** (<=23) | `47.50%` | `47.20%` | BASELINE_UNAVAILABLE | 23.5−25.467=-1.967 games / `-0.326` | Same model | >=24 games from long two-set/three-set match |

**SUPPLIED_CONTRACT_RANKING (all four, unconditional on supplied-contract ordering):** Over 23.5 > Menšík −2.5 games > Gea +2.5 games > Under 23.5. Every submitted contract frozen; no analysts' replacement line promoted. `SUPPLIED_FIRST_V1` is the explicitly user-authorised local selection scope, **not** the baseline published P4 full-universe selection policy.

**Probability accounting:** four rows use **completed match** as the sample space: `W = p_card`, `PUSH=0`, `LOSS=1−p_card`, `VOID=0 conditional on completed match`; p_card = W/(W+L). Whole-world **pre-completion** probabilities of retirement/walkover/VOID are `NOT_ESTIMATED`, so none is presented as unconditional over all possible disruptions. Complete scores have no ties/draws: winner Menšík `67.13%` / Gea `32.87%`, total 100% (not the game handicap).

**Baseline coverage:** 0/4 exact supplied lines. **Rank-1 gate:** `SUPPLIED_SCOPE_GATE=RANK1_UNSTABLE`: 52.50% vs required >=62%, next non-complementary eligible supplied alternative Menšík −2.5 51.61%, difference ~0.89 percentage points (<4 pp). `GATE_NOT_VALID_AS_PUBLISHED_FULL_UNIVERSE`. **Rank-2 floor:** `BELOW_FLOOR` (51.61% <58%). Both below 90% selection ceiling. Ranking precision is robust to enumeration rounding but not to parameter selection.

**Joint failure / dependency:** Rank 1 loses when total <=23; Rank 2 loses when Menšík advantage <=2; model P(both fail) = `12.82%` (exact joint model, NOT sum of margins). P(both win) = `16.94%`. The top-two pair is not a complete complement pair, **not** MECHANICALLY_PROTECTED; however all four supplied contracts comprise *two* pairwise complements, so two independent trials cannot be inferred. P(a decisive outcome for both top ranks | completed) = 100%; model P(at least one top two wins) = `87.18%` under the unfitted assumptions, not a performance claim. Model joint failure can be as low as zero only in some hypothetical distributions; this estimate is not evidence of independent protection.

**Shadow gate / Rank 2:** `SHADOW_MAIN_P_ORDER_V2=NOT_COMPUTED` because a frozen supported combined supplied-and-derived universe was not constructed; `RET03/RET04/XCARD6=NOT_COMPUTED` beyond the four-row supplied-scope comparison; `SHADOW_RANK_DELTA=NOT_COMPUTED` (no baseline), `SHADOW_BASE_ONLY` same sorted four rows as primary. All are `NOT_PRIMARY` and not extra training wagers. **Adjustment dependence:** quality adjustments (Gea hold −2.6pp versus raw last-52 hard, Menšík +1.9–2.1pp) are subjective and may reverse rank order with alternative parameters; `ADJUSTMENT_DEPENDENT / LARGE_ADJUSTMENT_NOT_COMPUTED` in SD units. No alternative priced ladder introduced.

**Most likely match winner:** **Jakub Menšík `67.13%`** (completion, incl. all third-set tiebreak outcomes); Gea `32.87%`; H2H no prior meeting verified; winner not one of the user-supplied contracts.

### Appendix
#### A1. Identity, timing and state
- Tennis.com event (Round 4, Stadium Court) `https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/a-gea-vs-j-mensik-2026-10-13`, displayed **Upcoming** during the 13-Oct retrieval. Sofascore `https://www.sofascore.com/tennis/match/arthur-gea-jakub-mensik/mWYcsMEdd` has 13-Oct 05:10 UTC estimated start (16:10 AEDT); Tennis365 05:30 UTC estimates 16:30 AEDT; Tennis Tour Calendar `https://tennistourcalendar.com/2026-rolex-shanghai-masters-daily-schedule-order-of-play-and-results/` explicitly says *Followed By* De Minaur–Khachanov (not an independently fixed start). Exact actual first-serve timestamp `NOT_VERIFIED`. Later source updates must not be backdated to this receipt.
- Round is **R16 = Round 4**; court Shanghai Stadium Court, outside hard. Tour is ATP men's singles, not Challenger/WTA. Order and identity supported by independent calendars and TennisDB `https://tennis-db.com/matches/4709456/arthur-gea-vs-jakub-mensik` (secondary ID). Official ATP match-specific scoreboard/draw payload `NOT_VERIFIED` at issue; ATP season schedule and governing rules verified.
- Duplicate review: existing local carryover contains P-581/582 soccer, P-583 baseball, P-584 soccer; this event isn't among P-577–584 current canonical status entries. Current working mini previously no NEW CARD entries; no stronger claim regarding inaccessible user-machine writers. Original mini lease remains within 24h, frozen NO, this chat writer matching. Repository `main` remained at the receipt SHA on recheck before construction.

#### A2. Frozen supplied contracts and candidate recipe

| Supplied intake | Contract key | Completed-match sporting definition | W/P/L/V required |
|---|---|---|---|
| Gea +2.5 Games | `gea:+2.5:all-match-games:bo3` | Gea total >= Mensik total −2 | W=48.39%, P=0, L=51.61%, V=0 (completed) |
| Mensik −2.5 Games | `mensik:-2.5:all-match-games:bo3` | Mensik total >= Gea total +3 | W=51.61%, P=0, L=48.39%, V=0 (completed) |
| Over 23.5 Games | `games:over:23.5:bo3` | Gea+Mensik >=24 | W=52.50%, P=0, L=47.50%, V=0 (completed) |
| Under 23.5 Games | `games:under:23.5:bo3` | Gea+Mensik <=23 | W=47.50%, P=0, L=52.50%, V=0 (completed) |

- Complement identities checked: `p(Gea+2.5)+p(Mensik−2.5)=1`, `p(Over23.5)+p(Under23.5)=1` on completed BO3. A games handicap is **not** a sets handicap: Menšík can win 2–1 and fail −2.5 games, or lose and cover a positive games handicap. No implied match winner from a game-margin line.
- Frozen case parameters and ranking: 3 cases × complete set/match joint grid; tie break games one actual game; regular sets terminate at ≥6 games + margin 2 or 7–6 tiebreak. Candidate threshold and stable tie-break key set before pricing. Derived line ladder intentionally excluded under user instruction, not a zero-probability claim.

#### A3. Evidence and archive inputs; same-surface/format L5/L10/L15/L20
**Strict cohort:** outdoor hard, ATP Tour *main draw*, best-of-three, completed, 2026 before this match; exclude qualifying rounds and Grand Slams best-of-five, exhibitions/Davis Cup, walkovers and retirements. A tour-only TennisDB match log is the trace, NOT a fitted sample. Means below are **games per completed match**, NOT serves held or predicted BO3 game totals; windows overlap and are **counted once** in modelling. ATP rankings of opponents are as listed by TennisDB with page's match-context ranking, not backdated independently.

**Gea — strict ATP BO3 outdoor hard**
| Window | n | Dates (oldest–latest) | W–L | Games won per match | Games conceded per match | Signed game margin/match | Mean listed opponent rank | Three-set matches |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| L5 | 5 | 2026-09-30 to 2026-10-11 | 4–1 | 14.80 | 11.80 | +3.00 | 60.0 | 3 |
| L10 | 10 | 2026-07-28 to 2026-10-11 | 9–1 | 14.70 | 10.90 | +3.80 | 77.2 | 6 |
| L15 | 10 | 2026-07-28 to 2026-10-11 | 9–1 | 14.70 | 10.90 | +3.80 | 77.2 | 6 |
| L20 | 10 | 2026-07-28 to 2026-10-11 | 9–1 | 14.70 | 10.90 | +3.80 | 77.2 | 6 |

**Menšík — strict ATP BO3 outdoor hard**
| Window | n | Dates (oldest–latest) | W–L | Games won per match | Games conceded per match | Signed game margin/match | Mean listed opponent rank | Three-set matches |
|---|---:|---|---:|---:|---:|---:|---:|
| L5 | 5 | 2026-08-19 to 2026-10-11 | 3–2 | 12.20 | 11.20 | +1.00 | 34.6 | 2 |
| L10 | 10 | 2026-08-07 to 2026-10-11 | 7–3 | 11.90 | 11.00 | +0.90 | 47.1 | 3 |
| L15 | 15 | 2026-03-21 to 2026-10-11 | 10–5 | 13.40 | 12.00 | +1.40 | 77.0 | 8 |
| L20 | 17 | 2026-03-06 to 2026-10-11 | 11–6 | 13.24 | 12.18 | +1.06 | 73.1 | 9 |

**Cohort reconciliation:** Gea L15/L20 are **n=10**, not an invented 15/20; Menšík L20 n=17. Gea strict L5 4–1 over Shelton, Humbert, Faria, Hurkacz, Zhang; strict L10 9–1 adding Shapovalov, Coleman Wong, Francisco Cerundolo, Michael Zheng, Soonwoo Kwon. Menšík strict L5 3–2 against Cerundolo×2, Kecmanovic, Bublik, Tirante; L10 7–3. Court-level confound: Menšík's opponent list is substantially stronger on average than Gea's wider broader hard sample, and Gea's Shanghai wins are more recent. An unadjusted window blend cannot legitimately be called a calibrated head-to-head serve model.

**Supplemental all-format hard-court 2026 L5/L10/L15/L20 (not mixed into strict BO3 means):** Gea W/L 4–1, 8–2, 12–3, 16–4, including 5 best-of-five Grand Slam matches and 5 qualifiers in the last 20, against largely weaker listed opposition; Menšík 3–2, 7–3, 10–5, 13–7, including 3 best-of-five US Open matches. Note a 2026 Davis Cup hard-court match appears on Tennis Abstract that TennisDB's ATP main-draw list does not include. For Gea, the 20th all-format hard record extends back to Jan 22 Australian Open; do not call a 20-match 2026 BO3 tour cohort. The unnormalised all-format games per match are longer when Bo5 is present and should not be plugged into a Bo3 projected total.

**Event-level trace — Gea 20 hard matches, player-perspective score, dated BEFORE forecast**:
| Date | Opponent | Listed rank | Sets/games result | W/L | Format | Competition role |
|---|---|---:|---|---|---|---|
| 2026-10-11 | Shelton | #4 | 7-6(5) 7-6(3) | W | Bo3 | Masters |
| 2026-10-09 | Humbert | #32 | 6-4 3-6 6-1 | W | Bo3 | Masters |
| 2026-10-07 | Faria | #60 | 6-7(3) 6-1 6-2 | W | Bo3 | Masters |
| 2026-10-02 | Hurkacz | #39 | 6-7(5) 7-6(5) 2-6 | L | Bo3 | ATP 500 |
| 2026-09-30 | Zhang | #165 | 6-4 6-3 | W | Bo3 | ATP 500 |
| 2026-09-29 | Machac | #75 | 6-3 6-4 | W | Bo3 | ATP qualifying |
| 2026-09-28 | Rigele Te | NOT_VERIFIED | 6-2 6-3 | W | Bo3 | ATP qualifying |
| 2026-09-07 | van de Zandschulp | #70 | 6-3 7-6(0) 6-7(7) 6-7(3) 4-6 | L | Bo5 | Grand Slam |
| 2026-09-05 | Michael Zheng | #107 | 7-6(7) 3-6 4-6 6-3 6-2 | W | Bo5 | Grand Slam |
| 2026-09-03 | Zachary Svajda | #80 | 5-7 6-3 6-2 6-2 | W | Bo5 | Grand Slam |
| 2026-09-01 | J M Cerundolo | #45 | 6-3 2-6 3-6 6-3 6-1 | W | Bo5 | Grand Slam |
| 2026-08-28 | Basavareddy | #163 | 3-6 1-6 | L | Bo3 | ATP qualifying |
| 2026-08-26 | Chidekh | #185 | 6-4 6-7(4) 6-2 | W | Bo3 | ATP qualifying |
| 2026-08-25 | Nagal | #234 | 6-3 7-6(4) | W | Bo3 | ATP qualifying |
| 2026-08-01 | Shapovalov | #68 | 6-3 6-4 | W | Bo3 | ATP 250 |
| 2026-08-01 | Coleman Wong | #108 | 7-6(7) 6-3 | W | Bo3 | ATP 250 |
| 2026-07-31 | F Cerundolo | #20 | 6-7(11) 6-4 6-0 | W | Bo3 | ATP 250 |
| 2026-07-30 | Michael Zheng | #118 | 0-6 6-4 6-0 | W | Bo3 | ATP 250 |
| 2026-07-28 | Kwon | #158 | 6-4 6-7(8) 6-2 | W | Bo3 | ATP 250 |
| 2026-01-22 | Wawrinka | #139 | 6-4 3-6 6-3 5-7 6-7(3) | L | Bo5 | Grand Slam |

**Event-level trace — Menšík 20 hard matches, player-perspective score**:
| Date | Opponent | Listed rank | Sets/games result | W/L | Format | Competition role |
|---|---|---:|---|---|---|---|
| 2026-10-11 | F Cerundolo | #20 | 6-3 3-6 6-2 | W | Bo3 | Masters |
| 2026-10-09 | Kecmanovic | #61 | 6-3 6-3 | W | Bo3 | Masters |
| 2026-10-03 | F Cerundolo | #22 | 3-6 3-6 | L | Bo3 | ATP 500 |
| 2026-10-01 | Bublik | #20 | 6-4 7-6(5) | W | Bo3 | ATP 500 |
| 2026-09-05 | Tien | #15 | 3-6 6-1 7-6(2) 3-6 4-6 | L | Bo5 | Grand Slam |
| 2026-09-03 | Rodionov | #143 | 6-3 3-6 6-2 6-3 | W | Bo5 | Grand Slam |
| 2026-08-31 | Mochizuki | #117 | 6-1 6-4 7-5 | W | Bo5 | Grand Slam |
| 2026-08-19 | Tirante | #50 | 7-5 4-6 4-6 | L | Bo3 | Masters |
| 2026-08-17 | Hijikata | #95 | 6-3 6-4 | W | Bo3 | Masters |
| 2026-08-15 | Bellucci | #81 | 7-5 2-6 7-6(5) | W | Bo3 | Masters |
| 2026-08-11 | Shelton | #6 | 3-6 1-6 | L | Bo3 | Masters |
| 2026-08-09 | van de Zandschulp | #70 | 6-4 7-5 | W | Bo3 | Masters |
| 2026-08-07 | Atmane | #46 | 7-5 6-4 | W | Bo3 | Masters |
| 2026-08-05 | Fearnley | #110 | 6-3 3-6 6-3 | W | Bo3 | Masters |
| 2026-07-30 | Nakashima | #33 | 6-7(5) 6-3 4-6 | L | Bo3 | ATP 500 |
| 2026-07-28 | Svajda | #436 | 6-2 6-7(5) 6-3 | W | Bo3 | ATP 500 |
| 2026-03-23 | Tiafoe | #20 | 6-7(4) 6-4 6-7(11) | L | Bo3 | Masters |
| 2026-03-21 | Walton | #85 | 3-6 6-2 6-4 | W | Bo3 | Masters |
| 2026-03-08 | Davidovich Fokina | #19 | 2-6 6-4 2-6 | L | Bo3 | Masters |
| 2026-03-06 | Giron | #69 | 7-5 7-6(4) | W | Bo3 | Masters |

**Serve/return numerical source:** Tennis Abstract snapshot results: Gea last-52 hard (at last viewed source) 82.6% games held, 30.7% return games broken, service-points-won 65.1%, return-points-won 41.3%, first-serve in 59.7%, first-serve points won 73.7%; Menšík last-52 hard 83.9–84.4% hold, 21.0–21.8% breaks, serve-points-won ~66.3–66.8%, return-points-won 36.8–37.2%, first-serve in 59.8–60.1%, first-serve points won 79.1%. These sources have **snapshot changes and insufficient eligible match-by-match point numerators** for validated current paired matchup calibration: no exact n of service games or historical source publication timestamp established. Retain fields as descriptive aids only. Measured detailed official National Bank Open 2026 match vs van de Zandschulp: Mensik first-serve in 67% (42/63), won 81% of first-serve points (34/42), return points won 39% (26/66); one-match n=1, not a season prior.

**Form weights / shrinkage:** overlapping L5→L20 do not add their n. No fitted R2 per-match shrinkage coefficient was available for tennis at issue, so `R2_BLEND_NOT_ESTIMABLE`; the scenario holds are anchored descriptively on last-52 hard historical hold%, then adjusted by explicit *subjective* opponent-quality and recent opponent/tournament-level terms. Zero evidence of model validation. Gea recent 7–6 7–6 over Shelton (Oct 11) includes 75% first-serve points won in that single match, 4 aces and three breaks (Tennis Majors); not extrapolated as 75% next-match hold. Menšík Oct 11 three-set over Cerundolo 6–3,3–6,6–2 is an observed workload proxy; rest days 2 calendar days since last match for both. Actual minutes for all last 20 matches, opponent-strength Elo, verified match-day hydration/medical and serve numerators per event unavailable: `NOT_VERIFIED`.

#### A4. Distribution, baseline, expected score and arithmetic
Game hold chosen by subjective quality adjustment to raw last-52 hard court, not by a trained formula:

| Case | Weight | Gea games held if serving | Menšík games held if serving | Gea point-on-serve (inverse) | Menšík point-on-serve (inverse) | Gea tiebreak win approx | Menšík match win | Over23.5 | Menšík−2.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LOW | 78.00% | 87.00% | 62.22% | 67.63% | 41.01% | 74.82% | 49.23% | 60.13% |
| BASE | 80.00% | 86.00% | 63.29% | 66.94% | 43.91% | 67.35% | 52.80% | 51.67% |
| HIGH | 82.00% | 85.00% | 64.43% | 66.27% | 46.90% | 58.99% | 55.19% | 42.99% |

Derivation: Standard advantage-game holding function at serve point win `p`, q=1−p: `H(p)=p^4 (1+4q+10q²) + 20p³q³ × p²/(p²+q²)`. Numerically invert H(p)=h for each player/case. Tiebreak first server equally Gea/Menšík, serve order 1–2–2–2…; win at 7 points with 2 lead, recursively enumerate score/serve states and truncate the ultra-small continuation beyond 80 points (absorbing residual 0.5; numerical error negligible at displayed precision). For each set, alternate service games, sum all final 6–0 through 7–6 scorelines including 6–6 tiebreak. Start first service uniformly per set as an approximation; combine two set distributions, and take a third set exactly when first two split. This yields a joint probability mass on `(games_G, games_M, sets, winner)`; normalize each case (sum=1); use mixture `0.25 LOW +0.50 BASE +0.25 HIGH`. This process **does not model point correlation, fatigue, real tiebreak serve carryover or verified dynamic server parity**. It is conditional on a completed match, constant serve probabilities within each case, not a simulation of observed player outcomes.

Exact contract enumeration: `p(Over23.5)=Σ mass[g+m≥24]=52.50%`; `p(Menšík−2.5)=Σ mass[m−g≥3]=51.61%`; `p(Gea+2.5)=Σ mass[g−m≥−2]=48.39%`; `p(Under23.5)=Σ mass[g+m≤23]=47.50%`. `p(Menšík winner)=67.13%`. `P(3 sets)=46.95%`, compared with **historical men BO3 descriptive** 0.358 from RULES_TENNIS; elevated decider mass follows closer model holds, not a proven regime parameter. Total SD `6.030` versus reference men BO3 raw 6.00; model total games mean `25.467`. Cov(G,M) positive, ≈`5.24` game²; do not set total and margin variance by independence of game counts. Mixture variance includes both each-case variances and between-case mean dispersion.

**Baseline attempt** `BASELINE_LEAGUE_V1`: requires frozen ATP men's hard BO3 per-event score matrix independent of players and no future events, to price exact lines and endpoint. `ACTIVE_FILE_INDEX` and `ARCHIVE_USE_GUIDE` indicate no populated tennis yearly archive; direct ATP/2026 CSV path 404. BASE_RATES_REGISTER historical `P(3set)=0.358` does not price exact games handicaps / 23.5 total; `BASELINE_P=BASELINE_UNAVAILABLE:missing documented independent same-contract grid` on 4/4. No invalid equivalence between Tennis Abstract cohort hold and league-only baseline.

**Elo check:** Tennis Abstract recent pages report Gea Elo ~1777 vs Menšík ~1897 (different snapshot dates); standard 400-point logistic benchmark Menšík win `1/[1+10^(-(1897-1777)/400)] ≈ 66.61%`; computed 67.13%, +0.52 pp. This independent comparator supports only rough winner direction, not game-handicap/total prices and not calibrated correctness.

#### A5. Full supplied universe / W-P-L-V and two-way complements
- The 4/4 frozen supplied contracts are the complete **supplied universe**; no extra line is promoted. Original issue-time training rows include all four numeric supplied propositions, even informational ranks 3–4. W/P/L/V are in A2. Full two-case complement accounting in A2 is exact for completed match; if operator requires different walkover/retirement settlement this contract is **UNKNOWN_DEFINITION**, not silently assigned VOID or WIN.
- Exhaustive completed match outcomes are represented by 224 distinct `(game totals, sets, winner)` states under the three-case mixture, summed to 1.000000 to double precision. Each line has p_card == W/(W+L), W+L=1, P=V=0 only within the completed-match outcome space. All lines independent of official draw-only/no-push concerns; opponent changes and disruptions not represented.

#### A6. Adjustments, regimes, unadjusted comparison
- Last-52 descriptive hard holds (Gea 82.6%, Menšík 83.9% approximated) are *not* fitted to this opponent. BASE game holds Gea 80% (−2.6 pp, higher opponent strength); Menšík 86% (+2.1 pp, Gea's recent rise notwithstanding). No reliable opponent-specific point sample for precise shifts. These user-visible increments are judgmental sensitivities, not hidden 2026 fit coefficients. No evidence-supported separate injury numeric modifier was made.
- Base-only model: Over23.5 `52.80%`, Menšík−2.5 `51.67%`, Gea+2.5 `48.33%`, Under23.5 `47.20%`. Same order as mixed card. Unadjusted raw-hold scenario separately not issued because mixing raw last-52 pooled challenger/tour cohorts would be misleading; `NO_GROUNDED_UNADJUSTED_MODEL`. Adjustments alter a matchup hold rate by >0 and top-two identity could change under plausible low/high regime parameters; `ADJUSTMENT_DEPENDENT` possibility disclosed rather than concealed.

#### A7. Family coherence, joint risk, shadows, sensitivities
- Both games-handicap rows complement exactly. Same for totals; no pushes because .5 thresholds and integer game sums. No requirement `p(Mensik−2.5) ≤ p(Mensik wins)` applies: **a player can lose a best-of-three match while winning the aggregate games margin**; tennis RULES_TENNIS older `-k.5 ≤ winner` shortcut is not generally true and should not be used as arithmetic constraint without explicit proof. Match winner states are enumerated separately.
- Three-case sensitivity for Over23.5: `49.23%`→`52.80%`→`55.19%` (range `49.23%`–`55.19%`); Menšík−2.5 `60.13%`→`51.67%`→`42.99%` (range `42.99%`–`60.13%`). With strong Menšík advantage, **Menšík −2.5 ranks above Over 23.5**; with Gea service closer, Over ranks above. Hence ranking is not invariant to plausible quality adjustment. These are scenario sensitivities, not credible/confidence intervals. No margin-gap gate PASS can be claimed.
- For top two (Over23.5, Menšík−2.5): `P(both win)=16.94%`; `P(both loss)=12.82%`; `P(exactly one succeeds)=1−both−bothfail=70.24%`; event-level Hit@2 scenario = `87.18%` but *not* validated or independent-row forecasting ability. Pair is partially correlated: high total sometimes accompanies tight margin, so correlations must be obtained from the same game-state grid, not independent `p` multiplication.
- `RET03=NOT_COMPUTED`, `RET04=NOT_COMPUTED`, `XCARD6=NOT_COMPUTED` due no frozen derived universe / league comparator; `SHADOW_MAIN_P_ORDER_V2=NOT_COMPUTED`. `SHADOW_RANK_DELTA=NOT_COMPUTED`, `SHADOW_BASE_ONLY` same primary order with BASE p values and no threshold PASS. The exact different-quantity Rank 2 has NOT_PRIMARY shadow label when treated under original global v11 rather than supplied-first policy. No post-issue reforecast.

#### A8. Source receipts, evidence limitations and capture action
| Source / URL | Pre-event field and observed value | Source publication/update | Retrieval/check time | Lineage/limitations |
|---|---|---|---|---|
| `https://www.atptour.com/-/media/files/rulebook/2026/2026-rulebook-chapter-1_atp-circuit-regulations19dec25.pdf` | 2026 ATP singles Bo3 tie-break sets (all matches) | 19 Dec 2025 in document naming; exact web publish unknown | 13 Oct 2026 ~16:08 AEDT | Field-owner ATP rulebook; actual match-day tiebreak exception not independently seen |
| `https://tennistourcalendar.com/2026-rolex-shanghai-masters-daily-schedule-order-of-play-and-results/` | Stadium Court first de Minaur–Khachanov from 12:00 Shanghai; Gea–Menšík follows | current Oct-13 schedule; page dynamic | 13 Oct 2026 ~16:08 AEDT | Secondary order source; start is not fixed |
| `https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/a-gea-vs-j-mensik-2026-10-13` | R4, Stadium Court, **Upcoming**, players ranked #56/#15 | dynamic; publication/update NOT_VERIFIED | 13 Oct 2026 ~16:08 AEDT | Tennis.com second-party scoreboard; no independent verified first serve |
| `https://www.sofascore.com/tennis/match/arthur-gea-jakub-mensik/mWYcsMEdd` | R16, outdoor hard, 05:10Z estimate | dynamic; update NOT_VERIFIED | 13 Oct 2026 ~16:08 AEDT | Secondary fixture/time; may auto-update |
| `https://tennis-db.com/players/341/arthur-gea/matches` | Gea dated player scores with qualifying/Bo5 flags through 11 Oct | log update 2026-10-13 02:16 UTC | 13 Oct 2026 ~16:08 AEDT | Secondary match log; no post-fixture result listed at issue; field n audited from table |
| `https://tennis-db.com/players/18/jakub-mensik/matches` | Mensik dated scores through 11 Oct | log update 2026-10-12 07:16 UTC | 13 Oct 2026 ~16:08 AEDT | Secondary match log; no new 13 Oct result used |
| `https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqq&p=210150%2FJakub-Mensik&q=HaroldMayot` | Menšík last-52 hard ~84.4% hold / 21.1% break + ~66.8% SPW; player Elo ~1897 | exact capture/publication NOT_VERIFIED; page crawled within preceding week | 13 Oct 2026 ~16:08 AEDT | Statistical aggregator, overlapping tennis result providers; last-52 not independently audited for leakage |
| `https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqq&p=210338%2FArthur-Gea&q=TomasMachac` | Gea last-52 hard ~83.3% hold / 32.7% break, snapshots vary, Elo ~1777 | dynamic; exact snapshot NOT_VERIFIED | 13 Oct 2026 ~16:08 AEDT | Separate Tennis Abstract snapshots show Gea 82.6–83.3% hold and 30.7–32.7% break, so 82.6 value is a dated scenario anchor, not a precisely frozen career statistic |
| `https://www.tennismajors.com/atp/gea-stuns-shelton-for-first-top-10-win-and-reaches-shanghai-last-16-on-masters-1000-debut-863001.html` | Gea beat Shelton 7–6 7–6 Oct 11, 75% first-serve point wins, 4 aces, 3 breaks | published 2026-10-11 | 13 Oct 2026 ~16:08 AEDT | Independent editorial match report; n=1 |
| `https://nationalbankopen.com/matches-players/results/2026/van-de-zandschulp_vs_mensik` | Menšík in Aug 9 2026 match first serves 42/63; wins 34/42 first-serve points; 44/63 service points won | archived August 2026 event | 13 Oct 2026 ~16:08 AEDT | Tournament field-owner one-match example, not a season fit |

**Source restrictions:** no market odds, tip blogs, opponent fixtures after pregame cutoff, or downstream odds-linked probabilities entered. Actual player medical clearance / current warm-up, physical trainer treatment, withdrawal status and opponent-specific serve point numerators NOT_VERIFIED. Names are on upcoming draw and no dated official withdrawal found in inspected sources; **do not infer medically confirmed fitness**. H2H no meeting in visible logs. No issue-time lineup gate for singles; participant status listed/withdrawal NOT_VERIFIED.
**Collection and settlement:** manually follow ATP results after confirmed final (actual first serve, full set scores, tiebreaks, games by player and total, final winner/status, retirement/walkover); source capture with timestamps, exact operator retirement/void wording needed before operator grades. On unavailable ATP field, official tournament PDF/alternative Tennis Majors then corroborating source. Final time UNKNOWN, no exact due time derived; proposed 72h manual review after independently verified finish, no automation scheduled. **SETTLEMENT NOT_PERFORMED**.

#### A9. Integrity receipt and readback
- `SOURCE_CUTOFF/RESEARCH_COMPLETION=2026-10-13T16:08:33+11:00` Australia/Sydney; `ISSUE=2026-10-13T16:08:33+11:00` (write/readback checked separately); actual start `NOT_VERIFIED`, historical/live contamination `NONE_OBSERVED_IN_USED_EVIDENCE`, not a guarantee match had not started.
- Authority exactly published pinned `main` full SHA. Opening mini had 0 new cards and next P-585; prior original bytes preserved outside permitted queue, intake, card and footer updates; output includes exactly one `BEGIN CARD P-585` and `END CARD P-585` balanced marker; no duplicate new-event ID and no canonical allocations.
- **C1–C20 mini-log-7 audit:** C1 pinned-source receipt PASS; C2 identity VERIFIED_SECONDARY / official native ID NOT_VERIFIED; C3 duplicate accessible local PASS / external NOT_VERIFIED; C4 clock/timezone PASS / actual tip UNKNOWN; C5 cutoff and no post-event data PASS for used sources; C6 format ATP best-of-3 PASS; C7 settlement/retirement terms UNKNOWN_OPERATOR; C8 4 supplied lines frozen PASS; C9 evidence/source n PARTIAL; C10 L5/L10/L15/L20 true n PASS; C11 distribution mass=1 PASS subject to unfitted assumptions; C12 normalised W/P/L/V completed-match PASS / full disruption mass NOT_ESTIMATED; C13 benchmark compared PASS; C14 BASELINE_P 0/4 explicitly unavailable PASS_DISCLOSED; C15 gate/family and rank-2 floor disclosed PASS_DISCLOSED; C16 dependency/joint grid PASS; C17 sensitivity LOW/BASE/HIGH PASS; C18 shadow disclosure PASS_DIAGNOSTIC / unsupported branches NOT_COMPUTED; C19 settlement not performed and remote GitHub write NO PASS; C20 write/readback only PASS after file verification. This is a **mapping** to applicable card-integrity topics, not a claim all underlying source data are complete.
- **SF-A1–SF-A12 supplied-first audit:** SF-A1 all 4 supplied lines retained PASS; SF-A2 game-vs-set explicit PASS; SF-A3 full definitions and retirement gap PASS_DISCLOSED; SF-A4 distinct line identity PASS; SF-A5 4 complete model prices PASS; SF-A6 no generated ladder promoted PASS; SF-A7 rank by non-rounded p PASS; SF-A8 ceiling/floors PASS_DISCLOSED; SF-A9 local-only gate label PASS; SF-A10 joint alternatives from common distribution PASS; SF-A11 four training-row observations and WPLV disclosures PASS; SF-A12 original mini and footer readback PASS after actual file verification.
- `SPORTS_ONLY_MARKET_BLIND`: PASS on used evidence; `NUMERIC_MODEL`: UNCALIBRATED_ANALYST_SCENARIO; `OUTCOME_EXPOSURE`: NONE_OBSERVED_IN_USED_EVIDENCE; `SETTLEMENT`: NOT_PERFORMED; `CANONICAL_IMPORT`: PENDING; `GITHUB_WRITES`: NO.
<!-- END CARD P-585 -->

<!-- BEGIN CARD P-586 -->
## Card · P-586 · Basketball / BKT EuroCup 2026–27 Group D, Round 3 · Bahçeşehir Koleji Istanbul vs Kids&Us Manresa · 2026-10-13 Istanbul / 2026-10-14 Melbourne

- **Working ID:** `P-586 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`. Exactly one local card, not a committed canonical P-ID. User's four distinct **supplied contracts only** form the primary-priced universe. Fifth optional player/quarter contract NOT_SUPPLIED and is not manufactured.
- **Event key / native ID / aliases:** `EUROCUP:2026-27:RS-R3:U2026-GAME47:BKS-MAN:2026-10-13`; EuroLeague media-game view `19489` / gamecode `47`, season `U2026`. Bahcesehir Koleji / Bahçeşehir College Istanbul / BKS; Kids&Us Manresa / BAXI Manresa / MAN. No matching event in accessible prior P-585, previous imported P-577–P-584 or GitHub current status; large canonical Part 7 full-text reread and unknown other computer copies NOT_VERIFIED.
- **Authority:** `PUBLISHED_MAIN_PINNED` on `danisgreat/Sports-Research` `main` full SHA `65f780cef9f1a97a411b47fcb08e2355eb1be897`. MDS-2026.10.12-v11.0 / CR-2026.10.12-R2 / SCV-2026.10.12-v7 / SEL-2026.10.12-v3 and `SUPPLIED_FIRST_V1` user supplement. GitHub READ-ONLY, no canonical import.
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`; **not validated, no fitted per-team model, no inferred realised odds**. Numerical outputs CONDITIONAL on match completion and the stated score-distribution assumptions. Current draw/pace/lineup not proved.
- **Timing:** source research first available 2026-10-14T02:54:00+11:00–02:59:05+11:00, dedicated pre-event cutoff `2026-10-14T02:59:05+11:00`; calculation completion `2026-10-14T02:59:05+11:00` (independent calculation), **actual local append/issue** `2026-10-14T03:03:58+11:00`, source-status reread at issue NOT_VERIFIED; scheduled start 03:00 +11; actual jump ball NOT_VERIFIED. **Issue band:** `LATE_START_UNVERIFIED`; scheduled lead at issue `-3.98` minutes. Avoid clean prospective classification without a time-stamped pre-tip field-owner state and all roster checks. NO final, live points or outcome page read or used in pricing.
- **Scheduled start:** Tuesday 13 October 2026 19:00 TRT UTC+03:00 = 16:00 UTC = 18:00 CEST = Wednesday 14 October 2026 03:00 AEDT UTC+11:00, Sinan Erdem Sports Hall, Istanbul. `https://mediacentre.euroleague.net/mediacentre/en/games/view/19489/yes`.
- **Endpoint:** EuroCup men's 40 regulation minutes, four 10-minute quarters; ties at 40 minutes continue in 5-minute OT periods until winner; all four full-game spread/total contracts include OT, integer final team scores, no push on supplied half-point lines in a complete game. Operator cancellation/abandonment/reduced-game settlement action UNKNOWN_DEFINITION; unconditional real-world VOID risk NOT_ESTIMATED. The reported W/P/L/V below is *conditional on full completion*, not a claim zero real-world void frequency.
- **Expected full-game score (model only):** Bahçeşehir **93.431** points, Manresa **83.431**; total **176.861** points, expected signed Bahçeşehir−Manresa margin **+10.000**. Regulation mixture SD(T)=√404.75=20.118 points; SD(M)=√274.00=16.553. Regulation home SD=√((404.75+274.00+2×9.00)/4)=13.198, away SD=12.853; corrected full-game SDs not certified, extra-time variance introduces a small unestimated correction. Conditional covariance Cov(T,M)=9.00 from mixture mean shifts (zero only *within* each scenario, a simplifying assumption), Cov(home,away)=(404.75−274.00)/4=32.69 points². Score means are not exact-score prediction.
- **Lineup state / issue step:** `STARTING_FIVES_UNCONFIRMED; ACTIVE_BENCH_UNCONFIRMED; PRETIP_5_MIN_CHECK_MISSED_OR_NOT_VERIFIED`. Last confirmed Manresa lineup from 11-Oct Real Madrid fixture: Villar, Notae, Agbo, Minchev, Oriola; active on *that date* Allen, Kolenda, Benitez, Bassas, Tamba, Ongenda, Fernández. Benitez/Oriola recently returned after injuries; no verified 13-Oct playing availability. Bahçeşehir 7-Oct EuroCup scorers Flynn, Mike, Cavanaugh, Williams, Sipahi, Avramović, Akpınar, Inglis, Haltalı, Ponitka, but not tonight's confirmed starters/bench. No fictional confirmations.
- **Known-at:** All used scoring fixtures finished by 11-Oct-2026 (Manresa latest), Bahçeşehir latest 10-Oct-2026; official 2026-27 EuroCup fixtures and previous club reports dated before cutoff. Dynamic source update/publish time of cached score pages NOT_VERIFIED; detailed possession data not available; Rank-1 is NOT marked verified prospective. Did not use live 13-Oct outcome.
- **Baseline:** `BASELINE_UNAVAILABLE: EUROCUP_COHORT_NOT_ESTABLISHED` for all 4 exact lines; 2025 archive `Previous Sports Results/Basketball/EuroCup/2025/2025_games.csv` header-only (0 logical rows), 2026 season path NOT_FOUND; `LEAGUE_PROFILES.md` has EuroLeague, **not EuroCup**, and EuroLeague 168.19 cannot silently substitute. A tiny 2026–27 EuroCup Group D 8-result descriptive sample (mean ~168.25) is NOT treated as a vetted or independent cohort with a validated OT/margin baseline. Coverage `0/4`; do not backfill.
- **Regime/context:** `EARLY_SEASON`, `LINEUP_UNCONFIRMED`, `UNFITTED_MATCHUP`, `NO_VALIDATED_EUROCUP_LEAGUE_PROFILE`. Bahçeşehir 5–0 cross-league games, Manresa 1–4; Bahçeşehir 2–0 in EuroCup, Manresa 1–1. Manresa suffered 120–83 loss to Real Madrid 11-Oct (strong opponent); Bahçeşehir beat Balkan 100–61 per EuroLeague field-owner, but some other score publishers show 101–60 — score-level source conflict explicitly recorded (total 161 and margin 39/41 close), negligible effect on season means but not silently repaired. Adjust for opponent/roster uncertainty with a transparent predeclared mixture, **not** claimed empirically fitted rating.
- **Distribution:** `P586-GAUSS-TOTAL-MARGIN-3CASE-OT-APPROX-v1`: scenarios below. Conditionally independent normal 40-minute regulation total T ~ N(T_i,20²) and signed margin M ~ N(M_i,16²). A regulation tie is approximated by |M|<0.5; that state receives one 5-minute OT: +18 points to total and a symmetric +3/-3 Bahçeşehir margin, each probability 0.5. This deliberately simplified branch ignores rare multiple overtimes and actual OT-score volatility; expected OT tie share ~2.01%. Mixture weights fixed 0.25/0.50/0.25 before ranking, all probabilities analytically integrated with normal CDF, NOT a fitted possession-by-possession or simulated player model; rough numerical ε 0.005 (not a statistical confidence interval).
- **Adjustment direction:** unsmoothed five-game matchup centre `Bah=(Bah PF 93.0 + Man PA 102.0)/2 = 97.5; Man=(Man PF 89.8 + Bah PA 76.0)/2=82.9`, total 180.4, margin +14.6. Overstate suppression from weak Balkan and exaggerate Manresa's defensive weakness via elite Real Madrid → base subjective shrink to Bah 93, Man 83, regulation T=176 and M=+10. No invented ORtg/DRtg, possessions or quantified roster edge.
- **Evidence and archive:** `https://www.bahcesehirsporkulubu.org/fikstur`, `https://mediacentre.euroleague.net/mediacentre/en/games/view/19489/yes`, `https://mediacentre.euroleague.net/mediacentre/en/games/view/19497/yes`, `https://www.basquetmanresa.com/en/news/baxi-manresa/game-report/2026/kidsus-battles-an-unbeatable-madrid-side/`, `https://as.com/resultados/baloncesto/eurocup/2026_2027/calendario/grupos_d/`, `https://www.betexplorer.com/basketball/team/manresa/KAm6vlvR/results/` (sporting scores only; no markets examined). See A3/A8 for exact rows and conflicts.
- **Settlement capture:** exact completed final scores/quarters/OT periods, official starters and DNP/active roster, actual tip/final wall-clock, each final handicap and full-game total, exact operator action/void rule. EuroLeague field-owner game U2026 round 3 gamecode 47, fallback structured box. Responsible actor next manual user-invoked settlement; no automation or settled result now; due ~72 hours from independently verified final but actual final time UNKNOWN.

### Decision block — SUPPLIED_CONTRACT_RANKING / SUPPLIED_FIRST_V1
**Four distinct supplied lines priced; no derived line promoted.** Base-case Bahçeşehir projected +10, but published −13.5 is above that mean and Manresa's cushion has the strongest modeled chance. Lineup and team-opponent uncertainty are dominant; *nominal probabilities are uncalibrated scenarios*. Both top-two probabilities are below current gate/floor.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (signed; z at base) | Probability basis | Principal failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK (LOW_CONFIDENCE) | SUPPLIED | `FULL_GAME_MARGIN:MAN+13.5:INCL_OT` — Manresa **+13.5 points** | **58.37%** | 58.66% | BASELINE_UNAVAILABLE | threshold margin 13.5 − base M10 = +3.5; z=+0.219 | three-case normal margin | Bahçeşehir wins by ≥14 |
| 2 | PICK (LOW_CONFIDENCE) | SUPPLIED | `FULL_GAME_TOTAL:UNDER178.5:INCL_OT` — Combined **Under 178.5 points** | **53.31%** | 54.30% | BASELINE_UNAVAILABLE | threshold total 178.5 − base T176 = +2.5; z=+0.125 before OT | three-case normal total + tie/OT | Combined score reaches ≥179 |
| 3 | INFORMATIONAL | SUPPLIED | `FULL_GAME_TOTAL:OVER178.5:INCL_OT` — Combined **Over 178.5 points** | 46.69% | 45.70% | BASELINE_UNAVAILABLE | same line, opposite direction | complement of full total | Slow pace / bad shooting, total ≤178 |
| 4 | INFORMATIONAL | SUPPLIED | `FULL_GAME_MARGIN:BAH-13.5:INCL_OT` — Bahçeşehir **−13.5 points** | 41.63% | 41.34% | BASELINE_UNAVAILABLE | same margin threshold, opposite direction | complement of game handicap | Manresa loses by ≤13 or wins |

**Exact conditional W/P/L/V** on completed match, ordered above: `0.583683/0/0.416317/0`; `0.533056/0/0.466944/0`; `0.466944/0/0.533056/0`; `0.416317/0/0.583683/0`. Each decisive denominator W+L=1.000000. Zero modeled push from half-point contracts. Operator-VOID mass NOT_ESTIMATED, so do NOT describe these as literal unconditional operator probabilities.

**Baseline coverage:** 0/4 (no independent EuroCup-only 2025/26 league-wide same-line OT-aware empirical input; four `BASELINE_UNAVAILABLE`).
**SUPPLIED_SCOPE_GATE:** `FAIL_FLOOR`: Rank1 58.37% <62%; strongest non-complementary Rank2 Under 53.31%, lead 5.06 percentage points (at best near/below 4-point requirement); floor alone blocks. This is not the published full-universe gate. **Rank-2 floor:** `BELOW_FLOOR`: 53.31% <58%. Sensitivity and unfitted parameter ε mean ordering not robust to adjustment.
**Joint loss of Rank1 and Rank2:** P(Bah covers −13.5 AND total ≥179) = Σ weights×P_i(M>13.5)×P_i(T≥178.5) = **19.59%** in the simplified shared three-scenario model. No OT branch contributes materially because an overtime tie cannot grow to +14 under the frozen +/-3-point simplification. Event-level dependence retained (do not multiply overall marginals); mechanically protected NO. Main possibility both lose: Bahçeşehir scores heavily and dominates. Fréchet bounds from marginals: max(0,(1−cushion)+(1−under)−1) = 0%; upper min(41.63%,46.69%) = 41.63%. Opposite pairs 1 vs 4 and 2 vs 3 are exact complements: one wins and the other loses on every completed half-point score.
**Potential full-game winner:** Bahçeşehir **72.69%**, Manresa **27.31%**, final draw 0 by EuroCup OT rule; winner model excludes unmodelled abandonment/forfeit. Probability differs from Bah −13.5, as it should.
**Primary selection ceiling:** no supplied row >90%; all four remain visible and within capacity. **No player/quarter line supplied:** N/A.
**Shadows:** `SHADOW_MAIN_P_ORDER_V2` NOT_COMPUTED (no independently established derived candidate universe; no derived row may displace supplied four); `RET03` = not a separate promoted gate; `RET04` / `XCARD6` top two supplied are different quantities, NOT_PRIMARY shadows; `SHADOW_RANK_DELTA` NOT_COMPUTED (four BASELINE_P unavailable); `SHADOW_BASE_ONLY` top two Manresa +13.5 58.66%, Under 178.5 54.30% with same order, both below applicable floors. `ADJUSTMENT_DEPENDENT`: rank1 and rank2 swap/shift plausible under stronger pace/margin assumptions; no certified stability.

### Appendix
#### A1. Identity, timing and state
Field owner EuroLeague media-game page `19489` (round 3, 13-Oct 18:00 CEST, Sinan Erdem); official Bahçeşehir fixture page confirms 13-Oct 19:00 TRT. Time equivalence holds. User's 14-Oct 03:00 AEDT matches exactly. Source game state seen scheduled 0–0 on media page prior to scheduled tip; that is NOT proof of whistle state at actual append timestamp. No final/live score used. `LATE_START_UNVERIFIED` at local write. Duplicate/custody: local old P-585 Arthur Gea / Jakub Menšík different sport/event; status highest P-584; latest importer confirms P-585 canonical next, local current card P-585, so P-586 is next local if no invisible competing writers. Full Part7 body fetch inaccessible, external writer locks NOT_VERIFIED. Lease `2026-10-13T15:55:33+11` to `2026-10-14T15:55:33+11` held by same conversation; mini not frozen.

#### A2. Frozen supplied contracts / score definitions
Exactly 4 half-point full-game after-OT lines. Manresa +13.5 wins if official final Bah−Man ≤13; Bah −13.5 wins if Bah−Man ≥14; Over178.5 if combined ≥179; Under178.5 if combined ≤178. No double counting: 2 complementary pairs, no missing optional contract. Exact action/abandonment not supplied; sporting completion endpoints alone modelled. Zero push for completed integer scores. All four rows retained for later training observations irrespective of confidence; Ranks 3–4 informational. Thresholds not retuned.

#### A3. Dated team evidence, archive and four-window form
**Recent exact-game score list (oldest→newest; published previous completed results only, chronological):**

| Side | Date (venue) | Competition | Opponent | Scored | Conceded | Home/away | Source/state |
|---|---|---|---|---:|---:|---|---|
| Bahçeşehir | 2026-09-27 | Türkiye BSL | Fenerbahçe Tarfin | 98 | 83 | H | official club `fikstur`, final |
| Bahçeşehir | 2026-09-30 | BKT EuroCup | BC Roma | 91 | 78 | H | EuroLeague media center final |
| Bahçeşehir | 2026-10-04 | Türkiye BSL | Glint Çayırova Belediyesi | 84 | 76 | A | official club schedule |
| Bahçeşehir | 2026-10-07 | BKT EuroCup | Balkan Botevgrad | **100** | **61** | A | **EuroLeague field-owner** page `19497`: 61−100, versus many secondary reports 60−101; contested single-point score attribution |
| Bahçeşehir | 2026-10-10 | Türkiye BSL | Karşıyaka | 92 | 82 | H | official club schedule |
| Manresa | 2026-09-26 | Liga ACB | Bilbao | 92 | 107 | A | sporting result schedule |
| Manresa | 2026-09-30 | BKT EuroCup | PAOK | 78 | 93 | A | BKT EuroCup group standings |
| Manresa | 2026-10-03 | Liga ACB | Río Breogán | 95 | 101 | H | official club and sporting schedule |
| Manresa | 2026-10-07 | BKT EuroCup | ratiopharm Ulm | 101 | 89 | H | club result and EuroCup results |
| Manresa | 2026-10-11 | Liga ACB | Real Madrid | 83 | 120 | A | Manresa official 11-Oct report |

**L5 through L20; true audited n=5 in same current-season mixed 40-minute competitions, additional historical cross-season matches NOT independently traced in this session; do not invent n=10/15/20.** Supplying a 5-match fallback in windows with target 10, 15, 20 is an `ARCHIVE_UNAVAILABLE / FORM_WINDOW_SHORTFALL`, NOT an achieved full L20 sample. These windows *overlap* and are **counted once**.

| Team / target window | Actual n | Date interval | PF/game | PA/game | Margin/game | Strength/flag |
|---|---:|---|---:|---:|---:|---|
| Bahçeşehir L5 | 5 | 27 Sep–10 Oct 2026 | 93.00 | 76.00 | +17.00 | EuroCup x2, BSL x3, weaker Balkan opponent |
| Bahçeşehir L10 | 5 / 10 requested | same | 93.00 | 76.00 | +17.00 | `ARCHIVE_UNAVAILABLE: 2025-26 roster/transition not traced` |
| Bahçeşehir L15 | 5 / 15 requested | same | 93.00 | 76.00 | +17.00 | same gap, not independent form window |
| Bahçeşehir L20 | 5 / 20 requested | same | 93.00 | 76.00 | +17.00 | same gap |
| Bahçeşehir season to date | 5 | same | 93.00 | 76.00 | +17.00 | 2026-27 combined leagues, regulation/OT flag for past finals NOT_VERIFIED |
| Bahçeşehir league level | N/A | 2025 EuroCup archive 0 rows | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | league profile unavailable; observed Group D n=8 diagnostic only |
| Manresa L5 | 5 | 26 Sep–11 Oct 2026 | 89.80 | 102.00 | −12.20 | 2 EuroCup + 3 Liga ACB; Real Madrid elite outlier |
| Manresa L10 | 5 / 10 requested | same | 89.80 | 102.00 | −12.20 | `ARCHIVE_UNAVAILABLE: 2025-26 prior roster not incorporated` |
| Manresa L15 | 5 / 15 requested | same | 89.80 | 102.00 | −12.20 | same gap |
| Manresa L20 | 5 / 20 requested | same | 89.80 | 102.00 | −12.20 | same gap |
| Manresa season to date | 5 | same | 89.80 | 102.00 | −12.20 | opponent adjustment required |
| Manresa league level | N/A | EuroCup annual 2025 0 rows | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | no verified independent league benchmark |

**Archive checked:** pinned repo `Previous Sports Results/Basketball/EuroCup/2025/2025_games.csv`, header-only, 0 scored event rows (286-char header); `EuroCup/2026/2026_games.csv` NOT_FOUND; league-profile basketball entries for EuroLeague/NBA/NBL/Greek/WNBA, no validated EuroCup; current 2026 season web results 8 Group D games observed but NOT ingested as verified independent archive cohort. Earlier 2025-26 game schedules available through secondary sources, not reconstructed from full original box rows here. No fabricated ORtg/DRtg or possessions. Actual season-to-date L5 scoring is an observed contextual aggregate, not a model fit.

**R2-style shrinkage and window choice:** with absent EuroCup level prior `k NOT_ESTIMABLE` and no independently verified L20, cannot execute legitimate ARCHIVE_USE_GUIDE recipe R2 numerically; the simple 5-game matchup is printed only as diagnostic. A conservative adjustment from that raw matchup centre is *judgmental* to account for opponent quality/roster uncertainty (A4), not labelled a fitted or league-shrunk L20. Non-overlapping L5–L10, L10–L15, L15–L20 trends are NOT_COMPUTED because sufficient dated evidence absent. No 2025 player bench known-at equivalence assumed.

**Rotation and workload:** Menresa played Real Madrid 11-Oct and travelled Madrid→Istanbul for 13-Oct; 48-hour-ish turnaround from scheduled games, verified dates but exact travel/fatigue coefficient unavailable. Manresa's 11-Oct roster listed 12 participants; Benitez/Oriola recently returned from injuries; no dated official 13-Oct starters or DNP sheet located, so scenario width must encompass possible rotation swings. Bahçeşehir players named in official club and previous match score sheets; 13-Oct starting five/active bench NOT_VERIFIED. Fixture is five-on-five, no players identified as fully active unless checked tonight.

#### A4. Coherent probability arithmetic, score moments and OT approximation
No legitimate dated possession counts or ORtg/DRtg supplied, so **raw points matchup** rather than pretend a possession-by-efficiency fit. Unadjusted current-season five-game centre = `(93+102)/2 =97.5` Bah, `(89.8+76)/2=82.9` Man; T=180.4, M=+14.6. Downweight weak Balkan defensive number and Real Madrid's high attack against Manresa; shrink home ~4.5 and away ~0.1 (analyst estimate, not inferred from model fitting) to base 93,83.

| Scenario (declared before ranking) | Weight | Bah mean | Man mean | Reg total T | Reg signed margin M | Reg total SD | Reg margin SD |
|---|---:|---:|---:|---:|---:|---:|---:|
| LOW Bah edge / high Man form | 0.25 | 89 | 85 | 174 | +4 | 20 | 16 |
| BASE | 0.50 | 93 | 83 | 176 | +10 | 20 | 16 |
| HIGH Bah edge / low Man form | 0.25 | 98 | 82 | 180 | +16 | 20 | 16 |

`F_i(x;μ,σ)=Φ((x−μ)/σ)` (normal CDF). Approx tie mass r_i=Φ((0.5−M_i)/16)−Φ((−0.5−M_i)/16). All scenarios normalised independently, sum weights 1. Full-game under: `Σw_i [(1−r_i) Φ((178.5−T_i)/20) + r_i Φ((160.5−T_i)/20)]` (assumes 18 OT points, symmetric winner±3); Man +13.5: `Σw_i Φ((13.5−M_i)/16)` because tied-regulation OT by ±3 stays within +13.5; counterpart p = 1−p. Winner Bah = `Σw_i [1−Φ((0.5−M_i)/16)+0.5*r_i]`. Joint primary failure = `Σw_i [1−Φ((178.5−T_i)/20)] [1−Φ((13.5−M_i)/16)]`. Conditional independence of regulation T and M **within** each case is an explicit approximation, not an estimated covariance.

| Scenario | Tie reg (proxy) | Man +13.5 | Under 178.5 | Bah full-game winner | Both primaries lose |
|---|---:|---:|---:|---:|---:|
| LOW | 2.416% | 72.366% | 58.081% | 59.866% | 11.357% |
| BASE | 2.051% | 58.658% | 54.296% | 73.391% | 18.615% |
| HIGH | 1.512% | 43.792% | 46.549% | 84.123% | 29.784% |
| MIXTURE | 2.008% | **58.368%** | **53.306%** | **72.693%** | **19.593%** |

Mixture E[Treg]=176.5, E[M]=10.0, E[Tfull]=176.5+18×0.020076=176.861; Bah and Man means as listed. Regulation `Var(T)=400+ weighted variance(174,176,180)= 404.75`, `Var(M)=256+ weighted variance(4,10,16)=274.00`, Cov(T,M)=9.00. Mass below 0 or physical infeasible scores and exact discrete T/M parity are not truncated/renormalised; at these means/widths tail is negligibly small, but approximation still UNFITTED. The OT proxy ignores multiple OTs and conditional OT pace/total variance; team means are *illustrative*, no mechanistic forecast certified. `epsilon ≈0.005` covers approximation presentation, **not** structural model error.

#### A5. Full supplied universe and exact W/P/L/V
All four supplied rows, exact keys, role and completed-match W/P/L/V are in Decision block. Totals and spreads share T/M distribution, but exact complement identities are retained. For all four, model completed-game W+L=1, P=V=0; match not completed / operator actions cannot be assigned numerical V. Training rows stored even where under Rank-1/Rank-2 requirements. NO additional automatically generated threshold or player/quarter line.

#### A6. Adjustments / opponent strength / alternative pair
Unadjusted 5-game cross-league point proxy Bah 97.5 Man 82.9 → T180.4, M14.6 (ignore unproved home factor; home-court context already implicit in score histories). This would materially strengthen Bah−13.5 and Over178.5 and could alter selection; designation `ADJUSTMENT_DEPENDENT: YES`. Base shrinks to Bah93 Man83 due highly uneven opponent strengths and absent qualified EuroCup league model. Current environment: Bah 5–0 (EuroCup 2–0), Man 1–4 (EuroCup 1–1), travel Madrid→Istanbul, Manresan injury returns. Directional evidence only; no numeric pace or injury coefficient asserted.

#### A7. Family checks, sensitivities, shadows
All four supplied half-point contracts are distinct; exact opposite pairs complementary, avoid both of a complement pair as top two. Rank1 is full-game margin; Rank2 full-game total. OT can increase total and narrow a close result's uncertainty, but does not mechanically protect Rank 1/2. Lineup/unfitted margin sensitivity: Man +13.5 LOW 72.4%, BASE 58.7%, HIGH 43.8%; Under LOW 58.1%, BASE 54.3%, HIGH 46.5%. Scenario ranges are *not* confidence intervals; selected order can flip within plausible parameters. SHADOW_BASE_ONLY preserved, SHADOW_RANK_DELTA unavailable without baseline. Rank1 gate FAIL in all cases (unless different supplied alternative threshold scope; not evidence of validated gate). Zero odds or selection markets used.

#### A8. Source, field, publication, retry and settlement map
| Source | Exact useful field | Publication / last update | Access / cutoff | Confidence and risk |
|---|---|---|---|---|
| `https://mediacentre.euroleague.net/mediacentre/en/games/view/19489/yes` | Round 3, BKS–MAN Tue 13-Oct, 18:00 CEST, arena; no final | dynamic current, exact page update NOT_VERIFIED | retrieved pre 02:59:05 AEDT | official field owner; scheduled page is not verified whistle receipt |
| `https://mediacentre.euroleague.net/mediacentre/en/games/view/19497/yes` | 07-Oct Balkan–Bah 61–100, game facts | match 07-Oct; dynamic | by 02:59:05 | official result versus conflicting secondary 60–101 |
| `https://www.bahcesehirsporkulubu.org/fikstur` | BSL Bah results 98–83, 84–76, 92–82; 13-Oct opponent / 19:00 TRT | older completed fixtures by 10-Oct; dynamic index | pre 02:59:05 | own team source, no game-day 5/bench |
| `https://www.basquetmanresa.com/en/news/baxi-manresa/game-report/2026/kidsus-battles-an-unbeatable-madrid-side/` | 11-Oct Real120–Man83, 12 named participants, Oriola/Benitez returning | 11-Oct 2026 14:37 club local | pre 02:59:05 | own team source, last game's roster not today's |
| `https://as.com/resultados/baloncesto/eurocup/2026_2027/calendario/grupos_d/` | 8 2026-27 EuroCup Group D completed results through 07-Oct | dynamic listing, exact state time unknown | pre 02:59:05 | secondary scores; small, not league baseline |
| `https://www.betexplorer.com/basketball/team/manresa/KAm6vlvR/results/` | Manresa last five dated match results (only sporting scores) | dynamic | pre 02:59:05 | source bookmaker-linked domain; **ONLY result cells** used, no market/odds consulted; collector independence NOT_VERIFIED |
| `https://www.bahcesehirsporkulubu.org/` | published squad roster names, NOT active game roster | dynamic roster | pre 02:59:05 | NO proof starters or injuries tonight |

No exact current starter five, active substitute/DNP, possession data, EuroCup league baseline distribution, validated travel coefficient or current-minute lineup forecast found in accessed material. Follow EuroLeague `gamecode47` exact finished box for 4 quarter scores/OT result, official minutes, starting-five marks, active/dressed, injuries, final, tip and final time; operator policy user-supplied if necessary. If not published immediately, log manual retry without calling it scheduled. No source after declared cutoff used.

#### A9. Integrity and audit result
- Required refs: README, CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, SCORING_AND_VALIDATION, PROBABILITY_TOOLKIT, `research/prompts/1_GAME_CARD.md`, `research/prompts/README.md`, VERIFICATION_PROTOCOL, RULES_BASKETBALL, LEAGUE_PROFILES, ARCHIVE_USE_GUIDE, SOURCES, BASE_RATES_REGISTER, `GAME_LOG_STATUS_CURRENT`, mini original and Oct-13 importer. Published `main` pin full SHA above. Current method/control/scoring/selection v11/R2/v7/v3; sports sources as above; written local file only. **Not all controls read end-to-end**: a number were inspected in operative sections/excerpts; do not claim full-file reading.
- C1–C20: **C1** pinned SHA+scope PASS; **C2** identity official and alias check PASS_WITH_PART7_BODY_NOT_VERIFIED; **C3** supplied four exact lines PASS; **C4** complementary p sums and W+L PASS within stated analytic model; **C5** SUPPLIED_SCOPE_GATE FAIL explicitly; **C6** floor/joint/mechanical PASS_DISCLOSED; **C7** case sensitivity and ADJUSTMENT_DEPENDENT PASS_DISCLOSED; **C8** flags named but no fitted effects PASS_DISCLOSED; **C9** 40-min/OT simplified PASS_WITH_LIMITS; **C10** exact scoreboard capture and no automation PASS; **C11** source cutoff, research and write time distinct; classification LATE_START_UNVERIFIED; **C12** SPORTS_ONLY/MARKET_BLIND PASS for used sports data (no odds); **C13** EuroCup header-only archive proven, L10–L20 shortfall OPEN; **C14** 0/4 BASELINE_UNAVAILABLE PASS_DISCLOSED; **C15** arithmetic/SD/covariance formula PASS as model; **C16** physical write+readback verified separately; **C17** window shortfall honestly disclosed, recipe R2 UNAVAILABLE; **C18** line distances/z supplied and source missing; **C19** unrounded mixture, p_base and epsilon disclosed; **C20** issuing writer lease active, request-intake update and no frozen lock; external writers not independently verified.
- SF-A1–SF-A12: SF-A1–A4 all supplied propositions/keys/definitions retained; SF-A5 probabilities computed from one joint scenario with complements; SF-A6 no generated rows primary; SF-A7 primary order unrounded; SF-A8 ≤90% ceiling, floors disclosed; SF-A9 supplied-only gate not misnamed; SF-A10 joint computed conditional on scenario covariance assumption; SF-A11 all four issue-time observation rows stored with WPLV limitations; SF-A12 local write/readback independently checked. **Research-quality gaps remain:** L10/L15/L20, performance baseline, lineups, period/possession data, late/actual tip.
- `SPORTS_ONLY / MARKET_BLIND`: PASS for manually used fields; `OUTCOME_EXPOSURE`: NONE_OBSERVED_IN_INPUTS_BEFORE_CUTOFF, NOT_PROVEN_PROSPECTIVE; `SETTLEMENT`: NOT_PERFORMED; `CANONICAL_IMPORT`: PENDING; `GITHUB_WRITES`: NO.
<!-- END CARD P-586 -->



<!-- BEGIN CARD P-587 -->
## Card · P-587 · NHL 2026–27 · Calgary Flames @ Anaheim Ducks · 13 October 2026 PDT / 14 October AEDT

### Decision block (SUPPLIED_FIRST_V1, local policy override)

- **Working ID:** `P-587` — `ISSUED_LOCAL`, **not** yet canonical; `P-587` is the next working ID after the preserved P-585/P-586 cards. Event/native ID `2026020103`, canonical event key `NHL:2026-27:REGULAR:2026020103:CGY@ANA:2026-10-13`. Opponent/venue and native game ID from NHL game-centre. Search of the whole active mini and current canonical status, and repository indexed search, found no existing card under this native ID; remote search indexing and external writers are not exhaustive.
- **Selection policy:** `SUPPLIED_FIRST_V1 / PROMPT_REVISION SF-2` applied per latest user instruction, intentionally different from published `SEL-2026.10.12-v3 / P_ORDER_V2` (full-universe supplied-as-reference). Never pool this local gate with the published policy cohort. Method `MDS-2026.10.12-v11.0`, control `CR-2026.10.12-R2`, scoring `SCV-2026.10.12-v7`, `mini-log-7`.
- **Authority:** `PUBLISHED_MAIN_PINNED e73c9c24e418250f8816932facc5feeecd94ef5d` (`main`, read-only; state P-584 last canonical and P-585 next canonical). This active mini local working sequence P-585→P-586→P-587; no canonical number allocated by this task.
- **Event and timing:** NHL regular season, Honda Center Anaheim, 2026-10-13 **18:45 PDT / 21:45 EDT** = 2026-10-14 **01:45 UTC / 12:45 AEDT**. Requested estimate 12:52 AEDT is 7 min later than official advertised start. Actual first puck-drop / current live state `NOT_VERIFIED`. Sporting-data cutoff **12:45:00 AEDT** as a reconstructed, date-safe pre-event source ceiling; source research/execution and card issuance occurred **after** that scheduled start. `LATE_START_UNVERIFIED / SCHEDULED_LEAD_NEGATIVE / NOT_VERIFIED_PREGAME`, `OUTCOME_EXPOSURE=NONE_OBSERVED_IN_MODEL_INPUTS`, NOT a certified prospective forecast. First direct retrieval of actual live-score/terminal state intentionally not performed. `KNOWN_AT`: 2025–26 archive complete before cutoff, 2026 first-five games final by Oct 10; NHL Oct 13 preview dated before expected start; exact prior publication time of some secondary historical fields UNKNOWN. No post-event outcomes entered the model.
- **Roster/goalie gate:** `PARTIALLY_CONFIRMED` (official dated **projected** lines, scratches, injuries and first-listed goalies, not an authenticated final roster/starting-game-sheet). Calgary projected Dustin Wolf, backup Devin Cooley; Anaheim projected Lukáš Dostál, backup Ville Husso. Another secondary report calls the goalies confirmed; original NHL starting-goalie assignment at puck drop `NOT_VERIFIED`. Calgary Huberdeau and Honzek unavailable; Anaheim Terry, Gauthier, Poehling and Ian Moore injured; Roger McQueen projected NHL debut. Starting line/scratch details and missing goalie start histories in A3. No numerical lineup effect claimed validated.
- **Primary analysis:** `UNCALIBRATED_ANALYST_SCENARIO / RESEARCH_ONLY_NOT_CERTIFIED`, actual coarse Poisson enumeration, not a fitted calibrated model; mix 0.25 / 0.50 / 0.25 **on state masses before conditional pricing**. An adjusted all-completed-game score convention is assumed. Operator-specific action/abandonment exceptions `UNKNOWN_DEFINITION` and this must not be presented as operator-certified settlement.

#### SUPPLIED_CONTRACT_RANKING — exact four literal user lines only
| Rank | Exact supplied proposition | p_card decisive | W uncond† | P uncond† | L uncond† | V† | W+L† | p_base | BASELINE_LEAGUE_V1 | Formal role |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Flames +1.5 | 0.630112 (63.011%) | 0.630112 | 0.000000 | 0.369888 | 0.0† | 1.000000 | 0.629292 | 0.698933 | PICK |
| 2 | Ducks ML | 0.622630 (62.263%) | 0.622630 | 0.000000 | 0.377370 | 0.0† | 1.000000 | 0.622733 | 0.522104 | PICK |
| 3 | Combined Total Goals: Over 6.0 Goals | 0.514553 (51.455%) | 0.458154 | 0.109609 | 0.432237 | 0.0† | 0.890391 | 0.517957 | 0.523404 | INFO |
| 4 | Combined Total Goals: Under 6.0 Goals | 0.485447 (48.545%) | 0.432237 | 0.109609 | 0.458154 | 0.0† | 0.890391 | 0.482043 | 0.476596 | INFO |

† W/P/L/V are unconditional over the **modelled completed-match** cohort; outside this cohort, walkover/abandonment/void probabilities are UNKNOWN, not asserted to be zero. In this model V=0 *conditional on completed play only*. Exact integer-total 6.0 maps score-total==6 to PUSH on both O/U, not a loss. p_card=W/(W+L). A shootout-decided NHL result gets the official +1 credited final goal to the winner; that does not mean a shootout attempt scored an observed hockey goal.

- **Supplied-only top 2:** Rank 1 `CGY +1.5` **63.011%**, Rank 2 `ANA ML` **62.263%**. Ducks more likely full-game winner: **62.263%**; signed goal-margin centre Ducks +0.745. Top-two are **MECHANICALLY_PROTECTED:** zero shared losing states on a completed all-decisive game. Ducks win by exactly one occurs about 25.274% and both primary rows win; no predictive Hit@2 claim from the protected pair.
- **`SUPPLIED_SCOPE_GATE`:** original R1 p=0.630112 versus best eligible non-complementary supplied alternative ANA ML=0.622630, gap=0.007483 (**0.748 pp**, less than 4 pp); R1≥0.62 true, gap false ⇒ **RANK1_UNSTABLE**, not PASS. R2≥0.58 true. Above-ceiling exclusions none. All four supplied rows priceable using a frozen framework sporting convention but operator-specific grading unresolved. ε≤0.000001 from finite Poisson truncation/integration, excluding parameter uncertainty (far larger). Apparent precision is computational only.
- **Dependence and failure:** ANA ML loses ⇒ Calgary wins ⇒ Calgary +1.5 wins. Calgary +1.5 loses ⇒ Ducks win by ≥2 ⇒ ANA ML wins. `P(both lose | completed model)=0.000000` exact structural; `P(at least one wins | completed model)=1`. Identical venue/period/operator exceptions required. Unconditional push/void after an abandoned or unfinished game unknown. Joint-risk target 0.30/warning 0.35 are not evidence of forecasting skill.
- **Expected NHL credited final:** ANA 3.508 (SD 1.866), CGY 2.763 (SD 1.682), total 6.271 (SD 2.524), ANA margin +0.745 (SD 2.500), covariance +0.0308. Means are model expectations, not forecasts of an exact scoreline. Regulation goals mean ANA 3.419, CGY 2.693 before intensity mixing and OT credit. Mixture reg-tie mass 0.159245, regulation ANA win ~0.53355, Calgary win ~0.30721; tie resolution split OT 0.634969 versus SO 0.365031 from completed 2025–26 league OT/SO game fractions. Both outcomes add one credited *final-score* goal. No live or postgame score used.

### A1. Authority, lifecycle and exact event definition
READING RECEIPT: `PUBLISHED_MAIN_PINNED e73c9c24e418250f8816932facc5feeecd94ef5d`; read during 2026-10-14 ~12:45–12:52 AEDT. Controls opened from the same SHA: `README.md`, `CURRENT_STATE.md`, `METHOD.md`, `CURRENT_RULES.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md`, `SCORING_AND_VALIDATION.md`, `PROBABILITY_TOOLKIT.md`, `VERIFICATION_PROTOCOL.md`, `RULES_ICE_HOCKEY.md`, `RULES_NHL.md`, `LEAGUE_PROFILES.md` (hockey), `BASE_RATES_REGISTER.md` §7.2, `ARCHIVE_USE_GUIDE.md`, `SOURCES.md` §3.9, `research/prompts/1_GAME_CARD.md` (ICE HOCKEY), `research/prompts/README.md`, current section `GAME_LOG_STATUS_CURRENT.md`, archive `Previous Sports Results/Ice Hockey/NHL/2025/2025_games.csv`; verified `2026/2026_games.csv` NOT_FOUND. Required current user prompts loaded in full; active mini read in full and compared with its mirrored copy. **Control excerpt limitation:** files were retrieved, but only operative sections/excerpts of several long controls were manually reviewed; this is not represented as a full human-style end-to-end reading. Current repository full canonical Combined Part-7 body re-fetch unavailable due size, so direct exhaustive canonical-body comparison NOT_VERIFIED; status/main searches found no event collision. Local policy override is confined to supplied primary universe; state timing/model rules retain main authority. No local repository working tree, hidden concurrent writer or alternate unshared mini was available to inspect; this is a custody caveat, not evidence of conflict.

Event: Anaheim (home) vs Calgary (away), date Oct 13 local. Native ID 2026020103. NHL regulation 3×20 minutes; regular-season 5-minute 3-on-3 sudden-death OT then shootout; full-game two-way winner; no draw at certified final. Official NHL shootout-credit result scores winner as +1 final goal; goals actually scored in regulation/OT separated in sporting fields. User's **Flames +1.5**: ANA−CGY ≤1 final; Ducks ML: ANA final winner; Over 6.0: credited final total ≥7, Push exactly 6, lose ≤5; Under 6.0: ≤5, Push exactly 6, lose ≥7. Exact bookmaker operator timing, void and abandonment terms remain NOT_VERIFIED/UNKNOWN_DEFINITION. All rankings are frozen sports-research conventions, not represented as resolving actual provider terms.

`SUPPLIED_UNIVERSE_ID`: `P587-2026020103-SF2-4ROWS-V1` (deterministic descriptive ID; no claimed cryptographic hash). Four raw rows, four distinct normalized keys; raw ordinal→key exact below, all 4 trained/scored *candidates*, not guaranteed model-training-eligible due to late issue and missing operator definitions.

### A2. Literal ledger, definition and source receipt
| Original input index | Verbatim line | Frozen key | Endpoint/action |
|---:|---|---|---|
| 1 | `Flames +1.5` | `NHL-2026020103|MARGIN_CGY_MINUS_ANA|CGY|+1.5|FULL_OTSO|PUSH_NA` | Completed NHL game, 3 periods+OT/SO; no push; operator exception UNKNOWN |
| 2 | `Ducks ML` | `NHL-2026020103|WINNER|ANA|ML|FULL_OTSO|NO_DRAW` | Completed NHL game, 3 periods+OT/SO; no push; operator exception UNKNOWN |
| 3 | `Combined Total Goals: Over 6.0 Goals` | `NHL-2026020103|FINAL_TOTAL_GOALS|BOTH|OVER|6.0|FULL_OTSO|PUSH_AT_6` | Completed NHL game, 3 periods+OT/SO; PUSH exactly 6; operator exception UNKNOWN |
| 4 | `Combined Total Goals: Under 6.0 Goals` | `NHL-2026020103|FINAL_TOTAL_GOALS|BOTH|UNDER|6.0|FULL_OTSO|PUSH_AT_6` | Completed NHL game, 3 periods+OT/SO; PUSH exactly 6; operator exception UNKNOWN |

| Timestamp/source | Owner/field actually used | Time, access, missingness |
|---|---|---|
| [NHL game preview](https://www.nhl.com/news/calgary-flames-anaheim-ducks-game-preview-october-13-2026) | 0–5 vs 4–1 record; 9:45PM EDT, full projected 12F/6D/2G list each, injured/scratches | Published Oct 13 2026 (page says 6:34PM US ET); accessed before file write, exact provider revision time NOT_VERIFIED; projected not confirmation |
| [Ducks schedule](https://www.nhl.com/news/ducks-2026-27-season-schedule-announced) | Tue Oct 13, Honda Center, 6:45PM PDT | published months before start; 12:45 AEDT conversion |
| [2026 Calgary schedule](https://www.statmuse.com/nhl/team/calgary-flames-21/schedule/2027), [2026 Anaheim scores](https://www.hockey-reference.com/teams/ANA/2027_games.html) | first 5 dated final scores and opponent orientation | Historical game-score cache; independently consistent with NHL official standings/recap, not all individual games independently checked; exact field availability timestamps NOT_VERIFIED |
| [NHL Calgary recap](https://frontend.d3.nhle.com/flames/news/topic/scotia-place/flames-doubled-by-ducks-10-10-26) | Oct 10 shots 29/28, Calgary PP 0/3, Anaheim PP 1/2, 5v5 scoring chances CGY28/ANA23, HDCF 13/14 | Calgary owner, prior game, not season xG dataset |
| [NHL 2025–26 archived results](https://github.com/danisgreat/Sports-Research/blob/e73c9c24e418250f8816932facc5feeecd94ef5d/Previous%20Sports%20Results/Ice%20Hockey/NHL/2025/2025_games.csv) | 1,312 eligible 2025–26 regular-season games from 1,498 total outcomes incl preseason/playoffs; source dates, scores, `Decision Type` and `Game State=OFF` | Pinned main; read/parsed actual 2025 CSV. NHL native IDs per row. OT/SO scores treated as credited game results |
| [NHL original Oct 10 preview](https://www.nhl.com/news/anaheim-ducks-calgary-flames-game-preview-october-10-2026) | Previous goalie starters, lineup changes | Official historical, not tonight's confirmed starting sheet |

No market odds, tips, betting probabilities or previews used as quantitative inputs; lineage independence of website mirrors UNKNOWN.

### A3-FORM. Mandatory four historical windows, trace and goalies
**Current season, separate cohort:** NHL 2026–27 **only five prior completed games per team**. L5 has 5; L10/15/20 have *actual n=5*, not false 10/15/20. Current five contain Calgary GF8/GA27, ANA GF18/GA13; on the *regulation goal* metric Anaheim GF17/GA13 (3–2 OT win over Florida has 2–2 after regulation; +1 credited at finish). These season records are not a fitted predictive model. Raw 2026–27 team GF/GA fields present 5/5. Current 5v5 xG, season HDCF, possession, full special-teams opportunities and goalie starts not available as consistent denominators. Venue, opponent and stage are preserved in the event trace; opponent-strength correction `UNAVAILABLE` beyond unadjusted results. Goalie last 5/10/15/20 **eligible starts** are `0 supported detailed game logs / requested 5,10,15,20`: source has aggregate season goalie lines only, so no individual start-history means can responsibly be printed.

**CGY — current 2026–27**
| Window | Eligible events n/target | Metric n | W–L | GF/GA per game (credited final) | Margin / total pg | Venue split | Opponent adjustment | Last eligible date / source |
|---|---:|---:|---|---|---|---|---|---|
| L5 | 5/5 | 5 GF/GA | 0–5 | 1.600/5.400 | -3.800 / 7.000 | H=3 A=2 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| L10 | 5/10 | 5 GF/GA | 0–5 | 1.600/5.400 | -3.800 / 7.000 | H=3 A=2 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| L15 | 5/15 | 5 GF/GA | 0–5 | 1.600/5.400 | -3.800 / 7.000 | H=3 A=2 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| L20 | 5/20 | 5 GF/GA | 0–5 | 1.600/5.400 | -3.800 / 7.000 | H=3 A=2 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| Season (2026–27) | 5/5 | 5 | 0–5 | 1.600/5.400 | −3.800 / 7.000 | H=3 A=2 | UNAVAILABLE | 2026-10-10 / official NHL-aggregated external score route |
| League 2025–26 reference | 1,312 league events | 1,312 | N/A | 3.0027 per team **reg** | N/A | 1,312 league venues | baseline population | 2026-04-16 / pinned archive |

**ANA — current 2026–27**
| Window | Eligible events n/target | Metric n | W–L | GF/GA per game (credited final) | Margin / total pg | Venue split | Opponent adjustment | Last eligible date / source |
|---|---:|---:|---|---|---|---|---|---|
| L5 | 5/5 | 5 GF/GA | 4–1 | 3.600/2.600 | +1.000 / 6.200 | H=2 A=3 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| L10 | 5/10 | 5 GF/GA | 4–1 | 3.600/2.600 | +1.000 / 6.200 | H=2 A=3 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| L15 | 5/15 | 5 GF/GA | 4–1 | 3.600/2.600 | +1.000 / 6.200 | H=2 A=3 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| L20 | 5/20 | 5 GF/GA | 4–1 | 3.600/2.600 | +1.000 / 6.200 | H=2 A=3 | UNADJUSTED strength | 2026-10-10 / live current-game scores excluded |
| Season (2026–27) | 5/5 | 5 | 4–1 | 3.600/2.600 | +1.000 / 6.200 | H=2 A=3 | UNAVAILABLE | 2026-10-10 / official NHL-aggregated external score route |
| League 2025–26 reference | 1,312 league events | 1,312 | N/A | 3.0027 per team **reg** | N/A | 1,312 league venues | baseline population | 2026-04-16 / pinned archive |

**Last-five 2026–27 event-level trace (latest first; actual NHL-native 2026 game IDs not captured and hence surrogate only; no current-match outcome):**
| ID | Date | Opponent | Venue | GF–GA | Endpoint | Source/known-at |
|---|---|---|---|---|---|---|
| CGY-26-01 | 2026-10-10 | ANA | H | 2–4 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| CGY-26-02 | 2026-10-08 | COL | H | 3–7 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| CGY-26-03 | 2026-10-04 | SEA | A | 1–6 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| CGY-26-04 | 2026-10-03 | VAN | A | 1–4 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| CGY-26-05 | 2026-10-01 | SEA | H | 1–6 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| ANA-26-01 | 2026-10-10 | CGY | A | 4–2 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| ANA-26-02 | 2026-10-09 | WPG | A | 5–1 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| ANA-26-03 | 2026-10-07 | EDM | H | 2–5 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| ANA-26-04 | 2026-10-04 | FLA | H | 3–2 | OT | NHL schedule/2026-27; pre-cutoff date; goal counts available |
| ANA-26-05 | 2026-10-02 | VGK | A | 4–3 | REG | NHL schedule/2026-27; pre-cutoff date; goal counts available |

**Independent previous-season supplementary (2025–26, *not appended/padded into current-season windows*).** All games below are older-regime/roster and dated ≤2026-04-16; H/A and final credit retained. The historical archive lacks individual shots, high-danger/xG, goalie-starter fields, and reliable exact-time availability; season end precedes current cutoff by months. L5/10/15/20 cumulative means therefore describe previous-season form only.

| Team | Previous-season window | W–L | GF/GA | Mean GF/GA | Game count |
|---|---|---|---|---|---|
| CGY | L5 | 2–3 | 10/12 | 2.000/2.400 | 5 |
| CGY | L10 | 4–6 | 30/37 | 3.000/3.700 | 10 |
| CGY | L15 | 8–7 | 45/47 | 3.000/3.133 | 15 |
| CGY | L20 | 9–11 | 57/70 | 2.850/3.500 | 20 |
| ANA | L5 | 2–3 | 16/17 | 3.200/3.400 | 5 |
| ANA | L10 | 2–8 | 30/41 | 3.000/4.100 | 10 |
| ANA | L15 | 6–9 | 50/55 | 3.333/3.667 | 15 |
| ANA | L20 | 8–12 | 62/71 | 3.100/3.550 | 20 |

**2025–26 previous-season last-20 trace, native IDs, latest first**
| Source ID / native ID | Completed date | Opponent | Venue | GF–GA | Type | Provenance |
|---|---|---|---|---|---|---|
| CGY-25-01 / 2025021310 | 2026-04-16 | LAK | H | 3–1 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-02 / 2025021298 | 2026-04-14 | COL | H | 1–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-03 / 2025021281 | 2026-04-12 | UTA | H | 4–1 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-04 / 2025021273 | 2026-04-11 | SEA | A | 1–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-05 / 2025021256 | 2026-04-09 | COL | A | 1–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-06 / 2025021239 | 2026-04-07 | DAL | A | 3–4 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-07 / 2025021219 | 2026-04-04 | ANA | A | 5–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-08 / 2025021201 | 2026-04-02 | VGK | A | 3–6 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-09 / 2025021174 | 2026-03-30 | COL | A | 2–9 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-10 / 2025021165 | 2026-03-28 | VAN | H | 7–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-11 / 2025021147 | 2026-03-26 | ANA | H | 2–3 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-12 / 2025021133 | 2026-03-24 | LAK | H | 3–2 | SO | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-13 / 2025021116 | 2026-03-22 | TBL | H | 4–3 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-14 / 2025021097 | 2026-03-20 | FLA | H | 4–1 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-15 / 2025021081 | 2026-03-18 | STL | H | 2–1 | SO | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-16 / 2025021063 | 2026-03-16 | DET | A | 2–5 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-17 / 2025021051 | 2026-03-14 | NYI | A | 2–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-18 / 2025021032 | 2026-03-12 | NJD | A | 5–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-19 / 2025021017 | 2026-03-10 | NYR | A | 0–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| CGY-25-20 / 2025021009 | 2026-03-09 | WSH | A | 3–7 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-01 / 2025021307 | 2026-04-16 | NSH | A | 5–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-02 / 2025021296 | 2026-04-14 | MIN | A | 2–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-03 / 2025021280 | 2026-04-12 | VAN | H | 3–4 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-04 / 2025021258 | 2026-04-09 | SJS | H | 6–1 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-05 / 2025021243 | 2026-04-07 | NSH | H | 0–5 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-06 / 2025021219 | 2026-04-04 | CGY | H | 3–5 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-07 / 2025021206 | 2026-04-03 | STL | H | 2–6 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-08 / 2025021190 | 2026-04-01 | SJS | A | 3–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-09 / 2025021176 | 2026-03-30 | TOR | H | 4–5 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-10 / 2025021154 | 2026-03-28 | EDM | A | 2–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-11 / 2025021147 | 2026-03-26 | CGY | A | 3–2 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-12 / 2025021134 | 2026-03-24 | VAN | A | 5–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-13 / 2025021117 | 2026-03-22 | BUF | H | 6–5 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-14 / 2025021098 | 2026-03-20 | UTA | A | 4–1 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-15 / 2025021082 | 2026-03-18 | PHI | H | 2–3 | OT | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-16 / 2025021059 | 2026-03-15 | MTL | A | 4–3 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-17 / 2025021043 | 2026-03-14 | OTT | A | 0–2 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-18 / 2025021029 | 2026-03-12 | TOR | A | 4–6 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-19 / 2025021022 | 2026-03-10 | WPG | A | 4–1 | REG | NHL 2025 CSV, OFF regular; supplied native ID |
| ANA-25-20 / 2025021006 | 2026-03-08 | STL | H | 0–4 | REG | NHL 2025 CSV, OFF regular; supplied native ID |

**Non-overlap blocks (2025–26 supplemental):** CGY goals for/against blocks newest 1–5 10/12; 6–10 20/25; 11–15 15/10; 16–20 12/23. Anaheim blocks 1–5 16/17; 6–10 14/24; 11–15 20/14; 16–20 12/16. They show why treating L5/L10/L15/L20 as independent confirmations is invalid. For current-season block 1–5 only; later blocks have n=0, not zero performance.

**A3-LINEUPS (official Oct 13 dated projection, not game sheet):**
- Calgary forwards: Sharangovich–Backlund–Farabee; Suniev–Frost–Coronato; Gridin–Pospíšil–Strome; Tsyplakov–Castagna–Klapka. Defence: Bahl–Nemec; Kuznetsov–Whitecloud; Middleton–Parekh. Goaltenders Wolf/Cooley (ordering projected, not official certification). Scratched Othmann/Hanley; injured Huberdeau/Honzek. Confirmed full dressed roster/starting goalie by final game sheet: NOT_VERIFIED.
- Anaheim forwards: Killorn–Carlsson–Sennecke; Nesterenko–Granlund–Colangelo; Vatrano–McQueen–Greer; Malott–Washe–Caulfield. Defence: LaCombe–Warren; Mintyukov–Helleson; Hinds–Luneau. Goalies Dostál/Husso. Scratched Jensen/Klepov; injuries Moore/Terry/Gauthier/Poehling. McQueen projected debut; active sheet and final warm-up substitutions NOT_VERIFIED.
- Current goalie aggregate from NHL pre-event game centre (not specific starter histories): Wolf 0–3, GAA5.42/SV .816; Cooley 0–2, GAA5.01/SV .818; Dostál 3–1, GAA2.95/SV .884; Husso 1–0, GAA1.58/SV .935. Tiny split samples and special-teams exposure do not identify an independent goals adjustment. No goalie effect is added twice to historical defensive goals allowed.
- Last CGY–ANA matchup Oct 10 had shots CGY29/ANA28; CGY PP 0/3, Anaheim 1/2; 5v5 scoring chances 28 vs23 and high-danger 13 vs14 per Calgary's own game recap. Neither this one-game opportunity rate nor point quality is a season-level fitted multiplier; no fabricated 5v5 xG or PP/PK denominator.

### A4. Reproducible distribution, baseline and form-arithmetic
`P587_NHL_POISSON_REG_OTSO_3CASE_v1`; helper calculation outside GitHub: local Python SciPy Poisson mass product grid `0≤ANAreg≤23`, `0≤CGYreg≤23` per scenario; tail residual max 1.44e-12; independent Poisson *assumption* at fixed scenario, not learned 5v5 shot-quality model. For regulation tie h=a: split Anaheim win `α_s=λ_ANA/(λ_ANA+λ_CGY)` and Calgary `1−α_s`; add +1 to the winner's **official credited final goal total**. Distinguish OT from SO for statistics using 2025–26 archived split `207/326` overtime and `119/326` shootout among 326 tied-after-regulation regular-season games; both give one extra credited final-score goal, not actual SO game scoring. This split is a league approximation, not matchup-specific.

Prior 2025–26 regulation rates computed from each club's 82 completed regular games in pinned CSV, converting an OT/SO *credited final win* to actual end-of-regulation count by subtracting one winning-side goal: CGY GF `205/82=2.50000`, GA `250/82=3.04878`; ANA GF `256/82=3.12195`, GA `282/82=3.43902`. Current 2026–27 first-five regulation (CGY 8 GF/27 GA; ANA 17 GF/13 GA, one ANA shootout/OT credited goal reversed); sample n=5 each. No other current-season events admitted.

**Explicit shrinkage:** provisional `k=20` **prior-season pseudo-game weight**, chosen before computing this local comparison (not claimed as a published fitted k or league-optimal). Four rates per team/metric: `r_shrunk=(5×r_current+20×r_2025)/(5+20)`. CGY GF=2.320000, CGY GA=3.519024, ANA GF=3.177561, ANA GA=3.271220. Used *one* current-five block per participant plus separate older-season prior, not four times the same events. Opponent adjustments unavailable; these raw means retain strength-of-schedule bias.

**League anchor:** pinned 2025–26 NHL 1,312 full regular-season games, calculated after removing end-of-game credited one goal for the 326 OT/SO decisions: regulation home mean `3.070122`, away `2.935213`, per team `3.002668`. Matchup base Poisson regulation centres, freeze orientation H=ANA, A=CGY:
`λ_ANA,H=3.070122×sqrt(ANA_shrunk_GF×CGY_shrunk_GA)/3.002668 = 3.419058`;
`λ_CGY,A=2.935213×sqrt(CGY_shrunk_GF×ANA_shrunk_GA)/3.002668 = 2.692968`.
This square-root attack/defence interaction and k are **declared analyst assumptions**, not a validated fitted recipe. Score correlations and changing game-state/empty-net intensity are NOT fitted; empty-net scoring remains in observed team rates as a crude approximate tail, not a separately simulated state-dependent hazard. 5v5/xG and goalie microstats missing, hence no spurious additive offsets.

**Frozen three-scenario *total-intensity* sensitivity mixture:** weights 0.25/0.50/0.25; coherent multiplicative regulation lambdas 0.87, 1.0, 1.13. Weights and ±13% perturbation are analyst assumptions to reflect goaltending/injury/workload/shot-finishing uncertainty, *not derived from a goalie start mixture*. Mix each `(ANAfinal,CGYfinal,OT/SO-type)` state first; only then compute P(W/P/L/V) and `p_card` from the mixed distribution. They are not three empirical samples or three independent pieces of historical evidence. Expected full-score covariance includes between-scenario variance; continuous normal scoring not substituted for integer push mass. `P(reg tie)` ~0.159245, expected official extra goal ~0.159245; expected total = regulation 6.1120 + tie bonus ~6.2713. SD from enumerated common states; no Monte Carlo sampling or fitted calibration.

| Parameter | LOW | BASE | HIGH |
|---|---:|---:|---:|
| Weight | 0.25 | 0.50 | 0.25 |
| Regulation intensity multiplier | 0.87 | 1.00 | 1.13 |
| Reg λ_ANA | 2.974580 | 3.419058 | 3.863535 |
| Reg λ_CGY | 2.342882 | 2.692968 | 3.043054 |
| Mean final total | 5.489175 | 6.270671 | 7.054566 |

**`BASELINE_LEAGUE_V1` four exact supplied lines:** league-only 2025–26 NHL regular finished matches n=1,312; same full-game credited goal-score endpoint, all teams, not this matchup and no forecast game; cutoff at 2026-10-13 pre-event. Empirical frequencies baseline (no 0.5 placeholder): home ML=685/1312=0.522104; away+1.5 W=917/1312=0.698933; Over6 W=615, Push6=137, Lose=560, decisive n1175, p=615/1175=0.523404; Under6 W560, Push137, Lose615, p560/1175=0.476596. Baseline coverage **4/4 numeric supplied; 2/2 primary**. This comparator is a raw league reference, not independent held-out calibration, and carries its own matching 2025–26 cohort and no current-season data.

### A5. Supplied-only ranks, difficulty, action and shadows
- Exact raw index order (1) Flames+1.5, (2) Ducks ML, (3) Total Over6.0, (4) Total Under6.0 retained byte-legibly in A2. Complete four key ledger/ranking in Decision. All propositions supported numerically under framework convention. Conditional W+P+L+V=1 within numerical tail residual ≤1.44e-12.
- Rank1 `CGY +1.5`: mean signed Ducks margin μ=0.7450, SD=2.4996; line distance from centre `(1.5−μ)/SD=0.3020`, not used to alter discrete p. `ANA ML`: threshold margin0, z=-0.2981. Totals Over/Under6.0: `(6−μT)/SDT=-0.1075`; PUSH mass is 0.109609. Full final-score inclusion of SO winner credit frozen. Operator abandonment terms not provided.
- `SHADOW_MAIN_P_ORDER_V2`: NOT_COMPUTED (no independent defensible frozen full-derived ladder; source published would allow derived different lines, but caller forbids them entering the primary ranking). `SHADOW_MAIN_POLICY_GATE`: NOT_COMPUTED (universe absent). `RET03`: after excluding same margin-quantity candidates, supplied Over6 at 0.514553 is best different-quantity alternative, gap 0.115559, shadow *passes* 0.62/0.04 on supplied comparator only, not a published PASS. `RET04`: NONE (no other-quantity candidate p≥0.58). `XCARD6`: ANA ML (only other eligible p≥0.58, exact both-loss=0). `SHADOW_RANK_DELTA`: one eligible p≥0.58 positive change versus baseline (ANA ML +0.100526) so cannot form two eligible qualifying shadow ranks; NONE. `SHADOW_BASE_ONLY`: base slate CGY +1.5 (0.629292) / ANA ML (0.622733), original gate RANK1_UNSTABLE, rank2 floor true. All are NOT_PRIMARY; no retroactive pick replacement.

### A6. Adjustment source and joint coherence
| Mechanism | Source / evidence | Numeric treatment | Risk |
|---|---|---|---|
| Home venue | 2025–26 NHL reg home3.070 away2.935 | Venue-specific league base; NO second home-edge addition | Surface/rest not separately quantified |
| Team form | 2025–26 full season; first five Oct 2026 | k20 shrink GF/GA at 25 effective weight | Small early season, roster discontinuities; opponent strength unadjusted |
| Goalies | NHL projected Wolf/Cooley and Dostál/Husso; tiny .816/.818/.884/.935 SV% snapshot | NO independent goalie additive effect (already in team GF/GA); wide total-intensity scenarios instead | Starter-specific rate effects not identifiable |
| Injury/line combinations | NHL official projected lines/injured | Not numerical; no made-up scoring delta | Terry/Gauthier/Poehling absent changes ANA units; Huberdeau/Honzek absent for CGY |
| Special teams | Oct 10 single CGY0/3, ANA1/2; league details incomplete | No invented season PP/PK or penalty count term | One game not independent league rate |
| 5v5 chance/shot quality | Oct10 CGY chances28 ANA23, high-danger13/14; 29/28 shots | Qualitative cross-check only; no 5v5 xG inferred | Chance quality/finishing uncertainty |
| Rest/travel | Rematch Oct10 Calgary → Oct13 Anaheim, two days off between games | No claimed travel coefficient | ANA home ice, CGY road; calendar known |
| Empty nets | Historical credited scores include actual EN goals | Crude Poisson tail approximation, no separate fabricated EN state | State-dependent tail unmodelled |

**Exact complement/ordering checks:** p_Over6+p_Under6 = 1.000000000000; OverW=UnderL, both PUSH=0.109609. DucksML+Calgary +1.5 have intersecting *winning* sets but no intersecting losing set. Independent Poisson joint for regulation only; covariance on mixed final states printed in Decision; all derived from one normalized discrete score grid.

### A7. Sensitivities, rank stability and goalies
**Mix cases (same four supplied lines, probabilities over decisive outcomes):**
| Case | Reg λ_ANA | Reg λ_CGY | Expected total | CGY+1.5 | ANA ML | Over6 | Under6 | Top 2 by p |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LOW ×0.87 | 2.975 | 2.343 | 5.489 | 65.44% | 61.57% | 37.18% | 62.82% | Flames +1.5, Combined Total Goals: Under 6.0 Goals |
| BASE ×1 | 3.419 | 2.693 | 6.271 | 62.93% | 62.27% | 51.80% | 48.20% | Flames +1.5, Ducks ML |
| HIGH ×1.13 | 3.864 | 3.043 | 7.055 | 60.75% | 62.93% | 65.02% | 34.98% | Combined Total Goals: Over 6.0 Goals, Ducks ML |

Total-intensity assumption changes Rank1/2 composition across LOW and HIGH: `INTENSITY_SCENARIO_SENSITIVE` and `ADJUSTMENT_DEPENDENT`; decisive conditional Over6 range 37.178%–65.022% is sensitivity, NOT a confidence interval. League mean and team old/new forms do not establish ±13% calibrated limits. `WINDOW_SENSITIVITY_NOT_COMPUTABLE`: same-current-season L10/L15/L20 lack 10/15/20 independent eligible games; choosing an older-season substitution is explicitly forbidden without a supported recipe. The previous-season L20 is already incorporated as a separate pseudo-prior and never silently pooled into the observed current windows.

**Goalie-direction stress tests (separate non-fitted alternatives, not another mixture):** if Calgary goaltending underperforms and Anaheim's improves, change λANA by +0.35 and λCGY by −0.35 ⇒ ANA ML ≈73.16%, CGY+1.5 ≈51.92%, Over6 ≈51.49%; if reversed (Calgary improves / Anaheim weaker), λANA −0.35 and λCGY +0.35 ⇒ ANA ML ≈50.45%, CGY+1.5 ≈72.99%, Over6 ≈51.91%. The +/−0.35 goals are **unvalidated stress perturbations, not actual starter-specific estimated impacts**. They propagate goalie uncertainty through both winners/handicaps and totals. Current official starting goalies/backup minutes unavailable; nobody should treat these sensitivities as evidence that one option is a 70% pick.

### A8. Settlement fields, capture and unresolved tasks (NO SETTLEMENT)
`P-587` original contract fields to capture later from NHL game 2026020103: actual start and final times; confirmed CGY/ANA starters/backup TOI; final official GF/GA, regulation score, OT goal or SO credit, winner, empty-net goals, goalie saves/shots, 5v5 xG/high-danger if an actual original owner supplies, PP goals/chances and opponent adjusted data where measured; actual scratch/line sheet with publication timestamps; postponed/abandoned state; for each frozen contract WIN/LOSS/PUSH/VOID/UNRESOLVED under **user-provided operator's exact written terms if applicable**, not automatically under NHL convention. Verify credited shootout winning goal on exact owner box. Do not auto-notify or falsely claim future checks are scheduled; manual followup via next user-invoked settlement. `SETTLEMENT=NOT_PERFORMED`, `CANONICAL_IMPORT=NOT_PERFORMED`, `GITHUB_WRITES=NO`, `NEW_CANONICAL_IDS=0`.

### A9. Evidence-linked integrity checks and limitations
**C1–C20 mini-log-7**: C1 PARTIAL (one pinned published SHA; several operative excerpts, not all files read end-to-end). C2 PARTIAL (event NHL native ID, local duplicate check and indexed main search, massive Part7 body not inspected directly; external minis unknown). C3 PASS (frozen 4 supplied unique keys; probabilities descending). C4 PASS (actual Poisson discrete state calculation; W/P/L/V, complement sum, tail <2e-12). C5 PASS (supplied-only gate alternative and precision disclosed; failed actual gate). C6 PASS (Rank2 floor, exact mechanical joint zero). C7 PARTIAL (common-state intensity and goalie-direction stress tests; form windows n limited). C8 PARTIAL (home/venue + season form specified; inputs not fitted). C9 PARTIAL (verified NHL rule; OT/SO winner credit approximate mapping and missing EN-specific state). C10 PARTIAL (grading freeze framework, actual operator terms missing; manual capture only). C11 PASS disclosure (actual scheduled 12:45 crossed; late NOT_PREGAME, times separated). C12 PARTIAL (no odds consulted; collector/known-at lineage unknown). C13 PARTIAL (2025 archive rows verified, 2026 CSV missing and current 5 scores outside archive). C14 PASS (n1312 league-only exact-line baseline all 4). C15 PASS mathematical enumeration (scores/moments/covariance). C16 PASS **after physical readback verification only**. C17 PARTIAL (L5 current; L10–L20 shortfall and supplemental separated, shrink arithmetic). C18 PASS (z distances and baseline per-line available). C19 PASS (0.25/0.5/0.25 state-level mix, p_base separately, ε shown, base-only shadow). C20 PARTIAL (writer lease still active, intake/footer check subject to final readback, external writers not independently verifiable).

**FR1–FR6:** FR1 PARTIAL (5 current games each, previous-season supplemental trace 20, no full current 10–20); FR2 PASS separation (same league/format; separate year); FR3 PARTIAL (historical event trace and score fields complete, advanced metrics absent); FR4 PARTIAL (k20 pseudo prior but not a validated league-optimal k; window sensitivity not identified); FR5 PARTIAL (projected goalies and skaters, final start sheet unknown); FR6 PARTIAL (non-overlap trend and missingness documented, no full advanced data).

**SF-A1–SF-A12:** A1 PASS (4 literal raw→4 distinct). A2 PARTIAL (full-time action coherent but operator void exceptions unknown). A3 PASS conditionally (four normalized coherent sport-side rows, 0 operator-certified). A4 PASS (sorted unrounded). A5 PASS (only original four supplied). A6 PARTIAL (90% ceiling and generic/family checked, operator terms unknown). A7 PASS diagnostic (0.62/0.04 and 0.58 with exact actual p). A8 PASS conditional (shared lose sets zero, void caveat). A9 PASS shadows labelled and no substitutions. A10 PASS numerical (complete state, parameters, masses, separate baseline, timetamps). A11 PARTIAL (post official scheduled start; no prospective credit, some known-at timestamps unknown). A12 PASS only subject to actual file readback below (mini format/ID writer lease, frozen earlier blocks preserved; repository read-only).

**Q4:** weighted mixed mass within 1.5e-12 of unity; every conditional p in [0,1], all W/P/L nonnegative; expected score identities E[T]=E[H]+E[A], E[M]=E[H]−E[A]; covariance and SD from enumerated common states; exact integer push at 6 present; mirror signs correct; no numerical over-90% rows; mixture before conditioning; full supplied count=4 and ranking stable at actual p, although scenario order sensitive. Numerical validity does NOT confer empirical predictive skill or reliable opponent/goalie adjustments.
<!-- END CARD P-587 -->


<!-- BEGIN RESEARCH ADDENDUM P-587 2026-10-14-SHADOW-01 -->
### P-587 — issue-time shadow-delta interpretation correction (non-primary; 2026-10-14T12:59:23+11:00)

**Correction to original A5 `SHADOW_RANK_DELTA`:** The original A5 mistakenly required both qualifying rows to have *positive* p−baseline increments. Under `SELECTION_RULES.md` §3(c), the shadow universe contains every eligible supplied row with `p_card ≥ 0.58` and a frozen `BASELINE_P`; **negative deltas remain eligible**. The correct frozen same-row shadow is therefore:

| Shadow rank | Supplied proposition | Original p_card | Frozen league baseline | Delta p_card−baseline |
|---:|---|---:|---:|---:|
| 1 | Ducks ML | 0.622630 | 0.522104 | **+0.100526** |
| 2 | Flames +1.5 | 0.630112 | 0.698933 | **−0.068821** |

`SHADOW_RANK_DELTA` = `Ducks ML` / `Flames +1.5` (exact joint failure = 0 under the original completed-score state). This is an *informational* shadow; the **original frozen formal Rank 1 Flames +1.5, Rank 2 Ducks ML, numeric masses, gate, model version, scenario mix, issue timestamps and eventual settlement grades are unchanged**. The erroneous original wording is retained byte-for-byte for custody, with this dated correction taking precedence only for the shadow field. Original A9 statement that shadows were correctly defined is downgraded to `PARTIAL, resolved via this correction`. No new ID, original row replacement, reforecast, settlement or GitHub write. The original complete-card known-at/late status is unchanged.
<!-- END RESEARCH ADDENDUM P-587 2026-10-14-SHADOW-01 -->

<!-- BEGIN CARD P-588 -->
## Card · P-588 · BASKETBALL / NBA 2026 Preseason · Golden State Warriors @ Los Angeles Lakers · 2026-10-13 PDT / 2026-10-14 AEDT

- **Working ID and write status:** `P-588` / `LOCAL_UNIMPORTED` / `ISSUED_LOCAL` only after the active mini is written and read back. This card does **not** consume a canonical GitHub ID. Event native ID `0012600048`. User event key `NBA:2026-27:PRESEASON:0012600048:GSW@LAL:2026-10-13`; aliases `Golden State @ LA Lakers`, `Warriors vs Lakers`, `T-Mobile Arena`. A distinct Oct 6 preseason meeting was NBA `0012600010`; do not merge their identities.
- **Authority receipt:** `PUBLISHED_MAIN_PINNED e73c9c24e418250f8816932facc5feeecd94ef5d`; sports and arithmetic controls from published `main` only: `MDS-2026.10.12-v11.0`, `CR-2026.10.12-R2`, `SCV-2026.10.12-v7`, `SEL-2026.10.12-v3`, `P_ORDER_V2` full-universe publication. **User-supplied primary deviation:** `PROMPT_REVISION=SF-2`, `SUPPLIED_FIRST_V1`, four supplied contracts only. Scope `LOCAL_MINI_STAGING`; no GitHub writes, result settlement or import. No conflicting local control files were applied.
- **Location / timing:** Official Tuesday 13 Oct 2026 **7:00 PM PDT** (Vegas UTC−7) = Wed 14 Oct **02:00 UTC** = **13:00 AEDT** (Melbourne UTC+11); T-Mobile Arena, Las Vegas, Lakers home-designated but site NEUTRAL. User schedule estimate matches. Request appeared around the scheduled time; original status at read: fixture listed as upcoming/pregame in web search, but no independently verified actual tipoff or live clock. Research inputs were obtained around and **after** scheduled tipoff; research completion and local issue at `2026-10-14T13:14:34+11:00`. `TIMING=LATE_START_UNVERIFIED`, `OUTCOME_EXPOSURE=NONE_OBSERVED` (no live/final score intentionally consulted), `ACTUAL_TIPOFF=NOT_VERIFIED`, `NOT_PROSPECTIVE_CERTIFIED`. Analysis input cutoff = `2026-10-14T13:14:34+11:00` for retrieval; strictly historical score rows finished by Oct 10, with contemporary lineup news whose exact publication/field timestamps are `KNOWN_AT_UNVERIFIED`. This is *not* a reconstructed clean pregame prediction.
- **Analysis:** `UNCALIBRATED_ANALYST_SCENARIO`, `RESEARCH_ONLY_NOT_CERTIFIED`; low-data early preseason, rotational uncertainty, lineup gate `UNCONFIRMED`. **Expected full game (including approximate OT): Warriors 113.209 ± 14.756 SD; Lakers 108.917 ± 14.981; total 222.126 ± 23.624; signed Warriors−Lakers margin +4.292 ± 18.063; score covariance 57.952; corr 0.262.** Estimated winner GSW **59.397%**, Lakers 40.603%. Model regulation draw mass **2.149%**; all modelled game outcomes after repeated OT are decisive with zero full-game draw. These are *model outputs*, not official score forecasts or calibration.
- **Frozen supplied universe:** `P588_SUPPLIED_0012600048_SF2_v1`, ordered 4 original rows ⇒ 4 distinct; `Warriors -2.5`; `Lakers +2.5`; `Combined Total Points: Over 228.5 Points`; `Combined Total Points: Under 228.5 Points`. No optional placeholder becomes a proposition; no generated candidate enters primary ranks. Stable keys, raw mappings, endpoint and definitions in A1–A2.
- **Endpoint:** NBA exhibition, four 12-min regulation quarters and repeated 5-min overtime until winner under ordinary playing rules, if no event-specific exception. Full GAME points and signed margin include overtime. GSW −2.5 wins if final GSW−LAL ≥3; LAL +2.5 wins if difference ≤2; Over228.5 wins if final total ≥229, Under if ≤228. **Both half-point pairs have zero PUSH on a completed scored game**. Operator cancellation/abandonment/void terms absent: `UNKNOWN_DEFINITION` for all-event operator settlement; a reported sporting `FROZEN_FRAMEWORK_CONVENTION` applies conditionally to normally completed games. A future shortened, cancelled or abandoned game is not presumed decisive.
- **Scoring basis / strict limitation:** NBA preseason completed score traces 4 Warriors and 3 Lakers (only). 2025–26 regular-season results are **supplemental evidence only**, not pooled with October 2026 exhibition form. No supported pace/possessions or consistent ORtg/DRtg denominator from these exact team event score rows; model class is **`SCORE_BASED_APPROXIMATION`**, not a fitted possessions × efficiencies prediction. Material analyst assumption (LAL −3.0 points on average due to Dončić rest/rotation) **changes Rank 2**; without it, Rank 2 is Lakers +2.5. Do not call lineup adjustment learned or measured.
- **Same-line frozen baseline:** `BASELINE_LEAGUE_V1: NOT_AVAILABLE` for all four supplied rows: the pinned NBA/2025 file has **0 preseason rows** of 1,325 logical rows (1,230 regular; 95 other); NBA regular-season mean/width is the wrong stage, not an interchangeable preseason baseline. No independent, cutoff-safe same-era preseason full-game score population/parameter fit completed. **BASELINE_P coverage 0/4 supported / 0/2 formal.** `NO_LEAGUE_PROFILE / PROFILE_LACKS_ENDPOINT`; do not silently use regular-season baseline or 0.500.

### Decision — original frozen `SUPPLIED_CONTRACT_RANKING` (SUPPLIED_FIRST_V1)

**Formal, supplied-only top two:** **1) Total Under 228.5 (60.955%)**, **2) Warriors −2.5 (54.673%)**. All four lines are priced under the same conditional completed-score mixture. Under is first mainly because the recent exhibition totals, probable absences and total uncertainty make 229+ points less likely than 228 or fewer *under this arbitrary, uncalibrated mixture*. The Warriors' −2.5 advantage is fragile and entirely conditional on subjective lineup/usage adjustments; the neutral-venue designation prevents automatic full home edge.

| Rank | Role | Supplied key / proposition | W | L | P | V | `p_card = W/(W+L)` | `p_base` | `BASELINE_P` | Principal failure route |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | PICK | `T:GSW_plus_LAL:lt_228.5:FULL_OT:NBA_PRE` — **Combined Total Points: Under 228.5 Points** | 0.609554 | 0.390446 | 0.000000 | `0 conditional / all-event unknown` | 0.609554 | 0.636129 | `NO_PRESEASON_BASELINE` | final points >=229 |
| 2 | PICK | `M:GSW_minus_LAL:gt_2.5:FULL_OT:NBA_PRE` — **Warriors -2.5 points** | 0.546734 | 0.453266 | 0.000000 | `0 conditional / all-event unknown` | 0.546734 | 0.574168 | `NO_PRESEASON_BASELINE` | Golden State wins by <=2 or loses |
| 3 | INFORMATIONAL | `M:GSW_minus_LAL:lt_2.5:FULL_OT:NBA_PRE` — **Lakers +2.5 points** | 0.453266 | 0.546734 | 0.000000 | `0 conditional / all-event unknown` | 0.453266 | 0.425832 | `NO_PRESEASON_BASELINE` | Golden State wins by >=3 |
| 4 | INFORMATIONAL | `T:GSW_plus_LAL:gt_228.5:FULL_OT:NBA_PRE` — **Combined Total Points: Over 228.5 Points** | 0.390446 | 0.609554 | 0.000000 | `0 conditional / all-event unknown` | 0.390446 | 0.363871 | `NO_PRESEASON_BASELINE` | final points <=228 |

**Rank-1 diagnostics:** supplied-only rank 1 Under228.5 `p_card=0.609554` versus best eligible noncomplementary supplied alternative Warriors−2.5 `0.546734`; lead `0.062820` (**6.282 pp**, ≥0.04), but `p_card < 0.62`: **`SUPPLIED_SCOPE_GATE=RANK1_UNSTABLE`**. Rank 2 `0.546734 < 0.58`: **`RANK2_FLOOR_FAIL`**. Both numeric rows ≤0.90 ceiling and no sport-family blocker beyond acknowledged incomplete lineup/known-at; independent published full-universe P_ORDER_V2 gate `NOT_COMPUTED` (no legitimate derived universe frozen). No high-confidence PASS or promised prediction accuracy.

**Exact common-state dependence:** losses of Under228.5 and Warriors−2.5 intersect when *total ≥229 and GSW margin ≤2*, modelled `P(both lose)=0.180551` (**18.055%**). At least one wins with model probability `0.819449`, not certainty; this pair is **NOT MECHANICALLY_PROTECTED**. Under and Over 228.5 are strict complementary rows; Warriors−2.5 and Lakers+2.5 are strict complementary rows for completed games. These complements each sum to 1; neither is a demonstration of independent rank skill. See A5 for exact bounds and shadow dispositions.

### A1. Identity, original supplied ledger and reading receipt

**Raw user input (preserve indexes, correct unit/side, unique four):**

| RAW_INPUT_INDEX | Literal supplied row | Stable resolved key | Duplicate action |
|---:|---|---|---|
| 1 | `Warriors -2.5` | `M:GSW_minus_LAL:gt_2.5:FULL_OT:NBA_PRE` | distinct; issued training-candidate row |
| 2 | `Lakers +2.5` | `M:GSW_minus_LAL:lt_2.5:FULL_OT:NBA_PRE` | distinct; issued training-candidate row |
| 3 | `Over 228.5` | `T:GSW_plus_LAL:gt_228.5:FULL_OT:NBA_PRE` | distinct; issued training-candidate row |
| 4 | `Under 228.5` | `T:GSW_plus_LAL:lt_228.5:FULL_OT:NBA_PRE` | distinct; issued training-candidate row |

- Identity: NBA `0012600048` is *GSW @ LAL*, 2026-10-13 US date, **2026 preseason**, game 4 Lakers / game 5 Warriors. Neutral T-Mobile Arena, Las Vegas. Oct 6 earlier game `0012600010`, not a duplicate or postponed identity.
- Source/custody search: original local mini inspected in full (`P-585` to `P-587`, all preserved), no local `0012600048`/Warriors–Lakers event key; GitHub default-branch code search of native ID and named 2026-10-13 fixture returned zero matches. `CURRENT_STATE` + `GAME_LOG_STATUS_CURRENT` pinned head next committed P-585; local actual footer next P-588. Massive Combined Part 7 literal body still `NOT_VERIFIED` for exact event search, and external unshared minis/writers `NOT_VERIFIED`; no observed collision.
- **Reading receipt** — `PUBLISHED_MAIN_PINNED e73c9c24e418250f8816932facc5feeecd94ef5d`; fetched in full at pinned SHA: README, CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, SCORING_AND_VALIDATION, PROBABILITY_TOOLKIT, VERIFICATION_PROTOCOL, SOURCES, ARCHIVE_USE_GUIDE, BASE_RATES_REGISTER, prompts README and `1_GAME_CARD`, RULES_BASKETBALL, LEAGUE_PROFILES, GAME_LOG_STATUS_CURRENT, `Previous Sports Results/Basketball/NBA/2025/2025_games.csv`; `NBA/2026/2026_games.csv` NOT_FOUND. Relevant sections CURRENT_RULES §§0–8, SELECTION §§1–4,9, TEMPLATES §§2–3,7, SOURCES §3.2/§3.13, ARCHIVE §§1–4,8–9, RULES_BASKETBALL §0, LEAGUE_PROFILES Basketball, BASE_RATES §§7.1, PROBABILITY_TOOLKIT §1, SCORING §§1–3. Source input: supplied `SF-2` umbrella prompt and populated NBA section. No local control diff applied to published version. User's `SUPPLIED_FIRST_V1` primary-universe override explicitly conflicts with repository Rule P4 (supplied contracts reference only); user scope governs only the **local** card with separate policy, not a claim to change published main.
- Mode `LOCAL_MINI_STAGING`; allowed local mini intake/card/footer and same-file mirrors; prohibited settlement, retrospective grading, GitHub canonical import or changes. Lease read in header: ChatGPT this conversation valid 2026-10-13 15:55:33 to 2026-10-14 15:55:33 AEDT, `Frozen for settlement=NO`; expiry rechecked prior to write. Original file SHA `5bd43e969157dff559b3edd5ea9f319456e02eb5876e0872b030da147e982db8`. End user-issue/prewrite receipt is A9 + external readback file.

### A2. Action and competition definitions

All four rows are **completed full-game** NBA preseason scoring propositions with full regulation (4 × 12 minutes), plus any repeated 5-minute overtime. Contract constants are exact ±2.5 point margin and 228.5 total (so no integer equality/PUSH when scored final exists). Formulas: `M = GSW−LAL`, `T=GSW+LAL`, Warriors−2.5 `M≥3`, Lakers+2.5 `M≤2`, Over `T≥229`, Under `T≤228`. League standard five-foul team penalty situation, six personal fouls disqualifies, 5-minute OT, unless event-specific exception; exact exception NOT_VERIFIED. Betting operator's written terms NOT_SUPPLIED: no assumptions about postponement, midgame cancellation, early abandonment, void or settlement dispute; no all-event VOID rate invented. Conditional scoring universe has `W+P+L+V=1`, `P=V=0` for each completed contract; all-event model is **unestimated**.

### A3. Historical form, source trace, coverage and lineups (`A3-FORM`, `A3-LINEUPS`)

**Coverage audit:** Pinned `Previous Sports Results/Basketball/NBA/2025/2025_games.csv` **1,325 rows**, **1,230 REGULAR**, **0 PRESEASON**; 2026 season file path NOT_FOUND. Regular postseason and 2026 preseason **not pooled**. Latest current-source NBA full scores: GSW 2026-10-10, LAL 2026-10-08, pre-cutoff. Previous-season last final 2026-04-12 both. Current preseason comparable events unique: GSW 4, LAL 3, from official NBA game cards. No same-season L5 *full*, L10, L15 or L20 cohort; every cumulative current-window row faithfully reuses the available n rather than inventing a longer history. Opponent/rival strength, neutral/home segmentation and lineups change between games. Derived pace/possessions, shot quality, player on/off, minutes-adjusted ORtg/DRtg, reconciled overtime on aggregate archive score rows: `NOT_COMPUTED/NOT_AVAILABLE`.

**Golden State Warriors — current 2026 preseason, 4/4 completed:**

| Window | Eligible n/target | Observed scoring fields | W–L | Points for / against | Margin / total | Venue count | Opponent adjustment | Latest source |
|---|---:|---|---|---|---|---|---|---|
| L5 | 4/5 | score 4; pace/ORtg/DRtg **0** | 2–2 | 113.50 / 107.75 | +5.75 / 221.25 | 2 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-10 latest; PRESEASON 2026 |
| L10 | 4/10 | score 4; pace/ORtg/DRtg **0** | 2–2 | 113.50 / 107.75 | +5.75 / 221.25 | 2 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-10 latest; PRESEASON 2026 |
| L15 | 4/15 | score 4; pace/ORtg/DRtg **0** | 2–2 | 113.50 / 107.75 | +5.75 / 221.25 | 2 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-10 latest; PRESEASON 2026 |
| L20 | 4/20 | score 4; pace/ORtg/DRtg **0** | 2–2 | 113.50 / 107.75 | +5.75 / 221.25 | 2 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-10 latest; PRESEASON 2026 |

**Los Angeles Lakers — current 2026 preseason, 3/3 completed:**

| Window | Eligible n/target | Observed scoring fields | W–L | Points for / against | Margin / total | Venue count | Opponent adjustment | Latest source |
|---|---:|---|---|---|---|---|---|---|
| L5 | 3/5 | score 3; pace/ORtg/DRtg **0** | 2–1 | 113.00 / 112.33 | +0.67 / 225.33 | 1 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-08 latest; PRESEASON 2026 |
| L10 | 3/10 | score 3; pace/ORtg/DRtg **0** | 2–1 | 113.00 / 112.33 | +0.67 / 225.33 | 1 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-08 latest; PRESEASON 2026 |
| L15 | 3/15 | score 3; pace/ORtg/DRtg **0** | 2–1 | 113.00 / 112.33 | +0.67 / 225.33 | 1 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-08 latest; PRESEASON 2026 |
| L20 | 3/20 | score 3; pace/ORtg/DRtg **0** | 2–1 | 113.00 / 112.33 | +0.67 / 225.33 | 1 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-10-08 latest; PRESEASON 2026 |

**Current pre-match event trace — newest first; native ID, date, orientation, points, outcome.** Official score sources R04–R09 listed in A8; all completion dates safely before Oct 14 but exact completed wall-clock publication receipts unavailable (important only for same-day exclusions, none selected).

Golden State:

| Latest-first | Completed US date | NBA ID | Opponent | Home/away | GSW–opp | Status / form eligibility |
|---:|---|---|---|---|---|---|
| 1 | 2026-10-10 | `0012600014` | SAC | H | 111–106 (W) | pre-match final NBA / current PRESEASON |
| 2 | 2026-10-07 | `0012600033` | POR | A | 118–123 (L) | pre-match final NBA / current PRESEASON |
| 3 | 2026-10-06 | `0012600010` | LAL | H | 124–98 (W) | pre-match final NBA / current PRESEASON |
| 4 | 2026-10-04 | `0012600066` | LAC | A-N | 101–104 (L) | pre-match final NBA / current PRESEASON |

Lakers:

| Latest-first | Completed US date | NBA ID | Opponent | Home/away | LAL–opp | Status / form eligibility |
|---:|---|---|---|---|---|---|
| 1 | 2026-10-08 | `0012600036` | SAC | H | 114–110 (W) | pre-match final NBA / current PRESEASON |
| 2 | 2026-10-06 | `0012600010` | GSW | A | 98–124 (L) | pre-match final NBA / current PRESEASON |
| 3 | 2026-10-05 | `0012600028` | SAC | A | 127–103 (W) | pre-match final NBA / current PRESEASON |

**Previous 2025–26 NBA regular season — supplementary only (not matched to preseason coaching/roster usage, no numerical pooling):**

**Golden State Warriors — 2025–26 REGULAR SEASON, NOT POOLED**

| Window | Eligible n/target | Observed scoring fields | W–L | Points for / against | Margin / total | Venue count | Opponent adjustment | Latest source |
|---|---:|---|---|---|---|---|---|---|
| L5 | 5/5 | score 5; pace/ORtg/DRtg **0** | 1–4 | 111.40 / 116.00 | -4.60 / 227.40 | 3 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |
| L10 | 10/10 | score 10; pace/ORtg/DRtg **0** | 3–7 | 111.40 / 117.30 | -5.90 / 228.70 | 7 home / 3 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |
| L15 | 15/15 | score 15; pace/ORtg/DRtg **0** | 5–10 | 112.40 / 118.80 | -6.40 / 231.20 | 7 home / 8 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |
| L20 | 20/20 | score 20; pace/ORtg/DRtg **0** | 5–15 | 112.35 / 118.60 | -6.25 / 230.95 | 9 home / 11 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |

**Los Angeles Lakers — 2025–26 REGULAR SEASON, NOT POOLED**

| Window | Eligible n/target | Observed scoring fields | W–L | Points for / against | Margin / total | Venue count | Opponent adjustment | Latest source |
|---|---:|---|---|---|---|---|---|---|
| L5 | 5/5 | score 5; pace/ORtg/DRtg **0** | 3–2 | 113.20 / 108.00 | +5.20 / 221.20 | 3 home / 2 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |
| L10 | 10/10 | score 10; pace/ORtg/DRtg **0** | 7–3 | 116.20 / 112.20 | +4.00 / 228.40 | 6 home / 4 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |
| L15 | 15/15 | score 15; pace/ORtg/DRtg **0** | 11–4 | 115.67 / 111.53 | +4.13 / 227.20 | 6 home / 9 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |
| L20 | 20/20 | score 20; pace/ORtg/DRtg **0** | 16–4 | 118.10 / 112.40 | +5.70 / 230.50 | 11 home / 9 away or neutral | opponent-adjusted: unavailable | 2026-04-12 latest; REGULAR 2025–26 SUPPLEMENT |


**Full L20 supplemental event trace from pinned previous-season archive:** oldest full season league notes not treated as matchup talent regressors. Current-season n=4/3 dominates the explicit *ad hoc* model, and the supplemental records are for regime comparison only, not four independent form confirmations.

GSW 2025–26 regular:

| i | Final date | Native game ID | Opponent | Venue | GSW–opponent | Status |
|---:|---|---|---|---|---|---|
| 1 | 2026-04-12 | `401811054` | LA Clippers | A | 110–115 (L) | prev-season REGULAR / supplementary only |
| 2 | 2026-04-10 | `401811039` | Sacramento Kings | A | 118–124 (L) | prev-season REGULAR / supplementary only |
| 3 | 2026-04-09 | `401811025` | Los Angeles Lakers | H | 103–119 (L) | prev-season REGULAR / supplementary only |
| 4 | 2026-04-07 | `401811009` | Sacramento Kings | H | 110–105 (W) | prev-season REGULAR / supplementary only |
| 5 | 2026-04-05 | `401810997` | Houston Rockets | H | 116–117 (L) | prev-season REGULAR / supplementary only |
| 6 | 2026-04-02 | `401810972` | Cleveland Cavaliers | H | 111–118 (L) | prev-season REGULAR / supplementary only |
| 7 | 2026-04-01 | `401810968` | San Antonio Spurs | H | 113–127 (L) | prev-season REGULAR / supplementary only |
| 8 | 2026-03-29 | `401810945` | Denver Nuggets | A | 93–116 (L) | prev-season REGULAR / supplementary only |
| 9 | 2026-03-27 | `401810928` | Washington Wizards | H | 131–126 (W) | prev-season REGULAR / supplementary only |
| 10 | 2026-03-25 | `401810915` | Brooklyn Nets | H | 109–106 (W) | prev-season REGULAR / supplementary only |
| 11 | 2026-03-23 | `401810899` | Dallas Mavericks | A | 137–131 (W) | prev-season REGULAR / supplementary only |
| 12 | 2026-03-21 | `401810881` | Atlanta Hawks | A | 110–126 (L) | prev-season REGULAR / supplementary only |
| 13 | 2026-03-20 | `401810872` | Detroit Pistons | A | 101–115 (L) | prev-season REGULAR / supplementary only |
| 14 | 2026-03-18 | `401810854` | Boston Celtics | A | 99–120 (L) | prev-season REGULAR / supplementary only |
| 15 | 2026-03-16 | `401810839` | Washington Wizards | A | 125–117 (W) | prev-season REGULAR / supplementary only |
| 16 | 2026-03-15 | `401810836` | New York Knicks | A | 107–110 (L) | prev-season REGULAR / supplementary only |
| 17 | 2026-03-13 | `401810821` | Minnesota Timberwolves | H | 117–127 (L) | prev-season REGULAR / supplementary only |
| 18 | 2026-03-10 | `401810798` | Chicago Bulls | H | 124–130 (L) | prev-season REGULAR / supplementary only |
| 19 | 2026-03-09 | `401810789` | Utah Jazz | A | 116–119 (L) | prev-season REGULAR / supplementary only |
| 20 | 2026-03-07 | `401810775` | Oklahoma City Thunder | A | 97–104 (L) | prev-season REGULAR / supplementary only |

LAL 2025–26 regular:

| i | Final date | Native game ID | Opponent | Venue | LAL–opponent | Status |
|---:|---|---|---|---|---|---|
| 1 | 2026-04-12 | `401811053` | Utah Jazz | H | 131–107 (W) | prev-season REGULAR / supplementary only |
| 2 | 2026-04-10 | `401811040` | Phoenix Suns | H | 101–73 (W) | prev-season REGULAR / supplementary only |
| 3 | 2026-04-09 | `401811025` | Golden State Warriors | A | 119–103 (W) | prev-season REGULAR / supplementary only |
| 4 | 2026-04-07 | `401811010` | Oklahoma City Thunder | H | 87–123 (L) | prev-season REGULAR / supplementary only |
| 5 | 2026-04-05 | `401810995` | Dallas Mavericks | A | 128–134 (L) | prev-season REGULAR / supplementary only |
| 6 | 2026-04-02 | `401810971` | Oklahoma City Thunder | A | 96–139 (L) | prev-season REGULAR / supplementary only |
| 7 | 2026-03-31 | `401810958` | Cleveland Cavaliers | H | 127–113 (W) | prev-season REGULAR / supplementary only |
| 8 | 2026-03-30 | `401810953` | Washington Wizards | H | 120–101 (W) | prev-season REGULAR / supplementary only |
| 9 | 2026-03-27 | `401810930` | Brooklyn Nets | H | 116–99 (W) | prev-season REGULAR / supplementary only |
| 10 | 2026-03-25 | `401810907` | Indiana Pacers | A | 137–130 (W) | prev-season REGULAR / supplementary only |
| 11 | 2026-03-23 | `401810893` | Detroit Pistons | A | 110–113 (L) | prev-season REGULAR / supplementary only |
| 12 | 2026-03-21 | `401810879` | Orlando Magic | A | 105–104 (W) | prev-season REGULAR / supplementary only |
| 13 | 2026-03-19 | `401810865` | Miami Heat | A | 134–126 (W) | prev-season REGULAR / supplementary only |
| 14 | 2026-03-18 | `401810862` | Houston Rockets | A | 124–116 (W) | prev-season REGULAR / supplementary only |
| 15 | 2026-03-16 | `401810844` | Houston Rockets | A | 100–92 (W) | prev-season REGULAR / supplementary only |
| 16 | 2026-03-14 | `401810829` | Denver Nuggets | H | 127–125 (W) | prev-season REGULAR / supplementary only |
| 17 | 2026-03-12 | `401810815` | Chicago Bulls | H | 142–130 (W) | prev-season REGULAR / supplementary only |
| 18 | 2026-03-10 | `401810801` | Minnesota Timberwolves | H | 120–106 (W) | prev-season REGULAR / supplementary only |
| 19 | 2026-03-08 | `401810777` | New York Knicks | H | 110–97 (W) | prev-season REGULAR / supplementary only |
| 20 | 2026-03-06 | `401810769` | Indiana Pacers | H | 128–117 (W) | prev-season REGULAR / supplementary only |

**Non-overlap trend:** 2026 exhibition block 1–5 is PARTIAL (GSW n4, LAL n3); blocks 6–10, 11–15, 16–20 contain **zero** same-season eligible games. Previous-season regular blocks are not continuous 2026 preseason trends. Most recent 2-game subset: GSW scored 229/allowed 229 (114.50/114.50); LAL scored 212/allowed 234 (106.00/117.00) — high variance and opponent identity effects; evaluated as **L2_DIAGNOSTIC_ONLY** separately in A7. League-level current preseason μ and SD are `NOT_ESTIMATED` because same-stage population was not audited. `FR4 r_shrunk` **NOT_COMPUTED**: no supported same-stage league mean LM or eligible league-specific shrinkage n and k; do not invent k=2 or import regular-season reference across stages.

**Lineups / rotation (`LINEUP_GATE=UNCONFIRMED`, no verified full active bench):** GSW local contemporary lineup projection *Curry / Podziemski / Gui Santos / Yaxel Lendeborg / Draymond Green*; Steve Kerr's reported **regular-season intended lineup** is not a matchday confirmation. Expected rotational contributors include reserves Brandon Williams, Dalen Terry, Charles Bassey, Graham Ike (status not certified). Al Horford reportedly rested, Kristaps Porziņģis not back in team action, Butler and Moody reported absent. Lakers more recent injury report says **Luka Dončić rested (not injured)** and **Walker Kessler expected preseason debut** (finger), with Collin Sexton, Adou Thiero, Ziaire Williams and Cameron Carr unavailable. Other preview suggesting a starting Dončić is inconsistent with the newer absence report; do not mark him active. Austin Reaves / Quentin Grimes / Jake LaRavia are plausible core options only; fifth slot and full bench roster `NOT_VERIFIED`. No official complete tipoff starting-five plus bench printout located at research/issue. No player-minutes or lineup-effect point coefficient was measured for this fixture.

**Rest/travel / venue:** GSW played Sat Oct10 at home in San Francisco; Lakers played Thu Oct8 in Los Angeles; the fixture is Tue Oct13 evening at Las Vegas neutral T-Mobile Arena. GSW two off days, Lakers four off days (local game dates; actual overnight arrival unknown). No regular-season home advantage automatically assigned to designated Lakers. Travel effects not numerically measured. Reported player minutes/rest matter more than prior-April scoring form. Opponent strength adjustment `OPPONENT_ADJUSTMENT_UNAVAILABLE`, as no common opponent/strength model was fitted.

### A4. Model, score distribution, probabilities, and expected points

**Numerical method actually executed:** standalone local scratch Python/NumPy/SciPy computation `/mnt/data/p588_calc.py` (not placed in GitHub); revision `P588_SCORE_BASED_DISCRETE_NORMAL_3CASE_7OT_v1`. For each scenario, enumerate integer regulation score pairs `(GSW=x,LAL=y)`, x,y ∈ {0,…,210}; weights proportional to `Normal(x+y; μ_total, σ_total=22) × Normal(x−y; μ_margin, σ_margin=18)` and normalise to 1. This is a **discretised joint Gaussian score approximation**, not a possessions model or fitted stochastic simulator. Implied equal-team reg SD sqrt((22²+18²)/4)=14.212670, reg score Cov(G,L)=40.000 and corr 0.198020; both valid. The 2025–26 NBA REGULAR profile has narrower `σ_total≈20.04`, `σ_margin≈15.98`, but use widened **subjective** 22/18 for this preseason rotational uncertainty; NOT a stage-fitted width.

Regulation draw mass per scenario ≈ 0.02. After a regulation tie at `(k,k)`, append *independent per-team 5-minute overtime scores* `Poisson(12.5)` each. If still tied, repeat 5-minute overtime, preserving cumulative team points. Exactly enumerate scoring through up to **7 overtime periods**, summing all decisive final states; residual seventh consecutive tied-OT probability conditional on reaching overtime `0.0000000213`; full-event residual <`0.0000000005`. Overtime-score Poisson tail >59 points per player per period negligible within chosen support. Credited final score includes OT points, not postgame penalty/shootout; 48-minute regulation and 5-min overtime; multiple OT until non-tie. This is an explicitly approximate OT transition, not a claimed validated possession-level overtime simulation.

**Frozen raw pregame score means (2026 PRESEASON n4/n3):** GSW scored `113.500` / allowed `107.750`; Lakers scored `113.000` / allowed `112.333`. Symmetric, neutral venue matchup: `μ_GSW,raw=(113.5+112.333333)/2=112.916667`; `μ_LAL,raw=(113.0+107.75)/2=110.375000`. **No possessions or ORtg inferred from scoring**. Approximate baseline level from these samples, NOT `BASELINE_LEAGUE_V1`.

**Declared parameter adjustments:** Base LAL −3 points relative raw neutral (Dončić rest/rotation as **unfitted subjective assumption**, NOT measured actual loss of 3); GSW net zero for Curry ramp/Kessler rim protection/Warriors absence uncertainty. A 0/0 counterfactual is reported A7; -3 is NOT counted again through the scenario mix. LOW/HIGH joint cases shift each team coherently to reflect slow/fast exhibition pace and unconfirmed participant minutes, not separate independent weights, nor a fitted ±CI. Freeze weights before ranking: LOW 0.25, BASE 0.50, HIGH 0.25. Because each scenario is a valid common final-score state distribution, mix unconditional W and L masses first, then condition by decisive mass. For each half-point completed-game contract, P=V=0 and decisive mass approximately 1; hence the displayed p is also conditional W.

| Scenario | Weight | μ_GSW regulation | μ_LAL regulation | Under 228.5 | GSW −2.5 | Lakers +2.5 | Over 228.5 | Scenario top two |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LOW_TOTAL | 0.25 | 107.917 | 104.375 | 0.759563 | 0.530342 | 0.469658 | 0.240437 | Under 228.5; Warriors -2.5 |
| BASE | 0.50 | 112.917 | 107.375 | 0.636129 | 0.574168 | 0.425832 | 0.363871 | Under 228.5; Warriors -2.5 |
| HIGH_TOTAL | 0.25 | 117.917 | 115.375 | 0.406394 | 0.508258 | 0.491742 | 0.593606 | Over 228.5; Warriors -2.5 |

**Mixture output:** expected GSW=`113.208704`, Lakers=`108.917037`, total=`222.125741`, signed GSW margin=`4.291667`; marginal score SDs `14.756045` and `14.981155`, total SD `23.623721`, margin SD `18.062989`, score covariance `57.952150`. Identity checks: E[T]=E[G]+E[L] and E[M]=E[G]−E[L]; Var(T)=Var(G)+Var(L)+2cov; Var(M)=Var(G)+Var(L)−2cov. Model reg tie mass 0.021489; after OT P(GSW winner)=0.593966, P(LAL winner)=0.406034, draw=0, zero probabilities for league match tie once all OTs resolved. Unconditional mixtures normalize by completed-game probability; operator void probability unmodelled. Sample support excludes impossible negative points; exact NBA two/three-point scoring sequences are not explicitly simulated (discrete total score approximation).

**Numerical precision:** all contracts half-point → no pushes; calculated score weights normalised; total-vs-under and reciprocal spread complements sum 1 within `1e−12`; 7-OT residual <2.2e−8 conditional overtime before lower event tie multiplier. Discretisation and analyst parameter uncertainty are larger than floating error; exact grid truncation beyond 210 team points was effectively negligible but is a *model support restriction*, not verified NBA physics. Probabilities printed six decimals; no thresholds decided within 0.002, no false precision-driven PASS. W/P/L/V conditional complete: W=p, P=0, L=1−p, V=0; any alternative settlement conditions not in the conditional sample remain `UNKNOWN_DEFINITION`.

### A5. Full supplied ranking, gate, comparator and dependence

**SUPPLIED_CONTRACT_RANKING** is the four-row Decision table (unrounded underlying p in JSON; no missing or excluded supplied row). Numeric key order as displayed; all four ≤90% ceiling. RAW_INPUT_INDEX 1–4 retained even where ranked order differs; none duplicated. No fifth candidate created. For an integer score m: `P(Warriors−2.5)=P(M≥3)=0.546734`, `P(Lakers+2.5)=P(M≤2)=0.453266`; `P(Under)=P(T≤228)=0.609554`, `P(Over)=P(T≥229)=0.390446`. Both pairs of complements satisfy p sum exactly 1. No current-game actual score/result used.

**Gate and precision:** `SUPPLIED_SCOPE_GATE=RANK1_UNSTABLE` because `0.609554<0.620000`, despite competitor Warriors−2.5 `0.546734` and gap `0.062820>0.04`. Rank-2 floor `0.546734<0.58` (`FLOOR_FAIL`). Precision epsilon ε=0.00005 for numerically implemented *model probabilities* given grid/tail approximation, **not a physical/form uncertainty bound**; do not imply confident parameter estimates. Eligible family definition: preseason final-score full game with standard NBA OT, all four modelled, operator action missing; all-event selection remains uncertified.

**Exact two-primary joint losing mass** `0.180551` from common completed-game states where `T≥229` and `M≤2`; Fréchet bounds `[0, 0.390446]`. `P(both primary decisive)=1` conditional completed-game model; no push; `P(at least one win)=0.819449` is a mechanical calculation from model probabilities, **not** a verified skill rate. No mechanically protected Rank1–Rank2 pair here; `P(both lose)>0`, 0.30 historical target met, 0.35 warning not triggered under this *untested* model. Opposite sides on each same line are strict mutually exhaustive complements in the conditional completed-score universe; choosing both such sides would make Hit@2 a structural artefact, not proof.

**Same-exact-line baseline:** `BASELINE_LEAGUE_V1` attempted from `Previous Sports Results/Basketball/NBA/2025/2025_games.csv` and league profiles; no comparable PRESEASON population. Regular-season `n=1230` logged but not used as stage-specific baseline. Register NBA 2025–26 n=1,235 uses a differently scoped cohort and cannot be treated as the same sample. Baseline 0/4 numeric and 0/2 primary; codes `NO_LEAGUE_PROFILE`, `PROFILE_LACKS_ENDPOINT`. Frozen baseline route fails rather than inventing p=0.50, and paired skill later is NOT_COMPUTABLE until a legitimate independently frozen preseason same-line comparator exists.

**Shadows** (all `NOT_PRIMARY`): `SHADOW_MAIN_P_ORDER_V2`/published full universe: `NOT_COMPUTED` (no frozen supported derived ladder; limited user-supplied scope). `SHADOW_GATE_RET03` excludes same-quantity competitors: best other quantity Warriors−2.5, same gap, gate RANK1_UNSTABLE. `SHADOW_R2_RET04` highest eligible different quantity from Under228.5 = Warriors−2.5, but floor 58% NOT_MET → NONE under strict floor. `SHADOW_R2_XCARD6`: NONE because no remaining supported supplied row >=0.58. `SHADOW_RANK_DELTA`: NONE (0 same-line BASELINE_P). `SHADOW_BASE_ONLY`: supplied rankings computed directly from BASE scenario: Under228.5 `0.636129`, Warriors−2.5 `0.574168`, Lakers+2.5 `0.425832`, Over228.5 `0.363871`; same top2, gate/floor FAIL. No shadow changes original primary ranks or scores.

### A6. Named adjustments, availability and unadjusted pair

| Input / proposed effect | Evidence and basis | Frozen numeric implementation | Major limitation |
|---|---|---|---|
| Neutral venue | Official T-Mobile Arena Las Vegas; LAL home-designated only | **0** automatic regular NBA home court | Designated home does not equal usual Crypto.com home advantage |
| Preseason games n4/n3 | Official NBA completed previous games | Raw opponent-average matchup 112.9167/110.375 | Small sample, non-homogeneous starter minutes/opponents |
| Dončić rested | Contemporary Lakers injury news R10 | **Analyst hypothesized −3.0 LAL pts** in base | NOT_ESTIMATED player-specific impact; source publication clock not independently verified |
| Walker Kessler return | Contemporary Lakers report, jammed finger | Included in same opaque LOW/BASE/HIGH rotation uncertainty; **no second point deduction** | No minutes/confirmed five or defense-on/off numeric impact |
| Curry increased time, Al Horford rested, Porziņģis absent | GSW preview R11–R12 | GSW **net-zero base** relative small preseason sample; stress in LOW/HIGH | Interacting player minutes cannot be identified independently |
| Travel/rest | GSW Oct10 latest, LAL Oct8 latest; Las Vegas neutral | 0 numeric effect, uncertain not assumed equal | No historical coefficients/finalized travel manifest |
| Pace, efficiency, opponent quality | No reconciled possessions for current 7 event cards | `SCORE_BASED_APPROXIMATION`; no ORtg/DRtg adjustment | No hidden pace estimate, no double count |
| Total/margin scoring widths | Published 2025–26 NBA regular profile σ≈20.04/15.98 as reference | widen to σ(T)=22, σ(M)=18 (**subjective**) | Preseason distribution not fitted |

**Unadjusted common-state check:** same three scenario widths/weights but **no LAL −3 base shift** gives Under228.5=0.559790, Lakers+2.5=0.519320, Warriors−2.5=0.480680, Over228.5=0.440210. Top two **Under / Lakers+2.5**, whereas submitted adjusted original top two **Under / Warriors−2.5**. The adjustment changes second pick by **only three assumed Lakers points**: `ADJUSTMENT_DEPENDENT=YES` by SF-2/current selection rules (even if magnitude <0.25 SD). Original adjusted estimates remain frozen; unadjusted comparator is NOT_PRIMARY and not a replacement.

### A7. Scenario / window sensitivity and no false certification

**Frozen scenario support:** low total Under=75.956%, GSW−2.5=53.034%; base Under=63.613%, GSW−2.5=57.417%; high total Under=40.639%, GSW−2.5=50.826%. Range Under **40.639%–75.956%**, Warriors spread **50.826%–57.417%**. Both are parameter sensitivities, *not* empirical CIs. High-total scenario's first pick Over228.5, low-total scenario's first pick Under228.5; **`INTENSITY_SCENARIO_SENSITIVE=YES`**.

**Historical-window sensitivity:** Full current-stage L5/10/15/20 cannot be formed at n4/n3; no supported league-season pooling or opponent-adjustment method. **`WINDOW_SENSITIVITY_NOT_COMPUTABLE: full 5/10/15/20 same-season comparators missing.`** Separately, diagnostic last **two** current games per side substituted into exact same score formula gives (`L2_DIAGNOSTIC_ONLY`, no retraining, not an issued recipe) Under=0.565352, Warriors−2.5=0.610636; then **top two reverse** to Warriors−2.5 / Under228.5. Do not promote the two-game hot-streak model into original selection: an L2 source window is not a statistically meaningful proxy for L20. Form cohort blocks 6–10,11–15,16–20 unavailable; supplementary 2025–26 REGULAR L20 scores not modelled as if they were 2026 preseason possessions. `FORM_WINDOW_SENSITIVE_DIAGNOSTIC=YES` (only partial current-season alternative).

**Family/endpoint sensitivity:** Under line is >-6.374 total-point offset from the model's expected total, normalized line distance `(228.5−222.126)/23.624=0.270`; spread threshold margin `(2.5−4.292)/18.063=-0.099`. Endpoints are **regular 48 + standard 5-minute OT**, not no-OT regulation. A surprise confirmed active lineup, early hook, 3-point hot shooting, or 4Q bench run could invalidate the estimated centre. No claim of calibrated 60% accuracy.

### A8. Sources, settlement field capture and open tasks

**Retrieval policy:** all source reads occurred in this live research run around `2026-10-14T13:14:34+11:00`. Many NBA official previous-game scores were definitively published **before** Oct14 since dated Oct4–10; independent exact page-update timestamps not retained. Same-day previews/articles describe *pregame* states but publish time (hour) not verified; treat any late-updated official box as potentially outcome-bearing and do NOT import live data into the frozen distribution. URLs and concrete sourced fields:

| ID | Field/route | Exact source URL | Field / limitation |
|---|---|---|---|
| R01 | NBA 2026 fixture/game ID and venue | https://www.nba.com/game/0012600048 | Preseason; GSW @ LAL; T-Mobile Arena Las Vegas; 13 Oct 2026 10PM ET/7PM PDT (14 Oct 13:00 AEDT); pregame listing. Retrieval after listed start; only the fixture page pregame state was used. |
| R02 | Lakers official club schedule | https://www.nba.com/lakers/schedule | 13 Oct home-designated versus Warriors; venue T-Mobile Arena; neutral site. |
| R03 | Warriors official club schedule | https://www.nba.com/warriors/schedule | 13 Oct 7PM PDT Las Vegas vs Lakers; no season record inferred from unpublished statistics. |
| R04 | NBA official GSW @ Clippers Oct 4 | https://www.nba.com/game/gsw-vs-lac-0012600066 | GSW 101 LAC 104; completed 4 Oct. |
| R05 | NBA official Lakers @ GSW Oct 6 | https://www.nba.com/game/lal-vs-gsw-0012600010 | LAL 98 GSW 124; completed 6 Oct. |
| R06 | NBA official GSW @ Portland Oct 7 | https://www.nba.com/game/gsw-vs-por-0012600033 | GSW 118 POR 123; completed 7 Oct. |
| R07 | NBA official SAC @ GSW Oct 10 | https://www.nba.com/game/0012600014 | SAC 106 GSW 111; completed 10 Oct. |
| R08 | NBA official LAL @ SAC Oct 5 | https://www.nba.com/game/0012600028 | LAL 127 SAC 103; completed 5 Oct. |
| R09 | NBA official SAC @ LAL Oct 8 | https://www.nba.com/game/sac-vs-lal-0012600036 | SAC 110 LAL 114; completed 8 Oct. |
| R10 | Pre-game Lakers injury update | https://www.silverscreenandroll.com/lakers-injury-report/127269/lakers-injury-report-walker-kessler-luka-doncic-collin-sexton | Reports Dončić resting (not injury) and Walker Kessler expected preseason debut; Sexton, Thiero, Ziaire Williams, Cameron Carr also unavailable; report is contemporary but exact publish clock UNKNOWN. |
| R11 | Warriors rotation preview | https://www.sfchronicle.com/sports/warriors/article/kerr-leaning-toward-small-ball-warriors-22474023.php | Curry–Podziemski–Santos–Lendeborg–Green proposed small-ball configuration; Horford rested; Porziņģis absent. Proposed does not equal officially confirmed matchday starters. |
| R12 | Golden State local contemporary preview | https://www.goldenstateofmind.com/warriors-game-previews/112590/how-to-watch-warriors-vs-lakers | Warriors 2–2 preseason after 111–106 SAC; team lineup projected; source-level overlap with NBA owner likely. |
| R13 | Official NBA 2025–26 playing rules PDF | https://cdn.nba.com/manage/2026/01/Official-2025-26-NBA-Playing-Rules.pdf | 12-minute regulation quarters and 5-minute OT; 2026–27 special matchup exceptions not identified. |
| R14 | Pinned 2025–26 NBA archive | https://github.com/danisgreat/Sports-Research/blob/e73c9c24e418250f8816932facc5feeecd94ef5d/Previous%20Sports%20Results/Basketball/NBA/2025/2025_games.csv | 1,325 logical rows; 1,230 regular season; ZERO preseason rows; previous-season team L20 trace only; not a preseason same-line baseline. |
| R15 | Pinned methods/status | https://github.com/danisgreat/Sports-Research/blob/e73c9c24e418250f8816932facc5feeecd94ef5d/CURRENT_STATE.md | Current published v11; next canonical P-585, highest imported P-584, local mini working P-588 conditional. |

**Required later sporting fields (no settlement now):** official final NBA game `0012600048`: actual tipoff, exact final and regulation quarters Q1–Q4, each OT points and number of OTs, winner, final score GSW and LAL; starters in official box plus minutes, every active bench/substitute, DNP/inactive statuses and injury updates with publication times; possessions/pacing and advanced box if available; venue-state, cancellation/abandonment, exact definitions; then freeze each original supplied row's sporting WIN/LOSS/PUSH/VOID/UNRESOLVED under original framework and obtain operator's written settlement/void rules before operator-specific certification. Never use a postgame box to repair the original pregame probability. Suggested review within 72h of verified final, **MANUAL ONLY / NO AUTOMATION SCHEDULED**; actual final time currently not verified.

**Unresolved evidence:** (1) official game-day 5+bench inactives and minutes; (2) exact publication clock for Dončić rest and Kessler availability; (3) valid preseason league-only comparator to freeze for future games; (4) possession/ORtg/DRtg and opponent quality measures with denominators; (5) external local mini and full Combined-7 literal body check; (6) operator action/void clauses; (7) actual tipoff status/timing and eventual final source. All unconfirmed values remain missing, never silently zero or excluded from denominator.

`SETTLEMENT=NOT_PERFORMED` · `CANONICAL_IMPORT=NOT_PERFORMED` · `GITHUB_WRITES=NO` · `CANONICAL_IDS_CONSUMED=0`.

### A9. Actual integrity self-audit — C1–C20, FR1–FR6, SF-A1–SF-A12, Q4

**C1–C20 (mini-log-7):** C1 PASS published e73… pinned, all required controls fetched, relevant sections read, SF-2 deviation noted. C2 PARTIAL native game ID distinct from Oct6; current mini and GitHub search examined, canonical massive Part7 literal body and external hidden minis unverified. C3 PASS 4 unique supplied candidates, deterministic descending numeric. C4 PASS all W/P/L/V conditional sums1, exact half-point complements, OT treated as a state transition. C5 PASS supplied-only competitor/lead/floor and precision, RET03 named shadow. C6 PASS rank2 floor failure, exact common-state joint0.180551; no mechanical guarantee. C7 PASS low/base/high sensitivity, no-adjustment top-two flip explicit. C8 PARTIAL same-stage form used, one unmeasured −3 point assumption identified, no hidden venue shift. C9 PARTIAL NBA preseason 4×12 and standard overtime supported; 2026 event special override unverified, OT Poisson approximation not fitted. C10 PARTIAL exact sporting definitions/capture plan, operator terms missing, no job scheduled. C11 PASS honest late start and separately timed source/issue states; actual tipoff unknown, no pregame grade. C12 PARTIAL past scores owner backed and market-blind; media injury/lineup lineage/timestamps unknown. C13 PARTIAL inspected archive stage and 1,325 logical rows; no complete same-season L5/L10/L15/L20 or authoritative possession dataset. C14 PASS explicit stage-incompatible baseline attempts, no fabricated comparator (0/4). C15 PASS expected points and SD identities, covariance and signed orientation from executed grid. C16 PASS only **upon actual write/readback verification** below. C17 PARTIAL reported n4/n3 in all windows, supplemental 2025–26 REGULAR n20, shrink unavailable (no LM), diagnostic L2 changes ordering. C18 PASS exact-line zero pushes, offsets/z distances, baseline 0/4/0/2 and missingness. C19 PASS mixed unconditional state masses with 0.25/0.50/0.25, per-row `p_base`, separate unadjusted and shadows. C20 PASS **only after actual prewrite writer/lease/freeze/ID/intake/footer check and local readback**.

**FR1–FR6:** FR1 PARTIAL n4 GSW/n3 LAL current preseason with no more; previous REGULAR L20 traced separately. FR2 PASS 2026 exhibition separated from 2025–26 regular, no illegal pooling. FR3 PARTIAL native IDs/dates/opponents/scores for all 7 current and 40 supplementary games; advanced stat numerator/denominator and publication clock missing. FR4 PARTIAL no supported preseason same-stage LM or shrink, 2-game diagnostic window sensitivity executed. FR5 PARTIAL named players and probable/absence groups, both official starting-five-plus-bench lists unavailable; named scenario weights subjective. FR6 PARTIAL complete event trace and separately named missingness, no false fitting or validation claims.

**SF-A1–SF-A12:** A1 PASS four raw→four unique resolved keys. A2 PARTIAL orientation and full-game definitions explicit, operator void terms absent. A3 PASS four contracts priced by executed one distribution conditional completed event. A4 PASS unrounded deterministic complete descending ranking. A5 PASS both top-two literally supplied. A6 PARTIAL ceiling and rules applied, unknown operator-specific action/lineup verification disclosed. A7 PASS supplied-gate exact alternative/gap ε, p/floor states. A8 PASS actual common-state joint, reciprocal pairs identified. A9 PASS all optional shadows declared NOT_PRIMARY or NOT_COMPUTED. A10 PASS issue-time state model/parameters/masses/times/known-at gaps preserved. A11 PARTIAL late and date-stamped sourcing, actual tipoff and some publication times unknown, never prospective. A12 PASS only when actual prewrite and physical readback plus earlier block byte-identity checks succeed.

**Q4 calculation receipt:** local scratch `p588_calc.py` executed, scenario weights sum 1, all W/P/L/V valid conditional completed, all four supplied rows represented, extreme-regulation tails at 0..210 cut off and normalised; repeated OT truncated after 7 ties residual 2.14e−8 conditional OT; paired complements sum to one to float tolerance, final winner masses to one, expected-score/covariance identities verified, no p outside [0,1], no 90% exclusion, exact joint from same conditional final-score support (not p1×p2). **Any real game model misspecification remains an epistemic, not numerical, error.** Structural readback & frozen prior-original byte hashes will be recorded in receipt after the actual write.
<!-- END CARD P-588 -->

# RUNNING FOOTER

<!-- BEGIN CARD P-589 -->
## Card · P-589 · ICE HOCKEY / NHL 2026–27 regular season · Boston Bruins @ San Jose Sharks · 2026-10-13 PDT / 2026-10-14 AEDT

- **Working custody:** `P-589` / `LOCAL_UNIMPORTED` / `ISSUED_LOCAL` upon successful write/readback; event key `NHL:2026-27:REG:2026020105:BOS@SJS:2026-10-13`; native NHL game ID `2026020105`; no distinct matching card in the active local mini or indexed published main. Full remote Part 7 body search/index not independently exhaustively verified; ID/duplicate check has that limitation. New canonical IDs **0**.
- **Pinned authority:** `PUBLISHED_MAIN_PINNED 7640f9d10ef3c05eca4ea657de8b9554d446b635` read on 2026-10-14 AEDT, `MDS-2026.10.12-v11.0` / `CR-2026.10.12-R2` / `SEL-2026.10.12-v3 P_ORDER_V2` / `SCV-2026.10.12-v7`, `mini-log-7`. Explicit local selection-scope override `SUPPLIED_FIRST_V1 / SF-2`: **only the four literally supplied contracts** are formally ranked; generated/unfrozen ladders do not enter primary. Prior minis/cards remain under original pinned versions. GitHub READ-ONLY.
- **Timing:** The user estimated 2026-10-14 **14:07 AEDT**. League/team public fixture says **Tuesday 2026-10-13 20:00 PDT / 23:00 EDT = Wednesday 2026-10-14 03:00 UTC / 14:00 AEDT**, SAP Center at San Jose. Received by first observed local research time around `2026-10-14T14:04:00+11:00` (exact receipt clock NOT_VERIFIED); research/cutoff `2026-10-14T14:17:28+11:00` and final-state recheck separately recorded in receipt below. Official scheduled start already passed: `LATE_START_UNVERIFIED`, actual first puck `NOT_VERIFIED`; `OUTCOME_EXPOSURE=NONE_OBSERVED` (no in-game/final game information intentionally used). Late research is NOT a verified pregame cohort. Prior completed game outcomes used only through **2026-10-10**; pregame projected lineup issued Oct13 by NHL and read in this run, exact original publication minute not verified.
- **Playing rule/conditioning:** NHL regular 3×20min regulation, up to 5min 3-on-3 sudden-death OT, then shootout; no final full-game draw. For normal completed NHL official final scores, one deciding goal is credited on OT/SO resolution of a regulation tie (but a shootout is not a regulation goal). User ML is **full game including OT/SO**; Over/Under 6.5 is credited final total including actual empty-net and the credited OT/SO game-winner. On completed NHL scores the four half-point/two-way actions have zero PUSH. Unknown bookmaker void/shortened/postponed conditions labelled `UNKNOWN_DEFINITION`; the model is conditional on normal completion, not an unconditional all-event forecast.
- **Research status:** `UNCALIBRATED_ANALYST_SCENARIO`, `RESEARCH_ONLY_NOT_CERTIFIED`, `LINEUP_GATE=PARTIALLY_CONFIRMED` at most (NHL published *projected* lines and expected goalies, but final starters and scratches NOT_VERIFIED). No fitted model, proven independent source collectors or calibration. Player minutes/verified 5v5 xG and high-danger splits not fully available. Boston 4–2–0, San Jose 3–2–0 entering this game.
- **Expected official full game (score-distribution moments, with SO credit):** BOS **3.329**, SJS **2.778**; total **6.107 ± 2.507 SD**; signed margin BOS−SJS **+0.551 ± 2.366 SD**; score covariance **0.171938**, score correlation `NOT_REPORTED` (covariance is computed; reconstruct score variances from total/margin if needed). Model full-game winning mass BOS=59.3080%, SJS=40.6920%; regulation draw=24.8476%; OT resolves=15.7774%; SO resolves=9.0701%. No full-game tie.
- **Frozen user universe:** 4 literal inputs / 4 distinct resolved contract keys `P589_NHL_2026020105_SF2_v1`. No unused option placeholder priced, no generated primary lines. `BASELINE_LEAGUE_V1` empirical 2025–26 league population **4/4 supplied** / **2/2 formal** (exact actions and thresholds; historical cohort n=1,312; prior to Oct14).

### Decision — original supplied-only ranking

| Supplied rank | Literal contract | `p_card` decisive | Conditional W/P/L/V (decisive/push) | `p_base` | `BASELINE_P` | Eligibility / role |
|---:|---|---:|---|---:|---:|---|
| 1 | `Bruins ML` | **59.3080%** | `0.593079645 / 0 / 0.406920355 / 0` | 58.7815% | 47.7896% | ELIGIBLE / PICK / PRIMARY |
| 2 | `Combined Total Goals: Under 6.5 Goals` | **56.2676%** | `0.562675614 / 0 / 0.437324386 / 0` | 56.4775% | 53.1250% | ELIGIBLE / PICK / PRIMARY |
| 3 | `Combined Total Goals: Over 6.5 Goals` | **43.7324%** | `0.437324386 / 0 / 0.562675614 / 0` | 43.5225% | 46.8750% | ELIGIBLE / INFORMATIONAL |
| 4 | `Sharks ML` | **40.6920%** | `0.406920355 / 0 / 0.593079645 / 0` | 41.2185% | 52.2104% | ELIGIBLE / INFORMATIONAL |


**Formal Rank 1:** Bruins ML **59.3080%**, model-favoured full-game winner. **Rank 2:** Under 6.5 **56.2676%**. Third is Over 6.5, fourth Sharks ML; all four retained. The two sides within each family are mutually complementary on normally completed two-way NHL outcomes; original *top two* are **not mechanically protected**.

**`SUPPLIED_SCOPE_GATE=RANK1_UNSTABLE`:** Rank-1 59.3080% below 62.00% requirement; best eligible non-complementary alternative = Under6.5 56.2676%, lead **3.0404 percentage points**, below 4.00 pp. Rank-2 56.2676% below 58.00% floor. Eligibility unaffected; gates are diagnostics, **not** threshold-optimised selections. Calculated double-precision numerical error negligible (<1e-9 mass), pre-match parameter/model error unknown and substantially larger. `SHADOW_MAIN_POLICY_GATE=NOT_COMPUTED` without full universe.

**Pair dependence:** `P(both original primary picks lose)` = **17.8282%**, counted from the same credited final-score states where **San Jose wins AND final goals≥7**. `P(at least one wins)` = 82.1718%; `P(both decisive)` = 1 conditional on complete game; independent-products shortcut NOT_USED. Joint warning threshold 0.35 not exceeded. No claim of demonstrated skill or profit.

### A1. Reading receipt, event identity and source hierarchy

```text
READING RECEIPT
Authority mode: PUBLISHED_MAIN_PINNED
Repository: https://github.com/danisgreat/Sports-Research  main
Verified full commit SHA: 7640f9d10ef3c05eca4ea657de8b9554d446b635
Timestamp: 2026-10-14T14:17:28+11:00 Australia/Melbourne
Current versions: MDS-2026.10.12-v11.0; CR-2026.10.12-R2; SEL-2026.10.12-v3; SCV-2026.10.12-v7
Template/settlement: mini-log-7 / mini-settlement-6
Prompt revision SF-2; selection deviation SUPPLIED_FIRST_V1, not the published full-universe P_ORDER_V2
Read in full via connected pinned GitHub: README.md, CURRENT_STATE.md, METHOD.md, CURRENT_RULES.md,
 SELECTION_RULES.md, CARD_AND_LOG_TEMPLATES.md, SCORING_AND_VALIDATION.md,
 PROBABILITY_TOOLKIT.md, VERIFICATION_PROTOCOL.md, RULES_ICE_HOCKEY.md,
 RULES_NHL.md, LEAGUE_PROFILES.md, ARCHIVE_USE_GUIDE.md,
 BASE_RATES_REGISTER.md, SOURCES.md, research/prompts/README.md,
 research/prompts/1_GAME_CARD.md, GAME_LOG_STATUS_CURRENT.md;
 full local active mini as existing input. Source-file contents retrieved at same full SHA.
Specific current sections: NHL rule/goalie/OT §§0–2; SOURCES §3.9 NHL; NHL profile;
 archive R2 and §8; baseline §§7.2; 2025 NHL actual CSV 1,498 records incl 1,312 regular.
Last official known results: 2026-10-10; official starting goalie confirmation unavailable.
Current main canonical: highest imported P-584; next canonical P-585; Part7 active.
Local cards P-585..P-588 already issued; proposed P-589 local only.
Current local writer ChatGPT this conversation, lease expires 2026-10-14 15:55:33 AEDT,
 mini ACTIVE, freeze NO, no handover. Publishing/mutating GitHub prohibited.
Live/actual first-puck state NOT_VERIFIED; lineage independence NOT_VERIFIED.
```

**Identity and duplicate search:** NHL `2026020105` at SAP Center / San Jose, Tuesday Oct13 20:00 PDT. 2026–27 NHL regular season. The current mini's full text and its four issued P-585..P-588 cards were inspected; none matches this game. Connected GitHub main text searches for native ID and both team names returned zero indexed matches; this is not proof of an exhaustive byte scan of large canonical Part 7; concurrent user-machine mini availability UNKNOWN. No P-ID renumbering or canonical allocation.

### A2. Frozen literal contract manifest and actions

| Raw index | Exact supplied text | Frozen resolved key (orientation / quantity / line / endpoint) | Action |
|---:|---|---|---|
| 1 | `Bruins ML` | `2026020105:BOS:WIN:FULL_OT_SO:0` | W if BOS wins; L if SJS wins |
| 2 | `Sharks ML` | `2026020105:SJS:WIN:FULL_OT_SO:0` | W if SJS wins; L if BOS wins |
| 3 | `Combined Total Goals: Over 6.5 Goals` | `2026020105:TOTAL:OVER:6.5:FULL_CREDITED` | W total≥7; L total≤6 |
| 4 | `Combined Total Goals: Under 6.5 Goals` | `2026020105:TOTAL:UNDER:6.5:FULL_CREDITED` | W total≤6; L total≥7 |

Original order preserved; rank permutation uses unrounded p. Operator-specific early-abandonment/void rules `UNKNOWN_DEFINITION`; normal completed full-game NHL `FROZEN_FRAMEWORK_CONVENTION`. No observed/assumed 0% risk of real-world cancellation/abandonment; W/P/L/V values condition on a normal completed NHL game. Complete-game 0 P and 0 V are *conditional*, not operator-all-event claims. `SUPPLIED_UNIVERSE_ID=P589_NHL_2026020105_SF2_v1`; candidate keys remain issue-time research records, not automatically qualified ML training examples.

### A3. Team evidence, four form windows and confirmed-versus-projected goalies

**Current 2026–27 NHL regular-season results as known before research** (latest-first; source: official league previews, club recaps, Hockey-Reference, NHL gamecenter, event completion dates all before Oct13). A shootout/OT win is one extra final goal, not a scored regulation goal. NHL official score's SO winner credit retained in final field.

#### Boston Bruins — 2026–27 same-season form

| Window | Eligible n / target | W–L | Regulation GF / GA per game | Final GF / GA per game | Evidence / limitation |
|---|---:|---:|---:|---:|---|
| L5 | 5/5 | 3–2 | 3.200 / 2.600 | 3.400 / 2.600 | full window |
| L10 | 6/10 | 4–2 | 3.167 / 2.167 | 3.333 / 2.167 | PARTIAL; no earlier 2026–27 games |
| L15 | 6/15 | 4–2 | 3.167 / 2.167 | 3.333 / 2.167 | PARTIAL; no earlier 2026–27 games |
| L20 | 6/20 | 4–2 | 3.167 / 2.167 | 3.333 / 2.167 | PARTIAL; no earlier 2026–27 games |
| Season to cutoff | 6/6 | 4–2 | 3.167 / 2.167 | 3.333 / 2.167 | completed before 13 Oct |


#### San Jose Sharks — 2026–27 same-season form

| Window | Eligible n / target | W–L | Regulation GF / GA per game | Final GF / GA per game | Evidence / limitation |
|---|---:|---:|---:|---:|---|
| L5 | 5/5 | 3–2 | 2.000 / 3.400 | 2.600 / 3.400 | full window |
| L10 | 5/10 | 3–2 | 2.000 / 3.400 | 2.600 / 3.400 | PARTIAL; no earlier 2026–27 games |
| L15 | 5/15 | 3–2 | 2.000 / 3.400 | 2.600 / 3.400 | PARTIAL; no earlier 2026–27 games |
| L20 | 5/20 | 3–2 | 2.000 / 3.400 | 2.600 / 3.400 | PARTIAL; no earlier 2026–27 games |
| Season to cutoff | 5/5 | 3–2 | 2.000 / 3.400 | 2.600 / 3.400 | completed before 13 Oct |


**Current event-level trace (latest first, actual start/end clocks absent, dates are safely earlier):**

| Team | Completed date / native ID status | Opponent (H/A) | Final GF–GA | Reg GF–GA | Decision | Known-at note |
|---|---|---|---|---|---|---|
| BOS | 2026-10-10 / NHL ID not separately captured | PHI (H) | 5–1 | 5–1 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| BOS | 2026-10-08 / NHL ID not separately captured | UTA (H) | 6–1 | 6–1 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| BOS | 2026-10-05 / NHL ID not separately captured | OTT (H) | 1–4 | 1–4 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| BOS | 2026-10-03 / NHL ID not separately captured | MIN (A) | 1–4 | 1–4 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| BOS | 2026-10-02 / NHL ID not separately captured | WPG (A) | 4–3 | 3–3 | OT | Completed by prior date, contemporaneous NHL/hockey-reference results |
| BOS | 2026-09-29 / NHL ID not separately captured | NYR (H) | 3–0 | 3–0 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| SJS | 2026-10-10 / NHL ID not separately captured | EDM (H) | 1–3 | 1–3 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| SJS | 2026-10-08 / NHL ID not separately captured | STL (A) | 3–2 | 2–2 | OT | Completed by prior date, contemporaneous NHL/hockey-reference results |
| SJS | 2026-10-05 / NHL ID not separately captured | DAL (A) | 0–5 | 0–5 | REG | Completed by prior date, contemporaneous NHL/hockey-reference results |
| SJS | 2026-10-03 / NHL ID not separately captured | LAK (H) | 5–4 | 4–4 | OT | Completed by prior date, contemporaneous NHL/hockey-reference results |
| SJS | 2026-10-01 / NHL ID not separately captured | FLA (H) | 4–3 | 3–3 | OT | Completed by prior date, contemporaneous NHL/hockey-reference results |

**2025–26 NHL archive (pinned previous-season `2025_games.csv`, reg season 1,312 of 1,498 total rows):** supplementary previous-season L5/10/15/20 windows; these are not 2026–27 games and cannot be silently called current-form L20. The previous season's original NHL ID/date/venue/final/OT/SO field trace is below, oldest regime kept separately. Zero applicable xG/high-danger data fields in this scoring-result archive; no fabricated xG.

#### Boston Bruins — supplementary 2025–26 season ending April 2026 (not pooled as current-year L20)

| Prior-season window | n | W–L; regulation GF/GA (per game) |
|---|---:|---|
| Prior L5 | 5 | 2–3; reg 14/10 (2.80/2.00) |
| Prior L10 | 10 | 5–5; reg 31/24 (3.10/2.40) |
| Prior L15 | 15 | 8–7; reg 48/36 (3.20/2.40) |
| Prior L20 | 20 | 10–10; reg 60/50 (3.00/2.50) |

| Date / NHL game ID | Opponent | H/A | Credited final | Endpoint |
|---|---|---|---|---|
| 2026-04-14 / `2025021292` | NJD | H | 4–0 | REG |
| 2026-04-12 / `2025021278` | CBJ | A | 3–2 | REG |
| 2026-04-11 / `2025021261` | TBL | H | 1–2 | REG |
| 2026-04-07 / `2025021237` | CAR | A | 5–6 | OT |
| 2026-04-05 / `2025021224` | PHI | A | 1–2 | OT |
| 2026-04-04 / `2025021210` | TBL | A | 1–3 | REG |
| 2026-04-02 / `2025021193` | FLA | A | 1–2 | REG |
| 2026-03-31 / `2025021178` | DAL | H | 6–3 | REG |
| 2026-03-29 / `2025021170` | CBJ | A | 4–3 | SO |
| 2026-03-28 / `2025021155` | MIN | H | 6–3 | REG |
| 2026-03-25 / `2025021135` | BUF | A | 4–3 | OT |
| 2026-03-24 / `2025021120` | TOR | H | 2–4 | REG |
| 2026-03-21 / `2025021108` | DET | A | 4–2 | REG |
| 2026-03-19 / `2025021083` | WPG | H | 6–1 | REG |
| 2026-03-17 / `2025021069` | MTL | A | 2–3 | OT |
| 2026-03-16 / `2025021064` | NJD | A | 3–4 | OT |
| 2026-03-14 / `2025021044` | WSH | A | 3–2 | SO |
| 2026-03-12 / `2025021027` | SJS | H | 2–4 | REG |
| 2026-03-10 / `2025021012` | LAK | H | 2–1 | OT |
| 2026-03-08 / `2025021002` | PIT | A | 4–5 | OT |

#### San Jose Sharks — supplementary 2025–26 season ending April 2026 (not pooled as current-year L20)

| Prior-season window | n | W–L; regulation GF/GA (per game) |
|---|---:|---|
| Prior L5 | 5 | 2–3; reg 15/17 (3.00/3.40) |
| Prior L10 | 10 | 5–5; reg 31/34 (3.10/3.40) |
| Prior L15 | 15 | 7–8; reg 44/51 (2.93/3.40) |
| Prior L20 | 20 | 9–11; reg 59/72 (2.95/3.60) |

| Date / NHL game ID | Opponent | H/A | Credited final | Endpoint |
|---|---|---|---|---|
| 2026-04-16 / `2025021308` | WPG | A | 6–1 | REG |
| 2026-04-15 / `2025021305` | CHI | A | 2–5 | REG |
| 2026-04-13 / `2025021287` | NSH | A | 3–2 | REG |
| 2026-04-11 / `2025021275` | VAN | H | 3–4 | SO |
| 2026-04-09 / `2025021258` | ANA | A | 1–6 | REG |
| 2026-04-08 / `2025021246` | EDM | H | 2–5 | REG |
| 2026-04-06 / `2025021231` | CHI | H | 3–2 | REG |
| 2026-04-04 / `2025021220` | NSH | H | 3–6 | REG |
| 2026-04-02 / `2025021202` | TOR | H | 4–1 | REG |
| 2026-04-01 / `2025021190` | ANA | H | 4–3 | REG |
| 2026-03-30 / `2025021177` | STL | H | 5–4 | REG |
| 2026-03-28 / `2025021158` | CBJ | A | 3–2 | REG |
| 2026-03-26 / `2025021143` | STL | A | 1–2 | OT |
| 2026-03-24 / `2025021129` | NSH | A | 3–6 | REG |
| 2026-03-21 / `2025021103` | PHI | H | 1–4 | REG |
| 2026-03-19 / `2025021092` | BUF | H | 0–5 | REG |
| 2026-03-17 / `2025021073` | EDM | A | 3–5 | REG |
| 2026-03-15 / `2025021058` | OTT | A | 4–7 | REG |
| 2026-03-14 / `2025021048` | MTL | A | 4–2 | REG |
| 2026-03-12 / `2025021027` | BOS | A | 4–2 | REG |

**Nonoverlapping blocks / window trends:** Current Boston last five final 17–13; the sixth (Sep29 NYR 3–0) produces season 20–13, so its strongest incremental change is the opening shutout. Current San Jose L5 is its complete n5 season, final 13–17; all **three** wins required OT, not three regulation wins. Prior-season L1–5/L6–10/L11–15/L16–20 use the 20 exact dated rows above; these overlapping L5/10/15/20 summaries are one evidence family, not four independent likelihood ratios. Opponent-strength adjustment `OPPONENT_ADJUSTMENT_UNAVAILABLE`; full xG/5v5 chance, travel minutes, shots by all 2025–26 games: NOT_RECONCILED.

**On-ice/availability:** Official NHL Sharks pregame note lists (PROJECTED, NOT CONFIRMED) Bruins forwards Geekie–Zacha–Pastrnak / Khusnutdinov–Minten–Peterka / Mittelstadt–E. Lindholm–Hagens / Jeannot–Poitras–Kastelic; defenders H. Lindholm–McAvoy / Zadorov–Borgen / Brunet–Lohrei; goalies Swayman, DiPietro. Projected SJ top line duplicates Igor Chernyshov in two positions (source typo): **do not treat a duplicated player as two skaters**; a secondary preview projects Chernyshov–Celebrini–Will Smith, but official final top line remains NOT_CONFIRMED. Remaining Sharks expected Stenberg–Misa–Sherwood / Marchment–Wennberg–Toffoli / Goodrow–Ostapchuk–Graf; defensive pairs Nurse–Kesselring / Dickinson–Trouba / Orlov–Cagnoni. Official report says McAvoy returns after six-game suspension, Goodrow available despite illness; scratches provisional. No authenticated final game sheet for starter, backup and all active/scratches.

**Goalie histories and replacement availability:** projected Swayman (BOS) current **5 starts** through Oct10, 4–1, 124 SV/133 SA = .932, GAA ~1.79; DiPietro 1 start, 26/29=.897. Projected Askarov (SJS) current **4 starts**, 2–2, SV% ~.860, GAA ~3.71; Nedeljkovic one start, SV%~.923. Goalie start L5 coverage Swayman 5/5, Askarov 4/5; goalie L10/L15/L20 eligible-start trace and 2025 starts NOT_RETRIEVED, do not pad. These short goalie form fields are not an independent fourth/separate confirmation of team GA, nor confirmed starting-goalie evidence. No empirically justified isolated goalie conversion-to-goals coefficient; numeric stress is a subjective sensitivity only.

**Shots/special teams with denominators:** BOS 2026 season ~153 SOG/6 and 163 shots faced/6; PP **3/16 = 18.75%**, PK **17/21 = 80.95%**. SJ season 13 GF, 17 GA; shots ~23.4 for and 26.6 against per game; PP **2/13 = 15.38%**, PK **13/16 = 81.25%** (rounded values inferred from 15.4%/81.3% and reported success counts; opportunity denominators to be independently reconciled against official event sheets before using a goal adjustment). Thus: use no separate numerical special-team coefficient, preventing double counting; 5v5/xG/high-danger independently validated numeric rates unavailable. Travel/rest: both last completed Oct10; Boston starting a west-coast road trip, San Jose at home, no fitted effect assumed.

### A4. Reproducible coherent distribution and expected-score arithmetic

**Model `P589_NHL_DIAGONAL_TIE_POISSON_MIX1` / code:** a locally executed scratch Python script `/mnt/data/p589_calc.py` (outside GitHub; arithmetic reproduced here) enumerated regulation score pairs `(B,S)∈{{0..25}}²`; regulation independent Poisson with scenario `(λ_B,λ_S)`, then a *shared-state* empirical league regulation-tie correction (no unverified claim of fitted strength); on diagonal apply OT then SO decision, with exactly one deciding credited final goal. Numerical raw Poisson tail below 3×10⁻¹⁴ per scenario. All W/P/L/V derived from that shared credited-final-score distribution; after weighting the mixture, mass is 1.0000000000.

**Regulation rates, one longer-window shrinkage (prior-season L20 kept as 20 equivalent prior games, not 20 new current games):**
- Boston 2026 six regulation GF/GA **19/13**; previous L20 **60/50**. Attack `(19+60)/(6+20)={b['BOS_attack']:.6f}`, defence `(13+50)/26={b['BOS_defence']:.6f}` goals/game.
- San Jose 2026 five regulation GF/GA **10/17**; previous L20 **59/72**. Attack `(10+59)/(5+20)={b['SJS_attack']:.6f}`, defence `(17+72)/25={b['SJS_defence']:.6f}`.
- The explicit choice of 20 prior pseudo-games is an **analyst prior**, not a fitted or validated k, and the roster has changed across seasons; do not call this pinned R2 season-only shrinkage. The registered R2 k=2 league-shrinkage is separately left `NOT_COMPUTED` as a complete alternative due to noncomparability of prior season and current n6/n5; exact current season n shown above. Published 2025–26 league regulation home/away mean approx 3.0701/2.9352, empirical home scoring increment `(3.0701−2.9352)/2={b['home_reg_edge_half']:.6f}`.
- Base BOS λ `((BOS_attack+SJS_defence)/2)−league_half_home_edge` = **{b['BOS_reg_lambda']:.9f}**; base SJS λ `((SJS_attack+BOS_defence)/2)+league_half_home_edge` = **{b['SJS_reg_lambda']:.9f}**. Not a fitted 5v5 shot-quality/powerplay/empty-net process. Named +/- goals are *uncalibrated* goalie/finishing/empty-net uncertainty rather than measured individual player effects.

**Frozen low/base/high lineup+goalie+finishing scenario mixtures, weighting .25/.50/.25 before ranking:**

| Scenario | Weight | BOS regulation λ | SJS regulation λ | Interpretation (subjective) | BOS ML | Under 6.5 | Expected full game total |
|---|---:|---:|---:|---|---:|---:|---:|
| LOW | 0.25 | 2.931777 | 2.108993 | Strong goaltending/finishing suppression; projected starters | 63.7830% | 70.5945% | 5.2338 |
| BASE | 0.50 | 3.231777 | 2.658993 | Shrunk form matchup; both projected starters | 58.7815% | 56.4775% | 6.0832 |
| HIGH | 0.25 | 3.631777 | 3.208993 | Goalie/finishing variance and empty-net high-tail proxy; starter status not established | 55.8859% | 41.5207% | 7.0293 |


**Regulation draw/OT/SO transition:** Raw independent-score diagonal mass differs by scenario; to incorporate historic NHL 2025–26 326 OT/SO decisions in n=1,312 regular games, multiply all regulation `(g,g)` cells by scenario-specific `k = [t/(1−t)]·[(1−d₀)/d₀]`, where `t=326/1312=0.248475610` and `d₀` is raw diagonal mass; renormalise *all cells*. Correction factors LOW/BASE/HIGH 1.591230 / 1.684738 / 1.820140; diagonal regulation mass 24.8476% per scenario by design. Within regulation ties, 2025–26 historic OT decided 207/326 = 0.634969325; otherwise 119/326 shootout. OT first-goal side share approximated by λ_B/(λ_B+λ_S); shootout BOS 47.8% from 2023–25 league SO home share 52.2%. On either OT or SO outcome, **one** deciding goal is credited to the winner and not counted as regulation production. This is a coarse historic endpoint transition, not an NHL-exact 3v3 simulator or goalie-specific SO model. Historical regulation-tie correction (as opposed to raw Poisson) can affect total probabilities; applied to shared state, not to any one proposition independently.

**Modelled mixture:** BOS E=3.328995; SJ E=2.778403; total E=6.107398, SD=2.506861; margin BOS−SJ E=+0.550593, SD=2.365713; Cov(B,S)=0.171938. Score moments use `Var(T)=Var(B)+Var(S)+2Cov` / `Var(M)=Var(B)+Var(S)−2Cov` and exact scenario mixture variance `∑w_s(σ_s²+(μ_s−μ_mix)²)`; not an average of SDs. Model regulation draw 24.8476%, full-game draw=0; mass numerical tolerance 1e−10. Standard model is conditional on a *completed* game; cancellation/void probability NOT_ESTIMATED.

**Goalie replacement / form-choice stress (not primary, all other inputs held constant; subjective perturbations NOT confirmed start probabilities):**

| Alternative | BOS ML | Under 6.5 | Expected total | Effect on ordering |
|---|---:|---:|---:|---|
| If Swayman sits, SJS expected goals +0.60 | 49.3937% | 46.7541% | 6.684 | Over6.5 / SJS ML |
| If SJ goalie switches to stronger-saving backup, BOS λ −0.35 | 53.4647% | 62.1330% | 5.741 | Under6.5 / BOS ML |
| Both netminder/finishing threats up: BOS +0.35, SJ +0.60 | 54.4572% | 41.5006% | 7.030 | Over6.5 / BOS ML |
| Current season only n6/n5 (no previous-year shrinkage) | 66.9345% | 65.4932% | 5.548 | BOS ML / Under6.5 |
| Prior-year L20 alone; current scoring ignored | 56.6393% | 54.2326% | 6.219 | BOS ML / Under6.5 |


**Scenarios are sensitivity ranges, not confidence bounds:** BOS ML 55.8859%–63.7830%; Under6.5 41.5207%–70.5945%. LOW and HIGH reorder Rank 1 to Under and Over respectively. Unconfirmed goalies therefore materially affect both totals and rankings: `ADJUSTMENT_DEPENDENT`; no scenario weight is empirically estimated. No opponent-strength/5v5/xG quantitative coefficients or isolated McAvoy effect were smuggled into λ. Empty-net tail is only approximated through goal distribution and HIGH case; no proven late-game score/time-state model.

### A5. Mass/complement/gate/baseline/exact action ledger

| Key | Conditional W | Conditional P | Conditional L | Conditional V | Decisive mass | `p_card` | `p_base` | League-only exact-line baseline |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `BOS_ML` | 0.593079645 | 0 | 0.406920355 | 0 | 1 | 0.593079645 | 0.587814681 | 0.477896341 |
| `SJS_ML` | 0.406920355 | 0 | 0.593079645 | 0 | 1 | 0.406920355 | 0.412185319 | 0.522103659 |
| `O6_5` | 0.437324386 | 0 | 0.562675614 | 0 | 1 | 0.437324386 | 0.435224528 | 0.468750000 |
| `U6_5` | 0.562675614 | 0 | 0.437324386 | 0 | 1 | 0.562675614 | 0.564775472 | 0.531250000 |


**`BASELINE_LEAGUE_V1` frozen population recipe:** `Previous Sports Results/Ice Hockey/NHL/2025/2025_games.csv` at pinned 7640… blob `ddd01fb5e7902e0df1115dd2f82349ca4239b94d`: parsed 1,498 logical NHL rows, 1,312 regular-season games, last date 2026-04-16, excluded all preseason/playoff records; action on NHL credited final score including OT/SO. n=1,312. Home SJ ML 685/1312=52.2104%; away BOS ML 627/1312=47.7896%; Over6.5 615/1312=46.8750%; Under6.5 697/1312=53.1250%. Uses *no* Boston/SJ features, odds or lineup input, so comparable identical contracts. Baseline coverage 4/4 numeric supplied, 2/2 primary; future paired Brier/logloss only after properly verified prospective issue and operator definition (which are currently NOT_VERIFIED). This archived league-only population is NOT called a calibrated predictor.

**Line difficulty:** on shared mixture SD, total threshold 6.5 has descriptive z `(6.5−6.107398)/2.506861=+0.157`; ML signed full-game margin threshold 0 has z `(0−0.550593)/2.365713=-0.233`. These are *descriptive only*, not replacements for discrete CDFs. Under & Over exact complements on normally completed NHL score (push=0). Full game BOS+SJS winner probability=1. `P(both lose)=∑P(final_BOS<final_SJS AND final_BOS+final_SJS≥7)=0.178281737`; Fréchet check lower=0.000000000 upper=0.406920355, computed exact lies within. Conditional both decisive=1. Pair is NOT mechanically protected; high Hit@2 alone cannot establish accuracy.

**Shadows: all `NOT_PRIMARY`:** published full-universe `SHADOW_MAIN_P_ORDER_V2=NOT_COMPUTED` (no predeclared derived NHL total/spread ladder). `SHADOW_GATE_RET03`: exclude Rank1 match-winner quantity, best other family Under6.5, same <62 and <4pp gate. `SHADOW_R2_RET04=NONE`, since Under6.5 <58 on a different quantity. `SHADOW_R2_XCARD6=NONE`, since no remaining supplied row ≥58; no assisted substitution. `SHADOW_RANK_DELTA=NONE` because only Bruins ML meets p≥58 with same-line frozen baseline, fewer than 2 rows. `SHADOW_BASE_ONLY` under base scenario: BOS ML 58.7815% (Rank1), Under 56.4775% (Rank2); original general floor and gap still fail. Full published-policy gate is NOT_ASSESSABLE without supported complete comparison universe.

### A6. Adjustments and unchanged centre

| Driver | Observed | Model implementation | Caution |
|---|---|---|---|
| Venue | SAP Center SJ home, BOS travel west after Oct10 | 2025–26 league mean home/away reg gap split ±0.0675 goals | Venue effect not re-fitted to current teams; rest travel coefficient absent |
| Form | BOS 2026 reg 19–13/6; SJS 10–17/5; previous 2025 last20 separate | Twenty-game prior pseudo-count and simple attack/defence pair mean | Uncalibrated weight and roster continuity |
| Goalie | NHL projected Swayman and Askarov; short-season saves 0.932/0.860 | Named LOW/BASE/HIGH joint rate scenarios; further one-goalie stress | Starter NOT confirmed; no independently estimated shots→goals effect |
| Special teams | BOS 3/16 PP; SJS reported 15.4% PP | No extra numeric rate or double count | SJS denominator needs owner check |
| McAvoy | NHL reports season debut, prior suspension complete | QUALITATIVE_ONLY (no measured −goals effect) | Projection not game-night confirmed ice-time |
| Empty net | NHL scoring includes pulled-goalie goals | Total tail represented by regime-wide Poisson mixture only | No period/score-state pull risk model |
| Unadjusted stage-only league reference | Prior NHL regular 2025 league 6.2538 goals total; SJ home win .522 | Dedicated independent exact-line `BASELINE_P`, separate from card | Not a learned team model; never directly inserted as matchup p |

### A7. Sensitivity, endpoint and decision flags

- `RANK1_UNSTABLE`: BOS ML below 0.62; gap below 0.04. Rank2 Under6.5 below 0.58. No unsupported optimistic promotion.
- `ADJUSTMENT_DEPENDENT / GOALIE_UNCONFIRMED`: LOW primary order Under/BOS, BASE BOS/Under, HIGH Over/BOS. Goalie-alternative shocks can produce even Sharks ML first. Numerical bands are analyst perturbations, not statistical CIs.
- `FORM_WINDOW_SENSITIVE`: 2026 only vs 2025 prior-only quantifies model-mix choice; exact L10/15/20 for 2026 cannot be formed without borrowing across seasons. Identical-scope four-window sensitivity `WINDOW_SENSITIVITY_NOT_COMPUTABLE: insufficient 2026 current-season games`.
- `SO_CREDIT`: regulation tie mass transferred to winner by exact one-goal credit; penalty shootout attempts are *not* regulation goals. If an operator prices 60-minute result instead of ML including OT/SO, contract is DIFFERENT and this card must not be misgraded.
- `KNOWN_AT_UNVERIFIED`: source publication minute for lineup/goalie projections and independent lineup activation not captured; live outcome exposure NONE_OBSERVED but start cannot be certified. `ELIGIBILITY_PROSPECTIVE=NO` for clean pregame skill cohort, even when numeric outputs exist.

### A8. Source receipts, capture plan, excluded fields and intake

**Real research retrievals:** around 2026-10-14 14:04–14:10 AEDT; individual page modification times not always shown; every current-season result dated through Oct10. Roster projections published by Oct13, final lineup NOT independently retrieved. Three web domains may reuse NHL official feeds; independent collection `UNKNOWN`. No sportsbook odds, tips or market data used (market-side website results excluded from evidence).

| Source | URL / pinned path | Fields observed, use, missingness |
|---|---|---|
| Official Sharks NHL pregame projected lineup | https://www.nhl.com/sharks/news/boston-bruins-san-jose-sharks-game-preview-october-13-2026 | BOS (4–2), SJS (3–2); 11PM EDT, projected both goalies and lines; McAvoy returns, Goodrow available; duplicate Chernyshov typo, no final confirmation |
| NHL fixture/game center | https://www.nhl.com/gamecenter/bos-vs-sjs/2026/10/13/2026020105 | Native NHL ID and city; actual puck-drop/first-shift NOT verified from game-center live endpoint |
| Official club and independent pregame stats | https://puckbank.com/game/2026020105?v=preview | 2026 team GF/GA, special-teams % and estimated goalies; provider draws from NHL feed |
| 2026 BOS records (pre-cutoff) | https://www.hockey-reference.com/teams/BOS/2027.html | 6 games, 4–2, 20 GF,13 GA, 3/16 PP; 153 shots for, 163 against; full games through Oct10 |
| 2026 SJS records (pre-cutoff) | https://www.hockey-reference.com/teams/SJS/2027.html | 5 games,3–2,13 GF,17 GA; NHL season record and game dates Oct1–10 |
| NHL goalie prior-to-event | https://www.nhl.com/de/gamecenter/bos-vs-sjs/2026/10/13/2026020105 | Swayman season 5 starts,133 SA/124 SV; backup DiPietro; projected SJ Askarov; dynamic lineup status not final |
| StatMuse Sharks dated game trace | https://www.statmuse.com/nhl/ask/sharks-game-game-log | 2026 Oct1,3,5,8,10 scores; future games excluded |
| NHL official latest recap | https://www.nhl.com/news/quick-recap-oilers-at-sharks-10-10-2026 | SJS 1 EDM 3 Oct10; goalie 17 saves on 20 shots, PP 0/1 latest |
| NHL archive 2025–26 | https://github.com/danisgreat/Sports-Research/blob/7640f9d10ef3c05eca4ea657de8b9554d446b635/Previous%20Sports%20Results/Ice%20Hockey/NHL/2025/2025_games.csv | 1,498 logical, 1,312 regular; complete previous last20 traces; scores, decision, no measured xG |
| Current pinned controls/status | https://github.com/danisgreat/Sports-Research/blob/7640f9d10ef3c05eca4ea657de8b9554d446b635/CURRENT_STATE.md | v11 method, canonical P-584/P-585, publication and selection scope |

**Settlement field capture plan only (NOT performed):** official NHL game `2026020105` `gameState`, actual period first event time, NHL event summary, period-by-period BOS/SJS goals, each OT goal, shootout winner and credited score, shot/goalie ice time and starts, full special-team opportunities, official lineup/scratches, provenance of empty-net goals; any abandoned/shortened game requires specific operator action. Capture after final with publication timestamp and user-provided operator terms. No later data is permitted into original issued p/rank. `SETTLEMENT=NOT_PERFORMED`; `CANONICAL_IMPORT=NOT_PERFORMED`; `GITHUB_WRITES=NO`.

### A9. Self-audit — substantive evidence and gaps

| Check group | Result | Evidence / limitation |
|---|---|---|
| C1–C2 | PARTIAL | Full pinned v11 operating controls read; native NHL ID verified; complete local mini searched; no indexed GitHub duplicate; very large Part7 body and external private minis not exhaustively available |
| C3–C4 | PASS | Four unique supplied keys, four exact ranks; shared normalized 26×26 scenario score grid and coherent W/P/L/V; opposites sum 1 |
| C5–C6 | PASS | Rank1/Rank2 floor and supplied-scope noncomplementary gap computed; exact joint 0.178281737, <Frechet bounds and conditional both-decisive 1; no mechanical cover |
| C7–C9 | PARTIAL | Score and goalie/form sensitivity calculated; shot quality, exact goalie confirmation, roster and independent xG absent; NHL game endpoint treated with OT/SO credited goal |
| C10–C12 | PARTIAL | Late-start and outcome separation correct, pregame projections/owner pages cited; operator terms/known-at publication minutes not verifiable, no odds used |
| C13–C15 | PASS/PARTIAL | 1,312 prior NHL rows and exact-line 4/4 baseline computed; previous season separate; regulation/final distinction, covariance and SD calculated; L10–L20 current season partial |
| C16 | PASS SUBJECT TO VERIFIED READBACK | Previous four issued blocks retained byte-for-byte, one new P-589 block, one footer advancement; see actual file receipt below (no claim until readback succeeds) |
| C17–C20 | PARTIAL | Four-window current n6/n5 properly partial; line distance/gap/baseline and weights shown; writer lease valid at append; intake/footer updated; actual puck drop not verified |
| FR1–FR3 | PARTIAL | Both season and previous-season form tables with dates/IDs and actual n; missing xG, field availability and goalie older start histories disclosed |
| FR4–FR6 | PARTIAL | Explicit longer-window prior shrinkage, separate current stage and season, supported LOW/BASE/HIGH and goalie stresses; last5/10/15/20 complete-season independent comparisons not possible |
| SF-A1–SF-A5 | PASS | Four raw literals=4 distinct exact keys; user-only primary ranks and W/P/L/V; complete sorted table, no generated primaries |
| SF-A6–SF-A9 | PASS | 90% ceiling, family/gate/Rank2 diagnostics, joint exact event-state count, separately declared unavailable shadow universes |
| SF-A10–SF-A12 | PARTIAL / PASS after readback | frozen formulas, timestamp and late exposure; writer lease/mini freeze/next working ID rechecked, original blocks preserved and no GitHub writes; operator terms remain unknown |
| Q4 model arithmetic | PASS | final state mass 1.0000000000, nonnegative; max discarded pre-normalization Poisson tail <3×10⁻¹⁴; W+P+L+V=1; both complementary binary pairs 1; exact loss joint within Fréchet |

**Local research implementation note:** code and model JSON (`p589_calc.py`, `p589_model.json`) exist only in the current sandbox, not in GitHub. This card remains an **uncalibrated / late-start research observation**, not a historical backcast or certification. The scheduled start was already crossed when the research request was opened; no earlier pregame timestamp is fabricated.

<!-- END CARD P-589 -->

<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Highest new working ID used / next working ID | `P-589` / `P-590` |
| Repository next-ID snapshot | `P-585` |
| New cards / numeric / qualitative / NO_FORECAST | 5 / 5 / 0 / 0 |
| Pending events / unresolved evidence records | 6 / 3 (P-584 canonical + P-585/P-586/P-587/P-588/P-589 local; three inherited field-specific gaps; grouped dependencies separately; >5 pending alert TRIGGERED) |
| Local mini status / import status | ACTIVE / PENDING |
| GitHub writes performed | NO |
<!-- END FOOTER -->




# SETTLEMENT AND RETROSPECTIVES
<!-- SETTLEMENT-FORMAT: mini-settlement-6 -->

**Authority:** `PUBLISHED_MAIN_PINNED` · `3ab6d27fedb177add7cca5b41b14346107688ce3` (published GitHub `main`, read-only); source mini issued at older pinned commits, each remains authoritative for its issue-time fields. **Settled:** 2026-10-14T18:50:59+11:00 Australia/Melbourne. User policy `SUPPLIED_FIRST_V1` retained for original primary ranks, explicitly distinct from published `P_ORDER_V2`.
**FROZEN_SOURCE:** original `/mnt/data/Mini Prediction Log - P-585 onward - 2026-10-13/PREDICTION_MINI_RUNNING_LOG_P-585_ONWARD.md`, 208588 bytes, SHA256 `5a57bd78e79c6cd9b8eec8e6b52ab96bc4743ddbf656f442e659ad13c987fdae`, 1200 lines, cards P-585–P-589 + `P-587 2026-10-14-SHADOW-01` addendum; frozen 2026-10-14T18:39:18+11:00. Writer handover `NONE` (new mini not authorised). Exact source prefix and copy/settled-file readback subject to final audit in manifest. Current source kept unchanged. No GitHub writes, no canonical import, no new IDs.
**Evidence cut:** Each of 5 requested events is terminal in available owner/participant-official evidence; wall-clock final timestamps are unknown. Grading applies frozen completed-event sporting conventions, with unknown operator settlement/void policy recorded separately. Original mini queue has four inherited canonical records, not new predictions.
**Evidence timing precision:** Exact per-source network retrieval instants were not independently logged; the dated review and settlement compilation time are not substitutes for URL-specific source update or verified final-time evidence.

<!-- BEGIN SETTLEMENT P-585 revision-1 -->
### Settlement · P-585 · Arthur Gea vs Jakub Menšík · 2026-10-14T18:50:59+11:00
**Revision:** `revision-1`; parent `NONE`; affected keys `ALL_FOUR_ORIGINAL_SUPPLIED`; grade changes `UNSETTLED → LOSS/LOSS/WIN/WIN`; source `ORIGINAL_MINI.md`, immutable card markers; correction none. **State:** `SETTLED` for completed-game sporting convention; operator-grade `UNKNOWN` (no operator terms).
**Native identity:** `ATP-2026-SHANGHAI-R16`. **Verified score:** Géa 7–6(4), 6–4 Menšík. Completed best-of-three, two sets, no retirement reported; Géa 13 games, Menšík 10; total=23; Géa−Menšík=+3 games. **Evidence:** B (ATP-operated official tournament / ATP staff final match report; Tennis.com completed set scoreboard corroborates); https://en.rolexshanghaimasters.com/en/media/news/gea-mensik-shanghai-2026-tuesday. Actual final wall time and source original update minute `NOT_VERIFIED`; retrieved in 14 Oct 2026 settlement review. **Original timing:** FIRST_SERVE_NOT_VERIFIED / source displayed Upcoming at issue; prospectivity not certified.
**Original expected score (immutable):** Géa games 11.919 (SD 3.992); Menšík games 13.548 (SD 3.152); total 25.467 (SD 6.030); Géa−Menšík −1.628 (SD 3.923).

| Original numeric rank | Exact original proposition / scope | Original `p_card` | Original `p_base` | Original `BASELINE_P` | Sporting grade | Evidence | Frozen definition / arithmetic |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Total match games Over 23.5 | `52.50%` | `52.80%` | `BASELINE_UNAVAILABLE` | **LOSS** | B | 23 ≤ 23, needs ≥24; operator action UNKNOWN |
| 2 | Menšík −2.5 total games | `51.61%` | `51.67%` | `BASELINE_UNAVAILABLE` | **LOSS** | B | Menšík 10 − Géa 13 = −3; needs ≥+3; operator action UNKNOWN |
| 3 | Gea +2.5 total games | `48.39%` | `48.33%` | `BASELINE_UNAVAILABLE` | **WIN** | B | Géa 13 − Menšík 10 = +3; needs ≥−2; operator action UNKNOWN |
| 4 | Total match games Under 23.5 | `47.50%` | `47.20%` | `BASELINE_UNAVAILABLE` | **WIN** | B | 23 ≤23; operator action UNKNOWN |

**Literal source table custody:** The following four original ranked lines are copied verbatim from the frozen original card; retain user-supplied source-rank/definition and p exactly. Supplemental human-readable short labels above do not replace these lines.
```text
| 1 | PICK | SUPPLIED | `total_games:over:23.5:completed_bo3`: **Total match games Over 23.5** (24+) | `52.50%` | `52.80%` | BASELINE_UNAVAILABLE | 23.5−25.467=-1.967 games / `-0.326` | P585 3-case complete-match tree | Short straight-sets match <=23 games |
| 2 | PICK | SUPPLIED | `aggregate_games_margin:mensik_minus:2.5:completed_bo3`: **Menšík −2.5 total games** (wins margin >=3 games; may win or lose match) | `51.61%` | `51.67%` | BASELINE_UNAVAILABLE | 2.5−1.628=+0.872 games / `+0.222` | Same model | Gea keeps total game margin within 2 or leads |
| 3 | INFORMATIONAL | SUPPLIED | `aggregate_games_margin:gea_plus:2.5:completed_bo3`: **Gea +2.5 total games** | `48.39%` | `48.33%` | BASELINE_UNAVAILABLE | −2.5−-1.628=-0.872 games / `-0.222` | Same model | Menšík accumulates >=3 more total games |
| 4 | INFORMATIONAL | SUPPLIED | `total_games:under:23.5:completed_bo3`: **Total match games Under 23.5** (<=23) | `47.50%` | `47.20%` | BASELINE_UNAVAILABLE | 23.5−25.467=-1.967 games / `-0.326` | Same model | >=24 games from long two-set/three-set match |
```
**Top-two:** `ALL_LOST` · WIN=0, LOSS=2, PUSH=0; decisive=2/2. Original Rank1 Total match games Over 23.5 (52.50%)→LOSS; Rank2 Menšík −2.5 total games (51.61%)→LOSS. Winner call Menšík **WRONG**.
**Original numeric proper scores (conditional decisive; n=2):** Brier=0.270992, log loss=0.735159; `A/B HEADLINE` and `A/B+C/E SENSITIVITY` identical for this event; exact same-row paired baseline count=0/2.

**Frozen expected-vs-observed (first participant is source-card orientation):**
| Variable | Observed | Frozen mean | Error (obs−mean) | Error / original SD |
|---|---:|---:|---:|---:|
| first side | 13 | 11.919 | +1.081 | +0.271 |
| second side | 10 | 13.548 | -3.548 | -1.126 |
| total | 23 | 25.467 | -2.467 | -0.409 |
| signed first−second margin | 3 | -1.628 | +4.628 | +1.180 |
**Original shadows, separate:** `SHADOW_BASE_ONLY` present and follows same top-two contract keys in all five cards; its probabilities are base-case variants and not new original forecasts. `SHADOW_RANK_DELTA` not computed/no qualifying pair in this card. RET03/RET04/XCARD6 and published-policy comparators never retrospectively created.
**Form-window check:** observed first/second/total/margin values above vs frozen adjusted centre; independent original unadjusted common-event centre for like-for-like error is documented in original A4/A6 but not reconstructed as a new numerical forecast here; `UNADJUSTED_ERROR_NOT_COMPUTED`.
**R1. Original prediction:** Rank1 `Total match games Over 23.5` p=`52.50%`; Rank2 `Menšík −2.5 total games` p=`51.61%`; original `BASELINE_P` copied above; Géa games 11.919 (SD 3.992); Menšík games 13.548 (SD 3.152); total 25.467 (SD 6.030); Géa−Menšík −1.628 (SD 3.923).
**R2. Final event:** Completed best-of-three, two sets, no retirement reported; Géa 13 games, Menšík 10; total=23; Géa−Menšík=+3 games. Terminal evidence B; final wall-clock `NOT_VERIFIED`; operator terms `UNKNOWN`.
**R3. Contract settlement:** each user-supplied row graded literally as tabulated, with exact winner, line threshold and push rules; no new lines priced or reconstructed.
**R4. Rank diagnostics:** ALL_LOST, primary decisive 2/2, numeric p available 2/2; general gate and original supplied scope retain issued state; no hindsight reshuffle. Non-complementary original primary pair; no mechanical protection claim.
**R5. Winner call:** original predicted `Menšík` → WRONG; winner diagnostic NOT_PRIMARY for this settlement.
**R6. Line assessment:** Rank1 23 ≤ 23, needs ≥24; Rank2 Menšík 10 − Géa 13 = −3; needs ≥+3; Rank3 Géa 13 − Menšík 10 = +3; needs ≥−2; Rank4 23 ≤23. The distances in units derive from the frozen line, not new thresholds.
**R7. Expected versus realised:** Two competitive but short straight sets: 13 games in a first-set tiebreak and 10 in the second; Géa won the final-game margin 13−10. Original predicted Menšík match victory, which also failed. Frozen-score error table above; outcome is one draw from an uncalibrated distribution and not a proof of correctness or miscalibration.
**R8. Mechanism/failure:** Two competitive but short straight sets: 13 games in a first-set tiebreak and 10 in the second; Géa won the final-game margin 13−10. Original predicted Menšík match victory, which also failed. Advanced chance-quality or player-contribution causal attribution stays `NOT_ASSESSABLE` where exact frozen source lacks the measurable field.
**R9. Cutoff/source/timing:** The pre-issue hold/return assumptions were subjective; the observed result, return-game conversions and match fitness were not knowable at cutoff. First-serve time and final wall-clock are not verified. Timing FIRST_SERVE_NOT_VERIFIED / source displayed Upcoming at issue; prospectivity not certified. All terminal sources discovered after original issuance, not passed backwards as pregame information.
**R10. Process verdict:** NOT_ASSESSABLE — timing uncertainty and no independent held-out tennis games-total calibration; mathematical state tree does not establish matching frequencies. Probability status `UNCALIBRATED_ANALYST_SCENARIO / NOT_CERTIFIED`; distinct from ALL_LOST outcome.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED`: Pre-register ATP outdoor-hardpoint/service hold priors and chronological game-total backtests, comparing matched 23.5 and ±2.5 game lines with independent league-only baselines; test accuracy, not just rank.
**R12. Disposition:** `MONITOR + PROPOSE_EXPERIMENT` only; retain frozen ranks/p; no model change, no new prediction, no GitHub write, no automatic training promotion; operator term and final-time capture remain open.

**R1 DEEP REVIEW — mandatory eight parts for original Rank-1 LOSS**
1. **Exact original claim:** `Total match games Over 23.5`, Rank1 p=52.50%, match to complete best-of-three; 24+ games required.
2. **Verified result:** Géa beat Menšík 7–6(4), 6–4; total 23; Rank1 lost by exactly one game relative to minimum 24. The 7–6 tiebreak is 13 games (not 14).
3. **Original distribution:** 52.50% Over, thus 47.50% Under from same completed-match tree. Under was an explicitly non-negligible original outcome. Model total E=25.467, SD=6.030; observed 23 implies −0.409 original SD. Tail-at-exact-23 mass not available from frozen prose (do not invent).
4. **Cutoff knowability:** outcome and break-point performance unobservable before play; initial website showed Upcoming but actual first serve and data publication instants not independently verified. Past Gea form and Menšík service were accessible but model service-hold adjustments subjective.
5. **Process/model/variance:** loss compatible with ordinary variance; `NOT_ASSESSABLE` on performance certification due no held-out exact-line tennis validation and first-serve verification. No numeric attribution between short match, service holds, form or selection.
6. **Cutoff-only counterfactual:** original BASE p(Over)=52.80% and BASE p(Menšík−2.5)=51.67%; base-only would still choose same Rank1 and fail. No re-selection from later score.
7. **Failure classification:** `MODEL_TAIL_REALISATION / WEAK_RANK1`, `TIMING_VERIFICATION_GAP`, not a proven probability-calibration failure. Other original Rank2 also lost.
8. **Falsifiable correction:** freeze point-by-point/service-hold priors using only pre-cutoff matches, compare p(Over23.5) and ±2.5 games against a held-out same-line ATP baseline by chronology; measure Brier, log loss and unstable-slate frequency. `PROPOSED_NOT_TESTED`.
<!-- END SETTLEMENT P-585 revision-1 -->

<!-- BEGIN SETTLEMENT P-586 revision-1 -->
### Settlement · P-586 · Bahçeşehir Koleji Istanbul vs Kids&Us Manresa · 2026-10-14T18:50:59+11:00
**Revision:** `revision-1`; parent `NONE`; affected keys `ALL_FOUR_ORIGINAL_SUPPLIED`; grade changes `UNSETTLED → WIN/LOSS/WIN/LOSS`; source `ORIGINAL_MINI.md`, immutable card markers; correction none. **State:** `SETTLED` for completed-game sporting convention; operator-grade `UNKNOWN` (no operator terms).
**Native identity:** `EUROCUP-U2026-47`. **Verified score:** Bahçeşehir 100–88 Manresa. Four regulation quarters 32–20, 21–24, 23–22, 24–22; no overtime; total=188, Bahçeşehir−Manresa=+12. **Evidence:** B (official participating club report and quarter line (owner league media centre remained stale 0–0)); https://www.basquetmanresa.com/en/news/baxi-manresa/game-report/2026/defeat-of-kidsus-on-the-complicated-court-of-bahcesehir/. Actual final wall time and source original update minute `NOT_VERIFIED`; retrieved in 14 Oct 2026 settlement review. **Original timing:** LATE_START_UNVERIFIED; issue 2026-10-14T03:03:58+11:00 after 03:00 scheduled.
**Original expected score (immutable):** Bahçeşehir 93.431; Manresa 83.431; total 176.861 (regulation proxy SD 20.118); Bahçeşehir−Manresa +10.000 (regulation proxy SD 16.553); full-OT SD not established.

| Original numeric rank | Exact original proposition / scope | Original `p_card` | Original `p_base` | Original `BASELINE_P` | Sporting grade | Evidence | Frozen definition / arithmetic |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Manresa +13.5 points | `58.37%` | `58.66%` | `BASELINE_UNAVAILABLE` | **WIN** | B | Bahçeşehir 12-point victory <14-point exclusion; operator action UNKNOWN |
| 2 | Combined Under 178.5 points | `53.31%` | `54.30%` | `BASELINE_UNAVAILABLE` | **LOSS** | B | 188 ≥179; operator action UNKNOWN |
| 3 | Combined Over 178.5 points | `46.69%` | `45.70%` | `BASELINE_UNAVAILABLE` | **WIN** | B | 188 ≥179; operator action UNKNOWN |
| 4 | Bahçeşehir −13.5 points | `41.63%` | `41.34%` | `BASELINE_UNAVAILABLE` | **LOSS** | B | Bahçeşehir won by only 12, not ≥14; operator action UNKNOWN |

**Literal source table custody:** The following four original ranked lines are copied verbatim from the frozen original card; retain user-supplied source-rank/definition and p exactly. Supplemental human-readable short labels above do not replace these lines.
```text
| 1 | PICK (LOW_CONFIDENCE) | SUPPLIED | `FULL_GAME_MARGIN:MAN+13.5:INCL_OT` — Manresa **+13.5 points** | **58.37%** | 58.66% | BASELINE_UNAVAILABLE | threshold margin 13.5 − base M10 = +3.5; z=+0.219 | three-case normal margin | Bahçeşehir wins by ≥14 |
| 2 | PICK (LOW_CONFIDENCE) | SUPPLIED | `FULL_GAME_TOTAL:UNDER178.5:INCL_OT` — Combined **Under 178.5 points** | **53.31%** | 54.30% | BASELINE_UNAVAILABLE | threshold total 178.5 − base T176 = +2.5; z=+0.125 before OT | three-case normal total + tie/OT | Combined score reaches ≥179 |
| 3 | INFORMATIONAL | SUPPLIED | `FULL_GAME_TOTAL:OVER178.5:INCL_OT` — Combined **Over 178.5 points** | 46.69% | 45.70% | BASELINE_UNAVAILABLE | same line, opposite direction | complement of full total | Slow pace / bad shooting, total ≤178 |
| 4 | INFORMATIONAL | SUPPLIED | `FULL_GAME_MARGIN:BAH-13.5:INCL_OT` — Bahçeşehir **−13.5 points** | 41.63% | 41.34% | BASELINE_UNAVAILABLE | same margin threshold, opposite direction | complement of game handicap | Manresa loses by ≤13 or wins |
```
**Top-two:** `SPLIT` · WIN=1, LOSS=1, PUSH=0; decisive=2/2. Original Rank1 Manresa +13.5 points (58.37%)→WIN; Rank2 Combined Under 178.5 points (53.31%)→LOSS. Winner call Bahçeşehir **CORRECT**.
**Original numeric proper scores (conditional decisive; n=2):** Brier=0.228751, log loss=0.650004; `A/B HEADLINE` and `A/B+C/E SENSITIVITY` identical for this event; exact same-row paired baseline count=0/2.

**Frozen expected-vs-observed (first participant is source-card orientation):**
| Variable | Observed | Frozen mean | Error (obs−mean) | Error / original SD |
|---|---:|---:|---:|---:|
| first side | 100 | 93.431 | +6.569 | NOT_ESTIMATED |
| second side | 88 | 83.431 | +4.569 | NOT_ESTIMATED |
| total | 188 | 176.861 | +11.139 | NOT_ESTIMATED |
| signed first−second margin | 12 | 10.000 | +2.000 | NOT_ESTIMATED |
**SD restriction:** Frozen 20.118/16.553 are regulation-only proxy widths, so a full-game overtime-aware standardised score error is NOT_ESTIMATED; raw full-game errors above remain valid. For this observed no-OT game the regulation proxies may be displayed diagnostically only (total +11.139/20.118≈+0.554; margin +2.000/16.553≈+0.121).
**Original shadows, separate:** `SHADOW_BASE_ONLY` present and follows same top-two contract keys in all five cards; its probabilities are base-case variants and not new original forecasts. `SHADOW_RANK_DELTA` not computed/no qualifying pair in this card. RET03/RET04/XCARD6 and published-policy comparators never retrospectively created.
**Form-window check:** observed first/second/total/margin values above vs frozen adjusted centre; independent original unadjusted common-event centre for like-for-like error is documented in original A4/A6 but not reconstructed as a new numerical forecast here; `UNADJUSTED_ERROR_NOT_COMPUTED`.
**R1. Original prediction:** Rank1 `Manresa +13.5 points` p=`58.37%`; Rank2 `Combined Under 178.5 points` p=`53.31%`; original `BASELINE_P` copied above; Bahçeşehir 93.431; Manresa 83.431; total 176.861 (regulation proxy SD 20.118); Bahçeşehir−Manresa +10.000 (regulation proxy SD 16.553); full-OT SD not established.
**R2. Final event:** Four regulation quarters 32–20, 21–24, 23–22, 24–22; no overtime; total=188, Bahçeşehir−Manresa=+12. Terminal evidence B; final wall-clock `NOT_VERIFIED`; operator terms `UNKNOWN`.
**R3. Contract settlement:** each user-supplied row graded literally as tabulated, with exact winner, line threshold and push rules; no new lines priced or reconstructed.
**R4. Rank diagnostics:** SPLIT, primary decisive 2/2, numeric p available 2/2; general gate and original supplied scope retain issued state; no hindsight reshuffle. Non-complementary original primary pair; no mechanical protection claim.
**R5. Winner call:** original predicted `Bahçeşehir` → CORRECT; winner diagnostic NOT_PRIMARY for this settlement.
**R6. Line assessment:** Rank1 Bahçeşehir 12-point victory <14-point exclusion; Rank2 188 ≥179; Rank3 188 ≥179; Rank4 Bahçeşehir won by only 12, not ≥14. The distances in units derive from the frozen line, not new thresholds.
**R7. Expected versus realised:** Bahçeşehir scored 100, exceeding frozen expected 93.431; total overshot 178.5 by 9.5 points, but Manresa remained within 13.5. Frozen-score error table above; outcome is one draw from an uncalibrated distribution and not a proof of correctness or miscalibration.
**R8. Mechanism/failure:** Bahçeşehir scored 100, exceeding frozen expected 93.431; total overshot 178.5 by 9.5 points, but Manresa remained within 13.5. Advanced chance-quality or player-contribution causal attribution stays `NOT_ASSESSABLE` where exact frozen source lacks the measurable field.
**R9. Cutoff/source/timing:** Lineup and minutes unconfirmed at issuance; game was scheduled before the actual local issue time. The final scoring and fourth-quarter total could not legitimately inform frozen probabilities. Timing LATE_START_UNVERIFIED; issue 2026-10-14T03:03:58+11:00 after 03:00 scheduled. All terminal sources discovered after original issuance, not passed backwards as pregame information.
**R10. Process verdict:** DEFICIENT for verified prospective timing/lineup; sport-side definitions coherent. Single outcome not evidence of model-calibration error. Probability status `UNCALIBRATED_ANALYST_SCENARIO / NOT_CERTIFIED`; distinct from SPLIT outcome.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED`: Require an authenticated 40-minute league box and pre-issue starting five, then fit EuroCup pace/total distribution by chronological held-out results and measure exact-line coverage.
**R12. Disposition:** `MONITOR + PROPOSE_EXPERIMENT` only; retain frozen ranks/p; no model change, no new prediction, no GitHub write, no automatic training promotion; operator term and final-time capture remain open.
<!-- END SETTLEMENT P-586 revision-1 -->

<!-- BEGIN SETTLEMENT P-587 revision-1 -->
### Settlement · P-587 · Calgary Flames @ Anaheim Ducks · 2026-10-14T18:50:59+11:00
**Revision:** `revision-1`; parent `NONE`; affected keys `ALL_FOUR_ORIGINAL_SUPPLIED`; grade changes `UNSETTLED → WIN/LOSS/PUSH/PUSH`; source `ORIGINAL_MINI.md`, immutable card markers; correction none. **State:** `SETTLED` for completed-game sporting convention; operator-grade `UNKNOWN` (no operator terms).
**Native identity:** `NHL-2026020103`. **Verified score:** Calgary 4–2 Anaheim. NHL 3-period regulation 1–2, 1–0, 2–0; no OT/SO; total=6. Calgary scored final empty-net goal; Anaheim−Calgary=−2. **Evidence:** A (NHL official gamecenter final score, period line and goalie sheet (club official recap corroborates)); https://www.nhl.com/gamecenter/cgy-vs-ana/2026/10/13/2026020103/boxscore. Actual final wall time and source original update minute `NOT_VERIFIED`; retrieved in 14 Oct 2026 settlement review. **Original timing:** LATE_START_UNVERIFIED; issue after NHL scheduled 2026-10-14T12:45:00+11:00.
**Original expected score (immutable):** Anaheim 3.508 (SD 1.866); Calgary 2.763 (SD 1.682); total 6.271 (SD 2.524); Anaheim−Calgary +0.745 (SD 2.500).

| Original numeric rank | Exact original proposition / scope | Original `p_card` | Original `p_base` | Original `BASELINE_P` | Sporting grade | Evidence | Frozen definition / arithmetic |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Flames +1.5 | `0.630112` | `0.629292` | `0.698933` | **WIN** | A | Calgary wins by 2, so CGY−ANA+1.5=+3.5; operator action UNKNOWN |
| 2 | Ducks ML | `0.622630` | `0.622733` | `0.522104` | **LOSS** | A | Anaheim lost 2–4; operator action UNKNOWN |
| 3 | Combined Total Goals: Over 6.0 Goals | `0.514553` | `0.517957` | `0.523404` | **PUSH** | A | exact total=6; operator action UNKNOWN |
| 4 | Combined Total Goals: Under 6.0 Goals | `0.485447` | `0.482043` | `0.476596` | **PUSH** | A | exact total=6; operator action UNKNOWN |

**Literal source table custody:** The following four original ranked lines are copied verbatim from the frozen original card; retain user-supplied source-rank/definition and p exactly. Supplemental human-readable short labels above do not replace these lines.
```text
| 1 | Flames +1.5 | 0.630112 (63.011%) | 0.630112 | 0.000000 | 0.369888 | 0.0† | 1.000000 | 0.629292 | 0.698933 | PICK |
| 2 | Ducks ML | 0.622630 (62.263%) | 0.622630 | 0.000000 | 0.377370 | 0.0† | 1.000000 | 0.622733 | 0.522104 | PICK |
| 3 | Combined Total Goals: Over 6.0 Goals | 0.514553 (51.455%) | 0.458154 | 0.109609 | 0.432237 | 0.0† | 0.890391 | 0.517957 | 0.523404 | INFO |
| 4 | Combined Total Goals: Under 6.0 Goals | 0.485447 (48.545%) | 0.432237 | 0.109609 | 0.458154 | 0.0† | 0.890391 | 0.482043 | 0.476596 | INFO |
```
**Top-two:** `SPLIT` · WIN=1, LOSS=1, PUSH=0; decisive=2/2. Original Rank1 Flames +1.5 (0.630112)→WIN; Rank2 Ducks ML (0.622630)→LOSS. Winner call Anaheim **WRONG**.
**Original numeric proper scores (conditional decisive; n=2):** Brier=0.262243, log loss=0.718193; `A/B HEADLINE` and `A/B+C/E SENSITIVITY` identical for this event; exact same-row paired baseline count=2/2.
Paired frozen same-line baseline (n=2): card Brier 0.262243, baseline Brier 0.181617; card log loss 0.718193, baseline log loss 0.548281. No baseline retrofill.

**Frozen expected-vs-observed (first participant is source-card orientation):**
| Variable | Observed | Frozen mean | Error (obs−mean) | Error / original SD |
|---|---:|---:|---:|---:|
| first side | 2 | 3.508 | -1.508 | -0.808 |
| second side | 4 | 2.763 | +1.237 | +0.735 |
| total | 6 | 6.271 | -0.271 | -0.107 |
| signed first−second margin | -2 | 0.745 | -2.745 | -1.098 |
**Original shadows, separate:** `SHADOW_BASE_ONLY` present and follows same top-two contract keys in all five cards; its probabilities are base-case variants and not new original forecasts. P-587 `SHADOW_RANK_DELTA` correction addendum: frozen shadow order Ducks ML LOSS / Flames +1.5 WIN; do not count as original Rank1/2. RET03/RET04/XCARD6 and published-policy comparators never retrospectively created.
**Form-window check:** observed first/second/total/margin values above vs frozen adjusted centre; independent original unadjusted common-event centre for like-for-like error is documented in original A4/A6 but not reconstructed as a new numerical forecast here; `UNADJUSTED_ERROR_NOT_COMPUTED`.
**R1. Original prediction:** Rank1 `Flames +1.5` p=`0.630112`; Rank2 `Ducks ML` p=`0.622630`; original `BASELINE_P` copied above; Anaheim 3.508 (SD 1.866); Calgary 2.763 (SD 1.682); total 6.271 (SD 2.524); Anaheim−Calgary +0.745 (SD 2.500).
**R2. Final event:** NHL 3-period regulation 1–2, 1–0, 2–0; no OT/SO; total=6. Calgary scored final empty-net goal; Anaheim−Calgary=−2. Terminal evidence A; final wall-clock `NOT_VERIFIED`; operator terms `UNKNOWN`.
**R3. Contract settlement:** each user-supplied row graded literally as tabulated, with exact winner, line threshold and push rules; no new lines priced or reconstructed.
**R4. Rank diagnostics:** SPLIT, primary decisive 2/2, numeric p available 2/2; general gate and original supplied scope retain issued state; no hindsight reshuffle. **Protection:** original CGY+1.5/Ducks ML pair is mechanically protected; Hit@2 for this event is not evidence of skill.
**R5. Winner call:** original predicted `Anaheim` → WRONG; winner diagnostic NOT_PRIMARY for this settlement.
**R6. Line assessment:** Rank1 Calgary wins by 2, so CGY−ANA+1.5=+3.5; Rank2 Anaheim lost 2–4; Rank3 exact total=6; Rank4 exact total=6. The distances in units derive from the frozen line, not new thresholds.
**R7. Expected versus realised:** Calgary outshot Anaheim 36–25 and scored the winning goal late followed by a credited empty-net insurance goal. Total landed on the integer-6 push boundary; original Rank1/2 were mechanically protected for a completed NHL game. Frozen-score error table above; outcome is one draw from an uncalibrated distribution and not a proof of correctness or miscalibration.
**R8. Mechanism/failure:** Calgary outshot Anaheim 36–25 and scored the winning goal late followed by a credited empty-net insurance goal. Total landed on the integer-6 push boundary; original Rank1/2 were mechanically protected for a completed NHL game. Advanced chance-quality or player-contribution causal attribution stays `NOT_ASSESSABLE` where exact frozen source lacks the measurable field.
**R9. Cutoff/source/timing:** Actual first puck and finalized starting goalies were unverified at the card issue; Wolf and Dostál are confirmed only retrospectively via game sheet. No live outcomes may enter a reconstructed pregame model. Timing LATE_START_UNVERIFIED; issue after NHL scheduled 2026-10-14T12:45:00+11:00. All terminal sources discovered after original issuance, not passed backwards as pregame information.
**R10. Process verdict:** DEFICIENT for prospective certification/lineup verifiability; score-action arithmetic passes on NHL league endpoint. Probability status `UNCALIBRATED_ANALYST_SCENARIO / NOT_CERTIFIED`; distinct from SPLIT outcome.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED`: Prospectively capture authenticated goalie starters, 5v5 xG and pulled-goalie time-state inputs; evaluate identical 6.0-push lines against the league baseline.
**R12. Disposition:** `MONITOR + PROPOSE_EXPERIMENT` only; retain frozen ranks/p; no model change, no new prediction, no GitHub write, no automatic training promotion; operator term and final-time capture remain open.
<!-- END SETTLEMENT P-587 revision-1 -->

<!-- BEGIN SETTLEMENT P-588 revision-1 -->
### Settlement · P-588 · Golden State Warriors @ Los Angeles Lakers · 2026-10-14T18:50:59+11:00
**Revision:** `revision-1`; parent `NONE`; affected keys `ALL_FOUR_ORIGINAL_SUPPLIED`; grade changes `UNSETTLED → WIN/WIN/LOSS/LOSS`; source `ORIGINAL_MINI.md`, immutable card markers; correction none. **State:** `SETTLED` for completed-game sporting convention; operator-grade `UNKNOWN` (no operator terms).
**Native identity:** `NBA-0012600048-PRE`. **Verified score:** Golden State 101–89 Los Angeles. NBA preseason four quarters Warriors 29/21/22/29, Lakers 29/34/13/13; no overtime; total=190, Golden State−Los Angeles=+12. **Evidence:** B (NBA official final recap (independent CBS/secondary structured quarter splits corroborate; only score used)); https://www.nba.com/watch/video/game-recap-warriors-101-lakers-89?plsrc=nba. Actual final wall time and source original update minute `NOT_VERIFIED`; retrieved in 14 Oct 2026 settlement review. **Original timing:** LATE_START_UNVERIFIED; issued 2026-10-14T13:14:34+11:00 after scheduled 13:00.
**Original expected score (immutable):** Golden State 113.209 (SD 14.756); Lakers 108.917 (SD 14.981); total 222.126 (SD 23.624); GSW−LAL +4.292 (SD 18.063).

| Original numeric rank | Exact original proposition / scope | Original `p_card` | Original `p_base` | Original `BASELINE_P` | Sporting grade | Evidence | Frozen definition / arithmetic |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Combined Total Points: Under 228.5 Points | `0.609554` | `0.636129` | `BASELINE_UNAVAILABLE` | **WIN** | B | 190 ≤228; operator action UNKNOWN |
| 2 | Warriors -2.5 points | `0.546734` | `0.574168` | `BASELINE_UNAVAILABLE` | **WIN** | B | GSW margin=+12 ≥3; operator action UNKNOWN |
| 3 | Lakers +2.5 points | `0.453266` | `0.425832` | `BASELINE_UNAVAILABLE` | **LOSS** | B | Lakers margin=−12, no cover +2.5; operator action UNKNOWN |
| 4 | Combined Total Points: Over 228.5 Points | `0.390446` | `0.363871` | `BASELINE_UNAVAILABLE` | **LOSS** | B | 190 ≤228; operator action UNKNOWN |

**Literal source table custody:** The following four original ranked lines are copied verbatim from the frozen original card; retain user-supplied source-rank/definition and p exactly. Supplemental human-readable short labels above do not replace these lines.
```text
| 1 | PICK | `T:GSW_plus_LAL:lt_228.5:FULL_OT:NBA_PRE` — **Combined Total Points: Under 228.5 Points** | 0.609554 | 0.390446 | 0.000000 | `0 conditional / all-event unknown` | 0.609554 | 0.636129 | `NO_PRESEASON_BASELINE` | final points >=229 |
| 2 | PICK | `M:GSW_minus_LAL:gt_2.5:FULL_OT:NBA_PRE` — **Warriors -2.5 points** | 0.546734 | 0.453266 | 0.000000 | `0 conditional / all-event unknown` | 0.546734 | 0.574168 | `NO_PRESEASON_BASELINE` | Golden State wins by <=2 or loses |
| 3 | INFORMATIONAL | `M:GSW_minus_LAL:lt_2.5:FULL_OT:NBA_PRE` — **Lakers +2.5 points** | 0.453266 | 0.546734 | 0.000000 | `0 conditional / all-event unknown` | 0.453266 | 0.425832 | `NO_PRESEASON_BASELINE` | Golden State wins by >=3 |
| 4 | INFORMATIONAL | `T:GSW_plus_LAL:gt_228.5:FULL_OT:NBA_PRE` — **Combined Total Points: Over 228.5 Points** | 0.390446 | 0.609554 | 0.000000 | `0 conditional / all-event unknown` | 0.390446 | 0.363871 | `NO_PRESEASON_BASELINE` | final points <=228 |
```
**Top-two:** `ALL_WON` · WIN=2, LOSS=0, PUSH=0; decisive=2/2. Original Rank1 Combined Total Points: Under 228.5 Points (0.609554)→WIN; Rank2 Warriors -2.5 points (0.546734)→WIN. Winner call Golden State **CORRECT**.
**Original numeric proper scores (conditional decisive; n=2):** Brier=0.178949, log loss=0.549410; `A/B HEADLINE` and `A/B+C/E SENSITIVITY` identical for this event; exact same-row paired baseline count=0/2.

**Frozen expected-vs-observed (first participant is source-card orientation):**
| Variable | Observed | Frozen mean | Error (obs−mean) | Error / original SD |
|---|---:|---:|---:|---:|
| first side | 101 | 113.209 | -12.209 | -0.827 |
| second side | 89 | 108.917 | -19.917 | -1.329 |
| total | 190 | 222.126 | -32.126 | -1.360 |
| signed first−second margin | 12 | 4.292 | +7.708 | +0.427 |
**Original shadows, separate:** `SHADOW_BASE_ONLY` present and follows same top-two contract keys in all five cards; its probabilities are base-case variants and not new original forecasts. `SHADOW_RANK_DELTA` not computed/no qualifying pair in this card. RET03/RET04/XCARD6 and published-policy comparators never retrospectively created.
**Form-window check:** observed first/second/total/margin values above vs frozen adjusted centre; independent original unadjusted common-event centre for like-for-like error is original A4/A6 contains the 112.9167 / 110.375 scoring base; observed 101/89 deviated by −11.917 / −21.375; total raw centre 223.292 vs observed 190 (−33.292). This is a diagnostic, not an original pick replacement.
**R1. Original prediction:** Rank1 `Combined Total Points: Under 228.5 Points` p=`0.609554`; Rank2 `Warriors -2.5 points` p=`0.546734`; original `BASELINE_P` copied above; Golden State 113.209 (SD 14.756); Lakers 108.917 (SD 14.981); total 222.126 (SD 23.624); GSW−LAL +4.292 (SD 18.063).
**R2. Final event:** NBA preseason four quarters Warriors 29/21/22/29, Lakers 29/34/13/13; no overtime; total=190, Golden State−Los Angeles=+12. Terminal evidence B; final wall-clock `NOT_VERIFIED`; operator terms `UNKNOWN`.
**R3. Contract settlement:** each user-supplied row graded literally as tabulated, with exact winner, line threshold and push rules; no new lines priced or reconstructed.
**R4. Rank diagnostics:** ALL_WON, primary decisive 2/2, numeric p available 2/2; general gate and original supplied scope retain issued state; no hindsight reshuffle. Non-complementary original primary pair; no mechanical protection claim.
**R5. Winner call:** original predicted `Golden State` → CORRECT; winner diagnostic NOT_PRIMARY for this settlement.
**R6. Line assessment:** Rank1 190 ≤228; Rank2 GSW margin=+12 ≥3; Rank3 Lakers margin=−12, no cover +2.5; Rank4 190 ≤228. The distances in units derive from the frozen line, not new thresholds.
**R7. Expected versus realised:** Los Angeles managed only 26 second-half points (13+13), while Golden State finished with a 12-point margin. Large downside total deviation was a realized tail event under the issued total model. Frozen-score error table above; outcome is one draw from an uncalibrated distribution and not a proof of correctness or miscalibration.
**R8. Mechanism/failure:** Los Angeles managed only 26 second-half points (13+13), while Golden State finished with a 12-point margin. Large downside total deviation was a realized tail event under the issued total model. Advanced chance-quality or player-contribution causal attribution stays `NOT_ASSESSABLE` where exact frozen source lacks the measurable field.
**R9. Cutoff/source/timing:** Original card was issued after scheduled tip, with final starting five, minutes and exact news publication timing unknown. Current recap explains the mechanism only retrospectively; do not transport it into a pregame feature. Timing LATE_START_UNVERIFIED; issued 2026-10-14T13:14:34+11:00 after scheduled 13:00. All terminal sources discovered after original issuance, not passed backwards as pregame information.
**R10. Process verdict:** DEFICIENT for prospective timing/lineup verification and dependence on subjective −3 Lakers-point adjustment, despite both picks winning. Probability status `UNCALIBRATED_ANALYST_SCENARIO / NOT_CERTIFIED`; distinct from ALL_WON outcome.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED`: Freeze true opening active rosters/minute priors, fit a preseason-specific pace/efficiency variance, backtest neutral-site games and compare matchup adjustment against no-adjustment.
**R12. Disposition:** `MONITOR + PROPOSE_EXPERIMENT` only; retain frozen ranks/p; no model change, no new prediction, no GitHub write, no automatic training promotion; operator term and final-time capture remain open.
<!-- END SETTLEMENT P-588 revision-1 -->

<!-- BEGIN SETTLEMENT P-589 revision-1 -->
### Settlement · P-589 · Boston Bruins @ San Jose Sharks · 2026-10-14T18:50:59+11:00
**Revision:** `revision-1`; parent `NONE`; affected keys `ALL_FOUR_ORIGINAL_SUPPLIED`; grade changes `UNSETTLED → WIN/LOSS/WIN/LOSS`; source `ORIGINAL_MINI.md`, immutable card markers; correction none. **State:** `SETTLED` for completed-game sporting convention; operator-grade `UNKNOWN` (no operator terms).
**Native identity:** `NHL-2026020105`. **Verified score:** Boston 6–3 San Jose. NHL regulation three periods 2–1, 2–1, 2–1; no OT/SO; empty-net goal at 18:18 of third; total=9, Boston−San Jose=+3. **Evidence:** B (NHL official published detailed goals/period timeline and goalie names; official box route returned inaccessible during current inspection); https://www.nhl.com/news/boston-bruins-san-jose-sharks-game-recap-october-13-2026. Actual final wall time and source original update minute `NOT_VERIFIED`; retrieved in 14 Oct 2026 settlement review. **Original timing:** LATE_START_UNVERIFIED; issue 2026-10-14T14:17:28+11:00 after 14:00 scheduled.
**Original expected score (immutable):** Boston 3.329; San Jose 2.778; total 6.107 (SD 2.507); Boston−San Jose +0.551 (SD 2.366).

| Original numeric rank | Exact original proposition / scope | Original `p_card` | Original `p_base` | Original `BASELINE_P` | Sporting grade | Evidence | Frozen definition / arithmetic |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Bruins ML | `0.593079645` | `0.587815` | `0.477896` | **WIN** | B | Boston won 6–3; operator action UNKNOWN |
| 2 | Combined Total Goals: Under 6.5 Goals | `0.562675614` | `0.564775` | `0.531250` | **LOSS** | B | 9 goals ≥7; operator action UNKNOWN |
| 3 | Combined Total Goals: Over 6.5 Goals | `0.437324386` | `0.435225` | `0.468750` | **WIN** | B | 9 goals ≥7; operator action UNKNOWN |
| 4 | Sharks ML | `0.406920355` | `0.412185` | `0.522104` | **LOSS** | B | San Jose lost 3–6; operator action UNKNOWN |

**Literal source table custody:** The following four original ranked lines are copied verbatim from the frozen original card; retain user-supplied source-rank/definition and p exactly. Supplemental human-readable short labels above do not replace these lines.
```text
| 1 | `Bruins ML` | **59.3080%** | `0.593079645 / 0 / 0.406920355 / 0` | 58.7815% | 47.7896% | ELIGIBLE / PICK / PRIMARY |
| 2 | `Combined Total Goals: Under 6.5 Goals` | **56.2676%** | `0.562675614 / 0 / 0.437324386 / 0` | 56.4775% | 53.1250% | ELIGIBLE / PICK / PRIMARY |
| 3 | `Combined Total Goals: Over 6.5 Goals` | **43.7324%** | `0.437324386 / 0 / 0.562675614 / 0` | 43.5225% | 46.8750% | ELIGIBLE / INFORMATIONAL |
| 4 | `Sharks ML` | **40.6920%** | `0.406920355 / 0 / 0.593079645 / 0` | 41.2185% | 52.2104% | ELIGIBLE / INFORMATIONAL |
```
**Top-two:** `SPLIT` · WIN=1, LOSS=1, PUSH=0; decisive=2/2. Original Rank1 Bruins ML (0.593079645)→WIN; Rank2 Combined Total Goals: Under 6.5 Goals (0.562675614)→LOSS. Winner call Boston **CORRECT**.
**Original numeric proper scores (conditional decisive; n=2):** Brier=0.241094, log loss=0.674753; `A/B HEADLINE` and `A/B+C/E SENSITIVITY` identical for this event; exact same-row paired baseline count=2/2.
Paired frozen same-line baseline (n=2): card Brier 0.241094, baseline Brier 0.277410; card log loss 0.674753, baseline log loss 0.748024. No baseline retrofill.

**Frozen expected-vs-observed (first participant is source-card orientation):**
| Variable | Observed | Frozen mean | Error (obs−mean) | Error / original SD |
|---|---:|---:|---:|---:|
| first side | 6 | 3.329 | +2.671 | NOT_ESTIMATED |
| second side | 3 | 2.778 | +0.222 | NOT_ESTIMATED |
| total | 9 | 6.107 | +2.893 | +1.154 |
| signed first−second margin | 3 | 0.551 | +2.449 | +1.035 |
**Original shadows, separate:** `SHADOW_BASE_ONLY` present and follows same top-two contract keys in all five cards; its probabilities are base-case variants and not new original forecasts. `SHADOW_RANK_DELTA` not computed/no qualifying pair in this card. RET03/RET04/XCARD6 and published-policy comparators never retrospectively created.
**Form-window check:** observed first/second/total/margin values above vs frozen adjusted centre; independent original unadjusted common-event centre for like-for-like error is documented in original A4/A6 but not reconstructed as a new numerical forecast here; `UNADJUSTED_ERROR_NOT_COMPUTED`.
**R1. Original prediction:** Rank1 `Bruins ML` p=`0.593079645`; Rank2 `Combined Total Goals: Under 6.5 Goals` p=`0.562675614`; original `BASELINE_P` copied above; Boston 3.329; San Jose 2.778; total 6.107 (SD 2.507); Boston−San Jose +0.551 (SD 2.366).
**R2. Final event:** NHL regulation three periods 2–1, 2–1, 2–1; no OT/SO; empty-net goal at 18:18 of third; total=9, Boston−San Jose=+3. Terminal evidence B; final wall-clock `NOT_VERIFIED`; operator terms `UNKNOWN`.
**R3. Contract settlement:** each user-supplied row graded literally as tabulated, with exact winner, line threshold and push rules; no new lines priced or reconstructed.
**R4. Rank diagnostics:** SPLIT, primary decisive 2/2, numeric p available 2/2; general gate and original supplied scope retain issued state; no hindsight reshuffle. Non-complementary original primary pair; no mechanical protection claim.
**R5. Winner call:** original predicted `Boston` → CORRECT; winner diagnostic NOT_PRIMARY for this settlement.
**R6. Line assessment:** Rank1 Boston won 6–3; Rank2 9 goals ≥7; Rank3 9 goals ≥7; Rank4 San Jose lost 3–6. The distances in units derive from the frozen line, not new thresholds.
**R7. Expected versus realised:** Six Boston goals including Will Borgen empty-netter, compared with a frozen Boston mean of 3.329; both projected goalies (Swayman/Askarov) actually played. A high total defeated the Under while the Bruins ML won. Frozen-score error table above; outcome is one draw from an uncalibrated distribution and not a proof of correctness or miscalibration.
**R8. Mechanism/failure:** Six Boston goals including Will Borgen empty-netter, compared with a frozen Boston mean of 3.329; both projected goalies (Swayman/Askarov) actually played. A high total defeated the Under while the Bruins ML won. Advanced chance-quality or player-contribution causal attribution stays `NOT_ASSESSABLE` where exact frozen source lacks the measurable field.
**R9. Cutoff/source/timing:** Actual starters and full lines were unconfirmed at the 14:17 late issue, despite final sheet/recap supporting them after the game. No numerical scenario was calibrated to measured goalie-start outcomes. Timing LATE_START_UNVERIFIED; issue 2026-10-14T14:17:28+11:00 after 14:00 scheduled. All terminal sources discovered after original issuance, not passed backwards as pregame information.
**R10. Process verdict:** DEFICIENT prospective timing/confirmed goalie gate; sporting grade is sound under NHL completed-game convention. Probability status `UNCALIBRATED_ANALYST_SCENARIO / NOT_CERTIFIED`; distinct from SPLIT outcome.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED`: Use NHL owner-sourced pregame goalie confirmations with timestamped xG/5v5 inputs; benchmark the paired winner-and-total distribution on the same line with event-blocked proper scores.
**R12. Disposition:** `MONITOR + PROPOSE_EXPERIMENT` only; retain frozen ranks/p; no model change, no new prediction, no GitHub write, no automatic training promotion; operator term and final-time capture remain open.
<!-- END SETTLEMENT P-589 revision-1 -->

## CARRIED CANONICAL RECORDS — evidence observations only, NO NEW SETTLEMENT REVISION
The source mini references P-581/P-582/P-583/P-584 as **already canonical and previously settled/observed**. Their original canonical card bytes and earlier revision chains were not part of this mini. Do not create a replacement rank, p, grade or `revision-2` from the queue excerpt. The following discoveries are **evidence leads for separate authorised correction**, not imported results:
- **P-584 Dragones Oaxaca vs Guerreros del Pacífico:** BeSoccer's updated club fixture listing displays **FT 5–1** on 12 Oct, but the club-owned calendar and results pages still expose pregame/through-R6 data; no official field-owner terminal sheet, HT result or match corners verified. Mark `TERMINAL_REPORTED_SECONDARY / OFFICIAL_TERMINAL_UNVERIFIED` (C); carry full-time goal/HT/corners and source discrepancy for a subsequent canonical revision; original canonical frozen rank table unavailable in this mini.
- **P-583 KT @ Samsung:** KBO official English scoreboard for 2026-10-12 now gives **KT 4–2 Samsung**, with innings KT 1,0,0,2,0,0,0,0,1 and SAMSUNG 0,1,0,0,0,0,0,0,1. It refutes the previously captured stale/cache 4–1 observation. `OWNER_EVIDENCE_FOUND`, original card NO_FORECAST, no retrospective candidate grade; an owner-backed correction must be made to its existing canonical settlement parent chain separately.
- **P-582 Liverpool vs Man City:** Manchester City club match centre provides corners Liverpool **5**, Man City **6**. This supports total 11 and resolves the external field value at B quality (subject to specific provider/operator definition). Existing canonical diagnostic-only; no local relabelling of its original grades.
- **P-581 Brøndby vs Lyngby:** DBU official game `556151_506118` verifies the 5–2 final but does not expose authenticated corner counts in consulted view. Earlier 8/4 secondary corners remain `UNRESOLVED_EVIDENCE`.
All four inherited cases require separate source/revision custody and/or missing operator conditions; none consumes an ID, expands the local five-card denominator, or modifies GitHub.


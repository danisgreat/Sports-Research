<!-- MINI-LOG-FORMAT: mini-log-10 -->
# Prediction Mini Running Log — 20261022F6K3OJNO

## A. Authority snapshot

| Field | Value |
|---|---|
| Authority mode | `LOCAL_WORKING_TREE` (ENV-v2) — branch `main`, base HEAD `29e25a798f7ed1947e890debd2507455e167c7eb`; this mini is committed together with the v23.0 framework change (CR-2026.10.22-R1), whose working files governed this run |
| Repository / branch / read HEAD | `danisgreat/Sports-Research` / `main` / base `29e25a798f7ed1947e890debd2507455e167c7eb`, read 2026-10-22T00:13+11:00 |
| Relevant working differences | The v23.0 control changes of this run (ENV-v2, MLSCOPE-v2, MINI-v2, RELEASE-SCOPE-v1); listed in research/verification/framework_change_2026-10-22-1/IMPLEMENTATION.md |
| Method / control / scoring / selection | `MDS-2026.10.22-v23.0` / `CR-2026.10.22-R1` / `SCV-2026.10.16-v11` / `SEL-2026.10.12-v3` |
| Prompt and format | `P-2026.10.22-v23.0` / `mini-log-10`, `ENV-v2`, `MINI-v2`, `MLSCOPE-v2`, `EXH-v1` |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_9.md` |
| Highest committed / next canonical ID | `P-622` / `P-623` — read-only snapshot for duplicate checks, not an allocation; reserved P-518–P-522 |
| Outstanding local minis and keys | Received 2026-10-22 and copied byte-for-byte under `research/active_minis/received/2026-10-22/`: **20261021OKCSASR01** (1 card, LOCAL-20261021OKCSASR01-G0001, unsettled; carried below with its original key and bytes) and **20261021T7K4R9F2** (0 cards; one in-chat tennis draft, transcribed below as G0001). Both are superseded by this mini for new work and consume nothing further. Legacy `research/active_minis/P-590_ONWARD/` is imported. `MINI LOGS TO BE SETTLED/` holds the 16–18 October minis already imported as P-601–P-622 on 21 October. |
| MINI_KEY / first local event key | `20261022F6K3OJNO` / `LOCAL-20261022F6K3OJNO-G0001` |
| New canonical ID / assignment stage | `NOT_ASSIGNED / PROMPT_4_IMPORT` — assigned only in each event's settlement phase (prompt 3 runs the prompt-4 import) |
| Issuing writer / lease start / expiry | Repository agent (Claude Code, owner's PC) / `2026-10-22T00:40+11:00` / `2026-10-29T00:40+11:00`, renewed on each committed append |
| Lease hand-overs | 20261021OKCSASR01 and 20261021T7K4R9F2 (external-chat minis, owner-supplied 2026-10-22) → this mini, by owner instruction "compile the next local mini log, and add these unsettled logs" |
| Frozen for settlement | NO |
| Reading receipt / opened at | 2026-10-22T00:13+11:00: CURRENT_STATE, CURRENT_RULES §0–§1, MINI_LOG_IDENTITY_PROTOCOL §§1–6, CARD_AND_LOG_TEMPLATES §2–§3, research/prompts/2_START_LOCAL_MINI, COMMON_OPERATING_PROTOCOL, GAME_LOG_STATUS_CURRENT current section, research/verification/mini_import_P-601_P-622_2026-10-21-1/CANONICAL_IMPORT_REPORT.md and UNRESOLVED_POST_IMPORT.md, research/verification/retrospective_2026-10-21/RETROSPECTIVE_REPORT.md, both received minis in full |
| Mode | `LOCAL_MINI_STAGING` · `LOCAL_WORKING_TREE` |

`SPORTS_ONLY / MARKET_BLIND` · `RESEARCH_ONLY_NOT_CERTIFIED` · `CANONICAL_IMPORT_STATUS: PENDING`

## B. Local ID rules

This mini consumes no canonical P-ID. New events take `LOCAL-20261022F6K3OJNO-G0001`, `-G0002` and so on; addenda and duplicates consume no ordinal. Cards carried from an earlier mini keep their original local key and bytes in the **Carried unsettled cards** section and consume no ordinal here. A canonical P-ID is assigned only in an event's settlement phase: prompt 3 settles it and then runs the prompt-4 import (MINI-v2). New cards are priced by the analyst first (ANALYST_PRIMARY_V1); the pregame model shadow runs only after the card is written and never changes it (MLSCOPE-v2).

## C. Carryover and evidence queue

**Pending events and evidence carried into this mini**

| ID | Event key | Queue | Original card / frozen pick table | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LOCAL-20261021OKCSASR01-G0001 | NBA 2026-27 · Oklahoma City Thunder @ San Antonio Spurs · 20 Oct US | PENDING_EVENT (scheduled 2026-10-21T12:30+11:00; final not checked here) | Carried card below (original bytes) | Original 2026-10-21; unsettled | Final score, regulation score, OT, final time; four half-point outcomes | Prompt 3 | NBA official game book / box score for game 0022600003; ESPN summary corroboration | At prompt 3 | UNKNOWN | None in this mini | NO |
| LOCAL-20261021OKCSASR01-G0001 | same | UNRESOLVED_EVIDENCE | Carried card | same | Confirmed starters and active bench, both teams; original pre-tip injury lists | Prompt 3 reviewer | NBA game book starters; official injury report versions before tip | At prompt 3 | n/a | Card holds projections only | NO |
| LOCAL-20261021OKCSASR01-G0001 | same | UNRESOLVED_EVIDENCE | Carried card | same | Operator definitions (full game incl. OT assumed) | Owner | Operator rules for ±1.5 and 229.5 | At prompt 3 | n/a | Not supplied | NO |
| LOCAL-20261021OKCSASR01-G0001 | same | UNRESOLVED_EVIDENCE | Carried card | same | Original issue time and actual first play; dated L20 rows | Prompt 3 reviewer | Original chat timestamp; NBA play-by-play first event | At prompt 3 | n/a | Card: request ~19 min after scheduled start | NO |
| LOCAL-20261022F6K3OJNO-G0001 | ATP Almaty R2 · Facundo Díaz Acosta v Nikoloz Basilashvili · 21 Oct | PENDING_EVENT (scheduled ~2026-10-21T19:00+11:00; final not checked here) | Card G0001 below (NOT_ISSUED draft) | Transcribed 2026-10-22 | Final set and game scores; retirement/walkover status | Prompt 3 | ATP match centre scorecard; independent scoreboard | At prompt 3 | UNKNOWN | None | NO |
| LOCAL-20261022F6K3OJNO-G0001 | same | UNRESOLVED_EVIDENCE | Card G0001 | same | Retirement/void rule for games handicap and total; original issue time | Owner | Operator terms; original chat timestamp | At prompt 3 | n/a | Not supplied | NO |
| LOCAL-20261022F6K3OJNO-G0002 | Prva Liga RS R12 · Potkozarje v Drina Zvornik · 2026-10-21 16:30 CEST (14:30Z) | PENDING_EVENT (card issued after kickoff; final not viewed) | Card G0002 below | Original 2026-10-22 | Regulation final, half-time score | Prompt 3 | FSRS round-12 results; Flashscore scores feed `GI2RuAdD` (dc/df_sui) as second lineage | At prompt 3 | UNKNOWN | None | NO |
| LOCAL-20261022F6K3OJNO-G0002 | same | UNRESOLVED_EVIDENCE | Card G0002 | same | Confirmed XI/bench both sides (LINEUP_UNCONFIRMED); officials | Prompt 3 reviewer | FSRS match report (`utakmice.html` page timed out at issue) | At prompt 3 | n/a | Full ladder done, nothing published | NO |
| LOCAL-20261022F6K3OJNO-G0002 | same | UNRESOLVED_EVIDENCE | Card G0002 | same | Corner count (supplied O/U 10.5 is NO_FORECAST; no provider publishes corners for this league) | Prompt 3 | Any field-owner match statistics; otherwise row stays UNRESOLVED | At prompt 3 | n/a | Flashscore stats feed empty for the league | NO |
| LOCAL-20261022F6K3OJNO-G0003 | NBA 2026-27 · Atlanta Hawks @ Orlando Magic · 2026-10-21 23:00Z (22 Oct 10:00 AEDT) | PENDING_EVENT (card issued after the scheduled start; final not viewed) | Card G0003 below | Original 2026-10-22 | Final score, regulation score, overtime, final time | Prompt 3 | NBA official box score; ESPN event 401909834 as second lineage | At prompt 3 | UNKNOWN | None | NO |
| LOCAL-20261022F6K3OJNO-G0003 | same | UNRESOLVED_EVIDENCE | Card G0003 | same | Official starting fives, bench and minutes; official referee assignment (starters rest on RotoWire alone) | Prompt 3 reviewer | NBA game book / box score starters and officials | At prompt 3 | n/a | NBA CDN refused; ESPN empty at 22:52Z; no post-start searches by design | NO |
| LOCAL-20261022F6K3OJNO-G0003 | same | UNRESOLVED_EVIDENCE | Card G0003 | same | Operator terms: overtime inclusion for ±2.5 and 233.5 (full game incl. OT assumed) | Owner | Operator rules | At prompt 3 | n/a | Not supplied | NO |
| LOCAL-20261022F6K3OJNO-G0004 | NBA2026-27 MIL Bucks @ WAS Wizards; NBA0022600086 / ESPN401909835; scheduled2026-10-21T23:00Z | PENDING_EVENT (late issue; target outcome not viewed) | Card G0004 below | Original 2026-10-21T23:16:19+00:00 | Final score, regulation score, OT, final time | Prompt3 | Official NBA game book; ESPN401909835 corroboration | At prompt3 | UNKNOWN | Not checked | NO |
| LOCAL-20261022F6K3OJNO-G0004 | same | UNRESOLVED_EVIDENCE | Card G0004 | 2026-10-21T23:16:19+00:00 | Operator OT/postponement/void terms | Prompt3 reviewer / owner | Owner/operator exact contract rules | At prompt3; fragile capture2026-10-23T22:00+11:00 | n/a | A3/A8 actual attempts, gap retained | NO |
| LOCAL-20261022F6K3OJNO-G0004 | same | UNRESOLVED_EVIDENCE | Card G0004 | 2026-10-21T23:16:19+00:00 | Independent starter-role corroboration and coach minutes/usage caps | Prompt3 reviewer / owner | Official game book and independent exact-game role record; projections remain assumptions | At prompt3; fragile capture2026-10-23T22:00+11:00 | n/a | A3/A8 actual attempts, gap retained | NO |
| LOCAL-20261022F6K3OJNO-G0004 | same | UNRESOLVED_EVIDENCE | Card G0004 | 2026-10-21T23:16:19+00:00 | Independent historical54-OT regulation-quarter corroboration and target firstplay time | Prompt3 reviewer / owner | Archived official quarter lines; NBA target firstplay timestamp at prompt3 | At prompt3; fragile capture2026-10-23T22:00+11:00 | n/a | A3/A8 actual attempts, gap retained | NO |
| LOCAL-20261022F6K3OJNO-G0005 | AHL 2026-27 · Hamilton Hammers @ Toronto Marlies · 2026-10-21 23:00Z (22 Oct 10:00 AEDT) | PENDING_EVENT (card issued after the scheduled start; final not viewed) | Card G0005 below | Original 2026-10-22 | Final score, regulation score, decision (regulation / overtime / shootout), final time | Prompt 3 | HockeyTech game centre `gamesummary` for game 1029174 (AHL field owner); an independent second source for corroboration | At prompt 3 | UNKNOWN | None | NO |
| LOCAL-20261022F6K3OJNO-G0005 | same | UNRESOLVED_EVIDENCE | Card G0005 | same | Starting goalies and dressed line-ups, scratches, both sides (unpublished before puck drop; no AHL injury report) | Prompt 3 reviewer | HockeyTech `gamesummary` goalies and `home_team_lineup`/`visitor_team_lineup` (available after the game) | At prompt 3 | n/a | Preview line-up field empty; no post-start searches by design | NO |
| LOCAL-20261022F6K3OJNO-G0005 | same | UNRESOLVED_EVIDENCE | Card G0005 | same | Operator terms for the moneylines: overtime/shootout included (R-A) or 60-minute regulation with a tie losing (R-B); totals at 5.5 are reading-proof | Owner | Operator rules | At prompt 3 | n/a | Not supplied; both readings frozen | NO |

**Canonical obligations (pointers only; they stay in their canonical records and receive no new ID)**

| ID | Event | Queue | Open field | Next source | Last attempt |
|---|---|---|---|---|---|
| P-584 | Dragones de Oaxaca v Guerreros del Pacífico, 12 Oct | PENDING_EVENT | Terminal state, FT/HT goals, corners | Liga Premier field-owner match sheet | 2026-10-21 import (still pending) |
| P-620 | South Africa v Australia, 2nd Test from 18 Oct | PENDING_WINNER_CALL (contracts terminal) | Test winner/draw and final time | ICC / Cricket Australia scorecard (result due about 23 Oct) | 2026-10-21 import |
| P-606 | NBA preseason Hornets @ Grizzlies | DATA_REPAIR_PROPOSED | Settlement score 116–98, not 117–98 (no grade change) | Retrospective 2026-10-21 F-01 captures | 2026-10-21 retrospective |
| P-604 | Olympique Akbou v ES Ben Aknoun | UNRESOLVED_EVIDENCE | Corners: single candidate source 8–5 = 13 (would grade Over 10.5 WIN) | Second independent corner source | 2026-10-21 retrospective F-02 |
| P-616 | PBA TNT v Converge | UNRESOLVED_EVIDENCE | Operator OT/push action for ±2.0 (grade-changing) | Operator terms | 2026-10-21 import |
| P-603 / P-619 | SC Delhi v Mohun Bagan / Machida v Avispa | UNRESOLVED_EVIDENCE | Corner corroboration; conflicting Machida count | Match-owner reports | 2026-10-21 import |
| LOCAL-20261018MELILL01-G0004 | Beijing Guoan v Qingdao West Coast | HELD_INTAKE_DEFECT (no canonical ID) | Orphan END CARD marker; source custody | Original source bytes | 2026-10-21 import |
| 20261016A691119714D1 package | Downloads settlement package | UNIMPORTED_PACKAGE | Inventory and import decision | Owner's Downloads copy | 2026-10-21 import report |

Open sporting events in this mini: 6 (G0004 and G0005 added 2026-10-22; all six remain due for prompt 3). No automation is scheduled.

## D. Request intake

| Request key | Received (ISO, tz) | Event / alias as requested | Disposition | Card or addendum pointer, or no-card reason |
|---|---|---|---|---|
| REQ-20261021-OKCSAS-ORIGINAL | 2026-10-21T12:49+11:00 (minute-level, from source mini) | OKC Thunder @ SA Spurs, NBA; Spurs +1.5 / Thunder −1.5 / Over 229.5 / Under 229.5 | CARRIED_CARD | LOCAL-20261021OKCSASR01-G0001 (carried, original bytes) |
| REQ-20261021-OKCSAS-APPEND | 2026-10-21T19:18+11:00 (from source mini) | Add the previous analysis as a card (external chat) | CARRIED_CARD | Same card; source mini 20261021OKCSASR01 |
| CHAT-20261021-TENNIS-DIAZ-BASIL | 2026-10-21T18:50+11:00 (from source mini) | Díaz Acosta v Basilashvili, ATP Almaty R2; ±2.5 games, O/U 22.5 games | CARD (NOT_ISSUED draft) | LOCAL-20261022F6K3OJNO-G0001 |
| CHAT-20261021-MINI-SETUP | 2026-10-21T19:21:45+11:00 (from source mini) | Start a mini that is updated after each request (external chat) | SUPERSEDED | Mini 20261021T7K4R9F2 (0 cards) superseded by this mini |
| REQ-20261022-COMPILE-NEXT-MINI | 2026-10-22T00:00+11:00 (approximate; owner request in the repository session) | "compile the next local mini log, and add these unsettled logs into the mini log" with both received minis | MINI_CREATED | This mini; 1 carried card, 1 new draft card |
| REQ-20261022-POTKOZARJE-DRINA | 2026-10-22T01:18+11:00 (approximate; owner request in the repository session) | Potkozarje vs FK Drina Zvornik, Bosnia & Herzegovina 1st League; owner estimate 21 Oct 1:10 PM AEDT; 1H O/U 0.5, FT O/U 2.5, corners O/U 10.5 | CARD | LOCAL-20261022F6K3OJNO-G0002 (official kickoff 01:30 AEDT 22 Oct; issued after kickoff) |
| REQ-20261022-HAWKS-MAGIC | 2026-10-22T09:50+11:00 (approximate; owner request in the repository session) | ATL Hawks @ ORL Magic, NBA regular season; owner estimate 22 Oct 10:10 AM AEDT; Hawks +2.5 / Magic −2.5 / Over 233.5 / Under 233.5 | CARD | LOCAL-20261022F6K3OJNO-G0003 (scheduled 10:00 AEDT per ESPN and the NBA report; issued after the scheduled start with pre-start inputs) |
| REQ-20261022-MIL-WAS | 2026-10-22 (request timestamp UNKNOWN; first source fetch09:51 AEDT) | MIL Bucks @ WAS Wizards, NBA regular season; estimate22Oct10:10AEDT; Bucks+4.5 / Wizards-4.5 / Over238.5 / Under238.5 | CARD, INFORMATION_INCOMPLETE, POST_SCHEDULED_START_ISSUE | LOCAL-20261022F6K3OJNO-G0004; official scheduled10:00AEDT; no settlement |
| REQ-20261022-HAMMERS-MARLIES | 2026-10-22T10:04:53+11:00 (owner request in the repository session; received 4 min 53 s after the scheduled start) | HAM Hammers @ TOR Marlies, AHL regular season; owner estimate 22 Oct 10:00 AM AEDT; Hammers ML / Marlies ML / Over 5.5 / Under 5.5 | CARD | LOCAL-20261022F6K3OJNO-G0005 (scheduled 10:00 AEDT per the AHL feed; issued after the scheduled start with pre-start inputs; prepared as G0004, recorded as G0005 after a key collision) |

# CARRIED UNSETTLED CARDS

The block below is copied byte-for-byte from `research/active_minis/received/2026-10-22/PREDICTION_MINI_RUNNING_LOG_20261021OKCSASR01.md`. It keeps its original key, wording, probabilities and timing labels. It is unsettled and has no canonical ID. **Model shadow:** NOT_RUN — carried in after the scheduled start, and there is no NBA release (MLSCOPE-v2 runs the shadow only for new cards, before the start).

<!-- BEGIN CARD LOCAL-20261021OKCSASR01-G0001 -->
## Card · LOCAL-20261021OKCSASR01-G0001 · BASKETBALL / NBA regular season · Oklahoma City Thunder @ San Antonio Spurs · 2026-10-20 (US) / 2026-10-21 (AEDT)

- **Local event key:** `LOCAL-20261021OKCSASR01-G0001` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED / PROMPT_4_IMPORT`.
- **Event key / native ID / aliases:** `NBA-20261020-OKC-SAS`; the previously cited NBA listing URL contains `0022600003` (not independently refetched during this repackaging); aliases Thunder @ Spurs, OKC @ SA.
- **Authority:** `MDS-2026.10.17-v22.2 / CR-2026.10.17-R6 / SCV-2026.10.16-v11 / SEL-2026.10.12-v3`, published `main` at `29e25a798f7ed1947e890debd2507455e167c7eb`; no owner working-tree differences verified.
- **Probability method:** `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`; preserve the **previous chat's** manual three-scenario normal mixture and the four percentages **without re-estimation**. This assembly is not the original pre-match issuance.
- **Learning record:** `LEARN_RECORD_INCOMPLETE` — prior analysis supplies aggregate L5/L10/L15/L20 values and source URLs but not dated independent 20-game source rows/publication receipts for both teams.
- **Future learning:** `PENDING_SETTLEMENT`; no outcome labels, model feedback, ingest or retrospective run.
- **Analysis status:** `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`, historical research transferred to this card; `RESEARCH_ONLY_NOT_CERTIFIED`.
- **Timing:** Scheduled 12:30 AEDT (the original request estimated 12:40); original chat request approximately 12:49 AEDT. Prior analysis acknowledged its late issue; exact original response timestamp/actual first play not verified. Card conversion 19:20 AEDT. Classification `POST_SCHEDULED_START / TIMING_UNVERIFIED`, `KNOWN_AT_UNVERIFIED`, no clean pre-start issuance claim.
- **Scheduled start:** `2026-10-20T20:30:00-05:00` (San Antonio CDT) = `2026-10-21T01:30:00Z` = `2026-10-21T12:30:00+11:00` AEDT, from the prior analysis's NBA official listing.
- **Scheduled lead / band:** Original request roughly 19 minutes *after* scheduled start; true issuance lead NOT_VERIFIED, actual first-play NOT_VERIFIED. No retrospective scoring is claimed.
- **Endpoint / definition:** Assumed **full game including NBA overtime** for handicap and points total, with zero pushes at all four half-point lines. Operator-specific terms `UNKNOWN_DEFINITION / NOT_OPERATOR_VERIFIED`.
- **Distribution object:** `ANALYST_PRIMARY_NORMAL_MIX_20261021_OKCSAS`: weights 0.25 / 0.50 / 0.25; total means 218.00 / 223.72 / 231.00, common within-case total SD 21.7; Spurs margin means −3.00 / +0.27 / +3.50, common within-case margin SD 16.4; qualitative dependence and exact OT mechanism not identified. **These are copied from previous chat, not newly validated/fitted.**
- **Expected score:** Previous unadjusted, home-adjusted physical centre OKC 113.78 / SAS 114.05 (total 227.84). The copied adjusted three-case mixture has weighted total ≈224.11, weighted Spurs margin ≈+0.26, corresponding arithmetic score centre **SAS ≈112.19 / OKC ≈111.93**, not an exact-score forecast. Marginal team SD/covariance not independently fitted; NOT_VERIFIED.
- **Baseline:** Prior analyst's `BASELINE_LEAGUE_V1` diagnostic approximately Under 229.5 = 0.529 and Spurs +1.5 = 0.578; complements Over 0.471, Thunder −1.5 0.422. The current card cannot verify a separately time-frozen baseline record before the scheduled start, so this comparator is **RECONSTRUCTED_DIAGNOSTIC / NOT_VERIFIED_PRESTART**.
- **Regime flags / context:** `EARLY_SEASON` NBA recommended historical multiplier 0.988 (once). Postseason/Finals scores noted for sensitivity but FINALS_COMPRESSION **not** applied to a regular-season fixture. San Antonio home court +1.71 margin reference. Roster integration and exact starters uncertain.
- **Settlement fields / capture plan:** Official NBA final team scores, total, signed margin and OT; grade all four half-point outcomes only when Prompt 3 is requested, with operator terms reviewed. Scheduled automation: NO.
- **Rules read / archive check:** Current GitHub `CURRENT_STATE`, `CURRENT_RULES`, `CARD_AND_LOG_TEMPLATES`, `MINI_LOG_IDENTITY_PROTOCOL`, `research/prompts/2_START_LOCAL_MINI`, `research/prompts/COMMON_OPERATING_PROTOCOL`, `GAME_LOG_STATUS_CURRENT`; previous chat additionally used `RULES_BASKETBALL`, `PROBABILITY_TOOLKIT`, `BASE_RATES_REGISTER`, `SELECTION_RULES`, `ROSTER_AVAILABILITY_PROTOCOL` and basketball Prompt 1; online form L5/L10/L15/L20 aggregates carried over, underlying row register incomplete.
- **Evidence receipt:** This card **transcribes the prior conversation analysis**. It does not assert fresh retrieval or timestamp-confirmed source publication in this turn. Source URLs and their described fields appear in A3/A8.
- **Known-at:** Pre-start publication of individual injury/lineup/form claims `NOT_INDEPENDENTLY_VERIFIED`; avoid classifying as CLEAN_PRE_START_INPUTS solely because a source page is dated game day.
- **Lineup state / issue step:** `LINEUP_UNCONFIRMED`: projections and reported medical absences only; latest exact-game confirmed starters/bench not obtained in previous answer. Converted to file after scheduled start with no late-result analysis.
- **Pricing basis:** `MIXTURE`, weights 0.25/0.50/0.25; uncertain scoring pace, offseason roster effects, unconfirmed lineups and prior playoff form.
- **Form windows:** See A3 for each team's previously reported L5/L10/L15/L20, true sample-size window counts 5/10/15/20 (overlapping). No distinct full source-row list accompanies these aggregates.

### Decision block

**Original forecast assessment preserved:** Under 229.5 led the four supplied outcomes but **failed the 62% Rank-1 floor**. Spurs +1.5 ranked second but **failed the 58% Rank-2 floor**. San Antonio was the marginal potential winner, not a strong favourite. This is an uncalibrated, late-issued analysis and not a high-confidence framework-approved slate.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P (diagnostic; not verifiably frozen) | Line distance from base centre / z | Probability basis | Main failure route |
|---|---|---|---|---:|---:|---:|---|---|---|
| **1** | PICK (weak; no gate PASS) | SUPPLIED | `NBA:FULL:TOTAL:UNDER:229.5:INCLUDING_OT` | **0.596** | 0.605 | ~0.529 | `229.5 − 223.72 = +5.78`; `z = +0.266` | Hand normal mixture | Higher-than-projected pace, efficient shooting, free throws or OT |
| **2** | PICK (below floor) | SUPPLIED | `NBA:FULL:SPURS:+1.5:INCLUDING_OT` | **0.542** | 0.543 | ~0.578 | Cover threshold Spurs margin `−1.5`; `−1.5 − 0.27 = −1.77`; `z = −0.108` | Same margin mixture | Thunder win by ≥2 behind defensive efficiency and star creation |
| 3 | INFORMATIONAL | SUPPLIED | `NBA:FULL:THUNDER:−1.5:INCLUDING_OT` | 0.458 | 0.457 | ~0.422 | Complement of Spurs +1.5 | Same margin mixture | Spurs win or OKC win by exactly 1 |
| 4 | INFORMATIONAL | SUPPLIED | `NBA:FULL:TOTAL:OVER:229.5:INCLUDING_OT` | 0.404 | 0.395 | ~0.471 | Complement of Under | Same total mixture | Slower offensive possessions or lower conversion |

**Baseline coverage:** 4/4 numerically approximated from the prior analytical comparator, but **0/4 independently evidenced as pre-start frozen baselines**. Not valid as verified paired-skill baselines.

**Rank-1 gate:** `RANK1_UNSTABLE`. Rank 1 = 0.596 < 0.620 required; best eligible non-complementary alternative among the supplied set = Spurs +1.5 at 0.542; gap 0.054 > 0.040. The absolute floor fails regardless. Calculation-table tolerance ≈0.002 per row; parameter uncertainty is greater. A wider independently generated candidate universe was not exhaustively repriced, so the *full-universe* gate is `NOT_FULLY_ASSESSABLE`.

**Rank-2 floor:** `BELOW_FLOOR` (0.542 < 0.580).

**Joint failure:** Under loses if total ≥230; Spurs +1.5 loses if Spurs margin ≤−2. Their marginal losing masses are ~0.404 and ~0.458. Without an identified joint total/margin dependence distribution, Fréchet bound `max(0, 0.404+0.458−1)=0` to `min(0.404,0.458)=0.404`; **exact joint loss NOT_COMPUTED**, no independence assumption or claimed diversification benefit.

**Shadow gate / Rank 2:** RET03 different-quantity alternative Spurs +1.5 = 0.542; same Rank-1 floor failure. RET04 alternative with p≥0.58 on different quantity: NONE among supplied rows. XCARD6 eligible non-Rank-1 with p≥0.58: NONE. These are non-primary diagnostic statuses, not model runs.

**Shadow RANK_DELTA / BASE_ONLY:** If using the **unverified diagnostic** baseline above, deltas are Under +0.067, Thunder −1.5 +0.036, Spurs +1.5 −0.036 and Over −0.067; candidate delta ordering would be Under then Thunder −1.5, **NOT_PRIMARY / not a frozen verified shadow**. Base-only supplied order: Under (0.605), Spurs +1.5 (0.543), Thunder −1.5 (0.457), Over (0.395). Base-only Rank 1 still below 0.62. No model/shadow has been executed.

**Adjustment dependence:** Unadjusted home-adjusted centre = 227.84 total, Spurs +0.27; adjusted central total = 223.72. The total adjustment strengthens Under, but no unadjusted probabilities were frozen and issued. `ADJUSTMENT_DEPENDENT` as an uncertainty flag; no unsupported size-of-advantage claims.

**Potential winner:** **San Antonio Spurs ~0.506; Oklahoma City Thunder ~0.494** (unconditional two-way final-winner approximation, including NBA overtime). Not a high-confidence call.

**Supplied rows not selected as primary:** Thunder −1.5 (0.458) and Over 229.5 (0.404), informational exactly complementary to higher-ranked rows. No alternative player/team props manufactured.

### Appendix

#### A1. Identity, timing and state

- Competition: NBA **2026–27 regular season**; event Thunder at Spurs, opening night; Frost Bank Center, San Antonio, Texas.
- Original estimated start from owner: `2026-10-21 12:40 PM AEDT`; prior analysis's official-source claim: `12:30 PM AEDT` (20 October 2026 20:30 CDT in San Antonio).
- Original user request was after scheduled start (conversation-local time around 12:49 AEDT). Analysis continued; an exact original response issue timestamp and verified actual first play were not established.
- This card was **assembled later** (21 October 2026 ~19:20 AEDT) from existing conversation content. It is not a newly initiated pre-game forecast. Do not promote into a `PREGAME_ISSUED` or `CLEAN_PRE_START_INPUTS` cohort without impossible/unsupported timing reconstruction.
- Source status: **no target live score, realised box stats or final result were intentionally included in this migrated analysis**. Actual exposure audit cannot be independently reconstructed and is marked `KNOWN_AT_UNVERIFIED`; settlement untouched.
- Exact official NBA game listing originally given: https://www.nba.com/spurs/game/0022600003-thunder-vs-spurs-san-antonio-tx-10-20-2026 . Native game ID is inferred from this cited URL only, not newly cross-checked.
- Duplicate check: in `main` at pinned HEAD, repository code search for Thunder–Spurs 2026-10-20 returned no matching file. An unpublished local mini or other writer's record was not available to exclude independently.

#### A2. Frozen supplied contracts and candidate recipe

| Exact owner-supplied wording | Normalized quantity | Direction | Contract/definition status |
|---|---|---|---|
| `Spurs +1.5` | Spurs final margin | Spurs margin ≥−1 (equivalently final margin >−1.5) | Full game with OT **assumed**, not operator verified |
| `Thunder -1.5` | Thunder final margin | Thunder win by ≥2 | Complementary to Spurs +1.5 under same rules |
| `Combined Total: Over 229.5 Points` | Full-game combined points | ≥230 | Includes OT **assumed**, not operator verified |
| `Combined Total: Under 229.5 Points` | Full-game combined points | ≤229 | Complementary to Over 229.5 under same rules |

Candidate universe frozen here to the **four supplied rows only** because this card transfers the previous answer and does not create or reprice additional props. The earlier response ranked all four by its coherent mixture; no player props were asserted. All half-point contracts have `PUSH=0`, `VOID=0` under the assumed operator definition; any later operator-specific exception is an evidence correction, not a silent edit.

#### A3. Evidence and historical inputs from the previous analysis

**2025–26 regular-season baselines cited previously:**

| Metric | Oklahoma City Thunder | San Antonio Spurs |
|---|---:|---:|
| Record | 64–18 | 62–20 |
| Points for/game | 119.0 | 119.8 |
| Points against/game | 107.9 | 111.5 |
| Offensive rating per 100 possessions | 118.9 | 119.6 |
| Defensive rating per 100 possessions | 107.7 | 111.3 |
| Pace | 99.3 | 99.9 |
| Net rating | +11.2 | +8.3 |

**Overlapping last completed competitive-game windows from previous answer** (previous season regular season/postseason, not 2026–27 preseason; postseason opponent/regime effect noted):

| Team | Window | True n | W–L | Points for/game | Points against/game | Total/game |
|---|---|---:|---|---:|---:|---:|
| Thunder | L5 | 5 | 2–3 | 105.2 | 110.8 | 216.0 |
| Thunder | L10 | 10 | 6–4 | 113.4 | 111.4 | 224.8 |
| Thunder | L15 | 15 | 11–4 | 115.5 | 108.4 | 223.9 |
| Thunder | L20 | 20 | 14–6 | 117.0 | 109.8 | 226.8 |
| Spurs | L5 | 5 | 1–4 | 102.0 | 104.4 | 206.4 |
| Spurs | L10 | 10 | 4–6 | 106.4 | 104.8 | 211.2 |
| Spurs | L15 | 15 | 7–8 | 111.5 | 107.0 | 218.5 |
| Spurs | L20 | 20 | 11–9 | 112.6 | 105.0 | 217.6 |

**Window limitations:** The L5/L10/L15/L20 windows overlap; they are not 100 independent observations. Spurs' last five were described as NBA Finals games versus New York, materially changing opponent and pace conditions. Oklahoma City's last 15 were described as playoff games, and the last five repeated San Antonio matchups. The earlier analysis asserted that San Antonio won the seven-game 2026 Western Conference Finals 4–3. These claims are **transcribed rather than independently reverified now**. No game-by-game dated rows, regulation scores, publication timestamps or source-independence ledger were supplied in the original response; LEARN_RECORD_INCOMPLETE.

**Personnel: projected, not confirmed.** The previous analysis listed:

| Role | Oklahoma City (projected) | San Antonio (projected) |
|---|---|---|
| Guard 1 | Shai Gilgeous-Alexander | De'Aaron Fox |
| Guard 2 | Cason Wallace | Stephon Castle |
| Wing | Jalen Williams | Dylan Harper **or** Julian Champagnie (conflicting projections) |
| Forward | Chet Holmgren | Devin Vassell |
| Centre | Isaiah Hartenstein | Victor Wembanyama |

**Reported absences in previous answer, not rechecked as of this artifact's generation:** Thunder Nikola Topić (back), Thomas Sorber (knee), Otega Oweh (Achilles); Spurs Tobias Harris (calf), Jayden Quaintance (knee). The answer described SGA, Chet Holmgren and Jalen Williams as available but **did not establish a full exact-game officially confirmed active/bench list**. It mentioned Alex Caruso/Aday Mara as expected Thunder reserves and Keldon Johnson/Julian Champagnie as anticipated Spurs rotation options. The reported effects of offseason departures such as Lu Dort, Aaron Wiggins and Isaiah Joe motivated additional uncertainty rather than a sourced numerical roster penalty. No fabricated confirmed starts.

**Primary team-source URLs from the original answer:**

- NBA official game page: https://www.nba.com/spurs/game/0022600003-thunder-vs-spurs-san-antonio-tx-10-20-2026
- 2025–26 OKC team page: https://www.basketball-reference.com/teams/OKC/2026.html
- 2025–26 SAS team page: https://www.basketball-reference.com/teams/SAS/2026.html
- OKC dated advanced game log: https://www.basketball-reference.com/teams/OKC/2026/gamelog-advanced/
- SAS dated advanced game log: https://www.basketball-reference.com/teams/SAS/2026/gamelog-advanced/
- NBA 2026 playoffs: https://www.basketball-reference.com/playoffs/NBA_2026.html

#### A4. Distribution, baseline, score arithmetic and sensitivity

**Previous centre calculation, transcribed:**

1. Average pace: `(99.3 + 99.9)/2 = 99.6` possessions.
2. OKC vs SAS efficiency centre: `99.6 × (118.9 + 111.3) / 200 = 114.64` points.
3. SAS vs OKC efficiency centre: `99.6 × (119.6 + 107.7) / 200 = 113.20` points.
4. Unadjusted combined centre `227.84`. San Antonio home margin edge `+1.71`, allocated `+0.855` SAS / `−0.855` OKC, yields OKC `113.78`, SAS `114.05`, margin approximately SAS `+0.27`.
5. NBA opening-game multiplier in the prior repo baseline: `0.988 × 227.84 ≈ 225.10`. Prior L20 combined averages were OKC `226.8` vs regular season `226.9` (−0.1), Spurs `217.6` vs regular season `231.3` (−13.7). Subjective 20% average-difference shrinkage: `0.20 × [(−0.1 −13.7)/2] ≈ −1.38`. Base total `225.10 − 1.38 ≈ 223.72`.
6. Previous analysis's three scenarios (low/base/high) weighted `0.25/0.50/0.25`:

| Scenario | Weight | Total mean μT | Spurs signed margin mean μM | Width σT | Width σM |
|---|---:|---:|---:|---:|---:|
| Low scoring / OKC edge | 0.25 | 218.00 | −3.00 | 21.7 | 16.4 |
| Base | 0.50 | 223.72 | +0.27 | 21.7 | 16.4 |
| Higher scoring / SAS edge | 0.25 | 231.00 | +3.50 | 21.7 | 16.4 |

Widths 21.7 and 16.4 came from **raw** prior NBA 2025–26 SDs rather than narrower residual widths 19.4/15.1. No opponent-fitted conditional variance was claimed. The score arithmetic alone cannot produce an empirically verified total–margin covariance; a precise joint distribution is unavailable.

**Original normal-CDF calculations:**

- `P(Under 229.5) = Σ w_i Φ((229.5−μTi)/21.7)` = `0.25×0.702 + 0.50×0.605 + 0.25×0.472 ≈ 0.596`.
- `P(Spurs +1.5) = Σ w_i Φ((1.5+μMi)/16.4)` = `0.25×0.464 + 0.50×0.543 + 0.25×0.620 ≈ 0.542`.
- `P(Over 229.5) ≈ 0.404`; `P(Thunder −1.5) ≈ 0.458`, exact complements conditional on the assumed rules.
- `P(Spurs win) = 0.25×0.427 + 0.50×0.506 + 0.25×0.585 ≈ 0.506` with an approximate normal-no-tie final-winner calculation. `P(Thunder win) ≈ 0.494`.
- Base-only probabilities: Under ≈0.605, Spurs +1.5 ≈0.543, Thunder −1.5 ≈0.457, Over ≈0.395.
- Weighted mixture score centre: `0.25×218 + 0.50×223.72 + 0.25×231 = 224.11`; weighted Spurs margin `0.25×(−3) + 0.50×0.27 + 0.25×3.5 = 0.26`. Implied SAS `(224.11+0.26)/2 ≈112.19`, OKC `(224.11−0.26)/2 ≈111.93`. This is a derived expectation, **not** a new forecast or an empirical fitted model.

**Same-line league-only comparator (unverified frozen status):** NBA 2025–26 mean total 230.7; early multiplier 0.988 gives `230.7 ×0.988 = 227.9316`, raw total SD 21.7 → Under 229.5 ≈ `Φ((229.5−227.9316)/21.7)` = 0.529. League home edge +1.71; raw margin SD 16.4 → Spurs +1.5 ≈ `Φ((1.5+1.71)/16.4)` = 0.578. Complements are 0.471 and 0.422. These are **diagnostic recreation**, not proof of original baseline freezing.

**Sensitivity from earlier answer:** Low total centre 218 → Under 70.2%; base 223.72 → 60.5%; high 231 → 47.2%; weighted 59.6%. Interpretation: lower-scoring defensive/pacing regimes support Under, but an offensive reset reverses that preference. These are scenarios, not confidence intervals.

**Endpoint simplification:** Historical total distribution contains observed NBA OT games; no fresh +25-point OT correction was added. The exact regulation-tie mass and OT transition were **not** enumerated, and probability numbers must not be presented as an exact discrete/OT model.

#### A5. Full supplied contract assessment; W/P/L/V

The four rows are half-point lines and mutually complementary by family under the stated **conditional full-game+OT** operator assumption. All values below are **copied from the prior analysis**, with no new reranking.

| Contract | W unconditional | P unconditional | L unconditional | V unconditional | Denominator W+L | p_card | Assessment and failure mode |
|---|---:|---:|---:|---:|---:|---:|---|
| Under 229.5 | 0.596 | 0 | 0.404 | 0 | 1.000 | 0.596 | Best supplied direction; loses if fast, efficient game reaches 230+ |
| Spurs +1.5 | 0.542 | 0 | 0.458 | 0 | 1.000 | 0.542 | Marginal home-court lean; loses if Thunder win by ≥2 |
| Thunder −1.5 | 0.458 | 0 | 0.542 | 0 | 1.000 | 0.458 | OKC defence/SGA upside; opposite of Spurs +1.5 |
| Over 229.5 | 0.404 | 0 | 0.596 | 0 | 1.000 | 0.404 | Opposite of Under; needs high scoring, potentially OT |

**Accounting:** Under + Over = 1.000; Spurs +1.5 + Thunder −1.5 = 1.000; NBA final has no tied winner after permitted overtime. W/L are unconditional outcome probabilities *under the assumed game contract*, not verified market action. Expected value against a price **NOT_COMPUTED** because no contract price was provided and market data are excluded by SPORTS_ONLY; do not confuse win probability with expected financial return.

#### A6. Adjustments, regimes and unadjusted comparison

| Driver | Direction/quantity | Basis/status | Effect and uncertainty |
|---|---|---|---|
| Exact competition regular-season offensive/defensive efficiencies | Total 227.84; OKC 114.64 / SAS 113.20 before home edge | Prior 2025–26 season stats; simplified pace × average efficiencies | Older roster; not opponent/schedule fitted |
| Home venue | SAS expected margin +1.71 | Prior GitHub NBA league benchmark | Splits +0.855 SAS, −0.855 OKC, leaves total unchanged |
| NBA opening-season regime | Multiply total ×0.988 once | Prior GitHub NBA 25-season early-season multiplier | Total 227.84 →225.10 |
| L20/Finals carryover | Total adjustment −1.38 | **Subjective** 20% shrinkage of cross-team L20-vs-season total differential | Total 225.10 →223.72; main discretionary lever; postseason is not directly portable |
| Injury/rotation | No additional numerical shift | Exact confirmed starts/minute effects unavailable | Preserved in mixture uncertainty, not double-counted |
| Rest/travel | 0 adjustment | First regular-season matchup; detailed pregame travel/rest not documented here | No fabricated measured fatigue effect |
| Offensive reset/roster uncertainty | Low/base/high case means and 0.25/0.50/0.25 weights | Unfitted analyst sensitivity | Total preferences switch between 218 and 231 centres |

Unadjusted expected total 227.84 would give a smaller Under lean than the adjusted 223.72 centre, using the same SD. The earlier answer did not freeze an unadjusted four-row probability table; do not fabricate it in this card. A large speculative lineup adjustment might reverse the margin ordering; because no confirmed starter/bench verification was present, the Spurs +1.5 signal is explicitly fragile.

#### A7. Family rules, dependence and shadow status

- **P4:** Supplied contracts are reference choices, not evidence from odds. Four supplied rows only, no manufactured additional market thresholds, no player props.
- **T2:** Only Ranks 1/2 would enter primary outcome evaluation **if** original issuance/valid cohort is later established; no event settlement or credit given now.
- **R1:** Deep Rank-1 failure review deferred unless a later authorised settlement establishes a Rank-1 loss; retrospective NOT_PERFORMED.
- **Rank ceiling 0.90:** No selected probability exceeds the ceiling.
- **Rank-1 gate:** fails 0.62 absolute floor; supplied-universe gap passes 0.04, but full eligible universe not independently priced.
- **Rank-2 floor:** fails 0.58. This is a weak slate, not a forced strong selection.
- **Dependence:** Both contract pairs are complements; Under and Spurs +1.5 derive from total and margin of the same game. Dependence/joint failure not explicitly calculated; Fréchet bounds only (0–0.404).
- **RET03/RET04/XCARD6:** see Decision block; conditional rankings are documentary diagnostics only.
- **RANK_DELTA:** prior-baseline-derived suggestion Under then Thunder −1.5 is not a valid frozen verified independent shadow; preserve it only as diagnostic arithmetic.
- **No ML/RL:** no trained model, simulated sample, model shadow, run receipt, calibration, predictive certification or market decision lab used.

#### A8. Source register, provenance, gaps and capture/refresh plan

**This card is a transcription of the immediately preceding ChatGPT research answer.** It retains source URLs and conclusions rather than pretending to have re-researched a game that was already scheduled to start. Previous turn's tool-specific citation IDs and precise web publication times were not portable to a standalone Markdown card. Links below identify the prior **reported** source routes, not new fetches.

| Evidence topic | Source route from previous analysis | Claimed field | Current verification disposition |
|---|---|---|---|
| Fixture, start and venue | https://www.nba.com/spurs/game/0022600003-thunder-vs-spurs-san-antonio-tx-10-20-2026 | Thunder @ Spurs; 20 Oct US; 12:30 AEDT | Prior-chat reported; exact actual first play NOT_VERIFIED |
| OKC previous season | https://www.basketball-reference.com/teams/OKC/2026.html | Record, PF/PA, ORtg/DRtg, pace | Prior-chat reported; full capture receipt unavailable |
| SAS previous season | https://www.basketball-reference.com/teams/SAS/2026.html | Record, PF/PA, ORtg/DRtg, pace | Prior-chat reported; full capture receipt unavailable |
| Prior OKC games | https://www.basketball-reference.com/teams/OKC/2026/gamelog-advanced/ | L5/L10/L15/L20 aggregations | Aggregates retained; dated rows not transferred |
| Prior SAS games | https://www.basketball-reference.com/teams/SAS/2026/gamelog-advanced/ | L5/L10/L15/L20 aggregations | Aggregates retained; dated rows not transferred |
| NBA postseason | https://www.basketball-reference.com/playoffs/NBA_2026.html | 2026 playoff progression and matchup | Original research reported; not independently reopened |
| SAS lineup and absences | https://www.expressnews.com/sports/spurs/article/san-antonio-spurs-okc-thunder-how-to-watch-22482941.php | Reported projections/injuries | Projected ≠ confirmed; source publication time unknown |
| OKC injuries | https://www.aol.ca/articles/full-injury-report-tuesdays-thunder-130111000.html | Medical absence reports | Source independence and prestart known-at not verified |
| Supplemental injury report | https://sports.iheart.com/content/2026-10-20-thunder-vs-spurs-injury-report-oct-20/ | Injury listing corroboration | Same-day version/capture time not verified |
| Current framework | https://github.com/danisgreat/Sports-Research/tree/main | Control revisions and local-mini rules | GitHub HEAD pinned and actively checked for this card assembly |

**Required open fields for future independent evidence verification (without changing historical card ranks):** exact game-book starters and bench (both teams), the pre-tip original-version injury lists, signed final/actual start timestamps, independent dated L20 row coverage with true n, operator handicap/total terms, observed roster-minute availability, source-lineage independence and source-publication metadata. A future source correction should be a dated addendum, not a retrospective alteration of this copied original. Automated checking: NONE scheduled.

**Research assessment:** the prior game investigation addressed fixture, the major players, injuries, team statistics, both sides' aggregate four form windows, simple tempo/efficiency adjustment, four contracts, sensitivity and likely winner. It did not provide independently auditable confirmed rosters or per-game/source-time historical rows. `INFORMATION_INCOMPLETE`, not `COMPLETE`.

#### A9. Integrity, scope and completion receipt

| Required procedure | Status | What is actually evidenced / missing |
|---|---|---|
| Authority, identity and published main SHA | DONE for GitHub current authority | Pinned HEAD; native ID based on previously cited source URL |
| Existing mini/duplicate/lease reconciliation | PARTIAL | Published repo searched, no matching file discovered; owner's unpublished minis and issuing leases not accessible |
| Official scheduled start and zone conversion | DONE for previously reported schedule | 12:30 AEDT / 20:30 CDT; actual first play not proven |
| Timing, original issue and pre-start known-at | INCOMPLETE | Original request was after scheduled time; original response timestamp and pre-start version of evidence unavailable |
| Both-side confirmed starters | INCOMPLETE | Only projected starting fives |
| Both-side active bench and absence/medical evidence | INCOMPLETE | Named reports, but exact official active bench/late changes not confirmed |
| Both-side L5/L10/L15/L20 and season comparisons | PARTIAL | Aggregate n, W/L and PF/PA transferred; no dated row/source-reconciliation ledger |
| Basketball rules, full-game endpoint and OT | PARTIAL | NBA overtime convention assumed; operator terms not verified; exact discrete OT transition not modelled |
| Single coherent family, inputs and arithmetic | PARTIAL | All four marginal calculations reproduced from same low/base/high normal mixture; exact total–margin covariance/joint distribution unavailable |
| Four supplied contract assessments and ranks | DONE as TRANSCRIPTION | Four original probabilities, two complements, failure mechanisms preserved |
| Same-line league-only comparator | PARTIAL | Diagnostic arithmetic supplied; actual pre-start comparator freeze unverified |
| Family gate, dependence and sensitivities | PARTIAL | Rank-1/Rank-2 failure established; exact joint failure and full alternative universe unavailable |
| A1–A9 card assembly and local readback | DONE for this standalone file after verification | New card produced, no original active mini overwritten; readback check recorded below |
| Settlement, retrospective, canonical import, GitHub writes | NOT_PERFORMED (as requested) | No grades/retrospective, no canonical ID, no GitHub write |

**Overall:** `INFORMATION_INCOMPLETE` · `LEARN_RECORD_INCOMPLETE` · `READ_ONLY_SOURCE_REPACKAGING / LOCAL_MINI_STAGING` · `NOT_VERIFIED_PREGAME_ISSUE` · `UNCALIBRATED_ANALYST_PRIMARY`.

**Custody and marker audit:** One new local event card `LOCAL-20261021OKCSASR01-G0001` is placed before the running footer. Original file was an instruction prompt, so no prior mini card was claimed to be preserved. Source probabilities were not revised: 0.596 / 0.542 / 0.458 / 0.404; winner Spurs 0.506. Future event key is G0002. Any owner-side unpublished duplicate requires reconciliation prior to canonical import.

`SPORTS_ONLY_MARKET_BLIND: APPLIED` · `OUTCOME_EXPOSURE: NOT_VERIFIED_IN_SOURCE_PROVENANCE; no target live/final outcome used in repackaging` · `SETTLEMENT: NOT_PERFORMED` · `RETROSPECTIVE: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING`
<!-- END CARD LOCAL-20261021OKCSASR01-G0001 -->

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD LOCAL-20261022F6K3OJNO-G0001 -->
## Card · LOCAL-20261022F6K3OJNO-G0001 · TENNIS / ATP 250 Almaty R2 · Facundo Díaz Acosta v Nikoloz Basilashvili · 21 Oct 2026

- **Local event key:** `LOCAL-20261022F6K3OJNO-G0001` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** NOT_ASSIGNED / PROMPT_4_IMPORT (settlement phase).
- **Event key / native ID / aliases:** `ATP-ALMATY-2026-R2-DIAZACOSTA-BASILASHVILI`; native ID NOT_VERIFIED; aliases Díaz Acosta v Basilashvili.
- **Card class:** READ_ONLY_DRAFT / NOT_ISSUED. Transcribed on 2026-10-22 from §D1 of the owner-supplied mini 20261021T7K4R9F2, which recorded an external chat's analysis and said it was not an issued card. Carried here on the owner's instruction so it can be settled. It is settled only in the NOT_ISSUED draft stratum, never in primary counts.
- **Analysis status:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY (draft values as recorded; not re-estimated)
- **Probability method:** Four set-score branches from the source draft, Basilashvili 2–0 0.35, Basilashvili 2–1 0.21, Díaz Acosta 2–0 0.27, Díaz Acosta 2–1 0.17 (sum 1.00), with hand-priced game totals and handicaps inside each branch. The source calls this a rough scenario calculation, not a fitted joint set-score distribution; the within-branch game arithmetic was not recorded.
- **Timing:** Request 2026-10-21T18:50+11:00; scheduled about 2026-10-21T19:00+11:00 (owner estimate; source feeds conflicted). Original response time NOT_VERIFIED. Transcribed after the scheduled start. `TIMING_UNVERIFIED`, `KNOWN_AT_UNVERIFIED`; no pre-start issue claim.
- **Endpoint / definition:** Completed best-of-three match; games handicap and total games. Retirement/void action UNKNOWN_DEFINITION.
- **Baseline:** BASELINE_P NOT_RECORDED_IN_SOURCE_DRAFT for every row.
- **Lineup state:** Participation and fitness not officially confirmed in the source; Basilashvili's recent retirements were noted as added uncertainty.
- **Learning record:** LEARN_RECORD_INCOMPLETE (no dated prior-match rows were transferred).
- **Model shadow:** NOT_RUN — no tennis release in the forecast cycle, and the card was transcribed after the scheduled start.

### Decision block

The source draft found no row that reached the framework floors (Rank 1 0.577 < 0.62; Rank 2 0.523 < 0.58): **no qualifying high-probability selection**.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---:|---|---|---|---|---|
| 1 | PICK (draft; below gate) | SUPPLIED | Díaz Acosta +2.5 games, completed match | 0.577 (0.5768) | NOT_RECORDED | NOT_RECORDED_IN_SOURCE_DRAFT | N/A | Set-branch scenario | Basilashvili wins comfortably in straight sets |
| 2 | PICK (draft; below floor) | SUPPLIED | Under 22.5 total games | 0.523 (0.5226) | NOT_RECORDED | NOT_RECORDED_IN_SOURCE_DRAFT | N/A | Set-branch scenario | Three sets or tie-breaks push the total to 23+ |
| 3 | INFORMATIONAL | SUPPLIED | Over 22.5 total games | 0.477 (0.4774) | NOT_RECORDED | NOT_RECORDED_IN_SOURCE_DRAFT | N/A | Complement of Under | Two quick sets |
| 4 | INFORMATIONAL | SUPPLIED | Basilashvili −2.5 games | 0.423 (0.4232) | NOT_RECORDED | NOT_RECORDED_IN_SOURCE_DRAFT | N/A | Complement of Díaz Acosta +2.5 | Close match or Díaz Acosta win |

**Baseline coverage:** 0/4 (NOT_RECORDED_IN_SOURCE_DRAFT).
**Rank-1 gate:** RANK1_UNSTABLE (0.577 < 0.62).
**Rank-2 floor:** BELOW_FLOOR (0.523 < 0.58).
**Joint failure:** NOT_COMPUTED in the source; Fréchet bounds max(0, 0.423 + 0.477 − 1) = 0 to min(0.423, 0.477) = 0.423.
**Potential winner:** Basilashvili 0.56; Díaz Acosta 0.44 (from the set branches: 0.35 + 0.21 and 0.27 + 0.17).
**Supplied rows not selected:** Over 22.5 (0.477) and Basilashvili −2.5 (0.423), informational complements.

### Appendix

#### A1. Identity, timing and state
ATP 250 Almaty, round 2, indoor hard, best of three, 21 October 2026. Scheduled about 19:00 AEDT (08:00 UTC) per the owner; source feeds conflicted. Duplicate check: no canonical or local record of this match in Parts 1–9 or `research/active_minis/` at 2026-10-22T00:30+11:00.

#### A2. Supplied contracts
Díaz Acosta +2.5 games; Basilashvili −2.5 games; Over 22.5 combined games; Under 22.5 combined games. Retirement, walkover and tie-break-game counting rules: UNKNOWN_DEFINITION (queued).

#### A3. Evidence carried from the source draft
Basilashvili's indoor form and qualifying wins supported the winner lean; Díaz Acosta's first-round win over Tirante supported competitiveness and a small plus-games lean; recent Basilashvili retirements widened uncertainty. Sources named in the draft (leads, not re-opened here): ATP Almaty, Tennis.com, Tennis Abstract, Tennislive, TNT Sports.

#### A4–A7. Distribution, contracts and dependence
Only the four set-branch masses and the four row probabilities above were recorded. Within-branch game distributions, the total and handicap arithmetic and any baseline were not recorded; they are NOT_RECONSTRUCTED rather than invented.

#### A8. Gaps
Exact source timestamps, a result-state check at issue, independent historical rows, official participation and fitness, operator retirement terms, a reproducible joint distribution and a baseline.

#### A9. Completion receipt
| Procedure | Status |
|---|---|
| Identity and duplicate check | DONE (local and canonical search) |
| Timing and known-at | INCOMPLETE (issue time not verified; transcribed after start) |
| Online history and players | INCOMPLETE (not transferred) |
| Distribution and arithmetic | PARTIAL (branch masses and row values only) |
| Baseline | NOT_RECORDED |
| Model shadow | NOT_RUN (no tennis release; post-start) |
| Settlement / import | NOT_PERFORMED (prompt 3) |

`SPORTS_ONLY_MARKET_BLIND: APPLIED` · `CARD_CLASS: READ_ONLY_DRAFT / NOT_ISSUED` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD LOCAL-20261022F6K3OJNO-G0001 -->

<!-- BEGIN CARD LOCAL-20261022F6K3OJNO-G0002 -->
## Card · LOCAL-20261022F6K3OJNO-G0002 · SOCCER / Prva Liga Republike Srpske 2026/27, round 12 · FK Potkozarje (Aleksandrovac) v FK Drina (Zvornik) · 21 Oct 2026

- **Local event key:** `LOCAL-20261022F6K3OJNO-G0002` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** NOT_ASSIGNED / PROMPT_4_IMPORT (settlement phase).
- **Event key / native IDs / aliases:** `PRS-2026-27-R12-POTKOZARJE-DRINA`; Flashscore/Soccerway match id `GI2RuAdD`; FSRS COMET round 12 fixture (match page ids 54170914–54170918 listed, page timed out); aliases Potkožarje v Drina Zvornik, ФК Поткозарје v ФК Дрина.
- **Authority:** `LOCAL_WORKING_TREE`, branch `main`, HEAD `2f6139e01137f4fe7f8d1a575f1736d651b0b933`, no uncommitted control changes at read (2026-10-22T01:20+11:00). MDS-2026.10.22-v23.0 / CR-2026.10.22-R1 / SCV-2026.10.16-v11 / SEL-2026.10.12-v3; prompt P-2026.10.22-v23.0 (core + SOCCER).
- **Analysis status:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY
- **Probability method:** One regulation score grid: TB-1-MD Poisson ratings (k = 2, UNVALIDATED for this league) on the official table, league anchor from the 80-match 2026/27 population, low/base/high mixture 0.25/0.50/0.25 (×0.85/×1.00/×1.15 on both expected-goal rates) because line-ups are unconfirmed and the season is 11 games old. First half = 0.4178 × each rate (league share). Exact Poisson grid 0–12 goals per side, computed with code; every input below.
- **Scheduled start:** **2026-10-21 16:30 CEST (Europe/Sarajevo) = 14:30 UTC = 2026-10-22 01:30 AEDT** (FSRS round-12 fixture list, field owner; Soccerway/Flashscore match timestamp 1792593000 agrees). The owner's estimate of 21 Oct 1:10 PM AEDT does not match the official time and is not used.
- **Timing:** Request received about 2026-10-22T01:18+11:00 (14:18Z). Research began 14:20Z, before kickoff; the card was completed after kickoff. `POST_START_ISSUE`. Inputs are results of matches that kicked off by 2026-10-21 12:30Z (feed timestamps) plus the pre-kickoff table and fixture page; **no live or final information about this match was viewed**. Pages fetched after kickoff were parsed by code that dropped match id `GI2RuAdD` before reading any of its fields. Label: `CLEAN_PRE_START_INPUTS / POST_START_ISSUE` (own research cohort, not a pre-start-issued forecast).
- **Endpoint / definition:** Regulation 90 minutes plus stoppage time; league match, draw stands (no extra time). Goals rows settle on regulation goals; first-half rows on the first-half score. Supplied lines are half-goal/half-corner lines: no push.
- **Lineup state:** `LINEUP_UNCONFIRMED` / `BENCH_NOT_RETRIEVED` for both sides (A3 search ladder). No injury, suspension or rotation fact was found for either side.
- **Learning record:** Complete for prior games (31 dated rows with FT and HT, A3); availability snapshot empty (none published/found): `LEARN_RECORD_INCOMPLETE` for availability only.

### Decision block

Potkozarje are the home side with a modest attack (12 goals in 11) but the league's home edge is large (+0.80 goals per match, 62.5% home wins); Drina are the stronger team on goal difference (+14) with the second-best defence. The goal model is close to an even, slightly home-leaning match with about 2.6 goals. No row reaches a stable Rank 1. Main uncertainty: unconfirmed line-ups and an 11-game season.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---:|---:|---:|---|---|---|
| 1 | PICK (RANK1_UNSTABLE) | ANALYST_DERIVED | PRS:REG:POTKOZARJE_GOALS:OVER:0.5 (Potkozarje score at least once, regulation) | 0.7544 | 0.7572 | 0.8500 (68/80) | 0.5 − 1.415 = −0.92 goals; z −0.76 | Poisson mixture | Drina's defence (9 conceded in 11) keeps a home blank, as Laktaši did here (0-3) |
| 2 | PICK | ANALYST_DERIVED | PRS:REG:TOTAL_GOALS:UNDER:3.5 | 0.7413 | 0.7427 | 0.7625 (61/80) | 3.5 − 2.569 = +0.93; z +0.57 | Poisson mixture | Open game or Drina blow-out (they scored 8 at Nevesinje, 4 v Famos) |
| 3 | INFORMATIONAL | ANALYST_DERIVED | PRS:REG:TOTAL_GOALS:OVER:1.5 | 0.7222 | 0.7266 | 0.7250 (58/80) | 1.5 − 2.569 = −1.07; z −0.66 | Poisson mixture | 0-0 or 1-0 (Potkozarje had four 1-0/0-1 games) |
| 4 | INFORMATIONAL | ANALYST_DERIVED | PRS:1H:TOTAL_GOALS:UNDER:1.5 | 0.7089 | 0.7087 | 0.6835 (54/79) | 1.5 − 1.073 = +0.43; z +0.41 | Poisson mixture, league 1H share | Two first-half goals (Drina led 4-0 at half-time at Nevesinje) |

**Baseline coverage:** 4/4 ranked rows (BASELINE_LEAGUE_V1 = literal 2026/27 league frequency on the identical line, 80 matches, 79 with half-time scores, last match 2026-10-21 12:30Z, frozen before this card).
**Rank-1 gate:** `RANK1_UNSTABLE`. p 0.7544 ≥ 0.62, but the best non-complementary eligible alternative is FT Under 3.5 at 0.7413: gap 0.0131 < 0.04. ε ≈ 1e-6 (exact grid, truncation mass below 1e-6), so not a precision case. `SHADOW_GATE_RET03`: excluding other Potkozarje team-total lines leaves the same alternative, gap 0.0131 → RANK1_UNSTABLE.
**Rank-2 floor:** PASS (0.7413 ≥ 0.58).
**Joint failure:** Rank 1 and Rank 2 lose together only if Potkozarje score 0 **and** Drina score 4+: exact 0.0072 from the shared grid. Ranks 2 and 3 cannot both lose (total ≥ 4 and ≤ 1 are disjoint): `MECHANICALLY_PROTECTED`; this protection is construction, not skill.
**Shadow gate / Rank 2:** RET04 (highest p ≥ 0.58 on another quantity) = FT Under 3.5, 0.7413, BASELINE_P 0.7625, joint with Rank 1 0.0072. XCARD6 (minimum joint failure with Rank 1, p ≥ 0.58) = Potkozarje team Under 1.5, 0.5877, BASELINE_P 0.5125, joint 0.0000 (disjoint with Rank 1, MECHANICALLY_PROTECTED, same quantity). NOT_PRIMARY.
**Shadow RANK_DELTA / BASE_ONLY:** RANK_DELTA top two = Drina team Over 0.5 (0.6822 v 0.5625, Δ +0.120) and Potkozarje team Under 1.5 (0.5877 v 0.5125, Δ +0.075), joint loss P(Potkozarje ≥ 2 and Drina 0) = 0.1290; NOT_PRIMARY. BASE_ONLY: same order and gate (0.7572 / 0.7427 / 0.7266 / 0.7087; RANK1_UNSTABLE).
**Adjustment dependence:** `ADJUSTMENT_DEPENDENT` for ranks 2–4. Counting Drina's 8-0 as 4-0 moves FT Under 3.5 to 0.774 and 1H Under 1.5 to 0.732 above FT Over 1.5 (0.691); Rank 1 is unchanged at 0.754 (A6). Home edge ±1 SE moves Rank 1 between 0.726 and 0.780.
**Potential winner:** **Potkozarje 0.429, draw 0.265, Drina Zvornik 0.306** (regulation three-way). Potkozarje are the lean only because of home advantage; the non-Potkozarje mass is 0.571 and the draw is a real third outcome. Not a confident call.
**Supplied rows (all assessed):**
- **First-half goals Over 0.5:** 0.6560 (p_base 0.6582; BASELINE_P 0.6835, 54/79). Under 0.5: 0.3440 (BASELINE_P 0.3165). P(0-0 at half-time) = e^(−1.073) = 0.342 in the base case. Both teams' own first-half rates: Potkozarje 8/11 games with a first-half goal (1.00 per game), Drina 14/20 (1.15 per game). Below the 0.72 family floor for a first-half Over at Rank 1, and seventh in the eligible ladder: not selected.
- **Total goals Over 2.5:** 0.4718 (BASELINE_P 0.5500, 44/80); **Under 2.5:** 0.5282 (BASELINE_P 0.4500). Centre 2.57 against the line 2.5 (z −0.04): a coin flip, not selected.
- **Total corners Over/Under 10.5:** `NO_FORECAST`. No source publishes corner counts for this competition (Flashscore statistics feed empty for a played league match; ESPN does not cover the league; FSRS publishes no match statistics). SO-P3 and the soccer settlement-route rule forbid issuing a corner row without a named provider. The row also has no settlement route, so it would stay UNRESOLVED.
**Excluded from the primary slate (SO-P2, line-ups not retrieved):** side, double-chance and handicap rows are "capped" and full-match totals cannot be Rank 1. This card reads "capped" as ineligible for the primary slots, since v10 has no tier ladder (disclosed interpretation). Diagnostic only: Potkozarje +1.5 0.8766 (BASELINE_P 0.9125), no draw (12) 0.7354, Potkozarje or draw (1X) 0.6936, Drina or draw (X2) 0.5710.

**Model shadow (MLSCOPE-v2, frozen after this card):** run only after this card was written and read back; the dated shadow record is appended at the end of this card.

### Appendix

#### A1. Identity, timing and state
- Competition: Prva liga Republike Srpske (m:tel Prva liga RS), 2026/27 regular season, round 12; organiser Fudbalski savez Republike Srpske (FSRS). Promoted this season: Potkozarje (Druga liga RS Zapad champions 2025/26, 26 games 42-21, RSSSF) and Majevica.
- Fixture: FK Potkozarje (Aleksandrovac, Laktaši municipality) at home to FK Drina (Zvornik). FSRS round-12 list: "ФК ПОТКОЗАРJЕ (Александровац) — ФК ДРИНА (Зворник) · 21.10.2026 · 16:30"; referee, assistants, delegate and referee assessor shown as "-" (not yet published at retrieval). Stadium name NOT_VERIFIED.
- Soccerway/Flashscore match page `GI2RuAdD` (retrieved 14:21Z, page generation time 1792592507 = 14:21:47Z): "Prva Liga - RS - Round 12", start timestamp 1792593000 = 14:30:00Z, no score shown.
- Duplicate check (2026-10-22T02:17+11:00, names in Latin and Cyrillic): no local or canonical record of this fixture in Combined Log Parts 1–9 or `research/active_minis/`.
- Writer and lease: repository agent, mini 20261022F6K3OJNO, lease to 2026-10-29T00:40+11:00; mini not frozen.

#### A2. Contracts and candidate recipe (frozen before pricing)
Supplied: 1H total goals O/U 0.5; FT total goals O/U 2.5; FT total corners O/U 10.5 (regulation, half lines). Declared derived universe: three-way result; double chance 1X/X2/12; FT totals O/U 1.5/2.5/3.5; 1H totals O/U 0.5/1.5; both teams to score; each team's goals O/U 0.5/1.5; Drina −1.5 / Potkozarje +1.5. All from one grid; corners have no model (NO_FORECAST). Eligibility: SO-P2 exclusions above; 1H Over 0.5 at Rank 1 needs p ≥ 0.72 and a 5-point lead; selection ceiling 0.90 (no row exceeds it).

#### A3. Evidence, availability and online history

**Availability search (ROSTER_AVAILABILITY_PROTOCOL §§1–6), both sides.** Official match: FSRS round-12 page shows no squad or officials; FSRS match pages (`fsrs.org/utakmice.html?id=…`) timed out twice (HTTP 000). Teams: no club site found for either club. Permitted provider: the Flashscore line-up feed for a played Potkozarje league match is empty (`df_lc`), so line-ups are not carried for this competition; the incident feed carries goals but not cards, so suspensions cannot be read. Local-language search ("Potkožarje Drina Zvornik najava sastav povrede", "Drina Zvornik Famos 4:0", "Sutjeska Potkožarje") found no preview, injury or suspension report. Result: `LINEUP_UNCONFIRMED` for both sides; no absence is assumed and none is invented; the mixture widens instead.

**Recent scorers (feed incidents, goals only):** Drina v Famos 4-0 (17 Oct): Janković V. 25', Mikan M. 48', Stoisavljević A. 66', Ostojić S. 82'. Zvijezda 09 2-1 Drina (10 Oct): Dragićević M. 43', Tomić D. 87' (Zvijezda), Dragutinović N. 89' (Drina). Potkozarje 1-0 Slavija (9 Oct): Rosić B. 74'. FSRS scorer list: Bobić Luka (Potkozarje) 2; Milinković Nikola 3, Erić Danijel 2, Janjić Stefan 2 (Drina).

**Official table after round 11 (FSRS, retrieved about 14:28Z):** Potkozarje 6th, 11 GP 5-2-4, 12:12, 17 pts; Drina 4th, 11 GP 5-3-3, 23:9, 18 pts. Soccerway's table (14:21Z) agrees for both clubs; it already included three round-12 matches played earlier on 21 Oct.

**Form windows (true n; overlapping windows are one piece of evidence):**

| Side | Window | True n | GF/g | GA/g | Total/g | Over 2.5 | 1H goals/g | 1H Over 0.5 | W-D-L |
|---|---|---:|---:|---:|---:|---|---:|---|---|
| Potkozarje | L5 | 5 | 1.00 | 1.00 | 2.00 | 2/5 | 0.80 | 2/5 | 2-1-2 |
| Potkozarje | L10 | 10 | 1.00 | 1.20 | 2.20 | 4/10 | 1.00 | 7/10 | 4-2-4 |
| Potkozarje | L15 | 11 | 1.09 | 1.09 | 2.18 | 4/11 | 1.00 | 8/11 | 5-2-4 |
| Potkozarje | L20 | 11 | 1.09 | 1.09 | 2.18 | 4/11 | 1.00 | 8/11 | 5-2-4 |
| Drina | L5 | 5 | 1.60 | 0.60 | 2.20 | 2/5 | 0.60 | 3/5 | 3-1-1 |
| Drina | L10 | 10 | 2.20 | 0.70 | 2.90 | 6/10 | 1.20 | 7/10 | 5-3-2 |
| Drina | L15 | 15 | 2.00 | 1.07 | 3.07 | 10/15 | 1.27 | 11/15 | 6-5-4 |
| Drina | L20 | 20 | 1.75 | 1.00 | 2.75 | 12/20 | 1.15 | 14/20 | 8-6-6 |

Potkozarje's L15/L20 stop at 11: they played 2025/26 a tier lower (Druga liga RS Zapad), whose games are not the exact competition and were not translated into the windows. Drina's L20 spans 2025/26 (regular stage and promotion group) and 2026/27. Splits 2026/27: Potkozarje home 6 GP 8-6 (1.33/1.00), away 5 GP 4-6; Drina home 5 GP 11-2, away 6 GP 12-7 (2.00/1.17, of which 8-0 at Nevesinje).

**Potkozarje: 11 dated rows, newest first** (kickoff UTC from the feed; FT and HT shown Potkozarje first)

| # | Kickoff (UTC) | Venue | Opponent | FT (for-against) | HT (for-against) | Result | Feed match id |
|---:|---|---|---|---|---|---|---|
| 1 | 2026-10-17 12:30 | A | Sutjeska Foca | 1-2 | 1-1 | L | `QD3WWEDr` |
| 2 | 2026-10-09 16:00 | H | Slavija | 1-0 | 0-0 | W | `A1gJxpp4` |
| 3 | 2026-10-03 13:00 | A | Nevesinje | 1-2 | 0-2 | L | `fiU8RbK5` |
| 4 | 2026-09-26 17:00 | H | Leotar | 1-1 | 0-0 | D | `xYlyDa5C` |
| 5 | 2026-09-23 14:00 | A | Romanija Pale | 1-0 | 0-0 | W | `n7nq6ihS` |
| 6 | 2026-09-19 17:30 | H | Majevica | 1-0 | 1-0 | W | `6TpT9Zh3` |
| 7 | 2026-09-12 17:30 | H | Laktasi | 0-3 | 0-2 | L | `0CisspJa` |
| 8 | 2026-09-05 14:30 | A | Famos Vojkovici | 0-1 | 0-1 | L | `hnlZr6lm` |
| 9 | 2026-09-02 17:30 | H | Zvijezda 09 | 3-2 | 1-0 | W | `AVUd1857` |
| 10 | 2026-08-29 15:00 | A | Kozara | 1-1 | 1-0 | D | `Y7SBACrL` |
| 11 | 2026-08-22 17:30 | H | Omarska | 2-0 | 1-0 | W | `2yYvM3Vb` |

**Drina Zvornik: 20 dated rows, newest first** (kickoff UTC from the feed; FT and HT shown Drina Zvornik first)

| # | Kickoff (UTC) | Venue | Opponent | FT (for-against) | HT (for-against) | Result | Feed match id |
|---:|---|---|---|---|---|---|---|
| 1 | 2026-10-17 12:30 | H | Famos Vojkovici | 4-0 | 1-0 | W | `Yw7vVhre` |
| 2 | 2026-10-10 13:00 | A | Zvijezda 09 | 1-2 | 0-1 | L | `ptgQG2Np` |
| 3 | 2026-10-03 13:00 | H | Kozara | 1-0 | 0-0 | W | `SMcWRSVo` |
| 4 | 2026-09-27 14:00 | A | Omarska | 1-1 | 0-0 | D | `EJJ2BnU7` |
| 5 | 2026-09-23 14:00 | H | Prijedor | 1-0 | 1-0 | W | `KxInFUUr` |
| 6 | 2026-09-19 14:00 | A | Laktasi | 1-2 | 0-2 | L | `2u02ZhHj` |
| 7 | 2026-09-12 17:00 | A | Sutjeska Foca | 0-0 | 0-0 | D | `YP9WvFgT` |
| 8 | 2026-09-05 14:30 | H | Slavija | 3-0 | 2-0 | W | `dOjfWS4s` |
| 9 | 2026-09-02 14:30 | A | Nevesinje | 8-0 | 4-0 | W | `nVEUF7K0` |
| 10 | 2026-08-29 15:00 | H | Leotar | 2-2 | 1-0 | D | `Uiy0ECTk` |
| 11 | 2026-08-22 15:00 | A | Romanija Pale | 1-2 | 0-1 | L | `M5UfILUN` |
| 12 | 2026-05-30 15:30 | A | Leotar | 2-2 | 1-1 | D | `AJh3rFjm` |
| 13 | 2026-05-20 15:00 | H | Slavija | 2-1 | 1-1 | W | `tpCwSg66` |
| 14 | 2026-05-16 15:00 | A | BSK Banja Luka | 2-3 | 1-1 | L | `4M9hybqK` |
| 15 | 2026-05-09 15:00 | H | Kozara | 1-1 | 0-0 | D | `dxGjHxhl` |
| 16 | 2026-05-03 13:00 | A | Laktasi | 0-0 | 0-0 | D | `S2ZQ0H77` |
| 17 | 2026-04-25 14:30 | A | Romanija Pale | 3-1 | 1-1 | W | `6ifF1hIO` |
| 18 | 2026-04-18 13:00 | H | BSK Banja Luka | 0-1 | 0-0 | L | `Asfx0usK` |
| 19 | 2026-04-11 14:00 | A | Kozara | 0-1 | 0-1 | L | `dvU2otSQ` |
| 20 | 2026-04-08 14:00 | A | Nevesinje | 2-1 | 1-0 | W | `hpWCz4dB` |

Rows from Soccerway team result pages (home/away from the row text) with final and half-time scores from the Flashscore scores feed; page and feed agreed on all 31 rows. Retrieved 2026-10-21 between about 14:24Z and 14:45Z; source publication times not shown by the provider.

#### A4. Distribution, baseline and arithmetic
League anchor (2026/27, 80 matches 22 Aug – 21 Oct 12:30Z, both teams in the league, target excluded): 216 goals = 2.700 per match; home 1.750, away 0.950 per match; LM = 1.350 goals per team-game; home edge HE = +0.800 (margin SD 2.015, SE 0.225); total SD 1.626; first-half share s = 89 first-half goals / 213 goals in the 79 matches with a half-time score = **0.4178**; results home 50, draw 16, away 14.

TB-1-MD (PROBABILITY_TOOLKIT §4.2, k = 2):
- Potkozarje: O_h = (12 + 2×1.35)/13 = 1.1308; D_h = (12 + 2.7)/13 = 1.1308.
- Drina: O_a = (23 + 2.7)/13 = 1.9769; D_a = (9 + 2.7)/13 = 0.9000.
- T = (1.1308 + 0.9000)/2 + (1.9769 + 1.1308)/2 = 2.5692.
- M = [(1.1308 − 1.1308) − (1.9769 − 0.9000)]/2 + 0.800 = +0.2615.
- λ_home = (T + M)/2 = **1.4154**; λ_away = (T − M)/2 = **1.1538**; first half 0.4178 × each = 0.591 / 0.482 (total 1.073).

Mixture: low ×0.85 (1.203 / 0.981), base ×1.00, high ×1.15 (1.628 / 1.327), weights 0.25/0.50/0.25. Independent Poisson per side (toolkit §2 simplification: draws may be slightly low at small λ; disclosed, not adjusted). Expected regulation score **Potkozarje 1.42 – Drina 1.15** (total 2.57, SD 1.63 including mixture spread; margin +0.26 home); first-half total 1.07 (SD 1.04). Width check: total SD 1.63 ≥ the 1.37 benchmark floor.

Full priced ladder (p_card mixture / p_base / BASELINE_P literal count):

| Contract | p_card | p_base | BASELINE_P |
|---|---:|---:|---:|
| Potkozarje +1.5 | 0.8766 | 0.8760 | 0.9125 (73/80) |
| Potkozarje team Over 0.5 | 0.7544 | 0.7572 | 0.8500 (68/80) |
| FT Under 3.5 | 0.7413 | 0.7427 | 0.7625 (61/80) |
| No draw (12) | 0.7354 | 0.7370 | 0.8000 (64/80) |
| FT Over 1.5 | 0.7222 | 0.7266 | 0.7250 (58/80) |
| 1H Under 1.5 | 0.7089 | 0.7087 | 0.6835 (54/79) |
| Potkozarje or draw (1X) | 0.6936 | 0.6929 | 0.8250 (66/80) |
| Drina team Over 0.5 | 0.6822 | 0.6846 | 0.5625 (45/80) |
| Drina team Under 1.5 | 0.6797 | 0.6794 | 0.7875 (63/80) |
| 1H Over 0.5 | 0.6560 | 0.6582 | 0.6835 (54/79) |
| Potkozarje team Under 1.5 | 0.5877 | 0.5865 | 0.5125 (41/80) |
| Drina or draw (X2) | 0.5710 | 0.5701 | 0.3750 (30/80) |
| FT Under 2.5 | 0.5282 | 0.5262 | 0.4500 (36/80) |
| BTTS Yes | 0.5161 | 0.5183 | 0.4625 (37/80) |
| BTTS No | 0.4839 | 0.4817 | 0.5375 (43/80) |
| FT Over 2.5 | 0.4718 | 0.4738 | 0.5500 (44/80) |
| Potkozarje win | 0.4290 | 0.4299 | 0.6250 (50/80) |
| Potkozarje team Over 1.5 | 0.4123 | 0.4135 | 0.4875 (39/80) |
| 1H Under 0.5 | 0.3440 | 0.3418 | 0.3165 (25/79) |
| Drina team Over 1.5 | 0.3203 | 0.3206 | 0.2125 (17/80) |
| Drina team Under 0.5 | 0.3178 | 0.3154 | 0.4375 (35/80) |
| Drina win | 0.3064 | 0.3071 | 0.1750 (14/80) |
| 1H Over 1.5 | 0.2911 | 0.2913 | 0.3165 (25/79) |
| FT Under 1.5 | 0.2778 | 0.2734 | 0.2750 (22/80) |
| Draw | 0.2646 | 0.2630 | 0.2000 (16/80) |
| FT Over 3.5 | 0.2587 | 0.2573 | 0.2375 (19/80) |
| Potkozarje team Under 0.5 | 0.2456 | 0.2428 | 0.1500 (12/80) |
| Drina −1.5 | 0.1234 | 0.1240 | 0.0875 (7/80) |

Checks (toolkit §11): complements sum to 1 (e.g. 0.7413 + 0.2587; 0.6560 + 0.3440); 0.4290 + 0.2646 + 0.3064 = 1.0000; all rows from one grid. TEAM_BASELINE_P (TB-1-MD) is the base case itself here (UNVALIDATED:Prva Liga RS). Departure ledger: the card is below the league baseline on "home team scores" (−0.096) because Drina concede 0.82 per game; above it on Drina scoring (+0.120) because Drina score 2.09 per game against a league 1.35.

#### A5. Supplied contracts, W/P/L/V (unconditional)
| Contract | W | P | L | V | p_card |
|---|---:|---:|---:|---:|---:|
| 1H Over 0.5 | 0.6560 | 0 | 0.3440 | 0 | 0.6560 |
| 1H Under 0.5 | 0.3440 | 0 | 0.6560 | 0 | 0.3440 |
| FT Over 2.5 | 0.4718 | 0 | 0.5282 | 0 | 0.4718 |
| FT Under 2.5 | 0.5282 | 0 | 0.4718 | 0 | 0.5282 |
| Corners Over 10.5 | NOT_ESTIMATED | | | | NO_FORECAST |
| Corners Under 10.5 | NOT_ESTIMATED | | | | NO_FORECAST |

#### A6. Adjustments and sensitivity
| Driver | Treatment | Effect |
|---|---|---|
| Home venue | League HE +0.80 (2026/27, 80 matches) inside M | Moves the lean from Drina to Potkozarje |
| Availability | None known; LINEUP_UNCONFIRMED → mixture ×0.85/×1.15 | Widens; no centre shift |
| Rest | Both last played 17 Oct (4 days); equal | 0 |
| Weather (Open-Meteo, Laktaši 44.909N 17.301E, 14:00–16:00Z) | Overcast (code 3), 17.0–18.5 °C, 0.0 mm, wind ≤ 6.5 km/h | 0 |
| Drina 8-0 outlier | Base keeps the published table | Sensitivity below |

| Sensitivity | λ home / away | Potk O0.5 | FT U3.5 | FT O1.5 | 1H U1.5 | 1H O0.5 | FT U2.5 | Potk / draw / Drina |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Base (card) | 1.415 / 1.154 | 0.754 | 0.741 | 0.722 | 0.709 | 0.656 | 0.528 | 0.429 / 0.265 / 0.306 |
| 8-0 counted as 4-0 | 1.415 / 1.000 | 0.754 | 0.774 | 0.691 | 0.732 | 0.633 | 0.567 | 0.465 / 0.270 / 0.266 |
| HE −1 SE (0.575) | 1.303 / 1.266 | 0.726 | 0.741 | 0.722 | 0.709 | 0.656 | 0.528 | 0.375 / 0.267 / 0.358 |
| HE +1 SE (1.025) | 1.528 / 1.041 | 0.780 | 0.741 | 0.722 | 0.709 | 0.656 | 0.528 | 0.484 / 0.258 / 0.258 |

#### A7. Family rules and dependence
SO-P2 (no XI or bench) applied as above. SO-P3: corners NO_FORECAST. Disclosure thresholds (S-R2) not reached. No row above 0.80 on a single team without suppression branches (Potkozarje +1.5 is excluded anyway). Rank 1 is a single-team row (0.754): its failure branches are Drina's suppression (6 clean sheets in 11 this season, 2 of 6 away) and Potkozarje's finishing (blanked 2 of 11: 0-3 v Laktaši at home, 0-1 at Famos).

#### A8. Sources (opened; retrieval times UTC on 21 Oct 2026)
| # | Source | Field used | Retrieved | Role |
|---|---|---|---|---|
| 1 | FSRS Prva liga page https://fsrs.org/sr-BA/takmicenja-prva-liga.html | Official table after round 11, round-11 results and kickoff times, scorer list | ~14:28 | Field owner |
| 2 | FSRS round 12 https://fsrs.org/sr-BA/takmicenja-prva-liga.html?tab=matches&kolo=12 | Fixture, 21.10.2026 16:30, officials "-" | ~14:33 | Field owner |
| 3 | Soccerway standings https://ca.soccerway.com/bosnia-and-herzegovina/prva-liga-rs/standings (via r.jina.ai) | Table, next match markers | ~14:21 | Provider (Flashscore lineage) |
| 4 | Soccerway match page https://ca.soccerway.com/game/potkozarje-AHrFXeeB/zvornik-YZcveBlG/?mid=GI2RuAdD | Round 12, start timestamp 1792593000 | 14:21:47 | Provider |
| 5 | Soccerway team results https://ca.soccerway.com/team/potkozarje/AHrFXeeB/results/ and https://ca.soccerway.com/team/zvornik/YZcveBlG/results/ (+ 12 other clubs for the league population) | Dated rows, home/away | 14:24–15:12 | Provider |
| 6 | Flashscore scores feed `2025.flashscore.ninja/2025/x/feed/dc_1_<id>` and `df_sui_1_<id>` | Final and half-time scores, goal incidents; scores only, no odds feed read | 14:30–15:12 | Provider (same lineage as 3–5) |
| 7 | RSSSF Bosnia-Hercegovina 2025/26 https://rsssf.org/tablesb/bih2026.html | 2025/26 tables; Potkozarje promoted from Druga liga RS Zapad | ~14:50 | Independent history |
| 8 | Open-Meteo forecast API (Laktaši) | Weather 13:00–17:00Z | ~15:10 | Weather |

Independence: 3–6 are one lineage (Livesport); FSRS (1–2) is the independent field-owner corroboration of the table, round-11 results and kickoff. Inaccessible: FSRS match pages (timeout), FotMob (league not covered), Sofascore/FBref (blocked per SOURCES). Not used: odds, tips, previews.

#### A9. Completion receipt
| Procedure | Status |
|---|---|
| Authority, identity, duplicate | DONE |
| Official kickoff and zone | DONE (FSRS + Soccerway timestamp) |
| Timing / known-at | DONE: CLEAN_PRE_START_INPUTS / POST_START_ISSUE; no target outcome viewed |
| Starters, bench, absences | INCOMPLETE: LINEUP_UNCONFIRMED both sides after the full ladder |
| L5/L10/L15/L20 with true n | DONE (Potkozarje capped at 11 in this competition) |
| Rules and endpoint | DONE (regulation; league draw stands) |
| Distribution, arithmetic, baseline | DONE (one grid; BASELINE_LEAGUE_V1 4/4 ranked rows) |
| Supplied rows assessed | DONE (corners NO_FORECAST with reason) |
| Gate, dependence, shadows | DONE |
| Model shadow | See the Model shadow line |
| Settlement / import | NOT_PERFORMED (prompt 3) |

#### Model shadow record (2026-10-21T15:18:49Z, after the card was written and read back)
`python -m ml pregame run` → **`NOT_RUN_NO_RELEASE`**: no active forecast-cycle release for Soccer/Prva Liga RS (active releases: Baseball/MLB, Ice Hockey/NHL). Receipt `research/pregame/LOCAL-20261022F6K3OJNO-G0002/20261021T151849435596Z_PREGAME.csv`. Nothing was frozen in the shadow ledger; the card's p_card, ranks and picks are unchanged.

`SPORTS_ONLY_MARKET_BLIND: APPLIED` · `RESEARCH_ONLY_NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD LOCAL-20261022F6K3OJNO-G0002 -->

<!-- BEGIN CARD LOCAL-20261022F6K3OJNO-G0003 -->
## Card · LOCAL-20261022F6K3OJNO-G0003 · BASKETBALL / NBA 2026-27 regular season (opening round) · Atlanta Hawks @ Orlando Magic · 21 Oct 2026 (US) / 22 Oct 2026 (AEDT)

- **Local event key:** `LOCAL-20261022F6K3OJNO-G0003` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** NOT_ASSIGNED / PROMPT_4_IMPORT (settlement phase).
- **Event key / native IDs / aliases:** `NBA-20261021-ATL-ORL`; ESPN event `401909834`; NBA game id NOT_RETRIEVED (NBA CDN refused access); aliases Hawks @ Magic, ATL @ ORL.
- **Authority:** `LOCAL_WORKING_TREE`, branch `main`, HEAD `1ccaf3dd124e20083e8485f208811d5fc528f903`, no uncommitted control changes at read (2026-10-22T09:50+11:00). MDS-2026.10.22-v23.0 / CR-2026.10.22-R1 / SCV-2026.10.16-v11 / SEL-2026.10.12-v3; prompt P-2026.10.22-v23.0 (core + BASKETBALL).
- **Analysis status:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY
- **Probability method:** One joint (total, margin) object. League level from the ESPN 2025-26 standings (30 teams × 82 games) × the repo's EARLY_SEASON 0.988; team centres from TB-1-MD arithmetic on 2025-26 points for/against after a **data-measured season-to-season carry-over** (offence 0.314, defence 0.640, two season pairs); home edge +1.72 (BASE_RATES §7.1); within-case widths = the NBA residual benchmarks 19.4 (total) / 15.1 (margin); three-point mixtures (0.25/0.50/0.25) on the total centre (±5.43) and on the margin centre (±5.17) taken from the carry-over regression's own residuals, independent of each other. Exact normal tails computed with code; every input and step is in A4.
- **Scheduled start:** **2026-10-21 23:00:00Z = 19:00 EDT (7:00 PM ET) = 2026-10-22 10:00 AEDT** (ESPN event date; NBA injury report header "07:00 (ET)"). The owner's estimate (10:10 AM AEDT) is 10 minutes later and is treated as the likely tip time; the actual tip is `NOT_VERIFIED`. Venue: Kia Center, Orlando, Florida.
- **Timing:** Request received 2026-10-22T09:50+11:00 (22:50Z). Every target-specific input (fixture, injury lists, starters, referees) was retrieved between 22:50:42Z and 22:52:29Z, **before the scheduled start**. Past-game and standings data were fetched 22:52–22:59Z with the target event excluded by id before any field was read. The card was finished after 23:00Z. No live or final information about this game was viewed. Label: `CLEAN_PRE_START_INPUTS / POST_START_ISSUE` (own research cohort; not a pre-start-issued forecast). Provider publication times are not shown by RotoWire or ESPN; the NBA injury report carries its own time (6:30 PM ET).
- **Endpoint / definition:** Full game **including overtime**, as the NBA plays it; half-point lines, so no push; margin is never 0 (overtime decides). Operator terms `UNKNOWN_DEFINITION / NOT_OPERATOR_VERIFIED`.
- **Lineup state:** Injuries: official NBA report corroborated by ESPN. Starting fives: `STARTERS_THIRD_PARTY_CONFIRMED` (RotoWire "Confirmed Lineup" only; the official feed was not retrievable). Bench and rotation minutes: not published. Dependent player rows capped (control 20): none issued.
- **Learning record:** 40 dated prior-game rows (A3), injury and starter snapshots with times (A3). Availability for the bench is unknown, not healthy.

### Decision block

The model sees two close-to-average teams: it sits within 0.02 of the league-only baseline on every priced row, so there is **no team-specific edge**. Orlando are a slight home favourite (model margin +1.6: the +1.72 home edge, partly offset by Atlanta's better 2025-26 margin, +2.41 against +0.63). The ranked rows below are structural results of the declared line ladder, not insight about these two teams; three of the four are the same bet.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---:|---:|---:|---|---|---|
| 1 | PICK (RANK1_UNSTABLE) | ANALYST_DERIVED | NBA:FULL:TOTAL:UNDER:239.5:INCLUDING_OT | 0.7042 | 0.7078 | 0.7030 | 239.5 − 228.89 = +10.6; z +0.54 | Normal mixture | A fast, efficient game (opening-night teams, 2025-26 league scoring 231.2) or overtime |
| 2 | PICK | ANALYST_DERIVED | NBA:FULL:TOTAL:UNDER:237.5:INCLUDING_OT | 0.6684 | 0.6715 | 0.6704 | +8.6; z +0.44 | Same | Same (strictly nested inside Rank 1's losing set) |
| 3 | INFORMATIONAL | ANALYST_DERIVED | NBA:FULL:TOTAL:UNDER:235.5:INCLUDING_OT | 0.6310 | 0.6334 | 0.6364 | +6.6; z +0.33 | Same | Same |
| 4 | INFORMATIONAL | ANALYST_DERIVED | NBA:FULL:HAWKS:+6.5:INCLUDING_OT | 0.6239 | 0.6274 | 0.6147 | Magic margin line 6.5 − 1.59 = +4.9; z +0.32 | Same mixture, margin | Orlando win by 7 or more; flagged `PLUS_CUSHION_UNSUPPORTED` (A7) |

**Baseline coverage:** 4/4 ranked rows and 30/30 priced rows (BASELINE_LEAGUE_V1: league-only normal from the repo's NBA 2025-26 reference, mean total 230.7 × 0.988, home edge 1.72, raw SDs 21.7 / 16.4; frozen in this card before pricing).
**Rank-1 gate:** `RANK1_UNSTABLE`. p 0.7042 ≥ 0.62, but the best non-complementary alternative on the full priced universe (another threshold on the same quantity counts) is Under 237.5 at 0.6684: gap 0.0358 < 0.04. Precision: the grid is exact to about 1e-6, so this is not a precision tie.
**`SHADOW_GATE_RET03`:** excluding other totals lines, the alternative is Hawks +6.5 at 0.6239: gap 0.0803 ≥ 0.04 and p ≥ 0.62 → PASS (shadow only; not the primary gate).
**Rank-2 floor:** PASS (0.6684 ≥ 0.58).
**Joint failure:** Ranks 1 and 2 are nested on one quantity: if Rank 1 loses (total ≥ 240), Rank 2 loses too, so the joint loss equals Rank 1's own loss, **0.2958**. There is no diversification and Hit@2 is effectively one bet. Rank 1 and Rank 4 (different quantities, total and margin, independent within each case): both lose 0.1112.
**Shadow gate / Rank 2:** RET04 (highest p ≥ 0.58 on a different quantity from Rank 1) = Hawks +6.5, 0.6239, BASELINE_P 0.6147, joint loss with Rank 1 0.1112. XCARD6 (minimum exact joint failure with Rank 1 among p ≥ 0.58) = Hawks +6.5 as well (Hawks +5.5: 0.1185; any other totals row: 0.2958). NOT_PRIMARY.
**Shadow RANK_DELTA / BASE_ONLY:** RANK_DELTA top two (p ≥ 0.58, by p_card − BASELINE_P) = Hawks +6.5 (+0.0092) and Hawks +5.5 (+0.0081; p 0.5992), nested, joint loss 0.3761. BASE_ONLY (base case only): same order and gate (0.7078 / 0.6715 / 0.6334 / 0.6274, RANK1_UNSTABLE). NOT_PRIMARY.
**Adjustment dependence:** `ADJUSTMENT_DEPENDENT`. Without the EARLY_SEASON 0.988 multiplier the total centre is 231.67 and the order becomes Under 239.5 (0.6540), Hawks +6.5 (0.6239), Under 237.5 (0.6160), Under 235.5 (0.5768). That multiplier moves every Under by about 5 points (A6). The independent online check in A6 does not confirm it on the last three seasons alone.
**Potential winner:** **Orlando Magic 0.5408; Atlanta Hawks 0.4592** (two-way including overtime). A lean toward the home side, not a confident call.

**The four supplied rows (all assessed; ranks in the full ladder in brackets):**

| Supplied row | p_card | p_base | BASELINE_P | z from centre | Rank in ladder |
|---|---:|---:|---:|---|---|
| Combined total **Under 233.5** | 0.5922 | 0.5940 | 0.6013 | +0.23 | 6th |
| Hawks **+2.5** | 0.5233 | 0.5239 | 0.5190 | +0.06 | 13th |
| Magic **−2.5** | 0.4767 | 0.4761 | 0.4810 | −0.06 | 18th |
| Combined total **Over 233.5** | 0.4078 | 0.4060 | 0.3987 | −0.23 | 25th |

Among the supplied lines only Under 233.5 is above 0.58 (0.5922), and it sits below the league-only baseline (0.6013) because the team model carries the Hawks' high-scoring 2025-26 into the centre. Hawks +2.5 and Magic −2.5 are within 0.03 of a coin flip. Neither supplied handicap row reaches the 0.58 Rank-2 floor.
**Supplied rows not selected:** all four, for the reasons above; none was removed to manufacture a pass.
**Player rows:** none. No current-season minutes, usage or shooting lines for any player exist yet (0 games), the 2025-26 lines were not retrieved, and RULES_BASKETBALL control 20 caps a bare name at `AGGREGATE_ONLY`. A player prop would be invented.

**Model shadow (MLSCOPE-v2, frozen after this card):** run only after this card was written and read back; the dated shadow record is appended at the end of this card.

### Appendix

#### A1. Identity, timing and state
- Competition: NBA 2026-27 regular season, opening round (both teams 0-0). Atlanta Hawks (away) at Orlando Magic (home), Kia Center, Orlando.
- ESPN event 401909834, `STATUS_SCHEDULED`, date 2026-10-21T23:00Z at 22:50:42Z and at 22:52:29Z. NBA injury report (PDF, "10/21/26 06:30 PM"): "ATL@ORL", game time "07:00 (ET)".
- Referees (RotoWire, third party): Pat Fraher, Eric Dalen, Jenna Reneau. Official NBA referee assignment NOT_RETRIEVED.
- Duplicate check (2026-10-22T10:02+11:00): no local or canonical record of this fixture in Combined Log Parts 1–9 or `research/active_minis/`. The only hits for "Atlanta Hawks" or "Orlando Magic" are opponent rows (2026-03-21 games) inside other teams' form tables in Parts 7–8.
- Writer and lease: repository agent, mini 20261022F6K3OJNO, lease to 2026-10-29T00:40+11:00, not frozen.
- Observation disclosed: while reading the 2026-10-20 and 2026-10-21 scoreboards for early-season context I saw the **final score of the OKC @ SAS game** (the carried card `LOCAL-20261021OKCSASR01-G0001`). It was not used to set any input, and that card is **not graded here**; prompt 3 settles it from the field owner.

#### A2. Contracts and candidate recipe (frozen before pricing)
Supplied: Hawks +2.5; Magic −2.5; Combined Total Over 233.5; Under 233.5 (full game, half-point lines). Declared derived universe, frozen before any probability was computed: Magic −k and Hawks +k for k = 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5; totals Over and Under at 227.5, 229.5, 231.5, 233.5, 235.5, 237.5, 239.5; both moneylines. That is 30 rows from one object, spanning about ±0.55 SD of the total and ±0.45 SD of the margin around the supplied lines. Selection ceiling 0.90 (no row near it). Player, period and team-total rows are excluded: no supported inputs.

#### A3. Evidence and online history

**Availability.** Both teams' lists agree between the official NBA injury report (6:30 PM ET, retrieved 22:51:03Z) and ESPN's injury feed (22:50:54Z).

| Team | Out | Reason (NBA report) | ESPN date |
|---|---|---|---|
| Atlanta | Mouhamed Gueye | Left foot fracture | 2026-10-19 |
| Atlanta | Henri Veesaar | Right ACL tear | 2026-09-21 |
| Atlanta | RayJ Dennis, Keshon Gilbert, Jalen Wilson | G League two-way assignments | n/a |
| Orlando | Anthony Black | Right ankle sprain | 2026-10-20 |
| Orlando | Jonathan Isaac | Left knee injury management | 2026-10-20 |
| Orlando | Izaiyah Nelson | Left ankle injury recovery | 2026-09-28 |
| Orlando | Noah Penda | Right partially torn hamstring | 2026-10-17 |

No player is listed Questionable or Probable on either side. **Starters (RotoWire "Confirmed Lineup", retrieved 22:51:37Z):** Atlanta: CJ McCollum, Nickeil Alexander-Walker, Dyson Daniels, Jalen Johnson, Onyeka Okongwu. Orlando: Jalen Suggs, Desmond Bane, Franz Wagner, Paolo Banchero, Wendell Carter Jr. Official confirmation: NBA CDN returned "Access Denied"; the ESPN summary had no starter flags at 22:52:29Z; the teams' X timelines returned no data. Search ladder: official game (NBA CDN refused; ESPN empty) → both teams' feeds (X returned no data; club sites and beat reporters were **not** searched) → eligibility/medical (NBA report) → permitted provider (RotoWire, ESPN). After 23:00Z I deliberately ran no searches about this game, because snippets could show the live score and would end the clean-input claim; starters therefore remain single-lineage and a later official confirmation was not sought.

**Rotation continuity (R2 step 3).** Share of box-score minutes in each team's last games played by players still on the current ESPN roster: Orlando 100% (last regular-season game, 4/12) and 96% (last playoff game, 5/3: Moritz Wagner gone). Atlanta 50% (last regular-season game, mostly reserves) and **67% of the last playoff game's minutes** (4/30: Jonathan Kuminga 23 minutes, Zaccharie Risacher 16 and Gabe Vincent 13 are no longer on the roster). Atlanta therefore changed about 33% of its playoff minutes, above R2's roughly 30% line, so its previous-season windows are flagged and not used to move the centre. Atlanta's two absentees (Gueye, Veesaar) were not among the nine highest-minute Atlanta players in the two box scores read (their season minutes were not retrieved); Orlando's Anthony Black played 33 minutes in the last playoff game and 19 in the last regular-season game, so his absence is a real depth loss, handled as width (A6), not a numeric shift (his season minutes and usage were not retrieved).

**2025-26 season (ESPN standings and team statistics, 82 games each):**

| Metric | Atlanta | Orlando | League mean |
|---|---:|---:|---:|
| Record | 46-36 | 45-37 | n/a |
| Points for / game | 118.46 | 115.74 | 115.61 |
| Points against / game | 116.05 | 115.11 | 115.61 |
| Margin | +2.41 | +0.63 | 0 |
| Game total | 234.51 | 230.85 | 231.21 |
| Field goals attempted | 91.96 | 88.34 | n/a |
| Offensive rebounds / turnovers / FTA | 10.98 / 13.38 / 21.49 | 10.95 / 13.70 / 27.45 | n/a |
| Possessions (FGA − OREB + TO + 0.44 FTA) | 103.8 | 103.2 | n/a |
| ORtg / DRtg (estimated, own possessions) | 114.1 / 111.8 | 112.2 / 111.6 | n/a |

The possessions × efficiency centre (pace 103.5; ATL 116.8, ORL 115.9; total 232.7) agrees with the TB-1-MD total before carry-over (232.68), so the two methods are one calculation here. Postseason 2025-26: Atlanta lost 2-4 to New York; Orlando lost 3-4 to Detroit (game 7 at Detroit 94-116).

**Form windows (all 2025-26; 2026-27 regular season has 0 games, so these are previous-season games and flagged; windows overlap and count as one piece of evidence):**

| Side | Window | True n | W-L | PF | PA | Total | Dates |
|---|---|---:|---|---:|---:|---:|---|
| Atlanta | L5 | 5 | 2-3 | 100.0 | 118.8 | 218.8 | 04-21 to 04-30 |
| Atlanta | L10 | 10 | 3-7 | 106.4 | 118.2 | 224.6 | 04-06 to 04-30 |
| Atlanta | L15 | 15 | 7-8 | 111.5 | 114.3 | 225.7 | 03-27 to 04-30 |
| Atlanta | L20 | 20 | 11-9 | 115.2 | 114.8 | 230.1 | 03-19 to 04-30 |
| Orlando | L5 | 5 | 2-3 | 97.8 | 103.6 | 201.4 | 04-25 to 05-03 |
| Orlando | L10 | 10 | 5-5 | 105.1 | 105.3 | 210.4 | 04-08 to 05-03 |
| Orlando | L15 | 15 | 9-6 | 109.3 | 109.1 | 218.4 | 03-31 to 05-03 |
| Orlando | L20 | 20 | 10-10 | 110.5 | 113.0 | 223.5 | 03-21 to 05-03 |

Each side's last 5–7 games were playoff games (a different, slower regime against strong defences). The windows are context and a sensitivity, not the centre (A6). Preseason 2026-27 games are excluded by rule: Atlanta 4-1 (123-132 v MEM, 123-116 at SA, 119-117 at IND, 113-110 v OKC, 135-111 at DAL), Orlando 3-1 (122-118 at MEM, 105-119 at CLE, 132-116 v CLE, 136-115 v MIA). Three 2026-27 regular-season games had finished before the cutoff (BOS @ DET 234 points, PHI @ NY 206, OKC @ SA 220; mean 220.0, n = 3): width, not a lean.

**Orlando Magic: last 20 competitive games before the cutoff, newest first** (all from the 2025-26 season; the 2026-27 regular season has 0 games; kickoff date UTC)

| # | Date (UTC) | Type | Venue | Opponent | PF-PA | Result | Total | ESPN event id |
|---:|---|---|---|---|---|---|---|---|
| 1 | 2026-05-03 | PO | A | DET | 94-116 | L | 210 | `401869418` |
| 2 | 2026-05-01 | PO | H | DET | 79-93 | L | 172 | `401869417` |
| 3 | 2026-04-29 | PO | A | DET | 109-116 | L | 225 | `401869416` |
| 4 | 2026-04-28 | PO | H | DET | 94-88 | W | 182 | `401869415` |
| 5 | 2026-04-25 | PO | H | DET | 113-105 | W | 218 | `401869414` |
| 6 | 2026-04-22 | PO | A | DET | 83-98 | L | 181 | `401869411` |
| 7 | 2026-04-19 | PO | A | DET | 112-101 | W | 213 | `401869193` |
| 8 | 2026-04-12 | RS | A | BOS | 108-113 | L | 221 | `401811041` |
| 9 | 2026-04-11 | RS | A | CHI | 127-103 | W | 230 | `401811032` |
| 10 | 2026-04-08 | RS | H | MIN | 132-120 | W | 252 | `401811014` |
| 11 | 2026-04-06 | RS | H | DET | 123-107 | W | 230 | `401810999` |
| 12 | 2026-04-05 | RS | A | NO | 112-108 | W | 220 | `401810993` |
| 13 | 2026-04-04 | RS | A | DAL | 138-127 | W | 265 | `401810982` |
| 14 | 2026-04-01 | RS | H | ATL | 101-130 | L | 231 | `401810962` |
| 15 | 2026-03-31 | RS | H | PHX | 115-111 | W | 226 | `401810954` |
| 16 | 2026-03-29 | RS | A | TOR | 87-139 | L | 226 | `401810941` |
| 17 | 2026-03-26 | RS | H | SAC | 121-117 | W | 238 | `401810920` |
| 18 | 2026-03-25 | RS | A | CLE | 131-136 | L | 267 | `401810904` |
| 19 | 2026-03-23 | RS | H | IND | 126-128 | L | 254 | `401810894` |
| 20 | 2026-03-21 | RS | H | LAL | 104-105 | L | 209 | `401810879` |

**Atlanta Hawks: last 20 competitive games before the cutoff, newest first** (all from the 2025-26 season; the 2026-27 regular season has 0 games; kickoff date UTC)

| # | Date (UTC) | Type | Venue | Opponent | PF-PA | Result | Total | ESPN event id |
|---:|---|---|---|---|---|---|---|---|
| 1 | 2026-04-30 | PO | H | NY | 89-140 | L | 229 | `401869393` |
| 2 | 2026-04-29 | PO | A | NY | 97-126 | L | 223 | `401869392` |
| 3 | 2026-04-25 | PO | H | NY | 98-114 | L | 212 | `401869391` |
| 4 | 2026-04-23 | PO | H | NY | 109-108 | W | 217 | `401869389` |
| 5 | 2026-04-21 | PO | A | NY | 107-106 | W | 213 | `401869387` |
| 6 | 2026-04-18 | PO | A | NY | 102-113 | L | 215 | `401869189` |
| 7 | 2026-04-12 | RS | A | MIA | 117-143 | L | 260 | `401811044` |
| 8 | 2026-04-10 | RS | H | CLE | 124-102 | W | 226 | `401811028` |
| 9 | 2026-04-08 | RS | A | CLE | 116-122 | L | 238 | `401811013` |
| 10 | 2026-04-06 | RS | H | NY | 105-108 | L | 213 | `401810998` |
| 11 | 2026-04-03 | RS | A | BKN | 141-107 | W | 248 | `401810977` |
| 12 | 2026-04-01 | RS | A | ORL | 130-101 | W | 231 | `401810962` |
| 13 | 2026-03-30 | RS | H | BOS | 112-102 | W | 214 | `401810947` |
| 14 | 2026-03-28 | RS | H | SAC | 123-113 | W | 236 | `401810933` |
| 15 | 2026-03-27 | RS | A | BOS | 102-109 | L | 211 | `401810922` |
| 16 | 2026-03-25 | RS | A | DET | 130-129 | W | 259 | `401810906` |
| 17 | 2026-03-23 | RS | H | MEM | 146-107 | W | 253 | `401810892` |
| 18 | 2026-03-22 | RS | H | GS | 126-110 | W | 236 | `401810881` |
| 19 | 2026-03-21 | RS | A | HOU | 95-117 | L | 212 | `401810873` |
| 20 | 2026-03-19 | RS | A | DAL | 135-120 | W | 255 | `401810861` |

Rows from the ESPN team schedule API (final scores, ESPN event ids), retrieved 2026-10-21 22:52:56Z–22:53:04Z; the opponent column is ESPN's abbreviation. Postseason rows are marked PO.

#### A4. Distribution, baseline and arithmetic
**League level.** ESPN standings, 2025-26 regular season, 30 teams: league points per team-game LM = 115.607 (game total 231.21). Earlier seasons for the regression: 2024-25 113.83 (227.65); 2023-24 114.21 (228.42). Repo reference (BASE_RATES_REGISTER §7.1, NBA 2025-26): mean total 230.7, home margin +1.72 (95% CI 0.81–2.64), raw SD total 21.7, margin 16.4, residual SD 19.4 / 15.1, overtime in 4.4% of games adding 25.2 points on average. The 0.5-point gap between 231.21 and 230.7 is disclosed and not reconciled.

**Carry-over (measured, ESPN standings).** On league-centred points for and against per game, regressing the next season on the previous one, 30 teams per pair: offence 0.362 (2023-24 → 2024-25) and 0.266 (2024-25 → 2025-26), mean **0.314**; defence 0.543 and 0.736, mean **0.640**. Residual team SD of (PF+PA) 6.08 and 4.77 (mean 5.43); of (PF−PA) 4.94 and 5.39 (mean 5.17).

**Team centres.** Deviations from LM in 2025-26: Atlanta PF +2.85, PA +0.44; Orlando PF +0.13, PA −0.50. Carried: Atlanta o′ = 0.314 × 2.85 = +0.897, d′ = 0.640 × 0.44 = +0.283; Orlando o′ = 0.314 × 0.13 = +0.043, d′ = 0.640 × (−0.50) = −0.318.

**Centre (TB-1-MD form, Orlando home).** T = 2 × 115.607 + (0.043 + 0.283 + 0.897 − 0.318)/2 = 231.214 + 0.453 = **231.667**; × EARLY_SEASON 0.988 = **228.886**. M = [(0.043 + 0.318) − (0.897 − 0.283)]/2 + 1.72 = −0.127 + 1.72 = **+1.593** (Orlando). Expected score Orlando 115.24, Atlanta 113.65.

**Mixture and widths.** Offsets from the regression residuals: total d = √2 × (√2 × 5.43/2) = ±5.43; margin d = √2 × (√2 × 5.17/2) = ±5.17. Nine states (total case × margin case), weights 0.25/0.50/0.25 each, independent. Within each state the total and the margin are independent normals with SD 19.4 and 15.1 (correlation between total and margin assumed 0; not measured here). Effective SD total √(19.4² + 0.5 × 5.43²) = **19.78**; margin √(15.1² + 0.5 × 5.17²) = **15.54**. Check against the width rule: 19.78 ≥ 0.85 × 19.4 = 16.5. Row probabilities: Under L = Σ w Φ((L − μT)/19.4); Magic −k = Σ w [1 − Φ((k − μM)/15.1)]; Hawks +k is its complement; Magic win k = 0.

**Baseline (BASELINE_LEAGUE_V1, league-only, frozen).** Total ~ N(230.7 × 0.988 = 227.93, 21.7); margin ~ N(+1.72, 16.4). Example: Under 233.5 = Φ((233.5 − 227.93)/21.7) = Φ(0.257) = 0.6013; Hawks +2.5 = Φ((2.5 − 1.72)/16.4) = Φ(0.048) = 0.5190. `TEAM_BASELINE_P`: `TB1_EARLY_SEASON` (both teams have 0 games in this season), so TB-1-MD reduces to the league-only baseline and is not separately printed.

**Departure ledger (§8).** No priced row departs from BASELINE_P by more than 0.020. The team model differs from the baseline in only three places: total centre +0.96 (Atlanta's scoring carried over), margin −0.13 (the Hawks' offence edge offsets the Magic's defence) and a wider total spread (19.78 against 19.4 within case; the baseline uses the raw 21.7).

**Checks (toolkit §11).** Complements sum to 1: Under 233.5 + Over 233.5 = 0.5922 + 0.4078; Hawks +2.5 + Magic −2.5 = 0.5233 + 0.4767; moneylines 0.5408 + 0.4592. All 30 rows come from the one object.

**Full priced ladder (30 rows):**

| Contract | p_card | p_base | BASELINE_P | Departure |
|---|---:|---:|---:|---:|
| Under 239.5 | 0.7042 | 0.7078 | 0.7030 | +0.0012 |
| Under 237.5 | 0.6684 | 0.6715 | 0.6704 | -0.0020 |
| Under 235.5 | 0.6310 | 0.6334 | 0.6364 | -0.0054 |
| Hawks +6.5 | 0.6239 | 0.6274 | 0.6147 | +0.0092 |
| Hawks +5.5 | 0.5992 | 0.6021 | 0.5911 | +0.0081 |
| Under 233.5 | 0.5922 | 0.5940 | 0.6013 | -0.0091 |
| Hawks +4.5 | 0.5742 | 0.5763 | 0.5673 | +0.0069 |
| Under 231.5 | 0.5526 | 0.5536 | 0.5653 | -0.0127 |
| Hawks +3.5 | 0.5488 | 0.5502 | 0.5432 | +0.0056 |
| Magic win (ML) | 0.5408 | 0.5420 | 0.5418 | -0.0010 |
| Magic -0.5 | 0.5280 | 0.5289 | 0.5297 | -0.0017 |
| Over 227.5 | 0.5279 | 0.5285 | 0.5079 | +0.0200 |
| Hawks +2.5 | 0.5233 | 0.5239 | 0.5190 | +0.0043 |
| Under 229.5 | 0.5124 | 0.5126 | 0.5288 | -0.0164 |
| Magic -1.5 | 0.5024 | 0.5025 | 0.5054 | -0.0030 |
| Hawks +1.5 | 0.4976 | 0.4975 | 0.4946 | +0.0030 |
| Over 229.5 | 0.4876 | 0.4874 | 0.4712 | +0.0164 |
| Magic -2.5 | 0.4767 | 0.4761 | 0.4810 | -0.0043 |
| Under 227.5 | 0.4721 | 0.4715 | 0.4921 | -0.0200 |
| Hawks +0.5 | 0.4720 | 0.4711 | 0.4703 | +0.0017 |
| Hawks win (ML) | 0.4592 | 0.4580 | 0.4582 | +0.0010 |
| Magic -3.5 | 0.4512 | 0.4498 | 0.4568 | -0.0056 |
| Over 231.5 | 0.4474 | 0.4464 | 0.4347 | +0.0127 |
| Magic -4.5 | 0.4258 | 0.4237 | 0.4327 | -0.0069 |
| Over 233.5 | 0.4078 | 0.4060 | 0.3987 | +0.0091 |
| Magic -5.5 | 0.4008 | 0.3979 | 0.4089 | -0.0081 |
| Magic -6.5 | 0.3761 | 0.3726 | 0.3853 | -0.0092 |
| Over 235.5 | 0.3690 | 0.3666 | 0.3636 | +0.0054 |
| Over 237.5 | 0.3316 | 0.3285 | 0.3296 | +0.0020 |
| Over 239.5 | 0.2958 | 0.2922 | 0.2970 | -0.0012 |

#### A5. Supplied contracts, W/P/L/V (unconditional; no push at half-point lines)
| Contract | W | P | L | V | p_card |
|---|---:|---:|---:|---:|---:|
| Hawks +2.5 | 0.5233 | 0 | 0.4767 | 0 | 0.5233 |
| Magic −2.5 | 0.4767 | 0 | 0.5233 | 0 | 0.4767 |
| Combined Over 233.5 | 0.4078 | 0 | 0.5922 | 0 | 0.4078 |
| Combined Under 233.5 | 0.5922 | 0 | 0.4078 | 0 | 0.5922 |

Joint wins of supplied rows (total and margin independent within each case): Hawks +2.5 and Under 233.5 0.3099; Magic −2.5 and Under 233.5 0.2823; Hawks +2.5 and Over 233.5 0.2134; Magic −2.5 and Over 233.5 0.1944. Complementary pairs cannot both win.

#### A6. Adjustments and sensitivity
| Driver | Treatment | Effect |
|---|---|---|
| Home edge | +1.72 in M (CI 0.81–2.64, SE about 0.47) | Orlando +1.6 |
| EARLY_SEASON | Total × 0.988 (BASE_RATES regime table, 25 seasons, 95% CI 0.982–0.993) | −2.8 points on the total; the main driver of every Under |
| Independent re-check of EARLY_SEASON | ESPN scoreboards, first 7 days of the last three seasons v each full-season mean: 2025-26 1.023 (53 games), 2024-25 0.995 (52), 2023-24 0.978 (51); pooled 0.999 (156 games, SE about 0.006) | Does not confirm the multiplier on three seasons; precision-weighting the 25-season and three-season estimates gives about 0.990 (0.5 points). Base keeps the repo value (0.988) |
| Availability | Gueye, Veesaar (ATL) and Black, Isaac, Nelson, Penda (ORL) out; no minutes or usage lines retrieved | Width (mixture) only; no numeric shift |
| Rest / travel | Both teams' first regular-season game; last preseason game 10/17 (ATL) and 10/16 (ORL); ATL travels from Atlanta (same region) | 0 |
| Previous-season windows | L20 differs from the carried centre (A3) | Sensitivity only |

| Sensitivity | Total centre | Magic margin | Under 239.5 | Under 237.5 | Hawks +6.5 | Under 233.5 | Hawks +2.5 | Magic −2.5 | Over 233.5 | Magic win |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Base (card)** | 228.89 | +1.59 | 0.7042 | 0.6684 | 0.6239 | 0.5922 | 0.5233 | 0.4767 | 0.4078 | 0.5408 |
| No EARLY_SEASON multiplier | 231.67 | +1.59 | 0.6540 | 0.6160 | 0.6239 | 0.5369 | 0.5233 | 0.4767 | 0.4631 | 0.5408 |
| Margin carried directly (slope 0.59) | 228.89 | +1.20 | 0.7042 | 0.6684 | 0.6335 | 0.5922 | 0.5334 | 0.4666 | 0.4078 | 0.5307 |
| Last-20 windows (k = 2) instead of carry-over | 224.43 | +0.40 | 0.7770 | 0.7456 | 0.6526 | 0.6767 | 0.5537 | 0.4463 | 0.3233 | 0.5103 |
| Within-case SD 21.7 / 16.4 (raw) | 228.89 | +1.59 | 0.6850 | 0.6520 | 0.6148 | 0.5829 | 0.5215 | 0.4785 | 0.4171 | 0.5378 |
| Home edge 1.25 (−1 SE) | 228.89 | +1.12 | 0.7042 | 0.6684 | 0.6353 | 0.5922 | 0.5353 | 0.4647 | 0.4078 | 0.5288 |
| Home edge 2.19 (+1 SE) | 228.89 | +2.06 | 0.7042 | 0.6684 | 0.6124 | 0.5922 | 0.5112 | 0.4888 | 0.4078 | 0.5528 |

Reading: the order of the top three rows (Unders) and the Orlando lean survive every variant except the multiplier, which moves the Under rows by about 5 points and promotes Hawks +6.5 to Rank 2. Orlando's win probability stays between 0.51 and 0.55; the supplied handicap rows stay between 0.45 and 0.55. Plausible ranges are sensitivity, not confidence intervals.

#### A7. Family rules and dependence
Rank 1 is a totals Under: width rule K-13 satisfied (effective SD 19.78 ≥ 19.4). Nested Unders are one view, so the primary slate is two views at most (a total view and the Hawks +6.5 margin view); the framework counts only Ranks 1–2 as primary. Underdog cushions (C-PLUS-CUSHION): Hawks +k = P(Hawks win) + P(lose by ≤ k) (0.4592 + 0.0641 = 0.5233 for +2.5). The repo's weaker-team cover bands are 0.35–0.43 for +2.5, 0.38–0.45 for +3.5 and 0.44–0.51 for +5.5. The Hawks rows exceed those bands by more than 0.05 (+2.5: 0.5233; +5.5: 0.5992; +6.5: 0.6239) and no favourite-side mechanism supports a cushion, so Rank 4 carries the flag `PLUS_CUSHION_UNSUPPORTED` as disclosure. The bands describe weaker teams in typical matchups; this is a near pick'em (the league-only BASELINE_P for the same rows, 0.5190 / 0.5911 / 0.6147, also exceeds them), so the excess comes from the matchup, not from a cushion argument. The RM-1 pair flip is non-operative since v10 (ranking is by p_card) and is not applied. BK-P1 (rules): NBA 48 minutes, five-minute overtime. BK-P2 (availability): official injury lists yes; official starting fives and bench no → rows depending on a named player are not issued. BK-P3/P4: all rows full game including overtime, operator terms unknown. No ML or RL output was read before this card (MLSCOPE-v2).

#### A8. Sources (opened; retrieval times UTC, 21 Oct 2026)
| # | Source | Field used | Retrieved | Role |
|---|---|---|---|---|
| 1 | ESPN scoreboard API https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261021 | Fixture, venue, 23:00Z, scheduled status | 22:50:42 | Provider |
| 2 | ESPN summary API https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909834 | Injury feed and status only; odds and win-probability fields not read | 22:50:54, 22:52:29 | Provider |
| 3 | NBA official injury report https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-21_06_30PM.pdf | Both teams' out lists (6:30 PM ET report) | 22:51:03 | Field owner |
| 4 | RotoWire NBA lineups https://www.rotowire.com/basketball/nba-lineups.php | "Confirmed Lineup" starters, referees | 22:51:37 | Third-party aggregator |
| 5 | ESPN team schedule API (ATL id 1, ORL id 19; seasons 2026 and 2027; types 1–3) | 40 dated rows with final scores; target event excluded by id | 22:52:56–22:53:04 | Provider |
| 6 | ESPN team statistics API (`/teams/{1,19}/statistics?season=2026&seasontype=2`) | FGA, OREB, TO, FTA, PF | 22:54:03 | Provider |
| 7 | ESPN roster API and past box scores (each team's last regular-season and last playoff game; ESPN event ids in the A3 row tables) | Current rosters; minutes by player for continuity | 22:54:47–22:55:06 | Provider |
| 8 | ESPN standings API https://site.api.espn.com/apis/v2/sports/basketball/nba/standings?season=2024, 2025, 2026 | League level, carry-over regressions | 22:55:27 | Provider |
| 9 | ESPN scoreboards 2026-10-20 and 2026-10-21 (completed games only); first 7 days of 2023-24, 2024-25, 2025-26 | Early-season context and the multiplier re-check | 22:53:35; 22:59:07–22:59:44 | Provider |
| 10 | Repo: BASE_RATES_REGISTER §7.1 and the regime table; PROBABILITY_TOOLKIT §1, §4; RULES_BASKETBALL §0; SELECTION_RULES §§2–5, 9; ARCHIVE_USE_GUIDE R2 | Anchors, recipes, rules | 22:50 | Controls |

Independence: sources 1, 2, 5–9 are one lineage (ESPN). The injury lists are corroborated across the NBA report (3) and ESPN (2); starters rest on RotoWire (4) alone. Not reachable or empty: NBA CDN live data ("Access Denied"), the teams' X timelines, official referee assignment. Basketball-Reference was not used. Not used: odds, tips, previews, fantasy content, the ESPN `pickcenter`/`odds`/`predictor` blocks.

#### A9. Completion receipt
| Procedure | Status |
|---|---|
| Authority, identity, duplicate | DONE |
| Official start and zone | DONE (ESPN + NBA report: 23:00Z; actual tip NOT_VERIFIED) |
| Timing / known-at | DONE: CLEAN_PRE_START_INPUTS / POST_START_ISSUE; no outcome viewed |
| Injuries both sides | DONE (official + ESPN agree) |
| Starting fives | PARTIAL: single third-party source; official feed unreachable |
| Bench, minutes, rotation | INCOMPLETE (not published); handled as width |
| L5/L10/L15/L20 with true n, dated rows | DONE for 2025-26 (flagged as previous-season; 2026-27 has 0 games) |
| Rules, endpoint, overtime | DONE (full game including overtime; operator terms unknown) |
| Distribution, arithmetic, baseline | DONE (one joint object; BASELINE_LEAGUE_V1 30/30 rows) |
| Supplied rows assessed | DONE (all four) |
| Gate, dependence, shadows | DONE |
| Player rows | NOT_ISSUED (no supported inputs) |
| Model shadow | See the dated record below |
| Settlement / import | NOT_PERFORMED |

#### Model shadow record (2026-10-21T23:03:35Z, after the card was written and read back)
`python -m ml pregame run` → **`NOT_RUN_NO_RELEASE`**: no active forecast-cycle release for Basketball/NBA (active releases: Baseball/MLB, Ice Hockey/NHL). Receipt `research/pregame/LOCAL-20261022F6K3OJNO-G0003/20261021T230335428107Z_PREGAME.csv`. Nothing was frozen in the shadow ledger; the card's p_card, ranks and picks are unchanged. The run happened after the scheduled start (23:00Z), so it could not have been a pre-start freeze in any case.

`SPORTS_ONLY_MARKET_BLIND: APPLIED` · `RESEARCH_ONLY_NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD LOCAL-20261022F6K3OJNO-G0003 -->

<!-- BEGIN CARD LOCAL-20261022F6K3OJNO-G0004 -->
## Card - LOCAL-20261022F6K3OJNO-G0004 - BASKETBALL / NBA 2026-27 regular season - Milwaukee Bucks @ Washington Wizards - 21 Oct US / 22 Oct AEDT

- **Local event key:** LOCAL-20261022F6K3OJNO-G0004 / LOCAL_UNIMPORTED_EVENT
- **Canonical ID / assignment stage:** NOT_ASSIGNED / PROMPT_4_IMPORT; no canonical allocation or reservation
- **Event key / native IDs / aliases:** NBA-20261021-MIL-WAS; NBA0022600086; ESPN401909835; MIL / WSH / WAS
- **Authority:** LOCAL_WORKING_TREE; main; read HEAD 88724540185c4546fb10addd71798008b3fdc939; MDS-2026.10.22-v23.0 / CR-2026.10.22-R1 / SCV-2026.10.16-v11 / SEL-2026.10.12-v3; no uncommitted control changes at 2026-10-21T23:14:52+00:00
- **Analysis status:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY; RESEARCH_ONLY_NOT_CERTIFIED; INFORMATION_INCOMPLETE
- **Probability method:** Supported rotation scoring-budget approximation,50% shrink to fresh league regulation mean; nine-case bivariate integer-score distribution, measured covariance, widened uncertainty and explicit overtime kernel. Standalone arithmetic helper outside repo; no fitted forecast/model output. PROBABILITY_TOOLKIT sections1/4/8/11; every input below.
- **Learning record:** LEARN-v2 Markdown tables:40 dated prior-team-game rows,30 official active players,4 injury entries,19 prior-player rates. LEARN_RECORD_INCOMPLETE: independent regulation-quarter corroboration, starter-role second lineage and current minutes/usage remain missing. No learning-store export/ingest.
- **Future learning:** PENDING_SETTLEMENT; no target outcome labels or feedback
- **Timing:** Primary input captures2026-10-21 22:51-22:57Z, before scheduled23:00Z. Preparation 2026-10-21T23:14:52+00:00; actual insertion in dated receipt below. CLEAN_PRE_START_INPUTS / POST_SCHEDULED_START_ISSUE; first play NOT_VERIFIED. Later verification does not alter primary inputs; no target live score, statistics or outcome read.
- **Scheduled start:** 2026-10-21 19:00 EDT (America/New_York,UTC-04) =23:00Z =2026-10-22 10:00 AEDT (UTC+11), Capital One Arena. User10:10 estimate retained as estimate, not verified actual tip.
- **Scheduled lead / band:** -14.87 minutes at preparation; POST_SCHEDULED_START; not a pre-start-issued prospective forecast
- **Endpoint / definition:** Primary: full game including all overtime, points, half lines; W+L=1,P=V=0 conditional on a normally completed game. FROZEN_FRAMEWORK_CONVENTION; actual operator overtime/postponement/abandonment terms UNKNOWN_DEFINITION. Supplied regulation-only alternatives also frozen A5. Monetary EV NOT_COMPUTED.
- **Distribution object:** MILWAS-ROTATION50-9CASE-OT54; regulation0..240 per side, final storage0..300, normalized common grid, no final tie
- **Expected score:** WAS123.143786 SD15.379401; MIL116.140155 SD15.352523; total239.283942 SD24.111223; WAS-MIL+7.003631 SD19.055205. Full-game points; means, not an exact-score mode.
- **Baseline:** BASELINE_LEAGUE_V1: empirical2025-26 NBA regular-season1230 distinct completed fixtures, same line/endpoint/home-away orientation; no team/availability inputs. Finals independently agree with Basketball-Reference. Prior-season comparison, not current-regime calibration.
- **Regime flags / context:** EARLY_SEASON; both current regular-season n0; materially changed rotations. No borrowed early-season mean multiplier.
- **Settlement fields / capture plan:** Prompt3 only: NBA0022600086 final score, quarters1-4, overtime and final-time evidence; ESPN401909835 corroboration. Masks A5. Fragile capture due2026-10-23T22:00+11:00,36h after scheduled start; review normally within72h of verified final. Next authorized prompt3 operator; automation NO; no retrospective requested.
- **Known-at:** Decisive fixture, initial official starter/active fields,18:45ET injury PDF, player rates and league finals/OT lines captured before23:00Z. Source publication UNKNOWN unless exposed; capture proves availability by capture time.19:00ET PDF and23:03Z lineup recheck unchanged; later historical checks corroborate old facts only.
- **Lineup state / issue step:** STARTERS_OFFICIAL_CONFIRMED / SELECTED_BENCH_OFFICIAL_ACTIVE both sides from NBA exact-game starter/status fields, initial ~22:54Z; unchanged at23:03:24Z. Injury report19:00ET checked23:03:53Z, unchanged from18:45ET. Minutes and usage are assumptions.
- **Pricing basis:** MIXTURE: total offsets -12/0/+12 and WAS-margin offsets -5/0/+5, each weights0.25/0.50/0.25, Cartesian product. Numerical epsilon1e-6; not a parameter-error bound. p_base shown.
- **Form windows:** Eligible current-regime L5/L10/L15/L20/season n0 both teams. Previous-season windows excluded by R2 coach/roster change; historical descriptive windows/40 rows retained A3. Windows overlap; counted once.

### Decision block

**Washington is the potential winner, but there is no stable strong slate.** The current-player scoring budget favours Washington; the supplied -4.5 remains below the0.62 Rank-1 floor. These are the four highest eligible probabilities on a fixed diagnostic ladder. **All four are hypothetical ANALYST_DERIVED thresholds; market availability and prices NOT_VERIFIED.** Easier lines create higher probabilities, not proven value or skill. No supported player props.

| Rank / role | Contract: full game incl OT | p_card | p_base | BASELINE_P (W/1230) | Line-centre / z | Failure route |
|---|---|---|---|---|---|---|
| 1 PICK | Combined under 268.5 incl OT | 0.887555 | 0.902513 | 0.964228 (1186/1230) | +29.216 points / z=+1.212 | High shooting efficiency / pace / OT;269+ total |
| 2 PICK | WAS team total over 104.5 incl OT | 0.886684 | 0.897408 | 0.818699 (1007/1230) | -18.644 points / z=-1.212 | WAS attack or minutes disappoint;104 or fewer |
| 3 INFORMATIONAL | MIL team total under 134.5 incl OT | 0.883555 | 0.894186 | 0.933333 (1148/1230) | +18.360 points / z=+1.196 | MIL hot shooting or OT;135+ points |
| 4 INFORMATIONAL | WAS +14.5 incl OT | 0.871927 | 0.875986 | 0.843089 (1037/1230) | -21.504 points / z=-1.128 | WAS loses by15+; new-unit fit fails |

**Baseline coverage:**4/4 ranked,108/108 priced. **Rank-1 gate:** RANK1_UNSTABLE; p=0.887555175071>=0.62, best non-complementary eligible alternative WAS_OVER_104.5 p=0.886683826371; gap=0.000871348701<0.04. RET03 excluding other total lines gives same alternative and failure. Rank-2 floor PASS; no PRECISION_TIE.

**Joint loss:** 0.000006550288 unconditional. Both fail only with total>=269 and WAS<=104, requiring MIL>=165. Rare under this object, not impossible or proven skill. Empirical0/1230 does not establish true zero. P(both decisive)=1 under completed-game convention. RET04=WAS Over104.5. XCARD6=TOTAL_OVER_213.5, p=0.858301, baseline=0.814634, joint0: disjoint losing sets total>=269 and total<=213, MECHANICALLY_PROTECTED; NOT_PRIMARY.

**Base-only shadow:** WAS Over104.5 0.897408, MIL Under134.5 0.894186; gate gap0.003221, RANK1_UNSTABLE; joint0.005775. ADJUSTMENT_DEPENDENT: top two change without mixture; base Under268.5 exceeds0.90 ceiling. Delta shadow top two: WAS Over119.5 / WAS Over114.5, p=0.594478/0.713127, baseline=0.400000/0.551220, delta=+0.194478/+0.161907, nested joint loss0.286873; NOT_PRIMARY.

**Potential winner:** WAS0.645699, MIL0.354301, final draw0. Mean score approximately WAS123-MIL116; not an exact-score forecast. Nine-case WAS winner range 0.547-0.739.

**Supplied four ordered by p:**
| Order | Supplied full-game contract | p_card | p_base | BASELINE_P | Assessment |
|---|---|---|---|---|---|
| 1 | WAS -4.5 incl OT | 0.553356 | 0.554197 | 0.450407 | Best supplied direction; needs WAS win by5+, sensitive to role portability |
| 2 | Combined over 238.5 incl OT | 0.510388 | 0.510992 | 0.331707 | Coin flip; total direction reverses in scenarios |
| 3 | Combined under 238.5 incl OT | 0.489612 | 0.489008 | 0.668293 | Coin flip; no strong Under conclusion |
| 4 | MIL +4.5 incl OT | 0.446644 | 0.445803 | 0.549593 | Can cover with a close loss, but weaker than opposing direction in this centre |

None reaches0.62. All supplied rows retained. No prices supplied: fair odds=1/p only, monetary EV NOT_COMPUTED. No settlement/retrospective.

### Appendix

#### A1. Identity, timing, authority and custody

NBA0022600086 / ESPN401909835 and arena listing agree on fixture and23:00Z scheduled start. Initial ESPN scheduled; NBA gameStatus1 and played0. Safe23:03:24Z refresh returned gameStatus1 and unchanged roles; only status/name/role fields extracted, no performance. Actual firstplay NOT_VERIFIED. Preparation 2026-10-21T23:14:52+00:00; insertion/readback receipt below.

Duplicate search: rg names/native IDs over all active minis, prediction logs and GAME_LOG_STATUS_CURRENT found no target. Current HEAD88724540185c4546fb10addd71798008b3fdc939; initial read HEAD1ccaf3dd124e20083e8485f208811d5fc528f903. Another chatbot appended Hawks-Magic G0003 during research; complete new card re-read, preserved. No canonical state changed.

Task-scoped issuing writer: Codex repository agent for this MIL-WAS append and post-card receipt only. Owner instruction explicitly requests this chatbot append at the end of the same document without overwriting other chatbot work; applied as authorization for this event-scoped appointment. Original named writer/custodian remains unchanged; no assertion another chatbot stopped. Exclusive Windows write-sharing and compare-before-write protect concurrent bytes. This records the interpretation rather than inventing an independent owner lease message.

Reading receipt completed by2026-10-21T23:14:52+00:00, LOCAL_WORKING_TREE main: CURRENT_STATE current table; CURRENT_RULES sections0-1/5-10; METHOD current procedure; SELECTION_RULES1-10; CARD_AND_LOG_TEMPLATES2-3/3a/3b/C1-C22; complete prompt1 core+BASKETBALL; RULES_BASKETBALL0/current overrides; SOURCES3.2/3.13/firewall; BASE_RATES_REGISTER3/7.1 historical references; LEAGUE_PROFILES current admission; ARCHIVE_USE_GUIDE R2; HISTORICAL_SOURCE_PROTOCOL; ROSTER_AVAILABILITY_PROTOCOL1-6; TIMING_RESEARCH_PROTOCOL; RESEARCH_COMPLETION_PROTOCOL; RESEARCH_EXHAUSTIVENESS_PROTOCOL; RESEARCH_SOURCE_REGISTER; MINI_LOG_IDENTITY_PROTOCOL1-6; COMMON_OPERATING_PROTOCOL; toolkit1/4/8/11; GAME_LOG_STATUS_CURRENT current section; entire active mini plus new G0002/G0003. Local files accessible, no content fallback needed. Standing fallback https://github.com/danisgreat/Sports-Research/tree/main ; Drive optional, not controls. No fitted model outputs read before card.

#### A2. Frozen contracts and recipe

Original supplied: Bucks +4.5; Wizards -4.5; Combined Total: Over 238.5 Points; Combined Total: Under 238.5 Points. Primary full game incl OT; alternate regulation-only reading A5 because operator terms absent. Half lines no push. Abandonment/void treatment not invented.

PREPRICING_PLAN frozen externally before pricing: both winners; each team handicap +/-4.5,9.5,14.5,19.5,24.5; combined O/U198.5..278.5 step5; each team O/U89.5..149.5 step5.108 unique rows,91 eligible p<=0.90,17 excluded true p>0.90, never clipped. Restricted declared ladder, not every possible market. No thresholds moved after pricing. Pre-issuance structural amendment replaced midpoint integration with Gauss-Legendre and a league-derived diagonal tie adjustment on the whole grid; candidates, centres and scenario weights unchanged; scratch midpoint numbers never issued.

#### A3. Availability and online prior-game learning record

Exact-game NBA starter/status fields; initial pre-start capture and unchanged23:03:24Z recheck. ACTIVE indicates selection, not guaranteed minutes or full medical fitness. Unpopulated inactives array does not override the timed injury report.

| Team | Player | Role | Status | Source / time |
|---|---|---|---|---|
| MIL | Jaime Jaquez Jr. | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Kyle Kuzma | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Myles Turner | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Tyler Herro | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Ryan Rollins | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Nate Ament | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Brayden Burries | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Ousmane Dieng | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | AJ Green | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Kasparas Jakučionis | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Caris LeVert | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Bogoljub Marković | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Jericho Sims | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Gary Trent Jr. | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| MIL | Kel'el Ware | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Bilal Coulibaly | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Anthony Davis | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Alex Sarr | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Kyshawn George | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Trae Young | STARTER | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Deandre Ayton | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Reece Beekman | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Bub Carrington | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Justin Champagnie | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Anthony Gill | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Tre Johnson | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Tre Mann | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Khris Middleton | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Felix Okpara | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |
| WAS | Will Riley | SELECTED_BENCH | ACTIVE | NBA0022600086,~22:54Z; publication UNKNOWN |

| Team | Player | Official report status | Reason |
|---|---|---|---|
| MIL | Nate Ament | Available | No injury reason in report |
| WAS | AJ Dybantsa | Out | Left ankle sprain |
| WAS | Tristan Vukcevic | Out | Left hip impingement |
| WAS | Jamir Watkins | Out | Left ACL repair / surgery |

18:45ET PDF downloaded22:53:10Z;19:00ET PDF downloaded23:03:53Z, rendered/visually verified, same4 entries. No additional questionable/probable/rested MIL-WAS player listed there; absence from report does not establish unrestricted health. ESPN corroborates Wizards absences; roster membership does not confirm starts. Old depth-chart/injury snippets not adopted. Kevin Porter Jr is not inserted from an obsolete roster; Giannis/Portis no longer define this Milwaukee squad.

Actual availability ladder: official match CDN403 -> official NBA SSR starter/status fields succeed; both club official rosters and ESPN18-player squads opened; official medical index/PDF plus ESPN injury fields; NBA daily-lineups HTML projected/empty shell. Current minute caps/coach-confirmed rotation not verified. Independent second collector for starting roles missing; overall INFORMATION_INCOMPLETE. No invented absence penalty.

Current regular-season n0 each. Milwaukee new coach and substantial player turnover; Washington Young/Davis/Sarr starting unit differs materially. R2 excludes previous-season team games as current form. Old records MIL32-50,WAS17-65 are descriptive only. Current-lineup possession/efficiency/opponent calibration missing.

**MIL current-regime form:**
| Window | Eligible n | PF / PA / margin | Status |
|---|---|---|---|
| L5 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| L10 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| L15 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| L20 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| Season2026-27 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |

| Historical window | n | UTC dates | Wins | PF/g | PA/g | Margin/g | Admission |
|---|---|---|---|---|---|---|---|
| L5 | 5 | 2026-04-05 to 2026-04-12 | 2 | 112.600000 | 116.400000 | -3.800000 | Historical only, excluded |
| L10 | 10 | 2026-03-28 to 2026-04-12 | 3 | 110.800000 | 118.700000 | -7.900000 | Historical only, excluded |
| L15 | 15 | 2026-03-18 to 2026-04-12 | 4 | 108.200000 | 120.133333 | -11.933333 | Historical only, excluded |
| L20 | 20 | 2026-03-09 to 2026-04-12 | 5 | 108.300000 | 120.900000 | -12.600000 | Historical only, excluded |
| Season2025-26 | 82 | 2025-10-23 to 2026-04-12 | 32 | 110.634146 | 116.841463 | -6.207317 | Historical only, excluded |

| Historical window | Venue | n | PF/g | PA/g |
|---|---|---|---|---|
| L10 | H | 6 | 114.666667 | 118.166667 |
| L10 | A | 4 | 105.000000 | 119.500000 |
| L20 | H | 10 | 114.300000 | 121.400000 |
| L20 | A | 10 | 102.300000 | 120.400000 |

Descriptive blend B_PF=109.975000,B_PA=119.033333, each mean(L5,L10,L15,L20).k2 toolkit4.3; comparison shrink(13.5*B+2*LM)/15.5 gives PF110.701803,PA118.591319; NOT USED. Current n0 shrinks entirely to LM. Opponent pre-game ratings unavailable, no opponent adjustment. Windows overlap; counted once.

| # | UTC prior start | H/A | Opponent | Final PF-PA | Regulation PF-PA | OT periods | Source URL | Retrieved / published |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-04-12T22:00Z | A | PHI | 106-126 | 106-126 | 0 | https://www.espn.com/nba/game/_/gameId/401811046 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 2 | 2026-04-11T00:00Z | H | BKN | 125-108 | 125-108 | 0 | https://www.espn.com/nba/game/_/gameId/401811034 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 3 | 2026-04-08T23:00Z | A | DET | 111-137 | 111-137 | 0 | https://www.espn.com/nba/game/_/gameId/401811015 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 4 | 2026-04-07T23:30Z | A | BKN | 90-96 | 90-96 | 0 | https://www.espn.com/nba/game/_/gameId/401811005 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 5 | 2026-04-05T19:30Z | H | MEM | 131-115 | 131-115 | 0 | https://www.espn.com/nba/game/_/gameId/401810990 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 6 | 2026-04-04T00:00Z | H | BOS | 101-133 | 101-133 | 0 | https://www.espn.com/nba/game/_/gameId/401810981 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 7 | 2026-04-02T00:00Z | A | HOU | 113-119 | 113-119 | 0 | https://www.espn.com/nba/game/_/gameId/401810965 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 8 | 2026-04-01T00:00Z | H | DAL | 123-99 | 123-99 | 0 | https://www.espn.com/nba/game/_/gameId/401858694 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 9 | 2026-03-29T19:30Z | H | LAC | 113-127 | 113-127 | 0 | https://www.espn.com/nba/game/_/gameId/401810937 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 10 | 2026-03-28T19:00Z | H | SA | 95-127 | 95-127 | 0 | https://www.espn.com/nba/game/_/gameId/401810931 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 11 | 2026-03-26T02:00Z | A | POR | 99-130 | 99-130 | 0 | https://www.espn.com/nba/game/_/gameId/401810916 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 12 | 2026-03-24T02:30Z | A | LAC | 96-129 | 96-129 | 0 | https://www.espn.com/nba/game/_/gameId/401810901 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 13 | 2026-03-22T02:00Z | A | PHX | 108-105 | 108-105 | 0 | https://www.espn.com/nba/game/_/gameId/401810886 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 14 | 2026-03-20T01:00Z | A | UTAH | 96-128 | 96-128 | 0 | https://www.espn.com/nba/game/_/gameId/401810869 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 15 | 2026-03-18T00:00Z | H | CLE | 116-123 | 116-123 | 0 | https://www.espn.com/nba/game/_/gameId/401810850 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 16 | 2026-03-15T19:30Z | H | IND | 134-123 | 134-123 | 0 | https://www.espn.com/nba/game/_/gameId/401810834 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 17 | 2026-03-14T19:00Z | A | ATL | 99-122 | 99-122 | 0 | https://www.espn.com/nba/game/_/gameId/401810825 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 18 | 2026-03-12T23:30Z | A | MIA | 105-112 | 105-112 | 0 | https://www.espn.com/nba/game/_/gameId/401810812 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 19 | 2026-03-11T00:00Z | H | PHX | 114-129 | 114-129 | 0 | https://www.espn.com/nba/game/_/gameId/401810796 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |
| 20 | 2026-03-09T00:00Z | H | ORL | 91-130 | 91-130 | 0 | https://www.espn.com/nba/game/_/gameId/401810781 | 2026-10-21T22:54:14.226897+00:00; publication UNKNOWN, final captured pre-start |

**WAS current-regime form:**
| Window | Eligible n | PF / PA / margin | Status |
|---|---|---|---|
| L5 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| L10 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| L15 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| L20 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |
| Season2026-27 | 0 | NOT_ESTIMATED | Prior season excluded, roster/coach change |

| Historical window | n | UTC dates | Wins | PF/g | PA/g | Margin/g | Admission |
|---|---|---|---|---|---|---|---|
| L5 | 5 | 2026-04-05 to 2026-04-12 | 0 | 111.000000 | 127.800000 | -16.800000 | Historical only, excluded |
| L10 | 10 | 2026-03-28 to 2026-04-12 | 0 | 113.700000 | 131.800000 | -18.100000 | Historical only, excluded |
| L15 | 15 | 2026-03-17 to 2026-04-12 | 1 | 113.733333 | 130.133333 | -16.400000 | Historical only, excluded |
| L20 | 20 | 2026-03-08 to 2026-04-12 | 1 | 115.050000 | 130.600000 | -15.550000 | Historical only, excluded |
| Season2025-26 | 82 | 2025-10-23 to 2026-04-12 | 17 | 112.902439 | 124.878049 | -11.975610 | Historical only, excluded |

| Historical window | Venue | n | PF/g | PA/g |
|---|---|---|---|---|
| L10 | H | 4 | 113.500000 | 135.250000 |
| L10 | A | 6 | 113.833333 | 129.500000 |
| L20 | H | 8 | 111.750000 | 130.625000 |
| L20 | A | 12 | 117.250000 | 130.583333 |

Descriptive blend B_PF=113.370833,B_PA=130.083333, each mean(L5,L10,L15,L20).k2 toolkit4.3; comparison shrink(13.5*B+2*LM)/15.5 gives PF113.659464,PA128.215513; NOT USED. Current n0 shrinks entirely to LM. Opponent pre-game ratings unavailable, no opponent adjustment. Windows overlap; counted once.

| # | UTC prior start | H/A | Opponent | Final PF-PA | Regulation PF-PA | OT periods | Source URL | Retrieved / published |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-04-12T22:00Z | A | CLE | 117-130 | 117-130 | 0 | https://www.espn.com/nba/game/_/gameId/401811042 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 2 | 2026-04-10T23:00Z | H | MIA | 117-140 | 117-140 | 0 | https://www.espn.com/nba/game/_/gameId/401811027 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 3 | 2026-04-09T23:00Z | H | CHI | 108-119 | 108-119 | 0 | https://www.espn.com/nba/game/_/gameId/401811021 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 4 | 2026-04-07T23:00Z | H | CHI | 98-129 | 98-129 | 0 | https://www.espn.com/nba/game/_/gameId/401811003 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 5 | 2026-04-05T19:30Z | A | BKN | 115-121 | 115-121 | 0 | https://www.espn.com/nba/game/_/gameId/401810988 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 6 | 2026-04-04T19:00Z | A | MIA | 136-152 | 136-152 | 0 | https://www.espn.com/nba/game/_/gameId/401810984 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 7 | 2026-04-01T23:00Z | H | PHI | 131-153 | 131-153 | 0 | https://www.espn.com/nba/game/_/gameId/401810960 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 8 | 2026-03-31T02:00Z | A | LAL | 101-120 | 101-120 | 0 | https://www.espn.com/nba/game/_/gameId/401810953 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 9 | 2026-03-29T22:00Z | A | POR | 88-123 | 88-123 | 0 | https://www.espn.com/nba/game/_/gameId/401810942 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 10 | 2026-03-28T02:00Z | A | GS | 126-131 | 126-131 | 0 | https://www.espn.com/nba/game/_/gameId/401810928 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 11 | 2026-03-26T01:00Z | A | UTAH | 133-110 | 133-110 | 0 | https://www.espn.com/nba/game/_/gameId/401810912 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 12 | 2026-03-22T23:30Z | A | NY | 113-145 | 113-145 | 0 | https://www.espn.com/nba/game/_/gameId/401810889 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 13 | 2026-03-21T21:00Z | H | OKC | 111-132 | 111-132 | 0 | https://www.espn.com/nba/game/_/gameId/401810877 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 14 | 2026-03-19T23:00Z | H | DET | 95-117 | 95-117 | 0 | https://www.espn.com/nba/game/_/gameId/401810864 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 15 | 2026-03-17T23:00Z | H | DET | 117-130 | 117-130 | 0 | https://www.espn.com/nba/game/_/gameId/401810848 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 16 | 2026-03-16T23:00Z | H | GS | 117-125 | 117-125 | 0 | https://www.espn.com/nba/game/_/gameId/401810839 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 17 | 2026-03-14T22:00Z | A | BOS | 100-111 | 100-111 | 0 | https://www.espn.com/nba/game/_/gameId/401810826 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 18 | 2026-03-12T23:00Z | A | ORL | 131-136 | 123-123 | 1 | https://www.espn.com/nba/game/_/gameId/401810810 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 19 | 2026-03-10T23:30Z | A | MIA | 129-150 | 129-150 | 0 | https://www.espn.com/nba/game/_/gameId/401810793 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |
| 20 | 2026-03-08T23:00Z | A | NO | 118-138 | 118-138 | 0 | https://www.espn.com/nba/game/_/gameId/401810780 | 2026-10-21T22:54:15.518106+00:00; publication UNKNOWN, final captured pre-start |

League level: freshly reviewed prior-season1230 games; full-game PF/PA per team115.607724; regulation115.054065. Not current team form. Preseason context below excluded from all calculations and baseline.

| Team | UTC date | Fixture / final |
|---|---|---|
| MIL | 2026-10-06 | vs MIN97-116 |
| MIL | 2026-10-08 | at OKC128-126 |
| MIL | 2026-10-11 | at CHA90-105 |
| MIL | 2026-10-15 | vs CHI104-125 |
| MIL | 2026-10-16 | at IND128-127 |
| WAS | 2026-10-08 | at NY111-109 |
| WAS | 2026-10-10 | vs DET114-108 |
| WAS | 2026-10-12 | vs BKN122-131 |
| WAS | 2026-10-17 | at NO106-107 |

Neither side on a back-to-back. Indoor court, weather adjustment0. Travel/fatigue not measured, centre shift0.

#### A4. Distribution inputs, arithmetic and limits

**Supported approximation, not a measured possessions x efficiency forecast.** Current opponent-adjusted ORtg/DRtg and shared usage are unavailable. Adding historical PPG/minute can overcount possessions; Young15GP,Davis20,Herro33 and new roles are major uncertainty.50% shrink and scenario offsets are analyst choices, not trained coefficients. Exact arithmetic does not establish parameter accuracy.

| Team | Player | Prior GP | Prior MPG | Prior PPG | Assumed minutes | PPG/MPG | Budget points | Source | Retrieved UTC |
|---|---|---|---|---|---|---|---|---|---|
| MIL | Ryan Rollins | 74 | 32.1 | 17.3 | 31 | 0.538940810 | 16.707165109 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4591725/overview?season=2026 | 2026-10-21T22:55:39.796847+00:00 |
| MIL | Tyler Herro | 33 | 31.3 | 20.5 | 35 | 0.654952077 | 22.923322684 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4395725/overview?season=2026 | 2026-10-21T22:55:39.588775+00:00 |
| MIL | Jaime Jaquez Jr. | 75 | 28.3 | 15.4 | 29 | 0.544169611 | 15.780918728 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4432848/overview?season=2026 | 2026-10-21T22:55:39.442414+00:00 |
| MIL | Kyle Kuzma | 69 | 26.2 | 13.0 | 29 | 0.496183206 | 14.389312977 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/3134907/overview?season=2026 | 2026-10-21T22:55:39.802175+00:00 |
| MIL | Myles Turner | 71 | 26.9 | 11.9 | 28 | 0.442379182 | 12.386617100 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/3133628/overview?season=2026 | 2026-10-21T22:55:39.439441+00:00 |
| MIL | Caris LeVert | 60 | 19.2 | 7.4 | 20 | 0.385416667 | 7.708333333 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/2991043/overview?season=2026 | 2026-10-21T22:55:39.643575+00:00 |
| MIL | AJ Green | 78 | 29.1 | 10.4 | 18 | 0.357388316 | 6.432989691 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4397475/overview?season=2026 | 2026-10-21T22:55:39.638134+00:00 |
| MIL | Gary Trent Jr. | 65 | 21.2 | 8.1 | 18 | 0.382075472 | 6.877358491 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4277843/overview?season=2026 | 2026-10-21T22:55:39.622779+00:00 |
| MIL | Kel'el Ware | 77 | 22.1 | 11.1 | 20 | 0.502262443 | 10.045248869 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/5105623/overview?season=2026 | 2026-10-21T22:55:40.837642+00:00 |
| MIL | Ousmane Dieng | 57 | 19.3 | 7.6 | 12 | 0.393782383 | 4.725388601 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4997526/overview?season=2026 | 2026-10-21T22:55:41.095483+00:00 |
| WAS | Trae Young | 15 | 25.6 | 17.9 | 33 | 0.699218750 | 23.074218750 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4277905/overview?season=2026 | 2026-10-21T22:55:41.112976+00:00 |
| WAS | Kyshawn George | 48 | 29.0 | 14.8 | 32 | 0.510344828 | 16.331034483 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/5174563/overview?season=2026 | 2026-10-21T22:55:41.751337+00:00 |
| WAS | Bilal Coulibaly | 56 | 26.2 | 11.7 | 30 | 0.446564885 | 13.396946565 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/5104155/overview?season=2026 | 2026-10-21T22:55:41.231371+00:00 |
| WAS | Anthony Davis | 20 | 31.3 | 20.4 | 32 | 0.651757188 | 20.856230032 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/6583/overview?season=2026 | 2026-10-21T22:55:41.282571+00:00 |
| WAS | Alex Sarr | 48 | 27.2 | 16.3 | 29 | 0.599264706 | 17.378676471 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/5160992/overview?season=2026 | 2026-10-21T22:55:41.125762+00:00 |
| WAS | Deandre Ayton | 72 | 27.2 | 12.5 | 19 | 0.459558824 | 8.731617647 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4278129/overview?season=2026 | 2026-10-21T22:55:41.128384+00:00 |
| WAS | Khris Middleton | 63 | 22.8 | 10.2 | 20 | 0.447368421 | 8.947368421 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/6609/overview?season=2026 | 2026-10-21T22:55:42.267068+00:00 |
| WAS | Tre Johnson | 60 | 24.1 | 12.2 | 22 | 0.506224066 | 11.136929461 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/5238230/overview?season=2026 | 2026-10-21T22:55:42.489906+00:00 |
| WAS | Bub Carrington | 82 | 27.7 | 10.7 | 23 | 0.386281588 | 8.884476534 | https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4845374/overview?season=2026 | 2026-10-21T22:55:42.567493+00:00 |

All rates2025-26 regular season; aggregate multi-team season where relevant. Basketball-Reference independently agrees on all19 GP/MPG/PPG rows. Minutes ANALYST_ASSUMPTIONS sum240 each, no base OT minutes. Other selected players0 base minutes is a modelling assumption, not a DNP/availability prediction. Rookie roles and Davis/Sarr/Ayton or Herro/Rollins/LeVert usage competition unmeasured.

Budget_MIL=sum(minutes*PPG/MPG)=117.976655582562; Budget_WAS=128.737498363170. League regulation H=115.904065040650,A=114.204065040650; LM=115.054065040650,HE=1.700000000000. Hcentre=0.5*WASbudget+0.5*LM+HE/2; Acentre=0.5*MILbudget+0.5*LM-HE/2. T_reg=238.411142013516; M_reg=7.080421390304. HE/2 per team creates FULL1.70 home-margin effect, not half the margin.

Unbiased regulation covariance order(home,away)=[[161.07134229031467, 24.525695422942828], [24.525695422942828, 156.2894871235123]]. Multiply whole matrix by1.15^2 (unfitted opener width choice) ->[[213.01685017894113, 32.43523219684189], [32.43523219684189, 206.69284672084495]]. Nine frozen centres and weights:

| Total offset | WAS margin offset | Weight | T_reg | M_reg | Reg tie mass |
|---|---|---|---|---|---|
| -12 | -5 | 0.0625 | 226.411142 | 2.080421 | 0.037504 |
| -12 | 0 | 0.125 | 226.411142 | 7.080421 | 0.035198 |
| -12 | 5 | 0.0625 | 226.411142 | 12.080421 | 0.030817 |
| 0 | -5 | 0.125 | 238.411142 | 2.080421 | 0.037504 |
| 0 | 0 | 0.25 | 238.411142 | 7.080421 | 0.035198 |
| 0 | 5 | 0.125 | 238.411142 | 12.080421 | 0.030817 |
| 12 | -5 | 0.0625 | 250.411142 | 2.080421 | 0.037504 |
| 12 | 0 | 0.125 | 250.411142 | 7.080421 | 0.035198 |
| 12 | 5 | 0.0625 | 250.411142 | 12.080421 | 0.030817 |

Each case integrates exp[-0.5*(score-mu)transpose Sigma^-1(score-mu)] over integer cells[h-0.5,h+0.5]x[a-0.5,a+0.5] using4-point Gauss-Legendre per axis. Gaussian constants cancel at normalization. Restrict each regulation score0..240; increase ALL diagonal cells by a single league-derived multiplier, normalize entire grid, resolve each tie by the54-game OT kernel. No individual-row probability edits.

Tie multiplier=1.812600914824=(54/1230)/[Phi((0.5-HE)/SD_Mreg)-Phi((-0.5-HE)/SD_Mreg)] using uninflated league regulation covariance. Not team-specific OT skill. Mixture regulation tie=0.034679484932; WASregwin=0.624506349433,MILregwin=0.340814165635; three masses sum1.

OT:46 one-OT and8 double-OT fixtures; all54 quarter sums reconcile with finals and first4-quarter scores tied. Each tie scorex receives each observed ordered(homeOTpoints,awayOTpoints) increment with weight1/54; increments and source URLs A8. Mean OT total addition25.222222222222,home OT wins33/54. Double-OT paths included directly; no separate unmeasured five-minute independence assumption. Final tie0,sum1.

Omitted continuous-tail union bound over all9 cases<=3.5647635773e-14 before diagonal correction, multiplier<1.813; no lost OT mass, sum verified1 within1e-12.4-vs8-point quadrature maximum cell difference6.50521303491e-19,base candidate difference2.22044604925e-16. Conservative arithmetic epsilon1e-6; parameter uncertainty much larger.

Final covariance(H,A)=54.562559756503. E(T)=E(H)+E(A); E(M)=E(H)-E(A); Var(T)=Var(H)+Var(A)+2Cov; Var(M)=Var(H)+Var(A)-2Cov. Header moments come from weighted final grid, include between-case variance.

BASELINE_LEAGUE_V1 uses exact separate league-only1230 full-score masks: W=count/1230,L=1-W,P=V=0. Full total mean231.215447,SD19.875976; home margin1.737398,SD16.412953. Historical register n1235 and230.7/21.7 differ; those old profile values are not admitted or silently substituted. Source cohort/exclusions A8. TEAM_BASELINE_P: current n0,k2 makes offence/defence LM,TB1_EARLY_SEASON; same-family league-centred comparison is budget-weight0 in A6, separate from empirical baseline.

High-p mechanism is line distance plus the sourced league scores and disclosed rotation budget, not an asserted validated85% prediction. Under268.5 is29.216points above mean, baseline1186/1230. This row and MIL Under134.5 have LOWER p than their league baselines; WAS Over104.5 and WAS+14.5 higher because budget favours Washington. No odds means no value/EV conclusion. Unsupported current pace/defence effects remain limitations.

#### A5. Complete priced universe and alternate definitions

Every row: unconditional W=p_card,L=1-p_card,P=0,V=0,W+L=1 under normally completed full game incl OT; p=W/(W+L)=W. BASELINE_P=count/1230. Display rounding only; unrounded doubles determine order. Fair odds=1/p, not a quoted bookmaker price.

| Contract key | Tag | p_card=W | L | p_base | BASELINE_P (W/1230) | Eligibility |
|---|---|---|---|---|---|---|
| WAS_OVER_89.5 | DERIVED | 0.985468 | 0.014532 | 0.988873 | 0.984553 (1211/1230) | EXCLUDED_P_ABOVE_0.90 |
| MIL_UNDER_149.5 | DERIVED | 0.984903 | 0.015097 | 0.988300 | 0.996748 (1226/1230) | EXCLUDED_P_ABOVE_0.90 |
| WAS_OVER_94.5 | DERIVED | 0.968367 | 0.031633 | 0.974150 | 0.954472 (1174/1230) | EXCLUDED_P_ABOVE_0.90 |
| MIL_UNDER_144.5 | DERIVED | 0.967272 | 0.032728 | 0.973041 | 0.988618 (1216/1230) | EXCLUDED_P_ABOVE_0.90 |
| MIL_OVER_89.5 | DERIVED | 0.959233 | 0.040767 | 0.966222 | 0.980488 (1206/1230) | EXCLUDED_P_ABOVE_0.90 |
| WAS_UNDER_149.5 | DERIVED | 0.957278 | 0.042722 | 0.964315 | 0.993496 (1222/1230) | EXCLUDED_P_ABOVE_0.90 |
| TOTAL_OVER_198.5 | DERIVED | 0.956089 | 0.043911 | 0.966244 | 0.954472 (1174/1230) | EXCLUDED_P_ABOVE_0.90 |
| WAS_HCP_+24.5 | DERIVED | 0.951066 | 0.048934 | 0.953899 | 0.937398 (1153/1230) | EXCLUDED_P_ABOVE_0.90 |
| TOTAL_UNDER_278.5 | DERIVED | 0.947225 | 0.052775 | 0.957519 | 0.989431 (1217/1230) | EXCLUDED_P_ABOVE_0.90 |
| WAS_OVER_99.5 | DERIVED | 0.937344 | 0.062656 | 0.945857 | 0.904878 (1113/1230) | EXCLUDED_P_ABOVE_0.90 |
| MIL_UNDER_139.5 | DERIVED | 0.935402 | 0.064598 | 0.943881 | 0.975610 (1200/1230) | EXCLUDED_P_ABOVE_0.90 |
| TOTAL_OVER_203.5 | DERIVED | 0.932487 | 0.067513 | 0.945353 | 0.930894 (1145/1230) | EXCLUDED_P_ABOVE_0.90 |
| TOTAL_UNDER_273.5 | DERIVED | 0.921869 | 0.078131 | 0.934692 | 0.980488 (1206/1230) | EXCLUDED_P_ABOVE_0.90 |
| MIL_OVER_94.5 | DERIVED | 0.921043 | 0.078957 | 0.930835 | 0.954472 (1174/1230) | EXCLUDED_P_ABOVE_0.90 |
| WAS_HCP_+19.5 | DERIVED | 0.918536 | 0.081464 | 0.922111 | 0.908130 (1117/1230) | EXCLUDED_P_ABOVE_0.90 |
| WAS_UNDER_144.5 | DERIVED | 0.917874 | 0.082126 | 0.927617 | 0.982927 (1209/1230) | EXCLUDED_P_ABOVE_0.90 |
| TOTAL_OVER_208.5 | DERIVED | 0.900480 | 0.099520 | 0.915670 | 0.880488 (1083/1230) | EXCLUDED_P_ABOVE_0.90 |
| TOTAL_UNDER_268.5 | DERIVED | 0.887555 | 0.112445 | 0.902513 | 0.964228 (1186/1230) | ELIGIBLE |
| WAS_OVER_104.5 | DERIVED | 0.886684 | 0.113316 | 0.897408 | 0.818699 (1007/1230) | ELIGIBLE |
| MIL_UNDER_134.5 | DERIVED | 0.883555 | 0.116445 | 0.894186 | 0.933333 (1148/1230) | ELIGIBLE |
| WAS_HCP_+14.5 | DERIVED | 0.871927 | 0.128073 | 0.875986 | 0.843089 (1037/1230) | ELIGIBLE |
| MIL_OVER_99.5 | DERIVED | 0.860676 | 0.139324 | 0.872218 | 0.883740 (1087/1230) | ELIGIBLE |
| TOTAL_OVER_213.5 | DERIVED | 0.858301 | 0.141699 | 0.874930 | 0.814634 (1002/1230) | ELIGIBLE |
| WAS_UNDER_139.5 | DERIVED | 0.856077 | 0.143923 | 0.867411 | 0.962602 (1184/1230) | ELIGIBLE |
| TOTAL_UNDER_263.5 | DERIVED | 0.843741 | 0.156259 | 0.859910 | 0.941463 (1158/1230) | ELIGIBLE |
| MIL_HCP_+24.5 | DERIVED | 0.821012 | 0.178988 | 0.825224 | 0.924390 (1137/1230) | ELIGIBLE |
| WAS_OVER_109.5 | DERIVED | 0.812125 | 0.187875 | 0.823385 | 0.700813 (862/1230) | ELIGIBLE |
| WAS_HCP_+9.5 | DERIVED | 0.809514 | 0.190486 | 0.813584 | 0.753659 (927/1230) | ELIGIBLE |
| MIL_UNDER_129.5 | DERIVED | 0.807573 | 0.192427 | 0.818629 | 0.865041 (1064/1230) | ELIGIBLE |
| TOTAL_OVER_218.5 | DERIVED | 0.806002 | 0.193998 | 0.822667 | 0.715447 (880/1230) | ELIGIBLE |
| TOTAL_UNDER_258.5 | DERIVED | 0.789150 | 0.210850 | 0.805123 | 0.911382 (1121/1230) | ELIGIBLE |
| MIL_OVER_104.5 | DERIVED | 0.775080 | 0.224920 | 0.786080 | 0.783740 (964/1230) | ELIGIBLE |
| WAS_UNDER_134.5 | DERIVED | 0.769088 | 0.230912 | 0.779706 | 0.908130 (1117/1230) | ELIGIBLE |
| MIL_HCP_+19.5 | DERIVED | 0.745412 | 0.254588 | 0.749149 | 0.863415 (1062/1230) | ELIGIBLE |
| TOTAL_OVER_223.5 | DERIVED | 0.742957 | 0.257043 | 0.757900 | 0.635772 (782/1230) | ELIGIBLE |
| TOTAL_UNDER_253.5 | DERIVED | 0.725050 | 0.274950 | 0.739126 | 0.860163 (1058/1230) | ELIGIBLE |
| WAS_HCP_+4.5 | DERIVED | 0.724343 | 0.275657 | 0.727702 | 0.648780 (798/1230) | ELIGIBLE |
| WAS_OVER_114.5 | DERIVED | 0.713127 | 0.286873 | 0.722356 | 0.551220 (678/1230) | ELIGIBLE |
| MIL_UNDER_124.5 | DERIVED | 0.707171 | 0.292829 | 0.716049 | 0.773984 (952/1230) | ELIGIBLE |
| TOTAL_OVER_228.5 | DERIVED | 0.671418 | 0.328582 | 0.682872 | 0.543089 (668/1230) | ELIGIBLE |
| MIL_OVER_109.5 | DERIVED | 0.666079 | 0.333921 | 0.673681 | 0.666667 (820/1230) | ELIGIBLE |
| WAS_UNDER_129.5 | DERIVED | 0.659062 | 0.340938 | 0.666151 | 0.843902 (1038/1230) | ELIGIBLE |
| MIL_HCP_+14.5 | DERIVED | 0.655988 | 0.344012 | 0.658621 | 0.785366 (966/1230) | ELIGIBLE |
| TOTAL_UNDER_248.5 | DERIVED | 0.651696 | 0.348304 | 0.662085 | 0.808130 (994/1230) | ELIGIBLE |
| WAS_WIN | DERIVED | 0.645699 | 0.354301 | 0.648030 | 0.554472 (682/1230) | ELIGIBLE |
| WAS_OVER_119.5 | DERIVED | 0.594478 | 0.405522 | 0.599097 | 0.400000 (492/1230) | ELIGIBLE |
| TOTAL_OVER_233.5 | DERIVED | 0.592455 | 0.407545 | 0.598887 | 0.436585 (537/1230) | ELIGIBLE |
| MIL_UNDER_119.5 | DERIVED | 0.587478 | 0.412522 | 0.591613 | 0.659350 (811/1230) | ELIGIBLE |
| TOTAL_UNDER_243.5 | DERIVED | 0.572621 | 0.427379 | 0.577938 | 0.741463 (912/1230) | ELIGIBLE |
| MIL_HCP_+9.5 | DERIVED | 0.555847 | 0.444153 | 0.556876 | 0.677236 (833/1230) | ELIGIBLE |
| WAS_HCP_-4.5 | SUPPLIED | 0.553356 | 0.446644 | 0.554197 | 0.450407 (554/1230) | ELIGIBLE |
| MIL_OVER_114.5 | DERIVED | 0.541253 | 0.458747 | 0.543245 | 0.494309 (608/1230) | ELIGIBLE |
| WAS_UNDER_124.5 | DERIVED | 0.533862 | 0.466138 | 0.535305 | 0.724390 (891/1230) | ELIGIBLE |
| TOTAL_OVER_238.5 | SUPPLIED | 0.510388 | 0.489612 | 0.510992 | 0.331707 (408/1230) | ELIGIBLE |
| TOTAL_UNDER_238.5 | SUPPLIED | 0.489612 | 0.510388 | 0.489008 | 0.668293 (822/1230) | ELIGIBLE |
| WAS_OVER_124.5 | DERIVED | 0.466138 | 0.533862 | 0.464695 | 0.275610 (339/1230) | ELIGIBLE |
| MIL_UNDER_114.5 | DERIVED | 0.458747 | 0.541253 | 0.456755 | 0.505691 (622/1230) | ELIGIBLE |
| MIL_HCP_+4.5 | SUPPLIED | 0.446644 | 0.553356 | 0.445803 | 0.549593 (676/1230) | ELIGIBLE |
| WAS_HCP_-9.5 | DERIVED | 0.444153 | 0.555847 | 0.443124 | 0.322764 (397/1230) | ELIGIBLE |
| TOTAL_OVER_243.5 | DERIVED | 0.427379 | 0.572621 | 0.422062 | 0.258537 (318/1230) | ELIGIBLE |
| MIL_OVER_119.5 | DERIVED | 0.412522 | 0.587478 | 0.408387 | 0.340650 (419/1230) | ELIGIBLE |
| TOTAL_UNDER_233.5 | DERIVED | 0.407545 | 0.592455 | 0.401113 | 0.563415 (693/1230) | ELIGIBLE |
| WAS_UNDER_119.5 | DERIVED | 0.405522 | 0.594478 | 0.400903 | 0.600000 (738/1230) | ELIGIBLE |
| MIL_WIN | DERIVED | 0.354301 | 0.645699 | 0.351970 | 0.445528 (548/1230) | ELIGIBLE |
| TOTAL_OVER_248.5 | DERIVED | 0.348304 | 0.651696 | 0.337915 | 0.191870 (236/1230) | ELIGIBLE |
| WAS_HCP_-14.5 | DERIVED | 0.344012 | 0.655988 | 0.341379 | 0.214634 (264/1230) | ELIGIBLE |
| WAS_OVER_129.5 | DERIVED | 0.340938 | 0.659062 | 0.333849 | 0.156098 (192/1230) | ELIGIBLE |
| MIL_UNDER_109.5 | DERIVED | 0.333921 | 0.666079 | 0.326319 | 0.333333 (410/1230) | ELIGIBLE |
| TOTAL_UNDER_228.5 | DERIVED | 0.328582 | 0.671418 | 0.317128 | 0.456911 (562/1230) | ELIGIBLE |
| MIL_OVER_124.5 | DERIVED | 0.292829 | 0.707171 | 0.283951 | 0.226016 (278/1230) | ELIGIBLE |
| WAS_UNDER_114.5 | DERIVED | 0.286873 | 0.713127 | 0.277644 | 0.448780 (552/1230) | ELIGIBLE |
| MIL_HCP_-4.5 | DERIVED | 0.275657 | 0.724343 | 0.272298 | 0.351220 (432/1230) | ELIGIBLE |
| TOTAL_OVER_253.5 | DERIVED | 0.274950 | 0.725050 | 0.260874 | 0.139837 (172/1230) | ELIGIBLE |
| TOTAL_UNDER_223.5 | DERIVED | 0.257043 | 0.742957 | 0.242100 | 0.364228 (448/1230) | ELIGIBLE |
| WAS_HCP_-19.5 | DERIVED | 0.254588 | 0.745412 | 0.250851 | 0.136585 (168/1230) | ELIGIBLE |
| WAS_OVER_134.5 | DERIVED | 0.230912 | 0.769088 | 0.220294 | 0.091870 (113/1230) | ELIGIBLE |
| MIL_UNDER_104.5 | DERIVED | 0.224920 | 0.775080 | 0.213920 | 0.216260 (266/1230) | ELIGIBLE |
| TOTAL_OVER_258.5 | DERIVED | 0.210850 | 0.789150 | 0.194877 | 0.088618 (109/1230) | ELIGIBLE |
| TOTAL_UNDER_218.5 | DERIVED | 0.193998 | 0.806002 | 0.177333 | 0.284553 (350/1230) | ELIGIBLE |
| MIL_OVER_129.5 | DERIVED | 0.192427 | 0.807573 | 0.181371 | 0.134959 (166/1230) | ELIGIBLE |
| MIL_HCP_-9.5 | DERIVED | 0.190486 | 0.809514 | 0.186416 | 0.246341 (303/1230) | ELIGIBLE |
| WAS_UNDER_109.5 | DERIVED | 0.187875 | 0.812125 | 0.176615 | 0.299187 (368/1230) | ELIGIBLE |
| WAS_HCP_-24.5 | DERIVED | 0.178988 | 0.821012 | 0.174776 | 0.075610 (93/1230) | ELIGIBLE |
| TOTAL_OVER_263.5 | DERIVED | 0.156259 | 0.843741 | 0.140090 | 0.058537 (72/1230) | ELIGIBLE |
| WAS_OVER_139.5 | DERIVED | 0.143923 | 0.856077 | 0.132589 | 0.037398 (46/1230) | ELIGIBLE |
| TOTAL_UNDER_213.5 | DERIVED | 0.141699 | 0.858301 | 0.125070 | 0.185366 (228/1230) | ELIGIBLE |
| MIL_UNDER_99.5 | DERIVED | 0.139324 | 0.860676 | 0.127782 | 0.116260 (143/1230) | ELIGIBLE |
| MIL_HCP_-14.5 | DERIVED | 0.128073 | 0.871927 | 0.124014 | 0.156911 (193/1230) | ELIGIBLE |
| MIL_OVER_134.5 | DERIVED | 0.116445 | 0.883555 | 0.105814 | 0.066667 (82/1230) | ELIGIBLE |
| WAS_UNDER_104.5 | DERIVED | 0.113316 | 0.886684 | 0.102592 | 0.181301 (223/1230) | ELIGIBLE |
| TOTAL_OVER_268.5 | DERIVED | 0.112445 | 0.887555 | 0.097487 | 0.035772 (44/1230) | ELIGIBLE |
| TOTAL_UNDER_208.5 | DERIVED | 0.099520 | 0.900480 | 0.084330 | 0.119512 (147/1230) | ELIGIBLE |
| WAS_OVER_144.5 | DERIVED | 0.082126 | 0.917874 | 0.072383 | 0.017073 (21/1230) | ELIGIBLE |
| MIL_HCP_-19.5 | DERIVED | 0.081464 | 0.918536 | 0.077889 | 0.091870 (113/1230) | ELIGIBLE |
| MIL_UNDER_94.5 | DERIVED | 0.078957 | 0.921043 | 0.069165 | 0.045528 (56/1230) | ELIGIBLE |
| TOTAL_OVER_273.5 | DERIVED | 0.078131 | 0.921869 | 0.065308 | 0.019512 (24/1230) | ELIGIBLE |
| TOTAL_UNDER_203.5 | DERIVED | 0.067513 | 0.932487 | 0.054647 | 0.069106 (85/1230) | ELIGIBLE |
| MIL_OVER_139.5 | DERIVED | 0.064598 | 0.935402 | 0.056119 | 0.024390 (30/1230) | ELIGIBLE |
| WAS_UNDER_99.5 | DERIVED | 0.062656 | 0.937344 | 0.054143 | 0.095122 (117/1230) | ELIGIBLE |
| TOTAL_OVER_278.5 | DERIVED | 0.052775 | 0.947225 | 0.042481 | 0.010569 (13/1230) | ELIGIBLE |
| MIL_HCP_-24.5 | DERIVED | 0.048934 | 0.951066 | 0.046101 | 0.062602 (77/1230) | ELIGIBLE |
| TOTAL_UNDER_198.5 | DERIVED | 0.043911 | 0.956089 | 0.033756 | 0.045528 (56/1230) | ELIGIBLE |
| WAS_OVER_149.5 | DERIVED | 0.042722 | 0.957278 | 0.035685 | 0.006504 (8/1230) | ELIGIBLE |
| MIL_UNDER_89.5 | DERIVED | 0.040767 | 0.959233 | 0.033778 | 0.019512 (24/1230) | ELIGIBLE |
| MIL_OVER_144.5 | DERIVED | 0.032728 | 0.967272 | 0.026959 | 0.011382 (14/1230) | ELIGIBLE |
| WAS_UNDER_94.5 | DERIVED | 0.031633 | 0.968367 | 0.025850 | 0.045528 (56/1230) | ELIGIBLE |
| MIL_OVER_149.5 | DERIVED | 0.015097 | 0.984903 | 0.011700 | 0.003252 (4/1230) | ELIGIBLE |
| WAS_UNDER_89.5 | DERIVED | 0.014532 | 0.985468 | 0.011127 | 0.015447 (19/1230) | ELIGIBLE |

Supplied regulation-only alternate interpretation, same pre-OT grid. Operator terms determine actual definition; never choose after the result:
| Regulation-only supplied contract | W=p | P | L | V |
|---|---|---|---|---|
| WAS_HCP_-4.5 | 0.545007 | 0 | 0.454993 | 0 |
| MIL_HCP_+4.5 | 0.454993 | 0 | 0.545007 | 0 |
| TOTAL_UNDER_238.5 | 0.501662 | 0 | 0.498338 | 0 |
| TOTAL_OVER_238.5 | 0.498338 | 0 | 0.501662 | 0 |

Regulation half lines have no push even at tied regulation score. A regulation-only winner needs a separate draw/action convention; it is not substituted for the full-game potential winner. Void/abandonment probability NOT_ESTIMATED; rows condition on a completed game, definitions queued.

#### A6. Adjustments and sensitivities

| Driver | Before / after | Basis / limits |
|---|---|---|
| Rotation shrink | Raw total246.714154 ->50%shrink T_reg238.411142 | Analyst weight, not measured coefficient |
| Home court | Neutral M5.380421 ->home7.080421 | Fresh league HE1.70 applied once |
| Availability | Only selected players enter budget; no extra injury penalty | No double counting; current minutes unconfirmed |
| Width | Covariance x1.3225; plus9-case uncertainty | Unfitted1.15 SD inflation, no favourable narrowing |
| Form | Old team windows excluded | R2 current n0, no recency double count |
| Rest/travel/weather | Centre shift0 | No back-to-back, indoor, fatigue not measured |
| Pace/defence | NOT_MEASURED | Budget approximation does not estimate current opponent-adjusted efficiencies |

Nine-case sensitivities, NOT confidence intervals:
| Contract | Lowest case p | Highest case p |
|---|---|---|
| TOTAL_UNDER_268.5 | 0.778992 | 0.965533 |
| WAS_OVER_104.5 | 0.755107 | 0.967456 |
| MIL_UNDER_134.5 | 0.749999 | 0.965251 |
| WAS_HCP_+14.5 | 0.813780 | 0.921956 |
| WAS_HCP_-4.5 | 0.450385 | 0.654646 |
| MIL_HCP_+4.5 | 0.345354 | 0.549615 |
| TOTAL_UNDER_238.5 | 0.285294 | 0.695728 |
| TOTAL_OVER_238.5 | 0.304272 | 0.714706 |
| WAS_WIN | 0.547378 | 0.739360 |

Rotation-budget weight sensitivity, unchanged width/mixture/OT. Primary weight0.50 stays frozen;0/1 are stress tests:
| Budget weight | T_reg | M_reg | WASwin | WAS-4.5 | Over238.5 | Under238.5 | Under268.5 | WAS Over104.5 | MIL Under134.5 | WAS+14.5 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 230.108130 | 1.700000 | 0.538858 | 0.443534 | 0.375574 | 0.624426 | 0.938861 | 0.778110 | 0.902505 | 0.804269 |
| 0.25 | 234.259636 | 4.390211 | 0.593134 | 0.498403 | 0.442155 | 0.557845 | 0.916153 | 0.838263 | 0.893167 | 0.840443 |
| 0.5 | 238.411142 | 7.080421 | 0.645699 | 0.553356 | 0.510388 | 0.489612 | 0.887555 | 0.886684 | 0.883555 | 0.871927 |
| 0.75 | 242.562648 | 9.770632 | 0.695660 | 0.607368 | 0.578345 | 0.421655 | 0.852458 | 0.923791 | 0.873762 | 0.898809 |
| 1 | 246.714154 | 12.460843 | 0.742255 | 0.659458 | 0.644113 | 0.355887 | 0.810495 | 0.950861 | 0.863847 | 0.921328 |

Weights0.25..0.75 move WAS-4.5 across0.50 and reverse total direction; WAS winner remains a lean, not validated64.6% confidence. Primary budget-vs-league centre move8.303total/5.380margin exceeds0.25SD on both: LARGE_ADJUSTMENT. ADJUSTMENT_DEPENDENT also follows base-only top-two change; no quiet reordering.

#### A7. Rules, family and mechanical checks

NBA four12-minute quarters,5-minute OT until winner; sixth personal foul ordinarily disqualifies. Team penalty after4 regulation-quarter team fouls /3 OT, with last-two-minute exceptions. Current official rules A8. No referee/foul coefficient. Official assignment page at23:05Z lists John Goble,Natalie Sago,CJ Washington; pre-start publication not proved, verification only, no input. Indoor/no weather effect.

All ranked rows full-game team quantities; no supported player/period rows. Same-grid winner/handicap/total complements and monotonicity verified. WAS+14.5=P(WASwin)+P(lose by1..14), not a league absolute-margin statistic. Rank1 Under SD24.111 exceeds fresh raw19.876 and historical reference19.4. Risks: BASKETBALL_TOTAL_WITHOUT_PACE_MODEL / UNFITTED_ANALYST_ADJUSTMENT / SMALL_SAMPLE_STRENGTH_OVERREACH; limitations, not retrospective causal findings.

#### A8. Opened sources, attempts, captures and comparisons

| ID | Publisher/role | Opened URL | Used fields | Time/lineage limits |
|---|---|---|---|---|
| S01 | Arena field owner | https://www.capitalonearena.com/events/detail/washington-wizards-vs-milwaukee-bucks-10212026 | Oct21 7PM fixture/venue | Pre-start and ~23:03Z; publication UNKNOWN |
| S02 | NBA field owner | https://www.nba.com/game/mil-vs-was-0022600086/box-score | ID, pregame starter/status fields,15 selected each | Initial~22:54Z;23:03:24Z unchanged; publication UNKNOWN |
| S03 | ESPN provider | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261021 | Target fixture/date/venue/status only | 22:51:56Z; publication UNKNOWN |
| S04 | ESPN provider | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909835 | Injuries; empty pregame roster/starter arrays | 22:52:27.566846Z; no predictor/odds used |
| S05 | NBA injury field owner | https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-21_06_45PM.pdf | 4 relevant statuses, page1 | Published22:45Z; retrieved22:53:10Z, rendered/visually verified |
| S06 | NBA injury verification | https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-21_07_00PM.pdf | Same4 statuses, page1, no changed input | Published23:00Z; retrieved23:03:53Z, rendered/visually verified; verification only |
| S07 | NBA discovery | https://official.nba.com/nba-injury-report-2026-27-season/ | Actual timed PDF URLs | 22:52Z and23:03Z; plain403 then UA succeeds |
| S08 | NBA club rosters | https://www.nba.com/bucks/roster and https://www.nba.com/wizards/roster | Membership, not starter confirmation | ~22:53:48Z; same NBA lineage |
| S09 | ESPN rosters | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/15/roster and https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/27/roster | Current18-player squads, not active selection | 22:53:10Z |
| S10 | ESPN schedules | 30 exact URLs below | 1230 final scores/date/venue/opponent/period | 22:54:12Z onward; no target result |
| S11 | ESPN OT summaries | 54 exact URLs below | Quarter lines, regulation and OT increments | 22:57:32Z onward, one provider for quarter lines |
| S12 | ESPN player history | 19 exact URLs/times A4 | Regular-season GP/MPG/PPG only | ~22:55:39Z; news/fantasy objects not used |
| S13 | ESPN preseason | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/15/schedule?season=2027&seasontype=1 and https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/27/schedule?season=2027&seasontype=1 | Separate context, excluded from calculation | 22:53:47Z |
| S14 | Basketball-Reference | https://www.basketball-reference.com/teams/MIL/2026_games.html and https://www.basketball-reference.com/teams/WAS/2026_games.html | Old82-game schedules,40 window rows corroborated | 23:05:15Z, historical-only corroboration |
| S15 | Basketball-Reference | Seven exact month URLs below | 1230 finals agree by US date/home/away/final | Historical-only corroboration; independent provider, upstream collector may overlap |
| S16 | Basketball-Reference | https://www.basketball-reference.com/leagues/NBA_2026_per_game.html | 19/19 GP/MPG/PPG agree | Historical-only recheck, exact time below |
| S17 | NBA coach context | https://www.nba.com/news/milwaukee-bucks-finalize-coaching-staff-2026-27 | Jenkins new coach | Opened research; no coefficient |
| S18 | NBA transaction context | https://www.nba.com/news/giannis-antetokounmpo-stat-sheet-miami-trade-2026?lid=3r4y7dfiu9qb | Roster-change context only | Opened research; no trade-effect coefficient |
| S19 | NBA rules | https://official.nba.com/rule-no-5-scoring-and-timing/ | 48min/5minOT/tie resolution | ~23:03:53Z, stable rules |
| S20 | NBA rules | https://official.nba.com/rule-no-3-players-substitutes-and-coaches/ and https://official.nba.com/rule-no-12-fouls-and-penalties/ | Starting-list submission, foul/bonus rules | ~23:03:53Z |
| S21 | NBA officials | https://official.nba.com/referee-assignments/ | Goble/Sago/Washington | 23:05:15Z, pre-start publication unproved, not input |

ESPN routes are one lineage; NBA game, injury and club pages are one lineage. Basketball-Reference is an independent provider, but original official scoring upstream may be shared; no three-collector claim.

| Team ID | Actual league schedule URL | Retrieved UTC |
|---|---|---|
| 1 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/1/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.964728+00:00 |
| 2 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/2/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.841508+00:00 |
| 3 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/3/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.634613+00:00 |
| 4 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/4/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.744832+00:00 |
| 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/5/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.916134+00:00 |
| 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/6/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.789840+00:00 |
| 7 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/7/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.913064+00:00 |
| 8 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/8/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.156737+00:00 |
| 9 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/9/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:13.732765+00:00 |
| 10 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/10/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:13.853199+00:00 |
| 11 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/11/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:13.740455+00:00 |
| 12 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/12/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:13.821435+00:00 |
| 13 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/13/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:13.980544+00:00 |
| 14 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/14/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:13.972474+00:00 |
| 15 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/15/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.226897+00:00 |
| 16 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/16/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.207368+00:00 |
| 17 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/17/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.696440+00:00 |
| 18 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/18/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:15.071767+00:00 |
| 19 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/19/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.847673+00:00 |
| 20 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/20/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.593329+00:00 |
| 21 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/21/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.887704+00:00 |
| 22 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/22/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.802553+00:00 |
| 23 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/23/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:15.475850+00:00 |
| 24 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/24/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:15.311705+00:00 |
| 25 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/25/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.478554+00:00 |
| 26 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/26/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:15.651287+00:00 |
| 27 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/27/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:15.518106+00:00 |
| 28 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/28/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:15.523020+00:00 |
| 29 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/29/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:14.041193+00:00 |
| 30 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/30/schedule?season=2026&seasontype=2 | 2026-10-21T22:54:12.840921+00:00 |

Final dedup:1230 eligible distinct game IDs,82 games each team;8 postponed duplicate team-feed listings and2 Cup-final listings excluded. BRef1231 through12Apr includes NY-SAS Cup Championship124-113 on16Dec2025; exclude as non-standings final. Normalize BRef Los Angeles Clippers to ESPN LA Clippers/team12, then1230/1230 date/home/away/score agreement, no score conflicts.

| Month | Actual corroboration URL | Retrieved UTC |
|---|---|---|
| october | https://www.basketball-reference.com/leagues/NBA_2026_games-october.html | 2026-10-21T23:05:53.275403+00:00 |
| november | https://www.basketball-reference.com/leagues/NBA_2026_games-november.html | 2026-10-21T23:05:53.903457+00:00 |
| december | https://www.basketball-reference.com/leagues/NBA_2026_games-december.html | 2026-10-21T23:05:53.255590+00:00 |
| january | https://www.basketball-reference.com/leagues/NBA_2026_games-january.html | 2026-10-21T23:05:53.951125+00:00 |
| february | https://www.basketball-reference.com/leagues/NBA_2026_games-february.html | 2026-10-21T23:05:53.483636+00:00 |
| march | https://www.basketball-reference.com/leagues/NBA_2026_games-march.html | 2026-10-21T23:05:53.921364+00:00 |
| april | https://www.basketball-reference.com/leagues/NBA_2026_games-april.html | 2026-10-21T23:05:52.929625+00:00 |

OT kernel provenance (home/away orientation); all quarter sums and regulation ties checked:
| Event | Reg H-A | Added OT H-A | Final period | Actual opened URL | Retrieved UTC |
|---|---|---|---|---|---|
| 401809243 | 104-104 | 21-20 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809243 | 2026-10-21T22:57:32.747412+00:00 |
| 401809236 | 113-113 | 22-28 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809236 | 2026-10-21T22:57:32.248918+00:00 |
| 401809237 | 120-120 | 17-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809237 | 2026-10-21T22:57:32.622432+00:00 |
| 401809949 | 107-107 | 9-13 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809949 | 2026-10-21T22:57:32.231219+00:00 |
| 401809975 | 124-124 | 14-10 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809975 | 2026-10-21T22:57:32.240086+00:00 |
| 401809978 | 126-126 | 8-13 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809978 | 2026-10-21T22:57:32.214907+00:00 |
| 401810054 | 127-127 | 10-8 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810054 | 2026-10-21T22:57:32.222962+00:00 |
| 401810056 | 128-128 | 12-10 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810056 | 2026-10-21T22:57:32.257264+00:00 |
| 401809785 | 129-129 | 18-5 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809785 | 2026-10-21T22:57:32.709253+00:00 |
| 401809788 | 114-114 | 13-19 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809788 | 2026-10-21T22:57:32.679036+00:00 |
| 401810091 | 102-102 | 15-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810091 | 2026-10-21T22:57:32.690582+00:00 |
| 401810093 | 118-118 | 20-15 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810093 | 2026-10-21T22:57:32.722154+00:00 |
| 401810095 | 127-127 | 23-20 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810095 | 2026-10-21T22:57:32.732454+00:00 |
| 401810121 | 106-106 | 8-17 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810121 | 2026-10-21T22:57:32.818331+00:00 |
| 401810147 | 101-101 | 16-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810147 | 2026-10-21T22:57:33.095384+00:00 |
| 401809807 | 122-122 | 6-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809807 | 2026-10-21T22:57:33.128235+00:00 |
| 401810149 | 104-104 | 14-7 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810149 | 2026-10-21T22:57:33.712474+00:00 |
| 401810159 | 115-115 | 19-27 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810159 | 2026-10-21T22:57:33.247486+00:00 |
| 401810176 | 129-129 | 13-20 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810176 | 2026-10-21T22:57:33.356807+00:00 |
| 401836799 | 111-111 | 0-8 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401836799 | 2026-10-21T22:57:33.347203+00:00 |
| 401836805 | 129-129 | 11-4 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401836805 | 2026-10-21T22:57:33.309120+00:00 |
| 401836806 | 117-117 | 11-8 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401836806 | 2026-10-21T22:57:33.324271+00:00 |
| 401810230 | 119-119 | 14-9 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810230 | 2026-10-21T22:57:33.519685+00:00 |
| 401810231 | 110-110 | 6-4 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810231 | 2026-10-21T22:57:33.672677+00:00 |
| 401810235 | 115-115 | 19-18 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810235 | 2026-10-21T22:57:33.814569+00:00 |
| 401810248 | 118-118 | 9-10 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810248 | 2026-10-21T22:57:33.825923+00:00 |
| 401810256 | 112-112 | 13-12 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810256 | 2026-10-21T22:57:33.746189+00:00 |
| 401809242 | 115-115 | 27-23 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401809242 | 2026-10-21T22:57:34.048540+00:00 |
| 401810296 | 122-122 | 19-5 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810296 | 2026-10-21T22:57:34.477972+00:00 |
| 401810313 | 128-128 | 8-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810313 | 2026-10-21T22:57:34.078203+00:00 |
| 401810362 | 120-120 | 4-5 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810362 | 2026-10-21T22:57:34.059985+00:00 |
| 401810376 | 93-93 | 10-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810376 | 2026-10-21T22:57:34.132240+00:00 |
| 401810380 | 114-114 | 15-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810380 | 2026-10-21T22:57:34.180923+00:00 |
| 401810405 | 107-107 | 9-8 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810405 | 2026-10-21T22:57:34.888913+00:00 |
| 401810445 | 109-109 | 8-12 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810445 | 2026-10-21T22:57:34.354787+00:00 |
| 401810483 | 115-115 | 13-7 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810483 | 2026-10-21T22:57:34.493362+00:00 |
| 401810492 | 104-104 | 22-26 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810492 | 2026-10-21T22:57:34.528053+00:00 |
| 401810581 | 108-108 | 26-19 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810581 | 2026-10-21T22:57:34.538846+00:00 |
| 401810584 | 128-128 | 13-9 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810584 | 2026-10-21T22:57:34.556680+00:00 |
| 401810626 | 124-124 | 10-13 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810626 | 2026-10-21T22:57:34.752403+00:00 |
| 401810666 | 96-96 | 17-14 | 6 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810666 | 2026-10-21T22:57:34.939040+00:00 |
| 401810713 | 114-114 | 8-5 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810713 | 2026-10-21T22:57:35.062626+00:00 |
| 401810717 | 107-107 | 20-14 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810717 | 2026-10-21T22:57:34.954711+00:00 |
| 401810757 | 101-101 | 12-14 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810757 | 2026-10-21T22:57:34.970294+00:00 |
| 401810798 | 118-118 | 6-12 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810798 | 2026-10-21T22:57:35.019487+00:00 |
| 401810810 | 123-123 | 13-8 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810810 | 2026-10-21T22:57:35.005609+00:00 |
| 401810829 | 118-118 | 9-7 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810829 | 2026-10-21T22:57:35.178202+00:00 |
| 401810884 | 122-122 | 9-16 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810884 | 2026-10-21T22:57:35.845671+00:00 |
| 401810899 | 126-126 | 5-11 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810899 | 2026-10-21T22:57:35.565971+00:00 |
| 401810906 | 121-121 | 8-9 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810906 | 2026-10-21T22:57:35.426403+00:00 |
| 401810913 | 95-95 | 15-13 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810913 | 2026-10-21T22:57:35.453496+00:00 |
| 401810952 | 101-101 | 13-9 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810952 | 2026-10-21T22:57:35.441123+00:00 |
| 401810985 | 124-124 | 12-10 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401810985 | 2026-10-21T22:57:35.493887+00:00 |
| 401811002 | 125-125 | 12-7 | 5 | https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401811002 | 2026-10-21T22:57:35.550929+00:00 |

Player corroboration retrieved2026-10-21T23:07:09.014155+00:00:19/19 agree on printed GP/MPG/PPG. Exact player publication times UNKNOWN, but original rates captured pre-start.

Access/conflicts: NBA CDN liveData boxscore returned403; official SSR succeeded. NBA daily-lineups HTML had no usable confirmed list. ESPN pregame starter/bench arrays empty; general roster not substituted for game selection. Plain injury-index23:00Z refresh403, UA23:03Z succeeded. Local player-corroboration script encoding error corrected to UTF-8; successful fetch/rerun retained. Initial Clippers name-alias mismatch corrected by teamID; no score discrepancy. Independent starter-role collector and54 regulation-quarter corroborations remain open.

Incidental bookmaker/tips/fantasy search snippets quarantined/excluded, not forecast inputs. No ESPN predictor/pickcenter/odds/win-probability objects or fitted forecast outputs used. Raw whole NBA page saved externally, but only pregame identity/role fields inspected; refresh extracted names/status only. No target outcome or target performance read. Raw evidence/helpers external: C:/Users/danie/Desktop/Sports-Research-work/20261022MILWAS.

| External retained artifact | SHA256 |
|---|---|
| nba_game_props.json | 276ae11a291a8e209e5812988e00e1826e8ce62eff9cd059472c20d8b2b8c6d8 |
| injury_1845.pdf | 8ab8883b149a0b6cb4eefda825edc9a67f759caf65947340d59e74f048eb2bc0 |
| injury_1900.pdf | 78829badd6c56b9a327bffdc19cf0e9ad2d6afb5a8b54df5022c5450320680de |
| league_rows_with_reg.json | 96fe9689cfc8a70fa69661589c5ec707b83a328e90b679c0fbb254f7c78a5f3f |
| overtime_lines.json | e6f5ea5dc70de934578291e7f444ac43bc4b47aefaf06735db7f08ccd3f08a08 |
| rotation_stats.json | be6896e053428cf7479617368bf196059df57ee4efe4a0392bbe1dc8ca79d093 |
| bref_league.json | 24e1eee394a3ef5e48582c6221394082ee11b0bf514eef6ec22e801be5f50b67 |
| bref_player_rows.json | 0a19dc1bd7bf687565a2af8a98b2a7a3a9bbc71a6fe3a72d3393568f823de2f9 |
| calculations.json | c539ec919182dd93d84425ed253cb43573be155190f8d3e3cb0661d1bbaf3978 |
| all_candidates.json | b3cd7a132b6b307861ffe8039eae6c14a194677fbb15d6e0fd158b4fa941ce18 |
| analyst_grid.npz | b331336aa434242d575aca48728631abd9e968f50e0dbca804f10135943283e3 |
| calculate_analyst.py | 366b2596baf41818c349acbdbd00269cf69587707c2bced1877ed6b29b21c42d |
| PREPRICING_PLAN.md | 1ca31ab382e676c9e1c2d14832fb4cfdc8727dcc0b5da2db5cc490e469709cc6 |

#### A9. Completion matrix and actual audit

| Procedure / sport step | Status and evidence / gap |
|---|---|
| 1 Authority/reading/custody | Scoped local receipt A1; prior-block preservation checked at write; canonical state unchanged |
| 2 Identity/time/timing | NBA+ESPN+arena agree23:00Z; actual firstplay unverified; late issuance disclosed |
| 3 Availability | PARTIAL: official roles/active list and timed injuries; second starter collector, coach minutes/usage caps INCOMPLETE, source ladder A3/A8 |
| 3 History/form/learning | 40 dated prior rows and true windows; current n0,R2 exclusions;1230 finals corroborated; independent OT quarter lines missing, LEARN_RECORD_INCOMPLETE |
| 4 Distribution/score | CALCULATED_SUPPORTED_APPROXIMATION; all budget/covariance/mixture/OT inputs disclosed; current pace/opponent efficiency missing, not a fitted forecast |
| 4 Baseline | Exact league-only prior cohort;4/4 ranked and108/108 priced; frozen before issue, no target outcome |
| 5 Contracts/selection/dependence | All4 supplied assessed incl regulation alternative;108-row ladder,90% ceiling, failed gate and all shadows/joints |
| 6 Conditions/rules | Official rules,indoor,non-B2B; operator OT/void definitions UNKNOWN_DEFINITION |
| 7 Append/readback/model/publication | Actual dated receipt below; model command only after card readback; exact publication reported separately |
| Settlement/retrospective/import/ingest | NOT_PERFORMED, not requested |

Open-field next actions: independent exact-game starter record/game book; operator OT/void rules before grades; archived official quarter lines for54 historical OT games; target actual firstplay timestamp at prompt3; current-lineup possession/efficiency only from a future measured sample. No automation or fictitious closure. Overall INFORMATION_INCOMPLETE; numeric arithmetic executed as an approximation; predictive certification NOT_ESTABLISHED.

C1 authority/read receipt; C2 duplicate/local identity/no canonical allocation; C3 recipe/order/ceiling; C4 W/P/L/V/complements/monotonicity and grid normalization1e-12; C5/C6 full-universe gate/floor/joint/shadows; C7/C8 large adjustments/regime/sensitivity; C9/C10 full-game/alternate endpoint and open operator terms; C11 timing/input horizon separated; C12 market/model blindness; C13/C20 corroboration and minutes INCOMPLETE, not falsely passed; C14 exact separate baseline; C15 expected-score/covariance plus approximation limits/A9; C16 actual cumulative readback/earlier-byte checks at insertion; C17 current n0/historical rows and blends; C18 distances/coverage; C19 legacy runtime clause superseded by MLSCOPE-v2, analyst mixture checked, model after card only; C21 disclosed actual arithmetic; C22 actual mini path/readback/commit/push returned when verified.

**Model shadow (MLSCOPE-v2):** not accessed before insertion/readback. Actual dated run record follows afterward; primary probabilities/ranks/picks immutable.

**Append preparation receipt:** 2026-10-21T23:14:52+00:00, HEAD88724540185c4546fb10addd71798008b3fdc939, pre-write bytes106825, SHA2568a6a51b840205673e34887ae01ea3f715ffe1bf61a1eec72655b16c7a50e52e8; Codex task-scoped issuing writer. Actual insertion/readback details added after write.

**Original insertion timestamp:** 2026-10-21T23:16:19+00:00; POST_SCHEDULED_START_ISSUE. Full cumulative bytes read back and all earlier CARD blocks matched byte-for-byte by append verifier.

SPORTS_ONLY_MARKET_BLIND: APPLIED; OUTCOME_EXPOSURE: NO_TARGET_OUTCOME_SEEN; SETTLEMENT: NOT_PERFORMED; RETROSPECTIVE: NOT_PERFORMED; CANONICAL_IMPORT: PENDING
#### Dated post-card model/readback receipt - 2026-10-21T23:18:22+00:00

**Model shadow (MLSCOPE-v2, after original card write/readback): NOT_RUN_NO_RELEASE.** Actual root command: `python -m ml pregame run --mini research/active_minis/20261022F6K3OJNO.md --game <external>/GAME.csv --lines <external>/LINES.csv --capture <external>/FIXTURE_SOURCE.txt --confirm-no-outcome-seen`. Run at 2026-10-21T23:17:14.940519+00:00; reason: no active release for this competition; active: Baseball/MLB, Ice Hockey/NHL. Receipt: `research/pregame/LOCAL-20261022F6K3OJNO-G0004/20261021T231714942163Z_PREGAME.csv`. No release/model predictions, no frozen model rows, no frozen card-ledger rows, no expert feedback. Primary probabilities, ranks, picks, gate and assumptions unchanged.

The card was originally inserted/read back at 2026-10-21T23:16:19+00:00, after23:00Z scheduled start. Receipt binds pre-shadow mini SHA256 `2bffeeb370a5fe76ffd2a19281db939a4b63c08f61f75d8b31457dbb094f2de8` and original card SHA256 `8f68f1c2e885125cd9baa7eb3f6d85ab4998741544041c49854734d26acd234c`; this dated append naturally changes the current file hash. No pre-start publication claim.56 supported CLI contracts supplied (2 winners,20 handicaps,34 combined totals), each card_p copied verbatim at6 printed decimals.52 team-total rows remain analyst-only because this CLI supports winner/handicap/combined total, and no NBA release exists anyway. Initial invocation from the external working directory returned `No module named ml`; corrected invocation from repository root generated this actual receipt.

No target live score, result or post-start performance report was opened. Post-horizon19:00ET medical report and safe role/status-only page refresh are disclosed above and did not change inputs; the safe page still showed gameStatus1. The confirmation flag asserts no outcome exposure, not that all retrievals preceded23:00Z.

Full cumulative mini readback and exact prior-card byte checks PASS; five balanced card pairs, one footer, next keyG0005, no canonical state changes. `python -m ml primary verify-log --mini ...` returned cards5,analyst_primary5,qualitative_or_no_forecast0. This validates record structure/dispositions, not sourcing completeness or predictive skill. No full model test suite is warranted for a Markdown append. Previous card hashes:

| Preserved original key | Raw block SHA256 |
|---|---|
| LOCAL-20261021OKCSASR01-G0001 | 9964e128e6372c36d1b7e5c79dafad3a84ab462e6d996c681a8b57a2b1ae854a |
| LOCAL-20261022F6K3OJNO-G0001 | 56036201f5f19faaaebe1bf162a0cf49041c72588a079bcf22835a5e5503cd4d |
| LOCAL-20261022F6K3OJNO-G0002 | 860df22d0d61b43d699dcf3c8c95a4375c6698840db1beb433c8e87df400cec7 |
| LOCAL-20261022F6K3OJNO-G0003 | f3a133ac20961e60250680eb737e5631ccc533dba49b054819281b5bb6e6e618 |

External shadow inputs and hashes (raw originals/source custody A8):

| Input | SHA256 |
|---|---|
| GAME.csv | 877fb23dea8839a40d346929f0ac7eb348dbb380a070db572bbda69066b97ed0 |
| LINES.csv | 9432e4f336aeca202da3cbe31f1d8d18ae59e6ce5065c6735851597fe84d41aa |
| FIXTURE_SOURCE.txt | e3b2ef13487cd9358e877548d9559f6e5a2786beaaab8b7240541252c514749c |

<!-- END CARD LOCAL-20261022F6K3OJNO-G0004 -->

<!-- BEGIN CARD LOCAL-20261022F6K3OJNO-G0005 -->
## Card · LOCAL-20261022F6K3OJNO-G0005 · ICE HOCKEY / AHL 2026-27 regular season · Hamilton Hammers @ Toronto Marlies · 21 Oct 2026 (Toronto) / 22 Oct 2026 (AEDT)

- **Local event key:** `LOCAL-20261022F6K3OJNO-G0005` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** NOT_ASSIGNED / PROMPT_4_IMPORT (settlement phase).
- **Event key / native IDs / aliases:** `AHL-20261021-HAM-TOR`; HockeyTech (AHL official site feed) game id `1029174`, season id 94, home team id 335 (Toronto Marlies), visiting team id 457 (Hamilton Hammers); aliases HAM @ TOR, Hammers @ Marlies.
- **Authority:** `LOCAL_WORKING_TREE`, branch `main`, HEAD `88724540185c4546fb10addd71798008b3fdc939`, no uncommitted control changes at read (2026-10-22T10:04+11:00). MDS-2026.10.22-v23.0 / CR-2026.10.22-R1 / SCV-2026.10.16-v11 / SEL-2026.10.12-v3; prompt P-2026.10.22-v23.0 (core + ICE HOCKEY).
- **Analysis status:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY
- **Probability method:** League anchor from the full 2025-26 AHL season (all 1,152 regular-season games, final scores); team centres from TB-1-MD arithmetic on 2026-27 goals for and against (6 games each) shrunk toward a measured season-to-season carry-over of 2025-26 (k = 20, the NHL/MLB constant, `UNVALIDATED` for the AHL); the league distribution of final totals tilted to the matchup mean; a normal on the final margin anchored on the empirical home-win rate; empirical puck-line shares; nine-state mixture (0.25/0.50/0.25 on the total centre and on the margin centre, widths from the carry-over residuals and the measured goalie-talent spread). Computed with code; every input and step is in A4.
- **Scheduled start:** **2026-10-21 19:00 EDT = 23:00:00Z = 2026-10-22 10:00 AEDT** (HockeyTech schedule, `GameDateISO8601` 2026-10-21T19:00:00-04:00; matches the owner's estimate). Venue: the home arena is not shown by the feeds I read (`NOT_RETRIEVED`); the Marlies are the home team.
- **Timing:** Request received 2026-10-22T10:04:53+11:00 (23:04:53Z), **4 minutes 53 seconds after the scheduled start**. The only target-specific facts read were the schedule row (23:05:31Z: kickoff time and status "7:00 pm EDT, started 0, final 0", read as feed lag, not as a delay) and the game-centre preview (23:06:22Z: team standings lines, previous meetings, no line-ups). Everything else is dated 2026-10-20 or earlier. No score, goal, shot count, line-up or live state of this game was read; target rows were removed by game id before any field was parsed. Roster and transaction snapshots were read at 23:12–23:14Z (newest entry 2026-10-20). Label: `CLEAN_PRE_START_INPUTS / POST_START_ISSUE` (own research cohort; not a pre-start-issued forecast).
- **Endpoint / definition:** AHL regular season: 60 minutes, a five-minute overtime (goalie minutes 65:00 in the shootout game 1029105), then a shootout. The official final score gives the shootout winner one extra goal. **Moneylines:** two readings frozen and queued as an operator question: (R-A) full game, overtime and shootout included, no draw; (R-B) 60-minute regulation, a tie loses. **Totals at 5.5:** identical under every reading (a tie after 60 minutes has an even total, at most 4 or at least 6, and one overtime goal or the shootout credit never crosses 5.5). Puck lines are derived on the official final score.
- **Lineup state:** Starting goalies and line-ups `LINEUP_UNCONFIRMED` for both sides (AHL game sheets exist only once the game is under way; the preview line-up field is empty). The AHL publishes no injury report. Both teams have new head coaches; the Marlies kept 9 of the 20 players they dressed in their 2025-26 finale, and the Hammers' roster continuity is unknown.
- **Learning record:** 12 dated 2026-27 team rows with goalies (A3), roster status counts, transactions with dates, and the league population (A4). Availability for skaters is unknown, not healthy.

### Decision block

Two high-event, near-average teams. The model puts the Marlies a slight favourite (home edge plus a better start: 4-2 against 1-4-1) and the total about a quarter-goal above the league. Departures from the league-only baseline are small (at most 0.046). The strongest rows are cushions and a far Under, not a view on either side.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---:|---:|---:|---|---|---|
| 1 | PICK (RANK1_UNSTABLE) | ANALYST_DERIVED | AHL:FULL:MARLIES:+1.5:FINAL_SCORE | 0.7418 | 0.7422 | 0.7248 | margin line −1.5 − centre +0.34 = −1.84 goals; z −0.70 | Mixture, margin | Hammers win by two or more; 73% of two-goal NHL regulation wins contain an empty-net goal (AHL share not measured), so a late empty-netter is the kill path |
| 2 | PICK | ANALYST_DERIVED | AHL:FULL:TOTAL:UNDER:7.5:FINAL_SCORE | 0.7237 | 0.7249 | 0.7639 | 7.5 − 6.40 = +1.10 goals; z +0.47 | Mixture, total | A game of eight or more goals (both teams have averaged 7.2 in 2026-27) |
| 3 | INFORMATIONAL | ANALYST_DERIVED | AHL:FULL:HAMMERS:+1.5:FINAL_SCORE | 0.6694 | 0.6691 | 0.6875 | margin line +1.5 − centre +0.34 = +1.16 goals; z +0.44 | Mixture, margin | Marlies win by two or more |
| 4 | INFORMATIONAL | SUPPLIED | AHL:FULL:TOTAL:OVER:5.5:FINAL_SCORE | 0.5934 | 0.5952 | 0.5495 | 5.5 − 6.40 = −0.90 goals; z −0.39 | Mixture, total | Five goals or fewer (a 2-2 tie after 60 minutes lands here) |

**Baseline coverage:** 17/17 priced rows and 4/4 ranked rows (BASELINE_LEAGUE_V1: literal 2025-26 AHL league frequencies on the identical line, n = 1,152, frozen in this card before pricing).
**Rank-1 gate:** `RANK1_UNSTABLE`. p 0.7418 ≥ 0.62; the best non-complementary alternative in the eligible priced universe is Under 7.5 at 0.7237: gap 0.0181 < 0.04. The grid is exact to about 1e-6, so this is not a precision tie. **Would-be Rank 1 removed:** Over 4.5 (0.8092) was the top row, but it is a total with both starting goalies unresolved in an early-season competition (IH-P2, control 14); it is removed from the primary selection and kept in the diagnostic ladder, as SELECTION_RULES §2 requires.
**`SHADOW_GATE_RET03`:** excluding every signed-margin row (winner and handicap rows share that quantity), the alternative is Under 7.5 at 0.7237: gap 0.0181 → RANK1_UNSTABLE (shadow only).
**Rank-2 floor:** PASS (0.7237 ≥ 0.58).
**Joint failure:** Ranks 1 and 2 are on different quantities; exact joint loss 0.0713 (the total and the margin are assumed independent within each centre state; their correlation was not measured). Ranks 1 and 3 are opposite +1.5 lines: they cannot both lose (`MECHANICALLY_PROTECTED`), a covering pair whose combined record carries no skill; only Ranks 1–2 count as primary.
**Shadow gate / Rank 2:** RET04 (highest p ≥ 0.58 on a different quantity from Rank 1) = Under 7.5, joint with Rank 1 0.0713. XCARD6 (minimum exact joint failure with Rank 1 among p ≥ 0.58) = Hammers +1.5, 0.6694, joint 0.0000 (disjoint, `MECHANICALLY_PROTECTED`, same quantity). NOT_PRIMARY.
**Shadow RANK_DELTA / BASE_ONLY:** RANK_DELTA top two (p ≥ 0.58, by p_card − BASELINE_P, eligible rows) = Over 5.5 (+0.0439) and Marlies +1.5 (+0.0170), joint loss 0.1050. BASE_ONLY (base case only): same order and gate (0.7422 / 0.7249 / 0.6691 / 0.5952; gap 0.0173, RANK1_UNSTABLE). NOT_PRIMARY.
**Adjustment dependence:** `ADJUSTMENT_DEPENDENT`. On the league-only baseline the first two ranks would be Under 7.5 (0.7623) then Marlies +1.5 (0.7248): the team model swaps them. The same swap occurs with k = 40 and with the 2025-26 prior alone (A6). The set of the top three rows is stable; their order is not.
**Potential winner:** **Toronto Marlies 0.5464; Hamilton Hammers 0.4536** (two-way, overtime and shootout included, R-A). On the regulation reading (R-B): Marlies 0.4300, tie after 60 minutes 0.2326, Hammers 0.3373. A lean to the home side, not a confident call.

**The four supplied rows (all assessed):**

| Supplied row | R-A p_card | BASELINE_P | R-B p_card (draw loses) | Position |
|---|---:|---:|---:|---|
| **Hammers ML** | 0.4536 | 0.4835 | 0.3373 | 9th of 17 |
| **Marlies ML** | 0.5464 | 0.5165 | 0.4300 | 6th of 17 |
| Combined **Over 5.5** | 0.5934 | 0.5495 | 0.5934 | Rank 4 (5th of 17) |
| Combined **Under 5.5** | 0.4066 | 0.4505 | 0.4066 | 11th of 17 |

Only Over 5.5 is above 0.58; the model's Over lean comes from two sources, the high 2026-27 scoring of both teams (7.2 goals per game over 6 games, 3 of them against each other) and a league mean that was already 6.13 with 55% of games reaching six goals. The Marlies moneyline is 0.03 above the baseline on the home edge and the better start.
**Supplied rows not selected:** Marlies ML, Hammers ML and Under 5.5, for the reasons above; none was removed to manufacture a pass.
**Player rows:** none. No line-ups are published and no skater-level minutes, usage or injury data were retrieved; a player prop would be invented.

**Model shadow (MLSCOPE-v2, frozen after this card):** run only after this card was written and read back; the dated shadow record is appended at the end of this card.

### Appendix

#### A1. Identity, timing and state
- Competition: AHL 2026-27 regular season (HockeyTech season 94), North Division, Eastern Conference. This is the fourth meeting of the season; the Marlies won the first three (5-3 at Toronto on 10-03, 5-4 in a shootout at Hamilton on 10-09, 5-2 at Hamilton on 10-11). Those three games sit inside both teams' six-game samples and are counted once (control 25).
- The Hammers are the New York Islanders' new AHL affiliate, relocated from Bridgeport (AHL board approval 31 March 2026; name announced 21 May 2026; head coach Jay McKee; TD Coliseum, Hamilton) per CP24, The Hockey News and the HockeyTech coach and venue fields. The Marlies' head coach is Steve Sullivan; the 2025-26 finale was coached by John Gruden.
- Duplicate check (2026-10-22T10:19+11:00): no record of either club in any Markdown file of the repository outside the archive (Combined Log Parts 1–9, all minis, reports); searched "Toronto Marlies" and "Hamilton Hammers".
- **Key collision, resolved by ordinal:** this card was prepared as `G0004`. While it was being prepared, another session appended a Milwaukee Bucks @ Washington Wizards card to this mini under `LOCAL-20261022F6K3OJNO-G0005` (10:17–10:18 AEDT, its footer then named `G0005` as next). That card is untouched. This card is therefore recorded as `G0005`; no ordinal was reused and the other card's bytes are preserved. The AHL appears in the repository only as a settlement-route note (RESEARCH_SOURCE_REGISTER SRC-0609).
- Writer and lease: repository agent, mini 20261022F6K3OJNO, lease to 2026-10-29T00:40+11:00, not frozen.

#### A2. Contracts and candidate recipe (frozen before pricing)
Supplied: Hammers ML; Marlies ML; Combined Total Over 5.5; Under 5.5 (units: goals; period: full game; settlement action: moneyline per R-A and R-B above; totals identical under every reading). Declared derived universe, frozen before any probability was computed: totals Over and Under at 4.5, 5.5, 6.5, 7.5; each side's puck line ±1.5 on the official final score; the regulation three-way (Marlies, tie, Hammers). 17 rows from one object. Selection ceiling 0.90 (no row near it). Team totals, period rows and player rows are excluded: no supported inputs. Totals at 4.5 and 6.5 depend on the shootout-credit convention; priced with the credit counted (the official final score): Over 4.5 would be 0.7924 and Over 6.5 0.4687 base case with the credit removed (0.8120 and 0.4993 with it).

#### A3. Evidence, availability and online history

**Availability.** The AHL publishes no injury report. The HockeyTech roster feed (retrieved 23:13Z) lists, by contract status, Marlies: 28 players (6 AHL contracts, 21 NHL contracts on loan, 1 PTO) and goalies Samuel Hlavaj, Artur Akhtyamov and Ken Appleby; Hammers: 26 players (8 AHL, 17 NHL contracts, 1 ATO) and goalies Josh Kotai and Vítek Vaněček. Dated roster transactions (HockeyTech, retrieved 23:12:38Z):

| Team | Date | Transaction (HockeyTech wording) | Player | Effect on the AHL roster list |
|---|---|---|---|---|
| Marlies | 2026-10-20 | Returned on loan | Artur Akhtyamov (G) | Added: back on the Marlies' list after the 10-18 removal |
| Marlies | 2026-10-18 | Recalled from loan | Artur Akhtyamov (G); Vinni Lettieri (RW) | Removed |
| Marlies | 2026-10-16 | Conditioning loan | Dakota Joshua (F); Cade Webber (D) | Added |
| Marlies | 2026-10-15 | Recalled from loan / Loaned | Jacob Quillan (C) / Aatu Räty (F) | Removed / Added |
| Hammers | 2026-10-20 | Reassigned; Recalled from loan | Jesse Pulkkinen (D); Chas Sharpe (D) | Removed; Added |
| Hammers | 2026-10-19 | Recalled from loan | Mitchell Chaffee (RW) | Removed |
| Hammers | 2026-10-17 | Recalled from loan | Max Ellis (RW) | Added |

No injury, suspension or scratch information exists in any feed before puck drop. Roster changes (recalls, assignments) can still happen before a game, so the dressed line-up is unknown. Search ladder: official game centre (preview line-up field empty) → both clubs' feeds (HockeyTech roster and transactions read; club sites and social accounts were **not** searched, because the game was already under way and snippets could show the live score) → eligibility/medical (none published) → provider. Starters remain `LINEUP_UNCONFIRMED`.

**Goalie usage, 2026-27 (from the nine finished games' summaries):**

| Goalie | Team | Starts | Shots against | Goals against | Save % | 2025-26 line (HockeyTech) |
|---|---|---:|---:|---:|---:|---|
| Samuel Hlavaj | Marlies | 3 | 69 | 9 | .870 | 22 GP, .887 (with Iowa) |
| Artur Akhtyamov | Marlies | 3 | 76 | 9 | .882 | 37 GP, .904 (Toronto) |
| Vítek Vaněček | Hammers | 4 (pulled after 6:09 and 3 goals on 10-18) | 102 | 12 | .882 | not in the 135-goalie 2025-26 list read |
| Josh Kotai | Hammers | 2 (+ relief on 10-18) | 74 | 9 | .878 | 1 GP |

Marlies starter order: Hlavaj, Akhtyamov, Akhtyamov, Hlavaj, Hlavaj, Akhtyamov (latest 10-18); Hammers: Vaněček, Kotai, Vaněček, Kotai, Vaněček, Vaněček (latest 10-18, pulled). Both pairs split starts roughly evenly with no usable pattern, so each side's starter is modelled as unknown (width, not a lean). Measured goalie spread (2025-26, 53 goalies with 600+ shots against): true talent SD 0.0064 save percentage, 0.17 goals per game.

**Special teams and shots (2026-27, from the same summaries):** Marlies power play 5/24 (20.8%), penalty kill 21/26 (80.8%), shots for 181 and against 147 in 6 games (30.2 / 24.5); Hammers power play 6/33 (18.2%), penalty kill 17/23 (73.9%), shots for 174 and against 179 (29.0 / 29.8). These are context; they are already inside the goals for and against and move no centre.

**Previous-season windows.** Both teams changed head coach (Marlies: Gruden → Sullivan; Hammers: new franchise and coach), and only 9 of the 20 players the Marlies dressed in their 2025-26 finale appear on the 2026-27 AHL roster list. Under R2 step 3 the 2025-26 games are therefore **excluded from the form windows** (true n = 6). They enter only through the carry-over prior (A4), as the league's measured average carry-over.

**Form windows (2026-27 only; overlapping windows are one piece of evidence):**

| Side | Window | True n | W-L | GF/g | GA/g | Total/g | Over 5.5 |
|---|---|---:|---|---:|---:|---:|---|
| Marlies | L5 | 5 | 4-1 (one OT, one SO win) | 4.40 | 3.40 | 7.80 | 5/5 |
| Marlies | L10 / L15 / L20 | 6 | 4-2 | 3.83 | 3.33 | 7.17 | 5/6 |
| Hammers | L5 | 5 | 0-5 (one shootout loss) | 2.60 | 4.60 | 7.20 | 4/5 |
| Hammers | L10 / L15 / L20 | 6 | 1-5 (one shootout loss) | 3.00 | 4.17 | 7.17 | 5/6 |

League 2026-27 to date: 98 finished games, mean total 6.163, home 2.929, away 3.235 per game, 13 decided in overtime and 7 in shootouts. 2025-26 (Marlies, excluded from windows): 72 games, 3.18 for and 3.17 against. Bridgeport Islanders 2025-26 (Hammers' prior): 72 games, 3.04 for and 3.08 against.

**Toronto Marlies: 6 dated 2026-27 regular-season games before the cutoff, newest first** (AHL final score includes the shootout-winner credit; the Marlies and Hammers played each other in 3 of these 6)

| # | Date | Venue | Opponent | Final (for-against) | Decided | Goalie(s) used, with minutes, shots against, goals against | HockeyTech id |
|---:|---|---|---|---|---|---|---|
| 1 | 2026-10-18 | H | Senators | 2-4 (L) | regulation | Artur Akhtyamov 59:00, 17 SA, 2 GA | `1029167` |
| 2 | 2026-10-17 | A | Senators | 5-4 (W) | overtime | Samuel Hlavaj 62:59, 25 SA, 4 GA | `1029149` |
| 3 | 2026-10-11 | A | Hammers | 5-2 (W) | regulation | Samuel Hlavaj 59:23, 24 SA, 2 GA | `1029127` |
| 4 | 2026-10-09 | A | Hammers | 5-4 (W) | shootout | Artur Akhtyamov 64:56, 32 SA, 4 GA | `1029105` |
| 5 | 2026-10-03 | H | Hammers | 5-3 (W) | regulation | Artur Akhtyamov 60:00, 27 SA, 3 GA | `1029089` |
| 6 | 2026-10-02 | A | Americans | 1-3 (L) | regulation | Samuel Hlavaj 56:48, 20 SA, 3 GA | `1029077` |

**Hamilton Hammers: 6 dated 2026-27 regular-season games before the cutoff, newest first** (AHL final score includes the shootout-winner credit; the Marlies and Hammers played each other in 3 of these 6)

| # | Date | Venue | Opponent | Final (for-against) | Decided | Goalie(s) used, with minutes, shots against, goals against | HockeyTech id |
|---:|---|---|---|---|---|---|---|
| 1 | 2026-10-18 | H | Crunch | 3-4 (L) | regulation | Josh Kotai 51:56, 16 SA, 1 GA; Vítek Vaněček 6:09, 3 SA, 3 GA | `1029164` |
| 2 | 2026-10-16 | H | Americans | 1-4 (L) | regulation | Vítek Vaněček 58:37, 41 SA, 3 GA | `1029140` |
| 3 | 2026-10-11 | H | Marlies | 2-5 (L) | regulation | Josh Kotai 58:11, 23 SA, 3 GA | `1029127` |
| 4 | 2026-10-09 | H | Marlies | 4-5 (L) | shootout | Vítek Vaněček 65:00, 31 SA, 4 GA | `1029105` |
| 5 | 2026-10-03 | A | Marlies | 3-5 (L) | regulation | Josh Kotai 58:33, 35 SA, 5 GA | `1029089` |
| 6 | 2026-10-02 | A | Senators | 5-2 (W) | regulation | Vítek Vaněček 60:00, 27 SA, 2 GA | `1029071` |

Rows and goalies from the HockeyTech schedule and game-summary feeds, retrieved 2026-10-21 23:05–23:09Z; the target game (id 1029174) is excluded.

#### A4. Distribution, baseline and arithmetic
**League anchor (AHL 2025-26 regular season, all 1,152 games from 2025-10-07 to 2026-04-19, HockeyTech schedule, `final` = 1, final scores):** mean total 6.1328 (LM = 3.0664 per team-game), total SD 2.305, home 3.138 and away 2.995 per game (home edge HE = +0.1432; standard error about 0.077), home-win rate 0.5165, margin SD 2.608, games reaching overtime 0.2326 (175 decided in overtime, 93 in a shootout), regulation home wins 0.4019 and away wins 0.3655, share of home wins by 2+ 0.6050 and of away wins by 2+ 0.5691, total = 5 in 0.2309 and = 6 in 0.0972 of games. 2023-24 and 2024-25 league means were 6.061 and 6.060.

**Carry-over (measured, 32 teams per pair, HockeyTech schedules for seasons 81, 86, 90):** goals-for slope 0.425 (2023-24 → 2024-25) and 0.323 (2024-25 → 2025-26), mean **0.374**; goals-against slope 0.420 and 0.458, mean **0.439**. Residual team SD of (GF + GA): 0.320 and 0.302 (mean 0.311); of (GF − GA): 0.438 and 0.544 (mean 0.491).

**Ratings (k = 20):** 2025-26 deviations from LM: Marlies GF +0.114, GA +0.100; Bridgeport/Hammers GF −0.025, GA +0.017. Prior = slope × deviation: Marlies +0.0426 / +0.0439; Hammers −0.0094 / +0.0075. Current 2026-27 deviations (6 games): Marlies GF 23/6 − 3.0664 = +0.7669, GA 20/6 − 3.0664 = +0.2669; Hammers GF 18/6 − 3.0664 = −0.0664, GA 25/6 − 3.0664 = +1.1003. Weights 6/26 current, 20/26 prior. Marlies: o = 0.2308 × 0.7669 + 0.7692 × 0.0426 = **+0.2098**, d = 0.2308 × 0.2669 + 0.7692 × 0.0439 = **+0.0954**. Hammers: o = **−0.0225**, d = 0.2308 × 1.1003 + 0.7692 × 0.0075 = **+0.2596**.

**Centre (Toronto home):** T = 2 × 3.0664 + (0.2098 + 0.2596 − 0.0225 + 0.0954)/2 = 6.1328 + 0.2712 = **6.4040** goals; M = [(0.2098 − 0.0954) − (−0.0225 − 0.2596)]/2 + 0.1432 = 0.1983 + 0.1432 = **+0.3415** (Marlies). Expected final score Marlies 3.37, Hammers 3.03.

**Mixture and widths.** Centre standard deviations: total √[(√2 × 0.311/2)² + (√2 × 0.172)²] = 0.328, margin √[(√2 × 0.491/2)² + (√2 × 0.172)²] = 0.424 (carry-over residual plus goalie talent). Three-point offsets with weights 0.25/0.50/0.25: total ±0.464 goals, margin ±0.600 goals, nine states, independent. Effective SD total 2.328, margin 2.642 (league 2.305 / 2.608).

**Row formulas.** Totals: the league pmf of final totals (n = 1,152) tilted by e^(θt) so its mean equals the state's total centre; Over 5.5 = P(total ≥ 6) (0.5952 in the base state). Winner: p_home = Φ[Φ⁻¹(0.5165) + (M − 0.1432)/2.608] (0.5470 in the base state); away = 1 − home. Puck lines: P(Marlies −1.5) = p_home × 0.6050; P(Hammers −1.5) = (1 − p_home) × 0.5691; the +1.5 rows are the complements. Regulation: Marlies = p_home − 0.2326 × 0.5; tie = 0.2326 (league rate, not adjusted); Hammers = 1 − p_home − 0.2326 × 0.5. p_card = Σ states weight × row.

**Baseline (BASELINE_LEAGUE_V1, frozen):** literal 2025-26 AHL frequencies on the identical line, e.g. total ≥ 6 in 633 of 1,152 games = 0.5495; home win 0.5165; Marlies +1.5 = 1 − (1 − 0.5165) × 0.5691 = 0.7248. `TEAM_BASELINE_P`: TB-1-MD for the AHL has no validated constants (nearest sport: NHL, k = 20); the NHL rule that TB-1 has no resolution and the row anchors on BASELINE_P is followed, so the card stays within 0.046 of BASELINE_P everywhere.

**Departure ledger (§8).** The team model differs from the baseline in three places: the total centre is +0.27 goals (both teams scoring more in 2026-27), the margin centre is +0.20 over the home edge, and the effective SDs are 1% wider. Resulting departures by row: Over 5.5 +0.0439, Marlies ML +0.0299, Under 7.5 −0.0402, Marlies +1.5 +0.0170.

**Checks (toolkit §11).** Complements sum to 1: Over + Under 5.5 = 0.5934 + 0.4066; Marlies ML + Hammers ML = 0.5464 + 0.4536; Marlies regulation + tie + Hammers regulation = 0.4300 + 0.2326 + 0.3373 = 0.9999 (rounding); the +1.5 rows and the Over/Under rows come from the same objects. The standings lines in the preview feed (goals exclude the shootout credit: Marlies 22–20, Hammers 18–24) agree with the schedule rows (23–20 and 18–25) once the credit in the 10-09 shootout game is removed.

**Full priced ladder (17 rows):**

| Contract | p_card | p_base | BASELINE_P | Departure | Note |
|---|---:|---:|---:|---:|---|
| Over 4.5 | 0.8092 | 0.8120 | 0.7804 | +0.0289 | excluded from the primary slate (goalies unconfirmed, control 14) |
| Marlies +1.5 | 0.7418 | 0.7422 | 0.7248 | +0.0170 |  |
| Under 7.5 | 0.7237 | 0.7249 | 0.7639 | -0.0402 |  |
| Hammers +1.5 | 0.6694 | 0.6691 | 0.6875 | -0.0181 |  |
| Over 5.5 | 0.5934 | 0.5952 | 0.5495 | +0.0439 |  |
| Marlies ML (OT/SO incl.) | 0.5464 | 0.5470 | 0.5165 | +0.0299 | full game incl. OT/SO reading |
| Under 6.5 | 0.5017 | 0.5007 | 0.5477 | -0.0461 |  |
| Over 6.5 | 0.4983 | 0.4993 | 0.4523 | +0.0461 |  |
| Hammers ML (OT/SO incl.) | 0.4536 | 0.4530 | 0.4835 | -0.0299 | full game incl. OT/SO reading |
| Marlies reg. win (60 min) | 0.4300 | 0.4307 | 0.4019 | +0.0281 | regulation (60-minute) reading, draw loses |
| Under 5.5 | 0.4066 | 0.4048 | 0.4505 | -0.0439 |  |
| Hammers reg. win (60 min) | 0.3373 | 0.3367 | 0.3655 | -0.0281 | regulation (60-minute) reading, draw loses |
| Marlies -1.5 | 0.3306 | 0.3309 | 0.3125 | +0.0181 |  |
| Over 7.5 | 0.2763 | 0.2751 | 0.2361 | +0.0402 |  |
| Hammers -1.5 | 0.2582 | 0.2578 | 0.2752 | -0.0170 |  |
| Reg. tie after 60 | 0.2326 | 0.2326 | 0.2326 | +0.0000 | regulation (60-minute) reading, draw loses |
| Under 4.5 | 0.1908 | 0.1880 | 0.2196 | -0.0289 |  |

#### A5. Supplied contracts, W/P/L/V (unconditional)
| Contract | Reading | W | P | L | V | p_card |
|---|---|---:|---:|---:|---:|---:|
| Hammers ML | R-A full game | 0.4536 | 0 | 0.5464 | 0 | 0.4536 |
| Hammers ML | R-B regulation, tie loses | 0.3373 | 0 | 0.6627 | 0 | 0.3373 |
| Marlies ML | R-A full game | 0.5464 | 0 | 0.4536 | 0 | 0.5464 |
| Marlies ML | R-B regulation, tie loses | 0.4300 | 0 | 0.5700 | 0 | 0.4300 |
| Combined Over 5.5 | every reading | 0.5934 | 0 | 0.4066 | 0 | 0.5934 |
| Combined Under 5.5 | every reading | 0.4066 | 0 | 0.5934 | 0 | 0.4066 |

Joint wins of supplied rows (R-A moneyline; total and margin independent within each state): Marlies ML and Over 5.5 0.3242; Marlies ML and Under 5.5 0.2221; Hammers ML and Over 5.5 0.2692; Hammers ML and Under 5.5 0.1844 (the four sum to 1.0000). Complementary pairs cannot both win.

#### A6. Adjustments and sensitivity
| Driver | Treatment | Effect |
|---|---|---|
| Home edge | +0.1432 goals in M (2025-26 AHL, SE about 0.077) | Marlies +0.14 of the +0.34 margin |
| Goalies | Both starters unknown; measured talent spread as centre width | Width only (±0.46 total, ±0.60 margin) |
| Rest / travel | Both last played 10-18 (3 days' rest); Hamilton and Toronto are both in Ontario, travel not quantified; the Hammers' next game is 10-23 at Laval, the Marlies' 10-24 | 0 |
| Special teams | Marlies PP 20.8% / PK 80.8%, Hammers PP 18.2% / PK 73.9% over 6 games | Context only; inside goals for/against |
| Head-to-head | Marlies 3-0 this season (totals 8, 9, 7); the same games are in both teams' samples | Counted once, inside the 6-game ratings |
| League level | 2025-26 mean (6.133); 2026-27 so far 6.163 (98 games) | Sensitivity only |

| Sensitivity | Total centre | Marlies margin | Marlies +1.5 | Under 7.5 | Hammers +1.5 | Over 5.5 | Marlies ML | Over 4.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Base (card), k = 20** | 6.404 | +0.34 | 0.7418 | 0.7237 | 0.6694 | 0.5934 | 0.5464 | 0.8092 |
| k = 10 | 6.547 | +0.46 | 0.7520 | 0.7026 | 0.6587 | 0.6164 | 0.5642 | 0.8245 |
| k = 40 | 6.305 | +0.26 | 0.7347 | 0.7381 | 0.6770 | 0.5770 | 0.5339 | 0.7980 |
| No carry-over prior (league mean prior) | 6.371 | +0.34 | 0.7413 | 0.7284 | 0.6700 | 0.5881 | 0.5455 | 0.8056 |
| 2025-26 prior only (no 2026-27 games) | 6.175 | +0.15 | 0.7255 | 0.7564 | 0.6868 | 0.5552 | 0.5177 | 0.7827 |
| League-only (baseline centre) | 6.133 | +0.14 | 0.7248 | 0.7623 | 0.6875 | 0.5480 | 0.5165 | 0.7775 |
| Home edge 0.066 (−1 SE) | 6.404 | +0.26 | 0.7352 | 0.7237 | 0.6764 | 0.5934 | 0.5348 | 0.8092 |
| Home edge 0.220 (+1 SE) | 6.404 | +0.42 | 0.7484 | 0.7237 | 0.6625 | 0.5934 | 0.5579 | 0.8092 |
| League level 6.163 (2026-27 so far) | 6.434 | +0.34 | 0.7418 | 0.7192 | 0.6694 | 0.5983 | 0.5464 | 0.8125 |

Reading: the three leading rows (Marlies +1.5, Under 7.5, Hammers +1.5) stay on top in every variant, but Under 7.5 overtakes Marlies +1.5 whenever the team's 2026-27 scoring gets less weight (k = 40, prior only, league only). Marlies win probability stays between 0.52 and 0.56 and Over 5.5 between 0.55 and 0.62. Plausible ranges are sensitivity, not confidence intervals.

#### A7. Family rules and dependence
IH-P1 endpoint: moneyline readings frozen, totals reading-proof at 5.5. IH-P2 goalies: unresolved, so no total reaches Rank 1 (control 14). IH-P3: operator terms unknown (queued). H-R1: odd-total structure is carried by the league pmf (a 2-2 tie lands Under 5.5, a 3-3 tie lands Over 5.5). H-R2: a +1.5 row's main kill path is the empty-net goal; the AHL share of two-goal wins that contain an empty-net goal was **not measured** here (the NHL figure is 73%), and the 0.6050 / 0.5691 shares already include whatever empty-net effect the AHL has. H-R5 width: effective total SD 2.33 ≥ the 1.95 benchmark floor, margin 2.64 ≥ 2.18. Control 25: the three Marlies-Hammers games are counted once. Hockey is a sparse sport in this repository (evidence density `SPARSE`): treat the card as low-evidence. No ML or RL output was read before this card (MLSCOPE-v2).

#### A8. Sources (opened; retrieval times UTC, 21 Oct 2026)
| # | Source | Field used | Retrieved | Role |
|---|---|---|---|---|
| 1 | HockeyTech `modulekit` schedule, season 94 and 90 (`lscluster.hockeytech.com/feed/index.php?feed=modulekit&view=schedule&season_id=94&key=50c2cd9b5e18e390&client_code=ahl&fmt=json`; the public AHL site key, RESEARCH_SOURCE_REGISTER SRC-0609) | Fixture id and time; every finished game with final score and decision; target row excluded by id | 23:05:31, 23:06:50 | Field owner (AHL official site feed) |
| 2 | HockeyTech `gc` preview for game 1029174 | Standings lines, previous meetings; line-up field empty | 23:06:22 | Field owner |
| 3 | HockeyTech `gc` game summaries for the nine finished Marlies/Hammers games | Goalies, shots, power plays, head coaches, venue | ~23:09 | Field owner |
| 4 | HockeyTech schedules for seasons 81, 86, 90 | Carry-over regression (32 teams per pair) | 23:09:34 | Field owner |
| 5 | HockeyTech `statviewfeed` goalies, season 90 | 2025-26 goalie lines and talent spread | ~23:10 | Field owner |
| 6 | HockeyTech `modulekit` transactions and roster, teams 335 and 457 | Dated transactions, roster status counts, goalies | 23:12:38–23:14 | Field owner |
| 7 | Web search (identity only): CP24 https://www.cp24.com/local/hamilton/2026/05/21/hamilton-hammers-name-gives-new-ahl-franchise-a-steel-city-identity/ ; The Hockey News https://thehockeynews.com/nhl/new-york-islanders/latest-news/islanders-new-ahl-affiliate-hamilton-hammers-release-full-2026-27-regular-season-schedule | Hammers are the relocated Islanders affiliate | ~23:08 | Corroboration |
| 8 | Repo: PROBABILITY_TOOLKIT §2.3, §4, §8, §11; RULES_ICE_HOCKEY §0; SELECTION_RULES §§2–5, 9; ARCHIVE_USE_GUIDE R2; RESEARCH_SOURCE_REGISTER SRC-0609 | Recipes, rules, route | 23:04 | Controls |

Independence: sources 1–6 are one lineage (the AHL's own feed). The standings lines in the preview agree with the schedule rows, which is an internal consistency check, not an independent collector. No second independent results source was obtained for the 2026-27 rows (single-lineage, `CORROBORATION_INCOMPLETE`); the rows are official final scores. Not reachable or not searched: club sites and social accounts, beat reporters, NHL recall lists (all deliberately skipped after 23:00Z to protect the clean-input claim). Not used: odds, tips, previews, fantasy content.

#### A9. Completion receipt
| Procedure | Status |
|---|---|
| Authority, identity, duplicate | DONE |
| Official start and zone | DONE (23:00Z, 10:00 AEDT) |
| Timing / known-at | DONE: CLEAN_PRE_START_INPUTS / POST_START_ISSUE; no outcome viewed; request arrived 4:53 after the start |
| Starters, line-ups, injuries | INCOMPLETE: not published; AHL has no injury report |
| L5/L10/L15/L20 with true n, dated rows | DONE for 2026-27 (n = 6 per side; previous season excluded with reasons) |
| Rules, overtime, endpoint | DONE (readings frozen; operator question queued) |
| Distribution, arithmetic, baseline | DONE (one object; BASELINE_LEAGUE_V1 17/17) |
| Supplied rows assessed | DONE (all four, both moneyline readings) |
| Gate, dependence, shadows | DONE |
| Independent second source for results | INCOMPLETE (single AHL lineage) |
| Player rows | NOT_ISSUED |
| Model shadow | See the dated record below |
| Settlement / import | NOT_PERFORMED |

#### Model shadow record (2026-10-21T23:21:51Z, after the card was written and read back)
`python -m ml pregame run` → **`NOT_RUN_NO_RELEASE`**: no active forecast-cycle release for Ice Hockey/AHL (active releases: Baseball/MLB, Ice Hockey/NHL; the NHL release does not cover the AHL). Receipt `research/pregame/LOCAL-20261022F6K3OJNO-G0005/20261021T232151370454Z_PREGAME.csv`. Nothing was frozen in the shadow ledger; the card's p_card, ranks and picks are unchanged. The run happened after the scheduled start (23:00Z), so it could not have been a pre-start freeze in any case.

`SPORTS_ONLY_MARKET_BLIND: APPLIED` · `RESEARCH_ONLY_NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD LOCAL-20261022F6K3OJNO-G0005 -->

# RUNNING FOOTER
<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Last local event key / next local event key | `LOCAL-20261022F6K3OJNO-G0005` / `LOCAL-20261022F6K3OJNO-G0006` |
| Carried cards (original keys) | 1: `LOCAL-20261021OKCSASR01-G0001` |
| New cards / numeric / qualitative / NO_FORECAST | 5 / 5 / 0 / 0 (G0001 NOT_ISSUED draft; G0002 numeric/corners NO_FORECAST; G0003 numeric; G0004 numeric supported approximation/INFORMATION_INCOMPLETE; G0005 numeric, AHL, no player rows) |
| New canonical IDs assigned | NONE; assigned only in the settlement phase (prompt 3 → prompt-4 import) |
| Repository next-ID snapshot | P-623 (snapshot only; no reservation) |
| Pending events / unresolved evidence rows in this mini | 6 / 13 |
| Canonical obligations listed | 8 pointer rows (no ownership transferred) |
| Model shadows frozen | 0 (no frozen numerical model rows; G0004 and G0005 NOT_RUN_NO_RELEASE; earlier card dispositions preserved) |
| Local mini status / import status | ACTIVE / PENDING |
| Settlement / retrospective | NOT_PERFORMED / NOT_PERFORMED |
<!-- END FOOTER -->

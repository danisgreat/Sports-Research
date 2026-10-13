<!-- MINI-LOG-FORMAT: mini-log-6 -->
# Prediction Mini Running Log — P-580 onward

## A. Authority snapshot
| Field | Value |
|---|---|
| Repository / branch / read HEAD | `https://github.com/danisgreat/Sports-Research` / `main` (read-only) / `8831556d0408bb58e3cca0290fface3449bbf2ce`; HEAD's latest observed commit timestamp `2026-10-11T13:26:53Z` |
| Relevant working differences | NOT_VERIFIED — no user-machine Git checkout accessible; public GitHub `main` inspected read-only; local file library inspected separately |
| Method / control / scoring / selection | `MDS-2026.10.11-v10.0` / `CR-2026.10.11-R1` / `SCV-2026.10.11-v6` / `SEL-2026.10.11-v2` (`P_ORDER_V2`) |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_7.md` |
| Highest committed / next canonical ID | `P-579` / `P-580` (CURRENT_STATE + current GAME_LOG_STATUS_CURRENT + last import's 23-record continuity verification; Part 7 opening header is historical) |
| Outstanding local minis and IDs | No unimported P-580+ found in accessible Library or current container; last accessible local master P-556–P-579 fully accounted for and imported. User-machine folders / concurrent writers: NOT_VERIFIED (must recheck before issuing a card). Unimported ID range found: NONE. |
| First working ID | `P-580` (conditional on no newer unsynced local allocation; recheck at first card creation) |
| Reading receipt / opened at | `main` SHA `8831556d0408bb58e3cca0290fface3449bbf2ce` · 2026-10-12T00:34:01+11:00; read `README.md`, `CURRENT_STATE.md`, `GAME_LOG_STATUS_CURRENT.md` (current queue), `CARD_AND_LOG_TEMPLATES.md` §2, `research/prompts/2_START_LOCAL_MINI.md`, `research/prompts/README.md`, `research/prompts/examples/EXAMPLE_ACTIVE_MINI.md`, import `CANONICAL_IMPORT_REPORT.md`, `IMPORT_PLAN.md`, `VERIFICATION_REPORT.md`, `CANONICAL_ID_MAPPING.csv`, `UNRESOLVED_POST_IMPORT.md` under `research/verification/mini_import_P-556_P-579_2026-10-11/`; inspected accessible local settled master & settlement report; direct Part 7 body read NOT_VERIFIED (large-file content endpoint returned empty), canonical tail confirmed by independent import verification report. |
| Mode | LOCAL_MINI_STAGING |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING

## B. Local ID rules
Creating this mini consumes no ID. One retained event receives one permanent working ID; canonical status requires import. Addenda/carryovers consume none. No silent skipping, reuse or renumbering. Only a complete written/read-back card advances the footer. Before allocating P-580 or later, recheck CURRENT_STATE, the status queue, and any newly synced local minis against this snapshot; an unexpected collision, duplicate or prior unsynced local working ID blocks allocation until reconciled. This mini is separate from the canonical cards P-577–P-579.

## C. Carryover and evidence queue

### C1. Non-terminal PENDING_EVENT — 3 canonical cards

The three cards below are existing imported canonical forecasts, **not new local cards**. Their original candidate tables, probabilities, timings and endpoints are frozen. Do not reissue/reorder any pick or change its probability. Latest verified status from the completed 2026-10-11 import; no sporting result research performed here. Previously settled P-557–P-576 are not duplicated.

#### C1.1 · P-577 — PENDING_EVENT / CANONICAL

- **Owner / identity:** canonical P-577, `TENNIS / ATP Shanghai Masters — Alexander Bublik vs Brandon Nakashima — 2026-10-11`. Imported working owner: continuous master `P-556..P-579`; owner mini: `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md`, compiled from the P-572-onward mini for P-577.
- **Event key:** `ATP-SHANGHAI:2026:GRANDSTAND2-BUBLIK-NAKASHIMA-R32:2026-10-11`. **Native event ID:** `NOT_VERIFIED` (ATP tournament official H2H confirms the exact pairing; no match-native code independently retrieved)
- **Original frozen card:** `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md` lines 3535–3655, `<!-- BEGIN CARD P-577 -->` to `<!-- END CARD P-577 -->`. **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_7.md`, `<!-- BEGIN CANONICAL RESEARCH P-577 -->`. Original pick table reproduced *verbatim* below, **REFERENCE ONLY; not newly issued**.
- **Frozen endpoint / definitions:** `ATP men’s best-of-three normal advantage sets; tiebreak at 6-6 in all sets to 7 points win by 2; completed match only for all total-games/aggregate-games handicap rows; tiebreak set contributes 13 games; retirement: framework voids games rows, winner settles advancing player, unless a specified operator rule supersedes`
- **Scheduled start / known time:** `2026-10-11T19:30:00+11:00 (user-estimated, fourth match, NOT a fixed official start)`. **Latest settlement revision:** PENDING_EVENT / no final settlement as of import 2026-10-11; NONE.
- **Open field / status basis:** No verified terminal score as of 2026-10-11T21:58:06+11:00. **Next action:** Verify official terminal set scores, winner, withdrawal/retirement and completed games via ATP/tournament scoreboard; then settle under frozen endpoint.
- **Settlement capture requirement:** `Final match state, per-set score, number of completed sets, game scores and games totals, winner/advancing player, retirement/walkover/withdrawal and any suspension (provider: ATP Tour official results / Shanghai tournament official score; fallback ESPN ATP scoreboard)`
- **Due time:** NOT_VERIFIED; 72 hours after the independently verified final, with final time still NOT_VERIFIED. **Canonical/import status:** CANONICAL / IMPORTED_UNCALIBRATED; no fresh working ID.

Frozen original rank table (no new prediction):

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied Under 24.5) | Combined total games Under 33.5 — completed best-of-three match (tiebreak set = 13 games) | 89.9% | FROM_DISTRIBUTION:tennis_shanghai_exact_point_set_form_v1 | Total-games tree centre 24.37; fewer than 11% at 34+ | 34+ games: consecutive 7-6 or 7-5 sets plus long decider |
| 2 | PICK | ANALYST_DERIVED (replaces supplied Bublik +1.5) | Brandon Nakashima +5.5 aggregate games — completed best-of-three match | 89.7% | FROM_DISTRIBUTION:tennis_shanghai_exact_point_set_form_v1 | Match-level form allows either player to win, but +5.5 games is a large cushion | Bublik gains 6+ aggregate games advantage |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Over 24.5) | Combined total games Over 17.5 — completed best-of-three match | 88.8% | FROM_DISTRIBUTION:tennis_shanghai_exact_point_set_form_v1 | Hard-court service holds near 88% for both in prior 52 weeks | One player wins in two lopsided sets, total <=17 |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Under 24.5) | Combined total games Under 32.5 — completed best-of-three match | 86.9% | FROM_DISTRIBUTION:tennis_shanghai_exact_point_set_form_v1 | Model total SD 6.18 games; long tails remain | 33+ games from a long deciding-set or two tight sets |
#### C1.2 · P-578 — PENDING_EVENT / CANONICAL

- **Owner / identity:** canonical P-578, `BASKETBALL / NBA Preseason — Dallas Mavericks @ Houston Rockets — 2026-10-11`. Imported working owner: continuous master `P-556..P-579`; owner mini: `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md`, compiled from the P-572-onward mini for P-578.
- **Event key:** `NBA_PRESEASON:2026-27:0012600016:2026-10-11`. **Native event ID:** `NBA 0012600016` (NBA.com exact-game official page)
- **Original frozen card:** `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md` lines 3658–3788, `<!-- BEGIN CARD P-578 -->` to `<!-- END CARD P-578 -->`. **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_7.md`, `<!-- BEGIN CANONICAL RESEARCH P-578 -->`. Original pick table reproduced *verbatim* below, **REFERENCE ONLY; not newly issued**.
- **Frozen endpoint / definitions:** `Full official preseason game: four 12-minute quarters, overtime periods of 5 minutes if tied; all team points incl. any OT; NBA-declared terminal final. Neutral site Venetian Arena Macao; no Houston geographic home-court advantage. Operator-specific wager action/void terms unverified.`
- **Scheduled start / known time:** `2026-10-11T21:00:00+11:00 (scheduled; actual tip NOT_VERIFIED)`. **Latest settlement revision:** PENDING_EVENT / no final settlement as of import 2026-10-11; Canonical research addendum A8-20261011-210851 (already imported; no new ID).
- **Open field / status basis:** Scheduled start reported delayed; no terminal NBA box score at 2026-10-11T21:58:06+11:00. **Next action:** Verify official NBA game 0012600016 final, quarters, OT and player starters/DNP; keep the existing A8 addendum diagnostic; settle original picks.
- **Settlement capture requirement:** `official full-game final team scores, regulation score, OT flag, four quarters, official five starters, DNPs, withdrawals, tip time (provider: NBA official game 0012600016 / official NBA Game Book; independent structured fallback ESPN or RealGM)`
- **Due time:** NOT_VERIFIED; 72 hours after the independently verified final, with final time still NOT_VERIFIED. **Canonical/import status:** CANONICAL / IMPORTED_UNCALIBRATED; no fresh working ID.

Frozen original rank table (no new prediction):

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | Total points **Under 258.5**, NBA preseason full game incl. OT | 89.7% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Preseason-adjusted pace×PPP centre 228.37; wide NBA/rotation uncertainty | 259+ points from fast tempo, hot shooting, deep bench or overtime |
| 2 | PICK | ANALYST_DERIVED | Total points **Over 198.5**, NBA preseason full game incl. OT | 89.6% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Same total distribution, no new scoring estimate | 198 or fewer from rested scorers, slow pace, poor shooting |
| 3 | INFORMATIONAL | ANALYST_DERIVED | Houston Rockets **+21.5**, NBA preseason full game incl. OT | 89.3% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Houston+Dallas joint game margin, neutral-site scenario | Dallas wins by 22+ |
| 4 | INFORMATIONAL | ANALYST_DERIVED | Dallas Mavericks **+24.5**, NBA preseason full game incl. OT | 88.7% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Same margin distribution and preseason roster width | Houston wins by 25+ |
#### C1.3 · P-579 — PENDING_EVENT / CANONICAL

- **Owner / identity:** canonical P-579, `BASKETBALL / Liga ACB — La Laguna Tenerife @ UCAM Murcia — 2026-10-11`. Imported working owner: continuous master `P-556..P-579`; owner mini: `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md`, compiled from the P-572-onward mini for P-579.
- **Event key:** `ACB:2026-27:UCAM-LLT-20261011:2026-10-11`. **Native event ID:** `NOT_VERIFIED` (official match center lists the dated pairing, but match ID unavailable)
- **Original frozen card:** `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md` lines 3860–3973, `<!-- BEGIN CARD P-579 -->` to `<!-- END CARD P-579 -->`. **Canonical pointer:** `prediction logs/PREDICTION_LOG_COMBINED_7.md`, `<!-- BEGIN CANONICAL RESEARCH P-579 -->`. Original pick table reproduced *verbatim* below, **REFERENCE ONLY; not newly issued**.
- **Frozen endpoint / definitions:** `Four 10-minute FIBA/ACB regulation quarters + every 5-minute overtime period until winner; all listed totals/handicaps include OT, score integer points, no half-point push; operator-specific action terms UNKNOWN_DEFINITION`
- **Scheduled start / known time:** `2026-10-11T21:30:00+11:00 (scheduled; actual tip NOT_VERIFIED)`. **Latest settlement revision:** PENDING_EVENT / no final settlement as of import 2026-10-11; NONE.
- **Open field / status basis:** Official schedule had no terminal result as of 2026-10-11T21:58:06+11:00. **Next action:** Verify official ACB final score, OT, starters and minutes and settle original picks.
- **Settlement capture requirement:** `Full-time final points, quarter scores, OT flag/OT scores, official five starters, minutes, inactive players (provider: acb.com exact-match box score; fallback FIBA LiveStats and independent structured scores)`
- **Due time:** NOT_VERIFIED; 72 hours after the independently verified final, with final time still NOT_VERIFIED. **Canonical/import status:** CANONICAL / IMPORTED_UNCALIBRATED; no fresh working ID.

Frozen original rank table (no new prediction):

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied 170.5 totals) | Combined total points **Under 197.5** — full game incl. OT | 89.66% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Early-season pooled matchup total around 172, conservative 20-point SD | Exceptional offence, explosive fourth quarter or OT produces 198+ |
| 2 | PICK | ANALYST_DERIVED (replaces supplied 170.5 totals) | Combined total points **Over 147.5** — full game incl. OT | 89.34% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Wide lower bracket spans current offence and typical ACB scoring | Low-efficiency game, Boum out, Tenerife reduced rotation, 147 or fewer |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces Murcia −5.5) | UCAM Murcia **+13.5** point handicap — full game incl. OT | 88.91% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Home Murcia 62% favourite, substantial but unverified cushion | Tenerife wins by 14+ |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces 170.5 total) | Combined total points **Over 148.5** — full game incl. OT | 88.39% | FROM_DISTRIBUTION:basketball_acb_shrunk_pace_joint_normal_ot_v1 | Near-duplicate, slightly narrower Over lower-tail threshold | 148 points or fewer |

### C2. Terminal UNRESOLVED_EVIDENCE — 0 confirmed records

NONE identified in the completed import's outstanding sporting queue. Historical source/operator/process limitations remain with the original settled cards and reports and are **not** silently declared resolved. The latest import's separate process notes (Part 7 historical opening header and proposed lineup rule) are not sporting evidence queue records; the pending lineup rule was not adopted.

### C3. Local custody reconciliation

| Item | State / disposition |
|---|---|
| P-557–P-576 | FINAL_SETTLED / CANONICAL per completed import mapping and settlement report; no new carryover forecast |
| P-577–P-579 | PENDING_EVENT / CANONICAL; carried above 1:1 with owner event keys |
| P-580 onward | Unimported working ID found: NONE in accessible prior files; inaccessible local computer storage and competing writers NOT_VERIFIED |
| Historical P-518–P-522 | RESERVED; no new allocation or resurrection |
| Previous queue disposition | 3 pending events carried; 0 confirmed terminal unresolved-evidence records omitted; non-sporting process gaps preserved by pointer |
| Pending cap | PASS: 3 ≤ 5; alert not triggered |
| Sequence | Last imported local P-579; proposed first P-580, no known skip/overlap in accessible evidence |

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD P-580 -->
## Card · P-580 · Ice hockey / Czech Tipsport Extraliga · Motor České Budějovice vs Bílí Tygři Liberec · 2026-10-11 (venue date)

- **Working ID:** `P-580 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`. Local mini issue on 2026-10-12T02:01:18+11:00 (AEDT), LATE_START_UNVERIFIED. This ID is locally allocated only, not committed in GitHub, and this is **NOT a certified prospective pregame issue**.
- **Event key / native ID / aliases:** `CZE-ELH:2026-27:179863:2026-10-11`; official federation detail `179863`, round/game no. `66`; team aliases `BANES Motor České Budějovice`, `Motor`, `Č. Budějovice`, `CEB`, `Bílí Tygři Liberec`, `LIB`.
- **Authority:** published GitHub `danisgreat/Sports-Research` `main` HEAD `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae`; `MDS-2026.10.11-v10.0` / `CR-2026.10.11-R1` / `SCV-2026.10.11-v6` / `SEL-2026.10.11-v2` P_ORDER_V2; no GitHub writes; user machine working tree NOT_VERIFIED.
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO` / `ISSUED_LOCALLY` / `LATE_START_UNVERIFIED`. The original calculations were drafted before the scheduled start and **are unchanged**. Actual start and confirmed goalies are NOT_VERIFIED; the canonical Part 7 body could not be independently fetched. The card is retained for local custody and retrospective audit, **EXCLUDED from clean prospective pregame cohorts**, with these verification gaps disclosed.
- **Timing:** scheduled `2026-10-11T17:00:00+02:00` = `2026-10-11T15:00:00Z` = `2026-10-12T02:00:00+11:00`; original statistical input cutoff before scheduled start (2026-10-11 17:00 CEST); original event research approx. 2026-10-12 01:45–01:51 AEDT; research completion approx. 01:51 AEDT; original draft ≈01:54 AEDT. **Actual local issue:** `2026-10-12T02:01:18+11:00`; official page re-opened in the current session shortly before scheduled kickoff and displayed `0:0` with empty goalie/player tables, which is NOT reliable actual-start evidence. **Last state recheck:** current-session official match page pre-issuance (precise provider update timestamp NOT_VERIFIED). **Actual start:** NOT_VERIFIED. **Outcome exposure:** NO live/final scoring facts used for the original calculations; no result added during issue.
- **Scheduled lead / band:** -1.31 minutes to scheduled start at local issue (`scheduled kickoff crossed`); `LATE_START_UNVERIFIED`; research lead was ~9 minutes and is **not** the issued lead. No backdating or prospective qualification.
- **Venue:** Budvar Arena, České Budějovice, Czechia; round 10, regular season.
- **Endpoint / definition:** primary research assumption FULL official game, 60-minute regulation plus 5-minute 3v3 sudden-death OT, then shootout if tied. One winning goal is credited to the full-game final on an OT/SO-decided regulation tie; regulation draws remain a distinct model state. `Budejovice ML` and `Liberec ML` refer to full-game winner **only under this explicitly declared framework convention**; supplying platform/operator action rules is `UNKNOWN_DEFINITION`. All totals and proposed handicaps count that extra goal; integer score, half-goal lines, no push if the game is valid. Cancellation/postponement/operator void convention `UNKNOWN_DEFINITION`.
- **Distribution object:** `CEB_LIB_POISSON_20261011_v1` — independent regulation Poisson `H~Pois(2.580166625)`, `A~Pois(2.913499958)`, covariance 0 **as an analyst approximation, not a measured fact**. If H=A at 60 minutes, credit a single OT/SO winner goal, H with conditional 0.50 and A with 0.50. The equal OT split is an unvalidated assumption; no NHL coefficients are transferred. Exact finite grid 0–23 goals each, negligible remaining mass beyond grid; detailed arithmetic A4. Historical rates already include some observed empty-net scoring; a separate endgame-empty-net branch is `NOT_COMPUTED`, a material limitation.
- **Expected score:** regulation Motor `2.5802`, Liberec `2.9135`, total `5.4937` (independent-Poisson SD `2.3439`), signed Motor−Liberec margin `−0.3333` (SD `2.3439`); regulation draw `0.1730`. Full game expected Motor `2.6667`, Liberec `3.0000`, total `5.6667` (SD `2.3346`), signed margin `−0.3333` (SD `2.3805`), no full-game draw by model. No shot/xG or empty-net conditional SD support beyond this approximation.
- **Baseline:** `BASELINE_UNAVAILABLE` — the actual repo Czech Extraliga CSVs for 2022, 2023, 2024, 2025 have **zero data rows**; no frozen league-only exact-line empirical W/L distribution, home/away regulation split or validated Czech OT-conditioned count model. Contemporary league table gives 365 team goals over 62 games (5.887 per game), useful as a goal-level diagnostic only and not an exact-line baseline probability. All `BASELINE_P` values therefore `NOT_COMPUTED`.
- **Regime flags / context:** NONE; early season nine games per club is separately disclosed, not a measured EARLY_SEASON multiplier. Home venue known, home-ice numeric adjustment `NOT_ESTIMATED`; special teams included in observed season GF/GA, no unsupported second adjustment. Rest: Motor last 8 Oct at Plzeň (3 local calendar days), Liberec last 9 Oct against Karlovy Vary (2 days), normal short travel, numeric rest effect `NOT_ESTIMATED`.
- **Settlement fields / capture plan:** official Czech federation match 179863 final game status, period-by-period goals, regulation score, any 5-minute OT/shootout and decisive credited goal, final home/away goals, named starting goalies and TOI, empty-net markers where supported; provider `https://czehockey.cz/game/detail/179863`, fallback league match report / independent structured hockey score. Operator-specific definition/status still needs checking. Human manual check 12 October after verified final; no capture automation or notification scheduled. Latest final time and due time NOT_VERIFIED (review target within 72h of verified final).
- **Rules read / archive check:** `CURRENT_STATE.md`, `METHOD.md`, `CURRENT_RULES.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md` §§2–3, `RULES_ICE_HOCKEY.md` §0, `LEAGUE_PROFILES.md` (NHL reference only, no Czech profile), `SOURCES.md` §3.9 plus non-NHL official route, `ARCHIVE_USE_GUIDE.md`, `PROBABILITY_TOOLKIT.md` Poisson, `BASE_RATES_REGISTER.md` NHL notes not transferred, `research/prompts/1_GAME_CARD.md` ICE HOCKEY, `GAME_LOG_STATUS_CURRENT.md` and complete original P-580 mini. Archive `Previous Sports Results/Ice Hockey/Czech Extraliga/{2022,2023,2024,2025}/{year}_games.csv`, 4 files × 0 logical rows; no usable before-cutoff dates. Current official team totals source used instead, n=9 each; source independence UNKNOWN.
- **Evidence receipt:** see A3 for official source URLs and exact 2026 pre-match fields. Publication timestamps unavailable. Link retrieval was before scheduled kickoff. No bookmaker odds, lines, market/tip sources or prices used.

### Decision block

**Research assessment:** Liberec is a narrow model favourite on the full-game endpoint. The raw 5.5 total is nearly balanced; the supplied Under is 53.00%, not a strong-confidence selection. Goalies and starting skater lines remain unconfirmed, and the team's nine-game rates are noisy. Locally logged Rank-1 and Rank-2 candidates are long cushions; their estimated high coverage is mostly a property of broad thresholds, not demonstrated skill.

| Rank | Role | Tag | Contract key / exact proposition | p_card | BASELINE_P | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | `margin_lib+2.5_full`: Liberec **+2.5 goals**, full match including OT/SO | **89.1554%** | NOT_COMPUTED | CEB_LIB_POISSON_20261011_v1 | Motor wins by at least three, possibly aided by empty-net goal or starter mismatch |
| 2 | PICK | ANALYST_DERIVED | `total_under8.5_full`: combined total **Under 8.5 goals**, full match including OT/SO | **87.2092%** | NOT_COMPUTED | Same joint score object | Nine or more final goals: special teams, finishing, weak goaltending, empty net |
| 3 | INFORMATIONAL | ANALYST_DERIVED | `margin_motor+2.5_full`: Motor **+2.5 goals**, full match including OT/SO | **82.8332%** | NOT_COMPUTED | Same joint score object | Liberec wins by at least three |
| 4 | INFORMATIONAL | ANALYST_DERIVED | `total_under7.5_full`: combined total **Under 7.5 goals**, full match including OT/SO | **81.0266%** | NOT_COMPUTED | Same joint score object | Eight or more final goals |

**Rank-1 gate:** `RANK1_UNSTABLE`: Rank 1 p=89.1554% ≥62%; best eligible non-complementary alternative `total_under8.5_full` p=87.2092%; gap **1.9462 percentage points** <4; floor passes, lead fails. No threshold tuning. These calculations are frozen in this **late, local-only issue** and remain performance-ineligible as clean pregame selections.
**Rank-2 floor:** PASS (87.2092% ≥58%) on the issued-local, uncalibrated numeric slate.
**Joint failure:** local primary losses co-occur when Motor wins by ≥3 **and** final total ≥9: **1.8600% unconditional** in the common Poisson score grid. Both decisive=1.0000 conditional on a valid completed game and the stated half-line definitions. This is an estimate with significant tail-model/empty-net uncertainty; it is not independent product of losses.
**Shadow gate / Rank 2:** `RET03` removes same-quantity margin alternatives, retains Under 8.5 87.2092%, gap1.9462 → RANK1_UNSTABLE. `RET04` different quantity = Under 8.5 (87.2092%). `XCARD6` minimum-joint-failure = Motor +2.5 (82.8332%), whose losing set is disjoint from Liberec +2.5's loss, exact joint-loss 0 — **MECHANICALLY_PROTECTED**, NOT_PRIMARY.
**Adjustment dependence:** `NONE_APPLIED`; frozen neutral anchor already reflects observed season outcomes; missing goalie/rest adjustments are not estimated. Scenarios change rankings, so `ADJUSTMENT_DEPENDENCE_NOT_ASSESSABLE` for unverified starters. See A6.
**Potential winner:** Motor 44.4760%, Liberec 55.5240% including OT/SO; regulation Motor ahead 35.8260%, draw 17.3000%, Liberec ahead 46.8740%. Winning side Liberec, weak lean. These sum to 100% at each endpoint.
**All supplied contract probabilities** (full game incl OT/SO as assumed): Motor ML **44.4760%**, Liberec ML **55.5240%**, total goals Over 5.5 **46.9995%**, Under 5.5 **53.0005%**. Every supported half-line W/L decisive, P=0,V=0; `p_card=W/(W+L)`.
**Supplied rows not selected:** all four supplied propositions are priced above and excluded from the local top four solely because supported derived wide lines rank higher; this does not prove that wide-line candidates have positive value. Specific action if user intended *60-minute ML* is unresolved; neither side's quoted full-game probability is the 60-minute three-way probability.

### Appendix
#### A1. Identity, timing and state
Official match `https://czehockey.cz/game/detail/179863`, Czech Extraliga 2026/27 round 10, 11 Oct 17:00 CEST; Bílí Tygři club schedule `https://www.hcbilitygri.cz/matches/MUZ/2027`; Budvar Arena. Issue status `ISSUED_LOCALLY / LATE_START_UNVERIFIED` at `2026-10-12T02:01:18+11:00`; independent observed actual puck-drop `NOT_VERIFIED`; generic 0:0 official placeholder is not proof of either a start or a confirmed starter. Official page showed empty player and goalie tables at research. Earliest source check ≈2026-10-12 01:45 AEDT, reading receipt collected by ≈01:51 AEDT. No live game outcomes consumed. Date aliases local Oct11 / Australia Oct12.

#### A2. Frozen supplied contracts / declared derived candidate recipe
- Supplied exact propositions: Motor ML; Liberec ML; full-game total Over 5.5; full-game total Under 5.5. Supplied market labels alone do not confirm action/OT definition; scenario defines full game with a single credited OT/SO goal.
- Derived candidate universe declared for the research calculation: full-game totals Under and Over 2.5,3.5,4.5,5.5,6.5,7.5,8.5; full-game moneyline both teams; both teams' +1.5,+2.5 handicaps. There are no invented player/period/shot contracts. Duplicate total-5.5 rows occur once only.
- The selection ceiling p≤90% applies to eligible retained rows only. Over 2.5 at 94.2148% is **EXCLUDED_ABOVE_CEILING** (unclipped, preserved in A5). Other unsupported goalie/player props are excluded.
- Numeric ordering: all retained candidates sorted by raw unrounded p, tie-break by contract key. The league is sparse; no adjustment optimises the ladder or scans arbitrary tenth-of-goal lines.

#### A3. Evidence and archive inputs
- Federation `https://czehockey.cz/game/detail/179863`: exact match date `11.10.2026, 17:00`; Motor–Liberec, no populated lineups/goalie game stats, game number 66. Official source, publication/update time NOT_VERIFIED, observed in browser 2026-10-12 about 01:45 AEDT.
- Federation team statistics `https://czehockey.cz/competition/club-stats/14?playerCompetitionStatsWidget-filter%5Bclub%5D=9`: in pre-match nine-game snapshot Motor 2.56 GF and 3.11 GA per game; Liberec 2.89 GF and 2.78 GA; PP 23.08% vs 18.18%, PK 73.53% vs 72.41%. Time of raw publication NOT_VERIFIED; historic retrieved page not independently time-stamped. Exact nine-game totals 23-28 Motor, 26-25 Liberec corroborated by league standing at `https://www.irozhlas.cz/sport/elh-2026` and sporting match summaries. This is nine games/team, not 18 independent matchup games.
- Official recent results: Motor 8 Oct Plzeň 1–4, 5 Oct Brno 5–1; Liberec 9 Oct Karlovy Vary 5–0, 4 Oct Mladá Boleslav 5–3 (`https://ceskyhokej.cz/en/competition/games/14?gameListWidget-filter%5Bclub%5D=15&gameListWidget-page=174`). No last-game over-weighting.
- Published sporting goalie figures (secondary match-stat page `https://www.hokej.cz/zapas/2928320`): Motor Milan Klouček five appearances, 92.75% SV; Jan Strmeň five appearances, 91.61%; Matyáš Mařík one appearance, 86.96%; Liberec Petr Kváča eight appearances, 91.89%; Petr Hamalčík one, 87.50%. **Appearances are not confirmed starts.** Source webpage can host prohibited market material; none was read or used as an input to the calculation. Collector independence UNKNOWN.
- Official roster, confirmed goalie starts, injuries, 5v5 xG/shot process, scratches and power-play unit combinations: **NOT_VERIFIED**. Exact starter-mixture probabilities are also NOT_ESTIMATED; appearance counts are not treated as starting probabilities.
- Archive files actually fetched from GitHub main: `Previous Sports Results/Ice Hockey/Czech Extraliga/2022/2022_games.csv`, `/2023/2023_games.csv`, `/2024/2024_games.csv`, `/2025/2025_games.csv`: each 244 UTF-8 content characters in fetched text, header only, 0 logical data rows; no pre-cutoff match-level sample, latest usable date NONE. The global `LEAGUE_PROFILES.md` does NOT provide a vetted Czech Extraliga profile. Source team snapshots are external to that archive.
- Contemporary competition-wide standings (`https://www.irozhlas.cz/sport/elh-2026`): 14 teams, total 124 team-games = **62 actual matches**; sum goal GF 365 (= GA 365), league final goals/game 5.8871; league-only diagnostic, not a prefit Poisson score distribution and not enough to recover a regulation/OT baseline from exact-line scoring counts.

#### A4. Regulation distribution, OT/SO, arithmetic and expected score
- Final-score team means from the nine-game source, before any OT correction: `mH = (Motor GF23/9 + Liberec GA25/9)/2 = 2.6666667`; `mA = (Liberec GF26/9 + Motor GA28/9)/2 = 3.0000000`. These are a simple opponent-cross average of **raw outcomes**, NOT measured xG, adjusted for schedule strength, shooting, or goalkeeper mix.
- Those source scores include OT/SO wins when applicable. For one credited goal conditional on regulation tie, assume each side has 50% tiebreak chance and solve self-consistently: `λH = mH − 0.5 q`, `λA = mA − 0.5 q`, `q = Σ[k=0..∞] Pois(k;λH)·Pois(k;λA)`. Iteration yields `q=0.1730000833`, `λH=2.5801666250`, `λA=2.9134999583`. This is an **analyst-chosen** Poisson/OT decomposition, not observed Czech OT frequency.
- Regulation score states: `P(H=h,A=a) = exp(−(λH+λA))·λH^h/h!·λA^a/a!`. If h=a, credit one goal to home with probability .5 or away with probability .5. This gives a single coherent *final* score state object; there are no impossible tied full-game terminal scores. Grid computed for h,a=0…23; numerical residual <1e−12, total conditional masses ≈1.0000.
- Regulation result: H ahead `.3582597581`; draw `.1730000833`; A ahead `.4687401586`. Final result: H `.4447597998`; A `.5552402002`.
- Full-game expected scores: H `λH+q/2=2.6666667`, A `λA+q/2=3.0000000`; full total `λH+λA+q=5.6666667`; signed home-minus-away margin `−.3333333`. Regulation SD total and margin `sqrt(λH+λA)=2.3439`; full-game SD total `sqrt(5.45015915)=2.3346`; full signed margin SD `sqrt(5.66666665)=2.3805`. Covariance of final team totals induced by one-goal OT adjustment NOT separately estimated for model use; joint enumeration handles these supplied row correlations.
- FULLGAME Over5.5 = `Σ_{h,a} P(h,a)·[final_h+final_a≥6] = .4699954502` and Under = `.5300045498`; no score-based PUSH at half lines. FULLGAME ML as above. This specifically moves 2–2 regulation ties into 3–2 (total 5), 3–3 into 4–3 (total 7); it does not use the incorrect shortcut of automatically adding one goal to every match.
- **Empty-net mechanism limitation:** final GF/GA rates aggregate past empty-net outcomes, but cannot isolate conditional late trailing-pull frequency, and the Poisson grid does not add an independently parameterised pulled-goalie tail. Thus full-game >5.5 and +2.5 margin tails can be wrong; do NOT claim explicit empty-net tail is estimated. Opponent-adjusted shots/xG and goalie workload lack input data. This is an unsupported simplification with wide uncertainty, not a complete fitted hockey model.

#### A5. All priced rows and W/P/L/V, full-game convention
All shown p values are W unconditional, P=0 and V=0 for assumed completed full-game half-line contracts, L=1−W. The two full-game moneylines are mutually exclusive/exhaustive and likewise have no draw/push. Operator void actions remain UNKNOWN_DEFINITION.

| Proposition | W | P | L | V | p_card | Decision |
|---|---:|---:|---:|---:|---:|---|
| Liberec ML | .555240 | 0 | .444760 | 0 | 55.5240% | SUPPLIED/UNSELECTED |
| Motor ML | .444760 | 0 | .555240 | 0 | 44.4760% | SUPPLIED/UNSELECTED |
| Total Over 5.5 | .469995 | 0 | .530005 | 0 | 46.9995% | SUPPLIED/UNSELECTED |
| Total Under 5.5 | .530005 | 0 | .469995 | 0 | 53.0005% | SUPPLIED/UNSELECTED |
| Total Over 2.5 | .942148 | 0 | .057852 | 0 | 94.2148% | EXCLUDED_ABOVE_CEILING |
| Total Under 2.5 | .057852 | 0 | .942148 | 0 | 5.7852% | NOT_RETAINED |
| Total Over 3.5 | .797582 | 0 | .202418 | 0 | 79.7582% | eligible |
| Total Under 3.5 | .202418 | 0 | .797582 | 0 | 20.2418% | eligible |
| Total Over 4.5 | .699597 | 0 | .300403 | 0 | 69.9597% | eligible |
| Total Under 4.5 | .300403 | 0 | .699597 | 0 | 30.0403% | eligible |
| Total Over 6.5 | .361500 | 0 | .638500 | 0 | 36.1500% | eligible |
| Total Under 6.5 | .638500 | 0 | .361500 | 0 | 63.8500% | eligible |
| Total Over 7.5 | .189734 | 0 | .810266 | 0 | 18.9734% | eligible |
| Total Under 7.5 | .810266 | 0 | .189734 | 0 | 81.0266% | eligible |
| Total Over 8.5 | .127908 | 0 | .872092 | 0 | 12.7908% | eligible |
| Total Under 8.5 | .872092 | 0 | .127908 | 0 | 87.2092% | eligible, Rank2 |
| Liberec +1.5 | .788834 | 0 | .211166 | 0 | 78.8834% | eligible |
| Motor +1.5 | .697357 | 0 | .302643 | 0 | 69.7357% | eligible |
| Liberec +2.5 | .891554 | 0 | .108446 | 0 | 89.1554% | eligible, Rank1 |
| Motor +2.5 | .828332 | 0 | .171668 | 0 | 82.8332% | eligible, Rank3 |

#### A6. Uncertainty, lineup/goalie mixture and adjustments
No unverified athlete is called a confirmed starter; no physical trend estimate imported from NHL. Base already reflects realised special teams, home/away scoring as combined in nine-game rates. No unsupported numeric home-ice, back-to-back or power-play multipliers were used.

| Input / regime | Available fact | Applied numeric adjustment | Uncertainty route |
|---|---|---|---|
| Goalie Motor | Klouček/Strmeň/Mařík seen in prior games, **NOT confirmed today** | NONE, unknown starter weights | Sensitivity Liberec λ_A ±0.35 for starter-quality uncertainty |
| Goalie Liberec | Kváča/Hamalčík appearances, **NOT confirmed today** | NONE, unknown starter weights | Sensitivity Motor λ_H +0.45 for possible backup |
| Power play | Motor 23.08%, Liberec 18.18% in nine games | NONE, already represented in GF | Unknown opportunities and covariance |
| Home venue | Motor home Budvar Arena | NONE, no validated Czech home-edge parameter | Could favour Motor; not priced |
| Rest | Motor played Oct8, Liberec Oct9 | NONE, insufficient league-specific measured effect | Liberec shorter rest potential negative |
| Empty net | Low-frequency high-goal tail in final rates | NOT_SEPARATELY_MODELED | Missing late-score-state transitions cause tail uncertainty |

| Scenario (analyst sensitivity, not confidence interval) | λ Motor / λ Liberec regulation | Liberec ML | Under 5.5 | Liberec +2.5 | Under 8.5 |
|---|---|---:|---:|---:|---:|
| Low-scoring, both −0.30 | 2.280 / 2.613 | 55.8% | 63.5% | 90.5% | 92.2% |
| BASE | 2.580 / 2.913 | 55.5% | 53.0% | 89.2% | 87.2% |
| High-scoring, both +0.30 | 2.880 / 3.213 | 55.3% | 43.1% | 87.9% | 80.9% |
| Motor goalie weakness, λ Liberec +0.35 | 2.580 / 3.263 | 60.9% | 47.1% | 91.1% | 83.8% |
| Liberec backup weakness, λ Motor +0.45 | 3.030 / 2.913 | 48.1% | 45.5% | 84.1% | 82.5% |

No independent correction for season-wide scoring dispersion is established. Low scoring can move Under 8.5 above the 90% selection ceiling, and a Liberec backup scenario can reorder the top two. Hence **lineup-dependent primary order is not validated**, and the numerical probabilities are sensitivity estimates only, not confidence intervals. The user should not interpret the base values as reliably precise to hundredths of a point.

#### A7. Gate, family, dependence and shadows
- Current v10 `P_ORDER_V2` ranks by p_card; v9 RM-1 q is superseded for new cards. Four rows max, all supported by the shared count model under the stated assumptions.
- IH-P2 missing confirmed starters triggers explicit uncertainty and **no total may be Rank1**. Proposed Rank1 Liberec +2.5 (not a total) satisfies only that positional restriction; endpoint and operator definition remain conditional. Goalies' effects could change the top two, as shown.
- Primary Rank1 floor PASS but lead FAIL: gap 1.9462 points to best eligible non-complement Under8.5. RET03 same outcome. Rank2 floor PASS.
- Exact common-grid primary joint-loss .018600 (both decisive 1 in completed game); losing sets: Motor wins by ≥3 and nine or more goals. Frechet bounds from marginal L .108446 and .127908 would be [0, .108446]; the assumed grid refines this to .018600 (model-dependent).
- XCARD6 alternate Motor+2.5: disjoint losing sets with Liberec+2.5 → 0 modeled simultaneous losses; strictly MECHANICALLY_PROTECTED but not new information or proof of skill. RET04 different-quantity alternative Under8.5.
- No pseudo-benchmark from NHL margin or empty-net percentages is transferred to Czech Extraliga. Numeric learner/regime certification NOT_AVAILABLE.

#### A8. Sources, failure mechanisms, capture and refresh
Source chain: Czech federation game page and team statistics → official Liberec dated schedule and league scoreboard → independent iRozhlas aggregate/secondary sporting goalie table for corroboration. Source timestamps `NOT_VERIFIED` and collector independence UNKNOWN. Sporting-only fields were used; no betting markets, tips or odds. None provides a frozen list of starters at research time. Recheck both goalie announcements and actual game state for a future diagnostic addendum; this local issue is explicitly `LATE_START_UNVERIFIED` and must never be relabelled as clean pregame. On settlement verify final score, regulation periods, OT/SO marker, and full-game contract definition. **No settlement or recurring job performed.**

#### A9. Integrity and custody audit
- C1: current methods, sport, source/selection/template and active mini read, HEAD and missing Czech archive disclosed — PARTIAL because source availability/timing and canonical log body incomplete.
- C2: official match ID/aliases known; local mini checked empty P-580; CURRENT_STATE/status next P-580; GitHub Part 7 raw body fetch returned empty so full duplicate scan **NOT_VERIFIED** — UNVERIFIED; canonical collision gate remains an import blocker, not a claim of canonical custody.
- C3: fixed declared slate; user contracts all retained diagnostically; top four numeric decreasing; ceiling respected; qualifier 4 rows only — PASS on frozen late-issue mathematics.
- C4: dual Poisson 0–23 grid, score/OT branch sums 1, complements/WPLV exact within 0.0001 — PASS computational research.
- C5–C6: gate failure disclosed; Rank2 floor PASS; joint grid exact under assumptions, alternative mechanical protection separated — PASS as diagnostic.
- C7–C8: sensitivity printed, no undocumented operative regimes; unverified starter mixture is a material limit — PARTIAL.
- C9–C10: correct Czech 60m→3v3 OT/SO convention, endpoint assumption disclosed, goalie and empty-net process incomplete; operator convention unverified; capture plan not actual job — PARTIAL.
- C11–C12: actual local issue `2026-10-12T02:01:18+11:00`, official match page re-opened shortly before scheduled kickoff (0:0 placeholder is not confirmed event state); original numerical input assembled before scheduled start, with no observed live/final outcomes consumed; source publication/lineage partly UNKNOWN — PARTIAL, not pregame-certified.
- C13: 4 Czech Extraliga historical CSVs checked, all 0 rows; current nine-game league source disclosed — PASS for inspected range; archive no useful pregame historical rows.
- C14: `BASELINE_UNAVAILABLE` with exact reason; 62-game current aggregate diagnostic is not exact-line baseline — PASS missingness honesty.
- C15: score arithmetic, means, SD, covariance assumption and tail gaps disclosed — PASS approximation disclosure, NOT model validation.
- C16: PASS for local write/readback of this card, preservation of all three original canonical carryover blocks and reconciled footer (`P-580 / P-581`, 1 new card), verified in current session. Pre-match certification and full canonical-body duplicate audit remain NOT_PASSED; no remote write or prospective qualification claimed.

`SPORTS_ONLY_MARKET_BLIND: PASS FOR INPUTS` · `OUTCOME_EXPOSURE: NONE_OBSERVED_IN_RESEARCH` · `ISSUE: LOCAL_MINI_ONLY / LATE_START_UNVERIFIED / NOT_PROSPECTIVE` · `SETTLEMENT: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING` · `GitHub writes: NO`.
<!-- END CARD P-580 -->

**New locally issued cards:** P-580 Motor–Liberec and P-581 Brøndby–Lyngby (2). Canonical pending-event carryovers P-577–P-579 are unchanged. P-581 is explicitly late research and is not a verified pregame forecast.

<!-- BEGIN CARD P-581 -->
## Card · P-581 · SOCCER / Denmark 3F Superliga 2026–27 · Brøndby IF vs Lyngby BK · 2026-10-11

- **Working ID:** `P-581 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`. Locally appended/issued `2026-10-12T02:06:14+11:00` AEDT, after scheduled kickoff; historical/late-research cohort, NOT clean pregame and not certified. The earlier unissued P-580-labelled Brøndby draft was never a local allocation; hockey owns P-580.
- **Event key / native ID / aliases:** `DEN-SUPERLIGA:2026-27:DBU-556151:2026-10-11`; DBU match 556151; Brondby/Brøndby IF, Lyngby BK; venue Brøndby Stadion. No known duplicate in accessible mini and current canonical status; full 1.26MB Part 7 body could not be retrieved through available connector, hence global duplicate check NOT_VERIFIED.
- **Authority:** `danisgreat/Sports-Research` `main`, initial research HEAD `8831556d0408bb58e3cca0290fface3449bbf2ce`; local append recheck HEAD `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae`; MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6 / SEL-2026.10.11-v2, P_ORDER_V2. Local unpublished differences: hockey P-580 in mini and the present P-581; no GitHub writes; other local computer writers NOT_VERIFIED.
- **Analysis status:** LOCAL_MINI_ISSUED / PENDING_CANONICAL_IMPORT / LATE_START_UNVERIFIED / UNCALIBRATED_ANALYST_SCENARIO; numeric values are crude nine-match score-model estimates, not verified predictive probabilities, fitted xG estimates or investment advice.
- **Timing:** scheduled 2026-10-12T01:00:00+11:00; input cutoff approximately 2026-10-12T00:57:15+11:00 (after official teamsheets / DBU table read); original core research completed 2026-10-12T01:00:46+11:00 and later independent phase/corners supplement compiled after scheduled start; actual local issue/readback below in A9; source-state recheck pre-write: DBU match still displayed schedule and blank score at 00:55 AEDT, but actual non-start NOT_VERIFIED; LATE_START_UNVERIFIED; no live score/results knowingly accessed to build model. Source publication dates in A3; no evidence of whistle-time verification.
- **Scheduled start:** 2026-10-11 16:00 CEST / 2026-10-11T14:00:00Z / 2026-10-12 01:00 AEDT; official DBU.
- **Scheduled lead / band:** local issue at 2026-10-12T02:06:14+11:00, scheduled lead NEGATIVE (after 01:00 AEDT); LATE_START monitoring band. Not a clean verified PREGAME issuance.
- **Endpoint / definition:** Danish regular-season league, 90 regulation minutes plus stoppage, draw allowed; no extra time or penalties. Goal totals exactly regulation; 1H only first 45 + first-half stoppage; supplied 10.5 corners use separately calculated PROVISIONAL statistical counts, but exact operator `wonCorners` definition and action convention remain UNKNOWN_DEFINITION for selection/settlement; half-goal .5 thresholds: no push, unresolved abandonment/void follows frozen framework convention.
- **Distribution object:** `P581_INDEPENDENT_POISSON_RAW9` — lambda_home=1.555556 goals, lambda_away=1.388889 goals, independent conditional count model, combined mu=2.944444, no supported Dixon-Coles rho (zero correlation assumed, low-score draw bias). Poorly fitted, low reliability. Tail and arithmetic in A4.
- **Expected score:** regulation Brøndby 1.556 goals (SD 1.247), Lyngby 1.389 (SD 1.179), total 2.944 (SD 1.716), signed home margin +0.167 (SD 1.716); first-half goals total 1.0556 (SD 1.0274), home 0.5000, away 0.5556, from a separately sourced nine-game phase-rate approximation; corners home 5.11, away 5.17, total 10.28 (Poisson SD 3.2062), PROVISIONAL_UNVERIFIED_PROVIDER_DEFINITION. These supplementary phase/corner estimates were compiled after scheduled kickoff and are not eligible clean pregame inputs.
- **Baseline:** `BASELINE_LEAGUE_V1_DAN_2026_ROUND10_RAW`; league-only regulation goals Poisson mu=2.909091, from official DBU table, GF 160 across 55 completed games, 12 clubs, before fixture. Does NOT borrow team means or later results; sample pre-cutoff freshness limited by dynamic page without immutable snapshot. first-half and operator-verified corners BASELINE_UNAVAILABLE (nominal all-league corners mean 10.38 is only a diagnostic); winner/draw baseline NOT_COMPUTED; total exact lines computed independently.
- **Regime flags / context:** NONE; after international break, Brøndby four straight league defeats, Lyngby Colyn unavailable and Ambæk Brøndby first start; no arbitrary numerical multipliers.
- **Settlement fields / capture plan:** DBU match 556151 official final/home/away full goals, match status, half-time score/minutes, goal events if official; corners official `wonCorners` if available from named sports-data operator with verified convention, otherwise UNRESOLVED. Check at +36 h for phase/corners, final within 72 h; no scheduled capture job (NO). Responsibility: manual next settlement task; no automated scheduler.
- **Rules read / archive check:** CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES §§2–3/7, RULES_SOCCER §0, LEAGUE_RULES_SOCCER, LEAGUE_PROFILES soccer, PROBABILITY_TOOLKIT §2, BASE_RATES_REGISTER soccer, SOURCES §3.4, ARCHIVE_USE_GUIDE, prompt 1, current mini, GAME_LOG_STATUS_CURRENT. `Previous Sports Results/Soccer/` confirmed directory via GitHub path check, but Danish Superliga 2025 candidate paths returned NOT_FOUND; no league CSV content or logical season rows retrieved (0 read; coverage NOT_VERIFIED). No purported archive-fit. Official current DBU aggregate only (n=55 games league baseline, team n=9+9).
- **Evidence receipt:** field-owner DBU for venue/event/rates, Brøndby and Lyngby official squads, named XI from club graphic and two structured/report sources; URLs/update/lineage in A3. Additional 1H and corner statistical inputs came from SoccerStats/PredictVantage pre-fixture nine-game summaries with source lineage/definitions unverified; no odds, tips, betting previews or market sources used as model inputs.

- **Provenance/custody:** Migrated from unissued Brøndby P-580 proposed research and subsequent six-contract supplement. The initial ID P-580 was never assigned to that proposal and is already occupied by Motor–Liberec in the active mini; local P-581 is the sole allocated Brøndby card. No user-facing prior probability is recast as a timely pregame issue. No settlement was performed.
- **Local issue/recheck:** `2026-10-12T02:06:14+11:00` AEDT; main HEAD and NEXT canonical ID rechecked via repository `main` (`eb1acf58bb7b8c794a2f6a473f737d921f2d5fae`, GitHub next P-580). The local file, not the GitHub snapshot, is current ID authority for P-581.

### Decision block

The simple regulation-goal model favours a moderately scoring contest but cannot justify a high-confidence side; first-half and corners are separately estimated diagnostic supplied rows, not primary selections. The selected top two are wide, opposing-regime total-goal thresholds and are **MECHANICALLY_PROTECTED** against both losing at once; this is a construction property, **not** evidence of predictive skill. Small team sample, Lyngby's leading scorer suspended, small-sample first-half process, unverified corner definition/dispersion and missing xG are the main uncertainties.

| Rank | Role | Tag | Contract key / exact proposition | p_card | BASELINE_P | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | Combined total goals Under 4.5 — regulation | 82.45% | 83.03% | P581_INDEPENDENT_POISSON_RAW9 | Five or more goals |
| 2 | PICK | ANALYST_DERIVED | Combined total goals Over 1.5 — regulation | 79.24% | 78.69% | P581_INDEPENDENT_POISSON_RAW9 | Zero or one total goals |
| 3 | INFORMATIONAL | ANALYST_DERIVED | Either team wins in regulation (12; draw loses) | 75.53% | BASELINE_UNAVAILABLE: home/draw rates | P581_INDEPENDENT_POISSON_RAW9 | Draw |
| 4 | INFORMATIONAL | ANALYST_DERIVED | Combined total goals Under 3.5 — regulation | 65.97% | 66.76% | P581_INDEPENDENT_POISSON_RAW9 | Four or more total goals |

**Rank-1 gate:** RANK1_UNSTABLE; Rank 1 82.45%, best non-complementary `full_total:over:1.5` 79.24%, gap 3.21 percentage points vs 4.00 minimum; p≥62% passes. This is the original eligible full-goal and result universe, with first-half/corner estimates disclosed as later diagnostics; they do not outrank the displayed top two. The corner statistic remains ineligible pending definition/dispersion verification.
**Rank-2 floor:** PASS (79.24% ≥ 58%).
**Joint failure:** exact 0.0000 under single count model: Under4.5 loses iff total≥5; Over1.5 loses iff total≤1, mutually exclusive. MECHANICALLY_PROTECTED. Both rows always decisive absent separate void/abandonment: probability 1.000 under model.
**Shadow gate / Rank 2:** RET03 (ignore same total-goals quantity) selects regulation `12` with 75.53% and gap 6.92 pp, shadow PASS. RET04 different quantity = 12 (75.53%); joint loss with Rank1 from model NOT_COMPUTED without exhaustive correlated score check, could overlap on even high-scoring draws. XCARD6 = Over1.5 (79.24%), exact joint loss 0.0000; shadows NOT_PRIMARY.
**Adjustment dependence:** NONE, no numerical adjustment fitted; low/base/high scenarios reflect unresolved squad/home/xG uncertainty. The hypothetical high scenario reverses the first two probabilities, so **SENSITIVITY_ORDER_UNSTABLE** (no measured in-model adjustment applied). Large adjustment SD class NOT_ASSESSABLE.
**Potential winner:** Brøndby 41.46%, draw 24.47%, Lyngby 34.07%; 90-minute result including permitted draw, no extra time. Brøndby is highest single outcome, not a confident winner.
**Supplied rows not selected:** 1H Over0.5 65.20% / Under0.5 34.80%, separately estimated and below the top four; full Over2.5 56.42% / Under2.5 43.58%, eligible but below top four. Corners Over10.5 45.19% / Under10.5 54.81%, PROVISIONAL_UNRANKED pending operator field and dispersion verification; parsing `Over/Under` as two distinct supplied rows, not one proposition. Full total 1.5/3.5/4.5 ranks are analyst-derived; see all rows A5.

### Appendix
#### A1. Identity, timing and state
DBU native number 556151, competition regular season round 10, Brøndby home. Time conversion: 16:00 CEST UTC+2 = 14:00 UTC = 01:00 AEDT UTC+11 next calendar day. DBU blank score is not proof of actual non-start. The underlying team/fixture snapshot appeared before scheduled kickoff, but the later supplementary rates and this local append were after it; issue eligibility LATE_START_UNVERIFIED, excluded from clean pregame cohort. Local P-580 hockey record has a different event key; neither earlier unissued Brøndby drafts nor available status records show this event already issued. Full canonical Part 7 body was inaccessible, so global duplicate clearance NOT_VERIFIED. P-581 is now allocated locally; P-580 remains the earlier hockey card.

#### A2. Frozen supplied contracts and candidate recipe
Supplied full-time goals Over/Under2.5; first-half goals Over/Under0.5; regulation match corners Over/Under10.5 (two rows). Declared before pricing: goals-total full-game standard half lines 0.5,1.5,2.5,3.5,4.5,5.5 both directions, plus 1X2 and 1X/X2/12. The initial parent research left phase/corners UNPRICED; the distinct follow-up supplement prices them from competition-specific nine-game inputs. This is a recorded late research completion, not a retrospective pregame model repair. Corners stay non-eligible due to unverified exact definition and dispersion. Every line above 90% true probability excluded; no odds or alternate threshold tuning. One distinct event key, no repeat original forecast. Independent-Poisson parameter recipe fixed to arithmetic average of each club's observed 9-game GF/game with opponent 9-game GA/game; both are season pooled home+away rates (not opponent-strength adjusted beyond simple opponent concession). Home-venue differential and xG effects NOT_MEASURED.

#### A3. Evidence and archive inputs
- [DBU match 556151](https://www.dbu.dk/resultater/kamp/556151_506118/): 11 Oct 2026, 16:00 Europe/Copenhagen, round 10, Brøndby Stadion; official score blank when checked. Page has no explicit independent confirmation of the actual whistle time.
- [DBU official standings](https://www.dbu.dk/resultater/pulje/506118): before Round 10's Brøndby–Lyngby fixture, Brøndby 9 matches, GF 12 GA 15; Lyngby 9 matches, GF 10 GA 16. All 12 clubs have 110 combined matches and 160 GF; league matches n=55, mean total=160/55. Data checked near 00:57 AEDT on 12 Oct; DBU page not historically frozen and may update.
- [Brøndby official starting XI](https://brondby.com/nyheder/herrer/2026/oktober/startopstillingen-mod-lyngby-bk): article published 11 Oct 12:56 CEST, linked image used for XI/bench; [squad](https://brondby.com/nyheder/herrer/2026/oktober/truppen-hjemme-mod-lyngby-bk) published 07:25 CEST.
- [Lyngby official 20-player match squad](https://lyngby-boldklub.dk/2026/10/10/truppen-mod-broendby-if/): 10 Oct 18:48 CEST; [Campo named XI](https://campo.dk/2026/10/11/foerste-gang-i-saesonen-ambaek-fra-start-mod-lyngby/) published 11 Oct 14:52 CEST; [structured lineup](https://www.ysscores.com/en/lineup/5739520/Br%C3%B6ndby-IF-vs-Lyngby-Boldklub) exposes both XIs and nine substitutes each; provider's underlying collection lineage UNKNOWN.
- [FotMob match page](https://www.fotmob.com/matches/brondby-if-vs-lyngby/2tx088): unavailable Simon Colyn (suspension), Oskar Snorre (injury); independence from structured lineup provider NOT_VERIFIED. Club's own 20-player squad excludes both.
**Confirmed Brøndby XI** (official lineup image): Pentz; Villadsen, Alves, Binks, Divković; Ejdum, Slisz, Frøkjær; Hyseni, Younis, Ambæk. **Brøndby bench** (official lineup image): Sonne-Schmidt, Olivier, Mortensen, Wass, Bundgaard, Winther, Fukuda, Canut, Fenger.
**Confirmed Lyngby XI** (Campo plus structured lineup): Kochen; Buur, Aronsson, Garananga, Tytens; Fraulo, Højer, Sandgrav, Thomasen; Gytkjær, Þorvaldsson. **Lyngby bench** (structured lineup cross-checked as remainder of official 20): Ægidius, Allen, Kristjánsson, Hebo, Sertdemir, Steindorsson, Ngabo, Fischer, Anderson.
Colyn (suspended) and Snorre (injured) not among Lyngby's named 20; exact injury relevance not estimated. No confirmed penalty/set-piece takers. Weather/model impact NOT_MEASURED. Archive path search attempted `Previous Sports Results/Soccer/Denmark Superliga/2025/2025_games.csv` and `.../Danish Superliga/2025/2025_games.csv`, both not found; zero logical archived rows scanned (not a claim the repository has none). Last usable archive date NOT_VERIFIED. Actual latest source data known: DBU league standings as checked before scheduled kickoff. Collector independence UNKNOWN (official DBU and clubs are field owners for different claims; other lineup sites not counted as independent collections).

#### A4. Distribution, baseline, expected-score arithmetic and sensitivity
Home lambda = (Brøndby GF/9 + Lyngby GA/9)/2 = (12/9+16/9)/2 = 1.555556; away lambda=(Lyngby GF/9 + Brøndby GA/9)/2=(10/9+15/9)/2 = 1.388889. Both independent Poisson, P(Gh=i,Ga=j)=e^(-h)h^i/i! × e^(-a)a^j/j!, k≥0. Total is Poisson(mu=2.944444); mass normalized over nonnegative integers, explicit marginal tail above 23 negligible and accounted for by 1−partial sum; no arbitrary cap. Mean home/away/total/margin = 1.555556/1.388889/2.944444/+0.166667; variance home/away=1.555556/1.388889, assumed covariance=0, total/margin variance=2.944444. SDs printed on header. This is deliberately uncorrected low-score Poisson, tends to miss dependence and extra 0–0/1–1 draw frequency; Dixon–Coles adjustment NOT_COMPUTED (unidentified rho), not secretly set from another league. First-half and corners are computed separately in the post-start supplement: first-half mu=1.055556, SD=1.0274, corners mu=10.28, Poisson SD=3.2062; no score-corners joint distribution was estimated.
Winner grid: home 0.414582 / draw 0.244675 / away 0.340743, sum 1.000000. No ET/draw endpoint transition. League-only baseline: DBU 160 league GF / 55 matches = 2.909091; standard total-Poisson baseline, not opponent-adjusted, n=55 games all clubs, window July–Oct 2026 prior to fixture, no same-fixture result included. Exact same line and regulation endpoint; ignores unknown score dependence and cannot represent a baseline for 1H or a verified corners operator definition. The high-level source table is mutable; no immutable per-game archive read = baseline epistemic limitation.
**Unadjusted/used model:** 1.555556/1.388889, total 2.944444; unadjusted top two Under4.5 82.45%, Over1.5 79.24%; numerical adjustments table: home venue NOT_MEASURED (0 explicit coefficient, not zero effect), bench/Colyn absence NOT_MEASURED, travel/rest NOT_MEASURED, weather NOT_MEASURED. No hidden adjustments. Scenario means change total by ±0.40 keeping team split proportional (sensitivity, not CI):

| Scenario | Total mean μ | Under4.5 | Over1.5 | Over2.5 | Interpretation |
|---|---:|---:|---:|---:|---|
| Low | 2.5444 | 88.52% | 72.17% | 46.75% | Unobserved suppression, including absent Lyngby attacker |
| Base | 2.9444 | 82.45% | 79.24% | 56.42% | Published nine-game proxy |
| High | 3.3444 | 75.45% | 84.67% | 64.94% | Weak defending / additional chances |

Model central difference is too small to claim stable ordering. Scenario width is **illustrative not calibrated**; do not use as measured uncertainty. The return does not claim a scenario-specific team xG split is supported.

#### A5. Full priced declared universe; unconditional W/P/L/V
No pushes on half-goal lines or regulation 1X2/double chances; barring abandonment, W=p, L=1−p, P=0, V=0, decisive denominator 1. The following table displays W=p and BASELINE_P on each row; L=1−W. The following primary-universe table is from the original full-time goal/result model. The separately priced first-half and corner supplied rows follow below; no exact cross-goal/corner joint is implied.

| Key | Proposition | W = p_card | BASELINE_P | Disposition |
|---|---|---:|---:|---|
| `full_total:under:0.5` | Combined total goals Under 0.5 — regulation | 5.26% | 5.45% | ELIGIBLE |
| `full_total:over:0.5` | Combined total goals Over 0.5 — regulation | 94.74% | 94.55% | EXCLUDED_CEILING |
| `full_total:under:1.5` | Combined total goals Under 1.5 — regulation | 20.76% | 21.31% | ELIGIBLE |
| `full_total:over:1.5` | Combined total goals Over 1.5 — regulation | 79.24% | 78.69% | ELIGIBLE |
| `full_total:under:2.5` | Combined total goals Under 2.5 — regulation | 43.58% | 44.39% | ELIGIBLE |
| `full_total:over:2.5` | Combined total goals Over 2.5 — regulation | 56.42% | 55.61% | ELIGIBLE |
| `full_total:under:3.5` | Combined total goals Under 3.5 — regulation | 65.97% | 66.76% | ELIGIBLE |
| `full_total:over:3.5` | Combined total goals Over 3.5 — regulation | 34.03% | 33.24% | ELIGIBLE |
| `full_total:under:4.5` | Combined total goals Under 4.5 — regulation | 82.45% | 83.03% | ELIGIBLE |
| `full_total:over:4.5` | Combined total goals Over 4.5 — regulation | 17.55% | 16.97% | ELIGIBLE |
| `full_total:under:5.5` | Combined total goals Under 5.5 — regulation | 92.16% | 92.50% | EXCLUDED_CEILING |
| `full_total:over:5.5` | Combined total goals Over 5.5 — regulation | 7.84% | 7.50% | ELIGIBLE |
| `regulation_12` | Either team wins in regulation (12; draw loses) | 75.53% | NOT_COMPUTED | ELIGIBLE |
| `regulation_1x` | Brøndby win or draw in regulation (1X) | 65.93% | NOT_COMPUTED | ELIGIBLE |
| `regulation_x2` | Lyngby win or draw in regulation (X2) | 58.54% | NOT_COMPUTED | ELIGIBLE |
| `regulation_home` | Brøndby win in regulation | 41.46% | NOT_COMPUTED | ELIGIBLE |
| `regulation_draw` | Regulation draw | 24.47% | NOT_COMPUTED | ELIGIBLE |
| `regulation_away` | Lyngby win in regulation | 34.07% | NOT_COMPUTED | ELIGIBLE |

**All six supplied contracts (full list):** The full-time Over/Under 2.5 rows are above (56.42% / 43.58%). Additional 1H/corner diagnostic rows below are from the separate post-scheduled-kickoff source supplement; not a new frozen forecast or calibration claim.

| Exact supplied contract | W | P | L | V | p_card | BASELINE_P | Treatment |
|---|---:|---:|---:|---:|---:|---|---|
| 1H combined Over 0.5 goals | 65.20% | 0 | 34.80% | 0 | 65.20% | BASELINE_UNAVAILABLE | Late phase-rate approximation, diagnostic |
| 1H combined Under 0.5 goals | 34.80% | 0 | 65.20% | 0 | 34.80% | BASELINE_UNAVAILABLE | Late phase-rate approximation, diagnostic |
| FT regulation Over 2.5 goals | 56.42% | 0 | 43.58% | 0 | 56.42% | 55.61% | Main model, unselected |
| FT regulation Under 2.5 goals | 43.58% | 0 | 56.42% | 0 | 43.58% | 44.39% | Main model, unselected |
| Regulation corners Over 10.5 | 45.19% | 0 | 54.81% | 0 | 45.19% | BASELINE_UNAVAILABLE | PROVISIONAL; exact field/dispersion not verified; not ranked |
| Regulation corners Under 10.5 | 54.81% | 0 | 45.19% | 0 | 54.81% | BASELINE_UNAVAILABLE | PROVISIONAL; exact field/dispersion not verified; not ranked |

Idealized completed-match denominators W+L=1 and no pushes on half lines. Abandonment/void/underlying operator action not verified, so zero void above is *conditional model convention*, not a certified actual operator rule. No corner full-time covariance assumption is implied; cross-family joint failure is bounded only.

**Phase-specific and independent corner model receipt:** SoccerStats [pre-fixture Danish first-half statistics](https://www.soccerstats.com/pmatch.asp?league=denmark&stats=58-4-8-2027): Brøndby first-half goals for/against 4/6 over nine, Lyngby 4/5 over nine. Hence mu1H_home=(4/9+5/9)/2=0.500000, mu1H_away=(4/9+6/9)/2=0.555556, mu1H=1.055556, P(Over0.5)=1−exp(−mu1H)=0.652001. League corroboration [WinDrawWin](https://www.windrawwin.com/statistics/half-time-over-under-05-goals/denmark-superliga/) first-half Over0.5 40/55=72.73%, but this was not substituted in the team model. [PredictVantage 2026/27 Danish team corner summary](https://predictvantage.com/leagues/denmark-superliga): Brøndby corners for/against 6.11/4.56, Lyngby 5.78/4.11 (all nine); mean corners home=(6.11+4.11)/2=5.11, away=(5.78+4.56)/2=5.17, total 10.28. Independent Poisson for corners ⇒ P(Over10.5)=1−exp(−10.28)sum_{k=0}^{10}(10.28^k/k!)=0.451946. Both sources are statistical aggregators; publication-time proof, collector independence and exact corner field are NOT_VERIFIED. The statistical snapshot explicitly concerns each club's nine matches prior to this fixture; no match outcome is adopted from the post-start retrieval.

**Supplementary sensitivity:** 1H mu 0.85–1.38 ⇒ P(1H Over0.5) 57.26%–74.84%; corners mu 8.78–11.78 ⇒ P(corners Over10.5) approximately 26.83%–62.93%; scenario only, not calibrated intervals. The original top-four are unchanged, but this new completion must not be treated as evidence they were issued before the event.

#### A6. Adjustments, regimes and unadjusted comparison
Regime NONE; international-break context not a validated regime multiplier. Soccer generic league home advantage/halftime share not transferred into this Danish model. Colyn's 4 goals in earlier league snapshot cannot be used as a mechanical -4/9 decrement since shot creation redistribution and replacement are unknown. Brøndby Ambæk first season start; lineup is confirmed but productivity adjustment not quantified. Rank order changes under high sensitivity; ADJUSTMENT_DEPENDENT for an actually applied update NO; SENSITIVITY_ORDER_UNSTABLE YES. No support for ≥0.25 SD quantitative adjustment.

#### A7. Family checks and shadow records
Soccer first-half Over0.5 at Rank1: secondary estimate 65.20% fails special p≥0.72 criterion; a verified current Danish 0–0 HT/draw-phase fit and five-point alternative gate are also missing, so it is not a Rank1. Corners gate: named provisional count source exists, but definition/dispersion and operator settlement remain unverified, therefore exclude from eligible slate. Full total line p ceiling excludes Over0.5 and Under5.5 (see A5), does not clip to 90%. Rank1/2 same total quantity, opposite tails and structurally disjoint losses (goal count cannot be ≤1 and ≥5). Ret03 gate PASS as a shadow, but primary gate RANK1_UNSTABLE; RET04=12 different signed-margin quantity, XCARD6=Over1.5 joint zero. Under4.5 vs 12 joint-losing draw is possible on 6+ goals: therefore NOT MECHANICALLY_PROTECTED for this cross-quantity shadow. Any research-only high Hit@2 is a construction statistic, not calibration.

#### A8. Sources, failures and capture/refresh plan
Field owner match scoreboard DBU 556151 for exact 90-minute final and HT if exposed. If corners are later requested for settlement, verify event-specific Opta-linked `wonCorners` per SOURCES §3.4 and whether awarded corners include unused stoppage corners; do not grade if definition unknown. Availability: field owner club team sheet known; away bench supported by structured lineup plus official 20; native stadium/time known; latest actual event state remains NOT_VERIFIED. Recheck actual kickoff, live state, source versions and data availability at settlement; manual only, no recurring scheduled capture. Main failure routes: nine-game averages, injuries/lineup response, actual issue after kickoff, unverified late phase/corner snapshot, no xG or verified detailed phase/corner archive, draw covariance not corrected. No post-start or final event evidence deliberately used.

#### A9. Integrity receipt and readback
- **Cutoff:** approximately `2026-10-12T00:57:15+11:00`; **research completion:** 2026-10-12T01:00:46+11:00; **local issue/write:** `2026-10-12T02:06:14+11:00`; originally saved source draft after scheduled kickoff; latest source supplement compiled after kickoff; **latest pre-write source view:** DBU match scheduled/blank (no independently verified actual whistle). **Status:** LATE_START_UNVERIFIED / RESEARCH_ISSUED_LOCAL_AFTER_START, no clean pregame certification; no current score or final outcome fetched for this append.
- C1 controls/version read; C2 DBU ID + local duplicate scan with canonical full-body limitation; C3 recipe/pricing ceiling; C4 Poisson W/L complements no pushes; C5 gate arithmetic; C6 joint disjoint loss=0; C7 no measured adjustment; C8 no regime extrapolation; C9 soccer play format official; C10 1H/corners supplied probabilities now recorded, but corner operator definition/dispersion and pregame source timestamp remain NOT_VERIFIED; C11 cutoff/issue ordered; C12 official sports sources only, lineage disclosure; C13 missing archive path and n=0 archived rows; C14 same-line league 55-game baseline; C15 means/SD arithmetic; C16 PASS for local append/readback only (verified after creation); global canonical duplicate/eligibility NOT_PASSED. P-580 hockey content retained verbatim; P-581 issued locally, next P-582. No claims of verified prospective skill.
**C1–C16 evidence check (local-issuance scope, not certification):**

| Check | Result | Evidence / remaining limitation |
|---|---|---|
| C1 authority | PARTIAL | v10, CR-R1, SCV-v6, SEL-v2 and soccer rules read in original research; main recheck HEAD eb1acf58; full Combined 7 body inaccessible |
| C2 identity/custody | PARTIAL | DBU fixture 556151, unique in visible local mini; P-580 already hockey, P-581 next; cannot exclude unseen canonical-body collision |
| C3 candidate universe | PASS (scoped) | 12 scored total-goal ladder sides plus 1X2/double-chance; supplemental 1H/corners separately disclosed, corner excluded |
| C4 coherent masses | PASS for assumptions | Home+away independent Poisson, sum 1, regulation draw retained; six user contracts show complementary W/L |
| C5 gate | FAIL, disclosed | Rank1 82.45%, Rank2 79.24%, 3.21-point noncomplementary lead is below 4-point requirement |
| C6 dependence/shadows | PASS diagnostic | Top-two joint loss exactly zero by disjoint total-goal losing sets; RET03/04/XCARD6 separately marked |
| C7 sensitivity | PARTIAL | Goals mu 2.5444/2.9444/3.3444; first-half and corner ranges specified; no measured adjustment coefficient |
| C8 regimes | PASS disclosure | NONE operative; travel/home/rotation effects NOT_MEASURED; no cross-league rate silently substituted |
| C9 rules/endpoint | PASS for goal model | Danish 90-minute league endpoint, draws; first-half 45+stoppage; no ET/SO assumed |
| C10 phase/auxiliary | PARTIAL | First-half model uses 4/6 and 4/5 nine-game phase counts; corners independent 10.28 mean; corner operator definition unverified |
| C11 cutoff/issue | FAIL pregame, PASS honesty | Core input cutoff ~00:57:15; original core completion 01:00:46; supplement after 01:00; local issue 02:06:14 AEDT |
| C12 sport/source lineage | PARTIAL | DBU/official club lineups and cited statistical sources; no market inputs; collector independence unverified |
| C13 archive check | PARTIAL | Danish Superliga candidate paths absent; zero results rows retrieved; exact archival coverage NOT_VERIFIED |
| C14 comparator | PARTIAL | Official league-only 160 goals/55 games supports total-goals baseline; phase/corner and winner baselines unavailable |
| C15 precision/math | PASS computation, NOT_CERTIFIED | Full Poisson point probabilities; zero covariance assumptions; low-score correction and team xG unsupported |
| C16 local write/readback | PASS local, FAIL prospective | P-580 unchanged byte-for-byte; appended one P-581; exactly one footer, highest/next P-581/P-582; not a canonical/pregame card |

SPORTS_ONLY_MARKET_BLIND: PASS · OUTCOME_EXPOSURE: NONE_OBSERVED_AS_INPUT (actual-match state NOT_VERIFIED) · SETTLEMENT: NOT_PERFORMED · CANONICAL_IMPORT: PENDING; GitHub writes: NO
<!-- END CARD P-581 -->

<!-- BEGIN CARD P-582 -->
## Card · P-582 · SOCCER / English Premier League 2026–27 · Liverpool FC vs Manchester City · 2026-10-11 (venue date)

- **Working ID:** `P-582 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT` (local-only, not GitHub canonical).
- **Event key / native ID / aliases:** `EPL:2026-27:ESPN-401879264:2026-10-11`, structured-provider ESPN game ID 401879264; exact Premier League native match ID NOT_VERIFIED; aliases Liverpool vs Manchester City, LFC–MCFC, Liverpool v Man City. Round 6 at Anfield. No earlier duplicate found in the visible local mini P-577 to P-581 and GitHub current state/status; full canonical Part 7 body retrieval unavailable, therefore global duplicate audit PARTIAL.
- **Authority:** `danisgreat/Sports-Research` `main` HEAD `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae` observed during current read; repository working differences NOT_ACCESSIBLE (remote read only); original local mini is separate working file with P-580 hockey and P-581 Danish soccer.
- **Method / controls:** MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6 / SEL-2026.10.11-v2, mini-log-6. Soccer current-rule precedence overrides old historical RM-1 rank-by-q guidance: primary order decreasing p_card.
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO` / NOT CERTIFIED. Preliminary timestamped issue; starting lineup for Liverpool not independently field-owner-confirmed, contrary reports in secondary lineups; exact soccer corner provider definition not fully harmonised. No fitted model or formal predictive skill claim.
- **Timing:** 2026-10-12 02:30 AEDT scheduled kickoff; sporting inputs are five completed league matches dated through September 20 and 2025–26 full-season baseline. **Input cutoff:** `2026-10-12T02:21:02+11:00` AEDT (last latest source fetch prior to local write, excludes user-event outcome); **research completion:** `2026-10-12T02:21:02+11:00` AEDT (local computation finished immediately before write); **local issue time:** `2026-10-12T02:21:02+11:00` AEDT; **source state/recheck:** pre-issue pages described the event as scheduled/"Not started" but no timestamped live official whistle receipt; **actual start:** NOT_VERIFIED. For a source retrieved after its original publication, page refresh alone does not verify update time. No live scores from the requested event were used.
- **Scheduled start:** Sun 11 Oct 2026 16:30 BST (UTC+01:00) = Sun 11 Oct 15:30 UTC = Mon 12 Oct 02:30 AEDT (UTC+11:00). `https://www.premierleague.com/en/news/4688862/fixture-amendments-for-premier-league-matches-in-october-and-november`, `https://www.liverpoolfc.com/news/fixture-updates-new-dates-anfield-games-against-man-city-and-arsenal`.
- **Scheduled lead / band at issue:** 8.97 minutes; BUFFERED (>5 minutes before scheduled start); actual start state NOT_VERIFIED, so **not labelled clean PREGAME**.
- **Endpoint / definition:** 90 minutes + first/second-half stoppage time; regulation draw allowed; no ET or shootout in a league fixture; goals total includes both halves. Soccer corner proposition assumes awarded match corners at ESPN/Opta `wonCorners`, including regulation stoppage time; **operator's corner action and field definition UNKNOWN_DEFINITION** until verified, hence numerical corner prices are informational not primary.
- **Distribution object:** `SOCCER_P582_INDEP_POISSON_PHASES_V1`; four independent Poisson team-by-half counts with λ(Liverpool 1H)=0.500, λ(City 1H)=0.700, λ(Liverpool 2H)=1.065, λ(City 2H)=0.981; 90-min λ home 1.565, away 1.681. Low-score Dixon–Coles ρ=0 (no verified coefficient; correction NOT_ESTIMATED, not silently applied). Diagnostic corner model independent from goals: NegBin(mean 9.950, SD 3.270, shape r=133.265); score/corners dependence NOT_COMPUTED.
- **Expected score §3a:** Liverpool 1.565, Man City 1.681, regulation total 3.246, signed Liverpool minus City −0.116 goals; SD home √1.565=1.251, away √1.681=1.297, total/margin √3.246=1.802 under zero goal covariance; first half Liverpool 0.500, Man City 0.700, combined 1.200; second half 1.065+0.981=2.046; corners 9.950 total, SD 3.270. Zero-valued observed counts are retained, missing corner team count uncertainty explicit.
- **Baseline:** BASELINE_LEAGUE_V1 frozen league-only 2025–26 EPL (n=380, all completed regular-season league fixtures before Oct 2026): Poisson total goals mean 2.75, phase Poisson mean 1.19, published 2025–26 league corners mean 10.0 SD 3.27 and empirical P(≥11 corners)=0.437; separate comparator not using team factors. Derived side/winner comparator unavailable when signed-margin orientation not established. See `BASE_RATES_REGISTER.md` §7.3; no filling a baseline after issue.
- **Regime/context:** NONE as an operative adjustment. International break and injuries (Isak, Gakpo, Foden suspension) disclosed, not assigned fabricated coefficient; Manchester City's fully documented XI and bench named; Liverpool's not independently field-owner confirmed.
- **Settlement fields / capture plan:** Premier League official match centre / ESPN ID `401879264` for 90m final score, regulation halftime score, teams/lineups, substitution/injury context; Opta-linked ESPN `wonCorners` or verified official PL corner count for total corners. Local manual capture only, no automation. Freeze exact operator rules for abandonment/partial completion before grading; target evidence within 36 h and full review within 72 h, not scheduled jobs.
- **Rules read / archive check:** `CURRENT_STATE.md`, `METHOD.md`, `CURRENT_RULES.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md` §§2–5,7, `RULES_SOCCER.md` §0/§1, `LEAGUE_RULES_SOCCER.md` §1/EPL, `PROBABILITY_TOOLKIT.md` §2, `LEAGUE_PROFILES.md` Soccer, `SOURCES.md` §3.4, `ARCHIVE_USE_GUIDE.md`, `BASE_RATES_REGISTER.md` §7.3, `research/prompts/1_GAME_CARD.md` Soccer, `research/prompts/README.md`, `GAME_LOG_STATUS_CURRENT.md`, existing active mini. **Actual archive:** `Previous Sports Results/Soccer/Premier League/{2023,2024,2025}/{year}_games.csv` fetched and scanned: 0 logical game rows each; schema-only; no admitted matches; source snapshot from publicly accessible 2026 five-game data only (all dated ≤2026-09-20) and historical n=380 league register. League profile's soccer archive status notes header-only. 2026 archive file not inspected/NOT_VERIFIED.
- **Evidence receipt:** official fixture/venue from Liverpool/PL at URLs above; club XI from `https://www.mancity.com/news/mens/liverpool-v-manchester-city-premier-league-team-news-63927317` states Donnarumma, Nunes, Dias, Guéhi, O'Reilly, Anderson, Fernández, Ndiaye, Cherki, Semenyo, Haaland; reserves Rulli, Kovačić, Doku, Reis, Gvardiol, Bouaddi, Allan, Khusanov, Lewis. Liverpool XI appears inconsistently in secondary lineup sites; NOT FIELD-OWNER CONFIRMED. Source collector independence UNKNOWN.

### Decision block
Manchester City narrowly favoured, but the explicit Liverpool absences and five-game sample create significant model uncertainty. The strongest priced propositions are broad totals and a first-half under; neither passes the provisional Rank-1 selection gate. This is a research-only local card, not assurance of a successful prediction.

| Rank | Role | Tag | Contract key / exact proposition | p_card | BASELINE_P | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | `ft:under:5.5` Full time total goals Under 5.5 (regulation) | 88.93% | 93.92% | UNCALI­BRATED_ANALYST_SCENARIO | Heavy-tailed total / lineup shock |
| 2 | PICK | ANALYST_DERIVED | `firsthalf:under:2.5` First-half combined total goals Under 2.5 (regulation) | 87.95% | 88.16% | UNCALI­BRATED_ANALYST_SCENARIO | Phase-rate / state dependency |
| 3 | INFORMATIONAL | ANALYST_DERIVED | `ft:over:1.5` Full time total goals Over 1.5 (regulation) | 83.47% | 76.03% | UNCALI­BRATED_ANALYST_SCENARIO | Other total outcome |
| 4 | INFORMATIONAL | ANALYST_DERIVED | `mancity:+1.5` Man City +1.5 goals (regulation) | 82.56% | BASELINE_UNAVAILABLE (no vetted orientation score model) | UNCALI­BRATED_ANALYST_SCENARIO | Other total outcome |

**Rank-1 gate:** RANK1_UNSTABLE: Rank1 `ft:under:5.5` 88.93%; best eligible non-complementary alternative `firsthalf:under:2.5` 87.95%; gap 0.98 percentage points, below 4.00; 62% floor met. No gate PASS claimed. Full declared supported candidate universe checked before selecting top four.
**Rank-2 floor:** PASS (87.95% ≥ 58%), conditional on simplified phase model.
**Joint failure:** exact unconditional P(FT≥6 and HT≥3)=5.18% from common 1H Pois(1.20)+2H Pois(2.046), with full-time total = HT+2H. Both decisive = 100% conditional on complete match and no operator void. Not MECHANICALLY_PROTECTED: both can fail.
**Shadows (NOT_PRIMARY):** RET03 excludes other FT-total thresholds and picks 1H Under2.5 at 87.95%, same gap/unstable; RET04 different quantity 1H Under2.5 87.95%; XCARD6 minimum-joint-failure selection FT Over1.5 83.47% with exact joint loss 0 (FT≥6 vs FT≤1) = MECHANICALLY_PROTECTED shadow only; neither shadow changes ranks.
**Adjustment dependence:** no numerical XI/home/rest/weather adjustment applied beyond team current xG data, so primary = unadjusted top two and ADJUSTMENT_DEPENDENT=NO for executed adjustment; low/base/high scenarios below reveal wide ranking/line risk. Large adjustment SD assessment NOT_COMPUTED because effects not estimated.
**Potential winner:** Liverpool regulation win 35.94%; Draw 23.20%; **Manchester City regulation win 40.86%**, so City is the plurality winner only (not >50%).
**Supplied six rows (all priced):** 1H Over0.5 69.88%, 1H Under0.5 30.12%; FT Over2.5 62.96%, FT Under2.5 37.04%; corners Over10.5 41.09%, corners Under10.5 58.91% (corners are PROVISIONAL/NOT RANK ELIGIBLE pending definition/covariance audit). No supplied row displaces frozen main four.

### Appendix
#### A1. Identity, timing and state
Liverpool FC home vs Manchester City, 2026–27 EPL MW6, Anfield. Source official Liverpool and Premier League announce 11 Oct 16:30 BST. Venue zone Europe/London BST+1; UTC+0 15:30; Australia/Melbourne AEDT+11 02:30 next date. ESPN native external ID `401879264` from `https://www.espn.com/soccer/match/_/gameId/401879264/manchester-city-liverpool` (title ordering irrelevant). Competition native match ID not retrieved. The user kickoff agrees with official schedule. Initial research sources show fixture not yet started but live official start not independently timestamped; issue cutoff, local write and last official state recheck separately disclosed. Sources reporting kickoff are not proof of actual start. Existing P-580 and P-581 have completely different native fixture identifiers; no local duplicate.

#### A2. Frozen recipe and supplied contracts
Frozen before pricing: all regulation full-time goal totals half-lines 0.5 through 5.5 in 1.0 increments; both teams' goal totals half-lines 0.5 through 3.5; signed team goal margins ±0.5, ±1.5, ±2.5; regulation 1/X/2 and double-chance 1X/X2/12; first-half total half-lines 0.5,1.5,2.5. Distinct quantity keys FT_TOTAL, FIRST_HALF_TOTAL, LIVERPOOL_TOTAL, MAN_CITY_TOTAL, SIGNED_MARGIN. All supported results priced from single four-Poisson goal state family. Supplied 1H O/U0.5, FT O/U2.5, corner O/U10.5 diagnostic included. Default ceiling >90% excluded and retained actual diagnostic p. No thresholds moved post pricing. 1H over0.5 below soccer special Rank1 >=72%; never promoted to primary Rank1. Corner counts not sourced from goal events.

#### A3. Evidence and archive read
- Liverpool official revised fixture `https://www.liverpoolfc.com/news/fixture-updates-new-dates-anfield-games-against-man-city-and-arsenal`; Premier League `https://www.premierleague.com/en/news/4688862/fixture-amendments-for-premier-league-matches-in-october-and-november`: Sun Oct 11 16:30 BST, Anfield. Publication Aug17, 2026; retrieval current research session. Lineage distinct club and field owner, not proof underlying statistical collector independence.
- Manchester City official confirmed starting XI + bench: `https://www.mancity.com/news/mens/liverpool-v-manchester-city-premier-league-team-news-63927317`; eleven players and nine reserves cited in header; Foden suspended. The City official article conflicts with some secondary lineup sources (which list Gvardiol starting), so **City club release controls**. Retrieved current research session, source publication timestamp NOT_STATED.
- Liverpool official team-sheet for this fixture NOT_RETRIEVED. Reuters `https://www.reuters.com/sports/soccer/liverpool-without-isak-gakpo-heavyweight-man-city-clash-2026-10-09/` provides absences; secondary lineup pages include inconsistent first XI/bench `https://elpais.com/deportes/resultados/futbol/inglaterra/2026_2027/directo/regular-a-6-6a38cde9456aa39/alineaciones/` and `https://en.as.com/resultados/futbol/inglaterra/2026_2027/directo/regular_a_6_6a38cde9456aa39/alineaciones/`. Do not treat projected/inconsistent lineup as confirmed. Coach-level expected-minute replacement adjustment NOT_ESTIMATED.
- Provider xG/shots: StatMuse `/fc/ask/liverpool-premier-league-xg` Liverpool five prior EPL matches xG 8.43/xGA 6.66, GF7/GA4, 76 shots/24 SOT; `/fc/ask/man-city-xg-per-shot` City xG10.15/xGA7.22, GF13/GA5, 68 shots/27 SOT, five prior games. Latest date Sept 20, 2026; publisher timestamps and provider Opta or other collector lineage UNKNOWN. Derived matchwise xG intensities reflect early-season opponents but **do not explicitly correct opponent strength**; not a validated opponent-adjusted model.
- First-half actual goals: `https://www.soccerstats.com/pmatch.asp?league=england&stats=53-18-13-2027` match-specific preview time segmentation (pre-event club season n5): Liverpool 1H GF2/5, GA2/5; City 1H GF5/5, GA3/5. Home/away n2 each is too fragile and deliberately not used as main phase split. Published origin/lineage UNKNOWN; latest matches Sept 20.
- Corners same named SoccerStats structured provider: Liverpool corners F4.00/A4.40 per match (five); City F6.20/A4.20 (five); Liverpool *home* F4.00/A6.50 (two), City *away* F6.50/A4.00 (two); values from page `## Corner statistics`, total match corners are F+A. Match corner mean conservative 50/50 blend of all-venue matchup mean [(4.00+4.20)/2+(6.20+4.40)/2]=9.40 and venue-stratified mean [(4.00+4.00)/2+(6.50+6.50)/2]=10.50 ⇒ 9.95. The 50/50 blending **is an analyst assumption**, not a fitted weight. League 2025–26 SD 3.27 from BASE_RATES_REGISTER §7.3; corner definition/independence/operator not certified.
- Archive files actually read: EPL `2023_games.csv`, `2024_games.csv`, `2025_games.csv`, all zero data rows; 2026 NOT_VERIFIED. No model fitting from these header-only files. Historical n=380 from published register separate from empty CSVs.

#### A4. Coherent distribution / arithmetic / normalization / baselines
Five-match rates: Liverpool xG/game 8.43/5=1.686, xGA/game 6.66/5=1.332; City xG/game 10.15/5=2.030, xGA/game 7.22/5=1.444. Opponent-facing arithmetic Liverpool λ=(1.686+1.444)/2=1.565; City λ=(2.030+1.332)/2=1.681. This averages offensive shot-quality proxy with opponent concession proxy; opponent-strength-of-schedule correction is NOT_MEASURED. 1H Liverpool λ=(2/5+3/5)/2=0.500; City 1H λ=(5/5+2/5)/2=0.700. 2H intensities = full λ−phase λ =1.065/0.981. Independently Poisson per side/phase, then full time = 1H+2H; 90m team-score grid P(i,j)=e^(−λh)λh^i/i! × e^(−λa)λa^j/j!; regulation 1X2 exact summation over i,j=0..23 with omitted mass below 1e−12. Half under threshold k.5 is P(HT≤k); full total same. Draw retained: Liverpool win 35.939% / draw 23.199% / City win 40.861%, sum 100% within 0.001.
Cov(home,away)=0 by independent Poisson assumption; Var(FT total)=Var(signed margin)=3.246; 1H vs FT covariance=1.200. Low-score correction rho=0; tendency for 0-0/1-1 draw excess is acknowledged but no unsupported coefficient applied. Binomial / Skellam score difference read directly from grid. **No post-start match result used**. Team means/SD/total/margin stated above.
League-only frozen comparator: EPL 2025–26 `BASE_RATES_REGISTER.md` §7.3 season n380; 90m total Poisson λ=2.75 for unsupplied thresholds: P(FT Under5.5)=93.92%, P(FT Over1.5)=76.03%; 1H Poisson mean1.19: P(1H Under2.5)=88.16%. For **supplied** FT Over2.5 source empirical 2025–26 p=55.0% of n380 (whole-season distribution), first-half Over0.5 empirical 71.6% of n380, and corners Over10.5 empirical 43.7% of n380: these are separate **descriptive frequency checks**, not substituted into the frozen Poisson league-only comparator. The frozen same-line Poisson p for FT Over2.5=51.85% / 1H Over0.5=69.58%.
Corner distribution independent of goals (joint cross-family unknown): NegBin with mean 9.95 and SD3.27, shape r=μ²/(SD²−μ)=133.265; P(C=k)=Gamma(k+r)/(Gamma(r)k!) (r/(r+μ))^r (μ/(r+μ))^k; tail from k≥11 gives over10.5=41.09%, under10.5=58.91%; omitted tail k>27 below nominal rounding tolerance (base sums to >99.9% with high r). 90min corners include stoppage; operator's awarded corner definition must be confirmed. No goals-corners covariance inferred.

#### A5. Declared priced candidate universe — W/P/L/V
All half-goal contracts and 1X2 settled over a complete 90m match: unconditional W=p, P=0, L=1−p, V=0; p_card=W/(W+L) with denominator 1.000. Conditional issue void convention does not assert an operator-specific abandoned-match rule. No unsupported row is silently filled or clipped to .90. The table contains *all* goal-world candidate keys; corners separate below. FIRST_HALF entries use coherent phase marginals, not unadjusted generic league 43% constant.

| Key | Exact proposition | W | PUSH | L | VOID | p_card | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| `firsthalf:over:0.5` | First-half combined total goals Over 0.5 | 69.88% | 0% | 30.12% | 0% | 69.88% | ELIGIBLE |
| `firsthalf:over:1.5` | First-half combined total goals Over 1.5 | 33.74% | 0% | 66.26% | 0% | 33.74% | ELIGIBLE |
| `firsthalf:over:2.5` | First-half combined total goals Over 2.5 | 12.05% | 0% | 87.95% | 0% | 12.05% | ELIGIBLE |
| `firsthalf:under:0.5` | First-half combined total goals Under 0.5 | 30.12% | 0% | 69.88% | 0% | 30.12% | ELIGIBLE |
| `firsthalf:under:1.5` | First-half combined total goals Under 1.5 | 66.26% | 0% | 33.74% | 0% | 66.26% | ELIGIBLE |
| `firsthalf:under:2.5` | First-half combined total goals Under 2.5 | 87.95% | 0% | 12.05% | 0% | 87.95% | ELIGIBLE |
| `ft:over:0.5` | Full time total goals Over 0.5 | 96.11% | 0% | 3.89% | 0% | 96.11% | EXCLUDED_CEILING (>90%) |
| `ft:over:1.5` | Full time total goals Over 1.5 | 83.47% | 0% | 16.53% | 0% | 83.47% | ELIGIBLE |
| `ft:over:2.5` | Full time total goals Over 2.5 | 62.96% | 0% | 37.04% | 0% | 62.96% | ELIGIBLE |
| `ft:over:3.5` | Full time total goals Over 3.5 | 40.77% | 0% | 59.23% | 0% | 40.77% | ELIGIBLE |
| `ft:over:4.5` | Full time total goals Over 4.5 | 22.76% | 0% | 77.24% | 0% | 22.76% | ELIGIBLE |
| `ft:over:5.5` | Full time total goals Over 5.5 | 11.07% | 0% | 88.93% | 0% | 11.07% | ELIGIBLE |
| `ft:under:0.5` | Full time total goals Under 0.5 | 3.89% | 0% | 96.11% | 0% | 3.89% | ELIGIBLE |
| `ft:under:1.5` | Full time total goals Under 1.5 | 16.53% | 0% | 83.47% | 0% | 16.53% | ELIGIBLE |
| `ft:under:2.5` | Full time total goals Under 2.5 | 37.04% | 0% | 62.96% | 0% | 37.04% | ELIGIBLE |
| `ft:under:3.5` | Full time total goals Under 3.5 | 59.23% | 0% | 40.77% | 0% | 59.23% | ELIGIBLE |
| `ft:under:4.5` | Full time total goals Under 4.5 | 77.24% | 0% | 22.76% | 0% | 77.24% | ELIGIBLE |
| `ft:under:5.5` | Full time total goals Under 5.5 | 88.93% | 0% | 11.07% | 0% | 88.93% | ELIGIBLE |
| `liverpool:+0.5` | Liverpool +0.5 goals | 59.14% | 0% | 40.86% | 0% | 59.14% | ELIGIBLE |
| `liverpool:+1.5` | Liverpool +1.5 goals | 79.01% | 0% | 20.99% | 0% | 79.01% | ELIGIBLE |
| `liverpool:+2.5` | Liverpool +2.5 goals | 91.23% | 0% | 8.77% | 0% | 91.23% | EXCLUDED_CEILING (>90%) |
| `liverpool:-0.5` | Liverpool -0.5 goals | 35.94% | 0% | 64.06% | 0% | 35.94% | ELIGIBLE |
| `liverpool:-1.5` | Liverpool -1.5 goals | 17.44% | 0% | 82.56% | 0% | 17.44% | ELIGIBLE |
| `liverpool:-2.5` | Liverpool -2.5 goals | 6.85% | 0% | 93.15% | 0% | 6.85% | ELIGIBLE |
| `liverpool:over:0.5` | Liverpool total goals Over 0.5 | 79.09% | 0% | 20.91% | 0% | 79.09% | ELIGIBLE |
| `liverpool:over:1.5` | Liverpool total goals Over 1.5 | 46.37% | 0% | 53.63% | 0% | 46.37% | ELIGIBLE |
| `liverpool:over:2.5` | Liverpool total goals Over 2.5 | 20.76% | 0% | 79.24% | 0% | 20.76% | ELIGIBLE |
| `liverpool:over:3.5` | Liverpool total goals Over 3.5 | 7.41% | 0% | 92.59% | 0% | 7.41% | ELIGIBLE |
| `liverpool:under:0.5` | Liverpool total goals Under 0.5 | 20.91% | 0% | 79.09% | 0% | 20.91% | ELIGIBLE |
| `liverpool:under:1.5` | Liverpool total goals Under 1.5 | 53.63% | 0% | 46.37% | 0% | 53.63% | ELIGIBLE |
| `liverpool:under:2.5` | Liverpool total goals Under 2.5 | 79.24% | 0% | 20.76% | 0% | 79.24% | ELIGIBLE |
| `liverpool:under:3.5` | Liverpool total goals Under 3.5 | 92.59% | 0% | 7.41% | 0% | 92.59% | EXCLUDED_CEILING (>90%) |
| `mancity:+0.5` | Man City +0.5 goals | 64.06% | 0% | 35.94% | 0% | 64.06% | ELIGIBLE |
| `mancity:+1.5` | Man City +1.5 goals | 82.56% | 0% | 17.44% | 0% | 82.56% | ELIGIBLE |
| `mancity:+2.5` | Man City +2.5 goals | 93.15% | 0% | 6.85% | 0% | 93.15% | EXCLUDED_CEILING (>90%) |
| `mancity:-0.5` | Man City -0.5 goals | 40.86% | 0% | 59.14% | 0% | 40.86% | ELIGIBLE |
| `mancity:-1.5` | Man City -1.5 goals | 20.99% | 0% | 79.01% | 0% | 20.99% | ELIGIBLE |
| `mancity:-2.5` | Man City -2.5 goals | 8.77% | 0% | 91.23% | 0% | 8.77% | ELIGIBLE |
| `mancity:over:0.5` | Man City total goals Over 0.5 | 81.38% | 0% | 18.62% | 0% | 81.38% | ELIGIBLE |
| `mancity:over:1.5` | Man City total goals Over 1.5 | 50.08% | 0% | 49.92% | 0% | 50.08% | ELIGIBLE |
| `mancity:over:2.5` | Man City total goals Over 2.5 | 23.78% | 0% | 76.22% | 0% | 23.78% | ELIGIBLE |
| `mancity:over:3.5` | Man City total goals Over 3.5 | 9.04% | 0% | 90.96% | 0% | 9.04% | ELIGIBLE |
| `mancity:under:0.5` | Man City total goals Under 0.5 | 18.62% | 0% | 81.38% | 0% | 18.62% | ELIGIBLE |
| `mancity:under:1.5` | Man City total goals Under 1.5 | 49.92% | 0% | 50.08% | 0% | 49.92% | ELIGIBLE |
| `mancity:under:2.5` | Man City total goals Under 2.5 | 76.22% | 0% | 23.78% | 0% | 76.22% | ELIGIBLE |
| `mancity:under:3.5` | Man City total goals Under 3.5 | 90.96% | 0% | 9.04% | 0% | 90.96% | EXCLUDED_CEILING (>90%) |
| `margin:1` | Liverpool regulation win | 35.94% | 0% | 64.06% | 0% | 35.94% | ELIGIBLE |
| `margin:12` | Either team wins in regulation | 76.80% | 0% | 23.20% | 0% | 76.80% | ELIGIBLE |
| `margin:1X` | Liverpool or draw | 59.14% | 0% | 40.86% | 0% | 59.14% | ELIGIBLE |
| `margin:2` | Man City regulation win | 40.86% | 0% | 59.14% | 0% | 40.86% | ELIGIBLE |
| `margin:X` | Regulation draw | 23.20% | 0% | 76.80% | 0% | 23.20% | ELIGIBLE |
| `margin:X2` | Man City or draw | 64.06% | 0% | 35.94% | 0% | 64.06% | ELIGIBLE |

**Six supplied contracts with baseline/action receipt:**

| Supplied proposition (contract metadata) | W | P | L | V | p_card | BASELINE_LEAGUE_V1 | Status |
|---|---:|---:|---:|---:|---:|---|---|
| First half combined goals Over0.5 | 69.88% | 0% | 30.12% | 0% | 69.88% | 69.58% | Numeric, uncalibrated; Rank1 phase special gate fails |
| First half combined goals Under0.5 | 30.12% | 0% | 69.88% | 0% | 30.12% | 30.42% | Numeric, uncalibrated |
| Full-time combined goals Over2.5 | 62.96% | 0% | 37.04% | 0% | 62.96% | 51.85% | Numeric, uncalibrated |
| Full-time combined goals Under2.5 | 37.04% | 0% | 62.96% | 0% | 37.04% | 48.15% | Numeric, uncalibrated |
| Match combined corners Over10.5 | 41.09% | 0% | 58.91% | 0% | 41.09% | 43.70% historical empirical | PROVISIONAL, named structured provider, definition/dispersion unvalidated |
| Match combined corners Under10.5 | 58.91% | 0% | 41.09% | 0% | 58.91% | 56.30% historical empirical | PROVISIONAL, not rank eligible |

#### A6. Adjustments, regime and sensitivity
| Factor | Initial estimate | Applied numerical change | Basis / limitations |
|---|---|---|---|
| Home Anfield | Existing 5-match home/away blended team strengths | 0 additional goals | Small 5-match cohort lacks stable separate coefficient; home advantage NOT_MEASURED |
| Liverpool absences Isak/Gakpo; lineup | 1.565 Liverpool goals baseline from all five games | 0 applied; possible -0.25 shown scenario | Both attacks absent by Reuters; replacement and xG redistribution unknown; do not double subtract measured 5-game xG |
| City XI and keeper | Donnarumma and Haaland officially XI | 0 applied | Historical shot quality includes some different participants; substitution minute value unknown |
| Rest/travel/weather | Post-international-break context | 0 applied | No measured/weather-specific multiplier. WEATHER_NOT_VERIFIED; rest travel qualitative only |

**Unadjusted pair:** FT Under5.5 (88.93%) and 1H Under2.5 (87.95%). SENSITIVITY range based only on independently declared ±0.25 Liverpool/City 90m goals; half-rate scaled proportionally to team's phase/whole mean. This is a *model stress test*, not a statistical confidence interval. No observed match results are imported into sensitivity.

| Scenario | λ Liverpool | λ City | λ first half | FT Under5.5 | 1H Under2.5 | FT Over2.5 |
|---|---:|---:|---:|---:|---:|---:|
| Liverpool attack lower (illustrative) | 1.315 | 1.681 | 1.120 | 91.65% | 89.63% | 57.59% |
| Base recorded | 1.565 | 1.681 | 1.200 | 88.93% | 87.95% | 62.96% |
| City attack higher (illustrative) | 1.565 | 1.931 | 1.304 | 85.81% | 85.62% | 67.84% |
| City attack lower (illustrative) | 1.565 | 1.431 | 1.096 | 91.65% | 90.12% | 57.59% |
| Liverpool attack higher (illustrative) | 1.815 | 1.681 | 1.280 | 85.81% | 86.17% | 67.84% |


Ranking among different families may shift under larger joint changes; unestimated lineup effects and xG opponent-strength translation prevent a robust ranking guarantee. If a new adjustment changes original top-two, label its new dated version `ADJUSTMENT_DEPENDENT / NOT_PRIMARY`, no silent changes.

#### A7. Rank/family gates, shadows, joint and issues
Original rank gate FAIL: p 88.93%, next-best non-complementary eligible 1H Under2.5 87.95%, gap 0.98pp <4; selection ceiling excludes goal-world rows >90% without p clipping. Rank2 87.95% >58. Soccer 1H Over0.5 has p69.88% <72% and no five-point lead, cannot rank1. Team handicap signed distributions correct from grid; 1X and X2 are double chances and share signed margin quantity. RET03 gate still fails with differing quantity. RET04 = 1H Under2.5 87.95%; XCARD6 = FT Over1.5 83.47%, zero joint failure with FT Under5.5 as it is impossible to have FT≤1 and FT≥6 simultaneously, but this is MECHANICALLY_PROTECTED and not skill evidence. Original top-two exact joint failure 5.184% from common 1H/2H sum; no independence multiplication. Mixed corners/goals dependence NOT_ESTIMATED, bounds rather than fake exact joint.

#### A8. Capture plan, provenance and failure routes
Provider priority for settlement Premier League official / ESPN game 401879264; exact HT 45'+ stoppage score, regulation final, team XI and substitution evidence; for corners ESPN Opta `wonCorners` both club totals, confirm provider definition vs user contract before grading. Capture manually near match and within 36h, full retrospective target 72h. No automation has been created; timelines are requested follow-up plans, not running jobs. Unavailable/missing: EPL native match ID, Liverpool official starting XI, keeper substitutions/bench conflict, calibrated low-score rho, injury impact coefficient, fixture-specific weather/rest adjustment, corner goal-state dependence, 2026 PL raw archive and exact 2026 phase provider timestamps. Sporting provider xG/shot statistics and SoccerStats likely sourced from shared collectors, hence independence UNKNOWN. Material failure routes: small-sample xG/defence, missing attackers, first-half rate swing, 6+ goal tail, corners overdispersion and red card. No odds/markets/tips used.

#### A9. Integrity audit (C1–C16)
| Check | Result / evidence |
|---|---|
| C1 | PARTIAL: required control paths and this Soccer prompt opened from GitHub main at HEAD `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae`; not all long control full text streamed; local original mini read completely; source read time separate |
| C2 | PARTIAL: Liverpool v Man City fixture verified PL/LFC, ESPN id 401879264; no matching local key P-577..P-581 or status register entry; combined canonical Part7 original body fetch inaccessible, no certified global duplicate proof |
| C3 | PASS scoped: frozen supported quantity/families/lines and deterministic descending-p top4; 90% ceiling; six supplied rows diagnosed |
| C4 | PASS model arithmetic: 4-Poisson independent phases derive coherent 1H/90m; result masses sum 1; W/P/L/V and p denominator=1 |
| C5 | FAIL gate disclosed: 88.93 vs 87.95, gap0.98pp below 4; RET03 separate |
| C6 | PASS model diagnostic: first two exact shared-state joint loss 5.18%; shadows not promoted; phase threshold has no push |
| C7 | PARTIAL: five-match coefficients unadjusted; sensitivity scenarios; no unsupported injury ±0.25 called measured |
| C8 | PASS disclosure: operative regime NONE; no transferred automatic cup/home multiplier |
| C9 | PASS competition 90m+stoppage league draw; no ET/SO; venue time correctly converted |
| C10 | PARTIAL: 1H own five-match rates; corners named provider and distinct NB count, but exact operator definition and joint covariance unverified; corners not primary eligible |
| C11 | PARTIAL: match not proven started at cutoff, no actual whistle receipt; source-last-finished <=Sept20; source fetch/issue timestamps; issue may be buffered but no certified clean PREGAME state |
| C12 | PARTIAL: URLs, exact source fields, publication if available, retrieval day in this session; no audit that domains independently collect source data |
| C13 | PASS limited inspection: EPL 2023, 2024, 2025 archived CSVs actually fetched, 0 data rows each; 2026 archive not available to this inspection |
| C14 | PASS league-only comparator on top goal/phase rows with distinct source, signed-margin UNAVAILABLE; 2025-26 empirical diagnostics are not backfilled baseline |
| C15 | PASS numerical normalization grid+phase, expected team/total/margin, NB corner model and scenario values; low-score adjustment not fitted |
| C16 | Local-only file write/readback expected at completion; global canonical duplicate audit and clean official XI gate remain PARTIAL; prospective certification NOT_PASSED |

SPORTS_ONLY_MARKET_BLIND: PASS · OUTCOME_EXPOSURE: NONE USED; ACTUAL_START_NOT_VERIFIED · SETTLEMENT: NOT_PERFORMED · CANONICAL_IMPORT: PENDING · GitHub writes: NO
<!-- END CARD P-582 -->

<!-- BEGIN ADDENDUM P-582 20261012T022342+1100 -->
### Addendum · P-582 · 2026-10-12T02:23:42+11:00 · official starting XIs and benches located after original issue

- **Parent / status:** P-582 LOCAL_WORKING_ID / PENDING_CANONICAL_IMPORT; source-verification-only addendum, **NOT_PRIMARY**, not a replacement card or prospective reforecast.
- **Original card freeze:** Original P-582 card was locally issued at 2026-10-12T02:21:02+11:00. Its predicted probabilities, ranks, model, baseline, cutoff and timing labels remain unchanged.
- **Publication and retrieval:** Manchester City official matchday lineup article at https://www.mancity.com/news/mens/liverpool-v-manchester-city-premier-league-team-news-63927317 ; original article publication timestamp not displayed in retrieved text; this exact XI/bench evidence fetched and read **2026-10-12T02:23:42+11:00**, after the issue. The article's prior availability at original cutoff is **NOT_VERIFIED**, so no retrospective pre-cutoff receipt is claimed. Provider/collector = official Man City FC club communication, collector independence UNKNOWN.
- **Confirmed Liverpool XI:** Alisson; Araujo, Jacquet, van Dijk, Kerkez, Gravenberch, Mac Allister, Munoz, Wirtz, Barcola, Koumas.
- **Liverpool substitutes:** Mamardashvili, Gomez, Endo, Chiesa, Tsimikas, Frimpong, Nyoni, McConnell, Ngumoha.
- **Confirmed Manchester City XI:** Donnarumma; Nunes, Dias (captain), Guéhi, O'Reilly, Anderson, Fernández, Ndiaye, Cherki, Semenyo, Haaland.
- **Manchester City substitutes:** Rulli, Kovačić, Doku, Reis, Gvardiol, Bouaddi, Allan, Khusanov, Lewis.
- **Evidence/status correction:** The original A8 statement that Liverpool's official XI was unavailable is now superseded **as of this addendum retrieval only**. Both named club-sheet starting goalkeepers and both substitutes lists are verified in this official club source. This does not prove how long before issuance the XI was publicly available, whether substitutions occur, or actual-match-start state.
- **Implications:** No lineup-driven quantified adjustment is fitted; nothing is silently edited in the primary distribution, initial top two, or original supplied-contract estimates. The uncalibrated/partial-v10 audit and rank gate remain unchanged. No outcome or settlement data consumed.
- **Capture:** Confirm actual kickoff and final phase/corner statistics later from PL or event field owner; no job is scheduled. **SETTLEMENT NOT_PERFORMED; GitHub writes NO.**
<!-- END ADDENDUM P-582 20261012T022342+1100 -->

<!-- BEGIN CARD P-583 -->
## Card · P-583 · BASEBALL / Korea KBO 2026 regular season · KT Wiz @ Samsung Lions · 2026-10-12

- **Working ID:** `P-583 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`. One local event card; never a canonical assignment.
- **Event key / native ID / aliases:** `KBO:2026:REGULAR:20261012KTSS0`; published KBO Game Center game ID `20261012KTSS0`; KT (away) at Samsung (home), Daegu; distinct from 2026-10-07 and 2026-10-11 matchups. Duplicate check local original P-580–P-582 and carryovers P-577–P-579: no identity match. Full large Combined Log body / parallel local writers NOT_VERIFIED.
- **Authority:** GitHub `danisgreat/Sports-Research` `main`, last recent commit observed `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae` (latest commit search, branch-ref equality not independently confirmed). MDS-2026.10.11-v10.0; CR-2026.10.11-R1; SCV-2026.10.11-v6; SEL-2026.10.11-v2 P_ORDER_V2; local FR-5/10/15/20 supplement, not published. Other machine writes NOT_VERIFIED.
- **Analysis status:** `NO_FORECAST / PREMATCH_RESEARCH_ONLY / UNCALIBRATED_QUALITATIVE / RESEARCH_ONLY_NOT_CERTIFIED`. No numerical ranked picks issued because the user-required official batting-order/available-bench gate was **UNCONFIRMED**. Named starting pitchers are confirmed, not the complete playing orders. Numerical league averages and historical empirical percentages below are *descriptive*, not `p_card`.
- **Timing:** Officially scheduled first pitch 2026-10-12T18:30:00+09:00 KST = 2026-10-12T20:30:00+11:00 AEDT = 2026-10-12T09:30:00Z. Data research and web retrieval during 2026-10-12T20:22–20:26 AEDT; card construction/issue at `2026-10-12T20:29:24+11:00`. Official Game Center displayed `scheduled` and empty target scoreboard during research; **actual first pitch NOT_VERIFIED**. No live outcome was used. Source last-updated times generally unavailable.
- **Scheduled start:** Daegu Samsung Lions Park; KBO official schedule/game center, KST and AEDT above. No end-time inference.
- **Scheduled lead / band:** Calculated from issue at `2026-10-12T20:29:24+11:00` relative to official scheduled 20:30 AEDT. Timing label `PREGAME_SCHEDULED / ACTUAL_START_NOT_VERIFIED` if issue precedes 20:30, else `LATE_START_UNVERIFIED`; avoid claiming independently verified pre-first-pitch status.
- **Endpoint / definition:** Original contracts are full-game KT −1.5, Samsung +1.5, combined Over 11.5. KBO regulation typically nine innings with tie permitted after league extra-innings cap; precise shortened-game/operator terms not provided. 11+ inning example 2026-10-04 KT–Lotte 2–2 Final/11; user/operator action on suspended/cancelled games UNKNOWN. All three distinct lines are half-integer, so no exact-score PUSH under completed full-game sporting arithmetic. Winner family must retain possible tie.
- **Distribution object:** `NOT_COMPUTED` — starter/bullpen availability integration, exact official batting orders and defensible KBO extras mixture unavailable. `p_card=NOT_ESTIMATED`; no numerical selection/gate or generated universe.
- **Expected score:** Team runs, combined runs, signed KT−Samsung margin and SDs: `NOT_COMPUTED`. Historical KBO prior is not a supported current fixture forecast.
- **Baseline:** `BASELINE_UNAVAILABLE_ON_FROZEN_LINES`: league profile 2023–25 n=2182 means home 4.88, away 4.89, combined 9.77, total SD 4.93, margin SD 4.79. KBO extras share withdrawn as NOT_ESTIMABLE (2026-10-11 source audit). No discrete exact-line, extras-aware frozen `BASELINE_LEAGUE_V1` estimate obtained. The profile figures are descriptive priors, not a same-line score.
- **Regime flags / context:** NONE; KT first in table (89–49–5), Samsung second (83–57–3); late-regular-season personnel/rest motivation remains a qualitative uncertainty. Daegu venue, forecast mild/cloudy from MyKBO; no measured weather adjustment.
- **Settlement fields / capture plan:** KBO Game Center final score KT and Samsung, game status/innings (official), away+home total, signed margin, any tie/extras; operator settlement rules must be provided independently. Official page checked before event; recheck at/after verified final through KBO Game Center and KBO scoreboard; retry if stale (SOURCES official route, 12 h where applicable), `NOT_SCHEDULED` as no automation exists. No settlement here.
- **Rules read / archive check:** Current GitHub `main`: CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_BASEBALL §0, LEAGUE_PROFILES KBO, PROBABILITY_TOOLKIT, ARCHIVE_USE_GUIDE, 1_GAME_CARD plus local FR supplement. Full giant SOURCES/full canonical Combined Log body / full `GAME_LOG_STATUS_CURRENT` not re-read end-to-end in this operation; those gates PARTIAL/NOT_VERIFIED. Queried `Previous Sports Results/Baseball/KBO/2026/2026_games.csv` on `main`: **NOT_FOUND**. Historical archive league 2023–25 profile used only as prior; latest 20 participant finals traced from KBO official October results and MyKBO dated September/October schedule pages (see A3); 20/20 per team in same competition, no forecast-game data, no canceled games included. KBO profile extras and innings placeholders never treated as measured.
- **Evidence receipt:** KBO official `https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx?gameDate=20261012&gameId=20261012KTSS0&section=START_PIT` : KT So Hyeong-jun, Samsung Yang Chang-seop, 18:30 KST Daegu, scheduled; So season 9–3, ERA 3.23, WHIP 1.24, 22 games, 13 QS; Yang 8–2, ERA 5.01, WHIP 1.51, 28 games, 4 QS. MyKBO event `https://mykbostats.com/games/14037-KT-vs-Samsung-20261012` corroborates starters and standings. Nonofficial `https://yakuku-yaru.today/games/59155` explicitly displays *projected* batting lineup, not official lineup — **cannot pass lineup gate**; official batting order and active roster for today's event NOT_VERIFIED. All source independent-lineage status UNKNOWN.

### Decision block
**Qualitative direction only: KT has materially better last-5/10/20 form and the lower-ERA confirmed starter, but official batting orders/active bench remain unconfirmed and the totals/run-line distribution is uncomputed. Therefore NO numerical top-two picks or winner probability is issued.** This is not a claim that KT −1.5 is more probable than Samsung +1.5 or that Over 11.5 has a modeled p.

| Rank | Role | Tag | Contract key / exact proposition | p_card | BASELINE_P | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|
| — | NO_RANKED_ROWS | NO_FORECAST | No supported numerical primary selections | NOT_ESTIMATED | BASELINE_UNAVAILABLE | LINEUP_GATE_UNCONFIRMED + MODEL_NOT_COMPUTED | Late-season changes, unconfirmed roster/bench, high score variance |

**Rank-1 gate:** NOT_ASSESSABLE, no Rank 1. **Rank-2 floor:** NOT_ASSESSABLE. **Joint failure:** NOT_COMPUTED; for user-supplied KT−1.5 vs Samsung+1.5, the sporting win/loss sets are complementary on completed scores, so a pair of both is MECHANICALLY_PROTECTED against both losing, but there is **no** modeled joint mass or primary selection. **Shadow gate / Rank 2:** NOT_ISSUED. **Adjustment dependence:** NOT_COMPUTED; FORM_WINDOW_SENSITIVE=NOT_COMPUTABLE (no numeric model). **Potential winner:** qualitative KT lean; `KT/Wiz p=NOT_ESTIMATED`, `Samsung p=NOT_ESTIMATED`, `TIE p=NOT_ESTIMATED`; all winner masses unavailable.
**Supplied rows not selected:** KT Wiz −1.5 (NOT_ESTIMATED); Samsung Lions +1.5 (NOT_ESTIMATED); Combined Total Runs Over 11.5 (NOT_ESTIMATED); the fourth input repeats exactly the same Over 11.5 contract and is marked **DUPLICATE_REFERENCE — NO NEW CANDIDATE**.

### Appendix
#### A1. Identity, timing and state
- Native ID `20261012KTSS0`, KBO 2026 regular season, away KT vs home Samsung, 12 Oct 18:30 KST (20:30 AEDT). Historical series game 2026-10-11 ended KT 12/Samsung 3 and is explicitly a DIFFERENT event; no post-cutoff event result imported.
- Official source during 20:22–20:26 AEDT research displayed `경기예정` / Scheduled; first pitch and official full lineup unknown. The model cutoff is the research-period source-read bound, not a fabricated millisecond timestamp. Actual issue is `2026-10-12T20:29:24+11:00`.
- Prior local mini owner P-580–P-582 remains unchanged; working P-583 only locally and pending import.

#### A2. Frozen supplied contracts and candidate recipe
1. `Wiz -1.5` — exact provided line, interpret KT winning by at least two runs after full-game action.
2. `Lions +1.5` — exact provided line, interpret Samsung winning, tying, or losing by no more than one run after full-game action.
3. `Combined Total Runs: Over 11.5 Runs` — 12+ total runs on the exact full-game sporting score.
4. `Combined Total Runs: Over 11.5 Runs` — identical repeated input: deduplicated for selection but preserved literally here.
- All three unique lines are research propositions, not privileged picks. Price recipe STOPPED by FR5 lineup gate; no unsupported expansion, clipping, ordering or probabilities.

#### A3. Evidence and archive inputs — FR-5/10/15/20
- Cohort: last 20 chronologically most recent *completed* KBO regular-season fixtures per team available before 12 Oct 18:30 KST, including tie results as draws, excluding the target event and canceled games. Sources: KBO official scoreboard October and MyKBO dated records September/October. Date-only pre-12-Oct entries are on *earlier dates*, avoiding same-day completion leakage. Multiple competitions not pooled. Historical 2026 GitHub KBO CSV NOT_FOUND; alternative structured data explicitly disclosed. Actual provider source publication/update times often not displayed; current retrieval 2026-10-12 20:22–20:26 AEDT; lineage UNKNOWN. All stats are full-game scores with 11th-inning ties when present; do not treat all listed games as nine-inning regulation totals.

**KT Wiz form — 20/20 eligible** (H/A relative to team; Over11.5 frequency is historical, *not* the forecast's `p_card`):

| Window | Available n | W–D–L | Runs scored/game | Allowed/game | Run differential/game | Venue composition | Historical total >11.5 | Opponent quality |
|---|---:|---|---:|---:|---:|---|---:|---|
| Last 5 | 5/5 | 4–1–0 | 8.40 | 1.80 | +6.60 | 3 home / 2 away | 2/5 (40%) | MyKBO dated finals; opponent rating unavailable |
| Last 10 | 10/10 | 9–1–0 | 7.70 | 2.70 | +5.00 | 4 home / 6 away | 5/10 (50%) | MyKBO dated finals; opponent rating unavailable |
| Last 15 | 15/15 | 12–1–2 | 6.73 | 3.93 | +2.80 | 9 home / 6 away | 7/15 (47%) | MyKBO dated finals; opponent rating unavailable |
| Last 20 | 20/20 | 15–2–3 | 6.95 | 4.15 | +2.80 | 12 home / 8 away | 10/20 (50%) | MyKBO dated finals; opponent rating unavailable |

**Samsung Lions form — 20/20 eligible**:

| Window | Available n | W–D–L | Runs scored/game | Allowed/game | Run differential/game | Venue composition | Historical total >11.5 | Opponent quality |
|---|---:|---|---:|---:|---:|---|---:|---|
| Last 5 | 5/5 | 1–0–4 | 3.40 | 7.00 | -3.60 | 2 home / 3 away | 3/5 (60%) | MyKBO dated finals; opponent rating unavailable |
| Last 10 | 10/10 | 5–0–5 | 4.20 | 6.00 | -1.80 | 7 home / 3 away | 5/10 (50%) | MyKBO dated finals; opponent rating unavailable |
| Last 15 | 15/15 | 8–0–7 | 4.93 | 6.07 | -1.13 | 8 home / 7 away | 8/15 (53%) | MyKBO dated finals; opponent rating unavailable |
| Last 20 | 20/20 | 10–0–10 | 4.80 | 5.90 | -1.10 | 12 home / 8 away | 9/20 (45%) | MyKBO dated finals; opponent rating unavailable |

**Non-overlapping blocks** (games 1–5 most recent; separate descriptives, no double counting):

| Team / games | Runs for/game | Runs against/game | W–D–L |
|---|---:|---:|---|
| KT 1–5 | 8.40 | 1.80 | 4–1–0 |
| KT 6–10 | 7.00 | 3.60 | 5–0–0 |
| KT 11–15 | 4.80 | 6.40 | 3–0–2 |
| KT 16–20 | 7.60 | 4.80 | 3–1–1 |
| Samsung 1–5 | 3.40 | 7.00 | 1–0–4 |
| Samsung 6–10 | 5.00 | 5.00 | 4–0–1 |
| Samsung 11–15 | 6.40 | 6.20 | 3–0–2 |
| Samsung 16–20 | 4.40 | 5.40 | 2–0–3 |

**KT event-level trace** (1=most recent, full-game runs, 2026; primary source indexed by weeks below):

| # | Date | Opponent | H/A | Score KT–opponent | W/D/L |
|---|---|---|---|---|---|
| 1 | 2026-10-11 | Samsung | A | 12–3 | W |
| 2 | 2026-10-07 | Samsung | H | 9–3 | W |
| 3 | 2026-10-06 | Kiwoom | A | 10–1 | W |
| 4 | 2026-10-05 | Lotte | H | 9–0 | W |
| 5 | 2026-10-04 | Lotte | H | 2–2 | D |
| 6 | 2026-10-03 | Lotte | H | 5–0 | W |
| 7 | 2026-10-01 | KIA | A | 7–5 | W |
| 8 | 2026-09-30 | KIA | A | 3–2 | W |
| 9 | 2026-09-29 | KIA | A | 8–5 | W |
| 10 | 2026-09-27 | Doosan | A | 12–6 | W |
| 11 | 2026-09-26 | Kiwoom | H | 1–10 | L |
| 12 | 2026-09-24 | NC | H | 3–2 | W |
| 13 | 2026-09-23 | NC | H | 3–10 | L |
| 14 | 2026-09-22 | SSG | H | 8–2 | W |
| 15 | 2026-09-20 | Doosan | H | 9–8 | W |
| 16 | 2026-09-19 | Doosan | H | 15–3 | W |
| 17 | 2026-09-18 | LG | H | 1–12 | L |
| 18 | 2026-09-16 | Hanwha | A | 4–4 | D |
| 19 | 2026-09-15 | Hanwha | A | 13–3 | W |
| 20 | 2026-09-13 | Lotte | H | 5–2 | W |

**Samsung event-level trace** (full-game runs):

| # | Date | Opponent | H/A | Score Samsung–opponent | W/D/L |
|---|---|---|---|---|---|
| 1 | 2026-10-11 | KT | H | 3–12 | L |
| 2 | 2026-10-09 | SSG | A | 1–3 | L |
| 3 | 2026-10-07 | KT | A | 3–9 | L |
| 4 | 2026-10-06 | KIA | A | 5–4 | W |
| 5 | 2026-10-05 | Doosan | H | 5–7 | L |
| 6 | 2026-10-04 | Doosan | H | 0–12 | L |
| 7 | 2026-10-03 | Doosan | H | 6–4 | W |
| 8 | 2026-10-01 | Hanwha | H | 3–2 | W |
| 9 | 2026-09-30 | Hanwha | H | 6–2 | W |
| 10 | 2026-09-29 | Hanwha | H | 10–5 | W |
| 11 | 2026-09-24 | SSG | A | 5–4 | W |
| 12 | 2026-09-22 | NC | H | 8–5 | W |
| 13 | 2026-09-20 | Lotte | A | 6–13 | L |
| 14 | 2026-09-19 | Lotte | A | 3–5 | L |
| 15 | 2026-09-18 | Hanwha | A | 10–4 | W |
| 16 | 2026-09-16 | Doosan | A | 1–3 | L |
| 17 | 2026-09-15 | Lotte | H | 7–3 | W |
| 18 | 2026-09-13 | LG | H | 5–13 | L |
| 19 | 2026-09-12 | LG | H | 3–4 | L |
| 20 | 2026-09-11 | Kiwoom | H | 6–4 | W |

**Trace sources** (dated structured box/schedule, official KBO where cross-checked):
- KBO: `https://eng.koreabaseball.com/Schedule/DailySchedule.aspx` (official Oct results), `https://www.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-11` (official KT 12–3 Samsung final).
- MyKBO: `https://mykbostats.com/schedule/week_of/2026-09-15`; `/schedule/week_of/2026-09-22`; `https://pgtest.mykbostats.com/schedule/week_of/2026-09-29`; `https://mykbostats.com/schedule/week_of/2026-10-09`; `/schedule/22-KT-Wiz/week_of/2026-09-08`; `/schedule/3-Samsung-Lions/week_of/2026-09-08`. Direct game/event receipts provide independent display, but underlying feed independence NOT_ESTABLISHED.
- Historical opponent ratings: `OPPONENT_ADJUSTMENT_UNAVAILABLE` (opponent identities known, opponent adjusted efficiency/rating as-of-date not assembled). Home-away stratification counts provided; small samples not model adjusted. Named pitchers' last 5/10/15/20 starts not assembled: `0/5`, `0/10`, `0/15`, `0/20` **VERIFIED START-GAME RECORDS IN THIS CARD**, meaning not measured here, *not* zero prior starts.

**A3-LINEUPS**: Official KBO Game Center confirmed advertised starting pitchers So Hyeong-jun KT and Yang Chang-seop Samsung; official order 1–9 and available bench/bullpen list for today's event `NOT_VERIFIED`. Third-party fan site's lineups explicitly labeled PROJECTION, excluded as confirmed. `LINEUP_GATE: PARTIALLY_CONFIRMED` for pitchers / `UNCONFIRMED` for batting orders and active bench, so user-level numerical-primary gate FAIL.

#### A4. Distribution, baseline, expected-score arithmetic and sensitivity
- Historical observed means in A3 are exactly sum(for)/n and sum(against)/n; full n=20 each. No inflation toward probabilities. Last 5 KT for 42/5=8.4, against 9/5=1.8; Samsung for 17/5=3.4, against 35/5=7.0.
- KBO old/v10 league prior: 2023–25 regular-season n 2182, home 4.88, away 4.89, total 9.77, total SD 4.93, margin SD 4.79, sample tie share 2.1%. `Extra Innings`/`Innings Played` KBO archive fields hold placeholders, so 2026-10-11 framework explicitly withdraws computed extras shares; do not infer completed-game tie/innings distribution for exact full-game p.
- So season 3.23 ERA and 1.24 WHIP vs Yang 5.01 and 1.51 are verified published season aggregates, not sufficient to fit component offense/run distribution without lineup/bullpen/park and calibrated inputs. Rest/late season, venue, pitcher usage, and form are uncertainty disclosures only; adjustments NONE NUMERICALLY APPLIED.
- Last 5/10/15/20 form is intentionally shown, including sharp KT last-five improvement and Samsung last-five decline. These windows nest; they are not four independent samples. No arbitrary weights, no deduced forecast score, no covariance, no invented negative-binomial fit. `WINDOW_SENSITIVITY_NOT_COMPUTABLE` because no candidate distribution.
- Frozen `BASELINE_LEAGUE_V1` at supplied exact rows **NOT_COMPUTED** due unknown extras law/selection endpoint and missing complete distribution; no default 50% or line-implied substitution.

#### A5. Full priced universe or labelled subset; W/P/L/V by row
- Supported numeric candidate universe = NONE; attempted supplied rows 3 distinct plus 1 duplicate. For KT −1.5, Samsung +1.5 and Over 11.5: W/P/L/V `NOT_COMPUTED`, `p_card=NOT_ESTIMATED`, `BASELINE_P=UNAVAILABLE`. The historical over-11.5 fractions in A3 are **not** a pairwise same-line model and must not be scored as forecasts.
- No selected Rank 1/2 or row probability status fabricated; 2026 regular season draws allowed. Quarter/phase lines N/A.

#### A6. Adjustments, regimes and unadjusted comparison
- Home Daegu, official starters, starter ERA/WHIP differences, KT recent surge, Samsung late-season form deterioration, bullpen fatigue from 11 Oct and lineup rotation risks listed as **UNQUANTIFIED**. Unknown bullpen pitch counts and lineup mean no numerical adjustment. Regime flag NONE. Any claimed ranking change/adjustment sensitivity NOT_COMPUTABLE.

#### A7. Family checks and shadow records
- KT -1.5 and Samsung +1.5 are sporting complements at exactly the same line. Double loss impossible by sporting arithmetic on a completed score; pairing them would be mechanically protected, not skill. No selected pair exists. RET03, RET04, XCARD6 NOT_ISSUED. `FORM_WINDOW_SENSITIVE: NOT_COMPUTABLE`; `LINEUP_GATE: PARTIALLY_CONFIRMED (starters only), NUMERIC_ISSUANCE_BLOCKED`.
- KBO draw/extra inning policy must be confirmed to precise event operator rules at a later authorized reforecast; no endpoint assumptions silently imported from MLB automatic-runner rules.

#### A8. Sources, failures and capture/refresh plan
- Official KBO game center `https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx?gameDate=20261012&gameId=20261012KTSS0&section=START_PIT`; official KBO schedule `https://www.koreabaseball.com/Schedule/Schedule.aspx?month=10&year=2026` and English daily schedule. Official starters recorded, event shows scheduled. Current-order and bullpen/bench fields NOT_VERIFIED. Source times not displayed; researched 20:22–20:26 AEDT, lineage UNKNOWN.
- Structured MyKBO event `https://mykbostats.com/games/14037-KT-vs-Samsung-20261012` checked as comparison; dated games as in A3. Fan site's projected lineups do not satisfy official lineup confirmation.
- Archive 2026 KBO CSV on GitHub 404; 2023–25 profile available but extras placeholder. No opponent-quality table, no verified individual pitcher last-20 game log, no strict score-distribution fit.
- Settlement capture official structured final status, each team runs, total runs and 11-inning/tie/shortening field after actual terminal; no scheduled task, retry `NOT_SCHEDULED`. Pending local append does not settle an event.

#### A9. Integrity receipt, card audit and readback
- C1: PARTIAL (main current versions reviewed, giant register/full canonical body not exhaustively re-read). C2: PARTIAL (official event key + source and local duplicate search, remote all-log uniqueness NOT_VERIFIED). C3: N/A (NO_FORECAST; duplicate supplied line retained with disposition). C4–C7: N/A/NOT_COMPUTED (no numeric forecast). C8: PASS (no unsourced regime adjustment). C9: PARTIAL (KBO event action/operator conventions unknown). C10: PASS (no market source used as model evidence). C11: PARTIAL (schedule verified, true first pitch NOT_VERIFIED). C12: PASS (20/20 final result trace and no 2026 archive assumptions). C13: PARTIAL (official starters confirmed, playing orders/bench unconfirmed). C14–C16: PARTIAL/NOT_VERIFIED pending full template checks and write/readback.
- FR1–FR4: PASS for raw four-window source-reported team scoring form; opponent adjustment NOT_AVAILABLE; modeled sensitivity NOT_COMPUTABLE. FR5: BLOCKED numeric forecast (confirmed pitchers only). FR6: PARTIAL (complete evidence tables; no numeric ranks, readback in local execution receipt).
- No live result/settlement/canonical import performed. No numerical probability and no certainty/certification claim. Original P-580–P-582 block bytes preserved.
SPORTS_ONLY_MARKET_BLIND: PASS FOR INPUTS · OUTCOME_EXPOSURE: NONE_OBSERVED_IN_RESEARCH; ACTUAL_KICKOFF_NOT_VERIFIED · SETTLEMENT: NOT_PERFORMED · CANONICAL_IMPORT: PENDING · GITHUB_WRITES: NO
<!-- END CARD P-583 -->

<!-- BEGIN ADDENDUM P-583 20261012T202924+1100-TIMING -->
### Addendum · P-583 · 2026-10-12T20:29:24+11:00 AEDT · issued timing classification
- **Parent:** Original P-583 NO_FORECAST card above; original issue / complete write/readback: `2026-10-12T20:29:24+11:00 AEDT`.
- **Correction:** The original timing line conditionally said PREGAME_SCHEDULED if issued before scheduled kickoff. Under SCORING_AND_VALIDATION and CURRENT_RULES the scheduled lead was only **36 seconds** to 20:30 AEDT, therefore this card is **`LATE_START / ACTUAL_KICKOFF_NOT_VERIFIED`**, regardless of whether the true first pitch occurred later. This is a process-label correction only, not a new forecast or historical result.
- **Cutoff/source provenance:** Pregame-labeled official KBO Game Center queried during 20:22–20:26 AEDT; no actual first pitch timestamp established. Numeric LINEUP_GATE still blocked, Rank 1/2 NOT_ISSUED, `p_card` unchanged NOT_ESTIMATED, no event outcome or settlement ingested.
- **Custody:** Original P-583 bytes retained; this dated addendum supersedes only the timing band statement in P-583. Local P-584 remains the next working ID, GitHub writes zero.
<!-- END ADDENDUM P-583 20261012T202924+1100-TIMING -->

<!-- BEGIN ADDENDUM P-583 20261012T203748+1100-LATE-NUMERIC-DIAGNOSTIC -->
### Addendum · P-583 · 2026-10-12T20:37:48.908413+11:00 · Late quantitative scenario requested by user

**Parent/custody:** Existing P-583 NO_FORECAST card and its 20:29:24 AEDT timing correction remain **unchanged**. User instructed, after original issue, `Doesnt matter if its late START`. This is a separately dated **POST-ISSUE, LATE/START-UNCERTAIN, NUMERIC DIAGNOSTIC**, not a retroactive primary forecast, no new P-ID, no original `p_card`, no new Rank 1/2 for validated scoring, no settlement, no post-match outcomes or live inputs. The attached estimates must not enter prospective v10 calibration or W/L metrics. Official date 2026-10-12 18:30 KST = 20:30 AEDT; the actual first pitch and live score were **not verified at this analysis cutoff**. The estimate is conditional on pre-event public form, not game action. Do not present it as a live-game win probability.

**Frozen information and constraints:** use only pre-event data in original P-583 A3 (20 completed, date-traced prior KBO games per team, form 5/10/15/20) and pre-event published season team scoring through 143 games. Official KBO lists starting pitchers So Hyeong-jun (KT) and Yang Chang-seop (Samsung); full verified 1–9 batting order and available bench were NOT confirmed. LINEUP_GATE remains `PARTIALLY_CONFIRMED / NOT_PASSED`, so the original primary `NO_FORECAST` stays. Previews/odds/market lines did not inform the model. Third-party team season record as-of before game: KT 89–49–5; 821 runs scored, 647 allowed / 143; Samsung 83–57–3; 804 scored, 665 allowed / 143. Repo `LEAGUE_PROFILES.md` KBO 2023–25 regular-season n=2182: away 4.89, home 4.88, team-run dispersion phi=0.290, final tie share approx 2.1%; extra-innings share **NOT_ESTIMABLE**. Sources: https://m.aiscore.com/ko/baseball/tournament-kbo-league/2jr7onc64gs1q0e ; https://www.koreabaseball.com/Schedule/Schedule.aspx?month=10&year=2026 ; https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=11353 ; `LEAGUE_PROFILES.md` and original P-583 A3. No 2026 CSV found at the published KBO path. All figures explicitly research-only and provider lineage not independently established.

#### Diagnostic construction and assumptions

- Published season runs per game: KT offense 821/143=5.7413, KT allowed 647/143=4.5245; Samsung offense 804/143=5.6224, Samsung allowed 665/143=4.6503.
- **Arbitrary, explicitly unvalidated demonstration weights:** score rates = 70% season 2026 + 30% chosen lookback window, for each club's offense and allowed rates separately. These are nested-window alternatives, never pooled as four independent samples. Default last-20 window, not chosen retrospectively from outcome.
- Away KT centre = `[0.70×KT season offense + 0.30×KT window offense] × [0.70×Samsung season runs allowed + 0.30×Samsung window allowed] / 4.89`.
- Home Samsung centre = `[0.70×Samsung season offense + 0.30×Samsung window offense] × [0.70×KT season runs allowed + 0.30×KT window allowed] / 4.88`.
- Independent negative-binomial *approximation* to both full-game team run counts with `Var(R)=mu+0.290×mu²`, parameter `r=1/0.290≈3.448276` and `p=r/(r+mu)`. Calculated exact numerical discrete mass over 0–89 runs per team; tail residual less than 1e-7 in every scenario. Shared stadium environment/covariance, starters' innings vs relief sequencing, home no-bottom-ninth, actual lineup performance and inning-by-inning tie branching not fitted. No starter ERA modifier applied because staff/innings split is unknown and such a modifier could double-count team scoring. The official regular-season innings cap is 11 (KBO historical 2025 rule change), but no fully specified 9th-to-11th inning probability process is available.
- This is **not** a fitted, calibrated, validated or true full-game settlement distribution. In particular, the raw independent-score draw mass differs materially from historical final KBO draws. To illustrate full-game winner branches only, redistribute `(raw score-tie probability − 0.021)` 50:50 to each side, preserving 0.021 tied-final mass; assume any resolved tie adds exactly one run to the winner. This approximation is **not** used to change the supplied KT −1.5, Samsung +1.5 or Over 11.5 scores at their thresholds, and cannot establish operator-specific action terms. The 2.1% final-tie share is an historical unconditional league descriptive statistic, not a 2026 team-specific estimate. Full-game probability claims remain uncertainty-qualified.

#### Four-window model sensitivity (same frozen formula and inputs)

| Data window | E(KT runs) | E(Samsung runs) | P(KT −1.5) | P(Samsung +1.5) | P(total Over 11.5) |
|---|---:|---:|---:|---:|---:|
| Last 5 | 7.16 | 3.76 | 61.6% | 38.4% | 40.3% |
| Last 10 | 6.54 | 4.23 | 53.9% | 46.1% | 39.4% |
| Last 15 | 6.27 | 4.82 | 47.7% | 52.3% | 41.8% |
| Last 20 | 6.27 | 4.86 | 47.5% | 52.5% | 42.1% |

**Default last-20 numeric research scenario:** expected runs KT **6.27**, Samsung **4.86**, combined **11.13** and KT−Samsung signed expected margin **+1.41** runs. NB variance KT 17.68, Samsung 11.71, independent-approx total SD **5.42**, margin SD **5.42**. Score covariance set zero by *explicit approximation*, not by evidence of independence. Conditional first/last inning and exact likely score NOT_ESTIMATED.

#### Requested propositions — informational numeric probabilities ONLY

| Original supplied contract | Proxy probability | Numeric status | Principal way the proposition fails |
|---|---:|---|---|
| `Wiz -1.5` — KT wins by at least 2 runs | **47.5%** | `P_LATE_SCENARIO / NOT_PRIMARY` | KT loses, ties or wins by only one |
| `Lions +1.5` — Samsung loses by no more than 1, ties or wins | **52.5%** | `P_LATE_SCENARIO / NOT_PRIMARY` | KT wins by at least 2 |
| `Combined Total Runs: Over 11.5 Runs` — 12+ runs | **42.1%** | `P_LATE_SCENARIO / NOT_PRIMARY` | 11 or fewer total runs |
| `Combined Total Runs: Over 11.5 Runs` repeated | same **42.1%**, duplicate only | `DUPLICATE_REFERENCE / NOT_PRIMARY` | same exact proposition; not a fourth independent opportunity |

Derived diagnostic only: **Under 11.5** = **57.9%** (not supplied). **Potential game winner** under the explicitly ad hoc historical-tie-share resolution: KT **58.9%**, Samsung **39.0%**, final tie **2.1%**, sum = 100%. Without this correction, the raw joint score model yields KT win **55.8%**, Samsung win **35.9%** and score tie **8.2%**; the discrepancy demonstrates why true extra-innings simulation and confirmed batting orders matter. A regulation-only winner probability is not resolved by this model.

**Interpretation:** Last-5 gives KT −1.5 61.6%, while last-20 gives 47.5%: a **14.1-percentage-point form-window swing**. The supplied `Samsung +1.5` and `KT −1.5` are exact sporting complements in completed full-game scores, so the stronger of the pair always depends on which side of 50% a model gives; backing both is mechanically protected and is not selection skill. Under the current primary Rank-1 62% gate, **none of the three unique supplied contracts pass**, even under this unvalidated baseline scenario. Ret03/Ret04/XCARD6 not promoted. No original `BASELINE_P` backfill: `BASELINE_LEAGUE_V1` originally `UNAVAILABLE`, still unavailable because registered baseline endpoint treatment including extras was not executed preissue. Nothing becomes a `p_card` by being calculated after issue.

#### Integrity/audit and action

- `SOURCE_CUTOFF`: original 20:22–20:26 AEDT research; numerical calculation/write 2026-10-12T20:37:48.908413+11:00 after scheduled start; `LATE_SCENARIO / NOT_PROSPECTIVE`. No post-event score or in-play state used, and no claim of live-current state. Current online snapshots can be stale or cache old pregame status.
- `LINEUP_GATE`: official starting pitchers known, official confirmed batting orders, bench and bullpen composition NOT_VERIFIED; therefore no promotion to official numerical Rank 1/2. Original P-583 remains NO_FORECAST.
- `FORM_WINDOWS`: actual 20/20 games traced per side in original A3; alternate 5/10/15/20 outputs above; opponent-strength adjustment unavailable, source coverage period documented. 2026 standings source is a provider snapshot, not a independently audited team-level record. 70/30 weights and phi independent-score approximation NOT_TESTED.
- `SETTLEMENT`: NOT_PERFORMED. `GITHUB_WRITES`: NO. `CANONICAL_IMPORT`: PENDING. `CANONICAL_IDS_CONSUMED`: 0. `NEXT_LOCAL_WORKING_ID`: P-584 unchanged. Historical original card/ranks/probabilities remain unaltered.
<!-- END ADDENDUM P-583 20261012T203748+1100-LATE-NUMERIC-DIAGNOSTIC -->


<!-- BEGIN CARD P-584 -->
## Card · P-584 · Soccer / Mexico Liga Premier Serie A (Group 2, Round 7) · Dragones de Oaxaca vs Guerreros del Pacífico · 2026-10-12 Oaxaca / 2026-10-13 Melbourne

- **Working ID:** `P-584` — `LOCAL_WORKING_ID`, `PENDING_CANONICAL_IMPORT`; assignment only to this preserved local mini, no GitHub canonical ID issued.
- **Event key / aliases:** `MEX-LIGA-PREMIER-SERIE-A:2026-27:R7:DRAGONES-OAXACA-GUERREROS-PACIFICO:2026-10-12`; native match ID `NOT_VERIFIED`; BeSoccer match ref `2027176995` is a *provider reference*, not official native ID.
- **Authority:** `PUBLISHED_MAIN_PINNED` at full HEAD `adb8560a597e5ff1a5ad21bfc76b3148bd58c719`; MDS-2026.10.12-v11.0 / CR-2026.10.12-R2 / SCV-2026.10.12-v7 / SEL-2026.10.12-v3; repository read only. Existing local `mini-log-6` is continued with its original format; this new card has v11 limitation disclosure, not a retroactive conversion of prior cards.
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO` with `PROSPECTIVE_RANK_HELD_KNOWN_AT_UNVERIFIED`. Four internally ranked numerical **diagnostic** rows below are `NOT_PRIMARY / NOT_PERFORMANCE_ELIGIBLE`, not certified new Rank-1/2 picks. No fabricated first-half/corner values.
- **Timing:** scheduled `2026-10-13T13:05:00+11:00`; actual match start `NOT_VERIFIED`; cutoff of retrieved form/identity inputs ≤ `2026-10-13T13:06:27+11:00`; research and issue `2026-10-13T13:06:27+11:00`, final official-state recheck `NOT_VERIFIED` (no official live/started field accessible). Classification `LATE_START_UNVERIFIED`; lead -1.46 min / `LATE_START`. `OUTCOME_EXPOSURE: NONE_OBSERVED` (no current score or final used); **this does not prove the match had not started**. If a later official state proves kickoff before issue, label the card late separately; no backdating.
- **Scheduled start:** 12 Oct 2026, 20:05 Oaxaca local (UTC−06) = 13 Oct 2026 02:05 UTC = 13 Oct 2026 13:05 AEDT (UTC+11); Estadio del Instituto Tecnológico de Oaxaca (Estadio ITO), Oaxaca de Juárez; official club fixture and 09-Oct article.
- **Endpoint:** 90 minutes plus stoppage, excludes shootout and competition-specific post-match penalty shootout for extra points; result draw retained. Operator settlement for abandonments or extraordinary postponement `UNKNOWN_DEFINITION`. All lines treated as sport-regulation propositions. No ET/penalty conversion.
- **Distribution:** `P584-POISSON-RAW-SEASON-3CASE-v1`: observed side-specific season scored/conceded means; independent Poisson within each scenario with intensity scales 0.80/1.00/1.20, weights 0.25/0.50/0.25. Scale scenarios represent **arbitrary uncalibrated uncertainty, NOT player-based confirmed lineups**. No supported opponent-adjustment or validated seasonal league shrinkage.
- **Expected score:** Dragones 1.5667 goals (mixture SD 1.271), Guerreros 0.9833 (SD 1.001); total 2.5500 (SD 1.637); signed home-away margin +0.5833 (SD 1.599), shared mixture covariance 0.0308 under arbitrary common scenario scaling (not an empirical match covariance). Means are not exact-score forecasts.
- **League-only baseline:** `BASELINE_UNAVAILABLE` for this league/era/line: no independently vetted populated 2026-27 Liga Premier Serie A match-level, league-wide outcome cohort or league-profile scoring row read. **Do not use the Premier League or Liga MX as a substitute**. Baseline coverage 0/4 of ranked diagnostic numeric rows.
- **Context / regime:** `EARLY_SEASON`; Dragones promoted from Serie B; five/six matches in this new competition; home advantage and opponent strength unquantified, goalkeeper/substitute/rotation effects unresolved.
- **Lineup state / issue step:** `LINEUP_UNCONFIRMED / RETRIEVAL_MISS`: verified official starting XI, goalkeepers, matchday active substitutes, late scratches not obtained from official club / match-owner lineup sheet. A preview's suggested XI is not a confirmed sheet. T−60 and T−5 research targets not achieved for this user-requested near-start analysis; no fake confirmation.
- **Known-at:** Official club's historical six results and 09-Oct fixture article are dated before match; third-party Guerreros five-result compilation has no immutable capture timestamp, `KNOWN_AT_UNVERIFIED`. League-prior rate also missing. Therefore **none of these numerical diagnostic rows decides an eligible prospective Rank 1** under R28.
- **Settlement capture fields:** official final regulation goals and HT score, goal minutes, starting XIs, goalkeeper and substitutes, team corners (precise metric; whether corners incl. stoppage), match status/cancellation, official actual kickoff; field owner Liga Premier / club; structured fallback BeSoccer or Sofascore if match-specific data; final-time basis UNKNOWN, request initiated only, `AUTOMATION: NOT_SCHEDULED`.
- **Rules read and archive:** pinned `CURRENT_STATE`, `METHOD`, `CURRENT_RULES`, `SELECTION_RULES`, `CARD_AND_LOG_TEMPLATES`, `SCORING_AND_VALIDATION`, `GAME_LOG_STATUS_CURRENT`, `PROBABILITY_TOOLKIT`, `ARCHIVE_USE_GUIDE` R2, `RULES_SOCCER`, `LEAGUE_RULES_SOCCER`, `LEAGUE_PROFILES`, `BASE_RATES_REGISTER`, current Prompt 1 and the supplied local enhanced prompt; no eligible populated Premier Serie A archive for this fixture verified. `ACTIVE_FILE_INDEX` lists only 35 of 172 populated competition folders and does not list Liga Premier Serie A. Thus 0 local Liga Premier match-record rows programmatically read; all 11 qualifying results manually traced via current source pages.
- **Evidence receipt:** Dragones club official fixture/results/standings and article; Guerreros five dated matches in BeSoccer, corroborated as results (not as predictive odds) by an independent-looking structured result page, but collector independence `UNKNOWN`; retrieval/analysis timestamp `2026-10-13T13:06:27+11:00`. See A3/A8.

### Decision block — original issuance scope

**Direction:** Dragones have a supported qualitative home-edge case (4W–2D–0L, 14–7 goals in six current Serie A games) against Guerreros (2W–1D–2L, 4–4 in five). A five/six-match scoring sample, no matchday confirmed XI, absent first-half/corner denominators, unavailable league benchmark and unverified third-party known-at history preclude **prospectively eligible** numerical primary rankings. A narrow, explicitly uncalibrated full-time sensitivity model is disclosed for diagnostic comparison only.

| Rank (exploratory only) | Role | Tag | Contract key / exact proposition | p_scenario, NOT_PRIMARY | p_base | BASELINE_P | Distance units / z | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK_DIAGNOSTIC | ANALYST_DERIVED | `regulation_total:under:4.5` — Combined regulation goals Under 4.5 | 87.94% | 88.44% | BASELINE_UNAVAILABLE | +1.95 / +1.19 | Independent-Poisson 3-scenario, NOT_PRIMARY | Five or more regulation goals |
| 2 | PICK_DIAGNOSTIC | ANALYST_DERIVED | `regulation_result:1X` — Dragones de Oaxaca win or draw in regulation | 76.35% | 76.25% | BASELINE_UNAVAILABLE | N/A / N/A | Independent-Poisson 3-scenario, NOT_PRIMARY | Guerreros win in regulation |
| 3 | INFORMATIONAL_DIAGNOSTIC | ANALYST_DERIVED | `regulation_total:under:3.5` — Combined regulation goals Under 3.5 | 74.43% | 74.68% | BASELINE_UNAVAILABLE | +0.95 / +0.58 | Independent-Poisson 3-scenario, NOT_PRIMARY | Four or more regulation goals |
| 4 | INFORMATIONAL_DIAGNOSTIC | ANALYST_DERIVED | `regulation_total:over:1.5` — Combined regulation goals Over 1.5 | 71.50% | 72.28% | BASELINE_UNAVAILABLE | -1.05 / -0.64 | Independent-Poisson 3-scenario, NOT_PRIMARY | Zero or one regulation goal |

**Rank-1/Rank-2 issuance:** `HELD_KNOWN_AT_UNVERIFIED`; no prospectively counted top two. In the exploratory restricted slate, Under 4.5 has 87.94%, next alternative 1X 76.35%, gap 11.59 pp; nominal numeric gate PASS, but **not a valid prospective PASS**, since C13/R28 incomplete, BASELINE_UNAVAILABLE and candidate list is restricted diagnostic only. Rank-2 exploratory floor 58% met but no certified selection.

**Joint-failure diagnostic:** `3.00%` from joint mixture for Under 4.5 loss AND Dragones 1X loss (Guerreros win with five-plus combined goals); NOT mechanically protected, conditioned completed regulation 100% under this simplified model. `ε<0.00001` for numerical summation truncation only, NOT model uncertainty; parameter variation dominates.

**Shadows:** `RET03 / RET04 / XCARD6 / SHADOW_RANK_DELTA` = not promoted / not valid without eligible prospective slate and league baseline. `SHADOW_BASE_ONLY` under 4.5 88.44%, 1X 76.25%; same diagnostic ordering. No rank delta (0 valid BASELINE_P).

**Most likely sporting winner (90-minute 1X2, diagnostic):** Dragones **50.72%**, draw **25.63%**, Guerreros **23.65%**; total 100.00%. Full-time result not settled by a penalty shootout for a league bonus point.

**Supplied-input ledger:**

| Supplied contract (exact meaning) | Probability / disposition | Evidence condition |
|---|---|---|
| 1H Over 0.5 | NOT_ESTIMATED | Provider-backed first-half goals absent; 1/6 Dragones 1H (2–1) anecdote insufficient |
| 1H Under 0.5 | NOT_ESTIMATED | Same missing phase coverage; not silently inferred from FT |
| FT Over 2.5 | 46.55% | Exploratory uncalibrated full-time model; not certified |
| FT Under 2.5 | 53.45% | Same coherent full-time distribution |
| Corners Over 10.5 | NOT_ESTIMATED | No 20-row field-owner match-corner dataset; ambiguous/commercial aggregate rejected |
| Corners Under 10.5 | NOT_ESTIMATED | Same missing provider-backed corner definition; no inferred goal/corner rate |

### Appendix
#### A1. Verified event identity and state
Official club match listing: `https://www.dragonesfc.mx/equipos/premier-a/calendario` (Round 7, 12-Oct 20:05, Estadio ITO) and 09-Oct article `https://www.dragonesfc.mx/noticias/dragones-oaxaca-vivira-un-fin-de-semana-especial-con-el-lunes-premier`. Local date versus Melbourne timezone distinguished; final/started status NOT_VERIFIED; no live data used. Same-event search in this local mini found no Dragones/Guerreros card, so `P-584` is a fresh local record, not an addendum. Repo canonical next P-580 but local P-580–P-583 already exist, so next unimported local working ID was P-584. External parallel writers cannot be audited from the sandbox.

#### A2. Frozen propositions, modelling cohort and candidate recipe
Six supplied contracts in their supplied order: 1H Over 0.5, 1H Under 0.5, FT Over 2.5, FT Under 2.5, corners Over 10.5, corners Under 10.5. All refer to match combined counts; each quantity and endpoint distinct; no missing duplicate or silently altered side. Diagnostic pre-pricing candidate universe = goal totals Over/Under at 0.5, 1.5, 2.5, 3.5, 4.5, 5.5; match 1X2; double chance 1X and X2; BTTS yes/no where same score grid supports. First-half and corners candidate families **excluded from numerical universe** for lack of observed source fields. Numeric candidates with p > 90% are diagnostic exclusions, never capped. No derived lines selected retrospectively from an outcome.

#### A3. Historical form, event-level traces, opponent and lineup evidence

**Dragones de Oaxaca — six current-season, same-division regulation finishes (newest first):**

| Date (Oaxaca) | Opponent and venue | Regulation score (Dragones–opponent) | Result | Provider |
|---|---|---|---|---|
| 2026-10-03 | Real Refineros CDS, HOME | 3–2 | W | Club official |
| 2026-09-27 | Delfines Coatzacoalcos, AWAY | 3–3 | D; extra league-point shootout *not* a full-time goal | Club official |
| 2026-09-19 | Cañoneros Marina, HOME | 3–0 | W | Club official |
| 2026-09-13 | Acámbaro FC, AWAY | 1–1 | D | Club official |
| 2026-09-05 | Halcones Negros, HOME | 2–1 | W | Club official |
| 2026-08-29 | Ciervos, AWAY | 2–0 | W | Club official |

**Guerreros del Pacífico — five current-season, same-division regulation finishes:**

| Date (Mexico local; provider) | Opponent and venue | Regulation score (Guerreros–opponent) | Result | Provider |
|---|---|---|---|---|
| 2026-10-02 | Delfines Coatzacoalcos, HOME | 0–0 | D | BeSoccer |
| 2026-09-26 | Cañoneros Marina, AWAY | 2–0 | W | BeSoccer |
| 2026-09-18 | Acámbaro FC, HOME | 0–1 | L | BeSoccer |
| 2026-09-12 | Halcones Negros, AWAY | 0–3 | L | BeSoccer |
| 2026-09-04 | Ciervos, HOME | 2–0 | W | BeSoccer |

**Rolling-window counts and goals; DO NOT silently pool Dragones 2025-26 Serie B matches:**

| Club | Requested window | Actual eligible n | W–D–L | GF/game | GA/game | Net/game | Window/venue note |
|---|---|---:|---|---:|---:|---:|---|
| Dragones | L5 | 5/5 | 3–2–0 | 2.40 | 1.40 | +1.00 | Oct03–Sep05; 3 home/2 away |
| Dragones | L10 | 6/10 | 4–2–0 | 2.3333 | 1.1667 | +1.1667 | 3 home/3 away; 4 missing |
| Dragones | L15 | 6/15 | 4–2–0 | 2.3333 | 1.1667 | +1.1667 | 9 missing |
| Dragones | L20 | 6/20 | 4–2–0 | 2.3333 | 1.1667 | +1.1667 | 14 missing |
| Dragones | Season-to-date | 6/6 | 4–2–0 | 2.3333 | 1.1667 | +1.1667 | 2026-27 Liga Premier Serie A |
| Guerreros | L5 | 5/5 | 2–1–2 | 0.80 | 0.80 | 0.00 | 3 home/2 away |
| Guerreros | L10 | 5/10 | 2–1–2 | 0.80 | 0.80 | 0.00 | 5 missing |
| Guerreros | L15 | 5/15 | 2–1–2 | 0.80 | 0.80 | 0.00 | 10 missing |
| Guerreros | L20 | 5/20 | 2–1–2 | 0.80 | 0.80 | 0.00 | 15 missing |
| Guerreros | Season-to-date | 5/5 | 2–1–2 | 0.80 | 0.80 | 0.00 | 2026-27 Liga Premier Serie A |
| League profile | League level | N/A | N/A | NOT_ESTIMATED | NOT_ESTIMATED | N/A | No matching vetted `LEAGUE_PROFILES` row |

**Nonoverlapping blocks:** Dragones most-recent 1–5 = 5 complete, older 6–10 has only one match (2–0 Ciervos); blocks 11–15 and 16–20 have zero comparable matches. Guerreros most-recent 1–5 has five, blocks 6–10 onward zero. No independent L5/L10/L15/L20 trends exist beyond these nested repeated data. **Home/away:** Dragones home 3 games: GF8/GA3; away 3: GF6/GA4. Guerreros home 3: GF2/GA1; away 2: GF2/GA3. **Opponent quality:** Dragones opponents include the weaker Cañoneros (0 group points) and Ciervos (2 points), so 2.33 GF/game can overstate opponent-neutral strength; no pregame event-level opponent ratings computed, `OPPONENT_ADJUSTMENT_UNAVAILABLE`. The host club labels Dragones second in Group B at 15 points, Guerreros sixth at eight (league awards may use extra points after draws). **Historical division:** Dragones reached Serie A after promotion from Serie B, so Serie B results are contextual only, NOT merged into same-era Serie A window.

**Phase / corners field coverage:** Dragones official Oct03 article confirms **2–1 at half-time**, and Halcones Negros match goal timings include 15′, 55′, but no complete 5-match 1H dataset; HT sample actually usable only **1/6 match** (and a partial scoring chronology in another). Guerreros first-half final scores **0/5 verified**. Independent verified match-level combined corners: **0/6 Dragones, 0/5 Guerreros**. Some commercial sites show dynamically generated aggregate corners that cannot be reconciled to named matches; no imputed all-zero corners, no Poisson corner estimate. Similarly no verified xG/xGA, shots, lineup/bench, keeper names or opponent-adjustment data; these stay NOT_ESTIMATED.

#### A4. Distribution, reproducible arithmetic and sensitivity
- Observed pre-match Serie A averages: Dragones GF `14/6=2.33333`, GA `7/6=1.16667`; Guerreros GF `4/5=0.80000`, GA `4/5=0.80000`.
- **Illustrative unsupported-by-validation centre:** home `(Dragones GF/game + Guerreros GA/game)/2 = (2.33333 + 0.8)/2 = 1.566667`; away `(Guerreros GF/game + Dragones GA/game)/2 = (0.8+1.16667)/2 = 0.983333`; total `2.550000`. Equal averaging is a declared *analyst heuristic* and does not satisfy R2's tested opponent/league shrinkage because no reliable league-level `LM` available; no made-up k or imported EPL league level. Thus **R2 centre model coverage PARTIAL**, data gaps disclosed.
- Base independent score mass `P(H=i,A=j) = e^(−h) h^i/i! × e^(−a) a^j/j!`. Low/base/high scenarios multiply **both** h and a by `[0.8,1.0,1.2]`; weights `[0.25,0.50,0.25]` frozen before pricing. Scale width ±20% is illustrative only, no stated validation. Conditional independence within each scenario is assumed, NOT observed; common scale induces mixture covariance `0.03081`. Computed integer grid H,A=0..29, all masses normalized by grid sum; omitted tail is below 10⁻¹⁵ for these means (numerical, not predictive). Exact state query formula `Σ_i Σ_j P(H=i,A=j) · 1{contract wins}`. Zero pushes, zero voids on half-integer football goals and regulation 1X2 conditional completed result; operator abandonment action still unverified.
- Base-only goals λh=1.566667, λa=0.983333; mixture expectation home=1.566667 away=0.983333, total=2.550000; total σ=1.637086, signed margin σ=1.599001. Goals-centre direction intentionally *not* adjusted further for venue or promoted/away status due no validated coefficient, and goalkeeper/injury lineups `NOT_VERIFIED`.
- **Low/base/high FT Over 2.5:** 33.41% / 46.89% / 59.01%; full-mixture 46.55%. **Low/base/high Under 4.5:** 94.37% / 88.44% / 80.51%; full-mixture 87.94%.
- **Sensitivity:** low/high intensity ±20% produces FT Over2.5 range ≈33.4–59.0% and Under4.5 range ≈80.5–94.4%; this very wide range is a central caveat and is NOT a confidence interval. The 20-match windows are unavailable, so numerical FORM_WINDOW_SENSITIVE test cannot be computed; `WINDOW_SENSITIVITY_NOT_COMPUTABLE`. Changes are pre-outcome scenarios, not retrospective tuned weights. League-only baseline: `BASELINE_UNAVAILABLE` due source cohort/endpoint missing.

#### A5. Full supplied contracts and supported candidate families — W/P/L/V
On a hypothetical completed 90-minute match, unconditional W=p, P=0, L=1−p, V=0 for supported half-goal and 1X2 propositions; action rules for suspended games NOT_VERIFIED. Rows below are **analyst scenario probabilities, NOT_PRIMARY p_card**. Different families with missing data are NOT_ESTIMATED, not false zero.

| Contract key | Proposition | W | P | L | V | Scenario p | p_base | Disposition |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `regulation_total:over:2.5` | Supplied FT goals Over 2.5 | 46.55% | 0% | 53.45% | 0% | 46.55% | 46.89% | SUPPLIED_DIAGNOSTIC |
| `regulation_total:under:2.5` | Supplied FT goals Under 2.5 | 53.45% | 0% | 46.55% | 0% | 53.45% | 53.11% | SUPPLIED_DIAGNOSTIC |
| `regulation_total:under:4.5` | Derived Under 4.5 | 87.94% | 0% | 12.06% | 0% | 87.94% | 88.44% | DIAGNOSTIC_RANK1_ONLY |
| `regulation_result:1X` | Derived Dragones win/draw | 76.35% | 0% | 23.65% | 0% | 76.35% | 76.25% | DIAGNOSTIC_RANK2_ONLY |
| `regulation_total:under:3.5` | Derived Under 3.5 | 74.43% | 0% | 25.57% | 0% | 74.43% | 74.68% | DIAGNOSTIC_RANK3_ONLY |
| `regulation_total:over:1.5` | Derived Over 1.5 | 71.50% | 0% | 28.50% | 0% | 71.50% | 72.28% | DIAGNOSTIC_RANK4_ONLY |
| `regulation_home` | Dragones regulation victory | 50.72% | 0% | 49.28% | 0% | 50.72% | 50.91% | WINNER_DIAGNOSTIC |
| `regulation_draw` | Regulation draw | 25.63% | 0% | 74.37% | 0% | 25.63% | 25.34% | WINNER_DIAGNOSTIC |
| `regulation_away` | Guerreros regulation victory | 23.65% | 0% | 76.35% | 0% | 23.65% | 23.75% | WINNER_DIAGNOSTIC |
| `regulation_total:over:0.5` | Derived Over 0.5 | 91.67% | 0% | 8.33% | 0% | 91.67% | 92.19% | EXCLUDED_90_CEILING |
| `regulation_total:under:5.5` | Derived Under 5.5 | 95.02% | 0% | 4.98% | 0% | 95.02% | 95.46% | EXCLUDED_90_CEILING |
| `btts:no` | Derived BTTS No | 50.83% | 0% | 49.17% | 0% | 50.83% | 50.47% | INFORMATIONAL_ONLY |
| `regulation_1h_total:over:0.5` | Supplied first-half goals Over 0.5 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | N/A | PHASE_SOURCE_MISSING |
| `regulation_1h_total:under:0.5` | Supplied first-half goals Under 0.5 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | N/A | PHASE_SOURCE_MISSING |
| `regulation_corners:over:10.5` | Supplied combined corners Over 10.5 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | N/A | CORNER_PROVIDER_MISSING |
| `regulation_corners:under:10.5` | Supplied combined corners Under 10.5 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | 0 | NOT_ESTIMATED | N/A | CORNER_PROVIDER_MISSING |

FT complement: Over2.5 46.55% + Under2.5 53.45% = 100%; 1X2 home 50.72% + draw 25.63% + away 23.65% = 100%. Half and corners remain mutually exclusive but neither side is numerically priced; do not invent complement values.

#### A6. Adjustments / regime / unadjusted pair
Baseline raw Serie A means (GF/GA) are not league-strength adjusted. Model averages both team's offence and opponent defence at 50/50 as disclosed, not independently assessed. Home advantage, opponent/format strength, injuries, starting XI/keeper, red-card risk, weather and tactical role = `NOT_MEASURED`; **no hidden coefficient**. Since no separate adjusted-vs-unadjusted full-quality model exists, adjustment dependence = `NOT_ASSESSABLE`. Low/high scenario changes widths and winner masses; do not treat them as proven +20%/−20% roster contributions.

#### A7. Eligibility, family checks, gate and shadows
Soccer 1H Rank1 strict 0.72 minimum/phase source and 5-point gap: `NOT_ELIGIBLE`, no numbers. Corners require named provider and usable count model; `NOT_ELIGIBLE`. Full-time goal lines and 1X2 are mathematically coherent under declared approximate score grid, but pre-event known-at and exact match-owner XI not verified, so printed ranks are **diagnostic only**. Original gate nominal p=0.879386, floor≥0.62; runner-up full eligible displayed 0.763505, gap=0.115881≥0.04; **NOT A CERTIFIED PASS** due authority/timing/known-at limitations. If gate's proposed entire eligible universe were different, re-evaluate; this is a restricted-universe diagnostic. Ret03 not decision. Ret04 diagnostic different-quantity 1X; XCARD6 would choose a different pair only with full declared eligible comparison; leave NOT_VERIFIED. Rank delta unavailable (no BASELINE_P). Base-only pair same model order. Realised outcomes were not retrieved and cannot enter selection.

#### A8. Source and evidence register / next capture fields
- Official Dragones next game, local venue/time: `https://www.dragonesfc.mx/equipos/premier-a/calendario`, fixture Round 7, 12-Oct 20:05, Estadio ITO; owner publication time `NOT_STATED`; retrieved `2026-10-13T13:06:27+11:00`. Club 09-Oct announcement: `https://www.dragonesfc.mx/noticias/dragones-oaxaca-vivira-un-fin-de-semana-especial-con-el-lunes-premier`, explicitly dated 09-Oct and 20:05; ownership match identity A-grade.
- Official Dragones 2026 Serie A six results and scorers: `https://www.dragonesfc.mx/equipos/premier-a/resultados`, match scores above, update time `NOT_STATED`, retrieved `2026-10-13T13:06:27+11:00`. Official 05-Oct article verifies Round 6 half-time Dragones 2–1: `https://www.dragonesfc.mx/noticias/dragones-vence-a-real-refineros-y-mantiene-el-invicto-en-casa` (05-Oct date). Most-recent result 03-Oct, no same-day future exposure. Club stand/points `https://www.dragonesfc.mx/equipos/premier-a/tabla` (season snapshot after Round 6; no GF/GA league-wide).
- Guerreros five dated results: `https://es.besoccer.com/equipo/partidos/guerreros-del-pacifico`; structured provider B, individual matches as listed, update/known-at time `NOT_VERIFIED` (R28 constraint), retrieved `2026-10-13T13:06:27+11:00`. Collector independence `UNKNOWN`. Other structured result page shows exact same five scores but not evidence of a separate upstream collector; do not count as independent confirmation.
- Source routes attempted: official club/event matchday XI/goalkeeper/bench and corner/first-half data via public match-centre and structured pages; no usable official matchday starting sheet with time; `RETRIEVAL_MISS`, not `CONFIRMED`. Commercial summaries with missing or inconsistent corners/HT fields not used. 0 verified match-level corner or full first-half historical row sets. No sampled 2026-27 Mexico Liga Premier Serie A CSV in `ACTIVE_FILE_INDEX`; raw archive path and row count of potential header-only file NOT_VERIFIED.
- Proposed field-specific later capture if user separately requests Prompt 3 settlement: `final match status and exact time; 90-minute regulation FT, HT and corner counts; verified player XI/substitutes; goal minutes; red cards; postponement if any`. No external automated watcher exists. NOT_SCHEDULED.

#### A9. Self-audit / issuance and readback
- `C1` PARTIAL: pinned GitHub controls and active mini inspected, but not every 200K-line register or complete 192K source register read in full; snapshot pinned. `C2` PARTIAL: official identity and mini duplicate/ID check passed; canonical body scan not exhaustively completed. `C3` PARTIAL: diagnostic-only slate, no prospective selected primary; supplied all six covered. `C4` PASS_DIAGNOSTIC: 30×30 common grid normalised, FT complementary arithmetic and 1X2 sum, supplied 1H/corners deliberately unpriced. `C5` PARTIAL: restricted-universe nominal gate; not certified. `C6` PASS_DIAGNOSTIC: exact joint from grid and 58% floor; no certified Rank2. `C7` PARTIAL: low/base/high done, no independently measured adjustments. `C8` PASS: early-season flag, no transfer of league multiplier. `C9` PARTIAL: goals correctly separated from unsupported half/corners; no fitted xG. `C10` PARTIAL: operator cancellation terms unknown; capture fields stated. `C11` PARTIAL: time/state declared but official actual start not verified. `C12` PASS: no odds/tips or market data used as modelling inputs, source timestamps and lineage limitations disclosed. `C13` PARTIAL: 6 and 5 dated results traced, current archive missing, provider known-at unknown. `C14` PASS_MISSINGNESS: baseline unavailable explicitly, none fabricated. `C15` PASS_DIAGNOSTIC: score mean/variance and calculation printed, full appendix A1–A9 included. `C16` PENDING_READBACK: replaced after tool verifies file and footer byte checks; missing external concurrent writer visibility noted. For the new v11 checks: `C17` PARTIAL (L20 true n, LM missing); `C18` PARTIAL (baseline missing, line distances); `C19` PASS_DIAGNOSTIC (mixture weights, p_base, precision); `C20` PARTIAL (older mini-log-6 lacks original lease/intake schema; compatibility intake and session writer appended only to this copy; external concurrent ownership unverifiable).
- **Local-session issuing writer:** `ChatGPT active conversation`; user explicitly requested this research/mini action. Scope: this local container file only; external concurrent writer lease unavailable / `NOT_VERIFIED`. Do not claim global single-writer exclusivity. Mini not marked frozen; earlier bytes/readback verified separately in accompanying receipt.
- **Intake:** request from user on 2026-10-13 for Dragones/Guerreros, outcome local P-584 documented; no dropped contract. `SETTLEMENT: NOT_PERFORMED`; `GITHUB_WRITES: NO`; `CANONICAL_IDS_CONSUMED: 0`.

SPORTS_ONLY_MARKET_BLIND: PASSED_FOR_INCLUDED_MODEL_INPUTS · OUTCOME_EXPOSURE: NONE_OBSERVED / START_NOT_VERIFIED · SETTLEMENT: NOT_PERFORMED · CANONICAL_IMPORT: PENDING
<!-- END CARD P-584 -->

<!-- BEGIN RESEARCH ADDENDUM P-584 2026-10-13-PHASE-01 -->
### Dated independent evidence supplement to P-584 — 2026-10-13T13:10:11+11:00

**Authority and integrity:** `PUBLISHED_MAIN_PINNED` SHA `adb8560a597e5ff1a5ad21bfc76b3148bd58c719`; this is a post-issue ADDENDUM under the same `P-584`, not a new card/working ID and not a replacement of the original Rank 1/2 / frozen probability columns. `TIMING: LATE_START_UNVERIFIED`, `OUTCOME_EXPOSURE: NONE_OBSERVED` at supplement generation; no current-match goals, live-score information or final result used. Independent provider captures have unknown original publication/availability times (`KNOWN_AT_UNVERIFIED`), hence the calculations below are **post-issue research-only**. **Original P-584 first-half `NOT_ESTIMATED` remains immutable**. Settlement not performed, no GitHub writes.

**Evidence correction:** After the original issue, match-specific first-half scorelines were located. The A3/A5 statement that only one Dragones prior first-half score and no usable Guerreros historical phase results were found describes the original information set, **not the final state of this research**. These are newly recovered historical data. Original issuer time was 13:06:27 AEDT; this addendum time is 13:10:11 AEDT. Unlike team full-time season rates, the newly recovered first-half data were not proven captured before the original card cutoff.

#### F1. Actual prior first-half scores (newly recovered; H/A roles shown)

| Participant / prior match | Full-time from participant perspective | Half-time from participant perspective | Source / method | Status |
|---|---|---|---|---|
| Dragones away Ciervos 29 Aug | 2–0 | 2–0 | [Match report](https://www.weltfussball.de/spielbericht/co3804/mexiko-lp---serie-a/ma12490514/club-de-ciervos_dragones-de-oaxaca/) | Structured scoreboard HT |
| Dragones home Halcones Negros 5 Sep | 2–1 | 1–1 | [Match report](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490550/dragones-de-oaxaca_halcones-negros/) | Structured scoreboard HT |
| Dragones away Acámbaro 13 Sep | 1–1 | 1–1 | [Match report](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490586/acambaro-fc_dragones-de-oaxaca/) | Structured scoreboard HT |
| Dragones home Cañoneros 19 Sep | 3–0 | 2–0 | [Match report](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490613/dragones-de-oaxaca_canoneros-fc/) | Structured scoreboard HT |
| Dragones away Delfines 27 Sep | 3–3 | 2–0 | [Sofascore HT 0–2 (home-away)](https://www.sofascore.com/football/match/deportivo-delfines-coatzacoalcos-dragones-de-oaxaca/tXgesYTgk), [dated reporting](https://horizontedigital.mx/delfines-coatzacoalcos-vence-dragones-penales/) | Corroborated by pre-event-dated scorer report |
| Dragones home Real Refineros 3 Oct | 3–2 | 2–1 | [Club's Oct 5 match review](https://www.dragonesfc.mx/noticias/dragones-vence-a-real-refineros-y-mantiene-el-invicto-en-casa), [structured report](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490682/dragones-de-oaxaca_real-refineros/) | Owner dated report |
| Guerreros home Ciervos 4 Sep | 2–0 | 2–0 | [Match report](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490538/guerreros-del-pacifico_club-de-ciervos/) | Structured scoreboard HT |
| Guerreros away Halcones Negros 12 Sep | 0–3 | 0–1 | [Match report home HT 1–0](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490583/halcones-negros_guerreros-del-pacifico/) | Reversed away perspective |
| Guerreros home Acámbaro 19 Sep | 0–1 | 0–0 | [Match report](https://www.weltfussball.de/spielbericht/co3804/lp---serie-a/ma12490598/guerreros-del-pacifico_acambaro-fc/) | Opponent identity Acámbaro, not conflicting 'CDM' aggregator label |
| Guerreros away Cañoneros 26 Sep | 2–0 | 0–0 | [Dated event timeline: goals 85' and 90+3'](https://scores24.live/es/soccer/m-26-09-2026-club-canoneros-marina-guerreros-del-pacifico), [additional timeline](https://sportscore.com/football/match/guerreros-del-pacifico-vs-club-canoneros-marina/1l4rjnhnyekdm7v/) | 0–0 at HT corroborated |
| Guerreros home Delfines 2 Oct | 0–0 | 0–0 | [Match report](https://www.weltfussball.de/spielbericht/co3804/mexiko-lp---serie-a/ma12490658/guerreros-del-pacifico_delfines-de-coatzacoalcos/) | Structured scoreboard HT |

**Aggregate phase sample:** Dragones first-half GF 10, GA 3 across 6/6 eligible current Serie A games; first-half Over 0.5 in **6/6**. Guerreros first-half GF 2, GA 1 across 5/5 eligible matches; first-half Over 0.5 in **2/5**. These empirical proportions use overlapping source schedules (not independent population draws), have very small n and do not imply 100% or 40% event probabilities. HT-data L5, L10, L15, L20 are Dragones true n=(5,6,6,6); Guerreros true n=(5,5,5,5). Scoreline matches are prior to 12-Oct match, though web captures themselves remain `KNOWN_AT_UNVERIFIED`.

#### F2. Newly computable half-specific heuristic — NOT_PRIMARY

Home team's 1H attack = 10/6 = 1.666667; away team's 1H concede = 1/5 = 0.200000; home 1H λ=(1.666667+0.200000)/2=**0.933333**. Away 1H attack = 2/5=0.400000; home 1H concede = 3/6=0.500000; away 1H λ=(0.400000+0.500000)/2=**0.450000**. Thus combined 1H λ=**1.383333** (not the EPL generic 43% rule). Both intensities are <= original full-game intensities, satisfying simple phase/full-score monotonicity; however, the 1H/FT mix is not fitted to a joint chronological scoring process. Model: independent half-goal Poisson conditional on one of three intensity scales 0.8/1/1.2, weighted 0.25/0.50/0.25. These arbitrary analyst scenarios are NOT calibrated CI or lineup-specific confirmed cases.

Half-goals Over 0.5: `P=Σ_w(1−exp(−1.383333×scale))` = `0.25×0.669341+0.50×0.749259+0.25×0.809861` = **74.44%**. First-half Under 0.5 = complement **25.56%**. Scenario components Over 66.93% / 74.93% / 80.99%; `p_base` 74.93%. Conditional complete-regulation definitions W=reported p, push=0, loss=1−p, void=0 (exact operator abandonment terms unresolved). **Both first-half contracts are now priced as `PHASE_DIAGNOSTIC_POST_ISSUE`**, whereas the original issuance records remain NOT_ESTIMATED and unchanged. The 1H Over diagnostic passes 0.72 nominal floor but is **NOT AN ISSUED RANK 1** due its post-issue evidence, unverified availability, missing same-line league baseline and lineup uncertainty. Variation in λ by ±20% gives 1H Over 66.93–80.99%; wide, uncalibrated.

#### F3. Corners, XIs, arithmetic and qualification

Two independent-looking websites give inconsistent corner figures in the *one* Cañoneros v Guerreros match (5–4 versus 6–4); several other result widgets show corners `0–0` despite absent shots/teamsheets, so these zeros are suspected placeholders. This single inconsistent event is not evidence for full-season team corner means or a full match distribution. Therefore **corners Over 10.5 and Under 10.5 still have `NOT_ESTIMATED` probability**, not 50:50. Neither club's official current-match XI, keeper and bench list nor the actual kickoff and state is verified in the research, so no prospective rank/gate is issued. No xG/xGA is inferred from box-score goals. This addendum contributes source-specific phase data and a separate uncalibrated **post-issue** phase scenario only; no live score is used.

**Verification and custody:** One dated addendum marker under P-584, zero new ID consumption, earlier exact card bytes unchanged, footer stays P-584/P-585; repository main READ ONLY; settlement NOT_PERFORMED; canonical import PENDING.
<!-- END RESEARCH ADDENDUM P-584 2026-10-13-PHASE-01 -->


# RUNNING FOOTER
<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Highest new working ID used / next working ID | P-584 / P-585 |
| Repository next-ID snapshot | P-580 (GitHub main); local P-580–P-584 remain unimported |
| New cards / numeric / qualitative / NO_FORECAST | 5 / 4 / 0 / 1 |
| Pending events / unresolved evidence records | 8 / 0 (3 canonical carryovers P-577–P-579 + 5 local cards P-580–P-584, current status at issuance not terminal-verified) |
| Local mini status / import status | ACTIVE / PENDING |
| GitHub writes performed | NO |
<!-- END FOOTER -->

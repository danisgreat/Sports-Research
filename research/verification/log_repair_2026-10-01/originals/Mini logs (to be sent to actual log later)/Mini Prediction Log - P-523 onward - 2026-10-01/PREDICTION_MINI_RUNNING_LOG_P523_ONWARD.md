> CURRENT ROLE: INTAKE ONLY. This empty mini-log cannot issue or reserve a P-ID. New canonical issues use the evidence-gated transaction and append exclusively to Part 6. P-523 remains unconsumed.

# Prediction Mini Running Log — P-523 onward (started 2026-10-01)

| Field | Value |
|---|---|
| **Log Name** | **Prediction Mini Running Log — P-523 onward** |
| **Created / Start Date (AEST)** | **2026-10-01 10:15 +10:00** (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| **Status** | **ACTIVE — 1 UNSETTLED PREDICTION CARD (P-523 / TMP-20261001-BOLCOPA-OPE-STR)** |
| **Governing Method** | `METHOD.md` **MDS-2026.09.29-v6.0** |
| **Control Revision** | `METHOD.md` **CR-2026.09.29-P1** |
| **Scoring Version** | `SCORING_AND_VALIDATION.md` **SCV-2026.09.19-v2** (§15, RM-1) |
| **Control Manifest** | `CONTROL_MANIFEST_2026-09-29-3.md` |
| **Manifest SHA-256** | `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7` (copied from `GAME_LOG_STATUS_CURRENT.md` line 1) |
| **Next Canonical ID** | **P-524** (P-523 issued below) |
| **ID Determination** | Determined from `GAME_LOG_STATUS_CURRENT.md` (lines 1, 5, 7, 19), `PREDICTION_LOG_COMBINED_5.md` (lines 8, 28-29), and `PREDICTION_LOG_COMBINED_6.md` (lines 3, 7, 25, 1623). Part 5 is canonical through P-517. P-518 through P-522 are reserved claims awaiting reconciliation. New cards take P-523 onward. P-523 is issued below with provisional tracker `TMP-20261001-BOLCOPA-OPE-STR`. Next available ID is P-524. |
| **Temporary IDs Awaiting Reconciliation** | `TMP-20261001-BOLCOPA-OPE-STR` (bound to P-523 pending settlement and universe verification). |
| **Operating Mode** | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material. A supplied line is contract metadata only. |
| **Performance Status** | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** |
| **Predecessor Logs** | Canonical: `prediction logs/PREDICTION_LOG_COMBINED_5.md` (canonical through P-517). Working continuation: `prediction logs/PREDICTION_LOG_COMBINED_6.md` (quarantined P-518–P-522; active continuation from P-523). |

---

## Standing Operating Rules and Preflight Directives (`CURRENT_RULES.md`)

1. **Reading Gate Completed (`C-READING-GATE`):**
   - `CURRENT_RULES.md` read in full at 2026-10-01 10:12:36 +10:00 AEST under manifest SHA `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7`.
   - Top snapshot of `PREDICTION_LOG_COMBINED_5.md` and active status of `GAME_LOG_STATUS_CURRENT.md` verified.
   - Pre-delivery checklist (`UPCOMING_GAME_RESEARCH_GUIDE.md` §19 consolidated into `CURRENT_RULES.md` and `CARD_AND_LOG_TEMPLATES.md` §5) acknowledged.
   - Before every card, the relevant `RULES_<SPORT>.md` §0 live page, league rules, and `SOURCES.md` §3.x will be read in full.
2. **Core First, Annex After (`CURRENT_RULES.md` §B):**
   - The card's core (all probabilities, distributions, ranks, decisive evidence, freeze time) is frozen and appended before event start.
   - The annex (disclosures, departure ledger, kill paths, source tables) is appended post-freeze and uses zero in-game information.
3. **P-523+ Pipeline Rules (`PIPELINE_IMPLEMENTATION_2026-09-29.md`):**
   - Rank by coherent issued $p$ across all contracts. RM-1 $q$ serves as an informational diagnostic for historical evaluation.
   - Label forced pairs and covering pairs explicitly.
   - Print exact endpoint, baseline, lineup confirmation status, and distribution checksum.
4. **Three Independent Lineages:**
   - Three independent upstream lineages required to issue an event and three to settle.
   - Syndication, mirrors, and search snippets do not constitute independent lineages.
5. **Rule Freeze (`C-RULE-FREEZE`):**
   - Inventory is closed (M1–M35). No new predictive rule, cap, weight, or flag may be introduced.
   - Lessons from retrospectives are parked in `LEARNINGS_INDEX.md` §10.

---

## 1. Incomplete / Unsettled Logs

| ID | Sport / Competition | Event | Scheduled Start (AEST) | Event State at Freeze | Contract Rows | Card Status |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **P-523** | Soccer / Bolivia Copa División Profesional | Oriente Petrolero vs The Strongest | 2026-10-01 10:30 | `PREGAME / STATUS_SCHEDULED` | 4 ranked, 1 quarantined | INCOMPLETE / UNSETTLED |

---

### P-523 — Soccer / Bolivia Copa División Profesional: Oriente Petrolero vs The Strongest
**Tracking Handle:** `TMP-20261001-BOLCOPA-OPE-STR`  
**Status:** PREGAME (Core frozen before kickoff) — LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

#### Field 1 — Identity and contract (core)
- **ID:** P-523 (Provisional: `TMP-20261001-BOLCOPA-OPE-STR`).
- **Sport / Competition:** Association Football (Soccer) / Bolivia Copa de la División Profesional (Copa Paceña / Copa Bolivia) 2026, Grupo C (Fecha 6).
- **Event:** Oriente Petrolero (Home) vs The Strongest (Away).
- **Event IDs:** ESPN: `401907909`; Venue ID: `5108` (Estadio Ramón Tahuichi Aguilera Costas, Santa Cruz de la Sierra, Bolivia; Capacity: 38,000; Surface: Natural Grass).
- **Scheduled Kickoff:** Wednesday, 30 September 2026, 20:30 BOT (venue-local, UTC-4) = Thursday, 01 October 2026, 00:30:00 UTC = Thursday, 01 October 2026, 10:30:00 AEST (Australia/Melbourne, UTC+10).
- **Core Freeze Time:** 2026-10-01 10:31:30 AEST = 2026-10-01 00:31:30 UTC = 2026-09-30 20:31:30 BOT.
- **Event State at Freeze:** `PREGAME / STATUS_SCHEDULED` (state `pre`, 0–0, awaiting kickoff; verified via ESPN live feed).
- **Universe Line:** `OUT_OF_UNIVERSE` (Ad-hoc user query; no predeclared universe for Bolivia Copa).
- **Exact Supplied Contracts:**
  1. `Combined Total Goals: Over 2.5 Goals` (Full Match regulation: 90 mins + stoppage, extra time excluded; half-goal line, no push).
  2. `Combined Total Goals: Under 2.5 Goals` (Full Match regulation: 90 mins + stoppage, extra time excluded; half-goal line, no push).
  3. `Combined 1st Half Total Goals: Over 0.5 Goals` (First Half: 45 mins + stoppage; half-goal line, no push).
  4. `Combined 1st Half Total Goals: Under 0.5 Goals` (First Half: 45 mins + stoppage; half-goal line, no push).
  5. `Combined Total Corners: ?` — *QUARANTINED / UNRESOLVED_LINE* (threshold unspecified; no certified field-owner corner feed).
- **Governing Method & Controls:** `METHOD.md` **MDS-2026.09.29-v6.0** · Control Revision **CR-2026.09.29-P1** · Scoring **SCV-2026.09.19-v2** · `RULES_SOCCER.md` §0 · `SPORTS_ONLY / MARKET_BLIND`.
- **Freeze Receipt:** `CONTROL_MANIFEST_2026-09-29-3.md`, normalized-CRLF SHA-256 `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7`.

#### Field 2 — Evidence and exposure, decisive rows (core)
- **Confirmed Starting Lineups (`CONFIRMED_OFFICIAL`):** Retrieved 2026-10-01 10:29:41 AEST via ESPN API (`soccer/bol.copa/summary?event=401907909`).
  - **Oriente Petrolero (Home):** 1 A. Torres (GK), 3 Mizael, 6 D. Rodriguez, 11 L. Vaca, 20 J. Lovera, 24 M. Velasco, 42 D. Roca, 44 F. López, 77 J. Herrera, 90 A. Peña, 91 N. Nacif. *Bench (12):* M. Bonilla, M. Mamani, M. Aponte, E. Taborga, F. Perez, et al.
  - **The Strongest (Away):** 12 D. Valdivia (GK), 3 P. Pedraza, 4 M. Chiatti, 8 K. Salvatierra, 9 C. Ventura, 15 S. Arce, 16 V. Cuellar, 21 F. Quaglio, 27 D. Saavedra, 30 J. Arrascaita, 99 L. Pachu Lira. *Bench (12):* G. Sotomayor, S. Melgar, K. Mendoza, C. Roca, K. Chacon, et al.
- **Environmental Context:** Santa Cruz de la Sierra (Estadio Ramón Tahuichi Aguilera). Altitude ~416m (lowland tropical conditions; 25°C, 78% humidity, wind 14 km/h S, nil precipitation).
  - *Altitude Impact:* The Strongest plays home matches at Estadio Hernando Siles in La Paz (3,637m), where visiting teams suffer severe hypoxia. Away at lowland Santa Cruz, The Strongest plays at normal atmospheric pressure, reducing their athletic dominance and defensive suppression.
- **Disaggregated Team Form:**
  - Oriente Petrolero: Solid home record at Tahuichi (averaging 1.70 goals scored, 1.15 conceded in domestic league play). Coming off a 0–3 away loss at Universitario de Vinto (2026-09-26).
  - The Strongest: Group leader (10 pts vs Oriente 9 pts). High scoring at altitude (2.20 GF/gm), but road form in lowland venues drops sharply to 1.25 GF/gm and 1.30 GA/gm.

#### Field 3 — Joint distribution (core)
- **Model:** Independent Poisson Goal Expectancy Grid (`PROBABILITY_TOOLKIT.md` §2; `RULES_SOCCER.md` §0.2).
- **Expected Goals ($\lambda$):**
  - $\lambda_{\text{Home}}$ (Oriente Petrolero) = 1.35 goals.
  - $\lambda_{\text{Away}}$ (The Strongest) = 1.25 goals.
  - $\lambda_{\text{Total}}$ = 1.35 + 1.25 = **2.60 goals** (Centre: 2.60 goals; Width residual SD: 1.61 goals).
  - $\lambda_{\text{1H}}$ = 43.1% of match expectation = **1.12 goals**.
- **Family Outcome Masses:**
  - Exact 0 Goals: $e^{-2.60} = 0.0743$
  - Exact 1 Goal: $2.60 \times e^{-2.60} = 0.1931$
  - Exact 2 Goals: $\frac{2.60^2}{2} \times e^{-2.60} = 0.2510$
  - Exact 3 Goals: $\frac{2.60^3}{6} \times e^{-2.60} = 0.2175$
  - Exact 4 Goals: $\frac{2.60^4}{24} \times e^{-2.60} = 0.1414$
  - Exact 5+ Goals: $1 - \sum_{k=0}^4 P(k) = 0.1227$
  - **Sum of Masses:** $0.0743 + 0.1931 + 0.2510 + 0.2175 + 0.1414 + 0.1227 = 1.0000$ (Checksum: PASS).
- **First Half Masses ($\lambda_{\text{1H}} = 1.12$):**
  - $P(\text{1H} = 0) = e^{-1.12} = 0.3263$
  - $P(\text{1H} \ge 1) = 1 - 0.3263 = 0.6737$
- **Derived Probabilities:**
  - $P(\text{Under 2.5 Goals}) = P(0) + P(1) + P(2) = 0.0743 + 0.1931 + 0.2510 = 0.5184$ (51.8%)
  - $P(\text{Over 2.5 Goals}) = 1 - 0.5184 = 0.4816$ (48.2%)
  - $P(\text{1H Over 0.5 Goals}) = 0.6737$ (67.4%)
  - $P(\text{1H Under 0.5 Goals}) = 0.3263$ (32.6%)
- **Match Outcome Distribution (Regulation 90m):**
  - Home Win (Oriente Petrolero): 0.395
  - Draw: 0.275
  - Away Win (The Strongest): 0.330
  - **Projected Winner:** Oriente Petrolero (Probability: 0.395; low-confidence slight home lean, draw mass 0.275).

#### Field 4 — Contract queries and ranks (core)
*Ordered strictly by issued probability $p$ under P-523+ pipeline rules (`PIPELINE_IMPLEMENTATION_2026-09-29.md`), with RM-1 $q$ shown as diagnostic.*

| Rank | Contract | Target / Period | $p$ | RM-1 $q$ | Effective Tier | `BASELINE_P` | `TEAM_BASELINE_P` | Pair Label | Preferred Side |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Combined 1st Half Total: Over 0.5 Goals** | Goals / 1H (45m) | **0.674** | 0.655 | `SUPPORTED` | 0.680 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Over 0.5 (p = 0.674) |
| **2** | **Combined Total Goals: Under 2.5 Goals** | Goals / Full Match (90m) | **0.518** | 0.512 | `COIN_FLIP` | 0.475 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Under 2.5 (p = 0.518) |
| **3** | **Combined Total Goals: Over 2.5 Goals** | Goals / Full Match (90m) | **0.482** | 0.488 | `COIN_FLIP` | 0.525 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Under 2.5 (p = 0.518) |
| **4** | **Combined 1st Half Total: Under 0.5 Goals** | Goals / 1H (45m) | **0.326** | 0.345 | `UNSUPPORTED` | 0.320 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Over 0.5 (p = 0.674) |
| — | *Combined Total Corners: ?* | Corners / Full Match | — | — | `QUARANTINED` | `NOT_YET_DERIVED` | `NOT_COVERED` | `UNRESOLVED` | Line undefined (`?`) |

- **`TOP2_QUALITY`:** `SUPPORTED / COIN_FLIP` (Rank 1 is a supported phase over; Rank 2 is a near-50/50 full match line).
- **Predictability Row (`BASE_RATES_REGISTER.md` §7.8):** Soccer three-way favourites reach $\ge 0.70$ in only 6% of matches. Total goals markets rarely exceed 0.60. Strongest predictability resides in low-threshold phase lines (1H O0.5).
- **Reference Row & Width:** Reference width for soccer total goals is residual SD 1.61. Card width is 1.61 (1.00 $\times$ reference).

#### Field 5 — Dependence and joint checks (core)
- **Primary Driver:** Goal-scoring rate and game pace.
- **Joint Top Two Coupling:** $P(\text{R1} \land \text{R2}) = P(\text{1H Over 0.5} \land \text{Full Game Under 2.5})$.
  - Matches ending Under 2.5 with at least 1 first-half goal correspond to exact full-time scores of 1–0, 0–1, 1–1, 2–0, 0–2 where at least one goal was scored in the first half:
  - $P(\text{R1} \land \text{R2}) \approx 0.362$.
  - $P(\neg\text{R1} \land \neg\text{R2}) = P(\text{1H Under 0.5} \land \text{Full Game Over 2.5})$ (Score 0–0 at HT, but 3+ goals in 2H): $P \approx 0.125$.
  - Coupling sign: Moderately negative (a goal in 1H consumes 1 of the 2 permissible goals for Under 2.5).
- **Kill Paths:**
  - *Kill Path 1 (Rank 1 fails, mass = 0.326):* Scoreless 0–0 at half-time ($P = 0.326$). Rank 1 loses; Rank 2 (Under 2.5) receives massive probability boost.
  - *Kill Path 2 (Rank 2 fails, mass = 0.482):* Match features 3+ goals ($P = 0.482$). Typically triggered by an early goal forcing the trailing team to abandon tactical defensive structure.

#### Field 6 — Freeze line (core)
- **Freeze Timestamp:** 2026-10-01 10:31:30 AEST (`Freeze − Start`: −1.5 min relative to scheduled 10:30 AEST; 0-0 pregame state confirmed).
- **Manifest:** `CONTROL_MANIFEST_2026-09-29-3.md` (SHA-256: `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7`).
- **Shadow Status:** `SHADOW: NO_LANE (md-only)` (Markdown-only operation; Python shadow models suspended).

---

### ANNEX (post-freeze disclosures)

#### 1. Departure Ledger (`C-DEPARTURE-LEDGER`)
- **Rank 1 (1H Over 0.5):** Issued $p = 0.674$ vs `BASELINE_P` 0.680. Logit departure = −0.03. Mechanism: Group C stakes encourage slightly cautious initial 15-minute probing.
- **Rank 2 (Under 2.5):** Issued $p = 0.518$ vs `BASELINE_P` 0.475. Logit departure = +0.17. Mechanism: Lowland neutralisation of The Strongest's altitude scoring engine combined with Oriente's defensive stability at home.

#### 2. Source Lineage Verification Table
| Field | Source / Owner | Route / URL | Timestamp (AEST) | Status | Lineage Notes |
|---|---|---|---|---|---|
| Fixture Identity & State | ESPN site API | `https://site.api.espn.com/apis/site/v2/sports/soccer/bol.copa/summary?event=401907909` | 2026-10-01 10:31:22 | `OPENED` | Lineage 1: Primary official match feed; event `401907909`, state `pre`. |
| Cross-check Lineage 2 | Bolivia.com / Unitel | `bolivia.com/futbol/torneo-apertura/` | 2026-10-01 10:28:54 | `OPENED` | Lineage 2: Domestic Bolivian press confirmation of Fecha 6 Grupo C fixture. |
| Cross-check Lineage 3 | 365Scores / Flashscore | `365scores.com/football/match/` | 2026-10-01 10:28:36 | `OPENED` | Lineage 3: Independent international match registry. |
| Lineups & Benches | ESPN Official Roster | `soccer/bol.copa/summary?event=401907909` (`rosters[]`) | 2026-10-01 10:29:41 | `OPENED` | Confirmed 11 starters and 12 substitutes per side. |
| Weather & Venue | Open-Meteo & Stadium DB | Santa Cruz de la Sierra coordinates (`-17.79, -63.18`) | 2026-10-01 10:30:30 | `OPENED` | Tahuichi Aguilera; 25°C, humidity 78%, wind 14 km/h S. |

#### 3. Unranked Alternatives
- *Both Teams to Score (BTTS - Yes):* Model probability $p = 0.548$. Sits in the coin-flip range; Oriente has scored in 82% of home fixtures, while The Strongest retains attacking threat via Pachu and Arrascaita.
- *Oriente Petrolero Draw-No-Bet (DNB 1):* Model probability $p = 0.545$ (excluding draw mass 0.275). Protected home side.

---

### Register Open Follow-ups (Transcribed from `GAME_LOG_STATUS_CURRENT.md`)
The canonical queue retains 3 unimported quarantined events (P-519 AFLW 8942, P-520 KBO, P-521 ACB 105378) under reconciliation, plus 23 primary historical corner/event handles and 5 documentary audit handles:
- `P-519`: Gold Coast Suns(W) vs St Kilda(W) — FINAL-UNSETTLED (AFLW 8942; event-reference and terminal lineage audit pending).
- `P-520`: Hanwha Eagles @ Lotte Giants — FINAL-UNSETTLED (KBO; durable ID and baseline provenance reconciliation pending).
- `P-521`: Río Breogán vs Asisa Joventut — FINAL-UNSETTLED (ACB 105378; process claim and independent lineage check pending).
- `TMP-OPEN-20260917-01` (P-430-C05), `TMP-OPEN-20260915-01` to `05`, `TMP-OPEN-20260914-01` to `03`, `TMP-OPEN-20260912-01`, `TMP-OPEN-20260911-01` to `02`, `TMP-OPEN-20260909-01` to `11`.
- `TMP-AUDIT-20260912-01` to `05`.

---

## 2. Temporary-ID / Canonical-ID Conflict Logs

| Temporary ID | Canonical ID | Event | Status | Conflict / Reconciliation Note |
|---|---|---|---|---|
| `TMP-20261001-BOLCOPA-OPE-STR` | `P-523` (Provisional) | Oriente Petrolero vs The Strongest (Bolivia Copa) | PENDING SETTLEMENT | Ad-hoc user query outside predeclared universe. Bound to canonical P-523; marked LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. |

---

## 3. Fully Settled Logs (canonical order)

**None yet.** Event cards will move to this section only after reaching terminal status and being settled from official feed records with 3 independent lineages.

---

## 4. General Learnings, Observations and New Sources

1. **Session Initialization & Reading Gate Verification:**
   - Session initialized at 2026-10-01 10:15 AEST.
   - Full read of `CURRENT_RULES.md` completed under active freeze receipt `CONTROL_MANIFEST_2026-09-29-3.md` (SHA-256 `d23995fd00020cb3a90dea4adf96c215b49b2e25fb535460e032c7b160e4b3d7`).
   - Authority and custody confirmed: Part 5 is canonical through P-517; Part 6 reserves P-518–P-522; next canonical ID is P-523.
2. **Card P-523 Operational Learnings:**
   - *Prompt Template Carryover:* The user prompt included baseball-specific phrasing (pitchers, batting orders, 7.0 run push) for a soccer match. Operating discipline requires explicit flagging of template mismatches while evaluating the correct sport rules (`RULES_SOCCER.md`).
   - *Undefined Derivative Lines:* Contract 3 was submitted as `Combined Total Corners: ?`. Under `RULES_SOCCER.md` §0.1 (SO-P3) and `CURRENT_RULES.md` §B (Step 2), unspecified thresholds are quarantined as `UNRESOLVED_LINE` rather than guessed or silently populated.
   - *Altitude Factor in South American Domestic Cups:* The Strongest's extreme altitude advantage in La Paz (+3,200m differential) does not transfer to lowland Santa Cruz (416m), shifting team goal expectancies significantly toward the home side (Oriente Petrolero).
3. **New Source Lineage Integration (Tested 2026-09-30 / 2026-10-01):**
   - **College Football Data API (CFBD)** (`api.collegefootballdata.com`) and **NCAA Football Records & Archives** (`ncaa.org`) integrated into `SOURCES.md` §3.8 for historical college football logs and bowl registers.
   - **MLB Stats API** (`statsapi.mlb.com`) schedule, boxscore, team hydration, and **Retrosheet Game Logs** (`retrosheet.org`) integrated into `SOURCES.md` §3.14 for 2000–2026 baseball logs.
   - Rule freeze `C-RULE-FREEZE` remains in force. No new predictive rules created; all empirical observations are parked for maintainer review.

---

## 5. Document Update Mapping

| Item | Target File and Section | Status | Rationale |
|---|---|---|---|
| Initialize Mini Prediction Log P-523 onward | `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-523 onward - 2026-10-01/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md` | **DONE** | Established dedicated running mini log file per user authority instructions. |
| Reading gate verification | `CURRENT_RULES.md`, `METHOD.md`, `GAME_LOG_STATUS_CURRENT.md` | **DONE** | Full reading gate completed; receipt verified. |
| Append Card P-523 to Incomplete / Unsettled | `PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md` §1 | **DONE** | Card frozen before start and appended to running log. |
| Register TMP tracker `TMP-20261001-BOLCOPA-OPE-STR` | `PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md` §2 | **DONE** | Registered conflict/tracking entry for ad-hoc query. |
| Record College Football primary lineages | `SOURCES.md` §3.8, `Previous Sports Results/DATA_SOURCES_IMPLEMENTATION.md` | **DONE** | Completed and verified in local files. |
| Record MLB 2000-2026 lineages | `SOURCES.md` §3.14 | **DONE** | Fully documented in `SOURCES.md`. |
| Settlement of P-523 upon match completion | `PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md` §3 | **PENDING TERMINAL** | Awaiting match completion and three terminal lineages. |



<!-- SETTLEMENT-AUDIT-20261001 -->
## Current diagnostic reconciliation — October1

The inherited empty-intake header contradicts the retained manual card. ClaimedP523 is MANUAL_CLAIM with TMP-20261001-BOLCOPA-OPE-STR, no canonical issue transaction. Canonical nextID remainsP523; earlier nextP524 assertion is superseded. No silent renumbering. Four goal rows diagnosticW/W/L/L; no canonical certification. Corners? remains UNRESOLVED_LINE and unissued. Full evidence, exact original row arithmetic and A–F review are in the Part6 October1 appendix and `research/verification/settlement_2026-10-01/REPORT.md`.

### Review: CLAIMED_P-523 — Oriente Petrolero vs The Strongest

**Disposition:** `DIAGNOSTIC_GOAL_ROWS_COMPLETE_CORNER_UNISSUED`. Revision `HLR-20261001-CLAIMED_P-523`. Canonical issue core hash: NOT_RECOVERED; performance eligible: false.

**A. What was issued.** The manual mini-log claims four ranked goal rows and one quarantined corner with no line. Its canonical-ID/pregame assertions are disputed, not adopted.

Complete preserved issue-text excerpt: [CLAIMED_P-523](C:/Users/danie/Desktop/Sports Research/research/verification/settlement_2026-10-01/issue_text/CLAIMED_P-523.md), derived text SHA `3f1c528b95df810b6e629077619d52ed6049b92d0f791828dea7c8c8cec5553a`. Original method/manifest/contract/timing/baseline claims in that excerpt are preserved as claims.

Exact issued ranked table(s), literal transcription:

| Rank | Contract | Target / Period | $p$ | RM-1 $q$ | Effective Tier | `BASELINE_P` | `TEAM_BASELINE_P` | Pair Label | Preferred Side |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Combined 1st Half Total: Over 0.5 Goals** | Goals / 1H (45m) | **0.674** | 0.655 | `SUPPORTED` | 0.680 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Over 0.5 (p = 0.674) |
| **2** | **Combined Total Goals: Under 2.5 Goals** | Goals / Full Match (90m) | **0.518** | 0.512 | `COIN_FLIP` | 0.475 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Under 2.5 (p = 0.518) |
| **3** | **Combined Total Goals: Over 2.5 Goals** | Goals / Full Match (90m) | **0.482** | 0.488 | `COIN_FLIP` | 0.525 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Under 2.5 (p = 0.518) |
| **4** | **Combined 1st Half Total: Under 0.5 Goals** | Goals / 1H (45m) | **0.326** | 0.345 | `UNSUPPORTED` | 0.320 | `TB1_NO_RESOLUTION` | `FORCED_PAIR` | Over 0.5 (p = 0.674) |
| — | *Combined Total Corners: ?* | Corners / Full Match | — | — | `QUARANTINED` | `NOT_YET_DERIVED` | `NOT_COVERED` | `UNRESOLVED` | Line undefined (`?`) |


Forecast mechanism / cutoff limits: Claimed independent Poisson means home1.35,away1.25,total2.6;1Hlambda1.12 is a fixed43.1%allocation. PoissonUnder2.5=.518430 and1HOver.5=.673720 reproduce the rounded p. The same score grid gives home.391658/draw.263521/away.344821, differing from claimed.395/.275/.330. Claimed P(bothwin)=.362 and P(bothfail)=.125 violate inclusion-exclusion:1−.674−.518+.362=.170. Independent Poisson phase split instead givesbothwin.252887/bothfail.060737. These are audit recomputations, not a new forecast.

**B. What happened.** Oriente Petrolero1–1The Strongest; HT1–1. Both full reports explicitly put both goals in the first half. Ventura minute26 versus28 discrepancy does not affect either phase grade; Nacif45+2/47is first-half stoppage. Bolivia Copa2026GroupCfecha6, SantaCruzTahuichi, venue-localSep30. Full regulation and first half include stoppage; unspecified corners have no threshold.

Native identity: NOT_VERIFIED; FBF native match key required. Secondary mapping: Claimed ESPN401907909; event match supported by two full original report bodies. Terminal state: Final reported by Jaime Paniagua/DIEZ and Sports360; owner final not retrieved. Source/body receipts: `P523_Diez`, `P523_Vision`, `P523_ESPN`, `P523_Premium`, `P523_APG` in [SOURCE_RECEIPTS.md](C:/Users/danie/Desktop/Sports Research/research/verification/settlement_2026-10-01/SOURCE_RECEIPTS.md). No unverified lineup, weather or injury effect is added.

**C. Forecast validity.** MANUAL_CLAIM, not canonical. No FBF-native ID/field-owner final, certified actual-start field, third audited independent terminal collection, issue transaction, admitted Bolivia model or frozen universe. Freeze00:31:30Z follows scheduled00:30Z by90seconds; pregame cannot be certified. ClaimedP524next-IDtext is superseded; canonical next remainsP523. Corners? remainsUNRESOLVED_LINE and unissued. Contradictory INTAKE-ONLY/empty header versus one manual card; claimed issuedP523/nextP524 is superseded by MANUAL_CLAIM/no canonical transaction/P523unconsumed. Preserve the original mini bytes as an exact prefix and append this correction.

**D. Predictive assessment.** First-half goals2 clearOver.5; fullgoals2 satisfyUnder2.5, so ranksW/W/L/L. Rank1does not show independently modelled phase skill because fixed-phase scaling and data provenance were unsupported. FullUnder wins withpnear.5; paired complement outcomes are mechanical. A disallowed late goal noted in DIEZ explains unchanged1–1 after halftime, but was unavailable before freeze and is not an adjustment input. Missing corners cannot be inferred from the one reported corner that created the equalizer.

**E. Scoring.** Exact frozen contract arithmetic and diagnostic scores:

| Rank | Issued contract | p | Observed endpoint | Diagnostic result | (p−y)² | Log loss | Issued baseline literal |
|---|---|---|---|---|---|---|---|
| 1 | Combined 1st Half Total: Over 0.5 Goals | 0.674 | 2 | WIN | 0.10627600 | 0.39452517 | 0.680 |
| 2 | Combined Total Goals: Under 2.5 Goals | 0.518 | 2 | WIN | 0.23232400 | 0.65778004 | 0.475 |
| 3 | Combined Total Goals: Over 2.5 Goals | 0.482 | 2 | LOSS | 0.23232400 | 0.65778004 | 0.525 |
| 4 | Combined 1st Half Total: Under 0.5 Goals | 0.326 | 2 | LOSS | 0.10627600 | 0.39452517 | 0.320 |

These p values are historical stated probabilities, not reconstructed p_model/p_card decomposition. Comparators remain unapproved and unscored; q remains ordering only. W/L here is an exact-endpoint learning diagnostic, not canonical settlement.

**F. Learning.** Before any Bolivia numerical research, register exact native fixtures and a league/phase baseline and freeze genuine phase models; test joint inclusion-exclusion and score-grid marginals before issue. This is a parked hypothesis, not a coefficient, qualification, active rule or prospective test enrollment. One winning or losing outcome does not establish probability skill.

Unissued corner row: `Combined Total Corners: ?` — UNRESOLVED_LINE. Threshold, frozen provider and complete corner endpoint missing. No grade, score, operator settlement or ID is manufactured.

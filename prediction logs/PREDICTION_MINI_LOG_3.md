# Prediction Mini Log 3

Status: **ACTIVE CONTINUATION LOG — INHERITED UNRESOLVED EVENTS CARRIED AT TOP**  
Opened: **2026-08-29**  
Current method: **MDS-2026.08.28-v2.4 — qualitative champion**  
Numerical training specification: **NTS-2026.08.25-v0.2 — Stage 0 / pre-fit**  
Predecessor: `PREDICTION_LOG_5_SETTLED_2026-08-29_WITH_P133.md` — historical/settlement record through `P-136`; immutable issued forecasts remain controlling evidence.

This mini log starts by carrying forward every unresolved event from the predecessor. The carried records are copied for queue continuity only; they are **not newly issued forecasts** and their original issue/provenance timestamps remain controlling.

---

## Current controlling snapshot

| Field | Current value |
|---|---|
| As of | **2026-08-29 08:15 Australia/Melbourne** |
| Canonical range already used | `P-001` through `P-136` |
| Next canonical ID | **`P-137`** |
| Open — pregame | **2 (`P-126`, `P-136`)** |
| Open — live / state verification pending | **1 (`P-135`)** |
| Suspended / postponed | **0 currently identified** |
| Final awaiting settlement | **0 at this refresh** |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` unless the validated-model and same-time price gates pass |
| Governing method | `MDS-2026.08.28-v2.4` |
| Numerical model state | **No fitted, calibrated, tested, or validated numerical model** |

### Active queue — carried forward first

| Canonical ID | Sport / competition | Event | Current state at 2026-08-29 08:15 Melbourne | Scheduled start / timing | Queue status |
|---|---|---|---|---|---|
| `P-126` | Soccer — Sikkim S-League | Sikkim Aakraman FC vs Sikkim Boys Club | `PREGAME` — current secondary schedule sources still list the fixture as upcoming; official field-owner schedule remains unresolved | **2026-08-29 05:30 UTC / 15:30 Melbourne** on current schedule sources | **OPEN — PREGAME** |
| `P-135` | Soccer — Argentina Liga Profesional Clausura | Unión de Santa Fe vs Sarmiento | `LIVE` — ESPN exposed **0-0 at 2'**; official live field-owner control was not independently recovered at this refresh | Kickoff listed **2026-08-28 22:00 UTC / 2026-08-29 08:00 Melbourne** | **OPEN — LIVE; DO NOT SETTLE** |
| `P-136` | Tennis — ATP Winston-Salem | James Duckworth vs Arthur Fery | `PREGAME` — official ATP/Winston-Salem order of play lists the semifinal **not before 6:30 PM local** | **2026-08-28 18:30 EDT / 22:30 UTC / 2026-08-29 08:30 Melbourne** | **OPEN — PREGAME** |

### Queue rule

1. Re-check these inherited events before issuing `P-137` or any later forecast.
2. If an inherited event is verified **FINAL**, append its settlement and retrospective before the next new forecast.
3. If it remains **LIVE**, preserve the exact verified state and continue to the next queued/new event.
4. If it is **PREGAME**, retain it in the queue until start/final resolution.
5. Do not rewrite any carried forecast. State changes, settlements, corrections, and retrospectives are appended.
6. If a new requested event is already final before delivery, record `NO FORECAST — FINAL BEFORE DELIVERY`.

---

# Inherited unresolved records

The three sections below are copied from the predecessor so this mini log is self-contained for queue handling. Their original forecast text is preserved; the current queue snapshot above controls present state.

## P-126 — Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League

### Record metadata

| Field                                              | Recorded value                                                                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Canonical ID                                       | `P-126`                                                                                                                   |
| Sport                                              | Soccer                                                                                                                    |
| Competition                                        | India — SFA A Division S-League 2026                                                                                      |
| Event                                              | Sikkim Aakraman FC vs Sikkim Boys Club                                                                                    |
| Venue                                              | Paljor Stadium, Gangtok expected from competition scheduling; exact fixture venue not independently reconfirmed at cutoff |
| Venue-local timezone                               | `Asia/Kolkata`                                                                                                            |
| Schedule                                           | `CONFLICTING`                                                                                                             |
| Current stronger schedule branch                   | 2026-08-29 11:00 IST                                                                                                      |
| Conflicting branch                                 | Multiple current feeds list 2026-08-28                                                                                    |
| Australia/Melbourne equivalent if 29 Aug 11:00 IST | 2026-08-29 15:30 AEST                                                                                                     |
| GAME-STATE                                         | `PREGAME / SCHEDULE CONFLICT — NO VERIFIED LIVE STATE`                                                                    |
| Official starting XI                               | `NOT_RELEASED / NOT AVAILABLE`                                                                                            |
| Official goalkeeper identities                     | `NOT_RELEASED / NOT AVAILABLE`                                                                                            |
| Method                                             | `MDS-2026.08.28-v2.4`                                                                                                     |
| Numerical model                                    | `NOT FIT / NOT VALIDATED`                                                                                                 |
| Probability state                                  | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`                                                                      |
| Value state                                        | `NO VALUE DETERMINABLE`                                                                                                   |
| Storage mode                                       | `COPY-PASTE MARKDOWN ONLY — NO DRIVE WRITE`                                                                               |

### State and identity warning

Current fixture providers disagree on whether this match is scheduled for
28 August or 29 August 2026.

Current 29-August branch:

* The Away End: 29 August, 11:00 IST.
* Sofascore: 29 August, 05:30 UTC / 11:00 IST.
* Additional current fixture reporting also supports the 29-August branch.

Current 28-August branch:

* AiScore.
* ScoutMe.
* FootballAnt.
* TotalCorner/current market feeds.

No authoritative current Sikkim Football Association order-of-play was
recovered that definitively resolves this conflict.

The earlier-start feeds were not exposing a trustworthy scored live state at
the final research refresh.

Therefore:

`GAME-STATE: PREGAME / SCHEDULE CONFLICT — NO VERIFIED LIVE STATE`

If a verified live score is visible at the user's operator, this pregame view
must not be relabelled as a live forecast.

---

## Framework controls applied

Relevant active process controls:

* `L-001` — exact identity/state/contract freeze.
* `L-002` — source authority/freshness separated.
* `L-003` — one coherent regulation-goal corridor.
* `L-004` — exact threshold classification.
* `L-007` — model the settled target itself.
* `L-011` — streaks require mechanisms.
* `L-015` — historical cases challenge process, not vote on outcomes.
* `L-016` — candidate universe frozen before ranking.
* `L-017` — no invented probabilities.
* `L-018` — marginal likelihood ranking, not hedging.
* `L-021` — no value claim without validated probabilities/prices.
* `L-023` — derivative markets require their own target-event chain.
* `L-024` — field-owning source routing.
* `L-026` — unverified live states cannot drive directional live analysis.
* `L-029` — current-regime evidence and broad baseline retained separately.
* `L-030` — stale/placeholder score states are quarantined.

Soccer-specific controls:

* sparse local competition + unverified XI/keeper caps side confidence;
* goals and corners are separate target processes;
* corner dominance cannot be inferred from goals/possession;
* missing direct corner-causing evidence caps the corner row at `FORCED RANK`;
* rain/weather effects must be mechanism-specific.

---

## Candidate universe

**Decision-set ID:** `DS-P-126-V01`

**Candidate policy:** user supplied the 0.5 first-half goal line and 2.5
full-match goal line and explicitly authorised analyst-selected team/corner picks.

Frozen candidates:

| Candidate ID | Contract                                     | Origin                                                                | Eligibility                                                        |
| ------------ | -------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `P-126-C01`  | Sikkim Aakraman FC — regulation Match Winner | Analyst-selected                                                      | `ELIGIBLE`                                                         |
| `P-126-C02`  | 1st Half Goals Over 0.5                      | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C03`  | 1st Half Goals Under 0.5                     | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C04`  | Combined Total Goals Over 2.5                | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C05`  | Combined Total Goals Under 2.5               | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C06`  | Total Corners Over 7.5 — research threshold  | Analyst-selected / same sparse-local corner research threshold family | `ELIGIBLE FOR RESEARCH RANKING; OPERATOR AVAILABILITY UNCONFIRMED` |

No price-derived probability is used.

---

# Target definitions

## Goal target

**TARGET_ID:** `SOC-SIKKIM-REG-GOALS-P126-V01`

| Field                  | Definition                                                   |
| ---------------------- | ------------------------------------------------------------ |
| Outcome                | Regulation joint score `(Aakraman goals, Sikkim Boys goals)` |
| Unit                   | Official regulation goals                                    |
| Start                  | Pregame                                                      |
| Endpoint               | 90 minutes + official stoppage time                          |
| Extra time / penalties | Not applicable to league regulation target                   |
| Derived contracts      | Regulation winner, 1H O/U 0.5, FT O/U 2.5                    |
| Exact operator         | Not supplied                                                 |
| Void/abandonment terms | `UNKNOWN_DEFINITION`                                         |

## Corner target

**TARGET_ID:** `SOC-SIKKIM-CORNERS-P126-V01`

| Field                   | Definition                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| Outcome                 | Combined regulation corners                                                                               |
| Unit                    | Corners under named provider                                                                              |
| Research threshold      | Over 7.5                                                                                                  |
| Exact operator/provider | Not supplied                                                                                              |
| Current direct data     | Team corners for/conceded and recent match totals                                                         |
| Missing direct data     | crosses, blocked crosses, end-line entries, clearance events, set-play process, confirmed width/formation |
| Verdict ceiling         | `FORCED RANK`                                                                                             |
| Settlement state        | `UNKNOWN_DEFINITION` until provider is known                                                              |

---

# Participant verification

**Official starting XI — Sikkim Aakraman:** `NOT AVAILABLE`

**Official starting XI — Sikkim Boys:** `NOT AVAILABLE`

**Official goalkeepers:** `NOT AVAILABLE`

**Formation:** `NOT AVAILABLE`

**Current penalty/set-piece taker confirmation:** `NOT AVAILABLE`

No unverified player is treated as definitely starting.

This is a low-information local league and therefore side confidence is capped
under the active sparse-participant rule.

---

# Current league baseline

## Sikkim Aakraman

Reconstructed current league results:

| Opponent           | Result |
| ------------------ | -----: |
| Northerners        |  W 3-1 |
| Sang Mustang       |  W 3-0 |
| Gangtok Himalayan  |  W 2-0 |
| Sikkim Brotherhood |  W 1-0 |
| Dzongri            |  W 6-1 |
| Red Panda          |  W 2-1 |
| Howlers            |  W 5-0 |
| Sikkim Police      |  W 1-0 |

**Reconstructed league record:** 8 wins, 0 draws, 0 losses.

**Goals:** 23 for, 3 against.

The important mechanism is not simply the perfect record.

Aakraman have demonstrated both:

1. a separation branch — 3-1, 3-0, 6-1, 5-0;
2. a control branch — 2-0, 1-0, 1-0.

This means a strong winner forecast does not automatically require a high total.

---

## Sikkim Boys

Reconstructed current league results:

| Opponent           | Result |
| ------------------ | -----: |
| Sikkim Police      |  L 3-4 |
| Northerners        |  L 0-1 |
| Sang Mustang       |  L 1-2 |
| Gangtok Himalayan  |  D 1-1 |
| Sikkim Brotherhood |  L 1-6 |
| Dzongri            |  L 2-4 |
| Red Panda          |  L 0-6 |
| Howlers            |  W 8-3 |

**Reconstructed league record:** 1 win, 1 draw, 6 losses.

**Goals:** 16 for, 27 against.

The 8-3 win against Howlers is a material current-regime signal.

It proves Boys have a legitimate upper attacking tail and prevents the current
card from simply treating their season record as deterministic.

However, one 8-goal performance against Howlers is shrunk against the broader
league regime because Aakraman have conceded only three goals in eight league
matches.

---

# First-half goal evidence

Aakraman:

* at least one first-half goal in 6 of 8 reconstructed league games;
* recent HT states include 1-0 vs Police, 2-0 vs Howlers, 2-1 vs Red Panda and
  2-1 vs Dzongri;
* two meaningful 0-0 HT exceptions exist.

Sikkim Boys:

* at least one first-half goal in 7 of 8 reconstructed league games;
* each of the latest five had a first-half goal;
* recent first-half states include 3-1 vs Howlers, 0-3 vs Red Panda,
  0-1 vs Dzongri and 0-4 vs Brotherhood.

Mechanism:

`Aakraman early chance creation + Boys defensive instability + Boys transition
threat -> broad first-half scoring pathway`

Kill path:

`Aakraman possession control + low Boys block + wet surface/poor finishing ->
0-0 HT`

---

# Full-match goal evidence

Aakraman games Over 2.5:

**5 of 8**

Boys games Over 2.5:

**6 of 8**

Boys' four latest high-variance games:

* 1-6
* 2-4
* 0-6
* 8-3

All cleared 2.5.

The total is not ranked purely from those outcomes.

Central mechanisms:

1. Aakraman can create repeated chances against a defence conceding heavily.
2. Boys' current attack has a credible non-zero scoring branch after the
   Howlers performance.
3. An early Aakraman goal can force Boys into a more open trailing state.
4. Aakraman's own control game can still suppress the match into 1-0 or 2-0.

The 1-0 / 2-0 branch is why Over 2.5 does not outrank the first-half Over 0.5.

---

# Corner evidence

Current recoverable Aakraman corner totals:

* vs Sikkim Police: 6
* vs Howlers: 7
* vs Red Panda: 10
* vs Dzongri: 7
* vs Brotherhood: 8

Current recoverable Sikkim Boys corner totals:

* vs Howlers: 5
* vs Red Panda: 8
* vs Dzongri: 12
* vs Brotherhood: 11
* vs Gangtok Himalayan: 9

Recent observed distributions therefore support a broad 7-9 central corner
region with significant variance.

Historical Aakraman-Boys recorded H2H corner totals include:

* 4
* 13

This is too variable to treat H2H as a controlling prior.

### Missing corner mechanism

No reliable current data was recovered for:

* crossing volume;
* blocked crosses;
* end-line entries;
* defensive-clearance counts;
* current tactical width;
* confirmed winger/fullback roles;
* exact operator/stat-provider definition.

Therefore:

**Total Corners Over 7.5 = `FORCED RANK`, not `LEAN`.**

This line is a research threshold and should only be used if the user's operator
actually offers the same contract/provider definition.

---

# Weather/context

Current IMD warnings for Sikkim:

* 28 August: heavy-rain / thunderstorm-lightning warning.
* 29 August: thunderstorm/lightning warning.

Because the match schedule itself is conflicting, exact match-window conditions
cannot be frozen confidently.

Weather is bidirectional:

* poor surface/heavy rain may suppress clean combination play and finishing;
* it may also increase defensive errors, blocks, clearances and set plays.

No automatic weather-Under or weather-corner-Over adjustment is applied.

---

# Historical process reference

Prior Sports Research record `P-088` covered Howlers vs Sikkim Boys in this
same competition.

It established useful process warnings:

* official/current XIs may be unavailable;
* sparse-local team records do not remove participant uncertainty;
* direct corner-generation evidence is incomplete;
* corner settlement sources can remain unreliable after the final.

P-088's actual result is **not used as a forecast weight**.

Its process warnings are retained only to prevent repeating the same
source/derivative errors.

---

# Scenario map

| Scenario    | Match shape                                                            | Contracts helped                  |
| ----------- | ---------------------------------------------------------------------- | --------------------------------- |
| Lower       | Aakraman dominate but finish poorly; 1-0 / 2-0                         | Aakraman ML, Under 2.5            |
| Central     | Aakraman create early pressure and win 2-1 / 3-0 / 3-1                 | Aakraman ML, 1H O0.5, O2.5        |
| Upper       | Boys' defence collapses and/or contributes themselves; 4-1 / 5-1 / 4-2 | Aakraman ML, O2.5, likely 1H O0.5 |
| Upset       | Boys' Howlers-level attacking efficiency persists; 1-2 / 2-3           | O2.5, 1H O0.5, Aakraman ML fails  |
| Corner-low  | Early clean goals reduce prolonged crossing/clearance sequences        | Corner O7.5 fails                 |
| Corner-high | Boys trail and chase wide; repeated blocks/clearances/set plays        | Corner O7.5 helped                |

---

# Complete ranking

|  Rank | Candidate   | Contract                                        | Verdict       | Evidence                                | Dependence               | Actionability                                           | Probability     |
| ----: | ----------- | ----------------------------------------------- | ------------- | --------------------------------------- | ------------------------ | ------------------------------------------------------- | --------------- |
| **1** | `P-126-C01` | **Sikkim Aakraman FC — Match Winner**           | `FORCED RANK` | `MEDIUM-LOW — participant/schedule cap` | `GOAL TREE`              | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
| **2** | `P-126-C02` | **1st Half Over 0.5 Goals**                     | `LEAN`        | `MEDIUM`                                | `GOAL TREE / FIRST HALF` | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
| **3** | `P-126-C04` | **Combined Total Over 2.5 Goals**               | `LEAN`        | `MEDIUM`                                | `GOAL TREE`              | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
| **4** | `P-126-C06` | **Total Corners Over 7.5 — research threshold** | `FORCED RANK` | `LOW-MEDIUM`                            | `CORNER TREE`            | `NOT ACTIONABLE UNTIL OPERATOR LINE/PROVIDER CONFIRMED` | `NOT_GENERATED` |
|     5 | `P-126-C05` | Combined Total Under 2.5 Goals                  | `AVOID`       | `MEDIUM`                                | `GOAL TREE`              | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
|     6 | `P-126-C03` | 1st Half Under 0.5 Goals                        | `AVOID`       | `MEDIUM`                                | `GOAL TREE / FIRST HALF` | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |

---

# Ranking rationale

## #1 — Sikkim Aakraman FC Match Winner

Aakraman own the strongest overall regulation-win pathway:

* reconstructed 8-0-0 league record;
* 23-3 league goal differential;
* multiple strong scoring paths;
* multiple controlled clean-sheet paths;
* Sikkim Boys have lost six of eight league games;
* Boys' defensive concession regime remains severe despite their latest win.

The strongest failure path is Boys carrying their 8-3 attacking regime forward
while Aakraman's currently unverified XI/goalkeeper differs materially from
recent matches.

Because official participants are not confirmed, the row is capped at
`FORCED RANK / MEDIUM-LOW`.

---

## #2 — 1st Half Over 0.5 Goals

This has the strongest direct threshold-specific evidence of the supplied goal
markets.

A first-half goal appeared in:

* 6/8 reconstructed Aakraman games;
* 7/8 reconstructed Boys games;
* all five latest Boys matches.

Aakraman's early attacking strength and Boys' repeated first-half concessions
create several independent scoring routes.

Kill path: controlled Aakraman possession, compact Boys defence and poor
finishing produce 0-0 HT.

---

## #3 — Combined Total Over 2.5 Goals

The matchup supports a higher-scoring branch through:

* Boys' defensive leakage;
* Aakraman's scoring ceiling;
* Boys' newly demonstrated attacking ceiling;
* open trailing-state possibilities.

However, Aakraman have repeatedly demonstrated a 1-0/2-0 control branch.

That lowers the Over 2.5 ranking below the first-half Over 0.5.

---

## #4 — Total Corners Over 7.5

Recent direct corner counts provide some support, especially through a likely
Boys trailing/chasing branch.

However, the direct corner-causing chain is incomplete.

This contract therefore remains:

`FORCED RANK — LOW-MEDIUM`

and is not upgraded merely because Aakraman are likely to dominate the match.

---

# Potential winner

**Potential winner:** **Sikkim Aakraman FC**

**Canonical contract:** `P-126-C01`

**Winner status:** `FORCED WINNER — LOW CONFIDENCE`

The low-confidence token reflects sparse participant/schedule verification,
not a belief that the teams are evenly matched.

The football evidence itself clearly favours Aakraman.

Strongest upset path:

Sikkim Boys reproduce the unusually efficient transition/finishing state from
their 8-3 win while Aakraman's unavailable participant information hides a
meaningful lineup change.

---

# Final forecast card

|  Rank | Pick                                                                               |
| ----: | ---------------------------------------------------------------------------------- |
| **1** | **Sikkim Aakraman FC — Match Winner**                                              |
| **2** | **1st Half Goals — Over 0.5**                                                      |
| **3** | **Combined Total Goals — Over 2.5**                                                |
| **4** | **Total Corners — Over 7.5** *(research threshold; confirm operator availability)* |

**Potential game winner:** **Sikkim Aakraman FC**

**Supplied Under branches:**

* Full Match Under 2.5 — `AVOID`
* 1st Half Under 0.5 — `AVOID`

**GAME-STATE:**
`PREGAME / SCHEDULE CONFLICT — NO VERIFIED LIVE STATE`

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

**Forecast status:**
`RANKED FORECAST — CORNER ROW REQUIRES OPERATOR/PROVIDER CONFIRMATION`

---

# Source record

| Source                                      | Role                                                                              |
| ------------------------------------------- | --------------------------------------------------------------------------------- |
| Sikkim Football Association / SFA reporting | Competition/governing context                                                     |
| The Away End                                | Current league fixtures, results and goal times                                   |
| Sikkim Express                              | SFA-reported match results and competition context                                |
| Sofascore                                   | Fixture/state/result cross-check                                                  |
| AiScore                                     | Conflicting schedule and current-form cross-check                                 |
| ScoutMe                                     | Conflicting 28-August fixture schedule                                            |
| TotalCorner                                 | Direct corner totals, current match/corner research and provider-specific history |
| ScanGoal                                    | Specialist shot/chance/corner process cross-check                                 |
| IMD Met Centre Gangtok                      | Weather-warning state                                                             |
| Current market aggregator                   | Contract/market context only; NOT sporting evidence                               |

---

# Logging confirmation

**Canonical ID:** `P-126`

**Issued view:** `V01`

**Storage mode:** `COPY-PASTE MARKDOWN — NO GOOGLE DRIVE WRITE`

**Google Drive modified:** `NO`

**Historical combined log:** remains read-only predecessor evidence.

**Result status:** `OPEN — PENDING`

**Retrospective:** `NOT INCLUDED — per current user instruction`

---

# P-135 — Unión de Santa Fe vs Sarmiento — Torneo Clausura 2026

## State warning

**FINAL STATE:** `START CROSSED — LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`

The current official Unión match notice and current AFA referee assignment both scheduled the match for **19:00 Argentina time on 28 August 2026**, equivalent to **08:00 Australia/Melbourne on 29 August 2026**. That scheduled start passed during research.

At the first post-start refresh, no trustworthy source exposed both a verified live score and match clock. Some secondary feeds still carried conflicting 21:15 / 00:15 UTC schedule entries.

Under the active Sports Research state-integrity rules, the rankings below are preserved as a **frozen pre-start evidence view only** and are **not actionable as live picks**.

---

## Executive pre-start ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Sarmiento Team Total Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **2** | **1st Half Goals Over 0.5** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **3** | **Sarmiento or Draw — Double Chance X2** | `FORCED RANK` | `MEDIUM-LOW — official XI not verified` |
| **4** | **Total Corners Under 10.5 — research threshold** | `FORCED RANK` | `MEDIUM-LOW — derivative/provider cap` |
| **5** | **Combined Total Goals Over 2.5** | `FORCED RANK` | `MEDIUM-LOW — participant/state cap` |

**Potential game winner:** **Sarmiento — FORCED WINNER / LOW CONFIDENCE**

Lower-ranked supplied branches:
- 1st Half Under 0.5
- Full Match Under 2.5

---

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-135` |
| Sport | Soccer |
| Competition | Argentina Liga Profesional — Torneo Clausura 2026 |
| Round | Fecha 7 |
| Fixture type | Interzonal |
| Event | Unión de Santa Fe vs Sarmiento |
| Venue | Estadio 15 de Abril, Santa Fe |
| Official/current scheduled start | 2026-08-28 19:00 Argentina |
| Melbourne equivalent | 2026-08-29 08:00 AEST |
| Referee | Pablo Echavarría |
| VAR | Hernán Mastrángelo |
| Method | `MDS-2026.08.28-v2.4` |
| Sport module | `RULES_SOCCER.md` |
| Numerical status | `NO SOCCER MODEL FIT / VALIDATED` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Delivery | `DOWNLOADABLE MARKDOWN FILE` |
| Retrospective | `NOT INCLUDED` |

---

# Framework controls applied

The active soccer rules require:

- exact event, competition and regulation identity;
- current starting XI and goalkeeper status for participant-dependent side or player claims;
- winner and goal-total markets to come from one coherent goal process;
- corners to come from a separate corner-event process;
- current form/regime to be reconciled against older H2H;
- red-card and score-state branches to remain explicit;
- exact provider definition for corners;
- verified score and clock before any live forecast after kickoff.

Because the official starting XIs and goalkeepers were not independently verified from an official field-owner release before start crossing, participant-sensitive rows remain capped.

---

# Frozen candidate universe

**Decision-set ID:** `DS-P-135-V01`

User-supplied market families:
- 1H Over/Under 0.5 goals
- Full Game Over/Under 2.5 goals

Analyst-added candidates frozen before ranking:
- Sarmiento Team Total Over 0.5 goals
- Sarmiento or Draw — Double Chance X2
- Total Corners Under 10.5 — research threshold

No player prop was added because the official XI could not be verified.

---

# Current competition form

## Unión — first six Clausura matches

| Match | Result | Total |
|---|---:|---:|
| Platense vs Unión | 2-2 | 4 |
| Unión vs Lanús | 2-1 | 3 |
| Gimnasia Mendoza vs Unión | 2-0 | 2 |
| Unión vs Central Córdoba | 1-2 | 3 |
| San Lorenzo vs Unión | 1-0 | 1 |
| Aldosivi vs Unión | 1-3 | 4 |

Record: **2-1-3**

Goals:
- For: **8**
- Against: **9**

Over 2.5:
- **4 of 6**

Unión enter after a 3-1 win at Aldosivi, but had lost the previous two.

### Material Unión availability notes

Current reporting identifies:
- Julián Palacios — suspended after a red card in the previous round
- Lautaro Vargas — knee injury
- Federico Gomes Gerth — long-term knee injury
- Ignacio Malcorra — returning from a muscle injury / squad-status uncertainty in current reports

No named-player effect is converted into a numerical coefficient.

---

## Sarmiento — first six Clausura matches

| Match | Result | Total |
|---|---:|---:|
| Sarmiento vs Argentinos Juniors | 2-3 | 5 |
| Banfield vs Sarmiento | 3-2 | 5 |
| Sarmiento vs Independiente Rivadavia | 2-1 | 3 |
| Atlético Tucumán vs Sarmiento | 1-2 | 3 |
| Sarmiento vs Huracán | 2-0 | 2 |
| Sarmiento vs Estudiantes | 2-0 | 2 |

Record: **4-0-2**

Goals:
- For: **12**
- Against: **8**

Over 2.5:
- **4 of 6**

Most important current-regime fact:

**Sarmiento scored exactly two goals in all six Clausura matches.**

This is not treated as a self-validating streak. The mechanism is more important:
- repeated multi-chance attacking output;
- Junior Marabel has been the main high-xG scorer;
- a stable two-forward structure;
- improved defensive control during the four-match winning run;
- enough transition/box-entry quality to score multiple times across different game states.

Latest four:
- 2-1
- 2-1
- 2-0
- 2-0

That is why **Sarmiento Team Total Over 0.5** ranks first.

---

# Table / regime comparison

Sarmiento enter:
- 2nd in Zone B
- 12 points
- four consecutive wins

Unión enter:
- 7 points
- 2-1-3
- coming off a rebound 3-1 win

### Baseline branch
Unión's home field and historical competitiveness keep the match close.

### Current-regime branch
Sarmiento's four-match winning run is supported by repeated two-goal output and improved defence, while Unión remain inconsistent.

The current regime is weighted above stale reputation, but not strongly enough to eliminate the Unión home-win path.

---

# Probable lineups — secondary only

## Unión probable XI
Matías Mansilla; Juan De Dios Pintado, Maizon Rodríguez, Juan Pablo Ludueña, Lucas Ayala; Brahian Cuello, Emilio Giaccone, Lucas Menossi, Mauro Luna Diale; Cristian Tarragona, Marcelo Estigarribia.

## Sarmiento probable XI
Thyago Ayala; Santiago Salle, Renzo Orihuela, Juan Manuel Insaurralde, Lucas Suárez; Julián Contrera, Mauricio Martínez, Cristian Zabala, Julián Mavilla; Junior Marabel, Jonathan Herrera.

These were repeated across current Argentine media but were **not** upgraded to `CONFIRMED_OFFICIAL`.

Participant state:
`SECONDARY_ONLY / NOT OFFICIALLY VERIFIED AT CUTOFF`

---

# First-half goal process

Directly recoverable recent states:

### Unión
- vs Central Córdoba: **1-0 HT**
- at Gimnasia Mendoza: **0-1 HT**
- at Platense: **0-1 HT**
- vs Lanús: **0-0 HT**
- at San Lorenzo: **0-0 HT**

At least **3 of 5** directly recoverable recent league first halves contained a goal.

### Sarmiento
- vs Huracán: **1-0 HT**
- vs Estudiantes: **1-0 HT**
- February 2026 H2H vs Unión: **0-2 HT**

### 1H Over 0.5 mechanism
`Sarmiento's current attacking start + Unión's recent first-half concession risk + both teams' current multi-goal environments -> meaningful early-goal branch`

Strongest kill path:
both teams begin conservatively, prioritising transition prevention and field position.

Therefore:
**1H Over 0.5 = Rank #2**

---

# Full-game goal process

## Over 2.5 support
- Unión: **4/6**
- Sarmiento: **4/6**
- combined descriptive sample: **8/12**
- Sarmiento: 12 goals in six
- Unión: 9 conceded in six
- February 2026 H2H: **Sarmiento 1-3 Unión**

## Under 2.5 support
- Sarmiento's last two were both **2-0**
- Unión recently had **1-0** and **0-2**
- historical H2H average is roughly **2.1 goals**
- a leading side can reduce risk and compress late attacking exposure

### Goal corridor

Lower:
- 1-0
- 1-1
- 2-0

Central:
- 1-2
- 2-1

Upper:
- 2-2
- 1-3
- 3-1

Current-regime evidence slightly favours 3+ goals, but not strongly enough for high confidence.

---

# Side / winner process

## Why Sarmiento X2 ranks above the outright winner

Sarmiento:
- four straight wins
- 2 goals in every Clausura game
- two consecutive clean sheets
- second in Zone B

Unión:
- 2-1-3
- rebound win last round, but inconsistent overall
- suspended Julián Palacios
- current rebuild/lineup uncertainty

Strongest contrary path:
Unión's home field, Tarragona/Estigarribia finishing and the momentum from the 3-1 Aldosivi win recreate the February 3-1 H2H.

Therefore:
**Sarmiento or Draw X2 = Rank #3**

---

# Corner process

The active soccer framework prohibits using goals or possession as substitutes for corner evidence.

## Direct H2H corner evidence

Across 13 recoverable H2Hs:
- average total corners: approximately **10.0**
- Over 9.5: approximately **54%**

Recent H2H:
- Feb 2026: **9**
- Sep 2024: **4**
- Mar 2024: **11**
- Oct 2023: **10**
- May 2023: **18**
- Sep 2022: **13**

The distribution is wide.

## Current-rate corroboration

Current secondary statistical summaries place approximately:
- Unión corners for: **4.0–4.6**
- Unión corners against: **4.0–4.8**
- Sarmiento corners for: **3.9–4.1**
- Sarmiento corners against: **5.1–5.3**

A simple cross-team blend lands around the high-8s/low-9s total-corner range.

That makes **Under 10.5** the preferred research threshold.

### Missing corner layers
Not fully verified:
- crosses
- blocked crosses
- end-line entries
- clearances
- exact tactical width
- confirmed current fullbacks/wingers
- exact settlement provider/definition

Therefore:
**Total Corners Under 10.5 = FORCED RANK / MEDIUM-LOW**

---

# H2H audit

13 recoverable meetings:
- Sarmiento wins: 5
- draws: 2
- Unión wins: 6
- average goals: ~2.1
- average corners: ~10.0

Latest:
**Sarmiento 1-3 Unión — 26 February 2026**
- HT: 0-2
- corners: 7-2
- total corners: 9

The current-year H2H matters, but it does not override:
- Sarmiento's four-match winning run;
- current two-goal-per-match Clausura output;
- Unión's changed personnel/availability state.

---

# Scenario tree

## Sarmiento competitive / scores
Representative:
- 1-1
- 1-2
- 2-2

Helps:
- Sarmiento TT O0.5
- 1H O0.5 in early-goal branches
- Sarmiento X2
- O2.5 in 1-2 / 2-2

## Sarmiento control
Representative:
- 0-1
- 0-2

Helps:
- Sarmiento TT O0.5
- Sarmiento X2
- corner Under remains live
- FT Under 2.5 threatens Rank #5

## Unión rebound
Representative:
- 2-1
- 3-1

Helps:
- 1H Over
- Over 2.5
- Sarmiento TT O0.5 may still survive

Kills:
- Sarmiento X2

## Closed tactical branch
Representative:
- 0-0
- 1-0
- 1-1

Helps:
- Under 2.5
- Corners Under 10.5

Kills:
- 1H Over in many variants
- Sarmiento TT O0.5 in a 1-0
- Over 2.5

---

# Final pre-start ranking

| Rank | Candidate | Pick | Verdict | Evidence | Probability |
|---:|---|---|---|---|---|
| **1** | `P-135-C01` | **Sarmiento Team Total Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **2** | `P-135-C02` | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **3** | `P-135-C03` | **Sarmiento or Draw — X2** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **4** | `P-135-C04` | **Total Corners Under 10.5** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **5** | `P-135-C05` | **Combined Total Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |

---

# Potential game winner

## Sarmiento — `FORCED WINNER / LOW CONFIDENCE`

Why:
- four consecutive wins
- second in Zone B
- two goals in every Clausura match
- two straight clean sheets
- current form stronger than Unión's
- Unión missing suspended Julián Palacios

Why confidence remains low:
- official XI/keeper verification incomplete
- Unión are at home
- Unión won the February H2H 3-1
- Unión enter off a 3-1 away win

---

# State-integrity conclusion

The scheduled **19:00 Argentina / 08:00 Melbourne** kickoff passed during research.

At the post-start refresh:
- no current source provided a trustworthy exact score and clock together;
- secondary schedule sources still disagreed with the current official 19:00 schedule.

Therefore:

**`LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`**

The five rankings above are the frozen pre-start evidence view only.

They should not be transferred to live markets without a verified:
- score
- match clock
- red-card state
- substitutions
- current shot/corner state

---

# Source record

## Google Drive framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- active learning/model/evaluation specifications

## Official/current event sources
- Club Atlético Unión official match notice
- Asociación del Fútbol Argentino current referee assignment
- Liga Profesional current schedule
- TyC Sports current match preview
- current Argentine team/availability reporting

## Statistical support
- FotMob / Opta-powered current form and xG context
- TotalCorner direct H2H and corner-event records
- secondary aggregated corner-rate sources used only as corroboration

## Limitations
- official starting XIs/keepers were not recovered before start crossing
- corner provider/settlement definition not supplied
- exact live score/clock not verified after scheduled kickoff
- no fitted/validated soccer model exists

---

# Logging confirmation

**Canonical ID:** `P-135`  
**Issued view:** `V01`  
**Google Drive modified:** `NO`  
**Delivery:** `DOWNLOADABLE MARKDOWN FILE`  
**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value:** `NO VALUE DETERMINABLE`  
**Retrospective:** `NOT INCLUDED`  
**Current disposition:** `START CROSSED — LIVE STATE NOT VERIFIED — PRE-START RANKING PRESERVED FOR REFERENCE ONLY`

---

# P-136 — James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Total Games Over 22.5** | **LEAN** | **MEDIUM-HIGH** |
| **2** | **James Duckworth +1.5 Games** | **LEAN** | **MEDIUM** |
| **3** | **Arthur Fery -1.5 Games** | **FORCED RANK** | **MEDIUM** |
| **4** | **Total Games Under 22.5** | **AVOID** | **MEDIUM-HIGH** |

**Potential match winner:** **Arthur Fery — LEAN**

### Central interpretation

Fery is the preferred outright winner because his current hard-court return profile is stronger, his 2026 level is materially higher, and he has the better recovery situation entering the semifinal.

However, Duckworth has been serving extremely well in Winston-Salem, and the most recent head-to-head — only two weeks ago in Cincinnati — ended:

**Fery 6-4, 2-6, 7-6(4)**

Fery won the match, but Duckworth actually won **16 total games to Fery's 15**.

That creates a coherent central state in which:
- **Fery wins the match**
- **Duckworth +1.5 still covers**
- **Over 22.5 wins**

Representative central score shapes:
- Fery 7-6, 4-6, 6-4
- Fery 6-4, 3-6, 7-6
- Fery 7-5, 4-6, 6-4

---

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-136` |
| Sport | Tennis |
| Competition | ATP Winston-Salem Open 2026 |
| Level | ATP 250 |
| Round | Singles Semifinal |
| Event | James Duckworth vs Arthur Fery |
| Court | Stadium Court |
| Surface | Outdoor hard |
| Format | Best-of-three sets |
| Official scheduled start | Not before 6:30 PM EDT, Friday 28 Aug 2026 |
| Melbourne equivalent | Not before 8:30 AM AEST, Saturday 29 Aug 2026 |
| Final research refresh | 2026-08-29 08:05 AEST |
| GAME-STATE | `PREGAME` |
| Duckworth ranking | approximately ATP 79–86 depending live/static source |
| Fery ranking | ATP 37; live ranking at least mid-30s |
| H2H | Duckworth leads 2-1 |
| Method | `MDS-2026.08.28-v2.4` |
| Sport module | `RULES_TENNIS.md` |
| Numerical status | `NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL APPROVED OR FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# Framework controls applied

The active Sports Research tennis module requires:

- exact competition, round, surface, format and participant identity;
- retirement/walkover terms treated as contract-specific;
- surface-specific serve/return form separated from ranking/reputation;
- first/second serve, hold/break and return pressure used as process evidence;
- head-to-head continuity audited for surface, level and current player regime;
- one coherent match tree for winner, game handicap and total games;
- explicit straight-set and three-set branches;
- qualifying/workload/recovery treated mechanistically rather than as an automatic fatigue penalty;
- no published numerical probability because no approved/fitted tennis model exists.

---

# Frozen decision set

**Decision-set ID:** `DS-P-136-V01`

| Candidate ID | Exact contract |
|---|---|
| `P-136-C01` | James Duckworth +1.5 Games |
| `P-136-C02` | Arthur Fery -1.5 Games |
| `P-136-C03` | Total Games Over 22.5 |
| `P-136-C04` | Total Games Under 22.5 |

### Contract geometry

**Duckworth +1.5**
- wins if Duckworth wins the match;
- also wins if Fery wins but Duckworth finishes no more than one game behind in total games.

**Fery -1.5**
- requires Fery to win the match and finish at least two total games ahead.

The two handicap rows are exact half-game complements.

**Over 22.5**
- wins at 23+ total games.

**Under 22.5**
- wins at 22 or fewer.

No push exists.

### Retirement / walkover rules

No operator was supplied.

Therefore exact retirement settlement is:

`UNKNOWN_DEFINITION`

No expected-value or price claim is made.

---

# Official event and state verification

The official Winston-Salem Open schedule lists:

**James Duckworth vs Arthur Fery (4)**  
Singles semifinal  
Stadium Court  
**Not Before 6:30 PM EDT on 28 August 2026**

At 08:05 AEST / 18:05 EDT, the match remained pre-start and current match feeds continued to list it as upcoming.

Therefore:

`GAME-STATE: PREGAME`

---

# Head-to-head audit

Current H2H:

**Duckworth 2-1 Fery**

All three meetings were on hard courts.

| Date | Event | Winner | Score | Total games | Duckworth +1.5 |
|---|---|---|---|---:|---|
| 2024-04-10 | Busan Challenger | Duckworth | 4-6, 6-1, 6-4 | 27 | WIN |
| 2024-05-16 | Taipei Challenger | Duckworth | 7-5, 7-5 | 24 | WIN |
| 2026-08-15 | Cincinnati ATP 1000 | Fery | 6-4, 2-6, 7-6(4) | 31 | WIN |

### Direct descriptive results

- Over 22.5: **3/3**
- Duckworth +1.5: **3/3**
- Fery -1.5: **0/3**
- Under 22.5: **0/3**

These are not used as raw probabilities.

### Continuity weighting

The two 2024 meetings are downweighted because Fery was then ranked around the mid-200s and was in a materially different development/fitness regime.

The **Cincinnati meeting from two weeks ago** receives much greater weight because:
- same outdoor-hard North American swing;
- both players in essentially current technical regimes;
- ATP main-tour level;
- no major current injury change identified.

That current meeting strongly supports a **close-match / long-match branch**.

---

# Most recent H2H — Cincinnati 2026

Fery won:

**6-4, 2-6, 7-6(4)**

Match stats:

| Metric | Fery | Duckworth |
|---|---:|---:|
| Aces | 9 | 6 |
| Double faults | 3 | 4 |
| First serve in | 51% | 51% |
| First-serve points won | 73% | **82%** |
| Second-serve points won | 59% | 58% |
| Service games held | 12/15 | **13/15** |
| Breaks converted | 2/3 | **3/6** |

Important interpretation:

Fery won the higher-leverage final-set tiebreak, but Duckworth:
- held more often;
- broke more often;
- won one more total game.

This is exactly why **Fery winner** can coexist with **Duckworth +1.5**.

---

# Current hard-court process

## Arthur Fery — recent hard split

Tennis Abstract recent hard-court profile:

- record: approximately **33-12**
- hold rate: approximately **81.2%**
- service points won: approximately **65.2%**
- break rate: approximately **29.0%**
- return points won: approximately **41.1%**
- dominance ratio: approximately **1.18**

Fery's key advantage is **return pressure**.

His hold rate is strong but not elite; the differential comes from creating substantially more return opportunities than Duckworth across the recent hard sample.

---

## James Duckworth — recent hard split

Tennis Abstract recent hard-court profile:

- record: approximately **28-22**
- hold rate: approximately **83.3%**
- service points won: approximately **66.4%**
- break rate: approximately **19.9%**
- return points won: approximately **35.6%**
- dominance ratio: approximately **1.06**

Duckworth's profile is more serve-led:
- stronger ace rate;
- slightly higher hold baseline;
- weaker return pressure.

That structure naturally creates:
- 6-4 sets;
- 7-5 sets;
- tiebreaks;
- close overall game margins.

This supports the Over and Duckworth +1.5.

---

# Winston-Salem current tournament

## Duckworth

| Round | Opponent | Score | Total games | Game margin |
|---|---|---|---:|---:|
| R64 | Quinn Vandecasteele | 6-2, 6-1 | 15 | +9 |
| R32 | Mariano Navone | 6-3, 7-6(5) | 22 | +4 |
| R16 | Lorenzo Sonego | 7-5, 6-3 | 21 | +5 |
| QF | Fábián Marozsán | 6-7(4), 6-2, 6-4 | 31 | +5 |

Duckworth is **4-0** this week.

The first three matches were straight-set control wins. The quarterfinal became a full three-set test.

### QF process vs Marozsán

Duckworth:
- 8 aces
- 8 double faults
- only 48% first serves in
- 76% first-serve points won
- 59% second-serve points won
- held 12 of 15 service games
- broke 6 of 15 Marozsán service games

The first-serve percentage was poor, but he still created significant return pressure and recovered after losing the first set.

---

## Fery

| Round | Opponent | Score | Total games | Game margin |
|---|---|---|---:|---:|
| R32 | Cruz Hewitt | 6-1, 7-5 | 19 | +7 |
| R16 | Mees Röttgering | 6-3, 6-3 | 18 | +6 |
| QF | Aleksandar Kovacevic | 3-6, 7-5, 6-3 | 30 | +2 |

Fery is **3-0** this week.

### QF process vs Kovacevic

Fery:
- 4 aces
- **0 double faults**
- 56% first serves in
- **82% first-serve points won**
- **62% second-serve points won**
- held **14 of 15** service games
- broke 2 of 15 return games

This is an excellent serving performance and shows Fery can win even when return opportunities are scarce.

---

# Current form / ranking regime

## Fery

Fery's 2026 rise is substantial:
- current ranking around No. 37;
- live ranking at least around No. 35 after reaching this semifinal;
- Wimbledon semifinalist;
- recent Cincinnati win over Duckworth;
- current hard-court results substantially stronger than his 2024 Challenger-level profile.

That means the old 2024 Duckworth H2H wins cannot simply be treated as equal evidence to the current Cincinnati meeting.

## Duckworth

Duckworth:
- remains an experienced hard-court player;
- has reached his fourth ATP Tour semifinal;
- is in his best ATP-level tournament run since 2025;
- has beaten Navone, Sonego and Marozsán this week;
- is producing a materially better current tournament level than his broad 2026 ranking/record alone suggests.

Therefore the correct regime mixture is:

**Fery stronger broad/current player + Duckworth unusually strong current tournament form**

This widens the distribution and supports a close-match tree.

---

# Recovery / workload

## Fery quarterfinal
- beat Kovacevic 3-6, 7-5, 6-3
- duration approximately **2h08**
- played earlier in the evening

## Duckworth quarterfinal
- beat Marozsán 6-7, 6-2, 6-4
- duration approximately **2h23**
- finished close to **1:00 AM local time**

Duckworth is also 34 years old versus Fery's 24.

### Mechanistic implication

This gives Fery a real recovery edge:
- later Duckworth finish;
- longer match;
- older player;
- one additional tournament match played this week.

It supports:
- Fery winner;
- Fery separation / straight-set tail.

It does **not** automatically imply fatigue failure:
Duckworth has shown no current injury/medical problem and has repeatedly recovered through long professional schedules.

This is the strongest kill path against Duckworth +1.5 and Over 22.5.

---

# Match tree

## Branch A — long, close Fery win

Representative:
- Fery 7-6, 4-6, 6-4
- Fery 6-4, 3-6, 7-6
- Fery 7-5, 4-6, 6-4

Favours:
- **Over 22.5**
- **Duckworth +1.5** in many variants
- Fery winner

This is the central branch.

---

## Branch B — Fery straight-set separation

Representative:
- Fery 6-4, 6-3
- Fery 7-5, 6-3
- Fery 6-3, 6-4

Mechanism:
- Fery's return advantage converts into repeated break pressure;
- Duckworth's short recovery reduces first-serve quality;
- Fery protects his own serve at the level shown vs Kovacevic.

Favours:
- Fery -1.5
- Under 22.5 in most variants

This is the strongest contrary path to ranks #1 and #2.

---

## Branch C — tight Fery straight-set win

Representative:
- Fery 7-6, 6-4 = 23
- Fery 7-5, 7-5 = 24
- Fery 7-6, 7-6 = 26

Favours:
- Over 22.5
- Fery -1.5 in most variants
- Duckworth +1.5 only if the total-game margin stays within one

This branch helps explain why the Over can win even without a third set.

---

## Branch D — Duckworth upset

Representative:
- Duckworth 7-5, 4-6, 6-4
- Duckworth 7-6, 6-4
- Duckworth 6-4, 3-6, 7-6

Mechanism:
- Duckworth continues to hold at ~85%+;
- first serve controls Fery's return edge;
- Fery's break conversion remains limited;
- Duckworth's experience wins pressure points.

Favours:
- Duckworth +1.5
- Over 22.5 in most three-set/tight variants

---

# Why Over 22.5 ranks #1

### Direct matchup support
All three H2Hs:
- 27 games
- 24 games
- 31 games

All cleared 22.5.

### Current-regime support
The most relevant H2H was only two weeks ago:
- three sets
- deciding tiebreak
- 31 games

### Serve/return structure
Both recent hard hold rates are above 81%.

Duckworth is serve-led and Fery is not such a dominant returner that a double-break-per-set straight-set match should be treated as the default.

### Current tournament
Both players' quarterfinals went three sets:
- Duckworth 31 games
- Fery 30 games

### Tight straight-set rescue
Scores such as:
- 7-6, 6-4
- 7-5, 7-5
- 7-6, 7-6

all clear 22.5.

### Kill path
Fery's recovery advantage plus stronger return rate produces a cleaner 6-4, 6-3 or 6-3, 6-4 win.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM-HIGH`

---

# Why Duckworth +1.5 ranks #2

Direct H2H descriptive record:
- **3/3 covers**

Most importantly, Duckworth covered +1.5 in the **current-regime Cincinnati loss**, because he won one more total game despite losing the match.

The handicap also wins automatically on any Duckworth upset.

This line fits the central close-Fery-win branch particularly well.

### Kill path
Fery wins in straights or produces a 3+ net game margin in three sets through superior return pressure and Duckworth recovery decline.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM`

---

# Why Fery -1.5 ranks #3

Fery is the preferred match winner.

Support:
- much stronger 2026 ranking/current level;
- stronger recent hard return profile;
- 29% recent hard break rate vs Duckworth around 20%;
- won their Cincinnati meeting;
- better recovery after the quarterfinal;
- 10-year age advantage.

But the exact market asks for more than winning.

Fery must finish **2+ games ahead**.

That has failed in all three prior H2Hs.

The current Cincinnati win is especially important because it shows the exact winner/handicap split:
**Fery won, Duckworth won the game count.**

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM`

---

# Why Under 22.5 ranks #4

There is a real Under branch because most of each player's earlier Winston-Salem matches were efficient straight-set wins.

Duckworth tournament totals:
- 15
- 22
- 21
- 31

Fery:
- 19
- 18
- 30

So the current tournament itself contains many Under outcomes.

However, those Under matches mostly occurred when one player was clearly controlling a weaker/different opponent.

Against each other:
- all three meetings have exceeded 22.5;
- the current-regime meeting went 31;
- the winner is not projected to dominate sufficiently for a short straight-set result to be the central branch.

**Verdict:** `AVOID`  
**Evidence:** `MEDIUM-HIGH`

`AVOID` is evidence-relative and is not a negative expected-value claim.

---

# Potential game winner

## Arthur Fery — `LEAN`

Why:
- ranking/current level advantage;
- stronger recent hard-court dominance ratio;
- substantially better return and break profile;
- won the most recent H2H;
- reached the Wimbledon semifinal this year;
- excellent quarterfinal service numbers;
- more recovery time than Duckworth;
- younger by approximately 10 years.

Strongest failure path:
Duckworth's current Winston-Salem serving level persists, Fery cannot create enough break chances, and Duckworth's experience in close/tiebreak sets decides the match.

### Coherence statement

**Fery winner** and **Duckworth +1.5 games** are fully coherent.

The most recent H2H produced exactly that combination.

---

# Final forecast card

1. **Total Games Over 22.5**
2. **James Duckworth +1.5 Games**
3. **Arthur Fery -1.5 Games**
4. **Total Games Under 22.5**

**Potential match winner:** **Arthur Fery**

**GAME-STATE:** `PREGAME`

**Probability state:**  
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**  
`NO VALUE DETERMINABLE`

---

# Source record

## Google Drive framework
- `RULES_TENNIS.md`
- `RULES_GENERAL.md`
- active Sports Research model/evaluation/learning controls

## Official / primary current event sources
- Winston-Salem Open official schedule
- Winston-Salem Open official tournament news
- ATP Tour Winston-Salem results
- Tennis Australia current Duckworth reporting

## Current statistical sources
- Tennis Abstract — hard-court hold/break/serve/return and dominance splits
- Tennis.com — current Cincinnati H2H and Winston-Salem quarterfinal match stats
- tournament/result databases used to cross-check historical H2H

## H2H
- 2024 Busan Challenger: Duckworth 4-6, 6-1, 6-4
- 2024 Taipei Challenger: Duckworth 7-5, 7-5
- 2026 Cincinnati ATP Masters 1000: Fery 6-4, 2-6, 7-6(4)

## Limitations
- no operator was supplied, so retirement/walkover settlement rules are unknown;
- current statistical provider windows are not perfectly identical;
- no fitted/validated tennis probability model exists;
- old 2024 H2Hs are downweighted due to Fery's major development/fitness regime change;
- workload/recovery effect is treated as a branch rather than a deterministic penalty.

---

# Logging confirmation

**Canonical ID:** `P-136`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Delivery mode:** `DOWNLOADABLE MARKDOWN FILE`

**Retrospective:** `NOT INCLUDED`

**Final frozen state:** `PREGAME — approximately 25 minutes before the official not-before start`

---

# New forecast continuation

The next newly issued forecast is **`P-137`**.

## Continuation index

| Canonical ID | Sport | Competition | Event | View | Initial state | Rank #1 | Potential winner | Current status |
|---|---|---|---|---|---|---|---|---|
| `P-126` | Soccer | Sikkim S-League | Sikkim Aakraman FC vs Sikkim Boys Club | V01 | Pregame | Sikkim Aakraman ML | Sikkim Aakraman | **OPEN — PREGAME (inherited)** |
| `P-135` | Soccer | Argentina Liga Profesional Clausura | Unión de Santa Fe vs Sarmiento | V01 | Start crossed | Sarmiento team total Over 0.5 | Sarmiento | **OPEN — LIVE (inherited)** |
| `P-136` | Tennis | ATP Winston-Salem | James Duckworth vs Arthur Fery | V01 | Pregame | Over 22.5 games | Arthur Fery | **OPEN — PREGAME (inherited)** |
| `P-137` | — | — | — | — | — | — | — | **NEXT NEW FORECAST** |

## New-game entry boundary

Every new event from `P-137` onward follows the active Sports Research framework: exact identity and target freeze, participant/state verification, sport-native exposure/rate analysis, lower/central/upper/adverse scenario map, contract geometry/dependence, unique marginal-likelihood ranking, potential winner, final volatile refresh, and immutable append before delivery.

Current probability publication state remains `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; current value state remains `NO VALUE DETERMINABLE`.

# P-137 — Los Angeles Dodgers (Tarik Skubal) @ Detroit Tigers (Drew Anderson) — MLB

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Detroit Tigers +2.5 Runs** | **LEAN** | **MEDIUM-HIGH** |
| **2** | **Los Angeles Dodgers Moneyline** | **LEAN** | **MEDIUM-HIGH** |
| **3** | **Combined Total Under 7.5 Runs** | **LEAN** | **MEDIUM** |
| **4** | **Combined Total Over 7.5 Runs** | **AVOID** | **MEDIUM** |

**Potential game winner:** **Los Angeles Dodgers — LEAN**

### Central interpretation

The best-fit qualitative score corridor is approximately:

- Dodgers 3-2
- Dodgers 4-2
- Dodgers 4-3
- Dodgers 5-2

This makes the top three selections coherent:

- Detroit +2.5 can win even if Los Angeles wins the game.
- Dodgers ML captures the stronger starter/team-quality branch.
- Under 7.5 captures Skubal suppressing Detroit and the Dodgers' current lower-output offensive regime.

The main failure branch is a Dodgers power/contact surge against Drew Anderson and Detroit relief, producing a 6-2 / 7-2 type game.

---

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-137` |
| Sport | Baseball |
| League | MLB |
| Event | Los Angeles Dodgers @ Detroit Tigers |
| Venue | Comerica Park, Detroit |
| Date | 2026-08-28 local / 2026-08-29 Melbourne |
| Scheduled first pitch | 6:40 PM EDT |
| Melbourne equivalent | 8:40 AM AEST |
| Pregame research cutoff | Approximately 8:38 AM Australia/Melbourne |
| GAME-STATE | `PREGAME / WARMUP AT FINAL VERIFIED STATE` |
| Dodgers starter | Tarik Skubal — LHP |
| Tigers starter | Drew Anderson — RHP |
| Starter identity | `PROBABLE_OFFICIAL / MLB VERIFIED` |
| Method | `MDS-2026.08.28-v2.4` |
| Sport module | `RULES_BASEBALL.md` |
| Numerical state | `NTS-2026.08.25-v0.2 — PRE-FIT / NO VALIDATED BASEBALL MODEL` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# Identity gate

The supplied starter pairing initially required verification because Tarik Skubal had historically been associated with Detroit.

The pairing is **correct**.

MLB officially lists:

- **Los Angeles Dodgers: Tarik Skubal, LHP**
- **Detroit Tigers: Drew Anderson, RHP**

Skubal was acquired by Los Angeles from Detroit before the August 2026 trade deadline and is making his first start at Comerica Park as a visiting pitcher.

This starter identity was verified through MLB's official probable-pitcher page and Dodgers/Tigers official schedule material.

Therefore starter-quality evidence is allowed to become decision-driving.

---

# Exact decision set

**Decision-set ID:** `DS-P-137-V01`

| Candidate ID | Exact contract |
|---|---|
| `P-137-C01` | Dodgers Moneyline |
| `P-137-C02` | Tigers +2.5 Runs |
| `P-137-C03` | Over 7.5 Runs |
| `P-137-C04` | Under 7.5 Runs |

### Contract geometry

## Dodgers ML

Wins with any Los Angeles victory.

## Tigers +2.5

Wins if:
- Detroit wins;
- Detroit loses by 1;
- Detroit loses by 2.

Loses only if:
- Dodgers win by 3+.

This is not the opposite of Dodgers ML.

A Dodgers win by one or two runs makes **both Dodgers ML and Tigers +2.5 win**.

## Total

- Over 7.5 = 8+ runs.
- Under 7.5 = 7 or fewer.

No push exists.

---

# Official/current team state

## Los Angeles Dodgers

Current record around the cutoff:
**80-54**

Recent:
- first in the NL West
- 6-4 over the last 10
- entering after being swept in Atlanta

Broad offensive context:
- roughly 4.9 runs/game on the season
- season OPS around the upper-.700s
- significantly stronger broad lineup than Detroit

However, current August offence has cooled materially.

Recent reporting places Los Angeles around:
- **4.13 runs/game in August**
- approximately **94 wRC+**
- around 20th in MLB during that recent offensive window

The Dodgers were just shut out **1-0** by Chris Sale and Atlanta, completing a three-game sweep.

That current-regime offensive decline is explicitly retained rather than allowing the strong season reputation to control the total automatically.

---

## Detroit Tigers

Current record:
**62-71**

Recent:
- **2-8 over the last 10**
- approximately **10 losses in the last 12**
- 4th in the AL Central around the cutoff

Detroit scored only:
**32 runs in its last 10 games**

That is approximately:
**3.2 runs/game**

The Tigers are also materially weaker against left-handed starters by current record:
**16-25 vs LHP**

This is highly relevant with Skubal starting.

---

# Confirmed/current batting-order state

MLB's searchable starting-lineup page remained stale/TBD in the crawler close to first pitch, but contemporary Detroit and Los Angeles reports reproduced the official team lineup posts.

## Dodgers batting order

1. Shohei Ohtani — DH
2. Freddie Freeman — 1B
3. Mookie Betts — SS
4. Max Muncy — 3B
5. Tommy Edman — 2B
6. Kyle Tucker — RF
7. Alek Thomas — CF
8. Teoscar Hernández — LF
9. Hunter Feduccia — C

This is a deep lineup with:
- elite top-end OBP/power;
- multiple left-handed bats;
- substantial home-run clustering potential.

That power depth is the main threat to the Under.

## Tigers batting order

1. Gleyber Torres — 2B
2. Hao-Yu Lee — 3B
3. Kevin McGonigle — SS
4. Dillon Dingler — C
5. Eduardo Valencia — DH
6. Ben Malgeri — RF
7. Spencer Torkelson — 1B
8. Max Clark — CF
9. Javier Báez — LF

Detroit deliberately stacks several right-handed bats against Skubal, but:
- Kevin McGonigle and Max Clark remain left-handed;
- several players are young/small-sample major-league hitters;
- the overall offence has been weak recently.

Participant state for the batting orders:

`CURRENT SECONDARY CAPTURE OF OFFICIAL TEAM POSTS — HIGH CONFIDENCE, BUT MLB SEARCH CRAWLER NOT FULLY REFRESHED`

---

# Starting-pitcher process

## Tarik Skubal — Dodgers

Season line around cutoff:
- 8-7
- **2.91 ERA**
- approximately **0.95 WHIP**
- 146 strikeouts in 120⅔ innings

Recent Dodgers regime:
- four appearances / starts for Los Angeles
- approximately **24 IP**
- **3.38 ERA**
- **2.67 FIP**
- 30 strikeouts
- 7 walks
- 2 home runs allowed

Most recent outing:
- Dodgers beat Pittsburgh **4-3**
- Skubal recorded **11 strikeouts**

### Skubal mechanism

The strongest run-suppression chain is:

`high strikeout rate + elite K/BB profile + limited free passes + weak recent Detroit offence + Detroit poor current record vs LHP -> reduced Detroit baserunner/cluster frequency`

This strongly supports:
- Dodgers ML;
- Under 7.5.

### Contrary Skubal branch

Detroit knows Skubal unusually well from his years in the organisation.

That familiarity is descriptive, not automatically predictive, because:
- pitch sequencing may differ;
- current Detroit lineup differs from older Tigers lineups;
- current Skubal arsenal/location remains elite.

A homecoming-emotion narrative is not assigned a directional coefficient.

---

## Drew Anderson — Tigers

Season:
- 4-5
- **4.09 ERA**
- approximately **1.29 WHIP**

Current role:
- transitioned from relief into the Detroit rotation after major rotation turnover.

Recent four-start window:
- **17⅔ innings**
- **3.57 ERA**
- **5.57 FIP**
- 16 hits
- 4 home runs
- 6 walks
- 13 strikeouts

Latest two starts:
- roughly five innings each;
- three runs allowed in each.

At Comerica Park:
MLB's official preview notes approximately a **3.19 ERA in three home starts**, compared with a materially higher road ERA.

### Anderson interpretation

The central branch is not an automatic blowup.

His recent run prevention has been respectable.

But the underlying recent profile contains:
- home-run susceptibility;
- weaker strikeout-minus-walk quality than Skubal;
- a hook point around the middle innings.

That creates a meaningful Dodgers 5–7 run tail.

This tail is why:
- Tigers +2.5 is not `SUPPORTED`;
- Under 7.5 is only a moderate lean.

---

# Bullpen / exposure state

Detroit had a scheduled off day immediately before this series after completing its Rays set.

That generally improves availability for:
- leverage relievers;
- matchup choices behind Anderson.

Los Angeles arrive directly from the Atlanta series.

The Dodgers' recent series included:
- a 4-3 loss;
- a 6-5 loss with late bullpen involvement;
- a 1-0 loss where Yoshinobu Yamamoto worked into the seventh.

Thus Los Angeles have a less clean freshness state than Detroit.

However, Skubal's expected ability to work deeper reduces the amount of Dodgers bullpen exposure in the central branch.

The bullpen factor therefore slightly supports:
- Tigers +2.5;
- rather than materially reversing the Dodgers ML lean.

---

# Offensive matchup

## Dodgers vs Anderson

Key mechanism:
- elite top of order;
- multiple left-handed hitters against a right-handed starter;
- Anderson's recent HR/FIP weakness;
- deep power clustering.

Main suppression factors:
- Dodgers' current August offensive slowdown;
- Detroit's fresher bullpen;
- Comerica Park's larger dimensions;
- modest wind-in conditions around first pitch.

Central Dodgers run range:
**3–5**

Upper tail:
**6–8**

---

## Tigers vs Skubal

Key threats:
- right-handed-heavy lineup;
- Gleyber Torres/Dingler/Torkelson/Valencia contact-power branches;
- home-field last-bat entitlement.

Main suppressors:
- Skubal's elite strikeout/command;
- Detroit's recent 3.2 runs/game;
- 16-25 record vs left-handed starters;
- several young/small-sample hitters.

Central Detroit run range:
**1–3**

Upper tail:
**4–5**

---

# Park and weather

National Weather Service Detroit forecast for Friday evening:
- mostly clear;
- dry;
- temperature falling from near 80°F;
- light wind.

Current game-day conditions near the park were around:
- mid-70s °F;
- partly cloudy;
- wind approximately 7 mph **in from left field**.

No precipitation mechanism is material.

The wind-in direction gives a small home-run suppression mechanism, but weather is not strong enough to dictate the total.

---

# Recent game environment

## Dodgers

Recent scores include:
- 4-3
- 4-0
- 3-4
- 5-6
- 0-1

Six of the Dodgers' last eight were reportedly decided by one run.

That recent close-game distribution materially supports **Detroit +2.5**.

It is not used as an automatic cover rule; it is reconciled with:
- Skubal's strong starter edge;
- Anderson's home-run tail.

## Tigers

Detroit:
- 2-8 last 10;
- 32 runs in last 10;
- 10 losses in 12.

This current offensive/competitive regime strongly supports:
- Dodgers ML.

But Detroit's home field and rested relief chain preserve the narrow-loss branch.

---

# Joint run corridor

## Branch A — central Dodgers narrow win

Representative scores:
- Dodgers 3-2
- Dodgers 4-2
- Dodgers 4-3

Favours:
- Tigers +2.5
- Dodgers ML
- Under 7.5 in 3-2 and 4-2
- 4-3 remains Under at exactly 7 total

This is the central branch.

---

## Branch B — Skubal domination / low total

Representative:
- Dodgers 3-0
- Dodgers 4-1
- Dodgers 2-1

Mechanism:
- Skubal suppresses baserunners;
- Anderson survives five competitive innings;
- both bullpens prevent clustering.

Favours:
- Dodgers ML
- Under 7.5
- Tigers +2.5 in 2-1 / 3-2-type variants, but not 3-0 or 4-1.

---

## Branch C — Dodgers separation

Representative:
- Dodgers 5-1
- Dodgers 6-2
- Dodgers 7-2

Mechanism:
- Anderson HR/contact tail;
- Dodgers top order converts multiple baserunners;
- Detroit is forced into lower-leverage relief;
- Skubal keeps Detroit suppressed.

Favours:
- Dodgers ML
- defeats Tigers +2.5
- Over becomes live at 6-2 and above.

This is the strongest kill path for rank #1.

---

## Branch D — open game

Representative:
- Dodgers 6-4
- Tigers 5-4
- Dodgers 7-3

Mechanism:
- Skubal has an ordinary/shorter start;
- Detroit's right-handed bats convert mistakes;
- Anderson also allows power;
- both bullpens are exposed.

Favours:
- Over 7.5
- Tigers +2.5 in close versions;
- Dodgers ML only in LAD-win versions.

---

## Branch E — Detroit upset

Representative:
- Tigers 3-2
- Tigers 4-3

Mechanism:
- Anderson's home-start branch persists;
- Dodgers' August offensive malaise continues;
- Detroit scratches out two or three isolated Skubal runs and wins late.

Favours:
- Tigers +2.5
- often Under 7.5
- kills Dodgers ML.

---

# Final ranking

| Rank | Candidate | Pick | Verdict | Evidence | Probability |
|---:|---|---|---|---|---|
| **1** | `P-137-C02` | **Tigers +2.5** | `LEAN` | `MEDIUM-HIGH` | `NOT_GENERATED` |
| **2** | `P-137-C01` | **Dodgers ML** | `LEAN` | `MEDIUM-HIGH` | `NOT_GENERATED` |
| **3** | `P-137-C04` | **Under 7.5 Runs** | `LEAN` | `MEDIUM` | `NOT_GENERATED` |
| **4** | `P-137-C03` | **Over 7.5 Runs** | `AVOID` | `MEDIUM` | `NOT_GENERATED` |

---

# Detailed ranking rationale

## #1 — Detroit Tigers +2.5

This is the broadest robust contract.

It wins if:
- Detroit wins;
- Detroit loses by one;
- Detroit loses by two.

The most likely Dodgers-win branch is not necessarily a blowout.

Why the cushion is strong:
- Dodgers' recent offence has cooled;
- six of their last eight games were one-run games;
- Anderson has been respectable in recent starts;
- Anderson has a better home ERA;
- Detroit's bullpen enters with better rest;
- Comerica and light wind-in conditions do not enhance the Dodgers' HR tail.

Why it can fail:
- Skubal suppresses Detroit almost completely;
- Anderson's 5.57 recent FIP / HR susceptibility materialises;
- Dodgers win 5-1, 6-2 or wider.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM-HIGH`

---

## #2 — Dodgers ML

Los Angeles owns the strongest winner pathway.

Why:
- Skubal is by far the stronger starter;
- Dodgers are 80-54;
- Tigers are 62-71;
- Detroit is 2-8 in its last 10;
- Tigers have scored only 32 runs in those 10;
- Detroit is 16-25 vs left-handed starters;
- Dodgers lineup has substantial top-end and power depth.

Why not rank #1:
the moneyline loses every Detroit upset, while Tigers +2.5 survives all Detroit wins and narrow Dodgers wins.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM-HIGH`

---

## #3 — Under 7.5

Central run environment:
approximately **5–7 runs**.

Support:
- Skubal;
- Detroit recent offensive weakness;
- Dodgers current August slowdown;
- Detroit fresh bullpen;
- Comerica/light wind-in run-suppression;
- several recent low-scoring Dodgers games.

Why only medium:
- 7.5 is a low MLB total;
- Anderson's recent 5.57 FIP and four HR allowed create a real Dodgers power tail;
- Dodgers still possess Ohtani/Freeman/Betts/Muncy/Tucker/Teoscar;
- late bullpen sequencing can turn a 4-2 game into 6-3 rapidly.

**Verdict:** `LEAN`

---

## #4 — Over 7.5

The Over has a specific route:
- Anderson early HR/contact damage;
- Skubal allows two or three instead of zero/one;
- Detroit relief is forced into low leverage;
- game reaches 6-2 / 5-4 / 7-2.

But the central branch requires only moderate Dodgers scoring plus very low Detroit scoring.

That places the Over below the other three.

**Verdict:** `AVOID`

`AVOID` is evidence-relative only, not a negative-value claim.

---

# Potential game winner

## Los Angeles Dodgers — `LEAN / MEDIUM-HIGH`

Central reasons:
- major starting-pitcher advantage;
- stronger overall roster;
- much stronger season record;
- Detroit's current offensive decline;
- Detroit's poor current record versus left-handed starters.

Strongest failure path:
Anderson extends his home-start form, the Dodgers' recent offensive slump persists, and Detroit scratches out a low-scoring home win after Skubal exits.

---

# Coherence statement

The forecast is deliberately **not**:

> Dodgers are better, therefore Dodgers should also cover every wide margin.

The correct joint tree separates:

1. **winner**
2. **margin**
3. **total**

A central **Dodgers 4-2** result produces:

- Dodgers ML — WIN
- Tigers +2.5 — WIN
- Under 7.5 — WIN
- Over 7.5 — LOSS

That is the core forecast shape.

---

# Source record

## Google Drive framework
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- active Sports Research learning/model/evaluation controls

## Official MLB / Statcast
- MLB 2026 schedule
- MLB probable pitchers
- Dodgers probable-pitcher page
- MLB Skubal return-to-Detroit feature
- MLB Statcast Game Preview
- MLB matchup preview

## Current lineup cross-checks
- current Detroit media reproducing official Tigers lineup
- current Los Angeles media reproducing official Dodgers lineup
- current game tracker / lineup databases used for cross-check only

## Current performance sources
- Baseball-Reference matchup page
- StatMuse recent team scoring
- Reuters Dodgers-Braves final
- current Dodgers/Tigers reporting for Skubal and Anderson form

## Weather
- National Weather Service Detroit/Pontiac forecast
- current game-day park-condition cross-check

## Source limitations
- MLB's web-crawled starting-lineup page was not fully refreshed at the cutoff even though current team lineup posts were circulating.
- Exact operator listed-pitcher/action rules were not supplied.
- No fitted or validated baseball probability model exists.
- Bullpen role availability was assessed qualitatively rather than from a complete machine-readable same-day pitch-usage ledger.

---

# Logging confirmation

**Canonical ID:** `P-137`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Delivery mode:** `DOWNLOADABLE MARKDOWN FILE`

**GAME-STATE:** `PREGAME / WARMUP AT FINAL VERIFIED STATE`

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

**Retrospective:** `NOT INCLUDED`

**Important:** This forecast was frozen immediately before the scheduled first pitch. If the game has started when this file is opened, it must not be reinterpreted as a live forecast without a new verified inning/score/base-out/pitcher state.

# P-138 — Miami Marlins (Eury Pérez) @ Washington Nationals (Jackson Kent) — MLB

## Executive Forecast

|  Rank | Pick                               | Verdict       | Evidence      |
| ----: | ---------------------------------- | ------------- | ------------- |
| **1** | **Miami Marlins Moneyline**        | `LEAN`        | `MEDIUM-HIGH` |
| **2** | **Combined Total Under 8.5 Runs**  | `LEAN`        | `MEDIUM-HIGH` |
| **3** | **Washington Nationals +1.5 Runs** | `FORCED RANK` | `MEDIUM`      |
| **4** | **Combined Total Over 8.5 Runs**   | `AVOID`       | `MEDIUM`      |

**Potential game winner:** **Miami Marlins — LEAN**

### Central qualitative score corridor

* Miami 3-2
* Miami 4-2
* Miami 4-3
* Miami 5-2

The centre of the distribution is therefore:

`MIAMI WIN + MODERATE TOTAL`

rather than either a Nationals upset or an automatic Kent-driven slugfest.

---

## Record Metadata

| Field                 | Recorded value                                                      |
| --------------------- | ------------------------------------------------------------------- |
| Canonical ID          | `P-138`                                                             |
| Sport                 | Baseball                                                            |
| League                | MLB                                                                 |
| Event                 | Miami Marlins @ Washington Nationals                                |
| Venue                 | Nationals Park, Washington, DC                                      |
| Date                  | 2026-08-28 local / 2026-08-29 Melbourne                             |
| Scheduled first pitch | 6:45 PM EDT                                                         |
| Melbourne equivalent  | 8:45 AM AEST                                                        |
| Final state           | `OFFICIAL MLB PREVIEW / PREGAME VIEW FROZEN AROUND SCHEDULED START` |
| Miami starter         | Eury Pérez — RHP                                                    |
| Washington starter    | Jackson Kent — LHP                                                  |
| Starter status        | `PROBABLE_OFFICIAL / MLB VERIFIED`                                  |
| Method                | `MDS-2026.08.28-v2.4`                                               |
| Baseball module       | `RULES_BASEBALL.md`                                                 |
| Numerical model       | `NOT FIT / NOT VALIDATED`                                           |
| Probability state     | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`                |
| Value state           | `NO VALUE DETERMINABLE`                                             |
| Google Drive          | `READ-ONLY REFERENCE — NOT MODIFIED`                                |
| Retrospective         | `NOT INCLUDED — USER REQUEST`                                       |

> MLB's official scoreboard still displayed this matchup as `Preview` around the scheduled first-pitch time. This log therefore preserves the pregame evidence state. It must not later be treated as a live forecast without a verified inning/score/base-out/pitcher state.

---

# Framework Controls Applied

The active Sports Research baseball framework requires:

1. Exact MLB event and starter identity before pitcher-quality analysis.
2. Current batting-order and participant state where available.
3. Starter innings/batters-faced/hook distribution rather than ERA alone.
4. Explicit bullpen exposure and availability branches.
5. Small-sample starters represented as a mixture.
6. Current starter regime reconciled against season/career prior.
7. HR/contact and early-hook tails retained even when the central total is low.
8. Winner, run line and total derived from one joint run corridor.
9. Home ninth-inning entitlement treated as score-state dependent.
10. No numerical probability/value claim without a fitted and validated model.

---

# Frozen Decision Set

**Decision-set ID:** `DS-P-138-V01`

| Candidate ID | Exact contract            |
| ------------ | ------------------------- |
| `P-138-C01`  | Miami Marlins ML          |
| `P-138-C02`  | Washington Nationals +1.5 |
| `P-138-C03`  | Combined Total Over 8.5   |
| `P-138-C04`  | Combined Total Under 8.5  |

---

# Contract Geometry

## Marlins ML

Wins on any Miami victory.

Extra-inning/action rules depend on the user's operator, which was not supplied.

---

## Nationals +1.5

Wins if:

* Washington wins; or
* Washington loses by exactly one run.

Loses if:

* Miami wins by two or more.

### Important dependence

Miami ML and Washington +1.5 can **both win** if Miami wins by exactly one run.

Example:

**Miami 3-2 Washington**

* Marlins ML — WIN
* Nationals +1.5 — WIN
* Under 8.5 — WIN

---

## Total

**Over 8.5**

* 9+ runs

**Under 8.5**

* 8 or fewer runs

No push exists.

---

# Starter Identity Gate

MLB officially lists:

## Miami

**Eury Pérez — RHP**

* 7-9
* 3.17 ERA
* 137 strikeouts

## Washington

**Jackson Kent — LHP**

* 0-2
* 8.03 ERA
* 14 strikeouts

Both participants pass the exact-event starter identity handshake.

---

# Eury Pérez — Current Regime

## August performance

Pérez's August starts before this game:

* at Atlanta: 5 IP, 4 ER, 9 K
* vs Pittsburgh: 7 IP, 0 ER, 7 K
* vs Cincinnati: 6 IP, 0 ER, 5 K
* vs Washington: 5 IP, 1 ER, 4 K

August aggregate:

* **23 IP**
* **15 H**
* **5 ER**
* **1.96 ERA**
* **25 K**
* **12 BB**
* no home runs allowed in that four-start Statcast log

This is materially better than simply taking his season 3.17 ERA.

Contemporaneous reporting after his August 22 Washington start placed his ERA at roughly **1.80 since returning from injury in June**.

### Pérez run-suppression mechanism

`high strikeout ceiling + difficult contact profile + Washington's recent offensive inconsistency -> fewer sustained Nationals scoring clusters`

Pérez is therefore the single strongest player-level input in the game.

---

# Pérez vs Current Washington Hitters

Baseball Savant's current-roster matchup sample contains approximately:

* 61 PA
* .255 batting average
* .352 wOBA
* 16.4% strikeout rate
* 8.2% walk rate

This is not complete domination.

Washington's current hitters have made enough contact against Pérez historically to preserve:

* 2-run branch;
* 3-run branch;
* isolated HR/XBH branch.

That prevents an overly aggressive shutout projection.

---

# Jackson Kent — Small-Sample Mixture

Kent's MLB headline line:

* 3 starts
* 12⅓ IP
* 15 hits
* 11 earned runs
* 11 walks
* 14 strikeouts
* 1 home run
* 8.03 ERA
* roughly 2.11 WHIP

The Drive rules prohibit simply treating an 8.03 ERA from three starts as his true talent.

## Minor-league prior

Before his promotion, Kent had:

* 9-4 record
* 3.72 ERA
* 105 strikeouts
* 94⅓ IP
* 1.12 WHIP
* .216 opponent batting average
* .277 opponent OBP

across Double-A and Triple-A.

That is a materially stronger underlying prior than his first three MLB starts.

---

# Kent's Three MLB Starts

## vs Cubs

* 4 IP
* 3 ER
* 5 BB
* 6 K

## at Texas

* 4⅔ IP
* 5 ER
* 8 H
* 3 BB
* 3 K
* 1 HR

## at Miami

* **5⅔ IP**
* **4 H**
* **3 ER**
* **3 BB**
* **5 K**

His most recent start was already against this Marlins team and was clearly his best MLB outing.

Therefore the correct pitcher mixture is:

### Kent good branch

* 5–6 innings
* 2–3 runs
* competitive game

### Kent ordinary branch

* 4–5 innings
* 3–4 runs
* bullpen enters early-middle innings

### Kent bad/contact branch

* inefficient command
* 4+ runs
* early hook
* Miami reaches Washington relief before the sixth

This mixture is central to both the total and Nationals +1.5.

---

# Current Lineup Context

## Miami

Current reports around first pitch identified:

* Kyle Stowers back from the injured list and starting at first base
* Xavier Edwards in the middle-infield/OBP core
* Otto Lopez
* Javier Sanoja
* Miami's usual young outfield/left-handed depth around them

Stowers' return modestly strengthens the Miami run-production branch against a young left-handed starter.

Miami's recent offence, however, has not been overwhelming.

---

## Washington

Current reports identified:

* CJ Abrams returning to shortstop
* Jorbit Vivas at second
* Brady House at third
* Abimelec Ortiz returning
* Harry Ford returning
* Nasim Nuñez resting

Abrams' return improves Washington's offensive ceiling versus the lineup Pérez faced in some recent games.

Therefore Washington's attack is not treated as identical to last weekend's version.

---

# Current Team Form

## Miami

Record:
**68-66**

Last 10:
**5-5**

Runs scored in last 10:
**39**

Average:
**3.9 runs/game**

Recent results include:

* 1-4 Phillies
* 3-2 Nationals
* 4-2 Nationals
* 6-2 Nationals
* 2-4 Red Sox
* 3-7 Red Sox
* 4-0 Red Sox

Miami are winning enough games, but the offence is currently more **moderate** than explosive.

---

## Washington

Record:
**63-73**

Last 10:
**2-8**

Last 20:
**7-13**

Last 30:
**9-21**

Home:
approximately **28-38**

Against RHP:
approximately **39-54**

The Nationals did just beat Colorado 7-1, so their offence is not assumed dead.

But the broader current regime remains weak.

---

# Season-Series Audit

Miami lead the season series:

**8-1**

Results:

* Washington 3-2 Miami
* Miami 8-7 Washington
* Miami 5-2 Washington
* Miami 7-3 Washington
* Miami 7-3 Washington
* Miami 4-1 Washington
* Miami 3-2 Washington
* Miami 4-2 Washington
* Miami 6-2 Washington

### Total classification at 8.5

Totals:

* 5
* 15
* 7
* 10
* 10
* 5
* 5
* 6
* 8

Under 8.5:
**6 of 9**

Over 8.5:
**3 of 9**

### Nationals +1.5 descriptive result

Washington +1.5 would have won in:

* Washington's 3-2 win
* Miami's 8-7 win
* Miami's 3-2 win

and failed in the other six.

This is descriptive matchup context only.

It is **not** treated as a calibrated 3/9 probability.

---

# Most Relevant Recent Series

Only six days ago Miami swept Washington:

### Miami 3-2

Total: 5

### Miami 4-2

Total: 6

### Miami 6-2

Total: 8

All three:

* Marlins ML — WIN
* Under 8.5 — WIN

Nationals +1.5:

* 1 cover
* 2 failures

This is particularly relevant because the current player regimes have considerable continuity.

---

# Bullpen Tree

## Miami

The bullpen is not at full strength.

Closer **Pete Fairbanks** was placed on the 15-day IL on August 25 with right median nerve irritation.

Recent late-inning alternatives include **Calvin Faucher**, who entered this game period with:

* 57 appearances
* 3.99 ERA
* 63 strikeouts in 56⅓ IP

Faucher recently recorded a save against Washington.

Miami therefore still has usable late relief, but the Fairbanks injury increases:

* ninth-inning variance;
* Washington comeback probability;
* Nationals +1.5 tail;
* Over tail.

This is one reason Marlins ML is `LEAN`, not `SUPPORTED`.

---

## Washington

Washington's bullpen worked **4⅔ scoreless innings** in the previous day's 7-1 win over Colorado.

That demonstrates useful current relief performance but also means the unit does not enter after a completely idle day.

Kent's hook point is therefore important:

* 5⅔–6 IP Kent branch = manageable relief exposure;
* 3–4 IP Kent branch = materially larger Washington bullpen risk.

---

# Park / Weather

Nationals Park conditions near first pitch were forecast around:

* low-80s °F / high-20s °C
* humid
* light/moderate northerly to northeasterly wind
* low rain probability by first pitch

There is no major delay/rain suppression mechanism.

Warm conditions preserve carry/offence, but the weather is not strong enough to override the pitcher matchup.

No automatic Over adjustment is applied.

---

# Joint Run Distribution

## Branch A — Central Miami win / Under

Representative:

* Miami 3-2
* Miami 4-2
* Miami 4-3

Mechanism:

* Pérez gives Miami 5–6 strong innings;
* Washington produces isolated damage but not sustained rallies;
* Kent is competitive enough to prevent early separation;
* Miami edges Washington's bullpen late.

Favours:

* Marlins ML
* Under 8.5
* Nationals +1.5 only in 3-2 / 4-3

This is the **central branch**.

---

## Branch B — Pérez domination

Representative:

* Miami 3-0
* Miami 4-1
* Miami 5-1

Mechanism:

* Washington struggles to square Pérez;
* Miami scratches runs against Kent;
* Nationals chase from behind.

Favours:

* Marlins ML
* Under 8.5
* usually defeats Nationals +1.5

---

## Branch C — Kent good-start / one-run game

Representative:

* Miami 3-2
* Washington 3-2
* Miami 4-3

Mechanism:

* Kent reproduces or improves on his 5⅔ IP / 3 ER Miami outing;
* Pérez is strong but not untouchable;
* bullpens decide the result.

Favours:

* Nationals +1.5
* usually Under
* Miami ML only in Miami-win versions

This is the main support for rank #3.

---

## Branch D — Kent command/contact failure

Representative:

* Miami 6-2
* Miami 7-2
* Miami 7-3

Mechanism:

* walks extend innings;
* Miami's lefty/righty depth creates traffic;
* Kent exits early;
* Washington's bullpen absorbs excess innings.

Favours:

* Marlins ML
* defeats Nationals +1.5
* Over 8.5 becomes live at 7-2 / 7-3

This is the strongest Over pathway.

---

## Branch E — Washington offensive upset

Representative:

* Washington 4-3
* Washington 5-3

Mechanism:

* Abrams/House/Ortiz create extra-base traffic;
* Pérez has an ordinary rather than elite start;
* Miami's Fairbanks-less bullpen fails late.

Favours:

* Nationals +1.5
* kills Marlins ML
* total may remain Under at 4-3 or reach Over at 5-4/6-3 variants

---

# Strongest Kill Paths

## Marlins ML

Pérez gives up 3–4 runs instead of 1–2, Kent reproduces his best branch, and Washington exploits Miami's altered late-inning bullpen.

---

## Under 8.5

Kent's command breaks down early, Miami scores 6+, and Washington adds enough against Pérez/relief to push the game to 9+.

Example:
**Miami 6-3**

---

## Nationals +1.5

Pérez suppresses Washington and Miami's offence converts Kent's walks/contact into a multi-run lead.

Example:
**Miami 5-2**

---

## Over 8.5

Pérez performs close to his August baseline and Kent settles into another 5–6 inning competitive start.

Example:
**Miami 4-2**

---

# Final Ranking

|  Rank | Candidate   | Pick               | Verdict       | Evidence      |
| ----: | ----------- | ------------------ | ------------- | ------------- |
| **1** | `P-138-C01` | **Marlins ML**     | `LEAN`        | `MEDIUM-HIGH` |
| **2** | `P-138-C04` | **Under 8.5 Runs** | `LEAN`        | `MEDIUM-HIGH` |
| **3** | `P-138-C02` | **Nationals +1.5** | `FORCED RANK` | `MEDIUM`      |
| **4** | `P-138-C03` | **Over 8.5 Runs**  | `AVOID`       | `MEDIUM`      |

---

# Ranking Rationale

## #1 — Miami Marlins ML

Best-supported supplied contract.

Main evidence:

* substantial Pérez > Kent starter edge;
* Pérez's excellent August regime;
* Washington 2-8 in last 10;
* Miami 8-1 in the season series;
* Miami swept Washington only six days ago;
* Kent remains a three-start MLB uncertainty;
* Stowers' return improves Miami's lineup.

The main uncertainty comes from:

* Miami's only moderate recent offence;
* Kent's improved latest start;
* Washington home batting entitlement;
* Miami's Fairbanks-less bullpen.

**Verdict:** `LEAN — MEDIUM-HIGH`

---

## #2 — Under 8.5

Strongly coherent with the winner view.

Support:

* Pérez's August 1.96 ERA;
* Washington scored exactly two in each of the last three H2Hs;
* six of nine season meetings stayed below 8.5;
* Miami's last-10 offence averages only 3.9 runs;
* Kent's latest start suggests he can remain competitive rather than automatically implode.

The Under loses primarily through a Kent/relief blowup or an unusual Pérez off-game.

**Verdict:** `LEAN — MEDIUM-HIGH`

---

## #3 — Nationals +1.5

There is a credible close-game branch.

Support:

* Kent's latest start against Miami was substantially better;
* Miami's offence has been moderate recently;
* Fairbanks is unavailable;
* Washington has home ninth-inning entitlement;
* any Nationals win or one-run loss cashes the contract.

But the cushion is only +1.5.

Miami have beaten Washington by 2+ runs in six of the nine season meetings, which materially limits confidence.

**Verdict:** `FORCED RANK — MEDIUM`

---

## #4 — Over 8.5

The Over is not impossible.

It becomes strong if:

* Kent walks multiple hitters and exits early;
* Miami reaches 6–7;
* Washington contributes 2–3;
* either bullpen allows clustered late scoring.

However, that requires moving away from the central Pérez-led run-suppression branch.

The 8.5 threshold also gives the Under considerably more room than a 7.0/7.5 total would.

**Verdict:** `AVOID — MEDIUM`

`AVOID` means lowest-ranked among the four supplied contracts. It is not an expected-value statement.

---

# Potential Game Winner

## Miami Marlins — `LEAN / MEDIUM-HIGH`

Why:

* Pérez is the best pitcher in the matchup.
* Miami own a much stronger current H2H record.
* Washington are 2-8 over their last 10.
* Kent remains an uncertain rookie starter.
* Miami's offence does not need a high-end performance if Pérez holds Washington near 2 runs.

Strongest failure path:

`Kent good-start branch + Pérez ordinary branch + Washington home ninth + Miami closer-depth issue`

produces a close Nationals win.

---

# Coherence Statement

The forecast is not:

> Miami should win, therefore Washington +1.5 must be bad and the game must go Over.

The contracts answer different questions.

A central:

**Miami 4-2**

produces:

* Marlins ML — **WIN**
* Nationals +1.5 — **LOSS**
* Under 8.5 — **WIN**
* Over 8.5 — **LOSS**

A narrower:

**Miami 3-2**

produces:

* Marlins ML — **WIN**
* Nationals +1.5 — **WIN**
* Under 8.5 — **WIN**
* Over 8.5 — **LOSS**

Both are coherent branches of the same run distribution.

---

# Final Card

1. **Miami Marlins ML**
2. **Combined Total Under 8.5 Runs**
3. **Washington Nationals +1.5**
4. **Combined Total Over 8.5 Runs**

**Potential winner:** **Miami Marlins**

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

---

# Source Record

## Google Drive framework

* `RULES_BASEBALL.md`
* `RULES_GENERAL.md`
* active model/evaluation specifications

## Official MLB / Statcast

* MLB probable pitchers — Pérez/Kent identity
* MLB scoreboard / game state
* Baseball Savant game preview
* Baseball Savant Eury Pérez current game log
* Washington Nationals official Jackson Kent promotion release
* Miami Marlins official transactions

## Current reporting/statistics

* Baseball-Reference current matchup page
* Reuters recent Pérez/Marlins–Nationals coverage
* StatMuse Marlins recent run totals
* current Nationals/Marlins game-thread reporting for lineup changes

## Weather

* National Weather Service Washington-area hourly forecast

---

# Source / Model Limitations

* The user's sportsbook/operator was not supplied, so exact listed-pitcher/action and extra-inning settlement rules are not frozen.
* MLB's web starting-lineup endpoint was still partly stale around the research cutoff; current lineup components were cross-checked through contemporaneous team/game reporting.
* Kent has only three MLB starts, so his true run distribution remains wide.
* Miami's late-inning bullpen changed materially after Pete Fairbanks went on the IL.
* No fitted/validated baseball numerical model currently exists in the Sports Research framework.

---

# Logging Confirmation

**Canonical ID:** `P-138`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Retrospective:** `NOT INCLUDED — USER REQUEST`

**Delivery mode:** `INLINE MARKDOWN LOG`

**State:** `OFFICIAL MLB PREVIEW / PREGAME VIEW FROZEN AROUND SCHEDULED FIRST PITCH`

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

# P-138 — Atlanta Falcons @ Miami Dolphins — NFL Preseason Week 3

## Executive forecast

**Method:** `MDS-2026.08.29-v2.5`  
**Numerical status:** `NTS-2026.08.25-v0.2 — Stage 0 / no fitted football model`  
**GAME-STATE at final verified refresh:** `PREGAME`  
**Final verified refresh:** 2026-08-29 08:57:59 Australia/Melbourne  
**Official kickoff:** 2026-08-28 19:00 America/New_York / 2026-08-29 09:00 Australia/Melbourne  
**Venue:** Hard Rock Stadium, Miami Gardens, Florida  
**Competition:** NFL Preseason Week 3  
**Google Drive:** read-only reference; not modified

> **Participant-status cap:** Atlanta officially confirmed Tua Tagovailoa will start and Michael Penix Jr. will not play. Miami's decisive late quarterback/rotation report — Malik Willis and De'Von Achane sitting, Quinn Ewers unavailable and Cam Miller expected to start — was current named reporting citing NFL Network, but was not independently recovered from a field-owning Dolphins/NFL lineup release before the cutoff. Under `RULES_GENERAL.md`, this keeps the Miami QB role `SECONDARY_ONLY` and caps participant-sensitive rows at `FORCED RANK / MEDIUM-LOW`.

## Final ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Combined Total Under 36.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Atlanta Falcons -5.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Combined Total Over 36 Points** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Miami Dolphins +5.5** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **Atlanta Falcons — FORCED WINNER / LOW CONFIDENCE**

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`

---

# 1. Identity, target and contract freeze

**Target ID:** `AMFOOT_NFL_PRE_FULL_JOINT_SCORE-v1-QUAL`  
**Target definition:** final Atlanta and Miami points at the end of the NFL preseason game under the league's current preseason endpoint.  
**Unit:** integer points.  
**Start state:** pregame.  
**Exposure:** full regulation game; drives, plays, field position and special-teams opportunities are uncertain.  
**Termination:** official end of the preseason game.  
**Operator:** not supplied.  
**Market settlement assumption:** standard full-game NFL spread/total settlement; exact sportsbook-specific void/action wording remains unknown.

The current NFL overtime rulebook applies overtime to regular-season and postseason games; current preseason games are therefore treated as ending after regulation if tied.

## Supplied candidate slate

- `P-138-C01` — Falcons -5.5
- `P-138-C02` — Dolphins +5.5
- `P-138-C03` — Over 36
- `P-138-C04` — Under 36.5

### Spread geometry

The half-point spread is an exact complement:

- Falcons -5.5 wins if Atlanta wins by **6+**.
- Dolphins +5.5 wins if Miami wins/ties or loses by **1–5**.

### Total geometry

The total rows are **not exact half-point complements** because the Over is at an integer:

- Over 36 wins at **37+**, pushes at **36**, loses at **35 or fewer**.
- Under 36.5 wins at **36 or fewer**, loses at **37+**.

At exactly **36 points**, Under 36.5 wins while Over 36 pushes.

---

# 2. Updated Drive framework applied

The active Drive framework requires:

- NFL preseason to be treated as a separate phase population;
- starting QB, backup branch and expected reps to be decision-driving;
- starter quality to matter only for the snaps actually expected;
- line continuity and skill-player exposure to be treated as mixtures;
- drive outcomes, field position, red-zone conversion, turnovers and special teams to feed one discrete joint score tree;
- exact football key values and push mass to be preserved;
- one common score corridor to generate winner, spread and total;
- participant fields that remain secondary-only to trigger an evidence cap.

The active canonical Drive snapshot lists `P-138` as the next canonical ID, so this event uses **P-138** under the updated Drive authority.

No direct comparable NFL-preseason D0 case was recovered from the active combined log under the predeclared query `NFL preseason + quarterback rotation + starter reps`; this is recorded as:

`D0 RETRIEVAL: NO COMPARABLE CASE`

No historical outcome vote was used.

---

# 3. Official/current event state

NFL and Falcons official sources list:

- Atlanta Falcons @ Miami Dolphins
- Friday, 28 August 2026
- 7:00 PM ET
- Hard Rock Stadium
- NFL Preseason Week 3

At 08:57:59 Melbourne / 18:57:59 ET, the NFL game feed still showed the game in pre-start state (`Q1 15:00`, no score).

Therefore:

`GAME-STATE: PREGAME`

---

# 4. Atlanta quarterback and unit regime

## Officially verified

Atlanta head coach Kevin Stefanski said the **starters will play**, including **Tua Tagovailoa**.

He did not publish a fixed snap count; he said the club has a plan but the actual number of plays will depend on how the game develops.

**Michael Penix Jr. will not play**, despite being medically cleared for full-team practice.

The expected Atlanta QB progression is therefore:

1. Tua Tagovailoa — starter exposure, limited/variable
2. Cooper Rush — reserve branch
3. Jack Strand — reserve/development branch

The exact snap split between Rush and Strand is not officially frozen.

## Why the Atlanta depth branch matters

Atlanta's Week 2 reserve offense was highly productive against Indianapolis:

- Falcons won **34-6**
- total offense: **461 yards**
- Cooper Rush: **10/11, 86 yards**
- Jack Strand: **12/17, 212 yards, 1 passing TD**
- Strand also scored a rushing TD
- Atlanta possessed the ball for **38:41**

That is not treated as a repeatable 34-point forecast.

The relevant mechanism is that Atlanta demonstrated:
- functional reserve-QB operation;
- sustained drives;
- explosive-pass access;
- usable reserve rushing;
- enough depth to avoid a complete offensive collapse when the starters leave.

Atlanta's Week 1 loss to Denver provides the counterweight:

- Denver won **27-7**
- Tua and the first-team offense gained only **28 net yards over eight snaps / two drives**
- Atlanta's offense was generally ineffective until later reserve action.

The current Atlanta branch is therefore **wider than one Week 2 result**:
- starter offense can still stall;
- reserve offense has nevertheless shown a much higher ceiling than Miami's recent reserve-QB output.

---

# 5. Miami quarterback / rotation regime

## Broad official baseline

Miami's official preseason QB room includes:
- Malik Willis
- Quinn Ewers
- Cam Miller
- Mark Gronowski

Malik Willis entered camp as the presumptive regular-season starter.

## Current late report — important but secondary-only

Current named reporting shortly before kickoff, citing NFL Network's Cameron Wolfe, reported:

- **Malik Willis will not play**
- **De'Von Achane will not play**
- **Quinn Ewers will sit because of injury**
- **Cam Miller will start**
- many other Miami starters will sit

Because a field-owning Dolphins/NFL starting-QB release was not independently recovered before the cutoff, this remains:

`MIA QB1 FOR THIS GAME: SECONDARY_ONLY`

This is a major forecast limitation.

The framework therefore does **not** permit a `LEAN`/`SUPPORTED` label on rows whose direction depends heavily on this rotation.

## What is still knowable from completed preseason games

Miami is 0-2:

- at Washington: **L 7-20**
- vs New York Giants: **L 3-26**

The reserve passing process has been weak.

Quinn Ewers' Week 1 line:
- **1/8**
- **27 yards**
- **0 TD**
- **1 INT**
- passer rating **1.6**

Against the Giants:
- Cam Miller: **6/11, 60 yards**
- Mark Gronowski: **2/5, 1 yard**
- Miami scored only **3 points**

Raw preseason points are not treated as a stable offensive coefficient. The mechanism is more relevant:

`uncertain/developmental QB reps + limited explosive passing + reserve-line/skill rotation -> lower sustained-drive and red-zone expectations`

That supports the Under and Atlanta side **if** the current late QB/rotation report is accurate.

---

# 6. Preseason form reconciliation

## Atlanta

Preseason:
- vs Denver: **L 7-27**
- at Indianapolis: **W 34-6**

Average score:
- Atlanta 20.5
- opponent 16.5
- combined 37.0

But averaging those two games is not the model.

They arose from different QB/unit mixtures.

The important current evidence is Atlanta's plan to use starters briefly and then turn to Rush/Strand, whose latest reserve performance was strong.

## Miami

Preseason:
- at Washington: **L 7-20**
- vs Giants: **L 3-26**

Average:
- Miami 5.0
- opponent 23.0
- combined 28.0

Again, the raw average is not the model.

The persistent mechanism is poor reserve passing and a likely final-game emphasis on roster evaluation rather than protecting regular-season starter continuity.

---

# 7. Drive / possession process

## Atlanta scoring path

Central chain:

`brief starting-unit reps -> competent reserve QB play -> field-position advantage -> moderate scoring efficiency`

Key supports:
- Tua starts.
- Rush and Strand are experienced/currently productive enough to operate the offense.
- Atlanta generated 461 yards last week.
- Miami's late reported plan removes many starters.

Primary Atlanta downside:
- preseason play-calling becomes conservative;
- Tua's starter reps are extremely short;
- the Colts game proves less transferable than it looks;
- penalties and reserve-line mistakes kill drives.

## Miami scoring path

Central chain:

`reserve/developmental QB exposure -> conservative calls + pressure/third-down difficulty -> limited sustained scoring`

Main upper tail:
- Atlanta rotates deeply on defense;
- Miami gets short fields from turnovers/special teams;
- Cam Miller/Gronowski creates an explosive play;
- fourth-down aggression extends drives.

---

# 8. Weather and field environment

Hard Rock Stadium is open-air.

Current local reporting expected:
- hot/humid conditions;
- showers mainly earlier in the afternoon;
- drying by early evening.

A current game-weather cross-check near kickoff had roughly:
- high-80s °F;
- light E/ESE wind;
- low immediate precipitation risk.

There is no strong wind mechanism that materially suppresses passing/kicking.

Heat/humidity may matter through substitution frequency and fatigue, but in a preseason game with heavy rotation it is not assigned a one-directional total effect.

---

# 9. Market-state cross-check — not sports-model evidence

A current BetMGM snapshot showed approximately:

- Atlanta **-4.5**
- Miami **+4.5**
- total **36.5**

The user's alternate spread is:
- Atlanta **-5.5**
- Miami **+5.5**

The user's total pair is:
- Over **36**
- Under **36.5**

This market snapshot is recorded **only** for contemporaneous contract context.

It is **not** used as an internal probability and does not establish value.

---

# 10. Joint qualitative score tree

## Branch A — central Atlanta control / low total

Representative:
- Falcons 20-10
- Falcons 23-10
- Falcons 24-10

Mechanism:
- Atlanta QB depth functions;
- Miami struggles to sustain drives;
- Atlanta controls field position without needing a high-tempo passing game.

Contract effects:
- Falcons -5.5: WIN
- Dolphins +5.5: LOSS
- Under 36.5: WIN
- Over 36: LOSS

This is the **central branch**.

---

## Branch B — Atlanta separation with Miami nearly shut down

Representative:
- Falcons 24-6
- Falcons 27-7
- Falcons 30-6

Mechanism:
- Miami reserve offense repeatedly goes three-and-out;
- Atlanta gets short fields;
- Falcons backups continue Week 2 efficiency.

Effects:
- Falcons -5.5: WIN
- Under 36.5: still wins in all three example scores
- Dolphins +5.5: LOSS

This is why **Under and Atlanta -5.5 are positively compatible**, not contradictory.

---

## Branch C — open preseason / short-field scoring

Representative:
- Falcons 27-13
- Falcons 30-10
- Falcons 27-17

Mechanism:
- turnovers;
- fourth-down aggression;
- special-teams field position;
- reserve defensive busts;
- late two-minute offense.

Effects:
- Over 36: WIN in all examples
- Falcons -5.5: WIN in all examples

This is the strongest Over branch.

---

## Branch D — Miami late cover

Representative:
- Falcons 20-17
- Falcons 23-20
- Dolphins 20-17

Mechanism:
- Atlanta starters exit early;
- Falcons reserve offense regresses;
- Miami's developmental QB produces enough late drives against deep reserves;
- Atlanta prioritizes evaluation over game-state conservatism.

Effects:
- Dolphins +5.5: WIN
- Under 36.5 wins in 20-17? No — total 37, so Over 36 wins.
- close-game outcomes can therefore support Miami +5.5 and Over simultaneously.

This is the main kill path for Atlanta -5.5.

---

## Branch E — very low-output game

Representative:
- Falcons 17-7
- Falcons 17-10
- Falcons 20-7

Mechanism:
- both clubs become run-heavy;
- reserve offensive lines produce sacks/negative plays;
- red-zone drives end in field goals or empty possessions.

Effects:
- Under 36.5: WIN
- Falcons -5.5: WIN in all examples

---

# 11. Exact ranking rationale

## #1 — Under 36.5

Strongest central structure.

Support:
- Miami scored 7 and 3 in its first two preseason games.
- Miami's reserve passing process has been poor.
- current late reporting indicates Miami is sitting its presumptive QB1 and several starters.
- Atlanta does not need a high-volume scoring game to control the result.
- 24-10, 27-7 and even 30-6 all stay Under 36.5.

Strongest kill path:
- Atlanta's offense/short fields produce 27–30 and Miami contributes 10–17 against deep reserves.

Because Miami's exact QB rotation is not official-field-owner confirmed at cutoff:
`FORCED RANK — MEDIUM-LOW`

---

## #2 — Falcons -5.5

Support:
- Atlanta officially plans to play starters, including Tua.
- Penix is out, but Rush/Strand remain a relatively functional reserve sequence.
- Atlanta's reserve offense produced 461 yards last week.
- Miami's offense has scored only 10 preseason points.
- current late reporting strongly suggests Miami will sit many regular starters.

Why not #1:
- -5.5 is a meaningful preseason separation requirement.
- Atlanta's starters may play only briefly.
- late-game deep-reserve football creates large cover variance.
- Miami +5.5 wins every Miami victory and every Atlanta win by 1–5.

`FORCED RANK — MEDIUM-LOW`

---

## #3 — Over 36

The Over has a real structural path:
- Atlanta scores 27+;
- Miami generates at least two scoring drives;
- turnovers/short fields/non-offensive scores;
- fourth-down aggression and late reserve defensive busts.

The integer 36 line also gives a push at exactly 36 rather than a loss.

It stays below the Under because Miami's sustained offensive-drive outlook is the weakest unit-level process in the matchup.

`FORCED RANK — MEDIUM-LOW`

---

## #4 — Dolphins +5.5

The cushion is meaningful, but the current rotation evidence is unfavorable.

Miami cover path:
- Atlanta's starters exit rapidly;
- Rush/Strand regress;
- Miami's reserve QB group improves against deep Atlanta defenders;
- a late touchdown compresses margin.

Why last:
- Miami's first two preseason offensive performances were extremely weak.
- current late reporting removes Willis/Achane and many regulars.
- Atlanta retains a more credible multi-QB offensive chain.

`FORCED RANK — MEDIUM-LOW`

---

# 12. Potential winner

## Atlanta Falcons — `FORCED WINNER / LOW CONFIDENCE`

Atlanta is preferred because its **full-game QB/unit mixture** is stronger, not because its regular-season roster is simply better.

The expected winner path is:

`brief Tua/starters exposure + Rush/Strand reserve competence + Miami developmental offense -> Atlanta controls more scoring drives`

Strongest failure path:

`very short Atlanta starter exposure + reserve turnover/penalty variance + Miami late scoring against deep defensive reserves`

No numerical win probability is published.

---

# 13. Bottom line

### Best four in order

1. **Under 36.5**
2. **Falcons -5.5**
3. **Over 36**
4. **Dolphins +5.5**

### Potential winner
**Atlanta Falcons**

### Central score family
**Atlanta approximately 20–24, Miami approximately 7–13**

### Main upper tail
**Atlanta 27–30 with Miami 10–17**

### Main contrary state
**Atlanta starters exit quickly and Miami creates a late one-score game**

---

# 14. Source record

## Updated Google Drive framework
- `PREDICTION_LOG_COMBINED.md` — active canonical queue / next-ID authority
- `RULES_GENERAL.md`
- `RULES_AMERICAN_FOOTBALL.md`
- `AGENT_ROLE_AND_TASK.md`
- `MODEL_AND_DATA_SPEC.md`
- `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`
- `NUMERICAL_TRAINING_SPEC.md`
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `LEARNING_REGISTER.md`

## Current official sources
- NFL official game/schedule feed
- NFL Football Operations 2026 rulebook
- Atlanta Falcons official final-preseason preview
- Atlanta Falcons official depth chart
- Atlanta Falcons official Week 2 game center

## Current reputable reporting
- Reuters — Atlanta QB competition / Penix sitting / Tua starting
- NFL Network report as relayed by current Miami coverage — Miami late QB/starter plan
- current local Miami weather reporting

## Limitations
- Miami's exact final QB/starter rotation was not independently recovered from a field-owning official release before cutoff.
- Atlanta published no fixed snap count for its starters.
- Operator-specific grading/void terms were not supplied.
- No fitted/validated American-football model exists.
- Preseason personnel turnover makes regular-season team strength a weak prior.

---

# Logging / provenance note

The updated Drive canonical snapshot currently lists **P-139** as the next ID. This view therefore uses `P-138` under the Drive authority.

Earlier locally generated forecast files in this chat are not treated as canonical Drive entries unless separately reconciled into the active log.

**Google Drive modified:** `NO`

**Retrospective performed:** `NO`


# P-139 (conversation-local continuation) — Houston Astros (Hunter Brown) @ New York Mets (Christian Scott) — MLB

## Administrative note

Google Drive is being used as a **read-only framework source**. Its controlling snapshot has not been advanced by the immediately preceding locally delivered cards, so this entry is labelled **P-139 conversation-local continuation** to avoid reusing an ID in this chat. It should not be treated as the canonical Drive ID until reconciled into the active log.

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Houston Astros +1.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **New York Mets +1.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Combined Total Over 7.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Combined Total Under 7.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **Houston Astros — FORCED WINNER / LOW-MEDIUM CONFIDENCE**

### Central qualitative score corridor

- Astros 4-3
- Astros 5-3
- Mets 4-3
- Astros 5-4

This is a **close-game, 7–9 run** environment rather than a strong blowout or low-total state.

---

## Record metadata

| Field | Value |
|---|---|
| Sport | Baseball |
| League | MLB |
| Event | Houston Astros @ New York Mets |
| Venue | Citi Field, Queens, New York |
| Scheduled first pitch | 2026-08-28 19:10 America/New_York |
| Melbourne equivalent | 2026-08-29 09:10 Australia/Melbourne |
| Final research refresh | 2026-08-29 09:08:12 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Astros starter | Hunter Brown, RHP |
| Mets starter | Christian Scott, RHP |
| Starter status | `PROBABLE_OFFICIAL — MLB VERIFIED` |
| Starting batting orders | `NOT RELEASED / MLB OFFICIAL PAGE STILL TBD AT CUTOFF` |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_BASEBALL.md` |
| Numerical state | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 1. Framework controls applied

The updated baseball module requires:

- official event and starter identity before pitcher-quality analysis;
- official batting orders/catcher/defence where released;
- participant mixtures and evidence caps when official orders remain unreleased;
- starter batters-faced/pitch/inning/hook distributions rather than ERA-only reasoning;
- explicit bullpen-chain and workload treatment;
- season prior versus current starter-regime reconciliation;
- HR/contact and sequencing tails;
- home ninth-inning entitlement;
- +1.5 cushion decomposition;
- one joint run distribution for winner, run line and total.

Because MLB's official lineup page still displayed both batting orders as **TBD** at the final cutoff, every lineup-sensitive row is capped at:

`FORCED RANK / MEDIUM-LOW`

No numerical probability is published because no baseball model is fitted or validated.

---

# 2. Exact decision set

- `C01` — Astros +1.5
- `C02` — Mets +1.5
- `C03` — Over 7.5
- `C04` — Under 7.5

## Positive-run-line geometry

These are **not opposites**.

### Astros +1.5
Wins if:
- Houston wins; or
- Houston loses by exactly one.

### Mets +1.5
Wins if:
- New York wins; or
- New York loses by exactly one.

Therefore **both +1.5 contracts win simultaneously whenever the final margin is exactly one run**.

They can both lose only if neither condition is met? No: one of the teams must win, so at least the winning team's +1.5 always wins. The losing team's +1.5 fails only on a margin of 2+.

## Total geometry

- Over 7.5 wins at 8+ runs.
- Under 7.5 wins at 7 or fewer.
- No push exists.

---

# 3. Official event/starter verification

MLB's official probable-pitcher pages list:

## Houston
**Hunter Brown — RHP**
- 3-3
- 3.51 ERA
- 76 strikeouts

## New York
**Christian Scott — RHP**
- 4-3
- 3.73 ERA
- 111 strikeouts

The game is scheduled for **7:10 PM ET at Citi Field**.

At the final refresh around **7:08 PM ET**, the MLB page remained in **Preview / pregame** state.

---

# 4. Hunter Brown — season prior vs current regime

Season:
- 3.51 ERA
- approximately 74⅓ IP
- 76 strikeouts
- elevated walk rate / command volatility
- approximately 1.33 WHIP

Recent four starts:

| Date | Opponent | IP | ER | BB | K |
|---|---|---:|---:|---:|---:|
| Aug 22 | Athletics | 5.2 | 1 | 3 | 4 |
| Aug 16 | Mariners | 5.0 | 2 | 5 | 5 |
| Aug 11 | Giants | 5.0 | 3 | 3 | 4 |
| Aug 5 | Blue Jays | 6.0 | 3 | 2 | 8 |

Recent aggregate:
- 21⅔ IP
- 9 ER
- respectable central run suppression
- but persistent free-pass/efficiency risk

### Brown central mechanism

`above-average stuff + recent run suppression -> credible 2–3 run starter branch`

### Brown kill path

`walks + pitch-count inflation -> earlier exit -> already-taxed Houston bullpen`

Brown has not consistently delivered deep starts, which matters because Houston's bullpen enters under meaningful recent workload stress.

---

# 5. Christian Scott — season prior vs August regime

Season:
- 4-3
- 3.73 ERA
- 89⅓ IP
- 111 strikeouts
- approximately 1.32 WHIP

August starts:

| Date | Opponent | IP | ER | BB | K |
|---|---|---:|---:|---:|---:|
| Aug 22 | White Sox | 4.2 | 4 | 4 | 6 |
| Aug 16 | Nationals | 6.1 | 3 | 2 | 7 |
| Aug 10 | Braves | 4.0 | 4 | 1 | 6 |
| Aug 5 | Guardians | 5.0 | 3 | 2 | 7 |

August aggregate:
- 20.0 IP
- 14 ER
- **6.30 ERA descriptively**
- 26 strikeouts
- 9 walks
- 3 home runs allowed

The strikeout process remains strong, but his current run-prevention regime is materially worse than the season ERA.

### Scott central mixture

Do **not** simply replace 3.73 with 6.30.

The correct qualitative mixture is:

- good-start branch: strikeouts suppress Houston and he works 5–6 innings;
- ordinary branch: 3 runs in ~5 innings;
- adverse branch: walks/homers elevate pitch count and Houston reaches the bullpen early.

That adverse branch is the main support for Over 7.5 and Astros winner.

---

# 6. Houston offense

Houston enter:
- 67-67
- first in a weak AL West at the cutoff
- coming off a 5-1 win at Yankee Stadium
- having taken two of three from the Yankees

Season offensive context:
- among the stronger AL slugging teams
- approximately .412 team slugging in current reporting

Key offensive drivers include:
- Yordan Alvarez
- Jeremy Peña
- Isaac Paredes
- Christian Walker
- Jose Altuve
- Daulton Varsho

Alvarez entered as one of the league's dominant hitters, and Varsho has recently improved after a slow post-trade start.

Houston's recent offense has been uneven, however:
- 39 runs over the latest ten-game StatMuse window available before this matchup
- significant game-to-game volatility
- multiple low-output games mixed with 6–9 run performances

The current attack therefore has both:
- 3-run floor/central branch;
- 5–7 run power/sequence tail.

---

# 7. Mets offense / availability

New York enter:
- 60-74
- coming off an 8-2 loss to Milwaukee
- 6-4 over a current 10-game specialist window, but with consecutive losses entering this series

Key current availability:

## Juan Soto
Soto remains out recovering from a calf strain and is not expected back for this game.

That removes:
- elite on-base ability;
- left-handed power;
- lineup depth;
- stress pitches against Brown.

## Bo Bichette
Bichette recently sustained an ankle/foot contusion and was day-to-day. He was available off the bench in the prior game, but MLB's official current lineup was still not posted at cutoff.

Because his exact starting status was unresolved in the field-owning lineup source, no forecast branch assumes a full Bichette workload.

Other current Mets bats include:
- Francisco Lindor
- Carson Benge
- Luis Robert Jr.
- Marcus Semien
- Francisco Alvarez
- Brett Baty

The Mets retain enough power to punish Brown's walk/command branch, but Soto's absence lowers the central offensive ceiling.

---

# 8. Bullpen state

## Houston

This is a material negative.

Current reporting states:
- no Astros starter had completed six innings since August 10 before the latest Yankees series context;
- the bullpen has carried a high workload;
- Houston relievers had recently allowed runs in multiple consecutive games;
- bullpen fatigue contributed directly to several recent losses.

The Yankees scored six late runs against Houston relief in a 9-3 win earlier this week.

This increases:
- Mets comeback probability;
- one-run-game probability;
- Over tail.

It is one reason Astros +1.5 ranks above a simple Astros winner/large-margin thesis.

## New York

New York's late relief unit is not perfectly healthy:
- Devin Williams has a shoulder issue;
- Reed Garrett is unavailable long-term;
- other relief injuries exist.

However, because the Mets were beaten 8-2 the previous night, their most important currently available leverage options were less heavily stressed than Houston's.

That supports:
- Mets +1.5;
- a close-game state;
- some resistance to Houston's late separation.

---

# 9. Park/weather

Citi Field around first pitch:
- approximately 78–79°F
- low precipitation probability
- light wind, roughly left-to-right
- no strong rain/delay signal

There is no meaningful weather reason to force the total in either direction.

Citi Field's environment does not create the same automatic carry expectation as a small/hot hitter's park, so the Over must be supported through pitchers, lineups and bullpen exposure rather than temperature alone.

---

# 10. Joint run corridor

## Branch A — close Astros win

Representative:
- Astros 4-3
- Astros 5-4

Mechanism:
- Brown is slightly better than Scott;
- Houston gets 3–4 runs through Scott;
- Mets score late against Houston relief.

Effects:
- Astros +1.5: WIN
- Mets +1.5: WIN
- 4-3 -> Under
- 5-4 -> Over

This is a high-value central branch because both positive run lines cash.

---

## Branch B — Astros moderate separation

Representative:
- Astros 5-2
- Astros 5-3
- Astros 6-3

Mechanism:
- Scott's August run-leakage branch persists;
- Houston converts power/baserunners;
- Brown suppresses the Soto-less Mets.

Effects:
- Astros +1.5: WIN
- Mets +1.5: LOSS
- 5-2 -> Under
- 5-3 / 6-3 -> Over

This is why Astros +1.5 ranks above Mets +1.5.

---

## Branch C — Mets narrow win

Representative:
- Mets 4-3
- Mets 5-4

Mechanism:
- Scott's strikeout branch wins early innings;
- Brown walks hitters / exits around five innings;
- Houston bullpen fatigue becomes decisive.

Effects:
- Astros +1.5: WIN
- Mets +1.5: WIN
- total can be either side

This branch is also favorable to rank #1.

---

## Branch D — low-run starter duel

Representative:
- Astros 3-2
- Mets 3-2
- Astros 4-2

Mechanism:
- Brown command is adequate;
- Scott's season-quality branch reappears;
- Citi suppresses clustered power;
- bullpens avoid traffic.

Effects:
- Under 7.5: WIN
- both +1.5 win in 3-2 states
- Mets +1.5 loses in Astros 4-2

This is the strongest Under branch.

---

## Branch E — bullpen / Scott breakdown

Representative:
- Astros 6-3
- Astros 6-4
- Mets 6-4

Mechanism:
- Scott exits early;
- Houston forces New York into middle relief;
- Brown exits before the seventh;
- Houston's taxed relief also allows scoring.

Effects:
- Over 7.5: WIN
- spread result varies

This is the strongest Over branch.

---

# 11. Ranking rationale

## #1 — Astros +1.5

This is the most robust contract because it wins if:
- Houston wins by any margin;
- Houston loses by exactly one.

Support:
- slight Brown starter edge;
- stronger Houston season offense;
- Mets without Juan Soto;
- Scott's current August run-prevention decline;
- Houston's recent series win over the Yankees.

Even a Mets 4-3 win still cashes Astros +1.5.

Main failure:
- Mets win by 2+, likely through Brown command problems plus Houston bullpen failure.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Mets +1.5

This contract also benefits from the wide one-run overlap.

Support:
- home last-bat entitlement;
- Scott's strikeout ability;
- Houston's overworked bullpen;
- Mets leverage relief comparatively fresher;
- current matchup is close enough that a one-run final is an ordinary state.

Why below Astros +1.5:
- Houston is the preferred winner;
- Scott's recent run prevention is worse than Brown's;
- Soto is absent;
- a 5-2 / 5-3 Astros branch is more credible than an equivalent Mets 2+ win.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Over 7.5

Support:
- only 8 runs are required;
- Scott has allowed 14 ER in 20 August innings;
- Houston has real left/right power;
- Houston bullpen workload is a major late-game risk;
- a 5-3 or 4-4-through-nine style game clears.

Why not higher:
- Brown has been solid recently;
- Soto is absent;
- Citi is not a major offensive accelerator;
- Scott still owns strong strikeout stuff;
- official batting orders remained unresolved.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Under 7.5

The Under remains credible through:
- Brown 2–3 run suppression;
- Scott's strikeout/good-start branch;
- Mets lineup missing Soto;
- Citi Field;
- a 3-2 / 4-2 / 4-3 game.

It ranks last because 7.5 is a relatively low full-game threshold against:
- Scott's poor August run results;
- Houston power;
- Houston bullpen fatigue;
- New York's late home batting entitlement.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 12. Potential game winner

## Houston Astros — FORCED WINNER / LOW-MEDIUM CONFIDENCE

Why Houston:
- Brown has the stronger current starter run-suppression branch;
- Scott has allowed 3–4 runs in each of his last four starts;
- Houston has the deeper central offense;
- Soto is absent;
- Houston has recently played better baseball and enters off a series win at Yankee Stadium.

Why confidence is limited:
- Houston's bullpen is currently a major vulnerability;
- Mets have home last bat;
- official batting orders were still TBD;
- Scott's strikeout rate allows a much better start than his August ERA suggests.

---

# 13. Final card

1. **Astros +1.5**
2. **Mets +1.5**
3. **Over 7.5 Runs**
4. **Under 7.5 Runs**

**Potential winner:** Houston Astros

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

---

# 14. Source record

## Google Drive framework
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- active `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official
- MLB probable pitchers — Hunter Brown / Christian Scott
- MLB Starting Lineups — official orders still TBD at cutoff
- Astros official probable-pitcher page
- Mets official probable-pitcher page

## Current statistical/reporting
- StatMuse Hunter Brown game log
- Baseball-Reference / StatMuse Christian Scott game log
- Houston Chronicle bullpen workload reporting
- Reuters Astros-Yankees and Mets-Brewers recaps
- current Mets injury reporting for Juan Soto and Bo Bichette
- current Citi Field weather cross-check

## Limitations
- official batting orders were not posted at cutoff;
- exact catcher/defensive alignment therefore remained unresolved;
- Houston bullpen exact same-day arm availability is partly workload-inferred;
- operator listed-pitcher/action/extra-inning terms were not supplied;
- no fitted/validated baseball model exists.

---

# 15. Logging confirmation

**Conversation-local ID:** `P-139`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Final frozen state:** `PREGAME — 09:08:12 Australia/Melbourne, approximately 2 minutes before scheduled first pitch`


# P-140 (conversation-local continuation) — Boston Red Sox (Patrick Sandoval) @ New York Yankees (Cam Schlittler) — MLB

## Administrative note

Google Drive is being used strictly as a **read-only framework reference**. The active Drive queue has not been advanced by the most recent locally delivered conversation cards, so this entry is labelled **P-140 conversation-local continuation** to avoid reusing an ID in this chat. It is not claimed to be the Drive-canonical ID until reconciled there.

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Boston Red Sox +1.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **New York Yankees Moneyline** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Combined Total Under 7.0 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Combined Total Over 7.0 Runs** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **New York Yankees — FORCED WINNER / LOW-MEDIUM CONFIDENCE**

### Central qualitative score corridor

- Yankees 3-2
- Yankees 4-2
- Yankees 4-3
- Red Sox 3-2

The core distribution is therefore:

**close game + Yankees slight winner edge + low/mid scoring**

rather than a wide Yankees win or automatic slugfest.

---

## Record metadata

| Field | Value |
|---|---|
| Sport | Baseball |
| League | MLB |
| Event | Boston Red Sox @ New York Yankees |
| Venue | Yankee Stadium, Bronx, New York |
| Scheduled first pitch | 2026-08-28 19:15 America/New_York |
| Melbourne equivalent | 2026-08-29 09:15 Australia/Melbourne |
| Final research cutoff | 2026-08-29 09:12:45 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Boston starter | Patrick Sandoval — LHP |
| New York starter | Cam Schlittler — RHP |
| Starter status | `PROBABLE_OFFICIAL — MLB VERIFIED` |
| Official batting orders | `NOT RELEASED / MLB PAGE TBD AT CUTOFF` |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_BASEBALL.md` |
| Numerical status | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 1. Updated framework controls

The active baseball module requires:

1. exact official event and starter-identity handshake;
2. posted orders, catcher and defence when available;
3. participant mixtures and evidence caps when those fields remain unresolved;
4. starter batters-faced/pitch/hook distributions rather than ERA alone;
5. season prior versus current starter-regime reconciliation;
6. named bullpen exposure and workload branches;
7. HR/contact and sequencing tails;
8. state-dependent home ninth-inning exposure;
9. explicit +1.5 cushion decomposition;
10. one joint run distribution for winner, run lines and total.

MLB's official batting-order page still showed both teams as **TBD** at the final cutoff. Therefore participant-sensitive claims cannot be upgraded to high confidence.

All four rows are consequently capped at:

`FORCED RANK / MEDIUM-LOW`

No internal numerical probability is published.

---

# 2. Contract geometry

## Yankees ML

Wins on any Yankees victory.

## Red Sox +1.5

Wins if:
- Boston wins;
- Boston loses by exactly one.

Loses only if:
- New York wins by 2+.

### Important dependence

The two side contracts can both win.

Example:

**Yankees 3-2 Red Sox**

- Yankees ML — WIN
- Red Sox +1.5 — WIN

That is the main reason the Boston cushion can rank above the Yankees winner even though New York remains the preferred outright side.

---

## Total Over 7.0

- WIN at 8+ runs
- PUSH at exactly 7
- LOSS at 6 or fewer

## Total Under 7.0

- WIN at 6 or fewer
- PUSH at exactly 7
- LOSS at 8+

The integer boundary must be preserved.

---

# 3. Official identity/state

MLB officially lists:

**Boston Red Sox @ New York Yankees**  
Friday, August 28, 2026  
**7:15 PM ET**  
Yankee Stadium

Official probable starters:

### Boston
**Patrick Sandoval — LHP**
- 1-2
- 4.54 ERA
- 41 strikeouts

### New York
**Cam Schlittler — RHP**
- 11-6
- 2.16 ERA
- 193 strikeouts

At 09:12:45 Australia/Melbourne, roughly two minutes before scheduled first pitch, MLB still listed the game as scheduled/pregame.

Therefore:

`GAME-STATE: PREGAME`

---

# 4. Cam Schlittler — season prior and current regime

Schlittler is the strongest single run-suppression input in the game.

Season:
- 11-6
- 2.16 ERA
- 193 strikeouts
- one of the American League's strongest starting-pitcher seasons

August:

| Date | Opponent | IP | ER | BB | K |
|---|---|---:|---:|---:|---:|
| Aug 21 | Toronto | 6.0 | 1 | 3 | 4 |
| Aug 15 | Toronto | 5.1 | 1 | 3 | 7 |
| Aug 9 | Atlanta | 7.0 | 1 | 0 | 11 |
| Aug 3 | St. Louis | 3.0 | 4 | 5 | 6 |

The current regime therefore contains:

### Central Schlittler branch
- 5½–7 innings
- 0–2 runs
- substantial strikeout pressure

### Adverse branch
- command loss / walks
- pitch-count escalation
- earlier hook
- Boston reaches the Yankee bullpen before the seventh

The Aug. 3 start shows that the bad-command tail still exists and should not be erased by the following three strong starts.

---

# 5. Schlittler vs Boston continuity

Schlittler has already faced Boston repeatedly in 2026.

Across three regular-season meetings in available StatMuse records:
- roughly 18⅔ innings
- only **2 earned runs**
- 19 strikeouts
- limited hard scoring conversion overall

One Boston win against him contained multiple unearned runs, which is important:

**starter run prevention and final team result are not identical.**

The H2H is useful because:
- same season;
- same division;
- same current pitcher;
- meaningful current-lineup overlap.

But it is not treated as ownership.

Boston's offense has materially improved in the second half, so old 2026 meetings are retained only as supporting process evidence.

---

# 6. Boston's current offensive regime

Boston enter:
- **73-60**
- 7-3 over their last 10
- approximately +100 run differential
- only two games behind New York in the standings entering the series

Most importantly, Boston have been one of baseball's hottest second-half teams:

- **27-12 since the All-Star break**
- current reporting places the club around an **.810 August OPS**

This is the strongest counterweight to the Schlittler under/winner thesis.

Therefore the model does **not** assume:
> elite pitcher = automatic Boston suppression.

The current regime mixture is:

### Baseline
Schlittler strongly suppresses run scoring.

### Current Boston branch
Boston's improved offense creates more competitive at-bats, baserunners and extra-base-hit exposure than a broad season-average opponent.

That is why:
- Red Sox +1.5 ranks first;
- Yankees ML remains only a forced winner;
- the Over tail remains live.

---

# 7. Boston availability

Boston remain without major lineup pieces at the cutoff.

## Roman Anthony
Anthony has been on the injured list with a partially torn tendon in his right ring finger/hand and was still on a rehab assignment.

## Trevor Story
Story remains in a rehab progression from sports-hernia surgery and was not expected to be part of Friday's initial lineup branch.

Therefore Boston's recent strong offense has been produced **without its full theoretical lineup ceiling**.

That cuts in both directions:

- the current Boston offense is demonstrably functional despite the absences;
- but the missing bats still lower the absolute scoring ceiling compared with a fully healthy roster.

---

# 8. Patrick Sandoval — season prior and current regime

Season:
- 1-2
- 4.54 ERA
- eight starts around the current cutoff

Recent August:

| Date | Opponent | IP | ER | BB | K |
|---|---|---:|---:|---:|---:|
| Aug 22 | Giants | 5.2 | 2 | 2 | 6 |
| Aug 16 | Pirates | 4.0 | 7 | 3 | 6 |
| Aug 11 | Blue Jays | 6.0 | 2 earned / 4 total | 3 | 4 |
| Aug 4 | White Sox | 5.0 | 2 | 4 | 5 |

Current reporting notes Sandoval has allowed **two or fewer earned runs in six of eight starts**.

That makes his 4.54 ERA misleading if used as a one-number projection.

### Sandoval good/ordinary branch
- 5–6 innings
- roughly 2–3 runs
- enough swing/miss to keep New York from clustering

### Sandoval failure branch
- elevated walks
- long plate appearances
- shortened outing
- Yankee Stadium right-handed damage

The Aug. 16 seven-run outing demonstrates the material blow-up tail.

---

# 9. Yankees offense and platoon context

New York enter:
- **75-58**
- 7-3 in their last 10
- +100 run differential
- approximately 28-17 against left-handed starters

The Yankees therefore have a real matchup advantage against a left-handed starter.

However, the current lineup regime is materially weaker than full-strength New York.

## Aaron Judge
Judge remains on the injured list with a rib stress fracture and was only recently progressing to tee work.

## Giancarlo Stanton
Stanton also remains out with a calf injury.

## Cody Bellinger
Bellinger has returned from his hamstring injury and restores an important middle-order bat.

The resulting offense remains dangerous but is **not** equivalent to the full Judge/Stanton/Bellinger roster.

New York also enters after scoring only **one run** in Thursday's 5-1 loss to Houston.

That one game is not used as a forecast rate, but it fits the current missing-power context.

---

# 10. Bullpen state

## Boston

Boston had Thursday off before this series.

Current series reporting describes the bullpen as comparatively well rested.

There are still injury concerns:
- Garrett Whitlock unavailable;
- Justin Slaten unavailable;
- other depth changes have forced newer arms into relief roles.

The key point is:

`rested != automatically elite`

but Boston's highest-available leverage arms enter with better short-term rest than they would after a game the previous day.

That materially supports:
- Boston +1.5;
- Under 7 central branch.

---

## New York

New York completed a three-game series with Houston on Thursday.

The bullpen is also missing important depth, most notably Fernando Cruz after a significant elbow/UCL injury.

Thursday's starter Gerrit Cole completed six innings in the 5-1 loss, limiting catastrophic bullpen exposure, but New York still enters this series without Boston's full off-day advantage.

This slightly increases:
- late Boston comeback probability;
- one-run-game probability;
- Red Sox +1.5 robustness.

---

# 11. Weather / park environment

Latest National Weather Service point forecast near Yankee Stadium around first pitch:

- approximately **26°C / upper-70s°F**
- low immediate rain probability around **14%**
- light wind around **3 mph**
- wind shifting NW
- rain probability dropping rapidly later in the evening

There is no strong sustained wind or precipitation mechanism.

Weather therefore receives **minimal directional weight**.

Yankee Stadium's short right-field dimensions preserve the ordinary home-run tail, but the current lineup/pitcher evidence remains more important.

---

# 12. Season-series context

Boston leads the 2026 season series:

**5-4**

The nine prior results include both:
- low-run Yankee wins;
- higher-scoring Boston wins.

The season-series result is descriptive rather than predictive.

What matters more is that:
- Boston has demonstrated it can remain competitive with New York;
- the current standings/run differentials are very similar;
- New York's superior starting pitcher does not imply a large-margin central state.

This directly supports Boston +1.5 over a wide Yankee-margin thesis.

---

# 13. Joint run/margin tree

## Branch A — Yankees narrow win / Under

Representative:
- Yankees 3-2
- Yankees 4-2

Mechanism:
- Schlittler limits Boston;
- Sandoval keeps New York from a multi-inning explosion;
- bullpen scoring remains controlled.

Effects:
- Yankees ML: WIN
- Boston +1.5: WIN at 3-2; LOSS at 4-2
- Under 7: WIN
- Over 7: LOSS

This is the central branch.

---

## Branch B — Yankees narrow win / seven-run push

Representative:
- Yankees 4-3

Effects:
- Yankees ML: WIN
- Boston +1.5: WIN
- Under 7: PUSH
- Over 7: PUSH

This is an especially important boundary state.

---

## Branch C — Boston upset

Representative:
- Boston 3-2
- Boston 4-3

Mechanism:
- Boston's hot offense reaches Schlittler enough to force an earlier hook;
- Yankees' diminished offense does not separate;
- Boston's rested bullpen closes.

Effects:
- Boston +1.5: WIN
- Yankees ML: LOSS
- total stays Under or pushes at 7

This branch materially increases rank #1.

---

## Branch D — Yankees offensive separation

Representative:
- Yankees 5-2
- Yankees 6-2

Mechanism:
- Sandoval's walk/blow-up branch occurs;
- Yankees exploit left-handed matchup;
- bullpen is exposed early.

Effects:
- Yankees ML: WIN
- Boston +1.5: LOSS
- 5-2 -> both total sides PUSH at 7
- 6-2 -> Over 7 WIN

This is the strongest failure path for Red Sox +1.5.

---

## Branch E — open rivalry game

Representative:
- Yankees 5-3
- Boston 5-4
- Yankees 6-4

Mechanism:
- Sandoval struggles;
- Boston's second-half offense also creates damage;
- one or both bullpens surrender clustered late scoring.

Effects:
- Over 7: WIN

This is the strongest Over branch.

---

# 14. Ranking rationale

## #1 — Red Sox +1.5

This contract wins on:
- any Boston victory;
- any one-run Yankee victory.

Support:
- Boston is 27-12 since the break;
- Boston leads season series 5-4;
- both clubs have similar season run differentials;
- Yankees are missing Judge/Stanton;
- Boston bullpen enters with off-day rest;
- one-run states such as 3-2 and 4-3 are central.

Counterweight:
- Schlittler has an enormous starter advantage;
- Yankees are strong against LHP;
- Sandoval has a material walk/blowup tail.

The strongest kill path is a **Yankees 4-2 / 5-2 / 5-1** type state.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Yankees ML

New York remains the preferred winner.

Support:
- Schlittler 11-6, 2.16 ERA;
- three straight one-run starts entering tonight;
- excellent same-season run prevention against Boston;
- Yankees home last bat;
- Sandoval's command/blow-up tail;
- New York 28-17 versus LHP.

Why below Boston +1.5:
Yankees ML loses every Boston upset, while Boston +1.5 survives a large one-run Yankee-win branch.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Under 7.0

Support:
- Schlittler's current form;
- Sandoval has allowed <=2 ER in six of eight starts;
- Judge and Stanton absent;
- Anthony and Story absent/unavailable in Boston's central lineup state;
- Boston bullpen relatively rested;
- central scores 3-2 and 4-2 are <=6.

The integer line matters:
- exactly 7 is **not an Under win**;
- 4-3 produces a PUSH.

Strongest failure:
Sandoval's walks create 4–5 Yankee runs and Boston's current offense adds 3+.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Over 7.0

The Over has a legitimate route:
- Sandoval early command problems;
- Yankees' strong record against LHP;
- Boston's .810-ish August offensive regime;
- Yankee Stadium HR tail;
- weakened/injured bullpen depth.

But it needs **8+** runs to win.

At seven it only pushes.

Given Schlittler's run prevention and the missing power bats, that is less robust than the central low/mid-scoring state.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 15. Potential game winner

## New York Yankees — `FORCED WINNER / LOW-MEDIUM CONFIDENCE`

Why:
- Schlittler is the best player-level run-prevention input;
- New York has home last bat;
- Yankees perform well against left-handed starters;
- Sandoval's control creates a separation tail.

Why not stronger:
- Boston is extremely hot in the second half;
- Boston has already led the season series;
- Yankees are missing their two biggest right-handed power bats;
- Boston's bullpen is better rested.

The winner lean and Red Sox +1.5 are fully coherent.

A **Yankees 3-2** result makes both side selections win.

---

# 16. Final card

1. **Red Sox +1.5**
2. **Yankees ML**
3. **Under 7.0 Runs**
4. **Over 7.0 Runs**

**Potential winner:** New York Yankees

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

---

# 17. Source record

## Google Drive framework
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- active `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`
- active combined-log governance

## Official MLB
- MLB probable pitchers — Sandoval / Schlittler
- MLB starting-lineup page — both orders still TBD at cutoff
- MLB standings
- MLB Yankees injury reporting
- MLB Red Sox injury / rehab reporting
- MLB scoreboard

## Statistical / current reporting
- StatMuse Cam Schlittler 2026 game log
- StatMuse Patrick Sandoval 2026 game log
- StatMuse Schlittler vs Boston
- Baseball-Reference current matchup/standings splits
- current series reporting for Boston second-half offense and bullpen state
- Reuters Yankees-Astros recap

## Weather
- National Weather Service Bronx/Yankee Stadium-area hourly forecast

---

# 18. Limitations

- Official batting orders, catcher and defensive alignment were still not published in MLB's field-owning lineup page at cutoff.
- Exact operator action/listed-pitcher rules were not supplied.
- New York's bullpen exact same-day arm availability is not represented from a complete pitch-usage ledger.
- Boston's bullpen is rested but currently injury-altered.
- Schlittler's prior Boston success is same-season relevant but cannot be treated as deterministic ownership.
- No fitted or validated baseball numerical model exists.

---

# 19. Logging confirmation

**Conversation-local ID:** `P-140`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Final state:** `PREGAME — 09:12:45 Australia/Melbourne, approximately 2 minutes before scheduled first pitch`


# P-141 (conversation-local continuation) — Colorado Rockies (Tomoyuki Sugano) @ Atlanta Braves (Grant Holmes) — MLB

## State warning

**FINAL ISSUE STATE:** `START CROSSED — LIVE SCORE 0-0 EXPOSED, EXACT INNING/BASE-OUT STATE NOT VERIFIED`

The official scheduled first pitch was **7:15 PM EDT on 28 August 2026**, equivalent to **9:15 AM Australia/Melbourne on 29 August 2026**.

During research, the scheduled start crossed. The freshest MLB schedule surface exposed **Colorado 0 – Atlanta 0**, and the MLB scoreboard moved from preview-style presentation to Gameday, but an exact inning / outs / base state could not be reliably recovered at the final research cutoff.

Under `MDS-2026.08.29-v2.5`, the card therefore **does not convert the user's original pregame lines into actionable live advice**.

The ranking below is preserved as the **frozen pre-start evidence view** only.

---

## Executive pre-start ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Atlanta Braves Moneyline** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **2** | **Colorado Rockies +2.5 Runs** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **3** | **Combined Total Under 9.0 Runs** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **4** | **Combined Total Over 9.0 Runs** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |

**Potential game winner:** **Atlanta Braves — FORCED WINNER / LOW-MEDIUM CONFIDENCE**

### Central qualitative score corridor

- Atlanta 4-2
- Atlanta 5-2
- Atlanta 5-3
- Atlanta 4-3

The central distribution is:

`ATLANTA WIN + COLORADO +2.5 LIVE IN MANY BRANCHES + TOTAL CLUSTER AROUND 6–8 RUNS`

The main contrary state is a Sugano/contact failure that pushes Atlanta toward 6–8 runs and turns the game into an Over / wide-margin Braves result.

---

## Administrative note

Google Drive was used strictly as a **read-only framework source**.

The active Drive queue has not been advanced by the latest locally delivered conversation cards. This file is therefore labelled **P-141 conversation-local continuation** to avoid ID reuse inside this conversation.

It should not be interpreted as the Drive-canonical ID until reconciled into the active log.

---

# 1. Record metadata

| Field | Value |
|---|---|
| Sport | Baseball |
| League | MLB |
| Event | Colorado Rockies @ Atlanta Braves |
| Venue | Truist Park, Atlanta, Georgia |
| Scheduled first pitch | 2026-08-28 19:15 America/New_York |
| Melbourne equivalent | 2026-08-29 09:15 Australia/Melbourne |
| Starter — Colorado | Tomoyuki Sugano, RHP |
| Starter — Atlanta | Grant Holmes, RHP |
| Starter status | `PROBABLE_OFFICIAL — MLB VERIFIED` |
| Official batting orders at cutoff | `TBD / NOT FIELD-OWNER VERIFIED` |
| Secondary current lineup capture | `AVAILABLE` |
| Method | `MDS-2026.08.29-v2.5` |
| Baseball module | `RULES_BASEBALL.md` |
| Numerical status | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 2. Updated framework controls applied

The active baseball framework requires:

1. official exact-event and starter-identity handshake;
2. official batting orders, catcher and defence where released;
3. explicit participant mixtures and evidence caps if official orders remain unreleased;
4. starter batters-faced / pitch / innings / hook distributions;
5. season prior vs current pitcher-regime reconciliation;
6. named bullpen exposure and workload branches;
7. contact / HR / sequencing tails;
8. park, weather and defence adjustment;
9. state-dependent Atlanta home ninth-inning entitlement;
10. explicit +2.5 margin decomposition;
11. one joint run distribution for winner, margin and total;
12. exact integer total push handling.

The MLB official lineup page still showed both batting orders as **TBD** at the cutoff, even though current team-focused reporting had published expected/announced lineups.

That unresolved field-owner state triggers:

`FORCED RANK / MEDIUM-LOW`

for participant-sensitive rows.

---

# 3. Contract geometry

## Braves ML

Wins with any Atlanta victory.

---

## Rockies +2.5

Wins if:
- Colorado wins;
- Colorado loses by 1;
- Colorado loses by 2.

Loses only if:
- Atlanta wins by 3+.

This is **not** the opposite of Braves ML.

Both can win simultaneously.

Examples:

### Atlanta 4-2
- Braves ML — WIN
- Rockies +2.5 — WIN

### Atlanta 5-3
- Braves ML — WIN
- Rockies +2.5 — WIN

### Atlanta 5-2
- Braves ML — WIN
- Rockies +2.5 — LOSS

---

## Over 9.0

- WIN at 10+ runs
- PUSH at exactly 9
- LOSS at 8 or fewer

## Under 9.0

- WIN at 8 or fewer
- PUSH at exactly 9
- LOSS at 10+

The integer push mass is preserved.

---

# 4. Official starter identity

MLB officially lists:

## Colorado Rockies
**Tomoyuki Sugano — RHP**
- 12-7
- 4.96 ERA
- 71 strikeouts

## Atlanta Braves
**Grant Holmes — RHP**
- 8-5
- 3.64 ERA
- 100 strikeouts

The identity handshake therefore passes for both starting pitchers.

---

# 5. Grant Holmes — season prior vs August regime

Season baseline:
- 8-5
- 3.64 ERA

August game log:

| Date | Opponent | IP | ER | BB | K |
|---|---|---:|---:|---:|---:|
| Aug 20 | White Sox | 6.0 | 0 | 3 | 3 |
| Aug 15 | Diamondbacks | 3.2 | 6 | 3 | 3 |
| Aug 9 | Yankees | 6.0 | 0 | 2 | 2 |
| Aug 4 | Marlins | 6.0 | 0 | 1 | 5 |

August aggregate:
- **21⅔ innings**
- **6 earned runs**
- **2.49 ERA descriptively**
- all six earned runs concentrated in one bad start

### Holmes central branch

`5–6 innings + modest baserunner load + weak-contact / fielding support -> Colorado held around 1–3 starter-era runs`

### Holmes adverse branch

The Arizona outing proves the current regime still contains a meaningful:
- command loss;
- contact cluster;
- early hook;
- 4–6 run starter tail.

That tail must remain in the score tree.

### Matchup fit

Current specialist reporting notes Holmes' chase/whiff ability maps well against a Colorado lineup that:
- strikes out frequently;
- does not consistently exploit low walk rates;
- has often produced low-quality contact.

That is directionally supportive but not treated as an internal probability.

---

# 6. Tomoyuki Sugano — season prior vs current adverse branch

Season:
- 12-7
- 4.96 ERA
- low walk volume
- low strikeout volume relative to power starters
- contact-dependent run prevention
- 26 home runs allowed in the current broad statistical snapshot

Recent starts:

| Date | Opponent | IP | ER |
|---|---|---:|---:|
| Aug 23 | Cleveland | 3.0 | 5 |
| Aug 17 | Dodgers | 5.0 | 6 |
| Aug 11 | Arizona | 6.0 | 2 |
| Aug 5 | Tampa Bay | 5.0 | 3 |
| Jul 31 | Kansas City | 6⅔ | 1 |

### Current adverse trigger

Sugano has allowed:
- **11 earned runs in his last 8 innings**
- 16 hits across those two poor starts
- two home runs vs Los Angeles

The underlying mechanism is more important than the raw runs:

`low strikeout margin + contact dependence + recent inability to suppress extended at-bats -> higher sequencing and extra-base-hit risk`

Atlanta's lineup is capable of creating this type of pressure.

### Counterbranch

Sugano also owns:
- excellent control;
- multiple recent 5–6 inning competitive starts;
- the ability to survive when early-count contact is weak.

Therefore the model does **not** simply extend his last-two-start ERA forward.

---

# 7. Atlanta current offensive regime

Atlanta enter:
- **79-55**
- on a four-game winning streak
- having swept the Dodgers
- one of the stronger National League teams

However, the offense has not been uniformly explosive.

StatMuse's latest ten-game window:
- **26 total runs**
- only **2.6 runs/game descriptively**

Recent games:
- 1 run vs Dodgers
- 6 runs vs Dodgers
- 4 runs vs Dodgers
- 4 runs vs Brewers
- 1 run
- 1 run
- 2 runs

This is a critical current-regime counterweight to the Sugano blow-up narrative.

Atlanta can win without scoring 6–8 runs.

### Secondary current lineup state

Current Braves-focused reporting had:

- Ronald Acuña Jr. returning to the lineup and batting cleanup;
- Ozzie Albies, Matt Olson and Drake Baldwin in the upper order;
- Michael Harris II behind Acuña;
- Austin Riley receiving a rest day;
- Mauricio Dubón covering third base;
- Sean Murphy and Ha-Seong Kim contributing lower in the order.

Because MLB's own lineup page remained `TBD`, this is recorded as:

`SECONDARY CURRENT LINEUP — NOT FIELD-OWNER CONFIRMED AT CUTOFF`

Riley's rest modestly reduces Atlanta's power ceiling relative to a full-strength lineup.

---

# 8. Colorado current offensive regime

Colorado enter:
- **52-82**

Latest ten-game StatMuse window:
- **41 runs**
- but **13 came in one game**

Removing that 13-run outlier:
- 28 runs across the other nine games
- approximately **3.1/game descriptively**

Recent:
- 1 run vs Washington
- 13 runs vs Washington
- 3
- 3
- 2
- 3
- 1

The distribution is therefore highly skewed:
- several 1–3 run outputs;
- isolated explosive games.

### Current lineup / availability

Current reporting has:
- Jake McCarthy leading off;
- Cole Carrigg near the top;
- Hunter Goodman batting third after returning from IL;
- TJ Rumfield cleanup;
- Mickey Moniak back in the DH mix.

Hunter Goodman's return matters materially:
- he leads Colorado in home runs;
- he adds a legitimate Holmes mistake-punishment branch.

But Colorado still has a weaker broad offensive profile than Atlanta.

---

# 9. Bullpen state

## Atlanta

This is a meaningful positive.

Chris Sale threw a **complete-game shutout** against the Dodgers yesterday.

That meant Atlanta did **not need to use its bullpen at all** in the 1-0 win.

The entire relief chain therefore enters this game with unusually clean one-day freshness.

Framework interpretation:

`freshness is not quality`

but:
- Iglesias / leverage arms;
- setup options;
- bridge arms

have more availability flexibility than after an ordinary bullpen-heavy game.

This strengthens:
- Braves ML;
- Under 9 central branch;
- late suppression after Holmes exits.

---

## Colorado

Colorado's bullpen was described in current Reuters coverage as **among the worst in MLB**, although it recently delivered five scoreless innings in a 3-1 win over Washington.

That recent good outing is retained as a reminder that:
- a weak broad unit can still produce good individual games;
- bullpen weakness is a distributional tail, not a guaranteed collapse.

But compared with Atlanta:
- Colorado has a materially weaker season relief prior;
- more late-game Atlanta separation risk exists if Sugano exits early.

This is the strongest threat to Rockies +2.5.

---

# 10. Weather / park

National Weather Service Atlanta forecast around 7 PM:

- approximately **83°F**
- dew point around **70°F**
- very light wind around **1 mph**
- precipitation probability around **25%**

At 8 PM:
- approximately 81°F
- similarly light wind

### Mechanistic interpretation

Warm/humid air preserves ordinary carry.

However:
- wind is very light;
- no strong sustained outflow direction exists;
- scattered precipitation risk does not automatically support either total direction.

Weather therefore adds only a **small high-contact/HR ceiling modifier**, not enough to control the total.

---

# 11. 2026 head-to-head audit

Atlanta swept Colorado at Coors Field in May:

- Braves 8-6 Rockies
- Braves 9-1 Rockies
- Braves 11-6 Rockies

This is descriptive only.

Reasons for heavy downweighting:
- Coors Field is a materially different run environment;
- the current game is at Truist Park;
- current starter and bullpen regimes differ;
- the current lineups and team forms have changed.

Grant Holmes did start the 8-6 game, which preserves an ordinary Colorado-scoring counterbranch.

The May series does **not** justify simply projecting another 10+ Atlanta output.

---

# 12. Joint qualitative score tree

## Branch A — central Braves win / Rockies cover / Under

Representative:
- Braves 4-2
- Braves 5-3
- Braves 4-3

Mechanism:
- Holmes limits Colorado;
- Sugano is competitive enough to avoid early collapse;
- Atlanta bullpen closes cleanly.

Results:

### 4-2
- Braves ML WIN
- Rockies +2.5 WIN
- Under 9 WIN
- Over 9 LOSS

### 5-3
- Braves ML WIN
- Rockies +2.5 WIN
- Under 9 WIN
- Over 9 LOSS

### 4-3
- Braves ML WIN
- Rockies +2.5 WIN
- Under 9 WIN
- Over 9 LOSS

This is the **central branch**.

---

## Branch B — Atlanta moderate separation / Under

Representative:
- Braves 5-2
- Braves 6-2

Mechanism:
- Sugano allows repeated hard contact;
- Holmes suppresses Colorado;
- Atlanta's fresh bullpen protects the lead.

### 5-2
- Braves ML WIN
- Rockies +2.5 LOSS
- Under 9 WIN

### 6-2
- Braves ML WIN
- Rockies +2.5 LOSS
- Under 9 WIN

This branch is why a low total does **not** imply Rockies +2.5 automatically.

---

## Branch C — Atlanta blowout / Over

Representative:
- Braves 7-3
- Braves 8-2
- Braves 8-3

Mechanism:
- Sugano's current contact tail persists;
- Colorado bullpen is exposed early;
- Atlanta creates multiple HR/extra-base clusters.

Results:
- Braves ML WIN
- Rockies +2.5 LOSS
- Over 9 WIN

This is the strongest kill path for ranks #2 and #3.

---

## Branch D — Colorado competitive / one-run game

Representative:
- Braves 4-3
- Rockies 4-3
- Braves 5-4

Mechanism:
- Goodman/Moniak punish Holmes mistakes;
- Sugano's control survives;
- Atlanta's offense remains in its recent low-output state.

At **5-4**:
- total = 9
- Over 9 PUSH
- Under 9 PUSH

This is an important exact-boundary state.

---

## Branch E — Colorado upset

Representative:
- Rockies 4-3
- Rockies 5-3

Mechanism:
- Holmes' Arizona-style bad branch appears;
- Sugano gives Colorado 5–6 competitive innings;
- Atlanta's offense remains muted.

Results:
- Rockies +2.5 WIN
- Braves ML LOSS

This is the strongest ordinary adverse state for the winner selection.

---

# 13. Ranking rationale

## #1 — Braves ML

Strongest supplied contract.

Support:
- 79-55 vs 52-82 team baseline;
- Holmes' stronger current run-suppression branch;
- Sugano's last-two-start contact failure;
- Atlanta home last bat;
- Atlanta's bullpen completely rested after Sale's complete game;
- Colorado's weaker broad relief quality;
- Braves enter on a four-game winning streak.

Why confidence is capped:
- official field-owner batting orders still unresolved at cutoff;
- Atlanta offense has scored only 26 in its last 10;
- Holmes has a real blow-up branch;
- Colorado's offense has occasional high-run tails.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Rockies +2.5

This is a very broad underdog cushion.

It wins:
- on any Colorado victory;
- on an Atlanta win by 1 or 2.

Support:
- Atlanta's offense has been low-scoring recently;
- Holmes can suppress Colorado enough to produce low-margin finals;
- exact central scores 4-2, 5-3 and 4-3 all cash;
- the user line is materially more forgiving than a standard +1.5.

Why below Braves ML:
- Atlanta has a credible 5-2 / 6-2 branch;
- Colorado's bullpen creates late separation risk;
- Sugano's current contact state can turn a close game into a 4+ run Atlanta win.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Under 9.0

Support:
- Holmes' current August profile;
- Colorado's recent offense is mostly 1–3 runs outside one 13-run explosion;
- Atlanta bullpen is fully fresh;
- Atlanta's own offense has averaged only 2.6 runs in the latest ten-game window;
- Austin Riley rests in the reported lineup;
- 4-2 / 5-2 / 5-3 / 4-3 all remain Under.

Boundary:
- exactly 9 runs is a PUSH, not a win.

Kill path:
- Sugano exits early after another contact-heavy start and Colorado's bullpen allows Atlanta to reach 7–8.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Over 9.0

The Over has a legitimate path:

`Sugano contact failure + Colorado weak relief + warm Atlanta conditions + Colorado contributes 2–4`

Examples:
- 7-3
- 8-2
- 8-3

But it needs **10+ runs to win**.

Nine only pushes.

The central corridor contains substantially more 6–8 run states than 10+ states.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 14. Potential game winner

## Atlanta Braves — `FORCED WINNER / LOW-MEDIUM CONFIDENCE`

Primary mechanisms:
- stronger current starter;
- superior team baseline;
- home last bat;
- completely rested bullpen;
- Sugano's recent contact problems.

Strongest failure path:
- Holmes enters his adverse command/contact branch;
- Sugano gives Colorado a competitive six-inning outing;
- Atlanta's recent offensive slowdown persists.

---

# 15. Final pre-start card

1. **Braves ML**
2. **Rockies +2.5**
3. **Under 9.0 Runs**
4. **Over 9.0 Runs**

**Potential winner:** Atlanta Braves

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

---

# 16. Source record

## Google Drive framework
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- active `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official MLB
- MLB probable pitchers — Sugano / Holmes
- Braves official probable-pitcher page
- MLB scoreboard / schedule
- MLB official starting-lineup page — still `TBD` at cutoff
- Braves / Rockies official schedule pages

## Current process/statistical sources
- StatMuse Grant Holmes August game log
- Baseball-Reference Tomoyuki Sugano game log
- StatMuse Braves recent run production
- StatMuse Rockies recent run production
- Reuters Braves-Dodgers final
- Reuters Rockies-Nationals reporting
- current Braves/Rockies team-focused lineup previews

## Weather
- National Weather Service Atlanta hourly forecast

## Market context only
A contemporaneous market snapshot had approximately:
- Atlanta around -220
- standard run line around Atlanta -1.5 / Colorado +1.5
- main total around 8.5

This was used only as contract-state context, not as internal sports probability.

---

# 17. Limitations

- the scheduled start crossed during research;
- exact live inning / outs / base state could not be verified;
- official MLB batting orders remained `TBD` in the field-owning lineup endpoint;
- secondary lineup reports were therefore not promoted to confirmed official status;
- exact operator listed-pitcher/action rules were not supplied;
- no complete same-day reliever pitch-availability ledger was available;
- no fitted/validated baseball probability model exists.

---

# 18. Logging confirmation

**Conversation-local ID:** `P-141`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Current disposition:** `START CROSSED — LIVE 0-0 SHOWN, EXACT LIVE STATE NOT VERIFIED — PRE-START RANKING PRESERVED FOR REFERENCE ONLY`

# P-142 (conversation-local continuation) — New York Giants @ New York Jets — NFL Preseason Week 3

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Combined Total Under 37.0 Points** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **New York Jets +6.0** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **New York Giants -1.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Combined Total Over 33.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **New York Giants — FORCED WINNER / LOW CONFIDENCE**

### Central qualitative score family

- Giants 17-13
- Giants 20-13
- Giants 20-16
- Giants 20-17
- Jets 17-16

The central state is a **low-to-mid 30s, reserve-heavy one-score game**, with the Giants owning a small QB-depth edge but the Jets' +6.0 cushion protecting most close-game outcomes.

---

## Administrative note

Google Drive was used **read-only**. The current Drive snapshot still lists `P-137` as its next canonical ID because the recent locally generated cards were not appended to Drive. This file is therefore labelled **P-142 conversation-local continuation** to avoid reusing IDs inside this conversation.

It is not claimed to be the canonical Drive ID until formally reconciled.

---

# 1. Record metadata

| Field | Value |
|---|---|
| Sport | American football |
| Competition | NFL Preseason Week 3 |
| Event | New York Giants @ New York Jets |
| Venue | MetLife Stadium, East Rutherford, New Jersey |
| Scheduled kickoff | 2026-08-28 19:30 America/New_York |
| Melbourne equivalent | 2026-08-29 09:30 Australia/Melbourne |
| Research state | `PREGAME` |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_AMERICAN_FOOTBALL.md` |
| Numerical state | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive modified | `NO` |
| Retrospective | `NOT INCLUDED` |

---

# 2. Updated-framework controls

The Drive's active American-football framework requires:

- NFL preseason to be treated as a separate population from regular-season power ratings;
- starting/backup QB identity and expected reps to be decision-driving;
- line/skill-player depth to be represented through unit mixtures;
- drive volume, field position, third/fourth-down conversion and red-zone efficiency to drive scoring;
- turnover and non-offensive-score tails to be retained but shrunk;
- exact football score combinations and push states to be preserved;
- winner, spread and total to be derived from one shared discrete score tree;
- unresolved participant plans to reduce evidence quality rather than be guessed away.

No fitted/validated NFL model exists.

---

# 3. Participant-state gate

## Giants

The Giants' official midweek position was that head coach John Harbaugh had not yet publicly committed to Jaxson Dart/starter participation.

Current same-day reporting at the stadium subsequently stated:
- **Jaxson Dart will not play**;
- Giants regular starters will largely sit.

Because that final game-plan detail was not independently recovered from a field-owning Giants release at cutoff, it is recorded as:

`NYG STARTER REST PLAN: SECONDARY_ONLY`

The current Giants QB room includes:
- Jaxson Dart
- Jameis Winston
- Brandon Allen

The reserve game is expected to rely primarily on **Winston and Brandon Allen** if the secondary starter-rest report is correct.

## Jets

The Jets' official preview had Aaron Glenn still weighing starter participation.

Current same-day reporting states:
- **Geno Smith will not play**;
- most Jets starters will rest;
- Cade Klubnik, Bailey Zappe and Brady Cook will receive the quarterback work.

This final allocation was likewise not independently recovered from a field-owning Jets release at cutoff, so:

`NYJ STARTER REST PLAN: SECONDARY_ONLY`

Because both decisive QB-rotation plans remain secondary-only at final pregame issue, all four contracts are capped at:

`FORCED RANK / MEDIUM-LOW`

---

# 4. Quarterback-depth comparison

## Giants reserve chain

### Jameis Winston

Against Miami last week:
- started and played the entire first half;
- 15/21 passing;
- 150 yards;
- scored an 11-yard rushing touchdown.

This demonstrated a functional veteran-QB floor against reserve/preseason personnel.

### Brandon Allen

2026 preseason through two games:
- 18/26;
- 146 yards;
- 0 passing TD;
- 2 INT.

Split:
- vs Minnesota: 5/8, 45 yards, 2 INT;
- at Miami: 13/18, 101 yards, 0 INT.

Allen's Miami performance was materially cleaner than his opener, but the two-interception tail remains relevant.

### Giants QB interpretation

If Dart sits, the Giants still possess:
- a highly experienced Winston first branch;
- another veteran in Allen.

This gives New York Giants a modest four-quarter quarterback-experience advantage.

---

## Jets reserve chain

### Cade Klubnik

Across two preseason games:
- 15/21;
- 131 yards;
- 71.4% completions;
- 0 TD;
- 0 INT;
- 3 sacks.

Week 1 vs Tampa Bay:
- 5/7, 56 yards;
- led two scoring drives.

Week 2 at Pittsburgh:
- 10/14, 75 yards;
- plus a 16-yard run.

Klubnik's profile is efficient but not yet explosive.

### Bailey Zappe

Week 1:
- threw two interceptions on consecutive possessions.

Week 2:
- improved to 6/8 for 65 yards.

This is a wide turnover/efficiency branch.

### Brady Cook

Week 1:
- 8/13, 88 yards.

Week 2:
- 1/2 with a 31-yard late touchdown.

### Jets QB interpretation

The Jets have:
- a relatively stable rookie starter branch in Klubnik;
- greater variance behind him.

Their offense can function, but the reserve-QB chain carries more turnover/drive-stall risk than the Giants' Winston-led branch.

---

# 5. Current preseason team process

## Giants

Results:
- L 10-13 vs Minnesota
- W 26-3 at Miami

Game totals:
- 23
- 29

The 26-3 win was driven by:
- Winston's efficient first half;
- strong run/possession control;
- dominant defense;
- continued pressure on Miami's reserve offense.

The framework does not project a 23-point win automatically.

The mechanism that persists is:
`competent veteran reserve QB + defensive depth + field-position control`

## Jets

Results:
- L 16-24 vs Tampa Bay
- W 17-0 at Pittsburgh

Game totals:
- 40
- 17

The Pittsburgh shutout included:
- multiple sacks/negative plays;
- an interception near the red zone;
- another interception creating field-position control;
- Klubnik operating without turnovers.

The persistent mechanism is:
`defensive depth capable of forcing long-yardage and protecting a modest offensive output`

That is the strongest reason to prefer Under 37 and Jets +6 over a wide Giants-margin/high-total thesis.

---

# 6. Contract geometry

## Giants -1.5

Wins only if:
- Giants win by 2+.

## Jets +6.0

Wins if:
- Jets win;
- game ties;
- Jets lose by 1–5.

Pushes if:
- Giants win by exactly 6.

Loses if:
- Giants win by 7+.

### Important overlap

These are **not exact opposites**.

Both win if the Giants win by **2–5 points**.

Example:
**Giants 20-16**
- Giants -1.5: WIN
- Jets +6: WIN

---

## Over 33.5

Wins at:
- 34+ total points.

## Under 37.0

Wins at:
- 36 or fewer.

Pushes at:
- exactly 37.

Loses at:
- 38+.

### Total overlap

Both total contracts win at:
- 34
- 35
- 36

At exactly 37:
- Over 33.5 wins;
- Under 37 pushes.

This overlap materially shapes the ranking.

---

# 7. Weather

National Weather Service forecast for East Rutherford around game time:

- temperatures falling through the upper-70s°F;
- light winds;
- shower probability falling sharply after 8 PM;
- no strong sustained wind signal.

There was an afternoon shower/thunderstorm chance, but the evening forecast becomes increasingly benign.

Therefore weather receives only a small uncertainty modifier.

No automatic Under is assigned from rain risk.

---

# 8. Joint score tree

## Branch A — Giants narrow control / low total

Representative:
- Giants 17-13
- Giants 20-13

Mechanism:
- Winston/Allen avoid major mistakes;
- Giants field-position and defensive depth suppress Jets;
- Klubnik moves the ball but red-zone conversion stays modest.

17-13:
- Giants -1.5 WIN
- Jets +6 WIN
- Under 37 WIN
- Over 33.5 LOSS

20-13:
- Giants -1.5 WIN
- Jets +6 LOSS
- Under 37 WIN
- Over 33.5 LOSS

---

## Branch B — overlap sweet spot

Representative:
- Giants 20-16

Results:
- Giants -1.5 WIN
- Jets +6 WIN
- Over 33.5 WIN
- Under 37 WIN

This 34–36 point range is important because **all four supplied contracts can simultaneously cash depending on the exact margin**.

---

## Branch C — close higher-scoring game

Representative:
- Giants 20-17
- Jets 20-17

At 20-17:
- total = 37;
- Over 33.5 WIN;
- Under 37 PUSH.

The side depends on winner.

---

## Branch D — Giants separation

Representative:
- Giants 23-13
- Giants 24-13
- Giants 27-13

Mechanism:
- Winston-led offense gets early control;
- Jets deeper QBs turn the ball over;
- short fields create extra Giants points.

Effects:
- Giants -1.5 WIN
- Jets +6 LOSS
- Under/Over depends on exact total.

This is the strongest kill path for Jets +6.

---

## Branch E — Jets upset / defensive-control game

Representative:
- Jets 17-13
- Jets 20-16

Mechanism:
- Klubnik remains turnover-free;
- Jets defensive depth pressures Brandon Allen;
- Giants' Week 1 turnover branch returns.

Effects:
- Jets +6 WIN
- Giants -1.5 LOSS
- Under 37 WIN in both examples.

This is the strongest ordinary adverse state for the Giants winner selection.

---

# 9. Ranking rationale

## #1 — Under 37.0

Strongest marginal contract.

Support:
- Giants game totals: 23 and 29;
- Jets game totals: 40 and 17;
- three of four descriptive games stayed below 37;
- both regular starting QBs are expected to sit according to current reporting;
- Giants and Jets reserve defenses have each produced a dominant low-score game;
- Klubnik's current profile is efficient but low-explosive;
- the likely QB depth emphasizes roster evaluation over regular-season offensive systems.

Boundary benefit:
- at exactly 37, Under 37 only pushes rather than loses.

Main failure:
- Zappe/Cook/Allen turnover volatility creates short fields and non-offensive scoring;
- both teams' deep defensive rotations allow explosive plays.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Jets +6.0

This is the broadest side contract.

It wins:
- on any Jets win;
- any tie;
- any Giants win by 1–5.

It pushes at exactly a six-point Giants win.

Support:
- Jets defensive depth just pitched a shutout;
- Klubnik has not turned the ball over in two appearances;
- Giants' starter advantage is mostly removed if Dart and first-team players sit;
- final-preseason fourth-quarter personnel creates margin compression.

Why not #1:
- Winston is the most established QB expected to play;
- Giants won 26-3 last week;
- Zappe/Cook turnover variance creates a real 7+ Giants separation branch.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Giants -1.5

The Giants are the preferred winner.

Support:
- Winston's current 15/21, 150-yard half against Miami;
- Giants' veteran QB depth;
- strong reserve defensive showing last week;
- Brandon Allen improved significantly from Week 1 to Week 2.

Why below Jets +6:
- -1.5 loses every Jets win and every one-point Giants win;
- +6 protects nearly all close Giants victories;
- the Jets' defense and Klubnik's low-turnover profile keep the one-score branch broad.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Over 33.5

The line is low enough that a normal:
- 20-16;
- 20-17;
- 21-17

game clears it.

The strongest Over mechanisms:
- short fields from turnovers;
- deep-reserve missed assignments;
- aggressive fourth-down decisions;
- preseason special-teams volatility.

Why last:
- both teams are resting offensive starters;
- Giants' first two totals were 23 and 29;
- Jets' Week 2 total was only 17;
- reserve defensive process has been stronger than the raw offense in multiple games.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 10. Potential game winner

## New York Giants — `FORCED WINNER / LOW CONFIDENCE`

Primary mechanism:

`Winston/Allen experience + recent Giants reserve-offense competence + defensive depth -> slight Giants four-quarter advantage`

Strongest failure path:

`Klubnik remains efficient + Jets pressure forces Brandon Allen turnover/negative-play branch + Jets win a low-scoring field-position game`

A Jets outright win would not be surprising.

---

# 11. Final card

1. **Under 37.0 Points**
2. **Jets +6.0**
3. **Giants -1.5**
4. **Over 33.5 Points**

**Potential winner:** New York Giants

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

---

# 12. Source record

## Google Drive
- `PREDICTION_LOG_COMBINED.md`
- `RULES_GENERAL.md`
- `RULES_AMERICAN_FOOTBALL.md`
- active `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official NFL / team sources
- NFL game center / schedule
- Giants official schedule and game center
- Giants preseason Week 2 recap
- Giants Brandon Allen 2026 preseason splits
- Jets official schedule
- Jets Cade Klubnik 2026 preseason splits
- Jets Tampa Bay and Pittsburgh preseason recaps
- 2026 NFL rulebook

## Current participant-plan reporting
- current Giants game reporting: Dart/starters expected to sit
- current Jets reporting: Geno Smith/most starters expected to sit

These last participant-plan fields are **secondary-only** and are the reason for the evidence cap.

## Weather
- National Weather Service, East Rutherford

---

# 13. Limitations

- final starter/rest decisions were not independently recovered from field-owning official team releases at cutoff;
- exact Winston/Allen and Klubnik/Zappe/Cook snap shares are not frozen;
- final preseason roster-bubble substitutions create unusually large fourth-quarter variance;
- operator-specific full-game/action terms were not supplied;
- no fitted/validated American-football numerical model exists.

---

# 14. Logging confirmation

**Conversation-local ID:** `P-142`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Final intended issue state:** `PREGAME`

# P-143 (conversation-local continuation) — Tampa Bay Buccaneers @ Jacksonville Jaguars — NFL Preseason Week 3

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Tampa Bay Buccaneers -2.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Combined Total Over 35.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Jacksonville Jaguars +2.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Combined Total Under 35.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **Tampa Bay Buccaneers — FORCED WINNER / LOW-MEDIUM CONFIDENCE**

### Central qualitative score family

- Tampa Bay 20-16
- Tampa Bay 21-17
- Tampa Bay 23-17
- Tampa Bay 24-20
- Jacksonville 20-17

The central distribution is therefore:

`TB slight reserve-QB/depth edge + meaningful JAX close-game branch + total centered around the high-30s`

---

## Administrative note

Google Drive is being used strictly as a **read-only framework source**.

The active Drive queue has not been advanced by the recent locally delivered conversation cards, so this file is labelled **P-143 conversation-local continuation** to avoid reusing IDs inside this conversation.

It is not claimed to be the Drive-canonical ID until formally reconciled.

---

# 1. Record metadata

| Field | Value |
|---|---|
| Sport | American football |
| Competition | NFL Preseason Week 3 |
| Event | Tampa Bay Buccaneers @ Jacksonville Jaguars |
| Venue | EverBank Stadium, Jacksonville, Florida |
| Scheduled kickoff | 2026-08-28 19:30 America/New_York |
| Melbourne equivalent | 2026-08-29 09:30 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Tampa Bay starters | Expected to sit |
| Jacksonville starters | Officially expected to sit |
| Tampa Bay QB plan | Jalon Daniels reported to start and play first half / potentially into Q3; Jake Browning and Connor Bazelak behind him |
| Jacksonville QB plan | Trevor Lawrence out of game plan; Nick Mullens uncertain; Carter Bradley / Joey Aguilar major reserve branches |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_AMERICAN_FOOTBALL.md` |
| Numerical state | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 2. Updated Drive framework controls applied

The active American-football framework requires:

1. NFL preseason to be treated as a separate phase/population.
2. Regular-season roster strength to matter only insofar as those players actually receive snaps.
3. Starting/backup QB identity and expected reps to be decision-driving.
4. Offensive-line and skill-player depth to be represented as unit mixtures.
5. Expected drives, starting field position, third/fourth-down and red-zone process to determine scoring.
6. Turnover, explosive-play, special-teams and non-offensive-score tails to remain explicit.
7. Exact football key values to be preserved.
8. Winner, spread and total to derive from one shared discrete score tree.
9. Secondary-only decision-driving participant information to cap evidence rather than be treated as official fact.
10. No numerical win probability unless a fitted and validated football model exists.

No such validated model currently exists.

---

# 3. Participant release gate

## Jacksonville — field-owner official

Jacksonville's official team coverage is explicit:

- Head Coach Liam Coen has said the Jaguars' starters/front-line players **will not play** in the preseason finale.
- Trevor Lawrence is therefore removed from the full-game offensive model.
- Travon Walker, Josh Hines-Allen, Brenton Strange, Parker Washington and many other front-line players are likewise expected to sit.
- Nick Mullens may or may not receive work.
- Jacksonville's official Week 3 preview identifies **Carter Bradley and Joey Aguilar** as major reserve-QB storylines.

Participant state:

`JAX STARTER REST PLAN: CONFIRMED_OFFICIAL`

## Tampa Bay — team official + named secondary QB-start report

Tampa Bay's official team coverage says the Buccaneers are expected to hold:
- starters;
- key regulars

out of the preseason finale.

The official Bucs site specifically frames the game as a final roster audition and highlights the open backup-QB competition between:
- Jake Browning
- Jalon Daniels

A current named report from Tampa Bay Times / NBC Sports states:
- **Jalon Daniels will start**;
- he is expected to play the entire first half and possibly into Q3;
- Jake Browning and Connor Bazelak will follow.

That exact snap plan was not independently recovered from a field-owning Buccaneers release.

Participant state:

`TB STARTER REST PLAN: OFFICIAL EXPECTATION`
`TB JALON DANIELS START / HALF+ PLAN: SECONDARY_ONLY`

Because the exact Tampa Bay starting-QB exposure is still secondary-only:

**all four participant-sensitive rows remain capped at `FORCED RANK / MEDIUM-LOW`.**

---

# 4. Exact contract geometry

## Buccaneers -2.5

Wins if Tampa Bay wins by **3+**.

## Jaguars +2.5

Wins if:
- Jacksonville wins; or
- Jacksonville loses by 1–2.

These are exact half-point complements.

There is no push.

---

## Over 35.5

Wins at **36+** total points.

## Under 35.5

Wins at **35 or fewer**.

These are also exact half-point complements.

No push exists.

---

# 5. Tampa Bay quarterback process

## Jalon Daniels

Official Bucs results across the first two preseason games:

### Week 1 at Jets
- 10/15
- 111 passing yards
- rushing touchdown
- took over after halftime
- helped turn a close game into a 24-16 Tampa Bay win

### Week 2 vs Chiefs
- 9/14
- 71 passing yards
- 1 passing touchdown
- 19 rushing yards
- led **three consecutive scoring drives**
- Tampa Bay rallied from 9-0 down to win 16-15

Aggregate official passing:
- **19/29**
- **182 yards**
- **1 passing TD**
- **0 interceptions**

The important mechanism is not the 2-0 record itself.

It is:

`mobility + low-turnover decision-making + ability to extend plays + repeated second-half scoring-drive execution`

The official Buccaneers site states Daniels has led **five scoring drives and two game-winning rallies** across the first two games.

That is directly relevant if he truly receives half or more of tonight's QB exposure.

---

## Jake Browning

Week 2:
- approximately 9/12 for 84 yards in official Bucs reporting
- no interceptions
- substantial regular-season NFL experience, including 10 career starts

Browning provides a higher experience floor if he follows Daniels.

His current preseason sample has been less explosive than Daniels' but not turnover-heavy.

---

## Connor Bazelak

Week 1:
- 12/20
- 72 yards
- no touchdown
- no interception

Bazelak is the lower-scoring/deeper-game branch.

### Tampa Bay QB mixture

The Bucs therefore have:

1. Daniels — mobile/high-upside scoring-drive branch
2. Browning — veteran competence branch
3. Bazelak — lower-output depth branch

This is a relatively strong preseason QB mixture.

---

# 6. Jacksonville quarterback process

## Nick Mullens

Week 1:
- 3/7
- 33 yards
- 1 interception

Week 2:
- 6/7
- 65 yards
- led a 71-yard field-goal drive

He improved materially in Week 2.

However, the official Jaguars Week 3 preview says Mullens **may or may not play**, which makes him an uncertain exposure rather than the central four-quarter QB.

---

## Carter Bradley

Official Jacksonville Week 3 preview:

- **16/30**
- **156 yards**
- **1 touchdown**
- **2 interceptions**

Bradley is the key turnover/drive-stall branch.

Against Carolina he:
- completed 6/13 for 51 yards
- threw an interception that helped Carolina create a two-touchdown halftime lead

His mistakes increase:
- Tampa Bay short-field probability;
- Tampa Bay -2.5 separation probability;
- game Over tail through turnover-generated scoring.

---

## Joey Aguilar

Official Jaguars preseason:

- **10/11**
- **173 yards**
- **1 touchdown**
- **0 interceptions**

Week 2 vs Carolina:
- 9/10
- 130 yards
- 29-yard TD to Trebor Peña

Aguilar is the strongest Jacksonville upside branch.

His connection with Peña has generated:
- 43-yard completion in Week 1;
- 29-yard touchdown in Week 2.

This is the main reason Jacksonville +2.5 cannot be treated as a weak/no-offense position.

### Jacksonville QB mixture

The practical game tree is:

- possible short Mullens exposure;
- Bradley turnover/ordinary branch;
- Aguilar efficient/explosive second-half branch.

That is wider and less stable than Tampa Bay's projected Daniels/Browning sequence, but has a genuine late comeback/upset tail.

---

# 7. Preseason team process

## Tampa Bay

Results:
- **W 24-16 at Jets**
- **W 16-15 vs Chiefs**

Totals:
- 40
- 31

Tampa Bay has scored:
- 40 points over two games

Allowed:
- 31

The 24-point Week 1 result included a defensive pick-six, so the offense did not create all 24 points.

Week 2:
- offense was scoreless in the first half;
- Daniels then led three scoring drives;
- defense created a late interception that set up favorable field position.

Persistent mechanisms:
- defensive takeaway capability;
- Daniels' second-half efficiency;
- reserve defensive pressure;
- competent backup-QB depth.

---

## Jacksonville

Results:
- **W 24-20 at New Orleans**
- **L 17-34 vs Carolina**

Totals:
- 44
- 51

Jacksonville scored:
- 41 points

Allowed:
- 54

The Week 2 game is not directly comparable to tonight because:
- Carolina used more starting personnel early;
- Jacksonville used reserve-heavy units;
- weather ended the game with roughly two minutes remaining.

Persistent Jacksonville mechanisms:
- Cam Little field-goal reliability;
- Aguilar/Peña explosive connection;
- reserve defense has allowed meaningful sustained offense;
- Bradley turnover risk.

---

# 8. Scoring-drive process

## Tampa Bay central offensive branch

`Daniels mobility + reserve WR/RB auditions + Browning competence -> approximately 2–3 TD/FG scoring clusters`

Daniels has already shown:
- third-down improvisation;
- scrambling chain extension;
- late-game composure.

Tampa Bay's downside branch:
- first-half offense looks like Week 2 before Daniels took over;
- deep offensive-line combinations lose protection;
- Bazelak receives more late work;
- weather disrupts rhythm.

---

## Jacksonville central offensive branch

`Bradley/Aguilar rotation + reliable kicker + young receiving depth -> approximately 2–3 scoring drives`

Main support:
- Aguilar's efficiency;
- Peña explosiveness;
- Cam Little's field-goal conversion;
- home field.

Main downside:
- Bradley turnover;
- reserve protection;
- no Lawrence/front-line skill group;
- Tampa Bay reserve pass rush/DB takeaway ability.

---

# 9. Defensive / field-position process

## Tampa Bay

Week 1:
- Ayden Garnes returned an interception **47 yards for a touchdown**.

Week 2:
- Anthony Nelson generated 1.5 sacks;
- Tampa Bay created pressure;
- Roman Parodie intercepted a fourth-quarter pass and gave the offense a short-field opportunity.

This is not projected as a guaranteed defensive touchdown.

The mechanism that persists is:

`reserve front pressure + ball-hawking DB competition -> increased short-field tail`

That supports:
- Buccaneers -2.5;
- Over 35.5 through non-offensive/short-field scoring.

---

## Jacksonville

Jacksonville recorded four sacks against New Orleans in Week 1.

The reserve front therefore has enough pressure ability to create:
- Daniels/Browning negative plays;
- longer third downs;
- Under branches.

But the unit also conceded:
- 20 to New Orleans;
- 34 to Carolina.

The central defensive expectation is therefore mixed rather than dominant.

---

# 10. Weather

National Weather Service Jacksonville forecast:

- showers/thunderstorms likely in the evening;
- heavy rainfall/localized flooding is the principal weather concern;
- temperatures in the upper-70s/low-80s around game time;
- southeast winds generally light/moderate.

### Mechanistic interpretation

Rain is **not** assigned an automatic Under.

Possible Under mechanisms:
- wet ball;
- lower passing efficiency;
- slower footing;
- interrupted warmups or delay.

Possible Over/variance mechanisms:
- fumbles;
- short fields;
- blown defensive footing;
- special-teams mistakes.

Because wind is not forecast to be severe/persistent, the weather shifts **variance more than central scoring direction**.

It modestly lowers evidence confidence on the total.

---

# 11. Market-state cross-check — context only

Contemporaneous market snapshots around the research window generally showed:

- Tampa Bay favored by roughly **1.5 to 3.5**
- totals around **34.5 to 35.5**

The user's exact contracts:
- Tampa Bay -2.5
- Jacksonville +2.5
- Over 35.5
- Under 35.5

Market prices/consensus are **not** used as internal sports-model probabilities.

They are recorded only to verify that the supplied contracts are plausible contemporaneous lines.

---

# 12. Joint score tree

## Branch A — central Tampa Bay win / Over

Representative:
- Buccaneers 20-16
- Buccaneers 21-17
- Buccaneers 23-17

### 20-16
- Bucs -2.5 WIN
- Jaguars +2.5 LOSS
- Over 35.5 WIN
- Under LOSS

### 21-17
- Bucs -2.5 WIN
- Over WIN

### 23-17
- Bucs -2.5 WIN
- Over WIN

Mechanism:
- Daniels sustains multiple drives;
- Jacksonville scores through Aguilar/Little;
- Tampa Bay owns the stronger aggregate QB depth.

This is the **central branch**.

---

## Branch B — Tampa Bay narrow win / Jaguars cover

Representative:
- Buccaneers 20-18
- Buccaneers 17-16

Mechanism:
- Jacksonville's Aguilar branch is strong;
- Tampa Bay becomes conservative late;
- weather/roster rotation compresses the game.

Effects:
- Jaguars +2.5 WIN
- Bucs -2.5 LOSS

Total can land either side.

This is the main reason Jacksonville +2.5 remains credible.

---

## Branch C — Jacksonville upset

Representative:
- Jaguars 20-17
- Jaguars 23-20

Mechanism:
- Aguilar continues near-perfect efficiency;
- Bradley avoids turnovers;
- Jacksonville reserve defense gets pressure;
- Tampa Bay deep-QB/line branch stalls late.

Effects:
- Jaguars +2.5 WIN
- Bucs -2.5 LOSS
- Over likely in 23-20; 20-17 also Over

This is the strongest ordinary adverse state for the Bucs side.

---

## Branch D — low-output weather/backup game

Representative:
- Bucs 17-13
- Bucs 20-13
- Jaguars 17-14

Mechanism:
- field becomes wet;
- both teams become run-heavy;
- deep offensive lines create sacks;
- red-zone drives settle for field goals.

Effects:
- Under 35.5 WIN
- side depends on margin/winner.

This is the main Under branch.

---

## Branch E — turnover / deep-defense shootout

Representative:
- Bucs 27-17
- Bucs 27-20
- Jaguars 24-21

Mechanism:
- Bradley/Zappe-style turnover events;
- Daniels scrambles extend plays;
- deep defensive rotations give up explosive gains;
- short fields/special teams add possessions.

Effects:
- Over 35.5 WIN
- side depends on exact score

This is the strongest high-total tail.

---

# 13. Ranking rationale

## #1 — Buccaneers -2.5

Why it ranks first:

- Tampa Bay is 2-0 with its reserve-heavy game plans.
- Jalon Daniels has led **five scoring drives and two comeback wins**.
- Daniels has not thrown an interception.
- Browning supplies veteran NFL-starting experience behind him.
- Jacksonville is sitting Trevor Lawrence and most front-line players.
- Bradley has two interceptions in 30 preseason attempts.
- Tampa Bay's reserve defense has repeatedly created pressure and takeaways.

Why confidence remains capped:
- exact Daniels snap plan is secondary-only;
- Aguilar has been excellent;
- Jacksonville is at home;
- weather adds variance;
- a -2.5 line loses every 1–2 point Tampa Bay win.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Over 35.5

Support:

- Tampa Bay's two totals: 40 and 31.
- Jacksonville's two totals: 44 and 51.
- Jacksonville's Aguilar branch is efficient/explosive.
- Daniels has consistently generated second-half scoring drives.
- both teams will use deep defensive rotations;
- Tampa Bay's defensive pressure creates short-field/non-offensive scoring tails.
- a normal **20-16** game already wins the Over.

Why not #1:
- thunderstorms/heavy rain remain possible;
- both teams sit offensive starters;
- Tampa Bay produced only 16 last week;
- Bradley/Bazelak-type deep branches can create repeated punts.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Jaguars +2.5

Main support:

- any Jacksonville win cashes;
- a Tampa Bay win by one or two also cashes;
- Aguilar has been the most statistically efficient Jaguars QB;
- Jacksonville has home field;
- Tampa Bay's Week 2 win was only by one point;
- final-preseason fourth-quarter rotations create margin-compression risk.

Why below Bucs -2.5:
- Bucs own the more stable aggregate QB chain;
- Bradley turnover risk;
- Tampa Bay reserve defense creates short-field separation;
- Jags defense has allowed 54 points across two games.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Under 35.5

The Under has a credible branch:
- rain;
- reserve offensive-line sacks;
- starters resting;
- Tampa Bay's 16-15 Week 2 game;
- Jacksonville settling for field goals.

But 35.5 is low enough that:
- 20-16
- 21-17
- 20-17
- 24-14

all beat it.

With Daniels and Aguilar generating meaningful scoring-drive upside, plus turnover/short-field variance, the Under is the least robust supplied row.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 14. Potential game winner

## Tampa Bay Buccaneers — `FORCED WINNER / LOW-MEDIUM CONFIDENCE`

Primary chain:

`Daniels half+ upside + Browning experience + Tampa Bay reserve takeaways/pressure -> slightly stronger four-quarter drive distribution`

Strongest failure path:

`Aguilar continues high-efficiency play + Jacksonville home defensive pressure + Tampa Bay late deep-unit offense stalls -> Jaguars win one-score game`

A Jacksonville victory is a material, ordinary branch rather than an extreme upset state.

---

# 15. Final card

1. **Buccaneers -2.5**
2. **Over 35.5 Points**
3. **Jaguars +2.5**
4. **Under 35.5 Points**

**Potential winner:** Tampa Bay Buccaneers

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

# 16. Source record

## Google Drive
- `RULES_AMERICAN_FOOTBALL.md`
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- active `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official NFL / team sources
- NFL Preseason Week 3 schedule
- Buccaneers official schedule/game center
- Buccaneers official final-roster-audition preview
- Buccaneers official Week 1 recap
- Buccaneers official Week 2 recap
- Buccaneers official Jalon Daniels coverage
- Jaguars official Week 3 storylines
- Jaguars official Week 1 game report
- Jaguars official Week 2 game report
- Jaguars official depth chart / camp updates

## Current QB-plan corroboration
- NBC Sports / Tampa Bay Times report that Jalon Daniels starts and is expected to play the first half, possibly into Q3.

This exact Daniels exposure remains labelled `SECONDARY_ONLY`.

## Weather
- National Weather Service Jacksonville forecast and area forecast discussion.

## Market context only
- CBS/FanDuel/DraftKings current line snapshots around Tampa Bay -2.5 and total 34.5–35.5.

Market state was not used as an internal win-probability feature.

---

# 17. Limitations

- exact Tampa Bay QB snap plan was not independently field-owner confirmed;
- Nick Mullens' Jacksonville snap share is explicitly uncertain;
- both teams are using deep final-preseason rotations;
- thunderstorm timing/field conditions add operational variance;
- exact operator overtime/action terms were not supplied;
- no fitted/validated American-football numerical model exists.

---

# 18. Logging confirmation

**Conversation-local ID:** `P-143`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Forecast state:** `PREGAME`

# P-144 (conversation-local continuation) — Texas Rangers (Cody Bradford) @ Milwaukee Brewers (Logan Henderson) — MLB

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Texas Rangers +1.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Combined Total Over 7.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Milwaukee Brewers -1.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Combined Total Under 7.5 Runs** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **Milwaukee Brewers — FORCED WINNER / LOW-MEDIUM CONFIDENCE**

### Central qualitative score corridor

- Milwaukee 4-3
- Milwaukee 5-3
- Milwaukee 4-2
- Milwaukee 5-2
- Texas 4-3

The central state is therefore:

`MILWAUKEE SLIGHT-TO-MODERATE WINNER EDGE + TEXAS +1.5 REMAINS ROBUST + TOTAL CLUSTERS AROUND 7–8 RUNS`

The strongest high-total/separation branch is Milwaukee getting to 5–6 runs against Bradford plus the Texas bullpen.

---

## Administrative note

Google Drive was used strictly as a **read-only framework source**.

The active Drive snapshot still lists `P-137` as its next canonical ID because the recent locally delivered cards have not been appended into Drive. This file is therefore labelled **P-144 conversation-local continuation** to avoid ID reuse inside this conversation.

It is not claimed to be the Drive-canonical ID until formally reconciled.

---

# 1. Record metadata

| Field | Value |
|---|---|
| Sport | Baseball |
| League | MLB |
| Event | Texas Rangers @ Milwaukee Brewers |
| Venue | American Family Field, Milwaukee |
| Scheduled first pitch | 2026-08-28 18:40 America/Chicago |
| Melbourne equivalent | 2026-08-29 09:40 Australia/Melbourne |
| Final research refresh | `2026-08-29 09:30:26 Australia/Melbourne` |
| GAME-STATE | `PREGAME — MLB official scoreboard still Preview` |
| Texas starter | Cody Bradford — LHP |
| Milwaukee starter | Logan Henderson — RHP |
| Starter status | `PROBABLE_OFFICIAL — MLB VERIFIED` |
| MLB official starting orders | `TBD / NOT RELEASED AT RESEARCH CUTOFF` |
| Texas lineup secondary capture | `AVAILABLE` |
| Milwaukee lineup final field-owner capture | `NOT RELEASED` |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_BASEBALL.md` |
| Numerical state | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 2. Updated Drive framework controls applied

The current baseball framework requires:

1. exact event / starter identity before pitcher quality becomes decision-driving;
2. posted batting orders, catcher and defence where released;
3. participant mixtures and confidence caps when official orders remain unreleased;
4. starter batters-faced / pitch / inning / hook distributions rather than ERA alone;
5. season prior versus current starter regime;
6. bullpen-chain workload and quality separated;
7. sequencing, home-run and contact tails retained;
8. home-last-bat / extra-inning exposure;
9. explicit +1.5 cushion decomposition;
10. one joint run distribution for winner, run line and total;
11. exact half-run and integer-line settlement geometry;
12. no numerical probability without a fitted and validated baseball model.

MLB's official starting-lineup page still showed both teams as **TBD** at the research cutoff.

Therefore the participant-sensitive card remains capped at:

`FORCED RANK / MEDIUM-LOW`

---

# 3. Contract geometry

## Texas +1.5

Wins if:
- Texas wins; or
- Texas loses by exactly one run.

Loses only if:
- Milwaukee wins by 2+.

## Milwaukee -1.5

Wins only if:
- Milwaukee wins by 2+.

The run-line pair is an exact half-run complement.

---

## Over 7.5

Wins at:
- **8+ runs**

## Under 7.5

Wins at:
- **7 or fewer**

No push exists.

---

# 4. Official identity / current team context

MLB officially lists:

### Texas Rangers
- record: **66-68**
- starter: **Cody Bradford, LHP**
- 0-2
- 3.05 ERA
- 13 strikeouts

### Milwaukee Brewers
- record: **83-51**
- starter: **Logan Henderson, RHP**
- 8-2
- 2.60 ERA
- 79 strikeouts

Current broader team context:

### Texas
- 30-39 away
- 46-52 against right-handed starters
- 5-5 over the latest 10-game standings window
- coming off consecutive 11-7 and 10-4 losses to the White Sox after winning the opener 11-2

### Milwaukee
- 45-24 at home
- **26-13 against left-handed starters**
- 7-3 over the latest 10-game standings window
- coming off consecutive **8-1 and 8-2** wins against the Mets
- among the strongest overall run-differential teams in MLB

This gives Milwaukee the stronger winner prior before pitcher-specific adjustments.

---

# 5. Logan Henderson — current regime

Season:
- 8-2
- 2.60 ERA
- 3.33 FIP in current specialist reporting
- approximately 0.89 WHIP
- 79 strikeouts in 69⅓ innings

MLB's current matchup preview notes:

**Henderson has allowed 3 earned runs or fewer in 18 consecutive starts.**

August:

| Date | Opponent | IP | ER | K | BB | HR |
|---|---|---:|---:|---:|---:|---:|
| Aug 22 | Atlanta | 6.0 | 1 | 4 | 2 | 0 |
| Aug 16 | Dodgers | 7.0 | 1 | 6 | 1 | 1 |
| Aug 10 | San Diego | 6⅓ | 3 | 7 | 1 | 2 |
| Aug 4 | Pittsburgh | 6.0 | 2 | 8 | 1 | 2 |

August aggregate:
- 25⅓ IP
- 7 ER
- 25 K
- 5 BB

### Henderson central mechanism

`strong K/BB control + low WHIP + regular six-plus-inning exposure -> reduced Texas scoring clusters`

This is the strongest Under mechanism in the game.

### Henderson adverse tail

He has still allowed five home runs in the four-start August sample.

Texas retains:
- Corey Seager;
- Wyatt Langford;
- Joc Pederson;
- Brandon Nimmo;
- Jake Burger;
- Evan Carter

in the current secondary lineup capture.

Therefore a two-homer / 3–4 run Texas branch remains live.

---

# 6. Cody Bradford — small-sample return regime

Bradford missed:
- all of 2025;
- the first four months of 2026

with an arm injury before returning in August.

His entire current MLB sample is only **four starts / 20⅔ innings**.

August:

| Date | Opponent | IP | ER | H | K | BB | HR |
|---|---|---:|---:|---:|---:|---:|---:|
| Aug 22 | Angels | 5⅓ | 2 | 7 | 3 | 0 | 0 |
| Aug 16 | Athletics | 4.0 | 2 | 8 | 4 | 1 | 1 |
| Aug 11 | Angels | 7.0 | 3 | 5 | 1 | 1 | 0 |
| Aug 5 | Giants | 4⅓ | 0 | 5 | 5 | 2 | 0 |

Aggregate:
- 20⅔ IP
- 7 ER
- **25 hits**
- only **13 strikeouts**
- 4 walks
- 1 home run
- 3.05 ERA
- approximately 3.18 FIP in current specialist reporting

### Bradford central branch

His command has been good enough to limit:
- walks;
- home-run clusters;
- major innings.

That supports a competitive 2–4 run Milwaukee state rather than an automatic blowout.

### Bradford adverse branch

The 3.05 ERA is a very small return-from-injury sample.

The low strikeout rate and 25 hits in 20⅔ innings show significant ball-in-play exposure.

Against a Milwaukee offense that:
- is hot;
- runs deep through the lineup;
- has gone 26-13 against left-handed starters;

that contact dependence produces a meaningful:
- 4–5 run central Milwaukee branch;
- 6+ run upper tail.

This is the main Brewers -1.5 / Over mechanism.

---

# 7. Texas offensive regime

Latest 10-game StatMuse run total:
- **38 runs**
- 3.8 per game descriptively

Recent:
- 2
- 0
- 5
- 11
- 7
- 4

The last three road games at Chicago produced:
- 11
- 7
- 4

but that scoring came against a very different pitching environment.

It should **not** be transferred directly against Henderson.

### Current secondary lineup capture

1. Joc Pederson — DH
2. Corey Seager — SS
3. Wyatt Langford — LF
4. Brandon Nimmo — RF
5. Ezequiel Duran — 3B
6. Evan Carter — CF
7. Jake Burger — 1B
8. Tyler Freeman — 2B
9. Danny Jansen — C

MLB's field-owning lineup page remained TBD at cutoff, so this is not promoted to `CONFIRMED_OFFICIAL`.

### Texas absences

Current injury reporting includes:
- Josh Jung — calf
- Kyle Higashioka — forearm
- Robert Garcia — shoulder
- other pitching depth absences

Jung/Higashioka reduce some lineup/bench flexibility.

---

# 8. Milwaukee offensive regime

StatMuse latest 10-game window:
- **66 runs**
- .313/.373/.453 team batting line over that descriptive window

Recent results:
- 8-2 at Mets
- 8-1 at Mets
- 2-3 at Mets
- 2-4 vs Atlanta
- 4-1 vs Atlanta
- 2-1 vs Atlanta
- 7-4 vs Seattle

Milwaukee has scored **16 runs in its last two games**.

Current Reuters reporting:
- Jackson Chourio went **4-for-5 with two two-run homers** yesterday;
- Milwaukee has won **eight of its last eleven**.

Current team-focused reporting also identifies:
- Chourio in a major power surge;
- Christian Yelich hitting well recently.

These are current-regime facts, not proof the Brewers must remain hot.

### Handedness mechanism

Milwaukee is **26-13 against left-handed starters**.

That result is descriptive.

The mechanism that matters is the availability of:
- multiple right-handed/switch-hitting bats;
- Chourio;
- William Contreras;
- Andrew Vaughn;
- Gary Sánchez / Joey Ortiz-type right-handed branches

against Bradford's low-whiff left-handed profile.

---

# 9. Milwaukee run prevention / bullpen

Milwaukee has one of the strongest pitching/relief environments in MLB.

Latest 10-game StatMuse window:
- only **25 runs allowed**

Recent:
- 2 allowed
- 1
- 3
- 4
- 1
- 1
- 4

The broader team ERA is among MLB's best.

Current bullpen context includes:
- Trevor Megill as the main leverage closer;
- several relief injuries/availability issues;
- a demanding 16-game-in-16-day stretch.

However, Thursday's 8-2 win featured six innings from Jacob Misiorowski, avoiding a full bullpen game.

The previous day's emergency outing after Dustin May was hit by a comebacker required Robert Gasser to work 5⅓ relief innings, meaning some bulk depth has been taxed even though the leverage chain was not completely emptied.

Framework interpretation:

**freshness and quality are separate.**

Milwaukee still has the better broad late-game run-prevention prior.

---

# 10. Texas bullpen

Texas received an off day Thursday after allowing:
- 11 runs Tuesday;
- 10 runs Wednesday

against Chicago.

That off day improves short-term availability.

But Texas' broader pitching/relief run prevention is weaker than Milwaukee's, with current team-focused previews placing the Rangers well below Milwaukee in team ERA.

Current bullpen injuries include:
- Robert Garcia;
- additional depth absences.

This creates a material Milwaukee late-scoring tail even if Bradford leaves a close game.

---

# 11. Park / roof / weather

American Family Field has a retractable roof.

The official Brewers roof-status page does not expose a current machine-readable open/closed status; it directs users to the roof-status hotline.

Therefore:

`ROOF STATUS: NOT OFFICIALLY VERIFIED AT CUTOFF`

A current third-party game model displayed **roof closed**, but that is not promoted to official fact.

Because roof state is unresolved and can neutralize outside weather:

**weather receives minimal directional weight.**

No total direction is assigned from outdoor Milwaukee conditions.

---

# 12. Market-state cross-check — context only

A contemporaneous broad market snapshot showed approximately:
- Brewers ML around **-182**
- Rangers around **+148**
- main total around **8.0 runs**

The user's exact supplied contracts are:
- Texas +1.5
- Milwaukee -1.5
- Over 7.5
- Under 7.5

This is recorded only as current market/contract context.

It is **not** used as an internal probability, calibration target or value claim.

---

# 13. Joint run distribution / scenario tree

## Branch A — Milwaukee narrow win / Under

Representative:
- Brewers 4-3
- Brewers 3-2

Mechanism:
- Henderson suppresses Texas but allows isolated power;
- Bradford competes;
- Milwaukee edges late.

### 4-3
- Texas +1.5 WIN
- Milwaukee -1.5 LOSS
- Under 7.5 WIN
- Over LOSS

### 3-2
- Texas +1.5 WIN
- Under WIN

This is the strongest support for Rank #1.

---

## Branch B — Milwaukee two-run win / Under

Representative:
- Brewers 4-2
- Brewers 5-2

### 4-2
- Brewers -1.5 WIN
- Texas +1.5 LOSS
- Under 7.5 WIN

### 5-2
- Brewers -1.5 WIN
- Under WIN

Mechanism:
- Henderson dominates;
- Brewers create enough contact against Bradford;
- Milwaukee bullpen suppresses Texas late.

---

## Branch C — Milwaukee win / Over

Representative:
- Brewers 5-3
- Brewers 6-2
- Brewers 6-3

Mechanism:
- Bradford's ball-in-play exposure becomes clustered damage;
- Milwaukee's hot offense creates 5+;
- Texas gets 2–3 through power or bullpen.

Effects:
- Milwaukee -1.5 usually WIN
- Over 7.5 WIN

This is the main reason Over ranks above Under despite Henderson.

---

## Branch D — Texas upset / close game

Representative:
- Rangers 4-3
- Rangers 5-4

Mechanism:
- Henderson's home-run tail appears;
- Bradford's weak-contact/control branch holds;
- Texas' rested bullpen protects a lead.

Effects:
- Texas +1.5 WIN
- Milwaukee -1.5 LOSS
- total depends on exact score

This branch materially increases Rank #1.

---

## Branch E — Milwaukee separation

Representative:
- Brewers 6-1
- Brewers 7-2
- Brewers 8-2

Mechanism:
- Bradford cannot miss enough bats;
- Milwaukee right-handed core repeatedly reaches base;
- Texas relief cannot contain the game.

Effects:
- Milwaukee -1.5 WIN
- Over wins at 7-2 / 8-2
- 6-1 remains Under despite a large margin

This preserves the framework rule that **low total does not imply close margin**.

---

# 14. Ranking rationale

## #1 — Rangers +1.5

Most forgiving individual contract.

It wins on:
- every Texas victory;
- every one-run Milwaukee victory.

Why it ranks first despite Milwaukee being the preferred winner:
- Henderson can suppress Texas without Milwaukee necessarily scoring enough for separation;
- Bradford has kept all four starts reasonably competitive;
- 4-3 / 3-2 Milwaukee outcomes are ordinary;
- Texas had Thursday off, helping late-game bullpen availability.

Main failure:
- Milwaukee converts Bradford's high-contact profile into 4–6 runs and wins by 2+.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Over 7.5

The total is close, but 7.5 is low enough that an ordinary:

- 5-3
- 4-4 through nine
- 6-2

state wins the Over.

Support:
- Milwaukee scored 66 over its latest 10-game window;
- 16 in the last two;
- Bradford has a low strikeout rate and high hit count;
- Texas' broader relief run prevention is weaker;
- Texas itself has produced 22 runs over the last three games.

Why not #1:
- Henderson is excellent;
- Milwaukee has allowed only 25 over its last 10;
- Bradford has limited walks/homers in the small return sample.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Brewers -1.5

Milwaukee has the stronger underlying winner state.

Support:
- 83-51 overall;
- 45-24 at home;
- 26-13 vs left-handed starters;
- Henderson's current run suppression;
- Brewers' hot offense;
- Texas' weaker road record and bullpen;
- Bradford's small-sample contact dependence.

Why only third:
- -1.5 needs actual separation;
- a 4-3/3-2 Milwaukee win loses the contract;
- Rangers +1.5 survives every Texas upset.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Under 7.5

The Under is absolutely credible.

Support:
- Henderson;
- Milwaukee's strong bullpen / recent run prevention;
- Bradford's good walk/HR suppression;
- 4-2, 4-3, 5-2 all stay Under.

Why last:
- 7.5 gives no push protection;
- Milwaukee's current offense is extremely hot;
- Bradford's low K rate creates significant sequencing risk;
- Texas has recently found more extra-base damage;
- an ordinary 5-3 result already beats the line.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 15. Potential game winner

## Milwaukee Brewers — `FORCED WINNER / LOW-MEDIUM CONFIDENCE`

Primary chain:

`Henderson starter advantage + stronger Milwaukee offense + Brewers vs-LHP success + home field/last bat + stronger relief prior -> Milwaukee winner edge`

Strongest ordinary failure path:

`Bradford weak-contact/control branch + Henderson HR tail + rested Texas bullpen -> Rangers win a one-run game`

A Texas upset is not treated as an extreme tail.

---

# 16. Final card

1. **Texas Rangers +1.5**
2. **Over 7.5 Runs**
3. **Milwaukee Brewers -1.5**
4. **Under 7.5 Runs**

**Potential winner:** Milwaukee Brewers

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

---

# 17. Source record

## Google Drive framework
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official MLB
- MLB Probable Pitchers — Bradford / Henderson
- Rangers probable-pitcher page
- Brewers probable-pitcher page
- MLB Starting Lineups — final orders still TBD at cutoff
- Brewers scoreboard / game page
- MLB current standings
- MLB current matchup preview

## Specialist / reputable current evidence
- StatMuse Bradford game log
- StatMuse Henderson game log
- StatMuse Rangers recent runs
- StatMuse Brewers recent offense/run prevention
- Baseball-Reference exact matchup preview
- Reuters Brewers–Mets recaps
- current Rangers/Brewers team-focused series and lineup reporting

## Limitations
- MLB field-owner starting orders remained `TBD` at cutoff;
- Milwaukee final batting order was therefore not assumed;
- official roof open/closed state was not recoverable;
- Bradford's current sample is only four post-injury starts;
- exact operator listed-pitcher/action terms were not supplied;
- no fitted/validated baseball probability model exists.

---

# 18. Logging confirmation

**Conversation-local ID:** `P-144`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Forecast state:** `PREGAME`

# P-145 (conversation-local continuation) — Connecticut Sun @ Indiana Fever — WNBA

## State warning

**FINAL ISSUE STATE:** `SCHEDULED TIP CROSSED — EXACT LIVE SCORE/CLOCK NOT VERIFIED`

Official WNBA scheduling lists:
- Connecticut Sun @ Indiana Fever
- Friday, August 28, 2026
- 7:30 PM ET
- Gainbridge Fieldhouse, Indianapolis

That is **9:30 AM Australia/Melbourne on August 29, 2026**.

During research, scheduled tip crossed. At the final refresh, the official WNBA game page still did not expose a usable live score/clock and multiple current score surfaces still showed preview/no-play state.

Under `MDS-2026.08.29-v2.5`, this card therefore **does not convert the original pregame lines into live advice**.

The ranking below is the **frozen pre-start evidence view** only.

---

## Executive pre-start forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Indiana Fever -17.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Combined Total Over 177.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Connecticut Sun +17.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Combined Total Under 177.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential game winner:** **Indiana Fever — FORCED WINNER / MEDIUM-LOW CONFIDENCE**

### Central qualitative score corridor

- Indiana 99-78
- Indiana 101-80
- Indiana 102-79
- Indiana 98-82

This implies:
- strong Indiana winner/separation branch;
- game total centered around the high-170s/low-180s;
- meaningful garbage-time compression branch that keeps Connecticut +17.5 alive.

---

# 1. Administrative note

Google Drive was used strictly as a **read-only framework source**.

The active Drive snapshot has not been advanced by the recent local cards in this conversation. This file is labelled **P-145 conversation-local continuation** to avoid ID reuse.

It is not claimed to be the Drive-canonical ID until reconciled there.

---

# 2. Record metadata

| Field | Value |
|---|---|
| Sport | Basketball |
| League | WNBA |
| Event | Connecticut Sun @ Indiana Fever |
| Venue | Gainbridge Fieldhouse, Indianapolis |
| Scheduled tip | 2026-08-28 19:30 America/New_York |
| Melbourne equivalent | 2026-08-29 09:30 Australia/Melbourne |
| Final research refresh | approximately 2026-08-29 09:34 Australia/Melbourne |
| State | `START CROSSED — EXACT LIVE STATE NOT VERIFIED` |
| Connecticut record | 10-28 |
| Indiana record | 25-14 |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_BASKETBALL.md` effective 2026-08-29 |
| Numerical state | `NTS-2026.08.25-v0.2 — DESIGN ONLY / NO FITTED BASKETBALL MODEL` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 3. Framework controls applied

The updated basketball module requires:

1. exact league/rules/OT/phase identity;
2. newest official injury/availability report;
3. confirmed starting five when available;
4. active status separated from expected minutes/usage/closing-lineup probability;
5. possessions and efficiency built jointly;
6. shot profile, turnovers, offensive rebounds and free throws treated mechanistically;
7. blowout/garbage time treated as two-sided;
8. large spreads modeled using opening separation, maximum lead and closing margin separately;
9. mismatch total and margin derived from the same game tree;
10. current roster regime explicitly reconciled against old H2H;
11. late fouling and OT included as explicit tails;
12. no numerical probability unless the target-specific model is fitted/validated.

Current confirmed starting fives were not recovered from a field-owning league/team release before the issue cutoff.

Therefore all participant-sensitive rows are capped at:

`FORCED RANK / MEDIUM-LOW`

---

# 4. Contract geometry

## Connecticut +17.5

Wins if Connecticut:
- wins outright; or
- loses by 17 or fewer.

Loses if Indiana wins by 18+.

## Indiana -17.5

Wins only if Indiana wins by 18+.

These are exact half-point complements.

---

## Over 177.5

Wins at:
- 178+ combined points

## Under 177.5

Wins at:
- 177 or fewer

No push exists.

---

# 5. Indiana team baseline

Indiana enter:
- **25-14**
- 13-6 at home
- one of the league's top teams

Current season profile:

- **96.6 PPG — 1st in WNBA**
- **117.6 offensive rating — 1st**
- **81.2 pace — among the league's fastest**
- **48.9% FG**
- **39.5% from three**
- **90.9 PPG allowed**
- approximately **110.7 defensive rating**

This is not simply a high-scoring team.

The key process is:

`fast pace + elite shooting efficiency + multiple primary creators + strong spacing -> very high offensive ceiling`

The defensive weakness matters for the total because Connecticut does not need elite offense to reach a useful 75–82 point branch.

---

# 6. Indiana current offensive regime

Recent results:

- 113-90 at Chicago
- 102-109 at New York
- 85-91 at Dallas
- 101-95 at Toronto
- 95-91 at Atlanta

Indiana has scored:
- 95+
- in four of the last five

and:
- 100+
- in three of the last four

The mechanism is not the raw streak.

It is:
- Caitlin Clark creation;
- Kelsey Mitchell shooting/scoring;
- floor spacing;
- high three-point conversion;
- strong transition pressure.

### Caitlin Clark

Current season:
- approximately **22.1 PPG**
- **8.3 APG**

Latest game:
- **37 points**
- **10 assists**
- career-high eight threes

Current status:
- **probable** with a back issue
- no reported minutes restriction in the latest pregame reporting

### Kelsey Mitchell

Current season:
- approximately **24.8 PPG**
- around **45.5% from three**

Latest game:
- **30 points**

Her current scoring streak and three-point efficiency are major Connecticut matchup problems because Connecticut's depleted lineup has less room for defensive role specialization.

---

# 7. Aliyah Boston regime change

Boston missed Indiana's 113-90 win at Chicago because of a lower-leg issue.

Current pregame reporting says she is:
- **off the injury report / available**
- expected to return against Connecticut.

Season:
- approximately 17.0 PPG
- 8.4 RPG
- strong interior scoring/rebounding
- current-season three-point growth

### Mechanistic impact

Her return adds:
- interior finishing;
- screening;
- offensive rebounding;
- defensive rebounding;
- rim deterrence;
- additional passing hub play.

This matters especially because Connecticut is simultaneously missing major frontcourt depth.

Boston's exact minutes after injury remain uncertain, so the model does not assume a full maximum workload.

---

# 8. Connecticut current roster regime

Connecticut enter:
- **10-28**
- 3-7 over their latest 10
- one of the league's weakest net-rating teams

Season scoring:
- **78.8 PPG**

Current roster is materially weaker than its broad season baseline.

## Brittney Griner — OUT

Griner is unavailable with a knee injury.

This removes:
- interior scoring;
- post gravity;
- rim deterrence;
- rebounding size.

## Kennedy Burke — OUT / not with team

Burke has departed for international duty.

This removes:
- wing minutes;
- shooting;
- perimeter defensive flexibility.

## Leila Lacan — OUT / international duty

Lacan has left to represent France at the World Cup.

She was Connecticut's:
- leading scorer in current broad team leader data;
- primary assist creator;
- primary point-of-attack organizer.

This is a major offensive-regime change.

## Olivia Nelson-Ododa — questionable / uncertain

Nelson-Ododa was dealing with a knee issue and had missed recent games.

If unavailable or limited, Connecticut loses another:
- rebounder;
- interior finisher;
- defensive big.

### Current offensive replacement tree

Charlisse Leger-Walker has taken on more point-guard responsibility.

Against Golden State:
- career-high **17 points**
- 4 assists

But this creates a new role distribution rather than preserving Lacan's established creation structure.

Connecticut therefore has:
- lower creator depth;
- lower interior finishing;
- thinner frontcourt;
- more inexperienced minutes.

---

# 9. Rest/travel asymmetry

This is one of the stronger contextual mechanisms.

## Indiana

Indiana last played:
- August 23 at Chicago

This gives several days:
- off game load;
- recovery from a demanding road trip;
- practice time at home.

That matters mechanistically through:
- fresher transition legs;
- improved closeout effort;
- higher shot quality;
- more stable starter minutes.

## Connecticut

Connecticut played:
- August 25 vs Chicago
- August 26 vs Golden State

then traveled to Indiana for August 28.

That is:
- two games in two days;
- one off day;
- road travel;
- depleted rotation.

No automatic fatigue penalty is assigned.

The plausible pathways are:
- slower transition recovery;
- lower shooting legs;
- higher turnover risk;
- reduced closing-lineup resilience.

This supports Indiana's separation branch.

---

# 10. Recent Connecticut scoring environment

Recent five:

- 64 vs Golden State
- 87 vs Chicago
- 68 at Los Angeles
- 78 at Las Vegas
- 85 vs Los Angeles

Descriptive average:
approximately mid-70s.

Important mechanism:
- low offensive floor;
- heavy dependence on limited creators;
- inconsistent three-point efficiency;
- current roster losses.

However, Indiana's defense is one of the weaker units among contenders.

So Connecticut still owns a credible:
- 77–82 point branch

through:
- transition;
- second units;
- late-game garbage-time scoring;
- Indiana's weaker defensive efficiency.

That branch is important for the Over.

---

# 11. Head-to-head — 2026

Indiana leads the season series **2-0**.

## June 13
Indiana **85-75**
Total: 160
Margin: 10

Contracts at today's lines:
- Connecticut +17.5 — WIN
- Indiana -17.5 — LOSS
- Under 177.5 — WIN
- Over 177.5 — LOSS

## July 22
Indiana **123-88**
Total: 211
Margin: 35

Contracts:
- Indiana -17.5 — WIN
- Over 177.5 — WIN

Current Indiana stars in that game:
- Clark 27
- Mitchell 23
- Boston 22

### H2H weighting

The 35-point July result is relevant because:
- same venue;
- same core Indiana creators;
- similar offensive system.

But current Connecticut is even more depleted in some areas.

The 10-point June result remains equally important as proof that:
- Indiana dominance does not mechanically guarantee an 18+ closing margin.

The two games therefore create a wide margin distribution rather than a simple vote.

---

# 12. Extreme-spread analysis

The updated framework explicitly prohibits treating a huge spread as automatic safety.

Three separate quantities matter:

## Opening separation

Indiana has strong support to create an early lead:
- superior offense;
- fresher legs;
- home court;
- Connecticut depleted.

## Maximum lead

A 20–30 point Indiana maximum lead is a materially plausible state.

## Closing margin

This is different.

If Indiana leads by 20+:
- Clark/Mitchell/Boston minutes can fall;
- Fever bench usage rises;
- Connecticut can score against deeper reserves;
- defensive urgency can drop;
- late possessions may become faster/looser.

That produces a real **garbage-time compression** branch.

Therefore:
- Indiana -17.5 is directionally supported;
- but Connecticut +17.5 remains live enough that it cannot be dismissed.

---

# 13. Total process

## Over mechanisms

1. Indiana owns the league's best offense.
2. Indiana plays at a fast pace.
3. Clark/Mitchell are in high-scoring form.
4. Boston returns.
5. Connecticut is depleted defensively.
6. Indiana's own defense is weak enough to allow Connecticut 75–82.
7. Blowout bench minutes can increase late pace and reduce defense.
8. User's 177.5 threshold is below several current broad market totals observed around 180.5–182.5.

The market comparison is context only.

## Under mechanisms

1. Connecticut's offense is depleted.
2. Lacan/Griner/Burke are unavailable.
3. Nelson-Ododa may be unavailable/limited.
4. Connecticut recently scored only 64.
5. A large Indiana lead can reduce starter offensive minutes.
6. Indiana could win via suppression rather than a shootout.

The key issue is whether Connecticut can contribute enough.

The central Connecticut band is approximately:
- 76–82

while Indiana's central band is approximately:
- 98–103.

That puts a large share of the central qualitative corridor near:
- **176–185 total points**.

At the exact 177.5 line, the Over is narrowly preferred.

---

# 14. Joint score tree

## Branch A — Indiana high-efficiency blowout / Over

Representative:
- Indiana 103-79
- Indiana 102-78
- Indiana 105-80

Mechanism:
- Clark/Mitchell dominate perimeter creation;
- Boston restores interior edge;
- Sun turnovers create transition;
- Fever maintain scoring through bench minutes.

Results:
- Indiana -17.5 WIN
- Over 177.5 WIN

This is the strongest pro-Fever state.

---

## Branch B — Indiana controls but garbage time compresses

Representative:
- Indiana 99-83
- Indiana 100-84
- Indiana 98-82

Mechanism:
- Indiana builds a 20+ maximum lead;
- starters sit early;
- Connecticut scores against second-unit defense.

Results:
- Connecticut +17.5 WIN
- Over 177.5 usually WIN

This branch is why Over is compatible with Sun +17.5.

---

## Branch C — Indiana suppression / Under

Representative:
- Indiana 96-74
- Indiana 98-76
- Indiana 95-77

Mechanism:
- Connecticut cannot replace Lacan/Griner creation;
- Indiana controls the glass;
- Connecticut three-point shooting remains poor;
- Fever starter minutes fall in the fourth.

Results:
- Indiana -17.5 usually WIN
- Under 177.5 WIN

This is the strongest Under branch.

---

## Branch D — competitive Connecticut cover

Representative:
- Indiana 94-81
- Indiana 97-82

Mechanism:
- Leger-Walker handles lead creation well;
- Fever three-point shooting normalizes;
- Boston returns on a managed workload;
- Indiana defense leaks points.

Results:
- Connecticut +17.5 WIN
- total can land either side

This is the strongest ordinary Sun-cover state.

---

## Branch E — very wide Fever rout

Representative:
- Indiana 108-76
- Indiana 110-75
- Indiana 107-72

Mechanism:
- Connecticut turnovers;
- Indiana transition;
- extreme perimeter shooting;
- Sun fatigue/depth failure.

Results:
- Indiana -17.5 WIN
- Over often WIN at higher Connecticut outputs;
- Under possible in 107-72? total 179, still Over.

This demonstrates why a very large margin does not automatically imply Under.

---

# 15. Ranking rationale

## #1 — Indiana Fever -17.5

Why first:

- enormous offensive efficiency gap;
- Indiana 25-14 vs Connecticut 10-28;
- Indiana league-best offense;
- Connecticut missing several decision-driving players;
- Boston returns;
- Indiana is much better rested;
- previous Indiana home meeting ended 123-88;
- Connecticut just lost 89-64 at home.

Why only MEDIUM-LOW:
- 17.5 is extreme;
- garbage-time compression is real;
- confirmed starting fives were not recovered;
- Boston/Clark exact workload remains uncertain.

Strongest failure:
Indiana leads comfortably but finishes only 12–16 ahead after bench-heavy fourth quarter.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Over 177.5

Why second:

- Indiana averages 96.6 and has scored 100+ in three of four;
- league-leading offense and fast pace;
- Connecticut's depleted defense;
- Indiana's weak defense leaves Connecticut a 75–82 branch;
- Clark/Mitchell high-end scoring form;
- Boston return;
- user threshold 177.5 is below multiple current broader market totals.

Strongest failure:
Connecticut cannot create offense and Indiana reduces pace/minutes once ahead, producing 96-74 / 98-76.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Connecticut +17.5

Support:

- 17.5 is a huge cushion;
- first 2026 H2H was only a 10-point Indiana win;
- blowout garbage-time compression is specifically supported by the basketball framework;
- Indiana defensive rating is weak for a contender;
- late Connecticut bench scoring can close a 20+ maximum lead.

Why below Indiana -17.5:

- current Connecticut roster is materially weaker;
- Indiana is rested;
- Boston is returning;
- July meeting was a 35-point Indiana win;
- Sun's current creator/frontcourt shortages are severe.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Under 177.5

The Under has a strong low-Sun-output route.

But at this exact threshold:
- a 99-79 game = 178;
- a 100-80 game = 180;
- a 98-82 game = 180.

Indiana can clear the total through its offense without needing Connecticut to play well.

With Connecticut's depleted defense and Indiana's own weak defense creating two-sided scoring routes, the Under is the least robust row.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 16. Potential game winner

## Indiana Fever — `FORCED WINNER / MEDIUM-LOW CONFIDENCE`

This is the clearest qualitative conclusion.

Primary chain:

`Indiana elite offense + home court + rest advantage + Clark/Mitchell form + Boston return + Connecticut roster depletion -> Indiana winner`

Strongest ordinary failure:
- unexpected Clark limitation;
- poor Indiana shooting;
- Connecticut's new creator rotation materially outperforms expectation.

An outright Connecticut win remains a low-frequency branch relative to the central tree.

---

# 17. Final pre-start card

1. **Indiana Fever -17.5**
2. **Over 177.5 Points**
3. **Connecticut Sun +17.5**
4. **Under 177.5 Points**

**Potential winner:** Indiana Fever

**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value:** `NO VALUE DETERMINABLE`

---

# 18. Source record

## Google Drive
- `RULES_BASKETBALL.md` — effective 2026-08-29
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- active `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official league/team
- WNBA game page, game ID `1022600292`
- Indiana Fever official news / game-preview index
- Indiana Fever official practice/injury content
- Connecticut team status reporting referenced through current injury releases

## Current statistical / reputable sources
- Basketball-Reference 2026 WNBA team advanced stats
- Basketball-Reference Indiana team stats / starting-lineup history
- StatMuse current schedule/game context
- Reuters current Aliyah Boston injury reporting
- current live-score/preview cross-checks

## Availability state at cutoff
Connecticut:
- Brittney Griner — OUT
- Kennedy Burke — OUT / not with team
- Leila Lacan — OUT / international duty
- Olivia Nelson-Ododa — questionable / uncertain

Indiana:
- Caitlin Clark — probable, back
- Aliyah Boston — available / returning
- Damiris Dantas — out for season

## Limitations
- scheduled tip crossed before delivery;
- exact live score/clock could not be verified;
- confirmed starting fives were not recovered from a field-owning source;
- exact Clark/Boston post-injury minutes were not frozen;
- operator OT/settlement wording was not supplied;
- no fitted/validated basketball numerical model exists.

---

# 19. Logging confirmation

**Conversation-local ID:** `P-145`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Disposition:** `START CROSSED — EXACT LIVE STATE NOT VERIFIED — PRE-START EVIDENCE VIEW ONLY`

# P-146 (conversation-local continuation) — Gotham FC (W) vs Portland Thorns (W) — NWSL

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Gotham FC Team Corners Over 4.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Full Match Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Full Match Under 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **5** | **1st Half Under 0.5 Goals** | `AVOID / FORCED RANK` | `MEDIUM-LOW` |

**Potential regulation winner:** **Gotham FC — FORCED WINNER / MEDIUM-LOW CONFIDENCE**

### Central qualitative score family

- Gotham 2-1 Portland
- Gotham 2-0 Portland
- 1-1 draw
- Gotham 1-0 Portland

### Central first-half family

- Gotham 1-0 Portland
- 1-1
- 0-1
- 0-0 as the main contrary branch

The underlying pregame view is therefore:

`EARLY GOAL MORE LIKELY THAN SCORELESS HALF + GOTHAM TERRITORIAL/CORNER EDGE + FULL-GAME TOTAL NEAR THE 2–3 GOAL BOUNDARY + GOTHAM SLIGHT WINNER EDGE`

---

# Administrative note

Google Drive was used strictly as a **read-only framework source**.

The active Drive snapshot has not been advanced by the recent locally delivered conversation cards. This file is labelled **P-146 conversation-local continuation** to avoid reusing IDs in this conversation.

It is not claimed to be the canonical Drive ID until formally reconciled.

---

# 1. Record metadata

| Field | Value |
|---|---|
| Sport | Soccer |
| Competition | NWSL |
| Event | Gotham FC vs Portland Thorns FC |
| Venue | Sports Illustrated Stadium, Harrison, New Jersey |
| Scheduled kickoff | 2026-08-28 20:00 America/New_York |
| Melbourne equivalent | 2026-08-29 10:00 Australia/Melbourne |
| Final research refresh | 2026-08-29 09:45 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Match endpoint for winner | `90 MINUTES + STOPPAGE / REGULATION` |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_SOCCER.md` effective 2026-08-29 |
| Numerical state | `NTS-2026.08.25-v0.2 — DESIGN ONLY / NO FITTED SOCCER MODEL` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# 2. Exact candidate slate

The user supplied:

1. First-half goals Over/Under 0.5
2. Full-match goals Over/Under 2.5

A fifth requested selection was added from the corner process:

5. **Gotham FC team corners Over 4.5**

## Corner settlement definition

Because the user did not specify a sportsbook/provider:

- research target = **official NWSL match-stat corner kicks credited to Gotham FC in regulation**
- threshold = **Over 4.5**
- extra time = not applicable in this regular-season fixture
- bookmaker-specific definition = `UNKNOWN_DEFINITION`

The corner row therefore cannot be upgraded beyond `FORCED RANK / MEDIUM-LOW`.

---

# 3. Updated framework controls applied

The current soccer framework requires:

1. official competition, venue and regulation endpoint;
2. confirmed XI, goalkeeper, formation, bench and material absences where available;
3. dynamic attack/defence and current-role reconciliation;
4. goals derived from a separate goal process;
5. corners derived from their own exposure/rate/width/cross/clearance/score-state process;
6. no use of dominance, possession or xG alone as a corner proxy;
7. leading/trailing score-state branches;
8. current lineup/regime evidence reconciled against broad H2H;
9. unresolved participant fields to lower confidence;
10. exact provider/definition frozen for derivative markets where possible.

Gotham's starting XI is officially released.

Portland's final starting XI was **not recovered from a field-owning Portland/NWSL release** at the final research cutoff, despite current availability and likely-role information being available.

That unresolved Portland XI state caps participant-sensitive rows.

---

# 4. Official/current event identity

Official Gotham and Portland schedules list:

- Gotham FC vs Portland Thorns
- Friday, August 28, 2026
- 8:00 PM ET
- Sports Illustrated Stadium
- Prime Video

Current league position before kickoff:

## Gotham
- 13-3-5
- 44 points
- 1st
- +13 goal difference
- 26 scored
- 13 conceded

## Portland
- 11-6-4
- 37 points
- 3rd
- +6 goal difference
- 35 scored
- 29 conceded

Gotham enter unbeaten in nine consecutive league matches.

Portland enter on a three-match winning streak.

---

# 5. Gotham confirmed XI / current role regime

Gotham officially confirmed:

**GK**
- Ann-Katrin Berger

**Back line**
- Midge Purce
- Jess Carter
- Tierna Davidson
- Mandy Freeman

**Midfield**
- Jaelin Howell
- Jaedyn Shaw
- Savannah McCaskill

**Front line**
- Jordynn Dudley
- Sam Kerr
- Guro Reiten

Key current changes:

- Rose Lavelle is unavailable with a head injury.
- Emily Sonnett is on the season-ending injury list.
- Sofia Cook is out.
- Denise O'Sullivan is available again from the bench.
- Reiten moves from the left-back role into the left wing.
- Shaw shifts into midfield.

### Goal-process implication

Lavelle's absence removes an important progressive/creative midfielder.

However, moving **Reiten higher** increases:
- wide receiving;
- crossing;
- final-third combinations;
- direct chance creation.

The front three of:
- Dudley
- Kerr
- Reiten

is still a high-quality scoring unit.

Kerr has scored 10 goals in 17 career matches against Portland across all competitions.

That H2H fact is contextual only; it is not used as a fitted striker coefficient.

---

# 6. Portland current regime

Portland enter with one of the stronger attacks in the NWSL.

Official NWSL Week 19 notes describe this as:

**the league's No. 3 offense, led by Sophia Wilson and Pietra Tordin, against the league's best defense.**

Season:
- 35 goals in 21 matches
- 1.67 goals per match descriptively
- 29 conceded

Portland's latest results:

- 1-0 vs Denver
- 2-1 vs Orlando
- 4-3 at Boston
- 1-5 at Utah
- 2-2 vs Gotham

The last five show a wide scoring distribution:
- low-output 1-0;
- competitive 2-1;
- high-variance 4-3 / 5-1;
- direct 2-2 H2H.

## Availability

Current availability reporting indicates:

Returns/available:
- Reilyn Turner
- Morgan Weaver
- Marie Müller

Unavailable:
- Bella Bixby
- Julie Dufour
- Olivia Moultrie
- Isabelle Obaze

International duty:
- Valerin Loboa

The biggest attack-process loss is **Olivia Moultrie**, who is on the season-ending injury list.

That reduces Portland's central creative/shot-generation ceiling compared with the July H2H.

Because Portland's final official XI was unresolved at the cutoff, exact current minutes/roles remain a mixture.

---

# 7. Gotham defensive process

Gotham have allowed:

- **13 goals in 21 league matches**
- only **0.62 goals per match**
- **13 clean sheets**
- 7 home clean sheets in 11 current home matches

Ann-Katrin Berger has recorded 10 individual clean sheets and is seeking another club single-season record.

This is the strongest **Under 2.5** mechanism.

Gotham's current recent league results:

- 0-0 at Angel City
- 2-1 vs Kansas City
- 1-0 vs San Diego
- 1-0 at Houston
- 1-0 at Bay FC

Only one of those five exceeded 2.5 goals.

This current run is not treated as a mechanical "Under streak."

The mechanism behind it is:
- low opponent shot quality;
- strong central defending;
- Berger;
- controlled score-state play after leading.

---

# 8. Portland away regime

Portland's away record is materially weaker than its home form:

- 4 wins
- 1 draw
- 6 losses
- 16 goals scored
- 24 conceded

That is approximately **3.64 total goals per away match descriptively**.

Portland away matches have therefore been much more open than Gotham's home environment.

This is one of the strongest **Over 2.5** mechanisms.

The current mixture is:

### Gotham-home suppression branch
- Portland held to 0–1
- Gotham scores 1–2

### Portland-away openness branch
- Portland scores 1+
- Gotham exploits Portland's defensive transitions for 2+

The second branch produces a large 2-1 / 2-2 / 3-1 family.

---

# 9. First-half goal process

## Gotham

Current 2026 league data:

- **18 first-half goals in 21 matches**
- scored in the first half in roughly **62%**
- 10 halftime leads
- by mid-August, Gotham had the second-most first-half goals in the league behind Portland

Gotham's latest meaningful first-half examples include:

- vs Kansas City: Purce 13', Kerr 41' after conceding early
- vs San Diego: Shaw 44'
- at Bay FC: Purce 2'
- at Portland: Purce 2'

Gotham have repeatedly created useful first-half scoring exposure rather than relying only on late goals.

## Portland

A broader five-season NWSL profile has produced a first-half goal in roughly 75% of Portland matches.

That longer window is only a prior.

More importantly, Portland's 2026 attacking profile has been among the strongest in the league.

The July meeting between these clubs was already:

- Gotham goal — 2'
- Portland goal — 21'

Halftime:
**1-1**

### Current first-half reconciliation

The main Under-0.5 mechanism is:
- Gotham's defensive quality;
- Portland missing Moultrie;
- high-level opponents beginning cautiously.

The stronger Over-0.5 mechanism is:
- Gotham's early scoring history;
- Reiten now operating higher;
- Kerr/Dudley attack;
- Portland's Wilson/Tordin attack;
- both teams have demonstrated early-goal routes against each other.

Therefore:

**First Half Over 0.5 ranks first.**

---

# 10. Full-match total process

## Over 2.5 mechanisms

- Portland averages 1.67 goals scored.
- Portland away matches have been high-event.
- Portland have scored seven goals across their last three wins.
- Gotham have an upgraded direct attacking shape with Reiten at LW.
- Portland have conceded 24 goals in 11 away league matches.
- the July H2H finished 2-2.
- an early goal forces a stronger chasing/counterattack branch.

Representative:
- Gotham 2-1
- 2-2
- Gotham 3-1
- Portland 2-1

## Under 2.5 mechanisms

- Gotham have conceded only 13 in 21.
- Gotham have 13 clean sheets.
- only one of Gotham's most recent five league matches exceeded 2.5.
- Portland are missing Moultrie.
- Gotham can protect 1-0 / 2-0 states effectively.
- Berger is elite current goalkeeper opposition.

Representative:
- Gotham 1-0
- Gotham 2-0
- 1-1
- Portland 1-0

## Direction

The total is **close**.

The reason Over receives the higher ordinal rank is:
- Portland's away defensive vulnerability;
- Portland's own scoring ceiling;
- current Gotham attacking front;
- score-state acceleration if either team scores early.

The Under remains a substantial ordinary branch because Gotham's defense is the best unit in the match.

---

# 11. Corner process

## Target

**Gotham FC team corners Over 4.5**

## Direct exposure evidence

Gotham available 2026 corner sample:
- approximately **4.0 corners for per match**
- approximately **3.1 conceded**

Portland:
- approximately **3.9 corners for**
- approximately **5.7 corners conceded**

NWSL league:
- approximately **9.26 total corners per match**

## H2H

July 24:
- Portland 3 corners
- Gotham **8 corners**

Gotham had:
- 63.1% possession;
- 8 corners;
- significant pressure even while Portland created more raw shots.

The corner conclusion does **not** come from possession.

The more relevant mechanisms are:

### Gotham width
Current XI includes:
- Purce
- Reiten moved to wing
- Dudley
- Kerr

This creates:
- wide isolation;
- crosses;
- end-line entries;
- blocked crosses;
- defensive clearances.

### Portland conceded-corner tendency
Portland concede substantially more corners than they win on average.

### Score state

If Gotham trail or remain level:
- wide attack/corner demand remains high.

If Gotham score early:
- corner demand can fall as possession becomes more controlled.

This leading-state branch prevents a stronger confidence grade.

## Missingness

Unavailable at cutoff:
- official Portland final XI;
- complete event-level cross/block/end-line dataset;
- user's sportsbook/provider definition.

Therefore this row must remain:

`FORCED RANK / MEDIUM-LOW`

---

# 12. Weather

National Weather Service Harrison forecast for Friday night:

- around upper-60s°F / high-teens°C
- mostly cloudy
- only a low residual shower chance near the start
- light north/northwest wind

There is no strong persistent wind or severe rain mechanism at the scheduled 8 PM kickoff.

Weather receives minimal directional weight.

---

# 13. Joint scenario tree

## Branch A — Gotham early lead, controlled win

Representative:
- HT Gotham 1-0
- FT Gotham 2-0

Mechanism:
- Gotham press/width creates early chance;
- defense suppresses Wilson/Tordin;
- Portland chases without clean finishing.

Results:
- 1H Over 0.5 — WIN
- FT Under 2.5 — WIN
- Gotham winner — WIN
- Gotham corner Over 4.5 remains live but early lead can reduce late demand

---

## Branch B — open competitive match

Representative:
- HT 1-1
- FT Gotham 2-1

Mechanism:
- both attacks break through;
- Portland's away transition defense leaks;
- Gotham still owns home/defensive edge.

Results:
- 1H Over 0.5 — WIN
- FT Over 2.5 — WIN
- Gotham winner — WIN
- Gotham corners likely supported by sustained attacking width

This is the strongest Over branch.

---

## Branch C — scoreless first half / late Gotham goal

Representative:
- HT 0-0
- FT Gotham 1-0

Mechanism:
- Portland protects central areas;
- Gotham's first-half attacks do not convert;
- Berger/Gotham defense controls Portland.

Results:
- 1H Under 0.5 — WIN
- FT Under 2.5 — WIN

This is the strongest failure path for Rank #1.

---

## Branch D — Portland scores first

Representative:
- HT Portland 1-0
- FT 1-1 or Gotham 2-1

Mechanism:
- Wilson/Tordin exploit transition;
- Gotham increases width and pressure.

Effects:
- 1H Over 0.5 — WIN
- Gotham corner Over 4.5 becomes stronger
- full-game Over becomes more likely due to chase state

---

## Branch E — Portland away-defense failure

Representative:
- Gotham 3-1
- Gotham 3-0

Mechanism:
- Gotham's Reiten/Kerr/Dudley shape repeatedly reaches dangerous areas;
- Portland's away defensive weakness persists.

Effects:
- FT Over 2.5 — WIN
- Gotham winner — WIN
- corner direction depends on goal timing; early efficiency can suppress total corners

---

# 14. Ranking rationale

## #1 — First Half Over 0.5 Goals

Strongest supplied market.

Support:
- Gotham scored 18 first-half goals in 21 league matches.
- Gotham first-half scoring rate around 62%.
- Portland have one of the league's strongest attacks.
- last H2H had goals at 2' and 21'.
- current Gotham front line remains dangerous despite Lavelle's absence.
- Reiten moves higher.

Kill path:
- Portland defend compactly;
- Gotham create but fail to finish;
- game reaches HT 0-0 like Portland-Orlando recently.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Gotham Team Corners Over 4.5

Direct corner mechanism is better than a generic total-corner guess.

Support:
- Gotham ~4.0 for.
- Portland ~5.7 conceded.
- Gotham won 8 corners in the July H2H.
- current Gotham width is strong.
- Portland trailing/draw states can force clearances and blocked crosses.

Kill path:
- Gotham score efficiently early and reduce wide attacking demand;
- Portland final XI improves wide defending;
- Gotham chance creation comes through central combinations rather than corner-causing attacks.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

**Settlement:** `UNKNOWN_DEFINITION` for user's sportsbook; research target is official NWSL team corner kicks.

---

## #3 — Full Match Over 2.5 Goals

Support:
- Portland have 35 goals and are the league's No. 3 attack.
- Portland away games are high-event.
- Portland have conceded 24 away goals.
- July meeting ended 2-2.
- Gotham attack includes Kerr/Reiten/Dudley.
- early-goal branch increases transition/chasing exposure.

Counterweight:
- Gotham's league-best defense;
- 13 clean sheets;
- Portland missing Moultrie.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Full Match Under 2.5 Goals

This remains close to Rank #3.

Support:
- Gotham allow 0.62 goals per game.
- 13 clean sheets.
- current recent Gotham scorelines are heavily low-total.
- Portland Moultrie absence.
- 1-0 / 2-0 are highly coherent Gotham-win states.

Why below Over:
- Portland's away defensive vulnerability makes Gotham 2+ plausible;
- Portland's own attack is too strong to suppress to zero with high confidence;
- an early goal can change the match regime.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #5 — First Half Under 0.5 Goals

The scoreless-half branch exists.

However it loses to **any** goal in the opening 45+ minutes.

Given:
- Gotham's first-half scoring record;
- Portland's attack;
- last H2H 1-1 at halftime;
- current attacking roles;

it is the least robust of the five candidate contracts.

**Verdict:** `AVOID / FORCED RANK — MEDIUM-LOW`

`AVOID` here means lowest-ranked among this frozen candidate slate, not negative expected value.

---

# 15. Potential game winner

## Gotham FC — `FORCED WINNER / MEDIUM-LOW CONFIDENCE`

Endpoint:
**regulation 90 minutes plus stoppage time**

Support:
- 1st in NWSL
- 13-3-5
- nine-match unbeaten run
- 13 clean sheets
- 7-3-1 home record
- Portland only 4-1-6 away
- Portland have conceded 24 away goals
- Gotham confirmed strong front three
- Berger/defense is the best current unit

Why not stronger:
- Portland are on a three-match winning streak;
- Portland are the league's No. 3 attack;
- Sophia Wilson/Pietra Tordin create a real transition/scoring threat;
- Portland final official XI was not verified at cutoff;
- Gotham are missing Lavelle and Sonnett.

Central winner branch:
**Gotham 2-1 / 2-0**

Main failure:
**Portland attack converts first and forces Gotham into a more open game, producing 1-1 or Portland 2-1.**

---

# 16. Final card

1. **1st Half Over 0.5 Goals**
2. **Gotham FC Team Corners Over 4.5**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential regulation winner:** **Gotham FC**

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

# 17. Source record

## Google Drive framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official league/team
- Gotham official schedule
- Portland official schedule
- Gotham official match preview
- Gotham official starting XI
- Gotham official recent match recaps
- Portland official recent match recaps
- NWSL Week 19 pitch notes
- Portland current availability/resource page

## Supporting process data
- FootyStats 2026 Gotham/Portland team statistics
- GoalLineExpert Gotham corner sample
- APWin Portland corner sample
- FirstHalfScore first-half historical profiles

## Weather
- National Weather Service Harrison, NJ

---

# 18. Limitations

- Portland's final field-owning starting XI was not recovered before cutoff.
- Corner provider/bookmaker definition was not supplied.
- Complete current cross/block/end-line/clearance event data were not available.
- Corner statistics came from specialist secondary databases plus official H2H match stats.
- Current goal directions remain qualitative; no fitted/validated soccer model exists.
- Exact sportsbook settlement wording was not supplied.

---

# 19. Logging confirmation

**Conversation-local ID:** `P-146`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Forecast state:** `PREGAME`


# P-147 (conversation-local continuation) — Toluca Femenil vs León Femenil — Liga MX Femenil Apertura 2026

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Toluca Team Corners Over 4.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Full Match Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Full Match Under 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **5** | **1st Half Under 0.5 Goals** | `AVOID / FORCED RANK` | `MEDIUM-LOW` |

**Potential regulation winner:** **Toluca Femenil — FORCED WINNER / MEDIUM-LOW CONFIDENCE**

### Central score family
- Toluca 2-1
- Toluca 2-0
- 1-1
- León 2-1

### Central first-half family
- 1-0 Toluca
- 0-1 León
- 1-1
- 0-0 as the principal contrary branch

The central pregame state is:

`FIRST-HALF GOAL SLIGHTLY FAVORED + TOLUCA CORNER PRESSURE + FULL-GAME TOTAL NEAR THE 2–3 GOAL BOUNDARY + TOLUCA SLIGHT WINNER EDGE`

---

# 1. Administrative note

Google Drive was used strictly as a **read-only framework source**.

The current canonical Drive snapshot still has not been advanced by the locally delivered conversation cards. This entry is therefore labelled **P-147 conversation-local continuation** to avoid ID reuse.

It is not claimed to be the Drive-canonical ID until formally reconciled.

---

# 2. Record metadata

| Field | Value |
|---|---|
| Sport | Soccer |
| Competition | Liga MX Femenil — Apertura 2026 |
| Round | Jornada 5 |
| Event | Toluca Femenil vs León Femenil |
| Venue | Estadio Nemesio Díez, Toluca |
| Official scheduled kickoff | Friday 28 Aug 2026, 18:00 Central Mexico time |
| Melbourne equivalent | Saturday 29 Aug 2026, 10:00 AEST |
| Winner endpoint | `90 MINUTES + STOPPAGE / REGULATION` |
| Final research refresh | `2026-08-29 09:49 Australia/Melbourne` |
| Forecast state | `PREGAME — approximately 11 minutes before official kickoff` |
| Method | `MDS-2026.08.29-v2.5` |
| Sport module | `RULES_SOCCER.md` effective 2026-08-29 |
| Numerical state | `NTS-2026.08.25-v0.2 — DESIGN ONLY / NO FITTED SOCCER MODEL` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive modified | `NO` |
| Retrospective | `NOT INCLUDED` |

---

# 3. Candidate slate

The user supplied:

- First Half Over 0.5 Goals
- First Half Under 0.5 Goals
- Full Match Over 2.5 Goals
- Full Match Under 2.5 Goals

The fifth pick is:

- **Toluca Team Corners Over 4.5**

## Corner settlement target

Because no sportsbook/provider was supplied:

`Official competition match-stat team corner kicks credited to Toluca during regulation`

Bookmaker/provider-specific definition remains:

`UNKNOWN_DEFINITION`

That prevents a `LEAN` or `SUPPORTED` label under the active soccer framework.

---

# 4. Framework controls applied

The updated soccer module requires:

1. exact competition, venue, regulation endpoint and candidate slate;
2. starting XI, goalkeeper, formation, bench and material availability where recoverable;
3. goal creation separated from raw finishing outcomes;
4. corners modelled independently from goals/possession/class;
5. direct corner exposure using team corners for, opponent conceded, width/cross/block/end-line/clearance/set-piece mechanisms and score state;
6. old H2H treated as weak unless current role/system continuity is meaningful;
7. current lineup/competition evidence to outrank inherited reputation after reconciliation;
8. weather used only through a tactical/technical mechanism;
9. missing official XI/provider layers to cap confidence;
10. one coherent regulation goal tree for 1X2, first-half and full-match totals.

A current official Toluca XI and current official León XI were **not recovered from field-owning club/league sources** before the research cutoff.

Secondary probable lineups exist, but they are not promoted to confirmed status.

Therefore the entire participant-sensitive card is capped at:

`FORCED RANK / MEDIUM-LOW`

---

# 5. Current Apertura 2026 team state

## Toluca

Current league record:
- 3 wins
- 1 draw
- 0 losses
- 10 points
- approximately +6 goal difference

Results:
- Atlético San Luis 1-4 Toluca
- Toluca 2-0 Juárez
- Toluca 1-1 Atlas
- Atlante 1-2 Toluca

Goals:
- 9 scored
- 3 conceded

Toluca are unbeaten through four league matches.

Their official coach Alberto Toril said after the Atlante win that the team remains near the top and specifically noted that León are **very dangerous away**, having scored eight goals in two away matches, but that Toluca intend to impose their home conditions.

This is high-value current-event tactical context because it identifies the same opponent/venue state rather than generic motivation.

---

## León

Current results:
- Pumas 2-5 León
- León 1-2 Tigres
- León 0-1 Querétaro
- Monterrey 2-3 León

Record:
- 2 wins
- 2 losses

Goals:
- 9 scored
- 7 conceded

### Away regime

León's two away matches:
- won 5-2 at Pumas
- won 3-2 at Monterrey

That is:
- **8 away goals**
- 4 conceded
- both matches Over 2.5
- both matches containing first-half goals

This is the strongest current Over / León-scoring mechanism.

The sample is only two matches, so it remains a regime branch rather than a stable coefficient.

---

# 6. Current likely participant structure — secondary only

## Toluca probable core

Current secondary pregame reporting expects a structure around:

- Valeria Martínez — GK
- Yaneisy Rodríguez
- Karla Martínez
- Liliana Fernández
- Victoria López
- Faustine Robert
- Amandine Henry
- Yamile Franco
- Eugénie Le Sommer
- Sonia Vázquez
- Deneisha Blackwood

### Decision-driving roles

- Blackwood provides width and set-piece delivery.
- Amandine Henry adds box arrival/aerial set-piece threat.
- Le Sommer supplies penalty-box movement and finishing.
- Faustine Robert contributes midfield progression/attacking support.

These roles are consistent with recent Toluca match evidence.

But because the actual XI was not field-owner confirmed, minutes and exact formation remain a mixture.

---

## León probable core

Current secondary reporting expects a structure around:

- Natalia Acuña — GK
- Daniela Arias
- Valeria Razo
- Fernanda Pinilla
- Selene Cortés
- Marissa García
- Solange Ramos
- Vianey Alemán
- Nayeli Bolaños
- Kristal Soto
- Mayalu Rausch

León's direct scoring threats are particularly important because their away attack has already produced eight goals.

Again:

`SECONDARY PROBABLE LINEUP — NOT CONFIRMED_OFFICIAL`

---

# 7. First-half goal process

## Toluca first halves in Apertura 2026

### at Atlético San Luis
HT: 0-1 from Toluca's perspective / San Luis led 1-0

First-half goal:
**YES**

### vs Juárez
HT: 0-0

First-half goal:
**NO**

### vs Atlas
HT: Toluca 0-1 Atlas

First-half goal:
**YES**

### at Atlante
HT: 0-0

First-half goal:
**NO**

Toluca:
- first-half goal in match: **2 of 4**

This alone is not enough for a strong direction.

---

## León first halves in Apertura 2026

### at Pumas
HT: Pumas 2-3 León

First-half goal:
**YES**

### vs Tigres
HT: León 1-0 Tigres

First-half goal:
**YES**

### vs Querétaro
HT: 0-0

First-half goal:
**NO**

### at Monterrey
HT: 1-1

First-half goal:
**YES**

León:
- first-half goal in match: **3 of 4**

Combined current-event descriptive sample:
- 5 of the clubs' 8 league matches contained a first-half goal.

This is diagnostic only, not a calibrated probability.

---

# 8. Why First Half Over 0.5 ranks first

The direct mechanisms are:

1. León's away attack has been extremely aggressive/productive.
2. Both León away matches already produced first-half goals.
3. Toluca have conceded a first-half goal in two of four league matches.
4. León's attacking approach forces Toluca to defend transition and wide entries.
5. Toluca possess enough individual quality to score first themselves.

The latest H2H also produced an extreme first half:

**León 3-0 Toluca at halftime** in March/April 2026.

That old game is heavily downweighted because:
- different tournament;
- coaching/role changes;
- venue reversal.

It is supporting context, not the primary mechanism.

### Main failure path

Toluca's recent controlled home style and León's willingness to protect space produce:
- cautious opening;
- few clean box entries;
- 0-0 HT.

The fact Toluca's last away game at Atlante and home Juárez game both reached halftime 0-0 preserves this branch.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 9. Full-match goal process

## Toluca totals

- 4-1 → 5 goals
- 2-0 → 2
- 1-1 → 2
- 2-1 → 3

Over 2.5:
- 2 of 4

Under 2.5:
- 2 of 4

Toluca therefore do not supply a strong raw total direction by themselves.

---

## León totals

- 5-2 → 7
- 1-2 → 3
- 0-1 → 1
- 3-2 → 5

Over 2.5:
- 3 of 4

Under:
- 1 of 4

The more important mechanism is the away split:
- 7 total goals at Pumas
- 5 at Monterrey

León's away matches have been highly transitional and finishing-rich.

---

# 10. Full Match Over 2.5 — why it ranks above Under

### Over mechanisms

- León have scored eight goals in two away games.
- Toluca coach explicitly identifies León as dangerous away.
- Toluca have scored in all four Apertura matches.
- León have conceded in three of four.
- Toluca's Le Sommer / Blackwood / Henry core provides multiple goal routes.
- León's Soto / Rausch / García-type attacking structure gives a credible away goal.
- an early first-half goal creates a stronger chase/transition branch.
- the most recent H2H finished 3-3.

Representative scores:
- Toluca 2-1
- León 2-1
- 2-2
- Toluca 3-1

### Counterweight

Toluca have conceded only three goals through four league matches and have already recorded a 2-0 home win.

León also lost 0-1 to Querétaro.

So:
- Toluca 1-0
- Toluca 2-0
- 1-1

remain important ordinary states.

**Direction:** Over 2.5 narrowly above Under.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

# 11. Corner process — Toluca Team Corners Over 4.5

This is the selected fifth market.

## Toluca current Apertura corner production

Verified current-match corner counts:

### at Atlético San Luis
Toluca: **5**

### vs Juárez
Toluca: **4**

### vs Atlas
Toluca: **4**

### at Atlante
Toluca: **9**

Current four-match total:
- 22 Toluca corners

Descriptive mean:
- **5.5 per match**

This is not used as a fitted rate.

---

## León current corners conceded

### at Pumas
Pumas: **10**

### vs Tigres
Tigres: **7**

### vs Querétaro
Querétaro: **3**

### at Monterrey
Monterrey: **6**

León have therefore conceded:
- **26 corners in four matches**

descriptive mean:
- **6.5 per match**

Again, this is not a calibrated Poisson input.

---

## Direct corner mechanism

Toluca's attack contains:

- Blackwood width;
- Le Sommer box occupation;
- overlaps / end-line access;
- set-piece emphasis;
- Henry as an aerial target.

The previous Atlante match is especially useful because:
- Toluca won **9 corners**;
- the winning action came from a late Blackwood corner delivery finished by Amandine Henry according to Toluca's official report.

The mechanism is therefore:

`width + sustained pressure + blocked/cleared service + established set-piece threat -> repeated Toluca corner exposure`

not:
`Toluca are better, therefore more corners`.

---

## Score-state branches

### Match level / Toluca trailing
Toluca's corner demand should rise:
- more wide attacks;
- more defensive clearances;
- more late set-piece pressure.

### Toluca leading early
Corner demand can fall:
- more control;
- less need to attack end line;
- León carry more territorial initiative.

This is the strongest kill path for Over 4.5.

### Missing layers

Not fully available at cutoff:
- confirmed official León XI;
- full current cross/block/end-line event feed;
- user's bookmaker/provider corner definition.

Therefore:

`FORCED RANK — MEDIUM-LOW`

No `LEAN` upgrade is permitted.

---

# 12. Weather / surface branch

Toluca-area forecasts around 18:00 indicate:

- cool conditions around mid-teens °C;
- high rain/shower probability;
- relatively light wind.

Mexico's national weather service also forecasts strong afternoon/evening rain potential across parts of the State of Mexico.

### Mechanistic effects

Possible goal suppression:
- slower clean combination play;
- poorer footing;
- wet-ball handling.

Possible goal/corner enhancement:
- defensive slips;
- goalkeeper spills;
- blocked crosses;
- rushed clearances;
- set-piece volume.

Because wind is not the primary issue, the weather is treated as a **variance modifier**, not an automatic Under.

It modestly supports the corner-event tail more than a clear total direction.

---

# 13. H2H reconciliation

Latest meeting:
- León 3-3 Toluca
- halftime León 3-0
- corners León 7, Toluca 9

Previous:
- Toluca 1-0 León
- HT 0-0
- corners Toluca 6, León 3

Longer H2H:
- Toluca have historically held the overall win edge;
- many older matches were low-scoring.

The active framework requires current competition/lineup regime to outrank inherited H2H after reconciliation.

Therefore:
- the latest 3-3 supports the high-event branch;
- the prior 1-0 supports the low-total branch;
- neither controls the forecast.

---

# 14. Potential regulation winner — Toluca

## Why Toluca

- unbeaten 3-1-0 start;
- 10 points from four;
- 9 goals scored, only 3 conceded;
- home venue;
- stronger current defensive consistency;
- experienced attacking core;
- current coach explicitly intends to impose home conditions.

## Why confidence is limited

León are a dangerous away side:
- 5-2 at Pumas
- 3-2 at Monterrey

They have shown:
- transition scoring;
- ability to win in difficult away venues;
- multiple goals against strong opposition.

### Winner central branch
**Toluca 2-1**

### Secondary branch
**Toluca 2-0**

### Main failure
León's away attack converts early and Toluca are forced into a chase:
- 1-1
- 2-2
- León 2-1

**Verdict:** `FORCED WINNER / MEDIUM-LOW`

Endpoint:
`REGULATION 90 MINUTES + STOPPAGE`

---

# 15. Joint scenario tree

## Branch A — Toluca early goal / home control

HT:
- Toluca 1-0

FT:
- Toluca 2-0
- Toluca 2-1

Effects:
- 1H Over 0.5 WIN
- Toluca winner favored
- FT total depends on León response
- Toluca corner Over remains live but can be suppressed by early lead

---

## Branch B — León scores first

HT:
- León 1-0
- or 1-1

FT:
- 1-1
- Toluca 2-1
- 2-2

Mechanism:
- León away transition succeeds;
- Toluca increase territory/width;
- corner pressure rises.

Effects:
- 1H Over 0.5 WIN
- Toluca corners Over 4.5 strengthened
- FT Over 2.5 strengthened

---

## Branch C — cagey first half

HT:
- 0-0

FT:
- Toluca 1-0
- Toluca 2-0
- 1-1

Mechanism:
- wet conditions / compact midfields;
- Toluca avoid transition exposure;
- León unable to reproduce away finishing.

Effects:
- 1H Under 0.5 WIN
- FT Under 2.5 favored

This is the main contrary branch.

---

## Branch D — high-event León away regime continues

HT:
- 1-1

FT:
- Toluca 2-1
- León 2-1
- 2-2
- Toluca 3-1

Effects:
- 1H Over WIN
- FT Over WIN
- corners supported by chase state

This is the strongest joint Over branch.

---

# 16. Final ranking rationale

## #1 — First Half Over 0.5 Goals

Strongest goal threshold because it needs only one goal.

Support:
- León first-half goal event in 3/4 league matches;
- both León away matches had first-half scoring;
- Toluca first halves are not uniformly closed;
- current attacking personnel;
- last H2H was 3-0 at halftime.

Failure:
- 0-0 control branch similar to Toluca-Juárez / Atlante-Toluca.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Toluca Team Corners Over 4.5

Support:
- Toluca current corner sequence 5, 4, 4, 9;
- León conceded 10, 7, 3, 6;
- current set-piece/width mechanism;
- Blackwood delivery + Henry aerial target;
- trailing/draw state can increase Toluca width.

Failure:
- early Toluca lead reduces attacking need;
- provider/definition unknown;
- exact XI unresolved.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Full Match Over 2.5 Goals

Support:
- León Over in 3/4 league matches;
- both León away matches high-event;
- Toluca have scored in all four;
- León away scoring is explicitly recognized by Toluca's coach;
- early-goal branch opens transition space.

Failure:
- Toluca's strong defensive start;
- León 0-1 Querétaro result;
- rain/compact state.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Full Match Under 2.5 Goals

Support:
- Toluca have conceded only 3 through 4;
- two Toluca matches stayed at 2 total goals;
- 1-0 / 2-0 / 1-1 all ordinary states;
- older H2H contains several low totals.

Why below Over:
- current León away regime is materially more aggressive;
- Toluca score consistently;
- a 2-1 central result crosses the threshold.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #5 — First Half Under 0.5 Goals

It wins only on a complete scoreless first half.

That branch is real, but it loses to any:
- Toluca early home goal;
- León transition goal;
- set-piece conversion.

Given León's first-half and away scoring profile, it is the least robust of the five.

**Verdict:** `AVOID / FORCED RANK — MEDIUM-LOW`

`AVOID` means lowest-ranked in the supplied/frozen candidate set, not negative expected value.

---

# 17. Final card

1. **1st Half Over 0.5 Goals**
2. **Toluca Team Corners Over 4.5**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential regulation winner:** **Toluca Femenil**

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

# 18. Source record

## Google Drive framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- `PREDICTION_LOG_COMBINED.md`
- current `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official / field-owning evidence
- Deportivo Toluca official women's schedule
- Deportivo Toluca official Atlético San Luis match stats
- Deportivo Toluca official Atlante post-match report
- Deportivo Toluca coach comments before León
- Toluca official previous León 3-3 match centre
- Mexico National Meteorological Service regional forecast

## Supporting current data
- FotMob current Apertura results
- TotalCorner current Liga MX Femenil corner results
- 365Scores / Scores24 recent match-stat cross-checks
- current secondary pregame lineup reporting

---

# 19. Limitations

- confirmed official starting XIs were not recovered at the research cutoff;
- León official team availability detail is limited;
- exact sportsbook corner provider/definition was not supplied;
- corner cross/block/end-line event detail is incomplete;
- rainfall timing at the stadium is uncertain;
- no fitted/validated soccer numerical model exists.

---

# 20. Logging confirmation

**Conversation-local ID:** `P-147`  
**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`  
**Forecast disposition:** `PREGAME — final refreshed approximately 11 minutes before official kickoff`


# P-148 (conversation-local continuation) — Colorado Rapids 2 vs Ventura County FC — MLS NEXT Pro

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Ventura County FC Team Corners Over 3.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Full Match Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Full Match Under 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **5** | **1st Half Under 0.5 Goals** | `AVOID / FORCED RANK` | `MEDIUM-LOW` |

**Potential regulation winner:** **Ventura County FC — FORCED WINNER / MEDIUM-LOW CONFIDENCE**

### Central regulation score family
- Ventura County FC 2-1
- Ventura County FC 2-0
- 1-1
- 2-2
- Colorado Rapids 2 2-1 as the main home-upset branch

### Central first-half family
- Colorado 0-1 Ventura
- 1-1
- Colorado 1-0
- 0-0 as the main contrary branch

---

## Administrative / framework status

Google Drive was used strictly as a **read-only framework source**.

This is labelled **P-148 conversation-local continuation** so local cards in this chat are not assigned duplicate IDs while the Drive canonical queue remains unreconciled.

**Method:** `MDS-2026.08.29-v2.5`  
**Soccer module:** `RULES_SOCCER.md` effective 2026-08-29  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`

---

# 1. Event identity

- **Competition:** MLS NEXT Pro
- **Match:** Colorado Rapids 2 vs Ventura County FC
- **Venue:** DICK'S Sporting Goods Park, Commerce City, Colorado
- **Scheduled kickoff:** Friday Aug. 28, 2026, 6:00 PM MT
- **Melbourne equivalent:** Saturday Aug. 29, 2026, 10:00 AM AEST
- **Winner endpoint:** regulation 90 minutes + stoppage time only

MLS NEXT Pro regular-season tied matches may proceed to a shootout for an additional standings point. The “potential winner” in this card is therefore explicitly the **regulation winner**, not the eventual shootout winner.

---

# 2. Participant gate

## Colorado — confirmed official XI

- Zack Campagnolo
- Kamal Sawadogo
- Charlie Harper
- Grant Gilmore
- Edgar Heredia
- Sebastian Siegler
- Luis García
- Josh Copeland
- Chris Aquino
- Ali Fadal (C)
- Sydney Wathuta

Substitutes:
- Dashiel Williams
- Kai Thomas
- Hamdoin Altayeb
- Kellen Lowery
- Jackson Pomeroy
- Jordan Camacho
- Niccolo Del Carmen

This keeps three scorers from Colorado's 4-1 win over Real Monarchs — Wathuta, Copeland and Aquino — in the starting group.

## Ventura — unresolved official XI

A final field-owner Ventura XI was not recovered at the cutoff.

Recent Ventura lineups have included Sebastian Conlon, Dalgado, Martinez, McLean/Hernandez, Vicente Garcia, Gabriel Arnold, Luis Müller, Eric Preston, Jeremi Djieze and Julian Placias, but these are **not promoted to tonight's confirmed XI**.

Because this is a development/reserve competition with meaningful rotation, the unresolved Ventura XI caps all participant-sensitive rows at:

`FORCED RANK / MEDIUM-LOW`

---

# 3. Current team regime

## Colorado Rapids 2

Current record:
- **3-14-7**
- 18 points
- 14th in the Western Conference
- approximately **24 GF / 45 GA** in the freshest table snapshot

Recent five:
- L 1-2 Tacoma
- L 0-3 LAFC2
- D 0-0 St. Louis CITY2
- D 2-2 Sporting KC II
- W 4-1 Real Monarchs

The 4-1 win was a genuine attacking improvement:
- Chris Aquino 43'
- Josh Copeland 52'
- Jonny De La Fuente 67'
- Sydney Wathuta 90+4'

Colorado produced 17 shots and eight shots on target in that game.

The framework does not automatically treat one 4-1 result as a regime reset. It creates a stronger home-attack branch than the season baseline, especially because Aquino/Copeland/Wathuta remain in the XI.

---

## Ventura County FC

Current record:
- **11-6-6**
- 42 points
- 4th West
- **47 GF / 30 GA**
- +17 goal difference

Recent five:
- 2-0 LAFC2
- 3-0 San Jose II
- 6-1 North Texas
- 2-0 Houston Dynamo 2
- 2-2 Portland Timbers2

That is approximately:
- **15 goals scored**
- **3 conceded**
- four wins and a draw

Ventura's current attack has multiple routes:
- Julian Placias
- Eric Preston
- Luis Müller
- Gabriel Arnold
- Vicente Garcia / wide and midfield progression branches

The current strength difference favors Ventura, but the unresolved XI and Colorado's home rebound prevent a strong side grade.

---

# 4. First-half goal process

The strongest supplied market is **1H Over 0.5**.

Relevant process evidence:

- Ventura's current attacking regime is substantially stronger than Colorado's season defensive baseline.
- Colorado have conceded 45 league goals and have repeatedly allowed first-half pressure.
- Ventura scored in the 45th minute against Portland in their latest match.
- In the first 2026 H2H, Julian Placias gave Ventura the lead in the **8th minute**.
- Colorado's current XI also has genuine early-scoring threats: Aquino scored at 43' last week, and Copeland/Wathuta remain active attacking pieces.

The direct previous H2H reached halftime:
**Ventura 1-0 Colorado**

and finished 1-1 before Colorado won the shootout.

### Main 0-0 first-half branch

- Ventura's away finishing cools;
- Colorado protects central areas at home;
- the heat/altitude encourages a less aggressive opening;
- Ventura's actual XI is more rotated than recent lineups.

This keeps the evidence at MEDIUM-LOW rather than a stronger label.

---

# 5. Full-match total process

## Over 2.5 branch

Ventura:
- 47 goals in 23 matches;
- 15 goals in the last five;
- 6-1 and multiple 2–3 goal outputs recently.

Colorado:
- just scored four against Real Monarchs;
- current XI retains the three main current scorers;
- season defense remains highly vulnerable.

Representative Over states:
- Ventura 2-1
- Ventura 3-1
- 2-2
- Colorado 2-1

The strongest Over mechanism is:

`Ventura pressure creates the first goal -> Colorado must chase -> transition space opens -> both teams have more attacking sequences`

## Under 2.5 branch

The Under cannot be dismissed:

- the first H2H finished **1-1**;
- Colorado recently had a 0-0 against St. Louis;
- Ventura have recent 2-0 wins that stay Under 2.5;
- a 1-0 / 2-0 Ventura control state is coherent.

Representative Under states:
- Ventura 2-0
- Ventura 1-0
- 1-1

I therefore rank Over only narrowly above Under.

---

# 6. Corner process — Ventura County FC team corners Over 3.5

This is the chosen fifth market.

## Direct exposure evidence

Season team-corner totals:
- Ventura: **106 corners in 23 matches** (~4.6 per match descriptively)
- Colorado: 107 corners in 24 matches

Latest Ventura match vs Portland:
- Ventura **5 corners**
- Portland 2

Current H2H in June:
- Ventura only **2 corners**
- Colorado 1

The low H2H count is retained as a real contrary state.

## Why Ventura Over 3.5 is preferred

The mechanism is not “Ventura are better, so they get corners.”

It is:

`Ventura stronger attack + Colorado weak defensive field-position baseline + wide attackers + blocked/cleared entries + Colorado chase/defend branches -> repeated corner exposure`

Colorado also recently conceded **7 corners to LAFC2** in a 3-0 loss, showing a high-corner defensive-pressure branch.

### Score-state dependence

If Ventura trail or remain level:
- corner demand should remain high.

If Ventura score early and control the match:
- later attacking/corner demand can fall.

That is the main kill path.

### Settlement limitation

The user did not specify a sportsbook/stat provider.

Research target:
`official MLS NEXT Pro regulation team corner kicks credited to Ventura County FC`

Exact bookmaker definition:
`UNKNOWN_DEFINITION`

Under the Drive's derivative-completeness rule, this market cannot receive `LEAN` or `SUPPORTED`.

---

# 7. Winner process

## Why Ventura County FC

Season/current advantages:
- 4th West vs 14th West;
- 47 GF vs ~24 Colorado;
- 30 GA vs ~45 Colorado;
- +17 GD vs approximately -21;
- four wins plus a draw in the last five;
- 15-3 scoring margin over that recent window.

Ventura are therefore the stronger regulation-winner branch.

## Why winner confidence is capped

- Colorado are at home.
- Colorado just won 4-1.
- Colorado's XI is officially known and keeps Aquino/Copeland/Wathuta.
- the first H2H was 1-1 after 90 minutes.
- Ventura's final official XI is unresolved.
- MLS NEXT Pro developmental rotations can materially change effective team strength.

So:
**Ventura regulation win is preferred, but draw and Colorado-upset branches remain material.**

---

# 8. Weather / altitude

DICK'S Sporting Goods Park is approximately **5,100 ft above sea level**.

Near 6 PM:
- temperature roughly **88°F**
- light/moderate wind around 9 mph
- small shower/thunderstorm probability

Mechanisms:
- heat + altitude can increase second-half fatigue and defensive-transition errors;
- possible showers can affect footing/ball speed;
- wind is not strong enough to create a major directional goal suppression assumption.

Weather is therefore a variance modifier, not an automatic Over or Under.

---

# 9. Joint scenario tree

## Branch A — Ventura early advantage
HT: Colorado 0-1 Ventura  
FT: Colorado 1-2 Ventura

Results:
- 1H Over 0.5 WIN
- FT Over 2.5 WIN
- Ventura winner WIN
- Ventura corner Over remains live

## Branch B — Ventura controls without shootout
HT: 0-1 or 0-0  
FT: 0-2

Results:
- FT Under 2.5 WIN
- Ventura winner WIN
- corner line depends on how early the lead arrives

## Branch C — repeat H2H-style close match
HT: 0-1 Ventura  
FT: 1-1

Results:
- 1H Over WIN
- FT Under WIN
- regulation winner = DRAW

## Branch D — open reserve-league match
HT: 1-1  
FT: 2-2 or Ventura 3-1

Results:
- 1H Over WIN
- FT Over WIN
- corner demand generally rises through chasing states

## Branch E — Colorado home upset
HT: Colorado 1-0  
FT: Colorado 2-1

Mechanism:
- Colorado's recent attack carries forward;
- Ventura rotation weakens continuity;
- altitude/home environment matters.

This is the main failure path for the Ventura winner.

---

# 10. Final ranking rationale

## #1 — 1st Half Over 0.5 Goals

Support:
- Ventura's elite current scoring run;
- Colorado defensive vulnerability;
- Placias scored at 8' in the first H2H;
- current Colorado XI has improved attacking threats.

Failure:
- controlled 0-0 opening / rotated Ventura attack.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Ventura County FC Team Corners Over 3.5

Support:
- 106 season corners in 23 matches;
- five corners vs Portland last match;
- direct attacking superiority and wide/clearance mechanisms;
- Colorado can concede large corner counts under pressure.

Failure:
- prior H2H only two Ventura corners;
- early Ventura lead suppresses later demand;
- provider definition unknown.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Full Match Over 2.5 Goals

Support:
- Ventura 47 GF;
- 15 GF in last five;
- Colorado 45 GA;
- Colorado just scored four;
- chase-state transition branch.

Failure:
- previous H2H was 1-1;
- Ventura 2-0 control is credible.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Full Match Under 2.5 Goals

Support:
- first H2H 1-1;
- Colorado recent 0-0;
- Ventura can win 2-0 without opening the game.

Why below Over:
- Ventura's current attack is substantially hotter than in broad season-average form;
- Colorado's season defensive weakness remains severe;
- Colorado's current attack creates a more credible second-team goal than the season baseline.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #5 — 1st Half Under 0.5 Goals

Requires a full scoreless opening 45+ minutes.

It is a genuine branch, but loses to:
- any Ventura early attack conversion;
- any Colorado home counter/set-piece goal.

Given the current attacking environment, it is the least robust of the five.

**Verdict:** `AVOID / FORCED RANK — MEDIUM-LOW`

`AVOID` means lowest-ranked among these five, not demonstrated negative expected value.

---

# 11. Final card

1. **1st Half Over 0.5 Goals**
2. **Ventura County FC Team Corners Over 3.5**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential regulation winner:** **Ventura County FC**

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

# 12. Source / limitation record

## Framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- active combined-log governance
- `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official / high-value current evidence
- Colorado Rapids 2 official match preview and official starting XI
- MLS NEXT Pro match/video records
- Ventura County FC / MLS NEXT Pro recent match records
- NWS Commerce City forecast

## Specialist supporting data
- FotMob team corner totals
- current match-stat databases for corner and goal splits

## Limitations
- Ventura's final field-owner XI was not recovered at cutoff;
- sportsbook/provider corner definition not supplied;
- complete current cross/block/end-line event data unavailable;
- developmental-team rotations create higher participant uncertainty;
- no fitted/validated soccer model exists.

**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`



# P-148 (conversation-local continuation) — Colorado Rapids 2 vs Ventura County FC — MLS NEXT Pro

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **2** | **Ventura County FC Team Corners Over 3.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Full Match Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Full Match Under 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **5** | **1st Half Under 0.5 Goals** | `AVOID / FORCED RANK` | `MEDIUM-LOW` |

**Potential regulation winner:** **Ventura County FC — FORCED WINNER / MEDIUM-LOW CONFIDENCE**

### Central regulation score family
- Ventura County FC 2-1
- Ventura County FC 2-0
- 1-1
- 2-2
- Colorado Rapids 2 2-1 as the main home-upset branch

### Central first-half family
- Colorado 0-1 Ventura
- 1-1
- Colorado 1-0
- 0-0 as the main contrary branch

---

## Administrative / framework status

Google Drive was used strictly as a **read-only framework source**.

This is labelled **P-148 conversation-local continuation** so local cards in this chat are not assigned duplicate IDs while the Drive canonical queue remains unreconciled.

**Method:** `MDS-2026.08.29-v2.5`  
**Soccer module:** `RULES_SOCCER.md` effective 2026-08-29  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`

---

# 1. Event identity

- **Competition:** MLS NEXT Pro
- **Match:** Colorado Rapids 2 vs Ventura County FC
- **Venue:** DICK'S Sporting Goods Park, Commerce City, Colorado
- **Scheduled kickoff:** Friday Aug. 28, 2026, 6:00 PM MT
- **Melbourne equivalent:** Saturday Aug. 29, 2026, 10:00 AM AEST
- **Winner endpoint:** regulation 90 minutes + stoppage time only

MLS NEXT Pro regular-season tied matches may proceed to a shootout for an additional standings point. The “potential winner” in this card is therefore explicitly the **regulation winner**, not the eventual shootout winner.

---

# 2. Participant gate

## Colorado — confirmed official XI

- Zack Campagnolo
- Kamal Sawadogo
- Charlie Harper
- Grant Gilmore
- Edgar Heredia
- Sebastian Siegler
- Luis García
- Josh Copeland
- Chris Aquino
- Ali Fadal (C)
- Sydney Wathuta

Substitutes:
- Dashiel Williams
- Kai Thomas
- Hamdoin Altayeb
- Kellen Lowery
- Jackson Pomeroy
- Jordan Camacho
- Niccolo Del Carmen

This keeps three scorers from Colorado's 4-1 win over Real Monarchs — Wathuta, Copeland and Aquino — in the starting group.

## Ventura — unresolved official XI

A final field-owner Ventura XI was not recovered at the cutoff.

Recent Ventura lineups have included Sebastian Conlon, Dalgado, Martinez, McLean/Hernandez, Vicente Garcia, Gabriel Arnold, Luis Müller, Eric Preston, Jeremi Djieze and Julian Placias, but these are **not promoted to tonight's confirmed XI**.

Because this is a development/reserve competition with meaningful rotation, the unresolved Ventura XI caps all participant-sensitive rows at:

`FORCED RANK / MEDIUM-LOW`

---

# 3. Current team regime

## Colorado Rapids 2

Current record:
- **3-14-7**
- 18 points
- 14th in the Western Conference
- approximately **24 GF / 45 GA** in the freshest table snapshot

Recent five:
- L 1-2 Tacoma
- L 0-3 LAFC2
- D 0-0 St. Louis CITY2
- D 2-2 Sporting KC II
- W 4-1 Real Monarchs

The 4-1 win was a genuine attacking improvement:
- Chris Aquino 43'
- Josh Copeland 52'
- Jonny De La Fuente 67'
- Sydney Wathuta 90+4'

Colorado produced 17 shots and eight shots on target in that game.

The framework does not automatically treat one 4-1 result as a regime reset. It creates a stronger home-attack branch than the season baseline, especially because Aquino/Copeland/Wathuta remain in the XI.

---

## Ventura County FC

Current record:
- **11-6-6**
- 42 points
- 4th West
- **47 GF / 30 GA**
- +17 goal difference

Recent five:
- 2-0 LAFC2
- 3-0 San Jose II
- 6-1 North Texas
- 2-0 Houston Dynamo 2
- 2-2 Portland Timbers2

That is approximately:
- **15 goals scored**
- **3 conceded**
- four wins and a draw

Ventura's current attack has multiple routes:
- Julian Placias
- Eric Preston
- Luis Müller
- Gabriel Arnold
- Vicente Garcia / wide and midfield progression branches

The current strength difference favors Ventura, but the unresolved XI and Colorado's home rebound prevent a strong side grade.

---

# 4. First-half goal process

The strongest supplied market is **1H Over 0.5**.

Relevant process evidence:

- Ventura's current attacking regime is substantially stronger than Colorado's season defensive baseline.
- Colorado have conceded 45 league goals and have repeatedly allowed first-half pressure.
- Ventura scored in the 45th minute against Portland in their latest match.
- In the first 2026 H2H, Julian Placias gave Ventura the lead in the **8th minute**.
- Colorado's current XI also has genuine early-scoring threats: Aquino scored at 43' last week, and Copeland/Wathuta remain active attacking pieces.

The direct previous H2H reached halftime:
**Ventura 1-0 Colorado**

and finished 1-1 before Colorado won the shootout.

### Main 0-0 first-half branch

- Ventura's away finishing cools;
- Colorado protects central areas at home;
- the heat/altitude encourages a less aggressive opening;
- Ventura's actual XI is more rotated than recent lineups.

This keeps the evidence at MEDIUM-LOW rather than a stronger label.

---

# 5. Full-match total process

## Over 2.5 branch

Ventura:
- 47 goals in 23 matches;
- 15 goals in the last five;
- 6-1 and multiple 2–3 goal outputs recently.

Colorado:
- just scored four against Real Monarchs;
- current XI retains the three main current scorers;
- season defense remains highly vulnerable.

Representative Over states:
- Ventura 2-1
- Ventura 3-1
- 2-2
- Colorado 2-1

The strongest Over mechanism is:

`Ventura pressure creates the first goal -> Colorado must chase -> transition space opens -> both teams have more attacking sequences`

## Under 2.5 branch

The Under cannot be dismissed:

- the first H2H finished **1-1**;
- Colorado recently had a 0-0 against St. Louis;
- Ventura have recent 2-0 wins that stay Under 2.5;
- a 1-0 / 2-0 Ventura control state is coherent.

Representative Under states:
- Ventura 2-0
- Ventura 1-0
- 1-1

I therefore rank Over only narrowly above Under.

---

# 6. Corner process — Ventura County FC team corners Over 3.5

This is the chosen fifth market.

## Direct exposure evidence

Season team-corner totals:
- Ventura: **106 corners in 23 matches** (~4.6 per match descriptively)
- Colorado: 107 corners in 24 matches

Latest Ventura match vs Portland:
- Ventura **5 corners**
- Portland 2

Current H2H in June:
- Ventura only **2 corners**
- Colorado 1

The low H2H count is retained as a real contrary state.

## Why Ventura Over 3.5 is preferred

The mechanism is not “Ventura are better, so they get corners.”

It is:

`Ventura stronger attack + Colorado weak defensive field-position baseline + wide attackers + blocked/cleared entries + Colorado chase/defend branches -> repeated corner exposure`

Colorado also recently conceded **7 corners to LAFC2** in a 3-0 loss, showing a high-corner defensive-pressure branch.

### Score-state dependence

If Ventura trail or remain level:
- corner demand should remain high.

If Ventura score early and control the match:
- later attacking/corner demand can fall.

That is the main kill path.

### Settlement limitation

The user did not specify a sportsbook/stat provider.

Research target:
`official MLS NEXT Pro regulation team corner kicks credited to Ventura County FC`

Exact bookmaker definition:
`UNKNOWN_DEFINITION`

Under the Drive's derivative-completeness rule, this market cannot receive `LEAN` or `SUPPORTED`.

---

# 7. Winner process

## Why Ventura County FC

Season/current advantages:
- 4th West vs 14th West;
- 47 GF vs ~24 Colorado;
- 30 GA vs ~45 Colorado;
- +17 GD vs approximately -21;
- four wins plus a draw in the last five;
- 15-3 scoring margin over that recent window.

Ventura are therefore the stronger regulation-winner branch.

## Why winner confidence is capped

- Colorado are at home.
- Colorado just won 4-1.
- Colorado's XI is officially known and keeps Aquino/Copeland/Wathuta.
- the first H2H was 1-1 after 90 minutes.
- Ventura's final official XI is unresolved.
- MLS NEXT Pro developmental rotations can materially change effective team strength.

So:
**Ventura regulation win is preferred, but draw and Colorado-upset branches remain material.**

---

# 8. Weather / altitude

DICK'S Sporting Goods Park is approximately **5,100 ft above sea level**.

Near 6 PM:
- temperature roughly **88°F**
- light/moderate wind around 9 mph
- small shower/thunderstorm probability

Mechanisms:
- heat + altitude can increase second-half fatigue and defensive-transition errors;
- possible showers can affect footing/ball speed;
- wind is not strong enough to create a major directional goal suppression assumption.

Weather is therefore a variance modifier, not an automatic Over or Under.

---

# 9. Joint scenario tree

## Branch A — Ventura early advantage
HT: Colorado 0-1 Ventura  
FT: Colorado 1-2 Ventura

Results:
- 1H Over 0.5 WIN
- FT Over 2.5 WIN
- Ventura winner WIN
- Ventura corner Over remains live

## Branch B — Ventura controls without shootout
HT: 0-1 or 0-0  
FT: 0-2

Results:
- FT Under 2.5 WIN
- Ventura winner WIN
- corner line depends on how early the lead arrives

## Branch C — repeat H2H-style close match
HT: 0-1 Ventura  
FT: 1-1

Results:
- 1H Over WIN
- FT Under WIN
- regulation winner = DRAW

## Branch D — open reserve-league match
HT: 1-1  
FT: 2-2 or Ventura 3-1

Results:
- 1H Over WIN
- FT Over WIN
- corner demand generally rises through chasing states

## Branch E — Colorado home upset
HT: Colorado 1-0  
FT: Colorado 2-1

Mechanism:
- Colorado's recent attack carries forward;
- Ventura rotation weakens continuity;
- altitude/home environment matters.

This is the main failure path for the Ventura winner.

---

# 10. Final ranking rationale

## #1 — 1st Half Over 0.5 Goals

Support:
- Ventura's elite current scoring run;
- Colorado defensive vulnerability;
- Placias scored at 8' in the first H2H;
- current Colorado XI has improved attacking threats.

Failure:
- controlled 0-0 opening / rotated Ventura attack.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #2 — Ventura County FC Team Corners Over 3.5

Support:
- 106 season corners in 23 matches;
- five corners vs Portland last match;
- direct attacking superiority and wide/clearance mechanisms;
- Colorado can concede large corner counts under pressure.

Failure:
- prior H2H only two Ventura corners;
- early Ventura lead suppresses later demand;
- provider definition unknown.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #3 — Full Match Over 2.5 Goals

Support:
- Ventura 47 GF;
- 15 GF in last five;
- Colorado 45 GA;
- Colorado just scored four;
- chase-state transition branch.

Failure:
- previous H2H was 1-1;
- Ventura 2-0 control is credible.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #4 — Full Match Under 2.5 Goals

Support:
- first H2H 1-1;
- Colorado recent 0-0;
- Ventura can win 2-0 without opening the game.

Why below Over:
- Ventura's current attack is substantially hotter than in broad season-average form;
- Colorado's season defensive weakness remains severe;
- Colorado's current attack creates a more credible second-team goal than the season baseline.

**Verdict:** `FORCED RANK — MEDIUM-LOW`

---

## #5 — 1st Half Under 0.5 Goals

Requires a full scoreless opening 45+ minutes.

It is a genuine branch, but loses to:
- any Ventura early attack conversion;
- any Colorado home counter/set-piece goal.

Given the current attacking environment, it is the least robust of the five.

**Verdict:** `AVOID / FORCED RANK — MEDIUM-LOW`

`AVOID` means lowest-ranked among these five, not demonstrated negative expected value.

---

# 11. Final card

1. **1st Half Over 0.5 Goals**
2. **Ventura County FC Team Corners Over 3.5**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential regulation winner:** **Ventura County FC**

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

# 12. Source / limitation record

## Framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- active combined-log governance
- `MDS-2026.08.29-v2.5`
- `NTS-2026.08.25-v0.2`

## Official / high-value current evidence
- Colorado Rapids 2 official match preview and official starting XI
- MLS NEXT Pro match/video records
- Ventura County FC / MLS NEXT Pro recent match records
- NWS Commerce City forecast

## Specialist supporting data
- FotMob team corner totals
- current match-stat databases for corner and goal splits

## Limitations
- Ventura's final field-owner XI was not recovered at cutoff;
- sportsbook/provider corner definition not supplied;
- complete current cross/block/end-line event data unavailable;
- developmental-team rotations create higher participant uncertainty;
- no fitted/validated soccer model exists.

**Google Drive modified:** `NO`  
**Retrospective:** `NOT INCLUDED`

## P-149 (conversation-local continuation) — Montreal Alouettes @ Winnipeg Blue Bombers — CFL Week 13

### Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Montreal Alouettes -6.5** | `LEAN` | `MEDIUM` |
| **2** | **Full Game Under 60.5 Points** | `LEAN` | `MEDIUM` |
| **3** | **Winnipeg Blue Bombers +6.5** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Full Game Over 60.5 Points** | `FORCED RANK` | `MEDIUM-LOW` |

**Potential winner:** **Montreal Alouettes — LEAN**

### Central score family
- Montreal 31-23
- Montreal 33-24
- Montreal 34-24
- Montreal 29-26 as the main Winnipeg-cover branch
- Montreal 38-27 as the principal Over branch
- Winnipeg 27-24 as the principal upset branch

### Administrative / framework status

**Method:** `MDS-2026.08.29-v2.5`  
**Sport module:** `RULES_AMERICAN_FOOTBALL.md` — CFL treated as its own rules/data population.  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate origin:** `USER_SUPPLIED`  
**Operator:** `NOT SUPPLIED`  
**Exact OT/void settlement definition:** `UNKNOWN_DEFINITION`

### Event identity

- Competition: Canadian Football League — Week 13
- Match: Montreal Alouettes at Winnipeg Blue Bombers
- Venue: Princess Auto Stadium, Winnipeg, Manitoba
- Scheduled start: Friday Aug. 28, 2026, 7:30 PM CDT / 8:30 PM ET
- Australia/Sydney and Melbourne equivalent: Saturday Aug. 29, 2026, 10:30 AM AEST
- State at final research refresh: `PREGAME`

### Process summary

Montreal enters 9-1 on a seven-game winning streak and carries the materially stronger current offensive process. The Alouettes average 36.7 points and 454.3 offensive yards per game, lead the league in rushing at 118.8 yards per game and convert 57.9% of second downs. Winnipeg averages 25.6 points, 345 offensive yards and converts 44.7% of second downs.

The primary side matchup is Montreal's league-leading rushing attack against a Winnipeg defence allowing 127.9 rushing yards per game. Winnipeg's strongest counter is its league-leading pass defence, but that strength can redirect Montreal toward Travis Theis instead of eliminating the offence. Theis has averaged 103.8 rushing yards over his last six games, while Montreal has scored 23 touchdowns on 61 possessions over its last five.

Winnipeg's best close-game mechanism is Brady Oliveira, who remains in the lineup and has rushed for 427 yards at 7.1 yards per carry over his last four games, combined with a strong secondary and historical H2H success. The principal concern is offensive drive sustainability and touchdown conversion. Winnipeg scored 19 points against Edmonton last week despite Oliveira rushing for 118 yards and produced only two first downs after halftime.

The Under 60.5 narrowly outranks the Over because Winnipeg's scoring profile has produced 21 touchdowns against 33 field goals through ten games, while the matchup gives Montreal a plausible run-heavy control route. The strongest Under kill path is Montreal's recent offensive ceiling: 42.7 points per game over its last three, with enough explosive and defensive scoring routes for Montreal to carry a large portion of the total itself.

Weather is a secondary variance modifier only: mainly cloudy conditions, a 30% evening shower chance, thunderstorm risk and southerly wind were forecast for Winnipeg. No automatic weather-based Under adjustment is applied.

### Contract geometry

- Montreal -6.5 and Winnipeg +6.5 are exact half-point opposites with no push.
- Over 60.5 and Under 60.5 are exact half-point opposites with no push.
- Spread and total outcomes remain dependent through game script.
- A Montreal win does not imply Montreal -6.5.
- An Under does not imply Winnipeg +6.5; a controlled Montreal separation can satisfy Montreal -6.5 and Under simultaneously.

### Strongest kill paths

**Montreal -6.5:** Winnipeg pass defence suppresses explosives, Oliveira controls possessions and Winnipeg converts enough red-zone opportunities to keep the final margin within six.

**Under 60.5:** Montreal's current scoring regime remains near its recent 40+ level while Winnipeg converts field-goal possessions into touchdowns.

**Winnipeg +6.5:** Montreal's run advantage and superior second-down efficiency create repeated sustained drives and second-half separation.

**Over 60.5:** Winnipeg's touchdown-conversion problems persist and Montreal shifts successfully into a run/control script after gaining the lead.

### Final ordering

1. Montreal Alouettes -6.5 — strongest supplied contract.
2. Under 60.5 — preferred total, but vulnerable to Montreal's offensive ceiling.
3. Winnipeg Blue Bombers +6.5 — credible close-game counterbranch.
4. Over 60.5 — coherent high-scoring branch, but requires more Winnipeg scoring conversion or another major Montreal eruption.

**Potential winner:** Montreal Alouettes.

**No probability, expected value, staking or profitability claim is made.**

# P-150 (conversation-local continuation) — Boca Juniors vs Lanús — Argentina Liga Profesional / Torneo Clausura 2026

**Research cutoff:** 2026-08-29 10:28 Australia/Melbourne / 2026-08-28 21:28 Argentina  
**GAME-STATE:** `PREGAME` at the frozen cutoff, approximately two minutes before the scheduled 21:30 ART kickoff.  
**Competition:** Liga Profesional de Fútbol — Torneo Clausura 2026, Fecha 7, Zona A  
**Venue:** Estadio Alberto J. Armando (La Bombonera), Buenos Aires  
**Scheduled kickoff:** Friday 28 August 2026, 21:30 ART / Saturday 29 August 2026, 10:30 AEST  
**Referee:** Pablo Dóvalo; VAR Germán Delfino  
**Candidate origin:** `USER_SUPPLIED + ANALYST_ADDED_CORNER_MARKET`  
**Method:** `MDS-2026.08.29-v2.5`  
**Sport module:** `RULES_SOCCER.md`, effective 2026-08-29  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Operator:** `NOT SUPPLIED`

---

## Executive forecast

| Rank | Pick | Verdict | Evidence quality | Actionability |
|---:|---|---|---|---|
| **1** | **Full Match Under 2.5 Goals** | **LEAN** | **MEDIUM** | Likelihood ranking only; no price/value claim |
| **2** | **Boca Juniors Team Corners Over 4.5** | `FORCED RANK` | **MEDIUM-LOW** | Corner provider/operator definition not supplied |
| **3** | **1st Half Under 0.5 Goals** | **LEAN** | **MEDIUM** | Exact 45'+stoppage-time half only |
| **4** | **1st Half Over 0.5 Goals** | `FORCED RANK` | **MEDIUM-LOW** | Exact complement of Rank 3 |
| **5** | **Full Match Over 2.5 Goals** | **AVOID / FORCED RANK** | **MEDIUM** | Exact complement of Rank 1 |

**Potential regulation winner:** **Boca Juniors — LEAN / MEDIUM-LOW CONFIDENCE**

### Central regulation score family
- **Boca Juniors 1-0**
- **1-1**
- **Boca Juniors 2-0**
- 0-0 as the strongest very-low-event branch
- Lanús 1-0 as the principal away-upset branch
- Boca 2-1 / Lanús 2-1 as the principal Over-2.5 kill paths

### Central first-half family
- **0-0**
- Boca Juniors 1-0
- Lanús 1-0
- 1-1 as the main high-event first-half tail

---

# 1. Framework / contract freeze

The governing Drive method requires:
- one coherent regulation-goal process for winner and full-match total;
- a separate first-half goal target;
- a separate corner process rather than treating possession, shots or club strength as corner events;
- exact participant-status handling;
- no internally fabricated probabilities while the numerical model remains unfit.

## Target A — regulation goals
`TARGET_ID: SOC-ARG-CLAUSURA-2026-BOC-LAN-REG-GOALS-v1`

Outcome: `(Boca regulation goals, Lanús regulation goals)`  
Endpoint: 90 minutes plus official stoppage time.  
Extra time: not applicable to this league-stage match.  
Derived supplied contracts:
- Full Match Over 2.5
- Full Match Under 2.5
- Potential regulation winner

## Target B — first-half goals
`TARGET_ID: SOC-ARG-CLAUSURA-2026-BOC-LAN-1H-GOALS-v1`

Outcome: combined goals in the first half.  
Endpoint: first 45 minutes plus official first-half stoppage time.  
Derived supplied contracts:
- 1H Over 0.5
- 1H Under 0.5

## Target C — Boca team corners
`TARGET_ID: SOC-ARG-CLAUSURA-2026-BOC-LAN-BOCA-CORNERS-v1`

Outcome: Boca Juniors regulation team corners.  
Analyst-added line: **Over 4.5 Boca team corners**.  
Endpoint assumption: regulation plus stoppage time only.  
**Bookmaker/stat provider not supplied:** `UNKNOWN_DEFINITION`.

Because the Drive soccer module requires the exact derivative provider/definition plus the corner exposure/rate/context chain before a corner market can receive `LEAN` or `SUPPORTED`, the corner selection is deliberately capped at `FORCED RANK / MEDIUM-LOW`, even though the available statistical direction is favourable.

---

# 2. Event identity and current state

The Liga Profesional's official schedule lists:

- Friday 28 August 2026
- **21:30 ART — Boca Juniors vs Lanús**
- Torneo Clausura, Fecha 7, Zona A
- TNT Sports

The official LPF referee assignment lists **Pablo Dóvalo** as referee and **Germán Delfino** as VAR.

This card was frozen at **10:28 AEST / 21:28 ART**, before the scheduled kickoff. If the match starts before this text is consumed, this remains a frozen pregame view and must not be reinterpreted as a live forecast.

---

# 3. Participant gate

## Boca Juniors — confirmed current XI in multiple same-day sources

- Álvaro Montero
- Dylan Gorosito
- Lautaro Di Lollo
- Facundo Herrera
- Lautaro Blanco
- Santiago Ascacíbar
- Camilo Rey Domenech
- Milton Delgado
- Alan Velasco
- Leonel Flores
- Miguel Merentiel

**Important current-regime changes:**
- Ayrton Costa is out after the hamstring injury suffered against Racing.
- Tomás Aranda is out after a fracture in training.
- Lautaro Di Lollo returns to the XI.
- Alan Velasco starts.
- **Leandro Paredes starts on the bench**, reducing the certainty that Boca's best controlling passer/set-piece distributor is present for the full first-half phase.

Boca's XI is sufficiently resolved for the goal-side analysis.

## Lanús — exact official XI unresolved at cutoff

The strongest same-day reporting consistently projected:
- Nahuel Losada
- Tomás Guidara
- Carlos Izquierdoz
- José María Canale
- Sasha Marcich
- Agustín Medina
- Felipe Peña Biafore
- Matías Sepúlveda or Franco Watson
- Eduardo Salvio
- Dylan Aquino
- Allan Wlk

However, an equivalently authoritative official final XI was not recovered before the cutoff. The unresolved Sepúlveda/Watson branch and absence of a field-owner final team sheet prevent participant-sensitive claims from being described as confirmed.

This uncertainty is one reason the Boca winner call remains **MEDIUM-LOW** rather than stronger.

---

# 4. Baseline and current attacking/defensive regime

## Boca Juniors

The current Clausura has not produced a dominant league scoring profile:
- 6 matches before this fixture
- 1 win, 4 draws, 1 loss
- 6 goals scored, 8 conceded
- recent league sequence includes 1-1 vs Racing, 1-1 vs Platense, 1-1 vs Vélez, 1-0 vs Estudiantes and 2-2 vs Newell's.

A broader 2026 Liga Profesional sample places Boca around:
- **1.30 goals scored per match**
- **Under 2.5 in 65% overall**
- **Under 2.5 in 91% of home matches**
- home first-half total-goal average about **0.82**
- 1H Over 0.5 in **55% of home matches**
- therefore 1H Under 0.5 in **45% of home matches**.

Process-wise, Boca still own the stronger territory/creation baseline in several season-level datasets:
- approximately 60%+ possession/territorial control in the broader sample;
- about 5.2–5.6 team corners per match overall;
- roughly 6.3–6.5 team corners in home splits.

But the exact current XI matters. Paredes beginning on the bench plus the defensive changes around Costa/Aranda introduce a less stable first-half regime than a full-strength Boca prior.

## Lanús

Broader 2026 Liga Profesional sample:
- approximately **1.09 goals scored per match**
- approximately **1.04 conceded**
- combined match average about **2.13 goals**
- **Under 2.5 in 61% overall**
- **Under 2.5 in 55% away**
- first-half combined-goal average about **0.57**
- **1H Under 0.5 in 65% overall and 64% away**.

The half split is especially important:
- Lanús scored only **0.30 first-half goals per match** in the cited 23-game league sample;
- Lanús conceded only **0.26 first-half goals per match**;
- their second-half combined scoring environment is materially higher.

Their immediate league sequence also reinforces the slow-opening branch without being treated as a fitted weight:
- Lanús 1-1 Argentinos — **HT 0-0**
- Lanús 1-3 Independiente — **HT 0-1**
- Talleres 0-3 Lanús — **HT 0-0**
- Unión 2-1 Lanús — **HT 0-0**
- Lanús 0-1 Instituto — **HT 0-0**
- Lanús 1-0 San Lorenzo — **HT 0-0**

That is **five 0-0 half-times in the most recent six listed league matches**.

Lanús' official post-Argentinos comments also noted fatigue: Carlos Izquierdoz said the team became physically and mentally tired late in the 1-1 draw, while the match itself remained 0-0 until the 70th minute.

This is not an automatic Under rule, but it supports a match tree in which Lanús are more conservative early and become more vulnerable or expansive later.

---

# 5. Rank #1 — Full Match Under 2.5 Goals

**Verdict: LEAN**  
**Evidence: MEDIUM**

This is the strongest supplied direction.

## Why the Under leads

### A. Both broader team distributions lean low
- Boca: 65% Under 2.5 overall in the cited 2026 league sample.
- Boca home: 91% Under 2.5.
- Lanús: 61% Under 2.5 overall.
- Lanús away: 55% Under 2.5.

The framework does not simply average those rates. Their usefulness is that they are directionally consistent with the current mechanisms.

### B. Boca's current league attack has been more controlled than explosive
Boca's last four league results before this match were:
- 1-1 Racing
- 1-1 Platense
- 1-1 Vélez
- 1-0 Estudiantes

That gives a central 1–2 total-goal corridor rather than a stable high-scoring regime.

### C. Lanús' scoring is heavily second-half weighted
Lanús' broad sample shows only 0.57 combined first-half goals but around 1.57 in second halves. This creates a coherent path such as:
- 0-0 HT → 1-0 FT
- 0-0 HT → 1-1 FT
- 0-0 HT → 2-0 FT

### D. Boca's most established midfield controller is not starting
Paredes being on the bench is not automatically an Under. It increases uncertainty around Boca's first-half chance progression and set-piece distribution and reduces confidence in an aggressive Boca 2+ goal baseline from kickoff.

## Strongest Under kill paths
- Boca create the first goal early, forcing Lanús to chase and exposing transition space.
- Lanús' current defence repeats the 1-3 Independiente / 2-1 Unión type branch.
- Boca's front four convert efficiently rather than merely accumulating territory.
- Defensive instability from Boca's altered centre-back configuration gives Lanús a clearer scoring route.
- A penalty/red card/major goalkeeper error creates a high-event state.

### Scores that defeat Under 2.5
- Boca 2-1
- Lanús 2-1
- Boca 3-0
- 2-2

Those are credible but remain secondary to the 0-0 / 1-0 / 1-1 / 2-0 corridor.

---

# 6. Rank #2 — Boca Juniors Team Corners Over 4.5

**Verdict: FORCED RANK**  
**Evidence: MEDIUM-LOW**  
**Reason verdict is capped:** exact operator/provider corner definition was not supplied.

## Direct corner exposure evidence

### Boca
Two independent season/recent databases place Boca around:
- **5.1–5.6 corners for per match overall**
- **5.5–6.45 corners for at home**

Liga Profesional-specific home split in one dataset:
- **6.36 Boca corners for**
- **2.55 conceded**

A second database reports:
- **6.45 Boca corners for at home**
- **2.55 conceded**

Recent home-match corner counts cited by a separate tracker include:
- 8 vs Recoleta
- 5 vs Vélez
- 5 vs Estudiantes
- 7 vs O'Higgins
with a reported run of 5+ Boca home corners across the listed sequence.

### Lanús
Liga Profesional away corner profile:
- **3.18 corners for**
- **4.82 conceded**
- **8.00 total corners per away match**

Another rolling source places Lanús at:
- 3.7 corners for
- 4.2 conceded
- 7.9 combined

The opponent-adjusted centre of the Boca-team-corner process is therefore around the 5-corner boundary rather than below it.

## Mechanism
The current Boca XI retains two natural wide/fullback progression routes through **Lautaro Blanco and Dylan Gorosito**, plus Velasco/Flores/Merentiel as the advanced unit. Boca at home are likely to own more attacking sequences than Lanús.

However, the Drive rules correctly prevent treating "Boca have possession" as "Boca get corners." The direct corner evidence is stronger than the goal-proxy route, but the following decisive fields remain incomplete:
- exact current cross/block/end-line rate by the confirmed XI;
- exact operator/stat-provider definition;
- official Lanús XI and width/defensive substitutions;
- exact score-state corner response for this lineup.

Therefore **Over 4.5 Boca corners is retained as a strong ordinal candidate but capped at FORCED RANK / MEDIUM-LOW**.

## Kill path
Boca score early and shift into lower-risk possession, Lanús open up and take more of the territorial share, while Boca finish central attacks without producing blocks/deflections/end-line exits.

Representative Boca corner outcomes:
- central: **5–7**
- lower: **3–4**
- upper: **8+**

---

# 7. Rank #3 — 1st Half Under 0.5 Goals

**Verdict: LEAN**  
**Evidence: MEDIUM**

This is a genuine close decision against its exact opposite.

## Evidence for 0-0 at halftime
Lanús provide the strongest mechanism:
- 1H average total goals: **0.57**
- 1H Under 0.5: **65% overall**
- 1H Under 0.5 away: **64%**
- five 0-0 half-times in the last six listed league matches.

Boca's home data are less supportive:
- home 1H average: **0.82**
- home 1H Over 0.5: **55%**
- home 1H Under 0.5: **45%**

So this is not a "both teams are automatic 0-0 HT" claim.

## Why I still put Under above Over
- Lanús' first-half suppression is materially stronger than Boca's home early-goal tendency.
- Lanús' recent match-state structure has repeatedly delayed scoring.
- Boca's midfield/defence is changed and Paredes starts on the bench.
- Both sides enter needing points, but neither current league attack has shown a sustained first-half high-conversion regime.

## Kill path
Boca's return to La Bombonera creates an aggressive opening, Merentiel/Velasco get an early clear chance, or Lanús exploit the changed Boca centre-back pair before the match settles.

---

# 8. Rank #4 — 1st Half Over 0.5 Goals

**Verdict: FORCED RANK**  
**Evidence: MEDIUM-LOW**

This is the exact half-point complement of Rank #3 and therefore cannot be treated as independent confirmation.

The Over case is real:
- Boca home matches have produced at least one first-half goal in **55%** of the cited 2026 Liga Profesional home sample.
- Racing–Boca was already 1-1 at halftime in Boca's latest league match.
- Boca are returning to La Bombonera and need a league win.
- Lanús' away defence concedes more than its home defence over the full match.

But the Lanús slow-start profile plus Boca's altered XI keeps the 0-0 branch marginally ahead.

---

# 9. Rank #5 — Full Match Over 2.5 Goals

**Verdict: AVOID / FORCED RANK**  
**Evidence: MEDIUM**

The Over is not impossible and should not be dismissed as a tail-only outcome.

## Over pathways
- Boca score first and force Lanús out of their compact starting state.
- Lanús exploit Boca's altered central defence.
- A set piece or penalty creates the first goal and opens transition volume.
- Lanús repeat the high-event 1-3 / 0-3 / 2-1 recent branches.
- Boca's wider home attack generates both shots and second-phase chances.

However, at this exact threshold the evidence is weaker than the Under:
- Boca 2026 home O2.5 rate in the cited league sample: only **9%**.
- Lanús broader O2.5 rate: **39%** overall, **45% away**.
- Boca's immediate league sequence has been dominated by 1-0 / 1-1 scorelines.

Therefore the Over belongs fifth.

---

# 10. Potential regulation winner — Boca Juniors

**Winner status: LEAN / MEDIUM-LOW CONFIDENCE**

Boca are the preferred regulation winner, but the draw band is substantial.

## Boca winning mechanisms
- Home-field return to La Bombonera.
- Stronger broader territory/creation and home-corner profile.
- Merentiel plus Velasco/Flores provide multiple scoring roles.
- Lanús have shown late-game fatigue and second-half concession vulnerability.
- Lanús' away concession rate is higher than their home rate.

## Why this is not high confidence
- Boca have only one win through the first six Clausura matches.
- They have drawn four of six.
- Their current league sequence contains three straight 1-1 draws.
- Paredes is not starting.
- Costa is unavailable and the centre-back structure changes.
- Lanús' exact XI was not officially resolved at cutoff.
- Lanús have enough defensive experience and transition threat to make 0-0, 1-1 and 0-1 ordinary branches.

### Winner tree
1. **Boca 1-0** — strongest winner branch.
2. **1-1** — strongest non-Boca branch.
3. **Boca 2-0** — separation branch.
4. **0-0** — low-event draw.
5. **Lanús 1-0** — principal away-upset branch.

The potential winner is therefore **Boca**, but the Under is materially stronger than the outright side call.

---

# 11. Scenario / contract map

| Scenario | Representative score | 1H U0.5 | 1H O0.5 | FT U2.5 | FT O2.5 | Boca O4.5 corners |
|---|---:|:---:|:---:|:---:|:---:|:---:|
| Slow Boca control | Boca 1-0 | ✅ likely | ❌ | ✅ | ❌ | ✅ / neutral |
| Controlled draw | 1-1 | ✅ plausible | ❌ | ✅ | ❌ | ✅ plausible |
| Boca separation without shootout | Boca 2-0 | ✅/❌ | ✅/❌ | ✅ | ❌ | ✅ |
| Locked match | 0-0 | ✅ | ❌ | ✅ | ❌ | score-state dependent |
| Early Boca goal opens match | Boca 2-1 | ❌ | ✅ | ❌ | ✅ | ✅ likely |
| Lanús transition win | Lanús 1-0 | ✅/❌ | ✅/❌ | ✅ | ❌ | may fail |
| High-event tail | 2-2 | ❌ | ✅ | ❌ | ✅ | likely higher |

The table illustrates dependence. Under 2.5 and 1H Under 0.5 share a slow-start/low-conversion mechanism and are **not independent picks**.

---

# 12. Final ranking

1. **Full Match Under 2.5 Goals — LEAN / MEDIUM**
2. **Boca Juniors Team Corners Over 4.5 — FORCED RANK / MEDIUM-LOW**
3. **1st Half Under 0.5 Goals — LEAN / MEDIUM**
4. **1st Half Over 0.5 Goals — FORCED RANK / MEDIUM-LOW**
5. **Full Match Over 2.5 Goals — AVOID / FORCED RANK / MEDIUM**

**Potential regulation winner:** **Boca Juniors — LEAN / MEDIUM-LOW**

### Plain-language bottom line

The most defensible game state is **tight early and low-to-moderate scoring overall**. Lanús' strong first-half 0-0 profile and Boca's very high 2026 home Under-2.5 rate push the goal tree toward 0-0 HT and 1-0 / 1-1 / 2-0 FT outcomes. Boca are still the preferred winner because of home field and the stronger broader territory/creation profile, but the draw is too live to elevate the winner call above the total.

The best analyst-added corner direction is **Boca Over 4.5 team corners** because Boca's home corner generation sits above that threshold while Lanús concede close to five away corners per match. It is deliberately not called a LEAN because the exact operator/provider definition and full target-event corner chain are incomplete.

No numerical probability, expected value, staking advice, ROI or market-edge claim is made.

---

# 13. Source register

## Drive framework
- `RULES_SOCCER.md` — current sport-specific governing module.
- `RULES_GENERAL.md` — event/state/contract/source hard gates and derivative completeness.
- `AGENT_ROLE_AND_TASK.md` — mandatory ranking and honesty boundary.
- `PREDICTION_LOG_COMBINED.md` — canonical Drive queue authority; not edited in this task.

## Official / primary current sources
1. Liga Profesional — Fecha 4–7 schedule  
   https://www.ligaprofesional.ar/notas/primera/2026/08/07/agenda-de-la-fecha-4-a-la-7/
2. Liga Profesional — Fecha 7 referee assignments  
   https://www.ligaprofesional.ar/notas/arbitraje/2026/08/25/autoridades-de-la-fecha-7-6/
3. Club Atlético Lanús — post-Argentinos mixed-zone comments  
   https://clublanus.com/izquierdoz-pena-biafore-laplace-y-perez-presentes-en-zona-mixta/
4. Boca Juniors official news index / current club status  
   https://www.bocajuniors.com.ar/noticias

## Current team / lineup reporting
5. Planeta Boca Juniors — confirmed Boca XI  
   https://planetabj.com/boca-juniors/dos-cambios-y-una-sorpresa-el-equipo-confirmado-de-boca-vs-lanus-por-el-torneo-clausura-2026/
6. La Número 12 — confirmed Boca XI / Paredes bench  
   https://lanumero12.com.ar/formacion-boca-lanus-clausura-2026/
7. TyC Sports — match preview, time, venue  
   https://www.tycsports.com/liga-profesional-de-futbol/argentina-torneo-clausura-2026-boca-juniors-vs-lanus-fecha-7-id757268.html
8. Olé / Bolavip same-day preview — Lanús projected XI and current match context.

## Statistical research sources
9. FootyStats — Boca 2026 Liga Profesional goals/halves/home splits  
   https://footystats.org/clubs/ca-boca-juniors-705
10. FootyStats — Lanús 2026 Liga Profesional goals/halves/away splits  
    https://footystats.org/clubs/ca-lanus-704
11. FootyMetrics — Boca/Lanús goals and corner splits.
12. CornerEdge — Boca and Lanús rolling corner profiles.
13. FootballNation / FootyBets — corroborating Boca/Lanús corner splits and recent corner counts.

These secondary sources are used only for their statistical fields and are not allowed to override official event identity, referee, final score, or participant confirmation.

# P-151 (conversation-local continuation) — Atlante vs León — Liga MX Apertura 2026

## Executive forecast

| Rank | Pick | Verdict | Evidence | Contract note |
|---:|---|---|---|---|
| **1** | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | Supplied half-point exact complement |
| **2** | **Total Corners 9+ — Caliente 3-way Over 8** | `FORCED RANK` | `MEDIUM-LOW` | Exactly 8 is a separate 3-way result |
| **3** | **Full Match Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | Supplied half-point exact complement |
| **4** | **Full Match Under 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | Strong ordinary contrary branch |
| **5** | **1st Half Under 0.5 Goals** | `AVOID / FORCED RANK` | `MEDIUM-LOW` | Exact complement of Rank #1 |

**Potential regulation winner:** **León — FORCED WINNER / LOW CONFIDENCE**

### Central regulation score family
- León 2-1
- 1-1
- León 1-0
- Atlante 2-1
- 2-2 as the higher-event tail
- 0-0 / Atlante 1-0 as the main low-event/upset branches

### Central first-half family
- Atlante 0-1 León
- 1-0 Atlante
- 0-0
- 1-1 as the higher-event first-half tail

---

## Administrative / framework status

**Method:** `MDS-2026.08.29-v2.5`  
**Soccer module:** `RULES_SOCCER.md`, effective 2026-08-29  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate origin:** `USER_SUPPLIED + ANALYST_ADDED_CORNER_MARKET`  
**Operator:** not supplied by user; Caliente is used only to freeze the analyst-added corner contract and as an external market sanity check.  
**Canonical Drive state:** the Drive combined log still identifies `P-137` as its next canonical ID. This entry is therefore labelled `P-151 conversation-local continuation` and does not claim canonical Drive reconciliation or modification.

---

# 1. Event identity and state

- **Competition:** Liga MX — Apertura 2026
- **Round:** Jornada 6
- **Match:** Atlante vs Club León
- **Venue:** Estadio Banorte, Ciudad de México
- **Scheduled kickoff:** Friday 28 August 2026, 19:00 Central Mexico
- **Melbourne equivalent:** Saturday 29 August 2026, 11:00 AEST
- **Frozen research cutoff:** approximately Saturday 29 August 2026, 10:46 AEST / Friday 28 August 2026, 18:46 Central Mexico
- **GAME-STATE:** `PREGAME` at the final web refresh.

TUDN and AS independently list the match at Estadio Banorte at 19:00 Central Mexico. Some older/stale pages expose legacy venue labels; those were not allowed to control the event identity.

---

# 2. Target and contract freeze

## Target A — first-half regulation goals

`TARGET_ID: SOC-MEX-LIGAMX-2026-ATL-LEO-1H-GOALS-v1`

Outcome: combined first-half goals.  
Endpoint: 45 minutes plus official first-half stoppage time.  
Contracts:
- Over 0.5: wins with one or more first-half goals.
- Under 0.5: wins only with 0-0 at halftime.
- No push.

## Target B — regulation full-match goals

`TARGET_ID: SOC-MEX-LIGAMX-2026-ATL-LEO-REG-GOALS-v1`

Outcome: `(Atlante goals, León goals)` through 90 minutes plus stoppage time.  
Contracts:
- Over 2.5: wins on 3+ total goals.
- Under 2.5: wins on 0-2 total goals.
- No push.

## Target C — regulation total corners

`TARGET_ID: SOC-MEX-LIGAMX-2026-ATL-LEO-CORNERS-v1`

Chosen market:
**Caliente — Tiros de Esquina, 3 Opciones — Over (8).**

This is **not** an Asian Over 8 with a push. Caliente separately lists:
- Over 8
- Exact 8
- Under 8

Therefore the research-grade win condition is explicitly:
**9 or more total regulation corners.**

Because the Drive soccer module also requires target-event width/cross/block/end-line/clearance evidence for a corner `LEAN` or `SUPPORTED` verdict, and that full direct-event chain is incomplete, the market is capped at:
`FORCED RANK / MEDIUM-LOW`.

---

# 3. Participant / availability gate

A field-owner official final XI was not recovered during the cutoff window. A same-day AS match lineup feed lists a current starting structure, but under the Drive rules this remains secondary rather than `CONFIRMED_OFFICIAL`.

### Atlante — same-day secondary lineup core
The current feed includes:
- Óscar Jiménez in goal;
- Walter Portales, Walter Clar, Aarón Quirós, Eduardo Tercero and Nico Carrera across the defensive/wing structure;
- Octavio Vázquez and Eugenio Pizzuto in midfield;
- Luis Puente and Jhojan Julio in attack.

The visible secondary feed did not provide a sufficiently trustworthy field-owner source for every final slot, so no missing name is invented.

### León — same-day secondary lineup
The same-day feed lists:
- Óscar García;
- Bryan Colula, Salvador Reyes, José Rodríguez, Juan Guevara, Sebastián Vegas;
- Jordi Cortizo, Luis Valadez, Fernando Beltrán, Daniel Arcila;
- Díber Cambindo.

### Material availability
- León centre-back **Jhohan Romaña** was sent off against Monterrey and is not part of the current same-day listed XI.
- The exact Atlante suspension wording varies across secondary reports; this card does **not** repeat an uncertain name/position as fact.

Because a field-owner official XI was not recovered, participant-sensitive rows remain capped at `FORCED RANK / MEDIUM-LOW`.

---

# 4. Current league baseline

## Atlante

Through five Liga MX matches:
- **1 win, 2 draws, 2 losses**
- **5 points**
- **5 goals scored, 7 conceded**
- approximately **2.4 total goals per match**

League results:
- Necaxa 2-1 Atlante
- Atlante 1-1 América
- Cruz Azul 2-3 Atlante
- Atlante 0-0 Toluca
- Tigres 2-0 Atlante

This is not a pure low-event profile:
- 2 of 5 matches cleared 2.5 goals.
- 3 of 5 stayed Under 2.5.
- Their two home league games are **1-1** and **0-0**, so Atlante remain unbeaten at home but winless there.

Recent first halves:
- Necaxa 0-0 Atlante at HT
- Atlante 0-1 América at HT
- Cruz Azul 0-1 Atlante at HT
- Atlante 0-0 Toluca at HT
- Tigres 0-0 Atlante at HT

So Atlante alone would make 1H Over 0.5 a close proposition rather than a strong one.

## León

Through five Liga MX matches:
- **3 wins, 0 draws, 2 losses**
- **9 points**
- **7 goals scored, 5 conceded**
- approximately **2.4 total goals per match**

League results:
- León 2-3 Atlas
- Tijuana 1-0 León
- León 1-0 Pachuca
- Necaxa 1-2 León
- León 2-0 Monterrey

That also produces:
- 2 of 5 Over 2.5
- 3 of 5 Under 2.5.

The important current-regime difference is that León's recent attack has been starting faster:
- Daniel Arcila scored in the **27th minute** at Necaxa.
- Jordi Cortizo scored in the **24th minute** against Monterrey.
- Díber Cambindo scored in the **21st minute** against Real Salt Lake in the Leagues Cup quarterfinal.

León then beat Real Salt Lake **3-0** on 25 August and current Mexican reporting describes the club as carrying a seven-match winning streak across competitions.

That is why 1H Over 0.5 is ranked first even though Atlante have recently produced several 0-0 first halves.

---

# 5. Rank #1 — 1st Half Over 0.5 Goals

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

## Why it ranks first

The strongest mechanism is not a generic Liga MX Over tendency. It is León's current early attacking regime.

Across three consecutive relevant wins:
- Arcila scored at 27' vs Necaxa;
- Cortizo scored at 24' vs Monterrey;
- Cambindo scored at 21' vs Real Salt Lake.

The same-day secondary lineup again lists Cortizo, Arcila and Cambindo in León's current attacking unit, creating continuity in the transition/box-arrival mechanism rather than a simple streak argument.

Atlante's own recent 1H record is mixed, but they allowed América to score in the first half and they themselves led Cruz Azul before halftime.

The external Caliente market also prices **1H Over 0.5 shorter than Under 0.5**. This is only a market sanity check; it is not an internal model probability or value claim.

## Strongest kill path

The 0-0 branch is material:
- Atlante have had 0-0 first halves against Necaxa, Toluca and Tigres in three of their five league games.
- Atlante have drawn both home league games and held Toluca scoreless.
- León are coming off a midweek Leagues Cup quarterfinal and must manage short rest/travel.
- Heavy showers are forecast around the match window.

That keeps the verdict at `FORCED RANK / MEDIUM-LOW`, not `SUPPORTED`.

---

# 6. Rank #2 — Total Corners 9+ (Caliente 3-way Over 8)

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

## Contract clarity

Caliente lists:
- Over 8
- Exact 8
- Under 8

as three mutually exclusive outcomes.

Therefore:
**Over 8 = 9 or more corners.**
Exactly eight is not a push.

## Corner-rate evidence

Current Liga MX corner table:
- Atlante: **4.2 corners won**, **6.8 conceded**, **11.0 total corners** per match.
- León: **4.4 won**, **4.2 conceded**, **8.6 total corners** per match.
- Liga MX overall listed average: roughly **10.6-10.7 total corners** per match.

Atlante's 6.8 conceded is particularly important. It means their current matches create high opponent corner exposure even though Atlante themselves are not an elite corner-winning side.

The line is only 9+ total corners, below the current Atlante-match average and near the combined team/league centre.

## Mechanism

The relevant process is:
- León have enough wide/transition threat to attack Atlante's high corner-concession profile.
- If Atlante fall behind, their own chase state can increase attacking width and corner demand.
- If the match remains level, both sides can continue generating entries rather than immediately protecting a lead.

## Kill path

A quick goal followed by lower-risk possession, highly efficient central finishing, or persistent rain reducing clean crossing/end-line sequences could keep the count to 6-8.

The provider definition is resolved, but the full cross/block/end-line/clearance chain for the exact current XIs is not. Under `RULES_SOCCER.md`, that prevents a `LEAN`/`SUPPORTED` label.

---

# 7. Rank #3 — Full Match Over 2.5 Goals

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This is only narrowly above the Under.

## Over mechanisms

### León's current attacking regime
León have just:
- beaten Necaxa 2-1;
- beaten Monterrey 2-0;
- beaten Real Salt Lake 3-0.

The recent goals are not merely one finishing burst: early goals have come from Arcila, Cortizo and Cambindo across different matches.

### Defensive disruption
Romaña's suspension removes a regular León centre-back option. That raises the Atlante-scoring branch even if León remain the stronger team.

### Game state
Atlante still seek their first home league win after two home draws. If León score first, Atlante must eventually open their shape; if Atlante score first, León have shown enough current attacking quality to respond.

### Weather is two-sided
Wet conditions can suppress passing/finishing, but they also increase handling errors, goalkeeper spills, deflections and set pieces. The Drive rules prohibit converting rain automatically into an Under.

The current Caliente market has Over 2.5 modestly shorter than Under 2.5. Again, that is an external benchmark only.

## Central Over scores
- León 2-1
- Atlante 2-1
- 2-2

---

# 8. Rank #4 — Full Match Under 2.5 Goals

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

The Under is a serious contrary branch and very close to Rank #3.

## Why it remains credible

Both teams have the same basic five-game league shape:
- average total goals approximately **2.4**
- **3 of 5** matches Under 2.5.

Atlante's two home matches:
- 1-1 América
- 0-0 Toluca

are both Under 2.5.

León have also won 1-0 against Pachuca and 2-0 against Monterrey.

### Short-rest branch
León played a Leagues Cup quarterfinal in Colorado on Tuesday night and return to Liga MX on Friday. Fatigue can reduce pressing volume, repeated sprint quality and second-half execution.

### Weather branch
The match-window forecast calls for showers/heavy showers in Mexico City. This may reduce clean technical execution on a wet surface, although no automatic Under adjustment is made.

## Why it ranks below the Over

The combination of:
- León's current attacking momentum;
- three straight relevant matches with early León goals;
- Romaña's absence;
- Atlante needing to chase a home win;
- and the external total market's slight Over preference

keeps the higher-event branch fractionally ahead.

Central Under scores:
- León 1-0
- 1-1
- Atlante 1-0
- 0-0
- León 2-0

---

# 9. Rank #5 — 1st Half Under 0.5 Goals

**Verdict:** `AVOID / FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This is the exact complement of Rank #1.

Its case is stronger than a normal bottom-ranked pick:
- Atlante have reached halftime 0-0 in three of five league matches.
- Both Atlante home games have been controlled.
- León are on short rest.
- Rain is forecast near kickoff.

It is ranked fifth only because León's current attacking regime has produced first-half goals at 27', 24' and 21' in the three most recent relevant wins.

---

# 10. Potential regulation winner — León

**Status:** `FORCED WINNER — LOW CONFIDENCE`

León are the preferred regulation winner, but this is weaker than the first-half-goal and corner directions.

## León winner mechanisms

- Better league record: **3-0-2 / 9 points** versus Atlante **1-2-2 / 5 points**.
- Current seven-match winning run across competitions.
- Recent wins over Necaxa, Monterrey and Real Salt Lake.
- Current attacking continuity through Cortizo, Arcila and Cambindo in the same-day secondary lineup.

## Strongest failure paths

### Atlante home resilience
Atlante are **0-2-0 at home**, not 0-0-2:
- 1-1 América
- 0-0 Toluca.

They have already shown they can keep stronger Liga MX opponents in a narrow home score band.

### León schedule fatigue
León played in Colorado on Tuesday and return to league action Friday, creating a short-rest/travel branch.

### Romaña absence
The centre-back suspension weakens continuity in León's defensive structure.

### Market disagreement
Current Caliente snapshots have been close enough to move the favourite between León and Atlante. That reinforces the conclusion that there is no robust outright-winner edge to claim.

Therefore the winner is:
**León, but only as a low-confidence forced winner.**

---

# 11. Weather / environment

Mexico City forecast around the scheduled 19:00 kickoff:
- heavy showers in one current Met Office city forecast;
- very high precipitation probability around 18:00-21:00;
- local SGIRPC reporting, relayed by El Universal, also warned of strong localized showers, electrical activity and possible hail, with the strongest risk through approximately 19:00.

Mechanistic interpretation:
- possible reduction in clean combination play and finishing;
- possible increase in slips, spills, deflections, set pieces and corner-causing clearances;
- therefore **no automatic Under adjustment**.

---

# 12. Scenario / contract map

| Scenario | Representative score | 1H O0.5 | Corners 9+ | FT O2.5 | FT U2.5 |
|---|---:|:---:|:---:|:---:|:---:|
| León early control | León 2-1 | ✅ | ✅ plausible | ✅ | ❌ |
| Tight León win | León 1-0 | ✅/❌ | ✅/❌ | ❌ | ✅ |
| Competitive draw | 1-1 | ✅/❌ | ✅ plausible | ❌ | ✅ |
| Atlante home upset | Atlante 2-1 | ✅ plausible | ✅ plausible | ✅ | ❌ |
| Locked wet match | 0-0 | ❌ | ❌/neutral | ❌ | ✅ |
| Open transition game | 2-2 | ✅ | ✅ likely | ✅ | ❌ |

Dependence warning:
- the goal contracts are exact complements within their own target;
- first-half Over and full-match Over share some early-goal dependence;
- corners are a separate target and are not justified merely by the goal view.

---

# 13. Final ranking

1. **1st Half Over 0.5 Goals**
2. **Total Corners 9+ — Caliente 3-way Over 8**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential regulation winner:** **León — FORCED WINNER / LOW CONFIDENCE**

## Plain-language bottom line

The strongest state is **at least one first-half goal**, driven mainly by León's current early-scoring regime rather than Atlante's baseline.

The best analyst-added corner contract is **9+ total corners**, with Atlante matches currently averaging 11 total corners and León matches 8.6. The exact Caliente 3-way contract is important: eight corners does not push; it is a separate outcome.

The full-match 2.5 total is much closer. I rank the Over slightly ahead because León's attack is currently producing early and through multiple scorers, Romaña's suspension weakens their defensive continuity, and a first goal can open Atlante's home shape. The Under remains an ordinary and material branch because both teams have been Under 2.5 in three of their five league games and the weather/short-rest state can suppress clean execution.

León are the preferred winner, but Atlante's two home draws, León's travel/rest burden and the defensive suspension make that a low-confidence winner call.

No numerical probability, expected value, staking, ROI or market-edge claim is made.

---

# 14. Source register

## Governing framework
- Sports Research / `RULES_SOCCER.md`
- Sports Research / `RULES_GENERAL.md`
- Sports Research / `AGENT_ROLE_AND_TASK.md`
- Sports Research / `PREDICTION_LOG_COMBINED.md`

## Event / current state
- TUDN — Atlante vs León preview / Jornada 6:
  https://www.tudn.com/futbol/liga-mx/a-que-hora-y-donde-ver-el-partido-atlante-vs-leon-de-la-liga-mx-apertura-2026
- TUDN match centre:
  https://www.tudn.com/futbol/liga-mx/atlante-vs-leon-liga-mx-ap-2026-08-28
- AS — Jornada 6 / live match page:
  https://mexico.as.com/resultados/futbol/mexico_apertura/2026/directo/regular_a_6_6a2d4a0547eb864/
- AS — same-day lineup feed:
  https://chile.as.com/resultados/futbol/mexico_apertura/2026/directo/regular_a_6_6a2d4a0547eb864/alineaciones/

## Current process / results
- FBref Liga MX 2026-27 results and fixtures:
  https://fbref.com/en/comps/31/2026-2027/schedule/2026-2027-Liga-MX-Scores-and-Fixtures
- MLS / Leagues Cup Club León current tournament page:
  https://www.mlssoccer.com/clubs/club-leon/
- TUDN — Romaña red card vs Monterrey:
  https://www.tudn.com/futbol/liga-mx/roja-para-leon-romana-derriba-a-ocampos-y-deja-a-la-fiera-con-10-video/

## Corner process / exact analyst-added contract
- WinDrawWin — current Liga MX corner table:
  https://www.windrawwin.com/statistics/corners/mexico-liga-mx/
- Caliente — Atlante vs León corner markets:
  https://sports.caliente.mx/es_MX/Liga-MX/2026-08-28/Atlante-vs-Leon?mkt_grp_code=CRNRS

## External market sanity check
- Caliente — Atlante vs León:
  https://sports.caliente.mx/es_MX/Liga-MX/2026-08-28/Atlante-vs-Leon

## Weather
- Met Office — Mexico City:
  https://weather.metoffice.gov.uk/forecast/9g3qrx3cs
- El Universal report quoting CDMX SGIRPC:
  https://www.eluniversal.com.mx/metropoli/clima-cdmx-a-que-hora-se-esperan-lluvias-y-granizo-este-viernes-28-de-agosto/

# P-152 (conversation-local continuation) — Necaxa vs Cruz Azul — Liga MX Apertura 2026

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Full Match Over 2.5 Goals** | `LEAN` | `MEDIUM` |
| **2** | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **3** | **Total Corners 9+ — Caliente 3-way Over 8** | `FORCED RANK` | `MEDIUM-LOW` |
| **4** | **Full Match Under 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` |
| **5** | **1st Half Under 0.5 Goals** | `AVOID / FORCED RANK` | `MEDIUM-LOW` |

**Potential regulation winner:** **Cruz Azul — FORCED WINNER / LOW CONFIDENCE**

### Central regulation score family
- Cruz Azul 2-1
- 2-2
- 1-1
- Necaxa 2-1
- Cruz Azul 2-0 as the principal controlled-away-win branch
- 0-0 / 1-0 as the principal low-event tail

### Central first-half family
- 0-1 Cruz Azul
- 1-0 Necaxa
- 0-0
- 1-1

---

## Administrative / framework status

**Method:** `MDS-2026.08.29-v2.5`  
**Soccer module:** `RULES_SOCCER.md`, effective 2026-08-29  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate origin:** `USER_SUPPLIED + ANALYST_ADDED_CORNER_MARKET`  
**Operator:** not supplied by user; Caliente is used only to freeze the analyst-added corner contract and as an external market sanity check.  
**Canonical Drive state:** the Drive combined log has not been edited. This is a conversation-local continuation after P-151.

---

# 1. Event identity and state

- **Competition:** Liga MX — Apertura 2026
- **Round:** Jornada 6
- **Match:** Necaxa vs Cruz Azul
- **Venue:** Estadio Victoria, Aguascalientes
- **Scheduled kickoff:** Friday 28 August 2026, 19:00 Central Mexico
- **Melbourne equivalent:** Saturday 29 August 2026, 11:00 AEST
- **Frozen research cutoff:** approximately Saturday 29 August 2026, 10:50 AEST / Friday 28 August 2026, 18:50 Central Mexico
- **GAME-STATE:** `PREGAME`

Both Club Necaxa's official calendar and Cruz Azul's official preview list the fixture for Friday 28 August at 19:00 at Estadio Victoria.

---

# 2. Target and contract freeze

## Target A — first-half goals

`TARGET_ID: SOC-MEX-LIGAMX-2026-NEC-CAZ-1H-GOALS-v1`

Outcome: combined goals from kickoff through 45 minutes plus official first-half stoppage time.

Contracts:
- **Over 0.5** wins with one or more first-half goals.
- **Under 0.5** wins only at 0-0 HT.
- No push.

## Target B — regulation full-match goals

`TARGET_ID: SOC-MEX-LIGAMX-2026-NEC-CAZ-REG-GOALS-v1`

Outcome: joint regulation score through 90 minutes plus stoppage time.

Contracts:
- **Over 2.5** wins on 3+ total goals.
- **Under 2.5** wins on 0-2 total goals.
- No push.

## Target C — total corners

`TARGET_ID: SOC-MEX-LIGAMX-2026-NEC-CAZ-CORNERS-v1`

Analyst-added contract:
**Caliente — Tiros de Esquina, 3 Opciones — Over (8).**

Caliente separately lists:
- Over 8
- Exact 8
- Under 8

Therefore this pick requires **9 or more total regulation corners**. Exactly 8 is a separate 3-way result and is not a push.

Because the Drive soccer module requires direct target-event width/cross/block/end-line/clearance evidence before a corner market can be `LEAN` or `SUPPORTED`, the row is capped at `FORCED RANK / MEDIUM-LOW`.

---

# 3. Participant / availability gate

A same-day EL PAÍS / AS result feed exposed starting lineups, but a field-owner official team-sheet page was not recovered at the cutoff. The following therefore remain **same-day secondary lineups**, not `CONFIRMED_OFFICIAL` under the Drive rules.

## Necaxa — same-day secondary XI
- Luis Jiménez
- Ricardo Monreal
- Carlos Vargas
- Agustín Oliveros
- Alexis Peña
- Kaiky Naves
- Matías Espíndola
- Lorenzo Faravelli
- Owen González
- Julián Carranza
- Daniel Leyva

Coach: Martín Varini.

## Cruz Azul — same-day secondary XI
- Kevin Mier
- Ángel Márquez
- Omar Campos
- Jesús Orozco Chiquete
- José Paradela
- Willer Ditta
- Agustín Palavecino
- Andrés Montaño
- Christian Ebere
- Nicolás Ibáñez
- Carlos Rodríguez

Coach: Joel Huiqui.

### Material availability
Current injury/availability reporting lists:
- **Gonzalo Piovi** unavailable with a hamstring injury.
- **Carlos Rotondi** unavailable/doubtful with a foot issue.
- **Amaury Morales** unavailable with a knee injury.
- **Kevin Rosero** doubtful for Necaxa.

The current listed Cruz Azul XI already reflects a changed defensive/wing structure without Piovi and Rotondi.

Participant-sensitive claims remain capped because the final field-owner lineup handshake was incomplete.

---

# 4. Current league baseline

## Necaxa

Current Liga MX sample:
- **1.4 goals scored per match**
- **1.6 conceded**
- **0 clean sheets in 5**
- approximately **3.0 combined goals per match**

First-half split:
- **0.2 scored in 1H**
- **0.6 conceded in 1H**
- home 1H scoring: **0 goals in 3 home matches**
- home 1H conceded: **1 goal in 3**
- home 1H combined average: about **0.33**

Second-half split:
- **1.2 scored per match**
- **1.0 conceded**
- Necaxa are therefore strongly second-half weighted.

Latest official result:
- **Pumas 1-1 Necaxa**
- HT **0-0**
- Julián Carranza scored at 75'
- Pumas equalised late.

Necaxa have scored in every league game in the current FootyStats sample, but have also conceded in every league game.

## Cruz Azul

Current Liga MX sample:
- **1.6 goals scored per match**
- **2.0 conceded**
- **0 clean sheets in 5**
- approximately **3.6 combined goals per match**

First-half split:
- **0.4 scored in 1H**
- **1.0 conceded in 1H**
- Cruz Azul have conceded five first-half goals across five current league matches in the cited sample.

Second-half split:
- **1.2 scored**
- **1.0 conceded**

Current league path:
- Atlético San Luis 2-3 Cruz Azul
- Cruz Azul 2-1 Puebla
- Cruz Azul 2-3 Atlante
- Tijuana 2-1 Cruz Azul
- Cruz Azul 0-2 Atlas

That is:
- **4 of 5 matches at 3+ goals**
- three consecutive league defeats entering this fixture
- 8 goals scored and 10 conceded across the five-match sample.

Against Atlas, Cruz Azul conceded in the **30th and 45th minutes**, entering halftime down 0-2.

---

# 5. Rank #1 — Full Match Over 2.5 Goals

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM`

This is the strongest supplied direction.

## Why

### Both teams have zero current league clean sheets
Necaxa:
- 7 scored / 8 conceded in the five-match statistical sample.

Cruz Azul:
- 8 scored / 10 conceded.

The strongest mechanism is therefore not simply recent Over results; it is that **both teams are simultaneously creating enough to score while failing to suppress opponent scoring**.

### Cruz Azul's current games are high-variance
Four of their five league games cleared 2.5:
- 3-2 at San Luis
- 2-1 Puebla
- 2-3 Atlante
- 1-2 Tijuana

Only the latest 0-2 Atlas loss stayed Under.

### Necaxa's scoring is late
Necaxa average only 0.2 first-half goals but 1.2 in the second half. That means a restrained opening does not eliminate the full-game Over. It can instead create a 0-0 / 0-1 HT state that expands after substitutions and score-state pressure.

### Current defensive personnel
Cruz Azul are operating without Piovi and with Rotondi unavailable/doubtful. That widens the opponent-scoring branch and reduces confidence in a clean away-control state.

## Strongest kill path

The biggest Under path is:
- Necaxa reproduce their 0-0 HT structure;
- Cruz Azul's attacking crisis persists;
- Cruz Azul control possession without converting;
- the match finishes 1-0, 1-1 or 2-0.

The latest Cruz Azul match — a 0-2 defeat — proves that poor attacking conversion can coexist with defensive vulnerability.

Still, the total event tree favours three or more goals more than two or fewer.

---

# 6. Rank #2 — 1st Half Over 0.5 Goals

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This is weaker than the full-match Over.

## Over mechanisms

Cruz Azul have recently been involved in early scoring:
- Puebla scored at 28' and Luka Romero equalised at 44'.
- Atlas scored at 30' and again at 45'.

Their current first-half concession average is **1.0 per match**.

Necaxa's home early scoring is poor, but Cruz Azul's current defence creates a credible route for Carranza/Monreal/Faravelli-led attacks to generate the first goal.

Cruz Azul also retain Ibáñez, Paradela, Palavecino, Montaño and Charly Rodríguez in the same-day secondary XI, preserving enough attacking quality for the opposite early-goal branch.

## Why it is not #1

Necaxa's home 1H profile is very slow:
- 0 goals scored across three home first halves;
- only 1 conceded;
- combined home 1H average about 0.33.

Their latest match against Pumas was also 0-0 at halftime.

So 0-0 remains a strong ordinary state.

---

# 7. Rank #3 — Total Corners 9+ (Caliente 3-way Over 8)

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

## Exact contract

Caliente:
- Over 8
- Exact 8
- Under 8

This pick wins at **9+ total corners**.

## Direct corner-rate evidence

Current-season FootyMetrics snapshot:
- Liga MX: **10.37 total corners per match**
- league Over 8.5: **63%**
- Cruz Azul: **6.00 corners won per match** in the available current-season sample
- Necaxa: **5.67 corners won**
- both concede approximately **4.00 corners per match** in that snapshot
- Cruz Azul matches average **10.00 corners**
- Necaxa matches average **9.67 corners**

Broader rolling data:
- Necaxa approximately **4.9 corners for / 5.2 conceded**, about **10.0 combined**
- Cruz Azul approximately **5.6 for / 3.8 conceded**, about **9.5 combined**

The line is therefore close to the current centre but below the league's 10.37 baseline.

## Mechanism

- Cruz Azul's possession/territory game creates repeated wide and second-phase entries even when finishing is poor.
- Necaxa at home produce a respectable corner volume and their current attackers can create chase-state pressure.
- If either side trails, the losing team's required attacking volume should remain high.

## Why the evidence cap remains

The exact provider definition is resolved, but the exact current-XI:
- cross frequency
- blocked-cross frequency
- end-line entry
- defensive clearance
- set-piece creation

chain was not fully recovered under one current provider.

The Drive derivative-completeness rule therefore blocks a `LEAN`.

---

# 8. Rank #4 — Full Match Under 2.5 Goals

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This is the principal full-game contrary branch.

## Under mechanisms
- Necaxa's opening phases are slow.
- Cruz Azul were shut out by Atlas last week.
- Aguascalientes weather is forecast dry and relatively stable, so there is no weather-driven chaos requirement.
- A 1-1 state is very plausible if both teams continue to create only moderate-quality chances.

## Why it is below the Over
Cruz Azul's zero-clean-sheet start, Necaxa's zero-clean-sheet start, and Cruz Azul's 4/5 Over-2.5 current league pattern collectively keep the higher-event score tree in front.

---

# 9. Rank #5 — 1st Half Under 0.5 Goals

**Verdict:** `AVOID / FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This is not a dead bottom pick.

The strongest Under evidence in the entire card is Necaxa's home opening-state profile:
- 0 first-half home goals scored in three games;
- only 1 conceded;
- latest league match 0-0 HT.

The reason it still ranks fifth is Cruz Azul's recent inability to protect the opening 45:
- Puebla scored at 28'
- Atlas scored at 30' and 45'
- current 1H concession average is 1.0.

The pair is close enough that the Over is a forced marginal preference rather than a strong lean.

---

# 10. Potential regulation winner — Cruz Azul

**Status:** `FORCED WINNER — LOW CONFIDENCE`

## Why Cruz Azul

- The available external market prices Cruz Azul as the away favourite.
- Their attacking baseline is higher than Necaxa's: **1.6 vs 1.4 goals per match**.
- Cruz Azul's current listed attacking/midfield group still includes Nicolás Ibáñez, Christian Ebere, Paradela, Palavecino, Montaño and Carlos Rodríguez.
- The club are reigning champions and have shown a high attacking ceiling, including a 3-2 away comeback against San Luis.

## Why this is low confidence

Cruz Azul are entering on **three straight league defeats**:
- 2-3 Atlante
- 1-2 Tijuana
- 0-2 Atlas

The Atlas defeat exposed a real current-regime problem rather than a single unlucky result; Atlas led 2-0 by halftime.

Necaxa are only one point above Cruz Azul in the table entering the round and drew 1-1 at Pumas last time out.

Cruz Azul's defence is also missing important continuity because Piovi is unavailable and Rotondi is not in the same-day listed XI.

Therefore the winner order is:
1. Cruz Azul
2. Draw
3. Necaxa

but the separation is not large enough for a high-confidence side call.

---

# 11. Weather

Current Aguascalientes match-window forecast:
- around **26°C / 78°F at 19:00**
- approximately **0% rain**
- ENE wind around **13 mph / 21 km/h**
- mostly sunny to partly cloudy.

Weather is therefore not a material reason to move the goal or corner ranking.

---

# 12. Scenario / contract map

| Scenario | Representative score | 1H O0.5 | Corners 9+ | FT O2.5 | FT U2.5 |
|---|---:|:---:|:---:|:---:|:---:|
| Cruz Azul regain attacking control | CAZ 2-1 | ✅ likely | ✅ plausible | ✅ | ❌ |
| Open defensive game | 2-2 | ✅ | ✅ | ✅ | ❌ |
| Controlled draw | 1-1 | mixed | mixed | ❌ | ✅ |
| Necaxa home upset | NEC 2-1 | ✅/mixed | ✅ plausible | ✅ | ❌ |
| Cruz Azul low-event win | CAZ 2-0 | mixed | mixed | ❌ | ✅ |
| Locked first half / low conversion | 0-0 / 1-0 | ❌ | lower | ❌ | ✅ |

Dependence:
- 1H Over and FT Over share early-goal dependence but are different horizons.
- FT Over and FT Under are exact complements.
- 1H Over and 1H Under are exact complements.
- Corners remain a separate target and are not justified by goals alone.

---

# 13. Final ranking

1. **Full Match Over 2.5 Goals — LEAN / MEDIUM**
2. **1st Half Over 0.5 Goals — FORCED RANK / MEDIUM-LOW**
3. **Total Corners 9+ — Caliente 3-way Over 8 — FORCED RANK / MEDIUM-LOW**
4. **Full Match Under 2.5 Goals — FORCED RANK / MEDIUM-LOW**
5. **1st Half Under 0.5 Goals — AVOID / FORCED RANK / MEDIUM-LOW**

**Potential regulation winner:** **Cruz Azul — FORCED WINNER / LOW CONFIDENCE**

## Plain-language bottom line

The strongest position is **Over 2.5 goals**. Necaxa and Cruz Azul have both failed to keep a league clean sheet, Cruz Azul's five league matches average 3.6 goals, and four of five have cleared 2.5.

The first-half market is much tighter. Necaxa are unusually slow at home before halftime, but Cruz Azul have recently conceded early and entered halftime 0-2 against Atlas. I therefore rank **1H Over 0.5** above the Under, but only narrowly.

The best added corner market is **9+ total corners**. Current Liga MX corner averages sit above 10 per match and both Necaxa and Cruz Azul generate roughly 5.5-6 corners themselves in the available season sample. It remains capped because the exact cross/block/end-line chain is incomplete.

Cruz Azul are the potential winner, but their three straight league losses and current defensive absences make the side call low confidence.

No internally generated probability, expected value, staking, ROI or market-edge claim is made.

---

# 14. Source register

## Governing Drive framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- `AGENT_ROLE_AND_TASK.md`
- `PREDICTION_LOG_COMBINED.md`

## Official / primary
1. Cruz Azul official preview — Necaxa-Cruz Azul, J6 AP26  
   https://cfcruzazul.com/previa-necaxa-cruz-azul-liga-mx-j6-ap26/
2. Club Necaxa official calendar  
   https://clubnecaxa.mx/partidos/calendario/APERTURA-2026
3. Pumas official match report — Pumas 1-1 Necaxa  
   https://pumas.mx/noticias/3647/pumas-empata-1-1-contra-necaxa-en-cu
4. Cruz Azul official Atlas match report  
   https://cfcruzazul.com/cronica-cruz-azul-atlas-liga-mx-j5-ap26/
5. Cruz Azul official AP26 J1 / J2 reports  
   https://cfcruzazul.com/cronica-atletico-san-luis-cruz-azul-liga-mx-j1-ap26/  
   https://cfcruzazul.com/cronica-cruz-azul-puebla-liga-mx-j2-ap26/

## Same-day lineup / participant research
6. EL PAÍS / AS same-day lineup page  
   https://elpais.com/deportes/resultados/futbol/mexico_apertura/2026/directo/regular-a-6-6a2d4a0547eba52/alineaciones/
7. FotMob injury / lineup research
8. 365Scores lineup/availability research

## Statistical research
9. FootyStats — Necaxa 2026/27  
   https://footystats.org/clubs/club-necaxa-1428
10. FootyStats — Cruz Azul 2026/27  
    https://footystats.org/clubs/cruz-azul-fc-1432
11. FootyMetrics Liga MX corner statistics  
    https://www.footymetrics.com/statistics/corners/mexico-liga-mx
12. CornerEdge rolling Necaxa / Cruz Azul corner samples

## Exact analyst-added corner contract / external sanity check
13. Caliente — Necaxa vs Cruz Azul  
    https://sports.caliente.mx/es_MX/Liga-MX/2026-08-28/Necaxa-vs-Cruz-Azul

## Weather
14. Weather.com — Aguascalientes hourly forecast

# P-153 (conversation-local continuation) — Minnesota Vikings @ Denver Broncos — NFL Preseason Week 3, 2026

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Combined Total Under 37.5 Points** | `FORCED RANK` | **MEDIUM-LOW** |
| **2** | **Denver Broncos -3.5** | `FORCED RANK` | **MEDIUM-LOW** |
| **3** | **Minnesota Vikings +3.5** | `FORCED RANK` | **MEDIUM-LOW** |
| **4** | **Combined Total Over 37.5 Points** | `AVOID / FORCED RANK` | **MEDIUM-LOW** |

**Potential winner:** **Denver Broncos — FORCED WINNER / LOW CONFIDENCE**

### Central score family
- **Denver 17-13**
- **Denver 20-13**
- **Denver 17-14**
- Minnesota 17-16 as the principal Vikings-upset branch
- Denver 20-17 as the primary Under-loss / close-game boundary branch
- Denver 24-17 as the main Over-and-cover branch

---

## Administrative / framework status

**Method:** `MDS-2026.08.29-v2.5`  
**Sport module:** `RULES_AMERICAN_FOOTBALL.md`  
**Competition phase:** NFL PRESEASON — separate phase model  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate origin:** `USER_SUPPLIED`  
**Operator:** `NOT SUPPLIED`  
**Spread/total prices:** not supplied; no EV/value/ROI claim is made.

The Drive football module explicitly requires quarterback/unit rotation and expected reps in preseason rather than regular-season team power ratings.

---

# 1. Event identity and state

- **Competition:** NFL Preseason
- **Week:** Preseason Week 3 / preseason finale
- **Match:** Minnesota Vikings @ Denver Broncos
- **Venue:** Empower Field at Mile High, Denver, Colorado
- **Scheduled kickoff:** Friday 28 August 2026, 7:00 p.m. MDT / 9:00 p.m. ET
- **Melbourne equivalent:** Saturday 29 August 2026, 11:00 a.m. AEST
- **Final research refresh:** immediately after scheduled start time
- **Official state at final refresh:** `PREGAME / CREATED — Q1 15:00, no score posted`
- **GAME-STATE:** `PREGAME AT FINAL VERIFIED REFRESH`

The scheduled start crossed during research, so the state was refreshed under the Drive start-crossing rule. The NFL game feed still showed Q1 15:00 with no score and no live play, so the issued ranking remains a pregame card rather than a live-adjusted forecast.

---

# 2. Contract freeze

## Side target

`TARGET_ID: NFL-2026-PRE-W3-MIN-DEN-MARGIN-v1`

Outcome: Denver regulation/preseason final score minus Minnesota final score under the operator's standard full-game preseason settlement.

User-supplied exact-complement pair:
- Vikings +3.5
- Broncos -3.5

There is no push at a half-point line.

## Total target

`TARGET_ID: NFL-2026-PRE-W3-MIN-DEN-TOTAL-v1`

Outcome: combined final game points.

User-supplied exact-complement pair:
- Over 37.5
- Under 37.5

There is no push at a half-point line.

**Operator overtime/void terms:** `UNKNOWN_DEFINITION` because no sportsbook/operator was supplied.

---

# 3. Quarterback / participation gate

Preseason quarterback exposure is the decisive regime variable.

## Denver

Official Broncos reporting:
- Head Coach Sean Payton said **Bo Nix "probably won't play"** in the finale.
- Nix played only 14 snaps against Green Bay and led two scoring drives.
- If Nix sits, the material quarterback phases are **Jarrett Stidham** and **Sam Ehlinger**.

Official preseason quarterback production:
- Stidham vs Atlanta: 9/15, 131 yards, 1 TD, 0 INT.
- Stidham vs Green Bay: 9/15, 82 yards, 0 TD, 1 INT.
- Ehlinger vs Atlanta: 10/14, 67 yards, 0 TD.
- Ehlinger vs Green Bay: 2/2, 10 yards, 0 TD, while taking two sacks.

Denver therefore has a relatively predictable reserve-QB structure, but its scoring ceiling drops sharply from the Nix-led opening phase seen against Green Bay.

**Participation status:** Bo Nix = `PROBABLE_OFFICIAL TO SIT`, not confirmed inactive.

## Minnesota

Official Vikings reporting:
- **Kyler Murray will be rested.**
- J.J. McCarthy was dealing with an ankle injury and did not practice Wednesday.
- Kevin O'Connell said Carson Wentz and Max Brosmer were expected to play.

Same-day secondary reporting says **McCarthy will not play** because of the ankle issue.

Therefore the central branch is:
- **Carson Wentz**
- followed by **Max Brosmer**

but because the final field-owner starter/reps release was not recovered, this remains an unresolved participant gate.

Official current preseason production:
- Wentz vs Giants: 9/14, 81 yards, 1 TD, 0 INT.
- Wentz vs Ravens: 9/11, 92 yards, 0 TD, 0 INT.
- Brosmer vs Ravens: 11/17, 98 yards, 0 TD, 1 INT.
- McCarthy vs Ravens: 5/10, 81 yards, 0 TD.

**Participation status:** Murray = official rest; McCarthy = `SECONDARY_ONLY OUT / OFFICIAL STATUS UNRESOLVED`; Wentz/Brosmer expected.

Because the quarterback exposure is not fully confirmed by the field-owning source, all four supplied rows are conservatively capped at `FORCED RANK / MEDIUM-LOW`.

---

# 4. Offensive / line / drive process

## Minnesota offense

Minnesota's two preseason results:
- Vikings 13, Giants 10
- Ravens 13, Vikings 3

Minnesota has therefore scored:
- **16 points across 8 preseason quarters**
- only one offensive touchdown across the two games.

The important mechanism is not just the raw points.

Against Baltimore:
- Minnesota's reserve offensive line allowed **five sacks and nine quarterback hits**.
- The Vikings committed nine penalties, including six on offense.
- The offense lost two turnovers.
- Minnesota's run game produced very few explosives.

Wentz has been individually efficient, but repeated negative plays, protection leakage and penalties have prevented that efficiency from becoming sustained touchdown drives.

Brosmer moved the ball late against Baltimore but ended a 57-yard, 11-play drive with an interception.

That creates a preseason scoring profile dominated by:
- field goals,
- stalled drives,
- sacks/penalties,
- and low red-zone touchdown conversion.

## Denver offense

Denver's preseason:
- Broncos 27, Falcons 7
- Packers 33, Broncos 13

The 27-point Atlanta score overstates the repeatable offensive baseline because Denver also had a 97-yard defensive interception return touchdown.

Against Green Bay:
- Bo Nix led the first two possessions to 10 points.
- Denver finished with only 13 points.
- Stidham went 9/15 for 82 yards with an interception.
- Ehlinger had only two pass attempts and took two sacks.
- Denver rushed for only 65 yards in the official box score and averaged a low yards-per-carry rate across the backs.

Without Nix, the expected offense is therefore closer to the Stidham/Ehlinger reserve regime than the Nix-led opening phase.

Stidham showed a functional ceiling in Atlanta, but his Green Bay performance demonstrates meaningful downside.

---

# 5. Rank #1 — Under 37.5 Points

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This is the strongest of the four supplied contracts.

## Primary Under mechanisms

### 1. Minnesota's preseason offense has not generated touchdowns
The Vikings scored only 13 and 3 points in two games, with one offensive touchdown.

Wentz can move the chains, but the reserve-line pressure/penalty environment has repeatedly ended drives before they become touchdowns.

### 2. Denver likely removes its highest-ceiling QB phase
Nix led **both** Denver scoring drives to start the Green Bay game.

If he sits as Payton expects, the full game shifts to Stidham/Ehlinger:
- Stidham has one strong and one weak exhibition.
- Ehlinger has not thrown a preseason TD in the current two-game sample.

### 3. Preseason finale phase
Both clubs are evaluating reserve players shortly before final roster cuts. The football module treats this as a separate phase:
- more reserve OL combinations;
- more third-/fourth-string skill exposure;
- less stable red-zone execution;
- greater drive-killing penalty/assignment-error risk.

### 4. Minnesota defense has been competent with reserves
Minnesota has allowed only:
- 10 points to the Giants
- 13 to Baltimore

The Vikings' defensive depth kept both games well below 37.5.

## Central Under scores
- Denver 17-13 = 30
- Denver 20-13 = 33
- Denver 17-14 = 31
- Minnesota 17-16 = 33

## Strongest kill paths
The Under can fail through:
- defensive/special-teams touchdowns;
- repeated short fields from reserve-QB turnovers;
- a Denver pressure mismatch generating takeaways;
- late fourth-quarter broken-play explosives between deep reserves;
- overtime if the operator includes it and the game reaches a tie.

Denver already produced a 97-yard pick-six against Atlanta, so non-offensive scoring is a real tail rather than an abstract caveat.

Weather is not a strong Under reason: Denver has only a slight storm chance and moderate wind. The Under is driven by quarterback/line/red-zone phases.

---

# 6. Rank #2 — Broncos -3.5

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This side is much less robust than the Under.

## Why Denver is marginally preferred

### 1. Cleaner full-game QB rotation
If Nix sits:
- Stidham + Ehlinger is a known two-QB reserve sequence.
- Minnesota is expected to use Wentz + Brosmer, with McCarthy's status unresolved at the official-source level.

Stidham's ceiling is meaningful: he produced 131 yards and a TD in one half against Atlanta.

### 2. Minnesota reserve OL pressure vulnerability
Five sacks and nine QB hits against Baltimore are the clearest matchup warning on the Minnesota side.

Denver's reserve defense has already shown:
- pressure,
- takeaway production,
- and the ability to convert a defensive mistake directly into points.

A short field can be decisive in a projected low-total game.

### 3. Home / altitude context
Empower Field at Mile High provides Denver with the familiar altitude and home operation environment. This is a modifier, not a primary edge.

## Why -3.5 is fragile

The central total is low.

At a low total, the difference between:
- Denver 17-13 (**Denver covers by 4**)
- and Denver 17-14 (**Minnesota covers by 3**)

is one scoring event.

Wentz is also the most experienced backup quarterback expected to play. If Minnesota gives him a substantial first-half workload and protects him adequately, the Vikings can stay within one field goal.

Therefore Broncos -3.5 is only a narrow preference over Vikings +3.5.

---

# 7. Rank #3 — Vikings +3.5

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

This exact complement remains a credible branch.

## Vikings-cover mechanisms

- Wentz has completed 18 of 25 preseason passes for 173 yards, 1 TD and 0 INT.
- Minnesota's defense has allowed only 23 combined points through two games.
- A low total naturally compresses margin.
- Denver's offense scored only three points after Nix's two scoring drives against Green Bay.
- Stidham threw an interception in that game and Denver's reserve run game struggled.

If the game follows a 17-14 or 16-14 type state, Minnesota covers even if Denver wins.

## Why it ranks below Denver -3.5

Minnesota's reserve protection problems are more serious than Denver's current offensive inefficiency because they can create:
- sacks,
- field-position losses,
- turnovers,
- and short-field Denver scoring.

Brosmer is also a lower-floor late-game phase than Wentz.

---

# 8. Rank #4 — Over 37.5 Points

**Verdict:** `AVOID / FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

The Over needs the game to leave the central reserve-QB efficiency band.

## Over pathways

- Denver defensive or special-teams touchdown.
- Multiple turnovers creating short fields.
- Stidham reproduces the Atlanta first-half performance.
- Minnesota's Wentz phase scores efficiently and Brosmer avoids mistakes.
- Deep-reserve coverage busts generate 40+ yard plays.
- A tie creates overtime scoring under applicable operator rules.

## Why it ranks fourth

Minnesota's two preseason totals:
- 23
- 16

Denver's two:
- 34
- 46

But Denver's 46-point game against Green Bay included a Nix phase that is unlikely to exist here, while the Atlanta game included a Denver defensive touchdown.

The repeatable offensive processes are therefore lower than the raw Denver totals suggest.

The central 30-34 point corridor remains below 37.5.

---

# 9. Potential winner — Denver Broncos

**Status:** `FORCED WINNER — LOW CONFIDENCE`

Denver is the preferred winner because:
- the home team has the clearer reserve-QB rotation;
- Minnesota's reserve offensive line struggled badly against Baltimore pressure;
- Denver's defensive depth has already produced takeaways and non-offensive scoring;
- Minnesota's offense has scored only 16 preseason points.

But this is not a strong winner call because:
- Wentz has been efficient;
- Minnesota's defense has been the stronger stable unit through two exhibitions;
- Denver's offense after Nix was weak against Green Bay;
- preseason snap distributions remain partially unresolved.

Winner order:
1. **Denver**
2. Minnesota

but the margin confidence is low.

---

# 10. Weather / venue context

National Weather Service forecast near Empower Field:
- slight chance of showers/thunderstorms around the evening window;
- generally partly cloudy;
- winds in a moderate range with possible gusts;
- no severe weather condition strong enough to drive the total.

Weather is therefore a secondary variance modifier only.

Altitude may matter more late if reserve lines play extended snaps, but it is not independently sufficient to justify Denver -3.5.

---

# 11. Scenario map

| Scenario | Representative score | MIN +3.5 | DEN -3.5 | O37.5 | U37.5 |
|---|---:|:---:|:---:|:---:|:---:|
| Denver pressure/control | DEN 20-13 | ❌ | ✅ | ❌ | ✅ |
| Tight Denver win | DEN 17-14 | ✅ | ❌ | ❌ | ✅ |
| Low-event Denver cover | DEN 17-13 | ❌ | ✅ | ❌ | ✅ |
| Minnesota defensive upset | MIN 17-16 | ✅ | ❌ | ❌ | ✅ |
| Close higher-scoring game | DEN 20-17 | ✅ | ❌ | ❌ | ✅ |
| Turnover/explosive tail | DEN 24-17 | ❌ | ✅ | ✅ | ❌ |
| High-variance tie/OT branch | 20-20+ | side dependent | side dependent | ✅ | ❌ |

The Under and Denver -3.5 are **not independent**:
- low scoring helps the Under,
- but also increases the importance of the +3.5 / -3.5 boundary.

---

# 12. Final ranking

1. **Combined Total Under 37.5 — FORCED RANK / MEDIUM-LOW**
2. **Denver Broncos -3.5 — FORCED RANK / MEDIUM-LOW**
3. **Minnesota Vikings +3.5 — FORCED RANK / MEDIUM-LOW**
4. **Combined Total Over 37.5 — AVOID / FORCED RANK / MEDIUM-LOW**

**Potential winner:** **Denver Broncos — FORCED WINNER / LOW CONFIDENCE**

## Plain-language bottom line

The cleanest thesis is **Under 37.5**.

Minnesota has scored only 16 points through two preseason games and its reserve offensive line gave up five sacks and nine quarterback hits against Baltimore. Denver is likely removing Bo Nix, whose two drives produced 10 of Denver's 13 points against Green Bay, leaving a Stidham/Ehlinger offense with a lower expected touchdown rate.

The spread is closer. Denver has the more stable quarterback rotation and the clearer pressure mismatch, so I narrowly prefer **Broncos -3.5**, but the low total makes **Vikings +3.5** a very live complement because a 17-14 Denver win loses the favorite contract.

No internally generated probability, price value, expected value, staking recommendation, ROI or market edge is claimed.

---

# 13. Source register

## Governing Drive framework
- `RULES_AMERICAN_FOOTBALL.md`
- `RULES_GENERAL.md`
- `AGENT_ROLE_AND_TASK.md`
- `MODEL_AND_DATA_SPEC.md`
- `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`
- `NUMERICAL_TRAINING_SPEC.md`

## Official current event / participants
1. NFL Game Center — Vikings at Broncos, 2026 PRE Week 3  
   https://www.nfl.com/games/vikings-at-broncos-2026-pre-3
2. Denver Broncos — Game preview vs Minnesota  
   https://www.denverbroncos.com/news/game-preview-what-to-watch-in-broncos-preseason-finale-vs-minnesota-vikings
3. Denver Broncos — Bo Nix "probably won't play"  
   https://www.denverbroncos.com/news/broncos-notebook-qb-bo-nix-probably-won-t-play-vs-vikings
4. Minnesota Vikings — Preseason finale preview  
   https://www.vikings.com/news/previewing-2026-preseason-game-3-broncos
5. Minnesota Vikings — How to watch / QB plan  
   https://www.vikings.com/news/how-to-watch-broncos-2026-preseason-week-3-game

## Official preseason process
6. Minnesota Vikings — Ravens game observations  
   https://www.vikings.com/news/ravens-preseason-game-observations-2026
7. Minnesota Vikings — Giants game observations  
   https://www.vikings.com/news/2026-giants-preseason-game-observations-revamped
8. Denver Broncos — 27-7 win at Atlanta  
   https://www.denverbroncos.com/news/3-things-to-know-from-the-broncos-27-7-preseason-win-over-the-falcons
9. Denver Broncos — Green Bay box score  
   https://www.denverbroncos.com/game-day/2026/pre/packers-at-broncos
10. NFL.com — Jarrett Stidham 2026 preseason log
11. NFL.com — Sam Ehlinger 2026 preseason log

## Weather
12. National Weather Service — Denver point forecast  
    https://forecast.weather.gov/MapClick.php?lat=39.7007844&lon=-105.0031457

## Secondary same-day participation corroboration
13. Daily Norseman — same-day report that J.J. McCarthy will not play.
14. Other same-day reputable reporting used only as corroboration, not to override official participant status.

# P-154 (conversation-local continuation) — Philadelphia Phillies @ Los Angeles Angels — MLB — 2026-08-28

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the current `RULES_BASEBALL.md`, not the structure of any previously attached prediction-log file.

**Method:** `MDS-2026.08.29-v2.5 — qualitative champion`  
**Numerical specification:** `NTS-2026.08.25-v0.2 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate policy:** `USER_SUPPLIED`  
**Operator / exact book rules:** `NOT SUPPLIED`  
**Logging mode:** research + forecast + local Markdown log  
**Canonical Drive note:** the Drive combined log still names `P-137` as its next canonical ID. This is therefore a conversation-local continuation and does not claim to modify or reconcile the read-only Drive log.

---

# 1. Previous-log / queue gate

The active Drive snapshot required the open canonical queue to be refreshed before the new event.

| ID | Event | Refreshed disposition |
|---|---|---|
| `P-126` | Sikkim Aakraman FC vs Sikkim Boys Club | **OPEN — PREGAME / SCHEDULE FIELD-OWNER UNRESOLVED**; current stronger schedule branch is later on 29 Aug Melbourne time |
| `P-135` | Unión de Santa Fe vs Sarmiento | **FINAL — Unión 4-1 Sarmiento**; settlement below |
| `P-136` | James Duckworth vs Arthur Fery | **OPEN — UPCOMING** on the current Tennis.com event page |

## P-135 settlement required before this forecast

**Verified final:** Unión de Santa Fe **4-1** Sarmiento.  
**Half-time:** Unión **1-0** Sarmiento.

Scoring sequence recovered from current match reports:
- Cristian Tarragona 18'
- Cristian Tarragona 61'
- Ignacio Malcorra 74'
- Julián Mavilla 79'
- Eric Ramírez 84'

| Original rank | Frozen P-135 contract | Settlement |
|---:|---|---|
| 1 | Sarmiento Team Total Over 0.5 | **WIN** |
| 2 | 1st Half Over 0.5 | **WIN** |
| 3 | Sarmiento or Draw — X2 | **LOSS** |
| 4 | Total Corners Under 10.5 | **UNRESOLVED — final provider-consistent corner count not recovered in this pass** |
| 5 | Combined Total Over 2.5 | **WIN** |
| — | Potential winner: Sarmiento | **LOSS** |

### P-135 retrospective

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Sarmiento likely to score and remain competitive; early-goal and Over branches live | Unión scored first at 18', then separated 3-0 by 74'; Sarmiento's goal came only after the game was effectively separated | Sarmiento scoring/1H/Over directions survived, but the side/winner branch materially understated ordinary Unión separation | The Unión rebound/control branch was knowable and was present, but was weighted too low; no identity or source defect established | `COMPLIANT` | Branch-weight / winner-separation miss | L-031 / L-033 process reminder only | **None from one result** |

The corner row remains open at field level; the completed score-based rows do not remain ungraded merely because one niche statistic is unresolved.

---

# 2. Event, target, candidate and time freeze

## Official event

| Field | Frozen value |
|---|---|
| Sport | Baseball |
| Competition | Major League Baseball — 2026 regular season |
| Official event | Philadelphia Phillies @ Los Angeles Angels |
| MLB gamePk | `823985` |
| Venue | Angel Stadium, Anaheim, California |
| Away / home | Philadelphia away; Los Angeles home |
| Scheduled start | 2026-08-28 18:38 PDT / 21:38 EDT |
| Melbourne start | 2026-08-29 11:38 AEST |
| State at final volatile refresh | **`GAME-STATE: PREGAME`** |
| Scheduled innings | 9 |
| DH | Universal MLB DH |
| Home-last-bat | Angels hold conditional bottom-9th entitlement |
| Extra innings | Current MLB automatic-runner regime; exact sportsbook inclusion/void terms not supplied |
| Evidence cutoff | 2026-08-29 approximately 11:25 AEST, before scheduled first pitch |

## Decision set

`DECISION_SET_ID: DS-P154-V01`

| Candidate ID | Frozen contract | Eligible | Geometry |
|---|---|:---:|---|
| `P-154-C01` | Philadelphia Phillies +1.5 runs | YES | Overlaps C02 on an exact one-run final |
| `P-154-C02` | Los Angeles Angels +1.5 runs | YES | Overlaps C01 on an exact one-run final |
| `P-154-C03` | Combined Total Over 7.5 runs | YES | Exact complement of C04 |
| `P-154-C04` | Combined Total Under 7.5 runs | YES | Exact complement of C03 |

### Target 1 — final margin

`TARGET_ID: MLB-2026-823985-MARGIN-v1`

Outcome: `Phillies final runs - Angels final runs`.

- Phillies +1.5 wins if Philadelphia wins or loses by exactly one.
- Phillies +1.5 loses only if Los Angeles wins by **2+**.
- Angels +1.5 wins if Los Angeles wins or loses by exactly one.
- Angels +1.5 loses only if Philadelphia wins by **2+**.
- **Both +1.5 contracts win in every one-run final.**

This is a key structural property: these two rows are **not opposites**.

### Target 2 — total runs

`TARGET_ID: MLB-2026-823985-TOTAL-RUNS-v1`

Outcome: combined final runs under the full-game research definition.

- Over 7.5 wins at **8+**
- Under 7.5 wins at **0-7**
- No push at 7.5.

**Bookmaker action / listed-pitcher / extra-innings rules:** `UNKNOWN_DEFINITION` because the user did not supply an operator. Research assumes the normal full MLB game, but an actual ticket must be governed by its operator's terms.

---

# 3. Final participant identity handshake

## Philadelphia starter

**Andrew Painter — RHP**  
Status: `CONFIRMED_OFFICIAL` for the research card through MLB's current event/probable-pitcher and lineup pages.

Current MLB line:
- 3-8
- 6.04 ERA
- 79 strikeouts

## Los Angeles starter

**Reid Detmers — LHP**  
Status: `CONFIRMED_OFFICIAL` for the research card through MLB's current event/probable-pitcher and lineup pages.

Current MLB line:
- 4-8
- 3.62 ERA
- 172 strikeouts
- 149.0 innings
- 1.06 WHIP

## Posted Philadelphia order

1. Kyle Schwarber — DH, L
2. Trea Turner — SS, R
3. Bryce Harper — RF, L
4. Luis Arraez — 2B, L
5. Alec Bohm — 1B, R
6. Bryan De La Cruz — LF, R
7. Bryson Stott — 3B, L
8. J.T. Realmuto — C, R
9. Derek Hill — CF, R

## Posted Los Angeles order

1. Zach Neto — SS, R
2. Mike Trout — CF, R
3. Wade Meckler — LF, L
4. Vaughn Grissom — 1B, R
5. Moisés Ballesteros — DH, L
6. Christian Moore — 2B, R
7. Josh Lowe — RF, L
8. Denzer Guzman — 3B, R
9. Tyler Heineman — C, S

The exact orders matter. Philadelphia does not simply present a left-handed lineup to Detmers: Turner, Bohm, De La Cruz, Realmuto and Hill provide right-handed plate appearances around the left-handed stars. Los Angeles starts its two most established current bats, Neto and Trout, at the top against Painter.

---

# 4. D0 mechanism retrieval

### Predeclared query

`MLB pregame full-game side/total cards -> opposite-team +1.5 overlap -> uncertain or small-sample starter regime -> bullpen/HR separation tail -> standard nine-inning game`

### Retained comparable

**P-064 — Texas Rangers @ Chicago White Sox**

Why retained:
- same two positive +1.5 contracts;
- same need to distinguish one-run overlap from 2+ separation;
- starter uncertainty and HR/contact tail were central;
- full-game total linked to the same joint run corridor.

Why it is not a result vote:
- different pitchers, lineups, park, bullpens and threshold;
- its eventual outcome is not used as evidence for Philadelphia or Los Angeles;
- it is retained only to enforce cushion decomposition and the HR/early-hook tail.

**Eligible retained count:** 1.  
No raw analogue win rate is calculated.

---

# 5. Competition / venue baseline

Angel Stadium is not treated as an extreme run-suppressing park.

Baseball Savant's current one-year 2026 park-factor view places Angel Stadium in a pitcher-friendlier current-year state, with:
- overall park factor approximately 93-94;
- run factor in the high-80s on the retrieved current-year view.

But the **2024-2026 rolling view is approximately neutral at 100**.

Therefore the forecast uses:
- a modest current-year suppression branch;
- a neutral rolling park prior;
- no assumption that Angel Stadium alone forces an Under.

## Weather

National Weather Service forecast for Anaheim:
- mostly clear;
- low around 73°F;
- southwest wind around 5 mph becoming calm;
- no material precipitation issue.

Weather is effectively **neutral** for the total. It does not create the Under direction.

---

# 6. Philadelphia batting process vs Reid Detmers

Philadelphia enters with one of MLB's strongest current monthly offensive regimes.

Current MLB August team data:
- 24 games
- 131 runs
- .273 AVG
- .356 OBP
- .417 SLG
- .773 OPS

That is roughly **5.5 runs per game** in the retrieved August sample, but the raw average is not projected directly against Detmers.

## Detmers current regime

The season baseline is strong:
- 3.62 ERA
- 1.06 WHIP
- 172 K in 149 IP.

More importantly, his current seven-start regime has been materially better:
- **1.56 ERA**
- **0.84 WHIP**
- 40.1 innings
- 49 strikeouts.

Latest three:
- 6 IP, 1 ER, 6 K vs Texas on Aug 10
- 8 IP, 0 ER, 11 K vs Kansas City on Aug 15
- 6 IP, 0 ER, 5 K at Texas on Aug 21.

This creates the strongest suppression mechanism in the game.

### Baseline/current-regime reconciliation

The forecast does **not** mechanically assume that Detmers' last three starts continue unchanged.

Central Detmers branch:
- controls strike zone and misses enough bats to suppress clusters;
- works roughly through the middle/late starter phase;
- Philadelphia still generates traffic because its current order is deep.

Good Detmers tail:
- 6-7+ efficient innings;
- 0-1 runs;
- multiple strikeout escape sequences.

Adverse Detmers tail:
- Philadelphia's right-handed counters and Schwarber/Harper power create a multi-run or HR cluster;
- elevated pitch count forces earlier bullpen exposure.

Detmers is the primary reason the total does not become a strong Over despite Philadelphia's August offense.

---

# 7. Los Angeles batting process vs Andrew Painter

Painter's surface ERA materially overstates his Statcast expected-run estimate, but his underlying profile remains volatile.

Current Baseball Savant:
- 6.04 ERA
- **4.81 xERA**
- .261 xBA
- .439 xSLG
- .336 xwOBA
- 36.6% HardHit
- 19.3% K
- 8.3% BB
- 8.6% Barrel rate.

His fastball has been the central weakness:
- four-seamer ~32% usage;
- opposing .363 BA / .613 SLG on the retrieved pitch table;
- .410 xwOBA;
- only 14.2% whiff.

He has better miss weapons:
- slider and splitter generate materially higher whiff/strikeout rates.

## Current-regime branch

Painter's most recent outing was easily his best MLB start:
- career-high 7 innings;
- 1 run;
- 8 strikeouts;
- 20 swinging strikes;
- first 100-pitch game.

That outing matters as evidence that the upper/good-start tail is real. It does **not** erase:
- the 6.04 season ERA;
- below-average strikeout rate;
- fastball damage;
- young/small-sample MLB starter uncertainty.

The baseball rules explicitly require this kind of starter to retain a mixture.

### Painter mixture

**Good branch**
- recent command/whiff gains persist;
- slider/splitter finish counts;
- 6-7 innings, limited traffic.

**Ordinary branch**
- 5-6 innings;
- several baserunners;
- roughly 2-3 run exposure before the relief chain.

**Early-hook/contact branch**
- Neto/Trout or the right-handed middle order attack fastball mistakes;
- one HR or sequencing cluster forces an earlier hook;
- Philadelphia must cover 4+ bullpen innings.

This tail is the main reason Over 7.5 remains very live despite Los Angeles' current offensive weakness.

---

# 8. Los Angeles current batting regime

The Angels' August offense is materially weaker than Philadelphia's.

Current MLB August line:
- 24 games
- 82 runs
- .221 AVG
- .289 OBP
- .327 SLG
- **.616 OPS**
- 226 strikeouts.

That is approximately 3.4 runs per game in the retrieved monthly sample and includes a high strikeout burden.

The current order nevertheless preserves meaningful upper-tail hitters:
- Zach Neto
- Mike Trout
- multiple platoon looks behind them.

So this is not modelled as a shutout expectation. It is modelled as a lower central scoring rate with a real Painter fastball/HR tail.

---

# 9. Bullpen / late-inning process

Current MLB reliever ERAs:
- **Angels: ~4.20-4.24**
- **Phillies: 4.29**

The season bullpen baselines are therefore similar and neither relief unit is treated as automatic lockdown.

Both clubs had the prior day without this matchup, so there is no obvious extreme previous-night workload signal dominating the current availability tree.

Important framework distinction:

**freshness = availability, not quality.**

Central late-game branch:
- both teams can access normal leverage options;
- Philadelphia's stronger overall team context gives it a somewhat better late-win conversion route;
- neither bullpen is strong enough to remove a 2-3 run late-game tail.

Upper scoring tail:
- Painter exits early;
- one or both middle-relief chains are exposed;
- a one-run game creates maximum leverage and pinch-hit depth;
- extra innings add automatic-runner scoring risk if tied.

---

# 10. Underlying joint run corridor

The qualitative run object is constructed before querying the supplied lines.

## Lower tail

Representative scores:
- Phillies 3-2
- Angels 3-2
- Phillies 3-1

Mechanism:
- Detmers continues elite current form;
- Painter's last-start command gains mostly persist;
- normal bullpens convert;
- current-year park suppression shows up.

## Central corridor

Representative scores:
- **Phillies 4-3**
- **Phillies 4-2**
- **Angels 4-3**
- Phillies 5-3

Mechanism:
- Detmers suppresses Philadelphia early but not completely;
- Painter allows moderate rather than severe damage;
- Philadelphia's lineup depth creates late scoring;
- neither bullpen dominates.

## Upper tail

Representative scores:
- Phillies 6-3
- Phillies 6-4
- Angels 6-4

Mechanism:
- Painter's fastball/contact tail or an early Detmers pitch-count spike;
- middle-relief exposure;
- HR/extra-base-hit clustering.

## Structural tail

Representative:
- 4-4 after nine, then extra innings;
- early Painter hook + multiple homers;
- defensive/unearned-run cluster.

The automatic-runner extra-inning branch is especially relevant to **Over 7.5** because a tie at 4-4 has already settled the Over before extras and a 3-3/3-4 type late state can be pushed upward quickly.

---

# 11. Contract geometry and dependence

## Run-line overlap

A one-run final is the key shared state:

| Final | PHI +1.5 | LAA +1.5 |
|---|:---:|:---:|
| PHI 4-3 | WIN | WIN |
| LAA 4-3 | WIN | WIN |
| PHI 5-3 | WIN | LOSS |
| LAA 5-3 | LOSS | WIN |

The two +1.5 rows are therefore positively dependent and **can both win**.

## Total complement

| Total runs | Over 7.5 | Under 7.5 |
|---:|:---:|:---:|
| 7 or fewer | LOSS | WIN |
| 8 or more | WIN | LOSS |

There is no push.

## Cross-target dependence

- Detmers dominance supports LAA +1.5 and Under.
- Painter contact failure supports LAA +1.5 and Over.
- Philadelphia late-lineup/bullpen separation supports PHI +1.5 and Over.
- A 4-3 game supports **both +1.5 rows and Under 7.5**.
- A 5-3 Philadelphia game supports PHI +1.5 and Over while defeating both LAA +1.5 and Under.

---

# 12. Frozen ranking

| Rank | Candidate | Pick | Verdict | Evidence | Performance role | Actionability | Probability |
|---:|---|---|---|---|---|---|---|
| **1** | `P-154-C01` | **Philadelphia Phillies +1.5** | `LEAN` | **MEDIUM** | `PRIMARY_FORMAL — DG-P154-MARGIN` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P-154-C02` | **Los Angeles Angels +1.5** | `LEAN` | **MEDIUM** | `CORRELATED_SECONDARY — DG-P154-MARGIN` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P-154-C03` | **Combined Total Over 7.5 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P154-TOTAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P-154-C04` | **Combined Total Under 7.5 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P154-TOTAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

---

# 13. Rank #1 — Philadelphia Phillies +1.5

This is the most robust supplied contract.

Philadelphia does **not** need to win. It can lose by exactly one and still settle this row successfully.

## Central mechanism

- Philadelphia is the stronger overall team at 74-60 versus 52-82.
- The Phillies' August offense is dramatically stronger than the Angels' current monthly offense.
- The Philadelphia order remains deep enough to create runs after Detmers exits.
- A one-run Angels win still preserves the +1.5 cushion.

The main counterweight is substantial: **Detmers is clearly the stronger current starting pitcher**.

That is why this is a `LEAN / MEDIUM`, not `SUPPORTED`.

## Strongest ordinary kill path

**Angels win by 2+**.

The cleanest route:
1. Detmers extends his current 1.56-ERA/0.84-WHIP regime for 6-7 innings.
2. Painter's fastball/contact tail produces an early Neto/Trout-driven cluster.
3. Los Angeles leads by multiple runs before Philadelphia reaches the softer relief phase.
4. Angels convert the late lead without allowing a one-run backdoor finish.

Representative kill scores:
- LAA 4-2
- LAA 5-2
- LAA 6-3.

This 2+ separation branch is explicitly preserved even though Philadelphia is the preferred winner.

---

# 14. Rank #2 — Los Angeles Angels +1.5

This is also a legitimate `LEAN`, not a hedge inserted for diversification.

The contract benefits from:
- Detmers' major starting-pitcher advantage;
- home-last-bat geometry;
- the low/moderate central score corridor;
- the fact that a one-run Philadelphia win also settles this row.

The central 4-3 Philadelphia score therefore makes **both Rank #1 and Rank #2 win simultaneously**.

## Strongest ordinary kill path

**Philadelphia wins by 2+**.

The route:
1. Philadelphia forces Detmers into elevated pitch count despite limited early scoring.
2. Painter's good/ordinary branch survives 5-6+ innings.
3. Schwarber/Turner/Harper/Arraez/Bohm depth reaches the Angels' middle relief.
4. Philadelphia converts a 3-2 state into 5-2 or 6-3.

The Phillies' current August offense makes this ordinary enough that Angels +1.5 remains below Phillies +1.5.

---

# 15. Rank #3 — Over 7.5 Runs

This is a marginal direction, not a formal high-conviction Over.

Why it edges the Under:
- 7.5 is below the widely observed current market total of 8 to 8.5;
- exactly eight runs is a **win** for this user-supplied Over;
- Painter's season contact/fastball tail remains material;
- Philadelphia's August lineup can produce 4-6 runs even against a strong starter if it reaches the bullpen;
- both relief corps have season ERAs above 4;
- extra innings create an asymmetric upper tail.

Representative Over:
- PHI 5-3
- PHI 6-3
- LAA 5-4
- 4-4 through nine.

## Strongest ordinary kill path

Detmers dominates for 6-7 innings, Painter's recent command improvement persists enough to keep Los Angeles to 2-3, and the rested leverage arms convert.

Representative losses:
- PHI 4-2
- PHI 3-2
- LAA 3-2.

Because this lower tail is very credible, the Over receives only `FORCED RANK / MEDIUM-LOW`.

---

# 16. Rank #4 — Under 7.5 Runs

The Under has substantial process support and is **close to Rank #3** despite its fourth position.

Its strongest evidence:
- Detmers' seven-start 1.56 ERA / 0.84 WHIP regime;
- three straight starts allowing only one earned run in 20 innings;
- Angels' weak .616 August OPS;
- Painter's 4.81 xERA is much better than his 6.04 ERA;
- Painter just generated his best MLB start;
- current-year Angel Stadium run environment is suppressive;
- weather is benign rather than hitter-aiding.

## Why it still ranks fourth

The exact threshold matters.

At **7.5**, an ordinary 5-3 or 4-4 state defeats the Under, and the game contains several routes to eight:
- Painter early hook;
- Philadelphia late offense;
- both bullpens' middling season quality;
- extra innings;
- HR clustering.

This is not an `AVOID` because the Under mechanism is coherent. It is simply the lower-ranked half of a near-balanced total pair.

---

# 17. Potential winner

## Philadelphia Phillies — `LEAN`

**Contract:** full-game winner / moneyline-style endpoint under standard MLB game completion and extra-inning assumptions.  
**Evidence:** `MEDIUM-LOW`  
**Probability:** `NOT_GENERATED / NOT PUBLISHED`  
**Value:** `NO VALUE DETERMINABLE`

### Central winner mechanism

Philadelphia has:
- the better overall team record;
- markedly stronger current August offense;
- deeper upper/middle batting order;
- a more credible route to late scoring if the starters leave a one-run game.

The preferred score family:
- PHI 4-3
- PHI 4-2
- PHI 5-3.

### Strongest failure path

Detmers owns the starter phase, Painter's fastball is punished early, and the Angels convert a low-scoring lead before Philadelphia's lineup reaches enough weak relief exposure.

Representative:
- LAA 4-3
- LAA 4-2.

The starter matchup is sufficiently pro-Angels that the winner call does **not** receive stronger evidence than the Phillies +1.5 contract.

---

# 18. Final volatile refresh

Immediately before this record was written:
- MLB still listed the fixture at **9:38 PM ET / 6:38 PM PDT** with no final/live score;
- Painter and Detmers remained the listed starters;
- MLB's Spanish-language official starting-lineup page displayed both posted batting orders above.

**Frozen state:** `PREGAME`.

If the scheduled first pitch has occurred by the time this file is read, this record remains the immutable pregame view. A later live analysis must create a distinct live target/view and use inning, score, outs, bases, pitch count and remaining bullpen exposure rather than extrapolating this pregame corridor.

---

# 19. Final answer summary

1. **Philadelphia Phillies +1.5 — LEAN / MEDIUM**
2. **Los Angeles Angels +1.5 — LEAN / MEDIUM**
3. **Combined Total Over 7.5 Runs — FORCED RANK / MEDIUM-LOW**
4. **Combined Total Under 7.5 Runs — FORCED RANK / MEDIUM-LOW**

**Potential winner:** **Philadelphia Phillies — LEAN / MEDIUM-LOW**

### Most important interpretation

The two +1.5 picks rank above either total direction because the central game is close enough that a one-run final is highly relevant, and **both positive run lines win together in any one-run game**.

The total is much tighter. Detmers + the Angels' weak August offense + a benign park/weather branch pull downward, while Philadelphia's current offense + Painter's fastball/contact tail + 4.2-ish bullpens + extra innings pull upward. At the exact **7.5** threshold, I place **Over narrowly above Under**, not by a large margin.

---

# 20. Source register

## Governing Drive sources
- `UPCOMING_GAME_RESEARCH_GUIDE.md` — UGR-2026.08.25-v1
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

## Official MLB / field-owning sources
1. MLB probable pitchers — Aug. 28, 2026  
   https://www.mlb.com/probable-pitchers/2026-08-28
2. MLB official Spanish starting-lineups page  
   https://www.mlb.com/es/starting-lineups/2026-08-28
3. MLB Phillies-Angels preview, gamePk 823985  
   https://www.mlb.com/stories/game-preview/823985/
4. MLB Reid Detmers player page / current splits  
   https://www.mlb.com/player/reid-detmers-672282?season=2026&team=108
5. MLB Andrew Painter recent-start story  
   https://www.mlb.com/news/andrew-painter-pitches-a-career-high-7-innings
6. MLB August team hitting statistics  
   https://www.mlb.com/stats/team/ops?split=8
7. MLB reliever team pitching statistics  
   https://www.mlb.com/stats/team/pitching/era/regular-season?split=rp

## Statcast / environment
8. Baseball Savant — Andrew Painter  
   https://baseballsavant.mlb.com/savant-player/andrew-painter-691725
9. Baseball Savant — Statcast park factors  
   https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
10. National Weather Service — Anaheim point forecast  
    https://forecast.weather.gov/MapClick.php?lat=33.8355&lon=-117.9136

## Current market sanity check only — not forecast ground truth
11. FanDuel Research current published line snapshot
12. DraftKings Network current published line snapshot
13. Caliente current listed-pitcher market snapshot

Market information is used only as a contemporaneous sanity check. It does not generate an internal probability or a claim of betting value.

## P-135 settlement sources
14. Telefe Santa Fe — Unión 4-1 Sarmiento
15. Junín24 — Unión 4-1 Sarmiento

Final P-135 corners were not recovered under a provider-consistent final source and are therefore not invented.

# P-155 (conversation-local continuation) — Baltimore Orioles (Brandon Young) @ Athletics (Jacob Lopez) — MLB — 2026-08-28

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the current `RULES_BASEBALL.md`.

**Method:** `MDS-2026.08.29-v2.5 — qualitative champion`  
**Numerical specification:** `NTS-2026.08.25-v0.2 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate policy:** `USER_SUPPLIED`  
**Operator / exact book rules:** `NOT SUPPLIED`  
**Logging mode:** research + forecast + local Markdown log  
**Canonical Drive note:** the read-only Drive snapshot still names `P-137` as the next canonical ID. This is a conversation-local continuation and does not claim to update that Drive file.

---

# 1. Previous-log / queue gate

The active Drive guide requires the canonical open queue to be refreshed before a new forecast.

| ID | Event | Refreshed disposition |
|---|---|---|
| `P-126` | Sikkim Aakraman FC vs Sikkim Boys Club | **OPEN — PREGAME / SCHEDULE FIELD-OWNER UNRESOLVED**; current stronger schedule branch remains later on 29 Aug Melbourne time |
| `P-135` | Unión de Santa Fe vs Sarmiento | **FINAL — Unión 4-1 Sarmiento**; locally settled in the immediately preceding guide-format continuation |
| `P-136` | James Duckworth vs Arthur Fery | **FINAL — Fery advanced after Duckworth retired** |

## P-136 settlement / retrospective gate

ATP's official report confirms **Arthur Fery advanced to the Winston-Salem final after James Duckworth retired**.

The original P-136 contract set was:
1. Over 22.5 total games
2. Duckworth +1.5 games
3. Fery -1.5 games
4. Under 22.5 total games
Potential winner: Arthur Fery.

The original log explicitly froze retirement settlement as:

`UNKNOWN_DEFINITION`

because no sportsbook/operator was supplied.

Therefore:

| Original item | Settlement |
|---|---|
| Over 22.5 games | **UNSETTLEABLE — operator retirement rule unknown** |
| Duckworth +1.5 games | **UNSETTLEABLE — operator retirement rule unknown** |
| Fery -1.5 games | **UNSETTLEABLE — operator retirement rule unknown** |
| Under 22.5 games | **UNSETTLEABLE — operator retirement rule unknown** |
| Potential match winner: Fery | **Descriptive direction correct — Fery officially advanced/won by retirement** |

### P-136 retrospective

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Competitive long-match tree with Fery preferred outright and Duckworth competitive on game handicap | Match ended through Duckworth retirement | The central tennis scoring tree was censored by retirement, so totals/handicap process cannot be judged honestly | Retirement is a known structural tail but its occurrence was not established as forecastable preissue | `INCONCLUSIVE` | Censoring / retirement realization | Preserve retirement-rule freeze and do not grade bookmaker rows without terms | **None** |

P-154 — Phillies @ Angels — remains a separate conversation-local pregame record at the time this new research begins; it is not part of the canonical Drive queue.

---

# 2. Event, target, candidate and time freeze

## Official event

| Field | Frozen value |
|---|---|
| Sport | Baseball |
| Competition | Major League Baseball — 2026 regular season |
| Official event | Baltimore Orioles @ Athletics |
| MLB gamePk | `824960` |
| Venue | Sutter Health Park, West Sacramento, California |
| Away / home | Baltimore away; Athletics home |
| Scheduled start | 2026-08-28 18:40 PDT / 21:40 EDT |
| Melbourne start | 2026-08-29 11:40 AEST |
| State at final volatile refresh | **`GAME-STATE: PREGAME`** |
| Scheduled innings | 9 |
| DH | Universal MLB DH |
| Home-last-bat | Athletics hold conditional bottom-9th entitlement |
| Extra innings | Current MLB automatic-runner regime; operator inclusion/action terms not supplied |
| Information cutoff | Final refresh before scheduled first pitch |

## Decision set

`DECISION_SET_ID: DS-P155-V01`

| Candidate ID | Frozen user contract | Eligibility | Geometry |
|---|---|---|---|
| `P-155-C01` | Baltimore Orioles -1.5 runs | `ELIGIBLE` | Exact complement of ATH +1.5 |
| `P-155-C02` | Athletics +1.5 runs | `ELIGIBLE` | Exact complement of BAL -1.5 |
| `P-155-C03` | Combined Total Over 9.5 runs | `ELIGIBLE` | Exact complement of Under |
| `P-155-C04` | Combined Total Under 9.5 runs | `ELIGIBLE` | Exact complement of Over |

### Target 1 — final margin

`TARGET_ID: MLB-2026-824960-MARGIN-v1`

Outcome: `Baltimore final runs - Athletics final runs`.

- Orioles -1.5 wins only if Baltimore wins by **2+**.
- Athletics +1.5 wins if Oakland wins outright or loses by exactly one.
- No push.

### Target 2 — total runs

`TARGET_ID: MLB-2026-824960-TOTAL-RUNS-v1`

- Over 9.5 wins at **10+ total runs**.
- Under 9.5 wins at **0-9**.
- No push.

**Listed-pitcher / action / extra-inning sportsbook terms:** `UNKNOWN_DEFINITION` because operator was not supplied.

---

# 3. Final starter / lineup handshake

## Baltimore — Brandon Young, RHP

Status: `CONFIRMED_OFFICIAL`

Official MLB current line:
- 9-3
- 3.50 ERA
- 123.1 IP
- 99 SO
- 1.36 WHIP

Last seven:
- 3.69 ERA
- 39.0 IP
- 40 H
- 14 BB
- 32 K
- 1.38 WHIP

August:
- 20.0 IP
- 4.50 ERA
- 26 H
- 9 BB
- 14 K
- 1.75 WHIP
- five HR allowed.

Young's season profile is credible, but his current August contact/baserunner regime is materially worse than his full-season ERA.

## Athletics — Jacob Lopez, LHP

Status: `CONFIRMED_OFFICIAL`

Official MLB current line:
- 5-4
- 4.98 ERA
- 94.0 IP
- 90 SO
- 1.48 WHIP

Last seven starts:
- **2.33 ERA**
- 38.2 IP
- 27 H
- 13 BB
- 47 K
- 1.03 WHIP

Latest three:
- 6 IP, 1 ER, 9 K at Houston
- 6 IP, 2 ER, 6 K vs Texas
- 7 IP, 2 ER, 5 K vs Tampa Bay.

This is a real current-regime improvement and is not ignored because of the 4.98 season ERA.

## Posted Baltimore order

1. Blaze Alexander — SS, R
2. Pete Alonso — DH, R
3. Jackson Holliday — 2B, L
4. Coby Mayo — 1B, R
5. Christian Encarnacion-Strand — 3B, R
6. Leody Taveras — RF, S
7. Christian Franklin — CF, R
8. Dylan Beavers — LF, L
9. Carlos Narváez — C, R

**Key lineup note:** Gunnar Henderson is not in the posted order, while Blaze Alexander returns to the leadoff spot.

Baltimore nevertheless has **six clear right-handed bats plus Taveras' switch look** against the left-handed Lopez.

## Posted Athletics order

1. Henry Bolte — CF, R
2. Jeff McNeil — 2B, L
3. Zack Gelof — 3B, R
4. Lawrence Butler — RF, L
5. Tommy White — 1B, R
6. Max Muncy — DH, R
7. Carlos Cortes — LF, L
8. Jonah Heim — C, S
9. Alika Williams — SS, R

Oakland has meaningful right-handed exposure against Young, which matters because Young's 2026 platoon results have been worse against right-handed hitters.

---

# 4. D0 mechanism retrieval

### Predeclared query

`MLB pregame side/total -> favorite -1.5 vs underdog +1.5 exact complement -> starter-regime conflict -> bullpen separation tail -> hitter-friendly park`

### Retained comparable

**P-064 — Rangers @ White Sox**

Transferable controls:
- explicit +1.5 / -1.5 separation decomposition;
- do not let winner preference automatically imply -1.5;
- preserve HR/early-hook and bullpen separation tails;
- low/moderate total and margin are different targets.

Material differences:
- different pitchers, lineups and venue;
- P-064 outcome is not used as a vote;
- Sutter Health Park is a much more aggressive current park environment.

**Retained comparable count:** 1.

---

# 5. Structural baseline and current regime

## Team records

- Baltimore: **65-69**
- Athletics: **53-81**

Baltimore is the stronger team and remains in the AL wild-card race, but the gap is not large enough to treat a 2+ run road win as the automatic central outcome.

## August offense

### Baltimore
23 games:
- 97 runs
- 35 HR
- .236 AVG
- .307 OBP
- .423 SLG
- **.730 OPS**

This is a power-led rather than high-OBP attack.

### Athletics
24 games:
- 104 runs
- 25 HR
- .252 AVG
- .314 OBP
- .401 SLG
- **.715 OPS**

Oakland's current offense is not materially worse than Baltimore's on raw August run production.

That is important: the 53-81 season record cannot simply be converted into a large current offensive gap.

---

# 6. Starter matchup process

## Orioles offense vs Lopez

Lopez's current seven-start run suppression is the biggest reason Oakland +1.5 ranks first.

However, Baltimore's exact lineup creates a relevant adverse branch for him.

2026 Lopez opponent split:
- vs left-handed hitters: approximately .204 AVG / .299 OBP / .290 SLG
- vs right-handed hitters: approximately **.271 AVG / .354 OBP / .468 SLG**

He has allowed:
- 13 HR to right-handed hitters
- only 2 HR to left-handed hitters.

Baltimore has deliberately loaded its order with right-handed bats:
- Alexander
- Alonso
- Mayo
- Encarnacion-Strand
- Franklin
- Narváez
plus switch-hitting Taveras.

Therefore Lopez's current suppression remains central, but **the platoon configuration raises Baltimore's early scoring and HR tail**.

## Athletics offense vs Young

Young's full-season line is stronger than Lopez's, but the matchup is less comfortable than the 3.50 ERA suggests.

2026 Young opponent split:
- vs LHB: ~.226 AVG / .311 OBP / .369 SLG
- vs RHB: **~.303 AVG / .341 OBP / .463 SLG**

Oakland's posted order contains:
- Bolte
- Gelof
- White
- Muncy
- Williams

from the right side, while McNeil/Butler/Cortes provide left-handed balance.

Young's August line has also deteriorated:
- 4.50 ERA
- 1.75 WHIP
- .329 AVG allowed
- .948 OPS allowed
- 5 HR in 20 innings.

The baseball framework therefore freezes two Young branches:

**Season-prior branch**
- 5-6 innings;
- 2-3 runs;
- adequate contact management.

**Current adverse branch**
- traffic and HR damage;
- early/middle hook;
- 3-5 run Oakland starter-phase output.

The latter is material enough that Baltimore -1.5 cannot be ranked as the safest side.

---

# 7. Bullpen / late-game process

## Baltimore relievers

Current MLB reliever ERA:
- approximately **3.98-4.07**
- WHIP approximately 1.26-1.27.

Useful individual arms include:
- Rico Garcia
- Tyler Wells
- Yennier Cano
with weaker alternatives behind them.

Baltimore played the previous day in St. Louis, so its bullpen does not receive the same full-rest assumption as Oakland.

## Athletics relievers

Current MLB reliever ERA:
- **5.64**
- 1.52 WHIP
- .273 AVG allowed.

This is the worst current reliever ERA in the retrieved MLB table.

Oakland did have the previous day off after its 7-4 win over Minnesota, so its main arms are more available.

That distinction matters:

**Oakland bullpen freshness is positive availability evidence, but it does not erase a 5.64 season-quality baseline.**

José Suarez is also returning from injury and adds another available left-handed option, but his return does not transform the entire relief distribution.

## Late-game consequence

If the score is close after six:
- Oakland +1.5 is still protected by the one-run cushion and home last-bat;
- Baltimore gains a meaningful **late 2+ separation path** against the Oakland relief chain;
- the Over 9.5 tail becomes more dangerous.

---

# 8. Venue / environment

Sutter Health Park is a major scoring modifier.

Baseball Savant 2026 one-year park factors:
- overall park factor: **113**
- run factor: **128**
- HR factor: **127**

Those are among the most hitter-friendly marks in MLB.

Baseball Savant's environmental distance model also has Sutter Health Park adding roughly **4.7 feet** to comparable well-hit fly balls in 2026, with a warm average environment.

## Weather

National Weather Service Sacramento forecast around the evening:
- mostly clear
- temperatures falling from the 80s
- south wind roughly 3-6 mph later
- no precipitation concern.

Weather does not suppress the hitter-friendly park effect.

It is a secondary modifier rather than a standalone Over rule.

---

# 9. Underlying joint run corridor

The qualitative joint run object is built before querying the four supplied lines.

## Lower tail

Representative:
- Baltimore 4-2
- Athletics 4-3
- Baltimore 4-3

Mechanism:
- Lopez's current form persists;
- Young returns closer to season form;
- available Oakland late arms outperform the season bullpen baseline;
- HR clustering does not materialise.

## Central corridor

Representative:
- **Baltimore 5-4**
- **Baltimore 5-3**
- **Athletics 5-4**

Mechanism:
- both starters allow traffic but avoid complete collapse;
- Baltimore's right-handed lineup tests Lopez;
- Oakland's right-handed bats test Young;
- the bullpens add modest late scoring;
- home-last-bat keeps Oakland inside the one-run corridor.

## Upper tail

Representative:
- Baltimore 6-4
- Baltimore 7-4
- Athletics 6-5

Mechanism:
- Young's August HR/contact branch persists;
- Lopez's platoon disadvantage produces Baltimore power;
- Oakland's bullpen quality tail is exposed;
- Sutter converts hard contact into extra-base/HR damage.

## Structural tail

- starter exits before five innings;
- multi-HR inning;
- 5-5/6-6 type late state;
- extra innings with automatic runner.

---

# 10. Contract geometry and dependence

## Margin pair

- Orioles -1.5 requires Baltimore by **2+**.
- Athletics +1.5 wins on every Oakland victory and every one-run Baltimore win.

They are exact half-run complements.

Representative:

| Score | BAL -1.5 | ATH +1.5 |
|---|:---:|:---:|
| BAL 5-4 | LOSS | WIN |
| BAL 5-3 | WIN | LOSS |
| ATH 5-4 | LOSS | WIN |
| BAL 6-4 | WIN | LOSS |

## Total pair

- 9 total runs -> Under wins.
- 10 total runs -> Over wins.

Representative:

| Score | Total | O9.5 | U9.5 |
|---|---:|:---:|:---:|
| BAL 5-4 | 9 | LOSS | WIN |
| BAL 5-3 | 8 | LOSS | WIN |
| BAL 6-4 | 10 | WIN | LOSS |
| ATH 6-5 | 11 | WIN | LOSS |

## Cross-target dependence

- Lopez dominance supports ATH +1.5 and Under.
- Young rebound supports BAL winner and Under.
- Baltimore lineup/platoon success plus Oakland bullpen failure supports BAL -1.5 and Over.
- Young's August contact tail supports ATH +1.5 and Over.

---

# 11. Final ranking

| Rank | Candidate | Exact contract | Verdict | Evidence | Dependence group | Performance role | Actionability | Probability |
|---:|---|---|---|---|---|---|---|---|
| **1** | `P-155-C02` | **Athletics +1.5** | `LEAN` | **MEDIUM** | `DG-P155-MARGIN` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **2** | `P-155-C04` | **Combined Total Under 9.5** | `LEAN` | **MEDIUM-LOW** | `DG-P155-TOTAL` | `PRIMARY_FORMAL` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **3** | `P-155-C03` | **Combined Total Over 9.5** | `FORCED RANK` | **MEDIUM-LOW** | `DG-P155-TOTAL` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |
| **4** | `P-155-C01` | **Baltimore Orioles -1.5** | `FORCED RANK` | **MEDIUM-LOW** | `DG-P155-MARGIN` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED / NOT PUBLISHED` |

---

# 12. Ranking rationale

## #1 — Athletics +1.5

This is the most robust supplied contract.

The Athletics do not need to win. A one-run Baltimore victory still settles this row successfully.

Why it ranks first:
- Lopez's seven-start 2.33 ERA / 1.03 WHIP current regime is strong.
- Oakland has home last-bat.
- Oakland's August offense is producing slightly more raw runs than Baltimore's.
- Young's August contact/WHIP/HR profile creates a credible Oakland scoring route.
- The central score family contains two ATH +1.5 wins for every ordinary 2+ Baltimore branch.

### Strongest kill path

Baltimore's right-handed lineup gets Lopez out before the late-middle innings, then the **5.64 Oakland bullpen** turns a close game into a 2+ margin.

Representative:
- BAL 6-3
- BAL 7-4
- BAL 8-4.

This is a very real failure path and is why the evidence stays at MEDIUM.

---

## #2 — Under 9.5 runs

This is a narrow lean.

Why it ranks above the Over:
- 9.5 is a relatively high threshold.
- Lopez's current seven-start run suppression is substantial.
- Young's full-season 3.50 ERA remains relevant despite his poorer August.
- A central one-run game can easily finish 5-4 or 4-3 and still stay Under.
- Oakland's most trusted late arms are rested.

Central Under scores:
- 5-4
- 5-3
- 4-3.

### Strongest kill path

The park/HR/bullpen tree overwhelms the starter suppression:
- Baltimore's righties damage Lopez;
- Oakland's righties damage Young;
- Oakland's bullpen adds 2-4 late runs;
- Sutter's 128 run / 127 HR factors amplify hard contact.

That creates 6-4, 7-4 and 6-5 outcomes.

The Under is therefore only a **small ordinal edge**, not a strong low-total call.

---

## #3 — Over 9.5 runs

The Over is extremely live and close to Rank #2.

Support:
- Sutter Health Park is the most hitter-friendly 2026 park on the retrieved one-year Statcast table.
- Young's August line is 4.50 ERA / 1.75 WHIP with five HR.
- Lopez's season split against RHB is materially weaker than against LHB.
- Baltimore's exact order is right-handed-heavy.
- Oakland's bullpen carries a 5.64 ERA / 1.52 WHIP.
- Both offenses have produced roughly 4.2-4.3 runs per game in August.

Why it remains third:
- reaching ten requires the game to clear a meaningfully high threshold;
- Lopez's current suppression is not superficial;
- 5-4 remains Under despite being a relatively active game.

---

## #4 — Orioles -1.5

Baltimore is still my preferred winner, but that does not make -1.5 the best contract.

The run line needs a **2+ run win**.

Support:
- Baltimore is the better overall team.
- Lopez is vulnerable to right-handed hitters and Baltimore has shaped its lineup accordingly.
- Oakland's bullpen is the clearest large-margin failure mechanism.
- Baltimore's power has been strong in August: 35 HR in 23 games.

Why it ranks fourth:
- Lopez's current starter regime protects Oakland from early separation.
- Oakland's offense is capable of scoring against Young.
- Young is not currently pitching like a dominant road favorite.
- a 5-4 Baltimore win makes the winner call correct but -1.5 lose.

---

# 13. Potential winner

## Baltimore Orioles — `LEAN`

**Evidence:** `MEDIUM-LOW`  
**Probability:** `NOT_GENERATED / NOT PUBLISHED`  
**Value:** `NO VALUE DETERMINABLE`

### Central mechanism

Baltimore is preferred outright because:
- the club is stronger overall;
- its posted lineup has a favorable right-handed shape against Lopez;
- its bullpen baseline is much better than Oakland's;
- late-game separation/come-from-behind capacity is materially better.

### Strongest failure path

Lopez continues his 2.33-ERA current regime, Young's August contact problems persist, and Oakland uses home last-bat plus a rested relief sequence to protect a 4-3 / 5-4 lead.

Therefore:

**Winner order: Baltimore > Athletics**,  
but **Athletics +1.5 > Baltimore -1.5**.

There is no contradiction between those statements.

---

# 14. Final volatile refresh

Immediately before issue:
- MLB still listed **Brandon Young vs Jacob Lopez** for this exact Aug. 28 game.
- MLB's starting-lineup feed displayed both posted orders.
- Scheduled first pitch remained **6:40 PM PDT / 11:40 AM AEST**.
- No verified scored state was used in this forecast.

**Frozen state: `PREGAME`.**

If first pitch occurs after this cutoff but before the user reads the card, this remains the immutable pregame view. Any later live forecast must create a new view and use inning, score, outs, base state, pitch counts and remaining bullpen exposure.

---

# 15. Final answer summary

1. **Athletics +1.5 — LEAN / MEDIUM**
2. **Combined Total Under 9.5 — LEAN / MEDIUM-LOW**
3. **Combined Total Over 9.5 — FORCED RANK / MEDIUM-LOW**
4. **Baltimore Orioles -1.5 — FORCED RANK / MEDIUM-LOW**

**Potential winner:** **Baltimore Orioles — LEAN / MEDIUM-LOW**

### Central score family
- Baltimore **5-4**
- Baltimore **5-3**
- Athletics **5-4**
- Baltimore **6-4** upper branch.

### Most important interpretation

The highest-ranked contract is **Oakland +1.5**, not because Oakland is the preferred winner, but because the one-run corridor is wide enough that Baltimore can win the game and still fail to cover -1.5.

The total is nearly balanced. Both starter central branches keep **5-4 / 5-3** highly plausible, while Sutter Health Park, Young's current HR/contact deterioration, and Oakland's 5.64 bullpen ERA create a serious ten-plus-run tail.

No numerical probability, EV, staking, ROI or market-edge claim is made.

---

# 16. Source register

## Governing Drive sources
- `UPCOMING_GAME_RESEARCH_GUIDE.md` — UGR-2026.08.25-v1
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

## Official MLB / Statcast sources
1. MLB probable pitchers — 2026-08-28  
   https://www.mlb.com/probable-pitchers/2026-08-28
2. MLB official starting lineups — 2026-08-28  
   https://www.mlb.com/es/starting-lineups/2026-08-28
3. MLB preview, gamePk 824960  
   https://www.mlb.com/stories/game-preview/824960/
4. Brandon Young MLB player page  
   https://www.mlb.com/player/brandon-young-687064
5. Jacob Lopez MLB player page  
   https://www.mlb.com/player/jacob-lopez-682052
6. Baseball Savant Brandon Young  
   https://baseballsavant.mlb.com/savant-player/brandon-young-687064
7. Baseball Savant Jacob Lopez  
   https://baseballsavant.mlb.com/savant-player/jacob-lopez-682052
8. Baseball Savant game preview — gamePk 824960  
   https://baseballsavant.mlb.com/preview?game_pk=824960
9. Baseball Savant park factors  
   https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
10. MLB August team hitting stats  
    https://www.mlb.com/stats/team/ops?split=8
11. MLB reliever team ERA  
    https://www.mlb.com/stats/team/pitching/era/regular-season?split=rp

## Weather
12. National Weather Service — Sacramento  
    https://forecast.weather.gov/MapClick.php?lat=38.5669&lon=-121.4674

## Queue settlement
13. ATP official Winston-Salem Friday report — Fery advanced after Duckworth retirement  
    https://www.atptour.com/en/news/winston-salem-2026-friday-report

## Current market sanity check only
14. FanDuel Research — Orioles/Athletics current listed line
15. Caliente — Orioles (B. Young) @ Athletics (J. Lopez)

Market prices are not used to claim value or internal probability. They are only a contemporaneous contract/sanity cross-check.

# P-156 (conversation-local continuation) — Sacramento River Cats @ Reno Aces — Triple-A Pacific Coast League — 2026-08-28

## Decision outcome

**`LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`**

The scheduled 6:35 PM PDT / 11:35 AM AEST start crossed during research. At the final field-owner refresh immediately afterward, the official Pacific Coast League scoreboard still displayed the fixture as scheduled with no score, no pitch/play state, and Sacramento's starter still `TBD`.

Under `UPCOMING_GAME_RESEARCH_GUIDE.md`, this record therefore cannot pretend to be a current pregame card and cannot fabricate a live state.

The four supplied rows are retained below as the **frozen pre-start research ordering for record/reference only**. They are not presented as an actionable live reissue.

**Method:** `MDS-2026.08.29-v2.5 — qualitative champion`  
**Operational guide:** `UGR-2026.08.25-v1`  
**Sport module:** `RULES_BASEBALL.md`  
**Competition population:** Triple-A Pacific Coast League — explicitly separate from MLB/NPB/KBO priors  
**Numerical model:** `NTS-2026.08.25-v0.2 — DESIGN ONLY / NOT FITTED`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate origin:** `USER_SUPPLIED`  
**Operator:** `NOT SUPPLIED`  
**Exact sportsbook action/listed-pitcher/extra-inning terms:** `UNKNOWN_DEFINITION`

---

# 1. Previous-log / queue gate

The Drive canonical snapshot remains read-only and stale relative to the locally verified continuation work.

Local reconciliation already completed:
- `P-135` Unión de Santa Fe vs Sarmiento — final 4-1, locally settled.
- `P-136` Duckworth vs Fery — Fery advanced by retirement; betting rows remain UNSETTLEABLE because retirement terms were unknown.
- `P-126` remains open with the field-owner schedule conflict unresolved.

Recent conversation-local cards `P-154` and `P-155` were still upcoming at the beginning of this research and are not canonical Drive queue entries.

No Drive file is edited by this record.

---

# 2. Event, candidate and target freeze

## Event identity

| Field | Frozen value |
|---|---|
| Sport | Baseball |
| Level | Triple-A Minor League Baseball |
| League | Pacific Coast League |
| Event | Sacramento River Cats @ Reno Aces |
| Venue | Greater Nevada Field, Reno, Nevada |
| Scheduled start | Friday 2026-08-28, 6:35 PM PDT |
| Melbourne equivalent | Saturday 2026-08-29, 11:35 AM AEST |
| Home batting entitlement | Reno |
| Scheduled innings | 9 |
| Start-crossing state | Scheduled start crossed during research |
| Final field-owner state | Official PCL page still showed scheduled/no score/no play |
| Issued state | `LIVE STATE NOT VERIFIED` |

## Decision set

`DECISION_SET_ID: DS-P156-V01`

| Candidate | Contract | Eligibility | Geometry |
|---|---|---|---|
| `P-156-C01` | Sacramento River Cats -1.5 | Valid supplied row | Exact complement of Reno +1.5 |
| `P-156-C02` | Reno Aces +1.5 | Valid supplied row | Exact complement of Sacramento -1.5 |
| `P-156-C03` | Combined Total Over 12.5 | Valid supplied row | Exact complement of Under 12.5 |
| `P-156-C04` | Combined Total Under 12.5 | Valid supplied row | Exact complement of Over 12.5 |

## Target 1 — final margin

`TARGET_ID: PCL-2026-SAC-RNO-MARGIN-v1`

- River Cats -1.5 requires Sacramento to win by 2+.
- Aces +1.5 wins if Reno wins outright or loses by exactly one.
- No push at a half-run line.

## Target 2 — combined total

`TARGET_ID: PCL-2026-SAC-RNO-TOTAL-RUNS-v1`

- Over 12.5 wins at 13+.
- Under 12.5 wins at 0-12.
- No push.

Because the operator is not supplied, its pitcher-action, suspension, postponement and extra-inning rules remain `UNKNOWN_DEFINITION`.

---

# 3. Participant gate

## Reno starter

**Yu-Min Lin — LHP**  
Status: `CONFIRMED_OFFICIAL / FIELD-OWNER LISTED`

Official current line:
- 6-9
- 5.69 ERA
- 24 games / 23 starts
- 106.0 innings
- 77 strikeouts
- 1.58 WHIP
- .276 opponent average.

Lin has also demonstrated a credible good-start branch. In an official Reno report from early August he delivered his second consecutive quality start:
- 6.0 IP
- 2 ER
- 6 H
- 2 BB
- 6 K.

That was described as his fifth quality start of the season.

This is not enough to erase the 5.69/1.58 season baseline, but it prevents treating him as an automatic high-run starter.

## Sacramento starter

**Official status: `TBD / NOT RELEASED` at the final field-owner refresh.**

This is the most important uncertainty in the card.

The current baseball rules require starter identity to precede starter-quality analysis. Therefore:
- no Sacramento starter is invented;
- no secondary preview pitcher is silently promoted to starter;
- Sacramento's pitching phase is modelled as a broad mixture;
- all participant-sensitive rows are capped at `FORCED RANK / MEDIUM-LOW` or lower.

### Sacramento pitching mixture

**Good/normal branch**
- one of Sacramento's better bulk/starter arms handles 4-6 innings;
- the club's stronger overall pitching environment carries forward;
- normal relief options protect the middle/late innings.

**Ordinary branch**
- 4-5 inning starter/bulk exposure;
- 2-4 Reno runs before the main relief chain.

**Short-start/adverse branch**
- starter/bulk identity is a weaker or recently shifted role;
- Reno reaches the bullpen early;
- altitude plus repeated plate appearances create a 6+ Reno run route.

The missing starter identity materially widens both the Reno +1.5 and Over 12.5 tails.

## Posted lineups

A complete field-owner starting lineup for both clubs was not recovered before the start-crossing cutoff.

Accordingly, individual current roster statistics below are **roster-depth context only**, not statements that those players are starting.

---

# 4. Competition / team baseline

This is a PCL event. MLB scoring baselines are not transferred.

## Overall records / run environment

Before the latest series result, official PCL standings showed:

### Sacramento
- 73-52
- 740 runs scored
- 628 runs allowed
- +112 run differential.

After Reno's verified 5-0 win, Sacramento is 73-53.

Transparent descriptive update:
- 740 RS / 633 RA through 126 games
- approximately 5.87 scored and 5.02 allowed per game.

### Reno
Before the latest result:
- 55-72
- 697 runs scored
- 785 runs allowed
- -88 differential.

After the verified 5-0 win:
- 56-72
- 702 RS / 785 RA through 128 games
- approximately 5.48 scored and 6.13 allowed per game.

These are **descriptive arithmetic summaries**, not fitted probabilities.

The broad structural picture is:
- Sacramento is clearly the better club across the season.
- Reno's games carry materially weaker run-prevention.
- Both teams operate in a high-scoring PCL population.
- 12.5 is nevertheless a high threshold: ordinary 6-5, 6-4, 7-5 and 5-4 states still stay Under.

---

# 5. Current series / regime evidence

Official Reno reports show the first three games of this series:

1. Sacramento 12-3 Reno — total 15
2. Sacramento 6-4 Reno — total 10
3. Reno 5-0 Sacramento — total 5

The series has therefore produced:
- one very high scoring game;
- one normal PCL game;
- one strongly suppressed game.

This wide 15 / 10 / 5 range is useful because it directly demonstrates that Greater Nevada Field does **not** force every game Over 12.5.

It also demonstrates that 2+ separation is a very real Sacramento branch: the River Cats already won 12-3 in this series.

The results are not mechanically counted as a predictive hit rate.

---

# 6. Sacramento offense

Current official River Cats leader pages show strong Triple-A roster production including:

- Turner Hill: approximately .353 AVG / .420 OBP / .529 SLG / .949 OPS
- Scott Bandura: approximately .330 / .403 / .495 / .898
- Will Brennan: approximately .316 / .357 / .446 / .803.

The Sacramento postgame notes after the 5-0 loss also recorded Brennan extending an eight-game hitting streak and batting .394 with a 1.111 OPS over that span.

The roster therefore has a credible high-contact / high-traffic route against Lin and the Reno relief corps.

However, because today's starting order was not verified, no exact plate-appearance allocation is attached to those names.

## Sacramento offensive branches vs Lin

**Central**
- some traffic against a 5.69 ERA / 1.58 WHIP starter;
- approximately middle-PCL scoring before bullpen effects.

**Suppression**
- Lin reaches his quality-start branch and Sacramento repeats some of the previous night's poor sequencing.

**Upper tail**
- Lin's season baserunner problems return;
- Sacramento forces an early hook;
- Reno's weaker overall staff is exposed through the middle innings.

The upper tail is the main reason River Cats -1.5 and Over 12.5 remain credible.

---

# 7. Reno offense

Official Reno player stats show a usable offensive core in the current roster pool, including:

- Tyler Locklear around .306/.392/.486, .878 OPS
- A.J. Vukovich around .282/.341/.506, .847
- Kristian Robinson around .279/.388/.440, .828
- Jacob Amaya around .253/.361/.420, .781.

Again, these are roster-context statistics because the field-owner lineup was not recovered before the cutoff.

Reno has scored 3, 4 and 5 runs in the first three games of this series.

That sequence should **not** be extrapolated as a deterministic progression. What matters is that Reno has shown enough current offense to reach 4-6 runs, particularly if Sacramento's unknown starter lands in the weak/short-start branch.

---

# 8. Pitching / bullpen context

## Reno

Official Reno team pitching data:
- team ERA approximately 5.75
- WHIP approximately 1.59
- opponent average approximately .277.

Lin's 5.69 ERA / 1.58 WHIP sits close to that weak staff environment.

Reno does have useful relief arms, including Gerardo Carrillo at approximately a 4.06 ERA in the current official player table, but the team-level run-prevention distribution remains poor.

## Sacramento

Official River Cats pitching data from the current-season source window put Sacramento around:
- 4.73 team ERA
- approximately 1.48 WHIP.

The current relief pool includes:
- Michael Fulmer: 2.98 ERA / 1.25 WHIP
- Braxton Roxby: 4.11 / 1.18
- Wilkin Ramos: 4.64 / 1.47.

This is a stronger broad pitching environment than Reno's.

But because the Sacramento starter/bulk assignment is unresolved, the first 4-6 innings cannot be treated as if one of those relievers is automatically controlling them.

---

# 9. Venue / weather

## Greater Nevada Field

The Reno environment is a genuine upper-tail mechanism:
- high elevation around 4,500-4,600 feet;
- historically strong home-run / extra-base-hit environment;
- official MiLB/Reno reporting regularly documents deep home-run carry.

The dimensions include a deep center field, so the environment is not simply "every fly ball is a home run"; altitude can also increase extra-base-hit and gap-contact damage.

## Weather

National Weather Service Reno:
- 30% chance of showers/thunderstorms before 8 PM;
- mostly cloudy, gradually clearing;
- southwest wind around 5 mph becoming calm;
- low around 56°F.

Earlier observations included rain.

Mechanistic effect:
- possible delay / wet-surface / grip uncertainty;
- potential temporary command/fielding variance;
- no strong wind-based suppression;
- if normal play occurs, the underlying Reno altitude remains.

Weather is therefore a **variance modifier**, not an automatic Under or Over rule.

---

# 10. D0 mechanism retrieval

Predeclared query:

`Baseball -> pregame/full-game margin+total -> Triple-A PCL -> Reno altitude -> one officially unresolved starter -> user-supplied ±1.5 and 12.5 total`

**Result: `NO COMPARABLE CASE`**

The historical development set contains baseball process lessons from MLB/NPB/KBO/CPBL, but no sufficiently comparable PCL/Reno/unknown-starter event was retained as an outcome analogue.

Promoted process controls still apply:
- starter identity precedes starter quality;
- unresolved starter = explicit mixture;
- run-line cushion/separation decomposition;
- short start is exposure, not automatically Over;
- bullpen freshness and quality remain separate;
- HR/contact upper tails must remain in the joint score tree.

No historical outcome votes for any of the four directions.

---

# 11. Underlying run corridor

## Lower tail

Representative scores:
- Sacramento 5-3
- Sacramento 4-3
- Reno 5-3

Mechanism:
- Lin reaches his good-start branch;
- Sacramento's unknown starter is competent;
- run sequencing is inefficient despite baserunners;
- showers/cooler evening suppress clean offense modestly.

## Central corridor

Representative scores:
- **Sacramento 6-5**
- **Sacramento 7-5**
- **Reno 6-5**

Mechanism:
- Lin allows ordinary traffic without a full collapse;
- Sacramento's unknown pitching plan is neither dominant nor disastrous;
- both relief chains contribute some scoring;
- Reno's home-last-bat keeps close states live.

## Upper tail

Representative:
- Sacramento 8-5
- Sacramento 8-6
- Reno 8-6
- Sacramento 9-5

Mechanism:
- Lin's season traffic returns;
- Sacramento's TBD starter falls in the early-hook branch;
- altitude amplifies hard contact;
- middle relief is exposed;
- error/extra-base-hit clusters develop.

## Structural tail

- long weather delay changes starter/bulk plans;
- multiple early homers;
- unknown Sacramento pitching assignment becomes a bullpen game;
- 6-6/7-7 late state reaches extra innings.

---

# 12. Frozen pre-start research ranking

**Important:** Because the scheduled start crossed and no trustworthy live state was available, these are **research-order rows only**, not an actionable live forecast.

| Rank | Candidate | Pick | Verdict | Evidence | Performance role | Actionability |
|---:|---|---|---|---|---|---|
| **1** | `P-156-C04` | **Combined Total Under 12.5 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P156-TOTAL` | **NOT ACTIONABLE — LIVE STATE NOT VERIFIED** |
| **2** | `P-156-C02` | **Reno Aces +1.5** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P156-MARGIN` | **NOT ACTIONABLE — LIVE STATE NOT VERIFIED** |
| **3** | `P-156-C01` | **Sacramento River Cats -1.5** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P156-MARGIN` | **NOT ACTIONABLE — LIVE STATE NOT VERIFIED** |
| **4** | `P-156-C03` | **Combined Total Over 12.5 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P156-TOTAL` | **NOT ACTIONABLE — LIVE STATE NOT VERIFIED** |

`Probability: NOT_GENERATED / NOT PUBLISHED` for every row.  
`Value: NO VALUE DETERMINABLE`.

---

# 13. Ranking rationale

## #1 — Under 12.5 runs

The Under is a **narrow** ordinal preference, not a strong low-scoring thesis.

Why it ranks first:
- 12.5 is a high threshold even in the PCL.
- Sacramento's descriptive season games sit around an 11-run combined environment.
- Reno's descriptive season games are higher, but still not automatically 13+.
- the current series has produced totals of 15, 10 and 5;
- Lin has a credible six-inning quality-start branch;
- Sacramento owns the stronger broad pitching environment.

Central scores such as 6-5, 7-5 and 5-4 all remain Under.

### Strongest kill path

The strongest adverse state is **not rare or contrived**:

1. Sacramento's unknown starter is weak or becomes a short-start/bullpen game.
2. Reno reaches 5-7 runs.
3. Sacramento gets normal traffic against Lin and Reno's 5.7+ team-pitching environment.
4. altitude and middle-relief contact add another cluster.

Scores:
- 8-6
- 9-5
- 8-5

all defeat the Under.

That kill path is strong enough that the row cannot be upgraded beyond `FORCED RANK / MEDIUM-LOW`.

A contemporaneous Caliente snapshot had Over 12.5 slightly shorter than Under 12.5, which is a useful market sanity warning against overconfidence in this Under. It is not used as an internal probability.

---

## #2 — Reno Aces +1.5

Why it is robust:
- home last-bat;
- one-run Sacramento wins still settle Reno +1.5;
- Reno has the only field-owner confirmed starter;
- Lin has a real quality-start branch;
- Sacramento's own starter is unresolved;
- Reno has shown 3, 4 and 5 runs in the current series.

Representative wins:
- SAC 6-5
- RNO 6-5
- SAC 5-4.

### Strongest kill path

Sacramento's stronger offense gets to Lin and then reaches Reno's weaker staff, while Sacramento's unknown pitcher turns out to be competent.

Representative:
- SAC 7-4
- SAC 8-5
- SAC 9-5.

Those 2+ separation states are ordinary enough that Reno +1.5 remains only a forced rank.

---

## #3 — River Cats -1.5

Sacramento is the stronger team:
- 73-53 versus 56-72;
- materially better season run differential;
- stronger broad pitching environment;
- deeper current offensive roster;
- already owns a 12-3 win in this series.

The clearest cover route is:
- Sacramento scores 5-7+ against Lin/Reno relief;
- Sacramento's unknown starter falls in a good/ordinary branch;
- the River Cats turn a one-run middle-game lead into a multi-run win.

### Why it is below Reno +1.5

The contract needs **2+ separation**, while Sacramento's own starting-pitching state is still unresolved.

A 6-5 Sacramento win gets the winner call right but loses River Cats -1.5.

That margin geometry is decisive.

---

## #4 — Over 12.5 runs

This is a very live fourth-ranked row.

Support:
- Greater Nevada Field / Reno altitude;
- Lin's 5.69 ERA / 1.58 WHIP;
- Reno's team pitching around 5.75 ERA;
- Sacramento's starter is TBD;
- both teams have credible 5-7 run offensive branches;
- the current series already produced a 12-3 total;
- weather/delay can create pitching-plan volatility.

### Why it remains fourth

Thirteen is still a high requirement.

The game can be offensively active and still finish:
- 6-5 = 11
- 7-5 = 12
- 6-4 = 10
- 5-4 = 9.

Lin's quality-start branch and Sacramento's stronger staff environment give the game enough suppression states that 13+ does not become the central corridor.

---

# 14. Potential winner

## Sacramento River Cats — `FORCED WINNER — LOW CONFIDENCE`

**Endpoint:** full-game winner under standard research assumptions.  
**Evidence:** LOW / capped by unresolved Sacramento starter and unconfirmed lineups.  
**Probability:** NOT_GENERATED / NOT PUBLISHED.  
**Value:** NO VALUE DETERMINABLE.

### Central mechanism

Sacramento:
- owns the stronger record;
- has a +100-plus season run-differential advantage relative to Reno's negative differential;
- has the stronger overall pitching environment;
- has the deeper offensive roster;
- has already shown a large-separation route in this series.

### Strongest failure path

Lin reaches his good-start branch, the unresolved Sacramento starter is poor/short, and Reno uses home-last-bat to protect a 6-5 or 7-5 lead.

Therefore:

**Winner order: Sacramento > Reno**

while

**Reno +1.5 > Sacramento -1.5**

because a one-run Sacramento victory satisfies both statements.

---

# 15. Contract geometry and scenario map

| Scenario | Representative score | SAC -1.5 | RNO +1.5 | O12.5 | U12.5 |
|---|---:|:---:|:---:|:---:|:---:|
| Close Sacramento win | SAC 6-5 | ❌ | ✅ | ❌ | ✅ |
| Sacramento moderate separation | SAC 7-5 | ✅ | ❌ | ❌ | ✅ |
| Reno close upset | RNO 6-5 | ❌ | ✅ | ❌ | ✅ |
| Sacramento upper-tail cover | SAC 8-5 | ✅ | ❌ | ✅ | ❌ |
| Two-sided altitude game | SAC 8-6 | ✅ | ❌ | ✅ | ❌ |
| Reno upper-tail upset | RNO 8-6 | ❌ | ✅ | ✅ | ❌ |
| Suppression branch | SAC 5-3 | ✅ | ❌ | ❌ | ✅ |

The margin and total pairs are each exact half-run complements. Cross-market outcomes remain dependent through starter quality, bullpen exposure and game state.

---

# 16. Final volatile refresh / state warning

Final field-owner refresh after the scheduled 6:35 PM PDT start:

- official PCL scoreboard continued to display **Sacramento 73-53 @ Reno 56-72**;
- **no score or live play state was exposed**;
- Sacramento starter remained **TBD**;
- Reno starter remained **Yu-Min Lin, LHP, 6-9, 5.69 ERA**.

Because the start crossed, the guide prohibits presenting this as an ordinary pregame actionable forecast.

**Final state:**  
`LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`

When a trustworthy live state becomes available, any new analysis must start from:
- inning / half;
- score;
- outs;
- base state;
- actual Sacramento pitcher and pitch count;
- Lin status/pitch count;
- current batting order;
- remaining bullpen availability;
- weather/delay state.

The pre-start line may also no longer be offered.

---

# 17. Source register

## Governing Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md` — UGR-2026.08.25-v1
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

## Official MiLB / club sources
1. Pacific Coast League official scoreboard / Sacramento field-owner page  
   https://www.milb.com/sacramento/scores/triple-a/pacific-coast
2. Sacramento River Cats 2026 schedule  
   https://www.milb.com/sacramento/schedule/2026/fullseason
3. Reno Aces official Aug/Sept promotion schedule confirming Aug. 28 home fixture  
   https://www.milb.com/reno/news/reno-aces-announce-promotions-for-august-and-september
4. Reno Aces overall standings  
   https://www.milb.com/reno/standings/overall-standings
5. PCL second-half standings  
   https://www.milb.com/app-firstpitch/pacific-coast/standings
6. Yu-Min Lin official MiLB player page  
   https://www.milb.com/app-firstpitch/player/yu-min-lin-801179
7. Reno official pitching/player statistics  
   https://www.milb.com/reno/stats/pitching/player
8. Reno official hitting/player statistics  
   https://www.milb.com/reno/stats
9. Sacramento official hitting statistics  
   https://www.milb.com/sacramento/stats
10. Sacramento official pitching statistics  
    https://www.milb.com/sacramento/stats/pitching/player
11. Reno official series Game 1 recap — Sacramento 12-3  
    https://www.milb.com/app-firstpitch/reno/news/aces-rally-in-middle-innings-but-sacramento-snags-game-one
12. Reno official Game 2 recap — Sacramento 6-4  
    https://www.milb.com/news/crisantes-homer-highlights-reno-offense-in-game-two-defeat
13. Reno official Game 3 recap — Reno 5-0  
    https://www.milb.com/reno/news/short-shines-aces-blank-river-cats-for-second-time-in-2026
14. Reno official Yu-Min Lin quality-start report  
    https://www.milb.com/reno/news/lin-quality-aces-blast-three-homers-against-chihuahuas

## Weather
15. National Weather Service Reno — Aug. 28 evening forecast  
    https://forecast.weather.gov/MapClick.php?FcstType=text&TextType=2&lat=39.5316&lg=english&lon=-119.8045&unit=0

## Current market snapshot — sanity check only
16. Caliente — Sacramento River Cats @ Reno Aces  
    Current captured lines included SAC -1.5, RNO +1.5 and O/U 12.5.

No market price is used to claim internal model probability, expected value, ROI or staking edge.

# P-157 (conversation-local continuation) — Toronto Tempo @ Las Vegas Aces — WNBA — 2026-08-28

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the active `RULES_BASKETBALL.md`.

**Method:** `MDS-2026.08.29-v2.5 — qualitative champion`  
**Numerical specification:** `NTS-2026.08.25-v0.2 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate policy:** `USER_SUPPLIED`  
**Operator / exact OT terms:** `NOT SUPPLIED / UNKNOWN_DEFINITION`  
**Logging mode:** research + forecast + local Markdown log  
**Canonical Drive note:** the read-only Drive combined log still names `P-137` as its next canonical ID. This is a conversation-local continuation and does not claim to modify that Drive file.

---

# 1. Previous-log / queue gate

The Drive canonical snapshot still lists:
- P-126 — schedule-conflicted / open;
- P-135 — stale as live in Drive, but locally verified final and settled in the guide-format continuation;
- P-136 — stale as upcoming in Drive, but locally verified final-by-retirement and handled under unknown operator retirement terms.

No new canonical Drive final requires settlement before this card. Recent local cards P-154 through P-156 are conversation-local continuations rather than canonical Drive queue items.

---

# 2. Event, target, candidate and time freeze

## Official event

| Field | Frozen value |
|---|---|
| Sport | Basketball |
| Competition | WNBA — 2026 regular season |
| Event | Toronto Tempo @ Las Vegas Aces |
| Official WNBA game ID | `1022600293` |
| Venue | Michelob ULTRA Arena, Las Vegas, Nevada |
| Scheduled tip | Friday 2026-08-28, 10:00 PM ET / 7:00 PM PT |
| Melbourne equivalent | Saturday 2026-08-29, 12:00 PM AEST |
| Final research state | **`GAME-STATE: PREGAME`** — official WNBA page still showed scheduled game, no score/play state |
| Full-game endpoint | Standard WNBA full game; exact sportsbook OT/void terms not supplied |

## Decision set

`DECISION_SET_ID: DS-P157-V01`

| Candidate ID | Frozen contract | Eligibility | Geometry |
|---|---|---|---|
| `P-157-C01` | Toronto Tempo +14.5 | Eligible | Exact complement of Las Vegas -14.5 |
| `P-157-C02` | Las Vegas Aces -14.5 | Eligible | Exact complement of Toronto +14.5 |
| `P-157-C03` | Combined Total Over 174.5 | Eligible | Exact complement of Under 174.5 |
| `P-157-C04` | Combined Total Under 174.5 | Eligible | Exact complement of Over 174.5 |

### Margin target

`TARGET_ID: WNBA-2026-1022600293-MARGIN-v1`

- TOR +14.5 wins if Toronto wins outright or loses by 14 or fewer.
- LVA -14.5 wins only if Las Vegas wins by 15+.
- No push.

### Total target

`TARGET_ID: WNBA-2026-1022600293-TOTAL-v1`

- Over 174.5 wins at 175+.
- Under 174.5 wins at 174 or fewer.
- No push.

Exact operator overtime settlement is `UNKNOWN_DEFINITION` because no sportsbook was supplied.

---

# 3. Participant / minutes / lineup gate

This is the most important uncertainty in the forecast.

## Toronto

Latest same-day injury reporting:
- Marina Mabrey — OUT, right adductor.
- Brittney Sykes — OUT for season, left foot.
- Aneesah Morrow — OUT for season, left knee.
- Nyara Sabally — unavailable in current roster regime.
- Julie Allemand — unavailable in current roster regime.
- María Conde — unavailable in current roster regime.
- Isabelle Harrison — latest accessible same-day report still listed QUESTIONABLE with a foot issue at the research cutoff.

Toronto officially signed Kiana Williams to a seven-day extreme-hardship contract on Aug. 24, direct evidence that the active backcourt/depth structure is materially depleted.

Key lost creation:
- Mabrey was the team's leading scorer in the current season profile.
- Sykes was another high-usage scorer.
- Allemand led the club in assists in the available season profile.

The result is a materially different current roster regime from Toronto's full-season averages.

**Confirmed starting five:** `NOT RELEASED` on the official WNBA game page at final refresh.

## Las Vegas

- NaLyssa Smith — officially OUT for the remainder of the season after the leg injury suffered against Toronto on Aug. 23.
- A'ja Wilson — latest same-day injury report: QUESTIONABLE, head/back.
- Dana Evans — latest same-day injury report: QUESTIONABLE, leg.

Smith's absence is meaningful:
- 11.7 PPG
- 6.4 RPG
- league-leading 63.8% FG in the current report.

Wilson is the dominant uncertainty:
- roughly 26.0 PPG
- 9.5 RPG
- major rim protection / defensive value.

**Confirmed starting five:** `NOT RELEASED` on the official WNBA game page at final refresh.

### Required lineup branches

Because Wilson is unresolved, one single lineup state is prohibited.

**Wilson normal workload**
- Las Vegas retains elite primary half-court scoring and rim deterrence.
- 15+ separation becomes more plausible.
- Aces team scoring ceiling rises.

**Wilson active but limited**
- Las Vegas remains a clear winner favorite but closing-margin variance rises.
- Toronto +14.5 and Under gain relative to the full-Wilson branch.

**Wilson out**
- Jackie Young / Chelsea Gray absorb more creation.
- Las Vegas remains structurally stronger than the depleted Tempo, but both the favorite margin and total shift downward.
- Toronto +14.5 becomes substantially more robust than -14.5.

All supplied rows therefore remain capped below HIGH evidence.

---

# 4. D0 mechanism retrieval

Predeclared query:

`WNBA full-game pre-tip -> large spread >= 12 -> heavily depleted underdog -> favorite with unresolved primary star -> full-game spread plus total exact complements`

**Result:** `NO COMPARABLE CASE` retained from the formal D0 pool.

The Learning Register's `C-PL5-BSK-MISMATCH-PATH` is only a future candidate observation, not an active forecast weight. It is used here only as a process reminder to model:
- opening separation,
- maximum lead,
- starter-minute truncation,
- bench/garbage-time pace,
- closing-margin compression.

No historical result votes for Toronto +14.5 or Las Vegas -14.5.

---

# 5. Baseline and current regime

## Las Vegas

Current record:
- **26-13**

Current StatMuse team profile:
- Offensive rating approximately **112.8**
- Defensive rating approximately **108.2**
- Net rating approximately **+4.6**

Last five:
- beat Washington 83-76
- lost Minnesota 87-92
- lost Atlanta 82-97
- beat Connecticut 101-78
- beat Toronto 88-78

Average Las Vegas points across those five:
- **88.2**

Average combined total from those five:
- approximately **172.4**

## Toronto

Current record:
- **11-27**

Last five:
- lost Indiana 95-101
- lost Washington 82-93
- beat Portland 82-79
- lost Las Vegas 78-88
- lost Seattle 78-90

The critical current-regime fact is not Toronto's season scoring average; it is that the roster has progressively lost its primary creators.

Toronto scored:
- **78 vs Las Vegas**
- **78 at Seattle**

in its two most recent games.

Against Seattle:
- 37.1% FG
- 4-for-26 from three
- 17 turnovers
- 14 assists.

That is a more representative current depleted-offense branch than Toronto's early-season full-roster scoring average.

---

# 6. Current-season head-to-head

## July 20 — Las Vegas 109, Toronto 83
Margin:
- Las Vegas +26

Total:
- 192

Wilson:
- 26 points

Jackie Young:
- 24 points, 12 rebounds

This game represents the **high-efficiency Las Vegas separation branch**, but roster continuity is poor enough that it cannot control today's forecast.

## August 23 — Las Vegas 88, Toronto 78
Margin:
- Las Vegas +10

Total:
- 166

Wilson:
- 27 points, 7 rebounds, 7 assists

Jackie Young:
- 21 points

Toronto:
- 10-for-27 from three.

NaLyssa Smith suffered the season-ending injury during this game.

This game is more current than July but still not identical:
- Toronto has subsequently lost additional availability/creation.
- Las Vegas has lost Smith.
- Wilson is now questionable.

Therefore the two H2Hs are scenario evidence, not a two-game averaging model.

---

# 7. Possession / efficiency process

## Toronto offense

The current creation tree is compressed.

Primary current sources of offense are likely to come from combinations of:
- Kiki Rice initiation;
- Isabelle Harrison interior/post activity if available;
- Temi Fagbenle rim/roll activity;
- Kia Nurse perimeter shooting;
- Laura Juskaite;
- hardship/depth guard minutes.

Without Mabrey, Sykes and Allemand, Toronto loses:
- pull-up creation;
- shot-clock bailout ability;
- primary passing;
- high-volume three-point generation;
- free-throw pressure.

The strongest Toronto scoring branch is therefore not "season-average offense." It is:
1. keep turnovers manageable;
2. offensive-rebound enough misses;
3. reach the line;
4. make enough threes to force Las Vegas out of its preferred defensive shape.

The strongest failure branch is a prolonged half-court drought.

## Las Vegas offense

With Wilson:
- paint/rim pressure,
- elbow/post creation,
- Jackie Young secondary creation,
- Chelsea Gray pick-and-roll / late-clock organization
support an efficient half court.

Without Smith:
- finishing/rebounding depth falls;
- more frontcourt minutes move to lower-usage replacements;
- second-unit scoring becomes less certain.

If Wilson is limited/out, Las Vegas can still beat Toronto through defense and backcourt creation without necessarily pushing its own score into the high 90s.

That distinction is central to the **Under + Aces-winner** branch.

---

# 8. Rest / travel / schedule

Las Vegas has had approximately five days between games since the Aug. 23 Toronto meeting.

Toronto:
- played at Seattle Aug. 26;
- travels to Las Vegas;
- then is scheduled at Phoenix the following night.

Rest does not automatically create an Under.

Mechanistically:
- Las Vegas should have greater starter/rotation freshness.
- Toronto has an incentive to avoid overextending an already short rotation if the game separates.
- Toronto garbage-time units can either compress the margin or lose offensive efficiency further.
- The next-day Phoenix game makes late blowout minute management especially relevant.

---

# 9. Joint game corridor

## Lower-total / controlled Las Vegas branch

Representative:
- LVA 88-74
- LVA 90-76
- LVA 89-77

Mechanism:
- Toronto struggles to create efficient half-court shots.
- Las Vegas wins through defense rather than relentless pace.
- Smith absence reduces some Las Vegas interior efficiency.
- Wilson is limited or Las Vegas reduces late starter minutes.

Helps:
- Under 174.5
- Toronto +14.5 in 88-74 / 89-77
- Las Vegas -14.5 in 90-74 / wider variants.

## Central branch

Representative:
- **LVA 90-77**
- **LVA 91-77**
- **LVA 92-78**

Totals:
- 167
- 168
- 170

Margins:
- 13
- 14
- 14

This is the main reason the Under ranks first and Toronto +14.5 ranks narrowly above Las Vegas -14.5.

## Favorite-separation branch

Representative:
- LVA 94-76
- LVA 95-76
- LVA 96-77

Mechanism:
- Wilson plays normally;
- Toronto's short-handed offense turns the ball over;
- Las Vegas scores efficiently in transition/early offense;
- Toronto cannot sustain three-point shooting.

This branch:
- wins Las Vegas -14.5;
- can still keep Under 174.5 alive at 94-76 = 170.

## High-total shooting branch

Representative:
- LVA 97-80
- LVA 98-79
- LVA 95-82

Mechanism:
- Toronto shoots well from three;
- Las Vegas answers efficiently;
- both teams accumulate free throws;
- late fouling extends the game.

This is the main Over branch.

## Structural tails

### Garbage-time compression
Las Vegas leads by 20+ in the third quarter, starters sit, Toronto's reserves cut the final gap to 10-14.

Helps:
- Toronto +14.5
- often Under, depending bench pace.

### Garbage-time expansion
Toronto's depleted bench cannot score and Las Vegas' reserves continue producing.

Helps:
- Las Vegas -14.5
- can support Under or Over depending pace.

### Overtime
A close regulation game makes Toronto +14.5 likely but creates a major Over tail.

Operator OT inclusion is unknown because no book was supplied.

---

# 10. Contract geometry / dependence

The spread pair is an exact complement:
- Toronto +14.5 wins at TOR win or LVA margin 1-14.
- Las Vegas -14.5 wins at LVA margin 15+.

The total pair is an exact complement:
- Under wins at <=174.
- Over wins at >=175.

The important dependence is not "favorite = Over."

Examples:

| Score | TOR +14.5 | LVA -14.5 | O174.5 | U174.5 |
|---|---:|---:|---:|---:|
| LVA 90-77 | WIN | LOSS | LOSS | WIN |
| LVA 92-78 | WIN | LOSS | LOSS | WIN |
| LVA 94-76 | LOSS | WIN | LOSS | WIN |
| LVA 97-80 | LOSS | WIN | WIN | LOSS |
| LVA 88-80 | WIN | LOSS | LOSS | WIN |

A large Las Vegas win does not require an Over; Toronto offensive suppression can produce **favorite cover + Under**.

---

# 11. Final ranking

| Rank | Candidate | Pick | Verdict | Evidence | Performance role | Actionability |
|---:|---|---|---|---|---|---|
| **1** | `P-157-C04` | **Combined Total Under 174.5** | `LEAN` | **MEDIUM** | `PRIMARY_FORMAL — DG-P157-TOTAL` | `NO VALUE DETERMINABLE` |
| **2** | `P-157-C01` | **Toronto Tempo +14.5** | `LEAN` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P157-MARGIN` | `NO VALUE DETERMINABLE` |
| **3** | `P-157-C02` | **Las Vegas Aces -14.5** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P157-MARGIN` | `NO VALUE DETERMINABLE` |
| **4** | `P-157-C03` | **Combined Total Over 174.5** | `AVOID / FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P157-TOTAL` | `NO VALUE DETERMINABLE` |

All rows:
- `Probability: NOT_GENERATED / NOT PUBLISHED`

---

# 12. Rank #1 — Under 174.5

This is the strongest contract.

### Main reasons

1. Toronto's current offense is operating without most of its best shot creation.
2. Toronto scored only 78 in each of its last two games.
3. The most recent Aces-Tempo meeting finished 88-78 = **166**.
4. Las Vegas' last-five game totals average about **172.4**.
5. Smith's season-ending absence removes an elite-efficiency finisher/rebounder.
6. Wilson being questionable creates a meaningful lower-Las-Vegas-efficiency branch.
7. Aces defensive dominance can create a large margin **without** forcing a high total.

### Strongest ordinary kill path

Wilson plays a full workload, Las Vegas reaches 95-100, and Toronto gets enough threes/free throws to score 79-83.

Representative:
- 97-80 = 177
- 98-79 = 177
- 95-82 = 177.

Late fouling and overtime are additional Over tails.

The Under is a `LEAN`, not `SUPPORTED`, because Toronto's defense can permit an elite Las Vegas offensive night and 174.5 is not an extremely high WNBA threshold.

---

# 13. Rank #2 — Toronto +14.5

This is narrowly above Las Vegas -14.5.

### Main reasons

1. **14.5 is a large closing-margin requirement.**
2. Toronto lost the Aug. 23 meeting by only 10.
3. Las Vegas is now without NaLyssa Smith.
4. Wilson's status is unresolved.
5. Blowout garbage time can compress a 20-point maximum lead into a 10-14 point final.
6. Toronto's recent road margins have often remained around the low-teens range rather than producing repeated 20+ losses.

### Why this is not stronger

Toronto is much more depleted now than in the Aug. 23 matchup:
- Mabrey out;
- Sykes out;
- Morrow out;
- Allemand unavailable;
- Conde unavailable;
- Sabally unavailable;
- Harrison unresolved at cutoff.

A full-strength Wilson branch can overwhelm the current Toronto rotation.

### Strongest kill path

Las Vegas defends Toronto into a 70-75 point output and gets 90+ itself.

Representative:
- 94-74
- 95-76
- 96-75.

---

# 14. Rank #3 — Las Vegas -14.5

There is a strong case for the favorite, but the exact threshold is demanding.

### Main reasons

- Las Vegas: 26-13.
- Toronto: 11-27.
- Las Vegas has the superior offense/defense profile.
- Toronto is on the road and materially short-handed.
- Las Vegas has the rest advantage.
- Toronto's current lineup can suffer long creation droughts.
- If Wilson plays normally, Toronto lacks a clean matchup answer.

### Why it remains below Toronto +14.5

The line asks for **15+**, not simply an Aces win.

The basketball module specifically requires maximum-lead and closing-margin branches for extreme spreads. A 20-point third-quarter lead can finish 12 because:
- Wilson/Young/Gray sit;
- Toronto plays against lower-leverage lineups;
- next-game / playoff health management reduces late favorite intensity.

Smith's absence and Wilson uncertainty also reduce confidence in a full-game 15+ margin.

---

# 15. Rank #4 — Over 174.5

The Over is possible but needs a higher-efficiency branch.

### Main pathways

- Wilson plays full minutes and drives Las Vegas into the high 90s.
- Toronto repeats the July-style three-point/high-shotmaking branch.
- Toronto's weak defense creates transition opportunities.
- late fouling adds 8-12 points in the final two minutes.
- overtime.

### Why fourth

The current Toronto roster is more likely to create a **low offensive floor** than a reliable 80+ output.

Las Vegas can win 94-74 or 92-76 and still leave the total comfortably Under.

The absence of Smith and uncertainty around Wilson also weaken the most direct Las Vegas offensive-ceiling mechanism.

---

# 16. Potential winner

## Las Vegas Aces — `LEAN`

**Evidence:** MEDIUM  
**Endpoint:** full-game winner under standard WNBA game assumptions; exact operator OT terms not supplied.

### Central mechanism

Las Vegas has:
- better half-court creation;
- better defensive structure;
- more reliable ball-handling;
- home court;
- significant rest advantage;
- much more intact star/creator depth even with Smith out.

Toronto's depleted roster makes sustaining four quarters of high-level offense difficult.

### Strongest failure path

Wilson is ruled out or heavily limited, Las Vegas struggles on the defensive glass/inside without Smith, and Toronto makes a high volume of threes while keeping turnovers low.

That upset path exists, but it remains materially below the Las Vegas winner corridor.

**Winner order: Las Vegas > Toronto.**

The winner call is substantially more robust than **Las Vegas -14.5**.

---

# 17. Final volatile refresh

Immediately before issue:
- official WNBA game page still showed Toronto @ Las Vegas scheduled for 10:00 PM ET, no scored state;
- confirmed starting fives were not exposed;
- latest same-day reports still listed A'ja Wilson QUESTIONABLE;
- Dana Evans QUESTIONABLE;
- NaLyssa Smith OUT for season;
- Toronto's Mabrey/Sykes/Morrow unavailable, with major additional roster absences;
- Isabelle Harrison remained unresolved in the accessible final report.

Therefore no late lineup fact is invented.

**Frozen state: `PREGAME`.**

If a final lineup/injury release changes Wilson's status:
- **Wilson OUT/LIMITED:** strengthens Under 174.5 and Toronto +14.5; weakens Las Vegas -14.5 and Over.
- **Wilson ACTIVE without restriction:** strengthens Las Vegas -14.5 and the Over tail; does not automatically reverse the Under because Toronto's offensive suppression branch remains strong.

---

# 18. Final answer summary

1. **Under 174.5 — LEAN / MEDIUM**
2. **Toronto Tempo +14.5 — LEAN / MEDIUM-LOW**
3. **Las Vegas Aces -14.5 — FORCED RANK / MEDIUM-LOW**
4. **Over 174.5 — AVOID / FORCED RANK / MEDIUM-LOW**

**Potential winner:** **Las Vegas Aces — LEAN / MEDIUM**

### Central score family
- Las Vegas 90-77
- Las Vegas 91-77
- Las Vegas 92-78
- Las Vegas 94-76 as the favorite-cover / Under branch
- Las Vegas 97-80 as the principal Over branch.

### Core interpretation

The cleanest thesis is not "Aces blowout." It is **Toronto's depleted offense suppresses the game total**.

At the same time, **14.5 is sufficiently large that Toronto can lose comfortably and still cover**, especially if Wilson is limited/out or Las Vegas reduces starter minutes after building a large lead.

No internal probability, EV, ROI, staking recommendation or claimed market edge is published.

---

# 19. Source register

## Governing Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md` — UGR-2026.08.25-v1
- `RULES_BASKETBALL.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

## Official league/team sources
1. WNBA official game page — game 1022600293  
   https://www.wnba.com/game/1022600293/TOR-vs-LVA
2. Las Vegas Aces official Aug. 23 result/gallery — Aces 88, Tempo 78  
   https://aces.wnba.com/news/gallery-aces-tempo-8-23-2026
3. Las Vegas Aces official July 20 result/gallery — Aces 109, Tempo 83  
   https://aces.wnba.com/news/gallery-aces-109-tempo-83-7-20-2026
4. Toronto Tempo official hardship signing — Kiana Williams  
   https://tempo.wnba.com/news/toronto-tempo-sign-kiana-williams-to-7-day-extreme-hardship-contract

## Current injury / roster reporting
5. Reuters — NaLyssa Smith out for remainder of season
6. Same-day injury-report coverage citing WNBA report — Wilson/Evans/Harrison and Toronto absences
7. DraftKings Network current roster-regime summary — secondary only

## Statistical context
8. StatMuse — Toronto 2026 schedule/results and last five
9. StatMuse — Toronto last five road games
10. StatMuse — Las Vegas last five games and current team ratings
11. StatMuse — Las Vegas vs Toronto 2026 H2H

## Market sanity only
12. Action Network snapshot: Las Vegas -14.5, total 175.5
13. DraftKings snapshot: Las Vegas -13.5, total 173.5

Market data is not used to generate an internal probability or to claim value.

# P-158 (conversation-local continuation) — Washington Mystics @ Los Angeles Sparks — WNBA — 2026-08-28

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the active `RULES_BASKETBALL.md`.

**Method:** `MDS-2026.08.29-v2.5 — qualitative champion`  
**Numerical specification:** `NTS-2026.08.25-v0.2 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate policy:** `USER_SUPPLIED`  
**Operator / exact OT terms:** `NOT SUPPLIED / UNKNOWN_DEFINITION`  
**Canonical Drive note:** the read-only Drive combined log remains unreconciled with these conversation-local continuations. This file does not edit Google Drive.

---

# 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | WNBA 2026 regular season |
| Event | Washington Mystics @ Los Angeles Sparks |
| Official WNBA game | `1022600294` |
| Venue | Crypto.com Arena, Los Angeles |
| Scheduled tip | Friday Aug. 28, 2026 — 10:00 PM ET / Saturday Aug. 29 — 12:00 PM AEST |
| Evidence cutoff | approximately 11:59 AEST, before scheduled tip |
| Official state at cutoff | `PREGAME` — WNBA page showed scheduled fixture, no score/play state |
| Endpoint | full game; exact sportsbook OT terms not supplied |

Decision set: `DS-P158-V01`

| Candidate | Contract | Geometry |
|---|---|---|
| `P-158-C01` | Washington Mystics -4.5 | exact complement of LA +4.5 |
| `P-158-C02` | Los Angeles Sparks +4.5 | exact complement of WAS -4.5 |
| `P-158-C03` | Combined Total Over 166.5 | exact complement of Under 166.5 |
| `P-158-C04` | Combined Total Under 166.5 | exact complement of Over 166.5 |

---

# 2. Availability / minutes gate

## Washington

The Mystics' final same-day status report was **clean — no injuries to report**.

That is important because Washington is relying on a relatively stable current core built around:
- Shakira Austin
- Kiki Iriafen
- Sonia Citron
- Georgia Amoore
- the current wing/guard rotation.

Washington played at Phoenix the previous night and won **80-73**.

Key workload from that game:
- Georgia Amoore: 30 minutes, 25 points, 4 assists.
- Kiki Iriafen: 30 minutes, 20 points, 12 rebounds.
- Shakira Austin: about 30 minutes, 11 points, 7 rebounds.

Washington therefore enters healthy but on its **only back-to-back of the regular season** and at the end of a four-game Western road trip.

## Los Angeles

Latest same-day information:
- Emma Cannon — **Probable**, knee.
- Rae Burrell — no longer listed on the injury report after illness.
- Tonie Morgan — no longer listed on the injury report.

No material star absence was confirmed for Los Angeles at cutoff.

Confirmed starting fives were not recovered from the official WNBA page at the final pre-tip refresh. Accordingly, this card does not invent a confirmed five.

---

# 3. Current team regime

## Washington

Record entering the game:
- **24-15**
- three straight road wins.

Recent results:
- 80-73 at Phoenix
- 94-84 at Phoenix
- 105-100 at Portland
- 84-94 vs Minnesota
- 93-82 vs Toronto

Recent offensive ceiling is real, but the most recent game was much more defense-driven.

Washington's current season profile:
- about **82.8 PPG scored**
- about **82.9 PPG allowed**

The stronger process edge is the defense rather than an extreme scoring offense.

## Los Angeles

Record:
- **13-25**

Recent:
- 71-78 vs Atlanta
- 77-68 vs Connecticut
- 88-124 vs Atlanta
- 77-85 at Connecticut
- 70-80 at Washington

Los Angeles has scored:
- 71
- 77
- 88
- 77
- 70

over that five-game span.

That recent offensive environment is much lower than the Sparks' full-season 87+ scoring average.

The Sparks have also allowed roughly **92.5 PPG** across the season, which keeps Washington's scoring ceiling materially alive.

---

# 4. Current head-to-head

## May 29
Los Angeles 92, Washington 87.

Los Angeles won despite Kelsey Plum not playing in that earlier roster configuration.

## August 15
Washington 80, Los Angeles 70.

That game:
- stayed well below 166.5;
- was close through three quarters;
- Washington separated late;
- Los Angeles struggled to create efficient offense.

The two current-season meetings therefore span:
- one 179-point higher-efficiency game;
- one 150-point lower-efficiency game.

They are scenario evidence, not a two-game average model.

---

# 5. Possession / efficiency process

## Washington offense vs Los Angeles defense

Washington's central offensive route:
1. establish Austin/Iriafen interior pressure;
2. create kick-outs and secondary drive lanes;
3. use Citron/Amoore creation without excessive turnovers;
4. exploit a Sparks defense that has allowed very high season scoring.

The strongest upward-scoring branch is Washington getting into the high 80s / low 90s.

The fatigue counter:
- second night of a back-to-back;
- fourth road game in six days;
- previous-night starter minutes around 30.

That can reduce transition frequency and late-game shooting efficiency.

## Los Angeles offense vs Washington defense

Los Angeles' current offense is built around:
- Nneka Ogwumike interior/midrange efficiency and rebounding;
- Dearica Hamby creation/physicality;
- Erica Wheeler organization;
- Rae Burrell perimeter scoring;
- Cameron Brink rim/defensive impact and offensive secondary role.

The problem is current consistency.

Recent Sparks scoring has frequently settled in the low-to-high 70s.

Washington's defensive length, Austin/Iriafen interior coverage and active perimeter group can force LA into:
- contested half-court possessions;
- turnovers;
- low-efficiency late-clock shots.

The main LA scoring-up branch is:
- Washington's back-to-back legs weaken transition defense;
- Ogwumike/Hamby win the glass;
- LA gets to the line and makes enough threes to reach 80+.

---

# 6. Rest / travel branch

This is Washington's only back-to-back of the season:
- Aug. 27 at Phoenix
- Aug. 28 at Los Angeles.

Washington is also closing a four-game road trip:
- Portland
- Phoenix
- Phoenix
- Los Angeles.

This creates two opposite mechanisms:

### Helps LA +4.5 / Under
- Washington pace and shooting can fall late.
- legs can reduce transition offense.
- Washington may struggle to separate by multiple possessions.

### Helps Over / LA upset tail
- tired transition defense;
- weaker closeouts;
- more fouling;
- LA is substantially more rested.

Rest is therefore not coded as an automatic Under.

---

# 7. Joint score corridor

## Lower-total Washington control
- WAS 84-76
- WAS 85-77
- WAS 86-78

Mechanism:
- Sparks remain in their recent low-output offensive state;
- Washington wins through defense;
- back-to-back limits Washington's own ceiling.

## Central
- **WAS 86-79**
- **WAS 88-80**
- **WAS 87-79**

These place the game directly around the user's 166.5 threshold.

## Higher-efficiency Washington win
- WAS 90-81
- WAS 91-82

Mechanism:
- LA's weak season defense shows;
- Washington gets efficient paint/FT offense;
- LA scores enough against tired legs to keep pace.

## LA close-game / upset branch
- WAS 84-82
- LAS 84-82
- LAS 86-83

Mechanism:
- back-to-back fatigue compresses Washington's margin;
- Sparks win offensive rebounding / free throws;
- Washington's shooting falls late.

## Structural tails
- late fouling in a 3-6 point game adds 8-12 points;
- overtime strongly helps Over and LA +4.5;
- Washington builds a double-digit lead and LA's late offense stalls, helping WAS -4.5 + Under.

---

# 8. Final ranking

| Rank | Candidate | Pick | Verdict | Evidence | Performance role | Actionability |
|---:|---|---|---|---|---|---|
| **1** | `P-158-C01` | **Washington Mystics -4.5** | `LEAN` | **MEDIUM** | `PRIMARY_FORMAL — DG-P158-MARGIN` | `NO VALUE DETERMINABLE` |
| **2** | `P-158-C03` | **Combined Total Over 166.5** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P158-TOTAL` | `NO VALUE DETERMINABLE` |
| **3** | `P-158-C04` | **Combined Total Under 166.5** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P158-TOTAL` | `NO VALUE DETERMINABLE` |
| **4** | `P-158-C02` | **Los Angeles Sparks +4.5** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P158-MARGIN` | `NO VALUE DETERMINABLE` |

All probabilities: `NOT_GENERATED / NOT PUBLISHED`.

---

# 9. Rank #1 — Washington -4.5

Why it ranks first:
- Washington is 24-15; Los Angeles is 13-25.
- Washington has won three straight road games.
- Washington's final injury report is clean.
- Sparks are 1-4 in their last five and have repeatedly failed to reach 80.
- Washington won the latest H2H 80-70.
- Los Angeles' defense has been materially weaker than Washington's over the season.
- Current external market snapshots moved around Washington -5.5, making the supplied -4.5 threshold relatively less demanding as a likelihood boundary.

Strongest kill path:
- Washington's back-to-back fatigue reduces shotmaking;
- LA wins offensive rebounding/free-throw pressure;
- game stays within one possession late.

Representative:
- WAS 84-82
- LAS 84-82.

This is why the pick remains a LEAN rather than SUPPORTED.

---

# 10. Rank #2 — Over 166.5

This is only a narrow preference over Under.

Support:
- Washington's last-five offense has been much stronger than its season scoring average.
- LA has allowed about 92.5 PPG over the full season.
- Washington scored 94 and 105 in two of its three previous road games.
- LA's rested legs can raise its own offensive output against a tired Washington defense.
- late fouling is plausible if LA keeps the margin inside 6-8 points.
- the broadly observed contemporaneous total was around 167.5, one point above the supplied 166.5 threshold; this is used only as an external sanity check, not a value claim.

Representative wins:
- WAS 88-80 = 168
- WAS 90-81 = 171
- WAS 91-82 = 173.

Strongest kill path:
- LA repeats its recent 70-77 point offense;
- Washington wins via defense and tired-leg pace control.

Representative:
- WAS 85-77 = 162
- WAS 86-78 = 164.

---

# 11. Rank #3 — Under 166.5

The Under is very live.

Its strongest evidence:
- LA's last five outputs: 71, 77, 88, 77, 70.
- four of those five games finished below 166.5.
- Washington held LA to 70 on Aug. 15.
- Washington's latest game was an 80-73 defensive win.
- the Mystics' back-to-back can reduce their own offensive efficiency.

Why it remains below Over:
- 166.5 is a modest threshold relative to LA's poor defense;
- Washington is healthy and has recently produced 94/105-point road games;
- LA has a rest advantage;
- a competitive fourth quarter adds a late-foul scoring tail.

The total pair is near-balanced.

---

# 12. Rank #4 — Los Angeles +4.5

This is not a dead branch.

Support:
- Washington is on the second night of its only back-to-back;
- fourth road game in six days;
- LA is rested;
- the Sparks won the first 2026 meeting 92-87;
- the August 15 rematch was competitive into the second half before Washington separated.

Why it ranks fourth:
- Washington is currently healthier;
- materially better current record/form;
- better defense;
- stronger recent road results;
- LA's recent offense has repeatedly failed to reach 80.

LA +4.5 needs the fatigue/rest advantage to overcome Washington's clearer two-way edge.

---

# 13. Potential winner

## Washington Mystics — `LEAN / MEDIUM`

Central mechanism:
- Washington controls LA's half-court offense;
- Austin/Iriafen win enough interior possessions;
- Citron/Amoore create more stable late-clock offense;
- LA's poor defensive baseline allows Washington to maintain a multi-possession lead.

Strongest failure path:
- Washington's back-to-back legs fail late;
- Ogwumike/Hamby dominate second chances;
- LA gets an efficient three-point/free-throw game.

Winner order:
**Washington > Los Angeles.**

The winner call is stronger than the -4.5 margin call.

---

# 14. Contract dependence

| Score | WAS -4.5 | LA +4.5 | O166.5 | U166.5 |
|---|:---:|:---:|:---:|:---:|
| WAS 86-79 | WIN | LOSS | LOSS | WIN |
| WAS 88-80 | WIN | LOSS | WIN | LOSS |
| WAS 85-82 | LOSS | WIN | WIN | LOSS |
| WAS 85-77 | WIN | LOSS | LOSS | WIN |
| LAS 84-82 | LOSS | WIN | LOSS | WIN |

Favorite cover and Over are not synonymous.
Washington can cover through defensive suppression, and LA can cover while the game goes Over.

---

# 15. Final volatile refresh

Immediately before scheduled tip:
- official WNBA game page still displayed the fixture for 10:00 PM ET with no score/play state;
- Washington's same-day status report was clean;
- Emma Cannon was Probable for Los Angeles;
- Rae Burrell and Tonie Morgan were no longer listed on the injury report;
- no confirmed starting five was recovered.

**Frozen issued state: `PREGAME` at the pre-tip evidence cutoff.**

If the game has tipped after this cutoff, this file remains the immutable pregame view; any live forecast must use current score, quarter/clock, lineups, fouls/bonus, possessions and remaining rotations.

---

# 16. Source register

## Governing Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `RULES_BASKETBALL.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

## Official/current
1. WNBA game page — Washington @ Los Angeles, game 1022600294  
   https://www.wnba.com/game/was-vs-las-1022600294
2. Washington Mystics official schedule / road-trip structure  
   https://mystics.wnba.com/news/mystics-announce-2026-regular-season-schedule
3. Washington Mystics official status report as reproduced from same-day team social: no injuries.
4. Los Angeles Sparks official site / Aug. 28 home event  
   https://sparks.wnba.com/
5. WNBA official Aug. 15 matchup page  
   https://www.wnba.com/game/las-vs-was-1022600257

## Current process / results
6. RealGM — Washington 80, Phoenix 73, Aug. 27 box score and possession/four-factor context.
7. Fox Sports — current Washington/Los Angeles matchup, recent games, current injury updates.
8. Basketball-Reference / StatMuse — recent results and H2H context.

## Market sanity check only
9. Current public market snapshots around WAS -5.5 / total 167.5.

No sportsbook price or market snapshot is used to claim internal probability, expected value, ROI or staking edge.

# P-159 (conversation-local continuation) — Arizona Diamondbacks @ San Francisco Giants — MLB — 2026-08-28

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the active `RULES_BASEBALL.md`.

**Method:** `MDS-2026.08.29-v2.5 — qualitative champion`  
**Numerical specification:** `NTS-2026.08.25-v0.2 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE`  
**Candidate policy:** `USER_SUPPLIED`  
**Operator / listed-pitcher / extra-innings terms:** `NOT SUPPLIED / UNKNOWN_DEFINITION`  
**Canonical Drive note:** the Drive combined log remains read-only and still names `P-137` as its next canonical ID. This is a conversation-local continuation and does not claim Drive reconciliation.

---

# 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | MLB — 2026 regular season |
| Event | Arizona Diamondbacks @ San Francisco Giants |
| MLB gamePk | `823178` |
| Venue | Oracle Park, San Francisco |
| Scheduled start | Friday 2026-08-28, 7:15 PM PDT / Saturday 2026-08-29, 12:15 PM AEST |
| Away / home | Arizona away; San Francisco home |
| Scheduled innings | 9 |
| Home-last-bat entitlement | San Francisco, state-dependent |
| Extra innings | Current MLB automatic-runner regime under standard research assumptions; sportsbook terms not supplied |
| Research state | `PREGAME` at the final official pre-start refresh used for this record |

## Decision set

`DECISION_SET_ID: DS-P159-V01`

| Candidate ID | Frozen contract | Geometry |
|---|---|---|
| `P-159-C01` | Diamondbacks +1.5 | Opposite-team positive handicap; overlaps SF +1.5 on every one-run final |
| `P-159-C02` | Giants +1.5 | Opposite-team positive handicap; overlaps AZ +1.5 on every one-run final |
| `P-159-C03` | Combined Total Over 8.0 | Wins 9+, **pushes exactly 8**, loses 0-7 |
| `P-159-C04` | Combined Total Under 8.0 | Wins 0-7, **pushes exactly 8**, loses 9+ |

## Margin target

`TARGET_ID: MLB-2026-823178-MARGIN-v1`

- Arizona +1.5 wins if Arizona wins or loses by exactly one.
- San Francisco +1.5 wins if San Francisco wins or loses by exactly one.
- **Both +1.5 rows win in any one-run final.**

## Total target

`TARGET_ID: MLB-2026-823178-TOTAL-RUNS-v1`

- Over 8.0: WIN at 9+, PUSH at 8, LOSS at 0-7.
- Under 8.0: WIN at 0-7, PUSH at 8, LOSS at 9+.

The 8-run push state is explicitly retained in ranking and settlement geometry.

---

# 2. Starter identity handshake

## Arizona — Kohl Drake, LHP

**Status:** `CONFIRMED_OFFICIAL`

Official current MLB line:
- 0-1
- 5.40 ERA
- 16.2 IP
- 13 SO
- 1.56 WHIP
- four MLB appearances/starts in a very small major-league sample.

Known MLB branches:
- debut: 5.0 IP, 1 ER, 5 K;
- Washington: 4.0 IP, 4 ER;
- Cleveland: 4.0 IP, 2 ER, 6 K;
- most recent outing vs San Diego: 3.2 IP, 3 ER, 6 H.

Drake therefore cannot be represented by a stable 5.40-ERA point estimate.

### Drake mixture

**Good branch**
- changeup/fastball command resembles his debut or Cleveland outing;
- roughly 4-5 innings with 1-2 runs;
- Giants' poor season production against left-handed pitching is visible.

**Ordinary branch**
- 4-ish innings;
- 2-3 runs;
- Arizona bullpen enters during the middle innings.

**Early-hook/contact branch**
- right-handed Giants damage fastball mistakes;
- Devers/Eldridge/Lee still create dangerous left-handed quality despite the platoon disadvantage;
- 3-4+ runs before/around the hook.

The baseball small-sample starter rule is therefore fully active.

## San Francisco — Blade Tidwell, RHP

**Status:** `CONFIRMED_OFFICIAL`

Official/current game listing:
- 0-0
- 3.58 ERA
- 27 SO
- approximately 32.2 MLB innings in the current role sample.

August game-log branches:
- 5.0 IP, 2 ER vs Texas;
- 5.2 IP, 1 ER at Houston;
- 4.1 IP, 6 ER vs Colorado;
- 5.2 IP, 0 ER, 7 K at Boston.

August aggregate in the retrieved Statcast log:
- 20.2 IP
- 3.92 ERA
- 1.21 WHIP
- 17 K.

Statcast current preview also shows a materially better expected-contact line than his raw historical career sample, but the role remains small enough that the Colorado blow-up branch must remain.

### Tidwell mixture

**Good branch**
- recent Boston/Houston form persists;
- 5-6 innings, 0-2 runs;
- Arizona's season weakness versus RHP is exposed.

**Ordinary branch**
- 5 innings, 2-3 runs;
- moderate bullpen exposure.

**Adverse branch**
- Arizona's current August offense and top-of-order left-handed power get to him;
- pitch count rises early;
- 3-5 runs before/through the first relief phase.

Tidwell owns the clearer starter-phase advantage, but not enough evidence for a deterministic starter edge.

---

# 3. Official posted batting orders

## Arizona

1. Lars Nootbaar — LF, L
2. Corbin Carroll — RF, L
3. Gabriel Moreno — DH, R
4. Geraldo Perdomo — SS, S
5. Tim Tawa — 1B, R
6. Jose Fernandez — 3B, R
7. James McCann — C, R
8. Ildemaro Vargas — 2B, S
9. Jordan Lawlar — CF, R

### Material absences / regime notes

- Ketel Marte is on the injured list with left-knee inflammation.
- Lourdes Gurriel Jr. remains unavailable from the active MLB lineup.
- Marte was Arizona's leading home-run and RBI producer in the retrieved season context.
- Arizona therefore enters with a weaker lineup than its full-season / full-August aggregate.

The first two hitters, Nootbaar and Carroll, provide left-handed pressure against Tidwell, with Moreno/Perdomo/Tawa carrying the middle.

## San Francisco

1. Jonah Cox — CF, R
2. Rafael Devers — 1B, L
3. Bryce Eldridge — DH, L
4. Andrew Knizner — C, R
5. Jung Hoo Lee — RF, L
6. Shay Whitcomb — 3B, R
7. Turner Hill — LF, L
8. Christian Koss — SS, R
9. Osleivis Basabe — 2B, R

### Material absences / regime notes

- Willy Adames is on the injured list with a left-elbow sprain.
- The posted order is not the same as the previous night's lineup; Drew Gilbert is not in today's posted starting nine.
- San Francisco still has Devers/Eldridge/Lee, but all three hit left-handed against Drake.

---

# 4. Team offensive process

## Arizona baseline / current regime

Current official August team hitting:
- approximately .252 AVG
- .332 OBP
- .423 SLG
- **.755 OPS**
- 110 runs in 25 August games.

Arizona has therefore been a clearly stronger August offense than San Francisco.

However:
- season-long Arizona OPS vs RHP is only approximately **.68-.69**;
- Marte and Gurriel are not in today's lineup;
- Oracle Park reduces HR/run carry.

The correct blend is:
- stronger current team offense than San Francisco;
- weaker exact RHP matchup than the raw August total suggests;
- lower ceiling than a full-strength Arizona lineup.

## San Francisco baseline / current regime

Current official August team hitting:
- approximately .227 AVG
- .295 OBP
- .375 SLG
- **.670 OPS**
- 85 runs in 24 games.

Season production against left-handed pitching is also weak:
- approximately **.66 OPS vs LHP** in the retrieved current split.

That is one of the strongest direct Under mechanisms in the card.

The Giants can still score through:
- Drake's 1.56 WHIP / short-start tail;
- right-handed Cox/Knizner/Whitcomb/Koss/Basabe;
- Devers/Eldridge power overcoming platoon disadvantage;
- middle-relief exposure.

But San Francisco does not receive a strong central scoring baseline merely because Drake's ERA is 5.40.

---

# 5. Park / weather

## Oracle Park

Baseball Savant 2024-2026 rolling factors:
- overall park factor around **97**
- run factor around **94**
- HR factor around **78-80**.

Oracle remains one of the more suppressive established MLB parks for run and especially home-run production.

## Game-window weather

National Weather Service San Francisco at roughly 7 PM PDT:
- about **62°F**
- west wind around **16 mph**
- gusts around **23 mph**
- precipitation probability about **2%**
- humidity in the low/mid-80s.

The forecast is cool and windy.

The card does **not** mechanically assign "west wind = Under" without stadium-orientation proof. The direct usable mechanism is:
- cool evening air + Oracle's established suppressive park baseline;
- elevated wind adds batted-ball variance but is not automatically directional.

Weather therefore supports a lower scoring ceiling only modestly and through the park/air branch, not as a standalone rule.

---

# 6. Bullpen / late-inning process

Current MLB relief-staff baselines:

## Arizona relievers
- ERA approximately **4.13**
- WHIP approximately **1.25**
- opponent AVG approximately .243.

Current roster includes:
- Justin Martinez, recently activated;
- Drey Jameson, recently reinstated;
- Dennis Santana and other middle-relief options.

## San Francisco relievers
- ERA approximately **4.23**
- WHIP approximately **1.42**
- opponent AVG approximately .249.

Current Statcast game preview shows available/current pitching names including:
- Dylan Smith
- Ryan Walker
- Trent Harris
- Jason Foley
- Sam Hentges
- Reiver Sanmartin
- Carson Seymour / other lower-leverage branches.

San Francisco's bullpen threw four scoreless innings in the 6-1 series opener, but one game is not converted into a new bullpen-quality prior.

### Late-game implication

Arizona has a modest team-level relief-quality edge, particularly through WHIP.

If the game reaches the sixth close:
- Arizona's stronger offense + slightly stronger bullpen improves its winner path;
- San Francisco's home-last-bat preserves the one-run and upset branches;
- neither relief corps is strong enough to eliminate a late 9+ total tail.

---

# 7. Series / context

The Giants won the series opener **6-1**.

That game:
- was 2-1 through seven innings;
- expanded only when San Francisco scored four in the eighth;
- Arizona produced only six hits;
- Giants relief threw four scoreless innings.

This is useful process evidence:
- a low-run central state and a late separation tail can coexist;
- one recent final does not establish a new team-strength rule.

Arizona remains in the NL Wild Card race and enters with the stronger season record:
- Arizona 71-64
- San Francisco 55-79.

The previous official standings snapshot had Arizona around .500 on the road and San Francisco below .500 at home. Motivation/class is a contextual prior only; it does not override the starter matchup.

---

# 8. D0 mechanism retrieval

Predeclared query:

`MLB pregame full-game margin + total -> opposite-team +1.5 overlap -> both small-sample starters -> suppressive park -> integer total with push`

**Result: `NO COMPARABLE CASE` retained from formal D0.**

Reason:
- earlier baseball cases supply generic controls, but no D0 record was sufficiently similar on the combination of two positive run lines, two small-sample MLB starters, Oracle-like environment and an integer 8.0 total.

Promoted process controls still apply:
- one coherent joint run corridor;
- small-sample starter mixture;
- explicit 2+ separation kill paths;
- integer push geometry;
- bullpen freshness ≠ bullpen quality;
- no outcome-history vote.

---

# 9. Joint run corridor

## Lower tail

Representative:
- Arizona 3-2
- San Francisco 3-2
- Arizona 4-2

Mechanism:
- Tidwell reaches good branch;
- Drake benefits from San Francisco's poor LHP split;
- Oracle suppresses HR conversion;
- bullpens avoid clusters.

## Central

Representative:
- **Arizona 4-3**
- **San Francisco 4-3**
- **Arizona 5-3**

Interpretation:
- one-run games make both +1.5 rows successful;
- 4-3 makes Under 8.0 win;
- 5-3 produces an exact **total push at 8**.

## Upper tail

Representative:
- Arizona 5-4
- Arizona 6-3
- San Francisco 5-4
- San Francisco 6-3.

Mechanism:
- Drake or Tidwell exits early;
- one bullpen inherits runners;
- HR/extra-base cluster overcomes park suppression.

## Structural tail

- 4-4 after nine → extra innings; under ordinary full-game rules the final must reach at least 9 total runs, so Over 8.0 wins once a deciding run scores.
- defensive/unearned-run cluster;
- one starter lasts fewer than four and exposes long relief.

---

# 10. Frozen ranking

| Rank | Candidate | Pick | Verdict | Evidence | Performance role | Actionability |
|---:|---|---|---|---|---|---|
| **1** | `P-159-C01` | **Arizona Diamondbacks +1.5** | `LEAN` | **MEDIUM** | `PRIMARY_FORMAL — DG-P159-MARGIN` | `NO VALUE DETERMINABLE` |
| **2** | `P-159-C02` | **San Francisco Giants +1.5** | `LEAN` | **MEDIUM** | `CORRELATED_SECONDARY — DG-P159-MARGIN` | `NO VALUE DETERMINABLE` |
| **3** | `P-159-C04` | **Combined Total Under 8.0 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P159-TOTAL` | `NO VALUE DETERMINABLE` |
| **4** | `P-159-C03` | **Combined Total Over 8.0 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P159-TOTAL` | `NO VALUE DETERMINABLE` |

All rows:
`Probability = NOT_GENERATED / NOT PUBLISHED`.

---

# 11. Rank #1 — Diamondbacks +1.5

This is the most robust supplied contract.

Arizona can:
- win outright, or
- lose by exactly one.

Why it ranks first:
1. Arizona is the substantially stronger season team.
2. Arizona's August offense is stronger than San Francisco's.
3. Arizona owns the modest bullpen-quality edge.
4. San Francisco's offense has been weak against left-handed pitching.
5. A low/moderate scoring corridor increases the relevance of one-run finals.

### Strongest kill path

San Francisco wins by **2+**.

The cleanest ordinary route:
- Tidwell repeats his Boston/Houston good branch;
- Drake's short-start/contact branch appears;
- Giants score 3-4 early;
- home bullpen protects/extends.

Representative:
- SF 5-2
- SF 5-3
- SF 6-3.

That branch is substantial enough to prevent a stronger evidence label.

---

# 12. Rank #2 — Giants +1.5

San Francisco +1.5 is also a genuine LEAN.

Support:
1. Tidwell has the stronger starter-phase evidence.
2. San Francisco owns home-last-bat.
3. Oracle compresses the ordinary scoring corridor.
4. Arizona's lineup is missing Marte and Gurriel.
5. A one-run Arizona win still cashes Giants +1.5.

### Strongest kill path

Arizona wins by **2+**.

The route:
- Nootbaar/Carroll create traffic against Tidwell;
- Tidwell's Colorado-style contact/walk branch appears;
- Arizona reaches the 4.23/1.42 Giants relief baseline;
- Drake does enough against SF's poor LHP offense.

Representative:
- AZ 5-2
- AZ 5-3
- AZ 6-3.

Giants +1.5 remains below Arizona +1.5 because Arizona is still the preferred winner and carries the stronger team/offense profile.

---

# 13. Rank #3 — Under 8.0

This is a narrow lower-total direction.

### Under mechanisms

- Oracle Park: roughly 94 run factor / 78-80 HR factor in the rolling Statcast view.
- San Francisco: approximately .66 OPS vs LHP.
- Giants August offense: roughly .670 OPS.
- Tidwell has three relatively strong starts in four current August outings.
- Arizona lacks Marte and Gurriel.
- cool 62°F game-window environment.

Winning Under scores:
- 3-2
- 4-2
- 4-3.

### Important integer geometry

Exactly **8 runs is not an Under loss**:
- 5-3
- 4-4 before extras / if operator settlement somehow stops at regulation under special terms
produce the line-specific push state under the frozen eight-run boundary, subject to exact operator full-game terms.

### Strongest kill path

Either rookie exits early and the bullpens inherit traffic.

Representative:
- 5-4
- 6-3
- 6-4.

Current public market snapshots also converged near an 8-run total and were close to balanced. That is a sanity warning against describing the Under as a strong edge.

---

# 14. Rank #4 — Over 8.0

The Over has credible support:

- Drake 5.40 ERA / 1.56 WHIP in a small MLB sample.
- Tidwell has a six-run blow-up in his recent four-start window.
- both bullpens carry ERAs above 4.
- Arizona's August offense remains productive despite the current missing bats.
- extra innings strongly favor 9+ if regulation reaches 4-4.
- yesterday's 6-1 game showed San Francisco can add a late four-run cluster.

Why it remains fourth:
- nine runs are required for a win;
- exactly eight is only a push;
- Oracle suppresses HRs/runs;
- SF's lefty split is poor;
- Tidwell owns the cleaner central starter state.

The Over is a live adverse branch, not an `AVOID`, but it is the least robust of the supplied rows.

---

# 15. Potential winner

## Arizona Diamondbacks — `LEAN / MEDIUM-LOW`

### Central mechanism

Arizona is preferred outright because:
- stronger overall club;
- better current August offense;
- modest bullpen-quality advantage;
- San Francisco's lefty weakness makes Drake's good/ordinary branches more playable than his raw 5.40 ERA suggests.

### Strongest failure path

Tidwell controls the first 5-6 innings and Drake fails early.

San Francisco then leverages:
- home last-bat;
- Devers/Eldridge middle-order damage;
- current home-field sequence.

Representative:
- SF 4-3
- SF 5-3.

The starter matchup is sufficiently pro-Giants that the winner is only `MEDIUM-LOW`, weaker than Arizona +1.5.

---

# 16. Scenario / dependence table

| Scenario | Score | AZ +1.5 | SF +1.5 | O8.0 | U8.0 |
|---|---:|:---:|:---:|:---:|:---:|
| Central Arizona close win | AZ 4-3 | WIN | WIN | LOSS | WIN |
| Central Giants close win | SF 4-3 | WIN | WIN | LOSS | WIN |
| Arizona moderate separation | AZ 5-3 | WIN | LOSS | PUSH | PUSH |
| Giants moderate separation | SF 5-3 | LOSS | WIN | PUSH | PUSH |
| Arizona upper tail | AZ 5-4 | WIN | WIN | WIN | LOSS |
| Giants upper tail | SF 5-4 | WIN | WIN | WIN | LOSS |
| Arizona wide win | AZ 6-3 | WIN | LOSS | WIN | LOSS |
| Giants wide win | SF 6-3 | LOSS | WIN | WIN | LOSS |

The two +1.5 rows are positively dependent through one-run finals; they are **not opposite bets**.

---

# 17. Source register

## Governing Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md` — UGR-2026.08.25-v1
- `RULES_BASEBALL.md`
- `PREDICTION_LOG_COMBINED.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`

## Official MLB / Statcast
1. MLB probable pitchers — Aug. 28, 2026  
   https://www.mlb.com/probable-pitchers/2026-08-28
2. MLB official starting lineups — Aug. 28  
   https://www.mlb.com/es/starting-lineups/2026-08-28
3. D-backs probable pitchers  
   https://www.mlb.com/dbacks/roster/probable-pitchers
4. Giants probable pitchers  
   https://www.mlb.com/giants/roster/probable-pitchers
5. Kohl Drake official MLB profile  
   https://www.mlb.com/player/kohl-drake-684442
6. MLB Kohl Drake debut highlight / official outing note  
   https://www.mlb.com/video/kohl-drake-strikes-out-five-in-mlb-debut
7. Baseball Savant Blade Tidwell game log / current profile  
   https://baseballsavant.mlb.com/savant-player/blade-tidwell-694918
8. Baseball Savant game preview — gamePk 823178  
   https://baseballsavant.mlb.com/preview?game_date=2026-08-28&game_pk=823178
9. Baseball Savant park factors  
   https://baseballsavant.mlb.com/leaderboard/statcast-park-factors?rolling=3&stat=index_wOBA&type=year&year=2026
10. MLB August team hitting stats  
    https://www.mlb.com/stats/team/ops?split=8
11. MLB reliever team pitching stats  
    https://www.mlb.com/stats/team/pitching/regular-season?split=rp
12. D-backs injuries / roster moves  
    https://www.mlb.com/dbacks/news/d-backs-injuries-and-roster-moves
13. Giants injuries / roster moves  
    https://www.mlb.com/giants/news/giants-injuries-and-roster-moves
14. MLB Aug. 27 D-backs 1, Giants 6 official game summary  
    https://www.mlb.com/video/game/823179

## Weather
15. National Weather Service San Francisco hourly forecast  
    https://forecast.weather.gov/MapClick.php?FcstType=digital&lat=37.7749&lg=english&lon=-122.4194&unit=0

## Secondary/statistical corroboration
16. StatMuse — Arizona vs RHP and San Francisco vs LHP splits
17. Reuters / San Francisco Chronicle — Aug. 27 series opener context

## Market sanity check only
18. FanDuel / BetMGM / Action Network current public snapshots around AZ slight favorite and total 7.5-8.0.

Market prices are not used to create internal probabilities, expected value, ROI or staking recommendations.

# P-160 (conversation-local continuation) — Sultanes de Monterrey @ Toros de Tijuana — LMB Final de Zona Norte Game 1 — 2026-08-28

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the active `RULES_BASEBALL.md`.

- **Method:** `MDS-2026.08.29-v2.5 — qualitative champion`
- **Numerical specification:** `NTS-2026.08.25-v0.2 — Stage 0 / pre-fit`
- **League population:** Liga Mexicana de Béisbol (LMB), treated separately from MLB/NPB/KBO priors
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Candidate policy:** `USER_SUPPLIED`
- **Operator/action/extra-inning terms:** `NOT SUPPLIED / UNKNOWN_DEFINITION`
- **Lineup status:** official Game 1 batting orders were not recovered before cutoff; no preview lineup is treated as confirmed.

---

## 1. Event / time freeze

| Field | Frozen value |
|---|---|
| Competition | LMB 2026 — Serie de Campeonato / Final de Zona Norte, Game 1 |
| Event | Sultanes de Monterrey @ Toros de Tijuana |
| Venue | Toros Mobil Park, Tijuana |
| Home team | Tijuana |
| Revised start | 20:05 Tijuana PDT / 21:05 Monterrey-CDMX CDT |
| Melbourne | 13:05 AEST, 2026-08-29 |
| State at cutoff | `PREGAME` |
| Starter MTY | Manny Bañuelos, LHP — `CONFIRMED_OFFICIAL` |
| Starter TIJ | Adonis Medina, RHP — `CONFIRMED_OFFICIAL` |

Earlier Toros material listed 19:35 Tijuana. Current league-aligned sources report a 30-minute TV adjustment to 20:05 Tijuana; the later/current schedule controls this view.

### Supplied contracts

1. Monterrey +1.5
2. Tijuana -1.5
3. Over 8.5
4. Under 8.5

Margin geometry:
- MTY +1.5 wins on every Monterrey win and every one-run Tijuana win.
- TIJ -1.5 requires a Tijuana win by 2+.

Total geometry:
- Over 8.5 wins at 9+.
- Under 8.5 wins at 0-8.

---

## 2. Starter process

### Manny Bañuelos — Monterrey

Official 2026 regular season:
- 7-5
- 4.25 ERA
- 17 GS
- 82.2 IP
- 71 H
- 39 ER
- 10 HR
- 32 BB
- 70 SO
- 1.25 WHIP.

Current Toros-published postseason line:
- **2-0, 1.42 ERA**.

Recent strong branch:
- 7 IP, 0 R, 2 H, 1 BB, 4 K vs Charros.

Mixture:
- **Good/current:** 5-7 effective innings, 0-2 runs.
- **Ordinary:** ~5 innings, 2-3 runs.
- **Adverse:** regular-season contact/HR branch reappears, 3-5 runs.

### Adonis Medina — Tijuana

Official 2026:
- 8-2
- **2.86 ERA**
- 15 GS
- 78.2 IP
- 67 H
- 25 ER
- 5 HR
- 22 BB
- 77 SO
- **1.13 WHIP**.

Current postseason line:
- **0-0, 2.35 ERA**.

Recent postseason evidence includes four hitless innings to begin a Charros start, but another playoff start lasted only 2.2 innings with four walks.

Mixture:
- **Good:** 5-6+ innings, 1-2 runs.
- **Ordinary:** ~5 innings, 2-3 runs.
- **Short-start/command:** walks inflate pitch count and expose middle relief.

Medina has the stronger full-season prior. Bañuelos has the stronger current postseason result branch.

---

## 3. Same-starter matchup

Official LMB, May 30 at Toros Mobil Park:

**Monterrey 2, Tijuana 0**

- Bañuelos: **7.0 IP, 2 H, 0 R, 7 K**
- Medina: **6.1 IP, 2 H, 2 R, 9 K**
- both bullpens completed the shutout/scoreless finish.

This is unusually relevant because it matches clubs, venue, starters and season, but it is **not** used as a deterministic template.

---

## 4. Team-quality / postseason regime

### Tijuana
Regular season:
- **60-31**, first in Zona Norte.
- official club reporting: **3.28 team ERA**, best in LMB.
- **822 strikeouts**, league-leading staff.

Tijuana also displayed a deep current playoff relief chain in its 3-2, 10-inning clincher over Charros:
Jorge Pérez → Brady Feigl → Juan Hillman → Jonathan Aro → Adbert Alzolay → Brett de Geus.

### Monterrey
Regular season:
- **49-44**, third in Zona Norte.

Current official leaders:
- Gustavo Núñez .321 AVG
- Josh Lester 15 HR
- Víctor Mendoza 67 RBI
- Núñez 61 R / 30 SB.

Postseason:
- 4-1 over Charros
- 4-1 over Durango.

Official Sultanes preview:
- Omar Narváez **.441 postseason AVG, 15 hits, 1.118 OPS**.

Monterrey is therefore much hotter than its regular-season record alone implies.

---

## 5. Recent scoring regimes

### Toros vs Charros
Recent totals:
- 4
- 8
- 3
- 9
- 5.

This is not used as a raw Under trend. It aligns with direct pitching evidence: best LMB regular-season staff ERA plus a deep playoff relief chain.

### Sultanes vs Durango
Recent series included:
- 6-2
- 5-17
- 8-7
- 3-0
- 8-6.

That demonstrates both:
- a high Monterrey offensive ceiling;
- a real pitcher-dominant lower tail.

---

## 6. Venue / weather

No trustworthy versioned LMB park-factor model was recovered for Toros Mobil Park, so no numerical park adjustment is invented.

Tijuana game-window weather:
- about 79°F at 8 PM
- clear
- west wind around 5 mph
- ~1% rain.

Weather is benign and approximately neutral for direction.

---

## 7. Joint run corridor

### Lower tail
- TIJ 3-2
- MTY 3-2
- TIJ 4-2
- MTY 4-2

### Central
- **TIJ 4-3**
- **MTY 4-3**
- **TIJ 5-3**

### Upper tail
- TIJ 5-4
- MTY 5-4
- TIJ 6-3
- MTY 6-4

The central corridor is intentionally close because both starting-pitcher branches and Toros' relief depth suppress the clean separation path.

---

## 8. Final ranking

Because official Game 1 batting orders were not recovered, participant completeness is limited. Under the Drive baseball rules, confidence is capped.

| Rank | Pick | Verdict | Evidence | Role |
|---:|---|---|---|---|
| **1** | **Monterrey +1.5** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — MARGIN` |
| **2** | **Under 8.5** | `FORCED RANK` | **MEDIUM-LOW** | `PRIMARY_FORMAL — TOTAL` |
| **3** | **Over 8.5** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — TOTAL` |
| **4** | **Tijuana -1.5** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — MARGIN` |

All rows:
- `Probability: NOT_GENERATED / NOT PUBLISHED`
- `Actionability: NO VALUE DETERMINABLE`

---

## 9. Rank #1 — Monterrey +1.5

Why first:
- Bañuelos is 2-0 with a 1.42 postseason ERA.
- He already produced 7 scoreless innings against Tijuana at this venue in the exact Medina matchup.
- Monterrey is 8-2 across the first two playoff rounds.
- the +1.5 cushion wins on a one-run Toros victory.
- a lower/moderate run environment increases one-run-game relevance.

Strongest kill path:
Medina controls Monterrey, Bañuelos reverts toward his 4.25 regular-season branch, and Toros' bullpen protects a multi-run lead.

Kill scores:
- TIJ 4-2
- TIJ 5-3
- TIJ 6-3.

---

## 10. Rank #2 — Under 8.5

Support:
- Medina 2.86 ERA / 1.13 WHIP in the regular season.
- Bañuelos 1.42 postseason ERA.
- Toros 3.28 team ERA, best in LMB.
- current Toros playoff relief depth.
- exact Bañuelos-Medina matchup finished 2-0.
- most recent Toros series was generally low-scoring.

Central Under:
- 3-2
- 4-2
- 4-3
- 5-3.

Strongest kill path:
Monterrey's hot offense elevates Medina's pitch count, or Bañuelos' regular-season contact branch returns and both middle bullpens are exposed.

Over scores:
- 5-4
- 6-3
- 6-4.

The user's 8.5 is also lower than a contemporaneous public total around 9.0, so the Under direction is **narrow**, not strong.

---

## 11. Rank #3 — Over 8.5

Support:
- Monterrey's postseason offense is hot.
- Medina has a real walk/short-start branch.
- Bañuelos' season ERA is 4.25 despite his playoff surge.
- Monterrey's late relief is less structurally secure than Tijuana's.
- exactly 5-4 clears the total.

Why third:
the event-specific starting matchup and Toros' team pitching baseline provide stronger direct suppression evidence than a generic LMB run-environment argument.

---

## 12. Rank #4 — Tijuana -1.5

Tijuana is the preferred winner, but -1.5 is the hardest side contract.

Support:
- 60-31 regular season.
- best team ERA in LMB.
- Medina's stronger full-season line.
- home last bat.
- deeper recent playoff bullpen.

Why fourth:
a plausible **TIJ 4-3** makes the winner call correct but -1.5 lose. Bañuelos' current playoff form directly compresses the separation branch.

---

## 13. Potential winner

### **Tijuana — FORCED WINNER / MEDIUM-LOW**

Central mechanism:
- better full-season team;
- Medina's stronger regular-season starter profile;
- best pitching staff in the league;
- home last bat;
- deep relief chain.

Strongest failure path:
Bañuelos maintains postseason form and Monterrey's hot offense creates the decisive cluster. That path is real: Bañuelos already beat Medina 2-0 in Tijuana this season.

Thus:
- **Winner: Tijuana > Monterrey**
- **But: Monterrey +1.5 > Tijuana -1.5**

No contradiction exists between those statements.

---

## 14. Scenario map

| Score | MTY +1.5 | TIJ -1.5 | O8.5 | U8.5 |
|---|:---:|:---:|:---:|:---:|
| TIJ 4-3 | WIN | LOSS | LOSS | WIN |
| MTY 4-3 | WIN | LOSS | LOSS | WIN |
| TIJ 4-2 | LOSS | WIN | LOSS | WIN |
| TIJ 5-3 | LOSS | WIN | LOSS | WIN |
| TIJ 5-4 | WIN | LOSS | WIN | LOSS |
| MTY 5-4 | WIN | LOSS | WIN | LOSS |
| TIJ 6-3 | LOSS | WIN | WIN | LOSS |

---

## 15. Source register

### Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `RULES_BASEBALL.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

### Official LMB / clubs
- Sultanes Game 1 preview / starters and current postseason context.
- LMB Championship Series schedule.
- Toros Championship Series pitching preview.
- Adonis Medina official LMB player page.
- Manny Bañuelos official LMB player page.
- Official LMB May 30 game: Monterrey 2-0 Tijuana.
- Toros official postseason preview: 60-31, 3.28 team ERA, 822 strikeouts.
- Toros official Charros clincher / relief chain.
- LMB Toros and Sultanes team/roster pages.
- Sultanes official Durango-clincher report.

### Weather
- Weather.com Tijuana hourly forecast.

### Market sanity only
- contemporaneous public snapshot around Tijuana slight favorite / total 9.0.

Market data is not used to generate probabilities, EV, ROI or staking claims.

# P-162 (conversation-local continuation) — Rigele Te vs Chase Ferguson — M15 Maanshan — 2026-08-29

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and the active `RULES_TENNIS.md`.

- **Method:** `MDS-2026.08.29-v2.5 — qualitative champion`
- **Numerical state:** `NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL IS APPROVED OR FIT`
- **Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value:** `NO VALUE DETERMINABLE`
- **Candidate origin:** `USER_SUPPLIED`
- **Operator:** `NOT SUPPLIED`
- **Retirement / completed-set / walkover terms:** `UNKNOWN_DEFINITION`
- **Competition population:** ITF Men's World Tennis Tour M15
- **Surface:** Indoor hard
- **Round:** Semifinal
- **Best-of format:** best of three sets under normal ITF singles rules

---

## 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Event | Rigele Te vs Chase Ferguson |
| Tournament | M15 Maanshan, China |
| Dates | 24 Aug – 30 Aug 2026 |
| Surface | Indoor hard |
| Round | Semifinal |
| Current state | `PREGAME` at final research cutoff |
| Earliest current published start branch | 03:30 UTC / 13:30 AEST |
| Alternative current book listing | 04:00 UTC / 14:00 AEST |
| Final evidence cutoff | approx. 13:10 AEST |
| Retirement settlement | unknown because operator was not supplied |

The official ITF calendar confirms the current M15 Maanshan week and indoor-hard surface. A directly retrievable official current order-of-play page was not recovered, so the current start time is treated as a schedule branch rather than falsely labelled official. The earliest current published branch was still in the future at cutoff.

---

## 2. Decision set

`DECISION_SET_ID: DS-P162-V01`

| Candidate | Frozen contract | Geometry |
|---|---|---|
| `P-162-C01` | Rigele Te -2.5 games | exact complement of Ferguson +2.5 if match completes under matching terms |
| `P-162-C02` | Chase Ferguson +2.5 games | exact complement of Te -2.5 |
| `P-162-C03` | Total Games Over 22.5 | exact complement of Under 22.5 |
| `P-162-C04` | Total Games Under 22.5 | exact complement of Over 22.5 |

Because retirement terms are unknown, all four rows are `UNKNOWN_DEFINITION` for retirement settlement and `NO VALUE DETERMINABLE`.

---

## 3. Official player baseline

### Rigele Te

Official ITF profile snapshot:
- China
- age 28
- right-handed
- preferred surface: hard
- ATP ranking on 27 Jul 2026: **1009**
- 2026 professional record: **12-13**
- 2026 hard record: **12-13**.

Te's ranking is materially below Ferguson's, so this forecast does **not** rely on ranking superiority.

### Chase Ferguson

Official ITF profile snapshot:
- Australia
- age 27
- ATP ranking on 27 Jul 2026: **640**
- career-high ranking at that date: **640**
- 2026 professional record: **16-15**
- 2026 hard record: **16-15**.

The broad ranking/surface prior therefore favors Ferguson.

The current tournament and direct-matchup evidence point in the opposite direction, which requires a widened distribution rather than silently choosing one regime.

---

## 4. Current M15 Maanshan tournament path

### Te

R1:
- beat Anmar Faleh Alhogbani **6-4 6-1**

R2:
- beat Xirui Han **6-0 6-4**

QF:
- beat Joshua Charlton **6-4 6-3**

Current event:
- **3-0 matches**
- **6-0 sets**
- 52 total games played.

Every current win:
- covered Te -2.5 games;
- finished Under 22.5.

### Ferguson

R1:
- beat Y. Taka **6-3 7-6(4)**

R2:
- beat Hanyi Liu **6-3 6-2**

QF:
- beat Fumin Jiang **5-7 6-4 6-3**

Current event:
- **3-0 matches**
- 6 sets won, 1 lost
- 70 total games played.

Ferguson therefore enters after:
- one more set this week;
- **18 more games** than Te;
- a 31-game three-set quarterfinal yesterday versus Te's 19-game straight-set quarterfinal.

Workload is not automatically negative, but it gives Te the cleaner recovery/exposure state.

---

## 5. Current-event serve/return regime

A specialist current-event feed reports:

### Te
- service hold: approximately **94%**
- opponent hold: approximately **44%**

### Ferguson
- service hold: approximately **84%**
- opponent hold: approximately **63%**.

This is a small-tournament, small-sample snapshot and is therefore shrunk heavily toward broader ITF hard-court priors.

It nevertheless supports the direct visual result pattern:
- Te has not dropped a set;
- Te has repeatedly created separation without needing tiebreak-heavy sets;
- Ferguson has been more exposed to long-set / deciding-set paths.

Broader aggregate serve data are much closer:
- Te historical/current aggregate hold around 73-74%;
- Ferguson around 73%;
- Ferguson's aggregate return-point profile is at least as strong or slightly better.

Therefore the tournament-specific gap is treated as a **current regime branch**, not permanent player quality.

---

## 6. Head-to-head continuity audit

Te leads the available H2H **3-0 in matches and 6-0 in sets**.

### March 2026 — M15 Maanshan, indoor hard
Te won:
- **6-4 7-5**
- total games: **22**
- Te game margin: **+4**

This is the highest-value H2H because it matches:
- current venue/city;
- same indoor-hard environment;
- same ITF level;
- same season;
- same players.

It supports:
- Te -2.5
- Under 22.5.

### May 2024 — M25 Baotou, clay
Te won:
- **6-3 6-4**
- total games: **19**
- Te margin: **+5**

Surface/level differs, so it is reduced to secondary continuity evidence.

### July 2022 — M15 Monastir, hard
Te won:
- **6-2 6-1**
- total games: **15**
- Te margin: **+9**

This is old and receives very little current weight.

### H2H conclusion

All three historical meetings:
- Te -2.5 would have won;
- Under 22.5 would have won.

But the forecast does **not** convert "3-0" into a standalone probability. The March 2026 same-venue/surface meeting is the meaningful piece; the older two mainly show matchup continuity.

---

## 7. March 2026 same-venue serve/return details

In the 6-4 7-5 Te win:

### Te
- 7 aces
- 3 double faults
- 47% first serve in
- **87% first-serve points won**
- 47% second-serve points won
- saved 4 of 6 break points.

### Ferguson
- 0 aces
- 0 double faults
- 66% first serve in
- 59% first-serve points won
- 52% second-serve points won
- saved 4 of 8 break points.

Te's first-serve efficiency was the key separator despite a low first-serve-in percentage.

The strongest Ferguson counter-mechanism is:
- improve first-serve conversion;
- use his return profile to attack Te's second serve;
- turn the match into repeated 5-5 / tiebreak / deciding-set states.

That is credible and central to the +2.5 / Over kill paths.

---

## 8. Current-regime reconciliation

### Why Te's current form matters
- six straight sets won this week;
- all three victories by at least three net games;
- no tiebreaks needed;
- same-venue/surface H2H already favors Te;
- lighter quarterfinal workload.

### Why Ferguson cannot be dismissed
- ATP ranking roughly 640 versus Te 1009 in the latest official snapshot;
- stronger broad 2026 hard-court record;
- current event includes a 7-6 set and a successful three-set recovery;
- broader return data are competitive;
- higher-ranking / broader hard prior suggests the gap is smaller than a pure H2H reading.

### Forecast implication
The qualitative distribution is centered on **Te being the better match winner**, but with a meaningful Ferguson competitive/deciding-set branch.

---

## 9. Joint score tree

### Te ordinary straight-set control
Representative:
- **6-4 6-3** → 19 games, Te +5
- **6-4 6-4** → 20 games, Te +4
- **6-4 7-5** → 22 games, Te +4

Supports:
- Te -2.5
- Under 22.5.

### Te close straight sets
Representative:
- **7-6 6-4** → 23 games, Te +3
- **7-6 7-5** → 25 games, Te +3

Supports:
- Te -2.5
- Over 22.5.

This branch is important: Te can cover -2.5 while the total goes Over.

### Te deciding-set win
Representative:
- **6-4 4-6 6-4** → 30 games, Te +2
- **7-5 3-6 6-3** → 30 games, Te +4

Depending on third-set separation:
- Over 22.5 is strongly supported;
- Ferguson +2.5 can survive a narrow Te three-set win;
- Te -2.5 can still cover if the deciding-set separation is large enough.

### Ferguson win
Representative:
- Ferguson **7-5 6-4** → 22 games
- Ferguson **7-6 6-4** → 23 games
- Ferguson **4-6 6-4 6-3** → 29 games.

Every Ferguson win:
- Ferguson +2.5 wins.
Three-set / tiebreak variants usually support Over.

---

## 10. Final ranking

| Rank | Candidate | Pick | Verdict | Evidence | Performance role | Actionability |
|---:|---|---|---|---|---|---|
| **1** | `P-162-C01` | **Rigele Te -2.5 Games** | `LEAN` | **MEDIUM** | `PRIMARY_FORMAL — DG-P162-HANDICAP` | `NO VALUE DETERMINABLE` |
| **2** | `P-162-C04` | **Under 22.5 Total Games** | `LEAN` | **MEDIUM-LOW** | `PRIMARY_FORMAL — DG-P162-TOTAL` | `NO VALUE DETERMINABLE` |
| **3** | `P-162-C02` | **Chase Ferguson +2.5 Games** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P162-HANDICAP` | `NO VALUE DETERMINABLE` |
| **4** | `P-162-C03` | **Over 22.5 Total Games** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — DG-P162-TOTAL` | `NO VALUE DETERMINABLE` |

All rows:
- `Probability = NOT_GENERATED / NOT PUBLISHED`
- retirement settlement remains `UNKNOWN_DEFINITION`.

---

## 11. Rank #1 — Te -2.5 games

Why first:
1. Te has won all three matches this week in straight sets.
2. All three current matches cleared -2.5.
3. Te leads Ferguson 3-0 H2H / 6-0 sets.
4. The most relevant same-venue/surface meeting was Te 6-4 7-5, a +4 margin.
5. Te has played 18 fewer games this week and had the shorter quarterfinal.
6. Current-event hold/break data favor Te.

Strongest kill path:
- Ferguson's higher-ranking/broader-hard prior expresses itself;
- Ferguson serves more efficiently than in the March H2H;
- Te's first-serve percentage remains low enough for Ferguson to attack second serves;
- the match goes three sets or Ferguson wins outright.

Representative failures:
- Te 6-4 4-6 6-4 → Te margin +2, handicap loses.
- Ferguson 7-6 6-4 → Ferguson wins outright.

---

## 12. Rank #2 — Under 22.5 games

Why second:
- Te's three current matches totaled **17, 16, 19**.
- the March 2026 same-venue H2H totaled **22**.
- all three historical H2Hs finished Under 22.5.
- Te's central winning tree is a two-set, one-break-per-set type match.

Representative wins:
- 6-4 6-3 = 19
- 6-4 6-4 = 20
- 6-4 7-5 = 22.

Strongest kill path:
- a tiebreak plus a 6-4 set already creates **23**;
- any normal three-set match almost certainly clears 22.5.

Representative:
- 7-6 6-4 = 23
- 6-4 4-6 6-4 = 30.

Thus Under 22.5 is more fragile than Te -2.5.

---

## 13. Rank #3 — Ferguson +2.5 games

This is the strongest contrary side.

Support:
- Ferguson's official ATP ranking is materially higher.
- his broader 2026 hard-court record is better.
- he has already shown two different competitive pathways this week: a tiebreak set and a three-set comeback.
- any Ferguson outright win automatically cashes +2.5.
- a narrow Te three-set win can also cash it.

Why below Te -2.5:
- current-event process favors Te;
- same-venue current-season H2H favors Te;
- Te has won every set this week;
- all three historical H2Hs exceed the -2.5 separation threshold.

---

## 14. Rank #4 — Over 22.5 games

Over needs:
- at least one very close straight-set structure such as 7-6 6-4; or
- a deciding set.

Support:
- Ferguson can force tiebreaks;
- Ferguson played 31 games yesterday;
- his three-set route is established;
- ranking/broad-hard evidence argues against assuming another easy Te straight-set win.

Why fourth:
- Te's current six-set sweep is the strongest event-specific regime.
- the March same-venue H2H stopped at 22.
- Te's current scores have not approached 23 games.

The Over remains a real branch but is the least robust of the four supplied rows.

---

## 15. Potential match winner

### **Rigele Te — LEAN / MEDIUM**

Central mechanism:
- stronger current-event serve/return control;
- three straight-set wins;
- current same-venue H2H edge;
- lighter workload;
- repeated evidence that Te can create a one-break-per-set margin against Ferguson.

Strongest failure path:
- Ferguson's higher-ranking/broader-hard prior reasserts;
- he attacks Te's second serve more effectively;
- he turns the match into a tiebreak/third-set contest and wins the late pressure points.

Winner order:
**Te > Ferguson**, but not by enough evidence to call the match low-variance.

---

## 16. Scenario map

| Score | Te -2.5 | Ferguson +2.5 | O22.5 | U22.5 |
|---|:---:|:---:|:---:|:---:|
| Te 6-4 6-3 | WIN | LOSS | LOSS | WIN |
| Te 6-4 6-4 | WIN | LOSS | LOSS | WIN |
| Te 6-4 7-5 | WIN | LOSS | LOSS | WIN |
| Te 7-6 6-4 | WIN | LOSS | WIN | LOSS |
| Te 6-4 4-6 6-4 | LOSS | WIN | WIN | LOSS |
| Ferguson 7-5 6-4 | LOSS | WIN | LOSS | WIN |
| Ferguson 7-6 6-4 | LOSS | WIN | WIN | LOSS |
| Ferguson 4-6 6-4 6-3 | LOSS | WIN | WIN | LOSS |

---

## 17. Final volatile refresh

At the final research cutoff:
- current fixtures still showed Te vs Ferguson as upcoming;
- no live score was returned;
- the earliest current published start branch was 03:30 UTC / 13:30 AEST;
- another current sportsbook listed 04:00 UTC / 14:00 AEST;
- the official ITF calendar confirms the current Maanshan M15 week and indoor-hard surface;
- no current withdrawal/retirement report was found.

**Frozen state:** `PREGAME`.

If the actual match starts before the later listed time, this record remains the immutable pre-match view. A live reissue would need the exact set/game/point score, server and medical state.

---

## 18. Final answer summary

1. **Rigele Te -2.5 Games — LEAN / MEDIUM**
2. **Under 22.5 Total Games — LEAN / MEDIUM-LOW**
3. **Chase Ferguson +2.5 Games — FORCED RANK / MEDIUM-LOW**
4. **Over 22.5 Total Games — FORCED RANK / MEDIUM-LOW**

**Potential winner:** **Rigele Te — LEAN / MEDIUM**

No internal probability, expected value, ROI or staking recommendation is published.

---

## 19. Source register

### Governing Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `RULES_TENNIS.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md`

### Official ITF
- ITF Men's World Tennis Tour calendar — current M15 Maanshan week / indoor hard.
- Rigele Te official ITF profile.
- Chase Ferguson official ITF profile.
- ITF current/historical tournament pages where retrievable.

### Specialist statistical / score cross-checks
- Tennis Abstract — 2026 player match logs and March 2026 Te-Ferguson match.
- Stevegtennis — current player service/return aggregates and H2H.
- Tennis Explorer — current Maanshan match path.
- BsportsFan / current fixture page — current semifinal fixture and quarterfinal scores.
- MatchStat — current-event hold/break snapshot; treated as secondary and small-sample.

### Market sanity only
- Betfair current match odds: Te listed as favorite.
- Other public current match listings used only to cross-check schedule state.

No market source is used to generate an internal probability or value claim.

# P-163 (conversation-local continuation) — Adelaide Crows (W) vs West Coast Eagles (W) — AFLW Round 3 — 2026-08-29

## Decision outcome

**RANKED FORECAST — NO BET ENDORSED**

Method: MDS-2026.08.29-v2.5 — qualitative champion  
Numerical state: NTS-2026.08.25-v0.2 — design only; no AFL/AFLW model is fit  
Probability: NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
Value: NO VALUE DETERMINABLE  
Operator / draw / overtime settlement: NOT SUPPLIED / UNKNOWN_DEFINITION

## Event freeze

- Competition: 2026 NAB AFLW Premiership Season, Round 3
- Event: Adelaide Crows / Kuwarna v West Coast Eagles / Waalitj Marawar
- Venue: Unley Oval / Thomas Farms Oval, Adelaide
- Scheduled bounce: 2:05pm ACST / 2:35pm AEST
- Frozen research state: PREGAME
- Candidate horizon: full match

## Supplied contracts

1. Adelaide -21.5
2. West Coast +21.5
3. Over 93.5
4. Under 93.5

Geometry:
- Adelaide -21.5 requires Adelaide by 22+.
- West Coast +21.5 wins on a West Coast win or Adelaide by 21 or fewer.
- Over 93.5 wins at 94+.
- Under 93.5 wins at 93 or fewer.

## Current teams / availability

Adelaide official Round 3 changes:
- IN: Grace Kelly, India Rasheed
- OUT: Amy Boyle-Carr, Brooke Tonon (omitted)

Kelly returns from hamstring trouble and adds forward speed/experience. Rasheed returns after a conditioning block; coach Ryan Davis noted she kicked seven goals in a scrimmage, which is readiness evidence rather than an AFLW scoring-rate sample.

Current Adelaide injury context includes Kiera Mueller out for the season after patella-tendon surgery. The broader 2026 roster is materially different from the old premiership-era core, so historical Adelaide strength is not used mechanically.

West Coast official Round 3 changes:
- IN: Charlie Thomas, Lisa Steane
- OUT: Roxy Roux (managed), Mia Russo (omitted)

Thomas returns after illness caused a late Round 2 withdrawal, materially strengthening aerial defence and defensive organisation.

West Coast's injury list includes Kayla Dalgleish, Liz McGrath, Lily Paterson, Jess Rentsch, Courtney Rowley, Lily Smart and Mikayla Western.

No verified AFLW late-change notice was recovered before the frozen cutoff.

## Current scoreboard baseline

Adelaide:
- R1: Adelaide 53, Sydney 61 — total 114
- R2: Adelaide 23, Carlton 50 — total 73
- Through two: 38.0 points for per game, 55.5 against, average game total 93.5

West Coast:
- R1: West Coast 42, GWS 54 — total 96
- R2: West Coast 34, Gold Coast 69 — total 103
- Through two: 38.0 points for per game, 61.5 against, average game total 99.5

## Adelaide territory -> scoring chain

The key current process signal is Round 2. Adelaide won inside-50s 41-29 against Carlton but lost 50-23, with only eight scoring shots to Carlton's 15.

Coach Ryan Davis identified shallow/high entries, poor delivery to targets and risky corridor use. This separates territory strength from scoreboard efficiency.

Grace Kelly and India Rasheed can improve the forward phase, but one selection change does not prove the conversion problem is fixed.

## West Coast process

Round 1: West Coast lost 54-42 to GWS after kicking the last three goals once the margin had blown out.

Round 2: West Coast lost 69-34 to Gold Coast after a seven-goal-to-one first half.

This gives both:
- a competitive / late-compression branch;
- a genuine separation-loss branch.

Charlie Thomas' return strengthens the former.

## Historical matchup — descriptive only

2025:
- Adelaide 48
- West Coast 31
- Adelaide by 17
- total 79
- Adelaide inside-50s 43-23

Adelaide led by 36 early in the final quarter before West Coast kicked the last three goals.

This is useful because it demonstrates that major Adelaide territory dominance can still finish inside +21.5. It is not a direct 2026 baseline because Adelaide's coach, personnel and game style have changed.

## Venue / weather

BOM forecast for Unley / Adelaide:
- around 20C
- mostly sunny / partly cloudy
- about 5% rain chance
- light winds, potentially S-SE 15-20 km/h in the afternoon

No material wet-weather suppression is expected.

## Joint score corridor

Lower / competitive:
- Adelaide 44-32
- Adelaide 48-34
- Adelaide 50-35

Central:
- Adelaide 52-36
- Adelaide 54-37
- Adelaide 55-39

Separation:
- Adelaide 60-34
- Adelaide 62-35
- Adelaide 65-36

Upset / close:
- Adelaide 45-42
- West Coast 46-43

## Final ranking

1. **West Coast +21.5 — LEAN / MEDIUM**
2. **Under 93.5 — LEAN / MEDIUM-LOW**
3. **Adelaide -21.5 — FORCED RANK / MEDIUM-LOW**
4. **Over 93.5 — FORCED RANK / MEDIUM-LOW**

Potential winner: **Adelaide — LEAN / MEDIUM**

All rows: Probability NOT_GENERATED / NOT PUBLISHED; NO VALUE DETERMINABLE.

## Rank 1 — West Coast +21.5

Why:
- Adelaide is 0-2 and transitioning.
- Adelaide's large Round 2 territory edge did not translate into scoreboard efficiency.
- The line asks for 22+ rather than simply an Adelaide win.
- West Coast lost Round 1 by only 12 and has shown late-margin compression.
- Charlie Thomas returns.
- The 2025 meeting ended Adelaide by 17 despite a 43-23 inside-50 edge.
- AFL.com's current match preview tipped Adelaide by 14, consistent with Adelaide winning without necessarily covering 21.5.

Kill path:
- Adelaide dominates stoppage/territory;
- Kelly/Rasheed materially fix the forward phase;
- West Coast repeats its Gold Coast first-half collapse.

## Rank 2 — Under 93.5

Support:
- Adelaide's Round 2 total was 73.
- 2025 H2H total was 79.
- Adelaide is generating territory without reliable conversion.
- West Coast averages only 38 points scored.
- Charlie Thomas strengthens West Coast's defensive organisation.
- central scores 52-36 and 54-37 are Under.

Kill path:
- both defences again concede 50+;
- Adelaide's forward returns improve conversion;
- 55-39 already reaches 94.

## Rank 3 — Adelaide -21.5

Support:
- Adelaide can generate a large inside-50 advantage.
- West Coast conceded 69 to Gold Coast.
- Jess Allan plus Marinoff/Goodwin/Newman can create repeated territory.
- Kelly/Rasheed improve Adelaide's forward options.
- home ground and West Coast travel help Adelaide contextually.

Why below +21.5:
- Adelaide has not won yet.
- it scored only 23 last round.
- its forward conversion problem remains unresolved.
- a 10-20 point Adelaide win is a very ordinary branch.

## Rank 4 — Over 93.5

Support:
- West Coast has allowed 54 and 69.
- Adelaide has allowed 61 and 50.
- West Coast game totals are 96 and 103.
- Adelaide's Round 1 total was 114.
- dry conditions do not suppress handling.

Why fourth:
- Adelaide's forward-entry efficiency remains the strongest process weakness.
- West Coast is not currently a high-volume scorer.
- Adelaide can cover through suppression, e.g. 58-30 = 88, so a big margin does not imply Over.

## Potential winner — Adelaide

Adelaide remains the preferred winner because it has the stronger expected territory path, home ground, Jess Allan first-use influence, and midfield quality through Ebony Marinoff, Sarah Goodwin and Maddi Newman.

The strongest upset path is Adelaide repeating shallow entries and risky turnover chains while West Coast's aerial defence and contest group keep the game compressed.

Winner order: Adelaide > West Coast.

Best handicap order: West Coast +21.5 > Adelaide -21.5.

# P-164 (conversation-local continuation) — Chiba Lotte Marines @ Hokkaido Nippon-Ham Fighters — NPB — 2026-08-29

## Decision outcome

**`RANKED FORECAST — NO BET ENDORSED`**

This record follows the active `UPCOMING_GAME_RESEARCH_GUIDE.md` (`UGR-2026.08.25-v1`) and `RULES_BASEBALL.md`.

- **Method:** `MDS-2026.08.29-v2.5 — qualitative champion`
- **Numerical state:** `NTS-2026.08.25-v0.2 — design only; no baseball model is fit`
- **Competition population:** NPB Pacific League — kept separate from MLB/LMB/KBO priors
- **Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value:** `NO VALUE DETERMINABLE`
- **Candidate origin:** `USER_SUPPLIED`
- **Operator / action / extra-inning terms:** `NOT SUPPLIED / UNKNOWN_DEFINITION`
- **Current lineup state:** posted starting orders were not recovered from a field-owning source at the final pregame cutoff, so lineup-specific claims are capped.

---

## 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | NPB Pacific League, 2026 regular season |
| Event | Chiba Lotte Marines @ Hokkaido Nippon-Ham Fighters |
| Venue | ES CON FIELD HOKKAIDO |
| Scheduled start | 14:00 JST |
| Melbourne equivalent | 15:00 AEST |
| Final verified state | `PREGAME` immediately before scheduled start |
| H2H game number | 20th meeting of the season |
| Home team | Nippon-Ham |

### Candidate geometry

1. Lotte +1.5
2. Nippon-Ham +1.5
3. Over 8.5
4. Under 8.5

- Nippon-Ham +1.5 wins on every Fighters win and every one-run Lotte win.
- Lotte +1.5 wins on every Marines win and every one-run Fighters win.
- **Both +1.5 rows win in any one-run final.**
- Over 8.5 wins at 9+.
- Under 8.5 wins at 0-8.

---

## 2. Official starter handshake

### Nippon-Ham — Jiei Okawa, RHP

**Status:** `CONFIRMED_OFFICIAL / announced starter`

Current first-team context:
- 2 appearances
- 0-0
- listed ERA 27.00
- making his **first NPB start**.

The raw 27.00 ERA comes from an extremely small relief sample and is not treated as a stable run-rate estimate.

Farm / current development context:
- 17 farm appearances
- 7 starts
- around 4.18 ERA
- previous farm outing: 6 IP, 5 H, 1 R
- had won his previous two decisions.

### Okawa mixture

**Good/development branch**
- recent farm command transfers;
- 4-5+ useful innings;
- 1-2 runs.

**Ordinary branch**
- short first start;
- traffic but enough strike throwing to reach the middle innings;
- 2-3 runs.

**Early-hook/contact branch**
- first-start nerves / command instability;
- Lotte sees multiple baserunners early;
- bullpen enters before the fifth;
- 3-5+ run exposure.

The baseball small-sample starter rule is fully active.

---

### Lotte — Andre Jackson, RHP

**Status:** `CONFIRMED_OFFICIAL / announced starter`

Official 2026 NPB:
- 21 starts
- 9-7
- **3.12 ERA**
- 130 IP
- 100 H
- 12 HR
- 49 BB
- **118 K**
- 45 ER.

Current regime:
- **five consecutive quality starts**
- August ERA around **2.10**.

Previous start against Nippon-Ham, Aug. 23:
- 6 IP
- 3 H
- 3 BB
- 5 K
- 2 R
- no hits allowed through the first five innings.

Jackson therefore has the clear starter-phase advantage.

Strongest adverse branch:
- Fighters see him for the seventh time this season;
- repeated exposure improves pitch recognition;
- Reyes / Kiyomiya / current power bats generate HR or extra-base clustering;
- his 49 BB season total creates baserunner/HR sequencing risk.

---

## 3. Team baseline

### Nippon-Ham

Current official Pacific League team offense:
- .251 AVG
- .314 OBP
- .414 SLG
- 487 runs through 118 games
- **144 HR**.

Current team pitching:
- **3.29 ERA**.

Current standings after Aug. 28:
- **65-53-1**
- 3rd in Pacific League.

### Lotte

Current official team offense:
- .236 AVG
- .297 OBP
- .356 SLG
- 387 runs through 111 games at the last official team-stat snapshot
- 96 HR.

Current team pitching:
- **3.80 ERA**.

Current standings after Aug. 28:
- **52-58-3**
- 5th.

The broad full-season team-strength prior favors Nippon-Ham.

---

## 4. Direct 2026 matchup

Official Pacific League preview entering Game 20:

| Metric | Nippon-Ham | Lotte |
|---|---:|---:|
| H2H record | **11-8** | 8-11 |
| H2H ERA | **2.82** | 4.58 |
| H2H AVG | **.239** | .207 |
| H2H runs | **88** | 62 |
| H2H HR | **34** | 18 |

Combined H2H runs:
- 150 across 19 games
- descriptive average ≈ **7.9 runs/game**.

That does not mechanically predict Under 8.5, but it is consistent with a central total below nine.

Recent direct games:
- Aug. 28: Nippon-Ham 6-4 Lotte — 10 runs
- Aug. 23: Lotte 3-2 Nippon-Ham — 5
- Aug. 21: Lotte 4-3 Nippon-Ham — 7
- Aug. 2: Nippon-Ham 3-0 Lotte — 3.

The direct matchup contains both a suppression centre and a genuine HR/cluster upper tail.

---

## 5. Bullpen / late-game state

### Aug. 28 usage

Lotte:
- Ojima 5 IP
- Shuta Ishikawa 3 IP.

Most of the normal high-leverage relief group did not have to cover the preceding eight innings.

Recent roster/relief context includes:
- Yokoyama
- Ono
- Suzuki
- Masuda
- Sawada
- Nakamori
depending role/availability.

Nippon-Ham:
- Kitayama 6.2 IP
- Shimamoto 0.1
- Hori 1
- Yanagawa 1.

The Fighters used Hori and closer Yanagawa, but only for one inning each.

Earlier August evidence also identified an unstable eighth-inning phase for Nippon-Ham, so a close late Lotte game retains a comeback branch rather than treating the Fighters bullpen as automatic shutdown.

Bullpen freshness is not equated with bullpen quality.

---

## 6. Current run-production mechanism

### Nippon-Ham offense vs Jackson

Broad advantages:
- materially stronger season power;
- 144 HR versus Lotte's 96;
- stronger H2H contact/power against this opponent;
- home last bat.

But Jackson directly suppresses the central branch:
- five straight QS;
- 2.10 August ERA;
- 6 IP/2 R against the Fighters six days ago.

Thus the central Fighters offense is approximately a 3-5 run branch rather than an assumed 6+.

### Lotte offense vs Okawa

Lotte's season offense is weaker:
- .236/.297/.356;
- only .207 in the H2H with Nippon-Ham.

But Okawa is the largest volatility input in the game:
- first career start;
- tiny first-team sample;
- farm ERA 4.18.

That gives Lotte both:
- a low-output branch if Okawa's recent farm form transfers;
- a substantial 4-6 run branch if his command/first-start exposure fails.

---

## 7. Venue / conditions

ES CON FIELD HOKKAIDO is the home venue.

The NPB schedule listed generally fair/partly cloudy conditions around the event. Roof/open-roof status was not recovered at the final cutoff.

No weather direction is therefore applied.

---

## 8. Market sanity only

A contemporaneous public snapshot showed approximately:
- Nippon-Ham moneyline favored
- standard Nippon-Ham run line around **-1.5**
- Lotte standard run line around **+1.5**
- total **8.5**
- Under slightly preferred to Over in one current snapshot.

This matters only as external contract sanity.

The user's **Nippon-Ham +1.5** is therefore a materially more protected alternate than the current standard -1.5 Fighters line.

No implied probability, de-vig, EV or staking conclusion is derived from these prices.

---

## 9. D0 mechanism retrieval

Predeclared query:

`NPB pregame -> opponent positive +1.5 alternate lines -> strong home team/full-season edge -> home rookie first career start -> established road starter in strong current regime -> total 8.5`

**Result: `NO COMPARABLE CASE` retained.**

No prior MLB/KBO/NPB outcome is used as a vote.

---

## 10. Joint run corridor

### Lower / starter-control
- Nippon-Ham 3-2
- Lotte 3-2
- Nippon-Ham 4-2
- Lotte 4-2

Supports:
- both +1.5 in one-run finals
- Under 8.5.

### Central
- **Nippon-Ham 4-3**
- **Nippon-Ham 5-3**
- **Lotte 4-3**

Interpretation:
- NH +1.5 wins in all three
- Lotte +1.5 wins in both one-run games
- all three are Under 8.5.

### Upper / Okawa early-hook or HR cluster
- Nippon-Ham 5-4
- Lotte 5-4
- Nippon-Ham 6-3
- Lotte 6-3
- 6-4 either way.

The 5-4 state is especially important:
- both +1.5 rows can win
- Over wins.

---

## 11. Final ranking

| Rank | Pick | Verdict | Evidence | Role |
|---:|---|---|---|---|
| **1** | **Nippon-Ham Fighters +1.5** | `LEAN` | **MEDIUM** | `PRIMARY_FORMAL — MARGIN` |
| **2** | **Lotte Marines +1.5** | `LEAN` | **MEDIUM** | `CORRELATED_SECONDARY — MARGIN` |
| **3** | **Under 8.5 Runs** | `LEAN` | **MEDIUM-LOW** | `PRIMARY_FORMAL — TOTAL` |
| **4** | **Over 8.5 Runs** | `FORCED RANK` | **MEDIUM-LOW** | `CORRELATED_SECONDARY — TOTAL` |

All:
- `Probability: NOT_GENERATED / NOT PUBLISHED`
- `Actionability: NO VALUE DETERMINABLE`.

---

## 12. Rank #1 — Nippon-Ham +1.5

Why first:
1. user-supplied +1.5 is a very large cushion relative to the current standard market;
2. Nippon-Ham is the stronger full-season team;
3. stronger offense and power;
4. better team pitching baseline;
5. 11-8 H2H lead;
6. huge H2H run/HR edge;
7. home last bat.

Strongest kill:
Jackson dominates while Okawa's early-hook branch appears.

Representative:
- Lotte 5-2
- Lotte 5-3
- Lotte 6-3.

A Lotte win by two or more is the only way to defeat Fighters +1.5.

---

## 13. Rank #2 — Lotte +1.5

Why close behind:
1. Jackson has the clear starter advantage;
2. five straight QS;
3. excellent August ERA;
4. just held Fighters to two runs in six innings;
5. most normal Lotte relievers were not heavily used yesterday;
6. any one-run Fighters win still cashes +1.5.

Strongest kill:
Nippon-Ham's much stronger power lineup solves Jackson on repeated exposure and Okawa provides 4-5 viable innings.

Representative:
- Fighters 5-2
- Fighters 6-3
- Fighters 6-2.

---

## 14. Rank #3 — Under 8.5

Support:
- Jackson's strong current form;
- Lotte's weaker season offense;
- Lotte only .207 vs Fighters in the H2H;
- direct H2H combined runs average about 7.9;
- three of the four recent direct examples listed above finished at 7 or fewer;
- central 4-3 / 5-3 type states remain Under.

Strongest kill:
Okawa struggles early and creates a long bullpen game; Fighters still score 3-5 against Jackson/Lotte relief.

Representative:
- 5-4
- 6-3
- 6-4.

Yesterday's 6-4 final is direct evidence of that upper tail.

---

## 15. Rank #4 — Over 8.5

Support:
- Okawa is making his first career start;
- tiny first-team sample and 4.18 farm ERA;
- Nippon-Ham has serious power;
- Reyes hit two HR yesterday;
- first-start early hook can raise bullpen innings and variance.

Why fourth:
- Jackson sharply reduces the most obvious Fighters scoring branch;
- Lotte is a weaker offense;
- the 8.5 threshold requires nine;
- the H2H centre is below nine.

---

## 16. Potential winner

### **Hokkaido Nippon-Ham Fighters — LEAN / MEDIUM-LOW**

Central winner mechanism:
- stronger overall club;
- stronger offense;
- stronger team pitching baseline after the rookie exits;
- substantial season H2H superiority;
- home last bat.

Strongest failure path:
- Jackson repeats his Aug. 23 control;
- Okawa fails in his first start;
- Lotte scores first and hands a lead to a relatively fresh relief group.

The starter matchup strongly favors Lotte, which keeps the winner call below the confidence of Fighters +1.5.

---

## 17. Scenario map

| Score | Lotte +1.5 | NH +1.5 | O8.5 | U8.5 |
|---|:---:|:---:|:---:|:---:|
| NH 4-3 | WIN | WIN | LOSS | WIN |
| LOT 4-3 | WIN | WIN | LOSS | WIN |
| NH 5-3 | LOSS | WIN | LOSS | WIN |
| LOT 5-3 | WIN | LOSS | LOSS | WIN |
| NH 5-4 | WIN | WIN | WIN | LOSS |
| LOT 5-4 | WIN | WIN | WIN | LOSS |
| NH 6-3 | LOSS | WIN | WIN | LOSS |
| LOT 6-3 | WIN | LOSS | WIN | LOSS |

---

## 18. Final volatile refresh

Immediately before issue:
- official Pacific League search still showed the game as **`試合開始前 / pregame`**;
- NPB official starter page retained Okawa vs Jackson;
- no field-owner current starting-order page was recovered;
- no scored state was used.

**Frozen issued state: `PREGAME`.**

If first pitch occurs after this cutoff, this remains the immutable pregame view.

---

## 19. Final summary

1. **Nippon-Ham +1.5 — LEAN / MEDIUM**
2. **Lotte +1.5 — LEAN / MEDIUM**
3. **Under 8.5 — LEAN / MEDIUM-LOW**
4. **Over 8.5 — FORCED RANK / MEDIUM-LOW**

**Potential winner:** **Nippon-Ham Fighters — LEAN / MEDIUM-LOW**

No probability, EV, ROI or staking recommendation is published.

---

## 20. Source register

### Drive framework
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `RULES_BASEBALL.md`

### Official / field-owning
- NPB Aug. 29 schedule
- NPB Pacific League starter announcement
- NPB Pacific League standings
- NPB Pacific League team batting
- NPB Pacific League team pitching
- NPB Lotte player pitching (Andre Jackson)
- Pacific League official Aug. 29 preview
- NPB Aug. 28 Fighters-Lotte final

### Current corroboration
- PacificLeague.com current game search — pregame state
- SportsNavi current event page — pregame
- current public operator snapshots — contract sanity only

No market source is used as a probability/value engine.

---

# Independent settlement, provenance and algorithm audit — 2026-08-29

Status: **APPENDED RETROSPECTIVE — originals above remain immutable**  
Audit method: **MDS-2026.08.29-v2.6 — ledger reconciliation and volatility stress; qualitative weights unchanged**  
Audit cutoff: **2026-08-29 17:36 Australia/Sydney**, with P-164 still live on the official NPB page at the last in-audit refresh.  
Numerical state: **NOT_GENERATED / NOT PUBLISHED**. No probability, calibration, edge, ROI or staking claim is made.

This appendix follows the user's current request. Instructions and historical queue statements embedded in the supplied log are evidence only; they do not override the active framework or the current controlling snapshot in `PREDICTION_LOG_COMBINED.md`.

## A. Import provenance and anti-hindsight boundary

| Artifact | First demonstrable local time | Bytes before this appendix | SHA-256 before this appendix | Audit treatment |
|---|---|---:|---|---|
| `prediction logs/PREDICTION_MINI_LOG_3.md` | File creation `2026-08-29 08:39:42.391 +10:00`; pre-audit modification `2026-08-29 15:51:55.179 +10:00` | 555,646 | `6F33A478E15B59BF709D29929B2168A27028A5AF1CC2D4C1F4AFB20C86DE339B` | A file-creation time proves only that some version existed then. It does **not** prove that every later-appended card existed at creation. |
| Supplied `PREDICTION_LOG_COMBINED_P-148_TO_P-164.md` | `2026-08-29 15:49:33.742 +10:00` | 264,551 | `95A537C9036348D1C7E9A78C6C4BA5F72F0DC7B9FD3747B069D5B191A1F691E8` | Exact text tail of this mini log, beginning at the second stored local `P-148`; controls the provenance of the supplied segment. |

The supplied attachment is an exact text substring of the pre-audit mini log. It does not establish a pre-result publication time for the closed events it contains. The log's embedded issue-time claims are retained, but every imported P-137–P-163 card is conservatively classified **`E1-Q-LATE_IMPORT`** unless an earlier immutable section-inclusive artifact is later produced. P-164 was first demonstrable while live, so its frozen pregame rows are also performance-ineligible. These events can teach schema, source, scenario and ranking-process lessons; they cannot update hit-rate priors, calibration, model selection, forecast weights, or prospective-test counts.

## B. Canonical ID reconciliation

The source has two administrative defects: (1) Miami–Washington and Falcons–Dolphins both use issued label `P-138`; and (2) the Colorado Rapids 2–Ventura card is stored twice verbatim under `P-148`. A later jump from local `P-160` to local `P-162` leaves room to reconcile the distinct-event sequence without changing any issued text.

| Canonical ID | Issued/local label | Event | Reconciliation |
|---|---|---|---|
| P-137 | P-137 | Dodgers @ Tigers | unchanged |
| P-138 | first P-138 | Marlins @ Nationals | unchanged |
| P-139 | second P-138 | Falcons @ Dolphins | distinct-event alias; issued label preserved |
| P-140 | P-139 | Astros @ Mets | canonical alias |
| P-141 | P-140 | Red Sox @ Yankees | canonical alias |
| P-142 | P-141 | Rockies @ Braves | canonical alias |
| P-143 | P-142 | Giants @ Jets | canonical alias |
| P-144 | P-143 | Buccaneers @ Jaguars | canonical alias |
| P-145 | P-144 | Rangers @ Brewers | canonical alias |
| P-146 | P-145 | Sun @ Fever | canonical alias |
| P-147 | P-146 | Gotham FC v Portland | canonical alias |
| P-148 | P-147 | Toluca Femenil v León Femenil | canonical alias |
| P-149 | P-148 | Colorado Rapids 2 v Ventura County | one event; second stored block is `DUPLICATE_STORAGE`, not another forecast |
| P-150 | P-149 | Montreal @ Winnipeg | canonical alias |
| P-151 | P-150 | Boca Juniors v Lanús | canonical alias |
| P-152 | P-151 | Atlante v León | canonical alias |
| P-153 | P-152 | Necaxa v Cruz Azul | canonical alias |
| P-154 | P-153 | Vikings @ Broncos | canonical alias |
| P-155 | P-154 | Phillies @ Angels | canonical alias |
| P-156 | P-155 | Orioles @ Athletics | canonical alias |
| P-157 | P-156 | Sacramento @ Reno | canonical alias; issued as no actionable live forecast |
| P-158 | P-157 | Toronto Tempo @ Las Vegas Aces | canonical alias |
| P-159 | P-158 | Mystics @ Sparks | canonical alias |
| P-160 | P-159 | Diamondbacks @ Giants | canonical alias |
| P-161 | P-160 | Sultanes @ Toros | fills the unused canonical number |
| P-162 | P-162 | Rigele Te v Chase Ferguson | unchanged |
| P-163 | P-163 | Adelaide v West Coast | unchanged |
| P-164 | P-164 | Lotte @ Nippon-Ham | unchanged; live at audit cutoff |

The next canonical ID is therefore **P-165**. Issued/local labels remain searchable aliases forever. Duplicate storage is excluded from event, contract, rank and winner counts.

## C. Settlement ledger

`Official` means the competition, league, club or field-owning match page supplied the final. `Provisional` means the result or niche field is supported by specialist/secondary evidence pending an official-provider confirmation. Rows with unknown operator definitions are research settlements only.

| Canonical ID | Verified result / state | Ranked contract outcomes in issued rank order | Winner call | Settlement/source status |
|---|---|---|---|---|
| P-137 | Dodgers 2–1 Tigers | **W, W, W, L** | Dodgers **W** | Official MLB recap/game story |
| P-138 | Nationals 9–2 Marlins | **L, L, W, W** | Marlins **L** | Official MLB recap |
| P-139 | Falcons 17–12 Dolphins; total 29 | **W, L, L, W** | Falcons **W** | Official NFL/team report |
| P-140 | Astros 3–1 Mets | **W, L, L, W** | Astros **W** | Official MLB game story |
| P-141 | Yankees 1–0 Red Sox | **W, W, W, L** | Yankees **W** | Official MLB recap |
| P-142 | Braves 6–4 Rockies | **W, W, L, W** | Braves **W** | Official MLB recap |
| P-143 | Giants 23–6 Jets; total 29 | **W, L, W, L** | Giants **W** | Official Giants report |
| P-144 | Jaguars 19–0 Buccaneers; total 19 | **L, L, W, W** | Buccaneers **L** | Official team report |
| P-145 | Brewers 6–1 Rangers | **L, L, W, W** | Brewers **W** | Official MLB recap |
| P-146 | Fever 111–91 Sun; total 202 | **W, W, L, L** | Fever **W** | Official WNBA/team result |
| P-147 | Gotham 1–1 Portland; HT 0–0; corners 4–3 | **L, L, L, W, W** | Gotham regulation winner **L** | Official Gotham recap and official stats summary |
| P-148 | Toluca Femenil 1–0 León Femenil; HT 0–0 | **L, UNRESOLVED, L, W, W** | Toluca **W** | Score/goal timing corroborated by current reports; Toluca corner count not recovered |
| P-149 | Colorado Rapids 2 2–3 Ventura; HT 1–1 | **W, W, W, L, L** | Ventura **W** | Official score/phase; Ventura corners research result **provisional** |
| P-150 | Winnipeg 44–28 Montreal; total 72 | **L, L, W, W** | Montreal **L** | Official CFL report |
| P-151 | Boca Juniors 1–0 Lanús; HT 0–0 | **W, W, W, L, L** | Boca **W** | Official score/phase; Boca corners research result **provisional** |
| P-152 | Atlante 1–1 León; HT 0–0; corners 3–3 | **L, L, L, W, W** | León **L** | Current result/stat corroboration; corner field provisional |
| P-153 | Necaxa 1–3 Cruz Azul; HT 0–1; corners 7–7 | **W, W, W, L, L** | Cruz Azul **W** | Current result/stat corroboration |
| P-154 | Broncos 34–6 Vikings; total 40 | **L, W, L, W** | Broncos **W** | Official Vikings report |
| P-155 | Phillies 5–3 Angels; total 8 | **W, L, W, L** | Phillies **W** | Official MLB recap |
| P-156 | Orioles 4–3 Athletics; total 7 | **W, W, L, L** | Orioles **W** | Official MLB report/story |
| P-157 | Reno 6–1 Sacramento | `NO ACTIONABLE LIVE FORECAST`; frozen descriptive order would read **W, W, L, L** | none actionable | Official MiLB scoreboard; excluded from forecast performance |
| P-158 | Aces 93–73 Tempo; total 166 | **W, L, W, L** | Aces **W** | Official WNBA game page; specialist box cross-check |
| P-159 | Sparks 88–82 Mystics; total 170 | **L, W, L, W** | Mystics **L** | Official WNBA game page/current report |
| P-160 | Diamondbacks 10–6 Giants; total 16 | **W, L, L, W** | Diamondbacks **W** | Official MLB recap |
| P-161 | Toros 2–0 Sultanes; total 2 | **L, W, L, W** | Toros **W** | Official Sultanes report |
| P-162 | Rigele Te d. Chase Ferguson 6–1, 6–4; 17 games | **W, W, L, L** | Te **W** | Specialist scoreboard only; all rows provisional pending official ITF/event confirmation |
| P-163 | Adelaide 60–43 West Coast; margin 17, total 103 | **W, L, L, W** | Adelaide **W** | Official AFLW report |
| P-164 | Nippon-Ham 9–7 Lotte, **live top 6th** at last refresh | rank 3 Under 8.5 **mathematically lost**; rank 4 Over 8.5 **mathematically won**; both +1.5 sides and winner remain **OPEN** | Nippon-Ham **OPEN** | Official NPB live page; whole event stays open until official final |

### Descriptive accounting only

Across the 27 canonical P-137–P-163 events:

- 26 carried actionable pregame rankings; P-157 explicitly issued no actionable live forecast.
- Excluding P-157, there are 110 closed research-contract rows: **58 WIN / 51 LOSS / 1 UNRESOLVED**.
- Rank slots are: rank 1 **16–10**; rank 2 **12–13–1 unresolved**; rank 3 **12–14**; rank 4 **15–11**; rank 5 **3–3**.
- Potential-winner calls are **20–6**.
- P-164 currently adds one mathematically decided win and one loss, but it remains an open event and is not included above.

These are correlated, user-selected, late-import directional rows without issued probabilities or prices. They are **not** independent trials, calibration evidence, a betting record, profit/ROI evidence, or proof that any rank slot has stable skill. The unexpectedly strong rank-4 count is a useful ordinal-process warning, not a reason to reverse ranks retrospectively.

## D. Event-level retrospective

### P-137 — Dodgers @ Tigers

What went right: the top Tigers +2.5 cushion, Dodgers winner, and Under 7.5 all came from a coherent close, low-scoring branch. The official 2–1 final—with the winning run in the eighth—matched the intended distinction between outright winner and broad underdog cushion.

What to retain: model winner, run line and total from one joint run distribution. A strong favourite can win without clearing a large margin. Do not convert this one success into a new weight.

### P-138 — Marlins @ Nationals

What failed: Marlins ML and Under 8.5 ranked first and second; Washington won 9–2. The official recap records home runs by Brady House and Harry Ford behind Jackson Kent's first career win. The card let Eury Pérez/Miami starter quality and Kent's poor surface line suppress the Washington power/cluster and young-starter-good-tail branches too aggressively.

Correction: an inexperienced or weakly rated starter must retain a good/ordinary branch, while the opposing offence must retain a multi-homer/cluster branch even when the favourite starter is strong. This is a **DEPENDENCE_TAIL / RATE_PROCESS** ranking defect, not proof that every similar matchup should be an Over.

### P-139 — Falcons @ Dolphins preseason

What went right: Under 36.5 and Falcons winner; the 17–12 final was low scoring. What failed: Falcons -5.5 lost by half a point while Dolphins +5.5 won. The card needed a more explicit mass at the preseason narrow-margin/key-boundary region.

Correction: preseason unit rotations widen score variance but also concentrate margin probability around one-score outcomes. Exact integer/half-point geometry must be shown before ranking the favourite spread over the underdog cushion.

### P-140 — Astros @ Mets

What went right: Astros +1.5, Astros winner and Under 7.5. Hunter Brown struck out 10 over 6⅔ innings and Christian Scott carried a one-hit shutout into the sixth before three walks and a relief transition produced Houston's three-run inning.

Learning: starter quality and low total were directionally coherent, but the realised scoring came through hook/relief-chain sequencing. Preserve the exit-point and inherited-runner branch even in successful Unders.

### P-141 — Red Sox @ Yankees

What went right: Boston +1.5, Yankees winner and Under 7.0 all won in a 1–0 game. Cam Schlittler's 5⅔ scoreless innings and eight strikeouts supported the starter-control branch.

Learning: this is another useful example of winner/cushion coexistence. It does not validate a deterministic Under weight; it validates interval mapping from a shared score object.

### P-142 — Rockies @ Braves

What went right: Braves winner, Rockies +2.5 and Over 9.0 all won in a 6–4 final. What failed: Under 9.0. The correct lesson is structural: a favourite win and underdog alternate cushion can coexist in a moderately high total.

Correction: keep the margin and total dimensions coupled through the score grid rather than treating the underdog cushion as an Under proxy.

### P-143 — Giants @ Jets preseason

What went right: Under 37 and Giants side/winner. What failed: Jets +6 and Over 33.5; the 23–6 result stayed low but separated strongly.

Correction: low total and close spread are not synonyms. Preseason defensive/backup mismatch branches can produce a one-sided Under. The margin tree needs explicit shutout/low-underdog-score mass.

### P-144 — Buccaneers @ Jaguars preseason

What failed: Buccaneers -2.5, Over 35.5 and Buccaneers winner; Jacksonville won 19–0. What went right: Jaguars +2.5 and Under.

Correction: the card ranked a side without enough certainty about who would play and for how long. Preseason sides require quarter-by-quarter quarterback, offensive-line, skill-unit and defensive-rotation mixtures. Missing rep plans should cap the side and make the ordinary opponent-control/shutout branch explicit.

### P-145 — Rangers @ Brewers

What failed: Rangers +1.5 and Over 7.5; Milwaukee won 6–1. What went right: Brewers -1.5, Under and winner.

Learning: low total can coexist with a multi-run margin. The rank order placed the broad underdog cushion above the identified starter/team-quality separation branch and did not reconcile those positions.

### P-146 — Sun @ Fever

What went right: Fever -17.5, Over 177.5 and winner in a 111–91 final. The first two ranks correctly represented a large quality/depth gap and scoring environment.

What to retain: model opening separation, maximum lead, bench phase and closing margin separately in extreme spreads. This result is one descriptive success, not a fitted coefficient.

### P-147 — Gotham v Portland

What failed: first-half Over 0.5, Gotham team corners Over 4.5, full-match Over 2.5 and Gotham regulation winner. The official recap describes a cagey 0–0 first half, a 60th-minute 0.01-xG cross/shot goal and a 75th-minute penalty; official corners were Gotham 4, Portland 3. Full-match Under and first-half Under won.

Correction: late-import outcome notwithstanding, the original ranking leaned on attacking class and broad scoring/corner history more than the target-event mechanisms. First-half goal and team-corner rows require their own exposure, chance-quality, width/block/clearance and lineup paths. A dominant-possession home side can stop at four corners, and two unusual second-half scoring events do not retroactively imply a sound Over process.

### P-148 — Toluca Femenil v León Femenil

What failed: first-half Over 0.5 and full-match Over 2.5. Reports describe a rain-affected, congested first half and a 76th-minute penalty for the only goal. Full-match and first-half Unders won; Toluca winner won. Toluca's exact corner count remains unresolved and is not guessed.

Correction: rain, unresolved starting XIs, the opponent's current away scoring, and Toluca's defensive/home control needed an explicit low-event branch. A recent high-scoring run must be decomposed into persistent creation and current participants; it cannot automatically outrank the Under branch.

### P-149 — Colorado Rapids 2 v Ventura County

What went right: first-half Over 0.5, full-match Over 2.5 and Ventura winner in a 3–2 final. The Ventura corner Over is provisionally a research win but remains provider-sensitive.

Learning: reserve-soccer open-play and transition variance were represented. Keep the exact competition/lineup/substitution regime separate from senior soccer, and never promote a corner source until independence and provider definition are known.

### P-150 — Montreal @ Winnipeg, CFL

What failed: Montreal -6.5, Under 60.5 and Montreal winner; Winnipeg won 44–28. The card explicitly identified Brady Oliveira/Winnipeg ball control as a close-game mechanism but did not give it enough ordinal force. Winnipeg then dominated possession; Zach Collaros completed 26 of 32 for 324 yards and two touchdowns, and Ontaria Wilson had nine catches for 114 yards and two touchdowns.

Correction: CFL side/total modelling needs a possession-to-points chain: expected rushing workload, second-down conversion, protection/explosives, red-zone touchdown rate and opponent pass-defence redirection. A supported underdog-possession branch can defeat both favourite and Under simultaneously and must be reconciled before rank issue.

### P-151 — Boca Juniors v Lanús

What went right: full-match Under, first-half Under, Boca winner and provisionally Boca corners Over 4.5. The only goal came at 90+3 after a 0–0 first half.

What failed: first-half and full-match Overs. The ranking still placed first-half Over above the Under despite a plausible slow-control state. The settlement reinforces phase separation: late pressure/corners do not imply an early goal.

### P-152 — Atlante v León

What failed: first-half Over, 9+ corners, full-match Over and León winner; the game finished 1–1, HT 0–0, corners 3–3. The source card itself showed Atlante with three 0–0 first halves in five, two controlled home matches, León on short rest after Colorado, rain and no official XI, yet ranked first-half Over first and Under fifth because of León's early-goal run and seven-match winning streak.

This is a clear **ranking-reconciliation defect**. The evidence was present before issue. Recent early goals and a win streak were outcome summaries; they did not establish that the same creation/finishing mechanism would persist under rest, weather, venue and lineup uncertainty. The new soccer control requires explicit evidence-direction reconciliation before an early-goal row can outrank its complement.

### P-153 — Necaxa v Cruz Azul

What went right: full-match Over, first-half Over, 9+ corners and Cruz Azul winner in a 3–1 match with 14 corners. The main scoring and territory mechanisms were directionally coherent.

Learning: retain the separate goal and corner processes that converged here. Do not use this one aligned outcome to merge their labels or raise a numerical weight.

### P-154 — Vikings @ Broncos preseason

What failed: Under 37.5 ranked first; Denver won 34–6, total 40. Denver -3.5, Over and winner won. The official Vikings report says Minnesota rested starters; Carson Wentz played two series; Sam Ehlinger went 15-of-20 for 233 yards and three touchdowns; Denver gained 412 yards, converted 7 of 14 third downs and 2 of 3 fourth downs, and scored on both an 88-yard coverage bust and a 17-play drive.

Correction: the card over-weighted a tiny reserve-quarterback sample and under-weighted unit-mixture tails. Preseason totals must model each expected quarterback/offensive/defensive unit by quarter, shrink tiny samples, and retain explosive coverage-bust, return/non-offensive score, and long-drive conversion branches.

### P-155 — Phillies @ Angels

What went right: Phillies +1.5, Over 7.5 and Phillies winner in a 5–3 final. A grand slam supplied the cluster tail.

Learning: a broad favourite/underdog cushion and total must remain linked through sequencing and HR clusters. No new weight follows from one grand-slam realisation.

### P-156 — Orioles @ Athletics

What went right: Athletics +1.5, Under 9.5 and Orioles winner in a 4–3 final. What failed: Orioles -1.5 and Over.

Learning: this is a clean winner/cushion coexistence case. The correct administrative reading is Orioles by exactly one—not a contradiction—and the run-line intervals should be made visible on every baseball card.

### P-157 — Sacramento @ Reno

What went right in process: the log refused to issue an actionable live forecast because the live state could not be verified. The official final was Reno 6–1, but that outcome must not retroactively turn the descriptive ordering into a forecast.

Learning: `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST` is a successful safety control regardless of the final.

### P-158 — Tempo @ Aces

What went right: Under 174.5, Aces -14.5 and winner in a 93–73 final. What failed: Toronto +14.5, ranked second.

Correction: the underdog cushion underweighted Toronto's depleted roster and Las Vegas' freshness/depth. In extreme spreads, a low total can still coexist with a favourite blowout; model the favourite's defensive suppression and underdog scoring floor separately from total pace.

### P-159 — Mystics @ Sparks

What failed: Washington -4.5 and winner; Los Angeles won 88–82 after erasing a 17-point deficit. The card had already named the exact adverse path—Washington's back-to-back legs failing late, Los Angeles' frontcourt controlling and the Sparks becoming more efficient—but ranked it last. The total Over and Los Angeles +4.5 won.

This is another **ranking-reconciliation defect**. A named, current, supported adverse branch cannot remain decorative. Basketball rest must be segmented into second-half transition defence, turnover/rebound control, shot quality, foul/bonus exposure and closing-lineup probability before the side is ranked.

### P-160 — Diamondbacks @ Giants

What failed: Giants +1.5 and Under 8 ranked above the Over; Arizona won 10–6. Both starters carried small-sample/instability tails, and both bullpen contexts allowed runs, yet park and split arguments pulled the centre too low.

Correction: when both starter exit distributions and bullpen quality widen upward, a joint early-hook/cluster/HR branch must be explicitly compared with the park/split Under branch. The model may still rank Under, but only after showing why that joint tail is subordinate.

### P-161 — Sultanes @ Toros

What failed: Sultanes +1.5 ranked first and the Sultanes winner; Tijuana won 2–0. Under and Tijuana -1.5 won. The source card named the exact failure path—Teddy Stankiewicz/Medina controls, Manny Bañuelos regresses, and the bullpen protects a multi-run lead—but did not reconcile it with rank one.

Correction: low total does not guarantee a broad underdog run-line cover. One-sided shutout/2–0/3–0 branches must be retained and jointly queried for side and total.

### P-162 — Te v Ferguson

What went right descriptively: Te -2.5, Under 22.5 and Te winner in a 6–1, 6–4 final. The match result is currently specialist-only.

Learning: no tennis algorithm weight changes from one provisional ITF-level result. Preserve surface/level/opponent adjustment, set-count mixture and official-result fallback; keep the entire settlement provisional until an official event/tour source confirms it.

### P-163 — Adelaide v West Coast AFLW

What went right: West Coast +21.5 and Adelaide winner; the final margin was 17. What failed: Under 93.5 and Adelaide -21.5; total was 103. The pregame card named West Coast's improved conversion/returning personnel as the Over kill path, and it occurred.

Correction: availability must pass through the full AFLW chain—role/CBA/inside-50/shot location/scoring-shot volume and goal/behind conversion. When returning forwards or midfield creators can move conversion, run a sensitivity around the supplied total rather than retaining recent raw scoring as a fixed baseline.

### P-164 — Lotte @ Nippon-Ham, live

At the 17:36 audit refresh the official NPB page showed Nippon-Ham 9–7 in the top of the sixth. The total had already reached 16, so Under 8.5 was mathematically lost and Over 8.5 won. The +1.5 sides and winner were still open.

The named upper-tail mechanism occurred early: rookie Okawa allowed four runs and exited; Jackson also exited before Nippon-Ham's rally was complete; both teams produced home-run/relief-transition damage. This is strong process evidence that a first-career-start mixture cannot be centred away merely because the opposing starter is stronger. It is **not** a final settlement. The whole event remains open until the official final terminates every contract.

## E. Cross-sport lessons applied prospectively

1. **Canonical ledger integrity.** Every new event gets one canonical ID; distinct events cannot share it; a byte-equivalent storage duplicate never creates another event. Issued labels are preserved through an alias table, not rewritten.
2. **Section-level provenance.** File creation time proves only the artifact version that existed then. Each appended card needs a section-inclusive immutable receipt/hash or revision timestamp. Otherwise use the first demonstrable artifact containing that card and quarantine late imports.
3. **Adverse-branch reconciliation.** If a card names a current, supported branch that defeats a high rank, it must explain why that branch is subordinate. If it cannot, lower evidence and revise the ordinal position before issue.
4. **Side/total coherence.** Low total does not imply a close game; a high total does not imply the favourite covers. Query all contracts from the same score/margin distribution and show shutout, narrow-loss and separation branches.
5. **Mixture tails before point centres.** Debuts, reserve-unit rotations, uncertain minutes and returning personnel require explicit exposure mixtures. A strong opponent or favourable venue cannot erase the mixture's ordinary failure tail.
6. **Phase targets stay separate.** First-half goals, second-half fatigue, starter innings, late bullpen exposure and conversion shifts require their own phase/exposure states.
7. **Mathematically decided is not final.** A live row can be labelled mathematically won/lost, but the event remains OPEN until the official final/termination settles every remaining row.
8. **No single-log weight promotion.** These late-import cases propose controls and future-only comparisons. They do not alter coefficients, probabilities or confidence weights.

## F. Sport-rule changes implemented

| Sport | Prospective algorithm update | Evidence cases | Status |
|---|---|---|---|
| Baseball | Mandatory joint early-hook/relief/cluster tail when either starter is debut/small-sample or both exit distributions are unstable; explicitly reconcile that tail before an Under ranks above Over. Preserve one-sided low-total separation branches. | P-138, P-140, P-145, P-155, P-160, P-161, P-164 | Process control + future-only candidate |
| American football | Preseason quarter-by-quarter quarterback/offence/defence unit mixtures; shrink tiny reserve samples; add coverage-bust, long-drive, return/non-offensive-score and conversion tails. CFL adds rushing-possession, second-down and red-zone conversion pathway. | P-139, P-143, P-144, P-150, P-154 | Process control + future-only candidates |
| Basketball | Segment rest/back-to-back effect by half and by transition defence, turnover/rebound, shot quality, foul/bonus and closing lineup; large-spread low-total favourite blowout remains explicit. | P-146, P-158, P-159 | Process control + future-only candidate |
| Soccer | Early-goal ranks must reconcile opponent 0–0-HT base, rest, weather, XI/keeper uncertainty and persistent creation mechanism; streak/market direction cannot override these silently. Corner settlement remains provider-specific. | P-147, P-148, P-151, P-152, P-153 | Process control + future-only candidate |
| AFL/AFLW | Returning personnel is translated through role/territory/shot volume/shot quality/conversion, with total-line sensitivity when conversion uncertainty is material. | P-163 | Process control + future-only candidate |
| Tennis | No weight change; reinforce official-result confirmation and provisional specialist settlement. | P-162 | Existing control retained |

## G. Source audit and new research lanes

These are **field-specific research lanes**, not blanket approval for scraping, retention, numerical training or automation:

- [NPB official game page](https://npb.jp/scores/2026/0829/f-m-20/) — official inning score, live/final state, pitchers and home runs for P-164.
- [MiLB official scoreboard](https://www.milb.com/sacramento/scores/triple-a/pacific-coast) — official result/state with stable game identifier for P-157.
- [CFL official report](https://www.cfl.ca/2026/08/28/bomber-brigade-halts-alouettes-win-streak/) — final and game-driver reporting for P-150.
- [Minnesota Vikings official report](https://www.vikings.com/news/broncos-2026-preseason-game-observations) — preseason participation and drive/explosive detail for P-154.
- [Gotham FC official recap](https://www.gothamfc.com/news/recap-gotham-fc-portland-battle-to-draw-in-muchanticipated-rematch) — final, phase, xG, shots and official corner summary for P-147.
- [Colorado Rapids 2 official recap](https://www.coloradorapids.com/rapids2/news/recap-colorado-rapids-2-fall-in-tight-battle-against-ventura-county-fc) — official score and match narrative for P-149.
- [AFLW official report](https://www.afl.com.au/aflw/news/1596975/adelaide-crows-crank-it-up-to-hand-west-coast-eagles-third-loss-on-the-trot) — official final and quarter path for P-163.
- [Sultanes official report](https://www.sultanes.com.mx/noticias/duelazo-de-pitcheo-en-el-juego-1-y-cae-monterrey-en-tijuana) — official LMB final and pitching narrative for P-161.
- [WNBA official game pages](https://www.wnba.com/schedule) and official team recaps — primary result/box lanes; Her Hoop Stats is a useful specialist box cross-check, not the field owner.
- [MLB official game stories/video recaps](https://www.mlb.com/scores/2026-08-28) — final, lineups and event narrative for the MLB cases.
- [The Away End Sikkim page](https://theawayend.co/sikkim-premier-division-league/) plus current AiScore result — local schedule/result corroboration for P-126 only; field-owner result and corner count remain unresolved.

Livesport, BetPawa/Sportradar-derived pages, TotalCorner, PlayerStats, APWin and similar aggregators can discover or provisionally cross-check niche fields. Apparent agreement may come from one underlying feed. They do not become independent confirmations or field owners merely because multiple front ends display the same number.

## H. Items still requiring settlement follow-up

| Item | Current state | Required next action |
|---|---|---|
| P-126 score/phase rows | Boys Club 0–1 Sikkim Aakraman, HT 0–1 from current secondary result; provisional | Retry Sikkim field owner/local official result. Research grades: Aakraman ML W; 1H O0.5 W; 1H U0.5 L; FT O2.5 L; FT U2.5 W. |
| P-126-C06 corners O7.5 | **UNRESOLVED** | Obtain provider-consistent final corner count; never infer from score. |
| P-148-C02 Toluca team corners O4.5 | **UNRESOLVED** | Retry official/defined provider statistics. |
| P-149-C02 Ventura team corners O3.5 | **PROVISIONAL WIN** | Seek official/provider-owner confirmation; record same-feed risk. |
| P-151-C02 Boca team corners O4.5 | **PROVISIONAL WIN** | Seek official/provider-owner confirmation; record same-feed risk. |
| P-162 all rows | **PROVISIONAL FINAL** | Confirm 6–1, 6–4 through ITF/event owner and check retirement/completion status. |
| P-164 | **LIVE — Nippon-Ham 9–7, top 6th at last audit refresh** | Refresh official NPB page to final, then settle both +1.5 sides, total rows and winner. |

P-135 and P-136 are already settled in the inherited continuation and are removed from the current queue. Historical OPEN text above remains immutable evidence and does not control current work.

## I. Learning-register dispositions

Immediate promoted changes are limited to validity/process controls: canonical aliasing/duplicate handling, section-level provenance, full-event-open treatment for live mathematically decided rows, and mandatory reconciliation of a supported adverse branch. Forecast-direction ideas remain candidates with prospective count zero:

- `C-PL7-SOC-EARLY-RANK-RECON`
- `C-PL7-AF-PRESEASON-UNIT-TAIL`
- `C-PL7-CFL-POSSESSION-CONVERSION`
- `C-PL7-BSK-REST-SEGMENT`
- `C-PL7-BB-HOOK-TAIL`
- `C-PL7-AFLW-CONVERSION-AVAIL`

No retrospective case in this appendix increments a prospective test.

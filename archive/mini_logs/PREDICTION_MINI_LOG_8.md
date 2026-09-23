# PREDICTION MINI RUNNING LOG

**Status:** ACTIVE — LOCAL APPEND-ONLY CONTINUATION  
**Opened:** 2026-09-02 20:11 Australia/Melbourne  
**Canonical predecessor:** `PREDICTION_LOG_COMBINED.md` — current Drive top controlling snapshot  
**Next canonical forecast ID:** `P-249`  
**Google Drive policy:** READ ONLY — no Drive file is to be edited, uploaded, replaced, moved, renamed, or deleted  
**Local logging policy:** after every new sports forecast/query, append the full frozen card to this file and return the updated Markdown file  
**Settlement policy for this continuation:** preserve all pending/incomplete items. **Before researching and issuing each new sports forecast, first state-check the immediately previous issued event and prioritise its settlement and retrospective if it is final.** If that previous event is still live, suspended, postponed, abandoned pending terms, or otherwise not final/settleable, keep it open, explicitly mark it for settlement/retrospective at the next query, and proceed to the current event.  
**Retrospective gate:** AUTOMATIC FOR THE IMMEDIATELY PREVIOUS ISSUED EVENT ON THE NEXT SPORTS QUERY, BUT ONLY AFTER A VERIFIED FINAL. Never retrospect a live/suspended/unsettled event.

---

## Workflow amendment — 2026-09-02

**User-directed priority order for every subsequent sports query:**

`PREVIOUS EVENT STATE CHECK → SETTLEMENT (if final) → RETROSPECTIVE (if final) → CURRENT EVENT RESEARCH → CURRENT FORECAST → APPEND`

- If the previous event is still live/suspended/postponed or cannot yet be authoritatively settled, record that status and carry its settlement/retrospective forward.
- Do not block the current forecast merely because the previous event is still open.
- Once that previous event becomes final, its settlement and retrospective take priority at the start of the next query.
- This amendment changes workflow timing only; it does not alter probability/value publication gates, source hierarchy, market-blindness, or learning-promotion requirements.

---

## 1. Governing framework at opening

| Field | Active state |
|---|---|
| Framework review | 2026-09-02 |
| Published method | `MDS-2026.09.02-v3.1` |
| Forecast mode | `SPORTS_ONLY / MARKET_BLIND` |
| General algorithm | `GFA-2` |
| Operational guide | `UGR-2026.09.02-v1.6` |
| Numerical training | `NTS-2026.09.02-v0.3` — Stage 0 all-sports design / pre-fit / not finalised |
| H0 | NOT BUILT / NOT QUALITY-APPROVED |
| Numerical model | NONE FIT / NONE CALIBRATED / NONE VALIDATED |
| Probability publication | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value publication | `NO VALUE DETERMINABLE` unless a future validated probability model and complete same-time terms/price gate pass |
| Staking / ROI / edge claims | NOT AUTHORISED by the current evidence state |
| Forecast ranking objective | Direct marginal win likelihood and robustness under the exact supplied contract, not diversification and not market value |

### Authority order used by this mini log

1. Current user directive.
2. `AGENT_ROLE_AND_TASK.md`.
3. `RULES_GENERAL.md`, `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`.
4. Applicable current `RULES_<SPORT>.md`.
5. General defaults.
6. Only active/promoted items in `LEARNING_REGISTER.md`.
7. Historical prediction logs, settlements, retrospectives and audits are evidence only; they do not override the current framework.

The **top Current controlling snapshot** of `PREDICTION_LOG_COMBINED.md` alone controls the inherited queue and next canonical ID. Historical queue tables are not controlling.

---

## 2. Canonical predecessor and provenance boundary

The Drive canonical log now incorporates the continuation through `P-248`.

### Current canonical continuation state

- Latest incorporated forecast range: through `P-248`.
- Next distinct-event canonical ID: **`P-249`**.
- `P-215/P-216` and `P-217–P-238` are preserved as late-import descriptive evidence and are not prospective model/ranking-performance evidence.
- The `P-239–P-248` continuation was first demonstrable locally on 2026-09-02. Already-final events in that imported component remain late-import descriptive evidence.
- `P-241`, `P-242` and `P-243` were demonstrably pre-result at import and may enter their appropriate clean qualitative cohort once they are officially settled, subject to the framework's provenance rules.
- New forecasts beginning with **P-249** use **MDS-2026.09.02-v3.1 / GFA-2** unless the Drive authority changes before issuance.

### Immutable-record rule

Issued forecasts are never rewritten after the result. Corrections, live-state changes, settlements, and retrospectives are appended as separate records. Duplicate storage is marked administratively and never counted as a separate event.

---

## 3. Pending / incomplete queue carried into this mini log

### 3.1 Canonical open events — 3

These are part of the canonical queue and remain **TO BE SETTLED**.

| ID | Event | Drive controlling status | Opening web state check | Mini-log action |
|---|---|---|---|---|
| `P-241` | Zachary Svajda vs Daniel Altmaier — 2026 US Open Men's Singles R1 | UPCOMING / NOT STARTED | Current tennis listing still showed UPCOMING | KEEP OPEN — settle only after official final |
| `P-242` | Fabian Marozsan vs Michael Zheng — 2026 US Open Men's Singles R1 | UPCOMING / NOT STARTED | Current reporting says the match was removed from the day's outdoor schedule because of rain; no completed match | KEEP OPEN / POSTPONED-UNPLAYED — re-freeze state if rescheduled |
| `P-243` | Magda Linette vs Francesca Jones — 2026 US Open Women's Singles R1 | SUSPENDED; Jones won first set 6-4 | Current tennis/WTA listings still show SUSPENDED | KEEP OPEN — do not settle until official final |

#### Outstanding issued contracts for the three open events

**P-241**
- `P-241-C01` — Altmaier +2.5 games
- `P-241-C02` — Svajda -2.5 games
- `P-241-C03` — Over 39.5 games
- `P-241-C04` — Under 39.5 games

**P-242**
- `P-242-C01` — Marozsan +2.5 games
- `P-242-C02` — Michael Zheng -2.5 games
- `P-242-C03` — Over 38.5 games
- `P-242-C04` — Under 38.5 games

**P-243**
- `P-243-C01` — Jones +0.5 games
- `P-243-C02` — Linette -0.5 games
- `P-243-C03` — Over 21.5 games
- `P-243-C04` — Under 21.5 games

No result, process grade, lesson, or retrospective is created for these rows in this initialization.

---

### 3.2 Canonical final-event follow-up queue — 10

These are final-event records with unresolved/provisional fields or operator definitions. They remain **TO BE SETTLED / RECONCILED** exactly as carried by the canonical top snapshot.

| Queue item | Current state | Required future reconciliation |
|---|---|---|
| `P-126` | Field-owner result/phase confirmation incomplete; `C06` corners unresolved | Recover controlling result/phase record and settle C06 only from the proper field owner/provider |
| `P-148-C02` | PROVISIONAL LOSS | Confirm with controlling field owner/provider |
| `P-149-C02` | PROVISIONAL WIN | Confirm with controlling field owner/provider |
| `P-151-C02` | STRONG PROVISIONAL WIN | Confirm with controlling field owner/provider |
| `P-166` | OPERATOR OT/ACTION DEFINITION UNKNOWN | Requires the actual operator's settlement/action terms; do not invent them |
| `P-176-C05` | PROVISIONAL WIN | Confirm with controlling field owner/provider |
| `P-178-C05` | UNRESOLVED | No controlling field-owner corner record recovered |
| `P-179-C05` | PROVISIONAL WIN | Specialist result exists; provider-owner confirmation still missing |
| `P-200` | OPERATOR OT/SO/ACTION DEFINITION UNKNOWN | Requires actual operator terms; preserve `UNKNOWN_DEFINITION` otherwise |
| `P-217-C01/C02` | UNRESOLVED | Reduced-overs / DLS / action treatment of unnamed operator remains unknown |

These 10 items are not automatically re-analysed when a new forecast is requested. They remain queued for a user-requested settlement/cleanup pass.

---

### 3.3 Separate provisional-status reconciliation watchlist — not counted inside the canonical 10-item follow-up queue

The canonical snapshot separately states that the following are provisional pending a current CFA/club field-owner final, while omitting them from the stated 10-item queue. This local mini log preserves the inconsistency rather than silently rewriting canonical bookkeeping.

| ID | Current state | Reconciliation need |
|---|---|---|
| `P-233` | FINAL / PROVISIONAL | Recover current CFA/club field-owner final |
| `P-234` | FINAL / PROVISIONAL | Recover current CFA/club field-owner final |
| `P-235` | FINAL / PROVISIONAL | Recover current CFA/club field-owner final |

**Queue accounting:** 3 canonical open events + 10 canonical final-event follow-ups = 13 canonical queue items. The three P-233/P-234/P-235 records are carried separately as a provisional watchlist, giving 16 outstanding record references in this local continuation without falsely changing the canonical queue count.

---

## 4. Active process learnings and controls carried forward

This is a compact operational layer. The full current wording remains in the Drive authority.

### 4.1 Identity, state, contract and target

- Freeze exact official event, competition, participants, venue, rules era, phase and scheduled start before directional research.
- Freeze the sporting `TARGET_ID` separately from bookmaker thresholds.
- Freeze exact settlement geometry: regulation/OT/extra time/shootout/extra innings/DLS/action/void/push/retirement terms as applicable.
- `PREGAME` is valid only when `cutoff_at < scheduled_start_at`.
- If the start is crossed, use a verified live target/state, fail closed as `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, or report a verified final.
- A stale official schedule shell, zero placeholder or malformed official page does not control a field merely because it sits on an official domain.

### 4.2 SPORTS_ONLY / MARKET_BLIND hard gate

- Bookmaker odds, implied probabilities, line movement, consensus pricing, bookmaker previews, affiliate content and tipsters do **not** enter the sports forecast, scenario likelihood, confidence language or ordinal ranking.
- The operator may be used only to freeze the user's contract, threshold and settlement/action definition.
- If operator rules are missing, use `UNKNOWN_DEFINITION`; never select a convenient rule after the result.
- If the user later explicitly asks for price/value work, the sport-only forecast must first be frozen and any price audit remains segregated.

### 4.3 Source ownership and evidence lineage

- Official governing/competition/team sources own official identity, rules, participant releases, state and final.
- Government weather services own forecast/observation fields; the forecast process owns the sport transformation.
- Specialist providers control only their defined metrics.
- Every decisive field must have an atomic exact record/URL, source owner, definition/version, value/unit and timestamp.
- Multiple front ends repeating one upstream feed count as one evidence lineage.
- Conflicting values are preserved; do not majority-vote weak sources over a field owner.
- Late-import forecasts remain quarantined from prospective model/ranking performance.

### 4.4 Mandatory recency / H2H block

For both sides/players and head-to-head where applicable:

- Retrieve L5 / L10 / L15 / L20.
- Store the windows once, not as repeated independent confirmations.
- De-duplicate overlapping events.
- Apply the H2H continuity gate.
- Run the short-vs-long trend test.
- Explain the mechanism behind a trend rather than using a streak as the mechanism.

### 4.5 Descriptive reference-base-rate rule

For every supplied contract:

- Record the exact threshold, relevant historical population and denominator where a defensible descriptive reference rate can be obtained.
- The reference rate is descriptive only.
- Do **not** restore the retired hindsight-derived one-band movement cap or blanket conjunct Rank-1 block.
- Rank directly by current event marginal likelihood and robustness.

### 4.6 Environment / surface gate

For outdoor or open-roof events:

- Classify venue `OUTDOOR`, `INDOOR`, or `RETRACTABLE`.
- Obtain venue-coordinate match-window conditions before discussing totals or margins.
- Record wind speed, gusts, direction, dew point, cloud cover and hourly precipitation where relevant.
- Resolve wind direction against ground/court orientation when the sport requires it.
- Also inspect the actual current surface/field/pitch/strip condition; weather cannot invent an unreported surface state.
- In cricket, seek at least two independent conditions signals from distinct source-ladder rungs where available and always compute the venue-and-format baseline by innings order.

### 4.7 One coherent target object

- Do not create independent narratives for each supplied line.
- Build one sport-native corridor / branch tree for the exact target.
- Carry lower, central, upper and material-tail states.
- Derive all supplied contracts from the same coherent object.
- Preserve nested-line monotonicity, exact complements, overlaps, gaps and push mass.
- For paired-score sports, separate total volume, score allocation and winner/margin.

### 4.8 Component and separation budgets

- Every aggregate total must be decomposed into a component/team/phase budget.
- For plausible floor, centre and ordinary-high states of one component, solve what the other component must contribute to cross the line.
- Every spread/handicap/cushion must be solved as a **separation budget** across the sport's scoring-allocation phases.
- A low total does not imply a close margin.
- A favourite lean does not imply a favourite cover.
- A cushion must survive the ordinary separation branches, not only the winner narrative.

### 4.9 Deficit attribution and venue restraint — L-059

- A participant-quality deficit is attributed to the distribution that participant directly governs.
- A weak or compromised participant raises the opponent's scoring/opportunity branch; it does not mechanically widen both teams in the same direction.
- Venue reputation may scale an exposure budget already supported by the current participants/process.
- Venue reputation may not manufacture the missing scoring required to cross a total.

### 4.10 Rank-1 conditional coherence — L-057

After identifying Rank #1:

1. Define the branch set in which Rank #1 wins.
2. Convert that state into the unit of every other supplied contract.
3. Classify every other row:
   - `COHERENT`
   - `PARTIAL_OVERLAP`
   - `DISJOINT`
4. Re-solve aggregate/component and margin/separation budgets conditional on the Rank-1 state.
5. If a high-ranked row materially contradicts the Rank-1 winning state, repair the order or disclose why the overlap remains sufficient.

This is a coherence repair, not a fitted weight and not evidence of predictive lift.

### 4.11 Separation-budget control — L-058

For every margin/cushion:

- Split scoring/allocation into the sport's relevant phases.
- Hold each side at floor / centre / ordinary-high states by phase.
- Identify where separation is created or compressed.
- Do not allow a broad “close game” narrative or old close H2H record to carry a cushion when the phase arithmetic supports ordinary separation.

### 4.12 Winner / cushion reconciliation — L-060

- Derive the potential winner from the joint object's winner-branch mass.
- If Rank #1 is an underdog cushion, explicitly reconcile whether the same branch tree gives that underdog meaningful outright-win mass.
- Do not name the more famous/stronger side as “potential winner” independently of the handicap tree.
- If the potential winner is identical to a ranked winner contract, use the same canonical contract ID as an alias rather than creating a duplicate observation.

### 4.13 Slate geometry

Before ranking:

- Freeze every user-supplied valid row.
- Mark exact complements, integer-push pairs, overlaps, gaps and free rows.
- State any win count mathematically forced by the slate geometry.
- Forced win-count arithmetic is not forecast accuracy.

### 4.14 Evidence ceilings

Missing or conflicting information lowers the evidence grade; it never authorises invented facts.

Typical statuses:
- `SUPPORTED`
- `LEAN`
- `FORCED RANK`
- `AVOID`

Probability remains unpublished. Value remains undetermined without a validated probability model.

---

## 5. Sport-specific execution rule

For every new event, read the current Drive version of the applicable sport file immediately before research and log its `SFA-<SPORT>` controls.

Current dedicated modules:
- `SFA-CRICKET`
- `SFA-BASKETBALL`
- `SFA-AFL`
- `SFA-RUGBY-LEAGUE`
- `SFA-RUGBY-UNION`
- `SFA-AMERICAN-FOOTBALL`
- `SFA-BASEBALL`
- `SFA-SOCCER`
- `SFA-ICE-HOCKEY`
- `SFA-TENNIS`

Do not transfer scoring levels, rules, exposure units or calibration assumptions across competitions/sports without an explicit approved bridge.

---

## 6. Source hierarchy for future forecast research

Research order:

1. Current official event identity/state/rules.
2. Exact contract terms if the operator was supplied.
3. Official participants: lineup/XI/toss/starter/QB/goalie/team sheet/inactives/late changes.
4. Opponent-adjusted role/exposure/process evidence.
5. Venue/surface/roof/weather/rest/travel.
6. L5/L10/L15/L20 + continuity-qualified H2H.
7. Up to five genuinely comparable D0 mechanism cases, or `NO COMPARABLE CASE`.
8. Strongest ordinary contrary path.
9. Final volatile refresh immediately before issue.

Stop expanding sources when all decision-driving fields are verified or explicitly missing/conflicting, the sport-native mechanism chain is adequately represented, the strongest ordinary kill path is represented, and another search is unlikely to change the ordering before the next volatility refresh.

---

## 7. Running event index — new continuation

No new `P-249+` forecast has been issued in this mini log yet.

| Canonical ID | Event | Sport | Issue state | Method | Current status | Settlement | Retrospective |
|---|---|---|---|---|---|---|---|
| `P-249` | Hanwha Eagles @ KT Wiz | Baseball — KBO | LIVE-REQUEST / STATE GATE FAILED | `MDS-2026.09.02-v3.1` | OPEN — LIVE STATE NOT VERIFIED | NO ACTIONABLE FORECAST ISSUED | NEXT-QUERY PRIORITY STATE CHECK |

When P-249 is issued, replace the placeholder row with the actual event and advance the next-ID pointer to P-250.

---

## 8. New-event append template

Use this template for every new user sports forecast request.

```markdown
# P-### — <Event> — <Competition>

## A. Frozen identity and state
- Canonical ID:
- Request time:
- Final state-check time:
- Information cutoff:
- Sport:
- Competition / format / rules era:
- Official event ID:
- Participants:
- Venue:
- Venue class: OUTDOOR / INDOOR / RETRACTABLE
- Scheduled start — venue local:
- Scheduled start — Australia/Sydney:
- GAME-STATE: PREGAME / LIVE / POSTPONED / SUSPENDED / OTHER
- Method: MDS-2026.09.02-v3.1 or current Drive version
- General algorithm: GFA-2
- Sport algorithm: SFA-<SPORT>
- Candidate origin: USER_SUPPLIED
- Operator: NOT SUPPLIED / <operator>
- Operator terms: NOT SUPPLIED / VERIFIED
- Price role: EXCLUDED FROM SPORTS FORECAST
- Probability state: NOT_GENERATED / NOT_PUBLISHED
- Value state: NO VALUE DETERMINABLE

## B. Target and contract freeze
- TARGET_ID:
- Target definition:
- Start state:
- Endpoint:
- Unit/support:
- Scheduled exposure:
- Termination / censoring / action / void:
- Decision-set ID:

| Candidate ID | Exact contract | Settlement interval | Geometry | Dependence group | Eligible? |
|---|---|---|---|---|---|

### Slate geometry
- Exact complementary pairs:
- Push boundaries:
- Overlaps/gaps:
- Mathematically forced win-count, if any:

## C. Participant / role / release gate
| Decision-driving role | Official identity/status | Expected exposure | Release source/time | Missing/conflict state |
|---|---|---|---|---|

## D. Environment / surface
- Surface / field / strip condition:
- Weather source:
- Match-window temperature:
- Wind speed/gust/direction:
- Ground/court vector:
- Dew point:
- Cloud:
- Precipitation:
- Roof status:
- Mechanistic effect:
- Unknowns:

## E. Reference base-rate table
| Contract | Historical population | N | Descriptive reference rate | Definition / caveat |
|---|---:|---:|---:|---|

No retrospective band anchoring or one-band cap is applied.

## F. L5/L10/L15/L20 + H2H
### Side/player A
| Window | N | Target-relevant outcomes/process | Opponent/regime notes |
|---|---:|---|---|

### Side/player B
| Window | N | Target-relevant outcomes/process | Opponent/regime notes |
|---|---:|---|---|

### Head-to-head
| Window | N | Continuity-qualified meetings | Trend verdict |
|---|---:|---|---|

- Continuity count:
- Short-vs-long trend result:
- Mechanism behind trend:
- De-duplication note:

## G. Sport-native exposure × rate chain
- Baseline:
- Dynamic strength:
- Participant exposure:
- Matchup:
- Context:
- Rate mechanism:
- Exposure mechanism:
- Replacement / phase / score-state paths:

## H. Scenario tree
| Scenario | Representative state | Target outcome corridor | Contracts helped | Contracts hurt |
|---|---|---|---|---|
| Lower | | | | |
| Central | | | | |
| Upper | | | | |
| Material tail / kill path | | | | |

## I. Aggregate component budget
| Aggregate line | Component A floor/centre/high | Component B required to cross | Component B plausible? | Directional result |
|---|---|---|---|---|

## J. Separation budget
| Margin/cushion line | Phase 1 separation | Phase 2 separation | Late/terminal separation | Ordinary cover/fail branches |
|---|---|---|---|---|

## K. Deficit attribution / venue restraint
- Participant-quality deficit:
- Distribution directly affected:
- Opponent branch affected:
- Aggregate consequence:
- Venue factor:
- Does venue merely scale supported exposure, or is it being asked to manufacture missing scoring?

## L. Candidate robustness records
| Candidate | Win mechanism | Strongest ordinary kill path | Extra-condition audit | Evidence ceiling |
|---|---|---|---|---|

## M. Direct marginal-likelihood ranking
| Rank | Candidate | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Probability state |
|---:|---|---|---|---|---|---|---|

## N. Rank-1 conditional coherence
- Rank #1:
- Rank-1 winning branch set:
- Implied target interval/state:

| Other row | COHERENT / PARTIAL_OVERLAP / DISJOINT | Conditional-budget result | Action |
|---|---|---|---|

## O. Potential winner
- Potential winner:
- Endpoint:
- Winner/cushion reconciliation:
- Canonical winner contract alias if applicable:

## P. Source/evidence lineage
| Claim | Exact source/record | Owner/tier | Known/observed/accessed time | Definition | Conflict/missingness |
|---|---|---|---|---|---|

## Q. Final refresh
- Event state refreshed:
- Participants refreshed:
- Weather/surface refreshed:
- Start-crossing check:
- New conflict found:
- Cutoff frozen:

## R. Bottom line
1. Rank #1:
2. Rank #2:
3. Rank #3:
4. Rank #4:
5. Potential winner:

- Important unknowns:
- No probability/edge/ROI/staking claim:
- View appended before delivery: YES
- Google Drive modified: NO
- Prior forecast rewritten: NO
- Automatic settlement performed: NO unless explicitly requested
- Retrospective performed: NO unless explicitly requested
```

---

## 9. Settlement-first template

Use this **before each new sports forecast** for the immediately previous issued event. Settlement and retrospective have priority over research for the new event. If the previous event is not final/settleable, preserve it open and proceed to the new event.

```markdown
# Settlement append — P-###

- Settlement checked at:
- Official final source:
- Official final:
- Competition endpoint:
- Operator/action terms:
- Result status: FINAL / PROVISIONAL / UNRESOLVED / UNSETTLEABLE

| Contract ID | Frozen contract | Official settled quantity | Outcome | Source/definition | Boundary note |
|---|---|---:|---|---|---|

- Potential winner outcome:
- Event closed?: YES / NO
- Remaining unresolved fields:
- Canonical queue change:
- Retrospective status: REQUIRED NEXT IF FINAL / DEFERRED IF NOT FINAL
- Learning register changed: only through the active retrospective/prospective-test procedure
```

A factual settlement does not automatically trigger process grading, lesson creation, or model changes.

---

## 10. Retrospective template — automatic on the next sports query after a verified final

```markdown
# Retrospective append — P-###

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|

## Rank #1 review
- Rank #1:
- Outcome:
- If lost, ordinary failure branch:
- Was the failure branch present before issue?
- Was it given enough structural weight?
- Coherence defect?
- Separation-budget defect?
- Deficit-attribution defect?
- Participant/state/source defect?
- Random tail vs process defect:

## What went right
- Correct mechanisms:
- Correct source/identity/state controls:
- Correct geometry/budget controls:

## What went wrong
- Incorrect mechanism:
- Missing/underweighted branch:
- Source weakness:
- Target/contract issue:
- Arithmetic/coherence issue:

## Learning disposition
- CANDIDATE / TESTING / PROMOTED_PROCESS / RETIRED / SUPERSEDED
- Prospective-test manifest:
- No forecast-weight change from one outcome:
```

Do not promote a forecast weight from a single event or from retrospective slot frequencies. Automatic retrospective means the review is performed; it does **not** loosen the learning-register promotion gates.

---

## 11. Change and source provenance for this initialization

### Drive authority read
- `README.md` — active framework and current method.
- `PREDICTION_LOG_COMBINED.md` — top controlling snapshot, next ID, inherited queue, provenance boundary and P-233/P-234/P-235 watchlist inconsistency.
- `LEARNING_REGISTER.md` — active promoted process controls including L-052 through L-060.
- `RULES_GENERAL.md` — current `GFA-2`, SPORTS_ONLY / MARKET_BLIND gate, release/state/geometry/evidence rules.
- `UPCOMING_GAME_RESEARCH_GUIDE.md` — `UGR-2026.09.02-v1.6` operational lifecycle.
- Current sport files remain read-at-runtime authorities for each future event.

### Current web state check used only to preserve queue state
- P-241 Svajda vs Altmaier: current tennis listing showed upcoming.
- P-242 Marozsan vs Michael Zheng: current reporting indicated rain removed the match from the day's outdoor schedule; no final was used.
- P-243 Linette vs Francesca Jones: current tennis/WTA pages showed suspended.

### Initialization actions
- New local append-only mini running log created: YES.
- Canonical next ID copied from current Drive top snapshot: `P-249`.
- All 3 canonical open events carried forward: YES.
- All 10 canonical final-event follow-ups carried forward: YES.
- P-233/P-234/P-235 provisional watchlist preserved separately: YES.
- Drive modified: NO.
- Existing forecast rewritten: NO.
- Settlement retrospective run: NO.
- Learning register altered: NO.
- Numerical model run: NO.

---

## 12. Operating commitment for subsequent queries

For every new sports query in this continuation:

1. Re-read the current Drive top snapshot and framework versions if material changes may have occurred.
2. **Identify the immediately previous issued forecast event.**
3. **Priority first:** state-check that previous event from authoritative current sources.
4. If the previous event is **FINAL and settleable**, settle every frozen contract first, then perform the full retrospective before researching the new event.
5. If the previous event is **LIVE / SUSPENDED / POSTPONED / ABANDONED-PENDING / final not authoritatively verified / settlement terms unresolved**, do **not** force a retrospective. Keep it open, explicitly note `SETTLEMENT + RETROSPECTIVE DEFERRED TO NEXT QUERY`, then proceed to the current event.
6. Preserve older inherited unresolved/provisional queue items. The automatic priority applies to the **immediately previous issued event**; older queue cleanup can still be handled during a dedicated cleanup request unless resolving it is necessary for the current state/ID.
7. Only after the previous-event gate is complete, use the next unused canonical ID, beginning with **P-249**.
8. Perform comprehensive current web research for the new event under the field-owner/source-lineage hierarchy.
9. Apply `GFA-2` plus the applicable `SFA-<SPORT>`.
10. Keep the sports forecast fully market-blind.
11. Freeze the new card and append it locally before delivery.
12. Advance the running event index and next-ID pointer.
13. Preserve every unresolved/provisional queue item until actually reconciled.
14. Return the **updated full Markdown running log** after each query.
15. Never retrospect a game that is still live/suspended/unsettled; carry it forward to the next query.
16. A retrospective may create candidate/test observations, but no forecast-weight or calibration change is promoted from one outcome.

---

**NEXT CANONICAL ID: `P-249`**


---

# P-249 — Hanwha Eagles @ KT Wiz — Korean KBO — LIVE REQUEST

## A. Previous-event priority gate

The user-directed workflow requires the immediately previous issued event to be settled and retrospectively reviewed before a new card is attempted.

- Previous issued event: `P-248 — St. Louis Cardinals @ Los Angeles Dodgers`.
- Canonical Drive state: **FINAL — STL 13, LAD 8**.
- Canonical status: **SETTLED + RETROSPECTIVE ALREADY COMPLETED**.
- Action here: **NO DUPLICATE RETROSPECTIVE**. The priority requirement was already satisfied in the canonical log.

## B. Frozen identity and requested contracts

- **Canonical ID:** `P-249`
- **Request date:** 2026-09-02 Australia/Melbourne
- **Sport:** Baseball
- **Competition:** 2026 KBO League regular season
- **Event:** Hanwha Eagles @ KT Wiz
- **Venue:** Suwon KT Wiz Park, Suwon
- **Scheduled start:** 2026-09-02 18:30 Asia/Seoul
- **Requested mode:** LIVE
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-BASEBALL`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator/action terms:** NOT SUPPLIED / `UNKNOWN_DEFINITION`

### User-supplied slate

| Contract ID | Contract | Ordinary completed-game geometry |
|---|---|---|
| `P-249-C01` | Hanwha Eagles +4.5 runs | Wins if Hanwha wins/ties or loses by 1–4 |
| `P-249-C02` | KT Wiz -4.5 runs | Wins if KT wins by 5+ |
| `P-249-C03` | Combined Over 8.5 runs | Wins at 9+ combined runs |
| `P-249-C04` | Combined Under 8.5 runs | Wins at 0–8 combined runs |

Under ordinary completed-game rules, C01/C02 are exact half-run complements and C03/C04 are exact half-run complements. Exactly two of the four rows win if the official game completes under ordinary grading. This forced 2-of-4 geometry is **not forecast accuracy**. Operator-specific suspension/official-game/action treatment remains unknown.

## C. LIVE-STATE HARD GATE — FAILED

### Current source conflict

At the research cutoff, current web sources did **not** provide the two-source agreement required by the active state-integrity rule.

| Source lane | Retrieved state | Assessment |
|---|---|---|
| KBO official schedule/scoreboard | Current official web surface was stale/blank for the live score field | FIELD-OWNER STATE DEFECT / cannot control current score |
| MyKBO current search snapshot | **Hanwha 0 — KT 4, Top 3rd, LIVE** | Fresh exact-state indication, but unofficial |
| MyKBO exact-game page/search cache | Still displayed **Scheduled** on another exposed surface | Internal source-state conflict |
| TotalBase current schedule surface | Still displayed pregame/scheduled or stale early state | Does not independently confirm exact live state |
| ScoreCenter/other score pages | Blank or scheduled | Does not confirm exact live state |
| Current OSEN game reporting | Confirms the exact game, Ryu Hyun-jin and So Hyeong-jun, and live first-inning action | Independent current event/participant corroboration, but no exact full score + inning confirmation recovered |

### Gate decision

`GFA-2 / L-026` requires the official live state to control, or—when the field owner is defective—**two independent current sources agreeing on participant orientation, score and phase/inning** before directional live analysis.

That condition was **not met**.

**GAME-STATE: LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST**

No exact current base/out state, current pitcher/pitch count, or sufficiently current independently corroborated inning was frozen. A search-index snapshot showing `0-4 Top 3rd` could already be stale relative to the live game clock, so using it as though it were the present state would violate the remaining-exposure rule.

## D. Current matchup research completed before the state gate stopped ranking

The following is retained as background evidence for any later verified live view or settlement. It is **not** converted into current live picks.

### Team / starter state

- KT entered the game **67-43-3, 2nd**; Hanwha **49-63-3, 8th**.
- Current-season head-to-head entering the game: **KT 9-3 Hanwha**.
- Announced/actual starters: **Hanwha LHP Ryu Hyun-jin** vs **KT RHP So Hyeong-jun**.
- Ryu entered at **8-5, 3.85 ERA**, with a **0-1, 4.11 ERA** 2026 line against KT.
- So entered at **6-3, 3.36 ERA**, with a **0-0, 3.27 ERA** 2026 line against Hanwha.
- So had seven days of rest after reported right-lat discomfort and most recently worked six innings with two runs allowed.
- Ryu's latest start was five innings, one unearned run, but he had gone nine starts without a win; wins themselves are not treated as pitcher-performance statistics.

### Current lineups / roles

Hanwha materially reshuffled its lineup for this game, restoring **Choi In-ho, Yonathan Perlaza and Hwang Young-mook**, with **Ryu Hyun-jin / Heo In-seo** as the battery. The lineup change is treated as a role/exposure change, not an automatic offensive upgrade.

Current live reporting independently confirms **Ryu Hyun-jin** and **So Hyeong-jun** actually started the game.

### Team form — de-duplicated completed-game windows immediately before Sep 2

#### Hanwha
| Window | W-L | Runs scored | Runs allowed | Runs/game | Allowed/game |
|---|---:|---:|---:|---:|---:|
| L5 | 0-5 | 19 | 46 | 3.80 | 9.20 |
| L10 | 1-9 | 47 | 92 | 4.70 | 9.20 |
| L15 | 2-13 | 71 | 127 | 4.73 | 8.47 |
| L20 | 3-17 | 86 | 158 | 4.30 | 7.90 |

**Trend verdict:** the short-window deterioration is persistent and driven much more by run prevention than by a uniformly dead offense. It therefore enlarges KT scoring/separation and late-relief branches; it does not mechanically force an Over.

#### KT
| Window | Record | Runs scored | Runs allowed | Runs/game | Allowed/game |
|---|---:|---:|---:|---:|---:|
| L5 | 3-2 | 19 | 16 | 3.80 | 3.20 |
| L10 | 5-4-1 | 42 | 34 | 4.20 | 3.40 |
| L15 | 7-7-1 | 66 | 58 | 4.40 | 3.87 |
| L20 | 12-7-1 | 107 | 71 | 5.35 | 3.55 |

**Trend verdict:** KT's recent scoring rate is below its L20 pace, while run prevention has remained comparatively strong. A live KT lead therefore does not automatically imply continued margin expansion.

### Current-season H2H continuity block

The continuity-qualified 2026 series before this game contained 12 meetings.

- H2H L5: KT 4-1; Over 8.5 in 3/5; KT -4.5 in 2/5; Hanwha +4.5 in 3/5.
- H2H L10: KT 7-3; Over 8.5 in 7/10; KT -4.5 in 3/10; Hanwha +4.5 in 7/10.
- H2H L12/current-season full continuity set: KT 9-3; Over 8.5 in 9/12; KT -4.5 in 4/12; Hanwha +4.5 in 8/12.
- H2H L15/L20: **NOT AVAILABLE UNDER CURRENT-SEASON CONTINUITY**; older meetings were not padded into the table merely to reach a requested denominator.

**H2H interpretation:** KT's winner advantage is much more durable than a five-run-margin advantage. This distinction would matter materially if/when an exact live state is verified.

### Environment

- Venue class: **OUTDOOR**.
- Current forecast around the game window indicated roughly mid-20s °C, high humidity and light westerly/northwesterly wind, with no strong rain signal on the retrieved game page.
- A fresh field-owner Korean Meteorological Administration venue-vector record was not recovered in this pass.
- Therefore conditions are treated as a limited contextual/variance input, not a directional total signal.

## E. D0 / prior-mechanism retrieval

Two relevant prior KBO cases were used only as mechanism challenges:

1. **P-016 Kiwoom @ Lotte** — narrow Lotte win / low total; starter length and rested relief preserved a close game. Lesson: a winner direction and a cushion direction are separate margin questions.
2. **P-049 Doosan @ KIA** — KIA 2-1; both starters worked seven innings. Lesson: total direction must model the complete starter-to-bullpen exposure chain rather than starter ERA or recent run totals alone.

These outcomes do **not** vote for a direction and are not probability weights.

## F. Mechanical map of the single-source `0-4 Top 3rd` snapshot — NOT A FORECAST

Because the exact state did not pass the live-state gate, this section records only settlement arithmetic for the exposed snapshot.

If `Hanwha 0 — KT 4, Top 3rd` were independently confirmed:

- **Over 8.5** would require **5+ additional combined runs**.
- **Under 8.5** would require **4 or fewer additional combined runs**.
- KT currently leading by four would **not yet cover -4.5**.
- **KT -4.5** would require KT to finish at least five runs ahead; from a four-run lead, KT must create at least one additional net run of separation over the remainder.
- **Hanwha +4.5** would still cover if the remaining scoring were equal, or if Hanwha reduced the deficit.
- Representative KT wins such as 4-0, 5-1, 6-2 or 7-3 would still cash **Hanwha +4.5**.
- Representative 5-0, 6-1, 7-2 or 8-3 finishes would cash **KT -4.5**.

For the total, a five-run remaining requirement is reachable with the amount of scheduled baseball apparently remaining, but without the verified current inning/base-out/pitcher state it is not legitimate to say whether that requirement is likely or unlikely **now**.

## G. Ranked decision

### Required output under the governing hard gate

| Rank | Contract | Decision |
|---:|---|---|
| — | Hanwha +4.5 | **NOT RANKED — LIVE STATE NOT VERIFIED** |
| — | KT -4.5 | **NOT RANKED — LIVE STATE NOT VERIFIED** |
| — | Over 8.5 | **NOT RANKED — LIVE STATE NOT VERIFIED** |
| — | Under 8.5 | **NOT RANKED — LIVE STATE NOT VERIFIED** |

**Potential winner:** **NOT ISSUED — LIVE STATE NOT VERIFIED**

This is deliberately stricter than inventing a ranking from a possibly stale score/inning. It follows the user's instruction to avoid hallucinations and the active project hard gate.

## H. Queue / continuation update

- `P-249` status: **OPEN — LIVE STATE NOT VERIFIED / NO ACTIONABLE LIVE FORECAST ISSUED**
- Settlement rows to grade: **NONE**, because no directional forecast was issued.
- Next-query priority: **state-check P-249 first**. If final, record the verified final and close this no-action event; there is no pick-outcome retrospective to score, although the state-gate process can be reviewed.
- Older inherited unresolved/provisional queue remains unchanged.
- Drive modified: **NO**
- Existing forecast rewritten: **NO**
- Numerical probability generated: **NO**

**NEXT CANONICAL ID: `P-250`**

---

# P-250 — Yunnan Yukun vs Chongqing Tonglianglong — 2026 China FA Cup Quarterfinal — PREGAME

## A. Previous-event priority gate

Immediately previous local event: `P-249 — Hanwha Eagles @ KT Wiz`.

- Priority state-check performed first.
- P-249 remains **OPEN / LIVE**.
- No directional P-249 forecast had been issued because the live-state hard gate failed.
- **Settlement + retrospective: DEFERRED — GAME STILL LIVE.**
- P-249 remains in the unresolved queue for a future query/state check.

## B. Frozen identity, schedule and endpoint

- **Canonical ID:** `P-250`
- **Competition:** 2026 Chinese FA Cup — Quarterfinal
- **Event:** Yunnan Yukun vs Chongqing Tonglianglong
- **Venue:** Yuxi Plateau Sports Center, Yuxi, Yunnan, China
- **Venue class:** OUTDOOR / plateau venue
- **Scheduled kickoff:** 2026-09-02 20:00 Asia/Shanghai / 22:00 Australia/Melbourne
- **Final preissue status refresh:** 2026-09-02 21:52:08 Australia/Melbourne / 19:52:08 China
- **GAME-STATE:** PREGAME / SCHEDULED
- **Cutoff invariant:** PASS — frozen before kickoff
- **Method:** `MDS-2026.09.02-v3.1`; `GFA-2`; `SFA-SOCCER`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability:** NOT GENERATED / NOT PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Operator:** NOT SUPPLIED
- **Goal contracts:** 90-minute regulation including stoppage; extra time/penalties excluded
- **Potential-winner endpoint:** TO ADVANCE

## C. Frozen candidate slate

| ID | Contract | Endpoint / geometry |
|---|---|---|
| P-250-C01 | 1st Half Over 0.5 Goals | 1+ goals by HT |
| P-250-C02 | 1st Half Under 0.5 Goals | 0-0 at HT |
| P-250-C03 | Full Match Over 2.5 Goals | 3+ regulation goals |
| P-250-C04 | Full Match Under 2.5 Goals | 0-2 regulation goals |
| P-250-C05 | Total Corners Over 8.5 | 9+ regulation corners; research count anchored to TotalCorner-style full-match data |

C01/C02 and C03/C04 are exact complementary pairs. The corner row is definition-capped because the user supplied no operator/provider semantics.

## D. Confirmed starting XIs

**Yunnan:** Wang Zhifeng; Tsui Wang-Kit; Yi Teng; Burke; Xu Xin; Ionita/Jonica; Hou Yongyong; Caio; Oscar Taty Maritu; Huang Zichang; Bunyamin Abdusalam.

**Chongqing:** Yao Haoyang; Yue Ruijie; Liu Mingshi; He Xiaoqiang; Ngadeu; Lukang/Lucas; Li Zhenquan; Zhang Zhixiong; Cîmpanu/Kempanu; Landry Dimata; Wu Yuxi.

Yunnan selected a high-attacking first XI. Chongqing retained a compact defensive structure while starting Dimata and Cîmpanu/Kempanu; this is materially stronger than the rotated Aug. 29 league XI.

## E. Strength / recent regime

- Yunnan league: 10-5-10, 49-51; home 7-2-3, 26-19.
- Chongqing: 7-10-8, 26-29; away 3-5-5, 10-15.
- Yunnan latest five: 0-6, 3-3, 3-1, 1-0, 2-3.
- Chongqing latest five: 1-1, 0-1, 0-0, 2-3, 0-2.

Yunnan carries the wider scoring tail; Chongqing carries the lower-scoring regime. Neither raw trend is allowed to control without lineup/tactical reconciliation.

## F. Recency / first-half and 2.5-goal evidence

- Yunnan broader retrieved sample: first-half Over 0.5 in 17/21; latest five 4/5.
- Chongqing broader retrieved sample: first-half Over 0.5 in 13/19; latest five 2/5.
- Chongqing's two completed 2026 FA Cup matches both had a first-half goal.
- Yunnan freshest 10-match profile: 9/10 Over 2.5; broader sample about 19/21.
- Chongqing freshest 10-match profile: 2/10 Over 2.5; broader sample about 4/19.
- Exact definition-compatible L15/L20 half-time/corner event tables were not fully exposed before cutoff; broader 19/21-game samples are treated only as surrogate trend context, not mislabeled exact windows.

## G. H2H continuity

Current-season meeting: **Chongqing 0-0 Yunnan**, HT 0-0, corners 6-3. Older 2023-24 meetings are different competition/roster regimes and are descriptive only.

## H. Corner process

- Yunnan: roughly 4.5-5.1 corners for and 4.9-5.0 conceded; latest-five match-corner totals 10,14,12,13,8 (4/5 Over 8.5).
- Chongqing: roughly 3.9 for and 6.0-6.4 conceded; away about 3.15 for and 7.15 conceded; latest-five totals 9,8,7,11,10 (3/5 Over 8.5).
- Matchup mechanism: Yunnan home pressure vs a deeper Chongqing structure creates width/end-line/clearance exposure. Either side conceding first can increase the trailer's cross/set-play/corner exposure.
- Exact operator/provider definition absent -> C05 capped at `FORCED RANK / MEDIUM-LOW`.

## I. Environment

Current structured weather near 19:51 local was clear at about 24C with no strong rain-suppression signal. Exact wind vector/dew point and a field-owner surface report were not recovered to sufficient precision and remain unavailable. Plateau/home context is treated as a fatigue/context branch, not an automatic scoring boost.

## J. Scenario tree

- Lower: 1-0 Yunnan / 1-1 / 2-0 Yunnan.
- Central: **2-1 Yunnan** / 1-1 into late pressure.
- Upper: 3-1 / 3-2 after an early-goal chase switch.
- Over kill path: 0-0 HT plus Chongqing compact suppression.
- Under kill path: early goal opens transition/chase exposure.

Representative scores are qualitative branch illustrations only.

## K. Ranked decision

| Rank | Contract | Verdict | Evidence | Core reason |
|---:|---|---|---|---|
| **1** | **1st Half Over 0.5 Goals** | **LEAN** | **MEDIUM** | High Yunnan early-event rate, both Chongqing cup games with first-half goals, and attacking confirmed XIs. Counter-path: May H2H 0-0 HT and knockout caution. |
| **2** | **Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | Direct corner rates, Chongqing's high away corners-conceded profile, 7/10 combined latest-five samples clearing 8.5, and current H2H at 9. Definition gap prevents LEAN. |
| **3** | **Full Match Over 2.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | Yunnan home/recent scoring tail and aggressive XI; an early goal creates chase. Chongqing's low-scoring away profile prevents stronger language. |
| **4** | **Full Match Under 2.5 Goals** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** | 1-0, 2-0 and 1-1 remain credible through Chongqing suppression. Ranked below Over because Yunnan's home attack/defensive volatility and full-strength cup XIs preserve a stronger three-goal tail. |
| **5** | **1st Half Under 0.5 Goals** | **AVOID relative to C01** | **LOW-MEDIUM** | Needs 0-0 HT; supported by May H2H but opposed by broader first-half-goal evidence and current attacking personnel. |

## L. Rank-1 coherence

Rank #1 state = at least one first-half goal.
- Corners O8.5: PARTIAL_OVERLAP.
- FT O2.5: COHERENT / PARTIAL.
- FT U2.5: PARTIAL_OVERLAP (1-0, 2-0, 1-1 still win).
- 1H U0.5: DISJOINT exact complement.

## M. Potential winner

**Yunnan Yukun to advance — LEAN.**

Home record, stronger attacking selection and Chongqing's low away scoring support Yunnan, but Chongqing's defensive structure and the May 0-0 keep a regulation draw live. This is an advancement lean, not a guarantee of a 90-minute win.

## N. Queue / append confirmation

- P-249 checked first: YES — still live
- P-249 settlement/retrospective: DEFERRED
- P-250 pregame view frozen before kickoff: YES
- Drive modified: NO
- Numerical probability generated: NO
- Learning register changed: NO
- **NEXT CANONICAL ID: P-251**


---

# P-251 — Sassuolo vs Frosinone — 2026/27 Coppa Italia Round of 32 — PREGAME

## A. Previous-event priority gate

Immediately previous issued event: `P-250 — Yunnan Yukun vs Chongqing Tonglianglong`.

- State check performed before this forecast.
- At the current query time the fixture had already kicked off, but no trustworthy field-owner final had been recovered.
- A contradictory low-quality search surface already labelled the match "final 0-0" far too early relative to the known 20:00 China kickoff, while other current sources still exposed pregame/live shells.
- That impossible/stale result was quarantined under the official-placeholder/source-state rule.
- **P-250 remains OPEN / LIVE OR FINAL-NOT-VERIFIED.**
- **Settlement + retrospective: DEFERRED TO NEXT QUERY.**
- No P-250 result or retrospective is invented.

## B. Frozen identity, schedule and endpoint

- **Canonical ID:** `P-251`
- **Sport:** Soccer
- **Competition:** Coppa Italia Frecciarossa 2026/27
- **Round:** Round of 32 / sedicesimi
- **Event:** Sassuolo vs Frosinone
- **Venue:** MAPEI Stadium - Città del Tricolore, Reggio Emilia, Italy
- **Surface:** natural grass
- **Venue class:** OUTDOOR
- **Field-owner kickoff:** 2026-09-02 15:00 Europe/Rome
- **Australia/Melbourne kickoff:** 2026-09-02 23:00 Australia/Melbourne
- **Final preissue refresh:** immediately before 15:00 local kickoff
- **GAME-STATE:** PREGAME / SCHEDULED
- **Schedule conflict:** older/secondary pages exposed 16:00 or 18:30, but current Lega Serie A referee/schedule publication and both club/current live sources resolve kickoff at 15:00. Field owner controls.
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-SOCCER`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator:** NOT SUPPLIED
- **Goal endpoint:** 90-minute regulation including stoppage, excluding extra time/penalties
- **Potential-winner endpoint:** **TO ADVANCE** from the knockout tie

## C. Candidate slate and geometry

| Contract ID | Contract | Settlement region | Dependence |
|---|---|---|---|
| `P-251-C01` | 1st Half Over 0.5 Goals | 1+ goals by HT | P251-1H-GOAL |
| `P-251-C02` | 1st Half Under 0.5 Goals | 0-0 at HT | P251-1H-GOAL |
| `P-251-C03` | Full Match Over 2.5 Goals | 3+ regulation goals | P251-FT-GOAL |
| `P-251-C04` | Full Match Under 2.5 Goals | 0-2 regulation goals | P251-FT-GOAL |
| `P-251-C05` | Total Corners Over 8.5 | 9+ regulation corners under the research provider convention | P251-CORNER |

- C01/C02 are exact complements.
- C03/C04 are exact complements.
- Those four goal rows force exactly two winners if the regulation game is completed normally.
- C05 is a separate derivative target.
- The user did not supply an operator or exact corner provider definition. C05 therefore cannot exceed `FORCED RANK / MEDIUM-LOW` evidence even if the direct corner process is favorable.

## D. Field-owner schedule and match administration

Current Lega Serie A publication:
- Sassuolo-Frosinone: Wednesday 2 September, 15:00.
- Referee: Andrea Calzavara.
- Assistants: Gilberto Laghezza and Glauco Zanellati.
- Fourth official: Paride Tremolada.
- VAR: Daniele Rutella.
- AVAR: Matteo Gariglio.

The referee assignment is an identity/administration fact only; no referee scoring effect is assumed without current validated evidence.

## E. Confirmed starting XIs

Current published official lineups were corroborated by multiple live/pre-match sources.

### Sassuolo — 4-3-3
Turati; Cinquegrano, Odenthal, Leysen, Obrador; Thorstvedt, Lipani, Ghion; Volpato, Bowie, Dominguez.

### Frosinone — 4-3-3
Desplanches; Tchato, Akpoguma, Amey, Terzic; El Azzouzi, Grillitsch, Hasa; Fini, Zerbin, Birligea.

### Lineup interpretation

- Sassuolo rotate several headline first-choice names relative to their strongest league XI, but the front three of Volpato-Bowie-Dominguez plus Thorstvedt still supplies credible shot and transition quality.
- Frosinone's Birligea/Zerbin/Fini attacking line is not a low-threat reserve front three.
- Both coaches retain an orthodox attacking 4-3-3 rather than a clearly defensive five-back cup shell.
- The rotation widens the full-match uncertainty and prevents the current 3/3 Sassuolo Over streak from being copied mechanically.

## F. Environment / surface gate

- Outdoor natural-grass stadium.
- Current Reggio Emilia forecast around kickoff: hot, roughly upper-20s to low-30s °C, light wind and no meaningful rain signal.
- No evidence of a waterlogged or otherwise abnormal surface was recovered.
- Heat can increase late fatigue/substitution effects, but it is not assigned an automatic Over direction.
- Weather therefore does not overturn the current goal/corner ordering.

## G. Current-season competitive regime

### Sassuolo — first three competitive matches
1. Sassuolo 3-0 Cesena — Coppa Italia — HT 2-0 — corners 4-5 (9)
2. Atalanta 2-1 Sassuolo — Serie A — HT 1-0 — corners 4-4 (8)
3. Sassuolo 2-1 Torino — Serie A — HT 1-1 — corners 4-3 (7)

Current competitive summary:
- First-half Over 0.5: **3/3**
- Full Over 2.5: **3/3**
- Match corners Over 8.5: **1/3**

### Frosinone — first three competitive matches
1. Frosinone 4-1 Juve Stabia — Coppa Italia — HT 3-0 — corners 4-2 (6)
2. Frosinone 0-1 Juventus — Serie A — HT 0-1 — corners 3-12 (15)
3. Fiorentina 0-3 Frosinone — Serie A — HT 0-2 — corners 8-5 (13)

Current competitive summary:
- First-half Over 0.5: **3/3**
- Full Over 2.5: **2/3**
- Match corners Over 8.5: **2/3**

### Combined current-season descriptive reference
- First-half Over 0.5: **6/6**
- First-half Under 0.5: **0/6**
- Full Over 2.5: **5/6**
- Full Under 2.5: **1/6**
- Total Corners Over 8.5: **3/6**

These are only six selected early-season team-game observations and are **not probabilities**. Under the early-season shrinkage rule they are treated as a regime signal, not a calibrated base rate.

## H. Broader L10 process block

### Sassuolo
Current StatMuse Serie A L10:
- Goals: 13
- Goals conceded: 13
- xG: approximately 15.1
- xGA: approximately 12.7-13.4 depending on the exact current query
- Shots: 135
- SOT: 46
- Corners won: approximately 32 over the latest 10 Serie A matches

Interpretation:
- Sassuolo's chance creation has run above its actual goal total.
- Neither attack nor defence supports an extreme low-event prior.
- Current cup rotation is a genuine regime adjustment against simply copying the L10 centre.

### Frosinone
Current StatMuse Serie A L10:
- Goals: 9
- Goals conceded: 9
- xG: 12.26
- xGA: 14.28
- Shots: 142
- SOT: 49
- Corners won: approximately 57

Interpretation:
- Frosinone's observed 9-9 goal line understates the event volume suggested by its xG/xGA.
- Its corner generation has remained comparatively high even with low possession in several matches.
- The recent 3-0 Fiorentina win is not treated as a new true scoring rate by itself.

### L5/L15/L20 handling
- Current L5/current-season match rows were retrieved directly.
- L10 process rows were recovered.
- Exact single-provider definition-compatible L15/L20 event-by-event first-half and corner tables were not fully reconstructable before kickoff.
- Older-season windows were inspected only as shrunk prior context; they were not allowed to override the confirmed lineups or current competitive regime.
- Missing exact L15/L20 tables are recorded as `NOT AVAILABLE AFTER SEARCH`, not silently filled.

## I. Head-to-head continuity

Last eight meetings:
- Sassuolo 0-1 Frosinone — HT 0-1 — 11 corners
- Frosinone 1-2 Sassuolo — HT 1-1 — 8 corners
- Sassuolo 1-0 Frosinone — HT 0-0 — 3 corners
- Frosinone 4-2 Sassuolo — HT 1-2 — 11 corners
- Sassuolo 2-2 Frosinone — HT 0-2 — 9 corners
- Frosinone 0-2 Sassuolo — HT 0-1 — 11 corners
- Frosinone 0-1 Sassuolo — HT 0-0 — 10 corners
- Sassuolo 2-2 Frosinone — HT 1-2 — 9 corners

Descriptive H2H:
- First-half Over 0.5: **6/8**
- Full Over 2.5: **4/8**
- Total Corners Over 8.5: **6/8**
- Average total goals: about **2.8**
- Average total corners: about **9**

Continuity caveat:
- Several meetings are from materially older Serie A/Serie B roster and coaching regimes.
- The 2024-25 Serie B meetings are the nearest continuity references.
- H2H is therefore supportive context only, not a fitted weight.

## J. Corner-process audit

### Direct current evidence
- Sassuolo current competitive corner totals: 9, 8, 7.
- Frosinone current competitive corner totals: 6, 15, 13.
- Combined: 3/6 above 8.5.
- H2H: 6/8 above 8.5, with nine average total corners.
- Frosinone's broader L10 Serie A corner generation is high at roughly 5.7 per match.
- Sassuolo's current wing selection Volpato/Dominguez plus overlapping fullback roles preserves width/end-line entry exposure.
- Frosinone's Fini/Zerbin attacking widths and its recent ability to generate corners while playing lower-possession football preserve a chasing/counter corner path.

### Score-state branches
- Early Sassuolo goal: lowers some home attacking demand but can raise Frosinone crossing/corner volume.
- Early Frosinone goal: raises Sassuolo territory and wide pressure.
- 0-0 deep into the match: both clubs retain knockout urgency, potentially supporting late corner accumulation.
- Efficient central finishing with limited blocked/cross sequences is the main Over-8.5 kill path.

### Definition cap
Exact operator/provider corner semantics were not supplied. C05 is therefore ranked but capped at `FORCED RANK`.

## K. Goal-process scenario tree

| Scenario | Representative regulation family | Mechanism |
|---|---|---|
| Lower | 1-0 / 1-1 / 2-0 | rotation suppresses finishing; knockout caution; Desplanches/Turati absorb central chances |
| Central | 2-1 either way / 1-2 | both 4-3-3s create enough transition and second-phase attacking exposure |
| Upper | 3-1 / 2-2 / 3-2 | early goal plus open chase, heat/fatigue and stronger attacking substitutions |
| Over kill path | 0-0 HT, low-quality circulation, one side scores once after the hour | defeats C01/C03 |
| Under kill path | first-half goal forces sustained chase and both teams generate replacement-phase chances | defeats C02/C04 |

Representative scores are scenario families only, not precise predictions.

## L. Component budget for 2.5

The full-match Over needs at least three regulation goals.

Plausible allocations:
- Sassuolo 2 + Frosinone 1
- Sassuolo 1 + Frosinone 2
- 3-0 either way

Under wins through:
- 0-0
- 1-0 / 0-1
- 1-1
- 2-0 / 0-2

Current evidence supports both teams reaching at least one meaningful creation phase. The decisive question is conversion, not merely territory. Sassuolo's rotation lowers certainty, but the combined current-season 5/6 Over signal plus both teams' xG/process tails keeps the three-goal family marginally ahead.

## M. Ranked decision — most likely to least likely

| Rank | Contract | Verdict | Evidence quality | Why |
|---:|---|---|---|---|
| **1** | **P-251-C01 — 1st Half Over 0.5 Goals** | **LEAN** | **MEDIUM** | All six current competitive games across the two clubs have contained a first-half goal, the confirmed XIs preserve real attacking exposure, and 6/8 H2Hs also had a first-half goal. Small-sample shrinkage and knockout caution prevent stronger language. |
| **2** | **P-251-C03 — Full Match Over 2.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | Five of six current competitive games cleared 2.5; Sassuolo's recent xG and Frosinone's xG+xGA indicate enough event volume for a three-goal branch. Rotation and the latest 1-0 H2H keep the evidence below Medium. |
| **3** | **P-251-C05 — Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | H2H is 6/8 over this threshold, Frosinone has a strong broader corner-generation profile, and either trailing state can raise width/cross exposure. Current-season team totals are only 3/6 over, and provider semantics are unspecified. |
| **4** | **P-251-C04 — Full Match Under 2.5 Goals** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** | 1-0, 1-1 and 2-0 remain substantial branches, especially with Sassuolo rotating Berardi/Laurienté out of the XI. It is narrowly below the Over because both current XIs still carry enough transition/shot quality and five of six competitive matches reached three goals. |
| **5** | **P-251-C02 — 1st Half Under 0.5 Goals** | **AVOID RELATIVE TO C01** | **LOW-MEDIUM** | Requires 0-0 HT and is opposed by the 6/6 current competitive early-goal record plus 6/8 H2H first-half-goal frequency. Its best path is cup caution plus rotation suppressing chance quality. |

## N. Rank-1 conditional coherence

Rank #1 winning state: **at least one first-half goal**.

- C03 Full Over 2.5: `COHERENT / PARTIAL` — an early goal raises chase/open-game exposure but does not guarantee three.
- C05 Corners Over 8.5: `PARTIAL_OVERLAP` — an early goal can suppress the leader's attack but raise the trailer's wide pressure.
- C04 Full Under 2.5: `PARTIAL_OVERLAP` — 1-0, 2-0 and 1-1 still win after a first-half goal.
- C02 1H Under 0.5: `DISJOINT` exact complement.

No high-ranked row is structurally impossible under Rank #1.

## O. Potential winner

### **Sassuolo to advance — SLIGHT LEAN**

Endpoint: advancement from the Coppa Italia knockout tie, including extra time/penalties if necessary.

Supporting mechanisms:
- home venue;
- deeper top-end attacking bench/squad even after cup rotation;
- Sassuolo's recent attacking process remains credible;
- broader H2H favors Sassuolo historically.

Counter-paths:
- Frosinone just won 3-0 away at Fiorentina;
- the confirmed Frosinone XI is strong and experienced;
- Frosinone won the latest meeting at Mapei 1-0;
- Sassuolo have rotated several headline attackers out of the starting XI.

This is a narrow advancement lean, **not** a strong 90-minute winner call.

## P. Important limitations

- No fitted/validated numerical model.
- No internal probability publication.
- No bookmaker odds, implied probability or line movement used.
- Exact operator corner definition not supplied.
- Current-season sample is only three competitive matches per club and is aggressively shrunk.
- Exact L15/L20 first-half/corner tables were not fully reconstructable before kickoff.
- The final lineups materially differ from the strongest league XIs, especially Sassuolo.

## Q. Source / provenance snapshot

Decisive sources:
- Lega Serie A Coppa Italia schedule/referee publication — field-owner kickoff and officials.
- Frosinone official club site — current 25-man call-up and 15:00 kickoff.
- Current published official-lineup reports corroborated by multiple live match services.
- FBref — current 2026/27 competitive results/schedules.
- StatMuse — broader Serie A xG/xGA/shots/corner process.
- TotalCorner — H2H scores, half-time states and corner history.
- Reggio Emilia weather source — current temperature/wind/rain context.

Market prices appearing incidentally on some third-party pages were **not used** in the forecast or ranking.

## R. Queue / append confirmation

- P-250 state checked first: YES
- P-250 settlement/retrospective: DEFERRED — no trustworthy final
- P-251 pregame identity/schedule resolved: YES
- P-251 lineups refreshed: YES
- P-251 forecast frozen before kickoff: YES
- Drive modified: NO
- Prior forecast rewritten: NO
- Numerical model run: NO
- Learning register changed: NO
- **NEXT CANONICAL ID: P-252**


---

# P-252 — Belfast Wolves vs Edinburgh Castle Rockers — European T20 Premier League 2026, Match 11 — PREGAME

## A. Previous-event priority gate

Immediately previous issued event: `P-251 — Sassuolo vs Frosinone`.

- State check performed first.
- Scheduled kickoff had crossed, but no authoritative final was available.
- The event therefore remains **OPEN / LIVE OR FINAL-NOT-YET-VERIFIED**.
- **Settlement + retrospective: DEFERRED TO NEXT QUERY.**
- No result, pick grade, or retrospective is fabricated while the event is unfinished/unverified.

## B. Frozen identity, schedule, venue and target

- **Canonical ID:** `P-252`
- **Sport:** Cricket
- **Competition:** European T20 Premier League 2026
- **Match:** Match 11
- **Event:** Belfast Wolves vs Edinburgh Castle Rockers
- **Venue:** Sportpark Westvliet / Sportpark Duivesteijn, Voorburg, Netherlands
- **Official scheduled start:** 2026-09-02 15:15 CEST
- **Australia/Melbourne start:** 2026-09-02 23:15 AEST
- **Frozen preissue state:** 2026-09-02 23:14 Australia/Melbourne / 15:14 CEST
- **GAME-STATE:** PREGAME / OFFICIAL PAGE STILL "YET TO BAT"
- **Cutoff invariant:** PASS — before scheduled start
- **Toss:** NOT YET PUBLISHED at frozen cutoff
- **Confirmed playing XIs:** NOT YET PUBLISHED at frozen cutoff
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-CRICKET`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator / reduced-overs / action terms:** NOT SUPPLIED / `UNKNOWN_DEFINITION`

### Exact target interpretation

The user's phrase "Castle Rockers 1st innings" is interpreted as **Edinburgh Castle Rockers' own batting innings**, regardless of whether it is the first or second innings of the match.

Targets:
- `P252-ECR-PP6`: Edinburgh runs at the end of six legal overs of their batting innings, subject to innings termination/action rules.
- `P252-ECR-INN`: Edinburgh completed batting-innings total / 20-over endpoint under the operator's exact action terms.

This distinction is crucial because, if Edinburgh bats second, a successful chase can terminate before 20 overs. No fictional "projected 20-over score" is substituted for a completed chase.

## C. Supplied contract geometry

| Contract ID | Contract | Ordinary win region | Dependence |
|---|---|---|---|
| `P-252-C01` | Edinburgh 20-over/innings total Over 165.5 | 166+ settled runs under exact innings/action terms | P252-ECR-INN |
| `P-252-C02` | Edinburgh 20-over/innings total Under 165.5 | 0-165 settled runs under exact innings/action terms | P252-ECR-INN |
| `P-252-C03` | Edinburgh first 6 overs Over 44.5 | 45+ after six legal overs | P252-ECR-PP6 |
| `P-252-C04` | Edinburgh first 6 overs Under 44.5 | 0-44 after six legal overs | P252-ECR-PP6 |

- C01/C02 are exact half-run complements under ordinary action.
- C03/C04 are exact half-run complements under ordinary action.
- Exactly two of the four rows win if both targets settle normally.
- This forced 2-of-4 geometry is not forecast accuracy.

## D. Toss / innings-order mixture — mandatory because toss unresolved

### State 1 — Edinburgh bats first
- Full 20-over exposure is available unless all out, weather, or another termination mechanism intervenes.
- The 165.5 line sits above the current venue's ordinary completed-first-innings centre.
- Edinburgh's explosive top order creates a legitimate 170+ branch, but the line requires sustained middle/death scoring after the powerplay.

### State 2 — Edinburgh bats second
- Chase censoring becomes material.
- If Belfast sets a target below 166 and Edinburgh successfully chases it, the innings can end below 165.5 even after a very fast powerplay.
- This state therefore strengthens **Under 165.5** relative to a naive 20-over extrapolation.

### State 3 — reduced overs / weather interruption
- Match-window weather is currently dry enough that this is not the central branch.
- Exact sportsbook treatment is unknown because the operator was not supplied.
- The row is not redefined post hoc if overs are lost.

## E. Current team state

### Edinburgh Castle Rockers

Official ETPL squad core includes:
- Mitchell Santner (captain)
- Trent Boult
- Andries Gous
- Ross Adair
- JJ Smuts
- Brandon McMullen
- Laurie Evans
- Tom Curran
- Gareth Delany
- Mark Watt
- Jack Jarvis
- Andrew Tye / Safyaan Sharif and other squad options

Confirmed previous-XI continuity in both completed wins was strong:
`Ross Adair / JJ Smuts / Andries Gous / Brandon McMullen / Laurie Evans` formed the main top/middle batting chain, with Santner, Curran and Delany behind them.

### Belfast Wolves

Official ETPL squad includes:
- Glenn Maxwell
- Devon Conway
- David Miller
- Paul Stirling
- Mark Chapman
- Lorcan Tucker
- Tim Tector
- Mark Adair
- Chris Jordan
- Fred Klaassen
- Matthew Humphreys
- Saurabh Netravalkar and additional squad options

Belfast's previous conventional 20-over XI used a strong new-ball/pace group around Klaassen, Mark Adair, Jordan and Netravalkar/Humphreys, with Maxwell/Chapman providing additional matchup options.

### Participant ceiling

Because the exact toss and playing XIs were not released before cutoff:
- no player-specific prop is selected;
- any direction relying on one named bowler being certain to open is capped;
- the rankings rely on robust team-phase mechanisms that survive plausible XIs.

## F. Edinburgh current batting evidence

### Completed chase vs Glasgow Cosmic — Aug 27
- Target: 116
- Edinburgh: **116/3 in 11.3 overs**
- Powerplay: **70 runs**
- Ross Adair: 28 off 12
- JJ Smuts: 16 off 9
- Andries Gous: 40* off 28
- Brandon McMullen: 23 off 16

### Completed chase vs Dublin Guardians — Aug 30
- Target: 110
- Edinburgh: **110/6 in 13.4 overs**
- Powerplay: **68 runs**
- Ross Adair: 24 off 7
- JJ Smuts: 33 off 24
- Brandon McMullen: 12 off 6
- Laurie Evans: 19 off 24

### Critical interpretation

The two Edinburgh completed batting innings provide:
- **2/2 Over 44.5 at six overs**
- powerplay scores of **70 and 68**

But they do **not** provide valid evidence that a 20-over Edinburgh innings naturally finishes near 110-116. Both were chases of small targets and ended early. Their final scores are **chase-censored** and are prohibited from being treated as batting-first 20-over baselines.

The powerplay evidence is much more portable because both innings reached six overs and Edinburgh attacked immediately in each.

## G. Belfast current bowling / opponent state

Belfast's most useful full 20-over defensive evidence:
- Dublin Guardians were held to **132/9** after Belfast made 184/7.
- Belfast later conceded only 56/2 in a five-over rain-reduced game against Amsterdam, which is not comparable to a 20-over run-rate baseline.
- Against Rotterdam, Belfast made 156/9 first; only one over of Rotterdam's chase was completed before a no-result.

Belfast therefore has credible bowling personnel, but limited same-horizon full-match defensive evidence. The strongest caution against Edinburgh's powerplay Over is Belfast's multiple quality seam options, not a large team-level sample.

## H. Voorburg venue-and-format baseline — innings-order rung

Completed conventional first-innings scores at this venue before Match 11:
- 157/8
- 184/7
- 115 all out
- 183/5
- 156/9
- 109 all out
- 140/9

The five-over reduced match (56/2) is excluded from the 20-over first-innings baseline.

### Derived descriptive baseline
- Mean: approximately **149**
- Median: **156**
- Over 165.5: **2/7**
- Under 165.5: **5/7**

This is a small inaugural-league sample, so it is descriptive rather than a fitted probability. Still, 165.5 is visibly above the ordinary venue centre.

### Powerplay context
Edinburgh itself scored **70** and **68** in the first six overs of its two completed chases. The line of 44.5 requires only 7.5 runs per over, materially below those two observed Edinburgh starts.

## I. Weather / match conditions

Current Voorburg hourly forecast around 15:00-18:00:
- around **20°C**
- broadly dry / near-zero expected precipitation in the strongest hourly source
- west to southwest breeze around Beaufort 3
- no strong rain signal during the main match window

A second forecast source retained some drizzle/rain uncertainty later in the day, so weather is not labelled guaranteed dry.

### Conditions interpretation
- no current basis for a deterministic rain-Under adjustment;
- moderate breeze/overcast conditions can help new-ball movement, but the magnitude is not sufficient to erase Edinburgh's recent powerplay aggression;
- strip-specific field-owner pitch wording was not recovered at toss time and remains `NOT AVAILABLE`.

## J. Reference-base-rate summary

| Contract | Direct descriptive evidence | Result |
|---|---|---|
| ECR Over 44.5 PP | Edinburgh completed ETPL powerplays | 2/2 over — 70, 68 |
| ECR Under 44.5 PP | Same | 0/2 under |
| ECR Over 165.5 full innings | No uncensored ECR 20-over batting sample yet; venue conventional first innings | Venue 2/7 over |
| ECR Under 165.5 full innings | Same | Venue 5/7 under |

No 2-game team sample or 7-game venue sample is converted into an internal probability.

## K. Current form / L5-L20 handling

This is an inaugural competition and Edinburgh has only:
- two completed matches,
- one abandonment before a ball.

Belfast similarly has only a handful of tournament matches with weather-shortened/no-result exposure.

Therefore exact ETPL L5/L10/L15/L20 **cannot exist** for these franchises yet. The framework does not permit padding the windows with unrelated pre-franchise team games. Career/player T20 records are used as role priors only.

**H2H:** no prior Belfast Wolves vs Edinburgh Castle Rockers ETPL meeting was found. `NO CONTINUITY-QUALIFIED H2H`.

## L. Scenario tree — Edinburgh batting innings

| Branch | PP6 state | 20-over / innings state | Contracts helped |
|---|---|---|---|
| Fast-start / normal middle | 48-60 | 150-170 | C03 strongly; C01/C02 boundary-sensitive |
| Repeat Edinburgh powerplay burst | 60-70+ | 165-185 if batting first; lower if chase ends early | C03; C01 only if full exposure survives |
| Belfast new-ball win | 30-44 with 2-3 wkts | 125-155 | C04 + C02 |
| Fast PP then spin/middle slowdown | 50-65 | 145-165 | **C03 + C02** |
| Bat-second low/moderate chase | 45-60 PP | chase completed below 166 | **C03 + C02** |
| Full 20-over ceiling state | 50+ PP, wickets preserved | 175+ | C03 + C01 |

The important coherence point is that **Powerplay Over 44.5 and Full-Innings Under 165.5 are not contradictory**. A front-loaded start followed by spin control, wickets, or chase completion supports both.

## M. Component/resource budget

### To reach 166 after PP = 45
Edinburgh would need another **121 runs in 14 overs**: 8.64 runs/over.

### To reach 166 after PP = 55
They would need **111 in 14**: 7.93 runs/over.

### To reach 166 after PP = 65
They would need **101 in 14**: 7.21 runs/over.

So a PP Over does not by itself force the full Over. It lowers the later requirement, but wickets/chase target remain decisive.

### Under 165.5 kill path
If Edinburgh bats first and reaches 55-65/0-1, their depth can absolutely carry them to 170+. That is the strongest Under failure branch.

### Over 44.5 kill path
Two early seam wickets plus dot-ball pressure can leave Edinburgh around 35-44 despite their aggressive intent. Belfast's seam depth makes this a real branch, but the threshold is still low relative to Edinburgh's two observed powerplays.

## N. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-252-C03 — Edinburgh first 6 overs Over 44.5** | **LEAN** | **MEDIUM** | Edinburgh scored 70 and 68 in its two completed ETPL powerplays. The threshold needs only 7.5 RPO and survives either innings order. Belfast's quality seam attack is the main kill path, and the tiny sample prevents stronger language. |
| **2** | **P-252-C02 — Edinburgh 20-over/innings total Under 165.5** | **LEAN** | **MEDIUM-LOW** | 165.5 is above the current conventional venue first-innings mean/median and 5/7 comparable venue first innings stayed below. If Edinburgh chases, early target completion is an additional Under/censoring path. The major failure branch is an Edinburgh bat-first 55-65 powerplay with wickets in hand. |
| **3** | **P-252-C01 — Edinburgh 20-over/innings total Over 165.5** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** | Edinburgh's top four are explosive enough to turn a 50-65 powerplay into 170+, and the batting depth is real. It ranks below Under because there is no uncensored Edinburgh 20-over sample yet, the venue centre is below the line, and a chase may terminate early. |
| **4** | **P-252-C04 — Edinburgh first 6 overs Under 44.5** | **AVOID relative to C03** | **LOW-MEDIUM** | Requires Belfast's new-ball unit to materially suppress an Edinburgh top order that has already made 70 and 68 in two powerplays. The seam-quality branch exists, but the line sits well below Edinburgh's observed powerplay level. |

## O. Rank-1 conditional coherence

Rank #1 state: Edinburgh reaches **45+ after six overs**.

- Full Under 165.5: `COHERENT / PARTIAL` — fast start can still slow, lose wickets, or be chase-censored.
- Full Over 165.5: `COHERENT / PARTIAL` — a 50-65 PP with wickets preserved creates a very credible 166+ path.
- PP Under 44.5: `DISJOINT` exact complement.

The ranking therefore does not transfer the powerplay thesis mechanically into the full-innings Over.

## P. Potential winner

### **Edinburgh Castle Rockers — SLIGHT LEAN**

Reasons:
- two completed wins and one no-result; undefeated tournament start;
- the strongest bowling performance of either side in the matchup belongs to Edinburgh's attack: Trent Boult took 5 wickets against Glasgow and Mitchell Santner took 5/16 against Dublin;
- Edinburgh have already shown two distinct successful chase shapes — an explosive 11.3-over chase and a more disrupted 13.4-over chase;
- Boult/Santner/Watt/Curran/Jarvis gives Edinburgh multiple phase-specific bowling routes against Belfast's stronger batting depth.

Counterweights:
- Belfast are also undefeated;
- Belfast have posted 184/7 and 156/9 in their two conventional first innings and possess elite batting names including Conway, Maxwell, Chapman, Stirling/Miller depending on XI;
- toss and current XI were unresolved at cutoff.

Therefore the winner call is deliberately only a **slight Edinburgh lean**, not a high-confidence prediction.

## Q. Source / provenance snapshot

Primary/current:
- ETPL official Match 11 page — identity, venue, scheduled start, pre-start "yet to bat" state.
- ETPL official team pages — Belfast and Edinburgh squad rosters.
- ETPL official match reports / home page — prior results and Edinburgh performance context.

Scorecard/detail:
- Cricbuzz / Willow / myKhel — prior innings, fall-of-wickets and exact powerplay scores.
- Cricket Ireland archive — Belfast reduced-game and official competition scorecard cross-check.

Weather:
- Buienradar Voorburg hourly forecast.
- Secondary Dutch weather cross-checks retained only as conditions corroboration.

No bookmaker odds, implied probabilities, line movement, affiliate picks, or market consensus were used directionally.

## R. Queue / append confirmation

- P-251 priority state check: DONE
- P-251 settlement/retrospective: DEFERRED — no final
- P-252 frozen before scheduled start: YES
- P-252 toss/XIs confirmed: NO — explicitly unresolved and branched
- P-252 forecast appended before delivery: YES
- Drive modified: NO
- Prior forecast rewritten: NO
- Numerical probability generated: NO
- Learning register changed: NO
- **NEXT CANONICAL ID: P-253**

---

# Settlement / retrospective sweep before P-253 — 2026-09-02

## P-249 — Hanwha Eagles @ KT Wiz — closure

### Verified final
- **Final:** KT Wiz 9, Hanwha Eagles 6.
- Multiple current result sources agree on the 9-6 final.
- P-249 had been logged `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`.
- Therefore there are **no directional contract outcomes to grade** and no winner call to score.

### Process retrospective
| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|
| Refuse live ranking unless exact live score/inning is independently verified | Final became KT 9-6 after a volatile game with Hanwha defensive errors and late bullpen damage | No sports forecast was issued, so there is no directional miss; the state-gate decision is the object being reviewed | The conflicting live-state sources were knowable before issue | **COMPLIANT** | NONE — hard gate worked as intended | Reinforces L-026/L-046 live-state integrity | **NO forecast-weight change** |

### What went right
- The card refused to treat one uncorroborated live snapshot as controlling state.
- That mattered because the exposed sources were materially inconsistent on score/inning.
- The final was a high-variance 9-6 game, confirming that a stale early-game snapshot would have been a poor basis for remaining-exposure analysis.
- No fake probability, winner call, or retrospective pick-grade was manufactured.

### What could improve
- For KBO live requests, prioritize the official Korean KBO scoreboard before secondary English mirrors.
- When the official page is temporarily stale, search Korean-language live reporting earlier in the state-verification sequence.
- This is a source-routing improvement only, not evidence for any Over/Under or side weight.

### Learning disposition
- No new forecast rule.
- Process observation only: **retain the fail-closed live-state gate**.
- No model, probability, or calibration update.

**P-249 status: CLOSED — NO ACTIONABLE FORECAST ISSUED.**

---

## Remaining incomplete local events checked

### P-250 — Yunnan Yukun vs Chongqing Tonglianglong
- Current high-quality/live sources still show the match in progress / not field-owner-final.
- Latest trustworthy state recovered during this sweep remained a live 0-0 state.
- **Settlement + retrospective deferred.**

### P-251 — Sassuolo vs Frosinone
- Current Lega Serie A sources conflict on the fixture time across official publications (15:00 versus a same-day 18:00 events listing), and no authoritative final was recovered in this sweep.
- Preserve the issued pregame card; do not rewrite it.
- **Settlement + retrospective deferred.**
- Administrative observation: schedule-source conflict must be reconciled before prospective-status grading.

### P-252 — Belfast Wolves vs Edinburgh Castle Rockers
- Current ETPL/MyKhel surfaces still did not expose a verified completed final at the sweep time.
- **Settlement + retrospective deferred.**

Older inherited operator-definition/provisional follow-ups remain open exactly as previously carried. No unknown operator term is invented.

---

# P-253 — El Gounah vs Al Mokawloon Al Arab — Egyptian Premier League 2026/27, Round 3 — PREGAME

## A. Identity and schedule hard gate

- **Canonical ID:** `P-253`
- **User wording:** `Egypt Division 1`
- **Verified competition:** **Egyptian Premier League / Premier League, Round 3**
- **Field owner:** Egyptian Professional Clubs Association
- **Event:** El Gounah vs Al Mokawloon Al Arab
- **Venue:** Khaled Bichara Stadium, El Gouna, Egypt
- **Venue class:** OUTDOOR, natural grass
- **Field-owner kickoff:** 2026-09-02 17:00 Cairo local / 14:00 UTC
- **Australia/Melbourne kickoff:** 2026-09-03 00:00 Australia/Melbourne
- **Issue-time context:** approximately five minutes before kickoff
- **GAME-STATE:** PREGAME / SCHEDULED
- **Cutoff invariant:** PASS
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-SOCCER`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator:** NOT SUPPLIED
- **Goal endpoint:** regulation 90 minutes including stoppage
- **Potential winner endpoint:** regulation match winner

## B. Candidate slate

| Contract ID | Contract | Win region | Dependence |
|---|---|---|---|
| `P-253-C01` | 1st Half Over 0.5 Goals | 1+ first-half goals | P253-1H-GOAL |
| `P-253-C02` | 1st Half Under 0.5 Goals | 0-0 at halftime | P253-1H-GOAL |
| `P-253-C03` | Full Match Over 2.5 Goals | 3+ regulation goals | P253-FT-GOAL |
| `P-253-C04` | Full Match Under 2.5 Goals | 0-2 regulation goals | P253-FT-GOAL |
| `P-253-C05` | Total Corners Over 8.5 | 9+ regulation corners under research-provider convention | P253-CORNER |

Geometry:
- C01/C02 exact complements.
- C03/C04 exact complements.
- Those four goal rows force exactly two winners in an ordinary completed regulation match.
- C05 is a separate derivative target.
- Exact operator/provider corner definition is not supplied, so C05 is definition-capped at `FORCED RANK` / `MEDIUM-LOW`.

## C. Participant / lineup gate

### El Gounah — officially published current XI
Current same-day Egyptian reporting identifies the official XI:
- GK Ahmed Masoud
- Khaled Seddik
- Mostafa Metawea
- Saber El Shimi
- Abdel Gawad Taalab
- Omar El Gazar
- Nour El Sayed
- Michael Egbemba / Michael Ayo
- Ahmed Gamal
- Ojo Samuel
- Marwan Mohsen

Current role notes:
- Marwan Mohsen remains the central striker.
- Ojo and Ahmed Gamal supply the advanced support/width.
- Wilfried Parfait Teukeu is unavailable through suspension in current Opta/FotMob coverage.

### Al Mokawloon — current source conflict
The latest recoverable sources agree on the core defensive/midfield skeleton from the opening two rounds:
- Mahmoud Abou El-Saoud in goal
- Ahmed Magdy `Kahraba`, Hassan Shakoush, Mohamed Hamed, Nader Hesham in the back line
- Omar El Wahsh / Idrissa Thiam / Doku Dodo / Islam Gaber / Mido Gaber among the principal midfield/attacking roles

But current same-day sources conflict on the final striker:
- one current headline says **Shady Hussein leads the attack**;
- another current match/broadcast preview still lists **Mohammed Sandouqa** at striker.

The complete official Al Mokawloon XI was not recovered from the competition field owner before cutoff.

**Participant consequence:** side/winner and derivative rows are capped; no unsupported player prop is selected.

## D. Current league state

### El Gounah
First two 2026/27 league matches:
1. El Gounah 1-1 Modern Sport — HT 0-0; both goals came in second-half stoppage time.
2. El Qanah 1-1 El Gounah — HT 1-1; El Qanah scored 6', El Gounah equalized 45+2'.

Season after two:
- 0 wins, 2 draws, 0 losses
- 2 GF, 2 GA
- 2 points

### Al Mokawloon
First two:
1. Tala'ea El Gaish 1-0 Al Mokawloon — HT 0-0; only goal 70'.
2. Al Mokawloon 2-3 Al Masry — HT 1-1; Mokawloon 35', Al Masry 44'.

Season after two:
- 0 wins, 0 draws, 2 losses
- 2 GF, 4 GA
- 0 points

## E. Early-season shrinkage / reference rates

Current-season sample is only four team-games combined and is aggressively shrunk.

### First-half 0.5
- El Gounah: Over in 1/2, Under in 1/2.
- Al Mokawloon: Over in 1/2, Under in 1/2.
- Combined descriptive: **2/4 Over, 2/4 Under**.

### Full match 2.5
- El Gounah: 0/2 Over 2.5; 2/2 Under 2.5.
- Al Mokawloon: 1/2 Over 2.5; 1/2 Under 2.5.
- Combined descriptive: **1/4 Over, 3/4 Under**.

These are descriptive, not probabilities.

## F. Broader L10 / prior-regime context

Current rolling source summaries:
- El Gounah last 10: roughly 1.1 scored, 1.0 conceded; 3 wins, 5 draws, 2 losses; BTTS around 70%.
- Al Mokawloon last 10: roughly 1.1 scored, 1.0 conceded; 2 wins, 6 draws, 2 losses; BTTS around 60%.

Older-season windows are prior context only. Exact definition-compatible L15/L20 event-by-event first-half and corner tables were not recoverable before kickoff and were not fabricated.

## G. Head-to-head continuity

Most recent:
- 8 May 2026: Al Mokawloon 1-0 El Gounah — goal at 82' -> **HT 0-0**, Under 2.5.
- 23 Feb 2026: El Gounah 1-1 Al Mokawloon — Mokawloon goal 19', El Gounah 73' -> **1H Over 0.5**, Under 2.5.
- 18 Aug 2024: Al Mokawloon 0-1 El Gounah — Under 2.5.
- 3 Apr 2024: El Gounah 1-2 Al Mokawloon — Over 2.5.

Last 10 listed H2Hs:
- six finished Under 2.5
- four finished Over 2.5

2026 meetings receive the strongest continuity weight.

## H. Goal-process mechanism

### El Gounah attack
- Current XI preserves Marwan Mohsen centrally with Ojo and Ahmed Gamal as support.
- El Gounah scored in both opening matches, but only one featured a first-half goal.
- The Modern Sport game stayed 0-0 until 90+4; late scoring is not backfilled into first-half evidence.
- Against El Qanah, El Gounah generated 13 shots to 6 and about 0.81 xG to 0.40 in one recovered provider.

### Al Mokawloon attack
- Opening day stayed 0-0 until 70'.
- Against Al Masry, Mokawloon scored twice but one recovered xG source credited only about 0.25 xG; the finishing outcome is aggressively shrunk rather than treated as a stable high-scoring regime.
- Current striker-source conflict widens uncertainty.

### Defensive state
- El Gounah conceded exactly once in each match.
- Mokawloon conceded four in two, but three came against an Al Masry side that generated the stronger shot/xG process.
- The central family remains 0-0 / 1-0 / 0-1 / 1-1, with 2-1 as the principal upper branch.

## I. First-half branch tree

| Branch | Representative HT | Mechanism |
|---|---|---|
| Slow central | 0-0 | cautious winless teams; Mokawloon opening-day suppression; hot conditions |
| El Gounah breakthrough | 1-0 | home width/Ojo-Marwan chain attacks uncertain Mokawloon back line |
| Mokawloon counter | 0-1 | transition/set-piece route through Mido/Dodo/Shady-or-Sandouqa |
| Open early | 1-1 | repeat of Mokawloon-Al Masry / El Qanah-El Gounah early-event state |

The current sample is exactly balanced 2/4 Over vs 2/4 Under. The Under receives only a slight structural edge from the low-event prior and conditions.

## J. Full-match 2.5 component budget

For Over 2.5:
- 2-1 either side
- 3-0 / 0-3
- 2-2+

For Under 2.5:
- 0-0
- 1-0 / 0-1
- 1-1
- 2-0 / 0-2

Why Under leads:
- 3/4 current-season combined games are Under 2.5.
- both 2026 H2Hs are Under.
- six of the last 10 listed H2Hs are Under.
- El Gounah's two league matches are both 1-1 and one stayed 0-0 until the 94th minute.
- Mokawloon's 2-3 against Al Masry appears less repeatable than a generic three-goal baseline once xG/shot quality is considered.

Strongest Under kill path:
- an early goal forces the winless trailing side to open up, creating a 2-1/1-2 state.

## K. Corner process

Direct current evidence:
- El Gounah vs Modern Sport: **11 total corners (4-7)**.
- El Qanah vs El Gounah: **5 total corners (1-4)**.
- Al Mokawloon vs Al Masry: **9 total corners** in the rolling/event source.
- Tala'ea El Gaish vs Al Mokawloon: **9 total corners** in the rolling source.
- Feb 2026 El Gounah vs Al Mokawloon: **11 total corners (6-5)**.

Small direct set: 11, 5, 9, 9, 11 -> **4/5 Over 8.5**.

Broader Mokawloon rolling corner source:
- 5.3 corners for
- 5.3 conceded
- 10.5 total-match baseline
- about 5.0 corners won away

Mechanism:
- El Gounah's Ojo/Ahmed Gamal width can generate end-line/blocked-cross events.
- Mokawloon trailing state can raise crossing/corner exposure.
- Low goals do not mechanically imply low corners; the Feb H2H finished 1-1 with 11 corners.

Kill path:
- slow central possession with few blocked crosses/deflections, like the five-corner El Qanah-El Gounah match.

Exact operator/provider corner definition is absent, so C05 remains `FORCED RANK`.

## L. Environment

- Khaled Bichara Stadium / El Gouna area.
- Current nearby conditions: clear and very hot.
- Match-window temperature around **33-36°C**.
- El Gouna afternoon wind forecast around **16-18 knots** from northerly/north-northeasterly directions in one local forecast lane, with gusts around **18-20 knots**.
- Precipitation essentially **0%**.
- Nearby airport dew point around the mid-teens °C.

Mechanistic treatment:
- heat/wind can reduce sustained pressing and alter crossing/long-ball quality, but there is no fitted coefficient.
- conditions modestly strengthen the slow-tempo branch without mechanically determining an Under.
- no abnormal pitch report was recovered.

## M. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-253-C04 — Full Match Under 2.5 Goals** | **LEAN** | **MEDIUM** | Best-aligned with 3/4 current combined league games, both 2026 H2Hs, six of the last 10 listed H2Hs, and El Gounah's two 1-1 starts. |
| **2** | **P-253-C05 — Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | Direct recent/H2H sample is 4/5 over 8.5 and Mokawloon's rolling baseline is about 10.5 total corners. Provider definition missing. |
| **3** | **P-253-C02 — 1st Half Under 0.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | Current 1H sample is only 2/4 Under; edge comes from the low-event prior, May H2H 0-0 HT, Mokawloon opening 0-0 HT and hot conditions. |
| **4** | **P-253-C01 — 1st Half Over 0.5 Goals** | **LEAN-ADJACENT / FORCED RANK** | **MEDIUM-LOW** | Two of four current games and the February H2H produced a first-half goal. It is genuinely close to C02. |
| **5** | **P-253-C03 — Full Match Over 2.5 Goals** | **AVOID relative to C04** | **LOW-MEDIUM** | Needs the game to escape the dominant 0-0/1-0/1-1/2-0 families; credible mainly through an early goal plus Mokawloon defensive instability. |

## N. Rank-1 conditional coherence

Rank #1 state: match finishes with **0-2 regulation goals**.

- C05 Corners Over 8.5: `COHERENT / PARTIAL`.
- C02 1H Under 0.5: `COHERENT`.
- C01 1H Over 0.5: `PARTIAL_OVERLAP` because 1-0, 2-0 and 1-1 remain Under 2.5.
- C03 Full Over 2.5: `DISJOINT` exact complement.

No cross-row contradiction requires repair.

## O. Potential winner

### **El Gounah — SLIGHT LEAN (90-minute winner)**

Supporting factors:
- home venue;
- unbeaten after two rounds versus Mokawloon's 0 points;
- El Gounah scored in both matches;
- Mokawloon conceded four in two;
- El Gounah's current official XI is resolved while Mokawloon's final attacking XI had a source conflict.

Counterweights:
- both 2026 H2Hs were close: 1-1 and a 1-0 Mokawloon win;
- El Gounah are also winless;
- low-total matches amplify draw probability;
- Mokawloon retain transition/set-piece routes.

This is a **slight El Gounah winner lean**, with **draw as the strongest alternative**.

## P. Final delivery

1. **Full Match Under 2.5 Goals**
2. **Total Corners Over 8.5**
3. **1st Half Under 0.5 Goals**
4. **1st Half Over 0.5 Goals**
5. **Full Match Over 2.5 Goals**

**Potential winner:** El Gounah — slight 90-minute lean.

## Q. Append confirmation

- All currently incomplete local events state-checked before P-253: YES
- Newly completed P-249 settled/reviewed first: YES
- P-250/P-251/P-252 still unresolved and preserved open: YES
- P-253 competition corrected from user label to field-owner Premier League Round 3: YES
- P-253 frozen before kickoff: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probabilities generated: NO
- Learning register changed: NO new forecast rule
- **NEXT CANONICAL ID: P-254**


---

# Settlement / retrospective sweep before P-254 — 2026-09-03

## P-250 — Yunnan Yukun vs Chongqing Tonglianglong — FINAL

**Verified final:** Yunnan Yukun 1-0 Chongqing Tonglianglong; **HT 0-0**. Yunnan advanced.

| ID | Original rank | Contract | Result |
|---|---:|---|---|
| P-250-C01 | 1 | 1H Over 0.5 | **LOSS** |
| P-250-C02 | 5 | 1H Under 0.5 | **WIN** |
| P-250-C03 | 3 | Full Over 2.5 | **LOSS** |
| P-250-C04 | 4 | Full Under 2.5 | **WIN** |
| P-250-C05 | 2 | Corners Over 8.5 | **UNRESOLVED** — no trustworthy current provider final |

**Potential winner — Yunnan to advance:** **WIN**.

### Deep Rank-1 retrospective
Rank #1 (1H Over 0.5) lost. The card correctly named a 0-0 HT as the strongest kill path, but the broad recent first-half-goal frequency was allowed to outweigh the more matchup-specific low-event evidence: the current-season H2H had been 0-0 at HT/full time, Chongqing's recent regime was low-event, and knockout caution was knowable. The first-half rank therefore receives **PROCESS_DEFECT — early-goal/opponent-conditioning**.

What was right:
- Yunnan advancement direction won.
- Full Under 2.5 remained a clearly represented branch and won.
- The losing Rank-1 mechanism was predeclared rather than invented after the result.

What improves:
- first-half goal outcomes must be supported by opponent-conditioned first-half *creation* (shots/xG/entries), not just historical goal occurrence;
- a continuity-qualified 0-0 H2H plus current low-event opponent cannot be described as the main kill path and then functionally underweighted.

**Learning disposition:** reinforces existing `RULES_SOCCER` early-goal reconciliation control; **no new forecast weight**.

---

## P-251 — Sassuolo vs Frosinone — FINAL

**90 minutes:** 1-1. **HT:** 1-1. Sassuolo advanced on penalties.

| ID | Original rank | Contract | Result |
|---|---:|---|---|
| P-251-C01 | 1 | 1H Over 0.5 | **WIN** |
| P-251-C03 | 2 | Full Over 2.5 | **LOSS** |
| P-251-C05 | 3 | Corners Over 8.5 | **PROVISIONAL WIN — threshold invariant**; current feeds expose 10-11 corners |
| P-251-C04 | 4 | Full Under 2.5 | **WIN** |
| P-251-C02 | 5 | 1H Under 0.5 | **LOSS** |

**Potential winner — Sassuolo to advance:** **WIN**.

### Retrospective
Rank #1 won for the stated early-attacking reason: both teams scored before halftime. Rank #2 Full Over 2.5 failed because the two first-half goals did **not** propagate into a third regulation goal despite attacking substitutions. This is a **COMPLIANT forecast with calibration/phase-propagation caution**, not a new rule. It reinforces the existing control that an early goal changes the later state but does not mechanically imply a full-match Over.

Corner raw counts conflict (10 vs 11), but every credible retrieved value is above 8.5. Preserve the raw conflict and retain **PROVISIONAL WIN** because the user's exact operator/provider definition was never supplied.

---

## P-252 — Belfast Wolves vs Edinburgh Castle Rockers — OPEN

ETPL's current field-owner page still lists Match 11 as **UPCOMING / yet to bat** with no completed score, despite the scheduled start having passed. Treat this as a source-state defect, not a final.

**Settlement/retrospective deferred.**

## P-253 — El Gounah vs Al Mokawloon — OPEN

The Egyptian Professional Clubs Association still exposes the Round 3 fixture as `VS`, without a field-owner final. No sufficiently trustworthy final was recovered.

**Settlement/retrospective deferred.**

---

# P-254 — Jan Choinski vs Botic Van de Zandschulp — 2026 US Open Men's Singles R1 — PREGAME

## A. Identity / state / contract freeze
- **Canonical ID:** P-254
- **Round:** R128 / Round 1
- **Surface:** outdoor hard
- **Format:** best of five sets
- **Court:** Court 5 on the current order of play
- **Scheduled:** 2026-09-02 16:30 UTC / 12:30 EDT / 2026-09-03 02:30 Australia/Melbourne
- **State at cutoff:** NOT STARTED
- Sep 1 outdoor play was disrupted by rain, explaining the delayed first-round slot.
- **Method:** MDS-2026.09.02-v3.1 / GFA-2 / SFA-TENNIS
- **Operator retirement terms:** NOT SUPPLIED -> `UNKNOWN_DEFINITION`
- **Probability:** NOT_GENERATED / NOT PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Forecast lane:** SPORTS_ONLY / MARKET_BLIND

| ID | Contract | Ordinary win region |
|---|---|---|
| P-254-C01 | Choinski +5.5 games | Choinski win or loss by <=5 net games |
| P-254-C02 | Van de Zandschulp -5.5 games | Botic win by >=6 net games |
| P-254-C03 | Over 38.5 games | 39+ |
| P-254-C04 | Under 38.5 games | <=38 |

C01/C02 and C03/C04 are exact complementary pairs under ordinary completed-match terms. Exactly two of four rows win in a normal completed match; that is contract geometry, not model accuracy.

## B. Current hard-court regime

### Van de Zandschulp
Current hard-source record: **12-8 in 2026**, **6-4 L10**. Recent hard results include:
- W Darderi 6-1, 6-0
- W Vallejo 6-2, 6-0
- W Shevchenko 6-4, 6-4
- W Hurkacz 3-6, 7-6, 7-5
- W Medvedev 6-3, 7-6
- W Mpetshi Perricard 6-2, 3-6, 6-3
- L Bonzi 7-6, 6-4
- L Fonseca 6-4, 7-6

Mechanism: Botic's current ATP-level hard sample shows both reliable service holds and enough return pressure to create multi-break separation. His dominant wins over Darderi and Vallejo are directly relevant to the -5.5 tail.

### Choinski
Latest high-level hard results:
- L Rottgering 5-7, 6-2, 4-6
- L Taro Daniel 4-6, 3-6
- L Tirante 6-7, 7-6, 6-7

Mechanism: Choinski's serve is the stronger part of his hard profile. The three-tiebreak Cincinnati loss is direct evidence of margin resistance, but his current return/ATP-level results are less convincing than Botic's.

Level adjustment:
- Choinski's strongest 2026 title runs were largely Challenger clay.
- Botic's strongest recent evidence is ATP hard.
- Challenger clay success is not treated as exchangeable with US Open hard.

## C. H2H continuity
Clean current H2H source:
- 2025 Braunschweig Challenger, clay: Botic won 6-1, 6-0
- 2018 Scheveningen Challenger, clay: Botic won 7-5, 6-2

**H2H = Botic 2-0**, but both matches were clay, BO3 Challenger-level, and one is eight years old. Therefore **LOW continuity / diagnostic only**. Conflicting third-party H2H records are not used.

## D. Recency / BO5 context
- Botic: L5 hard 3-2; L10 hard 6-4; broader 2026 hard 12-8.
- Choinski: recent high-level hard sequence is 0-3, though two losses were margin-resistant.
- Exact definition-compatible L15/L20 hard tables for both players were not fully recoverable before issue and are not imputed.
- Current official US Open men's R1 event stats: 52 matches -> 22 three-set, 16 four-set, 13 five-set, 1 retirement; 27 tiebreaks. This is contextual only.

**Qualitative set-count weight index, not probabilities:**
- 3 sets = 3
- 4 sets = 2
- 5 sets = 1

The central tree therefore prefers Botic control in three or efficient four sets, while preserving Choinski tiebreak/extension branches.

## E. Environment
Outdoor hard; Fresh Meadows forecast is mostly cloudy around 24°C with E/NE wind near 9 mph and only a modest shower chance until later afternoon. Rain affected the previous day's outer courts, but there is no basis for an automatic weather direction now. No court-speed coefficient is invented.

## F. Match tree / separation budget

**Central Rank-1 scoreline:** Botic **6-3, 6-4, 6-4**
- Botic game margin +7 -> -5.5 covers
- total 29 -> Under 38.5 wins

**Efficient 3-1:** Botic **6-3, 6-4, 4-6, 6-3**
- margin +6 -> -5.5 covers
- total 38 -> Under 38.5 wins

**Main kill path:** close/tiebreak-heavy Botic win, e.g. 7-6, 6-4, 4-6, 7-6
- Choinski +5.5 becomes much stronger
- Over 38.5 becomes much stronger

**Choinski upset path:** high first-serve day plus Botic second-serve/forehand-error volatility -> Choinski wins 3-1/3-2, automatically defeating Botic -5.5 and usually supporting +5.5/Over.

### Handicap budget
Botic -5.5 needs actual break separation:
- 6-4, 6-4, 6-4 = +6, cover
- 7-6, 7-6, 6-4 = +4, no cover
- 4/5-set extension usually helps Choinski +5.5 unless Botic owns one lopsided set.

### Total budget
Under 38.5 is strongest in:
- ordinary Botic 3-0
- efficient Botic 3-1

Over 38.5 is strongest in:
- tiebreak-heavy 3-set extremes (three 7-6 sets = 39)
- close four-set matches
- most ordinary five-set matches

Thus the shared latent variable is **Choinski hold resistance**:
- if high -> Choinski +5.5 + Over rise together
- if Botic breaks repeatedly -> Botic -5.5 + Under rise together.

## G. Ranked forecast

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Van de Zandschulp -5.5 Games** | **LEAN** | **MEDIUM** |
| **2** | **Under 38.5 Total Games** | **SLIGHT LEAN** | **MEDIUM-LOW** |
| **3** | **Choinski +5.5 Games** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** |
| **4** | **Over 38.5 Total Games** | **FORCED RANK / weaker total direction** | **MEDIUM-LOW** |

### Rank-1 coherence
Rank #1 is Botic -5.5.
- Under 38.5: **COHERENT** with the central 3-0/efficient 3-1 cover states.
- Choinski +5.5: **DISJOINT**, exact complement.
- Over 38.5: **PARTIAL/TAIL**; its strongest close-match states usually compress Botic's margin.

## H. Potential winner
**Botic Van de Zandschulp — LEAN**

Reason: stronger current ATP hard serve/return regime, better opponent-quality wins, and demonstrated separation ceiling. Rankings are close and are not the decisive input.

## I. Final order
1. Van de Zandschulp -5.5 Games
2. Under 38.5 Games
3. Choinski +5.5 Games
4. Over 38.5 Games

**Potential winner:** Botic Van de Zandschulp.

## J. Append confirmation
- All incomplete local events rechecked: YES
- P-250 newly settled/retrospected: YES
- P-251 newly settled/retrospected: YES
- P-252/P-253 preserved open: YES
- P-254 frozen pre-start: YES
- Drive modified: NO
- Numerical probability generated: NO
- New forecast-weight rule: NO
- **NEXT CANONICAL ID: P-255**


---

# Queue state check before P-255 — 2026-09-03

## P-250-C05 — Yunnan Yukun vs Chongqing Tonglianglong corners
- Still **UNRESOLVED**.
- No trustworthy current field-owner/provider corner final recovered.
- No retrospective change.

## P-251-C05 — Sassuolo vs Frosinone corners
- Remains **PROVISIONAL WIN / threshold-invariant**.
- Retrieved raw counts still conflict but all credible counts remain above 8.5.
- Exact original operator/provider definition was never supplied.

## P-252 — Belfast Wolves vs Edinburgh Castle Rockers
- ETPL field-owner page still exposes Match 11 as `Yet to bat / no ball-by-ball`.
- Scheduled start has long passed; this is treated as a source-state defect.
- **No final / no settlement / no retrospective.**

## P-253 — El Gounah vs Al Mokawloon
- No field-owner final recovered.
- **No settlement / no retrospective.**

## P-254 — Jan Choinski vs Botic Van de Zandschulp
- Current US Open/Tennis.com/TNT surfaces still show the match not started/upcoming.
- Scheduled around 12:30 EDT / 02:30 Australia-Melbourne.
- **Leave open.**

No unknown operator definition is invented. No completed retrospective is skipped.

---

# P-255 — Inter Women vs VfL Wolfsburg Women — UEFA Women's Champions League 2026/27 Third Qualifying Round, Second Leg — PREGAME

## A. Identity and tie state

- **Canonical ID:** `P-255`
- **Sport:** Soccer
- **Competition:** UEFA Women's Champions League 2026/27
- **Stage:** Third qualifying round, second leg
- **Event:** Inter Women vs VfL Wolfsburg Women
- **Venue:** Stadio Ernesto Breda, Sesto San Giovanni, Italy
- **Scheduled kickoff:** 2026-09-02 18:30 CEST
- **Australia/Melbourne kickoff:** 2026-09-03 02:30 AEST
- **Frozen cutoff:** 2026-09-03 approximately 02:23 AEST / 18:23 CEST
- **GAME-STATE:** PREGAME / SCHEDULED
- **Aggregate before kickoff:** Wolfsburg lead **2-0**
- **First leg:** Wolfsburg 2-0 Inter
- **First-leg HT:** Wolfsburg 1-0 Inter
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-SOCCER`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator:** NOT SUPPLIED
- **Goal rows:** regulation 90 minutes including stoppage
- **Potential winner endpoint:** **TO ADVANCE TO THE LEAGUE PHASE**, not the same as the 90-minute match winner

## B. Candidate slate

| ID | Contract | Settlement region | Dependence |
|---|---|---|---|
| `P-255-C01` | 1st Half Over 0.5 Goals | 1+ first-half goals | P255-1H |
| `P-255-C02` | 1st Half Under 0.5 Goals | 0-0 at HT | P255-1H |
| `P-255-C03` | Full Match Over 2.5 Goals | 3+ regulation goals | P255-FT |
| `P-255-C04` | Full Match Under 2.5 Goals | 0-2 regulation goals | P255-FT |
| `P-255-C05` | Total Corners Over 8.5 | 9+ regulation corners under research-provider convention | P255-CORNER |

- C01/C02 exact complements.
- C03/C04 exact complements.
- C05 is a separate corner process.
- Exact operator/provider corner semantics were not supplied, so C05 is capped at `FORCED RANK / MEDIUM-LOW`.

## C. First-leg mechanism

Official/club first-leg evidence:
- Wolfsburg won 2-0.
- Prašnikar scored at 42'.
- Küver scored at 52' from a Peddemors corner.
- Inter's Robustellini was sent off at 49'.
- Wolfsburg were described by the club as controlling proceedings, especially after the red.
- Independent match statistics: Wolfsburg 25 shots to Inter 7; shots on target 11-2; corners 8-2.
- Inter still created dangerous first-half chances before the dismissal.

Interpretation:
- the first-leg 2-0 is not imported as a static return-leg expectation;
- the second leg begins in a **different tactical state** because Inter are already two goals behind on aggregate from minute 0;
- the red-card-distorted second half of leg one is not treated as ordinary 11-v-11 evidence.

## D. Participant / availability gate

The current Wolfsburg field-owner matchcenter had still not exposed the official second-leg XI at the frozen cutoff, despite listing both squads.

Latest reliable Wolfsburg team news:
- Lena Lattwein
- Cecilie Floe Nielsen
- Giovanna Hoffmann

were still unavailable for the Aug. 30 league match after also missing the first leg.

Inter participant notes:
- Chiara Robustellini received a straight red in the first leg, so the back-line structure necessarily requires disciplinary/selection reconciliation.
- Current indexed field-owner surfaces did not expose a trustworthy full second-leg XI before cutoff.
- A third-party page showing the **first-leg lineup again**, including Robustellini, was quarantined as stale and not used as the second-leg XI.

**Participant consequence:** side/advance and derivative evidence are capped; no player prop is selected.

## E. Current competitive form

### Inter Women — current competitive matches
1. Parma 0-1 Inter — HT 0-0
2. Wolfsburg 2-0 Inter — HT 1-0
3. Inter 6-0 Napoli — HT 4-0

Current competitive descriptive:
- 1H Over 0.5: **2/3**
- Full Over 2.5: **1/3**

Broader recent six including current pre-season:
- 1H goal in approximately **5/6**
- recent scores: 6-0, 0-2, 1-0, 2-0, 1-0, 4-1

### Wolfsburg Women — current competitive matches
1. Nürnberg 2-8 Wolfsburg — HT 2-0
2. Wolfsburg 2-0 Inter — HT 1-0
3. Leverkusen 1-2 Wolfsburg — HT 0-1

Current competitive descriptive:
- 1H Over 0.5: **3/3**
- Full Over 2.5: **2/3**

Broader recent:
- first-half goals have been frequent across league, Supercup/friendly and UWCL samples;
- current scoring ceiling remains high, but the Nürnberg 8-2 second half was heavily influenced by a dismissal and is not used as a normal baseline.

Combined current competitive descriptive:
- 1H Over 0.5 = **5/6**
- Full Over 2.5 = **3/6**

Small sample; diagnostic only.

## F. Two-leg regime switch

### Branch 1 — no early goal
- Wolfsburg can protect the 2-0 aggregate advantage.
- Inter attack demand rises with time, but Wolfsburg do not need to chase.
- Supports lower regulation total initially, while late corner pressure can still rise.

### Branch 2 — early Inter goal
- Aggregate becomes 2-1.
- Tie becomes materially live.
- Inter keep pressing; Wolfsburg gain counter space.
- Strongly supports 1H Over, later goals and corners.

### Branch 3 — early Wolfsburg goal
- Aggregate becomes 3-0.
- Inter now require three to draw level.
- Inter are forced into a very aggressive chase.
- Strongly supports later transition chances and corner volume.

### Branch 4 — dismissal/injury
- Must be rebuilt asymmetrically.
- First-leg red-card effects are not assumed to repeat.

This aggregate-state structure is more important than copying ordinary home/away totals.

## G. Early-goal reconciliation

Evidence supporting 1H Over 0.5:
- current competitive combined = 5/6
- first leg itself had a first-half goal
- Inter just scored four first-half goals against Napoli
- Wolfsburg's first two league matches and first leg all contained first-half scoring
- Inter must attack from kickoff because they trail 0-2 on aggregate

Counter-paths:
- Wolfsburg can begin conservatively and prioritize shape
- first-leg breakthrough did not arrive until 42'
- exact second-leg XIs were not field-owner-confirmed at cutoff

Result: early-goal Over remains the strongest goal direction, but evidence is capped at MEDIUM.

## H. Full-total component budget

Over 2.5 wins through:
- 2-1
- 1-2
- 3-0 / 0-3
- 2-2+

Under 2.5 wins through:
- 0-0
- 1-0 / 0-1
- 1-1
- 2-0 / 0-2

Central competing families:
- **1-1 / 1-2 Wolfsburg / 2-1 Inter**

The aggregate deficit specifically raises the right tail:
- if Inter score, chase remains active;
- if Wolfsburg score, Inter's chase becomes even more extreme.

The main Under path is Wolfsburg successfully slowing the match and denying Inter an early goal.

## I. Corner process

Direct first-leg:
- Wolfsburg 8 corners
- Inter 2
- total 10

Recent Inter corner process from the retrieved provider:
- Parma: 4 Inter corners
- Newcastle: 5
- Union Berlin: 4
- Grasshopper: 9
- first leg vs Wolfsburg: 2

The first-leg 2-corner output occurred in a match where Inter were reduced to ten shortly after halftime and then spent long periods defending.

Second-leg mechanism:
- Inter start already two goals behind on aggregate.
- Their required attacking exposure is materially higher from kickoff.
- If Inter trail further, crosses/end-line entries/set plays should rise.
- If Inter score early, Wolfsburg may counter more often, preserving two-sided corner generation.
- Wolfsburg themselves generated 8 corners in leg one and 11 in the 8-2 Nürnberg match.

Kill path:
- Inter create centrally rather than through blocked/cross actions;
- Wolfsburg protect territory effectively and the match produces goals from few corner-causing events.

Because the exact sportsbook/provider definition is absent, C05 remains a research-defined ranking row only.

## J. Environment

Sesto San Giovanni / Milan match-window forecast:
- approximately 30-31°C near kickoff
- dry / near-zero precipitation
- light wind around 5-9 km/h
- no abnormal surface report recovered

Mechanistic use:
- heat can increase late fatigue/substitution effects;
- dry light-wind conditions do not create a material suppression signal;
- no deterministic Over adjustment is assigned.

## K. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-255-C01 — 1st Half Over 0.5 Goals** | **LEAN** | **MEDIUM** | Aggregate state forces Inter to chase from minute 1; current competitive sample is 5/6 with a first-half goal and the first leg also had one. Wolfsburg's control-first branch is the main counter. |
| **2** | **P-255-C05 — Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | First leg produced 10 corners; Inter's second-leg chasing exposure is structurally higher, and either early-goal direction can raise crossing/set-piece demand. Exact provider definition is missing. |
| **3** | **P-255-C03 — Full Match Over 2.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | Two-leg regime switch raises the open-game tail: early Inter goal makes the tie live; early Wolfsburg goal forces an even larger Inter chase. Current competitive raw total sample is only 3/6 Over, so this remains below Rank #1. |
| **4** | **P-255-C04 — Full Match Under 2.5 Goals** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** | Wolfsburg can protect a 2-0 aggregate cushion and the first leg itself finished with only two goals. 0-0, 1-0, 1-1 and 2-0 remain credible if Inter fail to score early. |
| **5** | **P-255-C02 — 1st Half Under 0.5 Goals** | **AVOID RELATIVE TO C01** | **LOW-MEDIUM** | Requires 0-0 HT despite Inter's immediate aggregate chase and a current 5/6 competitive early-goal combined sample. Its strongest route is Wolfsburg successfully slowing the first phase. |

## L. Rank-1 coherence

Rank #1 = 1H Over 0.5.

- Corners Over 8.5: `COHERENT / PARTIAL` — early goal changes chase intensity and can add width/set pieces.
- Full Over 2.5: `COHERENT / PARTIAL` — early goal materially raises three-goal states.
- Full Under 2.5: `PARTIAL_OVERLAP` — 1-0, 2-0 or 1-1 still win Under after an early goal.
- 1H Under 0.5: `DISJOINT` exact complement.

No high-ranked row is structurally impossible under Rank #1.

## M. Potential winner / qualification endpoint

### **VfL Wolfsburg to advance — SUPPORTED qualitative direction**

This is intentionally an **advance** call, not a regulation-moneyline call.

Why:
- Wolfsburg begin 2-0 ahead on aggregate.
- They controlled much of the first leg and produced a large shot/corner advantage.
- Inter must score at least twice without net concession merely to force extra time.
- Wolfsburg's current league form is strong: 8-2 at Nürnberg, 2-1 at Leverkusen.
- Their transition threat becomes more dangerous as Inter chase.

### Regulation-result note
A 90-minute Wolfsburg win is only a **slight lean**, because they do not need to win the second leg and can qualify through a draw or narrow defeat.

## N. Final delivery

1. **1st Half Over 0.5 Goals**
2. **Total Corners Over 8.5**
3. **Full Match Over 2.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential winner endpoint:** VfL Wolfsburg **to advance**.

## O. Append confirmation

- All current incomplete local events rechecked: YES
- Newly final item requiring retrospective: NO
- P-252/P-253/P-254 remain open/unverified: YES
- P-250-C05 unresolved and P-251-C05 provisional preserved: YES
- P-255 frozen pre-start: YES
- Exact second-leg XI unavailable from indexed field-owner surface: YES / uncertainty preserved
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-256**


---

# Queue state check before P-256 — 2026-09-03

## Open / unresolved local items
- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED** — no trustworthy current provider final.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**; raw provider counts still conflict but remain above 8.5.
- `P-252` Belfast Wolves–Edinburgh Castle Rockers: **OPEN / FIELD-OWNER STATE DEFECT**; ETPL still exposes the match as upcoming/yet-to-bat after scheduled start.
- `P-253` El Gounah–Al Mokawloon: **OPEN / FINAL NOT VERIFIED**.
- `P-254` Choinski–Van de Zandschulp: **OPEN / UPCOMING-NOT STARTED** at the queue sweep.
- `P-255` Inter Women–Wolfsburg Women: **OPEN / PREGAME** at the queue sweep; scheduled for 18:30 CEST / 02:30 Melbourne.

No newly final local event was safe to settle. No retrospective was fabricated. Older inherited provisional/operator-definition items remain unchanged.

---

# P-256 — Paris Saint-Germain Women vs Eintracht Frankfurt Women — UEFA Women's Champions League 2026/27 Third Qualifying Round, Second Leg — PREGAME

## A. Frozen identity and tie state
- **Canonical ID:** `P-256`
- **Competition:** UEFA Women's Champions League 2026/27
- **Stage:** Third qualifying round, second leg
- **Event:** Paris Saint-Germain Women vs Eintracht Frankfurt Women
- **Venue:** PSG Campus, Poissy, France
- **Kickoff:** 2026-09-02 18:30 CEST / 2026-09-03 02:30 Australia/Melbourne
- **State at cutoff:** PREGAME / SCHEDULED
- **Aggregate before kickoff:** **1-1**
- **First leg:** Eintracht Frankfurt 1-1 PSG
- **First-leg HT:** 1-1
- **First-leg goals:** Mühlhaus 4', Feller 7'
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-SOCCER`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator:** NOT SUPPLIED
- **Goal endpoint:** regulation 90 minutes including stoppage
- **Potential winner endpoint:** **TO ADVANCE TO THE LEAGUE PHASE**
- If tied after 90 minutes, current Eintracht preview states extra time and then penalties decide the tie.

## B. Candidate slate

| ID | Contract | Settlement region | Dependence |
|---|---|---|---|
| `P-256-C01` | 1st Half Over 0.5 Goals | 1+ first-half goals | P256-1H |
| `P-256-C02` | 1st Half Under 0.5 Goals | 0-0 at halftime | P256-1H |
| `P-256-C03` | Full Match Over 2.5 Goals | 3+ regulation goals | P256-FT |
| `P-256-C04` | Full Match Under 2.5 Goals | 0-2 regulation goals | P256-FT |
| `P-256-C05` | Total Corners Over 8.5 | 9+ regulation corners under the research-provider convention | P256-CORNER |

- C01/C02 are exact complements.
- C03/C04 are exact complements.
- C05 is a separate corner process.
- Exact operator/provider corner semantics were not supplied, so C05 is capped at `FORCED RANK / MEDIUM-LOW` even if it ranks first by sporting likelihood.

## C. Participant / availability gate

### UEFA current squad status
UEFA's match page exposes current official squad lists but had not yet exposed the confirmed starting XIs at the frozen cutoff.

### PSG available attacking core
Current UEFA squad includes:
- Naomie Feller
- Romée Leuchter
- Merveille Kanjinga
- Rasheedat Ajibade
- Sakina Karchaoui
- Jennifer Echegini
- Jackie Groenen
- Vitória Yaya

First-leg PSG starters included:
Kiedrzynek; Chagas, De Almeida, Dudek, Elimbi; Echegini, Ebayilin; Feller, Karchaoui; Kanjinga, Leuchter.

### Frankfurt current squad / team news
Current UEFA squad includes:
- Laura Freigang
- Larissa Mühlhaus
- Hayley Raso
- Rebecka Blomqvist
- Danique Tolhoek
- Erëleta Memeti
- Hanna Bennison
- Amanda Ilestedt / Sara Doorsoun defensive options

Current Eintracht preview explicitly states goalkeeper **Sophia Winkler remains unavailable**.

The first-leg XI and current league rotation show meaningful attacking depth, but exact second-leg starter/minutes allocation was not confirmed before cutoff.

**Participant consequence:** no player prop is selected, and side/total confidence is capped below high confidence.

## D. First-leg mechanism

Official Frankfurt report:
- Frankfurt's high press forced an early PSG turnover.
- Larissa Mühlhaus scored at **4'**.
- PSG responded almost immediately through Naomie Feller at **7'**.
- The match then stayed 1-1.
- Frankfurt had a major second-half chance when Hanna Bennison struck both posts in the same sequence.
- Frankfurt described the tie as remaining open.

Independent match stats:
- possession: Frankfurt 56%, PSG 44%
- shots: Frankfurt 7, PSG 2
- shots on target: Frankfurt 4, PSG 1
- corners: **Frankfurt 10, PSG 5**
- total corners: **15**

Interpretation:
- the first-leg early-goal state was real, not a late-score artifact;
- Frankfurt generated the larger second-half pressure despite failing to score again;
- PSG proved capable of immediately punishing the high press;
- the second leg begins level, so neither team has an aggregate cushion to protect.

## E. Aggregate-state tree

### Branch 1 — no early goal
- Tie remains 1-1 aggregate.
- Neither side is forced into an immediate desperation chase.
- The match can remain tactical through the first hour.
- Supports Full Under 2.5 more than in an aggregate-deficit tie.

### Branch 2 — early PSG goal
- PSG lead aggregate 2-1.
- Frankfurt must raise attack/width and set-piece exposure.
- Supports corners and raises the late Over tail.

### Branch 3 — early Frankfurt goal
- Frankfurt lead aggregate 2-1.
- PSG must chase at home.
- Supports PSG territory/corners and raises transition chances.

### Branch 4 — level after 90
- Extra time remains possible.
- User's 90-minute total and first-half rows are settled before extra time.
- Potential winner-to-advance endpoint continues through ET/penalties.

This tied-aggregate structure is less inherently Over-biased than P-255 Inter–Wolfsburg because no side starts behind.

## F. Current goal form

### Frankfurt current competitive run
- Frankfurt 8-0 Omonia
- Frankfurt 2-0 Malmö
- Frankfurt 2-0 Köln
- Frankfurt 1-1 PSG
- Frankfurt 1-1 Nürnberg

Recent competitive totals:
- Over 2.5: **1/5**
- Under 2.5: **4/5**

First-half evidence:
- Köln 2-0 HT
- PSG 1-1 HT
- Nürnberg 0-1 HT
- current UWCL qualifying samples also contain early goals in the Omonia/Malmö wins
- Frankfurt's current attacking phases are often strongest before halftime even when the final total remains low.

### PSG current recent run
PSG domestic league had not yet begun; the current usable regime is first-leg plus friendlies:
- Saint-Malo 1-1 PSG
- Brighton 1-1 PSG
- PSG 1-3 Union Berlin
- PSG 4-0 Valencia
- Frankfurt 1-1 PSG

Known first-half states:
- Brighton 0-1 PSG
- PSG 1-2 Union Berlin
- PSG 2-0 Valencia
- Frankfurt 1-1 PSG

This makes PSG's current early-goal exposure materially stronger than its full-match 2.5 direction.

### Combined interpretation
- **1H goal:** strong current signal.
- **Full Over 2.5:** mixed.
- Frankfurt's process is particularly important: repeated first-half goals followed by low-scoring second halves create a natural `1H Over + Full Under` branch.

## G. L5 / L10 / broader-window handling

Current exact L5:
- Frankfurt: available and directly reconstructed.
- PSG: current first-team sample spans one competitive match plus friendlies; friendly phase is kept separate.

Broader current corner source:
- PSG last 10 tracked matches: about **10.8 average total corners**, with 70% above 9.5 in the provider's current window.
- Frankfurt latest five tracked corner totals: **11, 15, 9, 11, 8**.

Exact definition-compatible L15/L20 current-regime event tables were not fully reconstructable before kickoff. Older-season results remain prior context only.

No missing window is fabricated.

## H. Corner process

This is the strongest target-specific evidence.

### First leg
- Frankfurt corners: **10**
- PSG corners: **5**
- total: **15**

### Frankfurt latest five tracked totals
- vs Nürnberg: 11
- vs PSG: 15
- vs Köln: 9
- vs Malmö: 11
- vs Strasbourg: 8

**4/5 exceeded 8.5.**

Frankfurt's current tracked recent form also shows approximately:
- 7 corners for per match
- 3.8 against per match

### PSG recent tracked totals
Available recent records:
- vs Frankfurt: 15
- vs Valencia: 15
- vs Brighton: 7
- vs Paris FC: 13
- vs Lyon: 11

**4/5 exceeded 8.5.**

PSG broader tracked average: approximately **10.8 total corners** over the latest 10-provider window.

### Mechanistic branch
- tied aggregate means both sides need an eventual winner;
- first goal by either side raises the trailing team's crossing/end-line/set-piece exposure;
- Frankfurt demonstrated extremely high corner generation in leg one;
- PSG's current wide/advanced personnel — Feller, Karchaoui, Leuchter/Kanjinga/Ajibade options — preserve flank pressure;
- even a low-scoring regulation game can clear 8.5 corners.

### Kill path
- long central-possession spells;
- few blocked crosses;
- efficient finishing before sustained territorial pressure develops.

### Definition cap
Operator/provider definition absent -> row may rank #1 but cannot be labelled `LEAN/SUPPORTED`.

## I. First-half goal audit

Evidence supporting Over 0.5:
- first leg produced goals at 4' and 7';
- Frankfurt's latest league games vs Köln and Nürnberg both had first-half goals;
- PSG's recent known halftime states vs Brighton, Union, Valencia and Frankfurt all contained a goal;
- first-leg pressing/transition mechanism remains relevant.

Counter-path:
- second-leg aggregate is level and neither team needs to force the game in the first 20 minutes;
- both may be more cautious after the chaotic seven-minute opening in Frankfurt;
- confirmed second-leg XI was unavailable at cutoff.

Result: Over 0.5 still leads the first-half pair.

## J. Full-match 2.5 budget

### Under 2.5 central score families
- 0-0
- 1-0 PSG
- 0-1 Frankfurt
- 1-1
- 2-0 / 0-2

### Over 2.5 families
- 2-1 either way
- 3-0
- 2-2+

### Why Under has the slight edge
- Frankfurt's last five competitive matches: **4/5 Under 2.5**.
- The first leg generated two very early goals but no third across the remaining 80+ minutes.
- Aggregate starts level, so there is no forced chase until a goal occurs.
- Frankfurt have shown an ability to defend leads / keep games at 2 total or fewer.

### Strongest Under kill path
- early goal by either team forces the other to chase;
- PSG's home attack converts the additional territory;
- Frankfurt's strong set-piece/corner pressure produces a second/third goal.

Therefore the full total is close, but Under is marginally more robust than Over.

## K. Environment

Poissy forecast:
- roughly **20-24°C** through the afternoon/evening
- very low / 0% precipitation in the current local forecast
- light wind approximately 4-7 km/h
- no abnormal surface report recovered

No strong environmental suppression or enhancement is applied.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-256-C05 — Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | First leg produced 15; Frankfurt latest tracked five produced 11/15/9/11/8; PSG recent tracked sample also clears frequently. Tied aggregate ensures neither side can simply defend a lead from kickoff. Definition gap prevents LEAN label. |
| **2** | **P-256-C01 — 1st Half Over 0.5 Goals** | **LEAN** | **MEDIUM** | First leg had goals at 4' and 7'; both teams' current known halftime states are heavily early-goal oriented. Level aggregate caution is the main suppressor. |
| **3** | **P-256-C04 — Full Match Under 2.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | Frankfurt are 4/5 Under 2.5 in current competitive matches; first leg had two goals despite early scoring; tied aggregate allows a long tactical central branch. |
| **4** | **P-256-C03 — Full Match Over 2.5 Goals** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** | An early goal creates a clear chase/open-game state and both teams have attacking quality. It ranks below Under because the raw current Frankfurt total regime remains strongly low-scoring. |
| **5** | **P-256-C02 — 1st Half Under 0.5 Goals** | **AVOID relative to C01** | **LOW-MEDIUM** | Requires 0-0 HT despite an early-goal-heavy current sample and the first-leg 4'/7' goals. Its route is a much more cautious second-leg opening. |

## M. Rank-1 coherence

Rank #1 is Corners Over 8.5.

- 1H Over 0.5: `PARTIAL_OVERLAP` — early goal can increase chase/crossing exposure.
- Full Under 2.5: `COHERENT / PARTIAL` — low goals can coexist with high corners.
- Full Over 2.5: `COHERENT / PARTIAL` — an open chase also supports corners.
- 1H Under 0.5: `PARTIAL_OVERLAP` — 0-0 HT can still build late corners.

No ranked row is structurally disjoint from the corner thesis.

## N. Potential winner / qualification endpoint

### **Paris Saint-Germain to advance — SLIGHT LEAN**

This is a qualification call, not a strong 90-minute winner claim.

Supporting factors:
- home second leg at PSG Campus;
- first-leg PSG survived the larger Frankfurt pressure and still earned 1-1;
- PSG have multiple high-level attacking options and stronger squad depth on paper;
- home environment removes travel from PSG and places Frankfurt under away knockout pressure.

Counterweights:
- Frankfurt were arguably the stronger chance-generating side in leg one;
- Frankfurt's high press created the first goal and their 10-corner / 7-shot profile was stronger;
- Hanna Bennison hit both posts in one second-half sequence;
- Frankfurt have more current competitive-match rhythm than PSG.

Therefore:
- **PSG to advance: slight lean**
- Frankfurt advancing is a substantial competing branch.
- No high-confidence regulation winner is published.

## O. Final delivery

1. **Total Corners Over 8.5**
2. **1st Half Over 0.5 Goals**
3. **Full Match Under 2.5 Goals**
4. **Full Match Over 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential winner endpoint:** Paris Saint-Germain **to advance — slight lean**.

## P. Append confirmation
- Every incomplete local event rechecked: YES
- Newly safe-to-settle event: NO
- P-256 frozen pre-start: YES
- Confirmed second-leg XI unavailable at cutoff: YES / preserved as uncertainty
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-257**


---

# Queue state check before P-257 — 2026-09-03

## Current incomplete / unresolved local items
- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED**.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**.
- `P-252` Belfast Wolves–Edinburgh Castle Rockers: **OPEN / FIELD-OWNER STATE DEFECT**.
- `P-253` El Gounah–Al Mokawloon: **OPEN / FINAL NOT VERIFIED**.
- `P-254` Choinski–Van de Zandschulp: **OPEN / UPCOMING-NOT STARTED** at this sweep.
- `P-255` Inter Women–Wolfsburg Women: scheduled start crossed; **NO VERIFIED FINAL**.
- `P-256` PSG Women–Eintracht Frankfurt Women: scheduled start crossed; **NO VERIFIED FINAL**.

No newly final event was safe to settle. No retrospective was fabricated. All older provisional/operator-definition follow-ups remain open as previously recorded.

---

# P-257 — San Diego Padres (Casey Mize) @ Cincinnati Reds (Brandon Williamson) — MLB — PREGAME

## A. Frozen identity / state
- **Canonical ID:** `P-257`
- **League:** MLB
- **Event:** San Diego Padres @ Cincinnati Reds
- **Venue:** Great American Ball Park, Cincinnati, Ohio
- **Scheduled first pitch:** 2026-09-02 12:40 EDT
- **Australia/Melbourne:** 2026-09-03 02:40 AEST
- **Frozen research cutoff:** approximately 02:38 AEST, before scheduled first pitch
- **GAME-STATE:** PREGAME / SCHEDULED
- **Home last bat:** Cincinnati
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-BASEBALL`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
- **Value state:** `NO VALUE DETERMINABLE`
- **Operator/action/listed-pitcher terms:** NOT SUPPLIED / `UNKNOWN_DEFINITION`

## B. User-supplied slate
| ID | Contract | Ordinary completed-game settlement |
|---|---|---|
| `P-257-C01` | Padres -1.5 | SD wins by 2+ |
| `P-257-C02` | Reds +1.5 | CIN wins or loses by exactly 1 |
| `P-257-C03` | Over 9.5 runs | 10+ combined runs |
| `P-257-C04` | Under 9.5 runs | 0-9 combined runs |

C01/C02 and C03/C04 are exact half-run complements under ordinary completed-game terms.

## C. Starter identity and regime

### Casey Mize — Padres, RHP
MLB confirms San Diego acquired Mize from Detroit on 3 August 2026.

**Detroit pre-trade regime**
- 16 starts
- 4-6
- 2.70 ERA
- 2.59 FIP
- 85 K / 19 BB in 86.2 IP

**Padres post-trade regime**
Recent game log:
- at Arizona: 3.1 IP, 8 ER
- vs Milwaukee: 6 IP, 2 ER
- at Cleveland: 6 IP, 0 ER
- vs Minnesota: 2.2 IP, 4 ER, 3 HR
- at Tampa Bay: 5 IP, 7 R, 2 ER

The current Padres-only line exposed by the latest gametracker is roughly:
- 23 IP
- 1-2
- 6.26 ERA
- 1.52 WHIP

Interpretation:
- season reputation/Detroit form cannot silently override the post-trade San Diego regime;
- Mize retains a credible 5-6 inning suppression branch;
- his Padres starts also contain large hook/error/HR tails;
- the latest Tampa result included five unearned runs, so not all recent scoreboard damage is attributed to pitcher skill.

### Brandon Williamson — Reds, LHP
MLB confirms:
- 2-3
- 6.11 ERA
- 19 SO
- first MLB start since 29 April
- activated from the IL after a long shoulder-related absence
- missed 2025 following Tommy John surgery

2026 MLB pre-injury starts:
- 4.2 IP, 6 ER
- 6.2 IP, 0 ER
- 4 IP, 3 ER
- 5.1 IP, 1 ER
- 4.1 IP, 5 ER
- 3 IP, 4 ER

Totals over those six:
- 28 IP
- 19 K
- 20 BB
- 1.64 WHIP

Interpretation:
- Williamson has a very wide current exposure/run-rate mixture;
- no full normal-starter workload is assumed after the long layoff;
- an early hook creates extra Reds relief exposure;
- a short start is not automatically an Over, but Cincinnati's recent staff performance makes that relief transition non-trivial.

## D. Current lineup / participant gate

MLB's official starting-lineup page was still showing `TBD` close to the frozen cutoff, creating a field-owner publication lag.

A current secondary gametracker listed:
### San Diego
Tatis Jr.; Samad Taylor; Jackson Merrill; Ty France; Xander Bogaerts; Ethan Salas; Austin Hays; Luis Campusano; Jake Cronenworth.

### Cincinnati
Héctor Rodríguez; Elly De La Cruz; Sal Stewart; JJ Bleday; Tyler Stephenson; Dane Myers; Juan Brito; Matt McLain; Edwin Arroyo.

Important participant notes:
- Ethan Salas was called up for September and the latest gametracker had him making his MLB debut.
- Elly De La Cruz has recently been used at DH while managing a quad issue.
- Sal Stewart enters with 31 HR / 105 RBI in the current source.
- Because the field-owner lineup page lagged, the card does not treat every secondary batting slot as `CONFIRMED_OFFICIAL`.

## E. Recent team form

### Padres
Latest five runs scored:
- 4
- 6
- 4
- 5
- 3
= **22 runs / 4.4 per game**

Latest 10:
- **42 runs**
- .228 AVG / .306 OBP / .357 SLG / .663 OPS

Current structural interpretation:
- San Diego's offense has been inconsistent rather than dead.
- They produced 15 hits in the 5-0 opener here, then went 0-for-10 with RISP in the 4-3 loss.
- Tatis hit two homers in the latest game.
- Padres' low L10 OPS is a meaningful counterweight to a simple Williamson-fade thesis.

### Reds
Latest five:
- 10
- 5
- 7
- 0
- 4
= **26 runs / 5.2 per game**

Latest 10:
- **51 runs**
- .264 AVG / .338 OBP / .464 SLG / .802 OPS

Recent staff:
- latest current StatMuse team-pitching query shows a **6.59 ERA over the last 10**.

Interpretation:
- Cincinnati's offense has materially more current run/HR volume than San Diego's.
- Cincinnati's run-prevention tail is also much wider, supporting both Padres separation and the full-game Over branch.

## F. Handedness / matchup note
Padres' season line against left-handed pitching in the retrieved current source:
- .233 AVG
- .297 OBP
- .366 SLG
- .663 OPS

This is a real suppression factor for the Padres scoring centre and prevents Williamson's 6.11 ERA from becoming an automatic huge San Diego total.

However:
- Williamson's control/exposure uncertainty is materially larger than a normal established left-handed starter;
- San Diego's right-handed core is well positioned to receive multiple plate appearances if Williamson's command fails.

## G. Current-season H2H continuity
Previous five 2026 meetings:
- Padres 6-2 Reds
- Reds 5-3 Padres (11 innings)
- Padres 5-4 Reds
- Padres 5-0 Reds
- Reds 4-3 Padres

Descriptive:
- Padres lead 3-2.
- Padres -1.5 covered **2/5**.
- Reds +1.5 covered **3/5**.
- **Under 9.5 was 5/5**.

This is the strongest argument against ranking the Over too aggressively.

Why it does not control:
- today's starter pairing is unlike the prior games;
- Williamson is returning from a long IL absence;
- Mize's post-trade run distribution is wider than his Detroit season line;
- current midday conditions are materially hitter-friendlier than a neutral environment.

## H. Environment
Current game-day weather sources agree on:
- roughly **91-94°F near first pitch**
- essentially dry
- light wind, roughly 4-8 mph
- some sources indicate a component toward/out to left or left-center

No rain/termination concern.

Mechanistic use:
- hot, dry air does not suppress carry;
- modest wind is not strong enough to dictate the total alone;
- the environment raises the HR/contact tail at an already power-friendly venue but is treated as a scale factor, not a manufactured scoring mechanism.

## I. Joint run tree

### Lower state
Representative:
- Padres 4, Reds 3
- or Padres 5, Reds 3

Mechanism:
- Mize recovers toward his Detroit-quality centre;
- Williamson is efficiently limited and Cincinnati's relief chain holds;
- Padres continue current RISP inefficiency.

Helps:
- Under 9.5
- Reds +1.5 in the one-run branch

### Central state
Representative:
- **Padres 6, Reds 4**

Mechanism:
- Williamson's return/command limits Cincinnati's starter length;
- Padres exploit the first relief transition;
- Reds still score through Mize's current volatility and current power form.

Helps:
- Over 9.5
- Padres -1.5

### Upper cluster state
Representative:
- Padres 8, Reds 5
- or Reds 7, Padres 6

Mechanism:
- both starters shorten;
- HR/sequencing clusters in hot conditions;
- trailing bullpen states summon weaker relief arms.

Helps:
- Over strongly
- run-line direction depends on cluster allocation

### One-sided Padres separation
Representative:
- Padres 7, Reds 2

Mechanism:
- Williamson's command fails early;
- Mize lands on his 5-6 inning suppression branch;
- Cincinnati cannot activate its late offensive state.

Helps:
- Padres -1.5
- Under 9.5 can still win at exactly 9 total runs

## J. Component budget at 9.5

To reach 10 runs:

If San Diego scores 6:
- Cincinnati needs 4.

If San Diego scores 5:
- Cincinnati needs 5.

If Cincinnati scores 4:
- San Diego needs 6.

This threshold is not automatically an Over from one weak starter. The Over needs meaningful contribution from both sides or a dominant one-team 7-8 run branch.

Current support for that:
- Reds L5 scoring = 5.2/game
- Padres L10 = 4.2/game
- both starters have wide recent/return-state run distributions
- hot run environment

Counter:
- five straight season H2Hs stayed Under 9.5
- Padres' current offense is only .663 OPS over L10
- Padres are weak vs LHP on the season

## K. Separation budget at ±1.5

For Padres -1.5:
- San Diego must create at least two net runs of separation.
- Mize's current Padres volatility means a winner lean does not automatically become a run-line cover.
- Williamson's return-state plus Cincinnati's recent 6.59 staff ERA creates genuine 6-3 / 7-3 / 7-4 separation branches.

For Reds +1.5:
- every Cincinnati win covers;
- every one-run Padres win covers;
- home last-bat supports late one-run compression;
- current-season H2H produced three +1.5 covers in five.

The critical question is whether Cincinnati's pitching transition breaks before Mize's volatility does.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-257-C03 — Over 9.5 Runs** | **LEAN** | **MEDIUM** | Both starter states are unusually wide: Mize has a 6.26 Padres-only ERA in 23 IP and Williamson returns from a long IL absence with a 6.11 ERA / 1.64 WHIP / 20 BB to 19 K. Reds have scored 51 in L10 and their staff ERA is 6.59 over L10; hot GABP conditions add HR/contact tail. The 5/5 season H2H Under record is the strongest contrary path. |
| **2** | **P-257-C01 — Padres -1.5** | **SLIGHT LEAN** | **MEDIUM-LOW** | San Diego owns the clearer starter/relief transition advantage if Williamson is short or wild, and Cincinnati's recent run prevention is poor. Mize's volatility and Reds' current offense prevent a stronger cover call. |
| **3** | **P-257-C04 — Under 9.5 Runs** | **FORCED RANK / LEAN-ADJACENT** | **MEDIUM-LOW** | Every 2026 H2H so far stayed below 10 and San Diego's L10 offense is weak. It falls below the Over because today's starter pair and heat create substantially more upper-tail exposure than those prior games. |
| **4** | **P-257-C02 — Reds +1.5** | **FORCED RANK / weaker side direction** | **MEDIUM-LOW** | Home last bat, Mize volatility, and three +1.5 covers in five current-season H2Hs make this live. It ranks last because Williamson's return/command uncertainty plus Cincinnati's recent pitching collapse creates the clearest two-plus-run separation risk. |

## M. Rank-1 coherence

Rank #1 = Over 9.5.

- Padres -1.5: `COHERENT / PARTIAL` — central 6-4 / 7-4 / 8-5 Padres states support both.
- Under 9.5: `DISJOINT` exact total complement.
- Reds +1.5: `PARTIAL_OVERLAP` — high-scoring 6-5 / 7-6 games can cash Over + Reds cushion.

No cross-row contradiction requires repair.

## N. Potential winner

### **San Diego Padres — SLIGHT LEAN**

Why:
- Williamson's return-state is the largest single uncertainty in the game;
- Padres have the stronger broad run-prevention profile;
- Mize's season-level underlying 2026 work before the trade was strong despite his poor Padres-only results;
- Cincinnati's recent staff run prevention is much worse.

Why only slight:
- Reds offense is currently hotter;
- Mize has been unstable since the trade;
- Cincinnati has home last bat;
- Padres have lost four of their last five entering the finale.

## O. Final delivery
1. **Over 9.5 Runs**
2. **Padres -1.5**
3. **Under 9.5 Runs**
4. **Reds +1.5**

**Potential winner:** San Diego Padres — slight lean.

## P. Append confirmation
- All current incomplete local items rechecked: YES
- Newly verified final requiring retrospective: NO
- P-257 frozen before scheduled first pitch: YES
- MLB starter identity verified: YES
- Official lineup page lag preserved as uncertainty: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-258**


---

# Queue state check before P-258 — 2026-09-03

## Current unresolved/local items
- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED**.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**.
- `P-252` Belfast Wolves–Edinburgh Castle Rockers: **OPEN / FIELD-OWNER STATE DEFECT**.
- `P-253` El Gounah–Al Mokawloon: **OPEN / FINAL NOT VERIFIED**.
- `P-254` Choinski–Van de Zandschulp: **OPEN / current US Open surfaces had not yet produced a final**.
- `P-255` Inter Women–Wolfsburg Women: **LIVE / no verified final**.
- `P-256` PSG Women–Eintracht Frankfurt Women: **LIVE / no verified final**.
- `P-257` Padres–Reds: **LIVE / scheduled start crossed; no final**.

No newly final local item was safe to settle. No retrospective was fabricated.

---

# P-258 — Atlanta Braves (Grant Holmes) @ Washington Nationals (Brad Lord) — MLB — PREGAME

## A. Frozen identity / state
- **Canonical ID:** `P-258`
- **League:** MLB
- **Event:** Atlanta Braves @ Washington Nationals
- **Venue:** Nationals Park, Washington, D.C.
- **Scheduled first pitch:** 2026-09-02 13:05 EDT
- **Australia/Melbourne:** 2026-09-03 03:05 AEST
- **State at cutoff:** PREGAME / SCHEDULED
- **Home last bat:** Washington
- **Method:** `MDS-2026.09.02-v3.1`
- **Algorithms:** `GFA-2` + `SFA-BASEBALL`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability:** NOT_GENERATED / NOT_PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Operator action/listed-pitcher terms:** NOT SUPPLIED / UNKNOWN_DEFINITION

## B. User-supplied contracts

| ID | Contract | Ordinary completed-game region |
|---|---|---|
| `P-258-C01` | Braves ML | Atlanta wins |
| `P-258-C02` | Nationals +1.5 | Washington wins or loses by exactly one |
| `P-258-C03` | Over 9.5 | 10+ combined runs |
| `P-258-C04` | Under 9.5 | 0-9 combined runs |

C03/C04 are exact complements. C01 and C02 overlap in every one-run Atlanta win.

## C. Starter state

### Grant Holmes — Atlanta RHP
Current season:
- 9-5
- 3.71 ERA
- 128.2 IP
- 103 K
- 1.34 WHIP

August:
- 5 starts
- 26.2 IP
- **3.04 ERA**
- three scoreless starts
- one six-run outlier vs Arizona
- latest: 5 IP, 3 ER vs Colorado

Recent August starts:
- 6 IP, 0 ER vs Miami
- 6 IP, 0 ER at NYY
- 3.2 IP, 6 ER vs Arizona
- 6 IP, 0 ER at CWS
- 5 IP, 3 ER vs Colorado

Direct 2026 Nationals evidence:
- two prior appearances/starts against Washington
- 5 earned runs in 9.2 innings
- Washington hitters including Daylen Lile, Dylan Crews and Jorbit Vivas have created meaningful damage in the current series history

Interpretation:
- Holmes has the stronger current starter centre.
- His Nationals-specific matchup is not dominant enough to erase Washington's scoring branch.
- Atlanta can reasonably expect about five-to-six starter innings in the ordinary state, not a guaranteed quality start.

### Brad Lord — Washington RHP / opener-bulk role
Current season:
- 33 games
- 5-2
- 3.75 ERA
- 69.2 IP
- 64 K
- 1.19 WHIP

Latest three appearances:
- 2.1 IP, 1 ER vs Miami
- 2.1 IP, 0 ER vs Colorado
- 2.2 IP, 0 ER at Miami

Latest five include:
- 7.1 combined IP / 1 ER across the most recent three
- a 2-ER short outing at the Mets
- another 2.2-IP, 1-ER outing vs Cincinnati

Interpretation:
- Lord is currently pitching well.
- He is an opener/bulk bridge, not a normal six-inning starter.
- The game therefore exposes Atlanta to a larger Washington relief-chain share than a conventional Lord ERA comparison implies.
- Washington has an off day next, so manager flexibility is higher, but Jared Simpson threw three innings the night before and should not be assumed fully available.

## D. Bullpen structure

### Atlanta
Recent team relief/pitching run prevention:
- Braves L10 relief/team ERA source: roughly **3.3**
- current bullpen has been materially more stable than Washington's across the season

### Washington
Current preview sources describe the Nationals bullpen as among the worst in MLB / third-worst by ERA.
- Lord's short role means the relief chain is structurally decision-driving.
- Washington can be aggressive with available arms because of the following off day.
- However, the strongest fresh long-relief performance — Jared Simpson's three scoreless innings Tuesday — likely reduces his same-day availability.

This is the main reason Atlanta still owns the larger outright-win branch despite Washington's current offense.

## E. Current lineups / participant state

MLB's own lineup page remained `TBD` near the cutoff, but current local gameday reporting had the actual current changes:

### Atlanta core
- Drake Baldwin at DH
- Ronald Acuña Jr.
- Matt Olson
- Ozzie Albies
- Michael Harris II
- Sean Murphy
- Mike Yastrzemski
- Austin Riley
- Ha-Seong Kim

Notable current changes:
- Mike Yastrzemski starts in left
- Sean Murphy catches
- Baldwin shifts to DH
- Mauricio Dubón rests

### Washington current changes
- **James Wood returns** from an oblique issue and leads off in RF
- CJ Abrams shifts to the middle/cleanup region and plays second
- Yohandy Morales remains after a 3-hit debut
- Andres Chaparro / Abi Ortiz are in the current young-lineup mix
- Keibert Ruiz returns at catcher

Participant interpretation:
- Washington's lineup is stronger than the prior game's generic post-deadline roster because Wood is back.
- Atlanta still has the deeper established top/middle offensive core.
- No player prop is selected because the MLB field-owner lineup page lagged.

## F. Current offense

### Atlanta
Current L10 source:
- **35 runs in last 10**
- approximately 3.5 runs/game
- post-All-Star offense has been materially weaker than the season-wide top-10 reputation

Latest context:
- scored 5 in the 9-5 loss Tuesday
- Michael Harris II has homered in consecutive games / three of five
- Braves entered after a seven-game win streak, then lost two straight

### Washington
Current form:
- 9 runs vs Atlanta
- 6 vs Miami
- 2 vs Miami
- 5 vs Miami
- 9 vs Miami
- 7 vs Colorado
- 1 vs Colorado
- 13 vs Colorado in another recent home game

Current home L10:
- **57 runs**
- current home offense is materially hotter than its broad season reputation

Recent team trajectory:
- Washington has won five of six entering this game
- current homestand is 7-3
- James Wood's return adds another high-impact bat

This is why Nationals +1.5 is elevated above a simple Atlanta-team-strength pick.

## G. Season-series / H2H geometry

2026 completed series before today:
- ATL 9-4
- WSH 11-4
- ATL 8-6
- ATL 7-2
- ATL 5-4 (11)
- WSH 2-0
- WSH 2-1
- ATL 5-4
- ATL 6-2
- ATL 8-3
- ATL 4-2
- WSH 9-5

Descriptive:
- Atlanta ML: **8/12**
- Washington wins: 4/12
- Nationals +1.5: **6/12** (four WSH wins + two one-run ATL wins)
- Over 9.5: **5/12**
- Under 9.5: **7/12**

H2H supports Atlanta winner more than Washington cushion, but the recent Washington home/offensive regime is stronger than the early-season average.

## H. Weather / park environment

Current Nationals Park forecast around first pitch:
- approximately **87-90°F**
- humid / feels much warmer
- light easterly wind roughly 4-7 mph
- no strong wind-out signal
- precipitation estimates conflict by source: some local hourly feeds show low immediate risk, while one baseball-weather source flags scattered thunderstorms later in the game

Mechanistic treatment:
- heat does not suppress carry
- light wind has minimal directional effect
- any interruption would create starter-to-bullpen transition risk and widen total variance
- weather is therefore a variance factor, not an automatic Over

## I. Joint run tree

### Central close-Atlanta state
**ATL 5, WSH 4**
- Braves ML: WIN
- Nationals +1.5: WIN
- Under 9.5: WIN

Mechanism:
- Holmes gives 5-6 competent innings
- Atlanta scores enough against Lord + relief transition
- Washington's current lineup still reaches 3-4 runs
- Atlanta's stronger bullpen protects a narrow lead

### Atlanta separation state
**ATL 6, WSH 3**
- Braves ML: WIN
- Nationals +1.5: LOSS
- Under 9.5: WIN

Mechanism:
- Holmes suppresses Washington's current hot offense
- Atlanta gets to the weaker Washington relief chain

### Washington upset state
**WSH 5, ATL 4**
- Braves ML: LOSS
- Nationals +1.5: WIN
- Under 9.5: WIN

Mechanism:
- Washington continues its home offensive surge
- Holmes repeats his less-effective Nationals matchup
- Lord/bullpen sequencing survives

### Upper-tail state
**ATL 7, WSH 5** or **WSH 6, ATL 5**
- Over 9.5 wins
- side/cushion depends on allocation

Mechanism:
- Lord exits early and Washington's relief chain is hit
- Holmes allows 3-4 before Atlanta's bullpen
- hot/humid conditions plus bullpen transition increase cluster scoring

## J. 9.5 component budget

For Over:
- ATL 5 requires WSH 5
- ATL 6 requires WSH 4
- WSH 5 requires ATL 5

Current central scoring estimates are close to the line rather than clearly above it.

Under support:
- Holmes August centre is strong
- Atlanta bullpen L10 is stable
- Braves offense has only 35 runs in L10
- 7/12 H2Hs stayed Under 9.5

Over support:
- Washington home offense is hot
- James Wood returns
- Nationals bullpen exposure is high
- recent first game of series finished 9-5
- weather/interruption variance can widen relief exposure

Under therefore receives only a slight edge, not a strong recommendation.

## K. Side / cushion separation budget

### Braves ML
Wins through every Atlanta one-run or larger victory.
Main edge:
- stronger starter centre
- stronger broad bullpen
- stronger season team quality

Main failure:
- Washington's current home offense and James Wood return
- Holmes has not dominated this opponent

### Nationals +1.5
Wins through:
- every Washington victory
- every one-run Atlanta win

This is a broad union of the Washington upset branch plus the close-Atlanta branch.

The most likely failure family is Atlanta winning by 2+ because:
- Lord's short role exposes Washington's weak bullpen
- Atlanta's lineup can create separation after the opener exits

Given Washington's recent home form and Atlanta's mediocre current offense, the cushion is marginally more robust than the Atlanta winner itself.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-258-C02 — Nationals +1.5** | **LEAN** | **MEDIUM** | Captures every Washington win plus one-run Atlanta wins. Washington has won five of six, scored 57 in its last 10 home games, and gets James Wood back. Holmes is strong but not dominant vs this opponent. The kill path is Atlanta reaching Washington's weak bullpen and separating by 2+. |
| **2** | **P-258-C01 — Braves ML** | **LEAN** | **MEDIUM** | Atlanta owns the stronger starter centre (Holmes 3.04 ERA in August), deeper season quality, and more reliable bullpen. Washington's current hot offense prevents a stronger label. |
| **3** | **P-258-C04 — Under 9.5 Runs** | **SLIGHT LEAN** | **MEDIUM-LOW** | Central 5-4 / 6-3 / 5-3 families stay Under; 7/12 H2Hs did too. Holmes and Atlanta's pen provide the strongest suppression mechanisms. Washington's hot home offense and weak bullpen keep the Over tail substantial. |
| **4** | **P-258-C03 — Over 9.5 Runs** | **FORCED RANK / weaker total direction** | **MEDIUM-LOW** | Very live through bullpen exposure, James Wood's return, Washington's current scoring surge and possible weather interruption. It remains below Under because the line requires 10 runs and Atlanta's own L10 offense has been modest. |

## M. Rank-1 coherence / winner reconciliation

Rank #1 = Nationals +1.5.

Representative Rank-1 central state:
**Braves 5, Nationals 4**

This makes:
- Nationals +1.5 = WIN
- Braves ML = WIN
- Under 9.5 = WIN

Therefore the top three are strongly coherent.

Why Braves remain the potential winner while Washington +1.5 ranks #1:
- Atlanta has the larger outright winner branch because Holmes + bullpen are stronger.
- Washington +1.5 adds all close Atlanta wins to Washington's own win branch.
- The difference is specifically the **one-run Atlanta-win corridor**, not an independent contradictory narrative.

## N. Potential winner
### **Atlanta Braves — SLIGHT LEAN**

Reasons:
- Holmes' August run-prevention centre
- Washington's opener-to-bullpen exposure
- Atlanta's stronger season run differential / record
- Braves have won 8 of 12 current-season H2Hs

Counter:
- Washington is hotter at home and just won 9-5
- James Wood returns
- Braves offense has been mediocre recently

## O. Final delivery
1. **Nationals +1.5**
2. **Braves ML**
3. **Under 9.5 Runs**
4. **Over 9.5 Runs**

**Potential winner:** Atlanta Braves — slight lean.

## P. Append confirmation
- All current incomplete local items rechecked: YES
- Newly safe-to-settle item: NO
- P-258 frozen pre-start: YES
- Holmes/Lord starter identities verified: YES
- Current lineup publication lag disclosed: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New forecast-weight rule: NO
- **NEXT CANONICAL ID: P-259**


---

# Settlement / retrospective sweep before P-259 — 2026-09-03

## P-254 — Choinski vs Van de Zandschulp — FINAL

**Official final:** Botic Van de Zandschulp def. Jan Choinski **6-3, 6-1, 7-6(5)**.

- Total games: **29**
- Net game margin: Botic **+9**

| ID | Rank | Contract | Outcome |
|---|---:|---|---|
| P-254-C02 | 1 | Van de Zandschulp -5.5 | **WIN** |
| P-254-C04 | 2 | Under 38.5 | **WIN** |
| P-254-C01 | 3 | Choinski +5.5 | **LOSS** |
| P-254-C03 | 4 | Over 38.5 | **LOSS** |

**Potential winner — Botic:** **WIN**.

### Retrospective
Process grade: **COMPLIANT**.
- Rank #1 won through the exact predeclared mechanism: Botic's stronger current hard return profile created real break separation.
- Botic held in all 14 service games and broke Choinski four times.
- Choinski's serve-resistance branch appeared only late, producing the third-set tiebreak; it was not large enough to rescue +5.5 or the Over.
- The central scoreline `6-3, 6-4, 6-4` was directionally close to the actual 6-3, 6-1, 7-6.
- No new tennis weight is promoted.

## P-255 — Inter Women vs Wolfsburg Women — FINAL

**90-minute result:** Inter **2-0** Wolfsburg.
**HT:** Inter 1-0.
Inter ultimately advanced after extra time and penalties.

| ID | Rank | Contract | 90-minute outcome |
|---|---:|---|---|
| P-255-C01 | 1 | 1H Over 0.5 | **WIN** |
| P-255-C05 | 2 | Corners Over 8.5 | **UNRESOLVED / provider-definition final not recovered** |
| P-255-C03 | 3 | Full Over 2.5 | **LOSS** |
| P-255-C04 | 4 | Full Under 2.5 | **WIN** |
| P-255-C02 | 5 | 1H Under 0.5 | **LOSS** |

**Potential winner — Wolfsburg to advance:** **LOSS**.

### Retrospective
Process grade: **MIXED / PHASE-PROPAGATION CAUTION**.
- Rank #1 early-goal direction was correct: Inter scored at 40'.
- The card correctly preserved Full Under as a credible branch; regulation stopped at exactly two goals.
- The Over branch overstated how much Inter's aggregate chase would propagate into a third 90-minute goal.
- The advancement miss came from underweighting the exact `Inter wins by two in regulation -> extra-time/penalty variance` branch.
- No new forecast weight; reinforce existing two-leg regime-switch and endpoint-separation controls.

## P-256 — PSG Women vs Eintracht Frankfurt Women — FINAL

**90-minute result:** PSG **1-1** Frankfurt.
**HT:** PSG 0-1 Frankfurt.
PSG ultimately advanced after extra time.

| ID | Rank | Contract | 90-minute outcome |
|---|---:|---|---|
| P-256-C05 | 1 | Corners Over 8.5 | **UNRESOLVED / exact provider final not recovered** |
| P-256-C01 | 2 | 1H Over 0.5 | **WIN** |
| P-256-C04 | 3 | Full Under 2.5 | **WIN** |
| P-256-C03 | 4 | Full Over 2.5 | **LOSS** |
| P-256-C02 | 5 | 1H Under 0.5 | **LOSS** |

**Potential winner — PSG to advance:** **WIN**.

### Retrospective
Process grade: **COMPLIANT**.
- The forecast explicitly identified `1H Over + Full Under` as a coherent central family; the 90-minute result delivered exactly that structure.
- Frankfurt scored before halftime, then regulation remained at two total goals.
- PSG's advancement lean also won, but only after extra time, validating the distinction between 90-minute winner and qualification endpoint.
- No new rule promoted.

## P-257 — Padres @ Reds — FINAL

**Final:** Cincinnati Reds **7-3** San Diego Padres.

| ID | Rank | Contract | Outcome |
|---|---:|---|---|
| P-257-C03 | 1 | Over 9.5 | **WIN** |
| P-257-C01 | 2 | Padres -1.5 | **LOSS** |
| P-257-C04 | 3 | Under 9.5 | **LOSS** |
| P-257-C02 | 4 | Reds +1.5 | **WIN** |

**Potential winner — Padres:** **LOSS**.

### Retrospective
Process grade: **RANK-1 COMPLIANT / SIDE DEFECT**.
- Rank #1 Over won through the identified wide starter distributions.
- Brandon Williamson was better than the downside return-state feared, giving Cincinnati 5.1 innings and allowing three runs.
- Mize's poor Padres regime persisted; Cincinnati hit three home runs and turned a 3-0 deficit into a 7-3 win.
- The side call over-weighted Williamson's return uncertainty as a Padres advantage and under-weighted Mize's post-trade HR/run-volatility plus Cincinnati's hotter offense.
- Return-from-IL uncertainty is two-sided variance, not an automatic opponent-side upgrade. No fitted weight change.

## P-258 — Braves @ Nationals — FINAL

**Final:** Atlanta Braves **7-0** Washington Nationals.

| ID | Rank | Contract | Outcome |
|---|---:|---|---|
| P-258-C02 | 1 | Nationals +1.5 | **LOSS** |
| P-258-C01 | 2 | Braves ML | **WIN** |
| P-258-C04 | 3 | Under 9.5 | **WIN** |
| P-258-C03 | 4 | Over 9.5 | **LOSS** |

**Potential winner — Braves:** **WIN**.

### Deep Rank-1 retrospective
Process grade: **PROCESS_DEFECT — SEPARATION BUDGET UNDERWEIGHTED**.

What went right:
- Braves winner direction was correct.
- Under 9.5 was correct.
- The forecast explicitly identified Atlanta's strongest separation route: Holmes suppresses Washington and Atlanta reaches the weaker relief chain.

What went wrong:
- Nationals +1.5 was ranked first because it unioned Washington wins with one-run Atlanta wins, but the probability mass of the **Atlanta 2+ separation branch** was underweighted.
- Washington's recent hot home offense and James Wood's return were allowed to compress the margin too much.
- Grant Holmes and Atlanta relief combined to allow only two hits; the weather interruption did not weaken Atlanta's run prevention because Elieser Hernández supplied three scoreless relief innings.
- Atlanta's offense eventually broke the game open, led by Sean Murphy's three-run homer/four RBI.

Learning disposition:
- Reinforces `L-058` separation-budget control: a cushion cannot become Rank #1 merely because it catches close favorite wins; the favorite's starter-plus-bullpen shutdown state and opponent bullpen exposure must be explicitly budgeted as a multi-run branch.
- No new fitted weight or calibration change from one event.

## Still unresolved after sweep
- `P-250-C05` corners — unresolved.
- `P-251-C05` corners — provisional threshold-invariant win.
- `P-252` Belfast Wolves–Edinburgh Castle Rockers — field-owner source-state defect / no verified final.
- `P-253` El Gounah–Al Mokawloon — no field-owner final recovered.
- `P-255-C05` and `P-256-C05` corner rows — unresolved pending exact provider/definition-capable final.


---

# P-259 — New York Mets (Justin Hagenman) @ Tampa Bay Rays (Griffin Jax) — MLB — PREGAME

## A. Frozen identity / state

- **Canonical ID:** `P-259`
- **League:** MLB
- **Event:** New York Mets @ Tampa Bay Rays
- **Venue:** Tropicana Field, St. Petersburg, Florida
- **Venue class:** INDOOR / fixed-roof controlled environment
- **Scheduled first pitch:** 2026-09-02 18:40 EDT
- **Australia/Melbourne:** 2026-09-03 08:40 AEST
- **Research cutoff:** approximately 08:16-08:25 AEST, pre-start
- **GAME-STATE:** PREGAME / SCHEDULED
- **Home last bat:** Tampa Bay
- **Method:** `MDS-2026.09.02-v3.1`
- **Algorithms:** `GFA-2` + `SFA-BASEBALL`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability:** NOT_GENERATED / NOT_PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Operator action/listed-pitcher terms:** NOT SUPPLIED / UNKNOWN_DEFINITION

## B. User-supplied slate / geometry

| ID | Contract | Ordinary completed-game result |
|---|---|---|
| `P-259-C01` | Rays ML | Tampa Bay wins |
| `P-259-C02` | Mets +1.5 | New York wins or loses by exactly one |
| `P-259-C03` | Over 8.0 | 9+ runs win; exactly 8 pushes |
| `P-259-C04` | Under 8.0 | 0-7 runs win; exactly 8 pushes |

The total pair is an integer-line pair with a common push at exactly 8. C01 and C02 overlap in every one-run Rays victory.

## C. Confirmed starter roles

### Justin Hagenman — Mets RHP
- 2026 MLB season debut.
- Reinstated from 60-day IL after a rib fracture.
- Recent rehab: **2.89 ERA over 9.1 innings** across A/AA/AAA.
- 2025 MLB: approximately **4.5 ERA over 23.2 innings**, mostly bulk/relief exposure.
- Current assignment is partly to provide rest for the Mets' young starters and evaluate Hagenman for future depth.

Mechanistic consequences:
- he should not be treated as a normal six-inning established starter;
- current major-league form is **unknown**, not 0.00 ERA;
- early hook/bulk transition is a material branch;
- the injury was rib-related rather than elbow/shoulder, so no unsupported velocity-loss claim is made.

### Griffin Jax — Rays RHP
- Current 2026 line: **6-9, 3.63 ERA, 91.2 IP, 100 K, 1.21 WHIP**.
- Returning from IL after right-elbow discomfort.
- Before IL, recent full starts included:
  - 5 IP / 1 ER vs CWS
  - 5.2 / 1 ER vs TEX
  - 6 / 1 ER at TOR
  - 5 / 7 ER at BOS
  - 5 / 1 ER vs SEA
- Rehab progression:
  - 3 innings at Triple-A on Aug. 23
  - 4 innings in a sim game Aug. 28, reported feeling very good

Mechanistic consequences:
- Jax has the clearly stronger established MLB run-prevention centre.
- Return from elbow discomfort raises workload/command uncertainty.
- A normal 6-7 inning projection is not assumed; four-to-five innings is structurally more plausible than a full deep start unless efficiency is exceptional.

## D. Current lineups

Current same-day lineup reporting:

### Mets
1. Francisco Lindor SS
2. Juan Soto DH
3. Bo Bichette 3B
4. Carson Benge RF
5. Jared Young 1B
6. Marcus Semien 2B
7. A.J. Ewing CF
8. Brett Baty LF
9. Luis Torrens C

### Rays
1. Yandy Díaz DH
2. Jonathan Aranda 1B
3. Junior Caminero 3B
4. Liam Hicks C
5. Chandler Simpson LF
6. Victor Mesa Jr. RF
7. Cedric Mullins CF
8. Richie Palacios 2B
9. Taylor Walls SS

Important role notes:
- Juan Soto is active in the Mets lineup after his recent return.
- Victor Mesa Jr. is back in the current Rays lineup after hamstring rehab.
- Junior Caminero enters with a long current hitting streak and 37 HR in the current source.
- MLB's own lineup page lagged and still displayed TBD; current same-day local gameday lineups are therefore used with a source-status note.

## E. Current offense

### Mets — L10
- **3.2 runs/game**
- 32 runs
- .235 AVG / .288 OBP / .379 SLG / .667 OPS
- 11 HR

Interpretation:
- current scoring centre is low.
- there is still home-run power through Lindor/Soto/Bichette/Benge, but sustained baserunner creation has been weak.

### Rays — L10
- **4.2 runs/game**
- 42 runs
- .263 AVG / .325 OBP / .386 SLG / .711 OPS
- 7-3 record

Interpretation:
- higher current floor than New York.
- Rays create through both contact/efficiency and power.
- recent offense is good rather than explosive.

## F. Current series / direct matchup

First two games:
1. Mets **3-2** Rays
2. Rays **6-2** Mets

Totals:
- 5
- 8

At today's line 8.0:
- Game 1 = Under win
- Game 2 = push

Series mechanisms:
- Mets won Game 1 behind Robert Stock's 5.1 scoreless innings.
- Tampa won Game 2 as Freddy Peralta held New York down after the first inning and the Rays produced a three-run sixth.
- Current series therefore supports Tampa's superior sustained offense but also shows that eight is a meaningful ceiling/push boundary.

## G. Bullpen chain

### Rays
Recent relief run prevention is elite:
- **2.30 ERA from Aug. 23-Sep. 2**
- 82 relief innings in the retrieved team query
- 0.80 WHIP
- 24.4% K rate
- only 0.66 HR/9

This strongly supports both:
- Rays winner protection
- Under 8.0 after Jax exits

### Mets
Recent bullpen form has been better than the long-season reputation:
- approximately **3.15 relief ERA over Aug. 16-31**
- strong recent work from several arms, though isolated collapses remain
- Kodai Senga has converted five saves in five opportunities with a 1.74 ERA after moving to the closer role

The Mets bullpen is not treated as automatic failure after Hagenman.

## H. Venue / environment

Tropicana Field is a controlled indoor/fixed-roof environment.

Therefore:
- no wind-out factor
- no heat/humidity carry adjustment
- no rain interruption
- no outdoor weather variance

This removes one common source of upper-tail total volatility.

## I. Joint run tree

### Central Rays-control state
**Rays 5, Mets 2**
- Rays ML: WIN
- Mets +1.5: LOSS
- Under 8.0: WIN

Mechanism:
- Jax gives four-to-five effective innings
- elite Rays bullpen carries the back half
- Tampa gets repeated looks at Hagenman + Mets middle relief

### Close Rays state
**Rays 4, Mets 3**
- Rays ML: WIN
- Mets +1.5: WIN
- Under 8.0: WIN

### Push state
**Rays 5, Mets 3**
- Rays ML: WIN
- Mets +1.5: LOSS
- total = **8 PUSH**

### Mets upset state
**Mets 4, Rays 3**
- Rays ML: LOSS
- Mets +1.5: WIN
- Under 8.0: WIN

### Upper-tail state
**Rays 6, Mets 4** / **Rays 7, Mets 3**
- Over 8.0 wins
- Rays ML wins
- Mets cushion usually fails

## J. Total-8 component budget

For Over 8:
- 5-4
- 6-3
- 6-4
- etc.

Exactly 8 is a push:
- 5-3
- 6-2

Under wins at 7 or fewer:
- 4-3
- 5-2
- 4-2
- 3-2

Current descriptive scoring centres:
- Mets L10 = 3.2
- Rays L10 = 4.2
- simple combined descriptive centre = 7.4

That is not a model, but it locates 8.0 above the raw current scoring centre.

The Under also gets structural support from Tampa's 2.30 recent relief ERA and controlled indoor environment.

Over support:
- Hagenman's uncertain MLB length
- Jax returning from elbow IL
- both starters may hand off early, increasing middle-relief exposure

Because exactly 8 pushes, Under gains boundary protection that 8.5 would not have.

## K. Side / cushion budget

### Rays ML
Rays own the larger winner branch because:
- 83-55 vs Mets 62-77
- stronger current offense
- substantially more established starting pitcher
- stronger recent bullpen
- home last bat

Main failure:
- Jax return-state limitations plus early Mets top-order damage.

### Mets +1.5
Cashes through:
- every Mets upset
- every one-run Rays win

This row becomes strong only if the game stays compressed.

The major failure branch is Tampa exposing Hagenman early and winning 5-2 / 6-2 / 6-3.

Because the same Rays pitching structure that supports ML also suppresses Mets scoring, the cushion does not outrank the Rays winner direction.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-259-C01 — Rays ML** | **LEAN** | **MEDIUM** | Tampa has the stronger current offense, the far more established starter, elite recent relief run prevention and home last bat. Jax's elbow-return workload is the main uncertainty. |
| **2** | **P-259-C04 — Under 8.0 Runs** | **LEAN** | **MEDIUM** | Current L10 scoring centres sum to 7.4, the first two series totals were 5 and 8, Tampa's bullpen has a 2.30 recent ERA, and exactly 8 pushes. Starter-return uncertainty prevents a stronger label. |
| **3** | **P-259-C02 — Mets +1.5** | **SLIGHT LEAN / LEAN-ADJACENT** | **MEDIUM-LOW** | Covers every Mets win and close Rays victory. Low-total central branches support it, but Hagenman's uncertain exposure creates a real 2+ Tampa separation path. |
| **4** | **P-259-C03 — Over 8.0 Runs** | **FORCED RANK / weaker total direction** | **MEDIUM-LOW** | Both starters have workload uncertainty and Hagenman is making his 2026 MLB debut, so 9+ is credible. It ranks last because Tampa's bullpen, Mets' low L10 offense and the indoor environment suppress the central total. |

## M. Rank-1 conditional coherence

Rank #1 = Rays ML.

Representative Rank-1 states:
- Rays 5-2 -> Rays ML + Under
- Rays 4-3 -> Rays ML + Mets +1.5 + Under
- Rays 5-3 -> Rays ML + total push

Relations:
- Under 8.0: **COHERENT**
- Mets +1.5: **PARTIAL_OVERLAP**
- Over 8.0: **PARTIAL / upper-tail**

No structural contradiction.

## N. Potential winner

### **Tampa Bay Rays — LEAN**

Same branch mass as Rank #1:
- superior current team record and form
- better starter baseline
- materially stronger current bullpen
- deeper current run-production profile

This remains a lean rather than a strong claim because:
- Jax is returning from elbow discomfort
- Hagenman's exact MLB 2026 level is unknown
- Mets still possess substantial top-order power

## O. Final delivery
1. **Rays ML**
2. **Under 8.0 Runs**
3. **Mets +1.5**
4. **Over 8.0 Runs**

**Potential winner:** Tampa Bay Rays.

## P. Append confirmation
- Full incomplete-event sweep performed first: YES
- P-254/P-255/P-256/P-257/P-258 newly settled/retrospected: YES
- Remaining unresolved rows/events preserved: YES
- P-259 frozen pre-start: YES
- Starter identities verified: YES
- Current same-day lineups recovered with field-owner lag disclosed: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-260**


---

# Settlement / retrospective sweep before P-260 — 2026-09-03

## P-253 — El Gounah vs Al Mokawloon Al Arab — FINAL

**Verified final:** El Gounah 0-1 Al Mokawloon.  
**Halftime:** 0-1.  
**Corners:** El Gounah 8-3 Al Mokawloon = **11 total**.

| ID | Rank | Contract | Outcome |
|---|---:|---|---|
| P-253-C04 | 1 | Full Match Under 2.5 Goals | **WIN** |
| P-253-C05 | 2 | Total Corners Over 8.5 | **WIN** |
| P-253-C02 | 3 | 1H Under 0.5 Goals | **LOSS** |
| P-253-C01 | 4 | 1H Over 0.5 Goals | **WIN** |
| P-253-C03 | 5 | Full Match Over 2.5 Goals | **LOSS** |

**Potential winner — El Gounah:** **LOSS**.

### Retrospective
Process grade: **RANK-1 COMPLIANT / SIDE MISS**.

What went right:
- Rank #1 Full Under 2.5 won through the exact low-event family described pregame.
- Corners Over 8.5 also won despite the low goal total, validating the separate corner-process logic.
- The card explicitly noted that low goals do not imply low corners.
- The stronger current/H2H Under structure correctly outweighed the isolated 2-3 Mokawloon game.

What missed:
- The 1H Under lean lost to a 44th-minute penalty. The opening phase was still relatively low-event in scoring terms, but one penalty was enough to defeat the row.
- Potential winner El Gounah lost 0-1. The pregame side lean over-weighted home/unbeaten context and under-weighted Mokawloon’s transition/set-piece and penalty-winning paths.
- El Gounah had 65% possession and 20 shots but failed to convert; this reinforces the distinction between territory, chance quantity and scoreboard control.

Learning disposition:
- Reinforces existing soccer controls: territory/chance volume is not conversion, and a low total can coexist with the away side winning.
- No new fitted weight or calibration rule.

## Remaining open/provisional items
- `P-250-C05` corners — unresolved.
- `P-251-C05` corners — provisional threshold-invariant win.
- `P-252` Belfast Wolves–Edinburgh Castle Rockers — field-owner source-state defect / no verified final.
- `P-255-C05` and `P-256-C05` corner rows — unresolved pending exact provider/definition final.
- `P-259` Mets–Rays — **upcoming/not started at the sweep**.

No other newly final event required settlement before P-260.

---

# P-260 — San Francisco Giants (Landen Roupp) @ Pittsburgh Pirates (Bubba Chandler) — MLB — PREGAME

## A. Frozen identity / state

- **Canonical ID:** `P-260`
- **League:** MLB
- **Event:** San Francisco Giants @ Pittsburgh Pirates
- **Venue:** PNC Park, Pittsburgh
- **Scheduled first pitch:** 2026-09-02 18:40 EDT
- **Australia/Melbourne:** 2026-09-03 08:40 AEST
- **Cutoff:** approximately 08:22-08:30 AEST, pre-start
- **GAME-STATE:** PREGAME / SCHEDULED
- **Home last bat:** Pittsburgh
- **Method:** `MDS-2026.09.02-v3.1`
- **Algorithms:** `GFA-2` + current `SFA-BASEBALL`
- **Forecast lane:** SPORTS_ONLY / MARKET_BLIND
- **Probability:** NOT_GENERATED / NOT_PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Operator action/listed-pitcher terms:** NOT SUPPLIED / UNKNOWN_DEFINITION

### Starter-source conflict
Current MLB surfaces conflicted:
- MLB Giants probable-pitchers page: **Roupp vs Bubba Chandler**
- one MLB Pirates lineup cache: **Roupp vs Bubba Chandler**
- other MLB scoreboard/lineup caches: **Roupp vs Jared Jones**
- current CBS and same-day Giants gamethread: **Roupp vs Chandler**

Because the user supplied Chandler and multiple current sources including an MLB team probable-pitchers page support Chandler, the forecast is frozen as **Roupp vs Chandler**. The conflict remains logged; it is not erased.

## B. User-supplied slate

| ID | Contract | Ordinary completed-game region |
|---|---|---|
| `P-260-C01` | Pirates ML | Pittsburgh wins |
| `P-260-C02` | Giants +1.5 | San Francisco wins or loses by exactly one |
| `P-260-C03` | Over 9.0 runs | 10+ wins; exactly 9 pushes |
| `P-260-C04` | Under 9.0 runs | 0-8 wins; exactly 9 pushes |

C01 and C02 overlap in one-run Pittsburgh wins.  
C03/C04 share a push at exactly nine.

## C. Starting pitchers

### Landen Roupp — Giants RHP
Current line:
- 8-13
- 4.25 ERA
- 139.2 IP
- 133 K
- 66 BB
- 1.31 WHIP

August L5:
- 5 IP, 1 ER vs Arizona
- 5.1 IP, 3 ER at Cleveland
- 5.2 IP, 4 ER vs Colorado
- 5.1 IP, 1 ER vs Detroit
- 4.2 IP, 5 ER at San Diego

August total:
- 26 IP
- 14 ER
- **18 BB vs 19 K**

Mechanism:
- current walk/command shape is the main weakness;
- last start was excellent enough to preserve a real five-inning suppression branch;
- he faced Pittsburgh on May 9 and allowed only **1 ER in 4 IP**, even though the Giants bullpen later collapsed in a 13-3 loss.

### Bubba Chandler — Pirates RHP
Current line:
- 6-9
- 4.26 ERA
- 131 IP
- 117 K
- 68 BB
- 1.36 WHIP

August:
- 26.1 IP
- 9 ER
- **3.08 ERA**
- 24 K / 11 BB

Latest:
- 5.2 IP, 1 ER at San Diego
- 4 IP, 4 ER at Dodgers
- 5 IP, 2 ER vs Boston
- 6 IP, 0 ER vs Mets
- 5.2 IP, 2 ER at Milwaukee

Mechanism:
- Chandler has the better current starter centre;
- the walk rate still creates extra baserunner/cluster risk;
- San Francisco’s current left-handed core is capable of punishing mistakes.

## D. Confirmed/current lineup state

Current CBS gametracker lineup:

### Giants
Drew Gilbert; Rafael Devers; Bryce Eldridge; Turner Hill; Jung Hoo Lee; Drew Cavanaugh; Nate Furman; Shay Whitcomb; Christian Koss.

### Pirates
Spencer Horwitz; Brandon Lowe; Bryan Reynolds; Nick Gonzales; Oneil Cruz; Esmerlyn Valdez; Rafael Flores; Jake Mangum; Jared Triolo.

Key lineup observations:
- San Francisco is missing major established pieces such as Matt Chapman and Willy Adames, but its current young lineup is producing.
- Devers has 31 HR in the current source.
- Pittsburgh’s middle carries substantial left-handed power through Lowe/Cruz plus contact from Gonzales.
- The lineup strength is closer than the season records alone suggest.

## E. Current offense

### Giants L10
- **60 runs / 6.0 per game**
- .270 AVG / .355 OBP / .441 SLG / .797 OPS
- 13 HR

Recent:
- 7 at Atlanta
- 12 at Pittsburgh
- 7, 1, 6, 6, 9 in several immediately preceding games

### Pirates L10
- **36 runs / 3.6 per game**
- .227 AVG / .307 OBP / .329 SLG / .636 OPS

Recent:
- 13 vs Giants
- 5 at St. Louis
- 6 at St. Louis
- 1 at St. Louis
- 0 at San Diego

Interpretation:
- San Francisco has the hotter sustained offense.
- Pittsburgh’s 13-run opener is a genuine ceiling branch but is not treated as its new baseline.
- This is the main reason Giants +1.5 remains highly competitive despite Pittsburgh’s stronger record/home position.

## F. Current-season H2H

2026 completed meetings before P-260:
- Giants 5-2 Pirates
- Pirates 13-3 Giants
- Giants 7-6 Pirates (12 innings)
- Pirates 13-12 Giants

At the 9.0 total:
- 5-2 = Under
- 13-3 = Over
- 7-6 = Over
- 13-12 = Over

Descriptive:
- Over 9.0: **3/4**
- Pirates ML: 2/4
- Giants +1.5: the close 7-6 and other Giants wins create a substantial coverage path

Important caveat:
- two of the high-scoring meetings were driven heavily by bullpen/extra-inning or cluster states.
- H2H is contextual, not a probability.

## G. Bullpen availability / previous-night workload

The Sep. 1 game ended **Pirates 13-12** and heavily used both staffs.

### Giants previous night
- Braxton Roxby 31 pitches
- Cesar Perdomo **58 pitches / 4 IP** — effectively removes a major length option
- Trent Harris 20
- Carson Seymour 19

### Pirates previous night
- Yohan Ramírez 26
- Gregory Soto 7
- Camilo Doval 13
- Evan Sisk 22
- Luke Weaver 14
- Mason Montgomery 15

Implications:
- both bullpen trees are less clean than generic season bullpen ERA suggests;
- San Francisco’s loss of Perdomo as a long-relief bridge is especially important if Roupp is short;
- Pittsburgh still has several modest-pitch-count leverage arms that may remain usable;
- this supports Pittsburgh separation and the Over tail simultaneously.

## H. Park / weather

PNC Park current 2026 Statcast run-environment index is approximately **105**, above neutral for runs in the one-year sample; the 2024-26 rolling environment is closer to neutral/slightly above.

Current game weather:
- roughly **87-88°F**
- light/moderate wind around 8-9 mph, primarily right-to-left in the strongest current source
- low immediate rain risk in RotoWire; another weather source retained a higher scattered-storm branch
- no current likely postponement flag

Mechanistic use:
- warm air modestly supports carry/contact;
- wind is not a strong automatic HR direction;
- a delay would increase starter-hook/bullpen exposure and widen the total tail.

## I. Joint run tree

### Central close-Pirates state
**Pirates 5, Giants 4**
- Pirates ML: WIN
- Giants +1.5: WIN
- total 9 = PUSH

### Lower state
**Pirates 4, Giants 3**
- Pirates ML: WIN
- Giants +1.5: WIN
- Under 9: WIN

Mechanism:
- both starters give five competent innings;
- Chandler’s current August form holds;
- previous-night bullpen fatigue does not fully surface.

### Pittsburgh separation state
**Pirates 6, Giants 3**
- Pirates ML: WIN
- Giants +1.5: LOSS
- total 9 = PUSH

or **Pirates 7, Giants 3**
- Pirates ML WIN
- Giants +1.5 LOSS
- Over WIN

Mechanism:
- Roupp walks/traffic force an early exit;
- Giants lack their fresh long bridge;
- Pittsburgh reaches lower-leverage relief.

### Giants upset / close high state
**Giants 6, Pirates 5**
- Pirates ML: LOSS
- Giants +1.5: WIN
- Over 9: WIN

Mechanism:
- hot San Francisco offense gets to Chandler’s walk/command branch;
- Pirates’ used bullpen allows late scoring.

## J. Total-9 component budget

Over wins at 10+:
- 6-4
- 6-5
- 7-3
- etc.

Exactly 9 pushes:
- 5-4
- 6-3

Under wins at 8 or fewer:
- 4-3
- 5-3
- 4-2

Support for Over:
- Giants L10 = 6.0 R/G
- Pirates L10 = 3.6 R/G
- raw descriptive sum = 9.6
- 3/4 current-season H2Hs exceeded 9
- warm 2026 PNC environment
- both bullpens used heavily on Sep. 1
- Roupp’s current walk/command volatility

Support for Under:
- Chandler August = 3.08 ERA
- Roupp has a real suppression branch and just allowed 1 ER over 5
- PNC multi-year environment is roughly neutral
- Pittsburgh’s broader L10 offense is only 3.6 R/G
- exactly 9 pushes rather than loses

Result: **Over 9 receives only a slight edge**, not a strong call.

## K. Side / separation budget

### Pirates ML
Pittsburgh owns:
- home last bat
- better season record
- better current starter centre
- better usable bullpen-depth state after the previous-night marathon

Main failure:
- Giants offense is materially hotter and can win the game outright if Chandler’s command slips.

### Giants +1.5
Wins through:
- every Giants win
- every one-run Pirates win

Central 5-4 and 4-3 Pittsburgh states both cash the cushion.

Major failure branch:
- Roupp’s walk/traffic state + unavailable Giants length leads to 6-3 / 7-3 Pittsburgh separation.

Unlike P-258, the opponent’s current offense is not strong enough and Chandler is not dominant enough to make multi-run Pittsburgh separation the central branch. Therefore the cushion remains marginally more robust than Pirates ML.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-260-C02 — Giants +1.5** | **LEAN** | **MEDIUM** | Covers every SF win plus one-run PIT wins. Giants are scoring 6.0 R/G over L10, while PIT is at 3.6. The main failure is Roupp shortening and Pittsburgh exploiting the depleted Giants relief chain. |
| **2** | **P-260-C01 — Pirates ML** | **LEAN** | **MEDIUM** | Pittsburgh has home last bat, better season team quality, Chandler’s much stronger August form and a cleaner available relief structure. Giants’ hot offense prevents Rank #1. |
| **3** | **P-260-C03 — Over 9.0 Runs** | **SLIGHT LEAN** | **MEDIUM-LOW** | Raw current scoring centre is 9.6, 3/4 H2Hs are above 9, both bullpens were taxed, and PNC is warm/above-neutral in 2026. Chandler’s good August and the 9-run push boundary keep this below the side rows. |
| **4** | **P-260-C04 — Under 9.0 Runs** | **FORCED RANK / weaker total direction** | **MEDIUM-LOW** | 4-3/5-3 states remain credible, especially if Chandler continues current form. It ranks last because recent SF offense, bullpen fatigue and current H2H tail create more ordinary 10+ paths. |

## M. Rank-1 coherence

Rank #1 = Giants +1.5.

Representative states:
- PIT 5-4 SF -> Giants +1.5 + Pirates ML; total pushes
- PIT 4-3 SF -> Giants +1.5 + Pirates ML + Under
- SF 6-5 PIT -> Giants +1.5 + Over
- PIT 6-3 SF -> Giants +1.5 loses; Pirates ML wins; total pushes

Relations:
- Pirates ML: **COHERENT / PARTIAL OVERLAP**
- Over 9: **PARTIAL OVERLAP**
- Under 9: **PARTIAL OVERLAP**

The potential winner remains Pittsburgh because the largest single winner branch still belongs to the Pirates; Giants +1.5 is broader because it adds one-run Pittsburgh wins to all Giants victories.

## N. Potential winner

### **Pittsburgh Pirates — SLIGHT LEAN**

Why:
- home last bat
- better overall record
- Chandler’s better current starter form
- San Francisco bullpen-length problem after Perdomo’s 58-pitch outing
- Pittsburgh’s deeper current lineup core

Why only slight:
- Giants offense is significantly hotter
- Chandler still has walk volatility
- yesterday’s 13-12 game showed both clubs can attack tired relief
- San Francisco can absolutely win outright if Roupp repeats his latest start

## O. Final order
1. **Giants +1.5**
2. **Pirates ML**
3. **Over 9.0 Runs**
4. **Under 9.0 Runs**

**Potential winner:** Pittsburgh Pirates — slight lean.

## P. Append confirmation
- Full incomplete-event sweep performed first: YES
- P-253 newly settled/retrospected: YES
- P-259 checked and still upcoming/not started: YES
- Starter conflict explicitly resolved and preserved: YES
- Current lineups recovered: YES
- Bullpen previous-night workload incorporated: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-261**


---

# Queue state check before P-261 — 2026-09-03

## Current unresolved / incomplete local items
- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED**.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**.
- `P-252` Belfast Wolves–Edinburgh Castle Rockers: **OPEN / FIELD-OWNER STATE DEFECT**.
- `P-255-C05` Inter Women–Wolfsburg Women corners: **UNRESOLVED**.
- `P-256-C05` PSG Women–Frankfurt Women corners: **UNRESOLVED**.
- `P-259` Mets–Rays: **UPCOMING / NOT STARTED** at the sweep.
- `P-260` Giants–Pirates: **UPCOMING / NOT STARTED** at the sweep.

No newly final item was safe to settle. No retrospective was fabricated.

---


# P-252 — Belfast Wolves vs Edinburgh Castle Rockers — FINAL SETTLEMENT / RETROSPECTIVE

**Verified final:** Edinburgh Castle Rockers **189/5 (20)** defeated Belfast Wolves **130 all out (17.1)** by **59 runs**.  
**Toss:** Belfast won the toss and elected to bowl.  
**Edinburgh powerplay:** **55 runs**.

| ID | Original rank | Contract | Settled quantity | Outcome |
|---|---:|---|---:|---|
| `P-252-C03` | 1 | Edinburgh first 6 overs Over 44.5 | 55 | **WIN** |
| `P-252-C02` | 2 | Edinburgh innings total Under 165.5 | 189 | **LOSS** |
| `P-252-C01` | 3 | Edinburgh innings total Over 165.5 | 189 | **WIN** |
| `P-252-C04` | 4 | Edinburgh first 6 overs Under 44.5 | 55 | **LOSS** |

**Potential winner — Edinburgh Castle Rockers:** **WIN**.

## P-252 retrospective

### Process grade
**RANK-1 COMPLIANT / FULL-INNINGS BRANCH UNDERWEIGHTED**

### What went right
- Rank #1 **Powerplay Over 44.5** won. The pregame mechanism was correct: Edinburgh's top-order aggression was portable across innings order, and the 44.5 threshold sat materially below their two prior completed ETPL powerplays.
- The forecast correctly distinguished powerplay scoring from full-innings scoring instead of mechanically turning a fast start into a full Over.
- Edinburgh's winner lean also won decisively, supported by the stronger phase-specific bowling attack; Boult and Curran were again decisive.
- The forecast explicitly identified the **fast PP + full 20-over ceiling state** as the strongest failure branch for the full-innings Under.

### What went wrong
- Rank #2 **Under 165.5** lost badly: Edinburgh posted 189.
- The venue first-innings baseline (5/7 below 165.5) and the pre-toss chase-censoring branch were given too much practical influence relative to Edinburgh's explosive top-order state.
- Once Belfast won the toss and fielded, the chase-censoring branch disappeared completely. The remaining state was full 20-over exposure, and Edinburgh reached 55 in the powerplay with enough wickets/resources to make 166+ structurally easy.
- The preissue card did state that toss/XIs were unresolved, but the cricket process should seek a final toss refresh from alternative current sources when the official match page lags. If that refresh resolves innings order before first ball, the full-innings rows should be re-ordered from the new branch tree.

### Learning disposition
- Reinforces the existing cricket toss-window / innings-order refresh control.
- Reinforces that **pre-toss mixture weights must collapse immediately once the toss resolves**; chase-censoring cannot continue to support an Under after the team is confirmed batting first.
- No fitted probability, calibration or forecast weight is promoted from this single result.

**P-252 status: CLOSED.**

---

# P-261 — Toronto Blue Jays (Dylan Cease) @ Cleveland Guardians (Joey Cantillo) — MLB — PREGAME

## A. Frozen identity / state

- **Canonical ID:** `P-261`
- **League:** MLB
- **Event:** Toronto Blue Jays @ Cleveland Guardians
- **Venue:** Progressive Field, Cleveland, Ohio
- **Scheduled first pitch:** 2026-09-02 18:40 EDT
- **Australia/Melbourne:** 2026-09-03 08:40 AEST
- **Frozen cutoff:** approximately 2026-09-03 08:34 AEST, before scheduled start
- **GAME-STATE:** PREGAME / SCHEDULED
- **Home last bat:** Cleveland
- **Method:** `MDS-2026.09.02-v3.1`
- **Algorithms:** `GFA-2` + `SFA-BASEBALL`
- **Forecast lane:** SPORTS_ONLY / MARKET_BLIND
- **Probability:** NOT_GENERATED / NOT_PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Operator / listed-pitcher / action terms:** NOT SUPPLIED / `UNKNOWN_DEFINITION`

## B. User-supplied slate / geometry

| ID | Contract | Ordinary completed-game settlement |
|---|---|---|
| `P-261-C01` | Blue Jays ML | Toronto wins |
| `P-261-C02` | Guardians +1.5 | Cleveland wins or loses by exactly one |
| `P-261-C03` | Over 7.0 runs | 8+ wins; exactly 7 pushes |
| `P-261-C04` | Under 7.0 runs | 0-6 wins; exactly 7 pushes |

- C03/C04 share the integer push at exactly seven.
- C01/C02 overlap in every one-run Toronto win.
- No price/market information enters the sports ranking.

## C. Confirmed probable pitchers

Official MLB probable-pitcher pages agree:

### Toronto — Dylan Cease, RHP
Current:
- 9-5
- 2.33 ERA
- 217 strikeouts
- approximately 150.1 IP
- approximately 1.05 WHIP

Latest five starts:
- vs Seattle: 6.0 IP, 1 ER, 8 K, 1 BB
- at Yankees: 6.2 IP, 1 ER, 8 K
- vs Yankees: 6.1 IP, 2 ER, 10 K
- vs Boston: 5.0 IP, 3 ER, 7 K
- at Cubs: 7.0 IP, 0 ER, 10 K

Five-start aggregate:
- 31.0 IP
- 7 ER
- **2.03 ERA**
- 43 K
- 14 BB
- 15 hits

Mechanistic interpretation:
- Cease is the strongest single run-suppression component in the game.
- The walk count still preserves baserunner/cluster risk.
- Cleveland's recent home offense is much hotter than its season RHP split, so Cease is not assumed to throw seven scoreless innings.

### Cleveland — Joey Cantillo, LHP
Current:
- 9-7
- 3.70 ERA
- 145 strikeouts
- approximately 136.1 IP
- approximately 1.45 WHIP

Latest five:
- at Angels: 6.0 IP, 2 ER, 7 BB
- at Colorado: 4.2 IP, 1 ER, 4 BB
- vs San Diego: 6.0 IP, 1 ER, 3 BB
- at White Sox: 1.0 IP, 1 ER
- vs Mets: 5.0 IP, 2 ER, 2 BB

Five-start aggregate:
- 22.2 IP
- 7 ER
- **2.78 ERA**
- 21 K
- **16 BB**

Mechanistic interpretation:
- Cantillo's recent run prevention is much better than the season 3.70 headline.
- The underlying command is unstable: 16 walks in 22.2 recent innings is a major traffic/upper-tail risk.
- Toronto's season-long weakness against left-handed pitching materially reduces the chance that every walk becomes scoring damage.

## D. Lineup / participant gate

MLB's official starting-lineup page was still exposing both lineups as `TBD` at the frozen cutoff.

The prior-day cores were:
### Toronto
Brett Bateman; Alejandro Kirk; Vladimir Guerrero Jr.; George Springer; Nathan Lukes; Kazuma Okamoto; Andrés Giménez; Ernie Clement; Myles Straw.

### Cleveland
Steven Kwan; Chase DeLauter; José Ramírez; Jo Adell; Nathaniel Lowe; Angel Martínez; Travis Bazzana; Patrick Bailey; Brayan Rocchio.

Current same-day game-thread indexing indicates Toronto again begins with Brett Bateman / George Springer / Vladimir Guerrero Jr. in the top-order area, but because the field-owner lineup page lagged, no batter-specific prop is issued and exact order-dependent exposure is capped.

## E. Current offensive regime

### Toronto — latest 10
Current retrieval:
- approximately **4.0 runs/game**
- .273 AVG
- .335 OBP
- .444 SLG
- .780 OPS
- 11 HR in the current L10 table

The freshest immediate result:
- **1 run on only 3 hits** in the 6-1 loss to Cleveland on Sep. 1
- Gavin Williams struck out 13

Critical handedness split:
- Toronto season OPS vs **left-handed pitching: approximately .643**
- .225 AVG / .296 OBP / .348 SLG

This is the strongest direct argument against a large Toronto scoring centre despite Cantillo's walk rate.

### Cleveland — latest 10
Current:
- **55-56 runs / approximately 5.5-5.6 per game**
- .278-.280 AVG
- .340-.342 OBP
- roughly .426 SLG / .766 OPS in the freshest current table
- 8-2 recent record

Season split vs RHP:
- approximately **.694 OPS**
- .240 AVG / .313 OBP / .381 SLG

Interpretation:
- Cleveland is in a much hotter short-run offensive regime than its broad season RHP numbers.
- The current form must still be shrunk because recent 11-run and 6-run games widen the mean.
- Cease is a much stronger right-handed opponent than Cleveland's generic RHP population.

## F. Bullpen chain

### Cleveland
Latest current reliever window:
- **1.19 ERA**
- 37.2 IP
- 19 hits
- 5 ER
- 49 K
- 8 BB
- **0.72 WHIP**

This is an elite short-run bullpen state and materially strengthens:
- Cleveland +1.5
- Cleveland outright comeback/hold branches
- Under 7.0 after Cantillo exits

### Toronto
Freshest reliever retrieval:
- roughly **4.75 ERA** over the last 10 team games
- 41.2 IP
- 22 ER
- 22 BB
- 8 HR

Some slightly older query windows return lower figures around 3.4-4.2; the most current retrieval is therefore treated as the higher-variance recent state rather than silently selecting the most favorable number.

Interpretation:
- Toronto's bullpen is the largest reason Cease's starter edge does **not** automatically make Blue Jays ML Rank #1.
- Cleveland's home last-bat plus late-run differential widens its winner branch if the game is tied/close after Cease exits.

## G. 2026 head-to-head continuity

Completed meetings before P-261:
1. Cleveland 8-6 Toronto — Apr. 24
2. Toronto 5-3 Cleveland — Apr. 25
3. Toronto 4-2 Cleveland — Apr. 26
4. Cleveland 6-1 Toronto — Sep. 1

Descriptive:
- outright record: **2-2**
- Guardians +1.5: wins on both Cleveland victories; loses on the two two-run Toronto wins -> **2/4**
- at total 7.0:
  - 14 runs = Over
  - 8 runs = Over
  - 6 runs = Under
  - 7 runs = Push
- Over 7: **2/4**
- Under 7: **1/4**
- Push: **1/4**

This H2H does not independently support the Under. Today's Under ranking instead comes from the specific **Cease + Cantillo recent form + Cleveland bullpen + Toronto-vs-LHP suppression** chain.

Cantillo's Apr. 25 start vs Toronto:
- 5 IP
- 6 hits
- 3 runs, only 1 earned
- 1 HR
- 1 BB
- 4 K

Toronto won 5-3 after scoring three runs against Cleveland relief in the sixth inning. That old result is informative but the current Cleveland bullpen regime is materially stronger.

## H. Environment / weather

Current Progressive Field game window:
- about **88°F** at first pitch
- wind around **8 mph**, initially crosswind/toward right field
- gusts potentially above 20 mph
- wind may become more out-to-right-center later
- rain/thunderstorm chance around **30-40%** in parts of the game window

Mechanistic treatment:
- warm air and later outfield wind modestly enlarge HR/contact tail;
- possible interruption raises starter-hook/bullpen variance;
- this is meaningful contrary evidence to the Under;
- no deterministic Over adjustment is assigned because wind is not strongly out at first pitch and rain timing is uncertain.

## I. Joint run tree

### Central Cleveland-close state
**Guardians 3, Blue Jays 2**
- Guardians +1.5: WIN
- Blue Jays ML: LOSS
- Under 7: WIN

Mechanism:
- Cease limits Cleveland but does not fully blank them;
- Cantillo walks runners but Toronto's weak LHP split prevents a large cluster;
- Cleveland's bullpen outperforms Toronto's late.

### One-run Toronto state
**Blue Jays 3, Guardians 2**
- Guardians +1.5: WIN
- Blue Jays ML: WIN
- Under 7: WIN

Mechanism:
- Cease owns six-plus innings;
- Toronto converts Cantillo traffic once;
- Toronto survives the late bullpen state.

### Push state
**Guardians 4, Blue Jays 3**
- Guardians +1.5: WIN
- Blue Jays ML: LOSS
- total = **7 PUSH**

### Toronto separation state
**Blue Jays 5, Guardians 2**
- Blue Jays ML: WIN
- Guardians +1.5: LOSS
- total = **7 PUSH**

Mechanism:
- Cantillo's walk rate finally converts into a multi-run inning;
- Cease suppresses Cleveland;
- this is the main Rank-1 cushion kill path.

### Upper-tail state
**Guardians 5, Blue Jays 3** / **Blue Jays 5, Guardians 4**
- Over 7 wins

Mechanism:
- weather/HR effect, Cantillo command failure, or a Toronto bullpen collapse pushes the game out of the low-run centre.

## J. Total-7 component budget

Under wins at 0-6:
- 3-2
- 4-2
- 3-1
- 2-1

Exactly 7 pushes:
- 4-3
- 5-2
- 6-1

Over wins at 8+:
- 5-3
- 5-4
- 6-2
- etc.

### Under support
- Cease latest-five ERA approximately 2.03
- Cantillo latest-five ERA approximately 2.78
- Toronto only .643 OPS vs LHP
- Cleveland bullpen recent ERA 1.19
- Cleveland season OPS vs RHP only about .694
- exact 7 is push protection

### Over support
- Cleveland current offense around 5.5-5.6 R/G L10
- Cantillo has 16 BB in 22.2 recent innings
- Toronto's bullpen most-current recent ERA around 4.75
- warm 88°F conditions with later outfield wind
- current H2H has 2 Over / 1 Under / 1 Push at 7

Result:
- **Under 7.0 receives a lean, not a strong call.**
- The line is low enough that the Over remains a substantial tail.

## K. Side / separation budget

### Guardians +1.5
Wins through:
- every Cleveland outright win
- every one-run Toronto win

The central 3-2 CLE and 3-2 TOR states both cash it.

Main failure:
- Cease dominates while Cantillo's walks become real runs, creating 4-2 / 5-2 Toronto.

Why the cushion still ranks first after the P-258 lesson:
- Cleveland has home last bat;
- Cleveland's current bullpen is elite;
- Toronto's offense is unusually weak against left-handed pitching;
- Cleveland is 8-2 in the current L10 regime;
- Toronto's multi-run separation branch exists but is **not** the central branch because Cantillo's recent run prevention and the bullpen behind him compress it.

### Blue Jays ML
Toronto's strongest edge is Cease, by far the best starter in the matchup.

Why it stays below the Cleveland cushion:
- Toronto must win, while +1.5 also catches one-run Toronto wins;
- Cleveland has the hotter offense, home last bat and better recent relief chain;
- Toronto's weak LHP split directly limits its path to early separation.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-261-C02 — Guardians +1.5** | **LEAN** | **MEDIUM** | Captures Cleveland wins plus one-run Toronto wins. Cleveland's 8-2 form, 5.5+ L10 scoring, elite 1.19 recent bullpen ERA and Toronto's .643 OPS vs LHP create strong margin resistance. |
| **2** | **P-261-C04 — Under 7.0 Runs** | **LEAN** | **MEDIUM** | Cease is in elite current form, Cantillo has suppressed runs recently, Cleveland's bullpen is dominant, and seven pushes. Warm/outfield conditions and Toronto relief volatility are the principal kill paths. |
| **3** | **P-261-C01 — Blue Jays ML** | **SLIGHT LEAN / LEAN-ADJACENT** | **MEDIUM-LOW** | Cease supplies the strongest individual pitching edge and Toronto can win 3-2/4-2. It stays below the cushion because Cleveland owns the superior current offense, bullpen and home-late state. |
| **4** | **P-261-C03 — Over 7.0 Runs** | **FORCED RANK / weaker total direction** | **MEDIUM-LOW** | Seven is low, Cantillo's walks and Toronto's bullpen create 8+ paths, and weather raises variance. It ranks last because the central starter-to-bullpen tree is still low scoring. |

## M. Rank-1 conditional coherence

Rank #1 = Guardians +1.5.

Representative states:
- CLE 3-2 TOR -> Guardians +1.5 + Under
- TOR 3-2 CLE -> Guardians +1.5 + Blue Jays ML + Under
- CLE 4-3 TOR -> Guardians +1.5 + total push
- TOR 5-2 CLE -> Blue Jays ML; Guardians +1.5 loses; total push

Relations:
- Under 7.0: **COHERENT**
- Blue Jays ML: **PARTIAL_OVERLAP**
- Over 7.0: **PARTIAL / upper-tail**

The P-258 separation lesson was explicitly applied: Toronto's 2+ win branch was separately budgeted rather than hidden inside a generic close-game narrative.

## N. Potential winner

### **Cleveland Guardians — SLIGHT LEAN**

Why:
- stronger current team form (8-2)
- hotter current offense
- elite recent bullpen
- home last bat
- Toronto's poor season performance against left-handed pitching

Counter:
- Dylan Cease is the strongest player-level run-prevention advantage in the game and can carry Toronto to a low-scoring win.

This is therefore a close Cleveland winner lean, not a strong favourite call.

## O. Final delivery

1. **Guardians +1.5**
2. **Under 7.0 Runs**
3. **Blue Jays ML**
4. **Over 7.0 Runs**

**Potential winner:** Cleveland Guardians — slight lean.

## P. Append confirmation

- Full incomplete-event sweep performed first: YES
- Newly safe-to-settle event: NO
- P-259/P-260 still upcoming at sweep: YES
- P-261 frozen before scheduled first pitch: YES
- Cease/Cantillo identities verified by MLB: YES
- Current official lineup lag disclosed: YES
- Starter-to-bullpen chain incorporated: YES
- Integer total push geometry incorporated: YES
- P-258 separation-budget learning explicitly applied: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-262**


---

# Queue state check before P-262 — 2026-09-03

## Current unresolved / incomplete local items
- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED**.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**.
- `P-255-C05` Inter Women–Wolfsburg Women corners: **UNRESOLVED**.
- `P-256-C05` PSG Women–Frankfurt Women corners: **UNRESOLVED**.
- `P-259` Mets–Rays: current MLB surfaces still showed **PREVIEW / NOT STARTED** at the sweep.
- `P-260` Giants–Pirates: current MLB/CBS surfaces still showed **PREVIEW / NOT STARTED** at the sweep.
- `P-261` Blue Jays–Guardians: current MLB/CBS surfaces still showed **PREVIEW / NOT STARTED** at the sweep.

`P-252` was already settled and retrospectively reviewed in the prior running-log update.

No newly final event was safe to settle. No retrospective was fabricated.

---

# P-262 — Trinbago Knight Riders vs Antigua & Barbuda Falcons — Caribbean Premier League 2026, Match 24 — PREGAME

## A. Identity / timing / target freeze

- **Canonical ID:** `P-262`
- **Sport:** Cricket
- **Competition:** Republic Bank Caribbean Premier League 2026
- **Format:** T20
- **Event:** Trinbago Knight Riders vs Antigua & Barbuda Falcons
- **Official start:** 2026-09-02 19:00 AST / 23:00 UTC
- **Australia/Melbourne:** 2026-09-03 09:00 AEST
- **Frozen cutoff:** approximately 2026-09-03 08:55 AEST, pre-start
- **GAME-STATE:** PREGAME / SCHEDULED
- **Official-current venue resolution:** **Queen's Park Oval, Port of Spain**
- **Venue conflict note:** some older/secondary CPL surfaces still displayed Brian Lara Stadium, but the current Windies Cricket fixtures page and official CPL ticketing both list Queen's Park Oval for this exact fixture. The fresher field-owner/ticketing state controls.
- **Method:** `MDS-2026.09.02-v3.1`
- **General algorithm:** `GFA-2`
- **Sport algorithm:** `SFA-CRICKET`
- **Numerical state:** `NTS-2026.09.02-v0.3` / no fit cricket model
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability:** NOT_GENERATED / NOT_PUBLISHED
- **Value:** NO VALUE DETERMINABLE
- **Operator/DLS/action/reduced-overs terms:** NOT SUPPLIED / UNKNOWN_DEFINITION

## B. Target identity

The user's phrase "Falcons 1st innings" is frozen as **Antigua & Barbuda Falcons' own batting innings**, not necessarily the first innings of the match.

Targets:
- `P262-ABF-PP6`: Falcons runs after six legal overs of their batting innings, if the phase reaches six overs under the operator/action rules.
- `P262-ABF-INN`: Falcons innings total / 20-over endpoint under exact action, DLS and innings-termination terms.

### User-supplied contracts

| ID | Contract | Ordinary settlement |
|---|---|---|
| `P-262-C01` | Falcons innings total Over 165.5 | 166+ |
| `P-262-C02` | Falcons innings total Under 165.5 | 0-165 |
| `P-262-C03` | Falcons first 6 overs Over 45.5 | 46+ |
| `P-262-C04` | Falcons first 6 overs Under 45.5 | 0-45 |

C01/C02 and C03/C04 are exact complementary pairs under ordinary full-action terms.

## C. Blocking-precondition status

| Gate | Status | Consequence |
|---|---|---|
| Format / rules | T20 / CPL verified | PASS |
| Target identity | Team innings + PP6 separately frozen | PASS |
| Toss / innings order | **UNRESOLVED at cutoff** | explicit bat-first/chase mixture required |
| Confirmed XI / phase roles | **UNRESOLVED at cutoff** | named players remain role branches |
| Strip status | **NOT FOUND AFTER SEARCH** | no pitch characteristic invented |
| Match conditions status | **OBSERVED** | weather/conditions used only mechanistically |

Under current SFA-CRICKET, near-start unresolved toss/XI/strip caps target evidence at LOW unless a direction survives the material branches.

## D. Toss / innings-order mixture

### State 1 — Falcons bat first
- Full 20-over exposure available unless all out/interruption.
- Recent ABF conventional **bat-first** innings recovered:
  - 116 all out vs Guyana
  - 155/5 vs Barbados
- Both were below 165.5.
- This state therefore supports **Under 165.5** more than the raw all-innings average suggests.

### State 2 — Falcons chase
- Target censoring becomes decision-driving.
- Falcons' high current completed chase totals include:
  - 168/8 chasing 168 vs Jamaica
  - 183/7 chasing 188 vs Saint Lucia
  - 191/7 chasing 188 vs St Kitts
  - 168/5 chasing 166 vs TKR
- All four exceeded 165.5, but each was **target-conditioned**.
- If TKR set 165 or fewer, a successful chase can terminate below 166.
- If TKR set 170-190+, the full Over becomes much stronger.

### State 3 — rain/DLS/reduced overs
- Match-window forecasts retain some passing-shower risk.
- Current official/reliable weather did not show a strong deterministic washout signal.
- Exact operator treatment is unknown.
- No reduced-overs assumption is backfilled into the normal 20-over contract.

## E. Falcons current batting evidence

### Current conventional completed innings recovered
- 168/8 vs Jamaica — chase
- 183/7 vs Saint Lucia — chase
- 191/7 vs St Kitts — chase
- 168/5 vs Trinbago — chase
- 116 all out vs Guyana — bat first
- 155/5 vs Barbados — bat first

Descriptive:
- Over 165.5: 4/6
- Under 165.5: 2/6

But the 4/6 Over count is heavily **innings-order confounded**:
- all four Overs were chases,
- both recent bat-first innings were Unders.

Therefore the raw 4/6 Over frequency is diagnostic only and is not allowed to own the innings-total rank.

## F. Falcons verified powerplay evidence

Exact/reliable current powerplay states recovered:
1. vs Jamaica: **46/1 after 6** -> Over 45.5
2. vs Saint Lucia: **65/1 after 6** -> Over
3. vs Guyana: **49/2 after 6** -> Over
4. vs Trinbago: **33 after 6** -> Under

Descriptive:
- Over 45.5: **3/4**
- Under 45.5: 1/4

Important direct-opponent counter:
- the one verified PP Under was the **reverse fixture against TKR**, where Narine and the TKR attack held the Falcons to 33.

This creates a materially stronger kill path than a generic 3/4 trend.

## G. Phase participants / role mixture

Exact XI was not confirmed at cutoff.

Current Falcons squad / recent-XI role branches include:
- Evin Lewis / Rahkeem Cornwall / Amir Jangoo / Hasan Nawaz / Karima Gore as top-order possibilities
- Moeen Ali
- Shadab Khan
- Fabian Allen / Shamar Springer
- Alzarri Joseph / Jayden Seales / Sufyan Moqim among bowling options

Current TKR squad / recent-XI role branches include:
- Colin Munro
- Sunil Narine
- Nicholas Pooran
- Alex Hales
- Justin Greaves / Jyd Goolie
- Akeal Hosein
- Usman Tariq
- Lahiru Kumara / Dominic Drakes and other pace options

Phase implication:
- Falcons have enough top-order boundary access to make 46+ plausible without needing death-over rescue.
- TKR have multiple new-ball/spin control routes; Narine and Akeal are especially relevant if deployed inside the powerplay.
- Unconfirmed phase roles prevent a higher evidence grade.

## H. Direct H2H / continuity

Most recent 2026 meeting:
- TKR 165/6
- Falcons **168/5 in 18.3 overs**
- Falcons won by 5 wickets
- Falcons powerplay: **33**
- Shadab Khan: 52* from 20 in the late chase

Current broader H2H:
- ABF have won 4 of the 6 listed recent CPL meetings.

Continuity interpretation:
- the reverse fixture is highly relevant to opponent bowling/late-finisher branches;
- it is **not** sufficient to make today's PP Under the baseline because role/venue/toss state may differ;
- the 33 PP is a direct kill path to C03 and therefore materially lowers its confidence.

## I. Current Trinbago home / venue process

Recent Trinidad/Queen's Park/Brian Lara-labelled official-result sequence has been highly variable:
- Saint Lucia 211/4; TKR 175/6
- Barbados 127/9; TKR chased 128/3
- TKR 180/6 vs Jamaica in a DLS-affected match
- Guyana 185/5 in 16; TKR 172/7 in 16

The current Windies Cricket fixture and ticketing pages place P-262 at **Queen's Park Oval**.

Implication:
- 165.5 is not an extreme venue ceiling;
- the recent Trinidad leg contains both a 127 first innings and multiple 175-211-equivalent high states;
- venue score history therefore widens rather than resolves the Falcons full-innings line.

## J. Conditions

Current Queen's Park Oval / Port of Spain match-window forecast:
- approximately 82-84°F / 28-29°C
- humid
- overcast / passing-shower possibility
- winds around 8-10 mph
- rain probability in the stronger hourly source around low-to-moderate levels rather than a strong washout signal

Mechanistic treatment:
- humidity/dew may favour skid/chasing later, but **dew is conditional**, not a winner or Over by itself;
- passing showers create DLS/shortening variance;
- no strip report was recovered, so no claim about grip, seam, grass, pace or turn is made.

## K. Powerplay 45.5 resource tree

### Over-central branch
**48-55 / 0-2**
- one boundary-positive opener survives
- 7.7-9.2 RPO is sufficient
- C03 wins

### Strong Over branch
**60+**
- Cornwall/Lewis/Jangoo-type top-order aggression
- TKR pace misses length before spin control arrives

### Under branch
**32-45 / 1-3**
- repeat of reverse-fixture Narine/new-ball control
- wickets force rebuild
- C04 wins

Threshold note:
- 45.5 is low enough that the Falcons do not need an exceptional powerplay;
- the direct opponent 33 remains the main caution.

## L. Full-innings 165.5 resource tree

### Bat-first central
Representative:
- PP 45-50 / 1-2
- middle 55-65
- death 45-50
- final **150-165**
- supports Under

### Bat-first ceiling
- PP 50-60 with wickets intact
- Moeen/Shadab/Allen-style late resources preserved
- final **170-185**
- supports Over

### Chase-censored state
- TKR target <=165
- successful Falcons chase terminates below 166
- supports Under

### High-target chase
- TKR target 170-190+
- Falcons must sustain scoring through middle/death
- supports Over; recent 183/191/168 chases demonstrate ceiling

### Collapse floor
- early wickets + TKR spin control
- 120-150
- strongly supports Under

## M. Phase-to-innings coherence

A **PP Over 45.5 does not imply innings Over 165.5**.

Example:
- Falcons 50/1 after six
- then TKR spin/control takes 3 wickets through overs 7-14
- Falcons finish 158/7

This gives:
- PP Over = WIN
- Innings Under = WIN

Conversely:
- Falcons 42/1 after six
- wickets retained
- Moeen/Shadab finish strongly
- final 175

This gives:
- PP Under = WIN
- Innings Over = WIN

The two targets remain separate conditional distributions, as required by the active cricket rules.

## N. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-262-C03 — Falcons first 6 overs Over 45.5** | **LEAN** | **LOW** | Three of four verified current ABF powerplays cleared the line (46, 65, 49). The threshold requires only 7.67 RPO. The exact TKR reverse fixture held ABF to 33, so the direct-opponent kill path keeps evidence capped. |
| **2** | **P-262-C02 — Falcons innings total Under 165.5** | **SLIGHT LEAN** | **LOW** | Both recovered recent ABF bat-first innings were below 166 (116, 155), while a second-innings state gains chase-censoring support whenever TKR set <=165. The major failure branch is a 170+ TKR target or a wickets-in-hand ABF first innings. |
| **3** | **P-262-C01 — Falcons innings total Over 165.5** | **FORCED RANK / LEAN-ADJACENT** | **LOW** | ABF have cleared 165.5 in four conventional completed chases (168, 183, 191, 168), and the recent Trinidad scoring environment has multiple high states. It stays below Under because all four Overs were target-conditioned chases and both recent ABF bat-first totals were Under. |
| **4** | **P-262-C04 — Falcons first 6 overs Under 45.5** | **FORCED RANK / weaker phase direction** | **LOW** | The reverse fixture's 33-run PP proves TKR can suppress this top order, especially through Narine/new-ball control. It ranks last because 3/4 verified current Falcons PPs were 46+, including two substantially above the threshold. |

## O. Rank-1 conditional coherence

Rank #1 = Falcons PP Over 45.5.

- Innings Under 165.5: **COHERENT / PARTIAL** — fast start + middle-over spin squeeze or chase censoring.
- Innings Over 165.5: **COHERENT / PARTIAL** — fast start + retained wickets/death acceleration.
- PP Under 45.5: **DISJOINT** exact complement.

No full-innings direction is mechanically derived from the PP pick.

## P. Potential winner

### **Antigua & Barbuda Falcons — SLIGHT LEAN**

Why:
- Falcons won the reverse fixture this season by five wickets.
- Current recent H2H listing favours ABF 4-2.
- Their batting depth has repeatedly rescued difficult states through Moeen/Shadab and lower-middle resources.
- Their bowling attack has multiple phase-specific options through Alzarri, Seales, Shadab, Sufyan/Joshua James-type roles.

Counterweights:
- TKR are at home.
- Munro/Narine/Pooran/Hales give TKR a higher explosive top-order ceiling.
- TKR's spin attack can reproduce the 33-run powerplay suppression from the reverse fixture.
- Toss and final XIs were unresolved at cutoff.

Winner direction is therefore only a slight Falcons lean.

## Q. Final delivery

1. **Falcons first 6 overs — Over 45.5**
2. **Falcons innings total — Under 165.5**
3. **Falcons innings total — Over 165.5**
4. **Falcons first 6 overs — Under 45.5**

**Potential winner:** Antigua & Barbuda Falcons — slight lean.

## R. Append confirmation

- Full unresolved-event sweep performed first: YES
- Newly safe-to-settle event: NO
- Current active Drive cricket rules re-read: YES
- Official venue conflict resolved using fresher current field-owner/ticketing evidence: YES
- Toss at cutoff: UNRESOLVED
- XI at cutoff: UNRESOLVED
- Strip status: NOT FOUND AFTER SEARCH
- Match conditions: OBSERVED
- Bat-first / chase-censored mixture explicitly modelled: YES
- Phase-to-innings independence applied: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-263**


---

# P-263 — Jaime Faria vs Carlos Alcaraz — 2026 US Open Men's Singles Round 2 — PREGAME

## Queue state check
- P-250-C05: unresolved.
- P-251-C05: provisional threshold-invariant win.
- P-255-C05 and P-256-C05: unresolved.
- P-259 Mets–Rays: live; no settlement.
- P-260 Giants–Pirates: open / final not verified.
- P-261 Blue Jays–Guardians: live; no settlement.
- P-262 TKR–Antigua & Barbuda Falcons: delayed / no final verified.
- No newly final event was safe to settle; no retrospective was fabricated.

## Identity / state
- Canonical ID: P-263
- Event: 2026 US Open Men's Singles, Round 2 (R64)
- Match: Jaime Faria vs Carlos Alcaraz
- Venue: Arthur Ashe Stadium
- Surface: hard
- Format: best of five
- State at cutoff: UPCOMING / NOT STARTED
- Expected start: around 21:00 EDT Sep 2 / ~11:00 AEST Sep 3
- Method: MDS-2026.09.02-v3.1 / GFA-2 / SFA-TENNIS
- Operator retirement terms: UNKNOWN_DEFINITION
- Probability: NOT_GENERATED / NOT_PUBLISHED
- Value: NO VALUE DETERMINABLE

## Contracts
| ID | Contract |
|---|---|
| P-263-C01 | Faria +7.5 games |
| P-263-C02 | Alcaraz -7.5 games |
| P-263-C03 | Over 31.5 total games |
| P-263-C04 | Under 31.5 total games |

## Current regime
### Alcaraz
- No. 3 ranking / No. 2 US Open seed.
- Returned after 139 days away with a right-wrist injury.
- Beat Safiullin 6-4, 6-4, 6-4 in R1 and reported feeling pain-free.
- 2026 hard record in current provider: 18-2.
- Broad 2026 profile: ~88.9% hold, ~32.2% break.
- R1 serve speed was still managed below his normal peak, so current-state uncertainty remains.

### Faria
- Around No. 72, career high No. 70.
- Beat Brooksby 6-3, 7-6(4), 4-6, 1-6, 6-2 in 3h43m.
- Recent Cincinnati run: wins over Brooksby, Ben Shelton and Adam Walton; loss to Musetti.
- 2026 hard record in current provider: 5-3.
- Broad 2026 profile: ~77% hold, ~23% break.
- Extra rest day partly offsets the five-set R1 workload.

## H2H
- Current structured H2H: 0-0.

## Best-of-five qualitative set-count mixture
Ordinal weights only, not probabilities:
- 3 sets = 6
- 4 sets = 3
- 5 sets = 1

## Core branches
- Alcaraz 6-3, 6-4, 6-2 -> 27 games, +9 margin: Alcaraz -7.5 + Under 31.5.
- Alcaraz 6-4, 6-4, 6-3 -> 29 games, +7 margin: Faria +7.5 + Under 31.5.
- Alcaraz 6-3, 4-6, 6-3, 6-4 -> 34 games, +4 margin: Faria +7.5 + Over 31.5.
- Faria upset branches are retained but materially smaller.

## Separation budget
Alcaraz -7.5 needs 8+ net games. A straight-set win alone is not enough:
- 6-4, 6-4, 6-4 = +6 -> Faria covers.
- 6-3, 6-4, 6-3 = +8 -> Alcaraz covers.
The favourite handicap therefore requires repeated return pressure and at least one real separation set.

## Total budget
Under 31.5 is strongest in ordinary 3-0 Alcaraz wins:
- 6-3, 6-4, 6-2 = 27
- 6-4, 6-4, 6-4 = 30
Over can still hit in straight sets if sets are very close:
- 7-5, 6-4, 6-4 = 32
Most ordinary 4- and 5-set states support the Over.

## Ranked forecast
| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| 1 | Under 31.5 total games | LEAN | MEDIUM |
| 2 | Alcaraz -7.5 games | SLIGHT LEAN | MEDIUM-LOW |
| 3 | Faria +7.5 games | FORCED RANK / LEAN-ADJACENT | MEDIUM-LOW |
| 4 | Over 31.5 total games | FORCED RANK / weaker total direction | MEDIUM-LOW |

## Potential winner
**Carlos Alcaraz — LEAN**

## Final order
1. Under 31.5 total games
2. Alcaraz -7.5 games
3. Faria +7.5 games
4. Over 31.5 total games

## Append confirmation
- Queue sweep first: YES
- Newly safe-to-settle event: NO
- Official round/state verified: YES
- Status refreshed pre-issue: UPCOMING
- H2H continuity: 0-0
- Best-of-five mixture: YES
- Handicap separation budget: YES
- Retirement terms: UNKNOWN_DEFINITION
- Drive modified: NO
- Numerical probability generated: NO
- NEXT CANONICAL ID: P-264


---

# P-264 — Chicago White Sox (Davis Martin) @ Houston Astros (Hayden Wesneski) — MLB — PREGAME

## Queue / state check
- P-259 Mets–Rays: live, not final.
- P-260 Giants–Pirates: live/open, not final.
- P-261 Blue Jays–Guardians: live, not final.
- P-262 TKR–Falcons: in progress, not final.
- P-263 Faria–Alcaraz: upcoming.
- Existing unresolved corner-definition rows remain open/provisional.
- No newly final event was safe to settle or retrospect.

## Live-state hard gate
User labelled this match live, but MLB field-owner state at freeze was **PREGAME / PREVIEW**.
- Scheduled first pitch: 2026-09-02 20:10 EDT / 2026-09-03 10:10 AEST.
- Query time: about 10:03 AEST.
- Venue: Daikin Park.
- Home last bat: Houston.
- Official MLB event page linked Davis Martin vs Hayden Wesneski.
- Official batting orders were still TBD at the freeze.
- Operator/action/listed-pitcher terms: UNKNOWN_DEFINITION.
- Method: MDS-2026.09.02-v3.1 / GFA-2 / SFA-BASEBALL.
- Numerical model: not fit / not validated.

## Contracts
1. Astros ML
2. White Sox +1.5
3. Over 8.5
4. Under 8.5

## Starter state
### Davis Martin
- 9-6, 4.32 ERA, 111 K.
- Activated from 15-day IL on Sep. 2; first MLB start since Aug. 13.
- Aug. 27 rehab: 5 scoreless innings.
- Immediate pre-IL MLB starts were volatile, including 9 ER at Boston and 3 ER in 2 IP vs Cincinnati.
- Current mixture: competent 5-inning return / ordinary 3-4 run state / early-hook-contact-HR tail.

### Hayden Wesneski
- 4-1, 3.86 ERA, ~1.19 WHIP.
- Seventh 2026 start after Tommy John surgery.
- Latest two starts: 10 IP, 1 ER combined.
- One recent 5-ER start vs Seattle preserves downside.
- Current centre is better than Martin's, but a roughly 5-inning state remains more plausible than assuming a deep 7-inning start.

## Offense
### White Sox L10
- 49 runs, 4.9 R/G
- .239/.352/.382, .734 OPS
- 6-4
- season OPS vs RHP ~.721-.722

### Astros L10
- 44 runs, 4.4 R/G
- .207/.289/.385, .674 OPS
- 5-5
- season OPS vs RHP ~.728

Chicago has the hotter/steadier current offense. Houston retains greater HR ceiling through Yordan Alvarez / Isaac Paredes but has struggled to sustain baserunners.

## Bullpen
Houston preserved its primary leverage group in the 5-1 loss. Hader, Abreu, Okert, Blubaugh and De Los Santos carried roughly a 1.06 ERA over 59.1 August innings in current reporting. Hader was 21-for-21 in saves with an 18-game scoreless streak.

Chicago's recent relief ERA is window-sensitive (~3.6 to ~4.4 depending exact current window), so no single cherry-picked number controls.

## Joint early-hook branch
Both starters have exposure uncertainty:
- Martin is returning from IL.
- Wesneski is in a limited post-TJS starting season.

If both exit after ~4 innings, the upper tail rises. However, a short Wesneski start is not automatically an Over because Houston's strongest relievers are rested. Houston's cold offense also keeps the central run tree below nine.

## Central game tree
- HOU 4-3 CWS -> Under, Astros ML, CWS +1.5
- HOU 5-3 CWS -> Under, Astros ML
- CWS 4-3 HOU -> Under, CWS +1.5
- HOU 6-3 CWS -> Over, Astros ML
- HOU 5-4 CWS / CWS 5-4 HOU -> Over, CWS +1.5

## Ranked forecast
| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| 1 | Under 8.5 Runs | SLIGHT LEAN | MEDIUM-LOW |
| 2 | White Sox +1.5 | SLIGHT LEAN | MEDIUM-LOW |
| 3 | Astros ML | LEAN-ADJACENT / FORCED RANK | MEDIUM-LOW |
| 4 | Over 8.5 Runs | FORCED RANK / weaker total direction | MEDIUM-LOW |

## Potential winner
**Houston Astros — SLIGHT LEAN**

Reason: better current starter centre, rested leverage bullpen and home last bat. Confidence is capped by Chicago's better record/run differential/recent offense and Houston's weak current batting form.

## Final order
1. Under 8.5 Runs
2. White Sox +1.5
3. Astros ML
4. Over 8.5 Runs

**Next canonical ID: P-265**


---

# Queue state check before P-265 — 2026-09-03

## Current unresolved / incomplete local items
- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED**.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**.
- `P-255-C05` Inter Women–Wolfsburg Women corners: **UNRESOLVED**.
- `P-256-C05` PSG Women–Frankfurt Women corners: **UNRESOLVED**.
- `P-259` Mets–Rays: **LIVE / no verified final at the sweep**.
- `P-260` Giants–Pirates: **LIVE / no verified final at the sweep**.
- `P-261` Blue Jays–Guardians: **LIVE / no verified final at the sweep**.
- `P-262` TKR–Antigua & Barbuda Falcons: **IN PROGRESS / no verified final at the sweep**.
- `P-263` Faria–Alcaraz: **UPCOMING / not started at the sweep**.
- `P-264` White Sox–Astros: **UPCOMING / not started at the sweep**.

No newly final event was safe to settle. No retrospective was fabricated.

---

# P-265 — Toluca vs Club León — Leagues Cup 2026 Semifinal — PREGAME

## A. Identity / endpoint freeze
- **Canonical ID:** `P-265`
- **Competition:** Leagues Cup 2026
- **Stage:** Semifinal, single elimination
- **Event:** Toluca FC vs Club León
- **Venue:** Shell Energy Stadium, Houston, Texas — neutral site
- **Kickoff:** 2026-09-02 20:00 Houston / 21:00 ET
- **Australia/Melbourne:** 2026-09-03 11:00 AEST
- **Frozen state:** PREGAME / SCHEDULED
- **Knockout rule:** tied after 90 minutes -> direct penalty shootout; no extra time
- **Goal rows:** regulation 90 minutes including stoppage
- **Potential winner endpoint:** **TO ADVANCE TO THE FINAL**
- **Method:** MDS-2026.09.02-v3.1 / GFA-2 / SFA-SOCCER
- **Numerical model:** not fit / not validated
- **Operator / derivative provider:** not supplied
- **Probability:** NOT_GENERATED / NOT_PUBLISHED
- **Value:** NO VALUE DETERMINABLE

## B. Candidate slate
| ID | Contract | Ordinary settlement |
|---|---|---|
| `P-265-C01` | 1H Over 0.5 Goals | 1+ first-half goals |
| `P-265-C02` | 1H Under 0.5 Goals | 0-0 HT |
| `P-265-C03` | Full Match Over 2.5 Goals | 3+ regulation goals |
| `P-265-C04` | Full Match Under 2.5 Goals | 0-2 regulation goals |
| `P-265-C05` | Total Corners Over 8.5 | 9+ regulation corners under the research-provider convention |

C01/C02 and C03/C04 are exact complementary pairs.  
C05 is a separate derivative process. Exact operator/provider definition is absent, so C05 cannot receive `LEAN`/`SUPPORTED` under active SFA-SOCCER even if it ranks first by sporting likelihood.

## C. Participant gate
A field-owner confirmed XI was not recovered before the frozen cutoff.

Current same-day sources broadly agree on these attacking/structural cores:
- Toluca: Hugo González in goal; Alexis Vega, Helinho and Federico Viñas among the principal attacking options; Franco Romero / Nicolás Castro-type midfield control.
- León: Óscar García in goal; Diber Cambindo as the reference striker with Fernando Beltrán, Rodrigo Echeverría, Ismael Díaz / Juan Domínguez / Daniel Arcila-type support.

Current aggregation also lists material Toluca absences around Paulinho, Marcel Ruiz, Santiago Simón and Iván López, and León absences including Ángel Estrada / Edgar Guerra, but because this was not field-owner-confirmed at freeze these are retained as provisional availability states.

**Consequence:** winner/side confidence is capped; no player prop is issued.

## D. Tournament form

### Toluca — Leagues Cup 2026
- 3-0 Seattle
- 0-1 LAFC
- 3-1 FC Dallas
- 2-0 Austin FC

Summary:
- 3 wins, 1 loss
- 8 GF, 2 GA
- Full Over 2.5: 2/4
- Full Under 2.5: 2/4

Quarterfinal process:
- Toluca beat Austin 2-0.
- Austin went to 10 men in the 40th minute.
- Toluca finished with 25 shots, 9 on target.
- Austin did not record a shot on target.
- The red-card distortion prevents treating that defensive dominance as ordinary 11v11 baseline.

### León — Leagues Cup 2026
- 1-0 Nashville
- 2-1 Orlando
- 3-2 Inter Miami
- 3-0 Real Salt Lake

Summary:
- perfect 4-0 record
- 9 GF, 3 GA
- Full Over 2.5: 3/4
- scored in all four
- clean sheets in 2/4

Current Leagues Cup form therefore supports León's attack more consistently than a pure low-event semifinal prior would.

## E. Current all-competition L5

### Toluca
- 4-0 Juárez — HT 2-0 — corners 8
- 2-0 Austin — HT 0-0 — corners 14
- 2-1 Querétaro — HT 0-0 — corners 13
- 0-0 Atlante — HT 0-0 — corners 15
- 3-1 FC Dallas — HT 2-1 — corners 9

Descriptive:
- GF/game: 2.2
- GA/game: 0.4
- 1H Over 0.5: 2/5
- Full Over 2.5: 3/5
- Corners Over 8.5: 4/5

### León
- 1-1 Atlante — HT 0-0 — corners 6
- 3-0 Real Salt Lake — HT 1-0 — corners 11
- 2-0 Monterrey — HT 1-0 — corners 13
- 2-1 Necaxa — HT 0-1 — corners 10
- 3-2 Inter Miami — HT 0-1 from León perspective / 1-0 match HT — corners 15

Descriptive:
- GF/game: 2.2
- GA/game: 0.8
- 1H Over 0.5: 4/5
- Full Over 2.5: 3/5
- Corners Over 8.5: 4/5

Combined L5:
- 1H Over 0.5: 6/10
- Full Over 2.5: 6/10
- Corners Over 8.5: 8/10

Small descriptive sample; not a probability.

## F. H2H continuity

Recent five listed meetings:
- Toluca 4-1 León — Apr 2026
- León 2-4 Toluca — Oct 2025
- León 3-3 Toluca — Feb 2025
- Toluca 2-2 León — Nov 2024
- Toluca 4-1 León — Feb 2024

Current continuity summary:
- Toluca unbeaten in the last five: 3 wins, 2 draws
- all five cleared 2.5 goals
- current broader H2H source lists approximately 3.9 total goals per meeting
- the latest Apr 2026 match produced 9 corners
- older meetings retain lower weight because current rosters/coaches have changed

The recent H2H strongly supports the Over tail, but it is not allowed to override the current defensive regimes by itself.

## G. Early-goal reconciliation

### Over support
- León 1H Over in 4/5 current matches
- combined current L5 = 6/10
- recent H2Hs repeatedly produced first-half scoring
- latest April meeting had Toluca score in the 5th minute
- October 2025 meeting was 1-1 at HT
- February 2025 meeting had two León goals before halftime

### Under support
- Toluca were 0-0 at HT in 3 of their latest 5
- Toluca's quarterfinal stayed 0-0 through the first half despite a 40' Austin red
- semifinal single-elimination state plus direct penalties can preserve a tactical draw band
- official Toluca pre-match comments emphasized defending transitions and controlling León's counterattack threat

Result:
**1H Over 0.5 has a slight edge, not a strong one.**

## H. Full-total process

### Over-supporting mechanisms
- León have scored 9 in four Leagues Cup matches and cleared 2.5 in 3/4.
- Both teams are at 2.2 GF/game over current L5.
- Both teams clear 2.5 in 60% of current L5.
- The latest five H2Hs all cleared 2.5.
- First goal by either side creates a trailing-state chase because there is no second leg.

### Under-supporting mechanisms
- Toluca have conceded only 2 goals across four Leagues Cup matches.
- Toluca current L5 GA = 0.4.
- León have two tournament clean sheets and only three goals conceded in four.
- If level late, neither team needs to force reckless attacks because direct penalties are available.
- Neutral-site semifinal reduces ordinary home-pressure assumptions.

Central regulation families:
- 2-1 Toluca
- 1-1
- 2-1 León
- 2-0 Toluca / 1-0 either way as lower branch

Over therefore receives only a **slight** regulation edge.

## I. Corner process

Direct current target evidence:
- Toluca recent totals: 8, 14, 13, 15, 9 -> **4/5 Over 8.5**
- León recent totals: 6, 11, 13, 10, 15 -> **4/5 Over 8.5**
- combined: **8/10 Over 8.5**

Current provider process summaries:
- Toluca corners for ~5.8/game, against ~6.0
- León corners for ~4.2/game, against ~6.8
- broader H2H average ~9.7 total corners

Mechanistic support:
- León can generate transition attacks without needing high possession.
- Toluca's wide attack through Vega/Helinho and fullback width creates crossing/end-line entries.
- Either first goal raises the trailing side's crossing, clearance and set-play exposure.
- A 1-1 / 2-0 match can still clear 8.5 corners; corner and goal processes remain separate.

Kill path:
- efficient central finishing with few blocks/clearances;
- long tactical midfield phases;
- early lead followed by successful leading-state control.

**Definition cap:** exact sportsbook/provider corner settlement was not supplied. C05 is `FORCED RANK / MEDIUM-LOW`, not a formal LEAN.

## J. Conditions

Houston match-window forecasts are source-conflicted:
- broadly hot/humid, roughly low-to-mid 80s °F near kickoff
- SSE winds around 10 mph
- some nearby stations show only modest rain probability
- other local stations flag a significant evening thunderstorm/heavy-rain branch

Mechanistic treatment:
- weather widens delay/wet-surface uncertainty;
- rain can alter passing/crossing/surface speed in multiple directions;
- no deterministic Over/Under direction is assigned;
- if delayed, participant warm-up and surface state should be rechecked before live use.

## K. Knockout state

Leagues Cup knockout rule:
- single elimination
- tied after regulation -> direct penalty shootout
- **no extra time**

Consequences:
- regulation totals stop after 90 + stoppage.
- potential winner-to-advance includes penalties.
- draw at 90 is a substantial state and does not require either side to chase indefinitely late.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-265-C05 — Total Corners Over 8.5** | **FORCED RANK** | **MEDIUM-LOW** | 8/10 recent combined matches clear 8.5, direct team for/conceded corner rates imply double-digit event exposure, and either first-goal state raises chase-width pressure. Provider definition missing prevents LEAN label. |
| **2** | **P-265-C03 — Full Match Over 2.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | Both are at 2.2 GF/game L5, León cleared 2.5 in 3/4 Leagues Cup matches, and the latest five H2Hs all exceeded 2.5. Toluca's current defence and direct-penalty draw band prevent a stronger call. |
| **3** | **P-265-C01 — 1H Over 0.5 Goals** | **SLIGHT LEAN** | **MEDIUM-LOW** | León is 4/5 current 1H Over and recent H2H has strong early-goal continuity. Toluca's three 0-0 HTs in L5 and tactical semifinal opening keep this below the full Over. |
| **4** | **P-265-C04 — Full Match Under 2.5 Goals** | **LEAN-ADJACENT / FORCED RANK** | **MEDIUM-LOW** | Toluca's defensive regime and direct-penalty structure create 0-0/1-0/1-1/2-0 states. It stays below Over because León's tournament attack and H2H conversion tail are stronger. |
| **5** | **P-265-C02 — 1H Under 0.5 Goals** | **WEAKER DIRECTION** | **MEDIUM-LOW** | 0-0 HT is credible through Toluca control and semifinal caution, but current León early scoring plus recent H2H makes the no-goal first half narrower. |

## M. Rank-1 coherence

Rank #1 = Corners Over 8.5.

- Full Over 2.5: `COHERENT / PARTIAL`
- 1H Over 0.5: `COHERENT / PARTIAL`
- Full Under 2.5: `COHERENT / PARTIAL` because high corners can coexist with low conversion
- 1H Under 0.5: `COHERENT / PARTIAL` because a slow first half can still produce late corner pressure

No row is structurally disjoint from the corner thesis.

## N. Potential winner endpoint

### **Toluca to advance — SLIGHT LEAN**

Supporting:
- unbeaten in last five H2Hs vs León (3W, 2D)
- stronger current defensive L5 profile (0.4 GA/game)
- deeper demonstrated knockout experience
- recent 2-0 quarterfinal and 4-0 league win
- Toluca rotated in the Juárez match, reducing the raw two-day-rest concern

Counter:
- León are perfect 4-0 in Leagues Cup and have scored in every tournament match
- León have more rest before the semifinal
- neutral venue reduces Toluca's ordinary home advantage
- direct penalties make the draw/coin-flip advancement branch material

Regulation winner is therefore weaker than the advancement call; no strong 90-minute side is published.

## O. Final delivery
1. **Total Corners Over 8.5**
2. **Full Match Over 2.5 Goals**
3. **1st Half Over 0.5 Goals**
4. **Full Match Under 2.5 Goals**
5. **1st Half Under 0.5 Goals**

**Potential winner endpoint:** Toluca to advance — slight lean.

## P. Append confirmation
- Full unresolved-event sweep performed first: YES
- Newly safe-to-settle event: NO
- Competition/stage/neutral venue verified by Leagues Cup: YES
- Direct-penalty/no-extra-time rule verified: YES
- Current field-owner confirmed XI recovered: NO
- Participant uncertainty preserved/capped: YES
- Current L5 and direct corner process constructed: YES
- Early-goal reconciliation performed: YES
- Corners modeled separately from goals: YES
- Weather conflict preserved rather than silently reconciled: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-266**


---

# Queue state check before P-266 — 2026-09-03

## Current incomplete / unresolved local items

- `P-250-C05` Yunnan–Chongqing corners: **UNRESOLVED**.
- `P-251-C05` Sassuolo–Frosinone corners: **PROVISIONAL WIN / threshold-invariant**.
- `P-255-C05` Inter Women–Wolfsburg Women corners: **UNRESOLVED**.
- `P-256-C05` PSG Women–Frankfurt Women corners: **UNRESOLVED**.
- `P-259` Mets–Rays: **LIVE** at sweep; official game story had New York 3-0 in the first inning, therefore no settlement.
- `P-260` Giants–Pirates: **LIVE / no verified final** at sweep.
- `P-261` Blue Jays–Guardians: **LIVE / no verified final** at sweep.
- `P-262` TKR–Antigua & Barbuda Falcons: **IN PROGRESS / no verified final** at sweep.
- `P-263` Faria–Alcaraz: **UPCOMING / not final** at sweep.
- `P-264` White Sox–Astros: **LIVE / no verified final for the current P-264 event**; web results also contained a completed 5-1 prior game, which is preserved as a separate event rather than mis-settled onto P-264.
- `P-265` Toluca–León: **LIVE / just-started semifinal, no final** at sweep.

No newly final local event was safe to settle. No retrospective was fabricated.

---

# P-266 — New York Yankees (Cam Schlittler) @ Los Angeles Angels (Reid Detmers) — MLB — PREGAME

## A. Frozen identity / state

- **Canonical ID:** `P-266`
- **League:** MLB
- **Event:** New York Yankees @ Los Angeles Angels
- **Venue:** Angel Stadium, Anaheim, California
- **Scheduled first pitch:** 2026-09-02 21:38 EDT / 18:38 PDT
- **Australia/Melbourne:** 2026-09-03 11:38 AEST
- **Research freeze:** approximately 2026-09-03 11:20 AEST
- **GAME-STATE:** PREGAME / PREVIEW
- **Home last bat:** Los Angeles Angels
- **Official probable starters:** Cam Schlittler (NYY RHP) vs Reid Detmers (LAA LHP)
- **Official batting orders at freeze:** MLB page still showed `TBD`
- **Current secondary lineups:** available and used only as lineup-mixture evidence, not field-owner-confirmed
- **Method:** `MDS-2026.09.02-v3.1`
- **Algorithms:** `GFA-2` + `SFA-BASEBALL`
- **Numerical state:** `NTS-2026.09.02-v0.3`; no fitted/validated baseball model
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Probability:** `NOT_GENERATED / NOT_PUBLISHED`
- **Value:** `NO VALUE DETERMINABLE`
- **Operator / action / listed-pitcher terms:** not supplied / `UNKNOWN_DEFINITION`

## B. Supplied contracts / geometry

| ID | Contract | Ordinary settlement |
|---|---|---|
| `P-266-C01` | Yankees -1.5 | NYY wins by 2+ |
| `P-266-C02` | Angels +1.5 | LAA wins or loses by exactly 1 |
| `P-266-C03` | Over 6.5 runs | 7+ combined runs |
| `P-266-C04` | Under 6.5 runs | 0-6 combined runs |

- C01/C02 are exact half-run complements.
- C03/C04 are exact half-run complements.
- A low total does **not** imply a close margin; 3-0 / 4-1 / 4-2 separation branches are explicitly retained.

## C. Starting-pitcher state

### Cam Schlittler — Yankees RHP

Current official/current-preview line:
- 12-6
- **2.09 ERA**
- 163.2 IP
- **201 strikeouts**
- approximately 0.97 WHIP in current preview data

August:
- 5 starts
- 27.0 IP
- 7 ER
- **2.33 ERA**
- 36 K
- 16 BB
- 2 HR

Latest three:
- 5.2 IP, 0 ER vs Boston
- 6.0 IP, 1 ER vs Toronto
- 5.1 IP, 1 ER at Toronto

Current same-day preview notes:
- **2-0, 1.13 ERA over his latest four**
- road ERA approximately **1.14**
- first career start against the Angels

Mechanistic interpretation:
- Schlittler is the strongest single run-suppression component in this game.
- His fastball/curveball power profile creates a meaningful Angels 0-2 run floor branch.
- Walks remain the main cluster risk: 16 BB in August and 5 in the most recent Boston start.
- No direct Angels H2H starter history exists, so no opponent ownership is inferred.

### Reid Detmers — Angels LHP

Current:
- 4-8
- **3.54 ERA**
- 155 IP
- **174 K**
- approximately 1.07 WHIP

August:
- 5 starts
- 30 IP
- **5 ER**
- **1.50 ERA**
- 29 K
- 6 BB
- 2 HR

Latest four:
- 6 IP, 1 ER vs Philadelphia
- 6 IP, 0 ER at Texas
- 8 IP, 0 ER vs Kansas City
- 6 IP, 1 ER vs Texas

This is **26 innings / 2 earned runs** across the four-start run.

Current preview also reports:
- approximately **1.55 ERA over his last eight starts**
- career against Yankees: 1-0, approximately **0.59 ERA** in six appearances/two starts
- April 14, 2026: **7 IP, 1 R, 4 H, 0 BB, 9 K** against New York

Mechanistic interpretation:
- Detmers' current regime is dramatically stronger than his 3.54 season ERA.
- The direct April 2026 start is continuity-relevant because it is same season and same opponent, but one start is not treated as ownership.
- His slider/left-handed look is materially relevant to a Yankees lineup that has been only around league-average against LHP rather than elite.

## D. Current lineup / availability state

MLB's field-owner lineup page remained `TBD`, so exact slot-PA exposures are capped.

Current same-day secondary reporting listed:

### Yankees
1. Paul Goldschmidt 1B
2. Cody Bellinger LF
3. Heliot Ramos RF
4. Ben Rice DH
5. Amed Rosario 3B
6. Spencer Jones CF
7. Jose Caballero SS
8. Jazz Chisholm Jr. 2B
9. Ali Sánchez C

### Angels
1. Zach Neto SS
2. Mike Trout CF
3. Wade Meckler LF
4. Vaughn Grissom 1B
5. Moisés Ballesteros DH
6. Christian Moore 2B
7. Josh Lowe RF
8. Oswald Peraza 3B
9. Travis d'Arnaud C

Material Yankees availability:
- **Aaron Judge remains out** while progressing through rib-injury rehab.
- Giancarlo Stanton is also unavailable in the current roster/injury context.
- Yankees have intentionally introduced more right-handed bats against Detmers, including Goldschmidt/Rosario/Ramos-type exposure.

Participant implication:
- New York's current offense is hot, but its absolute ceiling is lower than a full Judge/Stanton roster.
- No player prop is added because the official lineup freeze was incomplete.

## E. Current offensive form

### Yankees — L10
Fresh current StatMuse window:
- **59 runs / 5.9 R/G**
- .288 AVG
- .347 OBP
- .457 SLG
- **.804 OPS**
- 15 HR
- 6-4

A separate same-day query returned 5.5 R/G because of a slightly different rolling window/cache. The more detailed 59-run game table includes Aug. 31 and Sep. 1 and is preferred as the freshest explicit event window.

Against left-handed pitching in 2026:
- approximately **.728-.730 OPS**
- .241-.243 AVG
- .312-.314 OBP
- .415-.416 SLG
- 59 HR

Interpretation:
- New York's overall recent offense is very strong.
- The specific LHP split is materially less dominant than its L10 overall run rate.
- Detmers therefore has a credible path to suppressing a normally hot offense.

### Angels — L10
Fresh current window:
- **37 runs / 3.7 R/G**
- .225 AVG
- .306 OBP
- .339 SLG
- **.645 OPS**
- only 5 HR
- 2-8

Season:
- approximately 4.09 R/G
- 568 runs
- 26th in runs in the current source
- 27th in HR
- among MLB's higher-strikeout offenses

Interpretation:
- the 10-run Aug. 31 game is a real ceiling event but not the central current offensive regime.
- Against Schlittler's power profile, the Angels' strikeout/contact floor is a major Under/Yankees-separation mechanism.

## F. Current series and H2H

2026 meetings before P-266:
- Apr. 13: Yankees 11-10 Angels
- Apr. 14: Angels 7-1 Yankees — Detmers 7 IP, 1 R
- Apr. 15: Yankees 5-4 Angels
- Apr. 16: Angels 11-4 Yankees
- Aug. 31: Angels 10-1 Yankees
- Sep. 1: Yankees 7-3 Angels

For today's 6.5 line:
- **all six listed 2026 meetings cleared Over 6.5**

This is strong **outcome** evidence against an Under.

Continuity caveat:
- today's pitcher pair is unique; Schlittler has never faced the Angels.
- the only highly starter-relevant H2H is Detmers' April 14 suppression of New York.
- previous high totals were driven by different starters, bullpen states, error clusters and/or one-sided blowups.
- therefore the 6/6 Over H2H is a kill-path signal, not the primary total baseline.

## G. Bullpen / availability chain

### Yankees
Sep. 1 relief usage:
- Brent Headrick 1.1 IP
- Paul Blackburn 1.1 IP
- John Schreiber 1.0 IP
- all scoreless

Aug. 31:
- Michael Fulmer, Luis Gil and David Bednar were used in the 10-1 loss and allowed damage.

Current implication:
- New York has enough relief depth, but several arms have worked recently.
- Bednar had Sep. 1 off after pitching Aug. 31, so he is not assumed unavailable.
- Blackburn/Headrick/Schreiber all worked the prior night.
- the bullpen therefore receives a **mild fatigue/role-mix widening**, not a generic quality downgrade.

### Angels
Sep. 1:
- Tayler Saucedo 1.0 IP
- Samy Natera Jr. 0.2 IP
- Sammy Peralta 1.1 IP

This makes the Angels' immediate post-Detmers chain less clean than if all primary relievers were fresh.

However, other arms remain available; no blanket "bullpen tired" assumption is used.

## H. Park / environment

Angel Stadium:
- 2026 one-year Statcast run factor approximately **92**, meaning observed run scoring has been below neutral in the one-year sample.
- 2024-26 rolling factor approximately **99**, essentially near neutral over the larger window.

Interpretation:
- the 2026 one-year environment supports modest run suppression.
- the broader multi-year environment says not to overstate the park effect.
- the park does not erase the Yankees' HR/cluster tail.

Current game conditions from secondary game-day reporting:
- low-80s °F
- clear
- modest wind with an out-to-right component

Weather:
- modestly widens the HR tail.
- not large enough to override the starter matchup.
- no rain/termination concern.

## I. Mandatory joint hook / cluster / separation branches

### BB-B1 — Both starters at centre
Representative:
**Yankees 3, Angels 2**
- Angels +1.5 WIN
- Under 6.5 WIN
- Yankees -1.5 LOSS

Mechanism:
- Schlittler 6 IP / 1-2 R
- Detmers 6-7 IP / 2-3 R
- bullpens largely hold.

### BB-B2 — Detmers exits first / Yankees reach relief
**Yankees 4, Angels 2**
- Yankees -1.5 WIN
- Under 6.5 WIN

This is important: **the Yankees run line can win while the Under also wins**. Low total does not imply close margin.

### BB-B3 — Angels HR/sequencing cluster
**Angels 4, Yankees 3**
- Angels +1.5 WIN
- Over 6.5 WIN

Mechanism:
- Schlittler walk traffic + one extra-base-hit/HR sequence
- current Yankees bullpen mix cannot fully suppress late scoring.

### BB-B4 — Schlittler suppression / favourite separation
**Yankees 4, Angels 1**
- Yankees -1.5 WIN
- Under 6.5 WIN

This is the primary kill path to Rank #1 Angels +1.5 and is explicitly budgeted after the P-258 separation lesson.

### BB-B5 — Detmers suppression / Angels upset
**Angels 3, Yankees 1**
- Angels +1.5 WIN
- Under 6.5 WIN

Mechanism:
- repeat of Detmers' current four-start regime
- Yankees' LHP performance remains ordinary rather than elite.

### BB-B6 — High cluster state
**Yankees 5, Angels 3** / **Yankees 6, Angels 2**
- Over wins
- Yankees -1.5 wins

Mechanism:
- Detmers' current suppression breaks
- Yankees hot offense converts traffic/HR
- Angels contribute against Schlittler or tired middle relief.

## J. 6.5-run component budget

Under wins at:
- 3-2
- 4-2
- 4-1
- 3-1
- 2-1

Over wins at:
- 4-3
- 5-2
- 5-3
- 6-1
- etc.

### Under support
- Schlittler: 2.09 season ERA; roughly 1.13 over latest four
- Detmers: **1.50 August ERA**, only 2 ER over latest four starts
- Angels current L10 offense only 3.7 R/G / .645 OPS
- Yankees only ~.73 OPS vs LHP
- Angel Stadium 2026 run factor below neutral
- Judge/Stanton absent
- a 4-2 Yankees result still wins the Under

### Over support
- line is extremely low at 6.5
- Yankees overall L10 offense around 5.9 R/G
- all six current-season H2Hs cleared 6.5
- current wind has a modest out-to-RF component
- both bullpen chains have some recent usage
- one multi-run homer/sequence cluster is enough to move 3-2 into 5-3

Result:
**Under 6.5 receives only a LEAN, not a stronger label.**

## K. ±1.5 separation budget

### Angels +1.5
Wins through:
- every Angels win
- every one-run Yankees win

Central cover states:
- NYY 3-2
- LAA 3-2
- LAA 3-1
- NYY 2-1

Failure states:
- NYY 3-1
- NYY 4-2
- NYY 4-1
- NYY 5-2

Why Rank #1 survives the separation audit:
- Detmers' current run-suppression state materially reduces New York's expected separation.
- home last bat preserves a one-run/walk-off branch for Los Angeles.
- Yankees are without Judge/Stanton.
- New York's LHP split is merely solid, not dominant.

Why confidence stays Medium rather than high:
- Schlittler creates a genuine Angels 0-1 run floor.
- Yankees are much stronger overall and hot offensively.
- 4-1 / 4-2 is not a remote tail.

### Yankees -1.5
This is the strongest alternative side direction.

It wins when:
- Schlittler holds LAA to 0-2,
- and NYY gets even an ordinary 3-5 run output.

At a 6.5 total, a **4-1** or **4-2** result is simultaneously:
- Yankees -1.5 WIN
- Under 6.5 WIN

Thus the run-line thesis is coherent with the low-total thesis.

## L. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-266-C02 — Angels +1.5** | **LEAN** | **MEDIUM** | Detmers is in an elite current suppression run (5 ER in August, 2 ER over latest four) and already held NYY to one run in April. The cushion covers every LAA win plus one-run NYY wins. Main kill path: Schlittler holds LAA to 0-1 and Yankees manufacture 3-4 runs, producing 3-1/4-1 separation. |
| **2** | **P-266-C04 — Under 6.5 Runs** | **LEAN** | **MEDIUM** | Both starters have top-tier current centres, LAA offense is weak, NYY are ordinary vs LHP, Judge/Stanton are absent, and Angel Stadium has suppressed runs in 2026. The 6.5 threshold itself, 6/6 season H2H Overs and bullpen/HR cluster tails prevent Rank #1. |
| **3** | **P-266-C01 — Yankees -1.5** | **SLIGHT LEAN / LEAN-ADJACENT** | **MEDIUM-LOW** | NYY have the overwhelming team-quality edge and Schlittler can reduce LAA to 0-2 runs; 4-1/4-2 cover states are very plausible. It stays below LAA +1.5 because Detmers' current form compresses NYY scoring and home last bat protects close Angels states. |
| **4** | **P-266-C03 — Over 6.5 Runs** | **FORCED RANK / weaker total direction** | **MEDIUM-LOW** | A 6.5 line is low, NYY are scoring 5.9 R/G L10, and every 2026 H2H has cleared it. It ranks last because today's pitcher pair is substantially more suppressive than the prior matchup set and both central starter branches point to 4-6 total runs. |

## M. Rank-1 coherence

Rank #1 = Angels +1.5.

Representative states:
- NYY 3-2 LAA -> Angels +1.5 + Under
- LAA 3-2 NYY -> Angels +1.5 + Under
- LAA 4-3 NYY -> Angels +1.5 + Over
- NYY 4-1 LAA -> Yankees -1.5 + Under; Angels +1.5 loses
- NYY 5-3 LAA -> Yankees -1.5 + Over; Angels +1.5 loses

Relations:
- Under 6.5: **COHERENT / PARTIAL**
- Yankees -1.5: **DISJOINT** exact side complement
- Over 6.5: **PARTIAL / cluster tail**

The favourite's low-total multi-run branch is explicitly retained rather than hidden.

## N. Potential winner

### **New York Yankees — LEAN**

Why:
- substantially stronger overall team record and run differential
- Schlittler is the better season-long starter
- Yankees' current offense is far hotter than the Angels'
- New York has more late-inning offensive and relief depth despite recent bullpen usage

Why the winner call can coexist with Angels +1.5 Rank #1:
- the most likely NYY win families are **close** when Detmers is in this current form;
- a 3-2 Yankees result makes both calls correct;
- LAA +1.5 has a broader settlement region because it also catches every Angels upset.

Why not a stronger winner label:
- Detmers has an excellent current regime and a successful same-season matchup against NYY;
- Judge and Stanton are unavailable;
- Angels have home last bat.

## O. Final delivery

1. **Angels +1.5**
2. **Under 6.5 Runs**
3. **Yankees -1.5**
4. **Over 6.5 Runs**

**Potential winner:** New York Yankees — LEAN.

## P. Append confirmation

- Full incomplete-event sweep performed first: YES
- Newly safe-to-settle event: NO
- MLB exact event/start state verified: YES
- Official starters re-handshaken: YES
- Official batting orders at freeze: TBD / uncertainty preserved
- Current secondary lineups used only as mixture evidence: YES
- Starter current-regime vs season-prior reconciliation: YES
- Bullpen recent usage included without freshness=quality shortcut: YES
- 6.5 total component budget solved: YES
- +1.5 / -1.5 separation budget solved: YES
- Low-total wide-margin branch explicitly retained: YES
- H2H 6/6 Over evidence retained but continuity-shrunk: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-267**


---

# Settlement / retrospective sweep before P-267 — 2026-09-03

## P-261 — Toronto Blue Jays @ Cleveland Guardians — FINAL

**Verified final:** Toronto Blue Jays **11-0** Cleveland Guardians.

### Contract settlement

| ID | Original rank | Contract | Outcome |
|---|---:|---|---|
| `P-261-C02` | 1 | Guardians +1.5 | **LOSS** |
| `P-261-C04` | 2 | Under 7.0 Runs | **LOSS** |
| `P-261-C01` | 3 | Blue Jays ML | **WIN** |
| `P-261-C03` | 4 | Over 7.0 Runs | **WIN** |

**Potential winner — Cleveland Guardians:** **LOSS**.

### Deep Rank-1 retrospective

**Process grade:** `PROCESS_DEFECT — COMMAND / SEPARATION TAIL UNDERWEIGHTED`.

#### What went right
- The pregame card correctly identified **Dylan Cease as the strongest single run-suppression component** in the matchup.
- The forecast explicitly preserved the Toronto multi-run separation branch, including a 5-2-type score family, rather than assuming every low-total state had to be close.
- Blue Jays ML and Over 7.0 were retained as real competing branches and both ultimately won.
- The baseball framework's low-total separation rule was conceptually present.

#### What went wrong
- Joey Cantillo's recent **walk/traffic risk** was recorded — 16 walks in 22.2 recent innings — but his recent 2.78 ERA was allowed to dominate the practical ranking too strongly.
- Toronto produced a decisive early cluster, scoring **five runs in the second inning** after already scoring in the first. Two second-inning runs scored on a throwing error, and the inning continued into further run creation.
- Cleveland's 8-2 recent form / hot offense was weighted too heavily against an elite, highly specific opposing starter. Cease shut Cleveland out.
- The card treated Cleveland's elite recent bullpen as meaningful cushion protection, but bullpen value is **score-state dependent**. Once Toronto created large early separation, the leverage chain no longer protected the `CLE +1.5` region in the way a close-game model implied.
- This was also a direct demonstration of the baseball control that **low expected total does not imply a close margin**: Toronto alone scored 11.

#### Learning disposition
No fitted weight or calibration parameter is promoted from one event. This result reinforces existing active baseball controls:
1. recent starter ERA must not mute an explicit walk/command-tail branch;
2. when an elite opposing starter can drive the underdog scoring floor toward zero while the underdog starter carries command traffic, the favourite's **multi-run separation + upper-total cluster states are linked** and must be stress-tested jointly;
3. elite bullpen quality cannot be treated as generic cushion insurance when the likely realised score state never summons the relevant leverage arms.

**P-261 status:** CLOSED.

## Still open / provisional at the P-267 sweep
- `P-250-C05` Yunnan–Chongqing corners — unresolved.
- `P-251-C05` Sassuolo–Frosinone corners — provisional threshold-invariant win.
- `P-255-C05` Inter Women–Wolfsburg Women corners — unresolved.
- `P-256-C05` PSG Women–Frankfurt Women corners — unresolved.
- `P-259` Mets–Rays — live / no final verified at sweep.
- `P-260` Giants–Pirates — live/open / no final verified.
- `P-262` TKR–Falcons — in progress / no final verified.
- `P-263` Faria–Alcaraz — upcoming / no final verified.
- `P-264` White Sox–Astros — live / no final verified.
- `P-265` Toluca–León — live / no final verified.
- `P-266` Yankees–Angels — upcoming / no final verified.

No other retrospective was fabricated.

---

# P-267 — Lanlana Tararudee vs Linda Noskova — 2026 US Open Women's Singles Round 2 — PREGAME

## A. Identity / contract freeze

- **Canonical ID:** `P-267`
- **Event:** 2026 US Open Women's Singles
- **Round:** Round of 64 / Second Round
- **Match:** Lanlana Tararudee vs Linda Noskova
- **Venue:** Louis Armstrong Stadium, USTA Billie Jean King National Tennis Center
- **Surface:** Outdoor hard; retractable-roof stadium
- **Format:** Best of three sets
- **State at research cutoff:** **UPCOMING / NOT STARTED**
- **Scheduled window:** approximately 2026-09-03 01:50 UTC / 11:50 AEST, subject to preceding match duration
- **Method:** `MDS-2026.09.02-v3.1`
- **Algorithm:** `GFA-2` + `SFA-TENNIS`
- **Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`
- **Numerical state:** no approved/fitted tennis target/source/model
- **Operator retirement/walkover terms:** NOT SUPPLIED -> `UNKNOWN_DEFINITION`
- **Probability:** `NOT_GENERATED / NOT_PUBLISHED`
- **Value:** `NO VALUE DETERMINABLE`

## B. User-supplied contracts

| ID | Contract | Ordinary completed-match region |
|---|---|---|
| `P-267-C01` | Tararudee +4.5 games | Tararudee wins, or loses by 4 net games or fewer |
| `P-267-C02` | Noskova -4.5 games | Noskova wins by 5+ net games |
| `P-267-C03` | Over 31.5 total games | 32+ games |
| `P-267-C04` | Under 31.5 total games | 0-31 games |

C01/C02 are exact complements under ordinary completed-match settlement.  
C03/C04 are exact complements.  
Retirement treatment remains operator-unknown.

## C. Participant / current-status gate

### Lanlana Tararudee
- Right-handed.
- Current WTA rank: **No. 76**.
- Age: 22.
- 2026 WTA official record: **41-17** across all recorded levels.
- 2026 breakthrough includes two WTA 125 titles (Austin and Istanbul), but those lower-level results are not treated as exchangeable with a Grand Slam match against a top-six opponent.
- US Open R1: defeated Elvina Kalieva **6-3, 6-7(4), 6-2**.
- No verified current injury/withdrawal was found.

### Linda Noskova
- Right-handed.
- Current WTA rank: **No. 6**.
- No. 6 seed at this US Open.
- 2026 Wimbledon champion.
- US Open R1: defeated Katie Volynets **7-5, 6-1**.
- No verified current injury/withdrawal was found.

## D. Level / surface adjustment

Tararudee's broad 2026 record is strong, but a large portion was accumulated at WTA 125 / qualifying / lower-level contexts. Her current WTA official Grand Slam record entering this round is still sparse.

Noskova's current evidence is materially higher-level:
- reigning Wimbledon champion;
- WTA 1000 hard-court wins over Katie Boulter and Clara Tauson in Cincinnati;
- Grand Slam/WTA-level opponent quality is substantially stronger.

Therefore:
- Tararudee's recent form is promoted above a ranking-only underdog prior;
- it is **not** treated as equivalent to Noskova's top-tier surface/level sample.

## E. Current hard-court form

### Tararudee — recent hard sequence
- W Kalieva: **6-3, 6-7(4), 6-2** — US Open
- L Timofeeva: **6-7(5), 6-2, 6-7(4)** — Monterrey qualifying
- L Sawangkaew: **4-6, 3-6** — Cincinnati qualifying
- W Emerson Jones: **7-5, 7-5** — Cincinnati qualifying
- W Emerson Jones: **7-6(2), 6-2** — Toronto main draw
- W Qinwen Zheng: **6-3, 6-4** — Toronto qualifying

Interpretation:
- Tararudee has real current hard-court margin resistance.
- Her Timofeeva loss was extremely close over three sets.
- However, level/opponent comparability is mixed and must be shrunk.

### Noskova — recent hard sequence
- W Volynets: **7-5, 6-1** — US Open
- L Anisimova: **1-6, 4-6** — Cincinnati R16
- W Tauson: **7-6(3), 6-2** — Cincinnati
- W Boulter: **6-3, 6-3** — Cincinnati
- L McNally: **6-7(5), 1-6** — Toronto

Interpretation:
- Noskova's recent wins repeatedly contain genuine second-set / margin separation.
- Her losses also show volatility; she is not modelled as an automatic straight-set dominator.

## F. Serve / return mechanism

### Tararudee R1 vs Kalieva
Official WTA match stats:
- 11 aces
- 6 double faults
- **49.1% first serves in**
- **83.9% first-serve points won**
- only **36.2% second-serve points won**
- faced 9 break points, saved 6
- converted 6/15 break points

Mechanistic read:
- Tararudee has a high-upside first-strike serve when the first ball lands.
- The low first-serve entry rate plus weak second-serve conversion creates a clear Noskova return-pressure / separation path.
- The key uncertainty is whether Tararudee can raise first-serve percentage without sacrificing first-strike effectiveness.

### Noskova recent hard mechanism
Against Boulter:
- 10 aces
- 65.3% first serves in
- 78.1% first-serve points won
- created 9 break points and converted 4

Against Tauson:
- 17 aces
- 65.7% first serves in
- 78.3% first-serve points won
- created 9 break points and converted 3

Against Anisimova:
- second-serve conversion collapsed and Noskova created no break points, demonstrating the downside state.

Mechanistic read:
- Noskova owns the more reliable high-level combination of serve power + return pressure.
- Her ability to attack vulnerable second serves is particularly relevant to Tararudee's R1 profile.
- Noskova's own double-fault/second-serve volatility prevents the handicap from receiving stronger confidence.

## G. H2H continuity

Structured current H2H: **0-0**.

No prior meeting exists to weight.  
No synthetic H2H is created from common opponents.

## H. Workload / rest

Tararudee R1:
- three sets
- score total: 30 games
- required a deciding set

Noskova R1:
- two sets
- score total: 19 games
- after falling behind 2-5 in the opener, she won 11 of the final 12 games

Both have had recovery time. Tararudee carries more match workload, but there is no evidence that this has become a fitness limitation.

## I. Best-of-three set-count mixture

Qualitative ordinal weights only — **not probabilities**:

| Match length | Relative weight | Mechanism |
|---|---:|---|
| **2 sets** | **6** | Noskova's higher-level serve/return edge produces straight-set control, or Tararudee's upset occurs quickly |
| **3 sets** | **4** | Tararudee's current hard resistance / Noskova volatility produces a split-set match |

The mixture remains meaningfully two-sided rather than treating every Tararudee-success branch as a long match.

## J. Mandatory two-sided score tree

### Noskova ordinary straight-set control
**6-3, 6-3**
- total games = 18
- Noskova margin = +6
- Noskova -4.5: WIN
- Under 31.5: WIN

### Noskova close straight sets
**7-5, 6-4**
- total = 22
- Noskova margin = +4
- Tararudee +4.5: WIN
- Under 31.5: WIN

### Noskova deciding-set win
**6-3, 4-6, 6-3**
- total = 28
- Noskova margin = +2
- Tararudee +4.5: WIN
- Under 31.5: WIN

### Long Noskova deciding-set win
**7-6, 4-6, 6-3**
- total = 32
- Over 31.5: WIN
- Tararudee +4.5 generally wins the handicap

### Tararudee ordinary straight-set upset
**7-5, 6-4**
- total = 22
- Tararudee +4.5: WIN
- Under 31.5: WIN

### Tararudee close straight-set upset
**7-6, 7-5**
- total = 25
- Tararudee +4.5: WIN
- Under 31.5: WIN

### Tararudee deciding-set upset
**6-4, 3-6, 6-4**
- total = 29
- Tararudee +4.5: WIN
- Under 31.5: WIN

### Long Tararudee deciding-set upset
**7-5, 5-7, 6-4**
- total = 34
- Tararudee +4.5 + Over 31.5

## K. Handicap separation budget — ±4.5

Noskova -4.5 needs **5+ net games**.

Examples:
- 6-3, 6-3 = +6 -> Noskova covers
- 6-4, 6-3 = +5 -> Noskova covers
- 7-5, 6-4 = +4 -> Tararudee covers
- 6-4, 6-4 = +4 -> Tararudee covers
- 6-3, 4-6, 6-3 = +2 -> Tararudee covers
- 6-2, 4-6, 6-2 = +6 -> Noskova covers

Therefore Noskova -4.5 needs real separation, not merely a match win.

The key favourite-cover mechanism:
- Noskova repeatedly attacks Tararudee's second serve;
- at least one 6-2/6-3-type set occurs;
- Noskova avoids donating a set through double-fault / second-serve collapse.

The main Tararudee +4.5 mechanism:
- close straight sets or any ordinary split-set match;
- Tararudee's own win branches;
- first-serve effectiveness protects enough service games to prevent five-game net separation.

## L. Total-games budget — 31.5

This threshold is structurally high for WTA best-of-three.

### Every straight-set match is Under
Maximum ordinary two-set total:
- 7-6, 7-6 = **26**

So **all two-set branches cash Under 31.5**.

### Many three-set matches are also Under
- 6-4, 4-6, 6-4 = 30
- 6-3, 4-6, 6-3 = 28
- 6-2, 4-6, 6-3 = 27

### Over requires a long three-set match
Examples:
- 7-6, 4-6, 6-3 = 32
- 7-5, 5-7, 6-4 = 34
- 7-6, 6-7, 6-3 = 35

Direct Tararudee evidence:
- her recent Timofeeva match (7-6, 2-6, 7-6) totaled **34 games**, proving a genuine Over pathway.

But:
- Tararudee R1 totaled 30;
- Noskova R1 totaled 19;
- Noskova-Boulter totaled 18;
- Noskova-Tauson totaled 21;
- Noskova-Anisimova totaled 17;
- Noskova-McNally totaled 20.

The Under therefore survives both the central two-set state **and a large portion of three-set states**.

## M. Rank-1 implied games interval

Rank #1 = Under 31.5.

Its ordinary winning score families span:
- approximately **12 games** in an extreme 6-0, 6-0 match
- through **31 games** in long but still Under three-set structures

The practical central interval is roughly:
**18-30 total games**.

This interval is compatible with:
- Noskova -4.5 in efficient straight-set control;
- Tararudee +4.5 in close straight sets or ordinary three sets.

The Over's 32+ region sits beyond the central Rank-1 interval and therefore belongs in the bottom half.

## N. Reference-base-rate status

No clean, definition-compatible current US Open / WTA-hard threshold population was reconstructed for:
- Tararudee +4.5
- Noskova -4.5
- Over 31.5
- Under 31.5

without mixing very different favourite strengths and match states.

`REFERENCE_BASE_RATE = NOT AVAILABLE CLEANLY`.

No market or historical threshold frequency is imputed.

## O. Environment

- Louis Armstrong Stadium.
- Current US Open schedule has experienced rain disruption on outside courts.
- No verified current court-speed measurement is available for this exact match state.
- No speed coefficient is assigned.
- Roof state at match start is not assumed before the official start-state refresh.

## P. Direct marginal-likelihood ranking

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-267-C04 — Under 31.5 Total Games** | **LEAN** | **MEDIUM** | Every straight-set result is automatically Under, and many ordinary three-set matches also stay at 28-30. A 32+ result requires a long three-set state. |
| **2** | **P-267-C02 — Noskova -4.5 Games** | **SLIGHT LEAN** | **MEDIUM-LOW** | Noskova has the materially stronger WTA/Grand Slam level and a more reliable high-level serve/return combination. Tararudee's 49% first-serve rate / 36% second-serve conversion in R1 creates a real multi-break path. |
| **3** | **P-267-C01 — Tararudee +4.5 Games** | **LEAN-ADJACENT / FORCED RANK** | **MEDIUM-LOW** | Tararudee's current hard form provides genuine margin resistance; any ordinary three-set match and close Noskova straight-set win can cover +4.5. Level gap and serve volatility keep it below Noskova's separation branch. |
| **4** | **P-267-C03 — Over 31.5 Total Games** | **WEAKER DIRECTION / FORCED RANK** | **LOW-MEDIUM** | Requires not merely three sets, but a long three-set match. Tararudee has demonstrated that state recently, but it remains narrower than the large 2-set and sub-32 three-set regions. |

## Q. Rank-1 coherence

Rank #1 = Under 31.5.

Representative central state:
**Noskova 6-3, 6-3**
- Under 31.5 = WIN
- Noskova -4.5 = WIN

Adjacent close state:
**Noskova 7-5, 6-4**
- Under 31.5 = WIN
- Tararudee +4.5 = WIN

Three-set Under state:
**Noskova 6-3, 4-6, 6-3**
- Under = WIN
- Tararudee +4.5 = WIN

Therefore the Under is more robust than either handicap direction.

## R. Potential winner

### **Linda Noskova — LEAN**

Why:
- current world No. 6 / No. 6 seed;
- reigning Wimbledon champion;
- materially stronger high-level opponent/surface sample;
- demonstrated current hard-court separation against Boulter, Tauson and Volynets;
- Tararudee's R1 second-serve vulnerability provides a specific return-pressure mechanism.

Why not stronger:
- Noskova started R1 poorly and trailed Volynets 2-5 before recovering;
- her Cincinnati loss to Anisimova and Toronto loss to McNally show real volatility;
- Tararudee is in genuine current hard-court form and has repeatedly played close, margin-resistant matches.

## S. Final delivery

1. **Under 31.5 Total Games**
2. **Linda Noskova -4.5 Games**
3. **Lanlana Tararudee +4.5 Games**
4. **Over 31.5 Total Games**

**Potential winner:** Linda Noskova — LEAN.

## T. Append confirmation

- Full unresolved-event sweep performed first: YES
- P-261 newly settled / deeply retrospectively reviewed: YES
- Other live/upcoming items left open: YES
- P-267 official event/round/state verified: YES
- H2H: 0-0
- Surface/level adjustment explicit: YES
- Two-set / three-set mixture explicit: YES
- Two-sided quick/close/deciding branches explicit: YES
- Handicap separation budget solved: YES
- Rank-1 games interval stated: YES
- Retirement terms: UNKNOWN_DEFINITION
- No bookmaker odds / implied probabilities / market movement used: YES
- Drive modified: NO
- Prior forecasts rewritten: NO
- Numerical probability generated: NO
- New fitted forecast-weight rule created: NO
- **NEXT CANONICAL ID: P-268**

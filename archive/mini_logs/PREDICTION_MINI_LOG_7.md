# Prediction Mini Running Log

**Status:** ACTIVE — LOCAL RUNNING CONTINUATION / APPEND-ONLY  
**Opened:** 2026-09-02 09:38 Australia/Sydney (AEST, UTC+10)  
**Timezone:** `Australia/Sydney`  
**Governing published method:** `MDS-2026.08.31-v2.9` — qualitative champion; qualitative weights unchanged  
**Executable general algorithm:** `GFA-1` in `RULES_GENERAL.md §11`  
**Sport algorithm:** applicable `SFA-<SPORT>` section for the event  
**Operational guide:** `UGR-2026.09.01-v1.5`  
**Numerical training state:** `NTS-2026.08.25-v0.2` — Stage 0 all-sports design / pre-fit / not finalised  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE` unless the validated-probability, same-time price/terms, de-vig/return and uncertainty gates are all satisfied  
**Staking/ROI state:** DISABLED / NOT SUPPORTED  
**H0 state:** NOT BUILT / NOT QUALITY-APPROVED  
**Numerical model state:** ALL BUILDS DESIGN-ONLY / DATA-BLOCKED / NOT FIT  
**Drive mode:** READ-ONLY  
**Retrospective mode:** EXPLICIT USER REQUEST ONLY

---

## 1. Authority and predecessor

### 1.1 Authority order

1. Current user directive.
2. `AGENT_ROLE_AND_TASK.md` honesty, identity, anti-hindsight and mandatory-ranking invariants.
3. Hard gates in `RULES_GENERAL.md`, `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, and `NUMERICAL_TRAINING_SPEC.md`; numerical build/source status from `DATA_SOURCE_REGISTER.md`, `H0_DATASET_CARD.md`, and `NUMERICAL_MODEL_REGISTER.md`.
4. Applicable active sport rule file and its `SFA-<SPORT>` algorithm.
5. General defaults.
6. Only `PROMOTED_PROCESS` / otherwise operative entries from `LEARNING_REGISTER.md`; `TESTING` rows are process-testing only and cannot promote forecast weights without their prospective manifest and gates.

Historical prediction logs, retrospectives, settlement audits, appendices and archive material are evidence only. They do not override the active flat Markdown authority or the canonical top snapshot.

### 1.2 Canonical predecessor

- Active canonical combined log: `PREDICTION_LOG_COMBINED.md`.
- Controlling snapshot date: 2026-09-02 Australia/Sydney.
- Canonical coverage through: `P-238`.
- Latest canonical forecast ID: `P-238`.
- **Next canonical ID: `P-239`.**
- This mini log continues the same `P-###` sequence; numbering is not restarted.
- The Drive combined log is the queue/ID authority. Older component snapshots and the older bundled local combined-log copy are non-controlling.
- Frozen issued forecasts are immutable. Corrections, state updates, settlements and retrospectives are append-only.

### 1.3 Provenance/performance boundary carried forward

- `P-215` through `P-238` are classified `E1-Q-LATE_IMPORT`.
- They are descriptive settlement/process evidence only.
- They are excluded from prospective ranking/model performance, calibration and test-completion counts.
- The next formal process/ranking checkpoint remains **60 new clean, demonstrably pre-result v2.9 event units**.
- The next sport-specific method-iteration target remains **100 new clean, balanced v2.9 event units**, with useful sport/market/horizon slices and roughly 30 eligible units per priority slice.
- Event count, not file count, controls those checkpoints.
- This mini log does not reclassify any prior event.

---

## 2. Opening queue state

### 2.1 Controlling queue copied from canonical top snapshot

**Live events:** 0  
**Final-event follow-ups in the controlling queue:** 10

| Queue item | Canonical status carried forward | Required follow-up only |
|---|---|---|
| P-126 | Final-event follow-up | Field-owner result/phase confirmation; C06 corners unresolved |
| P-148-C02 | PROVISIONAL LOSS | Resolve field owner/provider definition if available |
| P-149-C02 | PROVISIONAL WIN | Resolve field owner/provider definition if available |
| P-151-C02 | STRONG PROVISIONAL WIN | Resolve field owner/provider definition if available |
| P-166 | Definition unresolved | Operator OT/action definition unknown |
| P-176-C05 | PROVISIONAL WIN | Resolve named provider/operator corner definition |
| P-178-C05 | UNRESOLVED | Resolve field owner/provider definition |
| P-179-C05 | PROVISIONAL WIN | Resolve field owner/provider definition |
| P-200 | Definition unresolved | Operator OT/SO/action definition unknown |
| P-217-C01/C02 | UNRESOLVED | Operator reduced-overs/DLS/action definition unknown |

**Queue-integrity rule:** state checks and factual settlements are permitted where required. No why-it-won/why-it-lost analysis, lesson creation, process grading or method change is added unless the user explicitly requests a retrospective.

### 2.2 Provisional-status watchlist not included in the 10-item canonical queue

The canonical 2026-09-02 snapshot separately states that `P-233`, `P-234` and `P-235` are provisional pending a current CFA/club field-owner final, but it does not include them in its stated 10-item queue. This mini log does **not** silently rewrite the canonical queue. It preserves them once here as a reconciliation watchlist:

| ID | Current status | Reconciliation need |
|---|---|---|
| P-233 | FINAL / PROVISIONAL | Current CFA/club field-owner final not recovered |
| P-234 | FINAL / PROVISIONAL | Current CFA/club field-owner final not recovered |
| P-235 | FINAL / PROVISIONAL | Current CFA/club field-owner final not recovered |

Until the canonical top snapshot itself is corrected/reconciled, these remain a separate provisional watchlist rather than being counted inside the authoritative 10-item queue.

---

## 3. Publication boundaries

### 3.1 Probability

No internal numerical probability may be published at this time.

Required display state:
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

Do not publish or imply:
- calibrated win probability;
- internally fitted probability;
- fair odds;
- confidence percentage presented as a model probability;
- Brier/log/calibration performance for an unissued probability;
- numerical edge derived from a design-only model.

External model or market probabilities may be cited only as external evidence with provider, time and role clearly labelled; they are not internal forecasts.

### 3.2 Value / edge / staking

Default:
`NO VALUE DETERMINABLE`

`VALUE SUPPORTED` is prohibited unless all active value gates genuinely pass, including:
- validated and published calibrated W/P/L distribution for the exact target;
- exact same-time contract and operator terms;
- both-side price capture where required;
- frozen de-vig method / return arithmetic;
- push/refund/action treatment;
- uncertainty threshold and predeclared decision rule.

Do not claim expected value, market edge, ROI, profitability, staking advantage, guaranteed winner, lock, safe bet or risk-free outcome under the present framework.

### 3.3 Ranking

When prices are absent or value gates fail:
- rank valid unresolved supplied contracts by **marginal estimated win likelihood and robustness under their exact terms**;
- ranking remains qualitative under the current champion;
- lower loss probability and evidence quality are tie-breakers only;
- dependence does not convert the ordinal list into a hedge;
- an optional top-two coverage portfolio is separate and only used if explicitly requested.

---

## 4. Core active controls

The following are mandatory carry-forward controls, consolidated from the active framework and promoted-learning register.

### 4.1 Identity, time and state

- Freeze official event identity, competition/format/rules era, participants, venue, schedule, state, target, contract, interval and cutoff before directional analysis.
- `PREGAME` is valid only when `cutoff_at < scheduled_start_at` after timezone conversion.
- After start: use a verified live target, `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, or a verified final/no-forecast disposition.
- A stale schedule shell, zero-filled placeholder or old widget does not preserve pregame status.
- Decision-driving participants must pass the official event/team/role/participant handshake; otherwise branch uncertainty and apply the evidence cap.
- Never rewrite a frozen issued forecast after the fact.

### 4.2 Target and contract geometry

- Freeze the underlying target before bookmaker thresholds.
- Map exact win/push/loss intervals for each contract.
- Classify slate geometry at `G4.1`: exact complements, integer-push pairs, overlaps, gaps, opposite-side positive handicaps and free rows.
- State any forced row-win arithmetic created purely by slate geometry.
- All related contracts must derive from one coherent event target/distribution or qualitative corridor.
- A higher Over cannot be stronger than a lower Over merely because of separate narratives; equivalent monotonicity applies to Unders.
- Distinguish regulation/full-match/OT/extra-time/shootout/extra-innings/golden-point/DLS endpoints exactly.

### 4.3 Base-rate, recent-form and trend block

For every supplied contract:
- record a `REFERENCE_BASE_RATE` and qualitative band before event-specific narrative adjustment;
- apply event mechanism evidence only through the active anchor-and-adjust ordering;
- do not move a row more than the permitted band adjustment without the active framework explicitly authorising it;
- conjunct contracts cannot become Rank #1 unless each required condition is separately supported.

Retrieve and store once:
- L5;
- L10;
- L15;
- L20;
- head-to-head windows at the same window structure where available.

Then:
- de-duplicate to unique underlying events;
- record continuity count;
- apply the H2H continuity gate;
- run the short-versus-long trend test;
- explain causes and persistence before using a streak directionally;
- do not count nested windows as multiple independent confirmations.

### 4.4 Evidence lineage and source state

Every decisive factual claim should retain an atomic evidence record:
- source/URL or exact record;
- field owner;
- effective time;
- first-known/published time where material;
- observed/retrieved time;
- definition/version;
- authority class;
- freshness class;
- access/use state;
- evidence-lineage ID.

Rules:
- official sources own identity, rules, volatile releases, state and finals only for fields they actually expose;
- official data partners/specialists own only their defined metrics;
- government weather owns weather observations/forecasts;
- the operator/exchange owns contract, terms and price;
- reputable reporting may fill current news pending official confirmation;
- aggregators/snippets are discovery/corroboration, not final authority for decisive volatile facts;
- repeated descriptions/front ends of one upstream feed count as one lineage;
- official pages can be quarantined field-by-field when stale, zero-filled, malformed, internally impossible or unrevised.

### 4.5 Environment gate

Before any total or margin is discussed:
- classify venue `OUTDOOR`, `INDOOR` or `RETRACTABLE`;
- for outdoor/open-roof events obtain the venue-coordinate match-window forecast;
- record wind speed, gusts, wind direction, dew point, cloud cover and hourly precipitation where relevant;
- resolve wind against ground/field orientation when the sport is direction-sensitive;
- do not apply automatic rain/wind/heat/cold Under/Over effects; state the sport-specific mechanism.

### 4.6 Distribution/corridor and kill paths

- Build one sport-native exposure × rate object.
- Preserve lower, central, upper and material-tail branches.
- For two-sided score events retain at least: low/close, low/separation, high/close and high/separation families.
- Locate each line against the stated corridor.
- If ordinary branches cross both sides of a line and no validated weights exist, cap directional evidence rather than pretending precision.
- Solve aggregate totals through component/team/phase budgets.
- Decompose mechanisms that can have opposite signs on different contracts.
- A disclosed adverse branch must be shown subordinate; otherwise lower the evidence grade/ranking language.
- Sparse/new-regime uncertainty widens the distribution before shifting its centre unless a current directional mechanism is actually supported.

### 4.7 Dependence and performance accounting

- One event is the independent unit for evaluation.
- Multiple contracts, phases and winner aliases remain linked by event/dependence group.
- Potential winner aliases the matching canonical contract when terms are identical.
- Duplicate stored forecast blocks are marked `DUPLICATE_STORAGE` and excluded from counts.
- Late-import cards remain performance-ineligible.
- Directional row counts are not profit, ROI, calibration, independence or market edge.

---

## 5. Active learning controls and tests

### 5.1 Promoted-process state

`LEARNING_REGISTER.md` is the sole current lesson-status registry.

Promoted process controls now run through **L-056**. Important current additions/refinements carried into this log include:

- `L-046` start-state invariant;
- `L-047` corridor/threshold and aggregate component-budget coherence;
- `L-048` opposite-sign mechanism / terminal-state decomposition;
- `L-049` atomic evidence-lineage storage and de-duplication;
- `L-050` cricket pre-toss bat-first/bat-second/chase-censored mixture;
- `L-051` execution of ordered `GFA-1` + applicable `SFA-<SPORT>`;
- `L-052` mandatory L5/L10/L15/L20 + H2H window retrieval, continuity gate and trend test;
- `L-053` `REFERENCE_BASE_RATE` + band anchor and conjunct-contract gate;
- `L-054` venue classification and vector-aware match-window environment gate;
- `L-055` slate-geometry forced-outcome arithmetic;
- `L-056` cricket conditions ladder: seek two independent conditions signals where available and always compute the venue-and-format innings-order scoring baseline.

No learning above authorises a fitted weight or probability.

### 5.2 Testing rows

Active `TESTING` rows remain **PROCESS TESTING ONLY — FORECAST PROMOTION INELIGIBLE** until a complete prospective v2 manifest exists and promotion gates are met.

Current active testing IDs:
`T-001` through `T-014`, `T-P057-BB-Q2`, `T-P058-AFL-SHOTS`, `T-P059-TREND-CAUSE`.

Apply a testing row only when the new event satisfies its frozen eligible population. Do not retrospectively backfill eligibility.

### 5.3 Candidate hypotheses

Candidate observations are not operative forecast weights. New 2026-09-02 candidates include:
- `C-PL10-SOC-KNOCKOUT-REG`;
- `C-PL10-CR-PHASE-EXTRAS`.

They remain count 0 / `CANDIDATE` and cannot alter the qualitative champion until prospectively tested under the register procedure.

---

## 6. Sport-specific control matrix

The applicable sport file must be read for every later event. This matrix is a routing summary only; the full `SFA-<SPORT>` algorithm controls within its scope.

| Sport | Active algorithm | Mandatory sport-native focus |
|---|---|---|
| Cricket | `SFA-CRICKET` | Exact format/innings/target; toss/XI; legal-ball exposure; phase roles; wicket resources; strip and conditions gate; innings-order venue baseline; DLS/shortening/termination; bat-first vs chase-censored mixture |
| Basketball | `SFA-BASKETBALL` | League/rules/OT; participant minutes and lineup stints; possessions; shot/FT/turnover/rebound process; phase separation; team-score budgets; foul/late-foul, blowout and garbage-time multi-axis branches |
| American football | `SFA-AMERICAN-FOOTBALL` | Code-specific rules; QB/backup and expected reps; OL/skill/defensive units; drives/field position; red-zone/4th-down; turnover/explosive and special-teams tails; key-score discreteness; competition OT; preseason quarter/unit mixtures |
| Baseball | `SFA-BASEBALL` | Official starter handshake; posted lineups; starter batters faced/hook; score-state bullpen chain; contact/HR/sequencing tails; park/weather; home ninth and extras; listed-pitcher/action terms |
| AFL/AFLW | `SFA-AFL` | Separate AFL/AFLW populations; selected teams/roles; clearance/turnover → inside-50 → scoring-shot → conversion; venue/ground orientation; end-switch wind branches; total vs margin allocation; late territorial durability |
| Rugby league | `SFA-RUGBY-LEAGUE` | Competition/laws; official 13/bench/spine/kicker; sets/field position/completion; ruck/fatigue; goal-line entries; try/conversion; favourite-only blowout and low-total separation; golden-point/terminal winner branches |
| Rugby union / sevens | `SFA-RUGBY-UNION` | 15s vs sevens separation; official teams/squads; territory/22 entries; set piece/breakdown; discipline/cards; try/kicking composition; sevens restart/turnover/open-space clusters; qualitative-only module |
| Soccer | `SFA-SOCCER` | Regulation vs advance/ET/penalties; XI/keeper/bench minutes; goal process separate from corners/SOT; early-goal state changes; knockout/friendly/early-season regime handling; derivative completeness; provider-specific niche stats |
| Ice hockey | `SFA-ICE-HOCKEY` | Regulation vs full-match ML; starting-goalie mixture; lines/units/ice time; shots/chance quality/finishing/save process; special teams; empty-net; OT/SO treatment; goalie uncertainty cap |
| Tennis | `SFA-TENNIS` | Surface/level/format/tiebreak; exact participants; retirement terms; serve/return priors with shrinkage; H2H continuity; two-sided straight/close/deciding-set tree; winner/handicap/total scoreline coherence; qualitative-only module |

For any sport without a dedicated active module, apply `RULES_GENERAL.md` and require explicit target/source/model cards before numerical work.

---

## 7. Running event index

No new forecast is issued by this log-opening operation.

| Canonical ID | Event | State | Forecast appended | Settlement | Retrospective |
|---|---|---|---|---|---|
| P-239 | RESERVED AS NEXT ID — not yet issued | NOT CREATED | NO | N/A | NO |

**Reservation rule:** `P-239` is the next ID, not an issued event. It becomes a canonical forecast ID only when a distinct new event is fully frozen and its complete forecast is appended before delivery. If the canonical top snapshot changes before that event is issued, re-read it and use its current next ID instead.

---

## 8. New-event append template

```markdown
## P-### — [Event]

### A. Frozen identity and state
- Append sequence:
- Request time:
- State-check time:
- Information cutoff:
- Issue time:
- GAME-STATE:
- Sport / competition / format / rules era:
- Official event ID:
- Participants:
- Venue / home-away-neutral:
- Scheduled start — venue local:
- Scheduled start — Australia/Sydney:
- Venue class: OUTDOOR / INDOOR / RETRACTABLE
- Method: MDS-2026.08.31-v2.9
- General algorithm: GFA-1
- Sport algorithm: SFA-<SPORT>
- Applicable learning/test IDs:
- Provenance class:

### B. Decision set and contract freeze
- decision_set_id:
- candidate origin: USER_SUPPLIED / SYSTEMATIC_UNIVERSE
- operator / terms:
- price capture / both-side odds:
- slate geometry:
- forced-outcome arithmetic:
- target_id/version:
- target definition / unit / support:
- start state:
- endpoint / horizon:
- exposure / termination / censoring:
- regulation/OT/ET/SO/extra-innings/golden-point/DLS/action rules:

| Candidate ID | Canonical contract | Alias | Eligibility | W/P/L geometry | Dependence group |
|---|---|---|---|---|---|

### C. Participant release handshake
| Role | Side | Official participant | Status | Source/time | Exposure branch |
|---|---|---|---|---|---|

### D. Source and evidence-lineage register
| Evidence ID | Field | Source/record | Owner | Effective/known/observed/retrieved | Freshness | Lineage | State |
|---|---|---|---|---|---|---|---|

### E. Reference base-rate anchor
| Candidate | REFERENCE_BASE_RATE | Base-rate band | Basis/source | Max permitted event adjustment |
|---|---|---|---|---|

### F. Recent-form / H2H window block
Store underlying events once; derive L5/L10/L15/L20.
| Side/window | Sample | Target-relevant rate/result | Opponent/regime adjustment | Trend verdict |
|---|---:|---|---|---|
- H2H continuity count:
- H2H continuity verdict:
- Short-vs-long trend verdict:
- Causes/persistence test:
- De-duplication note:

### G. Environment gate
- Venue coordinates/orientation:
- Match-window source:
- Wind speed/gusts/direction:
- Ground/field vector resolution:
- Dew point:
- Cloud cover:
- Hourly precipitation:
- Surface/roof:
- Sport-specific mechanism:
- Unknown/conflicting fields:

### H. Sport-native exposure × rate model
- Baseline:
- Current regime:
- Participant exposure:
- Matchup interaction:
- Phase/score-state transitions:
- Context:
- Missingness/evidence caps:

### I. Scenario and component-budget map
| Scenario family | Exposure/rate mechanism | Representative target state | Contracts helped | Contracts hurt | Evidence lineage |
|---|---|---|---|---|---|
| Lower / low-close | | | | | |
| Central | | | | | |
| Low-separation | | | | | |
| High-close | | | | | |
| Upper / high-separation | | | | | |
| Material kill path | | | | | |

- Aggregate component/team/phase budget:
- Line-to-corridor relation:
- Same-mechanism adverse sign:
- Why the strongest kill path is subordinate, or evidence downgrade:

### J. GFA-1 / SFA gate record
| Gate/step | Result | Evidence / reason |
|---|---|---|

### K. Frozen ranking
Probability state for every row:
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

Value state:
`NO VALUE DETERMINABLE` unless every value gate passes.

| Rank | Candidate / Contract ID | Selection | Verdict | Evidence quality | Base-rate band | Event-adjusted band | Dependence | Performance role | Actionability |
|---:|---|---|---|---|---|---|---|---|---|

### L. Potential winner
- Canonical winner contract / alias:
- Endpoint:
- Status: LEAN / FORCED WINNER — LOW CONFIDENCE
- Reason:
- Winner is not a separate observation when identical to a ranked contract.

### M. Final volatile refresh
- Official state refresh:
- Participant refresh:
- Weather/roof refresh:
- Market/terms refresh:
- Cutoff invariant:
- Changes since initial research:

### N. Frozen forecast
[Insert the complete user-facing forecast exactly as issued. This block is immutable after issue.]

### O. Append confirmation
- Forecast appended before delivery: YES
- Drive modified: NO
- Retrospective performed: NO
```

---

## 9. Settlement-only append template

Use for factual result/queue integrity. This is **not** a retrospective.

```markdown
### Settlement update — P-### — [timestamp Australia/Sydney]

- Official/fallback final source:
- Source authority/state:
- Final score/result:
- Endpoint:
- Operator/provider terms used:
- Stat corrections checked:
- Event status: FINAL / PROVISIONAL / UNRESOLVED / NO ACTION
- Queue disposition:

| Contract ID | Frozen contract | Official/provisional settled value | Outcome | Settlement authority | Notes |
|---|---|---:|---|---|---|

- Potential-winner outcome:
- Remaining unresolved fields:
- Performance eligibility unchanged:
- No pregame rationale rewritten: YES
- Retrospective performed: NO
- Learning register changed: NO
```

---

## 10. Retrospective template — explicit request only

Do not execute this section automatically.

```markdown
### Retrospective — P-### — EXPLICITLY REQUESTED

| Preissue expectation | Actual driver | Difference | Knowability before issue | What was right | What was wrong/omitted | Process grade | Defect class | Candidate lesson/test | Method change |
|---|---|---|---|---|---|---|---|---|---|

Required controls:
- Separate outcome grade from process grade.
- Use only information demonstrably knowable by the frozen cutoff when judging the original process.
- Do not insert post-result facts into the frozen pregame rationale.
- A losing compliant forecast is not automatically a model defect.
- A winning defective process is not validation.
- Rank #1 losses receive detailed process review when retrospective work is requested, but no automatic weight strike.
- Candidate learning does not become a forecast weight without the LEARNING_REGISTER prospective procedure.
- Any learning/register update is append-only and versioned.
```

---

## 11. Source hierarchy and evidence-lineage rules

### Field-owning hierarchy
1. Governing body / league / competition / official match centre / team / venue for official identity, rules, participants, state and final.
2. Government meteorological service for venue-local forecast/observation; venue owner for roof/surface status.
3. Official data partner or established statistical database for its defined historical field.
4. Specialist analytical provider for its defined derived metric.
5. Reputable named reporting for material current information not yet officially released.
6. Actual operator/exchange for exact contract, terms, line and price.
7. Aggregator/query/snippet/social discovery as corroboration only unless the active fallback rule expressly permits it.

### Conflict handling
- Resolve conflicts field-by-field.
- Prefer the freshest definition-compatible field owner.
- Quarantine stale/zero-filled/unfinished official placeholders for the affected field.
- Preserve conflicting raw values and lineage.
- Two weak sources do not equal one controlling source.
- Multiple branded front ends using the same upstream feed are one lineage unless independence is demonstrated.
- For provisional settlement, retain provisional labels until field ownership/definition is resolved.
- Do not harmonise conflicting values merely to make settlement convenient.

---

## 12. Numerical-training state carried forward

- NTS specification: `NTS-2026.08.25-v0.2`.
- Stage: `S0 — Markdown targets/source/model/metric/gate design`.
- S1 source audits / snapshots: NOT STARTED.
- H0 systematic historical feature store: NOT BUILT / NOT QUALITY-APPROVED.
- A0/A1 models: NOT FIT.
- A2 sport-native simulators: NOT FIT.
- A3/A4 flexible challengers: NOT FIT.
- Calibration / untouched TEST: NOT STARTED.
- E1-P shadow: NOT STARTED.
- Publication decision: DISABLED.
- No numerical model is calibrated, validated, championed or authorised to publish probabilities.
- Rugby union/sevens and tennis have qualitative modules but no approved numerical target/source/dataset/model card.
- Any future numerical implementation requires explicit user authorisation and its separate approval gates.

**Metadata note:** the current Drive `NUMERICAL_TRAINING_SPEC.md` and `NUMERICAL_MODEL_REGISTER.md` headers still name `MDS-2026.08.31-v2.8` as the “governing published forecast method,” while current README, AGENT_ROLE_AND_TASK, RULES_GENERAL, MODEL_AND_DATA_SPEC, guide and learning register identify `MDS-2026.08.31-v2.9`. This mini log treats the v2.8 references as stale cross-reference metadata because the numerical stage/build state is unchanged and the current framework authority expressly identifies v2.9. No numerical permission is inferred from that mismatch.

---

## 13. Change and source provenance

### 13.1 Current Drive authority consulted read-only

- `README.md` — framework review 2026-09-02; identifies current method, active document map and canonical log.
- `PREDICTION_LOG_COMBINED.md` — controlling top snapshot through P-238; next ID P-239; queue/performance boundary.
- `LEARNING_REGISTER.md` — effective 2026-09-02; sole current lesson-status registry; promoted controls through L-056 and active tests/candidates.
- `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md` — supporting reconciliation evidence only; not used to override the canonical queue.
- `NUMERICAL_TRAINING_SPEC.md` — Stage 0 design/pre-fit and publication gates.

No Drive file was edited, uploaded, replaced, moved or deleted.

### 13.2 Active local framework copies consulted

- `AGENT_ROLE_AND_TASK.md`
- `RULES_GENERAL.md`
- `MODEL_AND_DATA_SPEC.md`
- `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`
- `NUMERICAL_TRAINING_SPEC.md`
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `DATA_SOURCE_REGISTER.md`
- `H0_DATASET_CARD.md`
- `NUMERICAL_MODEL_REGISTER.md`
- `LEARNING_REGISTER.md`
- `RULES_CRICKET.md`
- `RULES_BASKETBALL.md`
- `RULES_AMERICAN_FOOTBALL.md`
- `RULES_BASEBALL.md`
- `RULES_AFL.md`
- `RULES_NRL_RUGBY.md`
- `RULES_RUGBY_UNION.md`
- `RULES_SOCCER.md`
- `RULES_ICE_HOCKEY.md`
- `RULES_TENNIS.md`

### 13.3 External verification

- Australia/Sydney was verified as AEST / UTC+10 on 2026-09-02; this is recorded only for the opening timestamp. Sports facts for future events must still follow the active field-owning source hierarchy.

---

## 14. Opening verification checklist

- [x] README used to identify active framework and canonical combined log.
- [x] Canonical top controlling snapshot used for next ID and primary queue.
- [x] Next canonical ID agrees with top snapshot: `P-239`.
- [x] Latest valid method carried forward: `MDS-2026.08.31-v2.9`.
- [x] Numerical state preserved: Stage 0 / pre-fit / no validated model.
- [x] Probability publication blocked.
- [x] Value/edge/ROI/staking claims blocked unless future gates genuinely pass.
- [x] Current performance-ineligibility classifications preserved.
- [x] All 10 canonical queue follow-ups represented exactly once.
- [x] P-233/P-234/P-235 provisional-status inconsistency preserved once in a separate reconciliation watchlist rather than silently altering the queue.
- [x] No archived/historical snapshot treated as current queue authority.
- [x] No frozen issued forecast rewritten.
- [x] No retrospective performed.
- [x] No learning or method weight changed.
- [x] No Drive file modified.
- [x] This local mini log is ready to append the next distinct event after re-reading the canonical top snapshot.

---

## 15. Operating rule for every next prediction query

Before responding to any new forecast request:

1. Re-read the current Drive `README.md` and the top controlling snapshot of `PREDICTION_LOG_COMBINED.md`.
2. Reconcile any queue/next-ID change.
3. Perform factual state/settlement checks required for queue integrity only; do not run a retrospective unless explicitly requested.
4. Read the applicable active sport rule file and current promoted/testing learning rows.
5. Execute `GFA-1` plus the applicable `SFA-<SPORT>`.
6. Freeze the complete event/target/contract/state/evidence set.
7. Research and rank under the current publication boundaries.
8. Append the **complete frozen forecast** to this mini log before delivery.
9. Never rewrite that frozen forecast afterward.
10. Return the **complete updated running mini log** with the prediction response.


---

# P-239 — Athletics @ Texas Rangers — MLB — 2026-09-01 CDT / 2026-09-02 AEST

## A. Frozen identity and state

- **Append sequence:** P-239
- **Request received:** 2026-09-02 Australia/Melbourne
- **Final state/participant refresh:** 2026-09-02 09:53:03 Australia/Sydney (AEST, UTC+10)
- **Information cutoff:** 2026-09-02 09:53:03 Australia/Sydney
- **Scheduled first pitch:** 2026-09-01 19:05 CDT / 2026-09-02 10:05 AEST
- **Cutoff invariant:** PASS — cutoff precedes scheduled first pitch by approximately 12 minutes.
- **GAME-STATE:** PREGAME
- **Sport:** Baseball
- **Competition:** MLB regular season
- **Official event:** Athletics @ Texas Rangers
- **Venue:** Globe Life Field, Arlington, Texas
- **Home/away:** Athletics away; Texas Rangers home
- **Official/primary schedule evidence:** MLB.com probable-pitcher board and Rangers schedule
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-BASEBALL
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Performance/provenance class:** New local pre-result card, subject to future immutable-artifact/provenance audit; no performance claim is made at issue.

### Identity correction

The request contained two incompatible starter references:
1. supplied event/probables: Athletics @ Texas Rangers — B. Basso / M. Gore;
2. special-control text: “verify that Nola and Pfaadt remain the announced starters.”

The second pair is not this fixture. At the frozen cutoff, MLB’s current official probable-pitcher board listed:
- Athletics: **Brady Basso, LHP — PROBABLE_OFFICIAL**
- Texas Rangers: **MacKenzie Gore, LHP — PROBABLE_OFFICIAL**

Nola/Pfaadt were therefore quarantined as an unrelated copied control and were not used in the forecast.

A secondary Athletics game-day report further stated that Basso would **open a bullpen game** while J.T. Ginn received extra rest. Secondary lineup/DFS sources showed conflicting Athletics pitcher fields (including Ginn/Magdic), so Basso/Gore are treated as official probables rather than “confirmed starters.” If either pitcher changes before first pitch, this frozen card is not silently rewritten.

## B. Decision set and contract freeze

- **decision_set_id:** P-239-DS01
- **candidate origin:** USER_SUPPLIED
- **operator:** NOT SUPPLIED
- **odds:** NOT SUPPLIED
- **listed-pitcher/action rules:** UNKNOWN_DEFINITION
- **full-game extra-inning treatment:** OPERATOR TERMS NOT SUPPLIED
- **research target assumption:** official MLB full-game final score including extra innings if played; this assumption is for sporting-target analysis only and does not establish sportsbook settlement.
- **action caveat:** if the eventual operator uses listed-pitcher rules and Basso or Gore does not start/open as required, the operator may void or reclassify action. Settlement cannot be called definitively without the operator rules.
- **scheduled innings:** 9, subject to official MLB game termination/suspension rules.
- **target_id:** BASEBALL_JOINT_FINAL_RUNS-v1-QUAL
- **target definition:** joint official final runs (ATH, TEX) for the frozen full-game endpoint.
- **slate geometry:** two exact half-run complement pairs.
- **forced-outcome arithmetic:** absent abandonment/void/unknown-operator effects, exactly **2 of the 4 rows must win**:
  - Athletics +1.5 vs Rangers -1.5;
  - Over 7.5 vs Under 7.5.
- **performance note:** the forced 2-2 row structure is not evidence of prediction accuracy.

| Candidate ID | Contract | Eligibility | Geometry | Dependence group |
|---|---|---|---|---|
| P-239-C01 | Athletics +1.5 runs | ELIGIBLE | Exact complement of C02 | P239-MARGIN |
| P-239-C02 | Texas Rangers -1.5 runs | ELIGIBLE | Exact complement of C01 | P239-MARGIN |
| P-239-C03 | Full-game Over 7.5 runs | ELIGIBLE | Exact complement of C04 | P239-TOTAL |
| P-239-C04 | Full-game Under 7.5 runs | ELIGIBLE | Exact complement of C03 | P239-TOTAL |

## C. Participant and lineup handshake

### Probable pitchers
| Role | Side | Participant | Status | Key frozen evidence |
|---|---|---|---|---|
| Opener/probable starter | ATH | Brady Basso, LHP | PROBABLE_OFFICIAL | MLB probable-pitcher board: 0-1, 4.50 ERA, 22 SO |
| Probable starter | TEX | MacKenzie Gore, LHP | PROBABLE_OFFICIAL | MLB probable-pitcher board: 7-10, 4.40 ERA, 165 SO |

### Lineups
A current match-specific secondary page using MLB Stats API data displayed the following lineups:

**Athletics:** Henry Bolte, Zack Gelof, Lawrence Butler, Jonah Heim, Tommy White, Jeff McNeil, Max Muncy, Alika Williams, Denzel Clarke.

**Texas:** Justin Foscue, Corey Seager, Wyatt Langford, Brandon Nimmo, Ezequiel Duran, Jake Burger, Cody Freeman, Evan Carter, Elias Díaz.

The official team lineup release was not independently recovered through the available search surface before cutoff, and other secondary lineup sites contained stale/conflicting Athletics pitcher fields. Therefore lineup-driven claims are capped and this card does not describe every listed hitter as `CONFIRMED_OFFICIAL`.

## D. Environment gate

- **Venue classification:** RETRACTABLE
- **Venue:** Globe Life Field
- **Official venue fact:** Globe Life Field has a retractable roof.
- **Match-specific roof state:** secondary MLB-API-derived game page reported **Roof Closed**.
- **Indoor displayed condition:** approximately 72°F / no wind effect.
- **Weather mechanism:** with the roof reported closed, exterior wind/precipitation is not used as a scoring adjustment.
- **Roof-status limitation:** no independent official same-game roof-status announcement was recovered; if the roof state changes before first pitch, the environmental branch must be refreshed rather than backfilled.

## E. Recent form and H2H window block

### Team scoring windows
Recent StatMuse snapshots were retrieved once per window and treated as descriptive, not independent confirmations.

| Team | L5 R/G | L10 R/G | L15 R/G | L20 R/G | Trend read |
|---|---:|---:|---:|---:|---|
| Athletics | 3.8 | 4.1 | 4.47 | ~3.65 | Mixed; recent scoring around four runs, no strong directional streak |
| Rangers | 4.6 | 4.2 | ~3.8 | ~3.5-4.0 depending retrieval snapshot | Short-window rebound over a weaker longer-run scoring base |

Notes:
- The search surface exposed snapshot-timing differences for some L15/L20 StatMuse queries. The card records the conflict rather than selecting the most favourable number.
- Current team records at cutoff were Athletics 53-85 and Rangers 68-70.
- Athletics were 1-4 in the current L5 table; Rangers 2-3.
- Athletics were 4-6 over a current L10 scoring snapshot; Rangers 5-5 over a current L10 snapshot.

### Pitching/run-prevention context
- Athletics pitching allowed **174 runs in August**, the most in MLB according to the current game-day report, and the same report characterized the club’s relief situation as league-worst.
- A current match-specific bullpen page showed Athletics availability at **6 available / 2 limited / 1 rest required** versus Texas at **8 available / 2 limited / 0 rest required**.
- Athletics used Chris Roycroft for 37 pitches and José Suarez for 23 pitches in the prior 8-1 loss.
- Texas received seven scoreless innings from Jacob deGrom in that prior game, materially reducing immediate bullpen load.
- Texas closer Jacob Latz had last worked Aug. 30 and had a 1.65 ERA / 27 saves in the retrieved current log.
- Texas bullpen depth is not pristine: Peyton Gray and Cole Winn had just been placed on the IL. That weakens the “Texas pen is fully healthy” branch but does not erase the workload advantage created by deGrom’s seven-inning outing.

### Head-to-head continuity
Current 2026 season series before P-239:
- Athletics **6-5** Rangers.
- Reconstructed 11-game total results from the current StatMuse season-series record plus August/official game results: Over 7.5 occurred **7/11**; Under 7.5 **4/11**.
- Athletics +1.5 would have covered **7/11**; Texas -1.5 **4/11**.

**Continuity verdict:** LIMITED-MODERATE. Team identities and several core hitters persist, but the current Basso bullpen-game structure, Gore role/current form, bullpen health and late-season rosters differ materially from early-season meetings. H2H is descriptive, not controlling.

## F. Starter and relief-chain analysis

### Athletics: Brady Basso / bullpen game
- MLB listed Basso at 0-1 with a 4.50 ERA.
- The current Athletics game-day report says Basso is being used as the opener with J.T. Ginn receiving extra rest.
- Basso had recently appeared from the bullpen, so starter-length assumptions are inappropriate.
- This is a direct SFA-BASEBALL “short start = exposure, not automatic Over” case: direction depends on the actual relief chain.
- The current relief context is nevertheless adverse for Oakland: poor August run prevention, multiple recent bullpen usages and a game structure that requires many non-Basso outs.

### Rangers: MacKenzie Gore
- MLB listed Gore at 7-10 with a 4.40 ERA and 165 strikeouts.
- In his most recent start against the White Sox, Gore failed to complete four innings and allowed 4 runs on 8 hits and 4 walks in 3 2/3 innings.
- That recent outing is not treated as a permanent true-talent reset, but it preserves an ordinary Athletics-scoring branch and prevents the Texas side from being treated as a low-total certainty.

### Relief-chain asymmetry
The most decision-relevant asymmetry is **expected bullpen exposure**, not merely starter ERA:
- Oakland is scheduled into a bullpen game and comes off a game in which the starter recorded only 4 1/3 innings.
- Texas got seven innings from deGrom yesterday and has the deeper current availability count.
- This raises the Texas team-run and separation ceiling.
- Because Gore has a credible 3-4-run allowance branch, the same structure also raises the full-game Over path.

## G. Reference base-rate anchor

No model probabilities are generated. Bands are qualitative starting positions before event-specific adjustment.

| Contract | Reference band | Event adjustment | Frozen band |
|---|---|---|---|
| Athletics +1.5 | MEDIUM-HIGH — positive 1.5-run cushion | Down one band: bullpen-game/separation risk | MEDIUM |
| Rangers -1.5 | MEDIUM-LOW — requires Texas win by 2+ | Up one band: relief-chain/lineup/field-position equivalent scoring separation path | MEDIUM |
| Over 7.5 | MEDIUM — no price supplied; total direction begins neutral | Up one band: Oakland relief exposure + Gore non-trivial run allowance | MEDIUM-HIGH |
| Under 7.5 | MEDIUM — exact complement of Over before event adjustment | Down one band: same upper-tail mechanisms | MEDIUM-LOW |

No band is a calibrated probability.

## H. Scenario and component-budget map

| Scenario family | Representative score family | Main mechanism | Helps | Hurts |
|---|---|---|---|---|
| Low / close | TEX 4-3 or ATH 4-3 | Gore/Basso effective early, relief chain holds, limited HR clustering | ATH +1.5, Under | TEX -1.5, Over |
| Low / separation | TEX 5-1 or 6-1 | Gore rebound + Oakland bullpen gives Texas enough separation | TEX -1.5, Under | ATH +1.5, Over |
| Central | TEX 5-3, 6-3, 6-2 | Texas gets repeated relief looks; Gore allows some Athletics traffic | Over, TEX -1.5 | Under, ATH +1.5 |
| High / close | TEX 6-5 / ATH 6-5 | Gore instability + bullpen-game variance + HR clusters | Over, ATH +1.5 | Under, TEX -1.5 |
| High / separation | TEX 7-3 / 8-3 | Oakland relief chain fails; Texas power/traffic cluster | Over, TEX -1.5 | Under, ATH +1.5 |
| Athletics control kill path | ATH 5-3 / 6-4 | Gore command/contact issue persists while Oakland pen performs adequately | ATH +1.5, Over often | TEX -1.5; Texas winner |

### Component budget at 7.5
The Over needs combinations such as:
- Texas 5 + Athletics 3;
- Texas 6 + Athletics 2;
- Texas 4 + Athletics 4.

Those are compatible with both principal pitching uncertainties:
1. Oakland’s extended bullpen exposure can supply the Texas component;
2. Gore’s 4.40 ERA and recent 3 2/3-inning failure preserve a non-zero Athletics component.

The strongest Under path is not “both pitchers are aces”; it is specifically a **Texas-controlled low/separation state** such as 5-1 or 6-1 in which Gore rebounds and Oakland is suppressed. That path is credible and is the main reason Over is a LEAN rather than stronger language.

## I. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Total-direction rule:** only one of Over/Under is recommended; Under remains in the audit ranking only because the full supplied slate must be ranked.

| Rank | Contract | Verdict | Evidence | Why |
|---:|---|---|---|---|
| **1** | **P-239-C03 — Over 7.5 runs** | **LEAN** | MEDIUM-LOW | Best alignment with Oakland’s bullpen-game exposure plus a credible Athletics scoring contribution against volatile Gore. H2H also cleared 7.5 in 7/11, but that is secondary evidence. |
| **2** | **P-239-C02 — Texas Rangers -1.5** | **LEAN** | MEDIUM-LOW | Direct separation path against the Athletics relief chain; yesterday’s 8-1 result is illustrative, not a repeat assumption. Low-total 5-1/6-1 branches also support this row. |
| **3** | **P-239-C01 — Athletics +1.5** | **FORCED RANK** | LOW-MEDIUM | Positive cushion and 7/11 season-series cover history are real structural support, but the current bullpen-game state is materially worse than much of that history. |
| **4** | **P-239-C04 — Under 7.5** | **AVOID / FORCED RANK** | LOW-MEDIUM | Requires the low-conversion branch to dominate both Oakland’s relief exposure and Gore’s current uncertainty. It can win in a Texas 5-1/6-1 script, but it is the weaker total direction. |

### Recommended interpretation
- **Strongest evidence type:** TOTAL first, then TEX separation side.
- **Only total direction recommended:** **Over 7.5**.
- The ranking is not a value/staking recommendation because operator prices and terms were not supplied.
- Because C01/C02 and C03/C04 are exact complements, this slate mechanically produces two winning rows if all contracts have normal action.

## J. Potential winner

**Likely winner: Texas Rangers — LEAN**

This is a separate descriptive winner call, not an additional independent contract. Texas has:
- the more stable starting-pitcher length branch;
- home field;
- a materially better bullpen-exposure setup at cutoff;
- a current opponent forced into a bullpen game;
- a lineup that just generated sustained traffic in the series opener.

The main winner kill path is Gore again failing early while Oakland’s bullpen performs above its current baseline. That is credible enough to keep the winner at LEAN rather than stronger language.

## K. Source/state limitations

1. **Operator not supplied:** exact listed-pitcher, action, shortened-game and extra-inning settlement language is unresolved.
2. **Starters are official probables, not labelled confirmed starters:** MLB says “subject to change.”
3. **Secondary pitcher conflict:** some DFS/lineup pages still displayed stale Athletics pitcher names; MLB official probable-pitcher data controls the frozen participant branch.
4. **Lineups:** match-specific secondary MLB-API-derived lineups were available, but an independently accessible official lineup release was not recovered before cutoff.
5. **Roof:** match-specific secondary data says closed; the venue’s retractable-roof status is official, but same-game official roof confirmation was not independently recovered.
6. **Recent-window data:** some StatMuse L15/L20 searches exposed different retrieval snapshots. The direction was not allowed to depend on choosing the most favourable stale value.
7. **No calibrated model exists:** all scenario bands are qualitative.

## L. Frozen user-facing forecast

### Identity first
The request’s Nola/Pfaadt instruction does **not** match this event. MLB’s current official probable-pitcher board lists **Brady Basso for the Athletics and MacKenzie Gore for Texas**. The game is scheduled for **Tuesday, September 1 at 7:05 PM CDT at Globe Life Field**, which is **Wednesday, September 2 at 10:05 AM AEST**. The cutoff was frozen about 12 minutes before scheduled first pitch.

### Best four supplied contracts
1. **Over 7.5 runs — LEAN**
2. **Texas Rangers -1.5 runs — LEAN**
3. **Athletics +1.5 runs — FORCED RANK**
4. **Under 7.5 runs — AVOID / FORCED RANK**

### Why Over 7.5 is #1
The cleanest current mechanism is the **Athletics’ bullpen-game exposure**. Basso is not being treated as a normal starter-length arm; Oakland must cover a large number of outs with a relief group that has been under heavy pressure, while Texas got seven innings from deGrom in the prior game and enters with the better immediate bullpen availability profile. Texas therefore has a credible 5-6+ run component without requiring an extreme offensive game.

The other half of the Over is that Gore is not a shut-down certainty. His latest start ended after 3 2/3 innings with four runs, eight hits and four walks allowed. That does not mean another poor start is automatic, but it keeps Athletics 2-4 run states ordinary enough that Texas 5-6 runs can clear 7.5.

The strongest Under kill path is a **Texas-controlled 5-1 or 6-1** game: Gore rebounds, Oakland remains suppressed, and the Rangers win comfortably without the Athletics contributing enough. That branch is credible, so the Over is a lean rather than a high-confidence claim.

### Why Texas -1.5 is #2
The Athletics’ +1.5 has the structurally easier contract and covered 7 of 11 season meetings before this game, but the current state is materially different from much of that history. Oakland is using an opener/bullpen configuration and comes off an 8-1 loss in which the relief staff again had to absorb substantial work. Texas’ central separation paths are 5-3, 6-3 and 6-2; a Gore rebound also produces low-total separation paths such as 5-1 or 6-1.

### Why Athletics +1.5 is not discarded
It still has a real path. Texas is only 5-6 against Oakland this season, and Gore has been volatile enough that a 4-3/5-4 game or an Athletics outright win cannot be treated as remote. That is why Texas -1.5 is only second and not a strong-confidence selection.

### Total-direction control
**Recommend only Over 7.5 among the two total directions.** Under 7.5 is retained solely because the full supplied audit slate must receive a unique rank.

### Likely winner
**Texas Rangers — LEAN.**

This winner call is not a fifth independent pick.

### Publication boundary
No internally calibrated probability, expected value, market edge, ROI or staking claim is published. Operator/odds were not supplied and exact action/listed-pitcher settlement language remains unknown.

## M. Append confirmation

- Complete frozen forecast appended before delivery: **YES**
- Frozen cutoff before scheduled start: **YES**
- Google Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-240

The connected Drive canonical top snapshot still states `Next canonical ID: P-239` because Google Drive is read-only in this workspace. The local running continuation already contains the frozen, issued `P-239` Athletics @ Texas Rangers card. Reusing `P-239` for a distinct event would violate the one-event/one-canonical-ID invariant. Therefore this distinct event is appended locally as **P-240**, with the Drive/local sequence divergence explicitly quarantined for later canonical integration. No Drive file was modified.

---

# P-240 — Chicago White Sox @ Houston Astros — MLB — 2026-09-01 CDT / 2026-09-02 AEST

## A. Frozen identity and state

- **Append sequence:** P-240
- **Request date:** 2026-09-02 Australia/Melbourne
- **Final state/starter refresh:** 2026-09-02 09:59:52 Australia/Melbourne/Australia-Sydney equivalent (AEST, UTC+10)
- **Information cutoff:** 2026-09-02 09:59:52 AEST
- **Scheduled first pitch:** 2026-09-01 19:10 CDT / 2026-09-02 10:10 AEST
- **Cutoff invariant:** PASS — frozen approximately 10 minutes before scheduled first pitch.
- **GAME-STATE:** PREGAME
- **Sport:** Baseball
- **Competition:** MLB regular season
- **Official fixture:** Chicago White Sox @ Houston Astros
- **Venue:** Daikin Park, Houston, Texas
- **Home/away:** White Sox away; Astros home
- **Current records at cutoff:** CWS 72-65; HOU 70-68
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-BASEBALL
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective state:** NOT PERFORMED

## B. Starter identity handshake

MLB's field-owning probable-pitcher page at the frozen cutoff listed:

| Role | Team | Participant | Status | Frozen official line |
|---|---|---|---|---|
| Starting pitcher | CWS | Sean Burke, RHP | PROBABLE_OFFICIAL | 7-6, 3.32 ERA, 161 SO |
| Starting pitcher | HOU | Ronel Blanco, RHP | PROBABLE_OFFICIAL | 0-1, 7.71 ERA, 20 SO |

Both are labelled subject to change by MLB. The card therefore uses official probable status rather than calling either pitcher `CONFIRMED_OFFICIAL`.

### Burke current-regime branch
- Season centre remains strong: 3.32 ERA / 1.15 WHIP through 149 IP in the current public stat line.
- His latest five starts were less stable: 24 2/3 IP, 13 ER, 13 BB, 21 K, five HR (4.74 ERA over that window).
- Most recent start (Aug. 26 vs Texas): 3 IP, 2 ER, **8 walks**. This is a material command-width signal, not a permanent coefficient.
- Previous start vs Houston (July 25): 6 IP, 3 R / 2 ER, 10 K in a 4-1 White Sox loss. Houston therefore has a credible Burke-scoring branch even though Burke owns the superior season profile.

### Blanco current-regime branch
- Blanco returned during 2026 after Tommy John surgery in 2025.
- MLB season line at cutoff: 23 1/3 IP, 7.71 ERA, 1.46 WHIP.
- His five MLB appearances before this game included:
  - July 26 at CWS: 5 1/3 IP, 5 ER, 2 HR; White Sox won 12-3.
  - Aug. 1 vs TEX: 4 2/3 IP, 3 ER.
  - Aug. 7 at SD: 4 2/3 IP, 3 ER.
  - Aug. 15 vs SEA (relief): 4 IP, 5 ER.
- After being optioned, his two most recent Triple-A starts totalled 7 1/3 IP with **12 earned runs, 13 hits, three HR and four walks allowed**.
- He is recalled specifically to start P-240 because Houston's rotation depth is strained.
- This is a current-regime uncertainty state: the prior 2024 reputation does not override the 2026 post-surgery performance branch.

## C. Decision set / contract freeze

- **decision_set_id:** P-240-DS01
- **candidate origin:** USER_SUPPLIED
- **operator:** NOT SUPPLIED
- **odds:** NOT SUPPLIED
- **listed-pitcher/action rule:** UNKNOWN_DEFINITION
- **shortened/suspended-game operator rule:** UNKNOWN_DEFINITION
- **sporting-target assumption:** MLB official full-game final score, including regular-season extra innings if played.
- **MLB extra-inning state:** regular-season innings after the ninth begin with the automatic runner on second.
- **operator caveat:** the sporting target above does not establish how an unnamed sportsbook grades action if a listed pitcher changes or the game is suspended/shortened.

### Slate geometry

The supplied side contracts are **not opposites**:

- CWS +1.5 wins if Chicago wins or loses by exactly one.
- HOU +1.5 wins if Houston wins or loses by exactly one.
- **Both +1.5 contracts win in any one-run final.**
- If either team wins by 2+, only that winning team's +1.5 row wins.

The total pair is an exact half-run complement:
- Over 8.5 vs Under 8.5.
- Recommend only one total direction.

| Candidate ID | Contract | Geometry | Dependence |
|---|---|---|---|
| P-240-C01 | White Sox +1.5 | Overlaps C02 in one-run games | P240-MARGIN |
| P-240-C02 | Astros +1.5 | Overlaps C01 in one-run games | P240-MARGIN |
| P-240-C03 | Over 8.5 | Exact complement of C04 | P240-TOTAL |
| P-240-C04 | Under 8.5 | Exact complement of C03 | P240-TOTAL |

## D. Lineup gate

The MLB starting-lineup page still displayed both batting orders as **TBD** at the final cutoff.

Therefore:
- official batting orders, catcher and defensive alignment did not fully pass `BB-P2`;
- team-level rows remain rankable under explicit lineup mixtures;
- lineup-specific/platoon claims are evidence-capped;
- no secondary projected lineup is promoted to `CONFIRMED_OFFICIAL`.

Current secondary game-day reporting indicated:
- Randal Grichuk expected in RF for Chicago;
- Jose Altuve returning to Houston's lineup after resting in the series opener.

A separate secondary lineup page published a complete proposed order, but because the field-owning MLB lineup page remained TBD, it is retained as corroboration only.

## E. Venue, roof and weather

- **Venue class:** RETRACTABLE
- **Venue:** Daikin Park
- Astros' official park information confirms a retractable roof.
- Official roof guidelines permit/encourage a closed start for rain threat and relevant heat/wind conditions.
- Match-window Houston weather was materially adverse: Tropical Storm Edouard had made landfall and current Houston forecasts showed rain/thunderstorm risk through the game window.
- A current secondary baseball weather report stated that the Daikin Park roof would be **closed** for the game.
- Because no same-game Astros/MLB field-owner roof announcement was independently recovered, the frozen roof status is:
  **LIKELY CLOSED / SECONDARY CONFIRMATION — NOT FIELD-OWNER CONFIRMED.**

Mechanism:
- If closed as expected, outdoor rain/wind do not receive a run-direction adjustment.
- The storm remains operational/context evidence (travel/access/roof certainty), not an automatic Under or Over signal.

## F. Bullpen availability and recent workload

### Houston
The Astros' current relief environment is a real uncertainty:
- recent reporting described **mounting bullpen fatigue** after a long run of short starts;
- no Houston starter had completed six innings for an extended August stretch in the cited current report;
- bullpen ERA was reported around 4.14 for August in that workload discussion.
- In the Aug. 31 series opener, Houston used:
  - Enyel De Los Santos: 1.0 IP,
  - Bennett Sousa: 1.1 IP,
  - Steven Okert: 1.0 IP,
  - Bryan Abreu: 1.0 IP.
- Josh Hader did **not** appear in that game and current reporting described his long scoreless streak, preserving a high-leverage late-inning branch if Houston leads closely.
- Blanco's uncertain length creates a non-trivial probability of needing another 4+ bullpen innings.

### Chicago
- In the Aug. 31 opener, Chicago used:
  - Trevor Richards: 2.1 IP,
  - Tyler Davis: 1.0 IP.
- A current two-week relief split placed the White Sox bullpen around a **2.97 ERA** over the retrieved period.
- Sean Newcomb has been an important multi-role relief arm.
- Chicago's immediate bullpen state is not perfectly fresh, but the retrieved recent performance and prior-day workload are less concerning than Houston's broader repeated-short-start burden.

**Bullpen conclusion:** late-inning state modestly favours CWS relative to HOU, but score-state usage matters; Houston's best leverage arm remains a strong close-game branch.

## G. Recent-form and H2H window block

### Team scoring form
Current StatMuse retrievals were used as descriptive windows and were not counted as independent confirmations when they overlapped.

| Team | L5 | L10 | L15 | L20 / current longer read | Interpretation |
|---|---:|---:|---:|---:|---|
| CWS | ~3.6 R/G in retrieved L5 snapshot | 4.7 R/G | 5.2 R/G | ~4.6-5.35 R/G across timestamped L20 snapshots | Stronger medium window than immediate L5; recent clutch execution has cooled |
| HOU | ~4.4 R/G | ~4.1-4.7 R/G depending retrieval timestamp | ~4.0-4.9 R/G depending timestamp | ~4.5-4.9 R/G in later-summer snapshots | Ordinary-to-good scoring; short-window rebound but not a runaway scoring regime |

Timestamped StatMuse pages exposed different snapshots for several L15/L20 queries. This is logged as a source-timing conflict rather than cherry-picked.

Additional current-period context:
- White Sox: 4.81 R/G since Aug. 1 in the retrieved current split.
- White Sox pitching: 4.56 team ERA since Aug. 1.
- Houston pitching: 4.85 team ERA over the retrieved Aug. 18-Sep. 1 window.
- Houston: 4.19 R/G over the retrieved Aug. 2-Sep. 1 window.

### 2026 direct meetings before P-240
Current completed 2026 meetings:
1. July 24: HOU 9-5 CWS
2. July 25: HOU 4-1 CWS
3. July 26: CWS 12-3 HOU
4. Aug. 31: HOU 6-3 CWS

Derived descriptive facts:
- Houston leads the completed 2026 series **3-1**.
- Over 8.5 occurred **3 of 4**.
- CWS +1.5 covered **1 of 4**.
- HOU +1.5 covered **3 of 4**.
- Burke's direct start: HOU won 4-1 despite Burke pitching well.
- Blanco's direct start: CWS won 12-3 and scored five earned runs against Blanco.

### H2H continuity
**LIMITED-MODERATE.**
Current core hitters overlap meaningfully, and both probable pitchers have direct 2026 matchup evidence. However:
- Blanco's post-surgery state is evolving;
- bullpen health/workload changes quickly;
- roster expansion and September additions change depth;
- four same-season games remain too small to become a rate coefficient.

The H2H block therefore supports the scenario tree but does not control it.

## H. Reference base-rate anchor

No internal probability is generated.

| Contract | Structural/base-rate band | Event adjustment | Frozen qualitative band |
|---|---|---|---|
| White Sox +1.5 | HIGH for a +1.5 cushion in a near-even MLB matchup | Up/hold: superior SP centre and Blanco current-regime risk | HIGH |
| Astros +1.5 | HIGH for a +1.5 cushion in a near-even MLB matchup | Hold: home field/offence, but SP disadvantage | HIGH / slightly below C01 |
| Over 8.5 | MEDIUM | Up: Blanco regime + Burke recent command width + Houston bullpen length risk | MEDIUM-HIGH |
| Under 8.5 | MEDIUM | Down: must suppress Blanco/relief upper tail and Burke's recent volatility | MEDIUM-LOW |

External same-day market pages independently showed a near-coinflip moneyline and a modest Under lean at one sportsbook snapshot. Those prices are **not** the user's operator, are not used for value, and do not override the sports-only ranking.

## I. Scenario / score-family map

| Family | Representative score | Mechanism | Helps |
|---|---|---|---|
| Low-close | CWS 4-3 / HOU 4-3 | Burke stabilises; Blanco has best post-return start; bullpens suppress | Both +1.5, Under |
| CWS low-separation | CWS 5-2 / 5-3 | Blanco short/inefficient; Chicago pen holds | CWS +1.5, often Under at 5-2 |
| HOU low-separation | HOU 5-2 / 5-3 | Burke command issue persists; Blanco survives 5 innings | HOU +1.5, often Under at 5-2 |
| Central-close | CWS 5-4 / HOU 5-4 | Both starters allow traffic; leverage pens contain late damage | Both +1.5, Over |
| CWS high-separation | CWS 7-3 / 8-4 | Blanco/first relief transition fails; Chicago HR/contact cluster | CWS +1.5, Over |
| HOU high-separation | HOU 7-4 / 8-4 | Burke walks/HR cluster; Houston attacks Chicago middle relief | HOU +1.5, Over |
| Extra innings | 5-5 into 10th / 6-5 final | close-game state + automatic runner | both +1.5 often; Over boosted |

### Total 8.5 component budget

Over 8.5 clears through ordinary combinations such as:
- 5-4,
- 6-3,
- 6-4,
- 7-2.

Current process support exists on both sides:
- Chicago scoring path: Blanco's 7.71 MLB ERA, poor direct matchup and poor most-recent Triple-A results.
- Houston scoring path: Burke's recent 4.74 ERA over his last five plus eight walks in his most recent start, combined with Houston's top-order power.

The strongest Under path is a **one-starter-rebounds-and-controls** game:
- Burke gives Chicago 6+ efficient innings and Blanco finally converts his rehab work into a competent 4-5 inning return, followed by strong leverage relief;
- or one lineup produces only one to two runs while the winner stays around four to five.

That Under path is credible, but it requires more simultaneous suppression than the central upper-tail branches.

## J. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Evidence cap:** official batting orders were still TBD at cutoff; all participant-sensitive team conclusions remain below strong publication language.

| Rank | Contract | Verdict | Evidence quality | Main reason |
|---:|---|---|---|---|
| **1** | **P-240-C01 — White Sox +1.5** | **LEAN** | MEDIUM-LOW | The +1.5 cushion starts from a structurally high base rate and Chicago has the better starter centre plus a strong attack path against Blanco's current post-surgery regime. |
| **2** | **P-240-C02 — Astros +1.5** | **LEAN** | MEDIUM-LOW | Houston is still a near-even home side with an effective offence and a +1.5 cushion; both side rows can win in a one-run final. Burke's recent command width prevents this from being treated as merely a hedge. |
| **3** | **P-240-C03 — Over 8.5** | **LEAN** | MEDIUM-LOW | Blanco's current state, Burke's recent control variance, 3/4 2026 H2H Overs and Houston's bullpen-length risk create the stronger total direction. |
| **4** | **P-240-C04 — Under 8.5** | **FORCED RANK / AVOID relative to Over** | LOW-MEDIUM | Viable if Burke controls and Blanco rebounds, but it is the weaker total branch under the current exposure tree. |

### Special-control interpretation
- **Strongest evidence supports a SIDE, specifically White Sox +1.5.**
- The two +1.5 rows overlap; ranking both highly reflects marginal contract likelihood, not an unordered coverage portfolio.
- **Only one total direction is recommended: Over 8.5.**
- Without the user's operator and odds, none of these rows is labelled a value bet.

## K. Likely winner

**Likely winner: Chicago White Sox — LEAN**

Not an additional independent contract.

Primary reasons:
1. Burke's full-season starter centre is materially stronger than Blanco's current 2026 post-surgery regime.
2. Blanco has already been hit hard by this Chicago core and returned from Triple-A after poor latest results.
3. Chicago's recent relief performance is stronger than Houston's broad bullpen-fatigue regime.
4. The White Sox medium-window scoring process is sufficient to exploit a short Blanco start.

Winner kill paths:
- Houston's stronger home power core punishes Burke's recent walk/HR instability.
- Blanco's prior quality returns sharply toward his old baseline.
- Houston reaches Hader with a late lead after a close start.

Winner language remains LEAN because the official batting orders were not fully released through the MLB lineup page at cutoff and because both starter distributions retain wide tails.

## L. Frozen source/state limitations

1. **Operator absent:** listed-pitcher/action, suspended/shortened-game and exact settlement terms unresolved.
2. **Official lineups TBD:** BB-P2 incomplete at cutoff; no secondary full lineup is promoted to official fact.
3. **Starters probable, not confirmed:** MLB explicitly marks probable pitchers subject to change.
4. **Roof:** highly likely closed given tropical weather and secondary game weather reporting, but same-game field-owner roof confirmation was not recovered.
5. **StatMuse recency snapshots:** L15/L20 queries returned timestamp-dependent numbers; conflicts were recorded instead of selected away.
6. **Bullpen availability is score-state specific:** prior-day innings inform exposure but do not mechanically define who will pitch tonight.
7. **No validated numerical model:** no calibrated probabilities, fair odds or value claims.

## M. Frozen user-facing forecast

### Verified event
Chicago White Sox @ Houston Astros, MLB regular season, Tuesday September 1, 2026 at 7:10 PM CDT at Daikin Park — Wednesday September 2 at 10:10 AM AEST.

MLB's probable-pitcher board lists:
- Sean Burke (CWS): 7-6, 3.32 ERA, 161 K
- Ronel Blanco (HOU): 0-1, 7.71 ERA, 20 K

Both remain official probables / subject to change at cutoff.

### Ranking
1. **White Sox +1.5 — LEAN**
2. **Astros +1.5 — LEAN**
3. **Over 8.5 — LEAN**
4. **Under 8.5 — weaker total direction / FORCED RANK**

### Why White Sox +1.5 is #1
The contract has a broad one-run cushion in a matchup that is close at team level, but Chicago owns the cleaner starting-pitcher branch. Burke's season performance is far stronger than Blanco's 2026 post-surgery line. Blanco allowed five earned runs in 5 1/3 innings to Chicago on July 26, then was hit for 12 earned runs across 7 1/3 innings in his two most recent Triple-A starts before this recall. The White Sox therefore have an ordinary scoring route without needing Houston's bullpen to collapse.

Burke is not risk-free: his last five-start ERA is roughly 4.74 and his latest outing included eight walks in three innings. That is why Houston +1.5 also remains very strong.

### Why Astros +1.5 is #2
Houston is at home, has won three of the four completed 2026 meetings, scored six yesterday and has a power core capable of punishing Burke's recent control variance. A one-run finish makes **both** +1.5 contracts win, so the two side rows are not opposites.

I still put Chicago's +1.5 first because the starting-pitcher/current-regime mismatch is the clearest pregame asymmetry.

### Total: Over 8.5 only
The Over is the total direction I recommend.

Blanco creates a direct Chicago upper-tail branch, while Burke's recent walk/HR volatility keeps Houston's 4-5+ run contribution alive. Three of the four completed 2026 meetings have reached at least nine total runs: 9-5, 12-3 and 6-3. That history is supportive only; the decision is driven more by the current pitching/exposure state.

The Under's strongest path is a 4-3, 5-2 or similar game in which Burke stabilises and Blanco posts his best outing of the return. It is credible but requires more suppression assumptions.

### Likely winner
**Chicago White Sox — LEAN.**

This is not a fifth independent pick.

### Environment
Daikin Park is retractable. Houston is under significant Tropical Storm Edouard rain/storm risk during the game window. Current baseball weather reporting expects the roof closed, which would largely neutralise wind/rain effects on the batted-ball environment. Same-game official roof confirmation was not recovered at cutoff, so it remains a likely—not confirmed—closed-roof branch.

### Settlement/publication boundary
No operator or odds were supplied. Listed-pitcher/action rules, shortened-game treatment and sportsbook extra-inning grading remain unknown. The sports analysis assumes the MLB official full-game result, including regular-season extras. No calibrated probability, expected value, edge, ROI or staking claim is published.

## N. Append confirmation

- Complete frozen P-240 forecast appended before delivery: **YES**
- Scheduled-start cutoff invariant passed: **YES**
- Drive modified: **NO**
- Prior issued forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-241

The connected Drive canonical top snapshot remains stale at `Next canonical ID: P-239` because Drive is read-only. The local append-only continuation already contains issued P-239 and P-240 cards. Reusing either ID would violate the one-distinct-event/one-ID rule. This event is therefore appended locally as **P-241**, with the Drive/local integration gap explicitly preserved. No Drive file is modified.

---

# P-241 — Zachary Svajda vs Daniel Altmaier — 2026 US Open Men's Singles R1

## A. Frozen identity and state

- **Append sequence:** P-241
- **Request date:** 2026-09-02 Australia/Sydney
- **Final state check:** approximately 2026-09-02 10:10 AEST / 2026-09-01 20:10 EDT
- **Information cutoff:** 2026-09-02 10:10 AEST
- **Sport:** Tennis
- **Competition:** 2026 US Open
- **Draw:** Men's Singles
- **Round:** First round / Round of 128
- **Players:** Zachary Svajda (USA) vs Daniel Altmaier (GER)
- **Court:** Court 12
- **Surface:** Outdoor hard
- **Format:** Best-of-five sets
- **Final-set rule:** at 6-6 in the deciding set, a first-to-10 tiebreak with two-point margin applies under the Grand Slam rule.
- **Original schedule state:** scheduled on Tuesday Sep. 1 New York time, but rain delayed the outside-court order.
- **Frozen GAME-STATE:** **DELAYED / NOT STARTED — RAIN; 0-0 / UPCOMING on the current secondary score surfaces**
- **State evidence:** Tennis.com still displayed the match as `Upcoming`; Sportschau displayed 0-0 and reported rain-delayed Court 12 sequencing; current Flushing conditions showed light rain.
- **Start-crossing treatment:** this is not labelled PREGAME because the original scheduled time passed. It is a verified delayed/not-started state, with no live points/games imported.
- **Current ranking:** Altmaier #57; Svajda #80
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-TENNIS
- **Tennis numerical status:** NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL APPROVED OR FIT
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective performed:** NO

## B. Contract freeze and operator boundary

### User-supplied slate
1. Daniel Altmaier +2.5 games
2. Zachary Svajda -2.5 games
3. Total games Over 39.5
4. Total games Under 39.5

- **Operator:** NOT SUPPLIED
- **Odds:** NOT SUPPLIED
- **Retirement/walkover rules:** `UNKNOWN_DEFINITION`
- **Completed-set / full-match requirement:** `UNKNOWN_DEFINITION`
- **Void rule:** `UNKNOWN_DEFINITION`
- **No value claim permitted.**

A current Australian sportsbook page located during research showed a different total (`38.5`) and required full match completion for its own contracts. That is only an external market/state cross-check. It is **not** adopted as the user's settlement rule and it does not change the user's 39.5 target.

### Settlement geometry
- Altmaier +2.5 and Svajda -2.5 are exact game-margin complements under normal full-completion rules.
- Over 39.5 and Under 39.5 are exact total-game complements.
- With ordinary completed-match grading and no retirement/void complication, exactly **two of the four supplied rows win**.
- The forced 2-of-4 arithmetic is contract geometry, not model accuracy.

| ID | Contract | Geometry | Dependence group |
|---|---|---|---|
| P-241-C01 | Altmaier +2.5 games | Exact complement of C02 | P241-MARGIN |
| P-241-C02 | Svajda -2.5 games | Exact complement of C01 | P241-MARGIN |
| P-241-C03 | Over 39.5 games | Exact complement of C04 | P241-TOTAL |
| P-241-C04 | Under 39.5 games | Exact complement of C03 | P241-TOTAL |

## C. Participant/status gate

### Identity
- Official/current US Open coverage identifies Svajda vs Altmaier as a first-round match.
- Current rankings source: Altmaier #57, Svajda #80.
- No withdrawal/walkover was found at cutoff.
- No credible current injury report was found that justified a directional medical adjustment.
- Current score surfaces still showed the match as upcoming/0-0 following rain delay.

### Retirement status
Because the user did not identify the operator, the framework's retirement-term hard gate remains unresolved:
`TE-P3 = UNKNOWN_DEFINITION / NO VALUE DETERMINABLE`.

No row is described as value-supported.

## D. Current regime and surface profile

### Zachary Svajda
Current official ATP profile:
- Rank #80.
- 2026 ATP-level W-L: 9-13.
- Career ATP-level service games won: 75%.
- Career ATP-level return games won: 18%.
- First-serve points won: 70%.
- Second-serve points won: 49%.
- Return points won: 35%.

Current 2026 hard-court top-level sequence includes:
- L to Mattia Bellucci, Cincinnati: 7-6, 7-6.
- L to Arthur Fils, Canada: 6-4, 3-6, 6-1.
- W vs Denis Shapovalov after split sets, retirement at 3-0 in set three.
- L to Aleksandar Vukic, Washington: 6-3, 6-1.
- Earlier hard wins over Marin Cilic and Aleksandar Kovacevic.

Cross-level 2026 hard record from the broad results database is materially stronger (17-9), but that includes Challenger/qualifying populations and is **not** treated as exchangeable with main-tour US Open play.

Grand Slam/current-development signal:
- 2026 Roland Garros: fourth round.
- 2026 Wimbledon: third round.
- 2025 US Open: took a set from Novak Djokovic in round two.
These support improved best-of-five competence but do not create a fitted edge.

### Daniel Altmaier
Current ranking #57.
Official ATP career profile:
- Service games won: about 77%.
- Return games won: 18%.
- First-serve points won: about 71%.
- Second-serve points won: 48%.
- Return points won: 35%.

Broad 2026 results database:
- Overall: 20-26.
- Hard: 3-9.
Recent hard sequence:
- L Ignacio Buse, Winston-Salem: 7-6, 7-5.
- W Francisco Comesana: 6-1, 7-6.
- L Lorenzo Musetti, Cincinnati: 6-4, 6-2.
- W Coleman Wong: 3-6, 6-3, 6-4.
- L Brandon Nakashima, Canada: 6-2, 6-1.
- A long three-set Canada win over Aleksandar Vukic showed 11 aces and a 63% total service-point win rate.

Altmaier therefore carries:
- the higher ranking;
- slightly stronger broad career hold profile;
- but a materially weaker 2026 hard-surface result regime.

The current-surface regime is allowed to narrow the ranking prior, not erase it.

## E. Head-to-head continuity audit

### Verified meetings
The available broad H2H history is **Altmaier 2-0**:
1. 2021 Puerto Vallarta Challenger QF: Altmaier won 4-6, 7-6, 6-3.
2. 2023 Dallas ATP R32: Altmaier won 6-2, 6-4.

ATP's official Dallas archive verifies the 2023 6-2, 6-4 win.

### Provider discrepancy
One structured H2H source returned only the 2021 Challenger meeting, while ATP/other specialist records verify the 2023 Dallas match as well. The discrepancy is preserved rather than silently harmonised.

### Continuity verdict
**LOW-MODERATE / NON-CONTROLLING.**
Reasons:
- meetings are three and five years old;
- one is Challenger level;
- the 2023 Dallas match was indoor hard, while this is outdoor hard;
- Svajda has materially developed since those meetings;
- current 2026 hard form points differently from the old H2H.

Therefore old H2H is a kill-path reminder for the Svajda side, not the controlling prior.

## F. Recency and trend windows

The tennis rules require L5/L10/L15/L20 on the exact surface. Available current databases did not expose every requested serve/return metric at all four windows with one stable provider definition. This is recorded as partial-source coverage rather than backfilled.

### Surface-result windows
- **Svajda:** recent ATP hard results are mixed and mostly against strong opposition; broad all-level 2026 hard record is positive but includes lower-level events.
- **Altmaier:** broad 2026 hard record is 3-9; latest four hard matches alternate W/L, with straight-set losses to Buse and Musetti and wins over Comesana/Wong.
- **Trend verdict:** `NO TREND — NOISE` for short-window W/L. Neither player's L5-style sequence is monotone enough to justify a trend extrapolation.
- **Longest defensible current-surface read:** Svajda's 2026 hard regime is better than Altmaier's after level adjustment, but the difference is moderate rather than decisive.

### Match-length signal
Svajda's latest top-level hard matches include:
- two tiebreak sets vs Bellucci;
- a three-set loss to Fils;
- a retirement after two split sets vs Shapovalov.
Altmaier's recent hard matches include:
- 7-6, 7-5 vs Buse;
- 6-1, 7-6 vs Comesana;
- a three-set win over Wong;
- a long three-set win over Vukic in Canada.

This raises the close-set/tiebreak branch, but a 39.5-game best-of-five total still requires enough set count and closeness; close individual sets alone do not guarantee the Over.

## G. Environment / delay gate

- **Venue:** USTA Billie Jean King National Tennis Center, Flushing, New York.
- **Court:** Court 12.
- **Venue state:** OUTDOOR.
- **Current condition around final refresh:** light rain in Flushing.
- National Weather Service evening forecast around the delayed window:
  - approximately 24°C / mid-70s °F;
  - high humidity around 87-90%+;
  - E/NE wind around 5 mph, later 5-7 mph;
  - rain/thunderstorm probability remained material during the early evening and then declined later.
- Severe-weather/rain conditions already caused schedule disruption on outside courts.

Mechanism:
- the primary effect is **delay and uncertain resumption**, not an automatic Over/Under sign;
- humid/damp conditions can slow play and alter ball/court feel, but the directional magnitude is not verified strongly enough to move a contract band;
- rest/waiting affects both players and is not assigned one-sided fatigue without evidence.

Environment therefore widens timing/conditions uncertainty but does not drive the ranking.

## H. Score-tree construction

### Qualitative set-count weights
These are **relative scenario weights, not probabilities**:
- 3-set endpoint: **3/5**
- 4-set endpoint: **4/5** — central
- 5-set endpoint: **2/5**

Rationale:
- Svajda has the current-surface winner edge, but not enough separation for straight-set control to dominate;
- Altmaier retains ranking, serve and H2H-based resistance;
- five sets is live but not the central branch.

### Mandatory two-sided branches

**TE-B1 — Svajda straight-set control**
Representative: 6-4, 6-3, 6-4.
- Total = 29 games.
- Svajda game margin = +7.
- Wins: Svajda -2.5, Under 39.5.

**TE-B2 — Svajda close straight sets**
Representative: 7-6, 6-4, 7-6.
- Total = 36.
- Margin = +4.
- Wins: Svajda -2.5, Under 39.5.

**TE-B3 — Svajda extended/deciding control**
Representative four-set central: 6-4, 4-6, 6-3, 6-4.
- Total = 39.
- Margin = +5.
- Wins: Svajda -2.5, Under 39.5.
Alternative close four-set: 7-6, 4-6, 6-4, 7-6.
- Total = 46.
- Margin = +2.
- Wins: Altmaier +2.5, Over 39.5 despite a Svajda match win.

**TE-B4 — Altmaier straight-set control**
Representative: 6-4, 6-4, 6-3.
- Total = 29.
- Wins: Altmaier +2.5, Under 39.5.

**TE-B5 — Altmaier close straight sets**
Representative: 7-6, 6-4, 7-5.
- Total = 36.
- Wins: Altmaier +2.5, Under 39.5.

**TE-B6 — Altmaier extended win**
Representative: 4-6, 6-4, 6-3, 3-6, 6-4.
- Long five-set state; generally supports Altmaier +2.5 and Over 39.5.

**TE-B7 — best-of-five extension state**
- Five sets materially raises the Over opportunity but does not mathematically guarantee Over 39.5 because extremely one-sided individual sets can keep total games below the line.
- Normal close five-set score families strongly favour the Over.

**TE-B8 — retirement/withdrawal**
- Operator terms unknown.
- No settlement assumption is imported.

## I. Base-rate anchors and contract interpretation

No calibrated probabilities are issued.

### Under 39.5
**Base-rate band: MEDIUM-HIGH**
- 39.5 is a relatively demanding best-of-five total.
- Most normal three-set outcomes finish comfortably below.
- Many efficient four-set outcomes also remain below or near 39.
- Over requires either sufficient four-set closeness or a normal-length five-set branch.

### Over 39.5
**Base-rate band: MEDIUM-LOW**
- Needs extension and/or close sets.
- Recent tiebreak exposure supports it, but does not outweigh the structural set-count requirement.

### Altmaier +2.5 games
**Base-rate band: MEDIUM**
- Positive game cushion benefits from any Altmaier outright win.
- It can also cover in a very close Svajda four/five-set win.
- Old H2H and higher ranking help only modestly after the current-surface audit.

### Svajda -2.5 games
**Base-rate band: MEDIUM**
- Svajda is the current-surface winner lean.
- A typical 3-0 or ordinary 3-1 Svajda win usually clears -2.5.
- It fails in a close Svajda win with net game margin of only 1-2.

### External market sanity check — not user pricing
A current public Australian market snapshot found:
- Svajda match winner around 1.57 vs Altmaier 2.24;
- Svajda -2.5 around 1.87 vs Altmaier +2.5 around 1.82;
- total at 38.5, with Under slightly shorter than Over.

This is **external market evidence only**:
- not the user's operator;
- not the user's 39.5 total;
- not an internal model probability;
- not sufficient for value.

It does, however, corroborate the structural distinction: Svajda can be the more likely winner while Altmaier +2.5 is marginally easier than Svajda -2.5.

## J. Strongest kill paths

### Against Under 39.5
- Four competitive sets with one or more tiebreaks.
- Normal five-set extension.
- Altmaier serving well enough to keep sets close while Svajda still wins.

### Against Altmaier +2.5
- Svajda's current-surface edge converts to ordinary break separation rather than only match-win probability.
- Representative 6-4, 6-3, 4-6, 6-4 type score makes Altmaier lose the game handicap comfortably.

### Against Svajda -2.5
- Altmaier outright win.
- Svajda wins only by 1-2 net games in a close 4/5-set match.
- Old H2H tactical comfort reappears despite low continuity.

### Against Over 39.5
- Any routine straight-set result.
- Efficient four-set result around 36-39 games.
- One player's return pressure creates lopsided sets rather than tiebreak-heavy sets.

## K. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Retirement terms:** UNKNOWN_DEFINITION

| Rank | Contract | Verdict | Evidence quality | Reason |
|---:|---|---|---|---|
| **1** | **P-241-C04 — Under 39.5 games** | **LEAN** | MEDIUM-LOW | Most three-set states and many ordinary four-set states settle below 39.5. The match is competitive enough for four sets, but five sets is not the central branch. |
| **2** | **P-241-C01 — Altmaier +2.5 games** | **LEAN** | MEDIUM-LOW | The +2.5 cushion captures every Altmaier win and close Svajda wins; ranking/H2H resistance keeps this live even though Svajda is the winner lean. |
| **3** | **P-241-C02 — Svajda -2.5 games** | **FORCED RANK / LEAN-ADJACENT** | MEDIUM-LOW | Svajda has the better current hard-surface regime and likely-winner edge, but -2.5 needs that edge to convert into at least three net games. |
| **4** | **P-241-C03 — Over 39.5 games** | **FORCED RANK / AVOID relative to Under** | LOW-MEDIUM | Tiebreak/extension risk exists, but 39.5 still requires enough four-set closeness or a normal five-set state. It is the weaker total direction. |

### Total-direction control
Recommend **Under 39.5 only** among the two opposing total directions.

## L. Potential winner

**Zachary Svajda — LEAN**

This is a separate descriptive winner call, not a fifth independent contract.

Why:
1. Svajda's 2026 outdoor-hard/current-surface regime is stronger after accounting for Altmaier's 3-9 broad hard record.
2. Svajda has shown improving best-of-five competence in 2026 with deep Roland Garros and Wimbledon runs.
3. His recent losses include high-level opponents and a two-tiebreak loss, suggesting the raw W-L understates competitiveness.
4. External market and current match-preview sources also make Svajda the favourite, but those are corroboration only.

Why not stronger:
- Altmaier is ranked higher (#57 vs #80).
- Altmaier leads the broad H2H 2-0.
- Career ATP serve/return summaries are similar rather than clearly Svajda-dominant.
- Current hard samples are sparse and level-mixed.
- Rain delay and unknown operator retirement terms widen uncertainty.

## M. Frozen user-facing forecast

### Event/status
Zachary Svajda vs Daniel Altmaier is a **2026 US Open men's singles first-round match on outdoor hard court, best-of-five**. At the final research refresh the original start had passed because rain disrupted outside courts, but current score surfaces still showed **0-0 / Upcoming**, so this card is frozen as **DELAYED / NOT STARTED**, not as a stale pregame state.

### Best 4 supplied picks
1. **Under 39.5 total games — LEAN**
2. **Daniel Altmaier +2.5 games — LEAN**
3. **Zachary Svajda -2.5 games — lower-confidence directional side**
4. **Over 39.5 total games — weaker total direction**

### Why Under 39.5 is #1
This line is high enough that the match needs meaningful extension. A normal straight-set result is comfortably Under, and many ordinary four-set outcomes also stay below the line. My central set-count branch is four sets, but not necessarily four very close sets.

A representative central Svajda score such as **6-4, 4-6, 6-3, 6-4** totals 39 games. A routine Altmaier straight-set upset also lands far Under. The Over becomes strongest if the match produces tiebreak-heavy four sets or a normal five-set extension.

Recent hard matches for both players contain several close sets/tiebreaks, so the Over is not dismissed. It is simply the weaker side of 39.5.

### Why Altmaier +2.5 is #2 even though Svajda is the likely winner
The game handicap and match winner are different targets. Altmaier +2.5 wins if Altmaier wins the match **or** if Svajda wins but finishes only one or two net games ahead.

Altmaier is the higher-ranked player and leads the old H2H, while his recent hard matches include multiple close-set states. Those factors preserve a close-match branch.

The reason I still make Svajda the likely winner is current surface regime: Altmaier's 2026 broad hard record is only 3-9, while Svajda has shown more competitive hard play and much stronger Grand Slam development this year. The old H2H is too stale and format/level-mixed to override that.

### Why Svajda -2.5 is #3
If Svajda wins in the ordinary 3-0 or non-razor-thin 3-1 score families, he usually covers -2.5. His current hard-court condition and recent Slam progression give him the winner edge.

But this handicap is harder than simply picking him to win. A close four- or five-set Svajda victory can fail -2.5 while Altmaier +2.5 wins. That is why the Altmaier cushion ranks slightly higher than the Svajda negative handicap.

### Likely winner
**Zachary Svajda — LEAN.**

Not an additional independent pick.

### Weather/delay
Court 12 is outdoors. Rain and thunderstorms disrupted the evening schedule in Flushing; at the final refresh current conditions still showed light rain and the match remained delayed/not started. The main impact is uncertainty in start time and conditions, not an automatic total direction.

### Settlement/publication boundary
The user's operator and retirement terms were not supplied. Tennis handicap and total markets can grade differently after retirement, so the exact settlement definition remains `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking claim is published.

## N. Append confirmation

- Complete frozen P-241 forecast appended before delivery: **YES**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-242

The connected Drive canonical top snapshot remains at `Next canonical ID: P-239` because Google Drive is read-only. The local append-only continuation already contains issued P-239, P-240 and P-241 cards. Reusing any of those IDs for a distinct event would violate the one-event/one-canonical-ID invariant. This event is therefore appended locally as **P-242**, with the Drive/local integration gap explicitly preserved for later canonical reconciliation. No Drive file is modified.

---

# P-242 — Fabian Marozsan vs Michael Zheng — 2026 US Open Men's Singles R1

## A. Frozen identity and state

- **Append sequence:** P-242
- **Request date:** 2026-09-02 Australia/Sydney
- **Final state refresh:** 2026-09-02 10:17:49 AEST
- **Information cutoff:** 2026-09-02 10:17:49 AEST
- **Sport:** Tennis
- **Competition:** 2026 US Open
- **Draw:** Men's Singles
- **Round:** First round / Round of 128
- **Players:** Fabian Marozsan (HUN) vs Michael Zheng (USA)
- **Court:** Court 11
- **Surface:** Outdoor hard
- **Format:** Best-of-five sets
- **Final-set format:** Grand Slam deciding-set tiebreak at 6-6, first to 10 points by two.
- **Current ranking:** Marozsan #63; Zheng #107 on current match page
- **GAME-STATE:** **DELAYED / NOT STARTED — rain-disrupted outside-court schedule**
- **State evidence:** current Tennis.com/TNT-style match surfaces continued to show `Upcoming` / `Not started`; no set/game/point state was verified. A structured bracket feed contained a premature `live` flag with no score before its own listed start time, so that state flag was quarantined as internally inconsistent.
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-TENNIS
- **Tennis numerical state:** NO TARGET/SOURCE CARD, DATASET OR MODEL APPROVED OR FIT
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective performed:** NO

## B. Contract freeze

### User-supplied audit slate
1. Fabian Marozsan +2.5 games
2. Michael Zheng -2.5 games
3. Total games Over 38.5
4. Total games Under 38.5

- **Operator:** NOT SUPPLIED
- **Odds:** NOT SUPPLIED
- **Retirement/walkover rule:** UNKNOWN_DEFINITION
- **Completed-match requirement:** UNKNOWN_DEFINITION
- **Void/partial-set treatment:** UNKNOWN_DEFINITION
- **Value publication:** BLOCKED

### Geometry
- Marozsan +2.5 and Zheng -2.5 are exact game-margin complements under normal full-match grading.
- Over 38.5 and Under 38.5 are exact total-game complements.
- Under ordinary completed-match terms, exactly two of the four rows settle as wins.
- Retirement/void rules can alter that geometry, so definitive sportsbook settlement requires the unnamed operator's terms.

| ID | Contract | Geometry | Dependence group |
|---|---|---|---|
| P-242-C01 | Marozsan +2.5 games | Complement of C02 | P242-GAME-MARGIN |
| P-242-C02 | Zheng -2.5 games | Complement of C01 | P242-GAME-MARGIN |
| P-242-C03 | Over 38.5 games | Complement of C04 | P242-TOTAL |
| P-242-C04 | Under 38.5 games | Complement of C03 | P242-TOTAL |

## C. Participant, level and current-regime gate

### Fabian Marozsan
- Current ranking: #63.
- Career high: #36.
- 2026 ATP-level record: 19-21 overall; 9-10 on hard in the retrieved season database.
- 2026 ATP-level hard/overall service-return summary:
  - Hold: 76.60%
  - Break: 19.78%
  - First serve in: 65.99%
  - First-serve points won: 69.44%
  - Second-serve points won: 52.47%
  - Return points won: 34.93%
  - Tiebreak record: 13-7
- Career ATP summary is slightly stronger than the current season centre: approximately 79% service games won and 21% return games won.
- Immediate hard-court sequence:
  - L James Duckworth 7-6, 2-6, 4-6 (Winston-Salem QF)
  - W Martin Damm Jr 2-6, 6-3, 6-3
  - W Miomir Kecmanovic 6-3, 6-4
  - L Michael Zheng 6-3, 1-6, 6-7
  - L Matteo Arnaldi 5-7, 6-2, 4-6
- Interpretation: Marozsan has recently rebounded from the Cincinnati loss to Zheng and remains an established ATP-level player. His current hard record is mediocre rather than poor, with a meaningful tiebreak/close-set component.

### Michael Zheng
- Current match-page ranking: #107; recent official ATP material had him around a career-high #106.
- 2026 ATP main-draw sample: 6-8 overall; 4-6 hard in the retrieved main-draw database.
- Main-draw season service-return summary:
  - Hold: 71.60%
  - Break: 23.93%
  - First serve in: 62.01%
  - First-serve points won: 69.30%
  - Second-serve points won: 46.77%
  - Return points won: 36.57%
  - Tiebreak record: 3-7
- Broad all-level hard record is much stronger at roughly 16-7, but that includes qualifying/Challenger-level competition and is not treated as exchangeable with ATP main draw.
- Immediate hard sequence:
  - L Lorenzo Musetti
  - W Ugo Humbert
  - W Fabian Marozsan
  - W Trevor Svajda (qualifying)
  - W Moez Echargui (qualifying)
- Zheng's rise is supported by current US Open/ATP reporting: two-time NCAA champion, strong baseline power from both wings, recent Cincinnati Masters breakthrough and movement toward the top 100.
- Best-of-five evidence exists:
  - 2026 Australian Open win over Sebastian Korda in five sets.
  - 2026 Wimbledon five-set win over Cameron Norrie.
- These Slam results support long-match competence but come from different surfaces and are not copied directly into the hard-court total.

### Level adjustment
Zheng's L5/L10/L15/L20 hard results include ATP qualifying and lower-level matches. Marozsan's recent sample is more main-tour concentrated. Therefore Zheng's raw W-L advantage is shrunk before it affects the winner/handicap tree.

## D. Recency window block — exact surface

### Fabian Marozsan — hard court
| Window | W-L | Win rate | Population note |
|---|---:|---:|---|
| L5 | 2-3 | 40% | ATP-level |
| L10 | 3-7 | 30% | ATP-level |
| L15 | 6-9 | 40% | ATP-level |
| L20 | TRUE COUNT 19: 9-10 | 47.4% | Only 19 current 2026 hard matches available |

**Trend verdict:** NO TREND — NOISE. The windows are not monotone.

### Michael Zheng — hard court
| Window | W-L | Win rate | Population note |
|---|---:|---:|---|
| L5 | 4-1 | 80% | Level-mixed |
| L10 | 6-4 | 60% | Level-mixed |
| L15 | 9-6 | 60% | Level-mixed |
| L20 | 13-7 | 65% | Level-mixed |

**Trend verdict:** NO TREND — NOISE. L5/L10/L15/L20 are not monotone, and the population mix changes across the window.

### Recency conclusion
Zheng has the stronger short-window hard results, but the magnitude is reduced because several wins occurred in qualifying/lower-level populations. Marozsan has more established ATP-level baseline quality and a stronger career hold centre.

## E. Head-to-head continuity audit

### Verified H2H
**Michael Zheng leads 1-0.**

Cincinnati Masters, 2026-08-14, hard court:
- Zheng def. Marozsan **3-6, 6-1, 7-6(7-1)**.

Derived geometry from that match:
- Total games: 29.
- Net game margin: Zheng +3.
- At today's lines:
  - Zheng -2.5 would have won by only 0.5 game.
  - Marozsan +2.5 would have lost by only 0.5 game.

### Continuity
**MODERATE-HIGH for surface/current matchup, but format-limited.**

Positive continuity:
- same hard-court season;
- only about 2.5 weeks ago;
- same players and current technical regimes;
- ATP-level matchup.

Continuity break:
- Cincinnati was best-of-three;
- US Open is best-of-five;
- longer exposure changes fitness, set-count, total-game and game-margin distributions.

Therefore the H2H is materially useful but cannot be turned into an automatic Zheng -2.5 repeat.

## F. Environment / schedule gate

- **Venue:** USTA Billie Jean King National Tennis Center, Flushing, New York
- **Court:** Court 11
- **Venue class:** OUTDOOR
- Heavy rain caused significant delays across the outside courts on the session.
- Current evening forecast around the disrupted window:
  - roughly 23-24°C;
  - dew point around 22°C;
  - relative humidity around 90%+;
  - E/NE wind roughly 5-6 mph;
  - meaningful rain/thunderstorm risk in the early evening, declining later.

Mechanism:
- The primary verified effect is delay and schedule uncertainty.
- High humidity/damp conditions may affect ball/court feel, but no reliable quantitative court-speed change is available.
- No automatic Over/Under or player-side adjustment is assigned.
- Both players face the same waiting disruption; no one-sided fatigue claim is made without evidence.

## G. Serve-return and matchup reconciliation

### Baseline
Marozsan carries the stronger established ATP service-game base:
- 2026 hold ~76.6%;
- career ATP hold near 79%.

Zheng's current main-draw sample shows:
- lower hold (~71.6%);
- higher break/return pressure (~23.9% break, 36.6% return points won);
- but it is a smaller and less stable sample.

### Matchup implication
The Cincinnati meeting demonstrated both directions:
- Marozsan controlled set one 6-3;
- Zheng dominated set two 6-1;
- set three reached a tiebreak.

That is evidence for **variance plus closeness**, not a one-direction blowout template.

The current matchup therefore supports:
1. a narrow Zheng winner lean from recency/direct matchup;
2. a substantial Marozsan +2.5 cushion branch;
3. meaningful four/five-set extension risk.

## H. Set-count mixture

These are **qualitative relative weights, not probabilities**.

| Endpoint | Relative weight | Interpretation |
|---|---:|---|
| 3 sets | 2/5 | Meaningful if either player establishes return dominance |
| 4 sets | **5/5** | Central branch |
| 5 sets | 3/5 | Material because both have long-match competence and the matchup is not strongly separated |

This mixture is fixed before locating the 38.5 line.

## I. Mandatory two-sided score branches

### TE-B1 — Marozsan ordinary straight-set control
Representative: **6-4, 6-4, 6-3**
- 29 total games.
- Marozsan +5 games.
- Wins: Marozsan +2.5, Under 38.5.
- Defeats: Zheng -2.5, Over.

### TE-B2 — Marozsan close straight sets
Representative: **7-6, 6-4, 7-5**
- 35 games.
- Wins: Marozsan +2.5, Under 38.5.

### TE-B3 — Marozsan extended win
Representative: **6-4, 3-6, 7-5, 6-4**
- 41 games.
- Wins: Marozsan +2.5, Over 38.5.

### TE-B4 — Zheng ordinary straight-set control
Representative: **6-4, 6-3, 6-4**
- 29 games.
- Zheng clears -2.5.
- Under 38.5 wins.

### TE-B5 — Zheng close straight sets
Representative: **7-6, 6-4, 7-5**
- 35 games.
- Zheng generally clears -2.5; Under wins.

### TE-B6 — Zheng extended win
**Central coherence scoreline:** **7-6, 4-6, 7-6, 6-4**
- 46 total games.
- Zheng wins the match.
- Net game margin: Zheng +2.
- **Marozsan +2.5 wins.**
- **Over 38.5 wins.**
- Zheng -2.5 loses.

This is the key cross-market branch supporting the top two rankings.

### TE-B7 — Five-set extension
Normal five-set score families strongly support Over 38.5 and tend to reduce the chance of either player creating a large game margin, although lopsided individual sets can still create unusual margins.

### TE-B8 — Retirement / walkover
Operator terms not supplied.
`UNKNOWN_DEFINITION / NO VALUE DETERMINABLE`.

## J. Reference base-rate anchors

No calibrated probability is issued.

### Marozsan +2.5
**Reference band: MEDIUM-HIGH**
- Positive cushion.
- Captures every Marozsan outright win.
- Also captures close Zheng wins.
- Event adjustment: hold/maintain due higher ranking/ATP baseline and the narrow margin in the recent H2H.
- Frozen band: **MEDIUM-HIGH**.

### Zheng -2.5
**Reference band: MEDIUM**
- Requires Zheng to win net games by 3+.
- Event adjustment: up modestly from current recency and direct H2H, but capped because the previous matchup cleared this exact threshold by only 0.5 game and Bo5 increases close-extension paths.
- Frozen band: **MEDIUM**.

### Over 38.5
**Reference band: MEDIUM**
- Four sets often place the total near or above the line.
- Five sets strongly favour Over.
- Event adjustment: up modestly because four sets are central and the matchup has demonstrated set swings/tiebreak exposure.
- Frozen band: **MEDIUM-HIGH / borderline**.

### Under 38.5
**Reference band: MEDIUM**
- Every ordinary straight-set state supports it.
- Efficient four-set matches can also stay Under.
- Event adjustment: down modestly because the current tree gives meaningful 4/5-set extension.
- Frozen band: **MEDIUM-LOW**.

## K. External market/model sanity check — non-controlling

Current public market snapshots generally made **Michael Zheng the match favourite**, but there was disagreement on the -2.5 handicap and on the 38.5 total:
- several books had Marozsan +2.5 slightly shorter than Zheng -2.5;
- at least one source reversed that ordering;
- totals ranged from near-even to a mild Over preference.
A current Tennis.com projection also favoured Zheng.

These are external observations only:
- not the user's operator;
- not internal model outputs;
- not calibrated by this framework;
- not evidence of value.

The disagreement supports keeping all evidence grades below high confidence.

## L. Strongest kill paths

### Kill path against Marozsan +2.5
Zheng's return pressure converts the recent H2H advantage into a cleaner best-of-five separation, e.g. **6-4, 6-3, 4-6, 6-2**.

### Kill path against Over 38.5
Either player's ordinary straight-set control, or an efficient four-set winner with lopsided sets, keeps the total below the line.

### Kill path against Zheng -2.5
A close Zheng 3-1 or 3-2 win leaves his net game margin at only +1/+2, exactly the central coherence branch.

### Kill path against Under 38.5
Four competitive sets with tiebreaks or any normal five-set extension crosses the line.

## M. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Retirement terms:** UNKNOWN_DEFINITION

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-242-C01 — Fabian Marozsan +2.5 games** | **LEAN** | MEDIUM-LOW | Broad positive cushion, stronger established ATP baseline, and a close Zheng-win branch can still cover Marozsan. The recent H2H landed only 0.5 game beyond this exact threshold. |
| **2** | **P-242-C03 — Over 38.5 games** | **LEAN** | MEDIUM-LOW | Four sets are the central set-count branch and five sets remain material; 38.5 can be crossed by an ordinary close 3-1 scoreline. |
| **3** | **P-242-C02 — Michael Zheng -2.5 games** | **FORCED RANK / LEAN-ADJACENT** | MEDIUM-LOW | Zheng is the winner lean and owns the recent H2H, but -2.5 requires his winner edge to become game separation rather than a close extended win. |
| **4** | **P-242-C04 — Under 38.5 games** | **FORCED RANK / AVOID relative to Over** | LOW-MEDIUM | Strong in straight sets, but less aligned with the central four-set/competitive-match tree. |

### Total-direction control
Recommend **Over 38.5 only** among the opposing total directions.

## N. Potential winner

**Michael Zheng — LEAN**

This is a descriptive match-winner call, not a fifth independent contract.

Reasons:
1. Zheng won the direct hard-court meeting only weeks ago.
2. His current hard L5/L10 direction is stronger after appropriate level shrinkage.
3. He followed the Marozsan win by beating Ugo Humbert before losing to Lorenzo Musetti.
4. His 2026 Australian Open/Wimbledon results demonstrate best-of-five competence.
5. Current public market/match-preview sources also favour Zheng, used only as corroboration.

Counter-evidence:
- Marozsan is ranked materially higher.
- Marozsan owns the stronger established ATP hold profile and much larger tour sample.
- Marozsan rebounded immediately at Winston-Salem with two wins and a QF run.
- Zheng's broader hard record includes qualifying/lower-level opposition.
- The only H2H was extremely close at the exact current handicap boundary.

Winner status therefore remains LEAN rather than stronger.

## O. Frozen user-facing forecast

### Event and state
Fabian Marozsan vs Michael Zheng is a **2026 US Open men's singles first-round match on Court 11, outdoor hard, best-of-five**. Heavy rain disrupted the outside-court schedule. At the final frozen refresh, current match pages still showed **Upcoming / Not started**, with no verified live score. The inconsistent premature `live` flag on one bracket feed was rejected because it carried no score and contradicted its own listed timing.

### Best four supplied picks
1. **Fabian Marozsan +2.5 games — LEAN**
2. **Over 38.5 total games — LEAN**
3. **Michael Zheng -2.5 games — lower-confidence directional side**
4. **Under 38.5 total games — weaker total direction**

### Why Marozsan +2.5 is #1
Zheng is my likely match winner, but that does not make his -2.5 automatically stronger.

Their Cincinnati meeting only about 2.5 weeks ago ended **3-6, 6-1, 7-6 to Zheng**. Zheng finished exactly three net games ahead, meaning today's Zheng -2.5 would have won by only half a game. The match showed genuine two-sided control: Marozsan won the first set, Zheng dominated the second, and the third reached a tiebreak.

Marozsan also remains the higher-ranked and more established ATP player. His 2026 hard results have been inconsistent, but after losing to Zheng he reached the Winston-Salem quarterfinal with wins over Kecmanovic and Damm.

In a best-of-five match, a close Zheng 3-1 or 3-2 win can easily leave Zheng only one or two net games ahead. That is the main reason Marozsan +2.5 is more robust than Zheng -2.5 despite the Zheng winner lean.

### Why Over 38.5 is #2
My central set-count state is **four sets**, with five sets a meaningful secondary branch.

At 38.5, an ordinary competitive four-set match can already clear the line. For example:
**Zheng 7-6, 4-6, 7-6, 6-4 = 46 games.**
That scoreline is also fully coherent with Marozsan +2.5, because Zheng wins the match by only two net games.

The Under is strongest if one player controls in straight sets or the fourth set comes with enough lopsided games to finish around 34-38. That is a real branch, so the Over remains a lean rather than a strong call.

### Why Zheng -2.5 is #3
Zheng has the current winner edge:
- he won the recent direct hard-court meeting;
- his short-window hard results are stronger;
- he beat Ugo Humbert immediately after the Marozsan victory;
- he has already shown best-of-five resilience at the Australian Open and Wimbledon.

But his broader record contains qualifying/lower-level matches, while Marozsan has the stronger ATP-level baseline. More importantly, -2.5 needs Zheng not merely to win but to create at least a three-game net margin.

### Likely winner
**Michael Zheng — LEAN.**

This is not a fifth independent selection.

### Weather/delay
Court 11 is outdoors. Heavy rain produced substantial delays at the US Open, with humid conditions and continuing rain risk around the evening window. I use this mainly as a state/timing uncertainty rather than assigning an automatic player or total direction.

### Settlement/publication boundary
The user's operator and retirement rules were not supplied. Tennis game handicaps and totals can grade differently after retirement, so the exact contract definition remains `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking recommendation is published.

## P. Append confirmation

- Complete frozen P-242 forecast appended before delivery: **YES**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-243

The connected Drive canonical top snapshot remains stale at `Next canonical ID: P-239` because Google Drive is read-only. The local append-only continuation already contains issued P-239 through P-242. Reusing one of those IDs for a distinct event would violate the one-event/one-ID invariant. This event is therefore appended locally as **P-243**, with the Drive/local integration gap explicitly preserved for later canonical reconciliation. No Drive file is modified.

---

# P-243 — Magda Linette vs Francesca Jones — 2026 US Open Women's Singles R1

## A. Frozen identity and state

- **Append sequence:** P-243
- **Request date:** 2026-09-02 Australia/Melbourne
- **Final state refresh:** 2026-09-02 10:21 AEST
- **Information cutoff:** 2026-09-02 10:21 AEST
- **Sport:** Tennis
- **Competition:** 2026 US Open
- **Draw:** Women's Singles
- **Round:** First round / Round of 128
- **Players:** Magda Linette (POL) vs Francesca Jones (GBR, qualifier)
- **Court:** Court 6
- **Surface:** Outdoor hard
- **Format:** Best-of-three sets
- **Current rankings:** Linette #78 on current rankings source / #82 on the current Tennis.com match page; Jones #104
- **Ranking discrepancy:** source-timing difference preserved; no decision hinges on the 78/82 distinction.
- **H2H:** 0-0; no prior verified meeting.
- **GAME-STATE:** **DELAYED / NOT STARTED — rain-disrupted outside-court schedule**
- **State evidence:** current Tennis.com match page showed `Upcoming`; Reuters reported nearly four hours of outdoor-court rain disruption during the session.
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-TENNIS
- **Tennis numerical status:** NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL APPROVED OR FIT
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective performed:** NO

## B. Contract freeze

### User-supplied slate
1. Francesca Jones +0.5 games
2. Magda Linette -0.5 games
3. Total games Over 21.5
4. Total games Under 21.5

- **Operator:** NOT SUPPLIED
- **Odds:** NOT SUPPLIED
- **Retirement/walkover rule:** UNKNOWN_DEFINITION
- **Completed-match requirement:** UNKNOWN_DEFINITION
- **Void/partial-match treatment:** UNKNOWN_DEFINITION

### Geometry
- Jones +0.5 and Linette -0.5 are exact game-margin complements under ordinary full-match grading.
- Over 21.5 and Under 21.5 are exact total-game complements.
- A match winner and a ±0.5 game handicap are **not mathematically identical**: a player can win the match while finishing behind in net games in an uneven three-set scoreline.
- Under normal completed-match rules, exactly two of the four supplied rows win.
- Retirement rules can alter settlement, so sportsbook settlement remains operator-dependent.

| ID | Contract | Geometry | Dependence |
|---|---|---|---|
| P-243-C01 | Jones +0.5 games | Complement of C02 | P243-GAME-MARGIN |
| P-243-C02 | Linette -0.5 games | Complement of C01 | P243-GAME-MARGIN |
| P-243-C03 | Over 21.5 games | Complement of C04 | P243-TOTAL |
| P-243-C04 | Under 21.5 games | Complement of C03 | P243-TOTAL |

## C. Participant / current-status gate

### Magda Linette
- Right-handed, 34.
- Current ranking source: #78; Tennis.com match page: #82.
- Career high: #19.
- 2026 broad hard-court record from current Tennis Explorer snapshot: approximately **13-12**.
- Stronger historical tour-level baseline and much greater WTA/Grand Slam experience than Jones.
- Immediate hard-court sequence:
  - L Elena-Gabriela Ruse, Cincinnati: 0-6, 3-6
  - L Iva Jovic, Toronto: 3-6, 5-7
  - W Carol Zhao, Toronto: 4-6, 6-1, 6-4
  - L Leylah Fernandez, Washington: 1-6, 4-6
  - L Mai Hontama, Athens: 4-6, 5-7
- Exact-surface L5: **1-4**.
- Most concerning current service signal: against Ruse, Linette made only 43% first serves, won 59% of first-serve points and 28% of second-serve points, double-faulted six times, and held only 2 of 8 service games.
- That one match is not treated as a new permanent serve coefficient, but the broader five-match window does show weak recent hard-court results.

### Francesca Jones
- Right-handed, 25.
- Current ranking: #104.
- 2026 WTA official overall record: 24-18.
- Broad 2026 hard record is small and definition-sensitive: current databases range around **6-5**, with older/stale snapshots showing fewer matches before US Open qualifying.
- Qualified through three US Open hard-court matches:
  - def. Nuria Brancaccio 6-3, 6-4
  - def. Mona Barthel 7-6, 1-6, 6-2
  - def. Joanna Garland 6-4, 6-1
- Final qualifier vs Garland:
  - 68% first serve in
  - 92% first-serve points won
  - 67-80% second-serve points won depending source denominator rendering
  - faced no break points
  - broke 4 times
- Qualifying R1 vs Brancaccio:
  - 66% first serve in
  - 71% first-serve points won
  - 70% second-serve points won
  - 3/3 break points converted
- Qualifying R2 vs Barthel was much less clean:
  - six double faults
  - 57% service games won
  - match required three sets
- This shows a high-current-form branch but not a uniformly dominant serve regime.

### Fitness / retirement
- No current withdrawal or current injury report was found at cutoff.
- Jones has a documented history of retirements, including 2026 Australian Open/Auckland/Miami periods on a specialist history page.
- Historical retirement propensity is **not** used directionally without a current medical signal.
- It makes the unknown operator retirement rule particularly material.

## D. H2H continuity audit

- Verified H2H: **0-0**.
- No meeting exists to use as a matchup prior.
- H2H window count: **0 — NO COMPARABLE CASE**.
- No invented or proxy H2H is used.

## E. Surface-recency block

### Linette — exact hard-court L5
| Match | Result |
|---|---|
| vs Ruse | L 0-6, 3-6 |
| vs Jovic | L 3-6, 5-7 |
| vs Zhao | W 4-6, 6-1, 6-4 |
| vs Fernandez | L 1-6, 4-6 |
| vs Hontama | L 4-6, 5-7 |

- **L5:** 1-4
- **L10/L15/L20:** current source coverage is fragmented across WTA/Tennis.com/TennisExplorer snapshots and not stable enough to produce one definition-consistent reconstructed window without mixing timestamped datasets. Record as `PARTIAL_SOURCE_COVERAGE`, not backfilled.
- **2026 hard-season anchor:** ~13-12 on the freshest broad snapshot.
- **Trend verdict:** recent L5 is clearly negative, but the full L5/L10/L15/L20 monotonicity test cannot be completed from one stable current provider; therefore **NO FORMAL TREND PROMOTION**.

### Jones — exact hard-court current sample
Recent current-source hard sequence includes:
- W Garland
- W Barthel
- W Brancaccio
- earlier 2026 hard results include losses/wins at Miami, Indian Wells, Austin, Australian Open and Auckland.

- **Current US Open qualifying L3:** 3-0.
- **Current bookmaker-style L5 snapshot:** 4-1.
- **2026 hard anchor:** around 6-5 in current broad database.
- **L10/L15/L20:** true 2026 hard sample is too small for all requested windows; record true-count/missingness rather than inventing 15/20-match windows.
- **Trend verdict:** the three qualifying wins are positive current regime evidence, but not enough to call a validated monotone L5-L20 trend.

### Level adjustment
Jones's strongest recent evidence comes from US Open qualifying opponents ranked materially below Linette:
- Garland ~#201;
- Barthel ~#205;
- Brancaccio lower-tour/qualifying level.
That same-site adaptation is valuable, but the opponent-strength jump into an experienced main-draw WTA player requires shrinkage.

## F. Environment / schedule gate

- **Venue:** USTA Billie Jean King National Tennis Center, Flushing, New York
- **Court:** Court 6
- **Venue class:** OUTDOOR
- Reuters reported heavy rain delaying outside-court play for nearly four hours during the session.
- Current match page remained Upcoming at the final refresh.
- Conditions around the disrupted evening window were humid with continuing rain risk.

Mechanism:
- Primary impact is delay, uncertainty in start time and stop-start preparation.
- No automatic Over/Under direction is assigned from rain/humidity.
- Jones has same-site qualifying acclimatisation; Linette has greater tour experience.
- No one-sided weather adjustment is strong enough to move a contract band.

## G. Serve-return / matchup reconciliation

### Linette established prior
Linette has:
- materially more top-level hard-court experience;
- a long WTA baseline and career-high #19;
- stronger proof against elite opponents over multiple seasons;
- a 2026 hard season close to .500 despite the recent downturn.

### Jones current regime
Jones has:
- three recent wins on the exact US Open hard courts;
- strong final-qualifier serving and return pressure;
- a positive confidence/adaptation branch;
- but a small hard-court sample and lower-opponent-quality recent set.

### Matchup inference
No H2H exists, so the comparison is:
- **established level/experience advantage:** Linette
- **same-site current-form/acclimatisation advantage:** Jones
- **recent hard-result advantage:** Jones
- **sample size/opponent-quality advantage:** Linette

The evidence does not support a large separation state for either player.

## H. Best-of-three set-count mixture

These are qualitative relative weights, **not probabilities**.

| Endpoint | Relative weight | Interpretation |
|---|---:|---|
| 2 sets | 3/5 | Meaningful: both have straight-set control branches |
| **3 sets** | **4/5** | Central: near-even matchup, conflicting regime signals |

The three-set state is fixed as central before locating the 21.5 line.

## I. Mandatory score-tree branches

### TE-B1 — Linette ordinary straight-set control
Representative: **6-4, 6-3**
- Total: 19
- Linette net margin: +5
- Wins: Linette -0.5, Under 21.5

### TE-B2 — Linette close straight sets
Representative: **7-5, 6-4**
- Total: 22
- Wins: Linette -0.5, **Over 21.5**

### TE-B3 — Linette three-set win
**Central coherence scoreline:** **6-4, 4-6, 6-3**
- Total: 29
- Linette net margin: +3
- Wins: Linette -0.5, Over 21.5

A lopsided split-set Linette win such as 1-6, 6-4, 6-4 would make Linette win the match but **lose** the -0.5 game handicap. That path is possible and is why match winner ≠ exact game handicap.

### TE-B4 — Jones ordinary straight-set control
Representative: **6-4, 6-3**
- Total: 19
- Wins: Jones +0.5, Under 21.5

### TE-B5 — Jones close straight sets
Representative: **7-5, 6-4**
- Total: 22
- Wins: Jones +0.5, Over 21.5

### TE-B6 — Jones three-set win
Representative: **4-6, 6-3, 6-4**
- Total: 29
- Jones net margin: +3
- Wins: Jones +0.5, Over 21.5

### TE-B8 — retirement/walkover
- Operator terms unknown.
- `UNKNOWN_DEFINITION / NO VALUE DETERMINABLE`.

## J. Reference base-rate anchors

No calibrated probabilities are generated.

### Over 21.5
**Reference band: MEDIUM**
- A three-set match usually clears comfortably.
- Close straight sets can also clear: 7-5, 6-4 = 22.
- Event adjustment: up one band because three sets are central and the match is close.
- **Frozen band: MEDIUM-HIGH**.

### Under 21.5
**Reference band: MEDIUM**
- Ordinary straight-set outcomes like 6-3, 6-4 or 6-4, 6-4 settle Under.
- Event adjustment: down one band because the score tree gives substantial three-set/close-two-set mass.
- **Frozen band: MEDIUM-LOW**.

### Linette -0.5 games
**Reference band: MEDIUM**
- Near winner-like contract but requires positive net game margin.
- Event adjustment: small upward/hold from established level/ranking/experience, partially offset by current hard-form weakness.
- **Frozen band: MEDIUM**.

### Jones +0.5 games
**Reference band: MEDIUM**
- Captures every Jones positive net-game-margin state, including ordinary match wins.
- Event adjustment: up from same-site qualifying form, then shrink for opponent-quality jump.
- **Frozen band: MEDIUM, narrowly below Linette -0.5**.

## K. External market sanity check — non-controlling

Public prices were close and **conflicted on the handicap**:
- Oddschecker broadly had Linette a tiny moneyline favourite.
- BetVictor had Linette -0.5 slightly shorter than Jones +0.5.
- BetRaven instead had Jones +0.5 shorter than Linette -0.5.
- Bwin was essentially even.
- Multiple public books priced Over 21.5 shorter than Under 21.5.

Interpretation:
- External market agrees that this is close.
- External market provides more consistent corroboration for Over 21.5 than for either side.
- These are **not** the user's operator and are not used for expected value or edge.

One external model on Tennis.com projected Linette 52% / Jones 48%. This is cited only as an external estimate, not an internal probability.

## L. Strongest kill paths

### Against Over 21.5
Either player wins efficiently in straight sets:
- 6-3, 6-4 = 19
- 6-4, 6-4 = 20
A three-set match can also stay Under if the sets are extremely lopsided, e.g. 6-1, 1-6, 6-1 = 21.

### Against Linette -0.5
- Jones converts her qualifier form to main-draw level and wins outright.
- Linette wins in an uneven three-set scoreline but finishes with negative net games.
- Linette's Cincinnati serve instability persists.

### Against Jones +0.5
- Linette's experience/quality edge converts to a routine positive game margin.
- Jones's qualifying serving rates regress sharply against a stronger returner.

### Against Under 21.5
- Any normal three-set match.
- Close two-set match such as 7-5, 6-4 or 7-6, 6-4.

## M. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Retirement terms:** UNKNOWN_DEFINITION

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-243-C03 — Over 21.5 games** | **LEAN** | MEDIUM-LOW | The evidence points to a close contest; three sets are central and even close straight sets can clear 21.5. |
| **2** | **P-243-C02 — Linette -0.5 games** | **LEAN** | LOW-MEDIUM | Slight established-level/experience edge and external consensus lean, but recent hard form is weak enough to cap confidence. |
| **3** | **P-243-C01 — Jones +0.5 games** | **FORCED RANK / LEAN-ADJACENT** | LOW-MEDIUM | Exact-court qualifying form is excellent, but the opponent-quality jump and small hard sample prevent ranking it above Linette's established prior. |
| **4** | **P-243-C04 — Under 21.5 games** | **FORCED RANK / AVOID relative to Over** | LOW-MEDIUM | Strong in efficient straight sets but less aligned with the central three-set/close-match tree. |

### Total-direction control
Recommend **Over 21.5 only** among the opposing total directions.

## N. Potential winner

**Magda Linette — LEAN**

This is a separate descriptive match-winner call, not a fifth independent contract.

Why:
1. Linette's established WTA/Grand Slam baseline is materially stronger.
2. Current ranking still favours Linette.
3. Jones's three qualifying wins are strong same-site evidence but came against substantially lower-ranked opponents.
4. External public markets and the Tennis.com projection were slightly Linette-leaning overall.

Why not stronger:
- Linette is 1-4 in her exact-surface recent L5.
- Her Cincinnati serve performance was poor.
- Jones is fully acclimatised to the US Open courts and arrives 3-0 in qualifying.
- No H2H exists to resolve the stylistic matchup.
- Several market sources were close to 50/50 or even slightly Jones-side on the handicap.

## O. Frozen user-facing forecast

### Event and current state
Magda Linette vs Francesca Jones is a **2026 US Open Women's Singles Round 1 match on Court 6, outdoor hard, best-of-three**. At the final refresh the match remained listed as **Upcoming** after heavy rain disrupted the outside courts, so this is frozen as **DELAYED / NOT STARTED**, not a stale pregame state.

### Best four supplied picks
1. **Over 21.5 total games — LEAN**
2. **Magda Linette -0.5 games — LEAN**
3. **Francesca Jones +0.5 games — lower-confidence side**
4. **Under 21.5 games — weaker total direction**

### Why Over 21.5 is #1
The strongest evidence is that this matchup is close.

Jones has already won three US Open qualifying matches on the same courts:
- 6-3, 6-4 vs Brancaccio
- 7-6, 1-6, 6-2 vs Barthel
- 6-4, 6-1 vs Garland

Her final qualifier was especially clean: she faced no break points and dominated first-serve points.

Linette, however, is a much more established WTA player and remains the higher-ranked opponent. That makes a routine Jones straight-set control state less convincing than it would be against the qualifying field.

My central score tree is therefore three sets. A representative Linette win of **6-4, 4-6, 6-3** reaches 29 games. A representative Jones win of **4-6, 6-3, 6-4** also reaches 29. Even a close two-set score like **7-5, 6-4** reaches 22 and clears the line.

The Under's main path is an efficient straight-set result such as 6-3, 6-4 or 6-4, 6-4. That remains meaningful, but it is not the central branch.

### Why Linette -0.5 is #2
Linette has the stronger established tour baseline, higher ranking and much deeper Grand Slam/WTA experience. Jones's current qualifying run matters, but her three opponents were well below Linette's level, so those raw serving and return numbers must be shrunk.

The main concern is Linette's current hard form: she has lost four of her last five hard matches. Her latest Cincinnati loss to Ruse was particularly poor on serve.

That keeps Linette -0.5 at only a lean.

### Why Jones +0.5 remains live
Jones is in better immediate rhythm. She has:
- three recent wins on these exact courts;
- two straight-set qualifying victories;
- a strong final-qualifier service performance;
- no current withdrawal/injury signal.

If Linette's recent serve problems persist, Jones can win outright. That is why the two side contracts are close in rank.

### Likely winner
**Magda Linette — LEAN.**

This is not a fifth independent pick.

### Weather/delay
Heavy rain delayed outdoor US Open play for nearly four hours. Court 6 is outdoors, so the main verified effect is schedule/start uncertainty. I do not apply an automatic Over or Under adjustment from the weather.

### Settlement/publication boundary
The user's operator and retirement rules were not supplied. Jones also has a historical retirement record, which makes those terms particularly important. Exact handicap/total settlement therefore remains `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking recommendation is published.

## P. Append confirmation

- Complete frozen P-243 forecast appended before delivery: **YES**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-244

The connected Drive canonical top snapshot remains at `Next canonical ID: P-239` because Google Drive is read-only. The local append-only continuation already contains issued P-239 through P-243. Reusing one of those IDs for a distinct event would violate the one-event/one-ID invariant. This event is therefore appended locally as **P-244**, with the Drive/local integration gap explicitly preserved for later canonical reconciliation. No Drive file is modified.

---

# P-244 — Baltimore Orioles @ Colorado Rockies — MLB — 2026-09-01 MDT / 2026-09-02 AEST

## A. Frozen identity and state

- **Append sequence:** P-244
- **Request date:** 2026-09-02 Australia/Melbourne
- **Final state refresh:** 2026-09-02 10:27:09 AEST
- **Information cutoff:** 2026-09-02 10:27:09 AEST
- **Scheduled first pitch:** 2026-09-01 18:40 MDT / 2026-09-02 10:40 AEST
- **Cutoff invariant:** PASS — approximately 13 minutes before scheduled first pitch.
- **GAME-STATE:** PREGAME
- **Sport:** Baseball
- **Competition:** MLB regular season
- **Official fixture:** Baltimore Orioles @ Colorado Rockies
- **Venue:** Coors Field, Denver, Colorado
- **Home/away:** Baltimore away; Colorado home
- **Official starter status:** MLB/Rockies probable-pitcher pages list Kyle Bradish vs Gabriel Hughes; subject to change.
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-BASEBALL
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective performed:** NO

## B. Starter identity handshake

| Role | Team | Pitcher | Status | Frozen line |
|---|---|---|---|---|
| Starter | BAL | Kyle Bradish, RHP | PROBABLE_OFFICIAL | 7-12, 4.03 ERA, 133 K, 1.41 WHIP |
| Starter | COL | Gabriel Hughes, RHP | PROBABLE_OFFICIAL | 0-6, 6.61 ERA, 38 K, 1.45 WHIP |

### Kyle Bradish
- 2026 season: 4.03 ERA over 143 IP.
- Last five starts: **5.40 ERA**, 25 IP, 31 H, 15 ER, 10 BB, 19 K.
- Latest start at St. Louis: 4.1 IP, 9 H, 7 ER.
- Road split in the freshest current snapshot: approximately **4.50 ERA**; earlier cached snapshots were lower, so the current snapshot controls.
- Career vs Colorado is limited; StatMuse listed one prior successful appearance/start context around a 3.00 ERA.
- Bradish therefore has the stronger starter prior than Hughes, but his current form is not strong enough to make Colorado's run contribution negligible.

### Gabriel Hughes
- 2026 season: 6.61 ERA in 47.2 IP.
- Last five starts: **10.03 ERA**, 23.1 IP, 28 H, 26 ER, 12 BB, 17 K.
- Recent starts: 5 ER vs TB, 7 at AZ, 7 at SF, 3 vs CLE, 4 at WSH.
- Home/Coors sample is materially better than the raw recent road-heavy line:
  - 4 starts / 5 home appearances;
  - about **4.18 ERA** over 23.2 home innings.
- The home split is small and does not erase the current instability, but it is a real reason not to treat Baltimore -1.5 as automatic.

## C. Contract freeze and geometry

### Supplied slate
1. Orioles -1.5
2. Rockies +1.5
3. Full-game Over 11.0 runs
4. Full-game Under 11.0 runs

- **Operator:** NOT SUPPLIED
- **Odds:** NOT SUPPLIED
- **Listed-pitcher/action rules:** UNKNOWN_DEFINITION
- **Shortened/suspended-game rule:** UNKNOWN_DEFINITION
- **Extra-inning settlement rule:** UNKNOWN_DEFINITION
- **Sporting target assumption for research:** official MLB full-game final score including extra innings if played; this does not define unnamed-book settlement.

### Geometry
- BAL -1.5 and COL +1.5 are exact complements under ordinary completed-game action.
- Over 11.0 and Under 11.0 are **not exact win/loss complements because 11 is an integer**:
  - Over wins at 12+;
  - Under wins at 10 or fewer;
  - exactly 11 is a push under ordinary total-11 terms.
- The total's push mass makes forced “one of these must win” language invalid.

| ID | Contract | Win / Push / Loss geometry | Dependence |
|---|---|---|---|
| P-244-C01 | Orioles -1.5 | BAL margin 2+ / no push / otherwise loss | P244-MARGIN |
| P-244-C02 | Rockies +1.5 | COL win or BAL win by 1 / no push / otherwise loss | P244-MARGIN |
| P-244-C03 | Over 11.0 | 12+ / 11 / 0-10 | P244-TOTAL |
| P-244-C04 | Under 11.0 | 0-10 / 11 / 12+ | P244-TOTAL |

## D. Lineup and availability gate

- The current MLB starting-lineup page still displayed **TBD** for both clubs at the final cutoff.
- Baseball Savant also showed Baltimore as **Awaiting Starting Lineup**.
- Therefore no projected batting order is promoted to `CONFIRMED_OFFICIAL`.
- Secondary projections centered Baltimore around Jackson Holliday, Pete Alonso, Gunnar Henderson, Christian Encarnacion-Strand/Coby Mayo, Dylan Beavers, Samuel Basallo, Colton Cowser and Leody Taveras.
- Secondary Colorado projections centered around Jake McCarthy, Cole Carrigg/Connor Norby, Hunter Goodman, T.J. Rumfield, Willi Castro and Mickey Moniak.
- Baltimore's September additions Luis Robert Jr. and Heston Kjerstad were reported not to be in the starting lineup.
- Current injury reporting showed Baltimore still without several regular contributors, including Tyler O'Neill/Ryan Mountcastle/Jordan Westburg in the current injury feed.
- Because official orders were still unavailable, lineup/platoon-specific conclusions are capped below strong evidence.

## E. Environment gate

- **Venue class:** OUTDOOR
- **Park:** Coors Field
- **Elevation:** approximately one mile; 2025 MLB park factor listed runs at 128 where 100 = league average.
- **Field orientation:** home plate-to-center field is approximately due north (~4° bearing).
- **NWS match-window forecast near downtown Denver:**
  - ~30°C at 18:00 MDT, ~28°C at 19:00;
  - dew point ~9°C;
  - wind ~7 mph, E shifting SE;
  - partly cloudy/dry evening in the latest NWS point forecast.
- **Wind-vector interpretation:** with center field nearly due north, the E/SE wind is mostly cross-field with only a modest outfield component; it is not a strong straight-out wind.
- **Weather conclusion:** warm, dry, light-wind conditions preserve ordinary Coors carry but do not add a major wind-driven Over adjustment.
- The prior night's 2-1 game had a 1h38m rain delay; that weather state is not imported into tonight because the current NWS forecast is materially different.

## F. Recent-form windows

### Baltimore scoring
| Window | Runs/game |
|---|---:|
| L5 | 4.8 (24 runs) |
| L10 | ~5.3 |
| L15 | 5.13 |
| L20 | 5.00 |

- Season: 4.55 R/G.
- Road: 4.73 R/G.
- Current result form: four straight wins and eight wins in the last ten after the 2-1 opener.
- **Trend verdict:** NO TREND — NOISE. L5/L10/L15/L20 are not monotone; the stable current centre is roughly five runs/game.

### Colorado scoring
| Window | Runs/game |
|---|---:|
| L5 | 4.2 (21 runs, heavily influenced by one 13-run game) |
| L10 | ~3.3-3.5 |
| L15 | 4.13 |
| L20 | 3.85 |

- Home season: approximately **4.97-5.03 R/G** depending snapshot date.
- Current result form: ten straight home losses entering this game.
- **Trend verdict:** NO TREND — NOISE. Short windows are non-monotone and the L5 mean is distorted by a 13-run outlier.
- Important reconciliation: Colorado's home scoring prior is much stronger than its current all-location L10. Both states are retained rather than allowing either one to erase the other.

## G. Head-to-head continuity

### H2H windows
- Current 2026 continuity count before P-244: **1 game** — BAL won 2-1 on Aug. 31.
- Recent L5/L10 historical series exist, but many meetings come from 2019-2025 and materially different rosters/pitchers.
- Current StatMuse L10: Baltimore 6-4 vs Colorado.
- L20 historical record around 11-9 Baltimore in the freshest retrieval.

### Continuity verdict
**LOW for old H2H; HIGH only for the immediately prior 2026 game's team/venue context.**

Yesterday's 2-1 result is not treated as a direct total prior because:
- different starters;
- different bullpen entry timing;
- a long rain delay;
- today's Hughes/Bradish matchup is materially different.

## H. Bullpen exposure and workload

### Baltimore
- Current bullpen form: approximately **1.77 ERA over the last 15 days**.
- Yesterday:
  - Grant Wolfram threw two scoreless innings;
  - Rico Garcia and Andrew Kittredge also worked;
  - Kittredge earned the save.
- The recent pen performance is a meaningful late-game suppression mechanism, but those used relievers are not treated as fully fresh by default.

### Colorado
- Current bullpen form: approximately **3.59 ERA over the last 15 days**.
- Season/home environment remains more difficult; Colorado pitching owns approximately a **5.91 home ERA** overall.
- Yesterday, after Tanner Gordon's five innings, Colorado used four relievers including Manfredi, Frasso, Bernardino and Romano, mostly on modest pitch counts.
- Hughes' recent inability to work deep raises expected bullpen exposure again.

### Bullpen conclusion
Late-game structure favors Baltimore in quality, while Colorado's bullpen is not maximally depleted from yesterday. Hughes' expected starter-length/quality risk remains the larger side-market driver.

## I. Target distribution / score-family map

The 11.0 total is deliberately high. The qualitative target corridor is wide because the game combines:
- Coors;
- a poor current Hughes state;
- a hot Baltimore scoring profile;
- but a strong Baltimore bullpen and a slumping Colorado offense;
- plus Bradish's own recent instability.

### Representative score families

| Family | Score examples | Contracts helped |
|---|---|---|
| Low/close | BAL 5-4, COL 5-4 | COL +1.5, Under 11 |
| Low/separation | BAL 7-3, BAL 6-3 | BAL -1.5, Under 11 |
| Boundary | BAL 6-5, BAL 7-4 | COL +1.5 at 6-5 / BAL -1.5 at 7-4; total PUSH at 11 |
| High/close | BAL 7-6, COL 7-6 | COL +1.5, Over 11 |
| High/separation | BAL 8-4, BAL 9-4 | BAL -1.5, Over 11 |
| Colorado-control kill path | COL 6-4 / 7-5 | COL +1.5; Under or Over depending score |

### Component budget
- Baltimore central scoring component: approximately **5-7 runs**, with a material 8+ tail because Hughes has a 10.03 last-five ERA and Colorado's home pitching environment is poor.
- Colorado central scoring component: approximately **3-5 runs**, with a higher Coors/home tail because Bradish has a 5.40 last-five ERA and a recent 7-run start.
- This places **11 inside the ordinary corridor rather than clearly outside it**.
- Because unweighted ordinary branches cross both sides and also place meaningful mass exactly at 11, total evidence is capped.

## J. Reference base-rate anchors

No calibrated probabilities are generated.

| Contract | Reference band | Event adjustment | Frozen qualitative band |
|---|---|---|---|
| Rockies +1.5 | HIGH-MEDIUM — positive 1.5-run cushion | Down modestly for Hughes/current team mismatch | **MEDIUM-HIGH** |
| Orioles -1.5 | MEDIUM-LOW — requires 2+ separation | Up for Hughes, Baltimore form and bullpen advantage | **MEDIUM** |
| Over 11.0 | MEDIUM-LOW at a very high integer total | Up for Coors/Hughes/Bradish recent volatility | **MEDIUM** |
| Under 11.0 | MEDIUM because the threshold is high and push protects exactly 11 | Down for Coors and Hughes upper tail | **MEDIUM-LOW** |

### External market sanity check — not user pricing
Same-day public prices generally:
- made Baltimore the outright favorite;
- priced Colorado +1.5 shorter than Baltimore -1.5;
- leaned modestly toward Over 11 versus Under 11.

This is used only as external coherence evidence. It is not the user's operator, not an internal probability and not a value claim.

## K. Strongest kill paths

### Against Rockies +1.5
Hughes' current command/contact problems combine with Baltimore power, producing an ordinary 7-3 / 8-4 / 9-4 separation game.

### Against Over 11
Bradish stabilizes against Colorado's currently weak offense and Baltimore's bullpen preserves a lead, yielding 7-3 / 6-3 / 6-4 type finals.

### Against Orioles -1.5
Colorado's home offense returns toward its ~5 R/G home baseline; Hughes repeats one of his better Coors starts; Baltimore wins only by one or loses outright.

### Against Under 11
Hughes exits early after traffic and Bradish's recent 5.40-ERA window also leaks runs, producing 7-6 / 8-4 / 8-5.

## L. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Official lineups:** NOT YET CONFIRMED at cutoff

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-244-C02 — Rockies +1.5** | **LEAN** | MEDIUM-LOW | The +1.5 cushion has the strongest structural base rate and wins on a Colorado victory or a one-run Orioles win. Hughes creates real separation risk, but his better small home split and Coors volatility keep close-game paths material. |
| **2** | **P-244-C03 — Over 11.0** | **SLIGHT LEAN** | LOW-MEDIUM | Hughes' 10.03 last-five ERA, Coors and Bradish's recent volatility create a genuine 12+ tail, but 11 sits inside the central corridor and retains push mass. |
| **3** | **P-244-C01 — Orioles -1.5** | **LEAN-ADJACENT / FORCED RANK** | MEDIUM-LOW | Baltimore is the likely winner and has the clearer quality mismatch, but -1.5 needs two-run separation rather than merely the better team winning. |
| **4** | **P-244-C04 — Under 11.0** | **FORCED RANK / weaker total direction** | LOW-MEDIUM | Strong Baltimore bullpen and Colorado's recent scoring slump support it, but Hughes/Coors/Bradish volatility make it the weaker side of the total. |

### Total-direction control
Recommend **Over 11.0 only**, and only as a **slight lean**. Under 11.0 is retained solely because the complete supplied audit slate must receive a unique rank.

### Strongest evidence class
The strongest evidence is in the **side market**, not the total:
- likely winner = Baltimore;
- safest supplied side contract by marginal likelihood = Colorado +1.5;
- Baltimore -1.5 has the higher-separation upside but the harder threshold.

## M. Potential winner

**Baltimore Orioles — LEAN**

This is a descriptive winner call, not a fifth independent contract.

Why:
1. Bradish owns the clearly stronger season/starter baseline than Hughes.
2. Hughes carries a 10.03 ERA over his last five starts.
3. Baltimore has won four straight and eight of ten.
4. Colorado has lost ten straight home games.
5. Baltimore's bullpen has a 1.77 ERA over the last 15 days versus Colorado's 3.59.
6. Baltimore's recent scoring centre is around five runs/game and Hughes creates a meaningful 6-8 run team-score branch.

Why not stronger:
- Coors widens both tails.
- Bradish himself has a 5.40 ERA over his last five and allowed seven runs last start.
- Colorado still scores around five runs/game at home across the season.
- Official batting orders were still TBD at the frozen cutoff.

## N. Frozen user-facing forecast

### Verified event
Baltimore Orioles @ Colorado Rockies, MLB, **Tuesday September 1, 2026 at 6:40 PM MDT at Coors Field**, which is **Wednesday September 2 at 10:40 AM AEST**.

MLB/Rockies currently list:
- **Kyle Bradish (BAL): 7-12, 4.03 ERA, 133 K**
- **Gabriel Hughes (COL): 0-6, 6.61 ERA, 38 K**

Both remain official probables / subject to change.

### Best four supplied picks
1. **Rockies +1.5 — LEAN**
2. **Over 11.0 runs — SLIGHT LEAN**
3. **Orioles -1.5 — lower-confidence separation side**
4. **Under 11.0 runs — weaker total direction**

### Why Rockies +1.5 is #1 even though Baltimore is the likely winner
These are different targets.

Baltimore is the better team and has the superior starter matchup, but Rockies +1.5 wins in every Colorado victory **and** whenever Baltimore wins by exactly one. Yesterday's 2-1 Orioles win is a concrete example of that close-game branch, although it is not treated as a direct repeat prior because the starters and weather were different.

Hughes is a serious problem for Colorado: his last five starts produced a 10.03 ERA. But his small home sample is less disastrous at about a 4.18 ERA, and Coors creates enough offensive variance that a 6-5 or 7-6 Orioles win remains an ordinary branch.

That makes Colorado +1.5 marginally more robust than asking Baltimore to win by two.

### Why Over 11.0 is #2
This is not a generic “Coors Over” call.

The case for 12+ runs is:
- Hughes: 10.03 ERA over the last five;
- Colorado home pitching: about 5.91 ERA;
- Baltimore: about 5.0-5.3 R/G across L10-L20;
- Bradish: 5.40 ERA over his last five, including seven earned runs in his latest start;
- warm, dry Coors conditions around first pitch.

But 11 is already a very high total. Colorado is only around 3.3-3.5 R/G in its latest L10, Baltimore's bullpen has a 1.77 ERA over the last 15 days, and a 7-3 or 6-4 Baltimore win remains very plausible.

Therefore Over 11 is only a **slight lean**. Exactly 11 should be a push under ordinary total-11 rules.

### Why Orioles -1.5 is #3
The separation case is real:
- Hughes is in a poor current regime;
- Baltimore has won eight of ten;
- Colorado has lost ten straight at home;
- Baltimore's bullpen is currently much stronger.

A 7-3 or 8-4 Baltimore win is fully ordinary.

But -1.5 gives away the one-run-win branch. That is why it ranks below Rockies +1.5 even though Baltimore remains my likely winner.

### Likely winner
**Baltimore Orioles — LEAN.**

This is not a fifth independent pick.

### Weather
Coors is outdoors. The NWS match-window forecast is warm and dry at roughly 28-30°C, with only about 6-7 mph E/SE wind. With center field almost due north, that is largely a cross-field wind rather than a major straight-out boost. Coors' altitude still preserves the naturally high offensive variance.

### Lineup / settlement boundary
Official MLB lineup pages still showed both orders as TBD at the frozen cutoff. Therefore lineup-specific conclusions are evidence-capped.

The user's sportsbook/operator and action rules were not supplied. Listed-pitcher requirements, shortened/suspended-game treatment and exact extra-inning settlement therefore remain `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking recommendation is published.

## O. Append confirmation

- Complete frozen P-244 forecast appended before delivery: **YES**
- Frozen cutoff before scheduled first pitch: **YES**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-245

The connected Drive canonical predecessor remains behind the local read-only continuation. The local append-only running log already contains issued P-239 through P-244. Reusing any earlier ID for this distinct event would violate the one-event/one-ID invariant. This event is therefore appended locally as **P-245**. No Google Drive file is modified.

---

# P-245 — Alexander Zverev vs Lorenzo Sonego — 2026 US Open Men's Singles R1

## A. Frozen identity and state

- **Append sequence:** P-245
- **Final state refresh:** 2026-09-02 10:36:37 AEST
- **Information cutoff:** 2026-09-02 10:36:37 AEST
- **Sport:** Tennis
- **Competition:** 2026 US Open
- **Draw / round:** Men's Singles, Round 1 / Round of 128
- **Players:** Alexander Zverev (GER) vs Lorenzo Sonego (ITA)
- **Court:** Arthur Ashe Stadium
- **Surface:** Hard
- **Venue class:** RETRACTABLE-ROOF STADIUM
- **Format:** Best-of-five sets
- **Current scheduled start from tournament bracket feed:** 2026-09-02 01:20 UTC / 2026-09-02 11:20 AEST
- **Cutoff invariant:** PASS — approximately 44 minutes before the current scheduled start.
- **Current state:** PREGAME / NOT STARTED
- **Current rankings:** Zverev #2; Sonego #89
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-TENNIS
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective:** NOT PERFORMED

Current Tennis.com and tournament-bracket sources both showed the match as upcoming/not started at the frozen cutoff.

## B. Contract freeze

### User-supplied audit slate
1. Lorenzo Sonego +6.5 games
2. Alexander Zverev -6.5 games
3. Total games Over 33.5
4. Total games Under 33.5

- **Operator:** NOT SUPPLIED
- **Odds:** NOT SUPPLIED
- **Retirement/walkover rule:** UNKNOWN_DEFINITION
- **Completed-match requirement:** UNKNOWN_DEFINITION
- **Void/partial-set treatment:** UNKNOWN_DEFINITION

### Geometry
- Sonego +6.5 and Zverev -6.5 are exact game-margin complements under ordinary full-match grading.
- Over 33.5 and Under 33.5 are exact total-game complements.
- Under ordinary completed-match terms, exactly two of the four supplied rows win.
- Retirement/withdrawal rules may alter settlement, so the unnamed operator's rule remains a hard unresolved field.

| ID | Contract | Geometry | Dependence |
|---|---|---|---|
| P-245-C01 | Sonego +6.5 games | complement of C02 | P245-MARGIN |
| P-245-C02 | Zverev -6.5 games | complement of C01 | P245-MARGIN |
| P-245-C03 | Over 33.5 games | complement of C04 | P245-TOTAL |
| P-245-C04 | Under 33.5 games | complement of C03 | P245-TOTAL |

## C. Player baseline and current regime

### Alexander Zverev
- Current ranking: #2.
- 2026 overall: approximately **46-13** in the freshest complete season dataset.
- 2026 hard: approximately **17-7**.
- 2026 Grand Slam record before this match: **18-2**.
- Career hard best-of-five record in the current broad database: approximately **67-24**.
- 2026 full-season serve/return summary from the current database:
  - hold ~88.0%;
  - break ~25.7%;
  - first serve in ~72.1%;
  - first-serve points won ~76.4%;
  - second-serve points won ~57.6%;
  - return points won ~37.3%;
  - tiebreaks 24-12.
- Recent hard results:
  - L Tommy Paul: 6-4, 6-7, 4-6
  - W Terence Atmane: 7-6, 7-6
  - W Cameron Norrie: 3-6, 6-3, 6-3
  - L Tallon Griekspoor: 7-6, 2-6, 4-6
- Interpretation: elite underlying hard/Grand-Slam profile, but the immediate North American hard swing has included several close-set/tiebreak and losing states rather than pure blowouts.

### Lorenzo Sonego
- Current ranking: #89.
- Current 2026 hard record: approximately **5-5** in the freshest exact-surface retrieval.
- Career hard Grand Slam / best-of-five record: approximately **14-16**.
- Career hard record vs Top 10: approximately **4-20**.
- Recent hard results:
  - L James Duckworth: 5-7, 3-6
  - W Adrian Mannarino: 6-1, 7-6
  - W Pierre-Hugues Herbert: 7-6, 4-6, 6-3
  - L Frances Tiafoe: 3-6, 4-6
  - W Juncheng Shang: 6-3, 6-3
  - L Tallon Griekspoor: 6-7, 5-7
- Interpretation: mixed current hard form with meaningful tiebreak/close-set exposure. Sonego's record against elite hard-court opposition is poor, but his serve can preserve narrow-set branches even when the match-winner probability is low.

## D. Recency window block

### Zverev — hard
| Window | Result | Status |
|---|---:|---|
| L5 | 2-3 | current direct hard results |
| L10 | 6-4 | current direct hard results |
| L15 | not recovered as one stable provider-defined window | PARTIAL_SOURCE_COVERAGE |
| L20 | not recovered as one stable provider-defined window | PARTIAL_SOURCE_COVERAGE |
| 2026 hard anchor | 17-7 | current season anchor |

**Trend verdict:** NO FORMAL TREND — L5/L10 are non-monotone and exact L15/L20 provider windows were not recoverable consistently enough to manufacture a trend.

### Sonego — hard
| Window | Result | Status |
|---|---:|---|
| L5 | 3-2 | current hard results |
| L10 | 5-5 | complete 2026 hard window in current database |
| L15 | TRUE COUNT 10 | MISSING — insufficient 2026 hard matches |
| L20 | TRUE COUNT 10 | MISSING — insufficient 2026 hard matches |

**Trend verdict:** NO TREND — NOISE.

## E. Head-to-head continuity audit

Current H2H: **Zverev 3-0**.

Verified meetings:
1. Beijing 2025, hard: Zverev 6-4, 6-3.
2. Halle 2025, grass: Zverev 3-6, 6-4, 7-6.
3. Halle 2024, grass: Zverev 6-4, 7-6.

### Game-margin implication
All three prior meetings would have made **Sonego +6.5 games a winner**:
- Beijing: Zverev +5 net games.
- Halle 2025: net games approximately level.
- Halle 2024: Zverev +3 net games.

### Continuity verdict
**MODERATE for matchup shape; LOW-MODERATE for exact-contract transfer.**

Why:
- the Beijing meeting is recent and on hard;
- both Halle matches support Sonego's ability to keep sets close;
- but all three were best-of-three, while this match is best-of-five;
- best-of-five creates more opportunity for Zverev's quality edge to accumulate into a large game margin.

The H2H therefore supports the Sonego cushion as descriptive matchup evidence, not as a fitted cover rate.

## F. Environment / roof state

- Arthur Ashe Stadium has a retractable roof.
- Rain heavily affected the outside courts during the session.
- Earlier Arthur Ashe matches were played under the closed roof.
- NWS around the night-session window:
  - ~24-25°C early evening, falling toward 23°C;
  - dew point ~22°C;
  - humidity ~87-93%;
  - E/NE wind about 5-6 mph;
  - rain/thunderstorm probability still material around the early night window.
- **Exact roof state for Zverev-Sonego was not independently confirmed by a same-match field-owner notice at cutoff.**

Mechanism:
- if closed, wind/rain are mostly neutralised as direct ball-flight inputs;
- humidity/roof conditions may affect court feel, but no robust directional contract adjustment is justified;
- weather therefore does not drive the ranking.

## G. Set-count mixture

These are qualitative relative weights, **not probabilities**.

| Endpoint | Relative weight | Interpretation |
|---|---:|---|
| **3 sets** | **5/5** | central: large underlying quality gap and Zverev's elite Bo5 record |
| 4 sets | 3/5 | meaningful: Sonego's serve/tiebreak profile can steal a set |
| 5 sets | 1/5 | tail: requires sustained Sonego resistance or a major Zverev dip |

The mixture is fixed before locating the 33.5 total.

## H. Two-sided score-tree branches

### Zverev ordinary straight-set control
Representative: **6-3, 6-4, 6-3**
- Total games: 28.
- Net margin: Zverev +8.
- Wins: Zverev -6.5, Under 33.5.

### Zverev close straight-set control
Representative: **7-6, 6-4, 6-4**
- Total games: 33.
- Net margin: Zverev +4.
- Wins: Sonego +6.5, Under 33.5.

### Zverev extended four-set control
Representative: **6-4, 4-6, 6-3, 6-4**
- Total games: 39.
- Net margin: Zverev +5.
- Wins: Sonego +6.5, Over 33.5.

### Zverev separation four-set win
Representative: **6-3, 6-4, 4-6, 6-2**
- Total games: 37.
- Net margin: Zverev +7.
- Wins: Zverev -6.5, Over 33.5.

### Sonego ordinary upset
Any Sonego outright win automatically wins Sonego +6.5. A four- or five-set upset strongly favors Over 33.5; a straight-set upset is a remote Under path.

## I. Reference base-rate anchors

No calibrated probabilities are generated.

### Sonego +6.5
**Reference band: MEDIUM-HIGH**
- large positive game cushion;
- every Sonego win qualifies;
- many close Zverev straight/four-set wins qualify.
Event adjustment:
- up modestly from all three historical H2H game margins staying inside +6.5;
- down modestly for Zverev's elite Bo5/top-level gap.
**Frozen band: MEDIUM-HIGH.**

### Zverev -6.5
**Reference band: MEDIUM-LOW**
- requires substantial game separation.
Event adjustment:
- up for ranking/serve/Grand-Slam superiority and Sonego's poor Top-10 hard record;
- down because Zverev's latest hard matches have included tiebreak/close-set states and all prior H2Hs stayed inside this margin.
**Frozen band: MEDIUM-LOW / MEDIUM.**

### Under 33.5
**Reference band: MEDIUM**
- straight sets are structurally favored in a large mismatch;
- many normal 3-0 Zverev scores land below 34.
Event adjustment:
- up slightly because the three-set endpoint is the central branch.
**Frozen band: MEDIUM / slight lean.**

### Over 33.5
**Reference band: MEDIUM**
- four sets usually clear;
- close three-set scorelines can clear too.
Event adjustment:
- down slightly because Sonego winning a set is meaningful but not central.
**Frozen band: MEDIUM-LOW / boundary.**

## J. External market sanity check — non-controlling

Current public books showed:
- Zverev as a very heavy match favorite;
- Sonego +6.5 and Zverev -6.5 priced close to even, with several snapshots marginally favoring Sonego +6.5;
- total 33.5 near a 50/50 boundary, with some books slightly favoring Under and others slightly favoring Over;
- Zverev 3-0 as the single shortest correct-score outcome.

These are **not the user's operator**, are not internal probabilities and are not value evidence. They support the qualitative conclusion that:
1. winner certainty is much higher than handicap certainty;
2. +6.5 is a meaningful cushion;
3. the 33.5 total is genuinely near the central score corridor.

## K. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE  
**Retirement terms:** UNKNOWN_DEFINITION

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-245-C01 — Sonego +6.5 games** | **LEAN** | MEDIUM | The cushion survives every prior H2H margin and many plausible close-straight/four-set Zverev wins. |
| **2** | **P-245-C04 — Under 33.5 games** | **SLIGHT LEAN** | MEDIUM-LOW | Zverev straight sets are the central set-count branch; ordinary 3-0 scores land below 34. |
| **3** | **P-245-C02 — Zverev -6.5 games** | **LEAN-ADJACENT / FORCED RANK** | MEDIUM-LOW | Elite mismatch creates strong separation paths, but the line is large and prior matchup margins argue against assuming blowout conversion. |
| **4** | **P-245-C03 — Over 33.5 games** | **FORCED RANK / weaker total direction** | LOW-MEDIUM | Four sets or extremely close straight sets clear it, but those are secondary to the straight-set central branch. |

### Total-direction control
Recommend **Under 33.5 only** among the two opposing total directions.

## L. Potential winner

**Alexander Zverev — LEAN, with substantially stronger winner evidence than any derivative contract.**

This is not a fifth independent pick.

Why:
1. current world ranking #2 vs Sonego #89;
2. Zverev leads H2H 3-0;
3. Zverev is 17-7 on hard in 2026 versus Sonego around 5-5;
4. Zverev's 2026 Grand Slam record is 18-2;
5. Zverev's hard best-of-five record is elite;
6. Sonego is only about 4-20 against Top-10 opponents on hard.

Why the -6.5 handicap is much less certain than the winner:
- all three H2Hs stayed inside a 6.5-game Sonego cushion;
- Zverev's latest hard matches include several tiebreaks and close-set states;
- Sonego can lose 3-0 and still cover +6.5 if two sets are close.

## M. Frozen user-facing forecast

### Verified event/status
Alexander Zverev vs Lorenzo Sonego is a **2026 US Open Men's Singles Round 1 match at Arthur Ashe Stadium, hard court, best-of-five**. At the final refresh the match was still listed **Upcoming / Not started**, with the current bracket start around **11:20 AEST**, roughly 44 minutes after the frozen cutoff.

### Best four supplied picks
1. **Sonego +6.5 games — LEAN**
2. **Under 33.5 total games — SLIGHT LEAN**
3. **Zverev -6.5 games — lower-confidence separation side**
4. **Over 33.5 games — weaker total direction**

### Why Sonego +6.5 is #1
Zverev is overwhelmingly the stronger match-winner candidate, but +6.5 is a large game cushion.

The three verified prior meetings all went to Zverev, yet every one would have landed inside Sonego +6.5:
- Beijing 2025 hard: Zverev 6-4, 6-3 — +5 net games.
- Halle 2025: Zverev won in three with net games roughly level.
- Halle 2024: Zverev 6-4, 7-6 — +3 net games.

Best-of-five can amplify Zverev's quality edge, so I do not mechanically project those covers. But Sonego's recent matches still contain tiebreak/close-set patterns, and Zverev's North American hard swing has not been uniformly dominant.

A representative **7-6, 6-4, 6-4 Zverev straight-set win** finishes at only +4 net games, so Sonego +6.5 can win even while Zverev wins comfortably in sets.

### Why Under 33.5 is #2
The central match-length state is Zverev 3-0.

An ordinary Zverev straight-set score like **6-3, 6-4, 6-3** totals only 28 games. Even a closer **7-6, 6-4, 6-4** totals 33, still Under 33.5.

The Over becomes much stronger if Sonego wins a set; most four-set states clear 33.5. But I do not make Sonego taking a set the central branch given Zverev's ranking, Grand Slam record and serve/return edge.

### Why Zverev -6.5 is only #3
Zverev has obvious blowout routes. A 6-3, 6-4, 6-3 score covers comfortably.

The issue is that -6.5 needs **game separation**, not merely a straight-set win. Zverev could win 3-0 with one or two tiebreak/close sets and fail -6.5. The historical H2H margins reinforce that caution.

### Likely winner
**Alexander Zverev — LEAN.**

This is not an additional independent pick.

### Environment
Arthur Ashe has a retractable roof. Heavy rain affected the US Open session, and earlier Ashe matches were played under the roof. The exact Zverev-Sonego roof state was not independently field-owner confirmed at cutoff, so no weather-based total adjustment is made.

### Settlement/publication boundary
No operator or retirement rule was supplied. Exact retirement/walkover/void handling therefore remains `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking recommendation is published.

## N. Append confirmation

- Complete frozen P-245 forecast appended before delivery: **YES**
- State confirmed not started at cutoff: **YES**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

# P-246 — New York Yankees @ Los Angeles Angels — MLB — STATE-CROSSED / NO ACTIONABLE LIVE FORECAST

## A. Identity and request state

- **Append sequence:** P-246
- **Request received:** 2026-09-02 approximately 11:39 AEST
- **Scheduled first pitch:** 2026-09-01 18:38 PDT / 2026-09-02 11:38 AEST
- **Sport:** Baseball
- **Competition:** MLB regular season
- **Fixture:** New York Yankees @ Los Angeles Angels
- **Venue:** Angel Stadium, Anaheim, California
- **Supplied probable pitchers:** Gerrit Cole / Grayson Rodriguez
- **Official probable-pitcher verification:** PASS
  - Gerrit Cole, NYY: 7-7, 3.19 ERA, 105 SO
  - Grayson Rodriguez, LAA: 4-5, 6.03 ERA, 65 SO
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-BASEBALL

## B. Start-state gate

The request arrived at or immediately after the scheduled first pitch.

Current state evidence was inconsistent:
- MLB standings/schedule surfaces marked the event **LIVE**.
- One current live-score source showed **NYY 0 — LAA 1**.
- The MLB schedule surface returned **NYY 0 — LAA 0**.
- Current CBS/MLB pages did not expose a consistently retrievable inning/phase state in the same research window.

Because the active framework requires a verified live state before directional live analysis after first pitch, this card is classified:

**`LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`**

No stale pregame freeze is fabricated.

## C. Supplied contracts preserved for audit only

1. Yankees -1.5
2. Angels +1.5
3. Over 7.5
4. Under 7.5

- **Operator:** NOT SUPPLIED
- **Odds:** NOT SUPPLIED
- **Listed-pitcher/action rule:** UNKNOWN_DEFINITION
- **Extra-inning rule:** UNKNOWN_DEFINITION
- **Shortened/suspended-game rule:** UNKNOWN_DEFINITION
- **No ranking issued after state-crossing.**

## D. Pregame research evidence preserved — NON-ACTIONABLE

### Starter baseline

**Gerrit Cole**
- 2026: 7-7, 3.19 ERA, 1.07 WHIP.
- Last five starts: 30.2 IP, 8 ER, **2.35 ERA**, 32 K, 7 BB.
- Recent starts included 6 IP/1 ER at Baltimore, 6 IP/1 ER at Toronto, 7 IP/2 ER vs Atlanta.
- Stronger established current starter centre than Rodriguez.

**Grayson Rodriguez**
- 2026: 4-5, 6.03 ERA, 1.52 WHIP.
- Last five starts: 27.2 IP, 9 ER, **2.93 ERA**, 29 K.
- Latest two starts: 7 IP with 0 ER at Houston, then 5.2 IP with 1 ER vs Cleveland.
- His recent form materially improved from the poor full-season ERA and therefore blocked a simple “season ERA = Yankees blowout” argument.

### Team / bullpen context
- Yankees: 78-60, +108 run differential entering the game.
- Angels: 53-85.
- Yankees bullpen ERA over the prior 15 days: **2.65**.
- Angels bullpen ERA over the prior 15 days: **4.01**.
- Yankees recent scoring snapshots were roughly 5.4 R/G over the freshest L5 and about 4.6-5.7 over current L10 snapshots depending retrieval timestamp.
- Angels current L10 scoring snapshot: about **3.5 R/G**.
- Angels had won the series opener 10-1, but that was against a different starter and is not inserted as a current Cole/Rodriguez expectation.
- Aaron Judge remained out; the Yankees' lineup therefore was not full-strength.
- Current game reporting indicated New York planned a heavily left-handed lineup against Rodriguez.

### Environment
- Angel Stadium: outdoor.
- NWS near first pitch:
  - about 79°F at 18:00 PDT, 76°F around 19:00;
  - dew point about 58°F;
  - SW wind about 7-8 mph;
  - 0% precipitation.
- Weather did not create a strong directional total adjustment.

### Pregame market sanity check — external only
Same-day public snapshots had approximately:
- Yankees ML around -175 to -192;
- Yankees -1.5 around -102 to -110;
- Angels +1.5 around -118 to -110;
- total 7.5 with Over roughly -120 to -110 and Under roughly -102 to -110.

This is not the user's operator and is not a value claim. It shows:
- strong market preference for Yankees outright;
- much weaker confidence in Yankees -1.5 than in the moneyline;
- 7.5 was a genuine boundary total rather than a one-sided market.

## E. Why no ranking is issued

A valid pregame card requires `cutoff_at < scheduled_start_at`.
That condition failed.

A valid live card requires:
- score,
- inning/half-inning,
- outs/base state where material,
- participant orientation,
- current pitcher/batter state,
- consistent current feeds.

Those fields were not verified consistently enough.

Therefore:
- no four-pick directional ranking is issued;
- no likely-winner call is issued as an actionable live forecast;
- no stale pregame analysis is retroactively frozen;
- no probabilities/value/edge/ROI/staking claims are made.

## F. Research-only pregame conclusion

Before state crossing, the cleanest **non-actionable research conclusion** would have been:
- **Outright matchup edge:** Yankees, primarily because of Cole + bullpen quality.
- **Run-line uncertainty:** materially higher than moneyline certainty because Rodriguez's last-five form had improved and Angels +1.5 carried the positive cushion.
- **Total:** genuinely two-sided at 7.5; Cole/Yankees bullpen supported lower states, while Rodriguez's season volatility and the Yankees' left-handed matchup path supported upper states.

This section is preserved as research evidence only and is **not an issued forecast**.

## G. Append confirmation

- State checked before issuing a forecast: **YES**
- Event already at/after scheduled start: **YES**
- Live state consistently verified: **NO**
- Actionable forecast issued: **NO**
- Stale pregame forecast fabricated: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Drive modified: **NO**


---

## Administrative continuation note — before P-247

The connected Drive canonical top snapshot remains behind the local read-only continuation (`Next canonical ID: P-239`). The local append-only sequence already contains P-239 through P-246. This distinct event is therefore appended locally as **P-247**. No Google Drive file is modified.

---

# P-247 — Philadelphia Phillies @ Arizona Diamondbacks — MLB — ZERO-PITCH LIVE-START FORECAST

## A. Frozen identity and live state

- **Append sequence:** P-247
- **Request type:** LIVE
- **Final state refresh / frozen cutoff:** 2026-09-02 11:45 AEST (Australia/Melbourne)
- **Scheduled first pitch:** 2026-09-01 21:40 EDT / 18:40 MST at Chase Field
- **Sport:** Baseball
- **Competition:** MLB regular season
- **Fixture:** Philadelphia Phillies @ Arizona Diamondbacks
- **Venue:** Chase Field, Phoenix, Arizona
- **Venue class:** RETRACTABLE
- **Roof state at frozen live feed:** CLOSED
- **Frozen score:** PHI 0 — ARI 0
- **Frozen inning:** Top 1
- **Frozen phase:** LIVE (WARMUP)
- **Frozen batter/pitcher orientation:** Kyle Schwarber due; Eduardo Rodríguez pitching
- **Pitch count / starter exposure at frozen state:** 0 pitches recorded; both starters displayed at 0.0 IP
- **GAME-STATE:** `LIVE_ZERO_PITCH_WARMUP`
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-BASEBALL
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective performed:** NO

### Live-state freshness note

The best retrieved live game feed showed the zero-pitch warmup state above. This forecast is frozen **only** to that state. No pitch, run, baserunner or result first known after the frozen cutoff is inserted into this analysis. If a downstream app displayed a later state by the time of delivery, this card remains the immutable 0-0/Top-1/warmup forecast rather than being silently refreshed.

## B. Starter / participant handshake

### Philadelphia — Jesús Luzardo, LHP
- Official MLB probable/starting listing: **12-5, 3.09 ERA, 203 SO**.
- Current season WHIP around **1.12**.
- Current preview: approximately **11.2 K/9**.
- Latest start (Aug. 26 at Seattle): **7 IP, 0 ER, 1 H**.
- Current preview reports approximately a **1.90 ERA since June 10**, materially better than his early-season volatility.
- First-inning suppression has been particularly strong in 2026.
- Earlier 2026 direct start vs Arizona (Apr. 10): 4.2 IP, 5 ER. This is retained as matchup downside evidence but is heavily downweighted relative to his current regime.

### Arizona — Eduardo Rodríguez, LHP
- Official MLB probable/starting listing: **14-4, 2.50 ERA, 119 SO**.
- Season WHIP around **1.19**.
- Last five starts: **31.1 IP, 9 ER, 2.59 ERA**, 31 K.
- Last four starts before P-247: approximately **25.2 IP, 4 ER**, including back-to-back scoreless outings vs Cincinnati and Chicago.
- Latest start (Aug. 26 vs Cubs): **7 IP, 0 ER, 2 H, 9 K**.
- Recent home state is strong and materially reduces Philadelphia's ordinary early-run ceiling.
- Secondary expected-stat commentary suggested some ERA regression risk, but that is lower-authority evidence and does not override the actual current results.

## C. Confirmed/current lineup state

The live game feed / current match pages exposed the game-day batting orders.

### Philadelphia
1. Kyle Schwarber — DH
2. Trea Turner — SS
3. Bryce Harper — RF
4. Luis Arraez — 2B
5. Alec Bohm — 1B
6. Edmundo Sosa — LF
7. Bryson Stott — 3B
8. J.T. Realmuto — C
9. Derek Hill — CF

### Arizona
1. Geraldo Perdomo — SS
2. Corbin Carroll — RF
3. Gabriel Moreno — C
4. Ketel Marte — DH
5. Nolan Arenado — 3B
6. Ildemaro Vargas — 2B
7. Tim Tawa — 1B
8. Jordan Lawlar — CF
9. Ryan Waldschmidt — LF

Lineup interpretation:
- Philadelphia carries the stronger concentrated top-order power/OBP branch.
- Arizona has meaningful contact and speed through Perdomo/Carroll/Moreno/Marte.
- Both starters are left-handed, so platoon composition matters, but neither lineup is weak enough to erase late scoring tails.

## D. Contract freeze

### User-supplied slate
1. Phillies ML
2. Diamondbacks +1.5
3. Full-game Over 7.5
4. Full-game Under 7.5

- **Operator:** NOT SUPPLIED
- **User odds:** NOT SUPPLIED
- **Listed-pitcher/action terms:** UNKNOWN_DEFINITION
- **Extra-inning treatment:** UNKNOWN_DEFINITION from user/operator
- **Sporting target for analysis:** official MLB full-game result including extra innings if played.
- **Shortened/suspended-game settlement:** UNKNOWN_DEFINITION.

### Geometry
- Phillies ML and Diamondbacks +1.5 are **not complements**:
  - both win when Philadelphia wins by exactly one;
  - Arizona +1.5 also wins on every Arizona outright win;
  - Phillies ML loses on every Arizona win.
- Over 7.5 and Under 7.5 are exact half-run complements under normal completed-game action.

| ID | Contract | Geometry | Dependence group |
|---|---|---|---|
| P-247-C01 | Phillies ML | PHI final win | P247-WINNER |
| P-247-C02 | Diamondbacks +1.5 | ARI win or PHI by exactly 1 | P247-MARGIN |
| P-247-C03 | Over 7.5 | 8+ total runs | P247-TOTAL |
| P-247-C04 | Under 7.5 | 0-7 total runs | P247-TOTAL |

## E. Recent team form

### Philadelphia
- Record at freeze: **78-60**.
- Current streak entering game: **five straight wins**.
- Current broader run: **14 wins in the last 16**.
- Last 10: **8-2**.
- Current L10 scoring: approximately **5.2 runs/game**.
- August record: **21-7**, best in MLB in the cited current report.
- Recent road wins immediately before Arizona included 5-2, 4-2 and 5-3 over the Angels, plus a 6-0 win in Seattle.

### Arizona
- Record at freeze: **73-66**.
- Last 10 around **5-5** on the freshest current team snapshot; timestamped StatMuse windows ranged roughly **3.8-4.6 runs/game** as the rolling set changed.
- Lost the opener of this series 2-1.
- Arizona generated nine hits and four walks in the opener but went **0-for-9 with runners in scoring position**, showing traffic without conversion.
- Ketel Marte returned to the lineup in the opener after a 13-game absence.

### Trend verdict
- Philadelphia: clearly positive result regime, but L5/L10/L15/L20 run-rate windows are not treated as independent evidence.
- Arizona: mixed; no monotone directional trend is promoted.

## F. 2026 H2H / matchup continuity

Current completed 2026 meetings before this frozen state include:
- April 10: Arizona 5-4
- April 11: Philadelphia 4-3
- April 12: Arizona 4-3
- Aug. 31: Philadelphia 2-1

Implications at a 7.5 total:
- one of the four completed meetings cleared 7.5;
- three finished at 7 or fewer.
- All four were one-run games.

**Continuity verdict:** MODERATE.
- same clubs and several same core hitters;
- but pitchers, bullpen roles, injuries and current regimes differ substantially.
- H2H is therefore descriptive, not a direct probability estimate.

The repeated one-run geometry is relevant to **Diamondbacks +1.5**, but it is not treated as four independent confirmations.

## G. Bullpen state and prior-day workload

### Philadelphia
In the 2-1 opener, after Aaron Nola's five innings the Phillies used:
- Alex McFarlane — 15 pitches
- Orion Kerkering — 11
- Brooks Raley — 3
- José Alvarado — 14
- Jhoan Duran — 18

All five worked scoreless relief innings/outs.

Interpretation:
- quality state is good;
- several high-leverage arms were used the previous night;
- individual pitch counts were mostly moderate, so they are not automatically unavailable;
- repeated high-leverage usage reduces the certainty of a pristine full-game Under branch.

### Arizona
The Diamondbacks used:
- Jonathan Loáisiga — 14 pitches
- Juan Morillo — **33 pitches**
- Kevin Ginkel — 12 pitches

Interpretation:
- Morillo is the clearest likely workload limitation.
- Other key relief pieces were less taxed.
- Arizona's late-game depth is not fully fresh, adding a small upper-tail run mechanism.

## H. Venue / roof / environment

- **Chase Field:** retractable roof.
- Frozen live feed: **roof closed**.
- Displayed in-stadium condition: approximately **76°F**, no wind influence.
- External preview park profile: mild positive run/HR environment, roughly neutral-to-slightly hitter friendly rather than Coors-like.

Mechanism:
- outdoor Phoenix heat/wind is not directly applied with the roof closed.
- total direction must come from pitchers, offenses, relief exposure and score corridor rather than generic desert weather.

## I. Live target / score-family model

Because the frozen live state is **0-0 before a recorded pitch**, the original full-game target is effectively intact, but it is explicitly stored as a live zero-pitch state rather than retroactively labelled pregame.

### Low / close
Representative:
- PHI 3-2
- PHI 4-3
- ARI 3-2
- ARI 4-3

Supports:
- Diamondbacks +1.5
- Phillies ML in PHI versions
- Under 7.5 for 3-2/4-3

### Low / Philadelphia separation
Representative:
- PHI 4-1
- PHI 5-2

Supports:
- Phillies ML
- Under 7.5 at 4-1/5-2
- defeats Arizona +1.5 if margin 2+

### High / close
Representative:
- PHI 5-4
- ARI 5-4

Supports:
- Diamondbacks +1.5
- Over 7.5

### High / Philadelphia
Representative:
- PHI 6-3 / 6-4

Supports:
- Phillies ML
- Over 7.5
- often defeats Arizona +1.5

### Arizona control kill path
Representative:
- ARI 4-2 / 5-3

Mechanism:
- E. Rodríguez sustains his current form;
- Arizona converts traffic better than in the opener;
- Philadelphia's prior-day bullpen workload matters late.

## J. Total 7.5 component budget

### Under mechanisms
1. Two strong current starting-pitcher centres:
   - Luzardo 3.09 season ERA with excellent recent run prevention;
   - Rodríguez 2.50 season ERA / 2.59 last-five ERA.
2. Roof closed removes material weather variance.
3. Three of four current-season meetings finished with seven runs or fewer.
4. Both starters have recent six/seven-inning efficiency branches.

### Over mechanisms
1. Philadelphia offense: ~5.2 R/G over current L10.
2. Arizona has generated baserunners/traffic even during lower-scoring games.
3. Both relief groups used multiple arms in the opener; Philadelphia used five different relievers.
4. Arizona's Morillo threw 33 pitches.
5. Chase Field carries a mild positive HR/run environment.
6. Philadelphia's top order has high-impact extra-base potential.

### Corridor conclusion
**7.5 lies inside the central corridor.**
Representative central totals are roughly 6-8 runs.
The Under has a small mechanism edge from the two starter profiles, but ordinary upper branches reach eight without requiring a collapse.

Therefore the total evidence is capped below strong language.

## K. External same-day market sanity check — non-controlling

External same-day prices located during research varied by snapshot:
- Phillies ML approximately **1.64-1.66** in one current market;
- Arizona +1.5 approximately **1.60**;
- total 7.5 ranged from essentially even to an **Over-shorter** configuration in another snapshot.

An earlier market also dealt an 8.5 total.

Interpretation:
- external market agrees Arizona +1.5 can be marginally more likely than Phillies ML despite Philadelphia being the outright favorite;
- total pricing does **not** provide stable confirmation for either direction;
- market evidence is external only and does not create an internal value claim.

## L. Reference base-rate anchors

No calibrated probabilities are generated.

| Contract | Reference band | Live/event adjustment | Frozen band |
|---|---|---|---|
| Diamondbacks +1.5 | HIGH-MEDIUM | Strong E-Rod form + repeated close-game geometry; down for PHI current team form | **MEDIUM-HIGH** |
| Phillies ML | MEDIUM | Up for current team form/offense/Luzardo; down for E-Rod quality | **MEDIUM-HIGH, slightly below ARI +1.5** |
| Under 7.5 | MEDIUM | Up for starter quality/closed roof; down for bullpen usage and PHI offense | **MEDIUM / slight lean** |
| Over 7.5 | MEDIUM | Up for offense/relief exposure; down for two strong SP states | **MEDIUM-LOW / boundary** |

## M. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-247-C02 — Diamondbacks +1.5** | **LEAN** | MEDIUM | Positive run cushion, E-Rod's elite current form, and close-game pathways; can win alongside a one-run Phillies victory. |
| **2** | **P-247-C01 — Phillies ML** | **LEAN** | MEDIUM | Philadelphia is the stronger current team, hotter offense and stronger overall winner profile, but E-Rod materially narrows the gap. |
| **3** | **P-247-C04 — Under 7.5** | **SLIGHT LEAN** | MEDIUM-LOW | Two high-quality current starter profiles and closed roof; total remains boundary because relief usage/offense can create eight. |
| **4** | **P-247-C03 — Over 7.5** | **FORCED RANK / weaker total direction** | LOW-MEDIUM | Credible through bullpen/four-plus-run components, but requires the starter-suppression branch to be overcome. |

### Total-direction control
Recommend **Under 7.5 only**, and only as a slight lean.

### Strongest evidence type
**Side market first**, specifically the Arizona +1.5 cushion.  
Outright winner evidence still favors Philadelphia.

## N. Potential winner

**Philadelphia Phillies — LEAN**

Not an additional independent contract.

Reasons:
1. 78-60 vs 73-66.
2. Philadelphia has won five straight and 14 of 16.
3. Phillies score ~5.2 R/G over the current L10.
4. Luzardo combines a 3.09 ERA with a major strikeout advantage.
5. Philadelphia's bullpen has recently rounded into materially better form.

Counterweight:
- Eduardo Rodríguez has arguably the best immediate starter form in the matchup.
- Arizona has home field and strong top-half lineup quality.
- Four completed 2026 meetings before P-247 were all decided by one run.
- Philadelphia's high-leverage bullpen was used extensively in the opener.

## O. Frozen user-facing forecast

### Verified live state
The best live feed at the frozen cutoff showed:

- **PHI 0 — ARI 0**
- **Top 1**
- **Live / Warmup**
- **0 pitches recorded**
- **Eduardo Rodríguez on the mound**
- **Kyle Schwarber due**
- **Chase Field roof closed**

This is therefore a **zero-pitch live-start forecast**, not a retroactive pregame forecast.

### Best four supplied picks
1. **Diamondbacks +1.5 — LEAN**
2. **Phillies ML — LEAN**
3. **Under 7.5 — SLIGHT LEAN**
4. **Over 7.5 — weaker total direction**

### Why Diamondbacks +1.5 is #1
The cushion is more forgiving than asking Philadelphia simply to win.

Eduardo Rodríguez has a 2.50 season ERA and a 2.59 ERA over his last five starts. His two most recent outings were scoreless, and he has allowed only four earned runs across his last four starts. That makes a close game a very credible central branch.

At the same time, Philadelphia is still the better outright team. A 3-2 or 4-3 Phillies win makes **both** Diamondbacks +1.5 and Phillies ML successful.

The 2026 series has also repeatedly produced one-run games, including the 2-1 Philadelphia win in the opener. That is descriptive matchup geometry, not an independent cover-rate model.

### Why Phillies ML is #2
Philadelphia enters 78-60, on a five-game winning streak and 14-2 over its latest 16-game stretch. The Phillies are scoring about 5.2 runs per game over their last ten.

Luzardo is also strong enough to keep Arizona's offense controlled: 3.09 ERA, 1.12 WHIP and 203 strikeouts.

The reason this does not rank first is Eduardo Rodríguez. His current run-prevention state is strong enough that Arizona's outright-win branch remains substantial.

### Why Under 7.5 is #3
Both starting pitchers enter in excellent current form, and the roof is closed.

A 3-2, 4-2, 4-3 or 5-2 game all lands Under. Three of the four completed 2026 meetings before tonight also finished at seven runs or fewer.

The concern is bullpen workload. Philadelphia used five relievers in the opener and Arizona used three, including 33 pitches from Juan Morillo. Philadelphia's offense also has enough current form to turn a 3-2 game into 5-3 quickly.

So Under 7.5 is only a **slight lean**.

### Likely winner
**Philadelphia Phillies — LEAN.**

This is not a fifth independent contract.

### Publication/settlement boundary
No user sportsbook or odds were supplied. Listed-pitcher/action rules, shortened-game terms and exact extra-inning settlement therefore remain `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking recommendation is published.

## P. Append confirmation

- Complete frozen P-247 forecast appended before delivery: **YES**
- Live state frozen: **YES**
- Later live facts backfilled: **NO**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

## Administrative continuation note — before P-248

The connected Drive canonical top snapshot remains behind the local read-only continuation. The local append-only sequence already contains issued P-239 through P-247. This distinct event is therefore appended locally as **P-248**. No Google Drive file is modified.

---

# P-248 — St. Louis Cardinals @ Los Angeles Dodgers — MLB — PREGAME FORECAST

## A. Frozen identity and state

- **Append sequence:** P-248
- **Request time:** 2026-09-02 11:51 AEST
- **Final state refresh / frozen cutoff:** 2026-09-02 11:52:45 AEST
- **Scheduled first pitch:** 2026-09-01 19:10 PDT / 2026-09-02 12:10 AEST
- **Cutoff invariant:** PASS — approximately 17 minutes before scheduled first pitch.
- **GAME-STATE:** PREGAME / SCHEDULED / NO RECORDED PLAYS
- **Sport:** Baseball
- **Competition:** MLB regular season
- **Fixture:** St. Louis Cardinals @ Los Angeles Dodgers
- **Venue:** UNIQLO Field at Dodger Stadium, Los Angeles, California
- **Venue class:** OUTDOOR
- **Records at cutoff:** STL 68-70; LAD 82-55
- **Method:** MDS-2026.08.31-v2.9
- **General algorithm:** GFA-1
- **Sport algorithm:** SFA-BASEBALL
- **Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING
- **Value state:** NO VALUE DETERMINABLE
- **Retrospective performed:** NO

A current game-status page showed the event as scheduled, 0-0, with no recorded plays at the frozen cutoff.

## B. Starter handshake

### St. Louis — Michael McGreevy, RHP
- MLB official probable: **5-9, 3.86 ERA, 98 SO**.
- Season: 142.1 IP, 1.25 WHIP.
- Latest five starts reconstructed from the current game log:
  - 8/26 vs BAL: 5 IP, 7 ER
  - 8/20 at CIN: 5.1 IP, 3 ER
  - 8/15 at CHC: 6 IP, 0 ER
  - 8/9 vs COL: 5.2 IP, 3 ER
  - 8/3 at NYY: 4.1 IP, 2 ER
- Last-five aggregate: approximately **26.1 IP / 15 ER / 5.13 ERA**.
- Latest start was materially poor: 10 hits and seven earned runs in five innings.
- Direct 2026 matchup vs LAD (May 2): **6 scoreless innings**, three hits, three walks in a 3-2 Cardinals win.
- That direct success is relevant but not controlling; the Dodgers lineup/health and McGreevy's current form have changed.

### Los Angeles — Eric Lauer, LHP
- MLB official probable: **8-6, 4.78 ERA, 70 SO**.
- Current full-season line: about 105.1 IP, 1.26 WHIP.
- Latest five starts reconstructed from the current game log:
  - 8/18 at COL: 5 IP, 4 ER
  - 8/12 vs KC: 6.1 IP, 1 ER
  - 8/5 at CHC: 4 IP, 6 ER
  - 7/29 vs SEA: 6 IP, 0 ER
  - 7/22 at PHI: 5.1 IP, 3 ER
- Last-five aggregate: approximately **26.2 IP / 14 ER / 4.73 ERA**.
- Current reporting notes Lauer has generally pitched better at Dodger Stadium than his overall season ERA suggests.
- He is not an ace-level suppression anchor; ordinary 3-4 run Cardinals branches remain live.

## C. Contract freeze and geometry

### User-supplied slate
1. Dodgers -1.5
2. Cardinals +1.5
3. Full-game Over 9.0
4. Full-game Under 9.0

- **Operator:** NOT SUPPLIED
- **User odds:** NOT SUPPLIED
- **Listed-pitcher/action terms:** UNKNOWN_DEFINITION
- **Shortened/suspended-game rule:** UNKNOWN_DEFINITION
- **Extra-inning grading:** UNKNOWN_DEFINITION
- **Sporting target assumption for analysis:** official MLB full-game final score including extra innings if played.

### Geometry
- LAD -1.5 and STL +1.5 are exact margin complements under ordinary completed-game grading.
- Over 9.0 and Under 9.0 include **push mass at exactly 9 runs**:
  - Over wins at 10+;
  - Under wins at 8 or fewer;
  - exactly 9 pushes under ordinary total-9 terms.
- Therefore the total pair does not force one winner.

| ID | Contract | Win / Push / Loss geometry | Dependence |
|---|---|---|---|
| P-248-C01 | Dodgers -1.5 | LAD by 2+ | P248-MARGIN |
| P-248-C02 | Cardinals +1.5 | STL win or LAD by exactly 1 | P248-MARGIN |
| P-248-C03 | Over 9.0 | 10+ / 9 / 0-8 | P248-TOTAL |
| P-248-C04 | Under 9.0 | 0-8 / 9 / 10+ | P248-TOTAL |

## D. Lineup / availability gate

### Official lineup status
The MLB official lineup page still displayed **TBD** for both clubs at the frozen cutoff. Therefore projected/secondary orders are not promoted to `CONFIRMED_OFFICIAL`.

### Current secondary game-day lineup
A current CBS game page listed:

**St. Louis**
1. José Fermín — 2B
2. Iván Herrera — DH
3. Jordan Walker — RF
4. Alec Burleson — 1B
5. Joshua Báez — LF
6. Leo Bernal — C
7. Ramón Urías — 3B
8. Thomas Saggese — SS
9. Nathan Church — CF

**Los Angeles**
1. Shohei Ohtani — DH
2. Freddie Freeman — 1B
3. Mookie Betts — SS
4. Max Muncy — 3B
5. Will Smith — C
6. Kyle Tucker — RF
7. Tommy Edman — CF
8. Teoscar Hernández — LF
9. Alex Freeland — 2B

### Material availability
- Dodgers activated **Will Smith** from the injured list on Sep. 1; he is expected to materially deepen the lineup after a long absence.
- Dodgers also activated Justin Wrobleski as relief/length depth.
- Cardinals placed **JJ Wetherholt** on the 10-day IL with wrist tendinitis.
- Current injury reporting also listed Masyn Winn and Andre Pallante as unavailable/uncertain around this game.
- Because the field-owning lineup page remained TBD, lineup-specific claims remain capped below strong evidence.

## E. Environment gate

- **Venue:** Dodger Stadium, Los Angeles
- **Venue class:** OUTDOOR
- NWS evening forecast:
  - clear / mostly clear;
  - low near 61°F overnight;
  - west-southwest wind roughly **5-10 mph**, becoming light southeast later;
  - no meaningful precipitation signal.
- No extreme heat, rain or high-wind condition was present.
- Weather therefore receives only a small/neutral scoring adjustment.

## F. Recent-form block

### St. Louis
- Season scoring: **4.42 R/G**.
- Current L10: **4.8 R/G**.
- Current L20 from the freshest 2-day-old StatMuse snapshot: **98 runs / 20 = 4.9 R/G**.
- One recent L15 snapshot showed a higher 5.0 R/G state, while an older snapshot showed a materially lower figure; source timing is explicitly inconsistent.
- Team form: Cardinals entered having lost **seven of nine** and only three of the last ten.
- **Trend verdict:** NO TREND — NOISE. Recent scoring windows are snapshot-sensitive and not monotone.

### Los Angeles
- Current L10 freshest snapshot: **3.6 R/G**, reflecting recent offensive cooling.
- Current L15 freshest snapshot: **60 runs / 15 = 4.0 R/G**.
- Current L20 freshest snapshot: **81 runs / 20 = 4.05 R/G**.
- Older StatMuse snapshots show higher earlier-run windows; those are not silently blended into the current window.
- Dodgers are 82-55 and 6-4 over the freshest L10 snapshot despite the lower scoring.
- Current team context: Los Angeles just beat Detroit 6-1 after dropping four of its previous five.
- **Trend verdict:** current scoring centre has cooled, but no monotone L5/L10/L15/L20 trend is promoted.

## G. H2H / matchup continuity

2026 series in St. Louis:
- May 1: STL 7-2
- May 2: STL 3-2 — McGreevy 6 scoreless
- May 3: LAD 4-1

### Continuity verdict
**MODERATE, not controlling.**
- Same clubs/core offensive identities.
- Direct McGreevy matchup is relevant.
- Current September roster differs: Will Smith returns, Cardinals are without Wetherholt, and both bullpens/current forms have changed.
- Two of the three prior games were Under 9; one finished exactly 9.

The old series is descriptive, not a fitted H2H probability.

## H. Bullpen state

### Los Angeles
- Relief ERA over the prior 15 days: approximately **3.00**.
- Blake Treinen remains close to returning but was not yet activated.
- Justin Wrobleski was activated and is expected to work in relief, increasing left-handed/length depth.
- Dodgers received seven innings from Tyler Glasnow in their most recent game (6-1 win over Detroit), reducing immediate bullpen burden.

### St. Louis
- Relief ERA over the prior 15 days: approximately **6.10**.
- This is a material current weakness.
- Cardinals' starter McGreevy has averaged only around five-plus innings in several recent starts, increasing the chance of exposing that relief group.
- Andre Pallante was unavailable/uncertain in current injury reporting.

### Bullpen conclusion
The largest late-game asymmetry favors **Los Angeles**, and it is a major reason the Dodgers remain the likely outright winner despite Lauer's own volatility.

## I. Score-family / component-budget model

### Low / close
Representative:
- LAD 4-3
- LAD 5-4
- STL 4-3

Supports:
- Cardinals +1.5
- Under 9 at 4-3; push at 5-4

### Low / Dodgers separation
Representative:
- LAD 5-2
- LAD 6-2

Supports:
- Dodgers -1.5
- Under 9

### Boundary
Representative:
- LAD 5-4
- LAD 6-3

Total = exactly 9 → ordinary **push** on O/U 9.

### High / close
Representative:
- LAD 6-5
- STL 6-5

Supports:
- Cardinals +1.5
- Over 9

### High / Dodgers separation
Representative:
- LAD 7-3
- LAD 8-3

Supports:
- Dodgers -1.5
- Over 9

### Cardinals control kill path
Representative:
- STL 5-3 / 6-4

Mechanism:
- McGreevy repeats part of his May matchup success;
- Lauer's volatility appears;
- Dodgers' current offensive slowdown persists.

## J. Total 9.0 component budget

### Under mechanisms
1. Dodgers' current L10/L15/L20 scoring has cooled to roughly 3.6-4.1 R/G.
2. McGreevy has a direct six-scoreless-inning performance against this opponent in 2026.
3. Lauer can still give 5-6 innings of 2-3 run baseball.
4. Clear, ordinary weather does not create a major run boost.
5. The total benefits from **push protection at exactly 9**.

### Over mechanisms
1. McGreevy's last-five ERA is around **5.13**, with seven earned runs allowed in his latest start.
2. Lauer's last-five ERA is around **4.73**.
3. Cardinals current L10 scoring is 4.8 R/G.
4. Cardinals bullpen has a **6.10 ERA over the last 15 days**.
5. Dodgers lineup regains Will Smith and remains deep through Ohtani/Freeman/Betts/Muncy/Tucker despite recent scoring slowdown.

### Corridor conclusion
The central score corridor is approximately **7-10 runs**.
Nine itself carries meaningful boundary mass.
The Under receives a small edge because the current Dodgers run rate is lower than the season/reputation prior and a 5-3 / 6-2 / 5-4 family is ordinary.

## K. External market sanity check — non-controlling

Current same-day public prices:
- Dodgers ML around **-178 to -187**.
- Cardinals +1.5 around **-130 to -150**.
- Dodgers -1.5 around **+108 to +129**.
- Total 9:
  - Over around +100
  - Under around -105 to -120

Interpretation:
- external market strongly supports Dodgers as the outright winner;
- it also treats **Cardinals +1.5 as more likely than Dodgers -1.5**;
- it gives a modest Under lean at 9.

These are not the user's prices and do not establish value.

## L. Reference base-rate anchors

No calibrated probabilities are generated.

| Contract | Reference band | Event adjustment | Frozen band |
|---|---|---|---|
| Cardinals +1.5 | HIGH-MEDIUM | Down for LAD quality/bullpen; up for McGreevy H2H/current LAD scoring slowdown | **MEDIUM-HIGH** |
| Under 9.0 | MEDIUM | Up for push protection/current LAD scoring; down for both SP volatility/STL bullpen | **MEDIUM / slight lean** |
| Dodgers -1.5 | MEDIUM-LOW | Up for team/bullpen/lineup quality and STL pen weakness; down for large separation requirement | **MEDIUM** |
| Over 9.0 | MEDIUM | Up for starter/bullpen volatility; down for current LAD offense and 9-run push | **MEDIUM-LOW** |

## M. Frozen ranking

**Probability state:** NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING  
**Value state:** NO VALUE DETERMINABLE

| Rank | Contract | Verdict | Evidence quality | Core reason |
|---:|---|---|---|---|
| **1** | **P-248-C02 — Cardinals +1.5** | **LEAN** | MEDIUM | Positive cushion, current Dodgers offensive cooling, and McGreevy's prior success vs LAD; every STL win and every one-run LAD win covers. |
| **2** | **P-248-C04 — Under 9.0** | **SLIGHT LEAN** | MEDIUM-LOW | Nine is a high enough boundary with push protection; current LAD scoring is muted and several ordinary score families sit at 7-9. |
| **3** | **P-248-C01 — Dodgers -1.5** | **LEAN-ADJACENT / FORCED RANK** | MEDIUM | Los Angeles owns the clearer team/bullpen advantage, but the two-run requirement is materially harder than the moneyline. |
| **4** | **P-248-C03 — Over 9.0** | **FORCED RANK / weaker total direction** | LOW-MEDIUM | Credible via McGreevy/Lauer volatility and the STL bullpen, but less robust than the Under once current LAD run suppression and the push at 9 are respected. |

### Total-direction control
Recommend **Under 9.0 only**, as a slight lean.

### Strongest evidence type
The strongest supplied contract evidence is **Cardinals +1.5**.
The strongest winner evidence is **Dodgers outright**.

## N. Potential winner

**Los Angeles Dodgers — LEAN**

Not an additional independent contract.

Reasons:
1. 82-55 vs 68-70.
2. Dodgers bullpen current 15-day ERA ~3.00 versus Cardinals ~6.10.
3. St. Louis has lost seven of nine.
4. Dodgers lineup regains Will Smith and remains much deeper.
5. McGreevy's current last-five form is materially weaker than his season ERA.
6. Home field and better late-game depth favor Los Angeles.

Why not stronger:
- Dodgers' current offense is only about 3.6 R/G over the freshest L10.
- McGreevy threw six scoreless against Los Angeles in May.
- Lauer owns a 4.78 official ERA and a 4.73 last-five ERA, keeping St. Louis' outright branch live.

## O. Frozen user-facing forecast

### Verified event
St. Louis Cardinals @ Los Angeles Dodgers, MLB, **Tuesday Sep. 1 at 7:10 PM PDT**, which is **Wednesday Sep. 2 at 12:10 PM AEST**, at Dodger Stadium.

Official MLB probable pitchers:
- **Michael McGreevy (STL): 5-9, 3.86 ERA, 98 K**
- **Eric Lauer (LAD): 8-6, 4.78 ERA, 70 K**

The event was still scheduled with no recorded plays at the frozen cutoff.

### Best four supplied picks
1. **Cardinals +1.5 — LEAN**
2. **Under 9.0 — SLIGHT LEAN**
3. **Dodgers -1.5 — lower-confidence separation side**
4. **Over 9.0 — weaker total direction**

### Why Cardinals +1.5 is #1 even though Dodgers are the likely winner
The +1.5 cushion captures every Cardinals outright win and every one-run Dodgers win.

Los Angeles is the better team, but its current offense has cooled to roughly 3.6 R/G over the freshest L10 and around 4.0 R/G over the freshest L15. McGreevy also already threw six scoreless innings against this Dodgers club in May.

The main reason not to overrate that H2H is current form: McGreevy has a roughly 5.13 ERA over his last five starts and allowed seven earned runs last time out. Still, a 4-3 or 5-4 Dodgers win remains very plausible and lands Cardinals +1.5.

### Why Under 9.0 is #2
Nine provides push protection.

The most ordinary central scores include 5-3, 6-2, 5-4 and 6-3. Two of those are Under and the latter two push.

The Under is helped by Los Angeles' current offensive slowdown and ordinary clear weather. It is hurt by the fact that both starters have last-five ERAs near or above 4.7 and the Cardinals bullpen has a 6.10 ERA over the last 15 days.

That makes Under a **slight lean**, not a high-confidence total.

### Why Dodgers -1.5 is #3
The separation path is real:
- Los Angeles is 82-55;
- St. Louis has lost seven of nine;
- the Cardinals relief corps has been poor;
- Will Smith returns to deepen an already elite-name lineup.

A 6-2, 7-3 or 7-2 Dodgers win is ordinary.

But the run line is much harder than the winner call. Current public pricing also makes Cardinals +1.5 substantially shorter than Dodgers -1.5, reinforcing the structural difference.

### Likely winner
**Los Angeles Dodgers — LEAN.**

This is not a fifth independent pick.

### Weather / lineup / settlement boundary
NWS calls for a clear evening with light 5-10 mph winds and no meaningful rain threat.

MLB's official lineup page still showed TBD at the frozen cutoff; a current CBS game page had both complete batting orders, so those are treated as secondary rather than official field-owner confirmation.

No operator or user odds were supplied. Listed-pitcher/action, shortened-game and extra-inning sportsbook terms therefore remain `UNKNOWN_DEFINITION`.

No calibrated probability, expected value, market edge, ROI or staking recommendation is published.

## P. Append confirmation

- Complete frozen P-248 forecast appended before delivery: **YES**
- Frozen cutoff before scheduled first pitch: **YES**
- Drive modified: **NO**
- Prior forecast rewritten: **NO**
- Retrospective performed: **NO**
- Learning register changed: **NO**


---

# Settlement and retrospective cleanup — 2026-09-02 18:32 AEST

**Status:** APPEND-ONLY CLEANUP / EXPLICIT RETROSPECTIVE REQUEST  
**Drive mode:** READ-ONLY  
**Probability/value state:** unchanged — `NOT_GENERATED / NOT PUBLISHED`; `NO VALUE DETERMINABLE`  
**Frozen forecasts rewritten:** NO  
**Retrospectives authorised by user:** YES  
**Primary settlement sources:** MLB official Gameday/Film Room/club recaps; ATP/US Open/WTA/Tennis.com official/current match pages for tennis.

## 1. Current event-status sweep — P-239 onward

| ID | Event | Current status | Settlement action |
|---|---|---|---|
| P-239 | Athletics @ Texas Rangers | FINAL — TEX 8, ATH 5 | SETTLED + RETROSPECTIVE |
| P-240 | Chicago White Sox @ Houston Astros | FINAL — CWS 5, HOU 1 | SETTLED + RETROSPECTIVE |
| P-241 | Zachary Svajda vs Daniel Altmaier | UPCOMING / NOT STARTED | LEAVE OPEN |
| P-242 | Fabian Marozsan vs Michael Zheng | UPCOMING / NOT STARTED | LEAVE OPEN |
| P-243 | Magda Linette vs Francesca Jones | SUSPENDED — Jones leads first set 6-4; second set not completed | LEAVE OPEN; NO RETROSPECTIVE |
| P-244 | Baltimore Orioles @ Colorado Rockies | FINAL — COL 4, BAL 2 | SETTLED + RETROSPECTIVE |
| P-245 | Alexander Zverev vs Lorenzo Sonego | FINAL — Zverev won 6-4, 3-6, 6-7(7), 7-5, 6-4 | SETTLED + RETROSPECTIVE |
| P-246 | New York Yankees @ Los Angeles Angels | FINAL — NYY 7, LAA 3 | ADMINISTRATIVELY CLOSED — NO FORECAST HAD BEEN ISSUED |
| P-247 | Philadelphia Phillies @ Arizona Diamondbacks | FINAL — PHI 7, AZ 1 | SETTLED + **DEEP RANK-1 RETROSPECTIVE** |
| P-248 | St. Louis Cardinals @ Los Angeles Dodgers | FINAL — STL 13, LAD 8 | SETTLED + RETROSPECTIVE |

## 2. Contract settlement tables

### P-239 — Athletics @ Texas Rangers — Final: TEX 8, ATH 5

| Contract ID | Rank | Frozen selection | Official settled value | Outcome |
|---|---:|---|---:|---|
| P-239-C03 | 1 | Over 7.5 | 13 total runs | **WIN** |
| P-239-C02 | 2 | Texas -1.5 | Texas won by 3 | **WIN** |
| P-239-C01 | 3 | Athletics +1.5 | Athletics lost by 3 | LOSS |
| P-239-C04 | 4 | Under 7.5 | 13 total runs | LOSS |

**Potential winner:** Texas Rangers — **WIN**

#### Retrospective
| Forecast expectation | Actual driver | What was right | What was wrong / omitted | Knowability / lesson link | Process grade |
|---|---|---|---|---|---|
| Oakland bullpen-game exposure would create Texas scoring; Gore could still allow an Athletics contribution, producing an Over/Texas-separation family. | Texas scored 8; Brandon Nimmo had four hits and five RBIs. Oakland still scored 5 and rallied late. | The component budget was correct: Texas had a large scoring branch and Oakland did contribute enough to make the total clear comfortably. The top two ranks both won. | The forecast did not identify the specific Nimmo concentration, but that is normal player-level variance rather than a process miss. | Reinforces L-047 component-budget coherence and SFA-BASEBALL exposure-chain logic: short/opener games must be evaluated through the full relief chain, not the opener ERA alone. | **COMPLIANT / MECHANISM ALIGNED** |

**Learning note:** no new general rule is promoted. This is a positive example of correctly separating the Texas run component from Oakland's own scoring contribution.

---

### P-240 — Chicago White Sox @ Houston Astros — Final: CWS 5, HOU 1

| Contract ID | Rank | Frozen selection | Official settled value | Outcome |
|---|---:|---|---:|---|
| P-240-C01 | 1 | White Sox +1.5 | White Sox won by 4 | **WIN** |
| P-240-C02 | 2 | Astros +1.5 | Astros lost by 4 | LOSS |
| P-240-C03 | 3 | Over 8.5 | 6 total runs | LOSS |
| P-240-C04 | 4 | Under 8.5 | 6 total runs | **WIN** |

**Potential winner:** Chicago White Sox — **WIN**

#### Retrospective
| Forecast expectation | Actual driver | What was right | What was wrong / omitted | Knowability / lesson link | Process grade |
|---|---|---|---|---|---|
| Chicago had the stronger starter/current-regime and relief-state path; Blanco's post-surgery uncertainty could add scoring volatility. | Sean Burke threw 5 2/3 scoreless innings; Blanco himself threw four scoreless, then Houston's relief chain allowed all five Chicago runs. Houston managed only three hits and one run. | Rank #1 and winner were correct. The forecast correctly identified Houston's broader bullpen strain and Chicago's ability to win the matchup. | The total branch was mislocated: Blanco's poor season/rehab data were given too much weight relative to Burke's current run-prevention form and the possibility that Blanco could survive a short start before the bullpen failed only on one side. | Reinforces L-052 current-regime windows and SFA-BASEBALL's starter-vs-relief transition rule. A bad full-season starter ERA should not automatically widen **both** teams' scoring distributions. | **MIXED — SIDE COMPLIANT; TOTAL CALIBRATION DEFECT** |

**Local candidate learning — `C-P240-BB-STARTER-RELIEF-ASymmetry`:** when the weaker starter is expected to have a short leash, distinguish "opponent team-total upside" from "full-game Over." A one-sided relief failure can produce a comfortable side win while the total remains Under.

---

### P-244 — Baltimore Orioles @ Colorado Rockies — Final: COL 4, BAL 2

| Contract ID | Rank | Frozen selection | Official settled value | Outcome |
|---|---:|---|---:|---|
| P-244-C02 | 1 | Rockies +1.5 | Rockies won outright | **WIN** |
| P-244-C03 | 2 | Over 11.0 | 6 total runs | LOSS |
| P-244-C01 | 3 | Orioles -1.5 | Orioles lost outright | LOSS |
| P-244-C04 | 4 | Under 11.0 | 6 total runs | **WIN** |

**Potential winner:** Baltimore Orioles — LOSS

#### Retrospective
| Forecast expectation | Actual driver | What was right | What was wrong / omitted | Knowability / lesson link | Process grade |
|---|---|---|---|---|---|
| Rockies +1.5 was structurally more robust than Orioles -1.5 despite a Baltimore winner lean; the total sat inside a wide Coors corridor. | Colorado led 2-0 early, Baltimore tied it 2-2, then TJ Rumfield hit a two-run seventh-inning homer; Colorado won 4-2. | Rank #1 correctly separated **handicap likelihood** from winner probability. The forecast explicitly retained a Rockies-control kill path rather than treating Baltimore's team-strength edge as decisive. | Over 11 was too high in rank. The forecast over-weighted the generic Coors/Hughes upper tail and under-weighted Baltimore's inability to convert offense plus the possibility of a controlled Colorado bullpen game. The winner lean was also too reputation/team-strength anchored. | Strongly reinforces L-055 slate geometry and L-053 base-rate anchoring. Also reinforces L-047: a high total must be built from plausible component budgets; Coors alone cannot manufacture the missing Baltimore/Colorado runs. | **MIXED — RANK #1 COMPLIANT; WINNER/TOTAL CALIBRATION DEFECT** |

**Learning note:** no new general rule needed. Existing "venue is context, not direction" and component-budget controls were sufficient; execution should have given them more weight.

---

### P-245 — Alexander Zverev vs Lorenzo Sonego — Final: Zverev 6-4, 3-6, 6-7(7), 7-5, 6-4

**Final total games:** 54  
**Final net game margin:** Zverev +2

| Contract ID | Rank | Frozen selection | Official settled value | Outcome |
|---|---:|---|---:|---|
| P-245-C01 | 1 | Sonego +6.5 games | Sonego lost by only 2 net games | **WIN** |
| P-245-C04 | 2 | Under 33.5 games | 54 games | LOSS |
| P-245-C02 | 3 | Zverev -6.5 games | Zverev +2 games | LOSS |
| P-245-C03 | 4 | Over 33.5 games | 54 games | **WIN** |

**Potential winner:** Alexander Zverev — **WIN**

#### Retrospective
| Forecast expectation | Actual driver | What was right | What was wrong / omitted | Knowability / lesson link | Process grade |
|---|---|---|---|---|---|
| Zverev should win, but Sonego's serve/H2H margin history made +6.5 more robust; three sets were still assigned the central set-count branch. | Sonego pushed Zverev to five sets and was two points from victory in the fourth. Zverev finally won after nearly five hours, +2 net games. | Rank #1 and winner were both exactly aligned with the result. The key distinction "winner confidence > handicap separation confidence" was correct. | The **Under #2 was internally too aggressive**. The same evidence used to rank Sonego +6.5 first—close sets, H2H margin resistance, tiebreak exposure—also increased four/five-set extension risk. The set-count mixture (3 sets 5/5; 5 sets 1/5) understated the long-match branch. | Directly links to SFA-TENNIS cross-market coherence and the best-of-five set-count rule; also L-047-style target coherence. | **MIXED — SIDE/WINNER STRONG; TOTAL SET-COUNT CALIBRATION DEFECT** |

**Local candidate learning — `C-P245-TEN-CUSHION-TOTAL-COHERENCE`:** in best-of-five, if an underdog +large-game cushion is Rank #1 because repeated close-set/tiebreak resistance is decision-driving, the Under cannot also rank near the top without an explicit high-mass straight-set mechanism that is stronger than that resistance evidence. Do not promote; test prospectively.

---

### P-246 — New York Yankees @ Los Angeles Angels — Final: NYY 7, LAA 3

**Forecast status:** `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`

No ranked contracts were issued, so there is **nothing to settle as a prediction**.

#### Process review
- The state gate was correct: the request arrived at/after first pitch and available feeds disagreed.
- The research-only pregame note leaned Yankees outright; New York ultimately won 7-3, but that is **not counted as a forecast win**.
- This is a positive application of **L-046 start-state invariant**: refusing to backdate a card is more important than retrospectively claiming a correct side.

**Process grade:** **COMPLIANT — NO FORECAST / NO PERFORMANCE COUNT**

---

### P-247 — Philadelphia Phillies @ Arizona Diamondbacks — Final: PHI 7, AZ 1

| Contract ID | Rank | Frozen selection | Official settled value | Outcome |
|---|---:|---|---:|---|
| P-247-C02 | 1 | Diamondbacks +1.5 | Arizona lost by 6 | **LOSS** |
| P-247-C01 | 2 | Phillies ML | Philadelphia won | **WIN** |
| P-247-C04 | 3 | Under 7.5 | 8 total runs | LOSS |
| P-247-C03 | 4 | Over 7.5 | 8 total runs | **WIN** |

**Potential winner:** Philadelphia Phillies — **WIN**

## DEEP RANK-1 RETROSPECTIVE

### What actually happened
Philadelphia scored two runs in the first inning, Luzardo held Arizona to one run over 6 2/3 innings, and the Phillies turned a 3-1 game into a 7-1 separation game with four late runs in the eighth and ninth. Eduardo Rodríguez allowed three earned runs in five innings; Arizona's bullpen then allowed the margin to expand.

### Why Rank #1 failed
The forecast's top-ranked Diamondbacks +1.5 argument relied on three things:
1. Rodríguez's strong current form;
2. the positive +1.5 cushion;
3. four prior 2026 meetings that had all been one-run games.

Those inputs were real, but the ranking **over-concentrated on close-game evidence** and did not give enough weight to the favorite-separation channel:
- Philadelphia entered on a five-game winning streak and 14-2 stretch;
- the Phillies' current offense was around 5.2 R/G over L10;
- the forecast already identified Arizona bullpen workload/late-game exposure;
- the score-tree contained a Philadelphia high-separation branch, but it was declared subordinate without enough evidence.

The result exposed exactly that branch: Philadelphia was already ahead after the first inning, Luzardo suppressed Arizona, and the Diamondbacks' relief chain allowed the margin to widen late.

### What was right
- Phillies ML at Rank #2 won.
- The potential winner (Philadelphia) won.
- Over 7.5 at Rank #4 won exactly because the late separation created an eighth total run.
- The pregame analysis correctly recognized Luzardo, Philadelphia form and bullpen exposure as real advantages.

### What was wrong / process defect
The error was **ranking/calibration**, not absence of the correct mechanism.

**Defect classes:**
- `CALIBRATION / RANKING`
- `MATCHUP_CONTEXT`
- `RELIEF_TRANSITION`
- `H2H_CONTINUITY OVERWEIGHT`

The four one-run H2Hs were treated too strongly relative to current-team and bullpen-state evidence. L-052's H2H continuity gate explicitly says nested/small historical samples are descriptive; they should not outrank a strong current-state separation mechanism. L-053 also requires the base-rate anchor and event adjustment to remain bounded rather than letting one recent geometry pattern dominate.

### Strongest missed kill path
**PHI early lead + Luzardo suppression + Arizona bullpen separation.**

This was knowable before issue:
- Luzardo's current form was verified.
- Philadelphia's form/offense was verified.
- Arizona's bullpen usage was known.
- The lineup quality differential was known.

The miss was not that this path was invisible; it was that it was not weighted heavily enough when choosing Rank #1.

### How the process should improve
1. **Positive-cushion Rank #1 separation gate:** before ranking an underdog +1.5 first against a materially stronger favorite, explicitly test the favorite's **late separation probability** through starter + bullpen + lineup components.
2. **H2H cap:** a run of one-run H2Hs cannot itself lift the dog cushion above the favorite's winner/side evidence unless current starter, bullpen and lineup states support the same close-game mechanism.
3. **Bullpen margin budget:** for full-game run lines, model the expected score **after the starter exits** separately from the starter score. Run-line separation is often created after the sixth inning.
4. **Winner/handicap coherence:** if the favorite is the likely winner and the dog cushion is Rank #1, the analysis must show why most favorite-win branches are specifically one-run rather than two-plus.

**Process grade:** **PROCESS_DEFECT — RANK #1 CALIBRATION / MATCHUP_CONTEXT / RELIEF_TRANSITION**

**Local candidate learning — `C-P247-BB-CUSHION-SEPARATION-GATE`:** a +1.5 underdog cannot become Rank #1 primarily from historical close-game geometry when the favorite has a materially stronger current offense and a late separation advantage. Require an explicit post-starter margin budget. Candidate only; no promoted weight.

---

### P-248 — St. Louis Cardinals @ Los Angeles Dodgers — Final: STL 13, LAD 8

| Contract ID | Rank | Frozen selection | Official settled value | Outcome |
|---|---:|---|---:|---|
| P-248-C02 | 1 | Cardinals +1.5 | Cardinals won outright by 5 | **WIN** |
| P-248-C04 | 2 | Under 9.0 | 21 total runs | LOSS |
| P-248-C01 | 3 | Dodgers -1.5 | Dodgers lost outright | LOSS |
| P-248-C03 | 4 | Over 9.0 | 21 total runs | **WIN** |

**Potential winner:** Los Angeles Dodgers — LOSS

#### Retrospective
| Forecast expectation | Actual driver | What was right | What was wrong / omitted | Knowability / lesson link | Process grade |
|---|---|---|---|---|---|
| Cardinals +1.5 was more robust than Dodgers -1.5; Dodgers still had the stronger winner case; Under 9 had a small edge because LAD scoring had cooled and 9 offered push protection. | St. Louis scored 13 runs, hit **five home runs**, and won 13-8. Lauer was hit hard immediately; St. Louis led 7-0 in the third and 9-3 in the fourth. | Rank #1 won strongly. The forecast correctly kept a Cardinals outright-win branch alive and correctly identified Lauer's volatility and the possibility that the Dodgers run line was much harder than the winner call. | The total/winner hierarchy was poor. Both starters had last-five ERAs around 4.7-5.1 and the Cardinals offense had a 4.8 R/G L10, yet Under was ranked #2. The analysis over-weighted the Dodgers' recent scoring slowdown and underweighted the possibility that **St. Louis itself** could be the high-scoring side. | Links to L-048 opposite-sign mechanism decomposition and SFA-BASEBALL two-team component budget. A total must model each team's upper tail independently rather than assuming the favorite supplies most Over risk. | **MIXED — RANK #1 WIN; TOTAL/WINNER PROCESS DEFECT** |

**Local candidate learning — `C-P248-BB-UNDERDOG-OFFENSE-TOTAL`:** when an underdog cushion is ranked highly because an outright upset branch is credible, the total model must explicitly include the underdog's high-run component. If both starters are currently volatile, a low-total ranking needs stronger suppression evidence than "favorite offense recently cooled."

---

## 3. Rank-1 accountability summary

| ID | Rank #1 | Outcome | Deep review required? | Main conclusion |
|---|---|---|---|---|
| P-239 | Over 7.5 | WIN | No | Component-budget / bullpen-game thesis aligned |
| P-240 | White Sox +1.5 | WIN | No | Side right; total mechanism over-weighted Blanco weakness |
| P-244 | Rockies +1.5 | WIN | No | Cushion logic right; winner/Over too favorite/venue anchored |
| P-245 | Sonego +6.5 | WIN | No | Cushion/winner distinction excellent; set-count Under miscalibrated |
| P-246 | No forecast | N/A | No | Start-state refusal was correct |
| **P-247** | **Diamondbacks +1.5** | **LOSS** | **YES** | H2H/close-game geometry over-weighted; late PHI separation underweighted |
| P-248 | Cardinals +1.5 | WIN | No | Rank #1 right; Under/winner incoherent with underdog offensive upside |

**Settled Rank #1 record for issued P-239/P-240/P-244/P-245/P-247/P-248 cards:** **5-1**.  
This is a descriptive six-event sample only; it is **not** model validation, calibration, edge or ROI evidence.

## 4. Cross-event learning synthesis

### What worked
1. **Positive-cushion vs winner separation:** P-244, P-245 and P-248 show why the likelier match/game winner need not be the most likely derivative contract. This reinforces L-055 and sport-specific coherence rules.
2. **Component-budget thinking:** P-239 correctly combined a Texas scoring ceiling with a non-zero Athletics scoring component.
3. **Start-state discipline:** P-246 correctly refused to create a stale forecast after first pitch.
4. **Explicit kill paths:** even where rankings were wrong, several losing mechanisms were already disclosed. The main issue was weighting/ranking rather than hidden information.

### What needs improvement
1. **Cross-market coherence:** P-245 and P-248 show that a top cushion pick and a high-ranked Under can conflict when the cushion is supported by close/extended or underdog-upset states.
2. **Late separation modeling:** P-247 shows that full-game run-line cushions require a separate bullpen/post-starter margin budget.
3. **Current-regime weighting:** P-240 shows that poor full-season/rehab starter numbers cannot outrank a strong current opponent starter profile when evaluating totals.
4. **Venue/reputation restraint:** P-244 shows that Coors and team-quality reputation should not push the total/winner beyond the actual component evidence.

### Local candidate learnings added
These are **candidate process observations only**, not promoted weights:
- `C-P240-BB-STARTER-RELIEF-ASymmetry`
- `C-P245-TEN-CUSHION-TOTAL-COHERENCE`
- `C-P247-BB-CUSHION-SEPARATION-GATE`
- `C-P248-BB-UNDERDOG-OFFENSE-TOTAL`

No framework promotion is claimed. Any promotion still requires the active `LEARNING_REGISTER.md` prospective procedure.

## 5. Current open queue — new local events

| ID | Current status | Action |
|---|---|---|
| P-241 | Svajda vs Altmaier — UPCOMING / NOT STARTED | Keep open |
| P-242 | Marozsan vs Michael Zheng — UPCOMING / NOT STARTED | Keep open |
| P-243 | Linette vs Jones — SUSPENDED; Jones won first set 6-4 | Keep open; do not settle until official final |

## 6. Inherited canonical unresolved queue — recheck result

The inherited top-snapshot queue remains open because the missing items are **field ownership or operator definitions**, not merely final scores.

| Queue item | Current status after recheck | Why it remains open |
|---|---|---|
| P-126 | UNRESOLVED / CONFLICTED | Exact SFA field-owner result/phase and C06 corners ownership still not recovered |
| P-148-C02 | PROVISIONAL LOSS | Exact named provider/field-owner corner definition remains unproved |
| P-149-C02 | PROVISIONAL WIN | MLS NEXT Pro official club/league pages did not expose a controlling corner field in the current search |
| P-151-C02 | STRONG PROVISIONAL WIN | Named provider/field-owner corner definition still missing |
| P-166 | OPERATOR DEFINITION UNRESOLVED | Unnamed operator OT/action rule cannot be reconstructed from the official final |
| P-176-C05 | PROVISIONAL WIN under canonical top snapshot | Named provider-owner corner confirmation still absent; DATA_SOURCE_REGISTER wording remains internally inconsistent with the canonical snapshot |
| P-178-C05 | UNRESOLVED | No controlling field-owner corner record recovered |
| P-179-C05 | PROVISIONAL WIN | Specialist result exists; provider-owner confirmation still missing |
| P-200 | OPERATOR DEFINITION UNRESOLVED | Regulation/OT/SO/action terms of unnamed operator remain unknowable |
| P-217-C01/C02 | UNRESOLVED | Reduced-overs/DLS/action rule of unnamed operator remains unknowable |

### P-233/P-234/P-235 provisional watchlist
Targeted re-search of the CFA site still recovered the official **quarterfinal schedule / pre-quarterfinal coverage**, not a current field-owner results article for these three matches. Specialist pages now show results (for example Dalian Yingbo 1-0 Shanghai Shenhua), but the canonical issue was **field ownership**, so the three remain provisional rather than being silently upgraded.

## 7. Settled vs not-yet-settled list — from the first new event in this mini log

### Settled / closed
- **P-239** — Athletics @ Texas Rangers — FINAL / SETTLED
- **P-240** — White Sox @ Astros — FINAL / SETTLED
- **P-244** — Orioles @ Rockies — FINAL / SETTLED
- **P-245** — Zverev vs Sonego — FINAL / SETTLED
- **P-246** — Yankees @ Angels — FINAL / CLOSED, NO ACTIONABLE FORECAST
- **P-247** — Phillies @ Diamondbacks — FINAL / SETTLED
- **P-248** — Cardinals @ Dodgers — FINAL / SETTLED

### Not yet settled
- **P-241** — Svajda vs Altmaier — UPCOMING
- **P-242** — Marozsan vs Michael Zheng — UPCOMING
- **P-243** — Linette vs Jones — SUSPENDED

## 8. Source-quality review

### Preferred settlement sources used
1. **MLB Gameday / MLB Film Room / MLB club recaps** for official baseball finals, inning path and pitcher lines.
2. **US Open / ATP official pages** for Zverev-Sonego final and match narrative.
3. **WTA official match page** for Linette-Jones suspended status.
4. Tennis.com used only as a current state cross-check where official event pages were incomplete.

### Improvements over weaker research lanes
- Do not use a search-engine scoreboard snippet when an official game story/film-room final is available.
- Do not use specialist corner totals to upgrade a provisional soccer settlement unless the exact field owner/provider is established.
- Do not infer operator action, OT/SO or DLS rules from league rules; operator contract language owns those fields.
- For tennis, official event/tour result pages control final set scores; market or preview pages are not settlement sources.

## 9. Cleanup verification

- [x] Every P-239–P-248 event was state-checked.
- [x] Final events were settled.
- [x] P-241/P-242 were left open because they had not started.
- [x] P-243 was left open because it is suspended.
- [x] Rank #1 failure P-247 received a deep retrospective.
- [x] What went right and wrong was recorded for every settled issued forecast.
- [x] Candidate learnings were added locally without falsely promoting them.
- [x] Frozen pregame/live-start forecasts were not rewritten.
- [x] Historical inherited queue was rechecked and not falsely closed where operator/provider ownership remains unknowable.
- [x] Google Drive was not modified.

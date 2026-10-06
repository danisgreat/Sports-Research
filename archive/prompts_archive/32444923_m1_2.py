# Comprehensive settlement of current running log + full retrospective


Your task is to:

1. inspect **every record in the CURRENT active mini running/reference log**;
2. determine which events have genuinely reached a terminal state;
3. comprehensively research and settle every contract that can be settled correctly;
4. perform the **full current-framework retrospective** for every genuinely completed event;
5. update the existing mini running log carefully;
6. append settlement/retrospective material against the **correct existing canonical ID**;
7. preserve every genuinely unresolved record;
8. run the current repository verification workflow;
9. **do not archive the mini log and do not start a new mini log in this task.**

Accuracy, source quality, provenance, canonical custody, correct contract semantics and current repository methodology take priority over speed.

---

# 0. Hard invariants

These rules override any ambiguity elsewhere in this prompt.

### Canonical-ID invariant

Every event must retain an explicit:

```text
Canonical ID:
Canonical status:
Tracking handle:
Canonical destination:
```

Settlement must attach to the event's **existing canonical identity**.

Do **not** allocate a new P-number merely because an event is now being settled.

Do **not** renumber an event.

Do **not** replace a canonical ID with a TMP/local handle.

If an event already exists canonically, settle/add the retrospective against that existing P-ID.

### Original-forecast immutability

Never rewrite the original prediction after seeing the outcome.

The following are immutable:

- supplied contracts;
- contract lines;
- periods/endpoints;
- ranks;
- probabilities;
- `p_model`;
- `p_card`;
- baseline literals;
- historical q values;
- potential winner;
- original rationale;
- assumptions;
- injury/lineup state at research time;
- original timestamp/cutoff;
- original event state;
- original source statements.

Any correction must be an **append-only dated correction/addendum**.

### Sporting result is not automatically certified settlement

Keep these concepts separate:

1. **Event terminality** — whether the game actually ended.
2. **Sporting result** — what happened on the field/court/track.
3. **Contract grade** — whether the exact original proposition won/lost/pushed/voided.
4. **Formal/operator settlement** — whether the exact operator rules are known.
5. **Performance certification** — whether the repository's source, timing, independence and custody requirements are satisfied.

A game can have a confidently known final score while its formal operator settlement or performance certification remains unresolved.

Never collapse those distinctions.

---

# 1. Mandatory fresh-read current authority

Before doing **any** settlement, retrospective, grading or repository modification, read the CURRENT versions of at least:

- `METHOD.md`
- `CURRENT_RULES.md`
- `CARD_AND_LOG_TEMPLATES.md`
- `SCORING_AND_VALIDATION.md`
- `SOURCES.md`
- `RECORD_ELIGIBILITY_SCHEMA.md`
- `VERIFICATION_PROTOCOL.md`
- `GAME_LOG_STATUS_CURRENT.md`
- `research/README.md`
- active `prediction logs/PREDICTION_LOG_COMBINED_6.md`
- `research/canonical_ledger.jsonl` or current canonical-ledger equivalent
- applicable settlement code/workflow, including current equivalents of:
  - `research/src/settle.py`
  - settlement/revision operations;
- relevant `RULES_<SPORT>.md` for **every sport being settled**;
- competition/league-specific settlement rules;
- the CURRENT active mini running/reference log;
- the immediately preceding archive/carryover source if referenced;
- current reconciliation/closure/implementation files referenced by `METHOD.md` or `CURRENT_RULES.md`;
- the currently selected control/freeze manifest.

Use `METHOD.md` and `CURRENT_RULES.md` as current authority.

Do not let historical sections farther down a current file override its current controlling section.

If current repository documentation says local working files are authoritative while GitHub is only a publication copy, disclose that limitation. Do not pretend GitHub proves local state that you cannot access.

---

# 2. Canonical custody gate before settlement

Before settlement work:

1. inspect the canonical ledger;
2. identify the last committed record;
3. identify any pending/prepared transaction;
4. recover interrupted transactions where the current workflow permits;
5. verify Part 6 projections and retained-source custody;
6. identify the current next canonical ID;
7. verify every mini-log event's claimed canonical ID against repository custody.

Use the current equivalents of:

```text
py -3.14 -B -m research.operations.log_card recover
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.log_card next-id
```

### Important

The current next canonical ID is recorded only for custody verification.

**Do not consume it for settlement.**

Settlement against P-538 does not create P-539.

A settlement revision/addendum belongs to **P-538 itself**.

---

# 3. Resolve canonical identity for every mini-log record

Inspect every record in the active mini log.

Create an internal reconciliation table containing:

```text
Canonical ID
Canonical status
Tracking handle
Event
Sport
Competition
Original event key
Native event ID
Original research timestamp
Scheduled start
Observed state at original research
Current settlement state
Canonical Part 6 pointer
Projection/source pointer
```

Verify that each event is represented exactly once as an event, allowing dated addenda without treating them as new games.

### Existing canonical event

Use:

```text
Canonical ID: P-###
Canonical status: EXISTING_CANONICAL
```

or the repository's exact equivalent.

### Previously committed research card

Use its actual committed P-ID.

### Uncommitted/write-blocked mini record

If the mini contains something such as:

```text
Canonical ID: P-538
Canonical status: WRITE_BLOCKED_UNCOMMITTED
```

do **not** automatically treat P-538 as permanently owned by that event.

Fresh-read the ledger.

If the original research card can now be canonically retained under the current repository workflow, follow the current repository rules for importing/committing that **existing original forecast evidence without backdating it or rewriting it**.

Then settle against the ID actually returned/committed.

If canonicalization remains impossible:

- preserve the record;
- preserve its original research;
- perform only the diagnostic sporting settlement supported by evidence;
- mark canonical custody unresolved;
- do not claim a permanent canonical assignment that repository readback does not support.

---

# 4. Determine which events are genuinely terminal

Inspect **every active record**.

For each event verify:

- exact participants;
- sport;
- competition;
- season;
- round/stage;
- home/away designation;
- venue;
- native/event ID where recoverable;
- scheduled start;
- actual start where authoritative evidence exists;
- period/innings/sets/quarters completed;
- regulation vs overtime/extras;
- settlement endpoint;
- official terminal state.

Do not infer `FINAL` simply because enough time has elapsed.

Distinguish correctly between:

```text
FINAL
OFFICIAL_FINAL
CANCELLED
POSTPONED
ABANDONED
SUSPENDED
VOID
NO_CONTEST
WALKOVER
RETIRED
UNRESOLVED
IN_PROGRESS
DELAYED
```

and the exact sport-specific equivalents.

If an event has not reached the endpoint required by the original contract, leave the relevant contract unresolved.

---

# 5. Terminal evidence hierarchy

Follow the CURRENT `SOURCES.md`, applicable sport rules and terminal-admission requirements.

Prefer:

1. field owner / league / governing body;
2. official competition/team source where appropriate;
3. high-quality independent statistical/result source;
4. secondary reporting only where needed and clearly labelled.

Search broadly enough to identify contradictions rather than stopping at the first plausible final score.

For each terminal source used, retain/report where available:

```text
Source/provider
Exact URL/endpoint
Native/event ID
Retrieval timestamp
Source-published timestamp
Terminal state
Final score/result
Regulation result
OT/extras result
Period/quarter/inning/set result
Relevant derivative statistic
Raw result literal
Response/body hash
Repository source receipt
Parser version
Source-registry identity
Official/field-owner status
Collection lineage
Independence status
```

### Independence rule

Three websites using one upstream data provider are **one lineage**, not three.

Do not infer collection independence from different domains.

Use:

```text
INDEPENDENT_ESTABLISHED
SHARED_LINEAGE
UNKNOWN_INDEPENDENCE
```

or the current repository's exact terminology.

---

# 6. Separate diagnostic settlement from certified settlement

For every completed event make an explicit settlement-status determination.

Use current repository status names where they exist.

Conceptually distinguish:

### A. Fully supported formal/certified settlement

Only when all required:

- event identity;
- terminal result;
- actual-start evidence;
- endpoint;
- contract definition;
- period definition;
- operator semantics;
- source quorum;
- source independence;
- custody requirements

are satisfied.

### B. Diagnostic sporting settlement

Use when the sporting outcome is adequately established but one or more certification requirements remain unavailable.

For example:

```text
SPORTING_OUTCOME_KNOWN
DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED
UNKNOWN_DEFINITION
PERFORMANCE_INELIGIBLE
```

as appropriate under current repository terminology.

### C. Unresolved

If a material field remains ambiguous, preserve it as unresolved.

Do not force a binary answer.

Examples:

```text
UNRESOLVED_RESULT
UNRESOLVED_PERIOD
UNRESOLVED_ENDPOINT
UNRESOLVED_OPERATOR_DEFINITION
UNRESOLVED_PROVIDER_FIELD
UNRESOLVED_IDENTITY
UNRESOLVED_SOURCE_LINEAGE
```

Use current repository literals where defined.

---

# 7. Preserve the original forecast exactly

Read the original card from canonical custody or retained original mini evidence.

Do not reconstruct it from memory or prior-chat summaries.

Capture the literal original:

- canonical ID;
- tracking alias;
- event key;
- contracts;
- ranks;
- probabilities;
- baseline;
- q where historical;
- winner call;
- issue/research state;
- timestamp;
- lineup/participant assumptions;
- evidence limitations;
- failure/kill paths;
- sources.

Do not alter any of those because of what happened later.

If the historical card contains an obvious error, preserve it and append:

```text
DATED CORRECTION / SETTLEMENT NOTE
```

rather than rewriting the historical card.

---

# 8. Resolve exact contract semantics before grading

For every individual ranked selection establish:

```text
Sport
Market
Selection
Line
Period
Endpoint
Regulation/full-game
OT/extras included?
Tie treatment
Push treatment
Void rule
Shortened-game rule
Participant-action rule
Listed-starter/player rule
Settlement provider/field
```

The user-supplied contract wording is the immutable contract literal.

Do not silently substitute a similar market.

### Examples requiring explicit care

#### Basketball
Distinguish:

- regulation only vs including overtime;
- spread;
- moneyline;
- total;
- team total;
- player prop;
- quarter/half markets.

#### Baseball
Resolve:

- regulation vs completed game;
- extra innings;
- KBO/NPB tie rules;
- listed pitchers/action;
- shortened/suspended game rules;
- whole-run push lines.

#### Hockey
Resolve:

- regulation 3-way;
- moneyline including OT/SO;
- puck line;
- total including OT;
- goalie/player participation rules.

#### Soccer
Resolve:

- 90 minutes + stoppage only;
- extra time;
- penalties;
- Asian handicap;
- corners/cards provider semantics;
- first-half/second-half fields.

#### Tennis
Resolve:

- retirement/walkover;
- completed sets;
- game/set handicap;
- match winner;
- operator retirement rules if required.

If operator rules were never retained and materially affect settlement:

**do not invent them.**

Grade only the sporting proposition if possible and preserve formal settlement as `UNKNOWN_DEFINITION`.

---

# 9. Grade every issued contract

Grade **every original issued/supplied contract**, not just the top two.

Allowed settlement outputs:

```text
W
L
P
VOID
UNRESOLVED
```

Use the current repository's exact deterministic settlement output where available.

Do not:

- convert pushes to losses;
- exclude losing lower-ranked rows;
- omit contradictory/complementary rows;
- change a line to make it settle cleanly;
- grade an alternate suggestion as though it were supplied;
- silently delete a duplicated row.

For every row record:

```text
Rank:
Original contract:
Original p:
Original baseline:
Settlement field/value:
Grade:
Settlement status:
Evidence:
```

If `p` or baseline was originally:

```text
NOT_ESTIMATED
```

preserve that exact fact.

Never backfill a numerical probability during settlement.

---

# 10. Potential-winner settlement

Grade the original potential-winner call separately.

Record:

```text
Original potential winner:
Winner endpoint:
Actual sporting winner:
Grade/result:
Tie/OT/extras implications:
```

Do not treat the potential-winner call as another ranked contract unless the original framework did so.

---

# 11. Deterministic settlement tooling

Where the current repository contains deterministic settlement code applicable to the exact market and endpoint, use it.

For example, current deterministic settlement logic requires:

- matching event ID;
- terminal state;
- matching endpoint;
- exact score;
- explicit void state;
- correct market/side/line.

Do not hand-grade a contract when current repository tooling can grade it deterministically.

However:

**Do not force an unsupported specialised contract into a generic settlement function.**

Examples:

- corners;
- cards;
- player props;
- period-specific specialist stats;
- custom handicap rules;
- retired-player markets.

If the current deterministic implementation does not support that contract family, verify it separately using the exact registered settlement field/provider.

---

# 12. Comprehensive scoring and diagnostic metrics

Apply the CURRENT `SCORING_AND_VALIDATION.md`.

Where literal event probabilities exist and the endpoint is valid, compute only the metrics currently permitted.

Potential examples where applicable:

- binary Brier;
- multiclass Brier;
- log loss;
- calibration residual;
- baseline comparison;
- Rank-1 result;
- Rank-2 result;
- Hit@2 / Wins@2;
- event-level scoring;
- family-level scoring.

### Hard scoring rules

- `q` is **not** an event probability.
- `NOT_ESTIMATED` remains `NOT_ESTIMATED`.
- Missing means missing, not zero.
- A push is not a loss.
- A void is not a loss.
- An unresolved result is not a loss.
- Multiple contracts from the same game are not independent samples.
- Overlapping/correlated contracts must be recognised.
- Diagnostic settlements do not become certified performance.
- Do not calculate ROI unless explicitly requested and supported by retained market/price evidence.
- Do not manufacture implied odds/prices.
- Do not claim predictive skill from a handful of retrospective events.

---

# 13. Full retrospective for EVERY completed event

Perform the same depth of retrospective for winning and losing cards.

Do not devote all analysis only to mistakes.

For each completed event append the following **12-part retrospective**.

---

## Retrospective 1 — Observed endpoint and result

Record:

- official final result;
- regulation result where relevant;
- OT/extras result;
- relevant period score/stat;
- every ranked contract grade;
- potential-winner grade;
- settlement status;
- certification status.

---

## Retrospective 2 — Expectation vs reality

Compare the original forecast with what actually occurred.

Explain:

- expected game state;
- actual game state;
- where reality stayed within an anticipated branch;
- where it departed materially;
- whether the final result was central or tail-like relative to the original reasoning.

Do not invent a probability distribution if none existed.

---

## Retrospective 3 — Original probability/baseline audit

Preserve exactly:

- `p_model`;
- `p_card`;
- baseline;
- q;
- `NOT_ESTIMATED`;
- model status.

Where probabilities genuinely existed, calculate permitted diagnostic surprise/error metrics.

Do **not** revise the original probability.

---

## Retrospective 4 — Event/source/identity audit

Review:

- participant identity;
- event ID;
- venue;
- league/stage;
- scheduled start;
- actual start;
- endpoint;
- period;
- terminal evidence;
- source-lineage quality.

Identify any source or identity mistake separately from a sporting forecast miss.

---

## Retrospective 5 — Participant/availability audit

Compare original expectations with actual participants where recoverable:

- starters;
- lineups;
- active/inactive players;
- goalkeeper;
- starting pitcher;
- minutes/restrictions;
- late scratches;
- substitution/role changes;
- rotation decisions;
- rest.

Separate strictly:

```text
KNOWN BEFORE ORIGINAL RESEARCH
KNOWN BEFORE START BUT AFTER ORIGINAL RESEARCH
ONLY KNOWN AFTER START
ONLY KNOWN POSTGAME
```

Never treat postgame knowledge as though it could have informed the original forecast.

---

## Retrospective 6 — Mechanisms that occurred

Take the original card's declared mechanisms/risk branches and determine which actually occurred.

Examples:

- pace;
- shooting efficiency;
- turnovers;
- rebounds;
- foul/FT environment;
- pitching hook;
- bullpen transition;
- special teams;
- empty net;
- red card;
- injury;
- set-piece dominance;
- serve pressure;
- weather;
- venue;
- fatigue.

Prefer measurable evidence over narrative storytelling.

---

## Retrospective 7 — Mechanisms that did NOT occur

Identify important expected mechanisms that failed to materialise.

Distinguish between:

- mechanism genuinely absent;
- mechanism present but smaller than expected;
- mechanism unknowable because required data is unavailable.

---

## Retrospective 8 — Model vs research adjustment

Where applicable separate:

```text
MODEL SIGNAL
MANUAL/QUALITATIVE RESEARCH ADJUSTMENT
LINEUP/AVAILABILITY ADJUSTMENT
NO NUMERICAL MODEL
```

Determine diagnostically whether the adjustment moved the prediction in a helpful or harmful direction.

Do not derive a new coefficient from one game.

---

## Retrospective 9 — Failure-path / success-path analysis

For every losing ranked selection:

- identify the exact mechanism/path that defeated it;
- state whether that path was identified pregame;
- state whether its importance was underestimated or genuinely random.

For every winning selection:

- determine whether it won for the reason predicted;
- distinguish a well-reasoned win from a lucky/outlier win.

A winning prediction with incorrect mechanism is **not** automatically strong evidence for the method.

A losing prediction where the correct central mechanism occurred but variance dominated is **not** automatically a modelling defect.

---

## Retrospective 10 — Error classification

Classify each material issue under current-framework categories such as:

```text
DATA / SOURCE / IDENTITY
CONTRACT / ENDPOINT / PERIOD
TIMING
PARTICIPANT AVAILABILITY
MODEL
CALIBRATION
RESEARCH ADJUSTMENT
MECHANISM WEIGHTING
TRUE RANDOM MISS / VARIANCE
UNRESOLVED / CENSORED
NO MATERIAL ERROR IDENTIFIED
```

Use more than one category where appropriate.

Do not call every loss a model error.

---

## Retrospective 11 — Next testable hypothesis

If the event reveals something worth testing, formulate a **specific prospective hypothesis**.

It must include:

```text
Hypothesis
Target population
Feature/mechanism
Outcome/metric
Comparator
Minimum sample / cohort requirement where current framework defines one
Acceptance criterion
Rejection/futility criterion
Required source fields
```

Do not promote the hypothesis into a live rule, weight, cap or coefficient from one event.

If the current repository already has an experiment/proposal for the same mechanism, reference it rather than creating a duplicate concept.

---

## Retrospective 12 — What should NOT change

Explicitly list what this single result does **not** justify changing.

Examples:

- probability weights;
- calibration;
- ranking penalties;
- cushion penalties;
- total-direction bias;
- lineup adjustment coefficient;
- starter weighting;
- sport-wide rules;
- model family;
- source hierarchy.

This section is mandatory even for a dramatic loss or dramatic win.

---

# 14. Cross-event retrospective after individual reviews

After completing all individual retrospectives, perform a **batch-level diagnostic review**, without treating correlated observations as independent.

Include:

### Rank performance

- Rank 1 W/L/P/VOID/UNRESOLVED;
- Rank 2;
- Hit@2;
- only where mathematically valid.

### Sport/family pattern

Group cautiously by:

- sport;
- competition;
- contract family;
- model vs qualitative analysis;
- pregame vs late/live;
- calibrated vs uncalibrated.

### Error taxonomy counts

Count:

- source errors;
- identity errors;
- contract errors;
- timing errors;
- participant-state misses;
- model misses;
- research-adjustment misses;
- random misses;
- unresolved cases.

Do not infer significance from tiny samples.

### Hypothesis de-duplication

If multiple events suggest the same mechanism, consolidate them into **one prospective hypothesis** rather than creating many nearly identical rules.

Do not promote any hypothesis merely because several retrospective anecdotes point the same way.

---

# 15. Update canonical Part 6 correctly

For each canonical event:

- preserve original research bytes;
- append settlement/retrospective material;
- retain original canonical ID;
- retain tracking handle;
- retain original source/projection pointer;
- use the current repository's settlement/revision/addendum mechanism appropriate to the record class.

### Certified ISSUE record

Use the certified settlement workflow only if the current schema and evidence requirements genuinely apply.

Current repository documentation may use a workflow similar to:

```text
python -B -m research.src.workflow settle <terminal-bundle.json> --reason "Exact terminal evidence appended"
```

Use only when applicable.

### Research-only / uncalibrated card

Do **not** force a certified issuance/settlement schema onto a research-only card.

Use the repository's current append-only diagnostic/addendum mechanism.

Preserve:

```text
RESEARCH_ONLY_NOT_CERTIFIED
UNCALIBRATED_QUALITATIVE
NOT PERFORMANCE_ELIGIBLE
```

where applicable.

---

# 16. Update the CURRENT mini running log

Do **not** create a new mini log.

Do **not** archive the mini log.

Update the full current Markdown mini log.

For each event maintain its mandatory identity block:

```text
Canonical ID:
Canonical status:
Tracking handle:
Canonical destination:
Canonical pointer:
```

Then update:

```text
Event state:
Settlement state:
Formal/certification state:
Rank 1 grade:
Rank 2 grade:
All-row grades:
Potential-winner result:
Retrospective status:
Outstanding evidence:
```

### Completed and fully resolved

Move/update appropriately according to current log structure, but do not delete its audit trail.

### Sporting result known but formal settlement unresolved

Keep it visible as something equivalent to:

```text
DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED
```

and preserve exact outstanding evidence.

### Still unresolved

Keep it in the settlement-pending/carryover queue.

Do not remove it simply because it is old.

---

# 17. Canonical-ID rules during settlement

Settlement itself must **not** advance the canonical counter.

After settlement verify:

```text
Last committed canonical ID before settlement:
Last committed canonical ID after settlement:
Next canonical ID before settlement:
Next canonical ID after settlement:
```

Unless unrelated/new research was committed concurrently, these should normally remain unchanged.

If the canonical ID changes unexpectedly:

**stop and investigate before claiming settlement completion.**

Never allocate a new P-ID to:

- settlement;
- retrospective;
- correction;
- addendum;
- source update;
- terminal-evidence update.

These attach to the existing event/canonical ID unless the current repository explicitly defines otherwise.

---

# 18. Do not contaminate retrospective research with market hindsight

Maintain the repository's `SPORTS_ONLY / MARKET_BLIND` principles.

Do not use:

- closing odds;
- closing line movement;
- betting tip sites;
- prediction markets;
- sportsbook previews;
- public betting splits

to explain whether the original sporting analysis was good or bad.

If the repository explicitly permits an isolated post-event market benchmark, keep it quarantined and separate from model/research conclusions.

Do not calculate betting ROI unless I separately request it.

---

# 19. Source timing discipline

For every postgame source, distinguish:

```text
RETRIEVED_AFTER_EVENT
PUBLISHED_BEFORE_EVENT
PUBLISHED_DURING_EVENT
PUBLISHED_AFTER_EVENT
```

Retrieval today does not prove information was available pregame.

Do not use a postgame recap to claim that an injury, lineup or role change was known at original issue time unless contemporaneous evidence establishes that.

---

# 20. No survivor bias

Inspect **every active mini-log event**, not merely:

- winning cards;
- cards with easy official results;
- cards with available statistics;
- high-confidence predictions.

Events with:

- missing finals;
- source conflicts;
- ambiguous endpoints;
- ungraded derivative fields

must remain visible as unresolved/censored.

Never drop difficult events from the denominator silently.

---

# 21. Verification after settlement

After all settlement/addendum/log changes, run the CURRENT repository-prescribed checks.

At minimum use the current applicable equivalents of:

```text
py -3.14 -B -m research.operations.log_card recover
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.log_card next-id

py -3.14 -B -m research.operations.control_freeze --verify
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m research.operations.verify_reconciliation
py -3.14 -B -m research.operations.verify_all_logs

python -B -m pytest -p no:cacheprovider research/tests research/operations -q
```

Also run current applicable:

- archive validation;
- source validation;
- acceptance validation;
- workflow status;
- workflow scoring;
- experiment-measure verification;
- any settlement-specific checks prescribed by current `research/README.md` or `VERIFICATION_PROTOCOL.md`.

### Verification-reporting rule

Report **each command separately** with:

```text
Command
Exit/result
PASS / FAIL / NOT RUN
Reason
```

Do not convert partial success into a global `PASS`.

If full custody fails because current repository documentation says some bodies are local-only/not published, report:

```text
MECHANICS:
CUSTODY:
CLEAN-CHECKOUT COMPLETENESS:
SPORTING SETTLEMENT:
FORMAL CERTIFICATION:
```

separately.

---

# 22. Repository write failure

If GitHub/repository mutation fails:

1. do not claim files were updated;
2. do not claim settlement/addenda were committed;
3. read back the repository after the failed attempt;
4. preserve the completed settlement research locally/reference-side;
5. keep canonical IDs unchanged;
6. report the exact write failure;
7. do not allocate replacement IDs;
8. return/link the complete updated fallback mini log if available.

A reported `push` permission does not count as a successful write.

Only successful mutation plus readback establishes repository completion.

---

# 23. Required settlement record for every event

Each terminal event must finish with a machine-readable-looking summary block:

```text
Canonical ID:
Canonical status:
Tracking handle:
Event:
Sport/competition:
Terminal status:
Official final:
Regulation result:
OT/extras:
Settlement endpoint:

Rank 1:
Grade:

Rank 2:
Grade:

Rank 3:
Grade:

Rank 4:
Grade:

Potential winner:
Result:

Sporting settlement status:
Formal/operator settlement status:
Performance/certification status:

Primary official source:
Independent terminal lineage count:
Actual-start evidence:
Outstanding evidence:

Retrospective:
Canonical addendum/revision:
Mini-log status:
```

Do not omit a field. Use `UNKNOWN`, `NOT_APPLICABLE` or `UNRESOLVED` rather than guessing.

---

# 24. Final unresolved queue

At the end, produce an exact unresolved queue containing every record still requiring evidence.

For each:

```text
Canonical ID
Event
Exact unresolved field
Why it matters
Required source/evidence
Whether sporting grades are known
Whether formal settlement is blocked
Whether certification is blocked
```

Do not use vague wording such as "needs more research."

State precisely what is missing.

---

# 25. Final response

Return a concise operational completion report containing:

- active mini-log path;
- total event records inspected;
- terminal events found;
- events diagnostically settled;
- events formally/certifiably settled;
- events still unresolved;
- canonical IDs affected;
- Rank 1 and Rank 2 grades for each completed event;
- potential-winner results;
- important retrospective findings;
- source/custody defects;
- exact Part 6/addendum files changed;
- mini-log file changed;
- canonical ledger/counter state before and after;
- next canonical ID;
- repository write/readback result;
- verification commands and actual outcomes.

Do **not** paste the entire Combined Prediction Log into chat.

Do **not** create a new mini log.

Do **not** archive the current mini log.

Do **not** allocate new canonical IDs for settlement or retrospective work.

---

# Final hard rules

> **Settlement attaches to the existing canonical event ID. It never gets a new P-ID merely because the result is now known.**

> **Every event in the running log must retain an explicit `Canonical ID:` field and `Canonical status:` field.**

> **A known final score does not automatically mean certified settlement.**

> **Unknown operator definitions, period fields, participant-action rules, source independence or actual-start evidence remain explicitly unresolved.**

> **Original predictions are immutable. All settlement, corrections and retrospectives are append-only.**

> **Wins and losses receive the same retrospective scrutiny.**

> **No result from one game may silently become a new model rule, coefficient, cap, probability adjustment or ranking penalty.**

> **If repository write/readback fails, report the failure and preserve the work without pretending the canonical repository changed.**
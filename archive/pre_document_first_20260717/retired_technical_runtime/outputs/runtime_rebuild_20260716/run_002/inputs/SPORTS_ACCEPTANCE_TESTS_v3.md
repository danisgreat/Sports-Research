# Sports v3 Acceptance Tests

Effective: 2026-07-16  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**  
Owner: Sports research governance

This document converts hard rules into fail-closed tests. A prose checklist is not a pass. `scripts/validate_v3_system.ps1` executes static checks and the Node runtime exercises implemented packet, control, journal, scoring and development rules. Unimplemented or partial requirements remain activation blockers.

## 1. Test-state semantics

- `PASS`: the named executable test ran against the exact artifact/version and produced its expected result.
- `FAIL`: requirement violated; the prescribed fail-closed action applies.
- `NOT_RUN`: no evidence. It is not a pass and cannot support ACTIVE status.
- `NOT_APPLICABLE`: allowed only when the gate's applicability rule proves it; it cannot be used to bypass an ISSUE prerequisite.

Machine traceability is `schema/acceptance_traceability_v1.csv`. For the suspended 2026-07-16 rebuild it contains 88 unique requirements: 20 `COVERED`, 42 `PARTIAL`, and 26 `NOT_IMPLEMENTED`. Those labels describe executable coverage, not model performance. An OPERATIONAL release is prohibited until every row is `COVERED`; `src/controls.mjs` enforces that transition rule. A green Node run means only that implemented tests passed, with explicit TODOs and traceability gaps still visible. With no real ACTIVE model, every resolved quantitative request still returns `PASS / MODEL_UNAVAILABLE`.

## 2. Static specification tests

| Test ID | Owner | Pass condition | Failure action |
| --- | --- | --- | --- |
| `SPEC-FILES-001` | Governance | All nine manifest-listed artifacts exist | GATE-AUTH-001 fails; SYSTEM_NOT_READY |
| `SPEC-STATUS-001` | Governance | All canonical Markdown specs say `CANONICAL SPECIFICATION` and `SUSPENDED — NO ACTIVE MODELS` | GATE-AUTH-001 fails |
| `SPEC-AUTH-001` | Governance | Manifest lists precedence and explicitly makes legacy files non-operative | GATE-AUTH-001 fails |
| `SPEC-COVERAGE-001` | Model governance | Coverage CSV parses, IDs are unique, status values are controlled and ACTIVE count is zero in this release | Suspend system |
| `SPEC-DEVELOPMENT-MODELS-001` | Model governance | Every DEVELOPMENT coverage row has a catalogued model ID/version, no activation evidence fields, an explicit non-active reason, and the expected broad sport architectures are present | SYSTEM_NOT_READY |
| `SPEC-SCHEMA-001` | Data owner | Dictionary contains request/snapshot/prediction/candidate/branch/source/model/test/calibration/uncertainty/simulation/price/execution/settlement/evaluation entities | SYSTEM_NOT_READY |
| `SPEC-MODES-001` | Product/data owner | Both orthogonal mode vocabularies and conditional null rules exist | GATE-MODE-001 fails |
| `SPEC-GATES-001` | Governance | Every universal hard-gate ID appears in the manual and this file | SYSTEM_NOT_READY |
| `SPEC-SCORING-001` | Evaluation owner | Canonical Brier/log-loss/EV fixtures reproduce expected values | Scoring unavailable |
| `SPEC-NO-BROKEN-REF-001` | Governance | Canonical specs contain no reference to a missing operative dependency | GATE-AUTH-001 fails |

The bundled validator must exit nonzero on any static failure and print that a clean run validates specification safety only, not model validity.

## 3. Runtime hard gates

| Gate ID | Owner | Applies to | Executable pass condition | Required evidence | Failure result |
| --- | --- | --- | --- | --- | --- |
| `GATE-AUTH-001` | Governance | Every request | Static validator PASS; manifest/dependencies/hash versions match deployed package | Validator output + deployment manifest | PASS / SYSTEM_NOT_READY |
| `GATE-CONTRACT-001` | Request owner | Every request | ISSUE-path event/primary question/market/outcome space/settlement fields resolve; failure still freezes raw request/PASS without invented IDs | Frozen request + contract test log | PASS / CONTRACT_UNRESOLVED |
| `GATE-MODE-001` | Request owner | Every request | ISSUE-path `analysis_mode` and `forecast_state` independently validate; failure stores null unresolved mode/PASS; LIVE state/horizon populated | Schema validation output | PASS / MODE_UNRESOLVED |
| `GATE-CUTOFF-001` | Data owner | Every snapshot | All decisive source/feature `known_at <= cutoff <= frozen_at`; production fetch at/before freeze; pregame before actual start; LIVE state at/before freeze | Temporal-join test + raw hashes | PASS / CUTOFF_FAILURE |
| `GATE-SOURCE-001` | Source owner | Every snapshot | Required identity/rules/state/final authority and approved feature sources resolve; blocked/stale/conflict policy passes | Source-map version + parser/latency regression report | PASS / SOURCE_FAILURE |
| `GATE-UNIVERSE-001` | Selection owner | Every request | Universe and policy froze before outcome; child count/hash reconcile; exactly one primary question; every inspected/rejected candidate stored | Candidate-universe test artifact | PASS / UNIVERSE_NOT_FROZEN |
| `GATE-MODEL-001` | Model owner/approver | ISSUE | Exact ACTIVE model card and ACTIVE unexpired coverage row join every scope/artifact; no wildcard ACTIVE field | Model/coverage join report | PASS / MODEL_UNAVAILABLE |
| `GATE-TEST-001` | Independent evaluator | ISSUE/model activation | Train/tune/calibrate/test manifests disjoint; preregistration predates first view; test marked SPENT; later prospective shadow passed exact rule | Event manifests + timestamps + reports | PASS / MODEL_UNAVAILABLE |
| `GATE-PROB-001` | Model/evaluation owner | ISSUE | Branches sum within 1e-9; selected probability matches WIN aggregate; reproducible from artifacts; calibration wording/status valid | Probability fixture/reproduction report | PASS / PROBABILITY_INVALID |
| `GATE-COHERENCE-001` | Model/evaluation owner | ISSUE with related markets | Every linked distribution/state exists; constraint type is controlled; shared joint-distribution ID and declared invariants reconcile | Joint-state artifact + invariant test | PASS / PROBABILITY_INVALID |
| `GATE-UNCERTAINTY-001` | Model owner | ISSUE | TOTAL_PROBABILITY quantified; material components assessed/quantified; no material NOT_ESTIMABLE; decision robust under registered sensitivity | Uncertainty artifact + policy replay | PASS / UNCERTAINTY_UNRESOLVED |
| `GATE-PRICE-001` | Market-data owner | PRICE_ENABLED ISSUE | Complete contemporaneous outcome quotes, no-vig method, commission/payoffs, expiry/limits and EV interval recompute exactly | Market snapshot + calculation test | PASS / PRICE_PACKET_INVALID |
| `GATE-EXECUTION-001` | Risk/execution owner | Stake/yield/P&L/CLV claim | Authorized execution and applicable closing snapshot exist; receipt/hash, commission and risk-policy link validate | Execution audit | Claim prohibited |
| `GATE-SETTLEMENT-001` | Settlement reviewer | Settlement | Stored convention maps official outcome to exact branch; append-only/correction lineage and source pass | Settlement test + source | PENDING/UNGRADABLE |
| `GATE-LEGACY-001` | Evaluation owner | Evaluation | Every legacy/mixed-cutoff/missing-artifact row maps to EXCLUDED_LEGACY and cannot enter v3 metric query | Eligibility-query test | Report invalid/suspend |

## 4. Mandatory negative tests

An activation suite must prove fail-closed behaviour, not only happy paths.

### Identity and immutability

- Duplicate `snapshot_id` or `prediction_id` insert fails.
- Attempt to update a frozen snapshot/prediction/source packet/candidate universe fails; a new snapshot with `parent_snapshot_id` succeeds.
- Settlement cannot reference only `forecast_series_id` or an ambiguous version.
- Hash recomputation after any child-field mutation fails.

### Contract, mode and cutoff

- Missing settlement branch, primary question or event ID returns PASS/CONTRACT_UNRESOLVED.
- LIVE used as an analysis mode fails; PRICE_ENABLED plus LIVE is representable through two separate fields.
- PREGAME_PROJECTED and PREGAME_CONFIRMED never share an evaluation stratum without validated hierarchy.
- A source with `known_at` one microsecond after cutoff is rejected.
- A production fact fetched after freeze is rejected.
- A historical later fetch without versioned as-of evidence is rejected.
- A LIVE snapshot without sport-required clock/exposure/state is rejected.

### Candidate selection

- Universe child count/hash mismatch fails.
- Missing inspected/rejected candidate fails.
- Universe/policy frozen after an outcome or later live state fails.
- Multiple or zero primary questions fail.
- Changing selection threshold after untouched-test view spends the test and requires new future data.

### Model, test and shadow

- Model card ACTIVE with coverage DEVELOPMENT/UNSUPPORTED fails ISSUE.
- Coverage ACTIVE with model SHADOW/SUSPENDED fails ISSUE.
- ACTIVE coverage containing `ALL` in competition/market/state/mode fails.
- Artifact or scope mismatch fails even if names look similar.
- Any train/tune/calibration/test event overlap fails.
- Test results viewed before preregistration timestamp fail.
- Reusing a SPENT test for a changed feature/model/rule fails.
- Historical test pass without later prospective-shadow pass fails ACTIVE.
- Point improvement that misses the preregistered effect/uncertainty rule fails.

### Probability, calibration and uncertainty

- Outcome sum outside `1e-9` fails.
- PUSH probability duplicated on opposing candidates fails.
- Non-structural exact zero/one fails ISSUE.
- Calling raw=decision “calibrated” without VALIDATED/IDENTITY_JUSTIFIED evidence fails.
- A material NOT_ESTIMABLE input/model component fails ISSUE.
- A sensitivity scenario that flips the decision outside tolerance fails ISSUE.
- Correlated simulation using independent-Bernoulli MCSE fails.

### Price and execution

- RESEARCH_ONLY with edge/EV/stake fields fails.
- Incomplete outcome price set or stale quote fails PRICE_ENABLED ISSUE.
- Push-capable EV computed as `p*d-1` fails the `EV-WITH-PUSH` fixture.
- Positive point EV whose conservative interval/policy fails cannot be labelled value.
- Yield/P&L/CLV without execution fails; a quoted/watchlist price is insufficient.

### Settlement and evaluation

- Settlement that edits probability/model/rationale fails immutability.
- Missing phase cannot be inferred from full-event result.
- Correction without prior settlement/reason fails.
- Opposite sides or multiple markets cannot be counted as independent events.
- Legacy rows cannot become eligible by backfilling from retrospective text.
- Metric query must report exact inclusion denominator, passes, pending, void and ungradable counts.

## 5. Scoring and evaluation tests

| Test ID | Pass condition |
| --- | --- |
| `SCORE-BINARY-WIN` | Brier/log loss match `SPORTS_SCORING_SPECIFICATION_v3.md` within 1e-12 |
| `SCORE-BINARY-LOSS` | Brier/log loss match within 1e-12 |
| `SCORE-THREE-PUSH` | Three-branch normalized Brier/log loss match within 1e-12 |
| `SCORE-ZERO-OBSERVED` | Canonical log loss is positive infinity; raw zero remains stored |
| `EV-NO-PUSH` | Branch payoff EV is 0.10 |
| `EV-WITH-PUSH` | Branch payoff EV is 0.00 and invalid shortcut differs |
| `EVAL-IDENTICAL-SET` | Model and baseline have identical event/branch/weight keys |
| `EVAL-EVENT-WEIGHT` | Multiple predictions are averaged within event before event-level aggregation unless preregistered otherwise |
| `EVAL-CLUSTER` | Paired event clusters and any required time/participant blocks are used |
| `EVAL-SELECTION` | Complete model-selected universe and primary question are reported separately |

## 6. Drift, suspension and restart tests

| Test ID | Owner | Pass condition |
| --- | --- | --- |
| `DRIFT-CONFIG-001` | Model owner | Numeric statistic, window, minimum N, warning/suspend thresholds and missingness policy exist before ACTIVE |
| `DRIFT-SUSPEND-001` | Operations | Seeded threshold breach changes model/coverage to SUSPENDED and blocks ISSUE immediately |
| `INCIDENT-LEAKAGE-001` | Data/governance | Seeded post-cutoff feature blocks output and opens incident record |
| `ROLLBACK-001` | Model owner/approver | Restart requires new version, correction ticket, fresh untouched evidence, new prospective shadow and approval |

Words such as “material,” “consistent,” “current,” “protected” or “non-critical” are not executable until a model card supplies numeric/controlled definitions and tests.

## 7. Go-live rule

A specific scope may change to ACTIVE only when:

1. the static validator passes;
2. every applicable runtime gate and negative test passes against the exact production artifacts;
3. the untouched test has become SPENT only after preregistered evaluation;
4. a later mandatory prospective shadow passes;
5. model and coverage approvals/expiry are populated; and
6. the authority-manifest/coverage change is reviewed atomically.

No test may be waived by narrative judgment. Until then, the only compliant response is WATCH/PASS with null quantitative fields.

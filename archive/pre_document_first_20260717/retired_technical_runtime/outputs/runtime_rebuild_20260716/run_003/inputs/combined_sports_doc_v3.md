# Sports Research Operating Manual v3

Effective: 2026-07-16 (Australia/Sydney)  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**  
Scope: research requests, abstentions, probabilistic forecasts, optional price evaluation, settlement and model review

`SPORTS_RESEARCH_AUTHORITY_MANIFEST.md` controls document authority and precedence. `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` controls operational activation. It currently contains no ACTIVE row, so every quantitative request must return `PASS` with `pass_reason=MODEL_UNAVAILABLE`. A canonical specification is not evidence that a model is fitted, calibrated, profitable or ready.

## 1. Claims and decision meanings

- A probability is not a promise. Never use `lock`, `certain`, `guaranteed`, `safe`, or equivalent language.
- No honest process can promise no mistakes. The commitment is to frozen inputs, reproducibility, proper scoring, uncertainty, error measurement and abstention.
- `ISSUE` means a user-facing quantitative forecast from an ACTIVE, exactly in-scope model. It does not mean bet, value or guaranteed outcome.
- `WATCH` is a temporary non-forecast state while a named prerequisite is pending. It contains no decision probability, edge, expected value or stake, is not scored as a forecast, and must expire or be replaced by a new immutable snapshot.
- `PASS` is an abstention. It always has a controlled `pass_reason` and contains no forecast probability when the reason is `MODEL_UNAVAILABLE`, `CONTRACT_UNRESOLVED`, `CUTOFF_FAILURE`, `SOURCE_FAILURE`, `OUT_OF_SCOPE`, `UNCERTAINTY_UNRESOLVED`, or `PRICE_PACKET_INVALID`.
- A non-probabilistic research note may accompany WATCH/PASS, but it must not contain a numeric probability range, confidence label, edge, value, staking or profitability language.
- Historical v2/v3 probabilities are `LEGACY_UNVERIFIED_SNAPSHOT`. They are diagnostic evidence only and cannot support a verified accuracy, calibration, ROI, yield or CLV claim.
- `Comprehensive` means completed coverage against a declared checklist. It never means all possible facts were found.

## 2. Orthogonal modes

Every request freezes two independent fields under **GATE-MODE-001**:

1. `analysis_mode = RESEARCH_ONLY | PRICE_ENABLED`.
2. `forecast_state = PREGAME_PROJECTED | PREGAME_CONFIRMED | LIVE`.

`RESEARCH_ONLY` hard-blocks price-derived edge, expected value, stake, yield, P&L and CLV. `PRICE_ENABLED` permits evaluation only after a complete, contemporaneous market packet passes **GATE-PRICE-001**. LIVE is not a price mode; it is a forecast state and needs exact state/exposure.

Pregame-projected, pregame-confirmed and live forecasts use separate model scopes, identifiers, evaluation strata and calibration evidence. Live forecasts are further segmented by sport-native state/horizon buckets declared in the model card.

## 3. Universal hard gates

These gates fail closed. Their owners and executable acceptance tests are in `SPORTS_ACCEPTANCE_TESTS_v3.md`.

| Gate ID | Requirement | Failure result |
| --- | --- | --- |
| GATE-AUTH-001 | Canonical authority resolves through the manifest; every dependency exists | PASS / SYSTEM_NOT_READY |
| GATE-CONTRACT-001 | Event, primary question, market, outcome space and settlement convention are exact | PASS / CONTRACT_UNRESOLVED |
| GATE-MODE-001 | Analysis mode and forecast state are independently recorded | PASS / MODE_UNRESOLVED |
| GATE-CUTOFF-001 | Snapshot is immutable; all decisive facts were knowable by cutoff; live state is at/before publication | PASS / CUTOFF_FAILURE |
| GATE-SOURCE-001 | Identity/rules/state/final use approved authority; source packet has fact-level timestamps/status/hashes | PASS / SOURCE_FAILURE |
| GATE-UNIVERSE-001 | Primary question, selection mode, universe version and every inspected/rejected candidate were frozen before outcome | PASS / UNIVERSE_NOT_FROZEN |
| GATE-MODEL-001 | Model and coverage rows are ACTIVE, approved, unexpired and exactly match sport/competition/market/settlement/state/horizon and artifacts | PASS / MODEL_UNAVAILABLE |
| GATE-TEST-001 | Train/tune/calibrate/test periods are disjoint; test was untouched; mandatory prospective shadow passed; viewed tests are spent | PASS / MODEL_UNAVAILABLE |
| GATE-PROB-001 | Complete outcome branches reconcile; decision probability is reproducible; calibration wording is supported | PASS / PROBABILITY_INVALID |
| GATE-COHERENCE-001 | Related markets share a registered joint outcome space and satisfy every declared logical/arithmetic invariant | PASS / PROBABILITY_INVALID |
| GATE-UNCERTAINTY-001 | Typed total and material component uncertainty is quantified; decision is robust to declared scenarios | PASS / UNCERTAINTY_UNRESOLVED |
| GATE-PRICE-001 | PRICE_ENABLED packet has complete outcome quotes, time/source, de-vig method, commission/payoffs, staleness and limits | PASS / PRICE_PACKET_INVALID |
| GATE-EXECUTION-001 | Stake/yield/P&L/CLV has an authorized immutable execution and applicable closing snapshot | Claim prohibited |
| GATE-SETTLEMENT-001 | Official result and stored convention produce an append-only grade; forecast remains unchanged | UNGRADABLE/PENDING |
| GATE-LEGACY-001 | Legacy and mixed-cutoff rows are excluded from v3 metrics | Exclude from evaluation |

No evidence grade, analyst judgment or “stricter rule” may override a failed hard gate.

## 4. Prediction lifecycle

### Stage A — freeze the request and primary question

Before research, record:

- `request_id`, verbatim/raw request, `primary_question_id`, `forecast_series_id`, author and request time;
- official sport, competition, season/round, participants, venue, event ID, scheduled start and ruleset;
- exact market ID/definition, selection, line, full outcome space and settlement convention;
- `analysis_mode`, `forecast_state`, forecast horizon and cutoff;
- `selection_mode = USER_SUPPLIED | FIXED_UNIVERSE | MODEL_SELECTED`;
- candidate-universe version and selection-policy version;
- whether overtime, extra time, shootouts, extra innings, Super Overs, DLS/reduced exposure, target-score overtime or other branches count.

If identity, primary question, outcome space, settlement or mode is unresolved, freeze a PASS snapshot with the raw request and unresolved fields null; do not invent placeholder IDs and do not continue to a probability.

### Stage B — freeze the complete candidate universe

Log every candidate inspected, including rejected candidates, before the outcome is known. Each candidate stores market ID, selection, line, relationship, inclusion source, selection-policy score if any, eligibility, rejection reason and whether it is the primary question. A model-selected pipeline must be evaluated with the same universe-generation and selection code used prospectively.

The opposite side and push branch belong to one mutually exclusive outcome space. They are not independent picks. One issued prediction addresses one declared selection; secondary claims cannot replace the primary requested outcome in reporting.

### Stage C — build a point-in-time source packet

Use `SPORTS_SOURCE_REGISTRY_v3.md` as the researched fact-specific catalog. Each ACTIVE model must still supply an approved scoped `source_map_id` with parser/latency tests. Each decisive fact stores:

`source_observation_id | source_id | URL/route | authority tier | published_at | known_at | fetched_at | applies_to_time | access status | fact value/unit | raw hash`

Minimum packet:

- official fixture, identity, rules and settlement authority;
- official or explicitly projected availability/lineup state;
- performance features with definition, competition/season scope, latency and last observation time;
- venue/match-window conditions when material;
- exact official live state for LIVE;
- complete market snapshot for PRICE_ENABLED.

All feature/source joins must satisfy the temporal tests in `SPORTS_ACCEPTANCE_TESTS_v3.md`. Blocked, stale, snippet-only, conflicting or missing decisive evidence is recorded and fails closed unless the registered model explicitly supports that missingness and the uncertainty gate passes.

### Stage D — data and leakage tests

- Event/team/player IDs, competition, season, phase, venue and rules variant match.
- Feature definitions and units are versioned and stable over their applicable window.
- Duplicates, postponements, corrections, projected/confirmed status and missing phases are explicit.
- No final, closing, revised post-cutoff injury/lineup, later live state or outcome-derived field enters a frozen feature snapshot.
- Historical backtests reproduce production latency and missingness; a modern fetch of an as-of dataset is labelled reconstruction and must prove the value/version existed by cutoff.
- Snapshot hash recomputation, foreign keys and immutability tests pass.

### Stage E — activate only a validated model

The exact coverage row and model card must both be ACTIVE. The current registry has no ACTIVE models.

An activation candidate must have:

- exact target, scope, settlement, state and forecast horizon;
- cutoff-safe training data and reproducible artifacts;
- frozen naive baseline and, in PRICE_ENABLED mode, no-vig market comparator on identical eligible events;
- one preregistered primary metric, minimum practically relevant improvement, effective-N/precision rule and guardrails;
- disjoint train, tune, calibration and untouched-test periods;
- an untouched mandatory prospective shadow period after all choices are frozen;
- typed calibration evidence and total uncertainty;
- approval, expiry, drift, suspend, rollback and restart rules.

The untouched test may be evaluated once. Once any test outcome or aggregate is viewed, that period is `SPENT` for every related challenger or manual rule. A failed or modified model needs a new later untouched period. A point-estimate win without the preregistered uncertainty/effect rule is not evidence of improvement.

### Stage F — freeze ISSUE, WATCH or PASS

Every request receives a new immutable `snapshot_id`. Updates use a new snapshot and link `parent_snapshot_id`; a stable `forecast_series_id` groups the sequence. An ISSUE also receives a unique immutable `prediction_id` that is never versioned or reused.

ISSUE requires:

- exact ACTIVE model/coverage scope and artifact hashes;
- complete branch probabilities and raw/decision probability;
- calibration status/evidence without unsupported “calibrated” wording;
- typed uncertainty and invalidation triggers;
- baseline on the same eligibility set;
- price/no-vig/EV fields only for PRICE_ENABLED;
- one primary question and the frozen candidate universe.

WATCH/PASS store the missing prerequisite and contain null model/probability/edge/EV fields when no valid quantitative forecast exists. A later update is a new snapshot; nothing overwrites the prior one.

### Stage G — settle independently

- Wait for an official final/gamebook/scorecard or a predeclared fallback.
- Apply the exact stored settlement convention and outcome branch.
- Append settlement versions with official status, numeric outcome, `WIN | LOSS | PUSH | VOID | UNGRADABLE | PENDING`, source, fetch time and reviewer.
- Corrections append; they never alter the frozen request, candidates, sources, model, probability, rationale or price snapshot.

### Stage H — evaluate and review

Evaluation is a derived, versioned entity keyed by prediction, settlement version, scoring-spec version and scoring-code hash. Use `SPORTS_SCORING_SPECIFICATION_v3.md`. Report the primary question, complete selection pipeline, proper scores, baseline deltas, coverage/abstention, interval coverage and event-clustered uncertainty. Do not hand-edit KPI totals.

Postmortems may create hypotheses, not rules. A change requires a ticket, new future test data, mandatory prospective shadow and a new model version. No single outcome can activate a permanent rule.

## 5. Evidence-integrity grades

Grades describe evidence integrity, not confidence or activation. They can only restrict an otherwise ACTIVE, in-scope model.

| Grade | Meaning | Maximum action |
| --- | --- | --- |
| A | Contract/source/cutoff complete; volatile inputs current; model validated for the exact state | ISSUE, WATCH or PASS if all hard gates pass |
| B | One non-critical, model-supported projected/secondary input; registered sensitivity passes | ISSUE only if the model card explicitly covers this missingness; otherwise WATCH/PASS |
| C | Material lineup/exposure/surface/phase gap, transfer or unresolved component | WATCH/PASS |
| D | Contract/cutoff/leakage/stale-state/settlement failure | PASS |

## 6. Sport and model scope

`SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` is the only operational allowlist. Sport-native baselines, candidate model families, transfer restrictions and minimum development evidence are defined once in `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md`; instantiated non-operational model cards are in `SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md`; fact-source chains are defined in `SPORTS_SOURCE_REGISTRY_v3.md`. A DEVELOPMENT card records intended mechanics and blockers only. An unlisted, expired or non-ACTIVE scope must PASS.

## 7. Distributions and simulation

Distribution choice, Poisson diagnostics, alternatives, simulation records, convergence and Monte Carlo error are owned by the validation framework. Poisson is not an all-sport default, simulation repeatability is not forecast validity, and no simulated probability may bypass GATE-MODEL-001 or GATE-UNCERTAINTY-001.

## 8. Price, EV and execution

`SPORTS_SCORING_SPECIFICATION_v3.md` is the single authority for de-vig, outcome-branch payoff and expected-return mathematics; `SPORTS_DATA_DICTIONARY_v3.md` owns the price and execution entities. Keep `baseline_probability_delta`, realized proper-score skill, `market_edge` and `expected_return` distinct. RESEARCH_ONLY prohibits price/value/stake claims. PRICE_ENABLED still requires the registered conservative decision rule, and realized yield/P&L/CLV require an actual execution.

## 9. Monitoring, suspension and rollback

The validation framework owns monitoring windows, drift thresholds, suspension, restart and rollback. Leakage, scope/artifact mismatch, broken definitions, unresolved settlement error, regression failure or a preregistered drift breach must fail closed immediately; only a new approved version with new untouched evidence and prospective shadow may resume.

## 10. Minimum outputs

### ISSUE

```text
REQUEST / PRIMARY QUESTION / FORECAST SERIES:
SNAPSHOT ID / PREDICTION ID / PARENT SNAPSHOT:
ANALYSIS MODE / FORECAST STATE / HORIZON / CUTOFF UTC:
EVENT / MARKET / SELECTION / OUTCOME BRANCHES / SETTLEMENT:
CANDIDATE UNIVERSE / SELECTION MODE / POLICY VERSION:
DATA-QUALITY GRADE / DECISIVE SOURCES:
MODEL / COVERAGE / DATA / FEATURE / CODE / CALIBRATION ARTIFACTS:
RAW P / DECISION P / TYPED UNCERTAINTY:
BASELINE / BASELINE SKILL DELTA:
PRICE SNAPSHOT / NO-VIG METHOD / MARKET EDGE / EV INTERVAL: PRICE_ENABLED only
DECISION: ISSUE
INVALIDATION TRIGGERS:
```

### WATCH or PASS

```text
REQUEST / PRIMARY QUESTION / FORECAST SERIES:
SNAPSHOT ID / PARENT SNAPSHOT:
ANALYSIS MODE / FORECAST STATE / CUTOFF UTC:
EVENT / MARKET / SETTLEMENT:
CANDIDATE UNIVERSE / SELECTION MODE:
DECISION: WATCH | PASS
PASS OR WATCH REASON / MISSING PREREQUISITE / EXPIRY:
NON-PROBABILISTIC RESEARCH NOTE (optional):
MODEL / PROBABILITY / EDGE / EV / STAKE: N/A
```

Storage is controlled by `SPORTS_DATA_DICTIONARY_v3.md`; scoring by `SPORTS_SCORING_SPECIFICATION_v3.md`; modelling by `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md`; gates by `SPORTS_ACCEPTANCE_TESTS_v3.md`.

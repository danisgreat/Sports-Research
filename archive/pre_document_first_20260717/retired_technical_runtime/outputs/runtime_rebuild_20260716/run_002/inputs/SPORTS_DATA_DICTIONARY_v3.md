# Sports Research Data Dictionary v3

Effective: 2026-07-16  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**

This dictionary defines a normalized target schema. It is not a claim that the tables have been implemented. Until an implementation passes `SPORTS_ACCEPTANCE_TESTS_v3.md` and the exact coverage row is ACTIVE, quantitative output is prohibited.

## 1. Design principles and entities

- A request always produces an immutable decision snapshot, including WATCH and PASS.
- A quantitative ISSUE additionally produces one immutable prediction ID.
- An update never versions or overwrites an old prediction. It creates a new snapshot/prediction and links its parent.
- The stable grouping key is `forecast_series_id`; the immutable publication key is `snapshot_id`; the quantitative forecast key is `prediction_id`.
- Candidate discovery, forecast distributions, settlement states, source facts, model artifacts, price contracts, executions, settlements and evaluations are separate entities.
- Nullability is semantic. Null probability/model fields on MODEL_UNAVAILABLE are required honesty, not missing-data defects.

```text
request 1---n decision_snapshot n---1 candidate_universe 1---n candidate
model_forecast_run 1---n forecast_distribution n---1 market_outcome_space
forecast_distribution 1---n settlement_state 1---n candidate_state_map n---1 candidate
decision_snapshot 0---1 prediction n---1 candidate n---1 forecast_distribution
decision_snapshot 0---1 live_state
decision_snapshot n---1 source_packet 1---n source_observation
model_version n---1 source_map 1---n source_map_item n---1 registered_source
source_packet 1---1 feature_snapshot
prediction n---1 model_version 1---n test_evaluation
prediction 1---n uncertainty_component 0---n simulation_run
prediction 0---1 market_price_snapshot 1---n quote_contract 1---n quote_state_payoff
prediction 0---n execution
prediction 0---n settlement_version 0---n evaluation_run
change_ticket 1---n model_version
coverage_registry 1---n model_version
```

Entities shown here but not yet backed by machine-readable stores are implementation blockers, not optional prose.

## 2. Controlled vocabularies

| Vocabulary | Allowed values |
| --- | --- |
| `contract_status` | `RESOLVED`, `UNRESOLVED` |
| `analysis_mode` | `RESEARCH_ONLY`, `PRICE_ENABLED` |
| `forecast_state` | `PREGAME_PROJECTED`, `PREGAME_CONFIRMED`, `LIVE` |
| `selection_mode` | `USER_SUPPLIED`, `FIXED_UNIVERSE`, `MODEL_SELECTED` |
| `decision` | `ISSUE`, `WATCH`, `PASS` |
| `pass_reason` | `MODEL_UNAVAILABLE`, `CONTRACT_UNRESOLVED`, `MODE_UNRESOLVED`, `CUTOFF_FAILURE`, `SOURCE_FAILURE`, `UNIVERSE_NOT_FROZEN`, `OUT_OF_SCOPE`, `PROBABILITY_INVALID`, `UNCERTAINTY_UNRESOLVED`, `SYSTEM_NOT_READY`, `USER_CANCELLED`, `OTHER_DOCUMENTED` |
| `price_evaluation_status` | `NOT_REQUESTED`, `PENDING`, `VALUE`, `NO_VALUE`, `PRICE_UNAVAILABLE` |
| `model_status` | `UNSUPPORTED`, `DEVELOPMENT`, `SHADOW`, `ACTIVE`, `SUSPENDED`, `RETIRED` |
| `test_status` | `PLANNED_UNTOUCHED`, `SPENT`, `INVALIDATED` |
| `calibration_status` | `VALIDATED`, `IDENTITY_JUSTIFIED`, `FAILED`, `NOT_ASSESSED` |
| `uncertainty_type` | `ALEATORIC_OUTCOME`, `PARAMETER`, `INPUT_SCENARIO`, `STRUCTURAL_MODEL`, `CALIBRATION`, `MONTE_CARLO`, `TOTAL_PROBABILITY` |
| `uncertainty_status` | `QUANTIFIED`, `NOT_MATERIAL_WITH_EVIDENCE`, `NOT_ESTIMABLE` |
| `candidate_status` | `ELIGIBLE`, `SELECTED`, `REJECTED_PREMODEL`, `REJECTED_MODEL`, `PASS`, `WATCH` |
| `probability_generation_status` | `GENERATED`, `NOT_REQUIRED`, `FAILED`, `NOT_RUN` |
| `candidate_relationship_type` | `COMPLEMENT`, `OVERLAP`, `NESTED`, `CORRELATED`, `SAME_EVENT_ONLY`, `NONE` |
| `branch_type` | `WIN`, `LOSS`, `PUSH`, `VOID`, `OTHER_EXHAUSTIVE` |
| `settlement_grade` | `WIN`, `LOSS`, `PUSH`, `VOID`, `UNGRADABLE`, `PENDING` |
| `evaluation_eligibility` | `ELIGIBLE_V3`, `EXCLUDED_LEGACY`, `EXCLUDED_VOID`, `EXCLUDED_CONTRACT`, `EXCLUDED_DATA`, `PENDING` |
| `transport_type` | `HTML`, `API`, `PDF`, `DYNAMIC_UI`, `SCREENSHOT`, `FILE`, `OTHER` |
| `retrieval_status` | `SUCCESS`, `BLOCKED`, `INTERMITTENT`, `NOT_FOUND`, `AUTH_REQUIRED`, `TIMEOUT`, `ERROR` |
| `freshness_status` | `CURRENT`, `STALE`, `UNKNOWN` |
| `verification_status` | `VERIFIED`, `CONFLICT`, `UNVERIFIED`, `RETIRED` |
| `interval_type` | `OUTCOME_PREDICTIVE`, `PARAMETER_PROBABILITY`, `SCENARIO_PROBABILITY`, `TOTAL_PROBABILITY` |

`sport_family`, `competition_id`, `market_family`, `ruleset_id`, `settlement_convention_id`, `state_bucket_id` and `horizon_bucket_id` require separately versioned controlled values. Free-text aliases are preserved only in `*_original` migration fields.

## 3. Request record

| Field | Type | Required | Rule |
| --- | --- | --- | --- |
| `request_id` | text/UUID | yes | Unique, never reused |
| `primary_question_id` | text/UUID | yes | One primary user-visible question |
| `primary_question_text` | text | yes | Verbatim requested target, including ambiguity; never retrospectively rewritten |
| `raw_request_text` | text/hash reference | yes | Original request evidence |
| `contract_status` | enum | yes | RESOLVED only after GATE-CONTRACT-001 passes |
| `request_timestamp_utc` | UTC timestamp | yes | Immutable |
| `forecast_series_id` | text/UUID | yes | Groups later snapshots; carries no mutable forecast values |
| `event_id` | namespaced text | conditional | Required for RESOLVED/ISSUE; null allowed on PASS/CONTRACT_UNRESOLVED |
| `sport_family` | controlled text | conditional | Required for RESOLVED/ISSUE |
| `competition_id` | controlled text | conditional | Required for RESOLVED/ISSUE |
| `season_id` | controlled text | conditional | Required for RESOLVED/ISSUE where the competition has seasons |
| `event_name` / `venue` | text | conditional | Display only; IDs control matching |
| `event_start_utc` | UTC timestamp | conditional | Required for RESOLVED/ISSUE; scheduled start known when request froze |
| `ruleset_id` | text | conditional | Required for RESOLVED/ISSUE |
| `market_id` | text | conditional | Required for RESOLVED/ISSUE; stable definition including phase/exposure/line |
| `market_family` | controlled text | conditional | Required for RESOLVED/ISSUE |
| `selection` / `line` | text/typed number | yes/conditional | Exact requested selection and numeric line |
| `settlement_convention_id` | text | conditional | Required for RESOLVED/ISSUE; versioned branch rules |
| `analysis_mode` | enum | conditional | Required after mode resolution and for ISSUE; null allowed on PASS/MODE_UNRESOLVED |
| `forecast_state` | enum | conditional | Required after mode resolution and for ISSUE; null allowed on PASS/MODE_UNRESOLVED |
| `state_bucket_id` | text | conditional | Required for LIVE; model-card comparable-state bucket |
| `horizon_bucket_id` | text | conditional | Required for ISSUE; exact lead time or live remaining-exposure bucket |
| `selection_mode` | enum | conditional | Required once candidate inspection begins and for ISSUE |
| `candidate_universe_id` | text/UUID | conditional | Required once GATE-UNIVERSE-001 is reached and for ISSUE; null on an earlier fail-closed PASS |
| `selection_policy_version` | text | conditional | Required with candidate universe; `USER_DIRECT` allowed for user-supplied requests |
| `created_by` | text | yes | Human/system author |

## 4. Decision snapshot and prediction

### 4.1 Decision snapshot

| Field | Type | Required | Rule |
| --- | --- | --- | --- |
| `snapshot_id` | text/UUID | yes | Unique immutable publication key |
| `request_id` / `forecast_series_id` | text | yes | Valid foreign keys |
| `parent_snapshot_id` | text | conditional | Required for an update; points to one earlier immutable snapshot |
| `snapshot_sequence` | integer | yes | Starts at 1 within series; informational, not part of identity |
| `frozen_at_utc` | UTC timestamp | yes | Publication/freeze time |
| `data_cutoff_utc` | UTC timestamp | yes | Latest permissible `known_at`; `<= frozen_at_utc` |
| `decision` | enum | yes | ISSUE, WATCH or PASS |
| `pass_reason` | enum | conditional | Required for PASS; blank for ISSUE |
| `watch_reason` / `watch_expires_utc` | text/timestamp | conditional | Required for WATCH |
| `price_evaluation_status` | enum | yes | NOT_REQUESTED for RESEARCH_ONLY; for PRICE_ENABLED, price failure becomes PRICE_UNAVAILABLE and does not erase an otherwise valid forecast |
| `data_quality_grade` | enum A-D | yes | Cannot override a hard gate |
| `source_packet_id` | text | conditional | Required once sourcing begins and for ISSUE; null only for an earlier contract/mode/system/user-cancelled PASS |
| `candidate_universe_id` | text | conditional | Required once candidate inspection begins and for ISSUE; null only for an earlier fail-closed PASS |
| `missing_prerequisites` | structured text/array | conditional | Required for WATCH/PASS unless user cancelled |
| `research_note` | text | no | Non-probabilistic only for WATCH/PASS |
| `snapshot_hash` | SHA-256 or stronger | yes | Hash manifest includes canonical serialization and child artifact hashes |
| `created_by` | text | yes | Author |

WATCH/PASS with no valid model require all prediction, probability, edge, EV and stake fields to be null. They are still included in coverage/abstention denominators. `PRICE_UNAVAILABLE` blocks only market edge/value/EV/execution claims; it does not convert a valid forecast ISSUE into PASS.

An early PASS remains representable even when contract or mode fields are unresolved: preserve the raw request, missing fields, pass reason and snapshot hash; do not invent placeholder IDs to satisfy ISSUE-only requirements.

### 4.2 Prediction record

Exists only when `decision=ISSUE`.

| Field | Type | Required | Rule |
| --- | --- | --- | --- |
| `prediction_id` | text/UUID | yes | Globally unique, immutable, never versioned |
| `snapshot_id` | text/UUID | yes | Unique one-to-one foreign key to ISSUE snapshot |
| `selected_candidate_id` | text | yes | Candidate was frozen and eligible before ISSUE |
| `forecast_distribution_id` | text | yes | Frozen distribution shared by every candidate in the same market outcome space; selected probability is derived from its candidate-state map |
| `model_id` / `model_version` | text | yes | Exact ACTIVE model artifact |
| `coverage_id` | text | yes | Exact ACTIVE, approved, unexpired coverage row |
| `data_version` / `feature_version` | text | yes | Immutable point-in-time artifacts |
| `code_commit_or_hash` | text | yes | Reproducible code artifact |
| `model_artifact_hash` | hash | yes | Matches approved model card |
| `feature_snapshot_hash` | hash | yes | Matches source packet/feature snapshot |
| `model_probability_raw` | decimal | yes | Unrounded full-precision selection-win probability |
| `decision_probability` | decimal | yes | Operative full-precision selection-win probability after registered calibration/transform |
| `calibration_evidence_id` | text | yes | VALIDATED or IDENTITY_JUSTIFIED evidence; never inferred from field name |
| `baseline_id` / `baseline_version` | text | yes | Frozen naive comparator |
| `baseline_probability` | decimal | yes | Same target and cutoff |
| `baseline_probability_delta` | decimal | yes | `decision_probability - baseline_probability`; a pre-outcome probability contrast, never score skill |
| `uncertainty_set_id` | text | yes | Typed components including TOTAL_PROBABILITY |
| `invalidation_triggers` | structured text/array | yes | Facts/state changes requiring a new snapshot |
| `market_price_snapshot_id` | text | conditional | Allowed only for PRICE_ENABLED and required for VALUE/NO_VALUE; null when PRICE_UNAVAILABLE or RESEARCH_ONLY |
| `market_edge` / `market_edge_estimand` | decimal/text | conditional | PRICE_ENABLED only; model and no-vig probabilities must use the same conditioning event |
| `expected_return` / `ev_lower` / `ev_upper` | decimal | conditional | PRICE_ENABLED VALUE/NO_VALUE only; unconditional settlement-state payoff calculation |

ISSUE is invalid unless the model card, coverage row, calibration evidence, artifact hashes, state/horizon and decision policy all join exactly.

## 5. Candidate universe and outcome branches

### 5.1 Candidate universe

| Field | Required | Rule |
| --- | --- | --- |
| `candidate_universe_id` | yes | Unique immutable ID |
| `request_id` | yes | Parent request |
| `universe_definition_version` | yes | Fixed list/generator specification |
| `selection_mode` | yes | Matches request |
| `selection_policy_version` | yes | Frozen before selection |
| `known_at_utc` / `frozen_at_utc` | yes | Generator inputs and complete universe are known/frozen `<= data_cutoff_utc <= decision_snapshot.frozen_at_utc` |
| `universe_hash` | yes | Includes every inspected candidate, order-independent canonical hash |
| `candidate_count` | yes | Equals stored child rows |

### 5.2 Candidate record

Every inspected market/selection is stored, including rejects.

| Field | Required | Rule |
| --- | --- | --- |
| `candidate_id` | yes | Unique within universe |
| `candidate_universe_id` | yes | Parent universe |
| `market_id` / `selection` / `line` | yes/conditional | Exact candidate |
| `market_outcome_space_id` | yes | Canonical set of mutually exclusive realized settlement states for this market/rules/line |
| `forecast_distribution_id` | conditional | Required when probability_generation_status=GENERATED; exact complements share one distribution |
| `winning_state_ids` | conditional | States that grade this candidate WIN; candidate probability is derived from their summed mass |
| `relationship_type` / `related_candidate_ids` | yes/conditional | Controlled relationship; IDs required unless NONE |
| `complement_group_id` / `overlap_group_id` | conditional | Stable deduplication/dependence groups |
| `is_primary_question` | yes | Boolean; exactly one true per primary request |
| `inclusion_source` | yes | User, fixed-universe rule ID or generator version |
| `candidate_status` | yes | Controlled status frozen before settlement |
| `rejection_reason` | conditional | Required for rejected/pass candidate |
| `selection_score` | conditional | Pre-outcome model/policy score with version; not settlement result |
| `probability_generation_status` | yes | GENERATED, NOT_REQUIRED, FAILED or NOT_RUN; never infer a missing probability |
| `selected_for_issue` | yes | Boolean; at most one for a prediction snapshot |
| `candidate_frozen_at_utc` | yes | No later than universe freeze |

Opposite sides are candidates within one market outcome space, not independent evidence. Model-selected evaluation includes the frozen status of every eligible and rejected candidate, but scores each generated forecast distribution once.

### 5.3 Model forecast run and forecast distribution

A `model_forecast_run` stores the model/data/feature/code/calibration artifacts, cutoff, candidate-universe ID, run time, deterministic run hash and every generated distribution. One `forecast_distribution` exists per run and `market_outcome_space_id`; it stores raw and decision probability vectors, baseline vector, calibration evidence, branch count, frozen time and distribution hash. Multiple opposing/overlapping candidates may reference it, but duplicating the same outcome-space distribution under separate IDs is prohibited.

### 5.4 Settlement-state record

| Field | Required | Rule |
| --- | --- | --- |
| `settlement_state_id` | yes | Unique within market outcome space and stable under the stored settlement convention |
| `forecast_distribution_id` / `market_outcome_space_id` | yes | Parent frozen distribution/outcome space |
| `state_label` / `branch_type` | yes | One mutually exclusive and exhaustive realized state |
| `raw_probability` / `decision_probability` | yes | Full-precision 0-1 values |
| `is_structural` | yes | True only for rules-mandated impossibility/certainty; structural lines are excluded from skill claims |

The exhaustive settlement-state probabilities must sum to 1 within `1e-9` before display rounding. PUSH and VOID are separate states shared by opposing candidates. Non-structural model probabilities must be strictly between 0 and 1; exact zero produces infinite log loss and exact one risks the same on failure.

### 5.5 Candidate-state map

One row per candidate × settlement state stores `candidate_id`, `settlement_state_id`, `grade = WIN | LOSS | PUSH | VOID | UNGRADABLE`, and any contract-specific payoff class. Candidate win probability is the sum of its WIN-state probabilities. Complement candidates must share the same distribution and refund-state mass. The distribution receives one proper score; publication/selection policy receives one decision evaluation.

## 6. Registered sources, source maps and feature snapshots

### 6.1 Registered source and release

A registered source has a stable `source_id` that survives URL changes and stores publisher, authority class, publisher role, canonical entry URL, transport/authentication/API/licence metadata, proxy relationship and catalog status. A separately versioned `source_release_id` stores the exact season/ruleset/product URL, published/modified/effective/data-through times, retained raw artifact and hash. Source IDs and current route qualifications live in `SPORTS_SOURCE_REGISTRY_v3.md`; reachability alone is not approval.

### 6.2 Source-map record

Each ACTIVE model needs an approved versioned `source_map_id`. The parent stores exact model/sport/competition/market/state/horizon/mode scope, effective/expiry times, owner/approver, licence/retention policy and map hash. Each source-map item stores fact/feature type, source ID, priority/required flag, release constraint, parser ID/version/hash, maximum observation age/provider lag, cutoff rule, missingness action, conflict-rule ID and regression-test report. No approved source map currently exists.

### 6.3 Source observation

| Field | Required | Rule |
| --- | --- | --- |
| `source_observation_id` / `source_packet_id` | yes | Stable keys |
| `source_map_id` / `source_id` / `source_release_id` | yes | Exact approved map item and registered source/release |
| `requested_url` / `final_url` | yes | Preserve redirects and the publisher route; a proxy is separately identified |
| `authority_class` | yes | A0, A1, B, C, D or P under the source registry |
| `fact_type` | yes | Fixture, rules, lineup, injury, statistic, condition, price, live state, final, etc. |
| `published_at_utc` / `modified_at_utc` / `first_seen_at_utc` | conditional | Preserve original timezone and conversion evidence when exposed |
| `known_at_utc` | yes | Earliest evidenced availability, conservative when uncertain |
| `fetched_at_utc` | yes | Actual access time |
| `data_through_utc` / `applies_to_time` / `effective_from_utc` / `effective_to_utc` | conditional | Distinct coverage and validity concepts |
| `transport_type` / `retrieval_status` | yes | How capture was attempted and whether it succeeded |
| `freshness_status` / `verification_status` | yes | Freshness and fact integrity are independent of transport success |
| `extracted_value` / `definition_or_unit` | yes/conditional | Compact fact and typed definition |
| `raw_snapshot_path` / `raw_hash` / `extractor_version` | conditional | Required for machine-ingested or decisive volatile facts |
| `conflict_set_id` / `supersedes_observation_id` | conditional | Preserve conflicts and corrections append-only |
| `historical_reconstruction` | yes | Boolean; true requires as-of version evidence |

For a production snapshot, decisive observations must satisfy `known_at_utc <= data_cutoff_utc` and `fetched_at_utc <= frozen_at_utc`. Historical reconstruction may be fetched later only if a versioned as-of artifact proves availability by cutoff; otherwise it fails GATE-CUTOFF-001.

### 6.4 Feature snapshot

Stores `feature_snapshot_id`, source packet, model/data/feature versions, typed feature vector, each feature's source observation IDs and availability time, serialization version and hash. Outcomes, finals, closing prices, post-cutoff revisions and later live states are prohibited. Exact feature reconstruction from artifact hashes is mandatory.

### 6.5 Live-state record

Required when `forecast_state=LIVE`. It stores `live_state_id`, snapshot/event IDs, official state source-observation ID, state observed time, state-schema version, period/clock/over/innings, score, remaining exposure, possession/striker/batter/serve state where relevant, cards/fouls/wickets/outs, competition-specific exceptional state and hash. The model card declares required typed fields for its sport/state bucket. A generic free-form JSON blob does not pass; missing required clock/exposure fails GATE-CUTOFF-001.

## 7. Model, coverage, test and calibration records

### 7.1 Model version record

Stores:

- model ID/version, owner and approver;
- exact sport, competition, market, settlement, forecast state, state bucket and horizon scope;
- target/outcome branches, eligibility and missingness policy;
- training/tuning/calibration/test/shadow boundaries and event-manifest hashes;
- frozen naive baseline and applicable no-vig comparator;
- candidate universe/selection-policy versions;
- feature list, transformations, algorithm, distribution and hyperparameters;
- one primary metric, minimum relevant improvement, effective-N/precision rule and uncertainty decision rule;
- calibration, interval/tail and protected-segment guardrails;
- production ISSUE/WATCH/PASS thresholds and PRICE_ENABLED conservative-EV rule;
- data/feature/code/model/calibration artifact hashes;
- status, approval/expiry, drift/suspend/rollback/restart rules and known exclusions.

### 7.2 Coverage join

`SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` is the operational allowlist. An ACTIVE model requires an exact coverage row with no `ALL` wildcard, all approval/test/source-map fields populated and unexpired approval. Model card ACTIVE alone is insufficient; coverage ACTIVE alone is insufficient. The current file contains no ACTIVE rows.

### 7.3 Test evaluation record

| Field | Required | Rule |
| --- | --- | --- |
| `test_evaluation_id` | yes | Unique |
| `model_id` / `model_version` | yes | Challenger |
| `test_role` | yes | TUNE, CALIBRATION, UNTOUCHED_TEST, PROSPECTIVE_SHADOW |
| `start_utc` / `end_utc` / `event_manifest_hash` | yes | Disjoint event/time manifest |
| `test_status` | yes | `PLANNED_UNTOUCHED` until any result/aggregate is viewed; then `SPENT` |
| `first_viewed_at_utc` / `viewed_by` | conditional | Required once SPENT |
| `preregistered_rule_hash` | yes | Predates view |
| `results_artifact_hash` | conditional | Required after evaluation |

Any viewed test is SPENT for the related hypothesis/model family. A change after viewing requires a new later untouched period. Prospective shadow is mandatory before ACTIVE.

### 7.4 Calibration evidence

Stores evidence ID, model/version, status, method/version or identity justification, fit period, untouched evaluation period, raw-versus-decision probability mapping, intercept/slope/reliability diagnostics with counts/uncertainty, artifact hash and limitations. `decision_probability` may equal raw only with `IDENTITY_JUSTIFIED`; it must never be called calibrated merely because the fields match.

## 8. Uncertainty and simulation

### 8.1 Uncertainty component

| Field | Required | Rule |
| --- | --- | --- |
| `uncertainty_component_id` / `uncertainty_set_id` | yes | Stable keys |
| `prediction_id` | yes | Parent ISSUE |
| `uncertainty_type` / `uncertainty_status` | yes | Controlled values |
| `estimand` | yes | Probability, count, margin, etc. |
| `method_version` / `level` | yes/conditional | Level required for intervals |
| `lower` / `upper` / `standard_error` | conditional | Typed numeric result |
| `scenario_or_model_weights` | conditional | Required for mixture/disagreement components |
| `evidence_artifact_hash` | yes | Reproducible artifact |

Every ISSUE needs a QUANTIFIED `TOTAL_PROBABILITY` interval and an assessment of parameter, input-scenario, structural-model and calibration uncertainty. A material component cannot be `NOT_ESTIMABLE`; pass instead. Aleatoric outcome variability must not be mislabeled as uncertainty in the probability estimate.

### 8.2 Simulation run

Stores simulation ID, prediction/model/data/feature/code hashes, generator/PRNG version, seed, draw count, dependence/MCMC/quasi-random method, parameters, parameter-draw source, scenario weights, branch distribution, convergence target/result, error-estimator method, MCSE/effective sample size where applicable, sensitivity artifact and run hash. The independent-Bernoulli MCSE formula is prohibited for correlated draws unless justified.

## 9. Market prices and executions

### 9.1 Market price snapshot and outcome quotes

The parent stores `market_price_snapshot_id`, market ID, provider/book/exchange, URL/route, quote time, fetch time, expiry/staleness limit, currency, commission/payoff rules, limit information, complete-outcome flag, de-vig method/version, overround and hash.

Each `outcome_quote` stores outcome branch/selection, decimal price, raw implied probability, no-vig probability and net profit per unit for every settlement branch. The complete mutually exclusive price set must reconcile before PRICE_ENABLED evaluation.

Expected return is always:

`sum(branch_probability * net_profit_per_unit_for_branch)`.

Price, de-vig, branch-payoff and expected-return calculations are defined only in `SPORTS_SCORING_SPECIFICATION_v3.md`. This dictionary stores their versioned inputs and outputs; it does not restate the formulas.

### 9.2 Execution record

Stores execution ID, prediction ID, authorizing request/risk-policy ID, requested and accepted time, provider/account class, accepted decimal price, accepted stake/exposure, currency, commission, limits, status, correlated exposure group, linked opening/execution/closing snapshots and immutable receipt/hash. Stake, yield, P&L and CLV are null without a qualifying execution. A quoted price is not an execution.

## 10. Settlement and evaluation

### 10.1 Settlement version

| Field | Required | Rule |
| --- | --- | --- |
| `settlement_id` / `settlement_version` | yes | Append-only unique version; starts at 1 |
| `prediction_id` / `snapshot_id` | yes | Exact immutable forecast |
| `settled_at_utc` | yes | Verification time |
| `official_event_status` | yes | FINAL, POSTPONED, ABANDONED, SUSPENDED, CANCELLED, UNDER_REVIEW |
| `observed_outcome_branch_id` | conditional | Exact stored branch when gradable |
| `numeric_outcome` | conditional | Exact score/count/phase |
| `grade` | yes | Controlled settlement grade |
| `settlement_source_url` / `source_fetched_at_utc` | yes except PENDING | Direct official evidence or registered fallback |
| `rules_applied` / `reviewer` | yes | Stored convention and verifier |
| `prior_settlement_id` / `correction_reason` | conditional | Required for correction |

Settlement contains no revised probability, rationale, model, feature, source or price fields.

### 10.2 Evaluation run

Evaluation is derived and append-only, not hand-maintained. It stores evaluation ID, prediction/snapshot, settlement version, scoring-spec version, scoring-code hash, eligibility/exclusion reason, primary-question flag, selection-mode/universe version, Brier/log loss, baseline scores/deltas, interval inclusion, numeric error where applicable, error-taxonomy code, event cluster, time/block definition and report artifact hash. Execution-only fields are computed only from an execution link.

## 11. Canonical hard validations

1. **GATE-AUTH-001:** authority/status/dependencies pass the validator; no missing referenced operative document.
2. **GATE-CONTRACT-001:** ISSUE requires exact event, primary question, market/outcome space and settlement. Failure freezes PASS/CONTRACT_UNRESOLVED with raw request and null unresolved fields; it never invents identifiers.
3. **GATE-MODE-001:** ISSUE requires both orthogonal modes from controlled values. Failure freezes PASS/MODE_UNRESOLVED with null unresolved mode fields.
4. **GATE-CUTOFF-001:** `data_cutoff_utc <= frozen_at_utc`; pregame freezes before actual start; every decisive source/feature is as-of cutoff; LIVE state observation is at/before freeze and has required exposure.
5. **GATE-SOURCE-001:** decisive identity/rules/state/final facts and model features join the approved source map; access status, latency/parser tests, definitions and hashes pass. Failure freezes PASS/SOURCE_FAILURE.
6. **GATE-UNIVERSE-001:** universe/candidates/policy froze before outcome; candidate count/hash reconcile; exactly one primary question; all inspected candidates exist.
7. **GATE-MODEL-001:** ISSUE joins exact ACTIVE model and ACTIVE coverage scope, approval, expiry and artifacts. No wildcard ACTIVE scope.
8. **GATE-TEST-001:** event manifests and time periods do not overlap; test rule predates view; untouched test is SPENT after first view; later mandatory shadow passed.
9. **GATE-PROB-001:** full branches reconcile within `1e-9`; selected decision probability equals the WIN branch aggregate; non-structural values are in `(0,1)`; calibration wording matches evidence.
10. **GATE-COHERENCE-001:** related distributions reference one declared joint outcome space; linked state IDs and controlled logical/arithmetic invariants reconcile.
11. **GATE-UNCERTAINTY-001:** typed component set and total interval exist; material NOT_ESTIMABLE fails; decision passes registered sensitivity.
12. **GATE-PRICE-001:** RESEARCH_ONLY has null price math; PRICE_ENABLED ISSUE has a complete valid snapshot and reproducible no-vig/branch EV interval.
13. **GATE-EXECUTION-001:** stake/yield/P&L/CLV fields require authorized execution and relevant price snapshots.
14. **GATE-SETTLEMENT-001:** settlement is append-only and references exact branch/convention; correction lineage is complete.
15. **GATE-LEGACY-001:** legacy/unverifiable rows cannot become ELIGIBLE_V3.
16. Conditional nullability: ISSUE requires prediction/model/probability fields; WATCH/PASS without valid quantitative model require them null.
17. Hashes use canonical serialization and recompute exactly; IDs/foreign keys/uniqueness pass.

## 12. Deprecated and legacy treatment

Ranks, top/bottom penalties, sweep exemptions, manually typed probability buckets, opposite-side pseudo-picks, settlement text in prediction rows, generic source names without timing, and one-result active rules are prohibited.

Rows migrated from ledgers/logs/workbooks remain `LEGACY_UNVERIFIED_SNAPSHOT` and `EXCLUDED_LEGACY`. They may generate audit hypotheses only. Missing cutoff, source, candidate, model or probability fields must never be reconstructed from memory or post-event text.

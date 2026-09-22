# Sports Research Authority Manifest

Effective: 2026-07-16 (Australia/Sydney)

Status: CANONICAL SPECIFICATION

Operational status: **SUSPENDED — NO ACTIVE MODELS**

Owner: Sports research governance

## 1. Single source of authority

This manifest is the single source of authority for precedence and permitted claims. The machine release state is `SPORTS_RELEASE_MANIFEST_v1.json`; a mismatch between it and this manifest must fail closed as `PASS / SYSTEM_NOT_READY` and is an incident.

Older words such as ACTIVE, canonical, current, recommended, or “use the stricter rule” have no force unless this manifest lists the artifact as operative. Conflicts are recorded and resolved by a versioned reviewed change; the runtime must not choose whichever interpretation is more favorable.

## 2. Operative precedence

| Precedence | Artifact | Authority |
| ---: | --- | --- |
| 1 | `SPORTS_RESEARCH_AUTHORITY_MANIFEST.md` | precedence, claim boundaries, conflict rule |
| 2 | `SPORTS_RELEASE_MANIFEST_v1.json` | machine release mode, activation authorization, expected ACTIVE count, current capability truth |
| 3 | `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` | exact sport/competition/market/state/mode operational allowlist |
| 4 | `SPORTS_MODEL_REGISTRY_v1.csv`, `schema/contract_registry_v1.csv`, `schema/source_maps_v1.csv`, `schema/test_evaluations_v1.csv` | exact model, contract, source-map, untouched-test and shadow evidence joins |
| 5 | `schema/controlled_vocabularies_v1.json`, `schema/competition_registry_v1.csv`, `SPORTS_REGISTERED_SOURCES_v1.csv` | controlled identifiers and researched source records |
| 6 | `combined_sports_doc_v3.md` | universal workflow, decisions, modes, claims and hard gates |
| 7 | `SPORTS_DATA_DICTIONARY_v3.md`, `schema/decision_packet.schema.json` | entities, fields, nullability, keys and compiled packet structure |
| 8 | `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md` | model development, chronological validation, calibration, uncertainty, simulation, promotion and rollback |
| 9 | `SPORTS_SOURCE_REGISTRY_v3.md` | fact-specific source research; never an approved model map by itself |
| 10 | `SPORTS_SCORING_SPECIFICATION_v3.md` | eligibility, proper scores, weighting, branch payoff and evaluation versions |
| 11 | `SPORTS_ACCEPTANCE_TESTS_v3.md`, `schema/acceptance_traceability_v1.csv` | acceptance requirements and honest executable-test coverage |
| 12 | `src/`, `scripts/sportsctl.mjs`, `scripts/validate_v3_system.ps1` | executable enforcement; code cannot broaden a higher-precedence permission |
| 13 | `runtime/store/journal.jsonl`, `runtime/store/head_anchor.json` | append-only decision/settlement/evaluation record and local head anchor |

The runtime control-bundle hash binds executable code and machine controls for a recorded decision. It does not prove that a model is accurate; activation evidence must also join.

## 3. Current operational truth

- Release mode is `SUSPENDED` and activation authorization is false.
- `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` contains zero ACTIVE rows, 15 DEVELOPMENT architecture rows, and one UNSUPPORTED catch-all row.
- Contract, source-map and test-evaluation machine registries contain no approved data rows.
- Model registry rows are DEVELOPMENT only; none contains a fitted/calibrated/untouched-test/shadow approval bundle.
- Runtime journal contains zero decision, settlement, or evaluation records.
- Therefore a request cannot reach quantitative ISSUE.
- An unresolved exact target returns `PASS / CONTRACT_UNRESOLVED`; a resolved target without an exact ACTIVE model returns `PASS / MODEL_UNAVAILABLE`.
- WATCH/PASS contain no probability-like number, confidence, edge, expected value, stake, yield, P&L or CLV.
- PRICE_ENABLED ISSUE is explicitly disabled in the current release manifest.
- A passing static validator or unit-test run proves only the checks it names. It does not prove full acceptance coverage, calibration, baseline improvement, or profitability.

No document or code can honestly promise that future forecasts will contain no mistakes. The enforceable objective is reproducible evidence, scoped claims, proper evaluation, explicit uncertainty, monitoring, and abstention when proof is missing.

## 4. Development and research artifacts

`SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md` contains non-fitted version 0.1.0 architecture cards. `NEXT_TIME_MODEL_DEVELOPMENT_PLAYBOOK_v1.md` and `RESEARCH_RETROSPECTIVE_2026-07-16.md` are research guidance and retrospective evidence. They are non-authorizing and cannot supply a coefficient, learned parameter, calibration claim, current probability, pick, or ACTIVE status.

The registered source catalog supplies starting points. A source becomes operational only through an exact approved source map with parser, regression, latency, freshness, conflict, licensing and retention evidence.

## 5. Non-operative historical evidence

The following are non-operative and must never supply an active instruction, model coefficient, current probability, KPI, or source-access assumption:

- `combined_sports_doc_v2.txt` and backups;
- `POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md`;
- `AUDIT_AND_CHANGES_2026-06-12.md`;
- `PREDICTION_RESULTS_LOG_v2.md` and `PREDICTION_RESULTS_LOG_v3.md`;
- `SPORTS_CALIBRATION_LEDGER_v2.csv` and derived workbooks;
- `SPORTS_SOURCE_REGISTRY_v2.md`;
- root raw JSON files without complete point-in-time provenance;
- pre-runtime and historical audit outputs except as explicitly labeled evidence.

`PREDICTION_RESULTS_LOG_v4.md` is also pre-runtime evidence. Its four handwritten PASS descriptions were not imported; `PRE_RUNTIME_PASS_MIGRATION_AUDIT_20260716.csv` records that their claimed snapshot hashes and source packets cannot be recomputed from complete canonical artifacts. `PREDICTION_RESULTS_LOG_v5.md` is the empty journal-derived view contract.

The v3 flat CSV ledgers are transport/export shapes, not the machine source of truth. The append-only journal controls runtime identity and lineage.

## 6. Activation change contract

Activation is a reviewed state transition, not a validator side effect. An OPERATIONAL release requires all of the following in the same reviewed bundle:

1. exact unexpired ACTIVE coverage with no ALL or multi-value scope;
2. exact ACTIVE model/version with immutable data, code, feature, model and calibration artifacts;
3. exact effective rules/market/settlement contract and registered authority sources;
4. approved current source map with parser/regression, latency, missingness and conflict evidence;
5. chronological event-disjoint train, tune, calibration and preregistered untouched-test manifests;
6. a SPENT untouched-test result meeting its frozen effect/precision/guardrail rule;
7. a later event-disjoint prospective-shadow result meeting its frozen rule without post-view tuning;
8. full probability-distribution reproduction, calibration/sharpness, typed uncertainty and cross-market coherence evidence;
9. complete frozen candidate-universe and risk-coverage/selective-policy evaluation;
10. hypothesis-family and multiplicity records;
11. exact owner, independent evaluator, approver, review ticket, approval time and expiry;
12. monitoring, integrity suspension, rollback, restart and incident evidence;
13. every mandatory acceptance item either executable and passing or explicitly blocking activation;
14. for PRICE_ENABLED, separate complete price, payoff, staleness, execution and negative-test evidence;
15. a no-clobber release bundle hash and matching `SPORTS_RELEASE_MANIFEST_v1.json` OPERATIONAL declaration.

An ACTIVE model row alone is insufficient; an ACTIVE coverage row alone is insufficient; a prose approval is insufficient. Any incomplete join fails closed.

## 7. Evidence and integrity boundaries

The journal hash chain and local head anchor are tamper-evident, not externally immutable. Detecting coordinated deletion or replacement of both local files requires an independently retained expected head hash and record count. Anchor recovery therefore requires those external values.

The old `outputs/comprehensive_audit_20260716/FILE_INTEGRITY_MANIFEST_20260716.csv` is historical and became stale as live root artifacts changed. Current release claims must cite a no-clobber run under `outputs/runtime_rebuild_20260716/` with tool versions, exact command output, validation JSON, workspace inventory and hashes.

## 8. Rule lifecycle

Hard rules use stable gate IDs, owners, effective dates, pass/fail conditions, evidence and remediation. A viewed test manifest is SPENT for its hypothesis family. Corrections append; they never overwrite a frozen request, prediction, settlement, evaluation, or audit run.

# Sports Research workspace

Specification status: rebuilt and executable on 2026-07-17

Operational status: **SUSPENDED — NO ACTIVE MODELS**

Current authorized quantitative forecasts: **none**

Qualitative live analysis: **ACTIVE_ANALYSIS_ONLY — baseball, cricket, soccer, AFL and NRL**

## Start here

`SPORTS_RESEARCH_AUTHORITY_MANIFEST.md` owns precedence. `SPORTS_RELEASE_MANIFEST_v1.json` is the machine-readable release state. They agree that this workspace is suspended, has zero ACTIVE coverage rows, and cannot publish a probability, edge, expected value, stake, yield, P&L, or CLV claim.

Separately, `SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json` authorizes five deterministic live-state analysis models. They may state `TOSSUP` or a named-side qualitative lean, but they remain uncalibrated and cannot emit a probability or betting claim.

`combined_sports_doc_v3.md` is the portable human operating manual. It now contains the general request, research, logging, retrospective and sport-specific instructions needed for transfer. `PREDICTION_RESULTS_LOG_v5.md` is regenerated from the verified journal as the copy-friendly history.

The honest result for a new request is:

1. `PASS / CONTRACT_UNRESOLVED` if the exact event, rules, market, state, horizon, and settlement contract is not registered;
2. otherwise `PASS / MODEL_UNAVAILABLE` while no exact ACTIVE model and coverage row exists;
3. `WATCH` only when an exact ACTIVE scope exists and a short, named prerequisite can reasonably arrive before expiry;
4. `ISSUE` only after every runtime gate passes under an explicitly reviewed OPERATIONAL release.

## What is executable now

- Draft 2020-12 decision-packet schema compilation and strict nested runtime validation;
- canonical Unicode-normalized JSON and SHA-256 snapshot hashing;
- exact release/coverage/model/contract/source-map/test/shadow joins;
- frozen candidate-universe, point-in-time source-packet, probability, coherence, calibration, uncertainty, price-nullability, and execution-claim gates;
- fail-closed PASS/WATCH packet generation;
- tamper-evident append-only decision, settlement, and evaluation journal with a local head anchor;
- proper-score and branch-payoff primitives;
- chronological development-plan checks, paired event-cluster bootstrap, risk-coverage analysis, Holm decisions, and spent-test bookkeeping;
- adversarial Node tests, a static specification validator, and a combined system-validation command.

These controls can reject unsupported work. They do not establish that a real model is accurate.

## Commands

Requires Node.js 20+ and PowerShell.

```powershell
npm install
npm test
npm run validate
npm run verify-store
```

Run a fresh-source qualitative live analysis:

```powershell
node scripts/sportsctl.mjs analyse-live --input templates/live_analysis_cricket.template.json --output runtime/latest_analysis.json
```

The command records the frozen input/output and regenerates the prediction log by default. `--no-record` is for explicit tests or drafts only.

Create a fail-closed request after replacing every template sentinel:

```powershell
node scripts/sportsctl.mjs new-request --input templates/next_request.template.json --output runtime/next_decision_packet.json
node scripts/sportsctl.mjs render-log
```

The template is intentionally not runnable unchanged. Verbatim request text, one exact primary question, and a real creator are required. `new-request` will not invent them. A valid generated decision is journaled and rendered into the prediction log by default; use `--no-record` only for explicit draft construction.

For a delivered ranked card, create a structured user-facing record from `templates/publication.template.json` and either pass it to `new-request --publication FILE` or run `sportsctl publish --input FILE`. This preserves the exact ranking and potential winner in the generated log even when the formal decision is PASS.

Journal recovery is deliberately explicit. A missing/stale local anchor is not automatically blessed; recovery requires an independently retained expected head hash and record count.

## Authority and artifact map

| Purpose | File | Current truth |
| --- | --- | --- |
| Precedence and claims | `SPORTS_RESEARCH_AUTHORITY_MANIFEST.md` | Canonical authority; suspended |
| Machine release state | `SPORTS_RELEASE_MANIFEST_v1.json` | `SUSPENDED`, zero ACTIVE scopes |
| Qualitative analysis models | `SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json`, `SPORTS_ACTIVE_ANALYSIS_MODELS_v1.md` | Five `ACTIVE_ANALYSIS_ONLY` LIVE models; numeric claims prohibited |
| Exact operational allowlist | `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` | 15 DEVELOPMENT architecture scopes, one UNSUPPORTED catch-all, zero ACTIVE |
| Model registry | `SPORTS_MODEL_REGISTRY_v1.csv` | DEVELOPMENT records only |
| Contract/source/test controls | `schema/contract_registry_v1.csv`, `schema/source_maps_v1.csv`, `schema/test_evaluations_v1.csv` | Header-only; no approved evidence rows |
| Source starting points | `SPORTS_REGISTERED_SOURCES_v1.csv`, `SPORTS_SOURCE_REGISTRY_v3.md` | Research catalog, not approved model source maps |
| Operating policy | `combined_sports_doc_v3.md` | Universal workflow and hard gates |
| Data contract | `SPORTS_DATA_DICTIONARY_v3.md`, `schema/decision_packet.schema.json` | Normalized definitions plus compiled packet schema |
| Validation and scoring | `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md`, `SPORTS_SCORING_SPECIFICATION_v3.md` | Development/evaluation standards |
| Acceptance contract | `SPORTS_ACCEPTANCE_TESTS_v3.md`, `schema/acceptance_traceability_v1.csv` | Requirements plus honest executable-coverage status |
| Future operating sequence | `NEXT_TIME_MODEL_DEVELOPMENT_PLAYBOOK_v1.md` | Non-authorizing practical playbook |
| Retrospective | `RESEARCH_RETROSPECTIVE_2026-07-16.md` | What failed, what changed, what remains unproved |
| Runtime | `src/`, `scripts/sportsctl.mjs` | Fail-closed implementation |
| Machine record | `runtime/store/journal.jsonl`, `runtime/store/head_anchor.json` | Append-only decisions, qualitative analyses, settlements and evaluations |
| Human-readable result view | `PREDICTION_RESULTS_LOG_v5.md` | Generated copy-friendly view of every recorded decision and qualitative analysis |

## Current empirical truth

- Active models: 0.
- Active analysis-only live models: 5.
- Runtime decision records: 3 at the 2026-07-17 consolidation cutoff; use `verify-store` for the current count.
- Calibration-eligible predictions: 0.
- Approved contract rows: 0.
- Approved source-map rows: 0.
- Spent untouched-test reports: 0.
- Prospective-shadow reports: 0.
- Price-enabled ISSUE support: disabled.

The 437-row legacy CSV and 449-row latest workbook are retrospective, inconsistent populations. The apparent workbook record (253 wins, 190 losses, two pushes) is not a verified prospective hit rate. In the older CSV, 300 of 437 rows are exact complement-pair entries. Creation-time source/model artifacts, prices, executions, and immutable cutoffs are insufficient for calibration or profitability claims.

All legacy rows remain excluded. The four handwritten PASS descriptions in `PREDICTION_RESULTS_LOG_v4.md` are also pre-runtime evidence only; `PRE_RUNTIME_PASS_MIGRATION_AUDIT_20260716.csv` records why their claimed hashes and source packets cannot be reconstructed and why they were not silently imported.

## Development path

Use `NEXT_TIME_MODEL_DEVELOPMENT_PLAYBOOK_v1.md`. Start with one narrow competition/market/state/horizon—not all sports. Required evidence includes:

- exact effective contract and approved point-in-time source map;
- dataset datasheet and immutable event manifests;
- chronological event-disjoint train, tune, calibration, untouched-test, and later prospective-shadow periods;
- frozen baseline and identical evaluation population;
- complete probability distributions, calibration/sharpness evidence, typed uncertainty, and cross-market coherence;
- complete candidate-universe and selective risk/coverage reporting;
- hypothesis-family/multiplicity control and a spent-test ledger;
- named owner, independent evaluation, review, expiry, monitoring, suspension, rollback, and restart rules.

Only a reviewed change that makes the release manifest OPERATIONAL and adds complete exact ACTIVE machine evidence can authorize ISSUE. A passing unit test, architecture card, source URL, static validator, or historical percentage cannot.

## Audit evidence

`outputs/comprehensive_audit_20260716/` is a historical July audit bundle. Its retained outputs describe the legacy artifacts, but its root-file integrity inventory became stale after the rebuild and its analysis tooling has documented defects. Do not cite it as the current release manifest.

Current no-clobber validation evidence is generated under `outputs/runtime_rebuild_20260716/`. Each run contains tool versions, command output, a system-validation JSON report, and SHA-256 inventories. Failed runs remain evidence and are not overwritten.

The journal is tamper-evident relative to its anchor; it is not an external immutable ledger. Retain journal head/count anchors independently for stronger deletion detection.

# Research workspace

**Carryover review published to Part 7:** [65 reviews and mapping/source corrections](verification/carryover_review_2026-10-08/REPORT.md) retain all unresolved obligations and consume no canonical ID. The supplied local P-550 is source-only and pending import; canonical next P-550 and local next P-551 are distinct.

**October 8 current destination:** [Part 7](../prediction%20logs/PREDICTION_LOG_COMBINED_7.md) is active, with P-550 unconsumed. Part 6 retains P-523–P-549 and immutable special source custody. [Settlement/rollover evidence](verification/mini_rollover_2026-10-08/REPORT.md) and the selected 65-record carryover supersede earlier queue counts. `log_card addendum revision.json` appends a dated revision under its existing `card_id`; it never consumes a new ID.

Current October-5 all-log custody: 111 receipt bodies verify locally; 52 are intentionally excluded from Git (42 prior benchmark bodies plus 10 new restricted/market-bearing narrative captures). A clean checkout has 59 bodies and must fail strict custody for the other 52; no CI bypass or fabricated recapture is authorized. See the all-log source inventory and publication evidence.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current controls: [CURRENT_RULES.md](../CURRENT_RULES.md). No current model is live-qualified. Existing September evaluations and forecasts remain frozen; October's changed models are versioned SHADOW_ONLY candidates.

Current reconciliation: [all-log October 5 evidence](verification/all_log_resolution_2026-10-05/REPORT.md). The earlier [document/cleanup evidence](verification/implementation_2026-10-05/REPORT.md) is a completed historical checkpoint. P-523–P-537 are already canonical; P-538 was next at that historical repair; after the October 8 import, P-550 is next, subject to the live allocator. The two closed mini archives, all 15 carryovers, eleven diagnostic settlements and 132 retrospective sections are retained. No reimport, new certification or forecast rewrite is needed.

## Local-mini lifecycle — current default (CR-2026.10.09-R2)

Cards are written into a local mini by an external chat agent, settled locally, and imported here. The prompts are in [prompts/](prompts/README.md) and the format is [`mini-log-2`](../CARD_AND_LOG_TEMPLATES.md#local-mini-format-mini-log-2).

```powershell
# Local checks on a mini (any machine with the repository)
py -3.14 -B -m research.operations.mini_log verify "<mini>.md"
py -3.14 -B -m research.operations.mini_log next-id "<mini>.md" --repo-next P-NNN
py -3.14 -B -m research.operations.mini_log join "<ORIGINAL_MINI>/<frozen>.md" "<SETTLEMENT_SECTION>.md" --out "<settled>.md"
py -3.14 -B -m research.operations.mini_log verify-settled "<ORIGINAL_MINI>/<frozen>.md" "<settled>.md"
# Canonical import (prompt 4): plan is read-only; apply keeps every working ID or stops
py -3.14 -B -m research.operations.import_mini plan  --frozen F.md --settled S.md --out research/verification/mini_import_<P-AAA>_<P-BBB>_<date>
py -3.14 -B -m research.operations.import_mini apply --frozen F.md --settled S.md --out research/verification/mini_import_<P-AAA>_<P-BBB>_<date>
# Combined Log rollover (prompt 5): consumes no ID; then issue a new control manifest
py -3.14 -B -m research.operations.rollover plan
py -3.14 -B -m research.operations.rollover apply --main-head <40-hex SHA>
# Cohort retrospective (prompt 6): Rule T2 scoreboard from every retained settlement table
py -3.14 -B -m research.operations.cohort_review --out research/verification/retrospective_<date>/all [--from P-N] [--to P-M]
```

`import_mini apply` commits each card's exact block bytes through `log_card` (lock, journal, readback). It then appends the mini's `ADDENDUM` blocks and each settlement as dated addenda under the same ID, so a re-run commits nothing twice. `PENDING_EVENT` cards are imported without a settlement and carried into the next mini.

## Requested analyses and canonical logging — current default

Every requested sport receives evidence-based analysis and canonical logging to the active combined log regardless of model qualification or calibration. Qualitative ranks and explicitly uncalibrated reproducible analyst scenarios are allowed. Late news and after-start analysis are allowed with honest observation/log times. Missing calibration, fixture-universe registration or independence audits are labels and limits, not analysis/logging blockers. The certified-issuer sections below describe a separate performance protocol.

```powershell
py -3.14 -B -m research.operations.log_card next-id
py -3.14 -B -m research.operations.log_card commit path/to/card.json
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.log_card recover
```

Card JSON includes event_key, native_event_id, league, title, tracking_handle, analysis_status, original source_path and complete Markdown body. Research commits share the canonical ledger hash chain and writer lock, using distinct RESEARCH_LOG record types. Retained originals and exact per-part projections are hashed and read back. Duplicate imports return the same ID. Interrupted appends must be recovered before another ID; recovery refuses unrelated changes. Import minis into the configured active combined log and leave canonical pointers, without maintaining competing active copies. Do not backdate imports or manufacture previous predictions. No retrospective until requested.

Use `py -3.14 -B -m research.operations.control_freeze --verify` for METHOD's selected receipt. `py -3.14 -B -m research.operations.verify_custody` additionally checks research-card projections and alternate imported source-receipt fields in memory. Original receipts, frozen acceptance code and model dependencies remain unchanged. Research source/projection stores have their own ledger hashes and are excluded from the static control freeze.

After a reference mini closes, run `py -3.14 -B -m research.operations.log_card refresh-status` to update the living queue through the same verified workflow. Historical absolute canonical research-store paths are resolved in the current checkout and still require their original hashes; new records use relative store paths. The October 5 archived references, entry accounting and unresolved carryover are in [the closure report](verification/closure_2026-10-05/REPORT.md). Keep carryover IDs; do not reissue those events.

## Install and verify

The implementation was tested with CPython 3.14.6 and the exact [dependency lock](requirements.lock.txt). Use an isolated environment when installing; do not replace unrelated project runtimes.

```powershell
python -m pip install -r research/requirements.lock.txt
python -B -m pytest -p no:cacheprovider research/tests research/operations -q
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m research.operations.verify_reconciliation
py -3.14 -B -m research.operations.verify_all_logs
py -3.14 -B -m research.operations.control_freeze --verify
```

Tests are offline and check temporal leakage, contract coherence, source hashes, native parsers, evidence admission, transaction recovery, settlement revision custody and persistent pilot decisions. Live observations are separate from tests.

## Daily observations and shadows

```powershell
python -B -m research.src.daily --window-hours 48
python -B -m research.operations.workflow status
python -B -m research.operations.workflow score
```

A unique `research/daily/<UTC>/` directory contains each lane's raw-source receipt, processed scores, upcoming and excluded fixtures, snapshot hash, model shadows, complete fixture coverage and run status. Fresh score inputs are single-publisher provisional observations; this is model research, not certified issuance. EPL retains provider-derived IDs separately from missing official IDs. NBL uses the league's exact UUID. Failed sources or parsers create recorded FAILED_CLOSED lanes and a nonzero exit.

The daily job records new coherent EPL 1X2 and NBL ML shadows within 48 hours. It checks the complete model-build and historical-input receipts before fitting. New NBL terminal results can produce diagnostic grades for the unchanged September shadows; a single final source does not certify actual start or three independent lineages. Old shadows are never overwritten.

`current.py` and `nbl_current.py` are compatibility commands for dated immutable source snapshots. They cannot backdate source retrieval or rewrite the September 29 static files. `draft_epl.py` and `nbl_shadow.py` preserve older shadow bridges for reproducibility; their output is not canonical issuance. Prefer the dated daily workflow for new v2 candidate research.

## Models and experiments

| Model | Description | Operational status |
|---|---|---|
| epl-dc-0.1.0 | Original Dixon-Coles comparison model | Historical 1X2 holdout; SHADOW_ONLY |
| epl-coherent-ensemble-0.2.0 | 0.75 DC + 0.25 TB1 score matrix; coherent family arithmetic | Development-selected 1X2 candidate; SHADOW_ONLY |
| nbl-joint-0.1.0 | Original joint margin/total ridge model | Historical overtime-inclusive ML holdout; SHADOW_ONLY |
| nbl-oof-width-0.2.0 | Joint-model margin mean; width from strictly earlier out-of-fold residuals | Development-selected overtime-inclusive ML candidate; SHADOW_ONLY |

The [October protocol](runs/implementation_2026-10-01/development_protocol.json), [family results](runs/implementation_2026-10-01/family_diagnostics.json) and forecast CSV record five EPL candidates across 1X2/total-2.5/BTTS and four NBL ML candidates over chronological folds. Comparators include population scores, TB1-MD and fixed Elo. Calibration is reported with uncertainty; no calibrator trained on final test outcomes is deployed. October experiments use already opened data and do not create new untouched holdout evidence.

The old tuning and holdout commands refuse overwrite. Previous evaluation code and run bytes are retained in [implementation custody](custody/implementation_2026-10-01/manifest.json). [Model-build receipts](model_builds/current.json) pin all numerical and operational dependencies and exact runtime packages. An intentional numerical edit requires a new version, fresh dated experiment and rebuilt receipt.

## Evidence and real issuance

The canonical ledger is `research/canonical_ledger.jsonl`, created only when a genuine universe/action is registered. `sources_registry.json` defines allowed routes, parser/league/endpoint scope, official ownership and collector independence. UNKNOWN independence fails live admission. `admission_registry.json` scopes each model version and contract family. Neither a handwritten VALIDATED flag nor a generic M2_PASS promotes a model.

```powershell
python -B -m research.operations.workflow validate-bundle <bundle.json>
python -B -m research.operations.workflow register-universe <universe.json>
python -B -m research.operations.workflow prepare-issue <bundle.json> <new-transaction.json>
python -B -m research.operations.workflow commit-issue <transaction.json> --real
python -B -m research.operations.workflow settle <terminal-bundle.json> --reason "Exact terminal evidence appended"
```

These are operator commands for future qualified real events. Preparation writes a concrete draft without consuming an ID. Commit defaults to disabled unless `--real` is passed; it revalidates exact cached evidence under a lock and appends a journaled core to the active combined log. Source-state freshness is capped at five minutes. All three independently audited pregame lineages must agree, including one official source. Native NBL/MLB/ESPN JSON parsers check actual body identity. Other source mappings require a retained parser audit. Event-specific collector audits bind the event, body hash and upstream lineage.

Terminal admission additionally requires final-score agreement across three independent lineages and a source field explicitly audited as actual start. Schedule time and first play are not silently substituted. Corrections append chained revisions against the unchanged issue core. Recovery completes an exact pending projection and prevents ID reuse; it never edits issued bytes.

## Pilot and remaining evidence

The [pilot template](PILOT_LOCK_TEMPLATE.json) is NOT_FROZEN. `pilot.py` supports the fixed seven-contract EPL composite only after all those families are LIVE_QUALIFIED. It validates the frozen universe and source-backed power plan, enrols the first chronological adjusted issues, waits on earlier unsettled cohort members, uses at least four week blocks, records a single interim and makes futility terminal. NBL or a different family score needs a separately versioned scoring protocol.

No live pilot is started by this implementation. Existing family evidence, source independence and actual-start coverage are insufficient for that claim. Missing future shadows and real outcomes cannot be implemented by inventing records.

## Historical learning and archive

The frozen 522-slot `SETTLED_OUTCOMES_LEDGER.csv` remains an original index; missing fields remain blank. The original rank CSV is richer. [Normalized contracts](data/processed/legacy_learning/contracts.csv), [cards](data/processed/legacy_learning/cards.csv) and [manifest](data/processed/legacy_learning/manifest.json) retain all 2,004 literal rank rows, 630 probabilities and uncertainty/conflict dispositions. All rows remain performance-ineligible. Historical source pointers reference preserved logs; a path/line check is not independent result truth.

```powershell
python -B -m research.src.archive validate
python -B -m research.src.archive build
```

The archive guide explains canonical event grain, source receipt joins, season status, deduplication, mirrors/subsets and narrative separation. Use `research.src.archive.read_events(eligible_only=True, verify=True)` for source-checked historical labels, then apply `point_in_time` availability/endpoint gates before an as-of feature query. Most historical availability timestamps are unknown. Do not treat retrieval today as pregame availability years ago.

Full custody reports every missing/hash-invalid/length-invalid receipt body and returns nonzero for any failure. There is no clean-checkout bypass. At this repair all 78 receipt bodies verify locally, while 42 are local-only benchmark bodies excluded from Git; an export containing tracked bodies alone fails their custody checks. CI runs freeze verification even after custody failure and retains an overall failure. Do not refetch a different body or publish quarantined bytes to mask that gap.

Restricted Football-Data/FixtureDownload snapshots remain local under ignored `data/benchmark/`. The source registry prohibits automated retrieval through those restricted/manual routes. Forecast modules read processed sports-only columns; post-event market benchmark code is isolated. Raw historical rebuilds that require missing local restricted files fail clearly.

Baseline provenance is mandatory for certified admission: exact lane/league/endpoint/families/version, a pinned approved definition and code artifacts, approval strictly before cutoff, and matching distribution/holdout/shadow/pilot comparator. Hash joins verify retained bytes and declared metadata; they do not independently prove every declared input availability time or recompute every distribution. Review the original source field and baseline construction. The point-in-time feature filter likewise labels declared metadata and cannot confer live admission by itself.

Sports-only historical CSV exports for the active lanes are [EPL results](data/processed/league_csv/epl_results.csv), [NBL results](data/processed/league_csv/nbl_results.csv), and their [manifest](data/processed/league_csv/manifest.json). These retain 2,280 and 738 reconciled historical scores, with official IDs missing for EPL and availability/actual-start gaps explicitly preserved. Do not mistake them for populated Soccer/Basketball archive yearly files.

Publication readback: 152 ignored local cache files listed in the full local control freeze remain absent from Git. The first publication also had one workflow line-ending mismatch, corrected with byte-preserving Git attributes. Remote validation remains incomplete; the local freeze does not establish clean-checkout evidence availability. The exact paths are retained in `research/verification/all_log_resolution_2026-10-05/published_freeze_inventory.json`.

## Fifteen experiment measures and next steps

[The measure register](experiment_measures.json) and [execution guide](experiments/NEXT_STEPS.md) cover all fifteen retrospective proposals. Run `py -3.14 -B -m research.experiments.runner verify` or `status` from the repository root. The CLI supplies template, source-backed power planning, immutable protocol freeze, real-time forecast capture and complete-cohort evaluation. It never creates canonical IDs or promotes models. Follow the guide for exact artifact fields, experiment-specific measures and every next step. Original proposal statuses remain PROPOSED_NOT_TESTED; zero actual experiments were run at registration.

## Rollover and the frozen certified issuer

`research/src/issue.py`, `research/src/workflow.py` and `research/src/acceptance.py` are immutable model-pinned historical implementations. Current issuer and operator entry points are `research.operations.canonical_issue` and `research.operations.workflow`; their isolated module namespaces reuse frozen validation/transaction functions with the active-log custody and shared allocator. Historical modules remain available for reproduction and are not current append entry points. The logger defaults dynamically to `research/current_combined_log.json`. Existing preparations keep their recorded part; new ledger preparations retain the combined-log path. Never roll over with a pending transaction.

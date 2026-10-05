# Research workspace

Current October-5 all-log custody: 111 receipt bodies verify locally; 52 are intentionally excluded from Git (42 prior benchmark bodies plus 10 new restricted/market-bearing narrative captures). A clean checkout has 59 bodies and must fail strict custody for the other 52; no CI bypass or fabricated recapture is authorized. See the all-log source inventory and publication evidence.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current controls: [CURRENT_RULES.md](../CURRENT_RULES.md). No current model is live-qualified. Existing September evaluations and forecasts remain frozen; October's changed models are versioned SHADOW_ONLY candidates.

Current reconciliation: [all-log October 5 evidence](verification/all_log_resolution_2026-10-05/REPORT.md). The earlier [document/cleanup evidence](verification/implementation_2026-10-05/REPORT.md) is a completed historical checkpoint. P-523–P-537 are already canonical; P-538 is next at this repair, subject to the live allocator. The two closed mini archives, all 15 carryovers, eleven diagnostic settlements and 132 retrospective sections are retained. No reimport, new certification or forecast rewrite is needed.

## Requested analyses and canonical logging — current default

Every requested sport receives evidence-based analysis and canonical Part 6 logging regardless of model qualification or calibration. Qualitative ranks and explicitly uncalibrated reproducible analyst scenarios are allowed. Late news and after-start analysis are allowed with honest observation/log times. Missing calibration, fixture-universe registration or independence audits are labels and limits, not analysis/logging blockers. The certified-issuer sections below describe a separate performance protocol.

```powershell
py -3.14 -B -m research.operations.log_card next-id
py -3.14 -B -m research.operations.log_card commit path/to/card.json
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.log_card recover
```

Card JSON includes event_key, native_event_id, league, title, tracking_handle, analysis_status, original source_path and complete Markdown body. Research commits share the canonical ledger hash chain and writer lock, using distinct RESEARCH_LOG record types. Retained originals and exact Part 6 projections are hashed and read back. Duplicate imports return the same ID. Interrupted appends must be recovered before another ID; recovery refuses unrelated changes. Import minis into Part 6 and leave canonical pointers, without maintaining competing active copies. Do not backdate imports or manufacture previous predictions. No retrospective until requested.

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
python -B -m research.src.workflow status
python -B -m research.src.workflow score
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
python -B -m research.src.workflow validate-bundle <bundle.json>
python -B -m research.src.workflow register-universe <universe.json>
python -B -m research.src.workflow prepare-issue <bundle.json> <new-transaction.json>
python -B -m research.src.workflow commit-issue <transaction.json> --real
python -B -m research.src.workflow settle <terminal-bundle.json> --reason "Exact terminal evidence appended"
```

These are operator commands for future qualified real events. Preparation writes a concrete draft without consuming an ID. Commit defaults to disabled unless `--real` is passed; it revalidates exact cached evidence under a lock and appends a journaled core to Part 6. Source-state freshness is capped at five minutes. All three independently audited pregame lineages must agree, including one official source. Native NBL/MLB/ESPN JSON parsers check actual body identity. Other source mappings require a retained parser audit. Event-specific collector audits bind the event, body hash and upstream lineage.

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

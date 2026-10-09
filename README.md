# Sports Research

**October 9 final settlement, rules and retrospective:** All 72 pending records (the 65-record carryover plus P-550–P-556) are settled in Part 7. Missing details were settled on a declared evidence hierarchy, no ID was consumed, and the next ID stays P-557. New rules: only Rank 1 and Rank 2 count as wins (T2); every Rank-1 failure gets a deep retrospection (R1, 28 written); supplied contracts are reference only and the analyst derives its own top two out of four from the event distribution (P4). See [the settlement report](research/verification/final_settlement_2026-10-09/REPORT.md) and the [framework retrospective and improvement plan](FRAMEWORK_RETROSPECTIVE_2026-10-09.md), whose recommendations are not yet implemented.

**Carryover review published to Part 7:** [65 reviews and mapping/source corrections](research/verification/carryover_review_2026-10-08/REPORT.md) retain all unresolved obligations and consume no canonical ID. The supplied local P-550 is source-only and pending import; canonical next P-550 and local next P-551 are distinct.

**October 8 settlement and rollover:** P-538–P-549 were imported without renumbering into Part 6, with original text and dated sporting retrospectives. Part 7 is now active; P-550 remains next and no ID was consumed by its creation. The selected carryover has 65 exact records, including four P-540 retirement rows with UNKNOWN_DEFINITION. See [the complete settlement/rollover review](research/verification/mini_rollover_2026-10-08/REPORT.md).

**Local authority, numerical ML runtime and all-log reconciliation (October 6):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current method: **MDS-2026.10.09-v8.1**; controls: **CR-2026.10.09-R1** (with numerical runtime extension **CR-2026.10.06-NUMERICAL-1**). Requested analyses and canonical logging to the active combined log proceed regardless of calibration, with qualitative ranks or explicitly uncalibrated reproducible scenarios and honest live/late timestamps. Model qualification controls performance claims separately. This repository contains sports-only research, historical competition records, preserved prediction logs, and an authoritative numerical machine learning runtime.

## Start here

1. Read [current operating rules](CURRENT_RULES.md), then [the research workspace](research/README.md) and [the numerical runtime](runtime/README.md).
2. Consult the [Numerical Model Register](NUMERICAL_MODEL_REGISTER.md), [H0 Dataset Card](H0_DATASET_CARD.md), and [Data Source Register](DATA_SOURCE_REGISTER.md).
3. Use [the October 5 implementation evidence](research/verification/implementation_2026-10-05/REPORT.md) for historical reconciliation and verification.
4. Use [source contracts](research/sources_registry.json) and [admission registrations](research/admission_registry.json). A URL list or metadata flag cannot confer eligibility.
5. Use [the archive guide](Previous%20Sports%20Results/README.md) for historical CSVs, coverage, provenance and exclusions across all eight sports.
6. Use [templates](CARD_AND_LOG_TEMPLATES.md), [scoring](SCORING_AND_VALIDATION.md) and [verification](VERIFICATION_PROTOCOL.md) when preparing a forecast or evaluating a result.

```powershell
py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations runtime/tests -q
python -B -m research.src.daily --window-hours 48
python -B -m research.operations.workflow status
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m research.operations.verify_reconciliation
py -3.14 -B -m research.operations.verify_all_logs
```

The daily command creates dated immutable observations, model-only shadows, fixture coverage and diagnostic grades. It never issues a P-number or promotes a model. A source failure produces a recorded failure and a nonzero command exit.

## Evidence streams & Numerical Architecture

| Stream | Authority | Limits |
|---|---|---|
| Issued forecasts | Preserved Parts 1-6; future hash-chained issuer transactions | Old forecasts retain their original numbers and method; retrospective repair never creates prospective skill |
| Historical learning | Original rank CSV plus `research/data/processed/legacy_learning/` | Literal grades, unresolved conflicts and missing cutoffs remain explicitly labelled; every historical row is performance-ineligible |
| H0 Training Datasets | Independent population feature store (`H0_DATASET_CARD.md`) | D0 is frozen; model training uses declared populations with point-in-time safety ($known\_at \le cutoff\_at$) |
| Numerical Runtime | `runtime/` (A0–A8, BigQuery AI/ML, Monte Carlo Simulators) | Distribution-first event forecasting; contracts derived from underlying PMF; rolling-origin cross-validation |
| Statistical experiments | Frozen `research/runs/`, versioned model builds | Old holdouts are preserved. October comparisons use opened data and are development evidence |
| Prospective shadows | `research/shadow/` and dated `research/daily/` | No issued card, verified lineup or live qualification is implied |
| League archive | `Previous Sports Results/_canonical/` and its manifest | Exact-source matches, duplicates, mirror copies, unknown seasons and postgame narratives are separated |

Parts 1-5 remain historical. [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md) is the sole canonical destination for new issued cards. P-518 through P-522 remain reserved and excluded from performance; P-523–P-537 are canonical research records; the verified next ID at this repair is P-538. Always read the live allocator before issuance. The [status register](GAME_LOG_STATUS_CURRENT.md) links both closed mini archives and all 15 unresolved carryover records. Eleven diagnostic settlements and 132 retrospective sections remain learning evidence, with zero certified/performance-eligible settlements. Closed minis cannot assign IDs.

## Supported Sports & Numerical Pipelines (8 Sports)

1. **Cricket**: Test session/day discrete run & wicket distributions + Limited-overs ball/phase resource model.
2. **Basketball (NBA/International)**: Possessions × Efficiency joint score model yielding bivariate distribution.
3. **American Football (NFL/College)**: Drive-level Markov chain simulation generating discrete score PMFs.
4. **Baseball (MLB/KBO/NPB)**: PA-level base-out transition, starter hook model, and bullpen degradation chains.
5. **Australian Rules (AFL)**: Territory → Inside 50 → Scoring shots → Conversion pipeline.
6. **Rugby League (NRL)**: Sets → Field position → Try opportunities → Tries and conversions pipeline.
7. **Soccer**: Bivariate Poisson/NegBinomial goal distributions + independent corners process + player SOT.
8. **Ice Hockey (NHL/AHL)**: Shot attempts → Unblocked shots → xG → Goals with goalie quality and empty-net tail.

## BigQuery AI & ML Integration

The numerical runtime features built-in integration with Google Cloud BigQuery AI & ML:
- Cloud-native time-series forecasting via BigQuery ML (`ARIMA_PLUS`, `AI.FORECAST`).
- Vertex AI remote model integration for text analysis and injury extraction.
- SQL-driven feature engineering and analytical contract validation alongside the local DuckDB/Parquet engine.

## Custody and publication

The October overhaul was explicitly authorized by the user. Original controlling files and prior run artifacts are preserved under `research/custody/implementation_2026-10-01/`; archive corrections have their own custody journal. [METHOD.md](METHOD.md) identifies the active method and control revision. Restricted or odds-bearing raw files remain in the ignored benchmark quarantine; permitted source bodies and receipts stay auditable. No commit, push, deployment or recurring automation is performed by the daily command.


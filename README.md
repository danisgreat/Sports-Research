# Sports Research

**Current state:** [CURRENT_STATE.md](CURRENT_STATE.md) is generated from the repository and is the one place that states what is true now: method, control revision, active freeze, next canonical ID, active Combined Log, scoreboard, runtime evidence and source status. Rules in force: only Rank 1 and Rank 2 count as wins (T2); every Rank-1 failure gets a deep retrospection (R1); supplied contracts are reference only and the analyst derives its own top two out of four from one event distribution (P4). The [framework retrospective](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) lists every recommendation with its implementation status (§5.8). Dated status notes that earlier versions of this page carried are kept verbatim in [archive/status_notes/](archive/status_notes/SUPERSEDED_STATUS_PARAGRAPHS_2026-10-09.md).

Current method: **MDS-2026.10.09-v8.3**; controls: **CR-2026.10.09-R3** (with numerical runtime extension **CR-2026.10.06-NUMERICAL-1**). Operator prompts for the local-mini lifecycle (start mini → cards → settle → import → roll over → retrospective) are in [research/prompts/](research/prompts/README.md). Requested analyses and canonical logging to the active combined log proceed regardless of calibration, with qualitative ranks or explicitly uncalibrated reproducible scenarios and honest live/late timestamps. Model qualification controls performance claims separately. This repository contains sports-only research, historical competition records, preserved prediction logs, and an authoritative numerical machine learning runtime.

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
py -3.14 -B -m research.operations.dev_check            # every CI step, in CI order (needs the interpreter pinned in .python-version)
py -3.14 -B -m research.operations.current_state verify # CURRENT_STATE.md is fresh and no living document states a next ID
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

Parts 1-6 are historical, custody-hashed records; the active Combined Log is named in [CURRENT_STATE.md](CURRENT_STATE.md) and in `research/current_combined_log.json`. P-518 through P-522 remain reserved and excluded from performance; P-523 onward are canonical research records. Always read the live allocator (`log_card next-id`) before issuance. The [status register](GAME_LOG_STATUS_CURRENT.md) links the closed mini archives and every unresolved carryover record. Diagnostic settlements and retrospective sections remain learning evidence, with zero certified or performance-eligible settlements. Closed minis cannot assign IDs.

## Supported sports and numerical pipelines (9 engines)

1. **Cricket**: exact innings dynamic program over overs and wickets with the chase stopping rule, toss branch and reduced-overs resource ratio. Not fitted: the archive holds scorecards, not ball-by-ball data.
2. **Basketball (NBA/international)**: possessions × efficiency joint score with a Student-t margin and total, league-specific support (no NBA default for other leagues).
3. **American football (NFL/college)**: drive-level scoring with 6-, 7- and 8-point drives and key-number mass validated out of sample.
4. **Baseball (MLB/KBO/NPB)**: starter and bullpen run mixtures with a starter-leash mixture, a conditional bottom of the ninth, and tie-league handling.
5. **Australian rules (AFL/AFLW)**: scoring shots × conversion with points = 6 × goals + behinds.
6. **Rugby league (NRL)**: total tries (Conway–Maxwell–Poisson) with a negatively dependent home share, kicking, and a half-time distribution.
7. **Soccer**: Dixon–Coles score matrix with separate half rates, plus an independent negative-binomial corners model that requires a settlement provider.
8. **Ice hockey (NHL)**: goalie-adjusted regulation goals, a coherent full-game endpoint (OT/SO resolved) and an empty-net late-game state.
9. **Tennis**: exact point-to-match tree with serve order and a match-level form effect. Not fitted: the archive holds results, not serve-point counts.

## BigQuery integration (reduced scope)

`runtime/src/common/bigquery_ml.py` generates SQL text only and never connects to BigQuery. It is limited to point-in-time feature joins and `BOOSTED_TREE` challengers trained on the H0 feature tables; time-series forecasting of match outcomes (`ARIMA_PLUS`, `AI.FORECAST`) is not offered because outcomes are not a single autocorrelated series. The project and dataset come from the constructor or `SPORTS_BQ_PROJECT` / `SPORTS_BQ_DATASET`; none is hard-coded. See [NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md) section 6.

## Custody and publication

The October overhaul was explicitly authorized by the user. Original controlling files and prior run artifacts are preserved under `research/custody/implementation_2026-10-01/`; archive corrections have their own custody journal. [METHOD.md](METHOD.md) identifies the active method and control revision. Restricted or odds-bearing raw files remain in the ignored benchmark quarantine; permitted source bodies and receipts stay auditable. No commit, push, deployment or recurring automation is performed by the daily command.


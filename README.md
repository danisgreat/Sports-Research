# Sports Research

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current method: **MDS-2026.10.01-v7.1**; controls: **CR-2026.10.05-I5**. Requested analyses and canonical Part 6 logging proceed regardless of calibration, with qualitative ranks or explicitly uncalibrated reproducible scenarios and honest live/late timestamps. Model qualification controls performance claims separately. This repository contains sports-only research, historical competition records and preserved prediction logs.

## Start here

1. Read [current operating rules](CURRENT_RULES.md), then [the research workspace](research/README.md).
2. Use [the October 5 implementation evidence](research/verification/implementation_2026-10-05/REPORT.md) for current reconciliation, cleanup and verification. The [October 1 report](IMPLEMENTATION_2026-10-01.md) retains its historical results.
3. Use [source contracts](research/sources_registry.json) and [admission registrations](research/admission_registry.json). A URL list or metadata flag cannot confer eligibility.
4. Use [the archive guide](Previous%20Sports%20Results/README.md) for historical CSVs, coverage, provenance and exclusions.
5. Use [templates](CARD_AND_LOG_TEMPLATES.md), [scoring](SCORING_AND_VALIDATION.md) and [verification](VERIFICATION_PROTOCOL.md) when preparing a forecast or evaluating a result.

```powershell
py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations -q
python -B -m research.src.daily --window-hours 48
python -B -m research.src.workflow status
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m research.operations.verify_reconciliation
py -3.14 -B -m research.operations.verify_all_logs
py -3.14 -B -m research.operations.control_freeze --verify
```

The daily command creates dated immutable observations, model-only shadows, fixture coverage and diagnostic grades. It never issues a P-number or promotes a model. A source failure produces a recorded failure and a nonzero command exit.

## Evidence streams

| Stream | Authority | Limits |
|---|---|---|
| Issued forecasts | Preserved Parts 1-6; future hash-chained issuer transactions | Old forecasts retain their original numbers and method; retrospective repair never creates prospective skill |
| Historical learning | Original rank CSV plus `research/data/processed/legacy_learning/` | Literal grades, unresolved conflicts and missing cutoffs remain explicitly labelled; every historical row is performance-ineligible |
| Statistical experiments | Frozen `research/runs/`, versioned model builds | Old holdouts are preserved. October comparisons use opened data and are development evidence |
| Prospective shadows | `research/shadow/` and dated `research/daily/` | No issued card, verified lineup or live qualification is implied |
| League archive | `Previous Sports Results/_canonical/` and its manifest | Exact-source matches, duplicates, mirror copies, unknown seasons and postgame narratives are separated |

Parts 1-5 remain historical. [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md) is the sole canonical destination for new issued cards. P-518 through P-522 remain reserved and excluded from performance; P-523–P-537 are canonical research records; the verified next ID at this repair is P-538. Always read the live allocator before issuance. The [status register](GAME_LOG_STATUS_CURRENT.md) links both closed mini archives and all 15 unresolved carryover records. Eleven diagnostic settlements and 132 retrospective sections remain learning evidence, with zero certified/performance-eligible settlements. Closed minis cannot assign IDs.

## CSV policy

Historical results CSVs are useful for team strength, form, scoring distributions and reproducible validation. They are admitted by event grain and source quality, not file count. Empty headers do not constitute completed season research. Scores need endpoint/period definitions; exact event IDs, dates, neutral venues, competition changes and source hashes are retained. Awards, postgame narratives and whole-season summaries cannot become pregame features. Actual historical availability is often unknown; any date-based availability assumption must be explicit in an experiment and cannot certify a live receipt.

## Custody and publication

The October overhaul was explicitly authorized by the user. Original controlling files and prior run artifacts are preserved under `research/custody/implementation_2026-10-01/`; archive corrections have their own custody journal. [METHOD.md](METHOD.md) identifies the active freeze receipt. Restricted or odds-bearing raw files remain in the ignored benchmark quarantine; permitted source bodies and receipts stay auditable. No commit, push, deployment or recurring automation is performed by the daily command.

# Prediction results log v5

Status: GENERATED VIEW CONTRACT — EMPTY

Operational status: **SUSPENDED — NO ACTIVE MODELS**

This is the human-readable view contract for records in `runtime/store/journal.jsonl`. The journal, its verified hash chain, its head anchor, and each record's frozen control-bundle hash are the machine source of truth. This file must not be hand-edited to create, repair, settle, or evaluate a decision.

## Current journal state

- Decision packets: 0
- Quantitative ISSUE records: 0
- Settlements: 0
- Evaluations: 0
- Calibration-eligible forecasts: 0
- ACTIVE models: 0

The four PASS descriptions in `PREDICTION_RESULTS_LOG_v4.md` predate the executable packet runtime. They were reviewed in `PRE_RUNTIME_PASS_MIGRATION_AUDIT_20260716.csv`; none can be imported because the claimed hashes and source packets cannot be independently reconstructed from complete canonical artifacts.

## Generation rule

A future renderer may regenerate this view only after `sportsctl verify-store` succeeds. Each rendered row must include journal sequence and record hash, request/snapshot/prediction identifiers, decision and reason, exact scope, cutoff/freeze times, model/coverage/control-bundle identifiers, settlement/evaluation version, and eligibility. A rendering failure never changes the journal.

# Learning status and review log (LEARN-v1)

`REVIEW_LOG.csv` receives one row per completed review scope (prompt 6, or prompt 3 for mini-settlement diagnostics): `review_id,level,scope,through_at,disposition,report_path,recorded_at`. `level` is MINI_SETTLEMENT, INTERIM, COMPREHENSIVE, SPORT or COMPETITION. `through_at` is the latest settled-game availability the review covered. `disposition` is one of NO_CHANGE, DATA_REPAIR_REQUIRED, EXPERIMENTAL_RETRAIN, CALIBRATION_STUDY, PROSPECTIVE_SHADOW, PROMOTION_ELIGIBLE or INSUFFICIENT_EVIDENCE. PROMOTION_ELIGIBLE must point to its prospective evaluation report. Rows are appended, never edited.

`python -m ml learning-status --store research/learning_store --review-log research/learning_status/REVIEW_LOG.csv [...] --out <new folder>` derives the counters and review triggers. See [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §7.

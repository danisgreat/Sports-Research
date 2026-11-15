# Learning status and review log (LEARN-v1)

`REVIEW_LOG.csv` receives one row per completed review scope (prompt 6, or prompt 3 for mini-settlement diagnostics): `review_id,level,scope,through_at,disposition,report_path,recorded_at`. `level` is MINI_SETTLEMENT, INTERIM, COMPREHENSIVE, SPORT or COMPETITION. `through_at` is the latest settled-game availability the review covered. `disposition` is one of NO_CHANGE, DATA_REPAIR_REQUIRED, EXPERIMENTAL_RETRAIN, CALIBRATION_STUDY, PROSPECTIVE_SHADOW, PROMOTION_ELIGIBLE or INSUFFICIENT_EVIDENCE. PROMOTION_ELIGIBLE must point to its prospective evaluation report. Rows are appended, never edited.

`python -m ml learning-status --store research/learning_store --review-log research/learning_status/REVIEW_LOG.csv [...] --out <new folder>` derives the counters and review triggers. See [LEARNING_PIPELINE_PROTOCOL](../../ML_PIPELINE.md#part-c-learning_pipeline_protocol) §7.

Review thresholds are reminders (AUDIT-ANYTIME-v1, CR-2026.11.15-R3). The owner may request any review level, including COMPREHENSIVE, at any time and any count; record it here with its actual `through_at`.

An on-request review is logged with the level actually performed (INTERIM, COMPREHENSIVE, SPORT or COMPETITION). Earlier rows written with level USER_REQUEST are read as a review of their scope (CR-2026.11.16-R1).

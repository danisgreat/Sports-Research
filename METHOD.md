# METHOD - current authority

**October 9 final settlement, rules and retrospective:** All 72 pending records (the 65-record carryover plus P-550–P-556) are settled in Part 7. Missing details were settled on a declared evidence hierarchy, no ID was consumed, and the next ID stays P-557. New rules: only Rank 1 and Rank 2 count as wins (T2); every Rank-1 failure gets a deep retrospection (R1, 28 written); supplied contracts are reference only and the analyst derives its own top two out of four from the event distribution (P4). See [the settlement report](research/verification/final_settlement_2026-10-09/REPORT.md) and the [framework retrospective and improvement plan](FRAMEWORK_RETROSPECTIVE_2026-10-09.md), whose recommendations are not yet implemented.

**October 8 carryover review:** 65 existing records receive 780 supplied retrospective sections in active Part 7, with no new grades, cards or ledger writes. P-518-P-522 remain reserved. The excluded local P-550 card is preserved only in source custody; canonical next remains P-550, while its local working successor is P-551. [Review, source limits and corrections](research/verification/carryover_review_2026-10-08/REPORT.md).

**October 8 settlement and rollover:** P-538–P-549 were imported without renumbering into Part 6, with original text and dated sporting retrospectives. Part 7 is now active; P-550 remains next and no ID was consumed by its creation. The selected carryover has 65 exact records, including four P-540 retirement rows with UNKNOWN_DEFINITION. See [the complete settlement/rollover review](research/verification/mini_rollover_2026-10-08/REPORT.md).

**Local authority, numerical ML runtime and all-log reconciliation (October 6):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

October 5 administrative control repairs missing custody snapshots and restores the exact model-pinned control module, closes reconciled mini references, and refreshes the derived archive against retained CSVs. It changes no frozen forecasts, probabilities, model-build receipts or performance admission rules. Evidence and unresolved carryover: [closure report](research/verification/closure_2026-10-05/REPORT.md).

The subsequent [October 5 implementation](research/verification/implementation_2026-10-05/REPORT.md) aligns all current document authorities, removes the redundant closed mini pointer after archive readback, retains all eleven retrospective hypotheses as untested proposals, and reports every source-body custody failure.

Status: **ACTIVE**. Method **MDS-2026.10.09-v8.1**. Control revision **CR-2026.10.09-R1**. Scoring **SCV-2026.10.09-v4**. Active freeze: [CONTROL_MANIFEST_2026-10-09-1.md](CONTROL_MANIFEST_2026-10-09-1.md). Previous freeze: CONTROL_MANIFEST_2026-10-08-3.md (CR-2026.10.08-R3). Its SHA is recorded in the living [status register](GAME_LOG_STATUS_CURRENT.md), outside its own hash scope.

The user's instruction authorizes the implementation of the numerical machine learning system: [NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md), [H0_DATASET_CARD.md](H0_DATASET_CARD.md), [DATA_SOURCE_REGISTER.md](DATA_SOURCE_REGISTER.md), [RULES_NHL.md](RULES_NHL.md), and the executable `runtime/` engine. [CURRENT_RULES.md](CURRENT_RULES.md) is the controlling operational manual. [research/README.md](research/README.md) and [runtime/README.md](runtime/README.md) describe executable workflows.

Issued forecasts keep their original values and timestamps. Requested research, qualitative ranks and explicitly uncalibrated scenarios continue without blocker. All requested cards receive canonical IDs in the active combined log through `research.operations.log_card`, independently of calibration or certification. P-518–P-522 remain reserved. Read the current next ID from the ledger-backed workflow and status register.

October 6 numerical implementation establishes:
1. **Event-First Distribution Modeling**: Core simulators (A2) and machine learning models (A1, A3, A4, BigQuery ML) estimate the full outcome probability mass function ($P(Y=y \mid X)$). Contracts (Over/Under, spreads, moneylines) are derived questions asked of that distribution, mathematically guaranteeing monotonicity.
2. **Point-in-Time H0 Feature Store**: Strictly independent of D0. Features must satisfy $known\_at \le cutoff\_at$ or be masked as missing.
3. **Rolling-Origin Splitting**: Chronological partitioning (`TRAIN` -> `TUNE` -> `CAL` -> `TEST`). Probability calibrators are fit strictly on the out-of-fold calibration partition.
4. **Proper Scoring & Multi-Metric Evaluation**: Primary evaluation via Brier score and log loss without arbitrary clipping; distribution evaluation via discrete CRPS and interval coverage; ranking via Wins@2 and NDCG.
5. **BigQuery AI & ML Integration**: Enterprise-grade cloud time series forecasting (`AI.FORECAST`, `ARIMA_PLUS`) and remote models for high-scale feature pipelines.

| Purpose | Current file |
|---|---|
| Operating controls | [CURRENT_RULES.md](CURRENT_RULES.md) |
| Workflow and commands | [research/README.md](research/README.md), [runtime/README.md](runtime/README.md) |
| Numerical ML Model Portfolio | [NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md) |
| Independent Training Datasets | [H0_DATASET_CARD.md](H0_DATASET_CARD.md) |
| Data Source Register | [DATA_SOURCE_REGISTER.md](DATA_SOURCE_REGISTER.md) |
| Card/evidence schemas | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md), [RECORD_ELIGIBILITY_SCHEMA.md](RECORD_ELIGIBILITY_SCHEMA.md) |
| Evaluation & Scoring | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Retrospective & improvement plan | [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) |
| Source access | [SOURCES.md](SOURCES.md), [research/sources_registry.json](research/sources_registry.json) |
| Dataset custody | [Previous Sports Results/README.md](Previous%20Sports%20Results/README.md) |
| Verification | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |


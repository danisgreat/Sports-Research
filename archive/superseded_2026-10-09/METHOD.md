# METHOD - current authority

**October 9 prediction repair (CR-2026.10.09-R4):** Cutoff-safe league profiles, draw-consistent evaluation, native game identities, saved model-plus-calibrator issuance, and honest unknown-gate cohorts are recorded in the [repair report](research/verification/prediction_repairs_2026-10-09/REPORT.md).

**Earlier October 9 implementation (CR-2026.10.09-R3):** The recommendations of the [framework retrospective](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) were implemented (status table in its §5.8): coherent full-game distributions and fitted runtime engines, the Rank-1 gate and one-distribution cards (`mini-log-3`), the rolling scoreboard, CI-based promotion evidence, source adapters and evidence tooling, and the generated [CURRENT_STATE.md](CURRENT_STATE.md). Operator prompts, golden examples and validators are in [research/prompts/](research/prompts/README.md). Earlier dated notes are kept verbatim in [archive/status_notes/](archive/status_notes/SUPERSEDED_STATUS_PARAGRAPHS_2026-10-09.md).

October 5 administrative control repairs missing custody snapshots and restores the exact model-pinned control module, closes reconciled mini references, and refreshes the derived archive against retained CSVs. It changes no frozen forecasts, probabilities, model-build receipts or performance admission rules. Evidence and unresolved carryover: [closure report](research/verification/closure_2026-10-05/REPORT.md).

The subsequent [October 5 implementation](research/verification/implementation_2026-10-05/REPORT.md) aligns all current document authorities, removes the redundant closed mini pointer after archive readback, retains all eleven retrospective hypotheses as untested proposals, and reports every source-body custody failure.

Status: **ACTIVE**. Method **MDS-2026.10.09-v8.4**. Control revision **CR-2026.10.09-R4**. Scoring **SCV-2026.10.09-v5**. Active freeze: [CONTROL_MANIFEST_2026-10-09-4.md](CONTROL_MANIFEST_2026-10-09-4.md). Previous freeze: CONTROL_MANIFEST_2026-10-09-3.md (CR-2026.10.09-R3); superseded manifests are kept unchanged in [archive/controls/](archive/controls/). Its SHA is recorded in the living [status register](GAME_LOG_STATUS_CURRENT.md), outside its own hash scope.

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
| Operator prompts and local-mini lifecycle | [research/prompts/README.md](research/prompts/README.md) |
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


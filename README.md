# Sports Research

Status: **ACTIVE**
Framework review: **2026-08-30**
Current method: **MDS-2026.08.30-v2.7 — late-import, phase-transition, allocation/robustness and termination-order process patch; qualitative weights unchanged**
Numerical training program: **NTS-2026.08.25-v0.2 — STAGE 0 ALL-SPORTS DESIGN / PRE-FIT / NOT FINALISED**

The active authority is the flat Markdown set in this folder. Material under archive/ is historical evidence only. Framework and rule changes remain Markdown-only. The numerical rework defines targets, source/data/model registries, candidate probability models, chronological tests, and promotion gates on paper. It does not authorise a source download, runtime, code, notebook, database, fitted model, calibrator, generated probability, or other numerical artifact; those require a later explicit user request and remain outside the authoritative Markdown rule set.

## Active document map

| File | Purpose |
|---|---|
| [AGENT_ROLE_AND_TASK.md](AGENT_ROLE_AND_TASK.md) | Role, honesty boundary, ranking objective, and required delivery |
| [RULES_GENERAL.md](RULES_GENERAL.md) | Universal hard gates, state/source workflow, ranking, settlement, and governance |
| [MODEL_AND_DATA_SPEC.md](MODEL_AND_DATA_SPEC.md) | Versioned algorithm, data priority, provenance, validation, schemas, and evaluation |
| [ALGORITHM_PORTFOLIO_AND_EVALUATION.md](ALGORITHM_PORTFOLIO_AND_EVALUATION.md) | Numerical-model roadmap, feature governance, calibration, ranking, optional pair portfolio, and champion–challenger protocol |
| [NUMERICAL_TRAINING_SPEC.md](NUMERICAL_TRAINING_SPEC.md) | Distribution-first all-sports training architecture, target/threshold separation, candidate probability models, stages, and publication gates |
| [DATA_SOURCE_REGISTER.md](DATA_SOURCE_REGISTER.md) | Candidate providers, use/coverage/known-at audit fields, snapshot rules, and approval state |
| [H0_DATASET_CARD.md](H0_DATASET_CARD.md) | Preregistered source-derived target populations, grains, labels, splits, and data-quality gates for every dedicated sport; currently not built |
| [NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md) | Candidate and immutable-build registry; all numerical models currently design-only and not fit |
| [UPCOMING_GAME_RESEARCH_GUIDE.md](UPCOMING_GAME_RESEARCH_GUIDE.md) | Full operational guide for researching, forecasting, ranking, logging, settling, and learning from upcoming games |
| [LEARNING_REGISTER.md](LEARNING_REGISTER.md) | Sole current registry for hypotheses, tests, promotions, retirements, and superseded rules |
| [RULES_CRICKET.md](RULES_CRICKET.md) | Cricket-specific identity, inputs, model, live, and settlement controls |
| [RULES_BASKETBALL.md](RULES_BASKETBALL.md) | Basketball-specific controls |
| [RULES_AFL.md](RULES_AFL.md) | AFL/AFLW-specific controls |
| [RULES_NRL_RUGBY.md](RULES_NRL_RUGBY.md) | Rugby league/NRL-specific controls |
| [RULES_RUGBY_UNION.md](RULES_RUGBY_UNION.md) | Rugby union and rugby-sevens-specific controls; qualitative only |
| [RULES_AMERICAN_FOOTBALL.md](RULES_AMERICAN_FOOTBALL.md) | NFL, college, and UFL-specific controls |
| [RULES_BASEBALL.md](RULES_BASEBALL.md) | MLB/KBO/NPB and other baseball-specific controls |
| [RULES_SOCCER.md](RULES_SOCCER.md) | Soccer-specific controls |
| [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md) | NHL and other ice-hockey-specific controls |
| [RULES_TENNIS.md](RULES_TENNIS.md) | Tennis-specific surface, serve/return, format, retirement, and settlement controls |
| [PREDICTION_LOG_COMBINED.md](PREDICTION_LOG_COMBINED.md) | **Active canonical combined log**; its top snapshot alone controls queue state and next ID |
| [PREDICTION_LOG.md](<prediction logs/PREDICTION_LOG.md>) | Frozen source component, P-001–P-066; retained for hash verification/recovery |
| [PREDICTION_LOG_2.md](<prediction logs/PREDICTION_LOG_2.md>) | Frozen source component, P-067–P-088 closeout; retained for hash verification/recovery |
| [PREDICTION_LOG_3.md](<prediction logs/PREDICTION_LOG_3.md>) | Frozen source component containing the 2026-08-26 review; retained for hash verification/recovery |
| [PREDICTION_LOG_4.md](<prediction logs/PREDICTION_LOG_4.md>) | Frozen user-supplied continuation, P-089–P-102 plus settlement sweep; retained byte-for-byte for hash verification/recovery |
| [PREDICTION_LOG_6.md](<prediction logs/PREDICTION_LOG_6.md>) | Text-preserved user-supplied continuation, P-103–P-123; original import hash and terminal-newline normalization are documented in the combined log |
| [PREDICTION_LOG_5.md](<prediction logs/PREDICTION_LOG_5.md>) | Earlier mini-log artifact for P-124–P-136 before the supplied settlement/restoration sweep; retained for provenance comparison |
| [PREDICTION_LOG_5_SETTLED_2026-08-29.md](<prediction logs/PREDICTION_LOG_5_SETTLED_2026-08-29.md>) | Supplied P-124–P-136 continuation with settlement sweep, P-133 restoration and appended independent audit |
| [PREDICTION_MINI_LOG_3.md](<prediction logs/PREDICTION_MINI_LOG_3.md>) | P-137–P-164 source continuation; audited canonical aliases, duplicate-storage handling, settlements, detailed retrospective and pending-field queue |
| [PREDICTION_MINI_LOG_4.md](<prediction logs/PREDICTION_MINI_LOG_4.md>) | P-165–P-186 supplied continuation plus independent provenance, settlement, source and algorithm audit; late-import descriptive evidence only |
| [COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md](COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md) | Full P-001–P-060 audit, findings, corrections, and implementation record |

README never carries a queue ID or performance count. Those values change and belong only in the top controlling snapshot of the active log, currently PREDICTION_LOG_COMBINED.md.

## Workflow

1. Read the role, general rules, model/data specification, algorithm/evaluation protocol, numerical training specification, relevant sport file, and active entries in the learning register. Use UPCOMING_GAME_RESEARCH_GUIDE.md for the operational sequence. For numerical work, also read the source, H0, and model registries.
2. Read the log's top controlling snapshot and settle every verified final before forecasting; leave live events open and continue to the next item.
3. Freeze identity, contract, state, method version, and information cutoff.
4. Freeze the underlying target separately from the bookmaker lines. Research in data-priority order, build one coherent target distribution or qualitative corridor, derive every contract from it, and rank all supplied unresolved rows.
5. Append the forecast before delivery.
6. Settle from the official result, separate contract outcome from process quality, and update the learning register only through its prospective procedure.

## Claim boundary

The current log is an audit trail, not a calibrated betting record. D0 is process-development evidence only; H0 has not been built or quality-approved. NTS-2026.08.25-v0.2 is the **training phase at Stage 0 all-sports design/pre-fit**, not evidence that fitting is underway. No numerical challenger is trained, calibrated, tested, or validated. Numeric publication requires the target-specific gates in NUMERICAL_TRAINING_SPEC.md, MODEL_AND_DATA_SPEC.md, and ALGORITHM_PORTFOLIO_AND_EVALUATION.md; otherwise use qualitative verdicts, explicit unknowns, and no false precision.

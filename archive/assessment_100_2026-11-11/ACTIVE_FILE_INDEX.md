# Active file and usable-data index

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v2).** Defined in [WORKFLOW](WORKFLOW.md#part-a-execution_environment_protocol) Part A §2 (GitHub `main` at a printed SHA when a local file is unreadable).

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](WORKFLOW.md#part-a-execution_environment_protocol); summarised in [CORE](CORE.md) §1.

**Updated 2026-10-16; original operating index built 2026-10-12** (audit R37, framework change [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md)). This page names current operating documents. Retired folder inventories are historical and no longer describe the working tree. Online source research supplies new-card history; update this index when operating documents change.

**Consolidated 2026-11-07 (CR-2026.11.07-R2).** Several entries below now point to parts of merged files; the part names keep the old file names. Moves and hashes: [HISTORICAL_LINK_INDEX](HISTORICAL_LINK_INDEX.md#consolidation--2026-11-07-cr-20261107-r2).

## 1. Operating documents (read these; everything else is reference or history)

| Role | File |
|---|---|
| Local keys, prompt-4 canonical assignment and cumulative .md delivery | [WORKFLOW.md (MINI_LOG_IDENTITY_PROTOCOL)](WORKFLOW.md#part-b-mini_log_identity_protocol) |
| Persistent sourcing / information closure | [RESEARCH_PROTOCOL.md (RESEARCH_EXHAUSTIVENESS_PROTOCOL)](RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol) |
| Current exact competition source routes and access/coverage limits | [research/source_routes/README.md](research/source_routes/README.md) |
| R3 implementation and unresolved backlog | [research/verification/framework_change_2026-11-09-3/IMPLEMENTATION.md](research/verification/framework_change_2026-11-09-3/IMPLEMENTATION.md) |
| Reusable source discoveries | [RESEARCH_SOURCE_REGISTER.md](RESEARCH_SOURCE_REGISTER.md) |
| External research operation (EXT-v3, v24.15, 2026-11-11): the owner's research chats, the event key, lane returns, the merge, and the files a chat uploads (profile, lane briefs, kit, parameter files, do-not-open list, per-sport sources) | [EXT-v3 guide](EXTERNAL_RESEARCH_PROTOCOL_V3.md), [current upload package](research/external/README.md) |
| Open bulk results history (soccer, cricket) with provenance; studies and simulator checks that use it | [research/bulk_history/](research/bulk_history/DATA_PROVENANCE.md), [framework change 2026-11-11-1](research/verification/framework_change_2026-11-11-1/IMPLEMENTATION.md) |
| Current values (IDs, active log, versions, scoreboard) | [CURRENT_STATE.md](CURRENT_STATE.md) |
| Who runs which prompt, the remote fallback (REF-v2), delivery and prompt-4 intake (the external-chat route is retired, REQ-v3) | [EXECUTION_ENVIRONMENT_PROTOCOL](WORKFLOW.md#part-a-execution_environment_protocol) |
| The one page a game card reads in full before research (v24.0) | [CORE.md](CORE.md), with [GAME_REQUEST_TEMPLATE.md](GAME_REQUEST_TEMPLATE.md) for the owner's request and [RESEARCH_PROTOCOL.md (RESEARCH_CHECKLISTS)](RESEARCH_PROTOCOL.md#part-d-research_checklists) for what to research per sport and where |
| Reference stage, tiers, TB-2-MD and the model lane | [REFERENCE_MODEL_PROTOCOL.md](REFERENCE_MODEL_PROTOCOL.md), parameters in [PARAMETERS.md (COMPETITION_PARAMETERS)](PARAMETERS.md#part-a-competition_parameters) and [research/competition_parameters/](research/competition_parameters/) |
| Adjustment ledger, effect tables, picks block and benchmarks | [ADJUSTMENT_LEDGER_PROTOCOL.md](ADJUSTMENT_LEDGER_PROTOCOL.md), [PARAMETERS.md (EFFECT_TABLES)](PARAMETERS.md#part-b-effect_tables), [BENCHMARK_PROTOCOL.md](BENCHMARK_PROTOCOL.md); data in [research/adjustment_ledger/](research/adjustment_ledger/) and [research/effect_tables/](research/effect_tables/) |
| Simulation: when to use it and how to validate it | [SIMULATION_PROTOCOL.md](SIMULATION_PROTOCOL.md) (code in `ml/sim/`) |
| Method and rules | [CORE.md (METHOD)](CORE.md#merged-method), [RULES_REFERENCE.md (CURRENT_RULES)](RULES_REFERENCE.md#part-a-current_rules), [RULES_REFERENCE.md (SELECTION_RULES)](RULES_REFERENCE.md#part-b-selection_rules) |
| Card, mini, settlement and canonical formats; self-audit C1–C22, S1–S18 | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Research completion and input/issue timing | [TIMING_RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-e-timing_research_protocol) (no fixed manual research deadline; no separate cutoff, the evidence horizon is the game-log scheduled start) |
| Scoring and evaluation | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification checks | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Operator prompts 1–8 (prompt 1 = core plus one file in [research/prompts/1_sports/](research/prompts/1_sports/)) | [research/prompts/README.md](research/prompts/README.md), [common operating protocol](research/prompts/COMMON_OPERATING_PROTOCOL.md), [PROMPTS.md](PROMPTS.md) |
| Experiments and their status | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Operative lessons (promoted and narrowed), recurring mistakes and withdrawn rules | [LESSONS_PROMOTED.md](LESSONS_PROMOTED.md) |
| Hand probability method for every card (ANALYST_PRIMARY_V1) and arithmetic aids | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League levels, base rates | [PARAMETERS.md (LEAGUE_PROFILES)](PARAMETERS.md#part-d-league_profiles), [PARAMETERS.md (BASE_RATES_REGISTER)](PARAMETERS.md#part-c-base_rates_register) |
| Source routes and reachability | [SOURCES.md](SOURCES.md), [mandatory roster/availability research](ROSTER_AVAILABILITY_PROTOCOL.md) |
| Archive use, recipes (R2 form windows) and integrity rules | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) |
| Sport rules and lessons (v11 precedence banner at the top of each) | `RULES_<SPORT>.md`, [RULES_CRICKET.md (LEAGUE_RULES_CRICKET)](RULES_CRICKET.md#merged-league_rules_cricket), [RULES_SOCCER.md (LEAGUE_RULES_SOCCER)](RULES_SOCCER.md#merged-league_rules_soccer) |
| Current queue and canonical status | [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md) (current section at the top; later sections are dated history) |
| Active Combined Log | resolved dynamically from [CURRENT_STATE](CURRENT_STATE.md) |
| Contribution and publication rules | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Recovery of removed or moved paths | [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |
| Learning pipeline: research export, learning store, features, training releases, studies, prospective shadows, review levels, model registry | [ML_PIPELINE.md (LEARNING_PIPELINE_PROTOCOL)](ML_PIPELINE.md#part-c-learning_pipeline_protocol), [research/learning_store/](research/learning_store/README.md), [research/model_registry/MODEL_REGISTRY.csv](research/model_registry/MODEL_REGISTRY.csv), [research/learning_status/](research/learning_status/README.md) |
| ML/RL workshop and reference lane (MLSCOPE-v3: reference and freeze in prompt 1, settlement in prompt 3, review in prompt 6, releases in prompt 8) | [ml/README.md](ml/README.md), outputs in [research/model_shadow/](research/model_shadow/README.md), design [archive: ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](archive/consolidation_2026-11-07/archived/ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) |

**History, not instructions:** `archive/`, `prediction logs/` parts 1–6, dated folders under `research/verification/`, `research/issued_research/`, LEARNING_REGISTER / LEARNINGS_INDEX (lessons, with promotion status), FRAMEWORK_RETROSPECTIVE_2026-10-09, NUMERICAL_MODEL_REGISTER (design notes), VALIDATION_EVIDENCE.

**Root-document archive, 2026-10-14:** the ten historical documents approved for archiving have moved to [archive/root_documents_2026-10-14/](archive/root_documents_2026-10-14/README.md), including FRAMEWORK_RETROSPECTIVE_2026-10-09 and NUMERICAL_MODEL_REGISTER. Their contents are preserved; they are not operating instructions. See [old-path recovery](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14). The data-coverage counts below remain their original dated snapshot.

## 2. Current historical-research status

All sports use [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) for online form windows and [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) for confirmed players. The old store is retired; old inventory counts and store-derived profiles are not current input authority. [RESULTS_REBUILD_PLAN](archive/consolidation_2026-11-07/archived/RESULTS_REBUILD_PLAN.md) is a future proposal, not an executed rebuild.


**v24.15 additions:** [recent-team shadow centres and coverage](research/verification/framework_change_2026-11-11-3/team_strength/README.md), [corrected cricket normalization](research/bulk_history/cricket/v24.15/NORMALIZATION_RECEIPT.csv), [implementation and limits](research/verification/framework_change_2026-11-11-3/IMPLEMENTATION.md). The active working clone is `C:\Users\danie\Projects\Sports-Research`; the OneDrive checkout is a retained mirror.

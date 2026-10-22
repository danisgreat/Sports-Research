# Active file and usable-data index

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Google Drive (DRIVE-v2, optional).** Defined in [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Updated 2026-10-16; original operating index built 2026-10-12** (audit R37, framework change [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md)). This page names current operating documents. Retired folder inventories are historical and no longer describe the working tree. Online source research supplies new-card history; update this index when operating documents change.

## 1. Operating documents (read these; everything else is reference or history)

| Role | File |
|---|---|
| Local keys, prompt-4 canonical assignment and cumulative .md delivery | [MINI_LOG_IDENTITY_PROTOCOL.md](MINI_LOG_IDENTITY_PROTOCOL.md) |
| Persistent sourcing / information closure | [RESEARCH_EXHAUSTIVENESS_PROTOCOL.md](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) |
| Reusable source discoveries | [RESEARCH_SOURCE_REGISTER.md](RESEARCH_SOURCE_REGISTER.md) |
| Current values (IDs, active log, versions, scoreboard) | [CURRENT_STATE.md](CURRENT_STATE.md) |
| Required GitHub reference / local-access recovery | [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md) |
| Who runs which prompt, external-chat reading budget, delivery and prompt-4 intake | [EXECUTION_ENVIRONMENT_PROTOCOL](EXECUTION_ENVIRONMENT_PROTOCOL.md) |
| Optional Google Drive drop box (folder `1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj`; no push or mirror requirement) | [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md) |
| The one page a game card reads in full before research (v24.0) | [CORE.md](CORE.md), with [GAME_REQUEST_TEMPLATE.md](GAME_REQUEST_TEMPLATE.md) for the owner's request and [RESEARCH_CHECKLISTS.md](RESEARCH_CHECKLISTS.md) for what to research per sport and where |
| Reference stage, tiers, TB-2-MD and the model lane | [REFERENCE_MODEL_PROTOCOL.md](REFERENCE_MODEL_PROTOCOL.md), parameters in [COMPETITION_PARAMETERS.md](COMPETITION_PARAMETERS.md) and [research/competition_parameters/](research/competition_parameters/) |
| Adjustment ledger, effect tables, picks block and benchmarks | [ADJUSTMENT_LEDGER_PROTOCOL.md](ADJUSTMENT_LEDGER_PROTOCOL.md), [EFFECT_TABLES.md](EFFECT_TABLES.md), [BENCHMARK_PROTOCOL.md](BENCHMARK_PROTOCOL.md); data in [research/adjustment_ledger/](research/adjustment_ledger/) and [research/effect_tables/](research/effect_tables/) |
| Simulation: when to use it and how to validate it | [SIMULATION_PROTOCOL.md](SIMULATION_PROTOCOL.md) (code in `ml/sim/`) |
| Method and rules | [METHOD.md](METHOD.md), [CURRENT_RULES.md](CURRENT_RULES.md), [SELECTION_RULES.md](SELECTION_RULES.md) |
| Card, mini, settlement and canonical formats; self-audit C1–C22, S1–S18 | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Research completion and input/issue timing | [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) (no fixed manual research deadline; no separate cutoff, the evidence horizon is the game-log scheduled start) |
| Scoring and evaluation | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification checks | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Operator prompts 1–8 (prompt 1 = core plus one file in [research/prompts/1_sports/](research/prompts/1_sports/)) | [research/prompts/README.md](research/prompts/README.md), [common operating protocol](research/prompts/COMMON_OPERATING_PROTOCOL.md), [PROMPTS.md](PROMPTS.md) |
| Experiments and their status | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Hand probability method for every card (ANALYST_PRIMARY_V1) and arithmetic aids | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League levels, base rates | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) |
| Source routes and reachability | [SOURCES.md](SOURCES.md), [mandatory roster/availability research](ROSTER_AVAILABILITY_PROTOCOL.md) |
| Archive use, recipes (R2 form windows) and integrity rules | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) |
| Sport rules and lessons (v11 precedence banner at the top of each) | `RULES_<SPORT>.md`, [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md), [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md) |
| Current queue and canonical status | [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md) (current section at the top; later sections are dated history) |
| Active Combined Log | resolved dynamically from [CURRENT_STATE](CURRENT_STATE.md) |
| Contribution and publication rules | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Recovery of removed or moved paths | [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |
| Learning pipeline: research export, learning store, features, training releases, studies, prospective shadows, review levels, model registry | [LEARNING_PIPELINE_PROTOCOL.md](LEARNING_PIPELINE_PROTOCOL.md), [research/learning_store/](research/learning_store/README.md), [research/model_registry/MODEL_REGISTRY.csv](research/model_registry/MODEL_REGISTRY.csv), [research/learning_status/](research/learning_status/README.md) |
| ML/RL workshop and reference lane (MLSCOPE-v3: reference and freeze in prompt 1, settlement in prompt 3, review in prompt 6, releases in prompt 8) | [ml/README.md](ml/README.md), outputs in [research/model_shadow/](research/model_shadow/README.md), design [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) |

**History, not instructions:** `archive/`, `prediction logs/` parts 1–6, dated folders under `research/verification/`, `research/issued_research/`, LEARNING_REGISTER / LEARNINGS_INDEX (lessons, with promotion status), FRAMEWORK_RETROSPECTIVE_2026-10-09, NUMERICAL_MODEL_REGISTER (design notes), VALIDATION_EVIDENCE.

**Root-document archive, 2026-10-14:** the ten historical documents approved for archiving have moved to [archive/root_documents_2026-10-14/](archive/root_documents_2026-10-14/README.md), including FRAMEWORK_RETROSPECTIVE_2026-10-09 and NUMERICAL_MODEL_REGISTER. Their contents are preserved; they are not operating instructions. See [old-path recovery](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14). The data-coverage counts below remain their original dated snapshot.

## 2. Current historical-research status

All sports use [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) for online form windows and [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) for confirmed players. The old store is retired; old inventory counts and store-derived profiles are not current input authority. [RESULTS_REBUILD_PLAN](RESULTS_REBUILD_PLAN.md) is a future proposal, not an executed rebuild.

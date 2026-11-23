# Active file and usable-data index

*Standing protocols are defined once in [CORE.md](CORE.md); current release versions live in [VERSIONS.csv](VERSIONS.csv) and [CURRENT_STATE.md](CURRENT_STATE.md). Moves and hashes from earlier consolidations live in [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md).*

## 1. Active ONE-CHAT-v3 operation (current authority)

| Role | File |
|---|---|
| Operator runbook (prepare, register, seal, settle, score, parallel chats) | [research/one_chat/RUNBOOK.md](research/one_chat/RUNBOOK.md) |
| Registered prospective evaluation plan (Track P, 600-game horizon) | [research/external/EVALUATION_PLAN_v29.0.md](research/external/EVALUATION_PLAN_v29.0.md) |
| Shadow top-two selection (SELECT-SHADOW-v2, registered separately; v1 superseded unused) | [research/external/SELECTION_SHADOW_PLAN_v2.md](research/external/SELECTION_SHADOW_PLAN_v2.md), [`ml/selection_shadow.py`](ml/selection_shadow.py) |
| Reviewed competition aliases for the kit row named in the packet | [research/one_chat/KIT_COMPETITION_ALIASES.csv](research/one_chat/KIT_COMPETITION_ALIASES.csv) |
| Research chat brief & `ONECHAT_V1` block schema | [research/external/ONE_CHAT_BRIEF_v29.2.md](research/external/ONE_CHAT_BRIEF_v29.2.md), [templates](research/external/templates/) |
| Current chat upload package (kit, parameters, reader access, per-sport sources) | [research/external/README.md](research/external/README.md), [`ml/kit/sr_kit.py`](ml/kit/sr_kit.py) |
| One-chat intakes, scores, schedule sources & deep loss register | [research/one_chat/README.md](research/one_chat/README.md), [research/deep_loss/README.md](research/deep_loss/README.md) |
| Historical pre-event validation (Track H, HPPV-v1) | [research/verification/historical_pre_event_v1/README.md](research/verification/historical_pre_event_v1/README.md) |
| Release identities, live state & standing authority | [VERSIONS.csv](VERSIONS.csv), [CURRENT_STATE.md](CURRENT_STATE.md), [CORE.md](CORE.md), [README.md](README.md) |

## 2. Standing rules, sources, probability & sport references

| Role | File |
|---|---|
| Operating rules, selection rules, scoring, audit & verification | [RULES_REFERENCE.md](RULES_REFERENCE.md), [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md), [AUDIT_REVIEW_PROTOCOL.md](AUDIT_REVIEW_PROTOCOL.md), [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Request formats & templates | [GAME_REQUEST_TEMPLATE.md](GAME_REQUEST_TEMPLATE.md), [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Probability toolkit, competition parameters, effect tables & simulation | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [PARAMETERS.md](PARAMETERS.md), [SIMULATION_PROTOCOL.md](SIMULATION_PROTOCOL.md), [research/competition_parameters/](research/competition_parameters/) |
| Sport rules (10 sports) | `RULES_<SPORT>.md` ([Soccer](RULES_SOCCER.md), [Cricket](RULES_CRICKET.md), [Basketball](RULES_BASKETBALL.md), [Baseball](RULES_BASEBALL.md), [Ice Hockey](RULES_ICE_HOCKEY.md), [Tennis](RULES_TENNIS.md), [AFL](RULES_AFL.md), [NRL](RULES_NRL_RUGBY.md), [Rugby Union](RULES_RUGBY_UNION.md), [American Football](RULES_AMERICAN_FOOTBALL.md)) |
| Source access, routes, availability & online history | [SOURCES.md](SOURCES.md), [research/source_routes/README.md](research/source_routes/README.md), [RESEARCH_SOURCE_REGISTER.md](RESEARCH_SOURCE_REGISTER.md), [ROSTER_AVAILABILITY_PROTOCOL.md](ROSTER_AVAILABILITY_PROTOCOL.md), [HISTORICAL_SOURCE_PROTOCOL.md](HISTORICAL_SOURCE_PROTOCOL.md), [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) |
| Logs, status, hypotheses, lessons & learning pipeline | [prediction logs/PREDICTION_LOG_COMBINED_11.md](prediction%20logs/PREDICTION_LOG_COMBINED_11.md), [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md), [LESSONS_PROMOTED.md](LESSONS_PROMOTED.md), [ML_PIPELINE.md](ML_PIPELINE.md), [`ml/README.md`](ml/README.md) |
| Open bulk results history & contribution rules | [research/bulk_history/DATA_PROVENANCE.md](research/bulk_history/DATA_PROVENANCE.md), [CONTRIBUTING.md](CONTRIBUTING.md), [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |

## 3. Retained legacy routes (not used for new ONE-CHAT-v3 games)

| Role | File |
|---|---|
| Legacy repository-side `PICKS_V2` prompts 1–8 & mini workflow | [research/prompts/README.md](research/prompts/README.md), [WORKFLOW.md](WORKFLOW.md), [REFERENCE_MODEL_PROTOCOL.md](REFERENCE_MODEL_PROTOCOL.md), [ADJUSTMENT_LEDGER_PROTOCOL.md](ADJUSTMENT_LEDGER_PROTOCOL.md), [BENCHMARK_PROTOCOL.md](BENCHMARK_PROTOCOL.md), [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) |
| Retired five-lane external route (`EXT-v2` / `EXT-v3` pointers) | [EXTERNAL_RESEARCH_PROTOCOL.md](EXTERNAL_RESEARCH_PROTOCOL.md) |
| Compatibility pointers | [METHOD.md](METHOD.md), [PROMPTS.md](PROMPTS.md) |

**History, not instructions:** `archive/`, closed `prediction logs/` Parts 1–10, dated folders under `research/verification/`, `research/issued_research/`, `research/model_shadow/`, and [archive/root_documents_2026-10-14/](archive/root_documents_2026-10-14/README.md). Working clone outside OneDrive: `C:\Users\danie\Projects\Sports-Research`.

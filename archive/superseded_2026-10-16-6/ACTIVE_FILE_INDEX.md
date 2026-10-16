# Active file and usable-data index

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**Updated 2026-10-16; original operating index built 2026-10-12** (audit R37, framework change [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md)). This page names current operating documents. Retired folder inventories are historical and no longer describe the working tree. Online source research supplies new-card history; update this index when operating documents change.

## 1. Operating documents (read these; everything else is reference or history)

| Role | File |
|---|---|
| Local keys, prompt-4 canonical assignment and cumulative .md delivery | [MINI_LOG_IDENTITY_PROTOCOL.md](MINI_LOG_IDENTITY_PROTOCOL.md) |
| Persistent sourcing / information closure | [RESEARCH_EXHAUSTIVENESS_PROTOCOL.md](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) |
| Reusable source discoveries | [RESEARCH_SOURCE_REGISTER.md](RESEARCH_SOURCE_REGISTER.md) |
| Current values (IDs, active log, versions, scoreboard) | [CURRENT_STATE.md](CURRENT_STATE.md) |
| Required GitHub reference / local-access recovery | [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md) |
| Method and rules | [METHOD.md](METHOD.md), [CURRENT_RULES.md](CURRENT_RULES.md), [SELECTION_RULES.md](SELECTION_RULES.md) |
| Card, mini, settlement and canonical formats; self-audit C1–C22, S1–S18 | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Research completion and input/issue timing | [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) (no fixed manual research deadline; no separate cutoff, the evidence horizon is the game-log scheduled start) |
| Scoring and evaluation | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification checks | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Operator prompts 1–8 | [research/prompts/README.md](research/prompts/README.md), [common operating protocol](research/prompts/COMMON_OPERATING_PROTOCOL.md), [PROMPTS.md](PROMPTS.md) |
| Experiments and their status | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Arithmetic aids (with operative-status table) | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League levels, base rates | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) |
| Source routes and reachability | [SOURCES.md](SOURCES.md), [mandatory roster/availability research](ROSTER_AVAILABILITY_PROTOCOL.md) |
| Archive use, recipes (R2 form windows) and integrity rules | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) |
| Sport rules and lessons (v11 precedence banner at the top of each) | `RULES_<SPORT>.md`, [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md), [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md) |
| Current queue and canonical status | [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md) (current section at the top; later sections are dated history) |
| Active Combined Log | named in CURRENT_STATE (Part 7 on 2026-10-12) |
| Contribution and publication rules | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Recovery of removed or moved paths | [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |
| Primary runtime (named lane allowed for prompts 1–3) and separate workshop | [ml/README.md](ml/README.md), outputs in [research/model_shadow/](research/model_shadow/README.md), design [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) |

**History, not instructions:** `archive/`, `prediction logs/` parts 1–6, dated folders under `research/verification/`, `research/issued_research/`, LEARNING_REGISTER / LEARNINGS_INDEX (lessons, with promotion status), FRAMEWORK_RETROSPECTIVE_2026-10-09, NUMERICAL_MODEL_REGISTER (design notes), VALIDATION_EVIDENCE.

**Root-document archive, 2026-10-14:** the ten historical documents approved for archiving have moved to [archive/root_documents_2026-10-14/](archive/root_documents_2026-10-14/README.md), including FRAMEWORK_RETROSPECTIVE_2026-10-09 and NUMERICAL_MODEL_REGISTER. Their contents are preserved; they are not operating instructions. See [old-path recovery](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14). The data-coverage counts below remain their original dated snapshot.

## 2. Current historical-research status

All sports use [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) for online form windows and [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) for confirmed players. The old store is retired; old inventory counts and store-derived profiles are not current input authority. [RESULTS_REBUILD_PLAN](RESULTS_REBUILD_PLAN.md) is a future proposal, not an executed rebuild.

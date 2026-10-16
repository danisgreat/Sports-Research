# Operator prompts

**Online history and confirmed players (HIST-2026.10.16-v2 / AVAIL-2026.10.16-v3).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**Active suite: P-2026.10.16-v17.1** (new minis mini-log-9 / mini-settlement-8; existing formats retained). [Reading receipt and workflow](research/prompts/README.md). Use the complete selected prompt; its required rules/templates are linked there.

| # | Copy-ready prompt |
|---|---|
| 1 | [Individual game card, including sport blocks](research/prompts/1_GAME_CARD.md) |
| 2 | [Start a local mini](research/prompts/2_START_LOCAL_MINI.md) |
| 3 | [Settle and review the mini](research/prompts/3_SETTLE_LOCAL_MINI.md) |
| 4 | [Import into the active Combined Log](research/prompts/4_CANONICAL_IMPORT.md) |
| 5 | [Start the next Combined Log](research/prompts/5_START_THE_NEXT_COMBINED_LOG.md) |
| 6 | [Combined-log retrospective](research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md) |
| 7 | [Expand or repair historical results](research/prompts/7_EXPAND_PREVIOUS_RESULTS.md) |
| 8 | [Improve the framework](research/prompts/8_IMPROVE_THE_FRAMEWORK.md) |

Run 2 → 1 per event → 3 → 4; use 5–8 when needed. Current IDs/destination: [CURRENT_STATE](CURRENT_STATE.md). Implemented changes and recommendation roadmap: [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (current), [2026-10-11-1](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md). Preserved previous suites: [v10](archive/superseded_2026-10-12/research/prompts/README.md), [pre-v10](archive/superseded_2026-10-11/prompt_v10/research/prompts/README.md).

These prompts improve evidence, consistency and measurement. Predictive improvement remains to be demonstrated prospectively against frozen baselines; no prompt guarantees outcomes.

Availability procedure: [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md), mandatory for every prompt-1 game.

All eight tasks require [COMMON_OPERATING_PROTOCOL](research/prompts/COMMON_OPERATING_PROTOCOL.md). Use [prompt 1](research/prompts/1_GAME_CARD.md) for eleven separate sport/general Upcoming game blocks. The supplied-first root draft is reference only; current P4/selection rules govern.

**Primary ML/RL (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) governs new experimental model-assisted primary rows and sports-only model-selection feedback. Actual per-event execution and receipts required; no old artifact is automatically qualified.

**Preferred historical recovery:** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) applies to every sport and competition. Missing, incomplete or incorrect local history is researched online first, with reviewed web rows usable in the named primary input scope; shared archive maintenance is separate. Source/known-at checks and unsupported-model limits remain.


**Strict research completion:** [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_COMPLETION_PROTOCOL.md) requires full research, all applicable sport procedures and every requested contract assessment irrespective of model calibration/runtime, data/lineup gaps, kickoff or mini/write blockers. Supported automatic analyst comparisons stay NOT_PRIMARY; missing numerical ML never means stop research. The A9 evidence matrix is mandatory.


**Research retention before model availability (RETAIN-v1).** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) supersedes EXEC-v1's model prerequisite for recording/import. Write every identified researched event under its reconciled working P-ID and canonically retain it through verified import even if the model/adapter/runtime/module/baseline/calibration/receipt is absent or failed. Use RESEARCH_ONLY_NO_MODEL, explicit execution reason and blank nonexistent artifact paths; keep model p_card NOT_ESTIMATED and supported analyst_p NOT_PRIMARY. Missing ML never by itself blocks the ID or a source-backed settlement. Retain verified settled labels for future model development with source/known-at/revision/feature status; only actual frozen experts can supply Hedge losses. Never invent probabilities, execution, final scores or pregame timing. Identity/custody/write conflicts remain real blockers.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.

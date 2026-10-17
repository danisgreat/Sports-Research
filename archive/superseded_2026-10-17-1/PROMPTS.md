# Operator prompts

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**Active suite: P-2026.10.16-v20.0** (new minis mini-log-10 / mini-settlement-10; existing formats retained; LEARN-v1 structured research export, learning accounting and review levels under [LEARNING_PIPELINE_PROTOCOL](LEARNING_PIPELINE_PROTOCOL.md); dependency map in [research/prompts/DEPENDENCY_MAP.md](research/prompts/DEPENDENCY_MAP.md)). [Reading receipt and workflow](research/prompts/README.md). Use the complete selected prompt; its required rules/templates are linked there.

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


**Research retention before model availability (RETAIN-v2).** Retain every identified researched event under its stable local event key regardless of ML/runtime/baseline/calibration availability; use RESEARCH_ONLY_NO_MODEL and an honest execution disposition when needed. Prompts 1–3 neither assign nor reserve canonical P-IDs. Prompt 1 appends the full research card to the mini, updates its intake/footer, reads back the result and returns the complete updated Markdown document after every game request. Prompt 4 alone reconciles duplicates and assigns canonical P-IDs at import, preserving local originals and a local-to-canonical map. Verified labels remain future-development candidates; only real frozen bundles supply expert feedback. See RESEARCH_RETENTION_PROTOCOL and MINI_LOG_IDENTITY_PROTOCOL. Identity/custody/write conflicts remain real blockers; missing ML does not discard research.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card regardless of model availability, update intake and the local footer, verify the full mini and return its complete updated .md file after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.

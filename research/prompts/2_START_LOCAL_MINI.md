# PROMPT 2 — Start the next local mini

**Local keys until settlement; updated mini after every game (MINI-v2).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Research and mini creation (prompts 1–2) use stable local event keys and never assign or reserve canonical P-IDs. A canonical P-ID is assigned only in an event's settlement phase: prompt 3 settles the event and then runs the prompt-4 import, which assigns the ID. After each prompt-1 game request the repository agent appends the card to the active mini under `research/active_minis/`, updates intake and footer, reads the file back, and commits and pushes it. Preserve every owner-entered Upcoming game block and all earlier issued bytes. Formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.22-v23.0 · LOCAL_MINI_STAGING.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). **LOCAL_WORKING_TREE** (ENV-v2). Writes: one new Markdown mini at `research/active_minis/<MINI_KEY>.md` (no execution manifest), the CURRENT_STATE active-mini line, then a commit and push of exactly those paths. Creating a mini consumes no event ID and runs no model. Workshop forecasts and the decision lab are excluded.

**ML/RL scope (MLSCOPE-v2).** Owner instruction, 22 October 2026: models run where they are needed, beside the analyst card and never inside it. Prompt 1 researches the game online and prices every p_card as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY from one declared distribution ([PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md); code may do the arithmetic, with every input and step printed). Only after the card is written to the mini does prompt 1 run the pregame model shadow, which freezes the model and league-baseline rows, and the card's own p_card, on the same contracts when the competition has an active release, or records NOT_RUN_NO_RELEASE. Model output never changes a card's p_card, ranks or picks. Prompt 3 settles the shadow with the card; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only after at least 8 weeks and 50 paired games; a progress review falls due when either is reached first. RL has no forecasting role: online expert weighting updates at settlement. Details: [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Supersedes MLSCOPE-v1, NOCODE-v1 and any older text that forbids code or models in prompts 1–5.

**Execution environment (ENV-v2).** Owner instruction, 22 October 2026: every prompt, 1 to 8, runs in this repository as the repository agent (`LOCAL_WORKING_TREE`), with internet access for research. Controls are read from the local working tree; GitHub `main` is the published copy, and every run that changes files ends with a commit and push. The external-chat route (ENV-v1) is retired for new work; anything it produced earlier is still imported as before. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**Repository reference (local working tree).** Read this prompt's controls from the local working tree and print the branch and HEAD SHA in the reading receipt. [Sports Research on GitHub](https://github.com/danisgreat/Sports-Research/tree/main) `main` is the published copy and the fallback for any unreadable local file ([GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md)). Owner material dropped in Google Drive (DRIVE-v2, [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](../../GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md)) or attached to the request is read as input, never as a control.

## Inputs

- File: `research/active_minis/<MINI_KEY>.md`, written here.
- Previous mini, settlement and import receipts: in the working tree, or attached or pasted by the owner (copy owner-supplied minis byte-for-byte under `research/active_minis/received/` before using them); otherwise discover what exists and say what was found.
- Requested events/carryovers: exact requests, or NONE.
- Authority: the local working tree (`LOCAL_WORKING_TREE`), with branch and HEAD SHA recorded.

## 1. Read and reconcile

Read current state/method/rules/selection/templates, the prompt index/common protocol, current status, active log entries/addenda and previous mini/import receipts. Print actual paths/sections, one full authority SHA, versions, time/offset and missing evidence. Locate existing files before asking; inaccessible does not mean nonexistent.

Read current canonical state only for context/duplicate references. Resolve the actual active mini, existing MINI_KEY namespaces, local events and writer leases. Choose a unique MINI_KEY and initial LOCAL-<MINI_KEY>-G0001; do not choose/reserve a P-ID or require a reconciled canonical next number to start research. Canonical allocation conflicts are resolved in the settlement phase (prompt 3 through the prompt-4 import); actual local identity/custody/write conflicts still block the affected write.

Continue the eligible active mini or record an authorized hand-over; distinct authorized minis use distinct local namespaces. An exact existing requested mini returns ALREADY_EXISTS with zero new allocation. This concludes only duplicate mini creation: if the invocation also requests a game, continue prompt1 in that eligible active mini. Lease/identity/access conflicts block writes only; execute RESEARCH_COMPLETION_PROTOCOL and return a complete no-ID A1–A9 draft. Never treat an existing mini as a reason to abandon requested analysis. A frozen mini routes new events to the next authorized mini.

## 2. Create the complete mini

Use CARD_AND_LOG_TEMPLATES §2 exactly, format mini-log-10. Record authority/read time, active destination, canonical context and outstanding-local snapshots, immutable MINI_KEY and first local event key, writer, lease start/expiry, hand-over and frozen status. Initial counts are zero; last local key NONE; next local key LOCAL-<MINI_KEY>-G0001; canonical assignment NOT_ASSIGNED / PROMPT_4_IMPORT.

Carry pending events and terminal unresolved evidence separately with original IDs/local-canonical status. Each item names original reference, latest revision, open field, actor, exact next source/field, due time/zone, final-time basis or UNKNOWN, last attempt and actual automation. An open-event alert never discards a request or forces settlement.

Retain every request in intake: received time, identity/alias, disposition and existing/new-record pointer. Blocked/duplicate requests stay visible. Do not invent a card, picks, probabilities, source or lineup to populate the mini.

Model-shadow IDs remain separate from P-IDs. Prompt 1 prices each event itself (ANALYST_PRIMARY_V1) before its model shadow runs; do not seed a mini from model or historical predictions. Unsettled cards carried from an earlier mini keep their original local keys and bytes in a carried-cards section; they consume no new ordinal. Each prompt-1 game performs its own availability, cutoff, candidate and frozen-baseline checks.

## 3. Verify and return

Read back the complete mini. Check authority, local namespace/ordinal continuity, writer lease, zero initial counts, queue/intake coverage and footer agreement. Earlier minis, cards and canonical status/logs must remain unchanged. Structural examples use EXAMPLE IDs.

Write the mini to `research/active_minis/<MINI_KEY>.md`, set it as the active mini in CURRENT_STATE, read both back, and commit and push exactly those paths (plus any `received/` source copies). Report the path, MINI_KEY / first/next local key, format/status, HEAD SHA, retained carryovers/alerts, the reading evidence and the commit. Settlement/canonical import NOT_PERFORMED. Never claim a save, commit or push that did not happen.

Historical coverage gaps route each prompt1 game to HISTORICAL_SOURCE_PROTOCOL and verified online recovery; do not prepopulate missing scores or block a mini because local archive rows are absent.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and append the card, intake row and footer to the active mini after every game request (ENV-v2). The card never waits for or depends on a model; a model shadow run after the card (MLSCOPE-v2) is recorded beside it. Canonical P-ID assignment happens only in the settlement phase (prompt 3, through the prompt-4 import). Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Create new minis as mini-log-10 with no execution-manifest companion (template section E is legacy; model shadows have their own receipts under MLSCOPE-v2). Mini creation consumes no event ID, runs no model and performs no fit. Verify the empty new mini by reading it back: one format marker, zero cards, footer next key LOCAL-<MINI_KEY>-G0001.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card, its intake row and footer to the active mini, read it back and commit it after each game request (ENV-v2). Canonical IDs are assigned only in the settlement phase, when prompt 3 hands the settled event to the prompt-4 import, which reconciles duplicates and identity and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Current-source setup and prior-format continuity

A new mini follows current online-history and confirmed-player controls. Do not populate L5/L10/L15/L20, league profiles or selected players from the retired store or from another event. Existing minis keep their declared format and issued core bytes; apply current research steps only to new cards. Record genuine missing source/model fields without inventing a completed search or dropping the local research record.

## Persistent sourcing and information closure (EXH-v1)

Initialize references to EXH-v1, the shared source register and relevant prior package registers. Do not prefill source checks, field closures, independence or source-discovery rows. Each new card performs the actual searches and keeps the field/attempt ledger in its named evidence scope; preserve filled prompt-1 event inputs.

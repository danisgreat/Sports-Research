# PROMPT 2 — Start the next local mini

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, return the new card with its intake row and footer, plus the full mini when it fits, for the owner to save (ENV-v1). Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.17-v22.1 · LOCAL_MINI_STAGING.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). **EXTERNAL_CHAT** (ENV-v1). Writes: nothing; returns one new Markdown mini in the reply for the owner to save (no execution manifest). Creating a mini consumes no event ID. GitHub (latest `main`) is read-only; an optional DRIVE-v2 upload is the only remote write allowed. No code is run (MLSCOPE-v1). Workshop forecasts and the decision lab are excluded.

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Execution environments (ENV-v1).** Prompts 1–3 run in an external chat with internet access and read-only access to the GitHub repository at the latest `main` commit: no code, no repository writes, no hashes, a section-level reading budget, and every output returned in the reply for the owner to save. Prompts 4–8 run in this repository as the repository agent (`LOCAL_WORKING_TREE`); prompt 4 is the only intake point for external-chat output and computes the byte counts and SHA-256 the chat cannot. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**Repository reference (latest `main`).** Read this prompt's controls from the latest commit of the `main` branch of [Sports Research on GitHub](https://github.com/danisgreat/Sports-Research/tree/main). At the start, resolve that commit's full SHA, print it in the reading receipt and use that one commit for the whole run ([GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md)); never use an older branch, a cached copy or a Drive file as the authority. Optional: when this chat cannot write the repository, it may upload the new mini `.md` to the owner's [Google Drive folder](https://drive.google.com/drive/folders/1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj?usp=drive_link) `uploads/` (DRIVE-v2, [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](../../GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md)); this is never required, and the complete mini is still returned in the reply.

## Inputs

- Suggested file name: `research/active_minis/<MINI_KEY>.md` (the owner saves it; this chat writes nothing).
- Previous mini, settlement and import receipts: attached or pasted by the owner, or read from the repository at the latest `main` commit; otherwise discover what is committed and say what was found.
- Requested events/carryovers: exact requests, or NONE.
- Authority: the latest `main` commit, pinned by its full SHA (prompts 1–3 never use local controls).

## 1. Read and reconcile

Read current state/method/rules/selection/templates, the prompt index/common protocol, current status, active log entries/addenda and previous mini/import receipts. Print actual paths/sections, one full authority SHA, versions, time/offset and missing evidence. Locate existing files before asking; inaccessible does not mean nonexistent.

Read current canonical state only for context/duplicate references. Resolve the actual active mini, existing MINI_KEY namespaces, local events and writer leases. Choose a unique MINI_KEY and initial LOCAL-<MINI_KEY>-G0001; do not choose/reserve a P-ID or require a reconciled canonical next number to start research. Canonical allocation conflicts are resolved by prompt 4; actual local identity/custody/write conflicts still block the affected write.

Continue the eligible active mini or record an authorized hand-over; distinct authorized minis use distinct local namespaces. An exact existing requested mini returns ALREADY_EXISTS with zero new allocation. This concludes only duplicate mini creation: if the invocation also requests a game, continue prompt1 in that eligible active mini. Lease/identity/access conflicts block writes only; execute RESEARCH_COMPLETION_PROTOCOL and return a complete no-ID A1–A9 draft. Never treat an existing mini as a reason to abandon requested analysis. A frozen mini routes new events to the next authorized mini.

## 2. Create the complete mini

Use CARD_AND_LOG_TEMPLATES §2 exactly, format mini-log-10. Record authority/read time, active destination, canonical context and outstanding-local snapshots, immutable MINI_KEY and first local event key, writer, lease start/expiry, hand-over and frozen status. Initial counts are zero; last local key NONE; next local key LOCAL-<MINI_KEY>-G0001; canonical assignment NOT_ASSIGNED / PROMPT_4_IMPORT.

Carry pending events and terminal unresolved evidence separately with original IDs/local-canonical status. Each item names original reference, latest revision, open field, actor, exact next source/field, due time/zone, final-time basis or UNKNOWN, last attempt and actual automation. An open-event alert never discards a request or forces settlement.

Retain every request in intake: received time, identity/alias, disposition and existing/new-record pointer. Blocked/duplicate requests stay visible. Do not invent a card, picks, probabilities, source or lineup to populate the mini.

Model-shadow IDs remain separate from P-IDs. Prompt 1 prices each event by hand (ANALYST_PRIMARY_V1); do not seed a mini from model or historical predictions. Each prompt-1 game performs its own availability, cutoff, candidate and frozen-baseline checks.

## 3. Verify and return

Read back the complete mini. Check authority, local namespace/ordinal continuity, writer lease, zero initial counts, queue/intake coverage and footer agreement. Earlier minis, cards and canonical status/logs must remain unchanged. Structural examples use EXAMPLE IDs.

Return the complete new mini in the reply with its suggested file name (`research/active_minis/<MINI_KEY>.md`), MINI_KEY / first/next local key, format/status, the latest `main` SHA, retained carryovers/alerts and the reading evidence; the owner saves the file (ENV-v1 §4). Settlement/canonical import NOT_PERFORMED; GitHub writes NO. Never claim the file was saved, uploaded or committed.

Historical coverage gaps route each prompt1 game to HISTORICAL_SOURCE_PROTOCOL and verified online recovery; do not prepopulate missing scores or block a mini because local archive rows are absent.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and deliver the card, intake row and footer (full mini when it fits, ENV-v1) after every game request. No model, runtime, receipt or manifest is needed or recorded. Canonical P-ID assignment belongs exclusively to prompt 4 import. Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Create new minis as mini-log-10 with no execution-manifest companion (template section E is legacy; MLSCOPE-v1). Mini creation consumes no event ID, runs no code and performs no fit. Verify the empty new mini by reading it back: one format marker, zero cards, footer next key LOCAL-<MINI_KEY>-G0001.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Return the researched card with its intake row and footer (and the full mini when it fits, ENV-v1) after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Current-source setup and prior-format continuity

A new mini follows current online-history and confirmed-player controls. Do not populate L5/L10/L15/L20, league profiles or selected players from the retired store or from another event. Existing minis keep their declared format and issued core bytes; apply current research steps only to new cards. Record genuine missing source/model fields without inventing a completed search or dropping the local research record.

## Persistent sourcing and information closure (EXH-v1)

Initialize references to EXH-v1, the shared source register and relevant prior package registers. Do not prefill source checks, field closures, independence or source-discovery rows. Each new card performs the actual searches and keeps the field/attempt ledger in its named evidence scope; preserve filled prompt-1 event inputs.

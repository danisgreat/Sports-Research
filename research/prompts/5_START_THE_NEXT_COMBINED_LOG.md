# PROMPT 5 — Roll over the Combined Log without consuming IDs

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, return the new card with its intake row and footer, plus the full mini when it fits, for the owner to save (ENV-v1). Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.17-v22.1 · COMBINED_LOG_ROLLOVER · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Default trigger: working file exceeds 1.5 MB, contains at least 50 canonical entries, or cannot be opened/rendered reliably. Record the actual trigger/measurement; rollover is not required to settle or import. Run between complete imports.

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Execution environments (ENV-v1).** Prompts 1–3 run in an external chat with internet access and read-only access to the GitHub repository at the latest `main` commit: no code, no repository writes, no hashes, a section-level reading budget, and every output returned in the reply for the owner to save. Prompts 4–8 run in this repository as the repository agent (`LOCAL_WORKING_TREE`); prompt 4 is the only intake point for external-chat output and computes the byte counts and SHA-256 the chat cannot. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## Inputs and allowed writes

Resolve active Part N, user request/trigger and current queues. Writes: old-part closure, one new part, current state/status/live pointers, CHANGELOG and a new rollover receipt. No forecasts, settlements, copied cards, P-ID allocation or model promotion. Publish under the invoked task unless explicitly local-only.

## 1. Reconcile and plan

Read common controls/protocol, templates §8, verification §4, current status and actual log entries/opening/closure records. Print authority/HEAD/dirty inventory. Resolve current Part N, highest/next ID, reserved IDs, pending and evidence queues, and any partial import. Opening snapshots are historical; do not revise them to current values.

Block rollover over an unfinished import. Snapshot the entire old-part working bytes/count/hash and proposed Part N+1 path. An exact completed rollover returns ALREADY_COMPLETED with zero writes. A partial closure/new part requires scoped comparison/recovery; never overwrite an occupied file or create N+2 to hide it.

## 2. Apply closure and new opening

Immediately before closure, recheck HEAD, active path, raw count/hash/tail, next ID and source plan. On drift, re-plan. Append a dated closure with measured contained range/count, highest global ID, unchanged next ID, both queues and prior identity, plus the new-part link.

Recheck again before creating Part N+1. Create its ACTIVE opening, method/control/scoring/HEAD, time/zone, explicit OPENING_SNAPSHOT, previous-part continuity, reserved-ID note, highest/next ID unchanged, queue pointers and research-only/market-blind labels. Use canonical-md-1 and the END ACTIVE COMBINED LOG HEADER marker. Do not insert a placeholder forecast.

Later revisions for closed-part originals go into the new active part with original/prior-revision pointers; the closed original stays immutable. Shadow/model IDs and receipts remain at their existing independent locations. Rollover is no qualification or artifact change.

Update only live pointers and dated change/report records. Prefer dynamic CURRENT_STATE references; retain historical links and old-format semantics.

## 3. Verify, publish and return

Compare the entire old prefix, confirm only closure appended, and verify new part contains header/continuity/queues only. Reconcile all current pointers, zero copied forecasts, unchanged IDs and rerun idempotency. Read back every output; report raw/committed identities separately.

Stage exact paths and publish without force when authorized; fetch and verify remote SHA and artifacts. Return trigger, old/new paths, queue continuity, unchanged next ID, byte verification and actual publication status.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and deliver the card, intake row and footer (full mini when it fits, ENV-v1) after every game request. No model, runtime, receipt or manifest is needed or recorded. Canonical P-ID assignment belongs exclusively to prompt 4 import. Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Carry any legacy execution-manifest/attempt/bundle/feedback custody pointers and the open repair queue into the continuity report unchanged; prompt 6 owns them. A rollover must not manufacture runs or feedback, refit old cards or copy forecasts. Canonical-md-1 is unchanged.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Return the researched card with its intake row and footer (and the full mini when it fits, ENV-v1) after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.

## Persistent sourcing and information closure (EXH-v1)

Carry the current source-register and exact outstanding requirement/attempt pointers through rollover without duplicating facts, closing a gap or allocating an ID. Missing evidence remains open; preserve closed-part and source bytes. Research continuation uses EXH-v1 and current source observations.

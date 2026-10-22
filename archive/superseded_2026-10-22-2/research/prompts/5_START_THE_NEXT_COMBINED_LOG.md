# PROMPT 5 — Roll over the Combined Log without consuming IDs

**Local keys until settlement; updated mini after every game (MINI-v2).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Research and mini creation (prompts 1–2) use stable local event keys and never assign or reserve canonical P-IDs. A canonical P-ID is assigned only in an event's settlement phase: prompt 3 settles the event and then runs the prompt-4 import, which assigns the ID. After each prompt-1 game request the repository agent appends the card to the active mini under `research/active_minis/`, updates intake and footer, reads the file back, and commits and pushes it. Preserve every owner-entered Upcoming game block and all earlier issued bytes. Formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.22-v23.0 · COMBINED_LOG_ROLLOVER · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Default trigger: working file exceeds 1.5 MB, contains at least 50 canonical entries, or cannot be opened/rendered reliably. Record the actual trigger/measurement; rollover is not required to settle or import. Run between complete imports.

**ML/RL scope (MLSCOPE-v2).** Owner instruction, 22 October 2026: models run where they are needed, beside the analyst card and never inside it. Prompt 1 researches the game online and prices every p_card as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY from one declared distribution ([PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md); code may do the arithmetic, with every input and step printed). Only after the card is written to the mini does prompt 1 run the pregame model shadow, which freezes the model and league-baseline rows, and the card's own p_card, on the same contracts when the competition has an active release, or records NOT_RUN_NO_RELEASE. Model output never changes a card's p_card, ranks or picks. Prompt 3 settles the shadow with the card; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only after at least 8 weeks and 50 paired games; a progress review falls due when either is reached first. RL has no forecasting role: online expert weighting updates at settlement. Details: [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Supersedes MLSCOPE-v1, NOCODE-v1 and any older text that forbids code or models in prompts 1–5.

**Execution environment (ENV-v2).** Owner instruction, 22 October 2026: every prompt, 1 to 8, runs in this repository as the repository agent (`LOCAL_WORKING_TREE`), with internet access for research. Controls are read from the local working tree; GitHub `main` is the published copy, and every run that changes files ends with a commit and push. The external-chat route (ENV-v1) is retired for new work; anything it produced earlier is still imported as before. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

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

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and append the card, intake row and footer to the active mini after every game request (ENV-v2). The card never waits for or depends on a model; a model shadow run after the card (MLSCOPE-v2) is recorded beside it. Canonical P-ID assignment happens only in the settlement phase (prompt 3, through the prompt-4 import). Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Carry any legacy execution-manifest/attempt/bundle/feedback custody pointers and the open repair queue into the continuity report unchanged; prompt 6 owns them. A rollover must not manufacture runs or feedback, refit old cards or copy forecasts. Canonical-md-1 is unchanged.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card, its intake row and footer to the active mini, read it back and commit it after each game request (ENV-v2). Canonical IDs are assigned only in the settlement phase, when prompt 3 hands the settled event to the prompt-4 import, which reconciles duplicates and identity and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.

## Persistent sourcing and information closure (EXH-v1)

Carry the current source-register and exact outstanding requirement/attempt pointers through rollover without duplicating facts, closing a gap or allocating an ID. Missing evidence remains open; preserve closed-part and source bytes. Research continuation uses EXH-v1 and current source observations.

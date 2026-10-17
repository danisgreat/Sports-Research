# PROMPT 3 — Freeze, settle and review a local mini

**No canonical assignment here.** Preserve local event keys through original copies, settlement markers, queues and manifests. For unimported new cards LOCAL_ID_MAPPING says canonical ID NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT; never plan P-numbers here. Existing canonical references retain their real mappings. S18 checks this handoff. Retain reviewed labels locally by local key; defer the canonical-only research_learning exporter until prompt 4 has assigned and verified the mapping.

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, return the new card with its intake row and footer, plus the full mini when it fits, for the owner to save (ENV-v1). Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.17-v22.1 · LOCAL_MINI_SETTLEMENT.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). **EXTERNAL_CHAT** (ENV-v1). Writes: nothing; returns one settlement document with dated revisions in the reply for the owner to save (ENV-v1 §5); no canonical/GitHub writes. Original cards are immutable. Settle the original probabilities by hand; no code, model, runtime, feedback command or shadow settlement runs here (MLSCOPE-v1: prompt 6 owns model feedback and shadow comparisons). Historical MODEL_ASSISTED cards are settled on their frozen contracts like any other card; their bundles and feedback are left untouched for prompt 6. The decision lab is excluded.

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Execution environments (ENV-v1).** Prompts 1–3 run in an external chat with internet access and read-only access to the GitHub repository at the latest `main` commit: no code, no repository writes, no hashes, a section-level reading budget, and every output returned in the reply for the owner to save. Prompts 4–8 run in this repository as the repository agent (`LOCAL_WORKING_TREE`); prompt 4 is the only intake point for external-chat output and computes the byte counts and SHA-256 the chat cannot. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## Inputs

- Active mini or previously frozen package: attached or pasted by the owner, or committed in the repository at the latest `main` commit. State its file name, card count and first/last local key.
- Output: one settlement document, suggested name `research/active_minis/<MINI_KEY>_SETTLEMENT.md`, returned in the reply.
- Carryovers/prior revisions: supplied by the owner or committed, or discover.
- Evidence tasks: exact fields, or ALL.
- Authority: the latest `main` commit, pinned by its full SHA (prompts 1–3 never use local controls).

## 1. Read, inventory and freeze

Read common controls/protocol, scoring, verification, current status, sport/league rules, SOURCES, availability protocol and actual original cards/addenda. Print the reading receipt, authority SHA, exposure/availability limits and gaps. Inventory every card, supplied row, addendum, revision, pending event and terminal evidence gap. Preserve each mini's original format.

Freeze the supplied mini before settlement: record FROZEN_SOURCE with its file name, complete block inventory (every card key, addendum and revision, in order), card count, freeze time and writer hand-over. Its byte count and SHA-256 are PENDING_PROMPT_4: prompt 4 computes them at intake (ENV-v1 §6). New events go to the next authorized mini. Recheck the supplied text for later blocks and account for them instead of silently omitting them.

Return one settlement document in mini-settlement-10 sections: settlement blocks and revisions per card, LOCAL_ID_MAPPING, UNRESOLVED_CARRYOVER and SETTLEMENT_MANIFEST. Do not reproduce the frozen cards; name the frozen mini by file name and inventory. Prompt 4 joins the frozen mini and this document into PREDICTION_MINI_SETTLED at intake. A rerun returns a new revision document; never overwrite an earlier one.

Before scoring, preserve actual issue phase and independent pre-start-input proof under TIMING_RESEARCH_PROTOCOL. No settlement creates a pre-start freeze/issue receipt; late-issued clean-input research is separately scored and is never prospective pre-start issuance.

## 2. Establish outcomes and exact terms

Retrieve official terminal state and exact field-owner outcomes with permitted corroboration. Match frozen event/participant orientation/line/period/endpoint and activation/action/void/retirement/extras terms to the competition-season rules. Record definition status, source URL, field/extract, publication/update/retrieval time, evidence grade, failures/conflicts and unknown lineage.

Late lineups or participation can diagnose an original process gap; they cannot prove pre-issue knowability. Do not backfill original starters, probabilities, baselines, ranks or timestamps.

WIN/LOSS/PUSH need sufficient evidence; VOID needs the frozen void condition. Missing/conflicting result or definition is UNRESOLVED. A bound gives a definite grade only if every feasible value agrees. Sporting convention and unknown operator settlement are separate. Pending events receive state evidence and next action, not guessed finals.

## 3. Append settlements and retrospectives

Each revision has a unique per-original-record-key revision key, parent(s), effective time, affected contract keys, old/new values, source and reason. Resolve one valid chain per key; branching conflicts stay UNRESOLVED until a resolving revision names them. Do not choose the last row or count a key twice.

Copy original rank/proposition/p_card/BASELINE_P/expected score literally. Count W/L/PUSH/VOID/UNRESOLVED separately; only original ranks 1–2 are primary. Informational, reforecast and frozen shadow wins never replace losses. Compute proper scores only from issued numeric probabilities with correct conditioning; full vectors are scored separately. Missing original p, SD or baseline stays missing.

Complete R1–R12 for every terminal card, including wins and partial settlements; explain unavailable parts. Every Rank-1 LOSS gets eight parts: exact claim; verified outcome; original-distribution check; cutoff knowability; process/model/variance assessment; cutoff-only counterfactual; failure class; testable correction. No invented blame percentages, post-event rank replacement or miscalibration inference from one loss. Check matched wins for the same defects.

## 4. Model shadows (deferred to prompt 6)

Not performed here (MLSCOPE-v1). List the events that have frozen model shadows or legacy bundles so prompt 6 can settle and compare them; never read model outputs while settling the original card.

## 5. Verify and return

Run S1–S18 for new mini-settlement-10 (S1–S17 for legacy mini-settlement-9; S1–S16 for mini-settlement-8) and applicable original-format card checks with evidence. Reconcile every frozen card, mapping and revision against the inventory and re-read the returned document. Check source growth, markers, unconditional/decisive denominators and queue responsibilities. Verified final time drives SLA; absent final time means UNKNOWN, an estimate is triage only.

Return the settlement document, frozen-source identity (file name and inventory), full inventory, revisions/grades, primary denominators, pending/unresolved queues, deep-review coverage, optional shadow comparison/exclusions and verification limits. Canonical import PENDING; GitHub writes NO. A retry plan is not an executed or scheduled capture.


For new RC-v1 research records, inspect the A9 completion matrix and retain actual procedure gaps in the process review; missing calibration is separate. Analyst comparison rows labelled NOT_PRIMARY never become original primary picks or ML feedback. Old cards retain their original formats; do not retrofit a completion receipt or delay independently supported settlement because research was incomplete.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and deliver the card, intake row and footer (full mini when it fits, ENV-v1) after every game request. No model, runtime, receipt or manifest is needed or recorded. Canonical P-ID assignment belongs exclusively to prompt 4 import. Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Leave any legacy execution manifest and bundles untouched for prompts 4 and 6; new no-code minis have none. New settlement documents use mini-settlement-10. Run S16 by hand against the frozen mini.

Settle every card equally. Record verified event/contract outcomes in the settlement so prompt 6 can use them as learning candidates; partial/unknown outcomes remain queued.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Return the researched card with its intake row and footer (and the full mini when it fits, ENV-v1) after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Settle legacy originals without retroactive compliance

An original produced under earlier rules retains its actual method, format, probabilities, rank roles, endpoint definitions and timing. Never rewrite it to claim current online-history or confirmed-player research occurred. Research current terminal outcomes for its exact frozen contracts, preserve source/definition/custody gaps, and separate conditional sporting grades, operator action, analyst diagnostics and actual model scores. A complete available canonical original may be cited separately by exact repository path and commit when a local mini contains only its pointer; never reconstruct a missing draft or insert it into the frozen source.

## Persistent sourcing and information closure (EXH-v1)

Produce the mandatory visible **Source discovery, corroboration and reuse register** in the settled output and standalone report, plus the source-discovery, search-attempt and requirement-closure tables as Markdown with the template columns (prompt 4 saves them as SOURCE_DISCOVERY_REGISTER.csv, SOURCE_SEARCH_ATTEMPTS.csv and REQUIREMENT_CLOSURE.csv at intake). Consult/recheck shared and prior package entries, then actively pursue every missing outcome/period/statistic/definition/final-time/custody field through alternative sources and verify material facts independently. Do not stop when the first final score is found. New package mini-settlement-10 runs S1-S18. Any required field/corroboration still open means INFORMATION_INCOMPLETE, even if supported sporting rows can be settled and retained. No false completion, invented operator terms, backfilled pregame evidence, silent shared writes or unscheduled retry claim.

## Learning record and mini-level diagnostics (LEARN-v2)

After the original contracts are settled, record in the settlement package, as Markdown tables, each settled event's final score, regulation score, decision, final time and terminal source (URL, retrieved time), next to each card's learning record. Prompt 6 converts these records into the learning store under [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md); this prompt writes no CSV export and runs no command.

Account separately for settled unique events, events still pending and events with incomplete learning records. This mini settlement (about 40–50 games) is the first review level: report preliminary calibration and BASELINE_P diagnostics computed by hand (Brier per row, PROBABILITY_TOOLKIT §10) and data-integrity findings only. Never declare a method superior here, and never change ranks. Record a MINI_SETTLEMENT review row in the package (disposition usually NO_CHANGE, INSUFFICIENT_EVIDENCE or DATA_REPAIR_REQUIRED) for prompt 6 to append to `research/learning_status/REVIEW_LOG.csv`.


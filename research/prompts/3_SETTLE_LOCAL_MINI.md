# PROMPT 3 — Freeze, settle and review a local mini

**Canonical assignment happens in this settlement phase, through the prompt-4 import (MINI-v2).** Preserve local event keys through original copies, settlement markers, queues and manifests. The settlement document's own LOCAL_ID_MAPPING says canonical ID NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT; never plan P-numbers while settling. When the settlement is written and verified, run [prompt 4](4_CANONICAL_IMPORT.md) on it in the same session (section 6): that import alone assigns the IDs and records the final mapping. Events that stay pending are not imported and get no ID. Existing canonical references retain their real mappings. S18 checks this handoff. Retain reviewed labels locally by local key; defer the canonical-only research_learning exporter until prompt 4 has assigned and verified the mapping.

**Local keys until settlement; updated mini after every game (MINI-v2).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Research and mini creation (prompts 1–2) use stable local event keys and never assign or reserve canonical P-IDs. A canonical P-ID is assigned only in an event's settlement phase: prompt 3 settles the event and then runs the prompt-4 import, which assigns the ID. After each prompt-1 game request the repository agent appends the card to the active mini under `research/active_minis/`, updates intake and footer, reads the file back, and commits and pushes it. Preserve every owner-entered Upcoming game block and all earlier issued bytes. Formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.22-v23.0 · LOCAL_MINI_SETTLEMENT.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). **LOCAL_WORKING_TREE** (ENV-v2). Writes: the frozen mini's source identity, one settlement document with dated revisions at `research/active_minis/<MINI_KEY>_SETTLEMENT.md`, the model-shadow settlements of section 4, then the prompt-4 import of section 6 and a commit and push. Original cards are immutable. Settle the original probabilities from the frozen card; the model never re-grades or replaces them. Historical MODEL_ASSISTED cards are settled on their frozen contracts like any other card. The decision lab is excluded.

**ML/RL scope (MLSCOPE-v2).** Owner instruction, 22 October 2026: models run where they are needed, beside the analyst card and never inside it. Prompt 1 researches the game online and prices every p_card as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY from one declared distribution ([PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md); code may do the arithmetic, with every input and step printed). Only after the card is written to the mini does prompt 1 run the pregame model shadow, which freezes the model and league-baseline rows, and the card's own p_card, on the same contracts when the competition has an active release, or records NOT_RUN_NO_RELEASE. Model output never changes a card's p_card, ranks or picks. Prompt 3 settles the shadow with the card; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only after at least 8 weeks and 50 paired games; a progress review falls due when either is reached first. RL has no forecasting role: online expert weighting updates at settlement. Details: [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Supersedes MLSCOPE-v1, NOCODE-v1 and any older text that forbids code or models in prompts 1–5.

**Execution environment (ENV-v2).** Owner instruction, 22 October 2026: every prompt, 1 to 8, runs in this repository as the repository agent (`LOCAL_WORKING_TREE`), with internet access for research. Controls are read from the local working tree; GitHub `main` is the published copy, and every run that changes files ends with a commit and push. The external-chat route (ENV-v1) is retired for new work; anything it produced earlier is still imported as before. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## Inputs

- Active mini or previously frozen package: in the working tree, or attached by the owner (copied byte-for-byte under `research/active_minis/received/` first). State its file name, card count and first/last local key.
- Output: one settlement document, `research/active_minis/<MINI_KEY>_SETTLEMENT.md`, written here.
- Carryovers/prior revisions: supplied by the owner or committed, or discover.
- Evidence tasks: exact fields, or ALL.
- Authority: the local working tree (`LOCAL_WORKING_TREE`), with branch and HEAD SHA recorded.

## 1. Read, inventory and freeze

Read common controls/protocol, scoring, verification, current status, sport/league rules, SOURCES, availability protocol and actual original cards/addenda. Print the reading receipt, authority SHA, exposure/availability limits and gaps. Inventory every card, supplied row, addendum, revision, pending event and terminal evidence gap. Preserve each mini's original format.

Freeze the supplied mini before settlement: record FROZEN_SOURCE with its file name, complete block inventory (every card key, addendum and revision, in order), card count, freeze time and writer hand-over. Compute and record its byte count and SHA-256 now, before any settlement text is written. New events go to the next authorized mini. Recheck the supplied text for later blocks and account for them instead of silently omitting them.

Write one settlement document in mini-settlement-10 sections: settlement blocks and revisions per card, LOCAL_ID_MAPPING, UNRESOLVED_CARRYOVER and SETTLEMENT_MANIFEST. Do not reproduce the frozen cards; name the frozen mini by file name and inventory. The section-6 import joins the frozen mini and this document into PREDICTION_MINI_SETTLED. A rerun writes a new revision document; never overwrite an earlier one.

Before scoring, preserve actual issue phase and independent pre-start-input proof under TIMING_RESEARCH_PROTOCOL. No settlement creates a pre-start freeze/issue receipt; late-issued clean-input research is separately scored and is never prospective pre-start issuance.

## 2. Establish outcomes and exact terms

Retrieve official terminal state and exact field-owner outcomes with permitted corroboration. Match frozen event/participant orientation/line/period/endpoint and activation/action/void/retirement/extras terms to the competition-season rules. Record definition status, source URL, field/extract, publication/update/retrieval time, evidence grade, failures/conflicts and unknown lineage.

Late lineups or participation can diagnose an original process gap; they cannot prove pre-issue knowability. Do not backfill original starters, probabilities, baselines, ranks or timestamps.

WIN/LOSS/PUSH need sufficient evidence; VOID needs the frozen void condition. Missing/conflicting result or definition is UNRESOLVED. A bound gives a definite grade only if every feasible value agrees. Sporting convention and unknown operator settlement are separate. Pending events receive state evidence and next action, not guessed finals.

## 3. Append settlements and retrospectives

Each revision has a unique per-original-record-key revision key, parent(s), effective time, affected contract keys, old/new values, source and reason. Resolve one valid chain per key; branching conflicts stay UNRESOLVED until a resolving revision names them. Do not choose the last row or count a key twice.

Copy original rank/proposition/p_card/BASELINE_P/expected score literally. Count W/L/PUSH/VOID/UNRESOLVED separately; only original ranks 1–2 are primary. Informational, reforecast and frozen shadow wins never replace losses. Compute proper scores only from issued numeric probabilities with correct conditioning; full vectors are scored separately. Missing original p, SD or baseline stays missing.

Complete R1–R12 for every terminal card, including wins and partial settlements; explain unavailable parts. Every Rank-1 LOSS gets eight parts: exact claim; verified outcome; original-distribution check; cutoff knowability; process/model/variance assessment; cutoff-only counterfactual; failure class; testable correction. No invented blame percentages, post-event rank replacement or miscalibration inference from one loss. Check matched wins for the same defects.

## 4. Model shadows (MLSCOPE-v2)

Settle the original card first. Then, for each settled event with an accepted pregame attempt (its receipt under `research/pregame/<local key>/` and attempt under `research/cycle_attempts/<local key>/`), write the verified final into a settlement export with its capture and known-at time, and run `python -m ml cycle settle --bundle <attempt>/BUNDLE --export <export> --store research/learning_store --out research/cycle_feedback/<local key>_REV<n>`. A refused or failed settle is recorded with its exact error; it never changes a card grade. List events whose shadow was NOT_RUN with the disposition from the card. Shadow results are reported in their own table, never as card wins or losses.

## 5. Verify and return

Run S1–S18 for new mini-settlement-10 (S1–S17 for legacy mini-settlement-9; S1–S16 for mini-settlement-8) and applicable original-format card checks with evidence. Reconcile every frozen card, mapping and revision against the inventory and re-read the returned document. Check source growth, markers, unconditional/decisive denominators and queue responsibilities. Verified final time drives SLA; absent final time means UNKNOWN, an estimate is triage only.

Report the settlement document path, frozen-source identity (file name, bytes, SHA-256 and inventory), full inventory, revisions/grades, primary denominators, pending/unresolved queues, deep-review coverage, the model-shadow settlements and verification limits, then continue with section 6. A retry plan is not an executed or scheduled capture.

## 6. Settlement-phase canonical assignment

Run [prompt 4](4_CANONICAL_IMPORT.md) on the frozen mini and this settlement in the same session. It reconciles identity and duplicates, assigns new canonical IDs to the settled events only, appends them to the active Combined Log, records the final mapping and updates current state. Pending events stay in the mini's carryover with canonical ID NOT_ASSIGNED and move to the next mini. Commit and push the settlement, shadow settlements and import together, and report the commit.


For new RC-v1 research records, inspect the A9 completion matrix and retain actual procedure gaps in the process review; missing calibration is separate. Analyst comparison rows labelled NOT_PRIMARY never become original primary picks or ML feedback. Old cards retain their original formats; do not retrofit a completion receipt or delay independently supported settlement because research was incomplete.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and append the card, intake row and footer to the active mini after every game request (ENV-v2). The card never waits for or depends on a model; a model shadow run after the card (MLSCOPE-v2) is recorded beside it. Canonical P-ID assignment happens only in the settlement phase (prompt 3, through the prompt-4 import). Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Leave any legacy execution manifest and bundles untouched; new minis have none (model shadows keep their own receipts). New settlement documents use mini-settlement-10. Run S16 by hand against the frozen mini.

Settle every card equally. Record verified event/contract outcomes in the settlement so prompt 6 can use them as learning candidates; partial/unknown outcomes remain queued.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card, its intake row and footer to the active mini, read it back and commit it after each game request (ENV-v2). Canonical IDs are assigned only in the settlement phase, when prompt 3 hands the settled event to the prompt-4 import, which reconciles duplicates and identity and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Settle legacy originals without retroactive compliance

An original produced under earlier rules retains its actual method, format, probabilities, rank roles, endpoint definitions and timing. Never rewrite it to claim current online-history or confirmed-player research occurred. Research current terminal outcomes for its exact frozen contracts, preserve source/definition/custody gaps, and separate conditional sporting grades, operator action, analyst diagnostics and actual model scores. A complete available canonical original may be cited separately by exact repository path and commit when a local mini contains only its pointer; never reconstruct a missing draft or insert it into the frozen source.

## Persistent sourcing and information closure (EXH-v1)

Produce the mandatory visible **Source discovery, corroboration and reuse register** in the settled output and standalone report, plus the source-discovery, search-attempt and requirement-closure tables as Markdown with the template columns (prompt 4 saves them as SOURCE_DISCOVERY_REGISTER.csv, SOURCE_SEARCH_ATTEMPTS.csv and REQUIREMENT_CLOSURE.csv at intake). Consult/recheck shared and prior package entries, then actively pursue every missing outcome/period/statistic/definition/final-time/custody field through alternative sources and verify material facts independently. Do not stop when the first final score is found. New package mini-settlement-10 runs S1-S18. Any required field/corroboration still open means INFORMATION_INCOMPLETE, even if supported sporting rows can be settled and retained. No false completion, invented operator terms, backfilled pregame evidence, silent shared writes or unscheduled retry claim.

## Learning record and mini-level diagnostics (LEARN-v2)

After the original contracts are settled, record in the settlement package, as Markdown tables, each settled event's final score, regulation score, decision, final time and terminal source (URL, retrieved time), next to each card's learning record. Prompt 6 converts these records into the learning store under [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md); apart from the section-4 settlement exports of shadowed events, this prompt writes no learning-store export.

Account separately for settled unique events, events still pending and events with incomplete learning records. This mini settlement (about 40–50 games) is the first review level: report preliminary calibration and BASELINE_P diagnostics computed by hand (Brier per row, PROBABILITY_TOOLKIT §10) and data-integrity findings only. Never declare a method superior here, and never change ranks. Record a MINI_SETTLEMENT review row in the package (disposition usually NO_CHANGE, INSUFFICIENT_EVIDENCE or DATA_REPAIR_REQUIRED) for prompt 6 to append to `research/learning_status/REVIEW_LOG.csv`.


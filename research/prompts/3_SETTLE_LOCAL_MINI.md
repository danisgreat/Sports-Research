# PROMPT 3 — Freeze, settle and review a local mini

**Canonical assignment happens in this settlement phase, through the prompt-4 import (MINI-v2).** Preserve local event keys through original copies, settlement markers, queues and manifests. The settlement document's own LOCAL_ID_MAPPING says canonical ID NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT; never plan P-numbers while settling. When the settlement is written and verified, run [prompt 4](4_CANONICAL_IMPORT.md) on it in the same session (section 6): that import alone assigns the IDs and records the final mapping. Events that stay pending are not imported and get no ID. Existing canonical references retain their real mappings. S18 checks this handoff. Retain reviewed labels locally by local key; defer the canonical-only research_learning exporter until prompt 4 has assigned and verified the mapping.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**P-2026.10.22-v24.0 · LOCAL_MINI_SETTLEMENT.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). **LOCAL_WORKING_TREE** (ENV-v2). Writes: the frozen mini's source identity, one settlement document with dated revisions at `research/active_minis/<MINI_KEY>_SETTLEMENT.md`, the ledger inputs and frozen-row settlements of section 4, then the prompt-4 import of section 6 and a commit and push. Original cards are immutable. Settle the original probabilities from the frozen card; the model never re-grades or replaces them. Historical MODEL_ASSISTED cards are settled on their frozen contracts like any other card. The decision lab is excluded.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

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

## 4. Reference, model rows and the adjustment ledger (MLSCOPE-v3 / LEDGER-v1)

Settle the original card first. Then:

1. **Ledger inputs.** For every v24.0 card settled, write `RESULTS.csv` (`local_key,label,grade` for every picks row: WIN, LOSS, PUSH, VOID or UNRESOLVED from the section 2 evidence) and `ACTUALS.csv` (`local_key,quantity,actual`: home minus away for MARGIN, home plus away for TOTAL) under the settlement document's evidence folder. Take the scores from a box score or linescore with a sum check, never from a headline or video title. A row whose result is unresolved stays UNRESOLVED.
2. **Frozen model rows.** For each settled event with an accepted attempt (its receipt under `research/pregame/<local key>/` and attempt under `research/cycle_attempts/<local key>/`), write the verified final into a settlement export with its capture and known-at time, and run `python -m ml cycle settle --bundle <attempt>/BUNDLE --export <export> --store research/learning_store --out research/cycle_feedback/<local key>_REV<n>`. A refused or failed settle is recorded with its exact error; it never changes a card grade. List events whose reference or model stage was NOT_RUN with the disposition from the card. Frozen-row results are reported in their own table, never as card wins or losses.
3. **League-day events** (no card): `python -m ml league-day settle --competition C --date D --cache <dir outside the repository>` ingests the date's finals (two lineages must agree) and settles every frozen bundle of the date into `research/cycle_feedback/`.
4. **Benchmarks.** Only if the owner supplies them, a benchmarks file in the exact format of [BENCHMARK_PROTOCOL](../../BENCHMARK_PROTOCOL.md), entered after the verified final and as probabilities only. Never search for a price, line or odds. A missing benchmark is a missing table row, not a reason to delay settlement.
5. **Scoring.** When the scope is large enough, `python -m ml ledger score --results RESULTS.csv [--benchmarks B.csv] --out <new folder>` and `python -m ml ledger coverage --actuals ACTUALS.csv --out <new folder>`; report the paired differences with their intervals and strata exactly as SCORING_AND_VALIDATION §12 defines them. The ledger scoring is prompt 6's monthly work; prompt 3 supplies its inputs.

## 5. Verify and return

Run S1–S19 for new mini-settlement-10 (S1–S17 for legacy mini-settlement-9; S1–S16 for mini-settlement-8) and applicable original-format card checks with evidence. Reconcile every frozen card, mapping and revision against the inventory and re-read the returned document. Check source growth, markers, unconditional/decisive denominators and queue responsibilities. Verified final time drives SLA; absent final time means UNKNOWN, an estimate is triage only.

Report the settlement document path, frozen-source identity (file name, bytes, SHA-256 and inventory), full inventory, revisions/grades, primary denominators, pending/unresolved queues, deep-review coverage, the ledger inputs, the frozen-row settlements and verification limits, then continue with section 6. A retry plan is not an executed or scheduled capture.

## 6. Settlement-phase canonical assignment

Run [prompt 4](4_CANONICAL_IMPORT.md) on the frozen mini and this settlement in the same session. It reconciles identity and duplicates, assigns new canonical IDs to the settled events only, appends them to the active Combined Log, records the final mapping and updates current state. Pending events stay in the mini's carryover with canonical ID NOT_ASSIGNED and move to the next mini. Commit and push the settlement, shadow settlements and import together, and report the commit.

For new RC-v1 research records, inspect the A9 completion matrix and retain actual procedure gaps in the process review; missing calibration is separate. Analyst comparison rows labelled NOT_PRIMARY never become original primary picks or ML feedback. Old cards retain their original formats; do not retrofit a completion receipt or delay independently supported settlement because research was incomplete.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Defined in [RESEARCH_RETENTION_PROTOCOL](../../RESEARCH_RETENTION_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

Leave any legacy execution manifest and bundles untouched; new minis have none (model shadows keep their own receipts). New settlement documents use mini-settlement-10. Run S16 by hand against the frozen mini.

Settle every card equally. Record verified event/contract outcomes in the settlement so prompt 6 can use them as learning candidates; partial/unknown outcomes remain queued.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

## Settle legacy originals without retroactive compliance

An original produced under earlier rules retains its actual method, format, probabilities, rank roles, endpoint definitions and timing. Never rewrite it to claim current online-history or confirmed-player research occurred. Research current terminal outcomes for its exact frozen contracts, preserve source/definition/custody gaps, and separate conditional sporting grades, operator action, analyst diagnostics and actual model scores. A complete available canonical original may be cited separately by exact repository path and commit when a local mini contains only its pointer; never reconstruct a missing draft or insert it into the frozen source.

## Persistent sourcing and information closure (EXH-v1)

Produce the mandatory visible **Source discovery, corroboration and reuse register** in the settled output and standalone report, plus the source-discovery, search-attempt and requirement-closure tables as Markdown with the template columns (prompt 4 saves them as SOURCE_DISCOVERY_REGISTER.csv, SOURCE_SEARCH_ATTEMPTS.csv and REQUIREMENT_CLOSURE.csv at intake). Consult/recheck shared and prior package entries, then actively pursue every missing outcome/period/statistic/definition/final-time/custody field through alternative sources and verify material facts independently. Do not stop when the first final score is found. New package mini-settlement-10 runs S1-S18. Any required field/corroboration still open means INFORMATION_INCOMPLETE, even if supported sporting rows can be settled and retained. No false completion, invented operator terms, backfilled pregame evidence, silent shared writes or unscheduled retry claim.

## Learning record and mini-level diagnostics (LEARN-v2)

After the original contracts are settled, record in the settlement package, as Markdown tables, each settled event's final score, regulation score, decision, final time and terminal source (URL, retrieved time), next to each card's learning record. Prompt 6 converts these records into the learning store under [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md); apart from the section-4 settlement exports of shadowed events, this prompt writes no learning-store export.

Account separately for settled unique events, events still pending and events with incomplete learning records. This mini settlement (about 40–50 games) is the first review level: report preliminary calibration and BASELINE_P diagnostics computed by hand (Brier per row, PROBABILITY_TOOLKIT §10) and data-integrity findings only. Never declare a method superior here, and never change ranks. Record a MINI_SETTLEMENT review row in the package (disposition usually NO_CHANGE, INSUFFICIENT_EVIDENCE or DATA_REPAIR_REQUIRED) for prompt 6 to append to `research/learning_status/REVIEW_LOG.csv`.


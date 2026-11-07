# Workflow: where prompts run, local keys and delivery

**Merged 2026-11-07, CR-2026.11.07-R2 (FORMAT).** This document joins the files below, verbatim and in this order. Nothing was reworded. Each source's title line became its part heading. The banner paragraphs that every source repeated appear once, below. Links to the old files now point to their parts, and the originals are kept unchanged in [archive/consolidation_2026-11-07/merged_sources/](archive/consolidation_2026-11-07/merged_sources/).

| Part | Former file | Bytes | SHA-256 of the original |
|---|---|---:|---|
| [A](#part-a-execution_environment_protocol) | `EXECUTION_ENVIRONMENT_PROTOCOL.md` | 5,810 | `a44839f15fc8357a826ec45ddeb3d8b238c91723020f74f5b422e9ccc43f4b98` |
| [B](#part-b-mini_log_identity_protocol) | `MINI_LOG_IDENTITY_PROTOCOL.md` | 11,720 | `cb11c76b710f8f6bfe61d9c72ace9daff216bb9c7f1a62406ad09c4867e4def7` |

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](#part-a-execution_environment_protocol); summarised in [CORE](CORE.md) §1.

---

# Part A: EXECUTION_ENVIRONMENT_PROTOCOL

*Formerly `EXECUTION_ENVIRONMENT_PROTOCOL.md` (original title: Execution environment: every prompt runs in the repository (ENV-v2)). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/EXECUTION_ENVIRONMENT_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/EXECUTION_ENVIRONMENT_PROTOCOL.md).*

**ENV-2026.10.22-v2 · MDS-2026.10.22-v24.0 · CR-2026.10.22-R2 · P-2026.10.22-v24.0.** Owner instruction, 22 October 2026: the game logs are run here, not in an external chat. Every prompt, 1 to 8, is run in this repository by the repository agent (Claude Code on the owner's PC), with internet access for research. This supersedes ENV-v1 (17 October 2026), under which prompts 1–3 ran in an external chat; its text is archived in [archive/superseded_2026-10-22-1/](archive/superseded_2026-10-22-1/EXECUTION_ENVIRONMENT_PROTOCOL.md). Probabilities, selection, scoring and issued records are unchanged; delivery, model-shadow timing and the canonical assignment stage change (sections 3–5).

## 1. Who runs what

| Prompt | Environment | Authority | Writes | Model work (MLSCOPE-v3) |
|---|---|---|---|---|
| 1 Game card | REPOSITORY_AGENT, internet research | `LOCAL_WORKING_TREE` | Reference receipt and frozen rows; card, picks block, intake row and footer in the active mini; ledger rows; commit and push | Before the card: the reference stage (`pregame reference` or `reference run`); after it: `python -m ml pregame run` |
| 2 Start mini | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | New mini, active-mini pointer; commit and push | None |
| 3 Settle mini | REPOSITORY_AGENT, internet research | `LOCAL_WORKING_TREE` | Frozen-source identity, settlement document, RESULTS.csv and ACTUALS.csv, shadow settlements, then the prompt-4 import; commit and push | `python -m ml cycle settle` for frozen events |
| 4 Import | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | Canonical suffix, mapping, state; run by prompt 3 or alone | None |
| 5–8 | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | As each prompt declares | 6 evaluates (`pregame status`, `cycle evaluate`, `pregame compare-card`, `ledger score`, `ledger coverage`); 8 releases |

`PUBLISHED_MAIN_PINNED` remains valid only for an agent working outside the repository (the retired ENV-v1 route). Its outputs are taken in through prompt 4's intake, unchanged.

## 2. Reading

Read controls from the working tree. Print branch, HEAD SHA, read time with offset and every uncommitted control difference in the reading receipt (CURRENT_RULES §0). The section-level reading budget of ENV-v1 no longer applies: read what the prompt names, in full where it says so. GitHub `main` is the published copy and the fallback for an unreadable local file (REF-v1).

Research is done on the internet with the agent's own tools, from verifiable sources that carry comprehensive, accurate data for the exact game: competition and team field owners, official injury and line-up publications, league match centres and box scores, and the permitted structured providers in [SOURCES](SOURCES.md). Open each source; record its URL, the field used, publication and retrieval times, and an independent corroboration for every material fact (HISTORICAL_SOURCE_PROTOCOL, ROSTER_AVAILABILITY_PROTOCOL, RESEARCH_EXHAUSTIVENESS_PROTOCOL). A search snippet is not an opened source. Odds, tips, previews and fantasy content are never inputs.

## 3. Prompt 1 and 2 delivery

- **Prompt 2** writes the new mini to `research/active_minis/<MINI_KEY>.md`, points CURRENT_STATE at it and commits and pushes.
- **Prompt 1** appends the complete card immediately before the active mini's footer, updates intake and footer, reads the whole file back, then runs the pregame model shadow and adds its block to the card. It commits and pushes the mini, the receipt and the frozen rows, before the scheduled start whenever possible: the pushed commit is the externally checkable freeze. The reply summarises the picks, the likely winner, the reasons and sources, the shadow disposition and the commit.
- Owner material produced elsewhere (an attached mini, a pasted card) is first copied byte-for-byte under `research/active_minis/received/` and then used; it is never retyped into a frozen source.
- Never claim a write, commit or push that did not happen. A failed write or push is reported with its exact error, and the research is kept.

## 4. Prompt 3 delivery and canonical assignment

- Prompt 3 freezes the mini and records its byte count and SHA-256 itself; FROZEN_SOURCE is no longer PENDING_PROMPT_4.
- It writes the settlement document, settles the model shadows of shadowed events and then runs prompt 4 on the frozen mini and settlement in the same session. **Canonical IDs are assigned only in this settlement phase** (MINI-v2): settled events receive their IDs; pending events stay in the carryover with canonical ID NOT_ASSIGNED and move to the next mini.

## 5. Reference and model timing (MLSCOPE-v3)

The declared reference is frozen **before** the card's probabilities are written: a tier A release by `python -m ml pregame reference`, a TB-2-MD or baseline reference by `python -m ml reference run`. The pregame command refuses to freeze the card unless the card's BEGIN and END markers are already in the mini, and refuses a `card_p` value that is not printed in that card. The card's own final p_card is frozen beside the reference and the league baseline on identical contracts, so the three can be compared prospectively. A reference already frozen is reused, never rerun. Details: [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol), [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md).

## 6. Limits

- Agent arithmetic can still be wrong. Printed inputs and steps, the toolkit §11 checks and readback are the controls.
- A pushed commit time proves when bytes were published, not when a source was published; source times are recorded separately and an unverifiable time is labelled, never assumed.
- Drive (DRIVE-v2) remains an optional drop box for owner material; it is never a control.

---

# Part B: MINI_LOG_IDENTITY_PROTOCOL

*Formerly `MINI_LOG_IDENTITY_PROTOCOL.md` (original title: Local mini identity, canonical import and document delivery). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/MINI_LOG_IDENTITY_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/MINI_LOG_IDENTITY_PROTOCOL.md).*

**MINI-2026.10.22-v2 · MDS/P v23.0 · CR-2026.10.22-R1.** Owner instruction, 22 October 2026: canonical P-IDs are assigned only in an event's settlement phase, by the prompt-4 import that prompt 3 runs once the event is settled; never during research, pregame or mini creation. Prompts 1–3 now run in this repository (ENV-v2), so prompt 1 writes the card into the mini and commits it instead of returning a document. Earlier rule (MINI-2026.10.16-v1 · MDS/P v19.2 · CR-2026.10.16-R7 · RETAIN-v2): canonical P-IDs are assigned during prompt 4 canonical import, never during research/pregame or local settlement. Every prompt-1 game request updates its mini and returns the complete updated Markdown document. This applies to all eleven sport/general workflows. New formats are mini-log-10 / mini-settlement-10; canonical-md-1 and numerical selection/scoring/model rules are unchanged.

## 1. Stable local identity without canonical allocation

A mini has an immutable, unique MINI_KEY using uppercase letters/digits (for example 20261016A1B2C3D4). Check accessible mini/package namespaces before choosing it; use a sufficiently distinct random suffix, not a canonical number. Its first new event is LOCAL-<MINI_KEY>-G0001, then G0002, etc. The concrete key syntax is LOCAL-[A-Z0-9]+-G[0-9]{4,}, with a positive event ordinal. It is a local reference only. Do not predict, reserve, request or print a proposed P-NNN for a new event during research, mini creation or the settlement write-up. Canonical ID is NOT_ASSIGNED; assignment stage is PROMPT_4_IMPORT, which runs at the end of the event's settlement phase. Reading a current highest/next canonical snapshot for context or duplicate checks does not allocate it and cannot block independent local research.

Use the exact local key for card markers/headings, the manifest card_id column, addenda, local settlements, queues and source/requirement tables. event_id remains the verified native event identifier or an explicit stable event surrogate, not a changing canonical allocation. Manifest column names remain unchanged. Model-bundle IDs and native event IDs are not canonical P-IDs. Never rename/rewrite frozen model inputs, feedback, source IDs, hashes or issued cards to match an eventual P-ID.

Search local mini/package event keys, native IDs, participants, dates, reschedules/doubleheaders and canonical bodies/status before adding an event. An existing local event gets an addendum under its existing local key; no second card/ordinal. An already canonical event keeps its existing P-ID reference and gets a local dated addendum linked to that original; do not issue another canonical ID. A reschedule retains identity and records aliases. Genuine identity uncertainty blocks only the affected append, with full independent research retained.

## 2. Mini lifecycle and compatibility

Prompt 2 creates a uniquely named mini and header-only ML_EXECUTION_MANIFEST.csv, with zero cards and next local key G0001. It assigns no canonical ID. Names use the MINI_KEY, never an anticipated P-number. Only the declared writer with a valid lease appends; parallel minis use distinct namespaces. Prompt 1 can initialize this template within its authorized chosen local mini scope when no active mini exists and there is no missing prior original or competing writer; disclose the path/key. It must not invent a missing existing mini or silently append to a frozen source.

After each successfully recorded new card, advance only the local ordinal/card counts and intake/footer. Addenda and duplicate requests consume no new ordinal. Canonical state/next ID stay unchanged by prompts 1–2, mini creation, model runs, rollover and prompt 3 until its prompt-4 import step. A canonical queue conflict is resolved at import, not by guessing a pregame P-ID. A mini's real writer/access/freeze/identity conflict remains a write constraint.

Existing issued P-labelled local cards, canonical records, old formats and old settlements stay byte-preserved; do not renumber them. A still-active older mini receives a dated MINI-v1 lifecycle addendum outside prior cores establishing MINI_KEY/next local key, and new cards use local keys. Do not extend its old working P-ID sequence. Its old P labels are legacy source aliases until import reconciliation, never evidence of a newly committed canonical allocation. verify-log accepts documented local additions in mini-log-8/9, preserves legacy P-card support there, and requires local keys for new mini-log-10 card markers. Earlier formats retain manual original-format checks plus the new identity/delivery checks for new work. Already canonical references/carryovers may contain their true P-IDs.

## 3. Mandatory prompt-1 updated Markdown deliverable

For every upcoming-game request: read the entire actual latest mini; verify writer/lease/freeze and event identity; perform the full applicable research; append the complete card with decision block, A1–A9, evidence and honest completion/model/timing status immediately before the footer; update intake, queues, manifest and local footer; read back the complete resulting file. Preserve all earlier cards and addenda byte-for-byte. A missing model or open factual field never justifies dropping the researched record; information completeness remains separately honest under EXH-v1.

Under ENV-v2 the repository agent writes the card into the mini file itself, reads the complete file back and commits and pushes it after every request, reporting the exact path, local key, commit, readback status and remaining gaps. A chat summary, isolated card, diff or promise of a later update does not satisfy delivery; an unwritten or unpushed file is reported as such with its exact error. For an exact duplicate, state that no new card/ordinal was added. A substantive correction appends an addendum and commits the updated mini. (Legacy ENV-v1 external chats returned the cumulative document in the reply; their outputs are taken in by prompt 4.)

If reading/writing is blocked, state the precise actual failure and return the complete researched separate draft. If the complete current mini was read and its identity/custody are verified, a separately named proposed updated .md copy may be supplied with DRAFT_NOT_APPLIED status and a real readback; never claim the active mini changed. If the current original is inaccessible/incomplete, do not reconstruct its prior contents: return only the complete separate card draft and state updated-mini delivery BLOCKED with its required recovery action. An inaccessible original cannot be satisfied by an invented document. Do all independent research while resolving the obstruction; do not invent a write, file, link or future retry.

## 4. Prompt 3 settles local records, then runs the import

Freeze the exact mini and preserve its local-key markers, manifest and source hashes. Settlement-10 uses the original record key (local key or already-existing canonical reference) in revisions, source/requirement records, queues and LOCAL_ID_MAPPING. For new local cards the mapping row is local key, event/native identity, canonical ID NOT_ASSIGNED, status PENDING_PROMPT_4_IMPORT. No planned canonical sequence is inserted. Existing canonical carryovers retain known mappings; legacy issued P labels remain explicitly source aliases unless independently committed. Result/scoring/review/feedback work does not depend on obtaining a new P-ID. Once the settlement is written and verified, prompt 3 runs the prompt-4 import (section 5) in the same session; that import assigns the IDs.

Retain reviewed label CSV/evidence locally under the local key. The existing ml.research_learning retain exporter requires a canonical P-ID, so defer that exporter until prompt 4 has assigned/verified the mapping; do not invent an early P-ID to run it. Prompt 4 may export from its canonical wrapper (containing the exact local original), its mapped settlement wrapper and the original native-event LABELS.csv after verifying their scope. Pending label export is a named workflow step, not missing sporting evidence or fabricated expert feedback.

## 5. The prompt-4 import, at the end of the settlement phase, is the sole canonical assignment stage

Only settled events (and owner-authorized retention-only imports) are imported; pending events keep NOT_ASSIGNED and move to the next mini. Immediately before import, reconcile current canonical state/status, reserved IDs, all relevant canonical blocks/revisions and source/native aliases. Inventory all mini cards, revisions, carryovers and manifests. For each exact event: reuse its already committed P-ID when present; otherwise assign the next available contiguous canonical ID in deterministic source-card order only as part of the verified import plan. Across multiple minis, declare their source order. Local ordinals/namespaces never dictate canonical numbers. Do not reuse reserved IDs or consume IDs for duplicates, addenda, model rows, empty minis or failed/unapplied plans.

Record LOCAL_ID_MAPPING in the new import report with source mini/key, raw original hash, native event identity/aliases, assigned/existing canonical ID, disposition, destination block and actual import time. Keep prompt-3's pre-import mapping original unchanged; append the final mapping in the import evidence. A legacy P-labelled uncommitted source is reconciled as an alias; if already committed preserve that canonical ID, otherwise map explicitly to the current new ID without rewriting the issued source label. Any genuine competing identity/allocation evidence must be resolved before applying that batch.

Canonical-md-1 wrappers carry the assigned P-ID, actual import metadata and local-key mapping. Include the complete original local core unchanged (starting at Local event key for new cards, Working ID for old cards); retain the original local markers/headings in source captures. Settlement/addendum wrappers likewise carry the canonical reference externally while preserving complete original local blocks. Update actual canonical highest/next only after successful append/readback. Partial-import recovery reuses the recorded applied mapping and exact destination bytes; reruns allocate zero new IDs for imported events. Replan uncommitted rows after concurrent canonical changes, never renumber already imported events or alter source bytes. Canonical import is not a new forecast issue time or source/model certification.

## 6. Checks and return

C2 checks stable local event identity/duplicate handling and no pre-import canonical allocation. C16 checks cumulative-file readback and earlier-core preservation; C22 checks actual updated .md delivery after each prompt-1 request, including duplicate and blocked cases. Settlement S18 checks local keys and NOT_ASSIGNED mapping for unimported new events, known canonical references and source-preserving prompt-4 handoff. S1–S17 retain their earlier evidentiary purpose. Current checklists are C1–C22 / S1–S18; legacy formats retain their original checks and apply new procedural checks only to new work.

This release does not allocate a real event, edit old mini/log/settlement bytes, change highest/next canonical state, run a game forecast or establish predictive gain. Source persistence, confirmed-player research, online prior-game windows and honest missingness remain required.

# Workflow: where prompts run, local keys and delivery

**Consolidated 2026-11-07, CR-2026.11.07-R3.** The execution-environment and mini-identity protocols were joined verbatim on 2026-11-07 (R2) and then rewritten (R3) to remove contradictions and repetition; part and section numbers are unchanged. What changed and why: [consolidation report](research/verification/framework_change_2026-11-07-3/CONTRADICTIONS.md). Verbatim originals: [EXECUTION_ENVIRONMENT_PROTOCOL](archive/consolidation_2026-11-07/merged_sources/EXECUTION_ENVIRONMENT_PROTOCOL.md), [MINI_LOG_IDENTITY_PROTOCOL](archive/consolidation_2026-11-07/merged_sources/MINI_LOG_IDENTITY_PROTOCOL.md). Versions in force: [CURRENT_STATE](CURRENT_STATE.md).

---

# Part A: EXECUTION_ENVIRONMENT_PROTOCOL

*ENV-2026.10.22-v2. Owner instruction, 22 October 2026: every prompt, 1 to 8, is run in this repository by the repository agent (Claude Code on the owner's PC), with internet access for research. It superseded ENV-v1 (17 October 2026), under which prompts 1–3 ran in an external chat ([archived](archive/superseded_2026-10-22-1/EXECUTION_ENVIRONMENT_PROTOCOL.md)).*

## 1. Who runs what

| Prompt | Environment | Authority | Writes | Model work (MLSCOPE-v3) |
|---|---|---|---|---|
| 1 Game card | REPOSITORY_AGENT, internet research | `LOCAL_WORKING_TREE` | Reference receipt and frozen rows; card, picks block, intake row and footer in the active mini; ledger rows; commit and push | Before the card: the reference stage (`pregame reference` or `reference run`); after it: `python -m ml pregame run` |
| 2 Start mini | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | New mini, active-mini pointer; commit and push | None |
| 3 Settle mini | REPOSITORY_AGENT, internet research | `LOCAL_WORKING_TREE` | Frozen-source identity, settlement document, RESULTS.csv and ACTUALS.csv, shadow settlements, then the prompt-4 import; commit and push | `python -m ml cycle settle` for frozen events |
| 4 Import | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | Canonical suffix, mapping, state; run by prompt 3 or alone; commit and push | None |
| 5–8 | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | As each prompt declares; commit and push | 6 evaluates (`pregame status`, `cycle evaluate`, `pregame compare-card`, `ledger score`, `ledger coverage`); 8 releases |

**External research lanes (EXT-v1, owner instruction 2026-11-11).** The owner's research chats are reinstated as **research lanes**, not card makers: each works one lane at a pinned commit, uses the kit for every number, and returns one LANE_RETURN block that prompt 1 checks, merges and prices here ([EXTERNAL_RESEARCH_PROTOCOL](EXTERNAL_RESEARCH_PROTOCOL.md)). The paragraph below records why the earlier route was retired; each of its failures has a rule in EXT-v1. An owner capture of a page no agent may open follows OWNER-CAPTURE-v1 ([SOURCES](SOURCES.md)) and is not re-opened by the agent.

**The external-chat route was retired (REQ-v3, owner instruction 2026-11-08; superseded for research by EXT-v1).** Game cards are made only here. The owner asked whether outside chats improve accuracy and are still needed; the record says neither ([decision](research/verification/framework_change_2026-11-08-1/IMPLEMENTATION.md#2-external-chat-route)): on paired rows their cards tied or lost to the frozen league baseline (P-581–P-582 −0.0007, P-585–P-589 +0.022, P-612–P-622 +0.024 Brier), 0 of 11 recent primary cards had a verifiable pre-start issue time, their research tables could not be captured or hashed for learning, and their references were hand-computed. The paste-ready requests (REQ-v2), GITHUB_REFERENCE_PROTOCOL and GOOGLE_DRIVE_EXCHANGE_PROTOCOL are archived in [archive/retired_2026-11-08/](archive/retired_2026-11-08/). Text the owner brings from elsewhere (a pasted chat answer, an attached file) is copied byte for byte under `research/active_minis/received/` and used only as an owner-supplied research note for a card made here: every fact in it is re-opened and re-timed before use, and it is never issued, frozen or scored as a card. `PUBLISHED_MAIN_PINNED` remains only to read legacy minis made under ENV-v1.

## 2. Reading

Read controls from the working tree and print branch, HEAD SHA, read time with offset and every uncommitted control difference in the reading receipt ([RULES_REFERENCE](RULES_REFERENCE.md#part-a-current_rules) §0). Read what the prompt names, in full where it says so. **Remote fallback (REF-v2).** GitHub `main` (https://github.com/danisgreat/Sports-Research) is the published copy. When a required local file is missing, unreadable, truncated or a cloud placeholder, read it at one printed full commit SHA of `origin/main` before calling it unavailable, record the path, SHA and read time, and compare it with the local HEAD before relying on it; never mix revisions silently or overwrite local work to get access. If both routes fail, record the attempts and block only the dependent step (RULES_REFERENCE A§1). The full former text is archived: [GITHUB_REFERENCE_PROTOCOL](archive/retired_2026-11-08/GITHUB_REFERENCE_PROTOCOL.md).

Research is done on the internet with the agent's own tools, from verifiable sources with accurate data for the exact game: competition and team field owners, official injury and lineup publications, league match centres and box scores, and the permitted structured providers in [SOURCES](SOURCES.md). Open each source; record its URL, the field used, publication and retrieval times, and an independent corroboration for every material fact (HISTORICAL_SOURCE_PROTOCOL, ROSTER_AVAILABILITY_PROTOCOL, [RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol) Part B). A search snippet is not an opened source. Odds, tips, previews and fantasy content are never inputs. Every source passes the AI-access check first (SRC-ALT-v1, [SOURCES](SOURCES.md)): a blocked source is replaced by a permitted alternate, never worked around.

## 3. Prompt 1 and 2 delivery

- **Prompt 2** writes the new mini to `research/active_minis/<MINI_KEY>.md` (mini-log-10, with no execution-manifest companion), points CURRENT_STATE at it, and commits and pushes.
- **Prompt 1** appends the complete card immediately before the active mini's footer, updates intake and footer, reads the whole file back, then runs the pregame freeze and adds its block to the card. It commits and pushes the mini, the receipt and the frozen rows, before the scheduled start whenever possible: the pushed commit is the externally checkable freeze. The reply summarises the picks, the likely winner, the reasons and sources, the freeze disposition and the commit.
- Owner material produced elsewhere (an attached mini, a pasted card) is first copied byte for byte under `research/active_minis/received/`, then used; it is never retyped into a frozen source.
- Never claim a write, commit or push that did not happen; report a failure with its exact error and keep the research.

## 4. Prompt 3 delivery and canonical assignment

Prompt 3 freezes the mini and records its byte count and SHA-256 itself. It writes the settlement document, settles the frozen model rows of shadowed events, then runs prompt 4 on the frozen mini and settlement in the same session. **Canonical IDs are assigned only in this settlement phase** (MINI-v2): settled events receive their IDs; pending events stay in the carryover with canonical ID NOT_ASSIGNED and move to the next mini.

## 5. Reference and model timing (MLSCOPE-v3)

The declared reference is frozen **before** the card's probabilities are written: a tier A release by `python -m ml pregame reference`, a TB-2-MD or baseline reference by `python -m ml reference run`. The pregame command refuses to freeze the card unless the card's BEGIN and END markers are already in the mini, and refuses a `card_p` value not printed in that card. The card's own final p is frozen beside the reference and the league baseline on identical contracts, so the three can be compared prospectively. A reference already frozen is reused, never rerun. Details: [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md), including its forecast-cycle part.

## 6. Limits

- Agent arithmetic can still be wrong; printed inputs and steps, the toolkit §11 checks and readback are the controls.
- A pushed commit time proves when bytes were published, not when a source was published; source times are recorded separately, and an unverifiable time is labelled, never assumed.
- The Google Drive drop box (DRIVE-v2) is retired with the external route (2026-11-08); a file the owner provides from anywhere is owner material under §1, never a control.

---

# Part B: MINI_LOG_IDENTITY_PROTOCOL

*MINI-2026.10.22-v2. Owner instruction, 22 October 2026: canonical P-IDs are assigned only in an event's settlement phase, by the prompt-4 import that prompt 3 runs once the event is settled; never during research, pregame or mini creation. It superseded MINI-v1 (16 October 2026, assignment at any prompt-4 import). Formats: mini-log-10 and mini-settlement-10; canonical-md-1 wrappers, numerical selection, scoring and model rules are unchanged.*

## 1. Stable local identity without canonical allocation

A mini has an immutable, unique MINI_KEY of uppercase letters and digits (for example `20261016A1B2C3D4`), chosen after checking the existing mini and package namespaces, with a distinct random suffix, never a canonical number. Its events are `LOCAL-<MINI_KEY>-G0001`, then G0002 and so on (syntax `LOCAL-[A-Z0-9]+-G[0-9]{4,}`). A local key is a local reference only: never predict, reserve, request or print a proposed P-NNN for a new event during research, mini creation or settlement. Canonical ID: `NOT_ASSIGNED`; assignment stage: `PROMPT_4_IMPORT`. Reading the current highest and next canonical ID for context or duplicate checks allocates nothing.

Use the exact local key in card markers and headings, addenda, local settlements, queues and source and requirement tables (and in the `card_id` column of a legacy mini's execution manifest). `event_id` is the verified native event identifier or an explicit stable surrogate. Model-bundle IDs and native IDs are not canonical IDs. Never rewrite frozen model inputs, feedback, source IDs, hashes or issued cards to match an eventual P-ID.

Before adding an event, search local keys, native IDs, participants, dates, reschedules and doubleheaders, and the canonical records. An existing local event gets an addendum under its key, never a second card. An already canonical event keeps its P-ID and gets a dated local addendum linked to it. A reschedule keeps its identity and records aliases. Genuine identity uncertainty blocks only the affected append; the research is kept.

## 2. Mini lifecycle and compatibility

Prompt 2 creates a uniquely named mini-log-10 file with zero cards and next local key G0001, and **no execution-manifest companion** (template section E is legacy; model rows keep their own receipts under MLSCOPE-v3). It assigns no canonical ID. Only the declared writer with a valid lease appends; parallel minis use distinct namespaces. If no active mini exists and there is no missing prior original or competing writer, prompt 1 may initialise one within its scope and disclose the path and key; it never invents a missing mini or appends to a frozen one.

After each recorded card, advance only the local ordinal, the card counts, the intake table and the footer; addenda and duplicate requests consume no ordinal. Canonical state and the next ID are unchanged by prompts 1–2, mini creation, model runs, rollover and prompt 3 until its prompt-4 step. A canonical queue conflict is resolved at import, never by guessing a P-ID. A real writer, access, freeze or identity conflict remains a write constraint.

Existing issued P-labelled local cards, canonical records, old formats and old settlements stay byte-preserved and are never renumbered. A still-active older mini receives a dated lifecycle addendum outside its earlier cores that sets its MINI_KEY and next local key; new cards in it use local keys, and its old P labels are legacy source aliases until import reconciliation. `python -m ml primary verify-log` accepts documented local additions in mini-log-8/9, keeps legacy P-card support there, and requires local keys in new mini-log-10 card markers.

## 3. Mandatory prompt-1 updated Markdown deliverable

For every upcoming-game request: read the entire latest mini; verify writer, lease, freeze and event identity; do the full research; append the complete card (decision block, picks block, A1–A9, evidence and honest completion, model and timing status) immediately before the footer; update intake, queues and footer; read the whole file back; then commit and push it (ENV-v2). Every earlier card and addendum is preserved byte for byte. A missing model or open factual field never justifies dropping the record; information completeness stays separately honest (EXH-v1).

The delivered document is the committed mini: report the exact path, local key, commit, readback status and remaining gaps. A chat summary, isolated card, diff or promise of a later update is not delivery; an unwritten or unpushed file is reported with its exact error. For an exact duplicate, say that no card or ordinal was added. A substantive correction is an appended addendum, committed with the mini.

If reading or writing is blocked, state the exact failure and deliver the complete researched card as a separate draft. If the complete current mini was read and its identity and custody verified, a separately named proposed copy may be supplied with `DRAFT_NOT_APPLIED` status and a real readback; never claim the active mini changed. If the current original is inaccessible or incomplete, never reconstruct it: deliver only the separate card draft and state that updated-mini delivery is BLOCKED, with the recovery action.

## 4. Prompt 3 settles local records, then runs the import

Freeze the exact mini and preserve its local-key markers and source hashes (and a legacy mini's manifest). Mini-settlement-10 uses the original record key (local key or existing canonical reference) in revisions, source and requirement records, queues and LOCAL_ID_MAPPING; for a new local card the mapping row is the local key, the native identity, canonical ID `NOT_ASSIGNED` and status `PENDING_PROMPT_4_IMPORT`. No planned canonical sequence is inserted; existing canonical carryovers keep their mappings; legacy P labels stay source aliases unless independently committed. Results, scoring, review and feedback never wait for a new P-ID. Once the settlement is written and verified, prompt 3 runs the prompt-4 import (section 5) in the same session.

Reviewed labels and evidence are kept locally under the local key. The `ml.research_learning retain` exporter needs a canonical P-ID, so it runs only after prompt 4 has assigned and verified the mapping ([RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-c-research_retention_protocol) Part C §4); never invent an early P-ID to run it.

## 5. The prompt-4 import, at the end of the settlement phase, is the sole canonical assignment stage

Only settled events (and owner-authorised retention-only imports) are imported; pending events keep NOT_ASSIGNED and move to the next mini. Immediately before import, reconcile the current canonical state and status, reserved IDs, the relevant canonical blocks and revisions, and source and native aliases, and inventory every mini card, revision and carryover (and legacy manifest). For each event, reuse its committed P-ID if it has one; otherwise assign the next contiguous canonical ID in deterministic source-card order, only within the verified import plan; across several minis, declare their source order. Local ordinals never dictate canonical numbers. Reserved IDs are never reused, and no ID is consumed by a duplicate, addendum, model row, empty mini or failed plan.

The import report records LOCAL_ID_MAPPING: source mini and key, raw original hash, native identity and aliases, assigned or existing canonical ID, disposition, destination block and actual import time. Prompt 3's pre-import mapping stays unchanged; the final mapping is appended in the import evidence. A legacy P-labelled source is reconciled as an alias: an already committed canonical ID is kept, otherwise it is mapped explicitly to the new ID without rewriting the issued label. Competing identity or allocation evidence is resolved before that batch is applied.

Canonical-md-1 wrappers carry the assigned P-ID, the import metadata and the local-key mapping around the complete original local core, unchanged (from "Local event key" for new cards, "Working ID" for old ones); settlement and addendum wrappers likewise carry the canonical reference outside the unchanged local block. The highest and next canonical ID are updated only after a successful append and readback. Partial-import recovery reuses the recorded mapping and exact destination bytes, and reruns allocate no new IDs. After a concurrent canonical change, replan uncommitted rows; never renumber imported events or alter source bytes. An import is not a new forecast issue time or a certification.

## 6. Checks and return

C2: stable local identity, duplicate handling, no pre-import allocation. C16: cumulative-file readback and earlier-core preservation. C22: actual updated-mini delivery after each prompt-1 request, including duplicate and blocked cases. Settlement S18: local keys and NOT_ASSIGNED mappings for unimported new events, known canonical references and a source-preserving prompt-4 handoff. S19: the v24 ledger settlement (RESULTS.csv, ACTUALS.csv; [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md)). Current checklists: C1–C22 for cards, S1–S19 for mini-settlement-10 (S1–S17 for settlement-9, S1–S16 for settlement-8); legacy formats keep their original checks and apply the new procedural checks only to new work.

Source persistence, confirmed-player research, online prior-game windows and honest missingness remain required throughout.

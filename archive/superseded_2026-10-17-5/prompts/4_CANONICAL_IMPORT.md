# PROMPT 4 — Verify and import the complete settlement package

**Canonical assignment happens here (MINI-v1).** Accept local-key mini-log-10 research and mini-settlement-10 without any preassigned P-ID. Freeze/verify original source bytes, reconcile every event against canonical/native aliases, assign new canonical IDs only in this verified import, retain the final mapping separately from the frozen pre-import NOT_ASSIGNED mapping, and update actual canonical highest/next after append/readback. Exact reruns and already imported events receive no new ID. Replan unapplied rows on concurrent state changes; preserve applied IDs. Reviewed local label candidates may now be exported using mapped canonical original/settlement wrappers without rewriting source bundles or event IDs.

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, return the new card with its intake row and footer, plus the full mini when it fits, for the owner to save (ENV-v1). Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.17-v22.0 · CANONICAL_IMPORT · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Writes: active log suffix, current status/state/scoreboard, a new import report with preserved inputs, and declared append-only source observations in RESEARCH_SOURCE_REGISTER, plus the append-only LEARN-v1 learning store, training-candidate folders and review log. Never rewrite issued cores, closed parts or grades. Publish when this full prompt is invoked unless the user requests local-only.

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Execution environments (ENV-v1).** Prompts 1–3 run in an external chat with internet access and read-only access to the GitHub repository at the latest `main` commit: no code, no repository writes, no hashes, a section-level reading budget, and every output returned in the reply for the owner to save. Prompts 4–8 run in this repository as the repository agent (`LOCAL_WORKING_TREE`); prompt 4 is the only intake point for external-chat output and computes the byte counts and SHA-256 the chat cannot. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## Inputs

- Settlement package OR owner-authorized retention-only research mini and every source/carryover: exact paths. Settlement/ML execution is not a prerequisite for research retention.
- Canonical destination: resolve dynamically.
- Publication: invoked-task default or explicit local-only.

## 0. External-chat intake (ENV-v1)

Prompts 1–3 run in an external chat that writes nothing, so this prompt is their only intake point. Before importing:
1. **Place.** The owner saves each returned mini, card delta and settlement document under `research/active_minis/` or gives their paths. Download a Drive upload (DRIVE-v2) into a new empty folder outside the repository first.
2. **Assemble.** Insert each CARD_DELTA card before the footer in local-key order and replace the footer, keeping every returned block byte-for-byte. Stop on a missing ordinal, a duplicate key or a footer that disagrees with the cards.
3. **Freeze and hash.** Compute the frozen mini's byte count and SHA-256, complete the settlement's FROZEN_SOURCE (PENDING_PROMPT_4), and build PREDICTION_MINI_SETTLED as the frozen mini followed by the settlement document.
4. **Check.** Run `python -m ml primary verify-log --mini <mini>` for structure; confirm the settlement inventory equals the mini's card list and every settled key exists; save the Markdown source/closure tables as the package's CSV sidecars.
5. **Report.** Return any intake defect to the owner with the exact block and reason; never repair it by guessing. Then continue with the import below.

## 1. Read, reconcile and snapshot

Read common controls/protocol, templates §8, scoring, verification §3, original/settled bytes, mappings/manifests/queues, current state/status and relevant log entries/addenda. Print branch/HEAD/dirty inventory and reading receipt. Fetch the publication ref without overwriting local work; explain divergence.

Resolve active log, highest/next ID, reserved IDs, outstanding local sequence and effective revisions from current records. Opening headers are historical. Search parts/minis by ID, event key and aliases. Genuine identity/allocation disagreement blocks dependent mutation; preserve evidence and independent work.

Snapshot the full destination working bytes/count/hash/end marker and line endings. Distinguish raw source, imported literal core, destination prefix and committed blob. Check local text attributes/core.autocrlf. Line counts or zero deleted lines do not prove byte identity.

## 2. Plan every block

Require the exact complete source original; if a settlement package exists, also require its complete settled-prefix match. In retention-only mode preserve pending/unreviewed outcomes and import contiguous original research cores without inventing a settlement. Inventory every card, carryover, addendum and revision, including already-imported cards with new addenda. Map each unit to NEW_CANONICAL_EVENT, EXACT_EXISTING_SKIP, NEW_ADDENDUM_OR_REVISION, RETAINED_PENDING/UNRESOLVED or CONFLICT. Reconcile these separately for every block type.

Compare full existing blocks, not only IDs. Partial/mismatched blocks stop the batch until scoped recovery. Exact reruns plan zero changes. Preserve every original local key/source label in the source bytes. This prompt is the sole stage that assigns new canonical P-IDs: reuse already committed event mappings, then allocate genuinely new events contiguously from the freshly reconciled canonical next ID in declared source order, respecting reserved ranges. Record local key/native identity/original hash → assigned or existing canonical ID/disposition/destination/import time in the import report. Local ordinals never predetermine P-numbers. Do not consume IDs for duplicates, addenda, unapplied plans or model rows. Addenda and model rows consume no IDs.

Validate known-format balanced BEGIN/END, matching IDs/revision keys, no cross-ID nesting and unique revision keys. Legacy keyless markers stay valid in their declared format. Revision branches require explicit conflict resolution, never last-row-wins.

## 3. Apply append-only import

Before each batch recheck HEAD, active path, destination count/hash/tail, next ID and source inventory against the plan. A change forces a new plan.

Apply and verify the explicit local-to-canonical mapping in canonical-md-1 wrapper metadata; keep original local cores/markers and source settlement blocks byte-for-byte. A legacy uncommitted P-label is a source alias, not authority to reserve that number. Append canonical-md-1 wrappers containing complete original cores byte-for-byte. Import metadata is not a forecast timestamp. Append complete original source addenda/settlements under dated wrappers. A revision for a closed-part original goes into the active part with original/prior-revision pointers; never edit the closed part.

New cards are ANALYST_PRIMARY_V1 (hand-derived, no code). Historical MODEL_ASSISTED_PRIMARY_V3 / MODEL_ASSISTED_CYCLE_V1 cards are imported literally as their own cohort with their original policy/receipt intact. Never insert model probabilities into an original, create primary picks from shadow rows, or count separate shadow/comparator wins in card T2.

## 4. Reconcile and verify completely

Update state/status/scoreboard from effective settlement chains, with pending events and terminal unresolved fields separate. Headline scores use frozen same-row baselines and evidence strata; missing comparisons remain NOT_COMPUTABLE. Import does not confer certification. Preserve actual issue phase and clean-pre-start-input status separately under TIMING_RESEARCH_PROTOCOL; never relabel a legacy late card or pool late-issued research with a pre-start-issued prospective cohort.

Read back EVERY imported core/source block; compare the entire old destination prefix and raw identities, inspect append locations and committed line endings. Reconcile mappings, continuity, counts, revisions, queues and outputs. Source closure requires a destination or explicit retained disposition for every source block. Never delete originals automatically.

Report planned/applied/skipped/conflicting units, custody/readback evidence, pre/post state and limits. Exercise duplicate/rerun/partial-recovery failures and valid cases; label manual checks honestly.

## 5. Publish and return

Stage exact intended paths, inspect the full staged diff/scope, run relevant checks and commit/push without force when authorized. Fetch and compare remote SHA and key artifact contents. Preserve concurrent work.

Return package/destination/report links, all dispositions, canonical continuity, effective settlements/queues, paired-score coverage, byte identities and actual commit/remote status. A failed dependent append never erases completed verified work.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and deliver the card, intake row and footer (full mini when it fits, ENV-v1) after every game request. No model, runtime, receipt or manifest is needed or recorded. Canonical P-ID assignment belongs exclusively to prompt 4 import. Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

For retention-only import, accept researched cards with an honest probability-method disposition; complete source custody, identity and contiguous canonical allocation still apply. Check the mini structure by hand (one format marker, balanced local-key card markers, one Analysis status per card); `python -m ml primary verify-log --mini <mini>` may be used for the same structural check in the repository. No execution receipt, model, baseline or completed settlement is an ID/import prerequisite. Preserve originals and source capture; leave any legacy bundles/feedback in place for prompt 6.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Return the researched card with its intake row and footer (and the full mini when it fits, ENV-v1) after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Legacy grouped packages and current prompt continuity

Assess each issued source under its declared original rules; current online-history/player requirements govern new research and never retroactively certify an old card. Preserve the full frozen prefix and original package bytes. If repository file policy excludes a supplied JSON extension, preserve its exact bytes as a clearly mapped .json.original.txt capture, naming original path/extension/hash; never claim the renamed capture is a new receipt or reconstructed JSON.

A grouped legacy settlement with no per-event marker may be retained verbatim once as a DOCUMENTARY source corpus, with per-event canonical RESEARCH ADDENDUM wrappers referencing the original event/revision/affected keys and preserving complete exact event sections. The documentary corpus is not a second effective settlement. Resolve and count by event/revision/contract key, not repeated appearances in reports. The readback map covers the whole source group, every event section, every new core and source addendum; independently account for intake, footer, control notes and old carryovers. Recover an already-published canonical core by exact bytes when available; leave an unprovided earlier full draft missing.

Source grades are not automatic verification: record independent result/definition checks and unresolved limits without overwriting the supplied package. Keep analyst_p and manually labelled historical p_card in their declared source cohort; no missing model/baseline or outcome exposure is repaired by import. Preserve current owner-entered Upcoming game input blocks when editing prompt 1; instruction alignment begins at its first Read paragraph.

## Persistent sourcing and information closure (EXH-v1)

For new settlement-9 packages inventory and preserve the source-discovery, attempt and requirement-closure registers with the complete visible settlement section. Verify actual field coverage/corroboration/lineage and S17; never convert an open source/definition/time requirement into resolved merely through import. Old packages remain importable under their original formats without invented source sections. Include deduplicated dated candidate observations in the shared RESEARCH_SOURCE_REGISTER only within the declared authorized import scope, preserving original source IDs, package pointers, capability/access limits, hashes and prior observations. No global edits from prompts1-3 are implied.

## Training-data handoff (moved to prompt 6, MLSCOPE-v1)

Import does not ingest into `research/learning_store/`, run ML commands or update learning status. List each imported card's learning record and settlement package, with paths and hashes, in the import report so prompt 6 can ingest them.


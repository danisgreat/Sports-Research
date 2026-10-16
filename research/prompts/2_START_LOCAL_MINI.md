# PROMPT 2 — Start the next local mini

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.16-v19.0 · LOCAL_MINI_STAGING.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Writes: one new Markdown mini and its header-only execution-manifest CSV. Creating a mini consumes no event ID. GitHub is read-only. Workshop forecasts and the decision lab are excluded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## Inputs

- Output location: established local mini folder, or choose a descriptive folder.
- Previous mini, settlement and import receipts: exact paths, or discover.
- Requested events/carryovers: exact requests, or NONE.
- Authority: published main pinned, or explicitly requested local controls.

## 1. Read and reconcile

Read current state/method/rules/selection/templates, the prompt index/common protocol, current status, active log entries/addenda and previous mini/import receipts. Print actual paths/sections, one full authority SHA, versions, time/offset and missing evidence. Locate existing files before asking; inaccessible does not mean nonexistent.

Read current canonical state only for context/duplicate references. Resolve the actual active mini, existing MINI_KEY namespaces, local events and writer leases. Choose a unique MINI_KEY and initial LOCAL-<MINI_KEY>-G0001; do not choose/reserve a P-ID or require a reconciled canonical next number to start research. Canonical allocation conflicts are resolved by prompt 4; actual local identity/custody/write conflicts still block the affected write.

Continue the eligible active mini or record an authorized hand-over; distinct authorized minis use distinct local namespaces. An exact existing requested mini returns ALREADY_EXISTS with zero new allocation. This concludes only duplicate mini creation: if the invocation also requests a game, continue prompt1 in that eligible active mini. Lease/identity/access conflicts block writes only; execute RESEARCH_COMPLETION_PROTOCOL and return a complete no-ID A1–A9 draft. Never treat an existing mini as a reason to abandon requested analysis. A frozen mini routes new events to the next authorized mini.

## 2. Create the complete mini

Use CARD_AND_LOG_TEMPLATES §2 exactly, format mini-log-10. Record authority/read time, active destination, canonical context and outstanding-local snapshots, immutable MINI_KEY and first local event key, writer, lease start/expiry, hand-over and frozen status. Initial counts are zero; last local key NONE; next local key LOCAL-<MINI_KEY>-G0001; canonical assignment NOT_ASSIGNED / PROMPT_4_IMPORT.

Carry pending events and terminal unresolved evidence separately with original IDs/local-canonical status. Each item names original reference, latest revision, open field, actor, exact next source/field, due time/zone, final-time basis or UNKNOWN, last attempt and actual automation. An open-event alert never discards a request or forces settlement.

Retain every request in intake: received time, identity/alias, disposition and existing/new-record pointer. Blocked/duplicate requests stay visible. Do not invent a card, picks, probabilities, source or lineup to populate the mini.

Model-shadow IDs remain separate from P-IDs. Read PRIMARY_PREDICTION_PROTOCOL; prompt1 will run the actual event-specific primary model. Do not seed a mini from unadmitted historical predictions. Each prompt-1 game performs its own availability, cutoff, candidate and frozen-baseline checks.

## 3. Verify and return

Read back the complete mini. Check authority, local namespace/ordinal continuity, writer lease, zero initial counts, queue/intake coverage and footer agreement. Earlier minis, cards and canonical status/logs must remain unchanged. Structural examples use EXAMPLE IDs.

Return exact path, MINI_KEY / first/next local key, format/status, authority SHA, retained carryovers/alerts and actual reading/write/readback evidence. Settlement/canonical import NOT_PERFORMED; GitHub writes NO. If writing failed, return a complete READ_ONLY_DRAFT / NOT_ISSUED artifact without claiming creation.

Historical coverage gaps route each prompt1 game to HISTORICAL_SOURCE_PROTOCOL and verified online recovery; do not prepopulate missing scores or block a mini because local archive rows are absent.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research regardless of ML (RETAIN-v2).** Use the supported primary model when accessible; otherwise retain RESEARCH_ONLY_NO_MODEL, the actual reason, blank nonexistent receipt paths and supported analyst work separately NOT_PRIMARY. Record the full research under a stable local event key and deliver the complete updated mini Markdown after every game request. Canonical P-ID assignment belongs exclusively to prompt 4 import. Settle original contracts and retain verified targets for future development; never invent probabilities, receipts, expert losses or pregame timing. C21 checks honest model disposition; C22 checks updated-document delivery.

Create new minis as mini-log-10 with a header-only `ML_EXECUTION_MANIFEST.csv` companion (template section E). Mini creation consumes no event ID and performs no dummy fit. Every later event must actually execute and append its own attempt/manifest row; missing league profiles never pre-exempt a competition. Verify the empty new mini/manifest with `primary verify-log`.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card regardless of model availability, update intake and the local footer, verify the full mini and return its complete updated .md file after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Current-source setup and prior-format continuity

A new mini follows current online-history and confirmed-player controls. Do not populate L5/L10/L15/L20, league profiles or selected players from the retired store or from another event. Existing minis keep their declared format and issued core bytes; apply current research steps only to new cards. Record genuine missing source/model fields without inventing a completed search or dropping the local research record.

## Persistent sourcing and information closure (EXH-v1)

Initialize references to EXH-v1, the shared source register and relevant prior package registers. Do not prefill source checks, field closures, independence or source-discovery rows. Each new card performs the actual searches and keeps the field/attempt ledger in its named evidence scope; preserve filled prompt-1 event inputs.

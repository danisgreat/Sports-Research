# Settlement revisions import — P-604, P-606, P-620 — 7 November 2026

Authority `LOCAL_WORKING_TREE`; branch `main`; base HEAD `749bca06d2b63f358fce19a1969d6887ecfb8815` (= `origin/main` after `git fetch`, which succeeded). Owner-invoked prompts 3 and 4 (P-2026.10.22-v24.0) in one session: "fully settle all of the logs in the mini logs to be settled folder, and then delete/archive the folder, following the audit/settlement process stipulated". Append applied **2026-11-07T20:53:07+11:00** (clock read). No model, runtime, shadow, ledger or learning-store command was run (prompt 4: import does not ingest or run ML). The helper that hashed, wrapped, appended and read back stayed outside the repository.

**Working-tree note.** This clone was first checked out with the system default `core.autocrlf=true`, which turned LF files into CRLF on disk, so hashes did not match the committed receipts (e.g. the 79B3 frozen mini read 315,319 bytes rather than 313,155). Before any write, the clone was set to `core.autocrlf=false`, `core.eol=lf` and re-checked out from the index (no local changes existed). Every hash below is on the committed LF bytes and matches the earlier receipts.

## What the owner drop held

`MINI LOGS TO BE SETTLED/` (owner drop, commit `2f6139e01`, 22 October) held 14 files: two running minis, one settled R1 package, six prompt-3 settlement documents of 21 October with their README, and four documentary reviews. **All 14 are byte-identical** to copies already retained by the 21 October import ([OWNER_DROP_RECONCILIATION.csv](OWNER_DROP_RECONCILIATION.csv)). So every card in the drop was already settled (prompt 3, 21 October) and canonical (P-601–P-622, Part 8); the two documentary reviews of NOT_ISSUED drafts create no event. What remained was that import's open queue, U-601–U-611, and the retrospective's two unapplied data repairs (F-01 P-606 score, F-02 P-604 corners). This session settled what verified evidence allows and re-queued the rest.

## Prompt 3: settlement revisions written

| Document | Frozen source (bytes · SHA-256) | Keys revised | Change |
|---|---|---|---|
| [2026101679B3FBCC8D_SETTLEMENT_REVISION_3.md](../../active_minis/2026101679B3FBCC8D_SETTLEMENT_REVISION_3.md) | `…/mini_import_P-601_P-622_2026-10-21-1/inputs/2026101679B3FBCC8D/ORIGINAL_MINI.md` 313,155 · `b7478342…ad7e` | P-604 corner keys (revision-3, parent revision-2); P-606 all four keys (revision-2, parent revision-1) | P-604 corners **8–5 = 13**: Over 10.5 **WIN**, Under 10.5 **LOSS**, evidence C (two aggregators, lineage unknown). P-606 score **116–98** replaces 117–98; grades unchanged; evidence B |
| [20261018X7Q4M9R2_SETTLEMENT_REVISION_2.md](../../active_minis/20261018X7Q4M9R2_SETTLEMENT_REVISION_2.md) | `…/inputs/20261018X7Q4M9R2/ORIGINAL_MINI.md` 150,699 · `8bca9a3e…2748` | P-620 innings keys (evidence only) and the winner call (revision-2, parent revision-1) | South Africa won by an innings and 31 runs (425/9 dec; Australia 99 and 295; 425 − 99 − 295 = 31). Winner call (Australia) **incorrect**; contract grades unchanged; innings evidence E → B |

Both frozen sources were re-hashed before writing and equal the 21 October FROZEN_SOURCE receipts. Neither has later blocks. Retained copies: [SOURCE_FILE_INVENTORY.csv](SOURCE_FILE_INVENTORY.csv) (revision-3 package 15,554 bytes `2db26b35…fb12`; X7Q4 revision-2 10,937 bytes `a7cd8af2…c4fe`).

## Prompt 4: reconciliation and append

**Identity.** Highest **P-622**, next **P-623**, reserved P-518–P-522 (CURRENT_STATE, GAME_LOG_STATUS_CURRENT and Part 9's header agree). All three units are revisions of existing canonical events (`NEW_ADDENDUM_OR_REVISION`); **zero new IDs**. Revision keys are unique per original record key: `P-604 2026-11-07-settlement-revision-3`, `P-606 2026-11-07-settlement-revision-2`, `P-620 2026-11-07-settlement-revision-2`. One chain per key; no branch. The held card `LOCAL-20261018MELILL01-G0004` stays held (U-608): its source still lacks the BEGIN marker, and no corrected mini was supplied.

**Destination.** The originals are in closed Part 8, so the revisions go into the **active Part 9** with original and prior-revision pointers; Part 8 is not touched. Pre-append Part 9: **5,070 bytes**, SHA-256 `7796d904fea0833352ceed5eaee67ceeac782aee0800296ad9f76dff93957610` (= committed blob, rechecked immediately before the append). Post-append: **15,961 bytes**, SHA-256 `502ac808dd2bb1ca5082d9e6ba43ea16057310eec3f664caccb32b9d933ce591`. Appended suffix: 10,891 bytes, SHA-256 `8de3317c9066ea18e0d40c4d5757270d3af589089728d5360007915f425706e1`. The old prefix was compared in full after writing.

| Wrapper | Source offsets | Core bytes · SHA-256 | Destination offsets |
|---|---|---|---|
| RESEARCH ADDENDUM P-604 2026-11-07-settlement-revision-3 | 6729–8956 | 2,227 · `cabb5af5c281ab240287b300ad7a9be0ad3bdb30620508525db16b4c60b7be62` | 5945–8172 |
| RESEARCH ADDENDUM P-606 2026-11-07-settlement-revision-2 | 9091–11476 | 2,385 · `a0b2d76fbea6803f43e227be2b6b28440d4f3d2c8a2d3f14786c68ad9ce45024` | 9118–11503 |
| RESEARCH ADDENDUM P-620 2026-11-07-settlement-revision-2 | 4376–7825 | 3,449 · `703f263686f4f03afd4dfd5ef14959a42573beb55038d62337ec28bac1b2765c` | 12442–15891 |

Each wrapper holds the exact bytes between the source `SETTLEMENT` marker lines after one metadata line, as the 21 October wrappers do ([IMPORT_READBACK.csv](IMPORT_READBACK.csv)). Source-unit dispositions: [SOURCE_UNIT_DISPOSITIONS.csv](SOURCE_UNIT_DISPOSITIONS.csv).

## Effective settlements after this import

| Cohort | Events | Rows W / L / PUSH / UNRESOLVED | Primary (ranks 1–2) |
|---|---|---|---|
| RESEARCH_ONLY_NO_MODEL P-601–P-611 | 11 | 52: **26 / 26 / 0 / 0** (was 25 / 25 / 0 / 2) | none (p_card NOT_ESTIMATED) |
| ANALYST_PRIMARY_V1 P-612–P-622 | 11 | 50: 25 / 23 / 2 / 0 (unchanged) | 11 W / 10 L / 1 PUSH (unchanged) |

Evidence mix changes: the P-604 corner rows enter the sensitivity view on C; the P-620 innings rows move from E (sensitivity) to B (headline). The ANALYST_PRIMARY_V1 primary Brier (0.2041, n=21) is unchanged, because no graded row changed. P-620's qualitative winner call (Australia) was wrong; it carries no probability and enters no score. P-606's analyst residual becomes −8.50 (was −7.50).

## Queue after import

[UNRESOLVED_POST_IMPORT.md](UNRESOLVED_POST_IMPORT.md) supersedes the 21 October queue row by row: U-602 and U-604 are closed; U-605, U-606, U-607 and U-611 have new attempts logged; U-601, U-603, U-608, U-609 and U-610 are unchanged owner items. **Nothing grade-changing remains open except U-603** (P-616: whether the frozen ±2.0 and 221.5 lines include overtime). The card froze an OT-inclusive analyst definition "conditional on operator confirming", and RULES_BASKETBALL BK-P4 requires the operator's endpoint, so it stays the owner's decision. Information completion stays **INFORMATION_INCOMPLETE** (aggregator lineage, field-owner pages, final times, operator terms).

## Research-source register and learning handoff

[RESEARCH_SOURCE_REGISTER](../../../RESEARCH_SOURCE_REGISTER.md) gains one dated, append-only section for the routes observed here ([SOURCE_DISCOVERY_REGISTER.csv](SOURCE_DISCOVERY_REGISTER.csv)). For prompt 6, nothing was ingested here. The learning records are the "Learning record additions (LEARN-v2)" tables in the two revision documents, joined by the existing mapping (G0004 → P-604, G0006 → P-606, X7Q4 G0001 → P-620). The existing training candidates `research/training_candidates/P-604/2026-10-21-settlement-revision-1` and `P-606/…revision-1` are superseded by these revisions for the corner and score labels, and P-620 had none because it was pending. Their retention is prompt 6's work. The MINI_SETTLEMENT review rows are in each revision document, for prompt 6 to append to `research/learning_status/REVIEW_LOG.csv`. No PICKS_V2 block or adjustment-ledger row exists for these pre-v24 cards.

## Owner drop folder

Archived unchanged to [archive/owner_drop_settled_2026-11-07-1/](../../../archive/owner_drop_settled_2026-11-07-1/README.md) with `git mv`, so its history is kept. It is not deleted, because it is the owner's original drop; every byte of it is also retained in the 21 October inputs.

Verification: [VERIFICATION.md](VERIFICATION.md).

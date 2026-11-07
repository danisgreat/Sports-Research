# Settlement revision import — P-616 under BK-OT-1 — 7 November 2026

Authority `LOCAL_WORKING_TREE`; branch `main`; base HEAD `ef9eb9c7448837fa0e6b2185f8a5b45050d4f457` (= `origin/main`), with the BK-OT-1 rule edits in the same working tree and commit. Owner-invoked prompts 3 and 4 (P-2026.10.22-v24.0) under control **CR-2026.11.07-R1**. Append applied **2026-11-07T21:15:50+11:00** (clock read). No model, ledger or learning-store command was run.

## Owner decision and rule

Owner, 7 November 2026: "all basketball games have overtime inclusive lines, so do it accordingly, if this hasnt been included in the rules, then include it now". It was **not** in the rules. RULES_BASKETBALL BK-P4 required the operator's endpoint and labelled anything else `UNKNOWN_DEFINITION`, which held P-616 as grade-changing (U-603). It is now **BK-OT-1**: every basketball total, spread, team total and winner line includes overtime, in every competition, unless the contract's own text names regulation or a segment. The endpoint is `FROZEN_FRAMEWORK_CONVENTION`. Written into RULES_BASKETBALL (§0.1 BK-P4, §0.5, §6, §8.1, controls 6 and 13), CORE, CURRENT_RULES, README, the basketball prompt-1 sport file and the basketball external request: [implementation](../framework_change_2026-11-07-1/IMPLEMENTATION.md).

## Applied to every basketball game in the queues

| Scope | Effect |
|---|---|
| **P-616** TNT v Converge (114–112 OT; regulation 106–106) | Revision-2: definition `UNKNOWN_DEFINITION` → `FROZEN_FRAMEWORK_CONVENTION`. Grades unchanged, because revision-1 had already graded on the full game including OT (the card's own A2): Under 221.5 **LOSS**, TNT +2.0 **PUSH**, Converge −2.0 **PUSH**, Over 221.5 **WIN**. U-603 closed. The four rows join the headline view (B evidence + frozen convention). |
| Other basketball events P-601–P-622 (P-606, P-608, P-610, P-611, P-612, P-614, P-615, P-621) | Their existing grades were set on the final score, which is the BK-OT-1 endpoint, so they stand and no revision is needed. The settlement records show regulation finishes (four quarters, no OT) for P-606, P-610, P-611, P-612, P-614, P-615 and P-621. P-608 (128–118) records the final only, not whether it ended in regulation; its grades stand either way under BK-OT-1. |
| Earlier queues (P-584 legacy pending, P-590–P-600 carryover) | No open basketball overtime-definition item. The open definition items there (P-596, P-598) and the historical P-166 and P-200 are ice hockey, outside BK-OT-1. |
| Active local mini `20261022F6K3OJNO` | Its basketball cards already declare "full game including all overtime"; unchanged. |

## Append and custody

The revision document was retained byte-for-byte at [inputs/20261018Q7N4T9B2/](inputs/20261018Q7N4T9B2/20261018Q7N4T9B2_SETTLEMENT_REVISION_2.md) (9,936 bytes, `73c6a2f22fbfe14166e3086565df24479e8aa2aee87fc02014762a29f873c03e`). The frozen source `…/mini_import_P-601_P-622_2026-10-21-1/inputs/20261018Q7N4T9B2/ORIGINAL_MINI.md` (172,799 bytes, `89146dbb…c85d`) was re-hashed and equals its import receipt. Identity: highest P-622, next P-623, reserved P-518–P-522; zero IDs consumed.

Part 9 pre-append: 15,961 bytes, `502ac808dd2bb1ca5082d9e6ba43ea16057310eec3f664caccb32b9d933ce591` (= committed blob at `ef9eb9c74`, rechecked immediately before). Post-append: **20,056 bytes**, `a86ca1a975fe0cfea90fe39600a526c67a2aed28f0b5afcc20f0018581413f6c`. Suffix 4,095 bytes, `806767c57ff0ecd0a8fab156af382f0d82b29dcfca6884e4bd703ecee482cafa`. The wrapper `RESEARCH ADDENDUM P-616 2026-11-07-settlement-revision-2` holds source bytes 4385–7486 (3,101 bytes, `701053e2bec2f9b9a2933ac142715596da69a9e89569dd2603f59881e912df3e`) at destination 16885–19986. It points to Part 8 `RESEARCH ADDENDUM P-616 2026-10-21-settlement-revision-1`; Part 8 is untouched ([IMPORT_READBACK.csv](IMPORT_READBACK.csv)).

## Effective counts

Unchanged: ANALYST_PRIMARY_V1 P-612–P-622 rows 25W/23L/2 push, primary 11W/10L/1 push, Brier 0.2041 (n=21); research-only P-601–P-611 26W/26L/0U. What changes is the strata: P-616's four rows move from "definition unknown" into the headline view.

## Queue

[UNRESOLVED_POST_IMPORT.md](UNRESOLVED_POST_IMPORT.md) supersedes U-601 (now non-basketball and non-overtime operator terms only) and U-603 (closed). The other rows of the [first 2026-11-07 queue](../settlement_import_2026-11-07-1/UNRESOLVED_POST_IMPORT.md) are unchanged. **No grade-changing item remains open in P-601–P-622.**

For prompt 6: the learning record is the "Learning record additions (LEARN-v2)" table in the retained revision document, mapped G0002 → P-616. Its MINI_SETTLEMENT review row is in the same document.

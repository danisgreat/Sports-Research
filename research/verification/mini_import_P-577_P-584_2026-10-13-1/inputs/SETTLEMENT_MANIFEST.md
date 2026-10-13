# SETTLEMENT_MANIFEST — P-577–P-584

**MODE:** LOCAL_MINI_SETTLEMENT · GitHub read-only · no new forecast, new ID, rule edit, canonical import or remote writes.
**PINNED AUTHORITY:** PUBLISHED_MAIN_PINNED `adb8560a597e5ff1a5ad21bfc76b3148bd58c719`, MDS-2026.10.12-v11.0 / CR-2026.10.12-R2 / SCV-2026.10.12-v7 / SEL-2026.10.12-v3. Read from commit via connector. Original issued cards retain their own versions.

## FROZEN_SOURCE receipt (R16)
- Source: `/mnt/data/CHAT_ACTIVE_MINI_P580_ONWARD_2026-10-12.md`
- Raw byte length: **172050**; SHA-256 **`364dc74e30520df5711743ecbc9efd5122a9024627f1bba4f4bb7cb9c49adba0`**.
- Freeze checkpoint: **2026-10-13T15:08:06+11:00** AEDT, in this session. Copy materialised byte-identically in `ORIGINAL_MINI.md`.
- Writer lease hand-over: **NONE**; no local writer lock or future mini was changed. This source is declared frozen **for this settlement snapshot**; separate agents with external copies cannot be technically blocked. The source file continues to contain its original ACTIVE footer, preserved by the no-source-write instruction. Subsequent events should start a new authorised mini.
- Card inventory: existing references P-577, P-578, P-579; five complete issued-card blocks P-580..584.
- Addenda in original source: P-582 `20261012T022342+1100`; P-583 `20261012T202924+1100-TIMING`, `20261012T203748+1100-LATE-NUMERIC-DIAGNOSTIC`; P-584 `2026-10-13-PHASE-01`.
- Original footer: `Highest P-584 / next P-585; 5 new cards (4 numeric, 0 qualitative, 1 NO_FORECAST); 8 pending at original snapshot; GitHub writes NO`. Frozen as historical snapshot; settlement summary is a new suffix, **not an edit to footer**.

## Verification receipts
- Source copied with byte equality `original == source` — CHECKED. Settled file constructed as `original bytes + newline separator + settlement suffix`; complete exact-prefix `settled[:len(original)] == original` — CHECKED.
- Source growth is rechecked **at the last packaging step**, reported below.
- Full earlier *local original* P-577–P-579 card blocks sourced from Library master and bundled as `CARRIED_ORIGINAL_CARD_REFERENCES_P577_P579.md`; direct GitHub Combined Log 7 body fetch returned empty, so **independent canonical core byte equality NOT_VERIFIED**.
- Source publication/collector lineage and true full-time timestamp not independently provable in all cases. Calendar dates do not establish final wall-clock times.

## Inventory and settlement result
| Item | Quantity |
|---|---:|
| Event IDs | 8 |
| Already canonical carryovers | 3 |
| Local-unimported original cards | 5 |
| Dated original addenda retained in prefix | 4 |
| Terminal event records | 7 |
| Pending events | 1 (P-584) |
| Original numeric primary cards | 6 |
| NO_FORECAST cards | 1 (P-583) |
| Diagnostic-only numeric cards without issued primary | 1 (P-584) |
| Rank-1 primary WIN / LOSS | 4 / 2 |
| Rank-2 primary WIN / LOSS | 6 / 0 |
| Top-two WIN / LOSS | 10 / 2 |
| Top-two PUSH / VOID / UNRESOLVED | 0 / 0 / 0 |
| Eight-part Rank-1 LOSS reviews | 2 (P-577, P-581) |

## Proper scores (original numerics only; not predictive-skill proof)
- All 12 original primary rows: Brier **0.136674**, log loss **0.442658**. Cluster dependence, six different events, historical uncalibrated models, and late timing apply.
- Frozen paired same-line `BASELINE_P` available on **4/12** original primary rows (P-581 and P-582 only); paired subset card Brier **0.187418** vs baseline Brier **0.188131**. This is a four-row descriptive comparison, not validated skill.
- All twelve numeric primary rows have A/B-grade sporting final outcomes in the named settlement sources. Operator-definition verification remains separate. No C/E primary rows are added for sensitivity; first-half/corners diagnostic rows are excluded.
- The original core of P-584 contains four ranked **diagnostics** and an after-issue 1H price; none enters the original primary cohort. No reforecast is rescored prospectively.

## Files
- `ORIGINAL_MINI.md` — raw frozen original bytes, exact original footer.
- `CARRIED_ORIGINAL_CARD_REFERENCES_P577_P579.md` — exact earlier *local original* cores; canonical byte equality outstanding.
- `PREDICTION_MINI_SETTLED.md` — original prefix followed by eight distinct `revision-1` settlement blocks, R1–R12 and the two deep reviews.
- `LOCAL_ID_MAPPING.md` — per-ID old/new/pointer mapping.
- `UNRESOLVED_CARRYOVER.md` — one pending event and separate evidence/definition queues with next-source fields and proposed manual times.
- `PRIMARY_PROPER_SCORES.csv` — reproducible 12-row original primary score calculations.
- `SETTLEMENT_MANIFEST.md` — this manifest, snapshot and independent audit.
- `SETTLEMENT_REPORT.md` — human-readable results, evidence, limitations and handoff.
- `READBACK_VERIFICATION.md` — exact container-backed readback counts and raw file identity.

## Self-audit S1–S15
| ID | Result | Specific test/evidence / limitation |
|---|---|---|
| S1 | PASS | 8 unique P-IDs; 5 actual card blocks; 3 canonical carryover references; 4 original addenda; 8 settlement blocks. |
| S2 | PASS | Raw byte count/hash captured, source exact copy and settled prefix compared; original footer and original CRLF/LF raw bytes preserved. |
| S3 | PARTIAL | Complete original cards for P-580..584 and earlier local P-577..579 preserved; exact canonical imported core not directly retrievable for equality. |
| S4 | PASS sporting / PARTIAL operator | Exact line, score, game total, set arithmetic; missing operator definitions not resolved. |
| S5 | PARTIAL | Official A results for five primary numeric events, B tennis; source timestamps and some secondary/definition fields unknown; evidence conflict KT recorded. |
| S6 | PASS | 12 original primary rows, 10W/2L; no double-counting any complementary or info ranks. |
| S7 | PASS | R1–R12 written on all 7 terminal events; pending P584 R sections show N/A/limits. |
| S8 | PASS | Two original R1 losses receive distinct eight-part review; win process check disclosed. |
| S9 | PASS | Provisional corners, late phasing, shadow/reforecast and baseline entirely separate from primary scores. |
| S10 | PARTIAL | One live/pending event, evidence/definition queues preserved; final wall-clock times unverified so 72-hour adherence unknown. |
| S11 | PASS/NOT_COMPUTABLE | Brier/log loss and original-total residual/z computed for terminal numeric cards; paired baseline missing except four primary rows; no backfill. |
| S12 | PASS local / NOT_VERIFIED external | Output and exact prefix readback will be checked below; only new local files modified, no GitHub writes. |
| S13 | PASS | Eight unique `revision-1`, parent NONE, one per ID; no competing revision detected in accessible original mini. |
| S14 | PASS local | Source freeze checkpoint and block inventory, growth recheck; no mutation of source allowed. |
| S15 | PARTIAL | Pending and secondary queues specify actor/route/field/time/automation status; actual final timestamps unavailable, due times proposed manual not scheduled. |

**Settlement revision authority:** local-only. For P-577–P-579, existing canonical original card stays immutable; authorised future import must append settlement revisions to active Combined Log per current cross-part rules, not duplicate canonical cards.

## Final source growth check — 2026-10-13T15:15:00+11:00
- Source bytes now 172050, SHA-256 `364dc74e30520df5711743ecbc9efd5122a9024627f1bba4f4bb7cb9c49adba0`.
- **NO_GROWTH; source snapshot unchanged.**


<!-- BEGIN RESEARCH ADDENDUM P-612 2026-10-21-settlement-revision-1 -->
### Settlement — P-612 (local `LOCAL-20261018MELILL01-G0001`), source revision-1
Original: Part 8 canonical research P-612; prior revision: NONE. Source `inputs/20261018MELILL01/20261018MELILL01_SETTLEMENT.md` offsets 7347–9925; content SHA-256 `eef7e8865c3ef4ef616d10fbb4dc3bd53d257f5a6872391d1355322c18a5e725` (2,578 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018MELILL01-G0001 · Melbourne United v Illawarra Hawks · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` (draft research record).
**Final event:** Melbourne United **89** – Illawarra Hawks **91**, regulation (27-16-22-24 v 21-35-22-13). Total 180; Melbourne margin −2. Final time `UNKNOWN`.
**Definition status:** full game incl. OT (card); no OT. Operator `UNKNOWN_DEFINITION`. **Evidence:** B (ESPN + NBL recap).
**Expected vs final:** total 189.945 (σ 21) → 180: −9.95, z −0.47. Melbourne margin +4.85 (σ 17) → −2: −6.85, z −0.40.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---:|---|---|---|---|
| 1 | **Combined points Under 201.5** | 0.709 | 0.845 (STALE_COMPARATOR) | **WIN** | B | Research-record primary | 180 |
| 2 | **Illawarra Hawks +10.5** | 0.630 | 0.722 | **WIN** | B | Research-record primary | Hawks won |
| 3 | Melbourne United −10.5 | 0.370 | 0.278 | **LOSS** | B | No | |
| 4 | Combined points Over 201.5 | 0.291 | 0.155 | **LOSS** | B | No | |

**Top-two result:** `ALL_WON`; 2/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores (card / baseline / d_Brier; negative favours card):** R1 0.0847 / 0.0240 / **+0.0607**; R2 0.1369 / 0.0773 / **+0.0596**; R3 0.1369 / 0.0773 / +0.0596; R4 0.0847 / 0.0240 / +0.0607. The stale 2025-26 NBL league-only comparator out-scored the card on every row of this event (descriptive, n = 1 event).
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE` (shrinkage only, no separate form overlay).
**Winner call:** Melbourne ≈0.612 → **incorrect**.
**R1.** Rank 1 Under 201.5 (0.709); Rank 2 Hawks +10.5 (0.630). **R2.** 89–91 verified. **R3.** 180 ≤ 201; Hawks +2 margin vs threshold −10. **R4.** 2/2; Hit@2 hit; NDCG 1.0. **R5.** Wrong. **R6.** Total 21.5 under; Hawks covered by 12.5. **R7.** Both errors within 0.5σ. **R8.** Hawks won Q2 35–16 (Maker 23 off the bench, ML-S02); wins checked for the same defect as losses: starters were unconfirmed at issue. **R9.** Card completed after the scheduled 17:00 tip; `POST_SCHEDULED_START_DRAFT`; no outcome used. **R10.** Process `DEFICIENT` (post-start, starters unconfirmed); class for winner miss `CENTRE_MISS_SMALL_N`. **R11.** `PROPOSED_NOT_TESTED`: none from one aligned result. **R12.** `NO_CHANGE`; note baseline out-performed card on this event.
<!-- END RESEARCH ADDENDUM P-612 2026-10-21-settlement-revision-1 -->

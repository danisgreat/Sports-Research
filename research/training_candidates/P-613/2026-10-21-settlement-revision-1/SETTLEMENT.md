<!-- BEGIN RESEARCH ADDENDUM P-613 2026-10-21-settlement-revision-1 -->
### Settlement — P-613 (local `LOCAL-20261018MELILL01-G0002`), source revision-1
Original: Part 8 canonical research P-613; prior revision: NONE. Source `inputs/20261018MELILL01/20261018MELILL01_SETTLEMENT.md` offsets 10056–12600; content SHA-256 `954073d7d4bb645ce1252a7f2836b338bd44da7328f81fc508f01a4ff62636ab` (2,544 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018MELILL01-G0002 · Pakistan v Sri Lanka, ODI Tri-Series Match 1 · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED`.
**Final event:** Sri Lanka won the toss and fielded (card's secondary-source toss confirmed: Pakistan is innings 1 in the feed). Pakistan **305 all out in 49.5 overs**; after 5.0 overs **31/1**. Sri Lanka 268 all out (48.1). Pakistan won by 37 runs. First ball 19:02:47 AEDT; PAK innings ended 2026-10-18T12:07:32Z.
**Definition status:** card A2 — first innings until 50 overs or all out; 30 legal balls. Both endpoints reached; no DLS/reduction. Operator `UNKNOWN_DEFINITION`.
**Evidence:** B (ball-by-ball feed + four independent reports; 5-over field single lineage).
**Expected vs final:** innings 277.75 (σ 52 base) → 305: +27.25, z +0.52. 5-over 29.5 (σ 11) → 31: +1.5, z +0.14.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Pakistan 1st innings Under 311.5** | 0.732 | BASELINE_UNAVAILABLE | **WIN** | B | Research-record primary | 305 |
| 2 | **Pakistan after 5 overs Over 26.5** | 0.606 | BASELINE_UNAVAILABLE | **WIN** | B | Research-record primary | 31 |
| 3 | Pakistan after 5 overs Under 26.5 | 0.394 | BASELINE_UNAVAILABLE | **LOSS** | B | No | |
| 4 | Pakistan 1st innings Over 311.5 | 0.268 | BASELINE_UNAVAILABLE | **LOSS** | B | No | |

**Top-two result:** `ALL_WON`; 2/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (1−0.732)² = 0.0718; R2 (1−0.606)² = 0.1552; R3 0.1552; R4 0.0718.
**Winner call:** Pakistan ≈0.60 (qualitative) → **correct**.
**R1.** Rank 1 Under 311.5 (0.732); Rank 2 5-over Over 26.5 (0.606). **R2.** 305 (49.5 ov); 31/1 at 5.0. **R3.** 305 ≤ 311; 31 ≥ 27. **R4.** 2/2; Hit@2 hit; NDCG 1.0. **R5.** Correct. **R6.** Innings 6.5 runs under 311.5 (−0.13σ); 5-over 4.5 runs over 26.5. **R7.** Innings above the 277.75 centre but below the line; the card's HIGH scenario (300) was closest. **R8.** Agha 107 lifted the total; being all out with one ball left capped it. Wins checked: XIs were unverified at issue (same gap as elsewhere). **R9.** First ball 19:02:47 AEDT; card's research check after 19:06 → `POST_START_ISSUE`. **R10.** Process `DEFICIENT` (post-start; XIs unconfirmed); outcomes inside the issued distribution. **R11/R12.** `NO_CHANGE`.
<!-- END RESEARCH ADDENDUM P-613 2026-10-21-settlement-revision-1 -->

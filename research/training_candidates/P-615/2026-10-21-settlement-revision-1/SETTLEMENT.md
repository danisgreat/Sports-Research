<!-- BEGIN RESEARCH ADDENDUM P-615 2026-10-21-settlement-revision-1 -->
### Settlement — P-615 (local `LOCAL-20261018Q7N4T9B2-G0001`), source revision-1
Original: Part 8 canonical research P-615; prior revision: NONE. Source `inputs/20261018Q7N4T9B2/20261018Q7N4T9B2_SETTLEMENT.md` offsets 7723–10912; content SHA-256 `d433796560f968926ff7209aa0fefcaff11f76023d1a574ddb05bf8d70317b3c` (3,189 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018Q7N4T9B2-G0001 · Fighting Eagles Nagoya v Tryhoop Okayama · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` (research draft record).
**Final event:** FE Nagoya **82** – Tryhoop Okayama **89**, regulation (30-23-17-12 v 21-32-18-18). Total 171; Nagoya margin −7. Tip 2026-10-18T06:40:16Z = **17:40:16 AEDT**; last PBP 08:49:16Z.
**Definition status:** full game incl. OT (card A2); no OT. Operator `UNKNOWN_DEFINITION`. **Evidence:** A (owner record) + independent broadcaster.
**Expected vs final:** total 159.5 (σ 20) → 171: +11.5, z +0.58. Nagoya margin +2.0 (σ 20) → −7: −9.0, z −0.45.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Fighting Eagles Nagoya +1.5** | 0.568 | NOT_ESTIMATED | **LOSS** | A | Yes | lost by 7 |
| 2 | **Combined Under 161.5** | 0.538 | NOT_ESTIMATED | **LOSS** | A | Yes | 171 |
| 3 | Combined Over 161.5 | 0.462 | NOT_ESTIMATED | **WIN** | A | No | |
| 4 | Tryhoop Okayama −1.5 | 0.432 | NOT_ESTIMATED | **WIN** | A | No | won by 7 |

**Top-two result:** `ALL_LOST`; denominator 2; 0/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 0.568² = 0.3226; R2 0.538² = 0.2894; R3 0.2894; R4 0.3226. Baseline pairs 0.
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE` (no form adjustment; card centre was a raw season blend).
**Winner call:** Nagoya ≈0.539 → **incorrect**.
**R1.** Rank 1 Nagoya +1.5 (0.568); Rank 2 Under 161.5 (0.538). **R2.** 82–89 verified on owner record. **R3.** Nagoya −7 < −1.5; 171 ≥ 162. **R4.** 0/2; Hit@2 miss; NDCG 0. **R5.** Wrong. **R6.** Margin 5.5 points beyond the +1.5 threshold; total 9.5 points over 161.5. **R7.** Both errors within ~0.6σ of the stated widths. **R8.** Okayama won the second quarter 32–23 (owner record). Lineup: the card's last-confirmed FE five had Harima; the actual FE five had Sugimoto instead (Q7-S01) — a confirmed-lineup gap at issue, cause share not measurable. **R9.** Tip 17:40:16 AEDT; the card's artifact was assembled after 17:41:02 AEDT → `POST_START_ISSUE` confirmed by the owner PBP timestamp. **R10.** Process `DEFICIENT` (post-start, starters unconfirmed); model uncalibrated; class `NEAR_COINFLIP / CENTRE_MISS_SMALL_N (n=8)`. **R11.** `PROPOSED_NOT_TESTED`: B.ONE same-venue back-to-back rematches — weight the previous day's result? Not testable on one event. **R12.** `MONITOR`.

**Rank-1 LOSS — eight-part review:** (1) Nagoya loses by ≤1 or wins, p 0.568. (2) Lost by 7. (3) Centre +2.0, σ 20 → −7 is −0.45σ; ordinary. (4) The 17-Oct 76–90 loss and injuries were known; the Sunday starting five was not (the club announces at 15:30 JST) and was not backfilled. (5) Gate failed at issue (0.568 < 0.62); variance-dominated. (6) Cutoff-only: no defensible flip; honest output was no primary lean. (7) `NEAR_COINFLIP_RANKED / VARIANCE`. (8) Treat gate-failing rows as informational (`PROPOSED_NOT_TESTED`).
<!-- END RESEARCH ADDENDUM P-615 2026-10-21-settlement-revision-1 -->

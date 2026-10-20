<!-- BEGIN RESEARCH ADDENDUM P-622 2026-10-21-settlement-revision-1 -->
### Settlement — P-622 (local `LOCAL-20261018X7Q4M9R2-G0003`), source revision-1
Original: Part 8 canonical research P-622; prior revision: NONE. Source `inputs/20261018X7Q4M9R2/20261018X7Q4M9R2_SETTLEMENT.md` offsets 23079–26831; content SHA-256 `fdbc6d086a60b4f0ca479445c8212e5f85c09f4d748ac251cef466e7528b5e20` (3,752 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018X7Q4M9R2-G0003 · India Women v Zimbabwe Women, 2nd T20I · 2026-10-21T00:40+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:40+11:00 · affected contract keys ALL (`ZIMW-TOTAL-U-1105`, `ZIMW-TOTAL-O-1105`, `ZIMW-PP-U-335`, `ZIMW-PP-O-335`) · changes NONE.
**Card state:** `SETTLED`.
**Final event:** Zimbabwe Women chose to bat first: **102/8 in 20.0 overs** (innings ended 2026-10-18T15:10:06Z). After 6.0 overs: **20/1** (after 5.0: 16/1). India Women 104/1 in 8.5 overs; India won by 9 wickets. First ball 2026-10-18T13:30:39Z = 00:30:39 AEDT 19 Oct.
**Definition status:** card's full-innings / 6.0-completed-overs convention; both endpoints reached (20 overs batted, 6 overs completed, no rain). The card's open questions (chase-truncation, early all-out) did not arise because Zimbabwe batted first and batted out the 20 overs. Operator `UNKNOWN_DEFINITION`.
**Evidence grade:** total B (two lineages); 6-over A/B single lineage ball-level (X7-S10).
**Expected vs final:** innings 107.0 (mixture SD 29.94) → 102: error −5.0, z −0.17. 6-over 34.75 (SD 13.96) → 20: error −14.75, z −1.06.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | Zimbabwe innings **Under 110.5** | 0.560 | `BASELINE_UNAVAILABLE` | **WIN** | B | Yes | 102 ≤ 110 |
| 2 | Zimbabwe after 6 overs **Over 33.5** | 0.527 | `BASELINE_UNAVAILABLE` | **LOSS** | B | Yes | 20 ≤ 33 |
| 3 | Zimbabwe after 6 overs **Under 33.5** | 0.473 | `BASELINE_UNAVAILABLE` | **WIN** | B | No | complement |
| 4 | Zimbabwe innings **Over 110.5** | 0.440 | `BASELINE_UNAVAILABLE` | **LOSS** | B | No | complement |

**Top-two result:** `SPLIT` — R1 W, R2 L; primary 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (0.560−1)² = 0.1936; R2 (0.527)² = 0.2777; R3 0.2777; R4 0.1936. Baseline pairs 0/4.
**Shadow results:** none.
**Form-window check:** unadjusted powerplay anchor (selected five checkpoints, mean 36.2) gave Over 33.5 ≈0.577; the adjusted mixture gave 0.527; observed 20. The India-strength adjustment moved toward the outcome but the checkpoint centre was ~15 runs high either way.
**Winner call:** India Women (qualitative) → **correct**.

**R1. Original prediction:** Rank 1 Under 110.5 at 0.560; Rank 2 Over 33.5 at 0.527.
**R2. Final event:** 102/8 (20 ov), 20/1 at 6.0; verified.
**R3. Contract settlement:** 110.5 − 102 = 8.5 runs under; 33.5 − 20 = 13.5 runs under.
**R4. Rank diagnostics:** 1/2 primary; Hit@2 hit; NDCG@2 (descriptive): winners at ranks 1 and 3 → DCG = 1; IDCG (two winners) = 1.631 → 0.613.
**R5. Winner call:** correct.
**R6. Line assessment:** innings −8.5 runs (−0.28σ); powerplay −13.5 runs (−0.97σ).
**R7. Expected versus realised:** powerplay centre 34.75 vs 20 is the material miss; innings close to centre.
**R8. Missed mechanism:** the card's 6-over centre was anchored on five selected checkpoints (27–41) against weaker or different attacks; India's new-ball attack held Zimbabwe to 20/1. Supported observation; sample was explicitly n=5 and selected.
**R9. Source/timing review:** request 00:26 AEDT, first ball 00:30:39 AEDT, card completed after → `POST_START_ISSUE`. Second-match XIs and toss were unverified at issue.
**R10. Classification:** process `DEFICIENT` (phase-history n=5 selected, acknowledged in card); model uncalibrated; R2 class `PHASE_CENTRE_HIGH / SELECTED_SAMPLE`.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — opponent-adjusted powerplay rates (Zimbabwe vs full-member new-ball attacks only) would centre lower.
**R12. Disposition:** `MONITOR`; no Rank-1 loss.
<!-- END RESEARCH ADDENDUM P-622 2026-10-21-settlement-revision-1 -->

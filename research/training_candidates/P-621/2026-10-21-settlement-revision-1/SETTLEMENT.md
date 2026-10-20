<!-- BEGIN RESEARCH ADDENDUM P-621 2026-10-21-settlement-revision-1 -->
### Settlement — P-621 (local `LOCAL-20261018X7Q4M9R2-G0002`), source revision-1
Original: Part 8 canonical research P-621; prior revision: NONE. Source `inputs/20261018X7Q4M9R2/20261018X7Q4M9R2_SETTLEMENT.md` offsets 18143–22948; content SHA-256 `d6a369b7e2cd334620620c68ac400ce34e7c2f5bb7eafa058b01e0172600393f` (4,805 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018X7Q4M9R2-G0002 · Napoli Basketball v Olimpia Milano · 2026-10-21T00:40+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:40+11:00 · affected contract keys ALL (`LBA:20261018:NAP:MARGIN:-1.5:FINAL`, `…MIL:MARGIN:+1.5…`, `…COMBINED:OVER:174.5…`, `…COMBINED:UNDER:174.5…`) · changes NONE.
**Card state:** `SETTLED`.
**Final event:** Napoli 82 – **Olimpia Milano 98**, regulation (quarters NAP 25-13-23-21, MIL 18-23-25-32; no OT column). Total 180; Napoli margin −16. Final wall-clock `UNKNOWN`.
**Definition status:** full game incl. OT (card A2); no OT occurred, so the convention question is moot. Operator `UNKNOWN_DEFINITION`.
**Evidence grade:** B (RealGM box + four independent Italian reports; LBA field-owner box not yet opened).
**Expected vs final:** total 172.25 (σ 21) → 180: error +7.75, z = +0.37. Napoli margin +2.10 (σ 16) → −16: error −18.10, z = −1.13.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---:|---|---|---|---|
| 1 | Combined total **Under 174.5** (incl. OT) | 0.542 | 0.557 | **LOSS** | B | Yes | 180 ≥ 175 |
| 2 | **Napoli −1.5** (incl. OT) | 0.515 | 0.521 | **LOSS** | B | Yes | lost by 16 |
| 3 | **Milano +1.5** | 0.485 | 0.479 | **WIN** | B | No | won outright |
| 4 | Combined total **Over 174.5** | 0.458 | 0.443 | **WIN** | B | No | 180 |

**Top-two result:** `ALL_LOST` — decisive denominator 2; primary wins 0/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** binary Brier card / baseline / d_Brier — R1 0.2938 / 0.3102 (0.557²) / −0.0164; R2 0.2652 / 0.2714 (0.521²) / −0.0062; R3 0.2652 / 0.2714 / −0.0062; R4 0.2938 / 0.3102 / −0.0164. The card's baseline was the 24-game LBA league-only normal approximation; on these four rows the card scored marginally better than baseline (negative d), on one event — descriptive only.
**Shadow results:** none frozen; `SHADOW_BASE_ONLY` deferred to prompt 6.
**Form-window check:** unadjusted (raw shrink) margin +4.12 vs adjusted +2.10 (the card's subjective −2.0 Milano-quality prior); observed −16. The adjustment moved in the correct direction but was far too small; total unaffected.
**Winner call:** Napoli ≈0.551 → **incorrect** (Milano won).

**R1. Original prediction:** Rank 1 Under 174.5 at 0.542; Rank 2 Napoli −1.5 at 0.515 (both below gate/floor at issue).
**R2. Final event:** 82–98, regulation, verified on two lineages.
**R3. Contract settlement:** 180 − 174.5 = +5.5 over the line; Napoli −16 versus required +2.
**R4. Rank diagnostics:** 0/2 primary; Hit@2 miss; NDCG@2 0 (winners at ranks 3–4).
**R5. Winner call:** wrong.
**R6. Line assessment:** total +5.5 points above 174.5 (z vs line from centre: +0.26σ); margin 17.5 points beyond the Napoli −1.5 threshold.
**R7. Expected versus realised:** margin error −18.1 (z −1.13) dominates; total moderately above centre.
**R8. Missed mechanism:** Milano won the 4th quarter 32–21 and Mathews/Cole scored 21 each (X7-S09); the card's three-way Milano-foreign-exclusion uncertainty resolved with Mathews, Cole, Hall, Peters, Wright starting (X7-S08). The card had no confirmed Milano five; supported observation, not a measured effect size.
**R9. Source/timing review:** research completed after the scheduled 21:00 AEDT tip; actual tip `NOT_VERIFIED`; lineups unconfirmed at issue (card's own `LINEUP_UNCONFIRMED`). Not a pre-start issue.
**R10. Classification:** process `DEFICIENT` on lineup closure (C20 open at issue, by the card's own audit); model uncalibrated; class `SIDE_CENTRE_MISS / SMALL_SAMPLE_STRENGTH (n=3 LBA games)`.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — early-season (n≤3) team rates against a EuroLeague side should shrink harder toward prior-season/roster strength than k=w 0.40.
**R12. Disposition:** `PROPOSE_EXPERIMENT` (shrinkage strength for n≤3 early-season LBA); LBA field-owner box remains an open corroboration task.

**Rank-1 LOSS — eight-part review**
1. *Claim:* combined points ≤174 incl. OT, p 0.542.
2. *Outcome:* 180 in regulation.
3. *Distribution check:* centre 172.25, σ 21 → 180 is +0.37σ; ordinary.
4. *Knowability:* the active XIIs and Milano's three domestic foreign exclusions were unknown at issue and were not backfilled here.
5. *Process/model/variance:* a 0.542 row ranked first with a 0.027 gap to Rank 2 — flagged RANK1_UNSTABLE at issue; variance-dominated.
6. *Cutoff-only counterfactual:* no defensible cutoff-only flip; the honest alternative was no primary lean.
7. *Failure class:* `NEAR_COINFLIP_RANKED / VARIANCE`.
8. *Correction:* same as G0001 — gate-failing rows recorded as informational (`PROPOSED_NOT_TESTED`).
<!-- END RESEARCH ADDENDUM P-621 2026-10-21-settlement-revision-1 -->

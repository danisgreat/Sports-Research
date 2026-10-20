<!-- BEGIN RESEARCH ADDENDUM P-619 2026-10-21-settlement-revision-1 -->
### Settlement — P-619 (local `LOCAL-20261018K9V4R2M7F6-G0001`), source revision-1
Original: Part 8 canonical research P-619; prior revision: NONE. Source `inputs/20261018K9V4R2M7F6/20261018K9V4R2M7F6_SETTLEMENT.md` offsets 3898–8771; content SHA-256 `e05e172c172a4291f11e07d191c8643bf5e663ec15a2d3a18bd98b9d4c6c9297` (4,873 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018K9V4R2M7F6-G0001 · FC Machida Zelvia v Avispa Fukuoka · 2026-10-21T00:45+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:45+11:00 · affected contract keys ALL (4 ranked + 4 remaining supplied directions) · changes NONE.
**Card state:** `SETTLED`.
**Final event:** **Machida 3–0 Fukuoka**, half-time 1–0 (Yengi 22'), second-half goals Mae 73', Mochizuki 76'. 90 min + stoppage; no extra time in the league. Corners: Machida 1 (J.League) / 2 (ESPN), Fukuoka 5 → total **6 or 7**. Kick-off 07:00Z (18:00 AEDT). Final wall-clock `UNKNOWN`.
**Definition status:** card's 90-minute regulation convention; corners under the card's proposed J.League CK route (K9-S04, total 6) cross-checked with ESPN `wonCorners` (7). Operator `UNKNOWN_DEFINITION`.
**Evidence grade:** goals A (field owner + Opta); corners E (invariant across conflicting values).
**Expected vs final:** Machida 1.90 → 3 (+1.10); Fukuoka 1.05 → 0 (−1.05); total 2.95 → 3 (+0.05; Poisson SD √2.95 = 1.72 → z +0.03); first half 1.10 → 1 (−0.10); corners 8.40 → 6/7 (−2.4/−1.4; Poisson SD 2.90 → z −0.83/−0.48).

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Machida over 0.5 team goals** (90 min) — ANALYST_DERIVED | 0.848 | NOT_AVAILABLE | **WIN** | A | Yes | 3 goals |
| 2 | **Machida or draw (1X / +0.5)** — ANALYST_DERIVED | 0.791 | NOT_AVAILABLE | **WIN** | A | Yes | Machida won |
| 3 | Combined corners **Under 10.5** — SUPPLIED | 0.769 | ≈0.69 (unvalidated diagnostic, not a frozen baseline) | **WIN** | E | No | 6 or 7 |
| 4 | Combined 1st-half goals **Over 0.5** — SUPPLIED | 0.666 | ≈0.657 (diagnostic) | **WIN** | A | No | HT 1–0 |
| — | FT goals Over 2.5 — SUPPLIED, unranked | 0.565 | ≈0.56 (diagnostic) | WIN | A | No | 3 goals |
| — | FT goals Under 2.5 | 0.435 | — | LOSS | A | No | |
| — | 1st-half Under 0.5 | 0.334 | — | LOSS | A | No | |
| — | Corners Over 10.5 | 0.231 | — | LOSS | E | No | |
| — | Winner (3-way, informational): Machida 0.571 / Draw 0.220 / Fukuoka 0.209 | — | — | Machida | A | No | |

**Top-two result:** `ALL_WON` — decisive denominator 2, primary 2/2. Note: Ranks 1–2 are nested team-strength claims (dependent), not mechanically protected; zero joint loss is an outcome, not evidence of protection.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores (binary Brier):** R1 (1−0.848)² = 0.0231; R2 (1−0.791)² = 0.0437; R3 (1−0.769)² = 0.0534 [E]; R4 (1−0.666)² = 0.1116; FT O2.5 0.1892; FT U2.5 0.1892; 1H U0.5 0.1116; corners O10.5 0.0534. Three-way winner half-sum multiclass Brier: 0.5×[(1−0.571)² + 0.220² + 0.209²] = 0.5×(0.1840+0.0484+0.0437) = **0.1381** (labelled half-sum scaling). Paired frozen baselines: 0 → d_Brier `NOT_COMPUTABLE`.
**Shadow results:** none.
**Form-window check:** unadjusted centres Machida 1.918 / Fukuoka 1.195 vs adjusted 1.90 / 1.05; observed 3 / 0. The −0.05 Fukuoka adjustment moved toward the outcome; the −0.22 Machida rest/travel adjustment moved away from it. Net effect small relative to the result.
**Winner call:** Machida → **correct**.

**R1. Original prediction:** Rank 1 Machida team goals Over 0.5 at 0.848; Rank 2 Machida-or-draw at 0.791.
**R2. Final event:** 3–0, HT 1–0, verified by owner and Opta.
**R3. Contract settlement:** team goals 3 ≥ 1; 1X satisfied by the win; corners ≤10 under both providers; 1H goals 1 ≥ 1; FT goals 3 ≥ 3.
**R4. Rank diagnostics:** primary 2/2; Hit@2 hit; NDCG@2 for the four ranked rows (all four won) → DCG 1.631 / IDCG 1.631 = 1.0.
**R5. Winner call:** correct.
**R6. Line assessment:** team goals +2.5 over the 0.5 line; 1X margin +3 vs threshold 0; corners 3.5–4.5 under 10.5; 1H +0.5; FT +0.5 over 2.5.
**R7. Expected versus realised:** goals near the 2.95 centre (z +0.03); Fukuoka scoreless vs 1.05 expected; corners below centre.
**R8. Missed mechanism:** none material for the ranked rows. Process check on the win (S8): the card issued without a confirmed XI (`LINEUP_UNCONFIRMED`) — the same defect that appears in losses elsewhere; the wins do not validate that gap.
**R9. Source/timing review:** kick-off 18:00 AEDT; the card records research at 17:40–17:47 AEDT and no verified issue time — issue phase `UNVERIFIED` (possibly pre-start, not proven). No freeze receipt.
**R10. Classification:** process `NOT_ASSESSABLE` for pre-start certification; lineup closure `DEFICIENT` per card's own C20; outcomes consistent with the issued distribution.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — none specific from one aligned result.
**R12. Disposition:** `NO_CHANGE`; record the J.League vs Opta corner-count conflict as a data-integrity note.
<!-- END RESEARCH ADDENDUM P-619 2026-10-21-settlement-revision-1 -->

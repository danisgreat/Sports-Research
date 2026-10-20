<!-- BEGIN RESEARCH ADDENDUM P-616 2026-10-21-settlement-revision-1 -->
### Settlement — P-616 (local `LOCAL-20261018Q7N4T9B2-G0002`), source revision-1
Original: Part 8 canonical research P-616; prior revision: NONE. Source `inputs/20261018Q7N4T9B2/20261018Q7N4T9B2_SETTLEMENT.md` offsets 11043–15747; content SHA-256 `53157199a02c370bdbce005ea831fac4611501940bd4753440b1db8767d58fd6` (4,704 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018Q7N4T9B2-G0002 · TNT Tropang 5G v Converge FiberXers · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` under the card's declared endpoint; `ENDPOINT_SENSITIVE` (operator terms open).
**Final event:** **Converge 114 – TNT 112 after overtime.** Regulation **106–106** (XERS 27-28-19-32, TNT 35-21-30-20); OT 8–6. Full-game total 226; regulation total 212. Full-game TNT margin −2; regulation 0. Final wall-clock `UNKNOWN`. Venue Ynares Center **Antipolo** (Q7-S04; RealGM's "Pasig" label conflicts).
**Definition status:** the card's A2 interpreted all four rows on the **completed game including OT** ("analysis explicitly assumes normal completed-game OT-inclusive endpoint") → sporting grades below use that frozen convention. Regulation-only alternative shown for transparency; operator terms `UNKNOWN_DEFINITION` and here **grade-changing**.
**Evidence:** B (RealGM box + five independent Philippine reports).
**Expected vs final (full game):** total 220.0 (σ 24) → 226: +6.0, z +0.25. TNT margin −1.0 (σ 20) → −2: −1.0, z −0.05.

| Rank | Exact original proposition | Original p_card (decisive) | Original W / P / L | Original BASELINE_P | Grade (incl. OT — card convention) | Regulation-only alternative | Evidence | Counts toward wins |
|---|---|---:|---|---|---|---|---|---|
| 1 | **Combined Total Under 221.5** | 0.524 | 0.524 / 0 / 0.476 | NOT_ESTIMATED | **LOSS** (226) | WIN (212) | B | Yes |
| 2 | **Giga (TNT) +2.0** | 0.520 | 0.510 / 0.020 / 0.470 | NOT_ESTIMATED | **PUSH** (lost by exactly 2) | WIN (tie) | B | Yes — PUSH excluded from rate |
| 3 | Fiberxers (Converge) −2.0 | 0.480 | 0.470 / 0.020 / 0.510 | NOT_ESTIMATED | **PUSH** | LOSS | B | No |
| 4 | Combined Total Over 221.5 | 0.476 | 0.476 / 0 / 0.524 | NOT_ESTIMATED | **WIN** | LOSS | B | No |

**Top-two result:** `ONE_DECISIVE` — R1 LOSS, R2 PUSH; decisive denominator 1; primary wins 0/1; 1 PUSH.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** binary Brier R1 0.524² = 0.2746; R4 0.476² = 0.2746. Push rows: binary `NOT_COMPUTED` (p_card scores decisive outcomes only, SCV §1); categorical half-sum Brier on the issued W/P/L vector, y = PUSH: R2 0.5×(0.510² + 0.980² + 0.470²) = 0.5×1.4414 = **0.7207**; R3 identical 0.7207 (scaling labelled; not mixed with binary).
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE`.
**Winner call:** Converge ≈0.52 → **correct** (full game).
**R1.** Rank 1 Under 221.5 (0.524); Rank 2 TNT +2.0 (0.520), a PRECISION_TIE at issue. **R2.** 114–112 OT; 106–106 regulation; verified two lineages. **R3.** Full game 226 ≥ 222 → Over; TNT −2 = handicap 0 → push. **R4.** 0 W / 1 L / 1 PUSH; Hit@2 miss; NDCG N/A (push in slate). **R5.** Converge correct. **R6.** Total +4.5 over 221.5 (full game), −9.5 under (regulation); margin exactly on the push point. **R7.** Full-game errors small (|z| ≤ 0.25). The decisive mechanism was the OT period, adding 14 points to a regulation total that sat 9.5 under the line. **R8.** The card flagged OT branching and the push mass as unmodelled ("exact OT winner/total scoring distribution missing"); this event realised exactly that branch. **R9.** Scheduled 20:15 AEDT; card's research clock 20:17 AEDT → `POST_START`; target outcome not used. Starters (Q7-S03): TNT Hollis-Jefferson, Heading, Nambatac, Galinato, Oftana — matches the card's prior-game five; Converge Clark, Baltazar, Tungcab, Stockton, Policarpio (card listed Gómez de Liaño/Williams among Oct-16 starters; both came off the bench). **R10.** Process `NOT_ASSESSABLE` for timing; model's OT branch absent (acknowledged); class `OT_TAIL_ENDPOINT`. **R11.** `PROPOSED_NOT_TESTED`: price PBA totals as regulation mixture + P(tie)×E[OT points] rather than one full-game normal. **R12.** `PROPOSE_EXPERIMENT`; operator-definition request queued (Q7-Q2).

**Rank-1 LOSS — eight-part review:** (1) Total ≤221 incl. OT, p 0.524. (2) 226 after OT; 212 in regulation. (3) Centre 220, σ 24 → 226 is +0.25σ; but the loss came entirely through the OT branch, which the single full-game normal did not represent explicitly. (4) OT occurrence is not knowable pre-start; the endpoint convention was knowable and was declared. (5) Endpoint/model-structure issue plus variance; the near-coinflip rank was flagged at issue. (6) Cutoff-only: a regulation+OT mixture would move this row only slightly (~1–2 pp); no flip. (7) `OT_TAIL_ENDPOINT / NEAR_COINFLIP`. (8) Test the explicit OT branch on PBA history (`PROPOSED_NOT_TESTED`).
<!-- END RESEARCH ADDENDUM P-616 2026-10-21-settlement-revision-1 -->

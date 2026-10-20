<!-- BEGIN RESEARCH ADDENDUM P-614 2026-10-21-settlement-revision-1 -->
### Settlement — P-614 (local `LOCAL-20261018MELILL01-G0003`), source revision-1
Original: Part 8 canonical research P-614; prior revision: NONE. Source `inputs/20261018MELILL01/20261018MELILL01_SETTLEMENT.md` offsets 12731–16086; content SHA-256 `3ffae375dd71c5942ef44ccc9ec34254257eb12bbd2c4dcd9af54ecd6b7fd7fc` (3,355 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018MELILL01-G0003 · ŽBK KP Brno v Žabiny Brno B · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` on the sporting event; operator-identity label `OPEN`.
**Identity:** the card priced the federation match 532124 (ŽBK KP Brno) conditionally because the request said "KP Brno B". ČBF shows KP Brno B is an U17 side that played Zlín at 10:00 the same day and meets Žabiny Brno B only on 7–8 Nov (ML-S07). The only 18 Oct 11:15 KP–Žabiny B game is 532124, so the sporting identity is closed by elimination; whether the user's operator listed this exact event remains unverified.
**Final event:** **ŽBK KP Brno 82 – Žabiny Brno B 51**, regulation (KP 30-29-16-7; Žabiny 11-14-12-14). Total 133; Žabiny margin −31. Final time `UNKNOWN`.
**Definition status:** full game incl. OT; ±4.0 handicap with a push at exactly 4; no OT and no push. Operator `UNKNOWN_DEFINITION`.
**Evidence:** A (ČBF field owner + FIBA LiveStats).
**Expected vs final:** total 129.8 (σ 21) → 133: +3.2, z +0.15. Žabiny margin +6.0 (σ 16) → −31: −37.0, z **−2.31** (|z| > 2).

| Rank | Exact original proposition | Original p_card (decisive) | Original W / P / L | Original BASELINE_P | Grade | Evidence | Counts toward wins |
|---|---|---:|---|---|---|---|---|
| 1 | **Total Under 139.5** | 0.678 | 0.678 / 0 / 0.322 | NOT_DERIVED_EXACT_COMPETITION | **WIN** | A | Research-record primary |
| 2 | **Žabiny Brno B −4.0** | 0.551 | 0.5374 / 0.0247 / 0.4379 | NOT_DERIVED_EXACT_COMPETITION | **LOSS** | A | Research-record primary |
| 3 | ŽBK KP Brno +4.0 | 0.449 | 0.4379 / 0.0247 / 0.5374 | NOT_DERIVED_EXACT_COMPETITION | **WIN** | A | No |
| 4 | Total Over 139.5 | 0.322 | 0.322 / 0 / 0.678 | NOT_DERIVED_EXACT_COMPETITION | **LOSS** | A | No |

**Top-two result:** `SPLIT`; 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** binary — R1 (1−0.678)² = 0.1037; R2 0.551² = 0.3036; R3 (1−0.449)² = 0.3036; R4 0.322² = 0.1037. Categorical half-sum on the push-capable vectors (separate, labelled): R2 0.5×(0.5374² + 0.0247² + 0.5621²) = **0.3027**; R3 identical 0.3027.
**Winner call:** Žabiny B ≈0.646 → **incorrect** (KP won by 31).
**R1.** Rank 1 Under 139.5 (0.678); Rank 2 Žabiny −4 (0.551). **R2.** 82–51; verified two systems. **R3.** 133 ≤ 139; Žabiny −31 vs required +5. **R4.** 1/2; Hit@2 hit; NDCG 1/1.631 = 0.613. **R5.** Wrong. **R6.** Total 6.5 under; handicap missed by 35 points. **R7.** Margin error −37 (z −2.31) — a tail result against the stated width. **R8.** ČBF team stats (ML-S05): KP shot 34.8% from three vs Žabiny 5.0%, and out-rebounded them 57–40. The card had no confirmed lineups for either side, and both teams had played the previous day. Supported observation; cause shares not assessable. **R9.** Card begun before tip, completed time unverified; `ISSUE_PHASE_UNVERIFIED`. **R10.** Process `DEFICIENT` (identity conflict and unconfirmed lineups at issue, per the card's own audit); class `SIDE_CENTRE_MISS / TAIL`. **R11.** `PROPOSED_NOT_TESTED`: second-tier women's leagues with reserve ("B") teams may need much wider margin widths and a roster-availability gate. **R12.** `PROPOSE_EXPERIMENT`.
<!-- END RESEARCH ADDENDUM P-614 2026-10-21-settlement-revision-1 -->

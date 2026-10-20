<!-- BEGIN RESEARCH ADDENDUM P-618 2026-10-21-settlement-revision-1 -->
### Settlement — P-618 (local `LOCAL-20261018Q7N4T9B2-G0004`), source revision-1
Original: Part 8 canonical research P-618; prior revision: NONE. Source `inputs/20261018Q7N4T9B2/20261018Q7N4T9B2_SETTLEMENT.md` offsets 19406–23099; content SHA-256 `23c25397dfcfa76604821aff73a54df8c0e6fea0b94749a830b541693512d44d` (3,693 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018Q7N4T9B2-G0004 · KIA Tigers @ LG Twins, KBO semi-playoff Game 3 · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` as a retained **unissued** research record (`READ_ONLY_DRAFT / NOT_ISSUED`; ordinal G0004 not consumed per the footer).
**Final event:** **KIA 13 – LG 1**, 9 innings (KIA 0-7-0-0-1-1-1-3-0, H16 E0; LG 0-0-0-0-0-1-0-0-0, H8 E1). Start 18:31 KST (20:31 AEDT), end 21:58 KST (23:58 AEDT). KIA won the series 3–0. No draw; the 15-inning tie branch did not arise.
**Definition status:** card A2 — ML conditional on a decisive game (tie → void assumed for p); game was decisive, so the conditional and unconditional grades coincide. Total = full-game runs. Operator `UNKNOWN_DEFINITION`.
**Evidence:** A (KBO owner JSON) + independent report.
**Expected vs final:** total 9.50 (σ 5.0) → 14: +4.5, z +0.90. KIA margin +0.40 (σ 4.8) → +12: +11.6, z **+2.42** (|z| > 2).

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins (research record) | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Combined Total Under 9.5 Runs** | 0.556 | NOT_ESTIMATED | **LOSS** | A | Research-record primary | 14 |
| 2 | **Tigers ML** (decisive-game conditional) | 0.533 | NOT_ESTIMATED | **WIN** | A | Research-record primary | 13–1 |
| 3 | Twins ML | 0.467 | NOT_ESTIMATED | **LOSS** | A | No | |
| 4 | Combined Total Over 9.5 Runs | 0.444 | NOT_ESTIMATED | **WIN** | A | No | |

**Top-two result:** `SPLIT`; 1/2 (unissued record — reported separately from issued cohorts).
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 0.556² = 0.3091; R2 (1−0.533)² = 0.2181; R3 0.467² = 0.2181; R4 (1−0.444)² = 0.3091.
**Shadow results:** none. **Form-window check:** the card's season/L20 shrink (k=60) gave raw total 9.65 vs scenario 9.50; observed 14. Neither centre near the outcome.
**Winner call:** KIA (conditional 0.533) → **correct**.
**R1.** Rank 1 Under 9.5 (0.556); Rank 2 KIA ML (0.533). **R2.** 13–1, nine innings; verified. **R3.** 14 ≥ 10; KIA won. **R4.** 1/2; Hit@2 hit; NDCG winners at 2 and 4 → 0.631/1.631 = 0.387. **R5.** Correct. **R6.** Total 4.5 runs over the line (+0.9σ); margin 12 runs. **R7.** One-sided blowout: margin z +2.42 — a tail outcome relative to the stated width. **R8.** LG starter Carrasco conceded the 7-run 2nd inning (incl. Kim Do-yeong grand slam, Q7-S08); the card had modelled Carrasco as the better run-preventer. Supported observation. **R9.** Request 20:24 AEDT; first pitch 20:31 AEDT; card assembled after → `POST_START`; unissued. Announced lineups were press-corroborated pregame (one of the few cards with confirmed nines). **R10.** Process `NOT_ASSESSABLE` (unissued); model uncalibrated; class `STARTER_COLLAPSE / TAIL`. **R11.** `PROPOSED_NOT_TESTED`: KBO postseason margin width σ 4.8 may be too narrow (one |z|>2 is not evidence alone). **R12.** `MONITOR`; owner to decide whether G0004 is ever issued/imported.

**Rank-1 LOSS — eight-part review:** (1) Total ≤9, p 0.556. (2) 14. (3) +0.9σ from centre — inside the distribution. (4) Starters and lineups were known pregame and used; the 2nd-inning collapse was not knowable. (5) Variance; gate failed at issue (0.556). (6) Cutoff-only: none — the league mean (10.14) would have nudged toward Over, but the card already reported Under at 0.556 as unqualified. (7) `VARIANCE / STARTER_COLLAPSE`. (8) Compare postseason KBO totals against the regular-season 10.14 mean in prompt 6 (`PROPOSED_NOT_TESTED`).
<!-- END RESEARCH ADDENDUM P-618 2026-10-21-settlement-revision-1 -->

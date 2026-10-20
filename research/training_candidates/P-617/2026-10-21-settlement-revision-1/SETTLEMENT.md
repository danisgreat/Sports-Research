<!-- BEGIN RESEARCH ADDENDUM P-617 2026-10-21-settlement-revision-1 -->
### Settlement — P-617 (local `LOCAL-20261018Q7N4T9B2-G0003`), source revision-1
Original: Part 8 canonical research P-617; prior revision: NONE. Source `inputs/20261018Q7N4T9B2/20261018Q7N4T9B2_SETTLEMENT.md` offsets 15878–19275; content SHA-256 `78fbc09c97c4c364c7aea73216110e18a15b5dedb38d4df4025704c98bc92494` (3,397 bytes), exact bytes between the source SETTLEMENT marker lines. Sporting-convention grades only; operator terms unverified; no model feedback, primary or prospective certification. Any NOT_ASSIGNED mapping text inside is the frozen pre-import mapping.

### Settlement · LOCAL-20261018Q7N4T9B2-G0003 · CA Osasuna v Real Racing Club de Santander · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL six directions · changes NONE.
**Card state:** `SETTLED`.
**Final event:** **Osasuna 2–0 Racing**, half-time **1–0** (Budimir penalty 9'), Osambela 88'. Corners **Osasuna 7 + Racing 4 = 11** (ESPN `wonCorners`; SofaScore and La Nación agree). 90 min + stoppage; KO 12:00Z (23:00 AEDT). Final wall-clock `UNKNOWN`.
**Definition status:** card A2 — 1H incl. added time; FT 90'+; corners per ESPN/Opta `wonCorners` (pre-registered RULES_SOCCER §0 route). Operator `UNKNOWN_DEFINITION`.
**Evidence:** goals B (Opta + independent publishers); corners B (two publishers, Opta lineage likely shared).
**Expected vs final:** Osasuna 1.8125 → 2; Racing 1.3125 → 0; FT 3.125 (mixture SD 1.796) → 2: −1.125, z −0.63; 1H 1.575 → 1: −0.575; corners 10.80 (Poisson SD 3.29) → 11: +0.20, z +0.06.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **1H combined goals Over 0.5** | 0.790 | NOT_ESTIMATED | **WIN** | B | Yes | 1 goal by HT |
| 2 | **FT combined goals Over 2.5** | 0.600 | NOT_ESTIMATED | **LOSS** | B | Yes | 2 goals |
| 3 | FT corners Over 10.5 (PROVISIONAL_DIAGNOSTIC at issue) | 0.513 | NOT_ESTIMATED | **WIN** | B | No | 11 |
| 4 | FT corners Under 10.5 (PROVISIONAL_DIAGNOSTIC) | 0.487 | NOT_ESTIMATED | **LOSS** | B | No | 11 |
| 5 | FT goals Under 2.5 | 0.400 | NOT_ESTIMATED | **WIN** | B | No | |
| 6 | 1H goals Under 0.5 | 0.210 | NOT_ESTIMATED | **LOSS** | B | No | |
| — | Winner 3-way (informational): Osasuna 0.492 / D 0.230 / Racing 0.278 | — | — | Osasuna | B | No | |

**Top-two result:** `SPLIT` — R1 W, R2 L; 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (1−0.790)² = 0.0441; R2 0.600² = 0.3600; R3 (1−0.513)² = 0.2372; R4 0.2372; R5 0.3600; R6 0.0441. Three-way winner half-sum Brier 0.5×(0.508² + 0.230² + 0.278²) = 0.5×0.3883 = **0.1941**. Baselines 0.
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE` (no R2 blend admitted; card said weights not available).
**Winner call:** Osasuna plurality → **correct**.
**R1.** Rank 1 1H Over 0.5 (0.790); Rank 2 FT Over 2.5 (0.600). **R2.** 2–0 / HT 1–0 / corners 11; verified. **R3.** 1 ≥ 1; 2 ≤ 2; 11 ≥ 11. **R4.** 1/2; Hit@2 hit; NDCG over ranks 1–4: winners at 1 and 3 → 1/1.631 = 0.613. **R5.** Correct. **R6.** 1H +0.5 goals over the 0.5 line; FT 0.5 goals under 2.5; corners 0.5 over 10.5 (one corner from the other side). **R7.** Racing scored 0 against 1.31 expected; xG reported 3.38 v 0.28 (SofaScore news) — Osasuna created far more than the 2 goals scored. **R8.** R2 loss came from Racing's attack producing nothing and Osasuna's finishing below its chances; supported observation. Process check on the R1 win: the same unconfirmed-XI gap applied (card `LINEUP_UNCONFIRMED`). **R9.** Research began before KO (22:49 AEDT), card assembled after 23:00 → `POST_SCHEDULED_START_ISSUE`; no outcome used. **R10.** Process `DEFICIENT` on lineup closure; model uncalibrated; R2 class `VARIANCE / FINISHING`. **R11.** `PROPOSED_NOT_TESTED`: none specific. **R12.** `MONITOR`.
<!-- END RESEARCH ADDENDUM P-617 2026-10-21-settlement-revision-1 -->

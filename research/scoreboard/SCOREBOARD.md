# Top-two scoreboard (SCV-2026.10.09-v5)

Maintained by hand from the settled tables ([SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md) §7); figures below were generated on 2026-10-09 from the final-settlement table, cards P-126–P-556 (71 with forecasts), and updated by hand on 2026-10-11 with the 20 settled cards imported from the P-556–P-579 mini (P-557–P-576; P-577–P-579 are `PENDING_EVENT` and not scored). Rebuilt and refined from the settlement blocks by the [cohort retrospective of 2026-10-11](../verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) (new cohort P-557–P-576, comparison P-126–P-556); every number below agreed with the rebuild. Update after each import (prompt 4) and each retrospective (prompt 6), and copy the headline into CURRENT_STATE.md.

## Counted cohort (Rank-1 gate passed)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| All counted | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |

Rule T2: only Ranks 1–2 count; PUSH/VOID leave the denominators. Hit@2 0 of 0. Mean NDCG@2 n/a over 0 slates.

## Cohorts shown separately (EVL-05)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| COUNTED (gate passed) | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| RANK1_UNSTABLE | 20 | 34/40 | 85.0% | 70.9–92.9% | 16–4 | 18–2 | 14/6/0 |
| LEGACY_P_ONLY (full gate unknown) | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| UNKNOWN_GATE (not a recorded PASS) | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |
| All forecast cards (historical diagnostic) | 91 | 113/174 | 64.9% | 57.6–71.6% | 56–32 | 57–29 | 41/32/15 |

Missing gate results are never inferred to pass. Historical results remain visible independently of the prospective gate.
RANK1_UNSTABLE cohort (P-557–P-576, every card recorded `RANK1_UNSTABLE` before the event): Hit@2 20 of 20; mean NDCG@2 0.8387 over 20 slates. Most top-two pairs are bracketing totals or covering handicaps whose joint failure is 0% by construction, so the counted rate is not evidence of independent skill.
Informational ranks 3–4 (calibration only; never wins): 106–67 (61.3%, 95% CI 53.8–68.2%); in the RANK1_UNSTABLE cohort 31–9 (77.5%, 95% CI 62.5–87.7%), mean stated p 81.4%, Brier 0.164 (climatology 0.174). Historical cards: mean stated p n/a, Brier n/a.

## Does Rank 2 carry information?

| Slot | W–L | Rate | 95% CI |
|---|---|---:|---|
| Rank 1 | 56–32 | 63.6% | 53.2–72.9% |
| Rank 2 | 57–29 | 66.3% | 55.8–75.4% |
| Ranks 1–2 | 113–61 | 64.9% | 57.6–71.6% |
| Ranks 3–4 | 106–67 | 61.3% | 53.8–68.2% |

RANK1_UNSTABLE cohort only: Rank 1 16–4 (80.0%, 58.4–91.9%); Rank 2 18–2 (90.0%, 69.9–97.2%); Ranks 3–4 31–9 (77.5%, 62.5–87.7%).
UNKNOWN_GATE cohort only: Rank 1 40–28 (58.8%, 47.0–69.7%); Rank 2 39–27 (59.1%, 47.0–70.1%); Ranks 3–4 75–58 (56.4%, 47.9–64.5%); rank 5 (28 cards) 15–12.

Rank 1 does not beat Rank 2, and the intervals of Ranks 1–2 and Ranks 3–4 overlap heavily: the ranking is not separating propositions.

**Joint failure of the top two.** RANK1_UNSTABLE cohort: stated P(both lose) 0.0% by construction on 20 of 20 cards (disjoint losing events); realised `TOP2_ALL_LOST` 0/20 (0.0–16.1%). UNKNOWN_GATE cohort: stated value not recorded; realised 15/68 = 22.1% (13.8–33.3%). Because every RANK1_UNSTABLE pair covers itself, its Hit@2 of 20/20 is mechanical.

## By sport (counted cohort)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|

## By month (counted cohort; month from the event key, else UNDATED)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|

## Historical diagnostic by sport (all forecast cards)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| Australian rules | 1 | 1/2 | 50.0% | 9.5–90.5% | 0–1 | 1–0 | 0/1/0 |
| Baseball | 20 | 26/40 | 65.0% | 49.5–77.9% | 13–7 | 13–7 | 7/12/1 |
| Basketball | 19 | 27/38 | 71.1% | 55.2–83.0% | 11–8 | 16–3 | 10/7/2 |
| Cricket | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Ice hockey | 9 | 14/18 | 77.8% | 54.8–91.0% | 7–2 | 7–2 | 5/4/0 |
| Rugby league | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Soccer | 33 | 42/62 | 67.7% | 55.4–78.0% | 23–9 | 19–11 | 18/7/7 |
| Tennis | 7 | 3/10 | 30.0% | 10.8–60.3% | 2–3 | 1–4 | 1/1/3 |

## By sport, RANK1_UNSTABLE and UNKNOWN_GATE cohorts

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| RANK1_UNSTABLE · Baseball | 6 | 10/12 | 83.3% | 55.2–95.3% | 5–1 | 5–1 | 4/2/0 |
| RANK1_UNSTABLE · Basketball | 8 | 14/16 | 87.5% | 64.0–96.5% | 6–2 | 8–0 | 6/2/0 |
| RANK1_UNSTABLE · Ice hockey | 3 | 4/6 | 66.7% | 30.0–90.3% | 2–1 | 2–1 | 1/2/0 |
| RANK1_UNSTABLE · Soccer | 3 | 6/6 | 100.0% | 61.0–100.0% | 3–0 | 3–0 | 3/0/0 |
| UNKNOWN_GATE · Baseball | 14 | 16/28 | 57.1% | 39.1–73.5% | 8–6 | 8–6 | 3/10/1 |
| UNKNOWN_GATE · Basketball | 11 | 13/22 | 59.1% | 38.7–76.7% | 5–6 | 8–3 | 4/5/2 |
| UNKNOWN_GATE · Ice hockey | 6 | 10/12 | 83.3% | 55.2–95.3% | 5–1 | 5–1 | 4/2/0 |
| UNKNOWN_GATE · Soccer | 30 | 36/56 | 64.3% | 51.2–75.5% | 20–9 | 16–11 | 15/7/7 (1 void) |
| UNKNOWN_GATE · Tennis | 7 | 3/10 | 30.0% | 10.8–60.3% | 2–3 | 1–4 | 1/1/3 (2 void) |
| UNKNOWN_GATE · Australian rules, cricket, rugby league | 3 | 1/6 | — | — | 0–3 | 1–2 | 0/1/2 |

## Historical diagnostic by month (all forecast cards)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| 2026-10 | 39 | 53/76 | 69.7% | 58.7–78.9% | 26–12 | 27–11 | 19/15/4 |
| UNDATED | 52 | 60/98 | 61.2% | 51.3–70.3% | 30–20 | 30–18 | 22/17/11 |

## Rank 1 by proposition family

| Family | Counted W–L | 95% CI | RANK1_UNSTABLE W–L | UNKNOWN_GATE W–L |
|---|---|---|---|---|
| Match total | 0–0 | n/a | 9–3 | 6–6 |
| Handicap / spread | 0–0 | n/a | 4–1 | 11–10 |
| Team total | 0–0 | n/a | 2–0 | 5–3 |
| Period total (first half) | 0–0 | n/a | 1–0 | 9–5 |
| Winner / double chance | 0–0 | n/a | 0–0 | 5–2 |
| Corners | 0–0 | n/a | 0–0 | 4–1 |
| Player prop | 0–0 | n/a | 0–0 | 0–1 |

## Rank-1 failure classes (counted cohort)

| Class | Count |
|---|---:|

RANK1_UNSTABLE cohort: `OVERCONFIDENT_PROBABILITY` × 4 (P-560, P-564, P-571, P-576), each with its eight-part deep retrospection.
UNKNOWN_GATE cohort (28 Rank-1 losses, primary class mapped to SELECTION_RULES §8): `FIRST_HALF_GOAL_OVERSELECTION` 5, `RUNLINE_CUSHION_CEILING` 4, `RANK_BY_Q_NOT_P` 3, `SHARED_DRIVER_TOP_TWO` 3, `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` 2, `TENNIS_IID_UNDERDISPERSION` 2, and one each of `SMALL_SAMPLE_STRENGTH_OVERREACH`, `HANDICAP_TAIL_OVERREACH`, `PHASE_INCOHERENCE`, `CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL`, `OVERCONFIDENT_PROBABILITY`, `WEAK_SLATE_FORCED_RANK`, `QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION`, `REGIME_IGNORED`, `UNFITTED_ANALYST_ADJUSTMENT` (per-ID list in the retrospective's COHORT_TABLES §7).

## Evidence grades (all forecast cards)

A 196, B 135, C 33, E 2, OP 16, X 7; A/B share 85.1% (target 95%). By cohort: RANK1_UNSTABLE 80 rows, A 32, B 28, C 20; UNKNOWN_GATE 309 rows, A 164, B 107, C 13, E 2, OP 16, X 7 (the 2026-10-09 report's 313 rows and A 168 also include the four shadow rows of the no-forecast intake P-532).
Sensitivity (UNKNOWN_GATE cohort): excluding the seven live top-two rows settled on C or E, counted 74/127 = 58.3% (95% CI 49.6–66.5%).
Sensitivity (RANK1_UNSTABLE cohort): excluding the five cards settled only on evidence C (P-560, P-564, P-566, P-572, P-573), counted 26/30 = 86.7% (95% CI 70.3–94.7%).

## Calibration (RANK1_UNSTABLE cohort, frozen p_card against outcome)

80 graded rows (ranks 1–4, no PUSH or VOID): mean stated p 84.2%, win rate 81.2%, Brier 0.148 against climatology 0.152 (Brier skill +0.03). Ranks 1–2 only (40 rows): mean stated p 87.0%, win rate 85.0%, Brier 0.131 against climatology 0.128 (Brier skill −0.03). Rank 1 only (20 rows): mean stated p 88.7%, win rate 80.0%, 16 wins against 17.75 expected (z −1.24), Brier 0.169 against climatology 0.160 (Brier skill −0.06). Rank 2 only: mean stated 85.3%, win rate 90.0%, Brier 0.094 against 0.090.

| Stated p bin | n | Mean stated p | Win rate | 95% CI |
|---|---:|---:|---:|---|
| 50–59% | 1 | 57.9% | 100.0% | 20.7–100.0% |
| 60–69% | 3 | 64.4% | 66.7% | 20.8–93.9% |
| 70–79% | 10 | 75.0% | 50.0% | 23.7–76.3% |
| 80–90% | 66 | 86.9% | 86.4% | 76.1–92.7% |

Descriptive only (one cohort, 20 events, dependent rows). Each bin's mean stated p sits inside its win-rate interval; the 70–79% bin under-performs and is the one to watch. The historical cards have no usable frozen p_card/outcome pairs; their calibration is UNKNOWN. q scores are never substituted for probabilities.

## Legacy literal history (diagnostic only)

522 cards; literal logged_result W/L only; mixed grading eras.

| Rank | W–L | Rate | 95% CI |
|---|---|---:|---|
| 1 | 304–185 | 62.2% | 57.8–66.4% |
| 2 | 251–207 | 54.8% | 50.2–59.3% |
| 3 | 246–207 | 54.3% | 49.7–58.8% |
| 4 | 245–202 | 54.8% | 50.2–59.4% |

Learning diagnostics, not certified prospective skill. Complementary rows are dependent, not independent trials.

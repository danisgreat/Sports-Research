# Top-two scoreboard (SCV-2026.10.09-v5)

Maintained by hand from the settled tables ([SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md) §7); figures below were generated on 2026-10-09 from the final-settlement table, cards P-126–P-556 (71 with forecasts). Update after each import (prompt 4) and each retrospective (prompt 6), and copy the headline into CURRENT_STATE.md.

## Counted cohort (Rank-1 gate passed)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| All counted | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |

Rule T2: only Ranks 1–2 count; PUSH/VOID leave the denominators. Hit@2 0 of 0. Mean NDCG@2 n/a over 0 slates.

## Cohorts shown separately (EVL-05)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| COUNTED (gate passed) | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| RANK1_UNSTABLE | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| LEGACY_P_ONLY (full gate unknown) | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| UNKNOWN_GATE (not a recorded PASS) | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |
| All forecast cards (historical diagnostic) | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |

Missing gate results are never inferred to pass. Historical results remain visible independently of the prospective gate.
Informational ranks 3–4 (calibration only; never wins): 75–58 (56.4%, 95% CI 47.9–64.5%); mean stated p n/a, Brier n/a.

## Does Rank 2 carry information?

| Slot | W–L | Rate | 95% CI |
|---|---|---:|---|
| Rank 1 | 40–28 | 58.8% | 47.0–69.7% |
| Rank 2 | 39–27 | 59.1% | 47.0–70.1% |
| Ranks 1–2 | 79–55 | 59.0% | 50.5–66.9% |
| Ranks 3–4 | 75–58 | 56.4% | 47.9–64.5% |

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
| Baseball | 14 | 16/28 | 57.1% | 39.1–73.5% | 8–6 | 8–6 | 3/10/1 |
| Basketball | 11 | 13/22 | 59.1% | 38.7–76.7% | 5–6 | 8–3 | 4/5/2 |
| Cricket | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Ice hockey | 6 | 10/12 | 83.3% | 55.2–95.3% | 5–1 | 5–1 | 4/2/0 |
| Rugby league | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Soccer | 30 | 36/56 | 64.3% | 51.2–75.5% | 20–9 | 16–11 | 15/7/7 |
| Tennis | 7 | 3/10 | 30.0% | 10.8–60.3% | 2–3 | 1–4 | 1/1/3 |

## Historical diagnostic by month (all forecast cards)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| 2026-10 | 19 | 19/36 | 52.8% | 37.0–68.0% | 10–8 | 9–9 | 5/9/4 |
| UNDATED | 52 | 60/98 | 61.2% | 51.3–70.3% | 30–20 | 30–18 | 22/17/11 |

## Rank 1 by proposition family

| Family | Counted W–L | 95% CI | RANK1_UNSTABLE W–L |
|---|---|---|---|

## Rank-1 failure classes (counted cohort)

| Class | Count |
|---|---:|

## Evidence grades (all forecast cards)

A 164, B 107, C 13, E 2, OP 16, X 7; A/B share 87.7% (target 95%).


No usable frozen p_card/outcome pairs in this cohort. Calibration is UNKNOWN; q scores are never substituted for probabilities.

## Legacy literal history (diagnostic only)

522 cards; literal logged_result W/L only; mixed grading eras.

| Rank | W–L | Rate | 95% CI |
|---|---|---:|---|
| 1 | 304–185 | 62.2% | 57.8–66.4% |
| 2 | 251–207 | 54.8% | 50.2–59.3% |
| 3 | 246–207 | 54.3% | 49.7–58.8% |
| 4 | 245–202 | 54.8% | 50.2–59.4% |

Learning diagnostics, not certified prospective skill. Complementary rows are dependent, not independent trials.

# Top-two scoreboard (SCV-2026.10.09-v4)

Generated deterministically from 1 settlement tables; cards P-126–P-556 (71 with forecasts). Regenerate with `python -B -m research.operations.scoreboard publish`; CI fails if it is stale.

## Counted cohort (Rank-1 gate passed)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| All counted | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |

Rule T2: only Ranks 1–2 count; PUSH/VOID leave the denominators. Hit@2 53 of 71. Mean NDCG@2 0.577569 over 63 slates.

## Cohorts shown separately (EVL-05)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| COUNTED (gate passed) | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |
| RANK1_UNSTABLE | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| All forecast cards | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |

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
| Australian rules | 1 | 1/2 | 50.0% | 9.5–90.5% | 0–1 | 1–0 | 0/1/0 |
| Baseball | 14 | 16/28 | 57.1% | 39.1–73.5% | 8–6 | 8–6 | 3/10/1 |
| Basketball | 11 | 13/22 | 59.1% | 38.7–76.7% | 5–6 | 8–3 | 4/5/2 |
| Cricket | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Ice hockey | 6 | 10/12 | 83.3% | 55.2–95.3% | 5–1 | 5–1 | 4/2/0 |
| Rugby league | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Soccer | 30 | 36/56 | 64.3% | 51.2–75.5% | 20–9 | 16–11 | 15/7/7 |
| Tennis | 7 | 3/10 | 30.0% | 10.8–60.3% | 2–3 | 1–4 | 1/1/3 |

## By month (counted cohort; month from the event key, else UNDATED)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| 2026-10 | 19 | 19/36 | 52.8% | 37.0–68.0% | 10–8 | 9–9 | 5/9/4 |
| UNDATED | 52 | 60/98 | 61.2% | 51.3–70.3% | 30–20 | 30–18 | 22/17/11 |

## Rank 1 by proposition family

| Family | Counted W–L | 95% CI | RANK1_UNSTABLE W–L |
|---|---|---|---|
| corners | 4–1 | 37.6–96.4% | 0–0 |
| first_half_goals | 9–5 | 38.8–83.7% | 0–0 |
| match_total | 5–6 | 21.3–72.0% | 0–0 |
| player_prop | 0–1 | 0.0–79.3% | 0–0 |
| side_cushion_or_handicap | 11–9 | 34.2–74.2% | 0–0 |
| side_winner | 4–1 | 37.6–96.4% | 0–0 |
| team_total | 5–2 | 35.9–91.8% | 0–0 |
| tennis_games | 2–3 | 11.8–76.9% | 0–0 |

## Rank-1 failure classes (counted cohort)

| Class | Count |
|---|---:|
| FIRST_HALF_GOAL_OVERSELECTION | 5 |
| RUNLINE_CUSHION_CEILING | 4 |
| RANK_BY_Q_NOT_P | 3 |
| SHARED_DRIVER_TOP_TWO | 3 |
| BASKETBALL_TOTAL_WITHOUT_PACE_MODEL | 2 |
| TENNIS_IID_UNDERDISPERSION | 2 |
| CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL | 1 |
| HANDICAP_TAIL_OVERREACH | 1 |
| OVERCONFIDENT_PROBABILITY | 1 |
| PHASE_INCOHERENCE | 1 |
| QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION | 1 |
| REGIME_IGNORED | 1 |
| SMALL_SAMPLE_STRENGTH_OVERREACH | 1 |
| UNFITTED_ANALYST_ADJUSTMENT | 1 |
| WEAK_SLATE_FORCED_RANK | 1 |

## Evidence grades (all forecast cards)

A 164, B 107, C 13, E 2, OP 16, X 7; A/B share 87.7% (target 95%).

## Legacy literal history (diagnostic only)

522 cards; literal logged_result W/L only; mixed grading eras.

| Rank | W–L | Rate | 95% CI |
|---|---|---:|---|
| 1 | 304–185 | 62.2% | 57.8–66.4% |
| 2 | 251–207 | 54.8% | 50.2–59.3% |
| 3 | 246–207 | 54.3% | 49.7–58.8% |
| 4 | 245–202 | 54.8% | 50.2–59.4% |

Learning diagnostics, not certified prospective skill. Complementary rows are dependent, not independent trials.

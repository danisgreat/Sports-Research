# Cohort tables — P-601–P-622

Row-level source: [COHORT_ROWS.csv](COHORT_ROWS.csv) (102 rows), built from the import's [EFFECTIVE_SETTLEMENT_ROWS.csv](../mini_import_P-601_P-622_2026-10-21-1/EFFECTIVE_SETTLEMENT_ROWS.csv) joined to issuance, timing, evidence and ISO-week strata.

**Method disclosure.** `python -m ml card-history` reads the committed rank log (through P-600) and hard-coded import inventories that stop at `mini_import_P-590_P-600_2026-10-16-1`. It cannot see this cohort. The tables below were therefore computed by a one-off script kept outside the repository (`cohort.py`, same session scratchpad). The figures reconcile with the import report's hand-computed totals (Rank 1 6W/5L, Rank 2 5W/5L/1P, Brier 0.2041). The tool gap is finding F-03. Full-history context from the tool is in [HISTORY/CARD_HISTORY.md](HISTORY/CARD_HISTORY.md).

All figures are descriptive and outcome-exposed, and grades are literal. There are 2 ISO weeks (W42, W43), against the eight-week floor in SCORING_AND_VALIDATION, so every inferential reading is **INSUFFICIENT_EVIDENCE**.

## 1. Coverage

| Cohort | Events | Rows | W / L / PUSH / VOID / UNRESOLVED | Numeric p | Paired BASELINE_P |
|---|---:|---:|---|---|---|
| RESEARCH_ONLY_NO_MODEL (P-601–P-611), analyst NOT_PRIMARY | 11 | 52 | 25 / 25 / 0 / 0 / 2 | 44 decisive rows with analyst p (P-601 NOT_ESTIMATED; P-604 corners unresolved) | 0 |
| ANALYST_PRIMARY_V1 (P-612–P-622) | 11 | 50 | 25 / 23 / 2 / 0 / 0 | 50 | 8 rows (P-612, P-621), 2 events, 1 week |

Requests retained: 22 of 22 imported cards. Request coverage before the minis (owner requests that never became a card) is **NOT_COMPUTABLE**: the 79B3 R1 and MELILL01 intake histories are external-chat records. The held MELILL01-G0004 card and the unimported A691119714D1 package (8 events) are outside the denominator.

## 2. Primary slots (ANALYST_PRIMARY_V1, ranks 1–2)

| Slot | W / L / PUSH | Decisive rate (Wilson 95%) |
|---|---|---|
| Rank 1 | 6 / 5 / 0 | 6/11 = 54.5% (28.0–78.7) |
| Rank 2 | 5 / 5 / 1 | 5/10 = 50.0% (23.7–76.3) |
| Ranks 1–2 | 11 / 10 / 1 | 11/21 = 52.4% |
| Ranks 3+ (informational, not primary) | 13 / 10 / 1 | — |

Card classes: ALL_WON 3 (P-612, P-613, P-619) · SPLIT 5 (P-614, P-617, P-618, P-620, P-622) · ALL_LOST 2 (P-615, P-621) · ONE_DECISIVE 1 (P-616). **Hit@2 8/11**, both-loss 2/11. Mechanically protected (covering) primary pairs: **0 of 11**. No card's ranks 1–2 are complements or a covering pair. P-622's pair (Zim innings Under 110.5 / Zim 6-over Over 33.5) is anti-coupled, not covering.

Rank 1 by stated p: p ≥ 0.60 **5W/0L** (P-612 0.709, P-613 0.732, P-614 0.678, P-617 0.790, P-619 0.848). p < 0.60 **1W/5L** (P-622 0.560 won; P-615 0.568, P-616 0.524, P-618 0.556, P-620 0.537, P-621 0.542 lost). All five losses were below the 0.62 gate at issue.

## 3. Proper scores

| Set | n | Brier | Log loss | Expected wins (Σp) | Actual |
|---|---:|---:|---:|---:|---:|
| Primary decisive slot rows | 21 | **0.2041** | 0.5907 | 12.86 | 11 |
| All primary-cohort decisive rows (ranks 1–6) | 48 | 0.2018 | — | — | 25 |
| Research-only analyst diagnostics (NOT_PRIMARY) | 44 | 0.2429 (MSE) | 0.6832 | — | 22 |

The P-616 push row is scored separately as push-capable categorical (0.7207, from the settlement), not in the binary set. In-sample "coin" reference 0.25 is descriptive only. The card scored 2.1 fewer wins than its own probabilities implied (12.86 expected, 11 actual).

## 4. Strata (primary slots; Brier on decisive rows)

| Stratum | Cards | Slots W/L/P | Brier (n) |
|---|---:|---|---|
| Basketball | 5 | 3/6/1 | 0.2305 (9) |
| Soccer | 2 | 3/1/0 | 0.1177 (4) |
| Cricket ODI | 1 | 2/0/0 | 0.1135 (2) |
| Cricket T20 | 1 | 1/1/0 | 0.2357 (2) |
| Cricket Test | 1 | 1/1/0 | 0.2575 (2) |
| Baseball (KBO) | 1 | 1/1/0 | 0.2636 (2) |
| Issue NOT_ISSUED_DRAFT (P-612–P-618) | 7 | 7/6/1 | 0.2057 (13) |
| Issue phase UNVERIFIED (P-619–P-622) | 4 | 4/4/0 | 0.2015 (8) |
| Timing POST_START verified (P-613, P-615, P-618, P-622) | 4 | 4/4/0 | 0.2297 (8) |
| Timing UNVERIFIED | 7 | 7/6/1 | 0.1883 (13) |
| Evidence A | 4 | 4/4/0 | 0.2017 (8) |
| Evidence B | 7 | 7/5/1 | 0.1987 (12) |
| Evidence E (P-620 Rank 1, bound) | 1 | 0/1/0 | 0.2884 (1) |
| ISO 2026-W42 | 10 | 10/9/1 | 0.1978 (19) |
| ISO 2026-W43 | 1 | 1/1/0 | 0.2636 (2) |

Every competition cell has one card, and the competition cells are listed individually in COHORT_ROWS.csv. Small strata are explicit: every row above with n ≤ 4 is anecdotal. The evidence-A/B headline (20 decisive slots) equals the A/B+C/E sensitivity view except for P-620's Rank-1 loss, which rests on an invariant lower bound (SA ≥ 324 > 282.5). No row is graded on C/X evidence in the primary slots.

## 5. Reliability (primary decisive slot rows, complete range)

| Bin | n | Mean p | Realised |
|---|---:|---:|---:|
| [0, 0.5) | 0 | — | EMPTY |
| [0.50, 0.55) | 8 | 0.530 | 0.250 |
| [0.55, 0.60) | 4 | 0.559 | 0.250 |
| [0.60, 0.70) | 4 | 0.629 | 0.750 |
| [0.70, 0.80) | 4 | 0.756 | 1.000 |
| [0.80, 1.00] | 1 | 0.848 | 1.000 |

21 rows from 11 events. The bins show a steep, not flat, pattern: the near-coin-flip band realised 3/12 and the ≥ 0.60 band 8/9. The interval on each bin is very wide (for example Wilson 7–59% for 2/8), so no calibration claim follows.

## 6. Paired same-row baseline (frozen BASELINE_P only)

| Event | Rows | Card Brier | Baseline Brier | Mean d (card − base) | Mean d log loss |
|---|---:|---:|---:|---:|---:|
| P-612 NBL | 4 | 0.1108 | 0.0507 | **+0.0601** | +0.1559 |
| P-621 LBA | 4 | 0.2795 | 0.2908 | −0.0114 | −0.0229 |
| Row-equal / event-equal | 8 / 2 | | | +0.0244 / +0.0244 | |

There are 2 events in 1 ISO week, and 4 of the 8 rows are primary slots. P-612's baseline was a stale prior-season league baseline, but it is the frozen one and is used as frozen. The import report's +0.0602/+0.0245 are the same values rounded from per-row figures. **INSUFFICIENT_EVIDENCE.** Missing pairs (42 of 50 rows) remove only paired inference. They do not show the card adds no skill, and they do not show it adds skill.

## 7. Expected versus realised (as reported in each settlement, using the card's own σ)

| Card | Totals / innings z | Margin z |
|---|---|---|
| P-612 | −0.47 | −0.40 |
| P-613 | +0.52 (innings); 5-over +0.14 | — |
| P-614 | +0.15 | **−2.31** |
| P-615 | +0.58 | −0.45 |
| P-616 | +0.25 (full game) | −0.05 |
| P-617 | −0.63 (FT goals); corners +0.06 | — |
| P-618 | +0.90 | **+2.42** |
| P-619 | +0.03 (goals); corners −0.83/−0.48 | — |
| P-620 | ≥ +0.45 (lower bound; excluded from summaries) | — |
| P-621 | +0.37 | −1.13 |
| P-622 | −0.17 (innings); 6-over −1.06 | — |

Summary of the headline totals z (n = 10, P-620 excluded): mean +0.15, RMS 0.48, none beyond ±1. Margins (n = 6): mean −0.32, RMS 1.46, three beyond ±1 and two beyond ±2. Units differ, so the raw errors are never averaged. z is pooled only descriptively. Interval coverage is NOT_COMPUTABLE because the cards did not issue central intervals.

## 8. Research-only analyst diagnostics (NOT_PRIMARY)

Analyst A1 6W/4L, A2 4W/6L (P-602–P-611). There are 44 decisive rows with an analyst p: MSE 0.2429, log loss 0.6832. These never enter primary rank, Hit@2, calibration, feedback or model comparisons.

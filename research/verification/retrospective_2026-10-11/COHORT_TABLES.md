# Cohort tables: retrospective 2026-10-11

Built by hand from the settlement blocks listed in [DATA_INVENTORY.md](DATA_INVENTORY.md) (Combined Log 7, HEAD `df111ce`). Scoring follows [SCORING_AND_VALIDATION.md](../../../SCORING_AND_VALIDATION.md) (SCV-2026.10.09-v5): Rule T2 (only Ranks 1–2 count), PUSH and VOID leave the denominators, Wilson 95% intervals (§3), calibration bins (§4), NDCG@2 over the four-row slate (§6). Ranks 3+ are informational and never enter a win count.

- **New cohort:** P-557 to P-576, 20 cards, all `RANK1_UNSTABLE` (gate label printed on every card before the event).
- **Comparison cohort:** P-126 to P-556, 71 forecast cards from the 2026-10-09 final settlement, all `UNKNOWN_GATE` (no recorded gate result).
- **All:** 91 forecast cards. The `COUNTED` (gate passed) cohort is empty and the `LEGACY_P_ONLY` cohort is empty.

Abbreviations. Grades W/L/V (VOID). Card class: WON = `TOP2_ALL_WON`, SPLIT, LOST = `TOP2_ALL_LOST`, VOID. Rank-1 family: MT match total, HC handicap or spread, TT team total, PT period total (first half), WN winner or double chance, CO corners, PP player prop. Evidence codes per SELECTION_RULES §7. "CI" is the Wilson 95% interval; because the two picks of a card are dependent, every CI is descriptive and understates uncertainty.

## 1. New cohort, card by card (P-557 to P-576)

### 1a. Ranked rows (`p_card` as issued; grade and evidence from the settlement block)

| ID | Sport | Rank 1 (family) | p | G | Rank 2 | p | G | R3 p / G | R4 p / G | Ev | Class | NDCG@2 |
|---|---|---|---:|:-:|---|---:|:-:|---|---|:-:|---|---:|
| P-557 | Baseball | Under 13.5 (MT) | 88.4 | W | Over 5.5 | 73.9 | W | 65.2 W | 57.9 W | B | WON | 1.0000 |
| P-558 | Baseball | Under 16.5 (MT) | 89.5 | W | Over 5.5 | 84.8 | W | 82.1 W | 79.3 L | B | WON | 1.0000 |
| P-559 | Baseball | Under 16.5 (MT) | 89.5 | W | Over 5.5 | 85.1 | L | 82.0 W | 75.5 L | B | SPLIT | 0.6131 |
| P-560 | Basketball | Under 212.5 (MT) | 90.0 | L | Over 163.5 | 89.1 | W | 88.4 W | 88.0 W | C | SPLIT | 0.3869 |
| P-561 | Soccer | Beijing +1.5 (HC) | 86.4 | W | Over 1.5 | 80.0 | W | 76.9 L | 74.6 L | B | WON | 1.0000 |
| P-562 | Ice hockey | Mountfield team Under 4.5 (TT) | 89.4 | W | Over 3.5 | 82.8 | W | 75.3 L | 65.7 W | A | WON | 1.0000 |
| P-563 | Basketball | KTP +17.5 (HC) | 89.8 | W | Pyrintö +22.5 | 89.1 | W | 88.5 W | 88.4 W | B | WON | 1.0000 |
| P-564 | Baseball | Under 16.5 (MT) | 88.0 | L | Over 6.5 | 86.0 | W | 84.7 L | 81.7 W | C | SPLIT | 0.3869 |
| P-565 | Basketball | Under 204.5 (MT) | 89.7 | W | Over 155.5 | 89.4 | W | 89.3 W | 88.9 W | B | WON | 1.0000 |
| P-566 | Basketball | Under 200.5 (MT) | 89.8 | W | Over 151.5 | 89.1 | W | 89.0 W | 88.8 W | C | WON | 1.0000 |
| P-567 | Soccer | Over 1.5 (MT) | 86.8 | W | Under 5.5 | 85.9 | W | 80.1 W | 80.0 W | A | WON | 1.0000 |
| P-568 | Basketball | Chemnitz team Under 99.5 (TT) | 89.8 | W | Chemnitz team Over 62.5 | 89.7 | W | 89.6 W | 89.5 W | A | WON | 1.0000 |
| P-569 | Soccer | First-half Under 2.5 (PT) | 84.3 | W | Over 1.5 | 82.8 | W | 74.3 W | 73.8 W | A | WON | 1.0000 |
| P-570 | Ice hockey | HIFK +3.5 (HC) | 88.7 | W | KalPa team Over 1.5 | 84.6 | L | 84.0 W | 83.8 W | A | SPLIT | 0.6131 |
| P-571 | Ice hockey | Florida +2.5 (HC) | 88.4 | L | Minnesota team Over 1.5 | 74.1 | W | 72.1 W | 62.2 L | A | SPLIT | 0.3869 |
| P-572 | Baseball | KT +4.5 (HC) | 88.6 | W | Over 4.5 | 86.0 | W | 84.2 L | 83.7 W | C | WON | 1.0000 |
| P-573 | Baseball | Under 14.5 (MT) | 89.1 | W | Over 4.5 | 84.7 | W | 82.8 L | 81.1 W | C | WON | 1.0000 |
| P-574 | Basketball | Over 139.5 (MT) | 89.4 | W | Under 187.5 | 89.2 | W | 87.8 W | 85.5 W | A | WON | 1.0000 |
| P-575 | Basketball | Over 166.5 (MT) | 89.4 | W | Under 216.5 | 89.3 | W | 88.6 W | 86.1 W | B | WON | 1.0000 |
| P-576 | Basketball | Over 144.5 (MT) | 89.9 | L | Under 198.5 | 89.6 | W | 89.2 W | 88.5 W | A | SPLIT | 0.3869 |

Every card graded all four rows on one evidence code (column Ev). Sum of NDCG@2: 14 × 1.0000 + 2 × 0.6131 + 4 × 0.3869 = 14 + 1.2262 + 1.5476 = 16.7738; mean 16.7738 / 20 = **0.8387**.

### 1b. Decision-block and process fields (from each card and its settlement R9)

Minutes = `Research completed` − `Scheduled start` (positive = completed after the scheduled start).

| ID | Timing state | Minutes | Gate margin (points) | P(both lose) stated | Adjustment dependence | Regime flags | Rules read: sport file / SELECTION_RULES / SOURCES | Archive check | Evidence quotes | R9 process |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| P-557 | PREGAME | −9.6 | 0.8 | 0.0% | NONE | NONE | field absent (`mini-log-3`) | field absent | `Evidence snapshots` (hash tokens) | DEFICIENT |
| P-558 | PREGAME | −1.2 | 2.4 | 0.0% | NONE | NONE | field absent | field absent | hash tokens | DEFICIENT |
| P-559 | LATE_START_UNVERIFIED | +4.2 | 0.2 | 0.0% | NONE | NONE | field absent | field absent | hash tokens | DEFICIENT |
| P-560 | LATE_START_UNVERIFIED | +7.0 | 0.4 | 0.0% | NONE | EARLY_SEASON | field absent | field absent | hash tokens | DEFICIENT |
| P-561 | PREGAME | −7.4 | 1.3 | 0.0% | NONE | NONE | yes / yes / §3.4 | UNAVAILABLE (CSL header-only) | quotes | DEFICIENT |
| P-562 | PREGAME | −5.2 | 1.6 | 0.0% | NONE | EARLY_SEASON (no multiplier) | yes / yes / §3.9 | UNAVAILABLE (Czech header-only) | quotes | DEFICIENT |
| P-563 | LATE_START_UNVERIFIED | −0.3 | 0.31 | 0.0% | NONE | EARLY_SEASON (no multiplier) | yes / yes / §3.2 | UNAVAILABLE (no Korisliiga file) | quotes | DEFICIENT |
| P-564 | LATE_START_UNVERIFIED | +3.2 | 0.8 | 0.0% | ADJUSTMENT_DEPENDENT | NONE | yes / yes / §3.1 | rows read: KBO 2025, 874 rows; 2026 file absent | quotes | DEFICIENT |
| P-565 | LATE_START_UNVERIFIED | +1.5 | 0.30 | 0.0% | NONE | EARLY_SEASON (1.000) | yes / yes / §3.2 | rows read: NBL 2025, 206 rows; 2026 absent | quotes | DEFICIENT |
| P-566 | LATE_START_UNVERIFIED | +11.5 | 0.71 | 0.0% | ADJUSTMENT_DEPENDENT | EARLY_SEASON (1.000) | yes / yes / §3.2 | rows read: NBL 2025, 206 rows; 2026 absent | quotes | DEFICIENT |
| P-567 | LATE_START_UNVERIFIED | +1.2 | 0.9 | 0.0% | NONE | NONE | yes / yes / §3.4 | UNAVAILABLE (Bundesliga header-only) | quotes | DEFICIENT |
| P-568 | LATE_START_UNVERIFIED | +0.6 | 0.06 | 0.0% | NONE (but removing a < 0.25 SD adjustment changes the top two) | NONE | yes / yes / §3.2 | UNAVAILABLE (no BBL file; BSL excluded) | quotes | DEFICIENT |
| P-569 | LATE_START_UNVERIFIED | +0.8 | 1.5 | 0.0% | NONE | non-standard: `EREDIVISIE_EARLY_SAMPLE` | yes / yes / §3.4 | UNAVAILABLE (no Eredivisie file) | quotes | DEFICIENT |
| P-570 | LATE_START_UNVERIFIED | +5.4 | 0.2 | 0.0% | ADJUSTMENT_DEPENDENT | non-standard list (5 labels) | yes / yes / §3.9 | UNAVAILABLE (no Liiga file; NHL for comparison) | quotes | DEFICIENT |
| P-571 | LATE_START_UNVERIFIED | +10.8 | ~2.5 | 0.0% | NONE | EARLY_SEASON, NHL 1.024 applied | yes / yes / §3.9 | files shown: NHL 2024, 2025 (profile n 3,936) | quotes | DEFICIENT |
| P-572 | PREGAME | −5.0 | not printed (line says it fails 4.0) | 0.0% | NONE | NONE | yes / yes / §3.1 | PARTIAL: KBO 2023–25 headers and first record; profile row | quotes | DEFICIENT |
| P-573 | LATE_START_UNVERIFIED | +4.1 | 0.89 | 0.0% | NONE | NONE | yes / yes / §3.1 | PARTIAL: KBO 2023–25 headers; profile row | quotes | DEFICIENT |
| P-574 | PREGAME | −58.7 | 0.3 | 0.0% | NONE | EARLY_SEASON, RULE_CHANGE:on_court_free (no multiplier) | yes / yes / §3.2 | UNAVAILABLE (B League files header-only) | quotes | DEFICIENT |
| P-575 | LATE_START_UNVERIFIED | +5.2 | 0.1 | 0.0% | NONE | NONE | yes / yes / §3.2 | PARTIAL: NBL 2023–25 headers and first record; profile row | quotes | DEFICIENT |
| P-576 | PREGAME | −9.6 | 0.3 | 0.0% | NONE | non-standard: `BPREMIER_2026_NEW_FORMAT`, `EARLY_SEASON_SIX_GAMES` | yes / yes / §3.2 | UNAVAILABLE (B League header-only) | quotes | DEFICIENT |

Counts: `LATE_START_UNVERIFIED` 13 of 20; completed after the scheduled start 12 of 20 (P-563 finished 17 seconds before it and is still labelled late). Gate margin below 4.0 points on 20 of 20 (largest 2.5). Stated P(both lose) 0.0% "by construction" on 20 of 20. `ADJUSTMENT_DEPENDENT` 3 of 20 (P-564, P-566, P-570). Regime flag other than `NONE` on 10 of 20 (7 in the SELECTION_RULES §6 vocabulary, 3 with non-standard labels); a multiplier was applied once (P-571, NHL `EARLY_SEASON` 1.024, the §6 value); every other flag correctly applied no shift. `Rules read` present on 16 of 16 `mini-log-5` cards, each naming the sport file, the SELECTION_RULES sections and a SOURCES route. `Evidence quotes` present (not `NONE`) on 16 of 16. R9 `Process: DEFICIENT` on 20 of 20, `SOUND` on 0.

## 2. Comparison cohort, card by card (P-126 to P-556)

| ID | Sport | R1 family | R1 | R2 | Class | | ID | Sport | R1 family | R1 | R2 | Class |
|---|---|---|:-:|:-:|---|---|---|---|---|:-:|:-:|---|
| P-126 | Soccer | WN | W | V | WON | | P-524 | Baseball | HC | L | W | SPLIT |
| P-136 | Tennis | MT | V | V | VOID | | P-525 | Baseball | HC | W | L | SPLIT |
| P-148 | Soccer | PT | L | L | LOST | | P-526 | Baseball | MT | W | W | WON |
| P-149 | Soccer | PT | W | W | WON | | P-527 | Basketball | MT | L | W | SPLIT |
| P-166 | Ice hockey | HC | W | W | WON | | P-528 | Ice hockey | WN | W | W | WON |
| P-176 | Soccer | TT | L | L | LOST | | P-529 | Ice hockey | WN | W | W | WON |
| P-178 | Soccer | MT | W | L | SPLIT | | P-530 | Baseball | HC | W | W | WON |
| P-179 | Soccer | TT | W | L | SPLIT | | P-531 | Basketball | HC | L | L | LOST |
| P-200 | Ice hockey | HC | L | W | SPLIT | | P-533 | Baseball | WN | W | L | SPLIT |
| P-217 | Cricket | TT | L | L | LOST | | P-534 | Rugby league | HC | L | L | LOST |
| P-233 | Soccer | TT | W | W | WON | | P-535 | Basketball | HC | W | W | WON |
| P-234 | Soccer | PT | L | W | SPLIT | | P-536 | Basketball | HC | W | W | WON |
| P-235 | Soccer | PT | W | W | WON | | P-537 | Soccer | PT | W | W | WON |
| P-250 | Soccer | PT | L | V | LOST | | P-538 | Ice hockey | WN | W | W | WON |
| P-251 | Soccer | PT | W | L | SPLIT | | P-539 | Tennis | HC | W | L | SPLIT |
| P-255 | Soccer | PT | W | W | WON | | P-540 | Tennis | HC | V | V | VOID |
| P-256 | Soccer | CO | W | W | WON | | P-541 | Tennis | HC | L | L | LOST |
| P-265 | Soccer | CO | W | L | SPLIT | | P-542 | Basketball | MT | W | W | WON |
| P-274 | Baseball | HC | L | W | SPLIT | | P-543 | Baseball | HC | W | W | WON |
| P-341 | Soccer | PT | W | L | SPLIT | | P-544 | Baseball | HC | L | W | SPLIT |
| P-342 | Soccer | PT | L | L | LOST | | P-545 | Baseball | HC | W | L | SPLIT |
| P-368 | Soccer | PT | W | W | WON | | P-546 | Baseball | HC | W | L | SPLIT |
| P-369 | Soccer | CO | L | L | LOST | | P-547 | Baseball | HC | L | W | SPLIT |
| P-377 | Soccer | PT | L | L | LOST | | P-548 | Basketball | MT | L | W | SPLIT |
| P-399 | Soccer | PT | W | W | WON | | P-549 | Soccer | WN | L | L | LOST |
| P-401 | Soccer | CO | W | W | WON | | P-550 | Ice hockey | MT | W | L | SPLIT |
| P-407 | Soccer | CO | W | W | WON | | P-551 | Tennis | MT | L | L | LOST |
| P-409 | Soccer | TT | W | W | WON | | P-552 | Basketball | MT | W | L | SPLIT |
| P-410 | Soccer | TT | W | W | WON | | P-553 | Basketball | MT | L | W | SPLIT |
| P-418 | Soccer | — (contracts lost) | V | V | VOID | | P-554 | Basketball | HC | W | W | WON |
| P-419 | Soccer | TT | W | W | WON | | P-555 | Tennis | HC | L | L | LOST |
| P-430 | Soccer | TT | L | W | SPLIT | | P-556 | Tennis | MT | W | W | WON |
| P-492 | Baseball | PP | L | L | LOST | | | | | | | |
| P-518 | Baseball | HC | W | L | SPLIT | | | | | | | |
| P-519 | Australian rules (AFLW) | MT | L | W | SPLIT | | | | | | | |
| P-520 | Baseball | WN | L | W | SPLIT | | | | | | | |
| P-521 | Basketball | HC | L | W | SPLIT | | | | | | | |
| P-522 | Basketball | MT | L | L | LOST | | | | | | | |
| P-523 | Soccer | PT | W | W | WON | | | | | | | |

Tallies from this table: Rank 1 40 W / 28 L / 3 V; Rank 2 39 W / 27 L / 5 V; classes 27 WON, 26 SPLIT, 15 LOST, 3 VOID; Hit@2 = 27 + 26 = 53 of 68 cards with a live top-two row. These equal the 2026-10-09 report and the block's own cohort line (line 3,126).

## 3. Rule T2 summary by cohort

| Cohort | Cards | Live top-two rows | Counted wins | Rate | 95% CI | Rank 1 W–L–V | Rank 2 W–L–V | WON / SPLIT / LOST / VOID | Hit@2 | Mean NDCG@2 |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|
| New (P-557–P-576), `RANK1_UNSTABLE` | 20 | 40 | 34 | 85.0% | 70.9–92.9% | 16–4–0 | 18–2–0 | 14 / 6 / 0 / 0 | 20/20 (83.9–100%) | 0.8387 (20 slates) |
| Comparison (P-126–P-556), `UNKNOWN_GATE` | 71 | 134 | 79 | 59.0% | 50.5–66.9% | 40–28–3 | 39–27–5 | 27 / 26 / 15 / 3 | 53/68 (66.7–86.2%) | not recorded |
| All forecast cards | 91 | 174 | 113 | 64.9% | 57.6–71.6% | 56–32–3 | 57–29–5 | 41 / 32 / 15 / 3 | 73/88 (73.8–89.4%) | — |
| `COUNTED` (gate PASS) | 0 | 0 | 0 | n/a | n/a | 0–0 | 0–0 | 0 / 0 / 0 / 0 | n/a | n/a |

Arithmetic: new 16 + 18 = 34 of 20 + 20 = 40; comparison 40 + 39 = 79 of 68 + 66 = 134; all 113 of 174. Wilson check against SCORING_AND_VALIDATION §3: 79/134 gives 50.5–66.9% (the page's own worked example).

## 4. Slot rates side by side (Rank 1, Rank 2, ranks 3+)

| Slot | New | Comparison | All |
|---|---|---|---|
| Rank 1 | 16–4, 80.0% (58.4–91.9) | 40–28, 58.8% (47.0–69.7) | 56–32, 63.6% (53.2–72.9) |
| Rank 2 | 18–2, 90.0% (69.9–97.2) | 39–27, 59.1% (47.0–70.1) | 57–29, 66.3% (55.8–75.4) |
| Ranks 1–2 | 34–6, 85.0% (70.9–92.9) | 79–55, 59.0% (50.5–66.9) | 113–61, 64.9% (57.6–71.6) |
| Ranks 3–4 (informational) | 31–9, 77.5% (62.5–87.7) | 75–58, 56.4% (47.9–64.5) | 106–67, 61.3% (53.8–68.2) |
| Rank 5 (informational; comparison only) | — | 15–12, 55.6% (37.3–72.4) | 15–12 |
| Ranks 3+ (informational) | 31–9, 77.5% | 90–70, 56.2% (48.5–63.7) | 121–79, 60.5% |

Rank 3 and Rank 4 separately. New: Rank 3 15–5, Rank 4 16–4. Comparison: Rank 3 36–31–3 V, Rank 4 39–27–4 V.

**Reading.** In no cohort does Rank 1 beat Rank 2, and in every cohort the Ranks 1–2 interval overlaps the Ranks 3–4 interval. The ranking is not separating propositions.

## 5. By sport

| Sport | New: cards, counted, R1, R2, W/S/L | Comparison: cards, counted, R1, R2, W/S/L/V | All: counted (CI) |
|---|---|---|---|
| Baseball | 6; 10/12; 5–1; 5–1; 4/2/0 | 14; 16/28; 8–6; 8–6; 3/10/1/0 | 26/40, 65.0% (49.5–77.9) |
| Basketball | 8; 14/16; 6–2; 8–0; 6/2/0 | 11; 13/22; 5–6; 8–3; 4/5/2/0 | 27/38, 71.1% (55.2–83.0) |
| Ice hockey | 3; 4/6; 2–1; 2–1; 1/2/0 | 6; 10/12; 5–1; 5–1; 4/2/0/0 | 14/18, 77.8% (54.8–91.0) |
| Soccer | 3; 6/6; 3–0; 3–0; 3/0/0 | 30; 36/56; 20–9; 16–11; 15/7/7/1 | 42/62, 67.7% (55.4–78.0) |
| Tennis | 0 | 7; 3/10; 2–3; 1–4; 1/1/3/2 | 3/10, 30.0% (10.8–60.3) |
| Australian rules | 0 | 1; 1/2; 0–1; 1–0; 0/1/0/0 | 1/2 |
| Cricket | 0 | 1; 0/2; 0–1; 0–1; 0/0/1/0 | 0/2 |
| Rugby league | 0 | 1; 0/2; 0–1; 0–1; 0/0/1/0 | 0/2 |
| **Total** | **20; 34/40** | **71; 79/134** | **113/174** |

Counted-rate intervals for the larger cells: new baseball 83.3% (55.2–95.3), new basketball 87.5% (64.0–96.5); comparison baseball 57.1% (39.1–73.5), basketball 59.1% (38.7–76.7), ice hockey 83.3% (55.2–95.3), soccer 64.3% (51.2–75.5), tennis 30.0% (10.8–60.3).

## 6. Rank 1 by proposition family (live Rank-1 rows)

| Family | New W–L | Comparison W–L | All W–L | All rate (CI) |
|---|---|---|---|---|
| Match total (MT) | 9–3 | 6–6 | 15–9 | 62.5% (42.7–78.8) |
| Handicap / spread (HC) | 4–1 | 11–10 | 15–11 | 57.7% (38.9–74.5) |
| Team total (TT) | 2–0 | 5–3 | 7–3 | 70.0% (39.7–89.2) |
| Period total, first half (PT) | 1–0 | 9–5 | 10–5 | 66.7% (41.7–84.8) |
| Winner / double chance (WN) | 0–0 | 5–2 | 5–2 | 71.4% (35.9–91.8) |
| Corners (CO) | 0–0 | 4–1 | 4–1 | 80.0% (37.6–96.4) |
| Player prop (PP) | 0–0 | 0–1 | 0–1 | — |
| **Total** | **16–4** | **40–28** | **56–32** | 63.6% |

### Sport × family cells, Rank 1, all cohorts

| Cell | W–L | Rate (CI) | Note |
|---|---|---|---|
| Soccer × first-half period total | 10–5 | 66.7% (41.7–84.8) | 9–5 comparison (all 1H Over 0.5), 1–0 new (1H Under 2.5) |
| Basketball × match total | 6–6 | 50.0% (25.4–74.6) | comparison 2–4, new 4–2 |
| Baseball × handicap | 7–4 | 63.6% (35.4–84.8) | +1.5 to +4.5 run lines |
| Baseball × match total | 6–1 | 85.7% (48.7–97.4) | comparison 1–0, new 5–1 |
| Soccer × team total | 5–2 | 71.4% (35.9–91.8) | comparison only |
| Basketball × handicap | 4–2 | 66.7% (30.0–90.3) | |
| Soccer × corners | 4–1 | 80.0% (37.6–96.4) | comparison only |
| Ice hockey × winner | 3–0 | 100% (43.8–100) | comparison only |
| Ice hockey × handicap | 2–2 | 50.0% | comparison 1–1, new 1–1 |
| Tennis × all families | 2–3 | 40.0% (11.8–76.9) | comparison only |
| Baseball × winner | 1–1 | — | |
| Every other cell | n ≤ 2 | — | |

No cell has an interval wholly below 50% or wholly above 50%.

## 7. Rank-1 failure classes (SELECTION_RULES §8; aliases mapped)

**New cohort (4 Rank-1 losses, each with the eight-part deep retrospection).**

| Class | Count | IDs | Stated p | Realised outcome in the card's own distribution |
|---|---:|---|---|---|
| `OVERCONFIDENT_PROBABILITY` | 4 | P-560, P-564, P-571, P-576 | 90.0, 88.0, 88.4, 89.9 | total z +2.49; total z +1.33; margin z −1.40; total z −1.57 |

P-571 also records a `LATE_INFORMATION` timing concern (unconfirmed goalie, card completed 10.8 minutes after the scheduled start).

**Comparison cohort (28 Rank-1 losses).** Primary class = the first class named on each block's `Failure class` line, mapped to §8.

| Class (§8) | Primary count | IDs | All mentions (including second classes and the 2026-10-09 baseline grouping) |
|---|---:|---|---|
| `FIRST_HALF_GOAL_OVERSELECTION` | 5 | P-148, P-234, P-250, P-342, P-377 | 5 |
| `RUNLINE_CUSHION_CEILING` | 4 | P-274, P-524, P-544, P-547 | 4 |
| `RANK_BY_Q_NOT_P` | 3 | P-519, P-521, P-522 | 3 |
| `SHARED_DRIVER_TOP_TWO` (alias `TOP_ROW_DEPENDENCE`) | 3 | P-492, P-541, P-549 | 5 (+ P-176, P-555) |
| `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` | 2 | P-527, P-548 | 3 (+ P-553 in the baseline grouping) |
| `TENNIS_IID_UNDERDISPERSION` | 2 | P-551, P-555 | 3 (+ P-541 in the baseline grouping) |
| `SMALL_SAMPLE_STRENGTH_OVERREACH` | 1 | P-176 | 1 |
| `HANDICAP_TAIL_OVERREACH` | 1 | P-200 | 1 |
| `PHASE_INCOHERENCE` | 1 | P-217 | 1 |
| `CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL` | 1 | P-369 | 1 |
| `OVERCONFIDENT_PROBABILITY` (alias `OVERCONFIDENT_TEAM_TOTAL`) | 1 | P-430 | 1 |
| `WEAK_SLATE_FORCED_RANK` | 1 | P-520 | 1 (+ second labels `NO_EDGE_RANK1` P-234, `NEAR_COIN_FLIP_RANK1` P-553) |
| `QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION` | 1 | P-531 | 1 (+ `LATE_RESEARCH` → `LATE_INFORMATION`) |
| `REGIME_IGNORED` (alias `FINALS_REGIME_IGNORED`) | 1 | P-534 | 2 (+ `RULE_CHANGE_REGIME_SHIFT` on P-548) |
| `UNFITTED_ANALYST_ADJUSTMENT` | 1 | P-553 | 1 |
| **Total** | **28** | | |

Second labels with no §8 class (mapped to `OTHER`): `REDUCED_OVERS_RISK_UNMODELLED` (P-217), `NAMED_KILL_PATH_UNDERWEIGHTED` (P-250), `ROTATION_CONVERSION_DISCOUNT_MISSING` (P-342), `LEAGUE_BASE_RATE_MISSING` (P-377), `MEAN_VS_TAIL_INCOHERENCE` (P-524), `TENNIS_WORKLOAD_UNMODELLED` (P-541); `FABRICATED_SETTLEMENT_RECORD` (P-519) maps to `SOURCE_OR_IDENTITY`.

**Baseline (FRAMEWORK_RETROSPECTIVE §3.3):** first-half goal 5, +1.5 cushion 4, basketball total without pace 3, tennis i.i.d. 3, rank by q 3, dependent top two 5, other 7 (classes overlap).

## 8. Evidence grades (every graded row, ranks 1+)

| Cohort | Rows | A | B | C | E | OP | X | A/B share | C+E+OP+X share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| New | 80 | 32 | 28 | 20 | 0 | 0 | 0 | 75.0% | 25.0% |
| Comparison (71 forecast cards) | 309 | 164 | 107 | 13 | 2 | 16 | 7 | 87.7% | 12.3% |
| All | 389 | 196 | 135 | 33 | 2 | 16 | 7 | 85.1% | 14.9% |

New-cohort cards by code (all four rows share it): A P-562, P-567, P-568, P-569, P-570, P-571, P-574, P-576 (8 × 4 = 32); B P-557, P-558, P-559, P-561, P-563, P-565, P-575 (7 × 4 = 28); C P-560, P-564, P-566, P-572, P-573 (5 × 4 = 20). KBO: 0 of 6 cards at A (3 B on MyKBO, 3 C on MyKBO or Yonhap; the official KBO scoreboard was stale or unreadable each time).

Comparison live top-two rows by code: A 45 W / 33 L; B 27 W / 18 L; C 3 W / 2 L (P-126 R1, P-537 R1 wins; P-149 R2 win; P-148 R2, P-377 R2 losses); E 2 W (P-255 R2, P-256 R1); OP 2 W / 2 L (P-200 R2 W, P-274 R2 W; P-217 R1 L, P-274 R1 L).

**Sensitivity, C and E rows excluded.**

| Cohort | All rows | Excluding C and E | Also excluding OP |
|---|---|---|---|
| New, counted | 34/40, 85.0% (70.9–92.9) | 34 − 8 = 26 of 40 − 10 = 30, 86.7% (70.3–94.7) | same (no OP) |
| New, Rank 1 | 16/20, 80.0% | 13/15, 86.7% (62.1–96.3) | same |
| Comparison, counted | 79/134, 59.0% (50.5–66.9) | 79 − 5 = 74 of 134 − 7 = 127, 58.3% (49.6–66.5) | 72/123, 58.5% (49.7–66.9) |

## 9. Calibration of stated `p_card` (new cohort; SCORING_AND_VALIDATION §4)

The comparison settlement tables carry no `p_card`; comparison calibration is `NOT_COMPUTABLE` (the scoreboard already records it as unknown). q is never substituted.

**Inputs (80 graded rows; p in %; W/L).**

| Rank | Rows (ID p grade) | Sum of p | Wins |
|---|---|---:|---:|
| 1 | 557 88.4 W · 558 89.5 W · 559 89.5 W · 560 90.0 L · 561 86.4 W · 562 89.4 W · 563 89.8 W · 564 88.0 L · 565 89.7 W · 566 89.8 W · 567 86.8 W · 568 89.8 W · 569 84.3 W · 570 88.7 W · 571 88.4 L · 572 88.6 W · 573 89.1 W · 574 89.4 W · 575 89.4 W · 576 89.9 L | 1,774.9 | 16 |
| 2 | 557 73.9 W · 558 84.8 W · 559 85.1 L · 560 89.1 W · 561 80.0 W · 562 82.8 W · 563 89.1 W · 564 86.0 W · 565 89.4 W · 566 89.1 W · 567 85.9 W · 568 89.7 W · 569 82.8 W · 570 84.6 L · 571 74.1 W · 572 86.0 W · 573 84.7 W · 574 89.2 W · 575 89.3 W · 576 89.6 W | 1,705.2 | 18 |
| 3 | 557 65.2 W · 558 82.1 W · 559 82.0 W · 560 88.4 W · 561 76.9 L · 562 75.3 L · 563 88.5 W · 564 84.7 L · 565 89.3 W · 566 89.0 W · 567 80.1 W · 568 89.6 W · 569 74.3 W · 570 84.0 W · 571 72.1 W · 572 84.2 L · 573 82.8 L · 574 87.8 W · 575 88.6 W · 576 89.2 W | 1,654.1 | 15 |
| 4 | 557 57.9 W · 558 79.3 L · 559 75.5 L · 560 88.0 W · 561 74.6 L · 562 65.7 W · 563 88.4 W · 564 81.7 W · 565 88.9 W · 566 88.8 W · 567 80.0 W · 568 89.5 W · 569 73.8 W · 570 83.8 W · 571 62.2 L · 572 83.7 W · 573 81.1 W · 574 85.5 W · 575 86.1 W · 576 88.5 W | 1,603.0 | 16 |

**Bins (all 80 rows).**

| Stated p bin | n | Mean stated p | Win rate | 95% CI | Stated p inside CI? |
|---|---:|---:|---:|---|---|
| 50–59% | 1 | 57.9% | 1/1 = 100% | 20.7–100% | yes |
| 60–69% | 3 | 64.4% (193.1 / 3) | 2/3 = 66.7% | 20.8–93.9% | yes |
| 70–79% | 10 | 75.0% (749.8 / 10) | 5/10 = 50.0% | 23.7–76.3% | yes, at the edge |
| 80–90% | 66 | 86.9% | 57/66 = 86.4% | 76.1–92.7% | yes |

70–79% rows: 557 R2 73.9 W, 571 R2 74.1 W, 569 R3 74.3 W, 571 R3 72.1 W, 569 R4 73.8 W; 561 R3 76.9 L, 562 R3 75.3 L, 558 R4 79.3 L, 559 R4 75.5 L, 561 R4 74.6 L.

**Ranks 1–2 only (40 rows).** 70–79%: 2 rows, 2/2. 80–90%: 38 rows, mean stated 87.7% (3,332.1 / 38), 32/38 = 84.2% (69.6–92.6).

**Brier and skill.** Brier = mean of (p − y)²; climatology = b(1 − b) with b the realised win rate of the same rows (an in-sample reference, which flatters climatology slightly).

| Rows | n | Mean stated p | Win rate | Σ(p − y)² | Brier | Climatology | Brier skill | Expected wins Σp | Observed |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rank 1 | 20 | 88.7% | 80.0% | 3.3833 | 0.169 | 0.160 | −0.06 | 17.75 | 16 |
| Rank 2 | 20 | 85.3% | 90.0% | 1.8713 | 0.094 | 0.090 | −0.04 | 17.05 | 18 |
| Ranks 1–2 | 40 | 87.0% | 85.0% | 5.2546 | 0.131 | 0.128 | −0.03 | 34.80 | 34 |
| Ranks 3–4 | 40 | 81.4% | 77.5% | 6.5507 | 0.164 | 0.174 | +0.06 | 32.57 | 31 |
| All 80 | 80 | 84.2% | 81.2% | 11.8053 | 0.148 | 0.152 | +0.03 | 67.37 | 65 |

Rank-1 arithmetic: the 16 wins contribute 0.2093 in total (for example P-557: (0.884 − 1)² = 0.0135); the four losses contribute 0.8100 + 0.7744 + 0.7815 + 0.8082 = 3.1741; Σ = 3.3833; 3.3833 / 20 = 0.169. Rank-1 shortfall: 16 observed against 17.75 expected, SD √Σp(1 − p) = 1.41, z = −1.24. With a constant 11.3% loss rate, P(4 or more losses in 20) ≈ 0.18.

A least-squares reliability line is not reported: 66 of 80 stated probabilities sit between 80% and 90%, so the slope is not identified.

## 10. Joint failure of the top two

| Cohort | Mean stated P(Rank 1 and Rank 2 both lose) | Realised `TOP2_ALL_LOST` | 95% CI |
|---|---|---|---|
| New | 0.0% (20 of 20 cards print "0.0% by construction") | 0/20 = 0.0% | 0.0–16.1% |
| Comparison | `NOT_COMPUTABLE` (not recorded in the settlement tables; most cards predate the field) | 15/68 = 22.1% | 13.8–33.3% |
| All | — | 15/88 = 17.0% | 10.6–26.2% |

New-cohort top-two structures: a bracketing match total (Under A with Over B, B below A) on 12 cards (P-557, 558, 559, 560, 564, 565, 566, 567, 573, 574, 575, 576); a bracketing team total on 1 (P-568); opposite-side handicaps on 1 (P-563); a handicap or team total covered by a total on 6 (P-561, P-562, P-569 first-half Under with full-time Over, P-570, P-571, P-572). In every pair the two losing events are disjoint, so P(both lose) = 0 and Hit@2 = 20/20 follows from the construction, not from forecasting.

## 11. Expected score against the final (`mini-log-5` cards P-561 to P-576)

Orientation here is home minus away for the margin, so some signs differ from the card's own line (P-564, P-572, P-574 list the away side first). Error = final − expected; z = error ÷ the SD printed on the card.

| ID | Sport | Home: exp → final (err, z) | Away: exp → final (err, z) | Total: exp (SD) → final (err, z) | Margin H−A: exp → final (err, z) |
|---|---|---|---|---|---|
| P-561 | Soccer | 1.325 → 0 (−1.32, −1.15) | 1.635 → 3 (+1.36, +1.07) | 2.960 (1.724) → 3 (+0.04, +0.02) | −0.31 → −3 (−2.69, −1.57) |
| P-567 | Soccer | 1.25 → 2 (+0.75, +0.67) | 2.24 → 2 (−0.24, −0.16) | 3.49 (1.87) → 4 (+0.51, +0.27) | −0.99 → 0 (+0.99, +0.53) |
| P-569 | Soccer | 1.84 → 3 (+1.16, +0.85) | 1.36 → 3 (+1.64, +1.40) | 3.20 (1.80) → 6 (+2.80, +1.56) | +0.48 → 0 (−0.48, −0.27) |
| P-562 | Ice hockey | 3.407 → 5 (+1.59, +0.88) | 2.452 → 2 (−0.45, −0.29) | 5.859 (2.362) → 7 (+1.14, +0.48) | +0.955 → +3 (+2.04, +0.84) |
| P-570 | Ice hockey | 2.70 → 6 (+3.30, +2.00) | 3.33 → 1 (−2.33, −1.30) | 6.03 (2.40) → 7 (+0.97, +0.40) | −0.63 → +5 (+5.63, +2.28) |
| P-571 | Ice hockey | 3.16 → 1 (−2.16, −1.23) | 2.69 → 4 (+1.31, +0.79) | 5.86 (2.35) → 5 (−0.86, −0.37) | +0.47 → −3 (−3.47, −1.40) |
| P-564 | Baseball | 5.08 → 8 (+2.92, +1.04) | 5.99 → 9 (+3.01, +0.91) | 11.07 (4.47) → 17 (+5.93, +1.33) | −0.90 → −1 (−0.10, −0.02) |
| P-572 | Baseball | 4.40 → 3 (−1.40, −0.47) | 4.72 → 12 (+7.28, +2.19) | 9.11 (4.58) → 15 (+5.89, +1.29) | −0.32 → −9 (−8.68, −1.99) |
| P-573 | Baseball | 4.973 → 1 (−3.97, −1.20) | 3.818 → 4 (+0.18, +0.06) | 8.791 (4.448) → 5 (−3.79, −0.85) | +1.155 → −3 (−4.16, −0.98) |
| P-563 | Basketball (Korisliiga) | 85.93 → 88 (+2.07, +0.15) | 83.16 → 72 (−11.16, −0.89) | 169.09 (21.28) → 160 (−9.09, −0.43) | +2.78 → +16 (+13.22, +0.83) |
| P-565 | Basketball (NBL) | 90.54 → 99 (+8.46, +0.68) | 89.16 → 104 (+14.84, +1.21) | 179.70 (19.56) → 203 (+23.30, +1.19) | +1.38 → −5 (−6.38, −0.42) |
| P-566 | Basketball (NBL) | 90.27 → 100 (+9.73, +0.78) | 85.25 → 84 (−1.25, −0.10) | 175.52 (19.59) → 184 (+8.48, +0.43) | +5.03 → +16 (+10.97, +0.72) |
| P-568 | Basketball (BBL) | 80.93 → 83 (+2.07, +0.14) | 88.88 → 87 (−1.88, −0.14) | 169.80 (22.09) → 170 (+0.20, +0.01) | −7.95 → −4 (+3.95, +0.24) |
| P-574 | Basketball (B.PREMIER) | 81.45 → 81 (−0.45, −0.04) | 82.18 → 89 (+6.82, +0.57) | 163.63 (19.36) → 170 (+6.37, +0.33) | −0.73 → −8 (−7.27, −0.52) |
| P-575 | Basketball (NBL) | 96.22 → 100 (+3.78, +0.29) | 95.25 → 110 (+14.75, +1.14) | 191.47 (20.15) → 210 (+18.53, +0.92) | +0.96 → −10 (−10.96, −0.68) |
| P-576 | Basketball (B.PREMIER) | 86.98 → 68 (−18.98, −1.40) | 84.68 → 70 (−14.68, −1.11) | 171.66 (21.41) → 138 (−33.66, −1.57) | +2.30 → −2 (−4.30, −0.27) |

Extra soccer terms. First-half total: P-561 0.970 → 2 (+1.03, z +1.05); P-567 1.47 → 1 (−0.47, −0.39); P-569 1.36 → 1 (−0.36, −0.31). First-half teams: P-561 home 0.42 → 0 (−0.42, −0.65), away 0.55 → 2 (+1.45, +1.95); P-569 home 0.77 → 0 (−0.77, −0.88), away 0.59 → 1 (+0.41, +0.53); P-567 home 0.49 → 1 (+0.51) and away 0.98 → 0 (−0.98), no SD printed. Second-half total: P-567 2.02 → 3 (+0.98, +0.69); P-569 1.84 → 5 (+3.16, +2.32). Corners: P-561 10.307 → 6 (−4.31, −1.01), no corners row ranked.

**By sport and term.** Mean error = Σ error ÷ n; the interval is mean ± t × s/√n (t = 2.447 for n = 7, 4.303 for n = 3); a normal z has mean |z| ≈ 0.80.

| Sport | Term | n | Σ error | Mean error | 95% interval | Mean \|z\| | Share \|z\| > 2 | Verdict |
|---|---|---:|---:|---:|---|---:|---|---|
| Basketball | home | 7 | +6.68 | +0.95 | −7.8 to +9.8 | 0.50 | 0/7 | INSUFFICIENT_EVIDENCE |
| Basketball | away | 7 | +7.44 | +1.06 | −9.8 to +11.9 | 0.74 | 0/7 | INSUFFICIENT_EVIDENCE |
| Basketball | total | 7 | +14.13 | +2.02 | −15.6 to +19.7 | 0.70 | 0/7 | INSUFFICIENT_EVIDENCE |
| Basketball | margin | 7 | −0.77 | −0.11 | −8.9 to +8.7 | 0.53 | 0/7 | INSUFFICIENT_EVIDENCE |
| Basketball, NBL only | total | 3 | +50.31 | +16.77 | −2.0 to +35.6 | 0.85 | 0/3 | INSUFFICIENT_EVIDENCE (3 of 3 above; with P-560's diagnostic centre, 4 of 4 above, mean +24.2, −1.5 to +49.9) |
| Baseball (KBO) | home | 3 | −2.45 | −0.82 | −9.5 to +7.8 | 0.90 | 0/3 | INSUFFICIENT_EVIDENCE |
| Baseball (KBO) | away | 3 | +10.47 | +3.49 | −5.4 to +12.4 | 1.05 | 1/3 (P-572 +2.19) | INSUFFICIENT_EVIDENCE |
| Baseball (KBO) | total | 3 | +8.03 | +2.68 | −11.2 to +16.6 | 1.16 | 0/3 | INSUFFICIENT_EVIDENCE |
| Baseball (KBO) | margin | 3 | −12.93 | −4.31 | −15.0 to +6.4 | 1.00 | 0/3 (P-572 −1.99) | INSUFFICIENT_EVIDENCE |
| Ice hockey | home | 3 | +2.73 | +0.91 | −6.0 to +7.8 | 1.37 | 0/3 (P-570 exactly 2.00) | INSUFFICIENT_EVIDENCE |
| Ice hockey | away | 3 | −1.47 | −0.49 | −5.0 to +4.0 | 0.79 | 0/3 | INSUFFICIENT_EVIDENCE |
| Ice hockey | total | 3 | +1.25 | +0.42 | −2.3 to +3.2 | 0.42 | 0/3 | INSUFFICIENT_EVIDENCE |
| Ice hockey | margin | 3 | +4.20 | +1.40 | −10.0 to +12.8 | 1.51 | 1/3 (P-570 +2.28) | INSUFFICIENT_EVIDENCE |
| Soccer | home | 3 | +0.58 | +0.19 | −3.1 to +3.5 | 0.89 | 0/3 | INSUFFICIENT_EVIDENCE |
| Soccer | away | 3 | +2.76 | +0.92 | −1.6 to +3.4 | 0.88 | 0/3 | INSUFFICIENT_EVIDENCE |
| Soccer | total | 3 | +3.35 | +1.12 | −2.6 to +4.8 | 0.62 | 0/3 | INSUFFICIENT_EVIDENCE |
| Soccer | margin | 3 | −2.18 | −0.73 | −5.3 to +3.9 | 0.79 | 0/3 | INSUFFICIENT_EVIDENCE |
| Soccer | first-half total | 3 | +0.20 | +0.07 | −2.0 to +2.1 | 0.58 | 0/3 | INSUFFICIENT_EVIDENCE |
| Soccer | second-half total | 2 | +4.14 | +2.07 | −11.8 to +15.9 | 1.51 | 1/2 (P-569 +2.32) | INSUFFICIENT_EVIDENCE |

Worked interval (basketball total): errors −9.09, +23.30, +8.48, +0.20, +6.37, +18.53, −33.66; mean +2.02; squared deviations sum 2,186.9; s = √(2,186.9 / 6) = 19.09; s/√7 = 7.22; ± 2.447 × 7.22 = ± 17.7. Across all 16 cards, 0 of 16 total errors exceed 2 SD and the mean |z| of the total is 0.72.

## 12. Subgroups used in the report (counted wins over live top-two rows)

| Split (new cohort) | Cards | Counted | Rate (CI) | Rank 1 |
|---|---:|---|---|---|
| Timing PREGAME | 7 | 13/14 | 92.9% (68.5–98.7) | 6–1 |
| Timing LATE_START_UNVERIFIED | 13 | 21/26 | 80.8% (62.1–91.5) | 10–3 |
| `ADJUSTMENT_DEPENDENT` | 3 | 4/6 | 66.7% (30.0–90.3) | 2–1 |
| Adjustment NONE | 17 | 30/34 | 88.2% (73.4–95.3) | 14–3 |
| Archive rows actually read (P-564, P-565, P-566, P-571) | 4 | 6/8 | 75.0% (40.9–92.9) | 2–2 |
| Archive partial: headers and profile row (P-572, P-573, P-575) | 3 | 6/6 | 100% (61.0–100) | 3–0 |
| `ARCHIVE_UNAVAILABLE` (P-561, 562, 563, 567, 568, 569, 570, 574, 576) | 9 | 16/18 | 88.9% (67.2–96.9) | 8–1 |
| No archive field (`mini-log-3`, P-557–P-560) | 4 | 6/8 | 75.0% (40.9–92.9) | 3–1 |
| Process `DEFICIENT` | 20 | 34/40 | 85.0% | 16–4 |
| Process `SOUND` | 0 | — | — | — |

Winner calls (not a ranked row): new 10 correct of 20 (50.0%, 29.9–70.1) at a mean stated winner probability of 56.4%; comparison 37 correct of 48 recoverable (23 not recoverable).

## 13. Spot check (five random IDs, recomputed from their blocks)

IDs drawn at random (`shuf -n 5`) from the 91 forecast-card IDs, after the tables were built: **P-560, P-550, P-561, P-341, P-126**.

| ID | Block line | From the block | In these tables | Agree |
|---|---:|---|---|---|
| P-560 | 8,025 | R1 Under 212.5 90.0% LOSS C; R2 Over 163.5 89.1% WIN C; R3 88.4% W, R4 88.0% W; `TOP2_SPLIT`; NDCG 0.3869; deep retrospection, `OVERCONFIDENT_PROBABILITY` | §1a, §7, §8 (C list), §9 | yes |
| P-550 | 4,679 (addendum) | R1 Under 7.5 goals WIN A; R2 Anaheim +1.5 LOSS A; `TOP2_SPLIT`; winner call correct | §2 (Ice hockey, MT, W, L, SPLIT) | yes |
| P-561 | 8,079 | R1 Beijing +1.5 86.4% WIN B; R2 Over 1.5 80.0% WIN B; R3 76.9% L; R4 74.6% L; `TOP2_ALL_WON`; total expected 2.960 → 3 (+0.04, z +0.02) | §1a, §8 (B list), §9 (80–90 and 70–79 bins), §11 | yes |
| P-341 | 3,569 (consolidated block) | R1 first-half Over 0.5 WIN B; R2 Under 2.5 LOSS B; R3 VOID X; `TOP2_SPLIT` | §2 (Soccer, PT, W, L, SPLIT); §8 comparison X count | yes |
| P-126 | 3,132 (consolidated block) | R1 match winner WIN C; R2 first-half Over 0.5 VOID X; `TOP2_ALL_WON`, 1 counted of 1 | §2 (Soccer, WN, W, V, WON); §8 C/E/OP list (P-126 R1 C win) | yes |

An earlier hand-picked check of P-559, P-566, P-571, P-430 and P-548 also agreed in every field. No disagreement was found, and no table was changed after either check.

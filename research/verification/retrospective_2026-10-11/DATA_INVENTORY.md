# Data inventory: cohort retrospective 2026-10-11

Mode `COHORT_RETROSPECTIVE` (prompt 6, Markdown only, no cohort program). Base `main` = `origin/main` = `df111ce71f64a211b29bf3bddca92860f2321b72`, clean.

## 1. Scope (written 2026-10-11T22:37+11:00, before the tables were built)

- **Last retrospective.** No `research/verification/retrospective_*` folder exists. The last cohort retrospective is the 2026-10-09 pair: [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](../../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md) and the [final settlement of all pending records](../final_settlement_2026-10-09/REPORT.md), which settled every record through **P-556**.
- **New cohort:** the first card after that retrospective through the highest settled ID: **P-557 to P-576** (20 cards). P-577, P-578 and P-579 are canonical but `PENDING_EVENT`; they are excluded and never used.
- **Comparison cohort:** everything before that which has a final-settlement row: the **71 forecast cards from P-126 to P-556** in the 2026-10-09 final settlement (72 event records; P-532 is an intake with no ranked rows, `NO_FORECAST`). The legacy literal rank history (522 cards, mixed grading eras, no settlement blocks) is not a cohort here; it stays a diagnostic line on the scoreboard.
- **All:** the union, 91 forecast cards.
- **Below the 30-card threshold.** Prompt 6 runs at 30 newly settled cards "or whenever the user asks". The new cohort has 20; the user asked for this run.
- **Disclosure.** The new cohort's top-line totals were already computed during the canonical import earlier the same day (`research/verification/mini_import_P-556_P-579_2026-10-11/`). The ranges above follow mechanically from the rule (first ID after the last retrospective through the highest settled ID); they were not chosen with the results in view, and no other window is analysed.

## 2. New cohort: the settlement block used for each ID

File: `prediction logs/PREDICTION_LOG_COMBINED_7.md` (Combined Log 7). Each ID has exactly one settlement block, imported 2026-10-11 as `<!-- BEGIN RESEARCH ADDENDUM P-NNN 20261011-1 -->` with the heading `**Final settlement (<date>).**`. Line numbers are those of the `<!-- BEGIN SETTLEMENT P-NNN -->` marker at HEAD `df111ce`; the card line is its `<!-- BEGIN CANONICAL RESEARCH P-NNN -->` marker.

| ID | Sport / league | Card line | Settlement line | Settled (sources read) | Card format | Settlement format |
|---|---|---:|---:|---|---|---|
| P-557 | Baseball / KBO | 4,867 | 7,911 | 2026-10-09 | `mini-log-3` | `mini-settlement-3` style, `Expected vs final` N/A |
| P-558 | Baseball / KBO | 5,000 | 7,949 | 2026-10-09 | `mini-log-3` | as P-557 |
| P-559 | Baseball / KBO | 5,126 | 7,987 | 2026-10-09 | `mini-log-3` | as P-557 |
| P-560 | Basketball / NBL | 5,248 | 8,025 | 2026-10-09 | `mini-log-3` | as P-557 |
| P-561 | Soccer / Chinese Super League | 5,365 | 8,079 | 2026-10-10 | `mini-log-5` | `mini-settlement-4` |
| P-562 | Ice hockey / Czech Extraliga | 5,489 | 8,117 | 2026-10-10 | `mini-log-5` | `mini-settlement-4` |
| P-563 | Basketball / Finnish Korisliiga | 5,604 | 8,155 | 2026-10-10 | `mini-log-5` | `mini-settlement-4` |
| P-564 | Baseball / KBO | 5,724 | 8,193 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-565 | Basketball / NBL | 5,854 | 8,248 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-566 | Basketball / NBL | 5,986 | 8,286 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-567 | Soccer / Bundesliga | 6,125 | 8,324 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-568 | Basketball / German BBL | 6,241 | 8,362 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-569 | Soccer / Eredivisie | 6,371 | 8,400 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-570 | Ice hockey / Finnish Liiga | 6,491 | 8,438 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-571 | Ice hockey / NHL | 6,617 | 8,476 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-572 | Baseball / KBO | 6,772 | 8,524 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-573 | Baseball / KBO | 6,899 | 8,562 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-574 | Basketball / B.LEAGUE PREMIER | 7,035 | 8,600 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-575 | Basketball / NBL | 7,197 | 8,638 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |
| P-576 | Basketball / B.LEAGUE PREMIER | 7,332 | 8,676 | 2026-10-11 | `mini-log-5` | `mini-settlement-4` |

Excluded: P-577 (card line 7,470), P-578 (7,594; A8 addendum 7,845) and P-579 (7,728), all `PENDING_EVENT` with no settlement block.

Card-side fields read for each ID (same file, inside its canonical block): `Timing state`, `Research completed`, `Scheduled start`, `Regime flags`, `Expected score`, `Rules read`, `Archive check`, `Evidence quotes` (or `Evidence snapshots` on `mini-log-3`), and the decision-block lines `P(Rank 1 and Rank 2 both lose)`, `Rank-1 gate`, `Adjustment dependence` and `Potential winner`.

## 3. Comparison cohort: the settlement rows used

Source: [final_settlement_2026-10-09/REPORT.md](../final_settlement_2026-10-09/REPORT.md), the per-record table (the latest settlement for every ID P-126 to P-556; each row names the log, the card and the evidence for every rank). The settlement text for these records sits in the Combined Logs under "Final settlement of all pending records — 2026-10-09" (Combined Log 7, from line 3,120) and in the dated addenda that follow it. The 2026-10-09 report is the settled table those blocks were written from; this retrospective counts from its per-record table and does not re-grade any row.

For each comparison ID the latest settlement is the 2026-10-09 final settlement in Combined Log 7. Earlier settlements of the same IDs (for example the P-550–P-556 addenda at lines 2,818–3,119, and the settlements in Parts 4–6) are superseded and were not used.

**(a) Consolidated block, "Final settlement of all pending records — 2026-10-09" (Combined Log 7, heading line 3,120).** Line = the record's `### Final settlement · P-NNN` heading.

| ID | Line | ID | Line | ID | Line | ID | Line | ID | Line |
|---|---:|---|---:|---|---:|---|---:|---|---:|
| P-126 | 3,132 | P-233 | 3,363 | P-342 | 3,589 | P-418 | 3,796 | P-539 | 4,039 |
| P-136 | 3,151 | P-234 | 3,383 | P-368 | 3,618 | P-419 | 3,812 | P-540 | 4,058 |
| P-148 | 3,170 | P-235 | 3,412 | P-369 | 3,638 | P-430 | 3,832 | P-541 | 4,077 |
| P-149 | 3,199 | P-250 | 3,432 | P-377 | 3,667 | P-492 | 3,861 | P-542 | 4,105 |
| P-166 | 3,219 | P-251 | 3,461 | P-399 | 3,696 | P-518 | 3,889 | P-543 | 4,124 |
| P-176 | 3,238 | P-255 | 3,481 | P-401 | 3,716 | P-519 | 3,908 | P-544 | 4,143 |
| P-178 | 3,267 | P-256 | 3,501 | P-407 | 3,736 | P-520 | 3,936 | P-545 | 4,171 |
| P-179 | 3,287 | P-265 | 3,521 | P-409 | 3,756 | P-521 | 3,964 | P-546 | 4,190 |
| P-200 | 3,307 | P-274 | 3,541 | P-410 | 3,776 | P-522 | 3,992 | P-547 | 4,209 |
| P-217 | 3,335 | P-341 | 3,569 | — | — | P-538 | 4,020 | P-548 | 4,237 |
| | | | | | | | | P-549 | 4,265 |

**(b) Dated final-settlement addenda (Combined Log 7).** Line = the `<!-- BEGIN RESEARCH ADDENDUM P-NNN … -->` marker; each addendum holds `**Final settlement (2026-10-09) — …**`.

| ID | Line | ID | Line | ID | Line |
|---|---:|---|---:|---|---:|
| P-523 | 4,296 | P-530 | 4,476 | P-550 | 4,679 |
| P-524 | 4,320 | P-531 | 4,499 | P-551 | 4,702 |
| P-525 | 4,352 | P-533 | 4,554 | P-552 | 4,734 |
| P-526 | 4,375 | P-534 | 4,577 | P-553 | 4,757 |
| P-527 | 4,398 | P-535 | 4,609 | P-554 | 4,789 |
| P-528 | 4,430 | P-536 | 4,632 | P-555 | 4,812 |
| P-529 | 4,453 | P-537 | 4,655 | P-556 | 4,844 |

P-532 (line 4,531) is a `NO_FORECAST` intake; its shadow-ordered rows are excluded from every count here. P-418 is a forecast card whose original ranked contracts were not preserved; it counts as a VOID card with one X row.

**Row extraction.** The rank rows (`| <rank> | <proposition> | **<grade>** | … | <evidence> | … |`) of every block above were listed in a scratch file outside the repository: 308 rows on 70 cards plus P-418's single X row = 309 rows on 71 forecast cards (P-532's 4 rows would make the 2026-10-09 report's 313). By rank, live grades: Rank 1 40 W / 28 L / 2 V (+ P-418 = 3 V); Rank 2 39 W / 27 L / 4 V (+ P-418 = 5 V); Rank 3 36 / 31 / 3 V; Rank 4 39 / 27 / 4 V; Rank 5 (28 cards had five rows) 15 / 12 / 1 V. Evidence codes on the 309 rows: A 164, B 107, C 13, E 2, OP 16, X 7. These equal the 2026-10-09 report's totals (79/134; Rank 1 40-28-3V; Rank 2 39-27-5V; A 168 including P-532's four A rows).

**What the comparison blocks do not hold.** The 2026-10-09 settlement tables have no `p_card` column, no stated P(both lose), no R9/R10 process verdict, no `Expected vs final` line and no archive check. Those quantities are `NOT_COMPUTABLE` for the comparison cohort and are reported as such; they were not reconstructed from the original cards, whose probabilities were issued under older conventions (p and q columns, legacy rank orders).

## 4. Other sources read

- Sport for each comparison card: the league label in each `**Final settlement (2026-10-09) — <event> (<league>).**` line.
- Rank-1 failure classes: the `**Failure class.**` line of each of the 28 comparison deep retrospections and the 4 new-cohort ones; the comparison baseline counts in [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](../../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md) §3.3 and in the consolidated block's opening paragraph (line 3,128).
- League levels: [LEAGUE_PROFILES.md](../../../LEAGUE_PROFILES.md) and [BASE_RATES_REGISTER.md](../../../BASE_RATES_REGISTER.md) §7.1 (NBL 2025-26).
- Recommendation register: [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](../../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md) §5 and §5.8.
- Experiments: [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md).

## 5. How the numbers were produced

Counting was done from the blocks listed above. The rows, grades, probabilities and expected-score terms were copied into scratch files outside the repository and every total was cross-checked against the blocks' own `Top-two result` lines and the import and 2026-10-09 reports. Wilson bounds, Brier sums and means were evaluated with a calculator on those scratch files; every input row is printed in [COHORT_TABLES.md](COHORT_TABLES.md) so each number can be redone by hand. Nothing in the repository was executed, and no settlement was edited.

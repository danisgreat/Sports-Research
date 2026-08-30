# Settlement audit and reference update — 2026-07-29

Status: **V6-021 SETTLED AND GRADED; NO RECORD PENDING PRIOR TO V6-022**

Sweep run at 2026-07-29T10:40:00Z (2026-07-29 20:40 AEST). Scope: the single record in `PREDICTION_RESULTS_LOG_v6.md` whose `result` was `PENDING` — V6-021.

## Live check before any settlement work

| Record | Event | Scheduled start (UTC) | Live check at sweep time | Outcome |
|---|---|---|---|---|
| V6-021 | Sunrisers Leeds Men v Manchester Super Giants Men, The Hundred 10th Match | 2026-07-28T17:30Z | Complete — ESPNcricinfo returns a final result string and two closed innings | Settled |

## Verified final

Manchester Super Giants **181/3 (100 balls)**, extras 5 (1 b, 4 w); Sunrisers Leeds **186/2 (88 balls)**, target 182. **Sunrisers Leeds won by 8 wickets with 12 balls remaining.** MSG **Powerplay 1 (balls 1-25): 41/1**, from the scorecard's own phase line, not inferred from the innings total; Sunrisers' powerplay was 34/1 and must not be confused with it. Buttler 63* (33), Klaasen 53 (27), Markram 32 (23). Marsh 63 (26) Player of the Match.

Source: [ESPNcricinfo full scorecard 1521240](https://www.espncricinfo.com/series/the-hundred-men-s-competition-2026-1521176/manchester-super-giants-men-vs-sunrisers-leeds-men-10th-match-1521240/full-scorecard) and the [series match-results page](https://www.espncricinfo.com/series/the-hundred-men-s-competition-2026-1521176/match-results), both opened 2026-07-29T10:32Z via the validated text proxy. The two agree on both totals and the result string.

## Grades

| Row (rank) | Verdict on card | Grade |
|---|---|---|
| 1. MSG 100 balls Over 161.5 | `LEAN` (rank 1) | **WIN** (181) |
| 2. MSG 100 balls Under 161.5 | `PASS` (rank 2) | **LOSS** (complement, not independent) |
| 3. MSG first 25 balls Under 39.5 | `PASS` (`UNORDERED PAIR`) | **LOSS** (41) |
| 4. MSG first 25 balls Over 39.5 | `PASS` (`UNORDERED PAIR`) | **WIN** (complement, not independent) |
| Winner lean: Manchester Super Giants | `LEAN` | **WRONG** |

`calibration_eligible = FALSE` on all four rows: one `LEAN` and three `PASS`, so **no selection was made** and these grades measure directional and ranking accuracy only. **They are not a betting record, hit rate, ROI or evidence of an edge, and no price was used anywhere.** Only two pair-leader outcomes carry information — rank 1 correct, unordered pair resolved to the over.

## Findings carried into the manual

1. **The venue-baseline control worked prospectively, once, with the margin disclosed (§8.2).** The card named its mechanism before discussing the line: 138 at Lord's (2nd-lowest venue) versus a Headingley innings (2nd-highest) with an identical XI. MSG made 181. But the powerplay cleared by **1.5 runs**, and **both correct calls rest on the same adjustment applied to two positively correlated markets** — one observation with two readings. Recorded as a supported hypothesis with a visible mechanism; **not promoted to a rule**.
2. **The `UNORDERED PAIR` device earned its place.** Refusing to rank an n=2 team pattern against an n=2 venue pattern produced a record that teaches something on settlement, which is exactly what V6-019's "administrative rank" did not.
3. **Third consecutive wrong winner lean, and the defect is now nameable (§8.2, §10).** V6-019, V6-020 and V6-021 all leaned the wrong side. The first two rested on stale prices, which §1A has since forbidden; V6-021 used **no price at all**, so that fix held. What failed instead: a two-match record treated as form, and **an n=1 venue bat-first/chase-order signal**. **Control adopted: an n=1 venue bat-first/chase-order signal may not be cited in a winner case.** A high-scoring venue that supports an innings-total over simultaneously helps the chasing side; using one venue fact in two directions on the same card is a contradiction, not two arguments.

## Recordkeeping integrity

Settlement section appended to the log body **before** the ledger was written and before the new record was created — the index-before-settlement prohibition was observed. Post-write width assertion run: header 22 fields, **93 data rows, 0 rows off-width**. No original forecast was rewritten; the settlement and retrospective are appended with timestamps and reasons under the append-only rule.

## New record opened

V6-022 — Welsh Fire Women v Trent Rockets Women, The Hundred Women's 11th Match, Sophia Gardens, `TOSS / PRE-FIRST-BALL`, cutoff 2026-07-29T10:28:00Z. Four rows logged (`LEAN`, `LEAN`, `PASS`, `PASS`) plus a winner lean, all `PENDING`. **No live score from that match was retrieved or used**; the scheduled start had just passed while research was being completed, and that is disclosed on the card.

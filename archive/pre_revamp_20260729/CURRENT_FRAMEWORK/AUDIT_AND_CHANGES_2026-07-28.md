# Settlement audit and reference update — 2026-07-28

Status: **COMPLETED SETTLEMENT SWEEP — ALL PENDING RECORDS CLOSED**

Sweep run at 2026-07-28T17:01:09Z (2026-07-29 03:01 AEST). Scope: every record in `PREDICTION_RESULTS_LOG_v6.md` and every ledger row in `SPORTS_CALIBRATION_LEDGER_v3.csv` whose `result` field was `PENDING`.

## Scope and live check

Three records were pending: V6-018, V6-019 and V6-020. **Each was checked for live status before any settlement work**, per the instruction to skip anything still in progress. All three had passed their scheduled start by more than 72 hours and every primary feed returned a completed state, so none was skipped.

| Record | Event | Scheduled start (UTC) | Live check at sweep time | Outcome |
|---|---|---|---|---|
| V6-018 | FC Emmen v FC Twente (club friendly) | 2026-07-24T17:00Z | Complete — both clubs had published match reports | Settled |
| V6-019 | Birmingham Phoenix Men v Trent Rockets Men, The Hundred Match 4 | 2026-07-24T17:30Z | Complete — Cricbuzz match object `state: Complete`, `matchCompleteTimeGMT` Fri 24 Jul 20:22:46 | Settled |
| V6-020 | Cincinnati Reds at St. Louis Cardinals (MLB) | 2026-07-25T00:15Z | Complete — MLB `detailedState: Final`, `currentInning 9` = `scheduledInnings 9` | Settled |

## Verified finals

| Record | Verified final | Independently verified detail |
|---|---|---|
| V6-018 | FC Emmen 0-3 FC Twente | Half-time 0-2. Sam Lammers 6', 18', 85'. Both club match reports agree on score, scorer and minutes. |
| V6-019 | Birmingham Phoenix 214/4 (100 balls) beat Trent Rockets 204/7 (100 balls) by 10 runs | Toss: Trent Rockets, bowling. Phoenix extras 11 (b1, lb5, w5). Phoenix **Powerplay 1, balls 1-25: 54 runs, 0 wicket** — sourced from the scorecard's own phase line, not inferred from the innings total. Joe Clarke 68 (33) Player of the Match. |
| V6-020 | Cincinnati 4-2 St. Louis, nine innings, no extras | Reds 0 0 0 1 0 0 2 0 1 = 4 (11 H); Cardinals 0 0 0 0 2 0 0 0 0 = 2 (2 H). **Six total runs.** Lowder 5.0 IP / 2 ER / 4 K; May 6.0 IP / 1 ER / 8 K / 1 BB. Reds bullpen 4.0 shutout innings; Soriano L + BS. |

## Grading outcome

All twelve rows closed `NOT GRADED — CONTRACT UNVERIFIED` and `calibration_eligible = FALSE`. No hit rate, ROI, model promotion or calibration observation is created by this audit. Raw mappings are recorded as descriptive evidence only.

| Record | Rows | Raw mapping summary (descriptive only) |
|---|---|---|
| V6-018 | 4 | Twente winner would have won; BTTS Yes would have lost; Over 2.5 would have won on exactly three goals; corners **unsettleable** — no line supplied and no corner count published. |
| V6-019 | 4 | Under 141.5 misses by 72; Over 141.5 wins; Under 34.5 misses by 19.5; Over 34.5 wins. Informational winner lean (Trent Rockets) wrong. |
| V6-020 | 4 | Over 8.0 loses at six runs, no push; Cardinals ML loses; Reds +1.5 wins; Under 8.0 wins. Informational winner lean (St. Louis) wrong. |

## Data-quality defects found and fixed

| Defect | Evidence | Fix applied |
|---|---|---|
| Index recorded ahead of settlement | The open-event index already showed all three records `CLOSED — NOT GRADED` with final scores, but no settlement section existed in the log body and all twelve ledger rows still read `PENDING`. The log header requires the opposite order. | All three finals re-verified from scratch; every index score proved correct, so no score was amended. Settlement sections appended, ledger updated, and an **index-before-settlement prohibition** added to `combined_sports_doc_v4.md`. |
| Malformed CSV rows | The twelve pending rows parsed to 23 fields against a 22-field header, silently shifting `settled_utc`, `settlement_source` and `retrospective` by one column. Every other row in the file was correct. | The spurious empty column was removed from those twelve rows and the settlement fields written to their proper positions. A whole-file width audit now passes at 22 fields for all 85 data rows. A **post-write width assertion** was added to the manual. |

## Substantive findings carried into the manual

These are the analysis lessons, distinct from the recordkeeping fixes above. Each is now written into `combined_sports_doc_v4.md` — both in the 2026-07-28 settlement reference table and, where sport-specific, as a dated lesson inside the relevant §8 module so it is re-read at the mandatory pre-research gate.

1. **A written control that is not cited is not a control (V6-020, §8.1).** V6-020 repeated V6-010's failure exactly — same market, same 8.0 line, same "both starters are bad" thesis, five days apart — even though the V6-010 control ("preserve starter quality in every total projection") was already in the manual. The fix is a re-application check: restate the named control on the card and show how the current case differs.
2. **Venue-adjust recent-start samples (V6-020, §8.1).** An 8 ER start at Coors Field was carried into a run projection at face value. Name the park of each cited start or drop the sample. The card also had no bullpen input at all; the Reds' pen threw four shutout innings.
3. **A bowl-first toss is not a low-scoring signal (V6-019, §8.2).** It expresses a chasing preference. This drove both under branches on a card where the powerplay went 54/0 and the innings reached 214/4.
4. **An "administrative" rank is still a rank (V6-019, all sports).** Ranking the losing branch first and then disclaiming the ordering produces a hindsight-proof record that teaches nothing. Unseparable complementary pairs are now logged `UNORDERED`.
5. **Rotation notices do not erase a divisional class gap (V6-018, §8.3).** They widen uncertainty on margin, scorers and minutes, not on result direction.
6. **A market with no line and no published post-match statistic is unsettleable, not merely unattractive (V6-018, §8.3).** The corners row could not be mapped even after the final. Declaring this at cutoff is more useful than a generic pass.
7. **Informational winner leans must meet the formal-pick evidence bar (all sports, §10).** Wrong in both cases where issued this sweep, and both rested on a price snapshot the card itself had flagged as stale. "Not a wager" removes the ledger row, not the evidence standard.
8. **Rank 1 lost and rank 4 won on both ranked-pair cards.** Two of two — recorded as an observation with a visible mechanism (articulate narrative to the top slot, mechanical complement to the bottom), explicitly **not** promoted to a rule. The control added is procedural: write the case for the last-placed row before finalising any ranking.
9. **Contract capture, not contract verification, is now the binding constraint.** V6-016 through V6-020 are five consecutive records closed ungraded for want of a book, price and settlement rule. The verification control is working as designed; the gap is upstream. Step 3 must now surface an unresolvable contract in the delivered output *before* the research, so the user can supply the book and price rather than receive a structurally ungradeable card.

## Integrity conclusion

No record in `PREDICTION_RESULTS_LOG_v6.md` is open, live or pending. No ledger row has `result = PENDING`. All 85 ledger rows parse to the header's 22 fields. No original forecast was rewritten; every settlement, retrospective and correction is appended with its timestamp and reason under the append-only rule. The sweep produces no win/loss record and no change to any model's status: every affected row was `PASS` or `AVOID` except one `LEAN`, and that `LEAN` was conditional on a price that was never verified to exist.

## Addendum — price-independence directive and re-grade (same day, supersedes items 9 and 8 above)

After the sweep was written, the user directed: *refer to odds and prices only if it aids the analysis, otherwise don't rely on them.* Two conclusions above do not survive that directive or the fuller sample, and are withdrawn here.

**Withdrawn item 9 (contract capture).** The diagnosis was wrong. The problem was never that prices went uncaptured — it was that this manual had made a bookmaker contract a precondition for both reaching a view and grading an outcome. That is why five consecutive events were researched in detail and then declared unevaluable, and why the same MLB Over 8.0 thesis could fail twice (V6-010, V6-020) without either failure being counted. `combined_sports_doc_v4.md` §1A now governs: prices are optional supporting evidence; missing price never justifies a pass, a lower rank, or an ungraded event; completed events settle on the verified outcome under stated standard rules; and price-free grading measures direction and ranking only, never profitability.

**Withdrawn item 8 (the "two of two" slot claim).** All twenty rows across V6-016 to V6-020 have now been graded. Measured correctly — did the higher-ranked branch of each complementary pair win, since exactly one wins by construction — the result is **three of six**, not two of two. The original claim was generalised from the two records in front of me. It implied exploitable inversion; the truth is that the ordering showed no value and no systematic leak across a small sample. A new control follows: never generalise a slot or directional pattern without pulling every comparable settled record first.

**Research gap closed.** V6-016's first-25-ball score, absent since 24 July, is now sourced: Manchester Super Giants' mandatory powerplay was **26 runs for 1 wicket** (London Spirit's was 24/2 and must not be confused with it).

**Consequent correction to the cricket lesson.** V6-016 and V6-019 are the same competition and market pair analysed the same way, with unders correct at Lord's and wrong at Edgbaston. "Short-format under-bias" is therefore too blunt; the differentiator is venue and batting matchup. The genuine defect is that neither card carried a venue-specific scoring baseline, so both got the level wrong in opposite directions.

**Ledger effect.** Twenty rows moved from `NOT_GRADED_CONTRACT_UNVERIFIED` to `WIN` / `LOSS` / `UNSETTLEABLE`, with `formal_status` recording `RAW_GRADED_STANDARD_RULES_NO_PRICE` and the original status preserved in parentheses. `calibration_eligible` remains `FALSE` on every one of them, because each was a `PASS`, `LEAN` or `AVOID` — an abstention cannot be a calibration observation, and these grades must never be reported as a betting record or hit rate. Only one row remains genuinely ungradeable: V6-018-4 match corners, where no line was supplied and no corner count was ever published.

**Errors now countable rather than excused.** The V6-020 Over 8.0 miss is the most important: same market, same line, same reasoning as V6-010 five days earlier, against a control already written in this manual. Also countable: V6-019's two unders, V6-020's Cardinals moneyline, V6-018's BTTS Yes, and both informational winner leans — the latter two resting on a price snapshot the cards had themselves flagged as unreliable, which §1A now forbids as a basis for any view.

## Sources

- V6-018: [FC Emmen official match report](https://fcemmen.nl/fc-emmen-onderuit-tegen-effectief-fc-twente/) and [FC Twente official match report](https://fctwente.nl/nieuws/oefenzege-op-fc-emmen), both opened 2026-07-28.
- V6-019: [Cricbuzz match object](https://www.cricbuzz.com/live-cricket-scores/144695/brm-vs-tre-4th-match-the-hundred-mens-competition-2026) (completion state, status, toss) and [ESPNcricinfo full scorecard](https://www.espncricinfo.com/series/the-hundred-men-s-competition-2026-1521176/birmingham-phoenix-men-vs-trent-rockets-men-4th-match-1521234/full-scorecard) via the validated text proxy (both innings totals, extras, explicit 25-ball powerplay phase line), both opened 2026-07-28.
- V6-020: [Official MLB linescore, game 823031](https://statsapi.mlb.com/api/v1/game/823031/linescore), [official boxscore](https://statsapi.mlb.com/api/v1/game/823031/boxscore) and the [2026-07-24 schedule feed](https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-07-24&hydrate=linescore,decisions), all opened 2026-07-28T17:01Z.

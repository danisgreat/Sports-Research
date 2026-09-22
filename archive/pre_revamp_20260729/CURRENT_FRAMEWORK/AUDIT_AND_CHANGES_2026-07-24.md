# Settlement audit and reference update — 2026-07-24

Status: **COMPLETED SETTLEMENT CLEANUP**

## Scope

This audit checked every current `PENDING` row in the active calibration ledger and the matching open-event index entry. The only current record was V6-016: London Spirit Men v Manchester Super Giants Men, Match 3.

## Final-state review

| Record group | Final-state source check | Status | Treatment |
|---|---|---|---|
| V6-016 | Cricbuzz's completed scorecard records Manchester Super Giants 138/9 from 100 balls and London Spirit 131/6 from 100 balls; independent match reporting records a seven-run MSG win. | Final | Closed in the Markdown log and CSV ledger as `NOT GRADED — CONTRACT UNVERIFIED`. |

The event was complete, with both innings using the full 100-ball allocation. It was not live, postponed, abandoned, or shortened when checked. No active ledger row remains `PENDING`; historical `PENDING` labels inside frozen, append-only forecast cards remain part of their original record.

## Outcome and research review

| Item | What final evidence showed | Assessment |
|---|---|---|
| Full-innings raw total | MSG made 138/9 from 100 balls. If the unrecorded “Points” label meant raw completed-innings runs, Under 147.5 would map to a win and Over to a loss. | Descriptive only. The original rows were `PASS`, with no bookmaker, price, extras rule, interruption rule, or validated contract retained. They are not graded as bets or model results. |
| First-25-ball totals | The original 37.5 labels were not tied to a captured sportsbook contract, and no authoritative raw 25-ball aggregate was retained for settlement. | Neither branch can be inferred from the full innings. Both are closed `NOT GRADED — CONTRACT UNVERIFIED`. |
| Why the final innings finished below 147.5 raw runs | Seifert made 67 from 45 balls and MSG reached 105/2 after 67 balls, but Spirit then took seven wickets for 33 runs. Livingstone returned 2/14 from 20 balls, with Milne, Zampa and Willey also taking wickets. | The original full-innings under route was plausible, but one realized mechanism is not evidence of predictive quality or price value. |
| Why the result remained close | Livingstone made 69 from 40 balls in a 131/6 chase, but Atkinson and Baker took late wickets and MSG won by seven. | This reinforces that a side or total conclusion should not be inferred from one phase, one player, or a raw final alone. |

## Persistent reference update

| Sport / market | Evidence-specific reference | Control retained in active manual |
|---|---|---|
| Hundred first-X-ball and first-innings totals | The raw 100-ball innings was final at 138/9, while the book's “Points” definition and the raw first-25-ball settlement data were missing. | At settlement, store an independently sourced raw phase/innings score alongside the original sportsbook metric, exact ball boundary, extras, interruption/shortened-innings, void and price terms. If either side is absent, close `NOT GRADED — CONTRACT UNVERIFIED`; never infer a phase market from the full innings. |

## Integrity conclusion

V6-016 is fully closed as a completed event, not a live pending log. It provides no validated cricket model result, price value, ROI, hit-rate, or calibration evidence: every original row was a `PASS`, all exact contract terms were missing, and no numeric probability was issued.

Sources: [Cricbuzz completed scorecard](https://www.cricbuzz.com/live-cricket-scorecard/144684/ldn-vs-msg-3rd-match-the-hundred-mens-competition-2026), [Cricbuzz match report](https://www.cricbuzz.com/cricket-news/139640/manchester-super-giants-edge-past-london-spirit-despite-livingstone-special), and [Cricket Australia match report](https://www.cricket.com.au/news/4544337/london-spirit-v-manchester-super-giants-hundred-mens-womens-2026-match-report-scores-highlights-livingstone-zampa-lanning-lords), checked 2026-07-24.

# Settlement audit and reference update — 2026-07-25

Status: **COMPLETED SETTLEMENT CLEANUP**

## Scope and data-quality check

This audit checked the active open-event index and every ledger row where `result = PENDING`. V6-017, KT Wiz at Lotte Giants, was the sole active pending event. V6-016 is already closed: its historical `formal_status` contains `CONTRACT_UNVERIFIED`, but its `result` is `NOT_GRADED_CONTRACT_UNVERIFIED`, so it is not pending.

| Check | Evidence | Conclusion |
|---|---|---|
| Active-event grain | Four V6-017 rows share one event-level parent record and one frozen live cutoff. | Correct one-event/four-contract structure; no duplicate event row. |
| Current-pending predicate | `result = PENDING` identified V6-017 only; substring matching `formal_status` would also surface closed V6-016 rows. | Use the `result` field plus the open-event index for operational pending status. |
| Final state | Official KBO game centre shows KT 5, Lotte 4 at Sajik, with Logan Allen winning, Park Yeong-hyun saving and Na Gyun-an losing. | Complete, final, and eligible for closure. |
| Market-contract completeness | No bookmaker, odds, timestamped live availability, listed-pitcher condition, extra-innings treatment, shortened-game rule or void rule was retained. | Raw outcomes may be described, but no row may receive a formal win/loss grade. |

## Final result and retrospective

| Original contract | Standard raw mapping from the verified 5-4 final | Formal status | What the game showed |
|---|---|---|---|
| KT Wiz moneyline | KT win | `NOT GRADED — CONTRACT UNVERIFIED` | KT won by one, so the stronger-standings side did win; the original row was nevertheless a `PASS`. |
| Lotte Giants +1.5 | Lotte cover by 1.5 | `NOT GRADED — CONTRACT UNVERIFIED` | The one-run margin makes this overlap with KT moneyline under standard settlement; the contracts were never opposites. |
| Under 9.5 runs | Under, total 9 | `NOT GRADED — CONTRACT UNVERIFIED` | The total landed one run below the threshold, but the 0-0 first-inning cutoff was not a valid predictive total sample. |
| Over 9.5 runs | Over loss, total 9 | `NOT GRADED — CONTRACT UNVERIFIED` | All nine runs were scored by the end of the seventh; an early scoreless inning did not establish a low-scoring game state. |

The game detail is descriptive rather than evaluative: Logan Allen allowed two runs in six innings; Na Gyun-an allowed five in 5 2/3; Lotte's Han Dong-hui hit a two-run homer in the seventh to reduce the gap to one; Sugimoto Koki and Park Yeong-hyun then closed the final two innings. These events occurred after the frozen live snapshot and cannot be inserted into the original `PASS` rationale or used as model validation.

## Persistent reference updates

| Area | Reference retained | Why it matters |
|---|---|---|
| Full-game settlement | Store final score, innings/extra-innings status and a labelled standard raw mapping; only formal-grade with the original sportsbook contract. | Avoids turning unpriced or undefined live displays into hindsight wins/losses. |
| KBO source hierarchy | Official KBO game centre controls the final. The MyKBO detailed scorecard is useful only as explicitly unofficial descriptive context when official detail cannot be retrieved. | Keeps result authority separate from secondary player/inning narrative. |
| Ledger status checks | Determine active work from `result = PENDING` and the open-event index, not broad text matching against `formal_status`. | Prevents closed `CONTRACT_UNVERIFIED` rows from being re-opened by a cleanup query. |

## Integrity conclusion

V6-017 is closed as `NOT GRADED — CONTRACT UNVERIFIED`. No active ledger row remains `PENDING`. The audit creates no KBO model result, hit-rate, ROI, calibration observation or upgraded verdict: every V6-017 row was originally a `PASS` and no book-specific contract was available.

Sources: [Official KBO game centre](https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx?gameDate=20260724&gameId=20260724KTLOT0), checked 2026-07-24T16:41:42Z; [MyKBO Stats final scorecard](https://mykbostats.com/games/13727-KT-vs-Lotte-20260724), checked 2026-07-24 and used for descriptive detail only because it states it is not affiliated with KBO.

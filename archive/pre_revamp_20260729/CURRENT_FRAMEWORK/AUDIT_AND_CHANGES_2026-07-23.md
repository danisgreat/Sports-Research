# Settlement audit and reference update — 2026-07-23

Status: **COMPLETED SETTLEMENT CLEANUP**

## Scope

This audit reviews every currently pending row in the active calibration ledger and its matching open-event index entry as checked at 2026-07-22T17:28:30Z. The only pending record was V6-013, Tampa Bay Rays at Toronto Blue Jays.

## Final-state review

| Record group | Final-state source check | Status | Treatment |
|---|---|---|---|
| V6-013 | Official MLB game 822787 feed listed `Final`, with Tampa Bay 12 and Toronto 2 after nine innings. | Final | Fully settled in the Markdown log and CSV ledger under the recorded full-game convention. |

The event was not live, postponed, abandoned, or shortened at the check. No current ledger row remains `PENDING`; historical `PENDING` labels inside original append-only cards are preserved as part of their frozen pre-settlement record.

## Outcome and research review

| Item | What the final evidence showed | Assessment |
|---|---|---|
| Rays +1.5 and winner leans | Tampa Bay won 12-2. Rasmussen allowed two runs in five innings, while the Rays recorded 21 hits. | Directionally right, but the 10-run margin was not forecast. The two outcomes are correlated and not independent evidence. |
| Under 7.5 `PASS` | The game produced 14 runs. Gausman allowed five runs (four earned) in 3 1/3 innings; Tampa Bay then added runs against Toronto relievers. | The low-total scenario failed. Its `PASS` status was appropriately non-actionable, not a losing recommendation. |
| Over 7.5 `PASS` | The game produced 14 runs. Fortes and Díaz each hit a three-run home run; DeLuca drove in three. | The realized direction was over, but a comparison-only `PASS` is not a forecasting success. |
| Toronto +1.5 `AVOID` | Toronto lost by 10. | The avoided branch lost. It is not the exact opposite of Rays +1.5 and must not be counted as independent confirmation. |

## Persistent reference update

| Sport / market | Evidence-specific reference | Control retained in active manual |
|---|---|---|
| MLB pregame total at 7.5 or lower | One strong starter and a recent scoring slump did not prevent a 14-run game once Gausman exited early and Tampa Bay's lineup generated 21 hits. | Record starter-exit plus opponent-lineup/bullpen branches. Keep conflicting low-total evidence at `PASS` without a price, complete bullpen inputs, and a validated projection. |

## Integrity conclusion

The record is now complete, but it does not establish an MLB model, expected value, ROI, hit rate, or calibration. The exact bookmaker and prices were not recorded, and the framework contains no validated quantitative probability for this card.

---

## Supplement: V6-014 and V6-015 settlement review — 2026-07-23T17:32:23Z

| Record group | Official final | Result review | Learning disposition |
|---|---|---|---|
| V6-014 — Orioles at Red Sox, Game 1 | Boston 6, Baltimore 3 (total 9) | Boston ML `LEAN` won; Over 9.5 `PASS` and Baltimore +1.5 `PASS` lost; Under 9.5 `AVOID` won. | The side direction was right; the narrow total landing does not promote the avoided under or create a new rule. |
| V6-015 — Athletics at Diamondbacks | Arizona 15, Athletics 5 (total 20) | Arizona ML `LEAN` and Over 8.5 `PASS` won; Athletics +1.5 `PASS` and Under 8.5 `AVOID` lost. | The short-start/bullpen-risk branch was relevant, but a single 20-run outcome does not validate a total model. |

The results are now settled in the active log and calibration ledger using official MLB game recaps. No new baseball parameter was added: retained controls are complete starter, lineup, bullpen, and price/contract branches; `PASS` and `AVOID` outcomes are not counted as active-pick successes.

## Reference addition: Hundred first-X-ball market control — 2026-07-23T17:38:01Z

| Sport / market | Evidence-specific issue | Control added to active manual |
|---|---|---|
| Cricket — first 25 balls and first 100 balls | The supplied labels used “Points” without a sportsbook, price, or settlement terms. Official competition rules establish the 100-ball innings and 25-ball powerplay but do not define the book's market metric. | Freeze the book-defined metric, exact ball boundary, extras and shortened-innings treatment. Treat powerplay and full-innings totals as correlated but distinct; do not infer one market from the other. |

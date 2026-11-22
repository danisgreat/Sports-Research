# Demonstrating predictive advantage (EVAL-ONECHAT-v2 / ONE-CHAT-v2 / CR-2026.11.16-R3)

Owner order, 16 November 2026: the demonstrated predictive advantage must be fully implemented. Registered before any game of the cohort; it replaces [EVALUATION_PLAN_v25.0](EVALUATION_PLAN_v25.0.md), under which no game was ever scored. The forecast identity, the comparator and the card format are unchanged.

## What "demonstrated" means here

A predictive advantage cannot be built into code. It exists only if the cards' numbers beat a stated comparator on games whose results were unknown when the numbers were fixed. This plan makes that claim testable, checkable by anyone with the repository, and decidable as soon as the evidence is strong enough, without the error rate rising when the owner looks often.

- **Forecast:** the probabilities in each card's `ONECHAT_V1` PICKS table, exactly as written.
- **Comparator:** a constant 0.5 on every supplied line that has a line value (handicaps, totals, team totals, period and corner lines). It scores 0.25.
- **Per game:** d = 0.25 − (mean Brier score of the card's priced, decisive rows on those lines). d > 0 means the card beat 0.5. On a whole-number line the probability used is the side's share given no push (p ÷ the sum of the line's two sides), the framework's W/(W+L) rule.
- **Claim:** the mean of d over games is above zero.

## Which games count

All of these must hold, and every one is checked by `python -m ml one-chat score`:

1. **Admitted block.** The intake admitted the card: complete, coherent and sporting fields only. Every observed fact and the not-started check fall between `research_start_at` and `research_end_at`.
2. **Every supplied line priced.** An `UNPRICED` supplied line keeps the game out.
3. **Sealed before play, timed by GitHub.** The owner ran `python -m ml one-chat seal` on the card file. That commits the file and pushes it to `origin/main`, and the push is timed from GitHub's own server record (`PUSH_RECEIPTS.csv`, mirrored with `ml one-chat receipts`). The first push carrying the exact block must be at or before the official first play. The research must also have ended before the seal (otherwise the card is CLOCK_INCONSISTENT). A card sealed only on the owner's clock (SEALED_PRE_START_CLIENT), sealed after play, or never sealed is reported and does not count.
4. **Research before play, outcome unseen.** `research_start_at`, the not-started check, `research_end_at` and every fact's `observed_at` are at or before the official first play, and `outcome_exposure` is NONE.
5. **Settled from a saved page.** Every row has WIN, LOSS, PUSH or VOID, an `event_id` (the competition's native match identity) and a saved result capture whose SHA-256 is re-computed at scoring. At least one priced lined row is decisive.
6. **One game, one card.** Cards that share a game identity or an `event_id`, across every intake, are one game. The card sealed first is the card of record.
7. **Committed inputs.** The intakes (checked against their MANIFEST.csv), the outcome files and any frozen cohort must be committed and unchanged. Otherwise the run reports NOT_ASSESSABLE and decides nothing.

## The decision: an anytime-valid test

Games enter one sequence ordered by **scheduled start**, which is fixed before any result. The sequence stops at the first sealed, fully priced card whose game is not yet settled, so a slow settlement can never reorder games after their results are known.

The test is a betting e-process for "mean d ≤ 0". Wealth starts at 1; for each game it is multiplied by 1 + λ·d. λ is chosen only from earlier games (a predictable plug-in, shrunk toward no bet for the first games). It never exceeds 0.75 of the largest bet that keeps wealth positive at the worst possible d (−0.75). If the cards have no advantage, wealth is a nonnegative supermartingale. By Ville's inequality, the chance it ever reaches 20 is at most 5%, however often it is looked at.

| Verdict | Rule |
|---|---|
| **DEMONSTRATED** | The first time wealth reaches 20 while the running mean d is at least 0.01, within the first 400 games of the sequence. The verdict is then fixed. |
| **NOT_YET_DEMONSTRATED** | Fewer than 400 games and no crossing yet. |
| **NOT_DEMONSTRATED** | 400 games without a crossing. |
| **NOT_ASSESSABLE** | A custody check failed in this run. |

Every run also prints the 95% anytime-valid lower bound on mean d: the largest m whose own test ("mean d ≤ m") has been rejected.

**Error and power, by simulation before registration** (`ml/one_chat.py` constants, 400 to 100 sequences of 500 games each):

| True situation | Crossed | Median games to cross |
|---|---|---|
| Mean d exactly zero (null) | 5 of 400 (1.3%) | — |
| Coin-flip results, card states 55–75% | 0 of 200 | — |
| Calibrated card, favoured sides 55–65% | 59% within 400 games | 327 |
| Calibrated card, favoured sides 58–72% | 99% within 400 games | 176 |
| Calibrated card, favoured sides 62–78% | 100% within 400 games | 92 |

A card that is right but only modestly confident (about 60%) has an edge over a coin of about 0.01 per game, and showing that reliably takes hundreds of games. That is a property of the evidence, not of the test.

**Per sport.** The same test runs on each sport's games, with threshold 20 × 11 = 220 because there are eleven sport sections. A sport-level claim needs that higher bar.

## Secondary reports (never the verdict)

- The first 100 games of the sequence are frozen once (COHORT.csv with COHORT_RECEIPT.csv: hash and count). Later runs must reuse them with `--cohort`, and a cohort that is not the receipted 100 is refused. Their fixed-sample t interval of mean Brier − 0.25 is reported against the v25 criterion (−0.01, interval below zero). It assumes independent games and is descriptive.
- Calibration by band and slope, Rank 1 and Rank 2 results, family and sport tables, the priced share, and the six registered hypothesis flags (H-NODIR, H-BAND, H-AVAIL-CHAT, H-OWN-EVIDENCE, H-SPORT, H-PERIOD), flagged against unflagged.
- The card against a frozen league base rate where one exists (`--baseline`).

## Historical context (not evidence for the claim)

The same test was run over the 685 settled cards already in the repository ([historical_evidence](../verification/framework_change_2026-11-16-3/historical_evidence/HISTORICAL_EVIDENCE.csv)).

- **All 280 cards with a stated probability:** the e-value reached 59 at card 198; lower bound +0.005, mean d +0.020.
- **The 31 chat-research cards on supplied lines (P-639 onward):** e-value 1.0 and mean d +0.0015, so no evidence of an advantage.

The first figure does not demonstrate anything:
- the cards were never sealed;
- they span several policies;
- their rows do not record which lines the owner supplied and which the analyst chose;
- the analysis was chosen after the results were known.

It is a reason to run the prospective test, not a substitute for it.

## Limits stated in advance

- GitHub's push time proves when the file reached GitHub, not when the chat finished. A card sealed after the start of play never counts, whatever its own clocks say.
- The test assumes each game's advantage has mean at most zero given earlier games under the null. Shared days, teams and competitions do not break it, but a change in the cards' quality over time is measured as an average.
- Beating 0.5 on a supplied line is measured without any reference to a market or price (hard rule). It says the card's numbers carried information about the result of that line.
- Changing any registered constant (α 0.05, 0.01 practical mean, 400 games, bet cap 0.75, prior variance 0.0625, the comparator, the sequence order) is a new registration and restarts the sequence.

## Commands

```text
python -m ml one-chat seal --card "<card file>" [...]            before play: commit, push, record GitHub's time
python -m ml one-chat intake --drop "<owner drop>" --out research/one_chat/intake/<YYYY-MM-DD-n>
python -m ml one-chat receipts                                   refresh GitHub push times (run before scoring)
python -m ml one-chat score --intake research/one_chat/intake/* --outcomes research/verification/<package>/OUTCOMES.csv [...] --out research/one_chat/scores/<YYYY-MM-DD-n> [--cohort <first frozen>/COHORT.csv]
```

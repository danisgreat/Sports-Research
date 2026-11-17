# Prospective evidence: ONE-CHAT-v3 / SCV-v20 (v29.0)

Registration takes effect at its first independently verified GitHub publication on main, under the owner's instruction to implement the repository review accurately. Replaces v28.0 (and v27.0, v26.0) before any real request or card was registered or sealed: `forecast-seals` held no request index or seal on 18 November 2026. v29.0 keeps every v28.0 statistical constant and adds the settlement deadline, the first-play exclusion and the worst-case sensitivity below, so that several chats with up to ten games each can run without one unsettleable game stalling the sequence. v28.0 changes only two statistical constants, after a review showed the v27.0 constants left a well-calibrated card a poor chance of being shown within 400 games; the custody rules are unchanged. Original registrations and historical forecasts remain unchanged. Every seal binds this plan's exact hash and published commit; a forecast cannot precede its evaluation registration. This registers an evaluation, not a successful result.

## Population and immutable inputs

The forecast is the original card's probabilities on the owner's supplied contracts, conditional on a decisive result where a push is possible. The primary comparator is exactly 0.5 on supplied two-way lined contracts. A league sporting-data-only comparator is reported on the identical rows only where its probability, recipe and provenance were frozen in the original request's CONTRACTS.csv. Missing comparators remain missing.

Before research, register the unchanged owner request, namespaced native event identity, official schedule URL, UTC-aware start, and every contract's label, family, side, line, period, endpoint, action, unit and exact original request excerpt. Publication on `forecast-seals` freezes the request independently of the code branch. A request change needs a new key; retain and report the previous request. Unpriced, unsealed, late, outcome-exposed, unresolved and excluded requests remain in the census.

Seal the original ONECHAT_V1 card before first play. Its exact Git blob, original request, contract definitions and metadata must coexist in a commit whose publication time is independently fetched from GitHub's activity API. A client clock or editable receipt mirror is insufficient. Card numbers and research facts are replayed from that blob; committing a changed derivative and regenerating hashes never changes the forecast of record. Every registered request and sealed game must be accounted for in the supplied intake set.

Where no native competition ID is known before research, the request's event identity may be the derived `REQ:<sport>:<competition>:<home>:<away>:<UTC start>` written by `ml one-chat prepare`; settlement uses the same identity. Two chats must not be given the same game; if they are, game and event identity make it count once.

Results require the frozen native event identity, terminal grades for every row, saved result capture and hash, plus a separately identified official first-play capture, hash and exact excerpt. These checks establish identity and byte custody; source truth and interpretation still require the documented settlement review. Hashes alone do not verify sporting truth. An earlier unresolved candidate holds back later games in scheduled-start order, until its settlement deadline.

**Settlement deadline (v29.0).** A row that is still not terminal (WIN, LOSS, PUSH or VOID) 14 days after the game's registered scheduled start is dropped, by rule and without judgement. The game is then scored on its remaining decisive supplied lines, or recorded SETTLEMENT_UNATTAINABLE if none remain, and it no longer holds back later games. Every score run states its `as_of` time. As a sensitivity, never the verdict, each run also reports the same test with every dropped line counted as lost by the card's favoured side (`worst_case_verdict`, `worst_case_e_value`, `worst_case_lower_bound_95`), so withholding settlement can never help the card.

**Evidence problems never stop the run (v29.0).** A game whose official first play cannot be verified from a saved capture and exact excerpt is excluded (FIRST_PLAY_UNVERIFIED) and does not hold back later games. A missing or changed result capture, a missing event identity or an incomplete cancellation record is a custody problem: the run completes, reports it and decides nothing (NOT_ASSESSABLE) until it is repaired.

**The scored record is the sealed copy (v29.0).** Intake for scoring is built from the first sealed version of every sealed card (`ml one-chat intake --from-seals`), never from a chat's later copy of its mini. A card changed after it was sealed is refused when re-sealed; the first sealed version stays the forecast of record. Sealing works card by card: an incomplete, changed or unregistered card in a mini is refused on its own and the mini's other new cards are still sealed. One event counts once across all intakes and aliases. Doubleheaders have distinct native identities and UTC starts.

## Statistical target and decision

For each eligible game, d = 0.25 minus its mean decisive-row Brier score. Its range is [-0.75, 0.25]. The target at game n is the average conditional expected advantage through n, allowing different conditional means over time. The card protocol and selection policy remain frozen.

The lower confidence sequence uses the predictable empirical-Bernstein construction in Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences*, Theorem 4 and Appendix A.8: https://arxiv.org/abs/1810.08240. For X=d+0.75, use a predictable running forecast of X shrunk with one pseudo-observation at 0.75. The variance proxy is the cumulative squared prediction error. Mix equally over the fixed lambdas (0.5, 0.7, 0.9), with psi(lambda)=-log(1-lambda)-lambda. Invert the current mixture, not its historical maximum, to bound the current average conditional mean. No constant-mean assumption or running intersection of bounds for different means is imposed.

- Alpha: 0.05. Practical observed mean threshold: 0.01. Decision horizon: 600 games.
- `DEMONSTRATED`: a registered prefix within 600 games crosses mixture evidence 20 while its observed mean d is at least 0.01. Freeze that assessed prefix and report its own mean and lower bound. This is evidence on that prefix; it does not promise persistent future performance.
- `NOT_YET_DEMONSTRATED`: the sequence has fewer than 600 games and has not crossed.
- `NOT_DEMONSTRATED`: no crossing in the first 600 games.
- `NOT_ASSESSABLE`: any input, original-request, custody, complete-sequence or identity check failed.

Continue reporting the current mean and current lower bound separately after a crossing. A past positive bound is never reused for a deteriorating current average. Per-sport inference uses alpha/11 on the fixed eleven sport sections. A new sport section or any changed statistical constant requires a new registration. Simulations validate implementation; they are not evidence of real predictive success.

## Error rate and power, registered with the constants

`python -m ml one-chat power --out <folder>` runs the registered decision on simulated sequences with fixed seeds; the registration run is [POWER.csv](../verification/framework_change_2026-11-17-1/power/POWER.csv). Each simulated game has two supplied lines; "calibrated" means the card's stated probability on its favoured side is the true one, drawn from the band shown.

| Simulated cards | Runs | Shown within 400 games | Shown within 600 games | Median game of the crossing |
|---|---:|---:|---:|---:|
| Mean advantage exactly zero (null) | 400 | 0 | 0 | — |
| Coin-flip results; card states 55–75% | 200 | 0 | 0 | — |
| Calibrated, favoured sides 55–65% | 200 | 23 | 92 (46%) | 462 |
| Calibrated, favoured sides 58–72% | 200 | 171 | 198 (99%) | 289 |
| Calibrated, favoured sides 62–78% | 200 | 200 | 200 (100%) | 156 |

Under the v27.0 constants (eight lambdas, 400 games) the same review measured about 72% for the 58–72% card within 400 games and about 4% for the 55–65% card. A card whose favoured sides are right only about 60% of the time has an edge over 0.5 of about 0.01 per game; showing that reliably takes several hundred games under any valid test.

The first 100 eligible games are a secondary descriptive checkpoint, available immediately without any week/calendar minimum. Freeze exactly the actual first 100 with a hash receipt; later scoring verifies membership and reuses that file. Its t interval is descriptive and assumes independent games. It is not the sequential verdict.

Report calibration, log loss, Brier, coverage/abstention, contract family, sport, ranking and missing-comparator counts. Historical hypothesis flags remain exploratory and do not change a card. No model, recalibration, rule or hypothesis is promoted merely because a subgroup appears favourable.

## Historical evidence is retained

All 685 historical cards are used by CARD-TRAIN-v1 and itemised by `ml.evidence_status`. Their original cohorts and probabilities remain intact. Historical studies with positive comparisons are reported as such. New validators applied after results cannot establish that newer rules, requested lines or numbers were frozen before those results. Such records cannot be inserted into this new registration by relabelling them. Recoverable original custody may support a separately declared historical audit, with its original method and limits.

No genuine request or game had been registered or sealed under v27.0, v28.0 or this plan at release. Current prospective status: `NOT_YET_DEMONSTRATED`.

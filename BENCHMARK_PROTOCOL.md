# Settlement benchmarks and the market firewall (BENCH-v1)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-03, REV-04 and REV-20 and the owner's decision D1 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md): options (a) and (b) are adopted, option (c) is not. A benchmark is a probability that the research never saw, against which a card is scored after the event.

## 1. What is adopted and what is not

| Option | Status | Rule |
|---|---|---|
| (a) Line-implied 0.5 | **Adopted** | A supplied two-way spread or total, offered on both sides, sits where the market splits probability about evenly. The benchmark is therefore 0.5 on the decisive outcomes of a supplied two-way line. It is a property of the line, not a read of any price, and is written into every eligible picks row (`line_implied_p`) |
| (b) No-vig close | **Adopted, post-settlement only** | A hand-entered probability for the exact contract, entered after the verified final. It is outside the reading gate and outside card learning |
| (c) Market line as the prior | **Not adopted** | MARKET_BLIND stays: no odds, line movement, tips, previews or prediction markets enter research, the reference, the adjustments or any card |
| External non-market models | **Adopted, post-settlement** | Squiggle (AFL), ClubElo (soccer), Tennis Abstract Elo (tennis) as scored comparators |

CURRENT_RULES section 5a (the decision-lab firewall) is unchanged. Staking, CLV and in-play automation stay out of this repository.

## 2. The line-implied benchmark

`line_implied_p` is `0.5` on every picks row whose line is `SUPPLIED` and whose family is a two-way family (handicap, total, team total, period). It is blank on moneylines (no price, so no implied value), on `ANALYST_DERIVED` lines (an analyst-chosen line carries no information about the market) and on every non-two-way row. The linter enforces this. `python -m ml ledger score` reports "final minus line-implied 0.5": a card that cannot beat a coin on lines the market has already balanced has not shown skill on those lines.

## 3. The no-vig close (hand entry after the final)

A benchmarks file has the exact columns `local_key,label,benchmark_id,p,method,source_url,retrieved_at,final_at`.

- `benchmark_id`: `NOVIG_CLOSE`, `SQUIGGLE`, `CLUBELO`, `TENNIS_ABSTRACT_ELO` or `EXTERNAL_OTHER`.
- `p`: a probability for the card row's contract, strictly between 0 and 1. **No price, odds, line or movement column is accepted**; the loader refuses any other column name.
- `method` (for `NOVIG_CLOSE`): `MULTIPLICATIVE`, `POWER`, `SHIN` or `OO_EPC`. The de-vig is done by the person entering it, outside the repository, and only the resulting probability is stored.
- `retrieved_at` must be at or after `final_at` (the verified final), both with a UTC offset. A benchmark is entered after the event, never before; a row captured earlier is refused.
- Raw prices stay out of the repository (a local, git-excluded capture, as the decision lab does).

No prompt reads a benchmark before its card is settled. No rule, rank, width, adjustment size or learning disposition may cite one: it is a scoring reference, like a final score.

## 4. Reading it

The paired Brier of final p against `NOVIG_CLOSE` is the hardest honest test of the framework. In the repository's own firewalled study the fitted EPL model scored 0.2901 against 0.2795 for the de-vigged Pinnacle close (difference +0.0129, week-block interval 0.0079 to 0.0180), and the literature agrees that bookmaker odds are among the best public forecasters. A card that cannot get within a few thousandths of the close has no basis for confidence on a supplied line. A card that beats it on information rows is a result worth studying before it is believed.

## 5. Procedure

Prompt 3 settles the card, writes `RESULTS.csv` and `ACTUALS.csv` and, **only if the owner supplies them**, a benchmarks file; it never searches for prices. Prompt 6 runs `ledger score` monthly, reports each comparison with its interval and records the gaps. A missing benchmark is a missing row in the table, never a reason to delay settlement.

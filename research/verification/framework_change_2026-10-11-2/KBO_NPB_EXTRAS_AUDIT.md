# KBO and NPB extras audit, 2026-10-11

Prompt 7 §1 asks that, for the KBO extras audit, "missing flags versus genuine zeros" be told apart before any rate is estimated. This is that audit. Base revision `abb3e98d7ab2dfc3bd33bcdf42b4a3bf3a11a7d4`. Read-only: no archive cell was changed. The yearly files were copied to a scratch folder outside the repository and counted with `awk` (Windows line endings removed).

## 1. Question

LEAGUE_PROFILES (`LP-2026.10.09-v1`) gave an extra-innings share of **0.1% for the KBO** and **0.0% for the NPB**, beside tie shares of 2.1% and 2.8%. A game that ends tied has been played to the league's extras limit, so a tie share above the extras share is a contradiction. Is the extras share a measurement?

## 2. Structure and reproduction

| File set | Rows | Columns | Fields per row | Quoted fields |
|---|---:|---:|---|---:|
| KBO 2023 / 2024 / 2025 | 898 / 872 / 873 | 45 | 45 on every row | none |
| NPB 2023 / 2024 / 2025 | 912 / 909 / 906 | 46 | 46 on every row | none |

Physical lines equal logical records (no embedded newline or comma). Filtering `Season Phase` and `Game Type` = Regular Season and `Game Status` = a final (`Official Final` for the KBO, `Completed` for the NPB) reproduces the published rows exactly:

| League | n | Mean home / away / total | Total SD / margin SD | Corr | Ties |
|---|---:|---|---|---:|---:|
| KBO 2023-25 | 2,182 | 4.88 / 4.89 / 9.77 | 4.93 / 4.79 | 0.028 | 46 (2.1%) |
| NPB 2023-25 | 2,576 | 3.41 / 3.29 / 6.71 | 3.80 / 3.76 | 0.011 | 72 (2.8%) |

The profile's home-win and one-run shares reproduce when ties are excluded from the denominator (KBO 51.5% and 23.8%; NPB 54.2% and 33.7%). So the builder is understood, and the only quantity that cannot be reproduced as a measurement is the extras share.

## 3. The extras columns

| Check | KBO 2023 / 2024 / 2025 | NPB 2023 / 2024 / 2025 |
|---|---|---|
| Finals (all stages) | 802 / 789 / 779 | 879 / 880 / 878 |
| `Extra Innings` marked yes among finals | 1 / 1 / 1 | 0 / 0 / 0 |
| `Innings Played` above 9 among finals | 1 / 1 / 1 | 0 / 0 / 0 |
| Final scores tied (all stages) | 19 / 17 / 26 | 19 / 30 / 23 |
| Line-score cells populated | 75 / 22 / 28 | 0 / 0 / 0 |
| Winning-pitcher cells populated | 75 / 19 / 23 | 0 / 0 / 0 |
| `Game Summary` populated | 898 / 872 / 873 | 912 / 909 / 906 |
| Summary text containing "extra", "10th", "11th", "12th" or the number of innings | 0 / 0 / 0 | 0 / 0 / 0 |

- The three KBO games marked as extras are 2023-10-01 KIA (5–6, 10 innings, regular season), 2024-10-09 LG (5–6, 11 innings, wild card) and 2025-10-03 Hanwha (6–6, 11 innings, regular season, a tie). The 2023 and 2025 games are the two regular-season games behind the 0.09% (2 of 2,182).
- In NPB 2025 every one of the 906 rows reads `Innings Played` 9 and `Extra Innings` "No", **including the 28 cancelled games**; a cancelled game played no innings. That is a default fill, not a measurement.
- In KBO 2025 the 94 cancelled rows leave `Innings Played` blank, and 778 of 779 finals read 9. Tied finals across 2023–2025 are 62 (19 + 17 + 26, all stages); only the 2025 Hanwha game among them is marked.

## 4. Conclusion

1. **The flags are not measurements.** The KBO has 62 tied finals, of which one is marked as extras (the other two marked games were decided); the NPB has 72 ties and none marked. A game tied after nine innings goes to extras unless it was called by weather or a time limit, and the status column cannot separate those cases (it reads only `Official Final` or `Completed`). Even allowing for called games, a column that marks 1 of 62 tied KBO games and 0 of 72 tied NPB games, and reads 9 innings on cancelled games, is default-filled.
2. **The extras share is `NOT_ESTIMABLE` from these files.** The line scores that would settle it are blank for almost all rows, and the prose summaries contain no inning count. No replacement number is offered: any figure from memory or from another league would be an unsourced estimate.
3. **What stands.** The measured quantities (scores, totals, margins, ties, one-run and home-win shares) are unaffected.
4. **What changes.** LEAGUE_PROFILES now says `NOT_ESTIMABLE` for both extras shares, forbids borrowing the MLB 8.7%, and keeps `BASELINE_UNAVAILABLE` for extras-dependent baselines until innings are recovered. The correction is recorded in ARCHIVE_USE_GUIDE §8.
5. **Consequence for past cards.** A text search of the six KBO cards of the retrospective cohort (P-557, P-558, P-559, P-564, P-572, P-573) for "0.1%", "extra-innings share" and "extras share" found no use of the profile's figure; P-572 reports its own model's extras contribution (+0.12 runs a game). That limits the statement to those six cards and to those search terms. Earlier KBO and NPB cards were not re-read, and no issued probability is changed.

## 5. What would resolve it

An official source with innings per game: for the KBO, the box score route named in SOURCES §C (`GetBoxScoreScroll`) or the English scoreboard (SOURCES §3.1, KBO English scoreboard, line score and R/H/E); for the NPB, `npb.jp` box scores. A prompt-7 task would populate `Innings Played`, `Extra Innings` and the line scores for 2023–2025 (5,370 rows) with field provenance, then recompute the shares. That collection was not attempted in this run: it is large, the sources need route-by-route checks, and the repair belongs under prompt 7 with its own coverage report.

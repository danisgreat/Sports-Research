# NBL results model: locked retrospective protocol

Recorded on 2026-09-29 after score-source reconciliation and **before** any NBL tuning or model holdout calculation. This tests historical NBL moneyline forecasts, not the skill of issued cards. NBL26 final scores were ingested for completeness checks but not used to choose the model or settings.

## Data and cutoff

- Official NBL regular-season schedule API provides NBL22–NBL26 event IDs, times, teams and final scores. The [FixtureDownload NBL archive](https://fixturedownload.com/results/nbl-2021) supplies an independent local-only score check. It agrees on 736 of 738 exact UTC event/teams/score tuples. [Perth Wildcats](https://www.wildcats.com.au/news/wildcats-with-a-record-breaking-night-in-cairns) confirms Cairns 76–105 Perth on 2022-10-10; [NBL](https://www.nbl.com.au/news/kings-take-care-of-wounded-jackjumpers) confirms Sydney 105–94 Tasmania on 2026-01-22. These resolve two FixtureDownload score errors. ESPN's 152 missing and 17 conflicting results are retained as diagnostics, never training labels.
- FixtureDownload raw snapshots stay in local `data/benchmark/nbl_fixturedownload/` under its [use terms](https://fixturedownload.com/terms); the repository retains their hashes and exact reconciliation counts, not their raw file contents.
- This is a second publisher check. Its upstream score collection may overlap the league's; the two publishers are not asserted to be independent collection systems.
- Forecast every calendar-week block from matches with kickoff strictly before 00:00 UTC on that block's first date. Group by UTC ISO week. NBL22 supplies initial training; tune on NBL23–NBL25; hold out all NBL26 regular-season games. Scores, teams, event IDs, and source hashes are frozen in `data/processed/nbl_data_manifest.json` before tuning.

## Fixed models and test

- **M0:** Laplace-smoothed historic home-win rate before the cutoff: `(home_wins+1)/(games+2)`.
- **M2:** Weighted ridge regression for home and away points together. Each team's offense and defense share one parameter across venues, plus a league intercept and home advantage. Team terms have an eight weighted-game ridge penalty; intercept and home advantage are unpenalized. The sole tuned setting is exponential time-decay half-life in `{180, 365, 730}` days, with ties choosing the longer half-life. Covariance comes from weighted pre-cutoff home and away residuals, transformed to margin and total. There must be at least 100 training matches and a positive-definite covariance; otherwise no forecast. Full-game moneyline probability is the margin-normal probability `P(home margin > 0)`. Spreads and totals later use the same bivariate margin/total distribution and exact integer-score push rules.
- Tune half-life by mean NBL23–NBL25 moneyline log-loss, one prediction per match. Lock the choice, processed-data SHA-256, code version and bootstrap seed before the NBL26 calculation. Run the NBL26 holdout once; refuse overwrite.
- Primary: per-event binary moneyline log-loss. Secondary: binary Brier, five-bin calibration, and mean margin/total residuals. Bootstrap paired M2-minus-M0 log-loss differences by UTC week, 10,000 resamples, seed `20260929`. **Pass only if the upper 95% percentile bound is below zero.** A nonpass leaves NBL unvalidated. No comparison to closing odds is part of this gate.

The result of this historical test cannot start the live pilot. NBL27 still needs 50 independent shadow events or four weeks, exact pregame receipts, a complete card emitter, terminal NBL adapter, and its own locked cohort weight before any eligible live card.

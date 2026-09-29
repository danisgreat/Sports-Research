# EPL results model: locked retrospective protocol

Recorded on 2026-09-29 before the tuning or 2025–26 holdout command was run. This is a model test, not proof that issued cards have skill.

## Data and leakage boundary

- Primary final scores: [openfootball `england`](https://github.com/openfootball/england), Premier League 2020–21 through 2025–26. Second-publisher score and schedule check: [Football-Data E0 season files](https://football-data.co.uk/data.php). All six seasons are complete as of this run. The score builder reads only final score, teams, date and time from the cross-check source; odds remain under `data/benchmark/`, outside forecast imports. Every score and 20-team season must agree, or the build stops. The cross-check confirms agreement; it does not certify distinct upstream collection.
- A forecast training cutoff is 00:00 UTC on the first date of its calendar-week block. Every feature and fitted match has `kickoff_utc < cutoff`; all matches in that block are forecast from the same earlier history. This is stricter than using the previous day for later matches within the week.
- First-season promoted-team prior: mean fitted attack/defence of Fulham, Leeds and West Brom from completed 2020–21. Subsequent unknown entrants use the mean fitted parameters of historical teams that entered after the first season. No unknown team gets a zero-strength default.
- The source kickoff times were inconsistent in zone convention; the processed cutoff uses Football-Data's local `Date`/`Time` converted using `Europe/London`. Missing times get noon with `DATE_ONLY`, but the week cutoff remains before the local date.

## Models

- **M0:** smoothed historical home/draw/away population counts from all matches before the cutoff; one Laplace count per class.
- **M1:** `PROBABILITY_TOOLKIT.md` §4 TB-1-MD, using season-to-date PF/PA, `k=2`, current league mean or prior-season mean when zero games, and previous completed season's mean home margin. Goal rates and 1X2 probabilities come from one independent Poisson matrix.
- **M2:** Dixon–Coles attack/defence and league intercept/home advantage, low-score correction, exponentially decayed past matches. The fixed ridge penalty is 0.12 per team parameter squared; sum-to-zero penalty is 100 per attack/defence sum squared. Rho is bounded `[-0.1, 0.03]`; all low-score factors and the score matrix must be nonnegative. Score grid is 0–20 goals per side with missing tail below `1e-6`.

## Tuning and one-shot test

1. Score each calendar-week block in 2021–22 through 2024–25 from a fresh pre-block fit. Tune only `xi` from `{0.001, 0.0019, 0.003}` by mean 1X2 log-loss, choosing the smaller xi on an exact tie.
2. Write `runs/epl_tuning_lock.json`, including data hash and the winning xi. Do not retune after the holdout is opened.
3. Run once on all 380 2025–26 fixtures using the locked setting. Primary score: per-match 1X2 log-loss. Secondary: three-class Brier (sum of three squared errors) and calibration by predicted top-outcome confidence.
4. Use 10,000 paired bootstrap samples of calendar-week blocks, seed `20260929`. **M2 passes** only if the upper 95% percentile bound on mean `M2−M0` log-loss is below 0. If not, **M1 alone passes** only if its upper bound against M0 is below 0. Otherwise the EPL lane stops. M2−M1 is reported, not an added gate.
5. Historical closing odds are a secondary post-settlement benchmark only. They cannot alter the settings, gate, or forecast. If a closing probability is missing, report its available sample; never fill it.

No prospective pilot card can be performance eligible from this holdout alone. The live pilot requires a separate frozen event-level metric, fixed lane weights and sample, at least four weeks or 50 shadow events, issue-time receipts, and exact settlement feeds.

**Pre-holdout repair:** The first tuning attempt stopped before producing any scored output because a 0–15 grid omitted `1.0841e-6` in one match, just above the declared bound. The grid was enlarged to 0–20 before tuning was rerun. No holdout scores had been viewed.

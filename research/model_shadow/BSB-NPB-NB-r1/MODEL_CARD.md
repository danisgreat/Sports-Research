# Model card: `BSB-NPB-NB-r1`

**Status: `DEVELOPMENT_ONLY`.** Development did not pass the every-season bar; it stays a development artifact and enters no lane. It is not a card input.

| Field | Value |
|---|---|
| Competition / endpoint | `Baseball/NPB` / `FULL_GAME_INCL_EXTRAS` |
| Comparators | `BASELINE_LEAGUE_V1`; TB-1 constants `CALIBRATED_PREV_EDITION(k:MLB)`. VALIDATED = PROBABILITY_TOOLKIT §4.3 table. CALIBRATED_PREV_EDITION = the toolkit's arithmetic and the nearest sport's k, with home edge and widths taken from the competition's previous edition by replaying TB-1 game by game (earlier data only); the nearest sport's constants alone made TB-1 worse than the league-only baseline in some competitions |
| Evaluation stages | REG (regular season only where the competition has one) |
| Data integrity | no automatic warning |
| Engine | `count` |
| Contracts priced | winner, any handicap line, any total line, from one score grid |
| Population | competitive games from the archive (`Previous Sports Results/Baseball/NPB`); pre-season excluded; rows read 22345, kept 21666, dropped {'zero_zero_placeholder': 53, 'missing_numeric_score': 565, 'duplicate_event_id': 61} |
| Label tier | B (ML_RL_IMPLEMENTATION_FRAMEWORK §7.1) |
| Inputs | prior results only (dates strictly before the fit date). No lineups, injuries, weather, rest or prices. |
| Fit window | games before the Monday of the forecast week, seasons s − 3 … s, weekly refits |
| Hyperparameters | half_life_days=90.0, ridge=128.0 (chosen on [2021, 2022]) |
| Failure behaviour | fit failure gives `NOT_ISSUED:FIT_FAILED`; an unseen team gets an explicit, labelled prior (`NEW_TEAM_PRIOR`). No default numbers. |
| Calibration | identity (`IDENTITY_INSUFFICIENT_CAL`); the recalibration experiment is in DEVELOPMENT_RESULTS |
| Development verdict | `FAIL_DEVELOPMENT`: home-win Brier, all test seasons pooled: vs BASELINE_LEAGUE_V1: -0.0025 [-0.0047, -0.0003]; vs TEAM_BASELINE_P (TB-1): +0.0012 [-0.0001, +0.0026] |
| Prospective results | none (no lane started) |

## Method

Poisson team ratings (no rho), time-decayed weighted likelihood with a ridge penalty. Ice hockey: fitted on regulation goals (an OT/SO final keeps min(home, away) for both teams). Baseball: final runs with a negative-binomial dispersion phi (Var = mu + phi mu^2) estimated by moments.

Tied mass goes to an extra-innings branch won by the home team with the training share of home extra-inning wins (winner +1); a share fitted by moments stays tied where the competition allows ties (for example NPB and KBO).

## Files

- [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md): paired comparisons, calibration, tuning.
- [PARAMETERS.md](PARAMETERS.md): the latest fit, with a worked example a reader can check by hand.
- [DEVELOPMENT_PREDICTIONS.csv](DEVELOPMENT_PREDICTIONS.csv): every development price (no market fields).

## Limits

- Results-only model. Lineups, injuries and rest are not modelled; real cards know more on the day.
- The archive rows are LABEL_B unless stated; dates are calendar cutoffs, not publication times.
- Development seasons have been opened before; only a prospective lane can show skill.

## Receipt

- `run_utc`: 2026-10-14T09:01:37Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-NPB-NB-r1
- `archive_snapshot_sha256`: aa092627e3ea25c966cb025017aee11e6bcd7a15fcc243399fc83e5be38faa18
- `seconds`: 148

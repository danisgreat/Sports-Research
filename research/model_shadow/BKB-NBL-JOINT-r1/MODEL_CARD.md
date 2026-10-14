# Model card: `BKB-NBL-JOINT-r1`

**Status: `DEVELOPMENT_ONLY`.** Development did not pass the every-season bar; it stays a development artifact and enters no lane. It is not a card input.

| Field | Value |
|---|---|
| Competition / endpoint | `Basketball/NBL` / `FULL_GAME_INCL_OT` |
| Comparators | `BASELINE_LEAGUE_V1`; TB-1 constants `VALIDATED`. VALIDATED = PROBABILITY_TOOLKIT §4.3 table. CALIBRATED_PREV_EDITION = the toolkit's arithmetic and the nearest sport's k, with home edge and widths taken from the competition's previous edition by replaying TB-1 game by game (earlier data only); the nearest sport's constants alone made TB-1 worse than the league-only baseline in some competitions |
| Evaluation stages | REG (regular season only where the competition has one) |
| Data integrity | no automatic warning |
| Engine | `gaussian` |
| Contracts priced | winner, any handicap line, any total line, from one score grid |
| Population | competitive games from the archive (`Previous Sports Results/Basketball/NBL`); pre-season excluded; rows read 8124, kept 8116, dropped {'missing_numeric_score': 4, 'zero_zero_placeholder': 4} |
| Label tier | B (ML_RL_IMPLEMENTATION_FRAMEWORK §7.1) |
| Inputs | prior results only (dates strictly before the fit date). No lineups, injuries, weather, rest or prices. |
| Fit window | games before the Monday of the forecast week, seasons s − 3 … s, weekly refits |
| Hyperparameters | half_life_days=90.0, ridge=8.0, cov_inflation=1.2 (chosen on [2021, 2022]) |
| Failure behaviour | fit failure gives `NOT_ISSUED:FIT_FAILED`; an unseen team gets an explicit, labelled prior (`NEW_TEAM_PRIOR`). No default numbers. |
| Calibration | identity (`IDENTITY_INSUFFICIENT_CAL`); the recalibration experiment is in DEVELOPMENT_RESULTS |
| Development verdict | `FAIL_DEVELOPMENT`: home-win Brier, all test seasons pooled: vs BASELINE_LEAGUE_V1: -0.0222 [-0.0331, -0.0114]; vs TEAM_BASELINE_P (TB-1): -0.0040 [-0.0098, +0.0019] |
| Prospective results | none (no lane started) |

## Method

Joint-normal team ratings. Home score = mu_home + attack[home] + defence[away] + e1; away score = mu_away + attack[away] + defence[home] + e2; (e1, e2) bivariate normal. Fitted by weighted ridge least squares with exponential time decay (half-life in days) and a ridge penalty towards 0. The residual covariance is the weighted residual covariance times a tuned inflation factor. Prices come from the bivariate normal evaluated on the non-negative integer lattice and renormalised; tied mass is then resolved by the league's extra-time rule.

Tied regulation mass goes to one extra period: home wins it with Phi(mu_margin * sqrt(r) / sd_margin) (r = extra period / regulation length); each team adds about r * mean_total / 2 points and the winner a further w (rounded mean absolute extra-period margin).

## Files

- [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md): paired comparisons, calibration, tuning.
- [PARAMETERS.md](PARAMETERS.md): the latest fit, with a worked example a reader can check by hand.
- [DEVELOPMENT_PREDICTIONS.csv](DEVELOPMENT_PREDICTIONS.csv): every development price (no market fields).

## Limits

- Results-only model. Lineups, injuries and rest are not modelled; real cards know more on the day.
- The archive rows are LABEL_B unless stated; dates are calendar cutoffs, not publication times.
- Development seasons have been opened before; only a prospective lane can show skill.

## Receipt

- `run_utc`: 2026-10-14T09:02:39Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBL-JOINT-r1
- `archive_snapshot_sha256`: e021011368510ac7f3e1ec167b426403426f1afc8c9b7d8412d25ddffc57cddb
- `seconds`: 61

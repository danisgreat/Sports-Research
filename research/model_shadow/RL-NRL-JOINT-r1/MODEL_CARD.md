# Model card: `RL-NRL-JOINT-r1`

**Status: `DEVELOPMENT_ONLY`.** Development did not pass the every-season bar; it stays a development artifact and enters no lane. It is not a card input.

| Field | Value |
|---|---|
| Competition / endpoint | `Rugby League/NRL` / `FULL_GAME_INCL_GOLDEN_POINT` |
| Comparators | `BASELINE_LEAGUE_V1`; TB-1 constants `VALIDATED`. VALIDATED = PROBABILITY_TOOLKIT §4.3 table. CALIBRATED_PREV_EDITION = the toolkit's arithmetic and the nearest sport's k, with home edge and widths taken from the competition's previous edition by replaying TB-1 game by game (earlier data only); the nearest sport's constants alone made TB-1 worse than the league-only baseline in some competitions |
| Evaluation stages | REG (regular season only where the competition has one) |
| Data integrity | no automatic warning |
| Engine | `gaussian` |
| Contracts priced | winner, any handicap line, any total line, from one score grid |
| Population | competitive games from the archive (`Previous Sports Results/Rugby League/NRL`); pre-season excluded; rows read 9583, kept 9581, dropped {'zero_zero_placeholder': 1, 'missing_numeric_score': 1} |
| Label tier | B (ML_RL_IMPLEMENTATION_FRAMEWORK §7.1) |
| Inputs | prior results only (dates strictly before the fit date). No lineups, injuries, weather, rest or prices. |
| Fit window | games before the Monday of the forecast week, seasons s − 3 … s, weekly refits |
| Hyperparameters | half_life_days=180.0, ridge=2.0, cov_inflation=1.1 (chosen on [2021, 2022]) |
| Failure behaviour | fit failure gives `NOT_ISSUED:FIT_FAILED`; an unseen team gets an explicit, labelled prior (`NEW_TEAM_PRIOR`). No default numbers. |
| Calibration | identity (`IDENTITY_INSUFFICIENT_CAL`); the recalibration experiment is in DEVELOPMENT_RESULTS |
| Development verdict | `FAIL_DEVELOPMENT`: home-win Brier, all test seasons pooled: vs BASELINE_LEAGUE_V1: -0.0176 [-0.0297, -0.0056]; vs TEAM_BASELINE_P (TB-1): -0.0054 [-0.0134, +0.0027] |
| Prospective results | none (no lane started) |

## Method

Joint-normal team ratings. Home score = mu_home + attack[home] + defence[away] + e1; away score = mu_away + attack[away] + defence[home] + e2; (e1, e2) bivariate normal. Fitted by weighted ridge least squares with exponential time decay (half-life in days) and a ridge penalty towards 0. The residual covariance is the weighted residual covariance times a tuned inflation factor. Prices come from the bivariate normal evaluated on the non-negative integer lattice and renormalised; tied mass is then resolved by the league's extra-time rule.

Tied regulation mass goes to sudden-death extra time (winner + 3 in the NFL, + 1 in the NRL); a share fitted by moments on the training draws stays a draw.

## Files

- [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md): paired comparisons, calibration, tuning.
- [PARAMETERS.md](PARAMETERS.md): the latest fit, with a worked example a reader can check by hand.
- [DEVELOPMENT_PREDICTIONS.csv](DEVELOPMENT_PREDICTIONS.csv): every development price (no market fields).

## Limits

- Results-only model. Lineups, injuries and rest are not modelled; real cards know more on the day.
- The archive rows are LABEL_B unless stated; dates are calendar cutoffs, not publication times.
- Development seasons have been opened before; only a prospective lane can show skill.

## Receipt

- `run_utc`: 2026-10-14T09:04:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: RL-NRL-JOINT-r1
- `archive_snapshot_sha256`: e6ae0e16ed76975379c4e355e58b8f06a0155738636c942807d2b97c3ce8751c
- `seconds`: 103

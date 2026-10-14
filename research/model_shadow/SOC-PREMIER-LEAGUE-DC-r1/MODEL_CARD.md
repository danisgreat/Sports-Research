# Model card: `SOC-PREMIER-LEAGUE-DC-r1`

**Status: `DEVELOPMENT_ONLY`.** Development did not pass the every-season bar; it stays a development artifact and enters no lane. It is not a card input.

| Field | Value |
|---|---|
| Competition / endpoint | `Soccer/Premier League` / `REGULATION_90` |
| Comparators | `BASELINE_LEAGUE_V1`; TB-1 constants `VALIDATED`. VALIDATED = PROBABILITY_TOOLKIT §4.3 table. CALIBRATED_PREV_EDITION = the toolkit's arithmetic and the nearest sport's k, with home edge and widths taken from the competition's previous edition by replaying TB-1 game by game (earlier data only); the nearest sport's constants alone made TB-1 worse than the league-only baseline in some competitions |
| Evaluation stages | REG (regular season only where the competition has one) |
| Data integrity | no automatic warning |
| Engine | `dixon_coles` |
| Contracts priced | winner (3-way), any handicap line, any total line, from one score grid |
| Population | competitive games from the archive (`Previous Sports Results/Soccer/Premier League`); pre-season excluded; rows read 20740, kept 20740, dropped none |
| Label tier | B (ML_RL_IMPLEMENTATION_FRAMEWORK §7.1) |
| Inputs | prior results only (dates strictly before the fit date). No lineups, injuries, weather, rest or prices. |
| Fit window | games before the Monday of the forecast week, seasons s − 3 … s, weekly refits |
| Hyperparameters | half_life_days=365.0, ridge=16.0 (chosen on [2021, 2022]) |
| Failure behaviour | fit failure gives `NOT_ISSUED:FIT_FAILED`; an unseen team gets an explicit, labelled prior (`NEW_TEAM_PRIOR`). No default numbers. |
| Calibration | identity (`IDENTITY_INSUFFICIENT_CAL`); the recalibration experiment is in DEVELOPMENT_RESULTS |
| Development verdict | `FAIL_DEVELOPMENT`: home-win Brier, all test seasons pooled: vs BASELINE_LEAGUE_V1: -0.0322 [-0.0406, -0.0238]; vs TEAM_BASELINE_P (TB-1): -0.0088 [-0.0137, -0.0038] |
| Prospective results | none (no lane started) |

## Method

Dixon–Coles Poisson ratings. log lambda_home = c + home + attack[home] + defence[away]; log lambda_away = c + attack[away] + defence[home]; low-score dependence rho on the 0–0, 1–0, 0–1 and 1–1 cells. Time-decayed weighted likelihood with a ridge penalty, analytic gradient, L-BFGS-B. Promoted teams take a prior centre equal to the mean rating of the previous season's bottom three.

Draws are a genuine outcome at this endpoint and stay in the grid.

## Files

- [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md): paired comparisons, calibration, tuning.
- [PARAMETERS.md](PARAMETERS.md): the latest fit, with a worked example a reader can check by hand.
- [DEVELOPMENT_PREDICTIONS.csv](DEVELOPMENT_PREDICTIONS.csv): every development price (no market fields).

## Limits

- Results-only model. Lineups, injuries and rest are not modelled; real cards know more on the day.
- The archive rows are LABEL_B unless stated; dates are calendar cutoffs, not publication times.
- Development seasons have been opened before; only a prospective lane can show skill.

## Receipt

- `run_utc`: 2026-10-14T09:05:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: SOC-PREMIER-LEAGUE-DC-r1
- `archive_snapshot_sha256`: 042634114d6d7a64619ab41fd5c28d9b544503d9e2319d41783a91e477e956d2
- `seconds`: 128

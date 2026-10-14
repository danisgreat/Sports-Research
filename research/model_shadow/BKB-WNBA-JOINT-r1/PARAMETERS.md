# Parameters: `BKB-WNBA-JOINT-r1`

Fit as of **2025-10-11** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-10-10), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 8.0, `cov_inflation` = 1.0

League constants: mu_home **82.743**, mu_away **80.363**; residual covariance [[102.90, 20.02], [20.02, 107.34]] (inflation included); margin SD **13.05**; residual draw share **0.000**.

**Worked example (check by hand).** Minnesota Lynx at home to Chicago Sky: mean home = 82.743 + attack[Minnesota Lynx] +2.305 + defence[Chicago Sky] +2.595 = **87.64**; mean away = 80.363 + attack[Chicago Sky] -4.224 + defence[Minnesota Lynx] -3.355 = **72.78**. Normal approximation P(home ahead) = Phi(14.86 / 13.05) = **0.873**; the lattice price including the extra-time branch is **0.875** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Minnesota Lynx | 2.3047 | -3.3549 | 5.6596 |
| Las Vegas Aces | 3.2987 | -0.6895 | 3.9882 |
| Atlanta Dream | 0.3760 | -3.4419 | 3.8179 |
| New York Liberty | 1.5945 | -1.7139 | 3.3084 |
| Indiana Fever | 2.3156 | 0.7520 | 1.5636 |
| Seattle Storm | 0.2175 | -1.1467 | 1.3642 |
| Phoenix Mercury | 0.8065 | -0.4848 | 1.2913 |
| Golden State Valkyries | -3.5291 | -4.3493 | 0.8201 |
| Los Angeles Sparks | 2.4487 | 5.0445 | -2.5958 |
| Washington Mystics | -3.4660 | -0.0727 | -3.3933 |
| Connecticut Sun | -3.3178 | 0.9981 | -4.3160 |
| Dallas Wings | 1.1746 | 5.8636 | -4.6890 |
| Chicago Sky | -4.2237 | 2.5955 | -6.8192 |


## Receipt

- `run_utc`: 2026-10-14T09:03:14Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-WNBA-JOINT-r1
- `archive_snapshot_sha256`: e651045662e22d9aca0a4696605a09448f52392fdc8fb86b95b5b0f442701e58
- `seconds`: 72

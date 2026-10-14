# Parameters: `BKB-LIGA-ACB-JOINT-r1`

Fit as of **2026-10-12** on every regular-season and post-season game in the archive from season 2023 to the archive's last game (2026-10-11), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **90.138**, mu_away **86.808**; residual covariance [[134.10, 45.48], [45.48, 121.75]] (inflation included); margin SD **12.84**; residual draw share **0.000**.

**Worked example (check by hand).** Valencia Basket at home to Coviran Granada: mean home = 90.138 + attack[Valencia Basket] +5.477 + defence[Coviran Granada] +2.290 = **97.90**; mean away = 86.808 + attack[Coviran Granada] -2.673 + defence[Valencia Basket] -2.785 = **81.35**. Normal approximation P(home ahead) = Phi(16.55 / 12.84) = **0.901**; the lattice price including the extra-time branch is **0.904** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Valencia Basket | 5.4773 | -2.7850 | 8.2623 |
| Real Madrid | 4.6712 | -1.6844 | 6.3556 |
| Kosner Baskonia | 3.8236 | -1.9806 | 5.8043 |
| Barça | 2.8983 | -2.2178 | 5.1162 |
| Asisa Joventut | -1.2052 | -3.7821 | 2.5769 |
| UCAM Murcia | 0.1651 | -2.2233 | 2.3884 |
| La Laguna Tenerife | 0.0663 | -1.5697 | 1.6360 |
| Unicaja | -0.6434 | -1.9932 | 1.3498 |
| BAXI Manresa | -0.6916 | -1.0811 | 0.3895 |
| Baskonia | 0.6434 | 0.3414 | 0.3019 |
| iLERNA Lleida | 0.8795 | 0.8342 | 0.0453 |
| Surne Bilbao | -1.2352 | -1.2479 | 0.0126 |
| Joventut Badalona | -1.5932 | -1.5220 | -0.0712 |
| Monbus Obradoiro | 1.1771 | 1.3066 | -0.1294 |
| Recoletas Salud San Pablo Burgos | 1.7506 | 2.2950 | -0.5444 |
| Río Breogán | 2.3137 | 2.8796 | -0.5659 |
| Zunder Palencia | -0.7285 | -0.0885 | -0.6400 |
| Surne Bilbao Basket | -2.3173 | -1.3540 | -0.9632 |
| Bàsquet Girona | -1.8138 | -0.2720 | -1.5417 |
| Hiopos Lleida | -1.7490 | -0.0595 | -1.6895 |
| Dreamland Gran Canaria | -4.0646 | -1.8101 | -2.2545 |
| MoraBanc Andorra | -0.0685 | 2.5620 | -2.6305 |
| Casademont Zaragoza | -0.9281 | 1.7967 | -2.7248 |
| FIATC Girona | -1.9363 | 1.1532 | -3.0894 |
| Kids&Us Manresa | -0.4092 | 3.0210 | -3.4303 |
| Ilerna Lleida | -2.2607 | 2.1662 | -4.4269 |
| Leyma Coruña | 0.4510 | 5.0258 | -4.5748 |
| Coviran Granada | -2.6726 | 2.2895 | -4.9621 |


## Receipt

- `run_utc`: 2026-10-14T09:03:33Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-LIGA-ACB-JOINT-r1
- `archive_snapshot_sha256`: 406fb0bbfbf3bcb84b9d7e3a969ea0840ec523864a79b5f28ac5f2be3486594f
- `seconds`: 144

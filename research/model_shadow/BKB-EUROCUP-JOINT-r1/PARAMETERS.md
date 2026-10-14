# Parameters: `BKB-EUROCUP-JOINT-r1`

Fit as of **2026-10-14** on every regular-season and post-season game in the archive from season 2023 to the archive's last game (2026-10-13), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 365.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **85.663**, mu_away **83.001**; residual covariance [[120.55, 28.85], [28.85, 121.70]] (inflation included); margin SD **13.59**; residual draw share **0.000**.

**Worked example (check by hand).** Hapoel Midtown Jerusalem at home to Veolia Towers Hamburg: mean home = 85.663 + attack[Hapoel Midtown Jerusalem] +4.887 + defence[Veolia Towers Hamburg] +5.939 = **96.49**; mean away = 83.001 + attack[Veolia Towers Hamburg] -2.412 + defence[Hapoel Midtown Jerusalem] -1.757 = **78.83**. Normal approximation P(home ahead) = Phi(17.66 / 13.59) = **0.903**; the lattice price including the extra-time branch is **0.905** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Hapoel Midtown Jerusalem | 4.8866 | -1.7568 | 6.6434 |
| Valencia Basket | 4.7511 | -1.4008 | 6.1519 |
| Paris Basketball | 3.7377 | -1.4965 | 5.2342 |
| Besiktas GAIN Istanbul | 3.8385 | -1.2870 | 5.1255 |
| Bahcesehir College Istanbul | 0.0246 | -4.5460 | 4.5705 |
| Hapoel Shlomo Tel Aviv | 3.6642 | -0.8663 | 4.5304 |
| Turk Telekom Ankara | 0.1845 | -4.2841 | 4.4686 |
| Napoli Basketball | 1.1352 | -1.8837 | 3.0189 |
| Cedevita Olimpija Ljubljana | -0.4831 | -3.1125 | 2.6294 |
| Cosea JL Bourg-en-Bresse | -0.5972 | -3.1713 | 2.5742 |
| Hapoel Bank Yahav Jerusalem | 0.1635 | -2.3339 | 2.4974 |
| Maxima Roma | -0.1968 | -2.5882 | 2.3914 |
| Aris Thessaloniki | 1.0126 | -1.3437 | 2.3562 |
| Dreamland Gran Canaria | -1.3397 | -3.5770 | 2.2373 |
| Tofas Bursa | 0.7184 | -1.4571 | 2.1755 |
| Buducnost VOLI Podgorica | 2.0525 | 0.0130 | 2.0395 |
| Mincidelice JL Bourg en Bresse | -0.5363 | -2.3060 | 1.7697 |
| Umana Reyer Venice | 1.8463 | 0.3047 | 1.5416 |
| U-BT Cluj-Napoca | 4.6924 | 3.6135 | 1.0789 |
| PAOK Thessaloniki | 0.1092 | -0.5472 | 0.6564 |
| Prometey Slobozhanske | 1.3192 | 0.7049 | 0.6143 |
| Besiktas Fibabanka Istanbul | 0.6732 | 0.3112 | 0.3620 |
| Baglietto Derthona Tortona | 0.3441 | 0.1084 | 0.2357 |
| Wolves Twinsbet Vilnius | 0.7319 | 0.5611 | 0.1708 |
| Riga Zelli | 0.2589 | 0.2654 | -0.0065 |
| La Laguna Tenerife | -0.3525 | -0.1279 | -0.2246 |
| BAXI Manresa | 2.6876 | 3.0514 | -0.3639 |
| Besiktas Emlakjet Istanbul | -1.3859 | -0.9880 | -0.3978 |
| Recoletas Salud San Pablo Burgos | 0.0753 | 0.4782 | -0.4029 |
| ratiopharm Ulm | 1.4808 | 1.9063 | -0.4255 |
| NINERS Chemnitz | -2.1799 | -1.7290 | -0.4510 |
| BOSNA BH Telecom Sarajevo | -2.3941 | -1.6391 | -0.7551 |
| Roma Basketball | -0.4528 | 0.3036 | -0.7564 |
| Siauliai Basketball | -2.2125 | -1.3326 | -0.8799 |
| Joventut Badalona | -1.0323 | -0.0553 | -0.9770 |
| Kids&Us Manresa | 1.4842 | 2.5246 | -1.0404 |
| Wolves Vilnius | -0.6154 | 0.5486 | -1.1639 |
| Rostock Seawolves | -0.6987 | 0.6079 | -1.3066 |
| Le Mans Sarthe Basket | -1.0179 | 0.5881 | -1.6060 |
| London Lions | -3.4618 | -1.8222 | -1.6396 |
| Dolomiti Energia Trento | -2.0703 | 0.1109 | -2.1812 |
| Skyliners Frankfurt | -1.6308 | 0.6415 | -2.2723 |
| Lietkabelis Panevezys | -2.1028 | 0.2182 | -2.3210 |
| 7Bet-Lietkabelis Panevezys | -1.0580 | 1.2694 | -2.3273 |
| Neptunas Klaipeda | 3.1341 | 5.6066 | -2.4724 |
| Aris Thessaloniki Betsson | -0.5738 | 2.1805 | -2.7542 |
| Trefl Sopot | -2.8237 | 0.4434 | -3.2670 |
| Aris Midea Thessaloniki | -4.6821 | -1.3801 | -3.3019 |
| ratiopharm ulm | -0.4281 | 4.1148 | -4.5429 |
| Balkan Botevgrad | -3.1179 | 1.9150 | -5.0329 |
| Slask Wroclaw | -0.7486 | 5.2597 | -6.0083 |
| Panionios Cosmorama Travel Athens | -4.4016 | 3.4424 | -7.8441 |
| Veolia Towers Hamburg | -2.4117 | 5.9392 | -8.3510 |


## Receipt

- `run_utc`: 2026-10-14T09:00:51Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-EUROCUP-JOINT-r1
- `archive_snapshot_sha256`: 2ce7859cf98d73c270504b37e4548e5a304d6445e27d3c71604f7ad587e20834
- `seconds`: 70

# TB-1: team-strength baseline, oval-sport references and cushion base rates (2026-09-25(e))

**Status: REFERENCE; operative as the card's anchor under `C-TEAM-BASELINE`** (`RULES_GENERAL.md` §"2026-09-25(e)").
- TB-1 is fitted on **population data only**: field-owner scores from ESPN and MLB statsapi.
- It fits nothing from the prediction logs, so `L-087` is not engaged.
- It reads no odds, lines or market material. ESPN keys that carry them are never read.

## Why

`BASELINE_P` (C-BASELINE-SKILL) knows only home/away. The settled record says the cards have near-zero resolution in MLB and basketball, and none at all in tennis, NFL and AFL (`research/settled_rows_2026-09-25/README.md`).
- **A stronger, team-aware anchor** gives those cards something informative to start from.
- **It is also a stronger bar to beat:** a departure from it must be named (`C-DEPARTURE-LEDGER`).
- NFL, AFL and NRL cards printed `REFERENCE_BASE_RATE: NOT_YET_DERIVED` for everything. They carry the worst Rank-1/Rank-2 record (12 W / 20 L in the probability era).

## Files

| File | What it is |
|---|---|
| `../../tools/team_baseline.py` | TB-1: season state, contract probabilities, live data adapters, CLI `predict` |
| `../../tools/test_team_baseline.py` | Offline unit tests; CI runs them |
| `validate_team_baseline.py` → `validation_results.json` | Leak-free, out-of-sample validation on every cached league-season |
| `pull_oval.py` (specs in `../base_rates_2026-09-25/pull_oval_specs.py`) | NFL 2024–25, AFL 2025–26 and NRL 2025–26 day-by-day pulls. 1,704 completed games; 0 failed days |
| `oval_base_rates.py` → `oval_base_rates.json` | NFL/AFL/NRL population rates, NFL key numbers, and underdog-cushion cover rates (also NBA/WNBA/NBL) |

## The model

Leak-free: each game is predicted from games completed before its date only.
- **Team PF and PA per game.** The season-to-date totals are shrunk toward the league mean by k pseudo-games. They are optionally seeded by r × last season's deviation (carry-over).
- **total_hat** = (home PF + away PA)/2 + (away PF + home PA)/2.
- **margin_hat** = ((home PF − PA) − (away PF − PA))/2 + the home edge to date (0 at a neutral site).
- **Widths.** The running residual SD, with the §7 reference width until 20 games have been predicted.
- **Distributions:**
  - normal with continuity, no tie (basketball, NFL, AFL, NRL);
  - negative binomial totals (MLB);
  - Poisson totals (NHL);
  - two Poissons (EPL, three-way).
- **Baseball and hockey handicaps** use the season's running share of wins by ≥ k. Their margins are not normal: 27.6% of MLB games are one-run games.
- **k and r** were chosen on the earlier season(s) wherever an earlier season is cached; otherwise on the same season, which is flagged.

## Validation: latest season, out of sample

| League (season) | n | k / r | P(home win) Brier: TB-1 v base | P(total > league mean) Brier: TB-1 v base | Total RMSE: TB-1 v league mean | Margin RMSE: TB-1 v home edge | Resolution flag |
|---|---:|---|---|---|---|---|---|
| NBA 2025-26 † | 1,217 | 2 / 0 | **0.216 v 0.248** | **0.240 v 0.249** | 19.37 v 20.85 | 15.09 v 16.47 | margin ✓ total ✓ |
| WNBA 2026 | 316 | 2 / 0.75 | **0.216 v 0.256** | **0.232 v 0.258** | 19.40 v 20.44 | 13.43 v 14.65 | margin ✓ total ✓ |
| NBL 2025-26 | 154 | 5 / 0 | **0.223 v 0.255** | 0.246 v 0.251 | 18.72 v 19.32 | 16.55 v 18.33 | margin ✓ total ✗ |
| AFL 2026 | 193 | 2 / 0 | **0.202 v 0.249** | 0.248 v 0.255 | 28.91 v 29.37 | 35.79 v 41.25 | margin ✓ total ✗ |
| NFL 2025 | 256 | 2 / 0 | **0.231 v 0.252** | 0.246 v 0.254 | 13.64 v 13.83 | 13.52 v 14.48 | margin ✓ total ✓ (marginal) |
| NRL 2026 | 201 | 2 / 0 | **0.240 v 0.253** | 0.252 v 0.255 | 14.13 v 13.92 (worse) | 19.73 v 20.72 | margin ✓ total ✗ |
| EPL 2025-26 † | 370 | 2 / 0 | **0.231 v 0.247** | 0.258 v 0.250 (worse) | 1.60 v 1.57 (worse) | 1.55 v 1.62 | margin ✓ total ✗ |
| NHL 2025-26 † | 1,291 | 20 / 0 | 0.248 v 0.250 | 0.249 v 0.250 | 2.30 v 2.30 | 2.55 v 2.58 | none |
| MLB 2026 † | 2,358 | 20 / 0 | 0.248 v 0.250 | 0.249 v 0.250 | 4.49 v 4.51 | 4.55 v 4.57 | none |

† Only one season is cached, so k was chosen on the same season; for the NBA, the result is flat for k = 0–10. "Resolution" means TB-1's Brier is at least 3% below the base rate's **and** its RMSE is lower.

**Early season** (either team has fewer than 5 prior games):
- TB-1 still beats the base rate on sides in the NBL (0.242 v 0.266), WNBA (0.255 v 0.292), NFL (0.246 v 0.253) and AFL (0.240 v 0.259).
- It does not in the NRL (0.284 v 0.271), NHL, EPL or MLB.
- Last-season carry-over (r = 0.75) helped the WNBA (0.255 against 0.260 without).

The tool flags `TB1_EARLY_SEASON` below 3 games per team.

**Reading.**
- **For sides and handicaps in basketball, AFL, NFL, NRL and EPL results, a two-number team model beats the population base rate by 5–19% in Brier.** The cards have shown near-zero resolution in basketball and none in NFL/AFL. So a card that departs from TB-1 in these leagues must say why.
- **In MLB and NHL, TB-1 adds nothing.** The population rate (with starters and lineups as named departures) stays the anchor.

## New population references: NFL, AFL, NRL (field-owner scores)

| | NFL 2024 | NFL 2025 | AFL 2025 | AFL 2026 | NRL 2025 | NRL 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Games | 272 | 272 | 207 | 207 | 216 | 213 |
| Home win (non-neutral) | 0.524 | 0.536 | 0.565 | 0.585 | 0.551 | 0.545 |
| Draw | 0.000 | 0.004 | 0.005 | 0.015 | 0.005 | 0.000 |
| Total mean (SD) | 45.8 (13.1) | 46.0 (13.8) | 168.6 (29.8) | 178.2 (29.1) | 46.1 (14.0) | 47.8 (13.9) |
| Total 10/50/90% | 30/46/62 | 29/45/65 | 132/168/208 | 142/181/216 | 29/44/64 | 30/48/66 |
| Home margin mean | +1.7 | +2.2 | +6.0 | +7.1 | +3.8 | +0.0 |
| Margin SD | 14.5 | 14.2 | 42.5 | 40.8 | 18.7 | 20.7 |
| TB-1 residual SD: total / margin | 13.1 / 13.7 | 13.4 / 13.6 | 29.8 / 36.9 | 29.1 / 36.7 | 13.8 / 18.3 | 13.9 / 19.9 |

**NFL key numbers:**

| Margin | 2024 | 2025 |
|---|---:|---:|
| P(\|margin\| = 3) | 0.136 | 0.151 |
| P(\|margin\| = 7) | 0.074 | 0.096 |
| P(\|margin\| ≤ 3) | 0.239 | 0.268 |
| P(\|margin\| ≤ 7) | 0.518 | 0.496 |

**Close-game masses:**
- AFL: P(\|m\| ≤ 6) 0.145 / 0.169; P(\|m\| ≤ 12) 0.30 / 0.28.
- NRL: P(\|m\| ≤ 2) 0.125 / 0.150; P(\|m\| ≤ 6) 0.34 / 0.29.

These replace `NOT_YET_DERIVED` in `BASE_RATES_REGISTER.md` §7.7.

## Underdog cushion cover rates: the population fact behind M32

The underdog is the side with the lower leak-free TB-1 margin (never the market). The table gives the share of games in which the TB-1 underdog covered +k.5.

| League (season) | Dog won outright | +1.5 | +2.5 | +3.5 | +5.5 / +6.5 | +7.5 | larger |
|---|---:|---:|---:|---:|---:|---:|---|
| NBA 2025-26 | 0.297 | 0.321 | 0.348 | 0.383 | 0.439 (+5.5) | 0.501 | +9.5 0.562 |
| WNBA 2026 | 0.321 | 0.339 | 0.365 | 0.390 | 0.459 (+5.5) | 0.531 | +9.5 0.610 |
| WNBA 2025 | 0.353 | 0.365 | 0.385 | 0.409 | 0.480 (+5.5) | 0.540 | +9.5 0.631 |
| NBL 2025-26 | 0.368 | 0.397 | 0.427 | 0.449 | 0.507 (+5.5) | 0.559 | +9.5 0.566 |
| NBL 2024-25 | 0.383 | 0.392 | 0.408 | 0.442 | 0.500 (+5.5) | 0.583 | +9.5 0.683 |
| NFL 2024 | 0.320 | 0.345 | 0.379 | 0.453 | 0.567 (+6.5) | 0.606 | +10.5 0.690; +13.5 0.704 |
| NFL 2025 | 0.395 | 0.422 | 0.457 | 0.543 | 0.596 (+6.5) | 0.655 | +10.5 0.695; +13.5 0.762 |
| NRL 2025 | 0.385 | 0.412 | 0.440 | 0.511 (+4.5) | 0.566 (+6.5) | 0.615 (+8.5) | +12.5 0.670 |
| NRL 2026 | 0.417 | 0.429 | 0.491 | 0.509 (+4.5) | 0.549 (+6.5) | 0.617 (+8.5) | +12.5 0.651 |
| AFL 2025 | 0.294 | — | — | — | 0.383 (+6.5) | 0.483 (+12.5) | +18.5 0.556; +24.5 0.600; +30.5 0.628 |
| AFL 2026 | 0.328 | — | — | — | 0.430 (+6.5) | 0.505 (+12.5) | +18.5 0.586; +24.5 0.618; +30.5 0.688 |

**The fact.** In basketball, NFL, NRL and AFL, a small cushion on the weaker team **covers well under half the time**:
- basketball and NFL: +1.5 to +3.5 covers 32–54%;
- NRL: +1.5 or +2.5 covers 41–49%;
- AFL: +6.5 covers 38–43%.

The cards stated such rows at 0.52–0.64, and they won 7 of 27. The cushion adds only P(the dog loses by ≤ k), which is small: P(\|margin\| ≤ 2) is 7–12% in basketball.

This is the population mechanism behind M32 and the RM-1 cushion term. It is also the `BASELINE_P` for every such row from now on (`C-PLUS-CUSHION` amended, `RULES_GENERAL.md` §"2026-09-25(e)").

## Limits

- **Two numbers per team.** TB-1 knows nothing of lineups, injuries, rest, travel, pitchers, goalies or the venue beyond a league home edge. Those are the card's named departures.
- **One or two seasons per league.** k and r are coarse. NBA, NHL, EPL and MLB were tuned on the same season.
- **Early-season games** carry `TB1_EARLY_SEASON`. The NRL early-season result is worse than the base rate.
- **The NRL team-schedule endpoint returns HTTP 500** (2026-09-25). The tool reads the day-by-day scoreboard instead; the first call takes about 2 minutes, then it is cached.
- **The NFL margin model ignores key-number lumpiness.** The masses above are for disclosure and the departure ledger.

# Regime multipliers: do they make the forecast more accurate? (REGIME-v2)

**Owner instruction, 8 November 2026:** "do comprehensive research on them to see if they can improve the accuracy of predictions and see if this is still necessary and include/exclude them accordingly." The subject is the PRD-07 regime multipliers estimated on 2026-10-09 from the results archive (retired 16 October) and set aside by CR-2026.11.07-R3 (R-18).

## 1. The question that matters

The archive multipliers are raw ratios: mean game total in a regime (early season, finals) divided by the season mean. A card does not need that ratio. Its reference already follows the season to date (TB-2-MD blends the prior-season league mean into a young season and rates teams on their earlier games), so the only useful question is: **in this regime, is the reference's own total biased, and does correcting it improve held-out proper scores?** A raw ratio can be large while the reference is unbiased (it already sees early-season scoring), and small while the reference is badly biased (playoff teams play slower against stronger defences than their regular-season ratings say).

## 2. Method

- **Reference replication.** For every game, standings were built only from verified finals dated before the game's date (same-day results excluded). The expected total is the TB-2-MD additive centre of `ml/reference.py` with the toolkit's k (`ml.config.TB1_VALIDATED`), the league mean blended with the prior season's mean at 200 team-games (`LM_PRIOR_WEIGHT`), exactly as the reference does. Postseason games use the final regular-season standings, as the ESPN standings feed does. The NBA run is the declared NBA reference itself; MLB's reference is the release model MLB-CYCLE-4, so the MLB run is a proxy of it (the release has no postseason or calendar feature, so a regime row does not double count).
- **Scores.** Bias (actual minus forecast), CRPS of the reference's normal total (toolkit `sd_total`), and the Brier score of P(over) at three lines around the reference's own centre (the centre rounded to the half point, and plus and minus a quarter SD), so no line was chosen after the fact. Paired differences "with minus without"; negative means the multiplier helps.
- **Held-out test.** Leave one season out: each season's regime games get the multiplier fitted (pooled actual/forecast ratio) on the other seasons only; all held-out games are scored together, with a bootstrap over seasons (4,000 draws). The archive's recommended multiplier was also scored as published.
- **Status rule (EFFECT-v1).** `MEASURED_CONFIRMED` when the size's interval excludes zero and both held-out scores improve with intervals below zero; `MEASURED_NOT_CONFIRMED` when the size's interval excludes zero but the held-out test does not confirm it; `MEASURED_NULL` when the size's interval contains zero or the effect is no larger than the reference's bias outside the regime.

## 3. Data and access (checked 2026-11-08)

| League | Seasons tested | Source | Access check |
|---|---|---|---|
| NBA | 2020-21 to 2025-26 (2019-20 as the first prior) | `research/verified_history/2026-10-17-nba`, CANONICAL_EVENTS `CORROBORATED_FINAL`, scores from OWNER_RESULTS | In the repository |
| MLB | 2021 to 2026 (2019 as the first prior; 2020 skipped) | MLB Stats API schedule with scores, `statsapi.mlb.com/api/v1/schedule`, regular and postseason (F, D, L, W) | robots.txt 404 (no rules file) |
| AFL | 2015 to 2026 (2014 prior; 2020 skipped, 16-minute quarters) | AFL Tables season pages `afltables.com/afl/seas/<year>.html` | robots.txt 404 |
| NRL | 2021 to 2026 (2020 prior) | Rugby League Project `rugbyleagueproject.org/seasons/nrl-<year>/results.html` | robots.txt read: these paths allowed |
| NHL | not tested | `api-web.nhle.com` | robots.txt read: `User-agent: *` allowed with `ai-train=no`, but ClaudeBot, Claude-Web and anthropic-ai disallowed, so no bulk download was made by this agent |
| NFL | not tested | ESPN site API; Pro Football Reference | ESPN robots.txt 403, PFR a challenge page: neither is permission |

Raw captures are kept outside the repository in `../Sports-Research-workshop-cache/regime_study_2026-11-08/` (the ML_CACHE convention); their sizes and SHA-256 are in [outputs/RAW_CAPTURES.csv](outputs/RAW_CAPTURES.csv). They are study inputs, not learning-store admissions: no result was written to `research/learning_store`. Only score fields were parsed; no price field was read.

## 4. Results

Sizes are the pooled actual/forecast ratio minus one, with a season-block bootstrap interval ([REGIME_SIZES.csv](outputs/REGIME_SIZES.csv)). Held-out rows are from [LOSO_HELD_OUT.csv](outputs/LOSO_HELD_OUT.csv); the archive multipliers as published are in the `*_REGIME_TESTS.csv` files.

| League | Regime | Archive | Reference bias in the regime | Held-out CRPS | Held-out Brier | Seasons better | Status |
|---|---|---:|---|---|---|---|---|
| NBA | Playoffs | 0.970 | −4.5% (−6.0, −3.1), n 507; mean forecast 226.4, actual 216.2 | −1.547 (−2.521, −0.592) | −0.048 (−0.076, −0.020) | 5/6 | CONFIRMED |
| NBA | First 28 days | 0.988 | −0.3% (−0.7, +0.3), n 1,231 | +0.002 (−0.023, +0.047) | 0.000 (−0.001, +0.001) | 5/6 | NULL |
| MLB | Postseason | 0.924 | −10.9% (−13.9, −7.7), n 248; 8.92 against 7.94 runs | −0.077 (−0.120, −0.029) | −0.014 (−0.020, −0.006) | 4/6 | CONFIRMED |
| MLB | First 28 days | 1.000 | −1.4% (−3.4, +0.4), n 1,962 | −0.004 (−0.006, −0.002) | −0.001 (−0.001, −0.001) | 5/6 | NULL (size interval contains zero) |
| AFL | Finals | 0.943 | −3.2% (−6.1, −0.5), n 101 | −0.090 (−0.639, +0.436) | −0.006 (−0.018, +0.005) | 5/11 | NOT_CONFIRMED (HALF) |
| AFL | First 28 days | 1.000 | −0.7% (−1.2, −0.1), n 373 | −0.024 (−0.042, −0.006) | −0.000 (−0.001, +0.001) | 8/11 | NULL (smaller than the −1.7% bias outside the regime) |
| NRL | First 28 days | 0.938 | −2.5% (−4.5, −0.4), n 177 | −0.062 (−0.090, −0.025) | −0.004 (−0.006, −0.001) | 5/6 | CONFIRMED |
| NRL | Finals | 0.938 | −7.5% (−16.1, +1.8), n 54 | −0.052 (−0.591, +0.547) | −0.003 (−0.025, +0.021) | 3/6 | NULL |

**The archive multipliers as published.** NBA early season 0.988 made the forecast worse in every window (first 7, 14, 28 and 42 days; at 42 days CRPS +0.074, interval −0.007 to +0.160), because the reference was already within a point of the actual totals. NBA playoffs 0.970 helped (CRPS −1.44, interval −1.84 to −1.04) but under-corrected: the held-out size is about 0.955. MLB postseason 0.924 helped (CRPS −0.070) but under-corrected (about 0.89). AFL finals 0.943 over-corrected (bias −5.4 points became +4.3). NRL 0.938 was a raw early/season ratio; the reference's actual early bias is about −2.5%.

**Descriptive NBA check** ([NBA_REGIME_DESCRIPTIVE.csv](outputs/NBA_REGIME_DESCRIPTIVE.csv)): the early-28-day / season ratio ranges from 0.969 (2021-22) to 1.013 (2025-26), so the archive's 0.988 is a fair average of a quantity that does not help a season-to-date forecast. Playoff means sit 7 to 17 points below regular-season means (2023-24: 211.2 against 228.4).

**Mechanism (published sources).** NBA playoff games are slower: fewer possessions than the regular season in all but two seasons since 1980 (FiveThirtyEight, "The NBA playoffs are finally getting faster"), and in 2025-26 the playoff scoring drop was 8.3 points per team (TSN, "NBA playoffs 2026: five first-round trends"). MLB postseason scoring is lower because of bullpen-heavy usage (relievers over 53% of 2026 playoff innings, ESPN via ABC), optimised matchups and fewer second and third looks at a pitcher (CBS Sports, "Offense at historic low in 2026 MLB playoffs"). These explain the sign; the sizes come from the data above, not from the articles.

## 5. Decisions (implemented in CR-2026.11.08-R1)

| Decision | Rows |
|---|---|
| **Include, full size** | `E-NBA-PLAYOFF-TOTAL` −4.5%, `E-MLB-POSTSEASON-TOTAL` −10.9%, `E-NRL-EARLY-TOTAL` −2.5% (first 28 days) |
| **Include, half size until λ exists** | `E-AFL-FINALS-TOTAL` −3.2% (enters −1.6%) |
| **Exclude (measured, no effect)** | `E-NBA-EARLY-TOTAL`, `E-MLB-EARLY-TOTAL`, `E-AFL-EARLY-TOTAL`, `E-NRL-FINALS-TOTAL` |
| **Exclude (cannot be measured yet)** | `E-NEED-REGIME-NHL`, `E-NEED-REGIME-NFL`: `SCENARIO` rows only, with the data each needs |
| **Retire** | `E-NRL-SIX-AGAIN`: every season since 2020 is played under the rule, so the reference already contains it |
| **No row** | WNBA (archive recommended 1.000 for both flags); CUP_ROTATION (needs starting lineups) |

A row is applied once, to the total centre, before every contract is read from the one grid; the width floor still applies; the ledger records the row id and entry size (ADJUSTMENT_LEDGER_PROTOCOL §1).

## 5a. Correction the same day: the chronological test (REGIME-v3, CR-2026.11.08-R2)

A review on 8 November found that the leave-one-season-out fit in section 2 used later seasons when it evaluated earlier ones. That is not how information arrives. The confirmation test is now chronological: each season's multiplier is fitted on earlier seasons only (an expanding window), and the first season is not scored. Code: `ml/studies/regime_eval.py`. Output: [outputs/CHRONOLOGICAL.csv](outputs/CHRONOLOGICAL.csv). The leave-one-season-out table is kept and labelled exploratory.

| League | Regime | Chronological CRPS | Chronological Brier | Later seasons better | Status (R2 row) |
|---|---|---|---|---|---|
| NBA | Playoffs | −1.72 (−2.50, −0.90) | −0.052 (−0.076, −0.027) | 5/5 | CONFIRMED, FULL |
| MLB | Postseason | −0.081 (−0.117, −0.036) | −0.014 (−0.019, −0.009) | 5/5 | NOT_CONFIRMED, HALF: the test is on a proxy, not on MLB-CYCLE-4 |
| NRL | First 28 days | −0.029 (−0.081, +0.038) | −0.0019 (−0.0049, +0.0019) | 4/5 | NOT_CONFIRMED, HALF |
| AFL | Finals | +0.170 (−0.767, +1.064) | −0.005 (−0.026, +0.014) | 4/10 | NOT_CONFIRMED, HALF |
| MLB | First 28 days | −0.008 (−0.014, −0.003) | −0.002 (−0.004, −0.001) | 4/5 | NULL kept: the size's interval contains zero; a prospective candidate |

The append-only effect table gains `-R2` rows, and `research/effect_tables/SUPERSEDED.csv` retires the R1 rows; the ledger refuses a superseded row. Each regime adjustment on a card now carries its frozen unadjusted counterfactual (ADJUSTMENTS_V1), so prompt 6 scores adjusted against unadjusted on future games ([scikit-learn: time-series cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-of-time-series-data)).

## 6. Findings for prompt 8 (not acted on here)

The control window (regular season after day 28) shows the reference itself is biased in some leagues, which is a reference calibration matter, not a regime effect:

| League | Reference bias after day 28 (95% CI) | Note |
|---|---|---|
| NRL | +5.5% (+1.7, +9.8): totals underestimated | `LM_PRIOR_WEIGHT` = 200 team-games is about 12 NRL rounds; scoring rises through the season |
| AFL | −1.7% (−2.9, −0.5): totals overestimated | |
| MLB | +1.2% (+0.4, +2.1) | Consistent with warmer summer weather |
| NBA | +0.5% (−0.4, +1.5) | Unbiased |

A league-size-scaled prior weight (for example a fixed number of rounds rather than team-games) is a statistical change: it waits for prompt 8 at a season boundary (STATFREEZE-v1) and its own walk-forward test.

## 7. Limits

- MLB, AFL and NRL use a proxy of the reference built from the same code constants; MLB's declared reference is a release model.
- AFL and NRL finals are about nine games a season, so their intervals are wide; NHL and NFL could not be tested.
- Leave-one-season-out on six seasons is a small number of held-out blocks; the intervals are bootstrap intervals over those blocks.
- This is a development study (HISTORICAL_DEVELOPMENT evidence): it proves no prospective skill. Prompt 6 scores each regime row's ledger entries prospectively, and prompt 8 re-estimates the rows between seasons.

## 8. Reproduce

From the repository root (the study code moved to `ml/studies/` on 2026-11-08): `python -m ml.studies.regime_nba <OUT>`; with the cached captures, `python -m ml.studies.regime_generic mlb|afl|nrl <RAW> <OUT>`; then `python -m ml.studies.regime_eval --outputs <OUT>` for the sizes, the exploratory leave-one-season-out table and the chronological test. Seeds are fixed (20261108).

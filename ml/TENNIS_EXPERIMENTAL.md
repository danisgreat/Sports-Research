# Tennis singles experimental forecasting and online learning

**Status: EXPERIMENTAL_NOT_CERTIFIED.** Implementation: [`tennis_primary.py`](tennis_primary.py). Tests: [`tests/test_tennis_primary.py`](tests/test_tennis_primary.py). The existing [`PRIMARY_PREDICTION_PROTOCOL`](../PRIMARY_PREDICTION_PROTOCOL.md) `MODEL_ASSISTED_PRIMARY_V3` engine **still does not support tennis**; this is an independently versioned, opt-in development lane. Do not put its probabilities into that production lane, claim calibrated skill, auto-promote a model, or overwrite earlier cards.

## Scope and mathematics

- **Singles, standard 6-game sets with 7-point tiebreak at 6–6 in every set, best of 3/5, completed matches only.** No retirements, walkovers, abandoned matches, deciding match tiebreaks, no-ad scoring, Fast4, doubles, set/game-specific live markets, or other nonstandard formats.
- Source-reviewed historical tennis *service points won/total* for **both** players, competition identity, winner, surface, source availability and captured evidence. Separate exact-competition population (e.g. ATP or WTA) prevents unreviewed cross-tour borrowing.
- Hierarchical prior drawn from the actual reviewed same-surface competition cohort. Time-decayed (90/365 days), shrunk player serve and opponent return statistics infer future on-serve point probabilities. Standard deuce-game and tiebreak absorbing processes generate a **complete joint distribution of match winner, both players' total games, and sets won**, including best-of-five.
- Four experts: SURFACE_FAST, SURFACE_SLOW, SURFACE_ELO (chronological surface-weighted Elo **reweights the outcome classes**, without pretending games won determine match winner), and COHORT_BASE (league comparator). Full-information exponential Hedge combines all four distributions using **only actually retained and verified frozen forecasts** and subsequently available completed-match result feedback; provisional η=2. This is **online expert aggregation, not a trained environment-control RL agent**.
- Supported contracts: MATCH_WINNER PLAYER1/PLAYER2 (blank line), GAMES_HANDICAP PLAYER1/PLAYER2 (signed **handicap added to that player's games**), GAMES_TOTAL OVER/UNDER (whole-match games). Whole-match W/PUSH/LOSS and decisive `p_card`; no market prices, odds or stakes. Push is handled explicitly.
- No retrospective game-card forecasts are generated from outcomes. Standalone tennis research-only mini-log records remain `RESEARCH_ONLY_NO_MODEL` under the existing main primary protocol unless an authorised tennis-specific adoption/release explicitly changes operating rules. Stored numerical outputs are independent `TENNIS_EXPERIMENTAL_HEDGE_V1` development evidence.

## Input files and command

From repository root:

```bash
python -m ml tennis predict --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out TENNIS_ATTEMPT_001
python -m ml tennis verify --bundle TENNIS_ATTEMPT_001
python -m ml tennis settle --bundle TENNIS_ATTEMPT_001 --sets '6-4,3-6,7-6' --final-at 2026-10-17T11:00:00+11:00 --available-at 2026-10-17T11:05:00+11:00 --source-url https://example.org/results --evidence-path /absolute/capture.txt --evidence-sha256 ACTUAL_SHA256 --out FEEDBACK_001.csv
python -m pytest ml/tests/test_tennis_primary.py -q
```

`REQUEST.csv`: one row with `event_id,competition,player1,player2,surface,best_of,scheduled_start,issue_at,outcome_exposure` and recommended `actual_start,format`. Use `NONE_RECORDED`, `SINGLES`, one of HARD/CLAY/GRASS/CARPET, and time zones. The earliest scheduled/issue/verified actual start is the training horizon. Match identity is native/local, **not a reserved canonical P-ID**.

`HISTORY.csv`: independently reviewed, deduplicated completed rows with `event_id,competition,player1,player2,winner,surface,date,final_at,available_at,status,admission,p1_serve_won,p1_serve_total,p2_serve_won,p2_serve_total,source_url,evidence_path,evidence_sha256` and recommended `format=SINGLES`. Each source must have `status=FINAL`, `admission=RESEARCH_INPUT_REVIEWED`, a real HTTPS evidence URL, and matching capture digest. Date, final and first defensible source availability must predate the forecast horizon. **Required minimum for initial issue:** 40 reviewed matches in the same competition, at least 15 on the target surface, at least five prior matches per target player with both service-point count pairs. These are conservative operational gates, **not statistically validated adequacy or calibration thresholds**. Larger source-backed histories are preferable. No fabricated service-point statistics, source times, IDs, retirements or incomplete rows.

`CONTRACTS.csv`: `contract_key,family,side,line` with unique keys and the supported families above. The model computes each supplied line from the same coherent mixture; unsupported propositions remain separately assessed by normal research without fictitious ML values.

Optional `--feedback FEEDBACK.csv` contains unique rows emitted by `tennis settle` from earlier **original frozen tennis bundles**. Every eligible row is reverified against that immutable bundle, official completed set scores, evidence hashes and recomputed expert winner-Brier losses. Feedback arriving after the horizon cannot affect the forecast. Missing original bundles, duplicates, tampering and bad scope block its use. To keep the inputs reproducible, retain all original bundles and captures at stable paths.

`--out` is a new empty path. The runtime will **not overwrite** any forecast bundle. It writes `REQUEST.csv`, `HISTORY.csv`, `CONTRACTS.csv`, `FEEDBACK_INPUT.csv`, `GRIDS.csv` (all four experts plus mixed mass), `PREDICTIONS.csv`, and `RECEIPT.csv` (file hashes, policy, horizon, code hash, feedback counts, mixture weights). Verify after producing, and retain the original bundle before settling. Proof of capture hash is **not** independent proof of sporting-source truth, original pre-start publication or result blindness.

## Learning, imbalance, missing data and admission

Mini-log boundaries never form training batches. Ten basketball games and one tennis match in a mini are fine: accumulate validated tennis match labels across all minis. The previous human cards are useful for **research/error diagnostics**, not retroactive loss vectors for these tennis experts. No fixed mini-log quota is needed. The independently source-backed tennis historical population provides most training rows; a few manual mini-log results are future label candidates only. Never infer that four propositions on one match provide four independent observations.

This initial model is intentionally conservative and incomplete: on-serve points are approximated as independent conditional on player and surface, ignoring pressure, fatigue, injury, match-level tempo, player uncertainty, actual server order and weather. Elo K, shrinkage, decay, relative serve/return mapping and η are provisional. The platform has not conducted rolling-origin evaluation, separate per-tour validation, match winner/totals/handicap calibration, prospective performance testing or reliable data-source coverage proof for this code. Until those are independently demonstrated, **do not promote to certified or universal numerical primary**; complete manual research when a numerical run fails.

# MLB shadow model lane (`C-MLB-SHADOW`, opened 2026-09-26)

**Status: CODE IMPLEMENTED. TEAM-ONLY CORE VALIDATED ON RETROSHEET 2022–2024 AFTER ONE RE-SELECTED PRIOR (v2). STARTER TERM NOT VALIDATED. NEVER A CARD INPUT.**

This folder holds the prospective shadow record for the MLB A0/A1 pilot that `NUMERICAL_PROGRAM.md` §2 names as the numerical programme's first scope. The model is `tools/mlb_model.py`, with tests in `tools/test_mlb_model.py`.

## Why MLB first

The hand-built card process has its lowest resolution in MLB (0.0075; 58.6% of decisions won at a stated 0.596), and TB-1 found no resolution from team scoring alone. A model whose only extra information is the probable starters, captured before first pitch, is the cheapest honest test of whether anything beats the population in this sport.

## What the model is

| Part | Content | Status |
|---|---|---|
| A0 | League population to date: home-win rate and empirical total and margin frequencies | Leak-free by construction |
| A1 | Pooled park-neutral team offence and prevention, pooled park factor, league home/away split, and a starter term (the probable starter's pooled run prevention, blending RA9 and FIP, replaces his team's prevention for his expected share of innings) | Declared priors in `PRIORS`. **One re-selected (2026-09-26(c)):** `team_prior_games` 20 → 120, because v1 was overconfident (P(home win) 0.08–0.90) and no better than A0 |
| Joint | Shared-environment Gamma-Poisson (negative multinomial), shape from the season's moments; ties removed (route A reduced form, `RULES_BASEBALL.md` control 37) | Per `MODEL_IMPLEMENTATION_RECIPES.md` §5 |

## Files written here

| File | Written by | Rule |
|---|---|---|
| `shadow_log.csv` | `tools/mlb_model.py shadow` | One row per game and line, frozen after the card and before first pitch. Append-only; the tool refuses to replace a row or to freeze a started game |
| `shadow_results.csv` | `tools/mlb_model.py settle` | Finals from the statsapi feed, with source URL and time. Append-only |
| `validation_<season>.json` | `tools/mlb_model.py validate --season <year> --out …` | Leak-free rolling-origin A0 v team-only A1 from statsapi. **The independent test is 2025** (`--season 2025`): statsapi was unreachable from the implementation session. The Retrosheet 2022–2024 comparison (v1 failed; v2 selected on 2022, then better than A0 and level with TB-1 on 2023–2024, not independent) is in `research/sport_models_2026-09-26/README.md` |

## Order of operations for an MLB card

1. Build and freeze the card as normal. The card never sees this model.
2. Before first pitch: `python tools/mlb_model.py shadow --gamepk <pk> --total <line> --card P-###`. It is blind: it prints the row ID only (2026-09-26(d)).
3. After the final: `python tools/mlb_model.py settle`, then `python tools/mlb_model.py score`. The card's settlement prints `SHADOW: <row id>` or `SHADOW: MISSED <reason>` (audit `10s`).

## Preregistered review (150 settled games; a review point, not proof)

A proposal to use the model as an MLB anchor requires all three:
1. A1 − A0 Brier below 0 with the day-block interval below 0;
2. A1 better than the cards' own p on the shared games;
3. an explicit user instruction (the RM-1 precedent), because `C-RULE-FREEZE` treats any new anchor as a `MODEL_CHANGE`.

Otherwise the lane continues or is retired with the result recorded.

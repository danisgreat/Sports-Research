# Historical engine sections of RULES_AFL.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The AFL model (A1) is ridge ratings with draws allowed. On 2021–2024 it beat the league baseline on results and margins, and TB-1 on results. It gave **no gain on totals**; at the total line TB-1 was ahead by 0.008, but the interval crosses 0. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** AFL sides are the most predictable target in the repository. In 2026 the model's favourite reached 0.70 in **39%** of games and won **90.6%** of them (result Brier 0.183 against the population's 0.244). Totals are not predictable: 11% of games reach 0.70 at the league line, and those won 67%. On the cards' own AFL contracts (6, from 3 cards) the model was no better than the cards (A1 0.315, card 0.348, population 0.338). A STRONG Rank 1 is realistic on an AFL side, not on a total (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Territory to scoring shot to conversion pipeline:
   $$\text{Inside 50s (I50)} \longrightarrow \text{Scoring Shots} \longrightarrow \text{Goal/Behind Joint Distribution} \longrightarrow \text{Total Points } (6G + B)$$
2. **Shot and Conversion Decoupling**: Shot creation volume and conversion efficiency are separated; conversion variance is handled via Beta-Binomial shot modeling.
3. **Ground and Environmental Factors**: Venue dimensions (e.g. SCG vs MCG) and ground-level wind regimes condition scoring chains.
4. **Independent Training**: Fit exclusively on `H0-AFL-v1` via `fitzRoy` (ingested through isolated R script `runtime/r_ingestion/afl_fitzroy.R` (removed 2026-10-09)); D0 is strictly reserved for qualitative error diagnostics.


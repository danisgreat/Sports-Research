# Historical engine sections of RULES_AMERICAN_FOOTBALL.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The NFL model (A1) is ridge ratings with the league's own key-number weights (3, 7, …). On the NFL 2021–2025 it beat the league baseline on results and margins. It was ahead of TB-1 on results, but the interval crosses 0. It gave **no gain on totals**. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** In the NFL 2025, the model's favourite reached 0.70 in 27% of games and won **73.1%**. The 0.70–0.80 band won only 67% at a stated 0.747, so it is over-confident. This replicated on 2021–24 (66.7% at 0.744, 177 games; C1, 2026-09-27). A uniform shrink did not improve the Brier score, so the model is unchanged: read an NFL favourite at 0.70–0.80 as about a two-in-three row. Totals reach 0.70 in only 8% of games. The side reference is TB-1, because A1 was not separated from it. On the cards' own NFL contracts (9, from 5 cards): card 0.266, A1 0.274, population 0.301 (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Simulates match possessions as a Markov drive sequence:
   $$\text{Starting Field Position} \longrightarrow \text{Drive Efficiency (EPA/play)} \longrightarrow \text{Drive Outcome (TD / FG / Punt / Turnover)}$$
2. **Key Number Discrete Preservation**: Scores accumulate in increments of 3, 6, 7, and 8, naturally preserving NFL key numbers (3, 7, 10, 14) without artificial smoothing.
3. **Regime Conditioning**: QB availability, offensive line continuity, and defensive pressure rates condition drive transition matrices.
4. **Independent Training**: Fit exclusively on `H0-NFL-v1` via `nflfastR`; D0 is strictly reserved for qualitative error diagnostics.


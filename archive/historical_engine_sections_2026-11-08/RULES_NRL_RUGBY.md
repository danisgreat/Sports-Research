# Historical engine sections of RULES_NRL_RUGBY.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The NRL model (A1) is ridge ratings with key-number weights. Validated on 2026: results not significant (−0.0273, +0.0003); margin RPS better; totals no better than the population. TB-1's result gain was not significant either, so the NRL reference is the population. The hand-computed TB-1-MD did beat the population on 2026 sides (`PROBABILITY_TOOLKIT.md` §4.4). That is one season found after the fact, so it is test `T-TB1MD-NRL`, not an anchor. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** The model's favourite reached 0.70 in 19% of games and won 68.3%. The 0.70–0.80 band won 67% at 0.737, so it is over-confident. On the cards' own NRL contracts (4, from 2 cards): card 0.271, A1 0.203. That is too few to read (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Sets, completion, and territorial field position simulation:
   $$\text{Completed Sets} \longrightarrow \text{Attacking 20m Entries} \longrightarrow \text{Tries (4 pts) + Conversions (2 pts) + Penalty/Field Goals (1/2 pts)}$$
2. **Key Number Discrete Preservation**: Rugby league margins cluster around 2, 4, 6, 8, 10, 12; scores are discrete combinations, never continuous Gaussian approximations.
3. **Regime Conditioning**: 2020 six-again rule change strictly demarcates high-pace modern NRL from legacy low-pace rugby league. Spine availability (1, 6, 7, 9) and primary goal-kicker accuracy condition transition rates.
4. **Independent Training**: Fit exclusively on `H0-NRL-v1` via `nrlR` (ingested through isolated R script `runtime/r_ingestion/nrl_nrlr.R` (removed 2026-10-09)); D0 is strictly reserved for qualitative error diagnostics.


# Historical engine sections of RULES_ICE_HOCKEY.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The NHL model (A1) is regulation Poisson ratings, with OT won in proportion to scoring rates and the shoot-out a coin flip. Validated on 2023-24 to 2025-26: A1 beat the league baseline and TB-1 on the result, and beat the baseline on the regulation three-way and the margin. It was **worse than the baseline on totals**, and slightly worse than TB-1 at the total line. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** In the NHL 2025-26, the model's favourite reached 0.70 in only 6% of games (won 72.9%), and 67% of games sat at 0.50–0.60 (Brier 0.248 against 0.250). Totals are not predictable by any model here: A1 was worse than the population, and TB-1 no better. A STRONG NHL Rank 1 is rare (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


# Historical engine sections of RULES_BASKETBALL.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The basketball model (A1) is ridge offence/defence ratings with a no-tie normal margin and residual widths. It beat both the league baseline and TB-1 on results **and totals** in the NBA (2012-13 to 2014-15, and again 2023-24 to 2025-26) and the WNBA (2022–2026). In the NBL it beat the baseline and TB-1 on 2025-26 results, but not significantly on 2024-25; NBL totals improved in 2024-25 only. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** Basketball sides are highly predictable. The model's favourite reached 0.70 in 26–29% of games and won **80–84%** (NBA 79.5%, WNBA 83.7%, NBL 80.4%). Totals at a neutral line rarely reach 0.70 (NBA 12%, NBL 15%). On the cards' own contracts the samples are too small to separate card from model (WNBA: 8 contracts, card 0.170 against A1 0.270; NBL: 6 contracts, 0.285 against 0.322) (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Generates a bivariate joint team-score distribution $(S_{\text{home}}, S_{\text{away}})$ driven by:
   $$\text{Points} \approx \text{Pace (Possessions)} \times \text{Offensive Rating (Points per 100 Possessions)}$$
2. **Derived Contract Monotonicity**: Margins and totals are derived from the single joint matrix. All spreads $P(\text{Home} - \text{Away} \ge H)$ and totals $P(\text{Total} \ge T)$ satisfy strict monotonicity.
3. **Player Rotation & Minutes Exposure**: Team efficiency adjusts dynamically for confirmed starters, bench rotation minutes, and replacement-level usage transfers.
4. **Independent Training**: Fit exclusively on `H0-BASKETBALL-NBA-v1`; D0 is strictly reserved for qualitative error diagnostics.


# Historical engine sections of RULES_SOCCER.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The soccer model (A1) is Poisson attack/defence ratings with linked halves. On 2022-23 to 2025-26 it beat the league baseline on results and margins in all five top leagues, and TB-1 on EPL results. It did **not** beat the baseline on totals in the EPL, Serie A or Ligue 1, nor on BTTS or first-half totals outside La Liga. Dixon–Coles added nothing. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** EPL three-way favourites reach 0.70 in only 6% of games (result Brier 0.222 against 0.243), so soccer's STRONG Rank-1 rows come from phase, team-total and double-chance markets (the cards' own record), not from three-way results. On 4 EPL card contracts: card 0.178, A1 0.151. The 80 soccer cards spread across more than 30 competitions, most without a validated model (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.9 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Bivariate goal process derived from expected goals (xG) and shot quality:
   $$\text{Shots} \times \text{xG/Shot} \longrightarrow \text{Poisson/Negative Binomial Goal Matrix } P(G_{\text{home}}=g_1, G_{\text{away}}=g_2)$$
2. **Derivative Independence**: Corners and cards are modeled via distinct point processes, not as proxies for goal dominance; all contract lines (1X2, Over/Under, BTTS, Asian handicap) are integrated directly from the joint score PMF.
3. **Regime Conditioning**: Red cards, key starter rotation (especially starting goalkeeper and primary goalscorer), and match state (leading/trailing dynamics) condition transition intensities.
4. **Independent Training**: Fit exclusively on `H0-SOCCER-v1` via StatsBomb / Football-Data.co.uk; D0 is strictly reserved for qualitative error diagnostics.


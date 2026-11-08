# Historical engine sections of RULES_TENNIS.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The tennis model: on ATP 2023 to January 2026, surface-blended Elo narrowly beat overall Elo on winners (Brier 0.222 against 0.224). The serve-chain games route lost to the population at v1; after v2 (a match-level gap effect, selected on 2021–22) it is level to slightly better. WTA was not validated. A retirement voids the games rows. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** Tennis winners are predictable by Elo (Brier 0.222 against a coin flip's 0.25), and A1 improves that only narrowly. The WTA is not validated (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Surface-adjusted serve/return point Markov model:
   $$\text{Point Win Prob } p_{\text{serve}} \longrightarrow \text{Game Hold/Break } P(\text{Hold}) \longrightarrow \text{Tiebreak/Set Distribution} \longrightarrow \text{Match Winner & Games Matrix } (G_1, G_2)$$
2. **Derivative Coherence**: Games totals and games handicaps ($G_1 - G_2$) are integrated directly from the discrete joint games grid; P(deciding set) and straight-set distributions are explicit.
3. **Regime Conditioning**: Surface (Clay, Hard, Grass, Indoor) and tournament format (Best-of-3 vs Best-of-5) condition serve/return transition kernels.
4. **Independent Training**: Fit exclusively on `H0-TENNIS-v1` (Tennis Abstract / OnCourt / Jeff Sackmann match charting); D0 is strictly reserved for qualitative error diagnostics.


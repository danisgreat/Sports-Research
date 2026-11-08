# Historical engine sections of RULES_BASEBALL.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The MLB model (A1) is a team-only core. It was validated on Retrosheet 2022–2024 and was overconfident at v1 (20 prior games per team). v2 (120, selected on 2022) beat the population on results and totals in 2023–2024 and tied TB-1 on results; that test is not independent. **The independent 2025 test replicated it** (`T-MLB-V2-2025`): A1 − A0 = −0.0023 [−0.0042, −0.0005] over 2,121 games. The declared-starter term did not add skill on results (P1, 2026-09-26(e)). NPB, KBO and CPBL: **not validated**. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** MLB is the least predictable major league measured.
- **No STRONG favourites.** In 2026 the team model's favourite **never** reached 0.70; 90% of games sat at 0.50–0.60 (win Brier 0.247 against 0.250).
- **The starter term failed its test.** It was tested leak-free on 2025–2026 (probable starters are recoverable from statsapi, which corrects the earlier claim) and did **not** improve results (preregistered verdict: not demonstrated). It improved the 2026 totals only.
- **The cards held their own.** On 61 contracts from 34 MLB cards, the cards (0.238) were no worse than A1 (0.241), A1 with starters (0.241) or TB-1 (0.246).
- **Rank 1 in MLB is almost never STRONG.** Say so (`TOP2_COIN_FLIP`) rather than force it (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.10 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Plate appearance (PA) base-out Markov chain simulation:
   $$\text{Matchup (Pitcher vs Batter)} \longrightarrow \text{PA Outcome (1B, 2B, 3B, HR, BB, K, Out)} \longrightarrow \text{Base-Out State Transition} \longrightarrow \text{Runs}$$
2. **Hook and Relief Ladder**: Explicit starter pitch count/tbf leash and score-state relief transition inning.
3. **Regime Conditioning**: Pre-2008, 2008–2014, and 2015+ Statcast tracking regimes strictly demarcated; extra-inning ghost-runner regime (2020+) segregated.
4. **Independent Training**: Fit exclusively on `H0-BASEBALL-v1` via pybaseball/Statcast; D0 is strictly reserved for qualitative error diagnostics.


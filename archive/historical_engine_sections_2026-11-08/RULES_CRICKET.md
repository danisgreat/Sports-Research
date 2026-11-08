# Historical engine sections of RULES_CRICKET.md

Moved verbatim on 2026-11-08 (CR-2026.11.08-R2). Superseded by the v24 reference; kept for the cards that cite them.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The cricket model (A1) is Elo for the result plus a ridge batting/bowling/venue first-innings total, priced 50/50 on who bats first. Second innings are target-censored and not modelled. **On the IPL (2016–2026), v1 was worse than a coin flip on results and worse than the format mean on totals**; v2 (elo_k 4, lam_team 200, re-selected on 2016–19) is only level with both. Cricket has **no demonstrated model skill**. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** IPL results are no better than a coin flip for a team-strength model (Brier 0.254 against 0.250). A STRONG cricket result row needs event evidence (the toss, the strip and the XI), not team strength (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).


### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: The engine estimates the full discrete predictive probability mass function $P(Y=y \mid X)$ of runs and wickets. All user propositions (e.g. Day 2 runs Over 185.5, Over 235.5, Under 285.5) are derived analytically from this single CDF, guaranteeing monotonicity: $P(O285.5) \le P(O235.5) \le P(O185.5)$.
2. **Test Cricket Engine**: Simulates $(R_{\text{future}}, W_{\text{future}}, O_{\text{future}})$ conditioned on current session, pitch wear, crease occupants, new-ball age, follow-on status, declaration risk, and match time budget.
3. **Limited-Overs Engine**: Ball/over-by-ball discrete state transition model conditioned on phase (Powerplay 1–6, Middle 7–40/15, Death 41–50/16–20), remaining wickets, and target-chase pressure.
4. **Independent Training**: Fit exclusively on `H0-CRICKET-TEST-v1` and `H0-CRICKET-LO-v1` via Cricsheet JSON; D0 is strictly reserved for error diagnostics.


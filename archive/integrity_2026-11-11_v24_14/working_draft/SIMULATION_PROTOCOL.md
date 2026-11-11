# Simulation: when, where and how (SIM-v2)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-11 and REV-12 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). It supersedes the "run as many simulations as possible" reading of a request and extends the [22 October simulation review](research/verification/framework_change_2026-10-22-1/SIMULATION_REVIEW.md). **Exact calculation first; simulation only where the path of the score matters; code only; never described but not run.**

## 1. The rule

1. Use the exact distribution wherever one exists (normal table, Poisson or negative-binomial grid, point-to-match recursion).
2. Simulate only the contracts in the table below, only in repository code (`python -m ml sim …`), and print the **seed**, **N** and the **Monte Carlo standard error**. At N = 100,000 the standard error of a probability is at most 0.0016; at 1,000 it is 0.016, as large as the effects the framework measures.
3. Near a threshold (a gate, a rank tie, another row), a probability within three standard errors is `MC_UNRESOLVED`; raise N or use the exact method.
4. A chat or agent that has not run code does not "simulate". It says so, and uses the exact method. A request that asks for "as many simulations as possible" is answered under this rule ([GAME_REQUEST_TEMPLATE](GAME_REQUEST_TEMPLATE.md)).
5. A simulator is **NOT_VALIDATED** until its structural check agrees with the competition's observed shares and its test passes. A card may use an unvalidated simulator only for a labelled sensitivity row, never for p_card.
6. Compare contracts on common random numbers (the same simulated games).

## 2. Where simulation is used

| Sport and contract | Exact method | Simulator | Module |
|---|---|---|---|
| Basketball, AFL, NFL, rugby winner, spread, total | Normal grid with tails; NFL key-number table | No | |
| Soccer results, totals, handicaps, corners | Dixon-Coles or Poisson grid | No | |
| Hockey winner, totals | Regulation grid + OT/shootout | No | |
| Hockey puck lines ±1.5, ±2.5, late-game totals | Grid + empty-net adjustment (approximate) | Optional: Poisson goals, pulled goalie, empty net, 3v3 overtime, shootout | `ml.sim.hockey` |
| Baseball run lines, first five, extras, totals near ties | Negative-binomial grid; tie mass reassigned to one-run margins (approximate) | **Yes:** plate-appearance chain by half-inning, automatic extra-innings runner, home team's last half-inning | `ml.sim.baseball` |
| Cricket innings totals, chases, DLS-affected games | Normal with heavy tails (approximate) | **Yes**, once a phase table is built from ball-by-ball history | `ml.sim.cricket` |
| Tennis match, sets, games | **Exact recursion** (point → game → set → match) | Only the match-level form shock, done by exact quadrature | `ml.sim.tennis` |
| Player props, single | Count model × minutes | Optional | `ml.sim.props` |
| Player props, correlated or same-game combinations | None | **Yes:** shared total, margin, minutes and availability | `ml.sim.props` |
| Early season and new teams | None | Draw ratings from their uncertainty and push each draw through the exact grid (not yet built) | |
| Ladders, finals, futures | None | Season simulation (not built) | |
| Evaluation intervals and power | None | Block bootstrap | `ml.core.metrics` |

## 3. The simulators (all seeded, all in `ml/sim/`)

- **Baseball.** A team is six plate-appearance probabilities (out, walk, single, double, triple, home run) and three runner-advancement probabilities. A half-inning is played plate appearance by plate appearance (vectorised); extras start with the automatic runner on second (MLB since 2020; `--no-ghost-runner` for leagues without it); the home team does not bat when it leads after the top of the ninth and a walk-off ends the inning when the lead is taken (a home run counts every run, any other hit only the runs needed). `scale_to_runs` moves a team's environment to the run mean the card's own distribution gives. **Defaults are illustrative and NOT_VALIDATED.** With them the simulator produces 28.6% one-run games, 9.7% extra-innings games and 9.99% walk-offs; the competition's observed one-run share was 28.1% (MLB, 9,718 development games), which is the structural check a card must repeat for its own competition before use.
- **Tennis.** Exact: game, tie-break (service pattern 1-2-2-2…), set (tie-break at 6-6, advantage, or a 10-point match tie-break), best of 3 or 5. It returns the winner, the set-score distribution and the joint pmf of games won as a `ScoreGrid`, so game totals and handicaps use the standard pricing code; a game handicap and the match winner are different questions. `with_form_shock` integrates over a normal shock on the relative level of the two players (15 Gauss-Hermite nodes), the structural answer to i.i.d.-point underdispersion; its sigma must be estimated from history. A Monte Carlo of the same chain exists only to test the recursion (it agrees on win probability within 0.012 and on mean games within 0.25).
- **Hockey.** Poisson goals before the pull window; inside it a team trailing by one pulls its goalie (optionally by two), its own scoring rate is multiplied and the leader scores into the empty net at a stated rate; ties go to a sudden-death overtime and then a shootout (a coin by default). **Pull, empty-net and overtime parameters have no defaults**; estimate them from NHL play-by-play and record n. With no pull effect the simulator reproduces the Poisson game (49% one-goal finishes and 17% regulation ties at 3.1 v 2.9 expected goals).
- **Cricket.** Delivery-by-delivery innings from phase tables of outcome probabilities (runs 0-6, wicket, wide/no-ball), optional multipliers by wickets lost, and a chase that stops at the target. **No default tables**; build them from Cricsheet ball-by-ball for the exact competition and format.
- **Props.** One draw of the game's total and margin per simulated game; each player's availability (a Bernoulli, so a questionable player is a mixture), minutes (normal, cut at zero and the maximum, with a starter's minutes reduced in a blowout) and gamma-Poisson counts at a rate per minute scaled by the total's elasticity. Joint probabilities are read from the same simulated games. **No fitted defaults.** `coverage` checks held-out actuals against predictive samples at the 50% and 80% bands.

## 4. Validation before a card may use a simulator

| Simulator | Structural check (must pass) | Held-out check |
|---|---|---|
| Baseball | One-run, extra-innings and walk-off shares within 3 points of the competition's observed shares; mean runs equal to the target | Coverage of run-line and first-five outcomes on a held-out season |
| Hockey | One-goal, two-goal, regulation-tie, overtime and empty-net-goal shares within 3 points of observed | Coverage of puck-line outcomes |
| Cricket | Simulated total mean and SD within 5% of the venue-class history; 2.5 SD tail share within a factor of two of observed | Coverage of held-out totals at 50% and 80% |
| Tennis form shock | The sigma estimated on history reproduces the observed spread of games per match | Coverage of game totals |
| Props | Coverage within 3 points of nominal at the 50% and 80% bands for every stat priced | Per stat and per player role |

Passing is recorded as a dated row in the development record of the card that first uses the simulator; until then every use is a labelled sensitivity.

## 5. Limits

- The illustrative baseball defaults and the test parameters in the unit tests are not sporting evidence.
- Hockey, cricket and props need caller-supplied parameters; none has been estimated or validated in this release.
- The structural shares quoted from the 22 October simulation review are development evidence on unadmitted archive data.

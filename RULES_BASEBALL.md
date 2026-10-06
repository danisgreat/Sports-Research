> **Current authority (October 5):** [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](research/verification/closure_2026-10-05/carryover.md), and [current implementation evidence](research/verification/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

# Baseball analysis rules

**Live rules for Baseball (MLB, NPB, KBO, CPBL, LMB). Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_BASEBALL_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_BASEBALL_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.1. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

MLB, NPB, KBO, CPBL, LMB, MiLB and international baseball are separate populations at every step (§8).

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| BB-P1 starters | Both starters linked to the official event/team/role, re-handshaken at the final refresh | No starter analysis drives a row; the starter is a mixture; dependent rows are capped |
| BB-P2 orders | The statsapi `battingOrder` (or the NPB/KBO official order) with its fetch time (B-1) | `LINEUPS_NOT_YET_PUBLISHED @ time` or `RETRIEVAL_MISS`; with `RETRIEVAL_MISS` no full-game total or run line may be Rank 1 (G14.2) |
| BB-P3 league and rules era | Innings, extras rule, DH, listed-pitcher/action terms, roof | Stop (`GATE-TARGET`) |
| BB-P4 termination terms | Official-game rule and operator action rule | `UNKNOWN_DEFINITION`; keep the termination branch |
| BB-P5 endpoint | Who bats last; whether the contract includes extras | Required before any total or run line is located |
| Tie-permitting leagues | KBO/NPB: the winner family is home/away/tie summing to 1, with the innings cap from the rulebook (control 32) | Never a two-way winner label |

### 0.2 Freeze receipts
- Read from the MLB statsapi gamefeed and boxscore (`SOURCES.md` §3.1): probables, official orders, gamefeed weather (condition, temperature, field-relative wind), umpires, state. Re-run within 60 minutes of first pitch (B-5).
- MLB totals at #1 or as the top O/U print the gamefeed weather block or `WEATHER_NOT_RETRIEVED`. **Never a city forecast** (B-2, M30).
- Check `mlbDebutDate` for every posted starter; under about 30 days of service is `LOW_SERVICE_SAMPLE`, which widens the team marginal and does not shift it (2026-09-19).
- NPB: the official box posts スタメン about an hour before first pitch. KBO: the English scoreboard. Native-language search for same-day news (L-067).

### 0.3 Building the run distribution — the default order (the P-491 template, 2026-09-23)
1. **Anchor.** Partially pooled team R/G × opponent RA/G, the league row and the venue row (B-6; `BASE_RATES_REGISTER.md` §7.5). TB-1 has **no resolution in MLB**, so `BASELINE_P` is the population row (2026-09-25(e)(b)1). Print `BASELINE_P` beside every row.
2. **Starters, applied once.** Per-start game log (IP/ER/SO/BB) with a front-loaded/back-loaded/uniform verdict and "command held?" (control 24). Rehab pitch-count ladder for an IL return (25). Small-sample mixture (11). Season prior versus current-regime branch (13). **Recency (R-1):** recent results revise a rate only through a named mechanism (velocity, IL, role, leash); the last game is the worst predictor measured.
3. **Channel audit.** Park, heat and same-park form are one "carry" channel; ERA, last-N starts and opponent split are one starter channel. Three or more same-signed adjustments moving the centre by over a run are netted in one line (control 26). Lineup changes go through PA by slot (27).
4. **Relief.** A named score-state ladder for both sides (20, 36); the starter-exit transition inning with "first relief inning concedes 2+" as mass (30); freshness is not quality (6); workload informs availability only.
5. **Environment.** Park and weather scale a budget both lineups already support (override 7). No automatic weather direction; rain is a termination-order branch (18).
6. **Endpoint.** Choose route A (final-score model) or route B (regulation + rules-versioned extras kernel) and label it (37). A regulation tie at exactly L adds at least one run under completion. P(tie after 9) is context (8.75% in 2026).
7. **Width.** The reference is 4.50. A total width below 3.8 names what the card knows (B-8, M31). Push mass comes from the conditional distribution, never a cap (35).
8. **One joint run object → every row** (§8.4). Use the negative binomial tables and the run-line shares in `PROBABILITY_TOOLKIT.md` §3, with the arithmetic shown, so the numbers reproduce (B-11, M14).

### 0.4 Row rules
- **Run lines (control 34).** P(fav −1.5) = w(1 − r); P(dog +1.5) = P(dog wins) + w·r. P(A +1.5) ≥ P(A ML) always. For a ±1.5 in the top two print P(fav by 2+), the exactly-one-run mass split by who bats last, and the early-hook mass for a starter back from the IL (29). The cushion is decomposed into win / lose by 1 / lose by 2+ (4). A low total is not a close margin (5, 17). BB-B9 late separation is represented before any cushion is Rank 1 (override 6).
- **+1.5 baseline.** 0.638 for either side, extras included; nine-inning away/home 0.617/0.659. A +1.5 stated below it claims information against that side and the departure ledger names it (B-9).
- **Totals.** An Under outranking its Over states why the BB-B2/B3 upper tail is subordinate (override 2). One team alone can clear a total (P-404, P-417). Print the median-based P(total ≤ line) for skewed totals and the venue row beside the line; opposing the venue row needs a named mechanism (35).
- **NPB/KBO/CPBL.** A team total at p ≥ 0.65 needs the opposing starter's log and the posted order (31a). A batting pitcher is an exposure branch (31b). An ERA-built centre adds back unearned runs and reconciles with team R/G and RA/G (TESTING `O-NPB-ERA-CENTRE`).
- **Strikeout-floor props (33):** exposure base, direct opponent split, early-exit branch with mass, settlement definition.
- **Winner.** Three-way in tie leagues (32). The winner label inherits the ranked rows' evidence (G-L21(3)).
- **First five innings (B-7):** mean 5.00, SD 3.29, P(tied) 0.154; an F5 moneyline or −0.5 carries the tie mass.
- **Openers.** The opener's first inning is width, not direction (B-4).

### 0.5 Ranking and track record
- Rank by **RM-1 q** (`PROBABILITY_TOOLKIT.md` §5). A baseball +1.5 carries no cushion penalty. Rank 1 is the highest q, **not a +1.5 by habit**. A typical slate is `TOP2_COIN_FLIP` or `LEAN`, and the delivery says so.
- STRONG rows available from the population alone: +2.5 (0.72–0.75), a low total line (Over 5.5, 0.76), or a total two or more runs from the card's own centre. They appear only as the card's own distribution prices them (`SLATE_ADVISORY`).
- Opposite +1.5 rows, and a moneyline plus the opponent's +1.5, are a `COVERING_PAIR`.
- **Track record:** MLB won 58.6% at a stated 0.596, resolution **0.0075** (the lowest of any sport), so the departure ledger is mandatory. NPB/KBO/CPBL won 64.3% at 0.623. NPB/KBO/CPBL Unders 11/14 against Overs 4/9 is `T-TOTAL-DIRECTION-LEAGUE` (non-binding). `C-RUN-CENTRE-BIAS` accrues with no tilt.
- **MLB shadow model (C-MLB-SHADOW): suspended for md-only operation (2026-09-28).** It is maintainer Python, which the model does not run. Print `SHADOW: NO_LANE (md-only)` at settlement. It was never a card input.

### 0.6 Settlement
- Three terminal lineages. The MLB gamefeed and boxscore (`SOURCES.md` §3.1) give the final, the regulation score when extras were played, decisions, box weather and the lineup diff (starters are the `X00` entries).
- NPB: the official page marker 【試合終了】, plus Sports Navi and Kyodo as lineages 2–3. KBO: the English scoreboard ("FINAL", W/L/S). Mynavi result pages are AI-generated: exclude them.
- Record runs in the starter-exit transition inning (30). Keep regulation versus extras attribution exact.

### 0.7 Reference numbers (2026; `BASE_RATES_REGISTER.md` §1–§3, §7.5)
League total mean 8.95–8.98, SD 4.51–4.53. One-run games 27.6–27.8% (nine-inning games 23.9%). P(margin ≥ 2) 72.2%. r = P(margin = 1 | win) 22.9–30.1% (nearly flat). Extras 8.75% of games, adding a mean of 2.88 runs; the final margin is one run 68.5% of the time after extras. Park identity explains 4.3% of total-runs variance. Population P(total > L): 5.5 0.757 · 6.5 0.686 · 7.5 0.572 · 8.5 0.491 · 9.5 0.398 · 10.5 0.329.

### 0.8 Withdrawn in baseball — never apply
Universal run-line caps (0.53/0.54) and the 12% push cap; fixed extras contributions and the "60% extras conversion"; second-highest/median pseudo-tails; path-count categories; 40–60% top-slot bands; normalised-edge ordering; rebound, hangover or "due" rules; doubleheader-G1 deflation; "dual run-line arbitrage"; the KBO velocity filter; "ace dominance"; three-start form as validation (P-453 was lucky).

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The MLB model (A1) is a team-only core. It was validated on Retrosheet 2022–2024 and was overconfident at v1 (20 prior games per team). v2 (120, selected on 2022) beat the population on results and totals in 2023–2024 and tied TB-1 on results; that test is not independent. **The independent 2025 test replicated it** (`T-MLB-V2-2025`): A1 − A0 = −0.0023 [−0.0042, −0.0005] over 2,121 games. The declared-starter term did not add skill on results (P1, 2026-09-26(e)). NPB, KBO and CPBL: **not validated**. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** MLB is the least predictable major league measured.
- **No STRONG favourites.** In 2026 the team model's favourite **never** reached 0.70; 90% of games sat at 0.50–0.60 (win Brier 0.247 against 0.250).
- **The starter term failed its test.** It was tested leak-free on 2025–2026 (probable starters are recoverable from statsapi, which corrects the earlier claim) and did **not** improve results (preregistered verdict: not demonstrated). It improved the 2026 totals only.
- **The cards held their own.** On 61 contracts from 34 MLB cards, the cards (0.238) were no worse than A1 (0.241), A1 with starters (0.241) or TB-1 (0.246).
- **Rank 1 in MLB is almost never STRONG.** Say so (`TOP2_COIN_FLIP`) rather than force it (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

### 0.9 Control index (full text in §4 and the dated sections)
1 short start is exposure · 2 run suppression keeps the HR tail · 3 pitch limit ≠ innings · 4 cushion decomposition · 5 low total ≠ close margin · 6 bullpen freshness ≠ quality · 7 post-trade regime · 8 trend mechanism · 9 gapped/overlapping lines · 10 home batting is state-dependent · 11 small-sample starter mixture · 12 identity before quality · 13 season prior v current regime · 14 defence and unearned-run tails · 15 joint hook-tail reconciliation · 16 strong opponent doesn't erase debut variance · 17 low-total separation · 18 weather termination order · 19 stable centres keep cluster risk · 20 score-state bullpen · 21 favourite separation and clusters linked · 22 extras rate environment · 23 prior series game is context · 24 game log beats aggregates · 25 rehab pitch ladder · 26 mechanism-overlap audit · 27 PA-weighted lineup exposure · 28 opponent starter full-game branch (as corrected 2026-09-12) · 29 run-line decomposition · 30 starter-exit transition inning · 31 NPB/KBO/CPBL team totals; batting pitcher · 32 tie-permitting end states · 33 strikeout-floor props · 34 run-line identity · 35 conditional total and exact push · 36 score-state relief ladder before a run line is Rank 1 · 37 regulation-to-completion endpoint. Receipts and references: B-1 official lineup · B-2 gamefeed weather · B-3 run-centre accrual · B-4 opener caution · B-5 freeze/settlement receipts · B-6 all-park rows · B-7 first five · B-8 width benchmark · B-9 +1.5 baseline · B-10 total direction by league · B-11 `PROBABILITY_TOOLKIT.md`.

### 0.10 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Under the numerical ML architecture (`runtime/src/sports/baseball/engine.py`):
1. **Event-First Modeling**: Plate appearance (PA) base-out Markov chain simulation:
   $$\text{Matchup (Pitcher vs Batter)} \longrightarrow \text{PA Outcome (1B, 2B, 3B, HR, BB, K, Out)} \longrightarrow \text{Base-Out State Transition} \longrightarrow \text{Runs}$$
2. **Hook and Relief Ladder**: Explicit starter pitch count/tbf leash and score-state relief transition inning.
3. **Regime Conditioning**: Pre-2008, 2008–2014, and 2015+ Statcast tracking regimes strictly demarcated; extra-inning ghost-runner regime (2020+) segregated.
4. **Independent Training**: Fit exclusively on `H0-BASEBALL-v1` via pybaseball/Statcast; D0 is strictly reserved for qualitative error diagnostics.


## 1. Identity and contract


Resolve league and level: MLB, NPB, KBO, LMB, WBSC, minor league, college, or another competition. Record season/rules era, venue, home batting entitlement, designated-hitter rule, scheduled innings, doubleheader format, extra-innings rule, probable/confirmed starters, and operator action/listed-pitcher terms.


For MLB, use the current official rule and technology environment. The 2026 ABS challenge system weakens transfer from old home-plate zone tendencies; do not use an umpire effect without current-system evidence.


## 2. High-value inputs


### Participants and exposure


- Complete the final starter-identity handshake for both sides against the official event page or official team/league release. Store event ID, team, role, participant ID/name and `CONFIRMED_OFFICIAL`/`PROBABLE_OFFICIAL`/unresolved status; never translate a same-day secondary preview into a confirmed starter.
- Confirm both posted batting orders, bench, catcher, defence, starters, and material absences. If official starters or orders are not released, model explicit participant mixtures and apply the general evidence cap rather than choosing one preview lineup.
- Estimate plate appearances by lineup slot.
- For each starter, model batters faced, pitches, innings, and hook point separately from runs allowed.
- For every relevant reliever, estimate availability probability and likely role. Build opener → bulk → bridge → leverage → low-leverage alternatives; workload informs availability, not performance.


### Starter and lineup process


Use the current arsenal against the current lineup:


- pitch mix, velocity, movement and location;
- K-BB%, whiff/chase, ground/fly-ball shape, HR, barrel/hard-hit and expected contact measures where valid;
- handedness and platoon shape;
- catcher, defence, park, and opponent quality;
- injury/return, pitch cap, rest, and recent mechanics.


ERA and WHIP are context, not a complete distribution. FIP/xFIP/xERA or league equivalents are supporting estimates with their definitions and limitations. Direct starter history receives weight only when current-lineup overlap and arsenal/role continuity are meaningful; never promote one prior start as ownership.


### Environment and context


Record park factors with year/rolling window, dimensions, roof, venue-local game-window weather, altitude, rest/travel, series state, and home last-bat. Hot air, humidity, rain, or wind has no automatic total direction. Officials, motivation, and press comments are conditional only.


## 3. Model


Exposure units are plate appearances, pitcher batters faced, pitches, innings, and live base-out state. Use a joint team-run distribution with overdispersion and explicit sequencing/HR tails rather than a naive homogeneous Poisson.


Build:


1. starter run-rate and exit distributions;
2. the named relief-chain distribution;
3. lineup PA and matchup rates;
4. park/weather/defence adjustments;
5. home-ninth, extra-innings, and score-state branches.


Derive winner, run line, team total, game total, and player contracts from that same distribution.


For numerical training, compare empirical and Poisson/negative-binomial team-run baselines with a plate-appearance/base-out A2 simulator. The structural candidate samples starter batters faced/hook state, the named relief chain, PA outcomes, base/out transitions, sequencing and HR clusters, home-ninth entitlement and extra innings. A bivariate/direct score model or boosted distribution is a challenger only after covariance, overdispersion, support, era and tail checks. All totals, run lines and winners integrate the same joint run distribution; line-specific binary classifiers cannot become the primary engine. All candidates remain unfit and unvalidated.


## 4. Structural controls


1. **Short start is exposure, not an automatic Over.** More bullpen innings raise uncertainty; direction depends on the likely arms and lineup.
2. **Recent run suppression does not erase the HR/contact tail.** Record central and short-start/two-homer branches.
3. **Pitch limit and innings are separate.** Efficiency, baserunners, plate-appearance length, and quick outs determine how far a pitch cap travels.
4. **Cushion decomposition.** For every +1.5 line record win, exactly-one-run loss, and 2+-run loss branches.
5. **Low total does not imply close margin.** One dominant starter and clustered damage can produce a multi-run Under.
6. **Bullpen freshness is not quality.** Name the likely chain and manager alternatives.
7. **Post-trade or role-change regime.** Rebuild catcher, arsenal, velocity/location, mechanics, role, and current-lineup fit.
8. **Trend mechanism.** Classify recent totals by starters, lineups, contact/HR, errors, relief chain, park and weather before using an Under/Over run.
9. **Gapped/overlapping lines.** Map every interval; opposite-team positive run lines can both win, and alternate totals can overlap.
10. **Home batting exposure is state-dependent.** Derive ninth-inning entitlement from the score distribution; do not apply a fixed innings fraction.
11. **Small-sample starters require a mixture.** A debut, return, young starter, opener, or one-start sample is pooled toward the league/role prior with explicit good-start, ordinary, early-hook and contact/HR tails. One good outing cannot collapse that uncertainty.
12. **Starter identity precedes starter quality.** No ERA, arsenal, platoon or hook analysis is decision-driving until the starter is linked to the exact official event/team role at the final volatile refresh.
13. **Season prior versus current starter regime.** When recent arsenal/velocity/location, role, opponent quality or contact indicators conflict with season ERA/reputation, retain a shrunk season/league prior and an explicit current-regime branch. State why each branch is weighted; do not let either a famous season line or a short hot/cold run win silently.
14. **Defence and unearned-run tails stay in the score tree.** Team fielding quality may adjust the baseline, but one game's error cluster is a realised tail unless a current personnel/positioning mechanism made it forecastable. Do not backfit a generic error penalty from a single final.
15. **Joint hook-tail reconciliation.** When either starter is debut/small-sample/returning or both starters have wide exit distributions, construct the joint early-hook branch: batters faced, inherited runners, first available relief arms, bullpen innings, contact/HR cluster and home-ninth exposure. Before an Under can outrank its Over, state why that joint upper tail remains subordinate; otherwise lower evidence or change the order.
16. **Strong opponent starter does not erase debut variance.** A favourable opposing-starter matchup may shift the centre, but it cannot collapse a rookie/first-starter's ordinary and early-hook branches. Both teams' exposure mixtures survive into the total and margin distribution.
17. **Low-total separation remains explicit.** For each underdog +1.5 or favourite -1.5 row in a low-total game, retain shutout and 2–0/3–0/4–1-style one-sided branches. Low expected runs do not mechanically create a close margin.
18. **Weather termination has an event order.** Under the competition's official-game and operator-action rules, separate runs-before-stop, stop-before-runs, restart/relief-transition and void/no-action branches. Rain or a shortened final is not mechanically an Under once a clustered inning has already crossed the line.
19. **Stable starter centres do not remove cluster risk.** Even when both starters have established central projections, retain walks/errors, sequencing, multi-run homer, inherited-runner and first-relief-transition branches. The upper tail is a joint inning/relief state, not only an “early hook” label.
20. **Bullpen availability is score-state specific.** Map starter/opener → bulk/middle → tied/leading leverage → one-run trailing → multi-run trailing arms, with inherited runners and prior workload. A rested closer does not protect a side or +1.5 line if the likely game state never triggers his entry.
21. **Favourite separation and run clusters are linked.** When the favourite's offensive/HR ceiling and the opponent's starter-to-middle-relief transition drive both the Over and a multi-run win, stress those outcomes jointly. Do not describe the favourite run line and upper total as unrelated remote tails while ranking the underdog cushion first.
22. **Extra innings are a different rate environment, not more of the same innings.** Under a rule that seeds each extra half-inning with a runner already in scoring position, assign the tie-after-nine branch its own materially higher per-inning run distribution (RULES_GENERAL (archived) §11.3, G22; branch `BB-B7`). A correct nine-inning read can still lose a total or a run line once the game reaches that state; quantify the probability of reaching a tie after nine separately from the extras scoring rate itself.
23. **A prior game in the same series is context, not a cause.** A team's result in the immediately preceding game of the same series requires a named, currently active mechanism — the specific starter/bullpen usage it created, a lineup or rotation change it triggered, or comparable evidence — before it may support either a "bounce back"/"response" lean or a continuation lean for today's game, per RULES_GENERAL (archived) §11.3E (G17.1). Record the series score and the disclosed bullpen/lineup consequence of the prior game(s) under the series-state block (RULES_GENERAL (archived) §5); a prior blowout or a prior close loss is not itself evidence for today's direction.


## 5. Live state


Store inning/half, score, outs, base state, current pitcher/pitch count, bullpen behind him, lineup slot due, challenges/reviews, weather/roof, and home batting entitlement. Recalculate remaining PA and named pitcher/reliever branches.


## 6. Sources and settlement


- MLB official StatsAPI and MLB match centres control schedule, lineups, live state, box score, transactions, and final.
- [MLB Statcast glossary](https://www.mlb.com/glossary/statcast) controls Statcast definitions; Baseball Savant supplies park and batted-ball data.
- NPB.jp/BIS, KBO, CPBL official/advanced game pages, LMB.com.mx, WBSC, and official league/team sources control their competitions. Each league remains a separate source/definition population.
- Government weather services and official roof reports control game-window conditions.


Settle from the official final and named statistic provider. Preserve extra-innings and listed-player rules. Recheck documented official stat corrections for props.


## 7. Upcoming-game research sequence


1. Freeze league/rules era, scheduled innings, home-last-bat/extra-inning terms, listed-pitcher/action rules and full candidate slate.
2. Retrieve official probable/confirmed starters, posted orders, catcher/defence, transactions/injuries, roof and park-local weather; refresh lineups, starters, roof and weather before issue.
3. Model lineup PA, starter batters faced/pitch/inning/hook distribution, current arsenal versus lineup, the named bullpen chain, base-out transitions, sequencing/HR clusters, park/defence and home-ninth/extras. If either starter is debut/small-sample or both exit distributions are wide, stress their joint early-hook/relief/cluster branch before ordering the total.
4. Maintain MLB, NPB and KBO as separate priors/rules/data cards; MLB Statcast-era measurements cannot be silently transferred to another league or earlier tracking regime.
5. Derive winner, total, team totals and run lines from the joint run object. Pitcher/batter props use action probability and their own PA/batters-faced/event-rate targets.


Official league/team sources control lineups, starters, rules and finals. Statcast/Savant controls only its defined MLB tracking metrics; projections are external challengers, not labels or ground truth.


## 8. SFA-BASEBALL — sport forecast algorithm


Algorithm ID: `SFA-BASEBALL`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with baseball content. It is a process composition of promoted controls and §4 above; it introduces no fitted weight, scenario weight or published probability. MLB, NPB, KBO, CPBL, LMB, MiLB and other leagues remain separate populations at every step.


### 8.1 Blocking preconditions


Resolve these before any rate work. Each maps to a `GFA-2` gate.


| Precondition | Requirement | Failure output |
|---|---|---|
| `BB-P1` starter identity | Both starters carry `(official_event_id, team, SP, participant)` with `CONFIRMED_OFFICIAL` or `PROBABLE_OFFICIAL` from the field owner, re-handshaken at G31 | No ERA, arsenal, platoon or hook analysis is decision-driving; the affected rows cap at `FORCED RANK` / `MEDIUM-LOW` and the starter is carried as a mixture |
| `BB-P2` batting orders | Both posted orders, catcher, defensive alignment and material absences | Model lineup mixtures; slot-PA, platoon-cluster and player rows cap under RULES_GENERAL (archived) §11.5 |
| `BB-P3` league and rules era | League, scheduled innings, extra-innings rule, designated hitter rule, listed-pitcher and action terms, roof status | `GATE-TARGET` failure; do not proceed |
| `BB-P4` termination terms | Official-game rule and the operator's suspension/shortening/action rule where supplied | Label `UNKNOWN_DEFINITION`; keep the termination branch explicit |
| `BB-P5` home-last-bat | Which side bats last, and whether the contract endpoint includes extras | Required before any total or run-line is located |


### 8.2 Exposure chain


Run in order. Each step consumes the previous step's output; none may be skipped by asserting a team-level number.


| Step | Output |
|---|---|
| `BB-S1` | Lineup plate-appearance budget by slot for the scheduled innings, both sides |
| `BB-S2` | Starter batters-faced, pitch and inning distribution with an explicit hook point — modelled separately from runs allowed |
| `BB-S3` | Current arsenal against the current lineup: pitch mix, velocity/location, K-BB%, whiff/chase, batted-ball shape, barrel/hard-hit, home-run shape, handedness and platoon clusters |
| `BB-S4` | Named relief chain as a score-state ladder: opener, bulk, bridge, tied/leading leverage, one-run trailing, multi-run trailing, low leverage — each with availability probability, inherited-runner exposure and prior workload |
| `BB-S5` | Park factor with window, dimensions, roof, venue-local game-window weather, altitude, defence and catcher effects |
| `BB-S6` | Base-out transitions, sequencing and home-run cluster structure |
| `BB-S7` | Home-ninth entitlement derived from the score distribution, plus the extra-innings branch under the exact rule |
| `BB-S8` | One joint team-run object with overdispersion, from which winner, run line, team totals, game total and player rows are queried |


Workload informs availability, never performance. A rested arm that the likely score state never summons has no protective value.


### 8.3 Mandatory branch set


Every baseball card represents all nine states, with each supplied line located against them.


| Branch | Content |
|---|---|
| `BB-B1` | Both starters at their central length and run rate |
| `BB-B2` | Joint early-hook state: either or both starters exit early, with the first available arms and inherited runners named |
| `BB-B3` | Multi-run home-run or sequencing cluster inside one inning |
| `BB-B4` | One-sided separation with the opponent floor at nought to two runs — the low-total, wide-margin family |
| `BB-B5` | Relief-transition inning where the score state changes which arms appear |
| `BB-B6` | Home-ninth not batted because the home side leads, capping the total |
| `BB-B7` | Extra innings under the exact competition rule, modelled with that rule's own scoring-rate environment (for example a runner placed at second to open each half-inning materially raises the per-inning scoring rate above a regulation inning; do not extrapolate the nine-inning rate into extras under such a rule) |
| `BB-B8` | Termination order: runs before stop, stop before runs, restart and relief transition, official-game and no-action states |
| `BB-B9` | Late separation: the game is inside one run entering the last third and the margin expands by two or more runs after both starters are gone, through the relief chain, a home-run cluster or a bullpen collapse on one side only |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Game total | Joint run object, both teams | The component budget in RULES_GENERAL (archived) §11.4 G20, solved at the opponent floor, centre and ordinary high |
| Team total | Team marginal of the same object | Own-lineup exposure against the exact opposing starter and the arms that actually reach those innings |
| Run line and cushion | Margin marginal | Win, exactly-one-run loss and two-or-more-run loss branches stated separately |
| Winner | Margin sign, including home-ninth and extras | Not inferable from the total |
| Pitcher props | Batters faced and pitch budget from `BB-S2` | Hook risk and lineup turn count, not season rate |
| Batter props | Slot plate appearances from `BB-S1` | Opposing starter and the relievers that reach that slot |


**Worked run-line slate — you rank every row, you do not pick one.** A book that lists `Team A +1.5 / Team A ML` and `Team B −1.5 / Team B ML` has supplied **four** contract rows (plus the total pair). The question is never "which do I choose" — it is "rank all four by marginal win likelihood and robustness" (RULES_GENERAL (archived) §6, and §3: never replace the supplied slate with an easier market). The prices attached (e.g. `+1.5 @ 1.67`, `ML @ 2.50` for A; `−1.5 @ 2.10`, `ML @ 1.67` for B) are **recorded as metadata with a capture time and play no part in the forecast or the rank** — `SPORTS_ONLY / MARKET_BLIND` (§4 bookmaker-independence hard gate).


The four rows collapse to **two independent quantities** from the joint run object: `p_win = P(Team B wins)` and `p_one = P(the margin is exactly 1)`. Then, deriving from the same distribution (coherence is mandatory — G25.1):


| Row | Wins when | Probability |
|---|---|---|
| `Team B ML` | B wins by 1+ | `p_win` |
| `Team B −1.5` | B wins by 2+ | `p_win − P(B wins by exactly 1)` |
| `Team A +1.5` | A wins, or loses by exactly 1 | `1 − (p_win − P(B wins by exactly 1))` |
| `Team A ML` | A wins by 1+ | `1 − p_win` |


So `P(Team A +1.5) ≥ P(Team A ML)` and `P(Team B −1.5) ≤ P(Team B ML)` **always** — a rank order that violates this is an incoherence defect. The ordering then follows the game shape you forecast: a likely multi-run favourite game ranks `B ML ≈ B −1.5` above `A +1.5 > A ML`; a coin-flip game likely decided by one run ranks `A +1.5` and `B ML` up and both `−1.5 / underdog-ML` rows down (§4 control 4 cushion decomposition; §8.6 override 3). The **potential winner** is a separate single call with its endpoint stated (regulation vs eventual winner incl. extra innings; no automatic runner in the MLB postseason — §9.2).


### 8.5 Kill-path library


Each row names a mechanism, not an outcome, and the contracts it defeats. Use it to populate `kill` in the row robustness record.


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Multi-run home-run cluster in a single inning | Under; and the underdog cushion when the cluster lands for the favourite | L-006, C-PL7-BB-HOOK-TAIL, C-PL9-BB-SCORESTATE-RELIEF |
| Early hook plus first relief transition with inherited runners | Under; and the side resting on starter quality | T-004, T-005, C-PL4-BB-SMALL-SAMPLE-STARTER |
| Opponent scoring floor near nought to one run in a low-total game | The positive run-line cushion, while the Under still wins | §4 control 17, C-PL9-BB-SCORESTATE-RELIEF |
| The closer never enters because his club trails | Any row justified by generic bullpen freshness | C-PL9-BB-SCORESTATE-RELIEF |
| Rain or curfew arriving after runs have already scored | The assumption that shortening implies Under | C-PL8-BB-TERMINATION-ORDER, §4 control 18 |
| Home side leads and does not bat in the ninth | Over, by removing scheduled exposure | §4 control 10 |
| A debut or small-sample starter delivering his ordinary good outing | An Over resting on projected rookie collapse | §4 control 11, C-PL4-BB-SMALL-SAMPLE-STARTER |
| Joint favourite separation and upper total, positively dependent | The framing that an underdog cushion and the Over are unrelated remote tails | §4 control 21, C-PL7-BB-HOOK-TAIL |
| Post-starter separation in a game the starters kept close | Any underdog cushion whose support is a close-game or head-to-head-margin narrative rather than a budgeted relief-inning margin | `BB-B9`, C-PL11-BB-SEPARATION-BUDGET (P-247) |
| The underdog's own offence supplies the Over | An Under ranked from the favourite's cooled scoring, and any pairing of an underdog cushion with that Under | C-PL11-BB-UNDERDOG-TAIL (P-248) |
| A hitter-friendly park failing to manufacture runs that neither lineup's exposure supports | An Over ranked from venue reputation rather than a two-team component budget | C-PL11-BB-VENUE-RESTRAINT (P-244) |
| Walk-off in a tight low-total state | A road side in a one-run corridor | §4 control 10; local lesson `M4-L10` in PREDICTION_MINI_LOG_4.md §E |


### 8.6 Sport ordering overrides


These refine `GFA-2` G24 within baseball; they never reverse a `GFA-2` gate.


1. A short start raises relief exposure and therefore uncertainty. It is not directional, so it may not move a total's `corridor` classification by itself.
2. Before an Under outranks its Over, state why the joint `BB-B2`/`BB-B3` upper tail is subordinate. If that cannot be stated, lower evidence or change the order.
3. Before a positive run line outranks the opposing side, state which `BB-B4` separation scores are excluded and why. A low total is not evidence for a close margin.
4. Recent earned-run averages, Under runs and cover counts are `E — diagnostic only`. They may not supply a decisive term in the G23.1 marginal-likelihood comparison.
5. When both starters are established but the lineups carry power, `BB-B3` still applies. A stable centre does not remove cluster risk.
6. A run-line or cushion row is budgeted across the starter innings and the post-hook relief innings separately under G20.1, then against the home-ninth entitlement and the extras branch. State which relief innings can produce a two-or-more-run swing and why the cushion survives them. `BB-B9` must be represented before any cushion is ranked first.
7. A park or altitude factor scales a component budget that both lineups' exposure already supports. It may never supply runs that neither `BB-S1`–`BB-S4` chain produces, and venue reputation is `E — diagnostic only`.
8. A weak, rehabilitating, returning or small-sample starter attaches to the **opponent's** scoring branch under G14.1. It does not widen both teams' run distributions, and a stale season line on one side does not outrank the opposing starter's current-regime run prevention.
9. When an underdog run-line cushion is ranked first, the total is re-solved conditional on that state under G25.1: the branches that keep the underdog inside the line are branches in which the underdog scores, so the underdog's own upper tail enters the total before an Under may be ranked above the Over.


### 8.7 Pre-issue checklist


1. `BB-P1`–`BB-P5` status printed, with release status per starter.
2. Slot plate-appearance budget and both hook distributions stated.
3. Score-state relief ladder named, arm by arm, with inherited-runner exposure.
4. All nine `BB-B*` branches represented; component budget solved at the supplied total.
5. Kill-path rows selected from §8.5 and reconciled against the issued order.
6. Home-ninth and extras treatment stated for every total and margin row.
7. Termination branch stated whenever weather or curfew is live.
8. Lineups, starters, roof and weather refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Field-relative wind bearing, roof state and umpire crew pulled from the official game feed.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row across the starter innings and the post-hook relief innings separately, then the home-ninth entitlement and the extra-innings branch.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a post-starter multi-run relief inning.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.
17. Streak persistence-versus-reversion audit (G17.1) recorded for every hot/cold offensive or pitching run and for any prior-game/series "response" lean; extra-innings branch (`BB-B7`) modelled at its own rule-defined scoring rate, not the nine-inning rate, whenever an automatic-runner or similar rule applies.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Team run production | Runs scored and allowed per game, split against right- and left-handed starters |
| Team contact quality | Team hard-hit, barrel and home-run rate, and strikeout and walk rate, opponent-adjusted |
| Each named starter | That starter's own last 5/10/15/20 starts: innings, batters faced, pitches, hook point, home runs allowed, K-BB% |
| Bullpen load | Innings and appearances for each likely relief arm over the last 5 and 10 days, with back-to-back flags |
| Target-relevant output | How often the team total, game total and run line at this line would have settled in each window |


**Head-to-head continuity.** Continuity for baseball means the same starters, the same park and the same season roster. Two teams meeting for the fourth time in a series with different starters each day are four different matchups, and the head-to-head window is close to worthless unless the pitching matchup repeats.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **OUTDOOR unless the venue has a roof**.


| Field | Use in this sport |
|---|---|
| Field-relative wind | `statsapi.mlb.com` `v1.1/game/{gamePk}/feed/live` exposes `gameData.weather.wind` as a bearing relative to the field, for example "10 mph, Out To RF". Prefer it over any city forecast |
| Roof state | `gameData.venue.fieldInfo.roofType`, refreshed at G31 because roofs close late |
| Temperature and humidity | Ball carry; combine with park dimensions before any home-run branch |
| Hourly precipitation | Feeds the `BB-B8` termination branch and the official-game rule, never an automatic Under |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor totals on the park-and-era run environment at that line, and run lines on the league frequency of one-run and two-or-more-run margins. A +1.5 run line and a game total are different propositions and never start level.


StatMuse is an accepted research accelerator for this sport under `SOURCES.md`, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Umpire crew | `liveData.boxscore.officials`; the plate umpire is a strike-zone and pace factor, conditional and only with current data |
| Park factors with window | Recorded with the year or rolling window, never as a bare label |
| Catcher framing and defensive alignment | Affects the same starter differently by battery |
| Home-last-bat entitlement | Derived from the score distribution at `BB-S7`, not a fixed innings fraction |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. This section is a standing reference for the playing laws of baseball and the competition-specific rules of every baseball league that appears in the prediction logs. It supports `BB-P3`/`BB-P4` (league and rules era, termination terms) and §6 settlement; it introduces no rate, weight or ordering rule. Where a 2026 rule is cited, it is the rule in force for the 2026 seasons covered by the current log. Verify the rules era for any event outside 2026 — leagues change tie, roster, DH and postseason rules frequently.


**Maintenance (RULES_GENERAL (archived) §3, `G2`).** Before the first card of a new season, spring training / pre-season, or postseason for any league here — MLB, NPB, KBO, LMB, MiLB and the international events all start at different times of year — re-verify the tie/extra-innings rule, the ball-strike technology in force, the import and active-roster rules, the DH rule, the pitch-clock/pace values and the postseason bracket against the official league source, and update this section **before** issuing the card. The first time a new baseball competition is forecast (a winter league, a new international event, another domestic league), document its full rules here first.


### 9.1 Universal playing rules (all baseball)


**Objective and structure.** Two teams of nine alternate on offence (batting) and defence (fielding). A game is scheduled for **nine innings**; each inning has a top half (visiting team bats) and a bottom half (home team bats). A half-inning ends when the fielding team records **three outs**. The team with more **runs** after the last scheduled out wins.


**Scoring a run.** A run scores when a baserunner legally touches first, second, third and home plate in order before the third out of the inning. A run does **not** count if the third out is a force out, a batter-runner put out before reaching first, or a preceding runner passing another — this is the "time play" rule and matters for totals settlement on the final play.


**Home-team last bat.** If the home team leads after the top of the ninth, the bottom of the ninth is not played. If the home team scores the go-ahead run in the bottom of the ninth (or any later inning), the game ends immediately ("walk-off") — the winning margin is capped at the runs needed plus, on a home run, the batter and any runners. This is why a home favourite can never "cover" a large run line in a game it walks off by one.


**The count.** Each plate appearance is a contest of **balls** (pitches outside the strike zone not swung at) and **strikes** (pitches in the zone, swung on and missed, or fouled with fewer than two strikes). Four balls = a **walk** (batter to first). Three strikes = a **strikeout**. A foul ball with two strikes is not a third strike (except on a bunt).


**Reaching base:** hit (single/double/triple/home run), walk, hit-by-pitch, fielder's choice, error, dropped third strike, catcher's interference.


**Being put out:** strikeout, ground/fly/line out caught, force out, tag out, appeal (missed base, left early on a fly), interference, running out of the baseline.


**Batting order and substitution.** Nine hitters bat in a fixed rotation. A substitute takes the replaced player's lineup slot. **A player removed from the game cannot re-enter** (no re-entry in professional baseball). Pinch hitters and pinch runners are common; a pitching change mid-inning is unlimited subject to the three-batter minimum (below, where adopted).


**Designated hitter (DH).** Where adopted, a tenth player bats in place of the pitcher every time the pitcher's slot comes up, without playing the field. The "Ohtani rule" (MLB, and most DH leagues) lets a team keep the DH when its starting pitcher is also the DH and is later removed as pitcher.


**Pitching.** The starter must face at least one batter (or, where adopted, three — see below). Relievers enter freely between batters. A **balk** (illegal pitching motion with runners on) advances all runners one base.


**Weather, official games and suspensions.** A game called by weather is an **official game** once the trailing team has had a chance to complete five innings (4½ if the home team leads) — earlier than that it is a "no game" and (in most competitions) replayed in full. Modern MLB/MiLB rules make most weather-shortened or interrupted games **suspended** and resumed from the point of stoppage rather than reverted; older eras and many other leagues revert to the last completed inning. The termination-order branch (`BB-B8`, §4 control 18) is decided by the competition's official-game rule, not by an assumption that "shortened = Under."


**Mercy / run rule.** Not used in MLB, NPB, KBO or LMB regular seasons. Used in WBSC/college/high-school/some winter leagues (typically 10 runs after 7 innings, 15 after 5).


**Doubleheaders.** MLB doubleheader games are nine innings (the 2020–2021 seven-inning rule was discontinued). MiLB doubleheader games remain **seven innings** each. Some winter/independent leagues also use seven.


### 9.2 MLB (Major League Baseball)


**Structure.** 30 clubs, two leagues (AL/NL), three divisions each. **162-game** regular season. Universal **DH** since 2022 (both leagues).


**Rosters.** 26 active players (28 from September 1), with a **13-pitcher maximum** (14 in September); 40-man roster; injured lists (15-day, 60-day, 7-day concussion, 15-day pitcher minimum). Option rules govern MiLB movement. Postseason rosters are **set separately for each round** (26 players), so bullpen composition can change between the Wild Card Series and the LDS.


**Pace-of-play (in force 2023–2026).** Pitch timer **15 seconds** bases empty, **18 seconds** with a runner on (Triple-A 14/19 in 2025, tweaked 2026); a violation is an automatic ball, or an automatic strike on the batter if not set and looking at the pitcher with 8 seconds left. **Two pickoff/disengagement attempts** per plate appearance (a third that fails to retire the runner is a balk). **Five mound visits** per team per nine innings. **Three-batter minimum** for pitchers (must face three batters or end the half-inning). **Shift restriction**: four infielders, two on each side of second base, on the infield dirt at the pitch. **18-inch bases** (up from 15). Base coaches must stay in the box until the pitch is delivered (enforced from 2026).


**ABS challenge system (new for 2026).** Full automated ball-strike calls are **not** used; instead each team gets **two challenges** of the home-plate umpire's ball/strike call per game. Only the **pitcher, catcher or batter** may challenge, immediately after the pitch, by tapping the helmet/cap, with no help from the dugout. A successful challenge is **retained**; an unsuccessful one is lost. In extra innings a team that used both challenges gets **one per extra inning** (non-accumulating); a team that kept both keeps both. Applies in the regular season and postseason. The personalised strike zone is set from measured player height and is slightly smaller than the umpire-called zone — this weakens transfer from pre-2026 umpire/framing tendencies (§1).


**Extra innings.** Each half-inning from the 10th begins with an **automatic runner on second base** (the player who made the last out of the previous inning, or a pinch runner). **Regular season only** — the automatic runner is **not** used in the postseason, where extra innings are played under standard rules with no inning cap. This makes the tie-after-nine branch (`BB-B7`) a materially higher-scoring environment in the regular season and an ordinary-inning environment in October.


**Standings and tiebreakers.** Since 2022 there is **no tiebreaker game** (no "Game 163"). Ties for a playoff spot or seed are broken by (1) head-to-head record, (2) intradivision record, (3) record vs. the relevant opponent group, (4) second-half record — mathematically, before the season ends.


**Postseason (2022 format, in force 2026).** **12 teams** — three division winners and three Wild Cards per league. The **top two division winners in each league get a first-round bye**. **Wild Card Series**: best-of-three, all games at the higher seed. **Division Series (LDS)**: best-of-five (2-2-1). **Championship Series (LCS)**: best-of-seven (2-3-2). **World Series**: best-of-seven (2-3-2), home field to the pennant winner with the better regular-season record. Home-field advantage within each earlier round goes to the higher seed. No mercy rule, no tie games, no automatic runner.


**Settlement conventions (MLB).** "Official game" for most bet types is **5 innings** (4½ if the home team is ahead); many books void full-game bets that do not reach 8½/9 unless already decided. **Listed pitcher** bets void if a named starter is changed; "action" bets stand. Run line is **−1.5 / +1.5**. Game totals **include extra innings**; **first-5-innings (F5)** markets settle at the end of the top of the 5th / bottom of the 5th and exclude the automatic runner and late bullpen. Suspended games: most books settle when the game is completed (even a day later); some void if not completed within a set window.


### 9.3 NPB (Nippon Professional Baseball, Japan)


**Structure.** 12 clubs in the **Central League** and **Pacific League**, six each. **143-game** regular season plus ~18 interleague games in a late-May-to-mid-June window.


**Designated hitter.** **Pacific League uses the DH; Central League does not** (Central League pitchers bat). The Central League has announced it will **adopt the DH from 2027** — for any 2026 Central League card the pitcher still hits, which affects the bottom of the order and the double-switch. Interleague and the Japan Series use the DH in all games.


**Tie games.** Regular-season games are capped at **12 innings**; still level after 12 = an official **tie** (no winner). Ties are excluded from winning percentage (the Japanese standings metric). The 2020–2021 no-extra-innings pandemic rule has been discontinued. **Climax Series and Japan Series** games are capped at **15 innings**, then tie (and are replayed / added to the series as needed).


**Rosters.** A ~70-player club control list; roughly **29 registered** with the top team ("ichi-gun") and **25 in uniform / eligible** for a given game. **Foreign-player limit: four on the active roster**, of whom no more than three may be pitchers and no more than three position players (so a 4-import active roster must mix). No pitch timer (trialed in the minors / second team). Three-batter minimum adopted.


**Postseason — Climax Series.** Each league's top three qualify. **First Stage**: 2nd vs. 3rd, **best-of-three**, all games at the 2nd-place club, no ties advantage. **Final Stage**: First Stage winner vs. the **pennant winner**, played at the pennant winner's park, effectively **best-of-seven but the pennant winner starts 1–0** (needs 4 wins from a possible 6 games; the challenger needs 4 of 6). **Japan Series**: best-of-seven (2-3-2), DH in all games, 15-inning tie cap. No mercy rule.


**Settlement note.** Because a regulation NPB game can end **tied**, moneyline/side bets need a stated tie rule (push, or "tie no bet"); this is unlike MLB. Totals settle on the 12-inning final. Draw is a live outcome for any NPB regular-season winner market.


### 9.4 KBO League (South Korea)


**Structure.** 10 clubs, single table, no divisions. **144-game** regular season, roughly late March to early October, no Monday games. Universal **DH** (KBO has always used it).


**Tie games.** Since **2025**, regular-season games are called a **tie after 11 innings** (previously 12), to limit pitcher workload. Ties are excluded from winning percentage and games-behind. Postseason games are called a tie only **after 15 innings**.


**Technology and pace.** KBO uses a **full Automated Ball-Strike System (ABS)** — every pitch is called by the automated zone and relayed to the umpire — **since 2024** (this is a full auto-call, not the MLB challenge model). Pitch clock since 2024, revised for 2026 to **18 seconds** bases empty and **23 seconds** with runners on; pickoff limits and larger bases also adopted. Three-batter minimum.


**Rosters.** 28-player first-team roster (26 dressed for a game in recent seasons); expanded in September. **Foreign players (2026):** three standard imports **plus one** additional player from an Asian country or Australia under a new "Asia quota" — **all four may appear in the same game**. Spending caps apply (roughly US$1m first-year total per standard new import; US$200k total for the Asia-quota player).


**Postseason — step-ladder.** Top **five** teams qualify. **Wild Card**: 4th vs. 5th — the 4th seed needs **one win**, the 5th seed needs **two** (effectively best-of-three with 4th starting 1–0). **Semi-Playoff**: WC winner vs. 3rd, **best-of-five**. **Playoff**: Semi-Playoff winner vs. 2nd, **best-of-five**. **Korean Series**: Playoff winner vs. **1st** (which has rested throughout), **best-of-seven**. Higher seed has home advantage and the rest edge at every rung. No mercy rule.


**Settlement note.** As with NPB, a **tie is a live regular-season outcome** (after 11 innings) — KBO side/handicap bets need a stated tie rule. KBO totals are settled on the 11-inning final in the regular season.


### 9.5 LMB (Liga Mexicana de Béisbol)


**Structure.** A large league (about 20 clubs) split into **Zona Norte** and **Zona Sur**. Regular season runs roughly April–July (schedule length has varied; ~90+ games per club in 2026), then a four-round postseason July–September. Summer heat and altitude are significant (Mexico City ~2,240 m, Puebla, Saltillo). **DH** used.


**Rosters.** 38-player list. **Foreign-player limit: 18** of the 38 for 2026–2027 (reduced from 20); **minimum 20 Mexican-born** players on the 38-man list. This is by far the most import-heavy of the leagues in this register — LMB rosters are close to half non-Mexican.


**2026 rule changes.** LMB adopted an **ABS challenge system** for 2026: **two challenges** per team over nine innings, retained if successful, **one extra challenge per extra inning**. **Three-batter minimum** for all pitchers. **No automatic runner** in extra innings (this was mistakenly applied by umpires in the opening series and publicly corrected — LMB extra innings are played under standard rules).


**Postseason.** Four best-of-seven rounds: **Primer Playoff** (six qualifiers per zone), **Series de Zona** (the three Primer Playoff winners per zone plus the best losing team as a wild card), **Series de Campeonato** (zone final, producing the Zona Norte and Zona Sur champions), and the **Serie del Rey** (Norte champion vs. Sur champion for the title). Seeding by winning percentage, then **run differential**.


**Settlement note.** Confirm the exact schedule/round in force — LMB has changed its playoff qualifier count and regular-season length repeatedly. A "Serie de Campeonato" or "Serie del Rey" game is best-of-seven with standard extra innings.


### 9.6 MiLB and Triple-A (Pacific Coast League)


**Placement.** Triple-A is one level below MLB. The two Triple-A leagues are the **Pacific Coast League (PCL)** and the **International League**. The PCL is a notoriously extreme **hitting environment** — Albuquerque, Las Vegas, Salt Lake, Reno and El Paso are high-altitude or hot-and-dry parks; PCL run environments do not transfer to MLB or to the International League.


**Rules.** Triple-A runs **ahead of** MLB as the rules laboratory, so most MLB rules apply and some are stricter: pitch timer (14 sec bases empty / 19 with runners in 2025, adjusted 2026; a batter timeout resets the clock at Double-A/Triple-A), **automatic runner** in extra innings, **larger bases**, **shift limits**, **three-batter minimum**, pickoff limits. **ABS**: Triple-A has trialed both a full auto-call zone and the challenge system in recent seasons; the **challenge system** is the current Triple-A model, and a **checked-swing challenge** was added to the PCL from **6 May 2026**. **Doubleheaders are seven innings.** Rookie-level games are frequently seven innings due to pitching shortages.


**Rosters and data.** ~28-player active rosters with constant MLB churn (optioned players, rehab assignments, "taxi" moves) — participant identity is more volatile than MLB and must be re-handshaken late (`BB-P1`). Statcast-grade tracking is **not** available at every Triple-A park; treat PCL batted-ball and velocity data as lower-fidelity than MLB (`SFA-BASEBALL` §8.4, and RULES_GENERAL data-priority).


**Postseason.** A single Triple-A National Championship Game between the PCL and International League champions (regular-season-split winners), plus a longer late-season "Triple-A Final Stretch" in some years. Confirm the current structure for any postseason card.


### 9.7 International baseball (WBSC / WBC / Premier12 / Olympics)


Not directly forecast in the current log but the identity template must handle it. Common features: **pool play then knockout**; a **mercy rule** (typically 15 runs after 5 innings, 10 after 7); an **extra-innings tiebreaker** that places runners on **first and second** (not just second) to open each half-inning from the 10th, sometimes with a re-set lineup; **pitch-count limits and mandatory rest** (WBC pitch-smart rules); 28-player rosters. Each event is its own rules era and its own population — do not transfer MLB/NPB/KBO rates into it.


### 9.8 Cross-league settlement and identity checklist (baseball)


| Question | MLB | NPB | KBO | LMB | Triple-A |
|---|---|---|---|---|---|
| Regulation length | 9 | 9 | 9 | 9 | 9 (7 in DH games) |
| Tie possible in regulation/standings? | No | **Yes** (after 12) | **Yes** (after 11) | No | No |
| Automatic runner in extras | Reg. season only | No | No | **No** | Yes |
| Extra-innings cap | None (reg. + post) | 12 reg. / 15 post | 11 reg. / 15 post | None | None |
| DH | Universal | Pacific only (Central from 2027) | Universal | Universal | Universal |
| Ball/strike tech (2026) | Challenge (2/game) | None | Full ABS auto-call | Challenge (2/game) | Challenge + checked-swing |
| Import limit | None | 4 active | 3 + 1 Asia quota | 18 of 38 | None (MLB org players) |
| Postseason champion | World Series (Bo7) | Japan Series (Bo7) | Korean Series (Bo7) | Serie del Rey (Bo7) | 1-game final |


Always resolve, per `BB-P3`/`BB-P4`: the exact league and season, DH status, scheduled innings, the tie/extra-innings rule, the import and active-roster rules, the ball-strike technology in force, and the operator's official-game and listed-pitcher terms — before any rate work.

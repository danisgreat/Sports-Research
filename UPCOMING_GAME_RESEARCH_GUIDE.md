# Upcoming game research and forecast guide

Status: **ACTIVE OPERATIONAL GUIDE**

Guide ID: **UGR-2026.08.30-v1.1**

Published forecast method: **MDS-2026.08.30-v2.7 — qualitative champion**

Numerical training specification: **NTS-2026.08.25-v0.2 — Stage 0 all-sports design/pre-fit**

Effective: **2026-08-30**

This is the full procedure for an upcoming or live sports request. AGENT_ROLE_AND_TASK.md and RULES_GENERAL.md control conflicts. Read versions and status from the active files at run time; do not rely on a copied prompt's older version string.

## 1. Current truth and scope

- The active user-facing method is a qualitative sport-native exposure × rate corridor with scenarios and unique candidate ranking.
- H0 has not been built or quality-approved.
- No numerical model, simulator or calibrator is fit, tested or validated.
- No internal probabilities may be published. Current probability state is `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`.
- Same-time odds may be recorded, but value cannot be supported without a validated calibrated probability and the complete value gate.
- This workflow may research the web and update Markdown records. It does not authorise code, datasets, notebooks, databases, fitted artifacts or staking.

Dedicated qualitative sport modules: cricket, basketball, American football, baseball including MLB/NPB/KBO, AFL/AFLW, rugby league, rugby union/sevens, soccer, ice hockey and tennis. Tennis, rugby union and rugby sevens do not yet have approved numerical target/source/model cards. Use RULES_GENERAL.md §10 for other sports until a dedicated specification exists.

## 2. What to supply for an upcoming event

Provide as many of these fields as possible. The analyst should verify discoverable facts rather than ask unnecessary questions.

| Field | Required content |
|---|---|
| Sport and competition | Exact league/format/rules population |
| Event | Named teams/players and home/away/neutral status if known |
| Schedule | Date, time and named timezone; venue if known |
| Requested state | Auto-verify, pregame or live |
| Phase/horizon | Full event, regulation, quarter, half, period, innings, named day, remaining segment, etc. |
| Supplied contracts | Complete candidate slate exactly as offered |
| Operator/terms | Operator and regulation/OT/action/void terms, or `NOT SUPPLIED` |
| Odds | Decimal odds for each row and opposite side where available |
| Price time | Capture timestamp/timezone; required for value |
| Ranking objective | Marginal win likelihood by default; value only if every value gate can pass |
| Candidate origin | `USER_SUPPLIED` or a predeclared systematic/generated universe |
| Number of ranked rows | Normally every valid unresolved supplied row |
| Logging mode | Research + forecast + log, or research + forecast only |

Ask one concise clarification only when unresolved ambiguity changes event identity, target, settlement or eligible candidates materially. Never silently turn “Over 235.5 runs” into named-day, remaining-day or innings runs.

## 3. Permitted decision outcomes

| Outcome | When to use it |
|---|---|
| RANKED FORECAST | Active event, resolved targets/contracts, enough evidence for an honest ordering |
| RANKED FORECAST — NO BET ENDORSED | Valid rows can be ordered, but evidence/value gates do not support an endorsement |
| NO FORECAST — FINAL BEFORE DELIVERY | Event became final or relevant target settled before issue |
| EXCLUDED ROW — MALFORMED/UNRESOLVED | Identity, metric, endpoint or settlement cannot be resolved safely |
| LIVE STATE NOT VERIFIED | Start passed but no trustworthy conditional state is available; never pretend pregame |

A weak slate still receives unique ranks for all valid unresolved rows. Use `FORCED RANK`, low evidence and `NO VALUE DETERMINABLE`; do not use PASS to evade the user's requested ranking.

## 4. End-to-end lifecycle

```text
top log snapshot
  -> reconcile canonical IDs/aliases/duplicates
  -> settle verified finals; leave live/postponed open
  -> verify new event and state
  -> freeze decision set, targets, contracts and information cutoff
  -> retrieve volatile facts, process evidence and context from field-owning sources
  -> build sport-native target corridor/distribution object
  -> lower / central / upper / material tail scenarios
  -> integrate contract geometry and dependence
  -> unique marginal-likelihood ranks + potential winner
  -> final volatile refresh
  -> append immutable Markdown view
  -> deliver with sources and limitations
  -> official settlement, process retrospective and prospective learning
```

## 5. Previous-log and retrospective gate

1. Use README to identify the active prediction log, then read only its top Current controlling snapshot for queue state.
2. Verify every open event from authoritative current sources.
3. If FINAL, append the official settlement and retrospective before the new forecast.
4. If LIVE, postponed, suspended, abandoned pending terms, or final verification is unavailable, preserve that exact state, do not grade it and continue.
5. Never rewrite an issued view. Append corrections, live views, settlements and retrospectives.
6. Separate contract outcome from process grade, expected driver from actual driver, and knowable preissue information from random realization.
7. A single win/loss may create a candidate observation but cannot change forecast weights. Update LEARNING_REGISTER.md only under its preregistered prospective procedure.
8. Before combining a new component, verify one canonical ID per distinct event, preserve reused/skipped issued labels through aliases, and mark exact repeated blocks `DUPLICATE_STORAGE` rather than counting them again.
9. Compare each card's claimed issue time with the first section-inclusive immutable artifact that demonstrably contains it. A post-final first artifact is `E1-Q-LATE_IMPORT` even when the card embeds an earlier timestamp; settle it descriptively but exclude it from prospective counters.

Required retrospective fields:

| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change |
|---|---|---|---|---|---|---|---|

Process grade is `COMPLIANT`, `PROCESS_DEFECT` or `INCONCLUSIVE`. A losing compliant forecast is not automatically a model defect; a winning defective process is not validated.

## 6. Event, target, candidate and time freeze

Before directional analysis, record:

- official event ID, sport, competition/format, season/rules era, participants, venue and scheduled start;
- home/away/neutral status and current state;
- decision-set ID, candidate origin/policy, every candidate ID, canonical contract, alias, eligibility and exclusion reason;
- exact `target_id/version`, outcome, unit/support, start state, endpoint, exposure, termination/censoring and label provider;
- phase, line, statistic, regulation/OT/extra-time/golden-point/extra-innings/DLS/action/push/void terms;
- request, effective, first-known/published, observed, accessed, cutoff and issue times;
- method, source, definition and provider versions.

### Candidate policy

`USER_SUPPLIED` means freeze and rank the complete valid unresolved supplied slate. Do not replace it with an easier market.

`SYSTEMATIC_UNIVERSE` requires a predeclared operator/source, market families, threshold grid, universe freeze time and retained record of all eligible/unselected candidates. Post-forecast searching for a generous alternate is exploratory and performance-ineligible.

The issued slate is never claimed to be the full sportsbook universe unless a versioned generator proves that coverage.

### Start crossing

If start passes during research:

1. preserve the original contracts;
2. create a distinct live view and target/horizon ID;
3. verify exact live state and observation time;
4. model remaining exposure, not elapsed pace;
5. disclose that the original pregame contract may no longer be offered.

If the event becomes final, stop and report the result. No hindsight forecast is created.

## 7. Prediction-time web research protocol

### Field-owning hierarchy

1. Governing body, league/competition, official match centre, team/club, venue or government weather source.
2. Official data partner or established statistical database within its documented field/coverage.
3. Specialist analytical provider for the metric it defines.
4. Named reputable reporting for material current information not yet official.
5. Actual operator/exchange for exact contract, terms, line and price.
6. Reference/query sites, aggregators, previews, snippets and anonymous social sources for discovery/corroboration only.

Official authority and predictive importance are different. An official quote proves the quote occurred; it does not prove a large model effect. A specialist xG/EPA/Statcast provider controls its definition, not injuries or settlement. Two weak sources do not override a field owner.

### Acquisition order

1. event identity, state and rules;
2. contracts/terms and price snapshot if provided;
3. lineups/starters/toss/goalie/inactives/injuries and expected exposure, including the final official event/team/role/participant identity handshake;
4. opponent-adjusted process/strength and role information;
5. venue/surface/roof/game-window weather, rest/travel and other mechanistic context;
6. adjusted history and up to five predeclared D0 mechanism matches;
7. strongest ordinary contrary path;
8. final volatile refresh immediately before issue.

### Evidence record

For every decisive item store source/URL, field definition/provider version, value/unit, effective time, first-known/published time, live observation time, access time/feature age, source tier, transformation, predictive tier, conflict count and missingness code.

Use labels honestly: `VERIFIED FACT`, `SOURCE REPORT`, `HISTORICAL STATISTIC`, `MODEL TRANSFORMATION`, `MODEL INFERENCE`, `UNKNOWN/NOT AVAILABLE`, `STALE` or `CONFLICTING`.

Respect robots, terms, rate limits, authentication, retention and attribution. Search visibility does not authorise scraping or H0 ingestion. DATA_SOURCE_REGISTER.md controls numerical use.

### Research stopping rule

Stop expanding the source list when:

- every decision-driving field is verified or explicitly missing/stale/conflicting;
- the sport-native exposure/rate chain is covered;
- the central and strongest ordinary failure paths are represented;
- additional searching is unlikely to change the rank before the next refresh deadline.

Comprehensive research means complete material-field coverage, not an unlimited website count.

## 8. Sport-native upcoming-game checklist

| Sport | Volatile first | Core exposure -> rate -> outcome | Essential tails/refresh |
|---|---|---|---|
| Cricket | Official state, format/rules, squad/XI/toss, strip, weather/light | Legal balls/overs/time and wickets/resources -> coupled runs/dismissals -> day/innings/match outcome | DLS, no-play, collapse/death, declaration, innings switch, chase/match completion |
| Basketball | Official injury report, starters, minutes/role | Minutes/lineups/possessions -> shot/FT/turnover/rebound efficiency -> joint score | Foul trouble, late fouling, blowout, overtime; refresh confirmed lineup |
| American football | QB, injuries/inactives, line units, weather/roof | Drives/plays/field position/snaps -> drive scoring/turnover process -> discrete joint score | Explosive/non-offensive score, game script, key values, competition OT |
| Baseball | Confirmed starters, posted order, bullpen availability, roof/weather | PA/batters faced/base-out/innings -> K/BB/contact/HR and bullpen transitions -> joint runs | Starter hook, HR cluster, home ninth, extras, action terms; MLB/NPB/KBO separate |
| AFL/AFLW | Selected teams, substitute/interchange, late changes, venue/weather | Roles/time/territory -> inside-50/scoring shot -> goal/behind conversion -> joint score | Conversion variance, tempo, late separation; refresh final teams |
| Rugby league | Team list/late mail, spine, bench/interchange, goal kicker | Sets/field position/tackle state -> goal-line entry/try -> conversion/score | Errors/short field, fatigue, sin-bin, golden point; refresh final update |
| Soccer | Availability, confirmed XI/keeper/formation, roles | Attacking sequences/shots/xG -> goal process -> regulation score grid | Red card, score state, stoppage, extra-time/advance distinction; separate corners/cards/SOT |
| Ice hockey | Goalie, lines/pairs/units, scratches, rest | Shifts/ice time/shots/xG/manpower -> finishing/goaltending -> regulation goals | Penalties, pulled goalie/empty net, OT/SO; refresh goalie and scratches |

Named provider examples are candidate lanes, not permanent mandates. Use DATA_SOURCE_REGISTER.md and the sport file for field-specific roles and restrictions.

## 9. Build the underlying forecast object

Do not begin with “Which line looks safest?” Use this order:

1. competition/rules/venue baseline;
2. D0 mechanism retrieval, up to five genuinely comparable cases or `NO COMPARABLE CASE`;
3. opponent-adjusted dynamic strength with time decay and regime breaks;
4. participation/role/replacement and stochastic exposure;
5. matchup interaction;
6. verified context through a named mechanism;
7. lower, central, upper and material tail scenarios.

For a two-sided score event, write the total-volume, team-allocation and winner/margin branches separately. For linked phase/full targets, carry the complete phase-end state—score, resources, participants/replacements, tactics, workload and conditions—into the next phase. Where exposure may terminate early, include both event-before-termination and termination-before-event orderings under the frozen rules.

When the sport permits, joint team scores/resources generate winner, total and margin. “One distribution” means one per exact target, not one universal distribution across full game, phase, player and niche statistics.

Player/niche examples:

- player points: active/start × minutes × usage/opportunities × rate;
- strikeouts: pitcher action × batters faced × strikeout rate;
- SOT: start/minutes × shots per minute × role/box share × on-target conversion;
- batter runs: balls faced jointly with dismissal hazard × runs/ball;
- hockey shots: lineup/ice time × shot intensity × manpower/score state;
- corners/cards: direct target-event exposure/rate under the named provider.

Current model state is unvalidated/no run, so publish a qualitative corridor and scenario branches only. Do not invent a mean, standard deviation, interval or probability. If a future challenger genuinely runs, follow NUMERICAL_MODEL_REGISTER.md: shadow values stay hidden; validated values still suppress on OOD/drift/source/calibration failure.

## 10. Scenario and kill-path construction

At minimum record:

| Scenario | Question |
|---|---|
| Lower tail | What reduces exposure or rate materially below centre? |
| Central | What is the most plausible participant/state/game path? |
| Upper tail | What raises exposure, efficiency or event clustering? |
| Structural tail | Blowout, collapse, red/sin-bin, HR cluster, weather loss, extra period, empty net, declaration or another sport-native branch |

For every candidate name its strongest ordinary kill path. A named tail is not automatically likely; state its preconditions and evidence. Near-tied candidates remain near-tied in language despite unique ranks.

## 11. Contract geometry and dependence

Draw win/push/loss intervals before ranking. Tag exact complements, integer pushes, nested lines, overlap, gaps, positive-handicap overlap, phase/full links, player/team links, aliases and shared causal theses.

For integer `Y` and `F(k)=P(Y<=k)`:

- `P(Over k.5)=1-F(k)`;
- `P(Under k.5)=F(k)`.

Examples:

- `Dream -10.5` and `Sparks +10.5` are exact opposites if event scope and OT terms match.
- `Over 181.5` and `Under 181.5` are exact complements under matching terms.
- Those four rows form two guaranteed-opposite pairs absent void, but this does not prove candidate-generation skill or create four independent forecasts.
- `Over 185.5` and `Under 285.5` overlap and can both win from 186 through 285; never multiply their marginal chances.

Assign one event/target dependence group. Only one row per shared thesis is `PRIMARY_FORMAL`; the rest are `CORRELATED_SECONDARY`. All valid rows are still ranked and settled.

## 12. Ranking, no-bet and evidence labels

Default ranking objective: marginal estimated chance of WIN and robustness under exact terms. Dependence does not turn the ordinal list into a hedge.

| Field | Allowed values/use |
|---|---|
| Rank | Unique contiguous ordinal among valid unresolved rows |
| Verdict | SUPPORTED, LEAN, FORCED RANK, AVOID |
| Evidence | HIGH, MEDIUM, LOW or explicit limitation |
| Performance role | PRIMARY_FORMAL, CORRELATED_SECONDARY, INELIGIBLE |
| Actionability | VALUE SUPPORTED, NO VALUE DETERMINABLE, NOT ACTIONABLE |
| Probability | NOT_GENERATED, SHADOW, GENERATED_VALIDATED plus publication state |

`SUPPORTED` requires fresh event-specific evidence that outweighs the strongest ordinary kill path. `AVOID` is an evidence-relative direction, not a negative-EV claim. If no candidate clears an endorsement/value gate, add `NO BET ENDORSED` while preserving all requested ranks.

## 13. Potential winner

Analyse the complete event winner independently from totals, spreads, phases and props. State:

- exact regulation/full-match/draw/advance contract;
- `LEAN` or `FORCED WINNER — LOW CONFIDENCE`;
- evidence quality;
- central mechanism;
- strongest failure path;
- canonical contract ID or alias if already supplied.

A repeated moneyline/winner is one canonical observation, not a second pick.

## 14. Price and value layer

Likelihood is not value. `VALUE SUPPORTED` requires all of:

1. target-specific validated calibrated W/P/L probabilities;
2. exact same-time, same-contract, both-side price and operator/terms;
3. captured time no later than cutoff;
4. frozen overround/de-vig method;
5. expected-return arithmetic including push/refund/commission;
6. uncertainty margin beyond a predeclared threshold.

Otherwise use `NO VALUE DETERMINABLE`. Raw `1/odds` contains margin. Closing odds observed later are a benchmark only.

Keep three lanes separate: `MARKET_BLIND`, `MARKET_ONLY_BASELINE`, and `MARKET_INFORMED`. A hybrid can be accurate but cannot support a claim of independent sports-only signal.

## 15. Logging and user-facing delivery

When logging is authorised and write access exists:

1. append the complete view before delivery using MODEL_AND_DATA_SPEC.md's schema;
2. store one underlying target forecast and linked contract rows;
3. preserve issued records immutably;
4. store a section-inclusive content hash/append receipt or immutable revision that demonstrates the exact card text at issue time; a whole-file creation time cannot prove later sections;
5. update the top queue snapshot only after the append succeeds;
6. verify every Markdown table's column counts and the canonical event/alias/duplicate ledger;
7. confirm the log append in the response.

If write access is unavailable, state `NOT LOGGED — NO WRITE ACCESS`; do not claim prospective eligibility.

Recommended final response order:

1. previous-log status;
2. GAME-STATE, identity, start times, cutoff and refresh;
3. target/contract manifest and assumptions/exclusions;
4. key verified information/conflicts/missingness;
5. D0 mechanism retrieval;
6. sport-native underlying forecast;
7. scenario map;
8. contract geometry/dependence;
9. ranked table;
10. `NO BET ENDORSED` if applicable;
11. potential winner;
12. optional alternative only when pre-authorised from a frozen universe;
13. uncertainties and what could change the view;
14. current model/training/validation state;
15. logging confirmation;
16. direct source links.

## 16. Settlement and prospective learning

Settle from official result/stat sources and exact contract terms. Preserve WIN, LOSS, PUSH, VOID, UNRESOLVED or UNSETTLEABLE. Retry a niche official statistic once before final UNSETTLEABLE.

If a live threshold is already impossible to reverse, annotate the row mathematically won/lost but keep the event open until the official final/termination settles every remaining contract.

After settlement:

- compare the issued central/kill paths with actual process drivers;
- classify knowability and process defect separately from outcome;
- audit every #1 loss, but do not manufacture a calibration conclusion from one event;
- count aliases/dependent rows once at the independent event/target level;
- add only candidate/test evidence to LEARNING_REGISTER.md unless a preregistered promotion rule passes.

## 17. Numerical training roadmap

Future numerical work, only when separately authorised:

1. approve exact source fields and immutable point-in-time snapshots;
2. build H0 from every eligible event in a frozen population;
3. fit A0/A1 baselines on chronological TRAIN/TUNE;
4. fit sport-native A2 and flexible A3/A4 challengers on identical folds;
5. compare market-blind, market-only and hybrid lanes;
6. calibrate on disjoint CAL;
7. open untouched TEST once;
8. run immutable E1-P shadow forecasts;
9. publish only after target/population/horizon/slice gates pass.

Primary distribution metrics are CRPS/RPS and log score, with calibration/reliability, PIT/rank diagnostics, interval coverage/width and event-clustered uncertainty. Brier/log score assess derived contracts. MAE, rank results, hit rate and ROI are secondary and cannot alone promote a probability model.

## 18. Failure-mode stress tests

- Ambiguous cricket `O235.5`: do not guess day versus innings target.
- Start passes: switch to a verified live target or state `LIVE STATE NOT VERIFIED`.
- Final before delivery: result only, no hindsight forecast.
- Previous event live: leave open and continue; no retrospective.
- Missing/stale/post-result odds: likelihood rank allowed; value prohibited.
- Model registered but not run: `NOT_GENERATED`; registry text is not a forecast.
- Shadow model: store, do not publish.
- Validated build outside support or with failed source/calibration gate: `SUPPRESSED`; qualitative fallback.
- All candidates weak: unique ranks plus `NO BET ENDORSED`.
- Player/corner/SOT without direct exposure/rate/provider definition: low-evidence forced rank or exclusion.
- “Pick your own” without a frozen universe: do not post-hoc hunt; request/define the universe prospectively.
- Many thresholds from one target: one forecast/dependence group and one independent event weight.

## 19. One-page pre-delivery checklist

- [ ] Read active role/general/model/algorithm/numerical/sport/learning documents and top log snapshot.
- [ ] Settled verified earlier finals; left live/postponed/unverified events open.
- [ ] Verified new event identity, state, rules, venue and schedule/timezones.
- [ ] Frozen target, endpoint, exposure, contracts, slate origin and cutoff.
- [ ] Retrieved volatile facts first from field-owning sources.
- [ ] Matched every decision-driving participant to the exact official event/team/role at the final refresh; unresolved or secondary-only roles are labelled and scenario-weighted.
- [ ] Modelled participants/replacements, exposure, rate, matchup and context.
- [ ] Retrieved up to five predeclared D0 mechanism matches or recorded none.
- [ ] Built lower/central/upper/material tail scenarios and kill paths.
- [ ] Mapped W/P/L intervals, aliases, complements, overlap/gaps and dependence.
- [ ] Ranked every valid unresolved row uniquely; added no-bet label if warranted.
- [ ] Analysed potential winner independently.
- [ ] Made no probability/value claim beyond current validation and price gates.
- [ ] Refreshed state/participants/weather/price just before issue.
- [ ] Appended the immutable Markdown view before delivery, if authorised.
- [ ] Cited current claims and disclosed unknowns/conflicts/source limits.

Use the fill-in prompt in [UPCOMING_GAME_PROMPT_TEMPLATE.md](UPCOMING_GAME_PROMPT_TEMPLATE.md).

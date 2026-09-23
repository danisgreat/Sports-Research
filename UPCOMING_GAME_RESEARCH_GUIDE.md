## 2026-09-12 current pregame checklist amendment


> **CR-2026.09.21-3:** before using a historical audit lesson, resolve it through `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`. Do not revive superseded/rejected findings or double-apply duplicate controls. CR-3 additionally requires live-rule read-back so stale gate text cannot override the reconciliation.


> **Current revision — 2026-09-19:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.




Use CONTROLS.md's dated correction and RULES_GENERAL section 16.9. Capture both starters, full nominated bench/reserves and both coaches with source and publication time; separate unknown, unavailable and proven retrieval miss. Tennis team-lineup/bench fields are N/A. Official or secondary roster presence does not prove starters. Retrieve exact attempts/workload, avoid betting-tip/consensus prose in MARKET_BLIND analysis, and stress the top pick's full-event losing states including extra periods.


Before a new card, read the current settlement queue in GAME_LOG_STATUS_CURRENT.md and the active Part-5/mini-log snapshot. Live items are saved and skipped; their current score must not leak into already frozen analysis. Preserve canonical IDs and resolve the next ID from the live reconciliation rather than a hard-coded number. Archive imported raw mini logs in archive/mini_logs after verification. All present historical logs remain learning-only and not performance eligible.


# Upcoming game research and forecast guide


> **2026-09-12 controlling correction:** All current combined-log material is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current user request. Settlement preserves outcome evidence; it does not authorize a performance claim. The [2026-09-12 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md) and [probability/research corrections](audit_2026-09-12/rule_corrections.md) supersede conflicting older operational statements. Original issued records remain unchanged.




> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This document remains as the detailed narrative walkthrough of each step; `METHOD.md` §3 is the compressed authoritative statement of the same lifecycle.


Status: **ACTIVE OPERATIONAL GUIDE — DETAILED REFERENCE**


Guide ID: **UGR-2026.09.05-v1.8**


Published forecast method: **MDS-2026.09.19-v4.3 — SPORTS_ONLY / MARKET_BLIND qualitative method; no numerical champion is fitted (see METHOD.md)**


Numerical training specification: **NTS-2026.09.19-v0.5 — Stage 0 all-sports design/pre-fit**


Effective: **2026-09-05**


This is the full procedure for an upcoming or live sports request. AGENT_ROLE_AND_TASK.md and RULES_GENERAL.md control conflicts. Read versions and status from the active files at run time; do not rely on a copied prompt's older version string.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal event verification before research — CR-2026.09.19-4 component (preserved under CR-2026.09.21-1)


Before sport-specific research begins:
- collect **at least three independent reliable source lineages** for the exact event;
- verify venue/host, official venue-local date/time and IANA timezone;
- convert that instant to `Australia/Melbourne` with the correct AEST/AEDT label and calendar date;
- explicitly correct any conflicting user-supplied start estimate;
- verify current event state immediately before issue/refresh.


Search snippets, generated summaries and syndicated duplicates do not satisfy the source minimum.


For settlement, three independent reliable lineages must explicitly agree on the exact event/date, terminal state and final result. Any credible live/in-progress source or material conflict blocks settlement.


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


The authoritative step order is `GFA-2` in RULES_GENERAL.md §11, steps G0–G40 including G4.1 slate geometry, G12.1 descriptive base-rate record, G13.1 recency/head-to-head/trend windows, G14.1 deficit attribution, G15.1 environment gate, G20.1 separation budget, G23.1 direct marginal-likelihood ordering, G25.1 Rank-1 conditional coherence and G30.1 winner/cushion reconciliation, with the sport file’s `SFA-<SPORT>` section supplying the exposure chain, mandatory branch set, contract derivation map and kill-path library. The diagram below is the same lifecycle in summary form; where the two are read differently, `GFA-2` controls.


```text
top log snapshot
  -> reconcile canonical IDs/aliases/duplicates
  -> settle verified finals; leave live/postponed open
  -> verify new event and state
  -> freeze decision set, targets, contracts and information cutoff
  -> retrieve volatile facts, process evidence and context from field-owning sources
  -> record descriptive REFERENCE_BASE_RATE, threshold, population and denominator for every supplied contract
  -> retrieve L5/L10/L15/L20 for both sides + head-to-head with continuity count; perform the descriptive recency review
  -> classify venue OUTDOOR/INDOOR/RETRACTABLE; obtain the venue-coordinate match-window forecast
     (wind speed/gusts/direction, dew point, cloud cover, hourly precipitation) and resolve wind to a vector
  -> build sport-native target corridor/distribution object
  -> lower / central / upper / material tail scenarios
  -> integrate contract geometry and dependence
  -> solve the component budget for every aggregate line and the phase-split separation budget for every margin/cushion line
  -> run the extra-condition support audit; order by direct marginal likelihood (no band, trend or slot adjustment)
  -> state the Rank-1 implied-target interval; classify every other row COHERENT/PARTIAL_OVERLAP/DISJOINT and repair or disclose
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
4. If LIVE, suspended, abandoned pending terms, or final verification is unavailable, preserve that exact state, do not grade it and continue. A pre-start cancellation/rainout with no actionable view closes as `NO ACTION`; any rescheduled fixture requires a fresh state/participant/contract freeze and new view rather than being treated as the old card still live.
5. Never rewrite an issued view. Append corrections, live views, settlements and retrospectives.
6. Separate contract outcome from process grade, expected driver from actual driver, and knowable preissue information from random realization.
7. A single win/loss may create a candidate observation but cannot change forecast weights. Update LEARNING_REGISTER.md only under its preregistered prospective procedure.
8. Before combining a new component, verify one canonical ID per distinct event, preserve reused/skipped issued labels through aliases, and mark exact repeated blocks `DUPLICATE_STORAGE` rather than counting them again.
9. Record issue horizon, freeze provenance and local import time separately. Apply the existing-history user confirmation in PERFORMANCE_ELIGIBILITY_POLICY.md; do not exclude non-live cards merely because they were imported later. Explicit live-issued views remain separate. A later live status check does not change a pre-game card’s horizon.


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


For the competition/format, season/rules era and the regulation/OT/extra-time/tiebreak/DLS/promotion-relegation/settlement terms, use the **"Sport and competition rules reference"** section of the relevant `RULES_<SPORT>.md` (`§9`, or `§10`/`§11` where noted; cricket and soccer point to `LEAGUE_RULES_CRICKET.md` / `LEAGUE_RULES_SOCCER.md`). It carries the playing laws, the per-league rule differences and the per-competition format/playoff/settlement rules for every league in the logs — and its identity checklist is the list of facts to freeze here. It is reference material, not an override of `GFA-2` or any `SFA-<SPORT>` gate.


**Season-boundary and new-competition checks (RULES_GENERAL.md §3, `G2`).** If this is the first card of a new season, a new pre-season, a new tournament edition, or the first appearance of the competition after a gap of roughly six weeks or more, **re-verify the competition's rules against the field owner before modelling** — playing-law/playing-condition changes, format or playoff-structure changes, a new stage or in-season event, technology adoption (VAR, ABS, semi-automated offside), and roster/import-quota changes — and update the reference section before issuing the card. If the competition has **never been forecast before**, write its complete rules into the reference section first; do not forecast an undocumented competition. Record both checks on the card (line `1a` of the mandatory card checklist).


### Candidate policy


`USER_SUPPLIED` means freeze and rank the complete valid unresolved supplied slate. Do not replace it with an easier market.


`SYSTEMATIC_UNIVERSE` requires a predeclared operator/source, market families, threshold grid, universe freeze time and retained record of all eligible/unselected candidates. Post-forecast searching for a generous alternate is exploratory and performance-ineligible.


The issued slate is never claimed to be the full sportsbook universe unless a versioned generator proves that coverage.


**Self-generated logs (an operator choosing their own events and lines) are `SYSTEMATIC_UNIVERSE`, not `USER_SUPPLIED`.** The safeguards above then bind on the operator: pre-declare, in writing and once, the **operator/source** (which book), the **market families** carded for each sport (e.g. baseball = moneyline + run line ±1.5 + game total, both sides of each — the operator's featured ~1.90/1.95 two-way markets), and any **alternate-line grid** as a fixed rule (e.g. "also ±0.5 and ±2.5 on the main handicap, total ±1 run") — not a per-game hand-pick. Apply the same grid to **every** event; do not add a line to one card because it "looks good" or drop one because it looks hard. Record the odds and capture time for each row as metadata; they never enter the forecast or the rank (RULES_GENERAL.md §4 bookmaker-independence hard gate). Choosing lines per game by how attractive they look is selection bias and makes the whole log performance-ineligible.


### Start crossing


If start passes during research:


1. preserve the original contracts;
2. create a distinct live view and target/horizon ID;
3. verify exact live state and observation time;
4. model remaining exposure, not elapsed pace;
5. disclose that the original pregame contract may no longer be offered.


If the event becomes final, stop and report the result. No hindsight forecast is created.


Enforce `cutoff_at < scheduled_start_at` for every `PREGAME` view after converting both timestamps through named time zones. Once start is reached, a stale upcoming/0-0/zero-live schedule shell cannot preserve pregame status. If the exact live state cannot be verified, output `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, retain the event in the queue and move on.


## 7. Prediction-time web research protocol


### Field-owning hierarchy


1. Governing body, league/competition, official match centre, team/club, venue or government weather source.
2. Official data partner or established statistical database within its documented field/coverage.
3. Specialist analytical provider for the metric it defines.
4. Named reputable reporting for material current information not yet official.
5. Actual operator/exchange for exact contract, terms, line and price.
6. Reference/query sites, aggregators, previews, snippets and anonymous social sources for discovery/corroboration only.


Official authority and predictive importance are different. An official quote proves the quote occurred; it does not prove a large model effect. A specialist xG/EPA/Statcast provider controls its definition, not injuries or settlement. Two weak sources do not override a field owner. Even an official page must match the current event ID/date/participants, page state, score chronology and revision; quarantine stale status shells, old H2H widgets and malformed score/title slugs field by field.


### Acquisition order


**Rung 0 — structured keyless endpoint, before anything narrative (added 2026-09-06, `L-080` / `G10.1`).** Where a structured keyless endpoint exists for this competition, query it **first**, for every decisive field it carries, before opening any match report, preview, live blog or aggregator page. A structured JSON field cannot be reordered, misattributed or hallucinated by a summariser; a narrative page can, and on 2026-09-05 one was (`L-074`). Verified endpoints, coverage and — just as importantly — verified **non**-coverage are listed in `DATA_SOURCE_REGISTER.md` §September 6. Where an endpoint exists and was not queried, any conflicting narrative value is provisional only.


This rung was added because four rows recorded as unresolvable after weeks of extensive narrative searching (`P-300` powerplay, `P-302` corners, `P-273` corners, `P-151` corners) each closed in a single request once the structured layer was queried. The earlier passes did not search too little; they searched the wrong layer.


**Rung 0.5 — settlement-source pre-registration (`G10.2`).** Before a row enters the ranked slate, name the endpoint that will settle it and confirm in this session that the endpoint returns that field for this competition. A row with no nameable settling endpoint is `SETTLEMENT_UNSOURCED`, carries `LOW` evidence and is capped below Rank #1. This is a competition-coverage test, not a market-type ban.




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


Use one atomic row per decision-driving field. An organisation name, provider bundle, search result or “site-style scorecard” is not reproducible evidence. Identify the exact record/URL and field owner. De-duplicate one underlying match or upstream feed when it appears through recent-form, venue, H2H, prior-log and multiple front-end summaries.


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
3. opponent-adjusted dynamic strength with time decay and regime breaks; sparse or new regimes widen uncertainty before moving the centre unless a directional mechanism is supported;
4. participation/exact phase-and-score-state role/replacement and stochastic exposure;
5. matchup interaction;
6. verified context through a named mechanism;
7. lower, central, upper and material tail scenarios.


For a two-sided score event, write the total-volume, team-allocation and winner/margin branches separately, then stress low/close, low/separation, high/close and high/separation families. For linked phase/full targets, carry the complete phase-end state—score, resources, participants/replacements, tactics, workload and conditions—into the next phase. Where exposure may terminate early, include both event-before-termination and termination-before-event orderings under the frozen rules.


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


Before freezing Rank #1, write at least one representative score/event path that makes it win and verify that the strongest researched mechanism supports every extra condition required by the exact contract. One-team dominance is not automatically a full-game Over, a low total is not automatically a close handicap, and goal/shot/possession evidence is not a corner model.


Locate each line against the lower, central and upper corridor and all ordinary branches. If the line is inside the central corridor, or material unweighted ordinary branches fall on both sides, cap directional evidence at LOW unless an explicit predeclared mixture or validated distribution establishes separation. For an aggregate total, solve the threshold as a component/team/phase budget at each component's floor, centre and ordinary high state.


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


**Print the failure mass, not only the dependence label** *(added 2026-09-17(b))*. A dependence tag records that rows move together; it does not say how much mass sits in the state where they move together *against* you, which is the quantity that governs top-two and whole-card reliability.


- Top two: `P(¬R1 ∧ ¬R2)` with the single named state that produces it (`G-L17`).
- Three or more rows on one driver: `P(all fail)`, or `JOINT_UNQUANTIFIED` with Fréchet bounds `max(0, Σ(1−pᵢ) − (k−1)) ≤ P(all fail) ≤ min(1−pᵢ)` (`G-L21`).
- **Check the sign before calling two rows jointly supported.** Rows can share a driver and still oppose each other under it: a low-scoring, starter-suppressed game supports an Under *and works against a favourite's handicap*. `P-444` treated both as supported by one thesis and lost both.
- Label every over/under row `FORCED_PAIR` or `FREE`, name the preferred side of each forced pair, and derive the push mass rather than asserting it (`G-L15`, `G-L22`).


Worked case: `P-438` ranked four rows (0.84, 0.83, 0.82, 0.63) that all needed "few goals". Independence implies P(all four fail) ≈ 0.0018; the card's own marginals bound it at 0.16. The realised state sat somewhere across those two orders of magnitude and the card printed neither — it produced the worst card in Part 4. The counterpart `P-439` had the same slate shape and won every row, which is why this is a **disclosure and not a prohibition**: a correlated slate is high-variance in both directions and the card must say so before the result is known.


**Handicap rows are derived, not assigned** (`G-L24`). Compute `P(fav −L.5) = P(fav wins) × (1 − b_L)` and `P(dog +L.5) = P(dog wins) + P(fav wins) × b_L`, taking the cushion band `b_L = P(margin ≤ L | winner)` from `BASE_RATES_REGISTER.md` §1 with its `n` and date. If that sport's band has not been derived, derive it from the competition's completed-season record first, or print `BAND_NOT_DERIVED` and do not rank the row #1.


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


## 16. Settlement and prospective learning — the complete comprehensive settlement protocol


This section is the single self-contained walkthrough for settling a previous game log when its events are complete, consolidating RULES_GENERAL.md §§2, 8, 9 and 11.8 (`G0`, `GATE-READ`, `G36`–`G40`), AGENT_ROLE_AND_TASK.md §7, and the retrospective driver table in MODEL_AND_DATA_SPEC.md §11. It is written so that any generating session — this one, a future continuation, or a separate external session working only from these documents — can execute it without needing to reconstruct the procedure from scattered rule fragments. It creates no new authority: where any step below appears to conflict with the source sections it consolidates, those sections control.


**Trigger.** Before issuing any new forecast, first read the active log's (identified via README.md) top controlling snapshot and its queue. Every listed OPEN, LIVE, or PENDING event is a candidate for this protocol. Run it to completion, in ID order, before moving to a new forecast — never skip settlement to "get to" the requested pick sooner; the queue is processed first every time, without exception, including when the user's message only asks for a new pick and does not mention the queue.


**Step 0 — fresh-read confirmation (`G0`/`GATE-READ`).** Confirm this session has read AGENT_ROLE_AND_TASK.md, RULES_GENERAL.md, the relevant RULES_<SPORT>.md, and the active log's top snapshot **in this session**, not from memory of an earlier one. Record the method version exactly as found in that fresh read. A session that cannot demonstrate this (for example, an external chatbot that was not handed the current files) must not declare a method version at all rather than guessing or reusing a remembered one — see the 2026-09-04 finding at the top of `PREDICTION_LOG_COMBINED.md` for what happens when this step is skipped.


**Step 1 — state-check every queued event, in ID order.**


| Queued state | Action |
|---|---|
| Genuinely still upcoming / not started | Leave open, note state, continue to the next queued ID |
| LIVE | Leave open, continue to the next queued ID; do not force a live settlement from an unverified state |
| Suspended / postponed | Preserve the exact state and any partial score; do not settle |
| FINAL, officially verified | Proceed to Step 2 |
| Scheduled start passed, no trustworthy state recovered | Record `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST` or leave `OPEN`, per RULES_GENERAL.md §2; never guess a result |


**Step 2 — retrieve the official result.** Route to the field-owning source under RULES_GENERAL.md §4 (governing league/competition/team/official match centre first). If that source is stale, a placeholder, or unreachable, use two independent current high-quality sources that agree, and record both. If credible sources conflict on a raw value but every value settles the frozen contract identically (threshold-invariant), settle the contract and preserve the raw conflict; if any value would change the settlement, keep that field `UNRESOLVED` rather than picking the convenient number. A same-domain or same-provider page showing the wrong date/event (see the P-268 Sofascore "previous match" mislabel, 2026-09-04) is a source-state defect, not a genuine conflict — verify event identity/date before treating two numbers as disagreeing.


**Step 3 — settle every contract row from the frozen slate.** For each row, apply the exact terms frozen at issue time: `WIN`, `HALF_WIN`, `PUSH`, `HALF_LOSS`, `LOSS`, `VOID`, `UNRESOLVED`, or `UNSETTLEABLE`. Preserve push mass at integer lines, quarter-line child settlements, and operator terms where known; where operator terms were never supplied, settle the research outcome and separately label the operator treatment `UNKNOWN_DEFINITION` rather than inventing one. For a niche statistic with no field-owning source, retry once against an official/data-partner source after the final before marking `UNSETTLEABLE`. Settle the potential winner using its own exact endpoint (regulation vs eventual vs advance/qualify are different settlements — RULES_GENERAL.md §6 "Potential winner").


**Step 4 — grade process separately from outcome, for every row.** Record, per AGENT_ROLE_AND_TASK.md §7 and MODEL_AND_DATA_SPEC.md §11:


- preissue expectation (the central/kill-path branch actually named) versus the actual driver;
- whether the difference was knowable before issue, or was genuine in-event variance;
- process grade: `COMPLIANT`, `PROCESS_DEFECT`, or `INCONCLUSIVE` — never assign `PROCESS_DEFECT` merely because a supported ordinary branch occurred; a correctly weighted tail can still happen (AGENT_ROLE_AND_TASK.md §7);
- defect class from the MODEL_AND_DATA_SPEC.md §11 taxonomy where `PROCESS_DEFECT` applies;
- dependence group and any boundary sensitivity (a push-adjacent or single-possession/single-run margin is disclosed, not just graded pass/fail);
- **grade against the method version the card actually declares**, never against a later version's gates retroactively — a card frozen under an older method is not penalised for missing a control that postdates it (see P-271's `G30.1` discussion, 2026-09-04), but *is* flagged if its declared version was already stale relative to its own true append time (Step 0).


**Step 4a — open the process record before classifying anything (`G-L23`, added 2026-09-17(b)).** Step 4's process-versus-outcome split cannot be performed from a score and a narrative. Before assigning a grade, and **before any control is amended on the strength of this result**, retrieve and print:


1. the **sport's process fields** from the structured feed — shots and shots on target and possession (soccer), inning-by-inning with the regulation-versus-final split (baseball), phase runs and wickets (cricket), quarter scores (basketball);
2. the **disruption facts** required by `RULES_GENERAL.md` §16.11(o) — red cards, sin bins, injury exits, weather stoppages — each **with its minute and the score at that minute**;
3. an explicit classification: did the card's **process** read fail, or did the process read hold while **conversion, an endpoint or a disruption** produced the result? A control may not be amended on the second kind without a separate, independent argument.


The competition's official report is authoritative for the score and usually publishes nothing else — AFC reports carry no shots, corners or cards, and wire recaps carry no regulation-versus-final split. Register the **process feed** alongside the settlement route (`DATA_SOURCE_REGISTER.md`).


Origin: `P-438` finished 3–2 against three ranked Unders, and the external retrospective concluded the card's early-goal mass was too low. The structured feed said the opposite — the beaten side took **two shots in ninety minutes and scored two goals** while the winner took **41**, and a **60th-minute red card** preceded the late goals. Acting on the narrative diagnosis would have raised early-goal mass in exactly the low-process matches where it is least warranted. A settlement can be completely accurate about *what* happened and still be wrong about *why*, and it is the "why" that becomes a rule.


**Step 5 — deep retrospective, mandatory whenever Rank #1 loses, whenever the card's highest-ranked over/under selection loses or pushes (user directive 2026-09-19; `METHOD.md` §7), or whenever more than one top-ranked row loses.** Use this table format (already the working convention in this log):


| Question | Content |
|---|---|
| What went right? | Which named branches/rows, if any, were correct |
| What went wrong? | The specific reasoning gap, not merely "the result differed" |
| Actual mechanism | What the verified result/sources show actually happened |
| Improvement | A concrete, falsifiable refinement — cite the existing control it refines, or propose a new `CANDIDATE` in LEARNING_REGISTER.md |
| Grade | The process grade and defect class from Step 4 |


**Step 6 — record learning, never promote from one case.** Add only `CANDIDATE` (or, for a pure completeness/disclosure/symmetry repair with no predictive claim, `PROMOTED_PROCESS` — see LEARNING_REGISTER.md §5) entries. A single event, or a same-day batch, is an exploratory checkpoint (five cases minimum before even exploratory review) and can never itself promote a forecast weight.


**Step 6a — run the mechanical completeness audit.** Run `python audit_card_controls.py <running_log.md> --settlement` over the log and record the per-card result (`RULES_GENERAL.md` §16.8). A missing field does not invalidate an issued card — issued evidence is immutable — but it is a process defect on that card, and a cohort-wide pattern is itself a finding. The script detects *printed fields*, not analysis quality, so a PASS is weak evidence and a FAIL is strong evidence.


**Step 7 — update the log's controlling snapshot in the same pass.** Next canonical ID, queue state, and any descriptive ledger rows are updated before, or in the same edit as, the settlement content — never left stale for a later session to reconcile. If a batch is later found only after being merged into a separate settlement addendum (as happened with P-241–P-267 on 2026-09-03), the active log's own top snapshot must still be updated at the time of merge, not left pointing at an earlier ID.


**Only after Steps 1–7 are complete for every queued event does a new forecast request proceed.**


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
- Start passes: `PREGAME` becomes illegal; switch to a verified live target or state `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`.
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
- Line inside the declared central corridor without scenario weights: forced rank / LOW evidence, not a confident lean.
- One event repeated as venue, form, H2H and prior-log evidence: one underlying evidence unit, not four confirmations.
- Cricket `STRIP STATUS: NOT FOUND AFTER SEARCH` with no shown rung 1–5 attempt: not compliant with RULES_CRICKET.md §2/DATA_SOURCE_REGISTER.md §6A; run and disclose the rung table before the card issues.
- A streak, Under/Over run, or a "bounce back"/series-response lean used directionally with no named, currently active mechanism in either direction: zero weight under RULES_GENERAL.md §11.3E (G17.1); rank from the longer-run baseline instead.
- An extension endpoint (overtime, extra innings, penalties, super over) modelled at the regulation rate instead of its own rule-defined rate: repair before ranking (G22).


## 19. One-page pre-delivery checklist


- [ ] Read active role/general/model/algorithm/numerical/sport/learning documents and top log snapshot.
- [ ] Settled verified earlier finals; left live/postponed/unverified events open.
- [ ] Verified new event identity, state, rules, venue and schedule/timezones.
- [ ] Verified `cutoff_at < scheduled_start_at` before using `PREGAME`; otherwise changed state or failed closed.
- [ ] Frozen target, endpoint, exposure, contracts, slate origin and cutoff.
- [ ] Retrieved volatile facts first from field-owning sources.
- [ ] Matched every decision-driving participant to the exact official event/team/role at the final refresh; unresolved or secondary-only roles are labelled and scenario-weighted.
- [ ] Modelled participants/replacements, exposure, rate, matchup and context.
- [ ] Retrieved up to five predeclared D0 mechanism matches or recorded none.
- [ ] De-duplicated shared underlying events and upstream source lineages.
- [ ] Built lower/central/upper/material tail scenarios and kill paths.
- [ ] Ran the streak persistence-versus-reversion audit (G17.1) on every streak, Under/Over run, or series-prior used directionally, in both directions.
- [ ] For cricket: disclosed separate **TOSS FACT** and **STRIP/PITCH EVIDENCE** ladder attempts (RULES_CRICKET.md §2, DATA_SOURCE_REGISTER.md §6A), including upstream lineage, `COMPUTED`/`INSUFFICIENT_VENUE_HISTORY`, any `AUTOMATED_PITCH_METADATA`, and the bottom-line toss/strip/conditions statuses.
- [ ] Located every line against its corridor/ordinary branches and completed any aggregate component-budget arithmetic.
- [ ] Mapped W/P/L intervals, aliases, complements, overlap/gaps and dependence.
- [ ] Printed `P(¬R1 ∧ ¬R2)` for the top two, and `P(all fail)` with Fréchet bounds wherever 3+ rows share a driver, each with the single state named (`G-L17`, `G-L21`).
- [ ] Checked the **sign** of every row under its shared driver before calling rows jointly supported.
- [ ] Labelled every over/under row `FORCED_PAIR` or `FREE`, named the preferred side of each pair, and **derived** the push mass against the competition's own record (`G-L15`, `G-L22`).
- [ ] Derived every handicap row from `b_L` via the `G-L24` identity, with `b_L`'s `n`, source and date printed — or marked `BAND_NOT_DERIVED` and declined Rank #1.
- [ ] Printed the **venue's own current-season** `P(>L)/P(=L)/P(<L)` beside every total, and named a mechanism if the preferred side opposes it.
- [ ] For any total with an endpoint state (extra innings/time, shoot-out): printed `P(reach the endpoint)` and the endpoint's own distribution as a separate layer.
- [ ] Checked whether a competition site that returned HTTP 200 actually carried the fields, or only a JavaScript shell (`JS_ONLY — RENDER REQUIRED`) — a shell is a rendering escalation, not an unavailable source.
- [ ] Read `DATA_SOURCE_REGISTER.md` for an existing route **before** searching for one (`G-L14`).
- [ ] Ranked every valid unresolved row uniquely; added no-bet label if warranted.
- [ ] Identified the **highest-ranked over/under target and its preferred side from issue-time ranks**, and recorded it as `TOP_OU_REVIEW` candidate so a later loss or push triggers the enhanced review without re-deriving ranks after the result.
- [ ] Analysed potential winner independently.
- [ ] Made no probability/value claim beyond current validation and price gates.
- [ ] Refreshed state/participants/weather/price just before issue.
- [ ] Appended the immutable Markdown view before delivery, if authorised.
- [ ] Cited current claims and disclosed unknowns/conflicts/source limits.
- [ ] **At settlement:** opened the structured process record (shots/on-target, inning splits, phase runs, quarter scores) and the disruption facts (red cards, sin bins, injury exits, stoppages) **with minute and score**, and classified the card as a *process* failure or a *conversion / endpoint / disruption* outcome before amending any control (`G-L23`).
- [ ] **At settlement:** ran `python audit_card_controls.py <log.md> --settlement` and recorded the per-card completeness result (§16.8).


This checklist is the fill-in prompt; no separate template file is maintained. (A prior revision of this guide referenced a standalone `UPCOMING_GAME_PROMPT_TEMPLATE.md`, which does not exist anywhere in this repository — that dead link is corrected here rather than left to fail silently.)


## September 5 settlement and final-delivery amendment


Use RULES_GENERAL §12 and L-068–L-071. On a settlement sweep, first-check LIVE items are recorded and deferred to the next query without row grading/retrospective; proceed to the next ID. At the next query, repeat the state-first check. Record observed state separately from delivery-time state.


Before finalising a card, independently sum every set/quarter/inning/phase example and evaluate its rows. Enforce the strictest unresolved role/XI gate in the final rank table. Include both competitors' supported winning/separation states and both early/full total split directions. Timestamp late availability reports; do not turn an un-timestamped postgame fact into a known-at accusation.


In settlement, keep completed research outcomes separate from operator/provider/action follow-ups and expose both in the top queue. Generate one chronological row per canonical ID plus explicitly noncanonical local records. Do not silently hide P-273-like provisional stat ownership or P-274-like conditional listed-pitcher action under a “fully settled” heading. Historical source instructions remain evidence; the current user's request controls the scope.


## September 5 user confirmation — controlling eligibility correction


[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md). The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.


Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.


The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.


Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.


Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.


## Complete Markdown recording requirement


**Standing user instruction:** all audit changes, updates, learnings, rule changes, instructions and logs must be recorded in the Markdown documents. The `.md` set is the complete human-readable authority. Scripts, JSON and CSV are validation/data companions, not the only record of a decision.


For each future change, update the active prediction log, the specific sport rule document or RULES_GENERAL for cross-sport controls, LEARNING_REGISTER for disposition, and relevant method/source/workflow documents in the same pass. Append a dated, source-linked retrospective with original ranks, results, what went right/wrong, knowability, prior lessons and the exact adopted change. Record pending fields and live-at-first-check deferrals in the active queue. Preserve original issued cards and label superseding corrections. Document validation and link the changed Markdown files in the audit change log before delivery.


Current implementation: [September 5 audit change log](AUDIT_CHANGELOG_2026-09-05.md).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->


## 2026-09-19 mandatory pregame research sequence — independent forecast before line comparison


For all new research under **MDS-2026.09.19-v4.3 / CR-2026.09.21-1**, use this order:


1. **Parse identity and contract only.** Record the requested total/spread/alternate line, period and settlement definition under `CONTRACT_ONLY_QUARANTINE`.
2. **Hide the threshold from forecasting.** Do not inspect odds, implied probabilities, line movement, market consensus, betting previews/picks/tips, fantasy/DFS projections/rankings/ownership, or derivative articles based on them.
3. **Collect sporting state from permitted sources.** Prioritize league/competition, team/club, player/federation and official match-center records. Use independent specialist/statistical sources only for fields they can actually support. Record source class, field owner, lineage, timestamps, freshness and retrieval status.
4. **Resolve critical volatile state.** Lineups/rosters/starters/scratches/toss/goalkeeper/QB/weather/venue activation and analogous items must be current. If the field owner is unavailable, seek two independent high-quality lineages; otherwise preserve uncertainty rather than importing a fantasy/betting projection.
5. **Build features without the line.** Mechanism-level inputs (participant strength/exposure, opponent interaction, venue/environment, workload/rest/travel, tactical/role state and sport-specific process measures) may enter. Recent outcomes are descriptive unless connected to a tested mechanism.
6. **Produce one coherent event distribution.** Store centre/shape/uncertainty, scenario weights where used, participant/phase marginals and distribution hash. Do not manually steer the centre toward or away from the requested threshold.
7. **Freeze the distribution.** Only after the freeze may the quarantined line be reintroduced to calculate `P(over)`, `P(under)`, `P(push)` or cover/fail/push probabilities.
8. **Run preflight.** `prediction_preflight.py <manifest.json>` must pass. Version mismatch, line leakage, prohibited source, unknown lineage, post-cutoff data, stale critical input or insufficient independent evidence is blocking.
9. **Rank from the frozen probabilities**, then log before delivery. Market information cannot alter the frozen sporting forecast.


### Search/discovery hygiene


Search engines, aggregators and social posts may locate a source but do not become evidence merely by being discoverable. Open the upstream record. If a search result points only to sportsbook/fantasy/tipster content, discard it. When no valid upstream fact exists, record `UNAVAILABLE_FROM_VALID_SOURCE`.


### Minimum source receipt per material fact


`source_id | provider | source_class | field_name | field_owner | upstream_lineage_id | first_known_at | retrieved_at | cutoff_at | freshness_status | snapshot/content reference`


This receipt is part of the forecast record. A citation list without field-level provenance is insufficient for a performance-eligible build.


## 2026-09-21 mandatory cricket toss/pitch retrieval sequence — CR-2026.09.21-1


This section supersedes earlier “six-rung” wording for new cricket cards. It is a source-integrity workflow, not a predictive weighting rule.


### Stage A — identity and official routing
1. Resolve exact event, competition, venue, official venue-local date/time and official match/event ID.
2. Identify the field owner: ICC, national board, league/competition or sanctioned scoring partner.
3. Open the exact official event page.
4. Identify any official `Watch`, broadcaster, stream or verified video route.


### Stage B — pre-toss strip search
Run the event/venue searches needed to find:
- exact-match official/board/competition pitch material;
- `"<venue>" pitch report`;
- `"<venue>" curator`;
- `"<venue>" groundsman` / `groundstaff`;
- specialist exact-match “pitch and conditions” reporting;
- named reputable cricket journalism.


A dated venue profile that is not today's strip is `HISTORICAL_VENUE_TENDENCY`, not `OBSERVED`.


### Stage C — official video/broadcast search
Search the verified board/competition/rightsholder video channel for the exact match and terms such as `toss`, `pitch report`, `Toss & Pitch Report`. Verify account ownership; a title alone does not make a channel official.


### Stage D — toss-window refresh
At the competition's actual toss window:
1. refresh the official match centre / sanctioned scorecard;
2. refresh official/rights-holder video;
3. query the admitted structured toss/XI endpoint where available;
4. open specialist live commentary;
5. refresh official team/competition updates;
6. record toss winner, decision, XI status and exact-strip evidence **separately**.


### Stage E — final pre-issue refresh
Immediately before delivery refresh:
- event state;
- toss;
- confirmed XIs / late changes;
- exact strip;
- venue-local weather/radar;
- source conflicts/staleness;
- upstream-lineage de-duplication.


If scheduled start has passed, reclassify event state before issuing anything.


### Mandatory cricket evidence block


```text
TOSS STATUS:
- Status:
- Winner:
- Decision:
- XI status:
- Source:
- Upstream lineage:
- Retrieved at:
- Pre/post toss:


STRIP STATUS:
- Status: OBSERVED / NOT_FOUND_AFTER_SEARCH / CONFLICTING / STALE_ONLY
- Exact-match source(s):
- Speaker/author:
- Observation/report:
- Strip number if known:
- Same-strip reuse confirmed?:
- Automated metadata present?:
- Context-only evidence:
- Search ladder attempted:
- Missingness/conflicts:


MATCH CONDITIONS STATUS:
- Weather source:
- Match-window weather:
- Interruption/DLS risk:
- Dew/light only if evidenced:
- Conditions signals and independence:


SOURCE-LINEAGE CHECK:
- Qualifying event lineages:
- Pitch lineages:
- Suspected duplicate feeds:
- Search snippets used as evidence? NO
```


### Classification safeguards
- A previous same-venue match is `DIFFERENT_STRIP_CONTEXT` unless reuse is explicitly confirmed.
- A same-format venue baseline is `COMPUTED` with sample size or `INSUFFICIENT_VENUE_HISTORY`.
- Identical/near-identical unusual pitch blocks across front ends are a suspected shared upstream feed until proven independent.
- Unattributed feed-generated surface labels are `AUTOMATED_PITCH_METADATA`, not a human strip observation.
- A transcript of the same broadcast and the broadcast itself are one lineage.
- An official dynamic page can be `STALE` for one field while still owning another field.
- The toss decision is weak circumstantial context only; it never becomes the pitch report.


<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## All-sports audit-reconciliation step — 2026-09-21


Before finalizing research, check any historical audit/retrospective rule you intend to use against `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`. Apply only the current retained formulation. In particular, never use an older normalized-edge shortcut, O/U “one side won” success measure, universal probability cap, automatic rebound/hangover, `UNORDERED` escape hatch, bookmaker/fantasy evidence, or guaranteed venue-history fallback.


This is a governance step, not an additional model layer: the same sporting mechanism must not be counted twice merely because it appears in multiple dated audits.




<!-- GUIDE-CR3-DISTRIBUTION-QUERY-2026-09-21 -->
## CR-2026.09.21-3 audit-reconciled construction step


After source/participant/environment research and before ordering: construct one coherent sport-native joint event distribution or qualitative branch mixture, freeze it, then query each supplied target. Do not compute or rank from historical second-highest/median pseudo-tail sums, path-count/category shortcuts, a universal 40–60% separation floor, or a blanket `DISJOINT` ban. A dependence conflict triggers repair only when the underlying event object is actually incoherent.
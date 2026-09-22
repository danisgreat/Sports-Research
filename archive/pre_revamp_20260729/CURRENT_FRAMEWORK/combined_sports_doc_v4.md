# Combined sports research and prediction manual v4

Status: **ACTIVE**  
Effective date: **2026-07-17**  
Format: **portable, document-first**  
Supersedes for future work: the operational instructions in combined sports documents v2 and v3

## 1. Purpose and non-negotiable claim boundary

This manual governs pregame, in-play, team, player, derivative, and winner analysis. Its objective is to make decisions reproducible, honest, and easy to audit. It does not promise certainty, profit, or mistake-free outcomes. Sport is uncertain; the required standard is no invented fact, no hidden assumption, no false precision, and no rewriting history.

- Never say a pick is guaranteed, certain, or risk-free.
- Never invent a lineup, injury, weather report, pitch report, official, price, score, clock, market rule, or model probability.
- Separate verified fact, source-reported information, model output, analyst inference, and unknown information.
- If essential identity, state, market, settlement, or data is unresolved, use `PASS`.
- A disciplined pass is a valid result.
- Historical records are descriptive unless they meet the prospective validation rules in section 12.

## 1A. GOVERNING DIRECTIVE — price independence (added 2026-07-28, user-issued; supersedes any conflicting rule in this manual)

**Odds and prices are optional supporting evidence, not a prerequisite.** Use a price only where it genuinely aids the analysis — as a market-consensus cross-check, to identify a disagreement worth explaining, or where the question is explicitly about value. Otherwise analyse the event on its merits and do not rely on prices.

This overrides the contract-gating behaviour that had accumulated in this manual. Specifically:

1. **Absence of a price is not a reason to pass.** A `PASS` must be justified by insufficient *evidence about the event* — unresolved identity, unknown lineup or state, no model coverage, contradictory data. "No executable price was captured" is not, on its own, a valid basis for a pass, a lower rank, or a refusal to reach a view.
2. **Absence of a price is not a reason to leave an event ungraded.** Settle every completed event on the **verified outcome under clearly stated standard rules**, and label the basis. Record `NOT GRADED` only when the outcome itself is genuinely unresolvable — no line was ever supplied, the metric is undefined *and* uninferable, or the required statistic was never published.
3. **What price-free grading can and cannot measure.** It measures *directional and ranking accuracy*: was the call right about what happened. It cannot measure profitability, edge or expected value, because those are price-dependent by definition. Never present a directional record as a profit record, and never imply an edge over a market that was not examined.
4. **Push and boundary rules must still be stated.** Where a raw grade depends on a convention (a whole-number total pushing, a handicap landing exactly, a phase boundary), state the convention used and note that a different book could settle it differently. State it; do not let it block the grade.
5. **Prices remain useful for one thing in particular.** A large disagreement between the analysis and the market is a prompt to re-examine the analysis. Note the disagreement and its direction; do not adopt the market's view by default and do not treat a stale or non-time-aligned snapshot as evidence at all.
6. **Verdict vocabulary.** `LEAN` may no longer be justified by "price/contract limitations" alone (see §2); it must reflect genuine uncertainty about the event.

**Honesty requirements that this directive does not relax.** Complementary branches of the same market are never independent evidence; exactly one wins by construction and only the higher-ranked branch may count toward any ranking diagnostic. Rows that were `PASS` or `AVOID` were abstentions — grading their direction informs *ranking quality only* and must never be reported as selection performance or a hit rate. No post-cutoff fact may enter an original forecast. Original forecasts are never rewritten.

## 2. Required decision vocabulary

Use only these verdicts unless a settlement is being recorded:

- `SUPPORTED` — best available evidence points to the selection, with material risks disclosed.
- `LEAN` — some evidence supports it, but uncertainty or price/contract limitations prevent a stronger view.
- `PASS` — evidence, model coverage, market terms, or current state is insufficient for an actionable view.
- `AVOID` — evidence is materially adverse or the supplied option is inferior to another branch.

These are ordinal judgments, not implied percentages. Do not translate them into probabilities without validated calibration.

## 3. The complete workflow

### Step 1 — freeze the question

Record the sport, competition, teams or players, scheduled start, venue if known, market wording, line, forecast state (`PREGAME`, `LIVE`, or `POSTPONED`), and exact cutoff time with timezone. Resolve ambiguous team names or tournament labels before analysis.

### Step 2 — inspect the previous log

- If the previous event is live, upcoming, abandoned without a final ruling, or cannot be verified, label it `NOT GRADED` and continue.
- If it is final, settle it using the stated market rules and a reliable result source before using it as a lesson.
- Never infer a result from memory, a partial score, or a search snippet.

### Step 3 — resolve the market contract

Confirm regulation versus overtime or extra time, innings/overs/quarters included, dead-heat or push rules, listed-pitcher or player-start requirements, shortened-match treatment, and whether a displayed line is actually available. If the exact book rules are absent, state that limitation. A score threshold written as “points” is not automatically interchangeable with runs, goals, or fantasy points.

### Step 4 — build an evidence snapshot

Prefer primary sources. Record the cutoff beside every live or changeable fact. Minimum useful snapshot:

- event identity and current state;
- confirmed or projected availability and roles;
- venue, surface, weather, and ruleset where material;
- recent performance with opponent and sample context;
- market line and price if the analysis claims value;
- current live score, period/inning/over, clock, outs/wickets, possession or serve state for in-play work.

If a page does not expose its update time, say `SOURCE UPDATE TIME UNKNOWN`.

### Step 5 — identify dependence and contradictions

Mark options that are exact complements, mutually exclusive, overlapping, nested, or driven by the same thesis. Examples:

- Over 42 and Under 42 are complementary except for a push at exactly 42.
- Team -8.5 and opponent +7.5 leave an eight-run margin where both lose.
- A first-10-over over and full-innings over are correlated but not interchangeable.
- Match winner and a large favorite handicap share a winner thesis but have different tails.

Do not treat correlated selections as four independent confirmations.

### Step 6 — choose the model class

Use the sport-native rules in this document and the model framework. A simple Poisson distribution is a baseline, not a universal answer. Model the relevant exposure: possessions, drives, innings, overs, scoring shots, rallies, or minutes—not merely a season average.

### Step 7 — challenge the first explanation

For every supported pick, write the strongest plausible failure path. Check whether the evidence could instead support the opposite branch. Distinguish structural signal from one-game noise.

### Step 8 — rank the supplied choices

When the user asks for four picks from four supplied outcomes, rank all four, but recommend only the outcomes that clear the evidence threshold. It is acceptable for the card to contain one supported pick and three passes/avoids. Never manufacture four positive recommendations.

### Step 9 — log before delivery

Append a timestamped entry to `PREDICTION_RESULTS_LOG_v6.md`. Add one row per genuine forecast to `SPORTS_CALIBRATION_LEDGER_v3.csv`. A potential winner is a separate forecast if it is actually recommended.

### Step 10 — settle and learn later

Append the final result, settlement rule, source, and retrospective. Do not edit the original cutoff, evidence, verdict, probability, line, or explanation.

## 4. Required user-facing output

Each response must include:

1. Event and evidence cutoff.
2. Current state: pregame or exact live state.
3. Ranked selections with `SUPPORTED`, `LEAN`, `PASS`, or `AVOID`.
4. A potential winner, or `NO WINNER PICK` if not defensible.
5. The most important verified facts.
6. The strongest risks and unknowns.
7. Model status: validated quantitative model, research-only model, or qualitative analysis.
8. A plain-language bottom line.

If prices are unavailable, analyse likelihood only; do not claim betting value. A likely outcome can be a poor bet at a bad price.

## 5. Live-analysis rules

Live analysis decays quickly. Every update is a new frozen snapshot.

- Show score, clock/period/inning/over, outs/wickets, batting/serving/possession state, and source cutoff.
- Use only information visible before the cutoff.
- Treat a suspended price as context, not a tradable quote.
- Recalculate the target: required future runs, points, goals, wickets, games, or margin.
- Weight remaining opportunities and game state more than pregame averages.
- Account for tactical changes: bullpen quality, chase rate, foul/penalty environment, substitutions, weather, red cards, field position, or intentional late-game scoring mechanisms.
- Never overwrite the earlier live view. Append a new update.
- If the feed is stale, contradictory, or missing a critical state variable, pass.

## 6. Retrospective learning rules

A result alone does not prove the reasoning was good or bad.

For every settled forecast, answer:

1. Was event and market identity correct?
2. Was the result settled under the recorded rules?
3. Which assumptions were verified, unverified, or wrong?
4. Was the forecast right for the stated reason, right for a different reason, or merely lucky?
5. Did a known tail event occur?
6. Is the lesson supported by repeated data or only one match?
7. What exact process change follows, if any?

One event may create a hypothesis but not a universal rule. Promote a lesson only after repeated evidence or a defensible mechanism.

## 7. Recurring failure modes inherited from the historical logs

The legacy logs contained useful warnings. They are retained here without preserving the old scoring system.

- Exact-winner overconfidence: a narrow favorite edge is weaker than a broad non-loss or cushion outcome, but the safer market may be overpriced.
- Forced complements: selecting both sides of a total or handicap can create a cosmetic hit rate and destroys independence.
- Overlapping lines: two opposite-team handicaps can both lose in a gap; draw the settlement intervals explicitly.
- Phase-to-full extrapolation: a fast start does not guarantee a full-game over; wickets, substitutions, bullpen quality, pace, and game script can reverse the path.
- Full-game-to-phase extrapolation: a high full-game expectation does not automatically support a first-period or powerplay over.
- One-factor stacking: weather, form, an injury, or a returning star must not be used to justify several correlated picks without separate mechanisms.
- Narrative suppression: a “cold offense,” “ace pitcher,” or “slow pitch” story does not eliminate blowout, bullpen, overtime, conversion, or late-foul tails.
- Venue average misuse: long-run venue averages can conceal rules, era, opponent, surface, and lineup changes.
- Rendered-date error: publication date is not necessarily data currency.
- Chat/log mismatch: the delivered ranking and logged ranking must match exactly.
- Result leakage: no post-cutoff fact may enter the original forecast record.
- Small-sample lessons: one opener, one innings, or one match is weak evidence without shrinkage.

## 8. Sport-specific analysis modules

### 8.1 Baseball

Model units: plate appearances and innings; use run-environment or negative-binomial/empirical alternatives when variance exceeds Poisson.

Required checks:

- confirmed starting pitchers, pitch count, rest, handedness, recent workload and role;
- expected lineups and key absences;
- park, roof, temperature, wind and altitude;
- bullpen availability by recent pitches and leverage usage;
- defense, baserunning and umpire only when reliable;
- home batting entitlement and extra-inning/mercy-rule contract;
- live: inning half, outs, runners, current pitcher, bullpen path and remaining plate appearances.

Lessons:

- A replacement starter plus a taxed bullpen can create early and middle-inning over paths, but do not double count the same weakness.
- A large early score raises the observed total but may reduce late offensive urgency and change pitcher usage.
- A favorite leading by the run-line margin is not “safe”; model remaining innings and home-team batting entitlement.
- MLB, NPB, KBO, LMB and other leagues require league-specific run environment, roster, schedule and rules. Do not transfer an MLB calibration to LMB.
- **2026-07-28 (from V6-020, repeating V6-010):** a starter's poor season ERA/WHIP plus one recent blow-up is not a run-environment forecast. Venue-adjust every cited recent start — an 8 ER outing at Coors Field is not transferable — and name both bullpens' recent workload before ranking any total above `PASS`. Two viable starters beat a team-rates blend twice in six days at the same 8.0 line.

Active status: a documented qualitative module is available. Numeric probabilities require league- and market-specific validation.

### 8.2 Cricket

Model units: ball, over and wicket state. Use state-dependent run/wicket processes, innings simulations, or empirical analogues; simple full-innings Poisson is normally inadequate.

Required checks:

- format, innings, target, overs and revised-target rules;
- toss, confirmed XI, batting order and bowling roles;
- actual match-specific pitch report versus generic venue preview;
- boundaries, dew, wind, weather and interruption risk;
- recent team and player form with format and opponent quality;
- live: score, overs, wickets, batters, required rate, resources, phase and remaining bowling matchups.

Lessons:

- A wicketless powerplay supports current resources but does not guarantee a full-innings over.
- Clustered wickets require immediate re-anchoring; do not average them away.
- Phase and innings totals are correlated but distinct.
- For first-X-ball or first-innings cricket markets, freeze the book-defined scoring metric, exact ball boundary, extras treatment and shortened-innings rule. A 25-ball powerplay total must not be inferred from a full-innings price.
- In a chase, winning probability and individual batter props depend on remaining target and opportunity; a short chase can cap volume.
- If the toss, XI, pitch or weather is unknown, widen uncertainty rather than guessing.
- **2026-07-28 (from V6-019):** a captain choosing to field is expressing a chasing preference, not forecasting a low first-innings score. Do not cite a bowl-first toss as evidence for a first-innings or powerplay under without a match-specific pitch report or a documented venue chase-bias. Phoenix made 54/0 in the 25-ball powerplay and 214/4 from 100 balls after Trent Rockets bowled first.

- **2026-07-29 (from V6-021):** the venue-baseline control worked prospectively for the first time — MSG made 181/3 at Headingley against a 161.5 line after 138/9 at Lord's with an identical XI, and the 25-ball powerplay went 41 against a 39.5 line. **Both correct calls rest on the same venue adjustment applied to two positively correlated markets: that is one observation with two readings, not two confirmations,** and the powerplay margin was 1.5 runs. Treat the control as supported by one clean application and a plausible mechanism, not as a rule, and never let the innings and powerplay rows count as independent evidence for each other.
- **2026-07-29 (from V6-021, winner picks — applies to all sports, see §10):** **an n=1 venue bat-first/chase-order signal may not be cited in a winner case.** The V6-021 lean on MSG rested partly on "the one match at this venue was won by the side batting first"; Sunrisers Leeds then chased 182 in 88 balls. A high-scoring venue that supports an innings-total over **simultaneously helps the chasing side** — using the same venue fact in both directions on one card is a contradiction, not two arguments.

Active status: qualitative ODI/T20 pregame and chase-state modules are available. Numeric claims require format-specific backtesting and calibration.

### 8.3 Soccer

Model units: possessions, shots and goals; suitable candidates include hierarchical expected-goals, bivariate/Dixon–Coles score models, and event simulations.

Required checks:

- competition, leg/aggregate context, regulation versus qualification market;
- confirmed lineup, goalkeeper, formation, set-piece roles and minutes expectations;
- rest, travel, rotation and incentives;
- shot quality, shot volume, field tilt, pressing and opponent-adjusted form;
- weather, pitch and referee only when sourced;
- live: score, clock, red cards, substitutions, shot quality and tactical state.

Lessons:

- Regulation winner and “to advance” are separate markets.
- An elite opponent’s shot-on-target suppression should reduce confidence in a star 1+ SOT prop unless role or volume offsets it.
- Team corners can clear while match corners fail if the opponent contributes very little.
- A red card changes both expected scoring and possession asymmetrically; do not apply a universal over adjustment.
- **2026-07-28 (from V6-018):** in a friendly across divisions, a published rotation/reserve-squad notice widens uncertainty on margin, scorers and minutes but does not erase the class gap on result direction. A rotated FC Twente XI won 0-3 at FC Emmen. Separately, a corners market with no supplied line is unsettleable rather than merely unattractive: neither club's official report published a corner count, so no raw mapping exists even after the final.

Active status: qualitative match, total and common derivative modules are available for competitions with adequate data. Numeric probabilities remain competition- and market-specific.

### 8.4 Australian football (AFL)

Model units: scoring shots, field position and conversion, with venue and game-state effects. Total points are overdispersed and simple Poisson is rarely sufficient.

Required checks:

- venue dimensions, weather and roof;
- confirmed teams, late changes, ruck and key-position matchups;
- inside-50s, clearances, contested possession, intercepts and scoring-shot quality;
- travel, rest and substitutions;
- live: quarter/clock, score, inside-50 territory, scoring shots and conversion sustainability.

Lessons:

- A big halftime lead plus territorial dominance can widen second-half margin tails.
- One early goal should not flip a handicap view without repeatable territory or scoring-shot evidence.
- Separate scoring-shot creation from conversion luck.
- Large leads can produce either continued dominance or tempo reduction; model both branches.

Active status: qualitative side, margin and total modules are available. Numeric output requires AFL-specific time-ordered validation.

### 8.5 Rugby league / NRL and comparable competitions

Model units: sets, field position, line breaks and compound scoring events; points are not well represented by one homogeneous Poisson process.

Required checks:

- exact competition and rules, not just “rugby”;
- confirmed squads, spine, halves, hooker, fullback, middle rotation and late changes;
- rest, travel, weather, venue and referee only when sourced;
- completion rate, metres, play-the-ball speed, field position, tackle breaks and defensive integrity;
- live: score, clock, possession, field position, sin bins, interchange and fatigue.

Lessons:

- A reverse-fixture blowout is context, not a reusable expected margin.
- Handicap lines and totals can share a blowout thesis; disclose the dependence.
- A weak defense can support both favorite and over paths, but favorite dominance can also suppress the underdog contribution.
- Competition-specific data is mandatory; do not transfer an NRL model directly to Super League or a cup fixture.

Active status: qualitative NRL and rugby-league modules are available where competition data and rules are resolved. Numeric probabilities require competition-specific validation.

### 8.6 Basketball

Model units: possessions, lineup combinations and shot outcomes.

- Confirm availability, starting lineup, minutes limits, rest and rotation incentives.
- Use pace, offensive/defensive efficiency, shot profile and free-throw rate, opponent adjusted.
- In developmental or Summer League competitions, apply heavy shrinkage because roles and rotations are unstable.
- Quarter, half and full-game totals have different game-script and late-foul mechanisms.
- Blowouts can reduce star minutes while late fouling raises totals in close games.

### 8.7 Ice hockey

Model units: shots, expected goals, goalie performance and score state.

- Confirm starting goalie and rest.
- Use special teams, shot quality, travel and back-to-back context.
- Empty-net scoring creates a distinct late tail.
- Moneyline may include overtime/shootout while regulation markets do not.

### 8.8 American football

Model units: drives, field position and scoring-event type.

- Confirm quarterback, offensive line, pass rush, skill positions and weather.
- Use pace, early-down efficiency, explosive plays and red-zone performance with opponent adjustment.
- Game script changes play selection; totals and spread selections are dependent.
- Garbage time, kneel-downs and overtime must match the contract.

### 8.9 Rugby union

Model units: possessions and compound scoring events.

- Resolve competition rules, squads, goal kicker, scrum/lineout, discipline and weather.
- Tries, conversions and penalties are dependent scoring sequences.
- Red/yellow cards and tactical kicking can change tempo nonlinearly.

### 8.10 Tennis

Model units: points, games and sets using serve/return state and a Markov structure.

- Confirm surface, fitness, format, retirement rules and serve/return splits.
- Adjust for opponent quality and small samples.
- A match winner and set handicap are related but not equivalent.

### 8.11 Volleyball

Model units: rallies and sets.

- Confirm format, lineup, setter/opposite availability and home/travel context.
- Model side-out and break-point probabilities; total points depend on set count and close-set extensions.

### 8.12 Golf, motorsport and combat sports

- Golf: use hole-level scoring distributions, course fit, weather-wave effects, field strength and cut rules.
- Motorsport: use qualifying/race pace, grid, reliability, degradation, weather and survival/rank models.
- Combat: use style interaction, round duration, finish/survival hazards, judging and weight/fitness information.
- For all three, avoid naive Poisson treatment of ranks, placements, or time-to-event outcomes.

## 9. Player-prop rules

Player forecasts require opportunity before rate:

1. Confirm active status and likely role.
2. Project minutes, plate appearances, balls faced, overs, carries, routes, shots, or other exposure.
3. Estimate performance rate conditional on opponent and context.
4. Model substitution, injury, blowout, weather and tactical tails.
5. Check settlement rules for starts, voids, dead heats and shortened matches.

Do not recommend a player because of name recognition or one recent outlier. If role is unconfirmed, pass or give a conditional view.

## 10. Winner-pick rules

A requested potential winner is not mandatory if the evidence cannot support one.

- State whether the market means regulation, including overtime, series, qualification, or match result.
- Prefer `NO WINNER PICK` when event identity, lineup, state, or model coverage is unresolved.
- Do not attach a numeric win probability merely to make the answer look complete.
- Winner and handicap picks must be logged separately if both are recommendations.

## 11. Data and source discipline

Use the source registry. Source order is generally:

1. official competition, team, venue, weather or governing-body source;
2. official data partner or event feed;
3. reputable specialist data/provider;
4. reputable reporting;
5. market screen as a timestamped price/state source;
6. search snippets or social posts only as discovery clues.

Two weak sources do not become a strong source. Conflicts must be recorded. A source used for a live fact must be checked at the live cutoff.

## 12. Probability, validation and calibration

A probability may be published only when all are true:

- the exact sport, competition, market and forecast state are covered;
- features are available as they would have been at the historical cutoff;
- evaluation is time ordered and out of sample;
- sample size and uncertainty are disclosed;
- calibration and proper scoring rules are reported;
- the current input is within the model’s supported domain;
- settlement and price provenance are known.

Otherwise publish qualitative verdicts. Model quality is judged by out-of-sample log loss/Brier score, calibration, sharpness conditional on calibration, coverage, and decision value at recorded prices—not raw hit rate alone.

## 13. Recordkeeping and settlement

The active record system is human-readable:

- Markdown prediction log: full context, evidence, ranking, update, result, retrospective.
- CSV calibration ledger: one row per genuine forecast or explicit pass.
- Current operational status comes from the open-event index and the ledger `result` field. A row whose historical `formal_status` contains `CONTRACT_UNVERIFIED` is closed when its `result` is `NOT_GRADED_CONTRACT_UNVERIFIED`; do not mistake that label for an open event.

Do not log both sides of a complementary market as independent model successes. Do not change a prediction after kickoff or after seeing a result. Corrections must be appended with timestamp and reason. Legacy headline accuracy is labelled `LEGACY_UNVERIFIED` and must not be used as current performance.

## Settlement reference updates — 2026-07-20

These are evidence-specific controls from completed records V6-003, V6-005, V6-008, and V6-010. They are process references, not model promotions or claims of predictive accuracy. Supporting sources and full retrospectives are retained in `PREDICTION_RESULTS_LOG_v6.md`.

| Sport / market | Completed-record finding | Reference rule added |
|---|---|---|
| LMB live totals and run lines | Diablos won 13-5 (18 runs). Over 17.5 and Under 18.5 both won at the different supplied lines, while Diablos -8.5 and Tigres +7.5 both lost at the eight-run gap. | Record every alternate line’s actual settlement interval. Gapped/overlapping contracts are not opposite picks and must never be used as independent confirmation. Early scoring must be challenged with a bullpen and late-innings cooling branch. |
| WNBA live quarter/half/full totals | The 8-5 state with 6:24 left in Q1 finished 47 in Q1, 91 at half, and 179 for the game. Three correlated under recommendations lost. | A sub-four-minute pace sample cannot support quarter, half, and full-game totals without possession, shot-profile, and active-lineup evidence. With no validated live model, cap this evidence at `LEAN` or `PASS`. |
| AFL side and total | Collingwood beat Carlton 90-69, covering -4.5 while the 163.5 over lost. Post-start injuries affected the game but were not forecast inputs. | Descriptive averages and a lone prior meeting are insufficient for a stronger total claim. Require scoring-shot, territory, and conversion evidence; never backfill post-cutoff injuries or game narrative into the original case. |
| MLB pregame total | Chicago beat Toronto 3-0. Burke threw 6 2/3 scoreless innings and Yesavage struck out nine in a quality start, so the Over 8.0 thesis failed. | Preserve starter quality in every total projection. A team-rates blend or one recent control event cannot outweigh two viable starters without transparent lineup/bullpen inputs and prospective validation. |

## Settlement reference update — 2026-07-23

This is an evidence-specific control from completed record V6-013. It is a process reference, not a model promotion or a claim of predictive accuracy. The final-state check, source links, and full retrospective are retained in `PREDICTION_RESULTS_LOG_v6.md`.

| Sport / market | Completed-record finding | Reference rule added |
|---|---|---|
| MLB pregame low total and side | Tampa Bay beat Toronto 12-2. Rays +1.5 and the Rays winner lean won; the two total branches were both `PASS`, although 14 runs cleared 7.5. Rasmussen gave up two runs in five innings, while Gausman exited after 3 1/3 innings and the Rays produced 21 hits. | At 7.5 or lower, document both the starter-exit branch and the opponent-lineup/bullpen branch. Do not let a scoring slump or one strong starter carry an under case when a high-contact lineup and short-outing route remain credible. Without price, bullpen inputs, and validated projection, conflicting total evidence stays `PASS`; postgame direction never upgrades it. |

## Settlement reference update — 2026-07-24

This is an evidence-specific control from completed record V6-016. It is a process reference, not a model promotion or a claim of predictive accuracy. The final-state check, source links, and full retrospective are retained in `PREDICTION_RESULTS_LOG_v6.md`.

| Sport / market | Completed-record finding | Reference rule added |
|---|---|---|
| Hundred first-X-ball and innings totals | Manchester Super Giants finished 138/9 from 100 balls, which is below the recorded 147.5 raw-run threshold, but the original market said “Points” and no book, price, metric definition, extras policy, interruption rule, or first-25-ball raw score was frozen. The four rows were all `PASS`. | At settlement, retain both the independently sourced raw phase/innings result and the original book-defined contract. If either is absent, close the record as `NOT GRADED — CONTRACT UNVERIFIED`; do not infer a phase-total result from the full innings and do not leave the row `PENDING`. |

## Settlement reference update — 2026-07-25

This is an evidence-specific control from completed record V6-017. It is a process reference, not a model promotion or a claim of predictive accuracy. The final-state check, source links, and full retrospective are retained in `PREDICTION_RESULTS_LOG_v6.md`.

| Sport / market | Completed-record finding | Reference rule added |
|---|---|---|
| KBO live full-game side, run line and total | KT beat Lotte 5-4 in nine innings. Standard raw mapping would make KT moneyline, Lotte +1.5 and Under 9.5 winners, but the original live book, price and settlement terms were never retained and all four rows were `PASS`. | On every full-game settlement, store the official final, innings/extra-innings status and a clearly labelled standard raw mapping. Formally grade only if the original sportsbook contract is retained. Otherwise close `NOT GRADED — CONTRACT UNVERIFIED`; do not use the raw mapping as a win/loss, calibration observation or model evidence. |

## Settlement reference update — 2026-07-28

These are evidence-specific controls from the 2026-07-28 settlement sweep of completed records V6-018, V6-019 and V6-020. They are process references, not model promotions or claims of predictive accuracy. All twelve rows across the three records closed `NOT GRADED — CONTRACT UNVERIFIED`; no hit rate, ROI or calibration observation is created. Live checks, source links, per-row raw mappings and full retrospectives are retained in `PREDICTION_RESULTS_LOG_v6.md`.

| Sport / market | Completed-record finding | Reference rule added |
|---|---|---|
| Cross-division club friendly, side / BTTS / totals / corners (V6-018) | FC Twente beat FC Emmen 0-3 with a rotated XI, Lammers scoring at 6, 18 and 85 minutes. The card passed on the winner largely because Twente's official notice restricted the squad to players who had sat out the previous night's European tie. The corners row was correctly refused and remains unsettleable: neither official report published a corner count. | In a friendly between clubs from different divisions, a published rotation/reserve-squad notice widens uncertainty on **margin, scorers and minutes**; it is not a reason to discard the divisional class gap on **match-result direction**. Log the class gap and the rotation notice as two separate inputs. A market with no line and no published post-match statistic (e.g. corners) must be declared unsettleable at cutoff, not merely passed. |
| The Hundred first-innings and first-25-ball totals (V6-019) | Birmingham Phoenix made 214/4 from 100 balls against a 141.5 threshold and 54/0 in the mandatory 25-ball powerplay against a 34.5 threshold, then won by 10 runs. Trent Rockets had won the toss and bowled, which the card cited as a plausible lower-scoring route, and both under branches were ranked first and third "administratively". | **A bowl-first toss is not a low-scoring signal.** In The Hundred and T20 it normally expresses a chasing preference, not a first-innings forecast; do not cite it for an under without a match-specific pitch report or a documented venue chase-bias. **An "administrative" rank is still a rank.** When a complementary pair cannot be separated **on the evidence**, log it as an explicit `UNORDERED PAIR` rather than assigning ranks 1 and 2 and disclaiming the ordering. Missing prices are not what makes a pair unseparable — missing evidence about the event is. |
| MLB pregame full-game total (V6-020) | Cincinnati beat St. Louis 4-2 in nine innings for six total runs against an Over 8.0 `LEAN` at rank 1. Lowder went 5.0 IP / 2 ER and May 6.0 IP / 1 ER / 8 K, falsifying an Over thesis built on both starters' season ERA/WHIP and their poor 18 July outings — one of which was an 8 ER start at Coors Field, carried at face value. The card contained no bullpen and no park input; the Reds' pen then threw four shutout innings. | **Venue-adjust every recent-start sample before it enters a total**, and state the park of each cited start on the card or drop the sample. **A total card must name both bullpens'** recent workload and availability before any total is ranked above `PASS`. **Re-application check:** restate the V6-010 starter-quality control by name on every MLB total card and show how the current case differs — V6-020 repeated V6-010's exact failure (same market, same 8.0 line, same thesis) five days later, so a written-but-uncited control is not a control. |
| All sports — informational winner leans | Across the sweep the "informational only, not a wager" winner lean was wrong in both cases where one was issued (V6-019 leaned Trent Rockets, Phoenix won; V6-020 leaned St. Louis, Cincinnati won), and in the one card that declined a lean (V6-018) the price favourite won 3-0. Both wrong leans rested on a price snapshot the card itself had already flagged as stale or not time-aligned. | An informational winner lean must meet the **same evidence standard as a formal pick** or be recorded as `NO WINNER PICK` under §10. A price snapshot the card describes as stale or not time-aligned may not be the sole basis for a lean. A "not a wager" label does not lower the evidence bar; it only removes the ledger row. |
| All sports — ranking discipline | Initially recorded as "rank 1 lost and rank 4 won, two of two" from V6-019 and V6-020 alone. **Corrected 2026-07-28** once V6-016, V6-017 and V6-018 were also raw-graded: across all six complementary pairs in the five records the higher-ranked branch won **three of six**. The earlier claim was drawn from the two records that happened to be in front of me and did not survive the full sample. | Before finalising any ranking, write the one-line case for the row placed **last**; if it beats the case for the row placed first, the ordering is wrong. Pairs that cannot be separated on the evidence are logged `UNORDERED`. **And: never generalise a slot pattern from the subset of records currently in hand — pull every comparable settled record first.** |
| All sports — recordkeeping order | The open-event index already showed V6-018, V6-019 and V6-020 as `CLOSED — NOT GRADED` with correct final scores, but no settlement section had been appended and all twelve ledger rows still read `result = PENDING`. Independent re-verification confirmed every index score, so the defect was ordering, not fact. Separately, those twelve rows carried a 23-field CSV width against a 22-field header, silently shifting `settled_utc`, `settlement_source` and `retrospective`. | **Index-before-settlement is prohibited.** A record may be marked closed in the open-event index only after its settlement section is appended to the log body *and* its ledger rows are updated in the same pass. **Ledger width check:** after any ledger write, assert that every row parses to exactly the header's field count before the file is saved. |
| All sports — contract capture | V6-016 through V6-020 are five consecutive records where no book, price or settlement rule was captured at cutoff, so all closed ungraded. | **Superseded on 2026-07-28 by §1A.** The diagnosis was wrong: the problem was never that prices went uncaptured, it was that the manual had made prices a precondition for both analysing and grading. All twenty rows were re-graded on verified outcomes under stated standard rules (see the 2026-07-28 re-grade in `PREDICTION_RESULTS_LOG_v6.md`). Do not reinstate a contract-capture gate. |

## 14. Copy-and-paste prediction template

```text
EVENT:
SPORT / COMPETITION:
START / VENUE:
STATE AND EVIDENCE CUTOFF:
MARKET TERMS:
PREVIOUS LOG STATUS:

1. [selection] — [SUPPORTED / LEAN / PASS / AVOID]
   Evidence:
   Failure path:
2. ...
3. ...
4. ...

POTENTIAL WINNER: [team/player or NO WINNER PICK]
MODEL STATUS: [validated quantitative / research-only / qualitative]
KEY VERIFIED FACTS:
KEY UNKNOWNS:
DEPENDENCE / COMPLEMENT WARNING:
BOTTOM LINE:
LOGGED AT:
```

## 15. Framework maintenance

- Add a new sport or market only after defining its unit of exposure, settlement, evidence requirements, challenger models, and validation plan.
- Record process changes in a dated audit file.
- Preserve superseded documents in the archive.
- Prefer a short rule with a reason over duplicated instruction blocks.
- Never tune a rule only to make the historical record look better.

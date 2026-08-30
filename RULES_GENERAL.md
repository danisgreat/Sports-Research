# General analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Method version: **MDS-2026.08.30-v2.7**
Numerical training specification: **NTS-2026.08.25-v0.2 — Stage 0 all-sports design/pre-fit**
Read with: AGENT_ROLE_AND_TASK.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.

## 0. Authority and record boundaries

Precedence:

1. current user directive;
2. honesty, identity, anti-hindsight, and mandatory-ranking invariants in AGENT_ROLE_AND_TASK.md;
3. explicitly marked hard gates in this file, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md; DATA_SOURCE_REGISTER.md, H0_DATASET_CARD.md, and NUMERICAL_MODEL_REGISTER.md control numerical approval/build state;
4. the relevant sport file within its sport-specific scope;
5. general defaults;
6. only PROMOTED entries in LEARNING_REGISTER.md.

Prediction logs, comprehensive retrospectives, dated audits, and archive files are evidence, not active instructions. README identifies the active prediction log; only that file's top Current controlling snapshot controls queue status and next ID. Historical OPEN/PENDING tables are not a task queue.

Issued views and settlements remain immutable. The top queue snapshot, current template, corrected aggregate snapshot, and explicitly identified duplicate storage are administrative and may be updated without changing an issued decision.

Canonical IDs identify distinct events, not headings or stored text blocks. Before append, reconcile the last canonical ID and event identity. If two issued cards reused an ID, preserve both issued labels and assign a one-to-one canonical alias map; never rewrite the original card. If two stored blocks are byte/text-equivalent copies of one card, mark later copies `DUPLICATE_STORAGE` and exclude them from event, contract, rank and winner counts. A skipped issued number does not create an event and may be used only through a documented canonical reconciliation.

## 1. Mandatory pre-research gate

Before opening a stats source:

1. read AGENT_ROLE_AND_TASK.md, this file, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, NUMERICAL_TRAINING_SPEC.md, and UPCOMING_GAME_RESEARCH_GUIDE.md;
2. read the relevant sport file;
3. read the PROMOTED controls and applicable TESTING rows in LEARNING_REGISTER.md;
4. read the log's top controlling snapshot;
5. inspect the newest relevant same-sport retrospectives for mechanism evidence, without treating their outcomes as weights.

Record the method version and applicable lesson/test IDs on the card.

## 2. Queue, game state, and time

Use named IANA time zones. Convert the official venue-local start through Australia/Sydney; do not hardcode AEST/AEDT month ranges or infer state from a date label.

For every queued ID:

- verified FINAL: append settlement and retrospective before forecasting the new event;
- LIVE: keep it open and move to the next queued/new event;
- postponed, suspended, or abandoned: preserve the exact state and contract implications;
- final before any forecast was delivered: close as NO FORECAST — FINAL BEFORE DELIVERY and exclude from performance.

A live contract may become mathematically decided before the event ends. Record that row as `MATHEMATICALLY WON` or `MATHEMATICALLY LOST — LIVE`, but keep the event OPEN until the field-owning final/termination settles every remaining row and confirms that no abandonment, correction or operator term changes the result.

For the new event print one state:

- GAME-STATE: PREGAME;
- GAME-STATE: LIVE — exact score/clock/period/inning/over and observation time;
- GAME-STATE: LIKELY COMPLETE — fetch the verified final before doing anything else.

### Start crossing

If the scheduled start passes during research, transition to live analysis. Preserve the user's original contracts, refresh the exact live state, recalculate remaining exposure, and keep incorporating new verified information through the final refresh immediately before logging/delivery. State that an original pregame line may no longer be offered.

If the event becomes final before delivery, stop forecasting and report the result. Never freeze a pre-start ranking merely because research began before the start.

## 3. Identity and contract hard gate

Before modelling, map the user's wording to:

- official event and provider ID;
- sport, competition, format, season and rules era;
- official participants, team aliases, innings/period/player identity;
- venue and home/away/neutral status;
- exact metric, line, phase, duration, and official statistic;
- regulation, overtime, extra-time, golden-point, shootout, extra-innings, DLS, shortened-event, listed-player, and void terms;
- operator rules when supplied, or explicitly labelled assumptions when not.

### Underlying target hard gate

Freeze the random variable before mapping its bookmaker thresholds:

- `target_id` and version;
- exact outcome, unit and feasible support;
- pregame, scheduled checkpoint, or live start state;
- endpoint and horizon;
- scheduled and uncertain exposure;
- termination, censoring, void and settlement rules.

Named-day output, remaining-day output, innings total, remaining-innings output, phase total, full-game total and match result are different targets. A model or corridor for one cannot be relabelled as another. A changed cutoff or endpoint requires a new view and, for a numerical system, a distinct target/horizon model ID.

When weather, mercy rules, declarations, target completion, curfews or another mechanism can end exposure early, model event-before-termination and termination-before-event paths separately. A shortening risk does not mechanically support an Under: scoring or separation already realised before the stop remains in the settled target, subject to the frozen competition and operator rules.

Run a unit/magnitude sanity check. Ask for clarification when an identity or contract is genuinely malformed; never silently repair it.

### Participant identity release gate

For every decision-driving role—starting pitcher, goalkeeper, quarterback, starting XI/lineup, toss/innings order, goalie, or equivalent—store the tuple `(official_event_id, team/side, role, official participant ID/name)` and one status: `CONFIRMED_OFFICIAL`, `PROBABLE_OFFICIAL`, `SECONDARY_ONLY`, `NOT_RELEASED`, or `CONFLICTING`.

- Only `CONFIRMED_OFFICIAL` may be described as confirmed.
- A field-owning league/team probable release may control a probable branch, but it remains distinct from a confirmed starter/lineup.
- A preview, aggregator, snippet, or unaffiliated reporter is discovery/corroboration only. If it is the only source for a decision-driving participant, model the role as unresolved, cap the row at `FORCED RANK` with at most `MEDIUM-LOW` evidence, and do not attach the mechanism to that named participant as fact.
- Immediately before issue, refresh the field-owning official source or documented official data partner and match the full event/team/role/participant tuple. A stale same-day preview may not survive this handshake silently.
- If the official source has not released the role, record `NOT_RELEASED`; if sources disagree, record `CONFLICTING` and branch or abstain. Never choose the participant that makes the forecast narrative cleaner.

Draw settlement intervals before ranking:

- half-point exact opposites have mutually exclusive wins;
- integer exact opposites can both push at the boundary;
- alternate lines may overlap;
- gapped lines may both lose;
- opposite-team positive handicaps can both win;
- a completed contract at issue is SETTLED_AT_ISSUE, unranked and performance-ineligible.

### Contract integration from one distribution

For an integer target `Y` with CDF `F(k) = P(Y <= k)`, a half-unit line is derived as:

- `P(Over k.5) = 1 - F(k)`;
- `P(Under k.5) = F(k)`.

At an integer line `k`, Over wins at `Y >= k+1`, pushes at `Y = k`, and loses at `Y <= k-1`; Under uses the reverse intervals. Preserve the exact push mass.

All nested and complementary contracts must come from the same distribution or qualitative corridor. A higher Over cannot receive a higher win probability than a lower Over, and a higher Under cannot receive a lower win probability than a lower Under. Independent line-by-line binary classifiers or calibrators may be diagnostic challengers only; they are prohibited as the main production engine unless recombined into and revalidated as one coherent CDF.

## 4. Sources, freshness, and access

### Authority hierarchy

1. governing body, competition, official match centre, team, venue, or government weather service;
2. official data partner;
3. reputable specialist statistical provider;
4. reputable named reporting;
5. timestamped market source for market state only;
6. aggregator, snippet, or social source for discovery.

Two weak sources do not make one strong source. Official sources control identity, rules, volatile releases, live state, and finals. A provider controls only the field it actually defines.

Authority is field-specific and still requires a valid source state. An official page that is visibly a stale schedule shell, zero-filled placeholder, unfinished live snapshot, internally impossible record, or superseded revision does not control that affected field merely because the domain is official. Record the conflict and retrieval time, seek an official correction/static report, then use two independent high-quality current sources provisionally if the field owner remains defective. Never convert placeholder zeros into a final score or niche-stat settlement.

Route sources by **claim ownership**, not a site-wide reputation score:

- official competition/team sources own official identities, rules, participant releases, game state, and finals;
- government meteorological services own their forecasts and observations, but the model owns the transformation from weather to sport mechanism;
- specialist providers own the definition of their proprietary or derived metric, not injuries, lineups, rules, or market prices outside their scope;
- the quoted operator/exchange owns its exact contract, terms, line, and timestamped price;
- reference sites, query engines, aggregators, previews, and search snippets are discovery/cross-check tools unless a field-specific source card says otherwise.

DATA_SOURCE_REGISTER.md controls candidate source roles, freshness triggers, fallbacks, access/use constraints, and numerical approval. A website visible through search is not automatically approved for automated collection, retention, redistribution, or H0 training.

### Acquisition order

Retrieve volatile facts first: event/state, contracts, rules, lineups/starters/toss, injuries/availability, and live data. Then acquire process history and context. Research depth must not crowd out a final volatile-information refresh.

Stop expanding the search when all decision-driving fields are either verified, explicitly missing, stale, or conflicting; the sport-native exposure/rate chain has enough evidence for an honest rank; the strongest ordinary contrary path is represented; and further searching is unlikely to change a rank before the next volatility refresh. “Comprehensive” means complete coverage of material decision fields, not an unbounded count of websites.

### Access ladder

When a page fails:

1. official structured feed/API or match centre;
2. official static page or gamebook;
3. reputable specialist source;
4. clearly labelled rendering/reader proxy, with cached-date verification;
5. available browser/computer access.

Record access failures per session and timestamp them. Never bake a claim that a particular website is always blocked or available into the model.

### Provenance

For every decisive fact separately store effective time, first-known/published time, live observation time where applicable, access time, feature age, provider/definition version, source/tier, transformation, predictive tier, conflict count, and missingness code. A fact first known or accessed after cutoff cannot enter the issued view even if it describes an earlier event. A cached or rendered fact cannot control a top or bottom rank until its event date and freshness are verified.

Prospective status requires a demonstrable immutable artifact created before settlement, not only an embedded issue-time claim. A card first available after final is `E1-Q-LATE_IMPORT`: keep the claimed time, first-demonstrable time, path/hash and settlement, but exclude it from prospective performance, calibration, model selection and prospective-test completions. A later-provided earlier artifact is handled by an appended provenance correction.

A file creation time proves only the file version actually recoverable at that time; it does not prove that every section later appended to that path already existed. For each forecast card, store a section-inclusive immutable receipt: content hash, append/revision ID, signed publication, or other artifact that demonstrates the card text before the result. If only a later whole-file artifact exists, use that artifact's first-demonstrable time for the card and quarantine it accordingly.

### Market snapshot semantics

A price/value claim requires the exact event and contract, operator/source, both sides where available, decimal odds, capture time, terms version, overround and de-vig method. The price snapshot must be no later than the forecast cutoff and stored separately from later opening/closing labels. A closing price observed after issue is a later benchmark only; it cannot become an earlier input. Odds without a trustworthy capture time are ineligible for value, CLV, calibration-baseline and model-promotion claims.

For any derivative or niche market, freeze the exact provider and definition before issue where the operator is known. If the operator is unspecified, name the research-grade provider/definition and label bookmaker settlement `UNKNOWN_DEFINITION`; do not silently reconcile providers after the result.

Every numerical build declares one of two tracks:

- **MARKET-BLIND:** no price, implied probability, consensus forecast, or market-derived feature enters the sports model; contemporaneous prices remain a later benchmark;
- **MARKET-INFORMED:** a same-time de-vigged market feature may enter the challenger, and every result must be labelled market-informed.

The independent and market-informed tracks must be evaluated separately. A market-informed model may improve forecast accuracy, but it cannot be presented as evidence that the sport-only features independently beat the market.

Settle from an official final. If genuinely unavailable, use two independent high-quality sources and mark provisional. Exact phases come from an official phase line or a legality-reconciled official event/delivery reconstruction, never from a full-game total.

## 5. Research and evidence weighting

Follow the data priority in MODEL_AND_DATA_SPEC.md.

### Historical development-set retrieval

Use D0 only through the eligibility and retrieval procedure in MODEL_AND_DATA_SPEC.md §4. Retrieve up to five genuinely comparable cases under a predeclared query; zero is valid and must be logged as `NO COMPARABLE CASE`. Historical outcomes never vote mechanically for a direction and never supply fitted probabilities, calibration, or raw analogue win rates.

### Recent data

Research recent source rows once, normally up to 20 where available, then build adaptive time-decayed and opponent/venue/participant-adjusted features. Compact L5/L10/L20 summaries are diagnostics, not three confirmations. Do not require an old H2H15 merely to fill a table.

For every statistic used directionally record:

- population and sample size;
- definition and rules era;
- opponent quality;
- venue/home-away context;
- participant/coach/role continuity;
- recency or decay;
- uncertainty and relevant missingness.

### Trend-mechanism audit

A streak is a description, not a law and not proof that reversal is due. When a streak influences a rank, identify at least three causes in the sport's exposure chain, state which persist or reverse today, and compare the ordinary contrary path.

### Regime-dominance audit

When current target-specific evidence conflicts with a broad season prior, ranking, reputation, venue average or old H2H, freeze both a baseline branch and a current-regime branch before ranking. Name the regime trigger—participant/role return, lineup/system change, surface, competition phase, defensive collapse, starter form, schedule asymmetry or similar—then record sample size, reliability, mechanism and the reason for the qualitative mixture weight. Fresh evidence is not automatically dominant, but stale aggregates cannot silently control after a demonstrated regime break. If the mixture cannot be justified, widen the corridor, lower evidence quality and keep any directional change as a prospective candidate rather than retrofitting a coefficient.

If a current-regime adverse branch is material enough to appear in the scenario map or kill path, the ranking rationale must explain why it remains subordinate to the selected row. Merely naming a supported failure branch and then letting broad cover counts, averages, reputation or old H2H control is not reconciliation. When that explanation cannot be made, reduce the evidence grade and move the affected complementary rows closer in the ordinal language; do not reverse them solely because the adverse branch later occurred.

### Outcome-conditioned and branch-completeness audit

Statistics conditioned on the forecasted outcome—such as a handicap cover rate only in games the team/player won—are descriptive labels, not independent evidence that the underlying win or cover will occur. Record the conditioning event and denominator, avoid counting it twice with the win record, and keep causal exposure/rate/matchup evidence primary.

Before ranking, enumerate ordinary control paths for both sides, close/competitive paths, and the material phase/set/period or overtime branches allowed by the sport. A favourite's failure path cannot be restricted to “favourite wins but fails to cover” when any opponent win defeats the same contract. The strongest kill path is the broadest ordinary adverse state supported by current evidence, not the narratively narrowest version.

### Participants and exposure

Confirmed roles and expected exposure outrank team reputation. Separate active, available, starting, expected workload, and replacement quality. Model branches for unresolved participants rather than assuming full participation.

Assign starter, bench, substitute, relief and replacement quality through expected minutes, shifts, possessions, plate appearances, balls, drives or other sport-native exposure by phase. A starting-unit advantage is not a full-event advantage unless its expected duration and the replacement phase support that conclusion.

### Context

Home field, travel, rest, schedule, weather, surface, officials, motivation, coaching comments, and external news are conditional modifiers. Each needs a verified pathway into exposure, rate, tactics, or variance.

Late-season or tournament incentive requires official standings, tiebreakers, remaining schedule, and the exact consequence. It remains modest unless observable selection or tactical evidence changes the event model. Never allege manipulation without strong evidence.

### Weather

Use venue-local match-window forecasts and observations, roughly one hour before start through one hour after expected finish. Record roof status and surface state. Rain, heat, cold, or wind has no universal total direction; trace its effect on the sport's mechanism, event timing and any termination/settlement path.

## 6. Forecast coherence and ranking

Use one joint event distribution or qualitative scenario corridor for the frozen target/state. State a competition/venue baseline before a total, then update participant exposure, opponent-adjusted process, matchup, context, and tails in that order. The underlying-target forecast is stored once; supplied thresholds are deterministic contract queries and do not become independent model-training rows.

For two-sided score events, decompose at least three linked questions before ranking: total event/scoring volume, allocation of that volume between competitors, and winner/margin. Evidence for a low total does not identify which side receives the limited scoring mass; evidence for a stronger side does not determine the total or the separation margin. Rank the contract that remains most robust across the supported allocation states, not the row that merely repeats the central total thesis.

When a future numerical model exists, prefer a stored PMF/CDF or posterior predictive sample over an unsupported mean plus standard deviation. A parametric mean/scale representation is acceptable only when its family, support, tails, calibration and held-out coverage have passed the target-specific gates.

### Ranking objective

Every well-formed unresolved supplied row receives a unique ordinal rank, pregame or live. If evidence is insufficient for a lean, use FORCED RANK with low evidence quality and NO VALUE DETERMINABLE. PASS, UNORDERED PAIR, or missing data may not replace a required rank.

Without usable prices, rank by marginal estimated win likelihood and robustness under the exact contract. Do not diversify or hedge the ordinal ranks. Hit@2 and union-win probability are diagnostics; an unordered coverage portfolio is separate and only available on explicit request under ALGORITHM_PORTFOLIO_AND_EVALUATION.md §9. Do not imply expected value. AVOID is evidence-relative, not a price claim.

### Ordering table

For each row record:

- exact contract and settlement interval;
- decision-set ID, candidate ID, origin, candidate-universe scope, and eligibility;
- adjusted empirical evidence with denominator;
- central mechanism;
- lower and upper tail;
- strongest ordinary kill path;
- unknown/missingness codes;
- dependence group;
- verdict, evidence quality, performance role, actionability, and probability state.

Only a validated model may publish probabilities. A genuinely running but unvalidated challenger may freeze SHADOW probabilities before the result under the technical protocol, but they remain hidden from the user-facing card. A model that did not run records NOT_GENERATED; never invent a shadow value. Otherwise publication state is NOT PUBLISHED — VALIDATION PENDING.

### Top and bottom checks

- A top row may be SUPPORTED only when fresh event-specific evidence clearly outweighs its strongest ordinary kill path.
- A required #1 can remain LEAN or FORCED RANK.
- Rank the last row relatively; do not treat rank #4 history as a fade prior.
- Write the best case for the last row and run the swap test.
- Near-tied branches remain near-tied in language even though their ordinal ranks differ.
- Run a two-sided branch-completeness check: each competitor must have an ordinary control/win path wherever the event rules permit it. If a row loses under every opponent-win state, at least one supported opponent-win branch must appear in its kill path.

### Dependence

Tag exact complements, pushes, overlap, gaps, nested lines, phase/full dependence, shared-player exposure, and same-thesis rows. One thesis expressed several times is one mechanism observation. Only one row per shared thesis can be PRIMARY_FORMAL; dependent rows are CORRELATED_SECONDARY, not hidden or ungraded.

Before two correlated derivative rows can occupy both top slots, compare them directly with every opposing full-target contract. Shared evidence alone cannot promote a phase, set, period, innings or alternate-line derivative above the opposing full-target branch; it needs independent target-specific evidence. If that evidence is absent, keep the rows ranked but lower the derivative's evidence/verdict and record the concentration concern.

When an earlier phase and full-event target are linked, pass the complete phase-end state into the next transition: score/output, resources remaining, participants and replacements, tactical/score state, workload and conditions. The phase result alone is not a ceiling or continuation rule; a slow phase with retained resources can accelerate, while a fast phase with depleted resources can suppress the finish.

### Potential winner

Name a potential winner for every valid active event. Analyse it independently from totals and handicaps. If its exact settlement terms match a supplied winner row, use the same contract ID and count it once. Use FORCED WINNER — LOW CONFIDENCE when evidence does not support a lean.

## 7. Live analysis

Live evidence decays quickly. Pregame and live models have distinct target/horizon/model IDs. A live forecast estimates the conditional future outcome from the exact observed state; it does not reuse a pregame row or extrapolate elapsed pace.

- Store score, period/clock or inning/over, outs/wickets/base/possession/serve state, and observation time.
- Recalculate required output against remaining possessions, drives, plate appearances, balls, overs, scoring shots, sets, or attacking sequences.
- Model later phases independently; a fast first segment does not automatically persist.
- Track substitutions, injuries, fouls/cards, pitcher/bowler state, timeouts/interchanges, tactical changes, and weather.
- Refresh immediately before logging and delivery.
- Append a new stable view ID; never overwrite an earlier view.
- Do not count multiple views of one event as independent outcomes.
- Official live match-centre or play-by-play state controls. If it is unavailable, two independent current sources must agree on participant orientation, score, phase/period/inning/set and clock or equivalent state before any live fact is used directionally.
- If live sources are stale, conflicting, one-source-only, or cannot establish that full state, record `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`. Do not issue a forced conditional rank from a merely internally consistent feed; preserve the supplied contracts and move on.

## 8. Logging, settlement, and evaluation

Log the view before delivery using the canonical Markdown schema in MODEL_AND_DATA_SPEC.md and the candidate/model fields in ALGORITHM_PORTFOLIO_AND_EVALUATION.md.

Every view records `target_id`, target version, definition, unit, start state, endpoint, exposure/termination rules and distribution/publication state. When one target has several lines, store one underlying forecast reference and multiple derived contract rows.

Record `selection_origin` as `USER_SUPPLIED` or `SYSTEMATIC_UNIVERSE`. The issued user slate must be frozen and ranked in full, but it is a selected decision set and cannot establish population-wide model performance. Numerical training/evaluation requires a preregistered eligible-event universe and a versioned candidate/alternate-line policy frozen before results. Post-result or post-forecast hunting for attractive alternates is prohibited.

Canonical performance roles are only:

- PRIMARY_FORMAL;
- CORRELATED_SECONDARY;
- INELIGIBLE.

Verdict, evidence quality, rank, and actionability are separate.

Settlement outcomes are only WIN, LOSS, PUSH, VOID, UNRESOLVED, or UNSETTLEABLE. Preserve operator terms where known. Otherwise separate research outcome from unknown sportsbook treatment. One documented official-stat retry is required before a niche-stat row becomes final UNSETTLEABLE.

Every summary separates:

- forecast events;
- views;
- pregame and live horizons;
- canonical contracts and aliases;
- primary and correlated rows;
- winner contracts;
- exact-pair ordering;
- pushes/voids/unresolved;
- proper-score eligibility.

Historical qualitative rows are not proper-score eligible. Directional counts are descriptive only. Boundary-sensitive rows remain full W/L/PUSH observations and receive full proper-score weight when an issued probability exists.

After writing a Markdown table, verify its header and row column counts.

Before combining or appending a component log, run an event-identity ledger audit: canonical ID uniqueness, participant/event uniqueness, issued-label aliases, byte/text duplicate detection, missing-number explanation, next-ID continuity, and queue reconciliation. Preserve supplied text once; do not multiply a duplicate block into performance accounting.

## 9. Retrospectives and method changes

Use the retrospective driver table in MODEL_AND_DATA_SPEC.md. Separate:

1. contract outcome;
2. process grade;
3. defect class;
4. knowability;
5. lesson/test disposition.

Audit every #1 loss. A single outcome does not prove calibration or require a confidence strike. Apply an immediate process lock only when a preissue identity/contract, source-transformation, arithmetic, temporal-leakage, settlement, or compliance defect is demonstrated. Clear the lock only after the error and affected method are corrected.

A process-defective view keeps its contract settlements for ledger integrity but is excluded from forecast/ranking performance, mechanism validation, model selection, calibration, and prospective candidate/test completions. A winning contract cannot validate reasoning that was conditioned on the wrong participant, event, state, target, or transformation.

For forecast weighting:

- one event creates a candidate;
- preregister the eligible population and frozen comparator;
- a five-case review is exploratory;
- promote only after chronological prospective scoring and useful uncertainty;
- scheduled aggregate underperformance against the frozen baseline triggers model review;
- record every change in LEARNING_REGISTER.md with method version and effective date.

Do not create dated case narratives in active rule files. The log and comprehensive retrospective hold case evidence; the learning register holds status.

## 10. Brief modules without a dedicated file

- **Volleyball:** set format, lineup, rotation, side-out efficiency; total points depend strongly on set count.
- **Golf/motorsport/combat:** event-specific exposure, cut/finish rules, grid/reliability, or style/round distribution; never force a Poisson score model.

Create a dedicated Markdown sport file only after the sport recurs enough to justify stable specialist controls.

Ice hockey, tennis and rugby union/sevens now have dedicated modules. Ice-hockey numerical candidates remain design-only and data-blocked; tennis and rugby union/sevens remain qualitative-only until explicit target/source/model cards are approved.

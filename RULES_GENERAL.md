# General analysis rules




> **CR-2026.09.21-3 current audit-precedence override:** [`archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md) remains the supersession map for historical audit findings. CR-3 additionally removes stale live gate text that survived the CR-2 prose reconciliation. Older text remains provenance only where superseded/rejected; duplicate findings must not be double-weighted.








> **2026-09-12: section 16.9 below corrects G-L8/G-L9/G-L10/G-L11 and participant/source provenance. It controls over the older formulations in section 16.5.**




> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This document remains the full gate reference — every gate ID cited by a historical card is defined here in full, and §16 is the current controlling gate classification. For the day-to-day process and the current ~12-item mandatory checklist, read `METHOD.md` §§3–4 and `RULES_GENERAL.md` §16 — not the full §§0–15 narrative unless a specific gate's history or exact wording is needed.




Status: **ACTIVE — FULL GATE REFERENCE; §16 IS CONTROLLING FOR WHAT IS MANDATORY**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3**
Executable algorithm: **GFA-2 (§11) — general forecast algorithm; sport instantiations are the SFA-<SPORT> sections in each sport file**
Numerical training specification: **NTS-2026.09.19-v0.5 — Stage 0 all-sports design/pre-fit**
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




<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal event-verification hard gate — CR-2026.09.19-4




For every sport and event, require **at least three distinct reliable upstream source lineages**. Mirrors, syndication, reposts, search snippets and generated summaries do not create independent sources. Where available, include a governing/field-owner exact-event source, a second primary/team/participant source, and an independent high-quality secondary source.




Before issue/refresh, verify venue/host, official venue-local date/time, IANA timezone and exact-date UTC offset, then convert timezone-aware to `Australia/Melbourne`, recording the correct **AEST/AEDT** label and calendar-date rollover. Treat user-supplied times as estimates until independently verified and print corrections explicitly.




Immediately before issue/refresh, verify event state across the qualifying source set. Credible disagreement produces `EVENT_STATE_CONFLICT` and fails closed.




Settlement requires **three distinct reliable lineages** agreeing on the exact event/date, explicit terminal state and final result. A score without a terminal marker is insufficient; any credible live/in-progress source blocks settlement. Search summaries cannot establish finality. Re-check immediately before any Drive status transition and read the written log back afterward.




Blocking labels include `SOURCE_COUNT_LT_3`, `SOURCE_LINEAGE_NOT_INDEPENDENT`, `EVENT_DATE_NOT_VERIFIED`, `EVENT_LOCAL_TIME_NOT_VERIFIED`, `EVENT_TIMEZONE_NOT_VERIFIED`, `MELBOURNE_TIME_CONVERSION_NOT_VERIFIED`, `EVENT_STATE_CONFLICT`, and `FINAL_STATE_NOT_VERIFIED_BY_3_SOURCES`. P-469 is the reference false-final failure case.




## 1. Mandatory pre-research gate


**Revised 2026-09-26 (`C-READING-GATE`).** The 2026-09-26 review measured the old gate at about 65,000 words per baseball card: this file, four numerical-programme documents, the whole sport file and the register. At that length controls were listed and not executed (M15). The gate is now two-tiered. **Nothing was deleted**: every dated section remains the reference text, and where a summary and its cited section disagree, the cited section governs and the summary is corrected (§0).


**Tier 1 — read in full before opening a stats source:**


0. `CURRENT_RULES.md`: the one-page live summary and map;
1. the sport file's **§0 live rules page** (every `RULES_<SPORT>.md` opens with one, consolidated 2026-09-26);
2. the active log's top controlling snapshot, and the day's declared universe where one exists (`C-EVENT-UNIVERSE`, §"2026-09-26"(c));
3. `UPCOMING_GAME_RESEARCH_GUIDE.md` §19, the one-page checklist.


**Tier 2 — open by citation, every time a card relies on it:** the numbered gates in this file (§2–§11, §16); the full sport-file section behind any control the card applies; `METHOD.md`; `SCORING_AND_VALIDATION.md`; and the PROMOTED/TESTING rows in `LEARNING_REGISTER.md`, found through `LEARNINGS_INDEX.md`. Inspect the newest same-sport retrospectives for mechanism evidence, never as weights.


**Model work only:** `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`, `NUMERICAL_PROGRAM.md`.


Record the method version, the manifest SHA and the applicable lesson/test IDs on the card.




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




Apply a timestamp invariant before issue: `PREGAME` is valid only when `cutoff_at < scheduled_start_at` after both timestamps are converted through their named time zones. At or after scheduled start, a schedule shell that still says upcoming, zero live games, or 0-0 is not evidence that the event remains pregame. The only permitted outputs are a verified live target/view, `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, or a verified final/no-forecast disposition. Record the source conflict and move on rather than preserving the stale pregame rank.




**Zero-play delay clarification (added 2026-09-04; restates `G5`, no method/weight change).** Once the scheduled start has passed, an event whose field owner shows a weather/venue/administrative delay with no snap, pitch, serve, ball, possession or other sport-native unit begun is `GAME-STATE: LIVE — DELAYED ZERO-PLAY`, not `PREGAME`. Record the field-owner event ID, delay status, score/clock or equivalent untouched start state, explicit zero-play evidence, observation time and next state-check time. Any view issued from that point is a new live target/version: preserve the supplied contract text, refresh operator postponement/abandonment/action terms, keep the full scheduled exposure as uncertain rather than elapsed, and re-run the live-state refresh immediately before delivery. If the owner cannot establish both the delay and that play has not begun, output `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`. This is a cross-sport state/target clarification only; it adds no direction, coefficient, scenario weight or confidence lift.




## 3. Identity and contract hard gate




Before modelling, map the user's wording to:




- official event and provider ID;
- sport, competition, format, season and rules era;
- official participants, team aliases, innings/period/player identity;
- venue and home/away/neutral status;
- exact metric, line, phase, duration, and official statistic;
- regulation, overtime, extra-time, golden-point, shootout, extra-innings, DLS, shortened-event, listed-player, and void terms;
- operator rules when supplied, or explicitly labelled assumptions when not.




### Competition rules currency and new-competition onboarding




The "Sport and competition rules reference" section of each `RULES_<SPORT>.md` (`§9`, or `§10`/`§11` where noted; cricket and soccer in `LEAGUE_RULES_CRICKET.md` / `LEAGUE_RULES_SOCCER.md`) is the frozen record of each competition's playing laws, format and settlement rules **as at its last review date**. Sports change their rules almost every year. Two checks are mandatory and are part of `G2` (`GATE-IDENTITY`), not optional research:




1. **Season-boundary rules-currency check.** When the event is the **first card of a new season, a new pre-season, a new tournament edition, or the first appearance of a competition after a break of roughly six weeks or more**, verify against the field-owning source (the league/federation site, the competition's published regulations, IFAB / World Rugby / ICC / FIBA / World Aquatics / the relevant body) whether anything below has changed since the last logged card in that competition, and update the relevant reference section **before** issuing the card:
   - **playing-law / playing-condition changes** — e.g. a competition-specific substitution rule such as the IPL Impact Player (present now, not guaranteed next season), ICC playing-condition revisions, NFL/NBA/NHL rule tweaks, kickoff or overtime changes, new card/discipline laws;
   - **competition-format changes** — playoff/finals structure, number of teams, promotion/relegation on or off, points and tiebreak system, split-league adoption, a **new stage or in-season event** (the NBA play-in tournament, in-season cups, a wildcard round, an expanded knockout), calendar or scheduling changes, expansion or contraction of the field;
   - **technology changes** — VAR, semi-automated offside, ABS/automated strike zone, Hawk-Eye Live, the Bunker;
   - **roster / eligibility rule changes** — import or foreign-player quotas, designated-hitter adoption, interchange caps, squad sizes, homegrown rules.
   Record the check on the card with the source and date. A card that silently carries a prior season's rules for a competition whose rules changed is a `GATE-IDENTITY` failure of the same class as the stale-method finding at `G0`.
2. **New-competition onboarding.** The **first time any competition is forecast**, its complete rules must be written into the relevant reference section first — playing format; how a winner is decided (regulation / overtime / extra time / penalties / Super Over / golden point / shoot-out / draw allowed); points and tiebreak system; playoff, finals or group structure; promotion/relegation; roster and import limits; and the settlement conventions for the contract types in scope. **Do not forecast a competition that is not documented there — document it, then forecast.**




Neither check is a method or weight change, so neither goes through the LEARNING_REGISTER.md promotion procedure; both are reference-documentation maintenance, done in the same session as the card that triggered them.




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




For every decision-driving role—starting pitcher, goalkeeper, quarterback, starting XI/lineup, toss/innings order, goalie, or equivalent—store the tuple `(official_event_id, team/side, role, official participant ID/name)` and one status: `CONFIRMED_OFFICIAL`, `PROBABLE_OFFICIAL`, `SECONDARY_ONLY`, `NOT_YET_DUE`, `OVERDUE_NOT_RELEASED`, or `CONFLICTING`. Also store `release_expected_at`, `release_checked_at`, the official release source/version, and `next_check_at` where another release is expected.




- Only `CONFIRMED_OFFICIAL` may be described as confirmed.
- A field-owning league/team probable release may control a probable branch, but it remains distinct from a confirmed starter/lineup.
- A preview, aggregator, snippet, or unaffiliated reporter is discovery/corroboration only. If it is the only source for a decision-driving participant, model the role as unresolved, cap the row at `FORCED RANK` with at most `MEDIUM-LOW` evidence, and do not attach the mechanism to that named participant as fact.
- Immediately before issue, refresh the field-owning official source or documented official data partner and match the full event/team/role/participant tuple. A stale same-day preview may not survive this handshake silently.
- If the official release deadline has not arrived, record `NOT_YET_DUE`; after it passes without a release, record `OVERDUE_NOT_RELEASED`. If sources disagree, record `CONFLICTING` and branch or abstain. Never choose the participant that makes the forecast narrative cleaner.




**Bench and coaching extension (added 2026-09-06 — `G14.2`, `L-082`).** The roles above are the *starting* set. The gate now also covers, for each side, with the same tuple/status discipline:




- **the full named bench / substitutes list**, together with the competition's substitution allowance (and any competition-specific concussion, tactical or extra-time substitution provisions from the `RULES_<SPORT>.md` reference section);
- **a bench-depth count** — how many named bench players have started at least 40% of that side's last ten fixtures — as a single integer, because "a bench exists" and "a bench that can change the game exists" are different facts;
- **the named head coach or manager for each side**, with an interim/caretaker flag and a note of any change inside the last five fixtures;
- **any confirmed rotation, rest, congestion or priority signal**: another fixture inside four days, a cup/league priority statement, a dead rubber, or a publicly stated rotation plan.




This was a live blindspot, not a theoretical one. In `P-304` (SK Slavia Praha 4-0 FC Zbrojovka Brno, 2026-09-05) **two of Slavia's four goals were scored by substitutes** — Ayaosi, who entered in the 26th minute as a *forced injury replacement*, and Jurásek, who entered in the 63rd — while two starters (Zima 20', Provod 26') were lost to injury inside the first half hour. Any margin or full-match total row on that card would have been driven primarily by bench quality, a field the framework did not require anyone to retrieve. Where the bench record is `NOT_RETRIEVED`, no margin or full-game total row may be ranked #1.




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




Asian quarter lines are split into two equal-stake child contracts before forecasting and settlement: `x.25` into the adjacent integer and half line, and `x.75` into the adjacent half and integer line in the direction of the handicap/total. The parent may settle `WIN`, `HALF_WIN`, `PUSH`, `HALF_LOSS`, `LOSS`, `VOID`, `UNRESOLVED`, or `UNSETTLEABLE`; store both child outcomes and do not collapse a half result into a full win/loss. Because prices are excluded from forecasting, ranking remains by the frozen sport-only objective and must state how fractional outcomes are ordered if a quarter-line row is present.




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




**Synthetic-content exclusion (hard, added 2026-09-06 — `L-079`).** Content that is generated, simulated, projected or previewed rather than observed is **tier E, diagnostic only, and may never settle a contract, establish a result, a score, a scorer, a margin, a venue or a participant**, regardless of how complete and report-like the narrative appears. This covers, non-exhaustively: anything labelled "AI simulation", "simulated", "projected result", "match prediction", "preview", "who will win", "Dream11", "fantasy tips", "expert tips", or produced by a model rather than a scorer/statistician; and it applies to the *article*, not the domain — a site may publish genuine reporting alongside synthetic pieces.




This is not hypothetical. On 2026-09-06 a web search for `P-305` (Dublin Guardians v Amsterdam Flames, ETPL Match 15) returned a `sportscafe.in` article headlined *"AI Simulation | DLG vs AMF | Dublin Clinch Six-Run Thriller"* reporting **Dublin 176/7 beating Amsterdam 170/7 by six runs, James Vince player of the match with 54 off 37, at Sportpark Duivesteijn.** The actual result was **Amsterdam 169/7 beating Dublin 160/8 by nine runs, Vince 73 off 46 for the losing side, Tim Pringle player of the match, at Sportpark Westvliet.** Every load-bearing field was wrong, including the winner. The article was internally coherent, correctly named both squads, and was ranked alongside genuine scorecards. **A settlement taken from it would have recorded the wrong winner.**




Two operational consequences follow:




1. A result must be taken from a **scoreboard, scorecard or box-score record**, not from a narrative article, whenever such a record exists. Narrative reporting corroborates; it does not settle.
2. A search-result *summary* that asserts a scoreline is not a source. Open the underlying record and check what kind of page it is before any figure from it enters a settlement. This generalises `L-074` (an AI-summarised *fetch* produced an internally impossible result) from the fetch layer to the search layer.




Authority is field-specific and still requires a valid source state. An official page that is visibly a stale schedule shell, zero-filled placeholder, unfinished live snapshot, internally impossible record, old head-to-head module rendered as the current game, malformed score/title slug, or superseded revision does not control that affected field merely because the domain is official. Match event ID/date/participants, page state, score chronology and revision freshness. Record the conflict and retrieval time, seek an official correction/static report, then use two independent high-quality current sources provisionally if the field owner remains defective. Never convert placeholder zeros or stale status labels into a final score or niche-stat settlement.




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




**Native-language sourcing, added 2026-09-04 (L-067).** For a competition whose primary reporting is not in English (KBO, NPB, CPBL, LMB and comparable), route a native-language search for same-day reporting alongside any English-language source before treating thin English-language results as the evidence ceiling. A native-language outlet is routed through the same authority hierarchy above by what it is (named reporting, official source, and so on), not exempted from it merely by language.




### Access ladder




When a page fails:




1. official structured feed/API or match centre;
2. official static page or gamebook;
3. reputable specialist source;
4. clearly labelled rendering/reader proxy, with cached-date verification;
5. available browser/computer access.




Record access failures per session and timestamp them. Never bake a claim that a particular website is always blocked or available into the model.




### Provenance




For every decisive fact separately store effective time, first-known/published time, live observation time where applicable, access time, feature age, provider/definition version, source/tier, transformation, predictive tier, full conflict set, conflict impact, and missingness code. Conflict impact is one of `IDENTITY_BLOCKING`, `THRESHOLD_CHANGING`, `DIRECTION_CHANGING`, `DIRECTION_INVARIANT`, or `NON_DECISIVE`. A fact first known or accessed after cutoff cannot enter the issued view even if it describes an earlier event. A cached or rendered fact cannot control a top or bottom rank until its event date and freshness are verified.




An organisation name, provider family, list of websites, search result or phrase such as “provider-style scorecards” is not a source record. Each decision-driving field must identify the exact record or URL, claim owner, field definition/version, value and unit, effective or first-known time, observed/accessed time, transformation, missingness and conflict state. An unnamed market baseline without operator/source, exact line, price, terms and capture time has no directional role.




Apply PERFORMANCE_ELIGIBILITY_POLICY.md. The user has confirmed that existing non-live issued cards were frozen pre-game; label their provenance USER_CONFIRMED_PREGAME_FREEZE and admit settled, identifiable rows to historical ranking evaluation. Preserve actual import times and hashes. Explicit live views stay in a separate horizon; settlement-time LIVE does not reclassify issuance. A new unconfirmed late import retains an unresolved provenance flag until its source basis is established. Never backdate an artifact or treat a hash alone as a timestamp.




A file creation time proves only the file version actually recoverable at that time; it does not prove that every section later appended to that path already existed. For each forecast card, store a section-inclusive immutable receipt: content hash, append/revision ID, signed publication, or other artifact that demonstrates the card text before the result. If only a later whole-file artifact exists, use that artifact's first-demonstrable time for the card and quarantine it accordingly.




### Bookmaker-independence hard gate




Every active forecast and numerical build is `SPORTS_ONLY / MARKET_BLIND`. Bookmaker/operator odds, implied probabilities, line movement, consensus prices, bookmaker previews, affiliates, tipsters and any market-derived feature are prohibited from the sports model, qualitative corridor, scenario likelihood, mechanism, kill path, confidence language and ordinal rank. They may not be used as a “sanity check.”




**Terminology clarification, added 2026-09-06 (`L-100`, external blindspot audit `B-14`).** `MARKET_BLIND` means **price-blind / market-analysis-blind** — no price, implied probability, line movement or market commentary enters the forecast. It does **not** mean market-independent in every sense: the user-supplied candidate slate and its exact thresholds are themselves market-produced objects, and threshold placement changes task difficulty. Any reported accuracy is therefore conditional on the supplied thresholds and candidate slate, not evidence of skill independent of what the market chose to offer. State this conditionality explicitly whenever historical accuracy is discussed; do not describe `MARKET_BLIND` performance as demonstrating predictive lift over the market.




An operator/exchange record may be used only to freeze an exact user-supplied contract, threshold, settlement terms and action/void definition. Its price is not prediction evidence. For derivative or niche contracts, freeze the research-stat provider independently from the operator; if the operator definition is unspecified, label bookmaker treatment `UNKNOWN_DEFINITION` rather than selecting a convenient provider after the result.




Only when the user explicitly requests it may prices be captured **after the sport-only forecast and ranks are immutably frozen** for a segregated audit of the offered terms. That audit cannot revise the forecast, rank, evidence grade or learning weight, and it remains outside active predictive validation. Bookmaker-authored analysis and affiliate/tipster content remain prohibited even in that audit.




Settle from an official final. If genuinely unavailable, use two independent high-quality sources and mark provisional. Exact phases come from an official phase line or a legality-reconciled official event/delivery reconstruction, never from a full-game total.




## 5. Research and evidence weighting




Follow the data priority in MODEL_AND_DATA_SPEC.md.




### Historical development-set retrieval




Use D0 only through the eligibility and retrieval procedure in MODEL_AND_DATA_SPEC.md §4. Retrieve up to five genuinely comparable cases under a predeclared query; zero is valid and must be logged as `NO COMPARABLE CASE`. Historical outcomes never vote mechanically for a direction and never supply fitted probabilities, calibration, or raw analogue win rates.




### Recent data




Retrieval of the last 5, 10, 15 and 20 completed events for both sides, and of the head-to-head series over the same windows, is **mandatory** under G13.1 and §11.3B. Store them once as a single windowed table per side plus one head-to-head table carrying its continuity count, then build adaptive time-decayed and opponent/venue/participant-adjusted features from them. The four windows exist to support the trend test in §11.3B, not to be reproduced as four prose tables. Nested windows describe overlapping sets of the same matches: they are one evidence unit under G9 and are never three or four confirmations. Head-to-head influences a rank only through meetings that pass the continuity gate.




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




### Streak persistence-versus-reversion audit




A streak cuts both ways, and both directions are fallacies without a named mechanism. Extrapolating a streak forward with no identified cause is the continuation fallacy that the trend-mechanism audit above already blocks. Assuming a streak must break, snap back, or produce a "comeback," "bounce back," or "due for a change" simply because it has run for N events — with no named mechanism and no evidence the underlying rate ever changed — is the mirror gambler's-fallacy error, and it is exactly as prohibited. This applies identically to a losing/under streak and a winning/over streak, to a single prior result in a multi-game series or two-leg tie treated as a cause of the next one, and to any language describing a side as "due." The full procedure is `G17.1` (§11.3E); the evidence-ceiling consequence is in §11.5.




### Regime-dominance audit




When current target-specific evidence conflicts with a broad season prior, ranking, reputation, venue average or old H2H, freeze both a baseline branch and a current-regime branch before ranking. Name the regime trigger—participant/role return, lineup/system change, surface, competition phase, defensive collapse, starter form, schedule asymmetry or similar—then record sample size, reliability, mechanism and the reason for the qualitative mixture weight. Fresh evidence is not automatically dominant, but stale aggregates cannot silently control after a demonstrated regime break. If the mixture cannot be justified, widen the corridor, lower evidence quality and keep any directional change as a prospective candidate rather than retrofitting a coefficient. Sparse, new-coach, new-role, early-season or roster-change uncertainty changes distribution width before it changes the central direction; shift the centre only when a current directional exposure/rate mechanism is identified.




If a current-regime adverse branch is material enough to appear in the scenario map or kill path, the ranking rationale must explain why it remains subordinate to the selected row. Merely naming a supported failure branch and then letting broad cover counts, averages, reputation or old H2H control is not reconciliation. When that explanation cannot be made, reduce the evidence grade and move the affected complementary rows closer in the ordinal language; do not reverse them solely because the adverse branch later occurred.




**Most-recent-meeting reconciliation, added 2026-09-04.** Before a reference-band downgrade or upgrade is applied on a "current regime" narrative, check it against the single most recent head-to-head meeting that passes the §11.3B continuity gate. If that specific meeting already points the other way from the proposed band move, write one explicit sentence reconciling the two — do not apply a general regime narrative that a card's own freshest, most continuity-qualified data point already contradicts. This does not create a mechanical rule that the most recent meeting controls; it requires the conflict to be seen and addressed rather than silently overridden by a narrative. (Candidate `C-PL13-ALL-REGIME-VS-RECENT-H2H`, LEARNING_REGISTER.md, drawn from P-270's Broncos +7.5 downgrade against a card that itself already showed Brisbane's most recent 2026 meeting going the other way.)




### Outcome-conditioned and branch-completeness audit




Statistics conditioned on the forecasted outcome—such as a handicap cover rate only in games the team/player won—are descriptive labels, not independent evidence that the underlying win or cover will occur. Record the conditioning event and denominator, avoid counting it twice with the win record, and keep causal exposure/rate/matchup evidence primary.




Before ranking, enumerate ordinary control paths for both sides, close/competitive paths, and the material phase/set/period or overtime branches allowed by the sport. A favourite's failure path cannot be restricted to “favourite wins but fails to cover” when any opponent win defeats the same contract. The strongest kill path is the broadest ordinary adverse state supported by current evidence, not the narratively narrowest version.




### Participants and exposure




Confirmed roles and expected exposure outrank team reputation. Separate active, available, starting, exact phase/score-state role, expected workload, and replacement quality. Model branches for unresolved participants rather than assuming full participation. A participant may be available yet irrelevant to the target phase or game state—for example, a batter outside the powerplay, a closer while trailing, or a reserve whose entry depends on score—so map role eligibility before applying quality.




Assign starter, bench, substitute, relief and replacement quality through expected minutes, shifts, possessions, plate appearances, balls, drives or other sport-native exposure by phase. A starting-unit advantage is not a full-event advantage unless its expected duration and the replacement phase support that conclusion.




### Context




Home field, travel, rest, schedule, weather, surface, officials, motivation, coaching comments, and external news are conditional modifiers. Each needs a verified pathway into exposure, rate, tactics, or variance.




When the event is one leg of a multi-game series, a two-leg tie, or a rematch scheduled within the same short window, record a series-state block before ranking: the prior result(s) and exact score/aggregate, which side is protecting or chasing the series/aggregate, and any disclosed rotation, bullpen/relief usage, lineup, or tactical consequence of the prior leg(s). A prior loss or a prior blowout is not itself a mechanism for the next leg; it is context that must route through a named exposure/rate/tactical pathway exactly as any other context factor, and it is subject to the streak persistence-versus-reversion audit below when it is used to argue either continuation or a "response."




Late-season or tournament incentive requires official standings, tiebreakers, remaining schedule, and the exact consequence. It remains modest unless observable selection or tactical evidence changes the event model. Never allege manipulation without strong evidence.




### Weather




The environment gate in §11.3C is mandatory and runs at step G15.1, before any total or margin is discussed. Classify the venue as `OUTDOOR`, `INDOOR` or `RETRACTABLE` with its roof state from the official source. Outdoor and open-roof events require a venue-coordinate hourly forecast in venue-local time from one hour before start through one hour after expected finish, carrying temperature, hourly precipitation probability and amount, wind speed, wind gusts, wind direction, relative humidity, dew point and cloud cover. Wind must be resolved to a vector against ground or stadium orientation before it can act directionally. Rain, heat, cold, humidity or wind has no universal total direction; trace each through the sport's mechanism, event timing and any termination/settlement path, and run the G22 bidirectional-sign audit where a factor can act both ways.




## 6. Forecast coherence and ranking




Use one joint event distribution or qualitative scenario corridor for the frozen target/state. State a competition/venue baseline before a total, then update participant exposure, opponent-adjusted process, matchup, context, and tails in that order. The underlying-target forecast is stored once; supplied thresholds are deterministic contract queries and do not become independent model-training rows.




For two-sided score events, decompose at least three linked questions before ranking: total event/scoring volume, allocation of that volume between competitors, and winner/margin. Evidence for a low total does not identify which side receives the limited scoring mass; evidence for a stronger side does not determine the total or the separation margin. Rank the contract that remains most robust across the supported allocation states, not the row that merely repeats the central total thesis.




Stress every side/total decision set across four ordinary score families: low-total/close, low-total/separation, high-total/close and high-total/separation. Do not infer a cushion from an Under or a blowout from an Over. Then run a mechanism-to-contract check: state the score or event path that makes Rank #1 win and verify that the strongest researched mechanism actually predicts every extra condition required by that contract. One-team dominance, total scoring, margin, territorial control and a niche event such as corners are not interchangeable.




Solve every margin, handicap and cushion row as a separation budget, in the same way an aggregate line is solved as a component budget. Split the scheduled exposure into the phases that actually allocate scoring — starter innings and relief innings, halves, quarters, periods, sets, powerplay and death overs — and hold each side's output in each phase at its floor, centre and ordinary high. A cushion is supported only when the opponent's ordinary high in the phases that generate separation still leaves the margin inside the line. A close head-to-head record, a low total, a favourite lean or a narrative about a tight game is not a separation budget.




Rank #1 defines a state, and every other row is evaluated inside that state as well as marginally. Once the order is provisional, convert the branches under which Rank #1 wins into the unit of every other supplied line — runs, goals, games, points — and state the implied interval. A row whose winning region is disjoint from that interval contradicts Rank #1 rather than complementing it: repair the tree, change the order, or drop an evidence grade and record the conflict. Re-solve each aggregate component budget conditional on the Rank-1 state, not only marginally. An underdog cushion that requires the underdog to score cannot be paired with an Under that assumes it does not, and a cushion supported by close, extended or tiebreak states cannot be paired with a total that requires the short version of the same match.




Locate every supplied line against the lower, central and upper corridor and every ordinary scenario branch. If the line lies inside the stated central corridor, or supported ordinary branches without predeclared weights fall materially on both sides, no directional row may exceed `LOW` evidence unless an explicit auditable scenario mixture or validated distribution demonstrates separation. A representative point estimate on one side of the line does not repair a corridor that straddles it.




For any aggregate total, solve the threshold as a component budget before ranking. Holding each team, phase or scoring component at its floor, centre and ordinary high state, calculate what the remaining component may contribute without crossing the line. A weak opponent offence, slow phase or low component prior does not imply an Under when the other component's ordinary range can consume the available budget. Record the arithmetic or an equivalent joint-score grid.




Run a bidirectional-sign audit whenever one mechanism can help and hurt the same contract. Turnovers may suppress one team's offence while creating transition possessions for the other; aggression can raise both scoring and dismissal risk; weather can reduce exposure while changing efficiency. Represent both causal paths and their shared state before ranking. If their relative mixture is unresolved, widen the corridor and lower evidence rather than counting only the favourable sign.




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




De-duplicate evidence as well as contracts. One underlying event, match report, upstream feed or participant state counts once even when it reappears in recent form, venue history, H2H, a prior prediction log and several front-end summaries. Preserve the useful views, but identify the shared evidence unit and do not treat repetition as independent confirmation.




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




Settlement outcomes are `WIN`, `HALF_WIN`, `PUSH`, `HALF_LOSS`, `LOSS`, `VOID`, `UNRESOLVED`, or `UNSETTLEABLE`. Quarter-line parents retain the two child settlements. Preserve operator terms where known. Otherwise separate research outcome from unknown operator treatment. One documented official-stat retry is required before a niche-stat row becomes final UNSETTLEABLE. When credible providers disagree, preserve every value, owner, definition and retrieval time. If every credible value maps to the same side of the frozen line, the contract result may be marked invariant while the raw field remains conflicted; if any value changes the result, keep it unresolved. Never import an alleged conflict that cannot be independently reproduced.




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




Audit every #1 loss. As a standing operator instruction, also audit **every Rank-2 loss** and **every event where the total (over/under) rows were both ranked on the wrong side of the realised result** — not because losing a supported row is a defect, but because the top-two ordering and the total-corridor construction are the operator's designated improvement priorities and each loss there is a chance to check whether the component budget, the corridor width and the §8.6-equivalent Under-over-Over burden were honestly discharged. A single outcome does not prove calibration or require a confidence strike, and a `COMPLIANT` forecast that lost to a supported ordinary branch is not a defect. Apply an immediate process lock only when a preissue identity/contract, source-transformation, arithmetic, temporal-leakage, settlement, or compliance defect is demonstrated. Clear the lock only after the error and affected method are corrected. For every audited event also record **what went right and the mechanism behind it**, so a working read is reinforced rather than only failures examined.




An identifiable issued pick with a PROCESS_DEFECT stays in the headline historical ranking denominator, win or loss. Report the defect and a separate compliance slice. Exclude only a genuinely unscorable or already-decided contract from the applicable predictive metric, with a recorded reason. A winning contract does not validate defective reasoning. Candidate/model validation uses its predeclared data and eligibility rules; no retrospective removal of losing process failures is permitted.




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




## 11. GFA-2 — general forecast algorithm




Status: **ACTIVE — executable composition of validity and PROMOTED_PROCESS controls.**
Algorithm ID: `GFA-2`. Effective **2026-09-06** under method `MDS-2026.09.06-v3.9`. The v3.9 patch (2026-09-06, same day, following a second independent review — §15) withdraws the hard ordinal bars this session had itself just added in `G20.2`, `G21.1` and `G26.1`, reclassifying all three as disclosure-only pending their own prospective tests, per the `L-087` firewall applied to the framework's own new work rather than only to externally-cited lessons; corrects a union/intersection category error in `G21.1` and an overclaimed-joint-observation error in `G20.2`; adds nuance to `G25.1`'s `DISJOINT` ban and softens `G30.1`'s cushion-to-winner overclaim; splits `G36.1` into separate `RESEARCH_GRADE`/`OPERATOR_ACTION` fields; and adds source-independence and access-failure nuance to `G10.1`. The v3.8 patch (2026-09-06, same day, following receipt of an external blindspot audit — §14) adds the `rank_gap` ordering-strength field to `G23`, the two-pass result-blind retrospective discipline (`G37.1`), and the price-blind/market-analysis-blind terminology clarification to §4; it splits `L-075`–`L-077`'s magnitude components into the `C-WEIGHT-PROPAGATION` candidate. The v3.7 patch (2026-09-06) adds settlement-source pre-registration (`G10.1`/`G10.2`), the coaching/bench/rotation-capacity record (`G14.2`, §11.3F), the aggregate tail budget (`G20.2`), total-row path geometry (`G21.1`), the top-slot separation floor (`G26.1`), archival completeness (`G34.1`) and standard-rules settlement (`G36.1`); it adds the synthetic-content exclusion to §4 and the bench/coaching extension to §3. It renames no earlier gate and adds no fitted weight. Earlier history: originally effective **2026-09-04** under `MDS-2026.09.04-v3.4`. The v3.1 patch added deficit attribution (G14.1/§11.3D), the separation budget (G20.1), Rank-1 conditional coherence (G25.1) and winner/cushion reconciliation (G30.1). The v3.2 patch added the streak persistence-versus-reversion audit (G17.1/§11.3E), an extension-endpoint own-rate-environment requirement inside G22, and the mandatory series-state block in §5. The v3.3 patch (same day) strengthened `G0` to require a genuinely fresh, in-session method-version read rather than one carried over from memory or a cached copy. The v3.4 patch (same day) adds the most-recent-meeting reconciliation requirement to the regime-dominance audit (§5) and the native-language sourcing requirement to the acquisition order (§4). It renames no earlier gate and adds no fitted weight.




GFA-2 changes no fitted coefficient, probability, calibration or empirically estimated forecast weight. It corrects logical geometry, provenance, bookmaker independence, missingness and environmental admission; retrospective frequencies remain descriptive. It converts the controls in §§0–10, MODEL_AND_DATA_SPEC.md §3 and the PROMOTED controls in LEARNING_REGISTER.md into one ordered procedure with deterministic gates. Every sport file carries a sport instantiation (`SFA-<SPORT>`) that supplies the sport-native exposure chain, mandatory branch set and kill-path library. GFA-2 controls the order and gates; the sport file controls the content.




Run the phases in order. Do not start a later phase while an earlier gate is unresolved, except that Phase B may loop back into Phase A when research reveals an identity or contract defect.




### 11.1 Phase A — admission




| Step | Action | Gate and failure output |
|---|---|---|
| **G0** | Read the mandatory files in §1 **in this session**, and record the method version plus applicable lesson/test IDs found in that fresh read — never a version number carried over from memory, a prior session, or a cached copy of these documents. | `GATE-READ`. Not satisfied means no stats source may be opened. A card whose declared method version is older than the version actually present in the documents at the time of the card's own append timestamp is a `GATE-READ` failure, discovered in the 2026-09-04 audit of P-268/P-270/P-271 (all declared the retired `GFA-1`/`v2.9` a full method version behind what this repository already contained when they were frozen). This is a live risk whenever a generating session (including an external chatbot without repository access) is not handed the current documents at the start of its own work. |
| **G1** | Reconcile the canonical ledger: last canonical ID, event identity, alias map, duplicate-storage check, queue snapshot. | `GATE-LEDGER`. A reused ID gets an alias, never a rewrite. |
| **G2** | Freeze official event identity, competition, rules era, participants, venue, home/away/neutral and official event ID. Store the exact official rule document/version, effective dates, competition adoption/local variation and one state: `PROPOSED`, `REJECTED`, `TRIAL`, `ADOPTED`, or `SUPERSEDED`. Run the **competition rules currency and new-competition onboarding checks** (§3): a season/pre-season/new-edition boundary triggers a rules-currency re-verification against the field owner and an update of the relevant `RULES_<SPORT>.md` reference section before issue; a competition being forecast for the first time must be fully documented there first. | `GATE-IDENTITY`. Malformed identity, unresolved outcome-changing rule adoption, a stale carried-forward rule set at a season boundary, or an undocumented new competition all mean no actionable forecast; never silently repair. |
| **G3** | Freeze the underlying target: `target_id`/version, exact outcome, unit, support, start state, endpoint, scheduled and uncertain exposure, termination/censoring/void terms. | `GATE-TARGET`. One target may not be relabelled as another. |
| **G4** | Freeze the complete supplied candidate slate, each exact contract, settlement interval, push mass, overlap/gap/nesting and operator terms or labelled assumptions. Mark completed rows `SETTLED_AT_ISSUE`. | `GATE-CONTRACT`. An unfrozen derivative provider yields `UNKNOWN_DEFINITION`. |
| **G4.1** | Classify the frozen slate's geometry: exact half-line complements, integer-boundary pairs, quarter-line split parents/children, overlaps, gaps and free rows. State any outcome-count invariant only after checking identical terms, action and no push/void/split path. | `GATE-SLATE`. Exact half-line complements force one win/one loss only when both have action and no void/abandonment path; integer pairs can both push and quarter lines can split. Geometry is disclosure, never evidence of forecast accuracy. |
| **G5** | Freeze times: request, state-check, information cutoff, scheduled start, issue. Convert through named IANA zones and print one GAME-STATE. | `GATE-TIME`. `PREGAME` requires `cutoff_at < scheduled_start_at`; otherwise a verified live target, `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, or a verified final. |
| **G6** | Open the participant identity/release-clock ledger: tuple, expected release time, checked time, source version, release state and next check for every decision-driving role. | `GATE-PARTICIPANT`. `SECONDARY_ONLY`, `NOT_YET_DUE`, `OVERDUE_NOT_RELEASED` or `CONFLICTING` triggers the ceiling table in §11.5. |




### 11.2 Phase B — evidence acquisition




| Step | Action | Gate and failure output |
|---|---|---|
| **G7** | Acquire volatile facts first: state, contracts, rules, participants/toss/lineups, availability, live data. Then process history, then context. | `GATE-ORDER`. History acquired before volatile facts is a process defect even if the values agree. |
| **G8** | Route every decisive field to its claim owner under §4, validate source state and independence, and store the atomic record: exact URL/record, owner, definition/version, value/unit, effective/first-known/observed/accessed times, transformation, missingness, full conflict set/impact, commercial affiliation, market-derived flag and permitted role. | `GATE-PROVENANCE`. A provider-family name, site list or search phrase is not a source record. Bookmaker/affiliate/tipster or market-derived predictive evidence fails closed. |
| **G9** | Collapse evidence to unique underlying units. One match, feed, participant state or upstream provider counts once across recent form, venue, H2H, prior logs and front ends. | `GATE-LINEAGE`. Repetition is not confirmation. |
| **G10** | Retrieve up to five comparable D0 cases under a predeclared query; zero is valid and logged `NO COMPARABLE CASE`. Use them to expose missing branches only. | `GATE-D0`. No analogue win rates, outcome votes or fitted probabilities. |
| **G10.1** | Acquire every decisive field from a **structured keyless endpoint first** where one exists for this competition, before reading any narrative match report, preview or aggregator page. A structured field is far less exposed to summarisation error than a narrative field, but is **not infallible or independent by default** (corrected 2026-09-06(d)): a valid JSON/API field can still belong to the wrong event, hold a provisional/placeholder value, use an unexpected phase definition, or map participants in an unexpected order, and a zero value can mean a genuine zero, an unpopulated shell, or unsupported coverage rather than an observed result — verify field semantics against the actual event, not only the schema. Two endpoints from the same upstream data vendor (for example an API's own scoreboard and summary calls) share that vendor's lineage and are **not** automatically two independent confirmations; count distinct upstream publishers, not distinct URLs. An access failure (HTTP 403/400, empty search) in one automated route establishes that *route's* failure, not competition-wide non-coverage — before recording a competition as unsourceable, also check for an alternate official lane (e.g. a league's own data partner). | `GATE-STRUCTURED`. Where a structured endpoint exists and was not queried, any conflicting narrative value is provisional only. Pre-register the expected provider, event ID and required settling fields before the event goes final; do not require a future final-only field to already exist pregame. See `DATA_SOURCE_REGISTER.md` §September 6 for the verified endpoint list and the verified non-coverage list, both of which are session-specific findings, not permanent claims. |
| **G10.2** | **Settlement-source pre-registration.** For every row in the supplied slate, before it enters the ranked slate, name the exact source and endpoint that will settle it and confirm **in this session** that the endpoint returns that field **for this competition**. Record the endpoint alongside the contract. | `GATE-SETTLEMENT-SOURCE`. A row with no nameable settling endpoint is marked `SETTLEMENT_UNSOURCED`, capped below Rank #1, and given `LOW` evidence. This is a competition-coverage test, not a market-type ban: the same market may be fully sourceable in one competition and unsourceable in another, and that is the variable that actually determines whether the row can be graded. Evidenced 2026-09-06: corners settled cleanly and reproducibly for `P-302` (EPL), `P-273` (Coppa Italia) and `P-151` (Argentina Primera) from one keyless structured endpoint, while the same market remains unsourceable for Liga MX Femenil, MLS NEXT Pro, the French third tier and the China FA Cup because no structured provider carries those competitions. |
| **G11** | Stop when every decision-driving field is verified, explicitly missing, stale or conflicting; the sport-native exposure chain supports an honest rank; the strongest ordinary contrary path is represented; and more searching is unlikely to change an order before the refresh deadline. | `GATE-STOP`. Website count is not evidence strength, and research must not consume the final refresh. |




### 11.3 Phase C — construction




| Step | Action | Requirement |
|---|---|---|
| **G12** | State the competition/venue/rules-era baseline **before** any line is discussed. | The baseline is written first, in its own sentence, with population and sample. |
| **G12.1** | Record a descriptive `REFERENCE_BASE_RATE` for every supplied contract per §11.3A. | Mandatory attempt. `UNKNOWN` remains unknown; it is never imputed or converted into a forecast/rank weight. |
| **G13** | Build the baseline branch and the current-regime branch separately. Name the regime trigger, sample, reliability and mechanism, then state the reason for the qualitative mixture weight. | Sparse, new-role, early-season or roster-change uncertainty widens the distribution before it moves the centre. A centre moves only on an identified directional exposure/rate mechanism. |
| **G13.1** | Run the recency, head-to-head and trend block per §11.3B: L5/L10/L15/L20 for both sides and for head-to-head, the continuity gate, and descriptive recency review. | Mandatory retrieval. Nested windows are one evidence unit, never four confirmations. |
| **G14** | Convert every participant into sport-native exposure by phase and score state, with replacement quality and entry timing. | Available is not exposed. Role eligibility precedes quality. |
| **G14.1** | Attribute every participant-quality deficit, absence, injury-return, rehabilitation or small-sample uncertainty to the distribution that participant actually governs, per §11.3D. | `GATE-ATTRIBUTION`. A named weakness may not widen both sides symmetrically, and it reaches the aggregate total only through the opponent's own exposure and rate. |
| **G14.2** | **Coaching, bench and rotation-capacity record**, per §11.3F. For each side record the named head coach with an interim/caretaker flag and any change inside the last five fixtures; the full named bench/substitutes list with the competition's substitution allowance; a bench-depth count; and any confirmed rotation, rest or congestion signal. | `GATE-BENCH`. A missing entry takes a missingness code and may not be omitted. Where the bench record is `NOT_RETRIEVED`, no margin or full-game total row may be ranked #1, because in that case the single largest late-phase scoring input is unmodelled. Where official structured feeds are `LINEUPS_NOT_YET_PUBLISHED`, a lineup verified via `PROJECTED_BEAT_VERIFIED` under Control `S-1 Rev 2` satisfies pre-game personnel modeling and does not bar Rank #1. |
| **G15** | Apply matchup interactions on current participants and roles, then context (rest, travel, venue, weather, surface, incentive) only through a named exposure, rate, tactical or variance pathway. | A context factor with no stated pathway is recorded and given no directional weight. |
| **G15.1** | Run the separate weather and current-surface/field/pitch gates per §11.3C. Classify venue/roof, retrieve venue-coordinate match-window forecast **and** near-start observation/radar, and retrieve current condition evidence independently from static surface metadata. | `GATE-ENVIRONMENT`. No qualified match-window forecast for an outdoor/open-roof event means `WEATHER_NOT_AVAILABLE — NO ACTIONABLE FORECAST`. Missing current condition is `SURFACE_CONDITION_NOT_OBSERVED`, never inferred from weather, and applies the sport-specific ceiling or no-action rule. |
| **G16** | Form one joint event object for the frozen target: central corridor plus explicit lower and upper tails, or a validated distribution when one exists. Carry the complete phase-end state into the next phase. | All contracts are queries against this object. A phase result is neither a ceiling nor a continuation rule. |
| **G17** | Run the trend-mechanism audit on every streak used directionally: at least three causes in the exposure chain, which of them persist or reverse today, and the ordinary contrary path. | A streak failing this audit carries no directional weight. |
| **G17.1** | Run the streak persistence-versus-reversion audit per §11.3E on every streak, series-prior, or "bounce back" used directionally, including a losing/under run and a winning/over run alike. | `GATE-STREAK`. A continuation or a reversion lean lacking its own named, currently active mechanism carries no directional weight; the longer-run baseline controls instead. |




### 11.3A Descriptive reference-rate record — step G12.1




Reference rates provide context and expose threshold/population mistakes. They are **not** rank anchors or forecast weights. The previously promoted band-move scheme was derived from outcome-selected late-import cohorts and is superseded by v3.0; it may be tested later only under a prospective manifest.




Before any row is ranked, record a reference base rate for every supplied contract:




| Field | Requirement |
|---|---|
| Value | The unconditional frequency of that exact contract settling WIN at the exact threshold in the narrowest defensible population; otherwise a query from a versioned coherent CDF/distribution |
| Population | Competition, season/rules era, venue class and innings/home-away split where relevant, with the denominator stated |
| Descriptive band | Optional display only: `HIGH` at 60% or more, `MODERATE` 45–60%, `LOW` below 45%, or `UNKNOWN`; never used mechanically to order rows |
| Source | The exact record used, under §4; a base rate reconstructed from the card's own reasoning is not a base rate |
| Label | `REFERENCE_BASE_RATE` — descriptive population frequency, **never** a calibrated forecast probability for this event, and never publishable as one |




A reference rate is not a forecast. It cannot be substituted from the nearest historical line because threshold geometry may differ materially. Two contracts on the same event may have different descriptive frequencies, but only current sport-native evidence and a validated target distribution may turn that context into an event forecast. Record `UNKNOWN` honestly; it stays `UNKNOWN` and may lower evidence quality where material.




### 11.3B Recency, head-to-head and trend block — step G13.1




Effective 2026-09-01 by user directive. This reinstates mandatory recent-form and head-to-head retrieval, which an earlier method version had superseded. The supersession existed because cards were reproducing four nested prose tables and treating one underlying match as several independent confirmations. Both problems are solved by structure and de-duplication below, not by skipping retrieval.




**Retrieval is mandatory.** For both teams or players, and for the head-to-head series, retrieve the last **5, 10, 15 and 20** completed events. Where fewer exist, record the true count and the missingness code; never pad a window, and never silently substitute one window for another.




**Store once, as one table.** Four windows in four columns, not four tables:




| Metric | L5 | L10 | L15 | L20 |
|---|---|---|---|---|
| Sport-native exposure metric from `SFA-<SPORT>` | | | | |
| Sport-native rate/quality metric | | | | |
| Target-relevant output metric at the supplied line | | | | |
| Opponent strength faced (adjusted) | | | | |
| Venue split (home/away/neutral as relevant) | | | | |




Repeat once for each side, and once for head-to-head. The head-to-head table carries one extra mandatory row:




| Continuity | How many of those meetings shared the current coach, spine/rotation, starter/goalie/XI, venue, surface and rules era |
|---|---|




**Head-to-head continuity gate.** Head-to-head evidence may influence a rank only for the subset of meetings that pass continuity. If the continuity count is zero, head-to-head is recorded and given no directional weight. This is the direct control for the repeated surface, roster and regime failures logged at P-116, P-118, P-171 and P-200.




**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.




A directional recency effect must state its estimation method, continuity/opponent adjustment and uncertainty; a G17 causal account is not itself a significance test. Do not label an untested absence of trend as proof of noise.




Run the same block for any player whose exposure is decision-driving, over that player's own last 5/10/15/20 relevant appearances, in the phase or role the contract actually reaches.




**De-duplication is mandatory.** One match appears in L5, L10, L15, L20, possibly in head-to-head, possibly in a venue split and possibly in a prior prediction log. Under G9 it is one evidence unit. Shrink from the count of unique underlying events, not from the sum of window rows. Nested windows are never independent confirmations.




**Ceiling.** Raw win/loss, Over/Under and cover counts inside these windows remain `E — diagnostic only` under §5 and may never control an ordinal by themselves. Nested-window comparisons are descriptive diagnostics, not a validated change-point detector. Directional recency weights, exponential decay, state-space estimates and change-point rules remain candidate-only until prospectively tested; current sport-native exposure/rate evidence must justify any event-specific direction.




**Output discipline.** The user-facing card carries the compact tables and the trend verdicts. It does not reproduce twenty match reports.




### 11.3C Environment and conditions gate — step G15.1




Most events in this log are played outdoors. The environment packet is therefore an admission requirement, not an optional modifier added after a total looks interesting.




**Classify the venue first:** `OUTDOOR`, `INDOOR`, or `RETRACTABLE`; record official roof state, exact venue coordinates, static surface type and altitude. Indoor events skip the outdoor forecast gate only when the roof state is verified closed; they still require current court/ice/field/surface status where forecast-relevant.




For every `OUTDOOR` or open `RETRACTABLE` event, retrieve an hourly forecast at the **venue coordinates**, expressed in **venue-local time**, covering one hour before start through the latest plausible contract endpoint, including credible delay, extra-time/overtime, extra-innings or extended-innings branches. Also retrieve the nearest qualified near-start observation and radar/nowcast where available. A city daily value does not satisfy this step.




For each forecast/observation store issuer, product/model, run/issue time, valid time, latitude/longitude, selected grid point or station, distance and material elevation difference, units/timezone, retrieval time, and forecast-versus-observation status. Preserve material conflicts; do not average or majority-vote them without a validated rule.




Mandatory weather fields:




| Field | Primary use |
|---|---|
| Temperature | Ball carry, player conditioning, fatigue |
| Precipitation probability and amount, by hour | Handling, surface, and the termination/shortening branch |
| Wind speed and gusts | Kicking, carry, high-ball contests, swing |
| **Wind direction** | Mapped to ground or stadium orientation and to scoring ends |
| Relative humidity and dew point | Cricket dew and second-innings grip; swing; heat stress |
| Cloud cover | Cricket swing and light; interruption risk |
| Visibility/light where material | Cricket, baseball and tennis interruption/visibility branches |




**Wind must be resolved to a vector, not a speed.** A wind figure without a direction mapped to the ground's orientation is incomplete for AFL, cricket, and any kicking contract, and is recorded as such.




**Current field/pitch/surface report is separate.** Record current/day-of state from the venue, competition, curator/groundskeeper or a clearly qualified observation: moisture/wetness, covers/drainage/maintenance, hardness/grass/strip or court/ice/field condition, and retrieval time as applicable. A precipitation forecast and static surface label do not establish current condition. When no owner report exists, record `SURFACE_CONDITION_NOT_PUBLISHED`; when no qualified observation is recovered, record `SURFACE_CONDITION_NOT_OBSERVED`, sources attempted and the sport-specific consequence. Never invent a pitch/field report.




**Failure output.** If no qualified venue-coordinate match-window forecast is obtained for an outdoor/open-roof event, record `WEATHER_NOT_AVAILABLE` and fail `GATE-ENVIRONMENT`: **no actionable forecast or rank is issued**. A partially complete packet is `ENVIRONMENT_PARTIAL`; omit unsupported directional effects, widen relevant branches and apply the strictest sport-specific ceiling. Conditions are never assumed neutral. Missing current surface evidence remains separate and can itself force no action where the sport file marks the condition forecast-critical.




**No automatic sign.** Rain, heat, cold, wind and humidity have no universal total direction. Each is traced through the sport's own exposure and rate chain under the sport file, and any mechanism that can act in both directions goes through the G22 bidirectional-sign audit together with the termination branch.




### 11.3D Attribution of participant-quality deficits — step G14.1




A deficit attaches to a distribution, not to a scoreboard. When a named participant is weak, absent, returning from injury, on a rehabilitation assignment, in a new role or supported only by a small sample, state which distribution that participant governs and move only that one.




1. A weak or uncertain starting pitcher, goalkeeper, primary ball-handler, front-line bowler, quarterback or first-choice kicker raises the **opponent's** scoring branch and widens that team's conceded distribution.
2. The aggregate total moves only if the opponent's own exposure and rate can convert the deficit into output. A poor season line on one side is not evidence that the other side will also score more.
3. Symmetric widening of both teams from one participant's weakness is a defect. If genuine uncertainty exists on both sides, name the separate mechanism for each.
4. A stale full-season or pre-injury rate may not outweigh the opposing participant's current-regime run-prevention, goal-prevention or possession-suppression evidence when the two are being compared for the same phase.
5. Record the attribution explicitly: which side's distribution moved, through which exposure step, by how much in qualitative terms, and what the other side's distribution did.




### 11.3E Streak persistence-versus-reversion audit — step G17.1




Effective 2026-09-04 by user directive, extending L-011/G17. A streak of any length is evidence about the past, not a forecast. Two opposite errors are equally prohibited: extending a streak with no identified cause (the continuation fallacy G17 already blocks), and calling a "comeback," "bounce back," "regression," or "due for a change" with no identified cause (the reversion fallacy this gate blocks). Neither may be assumed as a default; both require the same standard of evidence.




**Applies to** any run of like results or like values used directionally: an Over/Under run, a win/loss run, a cover/no-cover run, a single prior leg of a series or two-leg tie treated as informative about the next leg, and a single recent result described as a "response" to an earlier one.




**Step 1 — state both rates.** Record the streak's own rate/length (the short window, e.g. L3–L5) and the longer-run baseline rate for the identical metric and population (season, multi-season, or the longest defensible window under §11.3B). Two different numbers with two different sample sizes must both be visible before either is used.




**Step 2 — plausibility check against the baseline.** Compare the streak's length/magnitude against the ordinary variance implied by the longer-run baseline rate at this sample size (for example, a binomial run of this length is not statistically remarkable if it falls within the spread ordinarily produced by repeated sampling at the baseline rate). A streak that is not remarkable against its own baseline carries no informational content in **either** direction: use the longer-run baseline as the centre and widen the tails, rather than moving the centre toward the streak or mechanically expecting a snap back toward it.




**Step 3 — name a mechanism for whichever direction is used.** A streak may influence the rank only when a currently active, named cause is identified in the sport's exposure chain (per G17). A reversion/comeback lean may influence the rank only under the identical standard: a named, currently active or newly resolved cause — such as a returning or now-healthy participant, a genuine tactical or personnel change, a schedule/opponent-quality shift, resolved fatigue/rest, or a demonstrated current-regime break under the regime-dominance audit (G13). "The streak has gone on long enough" and "a bounce back is due" are not mechanisms.




**Step 4 — populate both branches.** Exactly as the bidirectional-sign audit (G22) requires both causal signs of a mechanism to be represented, represent both the streak-persists branch and the streak-breaks branch in the scenario tree before ranking, with the state each requires. Do not silently default to only the branch that supports the row already favoured on other evidence.




**Failure output.** A streak or series-prior that fails Steps 1–3 in either direction is recorded and carries zero directional weight; rank from the longer-run baseline and the sport-native exposure/rate mechanism instead, per the evidence-ceiling table (§11.5).




### 11.3F Coaching, bench and rotation-capacity record — step G14.2




Implements `G14.2` and the §3 bench/coaching extension. Runs inside Phase C, before the geometry phase, because bench capacity is an input to the score distribution rather than a commentary note.




**Required record, per side:**




| Field | Content | Missingness code if absent |
|---|---|---|
| `coach` | Named head coach/manager | `COACH_NOT_RETRIEVED` |
| `coach_tenure_flag` | `ESTABLISHED`, `INTERIM`, `CARETAKER`, or `CHANGED_WITHIN_5` | `COACH_TENURE_UNKNOWN` |
| `bench_named` | Full named substitutes list as officially released | `BENCH_NOT_RELEASED` / `BENCH_NOT_RETRIEVED` |
| `sub_allowance` | The competition's substitution allowance from the `RULES_<SPORT>.md` reference section, including concussion/extra-time provisions | `SUB_RULE_UNKNOWN` |
| `bench_depth` | Integer: how many named bench players started ≥40% of the side's last ten fixtures | `BENCH_DEPTH_UNKNOWN` |
| `rotation_signal` | Fixture inside four days, competition priority statement, dead rubber, stated rotation plan, or `NONE_FOUND` | — |




**How it enters the forecast.** Bench capacity is a *phase-conditional exposure* term, not a general strength adjustment. It enters through the sport's own late-phase exposure step in `SFA-<SPORT>`: minutes/overs/innings available to a replacement, and the rate that replacement carries. It may not be applied as a flat markdown to a team's whole distribution — that is the same error `L-077` corrects for personnel losses, and the same discipline applies here.




**Hard consequences.**




- `BENCH_NOT_RETRIEVED` on either side ⇒ **no margin row and no full-game total row may be Rank #1** on that card. Phase rows confined to an interval before the substitution window are unaffected.
- **`PROJECTED_BEAT_VERIFIED` under Control `S-1 Rev 2`:** When official league structured APIs have not yet populated (`LINEUPS_NOT_YET_PUBLISHED`), pre-game line combinations and rotations verified across accredited beat reporters or official team media releases satisfy `G14.2` personnel modeling and **do not block a margin or full-game total row from Rank #1**, provided the projected state is explicitly disclosed on the card.
- `CHANGED_WITHIN_5` or `INTERIM` on either side ⇒ any evidence window that spans the change is split at the change and the pre-change segment is `E — diagnostic only`, exactly as a rules-era change is handled at `G2`.
- A bench-driven scoring branch that the card names must be reconciled against the issued order under `G25`, like any other named branch.




**Origin evidence.** `P-304`, 2026-09-05: Slavia scored two of four goals through substitutes (Ayaosi 76', on as a forced 26th-minute injury replacement; Jurásek 88', on 63'), having lost two starters to injury inside 26 minutes, and still won 4-0 against a promoted side. The favourable direction of that outcome is a third instance of `L-077`'s opponent-conditioned personnel discount; the *unmodelled* driver was the bench.




### 11.4 Phase D — geometry




| Step | Action | Requirement |
|---|---|---|
| **G18** | Decompose two-sided score events into three linked questions: total event volume, allocation between competitors, winner/margin. | Answering one never answers another. |
| **G19** | Enumerate the sport's mandatory branch set from `SFA-<SPORT>` and stress the four ordinary score families: low/close, low/separation, high/close, high/separation. | Never infer a cushion from an Under or a blowout from an Over. |
| **G20** | Solve every aggregate line as a component budget. Hold each team, phase or component at floor, centre and ordinary high, and calculate what the remainder may contribute without crossing. Record the arithmetic or joint grid. | A weak component does not create an Under when the other component's ordinary range can consume the budget. |
| **G20.1** | Solve every margin, handicap and cushion line as a separation budget. Split scheduled exposure into the sport's scoring-allocation phases from `SFA-<SPORT>` and hold each side at floor, centre and ordinary high in each phase. | Name the phases that generate separation and show the margin state each produces. A close head-to-head record, a low total or a favourite lean is not a separation budget. |
| **G21** | Locate every supplied line against the lower, central and upper corridor and against each ordinary branch. | This populates the corridor field of the ordering record. |
| **G20.2** | **Distributional tail audit — current rule (CR-2026.09.21-3).** For every total/phase-total, obtain lower-tail, boundary/push and upper-tail mass from the same frozen sport-native joint distribution/branch mixture used to rank the row. If no validated numerical distribution exists, state qualitative tail branches and uncertainty without inventing pseudo-probabilities. | `GATE-TAIL`. Historical second-highest+median / second-lowest+median order-statistic sums are **superseded** and are not computed as an active gate, probability proxy or rank input. |
| **G21.1** | **Exact target geometry — current rule (CR-2026.09.21-3).** Map each supplied target to its exact settlement event and derive WIN/PUSH/LOSS plus void/censoring/extension branches from the same frozen PMF/CDF or coherent joint branch mixture. Genuine mathematical unions may be described as unions, but historical path-count categories have no mandatory ordinal role. | `GATE-GEOMETRY`. The distribution, not the label or path count, determines marginal likelihood. |
| **G22** | Run the bidirectional-sign audit on every mechanism that can help and hurt the same contract, and model termination and extension endpoints as their own branches. | Shortening risk is not an automatic Under; an extension endpoint is part of the target, not a display note. An extension endpoint (overtime, extra innings, a shootout/super over, penalties) may run under its own rule-defined scoring-rate environment that differs materially from regulation play — for example an automatic-runner or golden-point rule — and must be modelled with that environment's own rate, never the extrapolated regulation rate. |




### 11.5 Evidence-ceiling table




Apply every matching row. The strictest ceiling wins. These are validity controls, not predictions.




| Observed condition | Ceiling imposed |
|---|---|
| Decision-driving participant `SECONDARY_ONLY`, `NOT_YET_DUE`, `OVERDUE_NOT_RELEASED` or `CONFLICTING` | The mechanism may not be attached to that named participant as fact; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` and must be modelled as a role mixture |
| Supplied line sits inside the stated central corridor | No directional row on that line exceeds `LOW` evidence without an explicit auditable scenario mixture or a validated distribution |
| Ordinary unweighted branches fall materially on both sides of the line | Same as above |
| Derivative or niche target missing any layer of its target-event exposure/rate/opponent/context chain, or its provider definition is unfrozen | `FORCED RANK`, `LOW`/`MEDIUM-LOW`; never `LEAN`/`SUPPORTED`; settlement labelled `UNKNOWN_DEFINITION` where the operator is unspecified |
| A named ordinary kill path cannot be explained as subordinate | Drop one evidence grade and re-run the §11.6 ordering before issue |
| A streak fails the G17 trend-mechanism audit | Zero directional weight; diagnostic only |
| A streak-break, "comeback," "bounce back," or series-response lean fails the G17.1 persistence-versus-reversion audit (no named, currently active mechanism; streak not remarkable against its own longer-run baseline) | Zero directional weight; rank from the longer-run baseline instead |
| Statistic conditioned on the forecast outcome, such as a win-conditioned cover count | Descriptive only; record the conditioning event and denominator; may not be counted alongside the win record |
| Official live state unavailable and two independent current sources do not agree on orientation, score, phase and clock | `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST` |
| Official page is a stale shell, zero-filled placeholder, unfinished snapshot, old head-to-head module or malformed slug | That field is quarantined; seek a correction or static report, then use two independent current high-quality sources provisionally |
| First local copy after final | Preserve import timing; existing non-live cards are USER_CONFIRMED_PREGAME_FREEZE and admitted to historical ranking evaluation. New unconfirmed imports require provenance classification. No automatic post-outcome challenger validation |
| No validated model ran | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; no probability, value, ROI or edge language |
| Outdoor or open-roof event with no qualified venue-coordinate match-window forecast | `WEATHER_NOT_AVAILABLE — GATE-ENVIRONMENT FAIL`; no actionable forecast or rank |
| Required current surface/field/pitch state not published or not observed | Preserve `SURFACE_CONDITION_NOT_PUBLISHED`/`SURFACE_CONDITION_NOT_OBSERVED`; do not infer from static metadata or weather; apply the sport-specific ceiling/no-action rule |
| Wind used directionally without a direction mapped to ground/stadium orientation | The wind claim carries no directional weight; record it as speed only |
| Head-to-head continuity count is zero | Head-to-head is recorded and carries no directional weight |
| `TREND_CANDIDATE` that fails the G17 causal test | Recorded; no directional weight |
| Contract requires an extra condition unsupported by the current mechanism | That mechanism cannot support the row; lower evidence and compare its marginal likelihood directly rather than applying a contract-family penalty |
| Margin, handicap or cushion row issued without the G20.1 separation budget | That row caps at `FORCED RANK` / `MEDIUM-LOW`; a close-game narrative may not substitute for the budget |
| A row is `DISJOINT` from the Rank-1 implied interval under G25.1 | Record the dependence/coherence relationship. Repair the tree or ranking **only** if the disjointness reveals an impossible score tree, inconsistent probability assignment or another construction defect. Mutually exclusive but coherent high-probability marginals may still occupy high ranks under direct marginal-likelihood ordering. |
| A participant-quality deficit was used to widen both sides' scoring distributions without a named opponent exposure/rate pathway | The symmetric widening is removed under G14.1; the deficit attaches only to the distribution that participant governs |
| L5/L10/L15/L20 or head-to-head windows not retrieved | `GATE-RECENCY` failure; record the missingness code and cap the affected rows at `LEAN` |




### 11.6 Phase E — ordering




Ranking is by marginal estimated win likelihood and robustness under the exact contract. Comparative likelihood judgment is internal and required; publishing a number requires the validated-model gate.




**G23 — build a row robustness record for every legally rankable supplied row.**




| Field | Values |
|---|---|
| `reference` | The descriptive `REFERENCE_BASE_RATE` or `UNKNOWN`, with exact threshold, population and denominator; diagnostic only |
| `align` | `EXACT` — the researched mechanism predicts every extra condition the contract requires; `PARTIAL` — it predicts the direction but not one required condition; `PROXY` — a different metric, or a dominance/territory narrative, is standing in for the settled event |
| `support` | Exact conditions the contract requires and whether each is supported by the researched mechanism; labels such as spread/team total are not mechanically `CONJUNCT` |
| `states` | Which of the enumerated mandatory branches and four score families settle this row WIN, and which of them require an unweighted assumption |
| `kill` | Breadth of the strongest ordinary state that defeats it: `NARROW_TAIL`, `ORDINARY_BRANCH`, `BROAD_ORDINARY` |
| `corridor` | `OUTSIDE`, `EDGE`, `INSIDE_CENTRAL` |
| `tier` | Data priority of the decisive field: A-volatile, B-process, B-environment, C-adjusted history, D-conditional, E-diagnostic |
| `trend` | Descriptive recency pattern and causal audit result; no nested-window direction or mechanical weight |
| `dep` | Dependence group, `PRIMARY_FORMAL` or `CORRELATED_SECONDARY`, and every complement, overlap, gap and nesting relation |
| `rank_gap` | Pairwise ordering strength against the row immediately below it in the issued order: `NEAR_TIE`, `SMALL`, `MODERATE` or `LARGE`, plus one sentence naming the exact evidence that separates the pair. `NEAR_TIE` still requires a unique ordinal (per `G23.1`'s `NEAR_TIED` handling) — this field records how close that forced choice actually was, so a reviewer can distinguish a genuinely dominant Rank #1 from one that only edged out Rank #2 on an administrative tie-break (added 2026-09-06, `L-088`) |




**G23.1 — direct marginal-likelihood ordering.** Compare every row against the same joint event object and rank it by estimated probability of the exact settlement event plus robustness to evidence uncertainty. The row record is an audit trail, not a points system: reference-rate bands, nested-window trends, `SINGLE`/`CONJUNCT` labels, corridor labels, kill-path adjectives and historical slot records may not mechanically add/subtract a band or force an ordinal. `UNKNOWN` remains unknown. If two rows cannot be separated honestly, assign required unique ordinals, label them `NEAR_TIED`, use `FORCED RANK`/LOW evidence, and state the non-predictive administrative tie-break.




**G24 — extra-condition support audit.** State every condition required for the exact row. A favourite spread needs winner and separation support; an underdog cushion needs the states in which it remains inside the line; a team total is one score variable and is not automatically conjunct. Missing support lowers the event-specific likelihood/evidence assessment but does not trigger a retrospective contract-family demotion. The former blanket Rank-#1 block and one-band penalty are superseded; their late-import evidence may support only a prospectively declared challenger.




**G25 — cross-row coherence gate.** Write one representative settled scoreline or event path for Rank #1. Check it against every other leading row. If the top rows require mutually incompatible states and no explicit branch produces both, the order is wrong: repair the tree or lower the affected evidence grades before issue.




**G25.1 — Rank-1 conditional coherence.** Convert the branch set under which Rank #1 wins into the unit of every other supplied line and state the implied interval. Classify every remaining row `COHERENT`, `PARTIAL_OVERLAP` or `DISJOINT` against that interval, and re-solve each aggregate component budget conditional on the Rank-1 state rather than only marginally. This is arithmetic on the frozen branch set, not a fitted weight, and it never displaces direct marginal likelihood between rows that are genuinely compatible.




**`DISJOINT` nuance (added 2026-09-06(d)).** The original text here read "a `DISJOINT` row may not sit in the top half of the order while Rank #1 stands," stated as a blanket ban. That is too strong and is corrected: three mutually exclusive complete outcomes with marginal probabilities 0.45 / 0.40 / 0.15 can legitimately rank two selections covering the first two outcomes as #1 and #2 even though they cannot both win — a single coherent joint distribution can still contain incompatible high-ranked marginal selections, and ranking by marginal probability is not the same objective as maximising the chance both top picks win together. The ban applies specifically where `DISJOINT` reveals an **actual construction defect**: an impossible score tree, a probability assignment that cannot be simultaneously true (e.g. both rows implicitly claim more than 100% of the outcome space once reconciled), or a corridor that was never solved jointly in the first place. It does **not** apply to two rows that are correctly, deliberately ranked by their own marginal probabilities and simply happen to be mutually exclusive — that is an ordinary property of ranking individual selections, not a defect. State explicitly, for every `DISJOINT` finding, which of these two cases it is before deciding whether to repair the tree, change the order, or leave it as a legitimate disjoint pair with the conflict recorded.




**G26 — top-row test.** `SUPPORTED` requires fresh event-specific evidence that clearly outweighs the strongest ordinary kill path. A required #1 may remain `LEAN` or `FORCED RANK`. No #1 may rest on an assumed, secondary-only or stale decisive fact.




**G26.1 — no universal top-slot separation floor (current rule, CR-2026.09.21-3).** Print any relevant descriptive `REFERENCE_BASE_RATE` and adjacent `rank_gap`, but **no 40–60% or other pooled probability band can disqualify Rank #1 or force a wider-separation row upward**. Rank by `G23.1` from the exact marginal likelihood of the row under the frozen joint event object plus robustness to evidence uncertainty. A precise numeric probability requires the validated-model gate.




**The former hard rule — "a row inside a 40–60% split may be Rank #1 only with named event-specific evidence, otherwise a wider-separation row takes the slot" — is withdrawn.** A second independent review correctly identified that this was itself an undisclosed ordinal effect derived from a single session's cohort (originally justified by `P-300` alone), which is exactly the pattern the predictive-weighting firewall (`L-087`) exists to catch — the 40–60% boundary had no derivation, no sample-adequacy requirement, and `UNKNOWN` passed the gate for free, which perversely rewards a thin research base over a properly quantified uncertain one. It is also not established that `P-300`'s Rank #2 winning by 20.5 runs demonstrates a wider *pre-issue* probability separation — a large realised margin is a fact about the outcome, not about the probability that was actually assignable before the event.




**Reclassified as `CANDIDATE C-SEPARATION-FLOOR`, no gate registered on this claim as of 2026-09-06(d).** Ranking continues to be governed by `G23.1`'s direct marginal-likelihood comparison alone; a near-even reference split is recorded honestly (via `rank_gap`) but does not by itself disqualify a row from Rank #1. Any future ordinal rule here requires its own frozen prospective test with a derived (not asserted) threshold and an explicit sample-size requirement, exactly as `G20.2`/`G21.1` above.




**G27 — bottom-row test.** Write the best case for the last row in full, then run the swap test against the row above it. If the last row survives more ordinary states or carries the narrower kill path, the order is wrong. Rank the last row relatively; historical slot-frequency records are retrospective diagnostics and are prohibited as a fade prior.




**G28 — corridor/complement diagnostic.** Exact complements around an inside-central line are boundary-sensitive and normally receive LOW evidence, but their ordinal positions still follow direct marginal likelihood. Do not move them away from extreme slots merely to make the slate look separated. Record the boundary sensitivity and any administrative near-tie explicitly.




**G29 — dependence disclosure.** One thesis expressed several times is one mechanism observation. Only one row per shared thesis is `PRIMARY_FORMAL`. Two correlated derivative rows may occupy both top slots only after direct comparison with every opposing full-target contract and only on independent target-specific evidence.




**G30 — potential winner.** Name one for every valid active event with its exact endpoint, analysed independently of totals and handicaps. If its settlement terms match a supplied row, reuse that contract ID as an alias and count it once. Use `FORCED WINNER — LOW CONFIDENCE` when evidence does not support a lean.




**G30.1 — winner and cushion reconciliation (revised 2026-09-06(d) — softened overclaim).** When Rank #1 is an underdog cushion, name the potential winner from the same joint object's win-branch mass, not from team strength, seeding, reputation or the favourite label. State the branch ordering explicitly: a cushion is the union of the underdog's outright-win branch and its narrow-loss branch. If the favourite is still named, identify the narrow-loss states that carry the difference. Analysing the winner independently of handicaps means deriving it from the branch set, never defaulting to the stronger side.




**Correction:** the prior text claimed that "evidence strong enough to rank the cushion first *necessarily* gives the outright branch weight." That is not generally true and is withdrawn. A counterexample: a favourite that wins narrowly 50% of the time, wins by more than the handicap 30% of the time, and loses outright 20% of the time gives the underdog cushion a strong 70% cover rate *while the favourite still wins outright 80% of the time* — both a well-supported Rank #1 cushion and a well-supported favourite winner call can coexist on the same joint object. The actual requirement is only that the *share* of the cushion's win mass carried by narrow losses versus outright underdog wins be estimated or reasoned through and stated, not presumed to transfer "substantial" weight either way. Also: "the side receiving points" is not a synonym for "the weaker side" — a strongly favoured side can be supplied receiving points on an unusual contract (e.g. `P-303`'s Nigeria +25.5, where Nigeria were the stronger side); treat an unusual sign as an identity/contract check first, never as evidence for an underdog-cushion pattern.




### 11.7 Phase F — freeze and issue




| Step | Action |
|---|---|
| **G31** | Final volatile refresh: state, participant release clock/lineups/toss/goalie/starter, official roof/surface state, current field/pitch/court condition, and match-window weather/observation. Re-run the participant handshake. The sports forecast stays market-blind; any explicitly requested price audit begins only after G33 freezes it. |
| **G32** | If the refresh changes a decisive fact, return to G14. If the scheduled start has passed, re-run G5. If the event is final, stop forecasting and report the result. |
| **G33** | Freeze the information cutoff, any genuine shadow output, the method version and the applicable lesson/test IDs. |
| **G34** | Append the complete view to the active log using the canonical schema **before** delivery, then state in the response that this was done. |
| **G34.1** | **Archival completeness.** A running-log component may not be archived, summarised or superseded while any card inside it is still unsettled, unless that card's **complete frozen ranked slate** — every row, not only Rank #1 — is reproduced verbatim in the archived artifact. Where a slate row was never written to any file, record it as `UNGRADABLE / ARCHIVAL_OMISSION`; never reconstruct it from memory or inference, which would be fabrication. |
| **G35** | Deliver only what has passed its publication gate: the mandatory output list in AGENT_ROLE_AND_TASK.md §6, with unknowns, source limitations and a plain-language bottom line. |




### 11.8 Phase G — settle and learn




| Step | Action |
|---|---|
| **G36** | Settle from the official final, field by field, preserving conflicting provider values and their lineages. Mark a contract invariant only when every credible value falls on the same side of the frozen line. |
| **G36.1** | **Standard-rules settlement; `PROVISIONAL` is not a terminal state (refined 2026-09-06(d) — two separate fields, not one).** A row whose only remaining obstacle is *unsupplied operator terms* is graded under the stated standard rules of the competition **as a `RESEARCH_GRADE`**, with the standard-rules assumption written down beside the grade. Record `OPERATOR_ACTION` **separately** as `UNKNOWN_DEFINITION` where no operator ticket/terms were ever supplied — sporting/competition rules (retirement, reduced-overs/DLS, overtime/shootout, listed-player conditions) do not by themselves determine what an *unidentified operator's contract* pays out on. `RESEARCH_GRADE` may be `WIN`/`LOSS`/`PUSH` under the stated standard-rules convention while `OPERATOR_ACTION` remains genuinely `UNKNOWN` — these are not in tension, and neither field may be silently dropped or merged into the other. `PROVISIONAL` and `UNRESOLVED` are reserved for genuine source conflict or genuinely missing *result* data, not for a missing operator convention, which now has its own field. This follows directly from the governing price-independence rule: a missing price or missing operator wording never justifies leaving a finished event's `RESEARCH_GRADE` ungraded, but it also never licenses inventing a universal betting-settlement convention on the operator's behalf. |
| **G37** | Grade outcome and process separately using the four honest verdicts: result-right/process-right, result-right/process-different, result-wrong/process-broadly-right, result-wrong/process-wrong. **Worked example of "result-right / process-different" (added 2026-09-25; 2026-09-22 audit):** P-482's powerplay Over won through the mechanism the card named (Sadaqat), but its probability was sized on chase powerplays while Jamaica batted first. A win with mis-sized evidence is not graded "process-right", so a lucky sizing is not reinforced. |
| **G37.1** | **Two-pass retrospective discipline (added 2026-09-06, `L-089`).** Reach the process/compliance grade (Pass A) from the frozen card's identity, contract, state, sources, scenario tree, kill-path library and component/separation budgets alone, judged against what was knowable and required at issue time — **before** consulting the final result. Only then reveal the result and perform Pass B: actual driver, its knowability, and whether the branch that occurred was ordinary or exceptional. Record both as separate fields, `ISSUE_TIME_PROCESS_GRADE` and `OUTCOME_DRIVER_GRADE`; a process lock may be applied only from Pass A, never inferred backward from Pass B alone. |
| **G38** | Audit every #1 loss. Apply a process lock only for a demonstrated identity/contract, source-transformation, arithmetic, temporal-leakage, settlement or compliance defect. |
| **G39** | Quarantine any process-defective view from mechanism validation, ranking/model performance, calibration and prospective test completions, while keeping its settlements for ledger integrity. |
| **G40** | Record dispositions in LEARNING_REGISTER.md only under its prospective rules. One event creates a candidate, never a weight. |




### 11.9 Mandatory card checklist




Every issued card carries these lines. A line that cannot be completed is written with its missingness code, not omitted.




1. `GATE-READ / LEDGER / IDENTITY / TARGET / CONTRACT / TIME / PARTICIPANT / SLATE / RECENCY / ENVIRONMENT / BOOKMAKER-INDEPENDENCE`: pass, or the exact failure.
1a. Competition rules currency (§3): the reference section consulted with its review date; for a season / pre-season / new-edition boundary or a >6-week gap, the field-owner rules-currency re-check with its source and date, and any reference-section update made this session; for a first-ever appearance of the competition, confirmation that its full rules were documented before this card.
2. Slate geometry: exact half-line complements, integer boundaries/pushes, quarter-line children, overlaps/gaps/free rows, and only genuinely qualified outcome-count invariants.
3. Descriptive `REFERENCE_BASE_RATE` or `UNKNOWN`, exact threshold, population and denominator for every supplied contract; no imputation or mechanical rank effect.
4. Baseline statement, written before any line.
5. Regime mixture: baseline branch, current-regime branch, trigger, sample, reliability, mixture reason.
6. Recency block: the L5/L10/L15/L20 table for each side, the head-to-head table with its continuity count, the trend verdict per metric, and the unique-event de-duplication. Where a streak, series-prior, or "bounce back" is used directionally in either direction, its G17.1 persistence-versus-reversion result: both rates, the plausibility check against the longer-run baseline, and the named currently active mechanism or the zero-weight disposition.
7. Environment block: venue/coordinates, roof/static surface, current field/pitch/surface condition state, forecast and near-start observation/radar with full provenance, plausible endpoint horizon, wind orientation, and explicit missingness/conflicts.
8. Exposure chain from `SFA-<SPORT>`, by phase and score state.
9. Attribution record for every participant-quality deficit: which side's distribution moved, through which exposure step, and what the other side's distribution did.
10. Mandatory branch set plus the four-family grid, with each supplied line located against it.
11. Component budget arithmetic for every aggregate line.
12. Separation budget arithmetic for every margin, handicap and cushion line, split by the sport's scoring-allocation phases.
13. Bidirectional-sign audit and termination/extension branches.
14. Row robustness records and direct marginal-likelihood comparison; no reference-band, trend, contract-family or slot-frequency mechanical adjustment.
15. Extra-condition support audit for every handicap, cushion and other multi-condition row.
16. Rank #1 representative scoreline and the cross-row coherence result.
17. Rank-1 implied-target interval, the `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT` classification of every other row, and every aggregate budget re-solved conditional on the Rank-1 state.
18. Best case for the last row and the swap-test result.
19. Dependence groups, aliases and evidence-unit lineage.
20. Evidence-ceiling rows applied.
21. Potential winner with its endpoint.
22. Winner-and-cushion reconciliation whenever Rank #1 is an underdog cushion, with the branch ordering stated.
23. `SPORTS_ONLY / MARKET_BLIND` declaration, probability state, any separate post-freeze price-audit state, and appended-before-delivery confirmation.
24. Settlement-source pre-registration (`G10.2`): for every supplied row, the exact endpoint that will settle it and the in-session confirmation that the endpoint returns that field for this competition; `SETTLEMENT_UNSOURCED` where none exists.
25. Coaching, bench and rotation-capacity record (`G14.2` / §11.3F) for both sides, with missingness codes.
26. Distributional tail audit (`G20.2`): lower-tail, boundary/push and upper-tail mass from the same frozen joint distribution, or explicit qualitative branch/missingness disclosure when no validated numerical distribution exists. Do not compute historical order-statistic pseudo-tail sums.
27. Exact target geometry (`G21.1`) and no-separation-floor check (`G26.1`): exact settlement mapping and PMF/CDF/branch mass for each supplied target; reference rates and `rank_gap` are descriptive only; no path-count/category shortcut or 40–60% top-slot rule.




### 11.10 Guard notes




- GFA-2 is a process/validity algorithm. Completing it is not evidence of predictive lift, and its steps may not be cited as calibration.
- No step introduces a fitted coefficient, scenario weight or published probability. Scenario weights remain qualitative until they are estimated from an approved H0.
- Slot-frequency history, raw cover counts, Over/Under streaks and reputation are `E — diagnostic only` at every step and may never control an ordinal by themselves.
- Where a sport file's `SFA-<SPORT>` conflicts with GFA-2 on sport-specific content, the sport file controls within its scope; where it conflicts on order, gates or honesty controls, GFA-2 and §§0–10 control.




## 12. September 5 audit amendments — L-068–L-071




Effective for future work under MDS-2026.09.05-v3.5. These amend execution of GFA-2 across **every SFA**; they do not fit coefficients, assign new branch weights, or establish predictive lift. Evidence and per-sport examples: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).




| Gate / step | Required operation | Failure handling |
|---|---|---|
| G4 / G20 / G25.1 — L-068 | Compute score-tree sums, signed margins and each row's WIN/PUSH/LOSS directly from the sport-native units. Winner, total and handicap are distinct queries. Check every representative branch before it supports a rank | Arithmetic or contract mapping must be repaired before issue; do not rely on a correct-looking narrative |
| Availability / G31 — L-069 | For every named decision-driving participant, reconcile current presence, actual role/entry/exposure and publication time. A nominal starting label may be ceremonial or short-lived. Propagate unresolved gates and their LOW ceiling into the final ranking | Missing evidence stays missing. A final-table LOW-MEDIUM label cannot override an earlier mandatory LOW gate. If a late change's publication time is unknown, its retrospective knowability is INCONCLUSIVE |
| G20 / G20.1 / G22 — L-070 | Make both competitors' ordinary win/separation states contract-evaluable. For early versus full totals, include both early-Under/full-Over and early-Over/full-Under paths where materially possible, passing resources and participant allocation into the next phase | A prose upset/kill-path note is not a substitute for the missing score/resource branch. No arbitrary numerical probability is required or authorised |
| G2 / G5 / G36 — L-071 | Preserve host, source event ID, competition/date and participants together. Check field meaning: scoring shots versus attempts; efficiency versus points; legal balls versus delivery sequence; official final versus static placeholders | A score field failing identity or semantics cannot settle a row. Do not transfer an event ID between club and league hostnames |




For settlement sweeps under the user's September 5 workflow, if the **first check** finds an event live, suspended or otherwise unsettled, record the snapshot and defer its settlement and retrospective to the next query. Do not grade a mathematically crossed row or keep polling it to close it during that sweep. Say “live at first check / deferred,” not “still live” at delivery without a fresh observation. On the next query, check all deferred IDs again; move on from each that remains live.




Maintain separate `event_state`, `research_endpoint_grade`, `operator_action_status`, and `remaining_fields`. A completed result can be research-settled while a provider/stat/action field remains open. Current snapshot/index must expose those cases (P-273/P-274 were previously buried). Do not infer a real ticket or operator contract from a printed research line.




For “at least one O/U should win,” first disclose complement geometry. An exact half-point Over/Under pair yields one winner on a normal completed endpoint regardless of analytical skill. Record preferred total direction, Rank #1, Rank #2, both-top-two and event dependence separately. Coverage is not a reason to distort the requested marginal likelihood order. Since the 2026-09-06 directive below, these diagnostics count in the descriptive performance scorecard as soon as the row is settled — the gate is settlement itself, not a separate performance-eligibility test.




## 13. September 6 audit amendments — L-079–L-086




Effective **2026-09-06**, method `MDS-2026.09.06-v3.7`. Every item below is a validity, provenance or disclosure control. **None fits a coefficient, assigns a scenario weight, publishes a probability, or claims predictive lift.** Origin evidence is the settlement of `P-304`/`P-305` and the closure of the `P-300`, `P-302`, `P-273` and `P-151` evidence gaps; full narrative in [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md).




| ID | Control | Where it lives |
|---|---|---|
| `L-079` | Synthetic/simulated/preview/fantasy content is tier E and may never settle a contract; results come from scoreboard/scorecard records, not narrative articles; a search-result summary is not a source | §4 authority hierarchy |
| `L-080` | Structured keyless endpoints are queried **before** any narrative page for every decisive field where one exists for the competition | `G10.1`; §4 access ladder; `UPCOMING_GAME_RESEARCH_GUIDE.md` §7 |
| `L-081` | Corners and other derivative rows are governed by a **settlement-coverage test**, not a market-type ban. **Narrows and supersedes `L-073`**, whose stated premise ("no corners market in this framework's entire recorded history has settled cleanly from a single independently-reproducible field owner") was falsified on 2026-09-06 | `G10.2` |
| `L-082` | Coaching, bench and rotation-capacity record mandatory on every card; `BENCH_NOT_RETRIEVED` blocks a margin or full-game total row from Rank #1 | `G14.2`, §3, §11.3F |
| `L-083` | A phase total whose retrieved window shows ≥1.5 wickets/possessions lost per phase is modelled as **bimodal**, located against the modes rather than the mean, with the collapse branch written as a named kill path | `RULES_CRICKET.md` §September 6; sport-file analogues |
| `L-084` | Aggregate upper-/lower-tail budget disclosure for every total row, computed from `G13.1` data | `G20.2` — **disclosure mandatory now; ordinal effect is `CANDIDATE C-TAIL-BUDGET`** |
| `L-085` | Total-row path geometry disclosure (`UNION_LOW_THRESHOLD` / `INTERSECTION_CONSTRAINT` / `CENTRAL_BAND`) | `G21.1`, `G26.1` — **disclosure mandatory now; ordinal effect is `CANDIDATE C-PATH-GEOMETRY`** |
| `L-086` | A component may not be archived while any card in it is unsettled unless that card's complete frozen slate is reproduced verbatim | `G34.1`; `EXTERNAL_LOGGING_WORKFLOW.md` |




**Explicit correction of a previously promoted control.** `L-073` (2026-09-05(b)) imposed a blanket cap forbidding any corners contract from being Rank #1 whenever a goal-based total was available in the same slate, on the stated ground that corners had *never* settled cleanly from an independently reproducible field owner across this framework's history. On 2026-09-06 three corners rows — `P-302` (EPL), `P-273` (Coppa Italia) and `P-151` (Argentina Primera) — were settled from a single keyless structured endpoint in one request each, and a fourth (`P-300`'s cricket powerplay, the same class of "unsourceable phase field") was closed the same way. The premise was false. `L-073` is marked `NARROWED — SUPERSEDED BY L-081` in `LEARNING_REGISTER.md`; the cap is replaced by `G10.2`'s competition-coverage test, which targets the variable that actually determines gradability.




The correction matters more than the picks it touched. A promoted control resting on a false empirical premise silently degrades every future slate containing that row type, and it does so invisibly, because the rule looks like accumulated experience. Any future promotion whose justification is "this has never worked" must state the search that was run and the endpoints that were tried, so the claim can be falsified the same way this one was.




**Ordering discipline preserved.** Nothing in this patch licenses promoting an opposite pick to manufacture an Over/Under win. `G20.2` and `G21.1` are disclosures; `G26.1` removes an unjustified claim to the top slot but never promotes a row on a reference rate. `G23.1`'s prohibition on mechanical band moves is unchanged.




## 14. September 6(c) external blindspot audit amendments — L-087–L-101




Effective **2026-09-06**, same day as §13, in response to an externally supplied Google-Drive-read-only audit (`archive/EXTERNAL_BLINDSPOT_AUDIT_2026-09-06_RECEIVED.md`) identifying fifteen governance blindspots (`B-01`–`B-15`). Full disposition of each: `LEARNING_REGISTER.md` §"2026-09-06(c) external blindspot audit disposition." **Every item below is a governance/validity/disclosure control. None fits a coefficient, assigns a scenario weight, publishes a probability, or claims predictive lift**, and several items confirm that an existing gate (`G25`/`G25.1`/`G30.1` for cross-row coherence; `G10.2`/`G20.2`/`G21.1`/`G26.1` for settleability and totals) already covers the finding and needed no new mechanism.




| Change | Gate/field | Lesson |
|---|---|---|
| Predictive-weighting firewall applied retroactively to `L-075`–`L-077`, splitting each into a disclosure component (`PROMOTED_PROCESS`) and a magnitude component (`CANDIDATE`) | — (register-level; see `LEARNING_REGISTER.md`) | `L-087` |
| Rank-gap / ordering-strength field added to the row-robustness record | `G23` table, new `rank_gap` field | `L-088` |
| Two-pass result-blind retrospective discipline | `G37.1` | `L-089` |
| Mandatory stratification of the settlement-only performance scorecard | `PERFORMANCE_ELIGIBILITY_POLICY.md` | `L-090` |
| Raw contract W/L confirmed descriptive-ledger-only, never the leading performance claim | — (reporting discipline) | `L-091` |
| Settlement-source pre-registration (`G10.2`) confirmed as the universal actionability gate across all niche/operator-sensitive markets, not corners alone | `G10.2` (unchanged; scope note) | `L-092` |
| Unresolved/provisional-row rate tracked by sport/market/source tier as a standing quality signal | `DATA_SOURCE_REGISTER.md` | `L-093` |
| Dual historical-compliance fields: `ISSUE_TIME_PROCESS_GRADE` vs `CURRENT_RULE_GAP` | §9 retrospectives | `L-094` |
| Control-taxonomy classification (`BLOCKING_INTEGRITY` / `MECHANISM_REQUIRED` / `CONTEXT_MATERIALITY`) for new promoted controls | `LEARNING_REGISTER.md` §2 | `L-095` |
| Periodic control-effectiveness review (recurrence rate before/after a control's effective date) | `LEARNING_REGISTER.md` §2 | `L-096` |
| Recurring Rank-1 total/Under failures confirmed already addressed by same-day `G20.2`/`G21.1`/`G26.1`; no new mechanism | `G20.2`, `G21.1`, `G26.1` (unchanged; cross-reference) | `L-097` |
| Winner/handicap/total incoherence confirmed already covered by `G25`/`G25.1`/`G30.1`; execution-verification note only | `G25`, `G25.1`, `G30.1` (unchanged; execution note) | `L-098` |
| Evidence-density labelling (`DENSE`/`MODERATE`/`SPARSE`) for sport-specific lessons | Each `RULES_<SPORT>.md` | `L-099` |
| `MARKET_BLIND` terminology clarified as price-blind/market-analysis-blind, not market-independent | §4 bookmaker-independence hard gate | `L-100` |
| `P-241`–`P-267` cohort formally tagged `REPRODUCIBILITY-LIMITED` | `GAME_LOG_STATUS_INDEX_2026-09-05.md` (cross-reference) | `L-101` |




**On the firewall finding (`L-087`) specifically.** The audit's central criticism — that `L-075`, `L-076` and `L-077` were labelled `PROMOTED_PROCESS` while actually prescribing a discount magnitude derived from a single session's outcome — is accepted as correct. §9's existing text ("one event creates a candidate, never a weight") already said this; the gap was that it was not being applied to lessons that were *labelled* process controls but whose content was a weighting instruction. The fix is not to retract `L-075`–`L-077` — their disclosure requirement (a materially contradictory named fact must be written down and reconciled, or its omission is a process defect) is sound and stays mandatory — but to split off the magnitude instruction into `C-WEIGHT-PROPAGATION`, a frozen prospective test, exactly as any other weighting candidate requires. This split is the template for evaluating any future lesson: does it require a fact to be *considered and disclosed* (promotable immediately), or does it prescribe *how much* that fact should move an order (never promotable from one session)?




**On what this section does not do.** It does not reopen any settled card. It does not retro-tag the 86 lessons that predate `L-095`'s taxonomy — that is explicitly deferred as a separate, larger task. It does not narrow `EP-2026.09.06-v2`'s settlement-only eligibility gate — `L-090` requires the resulting scorecard be stratified, not that fewer rows be eligible.




## 15. September 6(d) second independent review amendments — L-102-L-121




Effective **2026-09-06**, same day as §14, in response to a second, separately supplied local document (`archive/GAME_LOG_BLINDSPOT_REVIEW_2026-09-06_RECEIVED.md`) reviewing this repository's own records including this session's own immediately preceding work. Full disposition: `LEARNING_REGISTER.md` section "2026-09-06(d) second independent review disposition." **Every item below is a correction to gate wording, disclosure completeness, or reasoning validity. None fits a coefficient, assigns a scenario weight, publishes a probability, or claims predictive lift.**




**Central finding, stated plainly: three gates this session had itself adopted earlier the same day (`G20.2`, `G21.1`, `G26.1`) reintroduced the exact same-session-derived-ordinal-rule pattern that the predictive-weighting firewall (`L-087`, §14) was adopted specifically to prevent.** That firewall was applied, in §14, only to externally-cited historical lessons (`L-075`-`L-077`); it was not yet applied to this framework's own concurrently-drafted new gates. This section corrects that omission and states the general principle once: **the firewall applies to this repository's own new work with exactly the same force as it applies to any externally-cited lesson.** A same-session cohort finding may motivate a mandatory *disclosure*; it may never, by itself, motivate a hard *ordinal bar* written into the live gate text on the same day the evidence was produced.




| Change | Gate | Lesson |
|---|---|---|
| `G20.2` hard bar ("may not be Rank #1") withdrawn; reclassified disclosure-only; "already-observed combination" overclaim corrected to a labelled sensitivity scenario | `G20.2` | `L-104`, `L-107` |
| `G21.1` hard rule ("central-band may not outrank union") withdrawn; reclassified disclosure-only; union/intersection category error corrected (`TRUE_UNION` / `LOW_BAR_CUMULATIVE` / `CENTRAL_BAND`) | `G21.1` | `L-104`, `L-106` |
| `G26.1` hard bar (40-60% reference-split exclusion) withdrawn; reclassified `CANDIDATE C-SEPARATION-FLOOR`, no threshold asserted without derivation | `G26.1` | `L-104` |
| `G25.1`'s blanket `DISJOINT` ban given nuance — a mathematically valid counterexample (three mutually exclusive outcomes at 0.45/0.40/0.15, correctly ranked #1/#2) shows marginal-probability ranking and joint-branch coherence are different objectives | `G25.1` | `L-108` |
| `G30.1`'s claim that cushion strength "necessarily" transfers substantial weight to the outright-win branch is withdrawn — a valid counterexample (70% cushion cover, 80% favourite outright win, simultaneously true) is given; an unusual supplied sign is now explicitly routed to an identity check first | `G30.1` | `L-109` |
| `G36.1` split into two separate fields, `RESEARCH_GRADE` and `OPERATOR_ACTION`, so neither a missing operator convention nor a genuine settlement result can be silently merged into or masked by the other | `G36.1` | `L-119` |
| `G10.1` gains source-independence and access-failure nuance: a structured field is not infallible or automatically independent of another endpoint sharing the same upstream vendor, and a route's access failure does not itself prove a competition is uncovered | `G10.1` | cross-referenced from `L-092` |
| New `rank_gap`-adjacent lessons on ledger recomputation, row recovery, and dimensional/unit checking for sport-specific formulas, none of which changed a gate's live text but all of which changed how this framework verifies its own numbers before publishing them | — (process/verification discipline) | `L-102`, `L-103`, `L-105` |
| Population, reasoning, and identity corrections to specific settled cards' retrospective text (not their contract outcomes) | — | `L-110`, `L-111`, `L-112`, `L-113`, `L-114`, `L-115`, `L-116`, `L-117`, `L-118` |
| Confirms `L-090` already answers the "no reliable pooled all-history strike rate" question | — | `L-121`, cross-reference only |




**On why this happened.** `G20.2`, `G21.1` and `G26.1` were drafted in direct response to a real, correctly-diagnosed pattern (recurring Rank-1 total/Under failures) using the same session's own settlement data as the motivating evidence — and then written as live ordinal rules the same day, rather than as disclosures pending their own prospective tests. This is precisely the failure mode `L-087` names. The lesson generalises beyond these three gates: **any control drafted from evidence produced in the same session it is adopted must default to disclosure-only, with its ordinal force explicitly deferred to a named, frozen prospective test, regardless of who or what proposed the control** — this framework's own drafting process included.




**On verification discipline.** Every correction in this section was independently re-derived from primary source before being accepted — the settlement table, the ESPN API records retrieved earlier in this session, and the preserved raw component text — rather than accepted on the second review's assertion alone. Several of its claims (the corrected 15-card Rank #1/#2 cohort, the ESPN official match-numbering, the AFL points formula) were confirmed to match exactly on independent recomputation, which is recorded in `LEARNING_REGISTER.md`'s disposition table rather than only asserted here.




**What this section does not do.** It does not change any settled card's contract outcome. It does not retro-classify the 86 lessons predating `L-095`'s taxonomy. It does not resolve the `P-099`/`P-115`/`P-171` ETPL population gap (flagged, not fabricated). It does not re-litigate the ~200-row historical game-by-game table the second review supplied — the register absorbs the underlying classes of finding instead of re-annotating each historical card individually.




## September 6 user directive — settlement is the sole performance-eligibility gate




[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md), policy `EP-2026.09.06-v2`. The user directed that **any log that has been settled counts for performance eligibility.** This replaces pre-game-versus-live-issued horizon, import timing, git/local-timestamp provenance and the `E1-Q-LATE_IMPORT` label as tests for whether a settled row counts in the historical performance scorecard: the sole test is now whether the row has reached a final, graded result. `LIVE_ISSUED` cards are no longer a separate excluded cohort once settled — see the policy file for the full statement of what changes and what does not (no-action records, unresolved/void/partial rows, process-versus-outcome grading, no hindsight rewriting, and the numerical model's own separately-governed Stage 0/`E1-P` pipeline are all unaffected).




## September 5 user confirmation — controlling eligibility correction




[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md). The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.




Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.




The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.




Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.




Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.




## 16. September 6(f) — v4.0 comprehensive overhaul: gate portfolio consolidation




Status: **CONTROLLING.** Effective **2026-09-06**, method `MDS-2026.09.06-v4.0`. Origin: `archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md`, a complete review of every game log from `P-001` to `P-317` against this rule set, requested and delivered the same day, finding (i) a measured mandatory-checklist compliance rate between 0% and 28% across 238 parsed cards, (ii) an all-history Rank #1 record of 59.2% with no demonstrated separation from Rank #4 (which outperforms it in the largest fully-explicit sample), and (iii) a ~570 KB / ~143,000-token mandatory pre-research read that no session can complete in full before opening a stats source. This section is the controlling response. **Nothing below deletes any historical gate definition, card, or settlement in §§0–15 above — every gate discussed remains defined exactly as written, for reference and for interpreting historical cards issued under it.** What changes is which gates are *mandatory on every new card going forward*.




### 16.1 Governing principle




More process was not converting into better forecasts; it was converting into unexecuted checklists. The fix is not to add a 49th gate. It is to determine which of the existing 48 gates are actually load-bearing, make those genuinely mandatory and genuinely checked, and stop requiring the rest as blocking gates on every card. This is a validity and workload-triage correction. It fits no coefficient and claims no predictive lift, exactly like every other entry in §§12–15.




### 16.2 Gate classification (supersedes §11.9 as the mandatory-card authority)




| Class | Meaning | Gates |
|---|---|---|
| **BLOCKING** — hard fail, no actionable forecast without it | Identity, contract, state and settlement integrity; a failure here means the forecast is not about a well-defined event | `G0`–`G6` (admission), `G8` (provenance, simplified to: exact URL/record + access time + claim owner), `G31` (final refresh), `G36`/`G36.1` (settlement from official record), the `L-079` synthetic-content exclusion (§4) |
| **REQUIRED ANALYSIS** — mandatory, and this is the actual forecasting work | Omission is a process defect; these are the steps that would plausibly change a rank | `G13.1` (L5/L10/L15/L20 descriptive recency review), `G14`/`G14.1` (exposure chain and deficit attribution), `G14.2` (bench/coaching — retained: the origin evidence at `P-304` is a real, generalisable driver), `G15.1` (environment/surface — retained: this is a genuinely failed hard gate, not a candidate; see §16.4), `G16` (joint event object, now with the explicit-arithmetic requirement at §16.5), `G20`/`G20.1` (component and separation budgets), `G22` (bidirectional-sign audit) |
| **GUIDANCE** — sound practice, demoted from blocking because no card in this repository's history has demonstrated its absence changed an outcome or its presence prevented a wrong one | Still recommended; a card may use them; none is required for the card to issue | `G4.1`, `G9`, `G10`, `G17`, `G17.1`, `G19`, `G21`, `G23`, `G24`, `G25`, `G25.1`, `G26`, `G27`, `G28`, `G29`, `G30.1` |
| **REMOVED FROM THE LIVE CARD** — already reclassified `CANDIDATE`/disclosure-only in §15; now removed from the mandatory checklist entirely rather than retained as a disclosure burden | Their own prospective test manifests (`C-TAIL-BUDGET`, `C-PATH-GEOMETRY`, `C-SEPARATION-FLOOR`) remain open in `LEARNING_REGISTER.md` (the lesson archive) and may still be run deliberately on a card if useful, but are not required | `G20.2`, `G21.1`, `G26.1` |
| **UNRESOLVED CROSS-REFERENCE, CORRECTED HERE** | `AGENT_ROLE_AND_TASK.md` §6 item 12 and this file's own checklist item 27 (§11.9) continued to mandate `G26.1`'s result and the superseded `UNION_LOW_THRESHOLD`/`INTERSECTION_CONSTRAINT` vocabulary after both were withdrawn at §15 — a live defect the overhaul review documented at its §5.3. Both are corrected by this section superseding them; see §16.3 |




### 16.3 The new mandatory card checklist (supersedes §11.9)




A card must complete every `BLOCKING` and `REQUIRED ANALYSIS` item above, in this compressed form:




1. Identity/contract/target/time/participant freeze (`G0`–`G6`), method version read fresh this session from `METHOD.md`'s single version banner — not from any individual file header, which is why this repository's version chaos occurred in the first place (§5.3 of the overhaul review).
2. Exact source record, claim owner and access time for every decisive fact (`G8`, simplified).
3. Synthetic/simulated/preview content excluded from settlement (`L-079`).
4. L5/L10/L15/L20 table plus descriptive recency review, both sides and head-to-head, with the continuity gate (`G13.1`).
5. Exposure chain, deficit attribution, and the bench/coaching/rotation record for both sides (`G14`/`G14.1`/`G14.2`); `BENCH_NOT_RETRIEVED` still blocks a margin or full-game total row from Rank #1.
6. Environment and current-surface gate for every outdoor/open-roof event, with a venue-coordinate hourly forecast — not a city forecast — from one hour before start through the plausible endpoint (`G15.1`). **This gate failed on ~90% of outdoor cards measured in the overhaul review and is not being relaxed; it is being enforced.** A card without it does not issue.
7. One joint event object stated as an explicit prior, a named signed adjustment with a stated weight, and a resulting centre-and-width — not an unweighted adjective ("requires shrinkage") and not a bare range with no stated interpretation (`G16`, §16.5).
8. Component budget for totals and separation budget for margins, with exact joint-distribution queries under G-L24. Endpoint transitions are applied only if the base distribution does not already include them. See METHOD section 4.
8a. **Shared-driver failure mass** (`G-L17` §16.12(a), `G-L21` §16.13(a)): `P(¬R1 ∧ ¬R2)` for the top two, and `P(all fail)` with Fréchet bounds wherever three or more ranked rows need the same state — a number, or `JOINT_UNQUANTIFIED` with bounds. State the **sign** of each row under the shared driver before calling them jointly supported. An unanswered line blocks the card exactly as an unretrieved bench blocks a Rank-#1 margin row.
8b. Label each O/U FORCED_PAIR or FREE and freeze its preferred direction. Derive push mass from the conditional distribution; no universal MLB push cap. Apply SCORING_AND_VALIDATION.
9. Bidirectional-sign audit for every two-way mechanism (`G22`).
10. Final volatile refresh before issue (`G31`).
11. **An explicit `UNVALIDATED_SUBJECTIVE` probability for every ranked row** (new — §16.6, full specification in `METHOD.md`).
12. Settlement from the official record, `RESEARCH_GRADE`/`OPERATOR_ACTION` split where relevant (`G36`/`G36.1`).
13. **At settlement:** the structured process record and the §16.11(o) disruption facts, with the explicit process-versus-outcome classification (`G-L23` §16.13(c)). No control may be amended from a result until this is printed.




**Mechanical check.** Run `python audit_card_controls.py <log.md> --settlement` over the running log at the settlement pass and record the per-card result (§16.8). The script detects *printed fields*, not good analysis: a PASS is weak evidence and a FAIL is strong evidence, which is the correct asymmetry for an execution audit. *(From the 2026-09-25 control manifest onward, add `--strict`: the 2026-09-24(f) controls 7r, T13, 10p and 10l then block.)*




Every `GUIDANCE`-class gate remains legitimate practice and may be used at the analyst's discretion; none is checked for compliance and none blocks issue. This is the change that makes the checklist executable: it is roughly 12 items instead of 28, and every remaining item was chosen because the overhaul review's compliance measurement or origin evidence showed it actually mattered.




### 16.4 Environment gate — explicitly not softened




To be unambiguous given the scale of the compliance failure found (§16.2's `REQUIRED ANALYSIS` note): `G15.1`/`GATE-ENVIRONMENT` is unchanged and is not a candidate for demotion. A card for an outdoor or open-roof event with no qualified venue-coordinate hourly forecast fails closed exactly as §11.3C and §11.5 already state. The fact that this gate was violated on approximately 90% of historical outdoor cards is a reason to enforce it going forward, not a reason to relax it.




### 16.5 Explicit-arithmetic requirement (replaces prose shrinkage)




Every joint event object (`G16`) must show its arithmetic, not merely assert a corridor. At minimum:




- the prior/baseline value and its sample (`G12`);
- each material adjustment, signed, with a stated weight or shrinkage fraction toward that baseline, and the reason for the weight;
- the resulting centre and an explicit width (not an unweighted "range");
- the located position of every supplied line against that centre and width, with the arithmetic shown — not "the corridor is 27–34, so the 50.5 line looks like an Under," which conceals that the joint two-team sum can straddle the line even when each team's own range looks favourable (the exact failure documented at `P-309` in the overhaul review, §5.5).




This is arithmetic on stated qualitative inputs, not a fitted model; it introduces no coefficient. It simply requires the addition that was already implicitly required and was not being shown.




**16.5(a) — outcome-state family enumeration with mass (added 2026-09-09, `G-L1`; disclosure requirement, not an ordinal bar).** A centre-and-width alone hides where the mass sits and lets a named kill path count as "handled" while carrying no weight. Every joint event object must additionally state:




- an enumeration of the **discrete outcome-state families** the sport permits — score families for a soccer/basketball/cricket total, margin families for a spread, set-count families for tennis — with an **explicit probability mass on each family, summing to 1**;
- for **every kill path identified in the `G22` bidirectional-sign audit that is supported by current, specific evidence**, the family it lives in and its share of that family's mass — a kill path may not exist only as a prose sentence once the evidence for it is current and specific (this generalises `L-070`'s "make both competitors' ordinary win/separation states contract-evaluable" to *every* material adverse state, and it is the `RULES_TENNIS.md` §4 straight-set/deciding-set mixture-weights method exported to all sports);
- one **representative Rank-#1 outcome** written in the settlement unit of *every other supplied row* (e.g. a representative final score that is simultaneously checked against the handicap line, the total line and the first-half line), with confirmation that it is compatible with the other leading directions before the order is frozen;
- the located position of each supplied line against the **modal family and its neighbours**, not only against the centre.




Origin evidence: `P-340` ("2–1 is an Under kill state", finished 2–1, Under ranked #3), `P-342` ("1–0/2–0 control", finished 0–2, Over ranked #2), `P-344` (secondary-scorer breakout written as prose, margin centre +0.5 vs actual +21). Positive model: `P-338` (tennis, best card of its cohort — one tree, explicit branch weights, representative scoreline verified). This is a *disclosure* change of the same class as §16.5's original "show the arithmetic" rule; it forces no particular weighting and promotes no coefficient (`L-087`).




**16.5(c) — aggregate-to-disaggregate retrieval rule (added 2026-09-09 second pass, `G-L7`; retrieval requirement, not a weight).** Where a decision-driving claim rests on an **aggregate** — a multi-start ERA line, a "team leaders" list, a rehab innings count, a season split, a form summary — and the **disaggregated record is available from a source already in the card's own register**, the disaggregated record must be opened and printed before the aggregate may carry directional weight. An aggregate that has not been disaggregated is recorded `AGGREGATE_ONLY` and cannot support a `LEAN` or `SUPPORTED` grade on the row that depends on it.




This gate exists because all three of the `P-333`–`P-344` cohort's Rank-#1 losses trace to the same retrieval failure, and in every case the disaggregated record was one click away on a source the card had already cited and pointed the *other way*:




| Card | Aggregate the card used | Disaggregated record that was available | What it showed |
|---|---|---|---|
| `P-339` | "Ryu 0–3, 7.31 ERA through seven second-half starts" | KBO official English player page game log (already in the card's source register) | Last four starts **7 ER/3⅓ → 4 ER/6.0 → 0 ER/5.0 with 7 K and 0 BB → 3 ER/5.0**. The slump was **front-loaded**, the worst start was three weeks old, the most recent evidence included a dominant scoreless start, and **command never broke** (0/0/1/2 walks; ~1.2 BB/9 season). An ERA-only slump with an intact walk rate is a noisy-outcome slump, not a skill decline. |
| `P-335` | "4.1 innings for Triple-A El Paso on Aug 30" (innings only) | MLB/MiLB rehab reports (same lane the card used for the rehab note) | The rehab **pitch-count ladder** was 14 → 47 → **64 pitches (44 strikes), 4⅓ scoreless, 7 K**. A starter who has just thrown 64 pitches scorelessly is stretched to ~5 MLB innings. He threw **63 pitches / 5.0 scoreless**. The "short start → early relief → Over" branch the card weighted `+0.20` toward was directly contradicted by evidence the card had partially retrieved. |
| `P-344` | "Hungary's leaders include Juhász (17.0 PPG, 12.3 RPG), Takács-Kiss (13.0 PPG, 10.0 RPG), Réka Lelik and Ágnes Studer" | FIBA official player profiles (already in the card's source register) | **Lelik was Hungary's third-highest scorer at 8.7 PPG across the three group games (8 / 14 / 4) on ~26 minutes a game, 4.3 RPG, 3.5 APG.** The card printed a quantified exposure line for the two players above her and left the third as an unquantified *name*. A blowout needs a third scorer; the card's margin distribution contained no third scorer with a number in it. She scored 23. |




The common shape is not "bad weighting" — it is that a **summary statistic was allowed to stand in for a record the card could have opened**, and the summary happened to point the wrong way. Disaggregation is cheap, checkable, and does not require a new source. `G8` already requires an exact source record per decisive fact; `16.5(c)` adds that the *granularity* must match the claim.




**16.5(d) - total-probability coherence (G-L8; corrected 2026-09-12).** Derive each probability from its declared outcome masses or CDF at the exact endpoint. Define width units and family; an absolute centre-to-line ratio cannot alone determine direction or probability, and different families need not share a probability ordering. For integer totals, distinguish strict Under/Over and push mass. Section 16.9 is controlling. The old cross-sport normalised-edge table below is an exploratory diagnostic, not evidence of miscalibration or a valid universal ordering.




Measured against the `P-333`–`P-344` cohort, the issued probabilities did **not** track the cards' own arithmetic:




| Card | Centre | Line | Width (stated) | Normalised edge | Probability assigned | Coherent order? |
|---|---:|---:|---:|---:|---:|---|
| `P-340` | 2.409 | 2.5 | ±1.8 | **0.05** | Under **0.55** | over-confident |
| `P-336` | 2.39 | 2.5 | ±1.55 | **0.07** | Under **0.60** | most over-confident |
| `P-341` | 2.35 | 2.5 | *not quantified* | ~0.08 | Under **0.58** | width missing — a §16.5 defect in itself |
| `P-342` | 2.83 | 2.5 | ±1.9 | **0.17** | Over **0.56** | coherent |
| `P-339` | 10.25 | 9.5 | ±4.1 | **0.18** | Over **0.56** | coherent |
| `P-344` | 149.5 | 146.5 | ±16 | **0.19** | Over **0.54** | slightly under-confident |
| `P-335` | 9.1 | 8.0 | ±3.2 | **0.34** | Over **0.52** | **largest edge on the cohort, lowest probability assigned** |
| `P-337` | 2.00 | 2.5 | ±1.0 | **0.50** | Under **0.65** | coherent — and it won |




`P-335` computed the largest normalised edge of the cohort and assigned it the *lowest* probability; `P-336` computed the smallest edge and assigned nearly the highest. The ordering was asserted independently of the arithmetic the same cards had just performed. **Honest counter-check, recorded because it matters:** re-scoring those eight preferred-total rows at normal-CDF-coherent probabilities would have produced a mean Brier of **0.2614** against the issued **0.2538** — i.e. on this cohort of eight, mechanical coherence would have been *slightly worse*. `16.5(d)` is therefore justified on **internal-consistency grounds only** (`METHOD.md` §5's "derived from"), explicitly **not** on demonstrated accuracy improvement, and it is a disclosure/coherence rule rather than a performance claim.




**16.5(b) — uncertainty through a declared model (G-L2; revised 2026-09-17).** State the skill/population prior, its strength and scenario weights. Symmetric uncertainty around an unchanged prior increases width; hierarchical shrinkage or asymmetric availability/performance mixtures can legitimately change both mean and variance. Explain the mechanism or prior rather than inserting an unsupported signed lean. Every dependent probability must be regenerated from the same distribution; evidence-grade caps are not row-level probability caps. See SCORING_AND_VALIDATION section 5.




**16.5(d) addendum - count targets (corrected 2026-09-12).** Use P(X < L), P(X > L), and P(X = L) for an integer line; at a half-line, map to the correct integer count. A mean above a line can coexist with a preferred Under, but the exact mass distribution must demonstrate it. Right skew alone does not guarantee a particular median/mean relationship. See section 16.9.




**16.5(e) - complement decomposition (G-L9; corrected 2026-09-12).** Partition complete outcomes into mutually exclusive exhaustive states and count each losing state once. Named mechanisms may overlap and may not force a final loss. Do not add overlapping early-hook and bullpen-fatigue masses or cap a full-game probability using a starter-only outcome. Split threshold-crossing states and disclose residual uncertainty; separate action-conditional from unconditional probabilities. See section 16.9.




Origin — the dominant failure of `P-345`–`P-371`, on eleven cards: `P-347` (Seattle team-total Under at 0.71 beside a named Miller hook/HR-cluster branch and Quantrill's 2.79 ERA / 3.96 FIP regression — Seattle scored five); `P-351` (Dodgers team-total Over at 0.70 with Ohtani out of the lineup — three runs); `P-354` (Hanshin team-total Over at 0.74 against Tokoda's documented long-start branch — one run); `P-356` (Samsung team-total Over at 0.70 against Ko's 3.05 second-half ERA — zero); `P-357` (Belfast 150+ at 0.72 with the XI unretrieved and a collapse branch — 107); `P-364` (Under at 0.61 beside an old ball, a set Brook and a deep tail — 210 at 45 overs); `P-365` (Brothers +1.5 at 0.60 beside the card's own "4–1 / 5–1 Uni-Lions" separation state — 6–0). In every case the kill path was on the card; it carried no number. This extends `G-L1` from "every kill path is a weighted branch" to "the weights must add up against the row". Disclosure only — it forces no particular mass and introduces no coefficient (`L-087`).




**16.5(f) - joint top-two probability (G-L10; corrected 2026-09-12).** Read q = P(R1 and R2 win) from the same complete joint model. Check max(0,p1+p2-1) <= q <= min(p1,p2). If joint structure is not quantified, print JOINT_UNQUANTIFIED and the bounds; do not default to independence. Coupling is a model-dependent hypothesis, not a universal label for a market pair. See section 16.9.




Historical motivation: P-358/P-359/P-360 each split the top two, while P-367 won both. These few selected outcomes do not establish negative or positive dependence. The corrected recent diagnostic is 6/23 both-row-graded cards, or 6/24 logically decidable both-win outcomes; P-366 is censored. No family-weight change follows.




**16.5(g) - uncertainty on observed rates (G-L11; corrected 2026-09-12).** Print actual numerators, denominators, time windows and opponent mix. For independent binomial proportions use sqrt[p1(1-p1)/n1 + p2(1-p2)/n2]; only equal variances permit a sqrt(2) simplification. Runs allowed and batting strike rate are not Bernoulli proportions. Unknown n stays unknown. Use suitable uncertainty intervals and sensitivity; no automatic two-SE direction/width rule. See section 16.9 and the NIST/ASA references there.




Withdrawn worked example: P-371 used three Belgium games and four Germany games with no frozen attempts. Equal assumed n=75 and the claim "mostly noise" are not measured evidence. P-345 also cannot be declared a real or absent mechanism solely from a rough standard-error threshold. Current personnel, opponent context and sample design still matter.




### 16.6 Probability and population-scoping pointer




Two further v4.0 changes are specified in full in `METHOD.md` rather than duplicated here, because `METHOD.md` is now the primary operational document: (1) the mandatory `UNVALIDATED_SUBJECTIVE` probability per ranked row, scored with Brier score against a 0.5 baseline, which is the change that makes forecast quality measurable for the first time in this repository's history; and (2) the designation of MLB, one soccer competition (EPL) and NRL/AFL as `PRIMARY_SCORED` populations, with every other sport/competition marked `EXPLORATORY — NOT SCORED` in the primary performance record. Both apply to every card issued from this point forward. Neither is retrofitted onto any already-issued card — doing so would be exactly the hindsight fabrication §4's honesty gate prohibits.




### 16.7 Gate-cap and retirement rule




The `GUIDANCE` list may not silently grow back into a `BLOCKING`/`REQUIRED ANALYSIS` list. Promoting a `GUIDANCE` gate (or introducing a new one) at either tier requires the same evidence bar as any other `PROMOTED_FORECAST` change in `LEARNING_REGISTER.md` — prospective, chronological, out-of-sample evidence, not a same-session finding (the `L-087` firewall, applied here with the same force the September 6(d) review applied it to `G20.2`/`G21.1`/`G26.1`). `L-096`'s periodic control-effectiveness review is operationalised: every 25 settled cards, review the `BLOCKING`/`REQUIRED ANALYSIS` list; a gate that produced zero instances of catching or changing a forecast across that window is a demotion candidate, recorded and reviewed rather than automatically removed.




### 16.8 Card completeness block — the execution audit (added 2026-09-11)




**Why.** The `P-358`–`P-371` external session listed `G-L7`, `G-L8`, `G-L2` and `G14.2` as "incorporated as active process constraints", yet **none of its thirteen issued cards printed an outcome-family mass table, a numeric total width, a normalised edge or a representative Rank-#1 outcome**, and two broke `G14.2` (`P-362`, `P-365`). `G-L1` was not even on its carried list. A control that exists only as a list item behaves exactly like a kill path that exists only as prose. The remedy is structural: a fixed block of fields at the foot of every card, checked mechanically at settlement.




**Every card ends with this block.** A field that cannot be completed is printed with its missingness code — never silently omitted.




1. The method version read this session, and the controls actually applied, by ID.
2. The outcome-family table with explicit masses summing to 1 (§16.5(a)).
3. For every total and margin row: centre, **numeric width**, normalised edge `|centre − line| / width`, and the probability; for right-skewed count totals, the median-based `P(total ≤ line)` (§16.5(d) and addendum).
4. The complement decomposition for Rank #1 and Rank #2 (§16.5(e)).
5. `P(R1 ∧ R2)` with its coupling label (§16.5(f)).
5a. **`P(¬R1 ∧ ¬R2)` — the shared-failure mass — with the single state that produces it (`G-L17`, §16.12(a)); and, where three or more rows share one driver, `P(all of them fail)` with Fréchet bounds and the sign of each row under that driver (`G-L21`, §16.13(a)). A number, or `JOINT_UNQUANTIFIED` plus bounds — an unanswered line blocks the card in the same way an unretrieved bench blocks a Rank-#1 margin row** *(added 2026-09-17(b): four controls were listed and not executed across the `P-438`–`P-451` import, the `M15` pattern)*.
5b. Every over/under row labelled `FORCED_PAIR` or `FREE` (`G-L15`), with the preferred side named for each forced pair and the push mass shown with its derivation (`G-L22`, §16.13(b)).
6. One representative Rank-#1 outcome, checked against every other row.
7. Participant state per side: lineup `CONFIRMED_OFFICIAL` / `PROJECTED_BEAT_VERIFIED` / `LINEUPS_NOT_YET_PUBLISHED @ <time>` / `NOT_RETRIEVED`, bench, head coach. **Where the competition publishes line-ups before the freeze time** — a cricket XI is nominated before the toss (MCC Law 1.2); baseball, soccer and rugby-league line-ups are normally published before the start — `NOT_RETRIEVED` after publication is recorded as **`RETRIEVAL_MISS`**, a process defect, not as unavailability. When official feeds are not yet published, a lineup verified under Control `S-1 Rev 2` as `PROJECTED_BEAT_VERIFIED` satisfies `G14.2` exposure modeling and does NOT block full-game totals or margins from Rank #1. Only an unmodeled/unretrieved bench (`BENCH_NOT_RETRIEVED`) triggers the Rank #1 block. **Amended 2026-09-24(f):** `PROJECTED_BEAT_VERIFIED` counts only with its printed S-1 Rev 2 receipt (outlet, reporter, timestamp, verbatim quote, two sources). Where an official lineup or goalie was published before the freeze, only `CONFIRMED_OFFICIAL` or `RETRIEVAL_MISS` is allowed. At settlement, field 10 carries the `C-LINEUP-DIFF` line. See §"2026-09-24(f)"(c).
8. `AGGREGATE_ONLY` flags (§16.5(c)) and the sampling-noise checks (§16.5(g)).
9. The settlement source for every row (`G10.2`).
10. **At settlement only:** the structured process record and the disruption facts, with the explicit process-versus-outcome classification (`G-L23`, §16.13(c)). **Amended 2026-09-24(f)/2026-09-25:** every process fact names its endpoint and retrieval time (`C-PROCESS-RECORD-PROVENANCE`; audit field `10p`). Team sports also add the `C-LINEUP-DIFF` line, "k of n named starters started" per side (audit field `10l`). Run `audit_card_controls.py --settlement --strict`.




**Audit.** At settlement, run `python audit_card_controls.py <running_log.md> --settlement` (repository root) over the external running log and record which fields each card printed. *(Rebuilt 2026-09-17(b) after being found missing from the repository root — the block had been self-reported since 2026-09-11, and the `P-438`–`P-451` run found field 5a absent on 13 of 13 auditable cards one day after `G-L17` was promoted.)* **Run it against the running log, not the combined log:** the combined log carries settlement summaries rather than issued card bodies, so a run there measures the summary's completeness, not the card's. Fields 1–9 are matched only against text printed **before** the card's settlement heading, and field 10 only against settlement text — otherwise a retrospective sentence credits the card with a disclosure it never made. Detection is deliberately generous, so a PASS is weak evidence and a FAIL is strong evidence. Where an imported log did not carry a card's body at all, mark that card `BODY_NOT_CARRIED`: an unauditable record and a non-compliant card produce identical output and mean opposite things. A missing field does not invalidate an issued card — issued evidence is immutable — but it is recorded as a process defect on that card, and a pattern of missing fields across a cohort is itself a finding, as it was on 2026-09-11. This is a format and audit requirement of the same class as §16.5's "show the arithmetic"; it adds no coefficient, weight or ordinal bar (`L-087`). *(From the 2026-09-25 control manifest onward, add `--strict`: the 2026-09-24(f) controls 7r, T13, 10p and 10l then block.)*




## 2026-09-06(f) — settlement and retrospective addendum




METHOD v4.0 and §16 remain controlling. [The full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md) applies existing G34/G36 and the source-independence rules: P-304/P-305 slates were recoverable; P-290's lower corner row was omitted from a top queue; P-217 can be research-graded only with its revised-innings convention explicit and operator action separate. Do not substitute a shortened mandatory powerplay for six completed overs. Retain start-crossed and superseded view labels. No new hard rank cap, numerical weight or retrospective probability is introduced; older source/ranking claims contradicted by this audit are historical only.




## 2026-09-09 — `P-333`–`P-344` cohort cross-sport settlement learnings




**Pass type:** settlement + retrospective + cross-sport algorithm improvement. Full evidence: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09 — P-333–P-344 imported and settled". Method `MDS-2026.09.06-v4.0` unchanged. Two **disclosure requirements** added to §16.5 (`16.5(a)` family enumeration with mass = `G-L1`; `16.5(b)` unit uncertainty is width not lean = `G-L2`). **No fitted weight, ordinal bar, gate ID or `CANDIDATE` control promoted** (`L-087` firewall; the 25-card `PRIMARY_SCORED` pattern review is the gate for any ordinal rule).




Cohort record: 9 issued cards (8 `EXPLORATORY`, 1 `MLB PRIMARY_SCORED`), 3 admin closures. Rank #1 **6 W / 3 L** (`P-339`, `P-342`, `P-344`). Potential winners **8 / 9**. Preferred full-match total O/U **4 W / 5 L**. The recurring failure was in the **margin and total corridors**, not winner identification — exactly what §16's winner/margin/total separation predicts.




| ID | Learning | Disposition |
|---|---|---|
| `G-L1` | Joint object must enumerate outcome-state families with explicit mass; every current-evidence `G22` kill path appears as a weighted branch; one representative Rank-#1 outcome written in every other row's unit. | **§16.5(a) disclosure requirement.** Origin `P-340`/`P-342`/`P-344`; positive model `P-338`. |
| `G-L2` | Unit-performance uncertainty (returning starter, slumping veteran, rotated side, cold shooter) widens the distribution; a net signed total lean needs a named *directional* mechanism. | **§16.5(b) disclosure requirement.** Origin `P-335`/`P-339`/`P-342`. |
| `G-L3` | Competition-tier gaps (promotion, cup mismatch) are a distinct uncertainty — do not pool the weaker side's lower-tier rates into the centre; build a tier-translation branch; a *rotated* favourite produces territory + late conversion, not early goals. | **Observation → candidate-watch** (`P-341`, `P-342`). `RULES_SOCCER.md` §"2026-09-09". Needs 3+ recurrences. |
| `G-L4` | Winner and margin are separate answers from the same family set; a right winner with a compressed margin distribution is a margin-model failure. | Reinforces existing winner/margin/total separation. `RULES_BASKETBALL.md` controls 9/11/16. |
| `G-L5` | An `Under` supported by a clean-sheet run needs creation → shot-quality → finishing → goalkeeping decomposition before the history is treated as a low-event mechanism. | Reinforces `RULES_SOCCER.md` control 27 (`P-336`). |
| `G-L6` | In-game shocks with no pregame forecastability stay aleatory (`L-117`) — never a "should have known", never a pregame rule — but do not excuse a separately underweighted branch. | Reinforces `G37.1` / `L-117` (`P-344` Hayashi injury). |
| `G-L7` | **Aggregate-to-disaggregate retrieval.** Where a decision-driving claim rests on an aggregate and the disaggregated record is available from a source already in the card's register, open and print it before the aggregate carries directional weight; otherwise mark `AGGREGATE_ONLY` and cap the dependent row. | **§16.5(c) retrieval requirement.** All three Rank-#1 losses (`P-339` game log, `P-335` rehab pitch-count ladder, `P-344` third-scorer exposure line) trace to this single failure. |
| `G-L8` | Exact PMF/CDF at the contract line, with signed direction, support, endpoint and push mass; no universal ordering by absolute normalised distance. | SCORING_AND_VALIDATION sections 1 and 5; section 16.9. |




### Which O/U family has actually been the reliable one — three-cohort descriptive record




The user's standing ask is that the preferred over/under selection should win more often. The mechanically-true measure ("did at least one O/U row win") was already retired as meaningless in the 2026-09-06(d) correction, because an exact half-point complementary pair forces one winner regardless of skill (`L-055`). The honest measure is **highest-ranked O/U selection accuracy**, and split by family it shows a consistent gap:




| Family | `P-294`–`P-305` | `P-318`–`P-332` | `P-333`–`P-344` | Combined |
|---|---|---|---|---|
| Highest-ranked O/U row of any kind | 7 / 12 | — | **6 / 9** | — |
| `1H Over/Under 0.5` (phase total) | — | 5 W / 2 L | 3 W / 2 L | **8 W / 4 L (67%)** |
| Full-match goals total (soccer only) | — | 6 W / 3 L | 2 W / 3 L | **8 W / 6 L (57%)** |




This is the **third** cohort consistent with the observation already written into `RULES_SOCCER.md` §"September 5(b)" — *"first-half goal markets [are] the more resiliently-sourced early-scoring contract type relative to both full-match totals and corners."* Under the framework's own 3-recurrence threshold this is now formally registrable as a **`CANDIDATE`** with a prospective test manifest — **not** an ordinal bar, and **not** a licence to promote a 1H row above a better-evidenced full-match row (`L-087`, `G23.1`). Samples are small, mixed-competition and within-card dependent; the counts are descriptive.




**The mechanism behind the gap, and the actual fix.** Across the `P-333`–`P-344` soccer cards the full-match goal centres were **unbiased but imprecise**: mean signed error −0.20 goals, mean **absolute** error **1.49 goals**, against stated widths of ±1.55–1.8. The width was roughly honest; the problem is that the supplied line then sat only **0.09–0.50 goals** from the centre. A 0.09-goal edge on a ±1.5-goal error distribution is a coin flip, and no research improvement will make it otherwise. The full-match total is therefore not a row to pick *better* — it is a row to **rank honestly**, which the descriptive record supports: in this cohort the full-match total went **2 / 2 when it was Rank #1** (`P-336`, `P-337` — both persistent multi-window low-output `Under`s with the two largest normalised edges on the cohort) and **1 / 5 when it was Rank #2** (`P-344` won; `P-335`, `P-339`, `P-341`, `P-342` lost). Promote a full-match total only when it has *both* (a) a persistent multi-window mechanism, not a single-regime or single-streak one, and (b) a normalised edge that justifies its probability under §16.5(d).




**Operational note (cricket, `P-333`/`P-343`):** for innings-order-dependent cricket targets, begin the toss / live-state handshake earlier so the `PREGAME` window is not lost to the start-crossing invariant. `CR-P3` and cricket §10.6.2 worked as designed — both events correctly issued no forecast.




## 2026-09-11 — `P-345`–`P-371` cohort cross-sport settlement learnings




**Pass type:** settlement + retrospective + control-execution audit + cross-sport algorithm improvement. Full evidence: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-11 — P-345–P-371 imported, settled and retrospected". Method `MDS-2026.09.06-v4.0` unchanged. **No fitted weight, ordinal bar or new gate ID** (`L-087`); every addition below is a disclosure, retrieval, arithmetic or format requirement of the same class as §16.5's original "show the arithmetic".




Cohort: 26 issued cards (4 `MLB PRIMARY_SCORED`), 1 administrative closure (`P-370`), 1 unsupplied collision record (`TMP-SETTLED-20260911-01`). Rank #1 **16 W / 9 L** (+1 provisional L); top two both won **6 / 25**; potential-winner labels **13 / 25**; mean Brier **0.2434** over 105 graded rows (`P-358`–`P-371`: 0.2621, worse than the 0.5 baseline). Learning-only per user direction.




| ID | Learning | Disposition |
|---|---|---|
| **`G-L9`** | Complement decomposition — itemise `1 − p` across the row's named kill paths; lower `p` if they do not fit. | **§16.5(e).** Eleven cards (`P-347`, `P-351`, `P-352`, `P-354`, `P-356`, `P-357`, `P-361`, `P-362`, `P-364`, `P-365`, `P-371`). |
| **`G-L10`** | Joint top-two probability with a coupling label; `TOP-TWO HEDGE` when anti-coupled. | **§16.5(f).** `P-358`, `P-359`, `P-360`, `P-365`; positive mirror `P-367`. |
| **`G-L11`** | Sampling-noise check on small-sample rates before any signed adjustment; applies in both directions. | **§16.5(g).** `P-356`, `P-358`, `P-369`, `P-371`; counter-example `P-345`. |
| `G-L8` clarification | Right-skewed count totals: locate the line against the median of the family table. | §16.5(d) addendum. `P-347`, `P-349`. |
| **§16.8** | Card completeness block + settlement audit script. | New. Origin: 0 of 13 `P-358`+ cards printed a family table, width or normalised edge. |
| Line-up publication | `NOT_RETRIEVED` after the competition's own publication time is a `RETRIEVAL_MISS`. | §16.8 item 7. `P-357` (post-toss XIs), `P-362`/`P-365` (`G14.2` breaches). |
| Winner labels | Print the upset (and, in soccer, draw) mass beside any winner label at or below 60% or any plurality winner. | Application of `G-L1`. Labels went 13 / 25; soccer three-way 1 / 5. |
| Candidates opened | `C-RUN-CENTRE-BIAS` (baseball centres ran 1.58 runs high over 12 cards), `C-PROB-EXTREMITY` (`p ≥ 0.70` rows won 13 / 21), `C-UNDERDOG-SEPARATION` (basketball). | Prospective manifests in `LEARNING_REGISTER.md` §"2026-09-11"; no ranking effect. |




### The over/under record after four cohorts — and what it now implies




| Family (favoured side) | `P-318`–`P-332` | `P-333`–`P-344` | `P-345`–`P-371` |
|---|---|---|---|
| Phase totals (earlier cohorts: soccer 1st-half 0.5 only) | 5 W / 2 L | 3 W / 2 L | **7 W / 2 L** |
| Far-from-centre alternate lines | — | — | **3 W / 0 L** |
| Baseball team-total Unders v the stronger starter | — | — | **6 W / 2 L** |
| Supplied main-line full-game totals | soccer 6 W / 3 L | 4 W / 5 L | **13 W / 13 L** (Over-favoured cards 1 W / 5 L; Under-favoured rows 11 W / 8 L) |




**Measured centre error** (actual minus stated centre): soccer, 10 cards — mean −0.27 goals, **mean absolute 1.42**; baseball, 12 cards — mean **−1.58 runs** (9 of 12 below centre), mean absolute 3.35; basketball, 6 cards — mean **+4.9 points**, mean absolute 8.4. The supplied main line typically sits 0.05–0.5 of a width from the centre, so it remains close to a coin flip however much research is added. The implications written into the sport files: say "coin flip" when the normalised edge is small (§16.5(d), §16.8 item 3); correct the measured biases through mechanism, not coefficient (baseball control 26, basketball controls 22 and 24); when the user asks for the analyst's own picks, prefer the families that have held — phase totals, far-from-centre alternate lines, team-total Unders anchored on the stronger starter — as **guidance**, never as an ordinal bar (`G23.1` still ranks the supplied rows by marginal probability).








### 16.9 Probability, dependence and retrospective corrections - 2026-09-12








These corrections apply to future research and to interpretation of the historical retrospectives. They change no issued selection, probability, or outcome. The full log remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current user instruction. Older eligibility statements are historical. No numerical model, coefficient, or accuracy improvement is validated by this pass.




## Probability must describe the exact contract




G-L8 correction: use the distribution or joint scenario table for the exact target. For total X and threshold L, P(Under)=P(X<L), P(Over)=P(X>L), and P(push)=P(X=L) when the contract provides a push. State void/censoring separately. On an integer-valued target and a half-line, Under L is X<=floor(L). For integer lines, using P(X<=L) as the Under probability incorrectly includes the push mass.




Print the direction, centre definition (mean/median), width definition (standard deviation, interval coverage, or scenario range), and the signed distance from the line. Absolute distance alone loses direction. Mean and width do not uniquely determine a distribution; a median alone does not determine a probability either. Cross-card probability ordering by absolute normalized distance is justified only under a common specified standardized distribution and comparable width definitions. The old cross-sport normal-CDF comparison is an illustrative sensitivity calculation, not proof that the issued probabilities were incoherent. Do not enforce an invented 0.50-0.53 probability band from an undefined 0.10-width distance.




G-L9 correction: named adverse mechanisms can overlap and need not guarantee a loss. Partition complete outcomes into mutually exclusive, exhaustive states, then add each losing state's mass once. For example, an early pitching hook and bullpen fatigue can happen together; six innings allowing one run does not force a full-game team-total Under if the bullpen subsequently allows runs. If a state crosses a threshold, split it or disclose unresolved within-state mass. A representative score checks compatibility but does not identify the probability of a whole branch. Keep conditional-on-action probabilities distinct from unconditional win/loss/push/void probabilities.




## Top two and over/under assessment




G-L10 correction: derive the intersection q=P(A and B) from the joint outcome table. Verify max(0,pA+pB-1)<=q<=min(pA,pB). Compare q with pA*pB only within that same model and conditioning convention. If dependence is unspecified, publish those bounds and JOINT_UNQUANTIFIED instead of inventing an exact q or declaring independence. For two distinct total targets, P(at least one wins)=pA+pB-q; for more than two, enumerate the union without double counting.




An underdog handicap and Under are not inherently negatively dependent; an underdog rout can be short/low scoring, a favourite rout can be fast/high scoring, and close games can be slow. Similarly, an underdog tennis handicap can win in a short straight-set victory. Observing one winner and one loser on three cards does not establish a correlation. Treat the proposed coupling as a conditional mechanism to test.




Exactly one of an Over/Under half-line pair wins only when both contracts refer to the same completed target and have matching action/settlement conventions. Integer pushes, voids, shortened targets, retirements, and mismatched periods break an unconditional guarantee. Counting both sides is not evidence of successful selection. Freeze one preferred direction per distinct target before play; separately report rank 1, rank 2, both top two, preferred O/U, and at-least-one across distinct targets. Show both-row-graded and logically-decidable denominators; exclude unresolved/censored cases explicitly. Preserve losing and process-defective observations. No after-the-fact choice of a winning direction.




The prior phase-total/team-total-Under advantages are small, selected, mixed-population observations. They do not justify a general preference for those families. Compare fixed target families prospectively within competition, endpoint, line difficulty, and information horizon; use event clusters rather than treating complements as independent observations. Existing candidate manifests remain hypotheses.




## Sampling uncertainty and retrieval provenance




G-L11 correction: retrieve actual makes/attempts, exposure, dates, and roster regime before computing uncertainty. For independent binomial samples, a descriptive standard error for a difference is sqrt[p1(1-p1)/n1+p2(1-p2)/n2]. The sqrt(2) shortcut requires equal variances. Shot quality, player mix, repeated possessions, and game clustering may violate the binomial assumptions. Runs per innings, ERA, and strike rate are not binomial success proportions; do not apply the same formula to them. If denominators or dependence are unknown, record UNCERTAINTY_NOT_QUANTIFIED and show justified sensitivity rather than fabricate attempts.




Withdraw the automatic 'less than two SE means width only/mostly noise; greater means real' rule. A threshold does not establish either a causal effect or its absence. Report sample size, context, uncertainty, and any explicitly assumed shrinkage sensitivity. [NIST's proportion interval guidance](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm) supports appropriate small-sample intervals; [the ASA statement](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) rejects mechanical threshold-only scientific conclusions. Both are methodology references, not sports-predictive features.




For P-371 specifically, the card had three Belgium games and four Germany games; it did not freeze attempt denominators. The old equal-75-attempt / 1.7-SE calculation cannot establish that the difference was mostly noise. The shooting reversal is an observed result, not evidence that its exact magnitude was forecastable.




Participant audit: record both teams' starters, bench/reserves, and coaches as separate fields, with exact evidence URL and publication/access time. Separate what the issued card captured from what a later box score now exposes. Nominated before the toss does not mean publicly retrievable before the forecast. Call a miss RETRIEVAL_MISS only when accessible publication before cutoff is evidenced; otherwise PUBLICATION_TIME_UNVERIFIED or NOT_RETRIEVED. Tennis benches are NOT_APPLICABLE; named coaching information can still be unknown. Do not label a combined lineup/bench/coaching check complete if one of those applicable fields is missing.




## Source and retrospective discipline




Resolve the exact event, date, competition round, team order, period, field, final status and source lineage after opening the URL. A search excerpt can refer to a different match from the opened page. Different hostnames, translations and proxies do not prove independent upstream scoring. Multiple secondaries cannot repair an unfrozen provider definition. A league-branded shell without the field is not evidence of zero.




Apply the existing MARKET_BLIND boundary to source content as well as to prices. P-364's mini log explicitly used a Sporting Life betting-tips/in-play-preview page for conditions; this was a source-selection breach of METHOD section 1. Preserve it as issued evidence, exclude that material from prospective inputs, and retrieve the original broadcaster/board/venue report for the sporting fact. Review PerformanceOdds, bookmaker, tipster and affiliate pages cited by other cards by claim; their names or availability do not make them approved research sources.




For a failed top pick, identify the target's first decisive checkpoint, actual score/phase facts, assumptions in the original card, what was demonstrably knowable, and plausible alternatives. A narrative listing a possible loss does not prove its probability was too low; a final score alone does not prove the causal story. Credit sound retrieval and successful target logic separately from wins forced by complementary pairs. Retain positive cases and limitations together. Validate candidate predictive changes on future data; do not claim that correcting the explanation would necessarily have changed the pick or made it win.








### 16.10 Margin-distribution, fixture-identity and derivative-settlement requirements — 2026-09-15




Origin: the `P-373`–`P-423` import (`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"). **Disclosure and process requirements only — no coefficient, no ordinal bar, no fitted probability (`L-087`).** They sit beside §16.5(a)–(g) and §16.9 and are audited by the §16.8 completeness block.




**(h) `G-L12` — declared margin prior and conditional uncertainty (revised 2026-09-17).**




1. Print the margin prior, source, target and uncertainty before adjustment; state every signed mechanism and any shrinkage target/strength.
2. Missing information is not an automatic underdog lean. A genuine hierarchical population prior or asymmetric mixture may move the centre, including toward zero, while changing variance; document it and regenerate all contract probabilities.
3. **Residual benchmarks, not universal floors.** NFL 13.9 points (Stern 1991) and historical sport residuals describe their source populations. Compare conditional held-out coverage and dispersion for the actual scope. They impose no mathematical lower bound on every game's conditional standard deviation. If uncertainty is unquantified, say so and downgrade evidence; do not invent a width or calibrated probability.
4. For any handicap row ranked in the top two, print **P(favourite wins by more than the line)** as the sum of its separation families from the same margin table, and the exact masses at the sport's key margins (American football 3 and 7; baseball exactly one run, split by whether the home side bats last; rugby league 1–6; ice hockey exactly one goal with the empty-net branch).
5. Evidence (descriptive, learning-only): Rank-#1 underdog cushions `P-345`–`P-423` went **10 W / 13 L at a mean stated 0.61**; Rank-#1 favourite handicaps **7 W / 3 L at 0.57**; log-C printed margin centres missed toward the favourite on **8 of 10** cards (mean +6.1). Prospective test: `C-MARGIN-TAIL-MASS` (`LEARNING_REGISTER.md` §"2026-09-15(b)").




**(i) Fixture identity in sparse competitions.** When fixture sources for the exact match disagree (date, time or opponent) or the club's own schedule is stale, confirm the fixture with the competition/federation or a national broadcaster before issue; otherwise `G0` fails closed. Record every conflicting source. Origin `P-418` (aggregators disagreed on the time; the national broadcaster's round report lists no Drukpa–RTC match). **Correction 2026-09-16:** that broadcaster report (`bbs.bt/244289`) was published 2026-07-17 and does not cover 14 September; RSSSF lists the fixture — see §16.11(p).




**(j) Derivative settlement at the competition's official data record.** `METHOD.md` §7.1 makes the official record the settlement authority. A corner, card or shot row may therefore be research-settled at the competition's own data record when it is reachable, even if the card named only a generic "official match centre" (`P-402`, `P-408`: Premier League data). A data-partner or aggregator display (ESPN, FotMob, Statz, OFStats) that the card did not pre-register stays **provisional**, however many agree (§16.9).




**(k) External mini-log import checks.** Before appending: fingerprint every file and detect byte-identical duplicates; declare unused IDs (`P-372`); merge same-event records (`P-374` ↔ `TMP-SETTLED-20260911-01`); recompute every printed Brier from its probability and result (131 of 131 reproduced for logs A and B); independently re-verify finals at a field owner or structured feed.




### 16.11 Raw-record verification, settlement-route execution, over/under geometry and disruption facts — 2026-09-16




Origin: the 2026-09-16 settlement and learning pass (`PREDICTION_LOG_COMBINED_3.md` §"2026-09-16"; `PREDICTION_LOG_COMBINED_4.md` §"2026-09-16"). **Disclosure, retrieval and process requirements only — no coefficient, no ordinal bar, no fitted probability (`L-087`).** Audited by the §16.8 completeness block.




**(l) `G-L13` — a model-summarised retrieval is not a record.** A number, date, name or score produced by a summarising layer — a search-engine answer, an AI overview, or a fetch tool that returns a model's summary of a page (WebFetch) — must be found in the **raw record** (raw HTML or JSON via `curl`, the raw text returned by `r.jina.ai`, or a structured API field) before it settles a row, retires a handle, dates a piece of evidence or carries direction on a card. Otherwise it is `SUMMARY_ONLY` and treated as unretrieved.
- **Evidence from this pass.** (1) The official Bundesliga stats page for `P-410` was summarised as "corners 7–7, possession 62 %, 12 shots". The page's raw text holds only zero placeholders (it is JavaScript-rendered) and the direct route returns HTTP 403; the summary's numbers were not on the page. (2) A BBS article (`bbs.bt/244138`) was summarised as published 15 September 2026; its raw `Published Time` is **2026-07-12**. (3) The RSSSF Bhutan page summary misreported several score orientations.
- **Recurrence:** `L-20260915-03` recorded two search-summary errors ("132 for 2" v 130/2; "22" v FIBA's 28). Five errors across two passes — this is now a standing retrieval rule.
- **Dates** come from the page's own metadata (`Published Time`, dateline), never from an access date or a summary. See (p).




**(m) `G-L14` — settlement-route execution.** `G10.2` already requires the settling endpoint to be named and confirmed for the competition before ranking. It was listed, not executed, on most derivative rows. From this pass:
1. **At issue**, every corner, card, shot, phase and player row prints `settlement route: <record> — <status>`, with status `VERIFIED_FIELD_OWNER`, `VERIFIED_PREREGISTERED_PARTNER` (for example ESPN `wonCorners` named on the card as the settling provider), `JS_ONLY / BLOCKED`, `NON_COVERAGE` or `UNPROBED`. The league table is `RULES_SOCCER.md` control 35 and `DATA_SOURCE_REGISTER.md` §"2026-09-16". Rows with the last three statuses are capped below Rank #1 (the existing `G10.2` cap). A **self-generated** alternate with any of those statuses is not issued.
2. **At settlement**, `DATA_SOURCE_REGISTER.md` is consulted for the exact field before any row is declared unresolvable. `P-406`'s six-over rows were left "exact checkpoint not recovered" by two passes, although `SRC-ESPN-SITE-API-CRICKET` had exposed `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` for each innings since 2026-09-06. One request settled both rows (Edinburgh 68/2).
3. **Cost of non-execution (descriptive):** 12 corner rows in Part 3 and 8 in Part 2 remain unbooked. Seven of the Part-3 rows are in leagues ESPN covers, but the cards never pre-registered ESPN and the official records are not reachable keylessly.




**(n) `G-L15` — over/under geometry is labelled and reported separately.** Every O/U row is labelled `FORCED_PAIR` (its exact complement on the same target is also ranked) or `FREE`.
1. A forced pair wins exactly once, barring push or void. "At least one O/U won" is never reported for a forced pair; report the **preferred side** (the side with p > 0.5).
2. "At least one O/U wins" is reported only across `FREE` rows or distinct targets, as `Σp` minus overlaps read from the joint table (`G-L10`), or as `JOINT_UNQUANTIFIED` with bounds.
3. When the analyst chooses or generates O/U rows (the user asks for the analyst's own picks, or a self-generated alternate), include at least one `FREE` row whose threshold sits in a low-count tail of its family table: team goals Over 0.5 / Under 1.5, first-half Over 0.5, or team runs Under against the stronger starter. It needs a verified settlement route ((m)) and a probability read from the family masses. This is selection guidance for analyst-chosen rows only; supplied rows are still ranked by marginal probability (`G23.1`).
4. **Evidence (descriptive; `P-345`–`P-423` plus `P-406`'s phase pair settled this pass; booked rows only; complements dependent; selected population; `P-333`–`P-344` use a different table format and are summarised in §"2026-09-09"):**
   - **Forced pairs:** 45. **Preferred side won 27 of 45**:
     - soccer full-match 1 of 6;
     - MLB 7 of 9;
     - NFL 2 of 4;
     - basketball 3 of 6;
     - NPB/KBO/CPBL 3 of 5;
     - rugby league/AFL 2 of 3;
     - cricket full innings/match 2 of 3;
     - Test first innings 0 of 1;
     - cricket phase 4 of 4;
     - soccer first half 3 of 4.
   - **Free rows: 45 of 60** (mean stated 0.68):
     - team totals 18 of 24 — soccer 10 of 10 at mean 0.78; MLB 5 of 8 at 0.69; **NPB/KBO/CPBL 3 of 6 at 0.72**;
     - phase 9 of 11;
     - full-game 11 of 16;
     - corners 4 of 5.




   The prospective test is `C-OU-GEOMETRY` (`LEARNING_REGISTER.md` §"2026-09-16"). §16.9's caution still applies: these are small, selected, mixed-population counts.




**(o) Disruption facts at settlement.** Settlement copies discipline and disruption events from the structured feed (`keyEvents`, scoring plays, match notes): red cards and sin bins with the minute **and the score at that minute**, injury exits, weather or wet-ground stoppages, and overtime. The retrospective states whether each target was already decided before the event. These events are aleatory (`L-117`) — never a pregame "should have known" — but omitting them contaminates the population record. **Origin:** neither canonical settlement recorded them.
- `P-408`: Coventry's Awoniyi was sent off at 53' with Brighton already 2–0 up.
- `P-419`: three red cards (GAIS 59' at 1–0, Djurgården 86', GAIS 90+10').




**(p) Correction to (i)'s origin evidence.** (i) cited "the national broadcaster's round report lists no Drukpa–RTC match". That report (`bbs.bt/244289`) was **published 2026-07-17** and covers the final first-round matches, so it cannot speak to 14 September. RSSSF (last updated 11 September 2026) lists **Round 15, [Sep 14] Drukpa – RTC**, unscored. The fixture therefore appears genuine. Rule (i) still stands on the card's remaining identity defects: kickoff-time conflict (12:00 v 13:00 UTC across aggregators) and a stale club schedule. `P-418` is re-classified `RESULT_NOT_RECOVERED`. The misdating is itself a `G-L13` case (a date taken from somewhere other than the page's metadata).




**(q) `G-L16` — the settling record's period scope must match the contract's.** Before a row is settled from a match-statistics feed, check what interval the feed is reporting (`played_time`, period or phase fields) and compare it with the contract's interval. A whole-match feed cannot settle a 90-minute, regulation-only or phase contract exactly.
1. If the scopes match, settle normally.
2. If the feed's scope is **wider** than the contract's, settle only when the result is invariant across every admissible split, and record it as `PERIOD_SCOPE_BOUNDED` with the bound written out — the count, the excess interval and a sourced upper bound on excess-period events (or the actual split) that excludes every settlement-changing allocation. Merely computing the number needed to flip the row is not a bound.
3. If the row is not invariant, it stays open with the exact missing field named.
4. This also applies at issue: a derivative contract on a knockout fixture that can go to extra time should name the interval (90 minutes, regulation, or the whole match) and a record that exposes it (`G-L14`).




**Origin (2026-09-16).** Two documentary-audit rows were recovered at the UEFA field owner, which reports whole-match totals:
- `P-255-C05` — Inter 12 + Wolfsburg 12 = 24 corners with `played_time` 137 (the tie went to extra time and penalties; UEFA's `regular` score, 2–0, matches the card's 90-minute final). The 90-minute row loses only if 16 or more of the 24 corners fell in extra time.
- `P-256-C05` — PSG 11 + Frankfurt 4 = 15 corners with `played_time` 115. The row loses only if 7 or more fell in extra time.




**Correction 2026-09-17:** the earlier PERIOD_SCOPE_BOUNDED wins are withdrawn. Neither count supplies a lower bound on regulation corners; no evidence excludes the losing splits above. Both rows are UNRESOLVED_PERIOD and their existing audit handles are reopened. A low-plausibility split is still admissible until excluded by evidence. The same check applies to overtime in basketball and ice hockey, extra innings in baseball, and any "regulation" contract settled from a feed that totals the whole game. Full records: [`PREDICTION_LOG_COMBINED_4.md` Appendix A](PREDICTION_LOG_COMBINED_4.md).




### 16.12 Joint-failure mass, allocation marginals, end-state ontology and direct comparables — 2026-09-17




Origin: the `P-424`–`P-437` import (`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"). **Disclosure, retrieval and integrity requirements only — no coefficient, no ordinal bar, no fitted probability (`L-087`).** Audited by the §16.8 completeness block.




**(a) `G-L17` — print the joint *failure* mass of the top two, not only the joint win.** `G-L10` requires `P(R1 ∧ R2)` and a coupling label. That is the probability both rows **win**, which is not the quantity that governs top-two reliability. For any two ranked rows that share a driver, the card must also print: *(Clarified 2026-09-25, R-5 of the 2026-09-22 audit: when the card's joint states are explicit, the failure mass is read off the family table as a number. `JOINT_UNQUANTIFIED` with Fréchet bounds is reserved for dependence the model does not represent. P-483 printed bounds although its own six-branch tree gave about 30%.)*




1. **`P(¬R1 ∧ ¬R2)`** — the mass in which both fail — read from the same joint table, or `JOINT_UNQUANTIFIED` with the Fréchet bounds `max(0, (1−p1) + (1−p2) − 1) ≤ P(¬R1 ∧ ¬R2) ≤ min(1−p1, 1−p2)`;
2. **the single named state that produces it** — one sentence describing the concrete game state in which both rows lose together;
3. where that state is also a named `G22` kill path, the same mass in both places (no double accounting).




**Evidence.** `P-427` is the origin: Kolossos +2.5 and Under 162.5 were declared "mildly positively coupled" with `P(R1 ∧ R2) ≈ 39%`, and both then lost to one state — a Körfez fourth quarter of 25–9 that simultaneously broke the cushion and lifted the game to 170. `P-426` is the same shape across three rows (CAHN +1.5, Under 3.5 and Under 2.5 all needed the low-separation state). Recurrences: `P-397` (Over + underdog cushion), `P-413` and `P-414` (underdog cushion + Under on one "controlled game" thesis). Four cards across three sports — this is a disclosure requirement, **not** a rule against correlated selections: correlated rows may still be the two best rows.




**(b) `G-L18` — allocation marginals for every multi-participant total.** When a match, game or combined total is ranked, print each participant's **own** score marginal from the joint table and the **opponent-contribution branch**: the mass in which the side driving the thesis performs as expected while the opponent does not contribute enough for the total to land. A total may not be ranked above a same-direction single-side row unless that branch has been quantified.




**Evidence.** Three cards in one batch: `P-425` (Daejeon had 17 shots to Kyoto's 1 — the team-total Over won, both match-total Overs lost); `P-430` (the match Over won on Al Ain's four goals while the Rank-#1 Al Nassr scoring row failed — a correct total for the wrong allocation); `P-433` (combined Over 10.5 won with LG supplying nine of eleven runs while the NC team-total Over lost). This escalates `L-037` from a principle to printed arithmetic.




**(c) `G-L19` — build the competition's complete end-state family before any winner label.** Before a winner, "to advance", double-chance or moneyline-equivalent label is issued, enumerate every terminal state the competition's own rules permit, with mass summing to 1: win / loss / **draw or tie where the competition allows one**, plus shoot-out, extra-time, capped-extra-inning, tie-break and abandonment states where applicable. A two-outcome family on a competition that permits a third terminal state is structurally invalid regardless of the probabilities chosen.




**Evidence.** `P-432` issued KT 55% / Hanwha 45%, summing to 100%, in a competition whose regular-season games can end **tied** after the capped extra innings — and the game finished 4–4. The handicap and total rows were unaffected (both won), which is why this surfaced as a labelling defect rather than a scoring one. The competition's own terminal-state rules are a `G0`/`G2` identity field, not a forecasting judgment: confirm them at the league's rulebook or competition regulations, and record the endpoint used.




**(d) `G-L20` — a direct comparable that already cleared the line gets explicit mass.** Where a **current-regime** performance by the same participants, at the same venue or in the same competition, has already produced an outcome on the far side of a supplied line, that comparable is current evidence (`G-L7`). Print it beside the line with its own mass. Assigning above 0.50 to the side the comparable contradicts requires a **named current mechanism** for why it will not repeat — a personnel change, a surface change, a role change — never "it was an outlier".




**Evidence.** `P-431`: the card itself recorded England's **257/3 at the same venue** in July, then placed 55% on Under 193.5 and 62% on a powerplay Under; England made 254/4 with a 90/1 powerplay. This is the cricket mirror of `P-411`, where a same-tournament 83–53 result was set aside as an extreme-shooting outlier and the rematch reproduced the separation (basketball control 25, now generalised here).




### 16.13 Card-level failure mass, forced-pair measurement, result-versus-process separation and the handicap identity — 2026-09-17(b)




Origin: the `P-438`–`P-451` import (`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"). **Disclosure, measurement and integrity requirements only — no coefficient, no ordinal bar, no fitted probability (`L-087`).** Audited by the §16.8 completeness block.




**(a) `G-L21` — card-level shared-driver failure mass, and winner/row evidence coherence.** `G-L17` requires `P(¬R1 ∧ ¬R2)` for the top two. That is not enough when a whole slate rests on one thesis. Three additional requirements:




1. **Three or more rows on one driver.** Whenever three or more ranked rows on a card need the same underlying state, print `P(all of them fail)` from the joint table, or `JOINT_UNQUANTIFIED` with the Fréchet bounds — the lower bound `max(0, Σ(1−pᵢ) − (k−1))` and the upper bound `min(1−pᵢ)` — plus one sentence naming the concrete state. A card whose rows are near-duplicates of one thesis is a **high-variance card in both directions**, and it must say so before the result is known. This is a disclosure, never a prohibition: a correlated slate may still be the best slate.
2. **Direction check on shared drivers.** Before two rows are said to share support, confirm they move the *same* way under the driver. A low-scoring, starter-suppressed game supports an Under **and works against a favourite's run line**; those two rows are negatively coupled on that driver even though both feel like "the favourite controls the game". State the sign, not just the coupling.
3. **Winner label inherits the ranked-row evidence.** When the current-form, platoon or process evidence that produced the top-ranked contract points one way, the winner/1X2 distribution may not point the other way without a named mechanism for the divergence. A protected side and a plurality winner are different objects (that separation is correct and is preserved), but they must be built from the same evidence.




**Evidence.** `P-438`: four of five rows (0.84, 0.83, 0.82, 0.63) all needed "few goals". Under independence P(all four fail) ≈ **0.0018**; under the card's own marginals with perfect positive dependence the bound is **0.16**. The realised state lay somewhere in that two-order-of-magnitude interval and the card never printed which — it produced the worst card in Part 4 (Brier 0.5053). `P-439` is the same slate shape and won every row, which is exactly why this is a disclosure. `P-444`: R1 (Yankees −1.5) and R2 (Under 8.0) were treated as jointly supported by "Rodón suppresses the Twins", when a suppressed low-scoring game *reduces* the chance of a two-run margin; both lost to the single state **close game → tie after nine → automatic-runner extras**. `P-450` and `P-448`: the ranked contract and the winner label were built from opposite readings of the same platoon evidence, and the winner label lost in both.




**(b) `G-L22` — a forced pair is one decision, not two rows.** `G-L15` already requires every over/under row to be labelled `FORCED_PAIR` or `FREE`. This extends the label into measurement:




1. When a card ranks both sides of the same market (`X` and `¬X`), it has made **one** decision — which side, and how far from 0.5 — and that pair contributes **exactly one win and one loss** to any W/L tally regardless of the forecast. Report the **preferred side as the trial**; the complement row keeps its Brier for completeness but is never counted as an independent result.
2. The running scorecard in the active log carries **separate lines for `FREE` rows and for `FORCED_PAIR` decisions**, with their own counts and means. Pooling them biases the aggregate W/L toward 50% and makes the Brier a statement about the supplied line rather than the forecast.
3. **Push mass is part of the decision.** Inflating the push deflates both sides of the pair simultaneously, which lowers Brier on a loss and pushes the whole pair down the rank order against unpaired side rows. State the push mass with its derivation (§16.5(d)); an unsourced push is an unsourced rank.
4. **Covering pairs (added 2026-09-24(f), `G-L22(c)`).** Two rows whose union covers every outcome (e.g., opposite +1.5 cushions in MLB, or ML plus the opponent +1.5) record at least one win by construction. Label them `COVERING_PAIR` and exclude the card's Hit@2 from top-two reliability summaries. See §"2026-09-24(f)"(d).




**Evidence.** All eight MLB cards in the import were issued on `{dog +1.5, fav −1.5, Over L, Under L}` — two forced pairs — and **every one scored exactly 2 W / 2 L by construction**. The headline "16 W / 16 L" says nothing. As decisions the same eight cards went **10 / 16** (run lines 6/8, totals 4/8). Separately, push mass was over-stated on seven of the eight (see `RULES_BASEBALL.md` control 35), which plausibly explains why a side row was ranked #1 on all eight.




**(c) `G-L23` — separate result from process before amending any control.** At settlement, and **before** any control, weight or rule is changed on the strength of an outcome, open the structured process record for the event and record it beside the result:




1. **The process fields for the sport** — shots and shots on target (soccer), inning-by-inning and regulation-versus-final splits (baseball), phase runs and wickets (cricket), quarter scores (basketball) — from the structured feed, not a narrative report.
2. **The disruption facts** already required by §16.11(o) — red cards, sin bins, injury exits, weather stoppages — **with minute and score**.
3. **An explicit classification**: did the card's *process* read fail, or did the process read hold while conversion, an endpoint or a disruption produced the result? A control may not be amended on the second kind without a separate, independent argument.




**Evidence.** `P-438` finished 3–2 against a card that had ranked three Unders. The external retrospective diagnosed "the early-phase centre was too low" and proposed raising early-goal mass. The structured feed says the opposite: **Kuwait SC took two shots in ninety minutes and scored two goals**, Al-Wahda took **41 shots (16 on target, 64.5% possession, 11 corners)**, and **Kuwait's Marhoon was sent off in the 60th minute** — after which Al-Wahda scored the 87th- and 90+7th-minute goals. The card's low-scoring process read was vindicated; the loss came from finishing variance on a two-shot base plus a disruption event. Acting on the narrative diagnosis would have pushed the model to raise early-goal mass in exactly the low-process matches where it is least warranted. The mirror case is in the same import: `P-441`'s Celta took 19 shots and 12 corners and did not score, and every ranked row won — the same process model, working.




**(d) The §16.8 completeness block's failure-mass line is mandatory, not advisory.** Four controls in this import were listed on the card and not executed: §16.11(o) disruption facts (`P-438` settlement), `G-L8` phase distribution (`P-438` issue), `G-L14` settlement-route lookup (`P-445` — the CPL series ID was already in `DATA_SOURCE_REGISTER.md` and was searched for instead), and `G-L17` joint failure mass (`P-438`, `P-444`). This is the `M15` pattern. The completeness block must carry an explicit line for the `G-L17`/`G-L21` failure mass, answered with a number or with `JOINT_UNQUANTIFIED` plus bounds — an unanswered line blocks the card in the same way a missing bench blocks a Rank-#1 margin row.




**(e) `G-L24` — exact signed-margin queries (corrected 2026-09-17).** Define D=specified favourite score minus opponent score, w=P(D>0). For a positive half-integer handicap c, b=P(0<D<c | D>0), so P(favourite −c wins)=w(1−b), P(opponent +c wins)=P(D≤0)+wb. The latter includes draws where the contract does. For positive integer c, favourite win=P(D>c), push=P(D=c), loss=P(D<c); the opposite side reverses W/L and keeps the same push. Quarter-lines retain child settlement categories. If w=0 the conditional b is undefined; use the direct distribution queries. Different sporting margin units, such as cricket runs versus wickets, require separate targets.




Print the conditional band from the same joint model as the winner probability; identify model assumptions versus empirical estimates and their sample/cutoff. BASE_RATES_REGISTER supplies contextual historical frequencies, not universal bounds. A source frequency is itself an uncertain estimate. The previous mandatory pooled-band substitution, BAND_NOT_DERIVED rank-1 prohibition and MLB 0.53 ceiling are withdrawn. A missing conditional model remains a genuine evidence limitation; do not disguise an assumed band as an observed fact. The implied historical bands in P-444/P-446/P-449 merit scrutiny, but falling below a pooled league rate alone is not an arithmetic contradiction.




### 16.14 Consolidated operational object — 2026-09-17




METHOD v4.1 section 4 replaces the repeated mandatory presentation lists in sections 16.3 and 16.8 with six fields, carrying every identity, evidence, distribution, contract, dependence and settlement check once. Old gate IDs remain lookup references. SCORING_AND_VALIDATION governs exact scoring and conditioning, event-level measurement, prospective eligibility and the corrected G-L2/G-L8/G-L12/G-L16 interpretations. No numerical row cap can contradict the printed distribution. A completed JOINT_UNQUANTIFIED field with valid bounds is honest completion; do not invent a joint estimate to satisfy a checklist. Historical worked examples retain their issued values and are not fitted probability guidance.




<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->




## 2026-09-19 deep-research control addendum — source independence and distribution-first forecasting




This addendum is subordinate to current user instructions and aligned to METHOD **MDS-2026.09.19-v4.3** / CONTROLS **CR-2026.09.19-4**. It applies prospectively; historical issued cards remain unchanged evidence.




### Hard source firewall




A predictive fact or feature must not originate from a sportsbook/bookmaker/operator, odds/line-movement or betting-consensus service, betting preview/pick/tip/tout/handicap article, prediction-market signal, fantasy/DFS ranking/projection/ownership/optimizer/start-sit/waiver source, or a secondary article whose analysis merely republishes such material. **RotoWire, RotoGrinders and FPTrack are prohibited predictive sources.** If a material fact is first found there, recover it from a permitted upstream source or mark it unavailable.




### Threshold quarantine




A user-supplied spread, total or alternate line is contract metadata, not sporting evidence. The threshold may be parsed to identify the target but must remain unavailable to forecasting logic until the independent event distribution has been frozen and hashed. It must never set a prior, centre, variance, scenario weight, confidence, calibration target or ranking direction.




### Point-in-time and provenance gates




Every material predictive input records source ID, source class, field, field owner where applicable, upstream lineage, first-known/published time, retrieval time, cutoff, freshness state and a content/snapshot reference. `first_known_at > cutoff_at`, unknown lineage on a material input, stale critical state, or post-result/post-freeze contamination is blocking. Multiple websites on one upstream feed count as one lineage.




### Critical-source sufficiency




For a critical dynamic field (starter/lineup/roster/scratch/toss/goalkeeper/quarterback/venue activation or analogous state), prefer the field owner. If the field owner is unavailable, use at least two genuinely independent, high-quality current lineages or explicitly leave the field unresolved. More derivative copies do not create independence.




### Forecast construction




The normal order is raw sporting evidence -> canonical facts -> prediction-time features -> joint outcome distribution -> distribution freeze -> contract queries. Manual signed score/total adjustments are not promoted simply because they are transparent. A centre-changing effect must be either (a) fitted/estimated under frozen chronological training, or (b) an explicitly labelled **UNVALIDATED_SUBJECTIVE** scenario mixture with uncertainty and no performance claim. Short recent-result sequences do not receive automatic trend/rebound weight.




### Fail closed

Before issue, verify all preflight controls (pregame state, timezone conversion, market-blind source firewall, and minimum 3 independent lineages). Per 2026-09-23 user directive, interactive forecasting workflows verify these controls directly within the card body (and audit via `audit_card_controls.py`) without generating separate scratch JSON manifests; automated pipelines run `prediction_preflight.py` against the machine manifest. Any blocking failure means **NO NORMAL FORECAST** until resolved. Preflight proves control compliance only, not predictive accuracy.




<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## 16.10 Cross-audit canonical rule set — 2026-09-21




These are the all-sports findings that survive the historical audit chain and therefore control whenever older dated prose conflicts:




1. **Identity/time/state first:** exact event, rules population, venue-local date/time/IANA zone, Melbourne conversion and current state are verified before modelling.
2. **Independent lineage:** at least three reliable event lineages; mirrors/syndication count once; snippets/generated summaries are discovery only.
3. **Market quarantine:** user-supplied totals, spreads and alternate lines are frozen contract metadata and cannot shape the sporting distribution before freeze.
4. **Source firewall:** sportsbook/tipster/picks/prediction-market/fantasy/DFS-derived analysis is not predictive evidence.
5. **Point in time:** every predictive fact satisfies `first_known_at <= cutoff_at`; post-event data cannot backfill the issue-time record.
6. **Participants/exposure:** current starters/lineups, bench/reserves, role/workload and material absences are retrieved or explicitly missing.
7. **Disaggregate before direction:** available raw event/participant records control over narrative aggregates for directional mechanisms.
8. **One coherent event object:** totals, lines, cushions, phases and winner are queried from the same sport-native joint distribution/corridor; independent prose probabilities are invalid.
9. **Settlement geometry:** push, void, censoring, extra periods and terminal-state branches are explicit; complementary rows are one correlated decision family, not independent evidence.
10. **Recency is rate evidence, not deviation forecasting:** no automatic rebound, hangover, due, correction-to-mean or continuation lean.
11. **Anti-overfit:** a single result can expose a process bug or open a prospective test, not create a permanent coefficient/ranking override.
12. **Retrospective trigger:** Rank #1 loss and highest-ranked O/U loss or push receive the enhanced failure review.
13. **Terminal verification:** settlement requires three independent reliable terminal-state/result lineages; any credible live-state conflict blocks closure.
14. **No performance-by-documentation:** only frozen chronological out-of-sample plus prospective evidence can support model promotion or predictive-improvement claims.




Explicitly non-operative historical formulations include: “at least one O/U won” as success evidence; universal normalized-edge probability ordering; second-highest/second-lowest values as distribution modes; universal top-slot probability ceilings; `UNORDERED` as an escape from the current unique-ranking requirement; cushion ⇒ underdog-winner shortcuts; winner ⇒ games-handicap shortcuts; guaranteed venue-history availability; bowl-first ⇒ low-scoring; and any one-game rebound/hangover rule.








<!-- ALL-SPORTS-LIVE-GATE-RECONCILIATION-2026-09-21-CR3 -->
## 16.11 Live-gate reconciliation — CR-2026.09.21-3




CR-2 correctly classified several 6 September audit ideas as rejected/superseded, but a verification pass found residual active wording in `G20.2`, `G21.1`, `G26.1`, the `DISJOINT` evidence row and sport-specific instantiations. CR-3 removes that implementation drift.




Current rule: **one sport-native joint outcome distribution/branch mixture first; exact contract queries second.** Historical order-statistic pseudo-tail sums, path-count/category ranking shortcuts, universal 40–60% top-slot bands and blanket `DISJOINT` top-half bans are non-operative. A disjoint relationship is a defect only when it exposes an impossible/incoherent construction; otherwise it is a normal dependence fact. No old prospective candidate built on those shortcuts can control a forecast without a new preregistered design consistent with the current distribution-first method.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## 2026-09-23 — identity-gate pointer: `O-ID-DATE-STARTER-MATCH`

The identity gates (G0–G6) apply to **record merging as well as to issuance**. Two records may be treated as views of one event only when date, venue, home/away and starters/lineups/participants all match. Otherwise they are separate events with separate IDs, and a reforecast of a different date is a new event.

- Origin: P-489 v "R1" (22 v 23 Sep NPB), `PREDICTION_LOG_COMBINED_5.md` §"2026-09-23(c)".
- Procedure: `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-23".
- Integrity control only; no forecasting rule changes.

<!-- PREFLIGHT-WORKFLOW-AMENDMENT-2026-09-23 -->
## 2026-09-23 — preflight workflow amendment: direct card-level verification (user directive)

Per user directive on 2026-09-23, the requirement to generate a separate scratch JSON manifest file (`scratch/preflight_manifest_*.json`) and execute `prediction_preflight.py` is **dropped** for interactive forecasting and game log generation.

1. **Direct card-level verification:** All substantive preflight gates (event identity, pregame state before first action/freeze, IANA timezone and AEST/AEDT conversion, market-blind source firewall, and minimum 3 independent lineages) are verified and documented **directly within the prediction card** (Fields 1, 2, 6, Sources table, and the §16.8 completeness block).
2. **Audit execution:** Card-level compliance is verified directly on the Markdown file via `python audit_card_controls.py <file.md>`, which checks that all mandatory completeness and governance fields are printed.
3. **Machine manifest status:** `FORECAST_PREFLIGHT_MANIFEST.md` and `prediction_preflight.py` remain valid reference specifications for automated or batch-ingestion systems, but are not required for interactive card issuance.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
<!-- AUDIT-2026-09-24F -->
## 2026-09-24(f) — settlement-integrity controls, and withdrawal of the peer "§16.12" cross-sport learnings

**Numbering fix.** The peer import of 2026-09-24 (`cb95acd`) appended a section headed "## 16.12 Cross-sport settlement learnings". The number **§16.12** already belongs to *Joint-failure mass, allocation marginals, end-state ontology and direct comparables* (2026-09-17). The peer section is superseded by this one; its text is preserved in git at `cb95acd`.

**Evidence base.** `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(f)": every final re-verified; the process record checked against field-owner feeds; lineups diffed against official box scores.

**Status.** Every control below is integrity, measurement, retrieval or governance. None is a forecasting coefficient, probability cap or ranking override (§16.10 item 11).

### (a) Withdrawn: the four peer "cross-sport learnings"

| Peer item | Disposition | Why |
|---|---|---|
| 1. "Dual run-line / spread arbitrage (+1.5/+1.5)" | **REJECTED** | Opposite +1.5 cushions jointly cover every MLB outcome. At least one wins every game; both win in a one-run game, 27.6% of 2026 MLB finals (n = 2,374). The P-502 and P-506 "sweeps" are mechanical. "Arbitrage" is price language inside a MARKET_BLIND framework. Ranking both sides to guarantee a winner is the hedging the operator has ruled out. Measurement replacement: (d) below |
| 2. "International qualifier pace volatility" | **REJECTED as a rule** → TESTING `T-BKB-SEASON-OPENER-WIDTH` (`RULES_BASKETBALL.md`) | One game (P-499). Its "89 possessions" was never sourced. The miss traces to roster retrieval (Brno's top scorer was absent from the card) and comparator over-weighting (M13/M17) |
| 3. "End-of-season seeding motivation vs rest" | **OBSERVATION** | One game (P-504). The operative mechanism was an availability fact (Stewart OUT), which G14.2 already requires |
| 4. "Lower-tier clay handicap volatility" | **REJECTED as a rule** → TESTING `T-TEN-LOWTIER-HCP` (`RULES_TENNIS.md`) | One match (P-495). The row was a coin flip (normalised edge 0.09) ranked #1; G23.1, G-L2 and §16.5(d) already cover it |

### (b) `C-PROCESS-RECORD-PROVENANCE` — settlement process facts must be read, not written (extends G-L23, §16.13(c))

1. **Sourcing.** Every process fact printed in a settlement or retrospective names the endpoint or URL it was read from and the retrieval time. Process facts include linescores; quarter, period or set scores; decisions; scorers and goal types; goalies and time on ice; minutes; player stat lines; possessions; weather and wind; and any base rate. One source line per block is enough if it covers every fact in the block.
2. **Unsourced facts.** A fact not read from a record is either omitted or marked `UNSOURCED`. It may not be phrased as observation.
3. **Blocks with unsourced causal facts.** A settlement block whose *causal* narrative relies on unsourced facts is `PROCESS_RECORD_UNVERIFIED`. G23.1, G-L23 and no rule, weight, base rate or learning-register disposition may cite it.
4. **Record IDs.** Printed record IDs (gamePk, NHL game ID, match-centre IDs, URLs) must be the ones actually opened. A lineage whose ID cannot be reproduced does not count toward CR-4.

**Evidence and recurrence.**
- §"2026-09-24(e)": in 14 or more of 17 blocks the field owner contradicts the process facts. Examples: TMP-G25 went 12 innings, not 9; P-503 had no empty-net goal; P-506's Under was lost in regulation; four MLB gamePks and one NHL game ID were wrong. Six rules were derived from those narratives.
- Prior evidence: P-438 (G-L23's origin: a wrong causal diagnosis); L-20260923-08 (AI-generated recaps); the synthetic-match-report trap. The same failure mode is now appearing inside repository sessions.

### (c) `C-LINEUP-DIFF` and S-1 Rev 2 receipt enforcement (amends §16.8 fields 7 and 10; G14.2)

1. **At issue, field 7.** `PROJECTED_BEAT_VERIFIED` is valid only when the card prints the Control S-1 Rev 2 receipt for each side: outlet, reporter, publication timestamp and a verbatim quotation of the lineup or goalie line, corroborated by a second source. Without the receipt the state is `NOT_RETRIEVED`.
2. **Official lineups take precedence.** Where the competition's official lineup or goalie is published before the freeze, a non-official lineup may not be labelled "reported", "confirmed" or `PROJECTED_BEAT_VERIFIED`. The state is then `CONFIRMED_OFFICIAL`, with the fetch time, or `RETRIEVAL_MISS`, and G14.2's Rank-1 block applies to full-game total and margin rows. Official sources include:
   - MLB: statsapi `hydrate=lineups` / `battingOrder`;
   - NPB and KBO: official orders;
   - NBA, WNBA and NBL: official box or preview starters;
   - NHL: official lineup or starting goalie.
3. **At settlement, field 10.** Print the card-listed starters, starting pitcher or goalie beside the official box score.
   - State `k of n named starters started`, per side.
   - If a player the card named as a driver of the Rank-1 row did not play, classify the card `PROCESS_DEFECT: LINEUP_CLAIM_FALSE`, whatever the result.
4. **The completeness audit checks presence, not truth.** A **Y** from `audit_card_controls.py` on field 7 does not satisfy this control. ~~Proposed tooling fix (not implemented; Markdown-only pass)~~ **Implemented 2026-09-25.** Audit field `7r` flags `PROJECTED_BEAT_VERIFIED` without an S-1 Rev 2 receipt; it blocks under `--strict`. From 2026-09-25(b), `receipts.py` prints the official lineup, starting pitcher and goalie diff (§"2026-09-25(b)"(c)).

**Evidence.**
- 2026-09-24(f): personnel claims were false in five of the seven diffable cards (P-500, P-501, P-503, P-508, P-499) and partly wrong in P-504.
- P-501's Rank-1 Over was built on a Baltimore lineup of which 2 of 9 named players started.
- Recurrence: M19 (2026-09-11); L-20260923-06 (NBL wrong roster).
- L-20260924-01 scheduled a settlement audit of S-1 Rev 2; this is that audit.

### (d) `G-L22(c) COVERING_PAIR` — measurement (extends §16.13(b))

1. **Definition.** Two ranked rows whose union covers every settlement outcome are a `COVERING_PAIR`. Examples:
   - A +1.5 and B +1.5 in MLB, where ties are impossible;
   - A ML plus B +1.5;
   - in sports with draws or ties, only if the pair's settlement terms cover them.
2. **What it measures.** The pair records at least one win by construction, and both win exactly in the overlap state (for MLB, a one-run game).
3. **Labelling.** Label the pair on the card (field 5b) and in the settlement.
4. **Top-two summaries.** Exclude the card's Hit@2 from top-two reliability summaries. Report which member was preferred, whether it won, and P(overlap).
5. **Base rate.** MLB 2026 P(one-run game) = 0.276 (n = 2,374). Recorded in `BASE_RATES_REGISTER.md`.
6. **Ranking.** A covering pair may still be the honest ranked output of a supplied slate: G23.1 ranks by probability. What this rule forbids is *counting* it as evidence of skill, or *seeking* it to guarantee a win.

**Evidence.** R1/R2 were covering pairs in TMP-G25, P-500, P-502 and P-506; R1/R3 or R2/R3 in P-493, P-501, P-503 and P-507.

### (e) `C-SUMMARY-FROM-CARD` — summaries are copied, not recalled

Every summary of an issued card is **copied from the issued Field 4 table**: rank, contract, line and probability. This covers status-register rows, learning-register rows, sport-file tables and README lines. Any mismatch between a summary and its card blocks the import commit.

**Evidence.** In `cb95acd`, 13 of 17 status rows and 9 or more summary rows in the learning register and sport files misstated the Rank-1 contract, the line or the winner verdict. Examples: P-498 was summarised as "Rank-1 Lietkabelis −4.5 L; home-dog upset", when the issued Rank 1 was Under 171.5 and it won. P-500's Rank 1 was given as "Under 8.5", when the issued Rank 1 was Nationals +1.5.

### (f) `C-PROMOTION-RECEIPT` — a receipt for §16.10 item 11

Every rule written into a RULES file carries a one-line receipt:
- **status:** `TESTING`, `PROMOTED_PROCESS` or `REFERENCE`;
- **evidence:** the event count;
- **test:** for any rule that changes a probability, centre, width, ordinal or row eligibility, a prospective-test ID with its sample size.

A **predictive** rule supported by one or two events is `TESTING` and non-binding. `PROMOTED_PROCESS` is reserved for integrity, measurement, retrieval and completeness controls, or for predictive rules that have passed their preregistered test.

**Evidence.** Six single-game predictive rules were marked `PROMOTED_PROCESS` in `cb95acd`. One of them, the "derby" rule, had already leaked into the P-509 card's reasoning before settlement.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — research-derived reference checks and retrieval tooling

**Origin.** A research pass run on the operator's instruction of 2026-09-25 ("research what else can be implemented to improve the results"). It derived the base rates and recency magnitudes that the framework had marked `NOT_YET_DERIVED`, and built a receipt tool for the retrieval failures behind M19, M25, M26 and M30. Evidence is in `BASE_RATES_REGISTER.md` §7, `RECENCY_AND_REBOUND.md` §7 and [`research/base_rates_2026-09-25/`](research/base_rates_2026-09-25/README.md).

**Status of every item below.** Each is a **disclosure, measurement or retrieval control** (`C-PROMOTION-RECEIPT`: `PROMOTED_PROCESS` or `REFERENCE`). None changes a probability, centre, width or rank by itself. None is fitted from the log's own results (`L-087`).

### (a) `C-WIDTH-BENCHMARK` — print the reference width beside the card's width (disclosure)

1. **What to print.** Every card that prints a width (SD) for a total or margin also prints the reference width for that competition:
   - the crude-predictor residual SD from `BASE_RATES_REGISTER.md` §7 (§7.1(b), §7.2, §7.3, §7.5);
   - or, for tennis, the raw SD from §7.4;
   - or `REFERENCE_WIDTH_NOT_YET_DERIVED` when the competition has none.
2. **When the card is much narrower.** If the card's width is **below 0.85 × the reference**, the card names the information the crude predictor lacks that justifies narrowing. Examples: confirmed lineups and rotation, a pace or possession model, both starting pitchers, a same-day weather reading. Without a stated reason, the audit flags `WIDTH_BELOW_REFERENCE_UNEXPLAINED`.
3. **Why 0.85.** Adding opponent defence improved basketball RMSE by 7–11% (`RECENCY_AND_REBOUND.md` §7.2), so a card that knows more than the crude model can legitimately be about 10% narrower. 0.85 marks where the claim of extra knowledge must be written down. It is a disclosure trigger, not an estimate and not a floor.
4. **What it is not.** It does not widen anything automatically and has no rank effect.
5. **Evidence.**
   - In the 2026-09-24 cohort, basketball total widths ran about 39% too narrow: mean z² 1.93, n = 7 (`BASE_RATES_REGISTER.md` §7.6).
   - Both LKL cards used total widths of 12.1–12.9, below every derived benchmark (15.9–19.5).
   - Audit field `WB`: advisory; blocks under `--strict`.

### (b) `C-WIDTH-Z` — standardised miss at settlement (measurement)

1. **What to print.** Every settled card that printed a centre and width prints z = (actual − centre) / width for the total and for the margin.
2. **How it is used.** The values accrue in the `C-WIDTH-Z` manifest (`LEARNING_REGISTER.md` §"2026-09-25(b)"), by sport family. The decision rule is preregistered there. Until it fires, z is a record only.
3. **Audit field:** `10z` (advisory; blocks under `--strict`).

### (c) `C-RECEIPT-TOOL` — `receipts.py` (retrieval; implements the receipt format of 2026-09-24(f)(b)–(c) and the MLB gamefeed-weather rule)

**Commands.**
- **`python receipts.py pregame mlb <gamePk>`**, at freeze. Prints:
  - probable pitchers;
  - gamefeed weather, or `WEATHER_NOT_YET_PUBLISHED`;
  - the official batting orders, or `LINEUPS_NOT_YET_PUBLISHED`;
  - umpires;
  - the feed state (`PREGAME` / `LIVE` / `FINAL` / `START_CROSSED_STATUS_NOT_FINAL`), with UTC and AEST times.
- **`python receipts.py pregame espn <sport/league> <eventId>`** prints the state and the ESPN injury list. An empty list is labelled as **not** a confirmation of availability.
- **`python receipts.py settle {mlb|nhl|espn} …`** prints:
  - the final and the period, inning or quarter lines;
  - the regulation score where extras or overtime were played;
  - decisions, scorers, empty-net goals, goalies' time on ice, starters and minutes, and DNPs;
  - every fact with its endpoint and retrieval time.
- **`--card-away/--card-home/--card-sp-*/--card-goalie-*`** add the `C-LINEUP-DIFF` line (k of n started; `DID NOT PLAY` / `MISMATCH`).

**Rules for using it.**
1. **Where the tool covers the lane** (MLB statsapi; NHL api-web; ESPN summary for NBA, WNBA, NBL, NHL, soccer and others), its output is the preferred receipt at freeze and at settlement.
2. **A hand-written process record** must carry the same fields and endpoints. Otherwise it is `PROCESS_RECORD_UNVERIFIED` under (b) of 2026-09-24(f).
3. **Lineage count.** The tool is **one lineage**. It does not satisfy C-FINAL3's three independent terminal lineages on its own.
4. **Market-blind by construction.** ESPN `pickcenter`, `odds`, `againstTheSpread` and `winprobability` keys are deleted on load; the NHL `oddsPartners` key is never read.
5. **Tested.** `test_receipts.py` has 17 offline tests on fixtures of games already settled in Part 5 (P-500, P-503, P-504, P-506).

**Evidence.** It reproduces two retrieval failures from the settled record:
- P-503: the "confirmed" Oettinger did not play; Poirier played 59:29.
- P-500: gamefeed wind "14 mph, In From LF", where the card said out.

These are the failures the 2026-09-24(f) audit traced to hand retrieval.

### (d) Early-season and regime-shift references (disclosure; specialises M24 and field BR)

1. **Early-season windows.** A card in a derived early-season window prints that reference beside its total centre:
   - **NBL:** games where both teams have played fewer than 3 games ran **−8.5 points** (−14.3, −2.7), three seasons, n = 38.
   - **WNBA:** the same window ran **+6.5** (+0.4, +12.6), n = 57.
   - The signs are opposite, so **no cross-league early-season rule exists**. Other leagues are `NOT_YET_DERIVED`.
2. **Documented regime shifts.** A card that averages across a documented regime shift says how the pre-shift seasons were handled. Currently documented: WNBA 2026 at +10.7 points per game over 2024–25, n = 327 v 530.
3. **NHL preseason.** A preseason card uses the preseason reference (2025: 5.68 goals, n = 104; 2026 to date: 5.33, n = 36), not the regular-season 6.25.

### (e) `R-1` corollary — a one-game comparator never outweighs the season rate (reference)

In **six of six** competitions measured (MLB, NBA, WNBA, NBL, NHL, EPL), the last-game predictor is the worst tested. It is 18–40% worse than the league constant (`RECENCY_AND_REBOUND.md` §4, §7.2).

- A card may cite a single recent game only as a mechanism pointer: a new starter, a lineup change, a tactical change.
- Its numeric weight may not exceed the season rate's.
- This extends `R-1` and `G-L20` (direct comparables), and is consistent with M17 and M27.

### (f) Tennis games-handicap coherence — `C-HCP-COHERENCE` (disclosure; `RULES_TENNIS.md` §"2026-09-25(b)")

1. **What to print.** A games-handicap row −k.5 prints P(win), the implied P(margin ≥ k+1 | win), and the population conditional from `BASE_RATES_REGISTER.md` §7.4:
   - WTA best of 3, k = 5: straight-sets win **0.663**; deciding-set win **0.168**.
2. **When the implied conditional exceeds the straight-sets reference,** the card names the hold and break evidence for it. Otherwise it is flagged `HCP_CONDITIONAL_ABOVE_REFERENCE`.
3. **Status.** This is the measurement lane for the existing `T-TEN-LOWTIER-HCP` test. Origin: P-495, where the implied 0.70 exceeded the straight-sets reference 0.663 and the row lost.

<!-- REPO-HYGIENE-CI-2026-09-25C -->
## 2026-09-25(c) — current-rules summary, baseline skill check and repository controls

**Origin.** The repository review of 2026-09-25 rated the project 5/10. The method was rated strong, but four weaknesses were found:
- 95% of tracked files were `node_modules`;
- the rules were too large to follow;
- there was no CI and no branch discipline (the `cb95acd` invented process record reached `main` unchecked);
- there was no evidence of skill beyond a coin-flip comparison.

The operator then asked for every improvement to be implemented. Every item below is a documentation, measurement, retrieval or repository control (`C-PROMOTION-RECEIPT`: `PROMOTED_PROCESS`). None moves a probability, centre, width or rank.

### (a) `CURRENT_RULES.md` — step 0 of the reading gate (§1)

`CURRENT_RULES.md` is the one-page live summary: non-negotiables, workflow, card fields mapped to audit IDs, rules by topic, sport quick cards, M1–M31, tools, file map and withdrawn rules.

- **It is derived.** Every rule cites its source section, and where they disagree the source governs (`METHOD.md` §9). The disagreement is then a documentation defect, fixed in the same pass.
- **Keep it in step.** Any pass that adds, changes or withdraws a live rule updates `CURRENT_RULES.md` in the same edit.
- **It does not relax the reading gate.** §1's full read remains the standing user directive.
- **History has moved.** The README's dated history moved verbatim to `CHANGELOG.md`, and the README is now an overview and quickstart.

### (b) `C-BASELINE-SKILL` — every row carries a naive population baseline

1. **At issue.** From `CONTROL_MANIFEST_2026-09-25-3.md` onward, every ranked row prints `BASELINE_P`. This is the naive population probability of the same contract, taken from `BASE_RATES_REGISTER.md` §7 or its re-runnable query and restricted to games completed before the event. It knows only the league's outcome rates and which side is at home; for tennis it knows no side at all. Competitions without a population print `BASELINE_P: NOT_YET_DERIVED`.
2. **At settlement.** Append the decision row to `SKILL_BASELINE_LEDGER.md` (a forced pair once) and run `python tools/skill_baseline.py`.
3. **Why.** Comparison with a coin flip (0.25) credits the card with information any population table has. The seed comparison (2026-09-24 cohort, 29 decisions from 9 cards, hindsight-selected with pre-event data only) gave card Brier **0.2461** against baseline **0.2360**, a 95% card-cluster interval of [−0.059, +0.089]. That is **no demonstrated skill over the baseline**: totals trailed, moneylines trailed, handicaps led.
4. **Decision rule** (`LEARNING_REGISTER.md` §"2026-09-25(c)"). After 100 prospective decisions from at least 30 cards, report whether the interval lies below, spans or lies above 0. Nothing is claimed before then, and nothing is fitted from it (`L-087`).
5. **Audit field `BP`** (advisory; blocks under `--strict`).

### (c) Repository controls (`C-REPO-CI`, `C-BRANCH-PR`)

1. **CI** (`.github/workflows/checks.yml`) runs on every push and pull request:
   - all unit tests;
   - `tools/repo_hygiene.py`, which fails on tracked `node_modules`, `.pyc`, `.codex_spreadsheet_tmp`, local settings, oversized non-log files, control characters and literal-`\n` artefacts;
   - `tools/verify_manifest.py`, which fails if a governance file changed without a new manifest;
   - the strict card audit of the active mini logs (`--allow-empty`).
2. **Manifest tooling.** Manifests are generated with `tools/make_manifest.py` and verified with `tools/verify_manifest.py`. Hashes are taken in CRLF form, and `.gitattributes` forces CRLF checkout on every platform, so a manifest verifies anywhere.
3. **Branches.** Sessions work on `session/<date>-<topic>` branches and merge by pull request once the checks pass (`CONTRIBUTING.md`). Commit messages follow `type(scope): what changed`. Branch protection on GitHub is an owner action; the command is in `CONTRIBUTING.md`.
4. **Hygiene.** `.gitignore` excludes dependency trees, build output, machine-local settings, research caches and raw API pulls. `LICENSE` states the rights position.

**Evidence.**
- 16,142 of 17,045 tracked files were `node_modules` or build artefacts before this pass.
- Two literal-`\n` rendering bugs were found by the new hygiene check (the README custody table; this file's header).
- The CRLF/LF manifest fragility was found while committing 47e7748.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — full settled-row review: calibration findings, construction algorithm, and tools

**Origin.** On 2026-09-25 the operator asked for every completed and settled log to be checked for what could improve the probabilistic models, algorithms and learnings. Every graded row in Parts 1–5 was extracted into one dataset: 1,185 rows from 307 cards; 600 rows from 149 cards carry an issued probability. The extraction reproduces the logs' own cohort figures. Evidence is in [`research/settled_rows_2026-09-25/README.md`](research/settled_rows_2026-09-25/README.md).

**Status.** Every figure is hindsight on the framework's own selected cards, and descriptive. Nothing below is a fitted shrink, weight or cap (`L-087`). Each control is a disclosure, measurement or construction discipline with a prospective test (`C-PROMOTION-RECEIPT`).

### (a) What the record shows

1. **Overall calibration is good; skill is modest.** Brier 0.2249. Murphy reliability 0.002, resolution 0.019. Logistic slope 1.06 (SE 0.16). **No global shrink is warranted.** `C-PROB-EXTREMITY` is not supported on its prospective subset (79 of 100 rows: 91.1% won against a stated 79.3%).
2. **Skill lives at p ≥ 0.65.**

   | Decisions | n (cards) | Won | Mean stated |
   |---|---|---:|---:|
   | p 0.50–0.65 | 235 (132) | **53.6%** | 0.574 |
   | p ≥ 0.65 | 152 (68) | **80.3%** | 0.744 |

3. **Non-baseball underdog cushions (+k.5) are over-confident:** 17/40 won at a stated **0.642**, gap −0.217, card-cluster 95% interval [−0.353, −0.073]. Baseball +1.5 rows are calibrated: 27/45 at 0.613.
4. **Sports with no demonstrated skill:**
   - tennis: 8/16 at 0.60, Brier 0.281;
   - NFL/NCAA: 3/12 at 0.544, over-confident;
   - AFL: 3/10 at 0.662, over-confident;
   - MLB and basketball: near-zero resolution (0.0075 and 0.012).

   **Soccer** carries the clearest skill: 107/143 at 0.70, Brier 0.170.
5. **Rank slots below #1 are indistinguishable:** #1 66.4%; #2–#4 54–56% (1,179 rows).
6. **Top-two joint failure equals independence on average:** 14.4% observed against 14.5% (264 cards).
7. **Phase totals beat full-game totals in the same card:** 30/36 against 27/41 (34 cards).

### (b) `C-PLUS-CUSHION` — disclosure for non-baseball +k.5 rows (CANDIDATE control)

**Scope.** Any +k.5 handicap row outside baseball (basketball, NFL, AFL, rugby, soccer, tennis, hockey).

**What the card prints:**
1. The population margin band for the line (`BASE_RATES_REGISTER.md` §7, or `NOT_YET_DERIVED`) and `BASELINE_P`.
2. The decomposition P(cover) = P(underdog wins outright) + P(underdog loses by ≤ k), from the card's own margin distribution (`tools/card_math.py cover`, with `--no-zero` where a tie is impossible).
3. The named reason the underdog stays within k: pace, the favourite's missing personnel, garbage-time structure, or similar.

**Rules.**
- Stated above 0.60 without item 3, the row's evidence grade is capped at LOW and the row is labelled `PLUS_CUSHION_UNSUPPORTED`. This is an evidence label, not a probability cap.
- Audit field `PC` (advisory; blocks under `--strict`).
- **Why a CANDIDATE control, not TESTING:** the error has recurred across three independent readings: G-L12's origin (10 W / 13 L), `C-UNDERDOG-SEPARATION` (basketball), and now the full record (17/40). Its interval excludes zero. It still moves no probability. The prospective test is `T-PLUS-CUSHION` (`LEARNING_REGISTER.md` §"2026-09-25(d)").

### (c) `C-DEPARTURE-LEDGER` — baseline-anchored construction (construction discipline)

1. **The prior is the population.** Each ranked row starts from `BASELINE_P` (C-BASELINE-SKILL).
2. **Every departure is itemised.** The card states its final probability's log-odds departure from `BASELINE_P` and attributes it to named mechanisms, each with a signed share: pace, lineup, weather, starters, surface, and so on. `python tools/card_math.py departure --p … --baseline … --mech "name:share" …` computes it.
3. **Unattributed departure is flagged.** A departure more than 10% of which is unattributed is `UNEXPLAINED_DEPARTURE`: a process defect, and an evidence-grade cap at LOW.
4. **Where no population exists** (`BASELINE_P: NOT_YET_DERIVED`), the card prints `C-DEPARTURE-LEDGER: n/a`.
5. **Why.** Resolution is near zero exactly where the cards departed most from population rates without named evidence: MLB, basketball, tennis, NFL, AFL. The seed baseline check found the cards no better than the population (`SKILL_BASELINE_LEDGER.md`). Forcing every departure to be named is the construction-side answer. The measurement side is `C-BASELINE-SKILL`.
6. **Audit field `DL`** (advisory; blocks under `--strict`).

### (d) `C-TRACK-RECORD` — print the framework's own record beside the probability (disclosure)

Each card prints one row for its sport (and family where n ≥ 10) from `python tools/calibration_report.py`: decisions, win rate, mean stated p and Brier.

- Where that record is **over-confident** (the interval below 0), the card is labelled `NO_DEMONSTRATED_SKILL`. As of 2026-09-25(d): NFL/NCAA, AFL, and non-baseball +k.5 cushions. Tennis is also labelled, on Brier above 0.25.
- The label caps the evidence grade at LOW and requires the departure ledger. It never changes the number (`L-087`).

### (e) `C-LOW-RESOLUTION-BAND` — honest language for 0.50–0.65 rows (disclosure)

Rows stated between 0.50 and 0.65 are labelled `LOW_RESOLUTION`, and the card's delivery text calls them near-coin-flips. Historically they won 53.6% against a stated 0.574. It extends G23.1's `NEAR_TIED` language from normalised edge to the band. It changes no rank or number. Its prospective check is in `LEARNING_REGISTER.md` §"2026-09-25(d)".

### (f) Reporting and tooling

1. **The 25-card review standard** (`SCORING_AND_VALIDATION.md` §14): run `python tools/calibration_report.py`, which gives the reliability table, Murphy decomposition, logistic slope, and card-cluster intervals by family, sport, direction and rank. Report probabilities and the baseline difference, **not rank-slot records below #1**.
2. **`tools/card_math.py`** is the reference implementation of distribution-to-contract queries: normal with continuity correction, negative binomial, Poisson, Skellam, a `no_zero` option for margins, push mass, exact same-variable joints, and the departure ledger. It reproduces the issued P-509 and P-500 probabilities within 0.015. It is the M14/G-L8 check.
3. **Canonical settlement table** (`EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-25(d)"): `| Rank | Contract | Family | p | BASELINE_P | Result | Brier |`. The dataset is rebuilt with `python research/settled_rows_2026-09-25/extract_settled_rows.py`.
4. **Joint failure (G-L17).** Without a named shared driver, P(¬R1 ∧ ¬R2) should sit near P(¬R1) × P(¬R2). A card that states a much larger joint failure names the driver. Historically the product has held (14.4% against 14.5%).

<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2: the ranking model (RM-1), the team baseline (TB-1), oval-sport references and settlement integrity

**Origin.** On 2026-09-25 the user asked for a comprehensive review, sport by sport, of the information sources and of the reasoning applied to them, against the log results, the sport rules and the general framework. The aim is **to make Rank 1 and Rank 2 far more likely to win than lose.** Every point was to be implemented, including a new probabilistic model or calibration if one was needed or could be built.

**Evidence.**
- [`research/rank_model_2026-09-25e/README.md`](research/rank_model_2026-09-25e/README.md) (RM-1, with out-of-sample validation);
- [`research/team_baseline_2026-09-25e/README.md`](research/team_baseline_2026-09-25e/README.md) (TB-1, the NFL/AFL/NRL references and the cushion base rates);
- [`research/settled_rows_2026-09-25/README.md`](research/settled_rows_2026-09-25/README.md) §"2026-09-25(e) rebuild".

**Status.**
- `C-RANK-MODEL` and `C-TEAM-BASELINE` are **operative**. RM-1 is a **user-authorised exception to `L-087`** (item (h)).
- Every other item is a disclosure, a construction rule or a settlement-integrity control.
- All records remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

### (a) What the evidence says about Rank 1 and Rank 2

1. **The slot does not win; the probability does.**
   - Held out, Rank-1 rows with a calibrated probability q ≥ 0.70 won **73–81%**. Every tier below 0.70 won **53–62%**.
   - Stated p says the same: rows stated at 0.70 or more won 83%; rows at 0.50–0.65 won 54%.
   - **"Far more likely to win than lose" is available only when the slate contains a row the evidence supports at about 0.70 or more.**
   - What the process can do: rank by the best-calibrated probability; stop overstating weak rows; choose the right side of each pair; say plainly when no STRONG row exists; and show which contracts on the same event would be STRONG (item (c)).
2. **The stated probabilities are informative but predictably mis-stated.**
   - On decision rows, logit(q) ≈ −0.19 + 1.54·logit(p): rows stated at 0.55 won about 53%, and rows at 0.75 about 82%.
   - Underdog cushions (+k.5) outside baseball, hockey and soccer won **7 of 27** at a stated ~0.58.
   - A richer model with per-sport slopes and per-class offsets does **not** generalise (RM-1X; its ridge weight went to the maximum).
   - The 2026-09-25(d) all-rows slope of 1.06 is not a contradiction. Including forced complements symmetrises the fit. On the decision side, the middle is over-stated and the top under-stated.
3. **Why the cushions fail: the population fact.**
   - In basketball, NFL, NRL and AFL, a small cushion on the weaker team covers well under half the time: basketball +1.5 to +3.5 32–45%; NFL +1.5 to +3.5 34–54%; NRL +1.5/+2.5 41–49%; AFL +6.5 38–43%.
   - The cushion adds only P(the underdog loses by ≤ k), which is small: basketball P(\|margin\| ≤ 2) is 7–12%.
   - Cards priced these rows like a baseball +1.5, whose base rate is 0.638 because 27.6% of MLB games are one-run games (M32).
4. **Where a team-strength model has resolution and the cards do not.**
   - A two-number, leak-free team baseline (TB-1) beats the population rate on sides by 5–19% in Brier: NBA, WNBA, NBL, NFL, AFL, NRL, EPL.
   - It beats it on totals in the NBA, WNBA and (marginally) the NFL.
   - It adds nothing in MLB or the NHL. There, cards anchor on the population rate, with starters and lineups as named departures.
5. **The data were partly wrong.** The settled-row extractor was reading narrative columns ("Lobos lost by 1; +2.5 covers") as results. **17 rows were graded the wrong way round** in the 2026-09-25(d) dataset, and 55 more were dropped. The dataset is rebuilt: 1,264 graded rows, 641 with a stated probability.
6. **The P-510–P-515 settlement block was written, not read** (item (f)).

### (b) `C-RANK-MODEL` — rank by RM-1's calibrated probability (OPERATIVE)

**What the card prints.** Field 4 prints, for every ranked row:
- the card's own stated p, unchanged and still derived from the card's distribution;
- the RM-1 q, tier and flags from `python tools/rank_model.py rank --sport <league> --row "<contract>=<p>" …` (rows in stated order);
- the `TOP2_QUALITY` line the tool prints.

**Ordering.**
- **Ranks are ordered by q.** Stated p breaks ties within 0.005.
- If the q order differs from the p order, the card prints both orders, and the q order is the issued rank.

**`SIDE_FLIP`** (q crosses 0.5 by at least 0.05 against the stated side).
- The flipped side is ranked by its q, labelled `SIDE_FLIP`, and its tier is capped at SUPPORTED.
- The card writes one line reconciling it with its own distribution.
- **Override (`RM1_OVERRIDE`)** is allowed only where the league's `TEAM_BASELINE_P` has resolution (item (d)) **and** gives the stated side ≥ 0.55. The population model then says the mechanism behind the flip is absent.
- A narrative reason alone is never an override. The stated cushion rows were exactly the ones whose narrative reasons failed.

**`NEAR_TIED_FLIP`** (a flip within 0.05 of 0.5): the row keeps its stated side and is labelled a coin flip. Held out, such flips won 27/57.

**Scoring.** Both p and q are scored at settlement (Brier and log loss), and settlement tables gain a `q` column (`T-RM1-PROSPECTIVE`).

**Refit.** Only at the 25-card review, with the three commands in the RM-1 README, then a new control manifest.

**Audit field `RM`.** It is strict-blocking for cards frozen under `CONTROL_MANIFEST_2026-09-25-5` or later.

### (c) `C-TOP2-QUALITY` — say what the top two are worth, and what on this event would be stronger (disclosure)

1. **The TOP2_QUALITY line.** Every card prints it, from `tools/rank_model.py`:
   - `TOP2_STRONG`: both rows at q ≥ 0.70;
   - `TOP2_SUPPORTED`: both at ≥ 0.62;
   - `TOP1_ONLY`: R1 at ≥ 0.62, R2 below;
   - `TOP2_COIN_FLIP`: R1 below 0.62.

   The line also gives P(both win) and P(both lose) under independence (G-L17 holds on average: 14.4% against 14.5%).
2. **Plain language for a coin-flip top two.** Under `TOP2_COIN_FLIP`, the delivery text says in plain words that the top two are near coin flips. It never uses "lean", "supported" or "confident".
3. **`SLATE_ADVISORY`** (optional; printed whenever TOP2 is not STRONG).
   - Up to two contracts on the same event that the card's **own frozen distribution** prices at q ≥ 0.70. For example: a phase total, a team total, a wider cushion, a double chance, or a total line further from the centre, read with `tools/card_math.py`.
   - It is labelled `SLATE_ADVISORY — not ranked, not scored, not a recommendation to bet; market-blind, so a higher probability carries no claim of value`.
   - It is printed after the freeze and never changes a ranked row.
   - Why: the record shows the STRONG tier is where Rank 1 wins about four times in five, and the slate decides whether that tier is available. Phase totals won 30/36 against full totals' 27/41 on the same cards.

### (d) `C-TEAM-BASELINE` — TB-1 as the anchor where it has resolution (OPERATIVE)

1. **What the card prints.** For NBA, WNBA, NBL, NFL, AFL, NRL and EPL (and optionally MLB and NHL), `TEAM_BASELINE_P` for every ranked row goes beside `BASELINE_P`, from `python tools/team_baseline.py predict --league … --home … --away … --date <venue-local date> --total … --home-line …`.
   - Its flags are printed with it: `TB1_EARLY_SEASON`, and `TB1_NO_RESOLUTION:<target>`.
   - With too few games, the card prints `TEAM_BASELINE_P: NOT_YET_DERIVED`.
2. **The departure ledger's anchor** (`C-DEPARTURE-LEDGER`) is `TEAM_BASELINE_P` for every target where TB-1 has resolution, and `BASELINE_P` otherwise.

   | TB-1 has resolution | Leagues |
   |---|---|
   | Sides and margins | NBA, WNBA, NBL, NFL, AFL, NRL, EPL |
   | Totals | NBA, WNBA, NFL |

3. **A departure larger than 0.10 in probability** from the anchor names a row-specific, receipted mechanism: a confirmed absence, a starter, rest or travel, a rule or format difference, or weather. Otherwise the row is `UNEXPLAINED_DEPARTURE`, with the evidence grade capped at LOW.
4. **Where no tool covers the league** (FIBA, LKL, BCL, EuroLeague, KBO/NPB/CPBL, cricket, tennis, most soccer leagues), the card prints `TEAM_BASELINE_P: NOT_COVERED`, and `BASELINE_P` stays the anchor.
5. **Audit field `TB`.** It is strict-blocking for covered leagues from `CONTROL_MANIFEST_2026-09-25-5`.

### (e) `C-PLUS-CUSHION` amended — the population cover rate is the cushion's baseline (CANDIDATE → construction rule)

1. **The baseline.** For a non-baseball +k.5 row, `BASELINE_P` is the population cover rate of that side at +k.5 (`BASE_RATES_REGISTER.md` §7.7(c)):
   - the TB-1 underdog's rate if the side is the TB-1 underdog;
   - otherwise `TEAM_BASELINE_P`.
2. **The rule.** A cushion stated more than 0.05 above that baseline needs, in the departure ledger, a named mechanism that is receipted **on the favourite's side**: a confirmed absence, rest or a lineup change.
   - Otherwise it is `PLUS_CUSHION_UNSUPPORTED`, and `C-RANK-MODEL`'s flip stands.
   - "The underdog keeps it close" is not a mechanism.
3. **The rest of `C-PLUS-CUSHION` (2026-09-25(d)(b)) is unchanged:** the margin band, the decomposition P(dog wins) + P(dog loses by ≤ k), and the named reason.

### (f) `C-SETTLEMENT-FROM-FEED` — a settlement block is read, never written (OPERATIVE settlement-integrity control)

**What happened.**
- The P-510–P-515 settlement was generated by a script (`scratch/build_full_settlement.py`; archived 2026-09-26 at `archive/scratch_2026-09-25/`) whose settlement narratives were **typed-in strings**.
- The finals of five of the six games were right: checked on 2026-09-25 against MLB statsapi, the NPB official page, the KBO official scoreboard and ESPN.
- **P-515's score was wrong:** 36–14 against the true **36–20** (ESPN event 604843: half-time 16–6, full time 36–20). Grades are unchanged.
- **The P-510 and P-511 lineup diffs listed players who did not play.**
  - P-510: Contreras, Arenado, Nootbaar and Siani for St. Louis; Bart, Tellez and Hayes for Pittsburgh.
  - P-511: Schanuel, O'Hoppe, Rendon, Polanco and others.
  - They were compared with the official statsapi boxscores.
- The retrospective's "facts" (329 run metres, 14 errors, a 16–6 half-time "then" 36–14) were unsourced.

**The rules.**
1. **Settlement process facts** come from `receipts.py settle …` output, or from an endpoint response fetched in the same session and pasted with its URL and retrieval time. The linescore, lineup diff, scorers, stats and times all qualify.
2. **A script may assemble** a settlement block from fetched data. It may never contain the narrative or the numbers as literals.
3. **The audit's new field `10n`** (strict-blocking at settlement) checks that the lineup diff names players who appear on the issued card.
4. **The P-510–P-515 process records are `PROCESS_RECORD_UNVERIFIED`.** Their grades stand, because five finals were independently confirmed and P-515's corrected score leaves every grade unchanged. Their causal retrospectives may not be cited. M26 recurrence: P-510, P-511 and P-515.

### (g) Rule candidates from the P-510–P-515 mini log — dispositions

| Candidate | Disposition | Why |
|---|---|---|
| `C-ABSENCE-DEFENSIVE-PENALTY` (absences raise totals) | **REJECTED as a rule; hypothesis only** | Two games (M27). Mechanism asserted, not measured. The item (d) TB-1 anchor and G-L2 (uncertainty widens; it does not lean) already cover the construction |
| `C-KBO-PITCHER-VELOCITY-FILTER` | **REJECTED** | One game. No velocity data were retrieved (the claim was unsourced) |
| `C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR` | **REJECTED** | One game, built partly on an invented statistic (329 m) and a wrong score |
| `C-FINALS-BYE-RUST` | **TESTING, non-binding** (`T-NRL-BYE-RUST`) | A real, measurable question (finals after a bye, first-half margin). Needs a field-owner sample, not one game |
| "Ace starting pitcher dominance" | **Not a rule** | Two low totals. The existing starter adjustment is the channel |
| Source notes (NPB official, KBO official, ESPN NBL, NRL match centre) | **Verified in part; recorded in `SOURCES.md` §"2026-09-25(e)"** | NPB official and KBO English scoreboards were verified on 2026-09-25. The "NRL match centre" statistics were not |

### (h) The `L-087` exception for RM-1, and its safeguards

`L-087` forbids coefficients fitted from the log's own results. The user's instruction of 2026-09-25 authorises a calibration model. RM-1 is admitted **only** under these conditions:
1. **Pooled, pre-specified terms.** A term is admitted only if it beats the current RM-1 on log loss in every forward split at a 25-card review.
2. **Refits happen only at the 25-card review,** never after a single game or card.
3. **Stated p is printed unchanged beside q.** q never overwrites the distribution.
4. **Both p and q are scored.** If q's Brier is worse than p's over the next 25 settled cards (`T-RM1-PROSPECTIVE`), `C-RANK-MODEL` reverts to disclosure-only until the next review.
5. **Flips are capped at SUPPORTED.**

`L-087` continues to govern everything else. No single-game coefficient, cap or override is admitted anywhere.

### (i) What changes, sport by sport

The detail is in each sport file's §"2026-09-25(e)".

| Sport | Source change | Reasoning change |
|---|---|---|
| MLB | Settlement lineup diff from the statsapi boxscore `battingOrder` (never typed) | TB-1 has no resolution: anchor on the population rate. +1.5 rows sit near their 0.638 base; the first-choice R1 is whichever row's calibrated q is highest, not a +1.5 by habit |
| NPB / KBO / CPBL | NPB official score page and KBO English scoreboard verified for terminal state | RM-1 and the population anchor. Unders' 11/14 stays TESTING |
| Basketball | ESPN team-schedule lane for TB-1 | TB-1 anchor. Small cushions at their population rate (32–45%); a flip is expected unless the favourite's absence is receipted |
| Soccer | ESPN team schedule, EPL | Unchanged: the best record. Phase, team-total and double-chance rows remain the STRONG-tier source |
| NFL / AFL / NRL | ESPN scoreboards (`football/nfl`, `australian-football/afl`, `rugby-league/3`); NRL scoreboard fallback | First population references and TB-1. Cushions at population rate; the worst R1/R2 record (12 W / 20 L) is the main target of RM-1's flip |
| NHL | Unchanged | TB-1 has no resolution; population anchor |
| Tennis | Unchanged (Elo benchmark blocking) | RM-1 cushion term covers games handicaps (+k.5): 1/4 won |
| Cricket | Unchanged | RM-1 global recalibration only |


<!-- REVIEW-IMPLEMENTATION-2026-09-26 -->
## 2026-09-26 — review implementation: reading gate, rule freeze, event universe, closing-line benchmark, MLB shadow model and evidence status

**Origin.** The 2026-09-26 repository review (rated 6.5/10) found strong honesty and tooling, but **no demonstrated skill over a simple baseline**, a method changing faster than evidence arrives (six control revisions on 2026-09-25 and no card issued under the current rules), a self-selected event sample, no market benchmark, an unbuilt MLB model and a rule set too large to execute. The user instructed that every recommendation be implemented. **Nothing here is a fitted coefficient, cap or ranking override** (`L-087`). The controls below are process, measurement and documentation controls; the MLB model is a shadow lane that never touches a card.

### (a) `C-READING-GATE` (OPERATIVE, documentation) — the two-tier gate in §1

Every sport file now opens with a §0 live rules page (560–1,650 words, against 6,800–18,700 for the full files). `CURRENT_RULES.md` plus that page is the Tier-1 read. Maintenance: **a control added to a sport file is added to its §0 page in the same pass**, or the change is incomplete (the `C-PROMOTION-RECEIPT` discipline applied to the summary).

### (b) `C-RULE-FREEZE` (OPERATIVE, governance) — no new predictive rules until the evidence gates report

1. **In force until** `C-BASELINE-SKILL` reaches its checkpoint (100 prospective decisions from at least 30 cards) **and** `T-RM1-PROSPECTIVE` reaches its checkpoint (25 settled RM-1 cards). It lifts at the next scheduled 25-card review after both. `python tools/evidence_status.py` reports the state.
2. **While it is in force, a governance change may be only:** a validity repair (identity, contract, arithmetic, source, settlement, leakage: `LEARNING_REGISTER.md` §5 item 6); a retrieval or integrity control; a measurement or disclosure control that moves no probability, rank, width or centre; or documentation. **Not allowed:** a new predictive rule, coefficient, cap, ranking override, width multiplier or direction tilt, from any source, including a user-authorised exception like RM-1, **unless the user explicitly instructs that specific change after being shown the evidence-status table**.
3. **One control manifest per issuing day,** except for a validity repair. `tools/make_manifest.py` now requires `--category` (INTEGRITY, MEASUREMENT, DOCUMENTATION, VALIDITY_REPAIR or MODEL_CHANGE). `MODEL_CHANGE` also needs `--model-change` and `--freeze-override "<the user's instruction>"` while the freeze is in force.
4. **Ideas keep flowing into tests, not rules.** A retrospective may still open a TESTING row. It may not create a binding rule.

### (c) `C-EVENT-UNIVERSE` (OPERATIVE, measurement) — declare the population before the cards

1. Before the first card of an issuing day, run `python tools/slate_universe.py declare --date <venue-local date> --league <key> …` for the leagues to be carded. It writes `universe/UNIVERSE_<date>.json` with a SHA-256 of the declaration: every not-yet-started event on the official schedule, or a seeded random sample (`--max-per-league N --seed S`) declared before any event is researched.
2. Every in-scope event gets a card, or a `skip` record with a reason (`STARTED_BEFORE_FREEZE`, `POSTPONED`, `CANCELLED`, `GATE_FAIL:<gate>`, `SOURCE_UNAVAILABLE`, `OPERATOR_CAPACITY`, `OTHER:<text>`). `status` reports CARDED, SKIPPED or MISSING against the logs; the declaration cannot be edited afterwards without the hash failing.
3. Each card prints `UNIVERSE: <file> / <event id>`, or `OUT_OF_UNIVERSE` for an operator request outside it. Out-of-universe cards are still issued and settled; scorecards report the two groups separately.
4. **Test `T-UNIVERSE-VS-SELECTED`** (TESTING): after 30 settled cards in each group, compare calibration and Brier against `BASELINE_P`, with card-cluster intervals. This is the first executable form of `C-NT-ALL-UNIVERSE`.

### (d) `C-MARKET-BENCHMARK` (OPERATIVE, measurement; scoring-only) — the closing line, after settlement

1. **The forecasting firewall is unchanged.** Before and during forecasting nothing in `METHOD.md` §1.1 changes: no price, line movement, tipster or market-derived text may be read, and agents never fetch betting sites for any purpose.
2. **After settlement only,** the operator records the closing market's no-vig probability for each settled decision in `MARKET_BENCHMARK_LEDGER.md` (`Entered (UTC)` later than `Settled (UTC)`; only the probability and de-vig method are stored, never raw odds). `python tools/market_benchmark.py devig` converts, and `report` scores card − market with a card-cluster interval.
3. The ledger is outside the reading gate. No rule, rank, width, retrospective or disposition may cite it. It is not a value, ROI or performance claim.
4. **Decision rule** (preregistered): after 100 decisions from at least 30 cards, report "beats", "no demonstrated difference from", or "is less calibrated than" the closing market, with the interval. The last is the expected result and is recorded plainly.

### (e) `C-MLB-SHADOW` (OPERATIVE, measurement; the numerical programme's S6 lane)

1. `tools/mlb_model.py` implements the MLB A0/A1 pilot (`NUMERICAL_PROGRAM.md` §2; `MODEL_IMPLEMENTATION_RECIPES.md` §1, §5): leak-free league A0; A1 with pooled team offence and prevention, park, home, and a starter term; the shared-environment Gamma-Poisson joint; route A reduced-form final scores. **Every constant is a declared input, not a fitted value.**
2. **Order of operations:** freeze the MLB card first; then, before first pitch, run `python tools/mlb_model.py shadow --gamepk <pk> --total <line> --card P-###`. The tool refuses a started game and never replaces a frozen row. The shadow output is **never shown on, cited by or used to revise a card.**
3. At settlement, `settle` appends the finals and `score` reports A1 against A0. `validate --season <year>` runs the leak-free rolling-origin comparison of A0 and team-only A1 where statsapi is reachable. **Update 2026-09-26(c):** the team-only core was validated on Retrosheet game logs (2022–2024; `research/sport_models_2026-09-26/README.md`). v1 (20 prior games per team) was overconfident and no better than A0. v2 (120, selected on 2022 alone) beat A0 on results and totals on 2023–2024 and tied TB-1 on results. That test is not independent, so the 2025 season (`validate --season 2025`) and this lane are the real tests.
4. **Review at 150 settled shadow games** (a review point, not proof). A proposal to use the model as an MLB anchor needs: A1 − A0 below 0 with its day-block interval below 0; A1 better than the cards' own p on the shared games; and an explicit user instruction (as for RM-1).

### (f) Evidence status at every session start and every review

Run `python tools/evidence_status.py`. It prints `C-BASELINE-SKILL`, `T-RM1-PROSPECTIVE`, `C-MARKET-BENCHMARK`, `C-EVENT-UNIVERSE`, `C-MLB-SHADOW`, `C-SPORT-SHADOW` (added (k)) and `C-RULE-FREEZE` in one table. Every 25-card review prints that table first.

### (g) RM-1 — evidence caveats and a stricter reversion rule (validity, not a new weight)

The review re-ran `research/rank_model_2026-09-25e/validate_rank_model.py` and reproduced its output byte for byte. It also found three limits the headline figures do not show:
1. **The cushion term was found on the same record it was validated on.** It was observed in P-345–P-423 and confirmed by the 2026-09-25(d) review of rows through P-509, so the forward splits from P-420, P-450 and P-480 score data that helped discover it.
2. **Only the leave-one-card-out figure excludes zero** (+0.068 per card, [+0.007, +0.128]). The forward-split re-ranking intervals are [0.00, +0.15], [0.00, +0.26], [−0.08, +0.32] and [−0.05, +0.35]; 4–8 top-two choices change per split.
3. **The cushion effect is era-dependent.** Top-two cushions won 17/28 (61%) in the ordinal era and 7/24 (29%) in the probability era.

**Amendment to `T-RM1-PROSPECTIVE`:** in addition to the existing Brier(q) against Brier(p) rule, report non-baseball cushion-class rows separately. If, over at least 15 prospective cushion-class rows, their win rate exceeds their mean q by more than 0.15, the cushion term reverts to disclosure-only until the next review. RM-1 is described everywhere as **promising and unproven** until `T-RM1-PROSPECTIVE` reports.

### (h) Documentation corrections

- The rebuilt 2026-09-25(e) dataset gives **Brier 0.2268, calibration slope 1.01 and skill +6.6%** over the base rate (the README quoted the earlier (d) figures, 0.2249 / 1.06 / +7.7%). No conclusion changes.
- Soccer's record is the **strongest resolution** of any sport (37 cards). Its card-cluster calibration interval spans 0, so it is "the strongest evidence", not "proof of skill".
- RM-1 and TB-1 are fitted calibration and baseline layers. H0 remains unbuilt. The shadow models (MLB, and every other sport from (k)) are implemented code with declared priors, validated only where public results could be reached.
- `LEARNING_REGISTER.md`'s header now names the live method (v4.3) and the M1–M32 registry.

### (i) The untested candidate backlog is closed

The 59 historical `C-P*` candidates and the 21 early process tests (`T-001`–`T-014`, `T-P057`, `T-P058`, `T-P059`, `T-P240`, `T-P245`, `T-P247`, `T-P275`) sat at zero or near-zero prospective counts. None had a v2 manifest, and most predate the distribution-first rebuild. They are **CLOSED_UNTESTED** (`LEARNING_REGISTER.md` §"2026-09-26"). Their observations stay as provenance. Any of them may be re-registered under a new ID with a v2 manifest. The open tests are the ones `CURRENT_RULES.md` §D9 lists.

### (j) Repository

The unreferenced `drive_settlement_2026-09-21/` folder and the Drive-sync manifests moved into `archive/`. The former `scratch/` folder is archived at `archive/scratch_2026-09-25/`, and `scratch/` is now ignored. The retired runtime's 319 byte-identical input copies were removed, with `archive/DEDUP_INDEX_2026-09-26.md` naming each identical kept file. `tools/repo_hygiene.py` now fails on byte-identical duplicates outside the historical folders.

### (k) `C-SPORT-SHADOW` — a numerical model for every sport (2026-09-26(c); OPERATIVE, measurement)

The user asked for the numerical model to cover every sport, not only MLB.

1. **What exists.** `tools/sport_models.py` implements reduced-feature A0/A1 builds (`MODEL_IMPLEMENTATION_RECIPES.md` §4, "a separately labelled reduced-feature build") for:
   - soccer: Poisson ratings with linked halves;
   - ice hockey: regulation Poisson plus OT/SO resolution;
   - basketball, American football, AFL, rugby league and rugby union: ridge ratings, a discretised normal with the league's own key-number weights, and widths from out-of-sample residuals;
   - baseball outside MLB: the MLB joint with the competition's tie rate;
   - tennis: surface-blended Elo, then a serve/return chain with a match-level gap effect;
   - cricket: Elo, plus a ridge first-innings model.

   Adapters are in `tools/sport_data.py`: ESPN, CSV, TML-Database and cricsheet. Nothing reads odds or lines as inputs.
2. **Order of operations.** This is the same as `C-MLB-SHADOW`. Freeze the card first. Then, before the start, run `python tools/sport_models.py shadow --league <key> --event <ESPN id> --date <date> --card P-### --total … --line …`. Tennis adds `--surface` and `--best-of`, and takes the ESPN competition ID. Cricket adds `--espn-path cricket/<league id> --cricsheet <history>`; its first-innings line is priced before the toss, 50/50 on who bats first. The command is **blind**: it prints the row ID only, and the probabilities are read at review, never while building cards. At settlement, run `settle` (from the same ESPN feed, never typed) and `score`. The output is **never shown on, cited by or used to revise a card.**
3. **Validation (`research/sport_models_2026-09-26/README.md`).** Rolling origin on the public results that could be reached, with priors committed before the first run:
   - **Soccer (five leagues), NFL, AFL, NBA, WNBA and NHL** (the last three in the second pass, 2026-09-26(d)): A1 beat A0 on results and margins in every league. It beat TB-1 on results in the EPL, AFL, NBA, WNBA and NHL; in the NFL it was ahead but the interval crossed 0.
   - **Totals:** A1 gained in basketball (NBA and WNBA, also over TB-1), La Liga, the Bundesliga at the line, and MLB after v2. It was level elsewhere. It was **worse in the NHL** (total RPS +0.008, and +0.002 against TB-1 at the line). At the AFL total line TB-1 was ahead by 0.008, but the interval crosses 0.
   - **MLB, tennis and cricket:** each failed at v1 and was re-selected on an earlier TUNE window (v2, disclosed as not independent). IPL cricket v2 is only level with a coin flip on results and with the format mean on totals.
   - **Not validated:** NBL, NCAAF, NRL, rugby union, WTA, the Asian baseball leagues, cricket outside the IPL and the soccer competitions beyond the five top leagues.
4. **Review at 150 settled rows per league** (a review point, not proof). The rule is the same as (e): A1 − A0 below 0 with its interval below 0, A1 better than the cards' p on shared rows, and an explicit user instruction. Replacing TB-1 as the printed team baseline in a league where A1 beat it is a `MODEL_CHANGE` under `C-RULE-FREEZE`. It is a user decision, not an agent one.

### (l) Shadow lanes for every sport, and the settlement record (2026-09-26(d); measurement)

1. **Tennis and cricket lanes.** These are no longer `predict`-only. `sport_models.py shadow` reads the ESPN tennis scoreboard (competition ID, pregame state and start) and the ESPN cricket scoreboard. `settle` reads the same feed.
   - **Tennis:** a retirement settles the winner row only, and the games rows are void. A walkover voids every row.
   - **Cricket:** the first-innings total is scored only when the innings is known to be full-length. That means it was all out; or its overs are shown and complete with no DLS or reduced-overs note; or its overs are not shown but the chase batted the full scheduled overs with no such note. Otherwise the row is `FIRST_INNINGS_UNSCORED`. A tie settles on ESPN's super-over winner; an undecided tie or a no-result is void.
   - **Soccer:** after extra time or penalties, soccer settles on the 90-minute score when ESPN gives the period scores; otherwise the row is void. One unfindable event never blocks the others (`UNSETTLED <row>`). Old scoreboards are refetched unless every event was already final.
2. **Blind output.** `sport_models.py shadow` and `mlb_model.py shadow` now print only the row ID. The probabilities go to the CSV and are read only at review. The operator building the next card does not see them. This blindness is procedural: `predict` still prints probabilities, and it is research only, never used while building or revising a card. A game's side result is scored once, however many lines were frozen for it.
3. **Settlement record, audit field `10s`** (strict-blocking for cards frozen under `CONTROL_MANIFEST_2026-09-26.md` or later). Every settlement prints one of:
   - `SHADOW: <row id>` (the lane's row);
   - `SHADOW: NO_LANE <reason>` (for example, a league with no ESPN path);
   - `SHADOW: MISSED <reason>`.

   A lane that is not recorded is M15, "control listed, not executed".
4. **Second-pass validation** (see (k) point 3 and `research/sport_models_2026-09-26/README.md`) used public results for NHL, NBA 2023–26, WNBA and IPL cricket. No constant changed for NHL or basketball. Cricket's two constants were re-selected (v2) after v1 lost to a coin flip.


<!-- PREDICTABILITY-2026-09-26E -->
## 2026-09-26(e) — predictability across sports: what the models and the cards can do (measurement; no rule moves a probability)

**Origin.** On 2026-09-26 the user asked for predictability across all sports to be improved "properly".

**Evidence.**
- [`research/predictability_2026-09-26/README.md`](research/predictability_2026-09-26/README.md).
- P1–P4 were preregistered in `PREREGISTRATION.md`, committed in `cc447c9` before any run. P5 and the P3 disagreement split are exploratory.

**Category.** MEASUREMENT, plus validity repairs (TB-1 flags for NRL sides and NFL totals) and a documentation correction. **`C-RULE-FREEZE` is respected:**
- no probability, rank, width, centre or card construction rule changes;
- no model constant changes.

### (a) What the evidence shows

1. **Predictability differs enormously by sport** (P5; `BASE_RATES_REGISTER.md` §7.8). This is the share of games in which the validated model's favourite reaches 0.70 (the STRONG tier), with the win rate there:

   | League | STRONG share | Won |
   |---|---:|---:|
   | AFL | 39% | 90.6% |
   | Basketball (NBA, WNBA, NBL) | 26–29% | 80–84% |
   | NFL | 27% | 73.1% (the 0.70–0.80 band is over-confident) |
   | NRL | 19% | 68.3% (the same band is over-confident) |
   | NHL | 6% | 72.9% |
   | EPL three-way | 6% | small n |
   | **MLB** | **0%** (90% of games at 0.50–0.60) | — |

   Totals rarely reach 0.70 at a sensible line in any league.
2. **The team models add information over the population.** On sides in soccer's top five leagues, the NFL, AFL, NBA, WNBA, NBL (2025-26), the NHL (small) and MLB (small), and on totals mainly in basketball.
3. **They are not better than the cards on the cards' own contracts** (P3). On 98 contracts from 54 settled cards:

   | Source | Brier |
   |---|---:|
   | Card | 0.2438 |
   | A1 | 0.2505 |
   | Population | 0.2680 |

   Card − A1 is −0.007 [−0.025, +0.011]. A 50/50 blend was no better than the card. So **anchoring the cards on the models is not supported by the evidence** and is not proposed.
4. **MLB's declared starter term did not add skill on results** (P1, preregistered verdict: not demonstrated). It helped the 2026 totals only.
5. **NBL and NRL.**
   - NBL results beat the population and TB-1 in 2025-26, but not significantly in 2024-25.
   - NRL results were not significant, for A1 or for TB-1.

### (b) `C-MODEL-ANCHOR` — the reference registry (OPERATIVE as MEASUREMENT; not a card input)

1. **The registry.** `python tools/model_anchor.py registry` derives, per league and target, the reference model: A1S (MLB totals), A1, TB-1 or POP (the population). The rule preregistered as P4 is applied mechanically to held-out evidence stored in the tool:
   - the first model that beat the population with a 95% interval below 0;
   - A1 over TB-1 only if it also beat TB-1.
2. **Its uses:**
   - the reference model for each league's shadow-lane review (`C-SPORT-SHADOW`, `C-MLB-SHADOW`);
   - the source of the predictability map.
3. **It is never printed on, cited by or used to revise a card** (status `REFERENCE`).
4. **Changing that is a `MODEL_CHANGE`** that needs the user's explicit instruction under `C-RULE-FREEZE`. After P3, the case for it has to come from the shadow-lane review (150 rows per league, with the model beating the cards on shared rows), not from population validation alone.

### (c) `C-PREDICTABILITY-MAP` — say which contracts can be STRONG (disclosure)

1. **What the card prints.** Beside the track-record row, the card prints its league's §7.8 row: the share of STRONG favourites and their win rate, or `NOT_YET_DERIVED`.
   - Under `TOP2_COIN_FLIP` in a league whose map shows few or no STRONG favourites (MLB, NHL, soccer three-way results, most totals), the delivery text says the slate cannot produce a STRONG Rank 1, not only that this card did not.
2. **`SLATE_ADVISORY`** (optional, unchanged in kind) may name the league's STRONG-capable targets from the map:
   - AFL and basketball sides;
   - NFL sides with the over-confidence caveat;
   - soccer phase, team-total and double-chance rows from the cards' own record.

   It moves no probability or rank.
3. **`C-EVENT-UNIVERSE` declarations** may use the map to choose which leagues to card, before any event is researched. Choosing leagues by predictability is declared, never event-by-event after research.

### (d) Validity repairs

1. **NRL sides no longer anchor on TB-1.**
   - TB-1's 2026 NRL side gain has a 95% interval of [−0.0294, +0.0044]; the "resolution" flag had rested on a point estimate.
   - `tools/team_baseline.py` now prints `TB1_NO_RESOLUTION:margin` for the NRL, and NRL sides anchor on `BASELINE_P` (`RULES_NRL_RUGBY.md` §0.2; `CURRENT_RULES.md`).
   - §"2026-09-25(e)"(d) and `BASE_RATES_REGISTER.md` §7.7(d) are corrected by §7.8, not rewritten.
2. **NFL totals no longer anchor on TB-1.** The same standard was applied to every flag:
   - **NFL totals fail it.** The 2025 total gain has an interval of [−0.0184, +0.0017], and over 2021–2025 TB-1 was 0.2403 v 0.2423 over 1,359 games. `team_baseline.py` prints `TB1_NO_RESOLUTION:total` for the NFL (`RULES_AMERICAN_FOOTBALL.md` §0.2; `CURRENT_RULES.md`).
   - **NBA totals keep their flag.** Their single-season interval crosses 0, but 2023–26 gives 0.2129 v 0.2308 over 3,689 games.
3. **`tools/mlb_model.py`'s claim is corrected.** It said historical probable starters "cannot be reconstructed leak-free". They can: statsapi keeps `probablePitcher` on completed games, and pitcher game logs give every prior appearance. The starter term has now been tested on two seasons.

### (e) Candidates for the next preregistered model version (TESTING; nothing applied)

These are recorded so they are tested prospectively or on untouched seasons, **not** fitted to the data that revealed them:
- NFL and NRL over-confidence in the 0.70–0.80 favourite band (opened as `T-FAV70-BAND`: 100 band games per league not yet played on 2026-09-27; `LEARNING_REGISTER.md` §"2026-09-26(e)");
- NHL totals worse than the population;
- the MLB starter term's season-to-season inconsistency;
- NBL's mixed seasons.

### (f) What this means for Rank 1 and Rank 2

The route to "far more likely to win than lose" is a STRONG row that actually exists. By league:
- **Often:** AFL and basketball sides; NFL sides at a slightly lower hit rate.
- **Sometimes:** NRL and NHL.
- **Almost never:** MLB and most totals. Soccer's STRONG rows are in phase, team-total and double-chance markets.

The cards' own probabilities are about as informative as the models' on the contracts they priced. So the gain available now is **in which contracts are carded and in honest labelling**, not in replacing the card's judgement with the model's.

### (g) The user's bar for a model change (2026-09-27): none meets it

**The instruction.** On 2026-09-27 the user said: "do a model change if its absolutely going to make it better only". The bar was stated before testing: a 95% interval below 0 in every independent window, on data that did not suggest the change.

**Every candidate fails:**
- **Anchoring the cards on A1:** card − A1 −0.007 [−0.025, +0.011] (P3).
- **A 50/50 blend:** no better than the card (P3).
- **MLB's starter term:** not demonstrated (P1).
- **Shrinking the model's 0.70–0.80 favourites** (C1, preregistered in `1bc57d7`):
  - The NFL over-confidence replicated on 2021–24: 66.7% won at 0.744, [−0.147, −0.010].
  - The NRL's reversed in 2025: 82.8% won at 0.747.
  - Even an NFL-only shrink did not improve Brier in either test season.

**So no `MODEL_CHANGE` is made.** The freeze stays in force. `T-FAV70-BAND` remains open prospectively. The NFL band finding is disclosed in `RULES_AMERICAN_FOOTBALL.md` §0: a model favourite at 0.70–0.80 has won about two in three.

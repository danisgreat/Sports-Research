# League evidence collection, storage and model development

Owner-requested framework, 17 October 2026. This document specifies future work; it does not ingest, fit, launch jobs, promote models or authorise writes to the shared learning store. The NBA evidence snapshot in `2026-10-17-nba/` is a separate collection task. Apply CURRENT_STATE, CURRENT_RULES, HISTORICAL_SOURCE_PROTOCOL, LEARNING_PIPELINE_PROTOCOL and FORECAST_CYCLE_PROTOCOL at the time a new task is invoked. Existing issued records and retired stores are not rewritten or restored.

## 1. Declare one league population before downloading

Create a collection specification with: competition identifier; sport/format/gender/age; season naming; first and last scheduled UTC instant; source roles and coverage; stable provider IDs; exact outcome endpoint; season-type and stage taxonomy; periods/innings and scoring-rule eras; required statistics/units; planned first-fit population; raw capture location; and allowed writes. Record the expected fixture denominator independently of successful downloads. Unknown or incomplete coverage is not COMPLETE.

The default evidence destination is `research/verified_history/<snapshot-date>-<league>/`. Create it when real collection begins. Do not generate empty season trees. Collect the declared whole population, including cancelled, postponed, live and scheduled events; only independently corroborated finals can become future label candidates. Do not select only favourable cards or games with convenient box scores. Stable event identity is separate from canonical prediction-card P-IDs, which this process never allocates.

## 2. Capture sources, then project sporting facts

Use the organiser's permitted result/box source and a separately published check where accessible. When only two providers are usable, identify the chosen primary as a provider, not a league field owner. Record upstream independence as UNKNOWN unless established; two publishers need not mean two independent measurements. Recheck source access and field coverage every run. A blocked route is a recorded failure, not a reason to use proxies or evade access controls. A missing field requires alternative permitted sources and an explicit remaining requirement.

Keep every raw response outside the repository, including unsuccessful responses and market-bearing feeds. Each attempt records exact URL, UTC retrieval time, HTTP result/error, byte length, SHA-256, external capture path and parser version/hash. `known_at` is retrieval unless earlier public availability is supported by actual evidence. Extract only approved sporting fields; do not commit odds, articles, tips, fantasy, win-probability widgets, JSON dumps or raw HTML. Audit captures without importing their unrelated contents into the learning data.

## 3. Store linked evidence tables

| Table | Grain and required content |
|---|---|
| OWNER_RESULTS / INDEPENDENT_RESULTS / supplementary source results | One game per source: provider namespace/native ID, league ID if actually published, season/stage, scheduled UTC start, teams, venue, neutral status, source-reported status, final and regulation scores, period count, provenance |
| EVENT_ALIASES | One supported native-ID mapping: primary provider ID, league ID and other-provider ID, exact matchup/date evidence, mapping disposition; never guessed IDs |
| PERIOD_SCORES | One observed game/team/period/source; distinguish regulation, overtime, extra innings, target-score and abandoned segments; do not invent missing periods |
| TEAM_GAME_STATS | Existing long-format export schema in `ml/research_ingest.py`: competition, native_event_id, team, stat, value, source_url, source_kind, published_at, retrieved_at, known_at, capture_path, capture_sha256, review_status, collected_by |
| AVAILABILITY | Separate event/team/player/role/status/confirmation observations with publication evidence; a postgame participant is not a confirmed pregame starter |
| RECONCILIATION / FIELD_COMPARISONS | Every source pairing and field comparison, score/identity/status/clock discrepancies, exact source references, dispositions and reasons |
| QUARANTINE / REQUIREMENT_CLOSURE | Conflicting or incomplete facts, owner/reviewer, exact next field/source/action, last attempt, clock basis and OPEN/CLOSED status; no automatic closure |
| COVERAGE / QUALITY_CHECKS / FILE_HASHES | Expected and observed populations, uniqueness, field missingness by season/stage/source, equations, exclusions, capture checks, output byte counts and hashes |

Partition large long-format tables by season/source without changing their columns. Repeated source observations are not repeated training games. Keep observed source values; a reviewed correction is a new observation/revision with a parent and evidence. Provider rates without supporting attempts remain labelled provider statistics. Persist sufficient counts to reproduce model features later; collecting a column does not make the current model consume it.

## 4. League-specific collection contracts

The sources below are discovery candidates to be opened and tested in each future task, not claims that a new collection has been performed. Endpoint and adapter admission must be checked against the then-current runtime.

| League family | Required sporting components beyond identity/results | Population and endpoint controls | Candidate source routes |
|---|---|---|---|
| NBA, WNBA, NBL, EuroLeague and other basketball | FGM/FGA, 3PM/3PA, FTM/FTA, ORB, TOV, team scores, periods; other box counts; separately dated availability | Separate competition/gender/rules; regulation versus final inclusive of OT; regular season first, other stages held out; derive possessions only from sourced counts | League game centres, ESPN, Basketball-Reference where covered; verify each league's coverage |
| EPL, La Liga, Bundesliga, Serie A, Ligue 1 and other soccer | Regulation goals/halves, shots, shots on target, cards; provider-defined xG/npxG if consistent | League/cup and 90-minute versus extra-time/shootout distinct; corners/props need separate admitted models; do not treat shootout kicks as goals | League/federation match reports and an independent structured provider listed in SOURCES |
| MLB, NPB, KBO | Runs by inning, final, innings completed, pitcher identity, bullpen usage, batting counts, park | Separate leagues/rule eras, regulation versus extras, shortened/forfeit/suspended games; exact pitcher confirmation timing | League schedule/gamebook and ESPN where supported; local-language owner/provider routes for NPB/KBO |
| NHL and other hockey | Regulation period goals, final, OT/SO decision, shots, penalties/special-team counts, dated goalie confirmation | League/season rules, regulation tie versus final winner; shootout awarded score handling explicit | League game centre/API plus ESPN or another verified provider |
| NFL, NCAA FBS, CFL | Period points, passing/rushing plays and yards, turnovers, scoring events; EPA numerator/definition/version where available | Separate competitions and OT rule eras; final endpoint and key-number/tail checks; no assumed transfer of NFL coefficients | League/college gamebooks and a separately published structured score/box provider |
| AFL, AFLW, state football | Goals, behinds, total points, periods, disposals, clearances, inside 50s, scoring shots | Separate competitions/gender and rule eras; finals/draw/extra-time handling, venues and rest | AFL/competition game centre, AFL Tables where covered, corroborating game report |
| NRL, Super League | Tries, conversions, penalties/field goals, metres, completion attempts/successes, tackles | League-specific golden-point rules and ordinary-time versus final scores; representative games separate | NRL/competition match centre and independently published box/result |
| Rugby union competitions | Tries, conversions, penalty/drop goals, periods, possession/territory definitions, set-piece attempts/successes | Separate Super Rugby/Top 14/Premiership/internationals and scoring rules; extra time separate | Competition/federation match reports and a structured check |
| T20, ODI and other limited-overs cricket | Innings runs/wickets, legal balls, scheduled/revised overs, toss/selection timing, target, DLS/reduction, result method | Separate format, competition and innings; full-length first-innings ladder only where admitted; no-result, shortened games and super overs separate; Tests unsupported by analogy | Official scorecard plus ESPNcricinfo or another permitted independently published scorecard |
| ATP, WTA and other tennis | Sets/games, surface, best-of format, serve/return points and attempts, tie-break rules, retirement/walkover | Separate tours/formats/rule eras; completed matches versus retirement and market action; experimental tennis lane remains separate | Official tour/tournament result and permitted structured check |

Do not derive a regular-season fit from preseason, play-in, playoffs, cup championships or exhibitions merely because they share teams. Fit separate competitions first; pooling requires held-out evidence and a declared hierarchical specification. The current code's supported model family is an implementation limit, not proof of calibration or support for every listed statistic/contract.

## 5. Freeze and verify an evidence release

Before publication, re-read every authored output and validate: unique source/event keys; complete fixture dispositions; source hashes; native-ID aliases without collisions; home/away orientation; timezone conversion; finals versus non-finals; scoring/period and box arithmetic; stage/era exclusions; missing versus zero; and every source disagreement. Scores that disagree remain quarantined. Missing official IDs remain blank with a requirement; never synthesize an NBA-style number from row order. Mark exact fields with one-source coverage rather than calling the whole game exhaustively corroborated.

An evidence release contains a window/source/read-time README, transformation/provenance rules, schema and coverage tables, disagreement and requirement counts, quality checks and hashes. Completeness claims name their scope. A good hash proves capture identity, not sporting truth. Publish only intended paths, preserve unrelated edits, and verify the fresh remote SHA and committed bytes. Raw files/helpers/notebooks stay external under current repository rules. Rerunning an unchanged projection should reproduce identical fact tables; real later retrievals create a new snapshot/revision.

## 6. Separate future label use from historical feature availability

A box collected today is usable for a forecast made later. Its retrieval timestamp cannot be changed to an old match date to make an earlier feature row pass admission. The current `ml/features.py` uses only history/stats known at the requested horizon. Thus this new backfill alone does not create historical pregame feature snapshots for a 2020 versus 2021 challenger experiment. Later corrections and retrospective lineups must not leak into earlier predictions.

The next authorised training task must choose and record one of these honest paths:

1. **Strict point-in-time evaluation:** obtain demonstrably dated historical publications/snapshots; retain retrieval time separately; exclude unresolved availability. Use only those supported features at each old forecast horizon. This is still retrospective evaluation, not prospective publication.
2. **Explicit historical reconstruction study:** under a separately authorised implementation, construct lagged past-game features under a declared post-final availability assumption, preserve the true current `known_at`, and label all results HISTORICAL_RECONSTRUCTION_NOT_PREGAME_VERIFIED. No target-game statistics or future-season aggregates enter features. This requires its own release/feature specification; the present strict training builder cannot be made to accept it by falsifying timestamps.
3. **Forward collection:** freeze real pregame input snapshots and forecasts from now on, settle them later, and accumulate prospective evidence. Older verified results may support future no-context score fitting without becoming invented historical context or expert feedback.

## 7. Authorised ingestion and training, as a later task

First select one row per corroborated final from the declared training population and quarantine any unsettled conflict. Build exact-schema research exports from the evidence snapshot; ensure NBA stage filtering occurs before the shared-store ingest because the present game export has no dedicated season-type/stage column. Keep the evidence-side stage-to-selection manifest. **Do not feed the whole NBA evidence folder directly to ingest.**

Dry-run against an isolated store copy; check expected event/stat/alias and quarantine counts, repeat with zero additions, and compare protected shared-store hashes. Only the later expressly authorised prompt-4/8 task may append to `research/learning_store/`. Ingest has receipts/revisions; an interrupted ingest is not a release. Keep original evidence immutable.

Illustrative existing CLI sequence, to be parameterised and executed only in that later task:

```text
python -m ml ingest add --export <selected-exact-schema-export> --store <isolated-store-copy> --dry-run
python -m ml training build --store <authorised-store> --competition <exact-competition> --endpoint <exact-endpoint> --release-id <new-immutable-id> --out-root research/training_releases
python -m ml training verify --release <release-directory>
python -m ml bkb-features ablate --release <NBA-release-directory> --competition-source <reviewed-league-source> --tune-start <locked-date> --test-start <later-locked-date> --out <new-study-directory>
```

These commands are documentation, not executed work. The basketball challenger is basketball-specific; another sport needs its own compatible admitted training/feature/forecast route. Do not run it on another sport or invent a universal training command. The actual accepted flags are in `ml/training_admission.py` and `ml/models/basketball_features.py`. Required source/capture/endpoint/timing gates remain in force.

## 8. Evaluate and then adapt

Lock chronological TRAIN → TUNE → CALIBRATE → UNTOUCHED TEST boundaries by season/time, with earlier data allowed as lagged history only when its availability policy permits. Fit scaling, feature selection, missingness handling and hyperparameters on earlier partitions only. Use training warm-up/true window n; there is no automatic fixed five-year optimum. Compare recent windows and decay on tuning data, not on the final test.

For NBA, first-fit labels are regular-season finals only, including NBA Cup group/quarterfinal/semifinal games. Play-in, playoffs/Finals, Cup championship, preseason/exhibitions and All-Star/Rising Stars stay out. Compare BASE/no-context and the exact supported V3 comparator against the basketball feature challenger on identical later games and endpoints; distinguish current-context cycle versus legacy regulation/OT recipe cohorts. Do not silently substitute a final-inclusive-OT model for a regulation target.

Report Brier and log loss on identical contract definitions and available rows, calibration/reliability, margin/total CRPS where supported, 50/80/95% prediction-interval coverage/width, exclusions, and paired event/week uncertainty intervals. Multiple contracts from one game are dependent. An unresolved or short cohort yields INSUFFICIENT_EVIDENCE. Then freeze the winning candidate recipe, preserve a stable reference and collect genuine future pre-start predictions; promotion requires a separately recorded decision, not a better training score.

Use verified settlement feedback from actual frozen bundles to update online expert weights under a fixed versioned learning/forgetting rule. Backfilled outcomes without a prior bundle may train future models but never fabricate old expert losses. Study learning rates/forgetting on earlier chronological data, then freeze them for evaluation. A new rule/model/feature set gets a new version; refitting new data under a frozen rule retains its run receipt.

This is supervised sporting ML plus online expert aggregation. Full RL would require a separately authorised sequential state/action/reward problem, logged behaviour and independent decision evaluation behind the market firewall. It is not a prerequisite for improving probability forecasts and is not created by collecting historical results.

## Handoff for each next league

The next owner request should name: competition/seasons/window; primary/check sources; evidence destination; training population and endpoint; required counts/context; publication permission; and whether the task is collection-only or includes isolated validation, shared ingest, a training release, historical study and/or prospective shadows. Return actual counts and incomplete requirements at each gate. Do not label the next phase complete before it has run.

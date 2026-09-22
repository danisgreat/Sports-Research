# Prediction Results Log v4

Effective: 2026-07-16  
Status: CURRENT NON-NORMATIVE HUMAN-READABLE REGISTER  
Operational status: **SUSPENDED — NO ACTIVE MODELS**  
Structured records: `SPORTS_CALIBRATION_LEDGER_v3.csv` and `SPORTS_SETTLEMENTS_v3.csv`  
Schema: `SPORTS_DATA_DICTIONARY_v3.md`

## Current count

| Cohort | Frozen predictions | Settled predictions | Calibration eligible |
| --- | ---: | ---: | ---: |
| v4 / v3-compatible | 0 | 0 | 0 |
| v2/v3 historical records | Not imported | Not imported | 0 |

There are **zero calibration-eligible v4 predictions**. This is intentional. Historical rows lack the immutable cutoff, model/data/code versions, source packet, snapshot hash, and separate settlement record required by the v3 schema. Copying them into a new file would not repair the missing evidence.

The legacy records may be reviewed for failure modes, but every historical probability, mechanical grade, rank, and narrative is excluded from calibration, baseline comparison, ROI, model promotion, and headline accuracy.

## Append-only rules

The operating manual and data dictionary own the rules. This view enforces four log invariants:

1. Every publication gets a new immutable `snapshot_id`; an ISSUE also gets a new `prediction_id`, while lineage uses `forecast_series_id` and `parent_snapshot_id`.
2. One selected candidate is scored; inspected alternatives and mutually exclusive settlement branches are stored without becoming extra picks.
3. Settlement and corrections append against the exact snapshot/prediction with direct official evidence; frozen forecast fields never change and legacy eligibility is never backfilled.
4. WATCH/PASS contain no numerical forecast. ISSUE requires an ACTIVE exact scope; price claims require a complete price packet and realized P&L/CLV requires execution. There are currently zero ACTIVE scopes.

## Append contract

`SPORTS_DATA_DICTIONARY_v3.md` is the sole field/schema authority; this log does not duplicate it. Each human-readable entry shows only the identifiers and facts needed to follow the record:

| Entry | Minimum displayed content | Structured destination |
| --- | --- | --- |
| WATCH/PASS snapshot | request, primary question, `snapshot_id`, series/parent, event/market, modes/state, cutoff/freeze time, decision reason, missing prerequisites, source packet and hash | `SPORTS_CALIBRATION_LEDGER_v3.csv`; model/probability/edge/EV fields null |
| ISSUE | the snapshot fields plus `prediction_id`, selected candidate, ACTIVE model/coverage IDs, decision probability, baseline, typed uncertainty, invalidation triggers and artifact hashes | prediction row plus normalized candidate/outcome/source/model artifacts |
| Settlement | settlement/version IDs, exact prediction/snapshot, official status, observed branch/value, grade, verification time, direct official URL, rules and correction link | `SPORTS_SETTLEMENTS_v3.csv` |
| Evaluation | eligibility/exclusion, settlement and scoring versions, proper scores, baseline deltas, cluster/effective-N definition and report hash | generated evaluation artifact |

Complete candidate universes, outcome branches, source observations, uncertainty, prices and executions remain normalized child artifacts. A retrospective note may propose a hypothesis, but it cannot revise the frozen forecast or turn one result into proof of model quality.

## Active v4 prediction register

No records.

## Active v4 settlement register

No records.

## Legacy exclusion register

| Review ID | Original source | Original state | v4 eligibility | Reason |
| --- | --- | --- | --- | --- |
| `LEGACY-REVIEW-20260716-MLC-MINY-WAF` | `PREDICTION_RESULTS_LOG_v3.md`, 2026-07-16 11:55 AEST | Provisional watchlist, explicitly not a validated final card | `FALSE` | No immutable v3 snapshot/model/source packet; exact complements; event still live at review |

All other v2/v3 records are excluded by the global `LEGACY_UNVERIFIED_SNAPSHOT` designation in the audit. Their historical details remain in the archived files and legacy audit export; they are not duplicated here as active rows.

## Legacy case review - MI New York vs Washington Freedom

Review ID: `LEGACY-REVIEW-20260716-MLC-MINY-WAF`  
Competition: Major League Cricket 2026 Eliminator  
Venue: Oakland Coliseum, Oakland  
Original watchlist time: 2026-07-16 11:55 AEST (2026-07-16 01:55 UTC)  
Review verification time: approximately 2026-07-16 14:00 AEST (04:00 UTC)  
Eligibility: `FALSE - LEGACY_PROVISIONAL_UNVERIFIED_SNAPSHOT`

The v3 log said Washington Freedom elected to field and MI New York were 0/0. It published the following provisional watchlist while also saying it was **not a validated final card** because a match-specific same-day pitch report had not been verified.

MI New York subsequently scored **266/9 in 20 overs**, with **100 runs in the mandatory six-over powerplay**. The [official Washington Freedom match page](https://www.washingtonfreedom.com/schedule-fixtures-results/washington-freedom-vs-mi-new-york-wafmny07152026270186) provides the participant-hosted innings score and scorecard. The [current Cricbuzz scorecard](https://www.cricbuzz.com/live-cricket-scorecard/150931/waf-vs-miny-eliminator-3v4-major-league-cricket-2026), used as a labelled secondary phase source, lists `Mandatory 0.1-6: 100`.

| Original rank/type | Listed outcome | Stated probability | Verified target value | Mechanical grade | v4 calibration status |
| --- | --- | ---: | ---: | --- | --- |
| 1 | MI powerplay Under 52.5 | ~62% | 100 | LOSS | EXCLUDED |
| 2 | MI 20-over Under 183.5 | ~59% | 266 | LOSS | EXCLUDED |
| 3, forced complement | MI 20-over Over 183.5 | ~41% | 266 | WIN | EXCLUDED |
| 4, forced complement | MI powerplay Over 52.5 | ~38% | 100 | WIN | EXCLUDED |
| Winner lean | Washington Freedom | ~61% | Match not final on the opened sources at review time | PENDING / UNRESOLVED | EXCLUDED |

The two overs are mechanical complement outcomes, not independent evidence that half the card was good. The directional view favoured both unders, and both missed by extreme margins: 47.5 runs in the powerplay and 82.5 runs over the full-innings line.

The working bands were powerplay 44-49 and full innings 168-178. The realized values fell far outside both bands. The audit can identify plausible mechanisms - insufficient upper-tail allowance, excessive reliance on a short recent-innings sample, and failure to convert a missing surface input into a clean pass - but it cannot isolate a fitted-model error because no immutable model/feature snapshot was preserved.

The Washington winner lean remains unresolved in this log until a final is verified from an authoritative current source. A later final must be appended as a new legacy review update; this paragraph and table must not be overwritten. It will remain excluded regardless of the eventual winner.

## Next quantitative ISSUE

The next authorized append is a frozen PASS decision because the coverage registry contains no ACTIVE model. The first future quantitative v4 ISSUE must start a new forward cohort only after the exact model/coverage row is activated through the authority manifest. If any gate, timestamp, source packet, candidate universe, model artifact, baseline, calibration evidence, uncertainty record, or snapshot hash is missing, the correct entry remains `PASS`, not a precise probability.

## Legacy case review update - final verified

Review ID: `LEGACY-REVIEW-20260716-MLC-MINY-WAF`  
Update verification time: 2026-07-16 19:39 AEST (2026-07-16 09:39 UTC)  
Eligibility: `FALSE - LEGACY_PROVISIONAL_UNVERIFIED_SNAPSHOT`

The [official Washington Freedom match page](https://www.washingtonfreedom.com/schedule-fixtures-results/washington-freedom-vs-mi-new-york-wafmny07152026270186) now records the match as completed: Washington Freedom scored **270/4 in 18.4 overs** and beat MI New York, **266/9 in 20 overs**, by six wickets.

- The provisional Washington Freedom winner lean is mechanically a **WIN**, but remains `EXCLUDED` from v4 calibration and performance claims.
- Both directional under selections were **LOSSES**; their forced over complements were wins but were never independent picks.
- The correct process lesson is stronger than the result: the missing same-day surface input, absent immutable model snapshot and forced complement structure should have produced `PASS`. A correct winner lean does not rehabilitate the invalid card or offset the two severe directional total misses.
- Future reviews must score one selected outcome per market, preserve the full outcome distribution as branches, widen or explicitly model upper-tail risk, and fail closed whenever a critical registered input is unavailable.

This update appends the verified final without changing the earlier frozen review text.

## PASS snapshot - Geelong Cats vs St Kilda

| Field | Frozen value |
| --- | --- |
| Request / primary question | Rank the four supplied AFL line/total outcomes and add a potential match winner |
| Request timestamp | 2026-07-16 19:34 AEST (2026-07-16 09:34 UTC) |
| `forecast_series_id` | `AFL-20260716-GEEL-STK-R19` |
| `snapshot_id` | `SNAP-PASS-20260716-GEEL-STK-1939AEST` |
| Parent / sequence | null / 1 |
| Event | Geelong Cats v St Kilda, Round 19, GMHBA Stadium |
| Scheduled start | 2026-07-16 19:30 AEST (2026-07-16 09:30 UTC) |
| Modes / state | `RESEARCH_ONLY` / `LIVE` |
| Cutoff and freeze time | 2026-07-16 09:39:14 UTC |
| Decision | `PASS` |
| Primary reason | `MODEL_UNAVAILABLE` |
| Coverage | `AUSTRALIAN_FOOTBALL_ALL` = `UNSUPPORTED`; no ACTIVE AFL scope exists |
| Source packet | `SP-AFL-GEEL-STK-20260716-1939AEST` |
| Snapshot hash | `16fd2526538c0682858dc4f47530226e1e9f5b8dab53249a754d59174cf8e0de` |

Frozen candidate universe:

1. Geelong Cats -14.5
2. St Kilda +14.5
3. Combined total Over 175.5
4. Combined total Under 175.5

The line selections form one exact complementary market and the total selections form a second exact complementary market. They are four settlement branches, not four independent picks. No ranking, probability, confidence, edge, stake, or potential winner is issued.

Missing prerequisites: an ACTIVE model and coverage row for the exact AFL markets and `LIVE` state; registered source map; untouched test and prospective shadow evidence; frozen live-state observation; model, data, feature and code versions; baseline and calibration evidence; and a compliant non-duplicative selection policy.

Research-only note: the official AFL team announcement reported seven Geelong changes after a five-day break, including Jeremy Cameron and Tanner Bruhn out injured and three managed players, while St Kilda made one change. It also reported Geelong at 9-8 after three straight losses and St Kilda at 8-9. The official match centre scheduled the game for 19:30 AEST; the request arrived after that time. These facts are context only and are not converted into an unvalidated recommendation.

## PASS snapshot update - Geelong Cats vs St Kilda

| Field | Frozen value |
| --- | --- |
| Request / primary question | Select the best four player, team or other AFL outcomes and add a potential match winner |
| Request timestamp | 2026-07-16 19:57 AEST (2026-07-16 09:57 UTC) |
| `forecast_series_id` | `AFL-20260716-GEEL-STK-R19` |
| `snapshot_id` | `SNAP-PASS-20260716-GEEL-STK-1957AEST` |
| Parent / sequence | `SNAP-PASS-20260716-GEEL-STK-1939AEST` / 2 |
| Event | Geelong Cats v St Kilda, Round 19, GMHBA Stadium |
| Modes / state | `RESEARCH_ONLY` / `LIVE` |
| Cutoff and freeze time | 2026-07-16 09:57:24 UTC |
| Decision | `PASS` |
| Primary reason | `MODEL_UNAVAILABLE` |
| Coverage | `AUSTRALIAN_FOOTBALL_ALL` = `UNSUPPORTED`; no ACTIVE AFL scope exists |
| Source packet | `SP-AFL-GEEL-STK-20260716-1957AEST` |
| Snapshot hash | `8778f7ffe4598b39463732fac8a521c1e6c0ac4d34429d628e5b57a4b73f8d8f` |

The [official AFL live article](https://www.afl.com.au/news/1561025/follow-it-live-geelong-cats-v-st-kilda-saints-afl-round-19-2026) labelled the match LIVE from 19:30 AEST and confirmed no late changes. The opened official match-centre representation did not expose a complete frozen live score, clock or remaining-exposure record. The open-ended request also supplied no player lines, prices or settlement rules from which to freeze a valid candidate universe.

No four picks, ranking, probability, confidence, edge, stake or potential winner is issued. Producing them would require inventing live state and candidate contracts and would breach the active `MODEL_UNAVAILABLE` gate.

Retrospective status: the preceding MI New York v Washington Freedom case is final and was already appended from official evidence in the immediately preceding legacy update. It is not regraded or duplicated here.

## PASS snapshot update - Geelong Cats vs St Kilda live total 177.5

| Field | Frozen value |
| --- | --- |
| Request / primary question | Select Over or Under 177.5 combined points for the live AFL match |
| Request timestamp | 2026-07-16 21:43 AEST (2026-07-16 11:43 UTC) |
| `forecast_series_id` | `AFL-20260716-GEEL-STK-R19` |
| `snapshot_id` | `SNAP-PASS-20260716-GEEL-STK-2144AEST` |
| Parent / sequence | `SNAP-PASS-20260716-GEEL-STK-1957AEST` / 3 |
| Event / market | Geelong Cats v St Kilda / live combined total 177.5 points |
| Modes / state | `RESEARCH_ONLY` / `LIVE` |
| Cutoff and freeze time | 2026-07-16 11:44:39 UTC |
| Decision | `PASS` |
| Primary reason | `MODEL_UNAVAILABLE` |
| Additional failed gate | `CUTOFF_FAILURE` — no complete frozen official score, clock and remaining-exposure record was available |
| Coverage | `AUSTRALIAN_FOOTBALL_ALL` = `DEVELOPMENT`; `DEV_AFL_SCORE_V0` version 0.1.0 is architecture only and not fitted, calibrated, tested, shadowed, approved or ACTIVE |
| Source packet | `SP-AFL-GEEL-STK-20260716-2144AEST` |
| Snapshot hash | `e3571df90e51d77a607043359cf1acba7435effe7646d0cbaf2389707cd38440` |

Frozen candidate universe: Over 177.5 and Under 177.5. These are two branches of one market, not independent selections. The [official AFL match centre](https://www.afl.com.au/afl/matches/8195) confirmed the event but the opened public representations did not expose a complete auditable live score/clock state at the freeze time. No probability, confidence, edge, stake or directional selection is issued.

## PASS snapshot - England vs India, 2nd ODI

| Field | Frozen value |
| --- | --- |
| Request / primary question | Select the best four player, team or other outcomes and a potential match winner |
| Request timestamp | 2026-07-16 21:53 AEST (2026-07-16 11:53 UTC) |
| `forecast_series_id` | `CRICKET-20260716-ENG-IND-ODI2` |
| `event_id` | `BCCI-2118` |
| `snapshot_id` | `SNAP-PASS-20260716-ENG-IND-2155AEST` |
| Parent / sequence | null / 1 |
| Event | England Men v India Men, 2nd ODI, Sophia Gardens, Cardiff |
| Scheduled start | 2026-07-16 13:00 local / 12:00 UTC / 22:00 AEST |
| Modes / state | `RESEARCH_ONLY` / `PREGAME_PROJECTED` |
| Cutoff and freeze time | 2026-07-16 11:55:02 UTC |
| Decision | `PASS` |
| Primary reason | `MODEL_UNAVAILABLE` |
| Additional failed gate | `UNIVERSE_NOT_FROZEN` — open-ended request supplied no exact player lines, team markets, prices or settlement contracts |
| Coverage | `CRICKET_ALL` = `DEVELOPMENT`; `DEV_CRICKET_BALL_STATE_V0` version 0.1.0 is architecture only and not fitted, calibrated, tested, shadowed, approved or ACTIVE |
| Source packet | `SP-CRICKET-ENG-IND-ODI2-20260716-2155AEST` |
| Snapshot hash | `ba6d1bf5c7b0b7499895b3e76c014777daeba821c361111cf526c37532ab1279` |

Officially verified research context:

- The [ECB playing-conditions document](https://resources.ecb.co.uk/ecb/document/2026/03/24/de6a6bb4-07e3-450d-ac8f-fa6fcead9000/Metro-Bank-ODI-50-over-tour-U19-ODIs-variations-from-ICC-2026.pdf) identifies England Men v India Men at Sophia Gardens on 16 July 2026 with a 13:00 local start and 30 minutes of extra time.
- The [BCCI series announcement](https://www.bcci.tv/articles/2026/news/55556358) confirms the men’s three-match ODI series, date, venue and India squad.
- The [ICC first-ODI follow-up](https://www.icc-cricket.com/news/india-pacer-guilty-of-icc-code-of-conduct-breach) confirms India lead 1-0 after winning the first ODI by six wickets; this is series context, not a logged model result and not evidence of a repeatable edge.
- The [ICC injury update](https://www.icc-cricket.com/news/india-name-injury-replacements-for-upcoming-white-ball-series) confirms Harshit Rana was ruled out of the ODI series and Prince Yadav was added.

No candidate universe was invented and no four picks, ranking, probability, confidence, edge, stake or potential winner is issued. The immediately preceding Cats v Saints log entry is not retrospectively graded because no authoritative FINAL result was available at this cutoff; it is left unchanged under the user’s live-game rule.

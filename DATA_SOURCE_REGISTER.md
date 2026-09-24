# Data source register (full register)


> **CR-2026.09.21-3 source-audit precedence:** consult `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` before relying on an older coverage/source conclusion. Later verified route evidence supersedes disproved non-coverage; shared upstream feeds still count once. CR-3 is a control synchronization, not a new source weighting rule.


> **Current revision — 2026-09-19:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.




> **`SOURCES.md` is the new short quick-reference (v4.0 comprehensive overhaul, 2026-09-06)** — read that per card. This document is the complete register: every dated addendum, full source-card audits, and the numerical-approval gate mechanics in full detail.


Status: **ACTIVE DESIGN REGISTER — NO H0 INGESTION AUTHORISED**


Register version: **DSR-2026.09.05-v1.5**


Numerical training specification: **NTS-2026.09.19-v0.5**


Effective: **2026-09-05 (research-source audit)**


This register routes prediction-time research and defines what must be proved before any field enters H0. A source being public, official, popular, searchable, downloadable, or technically accessible does not establish permitted automation, retention, redistribution, complete coverage, stable definitions, prediction-time reconstructability, or model fitness.


No source or field is currently `APPROVED FOR FEATURE`.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Cross-sport event-verification source requirement — CR-2026.09.19-4 component (preserved under CR-2026.09.21-1)


For each forecasted event, the source register must be capable of identifying **at least three independent reliable upstream lineages**. Mirrored pages and syndicated copies share one lineage. Search snippets/generated summaries are discovery artifacts only.


Required event identity fields include venue/host, official venue-local date/time, IANA timezone, exact-date UTC offset, `Australia/Melbourne` converted date/time, AEST/AEDT label and date-rollover flag. Event-state fields must distinguish scheduled/pregame, live, postponed/cancelled and terminal.


Settlement routes must support three-source confirmation of explicit terminal state and final result. If a sport/competition lacks enough independent sources for a derivative field, record the limitation instead of treating a duplicate feed as independent confirmation.


## 1. Status vocabulary


| Status | Meaning |
|---|---|
| CANDIDATE | Plausible research/training lane identified; no H0 use |
| AUDIT IN PROGRESS | Ownership, coverage, timing, definitions, corrections and use terms are being checked |
| APPROVED FOR SNAPSHOT | Exact version and permitted capture/use are documented; immutable raw capture may begin |
| APPROVED FOR FEATURE | Named fields passed definition, known-at, quality, leakage and licence/use tests |
| RESEARCH ONLY | May support cited prediction-time human/web research under current terms; no retained H0 ingestion |
| RESTRICTED | Licence, access, automation, retention, redistribution or semantic limits block some uses |
| RETIRED | No new builds; prior approved snapshots remain reproducible evidence |


## 2. Field ownership and conflict rule


| Claim | Controlling source class | What it does not automatically control |
|---|---|---|
| Official identity, schedule, rules, participants, state, result | Governing body, league/competition, official match centre or team release | Forecast importance or proprietary derived metrics |
| Weather forecast/observation | Applicable government meteorological service and official venue roof/surface report | The sport-specific effect transformation |
| Historical official statistic | Official provider/data partner or reconciled official record | A different provider's definition or current availability |
| Derived metric | The specialist/provider that defines it | Official injury, lineup, rules, market or unrelated fields |
| Contract, terms, line and price | Actual operator/exchange at a captured time | Fair probability, outcome truth, or another operator's terms |
| Late news | Named reputable reporter when official confirmation is unavailable | Official status after an official release exists |
| Discovery/corroboration | Reference site, query engine, aggregator, preview or search snippet | Final control of a decisive volatile fact |


Conflicts are resolved field by field, not by majority vote or global site rank. Record every material disagreement and prefer the field owner with the freshest definition-compatible timestamp. Two weak sources do not equal one controlling source. Multiple branded front ends may reuse one upstream feed; treat them as one evidentiary lineage unless data provenance demonstrates independence.


The field owner must also pass a source-state check. A schedule shell, zero-filled placeholder, unfinished live record, impossible all-zero statistic block, or stale revision is quarantined for the affected field even on an official domain. Preserve URL/retrieval time/conflicting values, look for an official correction or static report, and only then use two independent high-quality current sources as a labelled provisional fallback. Unaffected official fields may remain usable.


## 3. Freshness classes


| Class | Examples | Required action |
|---|---|---|
| V0 — live | Score, clock/over/inning, on-court/on-field state | Observe and timestamp immediately; refresh just before issue |
| V1 — release driven | Lineup, starter, toss, goalie, team sheet, inactives, late changes | Refresh after the applicable official release and again before issue |
| V2 — short horizon | Injury status, expected role/workload, roof, pitch/surface, venue-local weather | Use the newest prediction-time source; branch unresolved states |
| V3 — current process | Season/rolling performance, lineup/participant form, specialist metrics | Update through the last completed eligible event and record provider lag |
| V4 — structural | Rules, venue dimensions, metric definitions, historical archive | Version by effective date and recheck on rules/provider changes |
| M0 — market | Exact contract, line, both-side odds and terms | Capture at or before cutoff; a later close is a separate benchmark only |


Research stops when every decision-driving item is verified or explicitly missing/stale/conflicting, the sport-native mechanism and contrary path are represented, and another search is unlikely to change the decision before the next required refresh.


## 4. Required source card and immutable snapshot


| Field | Required content |
|---|---|
| Source ID/version | Stable internal ID and exact provider/feed/file/API/page version |
| Owner/authority | Governing body, official partner, specialist, reporter, operator or discovery class |
| Permitted role/fields | Exact fields and definitions; approval is field-specific |
| Prohibited role | Fields or claims the source may not control |
| Population/coverage | Sport, competition, era, event type, dates, exclusions and missing partitions |
| Access/use | URL/API/file/manual capture, authentication, rate limits, robots/terms, retention and redistribution rights |
| Time semantics | Effective, first-known/published, observed, retrieved, corrected and cutoff behavior |
| Update/correction | Cadence, backfills, revisions, correction linkage and snapshot policy |
| Identity/definition | Stable IDs, crosswalks, units, rule eras and provider-version history |
| Freshness/fallback | Trigger/max age and the field-specific fallback source |
| Quality results | Completeness, uniqueness, range, referential, temporal, reconciliation and drift tests |
| Approval | Status, reviewer/date, permitted builds and blocked uses |


Every admitted snapshot stores source/version, request parameters or filename, retrieved time, upstream revision, content/hash, schema/parse state, coverage manifest, applicable use terms, and correction linkage. Canonical data never silently overwrites a revision. A feature may enter a forecast/H0 row only when its earliest demonstrable `known_at <= cutoff_at`.


## 5. Cross-sport research lanes


These rows guide prediction-time research. They do not approve H0 ingestion.


| Source ID | Candidate role | Freshness | Important restriction/gate | Status |
|---|---|---|---|---|
| `SRC-OFFICIAL-EVENT-*` | Identity, schedule, rules, participants, live state, official final | V0/V1/V4; final refresh | Provider-by-provider access, historical timing, correction and use audit | CANDIDATE |
| `SRC-OFFICIAL-STATIC-REPORT-*` | Dated official match report/gamebook as fallback when a dynamic official page is stale, misrendered or internally inconsistent | V1/V4; match exact event/date/participants and correction state | Report owns only exposed fields; team perspective, stat completeness, publication time and use still require audit | CANDIDATE / RESEARCH ONLY |
| `SRC-GOV-WEATHER-*` | Venue-local game-window forecasts/observations | V2; refresh near issue | Archive only forecasts demonstrably published by cutoff; realised weather is not a forecast feature | CANDIDATE |
| `SRC-MARKET-OPERATOR-*` | Exact contract, terms, line and price | M0 at cutoff | Operator/feed licence, timestamp accuracy, both sides, terms version and identity | CANDIDATE |
| `SRC-MARKET-ARCHIVE-*` | Historical line/price benchmark | Versioned historical | Never substitute a reconstructed/post-result value for prediction-time capture | CANDIDATE |
| `SRC-STATMUSE-RESEARCH` | Transient searchable splits and hypothesis checks for supported sports | V3 at query time | Current terms prohibit general scraping/systematic retention and require attribution; API/MCP/licence terms must govern programmatic use; never controls injuries, lineups, rules or price | RESTRICTED / RESEARCH ONLY |
| `SRC-REPORTING-NAMED-*` | Late injury/role/lineup/pitch/goalie reports pending official confirmation | V1/V2 | Name author/outlet/time; downgrade when official source exists or conflicts | CANDIDATE |


## 6. Cricket source lanes


| Source ID | Permitted prediction-time role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-CRIC-OFFICIAL-*` | Event/format/rules, toss, XI, state, scorecard, result | V0/V1; official board/competition fallback chain | Provider access, stable IDs, historical timestamps, corrections and terms | CANDIDATE |
| `SRC-CRIC-BOARD-BRANDED-SCORECARD` | Association-branded exact scorecard, innings/phase totals, wickets and result when the board routes through a specialist host | V0–V4; reconcile identity/result to board/competition | Hosting relationship, coverage, correction path, delivery legality, stable IDs, automation/retention and known-at timestamps | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-ICC-MATCH` | Fields explicitly published by ICC: competition/event identity, schedule, venue, squads/injuries, governing context and report narrative; state/result only when an exact ICC record exposes them | V0–V4; exact record, then host board/competition field owner | For non-ICC-operated events an ICC article does not automatically own toss, XI, live score, legal-ball sequence or phase totals; timestamps, corrections and use terms remain gated | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-NAMIBIA-OFFICIAL` | Host-board series identity, fixture/date, venue and board-issued Namibia squad/change notices; toss/XI only when an explicit timestamped board release states them | V1/V4; exact Cricket Namibia page/post, then competition/board field owner | No board-hosted live scorecard found; social/image posts are brittle; silence never proves toss, XI or strip; automation/retention and correction history unresolved | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-CA-MATCH-CENTRE` | Current exact-match live score, toss/team fields, scorecard/commentary and phase reconstruction where populated | V0/V1/V4; reconcile to host/event field owner | Cricket Australia is not the owner of a Namibia-hosted event; upstream feed/corrections are undocumented, rendering is dynamic and terms restrict systematic database retrieval | RESTRICTED / RESEARCH ONLY |
| `SRC-CRIC-RIGHTS-BROADCAST-TOSS-*` | Timestamped exact-match toss, confirmed-XI graphic and strip observations spoken by captain, curator or named presenter on the rights-holder broadcast | V1/V2 in toss window; capture speaker, wording and match timestamp | Geo/login/video/archive and rights limits; commentary opinion is not field-owner fact; no numerical retention approval | RESEARCH ONLY |
| `SRC-CRIC-OFFICIAL-VIDEO-*` | Verified board/competition video channel or official event-video page carrying match-specific toss, XI or pitch-report footage | V1/V2 in toss window; verify account/channel ownership and exact event/date | Video availability, geo/archive and rights limits; a title alone is discovery, and third-party channels do not become official by naming the match | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-NVPLAY-OFFICIAL-*` | Toss, teams, live scorecard and match state when the board/competition officially routes scoring through NV Play / a board-branded NV Play Match Centre | V0/V1; exact sanctioned competition/board route | NV Play is infrastructure, not automatically the competition field owner; confirm the sanctioned relationship, event identity, correction path, coverage and use/retention terms | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-BROADCAST-TRANSCRIPT-*` | Specialist live commentary that explicitly transcribes a named current-match broadcast pitch report | V1/V2; capture named speaker/presenter and timestamp | Counts as the **same lineage as the broadcast** it transcribes; never a second independent pitch source by itself | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-AUTOMATED-PITCH-METADATA-*` | Unattributed structured surface labels such as pitch/batting/pace/spin-condition blocks from downstream score/stat front ends | V2/V3; supporting context only | `AUTOMATED_PITCH_METADATA`: not a human strip observation, cannot set `STRIP STATUS: OBSERVED`; identical/near-identical unusual blocks across sites are one suspected upstream lineage until provenance proves otherwise | RESTRICTED / RESEARCH ONLY |
| `SRC-CRIC-WINDIES-OFFICIAL` | CWI/Windies Cricket fixture, venue, CPL state and official result; exact score/phase where exposed | V0/V1/V4; exact current result/match page, then official report | Schedule revisions, match-number changes, dynamic scorecard completeness, delivery legality, stable IDs and use/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-CRICSHEET-JSON` | Historical delivery/innings/match events with documented toss, players, outcome, format/revision, powerplay boundaries/missing indicators and delivery data | Versioned release; reconcile to official scorecard | Not a live/toss-time source; coverage/release lag, use terms, revision replay, day/session reconstruction and identity joins remain gated | CANDIDATE |
| `SRC-CRIC-CRICSHEET-REGISTER` | Person identity crosswalk | Exact release/hash | Attribution/licence implementation, missing-ID and crosswalk quality | CANDIDATE |
| `SRC-CRIC-SPECIALIST-SCORECARD` | Scorecards, commentary, venue/player history and exact-match reporting | V0–V3; official source controls conflicts | Access/automation terms, provider definitions, coverage and known-at reconstruction | CANDIDATE / RESTRICTED |
| `SRC-CRIC-PITCH-REPORT` | Timestamped exact-match strip/surface evidence | V2; official/team/reporting fallback | Historical reconstructability, semantic coding, conflicts and missingness | CANDIDATE |
| `SRC-CRIC-GOV-WEATHER` | Playable-time/weather/light scenarios | V2; applicable national service | Point-in-time archive and stadium-local mapping | CANDIDATE |
| `SRC-CRIC-ICC-PITCH-RATING` | ICC's own official Pitch and Outfield Monitoring Process rating (four-tier since November 2023: Very Good/Satisfactory/Unsatisfactory/Unfit) for a venue's recent internationally accredited matches | V3/V4; [icc-cricket.com pitch-ratings page](https://www.icc-cricket.com/about/cricket/rules-and-regulations/pitch-ratings) | Covers ICC-accredited international venues only, not stand-alone domestic/associate franchise grounds; assigned post-match by the match referee, so it is multi-year venue-reputation context, never a live pre-game strip report | CANDIDATE |
| `SRC-CRIC-CRICVIZ-PITCHVIZ` | CricViz's proprietary PitchViz ball-tracking-derived pitch-difficulty/pace index (0–10) | V3; citation-only | Verified 2026-09-04: [cricviz.com](https://cricviz.com/) publishes narrative/blog analysis but the numeric per-venue/per-session ratings render as an interactive graphic, not fetchable structured text; usable only when a dated named article or broadcast explicitly quotes an exact figure, never as a directly queried database | CANDIDATE / RESEARCH ONLY |


Cricsheet identifies JSON as its main/official format and exposes format version, creation and revision fields. Its documented missing-field indicators must be retained, not silently imputed. References: [formats](https://cricsheet.org/format/), [JSON](https://cricsheet.org/format/json/), [downloads](https://cricsheet.org/downloads/), and [register](https://cricsheet.org/register/).


Current official-research reference: [ICC match reporting](https://www.icc-cricket.com/news/india-retain-upper-hand-despite-sri-lanka-fightback). This proves a usable field-specific research lane, not blanket historical/API approval.


The [Windies Cricket official results lane](https://www.windiescricket.com/results/class_type/general/) confirmed P-187's CPL final and DLS result. Exact powerplay reconstruction still requires an official phase field or a legality-reconciled delivery/scorecard source; a revised schedule page must be matched to the same event ID/date/venue before it controls.


Audited exact-phase example: the [Cricket Ireland-branded Belfast–Dublin scorecard](https://cricketarchive.com/CricketIreland/Scorecards/1458/1458955.html) exposed final innings and powerplay fields used for P-115 settlement. Its usefulness does not resolve host relationship, automation, retention, full coverage or historical-known-at approval.


P-175 adds an exact current governing-report lane: the [ICC South Africa–Zimbabwe report](https://www.icc-cricket.com/news/brevis-blitz-sees-off-zimbabwe-as-south-africa-bounce-back) confirms Zimbabwe 144/8 and South Africa's seven-wicket chase. Detailed powerplay settlement still requires an exact scorecard/delivery field whose owner and legal-ball definition match the contract. P-171 was recoverable from current specialist scorecards/reporting, but no indexed competition-owner scorecard was established in this audit; retain that result as research corroboration rather than turning the specialist into a universal field owner.


P-216 adds field-specific exact-event lanes without approving any numerical source. The [ICC series overview](https://www.icc-cricket.com/news/all-the-details-about-namibia-south-africa-and-zimbabwe-tri-series), [Namibia squad release](https://www.icc-cricket.com/news/namibia-name-strong-squad-for-home-tri-series), [Zimbabwe squad/injury release](https://www.icc-cricket.com/news/experienced-spinner-in-zimbabwe-squad-for-namibia-tri-series), preceding [ICC match report](https://www.icc-cricket.com/news/brevis-blitz-sees-off-zimbabwe-as-south-africa-bounce-back) and [conditions interview](https://www.icc-cricket.com/news/a-privilege-to-watch-subrayen-on-sensational-brevis) own only the facts they explicitly publish. The conditions interview describes the preceding match at the venue, not P-216's exact strip; the P-216 strip remains `NOT FOUND`. [Cricket Namibia's tri-series announcement](https://cricketnamibia.com/cricket-namibia-to-host-the-proteas-and-zimbabwe-in-fnb-t20-tri-series/) is the host-board identity/schedule lane. The [Cricket Australia P-216 match centre](https://www.cricket.com.au/matches/CA%3A40941/namibia-men-zimbabwe-men-namibia-v-zimbabwe) is a strong moving cross-check but not the event field owner, and its terms do not authorise systematic database construction. For settlement, the [ICC final report](https://www.icc-cricket.com/news/zimbabwe-survive-namibia-fightback-in-windhoek-thriller) establishes Zimbabwe 195/6, Namibia 190 and the five-run result, while the [CricketWorld scorecard](https://www.cricketworld.com/cricket/namibia-vs-zimbabwe/match/scorecard/98363) exposes 64/1 after six. These are separate, field-specific lineages; neither owns sportsbook terms.


### 6A. Cricket toss and strip source protocol — CR-2026.09.21-1


The previous single six-rung conditions ladder is **superseded prospectively** by two separate ladders because it mixed factual toss retrieval, exact-strip observation and historical context, and later amendments duplicated the toss broadcast.


Every cricket card records:
- `TOSS STATUS`;
- `STRIP STATUS`;
- `MATCH CONDITIONS STATUS`;
- upstream lineage and freshness for each material claim.


Two front ends carrying one upstream feed are one evidentiary lineage. A current strip report and a weather forecast are different fields.


#### TOSS FACT ladder


| Rank | Source lane | Permitted use | Important note |
|---:|---|---|---|
| T1 | `SRC-CRIC-OFFICIAL-*`, board/competition exact-match centre, board-branded sanctioned scorecard | Toss winner, bat/bowl decision, XIs | Preferred field-owner route |
| T2 | `SRC-CRIC-RIGHTS-BROADCAST-TOSS-*` / `SRC-CRIC-OFFICIAL-VIDEO-*` | Toss, captain interview, confirmed-XI graphic | Verify exact event/channel; capture timestamp |
| T3 | Official team/competition live blog or timestamped official post | Toss/XI corroboration | Open the source; snippets/headlines are discovery only |
| T4 | Admitted structured endpoint such as `SRC-ESPN-SITE-API-CRICKET` where covered | Toss note, XIs, event state | ESPN/ESPNcricinfo records sharing one upstream feed count once |
| T5 | `SRC-CRIC-SPECIALIST-SCORECARD` | Toss corroboration | Official field owner controls conflicts |
| T6 | `SRC-REPORTING-NAMED-*` | Fallback/corroboration | Exact event/date/venue required |


If exhausted without verification: `TOSS STATUS = NOT_VERIFIED_AFTER_SEARCH`. Never infer the toss winner solely from innings order.


#### STRIP/PITCH EVIDENCE ladder


Only P1–P5 establish today's exact strip. P6–P8 are context.


| Rank | Signal | Lane | Evidence class / use |
|---:|---|---|---|
| P1 | Named current-match pitch report on official/rights-holder broadcast | `SRC-CRIC-RIGHTS-BROADCAST-TOSS-*`, `SRC-CRIC-OFFICIAL-VIDEO-*` | `EXACT_MATCH_OBSERVED`; capture speaker, wording, timestamp |
| P2 | Current curator/groundsman/venue/board statement about the exact strip | `SRC-CRIC-OFFICIAL-*`, host-board/venue pages | `EXACT_MATCH_OBSERVED` |
| P3 | Official toss report/preview quoting captain/coach/curator on the wicket | board/competition/ICC exact record where it actually publishes the quote | `EXACT_MATCH_REPORTED` |
| P4 | Specialist live commentary explicitly transcribing a named broadcast pitch report | `SRC-CRIC-BROADCAST-TRANSCRIPT-*` | `EXACT_MATCH_REPORTED`; same lineage as the underlying broadcast |
| P5 | Named reputable match-specific reporting with observed/quoted strip information | `SRC-REPORTING-NAMED-*` | `EXACT_MATCH_REPORTED`; author/outlet/time required |
| P6 | Immediately preceding same-venue match in the same series/tournament | official/board-branded scorecards | `DIFFERENT_STRIP_CONTEXT` unless same-strip reuse is explicitly confirmed |
| P7 | Same-venue, same-format/rules-era historical scoring/phase baseline by innings order | official scorecards, Cricsheet where covered | `VENUE_HISTORY`; compute sample or record `INSUFFICIENT_VENUE_HISTORY` |
| P8 | ICC post-match pitch rating / explicitly quoted approved historical surface metric | `SRC-CRIC-ICC-PITCH-RATING`, `SRC-CRIC-CRICVIZ-PITCHVIZ` | `VENUE_REPUTATION_CONTEXT`; never today's strip |


Valid `STRIP STATUS` values:
- `OBSERVED`
- `NOT_FOUND_AFTER_SEARCH`
- `CONFLICTING`
- `STALE_ONLY`


`NOT_FOUND_AFTER_SEARCH` is valid only after the shown P1–P8 attempt appropriate to the competition. A missing current strip widens uncertainty / lowers evidence grade; it does not license invention.


#### Venue-history missingness


The old table text saying the venue baseline was “always computable” is withdrawn. A new venue, new competition, rules-era break or insufficient comparable history can legitimately produce:


`VENUE_HISTORY_STATUS = INSUFFICIENT_VENUE_HISTORY`


Use a broader explicitly labelled comparable-context prior only if appropriate and widen uncertainty. Never fabricate a same-venue sample.


#### Shared-lineage fingerprinting and automated pitch metadata


If multiple front ends expose identical or near-identical unusual structured fields — e.g. the same `Pitch Condition`, `Batting Condition`, pace or spin labels — treat them as **one suspected upstream lineage** until provenance establishes independence.


Unattributed feed-generated fields are:
- `CLAIM_TYPE = AUTOMATED_PITCH_METADATA`
- `STRIP_OBSERVATION = NO`
- not independent observed strip reports
- never sufficient by themselves for `STRIP STATUS = OBSERVED`.


A transcript of the same broadcast and the original broadcast are also one lineage.


#### Official-page staleness


An official dynamic page can be field-specifically stale. If it remains `UPCOMING`, blank or otherwise stale while fresher reliable sources show live/final/toss/XI state:


1. mark the affected field `STALE`;
2. preserve still-valid identity/schedule fields;
3. use another official/static/sanctioned score route where possible;
4. reconcile with independent high-quality evidence;
5. do not majority-vote a stale official field into currency.


#### Mandatory toss-window refresh


At the actual toss window and again immediately before issue, refresh:
- official exact-match centre / sanctioned scorer;
- verified board/competition/rightsholder video;
- admitted structured toss/XI endpoint;
- specialist live commentary;
- official team/competition updates;
- local weather/radar.


Record whether the forecast freeze was `PRE_TOSS` or `POST_TOSS`.


#### Excluded “pitch report” sources


Fantasy-cricket, Dream11, betting/tipping and generic formulaic daily pitch-report pages remain excluded. Existing excluded-domain examples remain in force: `cricklive.in`, `pitch-report.com`, `crickonly.in`, `cricketstadiumsinfo.com`, `thecricscope.com`, `jaipurcircle.com`, `cricjosh.in`, `cricketfastliveline.in`, `bjsports.live`. A new page with the same unattributed/fantasy-tip pattern is excluded without needing a new domain-specific rule.


#### Verified retrieval-lane examples from the 2026-09-21 audit


- ICC official video pages publish dedicated “Toss, Pitch Report” content.
- Pakistan Cricket's verified official YouTube channel published a match-specific “Toss & Pitch Report” video in 2026.
- Cricket Australia exact-match Match Centre pages expose toss and teams.
- BCCI has published dedicated Toss Report pages with decision, XIs and captain comments on the wicket.
- Cricbuzz live commentary has carried named broadcast pitch-report transcripts including pitch number and surface observations; when it transcribes the broadcast, count one lineage.
- NV Play's scorer workflow explicitly records the toss and publishes live match data to Match Centre; use it only through a sanctioned board/competition route.
- ETPL testing showed identical structured pitch-condition text on multiple downstream sites; this is the reference example for `AUTOMATED_PITCH_METADATA` / shared-lineage fingerprinting.
- An ETPL official event page was observed stale as `UPCOMING` after independent sources had the final result; this is the reference example for field-specific official staleness.


These examples prove research lanes and failure modes, not blanket `APPROVED FOR FEATURE` status.


## 7. Basketball source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-BB-OFFICIAL-EVENT-*` | Schedule, rules, roster, game state, play-by-play and final | V0/V4 | League-by-league access, correction, IDs and use terms | CANDIDATE |
| `SRC-BB-OFFICIAL-INJURY-*` | Official availability status | V1/V2; team release fallback | Historical reports, publication times and status semantics | CANDIDATE |
| `SRC-BB-OFFICIAL-STATS-*` | Provider-defined pace, ratings, lineups, tracking and box statistics | V3; match centre cross-check | Coverage changes, automation/use, corrections and versioned definitions | CANDIDATE |
| `SRC-BB-FIBA-EVENT` | FIBA event identity, official final, quarter scores, box score and documented lead/margin path where exposed | V0/V4; exact FIBA game page/report | Event coverage, dynamic access, correction history, definitions, automation/retention and known-at timestamps | CANDIDATE / RESEARCH ONLY |
| `SRC-BB-FIBA-GDAP` | Under an authorised subscription: stable competition/game IDs, pre/post-game data, live score/timing, box score, play-by-play and game files | V0/V1/V4; authenticated GDAP route | Requires FIBA business contract/express authorisation; key sharing/use restrictions and throttling apply; public-page scraping is not a substitute | RESTRICTED / CANDIDATE |
| `SRC-BB-LNBP-OFFICIAL` | Exact LNBP/Copa Value identity, schedule, regulations, roster release, state, final and box fields only when an exact field-owner record exposes them | V0/V1/V4; exact `lnbp.mx` record or official app screen, then official club/static report | 2026-09-04 audit: web route returned HTTP 403; app/API, stable IDs, coverage, correction history, definitions, timestamps and use/retention terms remain unvalidated | CANDIDATE / RESEARCH ONLY |
| `SRC-BB-JBA-GAME-ROSTER` | Exact Japan federation release: named 12, publication date, matchup, venue and tip | V1; refresh after release and immediately pre-tip | Announced roster does not prove starters, minutes, late scratches or actual participation; FIBA start list/box score supersedes those fields | RESEARCH ONLY |
| `SRC-BB-QBF-WINDOW-ROSTER` | Qatar federation window squad, staff, matchup and scheduled local time | V1; refresh on federation update and pre-tip | Window squad is not a certified game start list; transliterations require FIBA ID crosswalk; cannot prove all players dressed or played | RESEARCH ONLY |
| `SRC-BB-WNBA-EVENT` | WNBA event identity, official final, quarter/box/play-by-play and team recap where exposed | V0/V1/V4; exact game page then official team report | Dynamic rendering, stable IDs, correction history, historical known-at times, definitions and use/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-BB-HERHOOP-BOX` | Specialist WNBA box-score/minutes cross-check | V3/V4; WNBA official final controls conflicts | Provider definitions, correction lineage, historical known-at time, licence/automation/retention and official reconciliation | CANDIDATE / RESTRICTED |
| `SRC-BB-SPECIALIST-PBP-*` | Possessions, lineup stints, on/off and shot-process features | V3 | Licence, coverage, possession definitions, lineup gaps and corrections | CANDIDATE / RESTRICTED |
| `SRC-BB-REFERENCE-RESEARCH` | Human-queryable history and cross-checks | V3 | No automatic H0 retention until terms/coverage/timing pass audit | RESEARCH ONLY |


The [NBA statistics glossary](https://www.nba.com/stats/help/glossary) defines NBA metrics such as pace. The [official WNBA injury report](https://www.wnba.com/wnba-injury-report) is a candidate volatility source. Neither link grants site-wide ingestion approval.


P-196 exposed a negative FIBA page-state case: a current game URL/search rendering surfaced an old 2018 head-to-head score rather than the 2026 final. `SRC-BB-FIBA-EVENT` remains the preferred field owner, but the page must pass event/date/participant and score-chronology validation. The [Agence Congolaise de Presse match report](https://acp.cd/sports/mondial-de-basketball-masculin-2027-rdc-egypte-77-75-et-premiere-victoire-congolaise-a-la-4eme-fenetre/) is a high-quality national-reporting fallback for the 77–75 final, not a FIBA box-score or numerical-ingestion substitute. Until the owner corrects a defective page, use a dated official/static report or two independent current high-quality reports provisionally for the affected field.


P-215 adds a positive exact-event example and another rendering warning. The [FIBA event page for game 126960](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers/games/126960-JPN-QAT) owns Japan 123–70 Qatar, event identity, quarter path, box score and play-by-play fields present in its current payload. A simplified render exposed blank quarter cells/“No Result Found” while the embedded record contained the complete periods, so state and statistics must be checked through event ID/date/participants, page state and chronology rather than one rendered shell. A competition schedule saying `Live (0)` is never affirmative proof that a scheduled event has not begun. FIBA team pages can mix season leaders with current roster context; they do not prove a leader is in the current game roster.


For future authorised data work, [FIBA GDAP](https://gdap-portal.fiba.basketball/) and its [documentation](https://gdap-portal.fiba.basketball/documentation), [change log](https://gdap-portal.fiba.basketball/gdap-api-change-logs) and [terms](https://gdap-portal.fiba.basketball/terms-of-services) are the credible structured route; the service remains restricted and unapproved locally. The exact [JBA roster release](https://fibaworldcup2027-asianqualifiers.japanbasketball.jp/news/525/) and [Qatar federation window-squad release](https://www.qatarbasketball.qa/news/qatar-basketball-team-faces-japan-in-world-cup-2027-qualifiers/) own their announced lists only, not starts or minutes.


### 7A. `SRC-BB-LNBP-OFFICIAL` source card — P-279 audit


| Required field | Audited content |
|---|---|
| Source ID/version | `SRC-BB-LNBP-OFFICIAL-v0`; [LNBP official site](https://lnbp.mx/) and [official mobile-app listing](https://play.google.com/store/apps/details?id=co.truewisdom.lnbp); observed 2026-09-04 19:15 Australia/Sydney |
| Owner/authority | Liga Nacional de Baloncesto Profesional (Mexico), field owner for its own competition identity, regulations, releases and official result/stat records |
| Permitted role/fields | Only the fields visibly published on an exact event/regulation/release record: competition/event identity, schedule, venue, rules version, roster status, live/final state, score and provider-defined box fields |
| Prohibited role | No inferred FIBA-rule adoption, unstated roster/import rule, operator settlement term, predicted minutes, proprietary efficiency metric, or field absent from the exact record; an app/website shell does not itself prove a final or a regulation |
| Population/coverage | LNBP and Copa Value, seasons/editions only where exact records are reachable; 2026 coverage, archive depth, deleted/corrected partitions and app-versus-web parity are unknown |
| Access/use | Scripted access to `https://lnbp.mx/` returned HTTP 403 in this audit. The app listing is public, but account needs, API/export route, rate limits, robots/terms, retention and redistribution rights were not established. Manual transient research only; no automation or bulk retention |
| Time semantics | Store the record's own publication/effective time plus observed/retrieved time. A current screen cannot reconstruct prediction-time `known_at`; no backdating from a post-result app screen |
| Update/correction | Cadence, revision IDs, correction replay and archive policy unknown. Preserve an immutable capture/hash and link any later correction rather than overwriting |
| Identity/definition | Stable competition/game/player IDs, schemas, units, phase definitions and version history were not recovered; explicit alias crosswalk and regulation edition are required |
| Freshness/fallback | V0 state/final: immediate and pre-delivery refresh. V1 lineup/roster: after official release and at G31. V4 rules: season/edition boundary. Fallback: exact official club/static report; if unavailable, two independent dated high-quality reports, labelled provisional |
| Quality results | Authority is high, operational reliability is not. Current web access test failed; no completeness, uniqueness, correction, historical-known-at or cross-device parity test passed. P-279's 96–86 final reconciled across three dated high-quality reports, but no exact LNBP final/box was recovered and one reporter's quarter claim conflicted with a provisional provider row |
| Approval | `CANDIDATE / RESEARCH ONLY` as of 2026-09-04. No H0 ingestion, feature approval, automated collection, training, phase-stat settlement or rules control until every failed/unknown field above passes §4 |


## 8. American-football source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-AF-OFFICIAL-*` | Rules, schedule, rosters, injury/inactive releases, state, gamebook and final | V0/V1/V4 | Competition/era-specific access, timestamps, corrections and use | CANDIDATE |
| `SRC-AF-CFL-OFFICIAL` | CFL rules, schedule, roster news, game state/final and official game-driver reporting | V0/V1/V4; exact CFL game/recap page | Stable structured fields, corrections, historical publication times, definitions and automation/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-AF-NFLVERSE-PBP` | NFL play-by-play and documented EPA/WP-oriented research fields | V3/versioned releases | Underlying source/licence, schema versions, corrections, coverage and prediction-time joins | CANDIDATE |
| `SRC-AF-NGS-*` | Provider-defined player/ball tracking metrics | V3 | Access/licence, historical coverage and definition drift | CANDIDATE / RESTRICTED |
| `SRC-AF-GOV-WEATHER` | Stadium-local forecast/observation | V2; NWS/other national service | Roof mapping, point-in-time archive and kick/game window | CANDIDATE |


References: [nflverse](https://nflverse.nflverse.com/), [NFL official injuries](https://www.nfl.com/injuries/), [NFL rules/operations](https://operations.nfl.com/rules-officiating/), and the [CFL official P-150 report](https://www.cfl.ca/2026/08/28/bomber-brigade-halts-alouettes-win-streak/). The report establishes a useful exact-game research lane, not blanket historical/API approval.


P-184 establishes two field-owner lanes for the current college final: the [TCU official recap and team-stat block](https://gofrogs.com/news/2026/8/29/football-tcu-falls-to-north-carolina-15-10-in-dublin) and [North Carolina official recap](https://goheels.com/news/2026/8/29/football-fb-recap-vs-tcu). The TCU final block reports 89 penalty yards, which supersedes an earlier 85-yard narrative value for that field. For P-185, the [current ESPN Robert Morris–Wagner final and box score](https://www.espn.com/college-football/game/_/gameId/401867916/robert-morris-wagner) is a reputable current scoreboard fallback while a school-owned recap remains unindexed; it confirms 28–7 and quarter scoring but does not become an official availability/rule source or H0 approval.


## 9. Baseball source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-BS-OFFICIAL-LEAGUE-*` | Schedule, rules, lineups, probable/confirmed pitchers, transactions, state and final | V0/V1/V4 | MLB/NPB/KBO and other leagues audited separately | CANDIDATE |
| `SRC-BS-NPB-BIS` | NPB event identity, schedule, starting lineups/pitchers where released, inning score, box score and final | V0/V1/V4; exact BIS game/day page | Japanese/English page parity, historical known-at times, corrections, automation/retention and terms | CANDIDATE / RESEARCH ONLY |
| `SRC-BS-KBO-OFFICIAL` | KBO event identity, starters/lineups, official game state, box score and final | V0/V1/V4; exact official game page | Endpoint stability, publication timestamps, correction history, access/use and field definitions | CANDIDATE / RESEARCH ONLY |
| `SRC-BS-CPBL-ADVANCED` | CPBL event ID, date/venue, official final/status, inning line, batting order, pitchers and box score | V0/V1/V4; `stats.cpbl.com.tw/schedule/{event_id}` | Pregame release timing, corrections, stable retrieval, automation/retention and use terms; do not infer an unreleased starter | CANDIDATE / RESEARCH ONLY |
| `SRC-BS-MILB-OFFICIAL-SCORE` | MiLB event identity/game ID, affiliate/level, state and final from official scoreboard/game page | V0/V4; exact club/league scoreboard | Dynamic access, correction history, historical known-at times, field definitions and automation/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-BS-LMB-OFFICIAL-CLUB` | LMB club-owned final and pitching/game narrative when league structured fields are incomplete | V1/V4; exact dated club report, league result preferred | Team perspective, correction path, opposing fields, historical timestamps and use/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-BS-MLB-STATCAST` | MLB pitch, contact, running and fielding measurements/defined metrics | V3; official gamefeed cross-check | Tracking-era regimes, missing tracking, download/access terms, corrections and definitions | CANDIDATE |
| `SRC-BS-RETROSHEET-EVENT` | Historical event reconstruction candidate | Versioned release | Licence/attribution, coverage, correction and official reconciliation | CANDIDATE |
| `SRC-BS-PROJECTION-*` | External projection/challenger only | Current release at cutoff | Method/version/coverage and use; never target truth | CANDIDATE / RESEARCH ONLY |
| `SRC-BS-GOV-WEATHER` | Park-local weather | V2; roof/venue report | Point-in-time archive and park-orientation transformation | CANDIDATE |


The [MLB Statcast glossary](https://www.mlb.com/glossary/statcast) controls Statcast definitions; its tracking-era changes require explicit feature regimes. [NPB](https://www.npb.or.jp/eng/) and [KBO](https://eng.koreabaseball.com/Default.aspx) official lanes remain separate populations.


Audited field-specific examples: [NPB BIS schedule/game lane](https://npb.jp/bis/eng/2026/games/gm20260826.html), [NPB official P-164 page](https://npb.jp/scores/2026/0829/f-m-20/), [NPB official P-165 final](https://npb.jp/scores/2026/0829/l-e-21/), [KBO official 2026-08-29 scoreboard](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-08-29), [CPBL official advanced GAME 290 record](https://stats.cpbl.com.tw/schedule/2026-A-290), [MiLB Sacramento scoreboard](https://www.milb.com/sacramento/scores/triple-a/pacific-coast), the [Sultanes P-161 report](https://www.sultanes.com.mx/noticias/duelazo-de-pitcheo-en-el-juego-1-y-cae-monterrey-en-tijuana), and the [MLB P-186 official game story](https://www.mlb.com/stories/game/824230/). Their visibility supports exact-field research and final settlement only; it does not settle automation, retention or historical-known-at approval. The KBO page also preserves the seven-inning rain-final state, which must remain distinct from operator action/total terms.


The [MLB P-188 official report](https://www.mlb.com/news/max-fried-returns-in-yankees-win-over-red-sox), [P-205 game story](https://www.mlb.com/stories/game/823662?storylocal=mig-final-game-button) and [P-214 report](https://www.mlb.com/news/gunnar-henderson-homers-twice-goes-4-for-4-orioles-win) demonstrate high-quality final and scoring-chronology lanes for retrospective bullpen/cluster analysis. They do not reconstruct prediction-time bullpen availability or operator action terms.


## 10. AFL/AFLW source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-AFL-OFFICIAL-*` | Rules, fixtures, teams/late changes, injuries, match centre, official stats and final | V0/V1/V4 | Historical release times, event access, correction and definition versions | CANDIDATE |
| `SRC-AFL-HISTORICAL-*` | Historical match/player records | V3/V4; official reconciliation | Coverage, identity, terms, correction and event-time fields | CANDIDATE / RESEARCH ONLY |
| `SRC-AFL-SQUIGGLE` | Fixtures/scores and external-model consensus challenger | Respect current cache/user-agent limits | API terms, hobby-service reliability, coverage; lacks advanced Champion Data fields | CANDIDATE / RESTRICTED |
| `SRC-AFL-BOM` | Venue-local forecast and observation | V2; official venue roof report | Point-in-time archive and venue mapping | CANDIDATE |


Official AFL/AFLW sources control current facts. The [official AFLW P-163 report](https://www.afl.com.au/aflw/news/1596975/adelaide-crows-crank-it-up-to-hand-west-coast-eagles-third-loss-on-the-trot) establishes a useful exact-game final/quarter-path research lane, while the [official P-169 AFL match centre](https://www.afl.com.au/afl/matches/9021) owns Carlton's 74–55 final. [Squiggle's API](https://api.squiggle.com.au/) is a candidate external comparison, not an approved feature source or production backend.


The [official P-191 match centre](https://www.fremantlefc.com.au/matches/8910) and [official P-193 AFLW report](https://www.afl.com.au/aflw/news/1598373/richmond-tigers-leave-it-late-to-edge-essendon-bombers-in-dreamtime-thriller) add exact-game final and game-flow lanes. Ground-level wind direction at bounce remains a separate V2 conditions field and must not be inferred solely from a post-match narrative.


## 11. Rugby-league source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-RL-OFFICIAL-*` | Rules, team lists, late mail/final update, injuries, match stats/state and final | V0/V1/V4; refresh at current official final-update deadline | Historical publication times, corrections, access and definitions | CANDIDATE |
| `SRC-RL-HISTORICAL-*` | Match/player/venue archive and cross-check | V3/V4 | Coverage, identity, licensing, corrections and event-stat definitions | CANDIDATE / RESEARCH ONLY |
| `SRC-RL-GOV-WEATHER` | Venue-local weather | V2; BOM/appropriate national service | Point-in-time archive and venue mapping | CANDIDATE |


References: [NRL team-list lane](https://www.nrl.com/news/topic/team-lists/), [NRL statistics](https://www.nrl.com/stats/), and [casualty ward](https://www.nrl.com/casualty-ward/). Refresh timing must follow the current competition release, not a timeless hard-coded number.


Audited field-specific example: the [NRL Broncos–Storm official report](https://www.nrl.com/news/2026/08/27/thursday-night-footy-broncos-v-storm/) exposed the final, halftime score and decision-driving player/tackle narrative. It supports those fields for research; it is not blanket approval for historical automated ingestion.


The [NRL P-170 official report](https://www.nrl.com/news/2026/08/29/super-saturday-we-stand-with-jai-at-cbus-super/) is an additional exact-event lane for the Cowboys' 24–10 final and second-half separation path. It controls only the fields it exposes; team lists, late mail and structured statistics still require their own official releases/definitions.


## 11A. Rugby-union and rugby-sevens source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-RU-WORLD-RUGBY-LAWS` | Current laws, scoring, variations, cards and law trials | V0; exact competition regulations also required | Version/competition mapping and historical law-era joins | CANDIDATE / RESEARCH ONLY |
| `SRC-RU-OFFICIAL-COMP-*` | Fixture, stage, teams, late changes, disciplinary state, match centre, statistics and final | V0/V1/V4; official union/team report fallback | Competition-specific access, publication times, corrections, provider definitions and use | CANDIDATE |
| `SRC-RU-NZR-NPC-*` | NPC identity, draw, team/provincial releases, match facts and finals where exposed | V0/V1/V4; exact NZR/provincial page | Current endpoint stability, historical known-at, corrections, definitions and automation/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-RU-LNR-SUPERSEVENS` | SuperSevens stage/schedule, tournament format, official reporting and results where exposed | V0/V1/V4; exact stage/match page | Match-level stat completeness, publication timing, corrections and use terms | CANDIDATE / RESEARCH ONLY |
| `SRC-RU-SPECIALIST-STATS-*` | Defined territory, entries, set piece, breakdown, line-break, card, scoring and player fields | V3/V4; official final controls conflicts | Provider definitions, competition coverage, missingness, corrections, licence and known-at reconstruction | CANDIDATE / RESTRICTED |
| `SRC-RU-GOV-WEATHER` | Venue-local forecast and observation | V2 | Point-in-time archive, venue mapping and surface mechanism | CANDIDATE |


References: [World Rugby Laws](https://passport.world.rugby/laws-of-the-game/) and the [official LNR SuperSevens hub](https://supersevens.lnr.fr/). The P-128 RugbyPass final is retained as reputable specialist corroboration because an accessible field-owner match report was not recovered; it does not become an official or approved H0 source. The official SuperSevens report/hub is preferred to generic score aggregators for P-132-style stage and result facts.


## 12. Soccer source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-SOC-OFFICIAL-*` | Rules, fixtures, squads/XI, suspensions, state, official stats and final | V0/V1/V4 | Competition-specific access, correction and provider semantics | CANDIDATE |
| `SRC-SOC-ASEAN-MATCH` | ASEAN competition identity, schedule, tie/aggregate state, start lists when released, official goals and final | V0/V1/V4; exact ASEAN United FC match page/media start list | Dynamic-field availability, exact publication times, corrections and use terms; does not control corners unless the official provider exposes that field | CANDIDATE / RESEARCH ONLY |
| `SRC-SOC-UEFA-MATCH` | UEFA competition/tie identity, schedule, venue, officials, lineups/updates and official final where exposed | V0/V1/V4; exact UEFA match page/report | Dynamic pages may not expose every field to the current access route; archive timing, corrections and use terms require audit | CANDIDATE / RESEARCH ONLY |
| `SRC-SOC-OFFICIAL-CLUB-REPORT` | Official club final, goals, lineups, disciplinary events and match narrative when the competition page is incomplete | V1/V4; exact dated report | Team perspective does not control opponent proprietary metrics; archive timing, corrections and use/retention still require audit | CANDIDATE / RESEARCH ONLY |
| `SRC-SOC-OFFICIAL-RESERVE-CLUB` | Official reserve/MLS NEXT Pro club final, phase and narrative when the competition page is incomplete | V1/V4; exact dated club report | Stat-field completeness, corrections, participant-phase detail, archive timing and use/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-SOC-NICHE-AGG-PROV` | Provisional discovery/cross-check for sparse-league corners or other niche fields | V4 only after official/provider-owner retry | Upstream-feed independence, provider definition, correction history, operator match, licence and known-at time | RESTRICTED / RESEARCH ONLY |
| `SRC-SOC-STATSBOMB-OPEN` | Selected historical event/lineup/360 research data | Versioned repository snapshot | Selective competition/season coverage, attribution/use, corrections, availability timing and provider match | CANDIDATE |
| `SRC-SOC-OPTA-DEFINITIONS` | Provider definition of shots, SOT, blocks and other Opta events | V4 | Data access is separate from public definition access; provider matching required | RESEARCH ONLY |
| `SRC-SOC-XG-*` | Provider-defined xG/xA or shot-quality feature | V3 | Method, version, coverage, corrections and terms; never mix providers silently | CANDIDATE / RESTRICTED |
| `SRC-SOC-GOV-WEATHER` | Venue-local weather | V2 | Point-in-time archive and roof/surface mapping | CANDIDATE |
| `SRC-SOC-LEAGUESCUP-OFFICIAL` | Leagues Cup (MLS/Liga MX) competition identity, schedule, official match report, semifinal/final endpoint and result | V0/V1/V4; exact `leaguescup.com`/`es.leaguescup.com` report | Already used successfully for P-265 (Toluca-León semifinal, 2026-09-02); coverage of earlier rounds, corrections, stable IDs, automation/retention and use terms remain unaudited. Formalised as a named row 2026-09-04 rather than left as an inline citation only | CANDIDATE / RESEARCH ONLY |


[StatsBomb Open Data](https://github.com/statsbomb/open-data) is selective, not a universal upcoming-match feed. Provider-specific corner, card and SOT labels require exact definition continuity.


The [Gotham P-147 official recap](https://www.gothamfc.com/news/recap-gotham-fc-portland-battle-to-draw-in-muchanticipated-rematch) exposed score, phase, xG, shots and corners. The [Colorado Rapids 2 P-149 official recap](https://www.coloradorapids.com/rapids2/news/recap-colorado-rapids-2-fall-in-tight-battle-against-ventura-county-fc) exposed the reserve-match final and narrative. APWin, TotalCorner, PlayerStats, BetPawa/Sportradar-derived pages and similar front ends remain provisional niche lanes; multiple front ends are not independent evidence when they share an upstream feed.


P-172–P-183 add several high-quality exact-event result lanes: the [Liverpool P-172 official report](https://www.liverpoolfc.com/news/isak-and-munoz-score-liverpool-draw-nottingham-forest/), [Bundesliga P-180 official report](https://www.bundesliga.com/en/bundesliga/news/cologne-hoffenheim-match-report-highlights-matchday-1-38869), [KNVB P-182 result lane](https://www.knvb.nl/node/15406), and [LaLiga P-183 official match page](https://www.laliga.com/en-MA/match/temporada-2026-2027-laliga-ea-sports-levante-ud-real-betis-3). Use the exact fields exposed by each owner. The LaLiga page exposes official shots and 5–8 corners; a club report may control narrative and final but not automatically own a proprietary corner count.


The Ligue 3 audit remains field-specific. [L'Équipe's round report](https://www.lequipe.fr/Football/Actualites/Amiens-gagne-enfin-thionville-accroche-mais-toujours-leader-le-resume-de-la-quatrieme-journee-de-ligue-3/1714460) supports finals; [Kickmetrics for P-177](https://kickmetrics.io/en/soccer/match/sc-aubagne-air-bel-bourg-en-bresse/019f25cd-f24a-7bdf-818e-303ac65584bb) and [Offside Scores for P-179](https://offsidescores.com/pt/futebol/jogo/thionville-lusitanos-paris-13-atletico-20260829/8be47d51-2258-429b-a957-27dc573f6d65/detalhe) remain specialist stat lanes. P-176-C05 and P-178-C05 stay unresolved; P-179-C05 stays provisional. A Forebet predicted corner score, a TotalCorner page still labelled upcoming after the final, or several fronts from one feed are negative source-state examples and cannot settle the field.


Audited field-specific examples: [ASEAN United FC Vietnam–Thailand official match page](https://aseanutdfc.com/vi/asean-championship/match/38w3neiqa1x8wrv2ibhgum978/details) and [UEFA Apollon–FH official match page](https://www.uefa.com/womenseuropacup/match/2049375--apollon-ladies-vs-fh/matchinfo/). Use only the fields actually exposed and timestamped by each owner.


The P-123 audit also establishes a negative source-state example: the Uzbekistan PFL match centre remained an all-zero 0-0 placeholder while current independent match reports documented BuxDU 0–4 Metallurg. The PFL shell is retained as a conflict record, not a valid settlement source for that score or its zero statistics.


P-194–P-210 add competition-owned result lanes through [Bundesliga](https://www.bundesliga.com/en/bundesliga/news/freiburg-werder-bremen-match-report-highlights-matchday-1-suzuki-38905), [Lega Serie A](https://www.legaseriea.it/serie-a/news/lazio-genoa-2026-2027-1-0-cronaca-risultato-gol) and [LaLiga](https://www.laliga.com/es-PE/partido/temporada-2026-2027-laliga-ea-sports-rc-deportivo-valencia-cf-3). Use them for the exact fields exposed, not as blanket corner owners. P-208 also exposed a negative official-domain case: a Lazio highlight slug displayed the score in the wrong orientation; event/date/participants, page content and competition/current reporting must agree before a slug or title settles a field.


New field-specific lanes from the P-124–P-136 audit:


- The [Liga Profesional official Fecha 4–7 schedule](https://www.ligaprofesional.ar/notas/primera/2026/08/07/agenda-de-la-fecha-4-a-la-7/) controls P-135's competition schedule (Unión–Sarmiento, 19:00 Argentina). A rendered current scoreboard may support live state, but it does not replace the LPF schedule owner.
- [The Away End's Sikkim competition page](https://theawayend.co/sikkim-premier-division-league/) and [Sikkim Express reporting](https://www.sikkimexpress.com/news-details/a-division-s-league-2026-sikkim-aakraman-overcomes-red-panda) are useful local discovery/corroboration lanes. Neither resolves P-126's conflicting exact date without an SFA field-owner record.
- The Israeli Football Association remains the preferred P-130 field owner, but the exact current match record was not recovered. PGLive/Tips.GG agreement can support a provisional regulation/AET score only; their agreement cannot settle an unfrozen corner-provider field.


## 13. Tennis source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-TEN-ATP-WTA-ITF-*` | Official event/player identity, draw, format, schedule, withdrawal, score, set score and final where exposed | V0/V1/V4; exact tour/event page | Tour/event coverage, historical known-at times, corrections, stable IDs, access/use and retirement semantics | CANDIDATE / RESEARCH ONLY |
| `SRC-TEN-OFFICIAL-EVENT-*` | Tournament-owned draw, court schedule, conditions, rules and official result/report | V0/V1/V4; governing tour fallback | Publication timing, corrections, IDs, automation/retention and field definitions | CANDIDATE / RESEARCH ONLY |
| `SRC-TEN-SPECIALIST-STATS-*` | Defined current serve/return, surface history, point/game/set statistics and cross-checks | V3/V4; official score controls final conflicts | Provider continuity, sample/coverage, corrections, retirement treatment, licensing and known-at reconstruction | CANDIDATE / RESTRICTED |
| `SRC-TEN-TENNISCOM-CURRENT` | Current match set score and defined serve/return/break statistics as a specialist cross-check | V3/V4; ATP/WTA/ITF/event source controls corrected final | Provider/upstream identity, correction latency, retirement semantics, licensing, automation/retention and known-at reconstruction | CANDIDATE / RESEARCH ONLY |


The [Tennis.com Kopp–Krumich match page](https://www.tennis.com/tournaments/schwaben-open/matches/s-kopp-vs-m-krumich-2026-08-27) proved useful for current set score and serve/break-point fields in the P-118 audit. It remains a specialist research lane, not governing-tour authority or an approved H0 source.


The [ATP Winston-Salem official results](https://www.atptour.com/en/scores/current/winston-salem/6242/results) and [official tournament schedule](https://www.winstonsalemopen.com/en/scores/schedule) are retained as field-owner lanes for P-136 identity, round, order and result. Tennis.com remains a useful current cross-check but does not override ATP/event corrections.


Livesport initially exposed the P-162 set score for research. The 2026-09-02 follow-up recovered the [official ITF printable draw](https://www.itftennis.com/en/tournament/draws-and-results/print/?eventClassificationCode=M&matchTypeCode=S&tourType=N&tournamentId=1100204161), which closes the final as Ferguson 6-1, 6-4. The printable draw is a field-specific official research lane; its coverage, revision semantics, stable IDs, automation/retention and historical `known_at` still require audit. The [official ATP Zhangjiagang results](https://www.atptour.com/en/scores/current-challenger/zhangjiagang/7783/results) separately confirms P-225 as Chun-Hsin Tseng vs **Tianhui Zhang**, 6-4, 6-0; it corrects the later settlement label without altering the frozen forecast or granting H0 approval.


The [ATP US Open results lane](https://www.atptour.com/en/scores/current/us-open/560/results?matchType=singles) confirmed P-213, while the [Tennis.com Kessler–Alexandrova page](https://www.tennis.com/tournaments/us-open/matches/m-kessler-vs-e-alexandrova-2026-08-30) supplied a current final/stat cross-check for P-212. The WTA page remained stale at suspended/upcoming after the match; authority did not cure freshness, so that state was quarantined rather than allowed to override a current corroborated final.


## 14. Ice-hockey source lanes


| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-IH-NHL-OFFICIAL` | NHL schedule, rules, roster, projected/confirmed lineup/goalie reports, state, official stats and final | V0/V1/V4 | Endpoint/access documentation, corrections, IDs and use terms | CANDIDATE |
| `SRC-IH-MONEYPUCK-DL` | Downloaded NHL shot/xG and game/player research fields within stated use | Versioned/nightly release as documented | Non-commercial/ad-hoc use limits, attribution, approved access, schema/corrections; listed shot data omits blocked shots | RESTRICTED / CANDIDATE |
| `SRC-IH-SPECIALIST-SHOTS-*` | Defined shot attempt/xG/manpower/line metrics | V3 | Licence, methodology, coverage, corrections and provider drift | CANDIDATE / RESTRICTED |
| `SRC-IH-GOALIE-REPORT-*` | Starting-goalie/line combination report pending official confirmation | V1; official NHL/team source controls conflicts | Historical availability, accuracy, timestamps and terms | CANDIDATE / RESEARCH ONLY |
| `SRC-IH-METALLIGAEN-OFFICIAL` | Danish Metal Ligaen fixture, final, period/game-flow report and club/league context | V0/V1/V4; exact league report then club report | Structured stat completeness, goalie release timing, OT/SO notation, corrections, stable IDs, automation/retention and operator-term separation | CANDIDATE / RESEARCH ONLY |
| `SRC-IH-AIHL-SPECIALIST` | Australian Ice Hockey League fixture, final, period-by-period score and game-flow narrative | V0/V1/V4; exact dated report | No AIHL-official (league-branded) structured data source was located as of 2026-09-04; this specialist reporting lane is the best available field-specific source, not a league-official record. Corrections, historical publication times, stable IDs and automation/retention remain unaudited | CANDIDATE / RESEARCH ONLY |


References: [NHL glossary](https://www.nhl.com/info/hockey-glossary), [official projected lineups/goalies](https://www.nhl.com/news/topic/game-previews/nhl-projected-lineup-projections), and [MoneyPuck downloads/use statement](https://www.moneypuck.com/data.htm).


Formalised 2026-09-04: `SRC-IH-AIHL-SPECIALIST` names the existing Ice Hockey News Australia lane (already used for P-125/P-166 below) as a stable row rather than leaving AIHL coverage as prose only. Before relying on it for a new AIHL card, re-attempt an official league/club match-centre page first, per the authority hierarchy in RULES_GENERAL.md §4 — this row is a fallback, not a preferred source.


For AIHL research, [Ice Hockey News Australia's P-125 result](https://icehockeynewsaustralia.com/2026/08/28/2026-goodall-cup-playoffs-canberra-brave-defeat-sydney-bears-in-the-preliminary-round-to-advance/) exposed final, period and SOG fields and linked a game card. Its [P-166 semifinal report](https://icehockeynewsaustralia.com/2026/08/29/2026-goodall-cup-playoffs-canberra-brave-defeat-melbourne-mustangs-in-semifinals-to-advance/) corroborates Canberra's 5–4 overtime final. Treat both as reputable specialist/research lanes pending direct AIHL field-owner access; neither establishes sportsbook OT/action terms or blanket numerical-ingestion approval.


The [Metal Ligaen P-199 official report](https://metalligaen.dk/nyheder/kampen-kort-finsk-fest-i-frederikshavn/) establishes a strong exact-event final/period/narrative lane. It does not establish P-200's unnamed operator treatment of overtime, shootout goals, totals or puck lines; preserve that definition follow-up separately.


## 15. Market snapshot schema


Market snapshots remain separate from sports features unless the build is explicitly `MARKET_INFORMED`.


| Field | Meaning |
|---|---|
| `market_snapshot_id` | Immutable snapshot key |
| `event_id` / `canonical_contract_id` | Exact event and settlement geometry |
| `operator` / `source_version` | Price owner and feed definition |
| `market_family` / `phase` / `metric` / `line` | Contract identity |
| `decimal_odds_side_a` / `decimal_odds_side_b` | Same-source, same-time prices where available |
| `captured_at` / `cutoff_at` | Price time and forecast boundary |
| `overround` / `devig_method_version` | Frozen transformation |
| `terms_version` | Push, void, OT, listed-player and shortening rules |
| `market_lane` | MARKET_BLIND benchmark only, MARKET_ONLY, or MARKET_INFORMED input |
| `raw_snapshot_hash` | Reproducibility |


## 16. Approval gate


A field moves to `APPROVED FOR FEATURE` only after access/use terms, exact coverage, identities, definitions, rules eras, correction replay, prediction-time `known_at`, completeness, uniqueness, ranges, joins, negative controls and feature admission all pass. Material limitations are copied into the applicable H0 card.


Until then, source names are research architecture candidates—not evidence that numerical training can begin.


## 17. Session access audit — 2026-09-01


Access results are session-specific and timestamped. Under RULES_GENERAL.md §4 they are never baked in as permanent claims that a site is available or blocked. Re-test each session and record the result again.


| Target | Direct result | Proxy result | Note |
|---|---|---|---|
| `statsapi.mlb.com` | 200 | — | Schedule and `v1.1/game/{gamePk}/feed/live` both served |
| `api-web.nhle.com` | 200 after redirect | — | Use `-L`; the retired `statsapi.web.nhl.com` host did not resolve |
| `api.squiggle.com.au` | 200 | — | AFL games/ratings |
| `api.open-meteo.com`, `archive-api.open-meteo.com` | 200 | — | Keyless, global, hourly, coordinate-addressed |
| `api.weather.gov` | 200 | — | Requires a descriptive User-Agent |
| `api.weather.bom.gov.au`, `bom.gov.au` | 200 | — | Use HTTPS; HTTP redirects |
| `cricbuzz.com` | 200 | — | `cricket-match-facts/{id}/{slug}` exposed toss, venue, umpires, local/GMT/IST start |
| `icc-cricket.com`, `cricketarchive.com`, `cricsheet.org` | 200 | — | — |
| `understat.com`, `nrl.com`, `afl.com.au`, `espn.com` | 200 | — | — |
| `statmuse.com` | 200 shell by direct fetch | Rendered fetch returns the data table | The raw HTML is a JS shell; use a rendering fetch |
| `espncricinfo.com` | 403 | 200 via `r.jina.ai` | Proxy output carried a stale `Published Time`; verify event dates before use |
| `fbref.com` | 403 | 200 via `r.jina.ai` | — |
| `pro-football-reference.com` | 403 | 200 via `r.jina.ai` | — |
| `atptour.com` | 403 | 200 via `r.jina.ai` | — |
| `baseball-reference.com` | 403 | 403 via `r.jina.ai` | No lane established this session |
| `site.api.espn.com` | 403 | — | Previously usable; treat availability as session-specific |


A proxy or reader rendering never upgrades a source's authority, licence or freshness. A proxied page must pass the same event/date/participant and revision checks as a direct fetch, and the stale-timestamp case above is why.


### Session access audit addendum — 2026-09-02


| Target | Session result | Permitted research use | Limitation/status |
|---|---|---|---|
| ITF printable draws | Exact official P-162 set score recovered | Official draw/result field for the exact event | Candidate/research only; coverage, revisions, identifiers, use terms and historical timing unproved |
| ATP Zhangjiagang results | Exact P-225 identity and set score recovered through the rendered official page | Official tour identity/result field | Candidate/research only; direct access remained session-dependent and H0 gates remain open |
| ICC static match reports | P-216 final and narrative recovered | Competition-owner result/mechanism fallback when a dynamic centre is stale or incomplete | Does not own phase fields, operator rules or reusable data rights |
| ETPL static match report | P-238 final recovered while the dynamic match page remained stale/upcoming | Competition-owner final/result narrative | Static page owns only its exposed fields; no general automation approval |
| 365Scores / Football365 complete timelines | P-148/P-176 corner endpoints reconstructed | Provisional niche-field fallback | Not the named operator/provider field owner; upstream lineage and correction state unproved |


No row in this addendum changes the global status: **no source or field is APPROVED FOR FEATURE and no H0 ingestion is authorised**.


### Session access audit addendum — 2026-09-04


| Target | Session result | Permitted research use | Limitation/status |
|---|---|---|---|
| `espncricinfo.com` match-preview article (IPL 2026, PBKS v GT) | Direct 403, confirmed again; `r.jina.ai` 200 | Rung 4 of the §6A cricket conditions ladder for major/franchise fixtures | Returned genuinely specific pitch content (numbered strip, prior scores, coach quote), not filler; confirms this rung is real and worth the query, not merely a theoretical lane |
| `cricviz.com` PitchViz blog page | 200, publicly readable | Narrative/citation-only research; not a per-match structured feed | Numeric per-venue ratings render as an interactive graphic and were not present in the fetched text; treat any specific PitchViz figure as usable only via a dated citing article, never a direct query |
| `icc-cricket.com/about/cricket/rules-and-regulations/pitch-ratings` | 200 | Official rule/process description of the ICC Pitch and Outfield Monitoring Process; specific venue ratings require a separate dated report/news search | Confirms the four-tier (Very Good/Satisfactory/Unsatisfactory/Unfit, since November 2023) rating exists and is ICC-owned; covers accredited international venues only |
| Generic "pitch report" tipping/SEO domains (`cricklive.in`, `pitch-report.com`, `crickonly.in`, `cricketstadiumsinfo.com`, `thecricscope.com`, `jaipurcircle.com`, `cricjosh.in`, `cricketfastliveline.in`, `bjsports.live`) | Indexed and returned in search, not individually fetched | None | Confirmed as the unattributed bulk-generated pattern already excluded by §6A; added to the named exclusion list so a future session recognises them immediately |


No row in this addendum changes the global status: **no source or field is APPROVED FOR FEATURE and no H0 ingestion is authorised**.


### Session access audit addendum — 2026-09-04(b), from the P-268–P-271 settlement pass


| Target | Session result | Permitted research use | Limitation/status |
|---|---|---|---|
| `nrl.com` draw/match-centre page (`/draw/nrl-premiership/.../bulldogs-v-broncos/`) | Direct fetch redirected to `account.nrl.com` login/OAuth flow (302) | None from this route this session | **Degraded from the 2026-09-01 audit**, which listed `nrl.com` as a working V0/V1 lane (RULES_GENERAL.md §4: access is session-specific and must be re-tested, never baked in as permanently available). Fallbacks used successfully: ABC News NRL score centre and Zerotackle match centre (below) |
| ABC News NRL score centre (`abc.net.au/news/sport/score-centre/nrl/...`) | 200, current final and full-time state | Reputable current-final fallback when `nrl.com` is inaccessible | Independently agreed with Zerotackle on both final and halftime score for P-270; treat as corroboration, not a league-official replacement |
| Zerotackle NRL match centre | 200, current final, halftime and full-time state | Specialist current-result cross-check | Agreed with ABC News; two independent lineages, not one feed shown twice |
| `mykbostats.com` exact game page (`/games/{id}-...`) | Direct 403; `r.jina.ai` 200 with a complete official-style line score | Rung/fallback KBO box-score lane when the official KBO site is not directly reachable | Same proxy caveat as `espncricinfo.com`: verify event date/identity before use — a same-site team page returned a *different, earlier* game mislabelled as "previous match" in this exact session (see the P-268 retrospective in `PREDICTION_LOG_COMBINED.md`) |
| Korean-language sports news (`sports.khan.co.kr`, `mt.co.kr`) | 200, dated, detailed, mutually consistent same-day recaps | High-value KBO same-day recap/box-score corroboration, particularly for bullpen/pitching-change detail beyond a bare line score | Named outlets, not aggregators; two independent lineages agreed with each other and with the proxied box score for P-268. Non-English KBO reporting is generally under-used in this log and should be searched routinely, not only when English-language sources are thin |
| `afl.com.au` match report | 200, complete quarter-by-quarter score and narrative | Confirmed continued strong direct-access lane for AFL finals coverage | Consistent with the existing register entry; no change |


No row in this addendum changes the global status: **no source or field is APPROVED FOR FEATURE and no H0 ingestion is authorised**.


## 18. Recency, head-to-head and trend lanes


These support the mandatory L5/L10/L15/L20 and head-to-head retrieval at RULES_GENERAL.md §11.3B. None is approved for H0 ingestion.


| Source ID | Permitted role | Freshness | Restriction/gate | Status |
|---|---|---|---|---|
| `SRC-RECENCY-OFFICIAL-SCHEDULE-*` | Completed-event list, dates, opponents and official results for each window | V0/V4 | Preferred owner for the window itself; league-by-league access and correction audit | CANDIDATE |
| `SRC-RECENCY-OFFICIAL-BOX-*` | Per-event official box/scorecard from which the sport-native process metric in each window is computed | V4 | Definitions are provider-versioned; phase fields need an official phase line or legality-reconciled reconstruction | CANDIDATE |
| `SRC-H2H-CONTINUITY-*` | Coach, roster, spine, starter/goalie/XI, venue, surface and rules-era state at each prior meeting, used to compute the continuity count | V3/V4 | Continuity must be evidenced per meeting, not assumed from team name | CANDIDATE |
| `SRC-STATMUSE-RESEARCH` | See §5; the fastest lane for windowed team/player splits and head-to-head game lists in supported American leagues | V3 at query time | Terms prohibit general scraping and systematic retention and require attribution; never controls injuries, lineups, rules, state or price; every returned row is date-verified against the official source before it is decision-driving | RESTRICTED / RESEARCH ONLY |


### StatMuse query patterns verified 2026-09-01


Supported leagues include MLB, NBA, WNBA, NFL and NHL. The URL form is `https://www.statmuse.com/{league}/ask/{query-with-hyphens}`. Phrasing materially changes what is returned, so the working forms are recorded:


| Need | Working pattern | Verified behaviour |
|---|---|---|
| Team last-N game log | `/{league}/ask/{team}-last-10-games` | Returned a dated game-by-game table with opponents and scores; the most recent row matched the official result for that date |
| Head-to-head game list | `/{league}/ask/{teamA}-scores-vs-{teamB}-last-10-games` | Returned a dated game-by-game head-to-head list with both final scores |
| Head-to-head aggregate **(fails)** | `/{league}/ask/{teamA}-vs-{teamB}-last-10-meetings` | Returned pooled season-level averages, **not** a meeting list; do not use this phrasing for the head-to-head window |
| Player windowed splits | `/{league}/ask/{player}-last-15-games` | Player game log for the window |


Swap `10` for `5`, `15` or `20` to fill the other windows. Because the aggregate phrasing silently returns a different object, every StatMuse result is checked for row count, date range and whether the returned object is a game list or a pooled average before it is used. StatMuse is a research accelerator; the official league source remains the field owner for every decisive fact and for settlement.


## 19. Environment and conditions lanes


Supports the mandatory environment gate at RULES_GENERAL.md §11.3C.


| Source ID | Permitted role | Freshness | Restriction/gate | Status |
|---|---|---|---|---|
| `SRC-WX-GOV-NWS` | United States venue forecasts/observations from `api.weather.gov`; gridpoint hourly after a `/points/{lat},{lon}` lookup | V2; refresh at G31 | Government field owner for its forecasts; requires a descriptive User-Agent; US coverage only | CANDIDATE |
| `SRC-WX-GOV-BOM` | Australian venue forecasts/observations, including `api.weather.bom.gov.au` location forecasts | V2; refresh at G31 | Field owner for Australian forecasts; location IDs must be mapped to the venue, not the city centre | CANDIDATE |
| `SRC-WX-GOV-OTHER-*` | The applicable national meteorological service for any other host country | V2 | One row per service; each needs its own coverage, licence and archive audit | CANDIDATE |
| `SRC-WX-OPENMETEO-FORECAST` | Coordinate-addressed hourly match-window forecast where a national service is unavailable, or as a second independent conditions signal | V2; refresh at G31 | Model aggregator, **not** a national service; it re-serves national model output and does not become the field owner. Verified fields: `temperature_2m`, `precipitation_probability`, `precipitation`, `wind_speed_10m`, `wind_gusts_10m`, `wind_direction_10m`, `relative_humidity_2m`, `dew_point_2m`, `cloud_cover`, with `timezone` set to the venue | CANDIDATE / RESEARCH ONLY |
| `SRC-WX-OPENMETEO-ARCHIVE` | Point-in-time historical hourly conditions for retrospective reconstruction | Versioned archive | Realised weather is never a prediction-time feature; archive use is retrospective only | CANDIDATE / RESEARCH ONLY |
| `SRC-VENUE-ORIENTATION-*` | Ground or stadium orientation, dimensions, altitude, surface and roof state | V3/V4 official venue or competition source | Required before any wind direction can be resolved into a scoring-end or kicking effect | CANDIDATE |


Wind direction is only meaningful once it is resolved against the ground's orientation. A forecast row carrying `wind_direction_10m` and a venue row carrying orientation are two different fields from two different owners, and both are required before a wind claim is directional.


## 20. Derived and low-salience stat lanes


These are the fields that are available but routinely skipped. Each is a research lane only.


| Sport | Field | Owner / lane | Why it matters in the log |
|---|---|---|---|
| Baseball | In-stadium wind direction relative to the field, temperature, roof state, umpire crew, venue | `statsapi.mlb.com` `v1.1/game/{gamePk}/feed/live` exposes `gameData.weather` (`condition`, `temp`, `wind` including a field-relative bearing such as "Out To RF"), `gameData.venue.fieldInfo.roofType` and `liveData.boxscore.officials` | A field-relative wind bearing is a materially better carry/home-run input than a city forecast, and the plate umpire is a known strike-zone and pace factor. Both sit in the same official payload already used for schedule and lineups |
| Baseball | Park dimensions and park factors with their window | Official venue pages and league park data | Recorded as a versioned window, never a bare label |
| Cricket | Venue/format historical scoring baseline by innings order | Official scorecards, board-branded scorecards and `SRC-CRIC-CRICSHEET-JSON` | The computable fallback when no strip report exists; see §6 conditions ladder |
| Cricket | Dew point and cloud cover in the match window | `SRC-WX-*` | Dew and swing are conditions mechanisms with opposite signs; both were repeatedly asserted without a measurement |
| AFL / AFLW | Ground orientation, dimensions, roof state, near-bounce wind vector | AFL venue pages plus `SRC-WX-*` | End-by-end scoring in strong directional wind is a quarter-level variable |
| American football | Stadium orientation, roof state, surface, kick-window wind and gusts | Official club/venue pages plus `SRC-WX-GOV-NWS` | Kicking and passing respond to gusts and direction differently |
| Rugby league / union | Surface state, wet-weather handling conditions, goal-kicker identity and range | Official competition and club sources | The kicker is a scoring-composition variable, not a footnote |
| Soccer | Referee assignment where current data support a mechanism | Official competition appointment pages | Conditional only; used for cards/penalties and only with current evidence |
| Ice hockey | Confirmed starting goalie and blocked-shot treatment of the shot metric | Official league lineup releases and the provider's own definition | Both were decisive and unresolved in logged rank-#1 losses |
| Cross-sport | Rest days, travel distance and direction, altitude, turnaround length, kick/tip local time | Official schedules plus venue data | Each must enter through a named exposure or rate mechanism, never as a label |


## September 5 research-source and field-definition addendum


Register DSR-2026.09.05-v1.5; research-only discoveries and corrections. No source becomes APPROVED FOR FEATURE or H0 ingestion. Full exact URLs, observation limitations and conflicting values: [September 5 source register](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md#research-source-register).


| Lane | Successful use | Restriction / routing improvement |
|---|---|---|
| NRL current preview + dynamic match centre | Timestamped final-team changes, ceremonial entry explanation; official final and team/scoring stats | Refresh the same-day preview as well as static team list. ABC 50–22 headline lost to official 50–20. RLP citing official NRL is not a second independent lineage |
| CPBL official `stats.cpbl.com.tw/schedule/2026-A-307` and `...308` | Inning/pitcher/hit/error fields; home unplayed ninth identifiable | Distinguish starter runs charged, inherited runners and inning exposure; do not turn blank/unplayed home ninth into an observed scoreless inning |
| Liberty Times / Videoland, Chinese reporting | Named reporters and dated sequencing detail for CPBL games | Native-language first-hand reporting aids mechanism reconstruction; reports corroborating the same official box do not multiply statistical independence |
| ETPL-linked NV Play | Exact completed 12-over score, six-over checkpoint, four-over regulatory powerplay, toss and XI | Follow link from competition page. Static Cricbuzz/ETPL shells can be stale. Ball-by-ball delivery ordinal may include extras; legal-ball field needs completed-over/scorecard reconciliation |
| NDTV exact-match over comparison | South Africa 70/0 after six and subsequent cumulative over totals | Specialist phase source; TOI/MyKhel/other front ends may share a scorer. Contradictory live/stale widgets are not final phase evidence |
| FIBA official game page | Final/quarters/shooting percentages and source-defined player fields | Efficiency is not points; high totals do not establish pace. Retain unavailable possession/attempt reconstruction as missing |
| AFL league and official club hosts | Final/quarter scores, late warm-up report and native match identity | Match IDs are not portable across hosts. Match centre plus its report share league lineage. Preserve host+ID+date+participants |
| US Open official SlamTracker stats | Completed set sequence and point/serve/return statistics | Count set games, not tiebreak points. Use data fields rather than autogenerated narrative; no injury/fatigue inference from score alone |
| Xinhua + Titan Sports originals | Independently authored reports corroborate three China FA Cup finals/halves | Originality checked at byline/source level. Reprints of Xinhua are one lineage. Goals/halves can be research-settled under fallback, corners remain provisional |
| Sikkim / lower-league corners | Current specialist/club/timeline checks improve identity and open-field records | P-126 still conflicted; time-only and postponed entries cannot authenticate prior 1–0. GioScore 8–8 for Cannes has no admitted lineage. No manufactured corner total |


Save decisive fields with `observed_at`, source publication/update time if exposed, event owner, upstream lineage where known, field definition, endpoint and source limitation. If individual observation times were not captured, give the honest session window rather than invented minute precision. Source recommendation is field-specific, not a claim every article or future page from that domain is reliable.


## September 5(b) research-source addendum — P-294–P-305 second continuation


Register DSR-2026.09.05-v1.6; research-only discoveries and corrections from the settlement of `P-288`, `P-290`–`P-305`. No source becomes APPROVED FOR FEATURE or H0 ingestion.


| Lane | Finding | Routing improvement |
|---|---|---|
| `nrl.com` match-centre / draw pages | Automated `WebFetch` now redirects to `account.nrl.com/authorize` (an NRL account login wall) instead of returning page content | **Do not rely on `nrl.com` for automated (non-browser) final-score retrieval going forward.** Route to the ABC News NRL/NRLW Score Centre instead |
| ABC News NRL/NRLW Score Centre (`abc.net.au/news/sport/score-centre/nrl(w)/<date>/<slug>/<id>`) | Returned a correct, internally consistent final score on verbatim re-fetch for both `P-294` (NRLW) and `P-295` (NRL) | **Promoted to the preferred automated-fetch lane for NRL/NRLW finals**, ahead of `nrl.com` |
| `etplofficial.com/matches` (listing page) | A first, AI-summarised fetch produced an internally self-contradictory result for `P-300`'s Match 14 card (claimed the team that "won by runs" had batted second, which is definitionally impossible for that margin type). A second, literal/verbatim-quote fetch of the identical URL resolved correctly | **Always request a verbatim/literal quote from this URL**; treat any summarised first read as provisional pending a literal re-fetch. See RULES_CRICKET.md L-074 |
| `etplofficial.com` — powerplay/six-over splits | Neither `P-300` nor the still-live `P-305` could source an independently reproducible powerplay figure, despite the full-innings/full-match total sourcing cleanly in both completed cases checked this session | ETPL powerplay-level contracts should carry a standing evidence cap (`LOW` or below) distinct from the full-innings total, until a reproducible powerplay source is identified |
| `mykbostats.com` individual game pages (`mykbostats.com/games/<id>`) | Returned HTTP 403 to automated `WebFetch` this session | Do not rely on for automated retrieval. Sofascore and Korean-language news outlets remain the working KBO same-day lanes (L-067) |
| `sofascore.com` KBO/football match pages | Returned a correct, verbatim-consistent score for `P-296` (Doosan–SSG) on direct fetch; returned early/stale live-match snapshots (consistent across two fetches at different elapsed times) for `P-304` (Slavia–Zbrojovka), correctly indicating a genuinely live match rather than conflicting data | Reliable for both finals and live-state corroboration when two independent fetches agree on elapsed-time direction |
| Czech live-blog sources (`isport.blesk.cz`, `livesport.cz`) | Both returned early-match cached snapshots (0-0 at 6 minutes; 0-0 at 25 minutes) for the same fixture (`P-304`), consistent with each other and with the fixture's known kickoff time | Acceptable secondary live-state corroboration for Czech Chance Liga fixtures; not yet tested for a completed-match final score |
| Corners-market sourcing (soccer, all competitions) | `P-302`'s Bournemouth-corners row is the tenth consecutive corners contract in this log's history (after P-148, P-149, P-151, P-176, P-178, P-179, P-233, P-234, P-235) to end unresolved or provisional | Corners remains the single weakest-sourced market type in this framework. See RULES_SOCCER.md L-073 (structural Rank-#1 cap) |


No row in this addendum changes the global status: **no source or field is APPROVED FOR FEATURE and no H0 ingestion is authorised**.


## September 6 research-source addendum — the structured keyless API lane


Register `DSR-2026.09.06-v1.7`. Discoveries and re-grades from the `P-304`/`P-305` settlement and the closure of the `P-300`, `P-302`, `P-273` and `P-151` evidence gaps. **No source in this addendum becomes `APPROVED FOR FEATURE`, and no H0 ingestion is authorised.** Everything below is prediction-time and settlement-time research use, request by request.


### `SRC-ESPN-SITE-API-*` — new primary structured lane


```
https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/scoreboard?dates=YYYYMMDD
https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/summary?event=<eventId>
```


| Source ID | Permitted prediction/settlement role | Freshness | Restriction and gate | Status |
|---|---|---|---|---|
| `SRC-ESPN-SITE-API-SOCCER` | Confirmed starting XI, full bench, formation, referee, venue, attendance; **`wonCorners`**, possession, total/on-target/blocked shots, fouls, cards, offsides, saves, pass/cross/tackle/interception/clearance detail; final score and scorers | V0–V4; re-query at `G31` | Opta lineage; ESPN is a documented **data partner, not the competition's field owner** — an official league/club source controls on conflict. **Coaches are absent** (`rosters[].coach` is `null`). Corner definition is "corners won"; a differing operator definition controls settlement over this field | CANDIDATE / RESEARCH ONLY |
| `SRC-ESPN-SITE-API-CRICKET` | **`Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` per innings**; toss note in the form `"<Team> , elected to <bat\|field> first"`; innings totals with runs/wickets/overs, target and `winner` flag; both playing XIs; full batting/bowling matchcards with dismissal types; debutants | V0–V4 | The `<league>` path segment is the **ESPNcricinfo series ID** (e.g. `1547871` for ETPL 2026), not a slug. `cricket/scoreboard` **without** a series ID returns 404. Host board/competition controls on conflict | CANDIDATE / RESEARCH ONLY |
| `SRC-ESPN-SITE-API-BASEBALL` | **`injuries[]`** — per-team list with player, status (`Day-To-Day`/`10-Day-IL`/`15-Day-IL`/`60-Day-IL`) and body part; **`gameInfo.officials`** — full umpire crew by position; plays, at-bats, win-probability series | V0–V2; re-query at `G31` | Corroboration lane for availability only — the club/league transaction wire remains the field owner for a same-day activation or scratch. The umpire crew licenses **no** rate adjustment without a validated model | CANDIDATE / RESEARCH ONLY |


**Verified coverage, 2026-09-06 (HTTP 200):** `soccer/eng.1`, `soccer/ita.coppa_italia`, `soccer/arg.1`, `soccer/fra.2`, `soccer/chn.1`, `soccer/mex.copa_mx`, `soccer/usa.usl.1`, `cricket/<seriesId>`, `baseball/mlb`.


**Verified NON-coverage, 2026-09-06 (HTTP 400 on the league slug) — recorded so no future session repeats the search:**


| Competition | Slugs tried | Cards affected |
|---|---|---|
| Liga MX Femenil | `mex.w.1`, `mex.femenil`, `mex.liga_mx_femenil` | `P-148` |
| MLS NEXT Pro | `usa.nextpro`, `usa.mlsnp`, `usa.nps`, `usa.mls.next_pro` | `P-149` |
| Championnat National (FRA tier 3) | `fra.3`, `fra.national` | `P-176`, `P-178`, `P-179` |
| China FA Cup | `chn.fa`, `chn.cup`, `chn.fa_cup` | `P-233`, `P-234`, `P-235` |


**Access note (important, and counter-intuitive):** sending a browser `User-Agent` header produced `403 Forbidden`; the default client with no custom `User-Agent` succeeded. Do not "improve" the request by adding browser headers.


### Re-grades and new exclusions


| Source | Prior grade | New grade | Evidence |
|---|---|---|---|
| `api.sofascore.com` (programmatic) | Working KBO/soccer lane (Sept 5(b)) | **BLOCKED** — `403 Forbidden` on every route tested | Verified 2026-09-06. Interactive page fetches may still work; API access does not. The Sept 5(b) row above is superseded for programmatic use only |
| `sportscafe.in` "AI Simulation" articles | Unregistered | **PROHIBITED as a settlement source; tier E for all purposes** | Produced a fully fabricated `P-305` report — wrong winner, wrong margin, wrong venue, wrong player of the match — indexed alongside genuine scorecards. See `L-079` |
| Any article whose title, byline or body carries `AI Simulation`, `simulated`, `projected result`, `prediction`, `preview`, `who will win`, `Dream11`, `fantasy tips`, `expert tips` | Unregistered | **PROHIBITED as a settlement source** | Generalisation of the above. The exclusion attaches to the **article**, not the domain: a site may publish genuine reporting alongside synthetic pieces |
| `etplofficial.com` powerplay/six-over splits | "no reproducible powerplay source"; standing evidence cap on ETPL powerplay contracts (Sept 5(b)) | **SUPERSEDED — cap withdrawn** | `SRC-ESPN-SITE-API-CRICKET` supplies the field reproducibly. `P-300` and `P-305` both settled from it |
| ESPNcricinfo `full-scorecard` and `match-overs-comparison` via `r.jina.ai` | Unregistered | **CANDIDATE — cross-check only** | Agreed exactly with the direct API on both ETPL matches, including the 60/1 and 28/3 powerplay figures and every fall-of-wickets entry. Prefer the structured API: a proxied page is summarised text and can be misread; a JSON field cannot |
| ČTK / `ceskenoviny.cz` | Unregistered | **CANDIDATE — Czech football reporting (named reporting tier)** | For `P-304` returned full-time score, half-time score, all four scorers with minutes, both starting XIs, substitution minutes, both head coaches and the referee **in a single fetch** — more decision-relevant fields than any English-language source returned. Validates the `v3.4` native-language requirement |
| `isport.blesk.cz` live-blog article URLs | Live-state corroboration only (Sept 5(b)) | **Upgraded — also usable for completed-match corroboration** | The same article URL's progressive headline sequence (`0:0` → `1:0. Chorý proměnil penaltu!` → `3:0` → `4:0`) independently established the half-time score and the first-goal minute for `P-304` |


### Acquisition-order consequence (`L-080`, `G10.1`)


The access ladder in §4 of `RULES_GENERAL.md` previously began at "official structured feed/API or match centre" but the operational guide's acquisition order did not require a structured endpoint to be tried **before narrative pages**. It now does. Four rows that had been recorded as unresolvable after extensive narrative searching closed in one request each once the structured layer was queried. The lesson is not that the previous passes searched too little — they searched honestly and recorded failure honestly — but that they searched the wrong layer.


## September 6(c) addendum — unresolved-rate tracking by market/source tier (`L-093`, external blindspot audit `B-07`)


Registered per `LEARNING_REGISTER.md` `L-093`: unresolved/provisional rows are not missing at random, and the rate at which a given market or competition fails to settle cleanly is itself a standing quality signal, tracked here rather than re-discovered per card.


| Market / competition class | Unresolved rate observed in this log (as at 2026-09-06) | Structural cause |
|---|---|---|
| Soccer corners, competitions **not** covered by `SRC-ESPN-SITE-API-SOCCER` (Liga MX Femenil, MLS NEXT Pro, French tier 3, China FA Cup) | 8 of 8 rows attempted remain unresolved (`P-148`, `P-149`, `P-176`, `P-178`, `P-179`, `P-233`–`P-235`) | No structured provider reachable; see the verified non-coverage list above |
| Soccer corners, competitions covered by `SRC-ESPN-SITE-API-SOCCER` | 0 of 3 rows attempted remain unresolved (`P-151`, `P-273`, `P-302` all closed 2026-09-06) | Structured provider available |
| Cricket phase/powerplay totals, competitions covered by `SRC-ESPN-SITE-API-CRICKET` | 0 of 2 rows attempted remain unresolved (`P-300`, `P-305` both closed 2026-09-06) | Structured provider available |
| Ice-hockey overtime/shootout action terms | 2 of 2 rows attempted remain open (`P-166`, `P-200`) | Contract-terms gap, not a sourcing gap — no operator terms were ever supplied; see `G36.1` |
| Cricket reduced-overs/DLS action terms | 1 of 1 row attempted remains open (`P-217`) | Same as above |


**How to use this table.** Before researching a niche row in an unlisted competition, check whether its market class already has a documented high unresolved rate here. A high rate is not a reason to skip research, but it is a reason to budget less confidence into the row from the outset and to name the settlement endpoint (`G10.2`) before, not after, researching the mechanism. Update this table whenever a new market/competition combination is attempted, whether it resolves or not.


## September 5 user confirmation — controlling eligibility correction


[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md). The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.


Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.


The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.


Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.


Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.


## 2026-09-06(f) — settlement and retrospective addendum


[Event-specific source table and limitations](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#general-learnings-rule-changes-observations-and-sources). Newly demonstrated coverage: official Chance Liga event 8382 supplies P-304 corners (Slavia 5, Brno 1), team/bench and substitution fields; it declares Stats Perform lineage. ESPN soccer mex.1/event 401876990 supplies P-290 corners (Juárez 1, Pachuca 3). No feature-admission approval is implied.


ESPN cricket 1547871/event 1547886 freshly confirms P-305 toss/PP/innings. ESPN cricket 1534175/event 1534200 confirms P-217 revised innings and mandatory PP **24/2 in 4.5**, not six overs. ESPN/ESPNcricinfo related endpoints count as one lineage. A cricket league-0 timeout is a failed request, not proof of non-coverage; the specific series routes succeeded.


Fresh supporting sources include official CPL and Wofford reporting, the official AFL P-315 report, MLB StatsAPI event feeds, completed Tennis.com match records and a named Xports News KBO venue report. KBO's official body was unpopulated; other human-report re-fetches were limited. A surfaced Nate `[AI상보]` report was excluded; “Nate + another hostname” is not automatically two independent sources. Earlier categorical HTTP/coverage claims are narrowed to their actual tested routes. Remaining eight corner fields are unconfirmed; no failed fetch upgrades a provisional result.


## 2026-09-09 — sources demonstrated during the `P-333`–`P-344` reconciliation


Card mapping: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09". Compact table in `SOURCES.md` §"2026-09-09". No source below reaches `APPROVED FOR SNAPSHOT`/`APPROVED FOR FEATURE`; all are prediction-time research / settlement lanes and this consolidation does not change the numerical-approval gate (§16).


**Field-owner lanes newly exercised.**
- **Asian Cricket Council** — `asiancricket.org/match/<id>`. Field-owning scorecard/innings-state for ACC competitions (2026 Women's T20 Asia Cup, `P-333`, `P-343`). `CANDIDATE`. Native competition body; preferred ahead of aggregators for ACC finals. Reinforces `L-067` where the local board is the field owner.
- **FIBA** — `fiba.basketball/en/events/<event-slug>/games/<id>` (game center report) and `.../teams/<team>/<playerId>` (player profile with per-tournament minutes/stats). Field-owning result + player minutes + tournament context for FIBA national-team competitions (`P-334`, `P-344`). `CANDIDATE`. The player-profile lane independently confirmed a post-hoc minutes fact (Saki Hayashi 8 minutes, `P-344`) that mattered to the retrospective's aleatory-shock classification (`L-117`).
- **KBO** — Korean-language official news + `koreabaseball.com` scoreboard remains the field owner for KBO finals/match detail (`P-339`); the official body page is still frequently slow/unpopulated. **SBS English** (`news.sbs.co.kr/english`) provided an accurate, independent English-language confirmation of the `P-339` final, starter line and home runs — recorded as a usable English rung for KBO / K League 1 when the Korean field-owner page is unavailable, not a replacement for it.


**Research-only / cross-check lanes (secondary; never settle a niche derivative alone — `G10.2`/`L-081`).**
- **PlaymakerStats / zerozero / ceroacero / leballonrond / playmakerstats** family — post-final structured soccer fields (shots, SOT, corners, xG where present). Used for `P-336`/`P-337` post-match context and for the Part-2 `P-178-C05`/`P-176-C05` appendix update. Declares Stats Perform lineage on some competitions. **Still secondary** — aggregator agreement across this family does not promote a niche corner field whose provider/definition was never frozen. Frequently returns HTTP 403 to `WebFetch`; content recoverable via `WebSearch` result snippets.
- **Futbol24** (`futbol24.com`) — minute-by-minute event timelines including reconstructable corner events (`P-340`). Provenance-clear cross-check only.
- **Forebet** post-final corner display — corroborates niche corner counts in sparse competitions (`P-342-C03` 1–15; Part-2 `P-178` 8–8). Secondary; cannot repair an unfrozen operator/provider definition.
- **Kawowo Sports** (`kawowo.com`) — specialist current Uganda football result + goal timeline when the league official match detail is sparse (`P-341`). Goal timeline reliable; **not** automatically a corner-stat field owner. **GHANAsoccernet** (`ghanasoccernet.com`) corroborated it independently for `P-341`.
- **matchcalendar.football** — independent K League 1 result/scorer cross-check (`P-340`). Secondary aggregator.
- **`site.api.espn.com` public web renderer** (`espn.com/fiba/boxscore`, `/soccer/match`, `/mlb/game`) — independent final confirmations for `P-335`/`P-336`/`P-337`/`P-338`/`P-344`. Same lineage as `SRC-ESPN-SITE-API-*` (`SOURCES.md` §2); the `fiba` box-score route is exposed on the public web renderer and is a reliable settlement cross-check.


**Route-specific access observations (2026-09-09, not universal):** `ceroacero.es`, `forebet.com`, `sofascore.com` match pages returned **HTTP 403** to `WebFetch`; their content was still recoverable through `WebSearch` result snippets. Consistent with the standing `api.sofascore.com` `BLOCKED` grade. No niche corner field was upgraded from any of these — `P-341-C03` remains `UNSETTLEABLE` to standard and `P-342-C03` `PROVISIONAL`.


### 2026-09-09(b) — `SRC-ESPN-SITE-API-SOCCER` coverage probe for the two open corner rows


`RULES_SOCCER.md` control 10 requires retrying official/data-partner sources after the final before an `UNSETTLEABLE` verdict, and `G10.2` requires confirming the structured provider carries **this competition**. The earlier pass in this session had tested only aggregator pages (all 403) and not the primary lane. Closed here. Method: direct `curl` to `site.api.espn.com` (default client, per §2's access note), `soccer/eng.1` as positive control.


| Probe | Response |
|---|---|
| `soccer/eng.1/scoreboard?dates=20260908` (control) | HTTP **200** |
| `soccer/uga.1/scoreboard?dates=20260908` | HTTP **200**; `leagues[0].name` = **"Ugandan Premier League"** |
| `soccer/uga.1` — events on 2026-09-08 | **0** |
| `soccer/uga.1` — events 2026-09-01 → 2026-09-15 | **0** |
| `soccer/uga.1` — default scoreboard season state | `season.year` = **2025**, `season.type.name` = **"2025-26 Ugandan Premier League"**, **97** calendar entries, newest events dated **2026-05-23** (NEC–Calvary, BUL–Entebbe UPPC, Mbarara–KCCA, Police–Kitara, Maroons–Lugazi, UPDF–SC Villa, Express–Vipers) |
| `soccer/svk.1`, `svk.2`, `svk.cup`, `svk.slovnaft_cup`, `svk.slovak_cup`, `svk.slovakia_cup`, `svk.fortuna_liga`, `svk.super_liga`, `slk.1`, `slovak.1` | HTTP **400** on all ten |
| `sports.core.api.espn.com/v2/sports/soccer/leagues?limit=1000` | `count` = **218**, 218 items returned (complete). No Slovak competition present. **No `uga.1` present either.** Only sub-Saharan African entry: `rsa.1` |


**Finding 1 — distinguish "covered but stale" from "not covered."** ESPN carries the Ugandan Premier League and `wonCorners` is a league-level capability of this lane, but as at 2026-09-09 the feed had not rolled to 2026-27. `P-341-C03`'s fixture is therefore absent for a **season-rollover** reason. This yields a concrete, checkable retry trigger (re-query `uga.1` for `dates=20260908` once the feed advances) rather than an open-ended one. A stale-season state must never be recorded as competition non-coverage — the two have different retry semantics and different implications for future cards in that competition.


**Finding 2 — the core league directory is not authoritative for what the site API serves.** `uga.1` is served by the site API with a real league name while being **absent from the complete 218-league core directory**. Had the directory been used as the coverage test, Uganda would have been wrongly written off. **Standing rule: probe the site API directly; use the core directory only as corroboration.** Slovakia fails *both* tests — ten site-API slug forms and the directory — which is why that non-coverage conclusion is treated as solid, whereas a directory-only absence proves nothing. This also narrows the 2026-09-06 practice of inferring competition-wide non-coverage from a small number of slug guesses: a 400 is evidence about the **tested route**, and a genuine non-coverage claim now wants both lines of evidence.


**Dispositions unchanged by this probe:** `P-341-C03` `UNSETTLEABLE` (`TMP-OPEN-20260909-01`), `P-342-C03` `PROVISIONAL RESEARCH WIN` (`TMP-OPEN-20260909-02`). No W/L or Brier booked for either.


## 2026-09-11 — sources demonstrated during the `P-345`–`P-371` reconciliation


Card mapping: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-11". Compact table: `SOURCES.md` §"2026-09-11". No source below reaches `APPROVED FOR SNAPSHOT`/`APPROVED FOR FEATURE`; the numerical-approval gate (§16) is unchanged.


### `SRC-UEFA-MATCHSTATS` — new field-owner lane for UEFA club competitions


- **Endpoint:** `https://matchstats.uefa.com/v1/team-statistics/{matchId}` — `matchId` is the number in the UEFA match URL (e.g. `2049556` from `uefa.com/uefachampionsleague/match/2049556--club-brugge-vs-aston-villa/`).
- **Shape:** a JSON array with **one entry per team** (`teamId`, `statistics[]` of `{name, value}`), identifying its data provider as FAME. Fields used: `goals_scored`, `goals_conceded`, `corners` (with `corners_left`/`corners_right`), `attempts`, `attempts_on_target`, `ball_possession`, `played_time`.
- **Access (2026-09-11):** keyless; `curl` with the default client returned ~350 KB per match. **The WebFetch summariser reported only the first array entry** — always parse the raw JSON.
- **Demonstrated:** `2049556` Brugge–Villa (Brugge corners 4, Villa 5; attempts 14/21) settled `P-345-C03`; `2049558` AEK–LASK (corners 7/3) settled `P-346-C05`; `2049568` Fenerbahçe–Roma (1–1) verified the collision record.
- **Conflict record:** where media secondaries disagreed, UEFA's feed sided with neither consistently — VI (Brugge 3) was wrong on `P-345`, the Guardian (LASK 4) was wrong on `P-346`. Both errors were **exactly one corner**, which is the margin that decides most corner rows.
- **Grade:** `CANDIDATE — FIELD OWNER` for UEFA club-competition settlement (corners, shots). Pre-register it on every UEFA derivative row (`RULES_SOCCER.md` control 30).


### FotMob match pages via `r.jina.ai` — structured secondary with wide coverage


- **Route:** `https://r.jina.ai/https://www.fotmob.com/matches/<slug>/<hash>`. The page renders a stats table (possession, total shots, shots on target, corners; xG where FotMob carries it) plus FT/HT and scorers. Direct FotMob/Sofascore API routes remain `BLOCKED`.
- **Demonstrated:** Australia Cup SF (Sydney 5 – Victory 4 corners; the card's pre-registered provider, so `P-355-C05` is settled); UAE Pro League (Al Jazira 6–3; United 5–6 corners — agreeing with Forebet and M9Bet, three lineages in all).
- **Grade:** `CANDIDATE — STRUCTURED SECONDARY`. Opta-sourced. Settles a derivative only where the card named it before ranking; otherwise it is the strongest corroborating lineage, not the field owner.


### Reconfirmed or newly exercised


- **KBO English scoreboard** (`eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=YYYY-MM-DD`) — readable by the fetch tool; line scores and W/L/S pitchers (`P-356`, `P-362`). Field owner; the English rung under `L-067`.
- **FIBA game pages** — quarter scores, team 2P/3P/FT splits, biggest lead, lead changes (`P-358`, `P-367`, `P-371`). Field owner.
- **MLB statsapi** — `schedule?sportId=1&date=YYYY-MM-DD&hydrate=linescore` returned all four MLB finals by `curl`; **WebFetch received HTTP 406**. Next MLB card: test whether the live feed's `battingOrder` is populated before first pitch; if so it becomes the field-owner lineup route that `P-347`–`P-351` lacked (they recorded orders as `SECONDARY_ONLY`).
- **ESPNcricinfo** — direct fetch HTTP 403; via `r.jina.ai` it returned the live Test state (`P-364`) and the Windhoek T20I scorecards (228/4 and 217/3 on 4 Sep; 205/5 on 6 Sep). The proxy returned an identical live state twice about 40 minutes apart — treat proxy snapshots as possibly cached and cross-check the page's own time/state.
- **Cricket Ireland-branded CricketArchive** — full ETPL scorecards including both XIs, bowling figures and fall of wickets (`P-357` re-opened this pass). Reconfirmed as the ETPL settlement lane; the ETPL first-party page is status-only (stale for more than 24 hours after Match 19).
- **Tennis Abstract Elo** — `tennisabstract.com/reports/atp_elo_ratings.html` returned overall and hard-court Elo with a "last updated" date (2026-08-31). `BENCHMARK ONLY`: it may sit beside a winner probability as a coherence check (`RULES_TENNIS.md` control 13), never set it. A sports rating, not a market input — compatible with `SPORTS_ONLY / MARKET_BLIND`.


### Re-graded


- **Guardian and VI match-stat corner counts** → **cross-check only**; never settle a derivative within ±1 of its line (two conflicts, two errors of one corner).
- **ETPL first-party match page** → status field only.


### Access failures and coverage (route-specific, not universal)


- **ClubElo API** (`api.clubelo.com/<date>` and `/<club>`): **0 bytes** on http and https, with and without a browser User-Agent, from this environment. Not graded; would have supplied the cross-league prior `RULES_SOCCER.md` control 31 asks for. Retry from another client before relying on it.
- **ESPN `soccer/uga.1`**: re-probed 2026-09-11 — still season 2025, 0 events on 2026-09-08. `P-341-C03`'s retry trigger remains unmet.
- **A-Leagues match centre** renders no statistics to a fetch; **UAE Pro League match centre** shows corners as "–" — no field-owner corner lane for that league.
# Research source review - 2026-09-12


The current field-level routes, successful openings and limitations are in [SOURCES.md](SOURCES.md), [recent queue evidence](audit_2026-09-12/recent_queue_evidence.md), [historical queue evidence](audit_2026-09-12/historical_queue_evidence.md), [sport evidence](audit_2026-09-12/sport_evidence.md) and [recovered MLB records](audit_2026-09-12/recovered_mlb_evidence.md). They add original CPL newsroom, CPBL statistics, dated NPB roster/box, Toluca match-report and explicit MLB innings routes to future retrieval guidance; some are strengthened routes already known, not newly discovered providers.


Status for all: **RESEARCH ONLY / CANDIDATE; no new APPROVED FOR FEATURE source.** Licence/retention, automation, historical known-at reconstruction and complete field definitions have not been established for H0. The exact source record must retain event ID, date/time zone, phase, team ordering, owner, publication/retrieval times, observed fields and missing fields. Independence is recorded only where upstream provenance supports it; proxy/embedded duplication is not corroboration.


The missing P267 artifact does not justify claiming every P-241-P-267 detail is absent: mini log 8 retained substantial issued and retrospective material, now restored. Five later corner adjudications still lack reproducible evidence and have explicit TMP-AUDIT handles. A source-lane audit must inspect all supplied mini variants before declaring a document gap total.


Method references newly checked: [NIST binomial-proportion intervals](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm) and [ASA statement on threshold-based inference](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf). These support uncertainty practice, not a claim of sports model accuracy. [Controlling corrections](audit_2026-09-12/rule_corrections.md).


## 2026-09-15 — sources demonstrated during the `P-364` final settlement and the `P-373`–`P-423` import


Detail and card mapping: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-15" and §"2026-09-15(b)"; quick reference `SOURCES.md` §"2026-09-15(b)". None is `APPROVED FOR FEATURE`. Every access observation is route- and date-specific.


| Source ID (proposed) | Endpoint / record | Field(s) owned or used | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-PL-DATA-API` | `footballapi.pulselive.com/football/compseasons` → `/football/fixtures?comps=1&compSeasons=<int>&statuses=C` → `/football/stats/match/<fixtureId>` | EPL final score; per-team `won_corners`, `corner_taken`, `total_scoring_att` | `CANDIDATE — FIELD OWNER` | Needs `Origin` and `Referer: https://www.premierleague.com`; `compSeasons` as an integer (841 = 2026/27; `841.0` → HTTP 400). Settled P-402-C02/C03 (Tottenham 5, Everton 6) and P-408-C01 (Brighton 3). Matched ESPN exactly on both matches |
| `SRC-ESPN-SITE-API-SOCCER` (coverage extension) | `soccer/{bel.1, fra.1, ger.1, swe.1, esp.1, ita.1, jpn.1, uefa.champions}/summary?event=` | score, goal minutes, `wonCorners`, XIs + benches | `CANDIDATE` (existing) | Matched J.League official `CK` (P-387) and the Premier League record (P-402, P-408). Provisional-only for rows that did not pre-register it |
| `SRC-ESPN-SITE-API-SOCCER` (`gua.1`) | Guatemala Liga Nacional | score only | limited | Summary returned no statistics object — cannot settle corners (P-377-C02) |
| `SRC-ESPN-SITE-API-SOCCER` (`bhu.1`, `uae.1`, `are.1`, `uae.pro_league`, `uae.league`) | Bhutan, UAE | — | non-coverage (HTTP 400) | Bhutan (P-418) and UAE Pro League (P-368/P-369) have no route |
| `SRC-ESPN-SITE-API-AFL` / `-NRL` / `-NFL` | `australian-football/afl`, `rugby-league/3`, `football/nfl` scoreboards | finals, quarter lines | `CANDIDATE` | Re-verified P-386, P-388, P-396, P-397, P-376, P-412–P-414, P-422 |
| `SRC-MLB-STATSAPI-BOXSCORE` | `statsapi.mlb.com/api/v1/game/<gamePk>/boxscore` | starting pitcher, IP, R/ER, pitchers used | field owner (existing lane, new endpoint) | Confirmed all four P-416/P-420/P-421/P-423 starters. Use `curl` (WebFetch returns HTTP 406 on statsapi) |
| `SRC-NPB-ENG-BOX` | `npb.jp/bis/eng/2026/games/gm<YYYYMMDD>.html`, `s<gameId>.html` | final, line score, pitchers, HR | field owner (reconfirmed) | P-381–P-383, P-405, P-417 |
| `SRC-KBO-ENG-SCOREBOARD` | `eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=` | final | field owner (reconfirmed) | P-384, P-385 |
| `SRC-FIBA-GAME` | `fiba.basketball/en/events/<event>/games/<id>` | quarter scores, shooting, biggest lead | field owner (reconfirmed) | P-411 |
| `SRC-ESPNCRICINFO-SERIES` via `r.jina.ai` | `espncricinfo.com/series/<slug>/match-schedule-fixtures-and-results` and `/full-scorecard` | every series result; innings runs/overs; day-by-day close log | `RESEARCH` route | P-364; direct fetch HTTP 403. Check the page's own day log for staleness |
| `SRC-BBS-BT` | `bbs.bt` round reports | dated Bhutan Premier League results and standings | `RESEARCH` (new) | P-418 identity conflict (2026-09-15 report) |
| `SRC-BFF-BT` | `bhutanfootball.org` match reports | competition-owner reports | `CANDIDATE` (new) | Search listing undated — open each article for its date |
| `SRC-JLEAGUE-CLUB-RESULTS` | J.League official club result tables (`CK`) | J1 team corners | `CANDIDATE — FIELD OWNER` (found by log A) | P-387-C03 |
| `SRC-LALIGA-CLUB-EVENT-FEED` | Real Racing official match page with embedded LALIGA events | timeline, corners | `CANDIDATE` (found by log B) | P-398 |
| `SRC-LIGA-BANTRAB` / Guatefutbol | Liga Nacional official feed; Guatefutbol reports | final score; local narrative | owner (score) / secondary | no corner field |
| `SRC-SPORTNAVI-NPB` | Yahoo! Japan SportNavi | NPB native-language corroboration | secondary (found by log B) | P-405 11-inning detail |
| Statz, OFStats, PlayerStats, ScoreBat, FootyMetrics | match / corner pages | corroboration | `SECONDARY — never settles alone` (from log B) | agreed with ESPN on P-399/P-401/P-402 counts |
| Sofascore / AiScore web pages; Cricbuzz and NDTV via WebFetch | — | — | `ACCESS FAILED` (2026-09-15, route-specific) | retry via proxy |
| Web-search engine result summaries | — | — | **Excluded** | wrong numbers observed twice: England chase "132 for 2" (130/2), Spain top scorer "22" (FIBA 28) |


## 2026-09-16 — sources demonstrated during the queue retry and the C′ reconciliation


Detail: `PREDICTION_LOG_COMBINED_3.md` §"2026-09-16"; quick reference `SOURCES.md` §"2026-09-16". None is `APPROVED FOR FEATURE`; route observations are environment- and date-specific (2026-09-16).


| Source ID (proposed) | Endpoint / record | Field(s) | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-ESPN-SITE-API-CRICKET` (settlement path now documented) | `cricket/<seriesId>/scoreboard?dates=YYYYMMDD` → `cricket/<seriesId>/summary?event=<id>` → `notes[]` with `type = matchnote`, grouped by `section` (innings) | exact 0.1–6.0 powerplay runs/wickets per innings; 50/100 milestones; innings break; toss | `CANDIDATE — settles phase rows` | Settled P-406-C01/C04 (series 1547871, event 1547895, note 767111: Edinburgh 68/2). Documented here since 2026-09-06 but not consulted by two later passes (`G-L14`) |
| `SRC-ESPN-NFL-SEASON-REF` | `football/nfl/scoreboard?dates=2025&seasontype=2&week=N` + `summary?event=` → `scoringPlays[].type.text` | season margin distribution; return-TD frequency | `REFERENCE_BASE_RATE` lane | 2025: 272 games. Margin = 3: 15.1 %; = 7: 9.6 %. Non-offensive TDs 59 = 0.217 a game, ≥ 1 in 18.8 % of games (American football controls 18, 20) |
| `SRC-ESPN-SITE-API-SOCCER` `keyEvents[]` | same summary | red cards, penalties, goal minutes | `CANDIDATE` — disruption facts at settlement (soccer control 34) | P-408 red 53'; P-419 reds 59'/86'/90+10' |
| `SRC-MLB-STATSAPI-FEEDLIVE` | `statsapi.mlb.com/api/v1.1/game/<gamePk>/feed/live` | inning line score, every pitcher line, HR plays, weather (condition, temperature, field-relative wind), umpires | field owner (existing lane, fuller endpoint) | Verified P-416/P-420/P-421/P-423; caught C′'s P-421 error |
| `SRC-BUNDESLIGA-MATCH-STATS` | `bundesliga.com/en/bundesliga/matchday/<season>/<md>/<slug>/stats` | would own Bundesliga corners, shots, possession | **`JS_ONLY / BLOCKED`** | Direct HTTP 403 ("Forbidden for non bundesliga top level usage"). `r.jina.ai` raw text: every statistic 0 (unrendered). A WebFetch summary reported "7–7 corners, 62 %, 12 shots" — not present on the page → excluded (`G-L13`) |
| `SRC-ALLSVENSKAN-MATCH` | `allsvenskan.se/matcher/<year>/<id>/<slug>` | Allsvenskan match facts | `JS_ONLY` (cookie wall in raw text) | P-419 (`6529990`) |
| `SRC-LIGUE1-LIVE` | `plus.ligue1.com/live/<id>`; `ligue1.com/fr/feuille-de-match/l1_championship_match_<id>/summary` | Ligue 1 match facts | `JS_ONLY` (empty raw text) | P-409 (`306887`) |
| `SRC-PROLEAGUE-MATCH` | `proleague.be/wedstrijden/seizoen-<yyyy-yyyy>-jupiler-pro-league-<md>-<home>-vs-<away>` | Pro League match facts | `NOT FOUND` for 2026-27 (slug 404; 2025-26 pages exist) | P-407 |
| `SRC-SKY-IT-TABELLINO` | `sport.sky.it/calcio/serie-a/partite/<year>/giornata-<n>/<slug>/tabellino-statistiche` | Serie A match stats incl. corners | `SECONDARY` (broadcaster; provider not stated) | P-399 8–9, same as ESPN; not a settlement record |
| `SRC-RSSSF` | `rsssf.org/tablesb/<country><year>.html` | round-by-round fixtures, results and tables; "Last updated" footer | `RESEARCH` (new) | Bhutan 2026 Round 15 [Sep 14] Drukpa – RTC unscored; updated 11 Sep 2026. Plain HTML — read raw |
| `SRC-BBS-BT` (metadata note) | `r.jina.ai/https://www.bbs.bt/<id>/` | `Published Time` | `RESEARCH` | 244138 = 2026-07-12; 244289 = 2026-07-17 (the report earlier cited as "2026-09-15"). Always read the date from metadata |
| `SRC-NFL-COM-PLAYER-LOGS` | `nfl.com/players/<slug>/stats/logs/<year>/` | player game logs | `CANDIDATE — field owner` (found by C′) | Not re-opened this pass |
| Reuters match reports; club match reports (Brighton); Guardian match stats; StatMuse FC; SoccerNews; Global Sports Archive; RedScores | narrative / stat displays | — | `SECONDARY` — narrative or corroboration only (found by C′) | Guardian/StatMuse/SoccerNews Leipzig corners 7 v ESPN 8 |
| Pro-Football-Reference via proxy | season tables | — | `ACCESS BLOCKED` (security verification page) | Not bypassed |
| WebFetch output (model summary) | — | — | **Excluded as a record** (`G-L13`) | Invented Bundesliga corner numbers; misdated a BBS article |


### Unresolved-rate tracking update (continues §"September 6(c)")


| Market / competition class | Status 2026-09-16 | Cause |
|---|---|---|
| Soccer corners where ESPN covers the league, no keyless official record exists, and the card did not pre-register ESPN (Serie A, Allsvenskan, Pro League, Ligue 1, Bundesliga) | 7 of 7 rows open (P-399-C02, P-401-C01/C03, P-407-C01, P-409-C02, P-410-C05, P-419-C05) | Provider not frozen at issue → soccer control 35 |
| Soccer corners in competitions with no route at all (UAE, Uganda, Guatemala, Slovakia) | 5 of 5 open (P-341, P-342, P-368, P-369, P-377) | No route |
| Cricket phase rows covered by `SRC-ESPN-SITE-API-CRICKET` | 0 of 3 open (P-300, P-305, **P-406** closed) | Route exists — consult it |


### 2026-09-16(b) — lanes exercised while re-probing the documentary-audit rows


| Source ID (proposed) | Endpoint / record | Field(s) | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-UEFA-MATCH-FINDER` | `match.uefa.com/v5/matches?fromDate=&toDate=&competitionId=&offset=0&limit=100` | `matchId`, kickoff, teams, round, and the score breakdown `regular` / `total` / `penalty` / `aggregate` | **`CANDIDATE — FIELD OWNER`** (new) | Keyless. `offset` is mandatory (HTTP 404 without it). `competitionId` 28 = UEFA Women's Champions League, 1 = UEFA Champions League. Supplies the `matchId` that `SRC-UEFA-MATCHSTATS` needs, and the **90-minute (`regular`) score** — decisive for extra-time ties (P-255, P-256) |
| `SRC-UEFA-MATCHSTATS` (scope caveat added) | `matchstats.uefa.com/v1/team-statistics/<matchId>` | corners, attempts, possession, `played_time` | field owner, **whole-match scope** | `played_time` 137 (P-255) and 115 (P-256) include extra time. A 90-minute contract settles only as `PERIOD_SCOPE_BOUNDED` (`RULES_GENERAL.md` §16.11(q), soccer control 36) |
| `SRC-ESPN-SITE-API-SOCCER` (`ita.coppa_italia`) | `summary?event=401911806` | `wonCorners` | `CANDIDATE` (reconfirmed) | Sassuolo 6, Frosinone 5 = 11 (P-251-C05, threshold-invariant) |
| `SRC-ESPN-SITE-API-SOCCER` (`concacaf.leagues.cup`) | `summary?event=401914297` | `wonCorners`, `keyEvents` | `CANDIDATE` (new slug verified) | Toluca 4, León 5 = 9 (P-265-C05, exactly at the threshold). `concacaf.leagues_cup` / `usa.leagues_cup` → HTTP 400 |
| `SRC-ESPN-SITE-API-SOCCER` (`uefa.wchampions`) | scoreboard | — | covered, **no qualifying events** | HTTP 200, 0 events for 1–4 Sep 2026 |
| ESPN non-coverage re-probe | `chn.fa`, `chn.cup`, `chn.fa_cup`, `chn.super_cup`, `chn.2`, `mex.w.1`, `mex.femenil`, `mex.liga_mx_femenil`, `usa.nextpro`, `usa.mlsnp`, `fra.3`, `fra.national`, `ind.sikkim` | — | **non-coverage confirmed 2026-09-16** (all HTTP 400) | P-250 and the nine Part-2 rows stay routeless |


**Unresolved-rate consequence.** Of the five documentary-audit corner rows, four became reproducible once the right lane was queried (P-251, P-255, P-256, P-265) and two of those settled at a field owner. The binding constraint was never the passage of time — it was that the lane had not been tried (`G-L14`).




## 2026-09-17 — sources exercised during the `P-424`–`P-437` import


Quick reference: `SOURCES.md` §"2026-09-17". None is `APPROVED FOR FEATURE`.


| Source ID (proposed) | Endpoint / record | Field(s) | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-ESPN-SITE-API-SOCCER` (`afc.champions`) | `soccer/afc.champions/scoreboard?dates=` → `summary?event=` | ACLE finals, `wonCorners`, `keyEvents` goal minutes, possession, shots | **`CANDIDATE` — coverage newly verified** | Five ACLE MD1 fixtures verified 2026-09-17, corners included (Daejeon 4–3, Gamba 1–3, Al Ain 2–10, Kashiwa 6–0, Port 4–4). Partner display — pre-register it on the card to make it a settling route (§16.10(j)) |
| `SRC-JLEAGUE-ACLE` | J.LEAGUE ACLE match-data route and club records (`CK`) | Corners and match data for ACLE fixtures with J.LEAGUE clubs | **`CANDIDATE — FIELD OWNER`** for those fixtures | Settled `P-425`, `P-426`, `P-436` corners |
| `SRC-AFC-MATCH-REPORT` | AFC official ACLE match reports | Score, scorers, narrative | field owner — **score only** | Publishes **no corner field**; `P-430-C05` stays open because the card pre-registered this record for a derivative it does not carry |
| `SRC-ESPN-SITE-API-CRICKET` (ETPL) | `cricket/1547871/summary?event=` → `notes[]` matchnotes | Innings totals, toss, exact 0.1–6.0 powerplay | `CANDIDATE` (third successful use) | `P-424` 48/2 and `P-428` 54/2 reproduced exactly |
| `SRC-KBO-ENG-SCOREBOARD` | `eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=` | KBO finals | **`ACCESS DEGRADED` 2026-09-17** | 174 bytes direct, 385 via proxy; `mykbostats` and Naver JS-only; no ESPN KBO route. Re-grade to field owner only after a successful raw retrieval |
| `SRC-KOREAN-ONSITE-REPORTS` | fnnews, SPOTV, SportsChosun, OSEN, Nate | KBO finals, pitcher lines, roster/workload | `RESEARCH` — named reporting (`L-067`) | Carried four finals this pass; independence between outlets not established |


**Unresolved-rate consequence.** Derivative settlement continues to be the binding constraint, not score settlement. `P-430-C05` is the fourteenth open corner row in the log, and the first whose failure cause is specifically *an official report that does not publish the field* rather than an unreachable competition. Record derivative field availability — not merely competition coverage — when pre-registering a route (`G-L14`).


## 2026-09-17(b) — sources exercised during the `P-438`–`P-451` import


Quick reference: `SOURCES.md` §"2026-09-17(b)". None is `APPROVED FOR FEATURE`.


| Source ID (proposed) | Endpoint / record | Field(s) | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-ESPN-SITE-API-SOCCER` (**`afc.cup`**) | `soccer/afc.cup/scoreboard?dates=` → `summary?event=` | **AFC Champions League Two** finals, `keyEvents` goal minutes and **red cards**, `wonCorners`, `totalShots`, `shotsOnTarget`, `possessionPct` | **`CANDIDATE` — new lane, verified 2026-09-17(b)** | `leagues[0].name` self-identifies as "AFC Champions League Two". **Every intuitive slug fails with HTTP 400** (`afc.champions_two`, `afc.champions.two`, `afc.acl2`, `afc.champions_league_two`, `afc.champions2`); only `afc.cup` resolves. Verified events 401912815 (`P-438`) and 401912814 (`P-439`). **Emits no `Halftime` key event** — reconstruct HT from goal minutes. Partner display: pre-register to settle (§16.10(j)) |
| `SRC-MLB-STATSAPI-SEASON` | `statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=&endDate=&gameType=R&hydrate=linescore` | **Season-scale base rates**: final margins, totals, per-venue distributions, `currentInning` vs `scheduledInnings` (extras), inning-by-inning regulation splits | **`CANDIDATE — FIELD OWNER`, new use** | Six monthly calls (~2 MB each) covered all of 2026 through 16 Sep, **n = 2,286**. Produced every figure in `RULES_BASEBALL.md` controls 34–37: `P(margin = 1)` 27.8%; `r` by strength gap 22.9–30.1%; `P(extras)` 8.75%; `P(margin = 1 \| extras)` 68.5%; extras runs added mean 2.88; max integer push 11.5%; park share of total-runs variance 4.3%. Also settled the `P-443`/`P-444` regulation splits (4–4 and 2–2). **Refresh per season; record `n` and retrieval date on any card citing it.** The `fields=` filter silently drops `linescore` — use `hydrate=linescore` instead |
| `SRC-LNBP-CLUB-RESULTS` | `lnbp.mx/<Team>/team_results.html` (and `lnbp.mx/scores.html`), **rendered** | LNBP per-Jornada finals | **`CANDIDATE — FIELD OWNER`; `JS_ONLY — RENDER REQUIRED`** | `curl` → **HTTP 200, ~16 KB JS shell, zero scores** (`src="js/coffee.instance.js"`, jQuery); rendered → finals with a Jornada selector. *Jornada 20* = **Dorados 97 – El Calor 86**, closing `P-451`. **Supersedes the "HTTP 403" note** in `RULES_BASKETBALL.md` §9.5 for results. Finals only: no regulation packet on the domain, so `BK-P1` is unchanged. Do not promote to a structured-stat source |
| `SRC-ESPN-SITE-API-CRICKET` (**CPL series `1534175`**) | `cricket/1534175/scoreboard?dates=` → `summary?event=1534214` → `notes[]` matchnotes | Innings order (`section`), exact `Powerplay 1: Overs 0.1 - 6.0` per innings, strategic timeouts, milestones, XIs | `CANDIDATE` (fourth successful use) | Verified `P-445` end to end. **This series ID was already recorded in this register from `P-217` and was not consulted before searching** — the `G-L14` miss is the finding, not the route |
| `SRC-ESPN-SITE-API-SOCCER` (`uefa.europa`) | same shape | UEL finals, **explicit `Halftime` key event**, goal minutes, shots, corners | `CANDIDATE` (reconfirmed) | `P-440` HT 0–2 / 1–4 and `P-441` HT 0–0 / 1–0 (88') reproduced exactly. **Date ranges are unsupported** — `dates=YYYYMMDD-YYYYMMDD` returns a gzip error blob, not a range |
| `SRC-ESPNCRICINFO-HS-CONSUMER` | `hs-consumer-api.espncricinfo.com/v1/pages/matches/{current,results,live}` | match index | **`ACCESS DENIED` 2026-09-17(b)** | HTTP 403 with an Akamai-style deny page on all three paths. Does not affect `site.api.espn.com/.../cricket/<seriesId>/…` |
| `SRC-CRICKETWORLD-SCORECARD` | `cricketworld.com/cricket/<fixture>/match/scorecard/<id>` | CPL scorecards | **`NOT REPRODUCIBLE`** | Cloudflare "Performing security verification" interstitial through `r.jina.ai` (543-byte body). The mini log cited this URL as its `P-445` settlement source; it cannot be re-opened by this repository's ladder |
| `SRC-ESPN-CORE-CRICKET-LEAGUES` | `sports.core.api.espn.com/v2/sports/cricket/leagues?limit=500` | (attempted) series discovery | **EMPTY — `count: 0`** | There is **no discovery endpoint for cricket series IDs.** They come from this register or from a scorecard URL. This is the structural reason `G-L14` requires the register to be read before searching for a route |


**Unresolved-rate consequence.** For the first time in Part 4 the binding constraint was **not** derivative settlement: all fourteen records were verified from raw records, no row was force-settled, no new open handle was created, and the one open item (`P-451`'s final) was **closed** by a rendering escalation. The cohort's failures were analytical (margin arithmetic, extras endpoint, push mass, slate correlation), not retrieval failures. Two retrieval defects remain and both are `G-L14` execution rather than availability: the CPL series ID was in this register and was searched for instead, and `lnbp.mx` was graded unreachable when it was merely unrendered.


**Field-availability note, extending the 2026-09-17 entry.** Record, per route, **which fields it publishes**, not merely which competitions it covers. Three routes in this import carried the score and nothing else (AFC report, AP/Reuters, MLB recaps), and in each case the decisive field lived elsewhere: the red card and shot counts in the ESPN feed, the regulation split in the MLB linescore. `G-L23` now requires the process record at settlement, so the process feed must be registered alongside the settlement route.


## Numerical source admission clarification — 2026-09-17


Prior season-scale MLB retrieval is retrospective reference evidence, not a quality-approved H0. A general CANDIDATE or field-owner label does not admit numerical features. For each admitted field record target/endpoint, exact source and schema, available_at versus retrieved_at, revisions, population/missingness, joins and access constraints. Require actual pre-cutoff snapshots for historical pregame features; current corrected labels may be used only with their reconstruction status declared. Completed-season winner-minus-loser W% strata are descriptive and cannot be silently back-joined as pregame covariates. No new external source was queried or promoted during this Markdown implementation. Existing key-number/base-rate records are uncertain references, never universal conditional limits. Publication includes prospective shadow under NUMERICAL_PROGRAM.


## 2026-09-19 — social-media lanes tested directly, and three structured lanes added


Prompted by a direct question: *should reporters, journalists, team accounts or league accounts on X/Twitter or Reddit be used for starting line-ups and stats?* Every route below was **tested in this pass**, not assumed. The short answer is that the two named platforms are unusable, the third has a serious identity problem, and the fields wanted are already available — better — from structured endpoints.


### Social platforms — tested 2026-09-19


| Route | Result | Verdict |
|---|---|---|
| `x.com/<handle>` direct | **HTTP 200, but a login wall.** 220 KB of markup containing **1,644 characters of visible text** — "Log in / Sign up", the profile name and a post count. **Zero post content.** | **UNUSABLE** |
| `cdn.syndication.twimg.com/timeline/profile?screen_name=` | **HTTP 200, 0 bytes.** The legacy unauthenticated timeline lane returns an empty body | **UNUSABLE** |
| `r.jina.ai/https://x.com/...` | **HTTP 403 `AbuseAlleviationError`** — "Anonymous access to domain x.com blocked … DDoS attack suspected" | **UNUSABLE** |
| `nitter.net` | connection failure (`000`) | **UNUSABLE** |
| `www.reddit.com/r/<sub>/.json` | **HTTP 403** | **UNUSABLE** |
| `old.reddit.com/r/<sub>/.json` with a browser UA | HTTP 200 but serves the **"Welcome to Reddit" interstitial HTML**, not JSON | **UNUSABLE** |
| `public.api.bsky.app` (Bluesky) | **API works.** Content coverage is the problem — see below | **CONDITIONAL / HIGH RISK** |


**Correction to a standing note.** Earlier source notes recorded X as "402, fully blocked". The current state is **200 with a login wall and no post content**, and the proxy route is separately blocked for abuse. Different mechanism, same conclusion: no usable content.


### The Bluesky identity trap — the most important finding of this test


Bluesky's public API is reachable and returns well-formed JSON. **Its sports-media handle space is not trustworthy.** Six plausible handles were tested:


| Handle tried | What it actually is |
|---|---|
| `jeffpassan.bsky.social` | **A handle-squatter.** The account's own posts read *"I continue to not be Jeff Passan"* and *"I'm merely place-holding this account handle"*. Last post **16 Nov 2024** |
| `fabrizioromano.bsky.social` | **A different person named Fabrizio.** Posts are in Turkish about domestic life; last post **5 Jul 2023**. Not the football journalist |
| `cricinfo.bsky.social` | No display name, last post **17 Nov 2024**; presents as an abandoned auto-relay |
| `mlb.bsky.social`, `espn.bsky.social`, `nba.bsky.social`, `kenrosenthal.bsky.social`, `mlbnetwork.bsky.social`, `theathletic.bsky.social` | **Profile not found** |
| `afl.bsky.social` | exists, **empty feed** |


**Zero of the handles tested were the real, current entity.** Two were confidently wrong in a way that is invisible from the handle alone — exactly the failure mode that would put a fabricated or two-year-stale "lineup" onto a card. A handle that *looks* canonical is not evidence of identity.


**Control `S-1 Rev 2` — Accredited Beat & Media Extraction Protocol (Approved 2026-09-24).** A beat-reported or team-media lineup, scratch, or rotation signal may be ingested and used for pre-game participant and rotation modeling (`G14.2`) when **all four conditions** hold, each recorded on the card:


1. **Accredited identity verified:** The report must originate from an accredited beat reporter (AP, accredited newspaper/media outlet, verified team beat writer, official broadcaster) or an official team PR channel (e.g. team PR media desk, official game notes). Parody accounts, fan blogs, odds/DFS touts, and unverified social aggregators are strictly prohibited.
2. **Temporal and event anchoring verified:** The report must explicitly anchor to **today's calendar date**, **correct venue**, and **opposing team**. Lineups lacking explicit date anchors are rejected to prevent historical matchup reuse.
3. **Corroboration standard:** Corroborated across at least **two independent accredited reporting outlets**, OR directly backed by an official team PR graphic / photograph of the physical lineup card.
4. **Verbatim citation and audit trail:** Quoted with the reporter's name, media outlet, original publication timestamp, and retrieval timestamp.


**Lineup State Taxonomy:**
- `CONFIRMED_OFFICIAL` — Published by the field owner / league structured API (`hydrate=lineups`, official boxscore, or official federation team sheet).
- `PROJECTED_BEAT_VERIFIED` — Extracted under Control `S-1 Rev 2` from accredited beat reporters present at morning skate, shootaround, batting practice, or press box. **Satisfies `G14.2` personnel modeling and DOES NOT block a margin or full-game total row from Rank #1.**
- `LINEUPS_NOT_YET_PUBLISHED @ <time>` — Structured query returned empty and no consensus beat report is available. Legitimate availability state, not a defect. Margin/full-game total capped per `G14.2`.
- `RETRIEVAL_MISS` — Lineup was published by the league or accredited beat consensus prior to freeze but not retrieved. A genuine process defect.


**Disposition:** While raw social media platforms (`x.com`) remain unauthenticated login walls, real-time search indexing, newsroom live blogs, and official team PR game notes provide reliable pre-game access to lineup cards 1–3 hours before league APIs populate. S-1 Rev 2 captures this latency advantage safely while preserving strict anti-parody, anti-stale, and anti-tout firewalls.


### Structured and beat-reporting lanes added — cross-sport coverage


| Source | Retrieval | Field | Why it is better than unverified social routes |
|---|---|---|---|
| **`SRC-BEAT-REPORTING-CROSS-SPORT`** | Search indexing / newsroom live blogs / team PR | **Projected line combinations, starters, scratches, pitch caps** | Verified beat journalists present at the venue bridge the 1–3 hour latency gap before central league feeds populate; governed by `S-1 Rev 2` |
| **`statsapi.mlb.com/api/v1/schedule?...&hydrate=lineups`** | keyless JSON | **Confirmed batting orders, both sides** | Populates with 9 named players per side once the club posts; returns empty arrays for games still `Scheduled` |
| **`statsapi.mlb.com/api/v1/game/{pk}/boxscore`** | keyless JSON | **`battingOrder` (9 IDs), `bench`, `bullpen`, positions** | Gives the exact `BENCH_NOT_RETRIEVED` field that has capped Rank-#1 margin rows on nearly every MLB card |
| **`statsapi.mlb.com/api/v1/people/{id}` → `mlbDebutDate`** | keyless JSON | **Debut date → service time** | Verified service time for rookie and debutant gates |
| **ESPN cricket `summary` → `debuts[]`** | keyless JSON | **Explicit per-match debutant list** | Machine-readable verification of format debutants |


### `NOT_YET_PUBLISHED` versus `RETRIEVAL_MISS` — updated for beat reporting


§16.8 field 7 treats a line-up not retrieved *after publication* as a `RETRIEVAL_MISS`, a process defect. Cards have been recording that flag without being able to tell the states apart.


`hydrate=lineups` and accredited beat reporting resolve it deterministically:
- **empty in feed, no beat consensus** → `LINEUPS_NOT_YET_PUBLISHED @ <time>` — verified availability state, **not** a process defect;
- **empty in feed, but verified via S-1 Rev 2** → `PROJECTED_BEAT_VERIFIED` — satisfies `G14.2` exposure modeling, unlocks Rank #1;
- **populated in feed or consensus beat published, but not captured** → `RETRIEVAL_MISS` — genuine process defect;
- **populated in feed and captured** → `CONFIRMED_OFFICIAL`.


Most of the `STARTING_LINEUPS_NOT_RETRIEVED_AT_FREEZE` flags across `P-442`–`P-455` are, on this evidence, the **first** category. The cards were penalising themselves for a publication schedule. The fix is the structured query and an honest label, not more searching.


### Press conferences and coaching-staff commentary — assessed, with a limit


Asked whether pre- and post-match press conferences can be mined for tactical intent (tempo, defensive focus, approach). Findings:


- **No structured transcript lane exists** in the keyless endpoints. `statsapi`'s `game/{pk}/content` returns 40 highlight/editorial items (video headlines, condensed game, `gameNotes`) — **not** press-conference text. Club and league sites publish pressers as prose articles, retrievable per-article but not as a feed.
- **Where they are genuinely useful: availability and role intent.** "He'll be back tomorrow", "he's on a pitch limit", "we're resting him", "he'll come off the bench". This is concrete, checkable, and already works — `P-444` captured Aaron Boone's stated plan to have Judge back, and `P-449` captured the Mason Adams pitch cap. Both were correct uses.
- **Where they are not: quantitative tactical adjustment.** A coach saying "we want to play faster" or "we need to defend better" is an intention, not a rate. Converting it into a pace or efficiency adjustment would be an unsupported signed adjustment of exactly the kind `G-L2` and §16.5 prohibit, and stated intent is weakly related to realised tempo.


**Control `S-2` — press-conference material.** Admissible as **participant, availability, workload and role evidence** — treated as `SECONDARY_ONLY` until the field owner confirms, and quoted with speaker, date and retrieval time. **Not admissible** as a signed adjustment to pace, efficiency, scoring rate or any modelled quantity. A stated tactical intention may widen a distribution or motivate a named branch with its own mass; it may not move a centre on its own.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — source-card schema and admission changes from deep research


Every material predictive field now requires a source-card record with at least:


`source_id · provider/domain · source_class · field_name · field_owner · upstream_lineage_id · definition/version · published_at · first_known_at · retrieved_at · cutoff_at · freshness_status · coverage_scope · correction/revision_semantics · prediction_research_status · snapshot_status · feature_status · invalid_reason · snapshot_hash`.


### Predictive source classes


- `VALID_PRIMARY_FIELD_OWNER` — authoritative for the field; one source can satisfy critical-state diversity when the field is truly owned by that source.
- `VALID_PRIMARY_TEAM` — authoritative only for the team's own announcement/transaction/lineup fields.
- `VALID_SECONDARY_INDEPENDENT` — acceptable supporting evidence with known lineage and timestamp.
- `HISTORICAL_STRUCTURED_CANDIDATE` — may support H0 only after coverage/definition/licensing/known-at validation.
- `DISCOVERY_ONLY` — can locate an upstream source; cannot contribute a feature or probability direction.
- `PROHIBITED_BETTING_MARKET` — sportsbook, bookmaker, odds, implied-probability, line movement, picks/tips/tout/prediction-market material.
- `PROHIBITED_FANTASY_DFS` — fantasy/DFS rankings, projections, ownership, start/sit, waiver, optimizer or derived analysis.
- `PROHIBITED_DERIVED_CONTAMINATION` — secondary content whose substantive forecast signal is inherited from either prohibited class.
- `UNKNOWN_LINEAGE` — not independent evidence until lineage is resolved.


### Point-in-time and lineage admission


A field is predictive only if `first_known_at <= cutoff_at`. The current corrected/revised value may be a **label** in development, but it cannot prove what was knowable pregame. All same-upstream mirrors share the same `upstream_lineage_id`; source count and corroboration count operate on unique lineage IDs.


Critical dynamic state (starting participants, active/inactive status, goalie/QB/pitcher/toss, weather/roof/surface where material) must be refreshed against the most recent authoritative update available before issue. If a newer official release exists than the snapshot used, mark the older snapshot `STALE_SUPERSEDED` and fail the preflight.


### Explicit exclusions


RotoWire, RotoGrinders and FPTrack are `PROHIBITED_FANTASY_DFS` for predictive evidence. Sportsbook/operator pages, odds archives/aggregators, betting previews/tips/picks and market-derived projections are `PROHIBITED_BETTING_MARKET`. A factual claim first encountered there is unusable until independently recovered from a valid upstream source.


<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## 2026-09-21 all-sports source-audit reconciliation


The register remains the source-route inventory; `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` controls historical audit precedence. No old “unavailable everywhere” claim survives merely because it predates a later demonstrated field-owner/structured route. Conversely, no new frontend, mirror or automated block is promoted to an independent lineage or human observation without provenance.


Global failure-safe labels retained across sports: `RETRIEVAL_MISS`, `NOT_YET_PUBLISHED`, `STALE_SUPERSEDED`, `SOURCE_LINEAGE_NOT_INDEPENDENT`, `SUMMARY_ONLY`, and competition/field-specific missingness. These labels describe evidence state; none creates a signed forecast adjustment.




<!-- FULL-SOURCE-REGISTER-SYNC-2026-09-21-CR3 -->
## CR-2026.09.21-3 full-register synchronization


No source class is promoted by this revision. Keep the CR-2/CR-1 source findings: field-specific source ownership, upstream-lineage deduplication, `known_at <= cutoff_at`, betting/fantasy source firewall, explicit stale/not-yet-published/retrieval-miss states, cricket toss/strip separation, and three-lineage event/finality verification. Unverified routes remain unverified; documentation cannot promote them.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## 2026-09-23 — sources exercised during the consolidated P-487–P-494 import

Quick reference: `SOURCES.md` §"2026-09-23". None is `APPROVED FOR FEATURE`. Settlement lineages must be independent and each must show a terminal marker (CR-4).

| Source ID (proposed) | Endpoint / record | Field(s) | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-NPB-BOX-RAWHTML` (method note on `SRC-BS-NPB-BIS`) | `https://npb.jp/scores/YYYY/MMDD/<home>-<away>-NN/box.html`, fetched with curl and tag-stripped | State (試合開始前 / 試合中 N回表・裏 / 試合終了), 開始/終了/試合時間/入場者, linescore, per-batter results, per-pitcher 投球数/打者/投球回/H/HR/BB/K/R/ER; pregame 先発 and スタメン | `CANDIDATE — FIELD OWNER` (reconfirmed 2026-09-23 on 0922 db-d-24, 0923 m-b-25 and 0923 db-d-25) | A summarising fetch returned an internally inconsistent box for the P-491 card; the raw parse did not. Innings notation such as "3 +" needs care. Pages lag live play by a few minutes. |
| `SRC-SPORTNAVI-NPB` (upgrade) | `https://baseball.yahoo.co.jp/npb/schedule/?date=YYYY-MM-DD` | Whole-slate state, score, W/L/S pitchers | `CANDIDATE — SETTLEMENT LINEAGE 2` | Independent statistics publisher. Summary line only; its game pages carry bench and pitcher-v-team splits. |
| `SRC-KYODO-NPB-WIRE` | Yahoo! News articles headed "D7―3中（22日）" | Final, key plays, W/L | `CANDIDATE — SETTLEMENT LINEAGE` | Wire copy is syndicated widely (Daily Sports and others): **count it once**. |
| `SRC-NIKKAN-NPB` | Nikkan Sports staff reports (also via Yahoo! News) | Final, starter lines, decisive play | `CANDIDATE — SETTLEMENT LINEAGE` | Staff byline and photographer credit; independent of Kyodo. |
| `SRC-MYNAVI-NPB-AI` | `news.mynavi.jp/article/YYYYMMDD-baseball_gameNN/` | — | **`EXCLUDED FOR SETTLEMENT`** | Self-labelled "AIを活用して作成"; the 22 Sep DeNA–Chunichi recap omitted a three-run inning. |
| `SRC-NBL-MATCH-API` | `https://schedule.nbl.com.au/api/calendar/match?match=<uuid>&league=NBL` | `match_status`, `status`, `match_status_string`, home/away score, period, clock, play-by-play (the first live event's timestamp = actual tip), lead tracker; data by Sportradar (`sportradar_timestamp`) | `CANDIDATE — FIELD OWNER (SETTLEMENT ONLY)` | **Contains `betting` and `odds` objects.** Read it programmatically and skip those keys; never print the raw JSON. Stays quarantined from forecast evidence. |
| `SRC-ESPN-SITE-API-NBL` | `site.api.espn.com/apis/site/v2/sports/basketball/nbl/scoreboard?dates=YYYYMMDD` → `summary?event=<id>` | Status, quarters, team/player box | `CANDIDATE` | HTTP **403 when a browser User-Agent is sent**. "Final" lagged the league feed by about 7 minutes and briefly reverted to "In Progress". Its data vendor relative to the NBL feed is unverified. |
| `SRC-FLASHSCORE-NBL-RESULTS` | `https://www.flashscore.com.au/basketball/australia/nbl/results/` (inline feed: `AB` status, `AG`/`AH` scores, `BA`–`BH` quarters) | Finished state, score, quarters | `CANDIDATE — INDEPENDENT SETTLEMENT LINEAGE` | Livesport runs its own data collection. The feed format is undocumented: record the raw fields; `AB÷3` on the results page = finished. |
| `SRC-WTA-MATCH-FEED` (behaviour note) | `api.wtatennis.com/tennis/tournaments/<id>/<year>/matches/` | `MatchState`, `ScoreSet*`, `ResultString` | `CANDIDATE — FIELD OWNER` | **A live (state `P`) match dropped out of the list** for several minutes (LS008, 21:33 AEST, 23 Sep); per-match `…/matches/LS008` returned 404. Re-query and cross-check with the ESPN tennis scoreboard (competition id). |
| `SRC-ESPN-SITE-API-WNBA` | `…/basketball/wnba/scoreboard?dates=` → `summary?event=` | Final, quarters, box, records | `CANDIDATE` (reconfirmed) | Used for the P-487 claimant A settlement. |
| `SRC-NBL-OFFICIAL-PREVIEW` | `nbl.com.au/news/how-to-watch-talking-points-<home>-v-<away>-round<N>`; `nbl.com.au/news/nbl26-the-latest-injury-updates` | **Expected depth chart** (first initial and surname); injury list with return round | `CANDIDATE — AVAILABILITY FIELD OWNER` | It listed "PF: J.McVeigh / K.Galloway", which the NBL card missed. It is an expected chart, not a confirmed starting five. |

<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
## 2026-09-24 — sources exercised during the consolidated P-495–P-508 import

Quick reference: `SOURCES.md` §"2026-09-24". None is `APPROVED FOR FEATURE`. Settlement lineages must be independent and each must show a terminal marker (CR-4).

| Source ID (proposed) | Endpoint / record | Field(s) | Status | Evidence and limits |
|---|---|---|---|---|
| `SRC-FESABAL-LMB` | `https://fesabal.info` (Federación Salvadoreña de Baloncesto) | Official LMB box scores, rosters, quarter scores, final confirmation | `CANDIDATE — FIELD OWNER (LMB)` | Official governing body for El Salvador Liga Mayor de Baloncesto. Primary lineage for P-505. |
| `SRC-LKL-MATCHCENTER` | `https://lkl.lt/rungtynes/...` | Official Lithuanian Basketball League play-by-play, box scores, shot charts, referee crew | `CANDIDATE — FIELD OWNER (LKL)` | High-precision official match center for Lithuania LKL. Primary lineage for P-497 and P-498. |
| `SRC-FIBA-EUROLEAGUE-WOMEN` | `https://www.fiba.basketball/en/events/euroleague-women-qualifiers-...` | Live box scores, shot charts, efficiency, quarter splits | `CANDIDATE — FIELD OWNER (FIBA)` | Official tournament portal. Primary lineage for P-499. |
| `SRC-MYKBOSTATS-PORTAL` | `https://mykbostats.com` | English-language KBO box scores, starting lineups, pitcher pitch counts, park factors | `CANDIDATE — SETTLEMENT LINEAGE` | Comprehensive KBO independent statistics portal. Corroborating lineage for P-493 and P-507. |
| `SRC-TENNISTEMPLE-LIVE` | `https://en.tennistemple.com` | Lower-tier ATP/WTA/ITF game-by-game scores, tiebreak point logs, retirement tracking | `CANDIDATE — INDEPENDENT LINEAGE` | Highly responsive lower-tier tournament coverage. Corroborating lineage for P-495 and P-496. |

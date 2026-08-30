# Data source register

Status: **ACTIVE DESIGN REGISTER — NO H0 INGESTION AUTHORISED**

Register version: **DSR-2026.08.30-v0.7**

Numerical training specification: **NTS-2026.08.25-v0.2**

Effective: **2026-08-30**

This register routes prediction-time research and defines what must be proved before any field enters H0. A source being public, official, popular, searchable, downloadable, or technically accessible does not establish permitted automation, retention, redistribution, complete coverage, stable definitions, prediction-time reconstructability, or model fitness.

No source or field is currently `APPROVED FOR FEATURE`.

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
| `SRC-CRIC-ICC-MATCH` | ICC competition identity, official match state/result reporting and governing competition context | V0–V4; exact match page/report | Dynamic scorecard coverage, event timestamps, correction path and use terms still require field audit | CANDIDATE / RESEARCH ONLY |
| `SRC-CRIC-CRICSHEET-JSON` | Historical delivery/innings/match events | Versioned release; reconcile to official scorecard | Coverage/exclusions, match-data use terms, revisions, day/session reconstruction and identity joins | CANDIDATE |
| `SRC-CRIC-CRICSHEET-REGISTER` | Person identity crosswalk | Exact release/hash | Attribution/licence implementation, missing-ID and crosswalk quality | CANDIDATE |
| `SRC-CRIC-SPECIALIST-SCORECARD` | Scorecards, commentary, venue/player history and exact-match reporting | V0–V3; official source controls conflicts | Access/automation terms, provider definitions, coverage and known-at reconstruction | CANDIDATE / RESTRICTED |
| `SRC-CRIC-PITCH-REPORT` | Timestamped exact-match strip/surface evidence | V2; official/team/reporting fallback | Historical reconstructability, semantic coding, conflicts and missingness | CANDIDATE |
| `SRC-CRIC-GOV-WEATHER` | Playable-time/weather/light scenarios | V2; applicable national service | Point-in-time archive and stadium-local mapping | CANDIDATE |

Cricsheet identifies JSON as its main/official format and exposes format version, creation and revision fields. Its documented missing-field indicators must be retained, not silently imputed. References: [formats](https://cricsheet.org/format/), [JSON](https://cricsheet.org/format/json/), [downloads](https://cricsheet.org/downloads/), and [register](https://cricsheet.org/register/).

Current official-research reference: [ICC match reporting](https://www.icc-cricket.com/news/india-retain-upper-hand-despite-sri-lanka-fightback). This proves a usable field-specific research lane, not blanket historical/API approval.

Audited exact-phase example: the [Cricket Ireland-branded Belfast–Dublin scorecard](https://cricketarchive.com/CricketIreland/Scorecards/1458/1458955.html) exposed final innings and powerplay fields used for P-115 settlement. Its usefulness does not resolve host relationship, automation, retention, full coverage or historical-known-at approval.

P-175 adds an exact current governing-report lane: the [ICC South Africa–Zimbabwe report](https://www.icc-cricket.com/news/brevis-blitz-sees-off-zimbabwe-as-south-africa-bounce-back) confirms Zimbabwe 144/8 and South Africa's seven-wicket chase. Detailed powerplay settlement still requires an exact scorecard/delivery field whose owner and legal-ball definition match the contract. P-171 was recoverable from current specialist scorecards/reporting, but no indexed competition-owner scorecard was established in this audit; retain that result as research corroboration rather than turning the specialist into a universal field owner.

## 7. Basketball source lanes

| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-BB-OFFICIAL-EVENT-*` | Schedule, rules, roster, game state, play-by-play and final | V0/V4 | League-by-league access, correction, IDs and use terms | CANDIDATE |
| `SRC-BB-OFFICIAL-INJURY-*` | Official availability status | V1/V2; team release fallback | Historical reports, publication times and status semantics | CANDIDATE |
| `SRC-BB-OFFICIAL-STATS-*` | Provider-defined pace, ratings, lineups, tracking and box statistics | V3; match centre cross-check | Coverage changes, automation/use, corrections and versioned definitions | CANDIDATE |
| `SRC-BB-FIBA-EVENT` | FIBA event identity, official final, quarter scores, box score and documented lead/margin path where exposed | V0/V4; exact FIBA game page/report | Event coverage, dynamic access, correction history, definitions, automation/retention and known-at timestamps | CANDIDATE / RESEARCH ONLY |
| `SRC-BB-WNBA-EVENT` | WNBA event identity, official final, quarter/box/play-by-play and team recap where exposed | V0/V1/V4; exact game page then official team report | Dynamic rendering, stable IDs, correction history, historical known-at times, definitions and use/retention | CANDIDATE / RESEARCH ONLY |
| `SRC-BB-HERHOOP-BOX` | Specialist WNBA box-score/minutes cross-check | V3/V4; WNBA official final controls conflicts | Provider definitions, correction lineage, historical known-at time, licence/automation/retention and official reconciliation | CANDIDATE / RESTRICTED |
| `SRC-BB-SPECIALIST-PBP-*` | Possessions, lineup stints, on/off and shot-process features | V3 | Licence, coverage, possession definitions, lineup gaps and corrections | CANDIDATE / RESTRICTED |
| `SRC-BB-REFERENCE-RESEARCH` | Human-queryable history and cross-checks | V3 | No automatic H0 retention until terms/coverage/timing pass audit | RESEARCH ONLY |

The [NBA statistics glossary](https://www.nba.com/stats/help/glossary) defines NBA metrics such as pace. The [official WNBA injury report](https://www.wnba.com/wnba-injury-report) is a candidate volatility source. Neither link grants site-wide ingestion approval.

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

## 10. AFL/AFLW source lanes

| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-AFL-OFFICIAL-*` | Rules, fixtures, teams/late changes, injuries, match centre, official stats and final | V0/V1/V4 | Historical release times, event access, correction and definition versions | CANDIDATE |
| `SRC-AFL-HISTORICAL-*` | Historical match/player records | V3/V4; official reconciliation | Coverage, identity, terms, correction and event-time fields | CANDIDATE / RESEARCH ONLY |
| `SRC-AFL-SQUIGGLE` | Fixtures/scores and external-model consensus challenger | Respect current cache/user-agent limits | API terms, hobby-service reliability, coverage; lacks advanced Champion Data fields | CANDIDATE / RESTRICTED |
| `SRC-AFL-BOM` | Venue-local forecast and observation | V2; official venue roof report | Point-in-time archive and venue mapping | CANDIDATE |

Official AFL/AFLW sources control current facts. The [official AFLW P-163 report](https://www.afl.com.au/aflw/news/1596975/adelaide-crows-crank-it-up-to-hand-west-coast-eagles-third-loss-on-the-trot) establishes a useful exact-game final/quarter-path research lane, while the [official P-169 AFL match centre](https://www.afl.com.au/afl/matches/9021) owns Carlton's 74–55 final. [Squiggle's API](https://api.squiggle.com.au/) is a candidate external comparison, not an approved feature source or production backend.

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

[StatsBomb Open Data](https://github.com/statsbomb/open-data) is selective, not a universal upcoming-match feed. Provider-specific corner, card and SOT labels require exact definition continuity.

The [Gotham P-147 official recap](https://www.gothamfc.com/news/recap-gotham-fc-portland-battle-to-draw-in-muchanticipated-rematch) exposed score, phase, xG, shots and corners. The [Colorado Rapids 2 P-149 official recap](https://www.coloradorapids.com/rapids2/news/recap-colorado-rapids-2-fall-in-tight-battle-against-ventura-county-fc) exposed the reserve-match final and narrative. APWin, TotalCorner, PlayerStats, BetPawa/Sportradar-derived pages and similar front ends remain provisional niche lanes; multiple front ends are not independent evidence when they share an upstream feed.

P-172–P-183 add several high-quality exact-event result lanes: the [Liverpool P-172 official report](https://www.liverpoolfc.com/news/isak-and-munoz-score-liverpool-draw-nottingham-forest/), [Bundesliga P-180 official report](https://www.bundesliga.com/en/bundesliga/news/cologne-hoffenheim-match-report-highlights-matchday-1-38869), [KNVB P-182 result lane](https://www.knvb.nl/node/15406), and [LaLiga P-183 official match page](https://www.laliga.com/en-MA/match/temporada-2026-2027-laliga-ea-sports-levante-ud-real-betis-3). Use the exact fields exposed by each owner. The LaLiga page exposes official shots and 5–8 corners; a club report may control narrative and final but not automatically own a proprietary corner count.

The Ligue 3 audit remains field-specific. [L'Équipe's round report](https://www.lequipe.fr/Football/Actualites/Amiens-gagne-enfin-thionville-accroche-mais-toujours-leader-le-resume-de-la-quatrieme-journee-de-ligue-3/1714460) supports finals; [Kickmetrics for P-177](https://kickmetrics.io/en/soccer/match/sc-aubagne-air-bel-bourg-en-bresse/019f25cd-f24a-7bdf-818e-303ac65584bb) and [Offside Scores for P-179](https://offsidescores.com/pt/futebol/jogo/thionville-lusitanos-paris-13-atletico-20260829/8be47d51-2258-429b-a957-27dc573f6d65/detalhe) remain specialist stat lanes. P-176-C05 and P-178-C05 stay unresolved; P-179-C05 stays provisional. A Forebet predicted corner score, a TotalCorner page still labelled upcoming after the final, or several fronts from one feed are negative source-state examples and cannot settle the field.

Audited field-specific examples: [ASEAN United FC Vietnam–Thailand official match page](https://aseanutdfc.com/vi/asean-championship/match/38w3neiqa1x8wrv2ibhgum978/details) and [UEFA Apollon–FH official match page](https://www.uefa.com/womenseuropacup/match/2049375--apollon-ladies-vs-fh/matchinfo/). Use only the fields actually exposed and timestamped by each owner.

The P-123 audit also establishes a negative source-state example: the Uzbekistan PFL match centre remained an all-zero 0-0 placeholder while current independent match reports documented BuxDU 0–4 Metallurg. The PFL shell is retained as a conflict record, not a valid settlement source for that score or its zero statistics.

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

The [Tennis.com Kopp–Krumich match page](https://www.tennis.com/tournaments/schwaben-open/matches/s-kopp-vs-m-krumich-2026-08-27) proved useful for current set score and serve/break-point fields in the P-118 audit. It remains a specialist research lane, not governing-tour authority or an approved H0 source.

The [ATP Winston-Salem official results](https://www.atptour.com/en/scores/current/winston-salem/6242/results) and [official tournament schedule](https://www.winstonsalemopen.com/en/scores/schedule) are retained as field-owner lanes for P-136 identity, round, order and result. Tennis.com remains a useful current cross-check but does not override ATP/event corrections.

Livesport exposed the P-162 set score for research, but no official ITF/event result was recovered in the audit. It remains within `SRC-TEN-SPECIALIST-STATS-*`; the settlement is provisional and no new source approval or model weight follows.

## 14. Ice-hockey source lanes

| Source ID | Permitted role | Refresh/fallback | Unresolved numerical gate | Status |
|---|---|---|---|---|
| `SRC-IH-NHL-OFFICIAL` | NHL schedule, rules, roster, projected/confirmed lineup/goalie reports, state, official stats and final | V0/V1/V4 | Endpoint/access documentation, corrections, IDs and use terms | CANDIDATE |
| `SRC-IH-MONEYPUCK-DL` | Downloaded NHL shot/xG and game/player research fields within stated use | Versioned/nightly release as documented | Non-commercial/ad-hoc use limits, attribution, approved access, schema/corrections; listed shot data omits blocked shots | RESTRICTED / CANDIDATE |
| `SRC-IH-SPECIALIST-SHOTS-*` | Defined shot attempt/xG/manpower/line metrics | V3 | Licence, methodology, coverage, corrections and provider drift | CANDIDATE / RESTRICTED |
| `SRC-IH-GOALIE-REPORT-*` | Starting-goalie/line combination report pending official confirmation | V1; official NHL/team source controls conflicts | Historical availability, accuracy, timestamps and terms | CANDIDATE / RESEARCH ONLY |

References: [NHL glossary](https://www.nhl.com/info/hockey-glossary), [official projected lineups/goalies](https://www.nhl.com/news/topic/game-previews/nhl-projected-lineup-projections), and [MoneyPuck downloads/use statement](https://www.moneypuck.com/data.htm).

For AIHL research, [Ice Hockey News Australia's P-125 result](https://icehockeynewsaustralia.com/2026/08/28/2026-goodall-cup-playoffs-canberra-brave-defeat-sydney-bears-in-the-preliminary-round-to-advance/) exposed final, period and SOG fields and linked a game card. Its [P-166 semifinal report](https://icehockeynewsaustralia.com/2026/08/29/2026-goodall-cup-playoffs-canberra-brave-defeat-melbourne-mustangs-in-semifinals-to-advance/) corroborates Canberra's 5–4 overtime final. Treat both as reputable specialist/research lanes pending direct AIHL field-owner access; neither establishes sportsbook OT/action terms or blanket numerical-ingestion approval.

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

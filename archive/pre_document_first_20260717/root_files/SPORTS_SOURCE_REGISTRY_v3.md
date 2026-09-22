# Sports Source Registry v3

Effective: 2026-07-16  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**  
**Audit basis:** Direct league, governing-body, tournament, club, national-weather-service, provider-documentation and original-research pages were checked on 2026-07-16 unless a row says otherwise.

This registry replaces the broken and stale v2 source table. Authority is assigned to a source for a particular fact; no website is universally authoritative. A page being reachable does not prove its data are current, and the newest rulebook is not necessarily the rulebook in force.

## 1. Authority classes

| Class | Meaning | Permitted use |
| --- | --- | --- |
| A0 | Governing body, competition organiser, official match centre, gamebook, scorecard, team sheet, or effective rulebook | Controls event identity, rules, participation state, result and settlement within its scope |
| A1 | First-party participant: official team, club or federation communication | Controls its own announcement until superseded by an A0 game sheet or ruling |
| B | Named licensed data provider or rights-holding broadcast | Primary only for its documented measurement/feed; record product, licence, timestamp and definition |
| C | Specialist independent source or reputable press | Context and cross-check; not final authority for decisive facts when A0/A1 exists |
| D | Aggregator, search snippet, social post or general discovery tool | Discovery only; independently verify every material fact |
| P | Proxy, cache or text-rendering layer | Access mechanism only; cite and retain the underlying publisher URL |

StatMuse, Reddit and social media are never mandatory. `r.jina.ai` is a transport layer, not a publisher. Undocumented official-host JSON routes may be useful but have no assumed service guarantee and must be schema-monitored.

## 2. Required registry and observation fields

Every production source record must store:

`source_id, publisher, direct_url_or_template, sport, competition, fact_classes, authority_class, official_status, access_method, authentication, machine_readable, documented_api, data_through, source_published_at, source_updated_at, observed_at_utc, effective_from, effective_to, season, access_state, last_access_test_at, next_retest_due, latency_note, coverage_limit, fallback_ids, conflict_rule, raw_snapshot_path_or_hash, notes`.

Do not substitute `last_access_test_at` for `data_through`, `known_at`, or `effective_from`. Preserve the direct URL and, where permitted, the response, PDF, gamebook or screenshot hash used by a forecast.

## 3. Fact-specific conflict rules

1. The exact competition rulebook and event regulations outrank a generic sport rulebook.
2. The official event sheet/gamebook outranks a team projection or media lineup.
3. An A0 correction supersedes an earlier A0 result; append the correction and retain the prior evidence.
4. A team is authoritative for its announcement, but not for the opponent or the competition's legal settlement.
5. Provider-specific advanced metrics are not interchangeable. Store provider, definition and model/version.
6. A sportsbook or exchange is authoritative only for its own quoted price and market state, not for the event result.
7. If decisive A0 evidence is unavailable or conflicts, mark the fact `UNVERIFIED` or `CONFLICT`; do not silently promote a lower tier.

## 4. Freshness and capture rules

| Fact | Minimum check |
| --- | --- |
| Rules | At season/event start and after a published change; record effective dates and competition overrides |
| Fixture/venue | At forecast cutoff, about T-24h, and near the final participation gate when relevant |
| Injury/availability | Latest official reporting deadline and the sport-specific final participation gate |
| Statistics | Record definition, unit, sample, exclusions and `data_through`; confirm the newest completed event is included |
| Weather | Venue coordinates and official point forecast/nowcast near T-24h, T-6h and T-90m when material; roof state separately |
| Officials | After the competition's release window and again on the official game sheet when available |
| Price | Operator/provider, jurisdiction, market ID/rules, line, selection, decimal price, status, in-play flag and observed UTC timestamp |
| Final | Direct official event page/gamebook after final status; append later corrections rather than overwriting |

## 5. Verified sport source chains

### Australian football

| Fact | A0/A1 chain | Qualification |
| --- | --- | --- |
| Fixtures, results and stats | [AFL fixture](https://www.afl.com.au/fixture), [AFL stats](https://www.afl.com.au/stats), official match centre | Use the match centre/team sheet for final state; AFLW and state competitions need their own rules and pages |
| Rules | [AFL Laws hub](https://www.afl.com.au/about-afl/laws-of-the-game), [2026 Laws PDF](https://resources.afl.com.au/afl/document/2026/02/13/8676d880-481a-4211-a479-305f138ce8b6/Laws-of-Australian-Football-Final-13-February-2026-.pdf), [2026 AFL Rules](https://resources.afl.com.au/afl/document/2026/02/13/52922632-b4be-4c8d-82b8-3766b96c8a88/AFL-Rules-Final-11-February-2026-.pdf) | Record season and competition variant |
| Availability | Official club/team selection and [AFL injury reporting](https://www.afl.com.au/news/injury-news) | Recheck at team selection and final game sheet |
| Officials | [AFLUA](https://aflua.com.au/) | A1/specialist appointment source, not the AFL governing body; final game sheet controls |

Champion Data is B when a licensed product is actually available. AFL Tables, FootyWire and Wheelo are C and must not be relabelled official.

### Baseball

| Scope | A0 chain | Qualification |
| --- | --- | --- |
| MLB | [Schedule](https://www.mlb.com/schedule), [lineups](https://www.mlb.com/starting-lineups), [transactions](https://www.mlb.com/transactions), [injuries](https://www.mlb.com/injury-report), [stats](https://www.mlb.com/stats), [Baseball Savant](https://baseballsavant.mlb.com/), [rules](https://www.mlb.com/official-information/official-rules) | Gameday/gamebook settles; lineups remain subject to change. `statsapi.mlb.com` is official-host but publicly undocumented |
| NPB | [NPB English](https://npb.jp/eng/), [2026 games](https://npb.jp/games/2026/), [2026 stats](https://npb.jp/bis/eng/2026/stats/), [announced starters](https://npb.jp/announcement/starter/), [registrations](https://npb.jp/announcement/roster/) | Clubs supply many injury facts; no complete central advanced/injury feed was verified |
| KBO | [KBO English](https://eng.koreabaseball.com/), [GameCenter](https://www.koreabaseball.com/Schedule/Schedule.aspx), [records](https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx), [registration](https://www.koreabaseball.com/Player/Register.aspx) | MyKBO and Naver are secondary, not KBO primary sources |
| CPBL, ABL, international | [CPBL](https://www.cpbl.com.tw/), [Australian Baseball League](https://theabl.com.au/), [WBSC events](https://www.wbsc.org/en/events) | WBSC was intermittently fetchable; test the exact event before use |

### Basketball

| Scope | A0 chain | Qualification |
| --- | --- | --- |
| NBA | [Schedule](https://www.nba.com/schedule), [NBA Stats](https://www.nba.com/stats), [official rules](https://official.nba.com/), [referee assignments](https://official.nba.com/referee-assignments/) | Referee assignments are normally posted about 9 a.m. ET game day. Injury-report URLs are season-specific |
| WNBA | [Schedule](https://www.wnba.com/schedule), [stats](https://stats.wnba.com/), [transactions](https://www.wnba.com/players/transactions), [key dates](https://www.wnba.com/keydates) | Use official team/league releases and gamebook for final availability |
| NBA Summer League | [Official 2026 hub](https://www.nba.com/summer-league/2026) | Separate rules, rosters and form; do not transfer regular-season assumptions |
| FIBA | [Event hub](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers), [reports](https://reports.fiba.basketball/), [rules hub](https://about.fiba.basketball/en/services/resource-hub/downloads), [refereeing/rules](https://refereeing.fiba.basketball/en/rules) | As of 2026-07-16, the 2024 global rules baseline remains current. [2026 changes](https://about.fiba.basketball/en/news/fiba-official-basketball-rules-changes-2026-summary-now-available) take effect 2026-10-01 unless a competition states otherwise |
| NCAA basketball | [Men's stats](https://www.ncaa.com/stats/basketball-men/d1), [women's stats](https://www.ncaa.com/stats/basketball-women/d1), [scoreboard](https://www.ncaa.com/scoreboard/basketball-men/d1), [2026 championship reports](https://www.ncaa.com/PAReports) | The cited availability policy is for 2026 Division I championship games only, not the regular season or football |
| Domestic leagues | [NBL](https://www.nbl.com.au/pages/stats-hub), [WNBL](https://www.wnbl.com.au/), [NZ NBL](https://nznbl.basketball/), [ACB](https://www.acb.com/es/liga), [LKL](https://lkl.lt/), [PLK](https://plk.pl/), [TBF BSL](https://www.tbf.org.tr/ligler/bsl-2025-2026), [Israel league](https://basket.co.il/) | Use each official match sheet and club status. TBLStat is independent; season labels must be checked |

### Cricket

| Fact | A0 chain | Qualification |
| --- | --- | --- |
| Laws/conditions | [MCC Laws](https://www.lords.org/mcc/about-the-laws-of-cricket), [ICC playing conditions](https://www.icc-cricket.com/about/cricket/rules-and-regulations/playing-conditions) | Do not apply MCC's published 2026 edition before 2026-10-01 unless the exact competition adopted it; select the exact ICC format/event document |
| Fixtures/results | [ICC fixtures/results](https://www.icc-cricket.com/fixtures-results), exact event and host-board scorecard | Official scorecard, toss and XI control. Board entry points: [BCCI](https://www.bcci.tv/), [ECB](https://www.ecb.co.uk/england/men/fixtures), [Cricket Australia](https://www.cricket.com.au/matches), [Bangladesh](https://www.tigercricket.com.bd/), [Ireland](https://cricketireland.ie/), [Afghanistan](https://www.acb.af/), [Sri Lanka](https://srilankacricket.lk/), [West Indies](https://www.windiescricket.com/) |
| Officials | [ICC appointments](https://www.icc-cricket.com/about/cricket/match-officials/match-official-appointments) | Appointments are provisional; verify the final scorecard |
| MLC | [Matches](https://www.majorleaguecricket.com/matches), [results](https://www.majorleaguecricket.com/matches/results), [stats](https://www.majorleaguecricket.com/stats) | Official but JavaScript-heavy; do not hard-code season/territory broadcast claims |
| Ball-by-ball archive | [Cricsheet](https://cricsheet.org/), [format](https://cricsheet.org/format/) | C: excellent structured independent data, not ICC/league authority; declare coverage gaps |

A broadcast pitch walkaround can be a direct observation, but it is not universally required. Record match identity, reporter, timestamp, wording, strip/boundary details and access state. If missing, mark the input unknown and pass only markets that materially require it.

### Rugby league

Primary A0 chain: [NRL draw](https://www.nrl.com/draw/), [stats](https://www.nrl.com/stats/), [team lists](https://www.nrl.com/news/topic/team-lists/), [judiciary](https://www.nrl.com/news/topic/judiciary/) and [Casualty Ward](https://www.nrl.com/news/topic/casualty-ward/). The injury route was intermittently fetchable, so official clubs are the fallback.

**2026 correction:** [NRL's Round 1 team-list notice](https://www.nrl.com/news/2026/03/03/nrl-team-lists-round-1/) states that two players are omitted 24 hours before kickoff and the final 19 is named 90 minutes before kickoff. Verify the actual 17 and positions in the official match centre at kickoff. The former “final 17 one hour before kickoff” rule is retired. Zero Tackle and League Unlimited are C; the undefined `Legz` source is removed.

### Rugby union

| Fact | A0/A1 chain | Qualification |
| --- | --- | --- |
| Laws and variations | [World Rugby Laws hub](https://passport.world.rugby/laws-of-the-game/), [2026 law book](https://passport.world.rugby/media/jxrnmptk/2026en-laws-of-the-game-compressed.pdf), [law clarifications](https://passport.world.rugby/laws-of-the-game/law-clarifications/), [application guidelines](https://passport.world.rugby/laws-of-the-game/law-application-guidelines/) | Select the exact competition regulations, law trials, effective dates and variation. Fifteens, sevens, tens, youth and community forms are not interchangeable. The June 2026 maul guideline applies only under its stated adoption/effective conditions. |
| International fixtures/results | [World Rugby fixtures and results](https://www.world.rugby/tournaments/fixtures-results), exact tournament match centre and official match sheet | The tournament organiser and final match sheet control lineup, cards, replacements, result and correction. A calendar listing alone does not prove a final team or status. |
| International strength context | [World Rugby rankings](https://www.world.rugby/rankings) | A transparent baseline/context only, not a fitted match probability. The ranking definition changed from 1 July 2026 by removing home weighting; store the effective version and never backfill the new definition into older cutoffs. |
| Club competitions and availability | Exact organiser match centre, competition regulations, official club/team announcement and final match sheet | Super Rugby, Six Nations, URC, Premiership, Top 14 and other competitions need separate source-map/parser tests. No complete universal public injury or advanced-statistics feed was verified. |

Rugby league data and scoring rules must never be substituted for rugby union. Provider-specific phase, ruck, possession, territory and expected-points fields require stored definitions and licences before model use.

### Soccer

| Scope | A0 chain | Qualification |
| --- | --- | --- |
| FIFA World Cup | [Tournament hub](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026), [Match Centre](https://www.fifa.com/en/match-centre), [2026 schedule update](https://inside.fifa.com/organisation/media-releases/updated-world-cup-2026-match-schedule-venues-kick-off-times-104-matches) | Official team sheet and match report control |
| Laws | [IFAB Laws](https://www.theifab.com/laws/latest/) | Pair with exact competition regulations for substitutions, extra time and settlement |
| Premier League | [Matches and live results](https://www.premierleague.com/en/matches/premier-league), [injury reporting](https://www.premierleague.com/en/news/4242565/club-by-club-injuries-article), exact official match page | Predicted lineups remain projections until the official sheet |
| Bundesliga | [Official matchdays](https://www.bundesliga.com/en/bundesliga/matchday), exact official match page and DFL regulations | Only Bundesliga is analysis-enabled; Bundesliga 2 and cup matches require separate scope |
| UEFA Champions League | [Fixtures and results](https://www.uefa.com/uefachampionsleague/fixtures-results/), exact UEFA match page and competition regulations | Other UEFA competitions do not inherit this source scope |
| A-League Men | [Official fixtures and results](https://aleagues.com.au/fixtures/a-league/), exact A-Leagues match page and rules | A-League Women is a separate scope and is not analysis-enabled by this row |
| MLS | [Schedule](https://www.mlssoccer.com/schedule/), [stats](https://www.mlssoccer.com/stats/players/), dated official availability/disciplinary reports | Reopen the exact dated report; do not assume a persistent URL is current |
| Argentina AFA | [Promocional draw](https://www.afa.com.ar/es/posts/se-realizo-el-sorteo-del-torneo-promocional-amateur), [programming/officials](https://www.afa.com.ar/es/posts/programacion-y-arbitros-de-la-proxima-fecha-de-la-primera-b-primera-c-y-promocional-amateur), [regulations](https://www.afa.com.ar/11608/reglaments/torneos-superiores?s=6) | No rich official public advanced/injury feed was verified; declare the gap |
| Peru Copa Caliente | Exact LFPP/FPF, club or official broadcast material | No stable official match-centre endpoint was verified. [TVPerú explainer](https://tvperu.gob.pe/noticias/deportes/copa-caliente-de-la-liga-2026-fecha-de-inicio-fixture-grupos-formato-y-premios) is dated secondary context |

Licensed Opta/Stats Perform/StatsBomb data is B only when held. Store the provider/model version; never splice incompatible xG series. FBref and score aggregators are C/D.

### Ice hockey

| Scope | A0 chain | Qualification |
| --- | --- | --- |
| NHL | [Schedule](https://www.nhl.com/schedule), [stats](https://www.nhl.com/stats/), [NHL EDGE](https://edge.nhl.com/), [teams/rosters](https://www.nhl.com/info/teams), Game Centre/game report | No verified complete central injury report; use official clubs. Treat projected goalies as projected until official/warmup evidence. `api-web.nhle.com/v1` is undocumented |
| IIHF | [2026 Worlds schedule](https://www.iihf.com/en/events/2026/wm/schedule), [official documents](https://www.iihf.com/en/events/2026/wm/tournamentinfo/officialdocuments), [rules/regulations](https://www.iihf.com/en/static/55352/rules_regulations_guidelinesspan) | Select the rule family effective for the event; newest published is not automatically applicable |

Scouting the Refs is C. The official game sheet is the final assignment source.

### American football

| Scope | A0 chain | Qualification |
| --- | --- | --- |
| NFL | [Schedules](https://www.nfl.com/schedules), [stats](https://www.nfl.com/stats), [Next Gen Stats](https://nextgenstats.nfl.com/), [injuries](https://www.nfl.com/injuries/), [transactions](https://www.nfl.com/transactions/), [inactives](https://www.nfl.com/inactives/), [rulebook](https://operations.nfl.com/the-rules/nfl-rulebook/) | Inactives are the final participation gate. On 2026-07-16 the generic page still exposed the 2025 rulebook; [2026 proposals](https://operations.nfl.com/media/dxfj3uak/2026-playing-rules-bylaw-and-resolution-proposals.pdf) are not a final rulebook |
| NCAA football | [FBS stats](https://www.ncaa.com/stats/football/FBS), [football rules](https://www.ncaa.org/championships/playing-rules/football-playing-rules/), NCAA scoreboard and school/conference game notes | No complete central availability report was verified; final gamebook controls participation |

Football Zebras and public EPA/success-rate providers are C unless a documented licence says otherwise.

### Tennis and golf

| Scope | A0 chain | Qualification |
| --- | --- | --- |
| Tennis | [Wimbledon order of play](https://www.wimbledon.com/en_GB/scores/schedule/schedule2.html), [scores](https://www.wimbledon.com/en_GB/scores/schedule/index.html?embed=true), [ITF draws/results](https://www.itftennis.com/en/tournament/wimbledon/gbr/2026/w-sl-gbr-2026-001/draws-and-results/), [ATP rulebook](https://www.atptour.com/en/corporate/rulebook), [ATP calendar](https://www.atptour.com/en/news/what-is-the-2026-atp-tour-calendar), [WTA rules](https://www.wtatennis.com/wta-rules) | Official draw/order/withdrawal and match page control. Entry does not prove fitness; no universal predictive injury report exists |
| Golf | [2026 PGA Tour schedule](https://www.pgatour.com/schedule/2026), [leaderboard/field/tee times](https://www.pgatour.com/leaderboard), [stats](https://www.pgatour.com/stats/stats) | The major organiser controls its championship; capture field, withdrawals and tee times after release |

### Volleyball

| Fact | A0 chain | Qualification |
| --- | --- | --- |
| Competition identity, fixtures and results | [FIVB competitions](https://www.fivb.com/volleyball/fivb-competitions/) and the exact Volleyball World/FIVB event match centre | Use the event-specific match sheet for format, participants, set scores, sanctions and final status; a generic competition hub is not settlement evidence |
| Rules | [FIVB Official Volleyball Rules 2025–2028](https://www.fivb.com/wp-content/uploads/2025/01/FIVB-Volleyball_Rules2025_2028-EN-v05.pdf) plus exact competition regulations | Indoor, beach, age-group and domestic variants are separate contracts; record edition and competition overrides |

No complete public universal injury/starting-lineup or rally-level feed was verified. Team announcements are A1 for their own availability; the final official match sheet controls participation. A rally model cannot activate from set scores alone.

### Motorsport

| Fact | A0 chain | Qualification |
| --- | --- | --- |
| Regulations and classifications | [FIA regulations](https://www.fia.com/regulations) and the exact championship/event document set | Store championship, document title, issue number, publication/effective time, bulletins and stewards' decisions; later classifications may correct the provisional result |
| Participant identity | [2026 FIA Formula One entry list](https://www.fia.com/events/fia-formula-one-world-championship/season-2026/2026-fia-formula-one-world-championship-entry) | Entry does not establish that a driver starts; event entry lists, grid, penalties and official classification are separate observations |

Every series needs its own source map and sporting/technical contract. Grid penalties, parc fermé changes, red flags, restarts, classification thresholds and post-race penalties can change the target. Telemetry or timing feeds are B only with documented rights, definitions, latency and completeness.

### Combat sports

| Fact | A0/A1 chain | Qualification |
| --- | --- | --- |
| Rules and judging | [Association of Boxing Commissions unified rules](https://www.abcboxing.com/unified-rules/) plus the event athletic commission's adopted rules | Commission/jurisdiction adoption controls; MMA, boxing and other combat formats are not interchangeable |
| Result and scorecards | Event athletic commission ruling, followed by [UFC scorecards](https://www.ufc.com/scorecards) as promotion-hosted evidence where applicable | A commission correction/no-contest ruling overrides a promotion page; preserve later corrections as new settlement versions |

Official weigh-in, bout-order and withdrawal evidence must be event-specific. Method, round and duration markets require an exact branch map for technical decisions, disqualifications, draws, no contests and overturned results. Fight statistics from a named provider require its definition/version and cannot replace the commission's settlement authority.

## 6. Weather, venue and roof

Government weather sources are A0 for their forecasts: [Australia BOM](https://www.bom.gov.au/weather-and-climate), [US NWS](https://www.weather.gov/), [UK Met Office](https://weather.metoffice.gov.uk/forecast/uk), [Environment Canada](https://www.weather.gc.ca/), [KMA](https://www.weather.go.kr/w/index.do), [JMA](https://www.jma.go.jp/bosai/forecast/), [India IMD](https://mausam.imd.gov.in/) and [Mexico SMN/CONAGUA](https://smn.conagua.gob.mx/). Open-Meteo is a C model aggregator.

Store coordinates, issue and valid times, units, precipitation probability/amount, wind mean/gust/direction, temperature, humidity and warnings. The event or venue controls roof/surface state. Do not apply outdoor weather to a confirmed closed/domed venue.

## 7. Odds and market snapshots

Odds remain outside the workflow unless the user authorizes them. When authorized, preserve the operator/provider, jurisdiction, delay/account state, event and market IDs, rules, selection, line, decimal price, exchange side/size when applicable, market status, `inplay`, publish time, `observed_at_utc`, and response/screenshot hash.

[Betfair Exchange API definitions](https://betfair-developer-docs.atlassian.net/wiki/spaces/1smk3cen4v3lu3yomq5qye0ni/pages/2687465) distinguish market status, in-play state, delay and version. [Sportradar Odds API](https://developer.sportradar.com/odds/reference/intro) and [market-status documentation](https://docs.sportradar.com/uof/data-and-features/markets-and-outcomes/market-status) describe provider states. Define close before analysis as the last open, unsuspended, pre-start quote from the same operator, market, line and rules. Never reconstruct it from a later aggregator page.

## 8. Access-state vocabulary

`OPENED`, `API_OK`, `PDF_OK`, `DYNAMIC`, `INTERMITTENT`, `SNIPPET_ONLY`, `BLOCKED`, `STALE`, `CONFLICT`, `UNVERIFIED`, `RETIRED`.

`OPENED` says only that access succeeded. Production use still requires correct event identity, freshness, effective period and a retained point-in-time observation.

## 9. Retired v2 mandates

- Mandatory StatMuse-first querying.
- Mandatory X/Reddit checks.
- Domain-verified social accounts treated as A0/A1 automatically.
- `r.jina.ai`, TotalCorner, Guardian live pages or ESPN public endpoints used as final settlement authority.
- MyKBO, TBLStat, AFLUA, Zero Tackle, League Unlimited, Scouting the Refs, Football Zebras or ASAP Sports labelled as their sport's governing body.
- Universal L5/L10/L15/L20 collection regardless of market relevance, continuity or sample size.
- Persistent broadcast-rights assumptions and the undefined `Legz` source.

The detailed evidence trail for this replacement is retained in `outputs/comprehensive_audit_20260716/source_research.md`.

# Source-registry and forecasting-method audit

**Audit date:** 2026-07-16 (Australia/Sydney)  
**Files audited:** `SPORTS_SOURCE_REGISTRY_v2.md`, source-related instructions in `combined_sports_doc_v2.txt`, `POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md`, and the calibration-ledger schema.  
**External verification rule used here:** primary league, governing-body, tournament, club, national meteorological-service, data-provider documentation, or original research papers were preferred. Unless a row says otherwise, links below were opened or verified through the official page/index on **2026-07-16**. A page described as dynamic was reachable but may require JavaScript in the production browser. No claim that an undocumented endpoint has a service guarantee is intended.

## Executive verdict

`SPORTS_SOURCE_REGISTRY_v2.md` is not safe to keep as the canonical registry without revision. The largest problems are:

1. **The rules table is syntactically broken.** Rows 34-37 have too few columns, prose at line 39 terminates the Markdown table, and the IFAB/NFL/NRL/NHL rows at lines 40-43 are therefore not table rows. This makes automated parsing unreliable.
2. **The update and access metadata are misleading.** The title says updated 2026-06-12 although the document contains 2026-07-12 material. Under its own 30-day access-test rule, tests dated June 10, 12 and 14 are now stale (36, 34 and 32 days old). A source's content freshness, a rules document's effective period, and the last successful accessibility test are currently conflated.
3. **The mandatory StatMuse-first rule is backwards.** The registry itself documents a live misparse, yet forces an unofficial natural-language query product ahead of official sport-native stats. StatMuse can be a query accelerator or cross-check; it cannot be a mandatory gate or a source of record.
4. **Several source tiers are wrong.** ESPN's `site.api.espn.com` routes are useful but undocumented and non-governing; MyKBO is unofficial; TBLStat is not the Turkish federation; Open-Meteo is not a national weather authority; AFLUA is the umpires' association rather than the AFL; Zero Tackle, League Unlimited, Scouting the Refs and Football Zebras are independent; ASAP Sports is an independent transcript service; a Bluesky domain-verified handle is not automatically Tier A; and `r.jina.ai` is an extraction/cache layer, never the underlying source.
5. **The registry contains current rules/timing errors.** The official 2026 NRL process has a 24-hour cut and a **final 19 at 90 minutes**, not a final 17 one hour before kickoff. The wrong one-hour wording is repeated throughout the combined document. FIBA's 2026 changes do not take effect until 2026-10-01, and MCC's published 2026 Laws also do not take effect until 2026-10-01. The generic NFL rulebook page still exposed the 2025 rulebook during this audit; 2026 proposals are not the final rulebook.
6. **The all-sport L5/L10/L15/L20 requirement creates false completeness.** It demands every window for every team/player/unit even where samples overlap heavily, rosters are discontinuous, or the statistic is irrelevant. This encourages multiple-comparison hunting and overfitting. Windows should be predeclared by market and tested out of sample, with `N`, through-date, role/rules continuity, and uncertainty.
7. **Mandatory X/Reddit checks add no evidentiary value when the routes are blocked.** Social sources should be optional discovery channels. A repeated line saying an inaccessible site was inaccessible is not research.

## Sports and competitions actually in scope

The active files cover these source families:

- Australian rules: AFL, AFLW, VFL/VFLW and state/local variants.
- Baseball: MLB, NPB, KBO; the framework also names CPBL, ABL and WBSC/international baseball.
- Basketball: NBA, WNBA, NBA Summer League, FIBA internationals, NCAA basketball, NBL/WNBL and domestic leagues including NZ NBL, ACB, LKL, PLK, Turkish BSL and Israel Winner League.
- Cricket: ICC internationals and events, men's/women's/U19, MLC and other franchise cricket, and national-board tours.
- Rugby league: NRL, NRLW and State of Origin.
- Soccer: FIFA World Cup, Premier League, MLS and minor domestic competitions appearing in the logs (Argentina Torneo Promocional Amateur and Peru Copa Caliente de la Liga).
- Ice hockey: NHL and IIHF.
- American football: NFL and NCAA football.
- Tennis: Wimbledon/ATP/WTA/ITF.
- Golf appears in the hard-data gate through PGA coverage, although it does not have a full sport module.

## Required registry redesign

### Fact-specific authority, not one universal source rank

Use these classes:

- **A0 — event/rules authority:** governing body, competition organiser, official match centre, official gamebook/scorecard/team sheet, current effective rulebook or competition regulations. Controls fixture identity, official result, rules and settlement facts.
- **A1 — first-party participant:** official team, club or federation release. Controls its roster announcement, medical/status communication and coach/player statement, subject to the competition's later official game sheet.
- **B — licensed primary data/broadcast feed:** Champion Data, Opta, Stats Perform, Sportradar, official host broadcast, or another named rights/data provider. Record product, licence/access and timestamp. It may be primary for a proprietary measurement but is not the competition's legal settlement authority.
- **C — specialist independent secondary:** Cricsheet, Reference sites, reputable press, MyKBO, TBLStat, ASAP Sports. Useful when the fact is within scope and dated; cross-check decisive facts.
- **D — aggregator/discovery/social:** StatMuse, score aggregators, search snippets, social posts, Reddit. Never final settlement authority.
- **P — transport/proxy/cache:** `r.jina.ai`, text renderers and caches. Cite the underlying publisher URL and preserve the proxy only as access metadata.

Authority must be selected by **fact type**. A league match sheet can settle a result; a team can best announce its own injury update; a national weather service controls official weather forecasts; a sportsbook/exchange is primary only for its own quoted price.

### Required row fields

Replace the current prose-heavy rows with:

`source_id, publisher, direct_url_or_template, sport, competition, fact_classes, authority_class, official_status, access_method, authentication, machine_readable, documented_api, data_through, source_published_at, source_updated_at, observed_at_utc, effective_from, effective_to, season, access_state, last_access_test_at, next_retest_due, latency_note, coverage_limit, fallback_ids, conflict_rule, raw_snapshot_path_or_hash, notes`.

Never use `Last Tested` as a substitute for `data_through` or `effective_from`. Store all observed times in UTC plus the source's displayed timezone. Search snippets must be `SNIPPET`; dynamic pages must retain their underlying URL; every final/live fact should retain a raw response, PDF, gamebook or screenshot when permitted.

### Freshness rules

- **Rules:** verify effective date, season and competition override at season/event start and after a published change. The newest document is not necessarily the currently effective document.
- **Fixture/venue:** official competition page at research cutoff, again at T-24h and near lineup release if the pick depends on venue/start state.
- **Injury/availability:** latest official reporting deadline plus the sport-specific final participation gate. A roster entry is not a confirmed starter.
- **Stats:** store `data_through` and verify the newest completed event is included; never rely only on page-access date.
- **Weather:** official point forecast/nowcast for venue coordinates at roughly T-24h, T-6h and T-90m for weather-sensitive outdoor events; record roof status separately.
- **Officials:** after that competition's release window and again on the official game sheet where available.
- **Odds:** every quote needs `observed_at_utc`; opening/closing comparisons must use the same operator, jurisdiction, market ID/rules, selection, line and price format.

## Verified primary source chains

### 1. Australian rules

| Need | Primary source | Audit finding |
|---|---|---|
| Fixtures/results, lineups, injuries | [AFL fixture](https://www.afl.com.au/fixture), [AFL stats](https://www.afl.com.au/stats), AFL Team Lineups and Injury List links from the official navigation | Official and current; use the match centre/team sheet for final state. AFLW and state/local competitions require their own competition pages and variant rules. |
| Rules | [AFL Laws hub](https://www.afl.com.au/about-afl/laws-of-the-game), [2026 Laws PDF](https://resources.afl.com.au/afl/document/2026/02/13/8676d880-481a-4211-a479-305f138ce8b6/Laws-of-Australian-Football-Final-13-February-2026-.pdf), [2026 AFL Rules](https://resources.afl.com.au/afl/document/2026/02/13/52922632-b4be-4c8d-82b8-3766b96c8a88/AFL-Rules-Final-11-February-2026-.pdf), [2026 Regulations](https://resources.afl.com.au/afl/document/2026/02/13/54c158af-15e9-483b-a195-62a0f4e33b11/AFL-Regulations-Final-11-February-2026-.pdf) | Direct 2026 official documents. Store variant and effective season. |
| Availability example | [Official AFL Medical Room, R19](https://www.afl.com.au/news/1561100/medical-room-the-full-afl-injury-list-r19) | Updated 2026-07-14 during the audit; still recheck club/team selection. |
| Officials | [AFLUA](https://aflua.com.au/) | First-party umpires' association and useful appointment PDFs, but not the AFL governing body. Class A1/B for appointments, not `OFFICIAL AFL`. Final game sheet controls. |
| Advanced stats | Official AFL stats; licensed Champion Data if held | Champion Data's richer fields are proprietary. Public sites such as AFL Tables, FootyWire and Wheelo are secondary and must not be relabelled official. |

### 2. Baseball

| League | Primary chain | Availability/advanced-stat note |
|---|---|---|
| MLB | [Schedule](https://www.mlb.com/schedule), [starting lineups](https://www.mlb.com/starting-lineups), [transactions](https://www.mlb.com/transactions), [injury report](https://www.mlb.com/injury-report), [official stats](https://www.mlb.com/stats), [Baseball Savant](https://baseballsavant.mlb.com/), [rules](https://www.mlb.com/official-information/official-rules) | MLB.com/Gameday controls state; lineups say subject to change. Savant is official Statcast/advanced data. `statsapi.mlb.com` schedule/live-feed routes are official-host and useful, but publicly undocumented/unsupported: schema-test them and validate final settlement against Gameday/gamebook. |
| NPB | [NPB English](https://npb.jp/eng/), [2026 games](https://npb.jp/games/2026/), [2026 stats](https://npb.jp/bis/eng/2026/stats/), [announced starters](https://npb.jp/announcement/starter/), [registrations](https://npb.jp/announcement/roster/) | Official central starter and registration pages; clubs supply many injury details. No public central advanced/injury feed was verified. |
| KBO | [KBO English](https://eng.koreabaseball.com/), [Korean schedule/GameCenter](https://www.koreabaseball.com/Schedule/Schedule.aspx), [official records](https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx), [player registration](https://www.koreabaseball.com/Player/Register.aspx) | The Korean official site has the richer current GameCenter/rules/registration context. MyKBO and Naver are fallbacks, not KBO primary sources. |
| CPBL / ABL / international | [CPBL](https://www.cpbl.com.tw/), [Australian Baseball League](https://theabl.com.au/), [WBSC events](https://www.wbsc.org/en/events) | Official entry points verified. WBSC returned intermittent fetch errors in this environment; retain `DYNAMIC/INTERMITTENT`, not `WORKING`, until opened for the specific event. |

### 3. Basketball

| Scope | Primary chain | Critical qualification |
|---|---|---|
| NBA | [Schedule](https://www.nba.com/schedule), [NBA Stats](https://www.nba.com/stats), [official NBA site/rulebook](https://official.nba.com/), [referee assignments](https://official.nba.com/referee-assignments/) | Referee page states NBA/WNBA assignments are normally posted about 9 a.m. ET game day. The injury-report URL is season-specific: [2025-26 page](https://official.nba.com/nba-injury-report-2025-26-season/) must rotate each season and must not govern Summer League. |
| WNBA | [Schedule](https://www.wnba.com/schedule), [WNBA Stats](https://stats.wnba.com/), [transactions](https://www.wnba.com/players/transactions), [key dates](https://www.wnba.com/keydates) | Use current team/league PR and official gamebook for availability/start status when no complete public central report exists. |
| NBA Summer League | [Official 2026 hub](https://www.nba.com/summer-league/2026) | Separate rules, rosters, schedule and box scores. NBA regular-season stats/injury reports and parent-franchise form do not transfer. |
| FIBA internationals | [FIBA event hub example](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers), [official reports service](https://reports.fiba.basketball/), [rules hub](https://about.fiba.basketball/en/services/resource-hub/downloads), [current referee/rules portal](https://refereeing.fiba.basketball/en/rules) | **As of 2026-07-16 the 2024 rules remain the current global baseline.** FIBA says the [2026 changes](https://about.fiba.basketball/en/news/fiba-official-basketball-rules-changes-2026-summary-now-available) take effect 2026-10-01. Competition regulations can override. |
| NCAA basketball | [Men's stats](https://www.ncaa.com/stats/basketball-men/d1), [women's stats](https://www.ncaa.com/stats/basketball-women/d1), [scoreboard](https://www.ncaa.com/scoreboard/basketball-men/d1), [2026 championship availability reports](https://www.ncaa.com/PAReports) | The availability policy applies **only** to 2026 DI men's/women's Championship games: initial report 9 p.m. local the prior day and game-day report two hours before tip. Do not generalize it to the regular season or football. |
| Domestic FIBA-style leagues | [NBL Stats Hub](https://www.nbl.com.au/pages/stats-hub), [WNBL](https://www.wnbl.com.au/), [NZ NBL](https://nznbl.basketball/), [ACB](https://www.acb.com/es/liga), [LKL](https://lkl.lt/), [PLK](https://plk.pl/), [TBF BSL](https://www.tbf.org.tr/ligler/bsl-2025-2026), [Israel league](https://basket.co.il/) | Use each official schedule/game sheet/start list/box score plus official club status. NZ NBL showed mixed 2025/2026 labels in page content, so verify season and event ID. Split TBF (official) from TBLStat (independent historical context). |

### 4. Cricket

| Need | Primary source | Audit finding |
|---|---|---|
| Laws and playing conditions | [MCC Laws](https://www.lords.org/mcc/about-the-laws-of-cricket), [ICC playing conditions](https://www.icc-cricket.com/about/cricket/rules-and-regulations/playing-conditions) | **Do not apply the published MCC 2026 edition before 2026-10-01** unless the competition already adopted a change in its playing conditions. ICC lists format-, gender- and event-specific current conditions; select the exact document. |
| Fixtures/results | [ICC fixtures/results](https://www.icc-cricket.com/fixtures-results); exact event page; official host board | Board examples verified: [BCCI](https://www.bcci.tv/), [ECB](https://www.ecb.co.uk/england/men/fixtures), [Cricket Australia](https://www.cricket.com.au/matches), [Bangladesh](https://www.tigercricket.com.bd/), [Ireland](https://cricketireland.ie/), [Afghanistan](https://www.acb.af/), [Sri Lanka](https://srilankacricket.lk/), [West Indies](https://www.windiescricket.com/). Official scorecard/toss XI controls. |
| Officials | [ICC match-official appointments](https://www.icc-cricket.com/about/cricket/match-officials/match-official-appointments) | Official page says appointments are provisional and may change; verify the match scorecard. |
| MLC | [Matches](https://www.majorleaguecricket.com/matches), [results](https://www.majorleaguecricket.com/matches/results), [stats](https://www.majorleaguecricket.com/stats), [fan FAQ](https://www.majorleaguecricket.com/fanfaq) | Official but JavaScript-heavy. Willow currently exposes an [MLC schedule](https://www.willow.tv/cricket-schedule/series/all); broadcast rights must be verified by season and territory. Seven/JioHotstar cannot remain permanent blanket registry claims. |
| Ball-by-ball/advanced | [Cricsheet](https://cricsheet.org/), [format documentation](https://cricsheet.org/format/) | High-quality independent structured archive, not an ICC/league official source. JSON is the preferred current format; coverage must be checked and missing matches declared. |

The host-broadcast pitch walkaround can be the best direct observation of the strip, but it is not a reason to withhold every cricket card automatically. Record reporter, same-match identity, timestamp, wording, strip/boundary details and access state. If it is unavailable, mark the pitch observation unknown and either pass markets that truly depend on it or proceed at an explicit confidence cap when the market is not surface-sensitive. Do not manufacture a pitch description from a generic preview.

### 5. Rugby league

Primary official chain: [NRL draw](https://www.nrl.com/draw/), [NRL stats](https://www.nrl.com/stats/), [official team-list topic](https://www.nrl.com/news/topic/team-lists/), [judiciary](https://www.nrl.com/news/topic/judiciary/), and [Casualty Ward](https://www.nrl.com/news/topic/casualty-ward/). The Casualty Ward route was intermittently fetchable; keep an honest dynamic/intermittent flag and use official club status when needed.

**Critical correction:** the official [2026 Round 1 team-list notice](https://www.nrl.com/news/2026/03/03/nrl-team-lists-round-1/) says two players are omitted 24 hours before kickoff and the **final 19 is named 90 minutes before kickoff**. Six players may be named on the interchange bench, but only four can enter. Replace every “final 17 one hour before kickoff” statement in the combined document (including its NRL module and universal availability gates). At kickoff, verify the actual 17/positions in the official match centre. Zero Tackle and League Unlimited can be labelled secondary fallbacks; remove the undefined `Legz` entry.

### 6. Soccer

| Scope | Primary chain | Note |
|---|---|---|
| FIFA World Cup | [Official tournament hub](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026), [FIFA Match Centre](https://www.fifa.com/en/match-centre), [official schedule update](https://inside.fifa.com/organisation/media-releases/updated-world-cup-2026-match-schedule-venues-kick-off-times-104-matches) | FIFA pages are JavaScript-heavy but official. Use official team sheet/match report for lineup, events and final. |
| Laws | [IFAB Laws](https://www.theifab.com/laws/latest/) | Pair with exact competition regulations for substitutions, extra time, shootouts and eligibility. |
| Premier League | [Fixtures](https://www.premierleague.com/en/fixtures), [club-by-club injuries](https://www.premierleague.com/en/news/4242565/club-by-club-injuries-article), official match centre and match-official articles | Predicted lineups are projections. Official match centre/club sheet at release controls. |
| MLS | [Schedule](https://www.mlssoccer.com/schedule/), [official stats](https://www.mlssoccer.com/stats/players/), official player-availability/disciplinary/roster pages | Reopen the dated availability report for the precise match; do not treat a persistent old injury URL as current without its through-date. |
| Advanced data | Official event stats; licensed Opta/Stats Perform/StatsBomb where held | Provider xG definitions differ. Store provider/model version and never splice xG series as though identical. FBref and public aggregators are secondary. |

The logged Argentina Torneo Promocional Amateur is real; official AFA sources include the [draw](https://www.afa.com.ar/es/posts/se-realizo-el-sorteo-del-torneo-promocional-amateur), [programming/officials](https://www.afa.com.ar/es/posts/programacion-y-arbitros-de-la-proxima-fecha-de-la-primera-b-primera-c-y-promocional-amateur), [regulations index](https://www.afa.com.ar/11608/reglaments/torneos-superiores?s=6) and an [official 2026 bulletin](https://assets1.afa.com.ar/2026/BOLETINES/Boletin-Resoluciones-6895-%2815-05-2026%29.pdf). It has no rich official public advanced/injury feed; record that absence rather than filling it with an aggregator.

The Peru Copa Caliente de la Liga is also real, but no stable official match-centre endpoint was verified in this audit. [TVPerú's state-broadcaster explainer](https://tvperu.gob.pe/noticias/deportes/copa-caliente-de-la-liga-2026-fecha-de-inicio-fixture-grupos-formato-y-premios) is a dated secondary source. Require LFPP/FPF/official club or official broadcast material for decisive event facts and mark the official-feed gap honestly.

### 7. Ice hockey

| Scope | Primary chain | Note |
|---|---|---|
| NHL | [Schedule](https://www.nhl.com/schedule), [NHL Stats](https://www.nhl.com/stats/), [NHL EDGE](https://edge.nhl.com/), [teams/rosters](https://www.nhl.com/info/teams), official Game Centre/game reports | EDGE is official tracking-derived advanced data. There is no verified comprehensive central NHL injury report; use official team communications and treat projected lineups/goalies as projected until team/warmup/game sheet. `api-web.nhle.com/v1` is official-host but should be schema-monitored rather than promised as a supported public API. |
| IIHF | [2026 Worlds schedule/results](https://www.iihf.com/en/events/2026/wm/schedule), [official documents/line-ups/game summaries](https://www.iihf.com/en/events/2026/wm/tournamentinfo/officialdocuments), [rules/regulations](https://www.iihf.com/en/static/55352/rules_regulations_guidelinesspan) | Select the rulebook tied to the event. The May 2026 World Championship used the 2025-26 family; the site now also publishes 2026-27 material. Newest is not automatically effective for an earlier event. |

Scouting the Refs may discover daily assignments but is unofficial. The official game sheet/Game Centre is the final assignment source.

### 8. American football

| Scope | Primary chain | Note |
|---|---|---|
| NFL | [Schedules](https://www.nfl.com/schedules), [stats](https://www.nfl.com/stats), [Next Gen Stats](https://nextgenstats.nfl.com/), [injuries](https://www.nfl.com/injuries/), [transactions](https://www.nfl.com/transactions/), [inactives](https://www.nfl.com/inactives/), [Football Operations rulebook](https://operations.nfl.com/the-rules/nfl-rulebook/) | Inactives are the final participation gate in season. As of the audit, the generic rulebook route exposed the 2025 rulebook; [2026 playing-rule proposals](https://operations.nfl.com/media/dxfj3uak/2026-playing-rules-bylaw-and-resolution-proposals.pdf) are proposals, not the final rulebook. Football Zebras is an independent assignment tracker; official gamebook is final. |
| NCAA football | [NCAA FBS stats](https://www.ncaa.com/stats/football/FBS), [football rules](https://www.ncaa.org/championships/playing-rules/football-playing-rules/), official NCAA scoreboard plus school/conference game notes | No central match-availability report was verified. School/conference/team communication controls reported status; game participation/gamebook controls final. Public EPA/success-rate providers are independent unless licensed; label provider and methodology. |

### 9. Tennis and golf

| Sport | Primary chain | Note |
|---|---|---|
| Tennis | [Wimbledon order of play](https://www.wimbledon.com/en_GB/scores/schedule/schedule2.html), [Wimbledon scores schedule](https://www.wimbledon.com/en_GB/scores/schedule/index.html?embed=true), [ITF 2026 Wimbledon draws/results](https://www.itftennis.com/en/tournament/wimbledon/gbr/2026/w-sl-gbr-2026-001/draws-and-results/), [ATP rulebook](https://www.atptour.com/en/corporate/rulebook), [2026 ATP calendar](https://www.atptour.com/en/news/what-is-the-2026-atp-tour-calendar), [WTA rules](https://www.wtatennis.com/wta-rules), [WTA rankings](https://www.wtatennis.com/rankings/singles/) | Tournament draw/order/withdrawal and official match page control. There is no universal official predictive injury report; entry does not prove fitness. Advanced public sites are secondary. |
| PGA Tour/golf | [2026 PGA Tour schedule](https://www.pgatour.com/schedule/2026), [official leaderboard/field/tee times](https://www.pgatour.com/leaderboard), [PGA Tour stats](https://www.pgatour.com/stats/stats) | For majors, the championship organiser's page is final (the PGA page may say scoring supplied by The Open, etc.). ShotLink/PGA Tour stats are official for covered events. Capture field/withdrawal and tee time after release. |

## Weather, venue and roof policy

Split the registry's `Open-Meteo / official weather services` row. Primary government services are [Australia BOM](https://www.bom.gov.au/weather-and-climate), [US National Weather Service](https://www.weather.gov/), [UK Met Office](https://weather.metoffice.gov.uk/forecast/uk), [Environment Canada](https://www.weather.gc.ca/), [Korea Meteorological Administration](https://www.weather.go.kr/w/index.do), [Japan Meteorological Agency](https://www.jma.go.jp/bosai/forecast/), [India Meteorological Department](https://mausam.imd.gov.in/) and Mexico's [SMN/CONAGUA](https://smn.conagua.gob.mx/). Open-Meteo is a useful secondary model aggregator/API, not a national authority.

Store venue coordinates, forecast issue time, valid time, units, precipitation probability/amount, wind mean/gust/direction, temperature/humidity and warning state. Official league fixture/match centre controls venue; official venue/event/game centre controls roof/surface state. Do not apply outdoor weather to a closed/domed venue, and do not infer roof state from a weather forecast.

## Odds and market-timing policy

Odds should remain excluded unless the user authorizes market inputs. When authorized, a sportsbook/exchange is primary only for **its own** price. Licensed providers can aggregate quotes but are not official results authorities.

Verified technical references include Betfair's [Exchange API type definitions](https://betfair-developer-docs.atlassian.net/wiki/spaces/1smk3cen4v3lu3yomq5qye0ni/pages/2687465), which distinguish market ID, delayed data, `OPEN/SUSPENDED/CLOSED`, `inplay`, last-match time and market version; and Sportradar's [Odds API overview](https://developer.sportradar.com/odds/reference/intro), [market-status documentation](https://docs.sportradar.com/uof/data-and-features/markets-and-outcomes/market-status), and [timestamp/availability FAQ](https://developer.sportradar.com/odds/reference/oc-futures-faq).

Required snapshot fields: operator/provider, jurisdiction, account/data-delay status, sport/competition/event IDs, scheduled start, market ID/type/rules, selection, line/handicap, decimal price, back/lay side if exchange, available size where available, market status, in-play flag, source publish time, `observed_at_utc`, raw response/screenshot hash. Define “close” before analysis as the last **open, unsuspended, pre-start** quote from the same operator and market. Never reconstruct an opening/close from a later aggregator page, mix books, or use post-start prices in a pregame backtest.

## Probabilistic forecasting, calibration and validation research

### Primary research basis

- Brier's original probability-score paper: [Brier (1950)](https://doi.org/10.1175/1520-0493%281950%29078%3C0001%3AVOFEIT%3E2.0.CO%3B2).
- Proper scoring rules and why forecast evaluation must reward honest probabilities: [Gneiting & Raftery (2007)](https://doi.org/10.1198/016214506000001437).
- Calibration as long-run agreement between quoted probabilities and event frequencies: [Dawid (1982)](https://doi.org/10.1080/01621459.1982.10477856).
- Calibration, sharpness and distributional diagnostics: [Gneiting, Balabdaoui & Raftery (2007)](https://doi.org/10.1111/j.1467-9868.2007.00587.x).
- Stable, reproducible reliability diagrams using CORP/PAV rather than arbitrary hand-picked buckets: [Dimitriadis, Gneiting & Jordan (2021)](https://doi.org/10.1073/pnas.2016191118).
- Empirical probability calibration and the need to fit calibration out of sample: [Niculescu-Mizil & Caruana (2005)](https://doi.org/10.1145/1102351.1102430).
- Time-series cross-validation qualifications: [Bergmeir, Hyndman & Koo (2018)](https://doi.org/10.1016/j.csda.2017.11.003).
- Paired predictive-accuracy testing: [Diebold & Mariano (1995)](https://doi.org/10.1080/07350015.1995.10524599).
- Protection against model-search/data-snooping false discoveries: [White (2000)](https://doi.org/10.1111/1468-0262.00152).
- Sport-model examples that support count baselines but not blind raw Poisson: [Dixon & Coles (1997)](https://doi.org/10.1111/1467-9876.00065), [Karlis & Ntzoufras (2003)](https://doi.org/10.1111/1467-9884.00366), [Baio & Blangiardo (2010)](https://doi.org/10.1080/02664760802684177), and [Hvattum & Arntzen (2010)](https://doi.org/10.1016/j.ijforecast.2009.10.002).

### Process correction

The workspace currently treats a result as a win/loss and then creates many narrative lessons. That is not enough to know whether stated probabilities are good. One 80% forecast can lose without being an error; repeated 80% forecasts winning materially less than 80%, or showing inferior proper scores to a baseline, is evidence of miscalibration.

Adopt this minimum protocol:

1. **Immutable forecast snapshot:** unique prediction ID, created/cutoff time, model/data/source versions, exact information set, rules/lineup status and probabilities for all mutually exclusive outcomes. Never overwrite a forecast after lineup or live information arrives; issue a new version.
2. **Predeclared target and settlement:** event, horizon, market rules, push/void handling and outcome source. Separate regulation-only from advancement/OT/shootout and other sport-specific settlement states.
3. **Chronological nested evaluation:** expanding/rolling training windows; all feature engineering and hyperparameter/decay/window selection inside the training fold; a separate rolling calibration set; untouched forward test. Random match shuffling is inappropriate under roster/rule/regime drift except under explicit dependence assumptions that have been checked.
4. **Baselines:** unconditional league rate, season/team rate, simple Elo/rating, transparent sport-native count model, and market probability only when authorized and cleanly de-vigged. A complex model must beat simple baselines out of sample.
5. **Proper scores:** log loss and Brier score for binary outcomes; multiclass log/Brier/ranked probability score where appropriate; CRPS or distributional score for continuous/count distributions. Report mean score and paired difference versus baseline with uncertainty, not only hit rate.
6. **Calibration and discrimination:** calibration-in-the-large, calibration slope, CORP reliability plot with uncertainty, sharpness/distribution of forecast probabilities, and discrimination. The fixed 50-59/60-69/70-79/80+ buckets in the ledger are too coarse and unstable on small samples.
7. **Dependence-aware uncertainty:** resample by date/round/series or another defensible block; do not treat multiple picks from one match as independent. Report effective sample size and confidence intervals.
8. **Multiple-testing control:** log every tried feature/window/model, freeze a champion before the forward period, and use a final holdout or data-snooping correction when many variants were searched. Do not mint a new hard rule from a single miss.
9. **Segment only with support:** sport, competition, market family, pregame/live, lineup-confirmed/projected, season/rules regime and probability band. Use partial pooling or mark insufficient `N`; do not publish a “95%” rate from a handful of correlated selections.
10. **Operational decision layer:** probabilities come first. Ranking, confidence labels and any wager/edge decision are downstream utilities with their own thresholds. Closing-line value is a market benchmark, not proof that an outcome forecast was correct.

Recommended ledger additions: exact `probability` (not just bucket), complete outcome probability vector, `forecast_created_at_utc`, `information_cutoff_at_utc`, `event_start_at_utc`, `model_version`, `feature_snapshot_hash`, `source_snapshot_ids`, `calibrator_version`, `train_end`, `calibration_end`, `test_fold`, `baseline_probabilities`, `brier_contribution`, `log_loss_contribution`, `RPS/CRPS`, `paired_loss_delta`, `market_snapshot_id`, and `correlation_cluster_id`.

## Explicit edits to make in v2

### Delete or demote

- Delete the mandatory StatMuse-first rule. Replace with “official/sport-native source first; StatMuse optional discovery/query cross-check; validate every returned qualifier and date.”
- Replace mandatory X/Reddit checks with optional discovery. Never claim a blocked route was checked.
- Remove “domain-verified Bluesky = Tier A-equivalent.”
- Move `r.jina.ai` out of the source table into an access-method table; citations must name the underlying publisher.
- Remove TotalCorner as a settlement source. Official match stats/game report should control; an aggregator may cross-check only.
- Remove undefined `Legz` and blanket broadcast-rights assumptions.
- Demote ESPN public endpoints to undocumented secondary cross-check; official competition/event sources settle.
- Demote Guardian live pages to context/cross-check, not final settlement when an official match report exists.
- Replace the universal four-window/every-player rule with predeclared market-relevant windows plus `N`, through-date, continuity and uncertainty.

### Split or relabel

- Split TBF official and TBLStat independent.
- Split national meteorological services and Open-Meteo.
- Label AFLUA as the umpires' association, not AFL official.
- Label Zero Tackle/League Unlimited, Scouting the Refs and Football Zebras as independent.
- Label ASAP Sports as independent transcript provider; official league/team video/transcript is primary when available.
- Label Cricsheet independent specialist data, not official cricket authority.
- Label MLB/NHL official-host JSON routes as undocumented interfaces unless their publishers document support.

### Correct immediately

- Repair the malformed rules table and UTF-8 mojibake (`â€”`, etc.).
- Change the document title/update timestamp and give every row an actual `observed_at`/`data_through`/`effective_from` value.
- NRL: final 19 at 90 minutes in the 2026 process, then verify actual 17/positions at kickoff.
- FIBA: 2024 rules remain effective until 2026-10-01 unless exact competition regulations say otherwise.
- MCC: published 2026 Laws take effect 2026-10-01; current ICC/event playing conditions may already incorporate individual changes.
- NFL: do not call proposals a rulebook or assume the generic URL's year; record the PDF title/year actually opened.
- NBA injury report: make the URL season-specific metadata and create separate WNBA/Summer League availability chains.
- IIHF: bind the rulebook to the event rather than selecting the newest posted PDF.

## Bottom line

The source failures are fixable, but the repair is not “add more sites.” It is to make authority fact-specific, preserve effective dates and cutoff-time evidence, distinguish source from access proxy, declare real coverage gaps, and evaluate probabilities chronologically with proper scores and uncertainty. Those changes directly address the pattern of confident but poorly supported predictions far better than more mandatory searches or more overlapping recent-form windows.

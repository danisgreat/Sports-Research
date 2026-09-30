# Previous Sports Results — data source implementation guide

**Written 2026-09-30 (AEST).** Every access status below comes from a live request made on 2026-09-30 from the research environment, not from memory. A source marked VERIFIED returned HTTP 200 with the expected content. Re-test before relying on any route: sites change.

This guide says **where** to get each field for each competition folder. The companion [explanation document](COVERAGE_AND_BLANK_YEARS.md) says **which years** have no competition, which fields cannot be recovered for which eras, and where the current folder statuses are wrong.

## 1. What gets populated

| File | Content | Primary field owner |
|---|---|---|
| `<Year>/<Year>_games.csv` | One row per game: number, type, teams, home/away, venue, date, score, total, margin, notable players, one-line comment | The competition's own record, then a statistical database (sections 4+) |
| `<Year>/COACHES.md` | Head coach and senior staff per team for that season, with mid-season changes and dates | Club or league record, then a reference database |
| `<Year>/OFFICIATING.md` | Referees/umpires for the competition that year, and per game where available | League officials record, then match reports and newspapers |
| `HISTORICAL_PLAYERS_AND_ROSTERS.md` | Players and the team(s) they played for, by year | Season rosters or per-game line-ups |

## 2. Rules for populating

1. **Field owner first.** Use the competition's own record, then an established statistical database, then a newspaper report. Wikipedia and search results are discovery only: confirm every value on a primary source.
2. **Never** use betting, odds, tipster, fantasy/DFS or AI-generated recap sites (`SOURCES.md` §1.4). Some data files (nflverse `games.csv`, football-data.co.uk) carry betting columns: read only score, date, venue and official columns.
3. **Record provenance.** For each season, add a `Sources` line to `COACHES.md` and `OFFICIATING.md` (URL, retrieval date), and keep a per-year source note for the CSV. A value without a source is left blank.
4. **Blank means unknown, not zero.** If a field cannot be sourced, leave it blank and say why in the season file, using the reasons in the explanation document.
5. **No scraping of blocked sites.** Sources marked BROWSER ONLY or PAYWALL are for manual reading within their terms. Do not automate around Cloudflare, Akamai or paywalls.
6. **Rate limits.** Wikipedia, worldfootball.net and Transfermarkt throttle quickly. Pause between requests and cache responses (the `_football_research/sources/` cache pattern works).
7. **Season-year convention.** Follow the convention in the explanation document §2 before filing any split-season or postponed event.

## 3. Source catalogue (tested 2026-09-30)

Status key: **VERIFIED** 200 with expected content · **VERIFIED (browser UA)** needs a browser user-agent (403 to a plain request) · **HOME ONLY** site reachable, deeper routes untested · **BROWSER ONLY** automated requests blocked here (Cloudflare, Akamai or a bot check) · **FREE KEY** API needs free registration · **PAYWALL** · **UNREACHABLE** 404/DNS/TLS failure · **EXCLUDED** must not be used.

### Cross-sport and historical archives

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `WIKI` | Wikipedia (Action API / REST) | `https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&page=<Title>` | **VERIFIED** | Season lists, formats, champions tables. DISCOVERY ONLY: confirm every fact on a primary source. Rate-limits (HTTP 429) under load; send a descriptive user-agent and pause between calls. |
| `OLY` | Olympedia | `https://www.olympedia.org/sports/<CODE> (BKB basketball, BBL baseball, FBL football, HOC hockey, IHO ice hockey, TEN tennis)` | **VERIFIED** | Every Olympic tournament: results and each team's entered players. Sport pages verified; event pages were not opened in this pass. |
| `ESPN` | ESPN site API | `https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/scoreboard?dates=YYYYMMDD and /summary?event=<id>` | **VERIFIED** | Modern results, line/box scores, rosters and (for some leagues) officials. Verified today for NBA, NFL, college football, UFL (football/ufl), CFL (football/cfl), MLB, soccer, rugby union (164205), rugby league (3) and IPL cricket (8048). Plain request; quarantine odds keys. |
| `IA` | Internet Archive | `https://archive.org/advancedsearch.php?q=<query>&output=json` | **VERIFIED** | Scanned media guides, record books, programmes and yearbooks: often the only source for historical coaching staffs and officials. |
| `LA84` | LA84 Foundation digital library | `https://digital.la84.org/` | **VERIFIED** | Digitised sports periodicals and Olympic official reports. |
| `DELPHER` | Delpher (Dutch newspapers) | `https://www.delpher.nl/` | **VERIFIED** | Dutch newspaper archive: Hoofdklasse and Dutch football/hockey line-ups and officials. |
| `TROVE` | Trove (National Library of Australia) | `https://trove.nla.gov.au/` ; `API https://api.trove.nla.gov.au/v3/` | **FREE KEY** | Australian newspapers: team lists, umpires, coaches and scores for AFL/VFL, state leagues, NRL, cricket, NBL. Web search shows a bot check here; the v3 API returns 401 without a free key. |
| `PAPERSPAST` | Papers Past (National Library of New Zealand) | `https://paperspast.natlib.govt.nz/` | **BROWSER ONLY** | NZ newspapers: Plunket Shield, NZ rugby and provincial rugby line-ups and referees. |
| `CHRONAM` | Chronicling America / Library of Congress | `https://chroniclingamerica.loc.gov/` ; `https://www.loc.gov/collections/chronicling-america/` | **BROWSER ONLY** | US newspapers to 1963: box scores, umpires, college football line-ups and officials. |
| `GALLICA` | Gallica (Bibliothèque nationale de France) | `https://gallica.bnf.fr/` | **BROWSER ONLY** | French newspapers (L'Auto, L'Équipe predecessors): Top 14, French football, LNB and Roland-Garros history. Returned a security-check page here. |
| `BNA` | British Newspaper Archive | `https://www.britishnewspaperarchive.co.uk/` | **PAYWALL** | UK newspapers: county cricket, rugby league/union, football line-ups and officials. Subscription; security check here. |
| `STATSCREW` | Stats Crew | `https://www.statscrew.com/` | **HOME ONLY** | Historical standings and rosters for minor/secondary leagues (minor-league baseball, AHL/ECHL, CFL). Deep pages not tested. |
| `SPORTSREF` | Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead | `https://www.baseball-reference.com/` ; `https://www.pro-football-reference.com/` ; `https://www.sports-reference.com/cfb/` | **BROWSER ONLY** | Complete seasons, rosters, coaches and (PFR) game officials. Cloudflare 403 here, also through the r.jina.ai proxy. Open manually in a browser; never scrape. |

### Soccer

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `WF` | worldfootball.net | `https://www.worldfootball.net/all_matches/<competition-slug>-<season>/` ; `/report/<match>/` ; `/teams/<club>/<year>/2/` ; `/referees/<competition>-<season>/1/` | **VERIFIED (browser UA)** | Fixtures and results by season (verified back to English 1899-1900, Serie A 1929-30, Ligue 1 1932-33, World Cup 1930, European Cup 1955-56, Copa América 1916); match reports with line-ups and referee (World Cup 1930 verified); club season squads with coach (Juventus 1930, Real Madrid 1956 verified); referee season tables. Some slugs differ (La Liga 1929 and Frauen-Bundesliga 1990-91 guesses returned 404): navigate from the competition page. |
| `TM` | Transfermarkt | `https://www.transfermarkt.com/<comp>/gesamtspielplan/wettbewerb/<CODE>/saison_id/<YYYY>` ; `/schiedsrichter/wettbewerb/<CODE>/saison_id/<YYYY>` ; `/<club>/mitarbeiterhistorie/verein/<id>` | **VERIFIED** | Fixtures (La Liga 1950 verified), referee lists per season (Premier League 2023-24 verified), club coaching-staff history (Arsenal verified), squads per season. |
| `RSSSF` | RSSSF | `https://www.rsssf.org/` | **VERIFIED** | League tables, results and international match details back to the 19th century (England 1901-02 verified). Page URLs vary; start from the index. |
| `11V11` | 11v11 (AFS) | `https://www.11v11.com/` | **VERIFIED** | English football history: tables (1905 verified), results and line-ups. |
| `OPENFB` | openfootball (GitHub) | `https://raw.githubusercontent.com/openfootball/<repo>/master/<season>/<file>.txt` | **VERIFIED** | Plain-text fixtures/results (England 2023-24 and World Cup 1930 verified). Results only. |
| `FIFAAPI` | FIFA API | `https://api.fifa.com/api/v3/calendar/matches?idCompetition=<id>&idSeason=<id>&language=en` | **VERIFIED** | FIFA tournaments: every match with stadium and an Officials block (verified for a World Cup season). Line-ups via the live/match endpoints. |
| `PLAPI` | Premier League pulselive API | `https://footballapi.pulselive.com/football/fixtures?comps=1&compSeasons=<id>` | **VERIFIED** | Premier League fixtures, line-ups, officials, match stats (see SOURCES.md §3.4). |
| `DFB` | DFB Datencenter | `https://www.dfb.de/datencenter/` | **VERIFIED** | German competitions (Bundesliga, Frauen-Bundesliga): fixtures, line-ups, referees. |
| `MLS` | MLSsoccer.com | `https://www.mlssoccer.com/schedule/scores` | **VERIFIED** | MLS schedule, results and match centre. |
| `NWSL` | NWSL official | `https://www.nwslsoccer.com/schedule/regular-season` | **VERIFIED** | NWSL schedule, results, match centre. |
| `UAL` | Ultimate A-League | `https://www.ultimatealeague.com/ (match pages ?match_id=<n>; /referees/)` | **VERIFIED** | A-League Men and Women history: match pages, line-ups, referee register. |
| `CONMEBOL` | CONMEBOL | `https://www.conmebol.com/` | **VERIFIED** | Libertadores and Copa América official site. |
| `NFT` | National-Football-Teams.com | `https://www.national-football-teams.com/` | **VERIFIED** | International squads and caps (World Cup, Euros, Copa América, Asian Cup, AFCON, Gold Cup). |
| `FBREF` | FBref / BDFutbol / kicker | `https://fbref.com` ; `https://www.bdfutbol.com` ; `https://www.kicker.de` | **BROWSER ONLY** | Cloudflare 403 here. BDFutbol is the best La Liga history source (coaches, referees) if opened manually. |

### Basketball

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `BREF` | Basketball-Reference | `https://www.basketball-reference.com/leagues/NBA_<YYYY>.html` ; _coaches.html ; `/referees/<YYYY>_register.html` ; `/wnba/years/<YYYY>.html` ; `/gleague/years/<YYYY>.html` | **VERIFIED** | NBA/BAA from 1946-47, WNBA from 1997, G League: games, rosters, coaches (BAA 1947 and WNBA 1997 coach pages verified). Referee registers exist from 1989-90 (1988-89 and earlier returned 404). |
| `NBAOFF` | NBA Official referee assignments | `https://official.nba.com/referee-assignments/` | **VERIFIED** | Current-season crews per game (not an archive). |
| `REALGM` | RealGM | `https://basketball.realgm.com/` | **VERIFIED (browser UA)** | Rosters and staff for NBA and international leagues. |
| `ELAPI` | EuroLeague / EuroCup data feeds | `https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/<E or U>/seasons/<E or U><YYYY>/games` ; `https://api-live.euroleague.net/v2/competitions/E/seasons/E<YYYY>/games/<n>` | **VERIFIED** | EuroLeague game lists back to E2000 (2000-01 season) and EuroCup (U2023 verified); the live game header carries referee1-referee4 (E2024 verified). Roster and coach fields per game were not checked. |
| `GENIUS` | FIBA LiveStats (Genius Sports) game JSON | `https://fibalivestats.dcd.shared.geniussports.com/data/<gameId>/data.json` | **VERIFIED** | Box score, both rosters and an officials block (fields verified on game 2382853). Works for any competition whose match centre exposes a FIBA LiveStats game ID; which leagues do so was not surveyed. |
| `ACB` | ACB (Liga Endesa) | `https://www.acb.com/es/liga/partidos?temporada=<YYYY>` ; `https://live.acb.com/es/partidos/<slug>-<id>/estadisticas` | **VERIFIED** | Fixtures page accepts a season parameter (1983 request returned the fixtures page; its contents were not checked); live.acb.com game pages embed the box score with starters and head coaches (verified for match 105380, 2026-09-30). |
| `LNB` | LNB (Betclic Élite) | `https://www.lnb.fr/elite/calendrier-resultats` | **VERIFIED** | French league fixtures and results. |
| `LBA` | Lega Basket Serie A | `https://www.legabasket.it/lba/calendario` | **VERIFIED** | Italian league fixtures and results. |
| `ESAKE` | ESAKE (Greek Basket League) | `https://www.esake.gr/` | **VERIFIED** | Greek league official site. |
| `ABA` | ABA League | `https://www.aba-liga.com/calendar/` | **VERIFIED** | Adriatic league calendar and game centre. |
| `KBL` | KBL | `https://www.kbl.or.kr/` | **VERIFIED** | Korean league official site. |
| `BLG` | B.LEAGUE | `https://www.bleague.jp/schedule/` | **VERIFIED** | Japanese league schedule and results. |
| `CBA` | CBA | `https://www.cbaleague.com/` | **HOME ONLY** | Chinese league official site (JavaScript page). |
| `PBA` | PBA | `https://www.pba.ph/` | **VERIFIED** | Philippine league official site. |
| `VTB` | VTB United League | `https://vtb-league.com/en/` | **HOME ONLY** | League official site. |
| `BBL` | easyCredit BBL | `https://www.easycredit-bbl.de/` | **HOME ONLY** | German league official site. |
| `BSLTBF` | TBF (Turkish BSL) | `https://www.tbf.org.tr/` | **BROWSER ONLY** | Cloudflare challenge here. |
| `NBLAPI` | NBL schedule API | `https://schedule.nbl.com.au/api/calendar/schedule?league=NBL&year=<start_year>` | **VERIFIED** | NBL fixtures/results (see SOURCES.md §3.2). |
| `NBL1` | NBL1 | `https://nbl1.com.au/` | **VERIFIED** | NBL1 site; games run on FIBA LiveStats. |
| `WNBL` | WNBL | `https://wnbl.basketball/` | **BROWSER ONLY** | TLS handshake failure direct; Cloudflare through the proxy. |
| `EUROBASKET` | Eurobasket.com | `https://basketball.eurobasket.com/` | **HOME ONLY** | International rosters and league history (deep pages not tested). |
| `PROBALLERS` | Proballers | `https://www.proballers.com/` | **BROWSER ONLY** | Cloudflare 403 on 2026-09-30 (SOURCES.md listed it as 200 on 2026-09-28). |

### Baseball

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `RETRO` | Retrosheet | `https://www.retrosheet.org/gamelogs/index.html (gl<YYYY>.zip)` ; `/boxesetc/<YYYY>/Y_<YYYY>.htm` | **VERIFIED** | MLB game logs 1871 onward: every game with score, home-plate umpire, both managers and starting line-ups (1901 file verified). Season, player, manager and umpire pages. |
| `MLBAPI` | MLB Stats API | `https://statsapi.mlb.com/api/v1/...` | **VERIFIED** | schedule (1950 verified), teams/&lt;id&gt;/roster?season= (1927 verified), teams/&lt;id&gt;/coaches?season= (1920: manager only; 1950: manager and coaches), game/&lt;pk&gt;/boxscore officials (1950: home-plate umpire only). sportId 51 = WBC (2023 verified), 23 = Mexican League (2019 verified), 11 = Triple-A (2005 verified). |
| `LAHMAN` | Lahman Baseball Database (SABR) | `https://sabr.org/lahman-database/` | **VERIFIED** | Season rosters (Appearances), Managers, Teams tables 1871 onward. The Chadwick GitHub mirror returned 404. |
| `SABRBIO` | SABR BioProject | `https://sabr.org/bioproject/` | **VERIFIED** | Biographies of players, managers and umpires. |
| `NPB` | NPB.jp | `https://npb.jp/bis/history/` ; `https://npb.jp/bis/eng/<YYYY>/games/` | **VERIFIED** | Japanese records history (Japanese) and English game results. |
| `KBO` | KBO | `https://www.koreabaseball.com/Record/History/Team/Record.aspx` | **VERIFIED** | Korean league history and records. |
| `STATIZ` | Statiz | `https://statiz.co.kr/` | **VERIFIED** | KBO historical statistics (independent). |
| `CPBL` | CPBL | `https://www.cpbl.com.tw/` | **HOME ONLY** | Taiwanese league site (HTTP 308 redirect not followed by the test client; see SOURCES.md §3.1). |
| `LMB` | Liga Mexicana de Béisbol | `https://www.lmb.com.mx/` | **VERIFIED** | Mexican League official site. |
| `ABL` | Australian Baseball League | `https://theabl.com.au/` | **VERIFIED** | ABL official site. |
| `WBSC` | WBSC | `https://www.wbsc.org/en/calendar` | **VERIFIED** | Premier12, Olympic qualifiers and WBSC events. |
| `PURAPELOTA` | Pura Pelota (LVBP history) | `https://www.purapelota.com/` | **UNREACHABLE** | TLS certificate failure here. |

### Ice hockey

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `HREF` | Hockey-Reference | `https://www.hockey-reference.com/leagues/NHL_<YYYY>.html` ; `/boxscores/<id>.html` | **VERIFIED** | NHL from 1917-18: seasons, rosters, coaches, box scores (1918 season and a 1950 box verified). No game officials found on box-score pages. |
| `NHLAPI` | NHL api-web | `https://api-web.nhle.com/v1/roster/<TEAM>/<YYYYYYYY>` ; `/v1/gamecenter/<gameId>/right-rail` | **VERIFIED** | Season rosters (Montreal 1950-51 verified); right-rail game info lists referees, linesmen, head coaches and scratches (2023-24 verified). A 1949-50 game-centre request returned 404. |
| `NHLREC` | NHL Records API | `https://records.nhl.com/site/api/franchise` | **VERIFIED** | Franchise and records data (the officials endpoint returned 403). |
| `EP` | Elite Prospects | `https://www.eliteprospects.com/league/<league>/<YYYY-YYYY>` ; `/team/<id>/<slug>/<YYYY-YYYY>?tab=staff` | **VERIFIED** | League-season rosters for AHL (1936-37 verified), ECHL (1988-89), DEL (1994-95), Czech Extraliga (1993-94), Swiss NLA (1990-91), SHL (1975-76), Liiga (1975-76), KHL; team staff tab (head coaches) verified. AIHL and PWHL league pages returned no player list. |
| `HDB` | HockeyDB | `https://www.hockeydb.com/` | **VERIFIED** | Standings and rosters for NHL, AHL (IAHL 1936-37 verified), ECHL and other leagues. |
| `LIIGAAPI` | Liiga API | `https://liiga.fi/api/v2/games?tournament=runkosarja&season=<YYYY>` ; `/api/v2/games/<season>/<id>` | **VERIFIED** | Every Liiga game; game detail lists referees and linesmen (verified). |
| `IIHF` | IIHF | `https://www.iihf.com/en/events/<YYYY>/<code>/schedule` | **VERIFIED** | Current IIHF championship schedules and results (older event URLs redirect to the home page). |
| `HARCH` | Hockey Archives | `https://www.hockeyarchives.info/` | **VERIFIED** | French-language history of World Championships and European leagues (1930 World Championship page verified). |
| `HHOF` | Hockey Hall of Fame | `https://www.hhof.com/` | **VERIFIED** | Historical registers including officials and builders. |
| `HOCKEYLEAGUES` | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL | `https://www.shl.se` ; `https://www.penny-del.org` ; `https://www.hokej.cz` ; `https://www.nationalleague.ch` ; `https://www.thepwhl.com` ; `https://theahl.com` ; `https://www.echl.com` | **HOME ONLY** | Current seasons (home pages verified 200). |
| `KHL` | KHL | `https://en.khl.ru/` | **HOME ONLY** | HTTP 307 redirect loop for the test client; open in a browser. |
| `AIHL` | AIHL | `https://theaihl.com/` | **BROWSER ONLY** | JavaScript redirect; Cloudflare through the proxy. |

### Australian football

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `AFLT` | AFL Tables | `https://afltables.com/afl/seas/<YYYY>.html` ; `/afl/stats/games/<YYYY>/<id>.html` ; `/afl/stats/coaches/coaches_idx.html` | **VERIFIED** | Every VFL/AFL game from 1897 with player line-ups and scores, season pages (Grand Final present in every season 1898-1931 except 1897 and 1924), coaches index. No umpire pages found. The AFLW URL tried returned 404. |
| `AFLAPI` | AFL API (aflapi.afl.com.au) | `https://aflapi.afl.com.au/afl/v2/competitions` ; `/competitions/<id>/compseasons` ; `/matches?compSeasonId=<id>` | **VERIFIED** | Competitions AFL, AFLW, VFL, VFLW, WAFL, SANFL. AFL premiership seasons available 2012-2026 only. Match lists carry no umpire fields. |
| `AFLSTATS` | AFL Stats Pro (api.afl.com.au) | `https://api.afl.com.au/statspro/playersStats/seasons/<providerId> (token from https://api.afl.com.au/cfs/afl/WMCTok)` | **VERIFIED** | (Verified through the collector's cached responses in _football_research/sources.) Player season totals for AFL, AFLW, VFL, VFLW, SANFL, WAFL seasons in the AFL API (used by the collector in _football_research). |
| `SQUIGGLE` | Squiggle API | `https://api.squiggle.com.au/?q=games;year=<YYYY>` | **VERIFIED** | Every VFL/AFL game from 1897 (1900 verified): scores, venues. Its 'tips' endpoint is excluded. |
| `FOOTYWIRE` | Footywire | `https://www.footywire.com/afl/footy/ft_match_list?year=<YYYY>` | **VERIFIED** | Modern AFL match lists, line-ups and player stats. |
| `AUSFOOTY` | Australian Football (australianfootball.com) | `https://australianfootball.com/` | **HOME ONLY** | Player and coach profiles across AFL and state leagues. |
| `WAFLFF` | WAFL FootyFacts | `https://www.waflfootyfacts.net/season/games/results.php?Season=<YYYY>` | **VERIFIED** | Every WAFL season 1885-2026 listed: results, team lists, records. |
| `SPORTIX` | Sportix statistics API (WAFL) | `https://api.sportix.cloud/public/statistics?competition=<id>&season=<id>` | **VERIFIED** | WAFL player statistics; the collector found player data only from 1994. |
| `STATELEAGUES` | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland | `https://sanfl.com.au` ; `https://wafl.com.au` ; `https://www.vfl.com.au` ; `https://www.aflnt.com.au/ntfl` ; `https://www.aflq.com.au` | **HOME ONLY** | Current fixtures, results and match centres (home pages verified). |
| `FPF` | Full Points Footy (fullpointsfooty.net) | `https://fullpointsfooty.net/` | **EXCLUDED** | The domain now serves a betting-prediction spam site. Older Wikipedia citations point to it; use archived copies on web.archive.org only. |

### Rugby league

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `RLP` | Rugby League Project | `https://www.rugbyleagueproject.org/seasons/<comp>-<YYYY>/results.html` ; `/referees/` | **VERIFIED** | NSWRFL/NRL from 1908, Super League (1996 verified), State of Origin (1980 verified), World Cups (1954 verified), NRLW (2018 verified): results, team lists, referees (NRL 2024 results carry referees; referee register verified), coaches. |
| `NRLAPI` | NRL draw API | `https://www.nrl.com/draw/data?competition=111&season=<YYYY>&round=<n>` | **VERIFIED** | NRL fixtures and match centre links (see SOURCES.md §3.6). |
| `RLSITES` | Super League / RFL / League Unlimited | `https://www.superleague.co.uk` ; `https://www.rugby-league.com` ; `https://leagueunlimited.com` | **HOME ONLY** | Current fixtures, results and team lists. |

### Rugby union

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `WRAPI` | World Rugby match API (pulselive) | `https://api.wr-rims-prod.pulselive.com/rugby/v3/match?startDate=YYYY-MM-DD&endDate=YYYY-MM-DD&pageSize=100` | **VERIFIED** | International matches with dates, venues and scores (40 matches in 1905 verified; 2023 verified). Match detail endpoints give line-ups and officials for modern matches. |
| `ABSTATS` | NZ Rugby stats (stats.allblacks.com) | `https://stats.allblacks.com/` | **VERIFIED** | All Blacks and NZ rugby history (1905 page verified). |
| `RUSITES` | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby | `https://www.epcrugby.com` ; `https://www.premiershiprugby.com` ; `https://top14.lnr.fr` ; `https://www.unitedrugby.com` ; `https://www.sixnationsrugby.com` ; `https://super.rugby` ; `https://league-one.jp` ; `https://www.provincial.rugby` | **HOME ONLY** | Current fixtures, results, team lists and officials. |
| `RUGBYARCHIVE` | Rugby Archive | `http://www.rugbyarchive.net/` | **HOME ONLY** | Historical club and international rugby data (only the home page was tested). |
| `SCRUM` | ESPN scrum / Statsguru | `http://stats.espnscrum.com/statsguru/rugby/stats/index.html` | **UNREACHABLE** | Returned HTTP 202 with an empty body or a connection error: treat as retired. |
| `ITSRUGBY` | itsrugby | `https://www.itsrugby.fr/` | **BROWSER ONLY** | Cloudflare challenge here. |

### Cricket

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `CRICSHEET` | Cricsheet | `https://cricsheet.org/downloads/ (e.g. ipl_json.zip, bbl_json.zip, cch_json.zip)` | **VERIFIED** | Ball-by-ball JSON per match; Cricsheet's published format carries teams, playing XIs and officials (not opened in this pass). Match counts listed today: IPL 1,243; BBL 662; WBBL 519; PSL 357; CPL 442; SA20 130; ILT20 134; MLC 109; The Hundred 389; WPL 88; Tests 919; ODIs 3,187; T20Is 5,729; England One-Day Cup 886; County Championship 1,467. No Sheffield Shield, Ranji Trophy, Plunket Shield, Marsh Cup or Vijay Hazare downloads. |
| `HOWSTAT` | Howstat | `http://www.howstat.com/cricket/Statistics/Matches/MatchList.asp` | **VERIFIED** | Test and ODI match lists and scorecards with umpires (1900 Test list verified). |
| `CRICINFO` | ESPNcricinfo | `https://www.espncricinfo.com/` | **BROWSER ONLY** | Complete scorecards with umpires, referees and captains for all first-class history. Access Denied directly AND through r.jina.ai on 2026-09-30 (SOURCES.md says the proxy worked on 2026-09-28). |
| `CRICKETARCHIVE` | CricketArchive | `https://cricketarchive.com/` | **PAYWALL** | The most complete first-class and List A scorecard archive (county, Shield, Ranji, Plunket). Season pages return a paywall. |
| `CRICBOARDS` | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL | `https://www.icc-cricket.com` ; `https://www.ecb.co.uk` ; `https://www.cricket.com.au` ; `https://www.nzc.nz` ; `https://www.bcci.tv` ; `https://www.iplt20.com` | **HOME ONLY** | Current fixtures, scorecards and squads (home pages verified). |

### Tennis

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `SACKMANN` | Jeff Sackmann tennis_atp / tennis_wta (GitHub) | `https://github.com/JeffSackmann/tennis_atp` | **UNREACHABLE** | Repositories return 404 (also listed as 404 in SOURCES.md §4). |
| `TA` | Tennis Abstract | `https://www.tennisabstract.com/` | **VERIFIED** | Match results and player histories (Open era; some pre-Open). |
| `SLAMS` | Grand Slam sites | `https://www.wimbledon.com` ; `https://www.rolandgarros.com` ; `https://ausopen.com` ; `https://www.usopen.org` | **HOME ONLY** | Wimbledon and Roland-Garros pages opened (the Wimbledon draws-archive URL redirected to its history page); ausopen.com returned Akamai 'Access denied'; usopen.org is a JavaScript shell here. |
| `ATPWTA` | ATP / WTA sites | `https://www.atptour.com/en/scores/results-archive` ; `https://www.wtatennis.com/tournaments` | **VERIFIED** | Results archive (Open era) and tournament pages. |
| `TARCH` | Tennis Archives | `https://www.tennisarchives.com/` | **VERIFIED** | Pre-Open-era player and tournament history. |

### American, college and Canadian football

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `NFLVERSE` | nflverse data | `https://github.com/nflverse/nflverse-data/releases/download/<tag>/<file>` ; `https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv` | **VERIFIED** | games.csv 1999-2026 (scores, venue, roof, surface, referee and head-coach columns); rosters/roster_&lt;YYYY&gt;.csv from 1920; officials/officials.csv 2015-2026 (22,012 rows). games.csv also carries betting columns: never read them. |
| `GRIDSITES` | League sites: UFL, CFL, U SPORTS, IFAF | `https://www.theufl.com` ; `https://www.cfl.ca` ; `https://en.usports.ca/sports/fball` ; `https://americanfootball.sport` | **HOME ONLY** | Current schedules and results. |
| `CFLDB` | CFLdb | `https://cfldb.ca/` | **HOME ONLY** | CFL history database (schedules, rosters, rulebook). |
| `CFBD` | College Football Data API | `https://api.collegefootballdata.com/ (docs https://collegefootballdata.com/)` | **FREE KEY** | FBS/FCS games, rosters, coaches from 1869. Returns 401 without a free key. |
| `NCAA` | NCAA stats | `https://stats.ncaa.org/` | **BROWSER ONLY** | Akamai 'Access Denied' here. |

### Field hockey

| ID | Source | Route | Status | What it gives (as tested) |
|---|---|---|---|---|
| `FIH` | FIH | `https://www.fih.hockey/` | **HOME ONLY** | World Cups, Pro League, Olympic hockey (the results URL tried returned 404). |
| `EHL` | EuroHockey (EHL) | `https://www.eurohockey.org/` | **VERIFIED** | Euro Hockey League official site. |
| `KNHB` | KNHB (hockey.nl) | `https://www.hockey.nl/` | **VERIFIED** | Dutch Hoofdklasse official site. |
| `HOCKEYINDIA` | Hockey India | `https://www.hockeyindia.org/` | **VERIFIED** | Hockey India and Hockey India League information (hockeyindialeague.in did not resolve). |

## 4. Sources by competition

Each row lists sources in order of preference, by catalogue ID. **Limits** says what cannot be logged from these sources and why; the explanation document gives the era-by-era detail.

### AFL

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **AFL** | AFL Tables [AFLT]; Squiggle API [SQUIGGLE]; AFL API (aflapi.afl.com.au) [AFLAPI]; Footywire [FOOTYWIRE] | AFL Tables [AFLT]; AFL Stats Pro (api.afl.com.au) [AFLSTATS]; Footywire [FOOTYWIRE] | AFL Tables [AFLT]; Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE]; Internet Archive [IA] | Field umpires per game are not on AFL Tables or in the AFL API match lists: use Trove match reports (to 1954) and club/AFL annual reports; modern umpires appear on AFL match-centre pages (not tested as an archive). Leave the officials file blank where no primary record is found. |
| **AFL Grand Final** | AFL Tables [AFLT]; Squiggle API [SQUIGGLE] | AFL Tables [AFLT] | AFL Tables [AFLT] | Trove (National Library of Australia) [TROVE]; Internet Archive [IA] | Grand Final umpires are widely reported: use Trove and AFL Grand Final records. |
| **AFLW** | AFL API (aflapi.afl.com.au) [AFLAPI]; Footywire [FOOTYWIRE] | AFL Stats Pro (api.afl.com.au) [AFLSTATS]; AFL API (aflapi.afl.com.au) [AFLAPI] | Australian Football (australianfootball.com) [AUSFOOTY]; Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | AFL Tables coverage of AFLW was not found at the URL tried. Umpires: AFL match centre only. |

### American Football

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **IFAF World Championship** | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES]; Wikipedia (Action API / REST) [WIKI] | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES]; Internet Archive [IA] | Wikipedia (Action API / REST) [WIKI]; Internet Archive [IA] | Internet Archive [IA] | Five editions (1999-2015). Officials were rarely published: expect blanks. |
| **NFL** | nflverse data [NFLVERSE]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | nflverse data [NFLVERSE] | nflverse data [NFLVERSE]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | nflverse data [NFLVERSE]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF]; Chronicling America / Library of Congress [CHRONAM] | nflverse officials start in 2015; earlier crews are on Pro-Football-Reference box scores (browser only) and in newspaper archives. Head coaches are in games.csv from 1999. |
| **Super Bowl** | nflverse data [NFLVERSE]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | nflverse data [NFLVERSE] | nflverse data [NFLVERSE]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | nflverse data [NFLVERSE]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF]; Internet Archive [IA] | Super Bowl officiating crews are well documented; nflverse covers 2015 onward. |
| **UFL** | ESPN site API [ESPN]; League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES] | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES]; ESPN site API [ESPN] | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES] | ESPN site API [ESPN] | Officials only where ESPN game summaries list them. |

### Baseball

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **Australian Baseball League** | Australian Baseball League [ABL]; Wikipedia (Action API / REST) [WIKI] | Australian Baseball League [ABL] | Australian Baseball League [ABL]; Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | Original ABL (1989-99) records are thin online: use Trove and club histories. Umpires rarely recorded. |
| **CPBL** | CPBL [CPBL] | CPBL [CPBL] | CPBL [CPBL] | CPBL [CPBL] | Chinese-language pages; umpire fields in CPBL box scores were not checked. |
| **Caribbean Series and Winter Leagues** | WBSC [WBSC]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI]; Internet Archive [IA] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | No verified structured source for pre-1990 Caribbean Series box scores; Pura Pelota was unreachable. |
| **KBO** | KBO [KBO]; Statiz [STATIZ] | KBO [KBO]; Statiz [STATIZ] | KBO [KBO] | KBO [KBO] | Umpire fields in KBO box scores were not checked. |
| **MLB** | Retrosheet [RETRO]; MLB Stats API [MLBAPI] | Retrosheet [RETRO]; MLB Stats API [MLBAPI]; Lahman Baseball Database (SABR) [LAHMAN] | MLB Stats API [MLBAPI]; Retrosheet [RETRO]; Lahman Baseball Database (SABR) [LAHMAN] | Retrosheet [RETRO]; MLB Stats API [MLBAPI] | Retrosheet game logs have fields for the full umpire crew (the plate umpire was present in the 1901 file checked); the Stats API gave only the plate umpire for the 1950 game checked. |
| **Mexican League** | MLB Stats API [MLBAPI]; Liga Mexicana de Béisbol [LMB] | MLB Stats API [MLBAPI]; Liga Mexicana de Béisbol [LMB] | MLB Stats API [MLBAPI]; Liga Mexicana de Béisbol [LMB] | MLB Stats API [MLBAPI] | Stats API sportId 23 covers the MiLB-affiliated era (2019 verified); earlier seasons need LMB and newspaper sources. |
| **Minor Leagues** | MLB Stats API [MLBAPI]; Stats Crew [STATSCREW] | MLB Stats API [MLBAPI]; Stats Crew [STATSCREW] | MLB Stats API [MLBAPI] | MLB Stats API [MLBAPI] | Stats API sportIds 11-16 cover modern MiLB (Triple-A 2005 verified). Pre-2005 minor-league box scores and umpires are largely unavailable online: leave blank. |
| **NPB** | NPB.jp [NPB] | NPB.jp [NPB] | NPB.jp [NPB] | NPB.jp [NPB] | Pre-1950 JBL records are in Japanese on NPB.jp; umpires per game are not consistently published. |
| **Summer Olympics** | Olympedia [OLY]; WBSC [WBSC] | Olympedia [OLY] | Olympedia [OLY]; Wikipedia (Action API / REST) [WIKI] | WBSC [WBSC] | Umpire crews are rarely published. |
| **WBSC Premier12** | WBSC [WBSC] | WBSC [WBSC] | WBSC [WBSC] | WBSC [WBSC] | — |
| **World Baseball Classic** | MLB Stats API [MLBAPI] | MLB Stats API [MLBAPI] | MLB Stats API [MLBAPI] | MLB Stats API [MLBAPI] | Stats API sportId 51. |

### Basketball

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **ABA League** | ABA League [ABA]; FIBA LiveStats (Genius Sports) game JSON [GENIUS] | ABA League [ABA]; RealGM [REALGM] | ABA League [ABA]; RealGM [REALGM] | ABA League [ABA]; FIBA LiveStats (Genius Sports) game JSON [GENIUS] | — |
| **B League** | B.LEAGUE [BLG] | B.LEAGUE [BLG] | B.LEAGUE [BLG] | B.LEAGUE [BLG] | Japanese-language game pages. |
| **BSL** | TBF (Turkish BSL) [BSLTBF]; Eurobasket.com [EUROBASKET] | Eurobasket.com [EUROBASKET]; RealGM [REALGM] | RealGM [REALGM] | TBF (Turkish BSL) [BSLTBF] | TBF is browser-only from here; early seasons (1966-) are sparse online. |
| **Basketball Bundesliga** | easyCredit BBL [BBL]; Eurobasket.com [EUROBASKET] | Eurobasket.com [EUROBASKET]; RealGM [REALGM] | RealGM [REALGM] | easyCredit BBL [BBL] | Pre-2000 officials are not published online in a verified source. |
| **CBA** | CBA [CBA]; Eurobasket.com [EUROBASKET] | Eurobasket.com [EUROBASKET] | Eurobasket.com [EUROBASKET] | CBA [CBA] | Chinese-language JavaScript site; officials rarely available. |
| **EuroBasket** | Olympedia [OLY]; Wikipedia (Action API / REST) [WIKI]; FIBA LiveStats (Genius Sports) game JSON [GENIUS] | Wikipedia (Action API / REST) [WIKI]; Internet Archive [IA] | Wikipedia (Action API / REST) [WIKI] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | Officials available only for recent FIBA LiveStats editions. |
| **EuroCup** | EuroLeague / EuroCup data feeds [ELAPI] | EuroLeague / EuroCup data feeds [ELAPI]; RealGM [REALGM] | EuroLeague / EuroCup data feeds [ELAPI]; RealGM [REALGM] | EuroLeague / EuroCup data feeds [ELAPI] | — |
| **EuroLeague** | EuroLeague / EuroCup data feeds [ELAPI]; Wikipedia (Action API / REST) [WIKI] | EuroLeague / EuroCup data feeds [ELAPI]; RealGM [REALGM] | EuroLeague / EuroCup data feeds [ELAPI]; RealGM [REALGM] | EuroLeague / EuroCup data feeds [ELAPI] | Feeds start in 2000-01; 1957-58 to 1999-2000 need FIBA archives, newspapers or Wikipedia season pages (discovery only). Referees before 2000 are largely unavailable. |
| **EuroLeague Women** | FIBA LiveStats (Genius Sports) game JSON [GENIUS]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI]; Eurobasket.com [EUROBASKET] | Wikipedia (Action API / REST) [WIKI] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | Early editions (1958-) are documented only in summary. |
| **FIBA AmeriCup** | FIBA LiveStats (Genius Sports) game JSON [GENIUS]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | — |
| **FIBA Asia Cup** | FIBA LiveStats (Genius Sports) game JSON [GENIUS]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | — |
| **Greek Basket League** | ESAKE (Greek Basket League) [ESAKE]; Eurobasket.com [EUROBASKET] | ESAKE (Greek Basket League) [ESAKE]; Eurobasket.com [EUROBASKET] | ESAKE (Greek Basket League) [ESAKE] | ESAKE (Greek Basket League) [ESAKE] | Greek-language official site; pre-1990 game-level records are sparse. |
| **KBL** | KBL [KBL] | KBL [KBL] | KBL [KBL] | KBL [KBL] | Korean-language official site. |
| **LNB Elite** | LNB (Betclic Élite) [LNB]; Eurobasket.com [EUROBASKET] | LNB (Betclic Élite) [LNB]; Eurobasket.com [EUROBASKET] | LNB (Betclic Élite) [LNB] | LNB (Betclic Élite) [LNB]; Gallica (Bibliothèque nationale de France) [GALLICA] | Pre-1987 French championship detail requires Gallica newspapers. |
| **Liga ACB** | ACB (Liga Endesa) [ACB] | ACB (Liga Endesa) [ACB] | ACB (Liga Endesa) [ACB] | ACB (Liga Endesa) [ACB] | ACB box pages list starters and head coaches; referee fields on archived games were not checked. |
| **Men's FIBA World Cup** | FIBA LiveStats (Genius Sports) game JSON [GENIUS]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI]; Internet Archive [IA] | Wikipedia (Action API / REST) [WIKI] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | — |
| **NBA** | Basketball-Reference [BREF]; ESPN site API [ESPN] | Basketball-Reference [BREF] | Basketball-Reference [BREF] | Basketball-Reference [BREF]; NBA Official referee assignments [NBAOFF] | Referee registers on Basketball-Reference start in 1989-90; game crews before that are not in a verified source. Leave officials blank for 1946-1989 unless a primary record is found. |
| **NBA G League** | Basketball-Reference [BREF]; ESPN site API [ESPN] | Basketball-Reference [BREF] | Basketball-Reference [BREF] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | Officials rarely published. |
| **NBL** | NBL schedule API [NBLAPI]; Wikipedia (Action API / REST) [WIKI] | NBL schedule API [NBLAPI]; Eurobasket.com [EUROBASKET] | Wikipedia (Action API / REST) [WIKI] | Trove (National Library of Australia) [TROVE] | Pre-2000 NBL game data is thin online: use Trove and club histories for coaches and referees. |
| **NBL1** | NBL1 [NBL1]; FIBA LiveStats (Genius Sports) game JSON [GENIUS] | NBL1 [NBL1]; FIBA LiveStats (Genius Sports) game JSON [GENIUS] | NBL1 [NBL1] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | — |
| **PBA** | PBA [PBA] | PBA [PBA] | PBA [PBA] | PBA [PBA] | — |
| **Serie A** | Lega Basket Serie A [LBA]; Eurobasket.com [EUROBASKET] | Lega Basket Serie A [LBA]; Eurobasket.com [EUROBASKET] | Lega Basket Serie A [LBA] | Lega Basket Serie A [LBA] | Pre-1980 detail requires Italian newspaper archives (not tested). |
| **Summer Olympics** | Olympedia [OLY] | Olympedia [OLY] | Olympedia [OLY]; Wikipedia (Action API / REST) [WIKI] | Olympedia [OLY] | Officials: not in a verified source; check Olympedia result pages and FIBA LiveStats (recent Games) edition by edition. |
| **VTB United League** | VTB United League [VTB]; Eurobasket.com [EUROBASKET] | VTB United League [VTB]; Eurobasket.com [EUROBASKET] | VTB United League [VTB] | VTB United League [VTB] | — |
| **WNBA** | Basketball-Reference [BREF]; ESPN site API [ESPN] | Basketball-Reference [BREF] | Basketball-Reference [BREF] | Basketball-Reference [BREF] | WNBA referee registers were not checked. |
| **WNBL** | WNBL [WNBL]; FIBA LiveStats (Genius Sports) game JSON [GENIUS] | WNBL [WNBL]; Eurobasket.com [EUROBASKET] | WNBL [WNBL] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | The WNBL site is browser-only from here; early seasons (1981-) need Trove. |
| **Women's FIBA World Cup** | FIBA LiveStats (Genius Sports) game JSON [GENIUS]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | FIBA LiveStats (Genius Sports) game JSON [GENIUS] | — |

### Canadian Football

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **CFL** | CFLdb [CFLDB]; ESPN site API [ESPN]; League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES] | CFLdb [CFLDB]; Stats Crew [STATSCREW] | CFLdb [CFLDB] | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES] | No verified officials source: cfl.ca game pages were not tested for crews. |
| **Grey Cup** | CFLdb [CFLDB]; Wikipedia (Action API / REST) [WIKI] | CFLdb [CFLDB] | CFLdb [CFLDB] | Internet Archive [IA] | Pre-1958 Grey Cups involved union and university teams: use newspaper archives. |
| **Vanier Cup** | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES]; Wikipedia (Action API / REST) [WIKI] | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES] | League sites: UFL, CFL, U SPORTS, IFAF [GRIDSITES] | Internet Archive [IA] | U SPORTS game officials are not published in an archive. |

### College Football

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **College Football Playoff** | ESPN site API [ESPN]; College Football Data API [CFBD] | College Football Data API [CFBD]; ESPN site API [ESPN] | College Football Data API [CFBD] | ESPN site API [ESPN] | — |
| **Cotton Bowl** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | No verified structured source for bowl officials: use newspapers or official game books where found. |
| **Fiesta Bowl** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | — |
| **NCAA Division I FBS** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | Game officials are not in any verified structured source: leave blank unless a game book or newspaper names them. |
| **NCAA Division I FCS** | College Football Data API [CFBD]; ESPN site API [ESPN] | College Football Data API [CFBD] | College Football Data API [CFBD] | Chronicling America / Library of Congress [CHRONAM] | — |
| **Orange Bowl** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | — |
| **Peach Bowl** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | — |
| **Rose Bowl** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | — |
| **Sugar Bowl** | College Football Data API [CFBD]; ESPN site API [ESPN]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | College Football Data API [CFBD] | College Football Data API [CFBD]; Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead [SPORTSREF] | Chronicling America / Library of Congress [CHRONAM] | — |

### Cricket One-Day Format

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **Marsh One-Day Cup** | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS]; ESPNcricinfo [CRICINFO] | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | No Cricsheet download; ESPNcricinfo is browser-only and CricketArchive is paywalled. |
| **Men's Champions Trophy** | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Cricsheet [CRICSHEET] | ESPNcricinfo [CRICINFO]; Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Coaches are not in scorecards: use team announcements and Wikipedia squad pages (discovery). |
| **Men's Cricket World Cup** | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Wikipedia (Action API / REST) [WIKI]; ESPNcricinfo [CRICINFO] | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Cricsheet ball-by-ball data does not cover the early World Cups; use Howstat scorecards. |
| **Metro Bank One Day Cup** | Cricsheet [CRICSHEET]; Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | Cricsheet [CRICSHEET] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | Cricsheet [CRICSHEET] | Cricsheet 'One-Day Cup' (rlc) covers the recent era only; Gillette/NatWest-era scorecards need CricketArchive or ESPNcricinfo. |
| **Vijay Hazare Trophy** | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS]; ESPNcricinfo [CRICINFO] | ESPNcricinfo [CRICINFO] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | ESPNcricinfo [CRICINFO] | No Cricsheet download found; BCCI site is current-season only. |
| **Women's Cricket World Cup** | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |

### Cricket T20

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **Big Bash** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS]; Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **CPL** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **ILT20** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **IPL** | Cricsheet [CRICSHEET]; ESPN site API [ESPN] | Cricsheet [CRICSHEET] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS]; Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **MLC** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **Men's T20 World Cup** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **PSL** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **SA20** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **The Hundred** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS]; Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **WBBL** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS]; Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **WPL** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |
| **Women's T20 World Cup** | Cricsheet [CRICSHEET] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET] | — |

### Cricket Tests

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **County Championship** | Cricsheet [CRICSHEET]; CricketArchive [CRICKETARCHIVE] | Cricsheet [CRICSHEET]; CricketArchive [CRICKETARCHIVE] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | Cricsheet [CRICSHEET]; CricketArchive [CRICKETARCHIVE] | Cricsheet covers only the recent County Championship seasons (1,467 matches); earlier scorecards need CricketArchive (paywall) or ESPNcricinfo (browser only). County coaches are a modern role (captains ran sides historically): leave the coach field blank for early seasons and log the captain in the notes. |
| **ICC World Test Championship** | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Cricsheet [CRICSHEET]; Howstat [HOWSTAT] | — |
| **Plunket Shield** | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | Papers Past (National Library of New Zealand) [PAPERSPAST] | No Cricsheet download. Historical umpires via Papers Past (browser only). |
| **Ranji Trophy** | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | ESPNcricinfo [CRICINFO] | No Cricsheet download. |
| **Sheffield Shield** | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | ESPNcricinfo [CRICINFO]; CricketArchive [CRICKETARCHIVE] | Boards and leagues: ICC, ECB, Cricket Australia, NZC, BCCI, IPL [CRICBOARDS] | Trove (National Library of Australia) [TROVE] | No Cricsheet download. Historical umpires via Trove. |
| **The Ashes** | Howstat [HOWSTAT]; Cricsheet [CRICSHEET] | Howstat [HOWSTAT]; Cricsheet [CRICSHEET] | Wikipedia (Action API / REST) [WIKI] | Howstat [HOWSTAT]; Cricsheet [CRICSHEET] | Howstat lists every Test by year (1900 verified); check its scorecards for umpires. Team coaches are a modern role (tour managers historically): leave blank and explain. |

### Hockey

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **Euro Hockey League** | EuroHockey (EHL) [EHL] | EuroHockey (EHL) [EHL] | EuroHockey (EHL) [EHL] | EuroHockey (EHL) [EHL] | — |
| **FIH Hockey Pro League** | FIH [FIH] | FIH [FIH] | FIH [FIH] | FIH [FIH] | — |
| **Hockey India League** | Hockey India [HOCKEYINDIA]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | Hockey India [HOCKEYINDIA] | hockeyindialeague.in did not resolve from here. |
| **Hoofdklasse** | KNHB (hockey.nl) [KNHB]; Delpher (Dutch newspapers) [DELPHER] | KNHB (hockey.nl) [KNHB]; Delpher (Dutch newspapers) [DELPHER] | KNHB (hockey.nl) [KNHB] | Delpher (Dutch newspapers) [DELPHER] | Dutch-language sources; historical umpires only via newspapers. |
| **Men's FIH Hockey World Cup** | FIH [FIH]; Wikipedia (Action API / REST) [WIKI] | FIH [FIH]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | FIH [FIH] | — |
| **Summer Olympics** | Olympedia [OLY] | Olympedia [OLY] | Olympedia [OLY]; Wikipedia (Action API / REST) [WIKI] | Olympedia [OLY] | — |
| **Women's FIH Hockey World Cup** | FIH [FIH]; Wikipedia (Action API / REST) [WIKI] | FIH [FIH]; Wikipedia (Action API / REST) [WIKI] | Wikipedia (Action API / REST) [WIKI] | FIH [FIH] | — |

### Ice Hockey

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **AHL** | HockeyDB [HDB]; League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | Elite Prospects [EP]; HockeyDB [HDB] | Elite Prospects [EP]; HockeyDB [HDB] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | Historical officials are not published in a verified source. |
| **AIHL** | AIHL [AIHL]; Wikipedia (Action API / REST) [WIKI] | AIHL [AIHL] | AIHL [AIHL] | AIHL [AIHL] | Official site browser-only; Elite Prospects AIHL pages showed no rosters. |
| **Czech Extraliga** | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES]; Elite Prospects [EP] | Elite Prospects [EP] | Elite Prospects [EP] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | Referee fields on hokej.cz match pages were not tested. |
| **DEL** | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES]; Elite Prospects [EP] | Elite Prospects [EP] | Elite Prospects [EP] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | — |
| **ECHL** | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES]; HockeyDB [HDB] | Elite Prospects [EP]; HockeyDB [HDB] | Elite Prospects [EP]; HockeyDB [HDB] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | — |
| **KHL** | KHL [KHL]; Elite Prospects [EP] | Elite Prospects [EP] | Elite Prospects [EP] | KHL [KHL] | en.khl.ru is browser-only from here. |
| **Liiga** | Liiga API [LIIGAAPI] | Liiga API [LIIGAAPI]; Elite Prospects [EP] | Elite Prospects [EP] | Liiga API [LIIGAAPI] | Liiga API game detail lists referees and linesmen. |
| **Men's IIHF World Championship** | IIHF [IIHF]; Hockey Archives [HARCH] | IIHF [IIHF]; Hockey Archives [HARCH]; Elite Prospects [EP] | Hockey Archives [HARCH]; Wikipedia (Action API / REST) [WIKI] | IIHF [IIHF] | Pre-1990 officials are not published in a verified source. |
| **NHL** | Hockey-Reference [HREF]; NHL api-web [NHLAPI]; ESPN site API [ESPN] | NHL api-web [NHLAPI]; Hockey-Reference [HREF] | Hockey-Reference [HREF]; NHL api-web [NHLAPI] | NHL api-web [NHLAPI]; Hockey Hall of Fame [HHOF] | Officials per game are in the NHL right-rail for the modern era only; Hockey-Reference box scores carry none. Historical crews: leave blank unless a game sheet or newspaper names them. |
| **PWHL** | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | — |
| **SHL** | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES]; Elite Prospects [EP] | Elite Prospects [EP] | Elite Prospects [EP] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | — |
| **Swiss National League** | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES]; Elite Prospects [EP] | Elite Prospects [EP] | Elite Prospects [EP] | League sites: SHL, DEL, hokej.cz, National League, PWHL, AHL, ECHL [HOCKEYLEAGUES] | — |
| **Winter Olympics** | Olympedia [OLY]; IIHF [IIHF] | Olympedia [OLY] | Olympedia [OLY]; Wikipedia (Action API / REST) [WIKI] | IIHF [IIHF] | — |
| **Women's IIHF World Championship** | IIHF [IIHF]; Wikipedia (Action API / REST) [WIKI] | IIHF [IIHF]; Elite Prospects [EP] | Wikipedia (Action API / REST) [WIKI] | IIHF [IIHF] | — |

### Rugby League

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **Men's Rugby League World Cup** | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | — |
| **NRL** | Rugby League Project [RLP]; NRL draw API [NRLAPI]; ESPN site API [ESPN] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | RLP results pages carry a referee field (verified on NRL 2024; the word appears on the 1908 page): check completeness season by season. |
| **NRLW** | Rugby League Project [RLP]; NRL draw API [NRLAPI] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | — |
| **RFL Championship** | Rugby League Project [RLP]; Super League / RFL / League Unlimited [RLSITES] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP]; British Newspaper Archive [BNA] | Decide the folder's lineage first (see the explanation document). |
| **State of Origin** | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | — |
| **Super League** | Rugby League Project [RLP]; Super League / RFL / League Unlimited [RLSITES] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | — |
| **Women's Rugby League World Cup** | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | Rugby League Project [RLP] | — |
| **Women's Super League** | Super League / RFL / League Unlimited [RLSITES]; Rugby League Project [RLP] | Super League / RFL / League Unlimited [RLSITES] | Super League / RFL / League Unlimited [RLSITES] | Super League / RFL / League Unlimited [RLSITES] | Coverage of this competition in RLP was not checked. |

### Rugby Union

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **Champions Cup** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; ESPN site API [ESPN] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | — |
| **EPCR Challenge Cup** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; ESPN site API [ESPN] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | — |
| **Farah Palmer Cup** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; NZ Rugby stats (stats.allblacks.com) [ABSTATS] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Papers Past (National Library of New Zealand) [PAPERSPAST] | The Provincial Rugby /fpc/ path returned 404; early women's NPC detail is sparse. |
| **League One** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Japanese-language pages; Top League-era archive not tested. |
| **Men's Rugby World Cup** | World Rugby match API (pulselive) [WRAPI]; ESPN site API [ESPN] | World Rugby match API (pulselive) [WRAPI] | Wikipedia (Action API / REST) [WIKI] | World Rugby match API (pulselive) [WRAPI] | — |
| **Premiership** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; ESPN site API [ESPN] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Pre-2000 officials and team sheets need newspaper archives. |
| **Premiership Women's Rugby** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | — |
| **Six Nations** | World Rugby match API (pulselive) [WRAPI]; Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | World Rugby match API (pulselive) [WRAPI]; NZ Rugby stats (stats.allblacks.com) [ABSTATS] | Wikipedia (Action API / REST) [WIKI] | World Rugby match API (pulselive) [WRAPI]; British Newspaper Archive [BNA] | Coaches did not exist as a team role for most of the amateur era (captains led sides): leave the coach field blank and explain. |
| **Super Rugby Pacific** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; ESPN site API [ESPN] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | — |
| **The Rugby Championship** | World Rugby match API (pulselive) [WRAPI]; NZ Rugby stats (stats.allblacks.com) [ABSTATS] | World Rugby match API (pulselive) [WRAPI]; NZ Rugby stats (stats.allblacks.com) [ABSTATS] | Wikipedia (Action API / REST) [WIKI] | World Rugby match API (pulselive) [WRAPI] | — |
| **Top 14** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; Gallica (Bibliothèque nationale de France) [GALLICA] | itsrugby (historical) is browser-only; pre-1990 detail requires Gallica. |
| **United Rugby Championship** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; ESPN site API [ESPN] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | — |
| **Women's Rugby World Cup** | World Rugby match API (pulselive) [WRAPI] | World Rugby match API (pulselive) [WRAPI] | Wikipedia (Action API / REST) [WIKI] | World Rugby match API (pulselive) [WRAPI] | — |
| **Women's Six Nations** | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES]; World Rugby match API (pulselive) [WRAPI] | Competition sites: EPCR, PREM Rugby, LNR Top 14, URC, Six Nations, Super Rugby, League One, Provincial Rugby [RUSITES] | Wikipedia (Action API / REST) [WIKI] | World Rugby match API (pulselive) [WRAPI] | — |

### Soccer

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **A-League Men** | Ultimate A-League [UAL]; worldfootball.net [WF]; ESPN site API [ESPN] | Ultimate A-League [UAL]; Transfermarkt [TM] | Ultimate A-League [UAL]; Transfermarkt [TM] | Ultimate A-League [UAL]; worldfootball.net [WF] | — |
| **A-League Women** | Ultimate A-League [UAL]; worldfootball.net [WF] | Ultimate A-League [UAL] | Ultimate A-League [UAL] | Ultimate A-League [UAL] | — |
| **AFC Champions League** | worldfootball.net [WF]; RSSSF [RSSSF] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF] | — |
| **Bundesliga** | worldfootball.net [WF]; DFB Datencenter [DFB]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; DFB Datencenter [DFB]; Transfermarkt [TM] | — |
| **CAF Champions League** | worldfootball.net [WF]; RSSSF [RSSSF] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF] | Early editions (1964-1990) have sparse line-ups and referees. |
| **CONCACAF Champions Cup** | worldfootball.net [WF]; RSSSF [RSSSF] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF] | — |
| **CONCACAF Gold Cup** | worldfootball.net [WF]; RSSSF [RSSSF] | National-Football-Teams.com [NFT]; worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | — |
| **CONMEBOL Libertadores** | worldfootball.net [WF]; RSSSF [RSSSF]; CONMEBOL [CONMEBOL] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF] | — |
| **Copa America** | worldfootball.net [WF]; RSSSF [RSSSF] | National-Football-Teams.com [NFT]; worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF]; RSSSF [RSSSF] | — |
| **FIFA Club World Cup** | FIFA API [FIFAAPI]; worldfootball.net [WF] | FIFA API [FIFAAPI]; worldfootball.net [WF] | worldfootball.net [WF] | FIFA API [FIFAAPI]; worldfootball.net [WF] | — |
| **Frauen-Bundesliga** | DFB Datencenter [DFB]; worldfootball.net [WF] | DFB Datencenter [DFB]; worldfootball.net [WF] | worldfootball.net [WF] | DFB Datencenter [DFB] | The worldfootball slug guessed for 1990-91 returned 404; navigate from the competition page. |
| **La Liga** | worldfootball.net [WF]; Transfermarkt [TM]; RSSSF [RSSSF] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM]; FBref / BDFutbol / kicker [FBREF] | worldfootball.net [WF]; Transfermarkt [TM]; FBref / BDFutbol / kicker [FBREF] | BDFutbol (browser only) is the most complete La Liga coach/referee history. |
| **Liga F** | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF] | worldfootball.net [WF] | Early Superliga Femenina seasons are sparse. |
| **Ligue 1** | worldfootball.net [WF]; Transfermarkt [TM]; RSSSF [RSSSF] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Gallica (Bibliothèque nationale de France) [GALLICA] | — |
| **Major League Soccer** | MLSsoccer.com [MLS]; worldfootball.net [WF]; ESPN site API [ESPN] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; MLSsoccer.com [MLS] | — |
| **Men's AFC Asian Cup** | worldfootball.net [WF]; RSSSF [RSSSF] | National-Football-Teams.com [NFT]; worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF]; RSSSF [RSSSF] | — |
| **Men's Africa Cup of Nations** | worldfootball.net [WF]; RSSSF [RSSSF] | National-Football-Teams.com [NFT]; worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF]; RSSSF [RSSSF] | — |
| **Men's FIFA World Cup** | FIFA API [FIFAAPI]; worldfootball.net [WF]; openfootball (GitHub) [OPENFB] | FIFA API [FIFAAPI]; National-Football-Teams.com [NFT]; worldfootball.net [WF] | worldfootball.net [WF] | FIFA API [FIFAAPI]; worldfootball.net [WF] | — |
| **Men's UEFA European Championship** | worldfootball.net [WF]; RSSSF [RSSSF] | National-Football-Teams.com [NFT]; worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | — |
| **NWSL** | NWSL official [NWSL]; worldfootball.net [WF]; ESPN site API [ESPN] | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF]; NWSL official [NWSL] | — |
| **Premier League** | Premier League pulselive API [PLAPI]; worldfootball.net [WF]; openfootball (GitHub) [OPENFB] | Premier League pulselive API [PLAPI]; worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | Premier League pulselive API [PLAPI]; worldfootball.net [WF]; Transfermarkt [TM] | — |
| **Premiere Ligue** | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | Early seasons are sparse. |
| **Serie A** | worldfootball.net [WF]; Transfermarkt [TM]; RSSSF [RSSSF] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | — |
| **Serie A Femminile** | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | Early seasons are sparse. |
| **Summer Olympics** | Olympedia [OLY]; worldfootball.net [WF]; RSSSF [RSSSF] | Olympedia [OLY] | worldfootball.net [WF] | worldfootball.net [WF]; RSSSF [RSSSF] | — |
| **UEFA Champions League** | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | The UEFA match API route in SOURCES.md is the field owner for modern matches. |
| **UEFA Conference League** | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | — |
| **UEFA Europa League** | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | — |
| **WSL** | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF]; Transfermarkt [TM] | worldfootball.net [WF] | — |
| **Women's FIFA World Cup** | FIFA API [FIFAAPI]; worldfootball.net [WF] | FIFA API [FIFAAPI]; worldfootball.net [WF] | worldfootball.net [WF] | FIFA API [FIFAAPI]; worldfootball.net [WF] | — |
| **Women's UEFA European Championship** | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | worldfootball.net [WF] | — |

### State Level AFL

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **NTFL** | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE] | Pre-2000 NTFL game detail requires Trove; umpires rarely recorded. |
| **QAFL** | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES]; Wikipedia (Action API / REST) [WIKI] | Australian Football (australianfootball.com) [AUSFOOTY] | Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE] | Game-level historical records require Trove. |
| **SANFL** | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES]; AFL API (aflapi.afl.com.au) [AFLAPI] | AFL Stats Pro (api.afl.com.au) [AFLSTATS]; Australian Football (australianfootball.com) [AUSFOOTY] | Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE] | AFL API SANFL seasons cover the modern era only; historical team lists and umpires via Trove. |
| **SANFLW** | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES]; AFL API (aflapi.afl.com.au) [AFLAPI] | AFL Stats Pro (api.afl.com.au) [AFLSTATS] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | — |
| **TSL** | Wikipedia (Action API / REST) [WIKI] | Australian Football (australianfootball.com) [AUSFOOTY] | Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE] | No official TSL site resolved from here (two guessed domains failed). Decide the folder's lineage first. |
| **VFL** | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES]; AFL API (aflapi.afl.com.au) [AFLAPI] | AFL Stats Pro (api.afl.com.au) [AFLSTATS]; Australian Football (australianfootball.com) [AUSFOOTY] | Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE] | VFA-era detail requires Trove. |
| **VFLW** | AFL API (aflapi.afl.com.au) [AFLAPI] | AFL Stats Pro (api.afl.com.au) [AFLSTATS] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | — |
| **WAFL** | WAFL FootyFacts [WAFLFF]; AFL API (aflapi.afl.com.au) [AFLAPI] | WAFL FootyFacts [WAFLFF]; Sportix statistics API (WAFL) [SPORTIX] | WAFL FootyFacts [WAFLFF]; Australian Football (australianfootball.com) [AUSFOOTY] | Trove (National Library of Australia) [TROVE] | WAFL FootyFacts carries team lists across the league's history; umpires need Trove. |
| **WAFLW** | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES]; AFL API (aflapi.afl.com.au) [AFLAPI] | AFL Stats Pro (api.afl.com.au) [AFLSTATS] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | State league sites: SANFL, WAFL, VFL, NTFL, AFL Queensland [STATELEAGUES] | — |

### Tennis

| Competition | Games (CSV) | Players and teams by year | Coaching staff | Officials | Limits |
|---|---|---|---|---|---|
| **ATP/London** | Grand Slam sites [SLAMS]; Tennis Archives [TARCH]; Tennis Abstract [TA] | Grand Slam sites [SLAMS]; Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | Tennis players' coaches were not recorded for most of history and chair umpires only for recent finals: leave COACHES/OFFICIATING blank and say so. |
| **ATP/Melbourne** | Tennis Archives [TARCH]; Tennis Abstract [TA]; ATP / WTA sites [ATPWTA] | Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | ausopen.com is browser-only (Akamai) from here. |
| **ATP/New York** | Tennis Archives [TARCH]; Tennis Abstract [TA]; ATP / WTA sites [ATPWTA] | Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | usopen.org is a JavaScript shell here. |
| **ATP/Paris** | Grand Slam sites [SLAMS]; Tennis Archives [TARCH]; Tennis Abstract [TA] | Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | — |
| **WTA/London** | Grand Slam sites [SLAMS]; Tennis Archives [TARCH]; Tennis Abstract [TA] | Grand Slam sites [SLAMS]; Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | — |
| **WTA/Melbourne** | Tennis Archives [TARCH]; Tennis Abstract [TA]; ATP / WTA sites [ATPWTA] | Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | — |
| **WTA/New York** | Tennis Archives [TARCH]; Tennis Abstract [TA]; ATP / WTA sites [ATPWTA] | Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | — |
| **WTA/Paris** | Grand Slam sites [SLAMS]; Tennis Archives [TARCH]; Tennis Abstract [TA] | Tennis Archives [TARCH] | Wikipedia (Action API / REST) [WIKI] | Internet Archive [IA] | — |

## 5. Sources that failed on 2026-09-30

| Source | Result | Consequence |
|---|---|---|
| Trove (National Library of Australia) | FREE KEY | Australian newspapers: team lists, umpires, coaches and scores for AFL/VFL, state leagues, NRL, cricket, NBL. Web search shows a bot check here; the v3 API returns 401 without a free key. |
| Papers Past (National Library of New Zealand) | BROWSER ONLY | NZ newspapers: Plunket Shield, NZ rugby and provincial rugby line-ups and referees. |
| Chronicling America / Library of Congress | BROWSER ONLY | US newspapers to 1963: box scores, umpires, college football line-ups and officials. |
| Gallica (Bibliothèque nationale de France) | BROWSER ONLY | French newspapers (L'Auto, L'Équipe predecessors): Top 14, French football, LNB and Roland-Garros history. Returned a security-check page here. |
| British Newspaper Archive | PAYWALL | UK newspapers: county cricket, rugby league/union, football line-ups and officials. Subscription; security check here. |
| Sports Reference: Baseball-, Pro-Football-, College-Football-Reference; Stathead | BROWSER ONLY | Complete seasons, rosters, coaches and (PFR) game officials. Cloudflare 403 here, also through the r.jina.ai proxy. Open manually in a browser; never scrape. |
| FBref / BDFutbol / kicker | BROWSER ONLY | Cloudflare 403 here. BDFutbol is the best La Liga history source (coaches, referees) if opened manually. |
| TBF (Turkish BSL) | BROWSER ONLY | Cloudflare challenge here. |
| WNBL | BROWSER ONLY | TLS handshake failure direct; Cloudflare through the proxy. |
| Proballers | BROWSER ONLY | Cloudflare 403 on 2026-09-30 (SOURCES.md listed it as 200 on 2026-09-28). |
| Pura Pelota (LVBP history) | UNREACHABLE | TLS certificate failure here. |
| AIHL | BROWSER ONLY | JavaScript redirect; Cloudflare through the proxy. |
| Full Points Footy (fullpointsfooty.net) | EXCLUDED | The domain now serves a betting-prediction spam site. Older Wikipedia citations point to it; use archived copies on web.archive.org only. |
| ESPN scrum / Statsguru | UNREACHABLE | Returned HTTP 202 with an empty body or a connection error: treat as retired. |
| itsrugby | BROWSER ONLY | Cloudflare challenge here. |
| ESPNcricinfo | BROWSER ONLY | Complete scorecards with umpires, referees and captains for all first-class history. Access Denied directly AND through r.jina.ai on 2026-09-30 (SOURCES.md says the proxy worked on 2026-09-28). |
| CricketArchive | PAYWALL | The most complete first-class and List A scorecard archive (county, Shield, Ranji, Plunket). Season pages return a paywall. |
| Jeff Sackmann tennis_atp / tennis_wta (GitHub) | UNREACHABLE | Repositories return 404 (also listed as 404 in SOURCES.md §4). |
| College Football Data API | FREE KEY | FBS/FCS games, rosters, coaches from 1869. Returns 401 without a free key. |
| NCAA stats | BROWSER ONLY | Akamai 'Access Denied' here. |

Also tested and not usable from here: todor66.com (connection timeout), American Soccer Analysis API (timeout), ozfootball.net (TLS error), UEFA history pages (connection reset), `stats.nba.com` (connection reset), `data.nba.net` (certificate mismatch), Soccerway (reachable, but its pages carry betting widgets: scores only, and prefer another source), Chadwick Bureau `baseballdatabank` GitHub (404), hockeyindialeague.in (DNS failure), NHL Records officials endpoint (403), Baseball-Reference/Pro-Football-Reference/College Football Reference through the r.jina.ai proxy (403).

## 6. Suggested order of work

1. Fix the folder statuses listed in the explanation document §5 (they decide which years get populated).
2. Populate the competitions with complete structured sources first: MLB (Retrosheet), VFL/AFL (AFL Tables), NRL and rugby league (RLP), NBA/WNBA (Basketball-Reference), NHL (Hockey-Reference + NHL API), soccer leagues and FIFA/UEFA/CONMEBOL tournaments (worldfootball.net + Transfermarkt), franchise T20 cricket (Cricsheet), NFL (nflverse).
3. Then the competitions whose history is only in official sites and databases (European basketball, European ice hockey via Elite Prospects).
4. Last, the pre-1950 detail that only newspapers hold (umpires, early team lists): Trove (free API key), Papers Past, Chronicling America, Gallica, Delpher, all read manually.


# Sources — the single source register

**Rebuilt 2026-09-28 for md-only operation; expanded 2026-09-28(f).** This page merges the old quick reference and full register, and adds the sources verified on 2026-09-28. It is the only source document the model reads.
- **What changed on 2026-09-28:** 60+ routes were re-tested by live request; the sport tables below list each with its access mode and result. About 30 are new to the register, including the standings feeds for the hand-computed team baseline, injury feeds, official ladders, rating systems and weather services.
- **Repo files versus web sources:** the model uses no Python and no non-Markdown *file from this repository*. Web sources may be JSON, HTML or PDF: the model opens them with its browser or fetch tool and quotes the fields it used.

---

## 1. Rules every source follows

### 1.1 Three independent lineages

- **To issue a card:** three distinct, reliable upstream lineages for the event's identity, time and state.
- **To settle one:** three lineages that agree on the exact event, an explicit final marker and the score.
- **What counts once:** mirrors, syndicated copies, reposts, two front ends on one feed, and a transcript of a broadcast all count as **one** lineage.
- **What never counts:** search-result snippets and generated summaries are discovery only.
- **When three are not available:** print `SOURCE_COUNT_LT_3` or `SOURCE_LINEAGE_NOT_INDEPENDENT` and fail closed. Never pretend.
- **Preferred mix:** the field owner's exact-event record, then an official club or player source (or a second primary), then an independent high-quality secondary.

### 1.2 Who owns which field

| Claim | Controlling source | It does not control |
|---|---|---|
| Identity, schedule, rules, participants, state, result | Governing body, league or official match centre; official team release | Forecast importance; proprietary metrics |
| Lineup, starter, goalie, toss, team sheet | **The official release** (MLB `battingOrder`, NPB/KBO official orders, NBA/WNBA/NBL official starters, NHL confirmed goalie, club XI, team lists) | — |
| Injury or availability | Official league injury report; team release | — |
| Weather | National meteorological service or venue-coordinate forecast; the venue's roof or surface report | The sport effect, which is the card's own mechanism |
| Historical statistic | The official provider; a reconciled official record | Another provider's definition |
| Derived metric (xG, Elo, pace) | The provider that defines it | Official facts |
| Late news before the official release | A named accredited reporter, with a receipt (§1.5) | Anything after the official release |

- **Resolve conflicts field by field**, not by majority vote. Two weak sources do not equal one controlling source.
- **A field owner can be wrong for one field.** A schedule shell, a 0–0 placeholder, an all-zero statistics block or a page still showing `UPCOMING` after independent sources show a final: mark that field `STALE`. Keep the valid fields, and use another official or static route plus independent corroboration.

### 1.3 Freshness

| Class | Examples | Rule |
|---|---|---|
| V0 live | Score, clock, inning, over | Observe and timestamp; refresh just before issue |
| V1 release-driven | Lineups, starters, toss, goalie, inactives | Refresh after the official release **and** immediately before issue |
| V2 short horizon | Injuries, role, roof, pitch, weather | The newest source before issue; branch the unresolved states |
| V3 current process | Season rates, recent form, specialist metrics | Through the last completed game; record the provider's lag |
| V4 structural | Rules, venue, definitions | Re-check at a new season or competition |

**Every decisive fact** carries its source, retrieval time and a status: `OPENED` (you read the record), `SNIPPET` (search text only; never decisive) or `ASSUMED` (never allowed at Rank 1).

### 1.4 The firewall — prohibited as forecasting evidence

Never forecasting evidence:
- sportsbooks, odds, line movement and odds aggregators;
- betting previews, picks, tips and touts;
- prediction markets;
- fantasy/DFS projections, rankings and ownership;
- anything that republishes those. This includes **RotoWire, RotoGrinders and FPTrack**.

Further rules:
- **Mixed pages.** A page that mixes scores with odds columns may be used **for scores only**, and the odds are never read. This applies to TennisExplorer, Flashscore and football-data.co.uk (whose results files carry bookmaker columns).
- **Market keys in ESPN and NHL feeds are quarantined:** `odds`, `pickcenter`, `againstTheSpread`, `winprobability`, `oddsPartners`, `betting`.
- **A supplied line is contract metadata,** not evidence.
- **Squiggle's `tips` endpoint aggregates other models' tips.** It is discovery only, and never an anchor. Its `games` and `standings` endpoints are ordinary results data.

**Synthetic content is prohibited everywhere (L-079, M20).** This means AI-written recaps, "AI simulation" or "projected result" articles, formulaic pitch-report or fantasy pages, and search summaries. Confirmed cases: sportscafe.in (a wrong winner), archysport, and the Mynavi AI recaps.
- Always open the underlying scoreboard or scorecard before a figure enters a card or a settlement.
- A narrative article never settles a result.

### 1.5 Lineups and late news (S-1 Rev 2)

1. **An official lineup published before the freeze always wins.** Print it with its fetch time as `CONFIRMED_OFFICIAL`.
2. Before the official release, a lineup claim counts only as `PROJECTED_BEAT_VERIFIED`, with a printed receipt: outlet, reporter, timestamp, verbatim quote, and two independent sources.
3. Otherwise print `LINEUPS_NOT_YET_PUBLISHED` (nothing is out yet) or `RETRIEVAL_MISS` (it was out, but you did not get it). A Rank-1 total or margin row may not depend on an unretrieved lineup (G14.2).
4. An original, complete, pre-issue lineup post from an authenticated league, competition or club account can be that organisation's release under §1.8. A player, journalist, fan, aggregator or copied post cannot confirm a whole lineup. The official match centre or posted team sheet remains the first route; the post and that organisation's site are one lineage.

### 1.6 Access modes (how to open each source)

| Mode | Meaning | Examples |
|---|---|---|
| **API** | A keyless JSON endpoint. Open it directly. ESPN routes **reject a browser user-agent** (HTTP 403) and accept a plain request | ESPN site API; MLB statsapi; NRL `draw/data` |
| **Browser** | Needs a normal browser request (it rejects a bare client) | NHL api-web; Tennis Abstract; UEFA; Squiggle; BOM; MET Norway; Baseball Savant |
| **Proxy** | Prefix `https://r.jina.ai/` to render a blocked or JavaScript page as text. Check the dates, because the proxy can serve stale copies | ESPNcricinfo pages; FotMob pages; ITF draws |
| **Blocked** | Failed on every route tested. Do not plan on it | See §4 |

**If a route fails:** record the route, time and failure, then move immediately to the next route for that field in §1.7 and the sport table. Try another access mode only when it is likely to expose the actual record; do not spend the pregame window repeatedly fetching one broken route. One failure is a `RETRIEVAL_MISS`, not proof that the data do not exist. A page that returns HTTP 200 but only a JavaScript shell is `JS_ONLY — RENDER REQUIRED`: use a browser or an allowed proxy. Recheck the field owner at the final refresh if time permits. A fallback does not waive the source-count, field-owner, exact-event or issue-time gates.

### 1.7 Immediate fallback by field (retrieval control, 2026-09-28)

For **each missing fact**, run the next applicable route at once. Log every attempted URL or endpoint, retrieval time, response (`OPENED`, `BLOCKED`, `JS_ONLY`, `STALE`, `WRONG_EVENT`, `NOT_PUBLISHED` or `RETRIEVAL_MISS`), exact field obtained, and upstream lineage. A search result only discovers a route. Do not copy a later result or lineup back into a pregame card. Separate the unavailable field from the rest of a usable source.

| Missing field | Route sequence | Stop condition |
|---|---|---|
| Event ID, date, start or state | Competition's exact-game feed or match centre → its official schedule or club match page → independent structured scoreboard → named independent report. Check venue-local date, timezone, participants and competition at every hop. | If exact identity or state is still ambiguous, do not infer `PREGAME` from the clock. |
| Starter, lineup, team sheet, inactives or toss | Official exact-game roster/team-sheet feed → official league or club release, including an authenticated original post (§1.8) → two independent current reporting lineages for an unresolved critical field, under `CURRENT_RULES.md` §D2. | Keep projected and confirmed separate. An unviewable post, projected lineup or later box score never proves pre-issue availability. |
| Injury, rest, roster move or coaching change | Timed league report or registration list → team/board release → authenticated original team/player announcement (§1.8, limited to what it says) → named independent reporter with the §1.5 receipt. | Do not convert a roster registration, practice appearance or absence from a page into confirmed game availability. |
| Weather, roof, surface or pitch | Exact-game field-owner/venue report → venue-coordinate hourly weather or national meteorological service → named venue/official report. Baseball and cricket retain their sport-specific weather/strip rules. | A city forecast or generic pitch description does not replace an exact-game reading. |
| Season rates, game logs or specialist metrics | Field-owning official stats → official competition/team history → independent specialist data with definition and cutoff. Use only games complete before the card's input cutoff. | Missing or revised historical data stay missing; never backfill a rate from a later page. |
| Terminal result and process record | Exact-game official final feed/scorecard → another official route for field-level cross-check → independent structured scorecard and independent report until three upstream lineages agree. | Two official fronts on one feed count once. A recap alone, live page or score without an explicit terminal marker cannot settle. |

If the next route also fails, continue through the remaining routes promptly; record the attempt and then fail closed on the field. The sport-specific sequences below identify the first practical alternates. Source discovery does not imply that every competition, target or historical date is covered.

### 1.8 Original social posts: conditional evidence, not a separate lineage

**Admit only an original post that can be opened in full before the card's cutoff** and whose account is authenticated from the league, club, tournament or governing body's own site, an official cross-link, or a verified domain handle. A platform badge alone is supporting evidence, not proof of the account's authority for every field. Record the exact post URL, account/organisation, platform, publication time (with timezone), retrieval time, visible text or image contents, claimed field and any later edit/correction. If the post's timestamp, image text or account identity cannot be read, use it for discovery only. Do not infer a player is fit from a photo, a training clip or silence.

An official account may announce its **own** starters, team list, withdrawal, roster change, roof status or schedule change; it does not become a source for unrelated statistics or another organisation's selection. A named player may confirm their own statement, but the team or competition still controls official participation. An official post, its embedded copy on the official site and a news article quoting it are **one upstream lineage**. Reposts, screenshots without the original, fan accounts, tipsters, fantasy/DFS accounts and market-bearing posts remain excluded. Social posts never settle a game without the exact-game terminal record and the required independent lineages.

| Platform or route | Use and access decision |
|---|---|
| Official organisation website's social links → exact Instagram/Facebook/YouTube post | Conditional source for that organisation's original announcement if the post contents and publication time are actually visible. A verified YouTube channel badge supports identity; the exact video must be watched or its official transcript read. [MLB club account directory](https://www.mlb.com/mariners/social); [YouTube verification guidance](https://support.google.com/youtube/answer/3046484?hl=en). |
| Bluesky exact post from an organisation-owned domain handle or officially cross-linked account | Conditional only after resolving the account identity and opening the post. Earlier six unverified sports handles remain unadmitted. [Bluesky domain-handle guidance](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial); [badge guidance](https://bsky.social/about/blog/04-21-2025-verification). |
| X/Twitter, Reddit, inaccessible Instagram/Facebook posts | X and Reddit remain blocked in this environment; an inaccessible post is `RETRIEVAL_MISS`, even if a snippet displays text. Seek the organisation's website, another public platform, a press release or an independent reporter instead. Re-test access before changing that status. |

The same rule applies in every sport. Sport-specific social uses and the next non-social routes are indexed in §3.11; no platform or account is pre-approved without an exact-post check for the event.

---

## 2. Cross-sport sources

### 2.1 ESPN site API (keyless; plain request; one date per scoreboard call)

| Route | Fields | Verified 2026-09-28 |
|---|---|---|
| `https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/scoreboard?dates=YYYYMMDD` | Events, state, scores, `neutralSite`, `season.type`. **Date ranges return HTTP 400**: use one date per call | MLB, NFL, NCAAF, NBL, NHL, AFL, NRL (`rugby-league/3`), EPL, MLS, J1, UCL, Super Rugby, URC, EuroLeague, ATP, CPL cricket: 200 |
| `…/<sport>/<league>/summary?event=<id>` | Box score, starters (`starter`, `didNotPlay`), soccer XI and `wonCorners`, cricket toss note and powerplay, MLB umpires and injuries, key events | NBL: 200 |
| `https://site.api.espn.com/apis/v2/sports/<sport>/<league>/standings` | **`pointsFor`, `pointsAgainst`, `gamesPlayed`** (or wins + losses), home/road records. This is the TB-1-MD input (`PROBABILITY_TOOLKIT.md` §4) | NBA, WNBA, NBL, NFL, AFL, NRL, EPL, La Liga, A-League, NHL, MLB: 200 |
| `…/site/v2/sports/<sport>/<league>/injuries` | League injury list with status | NFL, NBA, WNBA, MLB, NHL: 200 |
| `…/site/v2/sports/<sport>/<league>/teams/<id>/schedule` | A team's completed games and scores | WNBA: 200 (NRL returned HTTP 500 on 2026-09-25) |
| **Not on ESPN** | KBO and NPB (`baseball/kbo`, `baseball/npb`: HTTP 400) | Use the official league sites (§3.1) |

**League slugs:**
- basketball: `nba`, `wnba`, `nbl`, `euroleague`;
- football: `nfl`, `college-football`;
- `australian-football/afl`; `rugby-league/3` (NRL; its regular season is season type 1); `hockey/nhl`;
- soccer: `eng.1`, `esp.1`, `ger.1`, `ita.1`, `fra.1`, `usa.1`, `aus.1`, `jpn.1`, `uefa.champions` and more;
- `tennis/atp` and `tennis/wta`; cricket by league ID (CPL 8676 or 8623);
- rugby union by league ID (URC 270557, Super Rugby 242041).

A league slug that returns 400 is not proof of non-coverage (the Slovak leagues 400; `uga.1` was only stale).

### 2.2 Weather (every outdoor event: an hourly venue-coordinate forecast for the match window, in venue-local time)

| Source | Route | Access | Verified |
|---|---|---|---|
| **Open-Meteo** (global) | `https://api.open-meteo.com/v1/forecast?latitude=<lat>&longitude=<lon>&hourly=temperature_2m,precipitation_probability,precipitation,wind_speed_10m,wind_direction_10m,dew_point_2m,cloud_cover&timezone=<IANA>` | API | 200 |
| Open-Meteo archive (observed, for settlement notes) | `https://archive-api.open-meteo.com/v1/archive?…&start_date=…&end_date=…` | API | 200 |
| **US National Weather Service** (US venues) | `https://api.weather.gov/points/<lat>,<lon>`, then its `forecastHourly` URL | API | 200 |
| **Bureau of Meteorology** (Australia) | `https://www.bom.gov.au/` forecasts; observations `…/fwo/IDN60901/IDN60901.94768.json` (Sydney) | Browser | 200 |
| **Japan Meteorological Agency** | `https://www.jma.go.jp/bosai/forecast/data/forecast/<area>.json` (Tokyo 130000) | API | 200 |
| **MET Norway** (Europe and global) | `https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=<lat>&lon=<lon>` | Browser | 200 |
| **MLB only:** the statsapi gamefeed `gameData.weather` (field-relative wind) | See §3.1 | API | 200 |

**Weather rules:**
- Never use a city forecast for an MLB total (M30).
- Downgrade for rain only inside the match window (G15.1).
- Record the roof state for retractable venues.

### 2.3 Research accelerators (never field owners)

| Source | Use | Access | Verified |
|---|---|---|---|
| **StatMuse** (`https://www.statmuse.com/<nba|wnba|mlb|nfl|nhl>/ask/<question>`) | US-sport L5/L10/L15/L20 splits and quick baselines. Check the dates and scope of every answer | Browser | 200 |
| **r.jina.ai proxy** (`https://r.jina.ai/<url>`) | Renders blocked or JavaScript pages as text | API | 200 |
| Reference sites: Basketball-Reference, Hockey-Reference | History and cross-checks | Browser | 200 |

---

## 3. Sport tables

The **Role** column:
- **FO** field owner;
- **P** primary;
- **S** independent secondary (a lineage of its own);
- **F** fallback;
- **D** discovery only.

"New" marks a source added on 2026-09-28.

### 3.1 Baseball — MLB, NPB, KBO, CPBL, LMB

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| MLB Stats API: schedule | `https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=YYYY-MM-DD&hydrate=probablePitcher,linescore` | Games, probable starters, state, line scores | FO | API | 200 |
| MLB gamefeed | `https://statsapi.mlb.com/api/v1.1/game/<gamePk>/feed/live` | `gameData.weather`, probables, `battingOrder` (a starter's slot ends in `00`), officials, `codedGameState`, line score, decisions | FO | API | 200 |
| MLB boxscore | `https://statsapi.mlb.com/api/v1/game/<gamePk>/boxscore` | Official orders, pitching lines, `info[]` weather and wind | FO | API | 200 |
| MLB starting-lineups page | `https://www.mlb.com/starting-lineups` | Published batting orders; resolve the exact game and publication time before treating an order as confirmed | FO | Browser | Opened 2026-09-28 |
| MLB standings (new) | `https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season=YYYY` | Runs scored and allowed, records | FO | API | 200 |
| MLB transactions (new) | `https://statsapi.mlb.com/api/v1/transactions?startDate=…&endDate=…` | IL moves, call-ups | FO | API | 200 |
| MLB team stats (new) | `https://statsapi.mlb.com/api/v1/teams/stats?season=YYYY&group=pitching&stats=season&sportIds=1` | Team pitching and hitting | FO | API | 200 |
| Baseball Savant (new) | `https://baseballsavant.mlb.com/probable-pitchers`; expected-stats leaderboard (`…/leaderboard/expected_statistics?type=pitcher&year=YYYY`) | Probables with Statcast profile; xERA/xwOBA | P | Browser | 200 |
| ESPN MLB | §2.1 scoreboard, summary, injuries | Injuries, umpires, state | S | API | 200 |
| NPB official (English) | `https://npb.jp/bis/eng/YYYY/games/` (day index `gmYYYYMMDD.html`); standings `https://npb.jp/bis/eng/YYYY/stats/std_c.html` (Central) and `std_p.html` (Pacific) | Finals, box scores, standings | FO | API | 200 |
| NPB probable starters (new) | `https://npb.jp/announcement/starter/` (予告先発, the official announcement) | Next day's starters | FO | API | 200 |
| NPB active roster registration | `https://npb.jp/announcement/roster/` | Registered and deregistered players; registration alone does not confirm that game's availability | FO | Browser | Opened 2026-09-28 |
| NPB score pages | `https://npb.jp/scores/YYYY/MMDD/<away>-<home>-<nn>/` | 【試合終了】 final marker, 12-inning line score | FO | API (403 on the day index on 2026-09-28; the game pages worked on 2026-09-25) | mixed |
| KBO official (English) | `https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=YYYY-MM-DD`; standings `…/Standings/TeamStandings.aspx` | FINAL, line score, R/H/E, W/L/S, standings | FO | API | 200 |
| KBO official (Korean, new) | `https://www.koreabaseball.com/Schedule/Schedule.aspx` | Schedule, starters (Korean) | FO | API | 200 |
| KBO active registration | `https://www.koreabaseball.com/player/register.aspx`; full roster `https://www.koreabaseball.com/Player/RegisterAll.aspx` | Current registration and roster context; not a confirmed batting order | FO | Browser | Opened 2026-09-28 |
| CPBL (new) | `https://www.cpbl.com.tw/` (plain request); `https://stats.cpbl.com.tw/` (browser) | Schedule, box, batting order | FO | API or Browser | 200 |
| CPBL club lineup record | `https://cpbl.com.tw/team/lineuprecord?ClubNo=<club>` | Dated batting-order history and cross-check; today's row needs an observed pregame timestamp | FO | Browser | Opened 2026-09-28 |
| LMB | The official club report, then the league result | Final, pitching | FO/F | Browser | earlier |
| LMB official roster | `https://lmb.com.mx/roster` | Team roster context, never proof of today's lineup | FO | Browser | Opened 2026-09-28 |
| Fangraphs, Baseball-Reference | — | — | — | **Blocked** from here (403, even through the proxy). A browser may work; never plan on it | — |

**Settlement lineages:**
- MLB: statsapi (FO) + ESPN + one independent report or box.
- NPB and KBO: the official page + ESPN-independent media (e.g. Nikkan Sports or Yonhap) + a third report.

### 3.2 Basketball — NBA, WNBA, NBL, EuroLeague, ACB, FIBA, LKL and others

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| ESPN (NBA, WNBA, NBL, EuroLeague) | §2.1 scoreboard, summary, standings, injuries | Starters, `didNotPlay`, box, standings PF/PA | P | API | 200 |
| NBA official injury report (new in this register) | `https://official.nba.com/nba-injury-report-2025-26-season/` (links to timed PDFs) | Official status at a stamped time | FO | Browser | 200 |
| WNBA official injury report (new) | `https://www.wnba.com/wnba-injury-report` | Official status | FO | Browser | 200 |
| NBA daily lineups page | `https://www.nba.com/players/todays-lineups` | Potential official starters after rendering and exact-game check | FO | Browser | JS_ONLY on 2026-09-28; not an unattended fallback |
| NBL official | `https://www.nbl.com.au/` match pages; match data `schedule.nbl.com.au/api/calendar/match?match=<uuid>&league=NBL`. The first `jumpBall` event is the actual tip; skip the `betting`/`odds` objects | Tip time, play-by-play, box | FO | API | Site 200; the match API needs the match UUID from the page |
| NBL dated injury list | `https://www.nbl.com.au/news/nbl26-the-latest-injury-updates` (page titled NBL27; resolve by current title/date, not the slug) | League-listed injury context; recheck club/game-day status | FO | Browser | Opened 2026-09-28; page updated 27 Sep |
| EuroLeague official feeds (new) | `https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/E/seasons/E<yyyy>/games` (plain); `https://api-live.euroleague.net/v2/competitions/E/seasons/E<yyyy>/games` (browser) | Schedule, results, box | FO | API or Browser | 200 |
| ACB (Spain, new) | `https://www.acb.com/` and `https://live.acb.com` | Results, box. The site and the live stats are **one lineage** | FO | API | 200 |
| ACB medical and availability news | `https://acb.com/es/minicopa/noticias/novedades-y-parte-medico-para-la-jornada-1-de-la-liga-endesa-2026-27-146114` (dated example; find the current round) | Round-specific medical and availability notes | FO | Browser | Opened 2026-09-28 |
| FIBA | `https://www.fiba.basketball/en/events/<event>/games/<id>-<HOME>-<AWAY>` | Final, quarters, box. Check the event date: pages can show an old head-to-head | FO | Browser or Proxy | 200 |
| FIBA LiveStats competition link | Find the exact event's official match-centre link; product description: `https://about.fiba.basketball/en/services/data-and-video-solutions/fiba-live-stats` | Live box and player participation where the competition actually uses it; product page is discovery only | FO for that competition | Browser | Product page opened 2026-09-28; exact-game coverage untested |
| Basketball-Reference (WNBA and NBA history, new) | `https://www.basketball-reference.com/wnba/years/YYYY.html` | Team and player history | S | API | 200 |
| Proballers (new) | `https://www.proballers.com/` | International rosters and player lines | S | Browser | 200 |
| Eurobasket (new) | `https://basketball.eurobasket.com/` | International leagues, rosters, injuries | S | Browser | 200 |
| BasketNews (LKL) | `r.jina.ai/https://www.basketnews.lt/…` | Finals, quarter lines | S | Proxy | earlier |
| RealGM, NBA CDN JSON | — | — | — | **Blocked** from here | — |

**Settlement lineages:** ESPN summary + the league's own box + an independent report (e.g. Basketball-Reference or BasketNews). The league site and its live-stats page count once.

### 3.3 Cricket

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| ESPN cricket API | `…/sports/cricket/<leagueId>/scoreboard` and `summary?event=<id>` (CPL league 8623 or 8676); ball-by-ball `…/playbyplay?event=<id>&period=<inn>&page=<n>` | Toss note, XIs, powerplay, innings totals. **One lineage with ESPNcricinfo** | P | API | 200 |
| Cricbuzz | `https://www.cricbuzz.com/cricket-match/live-scores`; the scorecard page | Live, scorecard, commentary (a transcript of the broadcast pitch report is the broadcast's lineage) | S | API | 200 |
| ICC | `https://www.icc-cricket.com/` | International identity, reports, toss/pitch videos | FO (ICC events) | API | 200 |
| ICC squad replacement announcements | `https://www.icc-cricket.com/media-releases/rawat-approved-as-replacement-for-patil-in-india-squad` (dated example; find current event) | Tournament squad change, not proof of XI selection | FO (ICC events) | Browser | Opened 2026-09-28 |
| CPL official | `https://www.cplt20.com/` | Fixtures, official final report. CaribbeanCricket and CricTracker republish it (one lineage) | FO | API | 200 |
| IPL official (new) | `https://www.iplt20.com/` | Fixtures, toss report, results | FO | API | 200 |
| Cricket Australia (BBL, WBBL, internationals in Australia) | `https://www.cricket.com.au/matches` | Match centre, toss, teams | FO (Australia) | API | 200 |
| ECB scorecards for ECB competitions | `https://www.ecb.co.uk/county-championship/matches/112933/scorecard` (example; navigate to exact event) | Scorecard, toss and teams when published | FO (ECB competitions) | Browser | Opened 2026-09-28 |
| ESPNcricinfo pages | Through the proxy only: `r.jina.ai/https://www.espncricinfo.com/…` | Scorecard, commentary | S (same lineage as ESPN) | Proxy | 200 |
| Cricsheet | `https://cricsheet.org/downloads/` | Historical ball-by-ball for venue and phase history | P (history) | API | 200 |
| Howstat | `https://www.howstat.com/cricket/home.asp` | Historical records | S | Browser (intermittent) | mixed |

**Toss and strip protocol (kept in full from the old register §6A):**
- **Toss ladder:**
  - T1: the official match centre or board scorecard;
  - T2: the rights-holder broadcast or the official video;
  - T3: an official live blog;
  - T4: the ESPN toss note;
  - T5: a specialist scorecard;
  - T6: a named reporter.

  If none is found, `TOSS STATUS = NOT_VERIFIED_AFTER_SEARCH`. Never infer the toss from the innings order.
- **Strip ladder:**
  - P1: a named broadcast pitch report on the day;
  - P2: the curator or venue;
  - P3: an official toss report quoting the captain;
  - P4: a transcript of P1 (the same lineage as P1);
  - P5: a named reporter;
  - P6: the preceding match on a different strip (context);
  - P7: the venue's history by innings order;
  - P8: ICC pitch ratings (reputation only).

  Only P1–P5 set `STRIP STATUS = OBSERVED`.
- **Pitch metadata that is identical across sites is one automated lineage** (`AUTOMATED_PITCH_METADATA`), never an observation.
- **Excluded pitch-report sites** (formulaic or fantasy): cricklive.in, pitch-report.com, crickonly.in, cricketstadiumsinfo.com, thecricscope.com, jaipurcircle.com, cricjosh.in, cricketfastliveline.in, bjsports.live, and any page with the same pattern.
- **Refresh:** at the toss window and again immediately before issue. Record whether the freeze was `PRE_TOSS` or `POST_TOSS`.

**Settlement lineages:** the official final report or scorecard + Cricbuzz + ESPN (ESPN and ESPNcricinfo count once). A duck needs a dismissal, not just 0 runs.

### 3.4 Soccer

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| ESPN soccer | §2.1: scoreboard, summary (XI, bench, `wonCorners`, key events), standings | XI, stats, standings GF/GA | P | API | 200 |
| Premier League (pulselive) | `https://footballapi.pulselive.com/football/fixtures?comps=1&compSeasons=<id>&statuses=C` (send `Origin`/`Referer` `https://www.premierleague.com`) | **EPL corners and match stats (field owner)** | FO | API | 200 |
| Premier League injury updates | `https://www.premierleague.com/en/latest-player-injuries` | Dated availability reports; confirm team selection at the game cutoff | FO | Browser | Opened 2026-09-28 |
| UEFA match API | `https://match.uefa.com/v5/matches?competitionId=<id>&seasonYear=<yyyy>` | UEFA fixtures, lineups, stats (field owner for UEFA corners) | FO | Browser | 200 |
| UEFA match information kits | `https://www.uefa.com/news-media/mediaservices/informationkits/competitions/uefachampionsleague/2026/match/2045976/` (example; navigate to exact match) | Dated squad, history and match context; final XI must still be checked | FO (UEFA matches) | Browser | Opened 2026-09-28; content may require rendering |
| League official sites (new) | laliga.com, bundesliga.com, ligue1.com, kleague.com, keepup.com.au (A-League), `data.j-league.or.jp` | Official fixtures, lineups, stats | FO | API | 200 (Serie A redirects: use legaseriea.it through the browser) |
| Club official site or app | The club's match centre, and the XI about 60 minutes before kick-off | **The confirmed XI** (it beats predicted-lineup pages) | FO | Browser | — |
| FotMob (new route) | `https://www.fotmob.com/api/data/leagues?id=<id>` and `…/api/data/matches?date=YYYYMMDD`; pages via the proxy | Fixtures, lineups, xG, tables | S | API | 200 |
| Understat (new) | `https://understat.com/league/<EPL\|La_liga\|Bundesliga\|Serie_A\|Ligue_1>/<season>` | xG for and against by team | S | API | 200 |
| Transfermarkt injuries (new) | `https://www.transfermarkt.com/<league>/verletztespieler/wettbewerb/<code>` (EPL GB1) | Injuries and suspensions | S | API | 200 |
| openfootball (new) | `https://raw.githubusercontent.com/openfootball/football.json/master/<season>/<code>.json` | Historical fixtures and results | S (history) | API | 200 |
| ClubElo | `http://api.clubelo.com/<date>` | European club Elo | S | — | **HTTP 502 on 2026-09-28** (unverified; retry) |
| FBref, Sofascore, WorldFootball | — | — | — | **Blocked** (Cloudflare 403, even through the proxy) | — |

**Settlement lineages:** the league or competition official page + ESPN + FotMob or a named report.
- Corners settle with the field owner: pulselive for the EPL, the UEFA API for UEFA competitions, ESPN `wonCorners` otherwise.
- **Never settle from a placeholder** (the Uzbekistan PFL 0–0 shell).

### 3.5 AFL and AFLW

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| AFL API (new in this register) | `https://aflapi.afl.com.au/afl/v2/matches?competitionId=1&compSeasonId=<id>` (AFLW `competitionId=3`); `…/afl/v2/competitions` | Fixtures, results, venues, IDs | FO | API | 200 |
| AFL team lineups (new) | `https://www.afl.com.au/matches/team-lineups` | **Official team selections, ins/outs, emergencies** | FO | API | 200 |
| AFLW team pages | `https://www.afl.com.au/aflw/teams` → exact club and match team selection | AFLW club roster and official releases; a roster page alone is not the selected side | FO | Browser | Opened 2026-09-28; exact match selection untested |
| ESPN AFL | §2.1 scoreboard and standings (PF/PA) | Results, standings, the TB-1-MD input | P | API | 200 |
| AFL Tables (new) | `https://afltables.com/afl/seas/YYYY.html` | Complete results and scoring history | S | API | 200 |
| Footywire (new) | `https://www.footywire.com/afl/footy/ft_match_list` | Results, player stats | S | API | 200 |
| Squiggle API (new) | `https://api.squiggle.com.au/?q=games;year=YYYY` and `?q=standings;year=YYYY` | Results and standings. **The `tips` query is other models' tips: discovery only** | S | Browser | 200 |
| BOM | §2.2 | Venue weather | FO (weather) | Browser | 200 |

**Separation rule:** AFLW is a separate population. The men's widths, home edge and base rates never transfer.

### 3.6 NRL and rugby league

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| NRL draw data (new) | `https://www.nrl.com/draw/data?competition=111&season=YYYY&round=<n>` | Fixtures, state (`matchMode`, `matchState`), scores | FO | API | 200 |
| NRL ladder (new) | `https://www.nrl.com/ladder/data?competition=111&season=YYYY` | Points for and against, played | FO | API | 200 |
| NRL team lists (new) | `https://www.nrl.com/news/topic/team-lists/` | Tuesday lists, then the final 1–17 changes | FO | API | 200 |
| NRLW official team-list releases | `https://www.nrl.com/news/2026/08/11/nrlw-team-lists-round-7/` (dated example; find current round) | Named NRLW team lists and changes | FO | Browser | Opened 2026-09-28 |
| ESPN NRL | `rugby-league/3` scoreboard and standings | Results, half-time line score | P | API | 200 |
| Rugby League Project (new) | `https://www.rugbyleagueproject.org/seasons/nrl-YYYY/summary.html` | Results, history | S | API | 200 |

### 3.7 Rugby union

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| World Rugby rankings (new) | `https://api.wr-rims-prod.pulselive.com/rugby/v3/rankings/mru` (men), `…/wru` (women) | Official rating points: a strength input for internationals | FO | API | 200 |
| World Rugby fixtures (new) | `https://api.wr-rims-prod.pulselive.com/rugby/v3/match?startDate=…&endDate=…` | International fixtures and results | FO | API | 200 |
| World Rugby fixture and match centre | `https://www.world.rugby/tournaments/fixtures-results` → exact match | Fixtures, results and match centre; verify the team-sheet tab separately | FO (World Rugby events) | Browser | Opened 2026-09-28 |
| ESPN rugby | League IDs (URC 270557, Super Rugby 242041, others) | Results, line-ups | P | API | 200 |
| Competition official sites | URC, Premiership, Top 14, Super Rugby | Team sheets (48 hours ahead), results | FO | Browser | — |

### 3.8 NFL and college football

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| ESPN NFL and NCAAF | §2.1 scoreboard, summary, standings, **injuries** | Results, standings PF/PA, injury list | P | API | 200 |
| NFL official injuries | `https://www.nfl.com/injuries/` | Official practice and game status | FO | API | 200 |
| NFL official inactives | The team or league release about 90 minutes before kickoff | Inactives, QB status | FO | Browser | — |
| NFL inactives hub | `https://www.nfl.com/inactives/` → exact game and week | Published inactive list; off-season or empty page is `NOT_PUBLISHED` | FO | Browser | Opened 2026-09-28; no current game list |
| NFL official game books | `https://support.nfl.com/hc/en-us/articles/35869678028180-Game-Books` → exact game's book | Postgame participation and scoring cross-check; never a pregame lineup | FO | Browser | Opened 2026-09-28 |
| NCAA football scoreboard | `https://www.ncaa.com/scoreboard/football/fbs` → exact game/competition | College fixture and result cross-check; team athletic departments own injury/availability releases | FO for NCAA event results | Browser | Opened 2026-09-28 |
| nflverse (new in this register) | `https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv` (results columns only) | Historical results and schedule | P (history) | API | 200 |
| Pro-Football-Reference | — | — | — | **Blocked** from here | — |

### 3.9 NHL

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| NHL api-web | `https://api-web.nhle.com/v1/schedule/YYYY-MM-DD`; `/v1/score/YYYY-MM-DD`; `/v1/gamecenter/<id>/boxscore`; `/v1/standings/now` | Schedule, `gameType` (**1 = preseason, 2 = regular**), goals with `empty-net` modifier, goalie TOI, standings | FO | Browser | 200 |
| NHL stats API (new) | `https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=seasonId=<yyyyyyyy>` and `/goalie/summary?…` | Team and goalie season stats | FO | Browser | 200 |
| NHL official status reports | `https://www.nhl.com/news/nhl-status-report-news-and-notes-february-21-2026` (dated example; find the newest report) | Dated injuries, transactions and club statements; no automatic starter confirmation | FO | Browser | Opened 2026-09-28 |
| Daily Faceoff (new) | `https://www.dailyfaceoff.com/starting-goalies/` | Projected and confirmed starting goalies, with the source quoted. It needs the S-1 receipt until the team confirms | S | Browser | 200 |
| MoneyPuck (new) | `https://moneypuck.com/data.htm` | Expected goals and shot data | S | Browser | 200 |
| Hockey-Reference (new) | `https://www.hockey-reference.com/leagues/NHL_YYYY.html` | History | S | API | 200 |
| ESPN NHL | §2.1 | Results, standings, injuries | P | API | 200 |
| Natural Stat Trick | — | — | — | **Blocked** from here | — |

### 3.10 Tennis

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| **Tennis Abstract Elo** | `https://tennisabstract.com/reports/atp_elo_ratings.html`, `…/wta_elo_ratings.html` | Overall, hard, clay and grass Elo, with the page date. The **blocking benchmark** (`RULES_TENNIS.md` TE-P5; `PROBABILITY_TOOLKIT.md` §6). Snapshot it before the match: the page is re-dated on match day | P | Browser | 200 |
| ESPN tennis | `tennis/atp` and `tennis/wta` scoreboards | Set scores, `STATUS_RETIRED` and `STATUS_WALKOVER`. Covers Slams, tour events and WTA 125, not ITF | P | API | 200 |
| WTA API (new) | `https://api.wtatennis.com/tennis/tournaments/?page=0&pageSize=…` | Tournaments, draws | FO | API | 200 |
| WTA match page and draw PDF | `wtatennis.com/tournaments/<id>/<slug>/<yyyy>/scores/<matchId>`; `wtafiles.wtatennis.com/pdf/draws/<yyyy>/<id>/MDS.pdf` | Exact-match state and score | FO | Browser | earlier |
| WTA tournament order of play | `https://www.wtatennis.com/tournaments/wimbledon/order-of-play/` (example; find exact event/day) | Scheduled court/order and changes; confirm terminal state separately | FO (WTA events) | Browser | Opened 2026-09-28 |
| ATP Tour | `https://www.atptour.com/en/scores/current` | Draws, scores | FO | Browser | 200 |
| ITF draws | `r.jina.ai/https://www.itftennis.com/en/tournament/<slug>/…/draws-and-results/` | ITF results | FO | Proxy (the direct route is Incapsula-blocked) | earlier |
| ITF order of play | `https://www.itftennis.com/en/tournament/m25-monastir/tun/2026/m-itf-tun-2026-001/order-of-play/` (example; find exact event/day) | Court schedule and withdrawals as displayed; direct access can vary | FO (ITF events) | Browser or Proxy | Opened 2026-09-28 |
| Tennis Majors | `tennismajors.com/matches/…` | Terminal state, score | S | Browser | earlier |
| TennisExplorer, Flashscore | Scores only; **the odds columns are never read** | S | Proxy or Browser | 200 |
| Sackmann tennis repositories | — | — | — | **HTTP 404** (moved or removed) | — |

### 3.11 Field fallback and official social use by sport

Use the table for the **missing field only**; move to the next route immediately after `BLOCKED`, `JS_ONLY` without a renderer, `STALE`, `WRONG_EVENT` or `RETRIEVAL_MISS`. A page marked `NOT_PUBLISHED` calls for a timed refresh around the expected release, while other fields continue. For every sport, a verified original team or competition social post can carry only the field its author controls (§1.8). Its existence does not establish an additional independent lineage or override a newer official correction. An official web article copying the post is the same release.

| Sport / competitions | Practical route after exact-game field-owner feed or match centre | Original official social post that may help | If still missing |
|---|---|---|---|
| Baseball: MLB / NPB / KBO / CPBL / LMB | MLB starting lineups and transactions; NPB starter announcement then registration; KBO Korean schedule then registration; CPBL exact-game box then club lineup record; LMB club release then league roster | Club's own dated batting order, starter or transaction post; confirm the club account from its official site | Independent named reporter for a projected starter, then unresolved if no confirmed order. Registration/roster pages never become an order. |
| Basketball: NBA / WNBA / NBL / EuroLeague / ACB / FIBA and others | Dated NBA/WNBA league injury report; NBL dated injury list and club report; ACB round medical report; exact-game EuroLeague/FIBA live box when published. NBA daily-lineups page needs rendering | Club or league's explicit active roster, injury update or starting-five announcement | Independent current report with provenance; if starters/rotation remain unknown, preserve the availability branch and applicable card cap. |
| Cricket: ICC / IPL / CPL / BBL / WBBL / ECB and others | Follow the toss and strip ladders in §3.3; board/league exact-game scorecard, ICC squad notice or ECB scorecard where applicable | Board, tournament or club's explicit XI, toss, withdrawal or venue announcement | Broadcast/official live blog, then specialist scorecard or named reporter in ladder order. A squad announcement does not establish the XI. |
| Soccer: domestic leagues / UEFA / international | League exact-match page, UEFA match kit for context, club website/app for XI, then the dated league injury page where applicable | Club or national association's full team sheet, injury or withdrawal post | Independent current match report; do not promote an expected XI to confirmed. Check bench and goalkeeper separately. |
| AFL / AFLW | AFL official match/team-lineup page; AFLW club's exact-match team release; competition and club injury/selection news | Club's complete named side, emergencies or late-change post | Independent current team-list reporting; AFLW roster page is context only, and AFL men's rates never transfer. |
| NRL / NRLW and other rugby league | NRL topic page, exact round team list and late mail; club site for changes. For other leagues, find that competition's governing-body page first | Club/league's explicit final 1–17, late change or withdrawal | Independent named report; a Tuesday list does not confirm the final game-day side. |
| Rugby union | World Rugby exact match centre for its events; competition match centre, union/club team-sheet release and late change | Union or club's full XV and replacements, injury or late-change notice | Independent named report; keep XV and bench separate, and verify event-specific rules. |
| NFL / NCAA football | NFL injury report then inactives hub; exact club release; NCAA scoreboard and school athletics report for college games | Team or school athletics account's explicit inactive or QB-status release | Independent named report; game book is postgame only. College injury disclosure may be incomplete, so retain uncertainty. |
| NHL | NHL gamecenter and dated status report; club's game-day release for confirmed goalie and scratches | Club's explicit starting-goalie, scratch or injury post | Independent current goalie report with S-1 receipt remains projected until a field-owning confirmation; never infer from morning-skate photos. |
| Tennis: ATP / WTA / ITF | Tour exact-match page and current draw; WTA/ITF order of play and tournament desk's change notice | Tournament/tour's explicit withdrawal, walkover, court or schedule change; player's own health statement is limited to their words | Independent match report; an order of play is a schedule, not proof the player started or a terminal result. |

**Coverage limit:** these are tested routes and decision rules, not a guarantee that a given competition publishes every field. Each game log must show what was actually retrieved before its own cutoff, the failed routes, the field's final status and the effect on the forecast. Keep league, season and women's/men's populations separate.

---

## 4. Blocked, failed or excluded (do not plan on these)

| Source | State on 2026-09-28 |
|---|---|
| Fangraphs, Baseball-Reference, Pro-Football-Reference, FBref, WorldFootball, Natural Stat Trick, RealGM | HTTP 403 (Cloudflare), even through the proxy |
| Sofascore API | 403 |
| NBA CDN JSON | 403 |
| ESPNcricinfo direct | 403; use the proxy |
| MLS stats API | 404 |
| Sackmann tennis (GitHub) | 404 |
| ClubElo | 502 (possibly temporary) |
| X (Twitter), Reddit | Blocked on every route (2026-09-19) |
| football-data.co.uk | Reachable, but its files carry bookmaker odds columns. **Excluded** under the firewall |
| Bookmakers, odds sites, tipsters, RotoWire, RotoGrinders, FPTrack, fantasy/DFS | **Prohibited** (§1.4) |
| sportscafe.in "AI simulation", archysport, AI recaps, formulaic pitch-report sites | **Prohibited** as synthetic content |

---

## 5. Keeping this register honest

- **A source enters** only with a reproducible retrieval: route, date, access mode and response. One good result never promotes a source; judge it on accuracy, timeliness and authority.
- **Re-test the table each month,** and whenever a route fails twice. Record the date in the "Verified" column.
- **New sources found during a card** go into the mini log's document mapping with their route. They are added here at the next import.
- Historical source audits removed from this tree remain in Git history.

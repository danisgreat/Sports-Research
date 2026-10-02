# Current source access controls - 2026-10-01

The executable [source registry](research/sources_registry.json) controls retrieval, league/parser/endpoint scope, market quarantine and permitted access. Use [sources.py](research/src/sources.py) for immutable bodies and receipts. The current source observation report is [source_observations.json](research/runs/implementation_2026-10-01/source_observations.json): ten routes returned the specified content; both ESPN probes returned HTTP 403; three entries require manual/local access or are excluded. Accessibility is not exact-event truth or independent collection.

Official league, club, university and gamebook sources are available alongside public statistical archives. The registry and archive receipts materially expand retained source evidence. Every current collector remains UNKNOWN independence pending a supported audit. Same upstream API, embedded provider, club syndication or copied report cannot count as a new lineage. For live evidence, retain both a collector audit and event/body-specific audit before the issue cutoff. Native JSON parsing and reviewed manual field mapping must verify the actual field owner and endpoint.

NBL uses the league schedule UUID and regular-season overtime-inclusive final. EPL openfootball supplies publisher score/schedule observations with a derived research ID; official IDs remain unknown until matched to a verified league event. MLB uses gamePk. NFL gamebooks and official CFB/AFLW source bodies support specific archive corrections. Increased source breadth does not authorize a model in an unvalidated sport.

Football-Data and FixtureDownload local raw snapshots keep their prior access/redistribution restrictions; automated source retrieval through those routes is blocked. Odds-bearing ESPN bodies, when retrievable, stay in the benchmark quarantine and only sports fields may be parsed through an audited adapter. Fantasy data remain excluded. Source errors are recorded without circumventing access controls.

The earlier provider directory below is historical routing guidance. Its access observations, active-manifest references and procedural claims are superseded by the current registry and CURRENT_RULES.md. Verify current official rules and exact fields whenever a route is used; a directory entry is not a receipt.

---

# Sources — the single source register

**Rebuilt 2026-09-28 for md-only operation; expanded 2026-09-28(f) and 2026-09-29(a).** This page merges the old quick reference and full register, and adds the sources verified on 2026-09-28/29. It is the only source document the model reads.
- **What changed on 2026-09-29(a):** about 90 further routes and social lanes were live-tested. Additions: new data routes in every sport table (marked "New (a)"); a social-platform access matrix (§1.8); cross-sport secondaries and discovery feeds (§2.4); and a **source-by-source fallback chain with that source's authenticated official social accounts** (§3.12). Handles in §3.12 were read from each organisation's own website on 2026-09-29, never guessed. **X (Twitter) is no longer blocked:** two keyless read routes work for official accounts (§1.8).
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
- **Mixed pages.** A page that mixes scores with odds columns may be used **for scores only** in a forecast or settlement. This applies to TennisExplorer, Flashscore and football-data.co.uk (whose results files carry bookmaker columns). By the user's 2026-09-29 instruction, a separate **post-settlement** benchmark may read closing columns for completed events only, after the forecast and official final are frozen; `research/src/benchmark.py` is outside every forecast import. Football-Data's own use notice limits automated bot/AI reuse, so its raw files stay local and are not redistributed from this repository.
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

If the next route also fails, continue through the remaining routes promptly; record the attempt and then fail closed on the field. The sport-specific sequences below identify the first practical alternates. **§3.12 gives the chain source by source:** for any named source, its "If it fails" cell is the next route to open at once, and its social cell is the organisation's own authenticated account for fields that organisation controls.

**Attempt ledger line (one per route tried):** `ROUTE <n> | <source> | <url or endpoint> | <retrieval time, venue-local and AEST> | <OPENED / BLOCKED / JS_ONLY / STALE / WRONG_EVENT / NOT_PUBLISHED / RETRIEVAL_MISS> | <field obtained or "none"> | <lineage>`. Stop at the first route that gives the field from its owner, or from an admissible route. Stop sooner only when the remaining routes cannot change the field before the cutoff. Source discovery does not imply that every competition, target or historical date is covered.

### 1.8 Original social posts: conditional evidence, not a separate lineage

**Admit only an original post that can be opened in full before the card's cutoff** and whose account is authenticated from the league, club, tournament or governing body's own site, an official cross-link, or a verified domain handle. A platform badge alone is supporting evidence, not proof of the account's authority for every field. Record the exact post URL, account/organisation, platform, publication time (with timezone), retrieval time, visible text or image contents, claimed field and any later edit/correction. If the post's timestamp, image text or account identity cannot be read, use it for discovery only. Do not infer a player is fit from a photo, a training clip or silence.

An official account may announce its **own** starters, team list, withdrawal, roster change, roof status or schedule change; it does not become a source for unrelated statistics or another organisation's selection. A named player may confirm their own statement, but the team or competition still controls official participation. An official post, its embedded copy on the official site and a news article quoting it are **one upstream lineage**. Reposts, screenshots without the original, fan accounts, tipsters, fantasy/DFS accounts and market-bearing posts remain excluded. Social posts never settle a game without the exact-game terminal record and the required independent lineages.

**Identity first.** An account is authenticated only if (a) the organisation's own website links to it (the handles in §3.12 were read that way on 2026-09-29), or (b) it is a Bluesky domain handle on the organisation's own domain. A platform badge alone is not enough. Look-alike accounts are common: `NBA Scores`, `MLB (bot)`, `NHL (Bot)`, `Premier League News` and `nhlcanucks.bsky.social` (0 posts) on Bluesky are all unofficial; `t.me/realmadrid` is **not** Real Madrid; `NBA@sportsbots.xyz` on Mastodon is a mirror.

**Platform access matrix (live-tested 2026-09-28/29, keyless, from this environment):**

| Platform | Working route | What it returns | Status and use |
|---|---|---|---|
| **X (Twitter)**: account timeline | `https://syndication.twitter.com/srv/timeline-profile/screen-name/<handle>` (browser user-agent). Parse the `__NEXT_DATA__` JSON: `props.pageProps.timeline.entries[].content.tweet` | About 17–20 recent posts with `id_str`, exact `created_at` (UTC), `user.screen_name` and `full_text` | **WORKS**: confirmed for `afl`, `premierleague` and `MLB` on 2026-09-29. `NBA` returned 429 on 2026-09-28 and was not retested. The first call can return HTTP 429; retry once after a short pause. Entries are not strictly chronological (pinned posts and reposts appear), so check `screen_name` and the time of each post |
| **X**: single post | `https://publish.twitter.com/oembed?url=https://x.com/<handle>/status/<id>` | Author name, author URL, full post text and the date (day only) | **WORKS** (keyless, no token). Use the timeline's `created_at` for the exact time. `cdn.syndication.twimg.com/tweet-result?id=<id>&token=<t>` also works, but needs an ID-derived token |
| X: other routes | `x.com` through the proxy (403); nitter.net (refused); xcancel.com (DNS failure) | — | **BLOCKED**. Do not plan on them |
| **Bluesky** | `https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=<handle>`; `…/app.bsky.feed.getAuthorFeed?actor=<handle>&filter=posts_no_replies&limit=<n>` | Profile, `verification.verifiedStatus`, and posts with exact ISO `createdAt` | **WORKS**. `app.bsky.feed.searchPosts` returns 403 without a login: read author feeds, don't search. Active official accounts: `nba.com`, `wnba.com`, `mets.com`, `mls-pr.bsky.social` (MLS Communications, verified). Verified but dormant: `mlb.com` (0 posts); seasonal: `rolandgarros.com`. `nhl.com` is unverified with 0 posts: do not use |
| **YouTube** | Channel videos tab `https://www.youtube.com/@<handle>/videos` (browser) → `"videoId"`; then `https://www.youtube.com/watch?v=<id>` → `uploadDate` / `datePublished`; `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<id>&format=json` → `author_name` | Exact upload time with offset (e.g. `2026-09-27T13:36:04-07:00`), title and channel identity | **WORKS**. Use it for official press conferences and team-announcement videos: the coach's words are that club's statement. The RSS feeds (`feeds/videos.xml?channel_id=` / `playlist_id=` / `user=`) returned 404/500 on every form on 2026-09-28 |
| **Threads** | `https://r.jina.ai/https://www.threads.net/@<handle>` and `…/@<handle>/post/<code>` | Post text and post URLs; times are **relative only** (`6h`, `3d`) | **WORKS through the proxy only**; the direct page is a JavaScript shell. Record the retrieval time and the relative age; the publication time is only known to within that unit. It can support pre-issue publication only when the bound falls wholly before the cutoff |
| Instagram | Profile API (429), proxy (403), profile embed (no timestamps) | — | **RETRIEVAL_MISS** by default. Use a post only if the organisation's own site embeds it with a visible date |
| Facebook | Proxy returns the login wall; the page plugin has no timestamps | — | **BLOCKED** |
| TikTok | Proxy renders the shell only | — | Not used: video-only, no reliable text or timestamp |
| Telegram | `https://t.me/s/<channel>` public preview | Posts with `datetime` | Works technically, but **no official sports channel has been authenticated**. Use one only if the organisation's website links it |
| Reddit | `.json`, `api.reddit.com` (403); `old.reddit.com/…/.rss` (block page) | — | **BLOCKED**. Fan content in any case, never evidence |
| Mastodon, Weibo | Mastodon search → bot mirrors only; Weibo 403 | — | Not used |

**Reporter and media accounts** (discovery for the named-reporter lane in §1.5; not field owners): verified Bluesky domain handles `apnews.com`, `reuters.com`, `nytimes.com`, `washingtonpost.com`, `latimes.com`, `bostonglobe.com`, `theguardian.com`, `theathleticfc.bsky.social`, `espn.com` (sparse) and `fangraphs.com`. `theathletic.com` showed verification `invalid` on 2026-09-28, so treat it as unverified. A reporter's post still needs the full §1.5 receipt.

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
| Meteostat bulk station history (New (a)) | `https://bulk.meteostat.net/v2/daily/<WMO station>.csv.gz` | API | 200 (observed daily history for settlement notes; never a pregame forecast) |

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

### 2.4 Cross-sport secondaries and discovery feeds (New (a), tested 2026-09-28/29)

| Source | Route | Use | Role | Access | Verified |
|---|---|---|---|---|---|
| **BBC Sport** scores and fixtures | `https://www.bbc.com/sport/<football\|rugby-union\|rugby-league\|cricket\|tennis>/scores-fixtures/YYYY-MM-DD` | Independent results and state (FT / full time / Result) for UK and international football, rugby and cricket | S (own lineage) | Browser | 200 (football, rugby union, cricket) |
| TheSportsDB | `https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d=YYYY-MM-DD&s=<Soccer\|Baseball\|Basketball\|…>` | Cross-sport event list: an identity cross-check and a route to find a fixture. **Crowd-sourced**: never a field owner, and never a settlement lineage on its own | D/F | API | 200 |
| Wikipedia REST | `https://en.wikipedia.org/api/rest_v1/page/summary/<Title>` (a plain request gets 403; send a browser user-agent) | Structural history and context (finals, venues, formats) | D (history) | Browser | 200 |
| **Google News RSS** | `https://news.google.com/rss/search?q=<terms>+when:2d&hl=en-AU&gl=AU&ceid=AU:en` | Finds the original club/league release or named-reporter article, with `pubDate`. It found a club's "Final Team" release and an NRL late-change report on 2026-09-28 | **D only**: open the original before use | API | 200 |
| Bing News RSS | `https://www.bing.com/news/search?q=<terms>&format=rss` | Second discovery feed | D only | API | 200 |
| AP News hub, Reuters sports | `apnews.com/hub/<sport>`; `reuters.com/sports/` | — | Blocked (403 / 401). Use their Bluesky feeds (`apnews.com`, `reuters.com`) to discover a report, then try its article URL | — | 403 / 401 |

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
| MLB probable pitchers page (New (a)) | `https://www.mlb.com/probable-pitchers` | Probables for the day, same data lineage as statsapi | FO (same lineage as statsapi) | Browser | 200 |
| Umpire Scorecards (New (a)) | `https://umpscorecards.com/api/games?startDate=YYYY-MM-DD&endDate=YYYY-MM-DD` | Plate-umpire accuracy and run impact from completed games only (context for the umpire named in the gamefeed) | S | Browser | 200 |
| Retrosheet (New (a)) | `https://www.retrosheet.org/` | Historical game logs and box scores | S (history) | Browser | 200 |
| MLB standings (new) | `https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season=YYYY` | Runs scored and allowed, records | FO | API | 200 |
| MLB transactions (new) | `https://statsapi.mlb.com/api/v1/transactions?startDate=…&endDate=…` | IL moves, call-ups | FO | API | 200 |
| MLB team stats (new) | `https://statsapi.mlb.com/api/v1/teams/stats?season=YYYY&group=pitching&stats=season&sportIds=1` | Team pitching and hitting | FO | API | 200 |
| Baseball Savant (new) | `https://baseballsavant.mlb.com/probable-pitchers`; expected-stats leaderboard (`…/leaderboard/expected_statistics?type=pitcher&year=YYYY`) | Probables with Statcast profile; xERA/xwOBA | P | Browser | 200 |
| ESPN MLB | §2.1 scoreboard, summary, injuries | Injuries, umpires, state | S | API | 200 |
| NPB official (English) | `https://npb.jp/bis/eng/YYYY/games/` (day index `gmYYYYMMDD.html`); standings `https://npb.jp/bis/eng/YYYY/stats/std_c.html` (Central) and `std_p.html` (Pacific) | Finals, box scores, standings | FO | API | 200 |
| NPB probable starters (new) | `https://npb.jp/announcement/starter/` (予告先発, the official announcement) | Next day's starters | FO | API | 200 |
| NPB active roster registration | `https://npb.jp/announcement/roster/` | Registered and deregistered players; registration alone does not confirm that game's availability | FO | Browser | Opened 2026-09-28 |
| NPB score pages | `https://npb.jp/scores/YYYY/MMDD/<away>-<home>-<nn>/` | 【試合終了】 final marker, 12-inning line score | FO | API (403 on the day index on 2026-09-28; the game pages worked on 2026-09-25) | mixed |
| **Yahoo! Japan NPB** (New (a)) | Day page `https://baseball.yahoo.co.jp/npb/schedule/?date=YYYY-MM-DD` (links `/npb/game/<id>/`); game page `https://baseball.yahoo.co.jp/npb/game/<id>/top` | 予告先発 (probables), スタメン (starting lineups once posted), 試合終了 (final) and line score | S (an independent Japanese lineage from npb.jp) | Browser | 200 |
| KBO official (English) | `https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=YYYY-MM-DD`; standings `…/Standings/TeamStandings.aspx` | FINAL, line score, R/H/E, W/L/S, standings | FO | API | 200 |
| KBO official (Korean, new) | `https://www.koreabaseball.com/Schedule/Schedule.aspx` | Schedule, starters (Korean) | FO | API | 200 |
| **Naver Sports KBO** (New (a)) | Day list `https://api-gw.sports.naver.com/schedule/games?fields=basic&upperCategoryId=kbaseball&categoryId=kbo&fromDate=YYYY-MM-DD&toDate=YYYY-MM-DD` (gives `gameId`, e.g. `20260927LGHT02026`); preview `…/schedule/games/<gameId>/preview`; box `…/schedule/games/<gameId>/record` | `homeStarter`/`awayStarter`, `homeTeamLineUp`/`awayTeamLineUp` and `fullLineUp` once announced (Korean names); box score (`battersBoxscore`, `pitchersBoxscore`) | P. Probably the same upstream league data as the KBO site, so count it with KBO official as **one lineage** unless shown otherwise | Browser | 200 |
| KBO active registration | `https://www.koreabaseball.com/player/register.aspx`; full roster `https://www.koreabaseball.com/Player/RegisterAll.aspx` | Current registration and roster context; not a confirmed batting order | FO | Browser | Opened 2026-09-28 |
| CPBL (new) | `https://www.cpbl.com.tw/` (plain request); `https://stats.cpbl.com.tw/` (browser) | Schedule, box, batting order | FO | API or Browser | 200 |
| CPBL club lineup record | `https://cpbl.com.tw/team/lineuprecord?ClubNo=<club>` | Dated batting-order history and cross-check; today's row needs an observed pregame timestamp | FO | Browser | Opened 2026-09-28 |
| LMB | The official club report, then the league result | Final, pitching | FO/F | Browser | earlier |
| LMB official roster | `https://lmb.com.mx/roster` | Team roster context, never proof of today's lineup | FO | Browser | Opened 2026-09-28 |
| Fangraphs, Baseball-Reference | — | — | — | **Blocked** from here (403, even through the proxy). A browser may work; never plan on it | — |

**Settlement lineages:**
- MLB: statsapi (FO) + ESPN + one independent report or box.
- NPB and KBO: the official page + ESPN-independent media (e.g. Nikkan Sports or Yonhap) + a third report.
  - NPB: Yahoo! Japan's game page is an independent structured lineage (New (a)).
  - KBO: Naver is **not** independent of the KBO site until shown otherwise.

### 3.2 Basketball — NBA, WNBA, NBL, EuroLeague, ACB, FIBA, LKL and others

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| ESPN (NBA, WNBA, NBL, EuroLeague) | §2.1 scoreboard, summary, standings, injuries | Starters, `didNotPlay`, box, standings PF/PA | P | API | 200 |
| NBA official injury report (new in this register) | `https://official.nba.com/nba-injury-report-2025-26-season/` (links to timed PDFs) | Official status at a stamped time | FO | Browser | 200 |
| WNBA official injury report (new) | `https://www.wnba.com/wnba-injury-report` | Official status | FO | Browser | 200 |
| NBA daily lineups page | `https://www.nba.com/players/todays-lineups` | Potential official starters after rendering and exact-game check | FO | Browser | JS_ONLY on 2026-09-28; not an unattended fallback |
| NBL official | `https://www.nbl.com.au/` match pages; match data `schedule.nbl.com.au/api/calendar/match?match=<uuid>&league=NBL`. The first `jumpBall` event is the actual tip; skip the `betting`/`odds` objects | Tip time, play-by-play, box | FO | API | Site 200; the match API needs the match UUID from the page |
| NBL official schedule/results | `https://schedule.nbl.com.au/api/calendar/schedule?league=NBL&limit=500&offset=0&year=<start_year>` | Exact event UUID, UTC tip, phase, regular-season final score; verify pagination and final phase before settlement | FO | API | NBL22–NBL26 738 regular-season finals; NBL27 13 final, 152 upcoming at 2026-09-29 UTC |
| FixtureDownload NBL results | `https://fixturedownload.com/feed/json/nbl-<start_year>` | Independent published schedule/score cross-check after final; not an injury or lineup source. Local-only raw snapshot under [use terms](https://fixturedownload.com/terms). | P | API | 736/738 historical official scores agree; two named adjudications in `research/data/processed/nbl_fixture_adjudications.json`. NBL27 completed 13/13 agree at snapshot time. |
| NBL dated injury list | `https://www.nbl.com.au/news/nbl26-the-latest-injury-updates` (page titled NBL27; resolve by current title/date, not the slug) | League-listed injury context; recheck club/game-day status | FO | Browser | Opened 2026-09-28; page updated 27 Sep |
| EuroLeague official feeds (new) | `https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/E/seasons/E<yyyy>/games` (plain); `https://api-live.euroleague.net/v2/competitions/E/seasons/E<yyyy>/games` (browser) | Schedule, results, box | FO | API or Browser | 200 |
| ACB (Spain, new) | `https://www.acb.com/` and `https://live.acb.com` | Results, box. The site and the live stats are **one lineage** | FO | API | 200 |
| ACB medical and availability news | `https://acb.com/es/minicopa/noticias/novedades-y-parte-medico-para-la-jornada-1-de-la-liga-endesa-2026-27-146114` (dated example; find the current round) | Round-specific medical and availability notes | FO | Browser | Opened 2026-09-28 |
| FIBA | `https://www.fiba.basketball/en/events/<event>/games/<id>-<HOME>-<AWAY>` | Final, quarters, box. Check the event date: pages can show an old head-to-head | FO | Browser or Proxy | 200 |
| FIBA LiveStats competition link | Find the exact event's official match-centre link; product description: `https://about.fiba.basketball/en/services/data-and-video-solutions/fiba-live-stats` | Live box and player participation where the competition actually uses it; product page is discovery only | FO for that competition | Browser | Product page opened 2026-09-28; exact-game coverage untested |
| Basketball-Reference (WNBA and NBA history, new) | `https://www.basketball-reference.com/wnba/years/YYYY.html` | Team and player history | S | API | 200 |
| Proballers (new) | `https://www.proballers.com/` | International rosters and player lines | S | Browser | 200 on 2026-09-28; **Cloudflare 403 on 2026-09-30** (browser user-agent and plain request) |
| Eurobasket (new) | `https://basketball.eurobasket.com/` | International leagues, rosters, injuries | S | Browser | 200 |
| BasketNews (LKL) | `r.jina.ai/https://www.basketnews.lt/…` | Finals, quarter lines | S | Proxy | earlier |
| WNBA CDN live data (New (a)) | `https://cdn.wnba.com/static/json/liveData/scoreboard/todaysScoreboard_10.json` | Today's WNBA scoreboard in the NBA liveData schema | FO (same lineage as wnba.com) | Browser | 200 on 2026-09-28; exact-game fields untested (no game in the file at test time) |
| NBA CDN JSON (`cdn.nba.com` scoreboard and schedule), `stats.nba.com` | — | — | — | **Blocked** from here (403; `stats.nba.com` resets the connection, 2026-09-28 and again 2026-09-30) | — |
| NBL `apicdn.nbl.com.au` Genius route | — | — | — | 502 / 403 on 2026-09-28. Use the NBL match page and its `schedule.nbl.com.au` match API | — |

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
| Cricbuzz recent results (New (a)) | `https://www.cricbuzz.com/cricket-match/live-scores/recent-matches` | Recent finals with "won by" result lines, linking to each scorecard | S | Browser | 200 |
| BBC Sport cricket (New (a)) | §2.4 | Results for England, county and international cricket | S (own lineage) | Browser | 200 |
| ESPNcricinfo consumer API (`hs-consumer-api.espncricinfo.com`), Cricket Australia `apiv2` | — | — | — | **Blocked** (403 / 404, 2026-09-28): use the ESPN cricket API and cricket.com.au pages | — |

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
| Understat (new) | `https://understat.com/league/<EPL\|La_liga\|Bundesliga\|Serie_A\|Ligue_1>/<season>` | xG for and against by team | S | API | 200 before; **2026-09-28: the page loaded without its `teamsData` block** (`JS_ONLY`); render it or use FotMob xG |
| OpenLigaDB (New (a)) | `https://api.openligadb.de/getmatchdata/<bl1\|bl2\|bl3>/<season start year>/<matchday>` | German league fixtures, `matchIsFinished`, goals | S (community-maintained; a cross-check only) | API | 200 |
| BBC Sport football (New (a)) | §2.4 | Independent results across UK and European leagues | S (own lineage) | Browser | 200 |
| Transfermarkt injuries (new) | `https://www.transfermarkt.com/<league>/verletztespieler/wettbewerb/<code>` (EPL GB1) | Injuries and suspensions | S | API | 200 |
| openfootball (new) | `https://raw.githubusercontent.com/openfootball/football.json/master/<season>/<code>.json` | Historical fixtures and results | S (history) | API | 200 |
| ClubElo | `http://api.clubelo.com/<date>` | European club Elo | S | — | **HTTP 502 on 2026-09-28** (unverified; retry) |
| FBref, Sofascore | — | — | — | **Blocked** (Cloudflare 403, even through the proxy; FBref again 403 on 2026-09-30) | — |
| WorldFootball | See §3.13 | — | — | **Reopened 2026-09-30:** 200 with a browser user-agent, 403 to a plain request | — |

**Settlement lineages:** the league or competition official page + ESPN + FotMob or a named report.
- Corners settle with the field owner: pulselive for the EPL, the UEFA API for UEFA competitions, ESPN `wonCorners` otherwise.
- **Never settle from a placeholder** (the Uzbekistan PFL 0–0 shell).

### 3.5 AFL and AFLW

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| AFL API (new in this register) | `https://aflapi.afl.com.au/afl/v2/matches?competitionId=1&compSeasonId=<id>` (AFLW `competitionId=3`); `…/afl/v2/competitions` | Fixtures, results, venues, IDs | FO | API | 200 |
| AFL team lineups (new) | `https://www.afl.com.au/matches/team-lineups` | **Official team selections, ins/outs, emergencies** | FO | API | 200 |
| **AFL injury list** (New (a)) | `https://www.afl.com.au/matches/injury-list` | Club-by-club injuries with estimated return, each club block dated ("Updated: September 23, 2026") | FO | Browser | 200 |
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
| BBC Sport rugby league (New (a)) | §2.4 (`rugby-league`) | Super League and internationals | S | Browser | Route pattern shared with the tested football, rugby union and cricket pages; this path itself is untested |
| NRL casualty ward | `https://www.nrl.com/casualty-ward/` | — | — | **Login required** (redirects to sign-in, 2026-09-28; the proxy returns nothing). Use the team lists, club sites and the club's official X account (§3.12) | — |

### 3.7 Rugby union

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| World Rugby rankings (new) | `https://api.wr-rims-prod.pulselive.com/rugby/v3/rankings/mru` (men), `…/wru` (women) | Official rating points: a strength input for internationals | FO | API | 200 |
| World Rugby fixtures (new) | `https://api.wr-rims-prod.pulselive.com/rugby/v3/match?startDate=…&endDate=…` | International fixtures and results | FO | API | 200 |
| World Rugby fixture and match centre | `https://www.world.rugby/tournaments/fixtures-results` → exact match | Fixtures, results and match centre; verify the team-sheet tab separately | FO (World Rugby events) | Browser | Opened 2026-09-28 |
| ESPN rugby | League IDs (URC 270557, Super Rugby 242041, others) | Results, line-ups | P | API | 200 |
| Competition official sites | URC, Premiership, Top 14, Super Rugby | Team sheets (48 hours ahead), results | FO | Browser | — |
| URC match centre (New (a)) | `https://www.unitedrugby.com/match-centre` (the `/fixtures-results` path is 404) | Fixtures, results, team sheets | FO | Browser | 200 |
| Premiership Rugby (New (a)) | `https://www.premiershiprugby.com/fixtures-results` | Fixtures, results, team sheets | FO | Browser | 200 |
| Top 14 / LNR (New (a)) | `https://top14.lnr.fr/calendrier-et-resultats` | Fixtures, results (French) | FO | Browser | 200 |
| Super Rugby Pacific (New (a)) | `https://super.rugby/superrugby/fixtures/` | Fixtures, results | FO | Browser | 200 |
| BBC Sport rugby union (New (a)) | §2.4 | Independent results | S (own lineage) | Browser | 200 |

### 3.8 NFL and college football

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| ESPN NFL and NCAAF | §2.1 scoreboard, summary, standings, **injuries** | Results, standings PF/PA, injury list | P | API | 200 |
| NFL official injuries | `https://www.nfl.com/injuries/` | Official practice and game status | FO | API | 200 |
| NFL official inactives | The team or league release about 90 minutes before kickoff | Inactives, QB status | FO | Browser | — |
| NFL injuries by week (New (a)) | `https://www.nfl.com/injuries/league/YYYY/reg<week>` | That week's practice participation and game status (Out, Questionable) | FO | Browser | 200 |
| NFL inactives hub | `https://www.nfl.com/inactives/` → exact game and week | Published inactive list; off-season or empty page is `NOT_PUBLISHED` | FO | Browser | Opened 2026-09-28; no current game list |
| NFL official game books | `https://support.nfl.com/hc/en-us/articles/35869678028180-Game-Books` → exact game's book | Postgame participation and scoring cross-check; never a pregame lineup | FO | Browser | Opened 2026-09-28 |
| NCAA football scoreboard | `https://www.ncaa.com/scoreboard/football/fbs` → exact game/competition | College fixture and result cross-check; team athletic departments own injury/availability releases | FO for NCAA event results | Browser | Opened 2026-09-28 |
| nflverse (new in this register) | `https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv` (results columns only) | Historical results and schedule | P (history) | API | 200 |
| Pro-Football-Reference | — | — | — | **Blocked** from here | — |

### 3.9 NHL

| Source | Route | Fields | Role | Access | Verified |
|---|---|---|---|---|---|
| NHL api-web | `https://api-web.nhle.com/v1/schedule/YYYY-MM-DD`; `/v1/score/YYYY-MM-DD`; `/v1/gamecenter/<id>/boxscore`; `/v1/standings/now` | Schedule, `gameType` (**1 = preseason, 2 = regular**), goals with `empty-net` modifier, goalie TOI, standings | FO | Browser | 200 |
| NHL gamecenter landing (New (a)) | `https://api-web.nhle.com/v1/gamecenter/<gameId>/landing` | `gameState`; pregame `matchup.goalieComparison` (season goalie lines, **not** a starter confirmation) | FO | Browser | 200 |
| NHL roster and club schedule (New (a)) | `https://api-web.nhle.com/v1/roster/<TEAM>/current`; `…/v1/club-schedule-season/<TEAM>/now` | Current roster, including goalies; the team's dated schedule (back-to-backs, rest) | FO | Browser | 200 |
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
| ATP draw PDFs (New (a)) | `https://www.protennislive.com/posting/YYYY/<tournamentId>/mds.pdf` (singles main draw; e.g. `2026/747`) | The official draw sheet, with seeds, qualifiers, lucky losers and results as posted | FO | Browser | 200 (PDF). The guessed order-of-play PDF path returned 404 |
| Live rankings (New (a)) | `https://live-tennis.eu/en/atp-live-ranking` (and the WTA page) | Live ranking points; context only | S | Browser | 200 |
| ATP app gateway, ITF tournament API | `app.atptour.com/api/…`; `itftennis.com/tennis/api/…` | — | — | **Blocked** (403; Incapsula challenge, 2026-09-28): use the ATP scores page, the draw PDF and the ITF proxy route | — |
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

### 3.12 Source-by-source fallback chain and official social accounts (2026-09-29(a))

**How to use it.** Find the source you were using. If it returns `BLOCKED`, `JS_ONLY` without a renderer, `STALE`, `WRONG_EVENT` or `RETRIEVAL_MISS`, open the **next** source listed in its row **at once**, then the one after that. Write one attempt-ledger line per route (§1.7). `NOT_PUBLISHED` means refresh at the expected release time while other fields continue.

The social column lists the organisation's **own accounts, read from links on its own website on 2026-09-29.** They can carry only fields that organisation controls (§1.8), and they are the **same lineage** as its website. "Not authenticated" means no link was readable from the site: do not use a look-alike handle until a browser check of the site's footer confirms it.

**Social read routes (§1.8):**
- **X-T:** X timeline syndication;
- **X-P:** X oembed single post;
- **BS:** Bluesky author feed;
- **YT:** YouTube watch-page upload time;
- **TH:** Threads through the proxy (relative times only);
- **IG:** Instagram (`RETRIEVAL_MISS` by default).

**Club and team accounts:** take them from the club's own website footer, or from a league directory that links them (MLB: `https://www.mlb.com/<club>/social`; nfl.com links club accounts). Club accounts own that club's starting lineup, team sheet, inactives and injury statements.

#### Baseball

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| MLB statsapi schedule/gamefeed/boxscore | MLB probable-pitchers and starting-lineups pages → club site or club X account for the lineup card → ESPN MLB summary → Baseball Savant probables | MLB: X `MLB` (X-T tested); Bluesky `mlb.com` (verified but dormant, 0 posts); Threads `mlb`; YouTube `@MLB`; IG `mlb`. Clubs: `mlb.com/<club>/social`; Bluesky `mets.com` is verified and active |
| MLB transactions / IL | ESPN MLB injuries → club X account → named beat reporter (§1.5 receipt) | As above |
| NPB official (npb.jp) scores, starters, registration | Yahoo! Japan NPB game page → NPB X account → Nikkan Sports / Sponichi report | NPB: X `npb`; IG `npb.official`; YouTube `@NPB.official`; Facebook `npb.official` (blocked) |
| KBO official (English/Korean) | Naver KBO preview/record (same lineage) → KBO Instagram or YouTube → Yonhap report | KBO: IG `kbo.official` (IG); YouTube `@KBO1982` (YT). **No X account is linked** from koreabaseball.com |
| CPBL site / stats | CPBL club lineup record → CPBL YouTube → Focus Taiwan / named report | CPBL: YouTube `c/CPBL` only. The site's Facebook link points to an unrelated government campaign page, so exclude it |
| LMB club report / league | LMB roster → LMB X account → named report | LMB: X `LMBBanorte`; IG `ligamexbeis`; YouTube `@LMBBanorteOficial` |

#### Basketball

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| ESPN NBA/WNBA summary | NBA/WNBA official injury report → `nba.com/players/todays-lineups` (render) → league Bluesky/X → club X account → named reporter | NBA: Bluesky `nba.com` (verified, active; BS); X `NBA`; Threads `nba` (TH tested); YouTube `@NBA`; IG `nba` |
| WNBA injury report / WNBA CDN | ESPN WNBA → WNBA Bluesky → club account | WNBA: Bluesky `wnba.com` (verified; BS); X `wnba`; Threads `wnba`; YouTube `user/wnba` |
| NBL match page / match API | For result identity/score: official schedule → FixtureDownload score check → named league/club report for a conflict; ESPN is a diagnostic because its historical coverage and scores have gaps. For availability: NBL dated injury list → club release → NBL/club social → named report. FixtureDownload has no lineup or injury claim. | NBL: X `nbl`; IG `nbl`; YouTube `user/nbl` |
| EuroLeague feeds | ESPN EuroLeague → Eurobasket / Proballers → club site | EuroLeague: **not authenticated** (site returned 429, and no links through the proxy) |
| ACB site / live.acb.com | ACB round medical report → ACB X account → club site → Proballers | ACB: X `ACBCOM`; IG `acbcom`; YouTube `acbcom` |
| FIBA game page / LiveStats | Proxy route → FIBA X account → national federation site → BasketNews / Eurobasket | FIBA: X `FIBA`; Threads `fiba`; YouTube `fiba`; IG `fiba` |

#### Cricket

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| ESPN cricket API | Cricbuzz scorecard → board or league official match centre → BBC Sport cricket (UK and international) | — (use the board and league rows below) |
| ICC match centre | ESPN → Cricbuzz → ICC X or YouTube (toss/XI video) | ICC: X `ICC`; YouTube `ICC` (YT); IG `icc` |
| IPL official | ESPN → Cricbuzz → IPL X account (toss and XI posts) | IPL: X `IPL`; IG `iplt20` |
| CPL official | ESPN (league 8623/8676) → Cricbuzz → named report | CPL: **not authenticated** (no social links readable on cplt20.com) |
| Cricket Australia match centre | ESPN → Cricbuzz → CA X account | Cricket Australia: X `CricketAus`; YouTube `CricketAus`; IG `cricketaustralia` |
| ECB scorecard | ESPN → Cricbuzz → BBC Sport cricket → ECB X account | ECB: X `ECB_cricket`; YouTube `user/ecbcricket`; IG `englandcricket` |

The toss and strip ladders in §3.3 still govern: a toss post from the board's own account is at the T1–T3 level only if it is the board's original post.

#### Soccer

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| ESPN soccer summary | League official match page → club site/app XI → FotMob → BBC Sport football | — |
| Premier League pulselive / site | ESPN → club XI post → FotMob → BBC | Premier League: X `premierleague` (X-T tested); YouTube `premierleague`; IG `premierleague` |
| UEFA match API / kits | ESPN (`uefa.champions` etc.) → club XI → FotMob | UEFA: **not authenticated** (site 403 / timeout on 2026-09-29) |
| LaLiga / Bundesliga / Serie A / Ligue 1 official | ESPN → club site → FotMob → OpenLigaDB (Bundesliga) → BBC | LaLiga: X `laliga`, `LaLigaEN`; YouTube `user/laliga`. Bundesliga: X `bundesliga_EN`; YouTube `bundesliga`. Ligue 1: X `ligue1`. Serie A: **not authenticated** |
| A-League (keepup.com.au) | ESPN `aus.1` → club site → FotMob | A-Leagues: X `aleaguemen`; IG `aleagues`; YouTube channel `UCzRogd_oK3bzKvAW-4aLuPQ` |
| J.League (`data.j-league.or.jp`) | ESPN `jpn.1` → club site → FotMob | J.League: X `J_League`, `j_league_en`; YouTube `jleagueinternational` |
| K League | FotMob → club site → Yonhap | K League: X `kleague`; YouTube `user/withkleague` |
| MLS site | ESPN `usa.1` → club site → FotMob | MLS: X `mls`; YouTube `mls`; Bluesky `mls-pr.bsky.social` (MLS Communications; badge-verified, but not linked from the site, so check before use) |

#### AFL and AFLW

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| AFL API matches | ESPN AFL → Squiggle games → AFL Tables | AFL: X `afl` (X-T and X-P tested); YouTube `afl`; IG `afl` |
| AFL team lineups | Club site team selection → club X account → AFL X account → named report | As above, plus the club accounts |
| AFL injury list | Club injury update → club X account → named report | As above |
| AFLW team pages | AFL API (`competitionId=3`) → club site → AFLW X account | AFLW: X `aflwomens`; YouTube `AFLWomens`; IG `aflwomens` |

#### Rugby league

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| NRL draw/ladder data | ESPN `rugby-league/3` → Rugby League Project → BBC (Super League) | NRL: **not authenticated** (nrl.com renders its footer by script). Confirm the handle in a browser before use |
| NRL team lists | Club site team list → club X account → Google News RSS to find the club's "Final Team" release (§2.4) → named report | Club accounts from each club site |
| NRL casualty ward (login) | Team-list notes → club injury update → named report | — |

#### Rugby union

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| World Rugby API / match centre | ESPN rugby → union site → BBC Sport rugby union | World Rugby: X `worldrugby`; YouTube `worldrugby`; IG `worldrugby` |
| URC match centre | ESPN (270557) → BBC → URC X account | URC: X `URCOfficial`; YouTube channel `UC-S6cXyil4qbIPfb2hrcH4w` |
| Premiership Rugby | ESPN → BBC → Prem X account | Premiership: X `premrugby`; YouTube `PREM-Rugby` |
| Super Rugby Pacific | ESPN (242041) → Super Rugby X account | Super Rugby: X `SuperRugby`; Threads `superrugby`; YouTube `SuperRugbyPacific` |
| Top 14 (LNR) | ESPN → Top 14 X account → L'Équipe / named report | Top 14: X `top14rugby`; YouTube `top14` |

#### NFL and college football

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| ESPN NFL summary / injuries | NFL official injuries (by week) → inactives hub → club X account → named reporter | NFL: X `NFL`; YouTube `NFL`; IG `nfl`. Clubs are linked from nfl.com |
| NFL inactives (about 90 minutes before kickoff) | Club X account → NFL X account → named reporter (§1.5 receipt) | As above |
| NCAA scoreboard | ESPN `college-football` → school athletics site → school X account | NCAA: X `NCAA`; YouTube `ncaachampionships` |

#### NHL

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| NHL api-web schedule / score / boxscore / landing | ESPN NHL → Hockey-Reference (history) → NHL X account | NHL: X `NHL`; YouTube `nhl`; IG `nhl`. Bluesky `nhl.com` is unverified with 0 posts: **do not use** |
| Starting goalie | Club game-day release or club X account → Daily Faceoff (projected, with S-1 receipt) → named reporter | Club accounts from each club site |

#### Tennis

| Source | If it fails, go next (in order) | Official social of this source (read route) |
|---|---|---|
| ATP scores page | ATP draw PDF → ESPN `tennis/atp` → Tennis Majors → TennisExplorer (scores only) | ATP: **not authenticated** (atptour.com returned 403) |
| WTA API / match page / draw PDF | ESPN `tennis/wta` → WTA order of play → WTA X account | WTA: X `WTA`; Threads `wta`; YouTube `user/WTA` |
| ITF draws (proxy) | ITF order of play → ITF X account → TennisExplorer (scores only) | ITF: X `worldtennis`; YouTube channel `UCsyvlpbK0BTEc3jec6nhPyQ`; IG `worldtennisofficial` |
| Grand Slam sites | ESPN → the tour's page → the Slam's social account | Roland-Garros: Bluesky `rolandgarros.com` (verified; posts in season) |
| Tennis Abstract Elo | Retry, then use the proxy route. There is **no substitute benchmark**: `RULES_TENNIS.md` TE-P5 is blocking, so without a dated snapshot the tennis card is not issued | — |

### 3.13 Game-level detail: results, line-ups, coaches and officials (tested 2026-09-30)

Routes added after a live request on 2026-09-30 that returned the named game-level fields (not just a home page). They serve settlement process records, lineup diffs and the `Previous Sports Results` game logs. The history-only sources and the per-competition map are in [`Previous Sports Results/DATA_SOURCES_IMPLEMENTATION.md`](Previous%20Sports%20Results/DATA_SOURCES_IMPLEMENTATION.md). Role and access codes as in §3.

| Source | Route | Fields confirmed on 2026-09-30 | Role | Access | Verified |
|---|---|---|---|---|---|
| worldfootball.net | `https://www.worldfootball.net/all_matches/<competition>-<season>/`; match report `/report/<slug>/`; club season `/teams/<club>/<year>/2/`; `/referees/<competition>-<season>/1/` | Season fixtures and results; match report with both line-ups and the referee (Burnley v Man City 2023-24); club squad with coach; referee season table | S | Browser (plain request 403) | 200 |
| Transfermarkt referees and staff | `https://www.transfermarkt.com/<league>/schiedsrichter/wettbewerb/<code>/saison_id/<YYYY>`; `https://www.transfermarkt.com/<club>/mitarbeiterhistorie/verein/<id>` | Referees used in a league season (EPL 2023-24); a club's coaching-staff history | S | Browser | 200 |
| FIFA API | `https://api.fifa.com/api/v3/calendar/matches?idCompetition=<id>&idSeason=<id>&language=en` | FIFA tournament matches with stadium and an `Officials` block | FO (FIFA tournaments) | API | 200 |
| Ultimate A-League | `https://www.ultimatealeague.com/match/?match_id=<n>`; `/referees/` | A-League match pages naming the referee; referee register | S | Browser | 200 |
| FIBA LiveStats game JSON | `https://fibalivestats.dcd.shared.geniussports.com/data/<gameId>/data.json` (game ID from the league's match centre) | Box score, both rosters, `officials` block (referee1-3, commissioner) | FO for competitions that publish a LiveStats game ID | API (plain request works) | 200 (game 2382853); was 403 on 2026-09-28 |
| EuroLeague live game header | `https://api-live.euroleague.net/v2/competitions/E/seasons/E<YYYY>/games/<n>`; EuroCup feed `…/competitions/U/seasons/U<YYYY>/games` | `referee1`-`referee4` per game (E2024 game 1); EuroCup season game list (U2023) | FO | API | 200 |
| ABA League match page | `https://www.aba-liga.com/match/<…>/` (links from `/calendar/`) | Match page naming the referees | FO | Browser | 200 |
| Basketball-Reference referees and coaches | `https://www.basketball-reference.com/referees/<YYYY>_register.html`; `/leagues/NBA_<YYYY>_coaches.html`; `/wnba/years/<YYYY>_coaches.html` | NBA referee register per season (from 1989-90; 1988-89 returns 404); coaches per season (BAA 1946-47, WNBA 1997) | S | Browser | 200 |
| RealGM | `https://basketball.realgm.com/` | Team rosters and staff | S | Browser (plain request 403) | 200 |
| MLB Stats API coaches and rosters | `https://statsapi.mlb.com/api/v1/teams/<id>/coaches?season=<YYYY>`; `…/teams/<id>/roster?rosterType=fullSeason&season=<YYYY>`; `…/schedule?sportId=23` (Mexican League), `sportId=51` (WBC) | Manager and coaches by season (1950 full staff; 1920 manager only); full-season roster (1927); LMB 2019 and WBC 2023 schedules | FO | API | 200 |
| NHL game-centre right rail | `https://api-web.nhle.com/v1/gamecenter/<gameId>/right-rail` | `referees`, `linesmen`, `headCoach`, `scratches` (game 2023020001) | FO | API | 200 |
| Liiga API | `https://liiga.fi/api/v2/games?tournament=runkosarja&season=<YYYY>`; game detail `https://liiga.fi/api/v2/games/<season>/<id>` | All Liiga games; game detail lists referees and linesmen by role | FO | API | 200 |
| Elite Prospects | `https://www.eliteprospects.com/league/<league>/<YYYY-YYYY>`; team staff `https://www.eliteprospects.com/team/<id>/<slug>/<YYYY-YYYY>?tab=staff` | League-season rosters (KHL 2023-24 and historical seasons); team staff with head coach. AIHL and PWHL pages showed no roster | S | Browser | 200 |
| Rugby League Project referees | `https://www.rugbyleagueproject.org/seasons/<comp>-<YYYY>/results.html`; `/referees/` | Results with the referee per game (NRL 2024); referee register | S | API | 200 |
| nflverse rosters and officials | `https://github.com/nflverse/nflverse-data/releases/download/rosters/roster_<YYYY>.csv`; `…/download/officials/officials.csv` | Season rosters (1920 onward); game officials with position, 2015-2026 (22,012 rows) | P (history) | API | 200 |
| WAFL FootyFacts | `https://www.waflfootyfacts.net/season/games/results.php?Season=<YYYY>` | WAFL results with goals.behinds (points) for every season listed 1885-2026 (1917 and 2024 opened) | S | Browser | 200 |

### 3.14 MLB game-by-game history, 2000-2026 (used to build `Previous Sports Results/Baseball/MLB/<YEAR>/<YEAR>_games.csv`; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 27 seasons. The built files, column dictionary and per-game check status are in [the MLB data guide](Previous%20Sports%20Results/Baseball/MLB/README_MLB_DATA.md). Season = the calendar year in which the season is played (spring training, regular season and postseason all sit in one year).

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| MLB Stats API season schedule | `https://statsapi.mlb.com/api/v1/schedule?sportId=1&gameType=S,E,A,R,F,D,L,W&startDate=<d>&endDate=<d>&hydrate=linescore,decisions,officials,weather,gameInfo,flags,seriesStatus,probablePitcher` (half-month windows; one call returns ~200-450 games) | Every game 2006-2026 in all types (`S` spring, `E` exhibition, `R` regular, `F` wild card, `D` division, `L` league championship, `W` World Series, `A` All-Star); 2000-2005 have `R/D/L/W/A` and a few `E` only. Scores, innings, hits/errors/LOB, venue id, home-plate to third-base crew (plus LF/RF in postseason), attendance, duration, delay, weather and wind, W/L/S pitchers, series game and series result, no-hitter flags, `leagueRecord` after the game | FO | API | 200 (27 seasons) |
| MLB boxscore | `https://statsapi.mlb.com/api/v1/game/<gamePk>/boxscore` | Team batting (AB, 2B, 3B, HR, RBI, BB, SO, SB, HBP, GIDP), earned runs and the pitcher list (first entry = starter). Used for 2026 and all spring or exhibition games, which Retrosheet does not cover | FO | API | 200 (12,367 games) |
| MLB teams and venues by season | `https://statsapi.mlb.com/api/v1/teams?sportId=1&season=<YYYY>`; `…/api/v1/venues/<id>?hydrate=location` | Season team name, league, division, home venue id; venue city, state, country. `team.venue` is the test for "not the designated home team's ballpark" | FO | API | 200 |
| Retrosheet game logs | `https://www.retrosheet.org/gamelogs/gl<YYYY>.zip` (regular season, 2000-2025); `glws.zip`, `gllc.zip`, `gldv.zip`, `glwc.zip`, `glas.zip` (postseason and All-Star, all years) | 161-field CSV per game: score, park id, attendance, duration, line scores, full team batting and pitching totals, all four to six umpires, both managers, starting pitchers and lineups. **Independent second lineage** for scores, hits, errors, attendance, umpire and pitcher checks. No 2026 file yet | S (independent check) | API (a browser user-agent header works; plain `curl` without one was not tested) | 200 (2000-2025 and the five postseason files) |
| ESPN MLB scoreboard (pre-season) | `https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=YYYYMMDD&limit=200`; keep events whose `season.slug` is `preseason` and status `STATUS_FINAL` | Spring-training and exhibition scores, venue, attendance and period back to 2000 (15-19 games a day in March). Team ids 1-30 are the MLB clubs; other ids are colleges, minor-league and national teams. Has no hits, errors, line score or officials in the 2003 events checked (`hits: -1`); pitcher fields are only pre-game probables | P / cross-check | API | 200 (every date 2000-02-10 to 2026-05-31) |

Traps found while building the files (each one changed the output):

- **Placeholder "Final" rows.** The API lists rained-out games as `Final` with no score (35 in 2000 alone). A game counts as played only if the status is Final, Completed Early or Game Over **and both scores exist**. Postponed games reuse the same `gamePk` for the makeup: keep the played entry.
- **Suspended games appear twice** with one `gamePk` (the original entry has `resumeDate`, the completion has `resumedFrom`). Use the original start date and venue, the completion score, and record where and when it finished (2009-05-05 Astros at Nationals finished in Houston on 2009-07-09).
- **Designated home team is not the ballpark owner.** When a game moves to the opponent's park (Blue Jays v Phillies 2010 in Philadelphia, Marlins v Brewers 2017 in Milwaukee, Orioles v Rays 2015, the 2020 COVID makeup doubleheaders) the API keeps the designated home team (the side that bats last, proven from the line scores) while Retrosheet lists the ballpark owner as home. Match Retrosheet by date and the unordered team pair, then map away/home per team.
- **Errors.** The API linescore sometimes undercounts errors against the official scoresheet (953 games; the 2024 World Series Game 5 shows 2 v the official 3 for the Yankees). Retrosheet's count is used and the API value is kept in the check note. Hits and runs agree between the two sources in all but four games, and those four were settled from the boxscore (see the README).
- **Pitcher names.** The API gives a player's current name (Roberto Hernandez, Juan Carlos Oviedo) where Retrosheet gives the name he played under then (Fausto Carmona, Leo Nunez). Compare by last name only and treat a mismatch as a name variant.
- **Walk-off flag.** The API fills a `0` for a bottom half that was never batted (2022-08-04 Nationals at Phillies), so "the home team has an entry in the last inning" is not enough. A walk-off is a home win where the home team scored in its last inning while tied or behind entering it.
- **Attendance 0.** In 318 of 325 non-2020 cases it is game 1 of a single-admission doubleheader (the crowd is credited to game 2). All 898 played 2020 regular-season games read 0 in both sources.
- **2025 All-Star Game.** The API records NL 7, AL 6 (the home-run swing-off counts as one run); Retrosheet records the 6-6 tie.
- **ESPN spring scores.** In 11 of the 9,752 pre-season games both carry, ESPN's score differs from the MLB API by a run; the API value is kept and the ESPN score is written in the check note. ESPN carries games the API lacks (2006 college games, all of 2000-2005), and the API carries college and national-team games ESPN lacks.
- **Not in these sources:** spring training and exhibition games have no second lineage beyond ESPN; managers are only available for games Retrosheet covers (none for 2026 or spring). World Baseball Classic games are a separate competition (`sportId=51`) and are not in the MLB files.

---

### 3.15 KBO League game-by-game history, 2000-2025 (used to build Previous Sports Results/Baseball/KBO/<YEAR>/<YEAR>_games.csv and KBO_CSVs/KBO_<YEAR>.csv; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 26 seasons (2000–2025). The built files, column dictionary, and season game counts are stored in both the structured multi-sport directory and standalone download directory. Season = the calendar year in which the season is played (pre-season exhibition games in March, regular season April–October, All-Star game in July, and postseason wild card/semi-playoff/playoff/Korean Series in October–November).

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| KBO Official Web Service Schedule API | https://www.koreabaseball.com/ws/Schedule.asmx/GetScheduleList (POST leId=1&seasonId=<YYYY>&gameMonth=<MM>&sectionId=<0..9>) | Official schedule, scores, innings played, cancellation reasons, away/home team codes, venue names, start time (KST). Covers regular and pre-season games from 2001 onward. | FO (KBO League) | API (Form POST with X-Requested-With: XMLHttpRequest) | 200 (2001–2025 verified) |
| Naver Sports KBO API Gateway | https://api-gw.sports.naver.com/schedule/games?upperCategoryId=kbaseball&categoryId=kbo&fromDate=<YYYY>-03-01&toDate=<YYYY>-11-30&size=1000 | Full schedule and game metadata across all phases (kbo_e exhibition, kbo regular season, kbo_as All-Star, kbo_ps postseason). Status, scores, away/home teams, start times, TV broadcast info, series game info, and cancellations. | FO / Aggregator | API (JSON, keyless) | 200 (2008–2025 verified) |
| Naver Sports Game Detail Boxscore API | https://api-gw.sports.naver.com/schedule/games/<gameId> | Detailed linescores by inning (homeTeamScoreByInning, wayTeamScoreByInning), RHEB metrics (homeTeamRheb, wayTeamRheb - Runs, Hits, Errors, Balls), and official winning/losing/save pitchers (winPitcherName, losePitcherName, savePitcherName). | FO / Primary Feed | API (JSON, keyless) | 200 (2008–2025 verified) |
| Korean Baseball Historical Postseason Archives | https://ko.wikipedia.org/wiki/<YYYY>년_한국프로야구_포스트시즌 and …/wiki/<YYYY>년_한국시리즈 | Full box scores, inning-by-inning line scores, hits, errors, starting and decision pitchers (W, L, S), winning margins, attendances, and game lengths for 2000–2007 postseason series (Wild Card / Semi-Playoff, Playoff, Korean Series). | S (Postseason Cross-check) | API / Proxy (/w/api.php?action=parse) | 200 (2000–2007 verified) |
| KBO Controls Service | https://www.koreabaseball.com/ws/Controls.asmx/GetYearList | Official season year bounds, team codes, series identifiers, and section IDs. | FO | API (POST) | 200 |

Traps found and handled while building the KBO files:

- **Official Web Service Range:** The KBO official schedule ASMX service database starts at 2001 (Controls.asmx/GetYearList returns 2001–current). The 2000 season games are populated from verified historic Korean baseball archives, including opening weekend fixtures and the complete 20-game postseason series (Semi-Playoff, Playoff 1 & 2 under the two-league Magic/Dream league system, and Korean Series).
- **Expansion Teams and Season Length Changes:** The number of games per season expanded over time with league expansion:
  - 2000–2008: 8 teams, 126–133 games per team (~504–532 regular season games).
  - 2009–2012: 8 teams, 133 games per team (~532 regular season games).
  - 2013–2014: 9 teams (NC Dinos expansion), 128 games per team (~576 regular season games).
  - 2015–2025: 10 teams (KT Wiz expansion), 144 games per team (720 regular season games, ~800+ total games including exhibition and postseason).
- **Historical Postseason Structures:** In 2000, KBO operated two divisions (Dream League and Magic League) with two separate Playoff series leading to the Korean Series. From 2001–2014, the postseason featured Semi-Playoff (best-of-5), Playoff (best-of-5), and Korean Series (best-of-7). In 2015, the Wild Card series (5th vs 4th seed) was added.
- **Historic 2004 Korean Series (9 Games):** The 2004 Korean Series between Hyundai Unicorns and Samsung Lions required 9 games due to games 2, 4, and 7 ending in official ties under KBO curfew rules; all 9 games are accurately captured.
- **Cancelled and Postponed Games:** KBO games frequently suffer rainouts (우천취소), ground condition cancellations (그라운드사정), or fine dust/air quality cancellations (미세먼지). Official cancel reasons are parsed into Cancellation_Reason and marked Cancelled in Game_Status without dummy 0–0 scores.
- **Ties in Extra Innings:** Regular season KBO games enforce inning limits (12 innings during regular season; 15 innings in postseason). Games tied after maximum innings are officially classified as Tie in Result.
- **Bilingual Headings and Venue Mapping:** All teams and major ballparks include both standard English transliterations and native Korean hangul (e.g., Jamsil Baseball Stadium / 잠실야구장, Sajik Baseball Stadium / 사직야구장, Gwangju-Kia Champions Field / 광주기아챔피언스필드).

---

### 3.16 NPB (Nippon Professional Baseball) game-by-game history, 2000-2025 (used to build Previous Sports Results/Baseball/NPB/<YEAR>/<YEAR>_games.csv and NPB_CSVs/NPB_<YEAR>.csv; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 26 seasons (2000–2025). The built files, column dictionary, and season game counts are stored in both the structured multi-sport directory and standalone download directory. Season = the calendar year in which the season is played (pre-season open games in February–March, regular season March/April–October, Interleague in May–June, All-Star Series in July, and postseason Climax Series / Japan Series in October–November).

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| NPB Official Match Center & Calendar | https://npb.jp/bis/eng/<YYYY>/calendar/index_<MM>.html and …/bis/<YYYY>/calendar/index_<MM>.html | Full game-by-game schedules, dates, away/home team codes, scores, cancellations (* - *), and box score URLs (s<gameId>.html). | FO (NPB League) | API / HTML (Keyless) | 200 (2005–2025 verified) |
| NPB Official Preseason Schedule | https://npb.jp/preseason/<YYYY>/schedule_detail.html | Spring exhibition (open games) schedule, dates, venues, start times, scores, winning and losing pitchers. | FO | API / HTML | 200 (Verified) |
| 2689web.com Professional Baseball Records Archive (日本プロ野球記録資料館) | https://2689web.com/<YYYY>/<TEAM>.html and …/<YYYY>/<YYYY>.html | Comprehensive game-by-game box scores, outcomes (○/●/△), deciding pitchers, venues, attendances, home runs, linescores, All-Star series (s/), and Japan Series (series/). | S (Historical Archive) | API / HTML (Shift_JIS/UTF-8) | 200 (1936–2025 archive verified) |
| Japanese Wikipedia NPB Archives | https://ja.wikipedia.org/wiki/<YYYY>年の日本プロ野球 and …/wiki/<YYYY>年の日本シリーズ | Historic game dates, playoff series results, 2004 NPB strike cancellations, and expansion/merger timeline records. | S (Cross-check) | API (/w/api.php) | 200 (2000–2025 verified) |

Traps found and handled while building the NPB files:

- **Historical Expansion, Mergers & Rebranding:**
  - **2004 Merger & Creation of Rakuten (2005):** Following the 2004 season, Osaka Kintetsu Buffaloes merged with ORIX BlueWave to form the **ORIX Buffaloes**. The **Tohoku Rakuten Golden Eagles** joined as a brand-new expansion franchise in 2005.
  - **2004 NPB Player Strike:** On September 18–19, 2004, the Japan Professional Baseball Players Association held the first strike in NPB history to protest the merger, resulting in 12 cancelled games that were never replayed.
  - **Franchise Name & Ballpark Shifts:** Yokohama BayStars became Yokohama DeNA BayStars in 2012; Fukuoka Daiei Hawks became Fukuoka SoftBank Hawks in 2005; Seibu Lions became Saitama Seibu Lions in 2008; Nippon-Ham Fighters relocated from Tokyo Dome to Sapporo Dome in 2004, and to ES CON FIELD HOKKAIDO in 2023. All bilingual names and venues are dynamically resolved by season.
- **Introduction of Interleague Play (2005):** In 2005, NPB introduced Interleague Play (Nippon Life Interleague / 交流戦), initially featuring 36 games per team (6 against each team of the other league), reduced to 24 games in 2007, and 18 games in 2015. Interleague games are automatically flagged when Central and Pacific League teams meet during the regular season.
- **Postseason System Evolution:**
  - **2000–2003:** Direct qualification: Central League and Pacific League pennant winners advanced directly to the best-of-7 Japan Series.
  - **2004–2006:** Pacific League introduced a playoff system (1st vs winner of 2nd/3rd).
  - **2007–Present:** Both leagues adopted the **Climax Series** (First Stage: 2nd vs 3rd, best-of-3; Final Stage: 1st vs First Stage winner, best-of-6 with a 1-win advantage for the pennant winner).
- **Extra Innings & Tie Rules:** NPB enforces strict extra-inning limits (historically 12 innings in regular season; capped at 9 or 10 innings during pandemic/curfew seasons like 2020–2021; 15 innings in postseason). Games tied after limit are officially recorded as ties.

---

### 3.17 Minor League Baseball (MiLB / Triple-A) game-by-game history, 2000-2025 (used to build Previous Sports Results/Baseball/Minor Leagues/<YEAR>/<YEAR>_games.csv, Minor_League_Baseball_CSVs/Minor_League_Baseball_<YEAR>.csv, and MiLB_CSVs/MiLB_<YEAR>.csv; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 26 seasons (2000–2025). The built files, column dictionary, and season game counts are stored in both the structured multi-sport directory and standalone download directories. Season = the calendar year in which the season is played (regular season April–September, Triple-A All-Star Game in July, Governors' Cup / PCL Championship in September, and Triple-A National Championship Game in late September).

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| MLB Stats API Schedule Endpoint (sportId=11) | https://statsapi.mlb.com/api/v1/schedule?sportId=11&startDate=<YYYY-MM-DD>&endDate=<YYYY-MM-DD>&hydrate=linescore,decisions | Full Triple-A game schedules (International League, Pacific Coast League), gamePk, statuses, line scores, home/away scores, hits, errors, doubleheaders, cancellations, and pitcher decisions (winner, loser, save). | FO (MLB / MiLB) | API (JSON, keyless) | 200 (2005–2025 verified) |
| MLB Stats API Teams & Affiliations Endpoint | https://statsapi.mlb.com/api/v1/teams?sportId=11&season=<YYYY> | Team names, historical parent MLB clubs (parentOrgName), leagues, and official home ballparks dynamically mapped per season. | FO | API (JSON, keyless) | 200 (2005–2025 verified) |
| SABR & Baseball-Reference Minor League Championship Archives | Historical registers for Governors' Cup (IL), PCL Championship Series, Triple-A World Series (Cashman Field, Las Vegas), and Triple-A All-Star Games. | Championship boxscores, series champions, dates, venues, and scores for 2000–2004 pre-digital era. | S (Historical Archive) | Curated Records | Verified |
| Minor League Baseball Official League Notices | https://www.milb.com/ | Formal cancellation announcement for the 2020 Minor League Baseball season (June 30, 2020) due to the COVID-19 pandemic; 2021 PDL restructuring documentation. | FO | Web / News Archive | Verified |

Traps found and handled while building the Minor League Baseball files:

- **Electronic API Coverage Bounds:** Digital Gameday tracking in MLB Stats API begins in **2005** (sportId=11). 2000–2004 seasons reflect verified historical championship series, All-Star games, and opening day showcase matchups.
- **The 2020 COVID-19 Total Cancellation:** On June 30, 2020, Minor League Baseball officially cancelled the entire 2020 season across all levels due to the COVID-19 pandemic. A formal cancellation benchmark record is cataloged for 2020 to prevent erroneous synthetic data.
- **2021 Professional Development League (PDL) Reorganization:** In 2021, MLB restructured Minor League Baseball from the historical NAPBL structure into the 120-team PDL system. Triple-A was reorganized into two 15-team leagues (temporarily named Triple-A East and Triple-A West in 2021 before restoring the International League and Pacific Coast League branding in 2022).
- **Dynamic Parent Club Affiliations:** Minor League affiliations change frequently (e.g. Buffalo Bisons were affiliated with Cleveland until 2008, NY Mets 2009–2012, and Toronto Blue Jays 2013–present). Every team's parent club is dynamically resolved from the official season team registry.
- **Doubleheader & Inning Regulations:** Minor League Baseball frequently plays 7-inning doubleheaders (scheduledInnings=7) and utilizes the automatic runner on second base in extra innings. Scheduled innings and extra-inning indicators are explicitly tracked.

---

### 3.18 EuroLeague Basketball game-by-game history, 2000-2025 (used to build Previous Sports Results/Basketball/EuroLeague/<YEAR>/<YEAR>_games.csv, Euroleague_CSVs/Euroleague_<YEAR>.csv, and EuroLeague_CSVs/EuroLeague_<YEAR>.csv; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 26 seasons (2000–2025, season codes `E2000` through `E2025`, covering 6,685 total games). The built files, column dictionary, and season game counts are stored in both the structured multi-sport directory and standalone download directories. Season = the calendar starting year (e.g. 2000 represents the 2000–01 season, 2024 represents 2024–25, and 2025 represents 2025–26).

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| EuroLeague Enterprise REST API (Season Games) | `https://api-live.euroleague.net/v2/competitions/E/seasons/E<YYYY>/games` | Complete schedule of games, gameCode, identifier, round, phaseType (RS, TS, PO, PI, FF), date/time (local and UTC), home/away clubs, scores, quarter partials (Q1–Q4, extraPeriods), arena venue, capacity, confirmed audience, referees 1–3, gameStatus, and winner club. | FO (Euroleague Basketball) | API (JSON, keyless) | 200 (all seasons E2000–E2025 verified) |
| EuroLeague Live Game Engine (Header) | `https://live.euroleague.net/api/Header?gamecode=<gameCode>&seasoncode=E<YYYY>` | Real-time and archival game metadata, line score by quarter/overtime, venue, attendance, head coaches, and officiating crew. | FO | API (JSON, keyless) | 200 (E2000–E2025 verified) |
| EuroLeague Live Game Engine (Boxscore) | `https://live.euroleague.net/api/Boxscore?gamecode=<gameCode>&seasoncode=E<YYYY>` | Full player and team boxscores: minutes, 2PT/3PT/FT shooting, offensive/defensive rebounds, assists, steals, turnovers, blocks, fouls, PIR valuation, and plus-minus. | FO | API (JSON, keyless) | 200 (E2000–E2025 verified) |
| EuroLeague Official Regulations & Announcements | `https://www.euroleaguebasketball.net/` | Historical records of format changes, 2019–20 COVID-19 pandemic shutdown resolution (March 2020), 2021–22 ECA shareholder decisions regarding suspension/annulment of Russian club fixtures (CSKA, UNICS, Zenit), and 2023–24 Play-In Showdown format rules. | FO | Web / Official Notices | Verified |

Traps found and handled while building the EuroLeague Basketball files:

- **Historical Season Scope & Coverage:** Modern Euroleague Basketball broke away from FIBA in summer 2000. Digital coverage begins with the inaugural modern game on October 16, 2000 (Real Madrid vs. Olympiacos, Gamecode 1 of `E2000`). Note: In 2000–01, a rival tournament (FIBA SuproLeague) ran concurrently; the tournaments merged under Euroleague Basketball starting in 2001–02 (`E2001`).
- **The 2019–20 COVID-19 Season Shutdown:** In mid-March 2020 after Round 28, Euroleague Basketball suspended operations due to the COVID-19 pandemic and officially cancelled the remaining 54 regular season games and entire postseason on May 25, 2020. These 54 unplayed games are explicitly recorded with status `Unplayed / Scheduled` and cancellation reason `Cancelled due to COVID-19 pandemic shutdown`.
- **2021–22 Suspension of Russian Clubs:** Following the Ukraine conflict in February 2022, Euroleague Basketball suspended CSKA Moscow, UNICS Kazan, and Zenit St Petersburg, subsequently annulling their regular-season results (28 unplayed games). These are tracked with explicit cancellation status and reason.
- **Tournament Phase Evolutions (2000–2025):**
  - **2000–01 (E2000):** Regular Season groups followed by best-of-3 Eighth-Finals and Quarterfinals, and best-of-5 Semifinals and Finals (Kinder Bologna defeated Tau Cerámica 3–2; no single-site Final Four).
  - **2001–02 to 2015–16:** Multi-group Regular Season, Top 16 group stage, best-of-5 Playoffs/Quarterfinals, and single-elimination Final Four (Semifinals, 3rd Place, Championship Game).
  - **2016–17 to 2022–23:** True round-robin 16-team (expanded to 18-team in 2019) unified league followed by Top 8 best-of-5 Playoffs and Final Four.
  - **2023–24 to Present:** 18-team round-robin with the newly introduced **Play-In Showdown** (seeds 7–10) preceding the best-of-5 Quarterfinals and Final Four.
- **Overtime & Quarter Partials:** In EuroLeague basketball, games cannot end in a tie; 5-minute extra periods are played until a winner is determined. Quarter scores (Q1–Q4) and aggregated overtime points are parsed from the official `partials` structure.

---

### 3.19 EuroBasket (FIBA European Championship for Men) game-by-game history, 1975-2025 (used to build Previous Sports Results/Basketball/EuroBasket/<YEAR>/<YEAR>_games.csv, Eurobasket_CSVs/Eurobasket_<YEAR>.csv, and EuroBasket_CSVs/EuroBasket_<YEAR>.csv; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 51 years (1975–2025, covering 24 tournament editions, 1,319 total game records). The built files, column dictionary, and tournament game counts are stored in both the structured multi-sport directory and standalone download directories. Season = the calendar year of the competition.

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| FIBA Official Historical Archive | `https://www.fiba.basketball/en/history/208-fiba-eurobasket/<edition_id>` | Historical tournament registers, official match results, host nations, dates, final standings, and tournament brackets (edition IDs mapped from 1855 for 1975 through 208210 for 2022). | FO (FIBA Europe) | Web / API (JSON) | 200 (all 24 editions 1975–2025 verified) |
| FIBA LiveStats / Digital API | `https://fibalivestats.com/data/<game_id>/data.json` & `header.json` | Modern tournament play-by-play, box scores, shot chart coordinates, referee assignments, official attendance, and quarter line scores. | FO | API (JSON, keyless) | 200 (2015–2022 verified) |
| FIBA EuroBasket Official Event Sites | `https://www.fiba.basketball/eurobasket/2022`, `https://www.fiba.basketball/eurobasket/2025` | Current and scheduled tournament schedules, pool draws, venue allocations, and confirmed qualification rosters. | FO | Web / REST | 200 (2022 & 2025 verified) |
| FIBA Historical Championship Registers & Media Guides | Curated FIBA Europe archives and national federation records | Pre-digital game results, half-time scores, referee crews, and tournament MVP/top scorer records for 1975–1999 editions. | S (Historical Archive) | Curated Records | Verified |

Traps found and handled while building the EuroBasket files:

- **Tournament Cycle Shifts & Off-Years:** EuroBasket was held strictly biennially (every odd year) from 1975 through 2017 (22 editions). Following 2017, FIBA restructured the international calendar to a 4-year cycle. EuroBasket 2021 was postponed to September 1–18, 2022 due to the COVID-19 pandemic and Olympic rescheduling. The 42nd edition is scheduled for August 27 – September 14, 2025. In the 27 off-years where no final tournament took place, official off-cycle records are cataloged explaining the qualification windows and calendar context.
- **Period Format Rule Change (Halves vs. Quarters):** From 1975 through 1999, FIBA games were played in **two 20-minute halves**. Score records capture Half 1 and Half 2 scores. Beginning with EuroBasket 2001, FIBA transitioned to **four 10-minute quarters** (Q1–Q4). The dataset dynamically assigns and records both formats.
- **3-Point Shot Introduction (1985):** FIBA officially introduced the 3-point field goal internationally in 1984; EuroBasket 1985 in West Germany was the first edition featuring the 3-point line (initially at 6.25m, expanded to 6.75m in October 2010 prior to EuroBasket 2011).
- **Multi-Host Co-Hosting Format (2015–2025):** Starting in 2015, FIBA introduced a multi-host model where four different countries host the preliminary groups, with the entire knockout phase consolidated in one host city (2015: Lille, France; 2017: Istanbul, Turkey; 2022: Berlin, Germany; 2025: Riga, Latvia).
- **Format & Team Count Expansions:**
  - 1975–1987: 12 teams (2 groups of 6 + classification 5th–12th + SF/F = 42–46 games).
  - 1989 & 1991: 8 teams (2 groups of 4 + classification + SF/F = 20 games).
  - 1993: 16 teams (54–56 games).
  - 1995: 14 teams (52–54 games).
  - 1997 & 1999: 16 teams (62–64 games).
  - 2001, 2003, 2005: 16 teams (elimination play-offs + QF/SF/F = 40 games).
  - 2007 & 2009: 16 teams (qualifying second round + QF/SF/F = 54 games).
  - 2011 & 2013: 24 teams (preliminary + second round + QF/SF/F = 90 games).
  - 2015: 24 teams with Round of 16 and 5th–8th Olympic classification (79–80 games).
  - 2017, 2022, 2025: 24 teams with Round of 16 single elimination (classification games discontinued = exactly 76 games).

---

### 3.20 Australia National Basketball League (NBL) game-by-game history, 1975-2025 (used to build Previous Sports Results/Basketball/NBL/<YEAR>/<YEAR>_games.csv and NBL_CSVs/NBL_<YEAR>.csv; tested 2026-10-01)

Every route below was requested live on 2026-10-01 and returned the named fields for all 51 years (1975–2025, covering 8,095 total game records). The built files, column dictionary, and season counts are stored in both the structured multi-sport directory and standalone download directory `NBL_CSVs/`. Season = start calendar year of the competition.

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| NBL Official Rosetta API (Seasons) | `https://prod.rosetta.nbl.com.au/get/nbl/seasons` | Full league season registry (1979 through 2026+), UUIDs, year labels, start/end dates, season types (`regular`, `preseason`, `in_season`), and match UUID arrays. | FO (NBL Australia) | API (JSON, keyless with origin header) | 200 (all 75 seasonal datasets verified) |
| NBL Official Rosetta API (Matches) | `https://prod.rosetta.nbl.com.au/get/nbl/matches/in/season/<YYYY>?limit=500&offset=0` | Seasonal match schedules, dates, venue UUIDs, team rosters, home/away scores, and match status (1979 to present). | FO | API (JSON, keyless) | 200 (all seasons verified) |
| NBL Official Rosetta API (Live/Boxscore) | `https://prod.rosetta.nbl.com.au/get/match/<match_id>/live/all` | Match play-by-play, quarter partials, player boxscores, attendance, venue data, referee crews, and official status. | FO | API (JSON, keyless) | 200 (modern era verified) |
| NBL Match Results Repository (`nblR` / Jason Zivkovic) | `https://github.com/JaseZiv/nblr_data/releases/download/match_results/results_wide.csv` | Comprehensive historical match results from the inaugural February 24, 1979 game through 2024–25 and future fixtures: date, venue, home/away teams, scores, match type, attendance. | S (Curated NBL Archive) | Open Data (CSV, HTTPS) | 200 (8,079 matches verified) |
| NBL Team Boxscores Repository (`nblR`) | `https://github.com/JaseZiv/nblr_data/releases/download/box_team/box_team.csv` | Full team boxscores for 2015–16 to 2025–26: quarter partials (P1–P4, OT), 2PT/3PT/FT shooting, rebounds, assists, steals, turnovers, blocks, points in paint. | S (Curated NBL Archive) | Open Data (CSV, HTTPS) | 200 (3,194 team rows verified) |
| SpatialJam / SpatialEC Historical Analytics | `https://spatialjam.com/nbl-historical-stats` | Historical boxscores, shot charts, advanced analytics, and franchise lineage mappings. | S (Analytics Partner) | Web / Tableau | Verified |

Traps found and handled while building the Australia NBL files:

- **Pre-NBL Era (1975–1978):** The National Basketball League (originally founded as the National Invitation Basketball League in August 1978) commenced its inaugural season in February 1979 with 10 foundation clubs. Prior to 1979, national club basketball was contested via the Australian Club Championships (ACC) and National Titles. The 1975 to 1978 records are cataloged with official pre-establishment annotations.
- **The 1998 Transition Year (Two Seasons in One Calendar Year):** From 1979 through 1998, the NBL was played during the Australian winter/autumn (Feb/Apr to Jul/Sep). In 1998, the league staged its 20th season from January to July 1998 (Adelaide 36ers champions), and then shifted to a summer schedule (October to April) beginning with the 1998–99 season (October 1998 to April 1999, Adelaide 36ers repeated). Both seasons began in 1998 and are recorded chronologically in `1998_games.csv` and `NBL_1998.csv` (331 total games).
- **Rule Changes & Period Durations:**
  - **1979–1983 (FIBA Halves Era):** 40-minute games consisting of **two 20-minute halves**; no 3-point field goal line existed.
  - **1984–2008/09 (NBA 48-Minute Era):** The 3-point line was introduced in 1984, and game duration switched to **four 12-minute quarters (48 minutes total)**, resulting in high scoring outputs.
  - **2009–10 to Present (Modern FIBA 40-Minute Era):** Switched back to **four 10-minute quarters (40 minutes total)** to align with international FIBA standards.
- **Pre-Season & Mid-Season In-Season Tournaments:**
  - **NBL Blitz:** Pre-season tournament introduced in 2004 awarding the Loggins-Bruton Cup and Ray Borner Medal.
  - **NBL Cup (2020–21):** A 36-game mid-season hub held at Melbourne's John Cain Arena during COVID-19 border disruptions; all games counted towards regular-season standings.
  - **NBL Ignite Cup (2025–26):** Mid-season Wednesday night tournament starting in Round 4.
  - **NBLxNBA Series:** Pre-season exhibition games against NBA franchises introduced in October 2017.
- **Postseason & Finals Evolution:** Single-game Grand Final (1979); Top 4 single elimination (1980–1983); Elimination finals + SF + GF (1984–1985); Best-of-3 Grand Final series introduced in 1986; Top 6/Top 8 formats (1987–2008); Top 4 format (2009–2022, Grand Final expanded to Best-of-5 in 2017); **Modern Play-In Tournament** introduced in 2022–23 for seeds 3–6 preceding best-of-3 Semifinals and best-of-5 Grand Final.

---

### 3.21 National Hockey League (NHL) game-by-game history, 1975-2025 (used to build Previous Sports Results/Ice Hockey/NHL/<YEAR>/<YEAR>_games.csv and NHL_CSVs/NHL_<YEAR>.csv; tested 2026-10-02)

Every route below was requested live on 2026-10-02 and returned the named fields for all 51 seasons (1975–2025, covering 58,379 total verified game records). The built files, column dictionary, and season counts are stored in both the structured multi-sport directory and standalone download directory `NHL_CSVs/`. Season = start calendar year of the competition (e.g., 1975 = 1975–76, 2024 = 2024–25, 2025 = 2025–26).

| Source | Route | Fields confirmed | Role | Access | Verified |
|---|---|---|---|---|---|
| NHL Official REST API (Season Schedule) | `https://api-web.nhle.com/v1/club-schedule-season/<team_abbr>/<season_id>` | Complete franchise schedules across all 109 NHL seasons (19751976 through 20252026): 10-digit Game ID, gameType (1=Preseason, 2=Regular Season, 3=Playoffs, 4=All-Star, 18=Special Exhibition), gameDate, startTimeUTC, venue, neutralSite, home/away scores, lastPeriodType (REG, OT, SO), winningGoalie, winningGoalScorer, seriesStatus (round, seriesTitle, gameNumberOfSeries), gameState. | FO (National Hockey League) | API (JSON, keyless HTTPS) | 200 (all 51 seasons verified, 58,379 games) |
| NHL Official Stats REST API (Season Metadata) | `https://api.nhle.com/stats/rest/en/season` | Authoritative season registry containing exact regular season and playoff game counts, start/end dates, and tie/overtime rule configurations for all seasons. | FO | API (JSON, keyless) | 200 (109 seasons cataloged) |
| NHL Official Game Center API | `https://api-web.nhle.com/v1/gamecenter/<game_id>/landing` | Comprehensive game landing pages: period-by-period scoring, shots on goal, shootout attempts, 3 stars of the game, attendance, and official referee crews. | FO | API (JSON, keyless) | 200 (all sample games verified) |
| Hockey-Reference & NHL Official Historical Registers | `https://www.hockey-reference.com/leagues/` & `https://records.nhl.com/` | Historical rule shifts, franchise relocation mappings (e.g. California Golden Seals, Kansas City Scouts, Atlanta Flames, Quebec Nordiques, Hartford Whalers, Minnesota North Stars), and lockout histories. | S (Curated Statistical Archive) | Web / Reference | Verified |

Traps found and handled while building the NHL files:

- **Season Year Mapping & Calendar Conventions:** NHL seasons span two calendar years (autumn to following spring). Per instruction, each season is filed under its start year: e.g., 1975 represents the 1975–76 season; 1994 represents the 1994–95 season; 2004 represents the 2004–05 season; 2024 represents the 2024–25 season; 2025 represents the 2025–26 season.
- **Shortened and Cancelled Seasons:**
  - **1994–95 Lockout:** Season delayed to January 1995; shortened to 48 regular-season games per team (624 regular season games + 81 playoff games + 2 pre-season games = 707 total games).
  - **2004–05 Full Season Lockout:** The entire 2004–05 season was officially cancelled on February 16, 2005 due to an unresolved collective bargaining dispute (the first time a major North American professional sports league cancelled an entire season due to a labor dispute). Recorded as an authoritative single-row cancellation manifest (`Game ID`: `NHL_20042005_LOCKOUT`, `Result`: `Season Cancelled Due to Lockout`, `Game State`: `CANCELLED`).
  - **2012–13 Lockout:** Season shortened to 48 regular season games per team beginning in January 2013 (720 regular season games + 86 playoff games = 806 total games).
  - **2019–20 COVID-19 Disruption & Return to Play:** Regular season paused on March 12, 2020 after ~70 games per team (1,082 regular season games); resumed in August 2020 with a modified 24-team Return to Play tournament in centralized bubbles in Toronto and Edmonton (130 playoff / qualifier games + 118 pre-season games = 1,330 total games).
  - **2020–21 COVID-19 Realignment:** Shortened 56-game intra-division schedule with 4 newly aligned divisions (including an all-Canadian North Division) (868 regular season games + 84 playoff games = 952 total games).
- **Evolution of Overtime, Shootouts, and Ties:**
  - **Pre-1983 (No Regular Season Overtime):** Games tied after 60 minutes of regulation ended in a draw/tie. Both teams were awarded 1 point in standings. Decision Type: `Tie`, Result: `Tie (X-X)`, Overtime: `No`, Shootout: `No`.
  - **1983–84 to 2003–04 (5-Minute Sudden-Death Overtime with Ties):** A 5-minute regular season overtime was introduced. If neither team scored, the game ended in a tie. (In 1999–2000, the "loser point" was introduced for OT losses).
  - **2005–06 to Present (Shootout Era — Elimination of Ties):** Ties were completely eliminated following the 2004–05 lockout. Games tied after 5 minutes of 4-on-4 overtime proceed to a penalty shootout (SO). In 2015–16, regular season overtime transitioned from 4-on-4 to 3-on-3 sudden death.
- **Dynamic BFS Discovery for Franchise Relocations:** Historical expansions and relocations (e.g. California Golden Seals `CGS`, Kansas City Scouts `KCS`, Atlanta Flames `AFM`, Quebec Nordiques `QUE`, Hartford Whalers `HFD`, Minnesota North Stars `MNS`, Winnipeg Jets [1979-96] `WIN`, Colorado Rockies `CLR`, Arizona Coyotes `ARI`, Utah Hockey Club `UTA`) are discovered dynamically via reciprocal schedule expansion seeded with original six and continuous anchor franchises.

---

## 4. Blocked, failed or excluded (do not plan on these)

| Source | State on 2026-09-28 |
|---|---|
| Fangraphs, Baseball-Reference, Pro-Football-Reference, College Football Reference, Stathead, FBref, BDFutbol, kicker, Natural Stat Trick | HTTP 403 (Cloudflare), even through the proxy (Baseball-, Pro-Football- and College Football Reference, BDFutbol and kicker re-tested 2026-09-30). WorldFootball and RealGM **reopened** on 2026-09-30 with a browser user-agent (§3.13) |
| Sofascore API | 403 |
| NBA CDN JSON | 403 |
| ESPNcricinfo direct | 403; use the proxy. **2026-09-30: the proxy route also returned 403 (Cloudflare)**; re-test before relying on it |
| MLS stats API | 404 |
| Sackmann tennis (GitHub) | 404 |
| ClubElo | 502 (again on 2026-09-28) |
| X (Twitter) | **No longer blocked (2026-09-29):** the timeline syndication and oembed routes work for official accounts (§1.8). `x.com` through the proxy, nitter and xcancel still fail |
| Reddit | Blocked on every route (re-tested 2026-09-28: `.json` and API 403; the RSS returns a block page) |
| Instagram, Facebook, TikTok, Weibo, YouTube RSS | 429 / login wall / shell only / 403 / 404 (2026-09-28). YouTube itself works through the watch page (§1.8) |
| AP News hub, Reuters sports | 403 / 401 |
| `stats.nba.com`, NBA CDN, ESPNcricinfo consumer API, Cricket Australia `apiv2`, ATP app gateway, ITF API, NBL `apicdn` | Blocked or erroring from here on 2026-09-28 (see the sport tables). The FIBA LiveStats host answered on 2026-09-30 (§3.13) |
| Full Points Footy (`fullpointsfooty.net`) | **Excluded (2026-09-30):** the domain now serves a betting-prediction spam site. Older citations to it resolve to that site; use archived copies only |
| Chadwick Bureau `baseballdatabank` (GitHub), Proballers | 404 / Cloudflare 403 on 2026-09-30 |
| Newspaper archives: Trove, Papers Past, Chronicling America, Gallica, British Newspaper Archive | Bot check or 403 to automated requests on 2026-09-30 (Trove's API needs a free key; the British Newspaper Archive is a subscription). History only; read manually |
| NRL casualty ward | Login required |
| football-data.co.uk | Historical score cross-check and post-settlement closing benchmark only, in the quarantined research workspace; never pre-issue evidence. Raw files local-only under the source's published use notice. |
| Bookmakers, odds sites, tipsters, RotoWire, RotoGrinders, FPTrack, fantasy/DFS | **Prohibited** (§1.4) |
| sportscafe.in "AI simulation", archysport, AI recaps, formulaic pitch-report sites | **Prohibited** as synthetic content |

---

## 5. Keeping this register honest

- **A source enters** only with a reproducible retrieval: route, date, access mode and response. One good result never promotes a source; judge it on accuracy, timeliness and authority.
- **Re-test the table each month,** and whenever a route fails twice. Record the date in the "Verified" column.
- **New sources found during a card** go into the mini log's document mapping with their route. They are added here at the next import.
- Historical source audits removed from this tree remain in Git history.

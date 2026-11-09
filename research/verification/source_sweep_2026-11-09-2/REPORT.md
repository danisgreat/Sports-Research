# Pregame source sweep of every log — 9 November 2026 (MDS v24.9 / CR-2026.11.09-R4)

**Owner instruction, 9 November 2026:** sweep every log, analyse where the pregame information came from, and add accurate, comprehensive and up-to-date alternate sources to the register across sports, leagues and competitions, so that future mini logs can reference them in time before a game.

**Class.** PROCEDURE + SOURCE REGISTER. No card, grade, canonical ID, probability, reference or release changes. No `ml/` code changes, so the release code hash is unchanged.

## 1. What was swept

- **Files:** every tracked log and mini, 201 files and 180 unique by SHA-256 ([LOG_FILES.csv](LOG_FILES.csv)):
  - prediction logs Parts 1–9;
  - `research/active_minis/`;
  - `research/issued_research/`;
  - mini-import and carryover inputs and originals;
  - owner drops.
- **Citations:** 9,670 URL and bare-domain citations, from 893 hosts across 270 canonical cards ([LOG_SOURCE_OCCURRENCES.csv](LOG_SOURCE_OCCURRENCES.csv)). Each citation is tagged with its card, sport and section phase:
  - PREGAME: evidence, sources and availability sections;
  - SETTLEMENT_OR_REVIEW;
  - OTHER.
- **Per-host profile:** [HOST_PROFILE.csv](HOST_PROFILE.csv).
- **Limits of the phase tags.** Sport and phase are inferred from headings, so they are approximate. Wrappers that mix phases, and cross-card references, add noise. A citation shows that a source was named, not that it supplied a verified field at the time.

## 2. Access today, under the eight-token rule (SRC-ALT-v2)

All 3,079 distinct cited URLs were checked with `ml.source_audit` ([LOG_URL_ACCESS_AUDIT.csv](LOG_URL_ACCESS_AUDIT.csv)):

| Status | URLs |
|---|---|
| ALLOWED | 1,682 |
| NO_RULES_FILE | 277 |
| BLOCKED_FOR_AI | 694 |
| RULES_UNKNOWN | 424 |
| BLOCKED_FOR_ALL | 2 |

Share of pregame citations that would now fail closed:

| Sport | Pregame citations | Fail closed now |
|---|---|---|
| Cricket | 527 | 51% |
| Basketball | 2,072 | 48% |
| Ice hockey | 599 | 48% |
| Tennis | 516 | 40% |
| Baseball | 919 | 33% |
| Rugby union | 68 | 32% |
| Soccer | 1,487 | 31% |
| Rugby league | 20 | 20% |
| AFL | 94 | 7% |
| American football | 45 | 0% |

The heaviest-used sources that now fail closed:
- the ESPN site, APIs and web API;
- Basketball-Reference and Hockey-Reference, which block GPTBot;
- koreabaseball.com and tennis.com;
- RealGM, which blocks Claude-Web and anthropic-ai;
- BeSoccer and FBref (rules unknown);
- Cricbuzz, ESPNcricinfo, pcb.com.pk and Sofascore;
- hokej.cz and Yagoonara;
- Reuters, the BBC, the Guardian and ABC;
- weltfussball, nba.com and Open-Meteo.

Each of the 30 heaviest is listed in [PREGAME_SOURCE_REJECTIONS.csv](../../source_routes/PREGAME_SOURCE_REJECTIONS.csv) with its permitted replacement.

**Firewall finding.** Some past logs cited sites whose product is odds, tips or predictions:
- BetExplorer, APWin, TotalCorner, 24score and FootyMetrics;
- betimate, hockeypredicts and okooo.

They are now listed as excluded whatever their robots rules say (the no-market rule).

## 3. Candidate alternates

- **Candidates:** 226, in two batches, covering every sport, league and data need ([CANDIDATE_TESTS.csv](CANDIDATE_TESTS.csv)). The data needs were:
  - form and history;
  - advanced ratings;
  - injuries and availability;
  - lineups and starting goalies or pitchers;
  - officials;
  - schedule and official start;
  - squads and news;
  - weather.
- **How each was checked:**
  1. A robots check for all eight tokens.
  2. If permitted, a fetch through `ml.source_access.fetch_bytes`, which re-checks the access rules and every redirect.
  3. A record of HTTP status, bytes, SHA-256, title, readable-text size, whether a 2026/2027 season marker is present, and the count of price or tip terms.
- **Raw captures:** kept outside the repository, under `%TEMP%/sports_pregame_sources_20261109/raw/<sha256>`.
- **Plain fetch refused (403) despite permissive robots rules:**
  - FanGraphs, Elite Prospects, IIHF and Transfermarkt. The standard web reader also failed, so these are rejected.
  - The ATP results-archive index: the reader opened it, so it is admitted as index-only. Its per-tournament archive pages block every token.

**Result:**
- **Admitted:** 139 sources in [PREGAME_SOURCES.csv](../../source_routes/PREGAME_SOURCES.csv), all permitted and actually retrieved. 11 show prices or tips and are marked `YES_BLOCK`.
- **Rejected:** 118 rows, with reasons, in [PREGAME_SOURCE_REJECTIONS.csv](../../source_routes/PREGAME_SOURCE_REJECTIONS.csv):
  - 80 candidates that are blocked, unknown, refused, script shells or wrong-scope;
  - 30 log sources that now fail closed;
  - 8 firewall exclusions.

| Sport | Admitted | Main additions |
|---|---|---|
| Basketball | 24 | Official NBA injury report and referee assignments; Dunks & Threes EPM; StatMuse game logs; Fox scores; RotoWire lineups and injuries (prices blocked); Eurobasket and LatinBasket; official B.League, ACB, LBA, LKL, NKL, ESAKE, BBL, NBL1, Czech federation and FIBA sites; FanCrew NBL; Tiebreaker Times and Philstar (PBA) |
| Ice hockey | 12 | MoneyPuck; Daily Faceoff starting goalies (prices blocked); RotoWire lines; Scouting the Refs; StatMuse; Fox; nhl.com scores; AHL; PENNY DEL; Swehockey; czehockey.cz and Onlajny |
| Baseball | 14 | MLB Stats API; probable pitchers and starting lineups; Baseball Savant; StatMuse; Fox; RotoWire lineups and RotoGrinders park weather (prices blocked); MyKBO and KBO English; NPB and DELTA 1.02; CPBL official and CPBL stats |
| Tennis | 8 | Tennis Abstract Elo; Ultimate Tennis Statistics; WTA; Tennis Temple; Live Tennis rankings; Tennis Explorer (prices blocked); Sackmann data; ATP index only |
| Cricket | 15 | Cricsheet; ICC; ECB; Cricket Australia; BCCI; NZC; Cricket West Indies; IPL, BBL, PSL and SA20 official sites; Wisden; SuperSport; CricTracker (predictions excluded); Cricket World |
| Soccer | 26 | Soccerway; Futbol24 and ScoreMondo (corners); Football Database; RSSSF; 11v11; FootballCritic; theScore; RotoWire lineups; Physioroom; UEFA; AFC; J.League and its data site; MLS; American Soccer Analysis; A-Leagues; ISL; CBF; LPF; SPL; RFEF; DBU; 1 Lyga; MatchScan (CSL) |
| AFL | 5 | AFL team line-ups; AFL Tables; FootyWire injury list; Wheelo Ratings; AFLW |
| Rugby league | 6 | NRL; Rugby League Project; Zero Tackle; League Unlimited; Super League; Love Rugby League |
| Rugby union | 11 | World Rugby; Ultimate Rugby; RugbyPass; ItsRugby; Super Rugby; Premiership; URC; Top 14; EPCR; Six Nations; Rugby Australia |
| American football | 10 | NFL injury reports and operations; nflverse; Sumer Sports; StatMuse; Fox; RotoWire injuries; Football Zebras (officials); CFL; College Football Data |
| Weather | 7 | MET Norway; Met Office; Visual Crossing; Time and Date; Weather Underground; Meteostat bulk; Aviation Weather Center METAR |
| News | 1 | Bing News, as a pointer only |

Every row gives:
- the field;
- what it replaces;
- **when to check it**: for example, injury reports the day before and in the final hour, lineups after the team announcement, referee assignments on game day, and weather within 24 h and again within 3 h;
- **its use rule**: sporting fields only; prices and tips blocked; verify the exact event and the as-of time.

## 4. Gaps that remain (honest limits)

No permitted, retrievable source was found for:
- **All-league soccer expected goals.** Understat and FBref fail; only MLS via American Soccer Analysis works.
- **WNBA statistics.** wnba.com and Her Hoop Stats block AI.
- **NCAA basketball ratings.** Bart Torvik is blocked and Warren Nolan is unreachable.
- **KBL official statistics.** Only Flashscore, with prices blocked.
- **PBA official statistics.** News only.
- **Hockey:** the KHL, the SHL official site, Natural Stat Trick, Elite Prospects, HockeyDB and the NHL APIs.
- **Baseball:** FanGraphs, Baseball-Reference and Statiz.
- **Other sites:** ITF draws, Cricket South Africa, CPL, Club Elo, Transfermarkt, Liga MX and the CSL official site.

These fields stay `NOT_VERIFIED` under SRC-ALT-v2 until a permitted alternate is found and checked. Access is a dated observation: re-audit the exact URL before each use (`python -B -m ml source-audit --url <url>`). An admitted site is a route, never event evidence. Independence between sites remains UNKNOWN unless shown.

## 5. Other work in the tree

- **A separate uncommitted folder:** `research/verification/source_sweep_2026-11-09-1/` was present before this run. It was not read as an input, modified or committed here.
- **Tests:** results are in [TEST_RECEIPT.md](TEST_RECEIPT.md).

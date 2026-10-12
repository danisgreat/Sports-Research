# Field lineage and route matrix for leagues in current use (R29, scoped)

**Probed 2026-10-12, about 15:45–15:55 AEDT, from one machine** (this session, Windows, keyless HTTP; browser user-agent where noted). Scope: the leagues carded in the last cohort or rebuilt today. A 200 response with the expected field marker shows that the **route was reachable and returned that field on this date**. It does not show source truth, collector independence or availability tomorrow. Independence is `UNKNOWN` wherever no publisher statement establishes it. Two domains are never counted as two independent collectors on reachability alone (CURRENT_RULES §5).

| League | Field | Field owner (A) → route | Probe | Structured provider / compiler (B) → route | Probe | Collector lineage | Fallback and failure mode |
|---|---|---|---|---|---|---|---|
| NBL | Final, quarters, OT | nbl.com.au match page `/matches/<home>-v-<away>-men-<dd-mm-yyyy>` | 200 via HTML; **score not in the server render** (client-loaded; confirmed by an r.jina.ai render, which showed teams and date but no score) | ESPN site API `basketball/nbl/scoreboard?dates=YYYYMMDD` | 200, `score` present | UNKNOWN (likely one league stats feed behind both; not established) | Owner score needs a browser-capable read (run-2 gap; still DATA_PENDING). ESPN date ranges return 400, so query single dates |
| NBA | Final, quarters, starters | cdn.nba.com `scheduleLeagueV2.json` | **403** with and without a browser user-agent | ESPN `basketball/nba/scoreboard` | 200 | UNKNOWN | Use ESPN summary (B); NBA Game Book PDF when reachable |
| MLB | Final, linescore, innings | statsapi.mlb.com `/api/v1/schedule` | 200, `gamePk` | — | — | Owner | Owner route reliable keyless |
| NHL | Final, OT/SO | api-web.nhle.com `/v1/score/<date>` | **403 without user-agent; 200 with a browser user-agent** | ESPN `hockey/nhl` | not probed today | UNKNOWN | Send a browser user-agent |
| Liiga | Final, periods | liiga.fi `/api/v2/games` | 200, `homeTeam` | — | — | Owner | — |
| KBO | Final, innings, line score | eng.koreabaseball.com DailySchedule: 200 (page shell; marker present). **Usable owner route found 2026-10-12, about 22:10 AEDT:** POST `www.koreabaseball.com/ws/Schedule.asmx/GetScoreBoardScroll` (`leId=1`, `srId` series code, `seasonId`, native `gameId`; browser user-agent and GameCenter referer) | JSON per-inning line score and R/H/E/B. Read for all 779 completed 2025 games; 777 agreed with the repaired archive, and the 2 that did not exposed MyKBO errors | mykbostats.com weekly schedule | **403 direct; 200 via r.jina.ai** (marks extras as `Final/N`) | MyKBO compiles from KBO (not independent) | Settle from the official box score (RET-06); MyKBO is B corroboration only |
| NPB | Final, innings | npb.jp `/bis/eng/<year>/games/` and each game's box score `s<yyyymmdd><nnnnn>.html` | 200. Per-inning line score and a printed note "( N innings )" when N is not 9. Read for all 878 completed 2025 games on 2026-10-12, about 22:15 AEDT: scores 878/878, cell count matches the note every time | — | — | Owner | — |
| EPL | Final, HT, corners | Premier League pulselive `footballapi.pulselive.com/football/fixtures` (Origin/Referer headers) | 200, `content` | football-data.co.uk `E0.csv` (contains odds: read named fields only); ESPN `soccer/eng.1` | 200 / 200 | football-data and engsoccerdata are separate compilers, upstream UNKNOWN; ESPN UNKNOWN | Corners settle from pulselive (A) |
| ATP | Set scores, retirements | atptour.com results archive | **403 without user-agent; 200 with a browser user-agent** | ESPN tennis scoreboard (memory: covers WTA 125) | not probed today | UNKNOWN | Browser user-agent; Tennis Abstract for historical form (compiler) |
| ACB | Final, quarters | acb.com results | 200 | FIBA LiveStats (not probed) | — | UNKNOWN | — |
| B.LEAGUE | Final, quarters | bleague.jp schedule | 200 | — | — | Owner | — |
| Czech Extraliga | Final, periods | hokej.cz matches | 200 (page; field structure not parsed) | hockeyarchives.info season page | 200, round headers present | hockeyarchives is a compiler; upstream UNKNOWN | Archive rebuilt from hockeyarchives (single compiler); settle live cards from hokej.cz |

**What this does and does not close.**
- **Closed:** reachability and field presence of each primary route as of today, the browser-user-agent requirement for NHL and ATP, and the fact that the NBL owner page does not carry the score in its server render.
- **Also closed (later the same evening):** keyless owner routes for KBO and NPB per-game innings, used for the R31 repair.
- **Not closed:** publisher lineage statements (who collects for whom), NBL owner scores for the 19 single-source 2026-27 games, and the NBA owner CDN.

These stay `DATA_PENDING` in the implementation map. Probing more machines, or dated repeat probes, is a recurring task, not a one-off.

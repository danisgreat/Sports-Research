# Base-rate and recency research — 2026-09-25

**Status: REFERENCE / LEARNING_ONLY.** These are historical field-owner frequencies and out-of-sample comparisons, recorded with their n. They are not identities, not fitted coefficients (`L-087`), not universal bounds and not ranking rules. [`BASE_RATES_REGISTER.md`](../../BASE_RATES_REGISTER.md) §7 and [`RECENCY_AND_REBOUND.md`](../../RECENCY_AND_REBOUND.md) §7 are where the figures are cited. This folder is the re-runnable query that produced them, which the register's provenance rule requires.

**Market-blind.** Nothing here reads odds, spreads, totals lines or market-derived fields. ESPN summary keys that carry them (`pickcenter`, `odds`, `againstTheSpread`, `winprobability`) and the NHL score payload's `oddsPartners` key are never read by the analysis scripts. The result JSON files contain derived statistics only.

## Sources (retrieved 2026-09-25, ~00:10–01:00 AEST)

| Lane | Endpoint | Note |
|---|---|---|
| ESPN site API scoreboard | `site.api.espn.com/apis/site/v2/sports/{basketball/wnba, basketball/nba, basketball/nbl, hockey/nhl, soccer/eng.1}/scoreboard?dates=YYYYMMDD` | **One date per call.** Every date *range* (even 7 days, any `limit`) now returns HTTP 400. Verified 2026-09-25. |
| ESPN site API summary | `…/soccer/eng.1/summary?event={id}` | EPL goal minutes (`keyEvents`) and `wonCorners` (boxscore team statistics), 380 of 380 matches |
| ESPN tennis scoreboard | `…/tennis/{wta,atp}/scoreboard?dates=YYYYMMDD` | One call returns every match of each tournament active that day. Pulled every third day, 1 Jan – 24 Sep 2026. It covers the Slams, WTA/ATP tour events **and WTA 125 events** (e.g. Tolentino, Oeiras, Megasaray). |
| NHL api-web | `api-web.nhle.com/v1/score/YYYY-MM-DD` (**curl**; Python urllib gets 403) | Per-goal `goalModifier` (`empty-net`), `periodDescriptor`, `gameOutcome.lastPeriodType` |
| MLB statsapi | `statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=2026-03-25&endDate=2026-09-24&gameType=R&hydrate=linescore,venue` | One call |

## Scripts

- `fetch.py`: cached JSON fetcher (gzip-aware; no browser User-Agent). It writes to `cache/`, which is git-ignored.
- `pull_all.py`, `pull_more.py`, `pull_nhl_tennis.py`, `pull_nhl_pre.py`: season pulls.
- `analyze_leagues.py`: base rates, width benchmark, and R-1 recency and out-of-sample window tests (WNBA, NBA, NBL, NHL, EPL). Output: `league_results.json`.
- `analyze_extra.py`: rest-day contrast and monthly scoring drift. Output: `extra_results.json`.
- `analyze_more.py`: three-season NBL and WNBA checks, early-season totals, EPL first-half goals and corners. Output: `more_results.json`.
- `analyze_nhl.py`, `analyze_nhl_pre.py`: empty-net goals, regulation margins, OT/SO, preseason. Output: `nhl_results.json`.
- `analyze_tennis.py`: total games and game-margin conditionals. Output: `tennis_results.json`.
- `analyze_mlb.py`: all-park totals, first five innings, width benchmark. Output: `mlb_results.json`.

Re-run from this folder with `python pull_all.py` and then the `analyze_*` script. The day-by-day ESPN pulls take about 10 minutes when the cache is cold.

## Definitions used

- **Regular season** means ESPN `season.type == 2`. The EPL has no type split, so all 380 matches are used. The MLB population is Final (`F`) games with nine scheduled innings.
- **Width benchmark** is the residual SD of the game total, and of the home margin, around a leak-free season-to-date predictor:
  - total: (home points for + away points against)/2 + (away points for + home points against)/2;
  - margin: half the net-rating difference plus the league home edge to date;
  - both teams need at least 10 prior games (8 in the EPL, 15 in MLB).
  - It is the error of a deliberately crude model. A card that knows more (lineups, pace, starters) can be somewhat narrower. A card much narrower than the benchmark must say what it knows.
- **Recency tests** use the same design as `RECENCY_AND_REBOUND.md` §1, with two changes: the baseline is the team's own leave-two-out mean, and "poor game" means the bottom quintile of the previous-game residual. Out-of-sample predictions use only games before the one predicted; the league constant is the running league mean before that date.

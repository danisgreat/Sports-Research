# Local reference and input freeze — LOCAL-20261114B4496A3F-G0001
- Created: 2026-11-14T13:34:19+11:00
- Status: LOCAL_REFERENCE_SNAPSHOT_ONLY; no repository freeze, no published card
- Authority: `danisgreat/Sports-Research` `main` commit `008cedc4ff469e7a808292aa3667a7bffe22e273`
- Event: Chicago State @ San Diego, NCAA Division I men's basketball; 2026-11-13 18:30 PST = 2026-11-14 14:30 AEDT
- Pregame cutoff: verified start 2026-11-14 14:30 AEDT; no live outcome inputs
- Endpoint: 40-minute regulation plus 5-minute overtime periods if regulation is tied
- Source family: university official 2026-27 cumulative statistics + official 2025-26 schedules; NCAA 2025-26 team-average 75.9 PPG from Sports-Reference NCAA seasons table
- Chicago State 2026 season games: Texas 59-109; UIW 66-54; South Carolina State 67-82; California Baptist 81-62.
- San Diego 2026 season games: Biola 79-62; Tarleton State 96-90 (OT; regulation 82-82); Colorado 75-83.
- Chicago State aggregate: 273 points for / 307 against, FGA 220, offensive rebounds 48, FTA 88, turnovers 63, four games.
- San Diego aggregate: 250 points for / 235 against, FGA 190, offensive rebounds 39, FTA 78, turnovers 36, three games. Regulation-only scored 236, allowed 227 (Tarleton OT 14-8).
- Chicago State per-game approximated possessions, FGA - OREB + TOV + 0.475*FTA: 70.70, 73.98, 71.10, 61.03.
- San Diego estimated possessions: Biola 70.93; Tarleton 79.53 in 45 minutes -> 70.69 per 40 minutes; Colorado 73.60.
- NCAA 2025-26 mean team PPG = 75.9; combined league-only prior mean total = 151.8 (not the unrepresentative 2026-27 early season average).
- NCAAB-specific league parameters absent in repository `research/competition_parameters/COMPETITION_PARAMETERS.csv`. FAMILY_PRIOR:BASKETBALL_FIBA40 home margin +1.49 used ONLY as explicit cross-league placeholder (not validated NCAA home advantage).
- Total/margin Gaussian standard deviations: 21.0 and 18.0 points, deliberately wide for early season, roster turnover and NCAAB absence from validated profile. Family floor proxies 16.82*1.10=18.50 total and 12.76*1.10=14.04 margin, both lower than chosen widths.
- NCAA league mean possession assumption: arithmetic mean of the two observed teams' estimated possessions; the league reference offensive efficiency is 75.9 * 100 / estimated game possessions.
- Attack/defense additive matchup rates: predicted HOME ORtg = USD actual 2026 reg ORtg + Chicago 2026 DRtg - NCAA proxy 2025-26 league ORtg. Predicted AWAY ORtg = Chicago 2026 ORtg + USD 2026 reg DRtg - NCAA proxy 2025-26 league ORtg.
- Neutral team matchup margin given +1.49 home advantage proxy, split +0.745 / -0.745 points without changing total.
- Shrinkage assumption: 60% small-sample current matchup + 40% prior, applied separately to matchup total and margin. No unverified lineup/injury/travel magnitude added.
- Preliminary declared candidate universe: SUPPLIED_ONLY: Chicago State +16.5, San Diego -16.5, Over 140.5 and Under 140.5. No analyst-created easy lines.
- No published predictive certification, no model-bundle execution; analytical probabilities computed only after this input freeze. This local reference is not a GitHub receipt and has no external publication timestamp.

## Source URLs (pregame)
- https://www.gocsucougars.com/sports/mens-basketball/stats
- https://usdtoreros.com/sports/mens-basketball/stats/2026-27
- https://usdtoreros.com/news/2026/11/6/mens-basketball-stromers-last-second-three-sends-toreros-to-ot-win-over-texans.aspx
- https://www.sports-reference.com/cbb/seasons/game-averages.html
- https://github.com/danisgreat/Sports-Research/blob/main/research/competition_parameters/COMPETITION_PARAMETERS.csv

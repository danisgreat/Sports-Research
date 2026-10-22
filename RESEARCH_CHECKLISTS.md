# Value-ranked research checklists, by sport (CHECK-v1)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-14 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). The existing exhaustiveness rule (EXH-v1) treated every field alike; the value is concentrated. Work the **H** rows first and time them to when they are published, then the **M** rows, and spend effort on **L** rows only when the first two are closed. Each fact that moves a number becomes an adjustment row with a size from [EFFECT_TABLES](EFFECT_TABLES.md).

**Value.** H: can move a fair probability by several points. M: about one to three. L: rarely matters. Stated publication times were checked on 22 October 2026 unless marked *unverified*; a rule change by the league supersedes this page. The verified source routes are in [SOURCES](SOURCES.md); this page ranks the inputs and does not replace the routes.

**Timing rule.** The evidence horizon is the game-log scheduled start. A decisive fact needs a publication time and a second independent source; a rumour, a projection or a depth chart is not confirmation. A fact published after the freeze is not in the card; it goes in a dated addendum (never an edit).

**Every sport:** the scheduled start and timezone; the venue and whether it is neutral; the stage and format (overtime, extra time, tie rules); weather for outdoor play in venue-local time for the match window (Open-Meteo, keyless); travel and schedule congestion; the competition's [parameter row](COMPETITION_PARAMETERS.md).

## Basketball (NBA, WNBA, NBL, EuroLeague, ACB, B.League, KBL and others)

| Input | Value | When it is published | Where |
|---|---|---|---|
| Status of the top-minute players | H | NBA: a status by 5 p.m. local the day before (1 p.m. on the second night of a back-to-back); a game-day report between 11 a.m. and 1 p.m. local (8-10 a.m. for tip-offs at 5 p.m. or earlier) | official.nba.com injury report; team and league sites elsewhere; ESPN site API for NBL and WNBA starters and did-not-play |
| Starting five; minute restrictions | H | Shortly before the tip | Team announcements; league game centres |
| Rest, back-to-backs, travel | M | Schedule | League schedule; ESPN API (measured NBA back-to-back effect: [EFFECT_TABLES](EFFECT_TABLES.md), half size) |
| Player impact and minutes history | M | Continuous | NBA stats, Basketball-Reference; public impact metrics sit on different scales, so check before comparing |
| Officials | L | NBA about 9 a.m. ET on game day *(unverified timing)* | official.nba.com referee assignments |

Traps: preseason games; competition-specific overtime and quarter lengths; never carry NBA defaults into FIBA leagues. History: the ESPN scoreboard and Basketball-Reference schedule (two lineages) for the store; league routes in SOURCES 3.2.

## Baseball (MLB, KBO, NPB, CPBL, LMB)

| Input | Value | When | Where |
|---|---|---|---|
| Starting pitcher (probable, then confirmed) | H | Days ahead; confirmed on the day *(unverified timing)* | MLB Stats API; KBO and NPB official sites |
| Line-up | M-H | A few hours before *(unverified timing)* | MLB game feed; club accounts |
| Bullpen use over the last three days | M | Box scores | MLB Stats API |
| Park, temperature, wind | M (H for totals at wind-sensitive parks) | Forecast | Open-Meteo; MLB game-feed wind |
| Umpire | L-M | Day of the game | MLB game feed |
| Pitcher quality | M | Continuous | Baseball Savant, FanGraphs |

Traps: doubleheaders; openers; KBO and NPB ties and extra-inning rules. History: MLB Stats API, Retrosheet, the KBO GetScoreBoardScroll and npb.jp routes.

## Ice hockey (NHL, AHL, Liiga, SHL, Czech Extraliga and others)

| Input | Value | When | Where |
|---|---|---|---|
| Starting goalie | H | Morning skate or warm-up *(unverified timing)* | Team announcements; NHL API game centre |
| Skater absences; line changes | M | Day of the game | Team sites |
| Back-to-backs, travel | M | Schedule | NHL API (measured NHL back-to-back effect: null) |
| Expected goals and goalie quality | M | Nightly | MoneyPuck shot data from 2007-08, 124 attributes per shot |

Traps: regulation-only against overtime/shootout settlement; empty-net goals in puck lines.

## Soccer

| Input | Value | When | Where |
|---|---|---|---|
| Confirmed XI | H | Premier League: submitted at least 75 minutes before kick-off and published from then; most leagues about 60 minutes *(unverified)* | Club and league channels; ESPN API; FotMob (structured fallback) |
| Key absences and suspensions | H | Press conferences; disciplinary lists | League discipline pages; club news |
| Team strength with expected goals | M | After each round | Understat (top leagues). FBref's advanced Opta data was removed in January 2026; its basic results remain |
| Club ratings | M | After each round | ClubElo (CSV API), as a comparator |
| Rotation, fixture congestion | M | Fixture lists | League and cup schedules |

Traps: draws; extra time and penalties in cups; women's leagues have thin data; corners need a named provider (Premier League pulselive, UEFA matchstats).

## AFL and AFLW

| Input | Value | When | Where |
|---|---|---|---|
| Selected 22, emergencies, late changes | H | Team lists at fixed times (Wednesday 6:20 p.m. for Thursday games); final teams about 50-60 minutes before the bounce; a late change only with AFL approval | AFL team lists; Champion Data's selected-team schedule |
| Venue, travel, ground familiarity | H | Fixture | AFL fixture |
| Rain and wind | M | Forecast | Open-Meteo |
| External benchmark | - | Weekly | Squiggle API (set a User-Agent with contact details; cache; do not poll) |

Traps: AFLW is not the AFL (its widths are separate rows); draws exist; sources disagree on the number of named emergencies (three or four): check the current rule.

## Rugby league (NRL, Super League)

| Input | Value | When | Where |
|---|---|---|---|
| Team list and the final 19 | H | Tuesday about 4 p.m. AEST; two players cut 24 hours out; the final 19 at 90 minutes before kick-off | NRL.com team lists |
| Halves, hooker, fullback | H | Same | Same |
| Rain and wind | M | Forecast | Open-Meteo |

Traps: golden point; depleted squads in the State of Origin period.

## Rugby union

| Input | Value | When | Where |
|---|---|---|---|
| Team announcement | H | Usually two days before *(unverified)* | Unions and clubs |
| International strength prior | M | Weekly | World Rugby rankings (its API is undocumented) |
| Weather | M | Forecast | Open-Meteo |

Traps: draws; neutral venues in tournaments.

## American football (NFL, college)

| Input | Value | When | Where |
|---|---|---|---|
| Quarterback status | H | Weekly injury report; inactives 90 minutes before kick-off | Team and league reports |
| Other key positions, offensive line | M | Same | Same |
| Wind and precipitation | M (totals) | Forecast | Open-Meteo |
| History and play-by-play | - | - | nflverse (schedules, play-by-play, injuries, depth charts) |

Traps: key numbers 3 and 7 (use the margin table); overtime rules differ between regular season and playoffs.

## Cricket

| Input | Value | When | Where |
|---|---|---|---|
| XI and toss | H | At the toss, usually about 30 minutes before the start *(unverified)* | Cricbuzz, ESPNcricinfo, board sites |
| Venue scoring and pitch | H for totals | Pitch report on the day | Cricsheet history by venue; pitch reports |
| Rain and DLS | H in rain | Forecast | Open-Meteo |
| Dew in night games | M (weak evidence) | - | Weather (dew point) |

Traps: chase totals are capped near the target; reduced-overs games; the toss is worth about 2.8 points of win probability over 44,000 matches and less in T20 (ESPNcricinfo blog, 2016).

## Tennis

| Input | Value | When | Where |
|---|---|---|---|
| Surface-specific Elo | H | Weekly | Tennis Abstract Elo reports (a 50/50 blend of surface and overall rating) |
| Fitness, recent workload, withdrawals | H | Tournament news | ATP and WTA; tournament sites |
| Serve and return statistics | M | Continuous | Tennis Abstract; ATP and WTA statistics |
| Indoor or outdoor, altitude, balls | L-M | Tournament facts | Tournament sites |

Traps: retirements and walkovers (settlement rules); best of three against best of five; the Sackmann data licence is CC BY-NC-SA and the route's current status is unverified.

## Other sports

Use the sport that is closest in structure, then state the missing competition row and the family prior used. Tier C ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)) applies unless the competition has history in the store.

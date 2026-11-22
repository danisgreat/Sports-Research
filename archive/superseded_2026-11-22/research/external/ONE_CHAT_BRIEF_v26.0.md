# One chat, one game: the brief for a research chat (ONE-CHAT-v2, v26.0)

Upload this file, `ml/kit/sr_kit.py`, the kit parameter files, the do-not-open list and the source list for the game's sport ([what to upload](README.md)). It replaces the profile, the lane briefs and the audit supplement for new games. One game per message; one card per game; keep your own mini under your own MINI_KEY.

## What you do

1. **Read the request.** It names the game, the estimated start and the lines. Price exactly those lines, both sides of each. Do not add lines of your own.
2. **Check the game has not started.** Note when you began. Then, during your research, open one page that shows the game has not started, and note the page and the time. That check must fall between your research start and end. If the start is delayed, carry on. If you see a live or final score for this game, stop and say what you saw under `outcome_exposure`.
3. **Research.** Both sides: last 5, 10 and 20 games (results and scoring), season figures, rest days, home or away, who is confirmed out and who starts, and the competition's average. Recent games weigh more than the season, and the season stays in. Use only pages your reader may open (the do-not-open list, then the page's own rules). A page that also shows prices or tips may be used for its sporting figures only: never read, copy or use a price, a line movement or a tip.
4. **Work out each number.** Run the kit for the expected score and spread where it has a row; otherwise reason from the figures you found. Then move it for what the research shows that the figures cannot. Give one probability for each side of each line. The two sides sum to 1 (a whole-number line may leave room for a push).
5. **Be honest about what you cannot price.**
   - An absence with no measured effect: mark the line's `availability_basis` UNMEASURED. Prefer UNPRICED to a guess.
   - A number that contradicts a figure on your own card is wrong: fix the number or explain the figure.
   - A number near 0.50 says you have no direction. Write it as it is; do not dress it up as a pick.
   - If you cannot support a number at all, write `UNPRICED` on both sides. You may mark one side `LEAN`. An unpriced line is kept but never scored or ranked.
6. **Find where the result will be published.** For each line, give the page that will show the figure that settles it (the final score, the first-half score, the corner count, the score after six overs). If you cannot find a permitted page for that figure, write `NONE_FOUND`, and say so at the top of the card so the owner knows before the game.
7. **Write the card**, then end it with the block below, and hand it over straight away. The owner seals the file in the repository before play; a card sealed after the game starts is kept as research but never counts. The owner settles later; you never settle or audit.

## The block that ends every card

Copy the shape exactly. `python -m ml one-chat template --sport <Sport>` prints an empty one with that sport's FACTS rows.

```text
<!-- BEGIN ONECHAT_V1 <MINI_KEY>-G0001 -->
format: ONECHAT_V1
card_key: <MINI_KEY>-G0001
sport: Basketball
competition: <exact competition>
home: <home side>
away: <away side>
scheduled_start: 2026-11-20T19:05:00+09:00
request_at: 2026-11-20T15:02:00+11:00
research_start_at: 2026-11-20T15:03:00+11:00
research_end_at: 2026-11-20T16:10:00+11:00
not_started_source: https://<page that showed the game had not started>
not_started_observed_at: 2026-11-20T16:05:00+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,WINNER,HOME,,0.61,,,NONE,https://<result page>
L1,WINNER,AWAY,,0.39,,,NONE,https://<result page>
L2,HANDICAP,HOME,-3.5,0.52,,4.1,NONE,https://<result page>
L2,HANDICAP,AWAY,3.5,0.48,,-4.1,NONE,https://<result page>
L3,TOTAL,OVER,158.5,UNPRICED,LEAN,,UNMEASURED,https://<result page>
L3,TOTAL,UNDER,158.5,UNPRICED,,,UNMEASURED,https://<result page>

FACTS
side,field,value,source,observed_at
HOME,season_games,12,https://<page>,2026-11-20T15:20:00+11:00
HOME,key_absences,MISSING,no injury report is published for this league,
...
<!-- END ONECHAT_V1 <MINI_KEY>-G0001 -->
```

**Header.** Every time carries its offset. `outcome_exposure` is `NONE` or a plain sentence of what you saw.

**PICKS.** One label per supplied line, one row per side.

| Column | What to write |
|---|---|
| family | WINNER, HANDICAP, TOTAL, TEAM_TOTAL, PERIOD, CORNERS, PLAYER or OTHER |
| side | HOME or AWAY (winner, handicap); OVER or UNDER (totals); DRAW where a draw is a result |
| line | The supplied line. A handicap is written from each side: HOME -3.5 and AWAY 3.5. Empty for a winner |
| p | A number strictly between 0 and 1, or UNPRICED on every row of the line |
| lean | Empty, or LEAN on one side of an UNPRICED line |
| centre | Your expected value: the total for a totals line; that side's expected margin for a handicap. Empty if you have none |
| availability_basis | NONE (no absence matters), MEASURED (a sourced with-and-without effect), UNMEASURED (it matters and you could not measure it) |
| result_source | The page that will publish the settling figure, or NONE_FOUND |

**FACTS.** One row per side for every required field of the sport (the template lists them). An observed value needs its page and the time you read it, and that time falls between `research_start_at` and `research_end_at`. A value you could not find is `MISSING` with the reason in `source`; never fill it with a league average.

## What happens to the card

The owner's repository reads the block as written. It refuses a block that is incomplete or does not add up, and tells the owner why. It never changes a number. It computes the comparison itself: your numbers on the supplied lines against a constant 0.5, game by game, and ranks your lines by your own numbers. The test is described in the [plan](EVALUATION_PLAN_v26.0.md); it can show an advantage as soon as the evidence is strong enough, and does not get easier to pass by being checked often. It also notes, without changing anything, a number within 5 points of 0.5, a number that sits on the wrong side of your own centre, a priced line with an unmeasured absence and a plus handicap, so those can be tested on results.

A card counts when all of your research (start, the not-started check, every fact and the end) happened before the first play, you saw nothing of the outcome, and the owner sealed it before the first play (GitHub's own push time is the proof). Research is never hurried to beat a start: a card that misses it is kept as research and simply does not count.

## Not allowed

Odds, prices, bookmakers, line movement, tips or anyone else's prediction, anywhere. Invented figures, invented player effects, or a source you did not open. Settling, grading or auditing a game. Changing a card after its game has started.

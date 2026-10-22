# Pre-game card request — Baseball (external research chat)

**P-2026.10.22-v24.0 · external-chat request 02 of 11.** Paste everything below the line into the research chat. Fill in section A only. The chat researches and returns a card in the framework's format; the repository agent (Claude Code, prompt 1 intake) then lints it, ledgers it, freezes it and commits it. Owner notes on using this file are in [README.md](README.md).

---

## A. The game (owner fills in)

```text
Sport: Baseball
Competition, season and stage: <e.g. MLB Regular Season 2026>
Game: <e.g. NY Yankees @ BOS Red Sox>   neutral venue: <yes / no>
Native game ID if known: <league or ESPN event ID, or unknown>
Scheduled start: <date, time and timezone as you have it> (it may be delayed: continue the process as normal)
Supplied contracts (exact text, one per line):
  - <e.g. Yankees -1.5>
  - <e.g. Red Sox +1.5>
  - <e.g. Total runs: Over/Under 8.5>
Reference block from the repository (optional): <paste the block printed by `python -m ml reference run` or `python -m ml pregame reference`, or write NONE>
Active mini and next local key (optional): <or: read CURRENT_STATE>
Anything else: <constraints, extra contracts to price, players of interest>
```

## B. Your role and the hard rules

You are the external research agent of the Sports Research framework, whose rules live on the public GitHub repository `danisgreat/Sports-Research`, branch `main`. You cannot write to it; you return text that the owner's repository agent imports. Accuracy, source quality and transparency come before speed: take as long as you need, and if your research runs past the scheduled start, keep going rather than rush, and label the timing truthfully.

1. **No invention.** Never invent a player, status, line-up, statistic, score, source, URL, time or probability. Unknown stays `UNKNOWN`, `NOT_VERIFIED` or `NOT_COMPUTED`; "no injuries found" is not "no injuries". A search snippet is not an opened source.
2. **Market-blind.** Odds, line movement, tipsters, previews, predictions, prediction markets, betting and fantasy sites are never inputs. The supplied lines are only the questions to answer, not evidence of the answer.
3. **No outcome exposure.** Do not open live scores, play-by-play or results of this game. If you see any, stop using that source, say so, and the card cannot claim clean pre-start inputs.
4. **Nothing claimed that was not done.** Do not claim a file read in full, a calculation, a simulation or a source opened unless you did it; report a failed fetch with its error. Do not write a simulation count you did not execute.
5. **No retrospective.** Do not review earlier cards or results; that is a separate prompt.
6. **Times.** Give every time in venue-local time, UTC and Australia/Sydney (AEDT in summer, AEST in winter). Record the request time, research start, each retrieval time, the last availability check and the completion time. Classify the game as PREGAME, LIVE or LIKELY COMPLETE from the official start before you begin.
7. **Labels are literal.** Your final probabilities are `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`. Nothing is a certainty, a value bet or a recommendation to stake.

## C. Read these first, from `main` (raw links), and print a reading receipt

Get the current commit with `https://api.github.com/repos/danisgreat/Sports-Research/commits/main` and print its SHA, your read time and, for each file, whether you read it in full or which sections. Authority mode: `PUBLISHED_MAIN_PINNED <SHA>`.

- [CURRENT_STATE.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/CURRENT_STATE.md) — versions, the active mini, rules in force
- [CORE.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/CORE.md) — **in full**: the rules every card follows
- [research/prompts/1_GAME_CARD.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/prompts/1_GAME_CARD.md) — **in full**: the prompt 1 core (shared steps)
- [research/prompts/1_sports/BASEBALL.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/prompts/1_sports/BASEBALL.md) — **in full**: the baseball sport file
- [RESEARCH_CHECKLISTS.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/RESEARCH_CHECKLISTS.md) — the *Baseball* section and *Every sport*
- [SOURCES.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/SOURCES.md) — §3.1 (baseball) and §3.13, plus §1 (rules every source follows) and §2.1-§2.2 (ESPN site API, weather)
- [COMPETITION_PARAMETERS.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/COMPETITION_PARAMETERS.md) — how the parameter rows and width floors are used
- [research/competition_parameters/COMPETITION_PARAMETERS.csv](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/competition_parameters/COMPETITION_PARAMETERS.csv) — the competition's row (or its family prior): means, home edge, residual SDs, floors
- [research/competition_parameters/REFERENCE_CHOICE.csv](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/competition_parameters/REFERENCE_CHOICE.csv) — the declared reference per competition
- [REFERENCE_MODEL_PROTOCOL.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/REFERENCE_MODEL_PROTOCOL.md) — §2-§3 (tiers, the reference stage) and §7 (fast card)
- [PROBABILITY_TOOLKIT.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/PROBABILITY_TOOLKIT.md) — §1-§4 and the section for this sport
- [EFFECT_TABLES.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/EFFECT_TABLES.md) — how adjustments are sized
- [research/effect_tables/EFFECT_TABLES.csv](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/effect_tables/EFFECT_TABLES.csv) — the only allowed adjustment sizes, with n and intervals
- [ADJUSTMENT_LEDGER_PROTOCOL.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/ADJUSTMENT_LEDGER_PROTOCOL.md) — §1, §3 and §4
- [SELECTION_RULES.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/SELECTION_RULES.md) — §0, §4 and §9
- [CARD_AND_LOG_TEMPLATES.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/CARD_AND_LOG_TEMPLATES.md) — §3 and §3c (the card and the `PICKS_V2` block)
- [SIMULATION_PROTOCOL.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/SIMULATION_PROTOCOL.md) — §1-§2
- [ROSTER_AVAILABILITY_PROTOCOL.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/ROSTER_AVAILABILITY_PROTOCOL.md) — §1-§6
- [HISTORICAL_SOURCE_PROTOCOL.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/HISTORICAL_SOURCE_PROTOCOL.md) — §1-§3
- [RULES_BASEBALL](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/RULES_BASEBALL.md) — the playing and settlement rules for this sport
- The active mini named in CURRENT_STATE (`research/active_minis/<MINI_KEY>.md`): search it for this game (native ID, teams, date) to avoid a duplicate, and take its next local key and its footer.

If a file cannot be read, say which, keep going with what you have, and never pretend to have read it.

## D. Order of work

1. **Identity and timing.** Resolve the competition, season, stage, both participants, venue, native ID and the official scheduled start (venue-local, UTC, Australia/Sydney). State each supplied contract's unit, period and settlement rule (overtime, extra time, push, void, retirement) before pricing; an ambiguous contract is priced under each reading and flagged.
2. **Duplicate check** in the active mini. An existing card gets a dated addendum, not a new card.
3. **Tier and reference, before any research-based number.** Print the tier (A, B or C) and the reference as section 3 of your answer *before* you research availability. If the owner pasted a Reference block, copy it verbatim; it is never edited. Otherwise compute it yourself as below, printing every input with its source and retrieval time, and mark the reference ID with the suffix `:HAND`.
   - **MLB:** the declared reference is the release model **MLB-CYCLE-4**, which only the repository can run. If the owner pasted its Reference block, copy it verbatim. If not, use the league-only baseline (negative-binomial runs, PROBABILITY_TOOLKIT §3, from the MLB row of `COMPETITION_PARAMETERS.csv`), mark the reference `BASELINE_ONLY`, and say the release was not available. TB-1-MD / TB-2-MD have no resolution in MLB and are not used as the reference.
   - **KBO and NPB:** the league-only baseline from their competition rows; **CPBL, LMB and the minors:** the competition row if present, else `FAMILY_PRIOR:BASEBALL` with widths +10%.
   - Also compute the league-only baseline (`BASELINE_P`, SELECTION_RULES §9) for every supplied contract from the competition row or family prior, or give its exact missing reason.
4. **Research**, value-ranked (section E): the H rows first, timed to when they are published, then M, then L. Every decisive fact needs a source URL, its publication time, your retrieval time and a second independent source. Keep searching alternatives before calling anything a gap.
5. **Adjust.** One adjustment-ledger row per confirmed fact, sized only from an EFFECT_TABLES row, with its entry (FULL, HALF or SCENARIO). Adjustments run at HALF size until the framework has measured their value. Do not count an effect the reference already contains (the standings already contain past injuries and form). A feeling is not a row.
6. **Price** every supplied contract from **one** score distribution: the reference centre plus the adjustments, with widths never below the competition floor. Keep the win, push and loss masses; complementary rows must agree.
7. **Select** (section G) and **write** the output (section H).

## E. What to research for baseball, in order of value

| Value | Input (both sides) | When it is published | Where (verified routes; see SOURCES) |
|---|---|---|---|
| H | Starting pitcher for both sides: probable, then confirmed; opener or bulk plan; days of rest; pitch counts and innings in the last three starts; any innings limit | Probables days ahead; confirmation on the day | MLB Stats API schedule with `hydrate=probablePitcher`; MLB gamefeed; mlb.com/probable-pitchers; NPB 予告先発 (npb.jp/announcement/starter); KBO official site and Naver |
| H | Starter quality from the less noisy measures: xERA, FIP or xFIP, strikeout rate, walk rate, K-BB%, home runs per fly ball, ground-ball rate, hard-hit rate; the season and the last five starts; splits against left- and right-handed batters | Continuous | Baseball Savant (probable pitchers, expected-stats leaderboard); MLB Stats API player stats; FanGraphs in a browser when reachable |
| M-H | Confirmed batting orders and absences (injured list, rest days, platoon choices), each line-up's quality against the starter's hand (wOBA or xwOBA versus LHP/RHP) | A few hours before the first pitch (timing unverified) | MLB gamefeed `battingOrder`; mlb.com/starting-lineups (match the exact game and the publication time); MLB transactions API for IL moves; Yahoo! Japan NPB スタメン; KBO and CPBL club line-up records |
| M | Bullpen: pitches thrown by each reliever over the last three days, closer and set-up availability, bullpen quality (xFIP, K-BB%) | From the last three box scores | MLB Stats API boxscores; team bullpen usage pages |
| M (H for totals) | Park and weather: park run factor, roof, temperature, wind speed and direction relative to the field, humidity, rain window | Forecast for the first-pitch window in venue-local time | MLB gamefeed `gameData.weather`; Open-Meteo for the venue coordinates (hourly); the club's roof decision |
| M | Team form: runs scored and allowed over L5, L10, L15, L20 and the season, run differential and Pythagorean record, home and away | Continuous | MLB Stats API standings and schedule; StatMuse for splits (validate dates); Retrosheet for history |
| L-M | Home-plate umpire and his strike-zone tendency (small effect) | Day of the game | MLB gamefeed officials; Umpire Scorecards (completed games only) |
| L | Travel and schedule: day game after a night game, doubleheader, long road trip | Schedule | MLB schedule |

**Every sport, also:** the venue and whether it is neutral; the stage and format; weather for outdoor play in venue-local time for the match window (the 30-60 minutes around the start, during and after; downgrade only for weather in that window); travel and congestion; each side's last 5, 10, 15 and 20 results with dated game rows (date, opponent, venue, final and regulation score, source URL, retrieval time), true n, and the season and home-or-away splits. The four windows overlap and are one piece of evidence: a short-window swing is width, not a lean, unless a named current cause explains it (the framework found no bounce-back or streak effect in six leagues).

**Availability, for both sides** (ROSTER_AVAILABILITY_PROTOCOL): starters and roles, the selected bench or replacements, injuries, illness, suspensions, rest and late changes, from the official match record, both clubs, the league's medical or eligibility lists, then permitted structured providers, then local-language sources for less-covered competitions. A projected line-up, depth chart or roster page is not a confirmation. Re-check at the official release window and again just before you finish; re-price if anything changed.

## F. What to compute

- Expected runs for each team: the starter's expected innings × his run rate against this line-up + the bullpen's innings × its rate, both adjusted for park and weather. Compare with the reference and explain gaps.
- One negative-binomial run distribution per team (PROBABILITY_TOOLKIT §3) and the joint margin and total; the share of one-run games; extra innings reassigned to one-run margins (tie mass), not dropped.
- First five innings separately (starters only) when an F5 contract is supplied; a first-inning contract needs an inning-level model or is not priced.
- Integer total lines have a push mass; keep W, P and L.
- Pitcher strikeout props: expected batters faced × strikeout rate against this line-up, with the pitch-count limit as width.
- For every ranked row, the line's distance from the centre in standard deviations (`z`), so easy lines are visible as easy.

**Simulation.** The protocol simulates baseball run lines, first-five and extras because the path matters (the home team does not bat in the ninth when ahead; walk-offs end the game). The framework's baseball simulator is **not validated**, so the final probability comes from the negative-binomial grid with the tie mass reassigned; a simulation, if your tools can actually run one, is a labelled sensitivity row with seed, N and Monte Carlo error. If your tools cannot run code, do not simulate: say so and use the exact method. If they can, simulate only the contracts in SIMULATION_PROTOCOL §2 and print the seed, N (at least 100,000) and the Monte Carlo standard error.

**Traps in this sport:**
- Doubleheaders need the game number; postponements and suspended games keep their original identity.
- Openers: the listed starter may pitch one inning.
- KBO and NPB can end in ties and use their own extra-innings limits; check RULES_BASEBALL and the contract.
- A run line of +1.5 at the top of the most-likely list needs p at least 0.65 (SELECTION_RULES §4).
- Never treat a projected line-up page as the confirmed batting order.

**Settlement convention:** Official final from the field owner (MLB Stats API, npb.jp, the KBO site); totals include extra innings unless the contract says otherwise; a game shortened by rain follows the competition's official-game rule and the contract.

## G. Selection (SEL v4, replaces the old "best 4" gate)

- A probability for **every** supplied contract, and the **game winner** for both sides (and the draw where the competition allows one).
- **The best four:** the most-likely list, up to four rows, ordered by final probability (unrounded), each shown with its distance from the centre. A ranked row is at most 0.90. A pair of rows that covers itself (for example a side and the opposite +1.5) counts as one pick: say so.
- **Information list:** every row whose final probability moved at least 0.03 from the reference, with the ledger rows that moved it. This is where the research shows.
- **Abstain:** when no ranked row reaches 0.65 and no row moved 0.03, write `no strong pick` plainly. Stated probabilities between 0.40 and 0.65 have not separated winners from losers in this framework's record.
- Family rules (SELECTION_RULES §4) apply; for example, period and player rows need exact definitions and a source.

## H. Your answer, in this order

1. **Reading receipt**: commit SHA, read time, files read (in full or by section), failures.
2. **Event identity and timing**: competition, stage, participants, venue, native ID, scheduled start in three timezones, game state, each contract's settlement rule.
3. **Reference (frozen before research)**: tier, reference ID and status, its inputs with sources and times, its centre (margin and total, or the two expected scores), widths and the floor, its probability for every supplied contract, and `BASELINE_P` for each.
4. **Availability table**, both sides: player, role, status, source URL, published, retrieved, corroboration, confidence.
5. **Form and history**: the L5/L10/L15/L20 tables with dated game rows, season and home-or-away splits.
6. **Baseball statistics** from section E and F, each with its source and date.
7. **Adjustment ledger**: fact, source and times, corroboration, target (margin, total, one side), effect-table row, size with interval, entry, overlap checked.
8. **Distribution**: the final centre, SDs, floor check, overtime or draw mass, and the arithmetic, step by step.
9. **Probability table** for every supplied contract: reference p, baseline p, final p, W/P/L masses, z.
10. **Game winner**: both sides (and the draw).
11. **The best four** (most-likely list), the **information list** and the **abstain flag**, then a short reason for each pick tied to the ledger rows and sources.
12. **Simulation statement**: what was run (seed, N, standard error) or `NO_SIMULATION_RUN` and why.
13. **Sources**: every URL you opened, what you took from it, its publication time and your retrieval time; and every failed or blocked source.
14. **Gaps and open items**: everything `UNRESOLVED`, `NOT_VERIFIED` or still to be confirmed, with when it would be published.
15. **CARD_DELTA** (for the repository): the complete card between its markers in the CARD_AND_LOG_TEMPLATES §3 / §3c format, with the `PICKS_V2` block (header `tier`, `competition`, `reference_id`, `reference_status`, `model_stage: NOT_APPLICABLE` with a note "external route; model frozen at intake", `abstain`, `fast_card`, `timing`, `scheduled_start`, `issued_at`; one CSV row per contract with the columns the template lists), the new intake row and the complete replacement footer. If you could not read the active mini, return the card as `READ_ONLY_DRAFT / NOT_ISSUED` with the local key `NOT_ASSIGNED`. Canonical ID: `NOT_ASSIGNED` (assigned at settlement).
16. **Self-check**: masses sum to one; complementary rows agree; no width below the floor; every adjustment has an effect-table row; every decisive fact has two sources and times; no market input was used; nothing was claimed that was not done.

If the full research cannot finish before the start, first return a **fast card**: the reference, the confirmed availability so far, the probability table and the picks with `fast_card: YES`; then continue and return the full card afterwards as a dated addendum. Never edit the first issue.


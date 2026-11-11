# Game request template and how a request is read (REQ-v5)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-21 and the request side of REV-15 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). The Upcoming game blocks in the prompt-1 sport files carry the owner's per-game formats (section 1, 2026-11-09) and are filled in by the owner; this page is how the agent reads them.

## 1. The owner's per-game requests (REQ-v5, owner instruction 2026-11-11; REQ-v4 of 2026-11-09 and 2026-11-10 is still read)

These are the owner's own request formats, one per sport. REQ-v5 keeps every REQ-v4 line and adds the lines the 11 November review asked for: the home side or venue (a request's order is not home first), an explicit moneyline-or-spread choice for each side line, the cricket format and batting order, the tennis tournament, surface and best-of, the ranking choice, and, for a research chat, its lane, the mini and the commit to read (EXTERNAL_RESEARCH_PROTOCOL). **One game per message:** a message that holds several games, or the unfilled templates of other sports, is split by the agent and each game is read on its own. A REQ-v4 request is still accepted; the agent resolves each missing line from the field owner and says so. The same block heads the matching prompt-1 sport file.

```text
Upcoming Basketball Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Points

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Soccer/Football Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Combined First Half Goals: Over/Under 0.5 Goals;
Combined Total Goals: Over/Under 2.5 Goals;
Combined Total Corners: Over/Under 10.5 Corners;

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Cricket Game: Team A vs Team B, Competition, Format: T20 | ODI,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)
Team A bats: first | second | not known (toss not yet made)

Team A 1st Innings Runs at end of 20 overs (T20) / 50 overs (ODI) Total: Over/Under X.X Runs
Team A 1st Innings Runs at the end of over 6 (T20) / over 5 (ODI): Over/Under X.X Runs

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Tennis Match: Player A vs Player B, Tournament (full name and year), Round, Surface, Best of 3 | 5,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)

Player A ML  or  Player A Handicap Games X.X
Player B ML  or  Player B Handicap Games X.X
Combined Total: Over/Under X.X Games

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Ice Hockey Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Goals

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Rugby League Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Points

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Rugby Union Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Points

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming American Football Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Points

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Baseball Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Runs

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

```text
Upcoming Australian Rules Game: Team A vs Team B, Competition,
Estimated Game Time Start: Day Month Year, Time AM/PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Team A | Team B | Neutral (venue, if known)

Team A ML  or  Team A Spread X.X
Team B ML  or  Team B Spread X.X
Combined Total: Over/Under X.X Points

Rank: supplied lines only | all lines
Run: Lane L1, L2, L3, L4, L5 or FULL | Mini <MINI_KEY> | Commit <SHA>   (research chats only; leave out for the repository)
```

Other sports keep the free-form block in their sport files until the owner supplies a format for them.

## 1b. How each line is read

**Common to every request:**

- **REQ-v5 lines (2026-11-11).**
  - *Home side / venue.* Names the home side or a neutral venue. Without it the agent resolves home and away from the field owner; it never assumes the first-named side is at home.
  - *ML or Spread.* Each side line is written as one of the two: "Team A ML" or "Team A Spread −4.5". A line written "ML/Spread" with a number is read as the spread; without a number as the moneyline, and the agent says which reading it used.
  - *Cricket format and batting order.* "Format: T20 | ODI" fixes the 20- or 50-over innings and the over-6 or over-5 checkpoint. "Team A 1st Innings" is Team A's first innings whichever order it bats in: batting first it runs to the full overs or all out; batting second it is a chase that stops at the target (its total is censored at the winning delivery). With the order unknown, both branches are priced as the innings-order mixture (RULES_CRICKET control 21) and the row is frozen with both.
  - *Tennis tournament, surface and best-of.* The full tournament name and year, surface and best-of select the tour row and the exact recursion. A missing surface or best-of is resolved from the field owner before pricing.
  - *Rank.* "supplied lines only" (the default when the line is missing) writes `rank_scope: SUPPLIED_ONLY`, so the most-likely list holds only the owner's own lines (FREEZE-v1); "all lines" writes `rank_scope: ALL`, and analyst-derived lines are ranked and labelled as such.
  - *Run.* For a research chat only: its lane (EXTERNAL_RESEARCH_PROTOCOL §2), the mini it notes against and the commit SHA it must read. The repository ignores this line.
- **Header line.** It gives the teams or players and the competition. The agent resolves the exact competition, stage, venue and native event ID, and identifies home and away from the field owner; the request's order is not assumed to be home first.
- **Estimated start.** "Estimated Game Time Start … AEDT (can be delayed so continue the process as normal)" is an estimate. The agent verifies the official scheduled start in the venue's time zone, UTC and AEDT, and the actual start when known. The research then runs to completion whatever the time, under the owner's never-rush rule (RULES_REFERENCE A§5). The card's timing label comes from evidence (`PREGAME` only when a pre-start freeze is proved; LEDGER-v2), never from the estimate.
- **"ML/Spread".** Each side line is one contract, written as the owner fills it in: a moneyline ("Team A ML") or a spread or handicap with its number ("Team A −4.5"). Both sides of every supplied line are priced, and the winner probability for both sides is always shown, with the draw where the competition allows one.
- **"Over/Under X.X".** One two-way line: both Over and Under are priced from the same distribution.
- **Supplied lines are questions, not evidence** (MARKET_BLIND). The line-implied 0.5 is written only as a settlement benchmark.

**Per sport.** The endpoint is the framework default in `ml.config.SPORT_RULES` unless the line's own text names another. Basketball (BK-OT-1) and Australian rules finals (AFL-ET-1) have owner conventions for the operator's terms. Elsewhere, unknown operator terms are priced on both branches and settled by the sport file's rule.

| Request | Line | Family / quantity | Endpoint and settlement | Deep loss review (DEEPLOSS-v1) |
|---|---|---|---|---|
| Basketball | Team A / Team B ML or Spread | WINNER or HANDICAP / MARGIN | Final score including every overtime (BK-OT-1) | Top side: the higher-p side row |
| Basketball | Combined Total Points | TOTAL / TOTAL | Including overtime (BK-OT-1) | Top total |
| Soccer | Combined First Half Goals O/U 0.5 | PERIOD / PERIOD | First half, including its stoppage time | Reviewed if it is rank 1 |
| Soccer | Combined Total Goals O/U 2.5 | TOTAL / TOTAL | 90 minutes plus stoppage; extra time and penalties excluded (REGULATION_90) | Top total candidate |
| Soccer | Combined Total Corners O/U 10.5 | CORNERS / COUNT | 90 minutes plus stoppage, from a permitted structured provider (SRC-ALT-v1; corner rows need a provider count, RULES_SOCCER) | Top total candidate (a full-match count total) |
| Cricket | Team A 1st Innings Runs at end of 20/50 overs | TEAM_TOTAL / TEAM_TOTAL | Team A's first-innings total over the scheduled 20 (T20) or 50 (ODI) overs; if all out earlier, the total at the last wicket; a reduced-overs innings settles only under the frozen rule, otherwise UNRESOLVED (RULES_CRICKET) | Top total |
| Cricket | Team A 1st Innings Runs at the end of 6/5 overs | PERIOD / PERIOD | Runs at the end of over 6 (T20 powerplay) or over 5, as the line states; the checkpoint must be a completed over (RULES_CRICKET control 29) | Reviewed if it is rank 1 |
| Tennis | Player A / Player B ML or Handicap Games | WINNER or HANDICAP / MARGIN (games) | Completed match; retirement and walkover under RULES_TENNIS §10.6 | Top side |
| Tennis | Combined Total Games | TOTAL / TOTAL (games) | Completed match; a match tiebreak counts as one game; retirement under RULES_TENNIS §10.6 | Top total |
| Ice hockey | Team A / Team B ML or Spread (puck line) | WINNER or HANDICAP / MARGIN | FULL_GAME_INCL_OT_SO by default; the regulation-draw branch is kept, and unknown operator terms are priced on both branches (RULES_ICE_HOCKEY IH-P3) | Top side |
| Ice hockey | Combined Total Goals | TOTAL / TOTAL | As above; a shootout winner adds one goal to a regulation tie (H-R1) | Top total |
| Rugby league | ML or Spread; Total Points | WINNER, HANDICAP, TOTAL | FULL_GAME_INCL_GOLDEN_POINT | Top side; top total |
| Rugby union | ML or Spread; Total Points | WINNER, HANDICAP, TOTAL | 80 minutes (FULL_GAME); a draw is a live outcome and is priced | Top side; top total |
| American football | ML or Spread; Total Points | WINNER, HANDICAP, TOTAL | Including overtime (FULL_GAME_INCL_OT); a regular-season tie is a live outcome | Top side; top total |
| Australian rules (AFL, AFLW and state leagues) | ML or Spread; Total Points | WINNER, HANDICAP, TOTAL | Full game to the final siren of the fourth quarter (FULL_GAME); a home-and-away draw is a live outcome and is priced. Finals lines include extra time (AFL-ET-1). AFL and AFLW stay separate populations | Top side; top total |
| Baseball | ML or Spread (run line); Total Runs | WINNER, HANDICAP, TOTAL | Including extra innings (FULL_GAME_INCL_EXTRAS); KBO and NPB ties are live outcomes | Top side; top total |

**The DEEPLOSS-v1 roles in requests without a side line.** Soccer and cricket requests have no side line, so the review's top-total trigger covers the supplied full-match or full-innings total rows:
- **Soccer:** the higher-p of Total Goals and Total Corners.
- **Cricket:** the full-innings row. The over-6 or over-5 checkpoint is a period row.

Rank 1 covers the rest. The winner probability shown on a soccer or cricket card is informational unless the owner supplies a winner line.

**Where to send it (REQ-v3, 2026-11-08).** Send every request to the repository agent; cards are made only in this repository. The external-chat requests (REQ-v2) are retired and archived in [archive/retired_2026-11-08/external_requests/](archive/retired_2026-11-08/external_requests/README.md); a chat answer pasted with a request is an owner-supplied research note, re-verified before use ([WORKFLOW](WORKFLOW.md#part-a-execution_environment_protocol) §1).

## 2. Reading a request

| A request says | The agent does |
|---|---|
| "Do as many simulations as possible" / "run simulations" | Uses the exact distribution; runs a code simulation only for the contracts in [SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md) section 2 and prints seed, N and Monte Carlo error; says plainly that no simulation was run where none was needed. Never writes a simulation count it did not execute |
| "Pick your own picks" | Prices every supplied contract and returns the picks block: probabilities, a most-likely list with line difficulty, an information list, and `no strong pick` when nothing reaches 0.65 and nothing moved from the reference |
| "Best 4 in order from most to least likely" | The most-likely list of up to four rows, ordered by final probability; labelled with each row's distance from the centre so that easy lines are visible as easy |
| "Add a potential game winner" | The winner probability for both sides, including a draw where the competition allows one |
| "Take as long as you need" | Research completes (CURRENT_RULES section 5), but a request that arrives close to the start gets the fast card first (FASTCARD-v1) so that something checkable exists before play |
| "Do a retrospective" / "do not do a retrospective" | Retrospectives are prompt 6 and are never part of a card |
| Supplied lines | Contract metadata only: they set the questions asked, not the probabilities answered. The line-implied benchmark (0.5) is written for supplied two-way lines |

## 3. Timing

The agent records the request time, the research start, every source retrieval time, the completion time and the actual issue time, and labels the card `PREGAME`, `POST_START_ISSUE` or `TIMING_UNVERIFIED`. A request sent after the scheduled start can still be researched with pre-start inputs, but it is scored in its own stratum and is not a forecast issued before play.

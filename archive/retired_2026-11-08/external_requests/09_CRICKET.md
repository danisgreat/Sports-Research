# Pre-game card request — Cricket (external research chat)

**P-2026.10.22-v24.0 · external-chat request 09 of 11.** Paste everything below the line into the research chat. Fill in section A only. The chat researches and returns a card in the framework's format; the repository agent (Claude Code, prompt 1 intake) then lints it, ledgers it, freezes it and commits it. Owner notes on using this file are in [README.md](README.md).

---

## A. The game (owner fills in)

```text
Sport: Cricket
Competition, season and stage: <e.g. Big Bash League 2026-27 (T20), Match 14>
Game: <e.g. Sydney Sixers v Perth Scorchers at the SCG (home team first)>   neutral venue: <yes / no>
Native game ID if known: <league or ESPN event ID, or unknown>
Scheduled start: <date, time and timezone as you have it> (it may be delayed: continue the process as normal)
Supplied contracts (exact text, one per line):
  - <e.g. Sydney Sixers to win>
  - <e.g. Perth Scorchers to win>
  - <e.g. Sydney Sixers first-innings total: Over/Under 172.5 runs>
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
- [research/prompts/1_sports/CRICKET.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/prompts/1_sports/CRICKET.md) — **in full**: the cricket sport file
- [RESEARCH_CHECKLISTS.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/RESEARCH_CHECKLISTS.md) — the *Cricket* section and *Every sport*
- [SOURCES.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/SOURCES.md) — §3.3 (cricket), including the toss and strip ladders, plus §1 (rules every source follows) and §2.1-§2.2 (ESPN site API, weather)
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
- [RULES_CRICKET](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/RULES_CRICKET.md), [LEAGUE_RULES_CRICKET](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/LEAGUE_RULES_CRICKET.md) — the playing and settlement rules for this sport
- The active mini named in CURRENT_STATE (`research/active_minis/<MINI_KEY>.md`): search it for this game (native ID, teams, date) to avoid a duplicate, and take its next local key and its footer.

If a file cannot be read, say which, keep going with what you have, and never pretend to have read it.

## D. Order of work

1. **Identity and timing.** Resolve the competition, season, stage, both participants, venue, native ID and the official scheduled start (venue-local, UTC, Australia/Sydney). State each supplied contract's unit, period and settlement rule (overtime, extra time, push, void, retirement) before pricing; an ambiguous contract is priced under each reading and flagged.
2. **Duplicate check** in the active mini. An existing card gets a dated addendum, not a new card.
3. **Tier and reference, before any research-based number.** Print the tier (A, B or C) and the reference as section 3 of your answer *before* you research availability. If the owner pasted a Reference block, copy it verbatim; it is never edited. Otherwise compute it yourself as below, printing every input with its source and retrieval time, and mark the reference ID with the suffix `:HAND`.
   - **No stored history and no reference:** tier C, reference `NONE`. The innings-total estimate is the card's own first estimate (PROBABILITY_TOOLKIT §7), built from venue and format history; a chasing side's total is capped near the target. The framework's cricket simulator has no phase tables yet and is not used for the final probability.
   - Also compute the league-only baseline (`BASELINE_P`, SELECTION_RULES §9) for every supplied contract from the competition row or family prior, or give its exact missing reason.
4. **Research**, value-ranked (section E): the H rows first, timed to when they are published, then M, then L. Every decisive fact needs a source URL, its publication time, your retrieval time and a second independent source. Keep searching alternatives before calling anything a gap.
5. **Adjust.** One adjustment-ledger row per confirmed fact, sized only from an EFFECT_TABLES row, with its entry (FULL, HALF or SCENARIO). Adjustments run at HALF size until the framework has measured their value. Do not count an effect the reference already contains (the standings already contain past injuries and form). A feeling is not a row.
6. **Price** every supplied contract from **one** score distribution: the reference centre plus the adjustments, with widths never below the competition floor. Keep the win, push and loss masses; complementary rows must agree.
7. **Select** (section G) and **write** the output (section H).

## E. What to research for cricket, in order of value

| Value | Input (both sides) | When it is published | Where (verified routes; see SOURCES) |
|---|---|---|---|
| H | Both XIs and the toss result and decision | At the toss, usually about 30 minutes before the start (unverified) | The toss ladder in SOURCES §3.3: official match centre or board scorecard first (cricket.com.au, IPL, ECB, ICC, CPL), then the broadcast, the official live blog, the ESPN toss note, Cricbuzz. If none: `TOSS STATUS = NOT_VERIFIED_AFTER_SEARCH`; never infer the toss from the batting order |
| H for totals | The pitch and venue: a named pitch report on the day (the strip ladder), the venue's first- and second-innings totals by format, boundary sizes | On the day; history | Broadcast pitch report; curator; Cricsheet ball-by-ball for venue history; never the excluded formulaic pitch-report sites listed in SOURCES §3.3 |
| H in rain | Rain in the match window and the reduced-overs or DLS consequences | Forecast in venue-local time | Open-Meteo hourly; the board's weather updates |
| M | Squads and availability: overseas players in franchise leagues, injuries, workload rest, players on international duty | Squad announcements | Board and franchise sites; ICC replacement announcements |
| M | Team strength in this format: run rates in the powerplay, middle and death overs, batting and bowling, over L5, L10, L15, L20; bowling attack type (pace or spin) against the conditions | Continuous | ESPN cricket API (one lineage with ESPNcricinfo); Cricbuzz; Cricsheet |
| M (weak) | Dew in night games (dew point) | Forecast | Open-Meteo dew point |

**Every sport, also:** the venue and whether it is neutral; the stage and format; weather for outdoor play in venue-local time for the match window (the 30-60 minutes around the start, during and after; downgrade only for weather in that window); travel and congestion; each side's last 5, 10, 15 and 20 results with dated game rows (date, opponent, venue, final and regulation score, source URL, retrieval time), true n, and the season and home-or-away splits. The four windows overlap and are one piece of evidence: a short-window swing is width, not a lean, unless a named current cause explains it (the framework found no bounce-back or streak effect in six leagues).

**Availability, for both sides** (ROSTER_AVAILABILITY_PROTOCOL): starters and roles, the selected bench or replacements, injuries, illness, suspensions, rest and late changes, from the official match record, both clubs, the league's medical or eligibility lists, then permitted structured providers, then local-language sources for less-covered competitions. A projected line-up, depth chart or roster page is not a confirmation. Re-check at the official release window and again just before you finish; re-price if anything changed.

## F. What to compute

- Innings totals: a heavy-tailed normal around the venue-and-format mean adjusted for the XIs and the conditions; the chasing side's total capped near the target (a high team-total Over for the chasing side is a structural fade).
- Match winner from the two sides' strengths, the toss (worth about 2.8 points of win probability over 44,000 matches, less in T20), and the conditions; ties, super overs and no-results as the contract defines them.
- For every ranked row, the line's distance from the centre in standard deviations (`z`), so easy lines are visible as easy.

**Simulation.** Exact or approximate formulas only. The protocol would simulate innings ball by ball once a phase table is built from Cricsheet for the exact competition and format; none exists, so any simulation is a labelled sensitivity row. If your tools cannot run code, do not simulate: say so and use the exact method. If they can, simulate only the contracts in SIMULATION_PROTOCOL §2 and print the seed, N (at least 100,000) and the Monte Carlo standard error.

**Traps in this sport:**
- Chase totals are capped near the target.
- Reduced-overs games and DLS change every total.
- Tests can be drawn; limited-overs games can tie or have no result.
- Freeze `PRE_TOSS` or `POST_TOSS` and say which.

**Settlement convention:** The official scorecard or the board's final report, with Cricbuzz and ESPN as checks (ESPN and ESPNcricinfo count once).

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
6. **Cricket statistics** from section E and F, each with its source and date.
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


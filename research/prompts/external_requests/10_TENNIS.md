# Pre-game card request — Tennis (external research chat)

**P-2026.10.22-v24.0 · external-chat request 10 of 11.** Paste everything below the line into the research chat. Fill in section A only. The chat researches and returns a card in the framework's format; the repository agent (Claude Code, prompt 1 intake) then lints it, ledgers it, freezes it and commits it. Owner notes on using this file are in [README.md](README.md).

---

## A. The game (owner fills in)

```text
Sport: Tennis
Competition, season and stage: <e.g. ATP 500 Vienna 2026, round of 16 (indoor hard, best of three)>
Game: <e.g. Player A v Player B>   neutral venue: <yes / no>
Native game ID if known: <league or ESPN event ID, or unknown>
Scheduled start: <date, time and timezone as you have it> (it may be delayed: continue the process as normal)
Supplied contracts (exact text, one per line):
  - <e.g. Player A to win>
  - <e.g. Player B to win>
  - <e.g. Total games: Over/Under 22.5>
  - <e.g. Player B +3.5 games>
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
- [research/prompts/1_sports/TENNIS.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/research/prompts/1_sports/TENNIS.md) — **in full**: the tennis sport file
- [RESEARCH_CHECKLISTS.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/RESEARCH_CHECKLISTS.md) — the *Tennis* section and *Every sport*
- [SOURCES.md](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/SOURCES.md) — §3.10 (tennis), plus §1 (rules every source follows) and §2.1-§2.2 (ESPN site API, weather)
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
- [RULES_TENNIS](https://raw.githubusercontent.com/danisgreat/Sports-Research/main/RULES_TENNIS.md) — the playing and settlement rules for this sport
- The active mini named in CURRENT_STATE (`research/active_minis/<MINI_KEY>.md`): search it for this game (native ID, teams, date) to avoid a duplicate, and take its next local key and its footer.

If a file cannot be read, say which, keep going with what you have, and never pretend to have read it.

## D. Order of work

1. **Identity and timing.** Resolve the competition, season, stage, both participants, venue, native ID and the official scheduled start (venue-local, UTC, Australia/Sydney). State each supplied contract's unit, period and settlement rule (overtime, extra time, push, void, retirement) before pricing; an ambiguous contract is priced under each reading and flagged.
2. **Duplicate check** in the active mini. An existing card gets a dated addendum, not a new card.
3. **Tier and reference, before any research-based number.** Print the tier (A, B or C) and the reference as section 3 of your answer *before* you research availability. If the owner pasted a Reference block, copy it verbatim; it is never edited. Otherwise compute it yourself as below, printing every input with its source and retrieval time, and mark the reference ID with the suffix `:HAND`.
   - **No reference:** tier C, `NONE`. The card's own first estimate is the Elo chain of PROBABILITY_TOOLKIT §6: Tennis Abstract Elo, a 50/50 blend of the surface rating and the overall rating, with the page's date. Game and set contracts come from the exact point-to-match recursion. The card record is weakest in tennis: abstain readily.
   - Also compute the league-only baseline (`BASELINE_P`, SELECTION_RULES §9) for every supplied contract from the competition row or family prior, or give its exact missing reason.
4. **Research**, value-ranked (section E): the H rows first, timed to when they are published, then M, then L. Every decisive fact needs a source URL, its publication time, your retrieval time and a second independent source. Keep searching alternatives before calling anything a gap.
5. **Adjust.** One adjustment-ledger row per confirmed fact, sized only from an EFFECT_TABLES row, with its entry (FULL, HALF or SCENARIO). Adjustments run at HALF size until the framework has measured their value. Do not count an effect the reference already contains (the standings already contain past injuries and form). A feeling is not a row.
6. **Price** every supplied contract from **one** score distribution: the reference centre plus the adjustments, with widths never below the competition floor. Keep the win, push and loss masses; complementary rows must agree.
7. **Select** (section G) and **write** the output (section H).

## E. What to research for tennis, in order of value

| Value | Input (both sides) | When it is published | Where (verified routes; see SOURCES) |
|---|---|---|---|
| H | Both players' overall and surface Elo, with the report date | Weekly | tennisabstract.com Elo reports (ATP and WTA) |
| H | Fitness and workload: recent injuries, retirements and withdrawals, matches and sets in the last 7-14 days, time on court, a late finish the night before | Tournament news; order of play | ATP and WTA sites; the tournament's order of play and draw PDF; official player statements |
| M | Serve and return on this surface: hold %, break %, first-serve in and points won, second-serve points won, return points won, over the last 52 weeks and the last three months | Continuous | Tennis Abstract player pages; ATP and WTA statistics |
| L-M | Conditions: indoor or outdoor, court speed, altitude, balls; best of three or five; the final-set tie-break rule | Tournament facts | Tournament site |
| L | Head-to-head (context only; small samples) | - | ATP and WTA head-to-head pages |

**Every sport, also:** the venue and whether it is neutral; the stage and format; weather for outdoor play in venue-local time for the match window (the 30-60 minutes around the start, during and after; downgrade only for weather in that window); travel and congestion; each side's last 5, 10, 15 and 20 results with dated game rows (date, opponent, venue, final and regulation score, source URL, retrieval time), true n, and the season and home-or-away splits. The four windows overlap and are one piece of evidence: a short-window swing is width, not a lean, unless a named current cause explains it (the framework found no bounce-back or streak effect in six leagues).

**Availability, for both sides** (ROSTER_AVAILABILITY_PROTOCOL): starters and roles, the selected bench or replacements, injuries, illness, suspensions, rest and late changes, from the official match record, both clubs, the league's medical or eligibility lists, then permitted structured providers, then local-language sources for less-covered competitions. A projected line-up, depth chart or roster page is not a confirmation. Re-check at the official release window and again just before you finish; re-price if anything changed.

## F. What to compute

- The match-win probability from the Elo chain; then each player's probability of winning a point on serve, chosen so that the exact recursion reproduces that match probability and the players' observed hold and break rates; state both.
- From the recursion: the set-score distribution, total games, game handicaps and set handicaps, each from the same chain (a game handicap and the match winner are different questions).
- The match-level form shock (games per match are more spread out than independent points predict) has no estimated sigma yet: widen totals and say so.
- For every ranked row, the line's distance from the centre in standard deviations (`z`), so easy lines are visible as easy.

**Simulation.** Tennis is exact: point → game → set → match recursion. No Monte Carlo is needed. If your tools cannot run code, do not simulate: say so and use the exact method. If they can, simulate only the contracts in SIMULATION_PROTOCOL §2 and print the seed, N (at least 100,000) and the Monte Carlo standard error.

**Traps in this sport:**
- Retirements and walkovers follow the contract's settlement rule; state it before pricing.
- Best of three against best of five; the final-set tie-break format.
- Qualifiers and lucky losers have thin data: abstain readily.

**Settlement convention:** Official ATP, WTA or ITF result; a retirement or walkover is graded by the contract's stated rule, otherwise UNRESOLVED.

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
6. **Tennis statistics** from section E and F, each with its source and date.
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


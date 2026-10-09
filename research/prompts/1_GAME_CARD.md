# PROMPT 1 — GAME CARD (one event, appended to the active local mini)

**Run by:** external chat agent · **GitHub:** read only · **Output:** one card appended to the active local mini · **Mode:** `LOCAL_MINI_STAGING` · **Format:** `mini-log-4`

How to use: paste **Part A (common core)** and then the **one sport block** from Part B that matches the event. Fill in the `<…>` fields. The core governs; a sport block adds the sport's research list, the distribution to build, the rules, sources and past-results files to open, and the family checks. Nothing here needs code: calculate by hand from the formulas and tables in the repository and show the working.

---

## PART A — COMMON CORE (paste with every sport)

**Scope.** Research and write one card. Do **not** settle, grade, run a retrospective, change methodology or write to GitHub.

### A0. Reading gate (before any research)

Use only current `main` of `https://github.com/danisgreat/Sports-Research`. Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening, in full:

- [CURRENT_STATE.md](../../CURRENT_STATE.md) (method, control revision, next canonical ID, active Combined Log), [METHOD.md](../../METHOD.md), [CURRENT_RULES.md](../../CURRENT_RULES.md) (Rules T2, R1, P4; reading gate §1), [SELECTION_RULES.md](../../SELECTION_RULES.md) (gate §2, top two §3, families §4, ladders §5, regimes §6, codes §7, failure classes §8), [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) (the `mini-log-4` card §3 and the card self-audit §7);
- the sport's rules file named in the sport block, and the sections of [PROBABILITY_TOOLKIT.md](../../PROBABILITY_TOOLKIT.md), [BASE_RATES_REGISTER.md](../../BASE_RATES_REGISTER.md) and [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md) the sport block names;
- the sport's table in [SOURCES.md](../../SOURCES.md) and its reachability matrix, §1.3 (freshness), §1.4 (the firewall) and §1.5 (lineups and late news);
- [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md);
- [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md) (existing canonical events) and [research/prompts/examples/EXAMPLE_ACTIVE_MINI.md](examples/EXAMPLE_ACTIVE_MINI.md) (exact card structure);
- then the **active local mini** in full.

A mini that carries `<!-- MINI-LOG-FORMAT: mini-log-3 -->` or `mini-log-2` is still valid: write the card in that mini's own format ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §1 lists the differences; legacy examples are in `research/prompts/examples/legacy_mini_log_2/` and the archived prompt examples) and tell the user that new minis use `mini-log-4`. If a document cannot be opened, say so and stop.

### A1. Identity and ID gate

1. Confirm the exact event: competition, season, stage or round, teams or players, venue, scheduled start (official source, with its time zone and update time), and the native event ID where one exists.
2. Build the event key: `<LEAGUE>:<SEASON>:<native-id or a stable surrogate>:<YYYY-MM-DD local event date>`.
3. **Duplicate check.** Search the active mini (cards and carryovers), [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md) and the active Combined Log header for the event key and the team names. If the event already appears, do not create a card. Write a dated addendum under the existing ID instead (A8).
4. **ID.** Use the mini footer's `Next local working P-ID`. If the repository's next canonical ID in CURRENT_STATE is now **above** that number, stop and tell the user: a canonical card was written outside the mini lifecycle and must be reconciled first. Never invent, skip or reuse an ID.

### A2. Research and retained evidence

- Use official league, team and statistical sources first, then independent high-quality sources, following the route and fallback in the sport's SOURCES table. Record each source with what it supported and when it was read. When the first-choice route is unreachable, use the listed fallback and write `(fallback: <source>)` in the Evidence cell.
- Research as close to the start as practical. Lineups, starters, goalies, quarterbacks and late scratches change forecasts (SOURCES §1.5).
- **SPORTS_ONLY / MARKET_BLIND** (SOURCES §1.4). No odds, line movement, tips, betting previews, prediction markets or fantasy data in research, ranking or probabilities. Supplied lines are only contract thresholds.
- **Timing state:** `PREGAME` (state verified as not started at research completion), `LATE_START_UNVERIFIED` (scheduled start passed or state unknown), or `LIVE_OBSERVED`. If the event has started, never use observed scores, events or statistics as inputs, and say so.
- Make no unsupported claims. Mark every unverified item ("probable, not confirmed") and model the uncertainty instead of assuming the favourable case.
- **Evidence quotes (`Evidence quotes` bullet).** For each lineup, goalie, starter, injury or weather page the card relies on, record `<source> @ <ISO time you read it, with offset> — "<verbatim excerpt of up to 200 characters>"`. The quote is the audit trail; hashes no longer exist. A card whose Rank 1 rests on a lineup or goalie claim cannot be written with `NONE`.
- **Settlement fields and capture time.** Name the exact field each pick settles on and the provider that publishes it (`Final score including OT/SO (provider: <name>)`). A corners, half-time, period or player row is allowed only with `provider: <name>` and a `Capture due` time within 36 hours after the scheduled start, so the page is captured before it rots.
- **Contract definitions.** Fill `Retirement rule`, `Listed-pitcher rule` and `Abandonment rule` with `N/A`, `FRAMEWORK_DEFAULT: <rule>` or `OPERATOR: <name>: <rule>`. Never guess a definition the operator has not supplied.
- **Regime flags.** Set `Regime flags` from the regime table in BASE_RATES_REGISTER (SELECTION_RULES §6). Apply the table's `Recommended` multiplier only; where it reads 1.000, do not shift the distribution.

### A3. The archive check (past results)

Open the files the sport block names under `Previous Sports Results/` and the league's row in [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md), and do the recipes in [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md) §4 that bear on this event: league level (R1), both teams' form before the date (R2), line frequency for the lines you will price (R5), rest (R6), venue and home edge (R7), extras and tails (R8). Use only rows dated before your research time (§3 there). Print the numbers in appendix A3 and A4 and fill the `Archive check` bullet. If the files are header-only or missing, write `ARCHIVE_UNAVAILABLE: <exact reason>` and use the fallback the guide names. The archive never replaces confirmed lineups, starters, goalies and weather.

### A4. Build one event distribution (probabilities are mandatory)

- Build **one** joint distribution of the sporting outcome for the stated endpoint, using the sport block's method and the tables in PROBABILITY_TOOLKIT. Name it in `Distribution object` as `<family>_<method>_v<n>` followed by its parameters (for example `hockey_poisson_ot_v1 — λ 3.10 / 2.70, OT home 52%`). Every probability in the pick table is read from that grid, and each row's `Probability status` reads `FROM_DISTRIBUTION:<that id>`.
- No fitted model exists. Set `Analysis status` to `UNCALIBRATED_ANALYST_SCENARIO`. It is still mandatory and must be explicit, reproducible and honest about uncertainty. Never call it validated.
- Resolve the contract endpoint inside the distribution: regulation versus OT, shootout, extra innings or extra time, ties, retirement and abandonment conventions. A full-game row must not leave a draw unresolved.
- **Adjustments are parameters, not nudges.** Any analyst change to a distribution input is listed in the adjustments table of the appendix (name, target, size, size in SD units, basis `fitted | archive_estimate | analyst_judgement`). If an adjustment above 0.25 SD changes which two propositions are Rank 1 and Rank 2, print `**Unadjusted top two:** <rank 1>; <rank 2>` and label the card `ADJUSTMENT_DEPENDENT`. Otherwise label it `NONE`.
- Run at least one sensitivity case on the most uncertain input (goalie, starter, pace, lineup) and report how the top two move.
- Show the arithmetic: the inputs, the formula or table section used, and the grid or the key cells, so a reader can reproduce each priced line.

### A5. Candidates and the top two (Rule P4, SELECTION_RULES §2 to §5)

1. Price every **supplied** contract from the distribution. Supplied contracts are reference only: use one only if it is among the best-suited or most likely once ranked.
2. Price the strongest **analyst-derived** propositions from the same distribution: winner or double chance, handicap or spread, match total, team total and period total, on the sport's standard ladder (SELECTION_RULES §5). Exclude degenerate rows above **90%**. `p_card` is win ÷ (win + loss); a push leaves the denominator.
3. Choose **exactly four candidates** and **rank them by `p_card`**, highest first. Never rank by q, edge or narrative.
4. **Rank 1 and Rank 2 are the picks** (only they can count as wins, Rule T2). Ranks 3 and 4 are informational.
5. **Rank-1 gate.** Rank 1 passes when `p_card` is at least **62%** and it leads the best non-complementary alternative (not the opposite side of the same line) by at least **4 points**. Print `**Rank-1 gate:** PASS` or `RANK1_UNSTABLE` with the numbers, recomputed. A failing gate is not an error: the card is scored in its own cohort, and you say why no stronger proposition exists.
6. **Rank 2** is the remaining row with `p_card` of at least **58%** that minimises P(Rank 1 and Rank 2 both lose), computed from the joint grid by the case in SELECTION_RULES §3 (never assumed independent). Print that probability. If it exceeds **35%** the two picks share one driver: replace the weaker pick with the best less-correlated candidate, re-rank by `p_card`, and say what changed. Rows from different outcome spaces have no exact joint: use the conservative bound min(P(lose 1), P(lose 2)) and say so.
7. Apply the sport block's **family checks** and the family rules in SELECTION_RULES §4, and record the result of each in appendix A7.

### A6. Write the card in exact `mini-log-4` form

The card has two parts. The **decision block** is the page you would act on (about 650 words at most): the distribution line, the pick table, the six bold lines. Everything else goes in the **appendix**. Insert the card **immediately before `# RUNNING FOOTER`**. The master template is [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §3; this copy is for pasting, and the template page controls if they differ.

```markdown
<!-- BEGIN CARD P-NNN -->
## Card · P-NNN · <SPORT / LEAGUE> · <Away @ Home | Player A vs Player B> · <YYYY-MM-DD>

- **Working ID:** `P-NNN — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `<LEAGUE>:<SEASON>:<native-or-surrogate>:<YYYY-MM-DD>`
- **Native event ID:** `<id>` or `NOT_VERIFIED`
- **Sport:** `<Baseball | Cricket | Basketball | Ice hockey | Tennis | Soccer | Rugby league | Rugby union | Australian rules | American football>`
- **League:** `<league>`
- **Tracking alias:** `LOCAL-<YYYYMMDD>-P-NNN-<LEAGUE>-<AWAY>-<HOME>`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME | LATE_START_UNVERIFIED | LIVE_OBSERVED`
- **Research completed:** `<ISO 8601 with offset>`
- **Scheduled start:** `<ISO 8601 with offset>`
- **Endpoint:** `<exact endpoint, incl. OT/SO/extras/retirement convention>`
- **Distribution object:** `<id> — <parameters, one line>`
- **Regime flags:** `NONE` or a comma-separated list
- **Retirement rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Listed-pitcher rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Abandonment rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Settlement fields:** `<field> (provider: <name>)`
- **Capture due:** `<ISO 8601 with offset, after the start and within 36 h of it>`
- **Rules read:** `<documents and sections applied, e.g. RULES_BASEBALL §3 §8; SELECTION_RULES §2-§4; SOURCES §3.1; BASE_RATES §5>`
- **Archive check:** `<file(s) · rows read · date range · recipes · finding>` or `ARCHIVE_PARTIAL: …` or `ARCHIVE_UNAVAILABLE: <exact reason>`
- **Evidence quotes:** `<source> @ <ISO time> — "<verbatim excerpt>"; …` or `NONE`

### Decision block

**Distribution:** `<id>` — <parameters>; <how the ladder was priced>.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | SUPPLIED or ANALYST_DERIVED (replaces …) | <exact proposition, line, period, endpoint> | <xx.x%> | FROM_DISTRIBUTION:<id> | <key evidence> | <main failure route> |
| 2 | PICK | … | … | … | FROM_DISTRIBUTION:<id> | … | … |
| 3 | INFORMATIONAL | … | … | … | FROM_DISTRIBUTION:<id> | … | … |
| 4 | INFORMATIONAL | … | … | … | FROM_DISTRIBUTION:<id> | … | … |

**P(Rank 1 and Rank 2 both lose):** <xx.x%>
**Rank 1 − Rank 2 gap:** <x.x points>
**Rank-1 gate:** PASS | RANK1_UNSTABLE — p_card <xx.x%>; best non-complementary alternative <xx.x%>; margin <x.x points>
**Adjustment dependence:** NONE | ADJUSTMENT_DEPENDENT
**Supplied rows not selected:** <each with its p_card from the same distribution>
**Potential winner:** <name> — <xx.x%> (<endpoint>)

### Appendix

#### A1. Identity, timing and state
#### A2. Supplied contracts (reference only, Rule P4)
#### A3. Evidence summary
#### A4. Event distribution
#### A5. Priced ladder (excerpt)
#### A6. Adjustments
**Adjustments:** NONE   (or the table | Name | Target | Size | SD units | Prior basis |, then `**Unadjusted top two:** …` when any adjustment exceeds 0.25 SD)
#### A7. Family checks
#### A8. Sources
#### A9. Integrity receipt
`SPORTS_ONLY_MARKET_BLIND: PASS` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD P-NNN -->
```

Format rules checked in the self-audit:

- Keep the pick-table header exactly as shown, with **four** data rows, roles `PICK, PICK, INFORMATIONAL, INFORMATIONAL`, every `p_card` a percentage, non-increasing order, no `q` column, and no `TO_FILL` placeholder in any cell.
- The pick table sits inside the decision block, which ends at `### Appendix`.
- No heading inside the card may start with a P-ID (`## P-…`), because the import step would read it as a new card.
- The bold lines are spelled exactly as shown. The gate's state must agree with the numbers it states.

### A7. Update the footer and audit

Replace the footer table: `Highest local working P-ID actually used` = this card's ID; `Next local working P-ID` = this ID + 1; `New event cards` + 1. Leave every earlier byte of the mini unchanged.

Then run the **card self-audit C1 to C20** ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §7) and print the table `| Check | Result | Evidence |`, with the number, quote or search result for each check. Fix every failure before returning. If you cannot edit the mini document in place, return the complete updated mini.

### A8. Corrections, late news and re-forecasts (no new ID)

To correct a non-substantive error, or to record material news before the start, append after the card (before the footer):

```markdown
<!-- BEGIN ADDENDUM P-NNN -->
### Addendum · P-NNN · <ISO 8601 time with offset>
<what changed, why, and whether the original ranking would change; the original card stays unchanged and is what gets graded>
<!-- END ADDENDUM P-NNN -->
```

- Place it after the card it amends and immediately before `# RUNNING FOOTER`. Leave the footer unchanged.
- The ID is the amended card's own ID. For a canonical event outside this mini (found in the duplicate check), use its canonical ID. The import step attaches the addendum to that card, or stops if none exists.
- The time must be ISO 8601 with a UTC offset. The body must not contain a new pick table or a heading that starts with a P-ID.
- An addendum never consumes an ID and never edits the original card. Settlement grades the original card only.
- **Re-forecast trigger.** A confirmed starter, goalie or quarterback change (or a lineup change large enough to move the ranks) that becomes public after your research time and before the start makes the card's ranks stale. A change qualifies when it moves a distribution input by more than 0.25 SD or reorders the top two. Write an addendum with the trigger, its source and time, and a re-priced table headed `| Rank | Proposition | p_reforecast |` (deliberately not the pick-table header). The original card is still what is graded.

### A9. Return

The complete card, the updated footer, the self-audit table, and:

```text
READING RECEIPT: <as printed in A0>
Working ID: P-NNN (LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT)
Repository next-ID snapshot read:
Duplicate check: none found / existing ID P-…
Timing state:
Distribution object:
Rank 1 / Rank 2 (p_card):
Rank-1 gate: PASS / RANK1_UNSTABLE
P(both picks lose):
Adjustment dependence: NONE / ADJUSTMENT_DEPENDENT
Potential winner:
Settlement fields and capture due:
Archive check: <files · rows · finding> / ARCHIVE_UNAVAILABLE: <reason>
Evidence quotes: <n> recorded / NONE
Self-audit C1-C20: all PASS / failures fixed: <list>
Settlement: NOT_PERFORMED · GitHub writes: NO
```

---

## PART B — SPORT BLOCKS (paste the one that applies)

Each block lists the files to open (**Open**), the research, the distribution and the family checks. Paths are relative to the repository root.

### B1. BASEBALL

Upcoming game: `<Away @ Home>`, `<League>` · Estimated start: `<date, time, time zone>` (can be delayed)
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_BASEBALL.md` (§3 model, §4 controls, §5 live state, §7 research sequence, §8 SFA-BASEBALL, §9 league rules); `PROBABILITY_TOOLKIT.md` §3 and §3.1; `BASE_RATES_REGISTER.md` §3 and §5; `LEAGUE_PROFILES.md` Baseball (MLB, KBO, NPB); `SOURCES.md` §3.1 (and §3.14 to §3.16 for the league's history); archive `Previous Sports Results/Baseball/<MLB|KBO|NPB>/<year>/<year>_games.csv` (`Away Score`, `Home Score`, `Total Runs`, `Extra Innings`, starting pitcher and line-score columns).

**Research:** confirmed starting pitchers (announced or posted lineup), starting lineups and handedness and platoon splits; pitcher form, pitch mix, velocity, workload and pitch counts; K% and BB%; bullpen quality, recent usage and unavailable high-leverage relievers; team offence (opponent-adjusted); park factor; weather and wind; travel and rest; the league's extra-innings and tie rules (RULES_BASEBALL and the official league).

**Distribution:** per-team runs as a negative-binomial (over-dispersed) mixture of the starter segment (expected innings × starter run rate) and the bullpen segment, adjusted for the opposing offence, park and weather, with a shared game-environment factor for covariance (use the league's dispersion phi and environment sigma from LEAGUE_PROFILES). Resolve ties at nine innings with the league's extra-innings rule, or keep a tie outcome where the league allows ties. Account for the home team not batting in the bottom of the ninth when leading.

**Family checks:**
- For any ±1.5 run line, print P(win) + P(lose by exactly 1). Compare with the league's one-run share in LEAGUE_PROFILES (MLB 28.2%, KBO 23.8%, NPB 33.7%). An underdog +1.5 near 0.60 has no edge by construction; four Rank-1 +1.5 rows failed in the 2026-10-09 cohort, and a +1.5 is not Rank 1 below 65% (SELECTION_RULES §4).
- Make the one-run share a function of the expected total: high-run environments widen margins.
- A starter change after research invalidates the card. Write an addendum (A8).

### B2. CRICKET

Upcoming match: `<Team A vs Team B>`, `<competition, format>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_CRICKET.md` and `LEAGUE_RULES_CRICKET.md` (format, playing conditions, DLS, super over, follow-on); `PROBABILITY_TOOLKIT.md` §1 and §7; `BASE_RATES_REGISTER.md` §6; `SOURCES.md` §3.3; archive `Previous Sports Results/Cricket T20/<competition>/<year>/<year>_games.csv`, `Cricket One-Day Format/...`, `Cricket Tests/...` (match results and innings totals; there is no cricket row in LEAGUE_PROFILES, so build the level from the files).

**Research:** confirmed XI (after the toss, where available); injuries and rested players; batting order, wicketkeeper, bowling attack and expected overs; batting and bowling form (opponent-adjusted), with powerplay, middle and death phases for limited overs; venue, pitch report and boundary dimensions; weather, rain and dew; toss status; batting-first and chasing effects; travel and rest; playing conditions.

**Distribution:** one format-specific model. Limited overs: ball and over resource model with wickets, phase scoring rates and the chase stopping rule (a chase ends when the target is reached). Tests: session and day run and wicket model with draw and weather branches. If the toss is unknown, weight both batting-order branches explicitly. Include a rain, DLS or reduced-overs branch.

**Family checks:**
- Innings or phase totals and the match result come from the same model. The second-innings total is capped near the target (RULES_CRICKET controls CR-P3 and 21).
- Never pair opposite-direction phase and total picks unless the joint win mass is shown (the P-217 lesson).
- State how runs scored before a stoppage settle (runs scored before a stop count).

### B3. BASKETBALL

Upcoming game: `<Home vs Away>`, `<League>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_BASKETBALL.md`; `PROBABILITY_TOOLKIT.md` §1 (totals §1.2, margins §1.3); `BASE_RATES_REGISTER.md` §3 and §7.1; `LEAGUE_PROFILES.md` Basketball (NBA, WNBA, NBL, EuroLeague, Greek Basket League; do not use the excluded leagues); `SOURCES.md` §3.2; archive `Previous Sports Results/Basketball/<NBA|WNBA|NBL|EuroLeague|...>/<year>/<year>_games.csv` (`Home Score`, `Away Score`, `Total Points`, `Overtime`, quarter or half scores).

**Research:** confirmed starters; injury report, game-time decisions and rested players; expected minutes and rotation; usage changes; offensive and defensive efficiency; pace; shot profile and three-point dependency; rebounding, turnovers and free-throw rate; matchup strengths; opponent-adjusted recent form; home and away splits; rest, back-to-backs and travel; series or playoff situation; league rule changes this season.

**Distribution:** possessions × points-per-possession. Use team pace and efficiency (opponent-adjusted) to produce a total mean, a margin mean, SDs and their correlation (normal or Student-t). Use the league's own scoring level, margin SD, total SD and correlation from LEAGUE_PROFILES, never NBA defaults for another league. Apply early-season shrinkage toward the prior-season league mean (fewer than about 5 games) and the early-season regime table. Resolve overtime in the full-game distribution (overtime share in LEAGUE_PROFILES).

**Family checks:**
- A totals pick needs the pace × efficiency centre printed. Three Rank-1 totals failed in the 2026-10-09 cohort because centres were typed in or shifted by judgment.
- Name any analyst adjustment as a parameter with its size. If removing it would change the top two, say so.
- The potential winner and every handicap come from the same margin distribution.

### B4. ICE HOCKEY

Upcoming game: `<Away @ Home>`, `<League>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_ICE_HOCKEY.md` and `RULES_NHL.md`; `PROBABILITY_TOOLKIT.md` §2 and §2.3; `BASE_RATES_REGISTER.md` §7.2; `LEAGUE_PROFILES.md` Ice hockey (NHL); `SOURCES.md` §3.9; archive `Previous Sports Results/Ice Hockey/NHL/<year>/<year>_games.csv` (`Home Score`, `Away Score`, `Total Goals`, `Decision Type`, `Overtime`, `Shootout`).

**Research:** confirmed starting goalies (if unconfirmed, model a goalie mixture), backup quality, goalie workload; scratches, forward lines and defence pairs; injuries; 5v5 expected goals and high-danger chances; shot generation and suppression; power play, penalty kill and penalty rates; finishing and save-percentage regression; rest, back-to-backs and travel; home ice.

**Distribution:** regulation goals as goalie-adjusted Poisson (or a bivariate variant). Resolve regulation ties with the league's overtime and shootout rules (a shootout adds one goal to the winner); about 22% of NHL games reach overtime (LEAGUE_PROFILES). Add an explicit late empty-net branch for one- and two-goal leads.

**Family checks:**
- State whether each row settles on regulation or the full game.
- A −1.5 or −2.5 puck line needs the margin distribution printed. P(margin ≥ 2) is about 60% and P(margin ≥ 3) about 40% of NHL games (LEAGUE_PROFILES), and larger margins are rarer (the P-200 lesson).
- An unconfirmed goalie blocks a fragile totals Rank 1.

### B5. TENNIS

Upcoming match: `<Player A vs Player B>`, `<Tournament, round>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_TENNIS.md`; `PROBABILITY_TOOLKIT.md` §6 (tennis Elo) and §1; `BASE_RATES_REGISTER.md` §6 and §7.4 (deciding-set reference rates); `SOURCES.md` §3.10; archive: the tennis yearly files are header-only, so write `ARCHIVE_UNAVAILABLE: Tennis yearly files are header-only` and use the SOURCES tennis routes (match statistics and the Sackmann files) for serve and return statistics.

**Research:** verified players, round, surface, indoor or outdoor, best-of-3 or best-of-5, qualifying versus main draw; injury, medical and retirement news; recent workload and match durations; rest and travel; surface-specific form; opponent-adjusted quality; serve points won, first- and second-serve performance, hold rate, aces and double faults; return points won and break conversion; tiebreak record; handedness and style; overall and surface Elo benchmark. Head-to-head matters only when surface, level, fitness and style are comparable.

**Distribution:** one point-to-match score tree. Use point-on-serve probabilities for each player (opponent-adjusted, surface-adjusted), exact game, tiebreak and set enumeration, and a **match-level form random effect**. The plain independent-point model over-states deciding sets: P-551 and P-555 were reproduced at 0.50 deciding-set mass where the reference is 0.358. Winner, games handicaps and games totals all come from this one tree.

**Family checks:**
- Print P(deciding set) beside the reference (ATP best-of-3 0.358, WTA 0.340; BASE_RATES §7.4 and RULES_TENNIS). Explain any gap above about 8 points.
- Totals between 19.5 and 25.5 games are mostly deciding-set bets; say so.
- At most one of the two picks may need a deciding set.
- Endpoint: a completed match. Under the framework convention a retirement voids games rows, and the winner settles to the advancing player.

### B6. SOCCER

Upcoming match: `<Home vs Away>`, `<Competition>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_SOCCER.md` and `LEAGUE_RULES_SOCCER.md` (competition format, extra time, tie-breaks); `PROBABILITY_TOOLKIT.md` §2.1 and §2.2; `BASE_RATES_REGISTER.md` §7.3; `LEAGUE_PROFILES.md` Soccer (EPL row); `SOURCES.md` §3.4 and the reachability matrix; archive: the soccer yearly files are header-only, so for the English Premier League open `research/data/processed/league_csv/epl_results.csv`, otherwise write `ARCHIVE_UNAVAILABLE: Soccer yearly files are header-only`.

**Research:** confirmed starting XI, goalkeeper and bench; injuries and suspensions; rotation (cup ties, congestion); tactical changes; xG and xGA; shots and shots on target; finishing and save regression; pressing and transitions; set pieces; home and away splits; opponent-adjusted form; rest and travel; weather and venue; competition incentives (aggregate state, table position, two-leg ties).

**Distribution:** a Dixon–Coles score matrix for 90 minutes plus stoppage time, with **separate first-half and second-half λ**. In EPL 2025-26, first-half goals were 1.19 of 2.75 per match, and P(first-half goal) was 0.716 (BASE_RATES §7.3). 1X2 (with the draw), first-half rows, totals, team totals and double chance all come from this one matrix. Corners need their own negative-binomial count model with score-state effects (EPL mean 10.0 per match, SD 3.27) and a named settlement provider. Extra time and penalties apply only if the contract says so.

**Family checks:**
- A first-half Over 0.5 at Rank 1 needs the half-split λ printed, `p_card` of at least 72% (SELECTION_RULES §4) and at least 5 points above the next candidate. Five Rank-1 first-half Overs failed in the 2026-10-09 cohort.
- For a rotated or cup favourite, discount first-half conversion: territory is not timing.
- A team-to-score probability above 80% needs both confirmed XIs and the implied λ printed.
- Four candidates only. The format and the top-two rule replace the older five-pick slate.

### B7. RUGBY LEAGUE / RUGBY UNION

Upcoming match: `<Team A vs Team B>`, `<Competition>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_NRL_RUGBY.md` (league) or `RULES_RUGBY_UNION.md` (union); `PROBABILITY_TOOLKIT.md` §1; `BASE_RATES_REGISTER.md` §7.7 and the finals and six-again rows of the regime table; `LEAGUE_PROFILES.md` Rugby league (NRL); `SOURCES.md` §3.6 (league) or §3.7 (union); archive `Previous Sports Results/Rugby League/NRL/<year>/<year>_games.csv` (scores, halftime scores, tries, goals, field goals); the rugby union yearly files are header-only (`ARCHIVE_UNAVAILABLE`).

**Research (league):** confirmed team list and late changes; spine (fullback, halves, hooker); forward pack and bench; metres per set and post-contact metres; line breaks and tackle breaks; ruck speed; completion and error rates; kicking and field position; red-zone attack; defensive efficiency; penalties and six-agains; rest, travel and weather.
**Research (union):** confirmed XV and bench; halves and goal-kicker; scrum and front-row matchup; lineout; breakdown; gain line; territory and kicking; discipline and cards; attacking entries; goal-kicking percentage; bench impact; rest, travel and weather.

**Distribution:** a score-event model: tries, conversions, penalty goals and field goals as count processes from team ratings, giving joint margin and total (NRL: try 4, conversion 2, penalty goal 2, field goal 1; key margins in LEAGUE_PROFILES). Knockout and finals games are tighter and lower-scoring, so apply the finals compression from the regime table (the P-534 lesson). Resolve golden point or extra time as the endpoint requires.

**Family checks:** print the margin distribution around key numbers. A handicap above about 4.5 in a near-even final needs explicit support.

### B8. AFL / AFLW

Upcoming game: `<Team A vs Team B>`, `<AFL | AFLW>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_AFL.md`; `PROBABILITY_TOOLKIT.md` §1; `BASE_RATES_REGISTER.md` §7.7 and the AFL rows of the regime table; `LEAGUE_PROFILES.md` Australian rules (AFL, AFLW); `SOURCES.md` §3.5; archive `Previous Sports Results/AFL/AFL/<year>/<year>_games.csv` or `AFL/AFLW/...` (`Game Score` text, `Total Points`, `Winning Margin`).

**Research:** final teams and late changes; injuries; midfield availability and ruck matchup; contested possessions; clearances and centre clearances; inside-50s; scoring shots and shot quality; goal accuracy and its regression; intercepts and turnovers; pressure and tackles; marks inside 50; defensive transition; venue; travel and rest; weather and wind; opponent-adjusted form.

**Distribution:** scoring shots per team (negative binomial, mean and dispersion from LEAGUE_PROFILES) × goal conversion (beta-binomial around 53% for AFL and 46% for AFLW), with points = 6 × goals + behinds. Keep shot creation separate from accuracy. Shrink unusual recent accuracy toward the league rate. Apply weather and wind to both creation and conversion.

**Family checks:** totals use the current competition era's scoring level (AFLW totals differ markedly from AFL). Print P(total ≤ line) from the shot × conversion model.

### B9. AMERICAN FOOTBALL

Upcoming game: `<Away @ Home>`, `<NFL | CFB | other>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_AMERICAN_FOOTBALL.md`; `PROBABILITY_TOOLKIT.md` §1; `BASE_RATES_REGISTER.md` §7.7 and the NFL rows of the regime table; `LEAGUE_PROFILES.md` American football (NFL profile and the absolute-margin table); `SOURCES.md` §3.8; archive `Previous Sports Results/American Football/NFL/<year>/<year>_games.csv` (`Game Score` text, `Total Points`, `Winning Margin`).

**Research:** starting QB, QB injuries and backup; offensive-line injuries; receivers, running backs and tight ends; defensive injuries; EPA per play and success rate; passing and rushing efficiency; pressure and sack rates; explosive plays; early-down efficiency; red-zone performance; turnover regression; pace and play volume; special teams; coaching and tactical changes; rest and travel; home field; weather and wind.

**Distribution:** drive-based discrete scoring. Model the number of drives and the drive outcome probabilities (0, 2, 3, 6, 7, 8 points) per team, giving a discrete joint score and margin. Key margins (3, 7, 10, 14) must emerge from the discrete model, not from a smoothed normal; compare with the NFL absolute-margin table in LEAGUE_PROFILES (margin 3 is 14.6% of games, margin 7 is 8.7%). Resolve overtime under the league's rule.

**Family checks:** print P(margin = 3) and P(margin = 7) beside any spread within 1 point of them. Re-forecast after any change of starting QB (A8).

---

## No fitted models

The Markdown-only framework has no fitted pipeline, calibrator or saved model. Every card is an `UNCALIBRATED_ANALYST_SCENARIO`. Winner-class, total and handicap probabilities all come from the one distribution you built by hand, and nothing is borrowed from another league. Never substitute a ranking q for a probability. Do not fabricate historical probabilities to populate a scoreboard. New rows keep their issued `p_card` values for later settlement and calibration scoring.

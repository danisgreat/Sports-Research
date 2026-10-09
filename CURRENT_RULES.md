# Current operating rules

**Method MDS-2026.10.09-v9.0 · Control revision CR-2026.10.09-R5 (Markdown only) · Scoring SCV-2026.10.09-v5.** What is true right now (next ID, active log, scoreboard) is in [CURRENT_STATE.md](CURRENT_STATE.md). This page states the rules. The pre-rewrite manual, with its dated status snapshots, is kept unchanged in [archive/superseded_2026-10-09/CURRENT_RULES.md](archive/superseded_2026-10-09/CURRENT_RULES.md).

## 0. The framework is Markdown

The whole framework is documents: rules, formats, prompts, sources, base rates, league profiles, probability tables and the archive of past results (CSV). Nothing here runs code or opens a JSON file, and no step needs one.

- **Forecasting and settling agents** read Markdown and CSV, browse and search the web, calculate by hand with [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), and write Markdown.
- **The repository agent (Claude Code)** edits Markdown and CSV with its file tools and uses `git` and plain file commands (`ls`, `cp`, `grep`, `wc`, `cmp`). It writes no scripts into the repository.
- The Python runtime, the validators, the importer, the freeze scripts and every JSON registry were removed on 2026-10-09 (commits `a64675cf7` to `a93352c30`; their last working state is commit `37203fc2b`). Their rules were moved into the documents listed in section 12. Where an old document still names a removed file, the instruction is historical and this page controls.
- Checks that code used to run are now **self-audit checklists** in [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md). The agent performs them and prints the evidence for each. A check that is listed but not shown is treated as not done.

## 1. Read before you forecast: the reading gate

Every task starts by opening the documents below **in the repository's current `main`** and printing a **reading receipt** (format in [research/prompts/README.md](research/prompts/README.md)). Do not rely on memory of earlier chats, stale downloads, Drive copies or other branches. If a required document cannot be opened, say so and stop.

| Task | Read in full | Read the relevant sections |
|---|---|---|
| Any task | CURRENT_STATE, METHOD, this page, [SELECTION_RULES.md](SELECTION_RULES.md), [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) | |
| A card | The sport's `RULES_<SPORT>.md` (soccer and cricket also `LEAGUE_RULES_SOCCER.md` / `LEAGUE_RULES_CRICKET.md`), [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) (the league's row), [SOURCES.md](SOURCES.md) (the sport's table and the reachability matrix) |
| Settlement | SCORING_AND_VALIDATION, the sport files for the sports in the mini | SOURCES (settlement routes), BASE_RATES (regimes) |
| Import, rollover, retrospective | The matching prompt in [research/prompts/](research/prompts/README.md), VERIFICATION_PROTOCOL | The active Combined Log header and footer, GAME_LOG_STATUS_CURRENT |

**Cite what you use.** A card lists the sections it applied in its `Rules read` bullet (for example `RULES_BASEBALL §3, §8; SELECTION_RULES §2-§4; SOURCES §3 KBO; BASE_RATES §5`). A rule that shaped a number is named next to the number. A rule that applied and was not used is a finding in the settlement (R9).

**Consult the past results.** Every card does an archive check ([ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) §5) and prints the `Archive check` bullet: files opened, rows read, date range, recipes, finding, or `ARCHIVE_UNAVAILABLE` with the reason. The archive never substitutes for confirmed lineups, starters, goalies and weather.

## 2. Rule T2: only the top two picks count as wins

1. A card ranks four candidates. **Rank 1 and Rank 2 are the card's picks.** Ranks 3 and 4 are informational alternates.
2. Ranks 3-4 are graded exactly and kept for calibration and learning. They never count as wins in card summaries, cohort summaries, win rates, hit rates or any performance statement. A rank-3/4 win never offsets a rank-1/2 loss.
3. Classify each settled card by its live top-two rows: `TOP2_ALL_WON`, `TOP2_SPLIT`, `TOP2_ALL_LOST` or `VOID`. Report counted wins over live top-two rows, Rank-1 W/L/VOID, Rank-2 W/L/VOID and Hit@2. VOID and PUSH rows leave the denominators; they are never losses.
4. The two picks share one event. They are not independent trials, and every card reports their joint failure probability.

## 3. Rule R1: a Rank-1 failure needs a deep retrospection

A Rank-1 LOSS carries a dated deep retrospection in the same settlement record. A settlement with a failed Rank 1 and no deep retrospection is incomplete. The eight parts:

1. **Claim:** the exact proposition, `p_card`, the evidence it was ranked on and the gap to Rank 2.
2. **What happened:** the endpoint and the mechanism that decided the row.
3. **Distribution check:** recompute the card's distribution by hand, locate the outcome in it (tail mass or z-score) and stress the decisive assumption.
4. **Knowability:** what was available at the cutoff, as against post-event only.
5. **Verdict:** variance, ranking or selection, model or distribution, data or source, contract or endpoint, timing, adjustment, with the share you assign to each.
6. **Own-top-two counterfactual:** what Rule P4 would have ranked first and second using cutoff information only.
7. **Failure class:** a class from [SELECTION_RULES.md](SELECTION_RULES.md) §8, linked to earlier cards with the same class.
8. **Proposed correction:** testable, with an acceptance criterion. It stays `PROPOSED_NOT_TESTED` and no weight changes on one event.

A Rank-1 VOID or PUSH needs no deep retrospection, but the reason is recorded.

## 4. Rule P4: supplied contracts are reference only; derive your own top two out of four

1. Contracts and lines supplied with a request are reference metadata. They do not fix the candidate set or the ranking.
2. Build the **event distribution first** (section 7). All candidate probabilities come from that one distribution.
3. Form exactly four candidates from (i) the supplied contracts at their supplied lines and (ii) analyst-derived sporting propositions priced from the same distribution: winner or double chance, handicap or spread, match total, team total, period total, on the sport's ladder ([SELECTION_RULES.md](SELECTION_RULES.md) §5). Each candidate states its exact proposition, line, period, endpoint and tag (`SUPPLIED`, or `ANALYST_DERIVED` naming the supplied row it replaces). Exclude propositions above 90%.
4. Rank by `p_card`: the probability the proposition wins on its sporting endpoint. Never rank by q, edge or narrative. A supplied contract is used only when it is the best suited or the most likely once the top two are ranked. Being supplied gives it no priority.
5. Apply the Rank-1 gate, the Rank-2 floor, the joint failure test and the family rules ([SELECTION_RULES.md](SELECTION_RULES.md) §2-§4).
6. SPORTS_ONLY / MARKET_BLIND holds (section 5). Analyst-derived lines come from the distribution and the standard ladder, never from an odds page.

## 5. Evidence, sources and honesty

1. **SPORTS_ONLY / MARKET_BLIND.** No odds, line movement, tips, betting previews, prediction markets or fantasy data enter research, ranking, adjustments or confidence. A user-supplied line is contract metadata. An after-event market figure is quarantined and informational.
2. **Identity first.** Confirm the competition, season, stage, teams or players, venue, scheduled start (official source, time zone, update time) and the native event ID. Build the event key `<LEAGUE>:<SEASON>:<native id or stable surrogate>:<YYYY-MM-DD local date>`. Unknown official IDs stay unknown.
3. **Source ladder.** Official competition or field owner; official team or participant; official structured statistics provider; independent high-quality corroboration. Use the route and fallback in [SOURCES.md](SOURCES.md) and write `(fallback: <source>)` when the first-choice route was unreachable. Review the exact field and event, not a page title.
4. **Independence.** Three websites that share a provider count once. Official status shows who owns a field; it does not prove independent collection. Say when independence is unknown.
5. **Evidence quotes.** For every lineup, goalie, starter, injury or weather claim a card relies on, record the source, the time you read it and a short verbatim excerpt (`Evidence quotes` bullet). A Rank 1 that rests on such a claim cannot be written with `NONE`.
6. **Timing.** Record the actual research time, the observed state and the source's own update time. States: `PREGAME` (verified not started), `LATE_START_UNVERIFIED`, `LIVE_OBSERVED`. If the event has started, never use observed scores, events or statistics as inputs. A stale 0-0 or an initialised inning cannot prove a pregame state. Late news is welcome; label it honestly and never backdate.
7. **No unsupported claims.** Mark every unverified item ("probable, not confirmed") and model the uncertainty instead of assuming the favourable case. Never invent a source, a quote, a number, a result or a hash. If you cannot compute a figure, write `NOT_COMPUTED`.
8. **Weather** is environmental evidence, not an independent sporting-event lineage.
9. **Settlement is from the feed, not from memory or narrative.** Settle from official scorecards and structured results. AI-generated or narrative match reports are not sources. Typed-in scores need a quoted source line.

## 6. Requested research: the controlling default

Research every requested event. A missing model, baseline, calibration, fixture universe, independence audit or pre-start buffer does **not** block analysis, ranked picks or a canonical ID. Give the best-supported assessment with its uncertainty and missingness. Use `UNCALIBRATED_QUALITATIVE` ranks (percentages `NOT_ESTIMATED`) only when no distribution can be built; otherwise build one and label it `UNCALIBRATED_ANALYST_SCENARIO`. Never call a scenario validated. Explain complementary totals, covering run lines, ties and extra innings; do not count correlated picks as independent games. A missing bookmaker rule affects later operator settlement, not the sporting analysis. No retrospective or settlement until requested. An ID identifies a retained card; calibration and certification are separate labels.

## 7. Probabilities: one distribution, built by hand

1. Build **one** joint distribution of the sporting outcome for the stated endpoint (the sport block in prompt 1 gives the method). Name it in `Distribution object` as `<family>_<method>_v<n>` with its parameters. Every `p_card` is read from that grid, and each row's `Probability status` reads `FROM_DISTRIBUTION:<id>`.
2. Start from the league profile ([LEAGUE_PROFILES.md](LEAGUE_PROFILES.md)) and the team and lineup evidence; calculate with the tables in [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md): normal (§1), Poisson (§2), negative binomial (§3), tennis (§6), cricket (§7), two rows at once (§9), arithmetic checks (§11). Show the formula and the inputs so a reader can reproduce each number.
3. Resolve the endpoint **inside** the distribution: regulation against overtime, shootout, extra innings or extra time, ties, retirement and abandonment. A full-game row must not leave a draw unresolved.
4. **Adjustments are parameters, not nudges.** List each in the adjustments table (name, target, size, size in SD units, basis `fitted | archive_estimate | analyst_judgement`). An adjustment above 0.25 SD that changes the top two makes the card `ADJUSTMENT_DEPENDENT`; print the unadjusted top two.
5. Apply the regime table once ([SELECTION_RULES.md](SELECTION_RULES.md) §6). Run at least one sensitivity case on the most uncertain input and report how the top two move.
6. Record win, push and loss mass; `p_card` = win ÷ (win + loss). Prices on the same line are complements; prices across lines are monotone. q (the historical ordering score) is never an event probability and never ranks a new card.
7. No fitted model exists in the Markdown-only framework. Every new card is an `UNCALIBRATED_ANALYST_SCENARIO`. More archived years alone do not establish calibration.

## 8. The local-mini lifecycle

New cards move through the prompts in [research/prompts/](research/prompts/README.md). The format is `mini-log-4` ([CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md)); `mini-log-3` and `mini-log-2` minis in progress stay valid and are finished in their own format.

1. **Start a mini (prompt 2).** The first working ID is the larger of the repository's next canonical ID and the previous mini's highest working ID + 1. Only `PENDING_EVENT` cards carry forward. Creating a mini consumes no ID.
2. **Write cards (prompt 1).** One event, one working ID, issued in order and never changed. The card carries the reading and archive bullets, one distribution, four priced candidates, the joint failure, the gate, the adjustments, the regime flags, the contract-definition fields, the settlement fields with a capture time and the evidence quotes. Corrections and late news are dated `ADDENDUM` blocks under the existing ID.
3. **Settle (prompt 3)** within 72 hours of each final with open carryover at or below 5. Freeze the mini, then append the settlement section. Settle every terminal event on the evidence hierarchy A/B/C/E/OP/X (X = VOID). Only a non-terminal event stays `PENDING_EVENT`. R1 copies the card's own ranking. Every settlement carries R1-R12, and every Rank-1 loss has the deep retrospection.
4. **Import (prompt 4, Claude Code)** appends each card, addendum and settlement to the active Combined Log under its working ID by hand edit, stopping on an identity conflict or ID collision, and updates the status register.
5. **Roll over (prompt 5)** when the active Combined Log should close. It consumes no ID.
6. **Retrospective (prompt 6)** once enough new cards are settled. Recommendations stay `PROPOSED_NOT_TESTED`.
7. **Expand or repair the archive (prompt 7)** and **improve the framework (prompt 8)** as needed ([PROMPTS.md](PROMPTS.md)).

## 9. Custody in a Markdown-only repository

- **The commit is the freeze.** Every published change is a git commit on `main`. A card records the `GitHub HEAD SHA` it read. There are no hash manifests; git history is the custody record.
- **Issued bytes never change.** Parts 1-5 of the Combined Log, the original P-518-P-522 block in Part 6, every issued card and every settled mini are append-only. Corrections are dated addenda under the original ID. Do not backdate, reformat or silently rewrite an original probability, contract, rank, cutoff or native identity.
- **Reserved IDs.** P-518-P-522 stay reserved. Never reuse, skip, invent or renumber an ID.
- **Frozen mini.** The settlement step copies the mini byte for byte (a file copy) before appending. The settlement header records the line count, the card IDs and the footer line as the check. When you can, confirm that the frozen file is an exact prefix of the settled file with `cmp`.
- **Line endings.** The Combined Logs are stored with Windows line endings. Before committing any change to a log, run `git diff --numstat` on it: removed lines must be **0**. If an earlier line changed, restore the file and re-append.
- **Duplicate events.** If an event key already appears in the mini, a Combined Log or the status register, write an addendum under the existing ID instead of a new card.

## 10. Learning, scoring and certification

- Historical rank logs and reconstructed views are learning-only. Blank cutoffs, baselines and grades are not zero. A source-linked literal is not an independently audited result.
- Scoring definitions, the Wilson interval and the week-block comparison are in [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md). A miss can be well calibrated and a win can come from a bad process; assess process and result separately.
- Opened data are development data. Preserve untouched future testing for release decisions.
- **Certification is suspended.** Model qualification, live admission and prospective-pilot protocols needed the removed runtime. Every record is `RESEARCH_ONLY_NOT_CERTIFIED`. A verified sporting result is not operator certification. The earlier protocol text is in the archived manual.
- Proposed changes live in [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) and need a pre-registered test.
- Fractional-Kelly staking and any use of prices are not part of this framework.

## 11. Change control

Rule changes bump the method or control revision here and in [METHOD.md](METHOD.md) and [CURRENT_STATE.md](CURRENT_STATE.md), add a dated [CHANGELOG.md](CHANGELOG.md) entry, move the replaced text into `archive/`, and are committed as one reviewable change. A prompt change does the same. Never change a rule on the strength of one event.

## 12. Where each rule now lives

| Former home (removed) | Now |
|---|---|
| `runtime/config/selection_rules.json` | [SELECTION_RULES.md](SELECTION_RULES.md) §1-§5 |
| `runtime/config/regimes.json` | [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) regime table; [SELECTION_RULES.md](SELECTION_RULES.md) §6 |
| Failure taxonomy and codes in `top_two.py` | [SELECTION_RULES.md](SELECTION_RULES.md) §7-§8 |
| `runtime/config/leagues/*.json`, `sports/*.json` | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) |
| `research/sources_registry*.json`, `excluded_sources.json`, `runtime/config/sources` | [SOURCES.md](SOURCES.md) (source register, adapters, exclusions) |
| `research/improvement_register.json`, `experiment_measures.json`, `cross_card_v1.json` | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| `research/current_combined_log.json`, `current_settlement_register.json`, `canonical_ledger.jsonl` | [CURRENT_STATE.md](CURRENT_STATE.md), [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), the Combined Log headers |
| `mini_log`, `settlement_lint`, `settlement_sla`, `card_validator` | Self-audit checklists in [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| `import_mini`, `log_card`, `rollover`, `cohort_review`, `scoreboard` | Prompts 4, 5 and 6 and [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Archive builders and canonical exports | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [Previous Sports Results/README.md](Previous%20Sports%20Results/README.md) |
| Control manifests and freeze scripts | Git commits (section 9); the old manifests are in `archive/controls/` |
| Numerical ML runtime and its model register | Archived design notes: [NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md), [H0_DATASET_CARD.md](H0_DATASET_CARD.md) |

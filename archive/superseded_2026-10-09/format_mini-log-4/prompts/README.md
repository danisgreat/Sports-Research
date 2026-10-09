# Operator prompts: the Markdown-only local-mini lifecycle

**Prompt set P-2026.10.09-v9 (Markdown only).** These prompts run the whole forecasting cycle without code. They were rewritten on 2026-10-09; the previous set, which called Python tools and JSON registries, is kept in [archive/superseded_2026-10-09/prompts/](../../archive/superseded_2026-10-09/prompts/). The numbering matches the operator's prompt files.

| # | Prompt | Who runs it | GitHub | Writes |
|---|---|---|---|---|
| 2 | [Start a new local mini](2_START_LOCAL_MINI.md) | External chat agent | Read only | New local mini (`.md`) |
| 1 | [Game card](1_GAME_CARD.md), one per event | External chat agent | Read only | One card appended to the local mini |
| 3 | [Settle the local mini](3_SETTLE_LOCAL_MINI.md) | External chat agent | Read only | Local settlement folder |
| 4 | [Canonical import](4_CANONICAL_IMPORT.md) | Claude Code in the repository | Write | Active Combined Log, status register, state, scoreboard, import report |
| 5 | [Start the next Combined Log](5_START_THE_NEXT_COMBINED_LOG.md), when the active part is full | Claude Code in the repository | Write | New Combined Log part, closure block, state |
| 6 | [Combined Log retrospective](6_COMBINED_LOG_RETROSPECTIVE.md), periodically | Claude Code in the repository | Write (report and scoreboard only) | Cohort report, scoreboard, recommendations |
| 7 | [Expand or repair the previous results](7_EXPAND_PREVIOUS_RESULTS.md), as needed | Claude Code in the repository | Write (CSV and coverage notes) | Archive CSVs and coverage documents |
| 8 | [Improve the framework](8_IMPROVE_THE_FRAMEWORK.md), as needed | Claude Code in the repository | Write (documents) | Rule, prompt and register changes |

```text
2 Start mini ─► 1 Card ─► 1 Card ─► … ─► 3 Settle ─► 4 Import ─► 2 Start next mini (next canonical ID) ─► …
                                                                   └─► 5 Roll over Combined Log (when needed)
                                                                   └─► 6 Retrospective (when enough cards are settled)
```

## What "Markdown only" means for every prompt

- Read Markdown and CSV, browse and search the web, calculate by hand with [PROBABILITY_TOOLKIT.md](../../PROBABILITY_TOOLKIT.md), write Markdown.
- Claude Code (prompts 4 to 8) edits files with its file tools and uses `git` and plain file commands only. It writes no script and runs no interpreter against the repository.
- Where a step used to run a validator, the prompt gives a **self-audit checklist** ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §7 and §9, [VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md)). Print each check with its evidence. A check listed and not shown is treated as not done.
- If a document the prompt names cannot be opened, say so and stop. Do not continue from memory.

## The reading gate (every prompt starts here)

Open the documents in the current `main` of `https://github.com/danisgreat/Sports-Research`, record the HEAD SHA, and print this **reading receipt** before doing anything else. The receipt goes at the top of the reply and, for prompts 1 to 3, into the mini (authority table `Reading receipt` row, card `Rules read` bullet, settlement header).

```text
READING RECEIPT
Repository / branch / HEAD SHA: danisgreat/Sports-Research · main · <40-hex> · read <ISO 8601 with offset>
Read in full: CURRENT_STATE · METHOD · CURRENT_RULES · SELECTION_RULES · CARD_AND_LOG_TEMPLATES · <the prompt file>
Sport files read in full: RULES_<SPORT> (+ LEAGUE_RULES_SOCCER / LEAGUE_RULES_CRICKET) · PROBABILITY_TOOLKIT <sections> · BASE_RATES_REGISTER <sections> · LEAGUE_PROFILES <league row>
Sources: SOURCES <section numbers> (routes used, fallbacks noted)
Past results: ARCHIVE_USE_GUIDE · <Previous Sports Results file paths opened, rows read, date range>
Not read or unavailable: <list with the reason, or "none">
```

Rules for using what you read:

1. **Cite as you go.** When a rule shapes a number or a decision, name it next to the number: "(SELECTION_RULES §2)", "(RULES_BASEBALL §8)", "(SOURCES §3.9 NHL)". The card's `Rules read` bullet lists the sections actually applied.
2. **Use the past results.** Every card performs the archive check ([ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md) §5) and every settlement and retrospective compares with the archive when it holds rows. `ARCHIVE_UNAVAILABLE` needs an exact reason.
3. **Use the source register, not memory.** Choose each source from [SOURCES.md](../../SOURCES.md) (first-choice route, then the listed fallback) and state the route in the evidence.
4. **When documents disagree**, [CURRENT_STATE.md](../../CURRENT_STATE.md) and [CURRENT_RULES.md](../../CURRENT_RULES.md) control, then [SELECTION_RULES.md](../../SELECTION_RULES.md), then the sport file. Report the disagreement; do not choose silently.

## Shared contract between the prompts

- **Format.** New minis are `mini-log-4` ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md)). Minis already started in `mini-log-3` or `mini-log-2` stay valid and are finished in their own format. The [golden example](examples/EXAMPLE_ACTIVE_MINI.md) and its [settled copy](examples/EXAMPLE_SETTLED_MINI.md) are the structure to copy.
- **IDs.** A card's local working ID is the P-ID it keeps forever. The first ID of a mini is the larger of the repository's next canonical ID and the previous mini's highest local ID + 1. The import step keeps every local ID or stops on a collision; it never renumbers.
- **Rules.** CURRENT_RULES Rules **T2** (only Rank 1 and Rank 2 count as wins), **R1** (a Rank-1 failure needs the eight-part deep retrospection) and **P4** (supplied contracts are reference only; four candidates priced from one distribution, ranked by `p_card`, at most 90%; Rank 1 passes the provisional gate of 62% and a 4-point lead, otherwise the card is `RANK1_UNSTABLE` and scored in its own cohort).
- **Current state.** [CURRENT_STATE.md](../../CURRENT_STATE.md) states the next canonical ID, the active Combined Log and the method. No other document states them.
- **Settlement SLA.** Settle every card within 72 hours of its final; open carryover stays at or below 5.
- **Settlement.** Settle every terminal event. Missing details settle on the evidence hierarchy A/B/C/E/OP/X, and a row with no admissible data is VOID. Only a non-terminal event stays `PENDING_EVENT` and carries forward.
- **Market blindness.** No odds, line movement, tips, previews, prediction markets or fantasy data in research, ranking or probabilities. A supplied line is contract metadata only.
- **Honesty.** No invented source, quote, number, result or hash. Unknown is written `NOT_COMPUTED` or `NOT_VERIFIED`.

## What the self-audits catch, and what they cannot

They catch: a duplicate or out-of-order ID; a reused event key; a missing metadata field; a pick table without four rows, with wrong roles, a missing or degenerate probability, or not ordered by `p_card`; a probability that does not come from the one declared distribution; a leftover `TO_FILL`; an oversized decision block; a gate label that disagrees with its numbers; an adjustment above 0.25 SD without the unadjusted top two; a corners, half, period or player row with no provider; a missing reading or archive line; a heading that would consume a canonical ID; a stale footer; an edited frozen prefix; a settlement whose proposition or `p_card` differs from the card; a wrong `Counts toward wins` value or top-two line; a missing R1 to R12; a missing deep retrospection or failure class.

They cannot judge whether the research was honest, the distribution sensible or the ranking wise. That is the job of the prompts and of the retrospective.

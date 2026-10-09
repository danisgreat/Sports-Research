# Operator prompts: the local-mini lifecycle

These six prompts run the whole forecasting cycle. The numbering matches the operator's prompt files.

| # | Prompt | Who runs it | GitHub | Writes |
|---|---|---|---|---|
| 2 | [Start a new local mini](2_START_LOCAL_MINI.md) | External chat agent | Read only | New local mini (`.md`) |
| 1 | [Game card](1_GAME_CARD.md), one per event | External chat agent | Read only | One card appended to the local mini |
| 3 | [Settle the local mini](3_SETTLE_LOCAL_MINI.md) | External chat agent | Read only | Local settlement folder |
| 4 | [Canonical import](4_CANONICAL_IMPORT.md) | Claude Code in the repository | Write | Active Combined Log, ledger, reports |
| 5 | [Start the next Combined Log](5_START_THE_NEXT_COMBINED_LOG.md), when the active part is full | Claude Code in the repository | Write | New Combined Log part, config, freeze |
| 6 | [Combined Log retrospective](6_COMBINED_LOG_RETROSPECTIVE.md), periodically | Claude Code in the repository | Write (report only) | Cohort report and recommendation register |

```text
2 Start mini ─► 1 Card ─► 1 Card ─► … ─► 3 Settle ─► 4 Import ─► 2 Start next mini (next canonical ID) ─► …
                                                                   └─► 5 Roll over Combined Log (when needed)
                                                                   └─► 6 Retrospective (when enough cards are settled)
```

## Shared contract between the prompts

- **Format.** Every mini follows format `mini-log-2` ([specification](../../CARD_AND_LOG_TEMPLATES.md#local-mini-format-mini-log-2)). The [golden example](examples/EXAMPLE_ACTIVE_MINI.md) and its [settled copy](examples/EXAMPLE_SETTLED_MINI.md) are validated by the test suite. When in doubt, copy their structure exactly.
- **IDs.** A card's local working ID is the P-ID it keeps forever. The first ID of a mini is the larger of the repository's next canonical ID and the previous mini's highest local ID + 1. The importer (prompt 4) keeps every local ID, or stops on a collision; it never renumbers.
- **Rules.** CURRENT_RULES.md Rules **T2** (only Rank 1 and Rank 2 count as wins), **R1** (a Rank-1 failure needs the eight-part deep retrospection) and **P4** (supplied contracts are reference only; four candidates priced from one event distribution, ranked by p_card, p_card ≤ 90%).
- **Settlement.** Settle every terminal event. Missing details settle on the evidence hierarchy A/B/C/E/OP/X, and a row with no admissible data is VOID. Only a non-terminal event (postponed, suspended, not yet played) stays `PENDING_EVENT` and carries forward.
- **Market blindness.** No odds, line movement, tips, previews, prediction markets or fantasy data in research, ranking or probabilities. A user-supplied line is contract metadata only.

## Local checks (optional, any machine with the repository)

```powershell
py -3.14 -B -m research.operations.mini_log verify "<mini>.md"
py -3.14 -B -m research.operations.mini_log next-id "<mini>.md" --repo-next P-NNN
py -3.14 -B -m research.operations.mini_log append "<mini>.md" "<card block>.md"
py -3.14 -B -m research.operations.mini_log addendum "<mini>.md" "<addendum block>.md"
py -3.14 -B -m research.operations.mini_log join "<ORIGINAL_MINI>/<frozen>.md" "<settlement section>.md" --out "<settled>.md"
py -3.14 -B -m research.operations.mini_log verify-settled "<ORIGINAL_MINI>/<frozen>.md" "<settled>.md" --out "<folder>"
py -3.14 -B -m research.operations.mini_log new --dir "<minis folder>" --previous "<previous settled mini>.md"
```

Each command prints JSON, and `"passed": true` (or no `errors`) means the file meets the format. `new` and `next-id` also read the repository's allocator, so run them from an up-to-date checkout of `main`. Where `py -3.14` is unavailable, use `python -B -m …` from the repository root.

## What the validators catch, and what they cannot

They catch:
- a duplicate or out-of-order ID;
- a reused event key;
- a missing metadata field;
- a pick table that does not have four rows, has wrong roles, has a missing or degenerate probability, or is not ordered by p_card;
- a heading that would consume a canonical ID;
- a stale footer;
- an edited frozen prefix;
- a settlement whose proposition or p_card differs from the card;
- a wrong `Counts toward wins` value or top-two line;
- missing R1–R12;
- a missing deep retrospection or failure class;
- a bad hash.

They cannot judge whether the research was honest, the distribution sensible or the ranking wise. That is the job of the prompts and of the retrospective.

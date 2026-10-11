# Canonical import of settled mini P-556 to P-579 — 2026-10-11

Mode `CANONICAL_SETTLED_MINI_IMPORT` (prompt 4, Markdown-only, no importer program). Base `main` = `origin/main` = `33d0ea0c1c70056db7c7fb0a07dec77a633e573f`. Active log: `prediction logs/PREDICTION_LOG_COMBINED_7.md`. Plan and classification: [IMPORT_PLAN.md](IMPORT_PLAN.md). Checks: [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md).

## Inputs

The packet `PREDICTION_CONTINUOUS_MASTER_SETTLEMENT_P-556_TO_P-579_2026-10-11.zip` (folder `Continuous Log Settlement - P-572 to P-579 - 2026-10-11/`), copied unchanged to [inputs/](inputs/): the frozen master (593,775 B, SHA-256 `3a406f539b43c982d1bfa8274d18be0d0670e73a59b10944ab6d90c5d48cc875`), the settled master (632,372 B; the frozen bytes are its exact prefix), the manifest, ID mapping, unresolved carryover, settlement report and self-audit, latest status, source receipt, the proposed pre-start lineup rule (local only, not adopted here) and the original P-572–P-579 card files.

## Classification

| IDs | Class | Action |
|---|---|---|
| P-556 | `ALREADY_IMPORTED_EXACT` | skipped; card and settlement already in Part 7 |
| P-557–P-576 | `NEW_CANONICAL_EVENT`, settled | card and settlement appended |
| P-577–P-579 | `NEW_CANONICAL_EVENT`, `PENDING_EVENT` | card appended without settlement; carried forward |
| P-578 A8 | addendum `TO_APPEND` | appended under P-578 |

Blocked: none. Identity mapping, no renumbering: local ID = canonical ID for all 23 ([CANONICAL_ID_MAPPING.csv](CANONICAL_ID_MAPPING.csv)).

## Appended blocks (Combined Log 7, after line 4,865)

1. **23 canonical cards** P-557 to P-579 in ID order, format `canonical-md-1`: `<!-- BEGIN CANONICAL RESEARCH P-NNN -->`, the heading `## P-NNN — <SPORT / LEAGUE> — <Event> — <date>` (the card's `## Card · …` heading with `·` separators written as `—`), the import note, then the card lines from `- **Working ID:**` to the line before `<!-- END CARD P-NNN -->` byte for byte, and the closing marker.
2. **1 pre-settlement addendum**: P-578 A8 as `<!-- BEGIN RESEARCH ADDENDUM P-578 20261011-1 -->`; its content (source lines 3792–3849) verbatim, with an import note naming the original marker token `A8-20261011-210851`. Its own marker lines were replaced so that no addendum marker is nested inside another.
3. **20 settlement addenda** P-557 to P-576 in ID order, each `<!-- BEGIN RESEARCH ADDENDUM P-NNN 20261011-1 -->`, headed `**Final settlement (<date>).**` with the date the local settlement read its sources (P-557–P-560 2026-10-09; P-561–P-563 2026-10-10; P-564–P-576 2026-10-11), then the settlement block verbatim including its own `BEGIN/END SETTLEMENT` markers.

Totals: 44 blocks, 3,853 lines, 609,025 bytes. Line endings were converted from the mini's LF to CRLF, the Combined Logs' stored form (CURRENT_RULES §9); no other byte differs. Method: the blocks were assembled from exact line ranges of the packet file in a scratch directory outside the repository, every block was compared with its source slice (44 of 44 identical), and the result was appended with a single file concatenation so that no card text was retyped.

## Other files changed

- `GAME_LOG_STATUS_CURRENT.md`: `Next canonical ID` P-557 → **P-580**; 23 new rows after P-556; the `Highest canonical research ID` line P-556 → P-579 (it states the same fact as the next-ID line). 25 lines added, 2 changed; the register's existing CRLF and LF lines are preserved byte for byte.
- `CURRENT_STATE.md`: highest committed ID P-579, next ID P-580, the settlement note and the scoreboard headline.
- `research/scoreboard/SCOREBOARD.md`: updated by hand (SCORING_AND_VALIDATION §7).
- This folder.

## Rule T2 numbers (re-derived from the appended settlement blocks)

| Batch | Cards | Counted | Rank 1 W–L–V | Rank 2 W–L–V | Hit@2 | Mean NDCG@2 | Winner calls |
|---|---:|---|---|---|---|---:|---|
| P-557–P-560 (settled 2026-10-09) | 4 | 6/8 | 3–1–0 | 3–1–0 | 4/4 | 0.7500 | 2/4 |
| P-561–P-563 (settled 2026-10-10) | 3 | 6/6 | 3–0–0 | 3–0–0 | 3/3 | 1.0000 | 3/3 |
| P-564–P-566 (settled 2026-10-11) | 3 | 5/6 | 2–1–0 | 3–0–0 | 3/3 | 0.7956 | 2/3 |
| P-567–P-571 (settled 2026-10-11) | 5 | 8/10 | 4–1–0 | 4–1–0 | 5/5 | 0.8000 | 1/5 |
| P-572–P-576 (settled 2026-10-11) | 5 | 9/10 | 4–1–0 | 5–0–0 | 5/5 | 0.8774 | 2/5 |
| **All imported settled cards** | **20** | **34/40 (85.0%)** | **16–4–0** | **18–2–0** | **20/20** | **0.8387** | **10/20** |

The P-572–P-576 line equals the settlement section's own tallies (9/10; Rank 1 4/5; Rank 2 5/5; NDCG@2 0.8774; winners 2/5). Card classes: 14 `TOP2_ALL_WON`, 6 `TOP2_SPLIT`, 0 `TOP2_ALL_LOST`. Ranks 3–4 (informational): 31–9. Evidence grades on the 80 graded rows: A 32, B 28, C 20.

Rank-1 failure classes: `OVERCONFIDENT_PROBABILITY` × 4 (P-560, P-564, P-571, P-576), each with the eight-part deep retrospection. Every card recorded `RANK1_UNSTABLE` before its event, so all 20 enter the `RANK1_UNSTABLE` cohort; the gated counted cohort stays at 0.

Most top-two pairs are bracketing totals or covering handicaps whose joint failure is 0% by construction (each card says so), so the counted rate describes this rank structure and is not evidence of independent forecasting skill.

## Scoreboard after import

Gated counted cohort 0/0. `RANK1_UNSTABLE` cohort 34/40 = 85.0% (95% interval 70.9–92.9%). All forecast cards 113/174 = 64.9% (57.6–71.6%); Rank 1 56–32, Rank 2 57–29, ranks 3–4 106–67. Spot-checked P-559, P-564, P-570, P-574 and P-576 against their settlement blocks in the log: classes, grades, evidence codes and deep-retrospection presence agree.

## Carried forward

P-577, P-578 and P-579 are canonical cards with no settlement; their settlement belongs to the next mini ([UNRESOLVED_POST_IMPORT.md](UNRESOLVED_POST_IMPORT.md)). Next canonical ID: **P-580** (the first working ID of the next mini).

## Not changed

Methodology, rules, earlier forecasts, probabilities, ranks, timestamps, historical grades, Parts 1–6, the Part 7 header and every earlier block of Part 7. Nothing was researched, re-settled or re-written. Imported records stay `RESEARCH_ONLY_NOT_CERTIFIED`; a verified sporting result is not operator certification or pregame performance eligibility.

## Pre-existing gaps reported unchanged

- Part 7 header line 10 still reads "Highest committed canonical ID: P-549. Next available canonical ID: P-550." It is the immutable opening header; CURRENT_STATE and GAME_LOG_STATUS_CURRENT control (see IMPORT_PLAN.md). Prompt 4 step 1.2 and prompt 5 step 3 compare against it and will report the same disagreement on every later run until the prompts or the header convention are changed (prompt 8).
- Format and evidence limits carried by the cards and settlements themselves: P-557–P-560 `mini-log-3` (no expected score); P-560 shows 90.0% for 89.9933%; P-568 winner mass 98.0%; P-579 `Rules read` without a HEAD SHA; five cards settled only on evidence C (P-560, P-564, P-566, P-572, P-573); late or unverified start times and unconfirmed lineups as stated on each card.
- `GAME_LOG_STATUS_CURRENT.md` lines 49–50 still describe the 2026-10-09 register ("72 event records … 0 sporting settlements open"); they were outside this step's edit scope. The new rows and CURRENT_STATE record the three open carryovers.
- Part 7 is now about 1.26 MB, close to Part 6 (1.34 MB). Consider prompt 5 (start the next Combined Log) before the next import.

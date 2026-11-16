# Implementation · v25.0 / CR-2026.11.16-R2 · 16 November 2026

Prompt 8, LOCAL_WORKING_TREE, base HEAD `c1d0403ed`. Owner order, 16 November 2026: "implement all the other of your updated recommendations"; and "its fine if you have to take from sources that have prices included, just strip them for the prices, and only take the data, add this to your rules if needed". Proposal: [CHANGE_PROPOSAL](../framework_change_2026-11-16-1/CHANGE_PROPOSAL.md). Classification: FORMAT (the chat card's closing block) + measurement policy + PROCEDURE, so the method and prompt major versions move.

| Identity | Before | After |
|---|---|---|
| Method | MDS-2026.11.15-v24.20 | MDS-2026.11.16-v25.0 |
| Control revision | CR-2026.11.16-R1 | CR-2026.11.16-R2 |
| Prompt suite | P-2026.11.15-v24.18 | P-2026.11.16-v25.0 |
| Scoring | SCV-2026.11.15-v15 | SCV-2026.11.16-v16 |
| Selection | SEL-2026.10.22-v4 | unchanged |

## What was implemented in this release

| Proposal | What now exists | Where |
|---|---|---|
| M-1 cohort | ONE-CHAT-v1 registered before any game: first 100 eligible games by settlement; the five-lane plan takes no new game | [EVALUATION_PLAN_v25.0](../../external/EVALUATION_PLAN_v25.0.md), HYPOTHESIS_REGISTER |
| M-2 a number for every line | A line is priced on every side or UNPRICED on every side; unpriced lines are kept, never ranked or scored; the priced share is reported | `ml/one_chat.py` `check` |
| M-3 fixed block | `ONECHAT_V1` block parsed as written; refused with reasons when incomplete or incoherent | `ml one-chat intake`, [brief](../../external/ONE_CHAT_BRIEF_v25.0.md) |
| M-4 comparator here | 0.5 on supplied lines computed at scoring; a frozen league base rate is paired through `--baseline` | `ml one-chat score` |
| M-5 custody | File hash and saved time recorded at intake; TIMING-v3 label from the card's clocks and the official first play; saved time reported as a stratum | CARDS.csv, COVERAGE.csv |
| M-6 metric | Game-mean Brier minus 0.25 with a t interval over games; criterion -0.01 with the interval below zero; PROGRESS, READY and AUDITED_ON_REQUEST | SCORING_AND_VALIDATION §15 |
| L-1 result captures | A settled grade needs its result page and the SHA-256 of the saved capture, or scoring refuses it; prompt 3 ingests those finals at import | prompt 3, `score` |
| L-2 facts block | The sport's required figures from FEATURE_DICTIONARY, per side, observed with source and time or MISSING with a reason | FACTS.csv |
| L-4 card clocks | `ml learning-status --card-rows` counts settled card games | `ml/learning_status.py` |
| G-1 freeze | FREEZE-v1 now runs to the ONE-CHAT-v1 assessment | CORE §8 |
| G-2 one version file | `VERSIONS.csv`; `ml state --restamp` prints it into the prompts and CORE; `ml state --write` into CURRENT_STATE | `ml/state.py` |
| G-3 text (part) | CORE dated paragraphs reduced to pointers: 27.7 KB to 25.7 KB with two rules added | CORE.md |
| G-4 one brief | One brief replaces the profile, lane briefs and audit supplement for new games | research/external/README.md |
| S-2 result source | Each line names the page that will publish its result or NONE_FOUND, flagged at intake | PICKS `result_source` |
| S-3 two sources | Prompt 3 asks for a second permitted source where one exists | prompt 3 |
| S-4 deep loss register | `research/deep_loss/DEEP_LOSS_REGISTER.csv` (21 reviews seeded), `ml deep-loss check|tally` | `ml/deep_loss.py` |
| S-5 access rule | The brief states the reader rule and the stats-only limit | brief §3 |
| K-2 | Prompt 6's opening line no longer says "this 21-game batch" | prompt 6 |
| Hypotheses | H-NODIR, H-BAND, H-AVAIL-CHAT, H-OWN-EVIDENCE, H-SPORT, H-PERIOD fixed as flags and splits before the cohort | plan, `ml/one_chat.py` |
| Owner rule | STATS-ONLY-v2: price-carrying sources used for sporting fields only, prices dropped at read | CORE §1, RULES_REFERENCE |
| Report addition | A calibration table and slope in every import report | prompt 4, §15 |

## Verification

- `ml/tests/test_one_chat.py` (19 tests): a complete card is admitted with its numbers unchanged; thirteen incomplete or incoherent cards are refused with the reason; unpriced leans, missing facts and whole-number lines are legitimate; one game keeps one card; PROGRESS, on-request and the frozen first hundred; unsettled, unpriced, post-start, outcome-exposed and uncaptured games do not count.
- `ml/tests/test_release_records.py`: VERSIONS.csv equals what CORE, the prompts and CURRENT_STATE print; restamp replaces only the previous suite; the committed deep loss register is valid; bad classes, verdicts, aliases, duplicates and sources are refused; the brief's worked example and the printed template parse.
- `ml/tests/test_learning_governance.py`: card clocks count card games and reset on a review.
- Full suite: count in the commit message.

## Effects on existing records

None. No issued card, grade, canonical ID, earlier registration, parameter or model changed. The 685 imported cards carry no `ONECHAT_V1` block and stay in their own cohorts; the new cohort starts with the first card that carries the block. The kit, the source lists and the request format (REQ-v5) are unchanged.

## Records work done under the same order

| Proposal | Result | Where |
|---|---|---|
| K-1 rollover | Part 10 closed at 1,530,426 bytes with 26 originals P-660–P-685; Part 11 opened; IDs unchanged | [receipt](../combined_rollover_2026-11-16-1/README.md) |
| S-1 unresolved queue | All 53 UNRESOLVED rows settled as revision-2 from the owner's located sources: 26 WIN, 27 LOSS; the effective view holds 0 UNRESOLVED; one deep loss review; CARD-TRAIN-v1 rerun | [report](../settlement_import_2026-11-16-1/CANONICAL_IMPORT_REPORT.md), [run](../../card_training/2026-11-16-1/REPORT.md) |
| L-3 stale releases | MLB-CYCLE-4, NHL-CYCLE-6 and NBA-CYCLE-4 RETIRED (registry entries 17 to 19) and removed from CURRENT_RELEASES.csv; tiers A to B; declared references unchanged | research/model_registry/MODEL_REGISTRY.csv |
| G-3 / K-3 state | CURRENT_STATE cut from 56.2 KB to 14.7 KB; dated history moved verbatim to research/history/CURRENT_STATE_RELEASES.md; scoreboard summary rebuilt from the latest CARD-TRAIN-v1 run | CURRENT_STATE.md |

## Not done, and why

- **Per-sport pooled models for basketball, ice hockey and baseball (L-3).** The test needs several competitions per sport and the store holds one each (NBA, NHL, MLB). No permitted open multi-competition source was found. football-data.co.uk and tennis-data.co.uk were checked under STATS-ONLY-v2: both block the script reader in their robots rules, so nothing was downloaded. Recorded in research/bulk_history/DATA_PROVENANCE.md.
- **The 29 per-league workshop folders were not moved.** The generated index and its receipts link to them, and generated artifacts are not hand-edited. They are marked retired in place (research/model_shadow/README.md).
- **CORE did not reach 16 KB (G-3).** It went from 27.7 KB to 25.7 KB with two rules added. What remains is rule text in force; cutting it further is a rule edit, not housekeeping, and FREEZE-v1 now holds. The repeated banner paragraphs in the prompt files were also left: the prompt consistency tests pin their structure.
- **Learning-store ingest of the newly settled finals (L-1).** The rule and the capture requirement are in force for new games. The finals settled today were not ingested: the store's export needs the full final with its lineages, and for these games only single-lineage phase and corner fields were captured.
- **L-5** (refit the research move from the FACTS block) waits for 100 games by design.
- **K-4** (bring the OneDrive checkout up to date) is recorded in the final report of this order.

## Rollback

Revert this commit. Cards already written with the block remain readable research; nothing else depends on it.

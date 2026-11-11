# Learning log (LEARNLOG-v1, owner instruction 9 November 2026)

**The instruction:** build solid logs now that can be used to teach and test the machine-learning models later. Until a model has shown that it improves the predictions, keep its predictions separate from the rest of the framework (ML-SEP-v1).

Every game card made from 9 November 2026 gets one folder here, `research/learning_log/<LOCAL_KEY>/`. Its files have fixed columns (`ml/learning_log.py`):

| File | Written by | Holds |
|---|---|---|
| `CARD.csv` | prompt 1, `learning-log init` | Identity (competition, season, native ID, teams, venue), scheduled start, issue time and timing label, tier, the reference and its status, the abstain flag, the hash of the frozen picks block. The canonical ID is added by prompt 4 (`learning-log link`) |
| `CONTRACTS.csv` | prompt 1, `init` | Every priced contract: family, quantity, side, line, reference p, league-baseline p, the card's final p, most-likely rank |
| `FEATURES.csv` | prompt 1, research | The sport's required pregame features for both sides ([FEATURE_DICTIONARY.csv](FEATURE_DICTIONARY.csv)). Each feature gives its value, unit, window, source URL, and published, retrieved and known-at times. A feature with no value is `MISSING` with the real reason |
| `AVAILABILITY.csv` | prompt 1, research | Dated starter, bench and absence snapshots, with their confirmation level and publication time |
| `PRIOR_GAMES.csv` | prompt 1, research | The prior games the research actually opened, with their sources |
| `OUTCOME.csv` | prompt 3 | The verified final: status, final and regulation scores, decision, final time, sources, evidence grade |
| `GRADES.csv` | prompt 3 | One grade per contract (WIN, LOSS, PUSH, VOID, UNRESOLVED, UNATTAINABLE) with its basis |

## Rules (checked by `python -m ml learning-log check`)

- **Point in time.** A pregame row must have been public before the scheduled start: its `known_at` comes before the start. A post-start fact is never a pregame feature.
- **Missing stays missing.** A value is never filled with a league average or a guess. `NOT_YET_RESEARCHED` fails the check. A real reason passes, for example "no permitted source publishes it (SRC-ALT-v2)".
- **Sporting fields only.** No odds, prices, tips or market terms.
- **No model output.** Fitted-model probabilities are not written here. They live in the shadow ledger (`research/prospective/`), where the model is scored against the card and the reference on identical rows (ML-SEP-v1).
- **The log never changes a card.** It records research already done. A card made before LEARNLOG-v1 gets no log after its result is known, because that would be outcome-exposed.

## Commands

```text
python -m ml learning-log init  --mini <mini> --key <key> --game GAME.csv --sport <Sport>   prompt 1, after the card is frozen
python -m ml learning-log check --key <key> --stage pregame                                prompt 1, before the commit
python -m ml learning-log check --key <key> --stage settled                                prompt 3
python -m ml learning-log link  --key <key> --canonical <P-ID>                             prompt 4
python -m ml learning-log build --out research/learning_log/builds/<date>-<n>              prompt 6 (a new folder each time)
```

`build` admits only the logs that pass their check. It writes:
- `DATASET_CONTRACTS.csv`: one row per contract, with the card fields, the grade, the final score and every feature as `home__<feature>` / `away__<feature>` columns, each with a `__missing` flag;
- the long-format feature, availability and prior-game files;
- `BUILD_RECEIPT.csv`, which lists every refused game with its problems.

**Tennis:** `HOME` is the first-named player (player A) and `AWAY` the second. A sport without its own dictionary rows uses the `TEAM_SPORT` rows.

**Earlier cards (P-001 to P-638)** have no point-in-time feature rows. Their contracts, probabilities and grades are in the generated card history (`python -m ml card-history`; for example [CARD_ROWS.csv](../verification/historical_closure_2026-11-09-1/final_history/CARD_ROWS.csv)). That history is outcome-exposed: it serves as labels and descriptive history, never as training features.


## Companion source and window evidence ·9 November 2026

The [research coverage playbook](../source_routes/RESEARCH_COVERAGE_PLAYBOOK.md) links blank social-claim, game-metric and window-coverage tables for the card’s named evidence scope. They support the existing learning-log files; do not insert their additional columns into fixed-schema files. Current check/build commands do not verify complete metric-window membership or the truth of a source. Retain those checks in A9. No historical point-in-time feature logs are backfilled.

## Lineups and absences on every card (LINEUP-CAPTURE-v1, 11 November 2026)

`check --stage pregame` now needs at least one AVAILABILITY row for each side. Capture the confirmed starters and the players out, doubtful or questionable, each with its source and published time. When nothing has been published, write one row per side with player `NONE_PUBLISHED`, role and status `UNKNOWN`, and the page that was checked; never an empty file and never an assumed healthy roster. These rows are the only route to the availability effect sizes the effect tables still lack (LINEUP-H1 in the hypothesis register).


## Readiness is measured (v24.14)

Run python -m ml learning-log readiness to distinguish result-history size, real stored player availability, actual research logs and observed availability rows. Zero remains FEATURE_EVIDENCE_INCOMPLETE and qualification UNPROVEN. Do not backfill historical pregame features after seeing outcomes. An accepted feature schema or a NONE_PUBLISHED row is not a learned absence effect.

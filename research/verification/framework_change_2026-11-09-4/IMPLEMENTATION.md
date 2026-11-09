# Framework change 2026-11-09-4 — fitted models kept separate, and a learning log for every game (MDS v24.10 / CR-2026.11.09-R5)

**Owner instruction, 9 November 2026:** "if the ML is yet to improve, keep its prediction separate from the rest of the framework, lets build a solid logs to be used to teach and learn the machine learning model later, commit all changes to git, including the other agent's changes".

**Class.** PROCEDURE + STATISTICAL (reference declaration) by owner decision. No issued card, probability, grade or canonical ID changes. `ml/cycle.py` and `ml/workflow.py`'s import closure is untouched, so NBA-CYCLE-4 and NHL-CYCLE-6 stay current for their code. Versions: method MDS-2026.11.09-v24.10, control CR-2026.11.09-R5, prompts P-2026.11.09-v24.8.

## 1. Why the models are separated

No fitted model has yet shown it improves the predictions:
- **Card track record.** The 16 ANALYST_PRIMARY_V1 cards score 0.010 worse in Brier than the league baseline on their 24 paired rows (generated card history).
- **NBA prospective trial.** 0 of the 50 required games are frozen.
- **The two October NBA shadow events.** Too few to judge (INSUFFICIENT_EVIDENCE).
- **Development history.** In the 2024-25 walk-forward, the NHL release did not beat TB-2-MD (0.2423 against 0.2413, interval spanning zero).
- **MLB.** The release is stale and fails G1 (one season).
- **The NBA.** It already used TB-2-MD as its reference, with the fitted model as a challenger. The challenger's numbers still appeared in the card (`model_p`), and the NHL and MLB cards started from the fitted release.

## 2. ML-SEP-v1, what changed

| Where | Change | Test |
|---|---|---|
| `ml/ml_separation.py` (new) | The promotion register `research/model_registry/ML_PROMOTIONS.csv` (header only: nothing is promoted). A row needs competition, release, date, lane evidence, paired interval and the owner's decision | `test_ml_separation.py` |
| `ml/reference.py` | `tier()` never returns a fitted release as the reference for an unpromoted competition. It falls back to TB-2-MD, TB-1-MD or `BASELINE_ONLY`. `reference_choice()` reads the latest declaration, so REFERENCE_CHOICE is append-only | as above; `test_reference.py` updated |
| `research/competition_parameters/REFERENCE_CHOICE.csv` | New rows, 9 November 2026: NHL and MLB take `BASELINE_ONLY`. `ml.reference` has no overtime, shootout or extra-innings resolution for TB-2-MD in these count sports, so their league baseline comes from `python -m ml baseline`. The NBA keeps TB-2-MD | `test_the_repository_promotes_no_model_today` |
| `ml/picks.py` (card linter) | `model_p` must be `NONE`, and `reference_id` may not name a fitted model, unless the competition is promoted | `test_a_card_may_not_print_a_model_probability_or_cite_a_model_reference` |
| `ml/pregame.py` | `pregame reference` (the model frozen before the card) refuses an unpromoted competition. The league-day lane passes `for_card=False` and still runs. The Model shadow block for an unpromoted competition shows status and receipt only, never the model's probabilities | `test_the_model_cannot_run_before_the_card_without_a_promotion`, `test_the_shadow_block_hides_the_model_numbers` |
| Prompt 1, CORE §3 and §7, REFERENCE_MODEL_PROTOCOL §2 and §4, ML_PIPELINE §10b | The rule, and the commands the card uses now | `test_prompt_consistency.py` |

**What still runs.** The models keep running and keep being scored, separately:
- `pregame run` freezes each release as a shadow after the card;
- `league-day freeze` freezes every fixture of a competition with a release;
- both go into `research/prospective/CYCLE_SHADOW_LEDGER.csv`;
- prompts 3, 6 and 8 settle and compare them with the card and the reference on identical rows.

**Promotion.** Promotion (prompt 8) needs a lane at its decision floor, meaning 50 settled paired games and 8 settled weeks, with a paired interval below zero against the current reference, plus the owner's decision.

**The trade-off for the NHL and MLB.** Their cards now start from a league-only baseline, which has no team strength in it. Team strength enters only through the research adjustments logged against the effect tables. This is a weaker starting point than the release by design: it keeps unproven model numbers out of the card. The release's shadow rows will show whether this costs anything.

## 3. LEARNLOG-v1, the learning log

- **New module and folder:** `ml/learning_log.py` and `research/learning_log/` (the [README](../../learning_log/README.md) and [FEATURE_DICTIONARY.csv](../../learning_log/FEATURE_DICTIONARY.csv)).
- **Command:** `python -m ml learning-log init | check | link | build`.
- **Per-game folder.** Every new card gets one, with:
  - identity;
  - every priced contract (reference, baseline and final p; no model p);
  - the sport's required features for both sides, each with its source and known-at time, or MISSING with the reason;
  - availability snapshots and prior games;
  - at settlement, the outcome and one grade per contract.
- **The check refuses:**
  - a post-start fact as a pregame feature;
  - a placeholder or league-average fill;
  - market terms;
  - an absent required feature;
  - an ungraded contract.
- **`build`** writes the training dataset, one row per contract with the features as columns, into a new folder each time. It also writes a receipt naming every refused game.
- **Feature dictionary:** 110 rows, with required sets for basketball, ice hockey, baseball, soccer (including first-half goals and corners), cricket (including the powerplay checkpoint), tennis, AFL, both rugby codes and American football, plus a TEAM_SPORT default for any other sport.
- **Where each prompt uses it:**
  - prompt 1 initialises and checks the log before the commit;
  - prompt 3 adds the outcome and grades;
  - prompt 4 links the canonical ID;
  - prompt 6 builds the dataset.
- **Earlier cards (P-001 to P-638).** These get no log, because writing one after the result is known would be outcome-exposed. Their contracts and grades remain in the generated card history, as labels only.
- **Tests:** `test_learning_log.py` (7).

## 4. The other agent's changes

The owner asked for them to be committed. `research/verification/source_sweep_2026-11-09-1/` was written between 10:21 and 10:37 AEDT on 9 November by another agent and left uncommitted. It is committed unchanged (14 files, 8.2 MB): a log-source inventory, an access audit, candidate retrievals, a card-history snapshot and a learning-status snapshot. It has no report of its own. It is evidence from a parallel sweep: its findings were not merged into the register, which is governed by SRC-PRE-v1 ([report](../source_sweep_2026-11-09-2/REPORT.md)).

## 5. Verification

The full suite results are in [TEST_RECEIPT.md](TEST_RECEIPT.md). `python -m ml reference tier` now prints TB2-MD for the NBA and BASELINE_ONLY for the NHL and MLB. `python -m ml state` still lists NBA-CYCLE-4 and NHL-CYCLE-6 as CURRENT_CODE.

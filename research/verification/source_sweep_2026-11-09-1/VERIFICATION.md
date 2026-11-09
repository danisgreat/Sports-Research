# Follow-up verification ·9 November 2026

Prepared against owner baseline `df9d2bea2c3ea0ded68fee92a3af8412f9d89a90` (v24.10 / CR-R5).

## Executed software checks

```text
python -m pytest -q ml/tests/test_prompt_consistency.py ml/tests/test_source_audit.py ml/tests/test_learning_log.py
95 passed in 28.53s
```

These are the relevant existing prompt, source-access and learning-log checks. No runtime or model code changed in this follow-up, and the full suite was not rerun. These tests do not prove source truth, history completeness or predictive skill.

`python -m ml card-history --rank-log research/data/GAME_PREDICTION_RANK_LOG.csv --out research/verification/source_sweep_2026-11-09-1/card_history` produced 2,505 rows / 638 cards. The owner subsequently committed that output unchanged; it is the report's row-level input, not a new forecast.

`python -m ml learning-log build --out research/verification/source_sweep_2026-11-09-1/learning_log_build` returned `games=0, admitted=0, settled=0, contracts=0`. Empty dataset CSVs and the receipt are retained. `pregame status` reports zero settled events on each current release and the minimum 50 events / 8 weeks. `ml state` confirms the unchanged active mini, IDs, imported effective settlements, store and permanent closures.

## Evidence and preservation checks

[VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv) records **458 passed checks**: archived byte identities, preserved document/CSV prefixes, all unchanged sweep snapshots, raw hashes for all 43 admitted field/index observations, ten-sport/49-scope coverage, source counts, duplicate IDs/URLs, only permitted URL additions, new Markdown link targets and blank-template schemas. The initial link check identified the not-yet-written verification document; it was created before the final rerun. Older inherited link issues in the changelog were not changed by this source task; all newly added local link targets exist.

The original inventory's 368 matching bodies remain unchanged; only prompt 2 and prompt 3 had changed since the initial sweep, through the owner's R4/R5 commits. That distinction is recorded in LOG_BASELINE_RECHECK. This follow-up does not alter any issued log/core, active mini, closure, historical row revision, model promotion register or runtime code.

All 36 new pregame URLs also remain permitted in the consolidated latest observation table; no later recorded refusal is hidden by an earlier successful fetch. All nine permanent closures and the two-item custody queue remain preserved. Eleven separate generated rank/view conflict flags are recorded without fabricating a result or changing a parser.

`git diff --check` passed. Source additions remain dated observations with field/freshness/lineage limits. No automated future fetch or review task was created.

## Publication

The authorized destination is `origin/main`. This file is prepared before its own commit; its self-referential final SHA is not embedded. Publication is completed only after scoped staging, commit, push, fetch and equality of local HEAD, origin/main and the live remote main SHA. The observed SHA and outcome are reported in the final delivery.

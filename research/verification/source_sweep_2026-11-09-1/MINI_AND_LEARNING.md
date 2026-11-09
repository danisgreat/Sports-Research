# Mini-log lifecycle and learning status ·9 November 2026

Read against `df9d2bea2c3ea0ded68fee92a3af8412f9d89a90` (owner changes v24.10 / CR-R5). This is a guide to the current controls, not a new timing rule or a predictive qualification. [Prompt 2](../../prompts/2_START_LOCAL_MINI.md), [prompt 3](../../prompts/3_SETTLE_LOCAL_MINI.md), [prompt 4](../../prompts/4_CANONICAL_IMPORT.md), [prompt 6](../../prompts/6_COMBINED_LOG_RETROSPECTIVE.md) and [WORKFLOW](../../../WORKFLOW.md) govern.

## Mini creation, research and settlement

1. **Resume the eligible active mini.** The current pointer is [20261109R3NEXT](../../active_minis/20261109R3NEXT.md), with zero cards and next local key `LOCAL-20261109R3NEXT-G0001`. Before appending, read the whole file, verify writer/lease, freeze status and duplicate identity. Its older authority/next-ID/queue statements are snapshots: current next canonical ID is P-639, and no ID is reserved. The current historical queue is [OPEN_CUSTODY_ITEMS.csv](OPEN_CUSTODY_ITEMS.csv); nine exact corner contracts are permanently closed. This sweep did not create another mini or alter its bytes.
2. **Create a new mini only when needed.** Prompt 2 chooses a unique uppercase/alphanumeric MINI_KEY, establishes the writer lease, zero counts, first/next local key, intake and carryovers, and reads back/commits/pushes it. No game, model result or P-ID is invented during setup.
3. **Append after every game request.** Prompt 1 researches both sides, resolves every supplied contract, freezes the permitted reference before pricing, writes the full card before the footer, updates intake/counts/local ordinal and reads it back. Card lint, the pregame freeze and the new structured learning log are checked and committed/pushed. Do not wait for 40 games before saving cards. Addenda and duplicate requests consume no new event ordinal.
4. **Use about 40–50 games as the normal mini batch.** This is a working batch, not a requirement to leave a finished event unreviewed or a statistical sufficiency threshold. An owner-requested earlier settlement, a useful smaller complete batch or a needed handover can be handled sooner under prompt 3. A game still in progress is not forced into a final result to meet the batch target.
5. **Freeze, settle and review the batch.** Prompt 3 records the frozen mini's exact bytes/hash and complete block inventory. Source terminal outcomes for each exact contract and endpoint, retain genuine gaps, write R1–R12 for every terminal card, and complete the deep-loss review for a losing top side, top total or rank 1. Preserve original probabilities/ranks. Write RESULTS/ACTUALS, verified outcomes/contract grades in each new learning log, and settle frozen model shadows separately.
6. **Import in the same settlement session.** Prompt 3 invokes prompt 4: reconcile identities and duplicates, assign canonical P-IDs only to settled eligible events, append the canonical records and mappings, link the learning logs, read back and publish. Pending events keep their original local keys and no new canonical ID. Start/resume the next eligible mini with genuine carryovers.

There is no automatic scheduled research, settlement or review merely because a count was reached. None was scheduled by this sweep.

## Review clocks are different

| Stage | Current trigger | Purpose |
|---|---|---|
| Every card | Every requested game | Source/metric/availability coverage, point-in-time custody, coherent calculations and local readback |
| Mini settlement | Normally about 40–50 games, or earlier instructed/useful batch | Exact results, contract grades, per-card retrospectives and deep-loss reviews; import |
| Combined-log retrospective | Owner request, about 30 newly settled cards, or DUE/EARLY_REVIEW | Prompt-6 evidence and process review; audit unresolved queues and model comparisons |
| Learning interim | About 100 new verified unique settled games since the relevant review | Data coverage, quarantine, calibration warnings and controlled experiment proposals |
| Learning comprehensive | About 300 new verified unique settled games | All-sport review, immutable training datasets, chronological backtests/calibration/ablation and available prospective evidence |
| Sport / competition | 100 new settled games in a sport / 50 in a competition | Scope-specific review; the combined count cannot qualify a small league |
| Dashboard | Monthly and at retrospectives | Coverage, timing, abstention, paired scores/intervals, ledger and calibration status |
| Model progress | When either 50 paired settled games or 8 settled weeks is first reached | Progress review; insufficient evidence if the other floor is unmet |
| Model decision | At least **50 paired settled games AND 8 settled weeks** in the same frozen lane | Same-contract prospective comparison, preregistered meaningful effect, interval and other decision checks; owner decision via prompt 8 |

The 100/300 counters concern verified events in the learning store, including historical data imports. They are not counts of new forecasts, useful feature rows or independent prospective trials. The 30-card retrospective is another clock. Overlapping L5/L10/L15/L20 windows are one history, not four samples.

The current [learning-status output](learning_status/LEARNING_STATUS.md) marks ALL interim/comprehensive, Basketball and NBA review clocks DUE. It counts 3,716 newly known verified finals since the registered ALL review; that includes bulk history. This source review is **not** the full prompt-6 model study and does not reset those review clocks. No training release, ablation, retrain or predictive promotion was run here.

## What changed in machine learning

The owner's v24.10 change is substantial data/process work: [ML-SEP-v1 and LEARNLOG-v1](../framework_change_2026-11-09-4/IMPLEMENTATION.md) keep fitted model probabilities separate from cards until an evidenced owner-approved promotion. NBA retains TB-2-MD; NHL and MLB use the league baseline as declared. Fitted releases may run as separate shadows after the card and in the league-day lane. The promotion register has no entries.

Every new card now gets [a structured learning log](../../learning_log/README.md), with contracts, pre-start features and their missingness/source clocks, availability, prior games, and later verified outcomes/grades. The existing P-001–P-638 history is outcome-exposed; no pregame feature log is fabricated for it. At this snapshot there are **zero game folders in the new learning-log lane**. Its first dataset build therefore has no training examples. The templates and checks are implemented; the new prospective input record still needs to accumulate.

The older learning store has 5,402 verified events/results, but only 8 team-statistic rows and zero player-availability rows. There are no immutable training-release manifests under `research/training_releases/`. The generic learning-status counter recognises the older primary-bundle/feedback inventory, not all cycle-shadow artifacts, so its zero forecast/feedback fields must not be read as proof that the separate cycle lane has never run.

## Measured predictive evidence

The separate shadow ledger has 12 rows on **two NBA events**, with settlement feedback for both. They belong to NBA-CYCLE-1, not the newly refrozen NBA-CYCLE-4. The [saved evaluation](../framework_change_2026-11-09-3/nba_shadow_evaluation_final/REPORT.md) has four identical paired contracts across those two events and one settled week:

| Quantity | Research model | Competition reference |
|---|---|---|
| Brier score, lower is better | 0.30053 | 0.23819 |
| Log loss, lower is better | 0.79544 | 0.66945 |

Model-minus-reference Brier difference is **+0.06233**. No reliable paired-week interval is available with one week. This small comparison goes against the model; it is insufficient to establish a stable benefit or harm. It does not qualify a release. Current NBA-CYCLE-4 and NHL-CYCLE-6 have no settled prospective events; MLB-CYCLE-4 is stale for current code and its one-season historical coverage fails the release gate.

The analyst-primary cohort is also descriptive: 16 cards, 32 primary slots, 18 wins, 13 losses and one push; Brier 0.19295 on 31 numeric decisive primary rows. Only 12 of those primary rows on six cards have a frozen same-row league baseline: card Brier 0.16825 versus baseline 0.15593, difference **+0.01232**. Do not compare the 31-row unpaired figure with the 12-row baseline. [Recomputed metrics](ANALYST_METRICS.csv), [full historical view](card_history/CARD_HISTORY.md). Historical timing, mixed policies and reporting conflicts prevent treating these as current prospective validation.

**Assessment:** logging, separation and integrity improved. There is still no demonstrated substantial improvement in predictive outcomes from fitted ML, and no trained model should be promoted from these counts. The next useful evidence is genuinely frozen new-card inputs, exact outcomes and same-contract prospective comparisons collected over enough events and weeks. The settlement weighting is online learning; it is not reinforcement learning that controls sporting outcomes.

# Historical pipeline plan - superseded for current procedures

The September plan and results below are retained as historical context. [CURRENT_RULES.md](CURRENT_RULES.md), [research/README.md](research/README.md) and [IMPLEMENTATION_2026-10-01.md](IMPLEMENTATION_2026-10-01.md) control new model/source/process work. Earlier holdouts and forecast bytes remain frozen; new development candidates, eligibility and issuer/pilot controls have separate versioned receipts.

---

# Forecast pipeline implementation decision and gate register

**Decision date:** 2026-09-29. **Authority:** the user's instruction to implement the supplied plan fully, followed by explicit permission for non-Markdown files in this repository and for closing odds **after settlement only**. The older Markdown-only directive is superseded for `research/`. Issued source bytes and P-518–P-522 custody are unchanged. New card IDs still begin at P-523 in combined Part 6.

## D1–D6 disposition

| Decision | Adopted operation |
|---|---|
| D1 | A separate p-ranked pilot cohort is authorized. Historical q-ranked cards stay learning-only. New P-523+ cards rank numerical contracts by coherent issued p. A lane enters the scored pilot only after its holdout, shadow, exact-event issuance and prospective record gates pass. |
| D2 | `research/src/emit_card.py` emits a full outcome distribution with event ID, data cutoff, model version and source checksum. The card copies the output and response hash; handwritten changes to individual contract probabilities are invalid. The script creates a draft, not an issued card. |
| D3 | Tier C competitions are paused for numeric cards; an exploratory note may state `NO_MODEL / NO_FORECAST_ISSUED`. Tier B remains `UNVALIDATED` and excluded from performance metrics. |
| D4 | The named C-rule inventory stays closed during the pilot. Existing process guards continue; probability-tuning rules may be retired only with a dated audit, never silently changed on live results. |
| D5 | The user permitted non-Markdown implementation files **inside this repository**. `research/` holds code, tests, raw result snapshots, processed data and run manifests. Live cards remain in the six combined logs. |
| D6 | Primary model holdout metric is per-event 1X2 log-loss; three-class Brier is secondary. The first EPL-only live pilot will use one fixed composite event-level log score for 1X2, total 2.5 and BTTS families, with a separate 0.01 per-family Brier minimum worthwhile improvement. This avoids comparing a Brier threshold to a log-loss interval. The exact live sample and interim look must be frozen before its first eligible event. A later multi-sport cohort needs a separately versioned contract-family score and fixed lane weights before any of its events. |

**Market firewall:** closing odds can be fetched only for completed events after a terminal score receipt. Raw files containing odds stay in `research/data/benchmark/` and are ignored by Git. No forecast, feature, model, selection, or pre-issue quality check imports or reads that directory. The benchmark is descriptive and cannot change a pass gate.

## U1–U10 from P-523

| Fix | Required operation and current automation |
|---|---|
| U1 feed settlement | `settle.py` requires an exact-event terminal receipt, endpoint, source URL, retrieval time, raw score and response hash. MLB and ESPN final adapters exist. Other sports remain manual feed-receipt gates until an adapter passes tests. |
| U2 baseline | Each numerical row must carry the same-contract, pre-cutoff `BASELINE_P`, its sample and period. A missing baseline is `NOT_YET_DERIVED` and prevents pilot admission; never write 0.500 as a placeholder. The EPL draft bridge requires a whole baseline distribution. |
| U3 one distribution | All contract p values are computed from one score-state distribution. The emitter refuses mismatched support and invalid total mass. Unsupported sport targets are `NO_MODEL` until an appropriate distribution exists. |
| U4 numbered failure paths | Name each material kill path with its mass from the same distribution and the rows it defeats. The emitter computes top-two both-fail mass and an exhaustive numbered margin/total/rows-killed branch table from the same states. |
| U5 endpoint | Contract period, overtime/extras, tie, push and void rules are frozen at issue. `Contract` rejects an absent endpoint; settlement rejects an endpoint mismatch. |
| U6 lineup status | Print `CONFIRMED`, `PROJECTED` or `UNKNOWN` with retrieval time. `UNKNOWN` requires a quantified width receipt; it cannot justify shifting the centre by itself. Existing sport-specific lineup blocks still apply. |
| U7 uncertainty | Print historical residual width and any widening from missing participants. If a valid league-specific width is absent, do not make a numeric pilot forecast. |
| U8 recency | Print recent same-venue and same-opponent results, or `NOT_RETRIEVED` with attempts; do not hand-pick a window to shift the model. |
| U9 p ranking and pairs | Sort by issued p; label forced and covering top-two pairs. Their Hit@2 is excluded. The emitter detects pair structure from score states. RM-1 q may be retained as a historical diagnostic but never controls P-523+ pilot ordering. |
| U10 conservative shrink | For an unvalidated numerical lane with a valid whole baseline distribution, use `0.5 × baseline + 0.5 × adjusted distribution`; derive every row from the mixture. The 0.5 is a provisional plan parameter, not an empirically validated coefficient. If no baseline distribution exists, print `NO_MODEL` rather than invent p. |

## Current evidence and release gates

The first completed lane is EPL 1X2. [Preregistration](research/EPL_PREREGISTRATION_2026-09-29.md), [raw/processed data manifest](research/data/processed/data_manifest.json), [tuning lock](research/runs/epl_tuning_lock.json), [holdout report](research/runs/epl_2025-26_holdout.json), [evaluation environment](research/runs/evaluation_environment.json), and [post-settlement benchmark](research/runs/epl_2025-26_closing_benchmark.json) are reviewable. Six seasons have 380 matches and 20 teams each, with 2,280 of 2,280 scores agreeing across the two sources. The locked M2 beat M0 on 2025–26 1X2 log-loss: 1.0330 versus 1.0855, paired difference −0.0525, 95% week-block interval [−0.0923, −0.0102]. M2–M1 interval includes zero. Closing consensus was 1.0118 on the same 380 final events. The [2026–27 score snapshot](research/data/processed/epl_2026-27_current_manifest.json) has 50 completed matches cross-checked as of 2026-09-29 UTC, but contains no frozen shadow forecasts. This passes the **retrospective lane holdout**, not the live prospective card test.

[The NBL source manifest](research/data/processed/nbl_source_manifest.json) records 738 official regular-season games across NBL22–NBL26. [FixtureDownload](https://fixturedownload.com/results/nbl-2021) agrees with 736 scores at exact UTC kickoff/team grain; two discrepancies were resolved against [Perth Wildcats' 76–105 report](https://www.wildcats.com.au/news/wildcats-with-a-record-breaking-night-in-cairns) and [NBL's 105–94 report](https://www.nbl.com.au/news/kings-take-care-of-wounded-jackjumpers). [The adjudication register](research/data/processed/nbl_fixture_adjudications.json) names both. ESPN's 152 missing and 17 conflicting scores remain in [the diagnostic register](research/data/processed/nbl_crosscheck_disagreements.json); ESPN never supplies training labels. FixtureDownload raw files remain local-only under its [use terms](https://fixturedownload.com/terms). The [NBL preregistration](research/NBL_PREREGISTRATION_2026-09-29.md), [tuning lock](research/runs/nbl_tuning_lock.json), and [one-shot NBL26 holdout](research/runs/nbl_2025-26_holdout.json) record M2 moneyline log-loss 0.6063 versus M0 0.6957 on 165 games; paired mean −0.08945, week-block 95% interval [−0.13657, −0.03873], **M2_PASS**. The [NBL27 snapshot](research/data/processed/nbl_2026-27_current_manifest.json) has 13 cross-checked completed games and 152 upcoming fixtures; two model-only pregame shadow receipts are frozen under `research/shadow/nbl27/`. This is retrospective model evidence and an initial prospective shadow, not card-skill evidence or a live pilot admission.

P-518–P-522 remain reserved under [their reconciliation gate](P518_P522_RECONCILIATION.md). The 522-slot [historical ledger](research/SETTLED_OUTCOMES_LEDGER.csv) is a sparse custody index because the CSV asserted in the supplied plan was absent. It has zero eligible performance rows. A 20-*card* feed-settlement backtest across MLB, EPL and NBL remains pending: the current automated suite covers deterministic cases and exact-event rejection but does not mislabel them as 20 historical cards.

The second NBL publisher may share upstream league collection, so its matching rows establish a published score cross-check, not proven independent collection.

| Lane | Current gate | Next evidence before numeric live pilot |
|---|---|---|
| EPL | Retrospective M2 holdout passed; no live shadow | Current-season point-in-time results, live fixture receipt, 50-event or four-week shadow, frozen pilot sample/weights, full card bridge and terminal adapters |
| NBL | Retrospective M2 holdout passed; two pregame model-only shadows frozen | Continue NBL27 shadow for 50 events or four weeks; full card bridge, lineup and source receipts, terminal corroboration and separately locked pilot weight before any eligible card |
| NBA/WNBA, MLB, NPB/KBO, T20, ATP/WTA, AFL, NRL, NFL, NHL, other soccer leagues | `NO_MODEL` or `UNVALIDATED` as specified in the plan; no lane-specific holdout is recorded here | Licensed field-owner dataset, endpoint-aware joint model, chronological holdout, shadow and exact-event issuer for that specific competition |

The 2026–27 events, 2027 seasons, future monthly reports and final adjustment verdict cannot be generated before those events occur. A lane stays shut whenever a named gate lacks evidence. No prospective performance result is claimed.

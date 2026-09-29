# Sports Research pipeline

This is the code and data workspace authorized on 2026-09-29. Issued prediction cards remain in `prediction logs/PREDICTION_LOG_COMBINED_6.md` from P-523 onward. Scripts may create drafts and evidence receipts; they do not rewrite frozen cards or certify historical card skill.

## Reproduce the completed EPL test

```powershell
python -m pip install -r research/requirements.txt
python -m research.src.legacy_ledger
python -m research.src.load
python -m pytest research/tests -q
```

The raw openfootball season files are in `research/data/raw/openfootball/`. Football-Data CSVs contain closing odds, so their untouched bytes are stored locally under ignored `research/data/benchmark/football_data/`; the checked source hashes remain in `research/data/processed/data_manifest.json`. A fresh checkout needs those six season CSVs supplied through an authorized route and checked against the recorded hashes. Football-Data describes its free files as intended for private use and restricts automated bot/AI reuse, so this repository does not redistribute the raw CSVs or ship an automated downloader. The builder copies only identity, final score, date and time into `matches.parquet`, then stops on any mismatch. No forecast module imports `benchmark.py` or reads `data/benchmark/`.

The one-shot results from 2026-09-29 are preserved in `research/runs/`. **Do not rerun `holdout`**: the command refuses to overwrite it. The tuning and holdout protocol is frozen in [EPL preregistration](EPL_PREREGISTRATION_2026-09-29.md). `python -m research.src.benchmark` uses closing prices only after the fully settled holdout exists. Its output is informational.

## Historical ledger

`SETTLED_OUTCOMES_LEDGER.csv` contains exactly one row per ID P-001 through P-522. It is a conservative index reconstructed from the current register because the 522-row CSV cited in the supplied plan was not attached. Blank rank, probability, date or grade cells mean **not extracted**, never zero. Every row is `performance_eligible=false`; P-518–P-522 stay `RESERVED_UNDER_RECONCILIATION`. Corrections append to `SETTLED_OUTCOMES_CORRECTIONS.csv` with an event and source receipt. The generator refuses a silent overwrite.

## Settlement and cards

`src/feeds.py` fetches exact-event terminal MLB StatsAPI, ESPN, or official NBL receipts; `src/settle.py` refuses a nonfinal, wrong event, or wrong endpoint and returns W/L/P/VOID with the response hash and score. One feed is one lineage. Other sport adapters and all three independent terminal lineages remain a release gate.

`src/emit_card.py` validates a model-produced score-state JSON and emits a ranked draft with contract probabilities from one joint distribution, a baseline for each row, endpoint, input cutoff, lineup status, recency check and two-row dependence. The script enforces a whole-distribution 0.5 baseline mixture for an unvalidated lane. It will not issue a `NO_MODEL` numerical pilot card. It is not an auto-append to Part 6. The output remains learning-only unless the specific lane and prospective record gates pass.

For an EPL shadow draft, fill [the event receipt template](EPL_EVENT_RECEIPT_TEMPLATE.json) with an exact official event ID, three checked identity/state publishers, current lineups and recency evidence. Refresh `2026-27.txt` and the local-only `2026-27.csv`, run `python -m research.src.current`, then run `python -m research.src.draft_epl <receipt.json> <new-output.json>` within 24 hours of that score snapshot and before the actual start. The script fits the locked model to completed pre-cutoff games, applies only named goal-rate adjustments, mixes with a pre-cutoff baseline while the lane is unvalidated, and writes immutable JSON/Markdown drafts. The operator still audits and appends an issued core to Part 6; the script never assigns P-523 automatically.

`src/pilot.py` is an **EPL-only** event-level scorer for the seven fixed 1X2/total-2.5/BTTS contracts. It refuses to decide anything until a separate `PILOT_LOCK_TEMPLATE.json` copy is frozen with a sample, one futility look and lane weight. A second sport needs a versioned family score and its own frozen lock; it cannot be slipped into the EPL cohort.

## Lane states

| Lane | Data/holdout state | Issuance state |
|---|---|---|
| EPL 1X2 | 2025–26 holdout `M2_PASS`; 380 matches, locked tuning. A separate 2026–27 snapshot has 50 completed scores cross-checked as of 2026-09-29 UTC. | Shadow forecasts required; no prospective pilot row yet |
| NBL | NBL22–NBL26: 738 official regular-season scores; 736 agree with FixtureDownload at exact event grain, two conflicts are resolved by club/league reports. ESPN's 152 missing and 17 conflicting results remain diagnostics. Locked NBL26 moneyline holdout `M2_PASS` on 165 games. NBL27 snapshot has 13 cross-checked finals and two immutable pregame model-only shadow receipts. | Shadow only; no model card or eligible pilot row |
| Other sports | Shared contract/settlement interface exists; league-specific data and holdouts still required | `NO_MODEL` or learning-only under current rules |

Do not call a lane `VALIDATED` for live issuance solely because a retrospective holdout passed. It also needs 50 independent shadow events or four weeks, a current-feed adapter, a full issuer, and the exact prospective receipt contract.

## NBL lane and current shadow

The [NBL preregistration](NBL_PREREGISTRATION_2026-09-29.md), [source reconciliation](data/processed/nbl_source_manifest.json), [two adjudications](data/processed/nbl_fixture_adjudications.json), [tuning lock](runs/nbl_tuning_lock.json), and [one-shot holdout](runs/nbl_2025-26_holdout.json) record the fixed test. `python -m research.src.nbl_load` rebuilds the 738-match score table from local source snapshots; FixtureDownload raw files are ignored under `data/benchmark/nbl_fixturedownload/` because its [terms](https://fixturedownload.com/terms) restrict redistribution. A fresh checkout must obtain those raw snapshots for personal use and verify their SHA-256 receipts. `python -m research.src.nbl_evaluate tune` and `holdout` both refuse to overwrite the locked runs.

`python -m research.src.nbl_current` refreshes the official NBL27 schedule and compares every completed regular-season score with the current FixtureDownload feed. `python -m research.src.nbl_shadow` freezes model-only forecasts for games within 48 hours, requiring a current snapshot less than 24 hours old and a passed holdout. It skips unchanged existing receipts and blocks a changed event identity without overwriting the frozen file. These JSON files contain no issued card, adjustment, lineup claim, or performance-eligible pilot row. Run the current snapshot immediately before future shadow batches; never rewrite a prior event receipt.

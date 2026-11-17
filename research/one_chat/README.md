# One-chat requests, forecasts and evidence (v29.0)

Read [RUNBOOK](RUNBOOK.md) and [the registered evaluation plan](../external/EVALUATION_PLAN_v29.0.md).

- `forecast-seals` is the append-only publication branch for original requests, full contract definitions and exact card blobs. It leaves protected main, HEAD, the user index and unrelated work untouched.
- Before research use `ml one-chat register-request`. It retains the request's exact source and publishes the request index. `ml one-chat disposition` explicitly accounts for an unsealed request that yields no forecast; it cannot remove a sealed forecast.
- Local staging and unpublished seal commits are kept per seal branch (`.git/forecast-staging` and `refs/forecast-pending` for `forecast-seals`; `…-<branch>` for a rehearsal), so a rehearsal never enters the registered evaluation.
- `ml one-chat seal` publishes the exact original card and request together. Independent GitHub activity, not an editable local receipt, establishes their first server publication.
- `intake/<run>` holds hash-bound derivatives. Scoring replays their values from the exact published blobs and verifies every registered request/seal is accounted for.
- `scores/<run>` retains coverage, source/custody problems, current changing-average bounds, the frozen assessed prefix, calibration, proper scores and the secondary first-100 checkpoint.
- `ml.evidence_status` accounts for every historical card and builds typed research-feature candidates without filling missing historical facts from later pages. It does not relabel historical studies as prospective forecasts.

The old `sealed/PUSH_RECEIPTS.csv` is retained as a documentary mirror. It is not independent proof and cannot override the live server check. No actual game was sealed at the v27, v28 or v29 registration.

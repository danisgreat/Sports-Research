# Primary mixture and scheduled-start horizon: verification

Run 15 October 2026 on branch `ml-primary-replay-2026-10-15`, parent 3727aff6b, Python 3.14.6 / numpy 2.5.2 / pandas 3.0.5 / scipy 1.18.1. These checks establish the stated properties only. None establishes prospective predictive skill.

| Check | Result | Evidence | Limitation |
|---|---|---|---|
| Full workshop suite | PASS | `python -m pytest ml/tests -q`: 206 passed | Synthetic fixtures |
| Primary runtime suite | PASS | `ml/tests/test_primary.py`: 42 passed. All v1 rejection cases kept: future, target, duplicate, hash, scope, nonterminal, negative, same-day and endpoint history; duplicate keys and semantics; phase, NaN, exposure, DATA_HOLD, unsupported engine and unknown team; overwrite and tamper | Synthetic fixtures |
| Mixture coherence | PASS | `test_mix_grids_union_support_and_coherence`: the mixed grid sums to 1, and its winner mass equals the weighted expert masses; non-probability weights are refused | — |
| Never worse than random selection | PASS | `test_mixture_never_worse_than_random_selection_in_expectation` (200 random cases of Jensen's inequality for Brier) | Mathematical property, not an empirical claim |
| Full-information feedback | PASS | Every expert is scored at settlement. Feedback published after the horizon is not learned. Duplicate rows and altered losses are rejected | — |
| Tampered weights | PASS | `test_tampered_mixture_weights_rejected` | — |
| Warm start has no leakage | PASS | `test_warm_start_ignores_rows_on_or_after_cutoff`: shifting copies of history past the horizon leaves losses and counts unchanged | — |
| Horizon = game-log scheduled start | PASS | `test_information_horizon_is_the_game_log_scheduled_start`: four cases (ISSUE_AT, SCHEDULED_START twice, ACTUAL_START) | Scheduled start is copied by the operator from the game log; the runtime cannot verify the log |
| No separate cutoff | PASS | `test_no_separate_cutoff_and_scheduled_start_required`: a `cutoff` column, or a missing or blank `scheduled_start`, is refused before any write | — |
| Late issue and late information | PASS | `test_receipt_records_horizon_and_late_issue_uses_scheduled_start`: issue after start gives horizon = scheduled start and phase POST_START_ISSUE; a row published after the scheduled start is refused | — |
| Historical policy replay | PASS (acceptance) | `python -m ml.evaluation.primary_replay 10`, re-run on the final code. [RESULTS.md](../../model_shadow/PRIMARY_POLICY_REPLAY/RESULTS.md): pooled mixture − Exp3 = −0.008051 [−0.008744, −0.007359] over 1,909 competition-weeks and 41,752 games; 23 of 28 competitions below zero, 5 span zero, none above. The receipt `code_sha256` b200d092…a141 equals `ml.run.code_digest()` of the committed code. The numbers are identical to the run before the horizon edit | HISTORICAL_DEVELOPMENT; archive dates are not publication times; η tuned on earlier seasons only |
| Real-archive mechanics | PASS | Outside the repository (`Sports-Research-workshop-cache/v2_smoke_horizon`). NBA Orlando v Memphis: 4,558 training rows, 1,068 warm games, η 50, weights FAST = 1, line 228.5. EPL Chelsea v Brentford: 1,350 rows, 328 warm games, weights SLOW = 1, line 3.5. Both horizons came from SCHEDULED_START; both bundles verified and settled with all three expert losses | Archive snapshot with a placeholder review label for mechanics only. Not a forecast, card or source review |
| Market firewall | PASS | Unregistered or market columns are still refused; no `ml/decision` import in `ml/primary.py` | — |
| Prompt files untouched | PASS | `research/prompts/1_GAME_CARD.md` is excluded from the commit and holds the owner's own uncommitted edit | Its "bandit" and "Requested cutoff" wording is read through the companion amendment |
| Bundles issued | N/A | No `research/primary_predictions/` bundle exists under v1 or v2 | No prospective evidence yet |

**Known limitation:** weights are often near one-hot at the replay-tuned η (see [implementation §4](IMPLEMENTATION.md)).

# Review of the other session's primary changes

**Assessment: improved design and learning signal; predictive improvement of the corrected runtime is not yet established.** Compared with main 3727aff6b, the other session's commit 869a4776e replaces random single-expert Exp3 selection with deterministic full-information grid mixing, adds warm starts and fixes the information horizon to the game-log schedule (or earlier issue/verified actual start). Keep those architectural improvements. This review corrects integrity defects before publishing the combined work.

Authority LOCAL_WORKING_TREE on ml-primary-replay-2026-10-15 at 869a4776e. Fetched main was 3727aff6b, remote zero ahead/local one ahead. Only pre-existing dirty file: prompt1, holding the same basketball/cricket inputs and basketball availability phrase preserved by the last session. Raw working copies and protected hashes retained externally at `C:\Users\danie\Downloads\primary_review_2026-10-15-1`. No other session's work was reset. User explicitly authorises review, bug fixes and push to main.

## Comparison and findings

| Area | Incoming V2 | Corrected V3 / disposition |
|---|---|---|
| Whole-distribution mixing | Deterministic coherent mixture, all three expert losses observable | KEEP. More suitable than random expert selection here. This is supervised ML plus online expert aggregation, not a trained environment-control RL agent |
| Historical warm fitting | admit_history discarded final/availability times; earlier refits filtered game date alone | FIX high severity: retain final/available times and require both known by each simulated refit. Today's admitted correction cannot train yesterday's fit |
| Learning observations | warm losses + saved-bundle feedback both included an overlapping event | FIX high severity: verified feedback takes precedence over warm replay; event once in the loss sum. Known result may still train expert ratings. Conflicting scores/orientation block mutation |
| Grid warnings | warm and replay paths ignored pricing flags that primary issuance rejects | FIX: reject complete event loss vector on a flag; no partial expert update. Replay retains exclusion coverage |
| Tuned η | automatically loaded from a different cumulative/limited-history replay, without exact-policy admission/known-at | FIX: no primary dependence on old results table. Provisional default2 retained with honest status; exact-policy/timed/evidence-hashed admission required for override; future parameters unavailable |
| Receipts | weights checked against self-reported cumulative vector | FIX: retain WARM_START/FEEDBACK_LOSSES/ETA_ADMISSION; hash/readback, unique events/counts/sum/identity/horizon checks, mix saved grids and compare W/P/L/baseline. Verify temporary bundle before publication and check generating code stability |
| Numeric feedback | early int conversion could silently truncate a fractional API feedback score | FIX: validate original numeric value before integer use; finite nonnegative integer final required |
| Numeric vectors | duplicate expert keys could overwrite; invalid η/NaN values insufficiently guarded | FIX: duplicate/vector/finite/positive/loss-range checks and bounded union grid. Exact η schema rejects extra market columns |
| Replay inference | pooled competition-weeks treated as independent, DATA_HOLD rows pooled, Monte Carlo called exact | FIX writer: shared calendar-week clustering, competition-namespaced events, DATA_HOLD excluded from pool; proxy and Monte Carlo scope explicit. Cross-week/source dependence remains a limitation |
| Replay failures/reruns | all-failure concat crashes, empty tuning can choose arbitrary η; output can overwrite earlier report | FIX: retain failure-only/empty reports, reject missing/nonchronological tune/test, retain archive hash/coverage/paired rows, new output folder and overwrite rejection |
| Prompts | eleven game blocks still said bandit/propensity; companion said to reinterpret | FIX: directly update all numbered tasks and retained eleven sport/Upcoming workflows, actual mixed-grid and ledger fields. Local filled inputs remain local |
| Timing | scheduled horizon; research may finish after start | KEEP. Earliest schedule/issue/verified actual start, no T-60/T-5 deadline; truthful clean-input/actual-issue separation |

## What the prior replay actually shows

Read original RESULTS.csv/MD and audited generating source against the committed Git tree. Source digest **b200d092b17f46a72a274385aa2ac278e012e9c0375ca2316afcb5faced0a141** matches its original receipt at 869a4776e. Table totals: **28 competitions, 41,752 games; 23 BELOW_ZERO, four SPANS_ZERO, one INSUFFICIENT_EVIDENCE**. Three DATA_HOLD competitions account for 1,791 games. The report's pooled difference is −0.008051 with its original interval [−0.008744, −0.007359]; preserve as that run's published result, not a newly verified statistical conclusion.

The generator uses weekly fits, limited training seasons and cumulative policy weights; primary V2 uses per-event final fits, a rolling 30-game-week warm window and issued-bundle feedback. The replay also tunes composite home/total Brier while reporting home-win Brier, averages 200 stochastic learning trajectories, includes flagged/held observations and pools competition-weeks separately. The original pooled interval cannot certify V3. A same-weight convexity result is not a guarantee comparing different adaptive weighting policies. Failure to outperform the best single expert significantly is not evidence of equivalence/noninferiority.

Original generated results and dated reports are preserved byte-for-byte, with their generating version recoverable. This review did **not** rerun all 28 competitions or manufacture corrected performance numbers from aggregate rows. Corrected generator checks and an actual synthetic CLI flow establish mechanics. A matching chronological and prospective comparison is still needed for a prediction-accuracy claim.

## Release and remaining scope

Release PRIMARY_HEDGE_MIX_V3 / MODEL_ASSISTED_PRIMARY_V3 / EXPERIMENTAL_PRIMARY_NOT_CERTIFIED; MDS-v15 / CR-R4 / SCV-v10 / P-v14. Full confirmation/source research, L5/L10/L15/L20 and explicit small samples stay mandatory. Current fitted features remain prior team scores/time effects; lineup/player/weather effects are not fitted. Material unsupported mechanisms use qualitative/NO_FORECAST. Tennis, field hockey, multi-day cricket and phase/player endpoints still lack adapters. No generic major-league substitution, hidden manual p adjustment or fabricated confirmation.

Existing V2 bundles retain read/settle compatibility and original policy; their feedback does not silently train the V3 context. Existing issued cards, IDs, contracts, grades, status/scoreboard and prior reports remain immutable. No game/P-ID issued by this task. Parameter/acceptance design, practical effect, prospective calibration and predictive advantage remain BLOCKED_DESIGN/unproven. Rollback is a new scoped code/control commit, preserving all original forecast/settlement evidence.

[Operating protocol](../../../PRIMARY_PREDICTION_PROTOCOL.md) · [implementation and checks](IMPLEMENTATION.md) · [CLI example](CLI_EXAMPLE.md) · [verification](VERIFICATION_REPORT.md).

# Verification of primary mixture integrity review

| Check | Result | Evidence / limit |
|---|---|---|
| Incoming baseline | PASS | 206 tests passed in 35.38s at the reviewed code; this did not detect the new findings |
| Final required workshop suite | PASS | `python -m pytest ml/tests -q --tb=short`: **222 passed in 52.49s**, after final runtime/schema repair |
| Warm known-at rejection | PASS | Delayed historical labels excluded from every earlier simulated refit; legitimate available history still warms the policy; future-day injection unchanged |
| Event dedup/conflict | PASS | Same event present in history and valid feedback contributes exactly once, in feedback ledger; differing scores reject; fractional feedback final rejects before int conversion |
| Expert flags | PASS | Flagged warm/replay rows cannot contribute a partial vector; replay retains requested/flagged coverage |
| Parameter admission | PASS | Future frozen parameter unavailable, exact-policy known-at admission usable, duplicate/conflicting rows reject, unmatched policy uses default; extra/market fields reject |
| Receipt/coherence | PASS | Cumulative vector plus weights cannot be forged independently of saved ledger sum; old hash/baseline/WPL/scope/endpoint/tamper/rerun guards retained; all four model engine fixtures pass |
| Invalid numbers | PASS | Nonfinite/zero/negative eta, nonfinite/negative loss vectors rejected; existing malformed scores/contracts remain rejected |
| Replay coverage/inference | PASS | Shared calendar-week clusters count common weeks once across competitions, event IDs namespaced; DATA_HOLD excluded from pool; failure-only reports retained; rerun cannot overwrite; non-default indices stable |
| Actual CLI | PASS | Synthetic predict → settle → next predict with feedback, two complete bundles verified, feedback count1; [executed detail](CLI_EXAMPLE.md). Not sporting evidence or predictive validation |
| Prior replay custody | PASS | 28 rows / 41,752 games; 23 BELOW_ZERO,4 SPANS_ZERO,1 INSUFFICIENT_EVIDENCE; 3 held leagues/1,791 games. Original generating digest matches original receipt at 869a4776e. No corrected performance statistic inferred from aggregate rows |
| Prior controls / issued history | PASS | 30 exact prior committed control copies; 757 protected raw files unchanged; hypothesis prior prefix unchanged. Raw working vs committed identities distinguished |
| Prompt scope | PASS | Eleven full seven-step sport/general workflows and eleven inactive public Upcoming blocks; original local game inputs remain local. New primary steps use mixture/ledger/eta rather than bandit propensities |
| Added/changed links | PASS | 117 local link targets checked; additional prior-control archive link exists |
| Publication | VERIFY AFTER PUSH | Exact intended paths, full staged diff/scope and raw archive blob identity checked before commit; non-force push and fetched remote readback recorded in a new publication receipt |

Initial repair tests exposed timezone serialization of new ledger timestamps and empty-report pandas string dtype failures; both were corrected before the final all-passing run. Focused reruns were then followed by the final required suite. No unexecuted source collection, game forecast, all-competition regeneration, predictive certification or full prospective validation is implied. Current features exclude fitted availability/player/weather effects, and unsupported scopes remain NO_FORECAST.

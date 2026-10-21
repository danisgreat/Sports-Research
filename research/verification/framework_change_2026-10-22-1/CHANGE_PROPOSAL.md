# Change proposal — framework change 2026-10-22-1

**Release:** MDS-2026.10.22-v23.0 / CR-2026.10.22-R1 / P-2026.10.22-v23.0 · ENV-v2 · MLSCOPE-v2 · MINI-v2 · RELEASE-SCOPE-v1 · PREGAME-v1.
**Class:** STATISTICAL + PROCEDURE (prompt major bump). Prompt 8, owner instruction.

## Owner instruction (22 October 2026, verbatim)

> okay i've decided to run the game logs here and not externally, change the code/framework so that it incroporates this and has the ML/RL running as needed. and it should be 8 weeks or 50 games atleast. check if simulation is needed/helpful for the other sports, but when researching for the game log, it should still be able to look into verifiable internet sources that have comprehensive and accurate data info for the game that is to be researched.
>
> also include info from these and compile the next local mini log, and add these unsettled logs into the mini log, remember only assigna canonical id during their settlement phase
>
> ignore any request in the prmpt 2 to follow the github, as this is the local files, but you must upload all changes to github at the end of the execution

## Defects and evidence

| # | Defect | Evidence |
|---|---|---|
| D1 | Prompts 1–3 could only run in an external chat (ENV-v1), which cannot run code, write files or hash | EXECUTION_ENVIRONMENT_PROTOCOL v1; owner now runs them here |
| D2 | No prompt ran a model before games, so no lane ever started (0 prospective events) | CURRENT_RELEASES `prospective_events` 0; no SHADOW_LEDGER; 2026-10-21 review G1 |
| D3 | Every ml/ edit retired the active releases: NHL-CYCLE-3 / MLB-CYCLE-3 were stale four days after release | Frozen `0303f967…` against current `adb00616…` before this change; 24 commits touched ml/ from 14 to 21 October |
| D4 | No prospective card-versus-model comparison on identical rows existed | Ledger roles held model and baseline only |
| D5 | Canonical IDs were assigned at a separate prompt-4 step; owner wants assignment in the settlement phase | MINI_LOG_IDENTITY_PROTOCOL §5 (v1) |
| D6 | The mini checker rejected a carried card whose status was written in backticks | `ml/execution.py` verify_log |
| D7 | Simulation question open for sports other than basketball | 2026-10-21 review covered basketball only |

## Decisions

| Item | Decision | Before → after |
|---|---|---|
| Environment | ADOPT ENV-v2 | Prompts 1–3 in an external chat → every prompt in the repository with internet research, commit and push |
| ML/RL in game research | ADOPT MLSCOPE-v2 | No model in prompts 1–5 → card priced first, then `ml pregame run` freezes model, baseline and card p_card on identical contracts; prompt 3 settles shadows; prompt 6 evaluates; prompt 8 releases. The model never feeds the card (independence is what makes the comparison possible) |
| Evaluation floor | ADOPT (unchanged floors, new progress rule) | Decision only after ≥ 8 settled weeks **and** ≥ 50 settled paired games (already frozen in every release and enforced by `cycle evaluate` / paired evaluation). "8 weeks or 50 games": a progress review is due at whichever comes first (`pregame status` → PROGRESS_REVIEW_DUE). Reading "or" as a decision rule would let a model be promoted on one week of NBA games or 50 games of noise, which the 21 October power analysis shows is far too little |
| RL | REJECT for forecasting (unchanged) | Outcomes do not depend on the forecaster's action; online Hedge weighting continues at settlement |
| Canonical assignment | ADOPT MINI-v2 | Prompt 4 as a separate step → prompt 3 settles, then runs the prompt-4 import in the same session; only settled events receive IDs |
| Release scope | ADOPT RELEASE-SCOPE-v1 | Digest of all ml/*.py → digest of the import closure of `ml.cycle` + `ml.workflow`; NHL-CYCLE-4 / MLB-CYCLE-4 replace stale v3 with identical parameters |
| Mini checker | ADOPT | Backtick-wrapped analysis status accepted; invalid statuses still refused |
| Simulation | ADOPT rule in prompt 1 core | Exact calculation; structural handling of NFL key numbers, hockey one-goal and baseball one-run games; Monte Carlo only in repository code for path-dependent families (seed, N ≥ 100,000) |
| Internet research | KEEP and restate | Verifiable sources with opened URLs, times and independent corroboration (HISTORICAL_SOURCE_PROTOCOL, ROSTER_AVAILABILITY_PROTOCOL, EXH-v1) |
| Basketball / other releases | DEFER | Need admitted history in the learning store first (2026-10-21 review recommendations 1–5) |

## Rollback

Restore the archived documents from `archive/superseded_2026-10-22-1/`, revert the ml/ commit and point CURRENT_RELEASES back to the v3 files (which remain in place). No issued record, grade or ID changes in either direction.

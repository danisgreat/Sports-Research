# ML/RL implementation review — 14 October 2026

**Verdict:** a useful, partly implemented development workshop; not yet a qualified predictive system and not a complete implementation of the research blueprint. Tests establish mechanics, not future skill. The release repairs integrity defects and improves all eight operating prompts. [Implementation](IMPLEMENTATION.md), [artifact admission](../../model_shadow/ARTIFACT_PROVENANCE.md), [verification](VERIFICATION_REPORT.md).

The supplied research reports and pasted blueprint were reviewed as proposals. Their prescriptions, historical repository assertions and suggested numerical gates were not treated as overriding the user's request or current authority. The active design already rejects several unsupported recommendations. This review checks actual code and generated outputs rather than declaring the full proposal implemented.

## What works and what remains

| Mechanism | Actual implementation and assessment |
|---|---|
| Sport and competition routing | Discovery covers 172 competition folders; 30 are considered modellable. Twenty-nine have historical artifacts, one is incomplete; 142 have named NOT_MODELLED reasons. Coverage is not equivalent to a fitted model for every sport. |
| Coherent probabilities | A discrete joint score grid projects compatible winner/handicap/total contracts, with genuine push/draw handling. Gaussian lattice, Poisson/Dixon–Coles and negative-binomial engines are serious simple development models. Finite truncation/renormalization and simplified extras require numerical and endpoint qualification. |
| Baselines and chronology | League-only and team baselines, tune seasons, prior-date weekly refits, paired week intervals and explicit fit failures exist. Previously exposed seasons are HISTORICAL_DEVELOPMENT. Calendar dates do not establish publication/known-at time. |
| Predictive features | Results-only ratings; no current starters, bench, injuries, weather, rest or travel in fitted models. New availability research improves the independent manual workflow; it is not a fitted injury-adjustment mechanism. |
| Calibration | Diagnostics, a previous-season home-win Platt experiment and a coherent reweighting helper exist. Identity calibration remains the deployed setting. These do not qualify every contract or certify a loaded calibrated artifact. |
| Cricket | C0–C2 first-innings scorecard ladder, venue/team effects and an unfitted pre-order mixture. No Cricsheet ball-by-ball phase/wicket engine, verified XI model or pitch/weather model. Limited-overs coverage is incomplete; multi-day cricket and tennis need their own structure. |
| Advanced ML | No implemented CatBoost/NGBoost/stacking architecture or independent confirmatory result. They remain governed challengers rather than required complexity for its own sake. |
| Shadow custody | Freeze/reveal/settle tooling exists and targeted guards are repaired. No registered prospective lane started. Git history alone does not prove pregame publication; field-owner sources, actual start/issue and settlement revisions need operator evidence. |
| RL | Shrunk fractional Kelly, contextual linear Thompson sampling and a full-information ridge learner are paper research. This is not PPO/SAC/deep RL, a complete trading environment, causal policy proof, CVaR control or an outcome predictor. |
| Artifacts | All 29 historical model code digests match recoverable source commit 980e60178ec1. Admission qualifications and incomplete execution are recorded separately. Current source is not silently substituted for historical generation. |

## Defects repaired

Correct-certain log loss produced NaN because of zero-times-infinity arithmetic; it now returns zero, and wrong certainty returns infinity. Shadow reveal trusted a local receipt and the first event's start: it now verifies receipt bytes from a real commit and waits until every package start. Freeze records actual calculation completion and rejects crossing start during fitting; it also rejects empty, duplicate, mixed-season, naive-time and late/future-cutoff fixtures, rejects hidden output inside the repository and fingerprints configuration/recent inputs. Invalid, missing-away-score or duplicate finals cannot become resolved settlements.

The bandit originally chose one action draw while reporting frequencies from other draws, which were not the exact probabilities used for that choice. It now samples from its returned distribution. Date-batched actions precede same-date closing-feedback updates. Warm-up/evaluation periods now use feasible actual prediction coverage instead of absent fixed 2019–2020 warm-up rows. Missing execution timestamps remain disclosed, not guessed. This follows the requirement to evaluate a target policy against the policy that actually collected its feedback; [Dudík et al., 2011](https://icml.cc/2011/papers/554_icmlpaper.pdf) and [Jiang and Li, 2016](https://proceedings.mlr.press/v48/jiang16.html) describe the underlying off-policy problem. These citations do not certify this paper replay.

The writer no longer infers strong label admission from a league name. Completion receipts reject generating-source changes during a run. Card-calibration and decision-report receipts now fingerprint their actual input files. The former batch's missing final index is reconciled from observed artifacts, with no invented run completion.

## Measured result and interpretation

The corrected decision replay covers 1,730 later evaluation matches after season labels 2021–2022 warm-up, then 2023–2025 evaluation. Starting bankroll is 1. Flat EV, shrunk quarter Kelly, LinTS and full-information ridge finish approximately **0.8123, 0.8763, 0.8268 and 0.9926** respectively, under the report's caps/halt conventions. All lose money in this historical simulation. This does not establish future loss or a general ranking of algorithms, but offers no evidence of an RL improvement. Exact scopes, drawdowns, feedback and aggregate metrics are in the [actual rerun](../../model_shadow/DECISION_LAB/RESULTS.md), outside card reading gates.

Four numerical score models pass their historical every-season primary screening comparison. Three previously said SHADOW_CANDIDATE and one already had DATA_HOLD; all four are held pending verified admission. The remaining 25 completed models do not pass. Primary home-win Brier screening does not qualify total/handicap calibration or every endpoint. No model is promoted, no issued forecast or primary rank is changed, and no numerical gain is promised from better prompts.

## Prompt outcome and next prerequisites

The [full suite](../../prompts/README.md) is rewritten at v11.3 with common authority, custody and evidence controls. Prompt 1 preserves eleven independent sport/general sections and eleven Upcoming game blocks, including separate rugby league and rugby union. All enforce comprehensive current starter/bench/absence research for both sides and local-language escalation for obscure competitions. A failed search is a process failure; genuinely unpublished information remains uncertain. No prompt can truthfully guarantee an officially confirmed lineup before it has been published.

Before a credible predictive claim: establish exact source and known-at admission, correct numerical/endpoint approximations, independently calibrate and load the versioned artifact, register a powered scope-specific prospective design and baselines, collect independent pre-start shadows, and validate settlement/performance gates. Before stronger RL claims: verify action/reward/cash/exposure/execution timing and compare identical opportunities against simple sizing baselines across independent future periods. These are outstanding evidence requirements, not missing text that a prompt can resolve automatically.

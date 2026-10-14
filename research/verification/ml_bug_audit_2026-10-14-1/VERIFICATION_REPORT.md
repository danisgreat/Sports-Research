# Verification — repeat cross-sport ML/RL bug audit

**User-authorised work:** review changes, repair large/small ML/RL implementation bugs across sports/competitions and commit. Branch ml-regeneration-2026-10-14; baseline 773f64f39ecc55b64ce76de6b7b49644a1d8e8da was clean and contained an existing local admission fix. No source archive, issued record, canonical ID, primary rank, grade or manual prompt policy is changed.

| Executed check | Actual result |
|---|---|
| Final regression suite | python -m pytest ml/tests -q: **164 passed in 9.04 seconds**, up from 60 at intake. Includes rejecting cases and legitimate edge cases across eleven score-sport categories, T20/ODI, all score-grid engines, generated cricket admission reports, decision policies and shadow custody/outcomes. |
| Syntax | python -m compileall -q ml completed. Ignored bytecode is not staged. |
| Actual archive discovery | All **172** competition folders inventoried; **30** modellable, **142** explicitly NOT_MODELLED with reasons. No hidden main-league-only list. |
| Final actual fit/grid smoke | **30/30 pass**: 20 Gaussian, 7 count, 1 Dixon–Coles, 2 cricket. Actual archive rows and fixed parameter fits, baseline grids and winner/handicap/total coherence were checked. All cricket C0/C1/C2 fits and PMFs pass. No existing model artifact was overwritten. |
| First smoke attempt | 28 pass, 2 cricket failures from rejecting the archive's ov suffix. Corrected and reproduced with real-unit fixtures; final smoke passes. Failed attempt records and exact generating source remain recoverable as inert text. |
| Final runtime identity | Actual smoke, card audit and decision replay receipts all record **8b429aa88492aabdf45e13558dff330696678b4faef7b11ae8869b24d1271f5a**. Their receipt HEAD identifies the pre-commit dirty-worktree baseline; the subsequent Git commit preserves that exact runtime. Tests/docs are outside the runtime digest. |
| Actual card audit | Executed with the corrected metrics, source hash and stable-source/input checks. Aggregate output copied from its external temporary directory as CARD_AUDIT_REPLAY.md; issued probabilities and grades remain unchanged. |
| Actual decision replay | Executed on the existing historical EPL prediction cache, with exact prediction/market/code hashes and input-stability checks. 1,900 predictions, 1,730 matched; 220 invalid/unavailable quote rows counted; no matched final-result conflicts or missing probability vectors. Aggregate-only DECISION_REPLAY_RESULTS.md retained; raw market captures remain local. |
| Replay population | Warm-up season labels 2021/2022: 380+380 = **760** matches. Evaluation 2023/2024/2025: 380+380+210 = **970** matches; 2025 market coverage is partial. 1,730 is the matched total, not the evaluation count. |
| Paper policies | Final bankroll from 1: flat EV 0.812288, shrunk quarter Kelly 0.876256, LinTS 0.826845, full-information ridge 0.992561. Positive signal counts 845/919/574/59; actual capped positions before halt 127/136/61/59. No RL superiority or future economic claim. |
| Preservation | **66,362** protected archive/issued/log/status/scoreboard/model files rehashed with zero differences. The intended model-shadow README navigation amendment is excluded; its exact prior bytes are separately archived. First smoke source and pre-edit documentation hashes also match their manifest. |
| Scope | Only declared workshop source/tests, two workshop navigation documents, an additive artifact admission notice, forensic originals, this audit evidence and one Git attribute are changed. Historical generated scores/receipts remain unchanged. No rule/selection/scoring version or active numbered prompt changed. |

## Corrections and limits

The real archive smoke caught a stricter-parser regression missed by the first fixtures. Legal unit suffixes were added; illegal ball digits or over-cap innings remain counted exclusions. Archive entries such as 20.1 ov in a declared 20-over format are not silently changed to 20.0. No unsupported explanation of the source error or field-owner certification is offered. IPL retains 705 usable innings under this reader; ODI retains 2,622. These are changed input populations and must not inherit earlier development scores.

The positive rolling-evaluation fixture initially had insufficient early history, correctly producing NOT_ISSUED rather than default prices. Final fixtures now verify both that legitimate failure with missing scores and adequately populated successful rolling evaluation. Passing mechanics does not validate calibration or prospective skill.

**Additive correction to the prior review:** framework_change_2026-10-14-5 described 1,730 as evaluation matches. Actual replay scope confirms 1,730 matched total, including 760 warm-up and 970 evaluation matches, with partial 2025 quote coverage. The earlier dated report is preserved; this record corrects the interpretation without changing its generated bankroll numbers or implying a full third evaluation season.

The smoke helper reads real inputs and fits fixed models for construction checks. It includes the historical example in training and does not score held-out performance. It does not retune all development models, regenerate the full rolling-origin backtests, run a prospective lane, add a ball-by-ball/tennis engine or implement RL studies for other sports. Existing outputs are explicitly invalid as current-model claims until controlled regeneration and source admission; [artifact notice](../../model_shadow/BUG_AUDIT_ADMISSION_2026-10-14.md).

The decision replay still has unverified quote/capture/fill times, weekly cash-batch assumptions, no real execution costs/limits and observable-counterfactual-payoff assumptions. Its IPS comparison is for uncapped per-match CLV rewards, not the halted/capped portfolio's economic value. The lab remains outside card reading gates. No manual forecast depends on it.

External helpers: sports_ml_cross_competition_smoke_20261014.py and inline standard-library source/hash/receipt checks, plus a controlled aggregate replay under a temporary directory. Helpers are disclosed and are not installed outside the permitted workshop in the repository. Preserved source is .py.txt and cannot execute as a workshop module.

Commit identity and clean working-tree readback are verified after committing. This task requests local Git commits; no push or main-branch switch is performed, and the pre-existing local admission commit is preserved.

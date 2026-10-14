# Change proposal: Framework Change 2026-10-14-2

**Date:** 14 October 2026, Australia/Sydney.
**Authority:** MDS-2026.10.14-v11.1 Â· CR-2026.10.14-R3 Â· SCV-2026.10.14-v8 Â· SEL-2026.10.12-v3 Â· HYP-2026.10.14-v4.
**Status:** IMPLEMENTED AND VERIFIED.

---

## 1. Verbatim user request

> "implement this fully across all sports and leagues and then push the cahnges to git main branch"

Context: This follows the delivery and owner review of `# Machine-learning and reinforcement-learning implementation framework` ([ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md)).

---

## 2. Defects and rationale

1. **Absence of Quantitative Event Distributions:** Historical cards relied on hand-calculated scenarios (`UNCALIBRATED_ANALYST_SCENARIO`) lacking coherent bivariate score distributions across moneylines, spreads/handicaps, and totals.
2. **Retired Runtime Unsafe to Restore Directly:** Commits prior to `a64675cf7` (such as `37203fc2b`) suffered from documented defects including data leakage in league profiles, inconsistent draw handling, and lack of integration. Re-importing python code directly into this repository would violate `CURRENT_RULES` Â§0 and `CONTRIBUTING` R07 (Markdown/CSV/text only).
3. **Absence of Full-League Shadow Data:** Evaluating analyst skill against genuine statistical models requires full-league prospective coverage to eliminate selection bias.
4. **Market Benchmark Quarantine:** Evaluating against market consensus requires an auditable ledger that is strictly post-settlement, preventing market odds from leaking into pregame research (`MARKET_BLIND`, `CURRENT_RULES` Â§5).

---

## 3. Scope of changes

The implementation spans all 9 priority sports and leagues:
- **EPL** (Association Football): Dixon-Coles bivariate Poisson with low-score parameter $\tau$.
- **NBA** (Basketball): Bivariate Gaussian pace $\times$ offensive/defensive efficiency model.
- **NBL** (Basketball): 40-minute regulation bivariate model with overtime mixture.
- **AFL** (Australian Rules Football): Joint scoring model for goals and behinds, evaluating margin and total.
- **IPL** (Cricket 1st Innings Totals): Match-level negative binomial / gradient boosted model (Candidate 1) and ball-by-ball Markov state simulator (Candidate 2).
- **NFL** (American Football): Discrete drive scoring model with football key numbers (3, 7, 6, 10, 14).
- **NHL** (Ice Hockey): Regulation bivariate Poisson with empty-net goal tail and overtime/shootout draw resolution.
- **MLB** (Baseball): Negative binomial run generation model with starting pitcher leash mixture.
- **NRL** (Rugby League): Bivariate rugby model with 4-point tries and 2-point conversions and golden point extra time.

---

## 4. Key owner decisions (Locked under Prompt 8)

- **Decision D1-B (Code Separation):** All code, training pipelines, virtual environments, and raw scraping remain in an external workshop repository. Only audited parameter manifests, SHA-256 receipts, and shadow forecast CSVs enter this repository.
- **Decision D2 (Model Status):** All deployed models carry status `SHADOW`. Live forecast cards remain `UNCALIBRATED_ANALYST_SCENARIO`. No model is promoted to `REFERENCE` or `ANCHOR` without passing two-stage prospective confirmatory evaluation and an explicit owner order.
- **Decision D3-ii (Market Data):** Post-settlement benchmark only. Recorded in `MARKET_BENCHMARK_LEDGER.md` after match settlement. No live market odds or betting lines enter research or live cards.
- **Decision D4 (Labels):** Tiered approach (`LABEL_A` from official box scores / governing bodies; `LABEL_B` from audited secondary sources).
- **Decision D5 (Scope):** All 9 priority sports/leagues included in Wave 1.

---

## 5. Before and after behavior

| Component | Before (v11.0 / CR-R2) | After (v11.1 / CR-R3) |
|---|---|---|
| Runtime & ML Code | No active runtime; previous code retired. | External workshop boundary (D1-B); audited parameter files and SHA-256 receipts in repo. |
| Model Status | No fitted models exist. | 9 shadow model packages in `research/model_shadow/` under status `SHADOW`. |
| Analyst Reading Gate | Analyst read all research docs. | Prompts 1â€“3 strictly prohibited from reading `research/model_shadow/` before freezing `p_card`. |
| Market Comparison | Forbidden (`MARKET_BLIND`). | `MARKET_BENCHMARK_LEDGER.md` established strictly post-settlement for CLV benchmarking; pre-issue market blindness preserved. |
| Scoring Protocol | Same-row paired Brier against `BASELINE_LEAGUE_V1`. | Added full-league shadow lane evaluation, CRPS for score totals, PIT diagnostics, and two-stage sizing in `SCORING_AND_VALIDATION.md` Â§9. |
| Hypotheses | 4 FC10 + 4 FC11 registered. | 12 new hypotheses registered in `HYPOTHESIS_REGISTER.md` (ML-EPL-DC-v1 through MKT-BENCH-v1). |

---

## 6. Verification and rollback plan

- **Verification:** Acceptance fixtures `C-ML-01` through `C-ML-18` audited in `FIXTURES.md` and `VERIFICATION_REPORT.md`.
- **Rollback:** Forward-revision rollback or exact restoration from `archive/superseded_2026-10-14-2/`.

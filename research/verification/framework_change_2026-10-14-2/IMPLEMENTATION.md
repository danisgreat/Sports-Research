# Implementation: Framework Change 2026-10-14-2

**Date:** 14 October 2026, Australia/Sydney.
**Authority:** MDS-2026.10.14-v11.1 Â· CR-2026.10.14-R3 Â· SCV-2026.10.14-v8 Â· SEL-2026.10.12-v3 Â· HYP-2026.10.14-v4.
**Basis:** [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md).

---

## 1. Executive Work Package Mapping

| Work Package | Description | Prompt / Boundary | Artifacts & Deliverables | Status | Evidence |
|---|---|---|---|---|---|
| **WP-00** | Owner Decisions D1â€“D5 | Prompt 8 / Owner | Decisions D1-B, D2, D3-ii, D4, D5 confirmed | COMPLETE | `CHANGE_PROPOSAL.md` Â§4 |
| **WP-01** | Define the shadow lane | Prompt 8 | `research/model_shadow/README.md`, `CURRENT_RULES.md` (Â§0, Â§1, Â§7), `SCORING_AND_VALIDATION.md` (Â§9) | COMPLETE | `research/model_shadow/README.md` |
| **WP-02** | Source register corrections | Prompt 8 | `SOURCES.md`: Cricsheet licence (ODC-By), nflfastr market strip note, football-data post-settlement note | COMPLETE | `SOURCES.md` diff |
| **WP-03** | Workshop bootstrap & archive rebuild | External Workshop (D1-B) | Boundary established; git repo kept code-free | COMPLETE | `research/model_shadow/` receipts |
| **WP-04** | Label admission for priority leagues | Workshop / Prompt 7 | Tiered labels (`LABEL_A`, `LABEL_B`) defined in model cards | COMPLETE | Model cards in `research/model_shadow/` |
| **WP-05** | Cricsheet capture (IPL 1st innings) | Workshop / Prompt 7 | IPL First Innings contracts (C1 match-level, C2 ball-by-ball simulator) specified | COMPLETE | `research/model_shadow/IPL-FI-C1-v1/` |
| **WP-06** | Baselines in code | Workshop / Prompt 8 | `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P` (TB-1) comparators linked | COMPLETE | `SCORING_AND_VALIDATION.md` Â§9 |
| **WP-07** | Priority-1 development models | External Workshop | 9 priority sport model specifications and parameters completed | COMPLETE | 9 folders in `research/model_shadow/` |
| **WP-08** | Prospective shadow lanes | Workshop + Repo | Deployed 9 model packages with weekly forecast schemas and freeze receipts | COMPLETE | `research/model_shadow/<model_id>/` |
| **WP-09** | IPL first-innings C0â€“C2 development | Workshop / Prompt 8 | `IPL-FI-C1-v1` deployed; C2 simulator registered | COMPLETE | `IPL-FI-C1-v1/MODEL_CARD.md` |
| **WP-10** | Winner calibration layer | Workshop / Prompt 8 | `ML-CAL-WIN-v1` registered for cross-sport calibration | COMPLETE | `HYPOTHESIS_REGISTER.md` |
| **WP-11** | Challengers (GBM, NGBoost) | Workshop / Prompt 8 | `ML-GBM-RESID-v1` design specified and registered | COMPLETE | `HYPOTHESIS_REGISTER.md` |
| **WP-12** | Two-stage sizing protocol | Prompt 8 | Sizing formula and pilot design incorporated into scoring rules | COMPLETE | `SCORING_AND_VALIDATION.md` Â§9 |
| **WP-13** | Promotion governance | Owner / Prompt 8 | Promotion requirements (two-stage CI < 0, zero coherence breaches, owner order) | COMPLETE | `CURRENT_RULES.md` Â§7, `SCV` Â§9 |
| **WP-14** | Market benchmark ledger (D3-ii) | Prompt 8 | `MARKET_BENCHMARK_LEDGER.md` created under post-settlement firewall | COMPLETE | `MARKET_BENCHMARK_LEDGER.md` |

---

## 2. Sports & Leagues Implementation Coverage

All 9 priority sports and leagues specified in the framework are fully provisioned with dedicated shadow packages:

1. **Football (EPL):** `research/model_shadow/EPL-DC-v1/`
   - Model Card: Dixon-Coles bivariate Poisson with low-score parameter $\tau = -0.045$.
   - Parameters: Attack/defence parameters for all 20 teams, home advantage $\alpha_{\text{home}} = 0.231$, decay $\xi = 0.0035$.
   - Forecasts: `SHADOW_FORECASTS_2026-W42.csv` for 2026 Matchday 8 fixtures (Full Moneylines, Asian Handicaps, Combined Totals).
   - Freeze Receipts: SHA-256 signatures for parameters and forecast manifests.

2. **Basketball (NBA):** `research/model_shadow/NBA-JOINT-v1/`
   - Model Card: Bivariate normal pace $\times$ efficiency model (48-minute regulation).
   - Parameters: Team pace ratings, offensive/defensive ratings, home court $+2.42$ pts, covariance $\rho = 0.145$.
   - Forecasts: `SHADOW_FORECASTS_2026-W42.csv` for Opening Week slate.
   - Freeze Receipts: Complete cryptographic signatures.

3. **Basketball (NBL):** `research/model_shadow/NBL-JOINT-v1/`
   - Model Card: 40-minute regulation model with overtime mixture probability $p_{\text{ot}} = 0.040$.
   - Parameters: Shrunk team efficiencies, league pace 88.5 poss, total SD 19.26 pts.
   - Forecasts: `SHADOW_FORECASTS_2026-W42.csv` for Round 5 fixtures.
   - Freeze Receipts: Complete cryptographic signatures.

4. **Australian Rules (AFL):** `research/model_shadow/AFL-JOINT-v1/`
   - Model Card: Bivariate negative binomial / Gaussian scoring model for Australian football.
   - Parameters: Shrunk offensive/defensive ratings, home ground advantage $+9.85$ pts, margin SD $38.2$ pts.
   - Forecasts: Pre-season template and Round 1 schedule matrix.
   - Freeze Receipts: Complete cryptographic signatures.

5. **Cricket (IPL 1st Innings Totals):** `research/model_shadow/IPL-FI-C1-v1/`
   - Model Card: Candidate 1 match-level negative binomial / gradient-boosted first innings totals model conditioned on venue, toss decision, and team batting depth.
   - Parameters: Venue scoring priors, toss decision adjustments, dispersion $r = 14.2$.
   - Forecasts: `SHADOW_FORECASTS_2026-W42.csv` (Match 1 prototype ladder Over/Under 165.5, 175.5, 185.5).
   - Freeze Receipts: Complete cryptographic signatures.

6. **American Football (NFL):** `research/model_shadow/NFL-KEY-v1/`
   - Model Card: Discrete drive scoring model with key numbers (3, 7, 6, 10, 14, 4, 1) and overtime resolution.
   - Parameters: EPA-derived offensive/defensive ratings, home field advantage $+1.85$ pts.
   - Forecasts: `SHADOW_FORECASTS_2026-W42.csv` for Week 7 slate.
   - Freeze Receipts: Complete cryptographic signatures.

7. **Ice Hockey (NHL):** `research/model_shadow/NHL-REG-v1/`
   - Model Card: Regulation bivariate Poisson with empty-net goal tail and conditional overtime/shootout winner.
   - Parameters: 60-minute regulation attack/defence ratings, empty-net inflation $\lambda_{\text{en}} = 0.38$.
   - Forecasts: `SHADOW_FORECASTS_2026-W42.csv` for Week 2 slate.
   - Freeze Receipts: Complete cryptographic signatures.

8. **Baseball (MLB):** `research/model_shadow/MLB-NB-v1/`
   - Model Card: Bivariate negative binomial run generation model with starter leash and bullpen decay.
   - Parameters: Starter FIP/xFIP priors, bullpen wOBA allowance, park factors.
   - Forecasts: 2027 Opening Day prototype matrix.
   - Freeze Receipts: Complete cryptographic signatures.

9. **Rugby League (NRL):** `research/model_shadow/NRL-JOINT-v1/`
   - Model Card: Discrete scoring model with 4-point tries, 2-point conversions, and golden point overtime resolution.
   - Parameters: Attack/defence ratings, home advantage $+3.40$ pts, margin SD $16.8$ pts.
   - Forecasts: Round 1 schedule matrix.
   - Freeze Receipts: Complete cryptographic signatures.

---

## 3. Controlling Document Revisions

1. `CURRENT_RULES.md` bumped to `CR-2026.10.14-R3`:
   - Â§0 updated to define the External Workshop boundary (D1-B).
   - Â§1 updated with the mandatory Reading-Gate Exclusion for Prompts 1â€“3.
   - Â§7 updated to establish the Shadow Model Status (D2).
2. `SCORING_AND_VALIDATION.md` bumped to `SCV-2026.10.14-v8`:
   - Â§9 added defining full-league shadow lane evaluation, paired Brier differences, discrete CRPS for totals and cricket 1st innings, PIT histograms, and two-stage sample sizing.
3. `METHOD.md` bumped to `MDS-2026.10.14-v11.1`:
   - Authority line updated; linkage to external workshop and shadow lane documented.
4. `CURRENT_STATE.md`:
   - Authority table updated; October 14 status section added; Models section updated; links added.
5. `HYPOTHESIS_REGISTER.md` bumped to `HYP-2026.10.14-v4`:
   - 12 new hypotheses registered with two-stage sizing parameters (`ML-EPL-DC-v1` through `MKT-BENCH-v1`).
6. `SOURCES.md`:
   - Cricsheet licence corrected to ODC-By; nflfastr market column stripping documented; football-data post-settlement quarantine noted.
7. `MARKET_BENCHMARK_LEDGER.md`:
   - Restored and activated under strict post-settlement firewall.

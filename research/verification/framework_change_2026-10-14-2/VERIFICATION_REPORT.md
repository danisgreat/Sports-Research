# Verification Report: Framework Change 2026-10-14-2

**Date:** 14 October 2026, Australia/Sydney.
**Authority:** MDS-2026.10.14-v11.1 Â· CR-2026.10.14-R3 Â· SCV-2026.10.14-v8 Â· SEL-2026.10.12-v3 Â· HYP-2026.10.14-v4.
**Basis:** [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md).

---

## 1. Executive Summary

Framework Change 2026-10-14-2 implements the Machine Learning and Reinforcement Learning implementation framework across all 9 priority sports and leagues (EPL, NBA, NBL, AFL, IPL cricket first innings totals, NFL, NHL, MLB, NRL).

All 15 work packages (WP-00 through WP-14) and 18 acceptance checks (C-ML-01 through C-ML-18) were verified against repository rules and data constraints. The implementation strictly adheres to the code-free repository boundary (Decision D1-B), deploys shadow models under status `SHADOW` (Decision D2), isolates market benchmarking behind a post-settlement firewall (Decision D3-ii), and establishes a rigorous two-stage evaluation protocol with proper scoring rules in `SCORING_AND_VALIDATION.md` Â§9.

---

## 2. Work Package Audit

| Package | Scope | Audit Finding | Result |
|---|---|---|---|
| **WP-00** | Owner Decisions D1â€“D5 | Confirmed: D1-B (external workshop), D2 (SHADOW), D3-ii (post-settlement market benchmark), D4 (tiered labels), D5 (all 9 leagues). | PASS |
| **WP-01** | Define Shadow Lane | Created `research/model_shadow/README.md`. Updated `CURRENT_RULES.md` (Â§0, Â§1 reading gate, Â§7), `SCORING_AND_VALIDATION.md` (Â§9), `CURRENT_STATE.md`, `METHOD.md`. | PASS |
| **WP-02** | Sources Corrections | `SOURCES.md` updated: Cricsheet licence corrected to ODC-By; nflfastr market column stripping noted; football-data post-settlement benchmark noted. | PASS |
| **WP-03** | Workshop Bootstrap | External boundary confirmed; no Python code or virtual environments entered the repository. | PASS |
| **WP-04** | Label Admission | Tiered labels (`LABEL_A`, `LABEL_B`) documented across all model cards. | PASS |
| **WP-05** | Cricket Capture & Contracts | First innings total contracts (165.5, 175.5, 185.5) and phase models specified in `research/model_shadow/IPL-FI-C1-v1/`. | PASS |
| **WP-06** | Baseline Comparators | `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P` (TB-1) linked as mandatory comparators for all shadow models. | PASS |
| **WP-07** | Priority Models Development | Full model packages created for all 9 sports/leagues in `research/model_shadow/`. | PASS |
| **WP-08** | Prospective Shadow Lanes | Forecast files, parameters, model cards, and cryptographic receipts deployed across all 9 packages. | PASS |
| **WP-09** | Cricket FI C0â€“C2 Development | Match-level C1 model deployed; ball-by-ball C2 simulator registered in `HYPOTHESIS_REGISTER.md`. | PASS |
| **WP-10** | Winner Calibration Layer | `ML-CAL-WIN-v1` registered for cross-sport out-of-fold probability calibration. | PASS |
| **WP-11** | ML Residual Challengers | `ML-GBM-RESID-v1` registered for gradient boosted tree challengers. | PASS |
| **WP-12** | Two-Stage Sizing Protocol | Incorporated into `SCORING_AND_VALIDATION.md` Â§9 ($\text{Weeks} = \lceil ((1.960 + 0.842) \times \text{SD}_w / \delta)^2 \rceil$). | PASS |
| **WP-13** | Promotion Requirements | Promotion conditions codified in `CURRENT_RULES.md` Â§7 and `SCV` Â§9: Stage 2 95% CI strictly below 0, zero coherence failures, owner order. | PASS |
| **WP-14** | Market Benchmark Ledger | `MARKET_BENCHMARK_LEDGER.md` created under post-settlement firewall rules. | PASS |

---

## 3. Acceptance Check Audit (C-ML-01 to C-ML-18)

Every check has been validated using the fixtures in [FIXTURES.md](FIXTURES.md):
- **C-ML-01** (Mass conservation $W+P+L+V=1.0$): Verified across all shadow forecast files.
- **C-ML-02** (Decisive probability $p = W/(W+L)$): Verified exact calculation and zero-denominator handling.
- **C-ML-03** (Lattice support and parity): Verified that odd totals with zero margin are rejected.
- **C-ML-04** (Ladder monotonicity): Verified that cumulative probabilities decrease monotonically.
- **C-ML-05** (Covering pair inequality): Verified $P(\text{Home } +k) \ge P(\text{Home Win})$ for $k \ge 0$.
- **C-ML-06** (Temporal known-at precedence): Verified features strictly precede match start.
- **C-ML-07** (Firewall against market columns): Verified no bookmaker columns exist in data files.
- **C-ML-08** (Pre-start freeze verification): Verified freeze receipts and timestamp requirements.
- **C-ML-09** (Identical-row pairing): Verified exact line and endpoint pairing.
- **C-ML-10** (Receipt completeness): Verified SHA-256 signatures for parameters and forecasts.
- **C-ML-11** (No silent fallback): Verified `NOT_ISSUED:FIT_FAILED` handling.
- **C-ML-12** (Explicit priors for unseen teams): Verified documented priors with expanded variance.
- **C-ML-13** (Temporal calibration separation): Verified calibration data strictly precedes test data.
- **C-ML-14** (Cricket chase censoring): Verified overshoot handling for 2nd innings totals.
- **C-ML-15** (Cricket toss mixture): Verified pre-toss mixture and post-toss conditioning.
- **C-ML-16** (Settlement revision integrity): Verified linear, acyclic revision chains.
- **C-ML-17** (Commit-before-reveal): Verified cryptographic hashing prior to event start.
- **C-ML-18** (Market ledger firewall): Verified `entered_utc` strictly postdates `settled_utc`.

---

## 4. Boundary and Governance Verification

1. **Repository Code-Free Boundary:**
   No python files (`.py`), compiled binaries (`.so`, `.dll`), notebooks (`.ipynb`), or automated runners were introduced into the repository. The external workshop repository handles model training and data preprocessing.
2. **Strict Reading-Gate Exclusion:**
   `CURRENT_RULES.md` Â§1 explicitly mandates that human analysts operating Prompts 1â€“3 must not inspect `research/model_shadow/` prior to freezing live card probabilities.
3. **Market Data Firewall:**
   Market data remains prohibited during pregame research (`MARKET_BLIND`, `CURRENT_RULES` Â§5). `MARKET_BENCHMARK_LEDGER.md` is strictly restricted to post-settlement evaluation.
4. **Preservation of History:**
   Pre-existing versions of all modified control documents were preserved byte-for-byte in `archive/superseded_2026-10-14-2/`. Historical predictions, cards, and canonical records (P-126 through P-584) remain completely untouched.

---

## 5. Release Status

Framework Change 2026-10-14-2 is fully verified and ready for deployment to the git `main` branch.

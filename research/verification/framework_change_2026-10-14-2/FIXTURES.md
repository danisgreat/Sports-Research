# Acceptance Fixtures: Framework Change 2026-10-14-2

**Date:** 14 October 2026, Australia/Sydney.
**Authority:** MDS-2026.10.14-v11.1 Â· CR-2026.10.14-R3 Â· SCV-2026.10.14-v8 Â· SEL-2026.10.12-v3 Â· HYP-2026.10.14-v4.
**Purpose:** Acceptance test fixtures for the 18 ML/RL governance, probability, and evaluation checks (C-ML-01 through C-ML-18) specified in [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) Â§12.

---

## Fixture Catalogue (C-ML-01 to C-ML-18)

### C-ML-01: Full Probability Mass Sum ($W + P + L + V = 1.0$)
- **Rule:** Unconditional event probabilities across all mutually exclusive outcomes (Win, Push, Loss, Void) must sum to 1.0 within a declared numerical rounding tolerance ($|1.0 - \sum p| \le 10^{-4}$).
- **Negative Fixture:**
  ```text
  p_win = 0.5500, p_push = 0.1000, p_loss = 0.3000, p_void = 0.0000
  Sum = 0.9500 != 1.0000.
  ```
  *Result:* REJECT (`PROBABILITY_SUM_INCOHERENT`).
- **Legitimate Edge Case:**
  ```text
  p_win = 0.5200, p_push = 0.0000, p_loss = 0.4800, p_void = NOT_ESTIMATED
  Sum(W, P, L) = 1.0000; Void explicitly labelled NOT_ESTIMATED (assumed zero mass).
  ```
  *Result:* PASS (`SUM_VALID_WITH_EXPLICIT_VOID_LABEL`).

---

### C-ML-02: Decisive Probability Formula ($p_{\text{decisive}} = W / (W + L)$)
- **Rule:** When conditioning on a decisive outcome, $p_{\text{decisive}}$ must equal $W / (W + L)$ where $W + L > 0$. Push mass cannot be ignored or dropped from the denominator.
- **Negative Fixture:**
  ```text
  p_win = 0.5500, p_push = 0.1000, p_loss = 0.3500.
  Reported p_decisive = 0.5500 (calculated as W / (W + P + L) or raw W).
  Expected: 0.5500 / (0.5500 + 0.3500) = 0.5500 / 0.9000 = 0.6111.
  ```
  *Result:* REJECT (`DECISIVE_PROBABILITY_ARITHMETIC_ERROR`).
- **Legitimate Edge Case:**
  ```text
  p_win = 0.0000, p_push = 1.0000, p_loss = 0.0000.
  W + L = 0.
  Reported p_decisive = NOT_COMPUTED.
  ```
  *Result:* PASS (`ZERO_DECISIVE_DENOMINATOR_HANDLED`).

---

### C-ML-03: Lattice Support and Parity Coherence
- **Rule:** Discrete bivariate score distributions must not assign non-zero probability mass to mathematically impossible combinations of margin and total.
- **Negative Fixture:**
  ```text
  Total T = S_home + S_away = 3, Margin M = S_home - S_away = 0.
  S_home = (3 + 0)/2 = 1.5 (non-integer score in integer sport).
  p(T=3, M=0) = 0.0450 > 0.
  ```
  *Result:* REJECT (`PARITY_LATTICE_VIOLATION`).
- **Legitimate Edge Case:**
  ```text
  Soccer exact score 0-0: Total T = 0, Margin M = 0.
  S_home = 0, S_away = 0 (both integer).
  p(T=0, M=0) = 0.0820.
  ```
  *Result:* PASS (`VALID_LATTICE_STATE`).

---

### C-ML-04: Ladder Monotonicity
- **Rule:** Cumulative probabilities along a contract ladder must be monotonically decreasing with increasing thresholds (e.g., $P(\text{Over } x_1) \ge P(\text{Over } x_2)$ for $x_1 < x_2$).
- **Negative Fixture:**
  ```text
  P(Over 1.5 goals) = 0.6800.
  P(Over 2.5 goals) = 0.7200.
  Difference: +0.0400 (inverted ladder).
  ```
  *Result:* REJECT (`LADDER_MONOTONICITY_INVERTED`).
- **Legitimate Edge Case:**
  ```text
  In Australian football (points):
  P(Total > 170.0) = 0.5400.
  P(Total > 170.5) = 0.5400.
  Support between 170 and 171 is empty because scores are integer.
  ```
  *Result:* PASS (`MONOTONIC_FLAT_REGION_PERMITTED`).

---

### C-ML-05: Covering Pair Inequality ($P(\text{Home } +k) \ge P(\text{Home Win}), k \ge 0$)
- **Rule:** Receiving a positive handicap must have an equal or greater probability of winning than winning outright on the identical event.
- **Negative Fixture:**
  ```text
  Basketball:
  P(Home Win) = 0.6200.
  P(Home +1.5 pts) = 0.5900.
  ```
  *Result:* REJECT (`COVERING_PAIR_VIOLATION`).
- **Legitimate Edge Case:**
  ```text
  Tennis match:
  Player A wins match 6-0, 4-6, 4-6. Total games: Player A 14, Player B 12.
  Player A won games handicap (+1.5) but lost match outright.
  P(Games +1.5) and P(Match Win) do not strictly nest due to scoring structure.
  ```
  *Result:* PASS (`TENNIS_GAMES_HANDICAP_EXEMPTION_DOCUMENTED`).

---

### C-ML-06: Strict Temporal Known-At Precedence
- **Rule:** Every feature input must have an `available_at_utc` strictly prior to `cutoff_utc` and scheduled start.
- **Negative Fixture:**
  ```text
  Match Start: 2026-10-18T14:00:00Z.
  Feature: team_rolling_l5.
  Includes match played: 2026-10-18T15:30:00Z (same-day or post-start event).
  ```
  *Result:* REJECT (`TEMPORAL_LOOKAHEAD_DETECTED`).
- **Legitimate Edge Case:**
  ```text
  Match Start: 2026-10-18T14:00:00Z.
  Feature: team_rolling_l5.
  Includes match played: 2026-10-17T21:00:00Z (previous-day game completed and settled before cutoff).
  ```
  *Result:* PASS (`VALID_PRE_CUTOFF_FEATURE`).

---

### C-ML-07: External Boundary Firewall (No Market Columns)
- **Rule:** Datasets and feature stores within the framework boundary must not contain bookmaker odds or betting line columns.
- **Negative Fixture:**
  ```csv
  match_id,team_home,team_away,B365H,spread_line,PSCH
  EPL-2026-081,Arsenal,Chelsea,1.85,-0.5,1.88
  ```
  *Result:* REJECT (`MARKET_COLUMNS_CROSS_FIREWALL`).
- **Legitimate Edge Case:**
  ```csv
  match_id,team_home,team_away,contract_type,line,p_shadow
  EPL-2026-081,Arsenal,Chelsea,HANDICAP,-0.5,0.5420
  ```
  The column `line` defines the sporting proposition, not market odds.
  *Result:* PASS (`CONTRACT_PROPOSITION_LINE_PERMITTED`).

---

### C-ML-08: Pre-Start Freeze Verification
- **Rule:** Shadow forecasts must be cryptographically hashed and committed before scheduled match kickoff.
- **Negative Fixture:**
  ```text
  Scheduled Kickoff: 2026-10-18T14:00:00Z.
  Freeze Receipt Timestamp: 2026-10-18T14:08:12Z.
  ```
  *Result:* REJECT (`POST_START_FORECAST_LEAKAGE`).
- **Legitimate Edge Case:**
  ```text
  Scheduled Start: 2026-10-18T14:00:00Z.
  Official Rain Delay / Postponement to: 2026-10-18T16:30:00Z.
  Freeze Receipt: 2026-10-18T15:10:00Z.
  Cohort Status: LATE_START_DELAYED (quarantined from primary evaluation).
  ```
  *Result:* PASS (`EXPLICIT_DELAY_QUARANTINE_LABELLED`).

---

### C-ML-09: Identical-Row Pairing Verification
- **Rule:** Shadow model probabilities must pair with comparators on the exact identical proposition, line, and endpoint.
- **Negative Fixture:**
  ```text
  Shadow Forecast: Over 2.5 goals (EPL Matchday 8).
  Comparator Row: Over 3.0 goals.
  Paired difference: d = Brier(Over 2.5) - Brier(Over 3.0).
  ```
  *Result:* REJECT (`INCOMMENSURABLE_LINE_PAIRING`).
- **Legitimate Edge Case:**
  ```text
  Shadow Forecast: Over 2.5 goals (p = 0.5800).
  Comparator Row: Under 2.5 goals (p = 0.4500).
  Paired via complementary orientation: p_comp_over = 1.0 - 0.4500 = 0.5500.
  Line: 2.5 goals (exact match).
  ```
  *Result:* PASS (`COMPLEMENTARY_ORIENTATION_MATCH_ALLOWED`).

---

### C-ML-10: Freeze Receipts Completeness
- **Rule:** Every model package must publish SHA-256 digests for parameters, code artifacts, and forecast outputs.
- **Negative Fixture:**
  ```markdown
  ### Freeze Receipt
  - Parameter file: `PARAMETERS.md`
  - SHA-256: [PENDING / BLANK]
  ```
  *Result:* REJECT (`INCOMPLETE_FREEZE_RECEIPT`).
- **Legitimate Edge Case:**
  ```markdown
  ### Freeze Receipt
  - `PARAMETERS.md` SHA-256: `a94f1c...`
  - `SHADOW_FORECASTS_2026-W42.csv` SHA-256: `4b2e88...`
  - External Workshop Commit: `github.com/org/workshop@8c4d21...`
  ```
  *Result:* PASS (`FULL_CRYPTOGRAPHIC_PROVENANCE`).

---

### C-ML-11: No Silent Fallback / Explicit Fit Failure
- **Rule:** If a model optimization fails to converge, it must raise an explicit `FIT_FAILED` status rather than silently defaulting parameters to 0 or 0.50.
- **Negative Fixture:**
  ```text
  Optimizer max iterations reached without convergence.
  Model emits default attack = 0.0, defence = 0.0, predicting 0.5000 / 0.5000.
  Status: SUCCESS.
  ```
  *Result:* REJECT (`SILENT_FALLBACK_DEFAULT`).
- **Legitimate Edge Case:**
  ```text
  Optimization failed.
  Row emitted: `NOT_ISSUED:FIT_FAILED`, p_model = NULL, reason = "MAX_ITER_EXCEEDED".
  ```
  *Result:* PASS (`EXPLICIT_FAILURE_REPORTED`).

---

### C-ML-12: Unseen / Promoted Team Explicit Priors
- **Rule:** Newly promoted or unknown teams must not receive ungrounded arbitrary ratings. They must be explicitly initialized from league priors with declared variance inflation.
- **Negative Fixture:**
  ```text
  Promoted team (Ipswich Town) assigned arbitrary rating identical to mid-table team (Everton) without documentation.
  ```
  *Result:* REJECT (`UNGROUNDED_UNSEEN_TEAM_PRIOR`).
- **Legitimate Edge Case:**
  ```text
  Promoted team assigned prior: mean = league_relegation_tier_mean, variance = 2.5 * baseline_variance. Source = "LEAGUE_PROFILES.md Â§Championship_Promoted_Prior".
  ```
  *Result:* PASS (`DOCUMENTED_EXPANDED_PRIOR`).

---

### C-ML-13: Temporal Calibration Separation ($T_{\text{CAL}} < T_{\text{TEST}}$)
- **Rule:** Calibration data must strictly precede evaluation/test data in time. No k-fold random splitting across temporal regimes.
- **Negative Fixture:**
  ```text
  Calibration dataset: 2024 to 2026 games randomly sampled (30% holdout).
  Test dataset: 2024 to 2026 games.
  ```
  *Result:* REJECT (`TEMPORAL_LEAKAGE_IN_CALIBRATION`).
- **Legitimate Edge Case:**
  ```text
  Calibration dataset: 2024-2025 completed season.
  Test dataset: 2025-2026 prospective season.
  Temporal boundary: 2025-06-30T23:59:59Z.
  ```
  *Result:* PASS (`STRICT_TEMPORAL_SPLIT`).

---

### C-ML-14: Cricket Chase Censoring (Overshoot Accounting)
- **Rule:** Second innings totals in limited overs cricket must be modelled as censored at the target plus the single-delivery overshoot, never capped flat at the target.
- **Negative Fixture:**
  ```text
  Target: 180 runs.
  Score at 19.4 overs: 178 runs.
  Batsman hits a 6. Final score: 184 runs.
  Model simulation hard-caps chase total at 180.
  ```
  *Result:* REJECT (`ARTIFICIAL_TARGET_CAPPING`).
- **Legitimate Edge Case:**
  ```text
  Model evaluates final legal delivery: target 180, current 178.
  Outcome 6 runs: total 184 (valid overshoot).
  Outcome 1 run: total 179 (wicket/short of target).
  Support extends to target + 5 runs maximum.
  ```
  *Result:* PASS (`CENSORED_WITH_LEGAL_OVERSHOOT`).

---

### C-ML-15: Cricket Toss Mixture Conditioning
- **Rule:** Cricket first innings totals must explicitly model toss decision branches before the toss is called, and condition on the actual decision post-toss.
- **Negative Fixture:**
  ```text
  Toss completed at T-30: Team A wins toss and elects to bowl.
  Model continues to publish 50/50 mixture of bat-first scenarios as if toss unknown.
  ```
  *Result:* REJECT (`UNCONDITIONED_POST_TOSS_FORECAST`).
- **Legitimate Edge Case:**
  ```text
  Pre-toss forecast: P(Total > 175.5) = w_bat * P(T > 175.5 | Team A bats) + (1 - w_bat) * P(T > 175.5 | Team B bats), where w_bat = 0.50.
  Explicit label: `TOSS_UNRESOLVED_MIXTURE`.
  ```
  *Result:* PASS (`PRE_TOSS_MIXTURE_EXPLICITLY_LABELLED`).

---

### C-ML-16: Settlement Revision Integrity
- **Rule:** Any amendment or correction to a settlement must form a linear, acyclic chain referencing the exact parent row ID and disclosing modified keys.
- **Negative Fixture:**
  ```text
  Revision REV-02 references parent REV-01.
  Revision REV-03 also references parent REV-01 without resolving REV-02.
  ```
  *Result:* REJECT (`FORKED_SETTLEMENT_REVISION`).
- **Legitimate Edge Case:**
  ```text
  REV-01 (initial settlement) -> REV-02 (official score adjustment) -> REV-03 (stat correction from governing body resolving REV-02).
  ```
  *Result:* PASS (`LINEAR_REVISION_CHAIN`).

---

### C-ML-17: Commit-Before-Reveal Protocol
- **Rule:** The cryptographic digest of shadow predictions must be published to version control before the earliest event start time.
- **Negative Fixture:**
  ```text
  Kickoff: 12:30 UTC.
  Git commit containing predictions or hash committed at: 12:35 UTC.
  ```
  *Result:* REJECT (`COMMIT_AFTER_EVENT_START`).
- **Legitimate Edge Case:**
  ```text
  Kickoff: 12:30 UTC.
  Git commit with SHA-256 digest committed at: 12:15 UTC.
  Full CSV prediction table pushed at: 13:00 UTC with matching hash.
  ```
  *Result:* PASS (`PRE_START_HASH_COMMIT_VERIFIED`).

---

### C-ML-18: Post-Settlement Market Benchmark Quarantine
- **Rule:** In `MARKET_BENCHMARK_LEDGER.md`, `entered_utc` must be strictly later than `settled_utc`. No closing odds may be recorded prior to official game completion.
- **Negative Fixture:**
  ```markdown
  | match_id | entered_utc | settled_utc |
  | EPL-081 | 2026-10-18T12:00:00Z | 2026-10-18T14:30:00Z |
  Entered UTC is prior to Settled UTC.
  ```
  *Result:* REJECT (`PRE_SETTLEMENT_MARKET_ENTRY_BREACH`).
- **Legitimate Edge Case:**
  ```markdown
  | match_id | entered_utc | settled_utc |
  | EPL-081 | 2026-10-18T18:00:00Z | 2026-10-18T14:30:00Z |
  Entered UTC is 3.5 hours after match settlement.
  No-vig method: shin.
  ```
  *Result:* PASS (`POST_SETTLEMENT_FIREWALL_MAINTAINED`).

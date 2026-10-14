# Fixtures: framework change 2026-10-14-3

Prompt 8 (R35) requires every new check to have at least one negative fixture, naming the check that rejects it, and one legitimate edge case that passes. Every check below is an **executed automated test** in `ml/tests/` (run with `python -m pytest ml/tests`); none is a manual walkthrough unless marked.

| Check (ML_RL_IMPLEMENTATION_FRAMEWORK §12) | Negative fixture → rejecting test | Legitimate edge case → passing test |
|---|---|---|
| C-ML-01 masses sum to 1 | grid 0.55/0.10/0.30/0 → `test_c_ml_01_rejects_masses_not_summing_to_one` | uniform 2×2 grid → `test_c_ml_01_accepts_normalised_grid` |
| C-ML-02 p_decisive = W/(W+L) | W 0.55, P 0.10, L 0.35 must not give 0.55 → `test_c_ml_02_decisive_is_win_over_win_plus_loss` | all push → `None` (`NOT_COMPUTED`) → `test_c_ml_02_all_push_is_not_computed` |
| C-ML-03 lattice support and parity | negative score support → `test_c_ml_03_negative_support_rejected` | Dixon–Coles grid with draws; T and M share parity → `test_c_ml_03_parity_holds_on_lattice` |
| C-ML-04 ladder monotonicity | (property test on a five-line ladder) → `test_c_ml_04_total_ladder_monotone` | equal masses where no support lies between 2.25 and 2.75 → `test_c_ml_04_equal_masses_where_no_support_between_lines` |
| C-ML-05 covering pair | −1.5 must not exceed the winner probability → `test_c_ml_05_plus_handicap_covers_at_least_winner` | exact push mass on a whole line → `test_whole_line_push_mass_is_exact` |
| C-ML-06 known-at | a training row dated after the fit date → `test_c_ml_06_rejects_same_date_training_row` | previous-day game → `test_c_ml_06_previous_day_is_fine` |
| C-ML-07 no market columns | `B365H`, `PSCH`, `home_moneyline`, `spread_line`, `total_line`, `Over Odds` → `test_c_ml_07_market_columns_refused` | `line`, `league_median_line`, `mass_push` → `test_c_ml_07_contract_line_column_allowed` |
| C-ML-08 frozen before start | reveal one minute before the first start → `test_c_ml_17_reveal_refused_before_start_and_on_hash_mismatch` | reveal one minute after → same test |
| C-ML-09 identical-row pairing | **manual:** pairing is on `event_id` in `report.paired_table`; rows lacking either price are dropped (`np.isfinite` on both columns) | same |
| C-ML-10 receipt completeness | tampered file versus committed SHA-256 → `test_c_ml_10_reveal_refuses_tampered_file` | — |
| C-ML-11 no silent fallback | 10 training games → `FitError` → `test_c_ml_11_too_little_data_raises` | — |
| C-ML-12 unknown team labelled | (the test asserts the exact flag) → `test_c_ml_12_new_team_is_flagged` | `NEW_TEAM_PRIOR:NEWCOMER` row is priced, not dropped |
| C-ML-13 calibration fitted on an earlier season only | flipping the current season's outcomes must not move the fitted map → `test_c_ml_13_calibrator_ignores_current_season_labels` | — |
| C-ML-14 chase censoring | **not applicable in r1**: no second-innings model was built (§8.4, second innings) | — |
| C-ML-15 toss branch | (the mixture must be a distribution) → `test_c_ml_15_pre_toss_mixture_is_a_distribution` | 50/50 pre-toss mixture sums to 1 |
| C-ML-16 settlement revision chain | missing final must give `UNRESOLVED`, not VOID or LOSS → `test_c_ml_16_settlement_first_revision_and_push` | whole-line handicap gives `PUSH` → same test |
| C-ML-17 commit, then reveal | before start, or SHA mismatch → tests above | after start with matching SHA |
| C-ML-18 market firewall | **structural:** `ml/decision/lab.py` holds prices in memory only; `writers.write_decision_lab` emits aggregate tables; no row-level price file exists under `research/model_shadow/` (checked at verification) | — |

**Integrity gate and placeholder rule (added after defects were found in the run):**

| Check | Negative fixture → rejecting test | Legitimate edge case → passing test |
|---|---|---|
| OVERTIME_FIELD_IMPLAUSIBLE | 900 explicit rows, 0 overtime → `test_integrity_gate_flags_always_no_overtime_but_not_blank_fields` | blank field (missing) and a 5% overtime share pass, same test |
| IMPLAUSIBLE_SCORE_DISPERSION | a season with margin SD of 3 among seasons of 12 → `test_integrity_gate_flags_collapsed_season_dispersion` | — |
| DATA_HOLD status | PASS with a warning must not become SHADOW_CANDIDATE → `test_status_for_data_hold` | PASS without a warning → SHADOW_CANDIDATE |
| Zero-zero placeholder | 0–0 in Australian rules, basketball and baseball without extras → `test_zero_zero_placeholders_by_sport` | 0–0 in soccer, ice hockey, and a baseball extra-inning tie are kept |
| TB-1 calibration | an edition below 30 games returns None → `test_tb1_calibration_uses_previous_edition_only` | the home edge equals the previous edition's mean margin |
| TB-1 league-mean fallback | — | no season-to-date games: the league mean comes from the training window → `test_tb1_league_mean_falls_back_to_training_window` |

**Additional executed tests:**
- parameter recovery on synthetic data (`test_dixon_coles_recovers_ratings`, `test_gaussian_recovers_ratings_and_home_edge`);
- extra-time mass conservation (`test_resolve_ties_conserves_mass_and_removes_draws`);
- the October 12 recommendation's reweighting example, Over 1.5 moving from 0.55 to 15/28 (`test_reweight_winner_hits_targets_and_moves_totals`);
- refusal to give mass to an empty winner class;
- discrete versus closed-form CRPS;
- the Dixon–Coles rho domain: invalid raises, and a clamp happens only on the flagged path (`test_dixon_coles_rho_clamped_into_valid_domain`);
- de-vig normalisation and the Shin favourite–longshot direction;
- Kelly with and without push, shrinkage and caps;
- CLV arithmetic;
- both bandits learning the better arm;
- AFL and NFL score-text parsing;
- nested AFL names (Sydney / Greater Western Sydney, Adelaide / Port Adelaide, Melbourne / North Melbourne);
- the stage vocabulary.

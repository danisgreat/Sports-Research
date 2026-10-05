"""Fifteen source-bound protocols and explicit experiment-specific measures."""
from pathlib import Path
import json
from research.src.eligibility import digest, file_sha

ROOT = Path(__file__).resolve().parents[2]
VERSION = 'experiment-measures-1'
# These are measurement definitions, not fitted coefficients or chosen sample sizes.
SPECS = {
 'P-492': ('MLB pitcher outs', ['pitcher_outs'], 'PREGAME',
           ['starter_id:text', 'lineup_strength:number', 'removal_risk:number', 'workload_outs:integer'],
           ['pitcher_outs_contract', 'outs_distribution', 'removal_risk_strata'],
           'Build an outs PMF from pitcher workload/removal risk and opponent lineup features; compare with the frozen starter-only baseline.'),
 'P-524': ('KBO starter and bullpen totals', ['total'], 'PREGAME',
           ['starter_id:text', 'starter_workload:integer', 'bullpen_workload:integer', 'reliever_availability:list'],
           ['total_contract', 'total_distribution', 'bullpen_workload_strata'],
           'Build starter-only and starter-plus-relief totals PMFs from time-stamped workload and availability; run the relief ablation on the same fixtures.'),
 'P-525': ('NPB live remaining runs', ['remaining_runs'], 'LIVE',
           ['inning:integer', 'outs:integer', 'bases:integer', 'current_runs:integer', 'batting_half:text'],
           ['live_state_identity', 'remaining_runs_distribution', 'same_horizon_baseline'],
           'Build a state-conditioned remaining-runs PMF and a simpler live-state baseline, using identical inning/outs/bases observation horizons.'),
 'P-526': ('KBO pitching features and ranks', ['margin', 'total'], 'PREGAME',
           ['starter_id:text', 'command_measure:number', 'relief_measure:number', 'ranked_contract_ids:list'],
           ['supplied_rank_match', 'rank_hit_rate', 'representative_per_family'],
           'Build the starter/command/relief candidate and feature ablations; preserve supplied contract IDs and both successful and unsuccessful predictions.'),
 'P-527': ('Basketball rotation and pace scenarios', ['margin', 'total'], 'PREGAME',
           ['rotation_minutes:list', 'pace_scenarios:list', 'scenario_weights:probabilities'],
           ['joint_score_coherence', 'scenario_weight_sum', 'margin_total_calibration'],
           'Build pregame rotation/pace scenarios and their frozen probability mixture; derive margin and total from the same joint score distribution.'),
 'P-528': ('AHL goalie, special teams and empty-net tail', ['total'], 'PREGAME',
           ['goalie_id:text', 'goalie_confirmed:boolean', 'special_teams_exposure:number', 'empty_net_probability:probability'],
           ['goalie_confirmation', 'empty_net_tail', 'total_distribution'],
           'Build goalie/special-teams totals with and without an empty-net component; obtain event-level pilot differences for the power plan.'),
 'P-529': ('NHL regulation and overtime', ['regulation_margin', 'full_game_margin'], 'PREGAME',
           ['goalie_id:text', 'goalie_confirmed:boolean', 'conditional_ot_home_win:probability'],
           ['regulation_full_game_identity', 'ot_probability_coherence', 'three_way_regulation_brier'],
           'Build a regulation home/draw/away PMF and conditional overtime winner component; compare full-game winner probabilities with the unchanged single-winner model.'),
 'P-530': ('MLB opener, bulk workload and wind', ['total'], 'PREGAME',
           ['opener_id:text', 'bulk_pitcher_id:text', 'opener_outs:integer', 'bulk_outs:integer', 'wind_direction_degrees:number', 'wind_speed:number'],
           ['opener_bulk_identity', 'weather_availability', 'original_model_card_separation'],
           'Build opener/bulk workload and measured-wind feature ablations; freeze separate model and card probability artifacts before evaluation.'),
 'P-531': ('WNBA joint scores and late separation', ['margin', 'total'], 'PREGAME',
           ['starting_units:list', 'late_separation_probability:probability', 'scoring_floor:number'],
           ['joint_score_coherence', 'starting_unit_confirmation', 'tail_interval_coverage'],
           'Build the joint team-score PMF with late-separation/scoring-floor components; compare against the unchanged model at identical margin and total thresholds.'),
 'P-532': ('NBL free throws and offensive rebounds', ['margin', 'total'], 'PREGAME',
           ['free_throw_rate:probability', 'offensive_rebound_rate:probability', 'pace:number', 'injury_availability:list'],
           ['pace_feature_ablation', 'joint_score_coherence', 'availability_timing'],
           'Build separate free-throw, offensive-rebound and pace feature ablations in a shadow cohort; retain missing-feature and abstention records.'),
 'P-533': ('KBO tied late innings and extra innings', ['total'], 'PREGAME',
           ['late_tie_scoring_probability:probability', 'extra_inning_probability:probability', 'ranked_contract_ids:list'],
           ['supplied_rank_match', 'regulation_extra_innings_identity', 'late_run_component'],
           'Build separate regulation late-tie and extra-inning scoring components; require exact supplied-to-ranked contract matching before comparison.'),
 'P-534': ('NRL joint margin, total and late scores', ['margin', 'total'], 'PREGAME',
           ['late_score_probability:probability', 'lineup_availability:list'],
           ['joint_score_coherence', 'winner_cover_separation', 'gapped_threshold_calibration'],
           'Build a joint margin/total distribution with a late-score branch; freeze all winner, cover and total thresholds and test tail calibration.'),
 'P-535': ('Basketball replacement rotation and injuries', ['margin', 'total'], 'PREGAME',
           ['available_rotation:list', 'expected_minutes:list', 'replacement_usage:number'],
           ['joint_score_coherence', 'replacement_minutes', 'heavy_favourite_tail'],
           'Compare a uniform injury penalty with remaining-rotation usage/depth features; freeze expected minutes before the prediction cutoff.'),
 'P-536': ('Basketball rotation, rest and asymmetric tails', ['margin', 'total'], 'PREGAME',
           ['available_rotation:list', 'rest_hours:number', 'home_tail_parameter:number', 'away_tail_parameter:number'],
           ['joint_score_coherence', 'elapsed_rest_hours', 'asymmetric_score_tails'],
           'Build asymmetric team-score PMFs using actual rotation and elapsed rest hours; compare with the unchanged total-average model.'),
 'P-537': ('Football period and corners adapter', ['first_half_total', 'corners'], 'PREGAME',
           ['phase_provider_records:list', 'owner_phase_verified:boolean', 'conflict_resolved:boolean'],
           ['period_provider_identity', 'two_phase_records', 'adapter_corpus_perfect'],
           'First validate first-half/full-game/extra-time and corners-provider parsing on a fixed audited corpus; only then build and test forecast models.'),
}

def proposals(root=ROOT):
    root=Path(root)
    register=json.loads((root/'research/improvement_register.json').read_text(encoding='utf-8'))
    rows=list(register['records'])
    for ref in register['additional_review_registers']:
        path=root/ref['path']
        if file_sha(path)!=ref['sha256']:raise ValueError('Additional proposal register changed')
        rows.extend(json.loads(path.read_text(encoding='utf-8'))['records'])
    if len(rows)!=15 or {r['canonical_id'] for r in rows}!=set(SPECS):
        raise ValueError('Exactly fifteen distinct proposal mappings required')
    for row in rows:
        if row['status']!='PROPOSED_NOT_TESTED' or row['performance_eligible'] is not False:
            raise ValueError('Proposal was promoted without experiment evidence')
    return sorted(rows,key=lambda r:int(r['canonical_id'].split('-')[1]))

def template(proposal):
    cid=proposal['canonical_id'];title,targets,horizon,fields,checks,next_step=SPECS[cid]
    return dict(schema=VERSION,experiment_id=proposal['proposal_id'],source_card_id=cid,
        hypothesis=proposal['hypothesis_and_acceptance'],proposal_sha256=digest(proposal),
        status='MEASURES_IMPLEMENTED_NOT_FROZEN',performance_eligible=False,title=title,horizon=horizon,
        targets={name:dict(metric=name,weight=1/len(targets)) for name in targets},
        required_features={f.split(':')[0]:f.split(':')[1] for f in fields},
        process_checks=checks,primary_metric='CONTRACT_BRIER',secondary_metrics=['LOG_LOSS','CRPS','RELIABILITY','INTERVAL_COVERAGE','INTERVAL_SCORE'],
        inference=dict(method='PAIRED_WEEK_BLOCK_PERCENTILE_BOOTSTRAP',family_size=15,alpha_family=.05,
                       bootstrap_reps=60000,seed=20261005,minimum_blocks=20,
                       caveat='Approximate intervals assume week blocks represent exchangeable sampling units; audit serial dependence before freeze.'),
        acceptance=dict(minimum_brier_improvement=None,max_logloss_deterioration=None,
                        max_reliability_deterioration=None,max_interval_score_deterioration={target:None for target in targets},
                        minimum_numeric_coverage=None,zero_identity_or_timing_failures=True),
        candidate_model_ref=None,baseline_model_ref=None,cohort_ref=None,power_plan_ref=None,
        adapter_validation_ref=None,block_dependence_audit_ref=None,
        required_next_steps=[next_step,
          'Collect time-stamped sports-only inputs; retain owner bodies, missingness and exact contract/period definitions.',
          'Freeze a simple comparator and a candidate artifact; validate on development data without using the motivating game as untouched evidence.',
          'Estimate paired-loss variation on separate pilot weeks, select a scientifically justified minimum worthwhile improvement and guardrail tolerances, and record the sample plan.',
          'Complete an exact chronological future cohort and dependence/adapter audits; freeze this protocol before any cohort forecast.',
          'Capture predictions before outcomes and collect every cohort disposition; evaluate once at the locked terminal sample.',
          'Review uncertainty and calibration; obtain the separate source/qualification approvals before any operational promotion.'])

def catalog(root=ROOT):
    return [template(row) for row in proposals(root)]

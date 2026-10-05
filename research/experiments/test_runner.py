"""End-to-end synthetic fixtures, never stored as actual experiment results."""
from copy import deepcopy
from datetime import datetime,timedelta,timezone
from pathlib import Path
import json
import pytest
from .catalog import ROOT,catalog
from .runner import (adapter_check,capture,evaluate,freeze,joint_check,load,read_lock,
                     readiness,validate_features,validate_forecast,write_new)
from .measures import sample_plan
from research.src.eligibility import digest,file_sha

def ref(root,path,value):
    target=root/path;write_new(target,value)
    return dict(path=path,sha256=file_sha(target))

@pytest.fixture
def experiment(tmp_path):
    root=tmp_path
    register=json.loads((ROOT/'research/improvement_register.json').read_text())
    for path in ['research/improvement_register.json',*[r['path'] for r in register['additional_review_registers']]]:
        target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/path).read_bytes())
    paths=['research/experiments/'+name for name in ('__init__.py','catalog.py','measures.py','runner.py','verify.py')]
    paths+=['research/src/eligibility.py','research/src/ledger.py','research/requirements.lock.txt']
    for path in paths:
        target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/path).read_bytes())
    config=next(p for p in catalog(root) if p['source_card_id']=='P-524')
    zero=datetime(2027,1,1,tzinfo=timezone.utc)
    source=ref(root,'source.json',dict(label='SYNTHETIC_UNIT_FIXTURE_ONLY'))
    code=ref(root,'model.json',dict(label='SYNTHETIC_UNIT_FIXTURE_ONLY'))
    for label in ('candidate','baseline'):
        config[label+'_model_ref']=ref(root,label+'.json',dict(model_version=label+'-TEST',sports_only=True,
                                    training_last_outcome_utc='2026-01-01T00:00:00Z',dependency_refs=[code]))
    values=[-.03+(.001 if i%2 else -.001) for i in range(8)]
    pilot=ref(root,'pilot.json',dict(differences=values,weeks=[str(i) for i in range(8)],last_outcome_utc='2026-01-01T00:00:00Z',basis_refs=[source]))
    plan=sample_plan(values,[str(i) for i in range(8)],.005,.03)
    plan.update(pilot_ref=pilot,effect_size_rationale='SYNTHETIC_UNIT_FIXTURE_ONLY')
    config['power_plan_ref']=ref(root,'plan.json',plan)
    config['acceptance'].update(minimum_brier_improvement=.005,max_logloss_deterioration=0.,max_reliability_deterioration=0.,max_interval_score_deterioration={'total':0.},minimum_numeric_coverage=1.)
    events=[];payloads=[];outcomes=[]
    for i in range(20):
        start=zero+timedelta(days=3+7*i,hours=18)
        identity=dict(league='SYNTHETIC_KBO',season='TEST',event_id=f'SYNTHETIC-{i}')
        contract=dict(contract_id=f'CONTRACT-{i}',event_id=identity['event_id'],metric='total',threshold=1.5,
                      rule='OVER',period='FULL_GAME',includes_overtime=True,provider='SYNTHETIC')
        event=dict(**identity,scheduled_start_utc=start.isoformat(),targets={'total':contract});events.append(event)
        fields=dict(starter_id='SYNTHETIC_PITCHER',starter_workload=4,bullpen_workload=2,reliever_availability=['SYNTHETIC_RELIEVER'])
        features_ref=ref(root,f'features-{i}.json',dict(event_id=identity['event_id'],available_utc=(start-timedelta(hours=2)).isoformat(),features=fields,source_refs=[source]))
        features={name:dict(value=value,available_utc=(start-timedelta(hours=2)).isoformat(),evidence_ref=features_ref) for name,value in fields.items()}
        arms={label:dict(model_version=label+'-TEST',targets={'total':dict(support=[0,1,2],probabilities=([.1,.1,.8] if label=='candidate' else [.4,.4,.2]))}) for label in ('candidate','baseline')}
        payload=dict(**identity,disposition='FORECAST',state='PREGAME',cutoff_utc=(start-timedelta(hours=1,minutes=1)).isoformat(),features=features,**arms)
        payloads.append((payload,start-timedelta(hours=1)))
        facts=ref(root,f'facts-{i}.json',dict(**identity,state='FINAL',actual_start_utc=start.isoformat(),
                  observed_utc=(start+timedelta(hours=4)).isoformat(),targets={'total':dict(contract=contract,value=2)},source_refs=[source]))
        outcomes.append(dict(**identity,state='FINAL',facts_ref=facts))
    config['cohort_ref']=ref(root,'cohort.json',dict(events=events))
    cases=[]
    for i in range(20):
        role=('NORMAL','CONFLICT','WRONG_EVENT')[i%3]
        result={'state':'FINAL' if role=='NORMAL' else 'REJECTED'}
        cases.append(dict(case_id=str(i),role=role,body_ref=source,expected=result,observed=result))
    config['adapter_validation_ref']=ref(root,'adapter.json',dict(reviewed_by='SYNTHETIC_UNIT_FIXTURE_ONLY',cases=cases,adapter_code_ref=code))
    config['block_dependence_audit_ref']=ref(root,'dependence.json',dict(reviewed_by='SYNTHETIC_UNIT_FIXTURE_ONLY',block_definition='ISO_WEEK',rationale='Synthetic isolated weeks',basis_refs=[source]))
    lock_path=root/'lock.json';journal=root/'forecasts.jsonl';outcome_path=root/'outcomes.json'
    write_new(outcome_path,dict(records=outcomes))
    return dict(root=root,config=config,now=zero,events=events,payloads=payloads,outcomes=outcomes,
                lock=lock_path,journal=journal,outcome_path=outcome_path)

def run_all(fixture):
    freeze(fixture['config'],fixture['lock'],root=fixture['root'],now=fixture['now'])
    for payload,when in fixture['payloads']:capture(fixture['lock'],payload,fixture['journal'],root=fixture['root'],now=when)
    return evaluate(fixture['lock'],fixture['journal'],fixture['outcome_path'],root=fixture['root'],now=datetime(2028,1,1,tzinfo=timezone.utc))

def test_all_fifteen_have_explicit_feature_target_measure_and_next_step_definitions():
    protocols=catalog()
    assert len(protocols)==15 and len({p['experiment_id'] for p in protocols})==15
    for p in protocols:
        assert p['targets'] and p['required_features'] and p['process_checks'] and len(p['required_next_steps'])==7
        assert sum(t['weight'] for t in p['targets'].values())==pytest.approx(1)
        assert p['acceptance']['minimum_brier_improvement'] is None
        assert readiness(p)['status']=='INPUTS_REQUIRED'
        assert p['performance_eligible'] is False

def test_cannot_freeze_missing_inputs_or_modify_source_hypothesis(experiment):
    cfg=deepcopy(experiment['config']);cfg['baseline_model_ref']=None
    with pytest.raises(ValueError,match='missing inputs'):freeze(cfg,experiment['lock'],root=experiment['root'],now=experiment['now'])
    cfg=deepcopy(experiment['config']);cfg['hypothesis']='Changed after seeing results'
    with pytest.raises(ValueError,match='hypothesis'):freeze(cfg,experiment['lock'],root=experiment['root'],now=experiment['now'])

def test_complete_synthetic_pipeline_scores_once_without_promoting_model(experiment):
    result=run_all(experiment)
    assert result['status']=='CANDIDATE_FOR_REVIEW'
    assert result['scored_events']==result['declared_events']==20
    assert result['inference']['brier']['mean']==pytest.approx(-.6)
    assert result['inference']['brier']['confidence_level']==pytest.approx(1-.05/15)
    assert result['performance_eligible'] is False and result['model_promoted'] is False

def test_equal_models_retain_baseline(experiment):
    for payload,_ in experiment['payloads']:payload['candidate']['targets']=deepcopy(payload['baseline']['targets'])
    result=run_all(experiment)
    assert result['status']=='RETAIN_BASELINE'
    assert result['inference']['brier']['ci']==[0,0]

def test_pending_earlier_member_cannot_be_dropped_for_later_successes(experiment):
    experiment['outcomes'][0]['state']='PENDING'
    experiment['outcome_path'].unlink();write_new(experiment['outcome_path'],dict(records=experiment['outcomes']))
    result=run_all(experiment)
    assert result['status']=='INCOMPLETE' and result['counts']['PENDING']==1
    assert result['scored_events']==19 and not result['inference']

def test_actual_start_conflict_is_preserved_as_invalid_evidence(experiment):
    record=experiment['outcomes'][0];facts=load(experiment['root']/record['facts_ref']['path'])
    facts['actual_start_utc']=(experiment['payloads'][0][1]-timedelta(minutes=1)).isoformat()
    record['facts_ref']=ref(experiment['root'],'bad-actual-start.json',facts)
    experiment['outcome_path'].unlink();write_new(experiment['outcome_path'],dict(records=experiment['outcomes']))
    result=run_all(experiment)
    assert result['status']=='INCOMPLETE' and result['counts']['INVALID_EVIDENCE']==1
    assert 'Actual-start' in result['errors'][0]['reason']

def test_changed_contract_provider_is_not_graded(experiment):
    record=experiment['outcomes'][0];facts=load(experiment['root']/record['facts_ref']['path'])
    facts['targets']['total']['contract']['provider']='OTHER'
    record['facts_ref']=ref(experiment['root'],'bad-provider.json',facts)
    experiment['outcome_path'].unlink();write_new(experiment['outcome_path'],dict(records=experiment['outcomes']))
    result=run_all(experiment)
    assert result['status']=='INCOMPLETE' and result['counts']['INVALID_EVIDENCE']==1

def test_duplicate_capture_and_journal_mutation_are_rejected(experiment):
    freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])
    payload,when=experiment['payloads'][0]
    capture(experiment['lock'],payload,experiment['journal'],root=experiment['root'],now=when)
    before=experiment['journal'].read_bytes()
    with pytest.raises(ValueError,match='already captured'):capture(experiment['lock'],payload,experiment['journal'],root=experiment['root'],now=when)
    assert experiment['journal'].read_bytes()==before
    row=json.loads(before);row['payload']['candidate']['targets']['total']['probabilities']=[.2,.2,.6]
    experiment['journal'].write_text(json.dumps(row)+'\n')
    with pytest.raises(ValueError,match='journal changed'):evaluate(experiment['lock'],experiment['journal'],experiment['outcome_path'],root=experiment['root'])

def test_available_after_cutoff_and_late_capture_fail_before_append(experiment):
    freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])
    payload,when=deepcopy(experiment['payloads'][0]);payload['features']['starter_id']['available_utc']=(when+timedelta(seconds=1)).isoformat()
    with pytest.raises(ValueError,match='after forecast cutoff'):capture(experiment['lock'],payload,experiment['journal'],root=experiment['root'],now=when)
    payload,when=experiment['payloads'][0]
    with pytest.raises(ValueError,match='after scheduled start'):capture(experiment['lock'],payload,experiment['journal'],root=experiment['root'],now=when+timedelta(hours=2))
    assert not experiment['journal'].exists()

def test_model_dependency_changes_are_detected_after_freeze(experiment):
    freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])
    (experiment['root']/'model.json').write_bytes(b'Changed model code')
    with pytest.raises(ValueError,match='hash mismatch'):read_lock(experiment['lock'],experiment['root'])

def test_measurement_code_changes_are_detected_after_freeze(experiment):
    freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])
    (experiment['root']/'research/experiments/measures.py').write_bytes(b'Changed score definition')
    with pytest.raises(ValueError,match='hash mismatch'):read_lock(experiment['lock'],experiment['root'])

def test_lock_and_report_outputs_refuse_overwrite(experiment):
    freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])
    with pytest.raises(FileExistsError):freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])

def test_reusing_native_event_under_another_season_fails(experiment):
    cohort=load(experiment['root']/experiment['config']['cohort_ref']['path'])
    cohort['events'][1]['event_id']=cohort['events'][0]['event_id'];cohort['events'][1]['season']='OTHER'
    experiment['config']['cohort_ref']=ref(experiment['root'],'duplicate-native.json',cohort)
    with pytest.raises(ValueError,match='another season'):freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])

def test_joint_marginals_must_match_same_score_matrix():
    arm=dict(joint=dict(home_support=[0,1],away_support=[0,1],probabilities=[[.1,.2],[.3,.4]]),
             targets=dict(margin=dict(support=[-1,0,1],probabilities=[.2,.5,.3]),total=dict(support=[0,1,2],probabilities=[.1,.5,.4])))
    joint_check(arm)
    arm['targets']['total']['probabilities']=[.2,.4,.4]
    with pytest.raises(ValueError,match='marginal'):joint_check(arm)

def test_live_state_outs_and_bases_are_bounded(experiment):
    cfg=next(p for p in catalog(experiment['root']) if p['source_card_id']=='P-525')
    values=dict(inning=1,outs=3,bases=0,current_runs=0,batting_half='TOP')
    evidence=ref(experiment['root'],'live-feature-test.json',dict(features=values,available_utc='2026-01-01T00:00:00Z',source_refs=[experiment['config']['candidate_model_ref']]))
    features={k:dict(value=v,available_utc='2026-01-01T00:00:00Z',evidence_ref=evidence) for k,v in values.items()}
    with pytest.raises(ValueError,match='live inning'):validate_features(features,cfg,experiment['root'],experiment['now'])

def test_phase_adapter_requires_extra_time_and_rejects_conflict_grading(experiment):
    cfg=next(p for p in catalog(experiment['root']) if p['source_card_id']=='P-537')
    report=load(experiment['root']/experiment['config']['adapter_validation_ref']['path'])
    with pytest.raises(ValueError,match='failure/period'):adapter_check(report,cfg,experiment['root'])
    report['cases'][0]['role']='EXTRA_TIME';report['cases'][1]['observed']={'state':'FINAL'};report['cases'][1]['expected']={'state':'FINAL'}
    with pytest.raises(ValueError,match='silently graded'):adapter_check(report,cfg,experiment['root'])

def test_rank_contract_substitution_is_rejected(experiment):
    cfg=next(p for p in catalog(experiment['root']) if p['source_card_id']=='P-533')
    values=dict(late_tie_scoring_probability=.2,extra_inning_probability=.1,ranked_contract_ids=['A','B','C','D'])
    source=ref(experiment['root'],'ranked-features.json',dict(event_id='SYNTHETIC',available_utc='2026-01-01T00:00:00Z',features=values,source_refs=[experiment['config']['candidate_model_ref']]))
    features={k:dict(value=v,available_utc='2026-01-01T00:00:00Z',evidence_ref=source) for k,v in values.items()}
    event=dict(league='TEST',season='TEST',event_id='SYNTHETIC',scheduled_start_utc='2027-01-04T00:00:00Z',targets={'total':experiment['events'][0]['targets']['total']},ranked_contracts=[{'contract':{'contract_id':x}} for x in ['A','B','C','OTHER']])
    payload=dict(league='TEST',season='TEST',event_id='SYNTHETIC',state='PREGAME',cutoff_utc='2027-01-02T00:00:00Z',features=features)
    payload.update({label:dict(model_version=label+'-TEST',targets={'total':dict(support=[0,1,2],probabilities=[.1,.2,.7])}) for label in ('candidate','baseline')})
    lock=dict(config={**cfg,'candidate_model_ref':experiment['config']['candidate_model_ref'],'baseline_model_ref':experiment['config']['baseline_model_ref']},locked_utc='2027-01-01T00:00:00Z')
    with pytest.raises(ValueError,match='ranked contracts differ'):validate_forecast(payload,event,lock,experiment['root'],datetime(2027,1,2,tzinfo=timezone.utc))


def domain_payload(fixture,cid,values,targets):
    cfg=next(p for p in catalog(fixture['root']) if p['source_card_id']==cid)
    source=ref(fixture['root'],cid+'-features.json',dict(event_id='SYNTHETIC',available_utc='2027-01-01T01:00:00Z',features=values,source_refs=[fixture['config']['candidate_model_ref']]))
    features={k:dict(value=v,available_utc='2027-01-01T01:00:00Z',evidence_ref=source) for k,v in values.items()}
    contracts={name:dict(contract_id=name,event_id='SYNTHETIC',metric=name,threshold=0 if 'margin' in name else 1.5,rule='HOME_1X2' if 'margin' in name else 'OVER',period='REGULATION' if name=='regulation_margin' else 'FIRST_HALF' if name=='first_half_total' else 'FULL_GAME',includes_overtime=name!='regulation_margin' and name!='first_half_total',provider='SYNTHETIC') for name in targets}
    event=dict(league='TEST',season='TEST',event_id='SYNTHETIC',scheduled_start_utc='2027-01-04T00:00:00Z',targets=contracts)
    payload=dict(league='TEST',season='TEST',event_id='SYNTHETIC',state='PREGAME',cutoff_utc='2027-01-02T00:00:00Z',features=features)
    payload.update({label:dict(model_version=label+'-TEST',targets=deepcopy(targets)) for label in ('candidate','baseline')})
    lock=dict(config={**cfg,'candidate_model_ref':fixture['config']['candidate_model_ref'],'baseline_model_ref':fixture['config']['baseline_model_ref']},locked_utc='2027-01-01T00:00:00Z')
    return cfg,payload,event,lock


def test_nhl_conditional_overtime_probability_is_enforced(experiment):
    targets=dict(regulation_margin=dict(support=[-1,0,1],probabilities=[.3,.2,.5]),full_game_margin=dict(support=[-1,1],probabilities=[.35,.65]))
    cfg,payload,event,lock=domain_payload(experiment,'P-529',dict(goalie_id='TEST',goalie_confirmed=True,conditional_ot_home_win=.75),targets)
    when=datetime(2027,1,2,tzinfo=timezone.utc)
    validate_forecast(payload,event,lock,experiment['root'],when)
    payload['candidate']['targets']['full_game_margin']['probabilities']=[.3,.7]
    with pytest.raises(ValueError,match='overtime probability'):validate_forecast(payload,event,lock,experiment['root'],when)


def test_opener_weather_requires_original_model_artifact(experiment):
    cfg,payload,event,lock=domain_payload(experiment,'P-530',dict(opener_id='OPENER',bulk_pitcher_id='BULK',opener_outs=3,bulk_outs=12,wind_direction_degrees=90,wind_speed=4),dict(total=dict(support=[0,1,2],probabilities=[.1,.2,.7])))
    when=datetime(2027,1,2,tzinfo=timezone.utc)
    with pytest.raises(KeyError,match='model_targets'):validate_forecast(payload,event,lock,experiment['root'],when)
    payload['candidate']['model_targets']=deepcopy(payload['baseline']['targets'])
    validate_forecast(payload,event,lock,experiment['root'],when)


def test_football_phase_records_match_both_targets_and_retained_bodies(experiment):
    records=[]
    for name,period in [('first_half_total','FIRST_HALF'),('corners','FULL_GAME')]:
        body=ref(experiment['root'],name+'-phase.json',dict(event_id='SYNTHETIC',period=period,provider='SYNTHETIC',metric=name))
        records.append(dict(record_id=name,event_id='SYNTHETIC',period=period,provider='SYNTHETIC',metric=name,field_owner=True,body_ref=body))
    cfg,payload,event,lock=domain_payload(experiment,'P-537',dict(phase_provider_records=records,owner_phase_verified=True,conflict_resolved=True),{name:dict(support=[0,1,2],probabilities=[.1,.2,.7]) for name in ('first_half_total','corners')})
    when=datetime(2027,1,2,tzinfo=timezone.utc)
    validate_forecast(payload,event,lock,experiment['root'],when)
    event['targets']['corners']['provider']='OTHER'
    with pytest.raises(ValueError,match='does not match frozen target'):validate_forecast(payload,event,lock,experiment['root'],when)
    event['targets']['corners']['provider']='SYNTHETIC'
    body=load(experiment['root']/records[0]['body_ref']['path']);body['event_id']='OTHER'
    records[0]['body_ref']=ref(experiment['root'],'mismatched-phase.json',body)
    payload['features']['phase_provider_records']['evidence_ref']=ref(experiment['root'],'mismatched-phase-features.json',dict(event_id='SYNTHETIC',available_utc='2027-01-01T01:00:00Z',features={'phase_provider_records':records},source_refs=[experiment['config']['candidate_model_ref']]))
    with pytest.raises(ValueError,match='metadata differs'):validate_forecast(payload,event,lock,experiment['root'],when)


def test_scenario_weights_cannot_mismatch_pace_branches(experiment):
    cfg,payload,event,lock=domain_payload(experiment,'P-527',dict(rotation_minutes=[20,30],pace_scenarios=[70,90],scenario_weights=[1]),{name:dict(support=[0,1,2],probabilities=[.1,.2,.7]) for name in ('margin','total')})
    with pytest.raises(ValueError,match='weights/pace'):validate_forecast(payload,event,lock,experiment['root'],datetime(2027,1,2,tzinfo=timezone.utc))


def test_missing_entire_journal_remains_an_incomplete_result(experiment):
    freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])
    result=evaluate(experiment['lock'],experiment['journal'],experiment['outcome_path'],root=experiment['root'],now=datetime(2028,1,1,tzinfo=timezone.utc))
    assert result['status']=='INCOMPLETE' and result['counts']['MISSING_FORECAST']==20
    assert result['forecasts_sha256'] is None and result['scored_events']==0


def test_negative_terminal_total_is_not_graded(experiment):
    record=experiment['outcomes'][0];facts=load(experiment['root']/record['facts_ref']['path'])
    facts['targets']['total']['value']=-1
    record['facts_ref']=ref(experiment['root'],'negative-total.json',facts)
    experiment['outcome_path'].unlink();write_new(experiment['outcome_path'],dict(records=experiment['outcomes']))
    result=run_all(experiment)
    assert result['status']=='INCOMPLETE' and result['counts']['INVALID_EVIDENCE']==1
    assert 'Negative sporting' in result['errors'][0]['reason']


def test_boolean_numeric_coverage_is_rejected(experiment):
    experiment['config']['acceptance']['minimum_numeric_coverage']=True
    with pytest.raises(ValueError,match='Numeric coverage'):freeze(experiment['config'],experiment['lock'],root=experiment['root'],now=experiment['now'])


def test_integer_marginals_cannot_hide_fractional_team_scores():
    arm=dict(joint=dict(home_support=[.5],away_support=[.5],probabilities=[[1.]]),targets=dict(margin=dict(support=[0],probabilities=[1.]),total=dict(support=[1],probabilities=[1.])))
    with pytest.raises(ValueError,match='integer valued'):joint_check(arm)


@pytest.mark.parametrize('entry',[True,'1'])
def test_joint_matrix_does_not_coerce_booleans_or_strings(entry):
    arm=dict(joint=dict(home_support=[1],away_support=[0],probabilities=[[entry]]),targets=dict(margin=dict(support=[1],probabilities=[1.]),total=dict(support=[1],probabilities=[1.])))
    with pytest.raises(ValueError,match='actual numeric'):joint_check(arm)

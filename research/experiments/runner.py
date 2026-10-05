"""Immutable development-experiment locks, forecast capture and complete readback.

Hashes prove custody, not source truth or independent collection. This module
never writes a canonical P-ID, changes a qualification or admits live skill.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import math
import platform
from importlib.metadata import version
from pathlib import Path
import uuid
import numpy as np
from research.src.eligibility import aware_time, canonical_bytes, checked_json, checked_ref, digest, file_sha
from research.src.ledger import locked
from .catalog import ROOT, VERSION, catalog
from .measures import (contract_probabilities, distribution_scores, outcome_index,
                       paired_blocks, paired_reliability, pmf, probability_scores, reliability, sample_plan)

def need(condition,message):
    if not condition:raise ValueError(message)

def write_new(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:stream.write(canonical_bytes(value)+b'\n')

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def runtime():
    return dict(python=platform.python_version(),numpy=version('numpy'),scipy=version('scipy'))

def evaluation_refs(root):
    paths=['research/experiments/'+name for name in ('__init__.py','catalog.py','measures.py','runner.py','verify.py')]
    paths+=['research/src/eligibility.py','research/src/ledger.py','research/requirements.lock.txt']
    return [dict(path=name,sha256=file_sha(Path(root)/name)) for name in paths]

def expected(config,root):
    return next(p for p in catalog(root) if p['experiment_id']==config['experiment_id'])

def check_template(config,root=ROOT):
    original=expected(config,root)
    for key in ('schema','experiment_id','source_card_id','proposal_sha256','hypothesis','title','horizon',
                'targets','required_features','process_checks','primary_metric','secondary_metrics','inference'):
        need(config[key]==original[key],'Changed measurement definition: '+key)
    need(config['performance_eligible'] is False,'Experiment cannot grant performance admission')
    return original

def readiness(config,root=ROOT):
    check_template(config,root);missing=[]
    for name in ('candidate_model_ref','baseline_model_ref','cohort_ref','power_plan_ref','adapter_validation_ref','block_dependence_audit_ref'):
        if not config.get(name):missing.append(name)
    for name,value in config['acceptance'].items():
        if value is None:missing.append('acceptance.'+name)
        elif isinstance(value,dict):
            missing.extend('acceptance.'+name+'.'+k for k,v in value.items() if v is None)
    return dict(experiment_id=config['experiment_id'],measures='IMPLEMENTED',
                status='INPUTS_REQUIRED' if missing else 'READY_FOR_FREEZE_VALIDATION',missing=missing,
                next_steps=config['required_next_steps'],experiment_run=False,performance_eligible=False)

def event_key(event):
    fields=('league','season','event_id')
    need(all(isinstance(event.get(k),str) and event[k] for k in fields),'Exact league/season/native event identity required')
    return tuple(event[k] for k in fields)

def contract_check(contract,metric,event_id):
    need(contract.get('metric')==metric and contract.get('event_id')==event_id,'Contract event/metric mismatch')
    need(isinstance(contract.get('contract_id'),str) and bool(contract['contract_id']),'Exact contract ID missing')
    need(contract.get('period') in {'FULL_GAME','REGULATION','FIRST_HALF','REMAINING_GAME'},'Explicit sporting period required')
    need(isinstance(contract.get('includes_overtime'),bool),'Explicit overtime/extra-innings scope required')
    need(isinstance(contract.get('provider'),str) and bool(contract['provider']),'Frozen field provider required')
    if metric=='regulation_margin':need(contract['period']=='REGULATION' and not contract['includes_overtime'],'Regulation period mismatch')
    elif metric=='first_half_total':need(contract['period']=='FIRST_HALF' and not contract['includes_overtime'],'First-half period mismatch')
    elif metric=='remaining_runs':need(contract['period']=='REMAINING_GAME','Live remaining-run period mismatch')
    else:need(contract['period']=='FULL_GAME','Full-game period mismatch')
    if metric=='full_game_margin':need(contract['includes_overtime'],'Full-game NHL must include overtime')
    if metric in {'regulation_margin','full_game_margin'}:
        need(contract['rule']=='HOME_1X2' and contract['threshold']==0,'NHL winner endpoint requires three-way margin at zero')
    # Exercise threshold/rule validation without substituting a probability.
    contract_probabilities(dict(support=[0],probabilities=[1]),contract)

def adapter_check(report,config,root):
    need(isinstance(report.get('reviewed_by'),str) and bool(report['reviewed_by']),'Adapter review identity missing')
    cases=report.get('cases',[])
    need(len(cases)>=20,'Adapter validation needs at least twenty declared cases')
    need(len({c['case_id'] for c in cases})==len(cases),'Adapter case IDs must be unique')
    required={'NORMAL','WRONG_EVENT','CONFLICT'}
    if config['source_card_id']=='P-537':required.add('EXTRA_TIME')
    need(required<={c['role'] for c in cases},'Adapter corpus lacks required failure/period cases')
    for case in cases:
        checked_ref(case['body_ref'],root)
        need(case['expected']==case['observed'],'Adapter mismatch in '+case['case_id'])
        if case['role'] in {'WRONG_EVENT','CONFLICT'}:
            need(case['observed']['state'] in {'REJECTED','UNRESOLVED'},'Conflicted/wrong event silently graded')
    checked_ref(report['adapter_code_ref'],root)
    return dict(cases=len(cases),mismatches=0,
                limitation='Retained test expectations/results and code hashes, not an independent re-execution of an official provider adapter.')

def freeze(config,output,*,root=ROOT,now=None):
    root=Path(root).resolve();now=now or datetime.now(timezone.utc)
    check_template(config,root)
    need(not readiness(config,root)['missing'],'Protocol still has missing inputs or acceptance settings')
    need(config['status']=='MEASURES_IMPLEMENTED_NOT_FROZEN','Only a new draft may be frozen')
    acceptance=config['acceptance']
    need(acceptance['zero_identity_or_timing_failures'] is True,'Identity/timing guardrail cannot be waived')
    for name in ('minimum_brier_improvement','max_logloss_deterioration','max_reliability_deterioration'):
        value=acceptance[name]
        need(isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value) and value>=0,'Invalid tolerance: '+name)
    need(0<acceptance['minimum_brier_improvement']<1,'Positive meaningful Brier improvement required')
    tolerances=acceptance['max_interval_score_deterioration']
    need(set(tolerances)==set(config['targets']),'Interval tolerance required separately for every target/unit')
    need(all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and v>=0 for v in tolerances.values()),'Invalid per-target interval tolerance')
    need(isinstance(acceptance['minimum_numeric_coverage'],(int,float)) and not isinstance(acceptance['minimum_numeric_coverage'],bool) and .5<=acceptance['minimum_numeric_coverage']<=1,'Numeric coverage must be predeclared between .5 and 1')
    models=[]
    for name in ('candidate_model_ref','baseline_model_ref'):
        model=checked_json(config[name],root)
        need(isinstance(model.get('model_version'),str) and bool(model['model_version']) and model.get('sports_only') is True,'Model artifact identity/firewall missing')
        need(aware_time(model['training_last_outcome_utc'])<now,'Model training cutoff crosses lock')
        need(model.get('dependency_refs'),'Model dependency receipts required')
        for ref in model['dependency_refs']:checked_ref(ref,root)
        models.append(model)
    need(models[0]['model_version']!=models[1]['model_version'],'Candidate and comparator must be distinct versions')
    cohort=checked_json(config['cohort_ref'],root);events=cohort['events']
    need(bool(events) and len({event_key(e) for e in events})==len(events),'Empty or duplicate cohort')
    need(len({(e['league'],e['event_id']) for e in events})==len(events),'Native event reused under another season')
    ordered=sorted(events,key=lambda e:(aware_time(e['scheduled_start_utc']),event_key(e)))
    need(events==ordered,'Cohort must be chronological before outcomes are visible')
    for event in events:
        need(aware_time(event['scheduled_start_utc'])>now,'Retrospective or already-started cohort cannot be frozen')
        need(event.get('source_card_id')!=config['source_card_id'],'Motivating historical card is excluded')
        need(set(event['targets'])==set(config['targets']),'Cohort target coverage mismatch')
        for name,spec in config['targets'].items():contract_check(event['targets'][name],spec['metric'],event['event_id'])
        if 'supplied_rank_match' in config['process_checks']:
            ranked=event.get('ranked_contracts',[])
            need(len(ranked)==4 and len({r['contract']['contract_id'] for r in ranked})==4,'Four exact supplied ranked contracts required')
            for row in ranked:
                contract_check(row['contract'],config['targets'][row['target']]['metric'],event['event_id'])
    plan=checked_json(config['power_plan_ref'],root)
    pilot=checked_json(plan['pilot_ref'],root)
    need(aware_time(pilot['last_outcome_utc'])<now,'Pilot must precede lock and future sample')
    need(bool(pilot.get('basis_refs')),'Pilot score provenance required')
    for ref in pilot['basis_refs']:checked_ref(ref,root)
    need(bool(plan.get('effect_size_rationale')),'Anticipated effect/tolerance justification required')
    computed=sample_plan(pilot['differences'],pilot['weeks'],acceptance['minimum_brier_improvement'],plan['anticipated_improvement'],power=plan['power'])
    for name in ('method','pilot_events','pilot_blocks','family_size','alpha_family','minimum_blocks','approximate_events','minimum_brier_improvement','anticipated_improvement','block_influence_sd'):
        need(plan[name]==computed[name],'Power plan does not match retained pilot: '+name)
    weeks={aware_time(e['scheduled_start_utc']).strftime('%G-W%V') for e in events}
    need(len(events)>=plan['approximate_events'] and len(weeks)>=plan['minimum_blocks'],'Future cohort below planned sample/block requirement')
    audit=checked_json(config['block_dependence_audit_ref'],root)
    need(bool(audit.get('reviewed_by')) and audit.get('block_definition')=='ISO_WEEK' and bool(audit.get('rationale')),'Declared week-block dependence review required')
    need(bool(audit.get('basis_refs')),'Dependence audit needs evidence')
    for ref in audit['basis_refs']:checked_ref(ref,root)
    adapters=adapter_check(checked_json(config['adapter_validation_ref'],root),config,root)
    result=dict(config=config,locked_utc=now.isoformat(),lock_id=uuid.uuid4().hex,
                source='REAL_TIME_LOCAL_FREEZE',status='FROZEN_DEVELOPMENT_PROTOCOL',
                cohort_sha256=config['cohort_ref']['sha256'],minimum_blocks=plan['minimum_blocks'],
                planned_events=len(events),required_numeric_events=plan['approximate_events'],adapter_readback=adapters,
                evaluation_code_refs=evaluation_refs(root),runtime=runtime(),performance_eligible=False)
    result['lock_sha256']=digest(result)
    write_new(output,result)
    return result

def read_lock(path,root=ROOT):
    value=load(path)
    need(value.get('lock_sha256')==digest({k:v for k,v in value.items() if k!='lock_sha256'}),'Lock hash changed')
    need(value['status']=='FROZEN_DEVELOPMENT_PROTOCOL' and value['performance_eligible'] is False,'Unsupported lock status')
    check_template(value['config'],root)
    need(value['runtime']==runtime(),'Evaluation runtime differs from locked environment')
    for ref in value['evaluation_code_refs']:checked_ref(ref,root)
    for name in ('candidate_model_ref','baseline_model_ref','cohort_ref','power_plan_ref','adapter_validation_ref','block_dependence_audit_ref'):
        checked_ref(value['config'][name],root)
    for name in ('candidate_model_ref','baseline_model_ref'):
        for ref in checked_json(value['config'][name],root)['dependency_refs']:checked_ref(ref,root)
    return value

def validate_features(features,config,root,cutoff):
    for name,kind in config['required_features'].items():
        obj=features[name];value=obj['value']
        need(aware_time(obj['available_utc'])<=cutoff,'Feature available after forecast cutoff: '+name)
        evidence=checked_json(obj['evidence_ref'],root)
        need(evidence['features'][name]==value,'Feature value differs from retained normalized evidence: '+name)
        need(aware_time(evidence['available_utc'])==aware_time(obj['available_utc']),'Feature availability differs from retained normalized evidence: '+name)
        need(bool(evidence.get('source_refs')),'Feature source provenance missing')
        for ref in evidence['source_refs']:checked_ref(ref,root)
        number=isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)
        valid={'text':isinstance(value,str) and bool(value),'boolean':isinstance(value,bool),
               'number':number,'integer':number and value>=0 and int(value)==value,
               'probability':number and 0<=value<=1,
               'list':isinstance(value,list) and bool(value),
               'probabilities':isinstance(value,list) and bool(value) and all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>=0 for x in value) and abs(sum(value)-1)<1e-9}.get(kind,False)
        need(valid,'Invalid typed feature: '+name)
        if name in {'goalie_confirmed','owner_phase_verified','conflict_resolved'}:need(value is True,'Required confirmation unresolved: '+name)
    values={name:obj['value'] for name,obj in features.items()}
    if config['horizon']=='LIVE':
        need(values['inning']>=1 and 0<=values['outs']<=2 and 0<=values['bases']<=7 and values['batting_half'] in {'TOP','BOTTOM'},'Invalid live inning/outs/base state')
    if 'wind_direction_degrees' in values:need(0<=values['wind_direction_degrees']<360 and values['wind_speed']>=0,'Invalid measured wind')
    if 'rest_hours' in values:need(values['rest_hours']>=0,'Negative elapsed rest')
    if 'special_teams_exposure' in values:need(values['special_teams_exposure']>=0,'Negative special-teams exposure')
    if 'scenario_weights' in values:
        need(len(values['scenario_weights'])==len(values['pace_scenarios']),'Scenario weights/pace scenarios mismatch')
        need(all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>=0 for x in values['pace_scenarios']),'Invalid pace scenario')
        need(all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>=0 for x in values['rotation_minutes']),'Invalid rotation minutes')
    if 'expected_minutes' in values:
        need(len(values['expected_minutes'])==len(values['available_rotation']) and all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>=0 for x in values['expected_minutes']),'Replacement minutes/rotation mismatch')
    if 'phase_provider_records' in values:
        phase=values['phase_provider_records']
        need(len(phase)>=2 and len({r['record_id'] for r in phase})==len(phase),'Two distinct correctly identified phase/provider records required')
        need(any(r.get('field_owner') is True for r in phase),'Authoritative phase owner record missing')
        for row in phase:checked_ref(row['body_ref'],root)
    return values

def joint_check(arm):
    joint=arm['joint']
    for values in [joint['home_support'],joint['away_support'],*joint['probabilities']]:
        need(all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in values),'Joint entries must be actual numeric values')
    home=np.asarray(joint['home_support'],dtype=float);away=np.asarray(joint['away_support'],dtype=float)
    p=np.asarray(joint['probabilities'],dtype=float)
    need(home.ndim==away.ndim==1 and p.shape==(len(home),len(away)) and p.size<=250000,'Joint score dimensions invalid')
    need(np.isfinite(home).all() and np.isfinite(away).all() and (home>=0).all() and (away>=0).all() and (np.diff(home)>0).all() and (np.diff(away)>0).all(),'Joint score support invalid')
    need(np.equal(home,np.floor(home)).all() and np.equal(away,np.floor(away)).all(),'Joint team-score support must be integer valued')
    need(np.isfinite(p).all() and (p>=0).all() and abs(p.sum()-1)<1e-9,'Joint probabilities invalid')
    for target,values in [('margin',home[:,None]-away[None,:]),('total',home[:,None]+away[None,:])]:
        derived={}
        for value,mass in zip(values.ravel(),p.ravel()):derived[float(value)]=derived.get(float(value),0)+float(mass)
        x,q=pmf(arm['targets'][target]);supplied=dict(zip(x,q))
        need(all(abs(derived.get(v,0)-supplied.get(v,0))<1e-9 for v in derived.keys()|supplied.keys()),'Joint '+target+' marginal mismatch')

def validate_forecast(payload,event,lock,root,recorded):
    config=lock['config'];cutoff=aware_time(payload['cutoff_utc']);start=aware_time(event['scheduled_start_utc'])
    need(aware_time(lock['locked_utc'])<=cutoff<=recorded,'Cutoff precedes lock or exceeds capture time')
    need(event_key(payload)==event_key(event),'Forecast event identity mismatch')
    need(payload['state']==config['horizon'],'Forecast horizon mismatch')
    if config['horizon']=='PREGAME':need(recorded<start,'Pregame capture after scheduled start')
    else:need(start<=cutoff,'Live forecast cutoff precedes scheduled start')
    feature_values=validate_features(payload['features'],config,root,cutoff)
    if config['horizon']=='LIVE':
        live=checked_json(payload['live_state_ref'],root)
        need(live['event_id']==event['event_id'] and live['state']=='LIVE','Owner live-state identity/phase mismatch')
        need(aware_time(live['observed_utc'])<=cutoff,'Live state observed after cutoff')
        need(bool(live.get('source_refs')),'Live-state owner body missing')
        for ref in live['source_refs']:checked_ref(ref,root)
        need(all(live[name]==feature_values[name] for name in ('inning','outs','bases','current_runs','batting_half')),'Live-state fields differ from frozen features')
    for feature in payload['features'].values():
        evidence=checked_json(feature['evidence_ref'],root)
        need(evidence['event_id']==event['event_id'],'Feature native event mismatch')
    for label in ('candidate','baseline'):
        arm=payload[label]
        model=checked_json(config[label+'_model_ref'],root)
        need(arm['model_version']==model['model_version'],'Forecast model version mismatch')
        need(aware_time(model['training_last_outcome_utc'])<cutoff,'Training outcomes cross forecast cutoff')
        need(set(arm['targets'])==set(config['targets']),'Missing or extra target distribution')
        for name,distribution in arm['targets'].items():
            x,p=pmf(distribution)
            need(np.equal(x,np.floor(x)).all(),'Sporting counts/margins require integer-valued support')
            if 'margin' not in name:need((x>=0).all(),'Negative count/total support')
            contract_probabilities(distribution,event['targets'][name])
        if 'joint_score_coherence' in config['process_checks']:joint_check(arm)
    if 'ot_probability_coherence' in config['process_checks']:
        regulation=payload['candidate']['targets']['regulation_margin'];x,p=pmf(regulation)
        full=payload['candidate']['targets']['full_game_margin'];fx,fp=pmf(full)
        derived=float(p[x>0].sum()+p[x==0].sum()*feature_values['conditional_ot_home_win'])
        need(abs(derived-float(fp[fx>0].sum()))<1e-9 and float(fp[fx==0].sum())==0,'Regulation/overtime probability mismatch')
    if 'supplied_rank_match' in config['process_checks']:
        expected_ids={r['contract']['contract_id'] for r in event['ranked_contracts']}
        ids=feature_values['ranked_contract_ids']
        need(len(ids)==4 and len(set(ids))==4 and set(ids)==expected_ids,'Supplied and ranked contracts differ')
    if 'original_model_card_separation' in config['process_checks']:
        need(set(payload['candidate']['model_targets'])==set(config['targets']),'Original model distributions absent')
        for name,distribution in payload['candidate']['model_targets'].items():
            x,p=pmf(distribution)
            need(np.equal(x,np.floor(x)).all() and ('margin' in name or (x>=0).all()),'Original model has invalid sporting support')
    if 'phase_provider_records' in feature_values:
        for name,contract in event['targets'].items():
            matching=[r for r in feature_values['phase_provider_records'] if r.get('event_id')==event['event_id'] and r.get('period')==contract['period'] and r.get('provider')==contract['provider'] and r.get('metric')==contract['metric']]
            need(bool(matching),'Phase/provider record does not match frozen target: '+name)
        for row in feature_values['phase_provider_records']:
            body=checked_json(row['body_ref'],root)
            need(all(body[key]==row[key] for key in ('event_id','period','provider','metric')),'Phase/provider metadata differs from retained normalized record')
    return feature_values

def read_forecasts(path,lock):
    path=Path(path);records=[];previous='0'*64;seen=set()
    if not path.exists():return records
    for line in path.read_text(encoding='utf-8').splitlines():
        row=json.loads(line)
        need(row['previous_sha256']==previous and row['lock_sha256']==lock['lock_sha256'],'Forecast journal chain or protocol mismatch')
        need(row['record_sha256']==digest({k:v for k,v in row.items() if k!='record_sha256'}),'Forecast journal changed')
        need(aware_time(row['recorded_utc'])>=aware_time(records[-1]['recorded_utc'] if records else lock['locked_utc']),'Forecast capture clock moves backwards')
        key=event_key(row['payload']);need(key not in seen,'Duplicate captured event')
        seen.add(key);previous=row['record_sha256'];records.append(row)
    return records

def capture(lock_path,payload,output,*,root=ROOT,now=None):
    now=now or datetime.now(timezone.utc);lock=read_lock(lock_path,root)
    events=checked_json(lock['config']['cohort_ref'],root)['events']
    matches=[e for e in events if event_key(e)==event_key(payload)]
    need(len(matches)==1,'Forecast outside frozen cohort');event=matches[0]
    if payload.get('disposition')=='NO_FORECAST':
        need(bool(payload.get('reason')) and now>=aware_time(lock['locked_utc']),'Reasoned abstention after protocol lock required')
        if lock['config']['horizon']=='PREGAME':need(now<aware_time(event['scheduled_start_utc']),'Pregame abstention captured late')
    else:
        need(payload.get('disposition')=='FORECAST','Explicit FORECAST or NO_FORECAST required')
        validate_forecast(payload,event,lock,root,now)
    with locked(Path(output)):
        records=read_forecasts(output,lock)
        need(now>=aware_time(records[-1]['recorded_utc'] if records else lock['locked_utc']),'Forecast capture clock moves backwards')
        need(all(event_key(r['payload'])!=event_key(payload) for r in records),'Event already captured; preserve original forecast')
        row=dict(payload=payload,recorded_utc=now.isoformat(),lock_sha256=lock['lock_sha256'],
                 previous_sha256=records[-1]['record_sha256'] if records else '0'*64)
        row['record_sha256']=digest(row)
        with Path(output).open('ab') as stream:stream.write(canonical_bytes(row)+b'\n')
    return row

def evaluate(lock_path,forecast_path,outcomes_path,*,root=ROOT,now=None):
    now=now or datetime.now(timezone.utc)
    lock=read_lock(lock_path,root);config=lock['config']
    cohort=checked_json(config['cohort_ref'],root)['events'];keys={event_key(e) for e in cohort}
    forecasts=read_forecasts(forecast_path,lock);by_forecast={event_key(r['payload']):r for r in forecasts}
    outcomes=load(outcomes_path)['records'];by_outcome={event_key(r):r for r in outcomes}
    need(len(by_outcome)==len(outcomes),'Duplicate outcome; use a separate explicitly versioned terminal artifact')
    need(set(by_forecast)<=keys and set(by_outcome)<=keys,'Out-of-cohort row cannot be added')
    scored=[];dispositions=[];errors=[];cal={name:{'candidate':[],'baseline':[],'outcomes':[]} for name in config['targets']}
    for event in cohort:
        key=event_key(event);record=by_forecast.get(key);terminal=by_outcome.get(key)
        if not record:dispositions.append(dict(identity=key,status='MISSING_FORECAST'));continue
        if not terminal or terminal['state']=='PENDING':dispositions.append(dict(identity=key,status='PENDING'));continue
        try:
            facts=checked_json(terminal['facts_ref'],root)
            need(event_key(facts)==key and facts['state']==terminal['state'],'Terminal native event or state mismatch')
            need(bool(facts.get('source_refs')),'Terminal source provenance absent')
            for ref in facts['source_refs']:checked_ref(ref,root)
            need(aware_time(facts['observed_utc'])>aware_time(record['recorded_utc']),'Terminal facts precede forecast capture')
            need(aware_time(facts['observed_utc'])<=now,'Terminal observation lies in the future')
            payload=record['payload']
            need(terminal['state'] in {'FINAL','VOID'},'Unknown terminal disposition')
            if payload['disposition']=='NO_FORECAST':dispositions.append(dict(identity=key,status='NO_FORECAST'));continue
            if terminal['state']=='VOID':
                need(bool(facts.get('reason')),'Void disposition needs evidence/reason')
                dispositions.append(dict(identity=key,status='VOID'));continue
            need(terminal['state']=='FINAL','Unknown terminal disposition')
            values=validate_forecast(payload,event,lock,root,aware_time(record['recorded_utc']))
            actual_start=aware_time(facts['actual_start_utc'])
            need(actual_start<=aware_time(facts['observed_utc']),'Actual start follows terminal observation')
            need(aware_time(record['recorded_utc'])<actual_start if config['horizon']=='PREGAME' else actual_start<=aware_time(payload['cutoff_utc']),'Actual-start/horizon conflict')
            if config['horizon']=='LIVE':
                need(aware_time(record['recorded_utc'])<aware_time(facts['actual_end_utc'])<=aware_time(facts['observed_utc']),'Live capture crosses actual game end')
            totals={label:dict(brier=0.,logloss=0.,zero_probability_observed=False) for label in ('candidate','baseline')}
            details={};event_cal={}
            for name,spec in config['targets'].items():
                fact=facts['targets'][name]
                need(fact['contract']==event['targets'][name],'Terminal contract/period/provider differs from frozen target')
                y=fact['value'];category=outcome_index(y,event['targets'][name]);details[name]={}
                need(int(y)==y,'Sporting outcome is not an integer count/margin')
                if 'margin' not in name:need(y>=0,'Negative sporting count/total outcome')
                if name=='remaining_runs':need(y==facts['full_game_runs']-values['current_runs'] and y>=0,'Remaining runs inconsistent with frozen live score')
                for label in ('candidate','baseline'):
                    probabilities=contract_probabilities(payload[label]['targets'][name],event['targets'][name])
                    scores=probability_scores(probabilities,category);distribution=distribution_scores(payload[label]['targets'][name],y)
                    details[name][label]=dict(**scores,probabilities=probabilities,outcome=category,**distribution)
                    for metric in ('brier','logloss'):
                        if scores[metric] is not None:totals[label][metric]+=spec['weight']*scores[metric]
                    totals[label]['zero_probability_observed']|=scores['zero_probability_observed']
                event_cal[name]=dict(candidate=details[name]['candidate']['probabilities'],
                                     baseline=details[name]['baseline']['probabilities'],outcomes=category)
            rank_diagnostics=None
            if 'supplied_rank_match' in config['process_checks']:
                contracts={r['contract']['contract_id']:r for r in event['ranked_contracts']};rank_rows=[]
                for cid in values['ranked_contract_ids']:
                    selected=contracts[cid];target=selected['target'];contract=selected['contract']
                    category=outcome_index(facts['targets'][target]['value'],contract)
                    probs=contract_probabilities(payload['candidate']['targets'][target],contract)
                    rank_rows.append(dict(contract_id=cid,outcome=category,**probability_scores(probs,category)))
                rank_diagnostics=dict(rows=rank_rows,top_rank_win=rank_rows[0]['outcome']==2,
                                      limitation='Descriptive; correlated ranked rows are not independent trials or additional primary-score weight.')
            for values in totals.values():
                if values['zero_probability_observed']:values['logloss']=None
            # Commit calibration rows only after every target/rank validates.
            for name,values in event_cal.items():
                for label,value in values.items():cal[name][label].append(value)
            scored.append(dict(identity=key,week=actual_start.strftime('%G-W%V'),candidate=totals['candidate'],
                               baseline=totals['baseline'],targets=details,rank_diagnostics=rank_diagnostics))
            dispositions.append(dict(identity=key,status='SCORED'))
        except (ValueError,KeyError,TypeError,OSError) as exc:
            errors.append(dict(identity=key,reason=str(exc)));dispositions.append(dict(identity=key,status='INVALID_EVIDENCE'))
    coverage=len(scored)/len(cohort);counts=dict(Counter(r['status'] for r in dispositions))
    blocked=[]
    if errors:blocked.append('IDENTITY_TIMING_OR_EVIDENCE_ERRORS')
    if any(counts.get(k,0) for k in ('MISSING_FORECAST','PENDING')):blocked.append('EARLIER_OR_OTHER_COHORT_MEMBER_PENDING')
    if coverage<config['acceptance']['minimum_numeric_coverage']:blocked.append('INSUFFICIENT_NUMERIC_COVERAGE')
    if len(scored)<lock['required_numeric_events']:blocked.append('BELOW_PLANNED_NUMERIC_SAMPLE')
    if len({r['week'] for r in scored})<lock['minimum_blocks']:blocked.append('INSUFFICIENT_BLOCKS')
    if any(r[a]['zero_probability_observed'] for r in scored for a in ('candidate','baseline')):blocked.append('INFINITE_LOGLOSS_REQUIRES_REVIEW')
    inference={};diagnostics={};guardrails={}
    if not blocked:
        args=dict(alpha=config['inference']['alpha_family']/config['inference']['family_size'],reps=config['inference']['bootstrap_reps'],seed=config['inference']['seed'],minimum_blocks=lock['minimum_blocks'])
        for metric in ('brier','logloss'):
            inference[metric]=paired_blocks([r['candidate'][metric]-r['baseline'][metric] for r in scored],[r['week'] for r in scored],**args)
        for target,values in cal.items():
            diagnostics[target]={label:reliability(values[label],values['outcomes']) for label in ('candidate','baseline')}
            reliability_result=paired_reliability(values['candidate'],values['baseline'],values['outcomes'],[r['week'] for r in scored],**args)
            diagnostics[target]['reliability_difference']=reliability_result
            guardrails[target+'_reliability']=reliability_result['ci'][1]<=config['acceptance']['max_reliability_deterioration']
            interval_deltas=[np.mean([r['targets'][target]['candidate']['intervals'][level]['interval_score']-r['targets'][target]['baseline']['intervals'][level]['interval_score'] for level in ('0.5','0.8','0.95')]) for r in scored]
            interval_result=paired_blocks(interval_deltas,[r['week'] for r in scored],**args)
            diagnostics[target]['interval_score_difference']=interval_result
            diagnostics[target]['mean_crps']={label:float(np.mean([r['targets'][target][label]['crps'] for r in scored])) for label in ('candidate','baseline')}
            diagnostics[target]['interval_coverage']={label:{level:float(np.mean([r['targets'][target][label]['intervals'][level]['covered'] for r in scored])) for level in ('0.5','0.8','0.95')} for label in ('candidate','baseline')}
            guardrails[target+'_interval_score']=interval_result['ci'][1]<=config['acceptance']['max_interval_score_deterioration'][target]
        guardrails['primary_improvement']=inference['brier']['ci'][1]<-config['acceptance']['minimum_brier_improvement']
        guardrails['logloss']=inference['logloss']['ci'][1]<=config['acceptance']['max_logloss_deterioration']
    decision='INCOMPLETE' if blocked else 'CANDIDATE_FOR_REVIEW' if all(guardrails.values()) else 'RETAIN_BASELINE'
    return dict(schema=VERSION,experiment_id=config['experiment_id'],status=decision,blocked=blocked,
                counts=counts,declared_events=len(cohort),scored_events=len(scored),numeric_coverage=coverage,
                errors=errors,dispositions=dispositions,event_scores=scored,inference=inference,
                diagnostics=diagnostics,guardrails=guardrails,lock_sha256=lock['lock_sha256'],
                forecasts_sha256=file_sha(Path(forecast_path)) if Path(forecast_path).exists() else None,outcomes_sha256=file_sha(Path(outcomes_path)),
                performance_eligible=False,model_promoted=False,
                limitation='Development measurement only. Receipt hashes/normalized fields do not prove official truth, independent collection, or certified prospective admission. Statistical review never automatically changes the model or an issued forecast.')

def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('status');sub.add_parser('verify')
    p=sub.add_parser('template');p.add_argument('experiment_id');p.add_argument('output')
    p=sub.add_parser('plan');p.add_argument('pilot');p.add_argument('minimum_improvement',type=float);p.add_argument('anticipated_improvement',type=float);p.add_argument('output');p.add_argument('--power',type=float,default=.8);p.add_argument('--rationale',required=True)
    p=sub.add_parser('freeze');p.add_argument('config');p.add_argument('output')
    p=sub.add_parser('capture');p.add_argument('lock');p.add_argument('payload');p.add_argument('journal')
    p=sub.add_parser('evaluate');p.add_argument('lock');p.add_argument('forecasts');p.add_argument('outcomes');p.add_argument('output')
    args=parser.parse_args()
    try:
        if args.command=='status':
            stores=ROOT/'research/experiments/runs';runs=[]
            for path in stores.rglob('*.json') if stores.exists() else []:
                value=load(path)
                if isinstance(value,dict) and value.get('schema')==VERSION and 'event_scores' in value:runs.append(dict(experiment_id=value['experiment_id'],path=path.relative_to(ROOT).as_posix(),status=value['status'],scored_events=value['scored_events']))
            completed={r['experiment_id'] for r in runs if r['status'] in {'CANDIDATE_FOR_REVIEW','RETAIN_BASELINE'}}
            result=dict(measures_implemented=15,experiments_run=len(completed),evaluation_artifacts=len(runs),runs=runs,protocols=[readiness(p) for p in catalog()],
                        note='Catalog readiness only; examine versioned run stores for actual results. No experiment is automatically promoted.')
        elif args.command=='verify':
            from .verify import run
            result=run()
        elif args.command=='template':
            need(Path(args.output).resolve().is_relative_to(ROOT/'research/experiments/runs'),'Draft output must stay in the experiment run store')
            result=next(p for p in catalog() if p['experiment_id']==args.experiment_id);write_new(args.output,result)
        elif args.command=='plan':
            need(Path(args.output).resolve().is_relative_to(ROOT/'research/experiments/runs'),'Power output must stay in the experiment run store')
            pilot=load(args.pilot)
            result=sample_plan(pilot['differences'],pilot['weeks'],args.minimum_improvement,args.anticipated_improvement,power=args.power)
            result.update(pilot_ref=dict(path=Path(args.pilot).resolve().relative_to(ROOT).as_posix(),sha256=file_sha(Path(args.pilot))))
            result['effect_size_rationale']=args.rationale
            write_new(args.output,result)
        elif args.command=='freeze':
            need(Path(args.output).resolve().is_relative_to(ROOT/'research/experiments/runs'),'Lock output must stay in the experiment run store')
            result=freeze(load(args.config),args.output)
        elif args.command=='capture':
            need(Path(args.journal).resolve().is_relative_to(ROOT/'research/experiments/runs'),'Journal must stay in the experiment run store')
            result=capture(args.lock,load(args.payload),args.journal)
        else:
            need(Path(args.output).resolve().is_relative_to(ROOT/'research/experiments/runs'),'Results must stay in the experiment run store')
            result=evaluate(args.lock,args.forecasts,args.outcomes);write_new(args.output,result)
        print(json.dumps(result,indent=2,allow_nan=False))
        return 0 if result.get('status')!='INCOMPLETE' else 2
    except (ValueError,KeyError,TypeError,OSError,StopIteration) as exc:
        print(json.dumps(dict(status='FAILED_CLOSED',error=str(exc))))
        return 1

if __name__=='__main__':raise SystemExit(main())

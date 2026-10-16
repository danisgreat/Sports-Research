"""Meaningful cycle integration/regression checks; every sporting observation here is synthetic EXAMPLE data."""
import builtins
from dataclasses import replace
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from ml import cycle as C, primary as p, research_ingest as ri, workflow as W
from ml.endpoint import regulation_pair
from ml.models.contextual import ContextModel
from ml.evaluation import prospective as PS
from ml.tests import learning_fixtures as lf
from ml.tests.test_primary import inputs


@pytest.fixture
def setup(tmp_path):
    store=tmp_path/'store'; frame=lf.season_frame(n_teams=6)
    frame=frame[frame.hs!=frame.as_].head(65)
    lf.ingest_frame(tmp_path,store,frame,'history')
    cap=lf.capture(tmp_path/'target-capture')
    issued=pd.Timestamp.now(tz='UTC'); start=issued+pd.Timedelta(days=1)
    request=dict(event_id='EXAMPLE-CYCLE-1',competition=lf.COMPETITION,endpoint=lf.ENDPOINT,home='T00',away='T01',venue='EXAMPLE-ARENA',
                 scheduled_start=start.isoformat(),issue_at=issued.isoformat(),outcome_exposure='NONE_RECORDED',candidate_recipe='EXAMPLE')
    target=dict(competition=lf.COMPETITION,endpoint=lf.ENDPOINT,native_event_id=request['event_id'],season='2026',scheduled_start=start.isoformat(),
                home='T00',away='T01',venue='EXAMPLE-ARENA',source_url='https://example.org/target',known_at=(issued-pd.Timedelta(minutes=1)).isoformat(),
                capture_path=cap[0],capture_sha256=cap[1],collected_by='LOCAL-EXAMPLE-G0001')
    export=lf.write_export(tmp_path/'target',target=[target])
    contracts=[dict(contract_key=side,family='total',side=side,line='200.5',endpoint=lf.ENDPOINT,definition='FROZEN_FRAMEWORK_CONVENTION',action='STANDARD_COMPLETED') for side in ('OVER','UNDER')]
    release=tmp_path/'release.csv'; C.freeze_release(release,lf.COMPETITION,lf.ENDPOINT,'EXAMPLE-v1')
    # Freeze genuinely occurred after the original issue declaration; advance the synthetic issue to now.
    request['issue_at']=pd.Timestamp.now(tz='UTC').isoformat()
    request_path=tmp_path/'request.csv'; request_path.write_bytes(p.csv_bytes([request]))
    contracts_path=tmp_path/'contracts.csv'; contracts_path.write_bytes(p.csv_bytes(contracts))
    return dict(tmp=tmp_path,store=store,export=export,request=request,request_path=request_path,contracts=contracts,contracts_path=contracts_path,release=release,frame=frame,cap=cap)


def execute(s, name='attempt', ledger=None):
    return W.execute(s['export'],s['store'],s['request_path'],s['contracts_path'],s['release'],s['tmp']/name,ledger=ledger)


def test_one_command_ingests_fits_prices_both_baselines_and_freezes(setup):
    s=setup; ledger=s['tmp']/'ledger.csv'; rec=execute(s,ledger=ledger)
    assert rec['status']=='EXECUTED',rec['error']
    assert W.verify(s['tmp']/'attempt')['status']=='EXECUTED'
    bundle=s['tmp']/'attempt'/'BUNDLE'; model=C.verify_bundle(bundle)
    assert int(model['training_rows'])==len(s['frame'])
    predictions=p.read_rows(bundle/'PREDICTIONS.csv')
    assert sum(float(r['p_card']) for r in predictions)==pytest.approx(1)
    assert all(sum(float(r[k]) for k in ('win','push','loss'))==pytest.approx(1) for r in predictions)
    assert len(PS.verify_ledger(ledger))==4
    assert {r['role'] for r in PS.verify_ledger(ledger)}=={'CHAMPION','CANDIDATE'}
    # A receipt, not numerical output alone, binds every contextual fit and input snapshot.
    assert (bundle/'PARAMETERS.csv').exists() and (bundle/'TRAINING_CONTEXT.csv').exists()
    from ml.execution import MANIFEST_FIELDS,verify_log
    row=dict.fromkeys(MANIFEST_FIELDS,'')
    row.update(card_id='LOCAL-EXAMPLE-G0001',event_id=rec['event_id'],competition=rec['competition'],endpoint=rec['endpoint'],execution_path='attempt',
               execution_sha256=p.digest((s['tmp']/'attempt'/'EXECUTION.csv').read_bytes()),feedback_status='PENDING_EVENT',reason='EXAMPLE future event')
    manifest=s['tmp']/'manifest.csv'; manifest.write_bytes(p.csv_bytes([row]))
    mini=s['tmp']/'mini.md'; mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-10 -->\n<!-- BEGIN CARD LOCAL-EXAMPLE-G0001 -->\n- **Analysis status:** MODEL_ASSISTED_CYCLE_V1\n'+
        f"- **ML execution identity:** {rec['event_id']} | {rec['competition']} | {rec['endpoint']}\n<!-- END CARD LOCAL-EXAMPLE-G0001 -->\n",encoding='utf-8')
    assert verify_log(manifest,mini)['executed']==1
    (bundle/'FEATURES.csv').write_text('corrupted\n')
    with pytest.raises(p.AdmissionError,match='hash mismatch'): C.verify_bundle(bundle)


@pytest.mark.parametrize('defect',['missing','unsupported','hash','no_history'])
def test_every_attempt_retains_verifiable_failure(setup,defect):
    s=setup
    if defect=='missing': s['request_path']=s['tmp']/'absent.csv'
    elif defect=='unsupported':
        req=dict(s['request'],endpoint='FIRST_HALF'); s['request_path'].write_bytes(p.csv_bytes([req]))
    elif defect=='hash':
        rows=p.read_rows(s['release']); rows[0]['code_sha256']='0'*64; s['release'].write_bytes(p.csv_bytes(rows))
    else: s['store']=s['tmp']/'empty-store'
    rec=execute(s)
    assert rec['status']=='FAILED' and rec['error_type'] and rec['error']
    assert W.verify(s['tmp']/'attempt')['status']=='FAILED'
    with pytest.raises(FileExistsError): execute(s)


def test_missing_runtime_dependency_is_captured_without_numpy_or_pandas(setup,monkeypatch):
    original=builtins.__import__
    def broken(name,*args,**kwargs):
        if name=='ml' and 'cycle' in kwargs.get('fromlist',args[2] if len(args)>2 else ()):
            raise ModuleNotFoundError('EXAMPLE missing numerical runtime')
        return original(name,*args,**kwargs)
    monkeypatch.setattr(builtins,'__import__',broken)
    rec=execute(setup)
    assert rec['status']=='FAILED' and rec['stage']=='RUNTIME_IMPORT'
    assert W.verify(setup['tmp']/'attempt')['status']=='FAILED'


def test_final_endpoint_never_adds_overtime_twice_and_retains_unknown_regulation(setup):
    s=setup; row=lf.game_row(s['frame'].iloc[0],s['cap'],reg_hs='NOT_OBSERVED',reg_as='NOT_OBSERVED',decision='Overtime')
    export=lf.write_export(s['tmp']/'unknown-reg',games=[dict(row,native_event_id='EXAMPLE-EXTRA')])
    assert ri.ingest(export,s['store'])['new_results']==1
    bad=dict(row,reg_hs=row['hs'],reg_as=row['as_'])
    with pytest.raises(ValueError,match='observed tie'): regulation_pair(bad)
    assert regulation_pair(row) is None
    pair=regulation_pair(dict(hs='7',as_='4',reg_hs='3',reg_as='3',decision='EXTRAS'))
    assert pair==(3,3)


def test_native_id_reuse_on_different_day_is_quarantined(setup):
    s=setup; g=s['frame'].iloc[0]
    row=lf.game_row(g,s['cap'],event_at=(pd.Timestamp(g.event_at)+pd.Timedelta(days=10)).isoformat(),
                    final_at=(pd.Timestamp(g.event_at)+pd.Timedelta(days=10,hours=2)).isoformat(),
                    known_at=(pd.Timestamp(g.event_at)+pd.Timedelta(days=10,hours=3)).isoformat(),
                    retrieved_at=(pd.Timestamp(g.event_at)+pd.Timedelta(days=10,hours=4)).isoformat())
    rec=ri.ingest(lf.write_export(s['tmp']/'collision',games=[row]),s['store'])
    assert rec['quarantined']==1
    assert 'IDENTITY_COLLISION' in ri.load_store(s['store']).quarantine.reason.iloc[-1]


def test_context_is_fitted_and_changes_prediction_without_manual_player_adjustment():
    rng=np.random.default_rng(2); n=120
    rest=rng.uniform(1,5,n)
    rows=pd.DataFrame(dict(home=['A','B']*(n//2),away=['B','A']*(n//2),venue=['V']*n,
                           hs=np.round(85+6*rest+rng.normal(0,3,n)),as_=np.round(75+rng.normal(0,4,n)),home_rest_days=rest,
                           home_player_abc=(rest>3).astype(float),neutral_venue=(rest>2).astype(float),
                           event_at=pd.date_range('2025-01-01',periods=n,tz='UTC'),label_available_at=pd.date_range('2025-01-02',periods=n,tz='UTC')))
    model=ContextModel('Basketball/EXAMPLE',lf.ENDPOINT,180,10).fit(rows,'2026-10-16T00:00Z')
    target=pd.DataFrame([dict(home='A',away='B',venue='V',home_rest_days=1,home_player_abc=0,neutral_venue=0)])
    g1=model.grid(target); target.home_rest_days=5; g2=model.grid(target)
    assert g2.means()[0]>g1.means()[0]+10
    assert 'home_player_abc' in model.context and 'neutral_venue' in model.context
    assert g1.winner()[1]==pytest.approx(0)


def test_baseball_final_model_can_learn_home_wins_without_higher_home_run_mean():
    rng=np.random.default_rng(9); n=120
    # 60% home wins by 1, 40% home losses by 4: a final-score censoring example.
    wins=np.tile([True,True,True,False,False],24); hs=np.where(wins,4,2); away=np.where(wins,3,6)
    rows=pd.DataFrame(dict(home=['H']*n,away=['A']*n,venue=['P']*n,hs=hs,as_=away,event_at=pd.date_range('2025-01-01',periods=n,tz='UTC'),label_available_at=pd.date_range('2025-01-02',periods=n,tz='UTC')))
    model=ContextModel('Baseball/MLB','FULL_GAME_INCL_EXTRAS',90,32).fit(rows,'2026-10-16T00:00Z')
    grid=model.grid(pd.DataFrame([dict(home='H',away='A',venue='P')]))
    assert grid.winner()[0]>.55 and grid.winner()[1]==pytest.approx(0)
    assert rows.hs.mean()<rows.as_.mean()  # winner probability is fitted, not inferred from this mean ordering


def test_new_feedback_moves_weights_and_old_feedback_has_bounded_influence():
    config=dict(feedback_half_life_events='20',weight_floor='.05',eta_cap='.5')
    rows=[dict(event_id=f'E{i}',available_at=f'2025-01-{i+1:02d}T00:00Z',**{'loss_'+a:float(j!=0) for j,a in enumerate(C.ARMS)}) for i in range(20)]
    before,_,_,_=C.adaptive_weights(rows,config)
    rows.append(dict(event_id='LATEST',available_at='2026-10-16T00:00Z',**{'loss_'+a:float(j==0) for j,a in enumerate(C.ARMS)}))
    after,_,eta,mass=C.adaptive_weights(rows,config)
    assert after[0]<before[0] and min(after)>=.05 and 0<eta<=.5 and mass<21
    with pytest.raises(p.AdmissionError,match='duplicate'): C.adaptive_weights(rows+rows[-1:],config)


def test_settlement_store_feedback_and_next_prediction_are_connected(setup,monkeypatch):
    s=setup; assert execute(s)['status']=='EXECUTED'
    bundle=s['tmp']/'attempt'/'BUNDLE'; rec=C.verify_bundle(bundle)
    start=p.clock(s['request']['scheduled_start']); final=start+pd.Timedelta(hours=2); known=final+pd.Timedelta(hours=1)
    row=lf.game_row(s['frame'].iloc[0],s['cap'],native_event_id=s['request']['event_id'],event_at=start.isoformat(),hs='101',as_='91',reg_hs='101',reg_as='91',decision='Regulation',
                    final_at=final.isoformat(),known_at=known.isoformat(),published_at=known.isoformat(),retrieved_at=known.isoformat())
    export=lf.write_export(s['tmp']/'result',games=[row]); settlement=C.settle(bundle,export,s['store'],s['tmp']/'feedback'/'one')
    assert C.verify_settlement(s['tmp']/'feedback'/'one')['event_id']==s['request']['event_id']
    next_req=dict(s['request'],event_id='EXAMPLE-CYCLE-2',scheduled_start=(known+pd.Timedelta(days=2)).isoformat(),issue_at=(known+pd.Timedelta(days=1)).isoformat())
    config=C.release(s['release'])
    assert len(C.feedback_rows(s['tmp']/'feedback',next_req,config,known-pd.Timedelta(seconds=1)))==0
    assert len(C.feedback_rows(s['tmp']/'feedback',next_req,config,known))==1
    assert len(C.dataset(ri.load_store(s['store']),next_req))==len(s['frame'])+1
    outcomes=p.read_rows(s['tmp']/'feedback'/'one'/'OUTCOMES.csv')
    assert len(outcomes)==2 and set(outcomes[0])==set(PS.OUTCOME_FIELDS)


def test_future_news_cannot_change_old_feature_snapshot(setup):
    s=setup; st=ri.load_store(s['store']); target=ri.ingest(s['export'],s['store']); st=ri.load_store(s['store']); ev=st.events[st.events.native_event_id==s['request']['event_id']].iloc[0]
    at=s['request']['issue_at']; first=C.event_features(st,ev,at)
    future=dict(competition=lf.COMPETITION,native_event_id=ev.native_event_id,team='T00',player='EXAMPLE STAR',role='STARTER',status='CONFIRMED_OUT',confirmation='OFFICIAL_CONFIRMED',
                published_at=s['request']['scheduled_start'],retrieved_at=s['request']['scheduled_start'],known_at=s['request']['scheduled_start'],source_url='https://example.org/future',capture_path=s['cap'][0],capture_sha256=s['cap'][1],review_status='RESEARCH_INPUT_REVIEWED',collected_by='EXAMPLE')
    ri.ingest(lf.write_export(s['tmp']/'future',avail=[future]),s['store'])
    second=C.event_features(ri.load_store(s['store']),ev,at)
    assert all((np.isnan(v) and np.isnan(second[k])) or v==second[k] for k,v in first.items())


def test_existing_primary_adapter_also_has_attempt_receipt_and_real_baseline(inputs,monkeypatch):
    req,lg,history,contracts,tmp,cap=inputs
    monkeypatch.setattr(p,'get_league',lambda _:lg)
    target=dict(competition=req['competition'],endpoint=req['endpoint'],native_event_id=req['event_id'],season='2023',scheduled_start=req['scheduled_start'],home=req['home'],away=req['away'],venue='',source_url='https://example.org/fixture',known_at=req['issue_at'],capture_path=str(cap),capture_sha256=p.digest(cap.read_bytes()),collected_by='EXAMPLE')
    export=lf.write_export(tmp/'export',target=[target])
    paths=[]
    for name,rows in (('request',[req]),('history',history),('contracts',contracts)):
        path=tmp/(name+'.csv'); path.write_bytes(p.csv_bytes(rows)); paths.append(path)
    rec=W.execute(export,tmp/'store',paths[0],paths[2],None,tmp/'attempt',adapter='primary',history=paths[1])
    assert rec['status']=='EXECUTED',rec['error']
    rows=p.read_rows(tmp/'attempt'/'SHADOW_ROWS.csv')
    assert {r['role'] for r in rows}=={'CHAMPION','CANDIDATE'}
    assert {r['evidence_status'] for r in rows}=={'POST_START'}


def test_tennis_adapter_retains_actual_tennis_bundle_and_comparator(tmp_path):
    from ml.tests.test_tennis_primary import fixture
    req,history,contracts,cap=fixture(tmp_path)
    target=dict(competition=req['competition'],endpoint='COMPLETED_BEST_OF_3',native_event_id=req['event_id'],season='2024',scheduled_start=req['scheduled_start'],home=req['player1'],away=req['player2'],venue='',source_url='https://example.org/fixture',known_at=req['issue_at'],capture_path=str(cap),capture_sha256=p.digest(cap.read_bytes()),collected_by='EXAMPLE')
    export=lf.write_export(tmp_path/'export',target=[target])
    for name,rows in (('request',[req]),('history',history),('contracts',contracts)):
        (tmp_path/(name+'.csv')).write_bytes(p.csv_bytes(rows))
    rec=W.execute(export,tmp_path/'store',tmp_path/'request.csv',tmp_path/'contracts.csv',None,tmp_path/'attempt',adapter='tennis',history=tmp_path/'history.csv')
    assert rec['status']=='EXECUTED',rec['error']
    assert W.verify(tmp_path/'attempt')['endpoint']=='COMPLETED_BEST_OF_3'
    assert len(p.read_rows(tmp_path/'attempt'/'SHADOW_ROWS.csv'))==6


def test_empty_prospective_evaluation_does_not_invent_results(setup):
    s=setup
    rec=C.evaluate(s['release'],s['tmp']/'absent-ledger.csv',s['tmp']/'feedback',s['tmp']/'evaluation')
    assert rec['disposition']=='INSUFFICIENT_EVIDENCE' and rec['paired_events']==0


def test_exact_contract_and_stable_version_checks(tmp_path):
    from ml.tests.test_learning_governance import _rows
    start=pd.Timestamp('2026-11-01T00:00Z')
    rows=[_rows('BASE','v1','CHAMPION','E1',start,.5,1),_rows('NEW','v1','CANDIDATE','E1',start,.6,1)]
    ledger=tmp_path/'ledger.csv'; PS.freeze(ledger,rows,now=start-pd.Timedelta(hours=1))
    outcomes=pd.DataFrame([dict(event_id='E1',contract_key='WIN-H',result='WIN',final_at=(start+pd.Timedelta(hours=2)).isoformat(),available_at=(start+pd.Timedelta(hours=3)).isoformat(),evidence_sha256='a'*64)])
    frozen=PS.verify_ledger(ledger)
    changed=[dict(r,endpoint='FIRST_HALF') if r['model_id']=='NEW' else r for r in frozen]
    with pytest.raises(p.AdmissionError,match='identical-contract'): PS.evaluate(changed,outcomes,'BASE:v1','NEW:v1',delta=.01)
    result=PS.evaluate(frozen,outcomes,'BASE:v1','NEW:v1',delta=.01)
    assert 'log_loss_interval' in result and result['models']['BASE:v1']['rows']==1

"""Receipt-bound research -> learning -> forecast -> settlement cycle (CYCLE-v1).

New experiments are explicitly versioned. Legacy V3 bundles and issued cards are never rewritten.
Use the stdlib entry point ``python -m ml.workflow`` so dependency/import failures also have receipts.
"""
from __future__ import annotations

import argparse
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from ml import features as F, primary as p, research_ingest as ri
from ml.core.distributions import ScoreGrid
from ml.models.contextual import ContextModel, RECIPES, SPEC, supported
from ml.evaluation import prospective as ps

POLICY = "RESEARCH_FORECAST_CYCLE_V1"
ARMS = p.ARMS
FILES = ("REQUEST", "CONTRACTS", "HISTORY", "FEATURES", "PREDICTIONS", "GRIDS", "PARAMETERS",
         "ADAPTATION", "RELEASE", "TRAINING_CONTEXT", "CONTEXT_STATUS", "EXCLUSIONS")
RELEASE_FIELDS = ("policy", "version", "competition", "endpoint", "frozen_at", "code_sha256", "model_spec",
                  "fast_days", "slow_days", "ridge", "feedback_half_life_events", "weight_floor", "eta_cap",
                  "minimum_weeks", "minimum_events", "minimum_brier_effect", "status", "parameter_evidence")


def now():
    return datetime.now(timezone.utc).isoformat()


def code_hash():
    from ml.run import code_digest
    return code_digest()  # stable across LF/CRLF checkouts; the frozen policy is still exact source


def write_rows(path, rows, fields=()):
    data = p.csv_bytes(rows) if rows else (",".join(fields)+"\n").encode()
    Path(path).write_bytes(data)


def freeze_release(path, competition, endpoint, version):
    if not supported(competition, endpoint):
        raise p.AdmissionError("no contextual adapter for exact scope; retain a failure receipt or use the separate reviewed cricket/tennis adapter")
    if not version.strip():
        raise p.AdmissionError("nonempty stable release version required")
    fast, slow, ridge = RECIPES[competition.split("/",1)[0]]
    rec = dict(policy=POLICY, version=version, competition=competition, endpoint=endpoint, frozen_at=now(),
               code_sha256=code_hash(), model_spec=SPEC, fast_days=fast, slow_days=slow, ridge=ridge,
               feedback_half_life_events=20., weight_floor=.05, eta_cap=.5,
               minimum_weeks=8, minimum_events=50, minimum_brier_effect=.01,
               status="EXPERIMENTAL_NOT_QUALIFIED", parameter_evidence="PREDECLARED_FAMILY_DEFAULTS_NOT_TUNED")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("xb") as handle:
        handle.write(p.csv_bytes([rec]))
    return rec


def release(path, req=None, *, check_code=True):
    rows = p.read_rows(Path(path))
    if len(rows)!=1 or set(rows[0])!=set(RELEASE_FIELDS):
        raise p.AdmissionError("exact frozen release schema required")
    rec=rows[0]
    if rec["policy"]!=POLICY or rec["model_spec"]!=SPEC or rec["status"]!="EXPERIMENTAL_NOT_QUALIFIED":
        raise p.AdmissionError("unknown/unadmitted model release")
    if not supported(rec["competition"], rec["endpoint"]):
        raise p.AdmissionError("unsupported release scope")
    if check_code and rec["code_sha256"]!=code_hash():
        raise p.AdmissionError("frozen source differs: restore its checkout or create a new version; never restamp")
    for key in ("fast_days", "slow_days", "ridge", "feedback_half_life_events", "eta_cap", "minimum_brier_effect"):
        if not math.isfinite(float(rec[key])) or float(rec[key])<=0:
            raise p.AdmissionError("invalid release parameter "+key)
    if not 0<=float(rec["weight_floor"])<1/len(ARMS) or float(rec["eta_cap"])>1:
        raise p.AdmissionError("invalid expert floor/learning-rate cap")
    if int(rec["minimum_weeks"])<8 or int(rec["minimum_events"])<50:
        raise p.AdmissionError("release weakens prospective minimums")
    if req is not None:
        if any(req[k]!=rec[k] for k in ("competition", "endpoint")):
            raise p.AdmissionError("request differs from frozen competition/endpoint")
        horizon,_=p.information_horizon(req)
        if p.clock(rec["frozen_at"])>horizon:
            raise p.AdmissionError("release frozen after information horizon; no retrospective prospective claim")
    return rec


def event_features(store, ev, at):
    values=F.build(store, ev.competition, ev.endpoint, ev.home, ev.away, at,
                   target_event_uid=ev.event_uid, season=str(ev.season))
    stats=ri.effective_stats(store,at)
    neutral=stats[(stats.event_uid==ev.event_uid)&(stats.stat=='NEUTRAL_VENUE')]
    values['neutral_venue']=float(neutral.iloc[-1].value) if len(neutral) else math.nan
    # Player identities/roles are learned only when previously observed, never assigned hand-made impacts.
    for r in ri.availability_as_of(store, ev.event_uid, at).itertuples():
        if r.confirmation!="OFFICIAL_CONFIRMED":
            continue
        side="home" if r.team==ev.home else "away"
        key=side+"_player_"+p.digest((r.player+"|"+r.role).encode())[:16]
        values[key]=1. if r.status=="CONFIRMED_ACTIVE" else 0. if r.status=="CONFIRMED_OUT" else math.nan
    return {k:v for k,v in values.items() if k not in ("as_of", "spec_version") and not k.endswith(("__n","__missing"))}


def dataset(store, req, *, with_exclusions=False):
    horizon,_=p.information_horizon(req)
    labels=ri.effective_results(store, horizon)
    events=store.events.set_index("event_uid")
    rows=[]; excluded=[]
    quarantined=set(store.quarantine.native_event_id[store.quarantine.competition==req['competition']])
    earliest_known=min((p.clock(t) for t in store.source_observations.known_at),default=horizon)
    empty_store=ri.Store(store.root,0,{name:frame.iloc[0:0].copy() for name,frame in store.tables.items()})
    missing_context=None
    checked_captures=set()
    for lab in labels.itertuples():
        ev=events.loc[lab.event_uid].copy()
        ev['event_uid']=lab.event_uid
        if ev.competition!=req["competition"] or ev.endpoint!=req["endpoint"] or lab.status!="FINAL":
            continue
        if ev.native_event_id in quarantined:
            excluded.append(dict(event_id=ev.native_event_id,reason='OPEN_QUARANTINE'))
            continue
        if req["event_id"] in (ev.native_event_id, lab.event_uid):
            continue
        if p.clock(ev.event_at)>=horizon.normalize() or p.clock(lab.final_at)>horizon:
            continue
        # A result's reviewed capture is checked again before fitting.
        obs=store.source_observations
        obs=obs[(obs.event_uid==lab.event_uid)&(obs.kind=="RESULT")&(obs.link==str(lab.revision))]
        obs=obs[obs.known_at.map(p.clock)<=horizon]
        if obs.empty:
            raise p.AdmissionError("training label lacks visible source observation")
        for src in obs.itertuples():
            capture=(src.capture_path,src.capture_sha256)
            if capture not in checked_captures:
                p.receipt_file(*capture); checked_captures.add(capture)
        support=obs.iloc[0]
        row=dict(event_uid=lab.event_uid,event_id=ev.native_event_id,competition=ev.competition,endpoint=ev.endpoint,
                 season=ev.season,event_at=ev.event_at,home=ev.home,away=ev.away,venue=ev.venue,
                 hs=int(lab.hs),as_=int(lab.as_),reg_hs=lab.reg_hs,reg_as=lab.reg_as,decision=lab.decision,
                 label_available_at=lab.valid_from.isoformat(),label_revision=lab.revision,
                 source_url=support.source_url,evidence_path=support.capture_path,evidence_sha256=support.capture_sha256,
                 source_observation_ids=';'.join(sorted(obs.observation_id)))
        # Features use only information observable at that historical event, not its later result.
        if p.clock(ev.event_at)<earliest_known:
            # No observation of any kind existed yet. Reusing this all-missing snapshot
            # is identical to repeatedly querying the full store at each old event.
            if missing_context is None: missing_context=event_features(empty_store,ev,ev.event_at)
            row.update(missing_context)
        else:
            row.update(event_features(store,ev,ev.event_at))
        rows.append(row)
    frame=pd.DataFrame(rows).sort_values(["event_at","event_id"]).reset_index(drop=True) if rows else pd.DataFrame()
    return (frame,excluded) if with_exclusions else frame


def loss(grid, hs, away, scale):
    # Proper distribution scores cover every line; three-way Brier retains soccer draws.
    probs=np.array(grid.winner())
    y=np.array([hs>away,hs==away,hs<away],float)
    return float(.5*np.sum((probs-y)**2)+.25*grid.crps_margin(hs-away)/scale+.25*grid.crps_total(hs+away)/scale)


def adaptive_weights(rows, config):
    """Delayed full information; bounded memory by feedback-event order, no historical warm-loss domination."""
    rows=sorted(rows,key=lambda r:(p.clock(r["available_at"]),r["event_id"]))
    if len({r['event_id'] for r in rows})!=len(rows):
        raise p.AdmissionError("duplicate effective feedback event")
    discount=.5**(1/float(config["feedback_half_life_events"]))
    cumulative=np.zeros(len(ARMS)); variance=0.; mass=0.
    for row in rows:
        values=np.array([float(row['loss_'+a]) for a in ARMS])
        if not np.isfinite(values).all() or np.any(values<0):
            raise p.AdmissionError("invalid expert loss")
        # Scores need not be bounded by one; cap eta by empirical squared range.
        cumulative=discount*cumulative+values
        variance=discount*variance+float(np.ptp(values)**2)
        mass=discount*mass+1
    eta=min(float(config['eta_cap']),math.sqrt(2*math.log(len(ARMS))/(1+variance)))
    z=-eta*(cumulative-cumulative.min()); weights=np.exp(z); weights/=weights.sum()
    floor=float(config['weight_floor']); weights=floor+(1-len(ARMS)*floor)*weights
    return weights,cumulative,eta,mass


def feedback_rows(root, req, config, horizon):
    rows=[]
    if root is None or not Path(root).exists():
        return rows
    for path in sorted(Path(root).glob('*/SETTLEMENT.csv')):
        row=verify_settlement(path.parent)
        if row['event_id']==req['event_id']:
            raise p.AdmissionError("target settlement cannot enter its own forecast")
        if row['competition']==req['competition'] and row['endpoint']==req['endpoint'] and row['release_sha256']==p.digest(p.csv_bytes([config])) and p.clock(row['available_at'])<=horizon:
            rows.append(row)
    effective={}
    for row in rows:
        old=effective.get(row['event_id'])
        if old and int(old['result_revision'])==int(row['result_revision']) and any(old[k]!=row[k] for k in ('home_score','away_score','evidence_sha256')):
            raise p.AdmissionError('conflicting feedback for the same result revision')
        if old is None or int(row['result_revision'])>int(old['result_revision']): effective[row['event_id']]=row
    return list(effective.values())


def forecast(store_path, request, contracts, release_path, output, feedback_root=None):
    if request.get('outcome_exposure')!='NONE_RECORDED':
        raise p.AdmissionError("outcome exposure blocks forecast; retain research")
    allowed={'event_id','competition','endpoint','home','away','venue','scheduled_start','issue_at','actual_start','outcome_exposure','candidate_recipe'}
    if set(request)-allowed or request['home']==request['away']:
        raise p.AdmissionError("invalid request or unregistered/market input columns")
    issued=p.clock(request['issue_at']); clock_now=p.clock(now())
    if issued>clock_now:
        raise p.AdmissionError("declared issue is in the future")
    config=release(release_path,request)
    horizon,_=p.information_horizon(request)
    store=ri.load_store(store_path); digest_before=ri.store_digest(store)
    train,excluded=dataset(store,request,with_exclusions=True)
    if len(train)<30:
        raise p.AdmissionError(f"only {len(train)} verified exact-endpoint events; need 30")
    # Resolve native ID against the export; never select an event by a canonical P-ID.
    uid=ri.resolve_event(store.events,store.event_aliases,request['competition'],request['event_id'],request['scheduled_start'],request['home'],request['away'])
    if uid is None:
        raise p.AdmissionError("target absent from research export/store")
    ev=store.events[store.events.event_uid==uid].iloc[0]
    if (ev.home,ev.away,ev.endpoint)!=(request['home'],request['away'],request['endpoint']):
        raise p.AdmissionError("target identity/orientation/endpoint differs from research export")
    current=dict(home=request['home'],away=request['away'],venue=request.get('venue',''))
    current.update(event_features(store,ev,horizon)); target=pd.DataFrame([current])
    models={a:ContextModel(config['competition'],config['endpoint'],float(days),float(config['ridge']),baseline=a==ARMS[2]).fit(train,horizon)
            for a,days in zip(ARMS,(config['fast_days'],config['slow_days'],config['slow_days']))}
    grids={a:m.grid(target) for a,m in models.items()}
    fb=feedback_rows(feedback_root,request,config,horizon)
    weights,cumulative,eta,mass=adaptive_weights(fb,config)
    grid=p.mix_grids([grids[a] for a in ARMS],weights)
    if not contracts or len({r['contract_key'] for r in contracts})!=len(contracts):
        raise p.AdmissionError("nonempty unique contract slate required")
    predictions=[]; semantics=set()
    for row in contracts:
        if set(row)!={'contract_key','family','side','line','endpoint','definition','action'}:
            raise p.AdmissionError("exact contract schema required; no market columns")
        semantic=tuple(row[k] for k in ('family','side','line','endpoint','definition','action'))
        if semantic in semantics:
            raise p.AdmissionError("duplicate semantic contract")
        semantics.add(semantic)
        w,pu,l=p.price(grid,row,request['endpoint']); bw,bp,bl=p.price(grids[ARMS[2]],row,request['endpoint'])
        predictions.append(dict(**row,win=w,push=pu,loss=l,p_card=w/(w+l) if w+l else 'NOT_COMPUTED',
                                baseline_win=bw,baseline_push=bp,baseline_loss=bl,baseline_p=bw/(bw+bl) if bw+bl else 'NOT_COMPUTED',rank=''))
    # Pricing is exhaustive. These are model diagnostic ranks; card selection gates remain a separate check.
    eligible=sorted([r for r in predictions if isinstance(r['p_card'],float) and r['p_card']<=.90],key=lambda r:(-r['p_card'],r['contract_key']))
    for i,r in enumerate(eligible[:4],1): r['rank']=str(i)
    scale=max(1.,float(np.std(train.hs.astype(float)-train.as_.astype(float))))
    artifacts=dict(REQUEST=[request],CONTRACTS=contracts,HISTORY=train.drop(columns=[c for c in train if c not in ('event_uid','event_id','competition','endpoint','season','event_at','home','away','venue','hs','as_','reg_hs','reg_as','decision','label_available_at','label_revision','source_url','evidence_path','evidence_sha256','source_observation_ids')]).to_dict('records'),
                   TRAINING_CONTEXT=train.fillna('').to_dict('records'),FEATURES=[{k:'' if isinstance(v,float) and math.isnan(v) else v for k,v in current.items()}],
                   PREDICTIONS=predictions,GRIDS=[dict(arm=a,home=h+g.h0,away=away+g.a0,mass=float(g.p[h,away])) for a,g in grids.items() for h,away in np.ndindex(g.p.shape) if g.p[h,away]>0],
                   PARAMETERS=[r for a,m in models.items() for r in m.parameters(a)],ADAPTATION=fb,RELEASE=[config],EXCLUSIONS=excluded,
                   CONTEXT_STATUS=[dict(arm=a,feature=c,status='FITTED',training_observations=int(pd.to_numeric(train[c],errors='coerce').notna().sum())) for a,m in models.items() for c in m.context] or [dict(arm='ALL',feature='context',status='NO_HISTORICAL_CONTEXT_VARIATION',training_observations=0)])
    output=Path(output); output.mkdir(parents=True,exist_ok=False)
    for name,rows in artifacts.items(): write_rows(output/(name+'.csv'),rows,('event_id','available_at'))
    rec=dict(policy=POLICY,event_id=request['event_id'],competition=request['competition'],endpoint=request['endpoint'],
             version=config['version'],generated_at=now(),issue_at=request['issue_at'],scheduled_start=request['scheduled_start'],
             information_horizon=horizon.isoformat(),training_rows=len(train),store_view=store.view_seq,store_digest=digest_before,
             code_sha256=code_hash(),
             weights=';'.join(f'{a}:{w:.17g}' for a,w in zip(ARMS,weights)),eta=eta,effective_feedback_events=mass,
             feedback_events=len(fb),loss_scale=scale,qualification='EXPERIMENTAL_NOT_QUALIFIED',
             endpoint_model='DIRECT_FINAL_NO_SECOND_EXTRA_TIME_BRANCH',baseline='COMPETITION_FINAL_LEAGUE_V1',
             **{n.lower()+'_sha256':p.digest((output/(n+'.csv')).read_bytes()) for n in FILES})
    if ri.store_digest(ri.load_store(store_path,store.view_seq))!=digest_before or rec['code_sha256']!=config['code_sha256']:
        raise p.AdmissionError("source/store changed during inference")
    write_rows(output/'RECEIPT.csv',[rec]); verify_bundle(output)
    return rec


def load_grids(folder):
    return p._load_grids(Path(folder))


def verify_bundle(folder):
    folder=Path(folder); rec=p.read_rows(folder/'RECEIPT.csv')[0]
    if rec['policy']!=POLICY or rec['qualification']!='EXPERIMENTAL_NOT_QUALIFIED':
        raise p.AdmissionError("unknown cycle receipt")
    for name in FILES: p.receipt_file(folder/(name+'.csv'),rec[name.lower()+'_sha256'])
    req=p.read_rows(folder/'REQUEST.csv')[0]; config=release(folder/'RELEASE.csv',req,check_code=False)
    history=p.read_rows(folder/'HISTORY.csv'); checked=set()
    horizon,_=p.information_horizon(req)
    if len(history)!=int(rec['training_rows']) or len({r['event_id'] for r in history})!=len(history):
        raise p.AdmissionError('training coverage/identity differs from frozen receipt')
    for row in history:
        if row['event_id']==req['event_id'] or row['competition']!=req['competition'] or row['endpoint']!=req['endpoint'] or p.clock(row['event_at'])>=horizon.normalize() or p.clock(row['label_available_at'])>horizon:
            raise p.AdmissionError('training scope/time/target leakage')
        token=(row['evidence_path'],row['evidence_sha256'])
        if token not in checked: p.receipt_file(*token); checked.add(token)
    if rec['release_sha256']!=p.digest((folder/'RELEASE.csv').read_bytes()) or rec['code_sha256']!=config['code_sha256']:
        raise p.AdmissionError("bundle differs from frozen version")
    if any(rec[k]!=req[k] for k in ('event_id','competition','endpoint','issue_at','scheduled_start')):
        raise p.AdmissionError("receipt identity differs from request")
    fb=p.read_rows(folder/'ADAPTATION.csv')
    if any(p.clock(r['available_at'])>p.clock(rec['information_horizon']) for r in fb):
        raise p.AdmissionError("future feedback")
    w,_,eta,mass=adaptive_weights(fb,config)
    frozen=p._parse_vector(rec['weights'])
    if not np.allclose(w,[frozen[a] for a in ARMS],atol=1e-12,rtol=0) or abs(eta-float(rec['eta']))>1e-12 or abs(mass-float(rec['effective_feedback_events']))>1e-12:
        raise p.AdmissionError("online weights differ from frozen feedback")
    grids=load_grids(folder); mix=p.mix_grids([grids[a] for a in ARMS],w)
    contracts=p.read_rows(folder/'CONTRACTS.csv'); preds=p.read_rows(folder/'PREDICTIONS.csv')
    if len(preds)!=len(contracts): raise p.AdmissionError("incomplete contract coverage")
    for row,contract in zip(preds,contracts):
        if any(row[k]!=v for k,v in contract.items()): raise p.AdmissionError("contract semantics changed")
        values=p.price(mix,contract,rec['endpoint']); baseline=p.price(grids[ARMS[2]],contract,rec['endpoint'])
        for keys,expected in ((('win','push','loss'),values),(('baseline_win','baseline_push','baseline_loss'),baseline)):
            if any(not math.isfinite(float(row[k])) or abs(float(row[k])-v)>1e-10 for k,v in zip(keys,expected)):
                raise p.AdmissionError("frozen contract mass differs from grid")
        for key,masses in (('p_card',values),('baseline_p',baseline)):
            expected=masses[0]/(masses[0]+masses[2]) if masses[0]+masses[2] else 'NOT_COMPUTED'
            if (expected=='NOT_COMPUTED' and row[key]!=expected) or (expected!='NOT_COMPUTED' and (not math.isfinite(float(row[key])) or abs(float(row[key])-expected)>1e-10)):
                raise p.AdmissionError("frozen probability differs from masses")
    return rec


def shadow_rows(folder, now_at=None):
    rec=verify_bundle(folder); at=p.clock(now_at or now())
    status=ps._status(rec['generated_at'],rec['scheduled_start'],at)
    req=p.read_rows(Path(folder)/'REQUEST.csv')[0]
    if req.get('actual_start') and (p.clock(rec['generated_at'])>=p.clock(req['actual_start']) or at>=p.clock(req['actual_start'])):
        status='POST_START'
    rows=[]
    for role,model,prob in (('CANDIDATE',POLICY,'p_card'),('CHAMPION',rec['baseline'],'baseline_p')):
        base=ps._common(model,rec['version'],role,rec['event_id'],rec['competition'],rec['endpoint'],rec['generated_at'],
                        rec['scheduled_start'],'STORE:'+rec['store_digest'],rec['release_sha256'],rec['code_sha256'],status)
        for row in p.read_rows(Path(folder)/'PREDICTIONS.csv'):
            if row[prob]=='NOT_COMPUTED': continue
            # Definition and action are part of identity, not an informal display label.
            key=p.digest(p.csv_bytes([{k:row[k] for k in ('family','side','line','endpoint','definition','action')}]))[:24]
            rows.append(dict(forecast_id=rec['event_id']+':'+model,contract_key=key,family=row['family'],side=row['side'],
                             line=row['line'],p=row[prob],rank=row['rank'],**base))
    return rows


def settle(bundle, export, store, output):
    """Ingest the actual result and rederive every expert loss from its frozen grid."""
    rec=verify_bundle(bundle); ingest=ri.ingest(Path(export),Path(store)); st=ri.load_store(Path(store))
    if int(ingest['quarantined']):
        raise p.AdmissionError('settlement export has quarantined observations; reconcile before feedback')
    req=p.read_rows(Path(bundle)/'REQUEST.csv')[0]
    uid=ri.resolve_event(st.events,st.event_aliases,req['competition'],req['event_id'],req['scheduled_start'],req['home'],req['away'])
    results=ri.effective_results(st); hit=results[results.event_uid==uid]
    if len(hit)!=1 or hit.iloc[0].status!='FINAL': raise p.AdmissionError("one verified final result required; quarantine or missing result cannot train")
    lab=hit.iloc[0]
    if not p.clock(rec['generated_at'])<p.clock(lab.final_at)<=lab.valid_from:
        raise p.AdmissionError("settlement predates actual generated forecast; historical outcomes cannot masquerade as feedback")
    obs=st.source_observations; obs=obs[(obs.event_uid==uid)&(obs.kind=='RESULT')&(obs.link==str(lab.revision))]
    src=obs.sort_values('known_at').iloc[0]; p.receipt_file(src.capture_path,src.capture_sha256)
    grids=load_grids(bundle); hs,away=int(lab.hs),int(lab.as_)
    row=dict(event_id=req['event_id'],competition=req['competition'],endpoint=req['endpoint'],
             bundle=str(Path(bundle).resolve()),receipt_sha256=p.digest((Path(bundle)/'RECEIPT.csv').read_bytes()),
             release_sha256=rec['release_sha256'],home_score=hs,away_score=away,final_at=lab.final_at,
             available_at=lab.valid_from.isoformat(),event_uid=uid,result_revision=lab.revision,
             evidence_path=src.capture_path,evidence_sha256=src.capture_sha256,
             **{'loss_'+a:loss(g,hs,away,float(rec['loss_scale'])) for a,g in grids.items()})
    output=Path(output); output.mkdir(parents=True,exist_ok=False)
    write_rows(output/'SETTLEMENT.csv',[row]); write_rows(output/'INGEST.csv',[ingest])
    final=ScoreGrid(np.ones((1,1)),hs,away); shadows=shadow_rows(bundle); keys={(r['model_id'],r['contract_key']):r for r in shadows}
    outcomes=[]
    for prediction in p.read_rows(Path(bundle)/'PREDICTIONS.csv'):
        w,pu,l=p.price(final,prediction,rec['endpoint'])
        key=p.digest(p.csv_bytes([{k:prediction[k] for k in ('family','side','line','endpoint','definition','action')}]))[:24]
        if not any(k[1]==key for k in keys): continue
        outcomes.append(dict(event_id=req['event_id'],contract_key=key,result='PUSH' if pu else 'WIN' if w else 'LOSS',
                             final_at=lab.final_at,available_at=lab.valid_from.isoformat(),evidence_sha256=src.capture_sha256))
    write_rows(output/'OUTCOMES.csv',outcomes,ps.OUTCOME_FIELDS)
    verify_settlement(output)
    return row


def verify_settlement(folder):
    rows=p.read_rows(Path(folder)/'SETTLEMENT.csv')
    if len(rows)!=1: raise p.AdmissionError("one effective settlement required")
    row=rows[0]; rec=verify_bundle(Path(row['bundle']))
    p.receipt_file(Path(row['bundle'])/'RECEIPT.csv',row['receipt_sha256']); p.receipt_file(row['evidence_path'],row['evidence_sha256'])
    if any(row[k]!=rec[k] for k in ('event_id','competition','endpoint','release_sha256')): raise p.AdmissionError("settlement identity/version differs")
    if not p.clock(rec['generated_at'])<p.clock(row['final_at'])<=p.clock(row['available_at']): raise p.AdmissionError("invalid feedback chronology")
    scores=[float(row[k]) for k in ('home_score','away_score')]
    if any(not math.isfinite(v) or v<0 or v!=int(v) for v in scores): raise p.AdmissionError("invalid feedback score")
    for arm,g in load_grids(row['bundle']).items():
        if abs(float(row['loss_'+arm])-loss(g,*scores,float(rec['loss_scale'])))>1e-12: raise p.AdmissionError("feedback loss differs from frozen grid")
    return row


def evaluate(release_path, ledger, feedback_root, output):
    """Evaluate this frozen experiment, with auditable exclusions and paired proper-score intervals."""
    config=release(release_path,check_code=False); ledger_rows=ps.verify_ledger(Path(ledger))
    frozen_release_sha=p.digest(p.csv_bytes([config]))
    rows=[r for r in ledger_rows if r['competition']==config['competition'] and r['endpoint']==config['endpoint'] and
          r['model_version']==config['version'] and r['param_version']==frozen_release_sha]
    outcomes=[]; manifests=[]; effective={}
    for path in sorted(Path(feedback_root).glob('*/SETTLEMENT.csv')):
        row=verify_settlement(path.parent)
        if row['release_sha256']!=frozen_release_sha or p.clock(row['available_at'])>p.clock(now()): continue
        old=effective.get(row['event_id'])
        if old is None or int(row['result_revision'])>int(old['result_revision']): effective[row['event_id']]=row
    for event,row in effective.items():
        # Recompute terminal contract labels from verified frozen definitions and scores.
        final=ScoreGrid(np.ones((1,1)),int(row['home_score']),int(row['away_score']))
        for contract in p.read_rows(Path(row['bundle'])/'CONTRACTS.csv'):
            w,pu,l=p.price(final,contract,row['endpoint'])
            key=p.digest(p.csv_bytes([{k:contract[k] for k in ('family','side','line','endpoint','definition','action')}]))[:24]
            outcomes.append(dict(event_id=event,contract_key=key,result='PUSH' if pu else 'WIN' if w else 'LOSS',
                                 final_at=row['final_at'],available_at=row['available_at'],evidence_sha256=row['evidence_sha256']))
        manifests.append(dict(event_id=event,bundle=row['bundle'],receipt_sha256=row['receipt_sha256'],result_revision=row['result_revision'],evidence_sha256=row['evidence_sha256']))
    result=ps.evaluate(rows,pd.DataFrame(outcomes,columns=ps.OUTCOME_FIELDS),
                       'COMPETITION_FINAL_LEAGUE_V1:'+config['version'],POLICY+':'+config['version'],delta=float(config['minimum_brier_effect']))
    events=result.get('interval',{}).get('n_events',0)
    if events<int(config['minimum_events']):
        result.update(disposition='INSUFFICIENT_EVIDENCE',reason=f"{events} paired events; frozen minimum {config['minimum_events']}")
    output=Path(output); output.mkdir(parents=True,exist_ok=False)
    write_rows(output/'OUTCOMES.csv',outcomes,ps.OUTCOME_FIELDS)
    write_rows(output/'SOURCES.csv',manifests,('event_id','bundle','receipt_sha256','result_revision','evidence_sha256'))
    write_rows(output/'MODEL_METRICS.csv',[dict(model=tag,**values) for tag,values in result.get('models',{}).items()],('model','rows','events','brier','log_loss','slope','intercept'))
    intervals=[dict(metric=name,**values) for name,values in (('BRIER',result.get('interval',{})),('LOG_LOSS',result.get('log_loss_interval',{}))) if values]
    write_rows(output/'PAIRED_INTERVALS.csv',intervals,('metric','n_events','k_weeks','mean','lo','hi','status'))
    if rows and outcomes:
        from ml.core.metrics import reliability_table
        graded=ps._grade(pd.DataFrame(rows),pd.DataFrame(outcomes))
        paired=graded.groupby(['event_id','contract_key']).model_id.nunique()
        keep=set(paired[paired==2].index)
        graded=graded[[tuple(v) in keep for v in graded[['event_id','contract_key']].to_numpy()]]
        reliability=[]
        for model,g in graded[graded.y.notna()].groupby('model_id'):
            reliability += [dict(model=model,**r) for r in reliability_table(g.p.astype(float),g.y).to_dict('records')]
        write_rows(output/'CALIBRATION_BINS.csv',reliability,('model','bin','n'))
    summary=dict(policy=POLICY,version=config['version'],generated_at=now(),disposition=result['disposition'],reason=result['reason'],
                 paired_events=events,paired_contracts=result.get('pairs',0),release_sha256=frozen_release_sha,
                 ledger_sha256=p.digest(Path(ledger).read_bytes()) if Path(ledger).exists() else 'NONE',
                 qualification='EVALUATION_RECOMMENDATION_ONLY_NO_AUTOMATIC_PROMOTION',
                 **{f.stem.lower()+'_sha256':p.digest(f.read_bytes()) for f in output.glob('*.csv')})
    write_rows(output/'EVALUATION.csv',[summary])
    (output/'REPORT.md').write_text('# Frozen prospective evaluation\n\n'+result['disposition']+': '+result['reason']+'\n\nBrier, log loss and calibration use identical settled contract pairs. Differences average within event and then ISO week; intervals are paired week t-intervals. Minimum 50 events and eight weeks are admission floors, not proof of skill. Future or post-start rows and pushes/voids cannot become decisive probability labels. Raw terminal scores and grid definitions are reverified; no promotion or registry transition occurs automatically.\n',encoding='utf-8')
    return summary


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__); sub=parser.add_subparsers(dest='command',required=True)
    fr=sub.add_parser('release')
    for name in ('competition','endpoint','version','out'): fr.add_argument('--'+name,required=True)
    vf=sub.add_parser('verify'); vf.add_argument('--bundle',type=Path,required=True)
    st=sub.add_parser('settle')
    for name in ('bundle','export','store','out'): st.add_argument('--'+name,type=Path,required=True)
    ev=sub.add_parser('evaluate')
    for name in ('release','ledger','feedback-root','out'): ev.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args(argv)
    if args.command=='release': print(freeze_release(Path(args.out),args.competition,args.endpoint,args.version))
    elif args.command=='verify': print(verify_bundle(args.bundle))
    elif args.command=='settle': print(settle(args.bundle,args.export,args.store,args.out))
    else: print(evaluate(args.release,args.ledger,args.feedback_root,args.out))


if __name__=='__main__': main()

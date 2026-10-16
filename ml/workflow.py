"""Stdlib-only execution boundary: even dependency, input and adapter failures get real receipts.

python -m ml.workflow research --export DIR --store DIR --request REQUEST.csv
    --contracts CONTRACTS.csv --release RELEASE.csv --out ATTEMPT [--feedback-root DIR] [--ledger CSV]
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
from pathlib import Path
import traceback


def _bytes(rows):
    text=io.StringIO(newline=''); writer=csv.DictWriter(text,fieldnames=list(rows[0]),lineterminator='\n')
    writer.writeheader(); writer.writerows(rows); return text.getvalue().encode()


def _read(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as handle: return list(csv.DictReader(handle))


def _hash(data): return hashlib.sha256(data).hexdigest()
def _now(): return datetime.now(timezone.utc).isoformat()


def execute(export,store,request,contracts,release,out,feedback_root=None,ledger=None,*,adapter='context',history=None,feedback=None,competition_source=None):
    out=Path(out); out.mkdir(parents=True,exist_ok=False)
    started=dict(started_at=_now(),entrypoint='python -m ml.workflow research')
    (out/'STARTED.csv').write_bytes(_bytes([started]))
    rec=dict(**started,event_id='UNKNOWN',competition='UNKNOWN',endpoint='UNKNOWN',status='FAILED',stage='INPUT_CAPTURE',
             completed_at='',bundle='',bundle_sha256='',error_type='',error='',traceback_sha256='',adapter=adapter)
    inputs=[]
    try:
        for name,path in (('REQUEST',request),('CONTRACTS',contracts),('RELEASE',release),('HISTORY',history),('FEEDBACK',feedback),('COMPETITION_SOURCE',competition_source)):
            if path is None: continue
            raw=Path(path).read_bytes(); (out/(name+'.csv')).write_bytes(raw)
            inputs.append(dict(name=name,path=str(path),sha256=_hash(raw)))
            if name=='REQUEST':
                reqs=_read(out/'REQUEST.csv')
                if len(reqs)!=1: raise ValueError('exactly one research event per attempt')
                req=reqs[0]
                for key in ('event_id','competition'): rec[key]=req[key]
                rec['endpoint']=req.get('endpoint','COMPLETED_BEST_OF_'+str(req.get('best_of','UNKNOWN')))
        for path in sorted(Path(export).glob('*.csv')):
            raw=path.read_bytes(); saved=out/'EXPORT'/path.name; saved.parent.mkdir(exist_ok=True); saved.write_bytes(raw)
            inputs.append(dict(name='EXPORT/'+path.name,path=str(path),sha256=_hash(raw)))
        reqs=_read(out/'REQUEST.csv')
        if len(reqs)!=1: raise ValueError('exactly one research event per attempt')
        req=reqs[0]
        for key in ('event_id','competition'): rec[key]=req[key]
        rec['endpoint']=req.get('endpoint','COMPLETED_BEST_OF_'+str(req.get('best_of','UNKNOWN')))
        rec['stage']='RUNTIME_IMPORT'
        from ml import cycle, capability, primary as p, research_ingest as ri
        (out/'CAPABILITY.csv').write_bytes(p.csv_bytes([capability.receipt()]))
        rec['stage']='RESEARCH_INGEST'
        ingest=ri.ingest(out/'EXPORT',Path(store))
        (out/'INGEST.csv').write_bytes(p.csv_bytes([ingest]))
        # A successful store transaction may contain quarantined rows: record them, never treat them as admitted.
        rec['stage']='FORECAST'
        bundle=out/'BUNDLE'
        if adapter=='context':
            result=cycle.forecast(Path(store),req,p.read_rows(out/'CONTRACTS.csv'),out/'RELEASE.csv',bundle,feedback_root)
            cycle.verify_bundle(bundle)
            rows=cycle.shadow_rows(bundle)
        elif adapter in ('primary','tennis'):
            if history is None: raise ValueError('exact adapter-specific reviewed HISTORY.csv is required')
            from ml.evaluation import prospective as ps
            if adapter=='primary':
                source=p.read_rows(out/'COMPETITION_SOURCE.csv') if competition_source else None
                result=p.forecast(req,None if source else p.get_league(req['competition']),p.read_rows(out/'HISTORY.csv'),p.read_rows(out/'CONTRACTS.csv'),bundle,
                                  p.read_rows(out/'FEEDBACK.csv') if feedback else [],competition_source=source)
                rows=ps.rows_from_primary_bundle(bundle,'CANDIDATE')
            else:
                from ml import tennis_primary as t
                t.forecast(req,p.read_rows(out/'HISTORY.csv'),p.read_rows(out/'CONTRACTS.csv'),p.read_rows(out/'FEEDBACK.csv') if feedback else [],bundle)
                rows=ps.rows_from_tennis_bundle(bundle,'CANDIDATE')
            preds={r['contract_key']:r for r in p.read_rows(bundle/'PREDICTIONS.csv')}
            # Use actual generation time: a historical declared issue cannot create a fresh pre-start shadow.
            actual=_now()
            probabilities={}
            for row in rows:
                original_key=row['contract_key']
                contract=next(r for r in p.read_rows(out/'CONTRACTS.csv') if r['contract_key']==original_key)
                semantic={k:contract[k] for k in ('family','side','line','endpoint','definition','action') if k in contract}
                semantic.setdefault('endpoint',rec['endpoint'])
                row['contract_key']=_hash(_bytes([semantic]))[:24]
                probabilities[row['contract_key']]=preds[original_key]['baseline_p']
                row['issued_at']=actual; row['evidence_status']=ps._status(actual,row['scheduled_start'],p.clock(actual))
                if req.get('actual_start') and p.clock(actual)>=p.clock(req['actual_start']): row['evidence_status']='POST_START'
            baseline=[dict(r,model_id='BASELINE_LEAGUE_V1' if adapter=='primary' else 'TENNIS_COHORT_BASE_V1',role='CHAMPION',
                           forecast_id=r['forecast_id']+':BASELINE',p=probabilities[r['contract_key']]) for r in rows]
            rows+=baseline
        else: raise ValueError('unknown runtime adapter')
        rec.update(bundle='BUNDLE',bundle_sha256=_hash((bundle/'RECEIPT.csv').read_bytes()))
        rec['stage']='SHADOW_FREEZE'
        (out/'SHADOW_ROWS.csv').write_bytes(p.csv_bytes(rows))
        if ledger is not None:
            from ml.evaluation.prospective import freeze
            freeze(Path(ledger),rows)
        rec.update(status='EXECUTED',stage='COMPLETE')
    except Exception as exc:
        # Never convert a failed ledger append or half-built directory into an issued success.
        raw=traceback.format_exc().encode(); (out/'FAILURE.txt').write_bytes(raw)
        rec.update(error_type=type(exc).__name__,error=str(exc),traceback_sha256=_hash(raw))
    rec['completed_at']=_now()
    (out/'INPUTS.csv').write_bytes(_bytes(inputs) if inputs else b'name,path,sha256\n')
    rec['inputs_sha256']=_hash((out/'INPUTS.csv').read_bytes()); rec['started_sha256']=_hash((out/'STARTED.csv').read_bytes())
    # Attempt manifest also binds diagnostics/capability/ingest outputs, including an available bundle on partial failure.
    files=[dict(path=f.relative_to(out).as_posix(),sha256=_hash(f.read_bytes())) for f in sorted(out.rglob('*')) if f.is_file()]
    (out/'FILES.csv').write_bytes(_bytes(files)); rec['files_sha256']=_hash((out/'FILES.csv').read_bytes())
    (out/'EXECUTION.csv').write_bytes(_bytes([rec])); verify(out)
    return rec


def verify(folder):
    folder=Path(folder); rows=_read(folder/'EXECUTION.csv')
    if len(rows)!=1: raise ValueError('one completed execution receipt required')
    rec=rows[0]
    for name in ('INPUTS','STARTED','FILES'):
        if _hash((folder/(name+'.csv')).read_bytes())!=rec[name.lower()+'_sha256']: raise ValueError('execution custody mismatch: '+name)
    for row in _read(folder/'FILES.csv'):
        path=(folder/row['path']).resolve()
        if not path.is_relative_to(folder.resolve()) or _hash(path.read_bytes())!=row['sha256']: raise ValueError('attempt file changed/escaped')
    if datetime.fromisoformat(rec['completed_at'])<datetime.fromisoformat(rec['started_at']): raise ValueError('invalid attempt clock')
    if rec['status']=='EXECUTED':
        if rec['stage']!='COMPLETE' or rec['bundle']!='BUNDLE' or rec['error'] or rec['error_type']: raise ValueError('invalid success receipt')
        if rec['adapter']=='context':
            from ml.cycle import verify_bundle
            model=verify_bundle(folder/'BUNDLE')
        elif rec['adapter']=='primary':
            from ml.primary import verify_bundle
            model=verify_bundle(folder/'BUNDLE')
        else:
            from ml.tennis_primary import verify
            verify(folder/'BUNDLE')
            model=_read(folder/'REQUEST.csv')[0]
            model=dict(model,endpoint='COMPLETED_BEST_OF_'+model['best_of'])
        if _hash((folder/'BUNDLE'/'RECEIPT.csv').read_bytes())!=rec['bundle_sha256'] or any(model[k]!=rec[k] for k in ('event_id','competition','endpoint')): raise ValueError('execution differs from forecast')
    elif rec['status']=='FAILED':
        if not rec['error_type'] or not rec['error'] or _hash((folder/'FAILURE.txt').read_bytes())!=rec['traceback_sha256']: raise ValueError('failure lacks actual diagnostics')
    else: raise ValueError('incomplete execution')
    return rec


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__); sub=parser.add_subparsers(dest='command',required=True)
    run=sub.add_parser('research')
    for name in ('export','store','request','contracts','out'): run.add_argument('--'+name,type=Path,required=True)
    for name in ('release','history','feedback','competition-source'): run.add_argument('--'+name,type=Path)
    run.add_argument('--adapter',choices=('context','primary','tennis'),default='context')
    run.add_argument('--feedback-root',type=Path); run.add_argument('--ledger',type=Path)
    check=sub.add_parser('verify'); check.add_argument('--attempt',type=Path,required=True)
    args=parser.parse_args(argv)
    if args.command=='verify': print(verify(args.attempt)['status']); return
    result=execute(args.export,args.store,args.request,args.contracts,args.release,args.out,args.feedback_root,args.ledger,
                   adapter=args.adapter,history=args.history,feedback=args.feedback,competition_source=args.competition_source)
    print(result['status']+': '+str(args.out/'EXECUTION.csv')+' '+result['error'])
    if result['status']!='EXECUTED': raise SystemExit(1)


if __name__=='__main__': main()

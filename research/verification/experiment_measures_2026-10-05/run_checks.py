"""Retain real command output for the final local implementation checks."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,subprocess,sys

ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
COMMANDS={
 'regressions':['-m','pytest','-p','no:cacheprovider','research/tests','research/operations','research/experiments','-q'],
 'experiment_protocols':['-m','research.experiments.runner','verify'],
 'experiment_readiness':['-m','research.experiments.runner','status'],
 'canonical_storage':['-m','research.operations.log_card','verify'],
 'full_local_custody':['-m','research.operations.verify_custody'],
 'document_reconciliation':['-m','research.operations.verify_reconciliation'],
 'selected_control_freeze':['-m','research.operations.control_freeze','--verify'],
 'all_log_readback':['-m','research.operations.verify_all_logs'],
 'original_artifacts_and_links':[str(OUT/'verify_delivery.py')],
}

def check(item):
    name,args=item;command=[sys.executable,'-X','utf8','-B',*args]
    start=datetime.now(timezone.utc).isoformat()
    value=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='strict')
    result=dict(command=command,started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),returncode=value.returncode,stdout=value.stdout,stderr=value.stderr)
    print(name+': '+str(value.returncode),flush=True)
    return name,result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='local_checks.json');parser.add_argument('--reuse')
    parser.add_argument('--only',choices=list(COMMANDS));args=parser.parse_args()
    target=(OUT/args.output).resolve()
    if target.parent!=OUT:raise ValueError('Output must stay in this dated evidence folder')
    if target.exists():raise FileExistsError('Keep prior checks; use a separately versioned result')
    results={};reuse=None
    if args.reuse:
        if not args.only:raise ValueError('Specify the corrected check when reusing other results')
        path=(OUT/args.reuse).resolve()
        if path.parent!=OUT:raise ValueError('Reused evidence must stay in this folder')
        raw=path.read_bytes();results=json.loads(raw)['checks']
        if set(results)!=set(COMMANDS) or any(r['returncode']!=0 for k,r in results.items() if k!=args.only):raise ValueError('Cannot reuse failed or incomplete other checks')
        reuse=dict(path=path.name,sha256=hashlib.sha256(raw).hexdigest(),rerun_check=args.only,
                   reason='Changed verification scope records inherited historical links separately; unchanged successful checks retained.')
    elif args.only:raise ValueError('Single-check mode needs the other retained successful checks')
    target.write_text(json.dumps(dict(status='RUNNING'))+'\n',encoding='utf-8')
    commands={args.only:COMMANDS[args.only]} if args.only else COMMANDS
    with ThreadPoolExecutor(max_workers=3) as pool:results.update(dict(pool.map(check,commands.items())))
    result=dict(passed=all(r['returncode']==0 for r in results.values()),checks=results,
                reused_checks=reuse,
                limitation='Software/custody checks only; synthetic tests establish no model performance.')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(passed=result['passed'],commands=len(results)),indent=2))
    return not result['passed']

if __name__=='__main__':raise SystemExit(main())

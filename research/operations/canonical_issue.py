"""Current issuer adapter; keep the model-pinned historical issuer unchanged.

The isolated module namespace preserves the frozen validation/transaction code
while substituting destination custody and the shared current ID allocator.
No production module globals or historical source bytes are patched.
"""
from pathlib import Path
import argparse
import importlib.util
import json
import re
from research.src import issue as legacy
from research.src.combined_log import active_log, custody
from research.src.ledger import committed_issues, read_records


def next_card_id(part6_path=None, reconciliation_path=legacy.RECONCILIATION,
                 ledger_path=legacy.CANONICAL_LEDGER):
    path=Path(part6_path) if part6_path is not None else active_log()
    _,tail=custody(path)
    reserved=Path(reconciliation_path).read_text(encoding='utf-8')
    if 'reserved' not in reserved.lower() or not all(re.search(rf'P-{n}\b',reserved) for n in range(518,523)):
        raise ValueError('authoritative reserved-ID reconciliation is unavailable')
    records=read_records(ledger_path)
    completed={r['payload']['transaction_id'] for r in records if r['record_type'] in
               {'ISSUE_COMMITTED','RESEARCH_LOG_COMMITTED','RESEARCH_ADDENDUM_COMMITTED'}}
    if any(r['payload']['transaction_id'] not in completed for r in records if r['record_type'] in
           {'ISSUE_PREPARED','RESEARCH_LOG_PREPARED','RESEARCH_ADDENDUM_PREPARED'}):
        raise ValueError('pending canonical transaction must be recovered before assigning another ID')
    tails=[tail]
    if legacy.BEGIN_ORIGINAL not in path.read_bytes():
        previous=path.parents[1]/'prediction logs/PREDICTION_LOG_COMBINED_6.md'
        tails.append(legacy._custody(previous)[1])
    ids=[522]
    for body in tails:
        text=body.decode('utf-8')
        ids += [int(n) for n in re.findall(r'(?m)^<!-- BEGIN CANONICAL (?:ISSUE|RESEARCH) P-(\d+) ',text)]
        ids += [int(n) for n in re.findall(r'(?m)^#{1,6}\s+(?:Prediction\s+|Game(?:\s+Card)?\s+)?P-(\d+)\b',text)]
    ids += [int(c['card_id'][2:]) for c in committed_issues(records)]
    ids += [int(r['payload']['card_id'][2:]) for r in records if r['record_type']=='RESEARCH_LOG_COMMITTED']
    return f'P-{max(ids)+1}'


def _adapter():
    spec=importlib.util.spec_from_file_location('research.src._current_issuer_adapter',Path(legacy.__file__))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module._custody=custody
    module.next_card_id=next_card_id
    return module


def prepare_issue(bundle,registry_path=legacy.REGISTRY,**kwargs):
    if kwargs.get('part6_path') is None:kwargs['part6_path']=active_log()
    return _adapter().prepare_issue(bundle,registry_path,**kwargs)


def commit_issue(transaction,**kwargs):
    return _adapter().commit_issue(transaction,**kwargs)


def recover_issue(ledger_path,transaction_id,**kwargs):
    return _adapter().recover_issue(ledger_path,transaction_id,**kwargs)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['next-id','prepare','commit','recover'])
    parser.add_argument('input',type=Path,nargs='?')
    parser.add_argument('output',type=Path,nargs='?')
    parser.add_argument('--transaction-id')
    parser.add_argument('--allow-real-issue',action='store_true')
    args=parser.parse_args()
    if args.command=='next-id':result={'next_id':next_card_id()}
    elif args.command=='recover':
        if not args.input or not args.transaction_id:parser.error('recover needs ledger and --transaction-id')
        result=recover_issue(args.input,args.transaction_id,allow_real_issue=args.allow_real_issue)
    else:
        if not args.input:parser.error('prepare/commit needs JSON input')
        value=json.loads(args.input.read_text(encoding='utf-8'))
        result=prepare_issue(value) if args.command=='prepare' else commit_issue(value,allow_real_issue=args.allow_real_issue)
        if args.command=='prepare':
            if not args.output:parser.error('prepare needs output path')
            with args.output.open('x',encoding='utf-8') as handle:json.dump(result,handle,indent=2)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

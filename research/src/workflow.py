"""Operator CLI for evidence-gated research, issuance and settlement."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from datetime import datetime, timezone
from .load import ROOT, sha
from .eligibility import validate_evidence
from .ledger import register_universe, record_abstention, append_settlement_revision, read_records, committed_issues
from .issue import prepare_issue, commit_issue, recover_issue, CANONICAL_LEDGER, next_card_id
from .pilot import score_events, freeze_lock, decision
from .daily import put_json, run


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def status():
    records=read_records(CANONICAL_LEDGER)
    return dict(observed_utc=datetime.now(timezone.utc).isoformat(),next_card_id=next_card_id(),
                canonical_records=len(records),canonical_issued_events=len(committed_issues(records)),
                admissions=[{k:r[k] for k in ("lane","model_version","families","endpoint","status")}
                            for r in read(ROOT/"admission_registry.json")["admissions"]],
                source_independence={k:v["independence_status"] for k,v in read(ROOT/"sources_registry.json")["sources"].items()},
                prospective_skill="NOT_ESTABLISHED")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="command",required=True)
    sub.add_parser("status")
    daily=sub.add_parser("daily");daily.add_argument("--window-hours",type=int,default=48)
    for command in ("validate-bundle","register-universe","prepare-issue","settle"):
        p=sub.add_parser(command);p.add_argument("input",type=Path)
        if command=="prepare-issue":p.add_argument("output",type=Path)
        if command=="validate-bundle":p.add_argument("--terminal",action="store_true")
        if command=="settle":p.add_argument("--reason",required=True)
    p=sub.add_parser("abstain");p.add_argument("identity",type=Path);p.add_argument("reason");p.add_argument("evidence_refs",type=Path)
    p=sub.add_parser("commit-issue");p.add_argument("transaction",type=Path);p.add_argument("--real",action="store_true")
    p=sub.add_parser("recover-issue");p.add_argument("transaction_id");p.add_argument("--real",action="store_true")
    p=sub.add_parser("score");p.add_argument("--ledger",type=Path,default=CANONICAL_LEDGER)
    p=sub.add_parser("pilot-freeze");p.add_argument("definition",type=Path);p.add_argument("output",type=Path)
    p=sub.add_parser("pilot-decision");p.add_argument("lock",type=Path)
    args=parser.parse_args()
    if args.command=="status":result=status()
    elif args.command=="daily":
        path,result=run(args.window_hours);result["path"]=str(path)
    elif args.command=="validate-bundle":
        checked=validate_evidence(read(args.input),require_terminal=args.terminal)
        result=dict(eligible=checked.eligible,reasons=checked.reasons,verified=checked.verified)
    elif args.command=="register-universe":
        result=register_universe(CANONICAL_LEDGER,dict(path=str(args.input.resolve()),sha256=sha(args.input)),evidence_root=ROOT.parent)
    elif args.command=="abstain":
        result=record_abstention(CANONICAL_LEDGER,read(args.identity),args.reason,evidence_refs=read(args.evidence_refs),evidence_root=ROOT.parent)
    elif args.command=="prepare-issue":
        result=prepare_issue(read(args.input));put_json(args.output,result)
    elif args.command=="commit-issue":result=commit_issue(read(args.transaction),allow_real_issue=args.real)
    elif args.command=="recover-issue":result=recover_issue(CANONICAL_LEDGER,args.transaction_id,allow_real_issue=args.real)
    elif args.command=="settle":result=append_settlement_revision(CANONICAL_LEDGER,read(args.input),reason=args.reason)
    elif args.command=="score":
        frame=score_events(args.ledger);result=dict(events=frame.to_dict("records"),coverage={k:v for k,v in frame.attrs.items() if k!="issues"})
    elif args.command=="pilot-freeze":result=freeze_lock(args.output,read(args.definition),ledger_path=CANONICAL_LEDGER)
    else:result=decision(CANONICAL_LEDGER,args.lock)
    print(json.dumps(result,indent=2,default=str,allow_nan=False))
    if args.command=="validate-bundle" and not result["eligible"]:return 1
    if args.command=="daily" and result["status"]!="COMPLETE":return 1
    return 0


if __name__=="__main__":
    raise SystemExit(main())

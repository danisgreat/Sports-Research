"""Source-linked historical learning views; never reconstruct prospective skill.

Rank-log literals are claims, not independently verified results or forecasts.
Missing baselines, issue cutoffs, IDs and endpoints stay missing.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from functools import lru_cache
from .load import ROOT, sha

REPO=ROOT.parent
RANKS=REPO/"GAME_PREDICTION_RANK_LOG.csv"
OUTPUT=ROOT/"data/processed/legacy_learning"


@lru_cache(maxsize=24)
def source_lines(path):
    return Path(path).read_text(encoding="utf-8-sig").splitlines(),sha(Path(path))


def pointer_receipt(pointer, root=REPO):
    match=re.fullmatch(r"([^:;]+\.md):(\d+)",pointer.strip())
    if not match:
        return dict(status="UNRESOLVED_POINTER", pointer=pointer)
    name,line=match.groups(); candidates=[Path(root)/name,Path(root)/"prediction logs"/name]
    preserved=Path(root)/"research/custody/implementation_2026-10-01"/name
    # Original index references bind the historical header/line positions.
    # Prefer the retained pre-overhaul bytes when a root document was reworked.
    path=preserved if preserved.is_file() else next((p for p in candidates if p.is_file()),None)
    if path is None:
        return dict(status="MISSING_SOURCE_FILE",pointer=pointer)
    lines,file_checksum=source_lines(path)
    if not 1<=int(line)<=len(lines):
        return dict(status="SOURCE_LINE_OUT_OF_RANGE",pointer=pointer)
    text=lines[int(line)-1]
    return dict(status="PATH_AND_LINE_VERIFIED_ONLY",pointer=pointer,path=path.relative_to(root).as_posix(),
                line=int(line),file_sha256=file_checksum,line_sha256=hashlib.sha256(text.encode()).hexdigest())


def literal_probability(value):
    if not value:
        return None
    try:
        p=float(value)
        return p if math.isfinite(p) and 0<=p<=1 else None
    except ValueError:
        return None


def build(output=OUTPUT):
    output=Path(output)
    if output.exists():
        raise FileExistsError("historical view already exists; use a new dated revision")
    original=list(csv.DictReader(RANKS.open(encoding="utf-8-sig",newline="")))
    grains=Counter((r["card_id"],r["rank"]) for r in original)
    normalized=[]; pointers={}; cards=defaultdict(list)
    for ordinal,row in enumerate(original,2):
        pointer=row["grade_source"]
        pointers.setdefault(pointer,pointer_receipt(pointer))
        conflicts=[]
        if not row["rank"].isdigit(): conflicts.append("RANK_NOT_PRESERVED")
        if grains[(row["card_id"],row["rank"])]>1: conflicts.append("DUPLICATE_CARD_RANK")
        if row["source_claim_or_conflict"]: conflicts.append(row["source_claim_or_conflict"])
        if row["logged_result"] not in {"W","L","P"}: conflicts.append("UNRESOLVED_GRADE")
        if pointers[pointer]["status"]!="PATH_AND_LINE_VERIFIED_ONLY": conflicts.append("UNRESOLVED_GRADE_POINTER")
        p=literal_probability(row["stated_p"])
        if row["stated_p"] and p is None: conflicts.append("INVALID_P_LITERAL")
        result=row["logged_result"]
        diagnostic=((p-int(result=="W"))**2 if p is not None and result in {"W","L"} and not conflicts else None)
        record=dict(card_id=row["card_id"],rank=row["rank"],event=row["event"],
                    contract_literal=row["selection_or_contract"],family="NOT_EXTRACTED",endpoint="NOT_EXTRACTED",
                    official_event_id="",issued_utc="",data_cutoff_utc="",actual_start_utc="",
                    stated_p_literal=row["stated_p"],stated_p=p,ranking_q_literal=row["ranking_q"],
                    baseline_p="",logged_result=result,observed_value_literal=row["observed_settlement_value"],
                    source_pointer=pointer,source_pointer_status=pointers[pointer]["status"],
                    rank_log_line=ordinal,grade_independently_verified=False,performance_eligible=False,
                    learning_status="CONFLICT_OR_GAP" if conflicts else "SOURCE_LINKED_LITERAL_ONLY",
                    exclusion_reasons=";".join(conflicts),diagnostic_brier_p=diagnostic,
                    retrospective_literal=row["one_line_review"])
        normalized.append(record);cards[row["card_id"]].append(record)
    summaries=[]
    for card_id,group in sorted(cards.items()):
        reliable=all(r["learning_status"]=="SOURCE_LINKED_LITERAL_ONLY" for r in group)
        ranked=sorted((r for r in group if r["rank"].isdigit()),key=lambda r:int(r["rank"]))
        by_rank={int(r["rank"]):r for r in ranked}
        grades=[r["logged_result"] for r in group]
        binary=[r for r in ranked if r["logged_result"] in {"W","L"}]
        concordant=sum(a["logged_result"]=="W" and b["logged_result"]=="L" for i,a in enumerate(binary) for b in binary[i+1:]) if reliable else None
        discordant=sum(a["logged_result"]=="L" and b["logged_result"]=="W" for i,a in enumerate(binary) for b in binary[i+1:]) if reliable else None
        scores=[r["diagnostic_brier_p"] for r in group if r["diagnostic_brier_p"] is not None]
        summaries.append(dict(card_id=card_id,event=group[0]["event"],n_rank_rows=len(group),
            logged_wins=grades.count("W"),logged_losses=grades.count("L"),logged_pushes=grades.count("P"),
            rank1_logged_result=by_rank[1]["logged_result"] if reliable and 1 in by_rank else "",
            top2_logged_wins=sum(by_rank[i]["logged_result"]=="W" for i in (1,2)) if reliable and all(i in by_rank for i in (1,2)) else None,
            best_logged_winning_rank=min((int(r["rank"]) for r in ranked if r["logged_result"]=="W"),default=None) if reliable else None,
            rank_pairs_concordant=concordant,rank_pairs_discordant=discordant,
            diagnostic_mean_brier_p=sum(scores)/len(scores) if scores else None,n_diagnostic_p=len(scores),
            performance_eligible=False,status="SOURCE_LINKED_LEARNING_ONLY" if reliable else "CONFLICT_OR_GAP"))
    output.mkdir(parents=True,exist_ok=False)
    for filename,records in (("contracts.csv",normalized),("cards.csv",summaries)):
        with (output/filename).open("w",encoding="utf-8",newline="") as handle:
            writer=csv.DictWriter(handle,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
    report=dict(created_utc=datetime.now(timezone.utc).isoformat(),rank_log_sha256=sha(RANKS),
                rows=len(normalized),cards=len(cards),learning_states=dict(Counter(r["learning_status"] for r in normalized)),
                probabilities_retained=sum(r["stated_p"] is not None for r in normalized),
                diagnostic_p_rows=sum(r["diagnostic_brier_p"] is not None for r in normalized),
                performance_eligible_rows=0,source_pointers=list(pointers.values()),
                contracts_sha256=sha(output/"contracts.csv"),cards_sha256=sha(output/"cards.csv"),
                limitation="Logged grades and stated probabilities are historical literals. Brier diagnostics are neither audited source truth nor prospective predictive skill. q is never scored as a probability. No baseline or cutoff is imputed.")
    with (output/"manifest.json").open("x",encoding="utf-8") as handle:
        json.dump(report,handle,indent=2);handle.write("\n")
    return report


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,default=OUTPUT)
    args=parser.parse_args();r=build(args.output)
    print(json.dumps({k:v for k,v in r.items() if k!="source_pointers"},indent=2))

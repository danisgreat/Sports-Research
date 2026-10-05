"""Append approved-scope research addenda and reference copies, preserving prefixes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
from research.src.ledger import locked,read_records
from research.src.issue import CANONICAL_LEDGER,PART6,_custody
from research.operations.log_card import next_id,pending,research_cards

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def save(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def append(path,raw):
    before=path.read_bytes()
    with path.open('ab') as f:f.write(raw);f.flush();os.fsync(f.fileno())
    if path.read_bytes()!=before+raw:raise ValueError('Append readback failed: '+str(path))
    return dict(path=str(path),before_bytes=len(before),before_sha256=sha(before),append_bytes=len(raw),append_sha256=sha(raw),after_bytes=len(before)+len(raw),after_sha256=sha(before+raw))

if __name__=='__main__':
    text=(OUT/'settlement_addendum.md').read_text(encoding='utf-8')
    marker=b'<!-- BEGIN DIAGNOSTIC SETTLEMENT RECONCILIATION 2026-10-05 -->'
    part6_before=PART6.read_bytes()
    if marker in part6_before:raise ValueError('Already appended; inspect receipt, do not duplicate')
    if not part6_before.startswith((OUT/'originals/prediction logs/PREDICTION_LOG_COMBINED_6.md').read_bytes()):raise ValueError('Opening Part 6 prefix changed')
    mini=ROOT/'Mini logs (to be sent to actual log later)/Mini Prediction Log - P-523 onward - 2026-10-01/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md'
    downloads=Path('C:/Users/danie/Downloads/PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md')
    for target,snapshot in [(mini,OUT/'originals'/mini.relative_to(ROOT)),(downloads,OUT/'originals/downloads_mini_current.md')]:
        if target.read_bytes()!=snapshot.read_bytes():raise ValueError('Reference mini changed since opening: '+str(target))
    projection=text.replace('\n','\r\n').encode('utf-8')
    (OUT/'settlement_projection.bin').write_bytes(projection)
    grades=json.loads((OUT/'conditional_diagnostic_grades.json').read_text(encoding='utf-8'))
    imported=json.loads((OUT/'import_results.json').read_text(encoding='utf-8'))
    committed={r['card_id']:r for r in imported['records'] if r.get('record_sha256')}
    previous_audit=[json.loads(line) for line in (ROOT/'research/verification/mini_settlement_2026-10-02/diagnostic_revisions.jsonl').read_text(encoding='utf-8').splitlines()]
    recorded=datetime.now(timezone.utc).isoformat()
    previous='0'*64;revisions=[]
    for i,g in enumerate(grades,1):
        earlier=next((r['record_sha256'] for r in previous_audit if r['local_reservation']==g['card_id']),None)
        rec=dict(schema_version='canonical-research-diagnostic-revision-1',sequence=i,previous_sha256=previous,recorded_utc=recorded,canonical_id=g['card_id'],canonical_research_commit_sha256=committed[g['card_id']]['record_sha256'],original_source_sha256=sha((OUT/'originals'/('fallback_mini_source.txt' if int(g['card_id'][2:])<=531 else 'consolidated_source.txt')).read_bytes()),source_version_addenda_sha256=imported['addendum_sha256'],prior_local_diagnostic_revision_sha256=earlier,source_event_audit_sha256=sha((OUT/'source_event_audit.json').read_bytes()),source_capture_manifest_sha256=sha((OUT/'source_capture_manifest.json').read_bytes()),conditional_grades_sha256=sha((OUT/'conditional_diagnostic_grades.json').read_bytes()),addendum_sha256=sha(projection),diagnostic=g,formal_settlement='UNRESOLVED / UNKNOWN_DEFINITION / NO_AUDITED_TERMINAL_QUORUM',admission='HISTORICAL_RESEARCH_ONLY_NOT_PERFORMANCE_ELIGIBLE')
        rec['record_sha256']=sha(canonical(rec));previous=rec['record_sha256'];revisions.append(rec)
    ledger_before=CANONICAL_LEDGER.read_bytes()
    with locked(CANONICAL_LEDGER):
        records=read_records(CANONICAL_LEDGER)
        if pending(records) or next_id()!='P-538':raise ValueError('Canonical transaction state drift')
        _custody(PART6)
        part6_receipt=append(PART6,projection)
    (OUT/'diagnostic_revisions.jsonl').write_bytes(b''.join(canonical(r)+b'\n' for r in revisions))
    if CANONICAL_LEDGER.read_bytes()!=ledger_before:raise ValueError('Settlement unexpectedly changed canonical allocation ledger')
    source=(OUT/'originals/consolidated_source.txt').read_text(encoding='utf-8-sig')
    reference='\n## October 5 canonical import — retained reference copy\n\nThe original reservations have now been transactionally committed as P-527–P-531; six additional unique events are P-532–P-537. Four overlapping consolidated entries are dated addenda under P-527/P-529/P-530/P-531. This existing mini is a reference copy; Part 6 is authoritative. The stale P-516 path named by the attachment is absent, so no replacement mini is created. No archive occurs. Original observations/VERIFIED/next-ID labels below are historical source statements, superseded administratively by this dated section. Current next canonical ID: P-538.\n\n### Supplied consolidated source exhibit (historical, unchanged content)\n\n'+source+'\n\n### Canonical settlement reference copy\n\n'+text
    reference_raw=reference.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8')
    mini_receipts=[append(p,reference_raw) for p in [mini,downloads]]
    status='\n<!-- BEGIN CURRENT RESEARCH SETTLEMENT STATUS 2026-10-05 -->\n## Current research settlement status — October 5\n\nThis dated table supersedes earlier UNSETTLED/unplayed pointers for these imported research records, while preserving their original classifications. Full source variants, all row grades and eleven twelve-part retrospectives are in Part 6. Canonical IDs were allocated only for unique historical events; settlement creates no new ID. Next available ID: **P-538**.\n\n| Canonical ID | Sporting endpoint | Current status | Formal/performance status |\n|---|---|---|---|\n'
    for g in grades:status+=f"| **{g['card_id']}** | Home-away {g['score'][0]}-{g['score'][1]}; total {g['total']} | {g['status']} | UNRESOLVED operator/quorum; NOT PERFORMANCE_ELIGIBLE |\n"
    status+='\nCarryover: **P-537** first-half O/U 0.5 UNRESOLVED_PERIOD (2-0 detailed reports versus 0-0 ESPN split); corners Over 9.5 UNRESOLVED_PROVIDER_FIELD. All eleven retain UNKNOWN_DEFINITION and no three audited independent terminal lineages. Missing/unadmitted actual start remains distinct from scheduled time. NBL and later EuroLeague/NHL NO_FORECAST rows remain abstentions; MLB/WNBA late timing is unchanged. No certified settlements, live eligible forecasts or performance scores were created.\n\nAudit: `research/verification/reconciliation_2026-10-05/REPORT.md`; hash-chained research diagnostic revisions are separate from the immutable canonical allocation ledger. Current full-check failures are disclosed in the audit, not hidden by new manifests.\n<!-- END CURRENT RESEARCH SETTLEMENT STATUS 2026-10-05 -->\n'
    status_receipt=append(ROOT/'GAME_LOG_STATUS_CURRENT.md',status.replace('\n','\r\n').encode('utf-8'))
    _custody(PART6)
    save('append_receipt.json',dict(recorded_utc=recorded,part6=part6_receipt,minis=mini_receipts,status=status_receipt,ledger_unchanged_by_settlement=True,ledger_sha256=sha(ledger_before),revision_chain_tip=previous,revision_count=len(revisions),next_id=next_id(),certified=0,performance_eligible=0))
    print('Appended Part 6, both existing mini references and current status; next P-538.')

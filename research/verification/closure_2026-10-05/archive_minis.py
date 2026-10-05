"""Close reconciled reference minis without changing issued research bytes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from research.operations.log_card import next_id, pending, research_cards, retained_path, verify_projection
from research.src.ledger import read_records

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).parent
PRIOR=OUT.parent/'reconciliation_2026-10-05'
def sha(raw): return hashlib.sha256(raw).hexdigest()
def dump(name,value): (OUT/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
    part=ROOT/'prediction logs/PREDICTION_LOG_COMBINED_6.md'
    ledger=ROOT/'research/canonical_ledger.jsonl'
    before=ledger.read_bytes()
    records=read_records(ledger)
    assert not pending(records), 'recover before closure'
    following=next_id()
    cards=research_cards(records)
    assert len(cards)==15 and following=='P-538'
    for c in cards: verify_projection(c,part)
    events={e['id']:e for e in json.loads((PRIOR/'event_review.json').read_text(encoding='utf-8'))}
    revisions={r['canonical_id']:r for r in map(json.loads,(PRIOR/'diagnostic_revisions.jsonl').read_text(encoding='utf-8').splitlines())}
    old={
      'P-523':('2026-10-01T00:30:00Z',['1H Over 0.5 goals','90m Under 2.5 goals','90m Over 2.5 goals','1H Under 0.5 goals','Corners: undefined threshold'],
                'EXISTING_HISTORICAL_AUDIT_NOT_CERTIFIED; corners UNRESOLVED_LINE'),
      'P-524':('2026-10-01T09:30:00Z',['Kia +1.5','KT Wiz ML','Under 8.5 runs','Over 8.5 runs'],'UNSETTLED; last retained state IN_PROGRESS'),
      'P-525':('2026-10-01T09:00:00Z',['Carp +1.5','Over 6.5 runs','Under 6.5 runs','Dragons +1.5'],'UNSETTLED; last retained owner state Hiroshima 4-1, top seventh'),
      'P-526':('2026-10-01T09:30:00Z',['Under 11.5 runs','Samsung -0.5','Hanwha +2.5','Over 11.5 runs'],'UNSETTLED; last retained owner state 0-0, top third')}
    carry=[]
    accounting=[]
    for c in cards:
        cid=c['card_id']; event=events.get(cid)
        text=retained_path(c['projection_path']).read_text(encoding='utf-8')
        schedule_notes=[line for line in text.splitlines() if re.search('Scheduled|schedule remains',line,re.I)]
        fields=dict(canonical_id=cid,tracking_handle=c['tracking_handle'],event=c['title'],competition=c['league'],
                    event_key=c['event_key'],native_event_id=c.get('native_event_id'),
                    original_analysis_status=c['analysis_status'],performance_eligible=False,
                    canonical_pointer='prediction logs/PREDICTION_LOG_COMBINED_6.md',
                    canonical_marker='BEGIN CANONICAL RESEARCH '+cid,
                    projection_path=retained_path(c['projection_path']).relative_to(ROOT).as_posix(),
                    projection_sha256=c['projection_sha256'],source_sha256=c['source_sha256'],body_sha256=c['body_sha256'],
                    commit_sha256=c['commit_sha256'])
        if event:
            revision=revisions[cid]
            fields.update(original_scheduled_start=event['scheduled_utc'],actual_start=event.get('actual_start'),
                current_state=revision['diagnostic']['status'],unresolved_contracts_or_fields=[row['label'] for v in revision['diagnostic']['versions'] for row in v['rows']],
                unresolved_additional_rows=revision['diagnostic'].get('extra_rows',[]),
                remaining_requirement='Obtain exact original operator action/period/OT/shortened-game terms and an audited three-independent-terminal-lineage bundle for this exact event. Retain UNKNOWN_DEFINITION and formal UNRESOLVED; never grant prospective eligibility to this historical import.',
                diagnostic_revision_sha256=revision['record_sha256'] if 'record_sha256' in revision else revision.get('revision_sha256'),
                source_custody_notes=event['identity'],retrospective_pointer='research/verification/reconciliation_2026-10-05/settlement_addendum.md',
                source_capture_pointer='research/verification/reconciliation_2026-10-05/source_capture_manifest.json')
            if cid=='P-537':
                fields['remaining_requirement']+=' Resolve conflicting first-half score from a field-owner period sequence; recover the named provider’s corner definition/count and frozen corners 9.5 contract. Keep UNRESOLVED_PERIOD and UNRESOLVED_PROVIDER_FIELD.'
            if cid=='P-530': fields['remaining_requirement']+=' Preserve the duplicated supplied Over 7.5 row separately from the unsupported Under shadow alternative; no silent row repair.'
            if cid=='P-533': fields['remaining_requirement']+=' Preserve unsupported KIA ML separately from the supplied KIA +1.5 contract.'
        else:
            schedule,contracts,state=old[cid]
            fields.update(original_scheduled_start=schedule,original_schedule_notes=schedule_notes,current_state=state,
                unresolved_contracts_or_fields=contracts,
                remaining_requirement='Recover event-specific owner terminal score, period/innings/end-state, actual-start evidence, original operator action/period definitions and audited independent terminal corroboration. Perform a dated deterministic diagnostic settlement and full retrospective when exact outcome custody is available; preserve original/live probabilities and ranks. This archive operation supplies no new terminal evidence.',
                source_custody_notes='Original research source and projection verified against the canonical chain; prior logging repair and live/source notes retained at research/verification/log_repair_2026-10-01/REPORT.md. Historical imported statuses are not current finals.',
                retrospective_pointer='research/verification/settlement_2026-10-01/REPORT.md' if cid=='P-523' else None)
            if cid=='P-523': fields['remaining_requirement']+=' Corners threshold was never defined: preserve UNRESOLVED_LINE. Preserve the existing dated all-log audit and freeze/start conflict.'
        carry.append(fields)
        accounting.append({**{k:fields[k] for k in ['canonical_id','event_key','native_event_id','tracking_handle','source_sha256','body_sha256','commit_sha256']},
                           'classification':'ALREADY_CANONICAL_WITH_DIAGNOSTIC_ADDENDUM_AND_UNRESOLVED_CARRYOVER' if event else 'ALREADY_CANONICAL_REFERENCE_POINTER_WITH_CARRYOVER',
                           'new_import':False,'retrospective_sections':12 if event else 'EXISTING_AUDIT_OR_PENDING'})
    dump('carryover.json',dict(records=carry,next_id=following,never_reallocate=True))
    dump('entry_accounting.json',dict(unique_events=15,original_fallback_entries=5,consolidated_entries=10,
         overlap_versions=4,existing_reference_pointers=4,new_imports_in_this_closure=0,records=accounting,
         historical_imports_this_user_task=[c['card_id'] for c in cards[4:]],
         changed_versions_pointer='research/verification/reconciliation_2026-10-05/source_reconciliation_projection.bin'))
    lines=['# Unresolved carryover — mini closure 2026-10-05','',
           'Keep the existing IDs. This manifest preserves formal settlement gaps separately from the eleven retained conditional diagnostic outcomes and retrospectives. The four pre-existing reference cards retain their earlier state/audit; this closure does not invent new finals. Next canonical ID: **'+following+'**.','']
    for c in carry:
        lines += ['## '+c['canonical_id']+' — '+c['event'],'',
                  '- Competition / event key: '+str(c['competition'])+' / `'+c['event_key']+'`.',
                  '- Scheduled start: `'+c['original_scheduled_start']+'` (not actual-start certification).',
                  '- Current state: `'+c['current_state']+'`.',
                  '- Unresolved contracts/fields: '+', '.join(c['unresolved_contracts_or_fields'])+'.',
                  '- Exact remaining requirement: '+c['remaining_requirement'],
                  '- Canonical pointer: `'+c['canonical_pointer']+'`, marker `'+c['canonical_marker']+'`; immutable projection `'+c['projection_path']+'`.',
                  '- Original source SHA-256: `'+c['source_sha256']+'`; commit SHA-256: `'+c['commit_sha256']+'`.',
                  '- Source/custody notes: '+c['source_custody_notes'],'']
    (OUT/'carryover.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    receipt=json.loads((PRIOR/'append_receipt.json').read_text(encoding='utf-8'))
    stamp=datetime.now(timezone.utc).isoformat()
    archived=[]
    for index,mini in enumerate(receipt['minis']):
        original=Path(mini['path']); raw=original.read_bytes()
        assert sha(raw)==mini['after_sha256'] and len(raw)==mini['after_bytes']
        # Read the complete current reference; no destructive cleanup precedes this check.
        raw.decode('utf-8')
        name='PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md' if index==0 else original.name
        destination=ROOT/'archive/mini_logs/originals_2026-10-05'/name
        destination.parent.mkdir(parents=True,exist_ok=True)
        header=(f'# CLOSED / ARCHIVED MINI REFERENCE\n\nClosed UTC: {stamp}. Canonical coverage P-523–P-537 across the two references.\n'
          'Previously imported during this user task: P-527–P-537; closure imports: NONE. Already canonical reference pointers: P-523–P-526. Four overlapping versions are retained as dated addenda, not new cards.\n'
          'Eleven conditional diagnostic settlements and twelve-part retrospectives are already retained under P-527–P-537. Formal unresolved carryover: P-523–P-537, with exact fields in `research/verification/closure_2026-10-05/carryover.json`.\n'
          'Canonical authority: `prediction logs/PREDICTION_LOG_COMBINED_6.md`. Next ID returned by allocator: P-538. Method MDS-2026.10.01-v7.1; administrative control CR-2026.10.05-I1 / CONTROL_MANIFEST_2026-10-05-1.md.\n'
          f'Archive verification: PASS — original body {len(raw)} bytes / SHA-256 `{sha(raw)}`; all fifteen source/projection hashes and ledger chain read back. Full checks: `research/verification/closure_2026-10-05/REPORT.md`.\n'
          'Historical statements and queue snapshots below retain their original dates and scope. This is a closed reference copy, not an active ledger.\n\n<!-- BEGIN PRESERVED MINI BODY -->\n').encode('utf-8')
        with destination.open('xb') as handle: handle.write(header+raw)
        assert destination.read_bytes()[len(header):]==raw
        archived.append(dict(original_path=str(original),archive_path=destination.relative_to(ROOT).as_posix(),
                     body_offset=len(header),original_bytes=len(raw),original_sha256=sha(raw),archive_sha256=sha(header+raw)))
    assert ledger.read_bytes()==before
    dump('mini_archive_manifest.json',dict(closed_utc=stamp,archives=archived,canonical_range='P-523–P-537',
         next_id=following,new_imports=0,already_canonical=15,unresolved_carryover=15,
         ledger_sha256=sha(before),archive_convention_evidence='Existing historical register paths archive/mini_logs/originals_2026-09-23/',
         part6_before_closure_sha256=sha(part.read_bytes()),part6_before_closure_bytes=len(part.read_bytes())))
    # Replace redundant live reference bodies only after successful archive readback.
    for item in archived:
        pointer=('# CLOSED mini reference\n\nArchived with its original bytes at `'+item['archive_path']+'`.\n'
                 'Canonical ledger: `prediction logs/PREDICTION_LOG_COMBINED_6.md`. Next canonical ID: P-538; use the transactional allocator for current state.\n'
                 'Unresolved carryover: `research/verification/closure_2026-10-05/carryover.md`.\n'
                 'Archive receipt: `research/verification/closure_2026-10-05/mini_archive_manifest.json`.\n')
        Path(item['original_path']).write_text(pointer,encoding='utf-8')
    append=('\r\n## Mini-reference closure — 2026-10-05\r\n\r\n'
            'Fifteen canonical events P-523–P-537 were reconciled by ledger/source/body/event identity. No additional IDs were allocated during closure; next-id returned P-538. The eleven P-527–P-537 diagnostic settlements and full retrospectives above remain unchanged. Four overlapping source versions remain dated addenda.\r\n\r\n'
            'Closed byte-preserved references: `archive/mini_logs/originals_2026-10-05/`. Every formal unresolved record is retained in `research/verification/closure_2026-10-05/carryover.json` and `carryover.md`, including the four earlier reference cards and P-537 period/provider conflicts. No diagnostic grade was promoted to certified performance.\r\n\r\n'
            'Accounting and archive hashes: `research/verification/closure_2026-10-05/entry_accounting.json` and `mini_archive_manifest.json`. Administrative repair control: CR-2026.10.05-I1 / CONTROL_MANIFEST_2026-10-05-1.md; original issue/control/source receipts remain historical.\r\n').encode('utf-8')
    with part.open('ab') as handle:handle.write(append)
    dump('closure_append.json',dict(bytes=len(append),sha256=sha(append),after_bytes=part.stat().st_size,
                                  after_sha256=sha(part.read_bytes()),ledger_unchanged=True))
    print(json.dumps(dict(archived=len(archived),already_canonical=15,new_imports=0,next_id=following)))

if __name__=='__main__':main()

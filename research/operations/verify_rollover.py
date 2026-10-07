"""Read back the October 8 import, dated reviews and empty Part-7 rollover."""
from pathlib import Path
import argparse
import hashlib,json,re
from research.operations.log_card import next_id,pending,research_cards,research_addenda,verify_projection
from research.operations.diagnostic_rank import metrics
from research.operations.settlement_register import selected
from research.src.issue import CANONICAL_LEDGER,PART6,_custody
from research.src.ledger import read_records
from research.src.combined_log import active_log,custody
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research/verification/mini_rollover_2026-10-08'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def load(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
def need(value,message):
    if not value:raise ValueError(message)


def run(local_bodies=False):
    opening=load('opening.json');raw=PART6.read_bytes();records=read_records(CANONICAL_LEDGER)
    need(not pending(records),'Pending canonical transaction')
    for item in opening['files']:
        if item['path'].startswith('prediction logs/') or item['path']=='research/canonical_ledger.jsonl':
            body=(ROOT/item['path']).read_bytes()
            if item['path'].endswith('_6.md') or item['path']=='research/canonical_ledger.jsonl':body=body[:item['bytes']]
            need(len(body)==item['bytes'] and sha(body)==item['sha256'],'Original prefix changed: '+item['path'])
    original=(OUT/'provided_mini.original.bin').read_bytes()
    need(sha(original)==opening['original_mini_sha256'] and len(original)==opening['original_mini_bytes'],'Provided mini changed')
    imported=load('import_receipt.json');rollover=load('rollover_receipt.json')
    cards=research_cards(records);addenda=research_addenda(records)
    new=[c for c in cards if c['card_id'] in imported['imported_ids']]
    need([c['card_id'] for c in new]==['P-'+str(n) for n in range(538,550)],'Import IDs missing/duplicated/renumbered')
    for card in cards+addenda:verify_projection(card,active_log(ROOT))
    for card in new:
        from research.operations.log_card import retained_path
        need(retained_path(card['source_path']).read_bytes() in original,'Imported forecast is not an exact original substring')
    need(len([a for a in addenda if a['card_id'] in imported['imported_ids']])==12,'Missing dated retrospective')
    need(sha(raw[:rollover['previous_log_prefix_bytes']])==rollover['previous_log_prefix_sha256'],'Rollover prefix changed')
    first=rollover['previous_log_prefix_bytes']
    need(sha(raw[first:first+rollover['rollover_append_bytes']])==rollover['rollover_append_sha256'],'Rollover append changed')
    # This dated receipt proves the rollover itself was empty; later real appends
    # are checked by their own ledger hashes rather than a permanent P-550 claim.
    need(rollover['ledger_sha256_before']==rollover['ledger_sha256_after'] and not rollover['id_consumed_by_rollover'],'Empty rollover consumed an ID')
    need(sha(CANONICAL_LEDGER.read_bytes()[:imported['ledger_before_bytes']])==imported['ledger_before_sha256'],'Original ledger prefix changed')
    _custody(PART6);custody(active_log(ROOT))
    reviews=load('event_reviews.json');summary=load('summary.json')
    need(len(reviews)==12 and sum(len(r['rows']) for r in reviews)==49,'Frozen ranked slate coverage')
    for review in reviews:
        need(review['rank_metrics']==metrics([r['grade'] for r in review['rows']]),'Rank metric changed')
        need(set(review['retrospective'])=={'R'+str(n) for n in range(1,13)} and review['performance_eligible'] is False,'Review incomplete or promoted')
    need((summary['win'],summary['loss'],summary['unknown_definition'])==(26,19,4),'Disposition counts changed')
    register=selected(ROOT)['manifest'];old=json.loads((ROOT/'research/verification/all_log_resolution_2026-10-05/carryover_v3.json').read_text(encoding='utf-8'))
    current={r['canonical_id']:r for r in register['records']}
    for r in old['records']:need(current[r['canonical_id']]==r,'Historical carryover changed')
    need(register['event_count']==65,'Current carryover count changed')
    proposals=load('improvement_proposals.json')
    need(proposals['source_review_sha256']==sha((OUT/'event_reviews.json').read_bytes()),'Proposal source changed')
    register=json.loads((ROOT/'research/improvement_register.json').read_text(encoding='utf-8'))
    need(any(r['sha256']==sha((OUT/'improvement_proposals.json').read_bytes()) for r in register['pending_retrospective_review_registers']),'Pending hypothesis register unbound')
    need(all(r['status']=='PROPOSED_NOT_TESTED' and r['performance_eligible'] is False for r in proposals['records']),'Untested hypothesis promoted')
    following=next_id();queue=(ROOT/'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8-sig').split('<!-- END CURRENT RESEARCH QUEUE -->')[0]
    need(f'Next canonical ID: {following}' in queue and active_log(ROOT).relative_to(ROOT).as_posix() in queue,'Status destination/ID stale')
    checked=0
    if local_bodies:
        for receipt in load('source_capture_manifest.json'):
            body=Path(receipt['body_path']).read_bytes()
            need(len(body)==receipt['bytes'] and sha(body)==receipt['sha256'],'Terminal body changed: '+receipt['key'])
            checked+=1
    return dict(passed=True,imported_events=12,retrospective_sections=144,ranked_rows=49,win=26,loss=19,unknown_definition=4,
                active_log=active_log(ROOT).relative_to(ROOT).as_posix(),next_id=following,current_carryovers=65,
                legacy_part6_custody='PASS',original_forecast_substrings='PASS',local_terminal_bodies_checked=checked,
                source_certification='NOT_ESTABLISHED; collection independence is UNKNOWN')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--local-body-custody',action='store_true');args=parser.parse_args()
    try:result=run(args.local_body_custody)
    except (OSError,ValueError,KeyError,TypeError,IndexError) as exc:result=dict(passed=False,error=f'{type(exc).__name__}: {exc}')
    print(json.dumps(result,indent=2));raise SystemExit(not result['passed'])

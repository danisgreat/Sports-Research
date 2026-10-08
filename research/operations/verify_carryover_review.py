"""Verify the supplied P-126/P-549 review exhibit, without recounting grades."""
from pathlib import Path
import argparse
import json
from research.operations.review_packet import sha, require, validate_packet
from research.operations.log_card import next_id, research_cards, pending
from research.operations.settlement_register import selected
from research.src.combined_log import active_log, custody
from research.src.issue import CANONICAL_LEDGER
from research.src.ledger import read_records

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'research/verification/carryover_review_2026-10-08'


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def run(local_bodies=False):
    opening = load('opening.json')
    historical = json.loads((ROOT/opening['selected_register']['manifest_path']).read_text(encoding='utf-8'))
    require(sha((ROOT/opening['selected_register']['manifest_path']).read_bytes()) == opening['selected_register']['manifest_sha256'], 'Previous register changed')
    records = read_records(CANONICAL_LEDGER)
    require(not pending(records), 'Pending canonical transaction')
    packet = validate_packet(OUT/'inputs', historical, {c['card_id'] for c in research_cards(records)})
    require(packet['reviews'] == load('event_reviews.json'), 'Parsed reviews or mapping changed')
    projection = (OUT/'settlement_projection.bin').read_bytes()
    append = load('append_receipt.json')
    destination = ROOT/load('publication_mapping.json')['active_log']
    body, _ = custody(destination)
    start = append['before_bytes']
    require(sha(projection) == append['projection_sha256'] and len(projection) == append['projection_bytes'], 'Projection receipt differs')
    require(body.count(projection) == 1 and body[start:start + len(projection)] == projection, 'Exhibit absent, repeated or altered')
    require(sha(body[:start]) == append['before_sha256'] and sha(body[:start + len(projection)]) == append['after_sha256'], 'Append prefix/readback changed')
    settled = (OUT/'inputs/P126_P549_PREDICTION_MINI_SETTLED_P-126_P-549.md').read_bytes()
    require(settled[packet['original_prefix_bytes']:] in projection, 'Supplied supplement not retained exactly')
    require(b'## P-550' not in projection, 'Excluded local card was imported')
    for item in opening['files']:
        raw = (ROOT/item['path']).read_bytes()
        if item['path'] == load('publication_mapping.json')['active_log']:
            raw = raw[:item['bytes']]
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'], 'Earlier combined-log bytes changed: ' + item['path'])
    ledger = CANONICAL_LEDGER.read_bytes()
    require(sha(ledger[:opening['ledger_bytes']]) == opening['ledger_sha256'], 'Original ledger changed')
    require(append['ledger_before_sha256'] == append['ledger_after_sha256'] == opening['ledger_sha256']
            and append['next_id_before'] == append['next_id_after'] == opening['next_id']
            and append['new_ids'] == [] and append['new_formal_grades'] == 0, 'Audit consumed an ID or grade')
    carry = load('carryover.json')
    require(carry['records'] == historical['records'], 'Retrospective overlay replaced historical states')
    require(carry['event_count'] == 65 and len(carry['review_addenda']['records']) == 65, 'Current review coverage differs')
    for name, digest in carry['review_addenda']['artifact_sha256'].items():
        require(sha((OUT/name).read_bytes()) == digest, 'Bound review artifact changed: ' + name)
    require(selected(ROOT)['manifest'] == carry, 'Current selected carryover differs')
    proposals = load('improvement_proposals.json')
    require(proposals['source_review_sha256'] == sha((OUT/'event_reviews.json').read_bytes()), 'Proposal source changed')
    require(len(proposals['records']) == len(packet['reviews']), 'Proposal coverage differs')
    for proposal, review in zip(proposals['records'], packet['reviews']):
        literal = review['retrospective']['R11']
        require(proposal['canonical_id'] == review['id'] and proposal['hypothesis_and_acceptance'] == literal
                and proposal['source_text_sha256'] == sha(literal.encode('utf-8'))
                and proposal['status'] == 'PROPOSED_NOT_TESTED' and proposal['performance_eligible'] is False, 'Untested hypothesis changed or promoted')
    registry = json.loads((ROOT/'research/improvement_register.json').read_text(encoding='utf-8'))
    require(any(r['sha256'] == sha((OUT/'improvement_proposals.json').read_bytes()) for r in registry['pending_retrospective_review_registers']), 'Review register missing')
    current_next = next_id()
    queue = (ROOT/'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8-sig').split('<!-- END CURRENT RESEARCH QUEUE -->')[0]
    require(selected(ROOT)['manifest_path'] in queue and f'Next canonical ID: {current_next}' in queue, 'Current queue stale')
    checked = 0
    captures = load('source_capture_manifest.json')['records']
    if local_bodies:
        for receipt in captures:
            if 'body_path' not in receipt:
                continue
            raw = Path(receipt['body_path']).read_bytes()
            require(len(raw) == receipt['bytes'] and sha(raw) == receipt['sha256'], 'Local fresh source body changed')
            checked += 1
    require(all(r['field_admission'] == 'NOT_ADMITTED' and r['collection_independence'] == 'UNKNOWN' for r in captures), 'Source admitted without field/lineage audit')
    return dict(passed=True, reviewed_records=65, retrospective_sections=780, new_events=0, new_formal_grades=0,
                ids_consumed=0, next_id=current_next, active_log=active_log(ROOT).relative_to(ROOT).as_posix(),
                reserved_references=5, excluded_local_event='P-550', supplied_files_verified=len(packet['receipts']),
                optional_not_supplied=packet['missing_optional_artifacts'], fresh_source_urls=len(captures),
                fresh_local_bodies_checked=checked, source_certification='NOT_ESTABLISHED', states_replaced=0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local-body-custody', action='store_true')
    args = parser.parse_args()
    try:
        result = run(args.local_body_custody)
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        result = dict(passed=False, error=f'{type(exc).__name__}: {exc}')
    print(json.dumps(result, indent=2))
    raise SystemExit(not result['passed'])

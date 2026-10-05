"""Read-only current-document, mini-archive and diagnostic reconciliation checks."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from research.operations.log_card import next_id, pending, research_cards, verify_projection
from research.src.eligibility import digest
from research.src.issue import CANONICAL_LEDGER, PART6
from research.src.ledger import read_records

ROOT = PART6.parents[1]
CLOSURE = ROOT/'research/verification/closure_2026-10-05'
REVIEW = ROOT/'research/verification/reconciliation_2026-10-05'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run():
    records = read_records(CANONICAL_LEDGER)
    require(not pending(records), 'Pending canonical research transaction')
    cards = research_cards(records)
    card_map = {c['card_id']: c for c in cards}
    for card in cards:
        verify_projection(card, PART6)
    following = next_id()
    accounting = read_json(CLOSURE/'entry_accounting.json')
    carries = read_json(CLOSURE/'carryover.json')['records']
    archive = read_json(CLOSURE/'mini_archive_manifest.json')
    ids = {r['canonical_id'] for r in accounting['records']}
    require(len(ids) == accounting['unique_events'] == 15, 'Closure event accounting changed')
    require(ids == {r['canonical_id'] for r in carries}, 'Closure carryover coverage changed')
    for record in accounting['records']:
        card = card_map[record['canonical_id']]
        for key in ['event_key', 'tracking_handle', 'source_sha256', 'body_sha256', 'commit_sha256']:
            require(record[key] == card[key], 'Closure canonical mapping changed: '+key)
        require(record['new_import'] is False, 'Closure duplicated historical imports')
    for carry in carries:
        require(carry['performance_eligible'] is False, 'Historical carryover promoted')
        for key in ['event', 'competition', 'original_scheduled_start', 'current_state',
                    'unresolved_contracts_or_fields', 'remaining_requirement', 'source_custody_notes']:
            require(bool(carry[key]), 'Incomplete carryover: '+carry['canonical_id']+':'+key)
    raw = PART6.read_bytes()
    require(sha(raw[:archive['part6_before_closure_bytes']]) == archive['part6_before_closure_sha256'],
            'Pre-closure Part 6 bytes changed')
    for item in archive['archives']:
        body = (ROOT/item['archive_path']).read_bytes()
        require(sha(body) == item['archive_sha256'], 'Closed mini archive changed')
        original = body[item['body_offset']:]
        require(len(original) == item['original_bytes'] and sha(original) == item['original_sha256'],
                'Closed mini original body changed')
    revisions = [json.loads(line) for line in (REVIEW/'diagnostic_revisions.jsonl').read_text().splitlines()]
    previous = '0'*64
    for index, record in enumerate(revisions, 1):
        require(record['sequence'] == index and record['previous_sha256'] == previous,
                'Diagnostic revision chain order changed')
        require(digest({k: v for k, v in record.items() if k != 'record_sha256'}) == record['record_sha256'],
                'Diagnostic revision hash changed')
        card = card_map[record['canonical_id']]
        require(record['canonical_research_commit_sha256'] == card['commit_sha256']
                and record['original_source_sha256'] == card['source_sha256'], 'Diagnostic core join changed')
        require(record['diagnostic']['performance_eligible'] is False, 'Diagnostic promoted')
        for field, filename in [('conditional_grades_sha256', 'conditional_diagnostic_grades.json'),
                                ('source_capture_manifest_sha256', 'source_capture_manifest.json'),
                                ('source_event_audit_sha256', 'source_event_audit.json')]:
            require(sha((REVIEW/filename).read_bytes()) == record[field], 'Diagnostic evidence changed: '+filename)
        previous = record['record_sha256']
    projection = (REVIEW/'settlement_projection.bin').read_bytes()
    require(len(revisions) == 11 and raw.count(projection) == 1, 'Diagnostic projection absent or duplicated')
    require(len(re.findall(rb'(?m)^#### (?:[1-9]|1[0-2])\.', projection)) == 132,
            'Twelve-part retrospectives incomplete')
    improvements = read_json(ROOT/'research/improvement_register.json')
    events = read_json(REVIEW/'event_review.json')
    require(improvements['source_review_sha256'] == sha((REVIEW/'event_review.json').read_bytes()),
            'Retrospective proposal source changed')
    proposals = {r['canonical_id']: r for r in improvements['records']}
    require(len(proposals) == len(improvements['records']) == len(events) == 11, 'Missing/duplicate proposal')
    for event in events:
        proposal = proposals[event['id']]
        require(proposal['hypothesis_and_acceptance'] == event['hypothesis']
                and proposal['source_text_sha256'] == sha(event['hypothesis'].encode('utf-8')),
                'Retrospective suggestion changed')
        require(proposal['status'] == 'PROPOSED_NOT_TESTED' and proposal['performance_eligible'] is False,
                'Untested retrospective proposal promoted')
    method = (ROOT/'METHOD.md').read_text(encoding='utf-8-sig')
    control = re.search(r'Control revision \*\*([^*]+)\*\*', method)[1]
    freeze = re.search(r'Active freeze: \[([^\]]+)\]', method)[1]
    for filename in ['README.md', 'CURRENT_RULES.md']:
        require(control in (ROOT/filename).read_text(encoding='utf-8-sig'), 'Stale current control: '+filename)
    status = (ROOT/'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8-sig')
    queue = status.split('<!-- END CURRENT RESEARCH QUEUE -->', 1)[0]
    require(f'Next canonical ID: {following}' in queue and freeze in queue, 'Stale current queue/freeze')
    normalized = (ROOT/freeze).read_text(encoding='utf-8-sig').replace('\r\n', '\n').replace('\r', '\n').replace('\n', '\r\n').encode('utf-8')
    require(sha(normalized) in queue, 'Stale current freeze hash')
    references = list(ROOT.glob('RULES_*.md')) + [ROOT/name for name in [
        'LEAGUE_RULES_SOCCER.md', 'LEAGUE_RULES_CRICKET.md', 'BASE_RATES_REGISTER.md',
        'PROBABILITY_TOOLKIT.md', 'SKILL_BASELINE_LEDGER.md', 'MARKET_BENCHMARK_LEDGER.md',
        'SOURCES.md', 'VALIDATION_EVIDENCE.md', 'LEARNING_REGISTER.md', 'LEARNINGS_INDEX.md',
        'P518_P522_RECONCILIATION.md', 'PIPELINE_IMPLEMENTATION_2026-09-29.md',
        'IMPLEMENTATION_2026-10-01.md', 'VERIFICATION_RECEIPT_2026-09-28.md']]
    for path in references:
        text = path.read_text(encoding='utf-8-sig')
        require('> **Current authority (October 5):**' in '\n'.join(text.splitlines()[:10]),
                'Missing current authority: '+path.name)
        require('No unregistered league/family can receive an issued numerical forecast.' not in text,
                'Obsolete requested-research blocker: '+path.name)
    report = ROOT/'research/verification/implementation_2026-10-05/REPORT.md'
    require(report.is_file(), 'Current implementation evidence missing')
    return dict(observed_utc=datetime.now(timezone.utc).isoformat(), passed=True,
                canonical_cards=len(cards), next_id=following, closed_original_archives=len(archive['archives']),
                historical_carryovers=len(carries), diagnostic_revisions=len(revisions),
                retrospective_sections=132, untested_proposals=len(proposals),
                reference_documents=len(references), control=control, freeze=freeze,
                limitation='Readback verifies retained mechanics, mappings and missingness; it supplies no new sporting facts or prospective certification.')


if __name__ == '__main__':
    try:
        result = run()
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        result = dict(passed=False, error=f'{type(exc).__name__}: {exc}')
    print(json.dumps(result, indent=2))
    raise SystemExit(not result['passed'])

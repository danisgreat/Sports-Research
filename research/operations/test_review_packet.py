import pytest
import json
import shutil
from pathlib import Path
from research.operations.review_packet import parse_reviews, reference_class
from research.operations.review_packet import append_audit
from research.operations.review_packet import validate_packet


def review(card_id='P-126'):
    return '### LOCAL SETTLEMENT REVIEW - ' + card_id + ' - Fixture\n\n' + '\n\n'.join(
        f'**R{n} - Section.** Literal evidence {n}.' for n in range(1, 13)) + '\n'


def test_reviews_keep_literal_parts_and_exclude_metric_appendix():
    parsed = parse_reviews(review() + '## HISTORICAL RANK DIAGNOSTICS\nPrior cohort only.', ['P-126'])
    assert parsed[0]['retrospective']['R11'] == 'Literal evidence 11.'
    assert parsed[0]['performance_eligible'] is False
    assert 'Prior cohort' not in parsed[0]['retrospective']['R12']


@pytest.mark.parametrize('text,ids,excluded,message', [
    (review() + review(), ['P-126'], [], 'Duplicate'),
    (review().replace('**R7 - Section.**', '**R8 - Section.**'), ['P-126'], [], 'Missing'),
    (review().replace('Literal evidence 7.', ''), ['P-126'], [], 'Empty'),
    (review('P-550'), ['P-550'], ['P-550'], 'Excluded'),
    (review(), ['P-126', 'P-136'], [], 'coverage'),
])
def test_invalid_review_cannot_be_imported(text, ids, excluded, message):
    with pytest.raises(ValueError, match=message):
        parse_reviews(text, ids, excluded)


def test_reserved_references_cannot_be_classified_as_committed():
    assert reference_class('P-518', {'P-518'}) == 'RESERVED_DOCUMENTARY_REFERENCE_NOT_COMMITTED'
    assert reference_class('P-549', {'P-549'}) == 'COMMITTED_RESEARCH_CARD_NOT_CERTIFIED'
    assert reference_class('P-126', {'P-549'}) == 'HISTORICAL_DOCUMENTARY_REFERENCE_NOT_CERTIFIED'


def test_audit_is_idempotent_and_recovers_partial_append(tmp_path):
    log, ledger, store = tmp_path/'log.md', tmp_path/'ledger.jsonl', tmp_path/'receipt'
    log.write_bytes(b'Immutable header\n'); ledger.write_bytes(b'Original ledger\n')
    projection = b'\n### LOCAL SETTLEMENT REVIEW - P-126 - Fixture\nSource retained.\n'
    with pytest.raises(RuntimeError, match='interrupted'):
        append_audit(projection, log, store, ledger, lambda: 'P-550', fault='partial')
    result = append_audit(projection, log, store, ledger, lambda: 'P-550')
    assert result['next_id_before'] == result['next_id_after'] == 'P-550'
    assert ledger.read_bytes() == b'Original ledger\n'
    assert log.read_bytes() == b'Immutable header\n' + projection
    assert append_audit(projection, log, store, ledger, lambda: 'P-550')['duplicate']


def test_pending_audit_rejects_unrelated_append(tmp_path):
    log, ledger, store = tmp_path/'log.md', tmp_path/'ledger.jsonl', tmp_path/'receipt'
    log.write_bytes(b'Original log\n')
    with pytest.raises(RuntimeError):
        append_audit(b'Retrospective audit\n', log, store, ledger, lambda: 'P-550', fault='partial')
    with log.open('ab') as handle:
        handle.write(b'Unrelated edit')
    with pytest.raises(ValueError, match='Unrelated'):
        append_audit(b'Retrospective audit\n', log, store, ledger, lambda: 'P-550')


@pytest.mark.parametrize('projection', [b'## P-550 - Excluded local card\n', b'<!-- BEGIN CANONICAL RESEARCH P-550 example -->\n'])
def test_audit_cannot_import_a_card_by_accident(tmp_path, projection):
    with pytest.raises(ValueError, match='heading'):
        append_audit(projection, tmp_path/'log.md', tmp_path/'receipt', tmp_path/'ledger.jsonl', lambda: 'P-550')


@pytest.mark.parametrize('filename', ['P126_P549_ORIGINAL_MINI_FROZEN.md', 'P126_P549_RECONCILIATION_INVENTORY.csv'])
def test_changed_frozen_source_or_inventory_fails_custody(tmp_path, filename):
    root = Path(__file__).resolve().parents[2]
    inputs = root/'research/verification/carryover_review_2026-10-08/inputs'
    retained = tmp_path/'inputs'
    shutil.copytree(inputs, retained)
    with (retained/filename).open('ab') as handle:
        handle.write(b'Unrelated mutation\n')
    baseline = json.loads((root/'research/verification/mini_rollover_2026-10-08/carryover.json').read_text(encoding='utf-8'))
    with pytest.raises(ValueError, match='hash/size mismatch'):
        validate_packet(retained, baseline, set())

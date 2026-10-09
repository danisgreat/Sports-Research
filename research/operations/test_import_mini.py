import hashlib
import json
from pathlib import Path

import pytest

from research.operations import import_mini, log_card, mini_log
from research.src.issue import PART6, _custody
from research.src.ledger import read_records

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / 'research/prompts/examples'


def renumber(raw: bytes, mapping):
    text = raw.decode('utf-8')
    for old, new in mapping:
        text = text.replace(old, new)
    return text.encode('utf-8')


def reseal(frozen: Path, settled: Path):
    """Record the (renumbered) frozen file's SHA-256 in the settlement header, as prompt 3 requires."""
    raw = settled.read_bytes()
    start = raw.index(b'| Frozen original SHA-256 | `') + len(b'| Frozen original SHA-256 | `')
    settled.write_bytes(raw[:start] + hashlib.sha256(frozen.read_bytes()).hexdigest().encode() + raw[start + 64:])


MAP = [('P-902', 'P-525'), ('P-901', 'P-524'), ('P-900', 'P-523'), ('P-899', 'P-522')]


@pytest.fixture
def repo(tmp_path, monkeypatch):
    logs = tmp_path / 'prediction logs'; logs.mkdir()
    store = tmp_path / 'research'; store.mkdir()
    raw, _ = _custody(PART6)
    marker = b'<!-- END ORIGINAL P518 SOURCE BYTES -->'
    legacy = logs / 'PREDICTION_LOG_COMBINED_6.md'; legacy.write_bytes(raw[:raw.index(marker) + len(marker)] + b'\r\n')
    active = logs / 'PREDICTION_LOG_COMBINED_7.md'
    header = b'# Combined Prediction Log 7\r\n\r\nACTIVE FOR NEW CANONICAL RESEARCH\r\n'
    active.write_bytes(header)
    (store / 'current_combined_log.json').write_text(json.dumps(dict(
        active_log='prediction logs/' + active.name, header_bytes=len(header), header_sha256=hashlib.sha256(header).hexdigest())))
    reconciliation = tmp_path / 'reserved.md'; reconciliation.write_text('reserved P-518 P-519 P-520 P-521 P-522')
    monkeypatch.setattr(log_card, 'ROOT', tmp_path); monkeypatch.setattr(log_card, 'PART6', legacy)
    options = dict(part6=active, reconciliation=reconciliation, ledger=store / 'ledger.jsonl', store=store / 'issued_research')
    minis = tmp_path / 'minis'; minis.mkdir()
    frozen = minis / 'FROZEN.md'; frozen.write_bytes(renumber((EXAMPLES / 'EXAMPLE_ACTIVE_MINI.md').read_bytes(), MAP))
    settled = minis / 'SETTLED.md'; settled.write_bytes(renumber((EXAMPLES / 'EXAMPLE_SETTLED_MINI.md').read_bytes(), MAP))
    reseal(frozen, settled)
    return dict(active=active, legacy=legacy, options=options, frozen=frozen, settled=settled, out=tmp_path / 'out')


def test_plan_then_apply_imports_cards_and_addenda_with_local_ids(repo):
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert result['blocking'] == [] and result['new_cards'] == ['P-523', 'P-524']
    assert result['next_id_before'] == 'P-523' and result['expected_next_id_after'] == 'P-525'
    legacy_before = repo['legacy'].read_bytes()
    applied = import_mini.apply(repo['frozen'], repo['settled'], repo['out'], repo['options'])
    assert applied['next_id_after'] == 'P-525'
    kinds = [(t['id'], t['type']) for t in applied['transactions']]
    assert kinds == [('P-523', 'CARD'), ('P-524', 'CARD'), ('P-523', 'CARD_ADDENDUM'),
                     ('P-523', 'SETTLEMENT_ADDENDUM'), ('P-524', 'SETTLEMENT_ADDENDUM')]
    log = repo['active'].read_bytes()
    assert log.count(b'BEGIN CANONICAL RESEARCH P-523') == 1 and log.count(b'BEGIN RESEARCH ADDENDUM P-524') == 1
    assert log.count(b'BEGIN RESEARCH ADDENDUM P-523') == 2
    assert log.index(b'### Addendum \xc2\xb7 P-523') < log.index(b'### Settlement \xc2\xb7 P-523')
    frozen = repo['frozen'].read_bytes()
    card = next(b for b in mini_log.blocks(frozen) if b['id'] == 'P-523')['body']
    assert card.replace(b'\n', b'\r\n') in log  # exact card bytes, projected with CRLF by the logger
    assert repo['legacy'].read_bytes() == legacy_before
    for name in ('CANONICAL_IMPORT_REPORT.md', 'CANONICAL_ID_MAPPING.csv', 'CANONICAL_IMPORT_MANIFEST.json',
                 'DUPLICATE_RECONCILIATION.md', 'UNRESOLVED_POST_IMPORT.md', 'settlement_table.json'):
        assert (repo['out'] / name).exists()
    assert (repo['out'] / 'inputs' / 'FROZEN.md').read_bytes() == frozen


def test_reapply_is_idempotent_and_consumes_no_id(repo):
    import_mini.apply(repo['frozen'], repo['settled'], repo['out'], repo['options'])
    ledger = read_records(repo['options']['ledger'])
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert {i['classification'] for i in result['items']} == {'ALREADY_IMPORTED_EXACT'}
    assert {i['addendum'] for i in result['items']} == {'ALREADY_COMMITTED'}
    assert [a['status'] for a in result['addenda']] == ['ALREADY_COMMITTED']
    again = import_mini.apply(repo['frozen'], repo['settled'], repo['out'], repo['options'])
    assert again['transactions'] == [] and again['next_id_after'] == 'P-525'
    assert read_records(repo['options']['ledger']) == ledger


def test_collision_blocks_before_any_write(repo):
    other = repo['frozen'].parent / 'other.txt'; other.write_text('another event')
    log_card.commit(dict(event_key='OTHER:2026:X:2026-10-10', title='Other event', tracking_handle='OTHER',
                         analysis_status='UNCALIBRATED_ANALYST_SCENARIO', body='Other body', source_path=str(other)),
                    **repo['options'])
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert 'IDENTITY_CONFLICT' in result['blocking']
    before = repo['active'].read_bytes()
    with pytest.raises(ValueError, match='blocked'):
        import_mini.apply(repo['frozen'], repo['settled'], repo['out'], repo['options'])
    assert repo['active'].read_bytes() == before


def test_gap_in_local_ids_is_a_collision(repo):
    shifted = [('P-902', 'P-527'), ('P-901', 'P-526'), ('P-900', 'P-525'), ('P-899', 'P-524')]
    frozen = repo['frozen'].parent / 'F2.md'
    frozen.write_bytes(renumber((EXAMPLES / 'EXAMPLE_ACTIVE_MINI.md').read_bytes(), shifted))
    settled = repo['frozen'].parent / 'S2.md'
    settled.write_bytes(renumber((EXAMPLES / 'EXAMPLE_SETTLED_MINI.md').read_bytes(), shifted))
    reseal(frozen, settled)
    result, _ = import_mini.plan(frozen, settled, repo['options'])
    assert result['blocking'] == ['ID_COLLISION']
    assert 'allocator would assign P-523' in result['items'][0]['reason']
    assert [a['status'] for a in result['addenda']] == ['PARENT_BLOCKED']


def test_invalid_settlement_blocks(repo):
    bad = repo['settled'].read_bytes().replace(b'**Knowability.**', b'**Knowable?**', 1)
    repo['settled'].write_bytes(bad)
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert result['blocking'] == ['VALIDATION_FAILED'] and result['validation_errors']


def test_pending_event_card_is_imported_without_addendum(repo):
    text = repo['settled'].read_text(encoding='utf-8')
    start = text.index('<!-- BEGIN SETTLEMENT P-524 -->'); end = text.index('<!-- END SETTLEMENT P-524 -->')
    text = text[:start] + ('<!-- BEGIN SETTLEMENT P-524 -->\n### Settlement · P-524 · Westbay Gulls vs Eastvale Pines\n\n'
                           '**Card state:** `PENDING_EVENT`\nPostponed.\n') + text[end:]
    repo['settled'].write_text(text, encoding='utf-8')
    applied = import_mini.apply(repo['frozen'], repo['settled'], repo['out'], repo['options'])
    assert [(t['id'], t['type']) for t in applied['transactions']] == [
        ('P-523', 'CARD'), ('P-524', 'CARD'), ('P-523', 'CARD_ADDENDUM'), ('P-523', 'SETTLEMENT_ADDENDUM')]
    assert 'P-524: PENDING_EVENT' in (repo['out'] / 'UNRESOLVED_POST_IMPORT.md').read_text(encoding='utf-8')


def test_addendum_without_canonical_parent_blocks(repo):
    block = ('<!-- BEGIN ADDENDUM P-400 -->\n### Addendum · P-400 · 2026-10-10T10:00:00+11:00\n\n'
             'Late news.\n<!-- END ADDENDUM P-400 -->\n\n').encode('utf-8')
    for path in (repo['frozen'], repo['settled']):
        raw = path.read_bytes()
        path.write_bytes(raw.replace(b'# RUNNING FOOTER', block + b'# RUNNING FOOTER', 1))
    reseal(repo['frozen'], repo['settled'])
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert result['validation_errors'] == []
    assert 'SOURCE_CUSTODY_UNRESOLVED' in result['blocking']
    assert result['addenda'][-1]['id'] == 'P-400' and result['addenda'][-1]['status'] == 'SOURCE_CUSTODY_UNRESOLVED'


def test_settlement_manifest_hashes_are_checked(repo):
    manifest = repo['settled'].parent / 'SETTLEMENT_MANIFEST.json'
    good = {'original': {'sha256': hashlib.sha256(repo['frozen'].read_bytes()).hexdigest()},
            'settled': {'sha256': 'NOT_COMPUTED'}, 'pending_event_ids': []}
    manifest.write_text(json.dumps(good))
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert result['blocking'] == [] and any('NOT_COMPUTED' in w for w in result['validation_warnings'])
    manifest.write_text(json.dumps({**good, 'settled': {'sha256': '0' * 64}}))
    result, _ = import_mini.plan(repo['frozen'], repo['settled'], repo['options'])
    assert result['blocking'] == ['VALIDATION_FAILED'] and any('does not match' in e for e in result['validation_errors'])
    manifest.write_text(json.dumps(good))
    import_mini.apply(repo['frozen'], repo['settled'], repo['out'], repo['options'])
    assert (repo['out'] / 'inputs' / 'SETTLEMENT_MANIFEST.json').read_bytes() == manifest.read_bytes()

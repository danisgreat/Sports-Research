import hashlib
import json
from pathlib import Path

import pytest

from research.operations import verify_custody as custody


def receipt(root, name, body=b'evidence', *, stored=True):
    path = root/'research/data/source_receipts'/f'{name}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    body_path = root/'bodies'/name
    body_path.parent.mkdir(parents=True, exist_ok=True)
    if stored:
        body_path.write_bytes(body)
    value = dict(body_path=body_path.relative_to(root).as_posix(),
                 response_sha256=hashlib.sha256(body).hexdigest(),
                 retrieved_utc='2026-10-01T00:00:00Z', response_bytes=len(body))
    path.write_text(json.dumps(value), encoding='utf-8')
    return path, value, body_path


def test_all_missing_and_changed_bodies_are_reported(tmp_path):
    receipt(tmp_path, 'valid')
    receipt(tmp_path, 'missing-a', stored=False)
    receipt(tmp_path, 'missing-b', stored=False)
    _, _, changed = receipt(tmp_path, 'changed')
    changed.write_bytes(b'tampered')
    rows = custody.audit_sources(tmp_path/'research/data/source_receipts', tmp_path)
    assert len(rows) == 4
    assert sum(row['verified'] for row in rows) == 1
    assert sorted(row['error_type'] for row in rows if not row['verified']) == [
        'FileNotFoundError', 'FileNotFoundError', 'ValueError']


def test_imported_schema_preserves_receipt_and_checks_original_bytes(tmp_path):
    _, value, body = receipt(tmp_path, 'imported')
    imported = dict(content_sha256=value['response_sha256'],
                    stored_snapshot_path=value['body_path'], retrieved_utc=value['retrieved_utc'])
    original = imported.copy()
    assert custody.compatible_body(imported, tmp_path) == b'evidence'
    assert imported == original
    body.write_bytes(b'changed')
    with pytest.raises(ValueError, match='hash'):
        custody.compatible_body(imported, tmp_path)


def test_declared_body_length_is_verified(tmp_path):
    _, value, _ = receipt(tmp_path, 'length')
    value['response_bytes'] += 1
    with pytest.raises(ValueError, match='length'):
        custody.compatible_body(value, tmp_path)


def test_invalid_json_and_non_object_receipts_do_not_hide_other_failures(tmp_path):
    path, _, _ = receipt(tmp_path, 'valid')
    (path.parent/'bad-syntax.json').write_text('{', encoding='utf-8')
    (path.parent/'bad-schema.json').write_text('[]', encoding='utf-8')
    rows = custody.audit_sources(path.parent, tmp_path)
    assert len(rows) == 3 and sum(row['verified'] for row in rows) == 1
    assert len([row for row in rows if not row['verified']]) == 2
    with pytest.raises(ValueError, match='JSON object'):
        custody.compatible_body([], tmp_path)


def test_full_run_stays_invalid_and_restores_acceptance_adapter(tmp_path, monkeypatch):
    receipt(tmp_path, 'valid')
    receipt(tmp_path, 'missing-a', stored=False)
    receipt(tmp_path, 'missing-b', stored=False)
    monkeypatch.setattr(custody, 'PART6', tmp_path/'prediction logs/part6.md')
    monkeypatch.setattr(custody, 'research_cards', lambda records: [])
    monkeypatch.setattr(custody, 'read_records', lambda path: [])
    monkeypatch.setattr(custody, 'next_id', lambda: 'P-538')
    original = custody.acceptance.verified_body

    def acceptance_run():
        for path in (tmp_path/'research/data/source_receipts').glob('*.json'):
            custody.acceptance.verified_body(json.loads(path.read_text()), tmp_path)
        return dict(valid=True, checks={'other_checks_reached': True}, issues=[], limitation='Test fixture.')

    monkeypatch.setattr(custody.acceptance, 'run', acceptance_run)
    result = custody.run()
    assert result['valid'] is False
    assert result['checks']['other_checks_reached']
    assert result['checks']['source_receipt_bodies_verified'] == 1
    assert len(result['source_body_failures']) == 2
    assert custody.acceptance.verified_body is original

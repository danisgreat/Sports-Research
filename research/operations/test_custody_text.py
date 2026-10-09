"""Platform-independent custody bytes and pinned register snapshots (GOV-01, GOV-02)."""
import hashlib
import json
from pathlib import Path

import pytest

from research.operations import settlement_register
from research.src import custody_text

ROOT = Path(__file__).resolve().parents[2]


def test_to_crlf_is_idempotent_and_leaves_lone_carriage_returns():
    assert custody_text.to_crlf(b'a\nb\r\nc\n') == b'a\r\nb\r\nc\r\n'
    assert custody_text.to_crlf(custody_text.to_crlf(b'a\nb\n')) == b'a\r\nb\r\n'
    assert custody_text.to_crlf(b'a\rb') == b'a\rb'


def test_custody_bytes_match_on_lf_and_crlf_checkouts(tmp_path):
    (tmp_path / 'prediction logs').mkdir()
    name = 'prediction logs/PREDICTION_LOG_COMBINED_3.md'
    lf, crlf = b'one\ntwo\n', b'one\r\ntwo\r\n'
    (tmp_path / name).write_bytes(lf)
    from_lf = custody_text.custody_bytes(tmp_path / name, tmp_path)
    (tmp_path / name).write_bytes(crlf)
    assert from_lf == custody_text.custody_bytes(tmp_path / name, tmp_path) == crlf
    # an exact-bytes (-text) file is returned as stored, never rewritten
    other = tmp_path / 'prediction logs/PREDICTION_LOG_COMBINED_6.md'
    other.write_bytes(lf)
    assert custody_text.custody_bytes(other, tmp_path) == lf


def test_files_normalised_for_custody_are_not_pinned_as_exact_bytes_in_gitattributes():
    attributes = (ROOT / '.gitattributes').read_text(encoding='utf-8')
    for relative in custody_text.CRLF_CUSTODY:
        assert (ROOT / relative).exists(), relative
        assert f'"{relative}" -text' not in attributes and not (relative.startswith('research/') and 'research/** -text' in attributes), relative


def test_windows_recorded_paths_resolve_anywhere():
    assert custody_text.windows_path('research\\data\\raw\\x.body').as_posix() == 'research/data/raw/x.body'
    assert custody_text.windows_path('research/data/raw/x.body').as_posix() == 'research/data/raw/x.body'


def write_register(root: Path, name: str, kind: str, ids, open_count=0):
    folder = root / 'research/verification' / name
    folder.mkdir(parents=True, exist_ok=True)
    if kind == 'carryover':
        records = [{'canonical_id': i, 'event': 'e', 'competition': 'c', 'original_scheduled_start': 's', 'current_state': 'x',
                    'unresolved_contracts_or_fields': 'u', 'remaining_requirement': 'r', 'canonical_pointer': 'p', 'source_custody_notes': 'n',
                    'performance_eligible': False} for i in ids]
        manifest = {'event_count': len(records), 'records': records, 'documentary_repairs': 0}
    else:
        records = [{'canonical_id': i, 'event': 'e', 'state': 'FINAL_SETTLED', 'card_outcome': 'TOP2_ALL_WON', 'performance_eligible': False} for i in ids]
        manifest = {'event_count': len(records), 'records': records, 'open_sporting_settlements': open_count}
    raw = (json.dumps(manifest, indent=1) + '\n').encode()
    (folder / 'register.json').write_bytes(raw)
    return f'research/verification/{name}/register.json', hashlib.sha256(raw).hexdigest()


def test_pointer_history_pins_dated_snapshots_and_survives_a_move(tmp_path):
    old_path, old_sha = write_register(tmp_path, 'old', 'carryover', ['P-1', 'P-2'])
    pointer = tmp_path / 'research/current_settlement_register.json'
    pointer.write_text(json.dumps({'schema_version': 1, 'manifest_path': old_path, 'manifest_sha256': old_sha, 'report_path': 'r'}), encoding='utf-8')
    assert settlement_register.selected(tmp_path)['kind'] == 'carryover' and settlement_register.pinned(tmp_path, old_path)['event_count'] == 2
    new_path, new_sha = write_register(tmp_path, 'new', 'settled', ['P-1', 'P-2', 'P-3'])
    pointer.write_text(json.dumps({'schema_version': 2, 'kind': 'settled', 'manifest_path': new_path, 'manifest_sha256': new_sha, 'report_path': 'r',
                                   'history': [{'manifest_path': old_path, 'manifest_sha256': old_sha, 'kind': 'carryover'}]}), encoding='utf-8')
    current = settlement_register.selected(tmp_path)
    assert current['kind'] == 'settled' and current['manifest']['event_count'] == 3
    assert settlement_register.in_lineage(tmp_path, old_path) and settlement_register.in_lineage(tmp_path, new_path)
    assert settlement_register.pinned(tmp_path, old_path)['event_count'] == 2             # the dated verifier still gets its own snapshot
    assert not settlement_register.in_lineage(tmp_path, 'research/verification/other/register.json')
    with pytest.raises(ValueError, match='not in the settlement-register lineage'):
        settlement_register.pinned(tmp_path, 'research/verification/other/register.json')


def test_a_changed_snapshot_or_history_entry_is_refused(tmp_path):
    old_path, old_sha = write_register(tmp_path, 'old', 'carryover', ['P-1'])
    new_path, new_sha = write_register(tmp_path, 'new', 'settled', ['P-1'])
    pointer = tmp_path / 'research/current_settlement_register.json'
    pointer.write_text(json.dumps({'schema_version': 2, 'kind': 'settled', 'manifest_path': new_path, 'manifest_sha256': new_sha,
                                   'history': [{'manifest_path': old_path, 'manifest_sha256': old_sha, 'kind': 'carryover'}]}), encoding='utf-8')
    settlement_register.selected(tmp_path)
    (tmp_path / old_path).write_bytes((tmp_path / old_path).read_bytes() + b' ')
    with pytest.raises(ValueError, match='changed'):
        settlement_register.selected(tmp_path)                                         # a superseded snapshot may not drift
    with pytest.raises(ValueError, match='changed'):
        settlement_register.pinned(tmp_path, old_path)


def test_settled_registers_must_state_open_count_and_never_certify(tmp_path):
    path, sha = write_register(tmp_path, 'new', 'settled', ['P-1'])
    manifest = json.loads((tmp_path / path).read_text())
    manifest['records'][0]['performance_eligible'] = True
    raw = json.dumps(manifest).encode()
    (tmp_path / path).write_bytes(raw)
    (tmp_path / 'research/current_settlement_register.json').write_text(json.dumps({'schema_version': 2, 'kind': 'settled', 'manifest_path': path,
                                                                                    'manifest_sha256': hashlib.sha256(raw).hexdigest()}), encoding='utf-8')
    with pytest.raises(ValueError, match='admission'):
        settlement_register.selected(tmp_path)


def test_the_repository_pointer_selects_the_final_settlement_and_pins_the_old_register():
    current = settlement_register.selected(ROOT)
    assert current['kind'] == 'settled' and current['manifest']['event_count'] == 72 and current['manifest']['open_sporting_settlements'] == 0
    assert settlement_register.pinned(ROOT, 'research/verification/carryover_review_2026-10-08/carryover.json')['event_count'] == 65


def test_dated_verifiers_pass_after_the_pointer_moved():
    from research.operations import verify_carryover_review, verify_rollover
    assert verify_rollover.run()['passed'] and verify_carryover_review.run()['passed']

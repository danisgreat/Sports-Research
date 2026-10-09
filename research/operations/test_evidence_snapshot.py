"""Tests for evidence snapshots (SRC-03) and the capture schedule (SRC-02)."""
import hashlib
import re
from datetime import datetime
from pathlib import Path

import pytest

from research.operations import capture_schedule, evidence_snapshot as ev

EXAMPLE = Path(__file__).resolve().parents[1] / 'prompts/examples/EXAMPLE_ACTIVE_MINI.md'


def example_with_real_snapshots(root):
    """The example mini with every snapshot token replaced by one that resolves to a stored receipt."""
    text = EXAMPLE.read_text(encoding='utf-8')
    tokens = []

    def swap(match):
        out = []
        for token in match[1].split('; '):
            receipt = ev.store('evidence', f'P-900-page{len(tokens)}', f'page {len(tokens)}'.encode(), 'https://example.org/lineup',
                               token.split('@')[1], 'lineup', root=root)
            tokens.append(receipt['token'])
            out.append(receipt['token'])
        return match[0].replace(match[1], '; '.join(out))

    text = re.sub(r'(?m)^- \*\*Evidence snapshots:\*\*\s*`(sha256:[^`]+)`\s*$', swap, text)
    return text.encode('utf-8'), tokens


def test_store_is_exclusive_and_returns_the_card_token(tmp_path):
    r = ev.store('evidence', 'P-900-goalie', b'<html>goalie confirmed</html>', 'https://example.org/g', '2026-10-10T08:41:00+11:00', root=tmp_path)
    assert r['token'] == f"sha256:{hashlib.sha256(b'<html>goalie confirmed</html>').hexdigest()}@2026-10-10T08:41:00+11:00"
    assert ev.TOKEN.match(r['token'])
    with pytest.raises(FileExistsError):
        ev.store('evidence', 'P-900-goalie', b'<html>goalie confirmed</html>', 'https://example.org/g', '2026-10-10T08:41:00+11:00', root=tmp_path)
    for kwargs in ({'url': 'http://x'}, {'body': b''}, {'key': 'bad key'}, {'kind': 'other'}, {'retrieved': '2026-10-10T08:41:00'}):
        args = dict(kind='evidence', key='k', body=b'x', url='https://x', retrieved='2026-10-10T08:41:00+00:00', root=tmp_path)
        args.update(kwargs)
        with pytest.raises(ev.EvidenceError):
            ev.store(**args)
    assert ev.verify_store(tmp_path) == []


def test_tampered_body_and_missing_body_are_reported(tmp_path):
    r = ev.store('evidence', 'k1', b'one', 'https://x', '2026-10-10T08:00:00+00:00', root=tmp_path)
    body = next(tmp_path.glob('evidence/k1_*.body'))
    body.write_bytes(b'changed')
    assert any('no longer matches' in p for p in ev.verify_store(tmp_path))
    body.unlink()
    assert ev.verify_store(tmp_path) == []
    assert any('missing' in p for p in ev.verify_store(tmp_path, require_bodies=True))
    assert r['retained'] == 'BODY'


def test_verify_card_resolves_every_token(tmp_path):
    raw, tokens = example_with_real_snapshots(tmp_path)
    ok = ev.verify_card_text(raw, tmp_path)
    assert ok['passed'] and ok['checked_tokens'] == len(tokens)
    # a token with no receipt
    forged = raw.replace(tokens[0].encode(), ('sha256:' + '0' * 64 + '@' + tokens[0].split('@')[1]).encode())
    assert any('no stored receipt' in p for p in ev.verify_card_text(forged, tmp_path)['problems'])
    # NONE is allowed (the validator warns)
    none = re.sub(rb'(- \*\*Evidence snapshots:\*\* `)[^`]+(`)', rb'\1NONE\2', raw)
    assert ev.verify_card_text(none, tmp_path)['checked_tokens'] == 0


def test_snapshot_after_research_completed_is_rejected(tmp_path):
    text = EXAMPLE.read_text(encoding='utf-8')
    late = ev.store('evidence', 'late', b'late page', 'https://x', '2026-10-10T10:00:00+11:00', root=tmp_path)
    line = re.search(r'(?m)^- \*\*Evidence snapshots:\*\*\s*`(sha256:[^`]+)`\s*$', text)
    raw = text.replace(line[1], late['token']).encode('utf-8')
    assert any('after the research was completed' in p for p in ev.verify_card_text(raw, tmp_path)['problems'])


def test_capture_schedule_states(tmp_path):
    raw = EXAMPLE.read_bytes()
    due_text = re.search(r'Capture due:\*\* `([^`]+)`', raw.decode()).group(1)
    due = datetime.fromisoformat(due_text)
    before = due.replace(day=due.day - 1)
    assert capture_schedule.schedule(raw, before, tmp_path)[0]['state'] == 'PENDING'
    assert capture_schedule.schedule(raw, due.replace(day=due.day + 1), tmp_path)[0]['state'] == 'OVERDUE'
    ev.store('capture', 'P-900-final', b'final box', 'https://example.org/box', '2026-10-11T09:00:00+11:00', root=tmp_path)
    assert capture_schedule.schedule(raw, due.replace(day=due.day + 1), tmp_path)[0]['state'] == 'DONE'


def test_settlement_sla_deadline_and_carryover_cap():
    from research.operations import settlement_sla as sla
    raw = EXAMPLE.read_bytes()
    start = datetime.fromisoformat(re.search(r'Scheduled start:\*\* `([^`]+)`', raw.decode()).group(1))
    inside = sla.evaluate(raw, start.replace(day=start.day + 2))
    assert inside['passed'] and inside['cards'][0]['state'] == 'DUE'
    late = sla.evaluate(raw, start.replace(day=start.day + 5))
    assert not late['passed'] and late['cards'][0]['state'] == 'BREACHED' and 'P-900' in late['problems'][0]
    assert sla.allowance('Cricket (Test)') == 12 and sla.allowance('Ice hockey') == 4 and sla.allowance('Curling') == 6
    many = b'\n'.join(b'<!-- BEGIN CARRYOVER P-%d -->\n### Carryover \xc2\xb7 P-%d \xc2\xb7 x\n<!-- END CARRYOVER P-%d -->' % (i, i, i) for i in range(100, 107))
    assert sla.evaluate(raw + b'\n' + many, start)['open_carryover'] == 7 and not sla.evaluate(raw + b'\n' + many, start)['passed']

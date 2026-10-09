import hashlib
import json

import pytest

from research.operations import log_card, rollover
from research.src.combined_log import active_log, custody
from research.src.issue import PART6, _custody
from research.src.ledger import read_records

HEAD = 'a' * 40


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
    entry = {'header_bytes': len(header), 'header_sha256': hashlib.sha256(header).hexdigest()}
    (store / 'current_combined_log.json').write_text(json.dumps(dict(
        active_log='prediction logs/' + active.name, log_headers={'prediction logs/' + active.name: entry}, **entry)))
    (tmp_path / 'METHOD.md').write_text('Method **MDS-TEST**. Control revision **CR-TEST**. Scoring **SCV-TEST**. '
                                        'Active freeze: [CONTROL_MANIFEST_2026-01-01-1.md](CONTROL_MANIFEST_2026-01-01-1.md).')
    (tmp_path / '.gitattributes').write_text('"prediction logs/PREDICTION_LOG_COMBINED_7.md" -text whitespace=cr-at-eol\n')
    reconciliation = tmp_path / 'reserved.md'; reconciliation.write_text('reserved P-518 P-519 P-520 P-521 P-522')
    monkeypatch.setattr(log_card, 'ROOT', tmp_path); monkeypatch.setattr(log_card, 'PART6', legacy)
    ledger = store / 'ledger.jsonl'
    kwargs = dict(reconciliation=reconciliation, ledger=ledger, store=store / 'issued_research')

    def card(n):
        source = tmp_path / f'source{n}.txt'; source.write_text(f'Frozen source {n}')
        return dict(event_key=f'TEST:2026:{n}:2026-10-10', title=f'Test event {n}', tracking_handle=f'TEST-{n}',
                    analysis_status='UNCALIBRATED_ANALYST_SCENARIO', body=f'Body {n}', source_path=str(source))
    log_card.commit(card(1), part6=active, **kwargs)
    return dict(root=tmp_path, active=active, legacy=legacy, ledger=ledger, reconciliation=reconciliation,
                kwargs=kwargs, card=card)


def test_rollover_preserves_ids_custody_and_routes_new_cards(repo):
    root = repo['root']
    p = rollover.plan(root, repo['reconciliation'], repo['ledger'])
    assert (p['part'], p['new_part'], p['next_id'], p['cards_in_active']) == (7, 8, 'P-524', 1)
    old_before = repo['active'].read_bytes(); legacy_before = repo['legacy'].read_bytes()
    ledger_before = repo['ledger'].read_bytes()
    receipt = rollover.apply(HEAD, root, repo['reconciliation'], repo['ledger'], receipt_dir=root / 'receipt')
    new = root / 'prediction logs/PREDICTION_LOG_COMBINED_8.md'
    assert receipt['next_before'] == receipt['next_after'] == 'P-524' and not receipt['id_consumed_by_rollover']
    assert repo['ledger'].read_bytes() == ledger_before
    assert repo['active'].read_bytes().startswith(old_before) and repo['legacy'].read_bytes() == legacy_before
    assert active_log(root).resolve() == new.resolve() and new.read_bytes().count(b'# Combined Prediction Log 8') == 1
    assert b'Next available canonical ID: P-524' in new.read_bytes()
    assert '"prediction logs/PREDICTION_LOG_COMBINED_8.md" -text' in (root / '.gitattributes').read_text()
    assert 'PREDICTION_LOG_COMBINED_8.md' in (root / 'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8')
    custody(new); custody(repo['active'])
    result = log_card.commit(repo['card'](2), **repo['kwargs'])
    assert result['card_id'] == 'P-524'
    assert new.read_bytes().count(b'BEGIN CANONICAL RESEARCH P-524') == 1
    assert b'BEGIN CANONICAL RESEARCH P-524' not in repo['active'].read_bytes()
    for item in log_card.research_cards(read_records(repo['ledger'])):
        log_card.verify_projection(item, new)
    revision = dict(card_id='P-523', body='Dated settlement after rollover', source_path=repo['card'](1)['source_path'])
    assert log_card.addendum(revision, **repo['kwargs'])['card_id'] == 'P-523'
    assert log_card.next_id(None, repo['reconciliation'], repo['ledger']) == 'P-525'


def test_rollover_refuses_pending_and_existing_target(repo):
    with pytest.raises(RuntimeError):
        log_card.commit(repo['card'](3), fault='prepared', **repo['kwargs'])
    with pytest.raises(ValueError):
        rollover.apply(HEAD, repo['root'], repo['reconciliation'], repo['ledger'])
    log_card.recover(ledger=repo['ledger'])
    (repo['root'] / 'prediction logs/PREDICTION_LOG_COMBINED_8.md').write_bytes(b'existing')
    with pytest.raises(ValueError, match='already exists'):
        rollover.apply(HEAD, repo['root'], repo['reconciliation'], repo['ledger'])
    with pytest.raises(ValueError, match='main-head'):
        rollover.apply('not-a-sha', repo['root'], repo['reconciliation'], repo['ledger'])


def test_tampered_new_header_fails_custody(repo):
    rollover.apply(HEAD, repo['root'], repo['reconciliation'], repo['ledger'], receipt_dir=repo['root'] / 'r')
    new = repo['root'] / 'prediction logs/PREDICTION_LOG_COMBINED_8.md'
    new.write_bytes(new.read_bytes().replace(b'ACTIVE FOR NEW', b'ACTIVE FOR OLD', 1))
    with pytest.raises(ValueError, match='header'):
        custody(new)

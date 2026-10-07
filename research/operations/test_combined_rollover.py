import hashlib
import json
import pytest
from research.operations import log_card
from research.src.combined_log import custody
from research.src.issue import PART6, _custody
from research.src.ledger import read_records


@pytest.fixture
def rolled(tmp_path, monkeypatch):
    logs = tmp_path/'prediction logs'; logs.mkdir()
    store = tmp_path/'research'; store.mkdir()
    raw, _ = _custody(PART6)
    end = raw.index(b'<!-- END ORIGINAL P518 SOURCE BYTES -->') + len(b'<!-- END ORIGINAL P518 SOURCE BYTES -->')
    legacy = logs/'PREDICTION_LOG_COMBINED_6.md'; legacy.write_bytes(raw[:end]+b'\r\n')
    active = logs/'PREDICTION_LOG_COMBINED_7.md'
    header = b'# Combined Prediction Log 7\r\n\r\nACTIVE FOR NEW CANONICAL RESEARCH\r\n'
    active.write_bytes(header)
    (store/'current_combined_log.json').write_text(json.dumps(dict(active_log='prediction logs/'+active.name,
        header_bytes=len(header),header_sha256=hashlib.sha256(header).hexdigest())))
    reconciliation = tmp_path/'reserved.md'; reconciliation.write_text('reserved P-518 P-519 P-520 P-521 P-522')
    source = tmp_path/'forecast.txt'; source.write_text('Frozen fixture source')
    card = dict(event_key='TEST:1',title='Test only',tracking_handle='TEST',analysis_status='UNCALIBRATED_QUALITATIVE',
                body='No production fixture',source_path=str(source))
    monkeypatch.setattr(log_card,'ROOT',tmp_path); monkeypatch.setattr(log_card,'PART6',legacy)
    options = dict(reconciliation=reconciliation,ledger=store/'ledger.jsonl',store=store/'issued_research')
    return active, legacy, card, options


def test_empty_rollover_append_duplicate_and_status(rolled):
    active, legacy, card, options = rolled
    old = legacy.read_bytes()
    assert log_card.next_id(legacy,options['reconciliation'],options['ledger']) == 'P-523'
    assert log_card.next_id(None,options['reconciliation'],options['ledger']) == 'P-523'
    assert read_records(options['ledger']) == []
    assert log_card.commit(card,**options)['card_id'] == 'P-523'
    assert b'BEGIN CANONICAL RESEARCH P-523' in active.read_bytes()
    assert legacy.read_bytes() == old
    assert log_card.commit(card,**options)['duplicate']
    assert log_card.next_id(None,options['reconciliation'],options['ledger']) == 'P-524'
    status = active.parents[1]/'GAME_LOG_STATUS_CURRENT.md'
    assert active.name in status.read_text(encoding='utf-8')
    with pytest.raises(ValueError,match='different text'):
        log_card.commit({**card,'body':'correction needs addendum'},**options)
    revision = dict(card_id='P-523',body='Dated correction',source_path=card['source_path'])
    assert log_card.addendum(revision,**options)['card_id'] == 'P-523'
    assert log_card.addendum(revision,**options)['duplicate']
    assert log_card.next_id(None,options['reconciliation'],options['ledger']) == 'P-524'
    assert active.read_bytes().count(b'BEGIN CANONICAL RESEARCH P-523') == 1


@pytest.mark.parametrize('fault',['prepared','partial'])
def test_new_part_pending_recovery(rolled,fault):
    active, legacy, card, options = rolled
    with pytest.raises(RuntimeError): log_card.commit(card,fault=fault,**options)
    with pytest.raises(ValueError,match='pending'): log_card.next_id(None,options['reconciliation'],options['ledger'])
    log_card.recover(ledger=options['ledger'])
    assert log_card.recover(ledger=options['ledger']) is None
    assert active.read_bytes().count(b'BEGIN CANONICAL RESEARCH P-523') == 1
    assert log_card.commit(card,**options)['duplicate']


def test_both_legacy_and_active_header_custody(rolled):
    active, legacy, card, options = rolled
    custody(active)
    original = legacy.read_bytes(); legacy.write_bytes(original.replace(b'BEGIN ORIGINAL',b'BAD ORIGINAL',1))
    with pytest.raises(ValueError,match='markers'): custody(active)
    legacy.write_bytes(original)
    active.write_bytes(b'tampered header')
    with pytest.raises(ValueError,match='header'): custody(active)


def test_certified_adapter_uses_generic_custody_without_mutating_legacy(rolled):
    from research.operations import canonical_issue
    from research.src import issue
    active,legacy,card,options=rolled
    old_custody=issue._custody;old_next=issue.next_card_id
    adapted=canonical_issue._adapter()
    assert adapted._custody(active)[0] == active.read_bytes()
    assert canonical_issue.next_card_id(active,options['reconciliation'],options['ledger']) == 'P-523'
    log_card.commit(card,**options)
    assert canonical_issue.next_card_id(active,options['reconciliation'],options['ledger']) == 'P-524'
    assert issue._custody is old_custody and issue.next_card_id is old_next

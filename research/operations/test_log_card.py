from pathlib import Path
import pytest
from research.operations.log_card import commit, recover, next_id, research_cards
from research.src.ledger import read_records
from research.src.issue import PART6, _custody

@pytest.fixture
def workspace(tmp_path):
    raw, _ = _custody(PART6)
    end = raw.index(b'<!-- END ORIGINAL P518 SOURCE BYTES -->')+len(b'<!-- END ORIGINAL P518 SOURCE BYTES -->')
    part = tmp_path/'part6.md'; part.write_bytes(raw[:end]+b'\r\n')
    reconciliation = tmp_path/'reserved.md'
    reconciliation.write_text('reserved P-518 P-519 P-520 P-521 P-522')
    source = tmp_path/'source.txt'; source.write_bytes(b'original\r\nforecast\n')
    card = dict(event_key='KBO:2026:game1', title='Away @ Home', tracking_handle='TMP-1',
                analysis_status='UNCALIBRATED_QUALITATIVE', source_path=str(source),
                body='Rank 1: supplied contract. No retrospective.')
    options = dict(part6=part, reconciliation=reconciliation, ledger=tmp_path/'ledger.jsonl', store=tmp_path/'cores')
    return card, options, part.read_bytes()

def test_canonical_id_and_idempotent_reimport(workspace):
    card, options, before = workspace
    a = commit(card, **options); b = commit(card, **options)
    assert a['card_id'] == b['card_id'] == 'P-523' and b['duplicate']
    assert options['part6'].read_bytes().startswith(before)
    assert len(read_records(options['ledger'])) == 2
    assert next_id(options['part6'], options['reconciliation'], options['ledger']) == 'P-524'
    changed = {**card, 'body':'Changed probabilities'}
    with pytest.raises(ValueError, match='different text'): commit(changed, **options)

@pytest.mark.parametrize('fault', ['prepared','partial'])
def test_interruption_recovery_exactly_once(workspace, fault):
    card, options, before = workspace
    with pytest.raises(RuntimeError, match='simulated'): commit(card, fault=fault, **options)
    with pytest.raises(ValueError, match='pending'): commit({**card,'event_key':'other'}, **options)
    recover(part6=options['part6'], ledger=options['ledger'])
    assert recover(part6=options['part6'], ledger=options['ledger']) is None
    assert commit(card, **options)['duplicate']
    assert len(research_cards(read_records(options['ledger']))) == 1
    assert options['part6'].read_bytes().startswith(before)

def test_refuse_unrelated_append_during_recovery(workspace):
    card, options, before = workspace
    with pytest.raises(RuntimeError): commit(card, fault='prepared', **options)
    with options['part6'].open('ab') as handle: handle.write(b'unrelated work')
    raw = options['part6'].read_bytes()
    with pytest.raises(ValueError, match='unrelated'): recover(part6=options['part6'], ledger=options['ledger'])
    assert options['part6'].read_bytes() == raw

def test_detect_changed_original_and_projection(workspace):
    card, options, before = workspace
    commit(card, **options)
    stored = research_cards(read_records(options['ledger']))[0]
    Path(stored['source_path']).write_bytes(b'tampered')
    with pytest.raises(ValueError, match='original'): next_id(options['part6'], options['reconciliation'], options['ledger'])

def test_no_extra_heading_ids(workspace):
    card, options, before = workspace
    with pytest.raises(ValueError, match='nested'): commit({**card,'body':'## P-999 fake'}, **options)
    assert options['part6'].read_bytes() == before

def test_automatic_current_register_preserves_history(workspace,monkeypatch):
    from research.operations import log_card
    card,options,before=workspace
    monkeypatch.setattr(log_card,'PART6',options['part6'])
    monkeypatch.setattr(log_card,'ROOT',options['part6'].parent)
    status=options['part6'].parent/'GAME_LOG_STATUS_CURRENT.md'
    status.write_bytes(b'Historical bytes\r\n')
    commit(card,**options)
    assert 'Next canonical ID: P-524' in status.read_text(encoding='utf-8')
    assert status.read_bytes().endswith(b'Historical bytes\r\n')
    commit({**card,'event_key':'KBO:2026:game2','tracking_handle':'TMP-2'},**options)
    assert 'Next canonical ID: P-525' in status.read_text(encoding='utf-8')
    assert status.read_bytes().count(b'BEGIN CURRENT RESEARCH QUEUE')==1
    assert status.read_text(encoding='utf-8').count('## Historical status snapshots')==1
    commit(card,**options)
    assert status.read_text(encoding='utf-8').count('## Historical status snapshots')==1

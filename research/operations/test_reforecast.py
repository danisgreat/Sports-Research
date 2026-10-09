"""Re-forecast trigger (PRD-06): decisions, addendum text, and acceptance in a simulated P-274 / P-531 style change."""
from pathlib import Path

import pytest

from research.operations import mini_log, reforecast

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = (ROOT / 'research/prompts/examples/EXAMPLE_ACTIVE_MINI.md').read_bytes()
CARD, START = '2026-10-10T09:15:00+11:00', '2026-10-10T11:00:00+11:00'


@pytest.mark.parametrize('kind,when,expected,why', [
    ('STARTER', '2026-10-10T10:00:00+11:00', True, 'starting pitcher'),
    ('GOALIE', '2026-10-10T10:00:00+11:00', True, 'goalie'),
    ('QB', '2026-10-10T10:00:00+11:00', True, 'quarterback'),
    ('STARTER', '2026-10-10T08:00:00+11:00', False, 'already public'),
    ('STARTER', '2026-10-10T11:30:00+11:00', False, 'after the event started'),
])
def test_key_role_changes_trigger_only_inside_the_window(kind, when, expected, why):
    result = reforecast.decide(kind, CARD, START, when)
    assert result['reforecast'] is expected and why in result['reason']


def test_lineup_changes_need_the_threshold():
    below = reforecast.decide('LINEUP', CARD, START, '2026-10-10T10:00:00+11:00', starters_changed=1, minutes_share_changed=0.10)
    assert below['reforecast'] is False and 'below threshold' in below['reason']
    assert reforecast.decide('LINEUP', CARD, START, '2026-10-10T10:00:00+11:00', starters_changed=2)['reforecast'] is True
    assert reforecast.decide('LINEUP', CARD, START, '2026-10-10T10:00:00+11:00', minutes_share_changed=0.25)['reforecast'] is True
    with pytest.raises(ValueError):
        reforecast.decide('INJURY', CARD, START, '2026-10-10T10:00:00+11:00')
    with pytest.raises(ValueError):
        reforecast.decide('GOALIE', CARD, START, 'ten past ten')


def test_a_simulated_goalie_change_produces_a_valid_addendum_and_leaves_the_card_untouched(tmp_path):
    decision = reforecast.decide('GOALIE', CARD, START, '2026-10-10T10:12:00+11:00')
    assert decision['reforecast'] is True
    block = reforecast.addendum_block('P-900', 'GOALIE', '2026-10-10T10:12:00+11:00', 'team update 10:12',
                                      'Northfield start their backup goalie; λ_away rises to 2.95.',
                                      [{'proposition': 'Total goals Under 7.5 — full game incl. OT/SO', 'p_reforecast': 0.742},
                                       {'proposition': 'Northfield Owls +1.5 — full game incl. OT/SO', 'p_reforecast': 0.655}],
                                      '2026-10-10T10:20:00+11:00')
    assert block.startswith('<!-- BEGIN ADDENDUM P-900 -->') and 'p_reforecast' in block
    source = tmp_path / 'mini.md'
    # build a mini that has no earlier addendum for P-900 so we can add this one
    text = ACTIVE.decode('utf-8')
    start = text.index('<!-- BEGIN ADDENDUM P-900 -->')
    end = text.index('<!-- END ADDENDUM P-900 -->') + len('<!-- END ADDENDUM P-900 -->\n\n')
    source.write_text(text[:start] + text[end:], encoding='utf-8', newline='')
    before = source.read_bytes()
    addendum_file = tmp_path / 'addendum.md'
    addendum_file.write_text(block, encoding='utf-8', newline='')
    report = mini_log.add_addendum(source, addendum_file)
    assert report['errors'] == [] and [a['id'] for a in report['addenda']] == ['P-900']
    after = source.read_bytes()
    card_start = before.index(b'<!-- BEGIN CARD P-900 -->')
    card_end = before.index(b'<!-- END CARD P-900 -->')
    assert after[card_start:card_end] == before[card_start:card_end]                  # the original card bytes are unchanged


def test_bad_rows_are_rejected():
    with pytest.raises(ValueError):
        reforecast.addendum_block('P-1', 'STARTER', '2026-10-10T10:00:00+11:00', 's', 'd', [], '2026-10-10T10:10:00+11:00')
    with pytest.raises(ValueError):
        reforecast.addendum_block('P-1', 'STARTER', '2026-10-10T10:00:00+11:00', 's', 'd', [{'proposition': 'x', 'p_reforecast': 1.2}], '2026-10-10T10:10:00+11:00')

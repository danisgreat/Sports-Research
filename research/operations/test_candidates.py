"""Rule P4 tooling: the card JSON carries the ladder, four tagged rows, joint failure and the gate (PRD-04)."""
import json

import pytest

from research.operations import card_validator, candidates

HOCKEY = {'sport': 'ice_hockey', 'league': 'NHL', 'context': {'home_xg': 3.1, 'away_xg': 2.7}, 'names': ['Southport Bears', 'Northfield Owls'],
          'supplied': [{'type': 'total', 'side': 'over', 'line': 6.5, 'label': 'Over 6.5 (supplied)'},
                       {'type': 'moneyline', 'side': 'home', 'label': 'Southport Bears moneyline (supplied)'}]}


def test_card_json_has_the_ladder_the_four_rows_and_their_tags():
    out = candidates.run(HOCKEY)
    assert len(out['picks']) == 4 and [p['rank'] for p in out['picks']] == [1, 2, 3, 4]
    assert [p['role'] for p in out['picks']] == ['PICK', 'PICK', 'INFORMATIONAL', 'INFORMATIONAL']
    assert all(p['tag'] in ('SUPPLIED', 'ANALYST_DERIVED') for p in out['picks'])
    ps = [p['p_card'] for p in out['picks']]
    assert ps == sorted(ps, reverse=True) and max(ps) <= 0.90
    assert len(out['ladder']) > 30 and {t['family'] for t in out['ladder']} >= {'winner', 'handicap', 'total', 'team_total'}
    assert out['joint_failure_top2'] is not None and 'passed' in out['rank1_gate'] and out['endpoint'] == 'full_game'
    assert out['distribution_object'].startswith(out['distribution_id']) and 'NHLEngine' in out['distribution_object']
    assert any('ILLUSTRATIVE' in c for c in out['caveats'])
    json.dumps(out)                                                                          # the whole block serialises


def test_pick_table_passes_the_card_validator_apart_from_placeholders():
    out = candidates.run(HOCKEY)
    assert card_validator.check_tables(out['pick_table']) == []
    assert 'TO_FILL' in out['pick_table'] and out['pick_table'].count('FROM_DISTRIBUTION:' + out['distribution_id']) == 4


def test_distribution_id_is_stable_and_content_addressed():
    a, b = candidates.run(HOCKEY), candidates.run(HOCKEY)
    assert a['distribution_id'] == b['distribution_id']
    other = candidates.run({**HOCKEY, 'context': {'home_xg': 3.4, 'away_xg': 2.7}})
    assert other['distribution_id'] != a['distribution_id']


def test_supplied_rows_are_included_tagged_and_reported_when_not_selected():
    out = candidates.run(HOCKEY)
    tags = {p['proposition']: p['tag'] for p in out['picks']}
    for name in ('Over 6.5 (supplied)', 'Southport Bears moneyline (supplied)'):
        if name in tags:
            assert tags[name] == 'SUPPLIED'
        else:
            assert any(s['proposition'] == name for s in out['supplied_not_selected'])
    assert any(t['tag'] == 'SUPPLIED' for t in out['ladder'])


@pytest.mark.parametrize('sport,league,context', [
    ('soccer', None, {'home_xg': 1.7, 'away_xg': 1.0, 'dixon_coles_rho': -0.05}),
    ('basketball', 'NBA', {'home_expected_points': 116.0, 'away_expected_points': 111.0}),
    ('american_football', 'NFL', {'home_expected_points': 25.0, 'away_expected_points': 20.0}),
    ('tennis', None, {'p_serve1': 0.67, 'p_serve2': 0.61, 'form_sigma': 0.04}),
])
def test_other_sports_use_their_own_engines(sport, league, context):
    out = candidates.run({'sport': sport, 'league': league, 'context': context})
    assert len(out['picks']) == 4 and out['picks'][0]['p_card'] <= 0.90


def test_guards():
    with pytest.raises(ValueError, match='league is required'):
        candidates.run({'sport': 'basketball', 'context': {'home_expected_points': 110, 'away_expected_points': 105}})
    with pytest.raises(ValueError):
        candidates.run({'sport': 'curling', 'context': {}})
    with pytest.raises(ValueError, match='kicking'):
        candidates.run({'sport': 'rugby_league', 'league': 'NRL', 'context': {'home_expected_tries': 4.0, 'away_expected_tries': 3.5}})

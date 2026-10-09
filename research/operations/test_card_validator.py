"""Rank-order gate, historical replay and family rules (PRD-01, PRD-09, GOV-03)."""
from pathlib import Path

import pytest

from research.operations import card_validator as cv

ROOT = Path(__file__).resolve().parents[2]
PART6 = ROOT / 'prediction logs/PREDICTION_LOG_COMBINED_6.md'

GOOD = """| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | SUPPLIED | A | 71.0% | x | e | f |
| 2 | PICK | SUPPLIED | B | 64.0% | x | e | f |
| 3 | INFORMATIONAL | SUPPLIED | C | 55.0% | x | e | f |
| 4 | INFORMATIONAL | SUPPLIED | D | 55.0% | x | e | f |
"""


def test_a_p_card_ranked_table_passes():
    assert cv.check_tables(GOOD) == []


def test_inversion_is_flagged_and_equal_probabilities_are_not():
    bad = GOOD.replace('55.0% | x | e | f |\n| 4', '45.0% | x | e | f |\n| 4').replace('| D | 55.0%', '| D | 60.0%')
    kinds = {f['kind'] for f in cv.check_tables(bad)}
    assert kinds == {'RANK_ORDER_INVERSION'}


def test_q_beside_p_is_rejected_on_new_cards():
    table = "| Rank | Proposition | p | q |\n|---|---|---|---|\n| 1 | A | 0.60 | 0.70 |\n| 2 | B | 0.55 | 0.65 |\n"
    assert {f['kind'] for f in cv.check_tables(table)} == {'P_AND_Q_COLUMNS'}
    inverted = "| Rank | Proposition | p | q |\n|---|---|---|---|\n| 1 | A | 0.45 | 0.80 |\n| 2 | B | 0.55 | 0.70 |\n"
    assert {'RANK_ORDER_INVERSION', 'RANKED_BY_Q'} <= {f['kind'] for f in cv.check_tables(inverted)}


def test_historical_replay_flags_exactly_p519_p521_p522():
    found = cv.replay([PART6], {'RANK_ORDER_INVERSION'})
    flagged = sorted(k for k in found if 518 <= int(k[2:]) <= 522)
    assert flagged == ['P-519', 'P-521', 'P-522']                          # the retrospective's PRD-01 acceptance replay
    assert all(any(f['kind'] == 'RANK_ORDER_INVERSION' for f in found[k]) for k in flagged)
    ranked_by_q = cv.replay([PART6], {'RANKED_BY_Q'})
    assert {'P-519', 'P-521', 'P-522'} <= set(ranked_by_q)


def test_reconciliation_table_with_an_id_column_is_replayed_per_card():
    recon = ROOT / 'P518_P522_RECONCILIATION.md'
    found = cv.scan_markdown(recon)
    assert {f['card'] for f in found if f['kind'] == 'RANK_ORDER_INVERSION'} == {'P-519', 'P-521', 'P-522'}


def test_commit_gate_blocks_new_inversions_but_exempts_historic_imports():
    bad = GOOD.replace('| 71.0% |', '| 51.0% |')
    assert cv.commit_gate(bad, 'UNCALIBRATED_ANALYST_SCENARIO')
    assert cv.commit_gate(bad, 'HISTORICAL_RESEARCH_IMPORT') == []
    assert cv.commit_gate(GOOD, 'UNCALIBRATED_ANALYST_SCENARIO') == []
    assert cv.commit_gate('no tables here', '') == []


def test_log_card_commit_rejects_an_inverted_card(tmp_path):
    from research.operations import log_card
    source = tmp_path / 'card.txt'
    source.write_text('x', encoding='utf-8')
    card = {'event_key': 'T:1', 'title': 't', 'tracking_handle': 'h', 'analysis_status': 'UNCALIBRATED_ANALYST_SCENARIO',
            'body': GOOD.replace('| 71.0% |', '| 51.0% |'), 'source_path': str(source)}
    with pytest.raises(ValueError, match='rank-order gate'):
        log_card.commit(card)


@pytest.mark.parametrize('proposition,sport,rank,p,expect', [
    ('Mets +1.5 — full game', 'Baseball', 1, 0.640, 'Rank 1 below'),
    ('Mets +1.5 — full game', 'Baseball', 1, 0.660, None),
    ('Mets +1.5 — full game', 'Baseball', 2, 0.600, None),
    ('Northfield Owls +1.5 — full game', 'Ice hockey', 1, 0.60, None),
    ('1st half Over 0.5 goals', 'Soccer', 1, 0.700, 'Rank 1 below'),
    ('1st half Over 0.5 goals', 'Soccer', 1, 0.740, 'half_split'),
    ('Total games Over 21.5', 'Tennis', 2, 0.600, 'tennis_exact_tree_form_shock'),
    ('Total games Over 21.5', 'Soccer', 2, 0.600, None),
    ('Total corners Over 9.5', 'Soccer', 2, 0.600, 'corners_nb'),
])
def test_family_rules(proposition, sport, rank, p, expect):
    out = cv.family_rule_findings([{'rank': rank, 'proposition': proposition, 'p_card': p, 'status': ''}], {'Distribution object': 'plain_model'}, sport)
    if expect is None:
        assert out == []
    else:
        assert any(expect in line for line in out), out


def test_family_rules_accept_the_named_models():
    meta = {'Distribution object': 'tennis_exact_tree_form_shock', 'Settlement fields': 'corners (provider: opta)'}
    assert cv.family_rule_findings([{'rank': 2, 'proposition': 'Total games Over 21.5', 'p_card': 0.6}], meta, 'Tennis') == []
    meta = {'Distribution object': 'soccer_halves_half_split_v1', 'Settlement fields': ''}
    assert cv.family_rule_findings([{'rank': 1, 'proposition': '1st half Over 0.5 goals', 'p_card': 0.75}], meta, 'Soccer') == []
    meta = {'Distribution object': 'corners_nb_v1', 'Settlement fields': 'Corners (provider: opta)'}
    assert cv.family_rule_findings([{'rank': 2, 'proposition': 'Total corners Over 9.5', 'p_card': 0.6}], meta, 'Soccer') == []
    meta = {'Distribution object': 'corners_nb_v1', 'Settlement fields': 'Corners'}
    assert any('provider' in x for x in cv.family_rule_findings([{'rank': 2, 'proposition': 'Total corners Over 9.5', 'p_card': 0.6}], meta, 'Soccer'))

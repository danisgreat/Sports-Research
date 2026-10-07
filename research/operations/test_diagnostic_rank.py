import pytest
from research.operations.diagnostic_rank import metrics


def test_ideal_ranking_uses_all_winning_contracts():
    # P-539 has another win below rank 2; P-548 has three slate wins.
    assert metrics(['WIN', 'LOSS', 'LOSS', 'WIN'])['ndcg_at_2'] == pytest.approx(0.6131471927654584)
    assert metrics(['LOSS', 'WIN', 'WIN', 'WIN'])['ndcg_at_2'] == pytest.approx(0.3868528072345416)
    assert metrics(['WIN', 'WIN', 'LOSS', 'LOSS'])['ndcg_at_2'] == 1
    assert metrics(['LOSS', 'LOSS', 'WIN', 'LOSS', 'WIN'])['ndcg_at_2'] == 0


def test_censoring_and_no_relevance_do_not_invent_a_score():
    assert metrics(['UNKNOWN_DEFINITION'] * 4) is None
    assert metrics(['WIN', 'PUSH']) is None
    assert metrics(['LOSS'] * 4)['ndcg_at_2'] is None

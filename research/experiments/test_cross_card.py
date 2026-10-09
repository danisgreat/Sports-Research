"""Cross-card experiments: six frozen protocols with recomputed power plans (EVL-04)."""
import json
from pathlib import Path

import numpy as np
import pytest

from research.experiments import cross_card

ROOT = Path(__file__).resolve().parents[2]


def test_power_formula_matches_hand_calculation():
    plan = cross_card.power_plan(0.5, 1.0, rows_per_week=1.0, icc=0.0)
    assert plan['n_independent'] == 32 and plan['design_effect'] == 1.0 and plan['rows_required'] == 32     # (1.96 + 0.8416)^2 / 0.25 = 31.4
    clustered = cross_card.power_plan(0.5, 1.0, rows_per_week=11.0, icc=0.05)
    assert clustered['design_effect'] == 1.5 and clustered['rows_required'] == 48
    assert cross_card.power_plan(-0.5, 1.0, 1.0, 0.0)['rows_required'] == 32                                    # sign does not matter
    assert cross_card.power_plan(0.1, 1.0, 5.0)['rows_required'] > cross_card.power_plan(0.2, 1.0, 5.0)['rows_required']
    with pytest.raises(ValueError):
        cross_card.power_plan(0.0, 1.0, 5.0)


def test_six_protocols_cover_distinct_taxonomy_classes_and_the_lock_verifies():
    lock = json.loads((ROOT / 'research/experiments/cross_card_v1.json').read_text(encoding='utf-8'))
    assert [p['id'] for p in lock['protocols']] == [f'XCARD-{i}' for i in range(1, 7)]
    assert len({p['failure_class'] for p in lock['protocols']}) == 6
    assert cross_card.verify() == []
    for p in lock['protocols']:
        assert p['cohort']['frozen'] and p['performance_eligible'] is False and p['acceptance']['gate'] == 'EVL-02'
        assert p['power_plan']['rows_required'] >= p['power_plan']['n_independent'] and 'feasibility_note' in p['power_plan']


def test_infeasible_plans_say_so_instead_of_pretending(tmp_path):
    lock = json.loads((ROOT / 'research/experiments/cross_card_v1.json').read_text(encoding='utf-8'))
    by_id = {p['id']: p for p in lock['protocols']}
    assert by_id['XCARD-1']['power_plan']['feasible_within_weeks'] is True
    assert by_id['XCARD-5']['power_plan']['feasible_within_weeks'] is False
    assert 'directional' in by_id['XCARD-5']['power_plan']['feasibility_note']
    assert by_id['XCARD-6']['status'] == 'REGISTERED_BLOCKED'


def test_tampering_with_a_protocol_is_detected(tmp_path):
    lock = json.loads((ROOT / 'research/experiments/cross_card_v1.json').read_text(encoding='utf-8'))
    lock['protocols'][0]['acceptance']['delta_brier_ci95_upper_below'] = 0.05
    path = tmp_path / 'cross_card_v1.json'
    path.write_text(json.dumps(lock), encoding='utf-8')
    problems = cross_card.verify(path)
    assert problems and any('differs from the definitions' in p for p in problems)
    assert cross_card.verify(tmp_path / 'nope.json')[0].startswith(str(tmp_path / 'nope.json'))


def test_evaluate_applies_the_registered_acceptance_to_cohort_rows(tmp_path):
    rng = np.random.default_rng(2)
    n, per_week = 400, 8
    truth = np.clip(rng.normal(0.55, 0.15, n), 0.1, 0.9)
    y = (rng.random(n) < truth).astype(float)
    good, base = np.clip(truth + rng.normal(0, 0.03, n), 0.02, 0.98), np.full(n, 0.55)
    ids = [f'e{i}' for i in range(n)]
    blocks = [f'W{i // per_week:03d}' for i in range(n)]
    result = cross_card.evaluate('XCARD-1', y, good, base, ids, [0.0] * n, blocks)
    assert result['is_promotable'] is True and result['protocol_sha256'] and result['n_blocks'] == 50
    short = cross_card.evaluate('XCARD-1', y[:100], good[:100], base[:100], ids[:100], [0.0] * 100, blocks[:100])
    assert short['is_promotable'] is False and any('below minimum requirement' in r for r in short['promotion_reasons'])
    with pytest.raises(ValueError, match='cards'):
        cross_card.evaluate('XCARD-5', y, good, base, ids, [0.0] * n, blocks)

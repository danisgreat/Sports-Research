"""H0 rolling-origin receipts and the boosted challenger, on a small synthetic hockey archive (ML-03, ML-06)."""
import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

from research.operations import boosted_challenger as bc
from research.operations import fit_runtime_models as h0
from research.src.archive_std import StdEvent


def synthetic_league(seasons=6, teams=8, seed=3):
    rng = np.random.default_rng(seed)
    names = [f'Club{i}' for i in range(teams)]
    att = rng.normal(0, 0.25, teams)
    events = []
    for s in range(seasons):
        day = date(2018 + s, 10, 1)
        k = 0
        for _ in range(4):
            for i in range(teams):
                for j in range(teams):
                    if i != j:
                        events.append(StdEvent(sport='Ice Hockey', competition='SYN', season_year=2019 + s, date=day.isoformat(), stage='regular',
                                               home=names[i], away=names[j], home_score=int(rng.poisson(3.1 * np.exp(att[i] - 0.5 * att[j]))),
                                               away_score=int(rng.poisson(2.8 * np.exp(att[j] - 0.5 * att[i])))))
                        k += 1
                        if k % 4 == 0:
                            day += timedelta(days=1)
    return events


def test_rolling_origin_receipt_has_point_in_time_structure_and_metrics():
    spec = h0.specs()['nhl']
    events = synthetic_league()
    result = h0.run_spec(spec, events, test_seasons=1, sample=60)
    assert result['status'] == 'FITTED_RECEIPT' and result['test_seasons'] == [2024] and result['refits'] >= 2
    assert result['predictions'] > 40 and result['prediction_errors'] == {}
    metrics = result['metrics']
    assert set(metrics) == {'home_win', 'total_over_train_median', 'home_cover_train_median_margin'}
    win = metrics['home_win']
    assert win['n'] > 30 and win['blocks'] >= 8
    assert set(['brier_engine', 'brier_baseline', 'delta_brier', 'delta_brier_ci95', 'calibration_slope', 'calibration_slope_ci95']) <= set(win)
    assert win['delta_brier_ci95'][0] < win['delta_brier_ci95'][1]
    again = h0.run_spec(spec, events, test_seasons=1, sample=60)
    assert again['metrics']['home_win']['brier_engine'] == win['brier_engine']                  # deterministic


def test_too_little_history_is_reported_not_faked():
    result = h0.run_spec(h0.specs()['nhl'], synthetic_league(seasons=2), test_seasons=2, sample=20)
    assert result['status'] == 'INSUFFICIENT_SEASONS'


def test_build_writes_receipt_artifact_and_a_verifiable_index(tmp_path, monkeypatch):
    spec = h0.specs()['nhl']
    events = synthetic_league()
    monkeypatch.setattr(h0, 'load_events', lambda s, root=None: events)
    monkeypatch.setattr(h0, 'ROOT', tmp_path)
    receipt = h0.build(spec, tmp_path / 'out', test_seasons=1, sample=40)
    assert receipt['status'] == 'FITTED_RECEIPT' and (tmp_path / 'out/nhl.model.json').exists()
    assert len(receipt['code_sha256']) == 64 and receipt['final_fit']['games'] > 500
    index = h0.write_index(tmp_path / 'out')
    assert 'nhl' in index['receipts'] and set(index['not_fitted']) == {'tennis', 'cricket'}
    problems = h0.verify(tmp_path / 'out')
    assert any('engines without a receipt' in p for p in problems)               # only nhl was built here
    stored = json.loads((tmp_path / 'out/nhl.receipt.json').read_text(encoding='utf-8'))
    stored['predictions'] = 1
    (tmp_path / 'out/nhl.receipt.json').write_text(json.dumps(stored), encoding='utf-8')
    assert any('changed since the index' in p for p in h0.verify(tmp_path / 'out'))


def test_every_engine_is_covered_by_a_spec_or_an_explicit_reason():
    assert set(h0.specs()) == {'nhl', 'nba', 'mlb', 'nfl', 'nrl', 'afl', 'epl'}
    assert all('serve' in v[1] or 'ball-by-ball' in v[1] for v in h0.NOT_FITTED.values())


def test_committed_receipts_verify():
    index = Path(h0.OUT / 'INDEX.json')
    if not index.exists():
        pytest.skip('receipts not built in this checkout')
    assert h0.verify() == []


def test_crps_and_total_pmf_helpers():
    from runtime.src.common.contracts import ScoreDistribution
    grid = np.zeros((3, 3))
    grid[1, 1] = 1.0                                                     # total is exactly 2
    dist = ScoreDistribution(grid, np.arange(3), np.arange(3))
    assert bc.total_pmf(dist)[2] == pytest.approx(1.0)
    assert bc.crps_total(dist, 2) == pytest.approx(0.0)
    assert bc.crps_total(dist, 5) == pytest.approx(3.0)                  # F(t) = 1 at t = 2, 3, 4 while the actual total (5) has not been reached: three unit errors
    assert bc.crps_total(dist, 0) == pytest.approx(2.0)


def test_challenger_runs_on_synthetic_hockey_and_reports_measured_result():
    events = synthetic_league(seasons=6, teams=8)
    result = bc.run_sport('nhl', events, test_seasons=1, sample=60)
    assert result['status'] == 'MEASURED' and result['predictions'] > 40 and result['features'][0] == 'home_rest'
    for key in ('winner_log_loss', 'total_crps'):
        assert {'baseline', 'challenger', 'mean_difference', 'ci95', 'challenger_better'} <= set(result[key])
    assert isinstance(result['beats_baseline_on_both'], bool)
    assert bc.run_sport('nhl', synthetic_league(seasons=2), test_seasons=2)['status'] == 'INSUFFICIENT_SEASONS'


def test_challenger_index_applies_the_two_sport_acceptance_rule(tmp_path):
    for key, both in (('nhl', True), ('nba', True), ('epl', False)):
        (tmp_path / f'{key}.challenger.json').write_text(json.dumps({'key': key, 'status': 'MEASURED', 'beats_baseline_on_both': both,
                                                                     'winner_log_loss': {'mean_difference': -0.01}, 'total_crps': {'mean_difference': -0.1}}), encoding='utf-8')
    index = bc.write_index(tmp_path)
    assert index['acceptance']['met'] is True and index['acceptance']['sports_beaten'] == ['nba', 'nhl']
    (tmp_path / 'nba.challenger.json').write_text(json.dumps({'key': 'nba', 'status': 'MEASURED', 'beats_baseline_on_both': False}), encoding='utf-8')
    assert bc.write_index(tmp_path)['acceptance']['met'] is False

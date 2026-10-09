"""ML-02: an optimiser failure can never leave a model that predicts (acceptance: a forced failure cannot produce a ScoreDistribution)."""

import numpy as np
import pytest
from scipy.optimize import OptimizeResult

from runtime.src.common import calibration, dixon_coles, distributional, strengths
from runtime.src.common.contracts import ScoreDistribution
from runtime.src.common.errors import FitFailed, NotFitted
from runtime.src.sports.nhl.engine import NHLEngine
from runtime.src.sports.nrl.engine import NRLEngine, NRLKicking
from runtime.src.sports.soccer.engine import SoccerEngine
from runtime.tests.test_soccer_models import season

FAILED = lambda n: (lambda *a, **k: OptimizeResult(success=False, message="forced failure", x=np.zeros(n), jac=np.ones(n), fun=np.ones(2) * 9))


def hockey_games(n=160, seed=2):
    rng = np.random.default_rng(seed)
    teams = [f"T{i}" for i in range(8)]
    out = []
    for _ in range(n):
        h, a = rng.choice(teams, 2, replace=False)
        out.append({"home_team": h, "away_team": a, "home_goals": int(rng.poisson(3.1)), "away_goals": int(rng.poisson(2.8))})
    return out


def test_calibrators_raise_instead_of_returning_defaults(monkeypatch):
    monkeypatch.setattr(calibration, "minimize", FAILED(2))
    p = np.linspace(0.1, 0.9, 40)
    y = (p > 0.5).astype(float)
    for cls in (calibration.PlattScaler,):
        with pytest.raises(FitFailed):
            cls().fit(p, y)
    with pytest.raises(FitFailed):
        calibration.compute_calibration_slope(y, p)


def test_strength_model_failure_leaves_the_engine_unfitted_and_unable_to_predict(monkeypatch):
    monkeypatch.setattr(strengths, "minimize", FAILED(20))
    engine = NHLEngine()
    with pytest.raises(FitFailed):
        engine.fit(hockey_games())
    assert not engine.is_fitted
    with pytest.raises(Exception) as caught:
        engine.predict_distribution({"home_team": "T1", "away_team": "T2"})
    assert not isinstance(caught.value, AssertionError)


def test_dixon_coles_failure_cannot_produce_a_score_distribution(monkeypatch):
    monkeypatch.setattr(dixon_coles, "minimize", FAILED(20))
    engine = SoccerEngine()
    with pytest.raises(FitFailed):
        engine.fit(season())
    assert not engine.is_fitted
    result = None
    with pytest.raises((NotFitted, FitFailed, ValueError)):
        result = engine.predict_distribution({"home_team": "Club1", "away_team": "Club2", "dixon_coles_rho": -0.05})
    assert not isinstance(result, ScoreDistribution)


def test_negative_binomial_failure_leaves_no_flat_model(monkeypatch):
    monkeypatch.setattr(distributional, "minimize", FAILED(3))
    X = np.column_stack([np.ones(50), np.linspace(0, 1, 50)])
    model = distributional.NegativeBinomialCountRegressor()
    with pytest.raises(FitFailed):
        model.fit(X, np.arange(50) % 5)
    assert not model.is_fitted
    with pytest.raises(NotFitted):
        model.predict_pmf(X[0])


def test_structure_calibration_failure_refuses_to_price(monkeypatch):
    import runtime.src.sports.nrl.engine as nrl
    monkeypatch.setattr(nrl, "least_squares", lambda *a, **k: OptimizeResult(success=False, x=np.array([1.0, 1.0]), fun=np.array([0.9, 0.9])))
    from runtime.src.common.leagues import get_profile
    engine = NRLEngine(league=get_profile("rugby_league", "NRL"), kicking=NRLKicking(0.8, 0.5, 0.1))
    result = None
    with pytest.raises(FitFailed):
        result = engine.predict_distribution({"home_expected_tries": 4.0, "away_expected_tries": 3.5})
    assert result is None

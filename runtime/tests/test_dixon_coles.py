"""Unit tests for Dixon-Coles model."""

import numpy as np
import pytest

from runtime.src.common.dixon_coles import DixonColesEngine


def test_dixon_coles_fitting_and_distribution():
    engine = DixonColesEngine(xi=0.002, l2_reg=0.05)
    matches = [
        {"home": "ManCity", "away": "Everton", "home_goals": 3, "away_goals": 0, "days_ago": 10},
        {"home": "Everton", "away": "ManCity", "home_goals": 0, "away_goals": 2, "days_ago": 40},
        {"home": "Arsenal", "away": "Everton", "home_goals": 2, "away_goals": 1, "days_ago": 15},
        {"home": "ManCity", "away": "Arsenal", "home_goals": 1, "away_goals": 1, "days_ago": 25},
        {"home": "Arsenal", "away": "ManCity", "home_goals": 0, "away_goals": 0, "days_ago": 60},
    ]
    engine.fit(matches)

    score_dist = engine.predict_score_distribution("ManCity", "Everton")
    grid = score_dist.grid

    # Probability mass must sum to 1.0
    assert np.isclose(np.sum(grid), 1.0, atol=1e-4)

    # City at home vs Everton should heavily favor City
    p_h = score_dist.p_home_win()
    p_a = score_dist.p_away_win()
    assert p_h > p_a

    # Low-score adjustment check
    tau_00 = DixonColesEngine.tau(0, 0, 1.5, 1.2, -0.04)
    assert tau_00 > 1.0  # - rho * lambda * mu increases 0-0 probability when rho is negative

    # Parameter rho must be strictly within valid empirical bounds [-0.25, 0.25]
    assert -0.25 <= engine.rho <= 0.25

    # Verify all 4 low-score adjustment factors are strictly positive
    lambda_h = np.exp(engine.attacks[engine.team_idx["ManCity"]] + engine.defences[engine.team_idx["Everton"]] + engine.home_adv)
    mu_a = np.exp(engine.attacks[engine.team_idx["Everton"]] + engine.defences[engine.team_idx["ManCity"]])
    for (x, y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        assert DixonColesEngine.tau(x, y, lambda_h, mu_a, engine.rho) > 0.0


def test_dixon_coles_rejects_invalid_tau():
    """Verify that predicting with invalid dependence parameters raises ValueError rather than clipping."""
    engine = DixonColesEngine()
    engine.teams = ["TeamA", "TeamB"]
    engine.team_idx = {"TeamA": 0, "TeamB": 1}
    engine.attacks = np.array([0.5, -0.5])
    engine.defences = np.array([0.5, -0.5])
    engine.home_adv = 0.5
    engine.rho = -2.5  # Grossly invalid rho that produces tau <= 0

    with pytest.raises(ValueError, match="Invalid Dixon-Coles parameters"):
        engine.predict_score_distribution("TeamA", "TeamB")



# --- ML-02 / ML-04 / DST-13 -------------------------------------------------------------------

import time

from scipy.optimize import check_grad
from scipy.stats import poisson as _poisson

from runtime.src.common.errors import FitFailed, InsufficientData, UnknownTeam


def season(teams=20, rounds=2, seed=5, home_log=0.25, rho=-0.08):
    """A double round robin simulated from known strengths, with the Dixon-Coles low-score dependence."""
    rng = np.random.default_rng(seed)
    names = [f"Club{i:02d}" for i in range(teams)]
    att = rng.normal(0, 0.25, teams)
    att -= att.mean()
    dfn = rng.normal(0, 0.20, teams)
    base = np.log(1.25)
    matches, day = [], 380
    for _ in range(rounds):
        for i in range(teams):
            for j in range(teams):
                if i == j:
                    continue
                lam, mu = np.exp(base + att[i] + dfn[j] + home_log), np.exp(base + att[j] + dfn[i])
                grid = np.outer(_poisson.pmf(np.arange(10), lam), _poisson.pmf(np.arange(10), mu))
                grid[0, 0] *= 1 - lam * mu * rho
                grid[0, 1] *= 1 + lam * rho
                grid[1, 0] *= 1 + mu * rho
                grid[1, 1] *= 1 - rho
                flat = (grid / grid.sum()).ravel()
                k = rng.choice(flat.size, p=flat)
                matches.append({"home": names[i], "away": names[j], "home_goals": int(k // 10), "away_goals": int(k % 10),
                                "days_ago": float(day)})
                day = max(0, day - 0.5)
    return matches, names, att, dfn


def test_analytic_gradient_matches_finite_differences():
    matches, names, _, _ = season(teams=6, rounds=2)
    engine = DixonColesEngine(xi=0.002, l2_reg=0.05)
    index = {t: i for i, t in enumerate(sorted(names))}
    hi, ai, hg, ag, days = engine._prepare(matches, index)
    w = np.exp(-0.002 * days)
    n = len(index)
    rng = np.random.default_rng(0)
    theta = np.concatenate([rng.normal(0, 0.1, 2 * n), [0.2, -0.05]])
    f = lambda t: engine._objective(t, n, hi, ai, hg, ag, w)[0]
    g = lambda t: engine._objective(t, n, hi, ai, hg, ag, w)[1]
    assert check_grad(f, g, theta) < 2e-4 * max(1.0, np.linalg.norm(g(theta)))


def test_full_season_fit_is_fast_and_recovers_strengths():
    matches, names, att, _ = season()
    engine = DixonColesEngine(xi=0.0)
    started = time.perf_counter()
    engine.fit(matches)
    assert time.perf_counter() - started < 2.0                      # ML-04 acceptance: one EPL-size season in <= 2 s
    assert engine.converged
    fitted = np.array([engine.attacks[engine.team_idx[n]] for n in names])
    assert np.corrcoef(fitted, att)[0, 1] > 0.9
    assert engine.home_adv == pytest.approx(0.25, abs=0.12)


def test_xi_is_chosen_by_rolling_origin_cross_validation():
    matches, _, _, _ = season(teams=10, rounds=3, seed=2)
    engine = DixonColesEngine()
    best, table = engine.tune_xi(matches, xis=(0.0, 0.002, 0.02), folds=3, min_train=120)
    assert best in table and engine.xi == best
    assert all(np.isfinite(v) for v in table.values())
    assert table[best] == min(table.values())


def test_failed_optimiser_raises_instead_of_returning_a_flat_model(monkeypatch):
    from runtime.src.common import dixon_coles as module

    class Failed:
        success = False
        message = "forced failure"
        x = np.zeros(2)
        jac = np.array([9.0, 9.0])

    monkeypatch.setattr(module, "minimize", lambda *a, **k: Failed())
    matches, _, _, _ = season(teams=4, rounds=1)
    engine = DixonColesEngine()
    with pytest.raises(FitFailed, match="forced failure"):
        engine.fit(matches)
    assert not engine.converged and engine.teams == []


def test_unknown_team_is_refused_unless_a_stand_in_is_requested():
    matches, names, _, _ = season(teams=6, rounds=2)
    refuse = DixonColesEngine(xi=0.0).fit(matches)
    with pytest.raises(UnknownTeam):
        refuse.predict_score_distribution(names[0], "Newly Promoted FC")
    stand_in = DixonColesEngine(xi=0.0, unknown_team="league_average").fit(matches)
    dist = stand_in.predict_score_distribution(names[0], "Newly Promoted FC")
    assert dist.metadata["warnings"] and "Newly Promoted FC" in dist.metadata["warnings"][0]
    assert dist.endpoint == "regulation"
    with pytest.raises(InsufficientData):
        DixonColesEngine().fit(matches[:2])

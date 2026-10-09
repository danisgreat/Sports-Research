"""DST-05: opponent-adjusted, data-shrunk team strengths."""

import numpy as np
import pytest
from scipy.optimize import check_grad

from runtime.src.common.errors import InsufficientData
from runtime.src.common.strengths import AttackDefenceModel


def simulate(n_games=900, seed=3, teams=12, mean=1.4, home_log=0.12):
    rng = np.random.default_rng(seed)
    names = [f"T{i}" for i in range(teams)]
    att = rng.normal(0, 0.25, teams)
    att -= att.mean()
    defn = rng.normal(0, 0.20, teams)
    defn -= defn.mean()
    games = []
    for _ in range(n_games):
        i, j = rng.choice(teams, 2, replace=False)
        mu_h = mean * np.exp(home_log + att[i] + defn[j])
        mu_a = mean * np.exp(att[j] + defn[i])
        games.append((names[i], names[j], float(rng.poisson(mu_h)), float(rng.poisson(mu_a))))
    return games, names, att, defn


def test_recovers_known_strengths_and_home_advantage():
    games, names, att, defn = simulate()
    model = AttackDefenceModel(ridge=3.0).fit(games)
    assert model.log_home == pytest.approx(0.12, abs=0.05)
    fitted = np.array([model.att[model.teams.index(t)] for t in names])
    assert np.corrcoef(fitted, att)[0, 1] > 0.9
    league_home, league_away = model.league_means()
    assert league_home > league_away
    assert 1.2 < league_away < 1.6


def test_opponent_adjustment_not_raw_means():
    # Team A only ever plays a strong defence; its raw mean understates its attack.
    rng = np.random.default_rng(1)
    games = []
    for _ in range(400):
        games.append(("A", "STRONG_D", float(rng.poisson(1.0)), float(rng.poisson(1.3))))
        games.append(("B", "WEAK_D", float(rng.poisson(1.6)), float(rng.poisson(1.3))))
        games.append(("C", "D", float(rng.poisson(1.3)), float(rng.poisson(1.3))))
        games.append(("STRONG_D", "WEAK_D", float(rng.poisson(1.3)), float(rng.poisson(1.3))))
    model = AttackDefenceModel(ridge=1.0).fit(games)
    assert model.teams  # fits and converges on a connected graph
    scoring, conceding = model.factors()
    assert conceding["STRONG_D"] < conceding["WEAK_D"]


def test_shrinkage_grows_as_games_shrink():
    games, names, _, _ = simulate(n_games=600)
    full = AttackDefenceModel(ridge=10.0).fit(games)
    few = AttackDefenceModel(ridge=10.0).fit(games[:60])
    assert np.std(few.att) < np.std(full.att)
    heavy = AttackDefenceModel(ridge=3000.0).fit(games)
    assert np.std(heavy.att) < 0.2 * np.std(full.att) and np.std(heavy.defn) < 0.2 * np.std(full.defn)


def test_cv_chooses_a_larger_ridge_for_less_data():
    games, _, _, _ = simulate(n_games=1500, seed=9)
    big = AttackDefenceModel(min_games=20)
    big.choose_ridge(games)
    small = AttackDefenceModel(min_games=20)
    small.choose_ridge(games[:120])
    assert set(big.cv_scores) == set(small.cv_scores)
    assert min(small.cv_scores, key=small.cv_scores.get) >= min(big.cv_scores, key=big.cv_scores.get)


def test_gradient_matches_finite_differences():
    games, names, _, _ = simulate(n_games=120, teams=6)
    index = {t: i for i, t in enumerate(sorted(names))}
    home, away, hs, as_ = AttackDefenceModel._arrays(games, index)
    n = len(index)

    def f(theta):
        m, h, att, defn = theta[0], theta[1], theta[2:2 + n], theta[2 + n:]
        eta_h, eta_a = m + h + att[home] + defn[away], m + att[away] + defn[home]
        return np.sum(np.exp(eta_h) - hs * eta_h) + np.sum(np.exp(eta_a) - as_ * eta_a) + 0.5 * 2.0 * (np.sum(att ** 2) + np.sum(defn ** 2))

    def g(theta):
        m, h, att, defn = theta[0], theta[1], theta[2:2 + n], theta[2 + n:]
        r_h, r_a = np.exp(m + h + att[home] + defn[away]) - hs, np.exp(m + att[away] + defn[home]) - as_
        return np.concatenate([[r_h.sum() + r_a.sum(), r_h.sum()],
                               np.bincount(home, r_h, n) + np.bincount(away, r_a, n) + 2.0 * att,
                               np.bincount(away, r_h, n) + np.bincount(home, r_a, n) + 2.0 * defn])

    theta = np.random.default_rng(0).normal(0, 0.1, 2 + 2 * n)
    assert check_grad(f, g, theta) < 1e-4 * max(1.0, np.linalg.norm(g(theta)))


def test_zero_scores_are_real_scores_and_bad_input_is_rejected():
    games = [("A", "B", 0.0, 0.0)] * 15 + [("B", "A", 0.0, 1.0)] * 15
    model = AttackDefenceModel(ridge=5.0).fit(games)
    assert model.league_means()[0] < 0.5                    # shutouts are not replaced by a league-typical default
    with pytest.raises(InsufficientData):
        AttackDefenceModel().fit(games[:5])
    with pytest.raises(ValueError):
        AttackDefenceModel(min_games=1).fit([("A", "A", 1.0, 1.0)])
    with pytest.raises(ValueError):
        AttackDefenceModel(min_games=1).fit([("A", "B", -1.0, 1.0)])

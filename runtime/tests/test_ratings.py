"""Rating models (ML-07, ML-02): Elo with margins and carry-over, Glicko, surface Elo, draw-aware Bradley-Terry."""

import math

import numpy as np
import pytest
from scipy.optimize import approx_fprime

from runtime.src.common.errors import FitFailed, InsufficientData, UnknownTeam
from runtime.src.common.ratings import BradleyTerryDrawEngine, EloRatingEngine, GlickoRating, SurfaceElo, margin_multiplier


def test_elo_basic_updates_and_zero_sum():
    engine = EloRatingEngine(base_rating=1500.0, k_factor=32.0, home_advantage=50.0)
    assert engine.predict_prob("A", "B") > 0.5 and engine.predict_prob("A", "B", is_neutral=True) == pytest.approx(0.5)
    a, b = engine.update("A", "B", score_a=1.0)
    assert a > 1500.0 > b and a + b == pytest.approx(3000.0)
    assert engine.knows("A") and not engine.knows("C")
    with pytest.raises(ValueError):
        engine.update("A", "B", score_a=1.5)


def test_margin_multiplier_grows_with_margin_and_shrinks_with_favourite_edge():
    assert margin_multiplier(0, 100.0) == 1.0
    assert margin_multiplier(20, 0.0) > margin_multiplier(3, 0.0)
    assert margin_multiplier(10, 400.0) < margin_multiplier(10, 0.0) < margin_multiplier(10, -400.0)
    engine, plain = EloRatingEngine(), EloRatingEngine()
    engine.update("A", "B", 1.0, is_neutral=True, margin=20)
    plain.update("A", "B", 1.0, is_neutral=True)
    assert engine.ratings["A"] - 1500.0 > plain.ratings["A"] - 1500.0
    engine.update("C", "D", 0.5, is_neutral=True, margin=0)                                  # draws use the plain step
    assert engine.ratings["C"] == pytest.approx(1500.0)


def test_season_carry_over_regresses_toward_the_mean():
    engine = EloRatingEngine()
    engine.update("A", "B", 1.0, is_neutral=True)
    before = engine.ratings["A"]
    engine.regress_to_mean(carry=0.75)
    assert engine.ratings["A"] == pytest.approx(1500.0 + 0.75 * (before - 1500.0))
    with pytest.raises(ValueError):
        engine.regress_to_mean(carry=1.5)


def test_glicko_reproduces_glickmans_worked_example():
    g = GlickoRating()
    g.state = {"P": (1500.0, 200.0), "O1": (1400.0, 30.0), "O2": (1550.0, 100.0), "O3": (1700.0, 300.0)}
    g.last_period = {k: 0 for k in g.state}
    g.rate_period([("P", "O1", 1.0), ("P", "O2", 0.0), ("P", "O3", 0.0)])
    rating, rd = g.state["P"]
    assert rating == pytest.approx(1464.1, abs=0.1) and rd == pytest.approx(151.4, abs=0.1)    # Glickman (1999): r = 1464.1, RD = 151.4


def test_glicko_uncertainty_grows_when_idle_and_new_players_are_flagged():
    g = GlickoRating(c=40.0)
    g.rate_period([("A", "B", 1.0)])
    _, rd_now = g.rating("A")
    g.rate_period([("C", "D", 1.0)])
    g.rate_period([("C", "D", 0.0)])
    assert g.rating("A")[1] > rd_now                          # idle for two periods
    assert not g.knows("Z") and g.rating("Z") == (1500.0, 350.0)
    assert 0.5 < g.expected("A", "B") < 1.0
    uncertain = g.expected("A", "Z")
    assert 0.5 < uncertain < g.expected("A", "B") or uncertain > 0.5


def tennis_history(n=1500, seed=5):
    rng = np.random.default_rng(seed)
    players = [f"P{i}" for i in range(24)]
    skill = {p: rng.normal(0, 150) for p in players}
    clay_bonus = {p: (rng.normal(0, 120) if i % 2 else 0.0) for i, p in enumerate(players)}
    out = []
    for _ in range(n):
        a, b = rng.choice(players, 2, replace=False)
        surface = str(rng.choice(["hard", "clay"]))
        ra = skill[a] + (clay_bonus[a] if surface == "clay" else 0.0)
        rb = skill[b] + (clay_bonus[b] if surface == "clay" else 0.0)
        p = 1.0 / (1.0 + 10 ** (-(ra - rb) / 400.0))
        out.append((a, b, surface) if rng.random() < p else (b, a, surface))
    return out


def test_surface_elo_learns_surface_specialists_and_selects_a_weight():
    matches = tennis_history()
    model, table = SurfaceElo.fit_surface_weight(matches)
    assert set(table) == {0.0, 0.25, 0.5, 0.75, 1.0} and model.surface_weight == min(table, key=table.get)
    assert table[0.0] != table[0.5]
    base = -math.log(0.5)
    assert min(table.values()) < base - 0.02                      # beats the coin-flip baseline on walk-forward log loss
    a, b = "P1", "P3"                                              # odd-indexed players carry a clay bonus
    assert model.win_prob(a, b, "clay") != pytest.approx(model.win_prob(a, b, "hard"), abs=1e-3)
    assert model.win_prob(a, b, "hard") + model.win_prob(b, a, "hard") == pytest.approx(1.0)
    with pytest.raises(InsufficientData):
        SurfaceElo().fit(matches[:5])
    with pytest.raises(ValueError):
        SurfaceElo(surface_weight=1.5)


def test_rating_baseline_improves_on_the_home_rate_in_a_synthetic_league():
    rng = np.random.default_rng(1)
    teams = [f"T{i}" for i in range(16)]
    strength = {t: rng.normal(0, 100) for t in teams}
    engine = EloRatingEngine(k_factor=20.0, home_advantage=50.0)
    losses, base = [], []
    for _ in range(3000):
        h, a = rng.choice(teams, 2, replace=False)
        p_true = 1.0 / (1.0 + 10 ** (-(strength[h] - strength[a] + 50.0) / 400.0))
        home_win = rng.random() < p_true
        p = engine.predict_prob(h, a)
        losses.append(-math.log(p if home_win else 1.0 - p))
        base.append(-math.log(0.57 if home_win else 0.43))
        engine.update(h, a, 1.0 if home_win else 0.0, margin=None)
    assert np.mean(losses[1000:]) < np.mean(base[1000:])


MATCHES = [
    {"home": "Arsenal", "away": "Chelsea", "result": "home"}, {"home": "Liverpool", "away": "Arsenal", "result": "draw"},
    {"home": "Chelsea", "away": "Liverpool", "result": "away"}, {"home": "Arsenal", "away": "Liverpool", "result": "home"},
    {"home": "Liverpool", "away": "Chelsea", "result": "home"}, {"home": "Chelsea", "away": "Arsenal", "result": "draw"},
]


def test_bradley_terry_gradient_and_probabilities():
    engine = BradleyTerryDrawEngine(l2_reg=0.05, fit_home_advantage=True).fit(MATCHES)
    p_h, p_d, p_a = engine.predict_probs("Arsenal", "Chelsea")
    assert p_h + p_d + p_a == pytest.approx(1.0) and 0.0 < p_d < 1.0 and p_h > p_a
    index = engine.team_indices
    hi = np.array([index[m["home"]] for m in MATCHES])
    ai = np.array([index[m["away"]] for m in MATCHES])
    outcome = np.array([{"home": 0, "draw": 1, "away": 2}[m["result"]] for m in MATCHES])
    x = np.concatenate([engine.log_strengths + 0.1, [engine.log_nu, 0.2]])
    _, grad = BradleyTerryDrawEngine._nll(x, hi, ai, outcome, 3, 0.05, True)
    numeric = approx_fprime(x, lambda v: BradleyTerryDrawEngine._nll(v, hi, ai, outcome, 3, 0.05, True)[0], 1e-6)
    np.testing.assert_allclose(grad, numeric, rtol=1e-4, atol=1e-5)


def test_bradley_terry_recovers_home_advantage_and_draw_rate():
    rng = np.random.default_rng(2)
    teams = [f"T{i}" for i in range(8)]
    g = rng.normal(0, 0.4, 8)
    rows = []
    for _ in range(4000):
        i, j = rng.choice(8, 2, replace=False)
        ph, pa = np.exp(g[i] + 0.3), np.exp(g[j])
        pd_ = 0.8 * np.sqrt(ph * pa)
        probs = np.array([ph, pd_, pa]) / (ph + pd_ + pa)
        rows.append({"home": teams[i], "away": teams[j], "result": ["home", "draw", "away"][rng.choice(3, p=probs)]})
    fitted = BradleyTerryDrawEngine(l2_reg=0.01, fit_home_advantage=True).fit(rows)
    assert fitted.home_log_advantage == pytest.approx(0.3, abs=0.1) and math.exp(fitted.log_nu) == pytest.approx(0.8, abs=0.12)


def test_bradley_terry_refuses_unknowns_and_unfitted_models():
    with pytest.raises(UnknownTeam):
        BradleyTerryDrawEngine().predict_probs("A", "B")                       # no silent 1/3-1/3-1/3
    engine = BradleyTerryDrawEngine().fit(MATCHES)
    with pytest.raises(UnknownTeam):
        engine.predict_probs("Arsenal", "Everton")
    lenient = BradleyTerryDrawEngine(unknown_team="league_average").fit(MATCHES)
    assert sum(lenient.predict_probs("Arsenal", "Everton")) == pytest.approx(1.0)
    with pytest.raises(ValueError):
        BradleyTerryDrawEngine().fit([{"home": "A", "away": "B", "result": "win"}])
    with pytest.raises(InsufficientData):
        BradleyTerryDrawEngine().fit([])
    with pytest.raises(ValueError):
        BradleyTerryDrawEngine(unknown_team="guess")


def test_bradley_terry_nonconvergence_raises(monkeypatch):
    import runtime.src.common.ratings as ratings
    from scipy.optimize import OptimizeResult
    monkeypatch.setattr(ratings, "minimize", lambda *a, **k: OptimizeResult(success=False, message="forced", x=np.zeros(4), jac=np.ones(4)))
    engine = BradleyTerryDrawEngine()
    with pytest.raises(FitFailed):
        engine.fit(MATCHES)
    assert len(engine.log_strengths) == 0                                    # nothing half-fitted is left behind

"""Tennis engine (DST-04): exact tree with serve order, form shock, explicit policies, JSON artifacts."""

import numpy as np
import pytest

from runtime.src.common.errors import InsufficientData, MissingInputs, UnknownTeam
from runtime.src.sports.tennis.engine import (
    TennisEngine, calibrate_form_sigma, match_distribution, mix_over_form, p_game_hold, p_tiebreak_win, set_outcomes,
)

TRAIN = [
    {"player1": "Sinner", "player2": "Medvedev", "p1_serve_won": 50, "p1_serve_total": 70, "p2_serve_won": 40, "p2_serve_total": 70},
    {"player1": "Sinner", "player2": "Alcaraz", "p1_serve_won": 45, "p1_serve_total": 65, "p2_serve_won": 42, "p2_serve_total": 65},
]


def test_game_hold_formula():
    assert p_game_hold(0.5) == pytest.approx(0.5, abs=1e-9)
    assert p_game_hold(0.70) > 0.80 and p_game_hold(0.65) > p_game_hold(0.60)
    assert TennisEngine.p_game_hold(0.6) == p_game_hold(0.6)


def test_tiebreak_symmetry_and_monotonicity():
    assert p_tiebreak_win(0.65, 0.65) == pytest.approx(0.5, abs=1e-9)
    assert p_tiebreak_win(0.75, 0.55) > 0.65
    # the same match framed with either player serving first gives the same tiebreak probability
    a = p_tiebreak_win(0.68, 0.62)
    b = 1.0 - p_tiebreak_win(0.62, 0.68)                         # same match with the other player serving first
    assert a == pytest.approx(b, abs=1e-9) and 0.5 < a < 1.0


def test_set_outcomes_conserve_mass_and_respect_serve_order():
    for first in (True, False):
        out = set_outcomes(0.66, 0.62, first)
        assert sum(out.values()) == pytest.approx(1.0)
        assert set(out) <= {(6, k) for k in range(5)} | {(k, 6) for k in range(5)} | {(7, 5), (5, 7), (7, 6), (6, 7)}
    # who serves first leaves the set-win probability unchanged (a known property) but moves the scoreline
    first, second = set_outcomes(0.66, 0.62, True), set_outcomes(0.66, 0.62, False)
    assert sum(p for (a, b), p in first.items() if a > b) == pytest.approx(sum(p for (a, b), p in second.items() if a > b), abs=1e-9)
    assert abs(first[(6, 3)] - second[(6, 3)]) > 0.1 and abs(first[(4, 6)] - second[(4, 6)]) > 0.05


def test_match_distribution_is_exact_and_symmetric():
    grid, w1, w2, dec = match_distribution(0.65, 0.65, 2)
    assert grid.sum() == pytest.approx(1.0) and w1 == pytest.approx(0.5, abs=1e-9) and w1 + w2 == pytest.approx(1.0)
    swapped = match_distribution(0.62, 0.68, 2)
    base = match_distribution(0.68, 0.62, 2)
    assert base[1] == pytest.approx(swapped[2], abs=1e-9)
    assert base[3] == pytest.approx(swapped[3], abs=1e-9)
    assert np.allclose(base[0], swapped[0].T, atol=1e-9)
    # best of five has a longer distribution than best of three
    g5 = match_distribution(0.65, 0.63, 3)[0]
    assert (g5 * (np.add.outer(np.arange(g5.shape[0]), np.arange(g5.shape[1])))).sum() > (
        base[0] * np.add.outer(np.arange(base[0].shape[0]), np.arange(base[0].shape[1]))).sum()
    # the straight-sets two-set minimum is 12 games, a five-set minimum is 18
    assert g5[:18, :].sum() + g5[:, :18].sum() > 0 and np.all(np.add.outer(np.arange(g5.shape[0]), np.arange(g5.shape[0]))[g5 > 1e-12] >= 18)


def test_form_shock_reduces_deciding_set_rate():
    iid = mix_over_form(0.64, 0.64, 2, 0.0)
    shocked = mix_over_form(0.64, 0.64, 2, 0.05)
    assert iid[3] > 0.45                                          # the retrospective's i.i.d. reproduction: about 0.50
    assert shocked[3] < iid[3] - 0.02
    assert shocked[0].sum() == pytest.approx(1.0) and shocked[1] + shocked[2] == pytest.approx(1.0)
    with pytest.raises(ValueError):
        mix_over_form(0.64, 0.64, 2, -0.1)


def test_calibrate_form_sigma_hits_the_target_rate():
    rng = np.random.default_rng(3)
    population = [(float(np.clip(0.645 + rng.normal(0, 0.03), 0.5, 0.8)), float(np.clip(0.645 + rng.normal(0, 0.03), 0.5, 0.8))) for _ in range(12)]
    target = 0.358
    sigma = calibrate_form_sigma(population, target)
    achieved = float(np.mean([mix_over_form(a, b, 2, sigma)[3] for a, b in population]))
    assert 0.0 < sigma <= 0.12 and achieved == pytest.approx(target, abs=0.003)
    with pytest.raises(ValueError):
        calibrate_form_sigma(population, 0.9)
    with pytest.raises(InsufficientData):
        calibrate_form_sigma([], 0.35)


def test_engine_requires_an_explicit_form_sigma():
    engine = TennisEngine()
    with pytest.raises(MissingInputs, match="form_sigma"):
        engine.predict_distribution({"p_serve1": 0.67, "p_serve2": 0.61})
    dist = engine.predict_distribution({"p_serve1": 0.67, "p_serve2": 0.61, "form_sigma": 0.0})
    assert dist.metadata["form_sigma"] == 0.0 and dist.endpoint == "completed_match"


def test_match_distribution_contracts():
    engine = TennisEngine(form_sigma=0.04)
    dist = engine.predict_distribution({"p_serve1": 0.67, "p_serve2": 0.61, "surface": "hard", "format": "best_of_3"})
    assert dist.grid.sum() == pytest.approx(1.0, abs=1e-6)
    assert dist.p_home_win() > dist.p_away_win() and dist.p_home_win() == dist.p_match_home_win
    assert dist.p_home_win() + dist.p_away_win() == pytest.approx(1.0, abs=1e-9) and dist.p_draw() == 0.0
    contracts = engine.evaluate_contracts(dist, [{"type": "moneyline", "side": "home"}, {"type": "spread", "side": "home", "line": -2.5},
                                                 {"type": "total", "side": "over", "line": 21.5}])
    assert all(0.0 < c.stated_prob < 1.0 for c in contracts)
    assert dist.p_home_cover(2.5) >= dist.p_home_win() - 1e-9
    with pytest.raises(ValueError):
        engine.predict_distribution({"p_serve1": 0.67, "p_serve2": 0.61, "format": "best_of_7"})
    with pytest.raises(ValueError):
        engine.predict_distribution({"p_serve1": 0.67, "p_serve2": 0.61}, endpoint="full_game")


def test_fitting_shrinks_toward_the_tour_average_and_roundtrips_json(tmp_path):
    engine = TennisEngine(form_sigma=0.04).fit(TRAIN)
    assert engine.is_fitted and engine.player_stats["Sinner"]["serve_win_rate"] > 0.65
    assert engine.player_stats["Sinner"]["serve_win_rate"] < 95 / 135                       # shrunk, not the raw rate
    path = str(tmp_path / "tennis_model.json")
    engine.save_artifact(path)
    loaded = TennisEngine.load_artifact(path)
    assert loaded.is_fitted and loaded.form_sigma == 0.04
    assert loaded.player_stats["Sinner"]["serve_win_rate"] == engine.player_stats["Sinner"]["serve_win_rate"]
    with pytest.raises(InsufficientData):
        TennisEngine().fit([{"player1": "A", "player2": "B", "p1_serve_won": 3, "p1_serve_total": 5, "p2_serve_won": 2, "p2_serve_total": 5}])
    with pytest.raises(ValueError):
        TennisEngine().fit({})


def test_opponent_adjusted_return_and_unknown_player_policy():
    train = [
        {"player1": "ServerA", "player2": "AvgGuy", "p1_serve_won": 70, "p1_serve_total": 100, "p2_serve_won": 64, "p2_serve_total": 100},
        {"player1": "ReturnerB", "player2": "AvgGuy", "p1_serve_won": 62, "p1_serve_total": 100, "p2_serve_won": 55, "p2_serve_total": 100},
    ]
    engine = TennisEngine(form_sigma=0.0).fit(train)
    assert engine.player_stats["ReturnerB"]["return_win_rate"] > 0.40
    vs_elite = engine.predict_distribution({"player1": "ServerA", "player2": "ReturnerB"})
    vs_avg = engine.predict_distribution({"player1": "ServerA", "player2": "AvgGuy"})
    assert vs_elite.p_home_win() < vs_avg.p_home_win()
    with pytest.raises(UnknownTeam):                                  # no silent league-average default
        engine.predict_distribution({"player1": "ServerA", "player2": "DefaultGuy"})
    lenient = TennisEngine(form_sigma=0.0, unknown_team_policy="league_average").fit(train)
    dist = lenient.predict_distribution({"player1": "ServerA", "player2": "DefaultGuy"})
    assert dist.metadata["warnings"] and "DefaultGuy" in dist.metadata["warnings"][0]


def test_surface_effects_are_explicit():
    train = TRAIN
    engine = TennisEngine(form_sigma=0.0, surface_effects={"hard": 0.0, "clay": -0.10}).fit(train)
    hard = engine.predict_distribution({"player1": "Sinner", "player2": "Medvedev", "surface": "hard"})
    clay = engine.predict_distribution({"player1": "Sinner", "player2": "Medvedev", "surface": "clay"})
    assert clay.metadata["p_serve1"] < hard.metadata["p_serve1"]
    with pytest.raises(MissingInputs, match="surface"):
        engine.predict_distribution({"player1": "Sinner", "player2": "Medvedev", "surface": "grass"})
    with pytest.raises(MissingInputs):
        TennisEngine(form_sigma=0.0).predict_distribution({"player1": "A", "player2": "B"})

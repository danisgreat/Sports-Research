"""Unit tests for Tennis predictive engine."""

import numpy as np
import pytest

from runtime.src.sports.tennis.engine import TennisEngine
from runtime.src.common.contracts import DerivedContracts


def test_tennis_engine_hold_formula():
    # At p_serve = 0.50, hold prob should be 0.50
    assert np.isclose(TennisEngine.p_game_hold(0.50), 0.50, atol=1e-3)
    # Higher serve win prob implies higher hold prob
    assert TennisEngine.p_game_hold(0.65) > TennisEngine.p_game_hold(0.60)
    assert TennisEngine.p_game_hold(0.70) > 0.80


def test_tennis_engine_match_distribution():
    engine = TennisEngine().fit({})
    dist = engine.predict_distribution({
        "p_serve1": 0.67,
        "p_serve2": 0.61,
        "surface": "hard",
        "format": "best_of_3"
    })

    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)
    
    # Player 1 has higher serve rate -> should be favourite
    p_p1_win = dist.p_home_win()
    p_p2_win = dist.p_away_win()
    assert p_p1_win > p_p2_win

    # Derived contracts evaluation
    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "spread", "side": "home", "line": -2.5},
        {"type": "total", "side": "over", "line": 21.5}
    ])
    assert len(contracts) == 3
    assert 0.0 < contracts[0].stated_prob < 1.0
    assert 0.0 < contracts[1].stated_prob < 1.0
    assert 0.0 < contracts[2].stated_prob < 1.0

    # Covering pair check: P(Home +2.5 games) >= P(Home ML)
    p_plus_2_5 = dist.p_home_cover(2.5)
    assert p_plus_2_5 >= p_p1_win - 1e-9


def test_tennis_moneyline_uses_sets_not_games():
    """Verify that moneyline reflects match-win by sets, decoupling from games-won distribution."""
    engine = TennisEngine()
    # When p_set1 = 0.60, best_of_3 match win probability is 0.6^2 + 2*0.6^2*0.4 = 0.648
    # Even if total games is structured with heavy underdog game accumulation,
    # p_home_win() must return the analytical set-based match win probability.
    dist = engine.predict_distribution({
        "p_serve1": 0.68,
        "p_serve2": 0.60,
        "surface": "hard",
        "format": "best_of_3"
    })

    assert dist.p_match_home_win is not None
    assert dist.p_match_away_win is not None
    assert np.isclose(dist.p_home_win() + dist.p_away_win(), 1.0, atol=1e-5)
    # P(Home win) must reflect the match winner, not games won
    assert dist.p_home_win() == dist.p_match_home_win
    assert dist.p_away_win() == dist.p_match_away_win
    assert dist.p_draw() == 0.0  # No draws in tennis


def test_tennis_fitting_and_serialization(tmp_path):
    """Verify fitting player serve stats and artifact save/load roundtrip."""
    engine = TennisEngine()
    train_matches = [
        {"player1": "Sinner", "player2": "Medvedev", "p1_serve_won": 50, "p1_serve_total": 70, "p2_serve_won": 40, "p2_serve_total": 70},
        {"player1": "Sinner", "player2": "Alcaraz", "p1_serve_won": 45, "p1_serve_total": 65, "p2_serve_won": 42, "p2_serve_total": 65},
    ]
    engine.fit(train_matches)
    assert engine.is_fitted
    assert "Sinner" in engine.player_stats
    assert engine.player_stats["Sinner"]["serve_win_rate"] > 0.65

    # Test serialization
    art_path = str(tmp_path / "tennis_model.pkl")
    engine.save_artifact(art_path)

    loaded = TennisEngine.load_artifact(art_path)
    assert loaded.is_fitted
    assert "Sinner" in loaded.player_stats
    assert loaded.player_stats["Sinner"]["serve_win_rate"] == engine.player_stats["Sinner"]["serve_win_rate"]


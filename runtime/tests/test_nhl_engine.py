"""NHL engine: DST-01 (zero scores), DST-02 (endpoints), DST-05, DST-10, DST-13, ML-08."""

import numpy as np
import pytest

from runtime.src.common.endpoints import HockeyOvertime
from runtime.src.common.errors import InsufficientData, MissingInputs, MissingScore, NotFitted, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.base import EndpointMismatch
from runtime.src.sports.nhl.engine import HockeyLateGame, NHLEngine, late_game_grid


def toy_games(n=40):
    teams = ["A", "B", "C", "D"]
    games = []
    for k in range(n):
        h, a = teams[k % 4], teams[(k + 1 + (k // 4) % 3) % 4]
        games.append({"home_team": h, "away_team": a, "home_goals": [0, 0, 0, 3][k % 4], "away_goals": 0})
    return games


def test_shutouts_are_scores_not_defaults():
    # Home scores are 0,0,0,3 repeating (mean 0.75) and the visitors never score. The old `a or b` coercion turned every 0 into 3.0.
    from runtime.src.common.strengths import AttackDefenceModel
    from runtime.src.sports.base import collect_games
    games = collect_games(toy_games(), ("home_goals",), ("away_goals",))
    assert sum(g[2] for g in games) / len(games) == pytest.approx(0.75, abs=0)
    model = AttackDefenceModel(ridge=1e9).fit(games)
    assert model.league_means()[0] == pytest.approx(0.75, rel=2e-3)     # optimiser tolerance; the old routine gave 2.2
    assert model.league_means()[1] < 1e-3


def test_missing_scores_are_rejected_not_defaulted():
    rows = toy_games() + [{"home_team": "A", "away_team": "B", "home_goals": None}]
    with pytest.raises(MissingScore):
        NHLEngine().fit(rows)
    with pytest.raises(InsufficientData):
        NHLEngine().fit(toy_games(5))
    with pytest.raises(ValueError):
        NHLEngine().fit({})                      # an engine is never "fitted" on nothing


def test_context_only_prediction_needs_both_expected_values():
    engine = NHLEngine()
    dist = engine.predict_distribution({"home_xg": 3.2, "away_xg": 2.7})
    assert dist.endpoint == "regulation" and dist.grid.sum() == pytest.approx(1.0)
    with pytest.raises(MissingInputs):
        engine.predict_distribution({"home_xg": 3.2})
    with pytest.raises(NotFitted):
        engine.predict_distribution({"home_team": "A", "away_team": "B"})
    with pytest.raises(ValueError, match="empty_net_rate"):
        engine.predict_distribution({"home_xg": 3.2, "away_xg": 2.7, "empty_net_rate": 0.22})


def test_unknown_team_refused_or_flagged():
    rng = np.random.default_rng(4)
    teams = [f"T{i}" for i in range(8)]
    games = []
    for _ in range(300):
        h, a = rng.choice(teams, 2, replace=False)
        games.append({"home_team": h, "away_team": a, "home_goals": int(rng.poisson(3.1)), "away_goals": int(rng.poisson(2.9))})
    strict = NHLEngine().fit(games)
    assert strict.predict_distribution({"home_team": "T0", "away_team": "T1"}).grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        strict.predict_distribution({"home_team": "T0", "away_team": "Expansion"})
    lenient = NHLEngine(unknown_team_policy="league_average").fit(games)
    dist = lenient.predict_distribution({"home_team": "T0", "away_team": "Expansion"})
    assert any("Expansion" in w for w in dist.metadata["warnings"])
    # warnings do not leak into the next prediction
    assert NHLEngine._take_warnings(lenient) == []


def test_full_game_endpoint_is_coherent_and_refuses_mismatched_contracts():
    profile = get_profile("ice_hockey", "NHL")
    engine = NHLEngine(league=profile)
    reg = engine.predict_distribution({"home_xg": 3.1, "away_xg": 2.9})
    full = engine.predict_distribution({"home_xg": 3.1, "away_xg": 2.9}, endpoint="full_game")
    assert reg.p_draw() > 0.15
    assert full.p_draw() < 1e-12 and full.p_home_win() + full.p_away_win() == pytest.approx(1.0, abs=1e-12)
    # the archive-derived rule reproduces the observed share of overtime games decided before the shootout
    rule = engine.overtime_rule()
    assert rule.p_decided_in_overtime(profile.mean_total) == pytest.approx(profile.extra("overtime_decided_before_shootout"), abs=1e-9)
    ml = engine.evaluate_contracts(full, [{"type": "moneyline", "side": "home", "endpoint": "full_game"}])[0].stated_prob
    assert ml == pytest.approx(full.p_home_win())
    with pytest.raises(EndpointMismatch):
        engine.evaluate_contracts(reg, [{"type": "moneyline", "side": "home", "endpoint": "full_game"}])
    # playoff sudden death decides by scoring rates alone
    playoff = engine.predict_distribution({"home_xg": 3.1, "away_xg": 2.9, "playoffs": True}, endpoint="full_game")
    assert playoff.p_home_win() == pytest.approx(reg.p_home_win() + reg.p_draw() * 3.1 / 6.0, abs=1e-9)
    with pytest.raises(MissingInputs):
        NHLEngine().predict_distribution({"home_xg": 3.1, "away_xg": 2.9}, endpoint="full_game")
    assert NHLEngine(overtime=HockeyOvertime()).predict_distribution({"home_xg": 3.1, "away_xg": 2.9}, endpoint="full_game").p_draw() < 1e-12


def test_late_game_state_model_moves_mass_toward_two_goal_margins():
    base = NHLEngine().predict_distribution({"home_xg": 3.1, "away_xg": 2.9})
    late = NHLEngine(late_game=HockeyLateGame.ILLUSTRATIVE).predict_distribution({"home_xg": 3.1, "away_xg": 2.9})
    assert late.grid.sum() == pytest.approx(1.0, abs=1e-12)
    assert late.metadata["late_game"] == "state_model" and base.metadata["late_game"] == "none"

    def margin_ge_2(d):
        h, a = np.meshgrid(d.home_support, d.away_support, indexing="ij")
        return float(d.grid[np.abs(h - a) >= 2].sum())

    assert margin_ge_2(late) > margin_ge_2(base)                       # empty-net goals widen margins
    assert sum(late.expected_scores()) > sum(base.expected_scores())   # and add goals
    # with no pulling window effect (zero empty-net rate and no multiplier) the grid matches a plain Poisson end state
    inert = HockeyLateGame(pull_minutes_by_deficit={1: 2.0}, pulled_scoring_multiplier=1.0, empty_net_rate_per_minute=3.1 / 60.0)
    plain = late_game_grid(3.1, 3.1, inert)
    ref = NHLEngine().predict_distribution({"home_xg": 3.1, "away_xg": 3.1}).grid
    assert np.max(np.abs(plain - ref)) < 5e-4                         # the stepwise DP converges to the closed form


def test_artifact_roundtrip_uses_json_not_pickle(tmp_path):
    profile = get_profile("ice_hockey", "NHL")
    rng = np.random.default_rng(1)
    teams = [f"T{i}" for i in range(6)]
    games = [{"home_team": h, "away_team": a, "home_goals": int(rng.poisson(3.1)), "away_goals": int(rng.poisson(2.9))}
             for h, a in (rng.choice(teams, 2, replace=False) for _ in range(250))]
    engine = NHLEngine(league=profile, late_game=HockeyLateGame.ILLUSTRATIVE).fit(games)
    path = tmp_path / "nhl.json"
    document = engine.save_artifact(str(path), {"data_sha256": "abc", "metrics": {"games": 250}})
    assert document["model_card"]["engine"] == "NHLEngine" and document["model_card"]["metrics"] == {"games": 250}
    loaded = NHLEngine.load_artifact(str(path))
    a = engine.predict_distribution({"home_team": "T0", "away_team": "T1"}, endpoint="full_game")
    b = loaded.predict_distribution({"home_team": "T0", "away_team": "T1"}, endpoint="full_game")
    np.testing.assert_allclose(a.grid, b.grid)
    path.write_text(path.read_text().replace('"games": 250', '"games": 251'), encoding="utf-8")
    from runtime.src.common.artifacts import ArtifactError
    with pytest.raises(ArtifactError, match="hash"):
        NHLEngine.load_artifact(str(path))
    pickle_path = tmp_path / "old.pkl"
    pickle_path.write_bytes(b"\x80\x04\x95")
    with pytest.raises(ArtifactError, match="pickle"):
        NHLEngine.load_artifact(str(pickle_path))

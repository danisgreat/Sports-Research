"""Basketball engine: DST-02 (overtime), DST-03 (support), DST-09 (pace x efficiency), DST-13 (no NBA default)."""

import numpy as np
import pytest

from runtime.src.common.errors import MissingInputs, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.base import EndpointMismatch
from runtime.src.sports.basketball.engine import BasketballEngine, bivariate_grid, with_tie_share

NBA = get_profile("basketball", "NBA")


def stats(dist):
    h, a = np.meshgrid(dist.home_support, dist.away_support, indexing="ij")
    mh, ma = (h * dist.grid).sum(), (a * dist.grid).sum()
    return mh, ma, np.sqrt((((h + a) - mh - ma) ** 2 * dist.grid).sum()), np.sqrt((((h - a) - mh + ma) ** 2 * dist.grid).sum())


@pytest.mark.parametrize("mu", [55.0, 62.0, 72.0, 90.0, 112.0, 125.0])
def test_grid_mean_equals_input_mean_for_every_league_scoring_level(mu):
    grid = bivariate_grid(mu, mu - 3.0, 11.0, 11.0, 0.2)
    h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
    assert grid.sum() == pytest.approx(1.0)
    assert (h * grid).sum() == pytest.approx(mu, abs=0.1)
    assert (a * grid).sum() == pytest.approx(mu - 3.0, abs=0.1)


def test_low_scoring_leagues_are_not_truncated():
    # the old fixed 60-160 window gave grid means of 75.1/72.4 for inputs of 72/68
    grid = bivariate_grid(72.0, 68.0, 9.0, 9.0, 0.1)
    h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
    assert (h * grid).sum() == pytest.approx(72.0, abs=0.1) and (a * grid).sum() == pytest.approx(68.0, abs=0.1)


def test_student_t_has_heavier_tails_at_the_same_variance():
    normal, heavy = bivariate_grid(110, 108, 11, 11, 0.2), bivariate_grid(110, 108, 11, 11, 0.2, df=6.0)
    def sd_and_tail(grid):
        h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
        m = h - a
        mu = (m * grid).sum(); sd = np.sqrt(((m - mu) ** 2 * grid).sum())
        return sd, grid[np.abs(m - mu) > 3.0 * sd].sum()
    (sd_n, tail_n), (sd_t, tail_t) = sd_and_tail(normal), sd_and_tail(heavy)
    assert sd_t == pytest.approx(sd_n, rel=0.05) and tail_t > tail_n
    with pytest.raises(ValueError):
        bivariate_grid(110, 108, 11, 11, 0.2, df=2.0)
    with pytest.raises(ValueError):
        bivariate_grid(110, 108, 11, 11, 1.0)


def test_nba_full_game_reproduces_the_profile_moments():
    engine = BasketballEngine(league=NBA)
    ctx = {"home_expected_points": NBA.mean_home, "away_expected_points": NBA.mean_away}
    full = engine.predict_distribution(ctx, endpoint="full_game")
    mh, ma, total_sd, margin_sd = stats(full)
    assert mh == pytest.approx(NBA.mean_home, abs=0.05) and ma == pytest.approx(NBA.mean_away, abs=0.05)
    assert total_sd == pytest.approx(NBA.total_sd, rel=0.01) and margin_sd == pytest.approx(NBA.margin_sd, rel=0.01)
    assert full.endpoint == "full_game" and full.p_draw() < 1e-9
    reg = engine.predict_distribution(ctx, endpoint="regulation")
    assert reg.p_draw() > 0.02                                          # regulation keeps its ties (the ~4.7% of games that reach OT)
    assert reg.p_draw() == pytest.approx(NBA.extra("overtime_share"), abs=0.002)      # calibrated to the archive overtime rate
    assert sum(reg.expected_scores()) < sum(full.expected_scores())    # overtime adds points
    # the shared-pace correlation is positive for the NBA, so totals are wider than independent teams would give
    assert full.metadata["structure_corr"] > 0.0


def test_pace_times_efficiency_defines_the_means():
    engine = BasketballEngine(league=NBA)
    d = engine.predict_distribution({"pace": 99.0, "home_ppp": 1.17, "away_ppp": 1.14, "mean_basis": "final"}, endpoint="regulation")
    assert d.metadata["target_home"] == pytest.approx(99.0 * 1.17) and d.metadata["target_away"] == pytest.approx(99.0 * 1.14)
    with pytest.raises(MissingInputs):
        engine.predict_distribution({"pace": 99.0, "home_ppp": 1.17})


def test_other_leagues_never_borrow_an_nba_default():
    with pytest.raises(MissingInputs, match="no NBA default"):
        BasketballEngine().predict_distribution({"home_expected_points": 80, "away_expected_points": 78})
    wnba = BasketballEngine(league=get_profile("basketball", "WNBA"))
    d = wnba.predict_distribution({"home_expected_points": 82.8, "away_expected_points": 81.2}, endpoint="full_game")
    assert d.metadata["regulation_minutes"] == 40.0
    with pytest.raises(MissingInputs, match="regulation_minutes"):
        BasketballEngine(total_sd=18.0, margin_sd=15.0).predict_distribution(
            {"home_expected_points": 80, "away_expected_points": 78}, endpoint="full_game")


def test_explicit_regulation_inputs_skip_calibration():
    engine = BasketballEngine(league=NBA)
    d = engine.predict_distribution({"home_expected_points": 112.0, "away_expected_points": 109.0, "mean_basis": "latent",
                                     "sd_home": 11.0, "sd_away": 11.0, "pace_correlation": 0.2})
    assert d.metadata["endpoint_basis"] == "regulation_latent"
    assert stats(d)[0] == pytest.approx(112.0, abs=0.1)
    d_scaled = engine.predict_distribution({"home_expected_points": 112.0, "away_expected_points": 109.0, "mean_basis": "latent",
                                            "sd_home": 11.0, "sd_away": 11.0, "scoring_multiplier": 0.97})
    assert stats(d_scaled)[0] == pytest.approx(112.0 * 0.97, abs=0.1)


def test_contract_endpoint_is_enforced():
    engine = BasketballEngine(league=NBA)
    ctx = {"home_expected_points": NBA.mean_home, "away_expected_points": NBA.mean_away}
    reg = engine.predict_distribution(ctx)
    with pytest.raises(EndpointMismatch):
        engine.evaluate_contracts(reg, [{"type": "moneyline", "side": "home", "endpoint": "full_game"}])
    full = engine.predict_distribution(ctx, endpoint="full_game")
    got = engine.evaluate_contracts(full, [{"type": "total", "side": "over", "line": 228.5, "endpoint": "full_game"}])[0].stated_prob
    assert 0.2 < got < 0.8


def test_fit_and_unknown_team_policy():
    rng = np.random.default_rng(3)
    teams = [f"T{i}" for i in range(8)]
    games = []
    for h, a in (rng.choice(teams, 2, replace=False) for _ in range(500)):
        games.append({"home_team": h, "away_team": a, "home_score": int(rng.normal(112, 11)), "away_score": int(rng.normal(109, 11))})
    engine = BasketballEngine(regulation_minutes=48.0).fit(games)
    assert 14 < engine.total_sd < 22 and 11 < engine.margin_sd < 18
    d = engine.predict_distribution({"home_team": "T0", "away_team": "T1"}, endpoint="full_game")
    assert d.grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"home_team": "T0", "away_team": "Expansion"})


def test_tie_share_rescaling_conserves_mass_and_only_changes_ties():
    grid = bivariate_grid(112.0, 110.0, 11.0, 11.0, 0.2)
    n = min(grid.shape)
    base_tie = float(np.trace(grid[:n, :n]))
    scaled = with_tie_share(grid, 0.047)
    assert scaled.sum() == pytest.approx(1.0) and float(np.trace(scaled[:n, :n])) == pytest.approx(0.047)
    off = ~np.eye(n, dtype=bool)
    ratio = scaled[:n, :n][off & (grid[:n, :n] > 1e-9)] / grid[:n, :n][off & (grid[:n, :n] > 1e-9)]
    assert np.allclose(ratio, (1 - 0.047) / (1 - base_tie))
    with pytest.raises(ValueError):
        with_tie_share(grid, 0.7)

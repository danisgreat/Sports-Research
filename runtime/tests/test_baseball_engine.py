"""Baseball engine: DST-01/02/08/13."""

import time

import numpy as np
import pytest

from runtime.src.common.errors import MissingInputs, MissingScore, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.baseball.engine import BaseballEngine, game_grid, game_grid_reference, innings_pmf

MLB = get_profile("baseball", "MLB")
PMF = [MLB.extras[f"extra_inning_runs_p{r}"] for r in range(6)]


def one_run_share_decided(dist):
    h, a = np.meshgrid(dist.home_support, dist.away_support, indexing="ij")
    return float(dist.grid[np.abs(h - a) == 1].sum() / dist.grid[h != a].sum())


def moments(dist):
    h, a = np.meshgrid(dist.home_support, dist.away_support, indexing="ij")
    mh, ma = (h * dist.grid).sum(), (a * dist.grid).sum()
    total_sd = np.sqrt((((h + a) - mh - ma) ** 2 * dist.grid).sum())
    margin_sd = np.sqrt((((h - a) - mh + ma) ** 2 * dist.grid).sum())
    return mh, ma, total_sd, margin_sd


@pytest.mark.parametrize("args", [(4.5, 4.4, 0.3, 0.275), (2.0, 7.0, 0.1, 0.0), (6.0, 1.5, 0.5, 1.0)])
def test_vectorised_grid_matches_the_loop_oracle(args):
    assert np.max(np.abs(game_grid(*args) - game_grid_reference(*args))) < 1e-10
    assert np.max(np.abs(game_grid(*args, ninth_factor=0.6) - game_grid_reference(*args, ninth_factor=0.6))) < 1e-10


def test_game_grid_conserves_mass_and_the_home_ninth_is_conditional():
    grid = game_grid(4.5, 4.5, 0.3, 0.275)
    assert grid.sum() == pytest.approx(1.0, abs=1e-12)
    h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
    # equal teams: the home side skips the bottom of the ninth when ahead, so it scores fewer runs on average
    assert (grid * h).sum() < (grid * a).sum() - 0.05
    with pytest.raises(ValueError):
        BaseballEngine(environment_sigma=0.07, total_sd=4.4, margin_sd=4.5).predict_distribution(
            {"home_expected_runs": 4.5, "away_expected_runs": 4.5}, endpoint="x")


def test_starter_leash_is_a_mixture_not_a_fixed_5_2():
    support, weights = innings_pmf(5.5, 1.3)
    assert weights.sum() == pytest.approx(1.0) and support[0] == 1 and support[-1] == 8
    assert (support * weights).sum() == pytest.approx(5.5, abs=0.15)
    engine = BaseballEngine(environment_sigma=0.07, total_sd=4.47, margin_sd=4.52, starter_ip_sd=1.3)
    common = {"home_expected_runs": 4.4, "away_expected_runs": 4.4, "league_ra9": 4.4}
    ctx = {**common, "away_sp_ra9": 3.2, "away_bp_ra9": 4.4, "away_sp_expected_ip": 6.0,
           "home_sp_ra9": 4.4, "home_bp_ra9": 4.4, "home_sp_expected_ip": 6.0}
    ace = engine.predict_distribution(ctx)
    plain = engine.predict_distribution(common)
    assert ace.expected_scores()[0] < plain.expected_scores()[0]       # facing an ace: the home side scores less
    with pytest.raises(MissingInputs):
        engine.predict_distribution({**common, "away_sp_ra9": 3.2})


def test_calibration_reproduces_the_target_moments():
    engine = BaseballEngine(league=MLB)
    dist = engine.predict_distribution({"home_expected_runs": MLB.mean_home, "away_expected_runs": MLB.mean_away}, endpoint="full_game")
    mh, ma, total_sd, margin_sd = moments(dist)
    assert mh == pytest.approx(MLB.mean_home, rel=2e-3) and ma == pytest.approx(MLB.mean_away, rel=2e-3)
    assert total_sd == pytest.approx(MLB.total_sd, rel=5e-3) and margin_sd == pytest.approx(MLB.margin_sd, rel=5e-3)
    meta = dist.metadata
    assert meta["latent_mean_home"] > MLB.mean_home * 0.99 and 0.0 <= meta["matchup_tau"] < 0.6


def test_matchup_shock_widens_margins_not_totals():
    base = BaseballEngine(environment_sigma=0.0, total_sd=4.47, margin_sd=4.52)
    wide = BaseballEngine(environment_sigma=0.0, total_sd=4.47, margin_sd=5.2)
    ctx = {"home_expected_runs": 4.4, "away_expected_runs": 4.4}
    d0, d1 = base.predict_distribution(ctx), wide.predict_distribution(ctx)
    m0, m1 = moments(d0), moments(d1)
    assert m1[3] > m0[3] + 0.4 and m1[2] == pytest.approx(m0[2], rel=0.01)


def test_one_run_share_falls_as_the_expected_total_rises():
    engine = BaseballEngine(league=MLB)
    shares = [one_run_share_decided(engine.predict_distribution({"home_expected_runs": m, "away_expected_runs": m, "mean_basis": "latent",
                                                                 "matchup_tau": 0.12, "latent_dispersion_phi": 0.27}, endpoint="full_game"))
              for m in (3.0, 4.0, 5.0, 6.0)]
    assert all(a > b for a, b in zip(shares, shares[1:]))              # high-run environments widen margins (fixes the P-547 issue)


def test_league_average_game_against_the_archive_shape():
    """Documented validation of DST-08: moments are matched; the margin SHAPE is within ~3 points of the archive."""
    engine = BaseballEngine(league=MLB)
    dist = engine.predict_distribution({"home_expected_runs": MLB.mean_home, "away_expected_runs": MLB.mean_away}, endpoint="full_game")
    assert dist.p_draw() < 1e-12                                       # MLB has no ties
    assert one_run_share_decided(dist) == pytest.approx(MLB.extra("one_run_share"), abs=0.03)   # observed gap is ~+2.1 points
    assert dist.p_home_win() == pytest.approx(MLB.extra("home_win_share"), abs=0.02)
    assert dist.metadata["p_tie_after_nine"] == pytest.approx(MLB.extra("extra_innings_share"), abs=0.02)   # observed gap ~+1.2 points


def test_tie_leagues_keep_ties_and_require_the_rulebook_cap():
    profile = get_profile("baseball", "NPB")
    engine = BaseballEngine(league=profile)
    ctx = {"home_expected_runs": profile.mean_home, "away_expected_runs": profile.mean_away, "extra_inning_pmf": PMF}
    with pytest.raises(MissingInputs, match="innings_cap"):
        engine.predict_distribution(ctx, endpoint="full_game")
    capped = engine.predict_distribution({**ctx, "innings_cap": 3}, endpoint="full_game")
    reg = engine.predict_distribution({**ctx, "innings_cap": 3})
    assert 0.0 < capped.p_draw() < reg.p_draw()
    assert capped.grid.sum() == pytest.approx(1.0, abs=1e-12)


def test_fit_rejects_missing_scores_and_zero_runs_count():
    rng = np.random.default_rng(2)
    teams = [f"T{i}" for i in range(6)]
    games = [{"home_team": h, "away_team": a, "home_runs": int(rng.poisson(4.4)), "away_runs": int(rng.poisson(4.3))}
             for h, a in (rng.choice(teams, 2, replace=False) for _ in range(400))]
    games[0]["home_runs"] = 0
    engine = BaseballEngine(environment_sigma=0.07).fit(games)
    assert engine.total_sd > 0 and engine.margin_sd > 0 and engine.is_fitted
    realistic = {"total_sd": MLB.total_sd, "margin_sd": MLB.margin_sd}      # the synthetic Poisson residuals are not baseball-shaped
    ok = engine.predict_distribution({"home_team": "T0", "away_team": "T1", **realistic})
    assert ok.grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"home_team": "T0", "away_team": "Nobody", **realistic})
    with pytest.raises(MissingInputs):                                  # fitted, but no environment sigma anywhere
        BaseballEngine().fit(games).predict_distribution({"home_team": "T0", "away_team": "T1", **realistic})
    from runtime.src.common.errors import FitFailed
    with pytest.raises(FitFailed, match="did not reach its targets"):   # moments the structure cannot produce are refused, not approximated
        engine.predict_distribution({"home_team": "T0", "away_team": "T1"})
    with pytest.raises(MissingScore):
        BaseballEngine().fit(games + [{"home_team": "T0", "away_team": "T1", "home_runs": None, "away_runs": 2}])


def test_prediction_with_starters_is_fast_enough_for_card_use():
    engine = BaseballEngine(league=MLB)
    ctx = {"home_expected_runs": 4.4, "away_expected_runs": 4.4, "away_sp_ra9": 3.8, "away_bp_ra9": 4.2, "away_sp_expected_ip": 5.5,
           "home_sp_ra9": 4.0, "home_bp_ra9": 4.3, "home_sp_expected_ip": 5.8}
    engine.predict_distribution({k: ctx[k] for k in ("home_expected_runs", "away_expected_runs")})   # warm the structure cache
    started = time.perf_counter()
    engine.predict_distribution(ctx)
    assert time.perf_counter() - started < 15.0

"""Cricket engine (DST-11): exact dynamic program, chase stopping rule with overshoot, toss branch, phase rows."""

import itertools

import numpy as np
import pytest

from runtime.src.common.errors import InsufficientData, MissingInputs, NotFitted, UnknownTeam
from runtime.src.sports.cricket.engine import (
    CricketEngine, CricketFormat, PhaseRates, ball_pmf, calibrate_run_multiplier, chase_grid, run_innings,
)

T20 = CricketFormat.t20_illustrative()


def tiny_format(balls=3, depth=0.0):
    pmf = (0.30, 0.30, 0.10, 0.02, 0.12, 0.10, 0.06)
    return CricketFormat("tiny", balls, (PhaseRates("all", 0, balls, pmf),), wicket_depth_effect=depth, max_runs=60)


def test_innings_dp_matches_brute_force_enumeration():
    fmt = tiny_format(balls=3)
    table = run_innings(fmt)
    runs = {}
    pmf = np.array(fmt.phases[0].pmf)
    values = [0, 1, 2, 3, 4, 6, None]
    for combo in itertools.product(range(7), repeat=3):
        p = float(np.prod([pmf[i] for i in combo]))
        total = sum(values[i] for i in combo if values[i] is not None)
        runs[total] = runs.get(total, 0.0) + p
    got = table.runs_pmf()
    for total, p in runs.items():
        assert got[total] == pytest.approx(p, abs=1e-12)
    assert got.sum() == pytest.approx(1.0)


def test_innings_dp_matches_a_ball_by_ball_simulation():
    fmt = CricketFormat("short", 60, (PhaseRates("pp", 0, 24, T20.phases[0].pmf), PhaseRates("rest", 24, 60, T20.phases[2].pmf)),
                        wicket_depth_effect=0.04, max_runs=200)
    table = run_innings(fmt, run_multiplier=1.05, wicket_multiplier=1.1)
    rng = np.random.default_rng(0)
    n = 200000
    cumulative = {}
    for ph in fmt.phases:
        cumulative[ph.name] = np.cumsum([ball_pmf(ph, w, fmt.wicket_depth_effect, 1.05, 1.1) for w in range(10)], axis=1)
    runs = np.zeros(n, dtype=int)
    wickets = np.zeros(n, dtype=int)
    run_values = np.array([0, 1, 2, 3, 4, 6, 0])
    for ball in range(fmt.balls):
        live = wickets < 10
        table_c = cumulative[fmt.phase_of(ball).name][np.minimum(wickets, 9)]
        outcome = (rng.random(n)[:, None] > table_c).sum(axis=1)
        outcome = np.minimum(outcome, 6)
        runs += np.where(live, run_values[outcome], 0)
        wickets += np.where(live & (outcome == 6), 1, 0)
    values = np.arange(fmt.max_runs + 1)
    pmf = table.runs_pmf()
    mean = float(values @ pmf)
    assert runs.mean() == pytest.approx(mean, abs=0.25)
    assert runs.std() == pytest.approx(float(np.sqrt(((values - mean) ** 2) @ pmf)), rel=0.02)
    assert (wickets == 10).mean() == pytest.approx(table.wickets_pmf(60)[10], abs=0.005)


def test_chase_stops_at_the_target_with_boundary_overshoot():
    first, second = run_innings(T20), run_innings(T20)
    grid = chase_grid(first, second)
    assert grid.sum() == pytest.approx(1.0, abs=1e-9)
    for s1 in range(0, 200, 7):
        # the chasing innings can never finish above target + 5 (target = s1 + 1, so s2 <= s1 + 6)
        assert grid[s1, s1 + 7:].sum() < 1e-12
    mass_at = lambda s1, s2: grid[s1, s2] / first.runs_pmf()[s1]
    assert mass_at(150, 151) > 0 and mass_at(150, 156) > 0                  # finishing on the target and a six overshoot both occur
    assert mass_at(150, 156) < mass_at(150, 151)
    # an unrestricted pair of totals would put far more mass above s1 + 1 (the old model's rejected independence)
    unrestricted = np.outer(first.runs_pmf(), second.runs_pmf())
    h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
    assert unrestricted[a > h + 6].sum() > 0.2 and grid[a > h + 6].sum() < 1e-12


def test_first_passage_lands_in_the_five_run_window_above_the_target():
    table = run_innings(T20)
    for target in (90, 150, 190):
        reach = table.first_passage(target)
        assert reach[:target].sum() == 0 and reach[target + 6:].sum() == 0
        # P(reach) + P(finish short) = 1
        assert reach.sum() + table.runs_pmf()[:target].sum() == pytest.approx(1.0, abs=1e-9)


def test_phase_rows_come_from_the_same_simulation_as_the_total():
    table = run_innings(T20)
    values = np.arange(T20.max_runs + 1)
    after_pp = table.runs_pmf(36)
    final = table.runs_pmf()
    mean_pp, mean_final = float(values @ after_pp), float(values @ final)
    assert 40 < mean_pp < 62 and mean_final > mean_pp + 60
    # runs in the death overs = final - powerplay-middle: the three phases tile the innings exactly
    assert float(values @ table.runs_pmf(96)) < mean_final
    assert table.wickets_pmf(120)[10] > 0.0 and table.wickets_pmf(36).sum() == pytest.approx(1.0)
    # more wickets lost lowers later scoring (batting depth)
    assert ball_pmf(T20.phases[2], 7, 0.04, 1.0, 1.0)[5] < ball_pmf(T20.phases[2], 0, 0.04, 1.0, 1.0)[5]


def test_run_multiplier_calibration_hits_the_expected_total():
    m = calibrate_run_multiplier(T20, 175.0)
    values = np.arange(T20.max_runs + 1)
    assert float(values @ run_innings(T20, m).runs_pmf()) == pytest.approx(175.0, abs=0.05) and m > 1.0
    with pytest.raises(ValueError):
        calibrate_run_multiplier(T20, 400.0)


def test_toss_is_an_explicit_branch_and_the_mixture_is_exact():
    engine = CricketEngine({"t20": T20})
    base = {"format": "t20", "home_expected_runs": 172.0, "away_expected_runs": 160.0}
    with pytest.raises(MissingInputs, match="never assumed"):
        engine.predict_distribution(base)
    home_first = engine.predict_distribution({**base, "bat_first": "home"})
    away_first = engine.predict_distribution({**base, "bat_first": "away"})
    mix = engine.predict_distribution({**base, "p_home_bats_first": 0.3})
    np.testing.assert_allclose(mix.grid, 0.3 * home_first.grid + 0.7 * away_first.grid, atol=1e-12)
    assert home_first.p_home_win() > 0.5 and home_first.grid.sum() == pytest.approx(1.0)
    assert mix.p_home_win() == pytest.approx(0.3 * home_first.p_home_win() + 0.7 * away_first.p_home_win(), abs=1e-12)
    # tie mass is a real cell (super over), not folded into a win
    assert home_first.p_draw() > 0.0
    with pytest.raises(ValueError):
        engine.predict_distribution({**base, "p_home_bats_first": 1.5})


def test_chase_asymmetry_is_visible_in_contract_prices():
    engine = CricketEngine({"t20": T20})
    ctx = {"format": "t20", "home_expected_runs": 165.0, "away_expected_runs": 165.0}
    first = engine.predict_distribution({**ctx, "bat_first": "home"})
    second = engine.predict_distribution({**ctx, "bat_first": "away"})
    assert first.p_home_win() + first.p_away_win() + first.p_draw() == pytest.approx(1.0)
    assert abs(first.p_home_win() - (1.0 - second.p_home_win() - second.p_draw())) < 0.05
    # chase rows: P(away passes the target) is not the product of independent totals
    assert 0.3 < first.p_over(330.5) < 0.5                        # two 165-run innings: a 330.5 total is near the median


def test_reduced_overs_branch_uses_the_supplied_resource_ratio():
    engine = CricketEngine({"t20": T20})
    ctx = {"format": "t20", "home_expected_runs": 170.0, "away_expected_runs": 170.0, "bat_first": "home"}
    fair = engine.reduced_overs_chase(ctx, overs_second_innings=14, resource_ratio=0.82)
    harsh = engine.reduced_overs_chase(ctx, overs_second_innings=14, resource_ratio=1.0)
    assert fair["chasing_side_wins"] + fair["defending_side_wins"] == pytest.approx(1.0)
    assert fair["chasing_side_wins"] > harsh["chasing_side_wins"]            # a lower par target helps the chaser
    full = engine.reduced_overs_chase(ctx, overs_second_innings=20, resource_ratio=1.0)
    assert full["chasing_side_wins"] > harsh["chasing_side_wins"]            # more overs for the same target helps too
    with pytest.raises(ValueError):
        engine.reduced_overs_chase(ctx, 14, 0.0)


def test_fit_unknown_formats_and_unfitted_use():
    engine = CricketEngine({"t20": T20})
    rng = np.random.default_rng(6)
    teams = ["IND", "AUS", "ENG", "PAK"]
    matches = [{"format": "t20", "home_team": h, "away_team": a, "home_runs": int(rng.normal(165, 20)), "away_runs": int(rng.normal(160, 20))}
               for h, a in (rng.choice(teams, 2, replace=False) for _ in range(120))]
    engine.fit(matches)
    dist = engine.predict_distribution({"format": "t20", "home_team": "IND", "away_team": "AUS", "bat_first": "home"})
    assert dist.grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"format": "t20", "home_team": "IND", "away_team": "NED", "bat_first": "home"})
    with pytest.raises(MissingInputs):
        engine.predict_distribution({"format": "odi", "home_expected_runs": 280, "away_expected_runs": 270, "bat_first": "home"})
    with pytest.raises(NotFitted):
        CricketEngine({"t20": T20}).predict_distribution({"format": "t20", "bat_first": "home"})
    with pytest.raises(InsufficientData):
        CricketEngine({"t20": T20}).fit(matches[:5])
    with pytest.raises(ValueError):
        CricketEngine({"t20": T20}).fit({})
    with pytest.raises(ValueError):
        CricketFormat("bad", 120, (PhaseRates("a", 0, 60, T20.phases[0].pmf),), 0.04, 300)     # phases must tile the innings

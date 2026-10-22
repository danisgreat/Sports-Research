"""SIM-v2: seeded simulators for path-dependent contracts. Development parameters only; nothing here is sporting evidence."""
import numpy as np
import pytest

from ml.sim import baseball, core, cricket, hockey, props, tennis


# ------------------------------------------------------------------ core
def test_a_seed_and_a_card_sized_n_are_required():
    with pytest.raises(core.SimulationError, match="seed is required"):
        core.rng(None)
    with pytest.raises(core.SimulationError, match="below the card minimum"):
        core.check_n(50_000)
    assert core.check_n(100_000) == 100_000 and core.check_n(10, card=False) == 10


def test_probability_and_standard_error():
    r = core.probability(np.array([True] * 30 + [False] * 70), seed=1)
    assert r["p"] == 0.3 and abs(r["se"] - np.sqrt(0.3 * 0.7 / 100)) < 1e-12
    d = core.decisive(np.array([1, 1, 0, 0, 0], bool), np.array([0, 0, 1, 0, 0], bool), seed=2)
    assert d["p"] == pytest.approx(0.4) and d["p_decisive"] == pytest.approx(2 / 3)


def test_a_probability_within_three_standard_errors_of_a_gate_is_unresolved():
    assert core.unresolved(0.62, 0.005, 0.62) and core.unresolved(0.63, 0.005, 0.62)
    assert not core.unresolved(0.70, 0.005, 0.62)


# ------------------------------------------------------------------ baseball
def test_baseball_environment_must_be_a_distribution():
    with pytest.raises(core.SimulationError):
        baseball.Environment(probs=(0.5, 0.2, 0.2, 0.2, 0.0, 0.0))
    with pytest.raises(core.SimulationError):
        baseball.scale(baseball.Environment(), 100.0)


def test_baseball_scale_to_runs_hits_the_target():
    env = baseball.scale_to_runs(baseball.Environment(), 4.0, n=60_000, seed=3)
    assert baseball.mean_runs_per_game(env, 60_000, 3) == pytest.approx(4.0, abs=0.06)


def test_baseball_reproduces_extras_walk_offs_and_one_run_games():
    env = baseball.Environment()
    result = baseball.simulate_game(env, env, 40_000, 11, card=False)
    shares = baseball.structure_check(result)
    # A symmetric normal with the same mean and SD gives about 17% one-run games; the inning chain gives the observed ~28%.
    assert 0.24 < shares["one_run_share"] < 0.34
    assert 0.06 < shares["extras_share"] < 0.14 and shares["walk_off_share"] > 0.05
    assert (result["home"] != result["away"]).all()       # every game is settled
    assert abs(shares["home_win"] - 0.5) < 0.02


def test_baseball_home_team_does_not_bat_when_leading_after_the_top_of_the_ninth():
    env = baseball.Environment()
    result = baseball.simulate_game(env, baseball.scale(env, 0.4), 20_000, 5, card=False)
    assert (result["home"] > result["away"]).mean() > 0.6         # the stronger home team wins more
    assert result["innings"].min() == 9


def test_baseball_is_reproducible_and_seed_sensitive():
    env = baseball.Environment()
    a = baseball.simulate_game(env, env, 5_000, 7, card=False)
    b = baseball.simulate_game(env, env, 5_000, 7, card=False)
    c = baseball.simulate_game(env, env, 5_000, 8, card=False)
    assert (a["home"] == b["home"]).all() and (a["away"] == b["away"]).all()
    assert (a["home"] != c["home"]).any()


def test_baseball_grid_prices_contracts_with_the_standard_code():
    env = baseball.Environment()
    game = baseball.simulate_game(env, env, 30_000, 2, card=False)
    grid = core.histogram_grid(game["home"], game["away"])
    m = grid.handicap(-1.5, "HOME")
    assert m.win + m.push + m.loss == pytest.approx(1.0) and m.push == 0.0       # a half-line never pushes
    over = grid.total(8.5, "OVER")
    assert 0.3 < over.win < 0.7


# ------------------------------------------------------------------ tennis
def test_tennis_game_and_tiebreak_closed_forms():
    assert tennis.p_game(0.5) == pytest.approx(0.5)
    assert tennis.p_game(0.6) == pytest.approx(0.7357, abs=1e-3)
    assert tennis.p_tiebreak(0.6, 0.6, True) == pytest.approx(0.5, abs=0.03)
    assert tennis.p_tiebreak(0.7, 0.55, True) > 0.5


def test_tennis_exact_recursion_is_a_distribution_and_symmetric():
    r = tennis.match(0.65, 0.65, 3)
    assert r["games_grid"].sum() == pytest.approx(1.0) and sum(r["set_scores"].values()) == pytest.approx(1.0)
    assert r["p_a"] == pytest.approx(0.5, abs=0.015)          # equal players, only the opening server differs
    assert tennis.match(0.70, 0.62, 3)["p_a"] > tennis.match(0.65, 0.62, 3)["p_a"] > 0.5


def test_tennis_exact_recursion_agrees_with_monte_carlo():
    exact = tennis.match(0.65, 0.62, 3)
    mc = tennis.simulate_match(0.65, 0.62, 3, 12_000, seed=4)
    assert abs(exact["p_a"] - mc["p_a"]) < 0.012
    tv, tp = tennis.games_grid(exact).total_pmf()
    assert abs(float(tv @ tp) - mc["mean_total_games"]) < 0.25


def test_tennis_best_of_five_favours_the_stronger_player_more():
    assert tennis.match(0.68, 0.62, 5)["p_a"] > tennis.match(0.68, 0.62, 3)["p_a"]


def test_tennis_form_shock_widens_and_sigma_zero_is_the_iid_chain():
    base = tennis.match(0.68, 0.60, 3)
    assert tennis.with_form_shock(0.68, 0.60, 0.0)["p_a"] == base["p_a"]
    shocked = tennis.with_form_shock(0.68, 0.60, 0.20)
    assert shocked["p_a"] < base["p_a"]                      # more variance pulls a favourite towards one half
    var = lambda r: (lambda tv, tp: float(((tv - tv @ tp) ** 2) @ tp))(*tennis.games_grid(r).total_pmf())
    assert var(shocked) > var(base)
    with pytest.raises(core.SimulationError):
        tennis.with_form_shock(0.65, 0.6, -0.1)


def test_tennis_set_handicap_and_match_winner_are_different_questions():
    r = tennis.match(0.66, 0.62, 3)
    h = tennis.set_handicap(r, -1.5, "A")                      # A must win 2-0
    assert h["w"] + h["p"] + h["l"] == pytest.approx(1.0) and h["w"] < r["p_a"]
    g = tennis.games_grid(r).handicap(-3.5, "HOME")
    assert g.win < tennis.match(0.66, 0.62, 3)["p_a"] + 1e-9   # covering a games line does not imply winning the match... or more


def test_tennis_super_tiebreak_final_set_is_supported():
    r = tennis.match(0.65, 0.62, 3, final_set="super_tb10")
    assert r["games_grid"].sum() == pytest.approx(1.0)
    with pytest.raises(core.SimulationError):
        tennis.match(0.65, 0.62, 4)


# ------------------------------------------------------------------ hockey
def _late(multiplier=1.0, empty=0.0):
    return hockey.LateGame(pull_minutes=1.5, pull_attack_multiplier=multiplier, empty_net_rate_per_min=empty)


def test_hockey_without_pull_effects_matches_a_poisson_game():
    r = hockey.simulate_game(3.0, 3.0, 60_000, 21, hockey.LateGame(1.5, 1.0, 3.0 / 60), ot_rate_per_min=0.3, card=False)
    assert abs(r["reg_home"].mean() - 3.0) < 0.03 and abs(r["reg_away"].mean() - 3.0) < 0.03
    margin = np.abs(r["home"] - r["away"])
    assert margin.min() >= 1                                   # every game is decided by at least one goal
    assert abs((r["home"] > r["away"]).mean() - 0.5) < 0.01


def test_hockey_empty_net_play_turns_one_goal_games_into_two_goal_games():
    plain = hockey.structure_check(hockey.simulate_game(3.0, 3.0, 60_000, 22, hockey.LateGame(1.5, 1.0, 3.0 / 60), ot_rate_per_min=0.3, card=False))
    pulled = hockey.structure_check(hockey.simulate_game(3.0, 3.0, 60_000, 22, hockey.LateGame(1.5, 2.5, 0.25), ot_rate_per_min=0.3, card=False))
    # (with multiplier 1 and an ordinary scoring rate the "pull" changes nothing, but the late goals are still counted)
    assert pulled["empty_net_goal_share"] > 0.05 and pulled["empty_net_goal_share"] > 3 * plain["empty_net_goal_share"]
    assert pulled["two_goal_share"] > plain["two_goal_share"]
    assert pulled["regulation_tie_share"] > plain["regulation_tie_share"]      # the pulled goalie ties more games


def test_hockey_rejects_bad_parameters_and_small_n():
    with pytest.raises(core.SimulationError):
        hockey.simulate_game(3.0, 3.0, 1000, 1, _late(), ot_rate_per_min=0.3)
    with pytest.raises(core.SimulationError):
        hockey.simulate_game(-1.0, 3.0, 1000, 1, _late(), ot_rate_per_min=0.3, card=False)


# ------------------------------------------------------------------ cricket
TABLE = {"all": (1, 120, {"0": 0.35, "1": 0.35, "2": 0.05, "4": 0.1, "6": 0.07, "W": 0.04, "X": 0.04})}


def test_cricket_table_validation():
    with pytest.raises(core.SimulationError, match="sum to 1"):
        cricket.simulate_innings({"all": (1, 120, {"0": 0.5, "1": 0.2})}, 100, 1, card=False)
    with pytest.raises(core.SimulationError, match="cover every legal delivery"):
        cricket.simulate_innings({"pp": (1, 36, {"0": 0.5, "1": 0.5})}, 100, 1, card=False)
    with pytest.raises(core.SimulationError, match="overlap"):
        cricket.simulate_innings({"a": (1, 80, {"0": 1.0}), "b": (60, 120, {"0": 1.0})}, 100, 1, card=False)


def test_cricket_innings_total_matches_the_expected_value_of_the_table():
    r = cricket.simulate_innings(TABLE, 30_000, 8, card=False)
    per_ball = 0.35 * 0 + 0.35 * 1 + 0.05 * 2 + 0.1 * 4 + 0.07 * 6 + 0.04 * 1          # X adds a run without using a ball
    legal = 1 - 0.04
    expected_balls = 120.0            # almost no innings end on wickets at this rate, so use the observed mean below
    assert abs(r["runs"].mean() - (per_ball / legal) * r["balls"].mean()) < 1.0
    assert (r["balls"] <= 120).all() and (r["wickets"] <= 10).all()


def test_cricket_chase_stops_at_the_target_and_is_monotone_in_it():
    low = cricket.simulate_innings(TABLE, 20_000, 9, target=120, card=False)
    high = cricket.simulate_innings(TABLE, 20_000, 9, target=200, card=False)
    assert low["chase_won"].mean() > high["chase_won"].mean()
    assert (low["runs"][low["chase_won"]] >= 120).all()
    assert low["runs"][low["chase_won"]].max() <= 120 + 6 + 1          # stops within one delivery of the target


def test_cricket_wicket_factors_change_the_total():
    base = cricket.simulate_innings(TABLE, 20_000, 10, card=False)
    fragile = cricket.simulate_innings(TABLE, 20_000, 10, wicket_prob_factor=[3.0] * 11, card=False)
    assert fragile["runs"].mean() < base["runs"].mean() and (fragile["wickets"] >= 10).mean() > (base["wickets"] >= 10).mean()


# ------------------------------------------------------------------ props
def _players():
    return [props.Player("Star", "HOME", True, 34, 3, {"PTS": (0.75, 0.10), "REB": (0.20, 0.25)}, 1.0),
            props.Player("Sub", "AWAY", False, 18, 4, {"PTS": (0.45, 0.15)}, 0.5)]


ENV = props.Environment(total_mean=225.0, total_sd=18.0, margin_mean=0.0, margin_sd=13.0, elasticity={"PTS": 1.0, "REB": 0.5})


def test_props_availability_minutes_and_counts():
    r = props.simulate(_players(), ENV, 40_000, 31, card=False)
    sub = r["players"]["Sub"]
    assert abs((sub["MIN"] > 0).mean() - 0.5) < 0.01                      # a 50% availability is a mixture, not a guess
    star = r["players"]["Star"]
    assert 33 < star["MIN"].mean() < 34.1 and abs(star["PTS"].mean() - 0.75 * star["MIN"].mean()) < 0.5
    assert star["PTS"].var() > star["PTS"].mean()                           # negative binomial overdispersion


def test_props_share_the_game_environment():
    r = props.simulate(_players(), ENV, 60_000, 32, card=False)
    corr = np.corrcoef(r["players"]["Star"]["PTS"], r["total"])[0, 1]
    assert corr > 0.1                                                      # a higher-scoring game lifts a player's points
    both = props.joint(1, r["players"]["Star"]["PTS"] > 25.5, r["players"]["Star"]["REB"] > 6.5)["p"]
    independent = (r["players"]["Star"]["PTS"] > 25.5).mean() * (r["players"]["Star"]["REB"] > 6.5).mean()
    assert both > independent                                              # shared pace and minutes make the pair positively dependent


def test_props_blowouts_cut_a_starters_minutes():
    tight = props.simulate(_players(), props.Environment(225, 18, 0, 3), 30_000, 33, card=False)["players"]["Star"]["MIN"].mean()
    blowout = props.simulate(_players(), props.Environment(225, 18, 25, 3), 30_000, 33, card=False)["players"]["Star"]["MIN"].mean()
    assert blowout < tight - 3.0


def test_props_prob_over_and_coverage():
    r = props.simulate(_players(), ENV, 30_000, 34, card=False)
    q = props.prob_over(r["players"]["Star"]["PTS"], 24.5, 34)
    assert 0 < q["p_decisive"] < 1 and q["w"] + q["l"] + q["p"] == pytest.approx(1.0)
    rng = np.random.default_rng(1)
    predictive = [rng.normal(20, 5, 4000) for _ in range(400)]
    actual = rng.normal(20, 5, 400)
    cov = props.coverage(predictive, actual)
    assert abs(cov[0.5] - 0.5) < 0.08 and abs(cov[0.8] - 0.8) < 0.07       # a correct predictive sample covers at nominal
    with pytest.raises(core.SimulationError):
        props.coverage(predictive[:5], actual)

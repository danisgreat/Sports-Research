"""Cross-engine contract checks: every engine yields a proper, endpoint-labelled distribution with coherent contract prices.

Engine internals have their own test modules; this file checks what they share (ENG-01, DST-01, DST-13).
"""

import numpy as np
import pytest

from runtime.src.common.errors import MissingInputs, NotFitted
from runtime.src.common.leagues import get_profile
from runtime.src.sports.afl.engine import AFLEngine
from runtime.src.sports.baseball.engine import BaseballEngine
from runtime.src.sports.basketball.engine import BasketballEngine
from runtime.src.sports.cricket.engine import CricketEngine, CricketFormat
from runtime.src.sports.nfl.engine import NFLEngine
from runtime.src.sports.nhl.engine import HockeyLateGame, NHLEngine
from runtime.src.sports.nrl.engine import NRLEngine, NRLKicking
from runtime.src.sports.soccer.engine import SoccerEngine
from runtime.src.sports.tennis.engine import TennisEngine
from runtime.tests.test_soccer_models import season

AFL_SHOTS = get_profile("afl", "AFL").extra("scoring_shots_mean")
KICK = NRLKicking(conversion_rate=0.80, penalty_goals=0.5, field_goals=0.1)


def engines():
    """(name, engine, context) for each sport with a stated endpoint."""
    return [
        ("cricket", CricketEngine({"t20": CricketFormat.t20_illustrative()}),
         {"format": "t20", "home_expected_runs": 172.0, "away_expected_runs": 160.0, "bat_first": "home"}),
        ("basketball", BasketballEngine(league=get_profile("basketball", "NBA")), {"home_expected_points": 116.0, "away_expected_points": 112.0}),
        ("nfl", NFLEngine(league=get_profile("american_football", "NFL")), {"home_expected_points": 25.0, "away_expected_points": 20.0}),
        ("baseball", BaseballEngine(league=get_profile("baseball", "MLB")), {"home_expected_runs": 4.6, "away_expected_runs": 4.2}),
        ("afl", AFLEngine(league=get_profile("afl", "AFL")), {"home_expected_shots": AFL_SHOTS * 1.04, "away_expected_shots": AFL_SHOTS * 0.96}),
        ("nrl", NRLEngine(league=get_profile("rugby_league", "NRL"), kicking=KICK), {"home_expected_tries": 4.2, "away_expected_tries": 3.6}),
        ("soccer", SoccerEngine(), {"home_xg": 1.8, "away_xg": 0.9, "dixon_coles_rho": -0.05}),
        ("nhl", NHLEngine(league=get_profile("ice_hockey", "NHL"), late_game=HockeyLateGame.ILLUSTRATIVE), {"home_xg": 3.2, "away_xg": 2.7}),
        ("tennis", TennisEngine(form_sigma=0.04), {"p_serve1": 0.67, "p_serve2": 0.61}),
    ]


@pytest.mark.parametrize("name,engine,ctx", engines(), ids=[e[0] for e in engines()])
def test_distribution_is_proper_labelled_and_coherent(name, engine, ctx):
    dist = engine.predict_distribution(ctx)
    assert dist.grid.sum() == pytest.approx(1.0, abs=1e-6) and (dist.grid >= -1e-12).all()
    assert dist.endpoint != "unspecified"                                    # contracts refuse an unlabelled endpoint
    home, away, draw = dist.p_home_win(), dist.p_away_win(), dist.p_draw()
    assert home + away + draw == pytest.approx(1.0, abs=1e-6) and home > away      # the stated favourite is the favourite
    for value in (home, away, draw):
        assert 0.0 <= value <= 1.0
    # covering pair: +1.5 on the favourite's opponent can not be less likely than the moneyline for them
    assert dist.p_away_cover(1.5) >= away - 1e-9
    assert dist.p_home_cover(-1.5) <= home + 1e-9


@pytest.mark.parametrize("name,engine,ctx", engines(), ids=[e[0] for e in engines()])
def test_contract_prices_are_derived_from_the_same_grid(name, engine, ctx):
    dist = engine.predict_distribution(ctx)
    total = float(np.sum(dist.expected_scores()))
    line = float(np.floor(total)) + 0.5
    contracts = engine.evaluate_contracts(dist, [{"type": "moneyline", "side": "home"}, {"type": "total", "side": "over", "line": line},
                                                 {"type": "total", "side": "under", "line": line}])
    assert contracts[0].stated_prob == pytest.approx(dist.p_home_win(), abs=1e-9)
    assert contracts[1].stated_prob + contracts[2].stated_prob == pytest.approx(1.0, abs=1e-6)


def test_engines_refuse_to_predict_without_their_inputs():
    for _, engine, ctx in engines():
        with pytest.raises((MissingInputs, NotFitted, ValueError, KeyError)):
            engine.predict_distribution({})


def test_soccer_engine_fits_and_roundtrips_through_json(tmp_path):
    engine = SoccerEngine().fit(season())
    ctx = {"home_team": "Club1", "away_team": "Club2", "dixon_coles_rho": None}
    dist = engine.predict_distribution({k: v for k, v in ctx.items() if v is not None})
    assert dist.grid.sum() == pytest.approx(1.0, abs=1e-6)
    path = str(tmp_path / "soccer.json")
    engine.save_artifact(path)
    loaded = SoccerEngine.load_artifact(path)
    np.testing.assert_allclose(dist.grid, loaded.predict_distribution({k: v for k, v in ctx.items() if v is not None}).grid)

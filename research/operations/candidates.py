"""Rule P4 as tooling: price the standard ladder from ONE distribution and propose the four candidates (PRD-04, PRD-02, PRD-03).

  python -B -m research.operations.candidates REQUEST.json [--out CARD.json] [--table]

REQUEST.json
  { "sport": "ice_hockey", "league": "NHL", "endpoint": "full_game",
    "context": {"home_xg": 3.1, "away_xg": 2.7},                 # the engine's own context keys (explicit expected values)
    "supplied": [{"type": "total", "side": "over", "line": 6.5, "label": "Over 6.5"}],   # reference rows, tagged SUPPLIED
    "names": ["Southport Bears", "Northfield Owls"] }

The output is the card JSON block: the distribution object (id with a content hash), the full priced ladder, the four chosen rows with
their tags, the joint top-two failure mass, the Rank-1 gate and flags, and the pick table (evidence and failure-route cells are
left as TO_FILL for the analyst; the card validator refuses a card that keeps a placeholder). Nothing is read from a market.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SUPPORTED = ('soccer', 'ice_hockey', 'basketball', 'baseball', 'american_football', 'afl', 'rugby_league', 'tennis')


def build_distribution(sport: str, league: str | None, context: dict, endpoint: str | None = None):
    """(ScoreDistribution, engine name, caveats). Every engine is driven by explicit expected values, never a hidden default."""
    from runtime.src.common.leagues import get_profile
    caveats: list[str] = []
    if sport == 'soccer':
        from runtime.src.sports.soccer.engine import SoccerEngine
        return SoccerEngine().predict_distribution(context, endpoint or 'regulation'), 'SoccerEngine', caveats
    if sport == 'tennis':
        from runtime.src.sports.tennis.engine import TennisEngine
        return TennisEngine().predict_distribution(context, endpoint or 'completed_match'), 'TennisEngine', caveats
    if sport not in SUPPORTED:
        raise ValueError(f'unsupported sport {sport!r}; supported: {", ".join(SUPPORTED)}')
    if not league:
        raise ValueError('league is required: priors are never borrowed from another league')
    profile = get_profile(sport, league)
    if sport == 'ice_hockey':
        from runtime.src.sports.nhl.engine import HockeyLateGame, NHLEngine
        caveats.append('empty-net late-game parameters are the ILLUSTRATIVE scenario, not fitted on play-by-play')
        return NHLEngine(league=profile, late_game=HockeyLateGame.ILLUSTRATIVE).predict_distribution(context, endpoint or 'full_game'), 'NHLEngine', caveats
    if sport == 'basketball':
        from runtime.src.sports.basketball.engine import BasketballEngine
        return BasketballEngine(league=profile).predict_distribution(context, endpoint or 'full_game'), 'BasketballEngine', caveats
    if sport == 'baseball':
        from runtime.src.sports.baseball.engine import BaseballEngine
        return BaseballEngine(league=profile).predict_distribution(context, endpoint or 'full_game'), 'BaseballEngine', caveats
    if sport == 'american_football':
        from runtime.src.sports.nfl.engine import NFLEngine
        return NFLEngine(league=profile).predict_distribution(context), 'NFLEngine', caveats
    if sport == 'afl':
        from runtime.src.sports.afl.engine import AFLEngine
        return AFLEngine(league=profile).predict_distribution(context), 'AFLEngine', caveats
    from runtime.src.sports.nrl.engine import NRLEngine, NRLKicking
    kicking = context.get('kicking')
    if kicking is None:
        raise ValueError('rugby league needs context["kicking"] = {"conversion_rate", "penalty_goals", "field_goals"}')
    ctx = {k: v for k, v in context.items() if k != 'kicking'}
    return NRLEngine(league=profile, kicking=NRLKicking(**kicking)).predict_distribution(ctx), 'NRLEngine', caveats


def distribution_id(sport: str, engine: str, dist) -> str:
    digest = hashlib.sha256(np.round(dist.grid, 9).tobytes() + np.asarray(dist.home_support).tobytes() + np.asarray(dist.away_support).tobytes()).hexdigest()
    return f'{sport}_{engine.replace("Engine", "").lower()}_{digest[:8]}'


def run(request: dict) -> dict:
    from runtime.src.common.selection import ladder, load_rules, outcome_space, propose, row_from_spec
    rules = load_rules()
    sport = request['sport']
    if sport not in rules['ladders']:
        raise ValueError(f'no ladder specification for {sport!r}')
    dist, engine, caveats = build_distribution(sport, request.get('league'), request['context'], request.get('endpoint'))
    names = tuple(request.get('names', ('Home', 'Away')))
    space = outcome_space(dist)
    supplied = [row_from_spec(space, spec) for spec in request.get('supplied', [])]
    rows = ladder(space, rules['ladders'][sport], names=names)  # type: ignore[arg-type]
    proposal = propose(rows, space, supplied, rules)
    dist_id = distribution_id(sport, engine, dist)
    result: dict[str, Any] = proposal.as_dict()
    mu_h, mu_a = dist.expected_scores()
    result.update({'distribution_object': f'{dist_id} — {engine} {json.dumps(request["context"], sort_keys=True)}; endpoint {dist.endpoint}',
                   'distribution_id': dist_id, 'endpoint': dist.endpoint, 'expected_scores': [round(mu_h, 4), round(mu_a, 4)],
                   'caveats': caveats + list(dist.metadata.get('warnings', [])), 'pick_table': proposal.pick_table(dist_id),
                   'supplied_not_selected': [{'proposition': s.label, 'p_card': round(s.p_card, 4)} for s in supplied
                                             if all(p.row.kind != s.kind for p in proposal.picks)]})
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('request', type=Path)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--table', action='store_true', help='print only the pick table')
    args = parser.parse_args(argv)
    result = run(json.loads(args.request.read_text(encoding='utf-8')))
    if args.out:
        args.out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(result['pick_table'] if args.table else json.dumps({k: result[k] for k in ('distribution_id', 'picks', 'joint_failure_top2', 'rank1_gate', 'flags')}, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())

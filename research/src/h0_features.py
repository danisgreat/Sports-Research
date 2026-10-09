"""Point-in-time features over the standardised archive (the H0 training table, ML-03).

Every feature of a game is computed from games dated STRICTLY BEFORE that game's date, so two games on the same day never
see each other and a result can never leak into an earlier row. Each row records `known_at`: the first instant at which all
its inputs were public (the end of the latest contributing game's calendar day).

Features (home / away): rest days (-1 when no earlier game), games in the previous 7 days, points for and against over the
last 5 and 10 games, games played this season, an Elo rating with a margin multiplier (regressed to the mean at each new
season) and the Elo difference. League context: running mean home and away score. Missing history is NaN, never zero.
"""
from __future__ import annotations
import math
from collections import deque
from datetime import date, timedelta
from typing import Any, Iterable

from runtime.src.common.ratings import EloRatingEngine

FEATURES = [
    'home_rest', 'away_rest', 'home_games7', 'away_games7',
    'home_gf5', 'home_ga5', 'away_gf5', 'away_ga5', 'home_gf10', 'home_ga10', 'away_gf10', 'away_ga10',
    'home_season_games', 'away_season_games', 'home_elo', 'away_elo', 'elo_diff', 'league_mean_home', 'league_mean_away', 'is_early_season',
]
NAN = float('nan')


class _Team:
    def __init__(self) -> None:
        self.last_date: date | None = None
        self.dates: deque = deque(maxlen=12)
        self.gf: deque = deque(maxlen=10)
        self.ga: deque = deque(maxlen=10)
        self.season: int | None = None
        self.games_in_season = 0


def _mean(values: Iterable[float], k: int, minimum: int = 2) -> float:
    items = list(values)[-k:]
    return sum(items) / len(items) if len(items) >= minimum else NAN


def build_rows(events: list[Any], elo_k: float = 20.0, elo_home: float = 50.0, carry: float = 0.75) -> list[dict]:
    """Rows in event order; `events` need date, season_year, home, away, home_score, away_score (archive_std.StdEvent)."""
    ordered = sorted(events, key=lambda e: (e.date, e.home, e.away))
    teams: dict[str, _Team] = {}
    elo = EloRatingEngine(k_factor=elo_k, home_advantage=elo_home)
    sum_h = sum_a = 0.0
    count = 0
    seen_season: int | None = None
    rows: list[dict] = []
    i = 0
    while i < len(ordered):
        day = ordered[i].date
        j = i
        while j < len(ordered) and ordered[j].date == day:
            j += 1
        today = ordered[i:j]
        d = date.fromisoformat(day)
        for e in today:                                   # features first, from state as of the end of the previous day
            if seen_season is not None and e.season_year != seen_season:
                pass
            home, away = teams.setdefault(e.home, _Team()), teams.setdefault(e.away, _Team())
            row: dict[str, Any] = {'date': day, 'season': e.season_year, 'home': e.home, 'away': e.away,
                                   'home_score': e.home_score, 'away_score': e.away_score}
            latest = None
            for side, t in (('home', home), ('away', away)):
                same_season = t.season == e.season_year
                row[f'{side}_rest'] = float(min((d - t.last_date).days, 14)) if t.last_date else -1.0
                row[f'{side}_games7'] = float(sum(1 for x in t.dates if 0 < (d - x).days <= 7))
                row[f'{side}_gf5'], row[f'{side}_ga5'] = _mean(t.gf, 5), _mean(t.ga, 5)
                row[f'{side}_gf10'], row[f'{side}_ga10'] = _mean(t.gf, 10), _mean(t.ga, 10)
                row[f'{side}_season_games'] = float(t.games_in_season if same_season else 0)
                if t.last_date and (latest is None or t.last_date > latest):
                    latest = t.last_date
            row['home_elo'], row['away_elo'] = elo.get_rating(e.home), elo.get_rating(e.away)
            row['elo_diff'] = row['home_elo'] + elo_home - row['away_elo']
            row['league_mean_home'] = sum_h / count if count else NAN
            row['league_mean_away'] = sum_a / count if count else NAN
            row['is_early_season'] = float(min(row['home_season_games'], row['away_season_games']) < 5)
            row['known_at'] = (latest + timedelta(days=1)).isoformat() if latest else None
            rows.append(row)
        for e in today:                                   # then update state with today's results
            if seen_season is None or e.season_year != seen_season:
                if seen_season is not None:
                    elo.regress_to_mean(carry)
                seen_season = e.season_year
            for name, mine, theirs in ((e.home, e.home_score, e.away_score), (e.away, e.away_score, e.home_score)):
                t = teams[name]
                if t.season != e.season_year:
                    t.season, t.games_in_season = e.season_year, 0
                t.last_date = d
                t.dates.append(d)
                t.gf.append(float(mine))
                t.ga.append(float(theirs))
                t.games_in_season += 1
            margin = e.home_score - e.away_score
            elo.update(e.home, e.away, 1.0 if margin > 0 else 0.0 if margin < 0 else 0.5, margin=abs(margin) if margin else None)
            sum_h += e.home_score
            sum_a += e.away_score
            count += 1
        i = j
    return rows


def matrix(rows: list[dict], names: list[str] | None = None):
    """(n, k) float array of the feature columns, NaN where unknown."""
    import numpy as np
    names = names or FEATURES
    return np.array([[float(r[n]) if r[n] is not None and not (isinstance(r[n], float) and math.isnan(r[n])) else NAN for n in names] for r in rows], dtype=float)

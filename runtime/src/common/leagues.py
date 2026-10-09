"""League scoring profiles: explicit, sourced priors instead of hidden literals (DST-03, DST-13).

A profile is built from the archive by `research.operations.build_league_profiles` and stored in
`runtime/config/leagues/<sport>.json` with the hashes of the files it was computed from. Engines
take a profile explicitly; there is no silent NBA/NHL/MLB default for another league.
"""

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Dict, Mapping, Optional, Tuple

from .errors import MissingInputs

CONFIG_DIR = Path(__file__).resolve().parents[2] / "config" / "leagues"


@dataclass(frozen=True)
class LeagueProfile:
    sport: str
    league: str
    n_games: int
    seasons: Tuple[int, int]
    mean_home: float
    mean_away: float
    total_sd: float
    margin_sd: float
    score_corr: float
    extras: Mapping[str, float] = field(default_factory=dict)
    provenance: Mapping[str, object] = field(default_factory=dict)
    # Optional empirical distribution of the signed margin (home minus away) clipped at +/-limit, for key-number calibration.
    margin_pmf: Optional[Mapping[int, float]] = None

    @property
    def mean_team_score(self) -> float:
        return 0.5 * (self.mean_home + self.mean_away)

    @property
    def home_advantage(self) -> float:
        return self.mean_home - self.mean_away

    @property
    def mean_total(self) -> float:
        return self.mean_home + self.mean_away

    @property
    def team_sd(self) -> float:
        """Per-team score SD implied by the total and margin SDs: Var(h) = (Var(T) + Var(M)) / 4 for equal means."""
        return float(((self.total_sd ** 2 + self.margin_sd ** 2) / 4.0) ** 0.5)

    def extra(self, key: str) -> float:
        if key not in self.extras:
            raise MissingInputs(f"profile {self.sport}/{self.league} has no {key!r}; it must be supplied explicitly")
        return float(self.extras[key])


def _from_dict(sport: str, name: str, d: dict) -> LeagueProfile:
    return LeagueProfile(sport=sport, league=name, n_games=int(d["n_games"]), seasons=(int(d["seasons"][0]), int(d["seasons"][1])),
                         mean_home=float(d["mean_home"]), mean_away=float(d["mean_away"]), total_sd=float(d["total_sd"]),
                         margin_sd=float(d["margin_sd"]), score_corr=float(d["score_corr"]),
                         extras=dict(d.get("extras", {})), provenance=dict(d.get("provenance", {})),
                         margin_pmf=None if d.get("margin_pmf") is None else {int(k): float(v) for k, v in d["margin_pmf"].items()})


def load_profiles(sport: str, config_dir: Optional[Path] = None) -> Dict[str, LeagueProfile]:
    path = Path(config_dir or CONFIG_DIR) / f"{sport}.json"
    if not path.exists():
        raise MissingInputs(f"no league profiles for {sport!r} at {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    return {name: _from_dict(sport, name, body) for name, body in data["leagues"].items()}


def get_profile(sport: str, league: str, config_dir: Optional[Path] = None) -> LeagueProfile:
    profiles = load_profiles(sport, config_dir)
    if league not in profiles:
        raise MissingInputs(f"no profile for {sport}/{league}; known: {sorted(profiles)}. "
                            "Supply expected values explicitly instead of borrowing another league's prior.")
    return profiles[league]

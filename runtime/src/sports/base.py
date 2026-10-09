"""Abstract base class for sport predictive distribution engines."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Sequence, Tuple


from ..common import artifacts
from ..common.contracts import ScoreDistribution
from ..common.errors import InsufficientData, MissingInputs, NotFitted, UnknownTeam, finite_score
from ..common.identity import Contract, ContractType
from ..common.leagues import LeagueProfile

Game = Tuple[str, str, float, float]


class EndpointMismatch(ValueError):
    """A contract names an endpoint (regulation / full_game) that the grid does not settle on."""


def _first(record: dict, keys: Sequence[str]):
    for key in keys:
        value = record.get(key)
        if value is not None and str(value).strip() != "":
            return value
    return None


def collect_games(train_data: Any, home_score_keys: Sequence[str], away_score_keys: Sequence[str],
                  min_games: int = 20) -> List[Game]:
    """Validated (home, away, home score, away score) tuples from a list of dicts or a DataFrame.

    A missing or non-finite score raises; a zero score is a score. Nothing is defaulted (DST-01).
    """
    if hasattr(train_data, "to_dict") and hasattr(train_data, "columns"):
        records = train_data.to_dict("records")
    elif isinstance(train_data, (list, tuple)):
        records = list(train_data)
    else:
        raise ValueError("train_data must be a list of game dicts or a DataFrame; "
                         "an engine is never 'fitted' on nothing")
    games: List[Game] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"training record {index} is not a dict")
        home = _first(record, ("home_team", "home"))
        away = _first(record, ("away_team", "away"))
        if home is None or away is None:
            raise MissingInputs(f"training record {index} lacks home/away team names")
        games.append((str(home), str(away), finite_score(record, *home_score_keys), finite_score(record, *away_score_keys)))
    if len(games) < min_games:
        raise InsufficientData(f"need at least {min_games} games to fit, got {len(games)}")
    return games


class BaseSportEngine(ABC):
    """Base class for all sport engines producing discrete score distributions.

    league:              explicit `LeagueProfile` giving scoring level and dispersion; never a hidden default.
    unknown_team_policy: "refuse" (default) raises `UnknownTeam`; "league_average" uses 1.0 factors and
                         records a warning in the distribution metadata.
    """

    def __init__(self, sport_name: str, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse"):
        if unknown_team_policy not in ("refuse", "league_average"):
            raise ValueError("unknown_team_policy must be 'refuse' or 'league_average'")
        self.sport_name = sport_name
        self.is_fitted = False
        self.league = league
        self.unknown_team_policy = unknown_team_policy
        self._warnings: List[str] = []

    # ------------------------------------------------------------------ helpers
    def _warn(self, message: str) -> None:
        self._warnings.append(message)

    def _take_warnings(self) -> List[str]:
        out, self._warnings = self._warnings, []
        return out

    def _factor(self, table: Dict[str, float], team: Optional[str], label: str) -> float:
        if team is not None and team in table:
            return table[team]
        if self.unknown_team_policy == "league_average":
            self._warn(f"{label}: unknown team {team!r}; league-average factor 1.0 used, uncertainty not modelled")
            return 1.0
        raise UnknownTeam(f"{self.sport_name}: no fitted strength for {team!r} ({label}); "
                          "supply the expected values explicitly or set unknown_team_policy='league_average'")

    def _teams(self, ctx: Dict[str, Any]) -> Tuple[str, str]:
        """(home, away) names from a context; a fitted-strength lookup without names is an input error, not a guess."""
        home, away = _first(ctx, ("home_team", "home")), _first(ctx, ("away_team", "away"))
        if home is None or away is None:
            raise MissingInputs(f"{self.sport_name}: context needs home_team and away_team to look up fitted strengths")
        return str(home), str(away)

    def _require(self, context: Dict[str, Any], *keys: str) -> None:
        missing = [k for k in keys if context.get(k) is None]
        if missing:
            raise MissingInputs(f"{self.sport_name}: context needs {missing} (or a fitted engine / league profile)")

    def _need_fit_or_profile(self) -> None:
        if not self.is_fitted and self.league is None:
            raise NotFitted(f"{self.sport_name}: fit the engine or supply a league profile, or pass every expected value in the context")

    @abstractmethod
    def fit(self, train_data: Any) -> "BaseSportEngine":
        """Fit model parameters on historical records (never on nothing)."""

    @abstractmethod
    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce the joint score probability distribution P(Home = s1, Away = s2)."""

    # --------------------------------------------------------------- contracts
    def evaluate_contracts(self, score_dist: ScoreDistribution, contract_specs: List[Dict[str, Any]]) -> List[Contract]:
        """Derive contracts directly from the joint score distribution.

        A spec may carry `"endpoint": "regulation" | "full_game"`; it is refused against a grid that settles
        on another endpoint, because a regulation grid prices a full-game moneyline incoherently.
        """
        results: List[Contract] = []

        for spec in contract_specs:
            wanted = spec.get("endpoint")
            if wanted and score_dist.endpoint not in ("unspecified", wanted):
                raise EndpointMismatch(f"contract {spec} settles on {wanted!r} but the distribution is {score_dist.endpoint!r}; "
                                       "build the distribution with the matching endpoint")
            ctype = ContractType(spec["type"])
            cid = spec.get("contract_id", f"{ctype.value}_{spec.get('side', '')}_{spec.get('line', '')}")
            line = spec.get("line")
            side = spec.get("side", "").lower()
            p_stated: Optional[float] = None

            if ctype == ContractType.MONEYLINE:
                if side == "home":
                    p_stated = score_dist.p_home_win()
                elif side == "away":
                    p_stated = score_dist.p_away_win()
                elif side == "draw":
                    p_stated = score_dist.p_draw()

            elif ctype == ContractType.SPREAD:
                if line is None:
                    raise ValueError(f"Spread contract requires line: {spec}")
                if side == "home":
                    p_stated = score_dist.p_home_cover(float(line))
                elif side == "away":
                    p_stated = score_dist.p_away_cover(float(line))

            elif ctype == ContractType.TOTAL:
                if line is None:
                    raise ValueError(f"Total contract requires line: {spec}")
                if side == "over":
                    p_stated = score_dist.p_over(float(line))
                elif side == "under":
                    p_stated = score_dist.p_under(float(line))

            elif ctype == ContractType.TEAM_TOTAL:
                if line is None:
                    raise ValueError(f"Team total contract requires line: {spec}")
                team = spec.get("team", "home").lower()
                if side == "over":
                    p_stated = score_dist.p_team_total_over(team, float(line))
                elif side == "under":
                    p_stated = score_dist.p_team_total_under(team, float(line))

            elif ctype == ContractType.DOUBLE_CHANCE:
                p_stated = score_dist.p_double_chance(side)

            elif ctype == ContractType.DRAW_NO_BET:
                p_stated = score_dist.p_draw_no_bet(side)

            elif ctype == ContractType.BTTS:
                if side in ("yes", "btts_yes"):
                    p_stated = score_dist.p_btts_yes()
                else:
                    p_stated = score_dist.p_btts_no()

            results.append(
                Contract(
                    contract_id=cid,
                    contract_type=ctype,
                    target_side=side,
                    line=line,
                    stated_prob=p_stated,
                    market_prob=spec.get("market_prob")
                )
            )

        return results

    # --------------------------------------------------------------- artifacts
    def save_artifact(self, filepath: str, model_card: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Write engine parameters as a hashed JSON artifact with a model card (no pickle)."""
        card = {"engine": type(self).__name__, "sport": self.sport_name, "fitted": self.is_fitted}
        card.update(model_card or {})
        return artifacts.save(self, filepath, card)

    @classmethod
    def load_artifact(cls, filepath: str) -> "BaseSportEngine":
        """Load an artifact written by `save_artifact`, verifying its content hash."""
        engine = artifacts.load(filepath)
        if not isinstance(engine, BaseSportEngine):
            raise TypeError(f"Loaded artifact is not a BaseSportEngine instance: {type(engine)}")
        if not isinstance(engine, cls):
            raise TypeError(f"Loaded artifact is a {type(engine).__name__}, not a {cls.__name__}")
        return engine

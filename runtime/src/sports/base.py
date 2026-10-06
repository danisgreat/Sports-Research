"""Abstract base class for sport predictive distribution engines."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import numpy as np
from ..common.contracts import ScoreDistribution
from ..common.identity import Contract, ContractType


class BaseSportEngine(ABC):
    """Base class for all sport engines producing discrete score distributions."""

    def __init__(self, sport_name: str):
        self.sport_name = sport_name
        self.is_fitted = False

    @abstractmethod
    def fit(self, train_data: Any) -> "BaseSportEngine":
        """Fit model parameters on historical H0 data."""
        pass

    @abstractmethod
    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce the joint score probability distribution P(Home = s1, Away = s2)."""
        pass

    def evaluate_contracts(
        self,
        score_dist: ScoreDistribution,
        contract_specs: List[Dict[str, Any]]
    ) -> List[Contract]:
        """Derive betting contracts directly from the joint score distribution."""
        results: List[Contract] = []

        for spec in contract_specs:
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


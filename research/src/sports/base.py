from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
import math


@dataclass(frozen=True)
class Contract:
    event_id: str
    market: str
    side: str
    line: float | None
    endpoint: str
    period: str = "FULL_GAME"
    void_rule: str = "VOID_IF_NOT_COMPLETED"

    def __post_init__(self) -> None:
        if not self.event_id or not self.endpoint:
            raise ValueError("event_id and settlement endpoint are mandatory")
        if self.market in {"SPREAD", "TOTAL"} and self.line is None:
            raise ValueError("this market needs a line")
        if self.market not in {"ML", "1X2", "SPREAD", "TOTAL", "BTTS"}:
            raise ValueError(f"unsupported market {self.market}")
        sides={"ML":{"HOME","AWAY"},"1X2":{"HOME","DRAW","AWAY"},
               "SPREAD":{"HOME","AWAY"},"TOTAL":{"OVER","UNDER"},"BTTS":{"YES","NO"}}
        if self.side not in sides[self.market]:
            raise ValueError("invalid contract side")
        if self.line is not None and (isinstance(self.line,bool) or not isinstance(self.line,(int,float)) or not math.isfinite(self.line)):
            raise ValueError("line must be finite numeric contract metadata")
        if self.market not in {"SPREAD","TOTAL"} and self.line is not None:
            raise ValueError("this family has no line")
        if not self.period or self.void_rule not in {"VOID_IF_NOT_COMPLETED"}:
            raise ValueError("explicit period and supported void rule required")


class SportModel(Protocol):
    sport: str

    def fit(self, history, as_of): ...
    def simulate(self, event, n: int = 200_000): ...
    def price(self, draws, contract: Contract): ...

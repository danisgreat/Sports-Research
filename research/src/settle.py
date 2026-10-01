"""Deterministic settlement from an identified terminal feed receipt.

No narrative input is accepted. Future league adapters must produce FinalReceipt.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal
import re

from .sports.base import Contract

Result = Literal["W", "L", "P", "VOID"]


@dataclass(frozen=True)
class FinalReceipt:
    event_id: str
    state: str
    home_score: int
    away_score: int
    endpoint: str
    source_url: str
    retrieved_utc: datetime
    response_sha256: str
    raw_score: str
    void: bool = False

    def __post_init__(self) -> None:
        if self.retrieved_utc.tzinfo is None or self.retrieved_utc.utcoffset() is None:
            raise ValueError("receipt time must be timezone aware")
        if not self.event_id or not self.source_url.startswith("https://") or not re.fullmatch(r"[0-9a-f]{64}",self.response_sha256):
            raise ValueError("receipt lacks event, URL, or response checksum")
        if any(isinstance(v,bool) or not isinstance(v,int) or v<0 for v in (self.home_score,self.away_score)):
            raise ValueError("nonnegative integer scores required")


@dataclass(frozen=True)
class Settlement:
    result: Result
    event_id: str
    source_url: str
    retrieved_utc: str
    response_sha256: str
    raw_score: str


def settle(contract: Contract, receipt: FinalReceipt) -> Settlement:
    if contract.event_id != receipt.event_id:
        raise ValueError("event ID mismatch")
    if receipt.state.upper() not in {"FINAL", "OFFICIAL_FINAL"}:
        raise ValueError("feed state is not terminal")
    if contract.endpoint != receipt.endpoint:
        raise ValueError("settlement endpoint mismatch")
    if receipt.void:
        result: Result = "VOID"
    else:
        h, a = receipt.home_score, receipt.away_score
        if contract.market == "1X2":
            if contract.side not in {"HOME", "DRAW", "AWAY"}:
                raise ValueError("bad 1X2 side")
            actual = "HOME" if h > a else "AWAY" if a > h else "DRAW"
            result = "W" if contract.side == actual else "L"
        elif contract.market == "BTTS":
            actual = h > 0 and a > 0
            if contract.side not in {"YES", "NO"}:
                raise ValueError("bad BTTS side")
            result = "W" if actual == (contract.side == "YES") else "L"
        else:
            if contract.market == "ML":
                if contract.side not in {"HOME", "AWAY"}:
                    raise ValueError("bad ML side")
                value = h - a if contract.side == "HOME" else a - h
            elif contract.market == "SPREAD":
                if contract.side not in {"HOME", "AWAY"}:
                    raise ValueError("bad spread side")
                value = (h - a if contract.side == "HOME" else a - h) + contract.line
            else:
                if contract.side not in {"OVER", "UNDER"}:
                    raise ValueError("bad total side")
                value = (h + a - contract.line) * (1 if contract.side == "OVER" else -1)
            result = "W" if value > 0 else "L" if value < 0 else "P"
    return Settlement(result, receipt.event_id, receipt.source_url,
                      receipt.retrieved_utc.astimezone(timezone.utc).isoformat(),
                      receipt.response_sha256, receipt.raw_score)

"""Sport and match identity definitions and schemas."""

from dataclasses import dataclass, field
from enum import Enum
import hashlib
from typing import Optional


class SportIdentity(str, Enum):
    CRICKET = "cricket"
    BASKETBALL = "basketball"
    AMERICAN_FOOTBALL = "american_football"
    BASEBALL = "baseball"
    AFL = "afl"
    NRL = "nrl"
    SOCCER = "soccer"
    NHL = "nhl"


class ContractType(str, Enum):
    MONEYLINE = "moneyline"
    SPREAD = "spread"
    TOTAL = "total"
    TEAM_TOTAL = "team_total"
    DOUBLE_CHANCE = "double_chance"
    DRAW_NO_BET = "draw_no_bet"
    BTTS = "btts"


@dataclass(frozen=True)
class MatchIdentity:
    """Canonical deterministic identity for a sporting event."""
    sport: str
    competition: str
    season: str
    date: str  # YYYY-MM-DD
    home_team: str
    away_team: str
    venue: Optional[str] = None
    match_id: str = field(init=False)

    def __post_init__(self):
        # Generate canonical deterministic slug
        raw_slug = f"{self.sport}_{self.competition}_{self.season}_{self.date}_{self.home_team}_{self.away_team}".lower().replace(" ", "-")
        # Generate a clean short sha256 fingerprint for canonical storage
        digest = hashlib.sha256(raw_slug.encode("utf-8")).hexdigest()[:12]
        object.__setattr__(self, "match_id", f"{raw_slug}_{digest}")


@dataclass(frozen=True)
class Contract:
    """Betting contract specification derived from event distributions."""
    contract_id: str
    contract_type: ContractType
    target_side: str  # e.g., "home", "away", "draw", "over", "under", "btts_yes"
    line: Optional[float] = None
    stated_prob: Optional[float] = None
    market_prob: Optional[float] = None


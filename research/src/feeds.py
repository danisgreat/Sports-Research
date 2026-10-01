"""Exact-event terminal score adapters. One response is one source lineage."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from .sources import fetch_source, verified_body, read_registry, allowed_url

from .settle import FinalReceipt

ESPN_PATHS = {
    "EPL": "soccer/eng.1", "NBA": "basketball/nba", "WNBA": "basketball/wnba",
    "NBL": "basketball/nbl", "NFL": "football/nfl", "AFL": "australian-football/afl",
    "NRL": "rugby-league/3", "NHL": "hockey/nhl",
}


def _fetch(url: str) -> tuple[dict, str, datetime]:
    candidates=[sid for sid,source in read_registry().items() if allowed_url(url,source)]
    if url.startswith("https://site.api.espn.com/"):
        candidates=[sid for sid in candidates if (sid=="espn_epl" and "/soccer/eng.1/" in url)
                    or (sid=="espn_nbl" and "/basketball/nbl/" in url)]
    if len(candidates)!=1:
        raise ValueError("exact approved source adapter is required")
    receipt=fetch_source(candidates[0],url)
    return json.loads(verified_body(receipt)),receipt["response_sha256"],datetime.fromisoformat(receipt["retrieved_utc"])


def mlb_final(game_pk: int, endpoint: str = "INCL_EXTRAS") -> FinalReceipt:
    url = f"https://statsapi.mlb.com/api/v1.1/game/{int(game_pk)}/feed/live"
    obj, checksum, retrieved = _fetch(url)
    if str(obj.get("gameData", {}).get("game", {}).get("pk")) != str(game_pk):
        raise ValueError("MLB gamePk mismatch")
    status = obj["gameData"]["status"]
    if status.get("abstractGameState") != "Final" or status.get("detailedState") not in {"Final", "Game Over"}:
        raise ValueError(f"MLB feed not final: {status}")
    innings = obj["liveData"]["linescore"]["innings"]
    if endpoint == "INCL_EXTRAS":
        scores = obj["liveData"]["linescore"]["teams"]
        home, away = int(scores["home"]["runs"]), int(scores["away"]["runs"])
    elif endpoint == "REGULATION_9":
        if len(innings) < 9:
            raise ValueError("regulation nine innings not completed")
        first_nine = innings[:9]
        home = sum(int(i.get("home", {}).get("runs") or 0) for i in first_nine)
        away = sum(int(i.get("away", {}).get("runs") or 0) for i in first_nine)
    else:
        raise ValueError("unsupported MLB endpoint")
    return FinalReceipt(str(game_pk), "FINAL", home, away, endpoint, url,
                        retrieved, checksum, f"home={home},away={away}")


def espn_final(league: str, event_id: str, endpoint: str = "FINAL_SCORE") -> FinalReceipt:
    if league not in ESPN_PATHS:
        raise ValueError("league adapter not approved")
    if endpoint != "FINAL_SCORE":
        raise ValueError("ESPN adapter only certifies full final score")
    url = f"https://site.api.espn.com/apis/site/v2/sports/{ESPN_PATHS[league]}/summary?event={event_id}"
    obj, checksum, retrieved = _fetch(url)
    header = obj.get("header", {})
    competition = header.get("competitions", [{}])[0]
    if str(competition.get("id", header.get("id", ""))) != str(event_id):
        raise ValueError("ESPN event ID mismatch")
    state = competition.get("status", {}).get("type", {})
    if not state.get("completed") or state.get("name") not in {"STATUS_FINAL", "STATUS_FINAL_OT", "STATUS_FINAL_SO"}:
        raise ValueError(f"ESPN feed not final: {state}")
    competitors = {c["homeAway"]: c for c in competition["competitors"]}
    if set(competitors) != {"home", "away"}:
        raise ValueError("missing ESPN competitors")
    home = int(float(competitors["home"]["score"]))
    away = int(float(competitors["away"]["score"]))
    return FinalReceipt(str(event_id), "FINAL", home, away, endpoint, url,
                        retrieved, checksum, f"home={home},away={away}")


def nbl_final(event_id: str, season_start_year: int,
              endpoint: str = "INCL_OVERTIME") -> FinalReceipt:
    """Exact regular-season final from the league schedule API.

    The season year is explicit so an event cannot be matched by team/date
    guesswork. A second terminal lineage still belongs in the card receipt.
    """
    if endpoint != "INCL_OVERTIME" or not 2021 <= season_start_year <= 2100:
        raise ValueError("unsupported NBL endpoint or season")
    url = ("https://schedule.nbl.com.au/api/calendar/schedule?league=NBL"
           f"&limit=500&offset=0&year={season_start_year}")
    obj, checksum, retrieved = _fetch(url)
    matches = obj.get("matches", [])
    if obj.get("total") != len(matches):
        raise ValueError("NBL schedule is paginated or incomplete")
    selected = [m for m in matches if str(m.get("id")) == str(event_id)]
    if len(selected) != 1:
        raise ValueError("NBL event ID absent or duplicated")
    match = selected[0]
    if match.get("season_type") != "regular" or match.get("phase") != "complete":
        raise ValueError("NBL event is not a complete regular-season game")
    if match.get("home_score") is None or match.get("away_score") is None:
        raise ValueError("NBL completed event lacks scores")
    home, away = int(match["home_score"]), int(match["away_score"])
    return FinalReceipt(str(event_id), "FINAL", home, away, endpoint,
                        f"https://schedule.nbl.com.au/match?league=NBL&match={event_id}",
                        retrieved, checksum, f"home={home},away={away}")

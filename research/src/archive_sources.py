"""Hash-checked, market-free archive evidence and explicit source profiles.

Retrieval time proves custody, not historical pregame availability. A receipt alone
does not verify a game: callers must match the source event and owned fields.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import re
import html
from collections import defaultdict
from urllib.parse import urljoin
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_ROOT = ROOT / "Previous Sports Results"
CACHE = ARCHIVE_ROOT / "_football_research" / "sources"
OFFICIAL_CACHE = ARCHIVE_ROOT / "_custody" / "official_sources"
PARSER_VERSION = "archive-sources-v1"
SOURCE_PROFILES = {
    "afl_season_results": {"owner": "AFL Tables", "kind": "historical_results",
        "fields": ["event_date", "teams", "scores", "venue"],
        "url_template": "https://afltables.com/afl/seas/{year}.html"},
    "mlb_stats_api": {"owner": "MLB", "kind": "official_results",
        "fields": ["game_id", "teams", "scores", "start_time_utc"],
        "url_template": "https://statsapi.mlb.com/api/v1.1/game/{event_id}/feed/live"},
    "cfb_2025_dublin": {"owner": "Iowa State Athletics", "kind": "official_boxscore",
        "fields": ["event_date", "teams", "scores", "venue"],
        "url": "https://cyclones.com/sports/football/stats/2025/kansas-state/boxscore/17234"},
    "nfl_2025_brazil": {"owner": "NFL", "kind": "official_gamebook",
        "fields": ["event_date", "teams", "scores", "venue", "neutral_venue"],
        "url": "https://static.www.nfl.com/image/upload/v1757158720/gamecenter/f5919071-311e-11f0-b670-ae1250fadad1.pdf"},
    "aflw_2023_port_practice": {"owner": "AFL", "kind": "official_report", "fields": ["teams", "scores", "venue"],
        "url": "https://www.afl.com.au/aflw/news/1013712/aflw-practice-match-wrap-swans-stun-blues-power-impress-roos-make-statement"},
    "aflw_2023_north_practice": {"owner": "North Melbourne", "kind": "official_club_report", "fields": ["teams", "scores", "venue"],
        "url": "https://www.nmfc.com.au/news/1407407/aflw-practice-match-report-north-melbourne-v-western-bulldogs"},
    "aflw_2025_north_practice": {"owner": "North Melbourne", "kind": "official_club_report", "fields": ["teams", "scores", "venue"],
        "url": "https://www.nmfc.com.au/news/1846772/aflw-practice-match-report-north-melbourne-essendon"},
}


class EvidenceError(ValueError):
    """A receipt is missing, ambiguous, or fails body custody verification."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    try:
        tmp.write_bytes(data)
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def read_receipt(receipt_path: Path) -> tuple[dict, bytes]:
    """Verify every retained body on read; never trust a filename or stale flag."""
    receipt_path = Path(receipt_path)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    name = receipt.get("stored_body", "")
    if not name or Path(name).name != name:
        raise EvidenceError("Receipt has no safely retained source body")
    body_path = receipt_path.parent / name
    if not body_path.is_file():
        raise EvidenceError("Receipt body is missing")
    try:
        body = gzip.decompress(body_path.read_bytes())
    except (OSError, EOFError) as exc:
        raise EvidenceError("Receipt body is not readable gzip") from exc
    expected = receipt.get("stored_sha256", "")
    if not expected or sha256(body) != expected:
        raise EvidenceError("Stored source body SHA-256 mismatch")
    if not receipt.get("url") or int(receipt.get("http_status", 0)) != 200:
        raise EvidenceError("Receipt has no successful source URL/status")
    if receipt_path.stem != sha256(receipt["url"].encode("utf-8")):
        raise EvidenceError("Receipt filename does not match its source URL")
    return receipt, body


def fetch_official(profile_id: str, cache_dir: Path = OFFICIAL_CACHE) -> Path:
    profile = SOURCE_PROFILES[profile_id]
    url = profile.get("url")
    if not url:
        raise EvidenceError("This profile requires an event-specific URL")
    return fetch_url(url, profile["owner"], profile_id, cache_dir)


def fetch_url(url: str, owner: str, profile_id: str, cache_dir: Path = OFFICIAL_CACHE) -> Path:
    """Retain exact official sports-only result responses, keyed by URL."""
    if not (url.startswith("https://statsapi.mlb.com/api/v1/schedule?") or
            url in [p.get("url") for p in SOURCE_PROFILES.values()]):
        raise EvidenceError("URL is outside supported official sports result endpoints")
    key = sha256(url.encode("utf-8"))
    receipt_path = cache_dir / (key + ".json")
    if receipt_path.exists():
        read_receipt(receipt_path)
        return receipt_path
    request = Request(url, headers={"User-Agent": "SportsResearchArchive/1.0 (historical source verification)"})
    with urlopen(request, timeout=60) as response:
        body = response.read()
        status = response.status
        content_type = response.headers.get("Content-Type", "")
    if status != 200:
        raise EvidenceError(f"Source HTTP status {status}")
    # Evidence consists of sports results; do not persist odds/market material.
    # Official boxscores/gamebooks are the only fetchable fixed profiles here.
    receipt = {"url": url, "source_profile": profile_id, "owner": owner,
        "retrieved_utc": datetime.now(timezone.utc).isoformat(), "http_status": status,
        "content_type": content_type, "transport_sha256": sha256(body),
        "stored_sha256": sha256(body), "stored_body": key + ".gz",
        "historical_pregame_availability": "unknown", "parser_version": PARSER_VERSION}
    atomic_bytes(cache_dir / receipt["stored_body"], gzip.compress(body, mtime=0))
    atomic_bytes(receipt_path, (json.dumps(receipt, indent=2) + "\n").encode("utf-8"))
    read_receipt(receipt_path)
    return receipt_path


def mlb_schedule_url(year: int) -> str:
    return f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={year}-01-01&endDate={year}-12-31"


def _plain(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def parse_afl_tables(body: bytes, url: str) -> list[dict]:
    """Read team cells, numeric totals, date and exact match URL from season HTML."""
    document = body.decode("utf-8", errors="replace")
    result = []
    # Match only two-row game tables with their field-owner Match stats link.
    pattern = r'<table\b[^>]*style="font: 12px Verdana;"[^>]*>(.*?)</table>'
    for match in re.finditer(pattern, document, flags=re.I | re.S):
        table = match.group(1)
        game = re.search(r'href="([^\"]*/stats/games/[^\"]+)"', table, re.I)
        cells = [re.findall(r"<td\b[^>]*>(.*?)</td>", row, re.I | re.S)
                 for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", table, re.I | re.S)]
        if not game or len(cells) != 2 or any(len(row) < 4 for row in cells):
            continue
        try:
            date_text = _plain(cells[0][3])
            date_match = re.search(r"(\d{2}-[A-Za-z]{3}-\d{4})", date_text)
            if not date_match:
                continue
            event_date = datetime.strptime(date_match.group(1), "%d-%b-%Y").date().isoformat()
            first_score, second_score = int(_plain(cells[0][2])), int(_plain(cells[1][2]))
        except (ValueError, TypeError):
            continue
        venue = re.search(r'Venue:</b>\s*<a[^>]*>(.*?)</a>', cells[0][3], re.I | re.S)
        result.append({"event_date": event_date, "home_team": _plain(cells[0][0]),
            "away_team": _plain(cells[1][0]), "home_score": first_score,
            "away_score": second_score, "venue": _plain(venue.group(1)) if venue else "",
            "source_event_id": urljoin(url, game.group(1)), "start_time_utc": "",
            "stage": "", "season_id": event_date[:4], "status": "final"})
    return result


class EvidenceIndex:
    """Match exact result identity; field-owner metadata never supplies missing scores."""
    def __init__(self, archive_root: Path = ARCHIVE_ROOT, team_key=lambda x: x):
        self.root = archive_root
        self.team_key = team_key
        self.by_match = defaultdict(list)
        self.mlb = {}
        self.errors = []
        self.receipts_used = {}

    def key(self, date, home, away, hs, aws):
        return (date, tuple(sorted([(self.team_key(home), int(hs)), (self.team_key(away), int(aws))])))

    def _add(self, competition, event, path, receipt):
        event = dict(event)
        event.update({"source_url": receipt["url"], "source_receipt_path": str(path.relative_to(self.root.parent)).replace("\\", "/"),
            "source_body_sha256": receipt["stored_sha256"], "retrieved_at_utc": receipt.get("retrieved_utc", ""),
            "source_parser_version": PARSER_VERSION})
        self.receipts_used[str(path.relative_to(self.root.parent)).replace("\\", "/")] = receipt["stored_sha256"]
        if competition == "mlb":
            self.mlb[str(event["source_event_id"])] = event
        else:
            key = self.key(event["event_date"], event["home_team"], event["away_team"], event["home_score"], event["away_score"])
            self.by_match[(competition, key)].append(event)

    def load(self):
        cached = self.root / "_football_research" / "sources"
        official = self.root / "_custody" / "official_sources"
        for year in range(1900, 2027):
            url = f"https://afltables.com/afl/seas/{year}.html"
            path = receipt_for_url(url, (cached,))
            if path:
                try:
                    receipt, body = read_receipt(path)
                    for event in parse_afl_tables(body, url):
                        self._add("afl", event, path, receipt)
                except (EvidenceError, ValueError, OSError) as exc:
                    self.errors.append({"receipt": str(path), "error": str(exc)})
            path = receipt_for_url(mlb_schedule_url(year), (official,))
            if path:
                try:
                    receipt, body = read_receipt(path)
                    payload = json.loads(body)
                    for date in payload.get("dates", []):
                        for game in date.get("games", []):
                            if game.get("status", {}).get("abstractGameState") != "Final":
                                continue
                            teams = game["teams"]
                            if "score" not in teams["home"] or "score" not in teams["away"]:
                                continue
                            if any("name" not in teams[side].get("team", {}) for side in ["home", "away"]):
                                self.errors.append({"receipt": str(path), "source_event_id": game.get("gamePk"),
                                    "error": "source_record_missing_team_name;record_excluded"})
                                continue
                            event = {"source_event_id": str(game["gamePk"]), "event_date": game.get("officialDate", date["date"]),
                                "home_team": teams["home"]["team"]["name"], "away_team": teams["away"]["team"]["name"],
                                "home_team_source_id": str(teams["home"]["team"]["id"]), "away_team_source_id": str(teams["away"]["team"]["id"]),
                                "home_score": teams["home"]["score"], "away_score": teams["away"]["score"],
                                "start_time_utc": game.get("gameDate", ""), "venue": game.get("venue", {}).get("name", ""),
                                "stage": game.get("gameType", ""), "season_id": str(game.get("season", year)), "source_year": str(year), "status": "final"}
                            self._add("mlb", event, path, receipt)
                except (EvidenceError, ValueError, KeyError, OSError) as exc:
                    self.errors.append({"receipt": str(path), "error": str(exc)})
        # Process exact retained fixture responses, rather than trusting transformed JSON.
        metadata = self.root / "_football_research" / "afl_api.json"
        if metadata.exists():
            for season in json.loads(metadata.read_text(encoding="utf-8")):
                url = season.get("fixture_url", "")
                path = receipt_for_url(url, (cached,))
                if not path:
                    continue
                try:
                    receipt, body = read_receipt(path)
                    payload = json.loads(body)
                    matches = payload.get("matches", [])
                    competition = season.get("league", "").lower()
                    for game in matches:
                        if game.get("status") != "CONCLUDED":
                            continue
                        home, away = game["home"], game["away"]
                        if not home.get("score") or not away.get("score"):
                            continue
                        event = {"source_event_id": game.get("providerId", str(game["id"])),
                            "event_date": game["utcStartTime"][:10], "start_time_utc": game["utcStartTime"],
                            "home_team": home["team"]["name"], "away_team": away["team"]["name"],
                            "home_team_source_id": home["team"].get("providerId", ""), "away_team_source_id": away["team"].get("providerId", ""),
                            "home_score": home["score"]["totalScore"], "away_score": away["score"]["totalScore"],
                            "venue": game.get("venue", {}).get("name", ""), "stage": game.get("round", {}).get("name", ""),
                            "season_id": game.get("compSeason", {}).get("providerId", str(season["year"])), "source_year": str(season["year"]), "status": "final"}
                        self._add(competition, event, path, receipt)
                except (EvidenceError, ValueError, KeyError, OSError) as exc:
                    self.errors.append({"receipt": str(path), "error": str(exc)})
        facts_path = self.root / "_custody" / "verified_facts.json"
        if facts_path.exists():
            for fact in json.loads(facts_path.read_text(encoding="utf-8")):
                try:
                    path = self.root.parent / fact["source_receipt_path"]
                    receipt, _ = read_receipt(path)
                    if receipt["stored_sha256"] != fact["source_body_sha256"]:
                        raise EvidenceError("Manually verified fact receipt changed")
                    if fact.get("verification_method") != "manual_primary_source_event_and_fields":
                        raise EvidenceError("Unverified manual fact")
                    self._add(fact["competition_id"], fact, path, receipt)
                except (EvidenceError, ValueError, KeyError, OSError) as exc:
                    self.errors.append({"receipt": fact.get("source_receipt_path"), "error": str(exc)})
        return self

    def match(self, competition, date, home, away, hs, aws, source_id=""):
        if competition == "mlb":
            candidate = self.mlb.get(str(source_id))
            if candidate and candidate["event_date"] == date and candidate["home_score"] == hs and candidate["away_score"] == aws:
                return candidate
            return None
        candidates = self.by_match.get((competition, self.key(date, home, away, hs, aws)), [])
        if not candidates and competition == "afl" and "1987" <= date[:4] <= "1996":
            # The retired builder collapsed Brisbane Bears/Lions into "Brisbane".
            # Restore only an exact date/opponent/score match owned by that year's
            # retained AFL Tables result; Bears and Lions retain distinct team IDs.
            corrected_home = "Brisbane Bears" if self.team_key(home) == "brisbane lions" else home
            corrected_away = "Brisbane Bears" if self.team_key(away) == "brisbane lions" else away
            repaired = self.by_match.get((competition, self.key(date, corrected_home, corrected_away, hs, aws)), [])
            if len({candidate["source_event_id"] for candidate in repaired}) == 1:
                candidates = [dict(candidate, identity_repair_note="legacy_brisbane_alias_restored_to_field_owner_bears") for candidate in repaired]
        ids = {c["source_event_id"] for c in candidates}
        return candidates[0] if len(ids) == 1 else None


def receipt_for_url(url: str, cache_dirs: tuple[Path, ...] = (CACHE, OFFICIAL_CACHE)) -> Path | None:
    key = sha256(url.encode("utf-8"))
    for directory in cache_dirs:
        path = directory / (key + ".json")
        if path.exists():
            return path
    return None


def audit_receipts(archive_root: Path = ARCHIVE_ROOT) -> dict:
    """Verify all retained football/official source bodies, including unused evidence."""
    result = {"receipt_count": 0, "retained_bodies_verified": 0, "body_not_retained": 0, "errors": [], "receipts": {}}
    for directory in [archive_root / "_football_research/sources", archive_root / "_custody/official_sources"]:
        if not directory.exists():
            continue
        for item in os.scandir(directory):
            if not item.is_file() or not item.name.endswith(".json"):
                continue
            path = Path(item.path)
            result["receipt_count"] += 1
            try:
                receipt = json.loads(path.read_text(encoding="utf-8"))
                relative = str(path.relative_to(archive_root.parent)).replace("\\", "/")
                custody = {"receipt_sha256": sha256(path.read_bytes()), "url": receipt.get("url", ""),
                    "stored_body": receipt.get("stored_body", ""), "stored_sha256": receipt.get("stored_sha256", "")}
                if str(receipt.get("stored_body", "")).startswith("not retained"):
                    if path.stem != sha256(receipt["url"].encode()) or not receipt.get("transport_sha256"):
                        raise EvidenceError("Unretained-body receipt identity is invalid")
                    result["body_not_retained"] += 1
                    result["receipts"][relative] = custody
                    continue
                read_receipt(path)
                custody["stored_gzip_sha256"] = sha256((path.parent / receipt["stored_body"]).read_bytes())
                result["receipts"][relative] = custody
                result["retained_bodies_verified"] += 1
            except (EvidenceError, OSError, ValueError, KeyError) as exc:
                result["errors"].append({"receipt": str(path.relative_to(archive_root.parent)).replace("\\", "/"), "error": str(exc)})
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["profiles", "verify", "fetch", "fetch-mlb"])
    parser.add_argument("value", nargs="?")
    args = parser.parse_args(argv)
    if args.command == "profiles":
        print(json.dumps(SOURCE_PROFILES, indent=2))
    elif args.command == "verify":
        receipt, _ = read_receipt(Path(args.value))
        print(json.dumps({"verified": True, "url": receipt["url"], "stored_sha256": receipt["stored_sha256"]}))
    elif args.command == "fetch":
        print(fetch_official(args.value))
    else:
        year = int(args.value)
        if not 1900 <= year <= 2100:
            raise EvidenceError("Invalid archive year")
        print(fetch_url(mlb_schedule_url(year), "MLB", "mlb_stats_api_schedule"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

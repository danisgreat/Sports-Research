"""Permitted NBA standings alternate, with rounded published rates explicitly labelled as proxies."""
from html.parser import HTMLParser
import math

from ml import source_access

URL = "https://www.foxsports.com/nba/standings"
TEAMS = dict(zip(
    ("76ers", "Celtics", "Pistons", "Hawks", "Knicks", "Raptors", "Cavaliers", "Wizards", "Heat", "Hornets", "Pacers", "Magic", "Nets", "Bulls", "Bucks",
     "Thunder", "Spurs", "Lakers", "Warriors", "Timberwolves", "Rockets", "Grizzlies", "Trail Blazers", "Nuggets", "Mavericks", "Pelicans", "Suns", "Clippers", "Kings", "Jazz"),
    ("Philadelphia 76ers", "Boston Celtics", "Detroit Pistons", "Atlanta Hawks", "New York Knicks", "Toronto Raptors", "Cleveland Cavaliers", "Washington Wizards", "Miami Heat", "Charlotte Hornets", "Indiana Pacers", "Orlando Magic", "Brooklyn Nets", "Chicago Bulls", "Milwaukee Bucks",
     "Oklahoma City Thunder", "San Antonio Spurs", "Los Angeles Lakers", "Golden State Warriors", "Minnesota Timberwolves", "Houston Rockets", "Memphis Grizzlies", "Portland Trail Blazers", "Denver Nuggets", "Dallas Mavericks", "New Orleans Pelicans", "Phoenix Suns", "Los Angeles Clippers", "Sacramento Kings", "Utah Jazz")))


class _Table(HTMLParser):
    def __init__(self):
        super().__init__(); self.rows = []; self.cells = None; self.cell = None; self.buf = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr": self.cells = {}
        if tag == "td" and self.cells is not None:
            self.cell = dict(attrs).get("data-index"); self.buf = []

    def handle_data(self, text):
        if self.cell is not None: self.buf.append(text)

    def handle_endtag(self, tag):
        if tag == "td" and self.cell is not None:
            self.cells[self.cell] = " ".join(" ".join(self.buf).split()); self.cell = None
        if tag == "tr" and self.cells is not None:
            if self.cells: self.rows.append(self.cells)
            self.cells = None


def parse(raw: bytes) -> list[dict]:
    table = _Table(); table.feed(raw.decode("utf8"))
    teams = []
    for row in table.rows:
        if not {"1", "2", "5", "6"} <= row.keys(): continue
        nickname = row["1"]
        if nickname not in TEAMS: raise ValueError(f"standings alternate: unknown team {nickname!r}")
        wins, losses = (int(v) for v in row["2"].split("-"))
        n = wins + losses; pf, pa = float(row["5"]), float(row["6"])
        if n < 0 or not all(math.isfinite(v) and 0 <= v <= 200 for v in (pf, pa)):
            raise ValueError("standings alternate: invalid record or points per game")
        teams.append(dict(team=TEAMS[nickname], n=float(n), pf=pf * n, pa=pa * n))
    if len(teams) != 30 or len({r["team"] for r in teams}) != 30:
        raise ValueError("standings alternate: all 30 unique NBA teams required")
    return teams


def fetch():
    raw = source_access.fetch_bytes(URL, user_agent="SportsResearch standings read", timeout=45)
    return raw, parse(raw)

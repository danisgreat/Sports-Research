"""Load league results from the raw yearly archive CSVs into one normalised table.

Rows are LABEL_B (observed archive fields; see ML_RL_IMPLEMENTATION_FRAMEWORK §7.1) unless the
league's canonical admission says otherwise. Every row that cannot be parsed or fails the archive's
own arithmetic (total and margin columns) is dropped and counted, never guessed.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

from ml.config import ARCHIVE, League, is_placeholder_zero

csv.field_size_limit(10**9)

COLUMNS = ["league", "season", "date", "stage", "event_id", "home", "away", "hs", "as_", "reg_hs", "reg_as",
           "decision"]


@dataclass
class LoadReport:
    league: str
    files: int = 0
    rows_read: int = 0
    rows_kept: int = 0
    dropped: dict = field(default_factory=dict)

    def drop(self, reason: str) -> None:
        self.dropped[reason] = self.dropped.get(reason, 0) + 1


def stage_of(value: str) -> str:
    v = (value or "").strip().lower()
    if not v or v == "not applicable":
        return "OTHER"
    if "regular season" in v or v == "league":
        return "REG"
    if v.startswith("pre") or "exhibition" in v or "spring" in v or "all-star" in v or "blitz" in v:
        return "PRE"
    return "POST"


def _tokens(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in {"the", "fc", "club"}}


SCORE_TEXT_ALIASES = {
    "GWS GIANTS": "Greater Western Sydney", "GWS Giants": "Greater Western Sydney",
    "Gold Coast SUNS": "Gold Coast", "Gold Coast Suns": "Gold Coast", "Sydney Swans": "Sydney",
    "Adelaide Crows": "Adelaide", "Geelong Cats": "Geelong", "West Coast Eagles": "West Coast",
    "Kangaroos": "North Melbourne",
}


def _which(text: str, home: str, away: str) -> str | None:
    """Exact name (after aliasing) first, then Jaccard similarity of name tokens; ties are unmatched."""
    t = SCORE_TEXT_ALIASES.get(text.strip(), text.strip())
    if t == home:
        return "home"
    if t == away:
        return "away"
    th, ta, tx = _tokens(home), _tokens(away), _tokens(t)
    jh = len(th & tx) / max(len(th | tx), 1)
    ja = len(ta & tx) / max(len(ta | tx), 1)
    if abs(jh - ja) < 1e-12 or max(jh, ja) == 0:
        return None
    return "home" if jh > ja else "away"


AFL_RE = re.compile(r"^(?P<t1>.*?)\s+\d+\.\d+\s+\((?P<p1>\d+)\)\s+(?P<verb>def\. by|def\.|drew with)\s+"
                    r"(?P<t2>.*?)\s+\d+\.\d+\s+\((?P<p2>\d+)\)\s*$")
NFL_RE = re.compile(r"^(?P<t1>.*?)\s+(?P<p1>\d+)\s+(?P<verb>def\. by|def\.|tied|drew with|vs\.?)\s+"
                    r"(?P<t2>.*?)\s+(?P<p2>\d+)\s*$")
DASH_RE = re.compile(r"^(?P<p1>\d+)\s*[-–]\s*(?P<p2>\d+)$")


def _parse_text(row: dict, lg: League, rep: LoadReport) -> tuple[int, int] | None:
    c = lg.columns
    gs = (row.get(c["score_text"]) or "").strip()
    m = AFL_RE.match(gs) or NFL_RE.match(gs)
    if not m:
        rep.drop("score_text_unparsed")
        return None
    p1, p2 = int(m["p1"]), int(m["p2"])
    first = _which(m["t1"], row[c["home"]], row[c["away"]])
    second = _which(m["t2"], row[c["home"]], row[c["away"]])
    if first is None or second is None or first == second:
        rep.drop("score_text_team_unmatched")
        return None
    hs, as_ = (p1, p2) if first == "home" else (p2, p1)
    try:
        tot = int(float(row.get(c["total"] or "", "") or "nan"))
        mar = int(float(row.get(c["margin"] or "", "") or "nan"))
        if tot != hs + as_ or mar != abs(hs - as_):
            rep.drop("score_text_arithmetic_conflict")
            return None
    except ValueError:
        pass  # columns blank: the parsed text is the only evidence; kept
    return hs, as_


def _yes(v) -> bool:
    return (v or "").strip().lower() not in ("", "no", "n", "0", "false", "none", "nan", "regulation")


def _hockey_decision(row: dict, lg: League) -> str:
    c = lg.columns
    if c["decision"]:
        d = (row.get(c["decision"]) or "").strip()
        return {"regulation": "Regulation", "overtime": "Overtime", "shootout": "Shootout"}.get(d.lower(), d)
    so = c["shootout"] and _yes(row.get(c["shootout"]))
    ot = c["overtime"] and _yes(row.get(c["overtime"]))
    return "Shootout" if so else ("Overtime" if ot else "Regulation")


def load_league(lg: League | str, seasons: list[int] | None = None) -> tuple[pd.DataFrame, LoadReport]:
    if isinstance(lg, str):
        from ml.config import get_league
        lg = get_league(lg)
    c = lg.columns
    rep = LoadReport(lg.path)
    rows = []
    files = sorted(p for p in (ARCHIVE / lg.path).glob("*/*_games.csv") if p.parent.name.isdigit())
    for f in files:
        season = int(f.parent.name)
        if seasons is not None and season not in seasons:
            continue
        with open(f, newline="", encoding="utf-8-sig", errors="replace") as fh:
            got = False
            for row in csv.DictReader(fh):
                got = True
                rep.rows_read += 1
                stage = stage_of(row.get(c["stage"], "")) if c["stage"] else "REG"
                gt = (row.get("Game Type") or "")
                if "all-star" in gt.lower():
                    stage = "OTHER"
                date = pd.to_datetime(row.get(c["date"]), errors="coerce") if c["date"] else pd.NaT
                if pd.isna(date):
                    rep.drop("invalid_date")
                    continue
                raw_h = (row.get(c["home"]) or "").strip()
                raw_a = (row.get(c["away"]) or "").strip()
                home, away = lg.aliases.get(raw_h, raw_h), lg.aliases.get(raw_a, raw_a)
                if not home or not away or home == away:
                    rep.drop("invalid_team_identity")
                    continue
                if c["parser"] == "columns":
                    try:
                        hs = int(float(row[c["home_score"]]))
                        as_ = int(float(row[c["away_score"]]))
                    except (TypeError, ValueError, KeyError):
                        rep.drop("missing_numeric_score")
                        continue
                else:
                    res = _parse_text(row, lg, rep)
                    if res is None:
                        continue
                    hs, as_ = res
                if hs < 0 or as_ < 0:
                    rep.drop("negative_score")
                    continue
                ext = bool(c["extras"]) and (row.get(c["extras"]) or "").strip().upper() in ("Y", "YES")
                if is_placeholder_zero(lg.sport, hs, as_, ext):
                    rep.drop("zero_zero_placeholder")
                    continue
                decision = ""
                reg_hs, reg_as = hs, as_
                if lg.tie_rule == "hockey_regulation":
                    decision = _hockey_decision(row, lg)
                    if decision in ("Overtime", "Shootout"):
                        if abs(hs - as_) != 1:
                            rep.drop("ot_margin_not_one")
                            continue
                        reg_hs = reg_as = min(hs, as_)
                    elif decision != "Regulation":
                        rep.drop("unknown_decision")
                        continue
                    elif hs == as_ and stage == "REG":
                        decision = "Tie"  # a genuine regulation tie in a league/era without OT/SO
                elif lg.tie_rule == "extras" and c["extras"] and _yes(row.get(c["extras"])):
                    decision = "EXTRAS"
                eid = (row.get(c["id"]) or "").strip() if c["id"] else ""
                if not eid:
                    eid = f"{lg.model_id}:{date.date()}:{home}:{away}"
                rows.append((lg.competition, season, date, stage, eid, home, away, hs, as_, reg_hs, reg_as, decision))
            if got:
                rep.files += 1
    df = pd.DataFrame(rows, columns=COLUMNS)
    before = len(df)
    df = df.drop_duplicates(subset=["event_id"], keep="first")
    if len(df) < before:
        rep.dropped["duplicate_event_id"] = before - len(df)
    if lg.sport != "Baseball":  # baseball doubleheaders keep native IDs; elsewhere identical rows are copies
        dup = df.duplicated(subset=["date", "home", "away", "hs", "as_"], keep="first")
        if dup.any():
            rep.dropped["duplicate_identity"] = int(dup.sum())
            df = df[~dup]
    df = df.sort_values(["date", "event_id"]).reset_index(drop=True)
    rep.rows_kept = len(df)
    return df, rep


def training_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Regular season and post-season results are both evidence about strength; pre-season is not."""
    return df[df["stage"].isin(["REG", "POST"])]


def file_sha256(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot_hash(lg: League, seasons: list[int]) -> str:
    """SHA-256 over the ordered (path, file hash) list of the archive files a fit read."""
    import hashlib

    h = hashlib.sha256()
    for s in sorted(seasons):
        p = ARCHIVE / lg.path / str(s) / f"{s}_games.csv"
        if p.exists():
            h.update(f"{p.relative_to(ARCHIVE).as_posix()}:{file_sha256(p)}\n".encode())
    return h.hexdigest()


def seasons_available(lg: League) -> list[int]:
    return sorted(int(p.parent.name) for p in (ARCHIVE / lg.path).glob("*/*_games.csv") if p.parent.name.isdigit())

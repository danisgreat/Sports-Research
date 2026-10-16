"""Synthetic EXAMPLE research exports for the learning-pipeline tests (not sporting evidence)."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from ml import primary as p
from ml import research_ingest as ri
from ml.tests.test_models import synthetic

COMPETITION = "Basketball/EXAMPLE-LEARN"
ENDPOINT = "FULL_GAME_INCL_OT"


def capture(folder: Path, name: str = "capture.txt", text: str = "EXAMPLE synthetic capture") -> tuple[str, str]:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    path.write_text(text, encoding="utf-8")
    return str(path), p.digest(path.read_bytes())


def season_frame(n_teams: int = 6, seasons=(2025,), seed: int = 3) -> pd.DataFrame:
    frame, _, _ = synthetic(n_teams=n_teams, seasons=seasons, seed=seed, kind="normal")
    frame = frame.copy()
    # One game per team per day at most: spread games over consecutive days at 10:00 UTC.
    frame["event_at"] = [pd.Timestamp("2025-10-01T10:00:00Z") + pd.Timedelta(days=i // 3) for i in range(len(frame))]
    frame["native_event_id"] = [f"EX-{i:04d}" for i in range(len(frame))]
    return frame


def game_row(r, cap: tuple[str, str], *, source="https://example.org/box", kind="WEB_RECOVERED", known_hours=3,
             collected_by="LOCAL-EXAMPLE-G0001", **override) -> dict:
    at = pd.Timestamp(r.event_at)
    row = dict(competition=COMPETITION, endpoint=ENDPOINT, native_event_id=r.native_event_id, season=str(r.season),
               event_at=at.isoformat(), home=r.home, away=r.away, venue="", status="FINAL",
               hs=str(r.hs), as_=str(r.as_), reg_hs=str(r.reg_hs), reg_as=str(r.reg_as), decision="",
               final_at=(at + pd.Timedelta(hours=2)).isoformat(), source_url=source, source_kind=kind,
               published_at=(at + pd.Timedelta(hours=known_hours)).isoformat(),
               retrieved_at=(at + pd.Timedelta(hours=known_hours + 1)).isoformat(),
               known_at=(at + pd.Timedelta(hours=known_hours)).isoformat(), capture_path=cap[0],
               capture_sha256=cap[1], review_status="RESEARCH_INPUT_REVIEWED", collected_by=collected_by)
    row.update(override)
    return row


def write_export(folder: Path, games=(), stats=(), avail=(), target=()) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for name, rows in (("GAME_OBSERVATIONS.csv", games), ("TEAM_GAME_STATS.csv", stats),
                       ("AVAILABILITY.csv", avail), ("TARGET_EVENT.csv", target)):
        rows = list(rows)
        if rows:
            (folder / name).write_bytes(p.csv_bytes(rows))
        else:
            (folder / name).write_text(",".join(ri.EXPORT_FILES[name]) + "\n", encoding="utf-8")
    return folder


def ingest_frame(tmp: Path, store: Path, frame: pd.DataFrame, name: str, cap=None, **kw) -> dict:
    cap = cap or capture(tmp / "captures")
    export = write_export(tmp / "exports" / name, games=[game_row(r, cap, **kw) for r in frame.itertuples()])
    return ri.ingest(export, store)

"""REV-06: the full-league day freezes every open fixture. Network and parameter lookups are replaced by synthetic inputs."""
from datetime import datetime, timedelta, timezone

import pytest

from ml import chat, league_day as LD, pregame, reference as R
from ml.evaluation import prospective as PS
from ml.tests.test_chat_execution import runtime  # noqa: F401  (pytest fixture)
from ml.tests import learning_fixtures as lf


def _slate(rt, now):
    future = now + timedelta(hours=20)
    base = dict(season_type=2, season="2026", venue="EXAMPLE-ARENA", source_url="https://example.org/scoreboard",
                receipt=dict(raw_sha256="a" * 64, retrieved_at=now.isoformat(), source_url="https://example.org/scoreboard"))
    return [dict(base, event_id="900001", start=future, state="pre", home="T00", away="T01", open=True),
            dict(base, event_id="900002", start=now - timedelta(hours=1), state="in", home="T02", away="T03", open=False),
            dict(base, event_id="900003", start=future, state="pre", home="T02", away="T03", open=True, season_type=1)]


@pytest.fixture
def lane(runtime, monkeypatch):
    clock = datetime.now(timezone.utc)
    monkeypatch.setattr(LD, "fixtures", lambda competition, date, cache, now=None: _slate(runtime, clock))
    monkeypatch.setattr(LD, "total_line", lambda competition, root=None: 200.5)
    monkeypatch.setattr(R, "league_key", lambda competition: "NBL")
    standings = ("role,team,pf,pa,n\nHOME,T00,1195,1102,13\nAWAY,T01,1150,1231,13\nLEAGUE,ALL,18250,18250,200\n").encode()
    monkeypatch.setattr(R, "standings_csv", lambda competition, home, away, cache=None: (standings, dict(source_url="https://example.org/standings")))
    monkeypatch.setattr(R, "parameter_row", lambda competition, root=None: None)
    monkeypatch.setattr(R, "reference_choice", lambda competition, root=None: dict(reference_model="TB2-MD"))
    return runtime


def test_the_day_needs_the_outcome_confirmation_and_a_release(lane):
    with pytest.raises(LD.LeagueDayError, match="confirm-no-outcome-seen"):
        LD.run(lf.COMPETITION, "2026-11-01", lane["work"], root=lane["root"])
    with pytest.raises(LD.LeagueDayError, match="no active release"):
        LD.run("Basketball/EXAMPLE-UNRELEASED", "2026-11-01", lane["work"], confirmed=True, root=lane["root"])


def test_open_fixtures_are_frozen_with_the_model_the_baseline_and_the_tb2_reference(lane):
    rows = LD.run(lf.COMPETITION, "2026-11-01", lane["work"] / "cache", confirmed=True, root=lane["root"])
    done = [r for r in rows if r.get("model_status") == "EXECUTED"]
    assert len(done) == 1 and done[0]["local_key"].startswith("LOCAL-LEAGUE-NBL-20261101-G0001") and done[0]["reference_status"].startswith("EXECUTED:TB2-MD")
    assert sorted(r["status"] for r in rows if "status" in r) == ["SKIPPED", "SKIPPED"]          # a started game and a preseason fixture
    ledger = PS.verify_ledger(lane["root"] / chat.LEDGER)
    by = {}
    for r in ledger:
        by.setdefault(r["model_id"], []).append(r)
    assert len(by["RESEARCH_FORECAST_CYCLE_V1"]) == 2 and len(by[pregame.REFERENCE_MODEL]) == 2
    assert {r["evidence_status"] for r in ledger} == {"PRE_START_VERIFIED"}
    assert {r["contract_key"] for r in by[pregame.REFERENCE_MODEL]} == {r["contract_key"] for r in by["RESEARCH_FORECAST_CYCLE_V1"]}
    receipts = list((lane["root"] / pregame.RECEIPTS / done[0]["local_key"]).glob("*"))
    assert any(p.name.endswith("_REFERENCE_CYCLE.csv") for p in receipts) and any(p.name.endswith("_REFERENCE_ROWS.csv") for p in receipts)


def test_total_line_is_the_half_point_below_the_verified_mean(monkeypatch, tmp_path):
    monkeypatch.undo()
    monkeypatch.setattr(R, "parameter_row", lambda competition, root=None: dict(store_mean_total="229.15", mean_total="228"))
    assert LD.total_line("Basketball/NBA") == 229.5
    monkeypatch.setattr(R, "parameter_row", lambda competition, root=None: None)
    with pytest.raises(LD.LeagueDayError):
        LD.total_line("Basketball/NBA")


def test_settle_day_ingests_finals_once_and_settles_each_frozen_bundle(lane):
    LD.run(lf.COMPETITION, "2026-11-01", lane["work"] / "cache", confirmed=True, root=lane["root"])
    calls = []

    def fake_backfill(league, start, end, cache, out, store):
        calls.append(("backfill", league, start, end))
        (out / "EXPORT").mkdir(parents=True)
        return dict(verified=1, not_ingested=0, owner_games=1)

    def fake_settle(bundle, export, store, output):
        calls.append(("settle", bundle.parent.parent.name, export.name))
        output.mkdir(parents=True)

    LD.BB.LEAGUES["example"] = dict(competition=lf.COMPETITION)
    try:
        rows = LD.settle_day(lf.COMPETITION, "2026-11-01", lane["work"] / "cache", root=lane["root"], backfill=fake_backfill, settle=fake_settle)
        again = LD.settle_day(lf.COMPETITION, "2026-11-01", lane["work"] / "cache", root=lane["root"], backfill=fake_backfill, settle=fake_settle)
    finally:
        del LD.BB.LEAGUES["example"]
    assert [r["status"] for r in rows] == ["INGESTED", "SETTLED"] and calls[0][0] == "backfill" and calls[1] == ("settle", "LOCAL-LEAGUE-NBL-20261101-G0001", "EXPORT")
    assert [r["status"] for r in again] == ["ALREADY_SETTLED"] and len(calls) == 2         # nothing is fetched or settled twice


def test_a_failed_settlement_is_recorded_and_leaves_the_bundle_open(lane):
    LD.run(lf.COMPETITION, "2026-11-01", lane["work"] / "cache", confirmed=True, root=lane["root"])

    def fake_backfill(league, start, end, cache, out, store):
        (out / "EXPORT").mkdir(parents=True)
        return dict(verified=0, not_ingested=1, owner_games=1)

    def refusing_settle(bundle, export, store, output):
        raise ValueError("one verified final result required")

    LD.BB.LEAGUES["example"] = dict(competition=lf.COMPETITION)
    try:
        rows = LD.settle_day(lf.COMPETITION, "2026-11-01", lane["work"] / "cache", root=lane["root"], backfill=fake_backfill, settle=refusing_settle)
    finally:
        del LD.BB.LEAGUES["example"]
    assert rows[-1]["status"] == "NOT_SETTLED" and "verified final" in rows[-1]["detail"]
    assert not (lane["root"] / "research" / "cycle_feedback" / "LOCAL-LEAGUE-NBL-20261101-G0001_REV1").exists()


def test_settle_day_without_a_mapped_backfill_is_refused(lane):
    with pytest.raises(LD.LeagueDayError, match="no two-lineage backfill"):
        LD.settle_day("Soccer/Premier League", "2026-11-01", lane["work"], root=lane["root"])

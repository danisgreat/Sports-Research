"""LEARN-v1 store, point-in-time features and immutable releases (EXAMPLE data, not sporting evidence)."""
import math

import pandas as pd
import pytest

from ml import features as F
from ml import primary as p
from ml import research_ingest as ri
from ml import training_admission as ta
from ml.tests import learning_fixtures as lf


@pytest.fixture
def season():
    return lf.season_frame()


def test_same_match_researched_five_times_is_one_event_with_its_source_observations(tmp_path, season):
    store = tmp_path / "store"
    game = season.iloc[[0]]
    for k in range(5):  # five minis, each with its own capture of the same box score
        cap = lf.capture(tmp_path / f"cap{k}", text=f"EXAMPLE capture {k}")
        lf.ingest_frame(tmp_path, store, game, f"mini{k}", cap=cap, collected_by=f"LOCAL-M{k}-G0001")
    st = ri.load_store(store)
    assert len(st.events) == 1 and len(ri.effective_results(st)) == 1
    assert (st.source_observations.disposition == "CORROBORATING").sum() == 4
    rec = lf.ingest_frame(tmp_path, store, game, "mini0-again", cap=lf.capture(tmp_path / "cap0", text="EXAMPLE capture 0"),
                          collected_by="LOCAL-M0-G0001")
    assert rec["exact_duplicates"] == 1 and rec["observations"] == 0  # exact re-ingest adds nothing


def test_conflicts_are_quarantined_and_only_reviewed_corrections_revise(tmp_path, season):
    store, cap = tmp_path / "store", lf.capture(tmp_path)
    g = season.iloc[0]
    lf.ingest_frame(tmp_path, store, season.iloc[[0]], "first", cap=cap)
    wrong = lf.game_row(g, cap, hs=str(int(g.hs) + 2), reg_hs=str(int(g.reg_hs) + 2), source="https://example.org/other")
    rec = ri.ingest(lf.write_export(tmp_path / "x" / "conflict", games=[wrong]), store)
    assert rec["quarantined"] == 1 and "RESULT_CONFLICT" in ri.load_store(store).quarantine.reason.iloc[0]
    fixed = dict(wrong, source_kind="WEB_CORRECTED", known_at=(pd.Timestamp(g.event_at) + pd.Timedelta(days=3)).isoformat(),
                 published_at=(pd.Timestamp(g.event_at) + pd.Timedelta(days=3)).isoformat(),
                 retrieved_at=(pd.Timestamp(g.event_at) + pd.Timedelta(days=3, hours=1)).isoformat())
    assert ri.ingest(lf.write_export(tmp_path / "x" / "correction", games=[fixed]), store)["corrections"] == 1
    st = ri.load_store(store)
    before = ri.effective_results(st, pd.Timestamp(g.event_at) + pd.Timedelta(days=1))
    after = ri.effective_results(st)
    assert before.iloc[0].hs == str(g.hs) and after.iloc[0].hs == str(int(g.hs) + 2)  # point-in-time revisions


@pytest.mark.parametrize("defect", ["retired_archive", "archive_path", "unreviewed", "http", "chronology", "hash",
                                    "known_after_retrieval", "negative"])
def test_bad_observations_are_quarantined_with_reasons_never_dropped(tmp_path, season, defect):
    cap = lf.capture(tmp_path)
    row = lf.game_row(season.iloc[0], cap)
    row.update({"retired_archive": dict(source_kind="ARCHIVE_REVIEWED"),
                "archive_path": dict(capture_path="C:/x/Previous Sports Results/NBA/2025.csv"),
                "unreviewed": dict(review_status="UNREVIEWED"), "http": dict(source_url="http://example.org"),
                "chronology": dict(final_at=(pd.Timestamp(row["known_at"]) + pd.Timedelta(hours=1)).isoformat()),
                "hash": dict(capture_sha256="0" * 64),
                "known_after_retrieval": dict(retrieved_at=row["event_at"]),
                "negative": dict(hs="-1")}[defect])
    rec = ri.ingest(lf.write_export(tmp_path / "e", games=[row]), tmp_path / "store")
    st = ri.load_store(tmp_path / "store")
    assert rec["quarantined"] == 1 and len(st.quarantine) == 1 and ri.effective_results(st).empty


def test_exact_schema_rejects_market_columns_and_orientation_conflicts(tmp_path, season):
    cap = lf.capture(tmp_path)
    row = dict(lf.game_row(season.iloc[0], cap), closing_odds="1.90")
    folder = tmp_path / "market"
    folder.mkdir()
    (folder / "GAME_OBSERVATIONS.csv").write_bytes(p.csv_bytes([row]))
    with pytest.raises(p.AdmissionError, match="exact"):
        ri.ingest(folder, tmp_path / "store")
    lf.ingest_frame(tmp_path, tmp_path / "store", season.iloc[[0]], "ok", cap=cap)
    g = season.iloc[0]
    swapped = lf.game_row(g, cap, home=g.away, away=g.home, source="https://example.org/swap")
    rec = ri.ingest(lf.write_export(tmp_path / "swap", games=[swapped]), tmp_path / "store")
    assert rec["quarantined"] == 1
    assert "ORIENTATION_CONFLICT" in ri.load_store(tmp_path / "store").quarantine.reason.iloc[0]


def test_date_identity_gains_a_native_alias_instead_of_a_second_event(tmp_path, season):
    cap = lf.capture(tmp_path)
    g = season.iloc[0]
    ri.ingest(lf.write_export(tmp_path / "a", games=[lf.game_row(g, cap, native_event_id="")]), tmp_path / "s")
    ri.ingest(lf.write_export(tmp_path / "b", games=[lf.game_row(g, cap, source="https://example.org/2")]), tmp_path / "s")
    st = ri.load_store(tmp_path / "s")
    assert len(st.events) == 1 and len(st.event_aliases) == 1
    assert st.events.identity_basis.iloc[0] == "DATE_PARTICIPANTS"


def test_interrupted_ingest_rows_stay_invisible_and_their_sequence_is_never_reused(tmp_path, season):
    store = tmp_path / "store"
    lf.ingest_frame(tmp_path, store, season.iloc[:3], "a")
    ri._append(store / "RESULTS.csv", ri.STORE_FILES["RESULTS.csv"],
               [dict(event_uid="EORPHAN", revision="1", status="FINAL", hs="1", as_="0", reg_hs="1", reg_as="0",
                     decision="", final_at="", revision_basis="FIRST_OBSERVED", ingest_seq=2)])
    assert len(ri.load_store(store).results) == 3
    rec = lf.ingest_frame(tmp_path, store, season.iloc[3:5], "b")
    assert rec["ingest_seq"] == 3 and "EORPHAN" not in set(ri.load_store(store).results.event_uid)


def test_store_history_is_admissible_primary_history_at_the_horizon(tmp_path, season):
    lf.ingest_frame(tmp_path, tmp_path / "s", season, "a")
    st = ri.load_store(tmp_path / "s")
    horizon = season.event_at.iloc[40]
    rows = ri.history_rows(st, lf.COMPETITION, lf.ENDPOINT, horizon)
    train = p.admit_history(rows, horizon, "TARGET", lf.COMPETITION, lf.ENDPOINT)
    assert len(train) == len(rows) and train.date.max() < horizon.tz_localize(None).normalize()
    assert {r["source_kind"] for r in rows} == {"WEB_RECOVERED"}


def test_features_as_of_a_date_cannot_see_later_games_corrections_or_news(tmp_path, season):
    store, cap = tmp_path / "s", lf.capture(tmp_path)
    split = 30
    lf.ingest_frame(tmp_path, store, season.iloc[:split], "early", cap=cap)
    target = season.iloc[split + 5]
    as_of = pd.Timestamp(season.event_at.iloc[split]).normalize()
    tgt = dict(competition=lf.COMPETITION, endpoint=lf.ENDPOINT, native_event_id=target.native_event_id, season="2025",
               scheduled_start=target.event_at.isoformat(), home=target.home, away=target.away, venue="",
               source_url="https://example.org/fixture", known_at=(as_of - pd.Timedelta(days=5)).isoformat(),
               capture_path=cap[0], capture_sha256=cap[1], collected_by="LOCAL-EX-G0002")
    ri.ingest(lf.write_export(tmp_path / "t", target=[tgt]), store)
    st = ri.load_store(store)
    uid = st.events[st.events.native_event_id == target.native_event_id].event_uid.iloc[0]
    before = F.build(st, lf.COMPETITION, lf.ENDPOINT, target.home, target.away, as_of, target_event_uid=uid)
    later = (as_of + pd.Timedelta(days=1)).isoformat()
    g0 = season.iloc[0]
    correction = lf.game_row(g0, cap, hs=str(int(g0.hs) + 9), reg_hs=str(int(g0.reg_hs) + 9), source_kind="WEB_CORRECTED",
                             known_at=later, published_at=later, retrieved_at=(as_of + pd.Timedelta(days=2)).isoformat(),
                             source_url="https://example.org/correction")
    news = dict(competition=lf.COMPETITION, native_event_id=target.native_event_id, team=target.home, player="EXAMPLE A",
                role="STARTER", status="CONFIRMED_OUT", confirmation="OFFICIAL_CONFIRMED", published_at=later,
                retrieved_at=later, known_at=later, source_url="https://example.org/injury", capture_path=cap[0],
                capture_sha256=cap[1], review_status="RESEARCH_INPUT_REVIEWED", collected_by="LOCAL-EX-G0002")
    later_games = [lf.game_row(r, cap) for r in season.iloc[split:].itertuples()]
    ri.ingest(lf.write_export(tmp_path / "late", games=later_games + [correction], avail=[news]), store)
    st2 = ri.load_store(store)
    again = F.build(st2, lf.COMPETITION, lf.ENDPOINT, target.home, target.away, as_of, target_event_uid=uid)
    same = lambda x, y: x == y or (isinstance(x, float) and isinstance(y, float) and math.isnan(x) and math.isnan(y))
    assert set(again) == set(before) and all(same(again[k], before[k]) for k in before)
    now = F.build(st2, lf.COMPETITION, lf.ENDPOINT, target.home, target.away, target.event_at, target_event_uid=uid)
    assert now["home_confirmed_out"] == 1 and now["home_L20_net__n"] >= before["home_L20_net__n"]


def test_windows_report_true_n_and_unknown_availability_is_missing_not_healthy(tmp_path, season):
    lf.ingest_frame(tmp_path, tmp_path / "s", season.iloc[:6], "few")
    st = ri.load_store(tmp_path / "s")
    t = season.iloc[20]
    f = F.build(st, lf.COMPETITION, lf.ENDPOINT, t.home, t.away, t.event_at)
    assert f["home_L5_pf__n"] <= 5 and f["home_L20_pf__n"] <= 6  # never padded to the nominal window
    assert math.isnan(f["home_confirmed_out"]) and f["home_confirmed_out__missing"] == 1
    assert math.isnan(f["home_L10_pace"]) and f["home_L10_pace__missing"] == 1  # no possessions sourced


def test_possessions_are_derived_and_labelled_when_only_components_exist(tmp_path, season):
    cap = lf.capture(tmp_path)
    g = season.iloc[0]
    stats = [dict(competition=lf.COMPETITION, native_event_id=g.native_event_id, team=team, stat=s, value=v,
                  source_url="https://example.org/box", source_kind="WEB_RECOVERED", published_at="",
                  retrieved_at=(pd.Timestamp(g.event_at) + pd.Timedelta(hours=4)).isoformat(),
                  known_at=(pd.Timestamp(g.event_at) + pd.Timedelta(hours=3)).isoformat(), capture_path=cap[0],
                  capture_sha256=cap[1], review_status="RESEARCH_INPUT_REVIEWED", collected_by="LOCAL-EX-G0001")
             for team in (g.home, g.away) for s, v in (("FGA", "80"), ("ORB", "10"), ("TOV", "12"), ("FTA", "20"))]
    ri.ingest(lf.write_export(tmp_path / "e", games=[lf.game_row(g, cap)], stats=stats), tmp_path / "s")
    games = F.team_games(ri.load_store(tmp_path / "s"), lf.COMPETITION, lf.ENDPOINT, pd.Timestamp(g.event_at) + pd.Timedelta(days=2))
    assert games.poss.iloc[0] == pytest.approx(80 - 10 + 12 + 0.44 * 20) and set(games.poss_status) == {"DERIVED"}


def test_release_is_reproducible_immutable_and_explains_every_exclusion(tmp_path, season):
    store = tmp_path / "s"
    lf.ingest_frame(tmp_path, store, season, "all")
    a = ta.build_release(store, lf.COMPETITION, lf.ENDPOINT, tmp_path / "rel", "R1")
    b = ta.build_release(store, lf.COMPETITION, lf.ENDPOINT, tmp_path / "rel", "R2")
    assert (tmp_path / "rel/R1/ROWS.csv").read_bytes() == (tmp_path / "rel/R2/ROWS.csv").read_bytes()
    assert a["rows"] + a["excluded"] == len(season) and a["rows"] == b["rows"] > 0
    excl = p.read_rows(tmp_path / "rel/R1/EXCLUSIONS.csv")
    assert all(r["reason"].startswith("INSUFFICIENT_HISTORY") for r in excl)
    ta.verify_release(tmp_path / "rel/R1")  # rebuilds from the recorded store view
    with pytest.raises(FileExistsError):
        ta.build_release(store, lf.COMPETITION, lf.ENDPOINT, tmp_path / "rel", "R1")
    lf.ingest_frame(tmp_path, store, season.iloc[[0]], "later", cap=lf.capture(tmp_path / "c2", text="other"))
    ta.verify_release(tmp_path / "rel/R1")  # later ingests do not change a release built from an earlier view
    rows = tmp_path / "rel/R1/ROWS.csv"
    rows.write_bytes(rows.read_bytes() + b"tampered")
    with pytest.raises(p.AdmissionError):
        ta.verify_release(tmp_path / "rel/R1")

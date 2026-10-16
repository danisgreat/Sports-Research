"""End-to-end LEARN-v1 lifecycle on a synthetic competition (Improvement 24; EXAMPLE IDs, no live P-IDs).

research exports -> store -> primary forecast from store history -> later result -> settlement -> feedback ->
next forecast -> research-only game -> correction -> training release -> learning status.
"""
import math

import pandas as pd
import pytest

from ml import features as F
from ml import learning_status as LS
from ml import primary as p
from ml import research_ingest as ri
from ml import research_learning as rl
from ml import training_admission as ta
from ml.config import League
from ml.tests import learning_fixtures as lf

LG = League(lf.COMPETITION, "Basketball", "EXAMPLE-LEARN", "EX", "gaussian", endpoint=lf.ENDPOINT,
            tie_rule="overtime", extra_fraction=5 / 40)


def _contracts():
    winner = dict(family="winner", line="", endpoint=lf.ENDPOINT, definition="FROZEN_FRAMEWORK_CONVENTION",
                  action="THREE_WAY_DRAW_LOSES")
    total = dict(family="total", line="200.5", endpoint=lf.ENDPOINT, definition="FROZEN_FRAMEWORK_CONVENTION",
                 action="STANDARD_COMPLETED")
    return [dict(winner, contract_key="ML-H", side="HOME"), dict(winner, contract_key="ML-A", side="AWAY"),
            dict(total, contract_key="TOT-O", side="OVER"), dict(total, contract_key="TOT-U", side="UNDER")]


def _request(g, recipe="EXAMPLE_LIFECYCLE"):
    start = pd.Timestamp(g.event_at)
    return dict(event_id=g.native_event_id, competition=lf.COMPETITION, endpoint=lf.ENDPOINT, home=g.home, away=g.away,
                scheduled_start=start.isoformat(), issue_at=(start - pd.Timedelta(hours=1)).isoformat(),
                actual_start=start.isoformat(), outcome_exposure="NONE_RECORDED", candidate_recipe=recipe)


def _target(g, cap, mini):
    return dict(competition=lf.COMPETITION, endpoint=lf.ENDPOINT, native_event_id=g.native_event_id, season="2025",
                scheduled_start=pd.Timestamp(g.event_at).isoformat(), home=g.home, away=g.away, venue="",
                source_url="https://example.org/fixture", known_at=(pd.Timestamp(g.event_at) - pd.Timedelta(days=2)).isoformat(),
                capture_path=cap[0], capture_sha256=cap[1], collected_by=mini)


def _same(a, b):
    return set(a) == set(b) and all(a[k] == b[k] or (isinstance(a[k], float) and math.isnan(a[k]) and math.isnan(b[k])) for k in a)


def test_research_to_learning_lifecycle(tmp_path):
    season = lf.season_frame(n_teams=6)
    store, cap = tmp_path / "store", lf.capture(tmp_path / "caps")
    t1, t2, research_only = season.iloc[50], season.iloc[56], season.iloc[53]

    # Two minis research overlapping history; the second used different captures of the same box scores.
    mini_a = lf.write_export(tmp_path / "A", games=[lf.game_row(r, cap, collected_by="LOCAL-A-G0001") for r in season.iloc[:48].itertuples()],
                             target=[_target(t1, cap, "LOCAL-A-G0001")])
    cap_b = lf.capture(tmp_path / "caps_b", text="second capture")
    mini_b = lf.write_export(tmp_path / "B", games=[lf.game_row(r, cap_b, collected_by="LOCAL-B-G0001") for r in season.iloc[20:48].itertuples()])
    ri.ingest(mini_a, store)
    ri.ingest(mini_b, store)
    assert ri.ingest(mini_a, store)["observations"] == 0  # re-running an import never duplicates
    st = ri.load_store(store)
    assert len(ri.effective_results(st)) == 48  # 76 game observations -> 48 training games

    # Forecast T1 from store history known by its horizon (the game-log scheduled start).
    horizon = _request(t1)["scheduled_start"]
    history = ri.history_rows(st, lf.COMPETITION, lf.ENDPOINT, horizon, exclude_event=t1.native_event_id)
    uid1 = st.events[st.events.native_event_id == t1.native_event_id].event_uid.iloc[0]
    feats = F.build(st, lf.COMPETITION, lf.ENDPOINT, t1.home, t1.away, horizon, target_event_uid=uid1)
    F.write_snapshot(store / "FEATURE_SNAPSHOTS.csv", F.snapshot_rows("FC-T1", uid1, feats, st))
    with pytest.raises(p.AdmissionError):
        F.write_snapshot(store / "FEATURE_SNAPSHOTS.csv", F.snapshot_rows("FC-T1", uid1, feats, st))
    rec1 = p.forecast(_request(t1), LG, history, _contracts(), tmp_path / "bundles" / "T1")
    assert rec1["warm_start_games"] > 0 and rec1["feedback_events"] == 0

    # Unsupported contract families never receive an invented probability.
    bad = _contracts() + [dict(_contracts()[0], contract_key="PTS-P1", family="player_points", side="OVER", line="20.5")]
    with pytest.raises(p.AdmissionError):
        p.forecast(_request(t1, "EXAMPLE_BAD"), LG, history, bad, tmp_path / "bundles" / "T1-bad")
    assert not (tmp_path / "bundles" / "T1-bad").exists()

    # T1's own day and later games (first available after the horizon) arrive later: the T1 view is unchanged.
    assert (season.event_at.iloc[47].normalize() < t1.event_at.normalize() == season.event_at.iloc[48].normalize())
    later = [lf.game_row(r, cap, collected_by="LOCAL-A-G0002") for r in season.iloc[48:56].itertuples()]
    ri.ingest(lf.write_export(tmp_path / "A2", games=later), store)
    st = ri.load_store(store)
    assert ri.history_rows(st, lf.COMPETITION, lf.ENDPOINT, horizon, exclude_event=t1.native_event_id) == history
    assert _same(F.build(st, lf.COMPETITION, lf.ENDPOINT, t1.home, t1.away, horizon, target_event_uid=uid1), feats)

    # Settle T1 from the store's reviewed result: one genuine feedback contribution.
    final = ri.effective_results(st).set_index("event_uid").loc[uid1]
    obs = st.source_observations[(st.source_observations.event_uid == uid1) & (st.source_observations.kind == "RESULT")].iloc[0]
    fb = p.settle(tmp_path / "bundles" / "T1", int(final.hs), int(final.as_), final.final_at, obs.known_at,
                  obs.capture_path, obs.capture_sha256)
    (tmp_path / "FEEDBACK.csv").write_bytes(p.csv_bytes([fb]))

    # T2 consumes that feedback; the research-only game (no bundle) never becomes expert feedback.
    st = ri.load_store(store)
    h2 = ri.history_rows(st, lf.COMPETITION, lf.ENDPOINT, _request(t2)["scheduled_start"], exclude_event=t2.native_event_id)
    rec2 = p.forecast(_request(t2), LG, h2, _contracts(), tmp_path / "bundles" / "T2", feedback=[fb])
    assert rec2["feedback_events"] == 1
    assert research_only.native_event_id in {r["event_id"] for r in h2}

    # A reviewed correction published after T2's issue revises the label without changing T2's view.
    g0 = season.iloc[30]
    when = (pd.Timestamp(t2.event_at) + pd.Timedelta(days=1)).isoformat()
    fix = lf.game_row(g0, cap, hs=str(int(g0.hs) + 1), reg_hs=str(int(g0.reg_hs) + 1), source_kind="WEB_CORRECTED",
                      source_url="https://example.org/correction", known_at=when, published_at=when,
                      retrieved_at=(pd.Timestamp(when) + pd.Timedelta(hours=1)).isoformat())
    assert ri.ingest(lf.write_export(tmp_path / "C", games=[fix]), store)["corrections"] == 1
    st = ri.load_store(store)
    assert ri.history_rows(st, lf.COMPETITION, lf.ENDPOINT, _request(t2)["scheduled_start"], exclude_event=t2.native_event_id) == h2

    # The research-only settlement is a reviewed training candidate linked into an immutable release.
    card, settle_md = tmp_path / "card.md", tmp_path / "settle.md"
    card.write_text("# P-900010 EXAMPLE research-only card\n", encoding="utf-8")
    settle_md.write_text("# P-900010 EXAMPLE settlement\n", encoding="utf-8")
    ro = ri.effective_results(st).set_index("event_uid").loc[
        st.events[st.events.native_event_id == research_only.native_event_id].event_uid.iloc[0]]
    labels = tmp_path / "LABELS.csv"
    labels.write_bytes(p.csv_bytes([dict(zip(rl.LABEL_FIELDS, [
        research_only.native_event_id, lf.COMPETITION, lf.ENDPOINT, "HOME_POINTS", ro.hs, "POINTS",
        pd.Timestamp(research_only.event_at).isoformat(), ro.final_at, ro.valid_from.isoformat(),
        "https://example.org/box", cap[0], cap[1], "FROZEN_FRAMEWORK_CONVENTION", "TERMINAL_LABEL_REVIEWED",
        "revision-1", "POINT_IN_TIME_VERIFIED"]))]))
    rl.retain_candidate("P-900010", card, settle_md, labels, tmp_path / "candidates" / "P-900010" / "revision-1")
    man = ta.build_release(store, lf.COMPETITION, lf.ENDPOINT, tmp_path / "releases", "EX-R1",
                           candidates_root=tmp_path / "candidates")
    rows = {r["native_event_id"]: r for r in p.read_rows(tmp_path / "releases" / "EX-R1" / "ROWS.csv")}
    assert rows[research_only.native_event_id]["candidate_card_id"] == "P-900010"
    assert len(rows) == man["rows"] and len(set(rows)) == len(rows)  # no duplicate training events
    assert rows[g0.native_event_id]["hs"] == str(int(g0.hs) + 1)  # the release uses the effective (corrected) label

    # Learning counters keep the separate meanings apart.
    res = LS.status(ri.load_store(store), releases_root=tmp_path / "releases", bundles_root=tmp_path / "bundles",
                    feedback=[tmp_path / "FEEDBACK.csv"])
    s = res["status"].set_index(["scope_level", "scope"]).loc[("ALL", "ALL")]
    assert s.unique_settled_games == 56 and s.ml_admissible_games == man["rows"]
    assert s.frozen_model_forecasts == 2 and s.hedge_feedback_games == 1

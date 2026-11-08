"""CR-2026.11.08-R2 integrity repairs, each proven by a rejection test (review of 2026-11-08, items 2, 3, 5 and 10).

Synthetic EXAMPLE data only; no live store, ledger or record is touched."""
import math

import numpy as np
import pandas as pd
import pytest

from ml import primary as p, research_ingest as ri
from ml.evaluation import effective_settlement as es
from ml.tests import learning_fixtures as lf


@pytest.fixture
def season():
    return lf.season_frame(n_teams=6)


# ------------------------------------------------------------------ item 2: publication order and correction chronology
def test_a_result_known_before_its_publication_is_quarantined(tmp_path, season):
    store, cap = tmp_path / "s", lf.capture(tmp_path)
    g = season.iloc[0]
    final = pd.Timestamp(g.event_at) + pd.Timedelta(hours=3)
    row = lf.game_row(g, cap, final_at=final.isoformat(), known_at=(final + pd.Timedelta(hours=1)).isoformat(),
                      published_at=(final + pd.Timedelta(days=1)).isoformat(), retrieved_at=(final + pd.Timedelta(days=2)).isoformat())
    receipt = ri.ingest(lf.write_export(tmp_path / "x", games=[row]), store)
    st = ri.load_store(store)
    assert receipt["quarantined"] == 1 and st.results.empty
    assert st.quarantine.reason.str.contains("KNOWN_BEFORE_PUBLICATION").any()
    # Nothing becomes visible in a historical view dated before publication.
    assert ri.effective_results(st, as_of=final + pd.Timedelta(hours=2)).empty


def test_a_statistic_correction_known_before_the_revision_it_replaces_is_refused(tmp_path, season):
    store, cap = tmp_path / "s", lf.capture(tmp_path)
    g = season.iloc[0]
    lf.ingest_frame(tmp_path, store, season.iloc[:1], "game", cap=cap)
    t0 = pd.Timestamp(g.event_at) + pd.Timedelta(days=1)
    stat = dict(competition=lf.COMPETITION, native_event_id=g.native_event_id, team=g.home, stat="FGA", value="80",
                source_url="https://example.org/box", source_kind="WEB_RECOVERED", published_at=t0.isoformat(),
                retrieved_at=t0.isoformat(), known_at=t0.isoformat(), capture_path=cap[0], capture_sha256=cap[1],
                review_status="RESEARCH_INPUT_REVIEWED", collected_by="LOCAL-EX-G0001")
    ri.ingest(lf.write_export(tmp_path / "s1", stats=[stat]), store)
    early = (t0 - pd.Timedelta(hours=12)).isoformat()
    bad = dict(stat, value="81", source_kind="WEB_CORRECTED", published_at=early, retrieved_at=early, known_at=early,
               source_url="https://example.org/box-corrected")
    ri.ingest(lf.write_export(tmp_path / "s2", stats=[bad]), store)
    st = ri.load_store(store)
    assert st.team_game_stats.revision.astype(int).max() == 1
    assert st.quarantine.reason.str.contains("CORRECTION_CHRONOLOGY").any()
    later = (t0 + pd.Timedelta(days=1)).isoformat()
    ri.ingest(lf.write_export(tmp_path / "s3", stats=[dict(bad, published_at=later, retrieved_at=later, known_at=later)]), store)
    assert ri.load_store(store).team_game_stats.revision.astype(int).max() == 2


# ------------------------------------------------------------------ item 10: one writer at a time
def test_a_second_writer_is_refused_while_the_store_is_locked(tmp_path, season):
    store, cap = tmp_path / "s", lf.capture(tmp_path)
    store.mkdir()
    (store / ri.LOCK_NAME).write_text("held by another ingest\n")
    with pytest.raises(p.AdmissionError, match="STORE_LOCKED"):
        lf.ingest_frame(tmp_path, store, season.iloc[:2], "a", cap=cap)
    (store / ri.LOCK_NAME).unlink()
    lf.ingest_frame(tmp_path, store, season.iloc[:2], "b", cap=cap)
    assert not (store / ri.LOCK_NAME).exists()


def test_a_writer_that_appended_meanwhile_stops_the_second_commit(tmp_path, season, monkeypatch):
    store, cap = tmp_path / "s", lf.capture(tmp_path)
    lf.ingest_frame(tmp_path, store, season.iloc[:2], "first", cap=cap)
    real = ri._max_seq
    calls = {"n": 0}

    def racing(root):           # the recheck sees a sequence another writer committed after this ingest started
        calls["n"] += 1
        return real(root) + (5 if calls["n"] >= 1 else 0)
    monkeypatch.setattr(ri, "_max_seq", racing)
    with pytest.raises(p.AdmissionError, match="STORE_CHANGED_DURING_INGEST"):
        lf.ingest_frame(tmp_path, store, season.iloc[2:4], "second", cap=cap)
    monkeypatch.setattr(ri, "_max_seq", real)
    assert len(ri.load_store(store).results) == 2


# ------------------------------------------------------------------ item 3: one effective-settlement view
def _inventory(tmp_path):
    v = tmp_path / es.V / "mini_import_EX"
    v.mkdir(parents=True)
    rows = [dict(canonical_id="P-9001", local_key="LOCAL-EX-G0001", probability_role="ANALYST_PRIMARY_V1 p_card", original_rank="1",
                 original_contract="Over 1.5", original_probability="0.6", sporting_grade="UNRESOLVED", effective_revision="revision-1",
                 evidence_class="X", note="")]
    pd.DataFrame(rows).to_csv(v / "EFFECTIVE_SETTLEMENT_ROWS.csv", index=False)
    (tmp_path / "doc.md").write_text("revision document")


def _revision(tmp_path, folder="settlement_import_EX", **kw):
    d = tmp_path / es.V / folder
    d.mkdir(parents=True, exist_ok=True)
    row = dict(canonical_id="P-9001", local_key="LOCAL-EX-G0001", original_rank="1", original_contract="Over 1.5", revision="revision-2",
               parent_revision="revision-1", sporting_grade="WIN", evidence_class="B", effective_at="2026-11-08T00:00:00+11:00",
               source_document="doc.md", note="")
    row.update(kw)
    path = d / "SETTLEMENT_REVISIONS.csv"
    old = pd.read_csv(path, dtype=str, keep_default_na=False) if path.exists() else pd.DataFrame(columns=es.REVISION_FIELDS)
    pd.concat([old, pd.DataFrame([row])])[list(es.REVISION_FIELDS)].to_csv(path, index=False)


def test_the_effective_view_applies_a_valid_revision_chain(tmp_path):
    _inventory(tmp_path)
    _revision(tmp_path)
    _revision(tmp_path, revision="revision-3", parent_revision="revision-2", sporting_grade="LOSS")
    row = es.effective_rows(tmp_path).iloc[0]
    assert row["sporting_grade"] == "LOSS" and row["effective_revision"] == "revision-3"
    assert row["revision_chain"] == "revision-1 > revision-2 > revision-3"


@pytest.mark.parametrize("change,needle", [
    (dict(parent_revision="revision-2", revision="revision-3"), "broken chain"),
    (dict(original_contract="Under 1.5"), "unknown contract"),
    (dict(local_key="LOCAL-EX-G0009"), "names local key"),
    (dict(sporting_grade="MAYBE"), "not in"),
    (dict(source_document="missing.md"), "does not exist"),
    (dict(revision="revision-4"), "must directly follow"),
])
def test_a_stale_forked_or_unknown_revision_is_refused(tmp_path, change, needle):
    _inventory(tmp_path)
    _revision(tmp_path, **change)
    with pytest.raises(es.RevisionError, match=needle):
        es.effective_rows(tmp_path)


def test_a_repeated_revision_is_refused(tmp_path):
    _inventory(tmp_path)
    _revision(tmp_path)
    _revision(tmp_path, folder="settlement_import_EX2")
    with pytest.raises(es.RevisionError, match="appears twice"):
        es.effective_rows(tmp_path)


def test_the_live_view_settles_p604_corners_and_carries_the_latest_revisions():
    """Review 2026-11-08 item 3: the history rebuild still showed P-604's corners UNRESOLVED."""
    frame = es.effective_rows()
    rows = {(r.canonical_id, r.original_contract): r for r in frame.itertuples()}
    assert rows[("P-604", "Corners Over 10.5")].sporting_grade == "WIN"
    assert rows[("P-604", "Corners Under 10.5")].sporting_grade == "LOSS"
    assert rows[("P-616", "Under 221.5")].effective_revision == "revision-2"
    assert rows[("P-620", "SA 1st inns Under 282.5")].evidence_class == "B"
    assert es.unmatched_revisions() == []


# ------------------------------------------------------------------ item 9: generated current state
def test_the_committed_state_block_is_what_the_records_generate():
    from ml import state
    assert state.committed_block() == state.generate(), "run `python -m ml state --write` and commit CURRENT_STATE.md"

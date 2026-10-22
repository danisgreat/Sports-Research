"""REV-22: the release data-quality gate reads only the learning store. Synthetic EXAMPLE competition."""
import csv
import io
from pathlib import Path

import pytest

from ml import releasegate as G

COMP = "Basketball/EXAMPLE-GATE"


def write(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    path.write_bytes(out.getvalue().encode())


def store(tmp_path, n=40, seasons=("2024", "2025"), domains=("https://a.example/x", "https://b.example/y"), decision="Regulation",
          reg="90", quarantine=0):
    events, results, obs = [], [], []
    for i in range(n):
        uid = f"E{i}"
        events.append(dict(event_uid=uid, competition=COMP, endpoint="E", native_event_id=str(i), identity_basis="N", season=seasons[i % len(seasons)],
                           event_at="2025-01-01T00:00:00+00:00", home="a", away="b", venue="", ingest_seq="1"))
        results.append(dict(event_uid=uid, revision="1", status="FINAL", hs=str(90 + i % 17), as_=str(88 + i % 11), reg_hs=reg, reg_as=reg,
                            decision=decision if i % 12 == 0 else "Regulation", final_at="x", revision_basis="FIRST_OBSERVED", ingest_seq="1"))
        for d in domains:
            obs.append(dict(observation_id=f"{uid}{d}", kind="RESULT", event_uid=uid, link="1", disposition="NEW", source_url=d, source_kind="WEB_RECOVERED",
                            published_at="", retrieved_at="", known_at="", capture_path="", capture_sha256="", collected_by="", ingest_seq="1"))
    base = tmp_path / G.STORE
    write(base / "EVENTS.csv", events, list(events[0]))
    write(base / "RESULTS.csv", results, list(results[0]))
    write(base / "SOURCE_OBSERVATIONS.csv", obs, list(obs[0]))
    write(base / "QUARANTINE.csv", [dict(ingest_seq="2", kind="RESULT", observation_id="q", competition=COMP, native_event_id="1", reason="r", source_url="u", row_digest="d")
                                    for _ in range(quarantine)] or [dict(ingest_seq="", kind="", observation_id="", competition="OTHER", native_event_id="", reason="", source_url="", row_digest="")],
          ["ingest_seq", "kind", "observation_id", "competition", "native_event_id", "reason", "source_url", "row_digest"])
    return tmp_path


def codes(result):
    return {c["check"]: c["status"] for c in result["checks"]}


def test_a_clean_store_passes_every_check(tmp_path):
    result = G.gate(COMP, store(tmp_path), min_events=30)
    assert result["passed"] and set(codes(result).values()) == {"PASS"} and result["finals"] == 40


def test_too_few_events_or_one_season_fails_g1(tmp_path):
    assert codes(G.gate(COMP, store(tmp_path), min_events=300))["G1"] == "FAIL"
    assert codes(G.gate(COMP, store(tmp_path / "one", seasons=("2025",)), min_events=30))["G1"] == "FAIL"


def test_quarantine_and_single_domain_support_fail(tmp_path):
    assert codes(G.gate(COMP, store(tmp_path / "q", quarantine=2), min_events=30))["G3"] == "FAIL"
    assert codes(G.gate(COMP, store(tmp_path / "d", domains=("https://a.example/x", "https://a.example/y")), min_events=30))["G4"] == "FAIL"


def test_extra_time_without_observed_regulation_fails_g5(tmp_path):
    result = G.gate(COMP, store(tmp_path, decision="Overtime", reg="NOT_OBSERVED"), min_events=30)
    assert codes(result)["G5"] == "FAIL" and not result["passed"]


def test_an_always_regulation_overtime_field_is_flagged_by_g2(tmp_path):
    big = store(tmp_path, n=600, seasons=("2020", "2021", "2022", "2023", "2024"), decision="Regulation")
    result = G.gate(COMP, big, min_events=300)
    assert codes(result)["G2"] == "FAIL" and "OVERTIME_FIELD_IMPLAUSIBLE" in next(c["detail"] for c in result["checks"] if c["check"] == "G2")

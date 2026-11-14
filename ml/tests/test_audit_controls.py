"""Adversarial AUDIT-v1 admission and final-mini custody checks (synthetic data only)."""
import csv
from pathlib import Path

import pytest

from ml import audit_controls as A, external as X, picks as P, ledger as L
from ml.tests.test_picks_ledger import KEY, META, good_rows, render, mini, root  # noqa: F401


@pytest.fixture
def review(root):
    note = root / "method.md"
    note.write_text("EXAMPLE exact competition, supported reference scope; n=100 sporting observations; uncertainty retained.")
    meta = dict(META, issued_at="2026-11-15T09:30:00+00:00", scheduled_start="2026-11-15T10:00:00+00:00",
                rank_scope="SUPPLIED_ONLY", audit_policy=A.VERSION, audit_review="review.csv")
    rows = []
    for pick in good_rows():
        r = dict.fromkeys(A.FIELDS, "")
        r.update(label=pick["label"], sport="Basketball", competition=META["competition"], event_date="2026-11-15",
                 native_event_id="EXAMPLE-1", home="EXAMPLE Home", away="EXAMPLE Away", scheduled_start=meta["scheduled_start"],
                 schedule_url="https://example.org/schedule/EXAMPLE-1", schedule_checked_at="2026-11-15T09:00:00+00:00",
                 method_id="EXAMPLE supported reference", method_status="SUPPORTED_REFERENCE", method_evidence="method.md",
                 method_evidence_sha256=A.digest(note.read_bytes()), sample_n="100", sample_coverage="0.8",
                 uncertainty="Incomplete season coverage; scope and sampling uncertainty disclosed, no calibrated skill claimed.",
                 opponent_check="NOT_APPLICABLE", opponent_evidence="EXAMPLE no plus handicap supplied",
                 availability_status="NO_MATERIAL_CHANGE_IDENTIFIED", availability_evidence="method.md", availability_evidence_sha256=A.digest(note.read_bytes()),
                 reason="EXAMPLE supported reference; no empirical effect invented")
        rows.append(r)
    meta["audit_event_key"] = X.event_key("Basketball", "2026-11-15", "EXAMPLE Home", "EXAMPLE Away",
                                           competition=META["competition"], native_event_id="EXAMPLE-1")
    return root, meta, rows


def bind(review):
    root, meta, rows = review
    raw = A.csv_bytes(A.FIELDS, rows)
    (root / "review.csv").write_bytes(raw)
    meta["audit_review_sha256"] = A.digest(raw)
    return root, meta, rows


def test_new_unsupported_card_is_refused_but_original_historical_card_stays_valid(root):
    assert P.lint(META, good_rows(), root) == []
    meta = dict(META, issued_at="2026-11-15T09:30:00+00:00", scheduled_start="2026-11-15T10:00:00+00:00", rank_scope="SUPPLIED_ONLY")
    assert any("require audit_policy" in e for e in P.lint(meta, good_rows(), root))


def test_supported_review_passes_normal_picks_admission(review):
    root, meta, _ = bind(review)
    assert P.lint(meta, good_rows(), root) == []


@pytest.mark.parametrize("field,value,needle", [
    ("event_date", "2026-11-16", "event_date"),
    ("native_event_id", "NEXT-DAY-REMATCH", "identity"),
    ("method_id", "retired v4.12", "legacy"),
    ("method_status", "UNCALIBRATED", "uncalibrated"),
    ("method_evidence", "missing.md", "missing method"),
    ("sample_n", "0", "sample_n"),
    ("sample_coverage", "nan", "sample_coverage"),
    ("sample_coverage", "1.2", "sample_coverage"),
    ("uncertainty", "", "missing uncertainty"),
    ("availability_status", "UNQUANTIFIED", "UNPRICED"),
    ("availability_status", "SCENARIO_ONLY", "UNPRICED"),
    ("availability_status", "MEASURED", "p_with"),
    ("schedule_checked_at", "2026-11-15T09:45:00+00:00", "after issue"),
])
def test_bad_review_cannot_admit_primary_probabilities(review, field, value, needle):
    for r in review[2]:
        r[field] = value
    root, meta, _ = bind(review)
    assert any(needle in e for e in P.lint(meta, good_rows(), root))


def test_review_tampering_and_method_evidence_drift_are_refused(review):
    root, meta, _ = bind(review)
    (root / "review.csv").write_bytes((root / "review.csv").read_bytes() + b"\n")
    assert any("SHA-256 mismatch" in e for e in P.lint(meta, good_rows(), root))
    bind(review)
    (root / "method.md").write_text("Changed after review")
    assert any("method/scope evidence" in e for e in P.lint(meta, good_rows(), root))


def test_review_cannot_escape_checkout_or_omit_or_repeat_a_priced_contract(review):
    root, meta, rows = bind(review)
    meta["audit_review"] = "../outside.csv"
    assert any("escapes" in e for e in P.lint(meta, good_rows(), root))
    meta["audit_review"] = "review.csv"
    rows.append(dict(rows[0])); bind(review)
    assert any("one review" in e for e in P.lint(meta, good_rows(), root))
    rows.pop(); rows.pop(); bind(review)
    assert any("one review" in e for e in P.lint(meta, good_rows(), root))


def test_plus_handicap_requires_opponent_strength_and_measured_player_cases_are_numeric(review):
    root, meta, rows = bind(review)
    priced = good_rows()
    priced[0].update(family="HANDICAP", line="5.5")
    assert any("opponent-strength" in e for e in A.problems(meta, priced, root))
    rows[0].update(opponent_check="CHECKED", opponent_evidence="method.md", opponent_evidence_sha256=A.digest((root / "method.md").read_bytes()))
    bind(review)
    assert A.problems(meta, priced, root) == []
    rows[0].update(availability_status="MEASURED", p_with="0.6", p_without="0.5")
    bind(review)
    assert any("availability effect" in e for e in A.problems(meta, priced, root))
    rows[0]["p_with"] = "nan"; bind(review)
    assert any("p_with" in e for e in A.problems(meta, priced, root))


def test_ledger_admission_cannot_skip_audit_gate(root, tmp_path):
    text = render(dict(issued_at="2026-11-15T09:30:00+00:00", scheduled_start="2026-11-15T10:00:00+00:00", rank_scope="SUPPLIED_ONLY"))
    with pytest.raises((P.PicksError, ValueError), match="AUDIT-v1"):
        L.add(mini(tmp_path, text), KEY, root=root)


def test_measured_availability_requires_a_current_scoped_player_effect(review):
    root, meta, rows = bind(review)
    path = root / L.EFFECTS
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); fields = tuple(reader.fieldnames); effects = list(reader)
    effect = dict(effects[0], row_id="E-EX-PLAYER", factor="EXAMPLE player availability", n="100")
    path.write_bytes(A.csv_bytes(fields, effects + [effect]))
    rows[0].update(availability_status="MEASURED", p_with="0.66", p_without="0.62", availability_effect_id="E-EX-PLAYER",
                   availability_effect_version=L.effect_rows(root)["E-EX-PLAYER"]["version"])
    bind(review)
    assert A.problems(meta, good_rows(), root) == []
    rows[0]["availability_effect_version"] = "invented version"; bind(review)
    assert any("version/competition" in e for e in A.problems(meta, good_rows(), root))


def write_final(tmp_path, key="LOCAL-EXAMPLE-G0001"):
    p = tmp_path / "final.md"
    p.write_text(f"<!-- MINI-LOG-FORMAT: mini-log-10 -->\n<!-- BEGIN CARD {key} -->\nEXAMPLE original\n<!-- END CARD {key} -->\n")
    (tmp_path / "scenario.txt").write_text("EXAMPLE associated sensitivity only")
    return p


def test_handover_has_final_original_inventory_and_detects_missing_or_changed_members(tmp_path):
    p = write_final(tmp_path)
    out = tmp_path / "HANDOVER.csv"
    result = A.handover(tmp_path, p.name, "EXAMPLE", "writer-one", ["scenario.txt"], out)
    assert result == A.verify_handover(tmp_path, out) == dict(files=2, cards=1, mini_key="EXAMPLE", publication_proof="NO")
    original = p.read_bytes(); p.write_bytes(original + b"changed")
    with pytest.raises(ValueError, match="changed"):
        A.verify_handover(tmp_path, out)
    p.write_bytes(original); (tmp_path / "scenario.txt").unlink()
    with pytest.raises(OSError):
        A.verify_handover(tmp_path, out)
    assert p.read_bytes() == original


@pytest.mark.parametrize("defect", ["foreign", "canonical", "unmarked", "unfinished", "nested", "duplicate"])
def test_handover_refuses_bad_or_missing_final_card_structure(tmp_path, defect):
    key = "LOCAL-FOREIGN-G0001" if defect == "foreign" else "P-99999" if defect == "canonical" else "LOCAL-EXAMPLE-G0001"
    p = write_final(tmp_path, key)
    text = p.read_text()
    if defect == "unmarked": text = "<!-- MINI-LOG-FORMAT: mini-log-10 -->\nheading only"
    if defect == "unfinished": text = text[:text.index("<!-- END CARD")]
    if defect == "nested": text = text.replace("EXAMPLE original", "<!-- BEGIN CARD LOCAL-EXAMPLE-G0002 -->")
    if defect == "duplicate": text += text[text.index("<!-- BEGIN CARD"):]
    p.write_text(text)
    out = tmp_path / "HANDOVER.csv"
    with pytest.raises(ValueError):
        A.handover(tmp_path, p.name, "EXAMPLE", "writer-one", [], out)
    assert not out.exists()


def test_handover_refuses_path_escape_and_overwrite(tmp_path):
    p = write_final(tmp_path)
    out = tmp_path / "HANDOVER.csv"
    with pytest.raises(ValueError, match="escapes"):
        A.handover(tmp_path, p.name, "EXAMPLE", "writer", ["../missing.txt"], out)
    A.handover(tmp_path, p.name, "EXAMPLE", "writer", [], out)
    original = out.read_bytes()
    with pytest.raises(FileExistsError):
        A.handover(tmp_path, p.name, "EXAMPLE", "writer", [], out)
    assert out.read_bytes() == original

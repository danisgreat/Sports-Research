"""Local-key research minis retain custody without preallocating canonical IDs."""
import pytest

from ml import primary as p
from ml.execution import MANIFEST_FIELDS, execute_files, verify_log
from ml.tests.test_execution import files, manifest
from ml.tests.test_primary import inputs


def local_card(key, event):
    return (f"<!-- BEGIN CARD {key} -->\n"
            "- **Analysis status:** RESEARCH_ONLY_NO_MODEL\n"
            f"- **ML execution identity:** {event} | Ice Hockey/EXAMPLE | FULL_GAME\n"
            f"<!-- END CARD {key} -->\n")


def local_row(key, event):
    row = dict.fromkeys(MANIFEST_FIELDS, "")
    row.update(card_id=key, event_id=event, competition="Ice Hockey/EXAMPLE", endpoint="FULL_GAME",
               feedback_status="NOT_APPLICABLE_NO_MODEL", reason="NOT_IMPLEMENTED: EXAMPLE synthetic scope")
    return row


def write_mini(tmp_path, body="", rows=(), fmt="mini-log-10"):
    mini, csv = tmp_path / "mini.md", tmp_path / "manifest.csv"
    mini.write_text(f"<!-- MINI-LOG-FORMAT: {fmt} -->\n" + body, encoding="utf-8")
    csv.write_bytes(p.csv_bytes(list(rows)) if rows else (",".join(MANIFEST_FIELDS) + "\n").encode())
    return csv, mini


def test_two_successive_local_cards_preserve_first_without_canonical_allocation(tmp_path):
    first, second = "LOCAL-EXAMPLEA-G0001", "LOCAL-EXAMPLEA-G0002"
    body = local_card(first, "EXAMPLE-EVENT-1")
    paths = write_mini(tmp_path, body, [local_row(first, "EXAMPLE-EVENT-1")])
    assert verify_log(*paths)["research_only"] == 1
    paths = write_mini(tmp_path, body + local_card(second, "EXAMPLE-EVENT-2"),
                       [local_row(first, "EXAMPLE-EVENT-1"), local_row(second, "EXAMPLE-EVENT-2")])
    before = [path.read_bytes() for path in paths]
    assert verify_log(*paths)["cards"] == 2
    assert paths[1].read_text(encoding="utf-8").endswith(body + local_card(second, "EXAMPLE-EVENT-2"))
    assert [path.read_bytes() for path in paths] == before
    assert "P-" not in paths[1].read_text(encoding="utf-8")


def test_supported_fitted_primary_card_uses_local_manifest_key(inputs):
    rec = execute_files(**files(inputs))
    paths = manifest(inputs, rec)
    for path in paths:
        text = path.read_text(encoding="utf-8").replace("P-900001", "LOCAL-EXAMPLEA-G0001")
        path.write_text(text.replace("mini-log-8", "mini-log-10"), encoding="utf-8")
    assert verify_log(*paths) == dict(cards=1, executed=1, failed=0, feedback_retained=0, research_only=0)


@pytest.mark.parametrize("fmt", ["mini-log-8", "mini-log-9"])
def test_legacy_p_card_and_new_local_addition_remain_valid(tmp_path, fmt):
    keys = ["P-900099", "LOCAL-EXAMPLEA-G0001"]
    paths = write_mini(tmp_path, "".join(local_card(k, "EXAMPLE-" + str(i)) for i, k in enumerate(keys)),
                       [local_row(k, "EXAMPLE-" + str(i)) for i, k in enumerate(keys)], fmt)
    assert verify_log(*paths)["cards"] == 2


def test_empty_local_mini_has_no_allocation(tmp_path):
    assert verify_log(*write_mini(tmp_path))["cards"] == 0


@pytest.mark.parametrize("key", ["P-900099", "LOCAL-example-G0001", "LOCAL-EXAMPLE-G0000",
                                  "LOCAL-EXAMPLE-G1", "LOCAL-EXAMPLE-G０００１", "UNKNOWN", "LOCAL-P-900099-G0001"])
def test_new_format_rejects_canonical_or_malformed_card_identity(tmp_path, key):
    paths = write_mini(tmp_path, local_card(key, "EXAMPLE-EVENT"), [local_row(key, "EXAMPLE-EVENT")])
    with pytest.raises(p.AdmissionError, match="stable local key"):
        verify_log(*paths)


@pytest.mark.parametrize("defect", ["missing_end", "orphan", "wrong_end", "nested", "duplicate",
                                    "malformed", "missing_manifest", "extra_format", "unknown_format"])
def test_local_markers_and_manifest_fail_closed(tmp_path, defect):
    key, other = "LOCAL-EXAMPLEA-G0001", "LOCAL-EXAMPLEA-G0002"
    body = local_card(key, "EXAMPLE-EVENT")
    rows = [local_row(key, "EXAMPLE-EVENT")]
    if defect == "missing_end": body = body.replace(f"<!-- END CARD {key} -->", "")
    if defect == "orphan": body = f"<!-- END CARD {key} -->\n" + body
    if defect == "wrong_end": body = body.replace(f"END CARD {key}", f"END CARD {other}")
    if defect == "nested": body = body.replace(f"<!-- END CARD {key} -->", local_card(other, "EXAMPLE-2") + f"<!-- END CARD {key} -->")
    if defect == "duplicate": body += body
    if defect == "malformed": body = f"<!-- BEGIN CARD {key}-->\n"
    if defect == "missing_manifest": rows = []
    if defect == "extra_format": body += "<!-- MINI-LOG-FORMAT: mini-log-9 -->\n"
    paths = write_mini(tmp_path, body, rows, "mini-log-99" if defect == "unknown_format" else "mini-log-10")
    with pytest.raises(p.AdmissionError): verify_log(*paths)


def test_local_card_cannot_claim_model_result_without_execution(tmp_path):
    key = "LOCAL-EXAMPLEA-G0001"
    paths = write_mini(tmp_path, local_card(key, "EXAMPLE-EVENT").replace("RESEARCH_ONLY_NO_MODEL", "MODEL_ASSISTED_PRIMARY_V3"),
                       [local_row(key, "EXAMPLE-EVENT")])
    with pytest.raises(p.AdmissionError, match="numeric primary"):
        verify_log(*paths)

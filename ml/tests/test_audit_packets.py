"""Packets contain dated reader rules before access; new events pin their control policy."""
import pytest
from ml import research_operations as O, research_intake as I, external as X
from ml.tests.test_external_integrity_v2 import event  # noqa: F401


def test_packet_contains_actual_permission_rows_and_one_role_instructions(event):
    text = O.packet(event["folder"], "L1", root=event["root"], at="2026-11-10T23:56:00+00:00")
    assert "club.example.org,ALLOWED" in text
    assert "BLOCKED and RULES_UNKNOWN are refusals" in text
    assert "L1-L4 and L6 return evidence" in text
    assert "Simulation count is not sample size" in text


def test_expired_reader_decisions_do_not_release_a_packet(event):
    before = (event["folder"] / "PACKET_RELEASES.csv")
    with pytest.raises(X.ExternalError, match="expired"):
        O.packet(event["folder"], "L1", root=event["root"], at="2026-11-19T00:00:00+00:00")
    assert not before.exists()


def test_new_event_cannot_pin_an_old_release_that_lacks_the_audit_protocol(event):
    spec = I.load(event["folder"], event["root"])
    artifacts = {r["role"]: r["path"] for r in I.read(event["folder"] / "ARTIFACTS.csv", I.ART_FIELDS)}
    with pytest.raises(X.ExternalError, match="audit_controls artifact"):
        I.initialize(spec, I.read(event["folder"] / "CONTRACTS.csv", I.CONTRACT_FIELDS),
                     I.read(event["folder"] / "REQUIREMENTS.csv", I.REQ_FIELDS), event["root"] / "new-event",
                     artifacts=artifacts, root=event["root"], at="2026-11-15T01:00:00+00:00")

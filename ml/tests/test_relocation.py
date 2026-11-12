"""RELOC-v1 (CR-2026.11.12-R1): cited paths follow hash-checked relocations; a changed moved file is refused."""
import hashlib

import pytest

from ml import relocation
from ml.evaluation import effective_settlement as es


def _setup(tmp_path, body=b"settlement revision\n"):
    new = tmp_path / "archive" / "moved" / "research" / "active_minis" / "X_SETTLEMENT.md"
    new.parent.mkdir(parents=True)
    new.write_bytes(body)
    (tmp_path / "archive" / "moved" / "RELOCATIONS.csv").write_text(
        "old_path,new_path,sha256\n"
        f"research/active_minis/X_SETTLEMENT.md,archive/moved/research/active_minis/X_SETTLEMENT.md,{hashlib.sha256(body).hexdigest()}\n",
        encoding="utf-8")
    relocation.table.cache_clear()
    return new


def test_relocated_file_resolves_by_hash(tmp_path):
    new = _setup(tmp_path)
    assert relocation.resolve(tmp_path, "research/active_minis/X_SETTLEMENT.md") == new
    assert relocation.resolve(tmp_path, "research/active_minis/OTHER.md") is None


def test_changed_relocated_file_is_refused(tmp_path):
    new = _setup(tmp_path)
    new.write_bytes(b"edited after the move\n")
    with pytest.raises(relocation.RelocationError):
        relocation.resolve(tmp_path, "research/active_minis/X_SETTLEMENT.md")


def test_repository_settlement_view_reads_relocated_revision_documents():
    relocation.table.cache_clear()
    rows = es.effective_rows()
    assert (rows["sporting_grade"] == "UNRESOLVED").sum() == 0
    assert (rows["revision_source"] != "").sum() >= 16

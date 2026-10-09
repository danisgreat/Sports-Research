"""Hashed raw snapshots and the data-source register's agreement with the filesystem (SRC-06)."""
import json
import re
from pathlib import Path

import pytest

from runtime.src.common import snapshots

ROOT = Path(__file__).resolve().parents[2]


def test_snapshot_layout_hash_and_immutability(tmp_path):
    receipt = snapshots.write_snapshot("afl", "fitzroy", b"parquet-bytes", "fetch_results_afl", "2026.10", "2026-10-09T03:04:05+00:00", tmp_path)
    assert receipt["path"].startswith("raw/afl/fitzroy/2026-10-09/") and receipt["bytes"] == 13 and len(receipt["sha256"]) == 64
    body = tmp_path / receipt["path"]
    assert body.read_bytes() == b"parquet-bytes"
    json_path = body.with_suffix(".json")
    assert snapshots.verify(json_path)["endpoint"] == "fetch_results_afl"
    body.write_bytes(b"tampered")
    with pytest.raises(snapshots.SnapshotError, match="no longer matches"):
        snapshots.verify(json_path)
    with pytest.raises(snapshots.SnapshotError, match="already exists"):
        snapshots.write_snapshot("afl", "fitzroy", b"parquet-bytes", "fetch_results_afl", "2026.10", "2026-10-09T03:04:05+00:00", tmp_path)
    assert snapshots.list_snapshots("afl", root=tmp_path) == [json_path]


def test_inputs_are_validated(tmp_path):
    with pytest.raises(snapshots.SnapshotError):
        snapshots.write_snapshot("afl", "fitz roy", b"x", "e", root=tmp_path)
    with pytest.raises(snapshots.SnapshotError):
        snapshots.write_snapshot("../afl", "p", b"x", "e", root=tmp_path)
    with pytest.raises(snapshots.SnapshotError, match="empty"):
        snapshots.write_snapshot("afl", "p", b"", "e", root=tmp_path)
    with pytest.raises(snapshots.SnapshotError, match="UTC offset"):
        snapshots.write_snapshot("afl", "p", b"x", "e", retrieved_utc="2026-10-09T00:00:00", root=tmp_path)


def test_cli_registers_and_verifies(tmp_path, capsys):
    export = tmp_path / "afl_matches.parquet"
    export.write_bytes(b"PAR1....PAR1")
    assert snapshots.main(["register", str(export), "--sport", "afl", "--provider", "fitzroy", "--endpoint", "fetch_results_afl", "--root", str(tmp_path / "data")]) == 0
    assert json.loads(capsys.readouterr().out)["sha256"]
    assert snapshots.main(["verify", "--root", str(tmp_path / "data")]) == 0


def test_register_mentions_only_paths_that_exist_or_are_created_at_run_time():
    text = (ROOT / "DATA_SOURCE_REGISTER.md").read_text(encoding="utf-8")
    created_at_run_time = ("runtime/data/",)
    for path in sorted(set(re.findall(r"`((?:runtime|research)/[A-Za-z0-9_./<>\-]+)`", text))):
        if path.startswith(created_at_run_time):
            continue
        assert (ROOT / path).exists(), f"DATA_SOURCE_REGISTER.md names {path}, which does not exist"
    for script in ("runtime/r_ingestion/afl_fitzroy.R", "runtime/r_ingestion/nrl_nrlr.R"):
        assert script in text and (ROOT / script).exists()
    assert "runtime/src/common/snapshots.py" in text


def test_r_bridges_write_to_the_documented_canonical_directory():
    for name, sport in (("afl_fitzroy.R", "afl"), ("nrl_nrlr.R", "nrl")):
        script = (ROOT / "runtime/r_ingestion" / name).read_text(encoding="utf-8")
        assert f'"runtime/data/canonical/{sport}"' in script and "snapshots register" in script

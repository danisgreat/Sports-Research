"""One authoritative effective-settlement view from validated revision chains (SETTLE-VIEW-v1, CR-2026.11.08-R2).

Original grades come from each canonical import's ``mini_import_*/EFFECTIVE_SETTLEMENT_ROWS.csv`` (kept unchanged).
Later revisions come from each settlement import's ``settlement_import_*/SETTLEMENT_REVISIONS.csv``. A row's key is
(canonical_id, original_rank, original_contract). A revision applies only when its ``parent_revision`` is the key's
current effective revision; a revision for an unknown key, a repeated revision id, a broken or branching chain, or a
revision document that does not exist is refused, so no report can silently consume a stale or forked grade.

    python -m ml settlement-view --out NEW_FOLDER      writes EFFECTIVE_SETTLEMENTS.csv with the applied revision chain

Reports, scoreboards and learning admission read ``effective_rows()``; the original inventories are never edited.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
from pathlib import Path

import pandas as pd

from ml import relocation

ROOT = Path(__file__).resolve().parents[2]
V = "research/verification"
REVISION_FIELDS = ("canonical_id", "local_key", "original_rank", "original_contract", "revision", "parent_revision",
                   "sporting_grade", "evidence_class", "effective_at", "source_document", "note")
GRADES = ("WIN", "LOSS", "PUSH", "VOID", "UNRESOLVED", "UNATTAINABLE")
KEY = ("canonical_id", "original_rank", "original_contract")


class RevisionError(ValueError):
    pass


def normalize_inventory(frame: pd.DataFrame) -> pd.DataFrame:
    """Admit the preserved legacy event/key layout without rewriting its source file."""
    if "canonical_id" in frame.columns:
        return frame.copy()
    if not {"event_id", "key", "revision_id", "original_contract", "original_rank_type", "sporting_grade"} <= set(frame.columns):
        return frame.copy()
    out = frame.copy()
    versions = out.revision_id.str.extract(r"-R(\d+)-", expand=False)
    if versions.isna().any() or out.key.duplicated().any():
        raise RevisionError("LEGACY_REVISION_ID: unique source keys and explicit -R<n>- versions required")
    out["canonical_id"] = out.event_id
    out["local_key"] = out.key
    out["original_rank"] = out.original_rank_type
    out["effective_revision"] = "revision-" + versions
    out["evidence_class"] = out.get("source_evidence_class", "X")
    return out


def _number(revision: str) -> int:
    if not revision.startswith("revision-") or not revision[9:].isdigit():
        raise RevisionError(f"revision id must be revision-<n>, got {revision!r}")
    return int(revision[9:])


def original_inventories(root=ROOT) -> list[Path]:
    return sorted(p for p in (Path(root) / V).glob("mini_import_*/EFFECTIVE_SETTLEMENT_ROWS.csv"))


def revision_files(root=ROOT) -> list[Path]:
    return sorted(p for p in (Path(root) / V).glob("settlement_import_*/SETTLEMENT_REVISIONS.csv"))


def read_revisions(path: Path, root=ROOT) -> pd.DataFrame:
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    if tuple(frame.columns) != REVISION_FIELDS:
        raise RevisionError(f"{path}: columns must be exactly {','.join(REVISION_FIELDS)}")
    for i, r in enumerate(frame.to_dict("records"), 2):
        if r["sporting_grade"] not in GRADES:
            raise RevisionError(f"{path}:{i}: grade {r['sporting_grade']!r} not in {GRADES}")
        if _number(r["revision"]) != _number(r["parent_revision"]) + 1:
            raise RevisionError(f"{path}:{i}: {r['revision']} must directly follow its parent {r['parent_revision']}")
        if relocation.resolve(root, r["source_document"]) is None:
            raise RevisionError(f"{path}:{i}: source document {r['source_document']} does not exist")
        if not r["effective_at"]:
            raise RevisionError(f"{path}:{i}: effective_at is required")
    frame["revision_file"] = str(Path(path).relative_to(root).as_posix()) if Path(path).is_relative_to(root) else str(path)
    return frame


def apply_revisions(original: pd.DataFrame, revisions: pd.DataFrame) -> pd.DataFrame:
    """Original rows with every validated revision applied in chain order; adds revision_chain and revision_source."""
    out = original.copy()
    out["revision_chain"] = out["effective_revision"]
    out["revision_source"] = ""
    index = {tuple(r[k] for k in KEY): i for i, r in out.iterrows()}
    if len(index) != len(out):
        raise RevisionError("Duplicate effective contract rows: original inventories hold duplicate (canonical_id, original_rank, original_contract) keys")
    if revisions.empty:
        return out
    if revisions.duplicated(list(KEY) + ["revision"]).any():
        raise RevisionError("a revision id appears twice for the same contract key")
    revisions = revisions.assign(_n=revisions["revision"].map(_number)).sort_values(list(KEY) + ["_n"])
    for r in revisions.to_dict("records"):
        key = tuple(r[k] for k in KEY)
        if key not in index:
            raise RevisionError(f"revision {r['revision']} for unknown contract {key}: no original row to revise")
        i = index[key]
        if out.at[i, "local_key"] != r["local_key"]:
            raise RevisionError(f"revision {r['revision']} for {key} names local key {r['local_key']}, not {out.at[i, 'local_key']}")
        if out.at[i, "effective_revision"] != r["parent_revision"]:
            raise RevisionError(f"broken chain for {key}: {r['revision']} names parent {r['parent_revision']} but the effective "
                                f"revision is {out.at[i, 'effective_revision']}")
        if out.at[i, "sporting_grade"] == "UNATTAINABLE":
            raise RevisionError(f"PERMANENTLY_CLOSED_UNATTAINABLE: {key}; no future settlement attempt")
        out.at[i, "sporting_grade"] = r["sporting_grade"]
        out.at[i, "evidence_class"] = r["evidence_class"]
        out.at[i, "effective_revision"] = r["revision"]
        out.at[i, "revision_chain"] += " > " + r["revision"]
        out.at[i, "revision_source"] = r["revision_file"]
    return out


def effective_rows(root=ROOT) -> pd.DataFrame:
    """Every local-layout original row with its validated revisions applied (the authoritative effective view)."""
    root = Path(root)
    frames = [normalize_inventory(pd.read_csv(p, dtype=str, keep_default_na=False)).assign(inventory=str(p.relative_to(root).as_posix()))
              for p in original_inventories(root)]
    frames = [f for f in frames if "canonical_id" in f.columns]
    original = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    revisions = [read_revisions(p, root) for p in revision_files(root)]
    revisions = pd.concat(revisions, ignore_index=True) if revisions else pd.DataFrame(columns=REVISION_FIELDS)
    return apply_revisions(original, revisions)


def revised_frame(path: Path, frame: pd.DataFrame, root=ROOT) -> pd.DataFrame:
    """One inventory's rows with the revisions that target its keys (used by card_history for each inventory)."""
    frame = normalize_inventory(frame)
    revisions = [read_revisions(p, root) for p in revision_files(root)]
    revisions = pd.concat(revisions, ignore_index=True) if revisions else pd.DataFrame(columns=REVISION_FIELDS)
    if not revisions.empty and "canonical_id" in frame.columns:
        keys = set(map(tuple, frame[list(KEY)].to_numpy()))
        revisions = revisions[[tuple(r) in keys for r in revisions[list(KEY)].to_numpy()]]
    else:
        revisions = revisions.iloc[0:0]
    return apply_revisions(frame, revisions)


def unmatched_revisions(root=ROOT) -> list[tuple]:
    """Revision keys that match no original inventory row: a stale or mistyped revision, never silently ignored."""
    root = Path(root)
    keys = set()
    for p in original_inventories(root):
        f = normalize_inventory(pd.read_csv(p, dtype=str, keep_default_na=False))
        if "canonical_id" in f.columns:
            keys |= set(map(tuple, f[list(KEY)].to_numpy()))
    out = []
    for p in revision_files(root):
        for r in read_revisions(p, root)[list(KEY)].to_numpy():
            if tuple(r) not in keys:
                out.append(tuple(r))
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        frame = effective_rows()
    except RevisionError as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)
    args.out.mkdir(parents=True, exist_ok=False)
    buf = io.StringIO()
    frame.to_csv(buf, index=False, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    (args.out / "EFFECTIVE_SETTLEMENTS.csv").write_bytes(buf.getvalue().encode("utf-8"))
    revised = int((frame["revision_source"] != "").sum())
    print(f"{len(frame)} effective rows, {revised} revised by settlement imports -> {args.out}")


if __name__ == "__main__":
    main()

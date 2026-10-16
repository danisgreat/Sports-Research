"""Immutable, reproducible training-data releases from the learning store (LEARN-v1 admission).

A release fixes one store view (completed ingest sequence), one feature specification and one generating code
hash. For every event of the exact competition/endpoint it either ADMITS a training row (label = the effective
reviewed result in that view; features = FEAT-v1 as of the event's own start) or records the exact EXCLUSION
reason. Verified research-only training candidates (ml.research_learning) are linked by event ID, and candidates
with no structured history are listed rather than silently dropped.

Rebuilding a release from the same store view produces byte-identical ROWS/EXCLUSIONS (verified by ``verify``).
Later corrections create a new release; an existing release directory is never overwritten.
"""
from __future__ import annotations

import argparse
import math
import secrets
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ml import features as F
from ml import primary as p
from ml import research_ingest as ri
from ml import research_learning as rl

RELEASE_VERSION = "TRAIN-RELEASE-2026.10.16-v1"
LABEL_COLUMNS = ("hs", "as_", "reg_hs", "reg_as", "decision", "margin", "total", "home_win", "label_revision",
                 "label_available_at")
ID_COLUMNS = ("event_uid", "native_event_id", "competition", "endpoint", "season", "event_at", "home", "away",
              "candidate_card_id")


def _candidates(root: Path | None) -> dict:
    """event_id -> card_id for every verified research-only candidate under ``root`` (any revision folder)."""
    found = {}
    if root is None or not Path(root).exists():
        return found
    for receipt in sorted(Path(root).rglob("RECEIPT.csv")):
        try:
            rec = rl.verify_candidate(receipt.parent)
        except (p.AdmissionError, KeyError, FileNotFoundError):
            continue
        found.setdefault(rec["event_id"], rec["card_id"])
    return found


def build_rows(store: ri.Store, competition: str, endpoint: str, *, min_games: int = 5,
               candidates: dict | None = None) -> tuple[list[dict], list[dict]]:
    candidates = candidates or {}
    labels = ri.effective_results(store)
    quarantined = set(store.quarantine.native_event_id[store.quarantine.competition == competition])
    events = store.events[(store.events.competition == competition) & (store.events.endpoint == endpoint)]
    events = events.assign(t_at=events.event_at.map(p.clock)).sort_values(["t_at", "event_uid"])
    by_uid = labels.set_index("event_uid") if len(labels) else labels
    rows, excluded = [], []
    for ev in events.itertuples():
        ident = {k: getattr(ev, k) for k in ID_COLUMNS if k != "candidate_card_id"}
        ident["candidate_card_id"] = candidates.get(ev.native_event_id, "")
        if ev.event_uid not in getattr(by_uid, "index", []):
            excluded.append(dict(**ident, reason="NO_REVIEWED_RESULT"))
            continue
        lab = by_uid.loc[ev.event_uid]
        if lab.status not in ri.FINAL_STATUSES:
            excluded.append(dict(**ident, reason="NOT_FINAL:" + lab.status))
            continue
        if lab.reg_hs == "NOT_OBSERVED" or lab.reg_as == "NOT_OBSERVED":
            excluded.append(dict(**ident, reason="REGULATION_NOT_OBSERVED: final-endpoint cycle may use the label; regulation release cannot"))
            continue
        if ev.native_event_id in quarantined:
            excluded.append(dict(**ident, reason="OPEN_QUARANTINE: unresolved conflicting or unreviewed observation"))
            continue
        feats = F.build(store, competition, endpoint, ev.home, ev.away, ev.event_at, target_event_uid=ev.event_uid,
                        season=str(ev.season))
        short = min(feats["home_L5_net__n"], feats["away_L5_net__n"])
        if short < min_games:
            excluded.append(dict(**ident, reason=f"INSUFFICIENT_HISTORY: min side L5 n={short} < {min_games}"))
            continue
        hs, as_ = int(lab.hs), int(lab.as_)
        label = dict(hs=hs, as_=as_, reg_hs=int(lab.reg_hs), reg_as=int(lab.reg_as), decision=lab.decision,
                     margin=hs - as_, total=hs + as_, home_win=int(hs > as_), label_revision=int(lab.revision),
                     label_available_at=lab.valid_from.isoformat())
        values = {k: ("" if isinstance(v, float) and math.isnan(v) else (repr(v) if isinstance(v, float) else v))
                  for k, v in feats.items() if k not in ("spec_version", "as_of")}
        rows.append(dict(**ident, **label, feature_as_of=feats["as_of"], **values))
    known = set(events.native_event_id)
    for event_id, card in sorted(candidates.items()):
        if event_id not in known:
            excluded.append(dict(event_uid="", native_event_id=event_id, competition=competition, endpoint=endpoint,
                                 season="", event_at="", home="", away="", candidate_card_id=card,
                                 reason="CANDIDATE_WITHOUT_STRUCTURED_HISTORY: ingest its research export"))
    return rows, excluded


def _manifest(store: ri.Store, competition, endpoint, release_id, rows, excluded, min_games, code) -> dict:
    return dict(release_id=release_id, release_version=RELEASE_VERSION, competition=competition, endpoint=endpoint,
                store_root=str(store.root), store_view_seq=store.view_seq, store_digest=ri.store_digest(store),
                feature_spec=F.SPEC_VERSION, min_games=min_games, rows=len(rows), excluded=len(excluded),
                code_sha256=code, repository_head=p.repository_head(),
                created_at=datetime.now(timezone.utc).isoformat(),
                qualification="TRAINING_DATA_ONLY_NOT_A_MODEL_OR_PREDICTIVE_CLAIM")


def _coverage(rows: list[dict]) -> list[dict]:
    if not rows:
        return [dict(feature="NONE", rows=0, missing=0)]
    names = [k for k in rows[0] if k.endswith("__missing")]
    return [dict(feature=k[:-9], rows=len(rows), missing=sum(int(r[k]) for r in rows)) for k in names]


def build_release(store_root: Path, competition: str, endpoint: str, out_root: Path, release_id: str, *,
                  view_seq: int | None = None, min_games: int = 5, candidates_root: Path | None = None) -> dict:
    if not release_id.strip() or any(c in release_id for c in "/\\") or release_id in (".", ".."):
        raise p.AdmissionError("plain release identifier required")
    out = Path(out_root) / release_id
    if out.exists():
        raise FileExistsError(out)
    code = p.source_hash()
    store = ri.load_store(store_root, view_seq)
    rows, excluded = build_rows(store, competition, endpoint, min_games=min_games,
                                candidates=_candidates(candidates_root))
    if not rows:
        raise p.AdmissionError("no admitted training rows; the exclusion list explains why")
    artifacts = {"ROWS.csv": p.csv_bytes(rows),
                 "EXCLUSIONS.csv": p.csv_bytes(excluded) if excluded else b"event_uid,reason\n",
                 "COVERAGE.csv": p.csv_bytes(_coverage(rows))}
    manifest = _manifest(store, competition, endpoint, release_id, rows, excluded, min_games, code)
    manifest.update({k.replace(".", "_").lower() + "_sha256": p.digest(v) for k, v in artifacts.items()})
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = out.parent / ("." + out.name + "." + secrets.token_hex(6))
    temporary.mkdir()
    try:
        for name, data in artifacts.items():
            (temporary / name).write_bytes(data)
        (temporary / "MANIFEST.csv").write_bytes(p.csv_bytes([manifest]))
        if p.source_hash() != code:
            raise p.AdmissionError("generating source changed during release build")
        temporary.rename(out)
    finally:
        if temporary.exists():
            for child in temporary.iterdir():
                child.unlink()
            temporary.rmdir()
    verify_release(out, rebuild=False)
    return manifest


def verify_release(folder: Path, *, rebuild: bool = True) -> dict:
    """Hash custody always; with ``rebuild`` also re-derive rows from the recorded store view (determinism)."""
    folder = Path(folder)
    rows = p.read_rows(folder / "MANIFEST.csv")
    if len(rows) != 1 or rows[0]["release_version"] != RELEASE_VERSION:
        raise p.AdmissionError("one release manifest of the current version required")
    man = rows[0]
    for name in ("ROWS.csv", "EXCLUSIONS.csv", "COVERAGE.csv"):
        p.receipt_file(folder / name, man[name.replace(".", "_").lower() + "_sha256"])
    data = p.read_rows(folder / "ROWS.csv")
    if len(data) != int(man["rows"]) or len({r["event_uid"] for r in data}) != len(data):
        raise p.AdmissionError("release rows differ from manifest or repeat an event")
    for r in data:
        if not p.clock(r["event_at"]) <= p.clock(r["label_available_at"]) or p.clock(r["feature_as_of"]) != p.clock(r["event_at"]):
            raise p.AdmissionError("release row chronology invalid (features must be as of the event start)")
    if rebuild:
        store = ri.load_store(Path(man["store_root"]), int(man["store_view_seq"]))
        if ri.store_digest(store) != man["store_digest"]:
            raise p.AdmissionError("store view changed since the release; append-only custody broken")
        if man["feature_spec"] != F.SPEC_VERSION:
            raise p.AdmissionError("feature specification changed; build a new release instead of re-deriving")
        again, _ = build_rows(store, man["competition"], man["endpoint"], min_games=int(man["min_games"]),
                              candidates={r["native_event_id"]: r["candidate_card_id"] for r in data if r["candidate_card_id"]})
        if p.csv_bytes(again) != (folder / "ROWS.csv").read_bytes():
            raise p.AdmissionError("release rows are not reproducible from the recorded store view")
    return man


def load_rows(folder: Path) -> pd.DataFrame:
    verify_release(folder, rebuild=False)
    frame = pd.read_csv(Path(folder) / "ROWS.csv", keep_default_na=True)
    frame["event_at"] = frame.event_at.map(p.clock)
    frame["label_available_at"] = frame.label_available_at.map(p.clock)
    return frame


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("--store", type=Path, required=True)
    for name in ("competition", "endpoint", "release-id"):
        b.add_argument("--" + name, required=True)
    b.add_argument("--out-root", type=Path, required=True)
    b.add_argument("--view-seq", type=int)
    b.add_argument("--min-games", type=int, default=5)
    b.add_argument("--candidates", type=Path, help="research/training_candidates root to link")
    v = sub.add_parser("verify")
    v.add_argument("--release", type=Path, required=True)
    v.add_argument("--no-rebuild", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "build":
        man = build_release(args.store, args.competition, args.endpoint, args.out_root, args.release_id,
                            view_seq=args.view_seq, min_games=args.min_games, candidates_root=args.candidates)
    else:
        man = verify_release(args.release, rebuild=not args.no_rebuild)
    print(f"{man['release_id']}: rows={man['rows']} excluded={man['excluded']} view={man['store_view_seq']} "
          f"spec={man['feature_spec']}")


if __name__ == "__main__":
    main()

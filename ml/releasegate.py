"""Data-quality gate that must pass before a release is frozen for a competition (REV-22; GATE-v2, CR-2026.11.08-R2).

    python -m ml release-gate --competition "Basketball/NBA" [--min-events 300]

The gate reads only the learning store. A release lane is the only evidence that can promote a model, so a lane may not start
on data with an open integrity flag. It checks, for the competition:

  G1  enough verified final events (default 300) over at least two seasons
  G2  the repository's plausibility checks (overtime field, score dispersion) raise no warning
  G3  nothing from this competition sits in quarantine
  G4  every effective final is supported by at least two observations OF THAT REVISION from different registrable domains
      (sub-domains of one site are one lineage) with different captures; the collectors are reported
  G5  both regulation coordinates are observed whenever the decision says extra time
  G6  no event carries two different effective finals (a result revision conflict)

Every run writes a versioned receipt bound to the exact store snapshot under research/release_gates/. ``python -m ml cycle
release`` refuses to freeze a release without a PASSED receipt for the same competition and the same snapshot (GATE-v2).
Releases frozen before GATE-v2 (MLB-CYCLE-4, NHL-CYCLE-4, NBA-CYCLE-1) are carried forward as they were made and are reported
as CARRIED_FORWARD_BEFORE_GATE_V2; their data limitations stay visible in their own records.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from ml import config

ROOT = Path(__file__).resolve().parents[1]
STORE = "research/learning_store"
RECEIPTS = "research/release_gates"
GATE_VERSION = "GATE-v2"
EXTRA = {"Overtime", "Shootout", "EXTRAS", "OT", "SO"}
SUPPORTING = {"FIRST_OBSERVED", "CORROBORATING", "CORRECTION"}
SNAPSHOT_FILES = ("EVENTS.csv", "RESULTS.csv", "SOURCE_OBSERVATIONS.csv", "QUARANTINE.csv", "INGEST_RECEIPTS.csv",
                  "EVENT_ALIASES.csv", "TEAM_GAME_STATS.csv", "PLAYER_AVAILABILITY.csv")
SECOND_LEVEL = {"co.uk", "org.uk", "gov.uk", "ac.uk", "com.au", "net.au", "org.au", "co.nz", "co.jp", "or.jp", "ne.jp", "co.kr",
                "or.kr", "com.br", "com.mx", "com.ar", "co.in", "com.cn", "com.tw", "co.za", "com.sg", "com.ph"}
RECEIPT_FIELDS = ("gate_version", "competition", "min_events", "passed", "finals", "store_snapshot_sha256", "generated_at", "checks")


def _rows(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def registrable(url: str) -> str:
    """The registrable domain of a URL (www.espn.com and site.api.espn.com are one lineage, espn.com)."""
    host = (urlparse(url).hostname or "").lower().strip(".")
    labels = host.split(".")
    if len(labels) >= 3 and ".".join(labels[-2:]) in SECOND_LEVEL:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:]) if len(labels) >= 2 else host


def store_snapshot(root=ROOT) -> str:
    """SHA-256 over the store files in a fixed order: the exact data a gate verdict is about."""
    h = hashlib.sha256()
    for name in SNAPSHOT_FILES:
        path = Path(root) / STORE / name
        h.update(name.encode())
        h.update(hashlib.sha256(path.read_bytes()).digest() if path.exists() else b"MISSING")
    return h.hexdigest()


def gate(competition: str, root=ROOT, min_events: int = 300) -> dict:
    store = Path(root) / STORE
    events = {r["event_uid"]: r for r in _rows(store / "EVENTS.csv") if r["competition"] == competition}
    latest: dict = {}
    for r in _rows(store / "RESULTS.csv"):
        if r["event_uid"] in events and r["status"] == "FINAL":
            old = latest.get(r["event_uid"])
            if old is None or int(r["revision"]) > int(old["revision"]):
                latest[r["event_uid"]] = r
    sport = competition.split("/")[0].strip()
    checks = []

    def check(code, ok, detail):
        checks.append(dict(check=code, status="PASS" if ok else "FAIL", detail=detail))

    seasons = defaultdict(list)
    for uid, r in latest.items():
        seasons[events[uid]["season"]].append(int(r["hs"]) - int(r["as_"]))
    check("G1", len(latest) >= min_events and len(seasons) >= 2,
          f"{len(latest)} final events over {len(seasons)} season(s): " + ", ".join(f"{s}: {len(m)}" for s, m in sorted(seasons.items())))
    explicit = [r for r in latest.values() if r["decision"] != ""]
    extra = [r for r in explicit if r["decision"] in EXTRA]
    warnings = config.integrity_warnings(sport, (len(latest), len(explicit), len(extra)),
                                         {int(s) if str(s).isdigit() else i: m for i, (s, m) in enumerate(sorted(seasons.items()))})
    check("G2", not warnings, "; ".join(warnings) or f"overtime/extras in {len(extra)} of {len(explicit)} explicit decisions")
    quarantined = [r for r in _rows(store / "QUARANTINE.csv") if r["competition"] == competition]
    check("G3", not quarantined, f"{len(quarantined)} quarantined observation(s)")
    support = defaultdict(lambda: dict(domains=set(), captures=set(), collectors=set()))
    for r in _rows(store / "SOURCE_OBSERVATIONS.csv"):
        uid = r["event_uid"]
        if r["kind"] != "RESULT" or uid not in latest or r["disposition"] not in SUPPORTING:
            continue
        if r["link"] != latest[uid]["revision"]:
            continue                     # an observation of another revision does not support the effective final
        s = support[uid]
        s["domains"].add(registrable(r["source_url"]))
        s["captures"].add(r["capture_sha256"] or r["observation_id"])
        s["collectors"].add(r["collected_by"] or "UNKNOWN")
    single = [uid for uid in latest if len(support[uid]["domains"]) < 2 or len(support[uid]["captures"]) < 2]
    collectors = sorted({c for s in support.values() for c in s["collectors"]})
    check("G4", not single, f"{len(single)} effective final(s) without two independent supporting lineages "
                            f"(registrable domains and captures of the effective revision); collectors: {', '.join(collectors) or 'none'}")
    bad = [r for r in latest.values() if r["decision"] in EXTRA
           and (r["reg_hs"] in ("", "NOT_OBSERVED", "UNKNOWN") or r["reg_as"] in ("", "NOT_OBSERVED", "UNKNOWN"))]
    check("G5", not bad, f"{len(bad)} extra-time final(s) without both observed regulation scores")
    conflicts = 0
    seen: dict = {}
    for r in _rows(store / "RESULTS.csv"):
        if r["event_uid"] in events and r["status"] == "FINAL":
            key = (r["event_uid"], r["revision"])
            value = (r["hs"], r["as_"])
            if key in seen and seen[key] != value:
                conflicts += 1
            seen[key] = value
    check("G6", conflicts == 0, f"{conflicts} result revision conflict(s)")
    return dict(competition=competition, passed=all(c["status"] == "PASS" for c in checks), checks=checks, finals=len(latest),
                min_events=min_events, store_snapshot_sha256=store_snapshot(root), gate_version=GATE_VERSION)


def write_receipt(result: dict, root=ROOT) -> Path:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", result["competition"]).strip("_")
    stamp = datetime.now(timezone.utc)
    path = Path(root) / RECEIPTS / slug / f"{stamp.strftime('%Y%m%dT%H%M%S%fZ')}_GATE.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    row = dict(gate_version=result["gate_version"], competition=result["competition"], min_events=result["min_events"],
               passed=str(result["passed"]), finals=result["finals"], store_snapshot_sha256=result["store_snapshot_sha256"],
               generated_at=stamp.isoformat(), checks=" | ".join(f"{c['check']} {c['status']}: {c['detail']}" for c in result["checks"]))
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=list(RECEIPT_FIELDS), lineterminator="\n")
    w.writeheader()
    w.writerow(row)
    with path.open("xb") as fh:
        fh.write(out.getvalue().encode("utf-8"))
    return path


def verify_receipt(path, competition: str, root=ROOT) -> dict:
    """A PASSED receipt of the current gate version, for this competition, on the store exactly as it is now."""
    rows = _rows(Path(path))
    if len(rows) != 1 or tuple(rows[0]) != RECEIPT_FIELDS:
        raise ValueError("GATE_RECEIPT_SCHEMA: not a release-gate receipt")
    r = rows[0]
    if r["gate_version"] != GATE_VERSION:
        raise ValueError(f"GATE_RECEIPT_VERSION: receipt is {r['gate_version']}, the gate is {GATE_VERSION}; rerun the gate")
    if r["competition"] != competition:
        raise ValueError(f"GATE_RECEIPT_SCOPE: receipt is for {r['competition']}, not {competition}")
    if r["passed"] != "True":
        raise ValueError("GATE_FAILED: the receipt records a failed gate; a release may not be frozen on it")
    if r["store_snapshot_sha256"] != store_snapshot(root):
        raise ValueError("GATE_STALE: the store changed after the gate ran; rerun the gate on the current store")
    return r


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--competition", required=True)
    parser.add_argument("--min-events", type=int, default=300)
    args = parser.parse_args(argv)
    result = gate(args.competition, ROOT, args.min_events)
    for c in result["checks"]:
        print(f"{c['check']} {c['status']}: {c['detail']}")
    receipt = write_receipt(result, ROOT)
    print("RELEASE GATE", "PASSED" if result["passed"] else "FAILED", "-", args.competition, "- receipt", receipt.relative_to(ROOT).as_posix())
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

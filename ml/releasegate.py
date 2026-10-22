"""Data-quality gate that must pass before a release is frozen for a competition (REV-22).

    python -m ml release-gate --competition "Basketball/NBA" [--min-events 300]

The gate reads only the learning store. A release lane is the only evidence that can promote a model, so a lane may not start
on data with an open integrity flag. It checks, for the competition:

  G1  enough verified final events (default 300) over at least two seasons
  G2  the repository's plausibility checks (overtime field, score dispersion) raise no warning
  G3  nothing from this competition sits in quarantine
  G4  every final result is supported by at least two source observations on different domains
      (necessary, not sufficient, for independent lineages: the ingest report names the two collectors)
  G5  regulation coordinates are observed whenever the decision says extra time
  G6  no event carries two different effective finals (a result revision conflict)
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

from ml import config

ROOT = Path(__file__).resolve().parents[1]
STORE = "research/learning_store"
EXTRA = {"Overtime", "Shootout", "EXTRAS", "OT", "SO"}


def _rows(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


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
    domains = defaultdict(set)
    for r in _rows(store / "SOURCE_OBSERVATIONS.csv"):
        if r["kind"] == "RESULT" and r["event_uid"] in latest:
            domains[r["event_uid"]].add(urlparse(r["source_url"]).netloc.lower())
    single = [uid for uid in latest if len(domains.get(uid, ())) < 2]
    check("G4", not single, f"{len(single)} final(s) with fewer than two source domains")
    bad = [r for r in latest.values() if r["decision"] in EXTRA and r["reg_hs"] in ("", "NOT_OBSERVED", "UNKNOWN")]
    check("G5", not bad, f"{len(bad)} extra-time final(s) without observed regulation scores")
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
    return dict(competition=competition, passed=all(c["status"] == "PASS" for c in checks), checks=checks, finals=len(latest))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--competition", required=True)
    parser.add_argument("--min-events", type=int, default=300)
    args = parser.parse_args(argv)
    result = gate(args.competition, ROOT, args.min_events)
    for c in result["checks"]:
        print(f"{c['check']} {c['status']}: {c['detail']}")
    print("RELEASE GATE", "PASSED" if result["passed"] else "FAILED", "-", args.competition)
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

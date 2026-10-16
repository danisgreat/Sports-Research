"""Normalised, deduplicated and point-in-time learning store built from prompt-1 research exports (LEARN-v1).

Every researched card can export the prior games, team statistics and availability rows it actually opened.
Ingest turns those exports into one append-only store per repository:

    EVENTS.csv               one row per sporting event (stable event_uid; native ID or date/participant basis)
    EVENT_ALIASES.csv        later native IDs for an event first stored under a date/participant identity
    RESULTS.csv              result revisions per event (revision 1, then reviewed WEB_CORRECTED corrections)
    TEAM_GAME_STATS.csv      team statistic revisions per event (long format)
    PLAYER_AVAILABILITY.csv  dated availability snapshots for target events (never "assumed healthy")
    SOURCE_OBSERVATIONS.csv  every distinct source observation and what it did (new/corroborating/correction)
    QUARANTINE.csv           rejected observations with the exact reason; nothing is silently dropped
    INGEST_RECEIPTS.csv      one row per ingest, written last; rows of an unfinished ingest are invisible

The same match researched in five minis is one event with up to five source observations, never five training
games. A result's availability (``valid_from``) is the earliest known_at of the reviewed observations that support
it, so rebuilding a view "as of" an earlier instant cannot see later games, later corrections or later team news.
The retired results store is not a source. No market fields are accepted (exact schemas).
"""
from __future__ import annotations

import argparse
import hashlib
import io
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ml import primary as p
import csv
import math
from types import SimpleNamespace

SCHEMA_VERSION = "LEARN-STORE-2026.10.16-v1"
GAME_FIELDS = ("competition", "endpoint", "native_event_id", "season", "event_at", "home", "away", "venue", "status",
               "hs", "as_", "reg_hs", "reg_as", "decision", "final_at", "source_url", "source_kind", "published_at",
               "retrieved_at", "known_at", "capture_path", "capture_sha256", "review_status", "collected_by")
STAT_FIELDS = ("competition", "native_event_id", "team", "stat", "value", "source_url", "source_kind", "published_at",
               "retrieved_at", "known_at", "capture_path", "capture_sha256", "review_status", "collected_by")
AVAIL_FIELDS = ("competition", "native_event_id", "team", "player", "role", "status", "confirmation", "published_at",
                "retrieved_at", "known_at", "source_url", "capture_path", "capture_sha256", "review_status",
                "collected_by")
TARGET_FIELDS = ("competition", "endpoint", "native_event_id", "season", "scheduled_start", "home", "away", "venue",
                 "source_url", "known_at", "capture_path", "capture_sha256", "collected_by")
EXPORT_FILES = {"GAME_OBSERVATIONS.csv": GAME_FIELDS, "TEAM_GAME_STATS.csv": STAT_FIELDS,
                "AVAILABILITY.csv": AVAIL_FIELDS, "TARGET_EVENT.csv": TARGET_FIELDS}

STORE_FILES = {
    "EVENTS.csv": ("event_uid", "competition", "endpoint", "native_event_id", "identity_basis", "season", "event_at",
                   "home", "away", "venue", "ingest_seq"),
    "EVENT_ALIASES.csv": ("event_uid", "alias_native_event_id", "ingest_seq"),
    "RESULTS.csv": ("event_uid", "revision", "status", "hs", "as_", "reg_hs", "reg_as", "decision", "final_at",
                    "revision_basis", "ingest_seq"),
    "TEAM_GAME_STATS.csv": ("event_uid", "team", "stat", "revision", "value", "ingest_seq"),
    "PLAYER_AVAILABILITY.csv": ("event_uid", "team", "player", "role", "status", "confirmation", "known_at",
                                "observation_id", "ingest_seq"),
    "SOURCE_OBSERVATIONS.csv": ("observation_id", "kind", "event_uid", "link", "disposition", "source_url",
                                "source_kind", "published_at", "retrieved_at", "known_at", "capture_path",
                                "capture_sha256", "collected_by", "ingest_seq"),
    "QUARANTINE.csv": ("ingest_seq", "kind", "observation_id", "competition", "native_event_id", "reason",
                       "source_url", "row_digest"),
    "INGEST_RECEIPTS.csv": ("ingest_seq", "ingested_at", "export_path", "export_sha256", "schema_version",
                            "code_sha256", "observations", "new_events", "new_results", "corroborating",
                            "corrections", "quarantined", "exact_duplicates"),
}
FINAL_STATUSES = ("FINAL",)
GAME_STATUSES = ("FINAL", "ABANDONED", "FORFEIT", "AWARDED", "POSTPONED", "CANCELLED")
SOURCE_KINDS = ("WEB_RECOVERED", "WEB_CORRECTED")
AVAIL_ROLES = ("STARTER", "BENCH", "NOT_IN_SQUAD", "UNKNOWN")
AVAIL_STATUSES = ("CONFIRMED_ACTIVE", "CONFIRMED_OUT", "DOUBTFUL", "QUESTIONABLE", "PROBABLE", "PROJECTED", "UNKNOWN")
AVAIL_CONFIRMATIONS = ("OFFICIAL_CONFIRMED", "REPORTED", "PROJECTED")
RETIRED_SOURCES = ("previous sports results",)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _row_digest(row: dict, fields) -> str:
    return hashlib.sha256("\x1f".join(str(row.get(f, "")) for f in fields).encode()).hexdigest()


def _iso(value) -> str:
    return p.clock(value).isoformat()


def _int(value, name) -> int:
    x = float(value)
    if not math.isfinite(x) or x < 0 or x != int(x):
        raise p.AdmissionError(f"{name} must be a nonnegative integer")
    return int(x)


def event_uid(competition: str, native_event_id: str, basis: str) -> str:
    return "E" + hashlib.sha256(f"{competition}|{basis}|{native_event_id}".encode()).hexdigest()[:20]


def surrogate_id(event_at: str, home: str, away: str) -> str:
    return f"DATE:{p.clock(event_at).date().isoformat()}:{home}:{away}"


# ---------------------------------------------------------------------------------------------------------- store
@dataclass
class Store:
    root: Path
    view_seq: int
    tables: dict

    def __getattr__(self, name):
        if name == "tables":
            raise AttributeError(name)
        key = name.upper() + ".csv"
        if key in self.tables:
            return self.tables[key]
        raise AttributeError(name)


def _read(path: Path, fields) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=list(fields), dtype=str)
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    if tuple(frame.columns) != tuple(fields):
        raise p.AdmissionError(f"store table {path.name} has unexpected columns")
    return frame


def load_store(root: Path, view_seq: int | None = None) -> Store:
    """Read the store as of a completed ingest sequence (default: the latest completed one)."""
    root = Path(root)
    tables = {name: _read(root / name, fields) for name, fields in STORE_FILES.items()}
    receipts = tables["INGEST_RECEIPTS.csv"]
    done = sorted(int(s) for s in receipts.ingest_seq) if len(receipts) else []
    if len(done) != len(set(done)):
        raise p.AdmissionError("duplicate ingest receipts")
    latest = done[-1] if done else 0
    if view_seq is None:
        view_seq = latest
    if view_seq > latest or view_seq < 0 or (view_seq and view_seq not in done):
        raise p.AdmissionError("requested store view is not a completed ingest")
    for name, frame in tables.items():
        seq = pd.to_numeric(frame.ingest_seq, errors="coerce") if len(frame) else pd.Series(dtype=float)
        tables[name] = frame[seq.isin(done) & (seq <= view_seq)].reset_index(drop=True) if len(frame) else frame
    return Store(root, view_seq, tables)


def store_digest(store: Store) -> str:
    """SHA-256 of every table restricted to the view: equal views have equal digests."""
    h = hashlib.sha256()
    for name in STORE_FILES:
        h.update(name.encode())
        h.update(hashlib.sha256(store.tables[name].to_csv(index=False, lineterminator="\n").encode()).digest())
    return h.hexdigest()


def resolve_event(store_events: pd.DataFrame, aliases: pd.DataFrame, competition: str, native: str,
                  event_at: str, home: str, away: str) -> str | None:
    comp = store_events[store_events.competition == competition]
    if native:
        hit = comp[comp.native_event_id == native]
        if len(hit):
            return hit.iloc[0].event_uid
        alias = aliases[aliases.alias_native_event_id == f"{competition}|{native}"]
        if len(alias):
            return alias.iloc[0].event_uid
    surrogate = surrogate_id(event_at, home, away)
    hit = comp[(comp.native_event_id == surrogate)]
    return hit.iloc[0].event_uid if len(hit) else None


def _valid_from(store: Store) -> dict:
    """(event_uid, revision) -> earliest known_at of a reviewed observation supporting that result revision."""
    obs = store.source_observations
    obs = obs[(obs.kind == "RESULT") & obs.disposition.isin(["FIRST_OBSERVED", "CORROBORATING", "CORRECTION"])]
    out = {}
    for r in obs.itertuples():
        key = (r.event_uid, int(r.link))
        t = p.clock(r.known_at)
        if key not in out or t < out[key]:
            out[key] = t
    return out


def effective_results(store: Store, as_of=None) -> pd.DataFrame:
    """Latest result revision per event whose availability is at or before ``as_of`` (all revisions if None)."""
    res = store.results.copy()
    if res.empty:
        return res.assign(valid_from=pd.Series(dtype=object))
    vf = _valid_from(store)
    res["valid_from"] = [vf.get((r.event_uid, int(r.revision))) for r in res.itertuples()]
    res = res[res.valid_from.notna()]
    if as_of is not None:
        limit = p.clock(as_of)
        res = res[res.valid_from.map(lambda t: t <= limit)]
    res = res.assign(_rev=res.revision.astype(int)).sort_values(["event_uid", "_rev"])
    return res.groupby("event_uid", sort=True).tail(1).drop(columns="_rev").reset_index(drop=True)


def effective_stats(store: Store, as_of=None) -> pd.DataFrame:
    stats = store.team_game_stats.copy()
    if stats.empty:
        return stats.assign(valid_from=pd.Series(dtype=object))
    obs = store.source_observations
    obs = obs[(obs.kind == "TEAM_STAT") & obs.disposition.isin(["FIRST_OBSERVED", "CORROBORATING", "CORRECTION"])]
    first = {}
    for r in obs.itertuples():
        key = r.link
        t = p.clock(r.known_at)
        if key not in first or t < first[key]:
            first[key] = t
    stats["valid_from"] = [first.get(f"{r.event_uid}|{r.team}|{r.stat}|{r.revision}") for r in stats.itertuples()]
    stats = stats[stats.valid_from.notna()]
    if as_of is not None:
        limit = p.clock(as_of)
        stats = stats[stats.valid_from.map(lambda t: t <= limit)]
    stats = stats.assign(_rev=stats.revision.astype(int)).sort_values(["event_uid", "team", "stat", "_rev"])
    return stats.groupby(["event_uid", "team", "stat"], sort=True).tail(1).drop(columns="_rev").reset_index(drop=True)


def availability_as_of(store: Store, event: str, as_of) -> pd.DataFrame:
    """Latest availability snapshot per (team, player) published at or before ``as_of``; empty means unknown."""
    rows = store.player_availability
    rows = rows[rows.event_uid == event]
    if rows.empty:
        return rows
    limit = p.clock(as_of)
    rows = rows[rows.known_at.map(lambda t: p.clock(t) <= limit)]
    rows = rows.assign(t_at=rows.known_at.map(p.clock)).sort_values(["team", "player", "t_at", "observation_id"])
    return rows.groupby(["team", "player"], sort=True).tail(1).drop(columns="t_at").reset_index(drop=True)


def history_rows(store: Store, competition: str, endpoint: str, horizon, exclude_event: str = "") -> list[dict]:
    """HISTORY.csv rows for ``primary predict``: FINAL results known by the horizon, game day before the horizon day.

    ``exclude_event`` is the target's native ID or event_uid. Evidence is the earliest supporting reviewed capture.
    """
    limit = p.clock(horizon)
    res = effective_results(store, limit)
    events = store.events.set_index("event_uid")
    obs = store.source_observations
    obs = obs[(obs.kind == "RESULT") & obs.disposition.isin(["FIRST_OBSERVED", "CORROBORATING", "CORRECTION"])]
    out = []
    for r in res.itertuples():
        ev = events.loc[r.event_uid]
        if ev.competition != competition or ev.endpoint != endpoint or r.status not in FINAL_STATUSES:
            continue
        if exclude_event and exclude_event in (r.event_uid, ev.native_event_id):
            continue
        when = p.clock(ev.event_at)
        if not when < limit.normalize() or p.clock(r.final_at) > limit:
            continue
        support = obs[(obs.event_uid == r.event_uid) & (obs.link == str(r.revision))]
        support = support.assign(t_at=support.known_at.map(p.clock)).sort_values(["t_at", "observation_id"])
        first = support[support.t_at <= limit].iloc[0]
        out.append(dict(event_id=ev.native_event_id, competition=competition, endpoint=endpoint,
                        date=when.isoformat(), final_at=_iso(r.final_at), available_at=first.t_at.isoformat(),
                        status="FINAL", admission="RESEARCH_INPUT_REVIEWED", source_url=first.source_url,
                        evidence_path=first.capture_path, evidence_sha256=first.capture_sha256,
                        source_kind=first.source_kind, season=ev.season, home=ev.home, away=ev.away,
                        hs=r.hs, as_=r.as_, reg_hs=r.reg_hs, reg_as=r.reg_as, decision=r.decision))
    return sorted(out, key=lambda r: (r["date"], r["event_id"]))


# --------------------------------------------------------------------------------------------------------- ingest
def _read_export(folder: Path) -> dict:
    folder = Path(folder)
    if not folder.is_dir():
        raise p.AdmissionError("research export folder not found")
    found = {}
    for name, fields in EXPORT_FILES.items():
        path = folder / name
        if not path.exists():
            found[name] = []
            continue
        rows = p.read_rows(path)
        if rows and set(rows[0]) != set(fields):
            raise p.AdmissionError(f"{name} requires the exact {SCHEMA_VERSION} columns; extra/market columns prohibited")
        if not rows:
            with path.open(encoding="utf-8-sig") as f:
                header = f.readline().strip().split(",")
            if set(header) != set(fields):
                raise p.AdmissionError(f"{name} requires the exact {SCHEMA_VERSION} columns")
        found[name] = rows
    if not any(found.values()):
        raise p.AdmissionError("empty research export")
    return found


def export_digest(folder: Path) -> str:
    h = hashlib.sha256()
    for name in sorted(EXPORT_FILES):
        path = Path(folder) / name
        if path.exists():
            h.update(name.encode())
            h.update(hashlib.sha256(path.read_bytes()).digest())
    return h.hexdigest()


class _Batch:
    def __init__(self, store: Store, seq: int):
        self.store, self.seq = store, seq
        self.new = {name: [] for name in STORE_FILES}
        self.counts = dict(observations=0, new_events=0, new_results=0, corroborating=0, corrections=0,
                           quarantined=0, exact_duplicates=0)
        self.seen_obs = set(store.source_observations.observation_id)

    def events(self) -> pd.DataFrame:
        add = pd.DataFrame(self.new["EVENTS.csv"], columns=STORE_FILES["EVENTS.csv"])
        return pd.concat([self.store.events, add], ignore_index=True) if len(add) else self.store.events

    def aliases(self) -> pd.DataFrame:
        add = pd.DataFrame(self.new["EVENT_ALIASES.csv"], columns=STORE_FILES["EVENT_ALIASES.csv"])
        return pd.concat([self.store.event_aliases, add], ignore_index=True) if len(add) else self.store.event_aliases

    def quarantine(self, kind, oid, row, reason):
        self.counts["quarantined"] += 1
        self.new["QUARANTINE.csv"].append(dict(ingest_seq=self.seq, kind=kind, observation_id=oid,
                                               competition=row.get("competition", ""),
                                               native_event_id=row.get("native_event_id", ""), reason=reason,
                                               source_url=row.get("source_url", ""), row_digest=oid))

    def observe(self, kind, oid, uid, link, disposition, row):
        self.new["SOURCE_OBSERVATIONS.csv"].append(dict(
            observation_id=oid, kind=kind, event_uid=uid, link=str(link), disposition=disposition,
            source_url=row["source_url"], source_kind=row.get("source_kind", "WEB_RECOVERED"),
            published_at=row.get("published_at", ""), retrieved_at=row.get("retrieved_at", ""),
            known_at=_iso(row["known_at"]), capture_path=row["capture_path"], capture_sha256=row["capture_sha256"],
            collected_by=row.get("collected_by", ""), ingest_seq=self.seq))

    def event(self, row, when_field) -> str:
        """Resolve or create the event for an observation; raise on orientation/identity conflicts."""
        comp, native = row["competition"], row["native_event_id"].strip()
        home, away = row["home"].strip(), row["away"].strip()
        if not comp.strip() or "/" not in comp or not home or not away or home == away:
            raise p.AdmissionError("exact Sport/Competition identity and two distinct participants required")
        if native.startswith("DATE:"):
            raise p.AdmissionError("native_event_id may not use the reserved DATE: surrogate prefix")
        events, aliases = self.events(), self.aliases()
        uid = resolve_event(events, aliases, comp, native, row[when_field], home, away)
        if uid is not None:
            ev = events[events.event_uid == uid].iloc[0]
            if (ev.home, ev.away) != (home, away):
                raise p.AdmissionError("ORIENTATION_CONFLICT: participants differ from the stored event")
            if ev.endpoint and row.get("endpoint") and ev.endpoint != row["endpoint"]:
                raise p.AdmissionError("ENDPOINT_CONFLICT: endpoint differs from the stored event")
            if native and ev.native_event_id != native and ev.identity_basis == "DATE_PARTICIPANTS":
                key = f"{comp}|{native}"
                if not (aliases.alias_native_event_id == key).any():
                    self.new["EVENT_ALIASES.csv"].append(dict(event_uid=uid, alias_native_event_id=key,
                                                              ingest_seq=self.seq))
            return uid
        basis = "NATIVE_ID" if native else "DATE_PARTICIPANTS"
        ident = native or surrogate_id(row[when_field], home, away)
        uid = event_uid(comp, ident, basis)
        self.counts["new_events"] += 1
        self.new["EVENTS.csv"].append(dict(event_uid=uid, competition=comp, endpoint=row.get("endpoint", ""),
                                           native_event_id=ident, identity_basis=basis, season=row.get("season", ""),
                                           event_at=_iso(row[when_field]), home=home, away=away,
                                           venue=row.get("venue", ""), ingest_seq=self.seq))
        return uid


def _check_source(row, *, require_kind=True) -> None:
    if not row["source_url"].startswith("https://"):
        raise p.AdmissionError("HTTPS sporting source required")
    if require_kind and row["source_kind"] not in SOURCE_KINDS:
        reason = "RETIRED_ARCHIVE_SOURCE" if row["source_kind"] == "ARCHIVE_REVIEWED" else "UNKNOWN_SOURCE_KIND"
        raise p.AdmissionError(reason + ": new research uses WEB_RECOVERED or WEB_CORRECTED")
    if any(token in row["capture_path"].replace("\\", "/").lower() for token in RETIRED_SOURCES):
        raise p.AdmissionError("RETIRED_ARCHIVE_SOURCE: the retired results store is not a source")
    if row.get("review_status", "RESEARCH_INPUT_REVIEWED") != "RESEARCH_INPUT_REVIEWED":
        raise p.AdmissionError("UNREVIEWED: retained in quarantine until source review")
    known = p.clock(row["known_at"])
    for name in ("published_at", "retrieved_at"):
        if row.get(name, "").strip():
            p.clock(row[name])
    if row.get("retrieved_at", "").strip() and known > p.clock(row["retrieved_at"]):
        raise p.AdmissionError("KNOWN_AT_AFTER_RETRIEVAL: a fact cannot become known after it was captured")
    p.receipt_file(row["capture_path"], row["capture_sha256"])


def _game_values(row) -> dict:
    status = row["status"].strip().upper()
    if status not in GAME_STATUSES:
        raise p.AdmissionError("unknown game status")
    values = dict(status=status, decision=row["decision"].strip(), final_at="")
    if status == "FINAL":
        for col in ("hs", "as_", "reg_hs", "reg_as"):
            values[col] = str(_int(row[col], col))
        if int(values["reg_hs"]) > int(values["hs"]) or int(values["reg_as"]) > int(values["as_"]):
            raise p.AdmissionError("regulation score exceeds final score")
        event, final, known = p.clock(row["event_at"]), p.clock(row["final_at"]), p.clock(row["known_at"])
        if not event <= final <= known:
            raise p.AdmissionError("CHRONOLOGY: event_at <= final_at <= known_at required")
        values["final_at"] = final.isoformat()
    else:
        for col in ("hs", "as_", "reg_hs", "reg_as"):
            values[col] = row[col].strip()
    return values


def _same(a: dict, b) -> bool:
    return all(str(a[k]) == str(getattr(b, k)) for k in ("status", "hs", "as_", "reg_hs", "reg_as", "decision"))


def ingest(export: Path, store_root: Path, *, dry_run: bool = False) -> dict:
    """Append one research export to the store. Exact re-ingest is idempotent (all observations duplicate)."""
    store_root = Path(store_root)
    data = _read_export(export)
    store = load_store(store_root)
    # Never reuse the sequence of rows left by an interrupted ingest: they would become visible with a new receipt.
    raw = [pd.to_numeric(_read(store_root / n, f).ingest_seq, errors="coerce").max() for n, f in STORE_FILES.items()]
    seq = int(max([store.view_seq] + [x for x in raw if pd.notna(x)])) + 1
    code = p.source_hash()
    batch = _Batch(store, seq)
    pending_results = {}

    for row in data["TARGET_EVENT.csv"]:
        oid = _row_digest(row, TARGET_FIELDS)
        if oid in batch.seen_obs:
            batch.counts["exact_duplicates"] += 1
            continue
        batch.seen_obs.add(oid)
        batch.counts["observations"] += 1
        try:
            _check_source(dict(row, source_kind="WEB_RECOVERED"), require_kind=False)
            p.clock(row["scheduled_start"])
            uid = batch.event(row, "scheduled_start")
            batch.observe("TARGET", oid, uid, "", "TARGET_REGISTERED", dict(row, source_kind="WEB_RECOVERED"))
        except (p.AdmissionError, ValueError, KeyError) as e:
            batch.quarantine("TARGET", oid, row, str(e))

    games = sorted(data["GAME_OBSERVATIONS.csv"], key=lambda r: (r.get("known_at", ""), _row_digest(r, GAME_FIELDS)))
    for row in games:
        oid = _row_digest(row, GAME_FIELDS)
        if oid in batch.seen_obs:
            batch.counts["exact_duplicates"] += 1
            continue
        batch.seen_obs.add(oid)
        batch.counts["observations"] += 1
        try:
            _check_source(row)
            values = _game_values(row)
            uid = batch.event(row, "event_at")
            pending_results.setdefault(uid, []).append((oid, row, values))
        except (p.AdmissionError, ValueError, KeyError) as e:
            batch.quarantine("RESULT", oid, row, str(e))

    vf = _valid_from(store)
    for uid in sorted(pending_results):
        items = pending_results[uid]
        stored = store.results[store.results.event_uid == uid]
        if stored.empty:
            first_vals = items[0][2]
            if any(not _same(first_vals, SimpleNamespace(**v)) and r["source_kind"] != "WEB_CORRECTED" for _, r, v in items[1:]):
                for oid, row, _ in items:
                    batch.quarantine("RESULT", oid, row, "RESULT_CONFLICT_IN_EXPORT: sources disagree; resolve before admission")
                continue
            revisions = []
        else:
            revisions = [r for r in stored.sort_values("revision", key=lambda s: s.astype(int)).itertuples()]
        for oid, row, values in items:
            current = revisions[-1] if revisions else None
            if current is None:
                rev = 1
                basis = "FIRST_OBSERVED"
            elif _same(values, current):
                rev, basis = int(current.revision), "CORROBORATING"
            elif row["source_kind"] == "WEB_CORRECTED" and (
                    (uid, int(current.revision)) not in vf or p.clock(row["known_at"]) > vf[(uid, int(current.revision))]):
                rev, basis = int(current.revision) + 1, "CORRECTION"
            else:
                batch.quarantine("RESULT", oid, row, "RESULT_CONFLICT: differs from the effective revision; "
                                                     "only a later reviewed WEB_CORRECTED observation revises it")
                continue
            if basis != "CORROBORATING":
                record = dict(event_uid=uid, revision=str(rev), revision_basis=basis, ingest_seq=seq, **values)
                batch.new["RESULTS.csv"].append(record)
                revisions.append(SimpleNamespace(**record))
                batch.counts["new_results" if basis == "FIRST_OBSERVED" else "corrections"] += 1
                vf[(uid, rev)] = p.clock(row["known_at"])
            else:
                batch.counts["corroborating"] += 1
                vf[(uid, rev)] = min(vf.get((uid, rev), p.clock(row["known_at"])), p.clock(row["known_at"]))
            batch.observe("RESULT", oid, uid, rev, basis, row)

    stats_now = store.team_game_stats
    stat_rev = {}
    for r in stats_now.itertuples():
        key = (r.event_uid, r.team, r.stat)
        if key not in stat_rev or int(r.revision) > stat_rev[key][0]:
            stat_rev[key] = (int(r.revision), r.value)
    for row in sorted(data["TEAM_GAME_STATS.csv"], key=lambda r: (r.get("known_at", ""), _row_digest(r, STAT_FIELDS))):
        oid = _row_digest(row, STAT_FIELDS)
        if oid in batch.seen_obs:
            batch.counts["exact_duplicates"] += 1
            continue
        batch.seen_obs.add(oid)
        batch.counts["observations"] += 1
        try:
            _check_source(row)
            stat = row["stat"].strip().upper()
            if not stat.replace("_", "").isalnum():
                raise p.AdmissionError("statistic names are upper-case tokens")
            value = float(row["value"])
            if not math.isfinite(value) or value < 0:
                raise p.AdmissionError("team statistics must be finite and nonnegative")
            events = batch.events()
            hit = events[(events.competition == row["competition"]) & (events.native_event_id == row["native_event_id"])]
            if hit.empty:
                raise p.AdmissionError("EVENT_UNKNOWN: ingest the game observation before its statistics")
            ev = hit.iloc[0]
            if row["team"] not in (ev.home, ev.away):
                raise p.AdmissionError("statistic team is not a participant")
            key = (ev.event_uid, row["team"], stat)
            value_text = repr(value)
            if key not in stat_rev:
                rev, basis = 1, "FIRST_OBSERVED"
            elif stat_rev[key][1] == value_text:
                rev, basis = stat_rev[key][0], "CORROBORATING"
            elif row["source_kind"] == "WEB_CORRECTED":
                rev, basis = stat_rev[key][0] + 1, "CORRECTION"
            else:
                raise p.AdmissionError("STAT_CONFLICT: differs from the stored value without a reviewed correction")
            if basis != "CORROBORATING":
                batch.new["TEAM_GAME_STATS.csv"].append(dict(event_uid=ev.event_uid, team=row["team"], stat=stat,
                                                             revision=str(rev), value=value_text, ingest_seq=seq))
                stat_rev[key] = (rev, value_text)
            batch.observe("TEAM_STAT", oid, ev.event_uid, f"{ev.event_uid}|{row['team']}|{stat}|{rev}", basis, row)
        except (p.AdmissionError, ValueError, KeyError) as e:
            batch.quarantine("TEAM_STAT", oid, row, str(e))

    for row in data["AVAILABILITY.csv"]:
        oid = _row_digest(row, AVAIL_FIELDS)
        if oid in batch.seen_obs:
            batch.counts["exact_duplicates"] += 1
            continue
        batch.seen_obs.add(oid)
        batch.counts["observations"] += 1
        try:
            _check_source(dict(row, source_kind="WEB_RECOVERED"), require_kind=False)
            if not row["published_at"].strip():
                raise p.AdmissionError("KNOWN_AT_MISSING: availability without a publication time cannot be dated")
            if p.clock(row["known_at"]) < p.clock(row["published_at"]):
                raise p.AdmissionError("availability known before publication")
            if row["role"] not in AVAIL_ROLES or row["status"] not in AVAIL_STATUSES or row["confirmation"] not in AVAIL_CONFIRMATIONS:
                raise p.AdmissionError("unknown availability role/status/confirmation")
            if not row["player"].strip():
                raise p.AdmissionError("player identity required")
            events = batch.events()
            hit = events[(events.competition == row["competition"]) & (events.native_event_id == row["native_event_id"])]
            if hit.empty:
                raise p.AdmissionError("EVENT_UNKNOWN: register TARGET_EVENT before availability")
            ev = hit.iloc[0]
            if row["team"] not in (ev.home, ev.away):
                raise p.AdmissionError("availability team is not a participant")
            batch.new["PLAYER_AVAILABILITY.csv"].append(dict(
                event_uid=ev.event_uid, team=row["team"], player=row["player"].strip(), role=row["role"],
                status=row["status"], confirmation=row["confirmation"], known_at=_iso(row["known_at"]),
                observation_id=oid, ingest_seq=seq))
            batch.observe("AVAILABILITY", oid, ev.event_uid, "", "SNAPSHOT", dict(row, source_kind="WEB_RECOVERED"))
        except (p.AdmissionError, ValueError, KeyError) as e:
            batch.quarantine("AVAILABILITY", oid, row, str(e))

    receipt = dict(ingest_seq=seq, ingested_at=_now(), export_path=str(Path(export)), export_sha256=export_digest(export),
                   schema_version=SCHEMA_VERSION, code_sha256=code, **batch.counts)
    if dry_run:
        return receipt
    if p.source_hash() != code:
        raise p.AdmissionError("generating source changed during ingest")
    store_root.mkdir(parents=True, exist_ok=True)
    for name, fields in STORE_FILES.items():
        if name == "INGEST_RECEIPTS.csv":
            continue
        _append(store_root / name, fields, batch.new[name])
    _append(store_root / "INGEST_RECEIPTS.csv", STORE_FILES["INGEST_RECEIPTS.csv"], [receipt])  # commit marker last
    return receipt


def _append(path: Path, fields, rows: list[dict]) -> None:
    exists = path.exists()
    if not rows and exists:
        return
    s = io.StringIO(newline="")
    w = csv.DictWriter(s, fieldnames=list(fields), lineterminator="\n")
    if not exists:
        w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in fields})
    with path.open("a", encoding="utf-8", newline="") as f:
        f.write(s.getvalue())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("add", help="append one research export to the store")
    a.add_argument("--export", type=Path, required=True)
    a.add_argument("--store", type=Path, required=True)
    a.add_argument("--dry-run", action="store_true")
    h = sub.add_parser("history", help="write primary HISTORY.csv rows known by the horizon")
    h.add_argument("--store", type=Path, required=True)
    for name in ("competition", "endpoint", "horizon"):
        h.add_argument("--" + name, required=True)
    h.add_argument("--exclude-event", default="")
    h.add_argument("--out", type=Path, required=True)
    s = sub.add_parser("summary")
    s.add_argument("--store", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == "add":
        rec = ingest(args.export, args.store, dry_run=args.dry_run)
        print(";".join(f"{k}={v}" for k, v in rec.items() if k not in ("code_sha256",)))
    elif args.command == "history":
        rows = history_rows(load_store(args.store), args.competition, args.endpoint, args.horizon, args.exclude_event)
        with args.out.open("xb") as f:
            f.write(p.csv_bytes(rows))
        print(f"{len(rows)} admitted history rows -> {args.out}")
    else:
        st = load_store(args.store)
        res = effective_results(st)
        print(f"view {st.view_seq}: events={len(st.events)} results={len(res)} "
              f"observations={len(st.source_observations)} quarantined={len(st.quarantine)} digest={store_digest(st)}")


if __name__ == "__main__":
    main()

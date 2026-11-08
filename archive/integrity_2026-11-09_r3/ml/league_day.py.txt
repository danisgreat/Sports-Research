"""Full-league pregame lane: freeze every fixture of a day, whether or not a card is requested (REV-06).

A model lane judged only on carded games would need years to answer; a full-league lane answers within a season. For one
competition and one date this command reads the day's fixtures from the ESPN scoreboard, and for every game that has not
started it:

  1. freezes the competition's active release (the fitted model, CANDIDATE) and the league baseline (CHAMPION) through the
     same cycle execution a card uses (``ml.pregame``), on two contracts: the home winner and the total at the league median;
  2. freezes the declared reference (TB-2-MD from the day's ESPN standings) on the same contracts as the champion
     ``TB2_MD_REFERENCE``, so the fitted model, the simple reference and the baseline are compared on identical rows.

    python -m ml league-day freeze --competition "Basketball/NBA" --date 2026-10-22 --cache <folder outside the repository> \
        --confirm-no-outcome-seen
    python -m ml league-day settle --competition "Basketball/NBA" --date 2026-10-22 --cache <folder outside the repository>

``settle`` (a day or two later) ingests that date's finals through the two-lineage backfill (ESPN and Basketball-Reference must agree) and
runs ``cycle settle`` for every frozen bundle of the date, writing ``research/cycle_feedback/<key>_REV1``; ``pregame status`` and
``pregame compare-card`` then count the settled, paired events.

Commit and push before the first tip-off: only the pushed commit makes the freeze externally checkable. Nothing here reads a
price or a line; the total is set from the competition's own verified mean. No automation is scheduled (CURRENT_RULES R38):
the operator or prompt 1 runs this each day.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import math
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from ml import backfill_basketball as BB, chat, pregame, reference as R

ROOT = Path(__file__).resolve().parents[1]
ESPN_SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/{slug}/scoreboard?dates={d}&limit=100"
SLUGS = {"Basketball/NBA": "basketball/nba"}
MIN_LEAD_MINUTES = 5


class LeagueDayError(ValueError):
    pass


def total_line(competition: str, root=ROOT) -> float:
    """The league's own verified mean total, rounded to the nearest half point below it (a no-push line near the median)."""
    row = R.parameter_row(competition, root)
    if not row:
        raise LeagueDayError(f"no parameter row for {competition}")
    mean = float(row["store_mean_total"] or row["mean_total"])
    return math.floor(mean) + 0.5


def fixtures(competition: str, date: str, cache: Path, now=None) -> list[dict]:
    if competition not in SLUGS:
        raise LeagueDayError(f"{competition}: no scoreboard slug mapped")
    url = ESPN_SCOREBOARD.format(slug=SLUGS[competition], d=date.replace("-", ""))
    raw, receipt = BB.fetch(url, Path(cache), ".json")
    if receipt["error"]:
        raise LeagueDayError("scoreboard unreachable: " + receipt["error"])
    now = now or datetime.now(timezone.utc)
    out = []
    for ev in json.loads(raw)["events"]:
        start = datetime.fromisoformat(ev["date"].replace("Z", "+00:00"))
        co = ev["competitions"][0]
        sides = {c["homeAway"]: c for c in co["competitors"]}
        out.append(dict(event_id=str(ev["id"]), start=start, state=ev["status"]["type"]["state"], season_type=ev["season"]["type"],
                        season=str(int(ev["season"]["year"]) - 1), home=BB.display(sides["home"]["team"]["displayName"]),
                        away=BB.display(sides["away"]["team"]["displayName"]), venue=co.get("venue", {}).get("fullName", ""),
                        source_url=url, receipt=receipt, open=ev["status"]["type"]["state"] == "pre" and (start - now).total_seconds() > MIN_LEAD_MINUTES * 60))
    return out


def run(competition: str, date: str, cache: Path, *, confirmed: bool = False, root=ROOT, ledger=chat.LEDGER, now=None) -> list[dict]:
    if not confirmed:
        raise LeagueDayError("pass --confirm-no-outcome-seen only if no live score or result of these games was opened")
    root = Path(root).resolve()
    tier = R.tier(competition, root)
    if tier["tier"] != "A":
        raise LeagueDayError(f"{competition} has no active release; a league-day lane needs one")
    line = total_line(competition, root)
    slate = fixtures(competition, date, cache, now)
    results = []
    stamp = (now or datetime.now(timezone.utc)).strftime("%Y%m%d")
    n = 0
    for fx in slate:
        if not fx["open"] or fx["season_type"] != 2:
            results.append(dict(event_id=fx["event_id"], status="SKIPPED", reason="started, finished or not a regular-season fixture"))
            continue
        n += 1
        key = f"LOCAL-LEAGUE-{R.league_key(competition) or 'X'}-{date.replace('-', '')}-G{n:04d}"
        label_total = f"OVER_{line}"
        lines = [dict(label="HOME_ML", family="winner", side="HOME", line=""), dict(label=label_total, family="total", side="OVER", line=str(line))]
        game = dict(local_key=key, competition=competition, native_event_id="ESPN:" + fx["event_id"], season=fx["season"],
                    scheduled_start=fx["start"].isoformat(), home=fx["home"], away=fx["away"], venue=fx["venue"], source_url=fx["source_url"])
        with tempfile.TemporaryDirectory(prefix="sr_leagueday_") as tmp:
            tmp = Path(tmp)
            (tmp / "GAME.csv").write_bytes(chat._csv([game], chat.GAME_FIELDS))
            (tmp / "LINES.csv").write_bytes(chat._csv(lines, chat.LINE_FIELDS))
            (tmp / "fixture.txt").write_text(
                f"ESPN scoreboard {date} event {fx['event_id']}: {fx['away']} at {fx['home']}, {fx['venue']}, scheduled {fx['start'].isoformat()}, "
                f"state pre; raw body sha256 {fx['receipt']['raw_sha256']} retrieved {fx['receipt']['retrieved_at']}\n", encoding="utf-8")
            model = pregame.reference(tmp / "GAME.csv", tmp / "LINES.csv", tmp / "fixture.txt", confirmed=True, root=root, ledger=ledger)
            row = dict(event_id=fx["event_id"], local_key=key, home=fx["home"], away=fx["away"], start=fx["start"].isoformat(),
                       model_status=model["status"], reason=model["reason"], reference_status="", reference_p_home="", reference_p_over="")
            if model["status"] == "EXECUTED":
                try:
                    data, _ = R.standings_csv(competition, fx["home"], fx["away"], cache)
                    (tmp / "STANDINGS.csv").write_bytes(data)
                    ref = R.run(tmp / "GAME.csv", tmp / "LINES.csv", tmp / "STANDINGS.csv", confirmed=True, root=root, now=now)
                    R.write_receipt(ref, root)
                    probs = {r["label"]: str(r["p_decisive"]) for r in ref["rows"]}
                    from ml.evaluation import prospective
                    attempt = root / model["attempt_path"]
                    clock = datetime.now(timezone.utc).isoformat()
                    rows = pregame.card_rows(attempt, {k: (v, "") for k, v in probs.items()}, clock, champion="TB2")
                    prospective.freeze(root / ledger, rows, now=clock)
                    row.update(reference_status="EXECUTED:" + ref["reference_id"], reference_p_home=probs.get("HOME_ML", ""),
                               reference_p_over=probs.get(label_total, ""))
                except (R.ReferenceError_, KeyError, ValueError) as exc:
                    row.update(reference_status="NOT_RUN:" + str(exc)[:120])
        results.append(row)
    return results


def settle_day(competition: str, date: str, cache: Path, *, root=ROOT, backfill=None, settle=None) -> list[dict]:
    """Ingest the day's finals (two lineages) and settle every frozen bundle of the date. Idempotent per local key."""
    root = Path(root).resolve()
    league = {v["competition"]: k for k, v in BB.LEAGUES.items()}.get(competition)
    if league is None:
        raise LeagueDayError(f"{competition}: no two-lineage backfill is mapped")
    stem = f"LOCAL-LEAGUE-{R.league_key(competition) or 'X'}-{date.replace('-', '')}-G"
    attempts = sorted((root / chat.ATTEMPTS).glob(stem + "????")) if (root / chat.ATTEMPTS).is_dir() else []
    todo = [a for a in attempts if not (root / chat.FEEDBACK / (a.name + "_REV1")).exists()]
    if not todo:
        return [dict(local_key=a.name, status="ALREADY_SETTLED" if attempts else "NO_FROZEN_BUNDLES") for a in attempts] or [dict(local_key=stem + "*", status="NO_FROZEN_BUNDLES")]
    backfill = backfill or BB.run
    if settle is None:
        from ml import cycle
        settle = cycle.settle
    out = root / "research" / "league_day" / date / "FINALS"
    ingest = backfill(league, date, date, Path(cache), out, root / chat.STORE)
    rows = [dict(local_key="(finals)", status="INGESTED", detail=str({k: ingest[k] for k in ("verified", "not_ingested", "owner_games") if k in ingest}))]
    for attempt in todo:
        bundle = sorted(attempt.glob("ATTEMPT_*"))[-1] / "BUNDLE"
        try:
            settle(bundle, out / "EXPORT", root / chat.STORE, root / chat.FEEDBACK / (attempt.name + "_REV1"))
            rows.append(dict(local_key=attempt.name, status="SETTLED", detail=""))
        except Exception as exc:    # a missing or unverified final is recorded; the bundle stays open for a later attempt
            rows.append(dict(local_key=attempt.name, status="NOT_SETTLED", detail=f"{type(exc).__name__}: {str(exc)[:160]}"))
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("freeze", "settle"):
        s = sub.add_parser(name)
        s.add_argument("--competition", required=True)
        s.add_argument("--date", required=True, help="US local date of the fixtures, YYYY-MM-DD")
        s.add_argument("--cache", type=Path, required=True, help="folder OUTSIDE the repository for raw feed bodies")
        if name == "freeze":
            s.add_argument("--confirm-no-outcome-seen", action="store_true")
    args = parser.parse_args(argv)
    if Path.cwd().resolve() != ROOT:
        print("REFUSED: run from the repository root")
        raise SystemExit(2)
    try:
        if args.command == "freeze":
            rows = run(args.competition, args.date, args.cache, confirmed=args.confirm_no_outcome_seen)
        else:
            rows = settle_day(args.competition, args.date, args.cache)
    except (LeagueDayError, pregame.PregameError, chat.ChatError) as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)
    for r in rows:
        print(" ".join(f"{k}={v}" for k, v in r.items() if v != ""))
    if args.command == "freeze":
        print(f"{sum(1 for r in rows if r.get('model_status') == 'EXECUTED')} game(s) frozen. Commit and push before the first tip-off.")


if __name__ == "__main__":
    main()

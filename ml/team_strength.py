"""Recent-team starting centres (TEAM-CENTRE-v1), shadow candidates until prospectively qualified.

One fixed recipe: last 20 exact-competition games, rates shrunk by five games to
the league's earlier mean, then average own attack and opponent defence. A centre
is not a calibrated distribution. Cricket uses conditional first-innings batting
and bowling rates. No unsupported sport is assigned a proxy or invented history.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
from pathlib import Path
import statistics

from ml import research_intake as I

VERSION = "TEAM-CENTRE-v1"
WINDOW, SHRINK = 20, 5
SPORTS = ("Basketball", "Soccer", "Cricket", "Tennis", "Ice Hockey", "Baseball", "AFL",
          "Rugby League", "Rugby Union", "American Football")


def split(competition):
    return "TUNE" if int(hashlib.sha256(competition.encode()).hexdigest(), 16) % 2 == 0 else "HELD_OUT"


def history(root=I.ROOT):
    """Normalized sporting outcomes only. Current capture never becomes historical known-at proof."""
    root = Path(root); rows = []; inputs = []
    path = root / "research/bulk_history/soccer/MATCHES.csv"
    if path.exists():
        inputs.append(path)
        for r in I.read(path):
            rows.append(dict(competition=r["competition"], date=r["date"], home=r["home"], away=r["away"],
                             hs=float(r["ft_home"]), as_=float(r["ft_away"]), endpoint="REGULATION", kind="MATCH", event_id=r["source_url"] + ":" + r["date"] + ":" + r["home"]))
    events = root / "research/learning_store/EVENTS.csv"; results = events.with_name("RESULTS.csv")
    if events.exists() and results.exists():
        inputs += [events, results]; outcomes = {}
        for r in I.read(results):
            old = outcomes.get(r["event_uid"])
            if not old or int(r["revision"]) > int(old["revision"]): outcomes[r["event_uid"]] = r
        for e in I.read(events):
            r = outcomes.get(e["event_uid"])
            if not r or r["status"] != "FINAL" or not r["hs"] or not r["as_"]: continue
            rows.append(dict(competition=e["competition"], date=e["event_at"][:10], home=e["home"], away=e["away"],
                             hs=float(r["hs"]), as_=float(r["as_"]), endpoint=e["endpoint"], kind="MATCH", event_id=e["event_uid"]))
    path = root / "research/bulk_history/cricket/v24.15/INNINGS.csv"
    if path.exists():
        inputs.append(path)
        for r in I.read(path):
            if r["innings"] != "1" or r["reduced"] != "N" or r["result_type"] == "no_result": continue
            rows.append(dict(competition=r["competition"], date=r["start_date"], home=r["batting_team"], away=r["bowling_team"],
                             hs=float(r["runs"]), as_=0.0, endpoint="FIRST_INNINGS", kind="INNINGS", event_id="CRICSHEET:" + r["match_id"]))
    keys = [(r["competition"], r["event_id"], r["endpoint"]) for r in rows]
    if len(keys) != len(set(keys)): raise ValueError("duplicate history event/endpoint; reconcile before calculating centres")
    return rows, inputs


def centre(rows, competition, home, away, as_of, *, endpoint=None):
    if home == away: raise ValueError("distinct participants required")
    horizon = I.clock(as_of).date().isoformat()
    prior = [r for r in rows if r["competition"] == competition and r["date"] < horizon and (not endpoint or r["endpoint"] == endpoint)]
    if not prior: raise ValueError("NO_EXACT_COMPETITION_HISTORY")
    if len({(r["kind"], r["endpoint"]) for r in prior}) != 1: raise ValueError("mixed innings/match endpoints require exact endpoint selection")
    prior.sort(key=lambda r: (r["date"], r["event_id"]))
    innings = prior[0]["kind"] == "INNINGS"
    league = statistics.mean([r["hs"] for r in prior] if innings else [s for r in prior for s in (r["hs"], r["as_"])])
    if innings:
        bat = [r["hs"] for r in prior if r["home"] == home][-WINDOW:]
        bowl = [r["hs"] for r in prior if r["away"] == away][-WINDOW:]
        if not bat or not bowl: raise ValueError("MISSING_EXACT_BATTING_OR_BOWLING_HISTORY")
        shrink = lambda v: (sum(v) + SHRINK * league) / (len(v) + SHRINK)
        return dict(competition=competition, home=home, away=away, as_of=as_of, endpoint=prior[0]["endpoint"],
                    home_n=len(bat), away_n=len(bowl), league_n=len(prior), mean_home=(shrink(bat) + shrink(bowl)) / 2,
                    mean_away="", total="", margin="", league_total=league, league_margin="",
                    status="SHADOW_ONLY_UNCALIBRATED_CONDITIONAL_FIRST_INNINGS", recipe=VERSION)
    def rates(team):
        games = [r for r in prior if team in (r["home"], r["away"])][-WINDOW:]
        if not games: raise ValueError("MISSING_TEAM_HISTORY")
        attack = sum(r["hs"] if r["home"] == team else r["as_"] for r in games)
        defence = sum(r["as_"] if r["home"] == team else r["hs"] for r in games)
        n = len(games)
        return (attack + SHRINK * league) / (n + SHRINK), (defence + SHRINK * league) / (n + SHRINK), n
    ha, hd, hn = rates(home); aa, ad, an = rates(away)
    # Home edge shrinks toward zero using ONLY this competition's earlier results.
    edge = sum(r["hs"] - r["as_"] for r in prior) / (len(prior) + 50)
    mh, ma = max(0.01, (ha + ad) / 2 + edge / 2), max(0.01, (aa + hd) / 2 - edge / 2)
    return dict(competition=competition, home=home, away=away, as_of=as_of, endpoint=prior[0]["endpoint"],
                home_n=hn, away_n=an, league_n=len(prior), mean_home=mh, mean_away=ma, total=mh + ma, margin=mh - ma,
                league_total=2 * league, league_margin=edge, status="SHADOW_ONLY_UNCALIBRATED", recipe=VERSION)


def study(out, *, root=I.ROOT):
    rows, inputs = history(root); by = defaultdict(list)
    for r in rows: by[(r["competition"], r["endpoint"])].append(r)
    predictions, summary = [], []
    for (competition, endpoint), games in sorted(by.items()):
        ordered = sorted(games, key=lambda r: (r["date"], r["event_id"]))
        # The last 200 per competition bound runtime; all earlier games remain available as training history.
        # No constants are selected on these labels. Same-day scores are excluded from every prediction.
        for g in ordered[-200:]:
            try: c = centre(ordered, competition, g["home"], g["away"], g["date"] + "T00:00:00+00:00", endpoint=endpoint)
            except ValueError: continue
            if min(c["home_n"], c["away_n"]) < 3 or c["league_n"] < 30: continue
            target = g["hs"] if g["kind"] == "INNINGS" else g["hs"] + g["as_"]
            prediction = c["mean_home"] if g["kind"] == "INNINGS" else c["total"]
            predictions.append(dict(competition=competition, sport="Cricket" if competition.startswith("Cricket") else competition.split("/")[0], endpoint=endpoint,
                                    event_id=g["event_id"], date=g["date"], split=split(competition), target=target, prediction=prediction,
                                    league_prediction=c["league_total"], error=prediction - target, baseline_error=c["league_total"] - target))
        local = [r for r in predictions if r["competition"] == competition and r["endpoint"] == endpoint]
        summary.append(dict(competition=competition, sport="Cricket" if competition.startswith("Cricket") else competition.split("/")[0], endpoint=endpoint, split=split(competition), n=len(local),
                            mae=statistics.mean(abs(r["error"]) for r in local) if local else "",
                            baseline_mae=statistics.mean(abs(r["baseline_error"]) for r in local) if local else "",
                            status="RETROSPECTIVE_DIAGNOSTIC_NOT_PREGAME_PROOF", qualification="NOT_PROMOTED"))
    coverage = []
    for sport in SPORTS:
        group = [r for r in summary if r["sport"] == sport and r["n"]]
        held = {r["competition"] for r in group if r["split"] == "HELD_OUT"}
        others = {r["competition"] for r in group if r["split"] == "TUNE"}
        coverage.append(dict(sport=sport, competitions=len(group), held_out_competitions=len(held), other_competitions=len(others),
                             status="HELD_OUT_COMPETITION_DIAGNOSTIC" if held and others else "NO_CROSS_COMPETITION_VALIDATION" if group else "NO_SUPPORTED_HISTORY",
                             primary_use="NOT_AUTHORIZED_SHADOW_ONLY"))
    out = Path(out); out.mkdir(parents=True, exist_ok=False)
    for name, data, empty in (("PREDICTIONS.csv", predictions, "event_id"), ("COMPETITIONS.csv", summary, "competition"), ("SPORT_COVERAGE.csv", coverage, "sport")):
        (out / name).write_bytes(I.csv_bytes(tuple(data[0]) if data else (empty,), data))
    receipts = [dict(path=p.relative_to(Path(root)).as_posix(), sha256=I.sha(p.read_bytes())) for p in inputs]
    (out / "INPUTS.csv").write_bytes(I.csv_bytes(("path", "sha256"), receipts))
    receipt = dict(recipe=VERSION, code_sha256=I.sha(Path(__file__).read_bytes()), run_at=I.now(), last_n=WINDOW, shrink_games=SHRINK,
                   evaluation="FIXED_RECIPE_LAST_200_PER_COMPETITION_STRICT_PRIOR_DATES", qualification="SHADOW_ONLY_NO_PROMOTION")
    (out / "RECEIPT.csv").write_bytes(I.csv_bytes(tuple(receipt), [receipt]))
    (out / "README.md").write_text("# Recent-team centre study\n\nFixed recipe, no tuning on reported outcomes. Competition split is a deterministic SHA-256 split. "
        "Each forecast uses strictly earlier dates from its own competition and exact endpoint; same-day games are excluded. "
        "Last 200 games per competition are an explicit bounded diagnostic sample, not prospective validation. "
        "Inputs were captured after historical outcomes. No historical availability/publication proof is inferred. "
        "MAE evaluates a starting centre only; it does not validate probabilities, uncertainty, player effects or profitability. "
        "Sports lacking multiple competitions or permitted history retain those limits. No candidate is promoted.\n", encoding="utf-8")
    return coverage


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__); sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("study"); s.add_argument("--out", type=Path, required=True)
    c = sub.add_parser("centre")
    for f in ("competition", "home", "away", "as-of"): c.add_argument("--" + f, required=True)
    c.add_argument("--endpoint"); c.add_argument("--out", type=Path, required=True)
    args = p.parse_args(argv)
    try:
        if args.command == "study": print(study(args.out))
        else:
            if I.clock(args.as_of) < I.clock(I.now()): raise ValueError("current-capture history cannot supply a historical known-at forecast")
            rows, inputs = history(); result = centre(rows, args.competition, args.home, args.away, args.as_of, endpoint=args.endpoint)
            args.out.mkdir(parents=True, exist_ok=False)
            (args.out / "CENTRE.csv").write_bytes(I.csv_bytes(tuple(result), [result]))
            receipt = dict(run_at=I.now(), code_sha256=I.sha(Path(__file__).read_bytes()), input_sha256=I.sha(b"".join(p.read_bytes() for p in inputs)),
                           status="SHADOW_ONLY_NOT_A_PRIMARY_PROBABILITY")
            (args.out / "RECEIPT.csv").write_bytes(I.csv_bytes(tuple(receipt), [receipt])); print(result)
    except (ValueError, OSError, KeyError) as exc: raise SystemExit(str(exc)) from exc

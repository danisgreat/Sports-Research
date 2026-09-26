#!/usr/bin/env python3
"""Model reference registry and query tool (C-MODEL-ANCHOR; added 2026-09-26(e)).

What it records. For every league and target (side, total), which numerical model has earned the right to be
the reference: tools/sport_models.py A1, tools/mlb_model.py A1S (MLB totals) or tools/team_baseline.py TB-1,
or none (POP = the population, BASELINE_P). The registry is DERIVED, not chosen. EVIDENCE holds the held-out
comparisons (95% intervals) from the research folders, and `select()` applies the rule preregistered in
research/predictability_2026-09-26/PREREGISTRATION.md P4:
  the reference for a (league, target) is the first of [A1S (MLB), A1, TB-1] that beat the population (A0)
  with a 95% interval below 0 on that target. If A1 and TB-1 both qualify, A1 is chosen only if it also beat
  TB-1 with its interval below 0; otherwise TB-1, the incumbent. If none qualifies, the reference is POP.
Targets: "side" (result, moneyline and handicaps, scored on result Brier) and "total" (scored at a line).

What it is for (STATUS "REFERENCE").
- It names the model each league's shadow lane is reviewed against (C-SPORT-SHADOW, C-MLB-SHADOW).
- It is the source of the predictability map (BASE_RATES_REGISTER.md §7.8).
It is NOT a card input: its probabilities are never printed on, cited by or used to revise a card.

Why it is not a card anchor. The same preregistration (P3) compared the cards' own probabilities with these
models on 98 contracts from 54 settled cards. The cards scored 0.2438 against A1's 0.2505, with no demonstrated
difference [-0.025, +0.011]. Forcing cards onto the model would not have improved the record. STATUS becomes
"ACTIVE" (a card anchor) only on the user's explicit instruction, as a MODEL_CHANGE under C-RULE-FREEZE, after
the shadow-lane review shows the model beating the cards on shared rows.
No odds, lines or prices are read.

Commands:
    python tools/model_anchor.py registry                 # the derived table, with the evidence behind it
    python tools/model_anchor.py anchor --league nba --home "Boston Celtics" --away "Miami Heat" \\
        --date 2026-11-02 --total 221.5 --line -4.5 [--csv results.csv] [--neutral]   # research use only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

STATUS = "REFERENCE"   # not a card input; "ACTIVE" only on the user's explicit instruction (MODEL_CHANGE)

# Held-out evidence, one entry per (league, target, model): Brier difference against A0 (the population)
# and, for A1, against TB-1, each with its 95% block-bootstrap interval. Sources:
#   S1 research/sport_models_2026-09-26/README.md (rolling origin, public results)
#   S2 research/predictability_2026-09-26/p2_coverage_results.json (NBL, NRL)
#   S3 research/predictability_2026-09-26/p4_tb1_intervals.json (TB-1 v its running base rate, latest season)
#   S4 research/predictability_2026-09-26/mlb_starters_results.json (MLB 2025 and 2026; A1 team-only)
# None: no held-out comparison exists. Intervals are [low, high] of (model − reference); below 0 = better.
EVIDENCE = {
    "epl":        {"side":  {"A1": [-0.0397, -0.0241], "A1vTB1": [-0.0133, -0.0026], "TB1": [-0.02393, -0.00734]},
                   "total": {"A1": [-0.0050, 0.0045], "A1vTB1": [-0.0057, 0.0032], "TB1": [0.00252, 0.01467]}},
    "laliga":     {"side":  {"A1": [-0.0401, -0.0260], "A1vTB1": None, "TB1": None},
                   "total": {"A1": [-0.0135, -0.0006], "A1vTB1": None, "TB1": None}},
    "bundesliga": {"side":  {"A1": [-0.0400, -0.0225], "A1vTB1": None, "TB1": None},
                   "total": {"A1": [-0.0125, -0.0007], "A1vTB1": None, "TB1": None}},
    "seriea":     {"side":  {"A1": [-0.0394, -0.0244], "A1vTB1": None, "TB1": None},
                   "total": {"A1": [-0.0053, 0.0053], "A1vTB1": None, "TB1": None}},
    "ligue1":     {"side":  {"A1": [-0.0338, -0.0196], "A1vTB1": None, "TB1": None},
                   "total": {"A1": [-0.0050, 0.0056], "A1vTB1": None, "TB1": None}},
    "nfl":        {"side":  {"A1": [-0.0277, -0.0148], "A1vTB1": [-0.0105, 0.0008], "TB1": [-0.02941, -0.01217]},
                   "total": {"A1": [-0.0084, 0.0034], "A1vTB1": [-0.0054, 0.0042], "TB1": [-0.01844, 0.00173]}},
    "afl":        {"side":  {"A1": [-0.0462, -0.0257], "A1vTB1": [-0.0183, -0.0048], "TB1": [-0.06384, -0.02924]},
                   "total": {"A1": [-0.0097, 0.0017], "A1vTB1": [-0.0002, 0.0177], "TB1": [-0.02013, 0.00856]}},
    "nba":        {"side":  {"A1": [-0.0418, -0.0321], "A1vTB1": [-0.0106, -0.0054], "TB1": [-0.04067, -0.02308]},
                   "total": {"A1": [-0.0245, -0.0164], "A1vTB1": [-0.0077, -0.0032], "TB1": [-0.01812, 0.00054]}},
    "wnba":       {"side":  {"A1": [-0.0457, -0.0297], "A1vTB1": [-0.0112, -0.0035], "TB1": [-0.05181, -0.03037]},
                   "total": {"A1": [-0.0231, -0.0100], "A1vTB1": [-0.0101, -0.0028], "TB1": [-0.03742, -0.01371]}},
    "nbl":        {"side":  {"A1": [-0.0578, -0.0201], "A1vTB1": [-0.0245, -0.0018], "TB1": [-0.04604, -0.01434]},
                   "total": {"A1": [-0.0402, -0.0078], "A1vTB1": [-0.0184, 0.0049], "TB1": [-0.01652, 0.0084]}},
    "nhl":        {"side":  {"A1": [-0.0107, -0.0042], "A1vTB1": [-0.0056, -0.0004], "TB1": [-0.00469, -0.00065]},
                   "total": {"A1": [-0.0004, 0.0033], "A1vTB1": [0.0003, 0.0030], "TB1": [-0.00292, 0.00091]}},
    "nrl":        {"side":  {"A1": [-0.0273, 0.0003], "A1vTB1": [-0.0180, 0.0029], "TB1": [-0.02939, 0.00442]},
                   "total": {"A1": [-0.0018, 0.0218], "A1vTB1": [-0.0054, 0.0180], "TB1": [-0.01148, 0.00489]}},
    # MLB (S4): side on 2025, the independent season for A1 v2 (2026 A1: -0.00542, +0.00002; TB-1 2026: -0.00432,
    # -0.00028); total at 8.5 on 2026, where the starter model A1S was tested (2025 A1S: -0.00433, +0.00164).
    "mlb":        {"side":  {"A1S": None, "A1": [-0.00784, -0.00103], "A1vTB1": [-0.00098, 0.00135],
                             "TB1": [-0.00732, -0.00206]},
                   "total": {"A1S": [-0.00646, -0.00016], "A1": [-0.00377, 0.00074], "A1vTB1": None,
                             "TB1": [-0.00241, 0.00051]}},
    "atp":        {"side":  {"A1": [-0.0033, -0.0001], "A1vTB1": None, "TB1": None},
                   "total": {"A1": None, "A1vTB1": None, "TB1": None}},
}
# Notes that travel with a registry row (disclosures the rule itself does not capture).
NOTES = {
    ("nbl", "side"): "2025-26 window; the 2024-25 window was not significant (-0.0368, +0.0058).",
    ("nbl", "total"): "2024-25 window; the 2025-26 window was not significant (-0.0251, +0.0136).",
    ("mlb", "side"): "A1 and TB-1 both beat A0 (2025) and are not separated, so the incumbent TB-1 stands. "
                     "Gains are small (win Brier 0.246 v 0.250).",
    ("mlb", "total"): "A1S (tools/mlb_model.py with probable starters) beat A0 at 7.5, 8.5 and 9.5 in 2026 but not in "
                      "2025; the starter term's preregistered result test failed (P1). Query with mlb_model.py predict "
                      "--home-sp/--away-sp.",
    ("atp", "total"): "The v2 games route was re-selected after a v1 failure on its own test window (not independent).",
    ("nhl", "total"): "A1 totals were significantly WORSE than the population.",
    ("epl", "total"): "TB-1 totals were significantly WORSE than the population.",
    ("nfl", "side"): "A1 v TB-1 not separated; A1 point estimate ahead by 0.005.",
    ("laliga", "side"): "No TB-1 for this league; A1 beat A0.",
    ("nba", "side"): "A1 v TB-1 from 2023-26; TB-1 k chosen on the same season (helps TB-1).",
}
COVERED_NO_EVIDENCE = ["championship", "eredivisie", "primeira", "spl", "aleague", "mls", "jleague", "ucl", "uel",
                       "ncaaf", "union", "npb", "kbo", "cpbl", "wta", "t20", "odi"]


def below0(ci) -> bool:
    return ci is not None and ci[1] < 0


def select(ev: dict) -> str:
    """The preregistered P4 rule for one (league, target) evidence entry. The candidate order is
    [A1S (MLB only), A1, TB-1]; A1S is taken first when it beat A0."""
    if below0(ev.get("A1S")):
        return "A1S"
    a1, tb1, a1v = below0(ev.get("A1")), below0(ev.get("TB1")), below0(ev.get("A1vTB1"))
    if a1 and tb1:
        return "A1" if a1v else "TB1"
    if a1:
        return "A1"
    if tb1:
        return "TB1"
    return "POP"


def registry() -> dict:
    reg = {}
    for lg, targets in EVIDENCE.items():
        reg[lg] = {t: {"anchor": select(ev), "evidence": ev, "note": NOTES.get((lg, t), "")} for t, ev in targets.items()}
    for lg in COVERED_NO_EVIDENCE:
        reg[lg] = {t: {"anchor": "POP", "evidence": None, "note": "no held-out comparison yet"} for t in ("side", "total")}
    return reg


# ---------------------------------------------------------------------------- queries


def _clip(p: float) -> float:
    return min(max(p, 1e-6), 1 - 1e-6)


def anchor_probs(league: str, home: str, away: str, date: str, total=None, line=None, neutral=False, csv=None) -> dict:
    """Probabilities from the registered anchor for each target, plus the population A0 (BASELINE_P)."""
    import sport_models as sm
    reg = registry().get(league)
    if reg is None:
        raise SystemExit(f"error: {league!r} is not in the registry; the anchor is POP (BASELINE_P)")
    out = {"league": league, "home": home, "away": away, "date": date, "status": STATUS, "rows": []}
    need_tb1 = any(v["anchor"] == "TB1" for v in reg.values())
    f0 = f1 = None
    if league != "mlb" and league != "atp":
        cfg = sm.config(league)

        class A:  # the argparse-like object sport_models.load_games expects
            pass
        a = A()
        a.csv, a.espn_path = csv, None
        games = sm.load_games(cfg, a, date)
        eng = sm.TeamEngine(cfg, [g for g in games if g["date"][:10] < date])
        import sport_data as sd
        teams = sorted({g["home"] for g in eng.games} | {g["away"] for g in eng.games})
        home, away = sd.match_name(home, teams), sd.match_name(away, teams)
        f0, f1 = eng.predict(home, away, date, neutral)
        out["home"], out["away"] = home, away
    tbr = None
    if need_tb1:
        import team_baseline as tb
        tbr = tb.predict_event(league, home, away, date, total, line, neutral)
    for target in ("side", "total"):
        model = reg[target]["anchor"]
        q = {}
        if model == "A1" and f1 is not None:
            q = f1.probs(total=total, line=line)
        elif model == "TB1" and tbr is not None:
            p = tbr["probs"]
            q = {"p_home_win": p.get("home_win"), "p_away_win": p.get("away_win"), "p_draw": p.get("draw")}
            if total is not None:
                q.update({"p_over": p.get(f"over_{total:g}"), "p_under": p.get(f"under_{total:g}")})
            if line is not None:
                q.update({"p_home_cover": p.get(f"home_{line:+g}"), "p_away_cover": p.get(f"away_{-line:+g}")})
        pop = f0.probs(total=total, line=line) if f0 is not None else {}
        keys = ("p_home_win", "p_draw", "p_away_win", "p_home_cover", "p_away_cover") if target == "side" else \
               ("p_over", "p_under", "p_push")
        for k in keys:
            if k in q and q[k] is not None or k in pop:
                out["rows"].append({"target": target, "query": k, "anchor_model": model,
                                    "anchor_p": None if model == "POP" else q.get(k),
                                    "population_p": pop.get(k), "note": reg[target]["note"]})
    return out


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("registry")
    q = sub.add_parser("anchor")
    q.add_argument("--league", required=True)
    q.add_argument("--home", required=True)
    q.add_argument("--away", required=True)
    q.add_argument("--date", required=True, help="venue-local event date; only earlier results are used")
    q.add_argument("--total", type=float)
    q.add_argument("--line", type=float, help="the home side's handicap, e.g. -4.5")
    q.add_argument("--neutral", action="store_true")
    q.add_argument("--csv", help="a local results CSV instead of the ESPN feed")
    q.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if args.cmd == "registry":
        print(f"C-MODEL-ANCHOR registry — status {STATUS} (derived by the P4 rule from EVIDENCE; not a card input)")
        print("| League | Side anchor | Total anchor | Notes |")
        print("|---|---|---|---|")
        for lg, r in registry().items():
            notes = "; ".join(x for x in (r["side"]["note"], r["total"]["note"]) if x)
            print(f"| {lg} | {r['side']['anchor']} | {r['total']['anchor']} | {notes} |")
        return 0
    if STATUS != "ACTIVE":
        print("REFERENCE — research only; never printed on, cited by or used to revise a card "
              "(C-MODEL-ANCHOR, C-RULE-FREEZE).", file=sys.stderr)
    if args.league in ("mlb", "atp"):
        raise SystemExit("MLB: use tools/team_baseline.py (TB-1 is the MLB side anchor; totals POP). "
                         "ATP: use tools/sport_models.py predict (A1 surface Elo is the winner anchor).")
    res = anchor_probs(args.league, args.home, args.away, args.date, args.total, args.line, args.neutral, args.csv)
    if args.json:
        print(json.dumps(res, indent=2))
        return 0
    print(f"ANCHOR ({res['status']}) {res['league']}: {res['away']} @ {res['home']} on {res['date']}")
    for r in res["rows"]:
        ap_ = "—" if r["anchor_p"] is None else f"{r['anchor_p']:.4f}"
        pp = "—" if r["population_p"] is None else f"{r['population_p']:.4f}"
        print(f"  {r['target']:5s} {r['query']:13s} ANCHOR_P {ap_} ({r['anchor_model']})   BASELINE_P (A0) {pp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

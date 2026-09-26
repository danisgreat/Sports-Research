#!/usr/bin/env python3
"""Print the README tables from validation_results.json. Usage: python research/sport_models_2026-09-26/report.py"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE / "validation_results.json").read_text(encoding="utf-8"))
NAMES = {"win_brier": "Result (home win) Brier", "result_rps3": "Result (3-way) RPS", "win_logloss": "Result log loss",
         "margin_rps": "Margin RPS", "total_rps": "Total RPS", "total_brier_line": "Total at fixed line (Brier)",
         "h1_total_rps": "First-half total RPS", "btts_brier": "BTTS Brier", "games_rps": "Total games RPS",
         "games_brier_line": "Total games at fixed line (Brier)", "three_sets_brier": "Three sets (Brier)"}


def verdict(d, ci):
    if ci[1] < 0:
        return "**A1 better**"
    if ci[0] > 0:
        return "**A1 worse**"
    return "no clear difference"


def table(key, res, metrics, label=None):
    print(f"\n**{label or key}** — {res['n']} forecasts, {res['from']} to {res['to']}"
          + (f"; fixed total line {res['total_line']}" if res.get("total_line") is not None else "") + "\n")
    print("| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |")
    print("|---|---:|---:|---|---|---|")
    for m in metrics:
        if m not in res:
            continue
        v = res[m]
        name = NAMES[m].replace("Result (home win)", "Winner (player A)") if "atp" in key else NAMES[m]
        tb = v.get("tb1")
        tbs = (f"{tb['a1_minus_tb1']:+.4f} ({tb['ci95_block'][0]:+.4f}, {tb['ci95_block'][1]:+.4f}), n {tb['n']}"
               if tb else "—")
        print(f"| {name} | {v['a0']:.4f} | {v['a1']:.4f} | {v['a1_minus_a0']:+.4f} ({v['ci95_block'][0]:+.4f}, "
              f"{v['ci95_block'][1]:+.4f}) | {verdict(v['a1_minus_a0'], v['ci95_block'])} | {tbs} |")


if __name__ == "__main__":
    team = ["win_brier", "result_rps3", "win_logloss", "margin_rps", "total_rps", "total_brier_line", "h1_total_rps", "btts_brier"]
    for k in ("epl", "laliga", "bundesliga", "seriea", "ligue1", "nfl", "afl", "nba"):
        table(k, R["v1"][k], team)
    team2 = team + ["reg_rps3"]
    NAMES["reg_rps3"] = "Regulation 3-way RPS"
    table("nhl (second pass, 2026-09-26(d))", R["v1"]["nhl"], team2)
    table("nba_recent (second pass; 2023-24 to 2025-26)", R["v1"]["nba_recent"], team)
    table("wnba (second pass)", R["v1"]["wnba"], team)
    table("mlb (v1, team_prior_games 20)", R["v1"]["mlb"], team)
    table("mlb v1 on the TEST window", R["v2"]["mlb_test_20"], team)
    table("mlb v2 on the TEST window (team_prior_games 120)", R["v2"]["mlb_test_120"], team)
    ten = ["win_brier", "win_logloss", "games_rps", "games_brier_line", "three_sets_brier"]
    table("atp v1 (gap_sd 0)", R["v1"]["atp"], ten)
    table("atp v2 on the same window (gap_sd 0.09)", R["v2"]["atp_test_0.09"], ten)
    cri = ["win_brier", "win_logloss", "total_rps", "total_brier_line"]
    NAMES["win_brier"] = "Result Brier"
    table("ipl v1 (elo_k 24, lam_team 6), 2016–2026", R["v1"]["ipl"], cri)
    table("ipl v1 on the TEST window", R["v2"]["ipl_test_6"], cri)
    table("ipl v2 on the TEST window (elo_k 4, lam_team 200)", R["v2"]["ipl_test_200"], cri)
    print("\nDixon–Coles candidate (soccer, A1dc − A1 on the result RPS):")
    for k in ("epl", "laliga", "bundesliga", "seriea", "ligue1"):
        x = R["v1"][k]["result_rps3"]["a1dc"]
        print(f"- {k}: {-x['a1_minus_a1dc']:+.5f} (95% CI {-x['ci95_block'][1]:+.5f} to {-x['ci95_block'][0]:+.5f})")
    print("\nTUNE windows:")
    for pre, m in (("mlb_tune_", "win_logloss"), ("atp_tune_", "games_rps"), ("ipl_elo_k_tune_", "win_logloss"),
                   ("ipl_lam_team_tune_", "total_rps")):
        for k in sorted((k for k in R["v2"] if k.startswith(pre)), key=lambda s: float(s.split("_")[-1])):
            v = R["v2"][k]
            print(f"- {k}: {m} A1 {v[m]['a1']:.4f} (A0 {v[m]['a0']:.4f})")

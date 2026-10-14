"""Markdown and CSV writers for research/model_shadow/. Every file carries its receipt block."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ml.config import SHADOW_ROOT

from ml.evaluation.report import COMPARATORS, METRICS, fmt, md_table

STATUS_CSV = SHADOW_ROOT / "MODEL_STATUS.csv"
PRED_COLS = ["league", "season", "date", "week", "event_id", "home", "away", "hs", "as_", "fit_date", "league_median_line",
             "MODEL_status", "MODEL_p_home", "MODEL_p_draw", "MODEL_p_away", "MODEL_p_over", "MODEL_mean_home",
             "MODEL_mean_away", "MODEL_sd_margin", "MODEL_sd_total", "BASE_p_home", "BASE_p_over", "TB1_p_home",
             "TB1_p_over", "KEYNUM_p_home", "KEYNUM_p_over"]

ENGINE_TEXT = {
    "gaussian": (
        "Joint-normal team ratings. Home score = mu_home + attack[home] + defence[away] + e1; away score = "
        "mu_away + attack[away] + defence[home] + e2; (e1, e2) bivariate normal. Fitted by weighted ridge least "
        "squares with exponential time decay (half-life in days) and a ridge penalty towards 0. The residual "
        "covariance is the weighted residual covariance times a tuned inflation factor. Prices come from the "
        "bivariate normal evaluated on the non-negative integer lattice and renormalised; tied mass is then "
        "resolved by the league's extra-time rule."),
    "dixon_coles": (
        "Dixon–Coles Poisson ratings. log lambda_home = c + home + attack[home] + defence[away]; log lambda_away = "
        "c + attack[away] + defence[home]; low-score dependence rho on the 0–0, 1–0, 0–1 and 1–1 cells. "
        "Time-decayed weighted likelihood with a ridge penalty, analytic gradient, L-BFGS-B. Promoted teams take a "
        "prior centre equal to the mean rating of the previous season's bottom three."),
    "count": (
        "Poisson team ratings (no rho), time-decayed weighted likelihood with a ridge penalty. Ice hockey: fitted on "
        "regulation goals (an OT/SO final keeps min(home, away) for both teams). Baseball: final runs with a "
        "negative-binomial dispersion phi (Var = mu + phi mu^2) estimated by moments."),
}

TIE_TEXT = {
    "draw": "Draws are a genuine outcome at this endpoint and stay in the grid.",
    "overtime": ("Tied regulation mass goes to one extra period: home wins it with Phi(mu_margin * sqrt(r) / "
                 "sd_margin) (r = extra period / regulation length); each team adds about r * mean_total / 2 points "
                 "and the winner a further w (rounded mean absolute extra-period margin)."),
    "overtime_residual": ("Tied regulation mass goes to sudden-death extra time (winner + 3 in the NFL, + 1 in the "
                          "NRL); a share fitted by moments on the training draws stays a draw."),
    "hockey_regulation": ("Regulation grid; tied mass goes to an OT/SO branch won by the home team with the training "
                          "share of home OT/SO wins (winner +1). A share fitted by moments stays drawn where the "
                          "competition's training window contains genuine ties."),
    "extras": ("Tied mass goes to an extra-innings branch won by the home team with the training share of home "
               "extra-inning wins (winner +1); a share fitted by moments stays tied where the competition allows "
               "ties (for example NPB and KBO)."),
}


def _receipt(rec: dict, extra: dict) -> str:
    items = {**rec, **extra}
    return "\n".join(f"- `{k}`: {v}" for k, v in items.items())


def status_for(verdict: str, warnings) -> str:
    """PASS on data with an integrity warning is DATA_HOLD: no lane until the rows are verified at a field owner."""
    if verdict != "PASS_DEVELOPMENT":
        return "DEVELOPMENT_ONLY"
    return "DATA_HOLD" if warnings else "SHADOW_CANDIDATE"


def status_row(model_id: str, path: str, engine: str, verdict: str, detail: str, seasons: str, tb1_label: str,
               warnings=()) -> dict:
    return {"model_id": model_id, "competition": path, "engine": engine, "development_verdict": verdict,
            "detail": detail, "test_seasons": seasons, "tb1": tb1_label,
            "data_warnings": ";".join(warnings), "status": status_for(verdict, warnings)}


def _status_row_unused(model_id: str, league: str, engine: str, verdict: str, detail: str, seasons: str) -> None:
    row = pd.DataFrame([{"model_id": model_id, "league": league, "engine": engine, "development_verdict": verdict,
                         "detail": detail, "test_seasons": seasons,
                         "status": "SHADOW_CANDIDATE" if verdict == "PASS_DEVELOPMENT" else "DEVELOPMENT_ONLY"}])
    if STATUS_CSV.exists():
        cur = pd.read_csv(STATUS_CSV, dtype=str)
        cur = cur[cur["model_id"] != model_id]
        row = pd.concat([cur, row.astype(str)], ignore_index=True)
    STATUS_CSV.parent.mkdir(parents=True, exist_ok=True)
    row.sort_values("model_id").to_csv(STATUS_CSV, index=False, lineterminator="\n")


def _write(path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_league(res: dict, rec: dict) -> None:
    lg = res["league"]
    code, mid = lg.competition, lg.model_id
    d = SHADOW_ROOT / mid
    pt = res["paired"]
    v = res["verdict"]
    status = status_for(v["overall"], lg.data_warnings)
    prim = pt[(pt["metric"] == METRICS[0][1])]
    receipt = _receipt(rec, {"model_id": mid, "archive_snapshot_sha256": res["data_sha"],
                             "seconds": round(res["seconds"])})

    # predictions (market-free)
    pred = res["pred"]
    cols = [c for c in PRED_COLS if c in pred.columns]
    out = pred[cols].copy()
    for c in out.columns:
        if out[c].dtype.kind == "f":
            out[c] = out[c].round(5)
    from ml.shadow.lane import assert_no_market_columns
    assert_no_market_columns(out.columns)
    d.mkdir(parents=True, exist_ok=True)
    out.to_csv(d / "DEVELOPMENT_PREDICTIONS.csv", index=False, lineterminator="\n")

    # results
    lines = [f"# Development results: `{mid}`", "",
             "**Evidence class: `HISTORICAL_DEVELOPMENT`.** Rolling-origin backtest on archive seasons that have been "
             "opened before. It shows mechanics and plausibility, not prospective skill (SCORING_AND_VALIDATION §8).", "",
             f"**Verdict:** `{v['overall']}`. Against BASELINE_LEAGUE_V1: `{v.get('BASELINE_LEAGUE_V1')}`. "
             f"Against TB-1: `{v.get('TEAM_BASELINE_P (TB-1)')}`. Rule: the primary metric (home-win Brier) must have a "
             "95% week-block interval below 0 against both comparators in every test season "
             "(ML_RL_IMPLEMENTATION_FRAMEWORK §9.5).", "",
             f"Test seasons {list(lg.test_seasons)}; hyperparameters chosen on {list(lg.tune_seasons)} only; "
             "differences are candidate − comparator (negative favours the model); each interval is a t-interval over "
             "ISO-week means of event-averaged differences (SCORING_AND_VALIDATION §5).", ""]
    for comp, name in COMPARATORS:
        sub = pt[pt["comparator"] == name]
        if sub.empty:
            continue
        lines += [f"## Against {name}", "",
                  md_table(sub, ["metric", "season", "n_games", "candidate", "comparator_value", "mean", "lo", "hi",
                                 "k_weeks", "status"]), ""]
    for k, tab in res["extra"].items():
        lines += [f"## Variant: {k} (NFL key-number reweighting minus the plain model)", "",
                  md_table(tab, ["metric", "season", "mean", "lo", "hi", "k_weeks", "status"]), ""]
    cal = res["calibration"]
    lines += ["## Calibration of P(home win) on the test seasons", "",
              f"Calibration-in-the-large {fmt(cal['fit']['cal_in_large'])}; ECE {fmt(cal['fit']['ece'])}; logistic "
              f"slope {fmt(cal['fit']['slope'], 3)} (SE {fmt(cal['fit']['slope_se'], 3)}), intercept "
              f"{fmt(cal['fit']['intercept'], 3)} (SE {fmt(cal['fit']['intercept_se'], 3)}). Brier decomposition: "
              f"reliability {fmt(cal['decomposition']['reliability'])}, resolution "
              f"{fmt(cal['decomposition']['resolution'])}, uncertainty {fmt(cal['decomposition']['uncertainty'])}.", "",
              md_table(cal["bins"], ["bin", "n", "mean_p", "hit_rate", "wilson_lo", "wilson_hi"]), ""]
    ce = res["calibration_experiment"]
    if len(ce):
        lines += ["## Recalibration experiment (ML-CAL-WIN): logistic map fitted on the previous season only", "",
                  "Calibrated minus uncalibrated home-win Brier; negative means recalibration helped.", "",
                  md_table(ce, ["season", "intercept", "slope", "n", "uncalibrated", "calibrated", "mean", "lo", "hi",
                                "status"]), ""]
    tt = res["tune_table"].head(10)
    lines += ["## Tuning (development seasons only; objective = mean margin CRPS + mean total CRPS)", "",
              md_table(tt, [c for c in tt.columns if c != "seconds"]), "", "## Receipt", "", receipt]
    _write(d / "DEVELOPMENT_RESULTS.md", "\n".join(lines))

    # parameters
    fm = res["final_model"]
    tab = fm.parameter_table()
    plines = [f"# Parameters: `{mid}`", "",
              f"Fit as of **{res['final_as_of'].date()}** on every regular-season and post-season game in the archive "
              f"from season {res['final_season'] - lg.history_seasons} to the archive's last game "
              f"({(res['final_as_of'] - pd.Timedelta(days=1)).date()}), with the frozen hyperparameters below. "
              "Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are "
              "not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).", "",
              "Hyperparameters: " + ", ".join(f"`{k}` = {v}" for k, v in res["best"].items()), ""]
    if lg.engine == "gaussian":
        c = fm.cov
        plines += [f"League constants: mu_home **{fm.mu_h:.3f}**, mu_away **{fm.mu_a:.3f}**; residual covariance "
                   f"[[{c[0, 0]:.2f}, {c[0, 1]:.2f}], [{c[0, 1]:.2f}, {c[1, 1]:.2f}]] (inflation included); margin SD "
                   f"**{fm.sd_margin:.2f}**; residual draw share **{fm.residual_draw:.3f}**.", ""]
        t0, t1 = tab.iloc[0]["team"], tab.iloc[-1]["team"]
        mh, ma, _ = fm.means(t0, t1)
        g, _ = fm.grid(t0, t1)
        from scipy import stats as _st
        plines += ["**Worked example (check by hand).** "
                   f"{t0} at home to {t1}: mean home = {fm.mu_h:.3f} + attack[{t0}] {fm.att[fm.idx[t0]]:+.3f} + "
                   f"defence[{t1}] {fm.dfn[fm.idx[t1]]:+.3f} = **{mh:.2f}**; mean away = {fm.mu_a:.3f} + "
                   f"attack[{t1}] {fm.att[fm.idx[t1]]:+.3f} + defence[{t0}] {fm.dfn[fm.idx[t0]]:+.3f} = **{ma:.2f}**. "
                   f"Normal approximation P(home ahead) = Phi({mh - ma:.2f} / {fm.sd_margin:.2f}) = "
                   f"**{_st.norm.cdf((mh - ma) / fm.sd_margin):.3f}**; the lattice price including the extra-time "
                   f"branch is **{g.winner()[0]:.3f}** (PROBABILITY_TOOLKIT §1).", ""]
        tab = tab.rename(columns={"net_margin_vs_average": "net (points per game vs average)"})
    else:
        extra = f"rho **{fm.rho:.3f}**, " if fm.p.use_rho else ""
        extra += f"phi **{fm.phi:.4f}**, " if fm.p.negbin else ""
        plines += [f"League constants: intercept c **{fm.c:.4f}**, home **{fm.home:.4f}**, {extra}P(home wins extra "
                   f"time) **{fm.p_home_extra:.3f}**; promoted-team prior centre (attack, defence) "
                   f"({fm.new_centre[0]:+.3f}, {fm.new_centre[1]:+.3f}).", ""]
        t0, t1 = tab.iloc[0]["team"], tab.iloc[-1]["team"]
        lh, la, _ = fm.rates(t0, t1)
        g, _ = fm.grid(t0, t1)
        w = g.winner()
        plines += ["**Worked example (check by hand).** "
                   f"{t0} at home to {t1}: lambda_home = exp({fm.c:.4f} + {fm.home:.4f} + {fm.att[fm.idx[t0]]:+.4f} + "
                   f"{fm.dfn[fm.idx[t1]]:+.4f}) = **{lh:.3f}**; lambda_away = exp({fm.c:.4f} + {fm.att[fm.idx[t1]]:+.4f} + "
                   f"{fm.dfn[fm.idx[t0]]:+.4f}) = **{la:.3f}**. Grid winner masses (home, draw, away) = "
                   f"**({w[0]:.3f}, {w[1]:.3f}, {w[2]:.3f})** (PROBABILITY_TOOLKIT §2–§3 tables).", ""]
    plines += [md_table(tab, list(tab.columns), 4), "", "## Receipt", "", receipt]
    _write(d / "PARAMETERS.md", "\n".join(plines))

    # model card
    load = res["load"]
    pcounts = prim[prim["season"] == "ALL"]
    summary = "; ".join(f"vs {r.comparator}: {r['mean']:+.4f} [{r['lo']:+.4f}, {r['hi']:+.4f}]"
                        for _, r in pcounts.iterrows())
    card = [f"# Model card: `{mid}`", "",
            f"**Status: `{status}`.** "
            + ({"SHADOW_CANDIDATE": "Development passed; it may enter a prospective shadow lane once its hypothesis is "
                                    "registered (HYPOTHESIS_REGISTER) and the lane is started. It is not a card input.",
                "DATA_HOLD": "Development passed, but the competition's rows failed an automatic integrity check "
                             f"({'; '.join(lg.data_warnings)}). No lane until the rows are verified against the field "
                             "owner (prompt 7). It is not a card input.",
                "DEVELOPMENT_ONLY": "Development did not pass the every-season bar; it stays a development artifact "
                                    "and enters no lane. It is not a card input."}[status]), "",
            "| Field | Value |", "|---|---|",
            f"| Competition / endpoint | `{lg.path}` / `{lg.endpoint}` |",
            f"| Comparators | `BASELINE_LEAGUE_V1`; TB-1 constants `{lg.tb1_label}`. VALIDATED = PROBABILITY_TOOLKIT §4.3 "
            "table. CALIBRATED_PREV_EDITION = the toolkit's arithmetic and the nearest sport's k, with home edge and "
            "widths taken from the competition's previous edition by replaying TB-1 game by game (earlier data only); "
            "the nearest sport's constants alone made TB-1 worse than the league-only baseline in some competitions |",
            f"| Evaluation stages | {', '.join(lg.eval_stages)} (regular season only where the competition has one) |",
            f"| Data integrity | {'; '.join(lg.data_warnings) or 'no automatic warning'} |",
            f"| Engine | `{lg.engine}` |",
            f"| Contracts priced | winner{' (3-way)' if lg.tie_rule == 'draw' else ''}, any handicap line, any total "
            "line, from one score grid |",
            f"| Population | competitive games from the archive (`Previous Sports Results/{lg.path}`); "
            f"pre-season excluded; rows read {load.rows_read}, kept {load.rows_kept}, dropped {load.dropped or 'none'} |",
            "| Label tier | B / development only; field-owner admission for these exact rows and fields is not established |",
            "| Inputs | prior results only (dates strictly before the fit date). No lineups, injuries, weather, rest "
            "or prices. |",
            f"| Fit window | games before the Monday of the forecast week, seasons s − {lg.history_seasons} … s, "
            "weekly refits |",
            f"| Hyperparameters | {', '.join(f'{k}={v}' for k, v in res['best'].items())} (chosen on "
            f"{list(lg.tune_seasons)}) |",
            "| Failure behaviour | fit failure gives `NOT_ISSUED:FIT_FAILED`; an unseen team gets an explicit, labelled "
            "prior (`NEW_TEAM_PRIOR`). No default numbers. |",
            "| Calibration | identity (`IDENTITY_INSUFFICIENT_CAL`); the recalibration experiment is in "
            "DEVELOPMENT_RESULTS |",
            f"| Development verdict | `{v['overall']}`: home-win Brier, all test seasons pooled: {summary} |",
            "| Prospective results | none (no lane started) |", "",
            "## Method", "", ENGINE_TEXT[lg.engine], "", TIE_TEXT[lg.tie_rule], "",
            "## Files", "",
            "- [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md): paired comparisons, calibration, tuning.",
            "- [PARAMETERS.md](PARAMETERS.md): the latest fit, with a worked example a reader can check by hand.",
            "- [DEVELOPMENT_PREDICTIONS.csv](DEVELOPMENT_PREDICTIONS.csv): every development price (no market fields).",
            "", "## Limits", "",
            "- Results-only model. Lineups, injuries and rest are not modelled; real cards know more on the day.",
            "- The archive rows are LABEL_B unless stated; dates are calendar cutoffs, not publication times.",
            "- Development seasons have been opened before; only a prospective lane can show skill.",
            "", "## Receipt", "", receipt]
    _write(d / "MODEL_CARD.md", "\n".join(card))
    return status_row(mid, lg.path, lg.engine, v["overall"], summary, ",".join(map(str, lg.test_seasons)), lg.tb1_label,
                      lg.data_warnings)


def write_cricket(res: dict, rec: dict) -> dict:
    from ml.core.metrics import paired_week_interval, iso_week

    lg = res["league"]
    mid = lg.model_id
    d = SHADOW_ROOT / mid
    t = res["test"].copy()
    t["week"] = iso_week(t["date"])
    rows = []
    pairs = [("C1", "C0"), ("C2", "C1"), ("C2", "C0"), ("C2PRE", "C0")]
    for a, b in pairs:
        for metric in ("crps", "brier_over"):
            for s in [*sorted(t["season"].unique()), "ALL"]:
                x = t if s == "ALL" else t[t["season"] == s]
                iv = paired_week_interval(x[f"{a}_{metric}"] - x[f"{b}_{metric}"], x["event_id"], x["week"])
                rows.append({"candidate": a, "comparator": b, "metric": metric, "season": s, "n": len(x),
                             "cand_value": x[f"{a}_{metric}"].mean(), "comp_value": x[f"{b}_{metric}"].mean(), **iv})
    pt = pd.DataFrame(rows)
    every = pt[(pt["candidate"] == "C2") & (pt["comparator"] == "C1") & (pt["metric"] == "crps") & (pt["season"] != "ALL")]
    every_c0 = pt[(pt["candidate"] == "C2") & (pt["comparator"] == "C0") & (pt["metric"] == "crps") & (pt["season"] != "ALL")]
    verdict = ("PASS_DEVELOPMENT" if len(every) and (every["status"] == "BELOW_ZERO").all()
               and (every_c0["status"] == "BELOW_ZERO").all() else "FAIL_DEVELOPMENT")
    cov = {lv: t[f"{lv}_in80"].mean() for lv in ("C0", "C1", "C2", "C2PRE")}
    pit = {lv: np.histogram(t[f"{lv}_pit"], bins=5, range=(0, 1))[0].tolist() for lv in ("C0", "C2")}
    receipt = _receipt(rec, {"model_id": mid, "params": res["params"], "dropped_rows": res["dropped"],
                             "rows_used": len(res["data"]), "seconds": round(res["seconds"])})
    keep = ["season", "date", "event_id", "bat", "bowl", "venue", "runs", "line", "C0_mean", "C0_sigma", "C1_mean",
            "C2_mean", "C2_sigma", "C0_p_over", "C1_p_over", "C2_p_over", "C2PRE_p_over"]
    out = t[keep].copy()
    for c in out.columns:
        if out[c].dtype.kind == "f":
            out[c] = out[c].round(4)
    d.mkdir(parents=True, exist_ok=True)
    out.to_csv(d / "DEVELOPMENT_PREDICTIONS.csv", index=False, lineterminator="\n")
    lines = [f"# Development results: `{mid}` (first-innings runs, `{lg.path}`)", "",
             "**Evidence class: `HISTORICAL_DEVELOPMENT`.** Refitted before every match date from earlier IPL first "
             "innings (four seasons plus season to date). Hyperparameters chosen on "
             f"{list(lg.tune_seasons)} only; test seasons {list(lg.test_seasons)}.", "",
             f"**Verdict for C2 (team model):** `{verdict}` (CRPS interval below 0 against both C1 and C0 in every "
             "test season required).", "",
             "Central 80% interval coverage on the test seasons (target 0.80): " +
             ", ".join(f"{k} {v:.3f}" for k, v in cov.items()) + ".", "",
             "PIT histogram, 5 equal bins (a flat histogram is calibrated; U-shaped means too narrow): " +
             "; ".join(f"{k} {v}" for k, v in pit.items()) + ".", "",
             md_table(pt, ["candidate", "comparator", "metric", "season", "n", "cand_value", "comp_value", "mean", "lo",
                           "hi", "k_weeks", "status"]), "",
             "## Tuning (top 8; objective = C2 mean CRPS on the tune seasons)", "",
             md_table(res["tune_table"].head(8), list(res["tune_table"].columns)), "", "## Receipt", "", receipt]
    _write(d / "DEVELOPMENT_RESULTS.md", "\n".join(lines))
    card = [f"# Model card: `{mid}`", "",
            f"**Status: `{'SHADOW_CANDIDATE' if verdict == 'PASS_DEVELOPMENT' else 'DEVELOPMENT_ONLY'}`.** Not a card "
            "input.", "",
            "| Field | Value |", "|---|---|",
            f"| Contract | runs of the team batting first, full-length innings ({lg.overs_cap:.0f} overs bowled or all out) |",
            f"| Population | scorecards in `Previous Sports Results/{lg.path}`; excluded: {res['dropped']} |",
            "| Ladder | C0 league-only (time-decayed mean and SD) · C1 + shrunk venue effect · C2 + batting and bowling "
            "team strengths (weighted ridge) · C2PRE = 50/50 unfitted symmetric batting-order scenario; toss fairness does not establish this weight |",
            "| Distribution | discretised normal on 0–600 runs; finite-support approximation, not a physical run cap |",
            f"| Hyperparameters | {res['params']} |",
            "| Known limits | no ball-by-ball phase data yet (WP-05), no XI, pitch or weather; Impact Player era "
            "(2023+) handled only through time decay |",
            "", "See [DEVELOPMENT_RESULTS.md](DEVELOPMENT_RESULTS.md).", "", "## Receipt", "", receipt]
    _write(d / "MODEL_CARD.md", "\n".join(card))
    allp = pt[(pt["candidate"] == "C2") & (pt["comparator"] == "C1") & (pt["metric"] == "crps") & (pt["season"] == "ALL")]
    det = "; ".join(f"C2−C1 CRPS {r['mean']:+.3f} [{r['lo']:+.3f}, {r['hi']:+.3f}]" for _, r in allp.iterrows())
    return status_row(mid, lg.path, "cricket_first_innings", verdict, det, ",".join(map(str, lg.test_seasons)),
                      "NONE (C0/C1 comparators)", lg.data_warnings)


def write_cards(res: dict, rec: dict) -> None:
    d = SHADOW_ROOT / "CARD_CALIBRATION"
    g = res["groups"]
    lines = ["# Calibration audit of the issued cards' stated probabilities", "",
             "**Descriptive only.** Source: `GAME_PREDICTION_RANK_LOG.csv` (rows with a numeric `stated_p` and a PASS or "
             "FAIL grade). Rows within a card are dependent, so intervals resample whole cards. The cards span several "
             "method and scoring versions, many were ungated, and line choice shapes hit rates (CURRENT_RULES §10). "
             "Nothing here recalibrates, regrades or relabels any card. This report applies the October 14 calibration "
             "recommendations to the cards' own history (see ML_RL_IMPLEMENTATION_FRAMEWORK §4, report R4).", "",
             f"Inventory: {res['info']}.", "",
             "Calibration-in-the-large is mean p − hit rate (positive = over-confident). Slope: logistic regression of "
             "the outcome on logit(p); 1 is ideal, below 1 means probabilities are too extreme.", "",
             md_table(g, ["group", "rows", "cards", "mean_p", "hit_rate", "cal_in_large", "cil_card_lo", "cil_card_hi",
                          "slope", "slope_se", "ece", "brier", "reliability", "resolution"]), "",
             "## Reliability bins, all rows", "", md_table(res["bins_all"], ["bin", "n", "mean_p", "hit_rate", "wilson_lo",
                                                                            "wilson_hi"]), "",
             "## Reliability bins, Ranks 1–2", "", md_table(res["bins_top2"], ["bin", "n", "mean_p", "hit_rate",
                                                                              "wilson_lo", "wilson_hi"]), "",
             "## Receipt", "", _receipt(rec, {})]
    _write(d / "REPORT.md", "\n".join(lines))


def write_decision_lab(res: dict, rec: dict) -> None:
    d = SHADOW_ROOT / "DECISION_LAB"
    pol = res["policies"]
    lines = ["# DECISION_LAB results: EPL paper staking study (firewalled)", "",
             "> **Firewall (CURRENT_RULES §5a).** Historical paper simulation only. Not betting advice, not a value claim, "
             "never read by prompts 1–3, never cited by a card, rule, rank, width or learning disposition. Raw prices stay "
             "in the local, git-excluded football-data capture; only these aggregates are committed.", "",
             f"Join: {res['join']}. Warm-up season labels {res['warmup_seasons']} (method choice, sigma_p, bandit warm-up); "
             f"later evaluation season labels {res['evaluation_seasons']}. Model: `" + res["model_id"] + "` prices, frozen at each week's Monday from earlier "
             "games. Taken price: Pinnacle pre-closing columns PSH/PSD/PSA; quote/capture/fill times are not verified. Close: Pinnacle "
             f"closing (PSCH/PSCD/PSCA), de-vigged by **{res['devig_method']}** (warm-up closing log loss "
             + ", ".join(f"{k} {v:.5f}" for k, v in res["devig_logloss_warmup"].items()) + ").", "",
             "## 1. Forecast benchmark: model against the no-vig market (MKT-BENCH-r1)", "",
             "Three-way half-sum Brier; lower is better.", "",
             md_table(res["bench"].pivot(index="season", columns="source", values="brier_3way").reset_index(),
                      ["season", "MODEL", "TB1", "BASELINE_LEAGUE_V1", "NOVIG_TAKEN", "NOVIG_CLOSE"]), "",
             "Paired differences (model − other), week-block intervals:", "",
             md_table(res["bench_paired"], ["model_minus", "season", "mean", "lo", "hi", "k_weeks", "status"]), "",
             "## 2. Staking policies (one position per match on the model's highest-EV outcome)", "",
             f"Estimation-error SD for Kelly shrinkage, sigma_p = **{res['sigma_p_warmup']:.4f}** (SD of model − no-vig "
             "close on the warm-up seasons). Caps: 2% per bet, 10% per matchweek; a drawdown over 20% halts staking "
             "pending review, and bankroll figures freeze there. CLV = taken odds × no-vig closing probability − 1. "
             "The CLV columns cover every decision the policy staked over all reported seasons, independent of the "
             "bankroll path.", "",
             md_table(pol, ["policy", "n_bets", "mean_clv", "clv_week_lo", "clv_week_hi", "share_clv_positive",
                            "stake_weighted_clv", "hit_rate", "mean_odds", "turnover", "pnl", "roi", "final_bankroll",
                            "max_drawdown", "halted_at_week"]),
             "",
             "## 3. Off-policy evaluation check", "",
             "Every arm's reward (stake × CLV) is computable for every match here, so the problem is full-information and "
             "the bandit's inverse-propensity estimate can be checked against the exact value of the policy 'always "
             f"quarter stake': {res['ope']}.", "",
             "## Reading", "",
             "- These are historical development comparisons; market-relative scores or simulated profit do not establish future economic performance or causal blame.",
             f"- Feedback timing: {res['feedback_timing']}. All same-day actions precede that day's closing-reward updates; date-only inputs still do not verify execution timing.",
             "- Actions are sampled from the returned probability vector, so logged propensities describe the actual behaviour policy. Full-information rewards still assume observable counterfactual payoffs without market impact.",
             "- Prices, limits, latency and account restrictions of a real operator are not modelled.", "",
             "## Receipt", "", _receipt(rec, {"rows": res["frame_rows"]})]
    _write(d / "RESULTS.md", "\n".join(lines))


def write_index(rec: dict, rows: list[dict] | None = None) -> None:
    if rows is not None:
        pd.DataFrame(rows).sort_values(["status", "competition"]).to_csv(STATUS_CSV, index=False, lineterminator="\n")
    if not STATUS_CSV.exists():
        return
    st = pd.read_csv(STATUS_CSV, dtype=str).fillna("")
    lines = ["# Model status (generated)", "",
             "One row per competition folder. `SHADOW_CANDIDATE` = passed development against both comparators in "
             "every test season, on rows with no integrity warning; may enter a registered prospective lane. "
             "`DATA_HOLD` = passed, but the rows failed an automatic integrity check; no lane until verified. "
             "`DEVELOPMENT_ONLY` = did not pass; enters no lane. `RUN_FAILED` = the run raised an error. No model "
             "is a card input. `RUN_INCOMPLETE` means the interrupted run has no completed artifact. `NOT_MODELLED` rows name why a competition in the archive has no model. "
             "Read [ARTIFACT_PROVENANCE.md](ARTIFACT_PROVENANCE.md) before admission; a numerical candidate with unverified source/code custody remains DATA_HOLD.", "",
             md_table(st, ["competition", "model_id", "engine", "status", "development_verdict", "tb1", "test_seasons",
                           "data_warnings", "detail"]),
             "", "## Receipt", "", _receipt(rec, {})]
    _write(SHADOW_ROOT / "STATUS.md", "\n".join(lines))

"""Standalone same-line league baseline (BASELINE_LEAGUE_V1) for any supported card (RET-10).

Prices the card's exact contracts from a league-only score distribution fitted on reviewed, horizon-admitted
history — no team identity, no lineup, no market input. It is the same comparator V3 uses as its LEAGUE_BASELINE
expert, made available on its own so that a card can freeze BASELINE_P even when the full primary run is unavailable
(unseen teams, short history) or not yet executed. In 600 historical cards only four events carried a numeric same-row
baseline, so skill against a baseline could not be measured.

    python -m ml baseline --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv \
        [--competition-source COMPETITION_SOURCE.csv] --out BASELINE.csv

Inputs use the primary schemas (PRIMARY_PREDICTION_PROTOCOL §2) and the same admission gates. The output lists
W/P/L, BASELINE_P = W/(W+L), the number of games used and the recipe; it is a comparator, never a card p_card.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from ml import primary as p
from ml.config import get_league
from ml.models.baseline import LeagueBaseline
from ml.models.common import residual_draw_share

RECIPE = "BASELINE_LEAGUE_V1: league-only score means/covariance (or count rates) of admitted history; tie rule as V3"


def baseline_rows(request: dict, history: list[dict], contracts: list[dict], competition_source=None) -> list[dict]:
    if "cutoff" in request:
        raise p.AdmissionError("no separate cutoff: supply scheduled_start")
    lg = p.reviewed_source_league(request, competition_source[0]) if competition_source else get_league(request["competition"])
    if lg is None or request["competition"] != lg.path or request["endpoint"] != lg.endpoint:
        raise p.AdmissionError("request/competition scope mismatch")
    horizon, basis = p.information_horizon(request)
    train = p.admit_history(history, horizon, request["event_id"], lg.path, lg.endpoint)
    fitting = train.copy()
    if lg.tie_rule != "draw" and lg.engine != "cricket":
        fitting["hs"], fitting["as_"] = train.reg_hs, train.reg_as
    if lg.engine == "cricket":
        raise p.AdmissionError("cricket baseline uses the first-innings C0 model inside primary predict")
    base = LeagueBaseline(lg).fit(fitting)
    # Final-score labels exactly as primary._fit_models applies them to its LEAGUE_BASELINE expert.
    if hasattr(base, "residual_draw") and hasattr(base, "sd_margin"):
        base.residual_draw = residual_draw_share(train, base.sd_margin)
    if hasattr(base, "p_home_extra"):
        extra = train[train.decision.isin(["Overtime", "Shootout", "EXTRAS"])]
        base.p_home_extra = float((extra.hs > extra.as_).mean()) if len(extra) >= 20 else .5
    grid = base.grid()
    out = []
    for c in contracts:
        w, push, loss = p.price(grid, c, lg.endpoint)
        out.append(dict(contract_key=c["contract_key"], family=c["family"], side=c["side"], line=c["line"],
                        endpoint=lg.endpoint, baseline_win=w, baseline_push=push, baseline_loss=loss,
                        baseline_p=w / (w + loss) if w + loss > 0 else "NOT_COMPUTED", games=len(train),
                        horizon=horizon.isoformat(), horizon_source=basis, recipe=RECIPE, role="COMPARATOR_NOT_P_CARD"))
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for name in ("request", "history", "contracts", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--competition-source", type=Path)
    args = parser.parse_args(argv)
    req = p.read_rows(args.request)
    if len(req) != 1:
        raise p.AdmissionError("exactly one event per request")
    src = p.read_rows(args.competition_source) if args.competition_source else None
    rows = baseline_rows(req[0], p.read_rows(args.history), p.read_rows(args.contracts), src)
    for r in rows:
        r["generated_at"] = datetime.now(timezone.utc).isoformat()
        r["code_sha256"] = p.source_hash()
    with args.out.open("xb") as f:
        f.write(p.csv_bytes(rows))
    print(f"{len(rows)} baseline rows -> {args.out}")


if __name__ == "__main__":
    main()

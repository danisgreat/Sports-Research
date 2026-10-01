"""Pre-issue distribution-to-contract bridge for integer-score sports.

Input is a model-produced JSON distribution, never hand-entered row probabilities.
Output is a draft; Part 6 issuance remains a separate immutable append.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from .sports.base import Contract


def states(spec: list[dict]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not spec:
        raise ValueError("empty joint distribution")
    for row in spec:
        for field in ("home","away"):
            value=row[field]
            if isinstance(value,bool) or not isinstance(value,(int,float)) or not np.isfinite(value) or value<0 or int(value)!=value:
                raise ValueError("score states require nonnegative integers")
    home = np.array([s["home"] for s in spec], dtype=int)
    away = np.array([s["away"] for s in spec], dtype=int)
    mass = np.array([s["p"] for s in spec], dtype=float)
    if (home < 0).any() or (away < 0).any() or (mass < 0).any() or not np.isfinite(mass).all():
        raise ValueError("invalid score or mass")
    if abs(mass.sum()-1) > 1e-8:
        raise ValueError("joint distribution must sum to one")
    if len(set(zip(home.tolist(), away.tolist()))) != len(home):
        raise ValueError("duplicate scoreline state")
    return home, away, mass


def _outcome(home: np.ndarray, away: np.ndarray, c: Contract) -> tuple[np.ndarray, np.ndarray]:
    if c.market == "1X2":
        if c.side not in {"HOME", "DRAW", "AWAY"}:
            raise ValueError("bad 1X2 side")
        win = ((home > away) if c.side == "HOME" else (home == away) if c.side == "DRAW" else (away > home))
        return win, np.zeros(len(home), dtype=bool)
    if c.market == "BTTS":
        if c.side not in {"YES", "NO"}:
            raise ValueError("bad BTTS side")
        yes = (home > 0) & (away > 0)
        return (yes if c.side == "YES" else ~yes), np.zeros(len(home), dtype=bool)
    if c.market == "ML":
        if c.side not in {"HOME", "AWAY"}:
            raise ValueError("bad ML side")
        value = home-away if c.side == "HOME" else away-home
    elif c.market == "SPREAD":
        if c.side not in {"HOME", "AWAY"}:
            raise ValueError("bad spread side")
        value = (home-away if c.side == "HOME" else away-home)+c.line
    else:
        if c.side not in {"OVER", "UNDER"}:
            raise ValueError("bad total side")
        value = (home+away-c.line)*(1 if c.side == "OVER" else -1)
    return value > 0, value == 0


def price(state: tuple[np.ndarray, np.ndarray, np.ndarray], c: Contract) -> dict:
    home, away, mass = state
    win, push = _outcome(home, away, c)
    w, p = float(mass[win].sum()), float(mass[push].sum())
    l = float(1-w-p)
    if min(w, p, l) < -1e-8 or 1-p <= 0:
        raise ValueError("invalid outcome masses")
    return dict(w=w, p=p, l=l, conditional_win=w/(1-p))


def pair_type(state, a: Contract, b: Contract) -> str:
    h, aw, mass = state
    active = mass > 1e-12
    wa, pa = _outcome(h, aw, a)
    wb, pb = _outcome(h, aw, b)
    if np.all(((wa.astype(int)+wb.astype(int)) == 1)[active]) and not (pa | pb)[active].any():
        return "FORCED_PAIR"
    if np.all((wa | wb)[active]):
        return "COVERING_PAIR"
    return "FREE"


def _sha_distribution(spec: list[dict]) -> str:
    raw = json.dumps(spec, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def build(spec: dict, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("issue time must be timezone aware")
    start = datetime.fromisoformat(spec["start_utc"].replace("Z", "+00:00"))
    cutoff = datetime.fromisoformat(spec["data_cutoff_utc"].replace("Z", "+00:00"))
    if start.tzinfo is None or cutoff.tzinfo is None or not cutoff <= now < start:
        raise ValueError("cutoff <= issue < actual start is required")
    checksum=spec.get("data_checksum","")
    if not spec.get("official_event_id") or len(checksum)!=64 or any(c not in "0123456789abcdef" for c in checksum.lower()) or not spec.get("model_version"):
        raise ValueError("missing event or model provenance")
    model = states(spec["model_states"])
    card_raw = spec.get("card_states", spec["model_states"])
    card = states(card_raw)
    if not np.array_equal(model[0], card[0]) or not np.array_equal(model[1], card[1]):
        raise ValueError("adjustment changed scoreline support")
    if card_raw != spec["model_states"] and not (spec.get("adjustment_type") and spec.get("adjustment_reason") and spec.get("adjustment_parameters")):
        raise ValueError("unexplained card adjustment")
    if spec.get("adjustment_type", "NONE") == "NONE" and card_raw != spec["model_states"]:
        raise ValueError("NONE adjustment changed distribution")
    tier = spec.get("lane_status")
    if tier not in {"VALIDATED", "UNVALIDATED", "NO_MODEL"}:
        raise ValueError("unknown lane status")
    if tier == "NO_MODEL":
        raise ValueError("NO_MODEL cannot emit numerical pilot card")
    baseline_raw = spec.get("baseline_states")
    if baseline_raw is None:
        raise ValueError("baseline distribution is mandatory")
    baseline = states(baseline_raw)
    if not np.array_equal(model[0], baseline[0]) or not np.array_equal(model[1], baseline[1]):
        raise ValueError("baseline support differs")
    if tier == "UNVALIDATED":
        # U10: a whole-distribution mixture preserves every cross-market identity.
        card = (card[0], card[1], .5*baseline[2]+.5*card[2])
    lineup = spec.get("lineup_status")
    if lineup not in {"CONFIRMED", "PROJECTED", "UNKNOWN"}:
        raise ValueError("lineup status is required")
    if lineup in {"CONFIRMED", "PROJECTED"}:
        if not spec.get("lineup_source_url","").startswith("https://"):
            raise ValueError("lineup status needs an original source URL")
        retrieved=spec.get("lineup_retrieved_utc")
        if not retrieved:
            raise ValueError("lineup status needs a retrieval timestamp")
        retrieved=datetime.fromisoformat(retrieved.replace("Z","+00:00"))
        if retrieved.tzinfo is None or retrieved>now or retrieved>start:
            raise ValueError("lineup retrieval time is invalid")
    if lineup == "UNKNOWN":
        width_receipt = spec.get("unknown_lineup_width_receipt")
        if not isinstance(width_receipt, dict) or not width_receipt.get("source_url"):
            raise ValueError("UNKNOWN lineup requires a quantified width receipt")
        before = states(card_raw)
        def moments(state):
            h,a,p = state
            margin,total = h-a,h+a
            return (float(np.dot(p,margin)),float(np.dot(p,total)),
                    float(np.sqrt(np.dot(p,(margin-np.dot(p,margin))**2))),
                    float(np.sqrt(np.dot(p,(total-np.dot(p,total))**2))))
        old, new = moments(model), moments(before)
        if abs(old[0]-new[0]) > .01 or abs(old[1]-new[1]) > .01:
            raise ValueError("UNKNOWN lineup shifted the distribution centre")
        if new[2] < old[2]*1.05 or new[3] < old[3]*1.05:
            raise ValueError("UNKNOWN lineup did not widen both margin and total")
    if not spec.get("recency_check"):
        raise ValueError("recency check or explicit NOT_RETRIEVED status required")
    if not spec.get("state_source_url"):
        raise ValueError("event-state source is required")
    contracts = [Contract(spec["official_event_id"], **c) for c in spec["contracts"]]
    if len({(c.market,c.side,c.line,c.endpoint,c.period) for c in contracts}) != len(contracts):
        raise ValueError("duplicate contract")
    if len({c.endpoint for c in contracts}) != 1:
        raise ValueError("mixed settlement endpoints require separate distributions")
    rows = []
    for c in contracts:
        m, b, ca = price(model,c), price(baseline,c), price(card,c)
        rows.append(dict(contract=c.__dict__, p_model=m, p_baseline=b, p_card=ca))
    rows.sort(key=lambda r: (-r["p_card"]["conditional_win"], r["contract"]["market"], r["contract"]["side"]))
    for rank, row in enumerate(rows,1):
        row["rank_by_p_card"] = rank
    ranked = [Contract(**r["contract"]) for r in rows]
    top_pair = pair_type(card, ranked[0], ranked[1]) if len(ranked) >= 2 else "NOT_APPLICABLE"
    kill_mass = None
    kill_paths = []
    if len(ranked) >= 2:
        wa, pa = _outcome(card[0],card[1],ranked[0]); wb,pb = _outcome(card[0],card[1],ranked[1])
        kill = (~wa & ~pa) & (~wb & ~pb)
        kill_mass = float(card[2][kill].sum())
        buckets: dict[tuple[str,str,tuple[int,...]],float] = {}
        for i in np.flatnonzero(kill & (card[2] > 0)):
            margin=int(card[0][i]-card[1][i]); total=int(card[0][i]+card[1][i])
            margin_band=("home by 2+" if margin>=2 else "home by 1" if margin==1 else
                         "draw" if margin==0 else "away by 1" if margin==-1 else "away by 2+")
            total_band="0-2" if total<=2 else "3" if total==3 else "4+"
            kills=[]
            for rank,c in enumerate(ranked,1):
                won,pushed=_outcome(card[0][i:i+1],card[1][i:i+1],c)
                if not won[0] and not pushed[0]: kills.append(rank)
            key=(margin_band,total_band,tuple(kills))
            buckets[key]=buckets.get(key,0)+float(card[2][i])
        for number,(key,mass) in enumerate(sorted(buckets.items(),key=lambda kv:-kv[1]),1):
            kill_paths.append(dict(number=number, margin_band=key[0],total_band=key[1],
                                   rows_killed=list(key[2]),mass=mass))
        if abs(sum(path["mass"] for path in kill_paths)-kill_mass)>1e-9:
            raise AssertionError("kill-path decomposition does not close")
    card_states = [dict(home=int(h), away=int(a), p=float(p)) for h,a,p in zip(*card)]
    return dict(event_id=spec["official_event_id"], card_id=spec.get("card_id", "DRAFT"),
                issued_utc=now.astimezone(timezone.utc).isoformat(),
                data_cutoff_utc=cutoff.astimezone(timezone.utc).isoformat(),
                start_utc=start.astimezone(timezone.utc).isoformat(),
                model_version=spec["model_version"], data_checksum=spec["data_checksum"],
                model_distribution_sha256=_sha_distribution(spec["model_states"]),
                card_distribution_sha256=_sha_distribution(card_states),
                lane_status=tier, lineup_status=lineup, recency_check=spec["recency_check"],
                adjustment_type=spec.get("adjustment_type","NONE"),
                adjustment_reason=spec.get("adjustment_reason",""),
                top2_pair_type=top_pair, top2_both_fail=kill_mass,
                numbered_top2_kill_paths=kill_paths,
                top2_hit_metric_allowed=(top_pair == "FREE"),
                rows=rows, card_states=card_states)


def markdown(output: dict) -> str:
    lines = [f"## {output['card_id']} — event {output['event_id']} (script draft)",
             f"- Issued UTC: {output['issued_utc']}",
             f"- Input cutoff UTC: {output['data_cutoff_utc']}; start UTC: {output['start_utc']}",
             f"- Model: {output['model_version']}; data SHA-256: `{output['data_checksum']}`",
             f"- Model distribution SHA-256: `{output['model_distribution_sha256']}`",
             f"- Card distribution SHA-256: `{output['card_distribution_sha256']}`",
             f"- Lane: {output['lane_status']}; lineup: {output['lineup_status']}",
             f"- Recency: {output['recency_check']}",
             f"- Adjustment: {output['adjustment_type']} — {output['adjustment_reason']}",
             "", "| Rank | Contract | Baseline p | Model p | Card p | Push mass |",
             "|---:|---|---:|---:|---:|---:|"]
    for r in output["rows"]:
        c = r["contract"]
        label = f"{c['market']} {c['side']} {'' if c['line'] is None else c['line']} ({c['endpoint']})"
        lines.append(f"| {r['rank_by_p_card']} | {label} | {r['p_baseline']['conditional_win']:.4f} | {r['p_model']['conditional_win']:.4f} | {r['p_card']['conditional_win']:.4f} | {r['p_card']['p']:.4f} |")
    lines.extend(["", f"Top-two pair: {output['top2_pair_type']}; both lose: {output['top2_both_fail']}; Hit@2 eligible: {output['top2_hit_metric_allowed']}.",
                  "", "Numbered top-two kill paths (exhaustive; sum = both-lose mass):"])
    for path in output["numbered_top2_kill_paths"]:
        lines.append(f"{path['number']}. {path['margin_band']}, total {path['total_band']} — {path['mass']:.6f}; kills ranks {','.join(map(str,path['rows_killed']))}.")
    lines.append("Numerical rows derive from one recorded score distribution. The full distribution is in the JSON output.")
    return "\n".join(lines)+"\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    output = build(spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    args.output.with_suffix(".md").write_text(markdown(output), encoding="utf-8")

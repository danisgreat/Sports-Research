"""SELECT-SHADOW-v1: a separately registered shadow policy for the top two picks (v29.2, 22 November 2026).

The registered ranker (ONE-CHAT-v3, EVALUATION_PLAN_v29.0) ranks every priced line's favoured side by its stated
probability, even at 0.50, and can rank two labels that settle on the same outcome. It stays frozen and is not
changed here. This module computes a second list from the same sealed cards, under rules fixed in
research/external/SELECTION_SHADOW_PLAN_v1.md before any result is scored:

- candidates: the favoured side of every priced supplied line, with its probability conditional on a decision;
- two variants, both registered: SHADOW_SIGNAL drops a candidate with NO_DIRECTION (conditional p below 0.55, the
  existing registered boundary), CONTRADICTS_OWN_CENTRE, INCOHERENT_ACROSS_LINES or NO_RESULT_SOURCE; SHADOW_STRICT
  also drops UNMEASURED_AVAILABILITY_PRICED (on the first 12 sealed cards every line carried it, so STRICT issued
  nothing: the comparison measures whether abstaining on unmeasured absences pays);
- at most one candidate per contract: a second label that is the same contract is dropped. "Same contract" uses the
  registered request's definitions (forecast_integrity: period, endpoint, action and unit, so a winner equals a
  half-point handicap only on the deciding score with no draw possible); without them, only an exact repeat of family,
  sides and lines on the card;
- the list holds the highest two remaining by conditional p (label order on ties). It may hold one or none;
- a pair is marked DEPENDENT when both picks are totals or both are handicaps on the same card (nested or shared
  game state), so the joint outcome is reported with that caveat.

Nothing here reaches a card, a seal, a rank or the registered score (ML-SEP-v1 style separation).

    python -m ml.selection_shadow select --intake <intake folder>... --out <folder>
    python -m ml.selection_shadow score --intake <intake folder>... --outcomes <OUTCOMES.csv>... --out <folder>
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from ml import forecast_integrity as F
from ml import one_chat as O

RULE = "SELECT-SHADOW-v1"
PLAN = "research/external/SELECTION_SHADOW_PLAN_v1.md"
MIN_P = 0.55                     # = 0.5 + one_chat.NO_DIRECTION: the boundary already registered for NO_DIRECTION
SIGNAL = ("NO_DIRECTION", "CONTRADICTS_OWN_CENTRE", "INCOHERENT_ACROSS_LINES", "NO_RESULT_SOURCE")
VARIANTS = {"SHADOW_SIGNAL": SIGNAL, "SHADOW_STRICT": SIGNAL + ("UNMEASURED_AVAILABILITY_PRICED",)}
POLICIES = ("REGISTERED_RANK", *VARIANTS)
PICK_FIELDS = ("card_key", "game_id", "sport", "policy", "slot", "label", "family", "side", "line", "p_conditional",
               "pair", "reason")
CHECKPOINT = 100                 # first 100 eligible games, as the registered plan's descriptive checkpoint
COVERAGE_FLOOR = 0.5             # a variant must issue at least half as many picks as the registered ranker
RESAMPLES, SEED = 10000, 20261122
ALPHA_EACH = 0.025               # two variants against one ranker: 0.05 split equally
COMPARE_FIELDS = ("variant", "games", "variant_picks", "rank_picks", "coverage_ratio", "variant_hit_rate", "rank_hit_rate",
                  "difference", "lower", "upper", "verdict")
SCORE_FIELDS = ("policy", "cards", "cards_with_pick", "picks", "wins", "losses", "pushes_or_voids", "unsettled",
                "hit_rate", "pairs", "both_won", "one_won", "neither_won", "dependent_pairs")


def _conditional(rows: list[dict]) -> dict:
    total = {}
    for r in rows:
        if r["p"] not in ("", "UNPRICED"):
            total[r["label"]] = total.get(r["label"], 0.0) + float(r["p"])
    return {(r["label"], r["side"]): float(r["p"]) / total[r["label"]]
            for r in rows if r["p"] not in ("", "UNPRICED") and total.get(r["label"])}


def _label_identities(rows: list[dict], sport: str, contracts: list[dict] | None) -> dict:
    """label -> contract identity. With the registered request's definitions, two labels are one contract exactly when
    forecast_integrity says so (period, endpoint, action and unit included: regulation-time hockey or a handicap on
    another statistic stays distinct). Without them, only an exact repeat of family, sides and lines is one contract."""
    defs, by_label, out = {}, {}, {}
    for c in contracts or []:
        defs.setdefault(c["label"], []).append(c)
    for r in rows:
        by_label.setdefault(r["label"], []).append(r)
    for label, group in by_label.items():
        if label in defs and not F.line_shape_problems(defs[label], ""):
            out[label] = ("REQUEST", F._contract_identity(defs[label], sport))
        else:
            out[label] = ("CARD", group[0]["family"],
                          frozenset((r["side"].upper(), F.line_value(r["line"]) if r["line"] else None) for r in group))
    return out


def load_contracts(keys, root=O.ROOT) -> dict[str, list[dict]]:
    """Each card's registered CONTRACTS.csv, from the seal branch (or local staging); absent keys are left out."""
    out = {}
    for key in keys:
        res = subprocess.run(["git", "-C", str(root), "cat-file", "blob",
                              f"refs/remotes/origin/{O.SEAL_BRANCH}:{F.request_path(key)}/CONTRACTS.csv"], capture_output=True)
        raw = res.stdout if not res.returncode else None
        local = O.request_staging(root) / F.request_path(key) / "CONTRACTS.csv"
        if raw is None and local.exists():
            raw = local.read_bytes()
        if raw is not None:
            out[key] = F.rows(raw)
    return out


def select(picks: list[dict], cards: dict[str, dict], contracts: dict[str, list[dict]] | None = None) -> list[dict]:
    """The shadow list and the registered ranker's top two, for every card, with the reason for each dropped candidate."""
    out = []
    by_card = {}
    for r in picks:
        by_card.setdefault(r["card_key"], []).append(r)
    for key in sorted(by_card):
        rows, sport = by_card[key], cards.get(key, {}).get("sport", "")
        cond = _conditional(rows)
        idents = _label_identities(rows, sport, (contracts or {}).get(key))
        gid = rows[0]["game_id"]
        current = sorted((r for r in rows if r["rank"]), key=lambda r: int(r["rank"]))[:2]
        for slot, r in enumerate(current, start=1):
            out.append(dict(card_key=key, game_id=gid, sport=sport, policy="REGISTERED_RANK", slot=slot, label=r["label"],
                            family=r["family"], side=r["side"], line=r["line"],
                            p_conditional=round(cond.get((r["label"], r["side"]), 0.0), 4), pair="", reason=""))
        favoured = sorted((r for r in rows if r["favoured"] == "Y" and r["p"] != "UNPRICED"),
                          key=lambda r: (-cond.get((r["label"], r["side"]), 0.0), r["label"]))
        for policy, excluding in VARIANTS.items():
            candidates, seen = [], set()
            for r in favoured:
                p = cond.get((r["label"], r["side"]), 0.0)
                why = sorted(set(filter(None, r["flags"].split(";"))) & set(excluding))
                if p < MIN_P and "NO_DIRECTION" not in why:
                    why.append("BELOW_0.55")
                ident = idents[r["label"]]
                if not why and ident in seen:
                    why.append("SAME_CONTRACT_AS_A_HIGHER_PICK")
                if why:
                    out.append(dict(card_key=key, game_id=gid, sport=sport, policy=policy + "_DROPPED", slot="",
                                    label=r["label"], family=r["family"], side=r["side"], line=r["line"],
                                    p_conditional=round(p, 4), pair="", reason=";".join(why)))
                    continue
                seen.add(ident)
                candidates.append((r, p))
            chosen = candidates[:2]
            pair = ""
            if len(chosen) == 2:
                fams = {c[0]["family"] for c in chosen}
                pair = "DEPENDENT" if len(fams) == 1 and fams <= {"TOTAL", "HANDICAP", "TEAM_TOTAL"} else "DISTINCT"
            for slot, (r, p) in enumerate(chosen, start=1):
                out.append(dict(card_key=key, game_id=gid, sport=sport, policy=policy, slot=slot, label=r["label"],
                                family=r["family"], side=r["side"], line=r["line"], p_conditional=round(p, 4), pair=pair,
                                reason=""))
            if not chosen:
                out.append(dict(card_key=key, game_id=gid, sport=sport, policy=policy, slot=0, label="", family="",
                                side="", line="", p_conditional="", pair="", reason="NO_STRONG_PICK"))
    return out


def score(selected: list[dict], outcomes: dict) -> list[dict]:
    """Both policies on the same cards: picks, hit rate, and both/one/neither for cards with two picks."""
    rows = []
    cards = sorted({r["card_key"] for r in selected})
    for policy in POLICIES:
        mine = [r for r in selected if r["policy"] == policy and r["label"]]
        res = dict(policy=policy, cards=len(cards), cards_with_pick=len({r["card_key"] for r in mine}), picks=len(mine),
                   wins=0, losses=0, pushes_or_voids=0, unsettled=0, pairs=0, both_won=0, one_won=0, neither_won=0,
                   dependent_pairs=0)
        by_card = {}
        for r in mine:
            g = outcomes.get((r["card_key"], r["label"], r["side"]), "")
            key = {"WIN": "wins", "LOSS": "losses", "PUSH": "pushes_or_voids", "VOID": "pushes_or_voids"}.get(g, "unsettled")
            res[key] += 1
            by_card.setdefault(r["card_key"], []).append((g, r["pair"]))
        for got in by_card.values():
            if len(got) == 2 and all(g in ("WIN", "LOSS") for g, _ in got):
                res["pairs"] += 1
                won = sum(g == "WIN" for g, _ in got)
                res[("neither_won", "one_won", "both_won")[won]] += 1
                res["dependent_pairs"] += got[0][1] == "DEPENDENT"
        decided = res["wins"] + res["losses"]
        res["hit_rate"] = round(res["wins"] / decided, 4) if decided else ""
        rows.append(res)
    return rows


def compare(selected: list[dict], outcomes: dict, eligible: set[str] | None = None, cards: dict | None = None,
            confirmatory: bool = False) -> list[dict]:
    """The registered decision (SELECTION_SHADOW_PLAN_v1 §4): per-pick hit-rate difference, variant minus registered
    ranker, on the same first CHECKPOINT eligible games, with a game-clustered bootstrap interval.

    Games are taken in the registered scorer's order (scheduled start, game_id, card_key). A verdict is confirmatory
    only with the registered score's eligibility and this plan's publication time; otherwise it is descriptive."""
    import random

    def order(k):
        c = (cards or {}).get(k, {})
        try:
            return (O.T.clock(c["scheduled_start"], "scheduled_start"), c.get("game_id", ""), k)
        except (KeyError, ValueError):
            return (datetime.max.replace(tzinfo=timezone.utc), "", k)

    games = sorted({r["card_key"] for r in selected if eligible is None or r["card_key"] in eligible}, key=order)[:CHECKPOINT]
    per = {}
    for r in selected:
        g = outcomes.get((r["card_key"], r["label"], r["side"]))
        if r["card_key"] in games and r["label"] and r["policy"] in POLICIES and g in ("WIN", "LOSS"):
            w, n = per.setdefault((r["policy"], r["card_key"]), [0, 0])
            per[(r["policy"], r["card_key"])] = [w + (g == "WIN"), n + 1]
    out = []
    for variant in VARIANTS:
        def rate(policy, sample):
            w = sum(per.get((policy, k), [0, 0])[0] for k in sample)
            n = sum(per.get((policy, k), [0, 0])[1] for k in sample)
            return (w / n if n else None), n
        v, nv = rate(variant, games)
        b, nb = rate("REGISTERED_RANK", games)
        lo = hi = None
        if v is not None and b is not None:
            rng, diffs = random.Random(SEED), []
            for _ in range(RESAMPLES):
                sample = [rng.choice(games) for _ in games]
                sv, _ = rate(variant, sample)
                sb, _ = rate("REGISTERED_RANK", sample)
                if sv is not None and sb is not None:
                    diffs.append(sv - sb)
            diffs.sort()
            if diffs:
                lo = diffs[int(len(diffs) * ALPHA_EACH / 2)]
                hi = diffs[min(len(diffs) - 1, int(len(diffs) * (1 - ALPHA_EACH / 2)))]
        ratio = nv / nb if nb else 0.0
        if not confirmatory:
            verdict = "DESCRIPTIVE_INCOMPLETE_INPUTS"
        elif len(games) < CHECKPOINT:
            verdict = f"DESCRIPTIVE_BELOW_{CHECKPOINT}_GAMES"
        elif lo is not None and lo > 0 and ratio >= COVERAGE_FLOOR:
            verdict = "IMPROVEMENT_DEMONSTRATED"
        else:
            verdict = "NOT_DEMONSTRATED"
        out.append(dict(variant=variant, games=len(games), variant_picks=nv, rank_picks=nb, coverage_ratio=round(ratio, 4),
                        variant_hit_rate=round(v, 4) if v is not None else "", rank_hit_rate=round(b, 4) if b is not None else "",
                        difference=round(v - b, 4) if v is not None and b is not None else "",
                        lower=round(lo, 4) if lo is not None else "", upper=round(hi, 4) if hi is not None else "",
                        verdict=verdict))
    return out


def _load(intakes):
    cards, picks = {}, []
    for folder in intakes:
        for c in O.read_csv(Path(folder) / "CARDS.csv"):
            if c["status"] == "ADMITTED":
                cards[c["card_key"]] = c
        picks += [r for r in O.read_csv(Path(folder) / "PICKS.csv")]
    return cards, [r for r in picks if r["card_key"] in cards]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("select")
    s.add_argument("--intake", nargs="+", required=True)
    s.add_argument("--out", required=True, type=Path)
    c = sub.add_parser("score")
    c.add_argument("--intake", nargs="+", required=True)
    c.add_argument("--outcomes", nargs="+", required=True)
    c.add_argument("--coverage", type=Path, help="the registered score's COVERAGE.csv: compare only its eligible games")
    c.add_argument("--registered-at", help="this plan's first verified main publication time: only games sealed after it count")
    c.add_argument("--out", required=True, type=Path)
    args = ap.parse_args(argv)
    if args.out.exists():
        raise SystemExit(f"{args.out} already exists")
    cards, picks = _load(args.intake)
    selected = select(picks, cards, load_contracts(sorted(cards)))
    args.out.mkdir(parents=True)
    (args.out / "SHADOW_PICKS.csv").write_bytes(O.csv_bytes(PICK_FIELDS, selected))
    if args.cmd == "score":
        grades = {}
        for path in args.outcomes:
            for r in O.read_csv(path):
                grades[(r["card_key"], r["label"], r["side"].upper())] = r["grade"].upper()
        (args.out / "SHADOW_SCORE.csv").write_bytes(O.csv_bytes(SCORE_FIELDS, score(selected, grades)))
        eligible = None
        if args.coverage:
            after = O.T.clock(args.registered_at, "registered_at") if args.registered_at else None
            eligible = {r["card_key"] for r in O.read_csv(args.coverage) if r.get("eligible") == "Y"
                        and (after is None or (r.get("seal_time") and O.T.clock(r["seal_time"], "seal_time") > after))}
        confirmatory = bool(args.coverage and args.registered_at)
        (args.out / "SHADOW_COMPARE.csv").write_bytes(O.csv_bytes(COMPARE_FIELDS, compare(
            selected, grades, eligible, cards, confirmatory)))
    print(f"{RULE}: {len({r['card_key'] for r in selected})} cards -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

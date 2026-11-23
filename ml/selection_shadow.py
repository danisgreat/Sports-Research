"""SELECT-SHADOW-v2: a separately registered shadow policy for the top two picks (v29.4, 23 November 2026).

The registered ranker (ONE-CHAT-v3, EVALUATION_PLAN_v29.0) ranks every priced line's favoured side by its stated
probability. It stays frozen and is not changed here. This module computes two other lists from the same sealed cards,
under rules fixed in research/external/SELECTION_SHADOW_PLAN_v2.md before any result is scored. v2 replaces v1, which
reached no eligible game: v1 judged picks one at a time, so a policy that issued one pick per card could pass it.

- One probability throughout: the stated p conditional on a decision, p / (sum of the line's priced sides). The push
  probability (1 minus that sum) and the stated p are shown beside it. The intake's NO_DIRECTION flag, which uses the
  stated p, is not used.
- Candidates: the favoured side of every priced supplied line. SHADOW_SIGNAL drops a candidate below 0.55 (conditional)
  or flagged CONTRADICTS_OWN_CENTRE, INCOHERENT_ACROSS_LINES or NO_RESULT_SOURCE. SHADOW_STRICT also drops
  UNMEASURED_AVAILABILITY_PRICED. A second label that is the same contract, by the registered request's definitions,
  is dropped. The two highest remaining by conditional p are kept; one or none is allowed.
- Every pair (the registered ranker's too) is marked SAME_QUANTITY when the registered definitions put both labels on
  one family, period, endpoint, action and unit, otherwise SAME_GAME. Both are dependent; the direction is unknown.
- The decision (§4 of the plan) is the rate of eligible requests on which a policy issued two distinct picks and both
  won, against the registered ranker on the same games, with a pair-coverage floor fixed in advance.

Nothing here reaches a card, a seal, a rank or the registered score (ML-SEP-v1 style separation).

    python -m ml.selection_shadow select --intake <intake> --out <folder>
    python -m ml.selection_shadow score --intake <intake> --outcomes <OUTCOMES.csv>... --score <registered score folder> --out <folder>
"""
from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

from ml import forecast_integrity as F
from ml import one_chat as O

RULE = "SELECT-SHADOW-v2"
PLAN = O.SHADOW_PLAN             # its first verified main publication is read by O.Repo
MIN_P = 0.55                     # conditional p; the same 0.05 margin as the registered NO_DIRECTION boundary
SIGNAL = ("CONTRADICTS_OWN_CENTRE", "INCOHERENT_ACROSS_LINES", "NO_RESULT_SOURCE")
VARIANTS = {"SHADOW_SIGNAL": SIGNAL, "SHADOW_STRICT": SIGNAL + ("UNMEASURED_AVAILABILITY_PRICED",)}
POLICIES = ("REGISTERED_RANK", *VARIANTS)
CHECKPOINT = 100                 # first 100 eligible requests of the registered sequence
PAIR_COVERAGE_FLOOR = 0.5        # a variant must issue two distinct picks on at least half the eligible requests
RESAMPLES, SEED = 10000, 20261123
ALPHA_EACH = 0.025               # two variants against one ranker: 0.05 split equally
GRADED = ("WIN", "LOSS", "PUSH", "VOID")
PICK_FIELDS = ("card_key", "game_id", "sport", "policy", "slot", "label", "family", "side", "line", "p_stated", "p_push",
               "p_conditional", "pair", "reason")
SCORE_FIELDS = ("policy", "requests", "requests_with_pick", "requests_with_pair", "pair_coverage", "picks", "wins", "losses",
                "pushes_or_voids", "pick_hit_rate", "slot1_hit_rate", "slot2_hit_rate", "pairs_decided", "both_won", "one_won",
                "neither_won", "both_won_per_pair", "both_won_per_request", "same_quantity_pairs")
COMPARE_FIELDS = ("variant", "requests", "variant_both_won", "rank_both_won", "variant_rate", "rank_rate", "difference",
                  "lower", "upper", "variant_pair_coverage", "verdict")


class ShadowError(ValueError):
    pass


def _probabilities(rows: list[dict]) -> dict:
    """(label, side) -> (stated p, push probability of the line, p conditional on a decision)."""
    total = {}
    for r in rows:
        if r["p"] not in ("", "UNPRICED"):
            total[r["label"]] = total.get(r["label"], 0.0) + float(r["p"])
    return {(r["label"], r["side"]): (float(r["p"]), max(0.0, 1.0 - total[r["label"]]), float(r["p"]) / total[r["label"]])
            for r in rows if r["p"] not in ("", "UNPRICED") and total.get(r["label"])}


def _label_identities(rows: list[dict], sport: str, competition: str, contracts: list[dict] | None) -> dict:
    """label -> contract identity. With the registered definitions, two labels are one contract exactly when
    forecast_integrity says so (competition-aware: NPB/KBO baseball can tie). Without them, only an exact repeat."""
    defs, by_label, out = {}, {}, {}
    for c in contracts or []:
        defs.setdefault(c["label"], []).append(c)
    for r in rows:
        by_label.setdefault(r["label"], []).append(r)
    for label, group in by_label.items():
        if label in defs and not F.line_shape_problems(defs[label], ""):
            out[label] = ("REQUEST", F._contract_identity(defs[label], sport, competition))
        else:
            out[label] = ("CARD", group[0]["family"],
                          frozenset((r["side"].upper(), F.line_value(r["line"]) if r["line"] else None) for r in group))
    return out


def _pair(a: dict, b: dict, scopes: dict) -> str:
    sa, sb = scopes.get(a["label"]), scopes.get(b["label"])
    return "SAME_QUANTITY" if sa is not None and sa == sb else "SAME_GAME"


def select(picks: list[dict], cards: dict[str, dict], contracts: dict[str, list[dict]] | None = None) -> list[dict]:
    """The two shadow lists and the registered ranker's top two, for every card, with the reason for each drop."""
    out = []
    by_card = {}
    for r in picks:
        by_card.setdefault(r["card_key"], []).append(r)
    for key in sorted(by_card):
        rows, card = by_card[key], cards.get(key, {})
        sport, competition = card.get("sport", ""), card.get("competition", "")
        prob = _probabilities(rows)
        defs = (contracts or {}).get(key)
        idents, scopes = _label_identities(rows, sport, competition, defs), O.contract_scopes(defs)
        gid = rows[0]["game_id"]

        def row(policy, slot, r, pair="", reason=""):
            ps, push, pc = prob.get((r["label"], r["side"]), (None, None, None)) if r else (None, None, None)
            return dict(card_key=key, game_id=gid, sport=sport, policy=policy, slot=slot,
                        label=r["label"] if r else "", family=r["family"] if r else "", side=r["side"] if r else "",
                        line=r["line"] if r else "", p_stated="" if ps is None else round(ps, 6),
                        p_push="" if push is None else round(push, 6), p_conditional="" if pc is None else round(pc, 4),
                        pair=pair, reason=reason)

        current = sorted((r for r in rows if r["rank"]), key=lambda r: int(r["rank"]))[:2]
        pair = _pair(*current, scopes) if len(current) == 2 else ""
        out += [row("REGISTERED_RANK", n, r, pair) for n, r in enumerate(current, start=1)]
        favoured = sorted((r for r in rows if r["favoured"] == "Y" and (r["label"], r["side"]) in prob),
                          key=lambda r: (-prob[(r["label"], r["side"])][2], r["label"]))
        for policy, excluding in VARIANTS.items():
            chosen, seen = [], set()
            for r in favoured:
                why = sorted(set(filter(None, r["flags"].split(";"))) & set(excluding))
                if prob[(r["label"], r["side"])][2] < MIN_P:
                    why.append("BELOW_0.55_CONDITIONAL")
                if not why and idents[r["label"]] in seen:
                    why.append("SAME_CONTRACT_AS_A_HIGHER_PICK")
                if why:
                    out.append(row(policy + "_DROPPED", "", r, reason=";".join(why)))
                    continue
                seen.add(idents[r["label"]])
                chosen.append(r)
            chosen = chosen[:2]
            pair = _pair(*chosen, scopes) if len(chosen) == 2 else ""
            out += [row(policy, n, r, pair) for n, r in enumerate(chosen, start=1)]
            if not chosen:
                out.append(row(policy, 0, None, reason="NO_STRONG_PICK"))
    return out


def read_grades(paths) -> dict:
    """(card_key, label, side) -> grade. A key graded twice with different grades is refused, never overwritten."""
    grades = {}
    for path in paths:
        for r in O.read_csv(path):
            k, g = (r["card_key"], r["label"], r["side"].upper()), r["grade"].upper()
            if k in grades and grades[k] != g:
                raise ShadowError(f"conflicting grades for {k}: {grades[k]} and {g}")
            grades[k] = g
    return grades


def _per_request(selected: list[dict], grades: dict, keys: list[str], policy: str) -> dict:
    """card_key -> (picks, wins, losses, pushes, pair issued, both won, slot results)."""
    out = {}
    for key in keys:
        mine = sorted((r for r in selected if r["card_key"] == key and r["policy"] == policy and r["label"]),
                      key=lambda r: int(r["slot"]))
        got = [grades.get((key, r["label"], r["side"]), "") for r in mine]
        out[key] = dict(picks=len(mine), got=got, pair=len(mine) == 2, both=len(mine) == 2 and got == ["WIN", "WIN"],
                        same_quantity=bool(mine) and mine[0]["pair"] == "SAME_QUANTITY")
    return out


def score(selected: list[dict], grades: dict, keys: list[str] | None = None) -> list[dict]:
    """Every policy on the same requests: coverage, per-pick and per-slot hit rates, and both/one/neither."""
    keys = keys if keys is not None else sorted({r["card_key"] for r in selected})
    rows = []
    for policy in POLICIES:
        per = _per_request(selected, grades, keys, policy)
        got = [g for v in per.values() for g in v["got"]]
        slot = [[v["got"][i] for v in per.values() if len(v["got"]) > i and v["got"][i] in ("WIN", "LOSS")] for i in (0, 1)]
        decided = [v for v in per.values() if v["pair"] and all(g in ("WIN", "LOSS") for g in v["got"])]
        wins, losses = got.count("WIN"), got.count("LOSS")
        rate = lambda a, b: round(a / b, 4) if b else ""
        rows.append(dict(
            policy=policy, requests=len(keys), requests_with_pick=sum(v["picks"] > 0 for v in per.values()),
            requests_with_pair=sum(v["pair"] for v in per.values()),
            pair_coverage=rate(sum(v["pair"] for v in per.values()), len(keys)), picks=len(got), wins=wins, losses=losses,
            pushes_or_voids=sum(g in ("PUSH", "VOID") for g in got), pick_hit_rate=rate(wins, wins + losses),
            slot1_hit_rate=rate(slot[0].count("WIN"), len(slot[0])), slot2_hit_rate=rate(slot[1].count("WIN"), len(slot[1])),
            pairs_decided=len(decided), both_won=sum(v["both"] for v in decided),
            one_won=sum(v["got"].count("WIN") == 1 for v in decided), neither_won=sum(v["got"].count("WIN") == 0 for v in decided),
            both_won_per_pair=rate(sum(v["both"] for v in decided), len(decided)),
            both_won_per_request=rate(sum(v["both"] for v in per.values()), len(keys)),
            same_quantity_pairs=sum(v["pair"] and v["same_quantity"] for v in per.values())))
    return rows


def compare(selected: list[dict], grades: dict, sequence: list[str], confirmatory: bool) -> list[dict]:
    """The registered decision (SELECTION_SHADOW_PLAN_v2 §4) on the first CHECKPOINT requests of the sequence."""
    games = sequence[:CHECKPOINT]
    for key in games:
        for r in selected:
            if r["card_key"] == key and r["label"] and r["policy"] in POLICIES and grades.get((key, r["label"], r["side"])) not in GRADED:
                raise ShadowError(f"{key} {r['label']} {r['side']}: no grade in the outcome files; every pick of an eligible request must be graded")
    both = {p: {k: v["both"] for k, v in _per_request(selected, grades, games, p).items()} for p in POLICIES}
    pairs = {p: {k: v["pair"] for k, v in _per_request(selected, grades, games, p).items()} for p in POLICIES}
    out = []
    for variant in VARIANTS:
        rate = lambda p, sample: sum(both[p][k] for k in sample) / len(sample) if sample else None
        v, b = rate(variant, games), rate("REGISTERED_RANK", games)
        lo = hi = None
        if games:
            rng, diffs = random.Random(SEED), []
            for _ in range(RESAMPLES):
                sample = [rng.choice(games) for _ in games]
                diffs.append(rate(variant, sample) - rate("REGISTERED_RANK", sample))
            diffs.sort()
            lo = diffs[int(len(diffs) * ALPHA_EACH / 2)]
            hi = diffs[min(len(diffs) - 1, int(len(diffs) * (1 - ALPHA_EACH / 2)))]
        coverage = sum(pairs[variant][k] for k in games) / len(games) if games else 0.0
        if not confirmatory:
            verdict = "DESCRIPTIVE_INPUTS_NOT_VERIFIED"
        elif len(games) < CHECKPOINT:
            verdict = f"DESCRIPTIVE_BELOW_{CHECKPOINT}_REQUESTS"
        elif lo is not None and lo > 0 and coverage >= PAIR_COVERAGE_FLOOR:
            verdict = "IMPROVEMENT_DEMONSTRATED"
        else:
            verdict = "NOT_DEMONSTRATED"
        out.append(dict(variant=variant, requests=len(games), variant_both_won=sum(both[variant][k] for k in games),
                        rank_both_won=sum(both["REGISTERED_RANK"][k] for k in games),
                        variant_rate="" if v is None else round(v, 4), rank_rate="" if b is None else round(b, 4),
                        difference="" if v is None else round(v - b, 4), lower="" if lo is None else round(lo, 4),
                        upper="" if hi is None else round(hi, 4), variant_pair_coverage=round(coverage, 4), verdict=verdict))
    return out


def registered_sequence(score_dir: Path, root=O.ROOT) -> tuple[list[str], str, list[str]]:
    """The eligible sequence of a verified registered score, after this plan's first verified main publication.

    Returns (card keys in the registered order, plan publication time or '', problems). Confirmatory use needs a score
    with zero custody problems and a plan publication time GitHub itself recorded; nothing is taken from the caller."""
    problems = []
    summary = O.read_csv(score_dir / "SUMMARY.csv")[0]
    if summary.get("custody_problems") != "0":
        problems.append(f"the registered score has {summary.get('custody_problems')} custody problems")
    sequence = [r["card_key"] for r in O.read_csv(score_dir / "SEQUENCE.csv")]
    seal_time = {r["card_key"]: r.get("seal_time", "") for r in O.read_csv(score_dir / "COVERAGE.csv")}
    repo = O.Repo(root)
    plan = repo.blob("refs/remotes/origin/main", PLAN)
    commit = repo.first_content(PLAN, O.sha(plan)) if plan is not None else None
    published = repo.pushed_at(commit) if commit else ""
    if not published:
        problems.append(f"{PLAN} has no independently verified main publication time")
        return sequence, "", problems
    after = O.T.clock(published, "plan publication")
    keep = [k for k in sequence if seal_time.get(k) and O.T.clock(seal_time[k], "seal_time") > after]
    return keep, published, problems


def _load(intake: Path):
    cards = {c["card_key"]: c for c in O.read_csv(intake / "CARDS.csv") if c["status"] == "ADMITTED"}
    return cards, [r for r in O.read_csv(intake / "PICKS.csv") if r["card_key"] in cards]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("select")
    s.add_argument("--intake", required=True, type=Path)
    s.add_argument("--out", required=True, type=Path)
    c = sub.add_parser("score")
    c.add_argument("--intake", required=True, type=Path, help="the intake built from every sealed card")
    c.add_argument("--outcomes", nargs="+", required=True)
    c.add_argument("--score", type=Path, help="the registered `ml one-chat score` folder on the same intake and outcomes")
    c.add_argument("--out", required=True, type=Path)
    args = ap.parse_args(argv)
    if args.out.exists():
        raise SystemExit(f"{args.out} already exists")
    cards, picks = _load(args.intake)
    selected = select(picks, cards, {k: v for k in sorted(cards) if (v := O.registered_contracts(k)) is not None})
    args.out.mkdir(parents=True)
    (args.out / "SHADOW_PICKS.csv").write_bytes(O.csv_bytes(PICK_FIELDS, selected))
    if args.cmd == "score":
        grades = read_grades(args.outcomes)
        (args.out / "SHADOW_SCORE.csv").write_bytes(O.csv_bytes(SCORE_FIELDS, score(selected, grades)))
        if args.score:
            sequence, published, problems = registered_sequence(args.score)
        else:
            sequence, published, problems = [], "", ["no registered score folder given"]
        for p in problems:
            print("descriptive only:", p)
        (args.out / "SHADOW_COMPARE.csv").write_bytes(O.csv_bytes(COMPARE_FIELDS, compare(
            selected, grades, sequence, confirmatory=not problems)))
    print(f"{RULE}: {len({r['card_key'] for r in selected})} cards -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

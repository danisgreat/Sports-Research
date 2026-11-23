"""Immutable request contracts and confidence sequences for prospective cards.

Request text is owner evidence, not a reconstructed request or a sporting fact.
The confidence sequence targets the average conditional mean, allowing drift.
"""

from __future__ import annotations

import csv
import hashlib
import io
import math
import re
from pathlib import Path

from ml import timing

REQUEST_ROOT = "research/one_chat/requests"
EVENT_FIELDS = (
    "event_id",
    "sport",
    "competition",
    "home",
    "away",
    "scheduled_start",
    "schedule_source",
)
CONTRACT_FIELDS = (
    "label",
    "family",
    "side",
    "line",
    "period",
    "endpoint",
    "action",
    "unit",
    "request_excerpt",
    "baseline_p",
    "baseline_id",
)
REQUEST_FILES = ("REQUEST.txt", "EVENT.csv", "CONTRACTS.csv")
# Registered in EVALUATION_PLAN_v28.0, now archive/superseded_2026-11-22/research/external/ (v27.0 used eight values from 0.05 to 0.9).
LAMBDAS = (0.5, 0.7, 0.9)
STATISTICAL_RULE = "AVERAGE-CONDITIONAL-MEAN-EB-v2"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def rows(raw):
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))


def csv_bytes(fields, values):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(values)
    return out.getvalue().encode("utf-8")


def request_path(key):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
        raise ValueError("a request needs a safe, stable card key")
    return f"{REQUEST_ROOT}/{key}"


def register_request(source, event, contracts, key, root):
    """Keep the exact owner request and explicit settlement definitions before sealing."""
    folder = Path(root) / request_path(key)
    payload = {
        "REQUEST.txt": Path(source).read_bytes(),
        "EVENT.csv": Path(event).read_bytes(),
        "CONTRACTS.csv": Path(contracts).read_bytes(),
    }
    problems = request_problems(payload)
    if problems:
        raise ValueError(" | ".join(problems))
    payload["MANIFEST.csv"] = csv_bytes(
        ("file", "sha256"),
        [dict(file=name, sha256=digest(payload[name])) for name in REQUEST_FILES],
    )
    if folder.exists():
        if all(
            (folder / name).exists() and (folder / name).read_bytes() == raw
            for name, raw in payload.items()
        ):
            return dict(status="ALREADY_REGISTERED", path=str(folder))
        raise ValueError(
            "a registered request is immutable; use a new key and retain the earlier request"
        )
    # v29.2: a new request must be cardable. An identical earlier registration is still recognised above.
    problems = contract_problems(payload)
    if problems:
        raise ValueError(" | ".join(problems))
    folder.mkdir(parents=True)
    for name, raw in payload.items():
        (folder / name).write_bytes(raw)
    return dict(
        status="REGISTERED",
        path=str(folder),
        contracts=len(rows(payload["CONTRACTS.csv"])),
    )


def request_problems(payload, meta=None, picks=None):
    problems = []
    try:
        text = payload["REQUEST.txt"].decode("utf-8-sig")
        events, contracts = rows(payload["EVENT.csv"]), rows(payload["CONTRACTS.csv"])
        if len(events) != 1 or set(events[0]) != set(EVENT_FIELDS):
            return [
                "request: exactly one EVENT.csv row with the registered columns is required"
            ]
        event = events[0]
        if not all(event.values()) or not (
            ":" in event["event_id"]
            and re.match(r"https?://\S+$", event["schedule_source"])
        ):
            problems.append(
                "request: namespaced native event_id and official schedule_source are required"
            )
        timing.clock(event["scheduled_start"], "request scheduled_start")
        if not contracts or any(set(r) != set(CONTRACT_FIELDS) for r in contracts):
            return problems + [
                "request: explicit contracts with period, endpoint, action, unit and original excerpt are required"
            ]
        seen = set()
        for r in contracts:
            k = (r["label"], r["side"].upper())
            if k in seen or any(
                not r[f].strip()
                for f in CONTRACT_FIELDS
                if f not in ("line", "baseline_p")
            ):
                problems.append("request: duplicate or incomplete contract definition")
            seen.add(k)
            if r["request_excerpt"] not in text:
                problems.append(
                    f"request {r['label']}: excerpt is absent from the unchanged original request"
                )
            line = line_value(r["line"])
            if r["line"].strip() and line is None:
                problems.append(
                    f"request {r['label']}: line must be a number, not {r['line']!r}; "
                    "a moneyline is a WINNER line with the line left empty"
                )
            elif line is not None and abs(line) not in {
                abs(float(x))
                for x in re.findall(r"[-+]?\d+(?:\.\d+)?", r["request_excerpt"])
            }:
                problems.append(
                    f"request {r['label']}: numeric line is absent from its original excerpt"
                )
            base = line_value(r["baseline_p"])
            if r["baseline_p"].strip() and (base is None or not 0 < base < 1):
                problems.append(
                    "request: frozen baseline probability must be between zero and one"
                )
        if meta:
            for f in ("sport", "competition", "home", "away"):
                if event[f] != meta[f]:
                    problems.append(f"request: {f} differs from the card")
            if timing.clock(event["scheduled_start"], "request start") != timing.clock(
                meta["scheduled_start"], "card start"
            ):
                problems.append("request: scheduled start differs from the card")
        if picks is not None:

            def identity(r):
                text = r["line"].strip()
                line = line_value(text) if text else None
                return (
                    r["label"],
                    r["family"],
                    r["side"].upper(),
                    text if line is None and text else line,
                )

            if {identity(r) for r in contracts} != {identity(r) for r in picks} or len(
                contracts
            ) != len(picks):
                problems.append(
                    "request: card omits, adds or changes an original requested contract"
                )
    except (KeyError, ValueError, UnicodeError) as exc:
        problems.append("request: " + str(exc))
    return problems


# v29.2 (CR-2026.11.22-R1). One rule set for the shape of a requested line, run both when a request is registered and
# when its card is checked, so a request that registers can always be carded (an NHL request registered with one side
# per label could never be sealed). Registration also refuses one contract registered twice (P-689 counted one AHL
# result twice). Neither check runs on a request registered earlier: sealed history keeps its original rules.
COMPLETE_SIDES = (
    {"HOME", "AWAY"},
    {"OVER", "UNDER"},
    {"YES", "NO"},
    {"HOME", "AWAY", "DRAW"},
)


def line_value(text):
    """The number a line or probability field holds, or None (empty, text such as 'ML', or not finite)."""
    try:
        x = float(str(text).strip())
    except ValueError:
        return None
    return x if math.isfinite(x) else None


def line_shape_problems(rows, name):
    """Problems with one requested line: every row sharing a label. ``name`` prefixes each message."""
    from ml import picks as P

    family = rows[0]["family"]
    sides = [r["side"].upper() for r in rows]
    if any(r["family"] != family for r in rows) or family not in P.FAMILIES:
        return [name + "one family from the allowed vocabulary per line"]
    if any(s not in P.SIDES[family] for s in sides) or len(set(sides)) != len(sides):
        return [name + f"sides must be distinct and from {'/'.join(P.SIDES[family])}"]
    three_way = family == "WINNER" and "DRAW" in sides
    if len(rows) != (3 if three_way else 2) or set(sides) not in COMPLETE_SIDES:
        return [
            name
            + "both sides of the line are required (HOME/AWAY, OVER/UNDER, YES/NO, or HOME/AWAY/DRAW); "
            f"this line has only {'/'.join(sides)}: add the other side's row under the same label"
        ]
    texts = [r["line"].strip() for r in rows]
    if family == "WINNER" or set(sides) == {"YES", "NO"}:
        if any(texts):
            kind = "winner" if family == "WINNER" else "yes/no"
            return [
                name
                + f"a {kind} row has no line: leave line empty (the excerpt may still say ML)"
            ]
        return []
    bad = [t for t in texts if t and line_value(t) is None]
    if bad:
        return [
            name
            + f"line must be a number, not {bad[0]!r}; a moneyline is a WINNER line with the line left empty"
        ]
    if not all(texts):
        return [name + "a numeric line is required on both rows"]
    lines = [line_value(t) for t in texts]
    if set(sides) == {"HOME", "AWAY"}:
        if abs(lines[0] + lines[1]) > 1e-9:
            return [name + "the two handicap lines must be equal and opposite"]
    elif lines[0] != lines[1]:
        return [name + "both rows carry the same line"]
    return []


# v29.4: baseball draws depend on the competition. MLB plays extra innings to a result; NPB, KBO and other leagues cap
# extra innings and allow ties (RULES_BASEBALL: "Tie-permitting leagues ... never a two-way winner label"). Any
# baseball competition not named here is treated as tie-permitting.
TIE_FREE_BASEBALL = ("MLB", "MAJOR LEAGUE BASEBALL")


def no_draw(sport, rows, competition=""):
    """True when a full-game result can never be a draw: basketball and tennis always (overtime and tie-breaks
    decide), ice hockey when the contract includes the shootout, MLB baseball when it includes extra innings."""
    if not all(r["period"].upper().startswith("FULL") for r in rows):
        return False
    text = " ".join(
        r[f] for r in rows for f in ("period", "endpoint", "action")
    ).upper()
    if "REGULATION" in text:
        return False
    if sport in ("Basketball", "Tennis"):
        return True
    if sport == "Ice Hockey":
        return bool(re.search(r"(?<![A-Z])SO(?![A-Z])|SHOOTOUT", text))
    comp = (competition or "").upper()
    return (
        sport == "Baseball"
        and "EXTRA" in text
        and any(
            re.search(rf"(?<![A-Z]){name}(?![A-Z])", comp) for name in TIE_FREE_BASEBALL
        )
    )


# The score that decides the match, when it is also a handicap's unit. Not tennis: a match is decided by sets, and a
# games spread can lose while the match is won (0-6 7-6 7-6 is a match win and a 14-18 games count).
WINNER_SCORE = {"Basketball": "POINTS", "Ice Hockey": "GOALS", "Baseball": "RUNS"}


def winner_by_margin(sport, rows, competition=""):
    """True when a half-point handicap on these rows settles exactly as the match winner: no draw is possible and
    every handicap row is on the score that decides the match (points; goals including the shootout goal; runs)."""
    unit = WINNER_SCORE.get(sport)
    handicaps = [r for r in rows if r.get("family", "HANDICAP") == "HANDICAP"]
    return (
        bool(unit)
        and no_draw(sport, rows, competition)
        and all(r["unit"].strip().upper() == unit for r in handicaps)
    )


def _contract_identity(rows, sport, competition=""):
    family = rows[0]["family"]
    sides = frozenset((r["side"].upper(), line_value(r["line"])) for r in rows)
    scope = frozenset(
        (r["period"].upper(), r["endpoint"].upper(), r["action"].upper()) for r in rows
    )
    two_way = {s for s, _ in sides} == {"HOME", "AWAY"}
    half = family == "HANDICAP" and all(
        v is not None and abs(v) == 0.5 for _, v in sides
    )
    if two_way and (
        (family == "WINNER" and no_draw(sport, rows, competition))
        or (half and winner_by_margin(sport, rows, competition))
    ):
        return "MATCH_WINNER", scope
    return family, sides, scope, frozenset(r["unit"].upper() for r in rows)


def contract_problems(payload):
    """Registration-only checks on a new request: every line is cardable and no contract is registered twice."""
    try:
        events, contracts = rows(payload["EVENT.csv"]), rows(payload["CONTRACTS.csv"])
        sport, competition = events[0]["sport"], events[0].get("competition", "")
    except (KeyError, IndexError, UnicodeError):
        return []  # request_problems has already reported a malformed request
    by_label = {}
    for r in contracts:
        by_label.setdefault(r["label"], []).append(r)
    problems, first = [], {}
    for label, group in by_label.items():
        shape = line_shape_problems(group, f"request {label}: ")
        if shape:
            problems += shape
            continue
        key = _contract_identity(group, sport, competition)
        if key not in first:
            first[key] = label
        elif key[0] == "MATCH_WINNER":
            problems.append(
                f"request {first[key]} and {label}: the same two-way contract twice. No draw is possible here, so a "
                "moneyline and either side's +0.5 or -0.5 all settle as 'this side wins'; register it once, as one "
                "WINNER label with a HOME row and an AWAY row (line empty), each row keeping its own excerpt"
            )
        else:
            problems.append(
                f"request {first[key]} and {label}: the same contract twice; register it once"
            )
    return problems


def log_mean_exp(values):
    top = max(values)
    return top + math.log(sum(math.exp(v - top) for v in values) / len(values))


def confidence_path(ds, alpha=0.05):
    """Predictable empirical-Bernstein mixture, Howard et al. (2021), Theorem 4.

    X=d+0.75 lies in [0,1]. For any predictable forecast xhat in [0,1],
    exp(lambda*sum(X-E[X|past]) - psi(lambda)*sum((X-xhat)**2)) is a
    nonnegative supermartingale, psi=-log(1-lambda)-lambda. A fixed mixture
    yields a lower CS for the *current* average conditional mean. Past
    crossings are not used as a lower bound for a later, different mean.
    Reference: https://arxiv.org/abs/1810.08240, Theorem 4 and Appendix A.8.
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between zero and one")
    total, variance, result = 0.0, 0.0, []
    threshold = math.log(1 / alpha)
    for n, d in enumerate(ds, 1):
        if not math.isfinite(d) or not -0.75 <= d <= 0.25:
            raise ValueError("game advantage must be finite and within [-0.75, 0.25]")
        # One pseudo-observation at d=0; only earlier games determine this forecast.
        forecast = 0.75 + total / n
        variance += (d + 0.75 - min(max(forecast, 0), 1)) ** 2
        total += d

        def log_e(m):
            return log_mean_exp(
                [
                    lam * (total - n * m) - (-math.log1p(-lam) - lam) * variance
                    for lam in LAMBDAS
                ]
            )

        lo, hi = -0.75, min(0.25, total / n)
        if log_e(lo) < threshold:
            bound = -0.75
        else:
            for _ in range(45):
                mid = (lo + hi) / 2
                if log_e(mid) >= threshold:
                    lo = mid
                else:
                    hi = mid
            bound = lo
        le = log_e(0)
        result.append(
            dict(
                game=n,
                bet="MIXTURE",
                e_value=math.exp(min(le, 700)),
                mean_d=total / n,
                lower_bound_95=bound,
            )
        )
    return result


POWER_SCENARIOS = (
    ("MEAN_ZERO_NULL", None),
    ("COIN_RESULTS_CARD_STATES_55_75", (0.55, 0.75)),
    ("CALIBRATED_FAVOURED_55_65", (0.55, 0.65)),
    ("CALIBRATED_FAVOURED_58_72", (0.58, 0.72)),
    ("CALIBRATED_FAVOURED_62_78", (0.62, 0.78)),
)


def _simulated_game(rng, scenario, band):
    """One game's d: two supplied lines; the card states p on its favoured side."""
    if band is None:
        return rng.choice((0.15, -0.15))
    out = []
    for _ in range(2):
        p = rng.uniform(*band)
        truth = 0.5 if scenario.startswith("COIN") else p
        out.append(0.25 - (p - (1 if rng.random() < truth else 0)) ** 2)
    return sum(out) / 2


def first_crossing(ds, *, alpha=0.05, practical=0.01, horizon=None):
    """First game at which the evidence reaches 1/alpha with mean d at least the practical threshold."""
    total = 0.0
    for i, r in enumerate(confidence_path(ds, alpha)):
        total += ds[i]
        if horizon is not None and i >= horizon:
            return None
        if r["e_value"] >= 1 / alpha and total / (i + 1) >= practical:
            return i + 1
    return None


def power_study(
    *, horizon, runs=200, null_runs=400, seed=20261117, alpha=0.05, practical=0.01
):
    """Deterministic simulation of the registered decision (Python's random module, fixed seed)."""
    import random

    rows = []
    for n, (scenario, band) in enumerate(POWER_SCENARIOS):
        rng = random.Random(seed + n)
        count = null_runs if band is None else runs
        hits = []
        for _ in range(count):
            ds = [_simulated_game(rng, scenario, band) for _ in range(horizon)]
            hit = first_crossing(ds, alpha=alpha, practical=practical, horizon=horizon)
            if hit:
                hits.append(hit)
        hits.sort()
        rows.append(
            dict(
                scenario=scenario,
                runs=count,
                horizon=horizon,
                lambdas=" ".join(str(x) for x in LAMBDAS),
                demonstrated_within_400=sum(h <= 400 for h in hits),
                demonstrated_within_horizon=len(hits),
                share_within_horizon=round(len(hits) / count, 4),
                median_crossing_game=hits[len(hits) // 2] if hits else "",
                seed=seed + n,
            )
        )
    return rows

"""Account for every historical card without turning retrospective checks into forecasts.

python -m ml.evidence_status --training research/card_training/2026-11-16-1 --out NEW_FOLDER
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

from ml import forecast_integrity as F


def historical_summary(training):
    training = Path(training)
    source = training / "ROWS.csv"
    records = F.rows(source.read_bytes())
    cards = defaultdict(list)
    for row in records:
        cards[row["card"]].append(row)
    admitted = [r for r in records if r["admission"] != "EXCLUDED"]
    probabilistic = [r for r in admitted if r["admission"] == "PROBABILISTIC"]
    # Do not infer eligibility from the newer name of an older row's admission class.
    if not probabilistic:
        probabilistic = [r for r in admitted if r["p"] and r["p"].lower() != "nan"]
    p_cards = {r["card"] for r in probabilistic}
    summary = dict(
        historical_cards=len(cards),
        historical_contract_rows=len(records),
        admitted_contract_rows=len(admitted),
        probability_rows=len(probabilistic),
        outcome_only_rows=len(admitted) - len(probabilistic),
        probability_cards=len(p_cards),
        excluded_contract_rows=len(records) - len(admitted),
        historical_evidence_class="HISTORICAL_OUTCOME_EXPOSED_STUDY",
        current_method_application="VALIDATION_ONLY_NOT_RETROACTIVE_ISSUANCE",
        prospective_evidence_class="SEPARATE_SEALED_REGISTERED_SEQUENCE",
        input_sha256=F.digest(source.read_bytes()),
    )
    study = training / "SCORES.csv"
    pair = (
        next(
            (
                r
                for r in F.rows(study.read_bytes())
                if r["model"] == "cal_identity" and r["baseline"] == "outcome_base_rate"
            ),
            {},
        )
        if study.exists()
        else {}
    )
    summary["historical_study_verdict"] = (
        "POSITIVE_HISTORICAL_ASSOCIATION"
        if pair and float(pair["interval_high"]) < 0
        else "NO_CLEAR_HISTORICAL_ASSOCIATION"
    )
    summary["historical_comparator_cards"] = pair.get("cards", 0)
    summary["historical_brier_difference"] = pair.get("card_mean_brier_difference", "")
    summary["historical_difference_low"] = pair.get("interval_low", "")
    summary["historical_difference_high"] = pair.get("interval_high", "")
    audit = []
    for card, rows in sorted(cards.items(), key=lambda kv: int(kv[0].split("-")[-1])):
        valid = [r for r in rows if r["admission"] != "EXCLUDED"]
        priced = [r for r in valid if r["p"] and r["p"].lower() != "nan"]
        audit.append(
            dict(
                card=card,
                rows=len(rows),
                admitted_rows=len(valid),
                probability_rows=len(priced),
                original_cohorts=";".join(sorted({r["cohort"] for r in rows})),
                original_eras=";".join(sorted({r["era"] for r in rows})),
                disposition="HISTORICAL_RESEARCH_RETAINED",
                prospective_admission="NOT_INFERRED_FROM_LATER_RULE_CHECKS",
                provenance="ORIGINAL_SOURCE_REFERENCES_PRESERVED",
                missing_feature_reason="NO_ONECHAT_FACTS_PACKET_LINKED_IN_CARD_TRAIN_DATASET",
            )
        )
    exclusions = [
        dict(reason=reason, rows=n)
        for reason, n in sorted(
            Counter(
                r["reason"] for r in records if r["admission"] == "EXCLUDED"
            ).items()
        )
    ]
    return summary, audit, exclusions


def typed_features(intakes, root):
    """Keep raw values, point-in-time lineage, units and missingness for training.

    This dataset is a research-feature candidate, never a forecast or model promotion.
    The issuer's missing values remain missing; no hindsight imputation is performed.
    """
    from ml import one_chat as O

    dictionary_path = Path(root) / O.DICTIONARY
    if not dictionary_path.exists():
        dictionary_path = O.ROOT / O.DICTIONARY
    dictionary = F.rows(dictionary_path.read_bytes())
    vocab = {(r["sport"], r["feature"]): r for r in dictionary}
    features, issues, coverage = [], [], []
    seen = set()
    for folder in intakes:
        problems = O.verify_intake(folder, root, require_committed=False)
        if problems:
            raise ValueError(" | ".join(problems))
        cards = {
            r["card_key"]: r
            for r in O.read_csv(Path(folder) / "CARDS.csv")
            if r["status"] == "ADMITTED"
        }
        for key, c in cards.items():
            if key in seen:
                raise ValueError("duplicate feature packet for " + key)
            seen.add(key)
            coverage.append(
                dict(
                    card_key=key,
                    game_id=c["game_id"],
                    sport=c["sport"],
                    competition=c["competition"],
                    facts_required=c["facts_required"],
                    facts_observed=c["facts_observed"],
                    admission="RESEARCH_FEATURE_CANDIDATE_NOT_CERTIFIED",
                )
            )
        for r in O.read_csv(Path(folder) / "FACTS.csv"):
            c = cards.get(r["card_key"])
            if c is None:
                continue
            spec = vocab.get(
                (c["sport"], r["field"]), vocab.get(("TEAM_SPORT", r["field"]))
            )
            issue = ""
            missing = r["value"] == "MISSING"
            if spec is None:
                issue = "UNKNOWN_FEATURE_DEFINITION"
            elif missing and not r["source"].strip():
                issue = "MISSING_REASON_REQUIRED"
            elif not missing:
                unit = spec["unit"]
                if unit not in ("players", "text", "category"):
                    try:
                        x = float(r["value"])
                        if (
                            not math.isfinite(x)
                            or (unit == "0/1" and x not in (0, 1))
                            or ("percent" in unit and not 0 <= x <= 100)
                        ):
                            issue = "VALUE_OUTSIDE_DEFINITION"
                    except ValueError:
                        issue = "NON_NUMERIC_VALUE_FOR_NUMERIC_FEATURE"
            row = dict(
                card_key=r["card_key"],
                game_id=r["game_id"],
                sport=c["sport"],
                competition=c["competition"],
                side=r["side"],
                feature=r["field"],
                value="" if missing else r["value"],
                unit=spec["unit"] if spec else "UNKNOWN_DEFINITION",
                window=spec["window"] if spec else "UNKNOWN_DEFINITION",
                status="MISSING" if missing else "OBSERVED",
                missing_reason=r["source"] if missing else "",
                source_url="" if missing else r["source"],
                known_at=r["observed_at"],
                admission="EXCLUDED"
                if issue
                else "MISSING_RETAINED"
                if missing
                else "FEATURE_CANDIDATE",
                reason=issue,
                source_intake=str(folder),
            )
            features.append(row)
            if issue:
                issues.append(
                    dict(card_key=r["card_key"], field=r["field"], reason=issue)
                )
    return features, issues, coverage


def write_table(path, rows, fallback):
    path.write_bytes(F.csv_bytes(tuple(rows[0]) if rows else fallback, rows))


def build(training, out, *, intakes=(), root=None):
    from ml.one_chat import ROOT

    root = Path(root or ROOT)
    out = Path(out)
    if out.exists():
        raise ValueError("evidence reports are immutable; choose a new output folder")
    summary, audit, exclusions = historical_summary(training)
    features, issues, coverage = typed_features(intakes, root)
    summary.update(
        feature_candidate_rows=sum(
            r["admission"] == "FEATURE_CANDIDATE" for r in features
        ),
        feature_missing_rows=sum(r["status"] == "MISSING" for r in features),
        feature_issue_rows=len(issues),
    )
    out.mkdir(parents=True)
    write_table(out / "SUMMARY.csv", [summary], ("historical_cards",))
    write_table(out / "HISTORICAL_CARD_AUDIT.csv", audit, ("card",))
    write_table(out / "EXCLUSIONS.csv", exclusions, ("reason", "rows"))
    write_table(
        out / "FEATURES.csv", features, ("card_key", "feature", "value", "admission")
    )
    write_table(out / "FEATURE_ISSUES.csv", issues, ("card_key", "field", "reason"))
    write_table(out / "FEATURE_COVERAGE.csv", coverage, ("card_key",))
    scores = Path(training) / "SCORES.csv"
    if scores.exists():
        (out / "HISTORICAL_STUDY_SCORES.csv").write_bytes(scores.read_bytes())
    (out / "REPORT.md").write_text(
        f"# Historical evidence and prospective admission\n\n"
        f"All **{summary['historical_cards']} historical cards** are accounted for: "
        f"{summary['historical_contract_rows']} contract rows, {summary['admitted_contract_rows']} admitted, "
        f"{summary['probability_rows']} with stated probabilities and {summary['outcome_only_rows']} outcome-only. "
        f"{summary['excluded_contract_rows']} are excluded with reasons in EXCLUSIONS.csv.\n\n"
        "These records are used in CARD-TRAIN-v1. Their original probabilities, cohorts and source references remain intact. "
        "The copied historical study scores are outcome-exposed evidence, not a prospective verdict. "
        "Applying a new validator after a result does not establish that its rules or probabilities were frozen before that result. "
        "A missing probability, original request, native identity or publication timestamp is never manufactured.\n\n"
        "Prospective advantage is decided separately from the complete registered request/seal sequence. "
        "No current-method eligibility is inferred from a historical card count. Recoverable historical custody can be audited "
        "as an explicitly labelled historical cohort; a later rule is never backdated.\n\n"
        "FEATURES.csv preserves sport-specific definitions, raw values, sources, known-at times and missingness. "
        "It is a research-feature candidate store; fitted models remain shadow studies. The old cards' unsaved research "
        "is recorded as an explicit gap in HISTORICAL_CARD_AUDIT.csv, not filled from post-result pages.\n",
        encoding="utf-8",
    )
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--training", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--intake", nargs="*", type=Path, default=())
    args = parser.parse_args(argv)
    print(
        json.dumps(build(args.training, args.out, intakes=args.intake), sort_keys=True)
    )


if __name__ == "__main__":
    main()

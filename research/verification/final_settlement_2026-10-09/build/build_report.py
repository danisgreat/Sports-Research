"""Render REPORT.md for the 2026-10-09 final settlement from its table, summary and apply receipt."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path

BUILD = Path(__file__).resolve().parent
OUT = BUILD.parent
spec = importlib.util.spec_from_file_location('settle', BUILD / 'build_settlement.py')
settle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(settle)
G = {'W': 'W', 'L': 'L', 'P': 'P', 'V': 'V'}


def main():
    table = json.loads((OUT / 'settlement_table.json').read_text(encoding='utf-8'))
    summary = json.loads((OUT / 'summary.json').read_text(encoding='utf-8'))
    receipt = json.loads((OUT / 'apply_receipt.json').read_text(encoding='utf-8'))
    t = summary['totals']
    lines = [
        '# Final settlement of all pending records — 2026-10-09',
        '',
        '**Directive (user, 2026-10-09).** Settle every pending log. Where details cannot be found, settle anyway. Any record holding only '
        'a temporary ID takes the next canonical ID in chronological order. Only the top two ranked picks can count as a win, '
        'and a Rank-1 failure requires a deep, thorough retrospection.',
        '',
        '## Outcome',
        '',
        f"- **Records settled:** {table and len(table['records'])}: the 65 records of the 2026-10-08 carryover register plus P-550–P-556. "
        'No sporting settlement obligation remains open.',
        "- **IDs:** none consumed. Every `TMP-`/`LOCAL-` alias in the repository already maps to a canonical P-ID, so no record needed a new one. "
        f"Next canonical ID before and after: **{receipt['next_id_before']} → {receipt['next_id_after']}**.",
        f"- **Log writes:** `{receipt['active_log']}` grew {receipt['log_before_bytes']:,} → {receipt['log_after_bytes']:,} bytes, append-only "
        '(the prefix was verified byte-identical). One consolidated block holds 50 records: P-126–P-522, which have no ledger parent, and P-538–P-549, '
        'whose rollover verifier pins exactly twelve ledger addenda. The other 22 ledger cards (P-523–P-537, P-550–P-556) '
        f"each received a dated addendum through `research.operations.log_card`, adding {receipt['ledger_records_added']} ledger records.",
        f"- **Top-two result (71 forecast cards):** {t['counted_wins']} counted wins from {t['counted_live_rows']} live top-two rows "
        f"({t['counted_wins'] / t['counted_live_rows']:.1%}). Rank 1: {t['rank1_W']} W / {t['rank1_L']} L / {t['rank1_V']} VOID. "
        f"Rank 2: {t['rank2_W']} W / {t['rank2_L']} L / {t['rank2_V']} VOID. Card classes: {t['TOP2_ALL_WON']} all won, {t['TOP2_SPLIT']} split, "
        f"{t['TOP2_ALL_LOST']} all lost, {t['VOID']} void. Hit@2 {t['hit_at_2']}/{t['cards'] - t['VOID']}.",
        f"- **Deep Rank-1 retrospections:** {len(summary['rank1_failures'])}, one in each failed record's settlement.",
        '- **Evidence grades (313 rows):** ' + ', '.join(f"{k} {v}" for k, v in sorted(summary['evidence_counts'].items())) + '.',
        '- **Certification:** unchanged. Every record remains `NOT_CERTIFIED` and performance-ineligible. This is a research-ledger closure, '
        'not operator certification.',
        '',
        '## Settle-anyway evidence hierarchy',
        '',
        '| Code | Meaning |',
        '|---|---|',
    ]
    for k, v in table['evidence_codes'].items():
        lines.append(f'| {k} | {v} |')
    lines += [
        '',
        'Framework defaults applied under OP: a missing operator definition does not block sporting settlement (CURRENT_RULES); '
        "a tennis retirement voids games rows (RULES_TENNIS); runs scored before a stop count (RULES_CRICKET); the card's own frozen "
        'full-match working assumption for hockey totals (P-200).',
        '',
        '## Corrections found while settling',
        '',
        '- **Rank-index `P` literal.** Five rows coded `P` (push) in `GAME_PREDICTION_RANK_LOG.csv` are blank-contract corner rows, '
        'not pushes: P-407 R1 (WIN), P-409 R2 (WIN), P-410 R5 (WIN), P-419 R5 (LOSS), P-430 R5 (LOSS). They are settled from their '
        'original settlement tables. The CSV itself is unchanged (it is a frozen learning artefact).',
        "- **Copied R1 blocks.** The Part 6 settlement-refresh \"R1. Original prediction\" text for P-539–P-545 repeats P-538's ranking. "
        "Each card's own rank table governs; the final settlement uses each card's actual ranks.",
        '- **P-519.** The original 50–22 settlement was fabricated. The AFLW owner final is 69–39 (total 108), so Rank 1 (Under 89.5) is a LOSS.',
        '- **P-136 and P-540.** Both retired mid-match. All game rows are VOID under the framework retirement convention, and both winner calls are correct.',
        '- **P-418.** The original ranked contracts are not preserved anywhere in the repository or its history, so the card is VOID. '
        'The single-secondary final, Drukpa 1–3 RTC, is recorded.',
        '- **Stale reservation.** The 2026-10-08 register still lists P-550 as `LOCAL_ONLY_PENDING_IMPORT`. It was imported on 2026-10-09; '
        '`register.json` here records it as resolved.',
        '',
        '## Register pointer',
        '',
        '`research/current_settlement_register.json` still selects the hash-pinned 2026-10-08 register. `verify_rollover` requires '
        '`event_count == 65`, and `verify_carryover_review` requires the selection to equal its own snapshot, so moving the pointer needs '
        'verifier code changes. Under the user instruction that improvements are laid out but not implemented, those changes are left as '
        "GOV-01 in `FRAMEWORK_RETROSPECTIVE_2026-10-09.md`. This folder's `register.json` supersedes the old register for sporting settlement.",
        '',
        '## Per-record result',
        '',
        '| ID | Event | R1 | R2 | Counted | Card class | Winner call | Deep R1 retro |',
        '|---|---|:-:|:-:|---|---|---|:-:|',
    ]
    for r in table['records']:
        pr = summary['per_record'][r['id']]
        lines.append(f"| {r['id']} | {r['event']} | {pr['rank1']} | {pr['rank2']} | {pr['counted_wins']}/{pr['counted_live_rows']} | "
                     f"{pr['card_outcome']} | {pr['winner_call']} | {'yes' if pr['rank1'] == 'L' and pr['card_outcome'] != 'NO_FORECAST' else '—'} |")
    lines += [
        '',
        '## Files',
        '',
        '| File | Role |',
        '|---|---|',
        '| `settlement_table.json` | Every row: grade, evidence code and basis (the settlement source of truth) |',
        '| `summary.json` | Derived diagnostics (`build/build_settlement.py`) |',
        '| `register.json` | Final settlement register (all 72 closed; certification unchanged) |',
        '| `apply_receipt.json` | Before/after hashes, ledger growth, next ID |',
        '| `build/rank1_retrospectives.py` | The 28 deep Rank-1 retrospections |',
        '| `build/tennis_overdispersion_check.py` | Reproduction of the P-551/P-555 tennis distributions with and without match-level variance |',
        '| `build/build_addenda.py`, `build/apply_settlement.py`, `build/build_report.py` | Rendering, application and this report |',
        '| `build/requests/`, `build/sources/`, `build/older_block.md` | Exact appended bodies (22 ledger addenda; 50-record consolidated block) |',
        '',
        'Reproduce the analysis: `python -B research/verification/final_settlement_2026-10-09/build/build_settlement.py`, then `build_addenda.py` '
        '(rendering is deterministic). `apply_settlement.py` is the one-time writer and refuses to run unless the next ID is P-557 '
        'and no transaction is pending.',
        '',
    ]
    (OUT / 'REPORT.md').write_text('\n'.join(lines), encoding='utf-8')
    print('REPORT.md written')


if __name__ == '__main__':
    main()

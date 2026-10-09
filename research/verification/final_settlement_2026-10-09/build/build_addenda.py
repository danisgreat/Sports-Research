"""Render final-settlement addenda from settlement_table.json and the Rank-1 retrospections.

Outputs (all under build/):
  sources/<ID>.final_settlement.txt   exact addendum body for each ledger-addendum card
  requests/<ID>.addendum.json         log_card addendum requests for those cards (P-523..P-537, P-550..P-556)
  older_block.md                      one consolidated block for P-126..P-522 (no ledger parent) and
                                      P-538..P-549 (verify_rollover pins exactly 12 addenda for these IDs)
  register.json                       final settlement register (all 72 records)
Pure rendering: no ledger or log writes. Apply with apply_settlement.py.
"""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path

BUILD = Path(__file__).resolve().parent
OUT = BUILD.parent
ROOT = OUT.parents[2]
STAMP = '2026-10-09'
LEDGER_FIRST = 523
# verify_rollover.py:37 requires exactly 12 ledger addenda for the P-538..P-549 import, so their
# final settlements are recorded in the consolidated block instead of as second ledger addenda.
ROLLOVER_PINNED = {f'P-{n}' for n in range(538, 550)}

spec = importlib.util.spec_from_file_location('retro', BUILD / 'rank1_retrospectives.py')
retro = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retro)
spec = importlib.util.spec_from_file_location('settle', BUILD / 'build_settlement.py')
settle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(settle)

GRADE = {'W': 'WIN', 'L': 'LOSS', 'P': 'PUSH', 'V': 'VOID'}
EVID = {'A': 'A owner', 'B': 'B structured', 'C': 'C best-available', 'E': 'E estimated bound',
        'OP': 'OP default rule', 'X': 'X no data'}
OUTCOME = {'TOP2_ALL_WON': 'every live top-two row WON', 'TOP2_SPLIT': 'one of the two live top-two rows WON',
           'TOP2_ALL_LOST': 'every live top-two row LOST', 'VOID': 'no live top-two row (VOID card)',
           'NO_FORECAST': 'no forecast was issued; shadow order only, not counted'}


def number(pid):
    return int(pid.split('-')[1])


def body(r):
    outcome, wins, live = settle.card_outcome(r)
    rank = {row[0]: row for row in r['rows']}
    lines = [f"**Final settlement ({STAMP}) — {r['event']} ({r['competition']}).** Settled under the user's "
             f"{STAMP} directive: every pending record is settled, with missing details settled on the best "
             "available evidence; only Rank 1 and Rank 2 can count as wins; a Rank-1 failure carries a deep "
             "retrospection. The original forecast, probabilities and ranks are unchanged where they were first logged.",
             '',
             f"**Final event.** {r['final']}.",
             '',
             '| Rank | Proposition | Grade | Counts toward wins? | Evidence | Basis |',
             '|---:|---|---|---|---|---|']
    for rk, contract, grade, evidence, basis in r['rows']:
        counted = ('YES' if grade == 'W' else 'NO (loss)' if grade == 'L' else 'NO (void/push)') if rk in (1, 2) \
            else 'NO (rank 3+ informational)'
        if r.get('no_forecast'):
            counted = 'NO (no forecast issued)'
        if rk == 0:
            counted = 'NO (contract not preserved)'
        lines.append(f"| {rk if rk else '—'} | {contract} | **{GRADE[grade]}** | {counted} | {EVID[evidence]} | {basis} |")
    lines += ['', f"**Top-two result.** {outcome}: {OUTCOME[outcome]} — **{wins} counted win(s) of {live} live top-two row(s)**."
              f" Rank 1: {GRADE[rank[1][2]] if 1 in rank else 'VOID'}; Rank 2: {GRADE[rank[2][2]] if 2 in rank else 'VOID'}.",
              f"**Winner call.** {r['winner_call'][0]}: {r['winner_call'][1]}.",
              '**Disposition.** `FINAL_SETTLED_2026-10-09`; the sporting carryover obligation is closed. Performance '
              'certification is unchanged (`NOT_CERTIFIED`, performance-ineligible): settlement under the directive is '
              'a research-ledger closure, not operator certification.']
    if r.get('no_forecast'):
        lines += ['', '**No forecast was issued**, so the shadow order is graded for learning only. No counted win, '
                  'no counted loss, and no mandatory retrospection; the existing Part 6 retrospective stands.']
    elif 1 in rank and rank[1][2] == 'L':
        lines += ['', '**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**', '', retro.R[r['id']].strip()]
    elif 1 in rank and rank[1][2] == 'W':
        lines += ['', '**Rank 1 won**, so no mandatory deep retrospection is triggered.']
    else:
        lines += ['', '**Rank 1 was VOID**, so there is no performance result and no mandatory deep retrospection.']
    return '\n'.join(lines) + '\n'


def register(records):
    return {
        'schema_version': 1,
        'created': STAMP,
        'status': 'ALL_PENDING_RECORDS_FINAL_SETTLED',
        'supersedes_for_sporting_settlement': 'research/verification/carryover_review_2026-10-08/carryover.json (65) and '
                                              'research/verification/settled_import_2026-10-09/UNRESOLVED_POST_IMPORT.md (7)',
        'selected_pointer_unchanged': 'research/current_settlement_register.json still pins the 2026-10-08 register because '
                                      'verify_rollover/verify_carryover_review require that exact snapshot; see REPORT.md.',
        'event_count': len(records),
        'open_sporting_settlements': 0,
        'certification': 'NOT_CERTIFIED for every record; performance_eligible false; unchanged by this settlement',
        'local_reservations': [],
        'stale_reservation_resolved': 'P-550 LOCAL_ONLY_PENDING_IMPORT was imported canonically on 2026-10-09; next canonical ID P-557',
        'temporary_ids': 'All TMP-/LOCAL- aliases in the repository map to canonical IDs; none required a new ID.',
        'records': [{'canonical_id': r['id'], 'event': r['event'], 'state': 'FINAL_SETTLED_2026-10-09',
                     'card_outcome': settle.card_outcome(r)[0], 'counted_wins': settle.card_outcome(r)[1],
                     'counted_live_rows': settle.card_outcome(r)[2], 'deep_rank1_retrospection': r['id'] in retro.R,
                     'performance_eligible': False} for r in records],
    }


def main():
    data = json.loads((OUT / 'settlement_table.json').read_text(encoding='utf-8'))
    records = data['records']
    settle.validate(records)
    failures = [r['id'] for r in records if not r.get('no_forecast')
                and {row[0]: row for row in r['rows']}.get(1, [0, 0, 'V'])[2] == 'L']
    assert sorted(failures) == sorted(retro.R), (sorted(set(failures) ^ set(retro.R)))
    (BUILD / 'sources').mkdir(exist_ok=True)
    (BUILD / 'requests').mkdir(exist_ok=True)
    older = []
    for r in records:
        text = body(r)
        if number(r['id']) >= LEDGER_FIRST and r['id'] not in ROLLOVER_PINNED:
            src = BUILD / 'sources' / f"{r['id']}.final_settlement.txt"
            src.write_bytes(text.encode('utf-8'))
            req = {'card_id': r['id'], 'body': text, 'source_path': str(src)}
            (BUILD / 'requests' / f"{r['id']}.addendum.json").write_text(json.dumps(req, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        else:
            older.append((r, text))
    summary = json.loads((OUT / 'summary.json').read_text(encoding='utf-8'))
    t = summary['totals']
    head = [
        '',
        '<!-- BEGIN FINAL SETTLEMENT 2026-10-09 -->',
        f'## Final settlement of all pending records — {STAMP}',
        '',
        f'**Scope.** All {len(records)} records still carrying a sporting settlement obligation: the 65 records of '
        '`research/verification/carryover_review_2026-10-08/carryover.json` and P-550–P-556 from the 2026-10-09 import. '
        'This is settled under the user directive of 2026-10-09: settle everything; where details cannot be found, settle anyway; '
        'only Rank 1 and Rank 2 can count as wins; every Rank-1 failure gets a deep retrospection. '
        'Original forecasts, probabilities and ranks are unchanged. No canonical ID is consumed; the next canonical ID stays **P-557**. '
        'No pending record carried an unassigned temporary ID: every `TMP-`/`LOCAL-` alias already maps to a canonical P-ID.',
        '',
        '**Settle-anyway hierarchy.** (A) owner/official field; (B) structured provider or multi-source agreement; '
        '(C) best-available single, secondary or provisional evidence adopted as final; (E) estimate from a partial measurement '
        'that bounds the field, with confidence stated; (OP) sporting endpoint known but operator rule absent, so the card\'s own '
        'frozen working assumption or the framework default applies (CURRENT_RULES: a missing operator definition does not block '
        'sporting settlement; RULES_TENNIS: a retirement voids games rows; RULES_CRICKET: runs scored before a stop count); '
        '(X) no admissible data, so the row is VOID.',
        '',
        f"**Cohort result under the top-two rule** (71 forecast cards; P-532 was a no-forecast intake): "
        f"**{t['counted_wins']} counted wins from {t['counted_live_rows']} live top-two rows "
        f"({t['counted_wins'] / t['counted_live_rows']:.1%})**; Rank 1 {t['rank1_W']} W / {t['rank1_L']} L / {t['rank1_V']} VOID "
        f"({t['rank1_W'] / (t['rank1_W'] + t['rank1_L']):.1%} of live); Rank 2 {t['rank2_W']} W / {t['rank2_L']} L / {t['rank2_V']} VOID; "
        f"cards with both top rows won {t['TOP2_ALL_WON']}, split {t['TOP2_SPLIT']}, both lost {t['TOP2_ALL_LOST']}, void {t['VOID']}; "
        f"Hit@2 {t['hit_at_2']}/{t['cards'] - t['VOID']}. Winner calls {t['winner_CORRECT']} correct / {t['winner_INCORRECT']} incorrect "
        f"({t['winner_NOT_AUDITED']} not recoverable). Ranks 3+ are recorded as informational only.",
        '',
        f"**Rank-1 failures with deep retrospection ({len(failures)}):** " + ', '.join(failures) + '. '
        'Recurring failure classes (a record can carry more than one): first-half-goal over-selection (P-148, P-234, P-250, P-342, P-377); '
        'baseball +1.5 cushion ceiling (P-274, P-524, P-544, P-547); basketball totals without a pace model (P-527, P-548, P-553); '
        'tennis score-tree under-dispersion or dependence (P-541, P-551, P-555); rank by q instead of p (P-519, P-521, P-522); '
        'dependent top two sharing one driver (P-176, P-492, P-541, P-549, P-555). Full analysis: `research/verification/final_settlement_2026-10-09/REPORT.md` and `FRAMEWORK_RETROSPECTIVE_2026-10-09.md`.',
        '',
        f"**Records settled in this block ({len(older)}).** P-126–P-522 have no research-ledger parent. P-538–P-549 are canonical ledger cards, "
        'but `verify_rollover` pins exactly twelve addenda for that import, so their final settlements are recorded here by canonical ID '
        'instead of as second ledger addenda. P-523–P-537 and P-550–P-556 are settled by individual dated ledger addenda that follow.',
        '',
    ]
    blocks = []
    for r, text in older:
        blocks += [f"### Final settlement · {r['id']} · {r['event']}", '', text.rstrip(), '']
    tail = ['<!-- END FINAL SETTLEMENT 2026-10-09 -->', '']
    (BUILD / 'older_block.md').write_bytes('\n'.join(head + blocks + tail).encode('utf-8'))
    (OUT / 'register.json').write_text(json.dumps(register(records), indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'ledger_addenda': len(records) - len(older), 'older_block_records': len(older),
                      'deep_retrospections': len(failures)}, indent=1))


if __name__ == '__main__':
    main()

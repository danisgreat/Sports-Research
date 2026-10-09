"""mini-log-3: one distribution, the Rank-1 gate, adjustments, contract capture, evidence snapshots, decision block (PRD/GOV/SRC)."""
from pathlib import Path

import pytest

from research.operations import card_validator, mini_log

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / 'research/prompts/examples'
ACTIVE = (EXAMPLES / 'EXAMPLE_ACTIVE_MINI.md').read_bytes()
SETTLED = (EXAMPLES / 'EXAMPLE_SETTLED_MINI.md').read_bytes()
LEGACY = ROOT / 'research/prompts/examples/legacy_mini_log_2'


def errors_for(text):
    return mini_log.analyse(text.encode('utf-8'))['errors']


def test_golden_v3_examples_are_clean_and_settle():
    report = mini_log.analyse(ACTIVE)
    assert report['version'] == 3 and report['errors'] == [] and report['warnings'] == []
    assert [c['id'] for c in report['cards']] == ['P-900', 'P-901']
    settled = mini_log.analyse_settled(ACTIVE, SETTLED)
    assert settled['errors'] == [] and settled['warnings'] == []
    assert settled['table']['summary']['totals']['counted_wins'] == 2
    first = report['cards'][0]['picks'][0]
    assert first['status'] == 'FROM_DISTRIBUTION:hockey_poisson_ot_v1' and first['p_card'] == pytest.approx(0.771)


def test_legacy_v2_minis_still_validate_without_the_v3_checks():
    legacy = (LEGACY / 'EXAMPLE_ACTIVE_MINI.md').read_bytes()
    report = mini_log.analyse(legacy)
    assert report['version'] == 2 and report['errors'] == []
    assert mini_log.analyse_settled(legacy, (LEGACY / 'EXAMPLE_SETTLED_MINI.md').read_bytes())['errors'] == []


def mutate(old, new, count=1):
    text = ACTIVE.decode('utf-8')
    assert old in text, old
    return text.replace(old, new, count)


@pytest.mark.parametrize('old,new,message', [
    ('- **Distribution object:** `hockey_poisson_ot_v1`', '- **Distribution:** `hockey_poisson_ot_v1`', 'Distribution object'),
    ('FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Combined λ 5.8; both', 'UNCALIBRATED_ANALYST_SCENARIO | Combined λ 5.8; both', 'FROM_DISTRIBUTION:hockey_poisson_ot_v1'),
    ('FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Close chance quality', 'FROM_DISTRIBUTION:other_model | Close chance quality', 'one declared distribution'),
    ('**Rank-1 gate:** PASS — p_card 77.1%', '**Rank-1 gate:** RANK1_UNSTABLE — p_card 77.1%', 'give PASS'),
    ('**Rank-1 gate:** RANK1_UNSTABLE — p_card 68.2%', '**Rank-1 gate:** PASS — p_card 68.2%', 'give RANK1_UNSTABLE'),
    ('p_card 77.1%; best', 'p_card 71.0%; best', 'differs from the pick table'),
    ('**Rank-1 gate:** PASS — p_card 77.1%; best non-complementary alternative 68.2%; margin 8.9 points\n', '', 'Rank-1 gate'),
    ('**Adjustment dependence:** NONE\n**Supplied rows not selected:** Over 6.5', '**Supplied rows not selected:** Over 6.5', 'Adjustment dependence'),
    ('**Adjustments:** NONE', '', 'Adjustments'),
    ('- **Retirement rule:** `N/A`', '- **Retirement rule:** `whatever`', 'Retirement rule must be'),
    ('- **Capture due:** `2026-10-11T11:00:00+11:00`', '- **Capture due:** `2026-10-09T11:00:00+11:00`', 'after the scheduled start'),
    ('- **Capture due:** `2026-10-11T11:00:00+11:00`', '- **Capture due:** `tomorrow`', 'ISO 8601'),
    ('sha256:', 'sha1:', 'Evidence snapshots item'),
    ('- **Regime flags:** `NONE`', '- **Regime flags:** `BIG_GAME`', 'unknown regime flag'),
    ('| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Over 6.5) | Total goals Over 5.5 — full game incl. OT/SO | 52.2% | FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Combined λ 5.8 sits at the line',
     '| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Over 6.5) | Total goals Over 5.5 — full game incl. OT/SO | 52.2% | FROM_DISTRIBUTION:hockey_poisson_ot_v1 | TO_FILL', 'TO_FILL'),
    ('### Decision block', '### Summary', 'Decision block'),
    ('### Appendix\n\n#### A1. Identity, timing and state\n\nNative event `EX-0001`', '### Notes\n\n#### A1. Identity, timing and state\n\nNative event `EX-0001`', 'Appendix'),
])
def test_v3_rule_violations(old, new, message):
    errors = errors_for(mutate(old, new))
    assert any(message in e for e in errors), errors


def test_a_q_column_beside_p_is_an_error_on_v3_cards():
    text = mutate('### Appendix\n\n#### A1.', '### Appendix\n\n| Rank | Proposition | p | q |\n|---|---|---|---|\n| 1 | A | 0.60 | 0.70 |\n\n#### A1.')
    assert any('P_AND_Q_COLUMNS' in e for e in errors_for(text))


def test_oversized_decision_block_is_rejected_and_a_long_one_warns():
    padding = ' evidence' * 700
    text = mutate('Combined λ 5.8; both starters confirmed', 'Combined λ 5.8;' + padding)
    assert any('decision block is' in e and 'limit' in e for e in errors_for(text))
    medium = mutate('Combined λ 5.8; both starters confirmed', 'Combined λ 5.8;' + ' evidence' * 110)
    report = mini_log.analyse(medium.encode('utf-8'))
    assert report['errors'] == [] and any('decision block is' in w for w in report['warnings'])


def test_large_adjustment_requires_the_unadjusted_ranking_and_correct_dependence_label():
    table = ('**Adjustments:**\n\n| Name | Target | Size | SD units | Prior basis |\n|---|---|---|---|---|\n'
             '| kobe_shift | margin | -4.75 | 0.32 | analyst_judgement |\n')
    base = mutate('**Adjustments:** NONE', table)
    assert any('Unadjusted top two' in e for e in errors_for(base))
    same = base.replace('**Adjustment dependence:** NONE\n**Supplied rows not selected:** Over 6.5',
                        '**Adjustment dependence:** NONE\n**Unadjusted top two:** Total goals Under 7.5 — full game incl. OT/SO; Northfield Owls +1.5 — full game incl. OT/SO\n'
                        '**Supplied rows not selected:** Over 6.5', 1)
    assert errors_for(same) == []
    flipped = same.replace('**Unadjusted top two:** Total goals Under 7.5 — full game incl. OT/SO; Northfield', '**Unadjusted top two:** Northfield Owls +1.5 — full game incl. OT/SO; Total goals Under 7.5 — full game incl. OT/SO; Northfield', 1)
    assert any('label ADJUSTMENT_DEPENDENT' in e for e in errors_for(flipped))
    labelled = same.replace('**Adjustment dependence:** NONE', '**Adjustment dependence:** ADJUSTMENT_DEPENDENT', 1)
    assert any('equals the picks' in e for e in errors_for(labelled))
    no_big = mutate('**Adjustment dependence:** NONE\n**Supplied rows not selected:** Over 6.5', '**Adjustment dependence:** ADJUSTMENT_DEPENDENT\n**Supplied rows not selected:** Over 6.5')
    assert any('requires an adjustment above 0.25 SD' in e for e in errors_for(no_big))


def test_family_rules_fire_inside_a_card():
    text = ACTIVE.decode('utf-8').replace('`Ice hockey`', '`Baseball`', 1).replace('Northfield Owls +1.5 — full game incl. OT/SO | 68.2%', 'Northfield Owls +1.5 — full game incl. OT/SO | 68.2%')
    # a Rank-1 +1.5 below 65% on a baseball card is refused
    text = text.replace('Total goals Under 7.5 — full game incl. OT/SO | 77.1%', 'Northfield Owls +1.5 — full game incl. OT/SO | 64.0%', 1).replace('p_card 77.1%', 'p_card 64.0%', 1)
    assert any('baseball_plus_1_5' in e for e in errors_for(text))


def test_capture_window_warning_for_late_capture():
    text = mutate('- **Capture due:** `2026-10-11T11:00:00+11:00`', '- **Capture due:** `2026-10-14T11:00:00+11:00`')
    report = mini_log.analyse(text.encode('utf-8'))
    assert report['errors'] == [] and any('Capture due is' in w for w in report['warnings'])


def test_no_snapshot_warns_and_new_minis_are_v3():
    text = ACTIVE.decode('utf-8')
    line = next(l for l in text.splitlines() if l.startswith('- **Evidence snapshots:**') and 'example goalie' not in l and '@2026-10-10T08:41' in l)
    report = mini_log.analyse(text.replace(line, '- **Evidence snapshots:** `NONE`', 1).encode('utf-8'))
    assert report['errors'] == [] and any('no pregame evidence snapshot' in w for w in report['warnings'])
    assert mini_log.FORMAT_TAG.endswith('mini-log-3 -->')
    assert card_validator.decision_block(text) is not None

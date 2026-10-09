import json
from pathlib import Path

from research.operations import cohort_review, mini_log

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / 'research/prompts/examples'


def test_real_repository_cohort_matches_final_settlement():
    cards, sources = cohort_review.load_tables(ROOT)
    result = cohort_review.review(cards, 'P-126', 'P-556')
    totals = result['summary']['totals']
    assert (totals['counted_wins'], totals['counted_live_rows']) == (79, 134)
    assert result['slot_comparison']['rank1']['W'] == 40 and result['slot_comparison']['rank1']['L'] == 28
    assert len(result['rank1_failures']) == 28
    assert result['summary']['rank1_failure_classes']['FIRST_HALF_GOAL_OVERSELECTION'] == 5
    assert 'TOP_ROW_DEPENDENCE' not in result['summary']['rank1_failure_classes']
    assert any(s['schema'] == 'final-settlement-1' for s in sources)


def test_latest_settlement_wins_and_mini_tables_carry_calibration(tmp_path):
    frozen = (EXAMPLES / 'EXAMPLE_ACTIVE_MINI.md').read_bytes()
    settled = (EXAMPLES / 'EXAMPLE_SETTLED_MINI.md').read_bytes()
    table = mini_log.analyse_settled(frozen, settled)['table']
    folder = tmp_path / 'research/verification/mini_import_example'; folder.mkdir(parents=True)
    (folder / 'settlement_table.json').write_text(json.dumps(table), encoding='utf-8')
    cards, sources = cohort_review.load_tables(tmp_path)
    assert sorted(cards) == ['P-900', 'P-901'] and sources[0]['records'] == 2
    result = cohort_review.review(cards)
    assert result['calibration']['n'] == 8
    assert result['slot_comparison']['ranks3plus'] == {'W': 4, 'L': 0, 'win_rate': 1.0,
                                                       'ci95': result['slot_comparison']['ranks3plus']['ci95']}
    report = cohort_review.render(result, sources)
    assert '| Rank 1 (pick) | 1–1 |' in report and 'VARIANCE' in report
    # Joint failure: P-900 stated 9.3%, P-901 stated 0.0%; neither lost both picks.
    joint = result['joint_failure_check']
    assert joint['cards'] == 2 and abs(joint['mean_stated'] - 0.0465) < 1e-9 and joint['realised_all_lost'] == 0.0
    assert result['rank1_stability']['stable']['W'] == 1 and result['rank1_stability']['stable']['L'] == 1
    assert result['rank1_stability']['unstable']['W'] == 0
    assert 'Reliability line' in report and 'Joint top-two failure' in report


def test_reliability_line_is_identity_for_perfect_calibration():
    from research.operations import top_two
    rows = [(1, 'W', 0.8, 'x')] * 8 + [(1, 'L', 0.8, 'x')] * 2 + [(1, 'W', 0.4, 'x')] * 4 + [(1, 'L', 0.4, 'x')] * 6
    cal = top_two.calibration([{'rows': rows}])
    assert abs(cal['reliability_slope'] - 1.0) < 1e-12 and abs(cal['reliability_intercept']) < 1e-12

"""Settlement lint (GOV-03): R1 must match the card, and a blank contract is never a push."""
from pathlib import Path


from research.operations import mini_log, settlement_lint

ROOT = Path(__file__).resolve().parents[2]
PART6, PART7 = ROOT / 'prediction logs/PREDICTION_LOG_COMBINED_6.md', ROOT / 'prediction logs/PREDICTION_LOG_COMBINED_7.md'
EXAMPLES = ROOT / 'research/prompts/examples'


def test_replay_flags_p539_to_p545_and_nothing_else_in_that_range():
    found = settlement_lint.scan_addenda([PART6, PART7])
    flagged = sorted(int(k[2:]) for k in found if 538 <= int(k[2:]) <= 556)
    assert flagged == [539, 540, 541, 542, 543, 544, 545]
    assert any('copy-paste' in f for f in found['P-541'])
    assert any('reads' in f and 'Panthers ML' in f for f in found['P-543'])
    assert 'P-538' not in found                                             # the card the text was copied from is itself consistent


def test_the_active_log_is_clean():
    assert settlement_lint.scan_addenda([PART7]) == {}


def test_five_blank_contract_pushes_are_found_and_new_ones_are_not_hidden(tmp_path):
    every = settlement_lint.lint_rank_log(include_known=True)
    assert sorted((b['card'], b['rank']) for b in every) == [('P-407', '1'), ('P-409', '2'), ('P-410', '5'), ('P-419', '5'), ('P-430', '5')]
    assert all(b['should_read'] == 'UNKNOWN_CONTRACT' and b['known_historical'] for b in every)
    assert settlement_lint.lint_rank_log() == []
    rows = (ROOT / 'GAME_PREDICTION_RANK_LOG.csv').read_text(encoding='utf-8-sig').splitlines()
    header = rows[0].split(',')
    extra = {h: '' for h in header}
    extra.update(card_id='P-999', rank='1', logged_result='P')
    import csv
    path = tmp_path / 'rank.csv'
    with open(path, 'w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=header)
        writer.writeheader()
        writer.writerow(extra)
    new = settlement_lint.lint_rank_log(path)
    assert len(new) == 1 and new[0]['card'] == 'P-999' and new[0]['known_historical'] is False


def test_r1_check_accepts_matching_and_unspecific_text_and_rejects_foreign_rankings():
    table = {1: 'Total goals Under 7.5 — full game incl. OT/SO', 2: 'Northfield Owls +1.5 — full game incl. OT/SO'}
    assert settlement_lint.check_r1('Ranks as issued above; uncalibrated analyst scenario; PREGAME.', table) == []
    assert settlement_lint.check_r1('Rank 1 Total goals Under 7.5; Rank 2 Northfield Owls +1.5.', table) == []
    wrong = settlement_lint.check_r1('Rank 1 Panthers ML; Rank 2 full-game Over 5.5.', table)
    assert len(wrong) == 2 and 'Panthers ML' in wrong[0]
    assert settlement_lint.check_r1('Rank 5 Something', table) == ['R1 names rank 5 but the card has no such row']


def test_mini_settlement_rejects_an_r1_copied_from_another_card():
    active, settled = (EXAMPLES / 'EXAMPLE_ACTIVE_MINI.md').read_bytes(), (EXAMPLES / 'EXAMPLE_SETTLED_MINI.md').read_bytes()
    assert mini_log.analyse_settled(active, settled)['errors'] == []
    text = settled.decode('utf-8')
    own = '**R1. Original prediction.** Rank 1 Total goals Under 7.5 (full game incl. OT/SO) at p_card 77.1%; Rank 2 Northfield Owls +1.5 (full game incl. OT/SO) at 68.2%; uncalibrated analyst scenario; PREGAME.'
    assert own in text
    bad = text.replace(own, '**R1. Original prediction.** Rank 1 Panthers ML; Rank 2 full-game Under 5.5; Rank 3 Kings ML.', 1)
    errors = mini_log.analyse_settled(active, bad.encode('utf-8'))['errors']
    assert any(e.startswith('P-900: R1:') for e in errors), errors


def test_card_propositions_reads_legacy_and_mini_tables():
    legacy = "| Rank | Exact proposition | p_card |\n|---|---|---:|\n| **1** | **COMBINED TOTAL UNDER 171.5 points** | **57.63%** |\n| **2** | **Kobe Storks +6.5 points** | **54.37%** |\n"
    assert settlement_lint.card_propositions(legacy) == {1: 'COMBINED TOTAL UNDER 171.5 points', 2: 'Kobe Storks +6.5 points'}
    assert settlement_lint.card_propositions('no table') == {}

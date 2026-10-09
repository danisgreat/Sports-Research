"""Tests for the generated current-state page (GOV-05)."""
from research.operations import current_state as cs


def test_stale_pattern_catches_next_id_and_destination_statements():
    for line in ('the next ID stays P-557.', 'canonical next ID P-550 and local next P-551', 'P-550 remains next and no ID was consumed',
                 'Part 6 is the sole canonical destination for new issued cards', 'Part 7 is now active; nothing else'):
        assert cs.STALE.search(line), line
    for line in ('Read the current next ID from the ledger-backed workflow and status register.', 'Cards from P-557 onward move through six prompts.',
                 'The first working ID is the larger of the repository next canonical ID and the previous mini highest + 1.'):
        assert not cs.STALE.search(line), line


def test_render_is_deterministic_and_carries_the_live_facts():
    first, second = cs.render(), cs.render()
    assert first == second
    facts = cs.facts()
    assert facts['next_id'] in first and facts['manifest'] in first and facts['method'] in first
    assert first.endswith('\n') and '\r' not in first


def test_the_committed_page_is_fresh_and_living_documents_state_no_next_id():
    assert cs.verify() == []

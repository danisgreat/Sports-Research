"""Current custody readback including research cards and imported receipt schema.

The adapter verifies alternate receipt bytes in memory; original receipts and
the four pinned model dependency files are never rewritten.
"""
import json
from pathlib import Path
from research.src import acceptance
from research.src.sources import verified_body
from research.src.ledger import read_records
from research.src.issue import CANONICAL_LEDGER, PART6
from research.operations.log_card import research_cards, verify_projection, next_id

def compatible_body(receipt, root):
    if 'response_sha256' not in receipt and 'content_sha256' in receipt:
        receipt={**receipt,'response_sha256':receipt['content_sha256'],
                 'body_path':receipt['stored_snapshot_path'], 'source_url':receipt.get('url')}
    return verified_body(receipt, root)

def run():
    # The frozen acceptance command expects the original collector schema.
    acceptance.verified_body=compatible_body
    result=acceptance.run()
    cards=research_cards(read_records(CANONICAL_LEDGER))
    for card in cards:verify_projection(card,PART6)
    result['checks'].update(canonical_research_cards=[c['card_id'] for c in cards],
                           research_next_id=next_id(), receipt_schema_adapter='IN_MEMORY_ONLY_NO_SOURCE_REWRITES')
    result['limitation']+=' Research IDs are canonical storage identities, not certified prospective ISSUE records.'
    return result

if __name__=='__main__':
    result=run();print(json.dumps(result,indent=2));raise SystemExit(not result['valid'])

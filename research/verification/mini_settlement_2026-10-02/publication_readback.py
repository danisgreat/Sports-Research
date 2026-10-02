"""Verify the publication projection and retain the post-append checks."""
import hashlib,json,subprocess
from pathlib import Path
from datetime import datetime,timezone
from research.src.issue import PART6,CANONICAL_LEDGER,_custody
from research.operations.log_card import next_id
from research.operations.verify_custody import compatible_body
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
prepared=json.loads((OUT/'publication_prepared.json').read_text())
formatted=json.loads((OUT/'publication_format_revision.json').read_text())
raw,_=_custody(PART6);before=prepared['part6_before_bytes']
assert sha(raw[:before])==prepared['part6_before_sha256']
assert raw[before:]==(OUT/'combined_projection_formatted.bin').read_bytes()
assert sha(raw)==formatted['part6_after_sha256'] and next_id()=='P-527'
assert sha(CANONICAL_LEDGER.read_bytes())==prepared['ledger_sha256']
mini_receipt=json.loads((OUT/'append_receipt.json').read_text())
assert sha(Path(mini_receipt['mini_path']).read_bytes())==mini_receipt['final_sha256']
commands=json.loads((OUT/'publication/command_results.json').read_text());assert len(commands)==8
for r in commands:assert sha((OUT/'publication'/r['output_path']).read_bytes())==r['output_sha256']
validation=ROOT/'Previous Sports Results/_canonical/validation.json'
(OUT/'publication/archive_validation_generated.json').write_bytes(validation.read_bytes())
old=subprocess.check_output(['git','show',prepared['base_git_commit']+':Previous Sports Results/_canonical/validation.json'],cwd=ROOT)
validation.write_bytes(old);assert validation.read_bytes()==old
source_count=0
for p in (ROOT/'research/data/source_receipts').glob('*.json'):
    compatible_body(json.loads(p.read_text(encoding='utf-8')),ROOT);source_count+=1
assert source_count==75
tests=(OUT/'publication/tests.output.txt').read_text()
assert '2 failed, 113 passed' in tests
freeze=(OUT/'publication/freeze.output.txt').read_text();assert '374 files; 20 mismatches' in freeze
canonical=json.loads((OUT/'publication/canonical_log.output.txt').read_text());assert canonical['next_id']=='P-527'
archive=json.loads((OUT/'publication/archive.output.txt').read_text());assert len(archive['issues'])==461
assert not subprocess.run(['git','diff','--check'],cwd=ROOT,capture_output=True).returncode
stamp=datetime.now(timezone.utc).isoformat()
result=dict(observed_utc=stamp,exact_existing_part6_prefix_preserved=True,part6_before_bytes=before,
    part6_before_sha256=prepared['part6_before_sha256'],part6_after_sha256=sha(raw),
    displayed_original_forecasts_preserved=True,source_mini_bytes_unchanged=True,
    original_frozen_part6_block_verified=True,canonical_ledger_unchanged=True,canonical_next_id='P-527',
    source_bodies_verified=source_count,canonical_card_check='PASS',workflow_status_score='PASS',
    tests='113 passed, 2 existing pinned-model failures',freeze='FAIL: existing 20 mismatches',
    custody_acceptance='FAIL: existing missing retained historical manifests',archive='FAIL: existing 461 input hash mismatches',
    archive_validation_file_restored=True,git_diff_check='PASS',performance_admission_unchanged=True,
    canonical_ids_added=0,publication_intent='User requested commit and push to main; final remote-SHA verification follows')
(OUT/'publication_readback.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
note=f'''

## Later user-authorized combined-log append and main publication — {stamp}

The earlier no-combined-log-append/no-Git-publication statements in this report, original mini, receipts and inventory describe the preceding local audit. The user subsequently explicitly requested “append and push this there then”. This dated section supersedes those administrative statements for the new work, without rewriting forecast or outcome custody.

Part 6 now contains the original mini forecast exhibit and all four twelve-part retrospective addenda, within an explicitly labelled LOCAL MINI DIAGNOSTIC AUDIT block. Original source bytes remain in the custody exhibits. Display headings are prefixed “Local reservation” to prevent the legacy next-ID reader from consuming local P-labels; blank-quote/hard-break display whitespace is formatted without altering original source files. [Publication preparation](publication_prepared.json), [append receipt](publication_append_receipt.json), [display-format revision](publication_format_revision.json) and [final readback](publication_readback.json) bind each step. The living status register has an append-only reference pointer.

All **{before:,} pre-existing Part 6 bytes** remain exactly unchanged, including the frozen 141,740-byte original block and existing P-523–P-526 projections. The canonical ledger is unchanged and **next canonical ID remains P-527**. This is diagnostic reference publication, not canonical ID allocation or certified settlement. Four formal outcome sets remain unresolved and P-528 remains the unplayed carryover at the original audit observation. The Downloads mini remains unchanged by this publication step and is not archived.

Checks were rerun after the combined-log append; [publication/command_results.json](publication/command_results.json) records exact commands/timestamps/exit codes and exact retained output hashes. Canonical projection, workflow status/score, all 75 source bodies, original prefix/source block and final diff checks pass. The full suite repeats **113 passed / 2 failed** on the pre-existing pinned `research/src/control_manifest.py` mismatch. Custody and acceptance repeat the missing retained manifest failure; freeze repeats 20 mismatches; archive repeats 461 indexed input-hash mismatches. These failures were not concealed, repaired by new hashes or reclassified as passes. Archive validation's generated output is retained in the publication audit and its existing file restored exactly.

Publication scope: Part 6, the living status-register pointer, this settlement audit directory and the two approved MLB raw bodies/two source receipts. The 17 mixed web-tool extract files remain ignored/local under the benchmark quarantine, with their hashes in the source audit; no market-bearing tool dump is published. No model, sport rule, source registry, control freeze, archive result CSV or original forecast file is changed. Git publication will be verified against the actual remote main SHA after committing; this pre-commit report does not itself assert a completed push. The final chat reports that verified commit.
'''
with (OUT/'REPORT.md').open('ab') as f:f.write(note.encode('utf-8'))
files=[dict(path=p.relative_to(ROOT).as_posix(),bytes=len(p.read_bytes()),sha256=sha(p.read_bytes())) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='publication_inventory.json']
(OUT/'publication_inventory.json').write_text(json.dumps(dict(observed_utc=stamp,files=files,
    report_scope='Supersedes earlier local-only file inventory for this later publication step'),indent=2)+'\n',encoding='utf-8')
print('Publication readback PASS; inherited full-check failures retained; ready to stage explicitly')

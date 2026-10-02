"""Project the requested diagnostic audit into Part 6 without assigning IDs."""
import hashlib,json,os,re,subprocess
from pathlib import Path
from datetime import datetime,timezone
from research.src.ledger import locked,read_records
from research.src.issue import PART6,CANONICAL_LEDGER,_custody
from research.operations.log_card import next_id,pending

OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def put(n,v):
    with (OUT/n).open('x',encoding='utf-8') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def append(path,raw):
    with path.open('ab') as f:f.write(raw);f.flush();os.fsync(f.fileno())

stamp=datetime.now(timezone.utc).isoformat()
receipt=json.loads((OUT/'append_receipt.json').read_text())
mini=Path(receipt['mini_path']);source=mini.read_bytes()
original=(OUT/'original_mini_evidence.txt').read_bytes()
addendum=(OUT/'settlement_addendum.txt').read_bytes()
assert source==original+addendum and sha(source)==receipt['final_sha256']
assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='main'
assert subprocess.check_output(['git','rev-list','--left-right','--count','origin/main...HEAD'],cwd=ROOT,text=True).strip()=='0\t0'
begin='<!-- BEGIN LOCAL MINI DIAGNOSTIC AUDIT 2026-10-02 -->'
end='<!-- END LOCAL MINI DIAGNOSTIC AUDIT 2026-10-02 -->'
# Plain P-ID headings are parsed by the legacy next-ID reader even inside fences.
# Give reference headings an explicit LOCAL prefix, without changing source bytes.
projection_text=re.sub(r'(?m)^(#{1,6}) (P-\d+\b)',r'\1 Local reservation \2',addendum.decode('utf-8'))
quoted='\n'.join('> '+line for line in original.decode('utf-8').splitlines())
intro=f'''\n\n{begin}
## October 2 local-mini settlement audit — published reference addendum

Appended to this combined log at **{stamp}** following the user's explicit instruction to append and push. This section contains the original retained mini forecast exhibit and the four diagnostic settlement/retrospective addenda. It is a **LOCAL RESERVATION / LEARNING-ONLY reference audit**, not new canonical issuance. P-527 through P-531 below remain source labels; no IDs are allocated or renumbered and the canonical next ID remains P-527. The earlier user instruction forbidding allocation merely for settlement remains in force.

The five source events and their graded rows are not duplicates of canonical P-523–P-526. Their missing full cards/operator terms and certification gaps are unchanged. In particular P-528 remains the unplayed carryover at the original audit time, and P-531 remains a provisional secondary final. No new sporting observations are introduced by publication.

Historical status/queue/publication statements inside the retained exhibit and October 2 addendum describe their original observation times. This new publication note supersedes the earlier statement that no combined-log append or Git publication was performed: the addendum is now projected here and publication is requested. Successful Git publication is established by the final remote-SHA check, not by this note alone.

The original exhibit is quoted for display. The original 7,831 bytes and exact retrospective append remain in [original_mini_evidence.txt](../research/verification/mini_settlement_2026-10-02/original_mini_evidence.txt) and [settlement_addendum.txt](../research/verification/mini_settlement_2026-10-02/settlement_addendum.txt), with the [append receipt](../research/verification/mini_settlement_2026-10-02/append_receipt.json), [four chained diagnostic revisions](../research/verification/mini_settlement_2026-10-02/diagnostic_revisions.jsonl) and [audit report](../research/verification/mini_settlement_2026-10-02/REPORT.md). Display headings use “Local reservation” so the legacy ID reader cannot mistake them for issued cards. Original source hashes/forecasts are unchanged.

### Original retained forecast exhibit — historical source text

{quoted}

### Retained settlement and retrospective projection
'''
projection=(intro+projection_text+'\n\n'+end+'\n').replace('\r\n','\n').replace('\n','\r\n').encode('utf-8')
status_path=ROOT/'GAME_LOG_STATUS_CURRENT.md'
status_projection=f'''\r\n\r\n## October 2 local-mini diagnostic addendum — combined-log reference\r\n\r\nUser-requested append at {stamp}: [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md) now retains the local mini forecast exhibit and four twelve-part sporting diagnostic retrospectives. Source labels P-527–P-531 remain local reservations, not assigned canonical IDs. Zero certified settlements; all formal rows remain unresolved, with P-528 unplayed at the original observation and P-531 secondary-only provisional. No renumbering or new issuance occurs. **Next canonical ID remains P-527.** Original ledger and existing cards are unchanged. [Audit and verification](research/verification/mini_settlement_2026-10-02/REPORT.md); pre-existing full-suite/custody/freeze/archive failures remain disclosed.\r\n'''.encode('utf-8')
with locked(CANONICAL_LEDGER):
    records=read_records(CANONICAL_LEDGER);assert not pending(records)
    assert next_id()=='P-527'
    old,tail=_custody(PART6);ledger_before=CANONICAL_LEDGER.read_bytes();status_old=status_path.read_bytes()
    assert begin.encode() not in old
    (OUT/'combined_projection.bin').write_bytes(projection)
    put('publication_prepared.json',dict(schema='diagnostic-publication-1',prepared_utc=stamp,
        base_git_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        part6_before_bytes=len(old),part6_before_sha256=sha(old),ledger_sha256=sha(ledger_before),
        status_before_bytes=len(status_old),status_before_sha256=sha(status_old),
        projection_sha256=sha(projection),original_mini_sha256=sha(original),mini_after_audit_sha256=sha(source),
        canonical_ids_added=0,canonical_next_id='P-527',performance_eligible=False))
    append(PART6,projection);assert PART6.read_bytes()==old+projection
    append(status_path,status_projection);assert status_path.read_bytes()==status_old+status_projection
    _custody(PART6);assert next_id()=='P-527' and CANONICAL_LEDGER.read_bytes()==ledger_before
    assert PART6.read_bytes().count(projection)==1 and mini.read_bytes()==source
    put('publication_append_receipt.json',dict(schema='diagnostic-publication-1',recorded_utc=datetime.now(timezone.utc).isoformat(),
        exact_part6_prefix_preserved=True,part6_before_bytes=len(old),part6_before_sha256=sha(old),
        projection_bytes=len(projection),projection_sha256=sha(projection),part6_after_sha256=sha(PART6.read_bytes()),
        part6_after_bytes=len(PART6.read_bytes()),original_frozen_source_bytes=141740,
        original_frozen_source_sha256='c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30',
        ledger_unchanged=True,ledger_sha256=sha(ledger_before),canonical_ids_affected=[],canonical_next_id='P-527',
        status_append_bytes=len(status_projection),status_after_sha256=sha(status_path.read_bytes()),
        original_mini_unchanged=True,push_status='NOT_YET_PUSHED; VERIFY_REMOTE_AFTER_COMMIT'))
print('Part 6 exact-prefix append and status pointer verified; next P-527, ledger unchanged')

"""Format only the newly projected quotation; retain original source bytes."""
import hashlib,json
from pathlib import Path
from datetime import datetime,timezone
from research.src.issue import PART6,CANONICAL_LEDGER,_custody
from research.src.ledger import locked
from research.operations.log_card import next_id
OUT=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
receipt=json.loads((OUT/'publication_append_receipt.json').read_text())
old_projection=(OUT/'combined_projection.bin').read_bytes()
lines=[]
for line in old_projection.decode('utf-8').splitlines():
    if line.startswith('> '):
        hard_break=line.endswith('  ')
        line=line.rstrip()+(' <br>' if hard_break else '')
    lines.append(line)
formatted=('\r\n'.join(lines)+'\r\n').encode('utf-8')
with locked(CANONICAL_LEDGER):
    raw,_=_custody(PART6);before=receipt['part6_before_bytes']
    assert raw[before:]==old_projection and sha(raw[:before])==receipt['part6_before_sha256']
    PART6.write_bytes(raw[:before]+formatted)
    _custody(PART6);assert next_id()=='P-527'
    (OUT/'combined_projection_formatted.bin').write_bytes(formatted)
    with (OUT/'publication_format_revision.json').open('x',encoding='utf-8') as f:
        json.dump(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
            reason='Quoted display whitespace only: empty blockquotes use > and original Markdown hard breaks render with <br>. Exact original evidence files/mini remain unchanged.',
            prior_projection_sha256=sha(old_projection),formatted_projection_sha256=sha(formatted),
            formatted_projection_bytes=len(formatted),part6_before_bytes=before,
            part6_before_sha256=sha(raw[:before]),part6_after_sha256=sha(PART6.read_bytes()),
            original_prefix_preserved=True,canonical_next_id='P-527'),f,indent=2);f.write('\n')
print('Only new quotation formatting revised; source bytes and existing Part 6 prefix preserved')

from pathlib import Path
from html.parser import HTMLParser
import json,hashlib,re
A=Path(__file__).resolve().parent;ROOT=A.parents[2]
D=Path((A/'delivery_dir.txt').read_text(encoding='utf-8'))
class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,t,a):
        if t in ['script','style']:self.skip+=1
    def handle_endtag(self,t):
        if t in ['script','style']:self.skip=max(0,self.skip-1)
        if t in ['tr','div','p','h1','h2','h3']:self.parts.append('\n')
    def handle_data(self,d):
        if not self.skip and d.strip():self.parts.append(d.strip()+' ')
for label in ['npb_game','kbo_rules_2025']:
    p=Text();p.feed((D/(label+'.body')).read_text(encoding='utf-8',errors='replace'))
    text=''.join(p.parts);(D/(label+'.txt')).write_text(text,encoding='utf-8')
    if label=='npb_game':print(text[text.find('試合TOP'):text.find('球審')])
receipts=[]
for file in A.rglob('*receipt.json'):
    r=json.loads(file.read_text(encoding='utf-8'));receipts.append((str(file.relative_to(ROOT)),r))
for name in ['sources.json','extra_sources.json']:
    for label,e in json.loads((A/name).read_text(encoding='utf-8')).items():
        if e.get('receipt'):receipts.append((name+':'+label,e['receipt']))
unique={}
for ref,r in receipts:
    key=(r.get('body_path'),r.get('response_sha256'))
    if key not in unique:unique[key]=(ref,r)
lines=['# Retained source receipts — October 1 logging repair','','Hashes prove retained bytes; they do not prove field truth, freshness, calibration or collector independence. Native request parameters bind POST bodies to exact fixtures. Generic shells/error bodies are not cited as participant evidence.','','| Receipt | Retrieved UTC | URL | Bytes | SHA-256 | Body |','|---|---|---|---:|---|---|']
verified=[]
for ref,r in unique.values():
    body=ROOT/r['body_path'];raw=body.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=r['response_sha256']:raise ValueError('source bytes changed: '+str(body))
    if 'response_bytes' in r and len(raw)!=r['response_bytes']:raise ValueError('source size changed')
    lines.append(f"| `{ref}` | {r['retrieved_utc']} | {r['source_url']} | {len(raw)} | `{r['response_sha256']}` | `{r['body_path']}` |")
    verified.append(r)
lines.extend(['','## Drive reference copies','','Full text fetched through the Google Drive connector; source URLs are in the KBO report. These copies contain older rules superseded by the current user instruction.'])
for name in ['drive_upcoming_guide.md','drive_current_rules.md','drive_baseball_rules.md']:
    path=A/name;lines.append(f"- `{name}`: {len(path.read_bytes())} bytes; SHA `{hashlib.sha256(path.read_bytes()).hexdigest()}`.")
(A/'SOURCE_RECEIPTS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(A/'verified_sources.json').write_text(json.dumps({'verified_source_bodies':len(verified),'receipts':verified},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Verified retained sources',len(verified))
lineup=json.loads((D/'kbo_lineup.body').read_text(encoding='utf-8'))
print('Refreshed lineup metadata',json.dumps(lineup[:3],ensure_ascii=False))

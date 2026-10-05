"""Retrieve the original P-520 event from the owner's exact dated game list."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import hashlib, json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
url = 'https://www.koreabaseball.com/ws/Main.asmx/GetKboGameList'
params = dict(leId='1', srId='0,1,3,4,5,6,7,8,9', date='20260927')
request = Request(url, data=urlencode(params).encode(), headers={
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx',
    'User-Agent': 'Mozilla/5.0', 'X-Requested-With': 'XMLHttpRequest'})
with urlopen(request, timeout=20) as response:
    raw = response.read(12000001)
    content_type = response.headers.get('Content-Type')
data = json.loads(raw)
game = next(g for g in data['game'] if g['G_ID']=='20260927HHLT0')
body = OUT/'kbo_p520_native.body'
with body.open('xb') as stream:
    stream.write(raw)
receipt = dict(source_id='kbo_p520_native', source_url=url,
               request_method='POST', request_params=params,
               retrieved_utc=datetime.now(timezone.utc).isoformat(),
               response_sha256=hashlib.sha256(raw).hexdigest(),
               response_bytes=len(raw), body_path=body.relative_to(ROOT).as_posix(),
               content_type=content_type, independence_status='UNKNOWN')
receipt_path=ROOT/'research/data/source_receipts/kbo_p520_native_20261005.json'
with receipt_path.open('x', encoding='utf-8') as stream:
    json.dump(receipt, stream, indent=2); stream.write('\n')
proof=dict(receipt=receipt,receipt_path=receipt_path.relative_to(ROOT).as_posix(),game=game)
with (OUT/'P-520_native_owner.json').open('x', encoding='utf-8') as stream:
    json.dump(proof, stream, indent=2); stream.write('\n')
print(json.dumps(game, ensure_ascii=False))

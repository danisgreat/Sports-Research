from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.parse import urlencode
import json,hashlib
A=Path(__file__).resolve().parent; ROOT=A.parents[2]
OUT=A/('delivery_'+datetime.now(timezone.utc).strftime('%H%M%SZ'));OUT.mkdir()
jobs=[('kbo_game','https://www.koreabaseball.com/ws/Main.asmx/GetKboGameList',{'leId':'1','srId':'0,1,3,4,5,6,7,8,9','date':'20261001'}),
      ('kbo_lineup','https://www.koreabaseball.com/ws/Schedule.asmx/GetLineUpAnalysis',{'leId':'1','srId':'0','seasonId':'2026','gameId':'20261001HHSS0'}),
      ('npb_game','https://npb.jp/scores/2026/1001/c-d-25/',None),
      ('kbo_rules_2025','https://www.koreabaseball.com/Kbo/League/GameManage2025.aspx',None)]
out={}
for label,url,params in jobs:
    request=Request(url,data=urlencode(params).encode() if params else None,headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx','User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'})
    with urlopen(request,timeout=20) as response:raw=response.read(12000000);ct=response.headers.get('Content-Type')
    path=OUT/(label+'.body');path.write_bytes(raw)
    receipt={'source_url':url,'request_params':params,'request_method':'POST' if params else 'GET','retrieved_utc':datetime.now(timezone.utc).isoformat(),'response_sha256':hashlib.sha256(raw).hexdigest(),'response_bytes':len(raw),'body_path':path.relative_to(ROOT).as_posix(),'content_type':ct,'independence_status':'UNKNOWN'}
    (OUT/(label+'_receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    out[label]=receipt
    if label=='kbo_game':
        game=next(g for g in json.loads(raw)['game'] if g['G_ID']=='20261001HHSS0');print(json.dumps(game,ensure_ascii=False))
(OUT/'index.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
(A/'delivery_dir.txt').write_text(str(OUT),encoding='utf-8')
print(OUT)

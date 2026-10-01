from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[3];A=Path(__file__).resolve().parent
class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.skip=0
    def handle_starttag(self,t,a):
        if t in ['script','style']:self.skip+=1
    def handle_endtag(self,t):
        if t in ['script','style']:self.skip-=1
        if t in ['tr','div','p','h1','h2','h3']:self.parts.append('\n')
    def handle_data(self,d):
        if not self.skip and d.strip():self.parts.append(d.strip()+' ')
U=Path((A/'latest_updates_dir.txt').read_text(encoding='utf-8'))
for name in ['npb_current','yahoo_current']:
    p=Text();p.feed((U/(name+'.body')).read_text(encoding='utf-8',errors='replace'))
    (A/(name+'.txt')).write_text(''.join(p.parts),encoding='utf-8')
mini=next((ROOT/'Mini logs (to be sent to actual log later)').rglob('PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md'))
raw=mini.read_bytes();(A/'originals/mini_before_import.md').write_bytes(raw)
text=raw.decode('utf-8-sig');kt=text[text.index('### TMP-20261001-KBO-KT-KIA'):]
kt=kt.split('\n<!--',1)[0].rstrip()+'\n'
(A/'originals/KT_KIA.md').write_text(kt,encoding='utf-8')
bol=ROOT/'research/verification/settlement_2026-10-01/issue_text/CLAIMED_P-523.md'
npb=Path(r'C:\Users\danie\.codex\attachments\129564e4-b6a9-4fd6-ba59-86877357cae3\Pasted text.txt')
(A/'originals/NPB_pasted.txt').write_bytes(npb.read_bytes())
stamp=datetime.now(timezone.utc).isoformat()
cards=[]
def record(file,title,handle,key,league,native,body,status):
    card=dict(source_path=str(file),title=title,tracking_handle=handle,event_key=key,league=league,native_event_id=native,body=body,analysis_status=status)
    name=A/(handle+'_card.json');name.write_text(json.dumps(card,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');cards.append(str(name))
quote=lambda s:'\n'.join('> '+line for line in s.splitlines())+'\n'
bolbody=('### Dated canonical import correction\n\n'
 'The retained mini-log card is now stored in the canonical running log as a historical research import. Its original P-523 claim maps to P-523. The import does not certify an earlier canonical issue or rewrite its forecast values. The source claim of pregame freezing conflicts with its stated 00:31:30 UTC freeze after scheduled 00:30; preserve both timestamps. No new forecast or retrospective is generated for this completed game. The earlier dated all-log audit remains separately linked at `research/verification/settlement_2026-10-01/REPORT.md`; it is not repeated here.\n\n'
 'Native FBF ID remains unknown; ESPN 401907909 is a secondary ID. Original numerical probabilities/baselines remain historical uncalibrated claims, with original arithmetic/source limits preserved. The undefined corners row remains unissued. This import resolves storage/ID custody, without backfilling evidence.\n\n'
 '### Retained original card text\n\n'+quote(bol.read_text(encoding='utf-8')))
record(bol,'Oriente Petrolero vs The Strongest — retained October 1 card','TMP-20261001-BOLCOPA-OPE-STR','BoliviaCopa:2026:secondary-ESPN-401907909','BoliviaCopa',None,bolbody,'HISTORICAL_RESEARCH_IMPORT')
ktbody=('### Dated canonical import correction\n\n'
 'The retained KT–Kia research is now canonically logged rather than left TMP-only. Actual import time appears above; the original text has no trustworthy issuance timestamp and already describes live play. It cannot be retrospectively certified as pregame. No new grades, settlement or retrospective are added.\n\n'
 'Owner verification now binds this event to KBO native `20261001KTHT0`; the longer `20261001KTHT02026` is a Naver provider key. A media gateway is not the league field owner, and weather is not a third independent sporting-event source. Official KBO regular-season rules changed extras to ELEVEN innings from 2025, not twelve. See `https://www.koreabaseball.com/Kbo/League/GameManage2025.aspx`. The retained numeric estimates are UNCALIBRATED historical analyst claims: their .769 margin factor, tie mass, run means and baselines have no retained validated joint score distribution or approved calibration. They are preserved, not converted to certified estimates. Cool air may influence carry; it does not establish a measured change in batter exit velocity. Wind relative to the field and complete bullpen availability were not demonstrated. These corrections change no original picks or percentages.\n\n'
 '### Retained original card text\n\n'+kt)
record(A/'originals/KT_KIA.md','KT Wiz @ Kia Tigers — retained October 1 card','TMP-20261001-KBO-KT-KIA','KBO:2026:20261001KTHT0','KBO','20261001KTHT0',ktbody,'HISTORICAL_UNCALIBRATED_RESEARCH_IMPORT')
npbbody=('### Dated canonical import and new assessment\n\n'
 'The supplied NPB card is now in the canonical running log, with its TMP alias preserved. Its old NONE_CONSUMED/NO_MODEL/UNRANKED and buffer/universe/quorum blockers describe the earlier response, not the current policy. The original intake is retained literally below. The new analysis is dated at canonical logging time and cannot become an earlier pregame forecast. No retrospective or settlement is performed.\n\n'
 '**New assessment: UNCALIBRATED_QUALITATIVE; numerical p and baseline NOT_ESTIMATED.** Official NPB and Sportsnavi bodies were retained at about 09:40 UTC in `updates_094047Z`: the owner showed Hiroshima 2–0 Chunichi, bottom third, while Sportsnavi remained 0–0/bottom first with publisher update 18:05 JST. The later owner refresh in `delivery_095713Z/npb_game.body` shows HIROSHIMA 2–0 CHUNICHI, TOP FIFTH; it controls this new live assessment. NPB records Nakamura’s third-inning two-run homer. Sportsnavi is stale, not an agreeing current-state source. NPB schedule remains 18:00 JST/19:00 AEST. This is conditional on the retained owner observation, not a reconstructed pregame forecast.\n\n'
 '| Rank | Pick | Reason and limitation |\n|---:|---|---|\n'
 '| 1 | Carp +1.5 | Hiroshima already leads 2–0 in the retained owner state. Its cushion still succeeds if it gives up that lead and ultimately loses by one; Tokoda’s posted 2.88 ERA adds contextual run-prevention support. The lead is not a guarantee, and current command/relief availability remain uncertain. |\n'
 '| 2 | Under 6.5 runs | Two runs through four completed innings leave room for four more while satisfying the Under. Both posted starters have low season ERAs and the orders include pitchers, but the documented home run and potential bullpen/extras make this a modest lean. |\n'
 '| 3 | Dragons +1.5 | The cushion covers a comeback win, tie or one-run loss. Chunichi has to erase at least one run of the present two-run deficit to reach that sporting proposition; the original pregame ERA advantage cannot override observed play. Chunichi’s larger head-to-head runs total is a contrary-context signal. |\n'
 '| 4 | Over 6.5 runs | Opposing requested total. Starter command loss, early hook, pinch-hit improvement, clustered hits or extra innings can produce seven-plus despite the season ERAs. |\n\n'
 '**Potential winner: Hiroshima**, based on its verified two-run lead, home field and Tokoda’s contextual run prevention. Chunichi’s better starter season ERA and cumulative head-to-head runs are contrary evidence, and later workload/state changes can reverse the view. No exact percentages or unsupported certainty are supplied. These new live ranks are not attributed to the original unranked intake.\n\n'
 'Sportsnavi’s head-to-head section totals Chunichi 95 runs and Hiroshima 86 across 24 prior meetings (combined 7.54/game), which argues against calling Under 6.5 safe or inferring all games are low-scoring. Its last listed meeting on September 21 is a LAST HEAD-TO-HEAD, not evidence that Chunichi last played on that date. The pasted “full bullpen available” claim is unsupported and is not used. Do not treat the page’s automated 調子 form labels as research inputs. Relevant posted orders, starters and season averages are retained in the original and fresh body; no fantasy/form prediction labels enter this assessment.\n\n'
 'Both +1.5 propositions succeed on a tie or any one-run final; they form a covering pair. Under/Over 6.5 are complementary on a valid integer official final, with no sporting-score push. Use NPB regular-season full-game permitted extras; operator void/shortened-game terms were not supplied. No bookmaker settlement is asserted. Sources: `https://npb.jp/scores/2026/1001/c-d-25/`, `https://baseball.yahoo.co.jp/npb/game/2021048568/top`; exact retained UTC/body hashes in SOURCE_RECEIPTS.md. Weather is environmental context only; no bullpen-rest, park-factor or weather coefficient is invented.\n\n'
 '### Retained original intake — superseded blockers, unchanged historical text\n\n'+npb.read_text(encoding='utf-8-sig'))
record(A/'originals/NPB_pasted.txt','Chunichi Dragons @ Hiroshima Toyo Carp — Game 25','TMP-20261001-NPB-CHU-HIR-G25','NPB:2026:20261001-c-d-25','NPB','20261001-c-d-25',npbbody,'IMPORT_WITH_DATED_UNCALIBRATED_QUALITATIVE_ANALYSIS')
analysis=A/'KBO_HANWHA_SAMSUNG_ANALYSIS.md'
record(analysis,'Hanwha Eagles @ Samsung Lions — October 1, 2026','TMP-20261001-KBO-HAN-SAM','KBO:2026:20261001HHSS0','KBO','20261001HHSS0',analysis.read_text(encoding='utf-8'),'LIVE_OBSERVED_UNCALIBRATED_QUALITATIVE')
(A/'cards_to_import.json').write_text(json.dumps(cards,indent=2)+'\n',encoding='utf-8')
print('Prepared',len(cards),'complete cards with original-source pointers; no canonical append yet.')

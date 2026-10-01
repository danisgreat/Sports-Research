from html.parser import HTMLParser
from pathlib import Path
import json,re
A=Path(__file__).resolve().parent
class Tables(HTMLParser):
    def __init__(self):super().__init__();self.tables=[];self.table=None;self.row=None;self.cell=None;self.skip=0
    def handle_starttag(self,t,a):
        if t in ['script','style']:self.skip+=1
        if t=='table':self.table={'attrs':dict(a),'rows':[]};self.tables.append(self.table)
        if t=='tr':self.row=[]
        if t in ['td','th']:self.cell=[]
    def handle_endtag(self,t):
        if t in ['script','style']:self.skip=max(0,self.skip-1)
        if t in ['td','th'] and self.cell is not None:
            if self.row is not None:self.row.append(re.sub(r'\s+',' ',''.join(self.cell)).strip())
            self.cell=None
        if t=='tr' and self.row is not None:
            if self.table is not None:self.table['rows'].append(self.row)
            self.row=None
        if t=='table':self.table=None
    def handle_data(self,s):
        if self.cell is not None and not self.skip:self.cell.append(s)
if __name__=='__main__':
    import sys
    for label in sys.argv[1:]:
        p=Tables();p.feed((A/(label+'.html')).read_text(encoding='utf-8-sig'))
        (A/(label+'_tables.json')).write_text(json.dumps(p.tables,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(label,json.dumps(p.tables,ensure_ascii=False))

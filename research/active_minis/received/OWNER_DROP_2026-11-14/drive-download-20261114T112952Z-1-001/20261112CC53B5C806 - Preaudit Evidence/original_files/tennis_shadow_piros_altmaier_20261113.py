"""Exploratory independent-set Markov chain; NOT framework primary, not calibrated.
P(point won on serve) scenario inputs, all tiebreaks first to >=7 by 2. 
Results include all games in completed best-of-three matches, no retirements.
"""
from collections import defaultdict
import functools, json, math

def game_hold(p):
 q=1-p
 return p**4 * (1+4*q+10*q*q)+20*p**3*q**3 * (p*p/(p*p+q*q))

def tb_win(pA,pB,first_server):
 d={(0,0):1.0}; won=0.; lost=0.
 for k in range(120):
  nxt=defaultdict(float)
  server= first_server if (k%4 in (0,3)) else 1-first_server
  w=pA if server==0 else 1-pB
  for (a,b),mass in d.items():
   for addA,pr in ((True,w),(False,1-w)):
    a1,b1=(a+1,b) if addA else (a,b+1)
    m=mass*pr
    if max(a1,b1)>=7 and abs(a1-b1)>=2:
     if a1>b1:won+=m
     else:lost+=m
    else:nxt[(a1,b1)]+=m
  d=nxt
  if sum(d.values())<1e-14:break
 return won+0.5*sum(d.values())

@functools.lru_cache(maxsize=32)
def set_outcomes(pA,pB,start):
 p_hA=game_hold(pA); p_hB=game_hold(pB)
 states={(0,0,start):1.0}; ret=defaultdict(float)
 for ng in range(13):
  nxt=defaultdict(float)
  for (a,b,s),mass in states.items():
   if a==6 and b==6:
    t=tb_win(pA,pB,s)
    ret[(7,6,1-s)]+=mass*t
    ret[(6,7,1-s)]+=mass*(1-t)
   else:
    wp=p_hA if s==0 else 1-p_hB
    for a1,b1,pr in ((a+1,b,wp),(a,b+1,1-wp)):
     if (a1>=6 or b1>=6) and abs(a1-b1)>=2:
      ret[(a1,b1,1-s)]+=mass*pr
     else:
      nxt[(a1,b1,1-s)]+=mass*pr
  states=nxt
 assert abs(sum(ret.values())-1)<1e-10, sum(ret.values())
 return ret

def match_dist(pA,pB):
 vals=defaultdict(float)
 sret=[set_outcomes(pA,pB,0),set_outcomes(pA,pB,1)]
 for start in (0,1):
  st={(0,0,0,0,start):0.5}
  for setsplayed in range(3):
   nxt=defaultdict(float)
   for (sa,sb,ga,gb,s),mass in st.items():
    for (a,b,ns),pr in sret[s].items():
     sa1,sb1=sa+(a>b),sb+(a<b)
     ga1,gb1=ga+a,gb+b
     if sa1==2 or sb1==2:
      vals[(ga1,gb1,sa1,sb1)]+=mass*pr
     else:nxt[(sa1,sb1,ga1,gb1,ns)]+=mass*pr
   st=nxt
 assert abs(sum(vals.values())-1)<1e-9
 return vals

def summarize(pA,pB):
 d=match_dist(pA,pB)
 prob=lambda f:sum(m for (a,b,sa,sb),m in d.items() if f(a,b,sa,sb))
 pa=prob(lambda a,b,sa,sb: a-b>=-2)
 pt=prob(lambda a,b,sa,sb: a+b>=23)
 win=prob(lambda a,b,sa,sb: sa==2)
 dec=prob(lambda a,b,sa,sb: sa+sb==3)
 return dict(pA=pA,pB=pB,holdA=game_hold(pA),holdB=game_hold(pB),p_piros_plus_0_5=pa,p_altmaier_minus_0_5=1-pa,p_over_22_5=pt,p_under_22_5=1-pt,p_piros_matchwin=win,p_altmaier_matchwin=1-win,p_deciding_set=dec,expected_total=sum((a+b)*m for (a,b,sa,sb),m in d.items()),expected_margin_piros=sum((a-b)*m for (a,b,sa,sb),m in d.items()),joint_piros_plus_and_under=prob(lambda a,b,sa,sb: a-b>=-2 and a+b<=22),joint_alt_minus_and_over=prob(lambda a,b,sa,sb: a-b<=-3 and a+b>=23),joint_alt_minus_and_under=prob(lambda a,b,sa,sb: a-b<=-3 and a+b<=22),score_examples=sorted([{'games':f'{a}-{b}','sets':f'{sa}-{sb}','p':m} for (a,b,sa,sb),m in d.items()],key=lambda x:-x['p'])[:8])


if __name__=='__main__':
 import hashlib, pathlib
 # Source: 52-week point-level serve/return numbers (PythiaTennis stat table), independently confirmed
 # match/form shape from tennisexplorer and stevegtennis; NO odds or source predictions used.
 # Piros 52wk service points won: all .623, indoor .637; return .390/.370.
 # Altmaier 52wk service points won: all .629, indoor .691; return .345/.311.
 # Match-up SPW = arithmetic mean of own SPW and opponent's service-point loss from return.
 p_piros_all=(.623+(1-.345))/2
 p_alt_all=(.629+(1-.390))/2
 p_piros_indoor=(.637+(1-.311))/2
 p_alt_indoor=(.691+(1-.370))/2
 shrink=20
 p_piros_shr=(shrink*p_piros_all+16*p_piros_indoor)/(shrink+16)
 p_alt_shr=(shrink*p_alt_all+10*p_alt_indoor)/(shrink+10)
 # Last two Orleans matches descriptive only (also included in indoor sample): low sample sizes;
 # do NOT multiply in base mixture, avoid double counting
 p_piros_two=(.603+(1-.382))/2
 p_alt_two=(.703+(1-.357))/2
 scenarios={'all_surface_52wk':(p_piros_all,p_alt_all),'indoor_shrink20':(p_piros_shr,p_alt_shr),'indoor_only_52wk':(p_piros_indoor,p_alt_indoor),'recent_two_matches_stress_only':(p_piros_two,p_alt_two)}
 results={name:summarize(*params) for name,params in scenarios.items()}
 # baseline qualitative direction uses shrink20 but no calibrated primary p
 info={'status':'EXPLORATORY_DIAGNOSTIC_ONLY_NOT_FRAMEWORK_PRIMARY','model':'Exact server-game/tiebreak/set/match outcome enumeration, best of 3',
 'endpoint':'Completed match games; includes completed third set; no retirement/WO; tiebreak counted as game',
 'competition':'Orleans Challenger 2026 quarterfinal',
 'inputs':{'piros':{'indoor_spw':.637,'indoor_rpw':.370,'indoor_n':16,'all_spw':.623,'all_rpw':.390,'all_n':72,'orleans_two_spw':.603,'orleans_two_rpw':.357},'altmaier':{'indoor_spw':.691,'indoor_rpw':.311,'indoor_n':10,'all_spw':.629,'all_rpw':.345,'all_n':60,'orleans_two_spw':.703,'orleans_two_rpw':.382}},
 'source_urls':['https://pythiatennis.com/daniel-altmaier-vs-zsombor-piros-prediction-and-stats/?d=2026-11-13','https://www.stevegtennis.com/head-to-head/men/Daniel_Altmaier/Zsombor_Piros/','https://www.tennisexplorer.com/match-detail/?id=3377369'],
 'limitations':['Not fitted/calibrated to player opponent levels and Challenger surfaces','52-week sample mixes tour/Challenger opponent quality','20-match shrink is an analyst sensitivity setting, not fitted','IID points ignore fatigue, pressure, set-specific performance','Recent-two scenario is stress only and already represented within indoor last-year; not independently weighted','No retirement/void/first-server verified; first server random 50:50','Statistics provider may have retrospective corrections'],
 'distributions':results}
 target=pathlib.Path('/mnt/data/TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0008.json')
 target.write_text(json.dumps(info,indent=2,ensure_ascii=False)+'\n')
 for name,r in results.items():
  cols=['p_piros_plus_0_5','p_altmaier_minus_0_5','p_over_22_5','p_under_22_5','p_piros_matchwin','p_deciding_set','expected_total','expected_margin_piros']
  print(name,{k:round(r[k],4) for k in cols})
 print('saved',target)

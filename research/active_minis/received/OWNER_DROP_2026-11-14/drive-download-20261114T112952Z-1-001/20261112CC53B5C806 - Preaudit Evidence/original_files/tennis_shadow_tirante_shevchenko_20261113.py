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
 pa=prob(lambda a,b,sa,sb: a>=b)
 pt=prob(lambda a,b,sa,sb: a+b>=24)
 win=prob(lambda a,b,sa,sb: sa==2)
 dec=prob(lambda a,b,sa,sb: sa+sb==3)
 return dict(pA=pA,pB=pB,holdA=game_hold(pA),holdB=game_hold(pB),p_tirante_plus_0_5=pa,p_shevchenko_minus_0_5=1-pa,p_over_23_5=pt,p_under_23_5=1-pt,p_tirante_matchwin=win,p_shevchenko_matchwin=1-win,p_deciding_set=dec,expected_total=sum((a+b)*m for (a,b,sa,sb),m in d.items()),expected_margin_tirante=sum((a-b)*m for (a,b,sa,sb),m in d.items()),joint_tirante_plus_and_under=prob(lambda a,b,sa,sb: a>=b and a+b<=23),joint_shev_minus_and_over=prob(lambda a,b,sa,sb: a<b and a+b>=24),joint_shev_minus_and_under=prob(lambda a,b,sa,sb: a<b and a+b<=23),score_examples=sorted([{'games':f'{a}-{b}','sets':f'{sa}-{sb}','p':m} for (a,b,sa,sb),m in d.items()],key=lambda x:-x['p'])[:8])

if __name__=='__main__':
 # Matchup point serve input = average(own service-point-win, 1 - opponent return-point-win).
 # Period-specific source: PythiaTennis, raw 52-week stats (NOT its prediction or odds).
 # Indoor sample: T 6 matches, S 11; overall: T 57 matches, S 66.
 overall_T=(.666+(1-.357))/2
 overall_S=(.633+(1-.358))/2
 indoor_T=(.663+(1-.353))/2
 indoor_S=(.672+(1-.317))/2
 prior_match_equiv=20 # Sensitivity parameter only, not fitted/calibrated.
 shrunk_T=(prior_match_equiv*overall_T+6*indoor_T)/(prior_match_equiv+6)
 shrunk_S=(prior_match_equiv*overall_S+11*indoor_S)/(prior_match_equiv+11)
 scenarios={'all_surface_52wk':(overall_T,overall_S),'indoor_shrink20':(shrunk_T,shrunk_S),'indoor_only_52wk':(indoor_T,indoor_S)}
 results={name:summarize(*inputs) for name,inputs in scenarios.items()}
 result={'type':'EXPLORATORY_ANALYST_SCENARIOS_NOT_PRIMARY','contract':'full completed tennis match, best of 3, tiebreak to 7 by 2 at 6-6','input_basis':'52wk individual serve- and return-points-won percentages from PythiaTennis, each opponent match-up averaged without validated opponent adjustment; 20-match shrink parameter chosen as sensitivity only; no calibrated effect sizes','assumptions':['IID serving points per player throughout match','both players hold fixed point-service strength in a scenario','initial server equally likely','no retirement/withdrawal','no fatigue/conditioning between sets','no ranking or form fed in as numerical effects'], 'source':{'url':'https://pythiatennis.com/alexander-shevchenko-vs-thiago-agustin-tirante-prediction-and-stats/?d=2026-11-12','indoor_match_n':{'tirante':6,'shevchenko':11},'overall_match_n':{'tirante':57,'shevchenko':66},'indoor_service_point_win':{'tirante':.663,'shevchenko':.672},'indoor_return_point_win':{'tirante':.317,'shevchenko':.353},'overall_service_point_win':{'tirante':.666,'shevchenko':.633},'overall_return_point_win':{'tirante':.358,'shevchenko':.357}},'distributions':results}
 with open('/mnt/data/TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0003.json','w') as f:json.dump(result,f,indent=2)
 for name,r in results.items():print(name,{k:round(v,4) for k,v in r.items() if k in ('holdA','holdB','p_tirante_plus_0_5','p_shevchenko_minus_0_5','p_over_23_5','p_under_23_5','p_tirante_matchwin','p_deciding_set','expected_total','expected_margin_tirante')})

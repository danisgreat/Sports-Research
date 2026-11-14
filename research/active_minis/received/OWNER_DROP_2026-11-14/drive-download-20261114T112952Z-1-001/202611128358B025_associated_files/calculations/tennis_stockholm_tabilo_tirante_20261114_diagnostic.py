"""CHAT-LOCAL 2026-11-14 Stockholm semi-final conditional scoring diagnostics.
Tabilo -1.5 games / Tirante +1.5 games / Over-Under 24.5 games.
Main analysis on 2026-11-14 AFTER scheduled first serve; not a certified pre-match issue.
No repository reference/freeze/promotion. No prices, betting tips, or live data used.
P(Service point won) values below are ILLUSTRATIVE scenario parameters, not fitted or qualified.
Tennis Abstract current Elo: Tabilo overall 1782.2, hard 1731.8; Tirante
overall 1756.6, hard 1669.4, blend T 1757.0, Tir 1713.0 (~56.3% T).
Tournament court serve-point won statistic 66.8% vs tour 63.7% on small sample;
season serve vs opponent return data exist but cannot fit exact-match service parameters.
Tabilo QF 7-5 7-6(2); Tirante QF 7-6(5) 6-7(5) 6-3.
Tirante R16 was an opponent walkover, not a played win.
Tennis Abstract & official Stockholm event URL are cited in the updated mini log.
"""
from math import sqrt
from hashlib import sha256
import json
import numpy as np
from collections import defaultdict
from functools import lru_cache
from math import log10

def hold(p):
    q=1-p
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3*(p*p/(p*p+q*q))

def tb_win(p_a,p_b,first):
    @lru_cache(None)
    def rec(a,b):
        if a>=7 and a-b>=2:return 1.0
        if b>=7 and b-a>=2:return 0.0
        if a+b >= 150: return 0.5 # exponentially small tail (unreported exactness)
        n=a+b
        srv=first if n==0 or ((n-1)//2)%2==1 else 1-first
        p=p_a if srv==0 else 1-p_b
        return p*rec(a+1,b)+(1-p)*rec(a,b+1)
    return rec(0,0)

def set_dist(pa,pb,first):
    h_a,h_b=hold(pa),hold(pb)
    tb={0:tb_win(pa,pb,0),1:tb_win(pa,pb,1)}
    wave={(0,0):1.}
    results=defaultdict(float)
    for _ in range(14):
        nxt=defaultdict(float)
        for (a,b),prob in wave.items():
            server=first if (a+b)%2==0 else 1-first
            if (a>=6 and a-b>=2) or (b>=6 and b-a>=2):
                results[(a,b,server)]+=prob
            elif (a,b)==(6,6):
                z=tb[server]
                results[(7,6,1-server)]+=prob*z
                results[(6,7,1-server)]+=prob*(1-z)
            else:
                awin=h_a if server==0 else 1-h_b
                nxt[(a+1,b)]+=prob*awin
                nxt[(a,b+1)]+=prob*(1-awin)
        wave=nxt
    assert not wave
    assert abs(sum(results.values())-1)<1e-11
    return results

def match_dist(pa,pb):
    s={0:set_dist(pa,pb,0),1:set_dist(pa,pb,1)}
    ret=defaultdict(float)
    for fs in (0,1):
        for (a1,b1,n1),w1 in s[fs].items():
            for (a2,b2,n2),w2 in s[n1].items():
                if (a1>b1)==(a2>b2):
                    ret[(a1+a2,b1+b2,int(a1>b1),2)]+=.5*w1*w2
                else:
                    for (a3,b3,n3),w3 in s[n2].items():
                        ret[(a1+a2+a3,b1+b2+b3,int(a3>b3),3)]+=.5*w1*w2*w3
    assert abs(sum(ret.values())-1)<1e-10
    return ret


def evaluate(label,pa,pb):
    d=match_dist(pa,pb)
    Aminus15=sum(v for (a,b,w,n),v in d.items() if a-b>=2)
    over245=sum(v for (a,b,w,n),v in d.items() if a+b>=25)
    mwin=sum(v for (a,b,w,n),v in d.items() if w==1)
    dec=sum(v for (a,b,w,n),v in d.items() if n==3)
    ea=sum(a*v for (a,b,w,n),v in d.items())
    eb=sum(b*v for (a,b,w,n),v in d.items())
    em=ea-eb; et=ea+eb
    var_t=sum((a+b-et)**2*v for (a,b,w,n),v in d.items())
    var_m=sum((a-b-em)**2*v for (a,b,w,n),v in d.items())
    joint=sum(v for (a,b,w,n),v in d.items() if (b-a>=-1) and (a+b>=25))
    return {"scenario":label, "p_service_Tabilo":pa, "p_service_Tirante":pb,
      "hold_Tabilo":hold(pa),"hold_Tirante":hold(pb),
      "P_Tabilo_minus_1_5":Aminus15,"P_Tirante_plus_1_5":1-Aminus15,
      "P_Over_24_5":over245,"P_Under_24_5":1-over245,
      "P_Tabilo_win":mwin,"P_Tirante_win":1-mwin,
      "P_deciding_set":dec,"expected_Tabilo_games":ea,"expected_Tirante_games":eb,
      "expected_total_games":et,"expected_games_margin_Tabilo":em,
      "SD_total_games":sqrt(var_t),"SD_games_margin":sqrt(var_m),
      "P_Tirante_plus_1_5_AND_Over_24_5":joint,
      "normalized_probability_sum":sum(d.values()),"score_states":len(d)}

if __name__=='__main__':
  cases=[('CENTRAL_ILLUSTRATIVE',0.675,0.664),
     ('NEAR_EQUAL_SERVE',0.667,0.667),
     ('TIRANTE_SERVE_EDGE',0.655,0.684),
     ('TABILO_SERVE_EDGE',0.684,0.654),
     ('BOTH_LOW_HOLD',0.642,0.640),
     ('BOTH_HIGH_HOLD',0.688,0.684)]
  results=[evaluate(*c) for c in cases]
  d=match_dist(cases[0][1],cases[0][2]); support=list(d.keys()); probs=np.array(list(d.values()));
  assert abs(probs.sum()-1)<1e-10
  rng=np.random.default_rng(20261114); samples=rng.choice(len(support),size=200_000,p=probs)
  raw=np.array(support,dtype=int)[samples];
  mc={"draws":200000,"seed":20261114,"P_Tirante_plus_1_5":float((raw[:,0]-raw[:,1]<=1).mean()),
      "P_Over_24_5":float((raw[:,0]+raw[:,1]>=25).mean())}
  mc['P_Tirante_plus_1_5_MC_SE']=sqrt(mc['P_Tirante_plus_1_5']*(1-mc['P_Tirante_plus_1_5'])/mc['draws'])
  mc['P_Over_24_5_MC_SE']=sqrt(mc['P_Over_24_5']*(1-mc['P_Over_24_5'])/mc['draws'])
  eloT=(1782.2+1731.8)/2; eloR=(1756.6+1669.4)/2
  pack={"heading":"Tabilo v Tirante Stockholm 2026 chat local conditional calculation", 
    "eloT":eloT,"eloR":eloR,"elo_formula_T_win":1/(1+10**(-(eloT-eloR)/400)),
    "scenarios":results,"MC_validation":mc,
    "caveat":"Uncalibrated illustrative serve-point params. No official model freeze or p_card."}
  out='/mnt/data/tennis_stockholm_tabilo_tirante_20261114_results.json'
  open(out,'w').write(json.dumps(pack,indent=2)+'\n')
  print(json.dumps(pack,indent=2))

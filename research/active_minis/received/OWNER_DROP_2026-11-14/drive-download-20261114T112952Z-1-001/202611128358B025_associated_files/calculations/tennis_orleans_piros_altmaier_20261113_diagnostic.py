"""CHAT-LOCAL diagnostic only: Piros v Altmaier, Orleans Challenger QF, 2026-11-13.

No official Sports-Research freeze, no calibrated model, no Monte Carlo claim.
Inputs are EXPLICIT ANALYST SCENARIOS, not fitted/verified point parameters.
A finite state recursion enumerates legal service games, tiebreaks, sets, match totals
and game margins in all match-winning and match-losing score states.
Full-match score includes all played games; best-of-3 hard court.
Pre-match sport facts used to choose the centre:
Tennis Abstract 2026-11 rating search: Piros Elo 1684.5/hElo 1647.7;
Altmaier 1715.2/hElo 1643.9 (2026-11 search snippet; page open snapshot stale).
2026 Orleans service games 2-match sample: Piros 23/30=76.7%; Altmaier 24/27=88.9%
(source stevegtennis 2026-11-13; too little and biased by opponent quality).
Central p_service = Piros 0.632, Altmaier 0.635; these are hypothetical and have
not been fit to the listed numbers, and no form shock is estimated.
"""
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

def evaluate(name,pa,pb):
    d=match_dist(pa,pb)
    pplus=sum(v for (a,b,w,n),v in d.items() if a-b>=-2)
    pover=sum(v for (a,b,w,n),v in d.items() if a+b>=23)
    pmatch=sum(v for (a,b,w,n),v in d.items() if w==1)
    pthird=sum(v for (a,b,w,n),v in d.items() if n==3)
    expa=sum(a*v for (a,b,w,n),v in d.items())
    expb=sum(b*v for (a,b,w,n),v in d.items())
    print(f'{name} | Apoint={pa:.3f} Bpoint={pb:.3f} | hold A={hold(pa):.5f}, B={hold(pb):.5f} | P(Piros match)={pmatch:.5f} | P(Piros +2.5)={pplus:.5f} | P(Alt -2.5)={1-pplus:.5f} | P(Over22.5)={pover:.5f} | P(Under22.5)={1-pover:.5f} | Egames A={expa:.3f} B={expb:.3f} Total={expa+expb:.3f} | P(decider)={pthird:.5f} | states={len(d)}')
    return pplus,pover

if __name__=='__main__':
    p_elo=1/(1+10**(-(((1684.5+1647.7)/2)-((1715.2+1643.9)/2))/400))
    print('Tennis Abstract blend Piros Elo 1666.10, Altmaier 1679.55, Elo win Piros=',round(p_elo,5))
    for scenario,pa,pb in [
        ('CENTRAL_ELO_BALANCED',.632,.635),
        ('PIROS_INDOOR_FORM',.638,.628),
        ('ALTMAIER_STRONG_SERVE',.619,.651),
        ('BOTH_SERVE_WEAKER',.615,.615),
        ('BOTH_SERVE_STRONGER',.648,.648)]:
        evaluate(scenario,pa,pb)

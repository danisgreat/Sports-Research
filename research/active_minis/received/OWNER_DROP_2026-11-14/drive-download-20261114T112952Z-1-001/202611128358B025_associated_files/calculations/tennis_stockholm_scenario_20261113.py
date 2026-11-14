"""Transparent conditional tennis score-grid diagnostic for Tirante/Shevchenko, 2026-11-12.
Inputs are retrospective snapshots of pre-scheduled-start aggregate point stats, NOT a published
or trained Sports-Research official forecast. Independent-serve model; no form shock fitted.
All set scores, winner, match-games handicap and match total derive from one distribution.
"""
from collections import defaultdict
from functools import lru_cache

def hold(p):
    q = 1-p
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3*(p*p/(p*p+q*q))

def tiebreak_first_server(p_a,p_b,first):
    @lru_cache(None)
    def rec(a,b):
        if a>=7 and a-b>=2: return 1.0
        if b>=7 and b-a>=2: return 0.0
        if a+b>=120: return 0.5  # extremely small remaining probability, truncation diagnostic
        t=a+b
        srv = first if t==0 or ((t-1)//2)%2 else 1-first
        pw = p_a if srv==0 else 1-p_b
        return pw*rec(a+1,b)+(1-pw)*rec(a,b+1)
    return rec(0,0)

def set_states(p_a,p_b,first):
    ha,hb=hold(p_a),hold(p_b)
    tb={0:tiebreak_first_server(p_a,p_b,0), 1:tiebreak_first_server(p_a,p_b,1)}
    wave={(0,0):1.0}
    outcomes=defaultdict(float)
    for t in range(14):
        nxt=defaultdict(float)
        for (a,b),w in wave.items():
            next_server=first if (a+b)%2==0 else 1-first
            if (a>=6 and a-b>=2) or (b>=6 and b-a>=2):
                outcomes[(a,b,next_server)]+=w
            elif a==6 and b==6:
                z=tb[next_server]
                outcomes[(7,6,1-next_server)]+=w*z
                outcomes[(6,7,1-next_server)]+=w*(1-z)
            else:
                awin=ha if next_server==0 else 1-hb
                nxt[(a+1,b)]+=w*awin
                nxt[(a,b+1)]+=w*(1-awin)
        wave=nxt
    assert not wave, (first,wave)
    assert abs(sum(outcomes.values())-1)<1e-10
    return outcomes

def match_distribution(p_a,p_b):
    s={0:set_states(p_a,p_b,0),1:set_states(p_a,p_b,1)}
    matches=defaultdict(float)
    for fs in (0,1):
        for (a1,b1,n1),w1 in s[fs].items():
            x1=a1>b1
            for (a2,b2,n2),w2 in s[n1].items():
                x2=a2>b2
                if x1==x2:
                    matches[(a1+a2,b1+b2,x1,2)]+=0.5*w1*w2
                else:
                    for (a3,b3,n3),w3 in s[n2].items():
                        matches[(a1+a2+a3,b1+b2+b3,a3>b3,3)]+=0.5*w1*w2*w3
    assert abs(sum(matches.values())-1)<2e-10
    return matches

def evaluate(label,p_a,p_b):
    m=match_distribution(p_a,p_b)
    p_margin=sum(w for (a,b,won,n),w in m.items() if a>b)
    p_match=sum(w for (a,b,won,n),w in m.items() if won)
    p_over=sum(w for (a,b,won,n),w in m.items() if a+b>23.5)
    p_dec=sum(w for (a,b,won,n),w in m.items() if n==3)
    ea=sum(a*w for (a,b,won,n),w in m.items())
    eb=sum(b*w for (a,b,won,n),w in m.items())
    p_different = sum(w for (a,b,won,n),w in m.items() if (a>b)!=won)
    print(label, 'point-A=',p_a,'point-B=',p_b,'hold-A=',round(hold(p_a),5),'hold-B=',round(hold(p_b),5), 'P(A match)=',round(p_match,5), 'P(A +0.5 games)=',round(p_margin,5), 'P(B -0.5 games)=',round(1-p_margin,5),'P(Over23.5)=',round(p_over,5),'P(Under23.5)=',round(1-p_over,5),'P(decider)=',round(p_dec,5),'E games A/B/T=',round(ea,3),round(eb,3),round(ea+eb,3),'opposite winner/game leader=',round(p_different,4),'states=',len(m))
    return m

if __name__=='__main__':
    # Tirante 64.6% serve points won, 36.0% return points won; Shevchenko 60.1% serve, 35.7% return.
    # Neutral opponent blend: p_A=(own serve P + (1 - opponent return P))/2; similarly p_B.
    a=(.646+(1-.357))/2
    b=(.601+(1-.360))/2
    evaluate('neutral_unadjusted',a,b)
    evaluate('illustrative_indoor_Shev_plus_point',a-.008,b+.010)
    evaluate('illustrative_both_serve_stronger',a+.015,b+.015)
    evaluate('illustrative_both_serve_weaker',a-.015,b-.015)
    evaluate('illustrative_Shev_major_increase',a-.015,b+.020)

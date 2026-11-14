from functools import lru_cache
from collections import defaultdict
from math import comb

def hold(p):
    q=1-p
    pre=p**4*(1+4*q+10*q*q)
    deuce=comb(6,3)*p**3*q**3
    win_deuce=p*p/(p*p+q*q)
    return pre+deuce*win_deuce

def tiebreak(pa,pb,first):
    @lru_cache(None)
    def pwin(a,b):
        if (a>=7 or b>=7) and abs(a-b)>=2:return float(a>b)
        if a==b and a>=6:
            pw2=pa*(1-pb)
            pl2=(1-pa)*pb
            return pw2/(pw2+pl2)
        i=a+b
        # first point first server, then blocks of 2 serves
        srv=first if i==0 or ( (i-1)//2)%2==1 else 1-first
        prob=pa if srv==0 else 1-pb
        return prob*pwin(a+1,b)+(1-prob)*pwin(a,b+1)
    return pwin(0,0)

def score_set(pa,pb,first):
    ha,hb=hold(pa),hold(pb)
    out=defaultdict(float)
    def rec(a,b,mass):
        if (a==6 and b<=4) or (b==6 and a<=4) or (a==7 and b==5) or (b==7 and a==5):
            out[(a,b)]+=mass;return
        if a==6 and b==6:
            t=tiebreak(pa,pb,first)
            out[(7,6)]+=mass*t
            out[(6,7)]+=mass*(1-t)
            return
        srv=first if (a+b)%2==0 else 1-first
        pwin=ha if srv==0 else 1-hb
        rec(a+1,b,mass*pwin);rec(a,b+1,mass*(1-pwin))
    rec(0,0,1.0)
    return out

def match(pa,pb):
    sets={0:score_set(pa,pb,0), 1:score_set(pa,pb,1)}
    joint=defaultdict(float)
    def rec(sw_a,sw_b,ga,gb,first,prob,ns):
        if sw_a==2 or sw_b==2:
            joint[(sw_a,sw_b,ga,gb,ns)]+=prob
            return
        for (a,b),p in sets[first].items():
            next_srv=first if (a+b)%2==0 else 1-first
            rec(sw_a+(a>b),sw_b+(b>a),ga+a,gb+b,next_srv,prob*p,ns+1)
    # initial service randomized equally
    for f in (0,1):rec(0,0,0,0,f,.5,0)
    mass=sum(joint.values())
    ea=sum(a*v for (_,_,a,b,n),v in joint.items())
    eb=sum(b*v for (_,_,a,b,n),v in joint.items())
    pma=sum(v for (sa,sb,a,b,n),v in joint.items() if sa==2)
    pua=sum(v for (sa,sb,a,b,n),v in joint.items() if a+b<=23)
    pplus=sum(v for (sa,sb,a,b,n),v in joint.items() if a>=b)
    pdec=sum(v for (sa,sb,a,b,n),v in joint.items() if n==3)
    return {"p_sv_win":pma,"p_sv_plus_0_5":pplus,"p_vi_minus_0_5":1-pplus,"p_under_23_5":pua,"p_over_23_5":1-pua,"expected_games_sv":ea,"expected_games_vi":eb,"expected_total":ea+eb,"expected_margin_sv":ea-eb,"p_decider":pdec,"sum":mass}

if __name__=='__main__':
    for pa,pb in [(.618,.612),(.640,.6335),(.645,.625),(.635,.64),(.655,.625),(.630,.630),(.620,.645),(.645,.660)]:
        print(pa,pb,match(pa,pb))

import numpy as np

def game_prob(p):
    # Probability server wins game with ad scoring
    # P(win before deuce):
    # 4-0: p^4
    # 4-1: 4 * p^4 * (1-p)
    # 4-2: 10 * p^4 * (1-p)^2
    # Reach deuce (3-3): 20 * p^3 * (1-p)^3
    # From deuce: p^2 / (p^2 + (1-p)^2)
    p_before = p**4 * (1 + 4*(1-p) + 10*(1-p)**2)
    p_deuce = 20 * (p**3) * ((1-p)**3)
    p_hold_deuce = (p**2) / (p**2 + (1-p)**2)
    return p_before + p_deuce * p_hold_deuce

def sim_tiebreak(p_a_serve, p_b_serve, server):
    # 7-point tiebreak
    pts_a = 0
    pts_b = 0
    cur_server = server
    pt_count = 0
    while True:
        if cur_server == 'A':
            if np.random.rand() < p_a_serve:
                pts_a += 1
            else:
                pts_b += 1
        else:
            if np.random.rand() < p_b_serve:
                pts_b += 1
            else:
                pts_a += 1
        
        pt_count += 1
        if pt_count == 1:
            cur_server = 'B' if cur_server == 'A' else 'A'
        elif pt_count % 2 == 1:
            cur_server = 'B' if cur_server == 'A' else 'A'
            
        if (pts_a >= 7 or pts_b >= 7) and abs(pts_a - pts_b) >= 2:
            break
            
    winner = 'A' if pts_a > pts_b else 'B'
    return winner, pts_a, pts_b

def sim_set(p_a_serve, p_b_serve, first_server):
    g_a = 0
    g_b = 0
    cur_server = first_server
    hold_a = game_prob(p_a_serve)
    hold_b = game_prob(p_b_serve)
    
    while True:
        if cur_server == 'A':
            if np.random.rand() < hold_a:
                g_a += 1
            else:
                g_b += 1
            cur_server = 'B'
        else:
            if np.random.rand() < hold_b:
                g_b += 1
            else:
                g_a += 1
            cur_server = 'A'
            
        if (g_a >= 6 or g_b >= 6) and abs(g_a - g_b) >= 2:
            winner = 'A' if g_a > g_b else 'B'
            return winner, g_a, g_b, cur_server
        if g_a == 6 and g_b == 6:
            tb_winner, _, _ = sim_tiebreak(p_a_serve, p_b_serve, cur_server)
            if tb_winner == 'A':
                return 'A', 7, 6, ('B' if cur_server == 'A' else 'A')
            else:
                return 'B', 6, 7, ('B' if cur_server == 'A' else 'A')

def sim_match(delta_mean=0.065, delta_sd=0.045, eps_sd=0.040, s_base=0.555, n_sims=200000):
    np.random.seed(42)
    # A = Romero Gormaz, B = Pieri
    # s_base: base service point probability in WTA clay environment (~0.555)
    # delta: baseline skill advantage of Romero Gormaz over Pieri
    # For A: serve point win rate = s_base + delta + eps
    # For B: serve point win rate = s_base - delta - eps
    
    results = []
    
    for _ in range(n_sims):
        delta = np.random.normal(delta_mean, delta_sd)
        first_server = 'A' if np.random.rand() < 0.5 else 'B'
        
        sets_a = 0
        sets_b = 0
        games_a = 0
        games_b = 0
        set_scores = []
        cur_srv = first_server
        
        while sets_a < 2 and sets_b < 2:
            eps = np.random.normal(0, eps_sd)
            p_a = np.clip(s_base + delta + eps, 0.35, 0.75)
            p_b = np.clip(s_base - delta - eps, 0.35, 0.75)
            
            set_win, ga, gb, cur_srv = sim_set(p_a, p_b, cur_srv)
            games_a += ga
            games_b += gb
            set_scores.append((ga, gb))
            if set_win == 'A':
                sets_a += 1
            else:
                sets_b += 1
                
        winner = 'A' if sets_a == 2 else 'B'
        tot_games = games_a + games_b
        margin = games_a - games_b # A minus B (Gormaz minus Pieri)
        
        results.append({
            'winner': winner,
            'sets_a': sets_a,
            'sets_b': sets_b,
            'games_a': games_a,
            'games_b': games_b,
            'tot_games': tot_games,
            'margin': margin,
            'set_scores': set_scores
        })
        
    return results

def analyze(results):
    n = len(results)
    p_a_win = sum(1 for r in results if r['winner'] == 'A') / n
    p_b_win = 1.0 - p_a_win
    
    # Families
    # B1: A straight-set control (ga >= gb + 3 each set or <= 3 conceded per set, or margin >= 6 in 2 sets)
    # Let's categorize standard families:
    # B1: A 2-0 control (tot <= 18, 2-0)
    # B2: A 2-0 close (tot >= 19, 2-0)
    # B3: A 2-1
    # B4: B 2-0 control
    # B5: B 2-0 close
    # B6: B 2-1
    
    b1 = sum(1 for r in results if r['winner'] == 'A' and r['sets_b'] == 0 and r['tot_games'] <= 18) / n
    b2 = sum(1 for r in results if r['winner'] == 'A' and r['sets_b'] == 0 and r['tot_games'] >= 19) / n
    b3 = sum(1 for r in results if r['winner'] == 'A' and r['sets_b'] == 1) / n
    b4 = sum(1 for r in results if r['winner'] == 'B' and r['sets_a'] == 0 and r['tot_games'] <= 18) / n
    b5 = sum(1 for r in results if r['winner'] == 'B' and r['sets_a'] == 0 and r['tot_games'] >= 19) / n
    b6 = sum(1 for r in results if r['winner'] == 'B' and r['sets_a'] == 1) / n
    
    tots = [r['tot_games'] for r in results]
    margins = [r['margin'] for r in results]
    
    p_over_19_5 = sum(1 for r in results if r['tot_games'] > 19.5) / n
    p_under_19_5 = 1.0 - p_over_19_5
    
    # Gormaz -5.5: margin >= 6
    # Pieri +5.5: margin <= 5 (i.e. Gormaz margin <= 5, or Pieri games + 5.5 > Gormaz games)
    p_gormaz_minus_5_5 = sum(1 for r in results if r['margin'] >= 6) / n
    p_pieri_plus_5_5 = 1.0 - p_gormaz_minus_5_5
    
    # Joint probabilities
    # Let's check all 4 contracts:
    # C1: Gormaz -5.5
    # C2: Pieri +5.5
    # C3: Over 19.5
    # C4: Under 19.5
    
    print(f"Total simulated: {n}")
    print(f"P(Gormaz win) = {p_a_win:.4f}, P(Pieri win) = {p_b_win:.4f}")
    print(f"Families: B1={b1:.4f}, B2={b2:.4f}, B3={b3:.4f}, B4={b4:.4f}, B5={b5:.4f}, B6={b6:.4f}")
    print(f"Total games: mean={np.mean(tots):.2f}, median={np.median(tots)}, 10th={np.percentile(tots, 10)}, 90th={np.percentile(tots, 90)}, sd={np.std(tots):.2f}")
    print(f"Margin (Gormaz - Pieri): mean={np.mean(margins):.2f}, median={np.median(margins)}, 10th={np.percentile(margins, 10)}, 90th={np.percentile(margins, 90)}, sd={np.std(margins):.2f}")
    print("-" * 50)
    print(f"Under 19.5 games: {p_under_19_5:.4f}")
    print(f"Over 19.5 games: {p_over_19_5:.4f}")
    print(f"Pieri +5.5 games: {p_pieri_plus_5_5:.4f}")
    print(f"Gormaz -5.5 games: {p_gormaz_minus_5_5:.4f}")
    print("-" * 50)
    
    # Joint between various pairs:
    # Under 19.5 and Pieri +5.5
    p_u_and_pieri = sum(1 for r in results if r['tot_games'] < 19.5 and r['margin'] <= 5) / n
    # Under 19.5 and Gormaz -5.5
    p_u_and_gormaz = sum(1 for r in results if r['tot_games'] < 19.5 and r['margin'] >= 6) / n
    # Over 19.5 and Pieri +5.5
    p_o_and_pieri = sum(1 for r in results if r['tot_games'] > 19.5 and r['margin'] <= 5) / n
    # Over 19.5 and Gormaz -5.5
    p_o_and_gormaz = sum(1 for r in results if r['tot_games'] > 19.5 and r['margin'] >= 6) / n
    
    print(f"P(Under 19.5 & Pieri +5.5) = {p_u_and_pieri:.4f}")
    print(f"P(Under 19.5 & Gormaz -5.5) = {p_u_and_gormaz:.4f}")
    print(f"P(Over 19.5 & Pieri +5.5) = {p_o_and_pieri:.4f}")
    print(f"P(Over 19.5 & Gormaz -5.5) = {p_o_and_gormaz:.4f}")
    
    # Common scorelines:
    from collections import Counter
    score_counts = Counter(tuple(r['set_scores']) for r in results)
    print("\nMost common scorelines:")
    for sc, cnt in score_counts.most_common(10):
        print(f"  {sc}: {cnt/n:.4f}")

if __name__ == '__main__':
    res = sim_match()
    analyze(res)

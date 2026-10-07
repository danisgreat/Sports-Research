"""Descriptive ranking metrics on one complete frozen slate, never certification."""
import math


def metrics(grades):
    if not grades or any(g not in {'WIN', 'LOSS'} for g in grades):
        return None  # Push/void/missing definitions need a separately fixed policy.
    wins = [int(g == 'WIN') for g in grades]
    discount = [1 / math.log2(i + 2) for i in range(min(2, len(wins)))]
    dcg = sum(w * d for w, d in zip(wins[:2], discount))
    ideal = sum(discount[:min(sum(wins), 2)])
    return dict(rank1=wins[0], rank2=wins[1] if len(wins) > 1 else None,
                hit_at_2=int(any(wins[:2])), wins_at_2=sum(wins[:2]),
                ndcg_at_2=dcg / ideal if ideal else None)

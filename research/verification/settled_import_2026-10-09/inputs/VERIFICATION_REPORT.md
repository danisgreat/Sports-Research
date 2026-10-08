# Local verification report — 2026-10-09

**Scope:** active local mini has 7 local sporting events P-550 through P-556 (P550 carried once), plus 65 unique canonical-reference carryover IDs. All rows preserved as issued in the frozen original.

- Frozen original length: **175,096 bytes**.
- Frozen original SHA-256: `fc1c3b4592b1df5e8ac2a9abbabb9f5945b124cf493d62e686ab59360e3f0415`.
- Appended settled copy length: **561,737 bytes**.
- Settled copy SHA-256: `62447b56fcc75c41695b5b59909a5e1ede610c885d1b3fab736eeae2e005bfe3`.
- Exact original prefix preserved: **True**.
- Prior P126–P549 retrospective supplement preserved: **353,736 original bytes**.
- Reconciliation rows: 72 unique IDs (65 original carryovers + 7 local events).
- New local cards: exactly 7; no new P-ID issued here. Historical P-550 is not part of the 65 existing canonical-reference carryover IDs.

## Newly settled sporting outcome diagnostics

| Metric | Value |
|---|---:|
| WIN / LOSS | 15 / 13 |
| PUSH / VOID / NO_ACTION | 0 / 0 / 0 |
| Rank-1 | 4/7 (57.1%) |
| Rank-2 | 3/7 (42.9%) |
| Hit@2 | 5/7 (71.4%) |
| Wins@2 | 7/14 (50.0%) |
| Binary NDCG@2 | 0.5162 |
| Winner-call correctness | 4/7 (57.1%) |

NDCG@2 uses binary W=1/L=0 relevance, discounts Rank 2 by `1/log2(3)` and compares with an ideal top-two arrangement of the **four originally issued rows**, rather than an ideal restricted to issued top two. Since two or three of four rows win in each completed match, the ideal DCG@2 is `1 + 1/log2(3)`. All contracts within an event remain dependent.

## Certification boundary

- Seven local events have completed sporting outcome evidence. Their original pregame timing, independent terminal process requirements, provider betting rules and qualified model status remain uncertified. They are NOT promoted to retrospective forecasting performance.
- The 65 older canonical-reference records retain their prior unresolved conditions and are not newly sportingly scored again. This prevents double-counting grades from historical reviews.
- GitHub main HEAD as inspected: `1ffbd9f52c63926bf7b1f5df9796e37477c1e9a3`; 0 repository writes, 0 Combined Log writes, 0 canonical-ledger writes.

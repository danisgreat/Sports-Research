# Lineage audits (SRC-04)

One `<source_id>.json` per audited collector, schema `lineage-audit-1`; see `research/operations/lineage_audit.py` for the rules and
`python -B -m research.operations.lineage_audit template SOURCE_ID` for an empty file.

**Status at the 2026-10-09 implementation: no audit has been performed.** The sandbox that built the tooling has no web access, so no
publisher documentation could be read and every registered collector stays `UNKNOWN`. The quorum rule therefore cannot be satisfied for any
league yet; this is stated, not hidden. The retrospective success criterion (at least three independent terminal collectors registered for MLB,
NBL and EPL) is OPEN until audits with retained evidence bodies exist.

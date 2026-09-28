# Audit-only permissive extraction preview (superseded)

**Not approved for scoring, training or prospective checkpoint counts.**

This was a pre-repair preview made before the extractor was tightened. It demonstrated that the earlier permissive path ingested 20 ranked rows from P-518–P-522, including 16 from four live-issued cards, without preserving horizon. **Do not use its CSV as current output.** The strict extractor has since been rerun to `research/settled_rows_2026-09-28/generated/`; it carries horizon/eligibility fields, quarantines the P-518 and P-520 conflict groups rather than selecting a row, and marks every retained row ineligible for performance counting.

The old frozen dataset was not overwritten. The strict versioned output is also descriptive only; the P-518–P-522 reconciliation register, not this old preview, records current event-specific dispositions.

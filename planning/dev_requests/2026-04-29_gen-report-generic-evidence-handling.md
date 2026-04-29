# Dev request: gen-report should handle any EvidenceItem subclass generically

**Date:** 2026-04-29
**Severity:** Medium — affects scalability of evidence integration; new evidence types currently require workflow edits to surface in reports.

---

## Principle

Any time mapping evidence of any type lands on a `MappingEdge`, `gen-report` should be able to surface it without the workflow needing per-type processing logic. Adding a new `EvidenceItem` subclass to the schema (e.g. `BulkCorrelationEvidence`) should require zero changes to `workflows/gen-report.md`.

The schema already supports this: `EvidenceItem` is the abstract parent with three required fields (`evidence_type`, `supports`, `explanation`). `explanation` is the LLM-handoff field. Subclass-specific fields (e.g. `best_f1_score` on `AnnotationTransferEvidence`, `statistics` on `BulkCorrelationEvidence`) are receipts the LLM can read alongside the explanation.

## What needs to change in gen-report

The current `workflows/gen-report.md` has type-specific logic in places — e.g. property-alignment-table generation has hard-coded rows like "Annotation transfer | F1=…". These should be replaced with a generic enumeration:

> **For each EvidenceItem on the edge:**
>
> - Render `evidence_type` as a badge or sub-section header.
> - Render `explanation` as the narrative (this is the assertion).
> - Render any other populated fields as a `key: value` details block, no special-casing per type.
> - For numeric fields (e.g. `best_f1_score`, the `statistics` map on `BulkCorrelationEvidence`), the LLM reads the values alongside the explanation and synthesises prose.

The synthesis subagent already gets the full edge YAML; the generic pattern is: pass evidence as-is, let the LLM read each item's `evidence_type` + `explanation` + remaining fields, write a paragraph or table row per item.

## Surface change

`workflows/gen-report.md`:
- Drop the dedicated AT F1 row in the property-alignment table.
- Replace with a generic "Evidence support" row (or section) that enumerates `edge.evidence[*]` with each item's `evidence_type`, `supports`, and `explanation`.
- Preserve property-comparison-table for `property_comparisons` (separate field from evidence) — that field has fixed semantics.

Optionally, the schema could grow a `headline_metric` slot on `EvidenceItem` (free string, e.g. `"F1=0.62"` or `"δ=0.090, rank 1/5322"`) that subclasses populate as a one-line summary for table display. But this can land later if needed.

## Why now

`BulkCorrelationEvidence` is now in the schema and on edges (Stephens, Knoedler) — but `gen-report` won't show it without an update. Rather than patching `gen-report` for every new evidence type as it's added, build the generic pattern once.

## Verification

After implementing:
- Re-run `gen-report` on `vmhvl_esr1_pr_neuron` (which now carries both `ATLAS_METADATA` and `BULK_CORRELATION` evidence on its SUPT_0563 edge). Confirm both evidence types surface in the report without per-type code paths.
- Re-run `gen-report` on `avpv_kiss1_neuron` — the CLUS_1915 edge has both ATLAS_METADATA and BULK_CORRELATION; both should appear.
- Add a hypothetical new evidence type (e.g. `OpticalImagingEvidence`) and confirm it surfaces with no workflow change.

## Related

This pairs with the meta-rule the user articulated: "any evidence from annotation transfer and perhaps from bulk RNA expression correlation from tightly selected neurons, deserves an edge." Lower the bar for KB writes — but only useful if reports surface those edges automatically. Generic evidence handling is what makes the lower-bar policy scalable.

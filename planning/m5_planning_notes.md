# M5 Planning Notes (2026-04-09)

Extracted from ROADMAP.md — observations from the first end-to-end annotation transfer
run (OLM hippocampus, GSE124847 → WMBv1).

Schema items S1-S3 and SC1-SC3 moved to milestone **S** (Schema Refinement) in ROADMAP.md.

---

## Report and workflow improvements

**R1. Mapping above rank 0.**
Current report structure assumes mapping at the most specific level (rank 0). When
annotation transfer shows strongest signal at a higher rank, the report should:
- Include an assessment at that rank, evaluating all rank-0 nodes within it collectively
  (soma locations, negative markers, neuropeptides)
- Frame the edge as "maps to rank N node X; rank 0 resolution pending" rather than
  picking a specific rank-0 node as the target
- Apply consistently regardless of taxonomy-specific level names

**R2. Subtype node creation.**
The schema already supports sub-nodes of classical types (e.g. Sst-OLM and Htr3a-OLM as
children of `olm_hippocampus`). This is a workflow improvement: the agent should judge
when to create sub-nodes based on source evidence (e.g. when a dataset clearly separates
subtypes with distinct expression profiles or mapping targets). Per-subtype annotation
transfer data (already available from the OLM run) would attach to the sub-node edges.

**R3. F1 heatmap visualisation.**
Add a source-label × target matrix heatmap at each taxonomy level to the annotation
transfer output or report. The MLI-PLI notebooks in `cellular_semantics_notebooks/` have
this pattern. Could be a step in the annotation-transfer workflow or a rendering option
in gen-report.

**R4. Annotation transfer → classical property bridge.**
When source data comes from genetically or morphologically defined cells (e.g.
Chrna2-Cre labelled, patch-clamped OLM), the annotation transfer inherits classical
characterisation — it's not just a transcriptomic similarity. Reports should make this
explicit: "cells were selected by [method], which confirms [markers/morphology/ephys],
so the transfer carries classical-type provenance."

**R5. Target-side expression from WMB h5ad files.**
Allen Brain Cell Atlas provides h5ad expression matrices by taxonomy class and dissection
region. These could resolve NOT_ASSESSED property comparisons (e.g. Grm1 in Sst Gaba_3
clusters) without new experiments. Documented in `workflows/annotation-transfer.md`
Step 5c. High-value, low-cost improvement.

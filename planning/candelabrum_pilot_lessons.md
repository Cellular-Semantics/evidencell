# Lessons from candelabrum cell pilot (2026-03-20)

Extracted from ROADMAP.md — observations from running lit-review.md end-to-end on a
single seed (PMID:35578131, candelabrum cell).

---

## Lit-review workflow improvements (originally M2)

**Full-text retrieval fallback chain**
artl-mcp `get_europepmc_full_text` silently returns empty on some confirmed-OA papers
(e.g. PMC9548381). Need: Unpaywall OA pre-check → artl-mcp full text → artl-mcp
PDF-to-markdown → WebFetch PMC HTML → WebFetch Unpaywall `best_oa_location.url`.
Flag retrieval failures rather than silently falling back to abstract-only. JATS XML +
local snippet generation being explored in parallel project (Asta_deepsearch).
**Status**: Still relevant — PMC fallback implemented in cite-traverse but silent
failure detection is not yet robust. Feeds into M2L (validated handovers).

**Single-seed fast path**
Skip selection step when there is one seed and max_depth≤1. The depth loop machinery
(fetch→select→fetch) adds pure overhead for targeted single-paper exploration.
**Status**: Still relevant — not implemented. Low priority unless single-seed use
cases become common.

**ASTA snippet quality filtering** ✅ Addressed
cite-traverse.md Step 2b now filters `snippetKind == "title"` and peer review sections.
Confirmed working in hippocampus GABA depth 1 run (1 peer-review snippet filtered).

**KB-first output** ✅ Addressed
`evidence-extraction.md` now exists (M2 complete). The workflow terminates at
`all_summaries.json` which feeds evidence-extraction, not at `report.md`.

**Citation traversal pipeline** ✅ Addressed
ASTA snippet_search is the primary mechanism; PMC full text is the fallback. Design
documented in `planning/citation_traversal_design.md`. Implemented in cite-traverse.md.

## Semantic validation loop for evidence placement

Iterative strategy that checks extracted evidence against the source paper for correct
placement on KB nodes/edges. During the pilot, snRNA-seq cluster markers (Nxph1,
Aldh1a3, Slc6a5) were initially placed on the `classical_candelabrum` node — but they
were measured on the PLI1 transcriptomic cluster, not on morphologically confirmed
candelabrum cells. The correction required recognising that smFISH on tissue with
spatial co-registration to Oxtr-Cre-labelled CCs constitutes independent confirmation,
while snRNA-seq cluster markers alone do not.

Key question the loop must answer: "is this evidence measured on this entity, or
inferred via a mapping edge?" If inferred → place on the source node, record inference
on the edge.
**Status**: Still relevant — not implemented. Important for evidence-extraction
correctness. Feeds into WC (workflow contracts) and evidence-extraction improvements.

## Spatial evidence from MERFISH data (originally M3+)

- **MERFISH co-location scoring**: agentic workflow to compute co-location scores
  between cell types using WMBv1 MERFISH spatial data. Automation would make this
  evidence type reproducible and scalable.
- **Allen Brain Cell Atlas link builder**: skill to generate deep links into the ABC
  website illustrating spatial placement of specific cell sets.
**Status**: Still relevant — not implemented. Independent of current priorities.

## Annotation transfer skill (originally M5)

Bounded skill for running MapMyCells annotation transfer between a source dataset and
WMBv1, computing purity/F1 metrics, and writing structured `AnnotationTransferEvidence`
to KB edges. ✅ Partially addressed — AT pipeline implemented, OLM run complete.
Orchestrator for KB import still pending (see WORKFLOW.md).

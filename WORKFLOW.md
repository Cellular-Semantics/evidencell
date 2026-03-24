# WORKFLOW.md

Guide to evidencell curation orchestrators: what to run, when, and with what inputs.

---

## Overview

The human is the top-level coordinator. Run each orchestrator when ready, review the output at each gate, and proceed at your own pace. There is no meta-orchestrator.

| Orchestrator | Location | Milestone | Status | When to run |
|---|---|---|---|---|
| `asta-report-ingest` | `workflows/asta-report-ingest.md` | M2 | **Ready** | Start here when you have an ASTA deep research PDF — proposes classical nodes + initial evidence |
| `ingest-taxonomy` | `workflows/ingest-taxonomy.md` | M1 | **Ready** | Ingest a taxonomy table → atlas cluster CellTypeNode stubs |
| `lit-review` | `workflows/lit-review.md` | M2 | **Ready** | Seed discovery when starting without a report; hands off to cite-traverse |
| `cite-traverse` | `workflows/cite-traverse.md` | M2 | **Ready** | Citation traversal + synthesis; called by lit-review and asta-report-ingest |
| `evidence-extraction` | `workflows/evidence-extraction.md` | M2 | **Ready** | After cite-traverse — extracts verified evidence items into KB YAML |
| `map-cell-type` | `workflows/map-cell-type.md` | M3 | Pending | After evidence base is built — proposes mapping edges and confidence |
| `annotation-transfer` | `workflows/annotation-transfer.md` | M5 | Pending | After AT results available — imports F1 scores as evidence |

---

## Inputs

| Input type | Location | Used by |
|---|---|---|
| ASTA deep research PDFs | `inputs/deepsearch/` | `asta-report-ingest.md` |
| Taxonomy tables (CSV/TSV) | `inputs/taxonomies/` | `ingest-taxonomy.md` |

Place input files in the appropriate subdirectory before running the relevant orchestrator.

---

## Typical workflow for a new mapping

Classical nodes emerge from research — they are not pre-created. Run these in
parallel where possible (taxonomy ingest + report ingest are independent).

```
── Discovery ──────────────────────────────────────────────────────────────────

1a. just ingest-report {region} {pdf_file}      # ASTA report → classical CellTypeNode
    → workflows/asta-report-ingest.md            # stubs + initial asta_report evidence
    [GATE] approve proposed nodes + CL mappings

1b. just ingest-taxonomy {taxonomy_file}         # taxonomy table → atlas cluster stubs
    → workflows/ingest-taxonomy.md               # (run in parallel with 1a)
    [GATE] approve field mapping + generated stubs

── Primary literature retrieval ───────────────────────────────────────────────

2.  workflows/cite-traverse.md                   # targeted retrieval per paper
    (handed off from asta-report-ingest, or      # fills gaps, verifies asta_report items,
     called directly after lit-review seeds)      # surfaces new types

    [GATE] review report.md — new types? extend scope or proceed

── Evidence extraction ─────────────────────────────────────────────────────────

3.  workflows/evidence-extraction.md             # summaries → proposed KB evidence items
    [GATE] expert reviews + approves items        # validates snippets, adjusts support

── Mapping ────────────────────────────────────────────────────────────────────

4.  workflows/map-cell-type.md                   # evidence + atlas metadata → MappingEdge
    [GATE] expert reviews proposed edges

── Reports + community ────────────────────────────────────────────────────────

5.  just gen-report {graph_file}                 # human-readable report (M4)
    [GATE] biologist reviews, executes proposed experiments

6.  workflows/annotation-transfer.md             # AT results → AnnotationTransferEvidence
```


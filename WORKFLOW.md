# WORKFLOW.md

Guide to evidencell curation orchestrators: what to run, when, and with what inputs.

---

## Overview

The human is the top-level coordinator. Run each orchestrator when ready, review the output at each gate, and proceed at your own pace. There is no meta-orchestrator.

| Orchestrator | Location | Milestone | When to run |
|---|---|---|---|
| `lit-review` | `workflows/lit-review.md` | M2 | Before curating a new cell type — builds the literature evidence corpus |
| `evidence-extraction` | `workflows/evidence-extraction.md` | M2 | After catalogue weeding — extracts evidence items from deepsearch output |
| `map-cell-type` | `workflows/map-cell-type.md` | M3 | After evidence base is built — proposes mapping edges and confidence |
| `annotation-transfer` | `workflows/annotation-transfer.md` | M5 | After experimental AT results are available — imports F1 scores as evidence |

---

## Typical workflow for a new mapping

```
1. just ingest-taxonomy {taxonomy_file}     # create CellTypeNode stubs (M1)
2. workflows/lit-review.md                 # build evidence corpus (M2)
3. [GATE] review report.md + prune catalogue
4. workflows/evidence-extraction.md        # extract LiteratureEvidence items (M2)
5. [GATE] expert reviews proposed evidence items
6. workflows/map-cell-type.md              # propose MappingEdge + confidence (M3)
7. [GATE] expert reviews proposed edges
8. just gen-report {graph_file}            # generate human-readable report (M4)
9. [GATE] biologist reviews report, executes proposed experiments
10. workflows/annotation-transfer.md       # import AT results as evidence (M5)
```

---

## Status

| Orchestrator | Status |
|---|---|
| `lit-review` | Pending (M2) — porting from Asta_deepsearch/workflows/lit-review.md |
| `evidence-extraction` | Pending (M2) |
| `map-cell-type` | Pending (M3) |
| `annotation-transfer` | Pending (M5) |

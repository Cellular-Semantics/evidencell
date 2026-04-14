# WORKFLOW.md

Guide to evidencell curation orchestrators: what to run, when, and with what inputs.

---

## Milestone status

| Milestone | Description | Status |
|---|---|---|
| M1 | Taxonomy ingest → atlas cluster stubs | **Complete** |
| M2 | Literature retrieval pipeline (ASTA ingest, cite-traverse, evidence extraction) | **Complete** |
| M3 | Mapping (property comparison, edge YAML, confidence assessment) | **Complete** |
| M4 | Report generation (summary + drill-down, LLM synthesis, anti-hallucination hooks) | **Complete** |
| M5 | Annotation transfer evidence | **In progress** — pipeline implemented, orchestrator pending |
| M7 | KB structure cleanup (Phase 1: directory restructure) | **Complete** |

---

## How to run a workflow

When asked to run a workflow, open the referenced orchestrator in `workflows/` and execute
its steps in order. The orchestrator is the authority — do not plan independently or
research prerequisites that the orchestrator already addresses. Use the skills and tools
it references. Stop at steps marked `[GATE]` and present results for human review before
proceeding.

---

## Overview

The human is the top-level coordinator. Run each orchestrator when ready, review the output at each gate, and proceed at your own pace. There is no meta-orchestrator.

| Orchestrator | Location | Milestone | Status | When to run |
|---|---|---|---|---|
| `ingest-taxonomy` | `workflows/ingest-taxonomy.md` | M1 | **Ready** | Ingest a taxonomy table → atlas cluster CellTypeNode stubs |
| `asta-report-ingest` | `workflows/asta-report-ingest.md` | M2 | **Ready** | Start here when you have an ASTA deep research PDF — proposes classical nodes + initial evidence |
| `lit-review` | `workflows/lit-review.md` | M2 | **Ready** | Seed discovery when starting without a report; hands off to cite-traverse |
| `cite-traverse` | `workflows/cite-traverse.md` | M2 | **Ready** | Citation traversal + synthesis; called by lit-review and asta-report-ingest |
| `evidence-extraction` | `workflows/evidence-extraction.md` | M2 | **Ready** | After cite-traverse — extracts verified evidence items into KB YAML |
| `map-cell-type` | `workflows/map-cell-type.md` | M3 | **Ready** | Discovery mode: finds candidate atlas matches from property overlap; hypothesis mode: tests curator's proposed mapping. Produces MappingEdge YAML with property comparisons. Can run on stubs (LOW confidence) or after lit review. |
| `gen-report` | `workflows/gen-report.md` | M4 | **Ready** | Generate summary + drill-down reports from KB YAML; LLM synthesis with hallucination guard (ID/quote/PMID/accession validation via pre-write hook) |
| `annotation-transfer` | `workflows/annotation-transfer.md` | M5 | **Pipeline ready** | Dataset retrieval → MapMyCells → F1 matrix → AnnotationTransferEvidence; marker assessment moved to `map-cell-type` |

---

## Anti-hallucination infrastructure

A pre-write hook (`.claude/hooks/validate_mapping_hook.py`) runs automatically before
every `Write` or `Edit` to KB files. It is **not** an orchestrator step — it fires on all
KB writes regardless of which workflow is running.

**KB YAML** (`kb/**/*.yaml`) — blocks writes with: YAML parse errors, structural
integrity failures (dangling edges, duplicate IDs, placeholder snippets), `quote_key`
values absent from `references.json`, `PMID:`/`DOI:` citations absent from
`references.json`, LinkML schema non-conformance.

**Markdown reports** (`reports/{region}/*.md`) — blocks writes with: blockquote blocks
missing a `<!-- quote_key: X -->` attribution annotation, quote keys or PMIDs absent
from `references/{region}/references.json`.

See [`.claude/anti-hallucination-hooks.md`](.claude/anti-hallucination-hooks.md) for
the full specification and correction loop protocol.

---

## Inputs

| Input type | Location | Used by |
|---|---|---|
| ASTA deep research PDFs | `inputs/deepsearch/` | `asta-report-ingest.md` |
| Taxonomy tables (CSV/TSV) | `inputs/taxonomies/` | `ingest-taxonomy.md` |
| Precomputed stats HDF5 | taxonomy local paths (see M8) | `map-cell-type.md` (target-side marker cross-check), `annotation-transfer.md` (local MapMyCells) |

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
    max_depth: 1 when coming from asta-report-ingest (ASTA already provides broad
    coverage; one level targets Round 2 ambiguities without duplicating discovery)
    max_depth: 2 when starting from lit-review seeds (no prior broad coverage)

    [GATE] review report.md — new types? extend scope or proceed

── Evidence extraction ─────────────────────────────────────────────────────────

3.  workflows/evidence-extraction.md             # summaries → proposed KB evidence items
    [GATE] expert reviews + approves items        # validates snippets, adjusts support

── Mapping ────────────────────────────────────────────────────────────────────

4.  workflows/map-cell-type.md                   # evidence + atlas metadata → MappingEdge
    [GATE] expert reviews proposed edges

── Reports + community ────────────────────────────────────────────────────────

5.  just gen-facts {graph_file} {node_id}        # extract structured facts (M4)
    → workflows/gen-report.md                    # LLM synthesis + ID/quote validation
    [GATE] biologist reviews, executes proposed experiments

6.  workflows/annotation-transfer.md             # AT results → AnnotationTransferEvidence
```


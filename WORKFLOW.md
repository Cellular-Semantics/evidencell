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
| M8 | Taxonomy reference DB — compact YAML + SQLite query index | **In progress** — Phase 1 complete; Phase 2–3: KB graphs use minimal taxonomy ref stubs |
| S1 | Taxonomy rank encoding — integer ranks replace hardcoded level names | **Complete** — schema, ingest, DB, find-candidates, map-cell-type all use integer ranks |

---

## How to run a workflow

When asked to run a workflow, open the referenced orchestrator in `workflows/` and execute
its steps in order. The orchestrator is the authority — do not plan independently or
research prerequisites that the orchestrator already addresses. Use the skills and tools
it references. Stop at steps marked `[GATE]` and present results for human review before
proceeding.

---

## KB data management principles

### Properties live on nodes; edges compare

All biological properties (markers, NT type, anatomy, sex ratio, expression
profiles) are stored on `CellTypeNode` entries. Mapping edges document how
properties on two nodes compare — they never introduce new property assertions.
This means the mapper always sees a node's full property set regardless of which
mapping graph references it.

### Taxonomy reference YAML is canonical for atlas properties

Atlas node properties belong in `kb/taxonomy/{id}/*.yaml`, not on stub nodes
inside mapping graphs. Mapping graphs reference taxonomy nodes by accession;
stubs carry only: `id`, `name`, `definition_basis`, `taxonomy_id`,
`cell_set_accession`.

**Known violation:** `precomputed_expression` blocks currently live on atlas
stubs in `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`.
These should migrate to the taxonomy reference store using
`just add-expression` (see below).

### Taxonomy update operations

Two managed operations update taxonomy YAML while preserving enrichments:

- **`just add-expression`** — write `PrecomputedExpression` blocks from HDF5
  stats to taxonomy nodes. Requires a gene mapping TSV (generate once with
  `just generate-gene-mapping`). Supports cluster and supertype levels.
- **`just reingest`** — re-ingest from source JSON while preserving enrichment
  fields (`precomputed_expression`, `electrophysiology`, `morphology`, etc.).
  Nodes removed in the new source are flagged for review, not silently dropped.
  Use `just reingest-dry` to preview changes.

Field ownership is explicit: `INGEST_FIELDS` are replaced from the new source,
`ENRICHMENT_FIELDS` are preserved from old data. Both sets are declared in
`src/evidencell/taxonomy_ops.py`.

The old flush-and-replace ingest (`just ingest-taxonomy-db`) still works but
does NOT preserve enrichments. Use `just reingest` when taxonomy nodes have
post-ingest enrichments.

### Provenance

The schema provides `PropertySource` as a general provenance record: `ref`
(PMID or DOI), `method`, `scope`, `snippet`/`quote_key`, `notes`.

As of v0.8.0, provenance is nested on property objects rather than in
separate per-property source fields. Each property carries its own `sources`
list:

- `electrophysiology.sources` — on `ElectrophysiologyProfile`
- `morphology.sources` — on `MorphologyProfile`
- `anatomical_location[].sources` — on each `AnatomicalLocation` entry
- `nt_type.sources` — on `NeurotransmitterType`
- `GeneDescriptor.sources` — as `MarkerSource` (adds `marker_type`)

This gives natural scoping (each source is attached to the assertion it
supports), clean RDF mapping (blank nodes, no reification needed), and
eliminates the former per-property field proliferation (`ephys_sources`,
`morphology_sources`, `location_sources` — all removed in v0.8.0).

`definition_references` (list of PMID/DOI strings) is retained as a
flat field — these are general node-level citations, not property-scoped.

Atlas node provenance follows a different convention: properties from
taxonomy ingest have implicit provenance from `taxonomy_meta.yaml`
(`source_file`, `ingest_date`). No per-field `PropertySource` entries are
needed on `ATLAS_TRANSCRIPTOMIC` nodes — the atlas and `cell_set_accession`
are the citation.

### Use `notes` fields, not YAML comments

YAML comments (`# ...`) are not preserved by programmatic round-trips
(e.g. `yaml.safe_load()` → `yaml.dump()`). Any annotation that must
survive automated processing — caveats, heterogeneity observations,
cross-references to other nodes — belongs in a `notes` field on the
relevant object, not in a YAML comment. Reserve comments for transient
developer-facing hints that are acceptable to lose.

---

## Overview

The human is the top-level coordinator. Run each orchestrator when ready, review the output at each gate, and proceed at your own pace. There is no meta-orchestrator.

| Orchestrator | Location | Phase | Status | When to run |
|---|---|---|---|---|
| `ingest-taxonomy` | `workflows/ingest-taxonomy.md` | Discovery | **Ready** | Ingest a taxonomy table → atlas cluster CellTypeNode stubs |
| `asta-report-ingest` | `workflows/asta-report-ingest.md` | Literature | **Ready** | Start here when you have an ASTA deep research PDF — proposes classical nodes + initial evidence |
| `survey` | `workflows/survey.md` | Literature | **Ready** | Broad snippet scan of ASTA corpus for a region → all_summaries.json; no synthesis, no KB write |
| `lit-review` | `workflows/lit-review.md` | Literature | **Experimental stub** | Seed discovery when starting without a report; may be revived; do not use in regular workflows |
| `cite-traverse` | `workflows/cite-traverse.md` | Literature | **Ready** | Citation traversal + synthesis; call as a skill for targeted follow-up, not primary discovery |
| `evidence-extraction` | `workflows/evidence-extraction.md` | Literature | **Ready** | After survey or asta-report-ingest — writes PropertySource entries with quote_key to KB YAML |
| `map-cell-type` | `workflows/map-cell-type.md` | Mapping | **Ready** | Discovery mode: queries taxonomy DB at multiple ranks (0=leaf, 1, 2…) for candidate atlas matches; hypothesis mode: tests curator's proposed mapping. Uses `just find-candidates` with rank parameter. Produces MappingEdge YAML with property comparisons. Can run on stubs (LOW confidence) or after lit review. |
| `gen-report` | `workflows/gen-report.md` | Reporting | **Ready** | Generate summary + drill-down reports from KB YAML; LLM synthesis with hallucination guard (ID/quote/PMID/accession validation via pre-write hook) |
| `annotation-transfer` | `workflows/annotation-transfer.md` | Evidence transfer | **Pipeline ready** | Dataset retrieval → MapMyCells → F1 matrix → AnnotationTransferEvidence; marker assessment moved to `map-cell-type` |

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
| ASTA corpus IDs | `research/{region}/{run}/pdf_corpus_ids.json` (asta-report-ingest output) | `survey.md` |
| Taxonomy tables (JSON/CSV/TSV) | `inputs/taxonomies/` | `ingest-taxonomy.md` |
| Taxonomy reference YAML | `kb/taxonomy/{taxonomy_id}/` | `map-cell-type.md`, `ingest-taxonomy.md` (M8) |
| Taxonomy SQLite index | `kb/taxonomy/{taxonomy_id}/{taxonomy_id}.db` | `map-cell-type.md` (candidate queries) |
| Taxonomy field mapping | `kb/taxonomy/{taxonomy_id}/field_mapping.json` | `ingest-taxonomy.md` (fast-path detection) |
| MBA ontology JSON | `conf/mba/mbao-full.json` (gitignored; fetch with `just fetch-mba-ontology`) | `ingest-taxonomy.md` Step 4 (anat closure build); shared across all taxonomies |
| Precomputed stats HDF5 | taxonomy local paths (see ROADMAP.md § Taxonomy Reference DB) | `map-cell-type.md` (target-side marker cross-check), `annotation-transfer.md` (local MapMyCells) |

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

1b. just ingest-taxonomy-db {taxonomy_file} {taxonomy_id}  # full taxonomy → YAML + SQLite
    → workflows/ingest-taxonomy.md                         # (run in parallel with 1a)
    [GATE] approve field mapping + generated stubs

── Primary literature retrieval ───────────────────────────────────────────────

2.  workflows/survey.md                          # ASTA corpus → all_summaries.json
    region: {region}                             # one pass, all ASTA papers, all nodes
    corpus_ids_file: research/{region}/.../pdf_corpus_ids.json
    output_dir: research/{region}/survey_{date}/

── Evidence extraction ─────────────────────────────────────────────────────────

3.  workflows/evidence-extraction.md             # per-node: all_summaries.json → KB YAML
    summaries_file: research/{region}/survey_{date}/all_summaries.json
    # no paper selection gate for ASTA survey runs
    # run once per node_id

── Mapping ────────────────────────────────────────────────────────────────────

4.  workflows/map-cell-type.md                   # evidence + atlas metadata → MappingEdge
    [GATE] expert reviews proposed edges

── Reports + community ────────────────────────────────────────────────────────

5.  just gen-facts {graph_file} {node_id}        # extract structured facts
    → workflows/gen-report.md                    # LLM synthesis + ID/quote validation
    [GATE] biologist reviews, executes proposed experiments

6.  workflows/annotation-transfer.md             # AT results → AnnotationTransferEvidence
```


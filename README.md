# evidencell

A structured knowledge base for cell type mapping evidence, linking classical cell type descriptions to clusters in modern transcriptomic atlases.

Cell type classification is undergoing a transition. Classical neuroscience built up rich descriptions of cell types over decades — defined by morphology, electrophysiology, connectivity, neurotransmitter phenotype, and marker expression. Modern single-cell transcriptomics has produced large-scale atlases (BICCN, HMBA) with thousands of molecularly defined clusters. These two vocabularies do not map cleanly onto each other, and the mappings that do exist are rarely documented with explicit, traceable evidence.

evidencell addresses this by treating each mapping as an **evidence graph**: structured nodes for classical and atlas types, structured edges recording the relationship (equivalent, partial overlap, cross-cutting, etc.), and typed evidence items — literature, atlas metadata, annotation transfer results — each with a verbatim source quote and a confidence assessment. The result is a KB where every mapping claim has a documented evidence trail and a machine-readable confidence level, and where gaps and conflicts are first-class data.

---

## How it works

Curation in evidencell is a **guided agentic workflow**. You work with Claude Code as a co-curator: Claude handles literature search, evidence extraction, and schema-compliant YAML drafting; you provide the biological expertise and hold the review gates. Nothing commits to the canonical KB without passing validation and expert sign-off.

The pipeline runs in phases, each driven by an orchestrator in `workflows/`:

```
1. Ingest taxonomy         Parse an atlas data release → CellTypeNode stubs
                           just ingest-taxonomy {taxonomy_file}

2. Literature review       Run deepsearch on a cell type topic → evidence corpus
                           workflows/lit-review.md

3. [GATE] Catalogue review  You review the paper list, prune irrelevant papers

4. Evidence extraction     Extract LiteratureEvidence items from the corpus
                           workflows/evidence-extraction.md

5. [GATE] Evidence review   You approve, edit, or reject proposed evidence items

6. Mapping hypotheses      Propose MappingEdge + confidence from evidence + atlas metadata
                           workflows/map-cell-type.md

7. [GATE] Mapping review    You review proposed edges and confidence assessments

8. Report generation       Human-readable report: evidence chain, caveats, proposed experiments
                           just gen-report {graph_file}

9. Annotation transfer     Import AT results (MapMyCells, Seurat) as structured evidence
                           workflows/annotation-transfer.md
```

Gates are not optional. The human is the top-level coordinator throughout — each phase produces output for review before the next phase begins. Claude does not proceed past a gate autonomously.

---

## The evidence model

Each KB file is a mapping graph for a brain region. It contains:

- **`CellTypeNode`** — one per type (classical or atlas cluster), with markers, anatomy, NT type, and definition references
- **`MappingEdge`** — one per proposed correspondence, with relationship type, confidence, caveats, and a structured property comparison
- **Evidence items** (typed) — `LiteratureEvidence`, `AtlasMetadataEvidence`, `AnnotationTransferEvidence`, and others; each with a verbatim snippet and source ID

Confidence levels (`HIGH`, `MODERATE`, `LOW`, `UNCERTAIN`, `REFUTED`) follow a decision guide: HIGH requires ≥2 independent evidence types including ≥1 experimental. The schema enforces structure; the confidence rationale is human-reviewed.

---

## Aims and ambitions

- **Transparency**: every mapping claim has a documented evidence trail. Absence of evidence and active conflicts are recorded, not hidden.
- **Reusability**: the schema and KB are designed to complement existing resources (Allen Brain Atlas, Cell Ontology, BICAN taxonomy) rather than duplicate them. The contribution is the evidence layer.
- **Scalability**: the agentic workflow is designed to work at the scale of a full atlas — dozens to hundreds of cell types per region — without requiring a specialist to read every paper manually.
- **Experimental agenda**: the KB is not just a record of what is known. It is a systematic account of what is uncertain, and the report pipeline turns that into a prioritised list of proposed experiments.
- **Community curation**: the schema and workflow are built to support GitHub-based community contributions with automated review, compliance scoring, and structured PR feedback.

---

## Getting started

```bash
# Install dependencies
just install

# Prime OAK ontology databases (large one-time download)
just fetch-oak-dbs

# Validate the draft KB examples
just qc-draft

# See all available commands
just --list
```

Draft examples (work-in-progress) are in `kb/draft/`. Canonical validated entries live in `kb/mappings/`. To graduate a draft entry: run `just qc-draft`, fix any issues, then move the file to `kb/mappings/`.

See `WORKFLOW.md` for the full curation workflow guide.
See `CLAUDE.md` for development and architecture guidelines.

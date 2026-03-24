# evidencell

A structured knowledge base for cell type mapping evidence, linking classical cell type descriptions to clusters in modern transcriptomic atlases.

Cell type classification is undergoing a transition. Classical neuroscience built up rich descriptions of cell types over decades — defined by morphology, electrophysiology, connectivity, neurotransmitter phenotype, and marker expression. Modern single-cell transcriptomics has produced large-scale atlases (BICCN, HMBA) with thousands of molecularly defined clusters. These two vocabularies do not map cleanly onto each other, and the mappings that do exist are rarely documented with explicit, traceable evidence.

evidencell addresses this by treating each mapping as an **evidence graph**: structured nodes for classical and atlas types, structured edges recording the relationship (equivalent, partial overlap, cross-cutting, etc.), and typed evidence items — literature, atlas metadata, annotation transfer results — each with a verbatim source quote and a confidence assessment. The result is a KB where every mapping claim has a documented evidence trail and a machine-readable confidence level, and where gaps and conflicts are first-class data.

---

## How it works

Curation in evidencell is a **guided agentic workflow** using [Claude Code](https://claude.ai/claude-code). Claude handles literature search, evidence extraction, and schema-compliant YAML drafting; you provide the biological expertise and hold the review gates. Nothing commits to the canonical KB without passing validation and expert sign-off.

The pipeline runs in phases. Each phase is an orchestrator in `workflows/` that you hand to Claude Code — Claude runs it, you review the output at each gate, and proceed when ready:

| Phase | Orchestrator | What it does |
|---|---|---|
| 1 | `workflows/ingest-taxonomy.md` | Parse atlas taxonomy table (`inputs/taxonomies/`) → `CellTypeNode` stubs |
| 2a | `workflows/lit-review.md` | Automated deepsearch → evidence corpus + report |
| 2b | `workflows/asta-report-ingest.md` | Ingest ASTA deep research PDF (`inputs/deepsearch/`) → evidence corpus |
| 3 | `workflows/evidence-extraction.md` | Corpus → proposed `LiteratureEvidence` items |
| 4 | `workflows/map-cell-type.md` | Evidence + atlas metadata → `MappingEdge` hypotheses |
| 5 | `workflows/annotation-transfer.md` | AT results → `AnnotationTransferEvidence` |

Gates between phases are not optional. Claude does not proceed past a gate autonomously.

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

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and the full curation walkthrough.

See [WORKFLOW.md](WORKFLOW.md) for the orchestrator guide (which workflow to run, when, and with what inputs).

See [CLAUDE.md](CLAUDE.md) for development and architecture guidelines.

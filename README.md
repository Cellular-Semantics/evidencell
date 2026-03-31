# evidencell

A structured knowledge base for cell type mapping evidence, linking classical cell type descriptions to clusters in modern transcriptomic atlases.

Cell type classification is undergoing a transition. Classical neuroscience built up rich descriptions of cell types over decades — defined by morphology, electrophysiology, connectivity, neurotransmitter phenotype, and marker expression. Modern single-cell transcriptomics has produced large-scale atlases (BICCN, HMBA) with thousands of molecularly defined clusters. These two vocabularies do not map cleanly onto each other, and the mappings that do exist are rarely documented with explicit, traceable evidence.

evidencell addresses this by treating each mapping as an **evidence graph**: 
structured nodes for classical and atlas types, structured edges recording the relationship (equivalent, partial overlap, cross-cutting, etc.), and typed evidence items — literature, atlas metadata, annotation transfer results — each with a verbatim source quote and a confidence assessment. The result is a KB where every mapping claim has a documented evidence trail and a machine-readable confidence level, and where gaps and conflicts are first-class data.

---

## How it works

Curation in evidencell is a **guided agentic workflow**. You work with Claude Code as a co-curator: Claude handles taxonomy loading, literature search, evidence extraction, ontology mapping and schema-compliant YAML drafting; you provide the biological expertise and review gates _human readable_ reports at key 'report gates'. Nothing commits to the canonical KB without passing validation and expert sign-off.

**Anti-hallucination hooks** block writes before they reach disk. No KB YAML or Markdown report is saved if it fails any of:

- Schema non-conformance (LinkML validation)
- Duplicate node IDs, dangling edge references, or placeholder snippets
- `quote_key` values not present in `references.json`
- `PMID:` / `DOI:` citations not present in `references.json`
- Blockquotes in reports without a `<!-- quote_key: X -->` attribution annotation
- PMIDs in reports not registered in `references.json`

All failures are returned as structured errors for the agent to correct. The hook runs synchronously on every `Write` / `Edit` to `kb/`. See [`.claude/anti-hallucination-hooks.md`](.claude/anti-hallucination-hooks.md) for the full specification.

Literature review uses ASTA-API/MCP under the hood. All assertions extracted from the literature include evidence and supporting verbatim quotes (content-hash keyed in `references.json`).

The pipeline runs in phases, each driven by an orchestrator in `workflows/`:

1. **Ingest taxonomy** — load any taxonomy format, map to schema + ontologies, generate atlas cluster stubs
   `workflows/ingest-taxonomy.md`
   *[GATE] approve field mapping + generated stubs*

2. **ASTA report ingest** — ASTA deep research PDF → classical `CellTypeNode` stubs + initial evidence
   `workflows/asta-report-ingest.md`
   *[GATE] approve proposed nodes + CL mappings*

3. **Literature retrieval** — targeted citation traversal per paper, verifies evidence, surfaces new types
   `workflows/cite-traverse.md`
   *[GATE] review traversal report — extend scope or proceed*

4. **Evidence extraction** — summaries → proposed KB evidence items, snippets, support assessments
   `workflows/evidence-extraction.md`
   *[GATE] expert reviews and approves items*

5. **Mapping** — evidence + atlas metadata → `MappingEdge` YAML with property comparisons and confidence
   `workflows/map-cell-type.md`
   *[GATE] expert reviews proposed edges*

6. **Report generation** — LLM-synthesised summary + per-paper drill-down reports; all IDs and quotes validated by hook before write
   `workflows/gen-report.md`
   *[GATE] biologist reviews; executes proposed experiments*

7. **Annotation transfer** — import AT results (MapMyCells, Seurat) as structured evidence
   `workflows/annotation-transfer.md`
   *(planned)*

Gates are not optional. The human is the top-level coordinator throughout — each phase produces output for review before the next phase begins. Claude does not proceed past a gate autonomously.

---

## The evidence model

Each KB file is a mapping graph for a brain region. It contains:

- **`CellTypeNode`** — one per type (classical or atlas cluster), with markers, anatomy, NT type, synonyms, references.
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

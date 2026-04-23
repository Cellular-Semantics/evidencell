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

All failures are returned as structured errors for the agent to correct. The hook runs synchronously on every `Write` / `Edit` to `kb/` and `reports/`. See [`.claude/anti-hallucination-hooks.md`](.claude/anti-hallucination-hooks.md) for the full specification.

Literature review uses ASTA-API/MCP under the hood. All assertions extracted from the literature include evidence and supporting verbatim quotes (content-hash keyed in `references.json`).

The pipeline runs in phases, each driven by an orchestrator in `workflows/`:

1. **Ingest taxonomy** — load a taxonomy from any source format into a queryable reference DB; generate atlas cluster stubs for use in mapping graphs
   `workflows/ingest-taxonomy.md` — single entry point for all source types:
   - **KG-backed** (neo4j bolt endpoint): run stored cypher via `just fetch-taxonomy-kg`, then `just ingest-taxonomy-db`
   - **Ad hoc** (CSV / XLSX / non-KG JSON): `workflows/ingest-adhoc-taxonomy.md` — agent inspects source, confirms field mapping, writes per-level YAML directly
   - Ingest reads `inputs/taxonomies/{id}_meta.yaml` to record taxonomy name, species, tissue, anatomy ontology, and MapMyCells file references
   - Output: per-level YAML in `kb/taxonomy/{id}/` + SQLite query index (`just build-taxonomy-db {id}`) — DB is gitignored and re-built from YAML as needed
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

6. **Report generation** — three-tier human-readable output from KB YAML:
   - *Region index* — one row per classical type, best hit, confidence, candidate count
   - *Per-type summary* — candidates table, referenced evidence paragraphs, consolidated proposed experiments
   - *Per-paper drill-down* — verbatim quotes per property, alignment scorecard, critical gap + bridging experiment
   `just gen-report {graph_file}` or `just gen-report-draft {region}` for draft KB content
   *[GATE] biologist reviews; executes proposed experiments*

7. **Annotation transfer** — run MapMyCells (web API or local) against a reference taxonomy; score results as F1 matrices; import as `AnnotationTransferEvidence` items that can upgrade mapping confidence from MODERATE to HIGH
   `workflows/annotation-transfer.md`
   Pipeline stages: preflight → convert → map → score → *(KB import: pending automation)*
   Local MapMyCells files: `just at-download-taxonomy {id}` — downloads to `conf/mapmycells/{id}/` (gitignored, re-fetchable) and records paths in `kb/taxonomy/{id}/taxonomy_meta.yaml`

Gates are not optional. The human is the top-level coordinator throughout — each phase produces output for review before the next phase begins. Claude does not proceed past a gate autonomously.

---

## The evidence model

Each KB file is a mapping graph for a brain region. It contains:

- **`CellTypeNode`** — one per type (classical or atlas cluster), with markers, anatomy, NT type, synonyms, references.
- **`MappingEdge`** — one per proposed correspondence, with relationship type, confidence, caveats, and a structured property comparison table.
- **Evidence items** (typed):
  - `LiteratureEvidence` — peer-reviewed paper with verbatim snippet, PMID/DOI, study type
  - `AtlasMetadataEvidence` — atlas taxonomy metadata (markers, MERFISH location, NT type, CCF distribution)
  - `AtlasQueryEvidence` — curator-performed interactive query against an atlas browser (ABC Atlas, Allen Brain Map) with filter parameters and `query_url`; reproducible given the same atlas version
  - `AnnotationTransferEvidence` — computational label transfer results (MapMyCells, Seurat) with F1 per taxonomy level
  - `PatchSeqEvidence`, `ElectrophysiologyEvidence`, `MorphologyEvidence` — experimental evidence types

**Taxonomy reference DB** — each ingested atlas taxonomy lives in `kb/taxonomy/{id}/` as per-level YAML files (source of truth) plus a SQLite query index (gitignored build artifact). The YAML files are schema-compliant `CellTypeNode` objects (wrapped in `TaxonomyNodeList` containers) with a unified `markers` list that encodes marker role via `MarkerCategory` (DEFINING, DEFINING_SCOPED, TF, NEUROPEPTIDE, MERFISH). The SQLite index exposes anatomical closure tables (built from the Mouse Brain Atlas Ontology), CL mapping coverage, NT type — including propagation from cluster to supertype for atlases where NT type is only stored at cluster level — and category-scoped marker queries. Raw expression data (full-transcriptome cluster means) lives in the precomputed stats HDF5 downloaded separately via `just at-download-taxonomy`; the SQLite DB does not replicate it.

All location data from spatial transcriptomics (MERFISH) reflects **soma position only**. Axonal and dendritic projection targets are recorded separately in `morphology_notes` and are not used in atlas location comparisons.

Confidence levels (`HIGH`, `MODERATE`, `LOW`, `UNCERTAIN`) follow a decision guide: HIGH requires ≥2 independent evidence types including ≥1 experimental (annotation transfer, electrophysiology, or morphological reconstruction) — not achievable from literature alone. The schema enforces structure; the confidence rationale is human-reviewed.

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

See [CLAUDE.md](CLAUDE.md) for the default curation guide (which workflow to run, when, and with what inputs). This is the file Claude Code loads automatically in curation sessions.

See [CLAUDE_dev.md](CLAUDE_dev.md) for the dev-mode companion — development and architecture guidelines. Load this explicitly for sessions that touch `src/`, `schema/`, or the `justfile`.

Dev access is gated: writes to `src/`, `schema/`, `justfile`, and `.claude/` are blocked by the pre-edit hook in curation sessions. If you need to work on code, schema, or tooling, request dev setup from the repo admin (@dosumis). Code and schema changes land through PR review against `main`.

### Taxonomy reference DB

After cloning, rebuild the SQLite index for any ingested taxonomy:

```
just build-taxonomy-db CCN20230722
```

The YAML source files (`kb/taxonomy/{id}/*.yaml`) are committed; the `.db` is not.
To validate the taxonomy YAML against the schema:

```
just validate-taxonomy-all CCN20230722
```

To also build the anatomical closure tables (for ancestor-aware location queries):

```
just fetch-mba-ontology          # one-time download to conf/mba/
just build-anat-closure CCN20230722
```

To download local MapMyCells taxonomy files for offline mapping:

```
just at-download-taxonomy CCN20230722   # downloads to conf/mapmycells/CCN20230722/
```

For KG-backed taxonomy re-ingest (requires a local neo4j instance at `bolt://localhost:7687`):

```
just fetch-taxonomy-kg inputs/taxonomies/CCN20230722.cypher CCN20230722
just ingest-taxonomy-db inputs/taxonomies/CCN20230722.json CCN20230722
```

Credentials are read from `NEO4J_BOLT_URL`, `NEO4J_USER`, `NEO4J_PASSWORD` environment variables (or CLI flags). Add them to `.claude/settings.local.json` alongside the ASTA key if needed.

---

### MCP / API keys

The literature workflow uses two MCP servers that require credentials:

**ASTA (Semantic Scholar)**

The project `.mcp.json` reads the key from the environment variable `${ASTA_API_KEY}`. Claude Code expands this at startup, so the key must be available before Claude Code launches.

The recommended approach is to add it to `.claude/settings.local.json` (gitignored) via the `env` field, which Claude Code injects before expanding variables in `.mcp.json`:

```json
{
  "env": {
    "ASTA_API_KEY": "<your-asta-api-key>"
  }
}
```

Request an ASTA API key from the Allen Institute. The `settings.local.json` file is gitignored and must be created locally by each contributor — it is never committed.

> **Note (sandbox users):** If you are running inside a Claude Code sandbox (`sbx`), setting `ASTA_API_KEY` as a sandbox secret (`sbx secret set`) is the intended mechanism, but secret-to-environment injection is not yet supported (tracked in [docker/sbx-releases#7](https://github.com/docker/sbx-releases/issues/7)). Use `settings.local.json` as above until that is resolved.

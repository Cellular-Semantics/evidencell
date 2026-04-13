# evidencell Roadmap

**Date**: 2026-04-13 (last updated)
**Status**: M0–M4 implemented. Active work: schema refinement, lit workflow robustness, workflow contracts.


## Summary

### Completed

| Milestone | Goal | Key deliverables |
|---|---|---|
| **M0** Schema Hardening | Fix schema issues; validator hook prototype | Schema v0.5.4, pre-edit hook, 1 validated example |
| **M1** Repo Bootstrap | Create evidencell repo structure | Repo, justfile, CLAUDE.md, ≥3 ported examples |
| **M2** Lit Review → KB | Deepsearch pipeline → evidence items + reference provenance | ASTA ingest + cite-traverse + evidence-extraction workflows, references.json cache |
| **M3** Mapping Hypotheses | Propose mapping edges from evidence + taxonomy | `map-cell-type.md` orchestrator, hippocampus + cerebellum draft mappings |
| **M4** Report Generation | Human-readable reports from draft mappings | Three-tier reports; `render.py` (91% coverage); `gen-report` recipes; `AtlasQueryEvidence` schema class |
| **AT** Annotation Transfer | AT pipeline + first end-to-end run | OLM hippocampus GSE124847 → WMBv1; schema v0.6.0 (AnatomicalLocation + CellCompartment); orchestrator for KB import pending |

### Active / Pending

| Milestone | Goal | Status | Key deliverables | Depends on |
|---|---|---|---|---|
<<<<<<< HEAD
| **S** Schema Refinement | Taxonomy level encoding, marker/assay consistency, semantic checks | 🔲 Pending | S1 rank encoding, S3 marker type split, SC1-SC3 semantic lint rules | — |
| **M2L** Lit Search File Specs | Formal schemas for cite-traverse intermediate files | 🔲 Pending | Pydantic models for summary/refs/manifest; output validation at step boundaries; canonical output_dir | — (parallel) |
| **WC** Workflow Contracts | Audit and formalise data contracts across all workflows | 🔲 Pending | Contract inventory; schema coverage map; inter-workflow handover specs; graduation criteria; user-facing terminology | S, M2L (inform) |
| **M2+** Lit Review Quality | Improve snippet context, paper quality signals, and domain relevance filtering in cite-traverse | 🔲 Pending | Contextual retrieval for priority papers; venue/citation/cross-citation quality signals; evidencell-specific relevance pre-filters | — (parallel, any time) |
| **CF** Community Feedback | Enable biologist review of mappings; KB quality scoring | 🔲 Pending | Report-based review workflow; compliance scoring; structured feedback mechanism | S, M4 |
| **M6** Code/Content Separation | Decouple KB content from code | 🔲 Pending | Content boundary; `content/hmba-mouse` branch; `main` passes `just test` with fixtures only | WC, S |
| **M7** KB Structure Cleanup | Move workflow ephemera out of `kb/`; one graph per region×atlas; naming convention; graduation criteria | 🔲 Pending — HIGH PRIORITY | `kb/` contains only graph YAML; `references/`, `research/`, `reports/` at repo root; graph naming + graduation criteria in CONTRIBUTING.md | — (can start now) |
| **M8** Taxonomy Reference DB | Full taxonomy ingest as local queryable DB; graph stubs pulled on demand from reference store | 🔲 Pending | Local taxonomy DB (SQLite or similar); query-based stub generation; `ingest-taxonomy` rewritten to populate DB; `map-cell-type` queries DB for candidates | M7 |


## Cross-Cutting Discussion Points

### 1. LinkML schema strictness

The current schema (v0.4) is moderately strict: required fields enforced, enumerations for key controlled values (`MappingRelationship`, `MappingConfidence`, `EvidenceSupport`), ontology term bindings for CL/UBERON/NCBITaxon via `meaning` fields. However, it has not been validated end-to-end with `linkml-validate` yet — the discriminated union pattern (multiple evidence subtypes in a single list) is an untested corner.

**Recommended stance for evidencell**: *strict on structure, lenient on optional fields.* Required fields enforced by schema; optional metadata fields (scope, caveats) are not blocking but flagged by compliance scoring. This mirrors dismech's approach and keeps the correction loop tractable.

### 2. `just` vs Python for workflow logic

dismech uses `just` as a thin task runner wrapping Python/uv scripts.

**For `just`**: Proven pattern in dismech; humans and agents both understand `just qc`; composable recipes are easy to read.

**For more Python**: Agents and humans can read, debug, and modify Python more readily than justfile + shell; error handling and structured output are cleaner; complex logic (auto-flagging, extraction pipelines) is much easier in Python; testable with pytest.

**Recommendation**: Use `just` as the *interface layer* — named recipes like `just qc`, `just research-celltype`, `just fetch-reference` — but implement non-trivial logic as Python scripts in `src/evidencell/` invoked by `just`. Pure shell in justfile only for truly simple operations. This gives the human-readable command surface of `just` while keeping complex logic debuggable.

### 3. Workflow output file structure and `kb/draft/` → `kb/mappings/` graduation

**Problem**: Workflow orchestrators produce many intermediate and final artifacts (snippets, summaries, candidate refs, reports, manifests) but there is no enforced convention for where they land. The `output_dir` parameter is set by the calling orchestrator — but when a workflow is run directly (no caller), the operator guesses. This led to cite-traverse outputs landing in `scratch/` (gitignored) when they are standard workflow artifacts that need to persist for the next pipeline step and for provenance.

**Current state**:
- `kb/mappings/{region}/` — validated, graduated KB files (source of truth)
- `kb/draft/{region}/` — work-in-progress YAML, references, and now workflow run directories
- `scratch/` — gitignored; intended for truly temporary intermediates
- No enforcement: orchestrators don't validate `output_dir` placement; nothing prevents workflow artifacts from landing in `scratch/` or an ad hoc location

**Needed**:
1. **Canonical output layout** — define where each orchestrator writes its outputs relative to `kb/draft/{region}/`. Proposal: `kb/draft/{region}/{workflow_name}/` (e.g. `kb/draft/hippocampus/cite_traverse/`, `kb/draft/hippocampus/evidence_extraction/`).
2. **Graduation criteria** — define what "graduating" from `kb/draft/` to `kb/mappings/` actually requires. Currently `CLAUDE.md` says "after just qc" but the boundary is fuzzy: does the report graduate? Do intermediate JSONs stay in draft? Is it per-file or per-graph?
3. **Enforcement** — orchestrators should validate that `output_dir` is under `kb/draft/{region}/` (or explicitly `scratch/` for throw-away runs). The pre-edit hook already gates KB YAML writes; a similar check could gate workflow output placement.
4. **User-facing terminology** — "add stubs" / "proceed to extraction" / "graduate" are internal jargon. Need clearer labels for curator-facing gates (e.g. "expand scope" vs "lock down evidence" vs "promote to validated").

---

## M0 — Schema Hardening and Validation Prototype

**Goal**: Resolve known schema issues and build a validator hook that catches bad YAML before it lands on disk.

### Deliverables
- Schema v0.5 (after issue review and resolution)
- Pre-edit validator hook (fires on `Edit`/`Write` to `kb/mappings/**/*.yaml`)
- ≥1 KB example passing all validators end-to-end

### Schema issues — ⚠️ ROUGH DRAFT
These items come from `examples/scratch_notes.md` and session discussion. **They need review against the current schema (v0.4) before acting on** — some may already be addressed or have changed in intent.

1. Split `SpatialColocationEvidence` into two types: `AbsoluteLocationEvidence` (where is this cell type relative to anatomy) and `ColocationEvidence` (where is it relative to other cell types)
2. Switch gene IDs from HGNC → NCBIGene for multi-species support; use NCBI Translator NodeNormalization endpoint for ID resolution
3. Slim down `AnnotationTransferEvidence` — current schema is overfitted to one example. Minimal required fields: method, target_dataset, F1. Extend later.
4. `TaxonomyLevel` enum is overfitted and likely redundant with the taxonomy being referenced. Make optional or replace with free text.
5. Fix incorrect hierarchy note in examples: Class is above Group in BG taxonomy (not the reverse, as written in one example)
6. Add evidence scope metadata fields to `EvidenceItem`: `species`, `developmental_stage`, `biological_context`, `experimental_system`, `flagged`, `flag_reason` — needed for M3 auto-flagging and expert review

### Validator hook (dismech pattern adapted)
- Fires on `Edit`/`Write` targeting `kb/mappings/**/*.yaml`
- Simulates resulting file content (no disk write until validated)
- Runs `linkml-validate` against schema — blocks on structural errors
- Runs OAK term validation for CL, UBERON, NCBITaxon prefixes against local SQLite DBs
- Does **not** yet run reference validation (deferred to M2)
- Returns structured error output; Claude rewrites YAML in correction loop (typically resolves in 1–2 iterations, per dismech experience)

### Tensions
- **`TaxonomyLevel` strictness**: current annotation transfer examples use it for cross-taxonomy metric tables. Probably retain as optional free text rather than forcing an enum.
- **OAK local DB setup**: pre-building SQLite for CL, UBERON, NCBITaxon requires disk space and setup. Document steps carefully; these are large ontologies.
- **HGNC → NCBIGene migration**: existing KB examples use HGNC. Need a migration script or manual one-time update.

### Open questions
- Does `linkml-validate` handle the discriminated union evidence item pattern without custom configuration? Needs testing.
- Should the hook also validate CCN accession format (`CS` + date string + level + index)?

---

## M1 — Evidencell Repo Bootstrap

**Goal**: Create the `evidencell` repo with dismech-inspired structure, adapted for cell type mappings. Immediately usable for hand-curation of new KB entries.

### Deliverables
- `evidencell/` repo initialised with uv, justfile, schema, `CLAUDE.md`
- `kb/mappings/` with ≥3 validated examples ported from this planning repo (GPi shell primate, GPi shell mouse, CB MLI)
- Validator hook wired into `.claude/hooks/`
- `just qc` running all validators
- `just ingest-taxonomy {taxonomy_file}` recipe: parses a source taxonomy (CCN-formatted YAML, Allen Brain Atlas data release, or equivalent) and creates `CellTypeNode` stubs in the relevant KB YAML. This step is **independent of deepsearch** — it can be run as the first step of any new mapping project, before M2 or M3 begin.
- `CONTRIBUTING.md` walkthrough for human curators

### Repo structure
```
evidencell/
  schema/celltype_mapping.yaml       # LinkML schema (source of truth)
  kb/mappings/{region}/              # one YAML per mapping graph
  references_cache/                  # cached ASTA reference text for provenance
  conf/oak_config.yaml               # OAK adapter config (CL, UBERON, NCBITaxon)
  src/evidencell/                    # all Python logic (validate, render, score, fetch)
  justfile                           # thin task-runner; logic lives in src/evidencell/
  CLAUDE.md                          # development and architecture guidelines
  WORKFLOW.md                        # guide: which orchestrator runs when, with what inputs
  workflows/                         # multi-step orchestrators (subagent-spawning, file-state)
    lit-review.md                    # ported from Asta_deepsearch
    evidence-extraction.md           # M2: filter→extract→provenance→review gate
    map-cell-type.md                 # M3: property searches→hypothesis→confidence check
    annotation-transfer.md           # AT: import AT results→propose AnnotationTransferEvidence
  .claude/hooks/validate_mapping_hook.py
  .claude/skills/                    # bounded single-focus tasks, called interactively
    catalogue-weeding/               # present flagged catalogue; human pruning interaction
    celltype-mapping-pr-review/      # CF: review KB PR against rubric
  .claude/agents/                    # (reserved: shared subagent personas, if needed)
```

### Taxonomy ingestion
`just ingest-taxonomy` produces `CellTypeNode` stubs — ID, name, taxonomy source, CCN accession — with empty evidence lists. Classical types (basket cell, stellate cell) are defined by hand or pulled from literature; atlas types (WMBv1 clusters, HMBA supertypes) are parsed from the data release. Atlas metadata (marker gene tables, MERFISH expression, spatial data) is stored alongside the stubs for use by the M3 mapping hypothesis agent.

**CCN accession lookup table**: as part of ingestion, `just ingest-taxonomy` should write a lookup file (e.g. `kb/taxonomies/{atlas_id}/accession_lookup.json`) mapping every CCN accession in the source to its name and taxonomy level. The validator hook uses this file to check that any `cell_set_accession` or `source_cell_set_accession` value in a KB YAML is a real accession from the declared atlas — rather than relying on a static regex pattern. This is deferred to M1 (no validator hook in M0 can use it before taxonomy is ingested).

Taxonomy ingestion is a hard prerequisite for M2 (`research-celltype` takes a `{node_id}`) but runs independently of the deepsearch pipeline.

### Key difference from dismech: reference backend
- **dismech**: validates snippet ↔ PubMed abstract (PMID, markdown cache)
- **evidencell**: validates snippet ↔ ASTA corpus (CorpusId, JSON cache)
- `references_cache/{corpus_id}.json` stores title, abstract, snippet text, content type, fetch timestamp
- For deepsearch-sourced evidence the verbatim text is already in `all_summaries.json` — snippet provenance validation is integrated into M2 (the lit-review pipeline) rather than as a separate pre-requisite milestone

### Tensions
- **Fresh repo vs dismech fork**: fresh repo is cleaner given the different domain, but loses dismech's CI/hook infrastructure. Recommendation: fresh repo borrowing patterns and tooling choices (linkml-validate, OAK, just, uv), not code.
- **Minimum viable rendering**: a per-graph page showing graph diagram, node descriptions, edge confidence, evidence items. Jinja2 approach from dismech is reusable.
- **Python tooling reuse**: `linkml-validate` and OAK work unchanged. New Python needed for: ASTA reference fetching (`src/evidencell/fetch.py`), compliance scoring (`src/evidencell/compliance.py`), report rendering (`src/evidencell/render.py`).

### Open questions
- Should `CONTRIBUTING.md` direct community curators to install Claude Code (like dismech), or is a simpler "edit YAML + PR" workflow appropriate for v1?

---

## M2 — ASTA Deepsearch Integration: Literature Review → KB

**Goal**: Run `Asta_deepsearch/workflows/lit-review.md` on a cell type topic and extract schema-compliant `LiteratureEvidence` items from the output. First end-to-end pipeline from "research a topic" to proposed KB YAML. Includes reference provenance validation: snippets must be traceable to their source text in `all_summaries.json`.

### Deliverables
- `just research-celltype {node_id} "{topic}"` recipe wrapping the lit-review orchestrator
- Auto-flagging script: scans `paper_catalogue.json` for species/stage/context signals → `paper_catalogue_flagged.json`
- Deepsearch report: `report.md` from lit-review is the primary human artefact for catalogue weeding — shows what was found before committing to extraction
- Catalogue weeding gate: human reviews `paper_catalogue_flagged.json` (title, year, venue, auto-flags) and prunes irrelevant papers before extraction runs
- **(Optional)** Full-text validation sweep: for flagged papers that are *kept* after weeding, call `get_europepmc_full_text` (EuropePMC, ~35–40% coverage for neuroscience) to read the Methods section and confirm species/stage/preparation. Updates `evidence_scope` fields and adds `validation_source: "full_text"`. Targeted and bounded — only flagged papers, not the whole corpus.
- Extraction agent: `all_summaries.json` + `paper_catalogue.json` + mapping context → proposed `LiteratureEvidence` YAML blocks
- Evidence scope fields populated from auto-flagging (requires M0 schema additions)
- `just fetch-reference CorpusId:NNN` recipe: for manually added evidence, fetches and caches text from ASTA to `references_cache/{corpus_id}.json`
- Snippet provenance check: verifies each proposed `LiteratureEvidence.snippet` is a substring of the corresponding entry in `all_summaries.json` (deepsearch path) or `references_cache/` (manual path)

### Pipeline
```
just research-celltype {node_id} "{topic}"
    │
    ▼
lit-review orchestrator (Asta_deepsearch/workflows/lit-review.md)
    → seeds.json, all_summaries.json, paper_catalogue.json, report.md
    │
    ▼
auto-flagging script (src/evidencell/flag_papers.py)
    → paper_catalogue_flagged.json
    │
    ▼
[GATE: human reviews deepsearch report.md + flagged catalogue, prunes papers]
    │
    ▼
[OPTIONAL: full-text sweep (get_europepmc_full_text) on kept flagged papers]
    → updates evidence_scope on linked snippets
    │
    ▼
extraction agent (Claude + mapping context prompt)
    reads: all_summaries.json (filtered), paper_catalogue_flagged.json
    writes: proposed_evidence_{node_id}.yaml
    │
    ▼
[GATE: expert reviews proposed LiteratureEvidence items, approves/edits/rejects]
    │
    ▼
Append validated evidence items to kb/mappings/{region}/{graph}.yaml
```

### Extraction agent design

The most complex piece of M2. The agent receives:
- `all_summaries.json` — per-snippet summaries with verbatim quotes, section, score, depth
- `paper_catalogue.json` — full metadata (title, year, venue, PMID, DOI, corpus_id)
- **Mapping context**: which `CellTypeNode` is being evidenced (name, markers, anatomy, NT type)

It proposes one `LiteratureEvidence` per high-relevance snippet:
```yaml
- corpus_id: "12345678"
  pmid: "PMID:38000000"
  doi: "10.1234/example"
  snippet: "exact verbatim quote from all_summaries.json"
  support: SUPPORT  # SUPPORT | PARTIAL | REFUTE — LLM judgment
  evidence_scope:
    species: human
    developmental_stage: adult
    biological_context: normal
    experimental_system: in_vivo
  auto_flagged: false
```

The `support` judgment requires the agent to assess whether the snippet supports the *specific mapping claim* — this is the key LLM task and requires explicit mapping context in the prompt.

### Auto-flagging signals
Lightweight pattern matching on `paper_catalogue.json` title/abstract/venue:
- **Species**: mouse/rat/NHP/primate-specific journal names
- **Developmental stage**: "embryonic", "postnatal day N", "P0–P21", developmental biology journals
- **Disease context**: disease name keywords, clinical cohort indicators, patient samples
- **Experimental system**: "organoid", "iPSC", "cell culture", "acute slice", "dissociated"

### Tensions
- **Token budget for extraction**: 100+ snippets in `all_summaries.json` is expensive to pass to one agent. Mitigation: pre-filter by relevance score (snippets carry scores from traversal); run a cheap filtering pass first, then extraction on top-K only.
- **Support judgment reliability**: LLM support judgments will be imperfect, especially for nuanced partial overlaps. Mandatory expert review gate before KB commit is non-negotiable.
- **Extract from summaries, not report**: `report.md` is synthesised prose — quotes from it are not verbatim from papers. Extract only from `all_summaries.json` which preserves original snippet text and CorpusIds.

### Open questions
- **1:1 or many:1 snippets per EvidenceItem?** Recommend 1:1 for traceability. Multiple snippets supporting the same claim can be listed as separate EvidenceItems on the same edge.
- **Where does the traversal output live in evidencell?** Proposed: `kb/mappings/{region}/traversal_output/{date}_{slug}/` — co-located with the KB entry for provenance.
- **Third-party deepsearch input (deferred)**: if the input is pre-run deepsearch text from an external provider (Perplexity, Falcon, etc.) rather than the ASTA pipeline, provenance validation is harder — we do not have `all_summaries.json` as a ground truth. The proposed approach: run `snippet_search` on the referenced papers to find supporting verbatim text; flag cases where no matching text is found. Deferred to a post-M2 extension — building this before the ASTA path exists end-to-end is premature.

---

## M3 — Mapping Hypothesis Generation

**Goal**: From the literature evidence base (M2) and taxonomy-derived atlas metadata (M1), an agent proposes mapping edges and confidence assessments. Targeted property-combination snippet searches optionally supplement the M2 corpus where gaps exist.

### Prerequisites
- **Taxonomy nodes defined** (via `just ingest-taxonomy` from M1 or hand-curation): `CellTypeNode` stubs for both classical and atlas types, with atlas metadata (markers, anatomy, NT type, spatial data) stored alongside
- **Curator's mapping context**: an explicit initial hypothesis — which classical types are believed to map to which atlas types, and at what relationship type. This is the curator's primary intellectual contribution entering M3 and scopes everything the hypothesis agent does.

### Deliverables
- `workflows/map-cell-type.md` orchestrator (not a skill — multi-step with explicit control flow and subagent prompts)
- Mapping hypothesis agent: M2 literature evidence + atlas metadata + curator hypothesis → proposed `MappingEdge` YAML with relationship, confidence, caveats, evidence list
- **(Optional)** Property-combination snippet search workflow: targeted ASTA searches for specific property combinations, scoped to `paper_catalogue.json` from M2 to avoid redundancy with the deepsearch corpus
- Human gate: expert reviews proposed edges (relationship type, confidence, caveats)

### Property-combination searches (optional)
Run only when M2 literature review has gaps for specific properties relevant to the mapping. Scoped to the paper catalogue already built in M2 — these are targeted queries *within the existing corpus*, not new traversal:

| Query pattern | Targets |
|---|---|
| `"{cell_type} {marker} expression"` | Positive/negative markers |
| `"{cell_type} {anatomy} location"` | Spatial localisation |
| `"{cell_type} GABA glutamate neurotransmitter"` | NT type |
| `"{cell_type} single-cell transcriptomic cluster"` | Atlas correspondence |

Scoping to `paper_catalogue.json` means no new papers are fetched — snippets are drawn from within the already-reviewed corpus. If a property is well-covered by M2, this step is skipped. Results go to `traversal_output/{slug}/phase2_snippets/`.

### Mapping hypothesis agent
Given: Phase 1 + Phase 2 evidence + atlas metadata (marker tables, MERFISH annotations), the agent proposes:
- `MappingRelationship` per candidate edge (EQUIVALENT / PARTIAL_OVERLAP / CROSS_CUTTING / etc.)
- `MappingConfidence` per the decision guide (plan.md §4.4)
- Draft `caveats[]`
- Evidence item list with corpus IDs

The existing KB examples (GPi shell, CB MLI) serve as in-context patterns for the agent.

### Tensions
- **Cross-cutting types**: recognising that a transcriptomic type partially overlaps multiple classical types (MLI1/MLI2 example) is a non-trivial inference. The CB MLI example must be included in the mapping skill prompt as a worked demonstration.
- **Atlas metadata sourcing**: WMBv1 marker tables and MERFISH annotations are structured data — they must be manually pulled from the atlas for now. A future tool to ingest Allen Atlas cell type metadata directly would remove this bottleneck.
- **Confidence over-claim**: HIGH confidence requires ≥2 independent evidence types including ≥1 experimental. The agent must be explicitly instructed to check this against the decision guide and not infer HIGH from literature alone.

### Open questions
- **No literature found**: if deepsearch yields no relevant snippets (very recently described type), the agent should explicitly propose `UNCERTAIN` confidence and document the evidence gap rather than guessing.
- **Agent architecture**: single Sonnet call for small graphs (≤5 edges); spawn sub-agents per candidate edge for complex multi-type regions. The `map-cell-type` orchestrator should specify this branching logic explicitly.

---

## M4 — Report Generation (MVP for biologists)

**Implementation plan**: [M4_report_generation.md](M4_report_generation.md)
**Status**: ✅ Done (2026-04-04). Three-tier reports implemented; `gen-report-draft` recipe added; test coverage at 91%.

**Goal**: Auto-generate human-readable mapping reports from KB YAML. This is the MVP milestone — after M3, biologists can review draft mappings and proposed experiments without reading YAML.

### What's done

**Architecture** — three-tier report hierarchy (see [M4_report_generation.md](M4_report_generation.md)):
- **Tier 0 — Region index**: one row per classical type; best hit, confidence, candidate count, link to summary
- **Tier 1 — Per-classical-type summary**: candidates table, evidence paragraphs, consolidated experiments, numbered references (`[1]`–`[N]` for literature, `[A]`–`[Z]` for atlas queries)
- **Tier 2 — Per-paper drill-down**: verbatim quotes per property, alignment to specific atlas cluster, summary scorecard, critical gap + bridging experiment

**Hand-crafted mock-ups** (OLM hippocampus case study, `kb/draft/hippocampus/reports/`):
- `OLM_mapping_report.md` — Tier 1 summary, demonstrates format including soma-only location note, adjacent vs distant counter-evidence, UNCERTAIN edge collapsing, numbered references
- `OLM_drilldown_Winterer2019.md` — Tier 2 drill-down, 17 verified quotes from `references.json`, per-property scorecard, critical gap (GEO:GSE124847 re-mapping)

**Schema** — `AtlasQueryEvidence` class + `ATLAS_QUERY` evidence type added (v0.5.4): atlas browser interactive queries (ABC Atlas, Allen Brain Map) as typed, citable evidence with `query_url`, `filters_applied`, `atlas_version`

**Location reasoning** — soma-only interpretation rule codified in `workflows/map-cell-type.md`: MERFISH location = soma position only; adjacent region = possible registration error (weak counter-evidence); distant region = genuine counter-evidence (subtype caveat preserved)

### What was delivered (M4 complete)

1. **`src/evidencell/render.py`** — `build_reference_index`, `render_summary`, `render_drilldown`, `render_index`, and all helpers; 91% test coverage
2. **Justfile recipes** — `gen-report`, `gen-report-node`, `gen-drilldowns`, `gen-index`, `gen-report-all`
3. **End-to-end test** — run on OLM hippocampus case; verify output matches hand-crafted mock-ups; confirm no invented references or quotes

### Deferred (not M4)
- HTML rendering (Jinja2 → HTML) — deferred pending community need
- Report versioning via git log
- `workflows/gen-report.md` LLM synthesis orchestrator — programmatic render.py may be sufficient; defer if quality adequate
- Automated experiment structuring (schema extension to `proposed_experiments[]`) — deferred

---

## S — Schema Refinement

**Goal**: Address known schema gaps and add semantic lint rules that catch common errors before they reach the KB.

**Status**: 🔲 Pending (priority 1)

S2 (AnatomicalLocation + CellCompartment) shipped in v0.6.0. Remaining items:

### Schema changes

**S1. Taxonomy level encoding — rank, not name.**
Taxonomy level names (CLASS, SUBCLASS, SUPERTYPE, CLUSTER) are arbitrary and
taxonomy-specific. Replace hardcoded level name enums with:
- `level_name: str` — free string, taxonomy-defined (e.g. "SUPERTYPE", "subclass")
- `rank: int` — 0 = most specific (leaf), incrementing for each level above

This affects `AnnotationTransferLevelResult.taxonomy_level`, `best_mapping_level`,
and any code that assumes WMB-specific level names. Mapping edges should be
expressible at any rank, not just cluster (rank 0).

**S3. Marker type / assay consistency.**
`marker_type` (PROTEIN/TRANSCRIPT) can conflict with `method` (e.g.
`marker_type: PROTEIN` with `method: "in situ hybridization"`). Options:
- Split into `detected_molecule` + `assay_method` with a consistency rule
- Or keep `marker_type` but add a semantic check (SC1 below)

### Semantic checks (lint rules for the pre-edit hook)

**SC1. Marker type vs method consistency.**
If `method` contains "RNA-seq", "in situ hybridization", "qPCR" → `marker_type`
should be TRANSCRIPT. If "immunohistochemistry", "Western blot" → PROTEIN.
Hook should flag inconsistencies but **not auto-fix** — confabulation could be
on either side.

**SC2. Node notes containing mapping information.**
Notes on classical nodes should describe the type, not its mapping to atlas
clusters. Lint rule flags notes that reference cluster IDs, supertype names, or
WMB-specific terms — these belong on edges, not nodes.

**SC3. Information in YAML comments vs structured fields.**
Data in `# comments` is invisible to validation and rendering. Negative marker
sources and heterogeneity notes should be in `sources` or `notes` fields.
Convention rule for CLAUDE.md: "never put data in YAML comments that could go
in a structured field."

### Open questions
- Should `CROSS_SPECIES_EXTRAPOLATION` be a structured field on `MappingEdge` (more queryable) or remain a free-text caveat?

---

## CF — Community Feedback on Mappings

**Goal**: Enable biologists to review, comment on, and improve mapping evidence — via reports, structured feedback, and KB quality scoring.

**Status**: 🔲 Pending (priority 5 — needs stable schema and reports first)

**Motivation**: The expert bottleneck is real — cell type mapping requires specialist knowledge (neuroscience, transcriptomics, atlas familiarity). The goal is not to eliminate the bottleneck but to make expert time efficient: surface the right questions, make evidence auditable, and capture feedback in structured form.

### Compliance scoring

Per-mapping-graph quality metrics in `src/evidencell/compliance.py`:

| Dimension | Metric |
|---|---|
| Schema completeness | Required fields present on all nodes and edges |
| Evidence coverage | ≥1 EvidenceItem per edge |
| Evidence diversity | ≥2 independent types for HIGH-confidence edges |
| CL term presence | Every node has at least a BROAD CL mapping |
| Reference validation | All LiteratureEvidence snippets validated against references.json |
| Scope metadata | `species` + `developmental_stage` populated on ≥80% of evidence items |

### Review workflow

How biologists interact with mappings — not yet designed in detail:
- Reports (from M4 gen-report) are the primary review surface
- Feedback needs a structured path back into the KB (not just PR comments)
- GitHub PR review (`celltype-mapping-pr-review` skill) is one option for curators comfortable with GitHub; may not suit all biologists
- CL term currency: CL is actively evolving; record CL version at entry creation; periodic term validation

### Runtime environments and user setup

Making evidencell accessible to curators (biologists who are not full-stack developers) requires reducing setup friction. Current findings (2026-04-09):

**Docker sandbox** (`docker sbx`): works well for running workflows with "allow everything" minus limited web search. Main blocker: environment variable setup (API keys for Semantic Scholar, EuropePMC, Anthropic) is painful — not yet fully working. Docker sbx is suitable for tech-savvy users (e.g. Nelson, Andrea) once env var injection is solved.

**Claude Code sandbox**: similar env var issues. Workaround of adding keys to `.zshrc` works but isn't ideal. Still too much permission-prompt noise even with permissive settings.

**GitHub Actions**: investigate for longer-term hosted execution — would eliminate local setup entirely. Potential pattern: curator opens a PR or issue; a GitHub Action runs the relevant orchestrator; results are committed back to the PR branch.

**Deliverables**:
1. `docs/SETUP.md` — step-by-step instructions for Docker sbx setup including env var injection
2. Docker Compose file or `justfile` recipe (`just docker-setup`) automating the container build with required MCP servers and Python deps
3. `.env.example` documenting required env vars without secrets
4. Investigate GitHub Actions for orchestrator execution (feasibility spike)

### Scale concern
A full cerebellar atlas has ~60 cell types; full brain could exceed 3,000. At that scale the mapping hypothesis agent (M3) must be largely automated. Community curation alone will not be sufficient. evidencell should complement and link to Allen Brain Atlas annotations, CL, and BICAN cell type taxonomy.

### Open questions
- Should `CROSS_SPECIES_EXTRAPOLATION` be a structured field on `MappingEdge` (more queryable) or remain a free-text caveat? A structured flag would allow systematic filtering.
- Should the evidencell KB be public from launch? Recommend yes — openness is a feature; early community feedback is valuable.

### GitHub workflow
Pattern from dismech:
- Curator opens PR with new/updated `kb/mappings/{region}/*.yaml`
- `claude-code-review.yml` runs the `celltype-mapping-pr-review` skill → inline comments on missing evidence, schema issues, imprecise CL terms
- Human expert does final approval
- `weekly-compliance.yaml` cron: finds lowest-compliance KB files, runs Claude to propose improvements, opens PR

### Runtime environments and user setup

Making evidencell accessible to curators (biologists who are not full-stack developers) requires reducing setup friction. Current findings (2026-04-09):

**Docker sandbox** (`docker sbx`): works well for running workflows with "allow everything" minus limited web search. Main blocker: environment variable setup (API keys for Semantic Scholar, EuropePMC, Anthropic) is painful — not yet fully working. Docker sbx is suitable for tech-savvy users (e.g. Nelson, Andrea) once env var injection is solved.

**Claude Code sandbox**: similar env var issues. Workaround of adding keys to `.zshrc` works but isn't ideal. Still too much permission-prompt noise even with permissive settings.

**GitHub Actions**: investigate for longer-term hosted execution — would eliminate local setup entirely. Potential pattern: curator opens a PR or issue; a GitHub Action runs the relevant orchestrator; results are committed back to the PR branch.

**Deliverables** (M5 scope):
1. `docs/SETUP.md` — step-by-step instructions for Docker sbx setup including env var injection
2. Docker Compose file or `justfile` recipe (`just docker-setup`) automating the container build with required MCP servers and Python deps
3. `.env.example` documenting required env vars without secrets
4. Investigate GitHub Actions for orchestrator execution (feasibility spike)

### Open questions (additional)
- **Scale**: a full cerebellar atlas has ~60 cell types; full brain could exceed 3,000. At that scale the mapping hypothesis agent (M3) must be largely automated. Community curation alone will not be sufficient.
- **Relationship to existing resources**: evidencell should complement and link to Allen Brain Atlas annotations, CL, and BICAN cell type taxonomy — the evidence graph and explicit confidence levels are the contribution, not duplicating the atlases.

---

## Lessons from candelabrum cell pilot (2026-03-20)

Extracted to [planning/candelabrum_pilot_lessons.md](planning/candelabrum_pilot_lessons.md).
Key items still relevant: full-text retrieval fallback robustness (→ M2L), semantic
validation loop for evidence placement (→ WC), MERFISH co-location scoring (future).
Items addressed: snippet quality filtering, KB-first output, citation traversal pipeline.

---

## M6 — Infrastructure: Code/Content Separation

**Goal**: Decouple the HMBA mouse KB from code and infrastructure so evidencell can serve as a clean starting point for new KB projects (different species, brain region, or atlas).

**Status**: 🔲 Pending (depends on S + WC — schema and contracts must be stable before separating content)

### Motivation

Development through S/WC is necessarily coupled: workflows, schema, and KB content co-evolve. Once schema and contracts are stable, a second KB project could adopt evidencell without inheriting HMBA mouse content.

### Content boundary

**Stays on `main` permanently (code + infra + minimal test fixtures):**
- `src/evidencell/`, `schema/`, `tests/`, `justfile`, `.claude/`, `workflows/`, `planning/`, `docs/`
- `inputs/taxonomies/test_single_row.json` — toy taxonomy fixture
- `kb/draft/BG/GPi_shell_neuron.yaml` + `GPi_shell_neuron_Mmus.yaml` — minimal complete KB examples; used as hook test fixtures in `test_hook_integration.py`

**Moves to `content/hmba-mouse` branch:**
- `kb/draft/hippocampus/` — all YAML, references.json, reports, traversal outputs
- `kb/draft/cerebellum/CB_MLI_types.yaml`, `CB_PLI_types.yaml`
- `inputs/taxonomies/hippocampus_GABA_stratum_oriens.json` (880 KB production taxonomy)

### Branch model (Phase 1)

Branch naming: `content/<project>` — e.g. `content/hmba-mouse`.

The content branch **merges from `main`** to pick up schema and tooling updates. KB-specific curation commits stay on the content branch. This is reversible; the repo can be restructured later without losing history.

`main` is verified clean: `just test` passes with BG fixtures only; `kb/mappings/` remains empty or minimal.

### Phase 2 (post-M6, not yet scoped)

Once evidencell's schema is stable and a second KB project starts:
- Make evidencell pip-installable (`uv build`, schema as packaged data asset)
- New KB projects become separate repos that `pip install evidencell` and supply their own `kb/`
- evidencell becomes a reusable tool rather than a content monorepo

### Deliverables
1. Content boundary documented (this section)
2. `content/hmba-mouse` branch created from current `main`; hippocampus + cerebellum content committed there
3. `main` cleaned to fixture-only KB content; `just test` verified green
4. `CONTRIBUTING.md` updated: content branch workflow (how to run orchestrators against content branch, how to merge `main` → content branch)

---

## M2+ — Lit Review Quality: Contextual Retrieval and Paper Relevance Signals

**Goal**: Improve the quality of evidence surfaced by `cite-traverse` by giving the LLM better context per snippet, filtering low-value papers early, and weighting traversal toward high-quality primary sources.

**Status**: 🔲 Pending (parallel — can run at any time, independent of M3–M6)

**Motivation**: Current cite-traverse works at the snippet level. Snippets are pre-computed by Semantic Scholar with fixed boundaries — a key claim may be split across snippet boundaries, or a negation may live in an adjacent sentence. The selection subagent has no paper quality signal beyond relevance, so a 2018 preprint and a 2024 Nature paper are treated identically.

### Option space

**Contextual retrieval for priority papers**

For papers flagged as Round 2 targets (ambiguous or contradicted claims), or for high-scoring snippets, retrieve the full text and re-extract passages in context rather than relying on pre-computed snippet boundaries. See [Anthropic contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval) for the principle: embedding a snippet with its surrounding context dramatically improves relevance. Concretely:
- For any Round 2 target paper with a PMC ID: fetch full text via `get_europepmc_full_text`, locate the relevant section, extract a window of ±2 paragraphs around each ASTA snippet. This costs one PMC fetch per paper but gives the LLM the logical unit rather than a pre-cut fragment.
- For high-relevance ASTA snippets (score > threshold, node_relevance=HIGH): optionally expand in the same way.

**Paper quality signals for selection**

Augment the selection subagent with paper-level quality signals beyond title/abstract relevance:
- **Venue**: peer-reviewed journal > preprint. Map venue strings to a tier (Nature/Science/Cell family, domain journals like J Neurosci/eLife, conference, preprint server).
- **Citation count**: Semantic Scholar already returns this. High citation count within the corpus is a quality proxy. Normalise by year (citations/year since publication).
- **Cross-citations within traversal corpus**: if paper A is cited by multiple papers already in the traversal corpus, it's likely a key reference. Count in-corpus citations as a strong positive signal.
- **Recency**: prefer recent papers for evolving marker characterisation; prefer older papers for foundational anatomy/morphology.

**Evidencell-specific domain relevance pre-filters**

Pre-filter seeds and candidate refs to down-rank papers unlikely to contain directly useful primary evidence for cell type identity mappings:
- **Low-rank**: disease model papers (e.g. epilepsy, Alzheimer's, Parkinson's) unless the query explicitly includes a disease context; pure in-vitro systems (dissociated culture, organoids) without in-vivo validation; synthetic biology / optogenetics methods papers where the cell type is a tool, not the subject.
- **Signal sources**: title + abstract keywords; MeSH terms if available from EuropePMC metadata; venue (methods journals).
- These are soft filters — deprioritise in selection, don't exclude entirely. Flag in selection rationale.

### Deliverables

1. `cite-traverse.md` Step 3: contextual expansion for Round 2 target papers (fetch full PMC text, locate section, extract ±2 paragraph window around ASTA snippet)
2. `cite-traverse.md` Step 4 (selection subagent): add quality scoring — venue tier, citation count, in-corpus cross-citation count, recency — and include scores in `selection_rationale`
3. `cite-traverse.md` Step 4: add domain relevance pre-filter with soft down-ranking for disease/in-vitro/methods papers; flag in rationale
4. `src/evidencell/venue_tier.py`: lookup table mapping venue strings → tier (reusable across selection steps)
5. Tests: unit tests for venue_tier lookup; integration test for selection scoring with synthetic paper catalogue

### Design questions to resolve

- Threshold for contextual expansion: all Round 2 targets, or only those with score > X? Cost vs coverage trade-off.
- In-corpus cross-citation counting: requires building a citation graph from `candidate_refs.json` across depths — worth the overhead?
- Whether to surface quality scores in `report.md` or only use them internally for selection.

---

## M2L — Lit Search File Specs and Validated Handovers

**Goal**: Formalise the data structures flowing through cite-traverse (and its callers/consumers) so that each step boundary is validated, not just instructed.

**Status**: 🔲 Pending (parallel — closely related to M2+ but independent)

**Motivation**: Of the 9 file types produced by cite-traverse, only 1 (`candidate_refs.json`) has a formal schema — defined as a docstring in `extract_asta_refs.py`. The rest are defined by prose in the orchestrator prompt. This means:
- A subagent that produces slightly wrong JSON (missing field, wrong enum value) is not caught until synthesis or extraction fails downstream.
- The summary object — the primary data contract between fetch → selection → synthesis → evidence-extraction — has no validation at all.
- `run_config.json` and `run_manifest.json` drift silently when orchestrator prompts are updated but the "schema" (prose) isn't updated consistently.

### Deliverables

1. **Pydantic models** in `src/evidencell/models/cite_traverse.py`:
   - `SnippetSummary` — source_corpus_id, source_title, source_method (enum: asta_snippet | europepmc_fulltext | asta_report), snippet_kind, section, snippet_score, node_relevance (enum: HIGH | MODERATE | LOW), node_relevance_reason, summary, quotes (list[str]), depth
   - `SelectionEntry` — corpus_id, title, selected, reason
   - `DepthRefs` — depth, all_candidate_ids, selected_corpus_ids, selection_rationale (list[SelectionEntry]), total_candidates, total_selected
   - `RunConfig` — all current params with types and defaults
   - `ManifestEntry` — step (enum), counts, timestamps
2. **Output validation** at each step boundary: fetch subagent writes summaries → validate against `SnippetSummary` before selection reads them. Selection writes refs → validate against `DepthRefs` before next fetch reads them. Validation can be a thin Python script (`uv run python -m evidencell.validate_cite_traverse {file} {schema}`) called by the orchestrator between steps.
3. **Canonical `output_dir` convention**: orchestrators enforce `kb/draft/{region}/cite_traverse/` (or `scratch/` if explicitly throw-away). Document in `WORKFLOW.md`.
4. **Schema-first orchestrator prompts**: the prose structure specs in `cite-traverse.md` reference the Pydantic models rather than inline JSON examples. Single source of truth.

### Relationship to M2+

M2+ improves what evidence cite-traverse finds (better snippets, smarter selection). M2L improves how reliably that evidence flows through the pipeline. They can run in parallel — M2L doesn't change retrieval logic, just wraps existing outputs in validation. If done together, new M2+ fields (venue_tier, quality_score) get added to the Pydantic models from the start.

---

## WC — Workflow Contracts: Cross-Workflow Handovers and Schemas

**Goal**: Audit and formalise the data contracts at every handover point across all evidencell workflows — not just within cite-traverse, but between workflows.

**Status**: 🔲 Pending

**Motivation**: Each workflow orchestrator was designed independently. The handover points between them are documented only by convention:
- `asta-report-ingest` → `cite-traverse`: passes `initial_summaries_file` and `report_context_file` — but there's no schema for the initial summaries format, and the report context is free-form Markdown.
- `cite-traverse` → `evidence-extraction`: the extraction workflow reads `all_summaries.json` — but its expected structure is defined only in the extraction orchestrator's prose, not validated.
- `evidence-extraction` → KB YAML: proposed evidence items must conform to the LinkML schema — this *is* validated (by the pre-edit hook), but the intermediate "proposed items" format before writing is not.
- `map-cell-type` reads KB YAML + atlas metadata — the KB side is schema-validated, but the atlas metadata input format is ad hoc.
- `gen-report` reads KB YAML — validated, but its own output (Markdown reports) has only a prose template spec.

This creates fragility: a change to one orchestrator's output format silently breaks the downstream consumer. The pre-edit hook catches KB YAML errors, but everything upstream of the KB write is unvalidated.

### Deliverables

1. **Contract inventory**: a table in `WORKFLOW.md` documenting every inter-workflow handover — what file is passed, what workflow produces it, what workflow consumes it, and whether it has a formal schema.
2. **Schema coverage map**: for each handover, classify as: (a) LinkML-validated, (b) Pydantic-validated (from M2L), (c) prose-only, (d) unspecified. Target: zero (d), minimal (c).
3. **Inter-workflow handover specs**: Pydantic or LinkML models for the key handover objects that aren't already covered — especially `initial_summaries` format, proposed evidence items, and atlas metadata input.
4. **Graduation criteria**: formalise what it means to move content from `kb/draft/` to `kb/mappings/`. Currently "after just qc" — define precisely which checks must pass, whether intermediate workflow artifacts (cite_traverse/, evidence_extraction/) are retained or archived, and what the human review gate looks like.
5. **User-facing terminology**: replace internal jargon at workflow gates. "Add stubs and continue research" → "Expand scope: add newly discovered types". "Proceed to extraction" → "Lock down: extract evidence for current types". "Graduate" → "Promote to validated KB".

### Relationship to other milestones

- **M2L** feeds into WC: cite-traverse contracts are the first and most complex case. M2L solves it for lit search; WC generalises.
- **M6** (code/content separation) depends on WC: you can't cleanly separate content from code if the handover formats aren't stable.
- **Cross-cutting point #3** (file structure) in this roadmap is the seed discussion; WC is the actionable plan.

---

## AT/Report improvements (from OLM pilot, 2026-04-09)

Observations from the first end-to-end annotation transfer run (OLM hippocampus,
GSE124847 → WMBv1). Schema items (S1–S3, SC1–SC3) moved to milestone **S** above.

**R1. Mapping above rank 0.**
Current report structure assumes mapping at the most specific level (rank 0).
When annotation transfer shows strongest signal at a higher rank, the report
should:
- Include an assessment at that rank, evaluating all rank-0 nodes within it
  collectively (soma locations, negative markers, neuropeptides)
- Frame the edge as "maps to rank N node X; rank 0 resolution pending"
  rather than picking a specific rank-0 node as the target
- Apply consistently regardless of taxonomy-specific level names

**R2. Subtype node creation.**
The schema already supports sub-nodes of classical types (e.g. Sst-OLM and
Htr3a-OLM as children of `olm_hippocampus`). This is a workflow improvement:
the agent should judge when to create sub-nodes based on source evidence
(e.g. when a dataset clearly separates subtypes with distinct expression
profiles or mapping targets). Per-subtype annotation transfer data (already
available from the OLM run) would attach to the sub-node edges.

**R3. F1 heatmap visualisation.**
Add a source-label × target matrix heatmap at each taxonomy level to the
annotation transfer output or report. The MLI-PLI notebooks in
`cellular_semantics_notebooks/` have this pattern. Could be a step in the
annotation-transfer workflow or a rendering option in gen-report.

**R4. Annotation transfer → classical property bridge.**
When source data comes from genetically or morphologically defined cells
(e.g. Chrna2-Cre labelled, patch-clamped OLM), the annotation transfer
inherits classical characterisation — it's not just a transcriptomic
similarity. Reports should make this explicit: "cells were selected by
[method], which confirms [markers/morphology/ephys], so the transfer
carries classical-type provenance."

**R5. Target-side expression from WMB h5ad files.**
Allen Brain Cell Atlas provides h5ad expression matrices by taxonomy class
and dissection region. These could resolve NOT_ASSESSED property comparisons
(e.g. Grm1 in Sst Gaba_3 clusters) without new experiments. Documented in
`workflows/annotation-transfer.md` Step 5c. High-value, low-cost improvement.

---

## M7 — KB Structure Cleanup

**Goal**: Make `kb/` contain only graph YAML. Establish naming conventions and graduation criteria. High priority — current structure is confusing and blocks clean onboarding.

**Status**: 🔲 Pending — can start immediately, independent of other milestones.

### Background: structural differences from dismech

dismech has one disease per file, with graph connections only to existing ontology terms (MONDO, HP, GO, CL). evidencell faces three challenges that dismech does not:

1. **Novel nodes**: atlas cluster stubs and literature-defined types are novel entities that exist nowhere else. The graph is a synthesis, not a connector between known entities.
2. **Partial taxonomy ingestion**: we ingest fragments of large taxonomies (e.g. 61 stubs from a taxonomy of thousands). Atlas stubs are shared infrastructure within a region, not per-mapping-problem.
3. **Gradual accretion**: a single region's graph grows over time as new classical types are researched and mapped. OLM today, bistratified cells next month, both mapping against the same atlas stubs.

### Design decisions

**One graph per region × atlas.** File = `{region}_{atlas}.yaml` (e.g. `hippocampus_WMBv1.yaml`). Multiple classical types coexist in one graph, sharing atlas stubs. This avoids stub duplication and matches the biology — a region's cell type landscape is interconnected. If a region exceeds ~500 nodes, split by subregion.

**Cross-cutting themes** (e.g. immature neuron populations spanning regions) get their own graph file: `immature_neurons_WMBv1.yaml`. These reference atlas nodes that also appear in region graphs — the node IDs are the canonical link. Cross-region graphs are expected to be rare; when they arise, document the overlap in the graph header.

**Gradual contribution.** ASTA report ingest adds a new classical node + edges to the existing region graph (read-merge-write). The human reviews the diff. This replaces the current pattern of creating standalone `proposed_kb_*.yaml` files.

### Phase 1: Move ephemera out of `kb/` (directory restructure)

```
BEFORE                                    AFTER
──────                                    ─────
kb/draft/{region}/references.json     →   references/{region}/references.json
kb/draft/{region}/field_mapping.json  →   research/{region}/
kb/draft/{region}/discovery_*.json    →   research/{region}/
kb/draft/{region}/reports/            →   reports/{region}/
kb/draft/{region}/traversal_output/   →   research/{region}/{run_id}/
kb/{region}/traversal_output/         →   research/{region}/{run_id}/
```

`references/` at repo root — the validation hook and report renderer need it; it's shared infrastructure, not ephemeral.

Update paths in: `validate_mapping_hook.py`, `render.py`, `justfile`, all workflow orchestrators, `CLAUDE.md`.

### Phase 2: Rename and consolidate graphs

| Current file | New name | Action |
|---|---|---|
| `hippocampus_GABA_stratum_oriens_stubs.yaml` | `hippocampus_WMBv1.yaml` | Rename |
| `CB_MLI_types.yaml` + `CB_PLI_types.yaml` | `cerebellum_WMBv1.yaml` | Merge (check for shared atlas nodes first) |
| `GPi_shell_neuron.yaml` | `BG_HMBA.yaml` | Rename |
| `GPi_shell_neuron_Mmus.yaml` | `BG_WMBv1.yaml` | Rename |

### Phase 3: Graduation criteria + enforcement

A graph graduates from `kb/draft/` to `kb/mappings/` when:
1. `just qc {file}` passes (schema valid, structural integrity, no placeholder snippets)
2. Every edge has ≥1 evidence item with a verified quote (not just `asta_report` status)
3. Every classical node has `species` populated
4. At least one edge has confidence ≥ MODERATE
5. Human has reviewed and approved (explicit sign-off in commit message or PR)

Deliverables:
- Criteria documented in `CONTRIBUTING.md`
- `just graduate {file}` recipe: runs checks, copies to `kb/mappings/`, reports pass/fail
- `WORKFLOW.md` updated with graduation as a documented step

### Phase 4: Update orchestrators

- `asta-report-ingest.md`: write classical node + edges into existing region graph (read-merge-write) rather than creating standalone `proposed_kb_*.yaml`
- `ingest-taxonomy.md`: write stubs into existing region graph or create new one
- `cite-traverse.md` + `evidence-extraction.md`: write to `research/` not `kb/`
- `gen-report.md`: read from `kb/`, write to `reports/`
- All orchestrators: read `references.json` from `references/{region}/`

### Deliverables summary

1. `kb/` contains only graph YAML (draft/ and mappings/)
2. `references/`, `research/`, `reports/` at repo root
3. Graph naming: `{region}_{atlas}.yaml`
4. Graduation criteria in `CONTRIBUTING.md` + `just graduate` recipe
5. All orchestrators + hooks updated for new paths
6. Existing content migrated; no data loss

---

## M8 — Taxonomy Reference DB

**Goal**: Replace fragment-based taxonomy ingestion with a local queryable database. Graph stubs are pulled on demand from the reference store rather than ingested in bulk.

**Status**: 🔲 Pending (depends on M7 — directory structure must be clean first)

### Problem

Current taxonomy ingest (`ingest-taxonomy.md`) takes a CSV/TSV slice and generates atlas stubs directly into the graph YAML. This creates two problems:

1. **Fragment inconsistency**: ingesting overlapping fragments at different times produces non-deterministic results (LLM-generated descriptions, field mapping choices). Merging on ID is unambiguous but metadata may conflict.
2. **Incomplete coverage**: each ASTA research run targets a narrow scope (e.g. GABAergic stratum oriens). Atlas types outside that scope are absent from the graph, even if relevant to mapping.

### Design: reference taxonomy as local DB

**Separate the taxonomy from the graph.** Ingest full taxonomies once into a local queryable store. When a mapping workflow needs candidate atlas types, query the store rather than scanning the graph.

```
inputs/taxonomies/
  WMBv1_hippocampus.json            # raw taxonomy slice (current)
  WMBv1_full.db                     # NEW: local SQLite (or similar) with full taxonomy

kb/draft/hippocampus/
  hippocampus_WMBv1.yaml            # graph: classical nodes + edges + only matched atlas stubs
```

### Workflow change

**Before (fragment ingest):**
1. Slice taxonomy CSV → `ingest-taxonomy.md` → atlas stubs written to graph YAML
2. Map classical types against stubs already in graph

**After (reference DB):**
1. Ingest full taxonomy → local DB (once, deterministic, no LLM involvement)
2. When mapping a classical type, query DB: "find WMBv1 clusters in region X with NT type Y and markers Z"
3. Promote matched candidates into graph as stubs (minimal, only what's needed)
4. Edges connect classical → promoted stubs as before

### Phased implementation

**Phase 1: DB format + ingest** (careful, foundational)
- Choose format: SQLite is simple, portable, no server dependency. Alternatives: DuckDB (better for analytical queries), plain JSON with index, OAK-compatible format.
- Write `src/evidencell/taxonomy_db.py`: ingest full taxonomy CSV/JSON → DB; query by region, NT type, markers, taxonomy level.
- `just ingest-taxonomy-db {taxonomy_file}` recipe: creates/updates the DB.
- Tests: round-trip ingest + query; verify determinism (same input → same DB).

**Phase 2: Query-based stub generation**
- Write `src/evidencell/stub_generator.py`: query taxonomy DB → generate atlas stub YAML nodes.
- `map-cell-type.md` orchestrator: instead of scanning graph for candidates, query DB first, then promote matches to graph.
- `asta-report-ingest.md`: after proposing classical node, query DB for candidate atlas types in the same region/NT.

**Phase 3: Migrate existing content**
- Rebuild `WMBv1_hippocampus.db` from current taxonomy JSON.
- Verify that existing graph stubs match DB query results.
- Remove stub-generation logic from `ingest-taxonomy.md`; redirect to DB path.
- `ingest-taxonomy.md` becomes: "ingest a taxonomy table into the reference DB" (no longer writes to KB graph).

**Phase 4: Formal KG sources (future, not yet scoped)**
- Some taxonomies have formal KG representations (e.g. CAS JSON, OWL exports from taxonomy teams).
- These could be ingested directly into the taxonomy DB alongside CSV sources.
- Avoid baking in a live dependency on an external KG service — use local snapshots stored in `inputs/taxonomies/`, versioned and reproducible.

### Open questions

1. **SQLite vs alternatives**: SQLite is the safe default (zero-config, portable, pip-installable). DuckDB is better for complex analytical queries but adds a dependency. JSON+index avoids any DB but limits query expressiveness.
2. **Schema for the taxonomy DB**: mirror the LinkML `CellTypeNode` fields (id, name, markers, region, NT type, taxonomy_level)? Or a flatter schema optimised for queries?
3. **Determinism guarantee**: the DB must be fully deterministic (same input → bit-identical output). No LLM involvement in ingest. Field mapping (taxonomy column → DB column) must be declared, not inferred.
4. **Multiple taxonomies**: the DB should support multiple atlases (WMBv1, HMBA, future). Partition by atlas name + version.
5. **Interaction with M6 (code/content separation)**: the taxonomy DB is shared infrastructure, not per-project content. It should stay on `main`, not on a content branch.

---

## Related documents

- [planning/citation_traversal_design.md](citation_traversal_design.md) — design space for citation traversal: ASTA snippets (primary), JATS/HTML/PDF fallbacks, passage location strategies, portable pipeline proposal
- [planning/asta_deepsearch_integration.md](asta_deepsearch_integration.md) — detailed integration plan for ASTA deepsearch component
- [paperqa2_cyberian/workflows/lit-review.md](https://github.com/Cellular-Semantics/paperqa2_cyberian/blob/Asta_experiments/workflows/lit-review.md) — literature review orchestrator workflow (Asta_deepsearch repo)
- [dismech-exptl-fork/CellSem_investigates.md](https://github.com/Cellular-Semantics/dismech-exptl-fork/blob/cellsem_notes_DONOTMERGE/CellSem_investigates.md) — dismech architecture reference
- [plan.md](../plan.md) — schema design, evidence taxonomy, worked examples
- [examples/scratch_notes.md](../examples/scratch_notes.md) — outstanding schema issues (review before M0)

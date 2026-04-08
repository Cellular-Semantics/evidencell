# evidencell Roadmap

> **Date**: 2026-03-31 (last updated)
> **Status**: M0–M3 implemented. M4 designed + mock-up complete, render.py implementation pending. M5 pending.

---

## Summary

| Milestone | Goal | Status | Key deliverables | Depends on |
|---|---|---|---|---|
| **M0** Schema Hardening | Fix schema issues; validator hook prototype | ✅ Done | Schema v0.5.4, pre-edit hook, 1 validated example | — |
| **M1** Repo Bootstrap | Create evidencell repo structure | ✅ Done | Repo, justfile, CLAUDE.md, ≥3 ported examples | M0 |
| **M2** Lit Review → KB | Deepsearch pipeline → evidence items + reference provenance | ✅ Done | ASTA ingest + cite-traverse + evidence-extraction workflows, references.json cache | M1 |
| **M3** Mapping Hypotheses | Propose mapping edges from evidence + taxonomy | ✅ Done | `map-cell-type.md` orchestrator, hippocampus + cerebellum draft mappings | M2 |
| **M4** Report Generation | Human-readable reports from draft mappings — MVP for biologists | 🔶 In progress | Three-tier architecture designed; hand-crafted OLM mock-up reports; `render.py` implementation pending | M3 |
| **M5** Cross-validation + Community | Annotation transfer feedback, compliance, GitHub review | 🔲 Pending | `AnnotationTransferEvidence` feedback loop, compliance scoring, PR review workflow | M4 |

M0 and M1 can proceed in parallel — the schema does not need to be finalised before the repo is bootstrapped; it can be iterated in place. M2 begins as soon as M1 has the repo structure.

---

## Cross-Cutting Discussion Points

### 1. LinkML schema strictness

The current schema (v0.4) is moderately strict: required fields enforced, enumerations for key controlled values (`MappingRelationship`, `MappingConfidence`, `EvidenceSupport`), ontology term bindings for CL/UBERON/NCBITaxon via `meaning` fields. However, it has not been validated end-to-end with `linkml-validate` yet — the discriminated union pattern (multiple evidence subtypes in a single list) is an untested corner.

**Recommended stance for evidencell**: *strict on structure, lenient on optional fields.* Required fields enforced by schema; optional metadata fields (scope, caveats) are not blocking but flagged by compliance scoring. This mirrors dismech's approach and keeps the correction loop tractable.

### 2. `just` vs Python for workflow logic

dismech uses `just` as a thin task runner wrapping Python/uv scripts.

**For `just`**: Proven pattern in dismech; humans and agents both understand `just qc`; composable recipes are easy to read.

**For more Python**: Agents and humans can read, debug, and modify Python more readily than justfile + shell; error handling and structured output are cleaner; complex logic (auto-flagging, extraction pipelines) is much easier in Python; testable with pytest.

**Recommendation**: Use `just` as the *interface layer* — named recipes like `just qc`, `just research-celltype`, `just fetch-reference` — but implement non-trivial logic as Python scripts in `src/evidencell/` invoked by `just`. Pure shell in justfile only for truly simple operations. This gives the human-readable command surface of `just` while keeping complex logic debuggable.

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
    annotation-transfer.md           # M5: import AT results→propose AnnotationTransferEvidence
  .claude/hooks/validate_mapping_hook.py
  .claude/skills/                    # bounded single-focus tasks, called interactively
    catalogue-weeding/               # present flagged catalogue; human pruning interaction
    celltype-mapping-pr-review/      # M5: review KB PR against rubric
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
**Status**: 🔶 Architecture designed; hand-crafted mock-ups complete; `render.py` implementation pending (2026-03-31).

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

### What remains (to close M4)

1. **`src/evidencell/render.py`** — implement the functions specified in `M4_report_generation.md`: `build_reference_index`, `fmt_atlas_query`, `render_summary`, `render_drilldown`, `render_index`, `_location_note`, `_candidate_verdict`, `_group_experiments`
2. **Justfile recipes** — `gen-report`, `gen-report-node`, `gen-drilldowns`, `gen-index`, `gen-report-all`
3. **End-to-end test** — run on OLM hippocampus case; verify output matches hand-crafted mock-ups; confirm no invented references or quotes

### Deferred (not M4)
- HTML rendering (Jinja2 → HTML) — deferred pending community need
- Report versioning via git log
- `workflows/gen-report.md` LLM synthesis orchestrator — programmatic render.py may be sufficient; defer if quality adequate
- Automated experiment structuring (schema extension to `proposed_experiments[]`) — M5

---

## M5 — Cross-Validation, Annotation Transfer Feedback, and Community Workflow

**Goal**: Close the experimental feedback loop — annotation transfer results proposed in M4 reports come back into the KB as `AnnotationTransferEvidence`, raising confidence where supported. Add compliance scoring and GitHub review workflow for community curation.

### Deliverables
- `AnnotationTransferEvidence` population workflow: take raw MapMyCells/Seurat/scANVI output (CSV/JSON) → extract per-taxonomy-level F1, purity, n_cells → propose `AnnotationTransferEvidence` YAML block → human confirms → append to KB
- Atlas paper citation traversal: extend M2 corpus to atlas papers not yet in `paper_catalogue.json` (for mapping-relevant atlas publications)
- Confidence update pass: re-run `just gen-report` after annotation transfer evidence is added — confidence may upgrade from MODERATE to HIGH
- Compliance scoring: per-mapping-graph field coverage, evidence completeness, CL term presence (`src/evidencell/compliance.py`)
- GitHub PR workflow: `celltype-mapping-pr-review` skill; auto-review on PR open; weekly compliance scan

### Annotation transfer feedback loop
The M4 report proposed experiments act as structured prompts for the biologist. When results come back:
1. Raw annotation transfer output file provided to the population workflow
2. Agent maps results to KB node IDs, extracts F1 per level
3. Proposes `AnnotationTransferEvidence` YAML block for human review
4. KB updated; report regenerated; confidence re-assessed

Note: annotation transfer is cross-species by design (mapping primate types to mouse WMBv1). `source_species` and `target_species` fields needed on `AnnotationTransferEvidence` — add at this milestone.

### Compliance dimensions
| Dimension | Metric |
|---|---|
| Schema completeness | Required fields present on all nodes and edges |
| Evidence coverage | ≥1 EvidenceItem per edge |
| Evidence diversity | ≥2 independent types for HIGH-confidence edges |
| CL term presence | Every node has at least a BROAD CL mapping |
| Reference validation | All LiteratureEvidence snippets validated against ASTA cache |
| Scope metadata | `species` + `developmental_stage` populated on ≥80% of evidence items |

### Tensions
- **Annotation transfer vs literature discordance**: if MapMyCells reports LOW confidence but literature strongly supports a mapping, the confidence decision guide needs a tiebreaker rule. Proposed: experimental evidence takes precedence over literature when they conflict, but the conflict must be documented as a caveat.
- **Expert bottleneck**: cell type mapping requires specialist knowledge (neuroscience, transcriptomics, atlas familiarity) that is harder to democratise than disease mechanism curation. The PR review workflow helps, but the bottleneck is real.
- **CL term currency**: CL is actively evolving. Record CL version at entry creation; run periodic term validation.

### Open questions
- Should `CROSS_SPECIES_EXTRAPOLATION` be a structured field on `MappingEdge` (more queryable) or remain a free-text caveat? A structured flag would allow systematic filtering.
- Should the evidencell KB be public from launch? Recommend yes — openness is a feature; early community feedback is valuable.

### GitHub workflow
Pattern from dismech:
- Curator opens PR with new/updated `kb/mappings/{region}/*.yaml`
- `claude-code-review.yml` runs the `celltype-mapping-pr-review` skill → inline comments on missing evidence, schema issues, imprecise CL terms
- Human expert does final approval
- `weekly-compliance.yaml` cron: finds lowest-compliance KB files, runs Claude to propose improvements, opens PR

### Open questions (additional)
- **Scale**: a full cerebellar atlas has ~60 cell types; full brain could exceed 3,000. At that scale the mapping hypothesis agent (M3) must be largely automated. Community curation alone will not be sufficient.
- **Relationship to existing resources**: evidencell should complement and link to Allen Brain Atlas annotations, CL, and BICAN cell type taxonomy — the evidence graph and explicit confidence levels are the contribution, not duplicating the atlases.

---

## Lessons from candelabrum cell pilot (2026-03-20)

Running lit-review.md end-to-end on a single seed (PMID:35578131, candelabrum cell) surfaced several issues and new capability needs. Items below are filed under the relevant milestone or as cross-cutting.

### M2 — lit-review workflow improvements

- **Full-text retrieval fallback chain**: artl-mcp `get_europepmc_full_text` silently returns empty on some confirmed-OA papers (e.g. PMC9548381). Need: Unpaywall OA pre-check (`api.unpaywall.org/v2/{doi}`) → artl-mcp full text → artl-mcp PDF-to-markdown → WebFetch PMC HTML (`pmc.ncbi.nlm.nih.gov/articles/{PMCID}/`) → WebFetch Unpaywall `best_oa_location.url`. Flag retrieval failures rather than silently falling back to abstract-only. JATS XML + local snippet generation being explored in parallel project (Asta_deepsearch).
- **Single-seed fast path**: skip selection step when there is one seed and max_depth≤1. The depth loop machinery (fetch→select→fetch) is designed for multi-seed broad traversal and adds pure overhead for targeted single-paper exploration.
- **ASTA snippet quality filtering**: ASTA `snippet_search` returns peer review comments alongside paper body text. Add filtering to exclude reviewer/response text (by snippetKind or section heuristic) before summarisation.
- **KB-first output**: the lit-review workflow currently terminates at `report.md`. Evidence extraction should be the primary output, with the report generated downstream from structured KB data. The report-first pattern created a dead end — `evidence-extraction.md` doesn't exist yet.
- **Citation traversal pipeline**: ASTA snippet_search (scoped to paper) is the primary mechanism when body text is indexed — provides pre-resolved citations with section labels. Fallback chain for papers without ASTA body text: JATS XML → PMC HTML DOM parsing → PDF+regex. All portable, pip-installable, no Grobid server. See [citation_traversal_design.md](citation_traversal_design.md) for full design.

### M2 — semantic validation loop for evidence placement

Iterative strategy that checks extracted evidence against the source paper for correct placement on KB nodes/edges. During the pilot, snRNA-seq cluster markers (Nxph1, Aldh1a3, Slc6a5) were initially placed on the `classical_candelabrum` node — but they were measured on the PLI1 transcriptomic cluster, not on morphologically confirmed candelabrum cells. The correction required recognising that smFISH on tissue with spatial co-registration to Oxtr-Cre-labelled CCs constitutes independent confirmation, while snRNA-seq cluster markers alone do not.

Key question the loop must answer: "is this evidence measured on this entity, or inferred via a mapping edge?" If inferred → place on the source node, record inference on the edge. Present placement decisions for review before writing.

### M3+ — spatial evidence from MERFISH data

- **MERFISH co-location scoring**: agentic workflow to compute co-location scores between cell types using WMBv1 MERFISH spatial data. Example: confirm that cluster 5178 cells co-localise with Purkinje neurons, providing independent spatial evidence for Purkinje layer placement beyond the coarse "CBX" atlas annotation (WMBv1 lacks laminar resolution). Manual inspection on the Allen Brain Cell Atlas website currently confirms strong co-location — automation would make this evidence type reproducible and scalable.
- **Allen Brain Cell Atlas link builder**: skill to generate deep links into the ABC website illustrating spatial placement of specific cell sets. Useful for manual QC and embedding visual evidence references in KB annotations.

### M5 — annotation transfer skill

Bounded skill for running MapMyCells annotation transfer between a source dataset and WMBv1, computing purity/F1 metrics, and writing structured `AnnotationTransferEvidence` to KB edges. Currently done manually in notebooks.

---

## Related documents

- [planning/citation_traversal_design.md](citation_traversal_design.md) — design space for citation traversal: ASTA snippets (primary), JATS/HTML/PDF fallbacks, passage location strategies, portable pipeline proposal
- [planning/asta_deepsearch_integration.md](asta_deepsearch_integration.md) — detailed integration plan for ASTA deepsearch component
- [paperqa2_cyberian/workflows/lit-review.md](https://github.com/Cellular-Semantics/paperqa2_cyberian/blob/Asta_experiments/workflows/lit-review.md) — literature review orchestrator workflow (Asta_deepsearch repo)
- [dismech-exptl-fork/CellSem_investigates.md](https://github.com/Cellular-Semantics/dismech-exptl-fork/blob/cellsem_notes_DONOTMERGE/CellSem_investigates.md) — dismech architecture reference
- [plan.md](../plan.md) — schema design, evidence taxonomy, worked examples
- [examples/scratch_notes.md](../examples/scratch_notes.md) — outstanding schema issues (review before M0)

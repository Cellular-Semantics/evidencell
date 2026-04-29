# evidencell Roadmap

**Format**: GFM task lists. `- [ ]` pending · `- [x]` done · `- [~]` in progress.
Priority: items are listed highest-priority-first within each section; **bold** = blocks other work.

Archive of prior roadmap with full milestone write-ups: [planning/ROADMAP_archive_2026-04.md](planning/ROADMAP_archive_2026-04.md)

---

## Tag glossary

| Tag | Scope |
|---|---|
| `#schema` | LinkML schema, enum values, semantic lint rules |
| `#kb` | KB file structure, naming conventions |
| `#content` | KB YAML content tasks — tracked in `planning/content-notes/` |
| `#lit` | Literature curation workflows generally |
| `#at` | Annotation transfer pipeline and report improvements |
| `#workflow-design` | Orchestrator architecture, data contracts |
| `#qc` | Validation hooks, compliance scoring, test coverage |
| `#community` | Biologist review tooling, compliance scoring, public access |
| `#infrastructure` | Packaging, CI, Docker, code/content separation |
| `#map-cell-type` | `workflows/map-cell-type.md` orchestrator |
| `#asta-ingest` | `workflows/asta-report-ingest.md` orchestrator |
| `#cite-traverse` | `.claude/skills/cite-traverse.md` (or current orchestrator) |
| `#evidence-extraction` | `workflows/evidence-extraction.md` orchestrator |
| `#survey` | `survey.md` orchestrator (not yet built) |
| `#targeted-search` | `targeted-search.md` orchestrator (not yet built) |
| `#gen-report` | `workflows/gen-report.md` + `render.py` |
| `#ingest-taxonomy` | `workflows/ingest-taxonomy.md` + `taxonomy_db.py` |
| `#annotation-transfer` | `workflows/annotation-transfer.md` orchestrator |

Milestones: `@Allen` (Allen Institute deliverable, date TBC) · `@BICAN` (BICAN deliverable, date TBC)

---

## Schema `#schema`

- [~] **Taxonomy rank encoding** — `taxonomy_rank: int` on `CellTypeNode` + `TaxonomyNodeList` `#ingest-taxonomy` `#map-cell-type`
  - [x] Schema fields + WMB YAML rank assignments (v0.7.1)
  - [x] `find_candidates()` accepts rank or level
- [ ] Review v0.8.0 schema additions — `PropertySource.source` rename candidate, WEAK vs PARTIAL, OVERLAPS vs PARTIAL_OVERLAP, CAS-specific fields on core `CellTypeNode`
- [ ] Marker/assay consistency — split `detected_molecule` + `assay_method`, or add SC1 lint check `#qc`
- [ ] Dual MBA + UBERON anatomy at ingest — annotate classical nodes with both IDs; shared `annotate-anatomy` skill `#asta-ingest` `#survey`
- [ ] Iterative mapping infrastructure — liberal initial writes, confidence upgrade, pruning with provenance trail, batch region-level review `#map-cell-type`
- [ ] Lint: marker type vs assay method in pre-edit hook (SC1) `#qc`
- [ ] Lint: flag mapping info in classical node notes (SC2) `#qc`
- [ ] Convention: no data in YAML comments (SC3) — add to CLAUDE.md

---

## KB structure `#kb`

- [ ] **Flatten kb/ — remove draft/mappings split**: single `kb/` directory; `just qc` + human sign-off as the quality gate `#kb`
- [ ] Wire remaining orchestrators to `references/`, `research/`, `reports/` at repo root `#asta-ingest` `#gen-report` `#evidence-extraction`
- [ ] Orchestrators write directly into region graph (read-merge-write); ephemera to `research/` `#asta-ingest` `#evidence-extraction`
- [ ] Self-contained KB graphs — inline snippets, `PublicationReference` metadata, ingest provenance (see [planning/schema_self_contained_references.md](planning/schema_self_contained_references.md)) `#schema`

---

## Precomputed stats HDF5 — download and file structure `#map-cell-type` `#annotation-transfer`

- [ ] **Verify HDF5 download in `at-download-taxonomy`** — the command runs `cd annotation_transfer && uv run annotation-transfer taxonomy-setup CCN20230722 --download` and writes to `annotation_transfer/conf/mapmycells/{id}/precomputed_stats.h5`. During the sexually_dimorphic mapping pilot, the download wrote to an empty directory because the working-directory shift means the file lands in `annotation_transfer/conf/mapmycells/` rather than the repo-root `conf/mapmycells/`. The existing file at `scratch/olm-at/precomputed_stats_ABC_revision_230821.h5` was found manually. Fix: either run `taxonomy-setup` from repo root, or symlink / update sync-mapmycells-paths to point to the actual file wherever it lives.
- [ ] **Standardise HDF5 canonical path** — define one authoritative location for `precomputed_stats.h5` per taxonomy (e.g. `conf/mapmycells/{taxonomy_id}/precomputed_stats.h5` from repo root) and document it in `CLAUDE.md` / orchestrator preamble. Agents and workflows that need the HDF5 should look there first, with a fallback scan. Currently the path is implicit and differs between runs.
- [ ] **Pre-run HDF5 check in `map-cell-type.md`** — add a Step 0 preflight: confirm `precomputed_stats.h5` and `conf/gene_mapping_{taxonomy_id}.tsv` exist; if not, print the download command and abort cleanly rather than silently skipping expression cross-check.

---

## Taxonomy DB queries `#ingest-taxonomy` `#map-cell-type`

- [ ] Update `query_by_region`, `query_by_nt`, `query_by_nt_propagated` to accept `taxonomy_rank`
- [ ] QC smoke tests: `--help` probes for new `taxonomy_ops` CLI subcommands `#qc`
- [ ] Verify supertype-level expression weighted mean logic in `test_taxonomy_ops.py` `#qc`

---

## Multi-taxonomy DB `#ingest-taxonomy` `#schema` `#map-cell-type`

Currently one taxonomy per DB file (`{taxonomy_id}.db`). With multiple atlases (WMBv1,
HMBA, future species), cross-taxonomy queries — especially for annotation transfer edges —
require either joining across DBs or consolidating into one.

**Core tension**: a single DB supports cross-taxonomy joins and keeps annotation transfer
edges queryable; separate DBs are simpler to ingest, version, and swap out independently.
Lean toward **single DB, partitioned by taxonomy_id** — the `taxonomy_id` column already
exists on every node row, so queries within a single atlas work unchanged.

- [ ] **Decide: single shared DB vs per-taxonomy DBs** — document the chosen model and its
  implications for `taxonomy_db_path()`, `build_from_yaml()`, and the skill `#workflow-design`
- [ ] If single DB: update `taxonomy_db_path()` to return a shared path (e.g.
  `kb/taxonomy/taxonomy.db`); `build_from_yaml()` upserts by taxonomy_id rather than
  dropping all nodes
- [ ] Cross-taxonomy candidate queries — `find_candidates()` needs a `taxonomy_ids` filter
  so callers can scope to one atlas or query across several `#map-cell-type`
- [ ] Cross-taxonomy annotation transfer edges in `MappingEdge` must explicitly record
  `source_taxonomy_id` and `target_taxonomy_id`; update schema + query skill `#schema`
- [ ] `reingest()` in `taxonomy_ops.py` must not clobber nodes from other taxonomies when
  updating a single atlas `#ingest-taxonomy`
- [ ] Update `_meta` table to track build timestamps per taxonomy_id (key:
  `taxonomy_built_at:{taxonomy_id}`) `#ingest-taxonomy`

---

## Literature curation `#lit`

- [ ] **Survey/targeted workflow split** — `survey.md` + `targeted-search.md` orchestrators; cite-traverse → skill; KB gap flags on nodes `#survey` `#targeted-search` `#cite-traverse` `#workflow-design` (see [planning/workflow_architecture_design.md](planning/workflow_architecture_design.md))
- [ ] Lit pipeline file schemas — Pydantic models for summary/refs/manifest; validated handovers between steps `#cite-traverse` `#evidence-extraction` `#workflow-design`
- [ ] Workflow handover contracts — handover inventory, schema coverage map, user-facing gate terminology `#workflow-design`
- [ ] Lit quality improvements — contextual retrieval for Round 2 papers, venue/citation quality signals, domain relevance pre-filters `#cite-traverse`

---

## Annotation transfer `#at`

- [ ] AT orchestrator: use `best_mapping_rank` throughout `#annotation-transfer` `#map-cell-type`
- [ ] AT-before-edges mapping loop — triage-first ordering, compute preflight gate, sub-node creation rule `#map-cell-type` `#annotation-transfer` (see [planning/adaptive_mapping_loop_design.md](planning/adaptive_mapping_loop_design.md))
- [ ] Report: assess all rank-0 nodes collectively when AT resolves above rank 0 `#gen-report`
- [ ] Workflow: agent-driven sub-node creation when source evidence separates subtypes `#map-cell-type`
- [ ] F1 heatmap visualisation in AT output / gen-report `#gen-report` `#annotation-transfer`
- [ ] Report: make classical-type provenance explicit for genetically/morphologically defined source data `#gen-report`
- [ ] Report: 10x cell count per cluster alongside MERFISH spatial cell count — investigate source (v2/v3 10x counts in taxonomy JSON; reliability flags needed before display); add to DB and render `#gen-report` `#ingest-taxonomy`
- [ ] Report: structured child-cluster concordance field on edges — add `child_concordance_summary` to edge schema so property alignment table can show "N/M children match" without relying on LLM prose synthesis `#schema` `#gen-report`
- [ ] Report: expression/annotation discrepancy as programmatic QC in gen-facts — flag when a DEFINING or NEUROPEPTIDE atlas marker shows near-zero precomputed expression vs. what atlas metadata annotates; emit structured `ATLAS_ANNOTATION_EXPRESSION_DISCREPANCY` item `#gen-report` `#qc`
- [ ] Report: ABC Atlas cell set linkouts — thread taxonomy node URLs (from download metadata) into rendered reports; document URL format `#gen-report` `#community`
- [ ] Report: ABC Atlas marker gene / combo linkouts — use existing code to generate query URLs for defining markers; add to candidate sections `#gen-report` `#community`
- [x] Report: minirefs author rendering — defensive `_coerce_authors()` in render.py + `_normalise_authors()` extended to handle string input + asta-report-ingest Step 2 prompt now spells out the field shape contract. Third instance of the asta-report-ingest free-form-writer class of bug (PMID prefix, DOI prefix, now authors shape — see [planning/asta_ingest_lessons_sexually_dimorphic.md](planning/asta_ingest_lessons_sexually_dimorphic.md) §1–2). Plan: [planning/minirefs_author_rendering_fix.md](planning/minirefs_author_rendering_fix.md). Medium-term structural fix subsumed by [planning/schema_self_contained_references.md](planning/schema_self_contained_references.md) Phase A `PublicationReference`. `#gen-report` `#asta-ingest`

---

## Workflow design `#workflow-design`

- [ ] **`map-cell-type.md` progressive rewrite** — direct KB writes; biologist report review is the main gate; remove per-edge curator gates except reference weeding `#map-cell-type`
- [x] **Fold expression cross-check into Step 0b refinement (default)** — Implemented: Steps 2a/2b/2c in `map-cell-type.md` now make expression enrichment mandatory (not optional). Step 0b refinement subagent prompt extended to enumerate child-cluster expression and AT evidence for every supertype candidate. `just build-taxonomy-db` called after any `add-expression` writes. `#map-cell-type`
- [ ] **DB regen performance check** — `just build-taxonomy-db {taxonomy_id}` is called after every `add-expression` run. If the rebuild is slow for large taxonomies, add a `--update-only` flag to `build_from_yaml()` that only re-inserts nodes whose YAML mtime has changed. `#map-cell-type`
- [x] **Sex bias scoring in `find-candidates`** — `find_candidates()` now accepts `optional_criteria: dict[str, str]`. The `_OPTIONAL_CRITERIA_REGISTRY` supports `sex_bias` (MFR < 0.3 → female, MFR > 3.0 → male, +1 pt at rank 0). `_cmd_find_candidates()` reads `sex_bias` from classical node YAML and passes as optional_criteria automatically. Extensible: new criteria added to registry without changing the call signature. Schema: `SexBias` enum added to `celltype_mapping.yaml`. `#find-candidates`
- [x] **Property alignment table in gen-report** — Section 4 of synthesis subagent prompt now requires a mandatory property alignment table (soma location, NT, expression, sex ratio, AT evidence) for each primary candidate. Headline null result required for UNCERTAIN-only mappings confirmed by expression data. `#gen-report`
- [ ] Curation mode vs dev mode — review workflow mode split (WORKFLOW.md / CLAUDE.md routing)
### Deliverables

1. **Contract inventory**: a table in `CLAUDE.md` (curation guide) documenting every inter-workflow handover — what file is passed, what workflow produces it, what workflow consumes it, and whether it has a formal schema.
2. **Schema coverage map**: for each handover, classify as: (a) LinkML-validated, (b) Pydantic-validated (from M2L), (c) prose-only, (d) unspecified. Target: zero (d), minimal (c).
3. **Inter-workflow handover specs**: Pydantic or LinkML models for the key handover objects that aren't already covered — especially `initial_summaries` format, proposed evidence items, and atlas metadata input.
4. **Graduation criteria**: formalise what it means to move content from `kb/draft/` to `kb/mappings/`. Currently "after just qc" — define precisely which checks must pass, whether intermediate workflow artifacts (cite_traverse/, evidence_extraction/) are retained or archived, and what the human review gate looks like.
5. **User-facing terminology**: replace internal jargon at workflow gates. "Add stubs and continue research" → "Expand scope: add newly discovered types". "Proceed to extraction" → "Lock down: extract evidence for current types". "Graduate" → "Promote to validated KB".

### Relationship to other milestones

- **M2L** feeds into WC: cite-traverse contracts are the first and most complex case. M2L solves it for lit search; WC generalises.
- **M6** (code/content separation) depends on WC: you can't cleanly separate content from code if the handover formats aren't stable.
- **Cross-cutting point #3** (file structure) in this roadmap is the seed discussion; WC is the actionable plan.

---

## Community feedback `#community`

- [ ] Biologist report review workflow — structured path from feedback → KB change with provenance `#gen-report`
- [ ] Compliance scoring in `src/evidencell/compliance.py`
- [ ] `celltype-mapping-pr-review` skill — rubric-based KB PR review
- [ ] GitHub Actions feasibility spike — hosted orchestrator execution on PR trigger `#infrastructure`

---

## Infrastructure `#infrastructure`

- [ ] Code/content separation — `content/hmba-mouse` branch; `main` fixture-only KB; `just test` green on main `#infrastructure`
- [ ] Docker setup — `docs/SETUP.md`, `just docker-setup`, `.env.example`

---

## Recently completed

Brief log — see [planning/ROADMAP_archive_2026-04.md](planning/ROADMAP_archive_2026-04.md) for full write-ups.

- [x] M0–M4: schema hardening, repo bootstrap, lit pipeline, mapping hypotheses, report generation
- [x] AT: OLM hippocampus end-to-end (GSE124847 → WMBv1); schema v0.6.0 (AnatomicalLocation + CellCompartment)
- [x] M8 Ph1: taxonomy SQLite DB + YAML ingest (CCN20230722); `taxonomy_db.py` `#ingest-taxonomy`
- [x] S1 (partial): `taxonomy_rank` schema + WMB rank assignments + `find_candidates` rank support
- [x] Taxonomy update ops: `add-expression`, `reingest` with field ownership (`taxonomy_ops.py`); `map-cell-type.md` Step 2b expression enrichment `#ingest-taxonomy` `#map-cell-type`
- [x] CAS taxonomy ingest: CTX-HPF CS202106160 + cross-taxonomy AT edges `#ingest-taxonomy` `#annotation-transfer`
- [x] Pre-commit hook: strict schema validation on all staged KB YAML `#qc`
- [x] Provenance schema unification (v0.8.0): `ElectrophysiologyProfile` + `MorphologyProfile` classes; `AnatomicalLocation.sources`; removed flat `ephys_sources`/`morphology_sources`/`location_sources` `#schema`

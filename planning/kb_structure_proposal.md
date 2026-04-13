# KB Structure Cleanup — Proposal

> **Date**: 2026-04-13
> **Status**: Draft proposal — for discussion before implementation
> **Context**: evidencell's `kb/` directory has become confusing. Workflow ephemera, intermediate artefacts, generated reports, reference caches, and actual KB graphs are all mixed together. Naming is inconsistent. Graduation criteria from `draft/` to `mappings/` are undefined. The hippocampus region has duplicate representations of OLM across multiple files.

---

## Fundamental differences from dismech

dismech provides a useful structural reference but evidencell faces challenges that don't exist in dismech:

### 1. Novel nodes vs ontology terms

dismech graphs connect diseases to **existing ontology terms** (MONDO, HP, GO, CL). Every node except the disease itself already exists in an external authority. File = one disease = one graph.

evidencell graphs are **full of novel nodes**. Atlas cluster stubs (e.g. `wmb_supt_0179`) are fragments of unpublished or newly published taxonomies with no ontology representation. Literature-defined cell types (e.g. `winterer_olm_2019`) are concepts from individual papers. Even classical types that map to CL terms carry novel evidence content. The graph is not a connector between known entities — it's a **synthesis of entities that mostly don't exist elsewhere yet**.

**Implication**: we can't adopt dismech's "one entity per file, everything else is ontology" pattern. Our graphs inherently contain multiple novel nodes.

### 2. Partial taxonomy ingestion

dismech ingests diseases one at a time from well-curated sources (MONDO). evidencell ingests **fragments of large taxonomies** — e.g. "all GABAergic supertypes and clusters in stratum oriens" from WMBv1 (61 nodes from a taxonomy of thousands). This is deliberate (narrows the search field for mapping), but it means:
- Atlas stub nodes are **shared infrastructure** within a region, not per-mapping-problem
- Multiple classical types in the same region map against the same pool of atlas stubs
- Adding a second classical type to a region means either adding to an existing graph or creating a second graph that shares stubs

### 3. Duplication across scopes

OLM currently exists in two places:
- `proposed_kb_hippocampus.yaml` (traversal output) — OLM classical node + `winterer_olm_2019` literature type, no atlas stubs
- `hippocampus_GABA_stratum_oriens_stubs.yaml` — OLM classical node + 61 atlas stubs with mapping edges

These are the *same* classical type at different stages of the pipeline. The stubs file is the result of merging the ASTA ingest output with taxonomy ingestion. But if we later run ASTA ingest for a second hippocampal classical type (e.g. bistratified cells), it could either:
- Get its own graph file (clean separation, but shares atlas stubs — duplication)
- Get added to the existing hippocampus graph (single source of truth for atlas stubs, but the file grows unboundedly)

This is the **core architectural tension**: the unit of curation is a mapping problem (classical type → atlas), but atlas stubs are shared across mapping problems in a region.

---

## Current file inventory (hippocampus)

| File | What it actually is | Should it be in `kb/`? |
|---|---|---|
| `hippocampus_GABA_stratum_oriens_stubs.yaml` | Working graph: 1 classical + 61 atlas stubs + edges | Yes — this is the KB graph |
| `references.json` | Provenance cache for quote validation | No — infrastructure, not KB |
| `field_mapping.json` | Taxonomy field translation metadata | No — workflow artefact |
| `discovery_candidates.json` | Classical type seed from ASTA | No — workflow artefact |
| `reports/*.md` | Generated human-readable reports | No — generated output |
| `traversal_output/*/` | Full audit trail of lit-review runs | No — workflow ephemera |

---

## Proposal

### Principle 1: `kb/` contains only graph YAML

Move everything else out:

```
kb/
  draft/{region}/{graph}.yaml        # working graphs
  mappings/{region}/{graph}.yaml     # graduated graphs

references/{region}/references.json  # quote store (at repo root, not in kb/)

research/{region}/{run_id}/          # traversal_output contents (renamed)
  run_config.json
  seeds.json
  depth_*_*.json
  all_summaries.json
  paper_catalogue.json
  report.md
  ...

reports/{region}/                    # generated Markdown reports
  {node_id}_summary.md
  {node_id}_drilldown_*.md
  index.md
```

`references/` at repo root because the validation hook and report renderer need it — it's infrastructure shared across workflows, not ephemeral per-run output.

### Principle 2: One graph per region, multiple classical types within it

Rather than one file per classical type (dismech pattern), use **one graph per region × atlas**:

```
kb/draft/hippocampus/hippocampus_WMBv1.yaml
kb/draft/cerebellum/cerebellum_WMBv1.yaml
kb/draft/BG/BG_HMBA.yaml
kb/draft/BG/BG_WMBv1.yaml
```

Rationale:
- Atlas stubs are shared within a region — deduplication is automatic
- Multiple classical types (OLM, bistratified, etc.) coexist in one graph
- Edges connect classical → atlas within the same file
- The graph is the **unit of LinkML validation** and the **unit of report generation**
- Matches the actual biology: a region's cell type landscape is interconnected

Trade-off: files get large for complex regions. But the current hippocampus file is already 158K with mostly-empty stubs — once stubs gain evidence the file will grow regardless. If a region exceeds ~500 nodes, consider splitting by subregion (e.g. `hippocampus_CA1_WMBv1.yaml`).

### Principle 3: Graph naming convention

`{region}_{atlas}.yaml` — e.g. `hippocampus_WMBv1.yaml`, `BG_HMBA.yaml`

This replaces:
- `hippocampus_GABA_stratum_oriens_stubs.yaml` (describes the search scope, not the graph)
- `GPi_shell_neuron.yaml` (describes one classical type, but the graph may grow)
- `CB_MLI_types.yaml` / `CB_PLI_types.yaml` (currently split by classical type — merge into `cerebellum_WMBv1.yaml`)

### Principle 4: Graduation criteria (draft → mappings)

A graph graduates from `kb/draft/` to `kb/mappings/` when:

1. `just qc {file}` passes (schema valid, structural integrity, no placeholder snippets)
2. Every edge has ≥1 evidence item with a verified quote (not just `asta_report` status)
3. Every classical node has `species` populated
4. At least one edge has confidence ≥ MODERATE
5. Human has reviewed and approved (explicit sign-off in commit message or PR)

These criteria should be documented in `CONTRIBUTING.md` and enforced by a `just graduate {file}` recipe that runs the checks and copies the file.

### Principle 5: Research runs are linked to graphs by metadata, not location

Currently, traversal_output directories sit inside `kb/` which makes them look like KB content. Move them to `research/{region}/{run_id}/` and add a `graph_file` field to `run_config.json` so the lineage is traceable:

```json
{
  "region": "hippocampus",
  "graph_file": "kb/draft/hippocampus/hippocampus_WMBv1.yaml",
  "run_id": "20260324_hippocampus_report_ingest",
  ...
}
```

Multiple runs for the same region are distinguishable by `run_id` (date-stamped). The graph file is the authoritative output; research runs are provenance.

---

## Migration plan (concrete steps)

### Phase 1: Move ephemera out of `kb/`

1. `mkdir -p references/hippocampus research/hippocampus research/cerebellum reports/hippocampus`
2. Move `kb/draft/hippocampus/references.json` → `references/hippocampus/references.json`
3. Move `kb/draft/hippocampus/field_mapping.json`, `discovery_candidates.json` → `research/hippocampus/`
4. Move `kb/draft/hippocampus/reports/` → `reports/hippocampus/`
5. Move `kb/draft/cerebellum/traversal_output/` → `research/cerebellum/`
6. Move `kb/hippocampus/traversal_output/` → `research/hippocampus/`
7. Delete `kb/hippocampus/` (now empty)
8. Update hooks + render.py to find `references.json` at new location
9. Update `justfile` recipes for new paths

### Phase 2: Rename and consolidate graphs

1. `hippocampus_GABA_stratum_oriens_stubs.yaml` → `hippocampus_WMBv1.yaml`
2. Merge `CB_MLI_types.yaml` + `CB_PLI_types.yaml` → `cerebellum_WMBv1.yaml`
3. `GPi_shell_neuron.yaml` → keep as is (or rename to `BG_HMBA.yaml` if it's the only BG/HMBA graph)
4. `GPi_shell_neuron_Mmus.yaml` → keep as is (or merge into `BG_WMBv1.yaml`)

### Phase 3: Document and enforce

1. Add graduation criteria to `CONTRIBUTING.md`
2. Add `just graduate {file}` recipe
3. Update `WORKFLOW.md` with new directory conventions
4. Update orchestrator workflows to write to `research/` not `kb/`

---

## Open questions

1. **Should `references/` be per-region or flat?** Per-region keeps the provenance local; flat would allow cross-region dedup. Per-region is simpler and matches current usage.

2. **Merging cerebellum files**: CB_MLI and CB_PLI are currently separate graphs with independent edges but some shared atlas context. Merging them is the right call structurally but needs care — do they share any atlas nodes?

3. **BG files**: the two BG files map the same classical type to different atlases (HMBA vs WMBv1). These should stay separate (`BG_HMBA.yaml`, `BG_WMBv1.yaml`) since the atlas is different.

4. **`proposed_kb_hippocampus.yaml` in traversal output**: this is a workflow intermediate that was absorbed into the stubs file. Once we move traversal_output to `research/`, it's clearly ephemeral. Delete or keep as provenance?

5. **Scale concern**: hippocampus already has 62 nodes. A full hippocampal GABAergic landscape might have 200+ atlas types and 20+ classical types. Is one file still the right unit? Alternative: subregion files (`hippocampus_CA1_WMBv1.yaml`), but this fragments the shared atlas stubs.
